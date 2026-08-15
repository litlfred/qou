---
doc_id: arxiv-2509.02354v2
doc_title: "THE HOLONOMY BRAIDING FORUξ(sl2) IN TERMS OF GEOMETRIC QUANTUM DILOGARITHMS"
section_id: sec-009-5-r-matrix-computations
section_title: "R-matrix computations"
section_number: 5
pages: 23-23
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
doc_brief: "THE HOLONOMY BRAIDING FORUξ(sl2) IN TERMS OF GEOMETRIC QUANTUM DILOGARITHMS — We derive an explicit formula for the holonomyR-matrix of quantumsl2 at a root of unity."
---
This section contains computations with theR-matrices. We refer frequently to the
identities concerning shiftedq-factorials and quantum dilogarithms collected in Appendix A.
Lemma 5.1.The R-matrix coefficients(4.16) associated to a positive, log-colored crossing
can be written as
(5.1)
bRn′
1n′
2
n1n2 = ωΘ/2(ω−Nζ 0
t− 1)
N
φ(ζ0
r +n′
2−n1)φ(ζ0
l +n2−n′
1)
φ(ζ0
b +n′
2−n′
1)φ(ζ0
t +n2−n1− 1)
×ωζ0
t +n2−n1ωn1(α1−µ1)+n2(α2+µ2)−n′
1(α1′−µ1)−n′
2(α2′+µ2)
Similarly for a negative crossing the matrix coefficients(4.17) are given by
(5.2)
bR
n′
1n′
2
n1n2 = ω−Θ/2(ω−Nζ 0
t− 1)
N
φ(−ζ0
r +n′
2−n1)φ(−ζ0
l +n2−n′
1)
φ(−ζ0
b +n′
2−n′
1)φ(−ζ0
t +n2−n1− 1)
×ωζ0
t +n1−n2ωn1(α1+µ1)+n2(α2−µ2)−n′
1(α1′+µ1)−n′
2(α2′−µ2)
×ω−(ζ0
t−ζ0
l +n1−n′
1)(ζ0
t−ζ0
r +n2−n′
2)
where in both cases
Θ :=ζ0
tζ1
t +ζ0
bζ1
b−ζ0
rζ1
r−ζ0
lζ1
l.
Proof. The positive case (5.1) follows form the definition (A.9) of Λ(ζ0,ζ 1|n) and some
elementary algebra. For the negative case(5.2) we must also use the relationζ0
r +ζ0
l =ζ0
t +ζ0
b
and the inversion relation [8, equation (16)], which in our conventions is
(5.3) φ(ζ)φ(−ζ− 1) = (1−ω−Nζ ) exp
 
πi(N + 1/N)
12 − πi
N

ζ− N− 1
2
2!
.
□
