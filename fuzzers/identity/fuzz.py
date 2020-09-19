import argparse
import gramfuzz
import progressbar
import os

def main():
    num_files = 50

    parser = argparse.ArgumentParser(description='YANG model grammar fuzzer')
    parser.add_argument('--num_files', '-N', help="number of models to generate", type=int)
    args = parser.parse_args()

    path = "./corpus/"

    if not os.path.isdir(path):
        os.makedirs(path)

    fuzzer = gramfuzz.GramFuzzer()
    
    fuzzer.load_grammar("identity-grammar.py")
    for i in progressbar.progressbar(range(num_files)):
        configs = fuzzer.gen(cat="identity", num=1)
        f = open(f"./{path}/{str(i)}.yang", "wb")
        f.write(configs[0])
        f.close()

if __name__ == '__main__':
    main()
