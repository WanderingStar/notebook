
from os import listdir
from os.path import isdir

header = '### Navigation\n'

# assume flat structure
for dir in sorted([d for d in listdir('.') if isdir(d)]):
    if not dir[0].isalpha():
        continue

    files = sorted([f for f in listdir(dir) if f.endswith('.md')])
    if len(files) < 2:
        continue

    if 'README.md' in files:
        files.remove('README.md')
        files.insert(0, 'README.md')
    print(f"{dir}: \n  " + "\n  ".join(files))
    navblock = header
    for file in files:
        navblock += f"* [{file[:-3]}]({file.replace(' ', '%20')})\n"
    navblock += '\n'
    
    for file in files:
        with open(f"{dir}/{file}.cross", 'w') as outfile, open(f"{dir}/{file}", 'r') as infile:
            flag = 'pre'
            for line in infile:
                if flag == 'pre':
                    if line != header:
                        outfile.write(line)
                    else:
                        flag = 'in'
                        outfile.write(navblock)
                elif flag == 'in':
                    if line != '\n':
                        continue
                    else:
                        flag = 'post'
                else:
                    outfile.write(line)
            if flag == 'pre':
                outfile.write("\n\n")
                outfile.write(navblock)
