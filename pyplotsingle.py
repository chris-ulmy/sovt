from hrmtools.hrm import HRM
from matplotlib import pyplot as plt

sub_num = 513


h = HRM()
path = r"P:\Data\HRM\Autonomic Arousal Study\513\513 Adjusted Annotations.txt"
# path = r"d:\Autonomic Arousal Study\512 Adjusted Annotations.txt"
h.import_data.from_text(path)
h.plot.time_in_min = False

tasks = [
            [513, "Resting Nasal Breathing 5 Cycles", 1, "Baseline", 351.81, 371.16, [10, 11, 12], list(range(8, 15)), list(range(15, 19)), [23]],
            [513, "Resting Nasal Breathing 5 Cycles", 1, "Arousal", 934.43, 953.36, [9, 10], list(range(8, 13)), list(range(13, 18)), [23]],
            [513, "Resting Oral Breathing 5 Cycles", 1, "Baseline", 378.41, 393.47, [10, 11, 12], list(range(8, 13)), list(range(13, 18)), [23]],
            [513, "Resting Oral Breathing 5 Cycles", 1, "Arousal", 378.56, 393.39, [10, 11, 12], list(range(8, 13)), list(range(13, 18)), [23]],
            [513, "Comfortable Ah", 1, "Baseline", 405.78, 411.53, [10, 11, 12], list(range(8, 13)), list(range(13, 19)), [23]],
            [513, "Comfortable Ah", 2, "Baseline", 415.72, 421.75, [10, 11, 12], list(range(8, 13)), list(range(13, 19)), [23]],
            [513, "Comfortable Ah", 3, "Baseline", 425.32, 431.15, [10, 11, 12], list(range(8, 13)), list(range(13, 19)), [23]],
            [513, "Comfortable Ah", 1, "Arousal", 985.73, 990.75, [10, 11, 12], list(range(8, 13)), list(range(13, 18)), [23]],
            [513, "Comfortable Ah", 2, "Arousal", 992.74, 997.27, [10, 11, 12], list(range(8, 13)), list(range(13, 18)), [23]],
            [513, "Comfortable Ah", 3, "Arousal", 999.61, 1003.82, [10, 11, 12], list(range(8, 14)), list(range(14, 18)), [23]]]

for task in tasks[:]:
    h.plot.line.create_overlay(
        # (task[4], task[5]), range(task[6][-1]+1, task[8][0]), title=f"{task[0]} {task[1]}, {task[3]}, Trial {task[2]}")
    (task[4], task[5]), range(8, 14), title=f"{task[0]} {task[1]}, {task[3]}, Trial {task[2]}")

# task = "ah comf"
# # state = "Baseline"
# state = "Arousal"
# st = 985.18
# sp = 999.16
# h.plot.line.create_overlay(
#     (st-2, sp+7), range(11, 15), title=f"{sub_num} {task}(s) {state}", show=True)
# h.plot.line.axes.set_ylim(bottom=-5, top=20)
# plt.show()
