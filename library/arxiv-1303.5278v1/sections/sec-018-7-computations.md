---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-018-7-computations
section_title: "Computations"
section_number: 7
pages: 43-51
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
7.1. How to compute the coeﬃcients of aq-series. In this section we will explain a
general method to compute the coeﬃcients of aq-series which is given by a multi-dimensional
sum of some basicq-series. The idea is simple, but the eﬀective aspects of it are tricky and
were explained to the ﬁrst author by D. Zagier. The method is applied in forthcoming work
[GV] which computes the coeﬃcients of the stabilization of the coloured Jones polynomial
of an alternating knot [GL].
Fix a 1-eﬃcient ideal triangulationT withn tetrahedra of a 1-cusped hyperbolic manifold
M and an oriented multi-curveϖ on ∂M. The index IT(ϖ)(q)∈ Z((q1/2)) is given by a
convergent (n−1)-dimensional sum over the integers of a summand that depends on the angle
structure equation matrices ofT; see Equation (17). The summand ofIT(ϖ) is a product of
tetrahedron indices (one per tetrahedron ofT) of linear forms ink = (k1,...,k n−1)∈ Zn−1
and the turning number vectors(aϖ|bϖ) of ϖ.
The building block of the summand is the tetrahedron indexI∆, whose degree (i.e., mini-
mum degree with respect toq) is a piecewise quadratic function onR2; see Section 4.2. By
a piecewise quadratic functionon Rm, we mean that there exists a partitionF of Rm into
a ﬁnite number of chambers whose boundaries are rational polyhedral cones such that the
restriction of the function to each chamber is given by a quadratic polynomial. It follows
that for ﬁxedϖ, the degreeδ(ϖ,k) of the summand in (17) is a piecewise quadratic function
deﬁned on a partitionFT of Rn−1. In a later publication, we will explain how to computeFT
directly from T. A priori, FT need not be a fan inRn−1 as the cones in the partition may
not be convex.
Since T is 1-eﬃcient, it follows that its indexIT(ϖ)(q) is a convergent series. In other
words, the degree of the summand is a proper function onZn−1. Thus, for ﬁxedϖ and every
half-integer N, the set{k∈ Zn−1 : δ(ϖ,k)≤ N} is ﬁnite. To compute the index ofT,
we need to compute bounds on this ﬁnite set. Sinceδ is convex and piecewise quadratic, it
follows that to boundδ(ϖ,k), it suﬃces to bound the restriction ofδ(ϖ,k) to an arbitrary
ray ρ ={k′ρ0 : k′∈ N} of FT. Now δ(ϖ,k′ρ0) is a quadratic function ofk′∈ N, and we
obtain sharp bounds forki typically of the formki =O(
√
N) and exceptionally of the form
ki =O(N). The latter happens whenδ has linear growth on some ray ofFT. These directions
of linear growth (also observed in [GL] in the context of stabilization of the coloured Jones
44 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
function) are computationally costly. For an example, see the case of the knot61 discussed
below.
The bounds forki discussed above are rigorous and sharp, and work well forn = 2 and
n = 3 tetrahedra. However, they quickly become ineﬃcient whenn increases (e.g. n = 9).
The better way to proceed for largern, as was explained to us by D. Zagier and is applied
successfully in [GV], is to useiterated summation. In the examples shown below forn = 2
andn = 3 iterated summation is not needed. For simplicity, we focus on 1-cusped manifolds
and their index for [ϖ] = 0 ∈ H1(∂M ; Z). The data presented below are available from
[Gara].
Remark 7.1. If two 1-cusped hyperbolic 3-manifoldsM and M′ have 1-eﬃcient ideal tri-
angulations T and T′ with equal angle structure matrices, thenIT(0)(q) = IT′(0)(q). For
example, M and−M have such triangulations, where−M denotes the orientation reversed
cusped hyperbolic manifold. Also, Mφ and M−φ have such triangulations for a pseudo-
Anosov homeomorphismφ of a once punctured torus, whereMφ denotes the mapping torus
of φ.
7.2. The index of the41 knot complement. The default SnapPy triangulation T of the
41 knot complement uses 2 regular ideal tetrahedra and coincides with the Epstein-Penner
decomposition, thus XEP
41 ={T}. SnapPy gives the angle structure matrices ofT:
A =
(
2 2
0 0
)
B =
(
1 1
1 1
)
C =
(
0 0
2 2
)
.
SnapPy also gives an additional two rows which correspond to the meridian and longitude
equations; we will not use these in our examples so we omit them here. We eliminateB to
obtain A and B. We choose our basic edge setB ={e1} and excluded edge setX ={e2}.
We can therefore ignore the rows of our matrices corresponding toe2, and write
A′ =
( 1 1 )
B′ =
(−1 −1 )
ν′ =
( 0 )
.
We obtain the angle structure equations
A′α + B′γ =πν′.
Equation (17) gives that
I41(0)(q) =
∑
k∈Z
I∆(k,k )(q)2∈ Z[[q]].
Equation(12)impliesthatthedegree δ(k)ofthesummandisgivenbythepiecewisequadratic
polynomial
δ(k) = 2δ(k,k ) = 2k2 +|k|.
Its corresponding fan FT in R consists of two rays, corresponding to the columns of the
matrix ( 1 −1 )
.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 45
Here, a column vectorv of a matrix, spans the rayR+v. It follows that for every natural
numberN we have
I41(0)(q) +O(q)N+1 =
⌈1/4(−1+√1+8N)⌉∑
k=⌊1/4(−1−√1+8N)⌋
I∆(k,k )(q)2 +O(q)N+1.
To computeI∆(k,k )(q) +O(q)N+1, we use its deﬁnition (5) and truncate then-summation
as follows
(32) I∆(k,k )(q)+O(q)N+1 =
⌈1/4(−1+√1+8N)⌉∑
n=⌊1/2(−1+2k−
√
1−4k+8k2+8N)⌋
(−1)nq
1
2n(n+1)−(n+ 1
2k)k
(q)n(q)n+k
+O(q)N+1.
Putting everything together, the ﬁrst 100 coeﬃcients ofI41(0)(q) are given by
1− 2q− 3q2 + 2q3 + 8q4 + 18q5 + 18q6 + 14q7− 12q8− 52q9− 106q10− 164q11− 209q12− 212q13− 141q14 + 14q15 +
309q16 + 714q17 + 1249q18 + 1824q19 + 2401q20 + 2794q21 + 2898q22 + 2434q23 + 1256q24− 918q25− 4186q26− 8712q27−
14394q28− 21046q29− 28184q30− 35094q31− 40740q32− 43732q33− 42508q34− 35068q35− 19524q36 + 6288q37 + 43942q38 +
95026q39 + 159698q40 + 237774q41 + 326680q42 + 422880q43 + 519595q44 + 608636q45 + 677761q46 + 713352q47 + 697625q48 +
611956q49+434572q50+144616q51−279773q52−856288q53−1599627q54−2515906q55−3602521q56−4842516q57−6203552q58−
7632646q59−9054429q60−10367858q61−11443874q62−12125534q63−12226286q64−11535062q65−9815935q66−6820480q67−
2289703q68+4024698q69+12355340q70+22887604q71+35751602q72+50979996q73+68497913q74+88071340q75+109297633q76+
131547294q77 +153959928q78 +175385202q79 +194390216q80 +209208210q81 +217767013q82 +217655122q83 +206182023q84 +
180375446q85 + 137083864q86 + 73018494q87− 15089960q88− 130393760q89− 275708923q90− 453351590q91− 664856517q92−
910744842q93−1190185170q94−1500703210q95−1837805659q96−2194650672q97−2561673782q98−2926258326q99−3272416148q100
The ﬁrst 1000 coeﬃcients are available from [Gara].
7.3. The index of the sister of the41 knot complement. The 41 knot complement
and its sister are the census manifoldsm004 and m003 respectively, and are punctured torus
bundles over a circle with monodromy+RL and−RL respectively [CDW]. The Epstein-
Penner decompositions form004 and m003 consist of two regular ideal tetrahedra. The edge
gluing equations of+RL and−RL coincide. Thus,Im003(0) =Im004(0).
7.4. The index of the52 knot complement. The default SnapPy triangulation T of the
52 knot complement uses 3 ideal tetrahedra. The Epstein-Penner decompositionTEP uses 4
ideal tetrahedra. Both triangulations carry geometric shape structures and thus canonical
strict angle structures. One can show thatT and TEP are related by geometric 2–3 moves
hence they have equal indices. For reasons of eﬃciency, we will work with the triangulation
T. Its angle structure matrices are given by:
A =


