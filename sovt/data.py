from pathlib import Path
import pandas as pd


class Data():
    def __init__(self, sovt):
        """
            This class contains the functions load and create a pandas dataframe
            which contains all of the raw data for each of the tasks. It also
            contains the sensor numbers located in the regions of interest (velum,
            pharnyx, UES, esophageal).
        """
        self.sovt = sovt

    def load(self):
        """
            Aggregates all raw data for each segment into a list of dictionaries
            which can be used to create a pandas dataframe. 

            Arguments:
            ----------
            None

            Returns:
            --------
            tasks_dict {dict} -- Dictionary containing raw segment data for all
            subjects.
        """

        # Subject Number, Task, Trial Number, State, Start, Stop, Velum, Pharynx, UES, Esophagus
        tasks = [
            [508, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 297.11, 314.15, [12], list(range(13, 19)), list(range(19, 23)), [29]],
            [508, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 332.35, 348.64, [11, 12], list(range(13, 19)), list(range(19, 23)), [29]],
            [508, "Comfortable Ah", 1, "Baseline", 379.73, 384.79, [12], list(range(13, 19)), list(range(19, 23)), [29]],
            [508, "Comfortable Ah", 2, "Baseline", 386.70, 391.88, [12], list(range(13, 19)), list(range(19, 23)), [29]],
            [508, "Comfortable Ah", 3, "Baseline", 394.30, 398.52, [12], list(range(13, 19)), list(range(19, 23)), [29]],
            [508, "Comfortable Ah", 1, "Arousal", 1039.25, 1044.05, [13], list(range(14, 19)), list(range(19, 23)), [29]],
            [508, "Comfortable Ah", 2, "Arousal", 1046.23, 1050.60, [13], list(range(14, 19)), list(range(19, 23)), [29]],
            [508, "Comfortable Ah", 3, "Arousal", 1052.51, 1057.02, [13], list(range(14, 19)), list(range(19, 23)), [29]],
            [508, "Soft Ah", 1, "Baseline", 409.25, 414.59, [12], list(range(13, 19)), list(range(19, 23)), [29]],
            [508, "Soft Ah", 2, "Baseline", 416.84, 421.58, [12], list(range(13, 19)), list(range(19, 23)), [29]],
            [508, "Soft Ah", 3, "Baseline", 423.70, 428.70, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "Soft Ah", 1, "Arousal", 1061.18, 1065.42, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "Soft Ah", 2, "Arousal", 1067.52, 1071.65, [13, 14], list(range(15, 21)), list(range(21, 24)), [29]],
            [508, "Soft Ah", 3, "Arousal", 1073.52, 1076.84, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "Loud Ah", 1, "Baseline", 433.23, 437.39, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "Loud Ah", 2, "Baseline", 440.09, 444.40, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "Loud Ah", 3, "Baseline", 447.54, 451.70, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "Loud Ah", 1, "Arousal", 1079.77, 1084.49, [13, 14], list(range(15, 19)), list(range(19, 23)), [29]],
            [508, "Loud Ah", 2, "Arousal", 1086.90, 1090.83, [13], list(range(14, 19)), list(range(19, 23)), [29]],
            [508, "Loud Ah", 3, "Arousal", 1094.71, 1097.82, [13, 14], list(range(15, 19)), list(range(19, 23)), [29]],
            [508, "Straw Phonation", 1, "Baseline", 474.56, 480.02, [13, 14], list(range(15, 21)), list(range(21, 23)), [29]],
            [508, "Straw Phonation", 2, "Baseline", 490.81, 496.08, [13, 14], list(range(15, 21)), list(range(21, 23)), [29]],
            [508, "Straw Phonation", 3, "Baseline", 498.59, 503.81, [13, 14], list(range(15, 22)), [22], [29]],
            [508, "Straw Phonation", 4, "Baseline", 506.38, 511.50, [13, 14], list(range(15, 22)), list(range(22, 24)), [29]],
            [508, "Straw Phonation", 1, "Arousal", 1110.89, 1115.09, [14, 15], list(range(16, 21)), list(range(21, 24)), [29]],
            [508, "Straw Phonation", 2, "Arousal", 1118.55, 1123.71, [14, 15], list(range(16, 21)), list(range(21, 24)), [29]],
            [508, "Straw Phonation", 3, "Arousal", 1125.75, 1130.77, [14, 15], list(range(16, 21)), list(range(21, 24)), [29]],
            [508, "Straw Blowing", 1, "Baseline", 515.92, 520.28,  [13, 14], list(range(15, 19)), list(range(19, 24)), [29]],
            [508, "Straw Blowing", 2, "Baseline", 523.30, 526.56, [13, 14], list(range(15, 19)), list(range(19, 24)), [29]],
            [508, "Straw Blowing", 3, "Baseline", 529.58, 533.14, [13, 14], list(range(15, 19)), list(range(19, 24)), [29]],
            [508, "Straw Blowing", 1, "Arousal", 1134.97, 1138.45, [14, 15], list(range(16, 21)), list(range(21, 24)), [29]],
            [508, "Straw Blowing", 2, "Arousal", 1141.39, 1145.06, [14, 15], list(range(16, 20)), list(range(20, 24)), [29]],
            [508, "Straw Blowing", 3, "Arousal", 1148.44, 1151.94, [14, 15], list(range(16, 20)), list(range(20, 24)), [29]],
            [508, "Bilabial Fricative", 1, "Baseline", 629.07, 633.51, [13], list(range(14, 20)), list(range(20, 22)), [29]],
            [508, "Bilabial Fricative", 2, "Baseline", 635.39, 639.10, [13], list(range(14, 20)), list(range(20, 22)), [29]],
            [508, "Bilabial Fricative", 3, "Baseline", 646.67, 651.35, [13], list(range(14, 20)), list(range(20, 22)), [29]],
            [508, "Bilabial Fricative", 4, "Baseline", 653.42, 658.34, [13], list(range(14, 20)), list(range(20, 22)), [29]],
            [508, "Bilabial Fricative", 5, "Baseline", 660.70, 665.38, [13], list(range(14, 20)), list(range(20, 22)), [29]],
            [508, "Bilabial Fricative", 1, "Arousal", 1225.45, 1230.56, [14], list(range(15, 23)), [23], [29]],
            [508, "Bilabial Fricative", 2, "Arousal", 1233.16, 1238.22, [14], list(range(15, 23)), [23], [29]],
            [508, "Bilabial Fricative", 3, "Arousal", 1240.65, 1245.18, [14], list(range(15, 23)), [23], [29]],
            [508, "Raspberry", 1, "Baseline", 598.46, 602.57, [13], list(range(14, 22)), list(range(22, 24)), [29]],
            [508, "Raspberry", 2, "Baseline", 605.90, 609.40, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "Raspberry", 3, "Baseline", 612.36, 616.31, [13], list(range(14, 22)), list(range(22, 24)), [29]],
            [508, "Raspberry", 1, "Arousal", 1200.71, 1204.83, [14], list(range(15, 23)), [23], [29]],
            [508, "Raspberry", 2, "Arousal", 1207.93, 1212.00, [14], list(range(15, 23)), [23], [29]],
            [508, "Raspberry", 3, "Arousal", 1214.63, 1219.11, [14], list(range(15, 23)), [23], [29]],
            [508, "Lip Trill", 1, "Baseline", 567.51, 571.67, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "Lip Trill", 2, "Baseline", 575.91, 579.67, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "Lip Trill", 3, "Baseline", 583.77, 587.83, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "Lip Trill", 1, "Arousal", 1175.89, 1180.20, [14], list(range(15, 23)), [23], [29]],
            [508, "Lip Trill", 2, "Arousal", 1182.35, 1186.84, [14], list(range(15, 23)), [23], [29]],
            [508, "Lip Trill", 3, "Arousal", 1189.10, 1193.75, [14, 15], list(range(16, 22)), list(range(22, 24)), [29]],
            [508, "M", 1, "Baseline", 736.71, 741.10, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "M", 2, "Baseline", 743.48, 748.01, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "M", 3, "Baseline", 750.48, 754.71, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "M", 1, "Arousal", 1253.34, 1257.62, [13], list(range(14, 20)), list(range(20, 25)), [29]],
            [508, "M", 2, "Arousal", 1259.33, 1263.82, [13], list(range(14, 21)), list(range(21, 25)), [29]],
            [508, "M", 3, "Arousal", 1265.93, 1270.78, [13], list(range(14, 21)), list(range(21, 25)), [29]],
            [508, "N", 1, "Baseline", 759.61, 763.80, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "N", 2, "Baseline", 765.98, 770.26, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "N", 3, "Baseline", 772.48, 776.74, [12], list(range(13, 20)), list(range(20, 23)), [29]],
            [508, "N", 1, "Arousal", 1273.90, 1278.35, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "N", 2, "Arousal", 1280.28, 1284.47, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [508, "N", 3, "Arousal", 1286.55, 1291.07, [13], list(range(14, 21)), list(range(21, 24)), [29]],
            [509, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 359.66, 382.76, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Resting Nasal Breathing 5 Cycles", 1, "Arousal", 1219.08, 1236.64, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 384.45, 406.48, [10], list(range(11, 18)), list(range(18, 22)), [24]],
            [509, "Resting Oral Breathing 5 Cycles", 1, "Arousal", 1237.36, 1251.74, [9], list(range(11, 17)), list(range(17, 22)), [24]],
            [509, "Comfortable Ah", 1, "Baseline", 425.29, 429.40, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Comfortable Ah", 2, "Baseline", 433.09, 437.35, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Comfortable Ah", 3, "Baseline", 442.56, 446.21, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Comfortable Ah", 1, "Arousal", 1269.78, 1273.70, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Comfortable Ah", 2, "Arousal", 1275.75, 1280.32, [9, 10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Comfortable Ah", 3, "Arousal", 1282.13, 1286.48, [9, 10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Soft Ah", 1, "Baseline", 452.76, 458.13, [10], list(range(11, 18)), list(range(18, 22)), [24]],
            [509, "Soft Ah", 2, "Baseline", 463.00, 467.76, [10], list(range(11, 18)), list(range(18, 22)), [24]],
            [509, "Soft Ah", 3, "Baseline", 469.99, 474.63, [10], list(range(11, 18)), list(range(18, 22)), [24]],
            [509, "Soft Ah", 1, "Arousal", 1289.52, 1294.03, [9, 10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Soft Ah", 2, "Arousal", 1295.52, 1300.13, [9, 10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Soft Ah", 3, "Arousal", 1301.97, 1306.33, [9, 10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Loud Ah", 1, "Baseline", 479.38, 484.11, [10], list(range(11, 18)), list(range(18, 22)), [24]],
            [509, "Loud Ah", 2, "Baseline", 486.96, 491.73, [10], list(range(11, 18)), list(range(18, 22)), [24]],
            [509, "Loud Ah", 3, "Baseline", 494.17, 498.47, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Loud Ah", 1, "Arousal", 1308.88, 1313.31, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Loud Ah", 2, "Arousal", 1315.09, 1319.45, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Loud Ah", 3, "Arousal", 1321.14, 1325.05, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Straw Phonation", 1, "Baseline", 514.06, 518.95, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Straw Phonation", 2, "Baseline", 523.89, 529.72, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Straw Phonation", 3, "Baseline", 533.10, 537.89, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Phonation", 4, "Baseline", 541.95, 546.93, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Straw Phonation", 1, "Arousal", 1337.85, 1342.26, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Phonation", 2, "Arousal", 1344.56, 1348.00, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Phonation", 3, "Arousal", 1351.50, 1356.17, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Blowing", 1, "Baseline", 552.16, 555.65, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Blowing", 2, "Baseline", 559.58, 564.65, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Blowing", 3, "Baseline", 567.63, 571.95, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Blowing", 1, "Arousal", 1359.32, 1363.00, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Blowing", 2, "Arousal", 1365.40, 1369.25, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Straw Blowing", 3, "Arousal", 1371.42, 1375.86, [10], list(range(11, 18)), list(range(18, 22)), [24]],
            [509, "Bilabial Fricative", 1, "Baseline", 760.08, 764.54, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Bilabial Fricative", 2, "Baseline", 767.85, 772.65, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Bilabial Fricative", 3, "Baseline", 775.44, 779.87, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Bilabial Fricative", 1, "Arousal", 1467.57, 1471.36, [10], list(range(11, 18)), list(range(18, 20)), [24]],
            [509, "Bilabial Fricative", 2, "Arousal", 1478.80, 1482.98, [10], list(range(11, 18)), list(range(18, 20)), [24]],
            [509, "Bilabial Fricative", 3, "Arousal", 1486.00, 1490.11, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Bilabial Fricative", 4, "Arousal", 1499.07, 1503.18, [10], list(range(11, 18)), list(range(18, 20)), [24]],
            [509, "Bilabial Fricative", 5, "Arousal", 1505.16, 1509.01, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Bilabial Fricative", 6, "Arousal", 1511.06, 1515.07, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Raspberry", 1, "Baseline", 648.00, 652.42, [10], list(range(11, 18)), list(range(18, 20)), [24]],
            [509, "Raspberry", 1, "Arousal", 1447.30, 1449.23, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "Raspberry", 2, "Arousal", 1453.89, 1456.60, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Lip Trill", 1, "Baseline", 600.22, 604.95, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Lip Trill", 2, "Baseline", 607.37, 611.44, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Lip Trill", 3, "Baseline", 620.36, 625.02, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "Lip Trill", 1, "Arousal", 1402.01, 1404.34, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Lip Trill", 2, "Arousal", 1406.46, 1410.62, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "Lip Trill", 3, "Arousal", 1413.28, 1417.44, [10], list(range(11, 18)), list(range(18, 21)), [24]],
            [509, "M", 1, "Baseline", 790.79, 794.50, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "M", 2, "Baseline", 799.25, 802.66, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "M", 3, "Baseline", 809.26, 814.21, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "M", 1, "Arousal", 1517.95, 1521.62, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "M", 2, "Arousal", 1522.76, 1526.73, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "M", 3, "Arousal", 1528.25, 1532.10, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "N", 1, "Baseline", 835.17, 839.16, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "N", 2, "Baseline", 841.96, 846.04, [10], list(range(11, 17)), list(range(17, 20)), [24]],
            [509, "N", 1, "Arousal", 1533.81, 1537.24, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "N", 2, "Arousal", 1538.66, 1542.15, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [509, "N", 3, "Arousal", 1543.82, 1547.75, [10], list(range(11, 17)), list(range(17, 21)), [24]],
            [510, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 319.71, 360.91, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 367.03, 395.43, [8], list(range(9, 15)), list(range(15, 19)), [24]],
            [510, "Comfortable Ah", 1, "Baseline", 404.24, 408.73, [8], list(range(9, 15)), list(range(15, 19)), [24]],
            [510, "Comfortable Ah", 2, "Baseline", 413.25, 417.95, [8], list(range(9, 14)), list(range(14, 18)), [24]],
            [510, "Comfortable Ah", 3, "Baseline", 421.18, 425.46, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Comfortable Ah", 1, "Arousal", 980.84, 985.00, [8, 9], list(range(10, 14)), list(range(14, 19)), [24]],
            [510, "Comfortable Ah", 2, "Arousal", 988.00, 992.44, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Comfortable Ah", 3, "Arousal", 995.03, 999.60, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Soft Ah", 1, "Baseline", 430.86, 436.20, [8], list(range(9, 14)), list(range(14, 18)), [24]],
            [510, "Soft Ah", 2, "Baseline", 437.69, 442.50, [8], list(range(9, 14)), list(range(14, 18)), [24]],
            [510, "Soft Ah", 3, "Baseline", 445.33, 450.03, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Soft Ah", 1, "Arousal", 1025.04, 1029.39, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Soft Ah", 2, "Arousal", 1031.63, 1035.83, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Soft Ah", 3, "Arousal", 1037.79, 1041.26, [8], list(range(9, 15)), list(range(15, 19)), [24]],
            [510, "Loud Ah", 1, "Baseline", 455.74, 460.60, [8], list(range(9, 14)), list(range(14, 18)), [24]],
            [510, "Loud Ah", 2, "Baseline", 462.76, 467.28, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Loud Ah", 3, "Baseline", 471.32, 475.25, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Loud Ah", 1, "Arousal", 1003.48, 1007.27, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Loud Ah", 2, "Arousal", 1009.78, 1014.09, [8, 9], list(range(10, 14)), list(range(14, 19)), [24]],
            [510, "Loud Ah", 3, "Arousal", 1016.45, 1021.33, [8, 9], list(range(10, 14)), list(range(14, 19)), [24]],
            [510, "Straw Phonation", 1, "Baseline", 508.49, 513.36, [8], list(range(9, 15)), list(range(15, 19)), [24]],
            [510, "Straw Phonation", 2, "Baseline", 515.31, 520.60, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Phonation", 3, "Baseline", 527.23, 531.14, [8], list(range(9, 15)), list(range(15, 19)), [24]],
            [510, "Straw Phonation", 4, "Baseline", 539.68, 545.07, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Phonation", 1, "Arousal", 1052.50, 1057.76, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Phonation", 2, "Arousal", 1059.77, 1065.08, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Phonation", 3, "Arousal", 1071.53, 1076.90, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Blowing", 1, "Baseline", 549.38, 554.37, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Blowing", 2, "Baseline", 558.54, 565.66, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Blowing", 3, "Baseline", 569.52, 574.55, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Blowing", 1, "Arousal", 1081.87, 1086.29, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Blowing", 2, "Arousal", 1092.91, 1098.11, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Straw Blowing", 3, "Arousal", 1102.56, 1107.69, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Bilabial Fricative", 1, "Baseline", 659.14, 663.67, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Bilabial Fricative", 2, "Baseline", 666.86, 671.56, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Bilabial Fricative", 3, "Baseline", 674.19, 678.17, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Bilabial Fricative", 1, "Arousal", 1179.01, 1183.89, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Bilabial Fricative", 2, "Arousal", 1186.59, 1190.93, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Bilabial Fricative", 3, "Arousal", 1194.10, 1199.18, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Raspberry", 1, "Baseline", 631.58, 636.23, [8, 9], list(range(10, 14)), list(range(14, 19)), [24]],
            [510, "Raspberry", 2, "Baseline", 640.68, 644.29, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "Raspberry", 3, "Baseline", 647.28, 651.21, [8, 9], list(range(10, 14)), list(range(14, 19)), [24]],
            [510, "Raspberry", 1, "Arousal", 1153.96, 1158.27, [8, 9], list(range(10, 14)), list(range(14, 19)), [24]],
            [510, "Raspberry", 2, "Arousal", 1161.85, 1166.34, [8, 9], list(range(10, 14)), list(range(14, 19)), [24]],
            [510, "Raspberry", 3, "Arousal", 1169.81, 1174.53, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Lip Trill", 1, "Baseline", 586.49, 589.33, [8, 9], list(range(10, 15)), list(range(15, 20)), [24]],
            [510, "Lip Trill", 2, "Baseline", 593.96, 598.16, [8, 9], list(range(10, 15)), list(range(15, 20)), [24]],
            [510, "Lip Trill", 3, "Baseline", 601.54, 605.09, [8, 9], list(range(10, 16)), list(range(16, 20)), [24]],
            [510, "Lip Trill", 1, "Arousal", 1115.31, 1120.10, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Lip Trill", 2, "Arousal", 1125.55, 1129.84, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Lip Trill", 3, "Arousal", 1133.82, 1139.01, [8, 9], list(range(10, 15)), list(range(15, 19)), [24]],
            [510, "Lip Trill", 4, "Arousal", 1144.70, 1148.59, [8, 9], list(range(10, 16)), list(range(16, 19)), [24]],
            [510, "M", 1, "Baseline", 687.73, 692.17, [8], list(range(9, 14)), list(range(14, 18)), [24]],
            [510, "M", 2, "Baseline", 693.68, 697.90, [8], list(range(9, 14)), list(range(14, 18)), [24]],
            [510, "M", 3, "Baseline", 699.29, 703.63, [8], list(range(9, 14)), list(range(14, 18)), [24]],
            [510, "M", 1, "Arousal", 1202.54, 1207.58, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "M", 2, "Arousal", 1211.32, 1216.67, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "M", 3, "Arousal", 1220.07, 1225.54, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "N", 1, "Arousal", 1229.86, 1234.42, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "N", 2, "Arousal", 1237.52, 1242.52, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [510, "N", 3, "Arousal", 1245.55, 1250.82, [8], list(range(9, 14)), list(range(14, 19)), [24]],
            [517, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 321.93, 348.64, [8], list(range(9, 16)), list(range(16, 20)), [25]],
            [517, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 355.00, 377.27, [8], list(range(9, 16)), list(range(16, 20)), [25]],
            [517, "Comfortable Ah", 1, "Baseline", 404.81, 408.31, [8], list(range(9, 17)), list(range(17, 21)), [25]],
            [517, "Comfortable Ah", 2, "Baseline", 410.93, 414.77, [8], list(range(9, 17)), list(range(17, 21)), [25]],
            [517, "Comfortable Ah", 3, "Baseline", 416.84, 420.22, [8], list(range(9, 17)), list(range(17, 21)), [25]],
            [517, "Comfortable Ah", 1, "Arousal", 967.86, 970.98, [8], list(range(9, 17)), list(range(17, 21)), [25]],
            [517, "Comfortable Ah", 2, "Arousal", 972.80, 976.05, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "Comfortable Ah", 3, "Arousal", 977.54, 980.84, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Soft Ah", 1, "Baseline", 423.69, 427.44, [8], list(range(9, 17)), list(range(17, 22)), [25]],
            [517, "Soft Ah", 2, "Baseline", 429.18, 433.0, [8], list(range(9, 17)), list(range(17, 22)), [25]],
            [517, "Soft Ah", 3, "Baseline", 434.46, 438.48, [8], list(range(9, 17)), list(range(17, 22)), [25]],
            [517, "Soft Ah", 1, "Arousal", 983.22, 986.03, [8, 9], list(range(10, 18)), list(range(18, 21)), [25]],
            [517, "Soft Ah", 2, "Arousal", 987.92, 991.72, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "Soft Ah", 3, "Arousal", 992.80, 995.77, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "Loud Ah", 1, "Baseline", 441.88, 445.37, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Loud Ah", 2, "Baseline", 447.39, 450.91, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Loud Ah", 3, "Baseline", 452.96, 456.69, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Loud Ah", 1, "Arousal", 997.87, 1001.14, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "Loud Ah", 2, "Arousal", 1002.55, 1005.87, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Loud Ah", 3, "Arousal", 1007.25, 1010.50, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Straw Phonation", 1, "Baseline", 535.70, 539.82,[8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "Straw Phonation", 2, "Baseline", 541.78, 546.33,[8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "Straw Phonation", 3, "Baseline", 548.31, 552.48,[8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "Straw Phonation", 1, "Arousal", 1046.00, 1049.37,[8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "Straw Phonation", 2, "Arousal", 1051.06, 1054.86,[8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Straw Phonation", 3, "Arousal", 1056.25, 1059.95,[8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Straw Blowing", 1, "Baseline", 559.45, 562.53,[8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Straw Blowing", 2, "Baseline", 570.22, 574.05,[8, 9], list(range(10, 19)), list(range(19, 22)), [25]],
            [517, "Straw Blowing", 3, "Baseline", 577.25, 581.14,[8, 9], list(range(10, 19)), list(range(19, 22)), [25]],
            [517, "Straw Blowing", 1, "Arousal", 1063.47, 1066.37,[8, 9, 10], list(range(11, 18)), list(range(18, 22)), [25]],
            [517, "Straw Blowing", 2, "Arousal", 1067.95, 1070.87,[8, 9, 10], list(range(11, 18)), list(range(18, 22)), [25]],
            [517, "Straw Blowing", 3, "Arousal", 1072.82, 1076.41,[8, 9, 10], list(range(11, 18)), list(range(18, 21)), [25]],
            [517, "Bilabial Fricative", 1, "Baseline", 670.48, 673.86, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "Bilabial Fricative", 2, "Baseline", 676.08, 679.38, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Bilabial Fricative", 1, "Arousal", 1134.62, 1138.06, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Bilabial Fricative", 2, "Arousal", 1139.94, 1143.13, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Bilabial Fricative", 3, "Arousal", 1144.76, 1148.18, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "Raspberry", 1, "Baseline", 642.74, 645.55, [8, 9], list(range(10, 18)), list(range(18, 21)), [25]],
            [517, "Raspberry", 2, "Baseline", 647.85, 650.39, [8, 9], list(range(10, 18)), list(range(18, 21)), [25]],
            [517, "Raspberry", 3, "Baseline", 652.83, 655.35, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Raspberry", 1, "Arousal", 1117.98, 1119.97, [8, 9], list(range(10, 17)), list(range(17, 22)), [25]],
            [517, "Raspberry", 2, "Arousal", 1121.86, 1123.84, [8, 9], list(range(10, 17)), list(range(17, 22)), [25]],
            [517, "Raspberry", 3, "Arousal", 1126.21, 1128.32, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Lip Trill", 1, "Baseline", 617.16, 620.57, [9], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "Lip Trill", 2, "Baseline", 623.11, 626.84, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Lip Trill", 3, "Baseline", 630.39, 633.35, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Lip Trill", 1, "Arousal", 1099.93, 1103.39, [8, 9], list(range(10, 18)), list(range(18, 22)), [25]],
            [517, "Lip Trill", 2, "Arousal", 1105.41, 1108.48, [9], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "Lip Trill", 3, "Arousal", 1110.52, 1114.13, [9], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "M", 1, "Baseline", 683.71, 687.01, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "M", 2, "Baseline", 688.26, 691.96, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "M", 3, "Baseline", 693.38, 696.39, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "M", 1, "Arousal", 1151.64, 1153.50, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "M", 2, "Arousal", 1156.04, 1159.39, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "M", 3, "Arousal", 1160.84, 1164.26, [8], list(range(9, 18)), list(range(18, 22)), [25]],
            [517, "N", 1, "Baseline", 698.00, 700.67, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "N", 2, "Baseline", 701.94, 704.98, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "N", 1, "Arousal", 1166.11, 1169.23, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "N", 2, "Arousal", 1170.54, 1173.67, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [517, "N", 3, "Arousal", 1175.03, 1178.33, [8], list(range(9, 18)), list(range(18, 21)), [25]],
            [518, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 430.36, 459.85, [8, 9], list(range(10, 15)), list(range(15, 20)), [26]],
            [518, "Resting Nasal Breathing 5 Cycles", 1, "Arousal", 1133.29, 1156.76, [8, 9], list(range(10, 15)), list(range(15, 20)), [26]],
            [518, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 463.54, 491.20, [8, 9], list(range(10, 15)), list(range(15, 20)), [26]],
            [518, "Resting Oral Breathing 5 Cycles", 1, "Arousal", 1162.73, 1179.64, [8, 9], list(range(10, 15)), list(range(15, 20)), [26]],
            [518, "Comfortable Ah", 1, "Baseline", 510.81, 515.73, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Comfortable Ah", 2, "Baseline", 518.75, 523.67, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Comfortable Ah", 3, "Baseline", 527.04, 531.91, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Comfortable Ah", 1, "Arousal", 1187.03, 1191.29, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Comfortable Ah", 2, "Arousal", 1193.26, 1197.73, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Comfortable Ah", 3, "Arousal", 1199.83, 1204.17, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Soft Ah", 1, "Baseline", 594.18, 598.04, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Soft Ah", 2, "Baseline", 600.92, 604.27, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Soft Ah", 3, "Baseline", 607.80, 611.31, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Soft Ah", 1, "Arousal", 1208.61, 1212.41, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Soft Ah", 2, "Arousal", 1214.32, 1218.57, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Soft Ah", 3, "Arousal", 1220.47, 1224.30, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Loud Ah", 1, "Baseline", 551.36, 555.74, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Loud Ah", 2, "Baseline", 559.40, 563.01, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Loud Ah", 3, "Baseline", 565.92, 569.58, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Loud Ah", 1, "Arousal", 1227.13, 1230.60, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Loud Ah", 2, "Arousal", 1232.30, 1235.92, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Loud Ah", 3, "Arousal", 1238.34, 1241.60, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Phonation", 1, "Baseline", 649.08, 652.57, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Phonation", 2, "Baseline", 657.23, 662.29, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Phonation", 3, "Baseline", 664.87, 670.08, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Phonation", 4, "Baseline", 672.94, 678.43, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Phonation", 1, "Arousal", 1251.28, 1255.50, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Phonation", 2, "Arousal", 1257.04, 1261.60, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Phonation", 3, "Arousal", 1262.99, 1267.84, [8, 9, 10], list(range(11, 17)), list(range(17, 21)), [26]],
            [518, "Straw Blowing", 1, "Baseline", 682.48, 686.46,  [8, 9], list(range(10, 16)), list(range(16, 21)), [26]],
            [518, "Straw Blowing", 2, "Baseline", 688.86, 693.17, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Blowing", 3, "Baseline", 695.31, 699.60, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Straw Blowing", 1, "Arousal", 1270.89, 1275.02, [8, 9], list(range(10, 16)), list(range(16, 21)), [26]],
            [518, "Straw Blowing", 2, "Arousal", 1276.56, 1280.10, [8, 9], list(range(10, 16)), list(range(16, 21)), [26]],
            [518, "Straw Blowing", 3, "Arousal", 1282.45, 1286.73, [8, 9, 10], list(range(11, 16)), list(range(16, 21)), [26]],
            [518, "Bilabial Fricative", 1, "Baseline", 855.21, 859.57, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 2, "Baseline", 863.29, 867.96, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 3, "Baseline", 870.23, 874.73, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 1, "Arousal", 1356.87, 1360.75, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 2, "Arousal", 1364.66, 1368.82, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 3, "Arousal", 1373.41, 1377.47, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 4, "Arousal", 1379.04, 1382.67, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 5, "Arousal", 1384.10, 1388.10, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 6, "Arousal", 1391.68, 1395.83, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 7, "Arousal", 1401.95, 1406.10, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Bilabial Fricative", 8, "Arousal", 1446.09, 1450.64, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Raspberry", 1, "Baseline", 779.75, 783.65, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Raspberry", 2, "Baseline", 786.18, 789.60, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Raspberry", 3, "Baseline", 791.51, 795.67, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Raspberry", 1, "Arousal", 1336.68, 1339.78, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Raspberry", 2, "Arousal", 1341.21, 1344.77, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Raspberry", 3, "Arousal", 1346.49, 1349.82, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "Lip Trill", 1, "Baseline", 745.01, 746.99, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Lip Trill", 2, "Baseline", 750.02, 754.44, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Lip Trill", 3, "Baseline", 757.06, 761.28, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Lip Trill", 4, "Baseline", 763.01, 767.93, [8, 9], list(range(10, 18)), list(range(18, 21)), [26]],
            [518, "Lip Trill", 1, "Arousal", 1308.32, 1310.52, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Lip Trill", 2, "Arousal", 1311.45, 1315.02, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Lip Trill", 3, "Arousal", 1317.25, 1320.77, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "Lip Trill", 4, "Arousal", 1322.27, 1326.11, [8, 9], list(range(10, 18)), list(range(18, 20)), [26]],
            [518, "M", 1, "Baseline", 883.43, 887.37, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "M", 2, "Baseline", 891.40, 894.08, [8], list(range(9, 16)), list(range(16, 20)), [26]],
            [518, "M", 3, "Baseline", 897.28, 900.22, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "M", 1, "Arousal", 1412.09, 1415.87, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "M", 2, "Arousal", 1417.25, 1421.40, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "M", 3, "Arousal", 1422.51, 1426.56, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "N", 1, "Baseline", 903.95, 908.11, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "N", 2, "Baseline", 910.28, 914.48, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "N", 3, "Baseline", 916.42, 920.60, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "N", 1, "Arousal", 1428.37, 1431.80, [8], list(range(9, 16)), list(range(16, 20)), [26]],
            [518, "N", 2, "Arousal", 1432.99, 1436.01, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [518, "N", 3, "Arousal", 1437.28, 1440.61, [8, 9], list(range(10, 16)), list(range(16, 20)), [26]],
            [519, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 334.88, 366.28, [9, 10], list(range(11, 19)), list(range(19, 22)), [26]],
            [519, "Resting Nasal Breathing 5 Cycles", 1, "Arousal", 975.23, 995.54, [9, 10, 11], list(range(12, 18)), list(range(18, 22)), [26]],
            [519, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 375.35, 397.06, [9, 10, 11], list(range(12, 18)), list(range(18, 22)), [26]],
            [519, "Resting Oral Breathing 5 Cycles", 1, "Arousal", 1003.16, 1025.30, [9, 10, 11], list(range(12, 18)), list(range(18, 22)), [26]],
            [519, "Comfortable Ah", 1, "Baseline", 409.69, 414.82, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Comfortable Ah", 2, "Baseline", 418.79, 424.35, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Comfortable Ah", 3, "Baseline", 426.71, 432.18, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Comfortable Ah", 1, "Arousal", 1036.97, 1040.93, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Comfortable Ah", 2, "Arousal", 1043.07, 1047.26, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Comfortable Ah", 3, "Arousal", 1049.34, 1053.04, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Soft Ah", 1, "Baseline", 441.87, 446.76, [11], list(range(12, 19)), list(range(19, 23)), [26]],
            [519, "Soft Ah", 2, "Baseline", 449.76, 454.91, [11], list(range(12, 19)), list(range(19, 23)), [26]],
            [519, "Soft Ah", 3, "Baseline", 456.92, 462.21, [11], list(range(12, 19)), list(range(19, 23)), [26]],
            [519, "Soft Ah", 1, "Arousal", 1056.82, 1060.88, [11], list(range(12, 19)), list(range(19, 23)), [26]],
            [519, "Soft Ah", 2, "Arousal", 1062.81, 1066.89, [11], list(range(12, 19)), list(range(19, 23)), [26]],
            [519, "Soft Ah", 3, "Arousal", 1069, 1073.09, [11], list(range(12, 19)), list(range(19, 23)), [26]],
            [519, "Loud Ah", 1, "Baseline", 467.63, 473.15, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Loud Ah", 2, "Baseline", 475.33, 480.21, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Loud Ah", 3, "Baseline", 482.15, 487.67, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Loud Ah", 1, "Arousal", 1075.26, 1079.69, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Loud Ah", 2, "Arousal", 1081.29, 1085.67, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Loud Ah", 3, "Arousal", 1087.07, 1091.22, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Straw Phonation", 1, "Baseline", 503.54, 508.54, [11], list(range(12, 21)), list(range(21, 23)), [26]],
            [519, "Straw Phonation", 2, "Baseline", 511.16, 516.27, [11], list(range(12, 21)), list(range(21, 23)), [26]],
            [519, "Straw Phonation", 3, "Baseline", 518.36, 523.63, [11, 12], list(range(13, 21)), list(range(21, 23)), [26]],
            [519, "Straw Phonation", 1, "Arousal", 1102.86, 1107.35, [11, 12], list(range(13, 21)), list(range(21, 23)), [26]],
            [519, "Straw Phonation", 2, "Arousal", 1109.43, 1114.08, [12], list(range(13, 21)), list(range(21, 23)), [26]],
            [519, "Straw Phonation", 3, "Arousal", 1115.89, 1120.38, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Straw Blowing", 1, "Baseline", 528.32, 532.12,  [11, 12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Straw Blowing", 2, "Baseline", 535.84, 540.12, [11, 12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Straw Blowing", 3, "Baseline", 543.10, 547.58, [11, 12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Straw Blowing", 1, "Arousal", 1123.36, 1126.60, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Straw Blowing", 2, "Arousal", 1129.87, 1134.26, [12, 13], list(range(14, 21)), list(range(21, 24)), [26]],
            [519, "Bilabial Fricative", 1, "Baseline", 647.68, 652.23, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Bilabial Fricative", 2, "Baseline", 654.81, 659.58, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Bilabial Fricative", 3, "Baseline", 662, 666.64, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Bilabial Fricative", 1, "Arousal", 1217.07, 1221.31, [12, 13], list(range(14, 21)), list(range(21, 24)), [26]],
            [519, "Bilabial Fricative", 2, "Arousal", 1223.03, 1227.47, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Bilabial Fricative", 3, "Arousal", 1229.14, 1233.25, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Raspberry", 1, "Baseline", 621.19, 625.38, [11, 12, 13], list(range(14, 21)), list(range(21, 24)), [26]],
            [519, "Raspberry", 2, "Baseline", 627.59, 632.26, [11, 12], list(range(13, 21)), list(range(21, 23)), [26]],
            [519, "Raspberry", 3, "Baseline", 637.58, 641.80, [12, 13], list(range(14, 19)), list(range(19, 23)), [26]],
            [519, "Raspberry", 1, "Arousal", 1197.11, 1201.56, [11, 12, 13], list(range(14, 19)), list(range(19, 23)), [26]],
            [519, "Raspberry", 2, "Arousal", 1203.55, 1207.84, [12, 13], list(range(14, 19)), list(range(19, 23)), [26]],
            [519, "Raspberry", 3, "Arousal", 1209.68, 1214.00, [12, 13], list(range(14, 19)), list(range(19, 23)), [26]],
            [519, "Lip Trill", 1, "Baseline", 599.42, 603.73, [11, 12, 13], list(range(14, 19)), list(range(19, 23)), [26]],
            [519, "Lip Trill", 2, "Baseline", 605.93, 610.35, [11, 12, 13], list(range(14, 19)), list(range(19, 23)), [26]],
            [519, "Lip Trill", 3, "Baseline", 612.48, 617.03, [12, 13], list(range(14, 21)), list(range(21, 23)), [26]],
            [519, "Lip Trill", 1, "Arousal", 1166.89, 1171.16, [11, 12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Lip Trill", 2, "Arousal", 1173.97, 1178.34, [12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Lip Trill", 3, "Arousal", 1180.79, 1183.04, [12], list(range(13, 19)), list(range(19, 23)), [26]],
            [519, "Lip Trill", 4, "Arousal", 1185.88, 1190.38, [12], list(range(13, 21)), list(range(21, 23)), [26]],
            [519, "M", 1, "Baseline", 671.86, 675.03, [9, 10], list(range(11, 19)), list(range(19, 22)), [26]],
            [519, "M", 2, "Baseline", 676.98, 680.88, [9, 10], list(range(11, 19)), list(range(19, 22)), [26]],
            [519, "M", 3, "Baseline", 682.51, 686.52, [9, 10], list(range(11, 19)), list(range(19, 22)), [26]],
            [519, "M", 1, "Arousal", 1236.85, 1241.04, [10, 11], list(range(12, 19)), list(range(19, 23)), [26]],
            [519, "M", 2, "Arousal", 1242.67, 1247.49, [10, 11], list(range(12, 19)), list(range(19, 22)), [26]],
            [519, "M", 3, "Arousal", 1250.69, 1254.91, [10, 11], list(range(12, 19)), list(range(19, 22)), [26]],
            [519, "N", 1, "Baseline", 688.64, 692.42, [9, 10, 11], list(range(12, 19)), list(range(19, 22)), [26]],
            [519, "N", 2, "Baseline", 694.01, 697.73, [9, 10, 11], list(range(12, 19)), list(range(19, 22)), [26]],
            [519, "N", 3, "Baseline", 699.30, 703.04, [9, 10], list(range(11, 19)), list(range(19, 22)), [26]],
            [519, "N", 1, "Arousal", 1258.25, 1262.55, [10, 11], list(range(12, 19)), list(range(19, 22)), [26]],
            [519, "N", 2, "Arousal", 1264.37, 1268.89, [10, 11], list(range(12, 19)), list(range(19, 22)), [26]],
            [519, "N", 3, "Arousal", 1270.61, 1275.75, [10, 11], list(range(12, 19)), list(range(19, 22)), [26]],
            [520, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 333.90, 359.83, [13], list(range(14, 19)), list(range(19, 22)), [26]],
            [520, "Resting Nasal Breathing 5 Cycles", 1, "Arousal", 1339.90, 1367.82, [13, 14], list(range(15, 19)), list(range(19, 22)), [26]],
            [520, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 372.10, 393.80, [13], list(range(14, 19)), list(range(19, 22)), [26]],
            [520, "Resting Oral Breathing 5 Cycles", 1, "Arousal", 1371.48, 1393.35, [13, 14], list(range(15, 19)), list(range(19, 22)), [26]],
            [520, "Comfortable Ah", 1, "Baseline", 411.13, 417.63, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "Comfortable Ah", 2, "Baseline", 424.05, 430.10, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "Comfortable Ah", 3, "Baseline", 434.03, 440.01, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Comfortable Ah", 1, "Arousal", 1083.25, 1087.15, [14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Comfortable Ah", 2, "Arousal", 1090.33, 1094.38, [14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Comfortable Ah", 3, "Arousal", 1098.03, 1101.36, [13, 14], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Soft Ah", 1, "Baseline", 470.73, 475.94, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Soft Ah", 2, "Baseline", 479.21, 483.42, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Soft Ah", 3, "Baseline", 485.82, 490.89, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Soft Ah", 1, "Arousal", 1122.70, 1126.37, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Soft Ah", 2, "Arousal", 1127.86, 1132.01, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Soft Ah", 3, "Arousal", 1133.51, 1137.46, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Loud Ah", 1, "Baseline", 444.47, 448.79, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Loud Ah", 2, "Baseline", 454.48, 458.82, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Loud Ah", 3, "Baseline", 462.63, 467.90, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "Loud Ah", 1, "Arousal", 1103.58, 1107.86, [14], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Loud Ah", 2, "Arousal", 1109.94, 1113.49, [14], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Loud Ah", 3, "Arousal", 1115.92, 1120.43, [14], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Straw Phonation", 1, "Baseline", 532.13, 536.12, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Straw Phonation", 2, "Baseline", 538.82, 543.43, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Straw Phonation", 3, "Baseline", 545.92, 550.58, [13], list(range(14, 18)), list(range(18, 22)), [26]],
            [520, "Straw Phonation", 1, "Arousal", 1170.07, 1173.63, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Straw Phonation", 2, "Arousal", 1177.31, 1182.15, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Straw Phonation", 3, "Arousal", 1184.44, 1189.28, [13, 14], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Straw Blowing", 1, "Baseline", 505.36, 510.27,  [13], list(range(14, 19)), list(range(19, 22)), [26]],
            [520, "Straw Blowing", 2, "Baseline", 513.54, 518.34, [13], list(range(14, 19)), list(range(19, 22)), [26]],
            [520, "Straw Blowing", 3, "Baseline", 521.89, 524.94, [13], list(range(14, 19)), list(range(19, 22)), [26]],
            [520, "Straw Blowing", 1, "Arousal", 1146.70, 1151.44, [13, 14], list(range(15, 19)), list(range(19, 22)), [26]],
            [520, "Straw Blowing", 2, "Arousal", 1154.08, 1159.13, [13, 14], list(range(15, 19)), list(range(19, 22)), [26]],
            [520, "Straw Blowing", 3, "Arousal", 1161.86, 1166.20, [13, 14], list(range(15, 19)), list(range(19, 22)), [26]],
            [520, "Bilabial Fricative", 1, "Arousal", 1264.20, 1268.50, [13, 14], list(range(15, 19)), list(range(18, 23)), [26]],
            [520, "Bilabial Fricative", 2, "Arousal", 1270.62, 1273.94, [13, 14], list(range(15, 19)), list(range(18, 23)), [26]],
            [520, "Bilabial Fricative", 3, "Arousal", 1276.49, 1280.61, [13, 14], list(range(15, 19)), list(range(18, 22)), [26]],
            [520, "Raspberry", 1, "Baseline", 625.08, 627.40, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "Raspberry", 2, "Baseline", 640.68, 644.95, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "Raspberry", 3, "Baseline", 648, 651.23, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "Raspberry", 4, "Baseline", 654.64, 658.19, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "Raspberry", 1, "Arousal", 1245.10, 1247.51, [13, 14], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Raspberry", 2, "Arousal", 1250.40, 1253.82, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Raspberry", 3, "Arousal", 1256.37, 1259.95, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Lip Trill", 1, "Baseline", 585.48, 587.44, [13], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "Lip Trill", 2, "Baseline", 591.66, 594.03, [13], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Lip Trill", 3, "Baseline", 597.67, 600.42, [13], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Lip Trill", 1, "Arousal", 1215.11, 1218.07, [13, 14], list(range(15, 18)), list(range(18, 23)), [26]],
            [520, "Lip Trill", 2, "Arousal", 1220.92, 1224.04, [13, 14], list(range(15, 18)), list(range(18, 22)), [26]],
            [520, "M", 1, "Baseline", 670, 673.98, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "M", 2, "Baseline", 676.53, 681.03, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [520, "M", 3, "Baseline", 682.80, 687.09, [13], list(range(14, 18)), list(range(18, 23)), [26]],
            [521, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 341.94, 375.81, [5], list(range(6, 13)), list(range(13, 17)), [26]],
            [521, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 396.57, 428.13, [5], list(range(6, 12)), list(range(12, 17)), [26]],
            [521, "Comfortable Ah", 1, "Baseline", 494.81, 499.35, [5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Comfortable Ah", 2, "Baseline", 504.30, 509.46, [5], list(range(6, 15)), list(range(15, 19)), [26]],
            [521, "Comfortable Ah", 3, "Baseline", 517.76, 520.09, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Comfortable Ah", 1, "Arousal", 1217.34, 1221.48, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Comfortable Ah", 2, "Arousal", 1224.73, 1228.70, [5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Comfortable Ah", 3, "Arousal", 1232.00, 1236.34, [5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Soft Ah", 1, "Baseline", 554.86, 559.46, [5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Soft Ah", 2, "Baseline", 563.44, 568.41, [5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Soft Ah", 3, "Baseline", 572.42, 577.61, [5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Soft Ah", 1, "Arousal", 1261.29, 1266.27, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Soft Ah", 2, "Arousal", 1267.85, 1272.25, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Soft Ah", 3, "Arousal", 1274.48, 1279.01, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Loud Ah", 1, "Baseline", 524.66, 530.01, [4, 5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Loud Ah", 2, "Baseline", 534.88, 540.51, [4, 5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Loud Ah", 3, "Baseline", 544.86, 550.10, [4, 5], list(range(6, 14)), list(range(14, 19)), [26]],
            [521, "Loud Ah", 1, "Arousal", 1239.87, 1244.05, [5], list(range(6, 15)), list(range(15, 19)), [26]],
            [521, "Loud Ah", 2, "Arousal", 1247.30, 1251.45, [5], list(range(6, 15)), list(range(15, 19)), [26]],
            [521, "Loud Ah", 3, "Arousal", 1254.53, 1258.29, [5], list(range(6, 15)), list(range(15, 19)), [26]],
            [521, "Straw Phonation", 1, "Baseline", 617.97, 622.48, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Straw Phonation", 2, "Baseline", 626.56, 630.86, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Straw Phonation", 3, "Baseline", 634.79, 639.27, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Straw Phonation", 1, "Arousal", 1310.08, 1314.48, [4, 5], list(range(6, 15)), list(range(15, 19)), [26]],
            [521, "Straw Phonation", 2, "Arousal", 1317.29, 1322.63, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Straw Phonation", 3, "Arousal", 1324.85, 1329.58, [5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Straw Blowing", 1, "Baseline", 588.71, 592.36,  [4, 5, 6], list(range(7, 16)), list(range(16, 19)), [26]],
            [521, "Straw Blowing", 2, "Baseline", 597.98, 603.19, [4, 5, 6], list(range(7, 15)), list(range(15, 19)), [26]],
            [521, "Straw Blowing", 3, "Baseline", 606.88, 611.87, [4, 5, 6], list(range(7, 15)), list(range(15, 18)), [26]],
            [521, "Straw Blowing", 1, "Arousal", 1287.71, 1291.96, [4, 5, 6], list(range(7, 15)), list(range(15, 18)), [26]],
            [521, "Straw Blowing", 2, "Arousal", 1295.10, 1299.24, [4, 5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Straw Blowing", 3, "Arousal", 1302.47, 1306.83, [4, 5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Bilabial Fricative", 1, "Baseline", 732.02, 736.70, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Bilabial Fricative", 2, "Baseline", 744.16, 748.22, [4, 5, 6], list(range(7, 16)), list(range(16, 18)), [26]],
            [521, "Bilabial Fricative", 3, "Baseline", 751.65, 755.74, [4, 5, 6], list(range(7, 16)), list(range(16, 18)), [26]],
            [521, "Bilabial Fricative", 4, "Baseline", 758.33, 762.76, [4, 5], list(range(6, 16)), list(range(16, 18)), [26]],
            [521, "Bilabial Fricative", 1, "Arousal", 1410.48, 1415.05, [4, 5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Bilabial Fricative", 2, "Arousal", 1417.69, 1422.15, [4, 5], list(range(6, 15)), list(range(15, 19)), [26]],
            [521, "Bilabial Fricative", 3, "Arousal", 1424.68, 1428.87, [4, 5], list(range(6, 15)), list(range(15, 19)), [26]],
            [521, "Raspberry", 1, "Baseline", 702.01, 705.70, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Raspberry", 2, "Baseline", 709.22, 712.79, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Raspberry", 3, "Baseline", 716.95, 720.58, [4, 5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Raspberry", 1, "Arousal", 1386.66, 1389.89, [5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Raspberry", 2, "Arousal", 1393.70, 1396.73, [5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Raspberry", 3, "Arousal", 1399.82, 1403.68, [5], list(range(6, 15)), list(range(15, 18)), [26]],
            [521, "Lip Trill", 1, "Baseline", 666.10, 668.84, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Lip Trill", 2, "Baseline", 673.31, 677.40, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Lip Trill", 3, "Baseline", 680.29, 684.42, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Lip Trill", 4, "Baseline", 688.44, 692.80, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Lip Trill", 1, "Arousal", 1353.45, 1358.04, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Lip Trill", 2, "Arousal", 1361.52, 1366.00, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Lip Trill", 3, "Arousal", 1368.76, 1373.50, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "Lip Trill", 4, "Arousal", 1376.98, 1381.46, [5], list(range(6, 14)), list(range(14, 18)), [26]],
            [521, "M", 1, "Baseline", 765.66, 769.74, [4], list(range(5, 13)), list(range(13, 18)), [26]],
            [521, "M", 2, "Baseline", 771.90, 776.11, [4], list(range(5, 13)), list(range(13, 18)), [26]],
            [521, "M", 3, "Baseline", 778.79, 782.36, [4], list(range(5, 14)), list(range(14, 18)), [26]],
            [521, "M", 1, "Arousal", 1431.94, 1436.30, [4], list(range(5, 13)), list(range(13, 18)), [26]],
            [521, "M", 2, "Arousal", 1439.09, 1445.21, [4], list(range(5, 13)), list(range(13, 18)), [26]],
            [521, "M", 3, "Arousal", 1446.91, 1452.17, [4], list(range(5, 13)), list(range(13, 18)), [26]],
            [521, "N", 1, "Baseline", 841.98, 845.86, [4], list(range(5, 13)), list(range(13, 17)), [26]],
            [521, "N", 2, "Baseline", 848.87, 852.67, [4], list(range(5, 13)), list(range(13, 17)), [26]],
            [521, "N", 3, "Baseline", 855.55, 858.99, [4], list(range(5, 13)), list(range(13, 17)), [26]],
            [521, "N", 1, "Arousal", 1453.95, 1457.72, [4], list(range(5, 13)), list(range(13, 17)), [26]],
            [521, "N", 2, "Arousal", 1460.73, 1464.20, [4], list(range(5, 13)), list(range(13, 18)), [26]],
            [521, "N", 3, "Arousal", 1467.24, 1470.72, [4], list(range(5, 13)), list(range(13, 18)), [26]],
            [512, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 330.10, 334.65, [6, 7], list(range(8, 15)), list(range(15, 19)), [23]],
            [512, "Resting Nasal Breathing 5 Cycles", 1, "Arousal", 1176.80, 1193.43, [6, 7], list(range(8, 13)), list(range(13, 18)), [23]],
            [512, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 348.97, 372.65, [6, 7], list(range(8, 13)), list(range(13, 18)), [23]],
            [512, "Comfortable Ah", 1, "Baseline", 374.57, 379.53, [7], list(range(8, 13)), list(range(13, 19)), [23]],
            [512, "Comfortable Ah", 2, "Baseline", 384.97, 389.86, [7], list(range(8, 13)), list(range(13, 19)), [23]],
            [512, "Comfortable Ah", 3, "Baseline", 393.04, 398.64, [7], list(range(8, 13)), list(range(13, 19)), [23]],
            [512, "Comfortable Ah", 4, "Baseline", 403.67, 408.42, [7], list(range(8, 13)), list(range(13, 19)), [23]],
            [512, "Comfortable Ah", 1, "Arousal", 1208.36, 1212.41, [7], list(range(8, 13)), list(range(13, 18)), [23]],
            [512, "Comfortable Ah", 2, "Arousal", 1216.50, 1220.63, [7], list(range(8, 13)), list(range(13, 18)), [23]],
            [512, "Comfortable Ah", 3, "Arousal", 1224.19, 1227.05, [7], list(range(8, 14)), list(range(14, 18)), [23]],
            [512, "Soft Ah", 1, "Baseline", 415.03, 419.88, [7], list(range(6, 14)), list(range(13, 19)), [23]],
            [512, "Soft Ah", 2, "Baseline", 422.80, 427.76, [7], list(range(6, 14)), list(range(14, 19)), [23]],
            [512, "Soft Ah", 3, "Baseline", 430.45, 435.10, [7], list(range(6, 14)), list(range(14, 19)), [23]],
            [512, "Soft Ah", 1, "Arousal", 1233.87, 1237.93, [7], list(range(6, 14)), list(range(14, 18)), [23]],
            [512, "Soft Ah", 2, "Arousal", 1240.53, 1245.16, [7], list(range(6, 14)), list(range(14, 18)), [23]],
            [512, "Soft Ah", 3, "Arousal", 1248.48, 1251.92, [7], list(range(6, 14)), list(range(14, 18)), [23]],
            [512, "Loud Ah", 1, "Baseline", 441.05, 445.89, [7], list(range(6, 14)), list(range(13, 18)), [23]],
            [512, "Loud Ah", 2, "Baseline", 448.54, 453.88, [7], list(range(6, 14)), list(range(13, 19)), [23]],
            [512, "Loud Ah", 3, "Baseline", 457.28, 460.95, [7], list(range(6, 14)), list(range(15, 18)), [23]],
            [512, "Loud Ah", 1, "Arousal", 1256.24, 1260.77, [7], list(range(6, 15)), list(range(14, 19)), [23]],
            [512, "Loud Ah", 2, "Arousal", 1264.46, 1267.72, [7], list(range(6, 15)), list(range(14, 18)), [23]],
            [512, "Loud Ah", 3, "Arousal", 1271.48, 1274.80, [7, 8], list(range(6, 15)), list(range(15, 19)), [23]],
            [512, "Straw Phonation", 1, "Baseline", 516.11, 520.97, [7, 8], list(range(6, 14)), list(range(15, 19)), [23]],
            [512, "Straw Phonation", 2, "Baseline", 524.38, 530.35, [7, 8], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Straw Phonation", 3, "Baseline", 534.59, 540.67, [7, 8], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Straw Phonation", 1, "Arousal", 1293.73, 1298.15, [7, 8], list(range(6, 15)), list(range(15, 19)), [23]],
            [512, "Straw Phonation", 2, "Arousal", 1302.01, 1307.27, [7, 8], list(range(6, 14)), list(range(16, 19)), [23]],
            [512, "Straw Phonation", 3, "Arousal", 1311.01, 1316.04, [7, 8], list(range(6, 15)), list(range(16, 20)), [23]],
            [512, "Straw Blowing", 1, "Baseline", 546.97, 552.96,  [7, 8], list(range(7, 16)), list(range(16, 19)), [23]],
            [512, "Straw Blowing", 2, "Baseline", 575.86, 579.81, [7, 8], list(range(7, 15)), list(range(15, 19)), [23]],
            [512, "Straw Blowing", 3, "Baseline", 584.65, 590.85, [7, 8], list(range(7, 15)), list(range(16, 20)), [23]],
            [512, "Straw Blowing", 1, "Arousal", 1319.84, 1325.07, [7, 8], list(range(7, 15)), list(range(16, 20)), [23]],
            [512, "Straw Blowing", 2, "Arousal", 1328.61, 1334.75, [7, 8], list(range(6, 15)), list(range(16, 20)), [23]],
            [512, "Straw Blowing", 3, "Arousal", 1338.58, 1343.90, [7, 8], list(range(6, 15)), list(range(15, 20)), [23]],
            [512, "Bilabial Fricative", 1, "Baseline", 835.34, 838.96, [7, 8, 9], list(range(6, 14)), list(range(16, 19)), [23]],
            [512, "Bilabial Fricative", 2, "Baseline", 842.78, 848.09, [7, 8], list(range(7, 16)), list(range(16, 19)), [23]],
            [512, "Bilabial Fricative", 3, "Baseline", 851.20, 856.87, [7, 8], list(range(7, 16)), list(range(16, 19)), [23]],
            [512, "Bilabial Fricative", 4, "Baseline", 859.70, 864.31, [7, 8], list(range(6, 16)), list(range(16, 19)), [23]],
            [512, "Bilabial Fricative", 1, "Arousal", 1352.79, 1357.48, [7, 8], list(range(6, 15)), list(range(16, 19)), [23]],
            [512, "Bilabial Fricative", 2, "Arousal", 1361.16, 1366.48, [7, 8], list(range(6, 15)), list(range(16, 20)), [23]],
            [512, "Bilabial Fricative", 3, "Arousal", 1369.13, 1374.89, [7, 8], list(range(6, 15)), list(range(16, 20)), [23]],
            [512, "Bilabial Fricative", 4, "Arousal", 1377.89, 1382.74, [7, 8, 9], list(range(6, 15)), list(range(16, 20)), [23]],
            [512, "Raspberry", 1, "Baseline", 816.26, 821.35, [7, 8, 9], list(range(6, 14)), list(range(15, 19)), [23]],
            [512, "Raspberry", 2, "Baseline", 825.58, 828.38, [7, 8, 9], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Raspberry", 1, "Arousal", 1502.71, 1505.32, [7, 8, 9], list(range(6, 15)), list(range(15, 19)), [23]],
            [512, "Raspberry", 2, "Arousal", 1508.30, 1511.09, [7, 8], list(range(6, 15)), list(range(15, 19)), [23]],
            [512, "Raspberry", 3, "Arousal", 1514.49, 1517.05, [7, 8], list(range(6, 15)), list(range(16, 19)), [23]],
            [512, "Lip Trill", 1, "Baseline", 668.67, 671.54, [7, 8], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Lip Trill", 2, "Baseline", 676.56, 679.05, [7, 8], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Lip Trill", 3, "Baseline", 683.92, 686.80, [7, 8], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Lip Trill", 1, "Arousal", 1393.29, 1396.41, [7, 8], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Lip Trill", 2, "Arousal", 1401.15, 1404.55, [7], list(range(6, 14)), list(range(16, 20)), [23]],
            [512, "Lip Trill", 3, "Arousal", 1409.42, 1412.90, [7, 8], list(range(6, 14)), list(range(16, 19)), [23]],
            [512, "Lip Trill", 4, "Arousal", 1417.64, 1420.41, [7, 8], list(range(6, 14)), list(range(16, 19)), [23]],
            [512, "M", 1, "Baseline", 870.88, 876.13, [6], list(range(5, 13)), list(range(15, 18)), [23]],
            [512, "M", 2, "Baseline", 880.43, 884.15, [6], list(range(5, 13)), list(range(15, 18)), [23]],
            [512, "M", 1, "Arousal", 1521.52, 1526.49, [6], list(range(5, 13)), list(range(14, 18)), [23]],
            [512, "M", 2, "Arousal", 1528.97, 1533.85, [6], list(range(5, 13)), list(range(14, 18)), [23]],
            [512, "M", 3, "Arousal", 1535.72, 1540.34, [6], list(range(5, 13)), list(range(14, 18)), [23]],
            [512, "N", 1, "Baseline", 887.87, 892.67, [6], list(range(5, 13)), list(range(14, 18)), [23]],
            [512, "N", 2, "Baseline", 896.29, 901.17, [6], list(range(5, 13)), list(range(14, 18)), [23]],
            [512, "N", 1, "Arousal", 1542.73, 1546.94, [6], list(range(5, 13)), list(range(13, 18)), [23]],
            [512, "N", 2, "Arousal", 1548.54, 1552.21, [6], list(range(5, 13)), list(range(13, 18)), [23]],
            [512, "N", 3, "Arousal", 1555.22, 1559.17, [6], list(range(5, 13)), list(range(13, 18)), [23]]]

        cols = "Subject Task Trial State Start Stop Velum Pharynx UES Eso".split()
        tasks_dict = [dict(zip(cols, task)) for task in tasks]

        return tasks_dict

    def dataframe(self):
        """
            Loads the raw data and creates a pandas dataframe containing the
            segment data. Also saves a copy of the segment data as a pickle file
            if it does not already exist or clean property was set to True in
            the sovt class object.

            Arguments:
            ----------
            None

            Returns:
            --------
            None 
            Saves dataframe in self.sovt.segs class property.
        """
        if self.sovt.clean:
            # Regardless create new dataframe
            self._make_df()
        elif not Path(self.sovt.path_out_root / "data/segs.pkl").is_file():
            self._make_df()
        else:
            self.sovt.segs = pd.read_pickle(self.sovt.path_out_root / "data/segs.pkl")


    def process_segs(self):
        """
            Adds a new column called Ignore to the dataframe. Marks any segment
            that is less than 3.0 seconds to be ignored. The dataframe is
            modified in place. No copy of the data frame is returned.

            Arguments:
            ----------
            None
            Uses self.sovt.segs class property

            Returns:
            --------
            None
        """
        df = self.sovt.segs
        df["Ignore"] = 0

        start = df["Start"]
        stop = df["Stop"]
        df.loc[(stop - start) < 3.0, "Ignore"] = 1
        self.segs_to_ignore()

    def segs_to_ignore(self):
        """
            Sets a list of indexs for the segments dataframe to 1 (True) for the
            column labeled 'Ignore'. These indexs follow the format of
            (subject_number, state, task, trial_number). Dataframe is modified in
            place. No copy is returned.

            Arguments:
            ----------
            None

            Returns:
            --------
            None
        """
        df = self.sovt.segs

        df.loc[(509, "Arousal", "Bilabial Fricative", 1), "Ignore"] = 1
        df.loc[(509, "Arousal", "Bilabial Fricative", 2), "Ignore"] = 1
        df.loc[(509, "Arousal", "Bilabial Fricative", 3), "Ignore"] = 1
        df.loc[(510, "Arousal", "Lip Trill", 2), "Ignore"] = 1
        df.loc[(521, "Baseline", "Bilabial Fricative", 1), "Ignore"] = 1
        df.loc[(512, "Baseline", "Lip Trill", 3), "Ignore"] = 1
        df.loc[(512, "Baseline", "Bilabial Fricative", 1), "Ignore"] = 1
        df.loc[(512, "Arousal", "Bilabial Fricative", 1), "Ignore"] = 1
        
    def _make_df(self):
        """
            Private method that creates the pandas dataframe from the data
            generated by the load method. Also saves a copy of the dataframe as
            a pickle file.

            Arguments:
            ----------
            None

            Returns:
            --------
            None 
            Saves the dataframe in the selfsovt..segs class property.

        """
        tasks = self.load()
        cols = "Subject Task Trial State Start Stop Velum Pharynx UES Eso".split()
        idxs = "Subject State Task Trial".split()
        df = pd.DataFrame(columns=cols)

        df = df.append(tasks, ignore_index=True)
        df = df.set_index(idxs).sort_index()

        # Create the folder that will contain the data
        save_path = self.sovt.path_out_root / "data"
        save_path.mkdir(parents=True, exist_ok=True)
        df.to_pickle(save_path / "segs.pkl")
        self.sovt.segs = df

