---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-032-61-gopakumar-vafa-invariants
section_title: "Gopakumar-Vafa invariants"
section_number: 6.1
pages: 29-30
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
the sake of notational simplicity we will assume that the group H2(X, Z) is torsion-free. The
Gromov-Witten potential of X is a formal series
F (x, λ) =
∑
g≥0
∑
β∈H2(X,Z)
GW(g, β)· xβ· λ2g−2, (34)
where GW(g, β)∈ Q is the genus g Gromov-Witten invariant for stable maps of class β∈ H2(X, Z).
Note that by deﬁnition these invariants are nonzero only for eﬀect ive curve classes β≥ 0. The
symbols xβ are formal variables living in a suitable completion of the eﬀective cone in the group
ring of H2(X, Z), and λ is a formal parameter corresponding to the string coupling.
We can split the series ( 34) into contributions from constant and non-constant maps
F (x, λ) = F0(x, λ) + F ′(x, λ).
The contribution from the constant maps [ 13, Theorem 4] is
F0(x, λ) = a0(x)λ−2 + a1(x) + χ(X)·
∑
g≥2
(−1)g−1· B2g· B2g−2
4g· (2g− 2)· (2g− 2)!λ2g−2, (35)
where the expressions a0(x) and a1(x) can be found for example in [ 27]. Although the precise
form of these expressions will not be relevant here it is worth noting that, unlike the higher genus
terms, they involve the variables xβ. Turning now to the contributions from non-constant maps,
30 TOM BRIDGELAND
the Gopakumar-Vafa conjecture [ 18, 27] claims that there exist integers GV( g, β)∈ Z, such that
F ′(x, λ) =
∑
β>0
∑
g≥0
GV(g, β)
∑
k≥1
1
k
(
2 sin
(kλ
2
)) 2g−2
xkβ.
We will be particularly interested in the expression
∑
β>0
GV(0, β)
∑
k≥1
1
k
(
2 sin
(kλ
2
)) −2
xkβ, (36)
which gives the contribution from genus 0 Gopakumar-Vafa invariants. Note that using the Laurent
expansion
(2 sin(s/2))−2 = 1
s2− 1
12 +
∑
g≥2
(−1)g−1B2g
2g(2g− 2)!· s2g−2,
we can write the coeﬃcient of λ2g−2 in ( 36) as
∑
β>0
GV(0, β)· (−1)g−1B2g
2g(2g− 2)!· Li3−2g(xβ), (37)
at least for g≥ 2.
