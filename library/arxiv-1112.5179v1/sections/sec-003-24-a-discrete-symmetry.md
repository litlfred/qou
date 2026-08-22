---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-003-24-a-discrete-symmetry
section_title: "A discrete symmetry"
section_number: 2.4
pages: 12-13
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
We could deﬁne standard discrete symmetries C, P , and T acting on theories T and their
indices, though in general the 3d SCFT’s in class R will not be invariant under any of these
“symmetries” alone. To see which discrete symmetries stand a chance at preserving a theory
T and its index, it is useful to consider more closely the Hilbert space Hm ofT on S2 in the
presence of magnetic ﬂux m. Suppose further that T is in classR, and has a UV Lagrangian
description as an abelian Chern-Simons-matter theory with superpotential.
The Hilbert space Hm is graded by charges (E,R,j 3,e ). Since states come in complete
multiplets of theSU (2) Lorentz group, changing the sign ofj3 should preserveHm. We could
also try to ﬂip the sign of the U(1) R-charge R. In a Lagrangian, this is accomplished by
Hermitian conjugation, switching chiral multiplets and antichirals, which has the additional
eﬀect of ﬂipping the ﬂavor chargee→−e. However, this overall charge conjugation still does
not preserve the theory in a magnetic ﬂux background. In order for antiparticles to behave
the same way as the original particles, it is also necessary to replace m→−m.
It appears that the simultaneous reversal of charges
ρ : (E,R,j 3,e,m ) → (E,−R,−j3,−e,−m) (2.23)
is a true symmetry of the graded Hilbert spaces Hm. In fact, there exists a simple geometric
operation that also realizes ρ in the context of the index. If we put the Euclidean version
ofT on S2×S1, with appropriate magnetic ﬂux and global Wilson lines so as to calculate
the index, then ρ corresponds to reﬂecting S2 through its equator (along the j3 axis) and
reversing time. The spatial reﬂection ﬂips m, while the time reversal ﬂipsj3 and eﬀectivelyR
ande. The eﬀective negation ofR ande happens because the fugacities in R-charge and ﬂavor
Wilson lines change sign. Altogether, this reversal of time and space is just the Euclidean
analogue of CPT symmetry.
The outcome is that we would expect the index to be invariant under ρ. Naively, from
(2.3), this means
IT (m;q,ζ )
ρ
= IT (−m;q−1;ζ−1), (2.24a)
or in a charge basis,
IT (m,e ;q)
ρ
= IT (−m,−e;q−1). (2.24b)
– 11 –
However, (2.24) are only true in a formal sense. In order to account for the inﬁnite cancel-
lations between bosons and fermions in Hm, the index should really be deﬁned with a reg-
ulator as in (2.1). Upon applying ρ, the “Hamiltonian” appearing in the regulator changes,
H = E−R−j3→ E +R +j3, so that the boson-fermion cancellations in H−m should be
counted diﬀerently than would be implied by the right-hand sides of (2.24). Therefore, as
written, the equalities (2.24) are not actually correct. This fact is most striking if (say) we
choose a superconformal R-charge assignment; then the indices on the left-hand side are series
in positive powers of q while the indices on the right-hand side are series in q−1. Typically
there is no analytic continuation from one to the other. 8
Making sense of ρ symmetry for indices requires a reorganization of the cancellations in
the spaces Hm, eﬀectively turning the series in q−1 on the right-hand sides of (2.24) into
series inq. One way to implement this reorganization is to separateHm into Fock spaces that
can be “inverted.” For example, the reorganization in the Fock space of a free boson would
correspond to rewriting the generating function of single-particle states as
1
1−q−1→ −q
1−q. (2.25)
This reorganization will be realized in Section 3.1 for the simple tetrahedron theory T∆.
For more complicated theories in class R, the mathematics of plethystic logarithms and
exponentials (cf. [48]) may help to convert indices IT (−m,−e;q−1) to series in q.
Although ρ symmetry only holds formally for the index, it is still powerful enough to
relate algebras of operators on the index (which do not feel the re-organization of Hilbert
spaces). We will see this beginning in Section 2.5 below, and ﬁnd a geometric meaning for
ρ acting in operator algebras in Section 5. In Section 6, we will show that when T is a 3-
manifold theory TM,ρ coincides with complex conjugation in SL(2, C) Chern-Simons theory
on M.
