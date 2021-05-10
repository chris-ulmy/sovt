from pathlib import Path
import pandas as pd


class Calcs():
    """
        This class calculates all of the metrics for this specific research
        study. All data is saved and exported to an Exel file. Two versions
        of the Excel file are generated. One is for running statistics on
        and the other is for human reading.
    """

    def __init__(self, sovt):
        self.sovt = sovt
        self.df_ss = None
        self.df_comp = None
        self.df_trials = None

    def perform(self):
        """
            Performs calculations for all tasks listsed in the segs dataframe of
            the parent sovt class. Calculations include mean, median, max, min,
            standard deviation. This creates two new dataframes. One df_ss for
            single sensor metrics (the calculations will be performed for each
            sensor within each region of the segs dataframe). Another df_comp
            for composite metrics where the calculations are performed on each
            region as a whole. A third dataframe df_trials will average each
            task across all trials (ignoring any trials marked as ignore = 1).

            Note: In the composite sensor calculations only a single sensor or
            average of sensors is given. The rules for each situation are
            outlined here. 

            Velum: If multiple sensors in the region, the superior most sensor
            was chosen.

            Pharynx: All sensors are averaged in this region.

            UES: If multiple sensors in the region, the middle sensor is chosen.
            If there are an even number of sensors in the region the sensor with
            the highest mean pressure of the two middle sensors is chosen.

            Eso: Only a single sensor is chosen for this region at all times.


            Arguments:
            ----------
            None

            Returns:
            --------
            None 
        """

        # Determine whether to load previously caclulated data saved in a pickle
        # file or to create a clean data set.
        if self.sovt.clean:
            # Start a new file regardless.
            self._df_calcs()
        elif not Path(self.sovt.path_out_root / "data/comp.pkl").is_file():
            # Start a new file if comp.pkl does not exist.
            self._df_calcs()
        else:
            # Load the data from the pickle files.
            self.df_comp = pd.read_pickle(
                self.sovt.path_out_root / "data/comp.pkl")
            self.df_ss = pd.read_pickle(
                self.sovt.path_out_root / "data/ss.pkl")
            self.df_trials = pd.read_pickle(
                self.sovt.path_out_root / "data/trials.pkl")

    def to_excel(self, dfs, sheet_names):
        """
            This function will write multiple dataframes to Excel spreadsheets.
            Two different versions will be generated. Aggregate Data.xlsx which
            is the version with a collapsed index for easier readability. The
            same data is also copied into a second Excel spreadsheet called
            Stats Data.xlsx in which the index is exploded to make statistic
            analysis easier.

            Arguments:
            ----------
            dfs {iter, pandas dataframes} -- Iterable of pandas dataframes which
            correspond to each sheet that will be written.

            sheet_names {iter, strings} -- Iterable of strings which correspond
            to the sheet names that will be written.

            Returns:
            --------
            None
        """

        # Create the folder that will contain the graphs
        save_path = self.sovt.path_out_root / "data"
        save_path.mkdir(parents=True, exist_ok=True)

        # Check if the Excel files already exist.
        agg_file = save_path / "Aggregate Data.xlsx"
        stats_file = save_path / "Stats Data.xlsx"
        if self.sovt.clean:
            # Regardless create new Excel files
            self._make_excel(dfs, sheet_names)
        elif not agg_file.is_file() or not stats_file.is_file():
            # Neither Aggregate Data or Stats Data exists.
            self._make_excel(dfs, sheet_names)

    def _make_excel(self, dfs, sheet_names):
        """
            Private function to create the Excel file versions of the data. 

            Arguments:
            ----------
            dfs {iter, pandas dataframes} -- Iterable of pandas dataframes which
            correspond to each sheet that will be written.

            sheet_names {iter, strings} -- Iterable of strings which correspond
            to the sheet names that will be written.

            Returns:
            --------
            None
        """

        save_path = self.sovt.path_out_root / "data"
        agg_file = save_path / "Aggregate Data.xlsx"
        stats_file = save_path / "Stats Data.xlsx"

        with pd.ExcelWriter(agg_file) as agg:
            with pd.ExcelWriter(stats_file) as stats:
                for df, sheet_name in zip(dfs, sheet_names):
                    df.to_excel(agg, sheet_name=sheet_name, index=True)
                    df_no_idx = df.reset_index()
                    df_no_idx.to_excel(
                        stats, sheet_name=sheet_name, index=False)

    def _explode_df_ss(self):
        """
            This explodes the df_ss dataframe on the Sensor column. It populates
            the Sensor column with the list/iter of sensor numbers for that
            region. It then explodes that list to make a new row for each sensor
            that was in the original list. For example: for a particular
            task/trial the sensors in the Velumn are 8 and 9 which are saved the
            segs dataframe as [8, 9]. This list is moved into the df_ss
            dataframe and then exploded so that two rows now exist, one for 8
            and one for 9. Modifies the dataframe inplace. 

            Arguments: 
            ----------
            None

            Returns:
            --------
            None
        """

        # Loop through the rows in df_ss and populate the Sensor column with the
        # list of sensors stored in the segs dataframe.
        for idx, row in self.df_ss.iterrows():
            # Use the region portion of the index to find the appropriate column
            # in the segs dataframe.
            region = idx[4]
            sensors = self.sovt.segs.loc[idx[:-1], region]
            self.df_ss.at[idx, "Sensor"] = sensors

        # Explode the Sensor column.
        self.df_ss = self.df_ss.explode("Sensor")

    def _find_center(self, idx):
        """
            This function takes will segment the df_ss dataframe (based on idx),
            and determines the middle sensor to use. 

            If there are an even number of sensors in the segment, of the two
            middle sensors, it will locate the sensor with the greatest mean
            pressure. 

            If there are an odd number of sensors in the segment, it will find
            the middle sensor of that region. 

            Arguments:
            ----------
            idx {pandas index} -- Of the format (Subject, State, Task, Trial,
            Region)

            Returns:
            --------
            max_mean_sens {int} -- The sensor number of the middle sensor
        """

        # Set df to the segment of df_ss based on the idx provided.
        df = self.df_ss.loc[idx]
        df_len = len(df)

        # Calculate the index of the middle row.
        idx_middle1 = int(df_len / 2) - 1
        idx_middle2 = idx_middle1 + 1

        # Reset the index so that you can use numeric index instead of the
        # multiindex used by df_ss
        df = df.reset_index()
        df_middle = df.loc[idx_middle1:idx_middle2]
        if df_len % 2 == 0:
            # even number of rows, find max of mean
            max_mean_sens = df_middle.loc[df_middle["Mean"].idxmax(), "Sensor"]
        else:
            # odd number of rows, return middle
            max_mean_sens = df.loc[idx_middle2, "Sensor"]

        return max_mean_sens

    def _df_calcs(self):
        """
            Performs all the calculations as described in the class description.
            This will store the three dataframes in the df_comp, df_ss,
            df_trials class properties. 

            Arguments:
            ----------
            None

            Returns:
            --------
            None
        """

        # Set aliases for commonly used objects
        segs = self.sovt.segs
        subs = self.sovt.subjects

        # Setup the indexs and columns for each dataframe
        ss_idx = segs.index.names + ["Region", "Sensor"]
        comp_idx = segs.index.names + ["Region"]
        regions = "Velum Pharynx UES Eso".split()
        ss_cols = "Sensor Mean Median Max Min Sensor_Std Ignore".split()
        ss_cols = dict(zip(ss_cols, ["object"] + ["float"] * len(ss_cols)))
        comp_cols = "Sensor Mean Median Max Min Region_Std Ignore".split()
        comp_cols = dict(
            zip(comp_cols, ["object"] + ["float"] * len(comp_cols)))

        # Create the df_comp dataframe
        self.df_comp = pd.DataFrame(index=segs.index, columns=comp_cols.keys())
        # Set the data types for the columns
        self.df_comp = self.df_comp.astype(comp_cols)
        # Broadcast the list of regions by the length of self.df_comp
        self.df_comp["Region"] = [regions] * len(self.df_comp)
        # Explode this list to create a row for each item in the regions list.
        self.df_comp = self.df_comp.explode("Region")
        # Set a new index for self.df_comp to include the Region column.
        self.df_comp = self.df_comp.set_index(
            "Region", append=True).sort_index()

        # Create the self.df_ss dataframe
        self.df_ss = pd.DataFrame(
            index=self.df_comp.index, columns=ss_cols.keys())
        # Set the data types for the columns
        self.df_ss = self.df_ss.astype(ss_cols)
        # Explode self.df_ss by sensors
        self._explode_df_ss()

        # self.df_ss index = (Subject, State, Task, Trial, Region)
        # self.df_ss index later adds in 'Sensor' below
        # self.df_comp index = (Subject, State, Task, Trial, Region)

        # Group the self.df_comp on Subject, State, Task, Trial, Region
        for idx, sub_df in self.df_comp.groupby(level=comp_idx):
            # idx (Subject, State, Task, Trial, Region)
            subject = idx[0]
            region = idx[4]
            seg_idx = idx[:-1]
            # Get the HRM data object from the subs dictionary
            hrm = subs[subject]
            start = segs.loc[seg_idx, "Start"]
            stop = segs.loc[seg_idx, "Stop"]
            sensors = segs.loc[seg_idx, region]
            ignore = segs.loc[seg_idx, "Ignore"]

            # Get the pressure data. Don't use the full segment by providing
            # spatio=False argument
            z = self.sovt.get_segments(
                subject, (start, stop), sensors, full=False)
            # z, _ = hrm.get_segment((start, stop), sensors=sensors)

            # Calculate the metrics for each sensor using z (pandas dataframe)
            z_mean = z.mean(axis=0)
            z_median = z.median(axis=0)
            z_max = z.max(axis=0)
            z_min = z.min(axis=0)

            # Save the values in the dataframe
            self.df_ss.loc[idx, "Mean"] = z_mean.values
            self.df_ss.loc[idx, "Median"] = z_median.values
            self.df_ss.loc[idx, "Max"] = z_max.values
            self.df_ss.loc[idx, "Min"] = z_min.values
            self.df_ss.loc[idx, "Sensor_Std"] = z.std(axis=0).values
            # Duplicate the ignore value by the number of sensors
            self.df_ss.loc[idx, "Ignore"] = ignore * len(sensors)

            # Calculate the composite metrics (across sensors)
            if region == "Pharynx" or len(sensors) == 1:
                # The region is Pharynx or there is only 1 sensor
                if region == "Pharynx":
                    # For the pharynx region there is no single sensor, all are
                    # averaged, equivalent to the self.df_comp for Pharynx
                    sub_df.loc[idx, "Sensor"] = "NA"
                else:
                    # The region isn't the Pharynx so set the sensor to the the
                    # first sensor listed in the sensors list which should only
                    # be one sensor anyways.
                    sub_df.loc[idx, "Sensor"] = sensors[0]

                # Perform the composite calculations. If there was only one
                # sensor then z_mean will be scalar. Performing z_mean.mean() on
                # this scalar value yields a scalar value.
                sub_df.loc[idx, "Mean"] = z_mean.mean()
                sub_df.loc[idx, "Median"] = z_median.median()
                sub_df.loc[idx, "Max"] = z_max.max()
                sub_df.loc[idx, "Min"] = z_min.min()
                sub_df.loc[idx, "Region_Std"] = z.stack().std()
                sub_df.loc[idx, "Ignore"] = ignore
            elif region == "Velum" and len(sensors) > 1:
                # The region is Velum and there is more than one sensor.
                # Find the superior/caudal most sensor
                sensor = sensors[0]
                self._ss_calc(sensor, idx, sub_df, ignore)
            elif region == "UES" and len(sensors) > 1:
                # The region is UES and there is more than one sensor.
                # Find the center sensor
                center_sensor = self._find_center(idx)
                self._ss_calc(center_sensor, idx, sub_df, ignore)

            # Update the self.df_comp dataframe with the modified sub_df
            # assert id(sub_df) == id(sub_df2)
            self.df_comp.update(sub_df)

        # Add Sensor column to the self.df_ss dataframe index.
        self.df_ss = self.df_ss.set_index("Sensor", append=True).sort_index()

        # Perform the means across trials
        self._mean_trials()

        # Convert the Ignore column to int
        self.df_ss["Ignore"] = self.df_ss["Ignore"].astype("int")
        self.df_comp["Ignore"] = self.df_comp["Ignore"].astype("int")
        # self.df_trials["Ignore"] = self.df_trials["Ignore"].astype("int")

        # Create the folder that will contain the data
        save_path = self.sovt.path_out_root / "data"
        save_path.mkdir(parents=True, exist_ok=True)
        # Save the dataframes as pickle files
        self.df_comp.to_pickle(save_path / "comp.pkl")
        self.df_ss.to_pickle(save_path / "ss.pkl")
        self.df_trials.to_pickle(save_path / "trials.pkl")

    def _ss_calc(self, sensor, idx, sub_df, ignore):
        """
            Private function that performs the single sensor calculations on the
            sub_df dataframe for each sensor listed in the sub_df.

            Arguments:
            ----------
            sensor {int} -- sensor number on which to filter 

            idx {tuple} -- the index of the sub_df which corresponds to the
            index of df_ss dataframe

            sub_df {pandas.dataframe} -- the dataframe that will be modified in
            place to store the calculated metrics

            ignore {int} -- the integer 0 or 1 of whether this segment is
            ignored 

            Returns:
            --------
            None
        """

        # Create the index 'where' based on the task/trial and the
        # center sensor
        where = (self.df_ss.index == idx) & (
            self.df_ss["Sensor"] == sensor)
        sub_df.at[idx, "Sensor"] = sensor
        sub_df.at[idx, "Mean"] = self.df_ss.loc[where, "Mean"].values[0]
        sub_df.at[idx, "Median"] = self.df_ss.loc[where, "Median"].values[0]
        sub_df.at[idx, "Max"] = self.df_ss.loc[where, "Max"].values[0]
        sub_df.at[idx, "Min"] = self.df_ss.loc[where, "Min"].values[0]
        sub_df.at[idx, "Region_Std"] = self.df_ss.loc[where,
                                                      "Sensor_Std"].values[0]
        sub_df.at[idx, "Ignore"] = ignore

    def _mean_trials(self):
        """
            Private function that performs the mean over trials on the df_comp
            dataframe. This will group the df_comp on Subject, State, Task,
            Region. Yields a new dataframe df_trials stored in the class
            property df_trials.

            Arguments:
            ----------
            None

            Returns:
            --------
            None
        """

        group = ["Subject", "State", "Task", "Region"]
        cols = group + list(self.df_comp.columns)
        self.df_trials = pd.DataFrame(columns=cols)
        self.df_trials = self.df_trials.set_index(group)

        # Group the self.df_comp on Subject, State, Task, Region
        for idx, sub_df in self.df_comp.groupby(level=group):
            # idx (Subject, State, Task, Trial, Region)
            filtered = sub_df.loc[sub_df["Ignore"] == 0]
            means = filtered.mean()
            means.name = idx

            self.df_trials = self.df_trials.append(means, ignore_index=False)

        self.df_trials = self.df_trials.drop(
            labels=["Sensor", "Region_Std"], axis="columns")
