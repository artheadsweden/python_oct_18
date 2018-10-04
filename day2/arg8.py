import argparse

def main():
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")

    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type= int, help="the exponent")

    parser.add_argument("-v", "--verbose", action="store_true", help="increase the output verbosity")
    parser.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()
    answer = args.x**args.y
    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.x} to the power of {args.y} is {answer}")
    else:
        print(f"{args.x}^{args.y} = {answer}")





if __name__ == '__main__':
    main()
