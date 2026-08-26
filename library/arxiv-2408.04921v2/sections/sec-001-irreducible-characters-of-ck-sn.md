---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING"
section_id: sec-001-irreducible-characters-of-ck-sn
section_title: "Irreducible characters of Ck \u2240 Sn"
section_number: 2
pages: 4-6
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING — 5 sections: Introduction; Irreducible characters of Ck ≀ Sn; X ij"
---
The generalized symmetric group Ck ≀ Sn is the wreath product of the
cyclic group Ck of order k with the symmetric group Sn of n elements, i.e.
the semidirect product Ckn ⋊ Sn , where the symmetric group Sn acts on
the direct product Ckn = Ck × · · · × Ck by permutating the factors. The
multiplication is given by
(g; σ) · (h; τ ) = (gσ(h); στ ),

(2.1)

where g, h ∈ Ckn and σ, τ ∈ Sn .
Since Ck is an abelian group of order k, there are exactly k conjugacy
classes, given by {1}, {c}, · · · , {ck−1 }, where Ck = hci. The order of the
centralizer of each conjugacy class is k. Its irreducible characters are given
by γi , i = 0, . . . , k − 1, where γi (cj ) = ω ij , and ω = e2πi/k is the k-th
primitive root of unity. The space of class functions on Ck is given by
R(Ck ) =

k−1
M

Cγi .

i=0

The conjugacy classes of Ck ≀ Sn are parametrized by colored partitions.
The color set is I = {0, 1, · · · , k − 1}, the indexing set of conjugacy classes.
The conjugacy class of an element x = (g; σ) ∈ Ck ≀ Sn corresponds to the
I-colored partition λ = (λ(i) ), which consists of |I| partitions λ(i) such that
Pk−1 (i)
kλk = i=0
|λ | = n, the ith partition λ(i) given by
i

i

λ(i) = (1m1 (c ) 2m2 (c ) · · · ),

where mj (ci ) equals to the number of j-cycles in σ whose cycle product
is ci . We also say that the colored partition λ = (λ(i) ) is supported at its
constituent subpartitions λ(i) . In particular, a colored partition λ supported
at only one color has one nontrivial constituent subpartition, and all other
constituents are empty.
Given a partition λ = (λ1 , λ2 , . . . , λl ), one can paint the parts with the
colors {0, 1, . . . , k − 1}, to get kl(λ) colored partitions λ, which are referred
as the colored partitions arising from λ. On the other hand, all these kl(λ)
colored partitions become to the partition λ by erasing their colors.
=
P If λ
(i)
(i)
(λ ) is a colored partition, we define the weighted length η(λ) as i il(λ ).
We also call λ the type of the conjugacy class. It is known that two
elements are conjugate in Ck ≀ Sn if and only if they have the same type.


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

5

A hook is a special partition of the form (a, 1b ), where a − 1 is the length
of its arm and b is the length of its leg. The hook length is defined as a + b.
For a general partition λ, its hook length at x = (i, j) ∈ λ, of the Young
diagram, is defined by
h(x) = λi + λ′j − i − j + 1,
and the hook length of λ is defined as the product of h(x) for x ∈ λ, where
λ′ is the conjugate of λ.
Example 2.1. In C3 ≀ S7 ,
x = ((1, 1, 1, ω 1 , ω 1 , ω 2 , 1); (1, 2, 3)(4, 5)(6, 7));
y = ((1, ω 2 , ω 1 , 1, 1, 1, ω 1 ); (1, 4, 5)(2, 6)(3, 7))
are conjuagate, since they have the same type ((3), (φ), (2, 2)).
Irreducible characters of the generalized symmetric group Ck ≀ Sn were
determined by Specht [22]. Frenkel, Wang, and the second author have given
a vertex algebraic method to express the irreducible character values by
matrix coefficients of certain vertex operators [5], which we now recall in
the following.
Let {an (γi )|n ∈ Z, i ∈ I} ∪ {c} be the set of generators of the Heisenberg
algebra H with defining relations
[an (γi ), am (γj )] = nδn,−m δi,j c,

(2.2)

[an (γi ), c] = 0.

(2.3)

Consider the Fock space V = Sym(a−n (γi )′ s), the polynomial algebra on
the variables a−n (γi ),n ∈ N and i ∈ I. The algebra H acts on V by the
following rule:
a−n (γi ).v = a−n (γi )v,

(2.4)

c.v = v,

(2.5)

an (γi ).a−n1 (α1 )a−n2 (α2 ) · · · a−nk (αk )
=

k
X

δn,nj hγi , αj ia−n1 (α1 )a−n2 (α2 ) · · · a−nk (αk )

(2.6)

j=1

where αj ∈ R(Ck ), hγi , γj i = δi,j and hγi , αj i is extended the whole space
by linearity.
For convenience, we denote an (γi ) := ain , where the first index i stands
for γi . The space V is equipped with a bilinear form given by
h1, 1i = 1,

a∗in = a−in ,

(2.7)

where a∗in denotes the adjoint of ain . We denote by Ai (z) and A∗i (z) the

generating series:

Ai (z) =

X

n∈N

a−in z n ,

A∗i (z) =

X

n∈N

ain z −n .

(2.8)


6

HUIMIN GAO AND NAIHUAN JING

Moreover, for a partition λ = (λ1 , λ2 , · · · λl ), we define
a−iλ = a−iλ1 a−iλ2 · · · a−iλl ,

(2.9)

which form an orthogonal basis:
ha−iλ , a−jµ i = δi,j δλµ zλ ,

Q

(2.10)

where zλ = i imi mi ! for (1m1 2m2 · · · ), the exponential notation of λ.
In fact, H has another set of generators consisting of the Fourier transform
of the first set: {e
ain |n ∈ Z, i ∈ I} ∪ {c}, where
e
ain =

k−1
X

ω −ij ajn .

(2.11)

j=0

Under the inverse Fourier transform, we have that
k−1

ain =
