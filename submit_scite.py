import pandas as pd
import os

def main():
    lines = None
    with open("./sims_ls_oct9") as file:
        lines = [line.rstrip() for line in file]

    for line in lines:
        sim = line.split("-")
        # simNo_10 s_7 m_20 h_1 minCP_0.10 ISAV_0 n_20 fp_0.001 fn_0.1 na_0.25 d_0 l_1000000
        s = sim[1][2:]
        muts = sim[2][2:]
        cells = sim[6][2:]
        alpha = sim[7][3:]
        beta = sim[8][3:]
        na = sim[9][3:]

        filename = "./transposed_matrices/" + line + ".SC.after_noise.transposed.tsv"
        num_samples = 100000

        scite_args = ""
        scite_args += "-i " + filename + " "
        scite_args += "-n " + muts + " -m " + cells + " "
        scite_args += "-fd " + alpha + " -ad " + beta + " "
        scite_args += "-r 1 -l " + str(num_samples) + " "
        scite_args += "-transpose -newicks " + "./scite_newicks/" + line + "." + str(num_samples) + ".newicks -seed 0"

        cmd = "sbatch"
        cmd += ' --job-name="' + "scite." + line + '"'
        cmd += ' --output="' + "scite." + line + '.%j.out"'
        cmd += ' --error="' + "scite." + line + '.%j.err"'
        cmd += ' --export=ARGS="' + scite_args + '"'
        cmd += ' run_scite.sbatch'
        os.system(cmd)

if __name__ == "__main__":
    main()
