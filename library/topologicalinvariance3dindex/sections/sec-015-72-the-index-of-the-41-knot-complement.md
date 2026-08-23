---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-015-72-the-index-of-the-41-knot-complement
section_title: "The index of the 41 knot complement"
section_number: 7.2
pages: 44-45
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
41 knot complement uses 2 regular ideal tetrahedra and coincides with the Epstein-Penner
decomposition, thus XEP
41 ={T}. SnapPy gives the angle structure matrices of T:
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
equations; we will not use these in our examples so we omit them here. We eliminate B to
obtain A and B. We choose our basic edge set B ={e1} and excluded edge set X ={e2}.
We can therefore ignore the rows of our matrices corresponding to e2, and write
A′ =
( 1 1 )
B′ =
(−1 −1 )
ν′ =
( 0 )
.
Here A′ is just A with the last row omitted, and similarly for the other primed symbols. We
obtain the angle structure equations
A′α + B′γ =πν′.
Equation (17) gives that
I41(0)(q) =
∑
k∈Z
I∆(k,k )(q)2∈ Z[[q]].
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 45
Equation (12) implies that the degree δ(k) of the summand is given by the piecewise quadratic
polynomial
δ(k) = 2δ(k,k ) = 2k2 +|k|.
Its corresponding fan FT in R consists of two rays, corresponding to the columns of the
matrix ( 1 −1 )
.
Here, a column vector v of a matrix, spans the ray R+v. It follows that for every natural
number N we have
I41(0)(q) +O(q)N+1 =
⌈1/4(−1+√1+8N)⌉∑
k=⌊1/4(−1−√1+8N)⌋
I∆(k,k )(q)2 +O(q)N+1.
To compute I∆(k,k )(q) +O(q)N+1, we use its de
nition (5) and truncate the n-summation
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
Putting everything together, the 
rst 100 coe
cients of I41(0)(q) are given by
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
The 
rst 1000 coe
cients are available from [Gara].
