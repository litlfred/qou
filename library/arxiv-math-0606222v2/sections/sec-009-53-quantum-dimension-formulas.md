---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-009-53-quantum-dimension-formulas
section_title: "Quantum dimension formulas"
section_number: 5.3
pages: 20-21
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
ical Uq-representationsV q
λ (λ ∈ Λ n) have the following explicit closed expressions.
Proposition 5.3. Forλ ∈ Λ n we have
Dimq
(
V q
λ
)
=q2(2n−d−1)|λ|−4(ρ,λ)
n∏
i=1
(
q2(1+λi+ρi);q2) 2
d−2n
(
q2(1+ρi);q2) 2
d−2n
(1 −q2(d−2n+1+2(λi+ρi)))
(1 −q2(d−2n+1+2ρi))
×
∏
1≤j<k≤n
(1 −q2(d−2n+1+λj +λk+ρj+ρk))2(1 −q2(λj−λk+ρj−ρk))2
(1 −q2(d−2n+1+ρj +ρk))2(1 −q2(ρj−ρk))2 .
(5.5)
In Section 8 we derive Proposition 5.3 from a generalization of the qua ntum dimension
formula (5.4) to the setup of the one-parameter family of quantum complex Grassmanni-
ans from [20] and [5]. By a suitable degeneration procedure we subse quently deduce the
quantum dimension formulas
(5.6) Dim q
(
V q
λ
)
=Dq2
(
λ;q2(d−2n+1),q 2;q2), λ ∈ Λ n
in terms of evaluations and quadratic norms of multivariable little q-Jacobi polynomials.
More directly, (5.6) is a direct consequence of the quantum dimensio n formula (5.4) if
one uses the fact that the quantum zonal spherical functions ϕq
λ (λ ∈ Λ n) identify with
multivariable little q-Jacobi polynomials (see [5] and Remark 8.5).
Remark 5.4. Taking the limit q → 1 in (5.5), we obtain the explicit dimension formulas for
the irreducible M-spherical K-representationsV C
λ (λ ∈ Λ n) as stated in Proposition 4.2.
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 21
We end this subsection by discussing the representation theoretic viewpoint on the quan-
tum dimension formula (5.5) for λ =ωr, in which case it yields the explicit expression
(5.7) Dim q
(
V q
ωr
)
=q2r(d−r)
(d
r
) 2
q−2
−q2(r−1)(d−r+1)
( d
r − 1
) 2
q−2
for r = 1,...,n by a straightforward computation. The following representation t heoretic
derivation of (5.7) bears strong resemblance to the representat ion theoretic derivation of
the dimension formula (4.16) in the classical non-Archimedean setup .
Let {ǫj}d
j=1 be the standard orthonormal basis of Rd. Let V =Lq
ǫ1 be the d-dimensional
vector-representation of Uq. Its weight spaces are one-dimensional, with weights ǫj (j =
1,...,d ). The irreducible representation Lq
ǫ1+···+ǫr (1 ≤ r ≤ n) can be realized as the rth
graded part Λ r
q(V ) of the q-exterior algebra Λ q(V ) of V (see [21]). The weight spaces of
Λ r
q(V ) are again one-dimensional, with weights given by ∑
j∈Jǫj for subsets J ⊆ {1,...,d }
of cardinality r. Hence
Dimq
(
Λ r
q(V )
)
= TrΛ r
q(V )(K 2δ·) =
∑
J ⊆{1,...,d}
#J=r
∏
j∈J
q2(d−j) =q(r−1)r
(
q2(d−r+1);q2)
r
(
q2;q2)
r
,
where the third equality follows by an easy induction argument. The d ual of Λ r
q(V ) is
irreducible of highest weight −ǫd−r+1 · · · −ǫd. In fact, by [21] we have
Λ r
q(V )∗ ≃ Cdet−1
q ⊗ Λ d−r
q (V ),
with Cdet−1
q ≃Lq
−ǫ1···−ǫd the one-dimensional representation realized by the inverse of the
quantum determinant det q ∈ Cq(K), hence
Dimq
(
Λ r
q(V )∗)
=q(1+r−2d)r
(
q2(r+1);q2)
d−r
(
q2;q2)
d−r
.
We conclude that
Dimq
(
Ur
)
=q2r(d−r)
(d
r
) 2
q−2
,
where Ur is the Uq-module
Ur = Λ r
q(V ) ⊗ Λ r
q(V )∗.
By [5, (6.14)] we have
Ur ≃Ur−1 ⊕V q
ωr, r = 1,...,n
as Uq-modules (with U0 the trivial representation), which now immediately implies (5.7).
