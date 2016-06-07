import math as m
"""
a=검은 폰
b=검은 룩
c=검은 나이트
d=검은 비숍
e=검은 퀸
f=검은 킹
g=하얀 폰
h=하얀 룩
i=하얀 나이트
j=하얀 비숍
k=하얀 퀸
l=하얀 킹
x=빈칸
"""
def Rule(board, str):
    # 8 X 8
    #체스판은 8 X 8 --> 예를들어 받은 시작점과 끝점이 전부다 0~7까지 인지 확인
    for i in range(4):
        if int(str[i]) >= 0 and int(str[i]) <= 7:         
            continue
        else:
            return False
    
    start_r = int(str[0]) #시작 행
    start_c = int(str[1]) #시작 열
    end_r = int(str[2])   #도착 행
    end_c = int(str[3])   #         
    piece = board[start_r][start_c]  #시작점의 row 와 col은 말이 있어야한다.
    arrive_piece = board[end_r][end_c] #도착점에 말이 있는지 없는지 확인해야한다.
    arrive_pos = [end_r,end_c]    #도착지점을 list로 생성      
    White_team =['g','h','i','j','k','l']
    Black_team =['a','b','c','d','e','f']
    
    print (piece)
    if piece == 'x': #시작위치에 말이 없다면
        #움직일수 있는 말이 없다고 메세지창 보내야됨
        return False
    
    if piece in Black_team:  #도착 지점에 애초에 우리팀이 있으면 그냥 False 그냥 안전장치..
        if arrive_piece in Black_team:
            return False
    elif piece in White_team:
        if arrive_piece in White_team:
            return False

    
    
    
    if piece == 'a':  #'시작위치' = '검은 폰'이라면
        if arrive_piece in White_team : #도착점이 '상대팀말'이라면 대각선으로도 이동가능.
            if  ((arrive_pos[0] == start_r+1 and arrive_pos[1] == start_c+1 ) or #대각선으로 이동 가능
                 (arrive_pos[0] == start_r +1 and arrive_pos[1] == start_c-1)):
                return True
            else: #그 이외에는
                return False
        elif start_r == 1 and board[start_r + 1][start_c] == 'x':     #시작점이 첫시작위치고 앞에 아무것도 없어야 이동가능
            if arrive_pos[0] == 2 and  arrive_pos[1] == start_c :    #1칸 먼 도착점으로 이동가능
                return True
            elif (arrive_pos[0]==3)and(arrive_pos[1] == start_c)and(board[start_r+2][start_c] == 'x'): 
                #2칸이동하려는경우에는 2칸앞에 아무것도없어야한다.
                return True  
            else:  #그 이외에는 다 False
                return False
        elif start_r != 1:    #시작점이 첫시작점이 아니라면,
            if (arrive_pos[0] == start_r+1) and (arrive_pos[1] == start_c)and(board[start_r+1][start_c]=='x'):
                #한칸 이동하려는 전진하려는곳에 아무것도 없어야한다.
                return True
            else:
                return False
        else: #시작 위치가 첫시작위치도 아닌것이 , 첫시작위친데 앞에'piece'가 있다면 False
            return False
            
            
                
    elif piece == 'g':  #'시작위치' = '하얀 폰'이라면
        if arrive_piece in Black_team : #도착점이 '상대팀말'이라면 대각선으로도 이동가능.
            if  ((arrive_pos[0] == start_r -1 and arrive_pos[1] == start_c+1 ) or #대각선으로 이동 가능
                 (arrive_pos[0] == start_r -1 and arrive_pos[1] == start_c-1)):
                return True
            else: #그 이외에는
                return False
        elif start_r == 6 and board[start_r - 1][start_c] == 'x':     #시작점이 첫시작위치고 앞에 아무것도 없어야 이동가능
            if arrive_pos[0] == 5 and  arrive_pos[1] == start_c :    #1칸 먼 도착점으로 이동가능
                return True
            elif (arrive_pos[0]==4)and(arrive_pos[1] == start_c)and(board[start_r-2][start_c] == 'x'): 
                #2칸이동하려는경우에는 2칸앞에 아무것도없어야한다.
                return True  
            else:  #그 이외에는 다 False
                return False
        elif start_r != 6:    #시작점이 첫시작점이 아니라면,
            if (arrive_pos[0]==start_r-1)and(arrive_pos[1]==start_c)and(board[start_r-1][start_c]=='x'):
                #한칸 이동하려는 전진하려는곳에 아무것도 없어야한다.
                return True
            else:
                return False
        else: #시작 위치가 첫시작위치도 아닌것이 , 첫시작위친데 앞에'piece'가 있다면 False
            return False
    
    
    elif piece == 'b': #'검은 룩'이라면
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        count = 1
        distance = 0
        
        if move_row == 0 and move_col ==0:  #rook의 이동은 행으로만이동 또는 열로만 이동해야한다.
            return False
        elif move_col == 0 and move_row != 0:
            distance = move_row
        elif move_col != 0 and move_row == 0:
            distance = move_col
        elif move_col == move_row:
            return False
        
        if arrive_piece == 'x' or arrive_piece in White_team :   #'도착점'이 '말'이 아니고 '나의말'이 아니라면
            if start_r > arrive_pos[0] and move_row != 0 and move_col == 0:   #위로 이동하는 경우에
                for i in range(distance): 
                    if board[start_r - count][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r - count][start_c] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True
                        else:
                            count += 1
                            continue
        
            elif start_r < arrive_pos[0] and move_row != 0 and move_col == 0:   #아래로 이동하는 경우에
                for i in range(distance):
                    if board[start_r + count][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False #움직이던 도중에 최종목적지가 아닌데, piece가 있으면 False를 return
                    elif board[start_r + count][start_c] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True            
                        else:
                            count += 1
                            continue
                            
            elif start_c > arrive_pos[1] and move_col != 0 and move_row == 0:  #왼쪽으로 이동하는 경우에
                for i in range(distance):
                    if board[start_r][start_c - count] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일 경우 안됨
                    elif board[start_r][start_c - count] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True
                        else:
                            count += 1
                            continue
            elif start_c < arrive_pos[1] and move_col != 0 and move_row == 0:  #오른쪽으로 이동하는 경우에
                for i in range(distance):
                    if board[start_r][start_c + count] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:  #최종목적지가 우리팀일경우 안됨
                            return False
                    elif board[start_r][start_c + count] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True
                        else:
                            count += 1
                            continue
                    
                
        
    elif piece == 'h': #하얀 룩이라면
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
        count = 1
        distance = 0
        
        if move_row == 0 and move_col ==0:  #rook의 이동은 행으로만이동 또는 열로만 이동해야한다.
            return False
        elif move_col == 0 and move_row != 0:
            distance = move_row
        elif move_col != 0 and move_row == 0:
            distance = move_col
        elif move_col == move_row:
            return False
            
        if arrive_piece == 'x' or arrive_piece in Black_team :   #'도착점'이 '말'이 아니고, '나의말'이 아니라면
            if start_r > arrive_pos[0] and move_row != 0 and move_col == 0:   #위로 이동하는 경우에
                
                for i in range(distance): 
                    if board[start_r - count][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r - count][start_c] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True
                        else:
                            count += 1
                            continue
        
            elif start_r < arrive_pos[0] and move_row != 0 and move_col == 0:   #아래로 이동하는 경우에
                for i in range(distance):
                    if board[start_r + count][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False #움직이던 도중에 최종목적지가 아닌데, piece가 있으면 False를 return
                    elif board[start_r + count][start_c] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True            
                        else:
                            count += 1
                            continue
                            
            elif start_c > arrive_pos[1] and move_col != 0 and move_row == 0:  #왼쪽으로 이동하는 경우에
                for i in range(distance):
                    if board[start_r][start_c - count] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일 경우 안됨
                    elif board[start_r][start_c - count] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True
                        else:
                            count += 1
                            continue
            elif start_c < arrive_pos[1] and move_col != 0 and move_row == 0:  #오른쪽으로 이동하는 경우에
                for i in range(distance):
                    if board[start_r][start_c + count] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if count == distance:  #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:  #최종목적지가 우리팀일경우 안됨
                            return False
                    elif board[start_r][start_c + count] == 'x': #한칸식 이동하면서 확인하다가 도착점이면 True.
                        if count == distance:
                            return True
                        else:
                            count += 1
                            continue
                    
    elif piece == 'c':   #검은 나이트라믄!
        if start_r < end_r: #아래쪽이면
            down = True
            up = False
        else:               #위쪽이면
            down = False
            up = True
        if start_c < end_c: #오른쪽이면
            right = True
            left = False
        else:               #왼쪽이면
            right = False
            left = True
            
    
        if down and right: #오른쪽 아래로 이동하면?
            if end_r == start_r + 1 and end_c == start_c +2:  #오른쪽 아래 경우1.
                if (board[start_r+1][start_c+1] == 'x')or(board[start_r+1][start_r+1] in Black_team)or(board[start_r][start_c+1]=='x') or (board[start_r][start_c+1] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r + 2 and end_c == start_c +1:  #오른쪽 아래 경우2.
                if (board[start_r+1][start_c+1] == 'x')or(board[start_r+1][start_r+1] in Black_team)or(board[start_r+1][start_c]=='x') or (board[start_r+1][start_c] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
            
        elif down and left:  #왼쪽 아래로 이동하면?
            if end_r == start_r + 2 and end_c == start_c - 1:  #왼쪽 아래 경우1.
                if (board[start_r+1][start_c-1] == 'x')or(board[start_r+1][start_r-1] in Black_team)or (board[start_r+1][start_c]=='x') or (board[start_r+1][start_c] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r + 1 and end_c == start_c - 2:  #왼쪽 아래 경우2.
                if (board[start_r+1][start_c-1] == 'x')or(board[start_r+1][start_r-1] in Black_team)or (board[start_r][start_c-1]=='x') or (board[start_r][start_c-1] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
            
        elif up and right:   #오른쪽 위로 이동
            if end_r == start_r - 2 and end_c == start_c +1:  #오른쪽 아래 경우1.
                if (board[start_r-1][start_c+1] == 'x')or(board[start_r-1][start_r+1] in Black_team)or (board[start_r-1][start_c]=='x') or (board[start_r-1][start_c] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r - 1 and end_c == start_c + 2:  #오른쪽 아래 경우2.
                if (board[start_r-1][start_c+1] == 'x')or(board[start_r-1][start_r+1] in Black_team)or (board[start_r][start_c+1]=='x') or (board[start_r][start_c+1] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
            
        elif down and right:  #왼쪽 위로 이동?
            if end_r == start_r - 1 and end_c == start_c - 2:  #왼쪽 위 경우1.
                if (board[start_r-1][start_c-1] == 'x')or(board[start_r-1][start_r-1] in Black_team)or (board[start_r][start_c-1]=='x') or (board[start_r][start_c-1] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r - 2 and end_c == start_c - 1:  #왼쪽 위 경우2.
                if (board[start_r-1][start_c-1] == 'x')or(board[start_r-1][start_r-1] in Black_team)or (board[start_r-1][start_c]=='x') or (board[start_r-1][start_c] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
        else: #이도저도 아니면 그냥 짤
            return False
                    
            
    elif piece == 'i':   #하얀 나이트라믄!    
        if start_r < end_r: #아래쪽이면
            down = True
            up = False
        else:               #위쪽이면
            down = False
            up = True
        if start_c < end_c: #오른쪽이면
            right = True
            left = False
        else:               #왼쪽이면
            right = False
            left = True
            
    
        if down and right: #오른쪽 아래로 이동하면?
            if end_r == start_r + 1 and end_c == start_c +2:  #오른쪽 아래 경우1.
                if (board[start_r+1][start_c+1] == 'x')or(board[start_r+1][start_r+1] in White_team)or(board[start_r][start_c+1]=='x') or (board[start_r][start_c+1] in White_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r + 2 and end_c == start_c +1:  #오른쪽 아래 경우2.
                if (board[start_r+1][start_c+1] == 'x')or(board[start_r+1][start_r+1] in White_team)or(board[start_r+1][start_c]=='x') or (board[start_r+1][start_c] in White_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
            
        elif down and left:  #왼쪽 아래로 이동하면?
            if end_r == start_r + 2 and end_c == start_c - 1:  #왼쪽 아래 경우1.
                if (board[start_r+1][start_c-1] == 'x')or(board[start_r+1][start_r-1] in White_team)or(board[start_r+1][start_c]=='x') or (board[start_r+1][start_c] in White_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r + 1 and end_c == start_c - 2:  #왼쪽 아래 경우2.
                if (board[start_r+1][start_c-1] == 'x')or(board[start_r+1][start_r-1] in White_team)or(board[start_r][start_c-1]=='x') or (board[start_r][start_c-1] in White_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
            
        elif up and right:   #오른쪽 위로 이동
            if end_r == start_r - 2 and end_c == start_c +1:  #오른쪽 아래 경우1.
                if (board[start_r-1][start_c+1] == 'x')or(board[start_r-1][start_r+1] in White_team)or(board[start_r-1][start_c]=='x') or (board[start_r-1][start_c] in White_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r - 1 and end_c == start_c + 2:  #오른쪽 아래 경우2.
                if (board[start_r-1][start_c+1] == 'x')or(board[start_r-1][start_r+1] in Black_team)or (board[start_r][start_c+1]=='x') or (board[start_r][start_c+1] in Black_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
            
        elif down and right:  #왼쪽 위로 이동?
            if end_r == start_r - 1 and end_c == start_c - 2:  #왼쪽 위 경우1.
                if (board[start_r-1][start_c-1] == 'x')or(board[start_r-1][start_r-1] in White_team)or(board[start_r][start_c-1]=='x') or (board[start_r][start_c-1] in White_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            elif end_r == start_r - 2 and end_c == start_c - 1:  #왼쪽 위 경우2.
                if (board[start_r-1][start_c-1] == 'x')or(board[start_r-1][start_r-1] in White_team)or(board[start_r-1][start_c]=='x') or (board[start_r-1][start_c] in White_team):
                    return True #한경로라도 이동할수 있는 경로가 있으면 가능
                else:
                    return False
            else:
                return False
        else: #이도저도 아니면 그냥 짤
            return False
    
    elif piece == 'd':   #검은 비숍일때
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        move_count = int(m.sqrt((move_row*move_row) + (move_col*move_col))) #움직일 횟수
        
        if (move_row != move_col) or (start_r == end_r and start_c == end_c): #대각선이동이 아니면 False리턴
            return False       
        
        if start_r < end_r: #아래쪽이면
            down = True
            up = False
        else:               #위쪽이면
            down = False
            up = True
        if start_c < end_c: #오른쪽이면
            right = True
            left = False
        else:               #왼쪽이면
            right = False
            left = True
            
        if arrive_piece == 'x' or arrive_piece in White_team :   #'도착점'이 '말'이 아니거나, 적팀이라면
            if left and up:  #'왼쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif left and down:  #'왼쪽 아래'라면 방향 이라면
                for i in range(move_count):
                    start_r += 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                        
            elif right and up:  #'오른쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c += 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.                            
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif right and down:  #'오른쪽아래'라면 방향 이라면
                count = 0
                for i in range(move_count):
                    start_r += 1
                    start_c += 1
                    count += 1
                    print ('여기까지')
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
                            
    elif piece == 'j':   #하얀 비숍일때
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        move_count = int(m.sqrt((move_row*move_row) + (move_col*move_col))) #움직일 횟수
        
        if (move_row != move_col) or (start_r == end_r and start_c == end_c): #대각선이동이 아니면 False리턴
            return False       
        
        if start_r < end_r: #아래쪽이면
            down = True
            up = False
        else:               #위쪽이면
            down = False
            up = True
        if start_c < end_c: #오른쪽이면
            right = True
            left = False
        else:               #왼쪽이면
            right = False
            left = True
        print (up,down,right,left)   
        if arrive_piece == 'x' or arrive_piece in Black_team :   #'도착점'이 '말'이 아니거나, 적팀이라면
            if left and up:  #'왼쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif left and down:  #'왼쪽 아래'라면 방향 이라면
                for i in range(move_count):
                    start_r += 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                        
            elif right and up:  #'오른쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c += 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.                            
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif right and down:  #'오른쪽아래'라면 방향 이라면
                
                for i in range(move_count):
                    start_r += 1
                    start_c += 1
                  
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
    
    elif piece == 'e':  #검은퀸일때
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        move_count = int(m.sqrt((move_row*move_row) + (move_col*move_col))) #움직일 횟수      
        
        if start_r < end_r:  #아래쪽이면
            down = True
            up = False
        elif start_r > end_r:#위쪽이면
            down = False
            up = True
        elif start_r == end_r: #행은 움직이지 않는다면
            down = False
            up = False
            
        if start_c < end_c:  #오른쪽이면
            right = True
            left = False
        elif start_c > end_c:  #왼쪽이면
            right = False
            left = True
        elif start_c == end_c:
            right = False
            left = False
            
        if arrive_piece == 'x' or arrive_piece in White_team :   #'도착점'이 '말'이 아니거나, 적팀이라면
            if left and up:  #'왼쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif left and down:  #'왼쪽 아래'라면 방향 이라면
                for i in range(move_count):
                    start_r += 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                        
            elif right and up:  #'오른쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c += 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.                            
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif right and down:  #'오른쪽아래'라면 방향 이라면
            
                for i in range(move_count):
                    start_r += 1
                    start_c += 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
            
            elif (up) and (not down) and (not right) and (not left): #위로만 올라갈때
                 for i in range(move_count):
                    start_r -= 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
            elif (not up) and (down) and (not right) and (not left): #아래로만 올라갈때
                 for i in range(move_count):
                    start_r += 1
                 
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif (not up) and (not down) and (not right) and (left): #왼쪽으로만 갈때
                 for i in range(move_count):
                    start_c -= 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
            
            elif (not up) and (not down) and (right) and (not left): #'오른쪽'으로만 갈때
        
                 for i in range(move_count):
                    start_c += 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue

    elif piece == 'k':  #흰퀸일때
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        move_count = int(m.sqrt((move_row*move_row) + (move_col*move_col))) #움직일 횟수      
        
        if start_r < end_r:  #아래쪽이면
            down = True
            up = False
        elif start_r > end_r:#위쪽이면
            down = False
            up = True
        elif start_r == end_r: #행은 움직이지 않는다면
            down = False
            up = False
            
        if start_c < end_c:  #오른쪽이면
            right = True
            left = False
        elif start_c > end_c:  #왼쪽이면
            right = False
            left = True
        elif start_c == end_c:
            right = False
            left = False
            
        if arrive_piece == 'x' or arrive_piece in Black_team :   #'도착점'이 '말'이 아니거나, 적팀이라면
            if left and up:  #'왼쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif left and down:  #'왼쪽 아래'라면 방향 이라면
                for i in range(move_count):
                    start_r += 1
                    start_c -= 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                        
            elif right and up:  #'오른쪽 위'라면 방향 이라면
                for i in range(move_count):
                    start_r -= 1
                    start_c += 1
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                            #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다.                            
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x': #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] or start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif right and down:  #'오른쪽아래'라면 방향 이라면
            
                for i in range(move_count):
                    start_r += 1
                    start_c += 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 piece가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #최종목적지에는 적이 있기로했고, 'x'가 아니므로 적일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
            
            elif (up) and (not down) and (not right) and (not left): #위로만 올라갈때
                 for i in range(move_count):
                    start_r -= 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
            elif (not up) and (down) and (not right) and (not left): #아래로만 올라갈때
                 for i in range(move_count):
                    start_r += 1
                 
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
                            
            elif (not up) and (not down) and (not right) and (left): #왼쪽으로만 갈때
                 for i in range(move_count):
                    start_c -= 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue
            
            elif (not up) and (not down) and (right) and (not left): #'오른쪽'으로만 갈때
        
                 for i in range(move_count):
                    start_c += 1
        
                    if board[start_r][start_c] != 'x':  #움직이던 도중에 'piece'가 있다면 안된다.
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]: 
                        #'최종목적지'에는 적이 있기로했고, 'x'가 아니므로 '적'일경우이다
                            return True
                        else:
                            return False  #최종목적지가 우리팀일경우는 안됨
                    elif board[start_r][start_c] == 'x':  #'한칸식 이동'하면서 확인
                        if start_r == arrive_pos[0] and start_c == arrive_pos[1]:
                            #최종목적지에는 무조건 적이 있기로했었고, 'x'이므로 return True
                            return True   
                        else:  #한칸씩 이동했는데 도착점이 아니면 ? return True 음
                            continue        
        
    elif piece == 'f': #만약 '검은퀸' 이라면
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        move_count = int(m.sqrt((move_row*move_row) + (move_col*move_col))) #움직일 횟수      
        
        if move_count == 1:
            if arrive_piece == 'x' or arrive_piece in White_team :   #'도착점'이 '말'이 아니거나, 적팀이라면
                return True
            else:
                return False
        else:
            return False
    
    elif piece == 'f': #만약 '검은퀸' 이라면
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        move_count = int(m.sqrt((move_row*move_row) + (move_col*move_col))) #움직일 횟수      
        
        if move_count == 1:
            if arrive_piece == 'x' or arrive_piece in White_team :   #'도착점'이 '말'이 아니거나, 적팀이라면
                return True
            else:
                return False
        else:
            return False
                    
    elif piece == 'l': #만약 '검은퀸' 이라면
        move_row = abs(start_r - arrive_pos[0]) #'행' 의 거리  -> 이동경로에 상대팀 말이나 우리팀 말이 있는지 확인하기 위함
        move_col = abs(start_c - arrive_pos[1]) #'열' 의 거리
    
        move_count = int(m.sqrt((move_row*move_row) + (move_col*move_col))) #움직일 횟수      
        
        if move_count == 1:
            if arrive_piece == 'x' or arrive_piece in Black_team :   #'도착점'이 '말'이 아니거나, 적팀이라면
                return True
            else:
                return False
        else:
            return False
