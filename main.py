import sys

encrypt = sys.stdin.readline()[:-1]

decrypt = []

for x in encrypt:
  if len(decrypt) != 0 and decrypt[-1] == x:
    decrypt.pop()
  else:
    decrypt.append(x)

print("".join(str(x) for x in decrypt))
