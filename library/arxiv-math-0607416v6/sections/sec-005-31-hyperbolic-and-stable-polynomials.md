---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-005-31-hyperbolic-and-stable-polynomials
section_title: "Hyperbolic and Stable Polynomials"
section_number: 3.1
pages: 9-16
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
---
nomials f, g ∈ H 1(R) interlace then the Wronskian W [f, g] := f ′g − f g′ is either
non-negative or non-positive on the whole real axis R.
Deﬁnition 6. Given f, g ∈ H 1(R) we say that f and g are in proper position,
denoted f ≪ g, if the zeros of f and g interlace and W [f, g] ≤ 0.
For technical reasons we also say that the zeros of the polynomial 0 interlace the
zeros of any (non-zero) hyperbolic polynomial and write 0 ≪ f and f ≪ 0. Note
that if f ≪ g and g ≪ f then f and g must be constant multiples of each other,
that is, W [f, g] ≡ 0.
The following theorem is a version of the classical Hermite-Biehler the orem [38].
Theorem 9 (Hermite-Biehler theorem) . Let h := f + ig ∈ C[z], where f, g ∈ R[z].
Then h ∈ H 1(C) if and only if f, g ∈ H 1(R) and g ≪ f . Moreover, h is strictly
stable if and only if f and g are strictly hyperbolic polynomials with no common
zeros and g ≪ f .
The next theorem is often attributed to Obreschkoﬀ [32].
Theorem 10 (Obreschkoﬀ theorem) . Let f, g ∈ R[z]. Then αf + βg ∈ H 1(R) ∪ {0}
for all α, β ∈ R if and only if either f ≪ g, g ≪ f , or f = g ≡ 0. Moreover, αf +βg
is strictly hyperbolic for all α, β ∈ R with α2 + β2 ⁄= 0 if and only if f and g are
strictly hyperbolic polynomials with no common zeros and ei ther f ≪ g or g ≪ f .
10 J. BORCEA AND P. BR ¨AND ´EN
Remark 5. Note that if T : πn(R) → π(R) is an R-linear operator then by
Obreschkoﬀ’s theorem T also preserves interlacing in the following manner: if f
and g are hyperbolic polynomials of degree at most n whose zeros interlace then
the zeros of T (f ) and T (g) interlace provided that T (f )T (g) ⁄= 0.
Lemma 1. Let n ∈ N. Suppose that T : Rn+1[z] → R[z] preserves hyperbolicity
and that f ∈ R[z] is a strictly hyperbolic polynomial of degree n or n + 1 for which
T (f ) = 0 . Then T (g) is hyperbolic for all g ∈ R[z] with deg g ≤ n + 1.
Let T : Cn[z] → C[z] be a stability preserver and suppose that f ∈ C[z] is a
strictly stable polynomial of degree n for which T (f ) = 0 . Then T (g) is stable for
all g ∈ C[z] with deg g ≤ n.
Proof. Let f be a strictly hyperbolic polynomial of degree n or n + 1 for which
T (f ) = 0 and let g ∈ R[z] be a polynomial with deg g ≤ n + 1. From Hurwitz’
theorem it follows that for ǫ ∈ R with |ǫ| small enough the polynomial f + ǫg is
strictly hyperbolic. Since deg( f + ǫg) ≤ n + 1 and T preserves hyperbolicity up to
degree n + 1 we get that T (g) = ǫ−1T (f + ǫg) is hyperbolic.
Suppose that f ∈ C[z] is a strictly stable polynomial of degree n such that
T (f ) = 0 and that the degree of g ∈ C[z] does not exceed n. By Hurwitz’ theorem
f + ǫg is strictly stable for all suﬃciently small |ǫ|. Since deg( f + ǫg) ≤ n and T
preserves stability up to degree n it follows that T (g) = ǫ−1T (f + ǫg) is stable. □
Lemma 2. Suppose that V ⊆ R[z] is an R-linear space whose every non-zero
element is hyperbolic. Then dim V ≤ 2.
Suppose that V ⊆ C[z] is a C-linear space whose every non-zero element is stable.
Then dim V ≤ 1.
Proof. We ﬁrst deal with the real case. Suppose that there are three line arly in-
dependent polynomials f1, f2 and f3 in V . By Obreschkoﬀ’s theorem the zeros
of these polynomials mutually interlace. Wlog we may assume that f1 ≪ f2 and
f1 ≫ f3. Consider the line segment ℓθ = θf3 + (1 − θ)f2, 0 ≤ θ ≤ 1. Since f1 ≪ ℓ0
and f1 ≫ ℓ1 by Hurwitz’ theorem there is a real number η between 0 and 1 such
that f1 ≪ ℓη and f1 ≫ ℓη. This means that f1 and ℓη are constant multiples of
each other contrary to the assumption that f1, f2 and f3 are linearly independent.
For the complex case let VR = {p : p + iq ∈ V with p, q ∈ R[z]} be the “real
component” of V . By the Hermite-Biehler theorem all polynomials in VR are hy-
perbolic, so by the above we have dim R VR ≤ 2. Clearly, V is the complex span of
VR. If dim R VR ≤ 1 we are done so we may assume that {p, q} is a basis for VR with
f := p + iq ∈ V . By deﬁnition W [p, q] ≥ 0 on the whole of R and the Wronskian is
not identically zero. Assume now that g is another polynomial in V . Then
g = ap + bq + i(cp + dq)
for some a, b, c, d ∈ R. We have to show that g is a (complex) constant multiple of
f . Since g ∈ V we have
W [ap + bq, cp + dq] = ( ad − bc)W [p, q] ≥ 0,
so that ad − bc ≥ 0. Now by linearity we have that
g + (u + iv)f = (a + u)p + (b − v)q + i((c + v)p + (d + u)q) ∈ V
for all u, v ∈ R which, as above, gives
H(u, v) := ( a + u)(d + u) − (b − v)(c + v) ≥ 0
P ´OLYA-SCHUR MASTER THEOREMS 11
for all u, v ∈ R. But
4H(u, v) = (2 u + a + d)2 + (2v + c − b)2 − (a − d)2 − (b + c)2,
so H(u, v) ≥ 0 for all u, v ∈ R if and only if a = d and b = −c. This gives
g = ap − cq + i(cp + aq) = ( a + ic)(p + iq) = ( a + ic)f,
as was to be shown. □
Notation 6. Let H−
1 (C) = {f ∈ C[z] : f (z) ⁄= 0 if Im(z) < 0}. By the Hermite-
Biehler theorem and Deﬁnition 6 if f, g ∈ R[z] then f + ig ∈ H −
1 (C) if and only if
f, g ∈ H 1(R) and f ≪ g. Given a linear subspace V of C[z] and M ⊆ V we say that
a linear operator T on V is stability reversing on M if T (H1(C)∩M ) ⊆ H −
1 (C)∪{0}.
Note that if S : C[z] → C[z] is the linear involution deﬁned by S(f )(z) = f (−z)
then T is stability reversing if and only if S ◦ T is stability preserving.
Lemma 3. Suppose that T : Rn[z] → R[z] maps all hyperbolic polynomials of
degree at most n to hyperbolic polynomials. Then T is either stability preserving or
stability reversing or the range of T has dimension at most two. In the latter case
T is given by
T (f ) = α(f )P + β(f )Q, f ∈ Rn[z], (3.1)
where P, Q are hyperbolic polynomials whose zeros interlace and α, β are real-valued
linear functionals on Rn[z].
Proof. The lemma is obvious for n = 0 so we may and do assume that n is a
positive integer. By Remark 5 and the Hermite-Biehler theorem we kn ow that T
maps all stable polynomials of degree n into the set H1(C) ∪ H−
1 (C) ∪ {0}. We now
distinguish two cases. Suppose ﬁrst that there are two strictly st able polynomials
f, g of degree n such that T (f ) ∈ H 1(C) and T (g) ∈ H −
1 (C).
Claim. If the above conditions are satisﬁed then the kernel of T must contain a
strictly hyperbolic polynomial of degree at least n − 1.
From Lemma 1 and the Claim we deduce that T : Rn[z] → π(R) ∪ {0}. Hence
all non-zero polynomials in the image of T are hyperbolic, which by Lemma 2 gives
that dim T (Rn[z]) ≤ 2 and thus T must be of the form (3.1).
Proof of Claim. Suppose that f1, f2 are two strictly stable polynomials of degree
n for which T (f1) ∈ H 1(C) and T (f2) ∈ H −
1 (C), respectively. By a homotopy
argument, invoking again Hurwitz’ theorem, there is a strictly stab le polynomial h
of degree n for which T (h) ∈ H 1(C) ∩ H−
1 (C) ∪ {0}. Writing h as h = p + iq, where
p and q are strictly hyperbolic polynomials (by the Hermite-Biehler theorem) gives
that T (p) and T (q) are constant multiples of each other. Suppose that deg p = n.
Then deg q ≥ n − 1 since the zeros of p and q interlace. If T (q) = 0 the claim is
obviously true so suppose that T (q) ⁄= 0. Then T (p) = λT (q) for some λ ∈ R. By
the Obreschkoﬀ Theorem p − λq is strictly hyperbolic and of degree at least n − 1.
Clearly, T (p − λq) = 0, which proves the Claim.
Suppose now that T maps all strictly stable polynomials of degree n into the
set H1(C) ∪ {0} (the case when T maps all such polynomials into H−
1 (C) ∪ {0}
is treated similarly). Let f be a strictly stable polynomial with deg f < n and
set fǫ(z) = (1 − ǫiz)n−deg f f (z). Then fǫ is strictly stable whenever ǫ > 0 and
T (fǫ) ∈ H 1(C) ∪ {0} since deg fǫ = n. Letting ǫ → 0 we get T (f ) ∈ H 1(C) ∪ {0}
and since strictly stable polynomials are dense in H1(C) it follows that T is stability
preserving. □
12 J. BORCEA AND P. BR ¨AND ´EN
As a ﬁnal tool we will need the Grace-Walsh-Szeg¨ o coincidence the orem [18, 42,
43]. Recall that a multivariate polynomial is multi-aﬃne if it has degree at most
one in each variable.
Theorem 11 (Grace-Walsh-Szeg¨ o coincidence theorem). Let f ∈ C[z1, . . . , zn] be
symmetric and multi-aﬃne and let C be a circular domain containing the points
ζ1, . . . , ζn. Suppose that either the total degree of f equals n or that C is convex (or
both). Then there exists at least one point ζ ∈ C such that
f (ζ1, . . . , ζn) = f (ζ, . . . , ζ).
From the Grace-Walsh-Szeg¨ o coincidence theorem we immediately deduce:
Corollary 5. Let f ∈ C[z1, . . . , zn] be of degree at most d in z1 and consider the
expansion of f in powers of z1,
f (z1, . . . , zn) =
d∑
k=0
Qk(z2, . . . , zn)zk
1 , Q k ∈ C[z2, . . . , zn], 0 ≤ k ≤ d.
Then f is stable if and only if the polynomial
d∑
k=0
Qk(z2, . . . , zn) ek(x1, . . . , xd)( d
k
)
is stable in the variables z2, . . . , zn, x1, . . . , xd, where ek(x1, . . . , xd), 0 ≤ k ≤ d, are
the elementary symmetric functions in the variables x1, . . . , xd given by e0 = 1 and
ek = ∑
1≤j1<j2<···<jk≤d xj1 · · ·xjk for 1 ≤ k ≤ d.
Lemma 4. Let T : Cn[z1] → C[z1] be a linear operator such that T [(z1 + w)n] ∈
H2(C). If f ∈ H m(C) is of degree at most n in z1 then T (f ) ∈ H m(C) ∪ {0}, where
T is extended to a linear operator on C[z1, . . . , zm] by setting T (zα1
1 · · ·zαm
m ) =
T (zα1
1 )zα2
2 · · · zαm
m for all α ∈ Nm with α1 ≤ n (compare with Notation 2).
Proof. Let f ∈ H m(C) be of degree n in z1. For ǫ > 0 set
fǫ(z1, . . . , zm) = f (z1 + ǫi, z2, . . . , zm).
Fixing ζ2, . . . , ζm in the open upper half-plane we may write fǫ(z1, ζ2, . . . , ζm) as
fǫ(z1, ζ2, . . . , ζm) = C(z1 −ξ1)(z1 −ξ2) · · · (z1 −ξn) = C
n∑
k=0
(−1)kek(ξ1, . . . , ξn)zn−k
1 ,
where C ⁄= 0 and Im(ξj ) < 0, 1 ≤ j ≤ n. Note that z1 ↦→fǫ(z1, ζ2, . . . , ζm) is
indeed a polynomial of degree n in z1. This is because
fǫ(z1, z2, . . . , zm) = zn
1 Qn(z2, . . . , zm) + terms of lower degree in z1
and Qn(z2, . . . , zn) := lim r→∞ r−nf (r, z2, . . . , zm) is stable by Hurwitz’ theorem
hence Qn(ζ2, . . . , ζn) ⁄= 0. Let us now write T [(z1 + w)n] as
T [(z1 + w)n] =
n∑
k=0
( n
k
)
T
(
zn−k
1
)
wk ∈ H 2(C).
By Corollary 5 we know that
n∑
k=0
T
(
zn−k
1
)
ek(w1, . . . , wn) ∈ H n+1(C).
P ´OLYA-SCHUR MASTER THEOREMS 13
But then
T (fǫ)(z1, ζ2, . . . , ζm) = C
n∑
k=0
T
(
zn−k
1
)
ek(−ξ1, . . . ,−ξn) ∈ H 1(C),
which gives T (fǫ) ∈ H m(C). Letting ǫ → 0 we have T (f ) ∈ H m(C) ∪ { 0}. If
f ∈ H m(C) is of degree less than n in z1 we may consider f ǫ = (1 − ǫiz1)n−deg f f ∈
Hm(C). Then by the above one has T (f ǫ) ∈ H n(C) ∪ {0} for all ǫ > 0. The lemma
now follows from Hurwitz’ theorem by letting ǫ → 0. □
We are now ready to prove Theorem 4.
Proof of Theorem 4. If T [(z +w)n] ∈ H 2(C) then by applying Lemma 4 with m = 1
it follows that T is stability preserving.
Suppose now that T preserves stability. Assume ﬁrst that there exists w0 ∈ C
with Im(w0) > 0 such that ( z + w0)n is in the kernel of T . Since ( z + w0)n is strictly
stable it follows from Lemma 1 and Lemma 2 that dim C T (Cn[z]) ≤ 1. Hence T is
given by T (f ) = α(f )P , where P is a ﬁxed stable polynomial and α : Cn[z] → C
is a linear functional. Otherwise we may assume that T [(z + w0)n] ∈ H 1(C) for all
w0 ∈ C with Im(w0) > 0 and conclude that T [(z + w)n] ∈ H 2(C). □
The proof of Theorem 2 now follows easily.
Proof of Theorem 2. Recall Notation 6 and note that by Lemma 3 we may assume
that dimR T (Rn[z]) > 2, so that T is either stability reversing or stability preserving.
By Theorem 4 T is stability reversing or stability preserving if and only if T [(z +
w)n] ∈ H 2(C) or T [(z − w)n] ∈ H 2(C), respectively, which proves the theorem. □
Proof of Theorem 3. By Theorem 2 it suﬃces to prove that if a linear operator
T : Cn[z] → C[z] satisﬁes T : πn(R) → π(R) then either
(a) There exists θ ∈ R such that T = eiθ ˜T , where ˜T : Rn[z] → R[z] is a
hyperbolicity preserver when restricted to Rn[z], or
(b) T is given by T (f ) = α(f )P , where α : Cn[z] → C is a linear functional
and P is a hyperbolic polynomial.
We prove this using induction on n ∈ N. If n = 0 there is nothing to prove so we
may assume that n is a positive integer. Note that T restricts to a linear operator
T ′ : πn−1(R) → π(R) and that by induction T ′ must be of the form (a) or (b)
above. Suppose that T ′ = eiθ ˜T ′, where ˜T ′ is a hyperbolicity preserver up to degree
n − 1. If T (zn) = eiθfn, where fn ∈ R[z] (actually, fn ∈ H 1(R) ∪ {0}), then T is of
the form (a). Hence we may assume that T (zn) = eiγfn, where 0 ≤ γ < 2π, γ − θ
is not an integer multiple of π and fn is a hyperbolic polynomial. Suppose that
there is an integer k < n such that T (zk) is not a constant multiple of fn. Let M
be the largest such k and set R(z) = e−iθT (zM ). Then
e−iθT
[
zM (1 + z)n−M ]
= R(z) +
(
r + ei(γ−θ)
)
fn(z)
for some r ∈ R. But this polynomial is supposed to be a complex constant multiple
of a hyperbolic polynomial, which can only happen if R and thus T
(
zM )
is a
constant multiple of fn. This contradiction means that T must be as in (b) above
with P = fn.
Assume now that T ′ is as in (b). If T (zn) is a constant multiple of P there is
nothing to prove, so we may assume that T (zn) = eiθfn, where 0 ≤ θ < 2π and
14 J. BORCEA AND P. BR ¨AND ´EN
fn is a hyperbolic polynomial which is not a constant multiple of P . Suppose that
there is an integer k < n such that α(zk)e−iθ /∈ R and let M be the largest such
integer. Then
e−iθT
[
zM (1 + z)n−M ]
=
(
α
(
zM )
e−iθ + r
)
P (z) + fn(z)
for some r ∈ R. However, the latter polynomial should be a complex constant
multiple of a hyperbolic polynomial and this can happen only if α(zM )e−iθ ∈ R,
which contradicts the above assumption. This means that T must be as in (a). □
Proof of Corollary 1. Note ﬁrst that if T : R[z] → R[z] is as in (a), (b) or (c) of
Corollary 1 then by Theorem 2 we have that T preserves hyperbolicity up to any
degree n ∈ N. Conversely, if T : R[z] → R[z] preserves hyperbolicity then for any
n ∈ N the restriction T : Rn[z] → R[z] preservers hyperbolicity (up to degree n).
The case when dim R T (R[z]) ≤ 2 is clear. Suppose now that dim R T (R[z]) > 2
and that T [(z + w)n] ∈ H 2(R) for some n ∈ N. Then by Lemma 4 we have that
T [(z + w)m] ∈ H 2(C) ∪ { 0} for all m ≤ n and since the latter polynomial has
real coeﬃcients we get T [(z + w)m] ∈ H 2(R) ∪ {0} for all m ≤ n. Similarly, if
T [(z − w)n] ∈ H 2(R) then T [(z − w)m] ∈ H 2(R) ∪ {0} for all m ≤ n. It follows
that if dim R T (R[z]) > 2 then either T [(z + w)n] ∈ H 2(R) ∪ {0} for all n ∈ N or
T [(z − w)n] ∈ H 2(R) ∪ {0} for all n ∈ N. □
By appropriately modifying the arguments in the proof of Corollary 1 one can
easily check that Corollary 2 follows readily from Theorem 4.
3.2. The T ranscendental Characterization. We will need the following lemma
due to Sz´ asz, see [41, Lemma 3].
Lemma 5 (Sz´ asz). Let m, n ∈ N with m ≤ n and f (z) = ∑ n
k=m ckzk ∈ C[z]. If
f (z) ∈ H 1(C) and cmcn ⁄= 0 then for any r ≥ 0 one has
|f (z)| ≤ | cm|rm exp
(
r |cm+1|
|cm| + 3r2 |cm+1|2
|cm|2 + 3r2 |cm+2|
|cm|
)
whenever |z| ≤ r.
For k, n ∈ N let ( n)k = k!
( n
k
)
= n(n − 1) · · · (n − k + 1) if k ≤ n and ( n)k = 0 if
n < k denote as usual the Pochhammer symbol.
Theorem 12. Let F (z, w) = ∑ ∞
k=0 Pk(z)wk be a formal power series in w with
polynomial coeﬃcients. Then F (z, w) ∈ H2(C) if and only if ∑ n
k=0(n)kPk(z)wk ∈
H2(C) ∪ {0} for all n ∈ N.
Proof. Suppose that F (z, w) = ∑ ∞
k=0 Pk(z)wk ∈ H2(C) has polynomial coeﬃcients.
Given n ∈ N, the sequence {(n)k}n
k=0 is a multiplier sequence, and since it is non-
negative it is a stability preserver by Theorem 3. By Corollary 2 and Le mma 4
we have that this multiplier extends to a map Λ : H2(C) → H 2(C) ∪ {0}. Now,
if ˜Fm(z, w) = ∑ Nm
k=0 Pm,k(z)wk is a sequence of polynomials in H2(C) converging
to F (z, w), uniformly on compacts, then Pm,k(z) → Pk(z) as m → ∞ uniformly
on compacts for ﬁxed k ∈ N. But then Λ[ ˜Fm(z, w)] → Λ[ F (z, w)] uniformly on
compacts, which gives ∑ n
k=0(n)kPk(z)wk ∈ H 2(C) ∪ {0}.
Conversely, suppose that ∑ n
k=0(n)kPk(z)wk ∈ H 2(C) ∪ {0} for all n ∈ N and let
Fn(z, w) = ∑ n
k=0(n)kn−kPk(z)wk.
P ´OLYA-SCHUR MASTER THEOREMS 15
Claim. Given r > 0 there is a constant Cr such that
|Fn(z, w)| ≤ Cr for |z| ≤ r, |w| ≤ r and all n ∈ N.
This claim proves the theorem since {Fn(z, w)}∞
n=0 is then a normal family whose
convergent subsequences converge to F (z, w) (by the fact that n−k(n)k → 1 for all
k ∈ N as n → ∞).
We ﬁrst prove the Claim in the special case when Pk(z) ∈ R[z] for all k ∈ N and
PK(z) is a non-zero constant, where K is the ﬁrst index for which PK (z) ⁄= 0.
Proof of the Claim in the special case. Let |PK (z)| = A, Br = max {|PK+1(z)| :
|z| ≤ r} and Dr = max{|PK+2(z)| : |z| ≤ r}. Then, if we ﬁx ζ ∈ C with Im(ζ) > 0,
we have that Fn(ζ, w) ∈ H 1(C) ∪ {0} and by Lemma 5
|Fn(ζ, w)| ≤ ArK exp
(
r Br
A + 3r2 B2
r
A2 + 3r2 Dr
A
)
(3.2)
whenever Im(ζ) > 0, |ζ| ≤ r and |w| ≤ r. If ζ ∈ C is ﬁxed with Im(ζ) < 0 then
Fn(ζ, −w) ∈ H 1(C) (since Fn(z, w) has real coeﬃcients and Fn(z, w) = Fn(z, w)).
By Lemma 5 this means that (3.2) holds also for Im(ζ) < 0 and by continuity also
for ζ ∈ R, which proves the Claim.
Next we assume that deg( PK (z)) = d ≥ 1. An application of Theorem 4 veriﬁes
that T = d/dz preserves stability, and by Lemma 4 T = ∂/∂z preserves stability
in two variables. Hence ∂Fn(z,w)
∂z ∈ H 2(R) ∪ {0} if Fn(z, w) ∈ H 2(R) ∪ {0}. To
deal with this case it is therefore enough to prove that if
⏐⏐⏐∂Fn(z,w)
∂z
⏐⏐⏐ ≤ Cr for
|z| ≤ r, |w| ≤ r and all n ∈ N then there is a constant Dr such that |Fn(z, w)| ≤ Dr
for |z| ≤ r, |w| ≤ r and all n ∈ N. Clearly, Fn(0, w) ∈ H 1(R) ∪ {0} for all n ∈ N.
Moreover, if m is the ﬁrst index such that Pm(0) ⁄= 0 then for n ≥ m we have
Fn(0, w) = ( n)mn−mPm(0)wm + (n)m+1n−m−1Pm+1(0)wm+1 + . . . ∈ H 1(R),
which by Lemma 5 gives
|Fn(0, w)| ≤ | Pm(0)|rm exp
(
r |Pm+1(0)|
|Pm(0)| + 3r2 |Pm+1(0)|2
|Pm(0)|2 + 3r2 |Pm+2(0)|
|Pm(0)|
)
=: Er
for |z| ≤ r. Here we have used that ( n)kn−k ≤ 1 and ( n)k+1n−k−1/(n)kn−k ≤ 1
for 0 ≤ k ≤ n. Suppose that
⏐⏐⏐⏐
∂Fn(z, w)
∂z
⏐⏐⏐⏐ ≤ Cr
for n ∈ N and |z| ≤ r, |w| ≤ r. Then,
Fn(z, w) = Fn(0, w) + z
∫ 1
0
∂Fn
∂z (zt, w)dt,
so
|Fn(z, w)| ≤ Er + rCr for |z| ≤ r, |w| ≤ r and all n ∈ N.
Next we prove the above Claim in the general case. For this we need a property
of multivariate stable polynomials that was established in [3, Corollary 1 ]:
Fact. If h = g + if ∈ H n(C) then f, g ∈ H n(R).
Now this means that if we let Pk(z) = Rk(z) + iIk(z) then we may write
Fn(z, w) = F Re
n (z, w) + iF Im
n (z, w)
16 J. BORCEA AND P. BR ¨AND ´EN
with F Re
n (z, w), F Im
n (z, w) ∈ H 2(R) ∪ {0}, where F Re
n (z, w), F Im
n (z, w) are given by
F Re
n (z, w) =
n∑
k=0
(n)kn−kRk(z)wk, F Im
n (z, w) =
n∑
k=0
(n)kn−kIk(z)wk.
By the above there are constants Ar and Br such that
|F Re
n (z, w)| ≤ Ar and |F Im
n (z, w)| ≤ Br for |z| ≤ r, |w| ≤ r and all n ∈ N.
Hence |Fn(z, w)| ≤
√
A2r + B2r for |z| ≤ r, |w| ≤ r and all n ∈ N, which proves the
Claim in the general case. □
