def gen_terms(nterm: str, limit: int, start: int = 0) -> list:
    """
    Given a LaTeX representation of the nth term of a series and the max interation value of n, 
    returns list of LaTeX code that represents the first few terms of that series.
    Function also includes customizable start variable. 
    Function does not evaulate expressions. 
    """
    output = list()
    for n in range(0, limit + 1, start):    
        output.append(nterm.replace("n", str(n)))
    return output

def output_file(content: str):
    with open("output.txt", "w") as f:
        f.write(content)

def main():
    nterm: str = input("Enter LaTeX form of the nth term of the series: ")
    limit: int = int(input("Enter the max iteration value of n: "))
    start = input("Enter start value (defaults to 0): ")
    if start == "":
        start = 0
    else:
        start = int(start)
    output = gen_terms(nterm, limit, start)

    output_file(" + ".join(output))

if __name__ == "__main__":
    main()


