---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-002-21-hyperbolicity-and-stability-preservers
section_title: "Hyperbolicity and Stability Preservers"
section_number: 2.1
pages: 3-7
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
---
swers to Problems 1–2 for R and the half-plane {z ∈ C : Im(z) ≤ 0} we need to
introduce some notation. As in [3] – and following the commonly used te rminology
in e.g. the theory of partial diﬀerential equations [2] – we call a non- zero univariate
polynomial with real coeﬃcients hyperbolic if all its zeros are real. Such a poly-
nomial is said to be strictly hyperbolic if in addition all its zeros are distinct. A
univariate polynomial f (z) with complex coeﬃcients is called stable if f (z) ⁄= 0 for
all z ∈ C with Im(z) > 0 and it is called strictly stable if f (z) ⁄= 0 for all z ∈ C with
Im(z) ≥ 0. Hence a univariate polynomial with real coeﬃcients is stable if and
only if it is hyperbolic. These classical concepts have several natur al extensions to
multivariate polynomials, the most general notion being as follows.
Deﬁnition 1. A polynomial f (z1, . . . , zn) ∈ C[z1, . . . , zn] is stable if f (z1, . . . , zn) ⁄=
0 for all n-tuples ( z1, . . . , zn) ∈ Cn with Im(zj) > 0, 1 ≤ j ≤ n. If in addition f
has real coeﬃcients it will be referred to as real stable. The sets of stable and real
stable polynomials in n variables are denoted by Hn(C) and Hn(R), respectively.
Note that f is stable (respectively, real stable) if and only if for all α ∈ Rn
and v ∈ Rn
+ the univariate polynomial f (α + vt) ∈ C[t] is stable (respectively,
hyperbolic). The connection between real stability and (G ˚ arding) hyperbolicity for
multivariate homogeneous polynomials is explained in e.g. [3, Proposition 1].
4 J. BORCEA AND P. BR ¨AND ´EN
Notation 1. Henceforth it is understood that if T is a linear operator on some
(real) linear subspace V ⊆ R[z1, . . . , zn] then T extends in an obvious fashion to a
linear operator – denoted again by T – on the complexiﬁcation V ⊕ iV of V .
Deﬁnition 2. A linear operator T deﬁned on a linear subspace V of C[z1, . . . , zn]
(respectively, R[z1, . . . , zn]) is called stability preserving (respectively, real stability
preserving) on a given subset M ⊆ V if
T (Hn(C) ∩ M ) ⊆ H n(C) ∪ {0} (respectively, T (Hn(R) ∩ M ) ⊆ H n(R) ∪ {0}).
A real stability preserver in the univariate case will alternatively be r eferred to as
a hyperbolicity preserver. For m ∈ N let Rm[z] = {f ∈ R[z] : deg( f ) ≤ m} and
Cm[z] = Rm[z]⊕iRm[z] = {f ∈ C[z] : deg( f ) ≤ m}. If T is a stability (respectively,
hyperbolicity) preserving operator on Cm[z] (respectively, Rm[z]) we will also say
that T preserves stability (respectively, hyperbolicity) up to degree m.
P´ olya-Schur’s characterization of multiplier sequences of the ﬁrs t kind that we
already alluded to in the introduction is given in the following theorem [12 , 28, 36].
Theorem 1 (P´ olya-Schur theorem). Let λ : N → R be a sequence of real num-
bers and T : R[z] → R[z] be the corresponding (diagonal) linear operator given by
T (zn) = λ(n)zn, n ∈ N. Deﬁne Φ( z) to be the formal power series
Φ( z) =
∞∑
k=0
λ(k)
k! zk.
The following assertions are equivalent:
(i) λ is a multiplier sequence,
(ii) Φ( z) deﬁnes an entire function which is the limit, uniformly on co mpact
sets, of polynomials with only real zeros of the same sign,
(iii) Either Φ( z) or Φ( −z) is an entire function that can be written as
Cz neaz
∞∏
k=1
(1 + αkz),
where n ∈ N, C ∈ R, a, αk ≥ 0 for all k ∈ N and ∑ ∞
k=1 αk < ∞,
(iv) For all non-negative integers n the polynomial T [(z + 1)n] is hyperbolic with
all zeros of the same sign.
As noted in e.g. [12, Theorem 3.3], parts (ii)-(iii) in P´ olya-Schur’s theorem give a
“transcendental” description of multiplier sequences while part (iv) provides an “al-
gebraic” characterization. We emphasize right away the fact that our main results
actually yield algebraic and transcendental characterizations of all hyperbolicity
and stability preservers, respectively, and are therefore natur al generalizations of
Theorem 1. Moreover, they also display an intimate connection betw een Problem 1
and its ﬁnite degree analog (Problem 2) in the case of (real) stability p reservers.
Notation 2. Given a linear operator T on C[z] we extend it to a linear operator –
denoted again by T – on the space C[z, w] of polynomials in the variables z, w by
setting T (zkwℓ) = T (zk)wℓ for all k, ℓ ∈ N.
Deﬁnition 3. Let α1 ≤ α2 ≤ · · · ≤ αn and β1 ≤ β2 ≤ · · · ≤ βm be the zeros of two
hyperbolic polynomials f, g ∈ H 1(R). We say that these zeros interlace if they can
be ordered so that either α1 ≤ β1 ≤ α2 ≤ β2 ≤ · · · or β1 ≤ α1 ≤ β2 ≤ α2 ≤ · · · .
P ´OLYA-SCHUR MASTER THEOREMS 5
Note that in this case one has |m − n| ≤ 1. By convention, the zeros of any two
polynomials of degree 0 or 1 interlace.
Our ﬁrst theorem characterizes linear operators preserving hyp erbolicity up to
some ﬁxed degree n.
Theorem 2. Let n ∈ N and let T : Rn[z] → R[z] be a linear operator. Then T
preserves hyperbolicity if and only if either
(a) T has range of dimension at most two and is of the form
T (f ) = α(f )P + β(f )Q, f ∈ Rn[z],
where α, β : Rn[z] → R are linear functionals and P, Q ∈ H 1(R) have
interlacing zeros, or
(b) T [(z + w)n] ∈ H 2(R), or
(c) T [(z − w)n] ∈ H 2(R).
Real stable polynomials in two variables have recently been characte rized by the
authors [3] as the polynomials f (z, w) ∈ R[z, w] that can be expressed as
f (z, w) = ± det(zA + wB + C), (2.1)
where A and B are positive semi-deﬁnite matrices and C is a symmetric matrix.
Hence (b) and (c) in Theorem 2 can be reformulated as
T [(z + w)n] = ± det(zA ± wB + C),
where A and B are positive semi-deﬁnite matrices and C is a symmetric matrix.
We will also need to deal with the case when we allow complex coeﬃcients .
Theorem 3. Let n ∈ N and let T : Cn[z] → C[z] be a linear operator. Then
T : πn(R) → π(R) if and only if either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ Cn[z],
where α : Cn[z] → C is a linear functional and P ∈ H 1(R), or
(b) T has range of dimension at most two and is of the form
T (f ) = ηα(f )P + ηβ(f )Q, f ∈ Cn[z],
where η ∈ C, α, β : Cn[z] → C are linear functionals such that α(Rn[z]) ⊆
R, β(Rn[z]) ⊆ R, and P, Q ∈ H 1(R) have interlacing zeros, or
(c) There exists η ∈ C such that ηT [(z + w)n] ∈ H 2(R), or
(d) There exists η ∈ C such that ηT [(z − w)n] ∈ H 2(R).
The corresponding theorem for stability preservers up to some ﬁx ed degree n
reads as follows.
Theorem 4. Let n ∈ N and let T : Cn[z] → C[z] be a linear operator. Then T
preserves stability if and only if either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ Cn[z],
where α : Cn[z] → C is a linear functional and P ∈ H 1(C), or
(b) T [(z + w)n] ∈ H 2(C).
From Theorems 2 and 4 we deduce the following algebraic characteriz ations of
hyperbolicity and stability preservers, respectively.
6 J. BORCEA AND P. BR ¨AND ´EN
Corollary 1 (Algebraic Characterization of Hyperbolicity Preservers) . A linear
operator T : R[z] → R[z] preserves hyperbolicity if and only if either
(a) T has range of dimension at most two and is of the form
T (f ) = α(f )P + β(f )Q, f ∈ R[z],
where α, β : R[z] → R are linear functionals and P, Q ∈ H 1(R) have inter-
lacing zeros, or
(b) T [(z + w)n] ∈ H 2(R) ∪ {0} for all n ∈ N, or
(c) T [(z − w)n] ∈ H 2(R) ∪ {0} for all n ∈ N.
Corollary 2 (Algebraic Characterization of Stability Preservers) . A linear operator
T : C[z] → C[z] preserves stability if and only if either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ C[z],
where α : C[z] → C is a linear functional and P ∈ H 1(C), or
(b) T [(z + w)n] ∈ H 2(C) ∪ {0} for all n ∈ N.
Notation 3. To any linear operator T : C[z] → C[z] we associate a formal power
series in w with polynomial coeﬃcients in z
GT (z, w) =
∞∑
n=0
(−1)nT (zn)
n! wn ∈ C[z][[w]].
Let n be a positive integer and denote by Hn(C) and Hn(R), respectively, the
set of entire functions in n variables that are limits, uniformly on compact sets,
of polynomials in Hn(C) and Hn(R), respectively. Hence in our notation H1(R)
is the Laguerre-P´ olya class of entire functions, sometimes denot ed by L-P in the
literature. For a description of H1(C) and H2(C) we refer to [28, Chap. IX].
Remark 1. As noted in [3], any linear operator T on C[z] may be uniquely rep-
resented as a formal linear diﬀerential operator with polynomials co eﬃcients, i.e.,
T = ∑ ∞
k=0 Qk(z) dk
dzk , where Qk ∈ C[z], k ≥ 0. In [3] we used the (formal) symbol of
T , i.e., FT (z, w) := ∑ ∞
k=0 Qk(z)wk ∈ C[z][[w]]. One can easily check that the “mod-
iﬁed symbol” GT (z, w) introduced in Notation 3 satisﬁes GT (z, w)ezw = FT (z, −w).
Theorem 5 (Transcendental Characterization of Hyperbolicity Preservers ). A lin-
ear operator T : R[z] → R[z] preserves hyperbolicity if and only if either
(a) T has range of dimension at most two and is of the form
T (f ) = α(f )P + β(f )Q, f ∈ R[z],
where α, β : R[z] → R are linear functionals and P, Q ∈ H 1(R) have inter-
lacing zeros, or
(b) GT (z, w) ∈ H2(R), or
(c) GT (z, −w) ∈ H2(R).
Theorem 6 (Transcendental Characterization of Stability Preservers) . A linear
operator T : C[z] → C[z] preserves stability if and only if either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ C[z],
where α : C[z] → C is a linear functional and P ∈ H 1(C), or
(b) GT (z, w) ∈ H2(C).
P ´OLYA-SCHUR MASTER THEOREMS 7
