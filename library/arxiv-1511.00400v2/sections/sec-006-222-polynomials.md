---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-006-222-polynomials
section_title: "Polynomials"
section_number: 2.2.2
pages: 8-10
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Here some properties of twisted Alexander polynomials viewed as tor sions are
brieﬂy discussed, since they are convenient for describing some re sults of Rei-
demeister torsion. See the recent surveys [69, 33] fore more det ails on twisted
Alexander polynomials.
Start with a surjective morphism φ∶ π1K → Z. Instead of a representation
ρ∶ π1K → SLn(F ), consider the twisted representation
ρ ⊗ φ∶ π1K → GLn(F (t))
where F (t) is the ﬁeld of fractions of the polynomial ring F [t].
If H∗(K; ρ) = 0, then H∗(K; ρ ⊗ φ) = 0 [68, 53] and there is a well deﬁned
torsion, or twisted polynomial:
∆ K,ρ,φ(t) = tor(K, ρ, φ) ∈F (t)/slash.l⟩ft ± tn Z.
8
As the determinant is not one, there is an indeterminacy factor tk n, for some
integer k ∈Z.
Remark 2.11. Assume H∗(K; ρ) = 0. Then
∆ K,ρ,φ(1) = tor(K, ρ).
This is proved from the map at the chain level C∗(K; ρ⊗φ) → C∗(K; ρ) induced
by evaluation t = 1.
If ∆ K,ρ,φ = ∑i aiti, then its degree can be deﬁned as:
deg(∆ K,ρ,φ) = max{i − j /divid⟩s.alt0ai, aj ≠0}.
Proposition 2.12. If M 3 is a three-manifold and Σ ⊂M 3 is a surface dual to
φ such that H0(Σ; ρ) = 0, then
deg ∆ M 3,ρ,φ ≤−χ(Σ )n.
This proposition can be proved using Mayer-Vietoris to a tubular neig hbor-
hood of the surface and its exterior.
For a knot K ⊂S3, there is a natural surjection φ∶ π1(S3 − K) → Z. Let AK
denote its Alexander polynomial. In [57] (this reference is based on a preprint
from 1990) Lin deﬁned a twisted Alexander polynomial Aρ
K that lives in F (t),
that was later modiﬁed by Wada [99].
Milnor in 1962 for the untwisted Alexander polynomials, and Kitano in 19 96
for the twisted ones, proved:
Theorem 2.13. For a knot exterior S3 − K, we have:
(a) [67] For the trivial representation:
∆ S3−K,1,φ = tor(S3 − K, φ) = AK(t)
(t − 1) .
(b) [53] For ρ a non-trivial acyclic representation:
∆ S3−K,ρ,φ = tor(S3 − K, ρ ⊗ φ) = Aρ
K(t).
Milnor’s formula, for the untwisted polynomial, has been generalized t o links
and to other three-manifolds in 1986 by Turaev [95]. See also [33, 69].
The following is straightforward from Mayer-Vietoris, Proposition 2 .10:
Proposition 2.14. Let K be a CW complex, f ∶ /divid⟩s.alt0K/divid⟩s.alt0 → /divid⟩s.alt0K/divid⟩s.alt0 a homeomorphism
with mapping torus Mf . Then
∆ Mf ,ρ,φ =
dim K
/product.disp
i=0
det(fi − t Id)(−1)i+1
,
where fi∶ Hi(K; ρ) → Hi(K; ρ) denotes the induced map in homology. In partic-
ular, by Remark 2.11,
tor(Mf , ρ) =
dim K
/product.disp
i=0
det(fi − Id)(−1)i+1
.
9
Another relevant issue for this polynomial is Turaev’s interpretatio n of the
twisted Alexander polynomial: namely this polynomial encodes the tor sion of
the ﬁnite cyclic coverings ([95], see also [25, 83, 89, 85, 109]).
Proposition 2.15. Let K, ρ∶ π1K → SLn(F ), and φ∶ π1K → Z be as above.
Let Km → K be the cyclic covering of order m corresponding to the kernel of φ
composed with the projection Z → Z/slash.l⟩ftmZ. Then
(a) H∗(Km; ρ) = 0 if and only if ∆ M 3,ρ,φ(ζ) ≠0 for every ζ ∈C satisfying
ζm = 1.
(b) If H∗(Km; ρ) = 0 then
tor(Km, ρ) =
m−1
/product.disp
i=0
∆ M 3,ρ,φ(ζi)
for ζ ∈C a primitive m-root of the unity.
