---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-015-i-elliptic-integrals-and-linear-fractional-trans
section_title: "I Elliptic integrals and linear fractional transformations"
section_number: null
pages: 31-35
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
From equation (85) we know that we may write A2(x,w ) as
A2(x,w ) = 1
π
∫ c2(x)
c1(x)
1√
−Q1(x;r)
· Q1(x;r)
Q2(x,w ;r)dr, (243)
where we have written the square-root of the quartic in the denom inator, which is what is typically done
for elliptic integrals. The next step for elliptic integrals is to use linear f ractional transformations to bring
the elliptic integral in the Legendre normal form. In our case, this m eans the following. Suppose we ﬁnd a
non-singular linear fractional transformation Φ : C∪{∞}→ C∪{∞} deﬁned as
Φ(z) = Az + B
Cz + D , (244)
where AD− BC⁄= 0, which is then invertible, with inverse Φ −1 : C∪{∞}→ C∪{∞} given by
Φ −1(ξ) = Dξ− B
−Cξ + A. (245)
Then if we take r = Φ −1(s), and if we know
AD− BC > 0 and Φ( c1(x))< Φ(c2(x)), (246)
then we may change variables, using r = Φ −1(s) to get
A2(x,w ) = 1
π
∫ Φ( c2(x))
Φ( c1(x))
1√
−Q1(x; Φ −1(s))
· Q1(x; Φ −1(s))
Q2(x,w ; Φ −1(s))
AD− BC
(−Cs + A)2 ds, (247)
where the last factor comes from taking the derivative dr =dΦ −1(s). We rewrite this as follows
A2(x,w ) = 1
π
∫ Φ( c2(x))
Φ( c1(x))
Q1(x; Φ −1(s))
Q2(x,w ; Φ −1(s))· 1√
−Q1(x; Ds−B
−Cs+A )· (−Cs + A)4
ds, (248)
31
because then we choose a,b,c,d ∈ R such that the term inside the square-root becomes
−Q 1
(
x; Ds− B
−Cs + A
)
· (−Cs + A)4 =−x2 ∏
ρ∈{c1(x),c2(x),d1(x),d2(x)}
(
Ds− B−
(
− Cs + A
)
ρ
)
, (249)
where we used (52). But we know the quartic function in s on the right hand side of (249) is such that it
vanishes at Φ( c1(x)), Φ( c2(x)), Φ( d1(x)) and Φ( d2(x)). Therefore, by the fundamental theorem of algebra,
we have
−Q 1
(
x; Ds− B
−Cs + A
)
· (−Cs + A)4 =−x2 ∏
ρ∈{c1(x),c2(x),d1(x),d2(x)}
((
D + Cρ
)
·
(
s− Φ(ρ)
)
. (250)
If we choose Φ such that
Φ(c1(x)) = −1, Φ(c2(x)) = 1 , Φ(d1(x)) = 1 /k, Φ(d2(x)) = −1/k, (251)
for some number k∈ (0, 1), then we will have the desired form for the Legendre convention ,
−Q 1
(
x; Ds− B
−Cs + A
)
· (−Cs + A)4 = Ξ( x)· (1−s2)(1−k2s2), (252)
where the constant Ξ( x) may be calculated as
Ξ(x) = −x2
k2 ·
(
D + C·c1(x)
)
·
(
D + C·c2(x)
)
·
(
D + C·d1(x)
)
·
(
D + C·d2(x)
)
. (253)
Of course, k also depends on x, as do A, B, C and D. So from all of this we obtain
A2(x,w ) = 1
π
√
Ξ(x)
∫ 1
−1
Q1(x; Φ −1(s))
Q2(x,w ; Φ −1(s))· 1√
(1−s2)(1−k2s2)
ds, (254)
assuming we have found the linear fractional transformation Φ suc h that (251) holds.
Lemma I.1 Forx,w∈ (0,∞) satisfying 4x +w2 < 1, we have
A2(x,w ) = 2
π√1− 4x
∫ −(1−4x)1/ 2
−(1+4x)− 1/ 2
1√ (
1− (1 + 4x)r2)(
1− (1− 4x)−1r2)· Q1
(
x;L−1(r)
)
Q2
(
x,w ;L−1(r)
)dr. (255)
Changing variables, by letting t =r/√1− 4x, this gives
A2(x,w ) = 2
π
∫ −1
−(1−16x2)− 1/ 2
1√
(1−t2)
(
1− (1− 16x2)t2)· Q1
(
x;L−1(r√1− 4x)
)
Q2
(
x,w ;L−1(r√1− 4x)
)dr. (256)
This still leaves the problem of determining the transformation beha vior forQ1(x;·)/Q2(x,w ;·). Fortunately,
one easy solution is to obtain the partial fraction decomposition for this rational function.
Lemma I.2 Suppose AD− BC⁄= 0 and suppose we have ρ∈ C∪{∞}\{− D/C}, then for Φ and Φ −1 as in
(244) and (245), we have
1
Φ −1(ξ)−ρ =− C
Cρ + D + AD− BC
(Cρ + D)2· 1
ξ− Φ(ρ). (257)
Proof: Simply calculate
Φ −1(ξ)−ρ = Dξ− B
−Cξ + A−ρ = Dξ− B + Cξρ− Aρ
−Cξ + A = (D + Cρ)ξ− (Aρ + B)
−Cξ + A . (258)
So 1
Φ −1(ξ)−ρ = −Cξ + A
(D + Cρ)ξ− (Aρ + B) = 1
Cρ + D· −Cξ + A
ξ− Aρ+B
Cρ+D
. (259)
32
Rewriting this as a partial fraction,
1
Φ −1(ξ)−ρ =− C
Cρ + D + 1
Cρ + D·
Cξ− C· Aρ+B
Cρ+D− Cξ + A
ξ− Aρ+B
Cρ+D
. (260)
Simplifying, this is equal to (257). □
We mention a useful reference for simplifying elliptic integrals [24], mor e speciﬁcally Section 19.14
https://dlmf.nist.gov/19.14.
One reference therein is a well-known preprint [19] available from the web link
https://cs.uwaterloo.ca/~glabahn/Papers/ellipticPrePrint.pdf.
Let us now give the partial fraction decomposition of Q1(x;·)/Q2(x,w ;·), and also determine the linear
fractional transformation Φ that satisﬁes (251).
Lemma I.3 LetZ(x,w ) ={A1(x,w ),A2(x,w ),b 1(x,w ),b 2(x,w )}, which is the variety of roots of Q2(x,w ;·).
Then, as meromorphic function on C∪{∞}, we have the partial fraction decomposition of Q1(x;·)/Q2(x,w ;·):
∀z∈ C∪{∞}\Z (x,w ), Q1(x;z)
Q2(x,w ;z) = 1 +
∑
ρ∈Z(x,w)
1
z−ρ· w2ρ2
x2
∏
σ∈Z(x,w)\{ρ}
1
ρ−σ. (261)
Proof: Note that by equation (49) we have
∀ρ∈Z (x,w ), Q1(x;ρ) = Q2(x,w ;ρ) +w2ρ2 = w2ρ2, (262)
becauseZ(x,w ) is the variety of roots of Q2(x,w ;·). By equation (56), we know that for each ρ∈Z (x,w ),
we have 1
Q2(x,w ;z) = 1
x2· (z−ρ)
∏
σ∈Z(x,w)\{ρ}
1
z−σ. (263)
Therefore, we have
∀ρ∈Z (x,w ), lim
z→ρ
Q1(x;ρ)
Q2(x,w ;z) = w2ρ2
x2
∏
σ∈Z(x,w)\{ρ}
1
ρ−σ. (264)
That gives the coeﬃcient of 1 /(z−ρ) for each of the roots. For the limit as z→∞ , we have
lim
z→∞
Q1(x;z)
Q2(x,w ;z) = 1 , (265)
because the leading coeﬃcient of each of the quartics Q1(x;·) andQ2(x,w ;·) is the same, x2. Therefore, the
meromorphic function equal to the left-hand-side minus the right- hand-side of (261) is a function with no
poles and which converges to 0 at ∞. So, by Liouville’s theorem from complex analysis, this diﬀerence is
identically 0. In other words, equation (261) is valid. □
References
[1] Lars V. Ahlfors. Complex Analysis. McGraw-Hill Inc., New York, USA, 1979.
[2] Michael Aizenman, Joel Lebowitz and David Ruelle. Some rigorous r esults on the Sherrington-
Kirkpatrick spin glass model. Commun. Math. Phys. 112, 3–20 (1987).
[3] Michael Aizenman and Anastasia Ruzmaikina. Characterization of invariant measures at the leading
edge for competing particle systems. Ann. Probab. 33, no. 1, 82–113 (2005).
[4] Michael Aizenman, Robert Sims and Shannon Starr. An extended variational principle for the SK
spin-glass model. Phys. Rev. B 68, 214403 (2003).
[5] David Aldous and Persi Diaconis. Longest increasing subsequenc es: from patience sorting to the Baik-
Deift-Johansson theorem. Bull Amer. Math. Soc. 36, no. 4, 413–432 (1999).
33
[6] David Aldous and J. Michael Steele. The Objective method: Proba bilistic combinatorial optimization
and local weak convergence Encyclopaedia Math. 110, 1–72 (2004).
[7] Louis-Pierre Arguin and Michael Aizenman. On the structure of q uasi-stationary competing particle
systems. Ann. Probab. 37, 1080–1113 (2009).
[8] Antonio Auﬃnger and Wei-Kuo Chen. The Parisi formula has a uniqu e minimizer. Commun. Math. Phys.
35, 1429–1444 (2015).
[9] Jinho Baik, Percy Deift and Kurt Johansson. On the distribution o f the length of the longest increasing
subsequence of random permutations. J. Amer. Math. Soc. 12, no. 4, 1119–1178 (1999).
[10] H.E. Boos, V.E. Korepin, Y. Nishiyama, M.Shiroishi. J. Phys. A: Math. General , 35, no. 20, 4443 (2002),
10 pages.
[11] Charalambos A. Charalambides. Enumerative Combinatorics. CRC Press, Taylor & Francis group, Boca
Raton, FL, 2002.
[12] Duncan Dauvergne, Janosch Ortmann, and B´ alint Vir´ ag. The directed landscape. Preprint,
https://arxiv.org/abs/1812.00309
[13] Bernard Derrida. Random-energy model: An exactly solvable mo del of disordered systems. Phys. Rev.
B24, 2613–2626 (1981).
[14] Bernard Derrida. A generalization of the random energy model which includes correlations between
energies. J. Phys. Lett. 46, L401–L407 (1985).
[15] Gerald B. Folland. Real Analysis: Modern Techniques and Their Applications. 2 nd Ed. John Wiley &
Sons, Inc., New York, USA, 1999.
[16] Francesco Guerra. Broken replica symmetry bounds in the mea n ﬁeld spin glass model. Com-
mun. Math. Phys. 233 1–12 (2003).
[17] Francesco Guerra and Fabio-Lucio Toninelli. Quadratic replica co upling in the SherringtonKirkpatrick
mean ﬁeld spin glass model. J. Math. Phys. 43, 3704–3716 (2002).
[18] H, M. Hammersley. A fee seedlings of research. In: Proc. 6th Berkeley symp. math. statist. and probability,
vol.1, pp. 345–394. University of California Press, California 1972.
[19] George Labahn and Mark Mutrie. Reduction of elliptic integrals to Legendre normal form. Technical
report Technical Report 97-21, Department of Computer Scienc e, University of Waterloo, Waterloo,
Ontario (1997).
[20] B. F. Logan and L. A. Shepp. A variational problem for random Y oung tableaux. Advances in Math. 26
206–222 (1977).
[21] Henry McKean. Probability: the classical limit theorems. Cambridge University Press, Cambridge, UK,
2014.
[22] Henry McKean and Victor Moll. Elliptic curves: function theory, geometry, arithmetic. Cambridge
University Press, Cambridge, UK, 1999.
[23] Marc Mezard, Giorgio Parisi and Miguel-Angel Virasoro. Spin Glass Theory and Beyond: An Intro-
duction to the Replica Method and Its Applications. World Scientiﬁc Publishing Company, Singapore,
1987.
[24] F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark,
B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain, eds. NIST D igital Library of Mathematical
Functions. http://dlmf.nist.gov/, Release 1.1.8 of 2022-12-15.
[25] Dmitry Panchenko. The Parisi ultrametricity conjecture. Ann. Math. 177, 383–393 (2013).
[26] Dmitry Panchenko. The Sherrington-Kirkpatrick Model. Springer, New York, 2013.
[27] Robin Pemantle and Mark C. Wilson. Analytic Combinatorics in Several Variables. Cambridge University
Press, New York, USA, 2013.
[28] Ross G. Pinsky. Law of large numbers for increasing subsequen ces of random permutations. Random
Structures Algorithms 29, no. 3, 277–295 (2006).
[29] Ross G. Pinsky. When the law of large numbers fails for increasing subsequences of random permutations.
Ann. Probab. 35, no. 2, 758–772 (2007).
[30] Georg P´ olya. Uber eine Aufgabader Wahrscheinichkeitsrechn ung betreﬀend die Irrfahrt im Straßennetz.
Math. Ann. 84, no. 1–2, 149–160 (1921).
34
[31] David Ruelle. A mathematical reformulation of Derrida’s REM and G REM. Commun. Math. Phys. 108,
225–239 (1987).
[32] David Sherrington and Scott Kirkpatrick. Solvable model of a sp in-glass. Phys. Rev. Lett. 35, no. 26,
1792–1796 (1975).
[33] J. Michael Steele. Probability theory and combinatorial optimization. Society for Industrial and Applied
Mathematics, Philadelphia, PA, 1997.
[34] Michel Talagrand. The Parisi formula. Ann. Math. 163, 221–263 (2006).
[35] A. M. Vershik and S. V. Kerov. Asymptotics of the Plancherel m easure of the symmetric group and the
limiting form of Young tables. Soviet Math. Dokl. , 18, 527–531 (1977).
[36] J. L. van Hemmen and R. G. Palmer. The replica method and solvab le spin glass model. J. Phys. A:
Math. Gen. 12 563–580 (1979).
35
