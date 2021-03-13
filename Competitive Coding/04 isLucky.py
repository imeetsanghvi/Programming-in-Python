def isLucky(n):
      
  x = str(n)
  y = reversed(x)

  x = list(x)
  y = list(y)

  half = int(len(x)/2)
  fh = [0]*half
  sh = [0]*half
  fhs = 0
  shs = 0

  for i in range(0,half):
    fh[i] = x[i]
    fhs = fhs + int(fh[i])
  for i in range(0,half):
    sh[i] = y[i]
    shs = shs + int(sh[i])
  if fhs == shs:
    print(True)
  else:
    print(False)

if __name__ == '__main__':
    print("""
Question
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.


Example
For n = 1230, the output should be isLucky(n) = true;
For n = 239017, the output should be isLucky(n) = false.
    """)
    isLucky(239017)