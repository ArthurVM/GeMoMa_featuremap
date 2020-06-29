import os, sys, re

frag_gff="/ibers/ernie/scratch/arm21/BODGe/gemoma_liftover_WD/Ae_STR_final_annotation.gff"

out_gff=open("./Ae_STR_transferred.gff", "w")

print("#Generated using GeMoMa liftover tool written by AM", file=out_gff)

with open(frag_gff, "r") as gff:
        for line in gff.readlines():
                if line.startswith("#") is False:
                        tmp_line = re.split("[\n|\t]", line)
                        old_id = tmp_line[0]
                        tool = tmp_line[1]
                        f_type = tmp_line[2]
                        start = int(tmp_line[3])
                        end = int(tmp_line[4])
                        misc_chunk = tmp_line[5:-1]

                        tmp_id = re.split("[-|:]", old_id)
                        scaff = tmp_id[-3]
                        s_S = int(tmp_id[-2])

                        adj_s = s_S+start
                        adj_e = s_S+end

                        newline="{scaff}\t{tool}/AM_transfer\t{f_type}\t{s}\t{e}\t{misc};old_col0={old_id}".format(scaff=scaff, tool=tool, f_type=f_type, s=adj_s, e=adj_e, misc="\t".join(misc_chunk), old_id=old_id)

                        print(newline, file=out_gff)

out_gff.close()
