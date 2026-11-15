---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland"
section_id: sec-003-jack-symmetric-functions-and-zonal-polynomials
section_title: "Jack symmetric functions and zonal polynomials"
section_number: null
pages: 3-3
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
toc_source: outline
doc_brief: "FPSAC 2011, Reykjavík, Iceland — In this paper we establish a new combinatorial formula for zonal polynomials in terms of power-sums. The proof relies on the sign-reversing involution principle."
---
Jack symmetric functions and zonal polynomials
The set of partitions of a given integer n can be endowed with a partial order, called dominance order: by
deﬁnition,
λ ⪯µ
⇐⇒
∀i≥1 λ1 + · · · + λi ≤µ1 + · · · + µi.
With respect to this order, the matrix of Schur functions in the monomial basis is upper triangular: i.e., if
one writes a Schur functions sλ on the monomial basis, the indices of the monomial symmetric functions
with non-zero coefﬁcients are dominated by λ. This triangularity property, together with the fact that they
form an orthonormal basis with respect to Hall scalar product, determines entirely the Schur functions.
Indeed, one can construct them by choosing any total order reﬁning the dominance order and applying
Gram-Schmidt orthogonalization process to the monomial symmetric function basis.
Hall scalar product can be deformed in the following way: ⟨·, ·⟩α is the bilinear form whose values on
the power-sum basis is given by
⟨pλ, pµ⟩α = zλ αℓ(λ) δλ,µ.
The following result corresponds to equations (VI,10.13) and (VI,10.14) of Macdonald’s book [Mac95].
Proposition 1 Fix α > 0. There exists a (unique) family of functions J(α)
λ
such that the following three
conditions are fulﬁlled:
TR The matrix of J(α)
λ
written in the monomial basis is upper triangular.
OR The J(α)
λ
form an orthogonal basis of the ring of symmetric functions endowed with the scalar
product ⟨·, ·⟩α.
N The coefﬁcient of p|λ|
1
in the power sum expansion of J(α)
λ
is equal to 1.
These functions are called Jack symmetric functions. When α = 1 they correspond, up to multiplication
by a scalar, to Schur functions. When α = 2 they are called zonal polynomials (because, as we already
mentioned in Section 1, they appear in representation theory of some Gelfand pairs, see [Mac95, VII, 2])
and denoted Zλ.
The uniqueness of such a family is easy to prove: it is essentially the same argument as the one given
above for the characterization of Schur functions.
