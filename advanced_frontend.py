import el_implementation as EL
print("Enter the board in CSV format (x,y,value):")
csv=input()
csv=csv.split("\n")
for i in range(len(csv)):
    csv[i]=csv[i].split(",")
board={0:{0:0}}
for i in csv:
    if (i[0] not in board):
        board[i[0]]={}
    board[i[0]][i[1]]=i[2]
print("Enter yer commands.")
commands=input()
result, direction, position = EL.langton(commands,system=board)
for i in result.keys():
    for j in result[i].keys():
        print(i,j,result[i][j],sep=",")
names={(0,1):"up",(1,0):"right",(0,-1):"down",(-1,0):"left"}
print("The operator points",names[direction])
print("The operator is at",position)
