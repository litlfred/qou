---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-002-12-state-integrals
section_title: "State integrals"
section_number: 1.2
pages: 3-5
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜ no [ 9] that perturbative series associated with the hyperbolic knots 4 1 and 5 2 are resurgent and"
---
where e(z) = exp(2 πiz) and Σ is the associated Riemann surface. In particular, Σ is deﬁned
by taking points p = (z, m) where z∈ C\(Z− iR) and m∈ Z with the equivalences
(k + 0 + iy, m)∼ (k− 0 + iy, m + B) for y < 0 , k ∈ Z ,
(z, m + A)∼ (z + 1, m) . (3)
Given the second equivalence relation, we can always represent poin ts p∈ Σ as p = ( z, m)
with m = 0 ,··· , A− 1. The critical points of V are in bijective correspondence with the
roots of the polynomial
P (x) = ( −x)A− (1− x)B . (4)
Indeed, to each root P (x0) = 0 the point
p0 = ( z0, m0) =
( log(x0)
2πi , B
2πi log(1− x0)− Alog(x0)
2πi − A
2
)
(5)
is a critical point of V . These roots are all distinct and therefore the critical points are
non-degenerate (see Appendix A). Notice that all ambiguities in the logarithms lead to
equivalent points in Σ. The function V computes the volumes of the 4 1 and 52 knots with the
parameters (A, B) = (1 , 2) and (2 , 3), respectively. Indeed, we ﬁnd that ( z1, m1) = (−1/6, 0)
and ( z2, m2) = (−5/6, 0) are the two critical points when A = 1 and B = 2 and these have
volumes
V (−1/6, 0) = 0 .051418··· i , V (−5/6, 0) = −0.051418··· i . (6)
We will denote the collection ( A, B, p0) by Ξ. Let V⊂ C denote the set of critical values,
which includes Z. Denote the set of rays R≥0
2πi
V −V0
byS(V0)⊆ C. These form a peacock
pattern so that C\S(V0) consists of a countable set of cones, see Figure 10.
We are interested in a perturbative expansion of certain integrals a t the critical points of
the function V . These integrals involve the formal series Ψ( z, ℏ)∈ C/llbracketℏ/rrbracketdeﬁned by
Ψ( z, ℏ) = µ8 exp
(
− (2πi)2
24ℏ − ℏ
24−
∞∑
k=0
Bk
k! Li2−k(e(z))ℏk−1
)
, (7)
where µ8
8 = 1 is an eighth root of unity and Bk denotes the k-th Bernoulli number. Explicitly,
for each Ξ the formal series is deﬁned by
Φ Ξ (ℏ) =
∫
Ψ( z, ℏ)B exp
(
− A
2ℏ (2πi)2z
(
z + 1− ℏ
2πi
)
+ (2πi)2 m0z
ℏ
)
dz , (8)
where we take the formal Gaussian integration around the critical point z0. More precisely,
consider the series
∞∑
k=0
∞∑
ℓ=−⌊k/3⌋
ak,ℓwkℏℓ∈ C/llbracketℏ , w/rrbracket (9)
4 VERONICA F ANTINI AND CAMPBELL WHEELER
deﬁned through the following equation
exp
(
− V (z0, m0)
ℏ − δ
ℏ w2
) ∞∑
k=0
∞∑
ℓ=−⌊k/3⌋
ak,ℓwkℏℓ
= Ψ( z0 + w, ℏ)B exp
(
− A
2ℏ (2πi)2(z0 + w)
(
z0 + w + 1− ℏ
2πi
)
− (2πi)2 m0(z0 + w)
ℏ
)
,
(10)
for some constant δ. Then, formal Gaussian integration gives
Φ Ξ (ℏ) =
√
−2πiℏ
δ exp
(
− V (z0, m0)
ℏ
) ∞∑
k=0
∞∑
ℓ=−⌊2k/3⌋
a2k,ℓ
(2k− 1)!!
δk ℏℓ+k. (11)
Given that Bk Li2−k(x) = O((k!)2(2π| log(x)|)−k) and exponentiation preserves the property
of being Gevery-1 [ 20, Thm. 5.55], it is easy to see that these series are Gevery-1, i.e. the
coeﬃcient of ℏk grows like A k! C k as k→∞ . We will prove that Φ Ξ is in fact Borel–Laplace
summable in Theorem 1.4. Importantly, for ( A, B) = (1 , 2) and (2 , 3), the series Φ Ξ give the
series Φ 41 and Φ 52 respectively. This was explicitly illustrated in [ 12, Sec. 7] but known in
previous work such as [ 10, Sec. 1.3].
1.2. State integrals. We are interested in the resurgent and summability properties of th e
series Φ Ξ (ℏ), which was deﬁned in terms of the quantum dilogarithm Ψ( z, ℏ) in Equation (11).
The latter was shown to be resurgent and Borel–Laplace summable t o a function given in
terms of Faddeev’s quantum dilogarithm Φ( z; τ ) (see [ 11, 2]). The function Φ( z; τ ) is a
meromorphic function of ( z, τ )∈ C× (C\R≤0) with poles located on a cone z∈ Z≥0 + τ Z≥0
and zeros located on the opposite cone z∈ Z<0 + τ Z<0. In addition, it has a variety of
descriptions
(qe(z); q)∞
(e(z/τ );~q)∞
= Φ( z; τ ) = exp
( ∫
i√τ R+ε√τ
e((z + 1 + τ )w/τ )
(e(w)− 1)(e(w/τ )− 1)
dw
w
)
, (12)
where ( x; q)k = ∏ k−1
j=0(1− qjx), the ﬁrst equality holds for τ ∈ H, and the second for
Re(−√τ− 1/√τ ) < Re(z/√τ ) < 0. We refer to [ 1, 6] and Appendix B for general properties
of the function Φ( z; τ ). We can now consider integrals of the same form as Equation ( 8)
replacing1 Ψ( z, ℏ) by Φ( zτ ; τ ): for ( A, B)∈ Z2
>0 with A⁄= B and m, ℓ∈ Z we deﬁne
Im,ℓ(τ ) := µB
8~q−B/24qB/24
∫
Jℓ,τ
Φ(( z− ℓ)τ ; τ )Be
( A
2 z(zτ + τ + 1) + mzτ
)
dz , (13)
whereJℓ,τ := ( i√τ e−iAǫR≥0− 1
2 + ℓ)∪ ( i√τ e−i(A−B)ǫR≤0− 1
2 + ℓ) for some small ǫ > 0.
The fact that Φ( z; τ ) is meromorphic for τ ∈ C\R≤0 implies that Im,ℓ(τ ) is holomorphic
for τ∈ C\R≤0. These integrals are not independent. Indeed, using the quasi-pe riodicity of
Faddeev’s quantum dilogarithm, Φ(z−τ ; τ ) = (1−e(z))Φ( z; τ ), one easily ﬁnds the relations
B∑
k=0
( B
k
)
(−1)kq−ℓkIm+k,ℓ(τ ) = Im,ℓ+1(τ ) = ( −1)AqA+mIm+A,ℓ(τ ) . (14)
1The relation between the variables is ℏ =−2πi/τ .
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 5
Therefore, over the ﬁeld Q(q) there are max {A, B} independent integrals. The Andersen–
Kashaev state integrals for 4 1 and 5 2 given in [ 1] correspond to m = ℓ = 0.
The conjectural description of the resurgent structure of the series Φ K requires the in-
troduction of all of the max {A, B} integrals [ 9]. What was not previously clear was how
to construct the explicit combination of state integrals to give the B orel–Laplace resumma-
tion of one of the asymptotic series of interest. In Section 3.1, we describe an algorithm
to compute this combination using the geometry of the function V and the asymptotics of
Faddeev’s quantum dilogarithm.
To understand the asymptotics of Φ( zτ ; τ ) for large τ , we need to consider an unusual
but useful principle branch of the dilogarithm function. For θ∈ (0, 2π) deﬁne the domain
Cθ = C\
(
(Z≥0 + eiθR≤0)∪ (Z<0 + eiθR≥0)
)
depicted in Figure 1.
Figure 1. Domain of D 3π/4(z) given by C\
(
(Z≥0 + (i− 1)R≤0)∪ (Z<0 + (i− 1)R≥0)
)
.
Deﬁne D θ : Cθ→ C to be
Dθ(z) =
∫ eiθ/2∞
z
∫ eiθ/2∞
w
e(ζ)
1− e(ζ)dζ dw , (15)
where the contours are contained in Cθ. This branch of the dilogarithm allows for us to
describe the asymptotics of Φ( zτ ; τ ).
Theorem 1.2. Suppose that τ∈ C\R≤0 and ε∈ R>0. Then as |τ|→∞ with ﬁxed argument
and z is bounded away from C\Cθ by ε, there exists a constant C > 0, independent of ε,
such that
⏐
⏐
⏐e(−Dθ(z)τ )Φ( zτ ; τ )− e
( 1
2 D′
θ(z) +
K∑
k=2
Bk
k!
(2πi)k−2
τ k−1 Li2−k(e(z))
) ⏐
⏐
⏐ < C ε −K K!|τ|−K , (16)
with θ = arg(−1/τ )∈ (0, 2π).
The proof of this theorem is described in Appendix
B (see Theorem B.6).
