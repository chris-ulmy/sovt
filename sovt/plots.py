from matplotlib import pyplot as plt


class Plots():
    """
        This class stores the methods for creating line plots and spatio
        temporal plots for each of the tasks in the sovt.segs dataframe. 
    """

    def __init__(self, sovt):
        self.sovt = sovt

    def lines(self):
        """
            This function generates a line plot graph for each task in the segs
            dataframe. It will plot multiple plos for each segment, one for each
            of the regions (Velum Pharynx UES Eso). These will be saved in the
            root directory provided by sovt.path_out_root property in the parent
            object.

            Arguments:
            ----------
            None

            Returns:
            --------
            None
        """

        regions = "Velum Pharynx UES Eso".split()
        segs = self.sovt.segs
        # Loop through each of the regions
        for region in regions:
            # Loop through each task in the segs dataframe
            for idx, task in segs.iterrows():
                # idx = (Subject, State, Task, Trial)
                # Retrieve the hrm data object from the subjects dictionary
                hrm = self.sovt.subjects[idx[0]]
                title = f"Subject {idx[0]}, {idx[1]}, {idx[2]}, Trial {idx[3]}, {region}"
                sensors = task[region]
                save_path = self.sovt.path_out_root
                save_path = save_path / str(idx[0]) / "Graphs" / "Line" / region
                # Create the folder that will contain the graphs
                save_path.mkdir(parents=True, exist_ok=True)
                save_file = f"{idx[1]}, {idx[2]}, Trial {idx[3]}, {region}.png"
                hrm.plot.line.create_overlay(
                    (task["Start"], task["Stop"]), sensors=sensors, title=title, show=False)
                hrm.plot.line.figure.savefig(
                    save_path/save_file, format="png", dpi=100)
                # Close the figure to save on memory
                plt.close(hrm.plot.line.figure)

    def spatio(self):
        """
            This will generate a spatiotemporal plot for each task in the segs
            dataframe. These will be saved in the root directory provided by
            sovt.path_out_root property in the parent object.

            Arguments:
            ----------
            None

            Returns:
            --------
            None
        """

        segs = self.sovt.segs
        # Loop through each  task in the segs dataframe
        for idx, task in segs.iterrows():
            # Retrieve the hrm data object from the subjects dictionary
            hrm = self.sovt.subjects[idx[0]]
            title = f"Subject {idx[0]}, {idx[1]}, {idx[2]}, Trial {idx[3]}"
            # Locate the first sensor of the Velum and the last sensor of the
            # UES
            sensor_start = task["Velum"][0]
            sensor_end = task["UES"][-1]
            # Include two superior sensors and include 3 more inferior sensors
            sensors = range(sensor_start-2, sensor_end+3)
            save_path = self.sovt.path_out_root
            save_path = save_path / str(idx[0]) / "Graphs" / "Spatio"
            # Create the folder that will contain the graphs
            save_path.mkdir(parents=True, exist_ok=True)
            save_file = f"{idx[1]}, {idx[2]}, Trial {idx[3]}.png"
            hrm.plot.spatio.create(
                (task["Start"], task["Stop"]), sensors=sensors, title=title, show=False)
            hrm.plot.spatio.figure.savefig(
                save_path/save_file, format="png", dpi=100)
            # Close the figure to save on memory
            plt.close(hrm.plot.spatio.figure)
