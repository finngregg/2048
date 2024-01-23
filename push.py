def push_up (grid):
    """merge grid values upwards"""
    for i in range (1,4):                       
        for x in range(1,4):                    
            for z in range(4):                  
                if grid[x-1][z] == 0:           
                    grid[x-1][z] = grid[x][z]
                    grid[x][z] = 0       
    for i in range(3):                                             
        for x in range(4):                      
            if grid[i][x] == grid[i+1][x]:      
                grid[i][x] = grid[i][x]*2       
                grid[i+1][x] = 0
    for i in range(1,4):                        
        for x in range(1,4):                    
            for z in range(4):                  
                if grid[x-1][z] == 0:
                    grid[x-1][z] = grid[x][z]
                    grid[x][z] = 0                           
    for i in range (1,4):                       
        for x in range(1,4):                    
            for z in range(4):                  
                if grid[x-1][z] == 0:           
                    grid[x-1][z] = grid[x][z]
                    grid[x][z] = 0    
    return grid  

def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
        for x in range(3, 0, -1):
            if grid[x][i]==0:
                for z in range(x-1, -1,-1):
                    if grid[z][i]!=0:
                        grid[x][i] = grid[z][i]
                        grid[z][i]=0
                        break
                        
        if(grid[3][i]==grid[2][i]):
            grid[3][i] += grid[2][i]
            grid[2][i]=0
        if(grid[2][i]==grid[1][i]):
            grid[2][i] += grid[1][i]
            grid[1][i]=0
        if(grid[1][i]==grid[0][i]):
            grid[1][i] += grid[0][i]
            grid[0][i]=0
        
        for x in range(3, 0, -1):
            if grid[x][i]==0:
                for z in range(i-1, -1,-1):
                    if grid[z][i]!=0:
                        grid[x][i] = grid[z][i]
                        grid[z][i]=0
                        break  
                    
def push_left (grid):                           
    """merge grid values left"""
    for x in range (1,4):                       
        for i in range(4):                      
            for z in range(1,4):                
                if grid[i][z-1] == 0:
                    grid[i][z-1] = grid[i][z]
                    grid[i][z] = 0
    for x in range(4):                           
        for z in range(3):                      
            if grid[x][z] == grid[x][z+1]:
                grid[x][z] = grid[x][z]*2
                grid[x][z+1] = 0
    for x in range(1,4):                        
        for i in range(4):                      
            for z in range(1,4):                
                if grid[i][z-1] == 0:
                    grid[i][z-1] = grid[i][z]
                    grid[i][z] = 0            
    return grid

def push_right (grid):
    """merge grid values right"""
    for i in range(4):
        for z in range(3, 0, -1):
            if grid[i][z]==0:
                for x in range(z-1, -1,-1):
                    if grid[i][x]!=0:
                        grid[i][z] = grid[i][x]
                        grid[i][x]=0
                        break
                            
        if(grid[i][3]==grid[i][2]):
            grid[i][3] += grid[i][2]
            grid[i][2]=0
        if(grid[i][2]==grid[i][1]):
            grid[i][2] += grid[i][1]
            grid[i][1]=0
        if(grid[i][1]==grid[i][0]):
            grid[i][1] += grid[i][0]
            grid[i][0]=0
            
        for z in range(3, 0, -1):
            if grid[i][z]==0:
                for x in range(z-1, -1,-1):
                    if grid[i][x]!=0:
                        grid[i][z] = grid[i][x]
                        grid[i][x]=0
                        break