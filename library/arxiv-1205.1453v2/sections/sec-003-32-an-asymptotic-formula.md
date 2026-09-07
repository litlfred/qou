---
doc_id: arxiv-1205.1453v2
doc_title: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗"
section_id: sec-003-32-an-asymptotic-formula
section_title: "An asymptotic formula"
section_number: 3.2
pages: 9-12
source_pdf: 1205.1453v2.pdf
source_sha256: 29d1b1fd9466a3d8
doc_brief: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗ — We show an asymptotic formula of the divergent bilateral bas ic hypergeometric series 1ψ 0(a; −;q, ·)"
---
In this section, we show an asymptotic formula of (20) with using the q-Borel-
Laplace transformations of the ﬁrst kind. We show the following the orem.
Theorem 1. For any x ∈ C∗ \ [−λ;q], we have
ˆ1ψ 0(a; −;λ;q,x ) = (q;q)∞
(q/a ;q)∞
θ(aqλ )
θ(qλ )
θ (ax/λ )
θ (x/λ )
1
(1/ax ;q)∞
,
where 1< |ax|.
Proof. We apply the q-Borel transformation B+
q to the series 1ψ 0(a; −;q,x ).
Then,
ψ (ξ) :=
(
B+
q 1ψ 0
)
(ξ) = 1ψ 1(a; 0;q, −ξ).
By Ramanujan’s sum (14), we obtain the inﬁnite product represent ation of
ψ (ξ) as follows;
ψ (ξ) = (q;q)∞
(q/a ;q)∞
θ(aξ)
θ(ξ) (−q/ξ ;q)∞ .
9
We apply the q-Laplace transformation L+
q,λ to ψ (ξ).
(
L+
q,λ ψ
)
(x) =
∑
n∈ Z
ψ (λq n)
θ
( λq n
x
) = (q;q)∞
(q/a ;q)∞
∑
n∈ Z
1
θ( λq n
x )
θ(aλq n)
θ(λq n)
(
− q
λq n ;q
)
∞
= (q;q)∞
(q/a ;q)∞
1
θ(λ/x )
θ(aλ)
θ(λ)
∑
n∈ Z
q
n(n− 1)
2
( λ
ax
) n (
− q
λq n ;q
)
∞
= (q;q)∞
(q/a ;q)∞
1
θ(λ/x )
θ(aλ)
θ(λ) (−q/λ ;q)∞ 1ψ 1(−λ; 0;q, 1/ax ). (22)
We remark that
1ψ 1(−λ; 0;q, 1/ax ) = θ(λ/ax )
(−q/λ ;q)∞ (1/ax ;q)∞
.
Combining (22) and (10), we obtain the conclusion.
Theorem 1 is rewritten by
(
L+
q,λ ◦ B+
q ˜u
)
(x) = (q;q)∞
(q/a ;q)∞
θ(aqλ )
θ(qλ )
θ(ax/λ )
θ(x/λ )
θ(x)
θ(ax) ˜u∞ (x).
We deﬁne the function C(x;q) as follows;
C(x;q) := (q;q)∞
(q/a ;q)∞
θ(aqλ )
θ(qλ )
θ(ax/λ )
θ(x/λ )
θ(x)
θ(ax).
Then, C(x;q) is single valued as a function of x.
Corollary 1. The function C(x;q) is the q-elliptic function, i.e., C(x;q)
satisﬁes
C(qx;q) = C(x;q), C (e2πix;q) = C(x;q).
4 The limit q → 1 − 0 of the asymptotic for-
mula
In this section, we give the limit q → 1 − 0 of our asymptotic formula.
We assume that x ∈ C∗ \ [−λ;q] ( −π < argx < π). We put a = qα and
x ↦→x/ (1 −q) in theorem 1 to consider the limit. We remark that the limit
of the left-hand side in theorem 1 formally gives the bilateral hyperg eometric
series 1H0(α ; −; −x). We show the following theorem.
10
Theorem 2. For any x ∈ C∗ \ [−λ;q] (−π <argx<π ), we have
lim
q→ 1− 0
(q;q)∞
(q1− α ;q)∞
θ(qα +1λ)
θ(qλ )
θ
( qαx
(1 −q)λ
)
θ
( x
(1 −q)λ
) 1(
(1 −q) q− α
x ;q
)
∞
= Γ(1 −α )
xα e
1
x,
where 1< |x|.
We give the proof of theorem 2.
Proof. The right-hand side of theorem 1 is rewritten by
(q;q)∞
(q1− α ;q)∞
θ(qα +1λ)
θ(qλ )
θ
(
qα
(1− q)
x
λ
)
θ
(
1
(1− q)
x
λ
) 1(
(1 −q) q− α
x ;q
)
∞
= Γ q(1 −α )θ(qα +1λ)
θ(qλ )



