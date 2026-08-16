---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-021-introduction
section_title: "Introduction"
section_number: null
pages: 45-46
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
The Nuclear Lattice Eﬀective Field Theory (EFT) method [33] has led to impressive progress in the
last decade and it has been applied to few- and many-body-systems successfully, for reviews see e.g.
Refs. [52, 107]. The lattice spacing serves as a natural UV regulator for the theory, as for a given value
of a the maximal momentum is pmax =π/a. Although these calculations give a quite good description
for the phase shifts, energy levels, etc., almost all calculations have been done for a ﬁxed lattice spacing
a≃ 2 fm, corresponding to a soft momentum cut-o ﬀ of about 300 MeV . This allows one to treat all
corrections beyond leading order (LO) in perturbation theory. However, the cut-o ﬀ dependence or
lattice spacing dependence has not been analyzed systematically and there are still some problems in the
two-nucleon system like the relatively poor description of the 3S1-3D1 mixing angle [61]. Further, such
soft potentials seem to lead to some overbinding in medium-mass nuclei, as discussed in Ref. [108]. Also,
it has been shown that the leading order four-nucleon contact interactions need to be smeared to avoid a
cluster instability when four nucleons reside on one lattice site [32]. One might argue that the extension
of such smearing methods also to the pion exchange contributions leads to a natural regularization of
the lattice EFT, allowing to vary the lattice spacing freely but using an explicit momentum cut-o ﬀ in
the spirit of the work of Ref. [38]. More precisely, this inherent physical cut-oﬀ was implemented by
formulating the lattice action in terms of blocked ﬁelds.
In this chapter, we will focus on the neutron-proton two-body system at lowest order and discuss
the lattice spacing dependence systematically. In addition, we discuss the necessity of regularizing the
one-pion-exchange potential and provide a method that goes beyond smearing and is borrowed from
continuum calculations, which leads to the lattice spacing independence of observables for a broad range
in a, see Ref. [22].
While most of the calculations solve the transfer matrix using Monte Carlo methods or the Lanczos
method for small eigenvalues of large sparse matrices, we use here the Hamiltonian formalism and solve
it with the Lanczos method. Using this approach we can eliminate the discretization in the time direction
and we have to consider only the variation in the position space discretization. In the following, all
expressions are given in lattice units and one has to multiply the lattice results by the appropriate power
of the lattice spacing a to get the physical values. Note also that we show simulations for various large
enough volumes so that Lüscher’s ﬁnite volume formulas are suﬃcient for the inﬁnite volume extraction
⋆ The following chapter has been published in [106].
39
