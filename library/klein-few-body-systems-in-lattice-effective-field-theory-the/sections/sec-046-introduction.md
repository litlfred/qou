---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-Body Systems in Lattice Effective Field Theory"
section_id: sec-046-introduction
section_title: "Introduction"
section_number: null
pages: 75-76
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
toc_source: outline
doc_brief: "Few-Body Systems in Lattice Effective Field Theory — 62 sections: Front matter; Introduction and Motivation; The standard model of particle phy"
---
Lattice simulations based on the framework of eﬀective ﬁeld theory (EFT) have been used in the study
of nuclear forces [116, 138], nuclear structure [34, 35, 108, 129, 139, 140], as well as scattering and
reactions [36, 133, 141]. It has also been applied to few-body [142, 143] and many-body [144–150]
problems in ultracold atomic systems. One of the challenges common to all of these lattice calculations
is the need to eliminate errors caused by the non-vanishing lattice spacing a. Lattice spacing errors or
artifacts can grow in importance as the number of particles increases. This is especially true in cases
where the particles form compact bound states. The problem of lattice errors in computing compact bound
states has been studied in two-dimensional droplets of bosons with attractive zero range interactions
[128]. In Chap. 5 lattice spacing errors were studied in light nuclei to understand deviations from a
universal relation between the triton and alpha-particle binding energies called the Tjon line [24, 72].
One practical approach to reducing lattice artifacts is to introduce a continuous-space regulator
that renders the particle interactions ultraviolet ﬁnite. In that case one can take the lattice spacing
to zero smoothly without any need to renormalize operator coeﬃcients, see [38] and Chap. 4. This
process does not remove errors produced by the continuous-space regulator, but it has the advantage
of eliminating unphysical lattice artifacts such as rotational symmetry breaking. Another approach to
removing lattice artifacts is accelerating the convergence to the continuum limit by including irrelevant
higher-dimensional operators into the lattice action. This general technique is called lattice improvement
and was ﬁrst introduced by Symanzik [3, 4]. The key idea is to write the lattice action as
S (a) = S 0 + f1(a) · S 1 + f2(a) · S 2 + · · ·
(6.1)
where the coeﬃcient functions fi(a) vanish in the continuum limit a →∞and are tuned to cancel the
dependence of the lattice Green’s functions on the lattice spacing, a, at momentum scales well below the
lattice cutoﬀmomentum, π/a. The coeﬃcient functions are ordered so that fi(a) vanishes more rapidly
in the limit a →0 with increasing i.
Symanzik’s improvement program has been widely used in lattice quantum chromodynamics [151–
154]. The improvement program has also been implemented to varying degrees in lattice eﬀective ﬁeld
theory calculations. However, a systematic study of the size of lattice errors arising in systems with
⋆The following chapter has been prepared for publication [137].
69
Chapter 6 Lattice Improvement in Lattice Eﬀective Field Theory
increasing numbers of particles has not yet been performed. In this chapter we address this problem
and benchmark the eﬀectiveness of the lattice improvement program in removing lattice errors for a
one-dimensional system of bosons with zero-range interactions [62]. By building the improved lattice
action step by step, we show that the lattice errors go from O(a1) at leading order (LO), to O(a3) at
next-to-leading order (NLO), and then to O(a4) at next-to-next-to-leading order (N2LO). Our discussion
is organized as follows. In Sec. 6.2 we introduce the one-dimensional boson system in the continuum,
and in Sec. 6.3 we present the lattice implementation. We show and discuss our results in Sec. 6.4 and
then summarize and give an outlook for future applications in Sec. 6.5.
