---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-003-22-preservers-of-polynomials-with-zeros-in-a-clo
section_title: "Preservers of Polynomials with Zeros in a Closed Circular Domain or Its Boundary"
section_number: 2.2
pages: 7-9
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — W e characterize all linear operators on ﬁnite or inﬁnite-di mensio- nal polynomial spaces that preserve the property of having"
---
or Its Boundary. Recall that a M¨ obius transformation is a bijective conformal
map of the extended complex plane, i.e., a map Φ : C ∪ {∞} → C ∪ {∞} given by
Φ( z) = az + b
cz + d , a, b, c, d ∈ C, ad − bc ⁄= 0. (2.2)
The inverse of Φ is then given by
Φ −1(z) = dz − b
−cz + a .
Deﬁnition 4. Let H = {z ∈ C : Im(z) > 0} and H = {z ∈ C : Im(z) ≥ 0}. An
open circular domain is the image of H under a M¨ obius transformation, i.e., an
open disk, the (open) complement of a closed disk or an open aﬃne ha lf-plane. A
closed circular domain is the image of H under a M¨ obius transformation, that is, a
closed disk, the (closed) complement of an open disk or a closed aﬃne half-plane.
For technical reasons we will henceforth assume the following:
If C is a half-plane then the corresponding M¨ obius transformat ion
Φ : C → H is a translation composed with a rotation, i.e., c = 0 in (2.2). (2.3)
Let us also extend Deﬁnition 1 to arbitrary sets Ω ⊆ C.
Deﬁnition 5. A polynomial f ∈ C[z1, . . . , zn] is called Ω- stable if f (ζ1, . . . , ζn) ⁄= 0
whenever ζj ∈ Ω for all 1 ≤ j ≤ n.
Remark 2. Note that an H-stable polynomial is precisely a stable polynomial in
the sense of Deﬁnition 1.
A fundamental discrepancy between πn(C1) and πn(C2), where C1 is closed and
unbounded and C2 is closed and bounded, is that πn(C1) \ πn−1(C1) is dense in
πn(C1) while πn(C2) \ πn−1(C2) is not dense in πn(C2) since constant non-zero
polynomials do not belong to πn(C2) \ πn−1(C2). In order for a linear transforma-
tion T : Cn[z] → C[z] to map πn(C1) ∪ {0} into π(C1) ∪ {0} it is therefore enough
(by Hurwitz’ theorem) for T to map πn(C1) \ πn−1(C1) into π(C1) ∪ {0}. However,
this is not the case for C2. Indeed, take for instance C2 to be the closed unit disk
and let Tn : Cn[z] → Cn−1[z] be deﬁned by
T (zk) = ( n − k)zk + kz k−1, 0 ≤ k ≤ n.
An application of Theorem 7 below shows that T : πn(C2)\πn−1(C2) → π(C2)∪{0}
but T (zn−1) = zn−2(z +n−1), which does not belong to π(C2) for n ≥ 3. Therefore
we need to solve a more general version of Problem 2, namely Problem 3 in §1. This
is done in the next two theorems for all closed circular domains and th eir boundaries.
Notation 4. Given Ω ⊆ C we denote its complement C \ Ω by Ω ′, its boundary
Ω \ ˚Ω by ∂Ω, and we let Ω r be the interior of the complement of Ω, that is, Ω r = ˚Ω ′.
Theorem 7. Let n ∈ N and T : Cn[z] → C[z] be a linear operator. Let further C be
an open circular domain given by C = Φ −1(H), where Φ is a M¨ obius transformation
as in (2.2). Then T : πn(C′) \ πn−1(C′) → π(C′) ∪ {0} if and only if either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ Cn[z],
where α : Cn[z] → C is a linear functional and P ∈ π(C′), or
8 J. BORCEA AND P. BR ¨AND ´EN
(b) The polynomial
T
[(
(az + b)(cw + d) + (aw + b)(cz + d)
) n]
is C-stable.
Remark 3. In the case when C′ is the closed unit disk then for
Φ( z) = (i/2)(z + i)
z − i (2.4)
the polynomial in (b) of Theorem 7 reduces to inT [(1 + zw)n].
Notation 5. Given a M¨ obius transformation Φ as in (2.2) and n ∈ N we deﬁne an
invertible linear transformation φn : Cn[z] → Cn[z] by φn(f )(z) = ( cz +d)nf (Φ( z)).
Theorem 8. Let n ∈ N and T : Cn[z] → C[z] be a linear operator and let further
C = Φ −1(H) be an unbounded open circular domain, where Φ is a M¨ obius trans-
formation as in (2.2). Then T : πn(∂C ) \ πn−1(∂C ) → π(∂C ) ∪ {0} if and only if
either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ Cn[z],
where α : Cn[z] → C is a linear functional and P ∈ π(∂C ), or
(b) T has range of dimension two and the linear operator given by S = φ−1
m T φn
is a stability preserver as in (b) of Theorem 3, where m = max{deg T (f ) :
f ∈ Cn[z]}, or
(c) The polynomial
T
[(
(az + b)(cw + d) + (aw + b)(cz + d)
) n]
is both C-stable and Cr-stable, or
(d) The polynomial
T
[(
(az + b)(cw + d) − (aw + b)(cz + d)
) n]
is both C-stable and Cr-stable.
Remark 4. If ∂C is the unit circle then for Φ as in (2.4) the polynomials in (c) and
(d) of Theorem 8 simply become inT [(1 + zw)n] and T [(z − w)n], respectively.
For the sake of completeness we also formulate analogs of Corollarie s 1 and 2
providing algebraic characterizations in the case of closed circular d omains and
their boundaries.
Corollary 3 (Algebraic Characterization: Closed Circular Domain Case) . Let T :
C[z] → C[z] be a linear operator and let C ⊂ C be an open circular domain given by
C = Φ −1(H), where Φ is a M¨ obius transformation as in (2.2). Then T : π(C′) →
π(C′) ∪ {0} if and only if either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ C[z],
where α : C[z] → C is a linear functional and P ∈ π(C′), or
(b) For all n ∈ N the polynomial
T
[(
(az + b)(cw + d) + (aw + b)(cz + d)
) n]
is C-stable.
P ´OLYA-SCHUR MASTER THEOREMS 9
Corollary 4 (Algebraic Characterization: Circle and Line Case) . Let T : C[z] →
C[z] be a linear operator and C = Φ −1(H) be an unbounded open circular domain,
where Φ is a M¨ obius transformation as in (2.2). Then T : π(∂C ) → π(∂C ) ∪ {0} if
and only if either
(a) T has range of dimension at most one and is of the form
T (f ) = α(f )P, f ∈ C[z],
where α : C[z] → C is a linear functional and P ∈ π(∂C ), or
(b) T has range of dimension two and for all n ∈ N the linear operator given
by Sn = φ−1
m(n)T φn is a stability preserver as in (b) of Theorem 3, where
m(n) = max {deg T (f ) : f ∈ Cn[z]}, or
(c) For all n ∈ N the polynomial
T
[(
(az + b)(cw + d) + (aw + b)(cz + d)
) n]
is both C-stable and Cr-stable, or
(d) For all n ∈ N the polynomial
T
[(
(az + b)(cw + d) − (aw + b)(cz + d)
) n]
is both C-stable and Cr-stable.
Similarly, we may characterize all linear maps that take polynomials with zeros in
one closed circular domain Ω 1 to polynomials with zeros in another closed circular
domain Ω 2, or the boundary of one circular domain Ω 1 to the boundary of another
circular domain Ω 2. However, this only amounts to composing with linear operators
of the type deﬁned in Notation 5, namely φn : Cn[z] → Cn[z], where φn(f )(z) =
(cz + d)nf (Φ( z)) and Φ is an appropriate M¨ obius transformation of the form (2.2) .
