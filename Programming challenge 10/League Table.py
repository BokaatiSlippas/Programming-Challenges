import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")
        
def read_csv(csv_file):
    csv_contents = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for row in reader:
            csv_contents.append(row)
    return csv_contents

def process_results(rows):
    dictionary={}
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]
        if home not in dictionary:
            dictionary[home] = [0,0,0,0,0]
        if away not in dictionary:
            dictionary[away] = [0,0,0,0,0]

        if winner=="D":
            dictionary[home][4]+=1 
            dictionary[away][4]+=1
            dictionary[home][1]+=1 
            dictionary[away][1]+=1
        elif winner=="A":
            dictionary[away][4]+=3
            dictionary[away][0]+=1
            dictionary[home][2]+=1
        elif winner=="H":
            dictionary[home][4]+=3
            dictionary[home][0]+=1
            dictionary[away][2]+=1
        dictionary[home][3]+=(int(homegoals)-int(awaygoals))
        dictionary[away][3]+=(int(awaygoals)-int(homegoals))
    return(dictionary)

if __name__ == "__main__":
    contents = read_csv(csv_file)
    dictionary=process_results(contents)
    newdictionary=dictionary
    print("-----------------------------------------")
    print("----------Premier League 16-17-----------")
    for key, value in sorted(newdictionary.items(), reverse=True, key=lambda e: e[1][4]):
        if len(str(key))==14:
            print(f'{key}{(7*" ")}{value[0]:>4}{value[1]:>4}{value[2]:>4}{value[3]:>4}{value[4]:>4}')
        else:
            spaces=14-(len(str(key)))
            print(f'{key}{((spaces+7)*" ")}{value[0]:>4}{value[1]:>4}{value[2]:>4}{value[3]:>4}{value[4]:>4}')
