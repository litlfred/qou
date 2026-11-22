---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-001-22-the-spectral-theorem
section_title: "The Spectral Theorem"
section_number: 2.2
pages: 8-10
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
The Spectral Theorem
The spectrum σ(a) of a ∈B(H) is {λ ∈C : a −λ1 is not invertible}.
Exercise 2.2.1. (Look up proofs if necessary.) Show that σ(a) is a non-
empty closed bounded subset of C and that if a = a∗, σ(a) ⊆[−||a||, ||a||]
with either ||a|| or −||a|| in σ(a).
The spectral theorem takes a bit of getting used to and knowing how
to prove it does not necessarily help much. If one cannot “see” the spectral
decomposition of an operator it may be extremely diﬃcult to obtain—except
in a small ﬁnite number of dimensions where it is just diagonalisation. But
fortunately there is nothing like a course in operator algebras, either C∗or
von Neumann, to help master the use of this theorem which is the heart of
linear algebra on Hilbert space. The book by Reed and Simon, “Methods of
mathematical physics” vol. 1, Functional Analysis, contains a treatment of
the spectral theorem which is perfect background for this course. We will
make no attempt to prove it here—just give a vague statement which will
establish terminology.
The spectral theorem asserts the existence of a projection valued measure
from the Borel subsets of σ(a) (when a = a∗or more generally when a is
8
normal i.e. [a, a∗] = 0) to projections in B(H), written symbolically λ →
E(λ), such that
a =
Z
λdE(λ).
This integral may be interpreted as a limit of sums of operators (necessitating
a topology on B(H)), as a limit of sums of vectors: aξ =
R
λdE(λ)ξ or simply
in terms of measurable functions ⟨ξ, aη⟩=
R
λd⟨ξ, E(λ)η⟩. The projections
E(B) are called the spectral projections of a and their images are called the
spectral subspaces of a.
Given any bounded Borel complex-valued function f on σ(a) one may
form f(a) by f(a) =
R
f(λ)dE(λ).
Exercise 2.2.2. If µ is a sigma-ﬁnite measure on X and f ∈L∞(X, µ),
the operator Mf : L2(X, µ) →L2(X, µ), (Mfg)(x) = f(x)g(x), is a bounded
(normal) operator with ||Mf|| = ess-supx∈X(|f(x)|). If f is real valued then
Mf is self adjoint. Find σ(f) and the projection-valued measure E(λ).
Exercise 2.2.3. If dim(H) < ∞ﬁnd the spectrum and projection-valued
measure for a (which is a Hermitian matrix).
The example of exercise 2.2.2 is generic -that any self-adjoint operator is
of the from Mf is another version of the spectral theorem.
Exercise 2.2.4. (A “visible” spectral decomposition.) Let H = ℓ2(Z and let
u ∈B(H) be translation by 1, i.e. uf(n) = f(n + 1). Then u + u∗is self-
adjoint. Use the Fourier transform to exhibit a measure space (X, µ) and a
function f on it so that (H, u + u∗) is unitarily equivalent to (L2(X, µ), Mf).
Proofs of the spectral theorem use the following general scheme:
If ξ ∈H is any vector and a = a∗∈B(H), let K be the closed linear span
of the {anξ : n = 0, 1, 2, 3, ...}, then a deﬁnes a self-adjoint operator on K
and one tries to ﬁnd a ﬁnite measure µ on the spectrum σ(a) such that (K, a)
is isomorphic in the obvious sense to (L2(σ(a), µ), multiplication by x). It
is not to hard to see how this should go-if a is supposed to be multiplication
by x, then we know that, for each n ∈N,
Z
σ(a)
xndµ = ⟨anξ, ξ⟩.
Moreover by the classical Weierstrass theorem polynomials are dense in the
continuous functions on the compact set σ(a). So we appeal to some classical
9
result from measure theory that says there is an appropriate measure. But
the inner product between anξ and amξ is then
R
σ(a) xn+mdµ so we may deﬁne
a unitary from K to L2(σ(a), µ) by sending amξ to the function xm on σ(a).
Note how it is the real numbers ⟨anξ, ξ⟩that determine everything.
So if you cannot "see" the spectral decomposition of an explicit operator
a, all is not lost but you should sniﬀaround the “moments” ⟨anξ, ξ⟩.
Continuing such an argument by restricting to K⊥one obtains a full
spectral theorem.
Exercise 2.2.5. Show that a self-adjoint operator a is the diﬀerence a+ −a−
of two positive commuting operators called the positive and negative parts of
a, obtained as functions of a as above.
