rj=0
bh=0
sc=0
while True:
    ps1=input("digite sua cidade: ")
    if(ps1=='rj'):
        rj=+1
    if(ps1=='bh'):
        bh=+1
    if(ps1=='sc'):
        sc=+1
    if(ps1=="fim"):
        break
print("essa pessao e do rio de janeiro: ",rj)
print("essa pessoa e de  belo horizonte: ",bh)
print("essa pessoa e de santa catarina: ",sc)
