# vcf = open("human1.tsv")
# names = open("gene_names.tsv")
with_names = open("with_names.tsv", "w")

name_list = []
for name_line in open("gene_names.tsv"):
    col = name_line.split("\t")
    chr = "chr{}".format(col[0])
    start = int(col[1])
    stop = int(col[2])
    name = col[4].rstrip()
    strand = col[3]
    name_list.append([chr, start, stop, name, strand])

thing = ""
line = 0
for vcf_line in open("human1.tsv"):
    line += 1
    print("Line {}".format(line))
    thing = ""
    vcf = vcf_line.split("\t")
    for name in name_list:
        if vcf[0] == name[0] and name[1] <= int(vcf[1]) <= name[2]:
            thing = "\t".join([name[3],"",vcf[0],vcf[1],vcf[2],vcf[3],vcf[4],vcf[5],vcf[6],vcf[7]])
            break
        else:
            pass
    if thing == "":
        thing = "\t".join(["","",vcf[0],vcf[1],vcf[2],vcf[3],vcf[4],vcf[5],vcf[6],vcf[7]])
    else: pass
    with_names.write(thing)
