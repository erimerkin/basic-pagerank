import argparse

def read_file(file_name):
    """Reads a file and returns its contents as a list of strings."""
    with open(file_name, 'r') as f:
        verticeInfo = f.readline()  # Skip the first line
        
        splitVerticeInfo = verticeInfo.split()
        
        if len(splitVerticeInfo) != 2:
            raise Exception("Invalid file format")
        
        verticeCount = int(splitVerticeInfo[1])
        
        vertices = {}
        
        adjacencyMatrix = [[0 for _ in range(verticeCount)] for _ in range(verticeCount)]
        
        for _ in range(verticeCount):
            verticeLine = f.readline()
            splitVerticeLine = verticeLine.split()
            
            vertices[int(splitVerticeLine[0])] = splitVerticeLine[1].replace('"', '')
            
        edgeInfo = f.readline()
                
        if edgeInfo.strip() == "*Edges":
            edge_cnt = 0
            for line in f:
                edge_cnt += 1
                splitEdgeLine = line.split()
                
                adjacencyMatrix[int(splitEdgeLine[0])-1][int(splitEdgeLine[1])-1] = 1
                adjacencyMatrix[int(splitEdgeLine[1])-1][int(splitEdgeLine[0])-1] = 1
                                
            return vertices, adjacencyMatrix
        else:
            raise Exception("Invalid file format")
    

    
    
def power_iteration(A, teleportation, threshold=0.0000001, max_iterations=500):
    # Get node count
    N = len(A)
    
    # Calculate teleportation rate for each node
    teleport_rate = teleportation/N

    # Initialize matrix x
    x = [1] * N
    
    # Convert adjacency matrix to a matrix of probabilities
    a_matrix = []    
    for i in range(N):
        vertices_in_row = sum(A[i])
        row = []
        for j in range(N):
            if A[i][j] == 1:
                row.append(teleport_rate + (1-teleportation)/vertices_in_row)
            else:
                row.append(teleport_rate)
                
        a_matrix.append(row)
        
    #Init conditions
    under_threshold = False  
    itr_count = 0

    # Power iteration
    while (not(under_threshold) and itr_count < max_iterations):
        itr_count += 1
        
        # Calculate matrix multiplication
        x_new = []
        for i in range(len(A)):
            summation = 0
            for j in range(len(A[i])):
                summation += a_matrix[j][i] * x[j]
                
            x_new.append(summation)
        
        # Check if all values are under threshold
        differences = []
        for i in range(len(x)):
            if abs(x[i] - x_new[i]) < threshold:
                differences.append(True)
            else:
                differences.append(False)
                
        x = x_new
        
        # If all values are under threshold, set under_threshold to True
        if not(False in differences):
            under_threshold = True
            
    return x
    
def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input", help="The name of the file to read from.")
    arg_parser.add_argument("output", help="The name of the file to write to.")
    arg_parser.add_argument("-teleportation", "-t", help="The teleportation rate.", type=float, default=0.10)
    arg_parser.add_argument("-threshold", "-th", help="The threshold for the power iteration.", type=float, default=0.000001)
    arg_parser.add_argument("-maxiter", "-m", help="The maximum number of iterations for the power iteration.", type=int, default=500)
    
    args = arg_parser.parse_args()
    vertices, adjacencyMatrix = read_file(args.input)

    result = power_iteration(adjacencyMatrix, args.teleportation, threshold=args.threshold, max_iterations=args.maxiter)
    
    sorted_results = []
    for i in range(len(result)):
        sorted_results.append((i+1, result[i]))
        
    top_results= sorted(sorted_results, key=lambda x: x[1], reverse=True)
    
    top20 = [(vertices[i[0]], i[1]) for i in top_results[:20]]
            
    print("TOP 20")
    for i in top20:
        print(f"{i[0]}: {round(i[1], 4)}")
        
    with open(args.output, 'w') as f:
        for i in top_results:
            f.write(f"{i[0]}: {round(i[1], 4)}\n")
        
    print(f"Results written to {args.output}")
    
if __name__ == "__main__":
    main()