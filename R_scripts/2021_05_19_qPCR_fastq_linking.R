# find samples without vanB for Ali's spike-in experiment

qPCR = read.csv("../genome_alignments/qPCR results tabulated.csv", header = T)
manifest = read.csv("../genome_alignments/manifest.limited.csv", header = T)

no_vanB = qPCR[is.na(qPCR$VanB) & qPCR$Sample.ID %in% manifest$specimen, ]

no_vanB[no_vanB$Sample.ID %in% "BA0298",]