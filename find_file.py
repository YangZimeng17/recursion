import os

def find_file(dir, filename):

    if os.path.isfile(dir):
        if os.path.basename(dir) == filename:
            return dir

    if os.path.isdir(dir):
        entries = os.listdir(dir)

        for e in entries:
            res = find_file(dir + "\\" + e, filename)
            # res may be None or string of correct directory
            if res:
                return res

print(find_file("E:\\yzm\\UofT\\first year content\\ESC 180", "test_calc.py"))

