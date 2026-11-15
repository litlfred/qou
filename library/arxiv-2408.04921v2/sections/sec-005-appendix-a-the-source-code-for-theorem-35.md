---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP"
section_id: sec-005-appendix-a-the-source-code-for-theorem-35
section_title: "Appendix A. The source code for Theorem 3.5"
section_number: null
pages: 22-22
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
toc_source: outline
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP — The paper studies how to compute irreducible characters of the generalized symmetric group Ck ≀Sn by iterative algorithms."
---
# Take k=3, n=5
P=PartitionTuples(3,5)
import random
lam=random.choice(P)
rho=random.choice(P)
print(lam,rho)
# Set environment
m=max(max(rho))
j=rho.index(max(rho))
r=Zmod(3)
w=SR.var(’w’)
import numpy
def ht(nums):
return numpy.count_nonzero(nums)-1
# Filter out lam satisfying conditions
for k in range(3):
if lam[k].size()>=m:
tem=Partitions(lam[k].size()-m,outer=lam[k]).list()
for i in tem:
if SkewPartition([lam[k],i]).is_ribbon():
coff =
(-1)^ht(SkewPartition([lam[k],i]).row_lengths())*w^r(-j*k)
l=list(lam)
l[k]=i
print(coff,"new lam:",PartitionTuple(l))
