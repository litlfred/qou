---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-008-41-deﬁnition-of-type-i-factor
section_title: "Deﬁnition of type I factor."
section_number: 4.1
pages: 25-26
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Deﬁnition of type I factor.
The ﬁrst crucial result about factors (remember a factor is a von Neumann
algebra with trivial centre) will be the following “ergodic” property.
Theorem 4.1.1. If M is a factor and p and q are non-zero projections in
M there is an x ∈M with pxq̸ = 0. Moreover x can be chosen to be unitary.
Proof. Suppose that for any unitary u ∈M, puq = 0. Then u∗puq = 0 and

W
u∈M u∗pu

q = 0. But clearly
W
u∈M u∗pu commutes with all unitaries u ∈M
so is the identity.
The reason we have called this an “ergodic” property is because of a per-
vasive analogy with measure-theoretic dynamical systems (and it will become
much more than an analogy). A transformation T : (X, µ) →(X, µ) pre-
serving the measure µ is called ergodic if T −1(A) ⊆A implies µ(A) = 0 or
µ(X \ A) = 0 for a measurable A ⊆X. If T is invertible one can then show
that there is, for any pair A ⊂X and B ⊂X of non-null sets, a power T n
of T such that µ(T n(A) ∩B)̸ = 0. Or, as operators on L2(X, µ), AT NB̸ = 0
where we identify A and B with the multiplication operators by their char-
acteristic functions. The proof is the same—the union of all T n(A) is clearly
invariant, thus must diﬀer from all of X by a set of measure 0.
Corollary 4.1.2. Let p and q be non-zero projections in a factor M. Then
there is a partial isometry u (̸= 0) in M with uu∗≤p and u∗u ≤q.
p and q had been swapped
around in the proof, so we
interchanged uu∗and u∗u
in the statement.
25
Proof. Let u be the partial isometry of the polar decomposition of pxq for x
such that pxq̸ = 0.
Deﬁnition 4.1.3. If M is a von Neumann algebra, a non-zero projection
p ∈M is called minimal, or an atom, if
(q ≤p) ⇒(q = 0
or
q = p).
Exercise 4.1.4. Show that p is minimal in M iﬀpMp = Cp.
Deﬁnition 4.1.5. A factor with a minimal projection is called a type I
factor.
