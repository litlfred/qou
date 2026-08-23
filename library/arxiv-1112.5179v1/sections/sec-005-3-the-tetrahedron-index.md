---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-005-3-the-tetrahedron-index
section_title: "The tetrahedron index"
section_number: 3
pages: 16-18
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
The basic building block used to construct the theory TM for any 3-manifoldM is the theory
T∆ associated to a single ideal tetrahedron. More precisely, we should call the theory
T∆,ΠZ, (3.1)
since it depends on a polarization for the boundary of the tetrahedron. As discussed in
Sections 2 and 4 of [19], we make a speciﬁc choice of polarization Π Z (see also Section 3.3
below). Then T∆ consists of a single free N = 2 chiral multiplet φ, coupled to a background
U(1) gauge multiplet with a level − 1
2 Chern-Simons interaction.
In order to calculate the index of T∆, we must specify the R-charge and fermion number
assignments for the theory on S2×S1. We take Rφ = Fφ = 0, and also require that the
vacuum in a ﬂux sector of any negative charge m has Rvac = Fvac = 0. Then, by following
the rules for constructing indices in [15, 17], we ﬁnd
I∆(m;q,ζ )≡I T∆,ΠZ(m;q,ζ ) = (−q
1
2 )
1
2 (m+|m|)ζ− 1
2 (m+|m|)
∞∏
r=0
1−qr+ 1
2|m|+1ζ−1
1−qr+ 1
2|m|ζ
. (3.2)
It turns out that this expression simpliﬁes nicely to
I∆(m;q,ζ ) =
∞∏
r=0
1−qr− 1
2m+1ζ−1
1−qr− 1
2mζ
. (3.3)
The various ingredients in (3.2) can be given an intuitive explanation. The denominator
in the product arises from bosonic creation operators of ﬂavor charge 1 and spin r + |m|
2
acting on the vacuum. The spin starts from |m|
2 due to the nontrivial magnetic ﬂux on S2.
The numerator arises similarly from fermionic creation operators of ﬂavor charge−1 and spin
r +|m|
2 + 1.
In addition to the product, the prefactor ( −q
1
2 )
1
2 (|m|+m)ζ− 1
2 (m+|m|) in (3.2) turns out to
be both subtle and important. It depends on the energy, R-charge, and ﬂavor charge of the
ground state in a non-trivial ﬂux sector, which have been calculated carefully in e.g. [49].
First, the ﬂavor charge of the ﬂux vacuum is aﬀected by the quantization of (anti)fermions
in the chiral multiplet, and receives from that a contribution − 1
2|m|. This is corrected by
the Chern-Simons coupling k =− 1
2 to− 1
2(m +|m|). In order to determine the R-charge
Rvac and fermion number Fvac, we can shift conventions so that Rφ = Fφ = 1 for the free
chiral boson. Then R =F = 0 for the fermion zero-mode whose quantization determines the
quantum numbers of the vacuum, implying Rvac =Fvac = 0. In terms of the index (3.2), we
can easily perform the shift to Rφ = Fφ = 1 by setting ζ→ (−q
1
2 )ζ. Then it is easy to see
that the vacuum acquires Rvac =Fvac = 0 as expected.
It is important to remark a subtle sign diﬀerence between our prescription for the index
of a chiral multiplet and the prescription that can be found in the literature [15, 17]. After
aligning the choices of R-charge and CS terms, the diﬀerence boils down to the prefactor
– 15 –
(−1)
1
2 (|m|+m). This prefactor aﬀects in a minimal way the checks of mirror symmetry that
have already been done in the literature, as it only aﬀects the overall sign of the index in
a given charge sector. However, only with our deﬁnition of the chiral index can such signs
be matched universally via an appropriate shift of F . This deeply aﬀects the calculation of
the index in theories whose superpotentials have monopole operators — which is standard in
classR.
Let us also write the index in an electric-magnetic charge basis, as in Section 2. By using
several standard identities for q-series, we ﬁnd
I∆(m;q,ζ ) =
∑
e∈Z
I∆(m,e ;q)ζe, (3.4)
with
I∆(m,e ;q) =
∞∑
n=⌊e⌋
(−1)nq
1
2n(n+1)−
(
n+ 1
2e
)
m
(q)n (q)n+e
, (3.5)
where⌊e⌋≡ 1
2(|e|−e) and (q)n≡ (1−q)(1−q2)··· (1−qn). The sum in (3.5) can be thought
of as deﬁning a formal power series in q; for ﬁxed charge γ = (m,e ), only ﬁnitely many terms
in the sum are necessary for calculating I∆(m,e ;q) to a desired order in q. The series (3.5)
also appears to converge to a well-deﬁned analytic function of q for|q|< 1.
In anticipation of the interpretation of the tetrahedron index as a geometric invariant of
an ideal tetrahedron ∆ itself (and connections to the classical Bloch group), we can take the
“classical limit” q = eℏ→ 1 and m→∞ with qm ﬁxed. Let us set q
m
2ζ = z, remembering
that ζ is a pure phase, so that z becomes a complex number. Then
I∆(m;q,ζ ) =
∞∏
r=0
1−qr+1z−1
1−qrz−1
ℏ→0∼ exp
(2V∆(z)
iℏ +...
)
, (3.6)
where the function
V∆(z)≡− Im Li2(z−1) (3.7)
is closely related to the hyperbolic volume of a tetrahedron with shape parameter z. In fact,
the actual volume can be written as Vol ∆(z) =V∆(z) + arg(1−z−1) log|z| , cf. [50].
3.1 Parity and ρ symmetry
Several identities satisﬁed by the tetrahedron index can be understood via discrete symmetries
acting on T∆. Let’s ﬁrst consider the action of parity P onT∆. In is not an exact symmetry
because it inverts the sign of the Chern-Simons level, from k =− 1
2 to k = 1
2. However, this
can be compensated for by subtracting a Chern-Simons term, i.e. applying T−1∈ Sp(2, Z).
In the S2×S1 background, it actually turns out that the R-charge and fermion number of
the vacuum must also be shifted, so that altogether we get
T∆ ≃ σR
mσF
mT−1◦ PT∆. (3.8)
– 16 –
Acting on the index, P simply sends m→−m, so (3.8) implies
I∆(m,e ;q) =
(
−q
1
2
)mI∆(−m,e +m;q). (3.9)
This identity can be checked explicitly (see Appendix A), most easily after converting to the
fugacity basis.
The ρ symmetry of Section 2.4 is more universal than parity, but also more subtle to
implement. Naively, it sends I∆(m;q,ζ ) toI∆(−m;q−1,ζ−1); but the latter does not make
sense for|q|< 1. In order to properly apply the symmetry, we need to reorganize the Hilbert
spaceH−m, and to reinterpretI∆(−m;q−1,ζ−1) as a series in q. For the tetrahedron, this is
actually straightforward.
Let us set z =q
m
2ζ, z =q
m
2ζ−1, noting that ρ acts on z by complex conjugation. Then
I∆(−m;q−1,ζ−1) =
∞∏
r=0
1−q−r−1z−1
1−q−rz−1 = exp
( ∞∑
n=1
−q−nz−n +z−n
n(1−q−n)
)
≃ exp
( ∞∑
n=1
−qnz−n +z−n
n(1−qn)
)
(3.10)
=
∞∏
r=0
1−qr+1z−1
1−qrz−1 =I∆(m;q,ζ ).
The necessary reorganization of cancellations happened in the middle step (3.10), and es-
tablished the ρ symmetry. Note that this is not analytic continuation, since neither of the
exponentials here make sense on the unit circle |q| = 1 — the expressions diverge at every
root of unity.
