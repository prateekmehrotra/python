__author__ = 'PrateekMehrotra'
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])