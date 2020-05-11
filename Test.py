import datetime
import Main


file = open("input.txt", 'r')
text = file.read()
start_time = datetime.datetime.now()
Main.RSA(Main.hash(text))
end_time = datetime.datetime.now()
print("Время вычисления = ", (end_time - start_time))