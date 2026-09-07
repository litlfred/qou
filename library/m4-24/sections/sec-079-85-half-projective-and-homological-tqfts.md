---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-079-85-half-projective-and-homological-tqfts
section_title: "Half-projective and homological TQFT’s"
section_number: 8.5
pages: 126-128
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
In [145] it is shown that, for a restricted set of cobordisms, the Reshetikhin-
Turaev TQFT at a prime p-th root of unity p can be de
ned, at least ab-
stractly, as a functorVp :Cob!Z[p]-mod, meaning the category of freeZ[p]-
modules. Note that there is a well de
ned ring epimorphismZ[p]− Fp[y]=yp−1 ,
which sends p 7! 1+ y and maps integer coecients canonically onto the 
-
nite 
eld Fp = Z=pZ. Thus an endomorphism, which for a choice of basis
of the free Z[p]-modules is given by a matrix with entries in Z[p], will be
represented by the same matrix with reduced coecients now in Fp[y]=yp−1 .
Collecting the coecients for each degree we can thus reexpress such a matrix
as a sum of matrices over Fp multiplied with powers of y, or, more succinctly,
use Mat(Fp[y]=yp−1)=M a t (Fp)[y]=yp−1 . This means that in the ring-reduction
the TQFT assigns to cobordisms a polynomial Vp(M)= Pp−2
j=0 yj V [j]
p (M),
where eachV[j]
p (M) is a matrix over Fp and is well de
ned for given bases.
Recall also the notion of a half-projective TQFT with respect to an element x2
R in the base ring, introduced in [210]. It is de
ned, by perturbing functoriality
intoV(NM)= x(M;N )V(N)V(M), where (M;N )=r a n k
(
H1(NM) !
H0(N\M)

.
Problem 8.12 (T. Kerler) [Cyclotomic integer TQFT’s]
(1) Find explicit/computable bases for theVp(g) as free modules overZ[p].
(2) Show that Vp can be extended to all cobordisms as a half-projective
TQFT with x =(p−1)
p−3
2 2 R =Z[p].
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 499
(3) Determine the structure of the V[j]
p (M) a n di nh o wf a rt h e yh a v el i f t s
fromFp toZ, analogous to the Ohtsuki invariants for closed 3-manifolds.
(4) Find a universal TQFT that combines allVp , at least perturbatively, into
one.
In the case of p = 5 the program for items (1){(3) has been mostly carried
out in [213], for primes p 7 not much is known though. Some explicit bases
have been found for genus g = 1 by Gilmer, but the situation for higher genera
g 3 is unknown. An immediate application of item (2) is that the quantum
order, as introduced in [92], is also an upper bound for the cut-number of a
3-manifold. A closely related statement for (2) would also yield a very di
erent
proof for the fact that the Ohtsuki invariants are of 
nite type. In item (3) the
\lift" must depend on p since the dimensions of the vector spaces do, and must
also involve further quotients that arise since the irreducible TQFT’s over Z
do not match the required dimensions either, but they become reducible when
reduced to Fp . Item (4) is rather vague at this point, indicating for some sort
of in
nite 
ltered space with 
nite graded components.
Any TQFTV :Cob! R-mod implies a sequence of representation V[g] :Γ g!
GLR(V(g)) of the mapping class groups. We say that a TQFT is homological
if each of these representations factors through the quotient Γ g− Sp(2g;Z)
(given by the action on H1(g)), and we say it is strictly homological if each
of the Sp(2g;Z)-representations is algebraic, i.e. either faithful or zero. A par-
ticular example of strictly homological TQFT’s over R =Z are the Lefschetz
componentsV(j) of the Frohman-Nicas TQFT, see [128, 214]. From these we
can generate a larger family Q0 of such TQFT’s by taking all direct sums of
V(j) ’s. For example all the TQFT’s constructed in [110] lie in Q0 .A n e v e n
larger familyQ is found by taking also tensor products and their irreducible
summands.
Problem 8.13 (T. Kerler) [Homological TQFT’s]
(1) Find the irreducible components and ring structure (w.r.t  and⊗)o f
Q .
(2) Determine whether all strictly homological TQFT’s lie in Q .
(3) Identify the homological TQFT’s that arise from the gauge theory of
higher rank groups (such as PSU (n) in [129]) with elements in Q .
(4) Identify the irreducible factors of the constant orders V[0]
p of the cyclo-
tomic integer expansion of the Reshetikhin-Turaev theory with elements
inQ .
Geometry &TopologyMonographs, Volume 4 (2002)
500 T. Ohtsuki (Editor)
The 
rst item is in some sense about 
nding the representation ring of Sp(2;Z)
Sp(4;Z):::  Sp(2g;Z)::: equipped with further generators and relations
given by the standard handle attachments. The constraints given by the latter
may be just good enough to ensure that the answer to item (2) is positive.
The application of (3) is a better understanding and possibly a closed form for
the polynomials from [129] that express the PSU (n)-invariants in terms of the
coecients of the Alexander polynomial. Evidence seems to suggest that the
TQFT’s from (4) stem from p−3
2 -fold symmetric products of elements in Q0 .
A plausible corollary would be that for a closed manifold with b1(M) 1w e
have
Vp(M)=( p−1)
p−3
