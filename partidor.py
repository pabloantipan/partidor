filename = ""
limit = 600000

with open('filename') as f:
  lines = f.read().splitlines()

with open('first_half.json', 'w') as fh:
  for idx in range (0, limit):
    fh.write(lines[idx])

with open('second_half.json', 'w') as sh:
  for idx in range (limit+1, len(lines)):
    sh.write(lines[idx])



