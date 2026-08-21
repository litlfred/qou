---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-093-62-a-formula-for-the-generic-rank-137
section_title: "A formula for the generic rank 137"
section_number: 6.2
pages: 145-147
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
6.2. A formula for the generic rank
The main goal of the present chapter is to obtain a recursive formula
for the generic rankrα of the perverse sheavespδα, by which we more
precisely mean the rank
rα = dimC
(H−g(pδα)η
)
of the lowest degree cohomology sheaf at the generic pointη∈ X. Note
that rα = 0 if and only if the perverse sheafpδα is supported on a proper
closed subset ofX (indeed any simple perverse sheaf arises via intermediate
extension from a local system on an open dense subset of its support).
THEOREM 6.1. For partitionsα = (d1, . . . ,dn) of degree d= deg(α)
the generic rank rα is given by the recursion
rα = ∑
c1+···+cn=g
0≤ci≤di
[ g!
c1!···cn!−1] n
∏
k=1
(2(g−1−ck)
dk−ck
) − ∑
β>α
deg(β)=d
Kβ α·rβ.
where the Kβ α are the Kostka numbers deﬁned combinatorially below.
Here we use the following conventions: For any integersa,m∈ Z the
binomial coefﬁcient(m
a
) is deﬁned as the coefﬁcient ofta in the expansion
of (1 +t)m as a power series, hence it vanishes fora < 0 and is given for
exponentsm < 0 by the formula(m
a
) = (−1)a·(a−m−1
a
). For partitions α
and β the notationβ > α refers to the lexicographic ordering. Finally, we
recall that the Kostka numbersKβ α are non-negative integers which can be
deﬁned combinatorially in the following way.
By a Young diagram of shapeβ = (e1, . . . ,em) we mean a diagram ofm
left-aligned rows such that for eachi the ith row consists ofei cells. If the
cells of the diagram are ﬁlled with the entries 1,2, . . . ,n and each entryj
occurs preciselydj times, the resulting array is called a Young tableau of
contentα = (d1, . . . ,dn). A Young tableau is said to be semistandard if the
entries of the rows are weakly increasing from left to right and those of the
columns are strictly increasing from top to bottom; by deﬁnition the Kostka
numberKβ α is the number of such tableaux of shapeβ and contentα. For
example, we haveK(3,2),(2,2,1) = 2 since
1 1 2
2 3
1 1 3
2 2
are the only semistandard tableaux of shape(3,2) and content(2,2,1). The
above deﬁnition also easily implies that the Kostka numbers satisfyKαα =1
andKβ α = 0 for all partitionsβ < α.
138 Chapter 6 – The generic rank of Brill-Noether sheaves
The Kostka numbers arise in the representation theory of the symmetric
group: Young’s rule [88, th. 2.11.2] says that for partitionsα = (d1, . . . ,dn)
of degreed = deg(α) we have
(⋆) Ind Sd
Sd1×···×Sdn
(1) =
⨁
β≥α
Kβ α· σβ
where the left hand side denotes the representation induced from the trivial
representation1 of the subgroupSd1×···× Sdn≤ Sd. Since Kαα = 1, it
follows that the dimensions of the Specht modules satisfy
(⋆⋆) dim (σα) = d!
d1!···dn! − ∑
β>α
Kβ α·dim(σβ).
This being said, let us take a look at the recursion formula in theorem 6.1 in
some explicit examples.
EXAMPLE 6.2. Let α be a partition of degree d. For d< g the ﬁrst sum
in theorem 6.1 is empty so that rα = 0. More interestingly, in degree d= g
the recursion of the theorem says
rα = g!
d1!···dn!− 1− ∑
β>α
Kβ α·rβ
which together with(⋆⋆) implies
rα =
{
dim(σα) if α⁄= (g),
0 if α = (g).
We remark that this can also be checked directly as follows. Ford < g
the subvarietyWd is a proper closed subset ofX, and by construction it
contains the support ofpδα. Similarly, in degree d = g the Abel-Jacobi
morphismhd :Cd→X is birational, and in this case our claim follows from
the observation that the perverse sheafγα∈ Perv(Cd,C) from section 6.1
has generic rank dim(σα) and contains the constant perverse sheaf if and
only if α = (g) is a singleton partition. However, for partitions of higher
degree the situation becomes increasingly complicated.
EXAMPLE 6.3. For g= 4 theorem 6.1 predicts that r6 = r5,1 = 0 and
more interestingly that
r4,2 = [ 4!
2!·2!−1]·(2
2
)·(2
0
) = 5,
r3,3 = 2· [ 4!
3!·1!−1]·(0
0
)·(4
2
)+ [ 4!
2!·2!−1]·(2
1
)·(2
1
)−r4,2 = 51.
