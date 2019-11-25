import sys
import timeit
import challenges


def time(challenge, args):
    setup = f'from challenges import challenge_{challenge}'
    return timeit.timeit(f'challenge_{challenge}.challenge({args})', setup=setup, number=1)


def main():
    challenge = sys.argv[1]
    args = sys.argv[2:]

    if challenge == '1A':
        print(f'Starting challenge {challenge}')
        print(f'Time elapsed: {time(challenge, args)} seconds')
        print(f'Result: {challenges.challenge_1A.challenge(args)}')

    if challenge == '1B':
        print(f'Starting challenge {challenge}')
        print(f'Time elapsed: {time(challenge, args)} seconds')
        print(f'Result: {challenges.challenge_1B.challenge(args)}')


if __name__ == "__main__":
    main()