1 1 1
0 0 0
1 1 1

 B =


0 2 0
1 0 1
1 0 1

 C =


1 0 1
1 2 1
0 0 0

 .
46 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Eliminating B, and removing the third row (which corresponds to the third edge equation),
we obtain the angle structure equations
A′α + B′γ =πν′
where
A′ =
(
1 −1 1
−1 0 −1
)
B′ =
(
1 −2 1
0 2 0
)
ν′ =
(
0
0
)
.
The index ofT is given by
(33) I52(0)(q) =
∑
(k1,k2)∈Z2
I∆(−k1,k 1−k2)2I∆(2k1− 2k2,−k1)∈ Z[[q]].
Equation (12) implies that the degreeδ(k1,k 2) of the summand is a piecewise quadratic
polynomial with fan FT given by six rays,ρ1,...,ρ 6, corresponding to the columns of the
matrix (
2 1 0 −1 −1 0
1 1 1 0 −1 −1
)
.
ρ5
ρ4
ρ3 ρ2
ρ1
ρ6
Figure 21. The fan of the summand ofI52(0).
Let Cij denote the two-dimensional cone with raysρi and ρj. Then we have:
δ(k1,k 2) =



k1
2 + k2
1
2 if (k1,k 2)∈C12
−k1
2 − k2
1
2 +k2 +k2
2 if (k1,k 2)∈C23
−k1 +k2
1 +k2− 2k1k2 +k2
2 if (k1,k 2)∈C34
−k1 +k2
1 if (k1,k 2)∈C45
k2
1−k2− 2k1k2 + 2k2
2 if (k1,k 2)∈C56
k1 + 2k2
1−k2− 4k1k2 + 2k2
2 if (k1,k 2)∈C61.
A plot ofδ(k1,k 2) for k1,k 2∈ [−1, 1] is given in Figure 22.
Ifδ(k1,k 2)≤N, then to boundk1 from above and below we use the restriction to the rays
ρ1 and ρ5 respectively. Likewise, to boundk2 from above and below we use the restriction
to the raysρ2 and ρ5 respectively. The equations
δ(k1,k 1) =
{
(−1 +k1)k1 if k1≤ 0
1
2k1(1 +k1) if k1≥ 0 δ(2k2,k 2) =
{
2k2(−1 + 2k2)k2 if k2≤ 0
k2(1 + 2k2) if k2≥ 0
and the inequalityδ(k1,k 2)≤N give the bounds
(34a) 1
2(1−
√
1 + 4N)≤k1≤ 1
2(1 +
√
1 + 8N)
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 47
Figure 22. The plot of the degree of the summand of52.
(34b) 1
2(1−
√
1 + 4N)≤k2≤ 1
2(1 +
√
1 + 8N).
With these bounds, we can compute the coeﬃcients ofI52(0)(q). The ﬁrst 100 of them are
given by:
1− 4q−q2 + 16q3 + 26q4 + 23q5− 34q6− 122q7− 239q8− 312q9− 221q10 + 102q11 + 778q12 + 1757q13 + 2930q14 +
3825q15 + 4003q16 + 2560q17− 1183q18− 8033q19− 18087q20− 30864q21− 44625q22− 56225q23− 60913q24− 52342q25−
23373q26 + 33675q27 + 124356q28 + 251997q29 + 412837q30 + 596153q31 + 778487q32 + 925195q33 + 984860q34 + 895092q35 +
579789q36− 39418q37− 1039055q38− 2474979q39− 4370844q40− 6691737q41− 9326308q42− 12059462q43− 14553043q44−
16329323q45−16762776q46−15091256q47−10436174q48−1863234q49+11551967q50+30594044q51+55785006q52+87178516q53+
124185931q54 +165312079q55 +207965719q56 +248191454q57 +280543349q58 +297911617q59 +291580973q60 +251299184q61 +
165675668q62+22662435q63−189540512q64−481437576q65−860708203q66−1330509280q67−1887333621q68−2518748267q69−
3200856694q70−3895826567q71−4549488766q72−5089337005q73−5423179738q74−5438686309q75−5004368747q76−3972096155q77−
2181963773q78 + 530655834q79 + 4324768774q80 + 9340768927q81 + 15683465230q82 + 23402429365q83 + 32468254286q84 +
42746925974q85+53970937518q86+65710530396q87+77343886238q88+88031000047q89+96690414035q90+101984965333q91+
102316085357q92+95834146866q93+80464612248q94+53958404128q95+13966121550q96−41855327561q97−115704867879q98−
209460627592q99− 324467541887q100
The ﬁrst 300 coeﬃcients are available from [Gara].
7.5. The index of the(−2, 3, 7) pretzel knot complement.The (−2, 3, 7) pretzel knot
is the 12 crossing knot 12n242 in the census. The default SnapPy triangulation T of the
12n242 complement uses 3 ideal tetrahedra. The Epstein-Penner decompositionTEP uses 3
idealtetrahedra. However, thetwotriangulations T and TEP arecombinatoriallydiﬀerent; for
instance have edge-valencies5, 6, 7 and 5, 5, 8 respectively. Nevertheless, both triangulations
are geometric with canonical strict angle structure and are related by geometric 2–3 moves,
which preserve the index. The angle structure equations ofT are given by:
48 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
A =


1 0 0
0 1 1
1 1 1

 B =


0 1 0
1 1 0
1 0 2

 C =


1 1 2
1 0 0
0 1 0

 .
Apply the following operations on(A|B|C):
• Permute the rows according to(123)↦→ (312).
• Permute the second and third columns ofA and simultaneously, ofB and C.
• If ¯a1, ¯b1, ¯c1 aretheﬁrstcolumnsof A, Band C, thenpermute (¯a1|¯b1|¯c1)↦→ (¯b1|¯c1|¯a1).
After the above permutations, the matrix(A|B|C) of the (−2, 3, 7) pretzel knot becomes
the corresponding matrix of the52 knot. Since the above permutations do not change the
index, it follows thatI(−2,3,7)(0) =I52(0).
Exercise 7.2.Using the matrix(A|B|C) above, it follows that the index ofT is given by
(35)
I(−2,3,7)(0)(q) =
∑
(k1,k2)∈Z2
(−1)k2q
1
2 (k1−2k2)I∆(k1,−k2)I∆(−k1 +k2,k 1)I∆(−2k1 + 2k2,k 1− 2k2).
On the other hand, the index of52 is given by Equation (33). Using the identities of the
tetrahedron index from Section 4, show that
∑
(k1,k2)∈Z2
I∆(−k1,k 1−k2)2I∆(2k1− 2k2,−k1) =
∑
(k1,k2)∈Z2
(−1)k2q
1
2 (k1−2k2)I∆(k1,−k2)I∆(−k1 +k2,k 1)I∆(−2k1 + 2k2,k 1− 2k2).
7.6. The index of the61 knot complement. In this section we discuss the indexI61(0)
as an example of the phenomenon of linear growth. The defaultSnapPy triangulation T of
the 61 knot complement has 4 ideal tetrahedra, and the Epstein-Penner decomposition uses
6 ideal tetrahedra. The two triangulations are related by geometric 2–3 moves and so have
equal indices. The angle structure equations ofT are given by:
A =


1 1 0 0
0 0 0 1
0 1 1 0
1 0 1 1

 B =


0 2 0 1
1 0 1 0
1 0 0 0
0 0 1 1

 C =


1 0 1 1
1 2 1 0
0 0 0 1
0 0 0 0

 .
Eliminating B, and removing the fourth row (which corresponds to the fourth edge equa-
tion), we obtain the angle structure equations
A′α + B′γ =πν′
where
A′ =


1 −1 0 −1
−1 0 −1 1
−1 1 1 0

 B′ =


1 −2 1 0
0 2 0 0
−1 0 0 1

 ν′ =


−1
0
1

 .
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 49
The index ofT is given by
I61(0)(q) =
∑
(k1,k2,k3)∈Z3
q
1
2 (−k1+k3)I∆(−k1,−k2 +k3)I∆(2k1− 2k2,−k1 +k3)
I∆(−k3,−k1 +k2)I∆(−k1 +k3,k 1−k2−k3)∈ Z[[q]].
FT in R3 has 18 rays, corresponding to the columns of the matrix


−1 −1 −1 −1 −1 −1 0 0 0 0 0 0 1 1 1 1 2 3
−2 −2 −1 0 0 1 −1 −1 −1 0 1 1 0 0 1 1 1 2
−3 −1 0 −1 0 0 −2 −1 0 1 −1 0 −1 1 0 1 1 1

 .
Ifδ(k1,k 2,k 3) denotes the degree of the summand andN∈ N, thenδ(k1,k 2,k 3)≤N implies
that (k1,k 2,k 3) satisfy the bounds
1
2(1−
√
1 + 4N)≤k1≤ 1
2(−1 +
√
1 + 12N)
2
3(1−
√
1 + 3N)≤k2≤ 1
2(−1 +
√
1 + 8N)
3
7(1−
√
1 + 7N)≤k3≤N.
Observe that the upper bound fork3 is linear inN. For instance, whenN = 3, the following
17 terms (each a product of 4 truncated tetrahedron indices, as in Equation (32) forN = 3)
contribute toI61(0) +O(q)4 = 1− 4q +q2 + 18q3 +O(q)4:
I∆(−2, 0)2I∆(0,−2)I∆(0, 0)−q− 1
2I∆(−1,−1)I∆(−1, 0)I∆(0,−1)I∆(0, 0) +I∆(−1, 0)2I∆(0,−1)I∆(0, 0) +I∆(0, 0)4
+I∆(−2, 0)I∆(0,−1)2I∆(0, 1)−q
1
2I∆(−2, 0)I∆(−1, 1)I∆(0, 1)I∆(1,−2)−q
1
2I∆(−1, 0)I∆(0, 1)2I∆(1,−1)
−q− 1
2I∆(−1, 1)I∆(0,−1)2I∆(1, 0)−q
1
2I∆(−2, 1)I∆(0, 1)I∆(1,−1)I∆(1, 0) +I∆(0, 0)I∆(0, 1)I∆(1, 0)2
+I∆(−2, 0)I∆(0, 0)I∆(1,−1)I∆(1, 1)−q
1
2I∆(0, 0)I∆(0, 1)I∆(1, 0)I∆(1, 1) +qI∆(−2, 0)I∆(0, 2)2I∆(2,−2)
−q− 1
2I∆(−2, 0)I∆(−1,−1)I∆(−1, 0)I∆(2,−1)−q− 1
2I∆(−1, 0)I∆(−1, 1)I∆(0,−1)I∆(2,−1)
−q− 1
2I∆(−1, 2)I∆(0, 0)I∆(1,−1)I∆(2,−1))−q
3
2I∆(−3, 0)I∆(0, 3)2I∆(3,−3)
The ﬁrst 50 coeﬃcients ofI61(0) are given by:
1− 4q +q2 + 18q3 + 22q4 +q5− 78q6− 178q7− 254q8− 188q9 + 167q10 + 855q11 + 1864q12 + 2892q13 + 3426q14 + 2583q15−
488q16− 6698q17− 16273q18− 28550q19− 41189q20− 49943q21− 48554q22− 28899q23 + 17621q24 + 98726q25 + 217819q26 +
371551q27 + 544496q28 + 707360q29 + 811832q30 + 792301q31 + 565550q32 + 40436q33− 872995q34− 2241496q35− 4087180q36−
6354321q37−8877834q38−11348143q39−13283739q40−14014789q41−12685231q42−8288627q43 +266720q44 +14032731q45 +
33862808q46 + 60173861q47 + 92687285q48 + 130092845q49 + 169735693q50
7.7. Theindexofthe 72 knotcomplement. Theindex I72(0)isanotherexampleoflinear
growth. Thedefault SnapPytriangulation T ofthe 72 knotcomplementhas4idealtetrahedra,
and the Epstein-Penner decomposition has 8 ideal tetrahedra. The two triangulations are
related by geometric 2–3 moves and have equal indices. The angle structure equations ofT
are given by:
50 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
A =


1 2 1 0
0 0 1 0
1 0 0 1
0 0 0 1

 B =


1 0 0 0
1 0 0 0
0 2 1 0
0 0 1 2

 C =


0 0 1 0
0 1 0 2
1 1 1 0
1 0 0 0

 .
Eliminating B, andremovingthefourthrow(whichcorrespondstothefourthedgeequation),
we obtain the angle structure equations
A′α + B′γ =πν′
where
A′ =


0 2 1 0
−1 0 1 0
1 −2 −1 1

 B′ =


−1 0 1 0
−1 1 0 2
1 −1 0 0

 ν′ =


1
1
−1

 .
The index ofT is given by
I72(0)(q) =
∑
(k1,k2,k3)∈Z3
(−1)k1+k2−k3q
1
2 (k1+k2−k3)I∆(−k1,k 1 +k2−k3)I∆(−2k2,k 3)
I∆(k1 +k2−k3,−k2 +k3)I∆(−k2 +k3, 2k1− 2k3)∈ Z[[q]].
FT in R3 has 14 rays, spanned by the columns of the matrix


−2 −1 −1 0 0 0 0 0 0 1 1 1 1 2
−1 −1 0 −1 −1 −1 0 1 1 0 0 0 1 1
−2 −1 0 −2 −1 0 1 −1 0 0 1 2 1 3

 .
Ifδ(k1,k 2,k 3) denotes the degree of the summand andN∈ N, thenδ(k1,k 2,k 3)≤N implies
that (k1,k 2,k 3) satisfy the bounds
1−
√
1 + 2N≤k1≤ 1
2(−1 +
√
1 + 8N)
1
2(1−
√
1 + 4N)≤k2≤N
1−
√
1 + 2N≤k3≤ 1
2(−1 +
√
1 + 12N).
Observe that the upper bound fork3 is linear inN. The ﬁrst 50 coeﬃcients ofI72(0) are
given by:
1− 4q +q2 + 16q3 + 20q4 +q5− 72q6− 156q7− 206q8− 98q9 + 275q10 + 924q11 + 1740q12 + 2370q13 + 2227q14 + 495q15−
3485q16− 10168q17− 19045q18− 28467q19− 34899q20− 33157q21− 16460q22 + 22305q23 + 89035q24 + 185478q25 + 306146q26 +
434575q27+539981q28+575717q29+479148q30+176483q31−408854q32−1340316q33−2648389q34−4301970q35−6179555q36−
8036073q37− 9477453q38− 9942897q39− 8710346q40− 4925980q41 + 2323715q42 + 13897628q43 + 30430263q44 + 52111135q45 +
78414600q46 + 107796294q47 + 137380650q48 + 162674912q49 + 177363801q50
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 51
