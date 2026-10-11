---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-007-3-periodic-families-and-pencils-of-flat-connecti
section_title: "Periodic families and pencils of flat connections"
section_number: 3
pages: 6-8
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
doc_brief: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS — We introduce a new notion of a periodic pencil of ﬂat connections on a smooth algebraic variety X."
---
3.1. Polynomial families and pencils of ﬂat connections. Let k be an algebraically
closed ﬁeld, X a smooth irreducible algebraic variety over k, and V a ﬁnite dimensional
k-vector space.
Deﬁnition 3.1. An n-parameter (polynomial) family of ﬂat connections on X with
values in V is a family of ﬂat connections
∇(s) = d −B(s),
s := (s1, ..., sn), on the trivial vector bundle X × V →X, where B ∈Ω1(X) ⊗EndV [s] (i.e.,
dB −[B, B] = 0, where d is the de Rham diﬀerential on X and [, ] is the supercommutator
in the graded algebra Ω•(X) ⊗EndV ).
Such a family is called a pencil if B is linear
homogeneous in s, i.e. B = Pn
j=1 sjBj, Bj ∈Ω1(X) ⊗EndV .
Thus a pencil of ﬂat connections is determined by a collection
Bj =
r
X
i=1
Bijdxi ∈Ω1(X) ⊗EndV, 1 ≤j ≤n
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
7
of 1-forms on X with values in EndV such that
(3.1)
dBj = [Bj, Bk] = 0, 1 ≤j, k ≤n.
Of course, if dim X = 1 then the ﬂatness conditions (3.1) are vacuous, and Bj can be
arbitrary. Yet this will already be an interesting case.
Remark 3.2. These deﬁnitions extend mutatis mutandis to the case when V is a possibly
nontrivial vector bundle on X. In this case the trivial connection d on the trivial bundle
X × V →X should be replaced by a ﬁxed ﬂat connection ∇(0) on the bundle V .
In
particular, when ∇is (aﬃne) linear in s, we have ∇(s) = ∇(0)−s1B1−...−snBn, where Bi ∈
Ω1(X, EndV ). In this case we will say that ∇is an aﬃne pencil of ﬂat connections. Note
that if V is trivial, we have ∇(0) = d−B0, so ∇(s) = d−B, where B = B0+s1B1+...+snBn,
which is an inhomogeneous (aﬃne) linear function in s, which justiﬁes the terminology. Note
that the notion of an aﬃne pencil (unlike that of an ordinary pencil) is stable under gauge
transformations, so it is the only meaningful notion when the bundle V is not necessarily
trivial and there is no canonical reference connection ∇(0).
We will, however, mostly restrict ourselves to the case when the bundle V is trivial, since
this is so in all the examples we consider.
3.2. Jumping loci of families of ﬂat connections. For a ﬂat connection ∇on a vector
bundle V on X, let Γ(∇) be the space of ﬂat global sections of ∇in Γ(X, V ).
Now let ∇(s), s ∈Cn be a family of ﬂat connections on the trivial bundle on X with ﬁber
V . For d ∈N let Qd(∇) be the set of s ∈Cn for which dim Γ(∇(s)) ≥d.
Lemma 3.3. Qd(∇) is a countable union of Zariski closed subsets2 of Cn.
Proof. Fix a basis {fi, i ≥1} of C[X], and for N ≤∞let C[X]N be the span of fi with
i ≤N. For a ﬂat connection ∇on the trivial bundle on X with ﬁber V , let Γ(∇)N be the
space of ﬂat sections of ∇in C[X]N ⊗V . In particular, Γ(∇)∞= Γ(∇).
Now let ∇(s) be our family.
For d ∈N let Qd,N(∇) be the set of s ∈Cn for which
dim Γ(∇(s))N ≥d.
Since Γ(∇(s))N is deﬁned inside C[X]N ⊗V by a ﬁnite system of
homogeneous linear equations with coeﬃcients in C[s], the subsets Qd,N(∇) ⊂Cn are Zariski
closed. Thus Qd(∇) = Qd,∞(∇) = S
N∈N Qd,N(∇) is a countable union of Zariski closed
subsets.
□
It is clear that Q0(∇) = Cn, Qd+1(∇) ⊂Qd(∇), and QdimV +1(∇) = ∅, so let d = d(∇)
be the largest integer in [0, dim V ] for which Qd(∇) = Cn, i.e., the smallest possible value of
dim Γ(∇(s)). The proper subset J(∇) := Qd+1(∇) of Cn is then called the jumping locus
of ∇. Lemma 3.3 implies
Corollary 3.4. The jumping locus J(∇) is a countable union of proper Zariski closed subsets
of Cn.
If a countable union of Zariski closed subsets of Cn is the whole Cn then one of them must
be the whole Cn, so there exists N = N(∇) ∈N such Qd,N(∇) = Cn. Thus for any s /∈J(∇)
we have Γ(∇(s))N = Γ(∇(s)). Hence for any point x ∈X the map J(∇)c →Gr(d, V ) from
the complement of J(∇) to the Grassmannian of d-dimensional subspaces in V given by
s 7→Γ(∇(s))|x is rational, i.e., is the restriction of a rational map γ(∇) : Cn →Gr(d, V ).
Note that, as any rational map, this map is regular outside a Zariski closed subset T(∇) ⊂Cn
of codimension ≥2.
2Note that Qd(∇) need not be Zariski closed. For example, if ∇(s) = d −s
xdx on C× then Q1(∇) = Z.
8
PAVEL ETINGOF AND ALEXANDER VARCHENKO
3.3. Periodic families and pencils of ﬂat connections.
Deﬁnition 3.5. A family ∇is said to be periodic if there exist shift operators
Aj ∈GL(V )(k(s)[X]), 1 ≤j ≤n
such that
∇(s + ej) ◦Aj(s) = Aj(s) ◦∇(s), 1 ≤j ≤n.
Remark 3.6. 1. Note that if ∇(s) has generically trivial endomorphism algebra (i.e., trivial
over C(s)) then Aj are unique up to multiplication by a scalar rational function of s. In this
case there exist scalar rational functions ξjk(s) such that
Ak(s + ej)Aj(s) = ξjk(s)Aj(s + ek)Ak(s).
2. As before, these deﬁnitions extend straightforwardly to the case when V is a possibly
nontrivial vector bundle on X.
Example 3.7. Let k = C, X = C×, V = C2, and ∇(s) = d −B(s, x), where
B(s, x) := 1
x

s
1
0
0

.
This family is actually an aﬃne pencil, since the dependence on s is aﬃne linear.
The
equation for ﬂat sections of ∇(s) is
( d
dx −B(s, x))F(x) = 0,
so it has a fundamental solution Fs(x) :=

xs
−1
s
0
1

. Thus Fs(x)−1 =

x−s
x−s
s
0
1

, so this
family is periodic with
A(s, x) = Fs+1(x)Fs(x)−1 =
x
x
s −
1
s+1
0
1

.
