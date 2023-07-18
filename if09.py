def main(a):
    x=a//10
    y=a%10
    b=y*10+x
    if  (a>b or a==b):
        return True
    else:
        return False
print(main(13))

"""
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
