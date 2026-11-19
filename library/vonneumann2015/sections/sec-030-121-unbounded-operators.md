---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-030-121-unbounded-operators
section_title: "Unbounded Operators"
section_number: 12.1
pages: 85-86
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Spectral Theory
There are many naturally arising examples of unbounded operators, some
of the most fundamental being multiplication by x and diﬀerentiation, the
position and momentum operators of quantum mechanics. Our immediate
motivation for studying unbounded operators here is to facilitate the study
of arbitrary von Neumann algebras acting on GNS Hilbert spaces. Here we
establish the necessary preliminaries on unbounded operators. The material
closely follows Reed and Simon [2].
12.1
Unbounded Operators
Deﬁnition 12.1.1. An operator T on a Hilbert space H consists of a linear
subspace D(T), the domain of T, and a linear map from D(T) to H.
Example 12.1.2.
(i) Mx, multiplication by x on L2(R).
D(Mx) =

f ∈L2(R) :
Z
R
x2|f(x)|2d x < ∞

.
(ii) T =
d
d x on L2([0, 1]). D(T) = C1[0, 1].
In order to do some analysis we want to restrict our attention a little so
as not to consider completely arbitrary linear maps.
Deﬁnition 12.1.3. Let T be an operator on H. The graph of T is
Γ(T) = {(ξ, Tξ) : ξ ∈D(T)} ⊂H ⊕H.
T is closed if Γ(T) is closed in H ⊕H.
85
Remark 12.1.4. Note that if T is closed and D(T) = H then T is bounded
by the Closed Graph Theorem.
Lemma 12.1.5. A linear subspace Γ ⊂H ⊕H is the graph of an operator
iﬀ(0, η) ∈Γ implies η = 0.
Proof. Straightforward.
Many operators are not closed, but can be extended to a closed operator.
Deﬁnition 12.1.6. Let S, T be operators on H. T is an extension of S,
denoted S ⊂T, if Γ(S) ⊂Γ(T). Equivalently D(S) ⊂D(T) and T|D(S) = S.
Deﬁnition 12.1.7. An operator T is preclosed (or closable) if it has a closed
extension.
Lemma 12.1.8. Suppose T is preclosed. Then T has a smallest closed ex-
tension T. Γ(T) = Γ(T).
Proof. Take a closed extension A of T. Γ(A) is closed and contains Γ(T) so
Γ(T) ⊂Γ(A). Γ(T) is the graph of an operator (call it T) because:
(0, η) ∈Γ(T) ⊂Γ(A) ⇒η = A(0) = 0.
T is the smallest closed extension because for all closed extensions A, Γ(T) =
Γ(T) ⊂Γ(A).
Deﬁnition 12.1.9. T is called the closure of T.
Remark 12.1.10. We thus obtain two equivalent deﬁnitions of a preclosed
operator:
(i) (0, η) ∈Γ(T) ⇒η = 0.
(ii) (ξn ∈D(T), ξn →0 and Tξn converges) ⇒Tξn →0.
Exercise 12.1.11.
(i) Deﬁne S on L2(R) by D(S) = C∞
