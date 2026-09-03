---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-037-dimensional-counting-analysis
section_title: "Dimensional counting analysis"
section_number: null
pages: 64-65
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
In this section we provide an illustration of the dimensiona l counting analysis [Gegelia et al., 1994] in
terms of a speciﬁc example. To that end let us consider the one -loop integral of Eq. (214),
H(p2,m 2,M 2;n) = −i
∫ dnk
(2π)n
1
k2 − 2p ·k +p2 −m2 +i0+
1
k2 −M 2 +i0+. (236)
64
One would like to know how the integral behaves for small valu es of M and/or p2 −m2 as a function
of n. If we consider, for ﬁxed p2 ⁄=m2, the limit M → 0, the integral H can be represented as
H(p2,m 2,M 2;n) =
∑
i
M βiFi(p2,m 2,M 2;n), (237)
where the functionsFi are analytic inM 2 and are obtained as follows. First, one re-writes the integr ation
variable as k =M αi ˜k, where αi is an arbitrary non-negative real number. Next, one isolate s the overall
factor ofM βi so that the remaining integrand can be expanded in positive p owers ofM 2 and interchanges
the integration and summation. The resulting series repres ents the expansion of Fi(p2,m 2,M 2;n)
in powers of M 2. The sum of all possible re-scalings with subsequent expans ions with non-trivial
coeﬃcients then reproduces the expansion of the result of th e original integral.
To be speciﬁc, let us apply this program to H:
H(p2,m 2,M 2;n) = −i
∫ M nαidn˜k
(2π)n
1
˜k2M 2αi − 2p · ˜kM αi +p2 −m2 +i0+
1
˜k2M 2αi −M 2 +i0+. (238)
From Eq. (238) we see that the ﬁrst fraction does not contribu te to the overall factor M βi for any αi.
It will be expanded in (positive) powers of ( ˜k2M 2αi − 2p · ˜kM αi) except for αi = 0. For 0 <α i < 1, we
re-write the second fraction as
1
M 2αi
1
(˜k2 −M 2−2αi +i0+) = 1
M 2αi
1
˜k2 +i0+
(
1 + M 2−2αi
˜k2 +i0+ + · · ·
)
. (239)
On the other hand, if 1 <α i we re-write the second fraction as
1
M 2
1
(˜k2M 2αi−2 − 1 +i0+) = − 1
M 2
(
1 + ˜k2M 2αi−2 + · · ·
)
. (240)
In both cases one obtains integrals of the type
∫
dn˜k ˜kµ1 · · · ˜kµm as the coeﬃcients of the expansion.
However, such integrals vanish in dimensional regularizat ion. Therefore, the only non-trivial terms in
the sum of Eq. (237) correspond to either αi = 0 or αi = 1. Thus we obtain
H(p2,m 2,M 2;n) = H (0)(p2,m 2,M 2;n) +H (1)(p2,m 2,M 2;n), (241)
where
H (0)(p2,m 2,M 2;n) = −i
∞∑
j=0
(
M 2
)j∫ dnk
(2π)n
1
k2 − 2p ·k +p2 −m2 +i0+
1
(k2 +i0+)j+1, (242)
and
H (1)(p2,m 2,M 2;n) = −i M n−2
p2 −m2 +i0+
∞∑
j=0
(−1)jM j
(p2 −m2 +i0+)j
∫ dn˜k
(2π)n
(
˜k2M − 2p · ˜k
)j
˜k2 − 1 +i0+ . (243)
A comparison with the direct calculation of H shows that the dimensional counting method indeed leads
to the correct expressions [Gegelia et al., 1994]. While the loop integrals of Eq. (243) have a simple
analytic structure in p2 −m2, the same technique can be repeated for the loop integrals of Eq. (242)
whenp2 −m2 → 0, now using the change of variable k = (p2 −m2)γi ˜k with arbitrary non-negative real
numbersγi.
