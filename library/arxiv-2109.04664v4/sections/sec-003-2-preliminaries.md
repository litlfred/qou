---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-003-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 4-6
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
In this section, we ﬁrst introduce the colored Jones polynomial, and then we
deﬁne a quantum dilogarithm, and variants of the logarithm and the d ilogarithm.
We also describe some of their properties.
For a knot K in the three-sphere S3, we denote by JN (K;q) the colored Jones
polynomial of K associated with the N -dimensional irreducible representation of
the Lie algebra sl(2; C) [12, 32]. We normalize it so that JN (U ;q) = 1 for the
unknot U ⊂S3. Note that J2(K;q) is the original Jones polynomial [9].
Let E be the ﬁgure-eight knot. We use the following formula obtained by
K. Habiro [7, P. 36 (1)] and T.T.Q. Le [14, P. 129]. See also [15].
JN (E;q) =
N −1∑
k=0
k∏
l=1
(
q(N −l)/ 2 −q−(N −l)/ 2
)(
q(N +l)/ 2 −q(N +l)/ 2
)
=
N −1∑
k=0
q−kN
k∏
l=1
(
1 −qN −l)(
1 −qN +l)
.
(2.1)
Next, we deﬁne functions TN (z), L0(z), L1(z), and L2(z), which are related as
TN (z) = N
ξ L2(z) +O(1/N ) ( N → ∞),
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 5
d L2
dz (z) = −2π
√
−1L1(z),
d L1
dz (z) = −L0(z).
Let ξ be a positive real number. We deﬁne C0 := (−∞, −1] ∪ {eτ √−1 | 0 ≤τ ≤
π } ∪ [1, ∞) and Cθ :=e
√−1θC0, where θ is a positive real number with tan θ <π
ξ
and we orient C0 from left to right.
Consider the following integrals:
∫
Cθ
e(2z−1)x
x sinh(x) sinh(γx)dx,
∫
Cθ
e(2z−1)x
xm sinh(x)dx,
where m = 0, 1, 2, γ := ξ
2Nπ √−1 for an integer N ≥ 2, and z is a complex number
with 0 < Re(ze
√−1θ ) < cosθ. Here we follow [4] to introduce TN (z), which plays
an important role in the paper. Note that the set of the poles of the integrands are
{kπ
√
−1 |k ∈ Z} ∪ {2lNπ 2/ξ |l ∈ Z} and {kπ
√
−1 |k ∈ Z},
respectively. Therefore, if N is large enough, then the only pole inside the unit circle
centered at the origin is 0 ∈ C and so the path of integral Cθ avoids the poles. Proofs
of their convergences (Lemmas 2.1 and 2.2 below) are given in Section 6.
Lemma 2.1. The integral
∫
Cθ
e(2z−1)x
x sinh(x) sinh(γx )dx converges if z ∈ C satisﬁes
−ξ sinθ
4Nπ < Re(zeθ√−1)< cosθ + ξ sinθ
4Nπ .
Lemma 2.2. If z ∈ C satisﬁes 0 < Re(zeθ√−1) < cosθ, then the integral∫
Cθ
e(2z−1)x
xm sinh(x)dx converges for m = 0, 1, 2.
Now deﬁne functions TN (z) and Lm(z) (m = 0, 1, 2) by using the integrals above.
Deﬁnition 2.3. Fix an integer N ≥ 2 and put γ := ξ
2Nπ √−1 . We deﬁne
TN (z) := 1
4
∫
Cθ
e(2z−1)x
x sinh(x) sinh(γx)dx,
for a complex number z with −ξ sinθ
4Nπ < Re(zeθ√−1)< cosθ + ξ sinθ
4Nπ .
Deﬁnition 2.4. For a complex number z with 0 < Re(ze
√−1θ )< cosθ, we deﬁne
L0(z) :=
∫
Cθ
e(2z−1)x
sinh(x) dx,
L1(z) := − 1
2
∫
Cθ
e(2z−1)x
x sinh(x)dx,
L2(z) := π √−1
2
∫
Cθ
e(2z−1)x
x2 sinh(x)dx.
Lemma 2.5. Form = 0, 1, 2, we calculate Lm(z) as follows.
L0(z) = −2π √−1
1 −e−2π √−1z,(2.2)
L1(z) =





log
(
1 −e2π √
−1z
)
if Imz ≥ 0,
π √−1(2z − 1) + log
(
1 −e−2π √−1z
)
if Imz <0,
(2.3)
