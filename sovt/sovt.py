from hrmtools.hrm import HRM
from pathlib import Path
from .calcs import Calcs
from .plots import Plots
from .data import Data
import pickle


class SOVT:
    """
        This class serves as the parent class to perform all calculations and
        generate all graphs for the "Measurement of pharyngeal air pressure
        during phonation using high-resolution manomtry" research study by
        Hoffmeister, Jesse; Ulmschneider, Christopher; Jones, Corinne; Cuicci,
        Michelle; McCulloch, Timothy

        Code written by Christopher Ulmschneider
    """

    def __init__(self, text_path, save_path, clean=False, make_plots=False):
        self.text_path = Path(text_path)
        self.path_out_root = Path(save_path)
        self.clean = clean
        self.make_plots = make_plots
        self.data = Data(self)
        self.segs = None
        self.calcs = Calcs(self)
        self.plots = Plots(self)
        self.subjects = {}
        self.interval_gap = 1
        self.interval_len = 2


    def run(self):
        """
            The main function for running all calculations and generating graphs.

            Arugments:
            ----------
            None

            Returns:
            --------
            None
        """

        # Load the data from the text files located in 'text_files' folder
        print("Loading data...")
        self.load_subjects()

        # Create the segments dataframe based on the data stored within the data
        # class
        self.data.dataframe()

        # Mark all segments that are too short or deemed not adequate for data
        # analysis to be ignored.
        self.data.process_segs()

        # Peform the calculations.
        print("Performing calculations...")
        self.calcs.perform()

        # Save all data to Excel spreadsheets. Makes two copies, human readable
        # and another for statistical analysis.
        print("Exporting data to Excel...")
        self.calcs.to_excel((self.segs, self.calcs.df_ss, self.calcs.df_comp, self.calcs.df_trials),
                            ("Segments",
                             "Single Sensor Data",
                             "Composite Sensor Data",
                             "Means Across Trials"))
        
        # Generate line and spatio plots
        if self.make_plots:
            print("Generating line plots...")
            self.plots.lines()
            print("Generating spatio-temporal plots...")
            self.plots.spatio()
        
        print("Completed all operations.")

    def load_subjects(self):
        """
            Loads all subjects into the subjects dictionary held in the subjects
            class property. If a pickle file does exist, this will be loaded
            instead of generating a new dictionary.

            Arguments: 
            ----------
            None

            Returns:
            --------
            None
        """

        if self.clean:
            # Run import regardless
            self._loadsub()
        elif not Path(self.path_out_root / "data/subjects.pkl").is_file():
            # Run import if file does not exist
            self._loadsub()
        else:
            # Load pickle data
            with open(self.path_out_root / "data/subjects.pkl", "rb") as file:
                self.subjects = pickle.load(file)

    def _loadsub(self):
        """
            Private function. Used to loop through all the text files in the
            text_path property and load each of those text files into hrm data
            objects. These are then stored in the subjects dictionary.

            Arguments:
            ----------
            None

            Returns:
            --------
        """
        # Loop through the text files in text_path and import the data
        for file in self.text_path.iterdir():
            if file.name == "dl_instructions":
                continue
            f_name_parts = file.name.split(" ", 1)
            sub_num = int(f_name_parts[0])

            hrm = HRM()
            hrm.import_data.from_text(file)
            self.subjects[sub_num] = hrm

        # Create the folder that will contain the data
        save_path = self.path_out_root / "data"
        save_path.mkdir(parents=True, exist_ok=True)
        with open(save_path / "subjects.pkl", "wb") as file:
            pickle.dump(self.subjects, file)

    def get_interval(self, time_seg, full=False):
        """
            This provides easy way to switch between the full data segment
            stored in the segs property that is used to graph the spatiotemporal
            plots, or the shortened interval requried for the calculations and
            line plots. The shortened interval will use the interval_gap and
            interval_len class properties to calculate the new interval.

            Arguments:
            ----------
            time_seg {iter float | iter string} -- Must be paired given as
            either float or string. Can be in the format of (78.3, 82.1) or as
            ("1:18.3", "1:22.1")

            full {bool} -- Boolean value that indicates whether the full segment
            (True) or the shortened segment (False) is returned.

            Returns:
            --------
            interval {tuple | float} -- tuple of lenth 2 containing the start
            and stop times
        """

        if full:
            # The full segment is required. 
            interval = time_seg
        else:
            # The shortened segment is required. Add the interval_gap to the
            # original start time
            start = time_seg[0] + self.interval_gap
            # Add the interval_len to the new start time
            stop = start + self.interval_len
            # If the new stop time is longer than the original segment, then use
            # the original stop time
            if stop > time_seg[1]:
                stop = time_seg[1]
        
            # Create the interval
            interval = (start, stop)

        return interval