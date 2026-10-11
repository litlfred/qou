---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "arXiv:alg-geom/9705010v1 7 May 1997"
section_id: sec-023-the-toda-system
section_title: "The Toda system"
section_number: null
pages: 31-33
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
---
A simple way to describe the Toda system is via the construction of Adler-
Kostant-Symes. Start with a decomposition g = a ⊕b of a Lie algebra g as vector
space direct sum of two of its subalgebras a, b. This induces a dual decomposition
g∗= a∗⊕b∗, an injection i := b∗֒ →g∗, and a projection π : g ։ b. Let Ox ⊂b∗
denote the coadjoint orbit of some x ∈b∗. The image i(Ox) ⊂g∗has, in general,
nothing to do with the coadjoint orbit Oi(x) of i(x) in g∗. So i∗of a G-invariant
function f on g∗can be a complicated, non-constant function on Ox. The AKS claim
is that any two such, i∗f1 and i∗f2, Poisson commute with respect to the natural
(Kirillov-Kostant) symplectic structure σOx on Ox. Indeed, let vj ∈g correspond
to the diﬀerential dfj|i(x) ∈g∗∗= g, so i∗dfj is given by π(vj). G-invariance of fj
implies that vj is conormal to Oi(x), i.e. that
0 = ⟨i(x), [g, vj]⟩.
We set aj := vj −π(vj) ∈a, and compute:
{i∗f1, i∗f2}Ox = σOx(πv1, πv2)
= ⟨x, [π(v1), π(v2)]b⟩
= ⟨i(x), [π(v1), π(v2)]g⟩
= ⟨i(x), [v1, π(v2)]g⟩−⟨i(x), [a1, π(v2)]g⟩
= ⟨i(x), [v1, π(v2)]⟩−⟨i(x), [a1, v2]⟩+ ⟨i(x), [a1, a2]⟩.
We have just seen that the ﬁrst two terms vanish when f1, f2 are G-invariant, and
the third term vanishes since it pairs i(x) ∈b∗= a⊥with [a1, a2] ∈a. This proves
AKS.
A shifted version of AKS is very convenient in applications. Replace the in-
clusion i : b∗֒ →g∗by its shifted version ǫ + i, where ǫ is an element of g∗which
annihilates [a, a] and [b, b]. The above argument goes through verbatim. For exam-
ple, take g = sl(n), a = strictly lower triangular matrices, b = upper triangulars,
32
RON Y. DONAGI
and (after identifying g with g∗, so that b∗becomes the lower triangulars):
ǫ =






0
1
0
...
0
1
0






, x =






0
1
0
...
0
1
0






.
The orbit Ox ⊂b∗consists of all matrices of the form:





b1
0
a1
...
...
0
an−1bn





with aj̸ = 0 and Σbj = 0. The shifted orbit consists of tridiagonal matrices:





b1
1
0
a1
·
·
·
·
·
·
·
1
0
an−1
bn




.
This is a 2(n−1)-dimensional symplectic manifold (X, σ), isomorphic as symplectic
manifold to the cotangent bundle of the maximal torus T ≈(C∗)n−1. The restric-
tion to it of the symmetric polynomials of SL(n) (= coeﬃcients of the characteristic
polynomial) gives n−1 independent, commuting Hamiltonians. This is the classical
Toda system.
An equivalent system is obtained if ǫ is replaced by m · ǫ with m ∈C∗. When
m = 0, the Hamiltonians become the symmetric functions of the bi. We get the
cotangent bundle X of (C∗)n−1, ﬁbered by its moment map over (C)n−1. Another
variant is to take ǫ = 0, but replace a by the algebra so(n) of skew symmetric
matrices. Now b∗sits in sl(n) as the symmetric matrices, and the orbit consists of
symmetric tridiagonal matrices






b1
c1
c1
b2
...
bn−1
cn−1
cn−1
bn






.
This is conjugate to the previous matrix with ai = c2
i , so we obtain a new version
( ˜X, ˜σ) of Toda which is just a 2n−1-sheeted cover of the previous, basic version,
(X, σ).
The Toda system for a semisimple Lie algebra g is obtained with b a Borel
subalgebra, a the nilpotent radical of the opposite Borel, x = Σeα and ǫ = Σe−α,
where the sums are over the simple roots α with respect to b, and the e±α are
normalized root vectors. The total space can again be identiﬁed with the cotangent
bundle of the maximal torus, a typical element having the form
Σ
α simple(bαhα +
aαeα + e−α) with respect to a standard basis hα, e±α.
Periodic Toda
SEIBERG-WITTEN INTEGRABLE SYSTEMS
33
The periodic Toda systems are obtained when the semisimple algebra g is re-
placed by a loop algebra g(1). This has an extended Dynkin diagram consisting of
the simple roots α of g plus the aﬃne root α0, corresponding to the highest root of
g. The general element of the periodic Toda system can thus be written as
Σα(bαhα + aαeα + e−α) + zeα0 + z−1a0e−α0,
where z is the loop variable, and the product a0
Q
α aα = µ is a ﬁxed non-zero
constant. (For g = sl(n), this is:





b1
1
a0z−1
a1
...
...
...
...
1
z
an−1
bn




,
with Q ai = µ, Σbj = 0).
