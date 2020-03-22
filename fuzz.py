import argparse
import gramfuzz
import progressbar


num_files = 1000

def main():
    global num_files

    parser = argparse.ArgumentParser(description='YANG model grammar fuzzer')
    parser.add_argument('--num_files', '-N', help="number of models to generate", type=int)
    args = parser.parse_args()

    if args.num_files:
        num_files = args.num_files

    fuzzer = gramfuzz.GramFuzzer()
    fuzzer.load_grammar("yang_grammar.py")
    for i in progressbar.progressbar(range(num_files)):
        configs = fuzzer.gen(cat="yang", num=1)
        f = open("./configs/" + str(i) + ".yang", "w")
        f.write(configs[0])
        f.close()

if __name__ == '__main__':
    main()
