---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK"
section_id: sec-002-21-irreducible-representations-of-w-and-h
section_title: "Irreducible representations of W and H"
section_number: 2.1
pages: 2-4
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl gr oup W , deﬁned over a ground ring in which “bad” primes for W are"
---
W ; see, for example, [14, 6.3.8]. We will write
Irr(W ) = {Eλ | λ ∈ Λ }, d λ = dim Eλ,
for the set of irreducible representations of W (up to equivalence), where Λ is some ﬁnite
indexing set.
HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR 3
Now let K be the ﬁeld of fractions of A. By extension of scalars, we obtain a K-algebra
HK = K ⊗A H. This algebra is known to be split semisimple; see [14, 9.3.5]. (Note the fo rm
of the quadratic relations for Ts, s ∈ S.) Furthermore, by Tits’ Deformation Theorem, the
irreducible representations of HK (up to isomorphism) are in bijection with the irreducible
representations of W ; see [14, 8.1.7]. Thus, we can write
Irr(HK) = {Eλ
v | λ ∈ Λ }.
The correspondence Eλ ↔ Eλ
v is uniquely determined by the following condition:
trace
(
w, E λ)
= trace
(
Tw, E λ
v
) ⏐
⏐
⏐
v=1
for all w ∈ W ;
note that trace
(
Tw, E λ
v
)
∈ A for all w ∈ W . See also [25, 20.2, 20.3] for a discussion of the
above correspondence, but note that this relies on the validity of L usztig’s conjectures (see
§2.4 below).
2.2. The integers a λ and fλ. The algebra H is symmetric, where {Tw | w ∈ W } and
{Tw−1 | w ∈ W } form a pair of dual bases. Hence we have the following orthogonality
relations for the irreducible representations of HK:
∑
w∈W
trace
(
Tw, E λ
v
)
trace
(
Tw−1, E µ
v
)
=
{ dλ cλ if λ = µ,
0 if λ ⁄= µ;
see [14, 8.1.7]. Here, 0 ⁄= cλ ∈ Z[v, v −1] and, following Lusztig, we can write
cλ = fλ v−2aλ + combination of strictly higher powers of v,
where aλ, f λ are integers such that aλ /greaterorequalslant0 and fλ > 0; see [14, 9.4.7]. Thus, using H, we
have associated with each Eλ ∈ Irr(W ) two integers aλ and fλ. These integers are explicitly
known for all types of W ; see Lusztig [25, Chap. 22].
Now let p be a prime number. We say that p is L-bad for W if p divides fλ for some
λ ∈ Λ. Otherwise, p is called L-good. If L is a positive multiple of the length function, this
corresponds to the familiar deﬁnition of “bad” primes; see Lusztig [ 23, Chap. 4]. Recall that,
in this case, the conditions for being good the various irreducible typ es of W are as follows:
An : no condition ,
Bn, C n, D n : p ⁄= 2,
G2, F 4, E 6, E 7 : p ⁄= 2, 3,
E8 : p ⁄= 2, 3, 5.
See [11, Example 4.7] and [13, Def. 2.3] for a description of the L-bad primes when L is not
constant on S.
4 MEINOLF GECK
