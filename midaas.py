import time
import argparse
def prime(start,end):
    res=[]
    for i in range(start,end+1):
        c=0
        for j in range(1,(i//2)+1):
            if i%j==0:
                c+=1
        if c==1:
            res.append(i)
    return res

def mahi(start,end):
    res=[]
    for i in range(start,end+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            res.append(i)
    return res




def main():
    parse=argparse.ArgumentParser(description="Prime number generator")
    parse.add_argument("start",type=int,help="Start of the range")
    parse.add_argument("end",type=int,help="End of the range")
    parse.add_argument("--strategy",choices=["prime","mahi"],default="prime",help="Prime number generation strategy")
    args=parse.parse_args()
    start,end=min(args.start,args.end),max(args.start,args.end)
    t1=time.time()
    if args.strategy=="prime":
        res=prime(start,end)
    elif args.strategy=="mahi":
        res=prime(start,end)
    t2=time.time()
    print("prime numbers between {} and {}:{}".format(start,end,res))
    print("time taken:{}".format(t2-t1))

if __name__ == "__main__":
    main()
        
            
            