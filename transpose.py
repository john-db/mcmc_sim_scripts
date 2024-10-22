import pandas as pd
import argparse


def main(args):
    path = args.input
    df = pd.read_csv(path, sep="\t", index_col=[0]).sort_values(by=["cell_id_x_mut_id"])
    df = df.transpose()
    df.to_csv(args.output, sep="\t", index=False, header=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='run.py')

    parser.add_argument("-i", "--input", type=str,                                                        
                        help="path input", required=True)
    parser.add_argument("-o", "--output", type=str,                                                        
                        help="path output", required=True)
    
    
    main(parser.parse_args())
