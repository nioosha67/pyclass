#Nioosha Asadi Moghadas Thursday 14-18
#mohasebe mohit ya masahate ashkale hendesi

def Mohasebe(scale1,scale2,shape,req):
    if (shape=='square') and (req=='masahat' or req=='mohit'):
        print(' barabar ast ba:' , scale1*scale2)
    elif shape=='rectangle' and req=='mohit':
        print('mohit barabar ast ba:', 2*(scale1+scale2))
    elif shape=='rectangle' and req=='masahat':
        print('masahat barabar ast ba:' , scale1*scale2)
    elif shape=='triangle' and reg=='masahat':
        print('masahat barabar ast ba:' , (scale1*scale2)/2)
    else:
        print('mohit mosalase motesaviolazla barabar ast ba:', 3*scale1)
Mohasebe(2,3,'rectangle','mohit')
