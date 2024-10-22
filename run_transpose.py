import os

def main():
    in_folder = "/data/CDSLSahinalp/bridgersjd/salems_sims/RECOMB-oct_9_2024/simulated_input_data/"

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

        input = in_folder + line + ".SC.after_noise"
        output = "./transposed_matrices/" + line + ".SC.after_noise.transposed.tsv"

        cmd = "python ./transpose -i " + input + " -o " + output
        os.system(cmd)
        # print(cmd)

        

if __name__ == "__main__":
    main()