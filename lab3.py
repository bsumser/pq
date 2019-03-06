from sys import argv
from pQueue import pQueue

def main(argv):
    # Loop over input file. 
    # Split each line into the task and the corresponding number (if one exists)
    # Depending on what the input task was, preform the corresponding function
    # Finally, close your file.


    inputFile = argv[1]
    with open(inputFile, 'r') as file_ob:
        for line in file_ob:
            count = 0
            if ' ' in line:
                command, num = line.split()
                if command == "insert":
                    count += 1
        myQueue = pQueue(count);
    with open(inputFile, 'r') as file_ob:
        for line in file_ob:
            if ' ' in line:
                command, num = line.split()
                if command == "insert":
                    myQueue.insert(num)
                if command == "delete":
                    myQueue.delete(num)
            else:
                line = line.split()
                if line[0] == "maximum":
                    myQueue.maximum()
                if line[0] == "extractMax":
                    myQueue.extractMax()
                if line[0] == "isEmpty":
                    myQueue.isEmpty()
                if line[0] == "print":
                    myQueue.printQueue()
            if 'str' in line:
                break

if __name__ == "__main__":
    main(argv)
