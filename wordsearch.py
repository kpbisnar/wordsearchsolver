
def get_words(n,words):   
    while n.isdigit()!=True or int(n)==0:
        n=input('Please input only positive number: ')
    else:
        n=int(n)
        i=1     # i is the counter
        for i in range(n):
            i+=1
            wor=input('Input word #{}: '.format(i))
            while len(wor)>15 or wor.isalpha()!=True:
                wor=input('Input word #{} (Maximum of 15 characters (must only contain letters): '.format(i))
            else:
                words.append(wor.upper())
    
def sort_words(words):
    words.sort()

def print_words(words):
        print('SORTED WORDS:')
        for wor in words:
            print(wor)

def populate_board(m,board, final_m):
    while m.isdigit()!=True or int(m)==0:
        m=input('Please input only positive integers: ')
    else:    
        m=int(m)
        final_m.append(m)
        for i in range(1, m+1):
            y=m
            x=input('Enter row #{}: '.format(i))
            while x.isalpha()!=True or y!=len(x):
                x=input('Re-enter row #{}: '.format(i))
            else:
                board.append(x.upper())             
    
def print_board(board):
    for i in board:
        print(" ".join(i))

def search_words(final_m, board, words, solutions):
    for m in final_m:
        m=int(m)
    def right(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_x>=m:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break
            i+=1
            dir_x+=1
        x.append("".join(y))
        for w in x:
            return w
    def up(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_y<0:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break
            i+=1
            dir_y-=1
        x.append("".join(y))
        for w in x:
            return w
    def left(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_x<0:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break
            i+=1
            dir_x-=1
        x.append("".join(y))
        for w in x:
            return w
    def down(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_y>=m:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break        
            i+=1
            dir_y+=1
        x.append("".join(y))
        for w in x:
            return w
    def right_down(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_x>=m or dir_y>=m:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break
            i+=1
            dir_x+=1
            dir_y+=1
        x.append("".join(y))
        for w in x:
            return w
    def right_up(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_y<0 or dir_x>=m:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break
            i+=1
            dir_y-=1
            dir_x+=1
        x.append("".join(y))
        for w in x:
            return w
    def left_down(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_x<0 or dir_y>=m:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break
            i+=1
            dir_y+=1
            dir_x-=1
        x.append("".join(y))
        for w in x:
            return w
    def left_up(word, dir_x, dir_y):
        i=0
        y=[]
        x=[]
        while i<len(word):
            if dir_y<0 or dir_x<0:
                break
            else:
                if word[i]==board[dir_y][dir_x]:
                    y.append(word[i])
                elif word[i]!=board[dir_y][dir_x]:
                    break        
            i+=1
            dir_y-=1
            dir_x-=1
        x.append("".join(y))
        for w in x:
            return w
                
    for word in words:
        for dir_y in range(m):
            for dir_x in range(m):
                if right(word, dir_x , dir_y)==word:
                    direction='right'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                elif down(word, dir_x, dir_y)==word:
                    direction='down'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                elif left(word, dir_x, dir_y)==word:
                    direction='left'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                elif up(word, dir_x, dir_y)==word:
                    direction='up'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                elif right_down(word, dir_x , dir_y)==word:
                    direction='right-down'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                elif right_up(word, dir_x, dir_y)==word:
                    direction='right-up'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                elif left_down(word, dir_x, dir_y)==word:
                    direction='left-down'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                elif left_up(word, dir_x, dir_y)==word:
                    direction='left-up'
                    solutions[word]=(dir_x, dir_y),direction
                    break
                    
def print_solutions(solutions):
    print('Solutions:')
    for i in solutions:
        print(i, ':', solutions[i][0], '-', solutions[i][1])

def edit_word(solutions, board):
    yellow=[]
    for word in solutions:
        if solutions[word][1]=='right':
            i=1 				#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                x+=1
                position=(x, y)
                yellow.append(position)
                i+=1
            
        elif solutions[word][1]=='left':
            i=1		#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                x-=1
                position=(x, y)
                yellow.append(position)
                i+=1
            
        elif solutions[word][1]=='down':
            i=1		#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                y+=1
                position=(x, y)
                yellow.append(position)
                i+=1
            
        elif solutions[word][1]=='up':
            i=1		#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                y-=1
                position=(x, y)
                yellow.append(position)
                i+=1
            
        elif solutions[word][1]=='right-down':
            i=1	#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                x+=1
                y+=1
                position=(x, y)
                yellow.append(position)
                i+=1

        elif solutions[word][1]=='left-down':
            i=1		#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                x-=1
                y+=1
                position=(x, y)
                yellow.append(position)
                i+=1

        elif solutions[word][1]=='right-up':
            i=1		#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                y-=1
                x+=1
                position=(x, y)
                yellow.append(position)
                i+=1

        elif solutions[word][1]=='left-up':
            i=1		#i is the counter
            x=solutions[word][0][0]
            y=solutions[word][0][1]
            while i<len(word):
                y-=1
                x-=1
                position=(x, y)
                yellow.append(position)
                i+=1
    
    red=[]
    for word in solutions:
        red.append(solutions[word][0])
    

    
    for y in range(len(board)):
        for x in range(len(board)):
            location=(x, y)
            for row in board:
                if location in red:
                    if x<((len(board))-1):
                        print(("\033[1;31m{}\033[0m".format(board[y][x])), end=" ")
                        break
                    else:
                        print("\033[1;31m{}\033[0m".format(board[y][x]))
                        break
                elif location in yellow:
                    if x<((len(board))-1):
                        print(("\033[1;33m{}\033[0m".format(board[y][x])), end=" ")
                        break
                    else:
                        print("\033[1;33m{}\033[0m".format(board[y][x]))
                        break
                else:
                    if x<((len(board))-1):
                        print((board[y][x].lower()), end=" ")
                        break
                    else:
                        print(board[y][x].lower())
                        break
               
def main():
    words=[]
    n=(input('Enter number of words: '))
    get_words(n,words)
    sort_words(words)
    print_words(words)
    m=(input('Input m:'))
    board=[]
    final_m=[]
    populate_board(m,board, final_m)
    print_board(board)
    solutions={}
    search_words(final_m, board, words, solutions)
    print_solutions(solutions)
    edit_word(solutions, board)
    
main()






