from hrmtools.hrm import HRM
from matplotlib import pyplot as plt

sub_num = 513


h = HRM()
path = r"P:\Data\HRM\Autonomic Arousal Study\513\513 Adjusted Annotations.txt"
# path = r"d:\Autonomic Arousal Study\512 Adjusted Annotations.txt"
h.import_data.from_text(path)
h.plot.time_in_min = False

tasks = [


# for task in tasks[12:]:
#     h.plot.line.create_overlay(
#         (task[4], task[5]), range(task[6][-1]+1, task[8][0]), title=f"{task[0]} {task[1]}, {task[3]}, Trial {task[2]}")
    # (task[4], task[5]), range(10, 15), title=f"{task[0]} {task[1]}, {task[3]}, Trial {task[2]}")

task = "n"
state = "Baseline"
state = "Arousal"
st = 1196.61
sp = 1208.89
h.plot.line.create_overlay(
    (st-2, sp+7), range(13, 17), title=f"{sub_num} {task}(s) {state}", show=True)
# h.plot.line.axes.set_ylim(bottom=-5, top=20)
# plt.show()
