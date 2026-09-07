---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-002-the-case-of-unitary-codes
section_title: "The case of unitary codes"
section_number: null
pages: 3-5
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
As a particular case we set G = Un(C) × Un(C) and X = Un(C). For g = U × V
and x = M we set gx = U M V−1. In this context the orbit of a pair ( x, y ) is
3
characterized by the eigenvalues ( eiθ1, ..., e iθn ) of the unitary matrix xy−1. The
Peter-Weil theorem gives a decomposition of L2(X) into irreducible subspaces
L2(X) = ⊕(Vχ ⊗ Vχ ) (3)
where the sum runs over all irreducible representations Vχ of Un(C). It is worth
noticing that the G-subspaces Vχ ⊗ Vχ are pairwise non isomorphic. From this
decomposition one can deduce the following theorem :
Proposition 3.1 The zonal functions associated to this decomposition are
Pχ (x, y ) = χ (xy−1)
where χ denotes any irreducible character of Un(C).
The irreducible characters of Un(C) are known to be ﬁnite dimensional and
to have a nice description using Schur polynomials ([16]). We recall brie ﬂy some
notations and deﬁnitions concerning those polynomials.
For any integer k, a partition of k in n parts is a ﬁnite decreasing sequence of
n non negative integers which sum exactly to k (k is also called the degree of the
partition). A partition λ is dominating µ (noted λ ≻ µ ) if ∀r ≤ n, ∑ r
i=1 λ i ≥∑ r
i=1 µ i. Given a partition λ = [λ 1, ..., λ n] we deﬁne the elementary symmetric
polynomials mλ ∈ Z[x1, ..., x n] as the renormalization to a monic polynomial of
∑
σ ∈Sn
xλ 1
σ (1)xλ 2
σ (2)...x λ n
σ (n).
These polynomials form a basis of the set of symmetric polynomials Z[x1, ..., x n]Sym.
Schur polynomials have been intensively studied and have several de ﬁnitions.
For our purpose we will deﬁne the Schur polynomials Sλ as
Sλ =
∑
λ ≻µ
Kλ,µ mµ ,
where the Kλ,µ ∈ N are the so called Kostka numbers. For more precision on
those numbers see [15]. It is clear that Schur polynomials form anoth er basis of
Z[x1, ..., x n]Sym.
It is well known that the irreducible polynomial characters of Un(C) are
expressed using Schur polynomials (we refer to [16] for details) in th e following
way: let ( eiθ1, ..., e iθn ) denote the eigenvalues of a unitary matrix M , and λ a
partition. Then
χ λ (M ) = Sλ (eiθ1 , ..., e iθn ).
One obtains all irreducible characters of Un(C) by multiplying the characters χ λ
by a relative power of det( M ) =∏ eiθk . All together, we obtain the theorem:
Theorem 3.2 For all partition λ and s ∈ Z, let
Pλ,s (x1, . . . , x n) = ( x1 . . . x n)sPλ (x1, . . . , x n). (4)
4
These rational fractions give the zonal functions associat ed to the irreducible
decomposition (3) in the following way: if χ ≃ dets ⊗λ, if the eigenvalues of
xy−1 are (eiθ1, ..., e iθn ), then
Pχ (x, y ) = Pλ,s (eiθ1 , ..., e iθn).
.
We are now almost ready to compute bounds for unitary codes V ⊂ Un(C).
Let
d2
Σ (eiθ1 , ..., e iθn) := 1
2n
n∑
i=1
(1 − cos θi)
and
d2
Π (eiθ1 , ..., e iθn ) := 1
2
( n∏
i=1
(1 − cos θi)
) 1
n
.
and deﬁne d2
Σ (x, y ) (resp. d2
Π (x, y )) to be the above functions evaluated at
the eigenvalues of xy−1. These functions are related to the diversity sum and
diversity product by
Σ V = min
x,y ∈V
x⁄=y
dΣ (x, y ) and Π V = min
x,y ∈V
x⁄=y
dΠ (x, y ).
We recall that the orbit of a pair ( x, y ) is characterized by the eigenvalues of
xy−1, so dΣ and dΠ are constant on G-orbits. We may now deﬁne, with the
notations of Section II, the sets S related to each diversity function:
SΣ (δ) := {(eiθ1, ..., e iθn ) : dΣ (eiθ1, ..., e iθn ) ≥ δ}
SΠ (δ) := {(eiθ1 , ..., e iθn) : dΠ (eiθ1 , ..., e iθn) ≥ δ}.
