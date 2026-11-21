---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-026-61-the-41-knot
section_title: "The 41 knot"
section_number: 6.1
pages: 22-25
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
2 ideal tetrahedra and trace ﬁeld F41 = Q(α) = Q(√−3) where α = e2πi/6 is a root of
x2 −x + 1 = 0 .
F41 is of type [0, 1] with discriminant −3.
The default SnapPy triangulation of 41 generates several Neumann-Zagier data. Most are
Z-nondegenerate; for example
(57)
γ :
A =

−2
1
−1
1

, B =

−1
2
−1
1

, ν = (0, 0) , z = (α, α) , f = (0, 1) , f ′′ = (1, 0)
is Z-nondegenerate. The 1-loop invariant at k = 1 and its norm is given by
(58)
knot
τ −2
1
N(τ −2
1 )
41
2α −1
3
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY
23
The norm of the 1-loop of 41 at level k is given in (59).
(59)
k
N(τk/τ1)
for 41
1
1
2
3
4
112
5
34 · 292
7
397332
8
34 · 3832
10
192892
11
310 · 4632 · 1282372
13
133392 · 139632 · 1300272
14
36 · 4192 · 44512
16
972 · 4181407192
17
316 · 1702392 · 3776155493572
19
5712 · 28512 · 275133292 · 837029940592
20
38 · 592 · 9759119392
22
1312 · 147832 · 396672 · 929272
In the above table, we avoided the (degenerate) case when k is divisible by 3, since in
those cases the trace ﬁeld contains the third roots of unity. Notice that the above norms are
squares of integers. This exceptional integrality may be a consequence of the fact that 41 is
amphicheiral.
Next, we give some sample computations of the factorization (3). In this and the next
sections, more data has been computed (even for non-prime levels k), but only a sample will
be presented here. Throughout this section, ℘n will denote a prime in OFk of norm n, a
prime power.
For k = 2 we have
ε2 = α
β2 = ℘3
℘3 = 2α −1
For k = 4 and ζ = ζ4 we have
ε4 = (−2α + 1)ζ −2
β4 = ℘112
℘112 = (−4α + 2)ζ + 1
For k = 5 and ζ = ζ5 we have
ε5 = (4α −5)ζ3 + (8α −5)ζ2 + 7αζ + 2α + 3
β5 = ℘33 · ℘292
℘33 = 2α −1
℘292 = −2ζ3 + (−α −1)ζ2 −αζ + α −2
24
TUDOR DIMOFTE AND STAVROS GAROUFALIDIS
For k = 7 and ζ = ζ7 we have
ε7 = (60α + 115)ζ5 + (239α + 90)ζ4 + (390α −61)ζ3 + (415α −240)ζ2+
(300α −300)ζ + 114α −186
β7 = ℘39733,1 · ℘39733,2
℘39733,1 = αζ5 + (α −2)ζ4 + (2α −1)ζ3 + (α −2)ζ2 + (2α −1)ζ + 2α −2
℘39733,2 = αζ5 −ζ4 + αζ3 −ζ2 + (2α −1)ζ + 2α −2
For k = 8 and ζ = ζ8 we have
ε8 = (−12α + 36)ζ3 + (17α + 17)ζ2 + (36α −12)ζ + 34α −34
β8 = ℘32,1 · ℘32,2 · ℘3832
℘32,1 = ζ3 −ζ2 −α + 1
℘32,2 = −ζ3 + αζ + 1
℘3832 = (−2α + 2)ζ3 + (3α −1)ζ2 + (α + 1)ζ −α + 3
For k = 10 and ζ = ζ10 we have
ε10 = (−3α + 7)ζ3 + (6α −4)ζ2 + (α + 1)ζ + 9α −10
β10 = ℘192892
℘192892 = (2α −5)ζ3 + (3α + 3)ζ2 + (−α + 6)ζ + 9α + 2
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY
25
For k = 11 and ζ = ζ11 we have
ε11 = (−353875255116707α + 117872583555117)ζ9+
(−688446384174845α + 401155759804328)ζ8+
(−897492189704312α + 759910737126284)ζ7+
(−914641448990872α + 1080237360407592)ζ6+
(−734446808203694α + 1260432001194770)ζ5+
(−414120184922386α + 1243282741908210)ζ4+
(−55365207600430α + 1034236936378743)ζ3+
(227917968648781α + 699665807320605)ζ2+
(345790552203898α + 345790552203898)ζ+
260826355539896α + 84964196664002
β11 = ℘35,1 · ℘35,2 · ℘463,1 · ℘463,2 · ℘1282372
℘35,1 = (α −1)ζ8 + (α −1)ζ7 + (α −1)ζ6 + (α −1)ζ5 −ζ4 + (α −1)ζ2 + (α −1)ζ −1
℘35,2 = −ζ8 −αζ5 −ζ4 + (α −1)ζ3 −ζ + α −1
℘463,1 = (α −1)ζ9 + αζ8 + ζ7 −ζ6 + (α −1)ζ5 + αζ4 + (α −1)ζ2 + αζ
℘463,2 = αζ8 + ζ7 + αζ5 + ζ4 + (−α + 1)ζ3 + (α −1)ζ2 + αζ + 1
℘1282372 = 2αζ9 + 2αζ8 + ζ6 + (−2α + 1)ζ5 + (−α −1)ζ + α −1
Some 2 and 3-loop invariants are shown next.
k
S2,k
for 41
1
(−10 + 11α)/108
2
(−25 + 41α)/216
3
(−20 + 37α)/108
4
(−977 + 1855α)/4752 + (5ζ)/44
5
(−14482 + 37559α)/78300 + (11ζ)/87 −(2(−133 + 11α)ζ2)/2175 + ((31 −22α)ζ3)/2175
k
S3,k
for 41
1
−1/54
2
−19/216
3
−401/1944
4
−17783/52272 + 347(−1 + 2α)ζ/23232
5
(−1569081 + 48037α)/2838375 + 48037(−1 + 2α)ζ/2838375+
(−64041 + 64472α)ζ2/1892250 + (−94781 −1268α)ζ3/5676750
