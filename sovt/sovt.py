import sys  # nopep8
sys.path.append(".")  # nopep8
from cutools.HRM.hrm import HRM
from pathlib import Path
from calcs import Calcs
from plots import Plots
from data import Data
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

    def __init__(self, path_out_root, clean=False, make_plots=False):
        self.path_out_root = Path(path_out_root)
        self.clean = clean
        self.make_plots = make_plots
        self.data = Data(self)
        self.segs = None
        self.calcs = Calcs(self)

        self.plots = Plots(self)
        self.path_txt = Path.cwd() / Path("sovt/text_files")  # change this for final
        self.subjects = {}


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
        self.calcs.to_excel((self.segs, self.calcs.df_ss, self.calcs.df_comp),
                            ("Segments",
                             "Single Sensor Data",
                             "Composite Sensor Data"))
        
        # Generate line and spatio plots
        if self.make_plots:
            print("Generating plots...")
            # self.plots.lines()
            self.plots.spatio()

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
            folds 'text_files' and load each of those text files into hrm data
            objects. These are then stored in the subjects dictionary.

            Arguments:
            ----------
            None

            Returns:
            --------
        """
        # Loop through the text files in path_txt and import the data
        for file in self.path_txt.iterdir():
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