θ
(
qα
(1− q)
x
λ
)
θ
(
q0
(1− q)
x
λ
) (1 −q)− α


eq
(
(1 −q) 1
qαx
)
.
Combining (9), (11), (12) and (8), we obtain the conclusion.
Acknowledgement
My heartfelt appreciation goes to Professor Yousuke Ohyama who provided
carefully considered feedback and valuable comments.
References
[1] G. E. Andrews, R. Askey and R. Roy, Special Functions, Encyclo pedia
of Math. Appl. 71, Cambridge Univ. Press, Cambridge, 1999.
[2] G. D. Birkhoﬀ, The generalized Riemann problem for linear diﬀerent ial
equations and the allied problems for linear diﬀerence and q-diﬀerence
equations, Proc. Am. Acad. Arts and Sciences, 49 (1914), 521 − 568.
[3] G. Gasper and M. Rahman, Basic Hypergeometric Series, 2nd ed, Cam-
bridge, 2004.
11
[4] G. H. Hardy, Ramanujan, Cambridge University Press, Cambridge;
reprinted by Chelsea, New York, 1978.
[5] Heine. E. Untersuchungen ¨ uber die Reihe..., J. reine angew. Math. 34,
285-328.
[6] M. E. Horn, Bilateral binomial theorem, SIAM Problem 03-001 (2003).
[7] T. H. Koornwinder and R. F. Swarttouw, On q-analogues of the Fourier
and Hankel transforms, Trans. Amer. Math. Soc. 333 (1992), 445-461.
[8] T. Morita, A connection formula of the Hahn-Exton q-Bessel Function,
SIGMA,7 (2011), 115, 11pp.
[9] T. Morita, A connection formula of the q-conﬂuent hypergeometric func-
tion, arXiv:1105.5770.
[10] T. Morita, On local solutions of the Ramanujan equation and the ir con-
nection formulae, arXiv:1203.3404.
[11] J. Sauloy, Algebraic construction of the Stokes sheaf for irre gular linear
q-diﬀerence equations, arXiv:math/0409393
[12] L. J. Slater, Generalized Hypergeometric Functions, Cambridge Univer-
sity Press, Cambridge, 1966. MR0201688 (34:1570)
[13] G. N. Watson, The continuation of functions deﬁned by genera lized
hypergeometric series, Trans. Camb. Phil. Soc. 21 (1910), 281–299.
[14] C. Zhang, Remarks on some basic hypergeometric series, in “Th eory
and Applications of Special Functions”, Springer (2005), 479–491 .
[15] C. Zhang, Sur les fonctions q-Bessel de Jackson, J. Approx. Theory, 122
(2003), 208–223.
[16] C. Zhang, Une sommation discr` e pour des ´ equations aux q-diﬀ´ erences
lin´ eaires et ` a coeﬃcients, analytiques: th´ eorie g´ en´ erale et exemples,
in “Diﬀerential Equations and Stokes Phenomenon”, World Scientiﬁc
(2002), 309–329.
12
