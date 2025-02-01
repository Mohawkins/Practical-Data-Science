def my_function(a: int, b: int) -> int:
    """
    my_fuction provides addition given two integers provided by user

    Input arg:
      a: int
      b: int
    Return:
      c: int
    """

    c = a+b
    
    return c

    var1 = int(Input("Enter an integer:"))
    var2 = int(Input("Enter an integer:"))
    var3 = my_function(var1, var2)
    print("answer is", var3)
    