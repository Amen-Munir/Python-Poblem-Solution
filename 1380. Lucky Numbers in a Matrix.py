
matrix = [[3,7,8],
          [9,11,13],
          [15,16,17]]
row=len(matrix)
col=len(matrix[0])

for i in range(row):
    row_min=min(matrix[i])
    index=matrix[i].index(row_min)

    checkMax=True
    for j in range(row):
        if(row_min<matrix[j][index]):
            checkMax=False
    
    if checkMax:
        print(row_min)


       