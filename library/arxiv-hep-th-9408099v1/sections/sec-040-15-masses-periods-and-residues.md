---
doc_id: arxiv-hep-th-9408099v1
doc_title: "E. Witten Institute for Advanced Study"
section_id: sec-040-15-masses-periods-and-residues
section_title: "Masses, periods and residues"
section_number: 15
pages: 52-54
source_pdf: 9408099v1.pdf
source_sha256: b534faddd2e3aa71
doc_brief: "Seiberg–Witten, Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD (1994) — exact metric on the moduli space of quantum vacua and exact stable-state spectrum for SU(2) with…"
---
As in [9], the particle masses and the low energy metric and co uplings are now de-
termined by equating a and aD with periods of a certain meromorphic one-form λ on the
curveE. λ has two characteristics: (i) λ may have poles but (as long as the monodromies
are in SL(2, Z)) its residues vanish; (ii) to achieve positivity of the met ric on the quantum
moduli space, its derivative with respect to u is proportional to dx
y .
Condition (i) means that the deﬁnition of a and aD by contour integrals
a =
∫
γ1
λ
aD =
∫
γ2
λ,
(15.1)
– with γ1 andγ2 some contours on E – is invariant under deformation of the γi, even across
poles of λ. This ensures that only the homology classes of the γi matter and reduces the
monodromies to a group SL(2, Z) that acts on H1(E, Z). In the presence of bare masses,
this is too strong a condition since (as we saw originally in t he discussion of N = 2 QED in
section 2.4) when the bare masses are non-zero the monodromi es are not quite in SL(2, Z).
As for condition (ii), the diﬀerential form dx
y has no poles and represents a cohomology
class on E of type (1, 0). Having dλ/du =f (u)dx/y leads to positivity of the metric as we
explained in [9]. The function f (u) is determined by requiring the right behavior at the
51
singularities , for instance a ≈ 1
2
√
2u for large u. f is a constant for the same reasons as
in [9]. The proper relation is in fact
dλ
du =
√
2
8π
dx
y . (15.2)
Up to an inessential sign, this is 1 /2 the value in the “old” conventions. By integration
with respect to u, (15.2) determines λ (once the curve is known) for all values of Nf . (15.2)
is only supposed to hold up to a total diﬀerential in x; λ is supposed to be meromorphic
in x.
But when one obtains λ by integration of (15.2), does one get a result that obeys
condition (i)? As an example, 6 consider the massive Nf = 2 theory with y2 = (x2 −
1
64 Λ 24)(x −u) + 1
4m1m2Λ 22x − 1
64 (m12 +m22)Λ 24. In this case, a meromorphic λ obeying
(15.2) can be found by inspection:
λ = −
√
2
4π
dx y
x2 − 1
64 Λ 24. (15.3)
Note that λ has poles at x = ± 1
8 Λ 22 whose residues are 7
±m1 ±m2
(2πi)2
√
2
. (15.4)
Thus, condition (i), as we have stated it so far, holds only wh en the bare masses are zero.
More generally, when the bare masses are not zero, the residu es of λ mean that the
deﬁnition of a andaD in (15.1) is not invariant under deforming the contours γi across the
poles of λ. Under such a deformation, a andaD would change by a constant – the residue
of the pole.
It follows that the monodromies are no longer simply in SL(2, Z). In deﬁning a and
aD, one tries to take a smoothly varying family of contours that keeps away from the poles
6 We consider this example because the theories with Nf ≥ 3 require considerably more pow-
erful methods - developed in the last section of this paper - t o analyze condition (i). On the other
hand, once the conditions are imposed for Nf = 2, there is no need to consider Nf < 2 separately
since the correct behavior for those cases follows from Nf = 2 by the renormalization group ﬂow.
7 Note that the residues are independent of u. The reason for this is that ω = dλ/du has zero
residues. The operation of taking the residue in x commutes with diﬀerentiation with respect to
u, so the fact that ω has zero residues means that the residues of λ are annihilated by d/du .
52
of λ. However, in looping around a closed path in the u plane, the contour might come
back on the wrong side of a pole. When this happens, in additio n to the SL(2, Z) action,
a and/or aD will jump by a constant.
But from our analysis in sections 2 and 6, we know that precise ly such constants are
needed when the bare masses m are not zero. In fact, according to equation (6.2), the
constant jump should be of the form ∑
imiSi/
√
