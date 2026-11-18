---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-034-122-spectral-theory-for-unbounded-operators
section_title: "Spectral Theory for Unbounded Operators"
section_number: 12.2
pages: 88-88
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
tors
Deﬁnition 12.2.1. Let T be a closed operator on H. The resolvent of T is
ρ(T) = {λ|λ1 −T : D(T) →H is a bijection}.
The spectrum of T is σ(T) = C\ρ(T).
Remark 12.2.2. Note that if λ1 −T : D(T) →H is a bijection then
(λ1 −T)−1 is bounded by the Closed Graph Theorem.
Exercise 12.2.3. The spectrum is highly dependent on the domain.
Let
AC[0, 1] denote the set of absolutely continuous functions on [0, 1]. Let T1 =
d
dx, T2 =
d
dx, with
D(T1)
=
{f ∈AC[0, 1] : f ′ ∈L2([0, 1])}
D(T2)
=
{f ∈AC[0, 1] : f ′ ∈L2([0, 1]), f(0) = 0}.
Show that T1 and T2 are closed. Show that σ(T1) = C while σ(T2) = ∅.
Proposition 12.2.4. Let (X, µ) be a ﬁnite measure space and F a measure-
able, real-valued, a.e. ﬁnite function on X. Let D(Mf) = {g ∈L2(X, µ) :
fg ∈L2(X, µ)} and let Mfg = fg. Then Mf is self-adjoint and σ(Mf) =
ess.range(f) = {λ ∈C : µ({x : |λ −f(x)| < ϵ}) > 0 ∀ϵ > 0}.
Exercise 12.2.5. Prove Prop 12.2.4.
Theorem 12.2.6 (Spectral Theorem - Multiplier Form). Let A be a self-
adfoint operator on H with dense domain. Then there exists a ﬁnite measure
space (X, µ), a real-valued a.e. ﬁnite function f on X and a unitary operator
u : H →L2(X, µ) such that uAu∗= Mf
Proof. See [2].
Remark 12.2.7 (Borel Functional Calculus). Note that the Spectral Theo-
rem allows us to deﬁne a Borel functional calculus for self adjoint operators.
Given a Borel function h on the spectrum of A, deﬁne h(A) = u∗Mh◦fu.
