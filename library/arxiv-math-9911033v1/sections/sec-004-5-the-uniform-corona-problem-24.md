---
doc_id: arxiv-math-9911033v1
doc_title: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface"
section_id: sec-004-5-the-uniform-corona-problem-24
section_title: "The uniform corona problem 24"
section_number: 5
pages: 1-4
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface — 18 sections: Introductions 1; A lower bound estimate 4; A counterexample 11"
---
References 34
1. Introductions
Suppose M is an n-dimensional K¨ ahler manifold andL is an ample line
bundle over M . Let the K¨ ahler form of M be ω g and the Hermitian metric
ofL be H. We assume that ω g is the curvature of H, that is, ω g =Ric(H).
The K¨ ahler metric ofω g is called a polarized K¨ ahler metric on M .
Using H and ω g, for any positive integer m, H 0(M,L m) becomes a Her-
mitian inner product space. We use the following notations: suppose that
S,T ∈H 0(M,L m). Let <S,T > H m be the pointwise inner product and
(S,T ) =
∫
M
<S,T > H m
ω n
g
n!
be the inner product of H 0(M,L m). Let
||S|| =
√
<S,S > H m
be the pointwise norm. In particular, ||S||(x) denotes the pointwise norm
at x ∈M . Let
||S||L2 =
√
(S,S )
be the L2-norm of S.
Date: November 5, 2013.
1991 Mathematics Subject Classiﬁcation. Primary: 53A30; Secondary: 32C16.
Key words and phrases. Riemannian Surface, Teichm¨ uller Space, Collar Theorem.
Research supported by NSF grant DMS 9971506.
1
Let {S1, · · ·,S d(m)} be an orthonormal basis of H 0(M,L m). The quan-
tity(see [11])
d(m)∑
i=1
||Si||2(1.1)
plays an important rule in K¨ ahler-Einstein geometry and stability of complex
manifolds. If m is suﬃciently large, then there is a natural embedding
ϕ m : M → CP d(m)−1 by x ↦→[S1(x), · · ·,S d(m)(x)]. This follows from
the Kodaira’s embedding theorem. The metric 1
mϕ ∗ω F S on M is called the
Bergman metric. The following formula is an easy but key obse rvation made
by Tian [11] in his proof of the covergence of the Bergman metr ics:
1
m∂∂ log
d(m)∑
i=1
||Si||2 = 1
mϕ ∗ω F S −ω g.
A lot of work has been done by several authors [11], [9], [15], [2] and [8]
on the estimates of (1.1). However, these works are concentr ated on a single
manifold. On the other hand, in studying the stability and K¨ ahler-Einstein
geometry of manifolds, we need to study the behavior of (1.1) for a family of
manifolds. Tian’s work [12] on the Calabi Conjecture shows t he importance
and non-triviality of the problem of giving lower bound esti mate of (1.1) for
a family of complex surfaces. In the n-dimensional case, Tian [13] proved
that (1.1) has a positive lower bound depends on the dimensio n n, the
upper bound of the Betti numbers, the positve upper and lower bound of
the Ricci curvature and the Ln norm of the Riemannian sectional curvature.
In general, (1.1) maybe a useful tool in studying algebraic ﬁ berations over
a compact K¨ ahler manifold. The paper of interest to us are [5 ] and [6].
In this paper, we shall study the behavior of (1.1) on Riemann surfaces.
Even in the case of Riemann surfaces, the problem of ﬁnding a u niform
lower bound of (1.1) is nontrivial. In fact, by the counterex ample in §3, we
know that there is no uniform lower bound in general. We prove d a partial
uniform estimate in §4 which, I believe, is the “right” one in the sense that
it gives all the information on stability of the Riemann surf aces.
We also consider the coordinate ring of Riemann surfaces. Fo r smooth
Riemann surfaces M of genus g ≥ 2, it is well known that its coordinate
ring is ﬁnitely generated. That is, there is a positive integ er m0, such that
for any S ∈H 0(M,K m
M ) with m>m 0, we can ﬁnd Ui ∈H 0(M,K m0
M ),i ∈I
and Ti ∈H 0(M,K m−m0
M ),i ∈I such that
S =
∑
i∈I
UiTi,
where I is a ﬁnite set. In studying the behavior of Riemann surfaces n ear
the boundary of the Teichm¨ uller space, we need some uniform estimates. In
this paper, we give a uniform estimate which will give us the i nformation on
singular Riemann surfaces.
2
The above setting is similar to that in the corona problem in c omplex
analysis. The corona problem on the unit disk was studied by C arleson
in [1]. Carleson’s result stimulates many ideas which prove d to be useful for
other problems. An extensive discussion of the Carleson’s c orona theorem
can be found in [4].
Modifying Wolﬀ’s [14] proof of Carleson’s theorem together with the ∂-
estimate, we give a uniform corona estimate in the last secti on of this paper
as an application of Theorem 1.3. In order to obtain the resul t, we take
special care to the points where the injective radius are sma ll.
The organization of the paper is as follows: in §2, we give a lower bound
of (1.1) in terms of the genus g and the injective radius δ of M . In §3, we
give a counterexample which shows that the lower bound must d epend on δ.
In §4, we give the partial uniform estimate. That is, a lower boun d of (1.1)
atx ∈M depending only on the injective radius δx ofx. In §5, we solve the
uniform corona problem by the partial uniform estimate.
The main results of this paper are the following:
Theorem 1.1. Let M be a Riemann surface of the genus g ≥ 2. Let KM
be the canonical line bundle of M endowed with a Hermitian metric H. Let
the curvature ω g of H be positive. ω g gives a K¨ ahler metric of M . Let the
curvatureK of ω g satisfy
−K1 ≤K ≤K2
for nonnegative constants K1,K 2 ≥ 0 and let δ′ be the injective radius of
M . Let
δ = min(δ′, 1√K1 +K2
).
Then there is an absolute constant C >0 such that for m ≥ 2,
d(m)∑
i=1
||Si||2 ≥e− Cg3
δ 6 ,
where {S1, · · ·,S d(m)} is an orthnormal basis of H 0(M,K m
M ).
Theorem 1.2. For any ε >0 and m ≥ 2, there is a Riemann surface M
of genus g ≥ 2 with the constant Gauss curvature (−1) such that
inf
x∈M
d(m)∑
i=1
||Si||2 ≤ε.
The theorem disproves the conjecture that the absolute lowe r bound ex-
ists.
When the injective radius of M goes to zero, the ﬁrst eigenvalue and the
Sobolev constant will also go to zero. In this case, Theorem 1 .1 gives no
information. In the following theorem, we proved that (1.1) has a lower
bound which depends only on the local information and is inde pendent to
3
the injective radius of M . For this reason, we call the result partial uniform
estimate.
Theorem 1.3. Let M be a Riemann surface of genus g ≥ 2 and constant
curvature (−1). Then there are absolute constants m0 > 0 and D >0 such
that for any m > m0 and any x0 ∈ M , there is a section S ∈ H 0(M,K m
M )
with ||S||L2 = 1 such that
||S||(x0) ≥
√
m
D(1 + 1√mδ2x0
e
π
δx0 )
,(1.2)
whereδx0 is the injective radius of δx0.
On the coordinate ring ⊕∞
j=0H 0(M,K j
M ), we have the following
Theorem 1.4. Let M be a Riemann surface as above. Then there is an
m0 > 0 such that for any m > m0 and S ∈H 0(M,K m
M ), there is a decom-
position
S =
d∑
i=1
Si
of Si ∈H 0(M,K m
M )(i = 1, · · ·,d ) such that
||Si||L2 ≤C(m,m 0,g )||S||L2
||Si||L∞ ≤C(m,m 0,g )||S||L∞
(1.3)
for i = 1, · · ·d, and
Si =TiUi
for a basis U1, · · ·,U d of H 0(M,K m0
M ) and T1, · · ·,T d ∈H 0(M,K m−m0
M ).
Acknowledgment. The author thanks Professor Tian for suggesting me
this problem and his help during the preparing of this paper. He also thanks
Professor Phong for the support and some suggestions of the w ork.
