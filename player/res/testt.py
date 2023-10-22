_x = """Sachin Tendulkar
Virat Kohli
Ricky Ponting
Kumar Sangakkara
Jacques Kallis
Hashim Amla
Mahela Jayawardene
Brian Lara
Rahul Dravid
AB de Villiers
David Warner
Joe Root
Rohit Sharma
Steve Smith
Chris Gayle
Sanath Jayasuriya
Shivnarine Chanderpaul
Younis Khan
Kane Williamson
Matthew Hayden
Ross Taylor
Tillakaratne Dilshan
Mohammad Yousuf
Alastair Cook
Sourav Ganguly
Virender Sehwag
Mark Waugh
Graeme Smith
Michael Clarke
Sunil Gavaskar
Herschelle Gibbs
Desmond Haynes
Inzamam-ul-Haq
Viv Richards
Steve Waugh
Gary Kirsten
Adam Gilchrist
Kevin Pietersen
Aravinda de Silva
Javed Miandad
Saeed Anwar
Babar Azam
Allan Border
Gordon Greenidge
Mohammad Azharuddin
Don Bradman
Graham Gooch
Nathan Astle
Marvan Atapattu
Greg Chappell"""

splited = _x.split("\n")

import random

def produce(i_value):
    _val = splited[random.randint(0, (len(splited))-1)]
    if _val == i_value:
        return produce(i_value)
    else:
        return _val.strip()

cout=1
output_ = ""
for i in splited:
    output_+=f"""a++;
window["ans"+a] = "{i.strip()}"; //Ans{cout}
window["noans1"+a] = "{produce(i)}";
window["noans2"+a] = "{produce(i)}";
window["noans3"+a] = "{produce(i)}";
window["noans4"+a] = "{produce(i)}";

"""
    cout+=1

f = open('playersOutput.txt', 'a')
f.write(output_)
f.close()