#flag{wh04m1_15_pr0ud_0f_y0u}

from pwn import *
p = process('./minesweeper')


def get_board():
	newboard = []
	for i in range(9):
		line = p.recvline().decode()
		if i==0 and line.startswith("Game"):
			return "hi"
		elif i==0 and line.startswith("You"):
			return p.recvline().decode()
		newboard.append(line.strip().split())
	return newboard

def convertBoard(board):
	newboard = [[-2 for i in range(9)] for j in range(9)]
	for i in range(9):
		for j in range(9):
			if board[i][j] == '_':
				newboard[i][j] = -2
			else:
				newboard[i][j] = int(board[i][j])
	for hi in range(2):
		for i in range(9):
			for j in range(9):
				if newboard[i][j]!=-2 and newboard[i][j]!=-1:
					count=0
					if i==0 and j==0:
						if newboard[i+1][j]==-2 or newboard[i+1][j]==-1 :
							count+=1
						if newboard[i][j+1]==-2 or newboard[i][j+1]==-1:
							count+=1
						if newboard[i+1][j+1]==-2 or newboard[i+1][j+1]==-1:
							count+=1
					if i==0 and j==8:
						if newboard[i+1][j]==-2 or newboard[i+1][j]==-1:
							count+=1
						if newboard[i][j-1]==-2 or newboard[i][j-1]==-1:
							count+=1
						if newboard[i+1][j-1]==-2 or newboard[i+1][j-1]==-1:
							count+=1
					if i==8 and j==0:
						if newboard[i-1][j]==-2 or newboard[i-1][j]==-1:
							count+=1
						if newboard[i][j+1]==-2 or newboard[i][j+1]==-1:
							count+=1
						if newboard[i-1][j+1]==-2 or newboard[i-1][j+1]==-1:
							count+=1
					if i==8 and j==8:
						if newboard[i-1][j]==-2 or newboard[i-1][j]==-1:
							count+=1
						if newboard[i][j-1]==-2 or newboard[i][j-1]==-1:
							count+=1
						if newboard[i-1][j-1]==-2 or newboard[i-1][j-1]==-1:
							count+=1
					if j==0 and i>0 and i<8:
						for k in range(3):
							if newboard[i+k-1][j+1]==-2 or newboard[i+k-1][j+1]==-1:
								count+=1
						if newboard[i+1][j]==-2 or newboard[i+1][j]==-1:
							count+=1
						if newboard[i-1][j]==-2 or newboard[i-1][j]==-1:
							count+=1					
					if j==8 and i>0 and i<8:
						for k in range(3):
							if newboard[i+k-1][j-1]==-2 or newboard[i+k-1][j-1]==-1:
								count+=1
						if newboard[i+1][j]==-2 or newboard[i+1][j]==-1:
							count+=1
						if newboard[i-1][j]==-2 or newboard[i-1][j]==-1:
							count+=1					
					if i==0 and j>0 and j<8:
						for k in range(3):
							if newboard[i+1][j+k-1]==-2 or newboard[i+1][j+k-1]==-1:
								count+=1
						if newboard[i][j+1]==-2 or newboard[i][j+1]==-1:
							count+=1
						if newboard[i][j-1]==-2 or newboard[i][j-1]==-1:
							count+=1					
					if i==8 and j>0 and j<8:
						for k in range(3):
							if newboard[i-1][j+k-1]==-2 or newboard[i-1][j+k-1]==-1:
								count+=1
						if newboard[i][j+1]==-2 or newboard[i][j+1]==-1:
							count+=1
						if newboard[i][j-1]==-2 or newboard[i][j-1]==-1:
							count+=1					
					if i>0 and i<8 and j>0 and j<8:
						for k in range(3):
							if newboard[i+k-1][j+1]==-2 or newboard[i+k-1][j+1]==-1:
								count+=1
							if newboard[i+k-1][j-1]==-2 or newboard[i+k-1][j-1]==-1:
								count+=1
						if newboard[i+1][j]==-2 or newboard[i+1][j]==-1:
							count+=1
						if newboard[i-1][j]==-2 or newboard[i-1][j]==-1:
							count+=1

					if count==newboard[i][j]:
						if i==0 and j==0:
							if newboard[i+1][j]==-2:
								newboard[i+1][j]=-1   #-1 denotes bomb
							if newboard[i][j+1]==-2:
								newboard[i][j+1]=-1
							if newboard[i+1][j+1]==-2:
								newboard[i+1][j+1]=-1
						if i==0 and j==8:
							if newboard[i+1][j]==-2:
								newboard[i+1][j]=-1
							if newboard[i][j-1]==-2:
								newboard[i][j-1]=-1
							if newboard[i+1][j-1]==-2:
								newboard[i+1][j-1]=-1
						if i==8 and j==0:
							if newboard[i-1][j]==-2:
								newboard[i-1][j]=-1
							if newboard[i][j+1]==-2:
								newboard[i][j+1]=-1
							if newboard[i-1][j+1]==-2:
								newboard[i-1][j+1]=-1
						if i==8 and j==8:
							if newboard[i-1][j]==-2:
								newboard[i-1][j]=-1
							if newboard[i][j-1]==-2:
								newboard[i][j-1]=-1
							if newboard[i-1][j-1]==-2:
								newboard[i-1][j-1]=-1
						if j==0 and i>0 and i<8:
							for k in range(3):
								if newboard[i+k-1][j+1]==-2:
									newboard[i+k-1][j+1]=-1
							if newboard[i+1][j]==-2:
								newboard[i+1][j]=-1
							if newboard[i-1][j]==-2:
								newboard[i-1][j]=-1					
						if j==8 and i>0 and i<8:
							for k in range(3):
								if newboard[i+k-1][j-1]==-2:
									newboard[i+k-1][j-1]=-1
							if newboard[i+1][j]==-2:
								newboard[i+1][j]=-1
							if newboard[i-1][j]==-2:
								newboard[i-1][j]=-1					
						if i==0 and j>0 and j<8:
							for k in range(3):
								if newboard[i+1][j+k-1]==-2:
									newboard[i+1][j+k-1]=-1
							if newboard[i][j+1]==-2:
								newboard[i][j+1]=-1
							if newboard[i][j-1]==-2:
								newboard[i][j-1]=-1					
						if i==8 and j>0 and j<8:
							for k in range(3):
								if newboard[i-1][j+k-1]==-2:
									newboard[i-1][j+k-1]=-1
							if newboard[i][j+1]==-2:
								newboard[i][j+1]=-1
							if newboard[i][j-1]==-2:
								newboard[i][j-1]=-1				
						if i>0 and i<8 and j>0 and j<8:
							for k in range(3):
								if newboard[i+k-1][j+1]==-2:
									newboard[i+k-1][j+1]=-1
								if newboard[i+k-1][j-1]==-2:
									newboard[i+k-1][j-1]=-1
							if newboard[i+1][j]==-2:
								newboard[i+1][j]=-1
							if newboard[i-1][j]==-2:
								newboard[i-1][j]=-1
	for i in range(9):
		for j in range(9):							
			if newboard[i][j]!=-2 and newboard[i][j]!=-1:	
				count =0
				if i==0 and j==0:
					if newboard[i+1][j]==-1:
						count+=1
					if newboard[i][j+1]==-1:
						count+=1
					if newboard[i+1][j+1]==-1:
						count+=1
				if i==0 and j==8:
					if newboard[i+1][j]==-1:
						count+=1
					if newboard[i][j-1]==-1:
						count+=1
					if newboard[i+1][j-1]==-1:
						count+=1
				if i==8 and j==0:
					if newboard[i-1][j]==-1:
						count+=1
					if newboard[i][j+1]==-1:
						count+=1
					if newboard[i-1][j+1]==-1:
						count+=1
				if i==8 and j==8:
					if newboard[i-1][j]==-1:
						count+=1
					if newboard[i][j-1]==-1:
						count+=1
					if newboard[i-1][j-1]==-1:
						count+=1
				if j==0 and i>0 and i<8:
					for k in range(3):
						if newboard[i+k-1][j+1]==-1:
							count+=1
					if newboard[i+1][j]==-1:
						count+=1
					if newboard[i-1][j]==-1:
						count+=1					
				if j==8 and i>0 and i<8:
					for k in range(3):
						if newboard[i+k-1][j-1]==-1:
							count+=1
					if newboard[i+1][j]==-1:
						count+=1
					if newboard[i-1][j]==-1:
						count+=1					
				if i==0 and j>0 and j<8:
					for k in range(3):
						if newboard[i+1][j+k-1]==-1:
							count+=1
					if newboard[i][j+1]==-1:
						count+=1
					if newboard[i][j-1]==-1:
						count+=1					
				if i==8 and j>0 and j<8:
					for k in range(3):
						if newboard[i-1][j+k-1]==-1:
							count+=1
					if newboard[i][j+1]==-1:
						count+=1
					if newboard[i][j-1]==-1:
						count+=1					
				if i>0 and i<8 and j>0 and j<8:
					for k in range(3):
						if newboard[i+k-1][j+1]==-1:
							count+=1
						if newboard[i+k-1][j-1]==-1:
							count+=1
					if newboard[i+1][j]==-1:
						count+=1
					if newboard[i-1][j]==-1:
						count+=1
				if count==newboard[i][j]:		
					if i==0 and j==0:
						if newboard[i+1][j]==-2:
							newboard[i+1][j]=9  #9 means safe
						if newboard[i][j+1]==-2:
							newboard[i][j+1]=9
						if newboard[i+1][j+1]==-2:
							newboard[i+1][j+1]=9
					if i==0 and j==8:
						if newboard[i+1][j]==-2:
							newboard[i+1][j]=9
						if newboard[i][j-1]==-2:
							newboard[i][j-1]=9
						if newboard[i+1][j-1]==-2:
							newboard[i+1][j-1]=9
					if i==8 and j==0:
						if newboard[i-1][j]==-2:
							newboard[i-1][j]=9
						if newboard[i][j+1]==-2:
							newboard[i][j+1]=9
						if newboard[i-1][j+1]==-2:
							newboard[i-1][j+1]=9
					if i==8 and j==8:
						if newboard[i-1][j]==-2:
							newboard[i-1][j]=9
						if newboard[i][j-1]==-2:
							newboard[i][j-1]=9
						if newboard[i-1][j-1]==-2:
							newboard[i-1][j-1]=9
					if j==0 and i>0 and i<8:
						for k in range(3):
							if newboard[i+k-1][j+1]==-2:
								newboard[i+k-1][j+1]=9
						if newboard[i+1][j]==-2:
							newboard[i+1][j]=9
						if newboard[i-1][j]==-2:
							newboard[i-1][j]=9					
					if j==8 and i>0 and i<8:
						for k in range(3):
							if newboard[i+k-1][j-1]==-2:
								newboard[i+k-1][j-1]=9
						if newboard[i+1][j]==-2:
							newboard[i+1][j]=9
						if newboard[i-1][j]==-2:
							newboard[i-1][j]=9					
					if i==0 and j>0 and j<8:
						for k in range(3):
							if newboard[i+1][j+k-1]==-2:
								newboard[i+1][j+k-1]=9
						if newboard[i][j+1]==-2:
							newboard[i][j+1]=9
						if newboard[i][j-1]==-2:
							newboard[i][j-1]=9					
					if i==8 and j>0 and j<8:
						for k in range(3):
							if newboard[i-1][j+k-1]==-2:
								newboard[i-1][j+k-1]=9
						if newboard[i][j+1]==-2:
							newboard[i][j+1]=9
						if newboard[i][j-1]==-2:
							newboard[i][j-1]=9				
					if i>0 and i<8 and j>0 and j<8:
						for k in range(3):
							if newboard[i+k-1][j+1]==-2:
								newboard[i+k-1][j+1]=9
							if newboard[i+k-1][j-1]==-2:
								newboard[i+k-1][j-1]=9
						if newboard[i+1][j]==-2:
							newboard[i+1][j]=9
						if newboard[i-1][j]==-2:
							newboard[i-1][j]=9

	return newboard
def check(board):
	for i in range(9):
		for j in range(9):
			if board[i][j]==9:
				return True
	return False
def getMove(board):
	for i in range(9):
		for j in range(9):
			if board[i][j]==9:
				return f"{i},{j}"

p.recvuntil(b']\n')			
for i in range(25):
	solved=False
	flag=0
	while not solved :
		board=get_board()
		if board=="hi":
			break
		if isinstance(board,str):
			if board.startswith("Here"):
				print(board)
				flag=1
				break
		p.recvline()
		board=convertBoard(board)
		if board[8][8]==-2:
			p.writeline(b'8,8')
			continue

		elif board[0][0]==-2 and not check(board):
			p.writeline(b'0,0')
			continue

		elif board[4][4]==-2 and not check(board):
			p.writeline(b'4,4')
			continue
			
		else:
			move=getMove(board)
			p.writeline(move.encode('utf-8'))
	if flag==1:
		break
		
p.close()
