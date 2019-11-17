import sys
import timeit
import challenge_1A


def time(challenge, args):
    setup = f'from challenge_{challenge} import challenge'
    return timeit.timeit(f'challenge({args})', setup=setup, number=1)


def main():
    challenge = sys.argv[1]
    args = sys.argv[2:]
    if challenge == '1A':
        print('Starting challenge 1A')
        print(f'Time elapsed: {time(challenge, args)} seconds')
        print(f'Result: {challenge_1A.challenge(args)}')


if __name__ == "__main__":
    main()

