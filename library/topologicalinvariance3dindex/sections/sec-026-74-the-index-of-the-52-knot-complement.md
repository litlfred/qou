---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-026-74-the-index-of-the-52-knot-complement
section_title: "The index of the 52 knot complement"
section_number: 7.4
pages: 45-47
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
52 knot complement uses 3 ideal tetrahedra. The Epstein-Penner decomposition TEP uses 4
ideal tetrahedra. Both triangulations carry geometric shape structures and thus canonical
strict angle structures. One can show that T and TEP are related by geometric 23 moves
hence they have equal indices. For reasons of e
ciency, we will work with the triangulation
T. Its angle structure matrices are given by:
46 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
A =


1
1
1
0
0
0
1
1
1


B =


0
2
0
1
0
1
1
0
1


C =


1
0
1
1
2
1
0
0
0

.
Eliminating B, and removing the third row (which corresponds to the third edge equation),
we obtain the angle structure equations
A′α + B′γ = πν′
where
A′ =

1
−1
1
−1
0
−1

B′ =

1
−2
1
0
2
0

ν′ =

0
0

.
The index of T is given by
(33)
I52(0)(q) =
X
(k1,k2)∈Z2
I∆(−k1, k1 −k2)2I∆(2k1 −2k2, −k1) ∈Z[[q]] .
Equation (12) implies that the degree δ(k1, k2) of the summand is a piecewise quadratic
polynomial with fan FT given by six rays, ρ1, . . . , ρ6, corresponding to the columns of the
matrix

2
1
0
−1
−1
0
1
1
1
0
−1
−1

.
ρ5
ρ4
ρ3
ρ2
ρ1
ρ6
Figure 21. The fan of the summand of I52(0).
Let Cij denote the two-dimensional cone with rays ρi and ρj. Then we have:
δ(k1, k2) =



















k1
2 + k2
1
2
if (k1, k2) ∈C12
−k1
2 −k2
1
2 + k2 + k2
2
if (k1, k2) ∈C23
−k1 + k2
1 + k2 −2k1k2 + k2
2
if (k1, k2) ∈C34
−k1 + k2
1
if (k1, k2) ∈C45
k2
1 −k2 −2k1k2 + 2k2
2
if (k1, k2) ∈C56
k1 + 2k2
1 −k2 −4k1k2 + 2k2
2
if (k1, k2) ∈C61 .
A plot of δ(k1, k2) for k1, k2 ∈[−1, 1] is given in Figure 22.
If δ(k1, k2) ≤N, then to bound k1 from above and below we use the restriction to the rays
ρ1 and ρ5 respectively. Likewise, to bound k2 from above and below we use the restriction
to the rays ρ2 and ρ5 respectively. The equations
δ(k1, k1) =
(
(−1 + k1)k1
if k1 ≤0
1
2k1(1 + k1)
if k1 ≥0
δ(2k2, k2) =
(
2k2(−1 + 2k2)k2
if k2 ≤0
k2(1 + 2k2)
if k2 ≥0
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
47
Figure 22. The plot of the degree of the summand of 52.
and the inequality δ(k1, k2) ≤N give the bounds
(34a)
1
2(1 −
√
1 + 4N) ≤k1 ≤1
2(1 +
√
1 + 8N)
(34b)
1
2(1 −
√
1 + 4N) ≤k2 ≤1
2(1 +
√
1 + 8N) .
With these bounds, we can compute the coe
cients of I52(0)(q). The 
rst 100 of them are
given by:
1 −4q −q2 + 16q3 + 26q4 + 23q5 −34q6 −122q7 −239q8 −312q9 −221q10 + 102q11 + 778q12 + 1757q13 + 2930q14 +
3825q15 + 4003q16 + 2560q17 −1183q18 −8033q19 −18087q20 −30864q21 −44625q22 −56225q23 −60913q24 −52342q25 −
23373q26 + 33675q27 + 124356q28 + 251997q29 + 412837q30 + 596153q31 + 778487q32 + 925195q33 + 984860q34 + 895092q35 +
579789q36 −39418q37 −1039055q38 −2474979q39 −4370844q40 −6691737q41 −9326308q42 −12059462q43 −14553043q44 −
16329323q45−16762776q46−15091256q47−10436174q48−1863234q49+11551967q50+30594044q51+55785006q52+87178516q53+
124185931q54 +165312079q55 +207965719q56 +248191454q57 +280543349q58 +297911617q59 +291580973q60 +251299184q61 +
165675668q62+22662435q63−189540512q64−481437576q65−860708203q66−1330509280q67−1887333621q68−2518748267q69−
3200856694q70−3895826567q71−4549488766q72−5089337005q73−5423179738q74−5438686309q75−5004368747q76−3972096155q77−
2181963773q78 + 530655834q79 + 4324768774q80 + 9340768927q81 + 15683465230q82 + 23402429365q83 + 32468254286q84 +
42746925974q85+53970937518q86+65710530396q87+77343886238q88+88031000047q89+96690414035q90+101984965333q91+
102316085357q92+95834146866q93+80464612248q94+53958404128q95+13966121550q96−41855327561q97−115704867879q98−
209460627592q99 −324467541887q100
The 
rst 300 coe
cients are available from [Gara].
