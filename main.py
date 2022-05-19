import matplotlib.pyplot as plt

def unipolar(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    for n,i in enumerate(inp1):
        if i == 0:
            inp1[n] = 1
        else:
            inp1[n] = 0
    return inp1
    

def polar_nrz_l(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    inp1=[-1 if i==0 else 1 for i in inp1]
    return inp1

def polar_nrz_i(inp):
    inp2=list(inp)
    inp2.insert(0,0)
    lock=False
    for i in range(len(inp2)):
        if inp2[i]==1 and not lock:
            lock=True
            continue
        if lock and inp2[i]==1:
            if inp2[i-1]==0:
                inp2[i]=1
                continue
            else :
                inp2[i]=0
                continue
        if lock:
            inp2[i]=inp2[i-1]
    inp2=[0 if i==0 else 1 for i in inp2]        
    return inp2
    

def pseudo(inp):
    inp1=list(inp)

    li = []
    state = 'X'
    if inp1[0] == 0:
        inp1[0] = 1
        li.append(1)
        li.append(1)
        li.append(1)
        li.append(1)
        state = 'P'
    else:
        inp1[0] = 0
        li.append(0)
        li.append(0)
        li.append(0)
        li.append(0)
        state = 'N'


    for n,i in enumerate(inp1):
        if n != 0:
            if i == 1:
                inp1[n] = 0
                li.append(0)
                li.append(0)
                li.append(0)
                li.append(0)
            elif i == 0 and state == 'P':
                inp1[n] = -1
                li.append(-1)
                li.append(-1)
                li.append(-1)
                li.append(-1)
                state = 'N'
            elif i == 0 and state == 'N':
                inp1[n] = 1
                li.append(1)
                li.append(1)
                li.append(1)
                li.append(1)
                state = 'P'
    inp1.insert(0,0)
    return li
    

def Biphase_manchester(inp):
    inp1=list(inp)
    li = []
    if inp1[0] == 0:
        li.append(-1)
        li.append(-1)
        li.append(0)
        li.append(0)
    else:
        li.append(0)
        li.append(0)
        li.append(-1)
        li.append(-1)

    for n,i in enumerate(inp1):
        if n != 0:
            if i == 1:
                li.append(0)
                li.append(0)
                li.append(-1)
                li.append(-1)
            elif i == 0:
                li.append(-1)
                li.append(-1)
                li.append(0)
                li.append(0)
    
    #li.insert(0,0)
    return li


    

def Differential_manchester(inp):
    inp1=list(inp)
    li = []
    if inp1[0] == 0:
        li.append(-1)
        li.append(0)
        #transicion mitad
        li.append(-1)
        li.append(-1)
        state = '1'
    else: 
        li.append(0)
        li.append(0)
        li.append(-1)
        li.append(-1)
        state = '1'

    for n,i in enumerate(inp1):
        if n != 0:
            if i == 1 and state == '1':
                li.append(-1)
                li.append(-1)
                li.append(0)
                li.append(0)
                state = '0'
            elif i == 1 and state == '0':
                li.append(0)
                li.append(0)
                li.append(-1)
                li.append(-1)
                state = '1'
            elif i == 0 and state == '0':
                li.append(-1)
                li.append(-1)
                li.append(0)
                li.append(0)
                state = '0'
            elif i == 0 and state == '1':
                li.append(0)
                li.append(0)
                li.append(-1)
                li.append(-1)
                state = '1'
                         
    return li                        


def AMI(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    lock=False
    for i in range(len(inp1)):
        if inp1[i]==1 and not lock:
            lock=True
            continue
        elif lock and inp1[i]==1:
            inp1[i]=-1
            lock=False
    return inp1  

    

def plot(li):
    plt.subplot(7,1,1)
    plt.ylabel("NRZ-L")
    plt.plot(unipolar(li),color='black',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,3)
    plt.ylabel("AMI")
    plt.plot(AMI(li),color='black',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,2)
    plt.ylabel("NRZI")
    plt.plot(polar_nrz_i(li),color='black',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,4)
    plt.ylabel("pseudo")
    plt.plot(pseudo(li),color='black',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,5)
    plt.ylabel("man")
    plt.plot(Biphase_manchester(li),color='black',drawstyle='steps-pre',marker='>')
    plt.subplot(7,1,6)
    plt.ylabel("man_d")
    plt.plot(Differential_manchester(li),color='black',drawstyle='steps-pre',marker='>')
    plt.show()
                

if __name__=='__main__':
    la = [0,1,0,0,1,1,0,0,0,1,1]
    plot(la) 
