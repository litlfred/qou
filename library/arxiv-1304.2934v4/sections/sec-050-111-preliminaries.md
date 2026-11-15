---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-050-111-preliminaries
section_title: "Preliminaries"
section_number: 11.1
pages: 91-93
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
11.1.1. Non-commutative probability theory. The originality of this section is that, al-
though the problem is formulated in a classical probability space, it is natural to work
in the setting of non-commutative probability theory.
Deﬁnition 11.7. A non-commutative probability space is a complex unital ⋆-algebra A
with some linear functional ϕ : A →C such that ϕ(1) = 1 and, for any a ∈A , ϕ(a⋆a) ≥0.
This generalizes the notion of probability space: elements of A should be thought as
random variables, while ϕ should be thought as the expectation. The difference is that,
unlike random variables in usual probability theory, elements of A are not assumed
to commute. Usually one also assumes that ϕ is tracial, i.e., ϕ(ab) = ϕ(ba) for any
a, b ∈A .
There are ﬁve natural analogues of the notion of independence in non-commutative
probability theory, see [Mur03]. In our context, the relevant one is the following one,
sometimes called tensor independence [HS10, Deﬁnition 1.1].
Deﬁnition 11.8. Two subalgebras A1 and A2 of A are tensor independent if and only if, for
any sequence a1, . . . , ar with, for each i, ai ∈A1 or ai ∈A2, one has
ϕ(a1 . . . ar) = ϕ




→
∏
1≤i≤r
ai∈A1
ai



ϕ




→
∏
1≤i≤r
ai∈A2
ai



.
The arrow on the product sign means that the ai in the product appear in the same order as in
a1, . . . , ar.
With this deﬁnition of independence, the notion of dependency graph presented in
Section 9.1 is immediately extended to the non-commutative framework. One can also
deﬁne joint cumulants as follows: if a1, . . . , ar are elements in A , we set
κ(a1, . . . , ar) = ∑
π
µ(π) ∏
B∈π
ϕ
 
→
∏
i∈B
ai
!
.
92
VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Note that, in the proof of Theorem 9.7, independence is only used in equation (45). By
deﬁnition of tensor independence, equation (45) also holds in the non-commutative
setting and hence, so does Theorem 9.7.
11.1.2. Two probability spaces. From now on, we ﬁx an element ω in the Thomas sim-
plex Ω. Denote CS(n) the group algebra of S(n). The function τω, deﬁned by Equa-
tion (52), can be linearly extended to CS(n). Then (CS(n), τω) is a non-commutative
probability space.
Note that we are now working with two probability spaces: the non-commutative
probability space (CS(n), τω) and the usual probability space that we want to study
(the set of Young diagrams of size n with the probability measure Pω,n). They are
related as follows. Consider an element y in CS(n) and deﬁne the random variable
(for the usual probability space) Xy by Xy(λ) = bχ(y). Then one has
EPω,n(Xy) = ∑
λ⊢n
Pω,n(λ)bχ(y) = τω(y).
In other words, the expectations of y (in the non-commutative probability space) and of
Xy (in the usual probability space) coincide (recall that the trace of a non-commutative
probability space, here τω, is considered as an expectation).
Besides, if we restrict to the center of (CS(n), τω), then the map y 7→Xy is an algebra
morphism, called discrete Fourier transform. As a consequence, if y1, . . . , yr lie in the
center of (CS(n), τω), their joint moments (and joint cumulants) are the same as those
of Xy1, . . . , Xyr.
11.1.3. Renormalized conjugacy classes and polynomiality of cumulants. Given a partition
µ = (µ1, . . . , µℓ) of size |µ| = ∑ℓ
i=1 µi = k, we denote
Σµ,n = ∑
A
ρµ(A) where ρµ(A) = (a1, . . . , aµ1)(aµ1+1, . . . , aµ1+µ2) · · · .
In the equation above, the formal sum is taken over arrangements in A(n, k) and is
considered as an element of the group algebra CS(n). It clearly lies in its center. Be-
sides, Σµ,n is the sum of n↓k elements of cycle-type µ, hence, if ρ is a ﬁxed permutation
of type µ, one has:
XΣµ,n = n↓kXρ.
Note that considering these elements Σµ,n and their normalized characters is a classical
trick in the study of central measures on Young diagrams; see [IO02, ´Sni06b, FM12].
Fix some permutations ρ1, . . . , ρr of respective size k1, . . . , kr. Denote µ1, . . . , µr their
cycle-types.
n↓k1 · · · n↓kr κ

X(n)
ρµ1, . . . , X(n)
ρµr

= κ(Σµ1, . . . , Σµr)
=
∑
A1∈A(n,k1)
...
Ar∈A(n,kr)
κ

ρµ1(A1), . . . , ρµr(Ar)

.
(53)
MOD-φ CONVERGENCE, I
93
As in the framework of subgraph count statistics, the invariance of τω by conjugacy of
its argument implies that the joint cumulant κ

ρµ1(A1), . . . , ρµr(Ar)

depends only on
the graph GA associated to the family of arrangement A = (A1, . . . , Ar). Copying the
proof of Corollary 10.6, we get:
Lemma 11.9. Fix some integer partitions µ1, . . . , µr. Then the rescaled joint cumulant
κ(Σµ1, . . . , Σµr) = n↓k1 · · · n↓kr κ

X(n)
ρµ1, . . . , X(n)
ρµr

is a polynomial in n.
