hr1,mi1=map(int,input().split())
hr2,mi2=map(int,input().split())
if(hr1>hr2):
    hrs=(hr1-hr2)*60
    h=hrs
    min=((mi1-mi2)*60)
    print(abs(h//60),abs(min//60))
else:
    hr=(hr2-hr1)*60
    h=hr
    min=((mi1-mi2)*60)
    print(abs(h//60),abs(min//60))
    



