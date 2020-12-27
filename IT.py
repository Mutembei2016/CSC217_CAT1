def CSC_217_Seperated(f2):
  dOut = {}
  with open('CSC_217_attendance_ week1_.txt') as f:
     for l in f:
        dOut[ l.split(':')[0] ] = l.split(':')[1]

  return dOut


def makeDict(f2):
    pass


def merge(f1,f2,f3):

  pwd = makeDict(f2)
  print pwd
  with open(f3, "a") as outputFile:

     with open(f1) as usernameFile:
        for line in usernameFile:
           if line.strip() == '': continue
           username = line.split(':')[0]
           lastname = line.split(':')[3]
           if lastname in pwd:
              outputFile.write(username + ':' + pwd[lastname] + '\n')


