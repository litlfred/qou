---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-015-bound-states-on-the-lattice
section_title: "Bound states on the lattice"
section_number: null
pages: 30-32
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
The identiﬁcation of bound states in the energy spectrum of a lattice calculation is quite important for
the determination of deuteron, triton and helium properties as well as any other description of nuclei in
the framework of NLEFT. Instead of neglecting ﬁnite-volume eﬀects by using a box with large enough
volume, one could also use these eﬀects to extrapolate to the inﬁnite volume. Therefore, it is necessary to
know the ﬁnite-volume behaviour of the bound state.
Firstly, we rederive Lüscher’s ﬁnite volume formula for non-relativistic two-body bound states [84].
The original approach takes into account only spinless pointlike particles for angular momentum l = 0.
24
3.3 Bound states on the lattice
Initial point is the inﬁnite volume solution for a local and ﬁnite-range potential,
V (⃗r) = 0 ∀
⏐⏐⏐⃗r
⏐⏐⏐> R, (3.8)
with R being the range of the potential. Then the Schrödinger equation with bound state solution EB > 0
is [ 1
2µ∆r + V (⃗r)]
ΨB
(⃗r) =−EBΨB
(⃗r), (3.9)
where ΨB is the inﬁnite-volume bound state solution for S wave scattering. In the asymptotic region with
vanishing potential, the solution is given by Eq. (2.36) for l = 0 but with imaginary momentum leading
to the solution,
ΨB
(⃗r) = Aκ√
4π
exp (−κr)
r , (3.10)
with r =|⃗r|. The respective binding momentum isκ =
√
2µEB andAκ is the normalization constant. In
the ﬁnite volume the situation is diﬀerent as it is generally only deﬁned in a box of size L× L× L with
periodic boundary conditions. This condition is used to extend the box to the whole space,
VL
(⃗r) =
∑
⃗n
V (⃗r +⃗nL). (3.11)
Correspondingly, the ﬁnite volume is periodically extended to the inﬁnite volume and the new Schrödinger
equation reads
HLΨ = (Hkin + VL
) Ψ. (3.12)
We can deﬁne a periodic wave function using the inﬁnte volume solution ΨB,
Ψ0
(⃗z) =
∑
⃗n∈Z
ΨB
(|⃗z +⃗nL|), ⃗z =⃗x−⃗y. (3.13)
Now the new wave function almost fulﬁlls the respective Schrödinger equation up to a correction term,
HLΨ0 =−EBΨ0 +
∑
⃗n,⃗n′
V (⃗z +⃗nL) ΨB
(
|⃗z +⃗n′L|
)
. (3.14)
Requiring that the box is large enough such that the asymptotic wave function is applicable at the edge
of the ﬁnite box, the correction term is suppressed by O[exp(−κL)] due to Eq. (3.10). Hence, we can
assume that Ψ≈ Ψ0 as corrections are negligible once the volume is chosen large enough. Finally, the
binding energy correction can be calculated by
∆EB = EB− EL =−
(⟨ΨB
⏐⏐⏐ H
⏐⏐⏐ΨB
⟩−⟨Ψ| HL|Ψ⟩
)
= EB− ⟨Ψ0
⏐⏐⏐ H
⏐⏐⏐Ψ0
⟩
=
∑
⃗n,⃗n′
∫
d⃗z ΨB
(|⃗z +⃗nL|) V (⃗z +⃗nL) ΨB
(
|⃗z +⃗n′L|
)
=−24π|A|2 exp (−κL)
mL +O
[
exp
(
−
√
2κL
)]
. (3.15)
Clearly, mostly S wave bound states emerge in nuclear physics, butP wave bound states can be created
in atomic physics as well. Hence, a generalization of the bound state energy shift formula may be useful
25
Chapter 3 Nuclear Lattice E ﬀective Field Theory
and it was derived in [85, 86].
As the computational power arises, three-body ﬁnite-volume eﬀects are now an actual ﬁeld of research.
Certainly, this is far more diﬃcult than the two-body problem as the most general three-body bound state
is in between a 2+1 state, where a very deeply bound dimer exists and a shallow 1 +1+1 bound state,
which is restricted to the unitary limit case. Finite-volume formulas and discussions can be found in
[87–92]. The explicit formula will be given in the respective chapter.
