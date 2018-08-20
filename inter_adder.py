# vcf = open("human1.tsv")
# names = open("gene_names.tsv")
with_inter = open("with_inter.tsv", "w")

name_list = []
for name_line in open("inter_list.tsv"):
    col = name_line.split("\t")
    chr = "chr{}".format(col[4].rstrip())
    start = int(col[0])
    stop = int(col[1])
    name = col[2]
    strand = col[3]
    name_list.append([chr, start, stop, name, strand])
thing = ""
line = 0
for vcf_line in open("with_names.tsv"):
    line += 1
    print("Line {}".format(line))
    thing = ""
    vcf = vcf_line.split("\t")
    for name in name_list:
        if vcf[2] == name[0] and name[1] <= int(vcf[3]) <= name[2]:
            thing = "\t".join([vcf[0],name[3],vcf[2],vcf[3],vcf[4],vcf[5],vcf[6],vcf[7],vcf[8],vcf[9]])
            break
        else:
            pass

    if thing == "":
        thing = "\t".join([vcf[0],"",vcf[2],vcf[3],vcf[4],vcf[5],vcf[6],vcf[7],vcf[8],vcf[9]])
    else: pass
    with_inter.write(thing)
