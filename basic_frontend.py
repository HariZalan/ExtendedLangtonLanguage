import el_implementation
result=el_implementation.langton(input())
for i in result[0].keys():
    for j in result[0][i].keys():
        print(i,j,result[0][i][j],sep=",")
direction=result[1]
names={(0,1):"up",(1,0):"right",(0,-1):"down",(-1,0):"left"}
print()
print("The ant points ",names[direction])
print("The ant is currently at (",result[2][0],";",result[2][1],")")
