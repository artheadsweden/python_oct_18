import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("square", type=int, help="display the square of this number")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase the output verbosity")

    args = parser.parse_args()
    answer = args.square**2
    if args.verbose >= 2:
        print(f"the square of {args.square} is {answer}")
    elif args.verbose == 1:
        print(f"{args.square}^2 = {answer}")
    else:
        print(answer)



if __name__ == '__main__':
    main()
