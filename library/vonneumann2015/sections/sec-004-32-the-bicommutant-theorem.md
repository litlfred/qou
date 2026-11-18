---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-004-32-the-bicommutant-theorem
section_title: "The bicommutant theorem."
section_number: 3.2
pages: 12-12
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
The bicommutant theorem.
We will now prove the von Neumann “density” or “bicommutant” theorem
which is the ﬁrst result in the subject. We prove it ﬁrst in the ﬁnite dimen-
sional case where the proof is transparent then make the slight adjustments
for the general case.
Theorem 3.2.1. Let M be a self-adjoint subalgebra of B(H) containing 1,
with dim(H) = n < ∞. Then M = M ′′.
Proof. It is tautological that M ⊆M ′′.
So we must show that if y ∈M ′′ then y ∈M. To this end we will “amplify”
the action of M on H to an action on H⊗H deﬁned by x(ξ⊗η) = xξ⊗η. If we
choose an orthonormal basis {vi} of H then H ⊗H = ⊕n
i=1H and in terms of
matrices we are considering the n x n matrices over B(H) and embedding M
in it as matrices constant down the diagonal. Clearly enough the commutant
of M on H⊗H is the algebra of all n x n matrices with entries in M ′ and the
second commutant consists of matrices having a ﬁxed element of M ′′ down
the diagonal.
Let v be the vector ⊕n
i=1vi ∈⊕n
i=1H and let V = Mv ⊆H ⊗H. Then
MV ⊆V and since M = M ∗, PV ∈M ′ (on H ⊗H) by exercise 2.1.14. So if
y ∈M ′′ (on H⊗H), then y commutes with PV and yMv ⊆Mv. In particular
y(1v) = xv for some x ∈M so that yvi = xvi for all i, and y = x ∈M.
Theorem 3.2.2. (von Neumann) Let M be a self-adjoint subalgebra of B(H)
containing 1. Then M ′′ = M (closure in the strong operator topology).
Proof. Commutants are always closed so M ⊆M ′′.
So let a ∈M ′′ and N(a, ξ1, ξ2, ..., ξn, ϵ) be a strong neighbourhood of
a. We want to ﬁnd an x ∈M in this neighbourhood. So let v ∈⊕n
i=1H
be ⊕n
i=1ξi and let B(H) act diagonally on ⊕n
i=1H as in the previous theorem.
Then the same observations as in the previous proof concerning matrix forms
of commutants are true. Also M commutes with PMv which thus commutes
with a (on ⊕n
i=1H). And since 1 ∈M, av = ⊕aξi is in the closure of Mv so
there is an x ∈M with ||xξi −aξi|| < ϵ for all i.
Corollary 3.2.3. If M = M ∗is a subalgebra of B(H) with 1 ∈M, then the
following are equivalent:
1. M = M ′′
