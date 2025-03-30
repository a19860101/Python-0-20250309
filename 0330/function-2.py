def foo(*args):
    # print(type(args))
    for item in args:
        print(item, end=' ')
# foo(1,2,3,4,'hello')


def foo2(**kwargs):
    # print(type(kwargs))
    for k,v in kwargs.items():
        print(f'{k}:{v}')

foo2(name="Tim",mail='asdf@gmail.com',age=19)


def foo3(x,y,*args,**kwargs):
    # print(x,y,args,kwargs)
    result = list(args)
    print(type(result))
foo3(100,80,999,888,n=10,name='test')

