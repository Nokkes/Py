import time
# num_lines = sum(1 for line in open('C:\\Scripts\\PY\\test.log'))
# print num_lines
cntr = 0
while (True):
    with open("C:\\Scripts\\PY\\test.log","r+") as f:
        cntr += 1
        time.sleep(2)
        print "Opening {0}, {1} times".format(f.name,cntr)
        print "------------------------------"
        for line in f:
            print line
        print "------------------------------"
        print "Closing {0}".format(f.name)
        print ""

# for i, line in enumerate(file, start=1):