---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-008-designs
section_title: "Designs"
section_number: null
pages: 23-27
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
In this section, we introduce the concept of a complex Grassmannian 2-design.
We give lower bounds for the size of a t-design and indicate the relationship
between designs and codes.
Recall that Ht(m, n ) is the direct sum of the irreducible representations Hµ
of U (n) containing the zonal polynomials Zµ,a , where µ is an integer partition
of size at most t and length at most m. Ht(m, n ) may also be thought of as the
symmetric polynomials of degree at most t in the principle angles of pairs of
subspaces in Gm,n . Since the zonal orthogonal polynomials Zµ,a (with |µ | ≤ t
and len( µ ) ≤ m) span Ht(m, n ) and are contained in Hom t(n), it follows that
Ht(m, n ) is a subspace of Hom t(n).
We call a ﬁnite subset S ⊆ G m,n a t-design if, for every polynomial f in
Ht(m, n ),
1
|S|
∑
a∈S
f (a) =
∫
Gm,n
f (c) dc.
In other words, the average of f over S is the same as the average of f over
the entire Grassmannian space. Recall that the average of f over Gm,n can be
written as ⟨1, f ⟩: with this in mind we deﬁne an inner product for functions on
S as follows:
⟨f, g ⟩S := 1
|S|
∑
a∈S
f (a)g(a).
Then S is a t-design if ⟨1, f ⟩ = ⟨1, f ⟩S for every f ∈ Ht(m, n ). Equivalently,
the zonal orthogonal polynomials Zµ,a span Hµ , so S is a t-design if every Zµ,a
has the same averages over S and Gm,n , where µ is a partition of at most t into
at most m parts.
By way of example, consider Theorem 6.4. If f =∑
µ cµ gµ and cµ > 0 for
every |µ | ≤ t, then equality in Theorem 6.4 implies that S is a t-design.
23
For the purposes of quantum tomography applications, 1- and 2-designs
play a special role (see [13], as well as [21]). In those cases , there is a more
explicit description of a t-design.
Lemma 9.1. Let S be a ﬁnite subset of Gm,n . Then S is a 1-design if and only
if 1
|S|
∑
a∈S
Pa =
∫
Gm,n
Pa da = m
n I.
Moreover, S is a 2-design if and only if
1
|S|
∑
a∈S
Pa ⊗ Pa =
∫
Gm,n
Pa ⊗ Pa da. (9.1)
Before proving Lemma 9.1, we note the integral on the RHS of eq uation (9.1)
can be evaluated explicitly. Writing Pa =∑ m
i=1 aia∗
i for some orthonormal basis
{ai} of a, and letting T denote the “swap” operator T : ei ⊗ ej ↦→ej ⊗ ei, the
integral is obtained from Lemma 5.3 of [20]:
∫
Gm,n
Pa ⊗ Pa da = m
n(n2 − 1) [(nm − 1)I + (n − m)T ] .
Proof. We prove the lemma by showing that Ht = Hom t for t ∈ { 1, 2}; the
result then follows by considering the polynomials of the fo rm a ↦→(Pa)ij in
Hom1 and a ↦→(Pa)ij(Pa)kl in Hom 2.
Recall that Ht is contained in Hom t, so it suﬃces to show that the dimen-
sions of the spaces are equal. When t = 1, we have dim(H1) = dim(Hom 1) = n2,
so H1 = Hom 1. When t = 2, recall that dim( H2) =
(n2
2
)
(assuming m > 1),
and the space of homogeneous degree-2 polynomials on the coo rdinates of n × n
matrices has dimension
(n2+1
2
)
. However, Hom 2 is the space of degree-2 polyno-
mials on projection matrices, not general matrices. If Pa is a projection matrix,
then the degree-2 polynomial
Pa ↦→m tr(AP 2
a ) − tr(Pa) tr(APa)
is identically zero for every A. There are n2 linearly independent polynomials
of that form for general n × n matrices; therefore,
dim(Hom2) =
(n2 + 1
2
)
− n2 =
(n2
2
)
.
Thus H2 = Hom 2.
24
We now consider bounds for t-designs. The following is the absolute bound .
Lemma 9.2. If S is a t-design, then
|S| ≥ dim(H⌊t/ 2⌋(m, n )).
Proof. Let {e1, . . . , e N } be an orthonormal basis for H⌊t/ 2⌋. Since ei is a
symmetric polynomial in the eigenvalues, so is eiej. It follows from the unique
decomposition of L2(Gm,n ) that eiej is in H2⌊t/ 2⌋ and therefore in Ht. If S is a
t-design, and eiej is in Ht, then
⟨ei, e j⟩ = ⟨1, eiej⟩ = ⟨1, eiej⟩S = ⟨ei, e j ⟩S ,
whence it follows that {e1, . . . , e l} are orthogonal as functions of S (a space of
dimension |S|).
If equality holds, then the basis for Ht/ 2(m, n ) is also a basis for the functions
on S. There is also a relative bound .
Theorem 9.3. Let f (x1, . . . , x m) ∈ R[x] be a symmetric polynomial such
that f = ∑
µ cµ Zµ , where Zµ is a zonal polynomial for the Grassmanian
space, and c0 > 0. Furthermore, suppose S is a t-design such that fa(b) =
f (y1(a, b ), . . . , y m(a, b )) ≥ 0 for every a ⁄= b in S, and cµ ≤ 0 for every |µ | > t .
Then
|S| ≥ f (1, . . . , 1)
c0
.
Proof. Let fa be the zonal polynomial of f at a, so that fa(b) ≥ 0 for b ⁄= a.
Summing over all b ∈ S,
|S| ⟨1, f a⟩S ≥ fa(a) = f (1, . . . , 1).
Again averaging over all a ∈ S,
f (1, . . . , 1) ≤
∑
a∈S
⟨1, f a⟩S
=
∑
a∈S
∑
µ
cµ ⟨1, Z µ,a ⟩S
=
∑
µ
cµ
∑
a∈S
⟨1, Z µ,a ⟩S .
25
Since S is a t-design, the inner sum is zero for |µ | ≤ t (µ ⁄= 0). For |µ | > t, the
inner sum is nonnegative (by Lemma 5.1) and cµ ≤ 0. Therefore,
f (1) ≤ c0
∑
a∈S
⟨1, Z 0,a ⟩S
= c0|S|.
If equality holds, then we have f (a, b ) = 0 for every a ⁄= b in S. That
is, S is an f -code. Furthermore, for every |µ | > t , we have either cµ = 0 or∑
a∈S Zµ,a = 0.
As with classical codes and designs, the case where S is both a f -code and
a t-design is of particular interest, as the size of the set can b e determined
exactly. Combining Theorems 6.4 and 9.3 gives the following .
Theorem 9.4. Suppose S is an f -code for f =∑
µ cµ Zµ , where cµ ≥ 0, and S
is also a t-design for t ≥ deg(f ). Then
|S| = f (1, 1, . . . , 1)
c0
.
Consider the following polynomial in Ht(m, n ):
Zt :=
∑
|µ |≤t
len(µ )≤m
Zµ .
This polynomial satisﬁes ⟨Zt,a , f ⟩ = f (a) for every f ∈ Ht(m, n ). Taking f = Zt
in Theorem 9.4, we get:
Corollary 9.5. If S is a Zt-code and a 2t-design, then
|S| = dim(Ht(m, n )).
Theorem 9.6. Any two of the following imply the third:
• S is an f -code, where deg(f ) = t;
• S is a 2t-design;
• | S| = dim(Ht(m, n )).
Proof. Suppose S is a f -code with |S| = dim( Ht). Since equality holds in
Corollary 6.3, the polynomials fa are a basis for Ht. However, we have
⟨Zt,a , f b⟩ = fb(a) =
{
0, b ⁄= a;
f (1, 1, . . . , 1), b = a.
26
Thus {Zt,a } is a dual basis for Ht and each Zt,a is a multiple of ft,a . Now
consider the averages ⟨Zt,a , f b⟩S: since fa(b) = Zt,a (b) = 0 for b ⁄= a, we get
⟨Zt,a , f b⟩S =
{
0, b ⁄= a;
f (1, 1, . . . , 1), b = a.
Thus we have
⟨1, Z t,a fb⟩S =
⟨
Zt,a , f b
⟩
S =
⟨
Zt,a , f b
⟩
= ⟨1, Z t,a fb⟩
for the bases {Zt,a } and {fb}. But the set {Zt,a fb} spans H2t(n), so S is a
2t-design.
Conversely, suppose S is a 2t-design with |S| = dim(Ht), and let f annihilate
of the angle set of A. Since Ht spans the functions on |S|, each fa is in Ht and
is therefore a polynomial of degree t. Thus f has degree t.
The simplest case of Theorem 9.6 is when t = 1: in this case, S is a 1-
distance set and a 2-design of size n2. Moreover, S is a Z1-code, and Z1 is
the annihilator of m(mn−1)
n2−1 . Thus the inner product between every two distinct
subspaces is α = m(mn−1)
n2−1 .
