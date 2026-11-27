---
doc_id: arxiv-math-0102098v1
doc_title: "Skein theory and the Murphy operators"
section_id: sec-007-41-algebraic-properties-of-a
section_title: "Algebraic properties of A."
section_number: 4.1
pages: 17-18
source_pdf: 0102098v1.pdf
source_sha256: f4bc5ca0ba1e47aa
toc_source: inferred
doc_brief: "Skein theory and the Murphy operators — The Murphy operators in the Hecke algebra Hn of type A are ex- plicit commuting elements whose sum generates the centre."
---
Algebraic properties of A.
Kawagoe [9] and other authors have used a skein which is linearly isomorphic
to A, based on the annulus with input and output on the same component.
The signiﬁcant advantage of A lies in its algebraic properties.
Both l and r are algebra homomorphisms, since it is clear diagrammati-
cally that l(c1, a1)l(c2, a2) = l(c1c2, a1a2), while r behaves similarly.
Theorem 4.1 The algebra A is commutative.
Proof :
Unlike the case of C this is not immediately clear. Using standard
skein theory techniques we can represent any element of A as a linear combi-
nation of tangles consisting of a totally descending arc lying over a number
of closed curves. Each such tangle represents l(cm, am) = l(cm, e)am for some
m and some cm ∈C. The general element of A can then be written as a
Laurent polynomial
X
m∈Z
l(cm, e)am
17
in a, with coeﬃcients in the commutative subalgebra l(C, e) ⊂A. Since a
commutes with l(C, e) it follows that any two elements of A commute.
✷
The subalgebras l(C, e) and r(e, C) are both isomorphic to C, but they
are not equal. Their diﬀerence determines a sort of commutator map [ , e] :
C →A, deﬁned by [c, e] = l(c, e) −r(e, c).
We have already noted that [h1, e] = (s −s−1)a. We can deduce theorem
3.9 about the power sums of Murphy operators from the next theorem.
Theorem 4.2 For m ≥1 we have [Pm, e] = (sm −s−m)am.
