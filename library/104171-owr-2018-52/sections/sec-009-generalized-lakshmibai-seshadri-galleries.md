---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-009-generalized-lakshmibai-seshadri-galleries
section_title: "Generalized Lakshmibai-Seshadri galleries"
section_number: null
pages: 27-29
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Jacinta Torres
Let g be a complex, simple Lie algebra, and L(λ) a simple module over the complex
numbers of highest weight λ ∈X+. Consider the set
Γ = {γ : [0, 1] −→XR : γ(1) ∈X, γ(0) = 0}
of piecewise linear paths starting at the origin and ending at an integral weight. In
[2], Littelmann deﬁned a ﬁnite set of paths P(γλ) ⊂Γ depending on a single path
γλ ∈Γ with endpoint γλ(1) = λ and contained in the dominant Weyl chamber,
for which the character of L(λ) is a generating function in the following sense:
ch(L(λ)) =
X
γ∈P (γλ)
xγ(1).
(1)
The set P(γλ) is constructed by applying certain root operators fα, one for every
simple root α, to γλ. Together with their partial inverses eα, they endow the set
P(γλ) with the structure of a crystal isomorphic to B(λ).
Question. Given a path γ ∈Γ, how can one decide if it belongs to P(γλ) for
some γλ contained in the dominant Weyl chamber?
In this note, we give necessary conditions for galleries of alcoves, that is, certain
sequences of alcoves in the corresponding aﬃne Coxeter complex (which has the
same underlying space XR), with the ﬁrst alcove containing the origin and a choice
of integral weight contained in the last one. Our ongoing work generalizes work of
Gaussent-Littelmann in [1], where they introduce so-called Lakshmibai-Seshadri
galleries, for which the formula (1) makes sense and still holds after replacing η(1)
for a path η by the endpoint e(γ) of a gallery γ.
1. Galleries
A gallery of alcoves, or just a gallery, is a sequence
γ := (v0, a0, p1, · · · , pr, ar, vr)
(2)
of alcoves and panels (i.e. codimension one faces of alcoves) ai−1 ⊃pi ⊂ai for
i ∈[1, r]. In addition we require a choice of a ﬁnal vertex vr ∈X, an integral weight
contained in the last alcove, and ask that the ﬁrst alcove a0 contains the origin
v0 = 0. The integral weight vr is the endpoint e(γ) of the gallery γ. By labelling
the codimension one faces of the fundamental alcove with colours I = {i0, ..., in},
where n is the rank of the Lie algebra g, we obtain a labelling of every panel.
The label of a panel p will be denoted by t(p) and referred to as the type of the
panel. The type of a vertex v is the set t(v) = {t(p) : v ∈p} of types of the panels
containing v. The type of γ is the sequence of types
t(γ) := (t(p1), ..., t(pr))
3108
Oberwolfach Report 52/2018
of its panels and endpoint. Given a dominant integral weight λ ∈X+, we will
denote by
γλ := (v′
0, a′
0, p′
1, · · · , p′
r, a′
r, v′
r)
(3)
a gallery with v′
r = λ and such that each one of its alcoves and panels is contained
in the dominant Weyl chamber. We will call such a gallery dominant.
1.1. Dimension and properties of galleries. Let γ be a gallery, with nota-
tion as in (2). A hyperplane H is a load-bearing wall for γ at i ∈[0, r] if it
contains the i-th panel pi ⊂H (or the origin v0 ∈H if i = 0) and if ai ⊂H−.
The dimension of the gallery γ is the number of load bearing walls, counting
repetitions:
dim(γ) = ♯{j| there exists a load-bearing wall H for γ at j} .
We say that there is a fold at a panel pi if ai = ai−1, and a crossing if ai−1̸ = ai.
The fold or crossing is positive (respectively negative) if ai ⊂H+ (respectively
ai ⊂H−), where H is the hyperplane on which the panel pi is contained.
Figure 1. A dominant gallery of dimension 10 for the simple
exceptional Lie algebra of type G2. It consists of six alcoves: the
ﬁve distinct ones a0, the fundamental alcove, a1, a2, a3, a4, which
are noted in the picture, and a5 = a4. The corresponding fold at
the panel p5 is negative. The panels are indicated by the black
path, and the origin and endpoint are indicated by thick black
dots.
Let γλ be a dominant gallery, with notation as in (3). Let D ⊂[1, r] be the set
of indices i such that there is a negative crossing or fold in γλ at p
′
i. Consider the
set of galleries of the same type as γλ. Within this set, we look at those which
at the panels with indices in D have either a negative crossing or a negative fold.
Out of these, we restrict ourselves to those which, at every other panel, have either
a crossing or a positive fold. We will denote this set by Γ+(γλ). Now, for every
Enveloping Algebras and Geometric Representation Theory
3109
µ ≤λ consider the subset of Γ+
max(γλ, µ) ⊂Γ+(γλ) of galleries γ with maximal
dimension having endpoint e(γ) = µ, and
Γ+
max(γλ) =
[
µ≤λ
Γ+
max(γλ, µ).
Remark 1. If γλ is minimal as deﬁned in [1], then the set Γ+
max(γλ) is the set
of Lakshmibai-Seshadri galleries (LS galleries for short) introduced by Gaussent-
Littelmann in a geometric context. If this is the case, an LS gallery γ ∈Γ+
max(γλ)
has dimension ⟨λ + e(γ), ρ∨⟩.
We are now ready to state our result which generalizes work of Gaussent-
Littelmann and partially answers Question 1.
Theorem 2. The set Γ+
max(γλ) is stable under the action of the root operators
fα. Moreover, it only contains one dominant gallery, that is γλ.
References
[1] S. Gaussent and P. Littelmann. LS galleries, the path model, and MV cycles. Duke Math.
J., 127(1):35–88, 2005.
[2] P. Littelmann. Paths and root operators in representation theory. Ann. of Math. (2),
142(3):499–525, 1995.
