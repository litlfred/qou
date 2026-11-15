---
doc_id: arxiv-math-9807106v2
doc_title: "An Extension of the Character Ring of sl(3) and Its Quantisation P. Furlan∗,†"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 9807106v2.pdf
source_sha256: e3cd089e3df5d71f
toc_source: inferred
doc_brief: "An Extension of the Character Ring of sl(3) and Its Quantisation P. Furlan∗,† — We construct a commutative ring with identity which extends the ring of characters of ﬁnite dimensional representations"
---
The aim of this work is to describe the characters (one-dimensional representations)
of the fusion algebra of g = bsl(n)k WZW conformal models at rational (shifted) level
κ := k + n = p′/p , for n = 3 = p′ , (p, 3) = 1 and their ‘classical’ counterparts.
In [9] we have realised this fusion algebra as a matrix algebra F ⊂Matp2(C) with
integer nonnegative structure constants (p)N z
y,x and a basis {Ny , (Ny)z
x = (p)N z
y,x , N1 =
1p2} . The labels of the basis run over the highest weights of the admissible representations
at κ = 3/p [12], which conveniently are parametrised by a subset W(+)
p
of the aﬃne Weyl
group W, see the text for precise deﬁnitions. F is a matrix realisation of a commutative,
associative algebra with identity, a distinguished basis, and an involution ∗. The deﬁnition
of the fusion algebra – an example of C-algebra (Character - algebra) in the terminology of
[2], implies that Ny are normal, hence simultaneously diagonalisable by a unitary matrix
ψ(µ)
y
labelled by some set Ep = {µ} of p2 indices,
(p)N z
x,y =
X
µ∈Ep
ψ(µ)
x
ψ(µ)
1
ψ(µ)
y
ψ(µ) ∗
z
=
X
µ∈Ep
χ(p)
x (µ)
χ(p)
y (µ) χ(p)
z∗(µ)
P
u∈W(+)
p
|χ(p)
u (µ)|2 .
(1.1)
The eigenvalues χ(p)
x (µ) = ψ(µ)
x /ψ(µ)
1
of Nx provide p2 linear representations Ny →χ(p)
y (µ) ,
i.e., characters of F, labelled by the set Ep,
χ(p)
x (µ) χ(p)
y (µ) =
X
z∈W(+)
p
(p)N z
x,y χ(p)
z (µ) .
(1.2)
With an appropriate reinterpretation of the labels this is the general setting for any
RCFT. In particular for WZW models based on the bsl(n)k integrable representations (a
subclass of the admissible representations at integer level k = p′ −n), both indices of the
unitary matrix ψ(µ)
λ
belong to the alcove P k
+ , ψ(µ)
λ
is a symmetric matrix which coincides
with the modular matrix, ψ(µ)
λ
= S(p′)
λµ , while (1.1) reduces to the Verlinde formula [15]
for the fusion rule (FR) multiplicities, i.e., the dimensions of the spaces of chiral vertex
operators.
In [9] we have speciﬁed the above general setting to the case of the generic subseries
κ = 3/p of the admissible representations, describing explicitly one of the fusion matrices,
a ‘fundamental’ fusion matrix Nf. Here f is some analog of the g = sl(3) fundamental
weight ¯Λ1 = (1, 0), but the product of Nf with any Nx produces generically seven terms,
each appearing with multiplicity one. The numbers (p)N z
f,y = 0, 1 were found by solving
2
a set of algebraic equations coming from the decoupling of singular vectors in g = bsl(3)k
Verma modules. More precisely the decoupling of the ‘horizontal’ singular vectors (which
exist also for generic values of the level, κ̸ ∈Q) determines the generic seven points, while
the additional truncation conditions, including the ones at rational level, were obtained
making also some assumptions suggested from explicit computations at small values of
p. Although Nf together with its conjugate Nf ∗are not suﬃcient to build up the full
polynomial fusion ring, diagonalising this matrix in an orthonormal basis, i.e., ﬁnding
the eigenvector matrix ψ(µ)
y
(common to all fusion matrices) recovers through (1.1) all
FR multiplicities. We called (1.1) Pasquier–Verlinde type formula since similar formulæ
– though with diﬀerent interpretation of the structure constants (no more required to be
nonnegative integers), were ﬁrst discussed in [13] in the context of lattice ADE models.
Such formulæ, together with their dual counterparts, describing the structure constants
of a ‘dual’ algebra, have been furthermore exploited in the study of nondiagonal modular
invariants of the integrable WZW conformal models [5], [14].
Diagonalising a p2 × p2 matrix becomes a tedious task for big p (we have done this
exercise for p = 4, 5) so it is preferable to have an explicit analytic formula for ψ(µ)
y , or
equivalently, for the characters χ(p)
y (µ) of the fusion algebra. The path we follow in this
paper to ﬁnd the characters χ(p)
y (µ) was suggested by the second formula for the admissible
FR multiplicities conjectured (with slightly changed notation) in [9],
(p)N z
x,y :=
X
w′∈W [z]
det(w′) mx
w′ z y−1 .
(1.3)
This formula is analogous to the formula for the integrable FR multiplicities derived in
[11],[16], [8], which is a truncated version of the classical Weyl–Steinberg formula for the
tensor product multiplicities of ﬁnite dimensional representations of the horizontal subal-
gebra g (with the role of the horizontal Weyl group W taken by the aﬃne Weyl group W).
In (1.3) the summation runs over the Kac–Wakimoto (KW) aﬃne group W [z], generated
by Kac–Kazhdan reﬂections corresponding to singular vectors of the g Verma module of
highest weight parametrised by the element z ∈W. In the integrable case the counterpart
of mx
v is the multiplicity mλ
µ of the weight µ of the g ﬁnite dimensional module of highest
weight λ. Here the integers mx
v , x, v ∈W describe a generalised (ﬁnite) weight diagram.
The realisation that one has to generalise the classical notion of weight diagram in order
to describe the rational level FR was the main lesson of the, otherwise still incomplete,
analysis of the null-decoupling equations of [9]. While the g weight diagrams are subsets
3
of the root lattice Q of g, attached to the highest weight λ, in our case the role of a ‘root
lattice’ is taken by the aﬃne Weyl group W = W ⋉tQ at a generic (κ̸ ∈Q) level. Now
the question is, can one ﬁnd formal characters encoding this information about the gener-
alised weight diagrams, which furthermore are closed under multiplication and recover a
‘classical’ analogue of (1.3) at generic levels, with the aﬃne KW groups replaced by their
horizontal counterparts W
[z]. Then by analogy with the integrable case one can ‘quantise’
these ‘classical’ characters imposing the periodicity conditions, accounting for the rational
level, and thus recover the linear representations of F.
Though it is not necessary, to understand our way of reasoning and the motivating
idea it is helpful to imagine that there is a ﬁnite dimensional algebraic object playing the
role of g. The irreps of the assumed hidden algebra are labelled in general by x ∈˜
W(+),
a fundamental subset of the extended aﬃne Weyl group ˜W = W ⋉tP with respect to
the right action of W (equivalent to the action of the horizontal KW Weyl group, see [12]
and the text below). The same set also parametrises maximally reducible Verma modules
of g at generic level and the corresponding irreducible quotients. In the simplest bsl(2)k
case solved in [1], [6] this intrinsic algebra is the Z2 graded algebra osp(1|2) [7]; the Weyl
group W ≃Z2 of sl(2) distinguishes between even and odd vacuum state ﬁnite dimensional
irreps of osp(1|2). Alternatively mapping ι : ˜W →Q one can use the horizontal subalgebra
g = sl(2) itself, but restricting to its representations with highest weights on the root lattice
Q (integer isospins). In general this map ι (see section 2) allows to describe the generalised
modules through subsets of the supports of standard modules of g (with highest weights
of n-ality zero); the case sl(2) is trivial since then Im(ι) ≡Q.
The construction of the ‘classical characters’ at generic level, k̸ ∈Q, takes a consid-
erable part of this work and is its main novel result. It is done in the ﬁrst part of the
paper (sections 2,3,4) by full analogy with the standard case starting with some analogs of
the Verma module characters, used as ingredients in a generalised Weyl character formula.
While the input about the relevant generalised supports of the ﬁnite or inﬁnite ‘mod-
ules’ (the set of weights and their multiplicities) is essentially taken over from [9], slightly
rephrased and generalised, the main eﬀort here is to ﬁnd the proper multiplicative struc-
ture of the formal characters. They are elements of the group ring Z[ ˜
W] of the extended
aﬃne Weyl group of bsl(3)k, closed under multiplication. The structure constants of the
resulting commutative subring ˜W of Z[ ˜W] satisfy a generalised Weyl-Steinberg formula.
As a side result one obtains an explicit formula for the cardinality of the generalised weight
4
diagrams, i.e., for the dimensions of the ‘ﬁnite dimensional modules’ of the unknown alge-
bra possibly generalising osp(1|2). Some steps of the construction in this ﬁrst part hold,
or are straightforwardly generalisable, for g = bsl(n)k , arbitrary n. So we keep the expo-
sition general although we present the details fully for the case g = bsl(3)k; the general
case will be elaborated elsewhere. In the second part (sections 5,6,7) we consider rational
values κ = 3/p, thus a generic subseries of the admissible representations of g = bsl(3)k.
The formal characters are ‘quantised’ imposing periodicity constraints and realised as C
- valued functions. They satisfy the orthogonality and completeness relations equivalent
to the unitarity of ψ(µ)
y , so that one recovers the Pasquier–Verlinde type formula (1.1).
Thus given the characters both formulæ for the FR multiplicities of the admissible repre-
sentations (1.1) and (1.3) derive from the classical analog of the Weyl–Steinberg formula
established in the ﬁrst part of the paper. Furthermore one proves a third formula for the
FR multiplicities, conjectured in [9], which also has a ‘classical’ counterpart,
(p)N z
x,y = (3p) ¯N ι(z)
ι(x) ι(y) ,
(1.4)
where (3p) ¯N ι(z)
ι(x) ι(y) are structure constants of the integrable fusion algebra at κ = 3p, while
ι is the map sending ˜W to a subset of the triality zero weights. Presumably the fusion
rules of bsl(n) WZW at κ = n/p are given by the above formula with n substituting 3.
