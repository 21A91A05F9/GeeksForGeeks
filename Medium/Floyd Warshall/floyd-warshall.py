#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n=len(matrix)
		for i in range(n):
		    for j in range(n):
		        if matrix[i][j]==-1:
		            matrix[i][j]=float('inf')
		#print(matrix)
		for k in range(n):
		    for i in range(n):
		        if i==k:
		            continue
		        for j in range(n):
		            if j==k:
		                continue
		            if matrix[i][j]>matrix[i][k]+matrix[k][j]:
		                #print(matrix[i][j],matrix[i][k]+matrix[k][j)
		                matrix[i][j]=matrix[i][k]+matrix[k][j]
		  
		            
		            


#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends