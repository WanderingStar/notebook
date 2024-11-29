
from os import listdir, rename
from os.path import isdir

header = '### Navigation\n'

# assume flat structure
for dir in sorted([d for d in listdir('.') if isdir(d)]):
    if not dir[0].isalpha():
        continue
    for f in sorted([f"{f}" for f in listdir(dir) if f.endswith('.cross')]):
        base = f[:-len('.cross')]
        print(f"{dir}/{f} ->\n{dir}/{base}\n")
        rename(f"{dir}/{f}", f"{dir}/{base}")
