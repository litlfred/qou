---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-010-33-determinantal-probability-measures
section_title: "Determinantal probability measures"
section_number: 3.3
pages: 17-18
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
tal probability measure on 2[n] to be a measure µ ∈Pn such that there is an n × n
matrix A so that for any subset S of [n] one has
(11)
µ({T : S ⊆T}) = det(A[S]),
where as before A[S] denotes the principal submatrix of A whose rows and columns
are indexed by S. As discussed in e.g. [5, 57], such measures have important appli-
cations ranging from fermionic processes/continuous scaling limits of discrete point
processes [23, 59] to the distribution of eigenvalues of random matrices and zeros
of the Riemann zeta function [21], transfer current matrices [16], non-intersecting
random walks [47], Poissonized versions of the Plancherel measure on partitions
[13] and Young diagrams [64], discrete orthogonal polynomial ensembles [46], etc.
538
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
Recall that a square matrix A is said to be a contraction if ||A|| ≤1, where || · ||
denotes the supremum (operator) norm. Clearly, a positive semi-deﬁnite matrix is
a contraction if and only if all its eigenvalues are in the interval [0, 1]. Such matrices
were called positive contractions in [57].
Theorem 3.4. Suppose that µ is a determinantal measure on 2[n] whose corre-
sponding matrix is a positive contraction. Then µ is CNA+.
This is one of the main results of [57] (cf. [57, Theorem 8.1]), where exterior
(Grassmann) algebra methods were used to investigate determinantal probability
measures and, in particular, to prove the above theorem. As noted in loc. cit., The-
orem 3.4 provides a powerful tool for studying determinantal probability measures,
comparable to the FKG theorem in the theory of positive association, and is crucial
to most of the results in e.g. [59].
Let us show that Theorem 3.4 actually follows from Theorem 4.9 of §4.2 and
the fact that determinantal measures induced by positive contractions are strongly
Rayleigh:
Proposition 3.5. Suppose that µ is a determinantal measure on 2[n] whose corre-
sponding matrix is a positive contraction. Then µ is strongly Rayleigh.
Proof. Since positive deﬁnite matrices are dense in the set of all positive semi-
deﬁnite matrices, by Proposition 3.1 (3) it is enough to prove the statement for
invertible positive contractions. Elementary computations show that
gµ(z1, . . . , zn) = det(I −A + AZ) = det(A) · det(A−1 −I + Z),
where Z = diag(z1, . . . , zn). Since A is an invertible positive contraction, A−1 −I is
positive semi-deﬁnite and det(A) > 0, so by (6) the polynomial gµ is real stable.
□
Another main result of [57] is that if A and B are commuting positive contrac-
tions and A ≤B, then the measure corresponding to B stochastically dominates
the one corresponding to A (Deﬁnition 2.14). In §4.3 we extend this result using the
theory of stability and strongly Rayleigh measures and we prove that the condition
[A, B] = 0 (where [·, ·] denotes the Lie bracket) can be dropped from the hypothesis.
