---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-009-23-koszul-matrix-factorizations
section_title: "Koszul matrix factorizations"
section_number: 2.3
pages: 11-12
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
factorization that is ubiquitous in our work and in the previous work t hat relates matrix factorizations to
knot invariants [26]. We need slightly more general setting than the one from [26] because we work with
equivariant matrix factorizations. We state some simple properties of these factorizations that are used later
in the paper.
SupposeZ is a variety with the action of a group G and F is a G-invariant potential. An object of
the category MF str
B2 (Z,F ) is a free B2-equivariant Z2-graded C[Z]-module M with the odd G-invariant
diﬀerential D such that D2 = F /BD
M . In particular, a free G-equivariant C[Z]-module V with two elements
dl∈V , dr∈V ∗ such that (dl,d r) = F , determines a Koszul matrix factorization K( V ;dl,d r) = ⋀ •V with
the diﬀerential Dv = dl∧v +dr·v for v∈ ⋀ •V . We use a more detailed notation by choosing a basis
θ1,...,θ n∈V and presenting dl anddr in terms of components: dl =a1θ1 +··· anθn,dr =b1θ∗
1 +··· +bnθ∗
n:
(2.3) K( V ;dl,d r) =


a1 b1 θ1
... ... ...
an bn θn


The structure of G-module is described by specifying the action of G on the basis θ1,...,θ n. In some cases
when G-equivariant structure of the module M is clear from the context we omit the last columns from
the notations. We call a matrix presenting Koszul matrix factoriza tion Koszul matrix. For example, if we
change the basis θ1,...,θ n to the basis θ1,...,θ i +cθj,...,θ j,...,θ n the i-th and j-th rows of the Koszul
matrix will change: ñ
ai bi θi
aj bj θj
ô
↦→
ñ
ai +caj bi θi +cθj
aj bj−cbi θj
ô
Suppose a1,...,a n ∈ C[Z] is a regular sequence and F ∈ (a1,...,a n). We can choose bi such that
F = ∑
iaibi and dl and dr are as above: dl =a1θ1 +··· anθn,dr =b1θ∗
1 +··· +bnθ∗
n. In general, there is no
unique choice for bi but all choices lead to homotopy equivalent Koszul matrix factoriza tions (in the non-
equivariant case they would be simply isomorphic). In other words, if b′
i is a another collection of elements
11
such that F = ∑ aib′
i and d′
r = b′
1θ∗
1 +··· +b′
nθ∗
n then Lemma 2.2 implies that the complexes K( V ;dl,d r)
and K(V ;dl,d ′
r) are homotopy equivalent.
Indeed, we need to apply Lemma 2.2 for ( C•,d +
• ) = ( ˜C•, ˜d+
• ) = (Λ •V,d l). The elements ai form a regular
sequence hence Λ •V,d l is homotopic toO = C[Z]/I,I = (a1,...,a n) and we conclude that Hom <0
d+ (C•,C •) =
Hom<0
d+ (O,C •) = 0. Moreover, the diﬀerentials dr and d′
r are homotopies between F ∈ Hom 0
d+(C•,C •)
and 0. Thus there is a homotopy between K( V ;dl,d r) and K( V ;dl,d ′
r) and from now on we use notation
KF (a1,...,a n) for such matrix factorization.
