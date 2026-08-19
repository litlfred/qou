---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae Takeshi MORITA∗"
section_id: sec-007-42-the-connection-formula-and-alternate-represen
section_title: "The connection formula and alternate representation"
section_number: 4.2
pages: 14-19
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae Takeshi MORITA∗ — We show connection formulae of local solutions of the Ramanu jan equation between the origin and the"
---
tion
At ﬁrst, we show the following connection formula between eq(·) and Eq(·).
Theorem 2. For any x ∈ C∗ \ [1;q],
eq(x) = (q;q)∞
θq(−x)Eq
(
−q
x
)
where |x|< 1.
Proof. The function eq(x) and Eq(x) have inﬁnite product as follows:
eq(x) = 1
(x;q)∞
, |x|< 1
14
and
Eq(x) = ( −x;q)∞.
We remark that eq(x) can be described as
eq(x) = 1
θq(−x)
(
q, q
x;q
)
∞
= (q;q)∞
θq(−x)Eq
(
−q
x
)
where |x|< 1. We obtain the conclusion.
Therefore, these q-exponential functions are related by the connection
formula between the origin and the inﬁnity. If we replace x byx/q , we obtain
the following lemma. This is useful to consider the connection problem in
the last section.
Lemma 5. For any x ∈ C∗ \ [1;q], the function eq(x/q ) has the following
alternate representation.
eq
(x
q
)
= (q;q)∞
θq
(
− x
q
) 0ϕ 1
(
−;q;q2, q5
x2
)
− (q;q)∞
θq
(
− x
q
) q2
(1 −q)x 0ϕ 1
(
−;q3;q2, q7
x2
)
.
Proof. From theorem 2,
1ϕ 0
(
0; −;q, x
q
)
= (q;q)∞
θq
(
− x
q
) Eq
(
−q2
x
)
= (q;q)∞
θq
(
− x
q
) 0ϕ 0
(
−; −;q, q2
x
)
.
Here,
0ϕ 0
(
−; −;q, q2
x
)
=
∑
k≥0
1
(q;q)k
(−1)kq
k(k− 1)
2
(q2
x
) k
and we remark that ( a;q)2k = (a,aq ;q2)k[2]. By separating the terms with
even and odd k ≥ 0, we obtain the conclusion.
4.3 The connection formula of the series 2ϕ 0(0, 0; −;q, ·)
The aim of this section is to give a proof for the following theorem;
15
Theorem 3. For any x ∈ C∗ \ [−λ;q],
θq(x)2f0
(
0, 0; −;q, −x
q
)
= (q;q)∞
θq(x)θq2
(
− λ 2
qx
)
θq
(
− λ
q
)
θq
(λ
x
) 1ϕ 1
(
0;q;q2, q2
x
)
+ (q;q)∞
1 −q
θq(x)θq2
(
− λ 2
x
)
θq
(
− λ
q
)
θq
(λ
x
)
λ
x 1ϕ 1
(
0;q3;q2, q3
x
)
.
We deﬁne the q-Borel-Laplace transformations of the ﬁrst kind to obtain
the connection formula between the origin and the inﬁnity.
Deﬁnition 3. For any analytic function f(x), the q-Borel transformation of
the ﬁrst kind B+
q is
(
B+
qf
)
(ξ) :=
∑
n≥0
anq
n(n− 1)
2 ξn =:ϕ (ξ),
the q-Laplace transformation of the ﬁrst kind L+
q is
(
L+
qϕ
)
(x) :=
∑
n∈Z
ϕ (λq n)
θq
(λq n
x
) .
We remark that the q-Borel transformation B+
q is formal inverse of the
q-Laplace transformation L+
q as follows;
Lemma 6. For any entire function f (x), we have
L+
q ◦ B+
qf =f.
We give the proof of theorem 3.
Proof. We apply theq-Borel transformation B+
q to the divergent seriesv(x) =
2ϕ 0(0, 0; −;q, −x/q ). We obtain
(
B+
qv
)
(ξ) = 1ϕ 0
(
0; −;q, ξ
q
)
=:ϕ (ξ).
From lemma 5,
ϕ (ξ) = (q;q)∞
θq
(
− ξ
q
) 0ϕ 1
(
−;q;q2, q5
ξ2
)
− (q;q)∞
θq
(
− ξ
q
) q2
(1 −q)ξ 0ϕ 1
(
−;q3;q2, q7
ξ2
)
16
where |ξ/q |< 1.
We apply the q-Laplace transformation L+
q to ϕ (ξ):
(
L+
qϕ
)
(x) =
∑
n∈Z
ϕ (λq n)
θq
(λq n
x
) =
∑
n∈Z
1ϕ 0
(
0; −;q, λq n
q
)
θq
(λq n
x
)
= (q;q)∞
θq
(
− λ
q
)
θq
(λ
x
)
∑
n−m∈Z
(q2)
(n− m)(n− m− 1)
2
(
−λ 2
qx
) n−m
×
∑
m≥0
(−1)m(q2)
m(m− 1)
2
(q;q2;q2)m
(q2
x
) m
− (q;q)∞
θq
(
− λ
q
)
θq
(λ
x
)
q2
(1 −q)λ
∑
n−m∈Z
(q2)
(n− m)(n− m− 1)
2
(
− λ 2
q2x
) n−m
×
∑
m≥0
(−1)m(q2)
m(m− 1)
2
(q3,q 2;q2)m
(q3
x
) m
.
Therefore,
2f0
(
0, 0; −;q, −x
q
)
= L+
q ◦ B+
q 2ϕ 0
(
0, 0; −;q, −x
q
)
= (q;q)∞
θq2
(
− λ 2
qx
)
θq
(
− λ
q
)
θq
(λ
x
) 1ϕ 1
(
0;q;q2, q2
x
)
+ (q;q)∞
1 −q
θq2
(
− λ 2
x
)
θq
(
− λ
q
)
θq
(λ
x
) 1ϕ 1
(
0;q3;q2, q3
x
)
.
We obtain the conclusion.
Acknowledgement
The author would like to thank Professor Yousuke Ohyama whose co mments
and suggestions were innumerably valuable throughout the course of this
study.
17
References
[1] G. D. Birkhoﬀ, The generalized Riemann problem for linear diﬀerent ial
equations and the allied problems for linear diﬀerence and q-diﬀerence
equations, Proc. Am. Acad. Arts and Sciences, 49 (1914), 521 − 568.
[2] G. Gasper and M. Rahman, Basic Hypergeometric Series, 2nd ed, Cam-
bridge, 2004.
[3] C. F. Gauss, Disquisitiones generales circa seriem inﬁnitam . . . , Comm.
soc. reg. sci. G¨ ott. rec., Vol. II; reprinted in Werke 3 (1876), 123-162.
[4] T. Hamamoto, K. Kajiwara, N. S. Witte, Hypergeometric solution s to
the q-Painlev´ e equation of type (A1 +A′
1)(1), Int. Math. Res. Not. Vol.
2006, Article ID 84619, Pages 1 − 26.
[5] Heine. E. Untersuchungen ¨ uber die Reihe..., J. reine angew. Math. 34,
285-328.
[6] M. E. H. Ismail, Asymptotics of q-Orthogonal Polynomials and a q-Airy
Function, Int. Math. Res. Not. (2005), No. 18 1063–1088.
[7] M. E. H. Ismail and C. Zhang, Zeros of entire functions and a pro blem
of Ramanujan, Adv. Math. 209 (2007), 363–380
[8] K. Kajiwara, T. Masuda, M. Noumi, Y. Ohta, and Y. Yamada, Hype r-
geometric solutions to the q-Painlev´ e equations, Int. Math. Res. Not.
(2004), no. 47, 2497–2521.
[9] T. Morita, A connection formula of the Hahn-Exton q-Bessel Function,
SIGMA,7 (2011), 115, 11pp.
[10] T. Morita, A connection formula of the q-conﬂuent hypergeometric func-
tion, arXiv:1105.5770.
[11] Y. Ohyama, A uniﬁed approach to q-special functions of the Laplace
type, arXiv:1103.5232.
[12] S. Ramanujan, The Lost Notebook and Other Unpublished Pape rs (with
an introduction by G. E. Andrews), Narosa, New Delhi, 1988.
18
[13] J. Sauloy, Algebraic construction of the Stokes sheaf for irre gular linear
q-diﬀerence equations, arXiv:math/0409393
[14] G. N. Watson, The continuation of functions deﬁned by genera lized
hypergeometric series, Trans. Camb. Phil. Soc. 21 (1910), 281–299.
[15] C. Zhang, Remarks on some basic hypergeometric series, in “Th eory
and Applications of Special Functions”, Springer (2005), 479–491 .
[16] C. Zhang, Sur les fonctions q-Bessel de Jackson, J. Approx. Theory, 122
(2003), 208–223.
[17] C. Zhang, Une sommation discr` e pour des ´ equations aux q-diﬀ´ erences
lin´ eaires et ` a coeﬃcients, analytiques: th´ eorie g´ en´ erale et exemples,
in “Diﬀerential Equations and Stokes Phenomenon”, World Scientiﬁc
(2002), 309–329.
19
