import copy

N, M = map(int, input().split())

board=[]
answer=M**M

for i in range(N):
  board.append(list(input()))

#print(board)
#print(board[0][1])


def switch(pos,boardcopy):
  row=pos//M
  column=pos%M
  if boardcopy[row][column]=='#':
    boardcopy[row][column]='.'
  else:
    boardcopy[row][column]='#'
  if row!=0:
    if boardcopy[row-1][column]=='#':
      boardcopy[row-1][column]='.'
    else:
      boardcopy[row-1][column]='#'
  if row!=N-1:
    if boardcopy[row+1][column]=='#':
      boardcopy[row+1][column]='.'
    else:
      boardcopy[row+1][column]='#'
  if column!=0:
    if boardcopy[row][column-1]=='#':
      boardcopy[row][column-1]='.'
    else:
      boardcopy[row][column-1]='#'
  if column!=M-1:
    if boardcopy[row][column+1]=='#':
      boardcopy[row][column+1]='.'
    else:
      boardcopy[row][column+1]='#'

def search(topcheck,boardcopy):
  result=0
  
  #最上段についてtopcheckのパターンに従ってスイッチを押す
  for i in range(len(topcheck)):
    if topcheck[i]==1:
      switch(i,boardcopy)
      result+=1
      #print(boardcopy)
  
  #一つ上のマスが#になっているマスのスイッチを押す
  for j in range(M,N*M-1):
    if boardcopy[(j//M)-1][j%M]=='#':
      switch(j,boardcopy)
      result+=1
  #print(result)
  return result



#最上段を押すかどうかの全パターンを試す
for i in range(2**M):
  boardcopy=copy.deepcopy(board)
  #print(board,boardcopy)
  
  #topcheckに今回のループで試す最上段の押すパターンを格納
  topcheck=[]
  count=0
  while(count!=M):
    topcheck.append(i%2)
    i=(i//2)
    #print(topcheck)
    count+=1
  
  #topcheckに対してアルゴリズムに従ってswitchを何回押したかを探索
  result=search(topcheck,boardcopy)
  
  
  #最下段の行が全て消灯しているか確認
  flag=1
  for i in range(M):
    if boardcopy[M-1][i]=='#':
      flag=0
      break;
  #消灯していたら値を更新
  if flag==1:
    #print('c')
    answer=min(answer,result)
  
print(answer)

'''
for check in topcheck:
  checknumber=[]
  while(check>0):
    checknumber.append(check)
'''
