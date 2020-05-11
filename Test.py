import datetime
import Main


chose = input("1 - 1MB, 2 - 10MB, 3 - 100MB:  ")
if chose == "1":
    file = open("input_1MB.txt", 'r')
    text = file.read()
    start_time = datetime.datetime.now()
    Main.RSA(Main.hash(text))
    end_time = datetime.datetime.now()
    print("Время вычисления = ", (end_time - start_time))
elif chose == '2':
    file = open("input_10MB.txt", 'r')
    text = file.read()
    start_time = datetime.datetime.now()
    Main.RSA(Main.hash(text))
    end_time = datetime.datetime.now()
    print("Время вычисления = ", (end_time - start_time))
elif chose == '3':
    file = open("input_100MB.txt", 'r')
    text = file.read()
    start_time = datetime.datetime.now()
    Main.RSA(Main.hash(text))
    end_time = datetime.datetime.now()
    print("Время вычисления = ", (end_time - start_time))