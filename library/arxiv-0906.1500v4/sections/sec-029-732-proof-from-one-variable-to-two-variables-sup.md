---
doc_id: arxiv-0906.1500v4
doc_title: "TWISTED ALEXANDER INV ARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS"
section_id: sec-029-732-proof-from-one-variable-to-two-variables-sup
section_title: "Proof from one variable to two variables. Suppose that ϕ : π1(M ) → Z ⊕ Z. A"
section_number: 7.3.2
pages: 22-23
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "TWISTED ALEXANDER INVARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS — W e study a computational method of the hyperbolic Reidemeister torsion (also"
---
priori, up to multiplications by tr
1ts
2, the torsion ∆ ϕ⊗Ad◦ρ
M (t1, t2) is a rational function
P (t1, t2)/Q(t1, t2), where P (t1, t2) and Q(t1, t2) ⁄= 0 are coprime in C[t1, t2]. We will
prove in fact, reducing the situation to one variable, that the polyn omial Q(t1, t2) is
constant.
To this end, suppose that Q(t1, t2) is a non–constant polynomial. Without loss of
generality we assume that Q(t1, t2) is a non–constant in t2. Applying Euclidean algorithm
to P (t1, t2) and Q(t1, t2) in C(t1)[t2], we obtain the following equality in the polynomial
ring C(t1)[t2] over the rational function ﬁeld C(t1):
P (t1, t2)˜u(t1, t2) + Q(t1, t2)˜v(t1, t2) = 1 .
Here the coeﬃcients of the polynomials in t2 ˜u(t1, t2) and ˜v(t1, t2) are rational functions
in C(t1). By taking product with some polynomial w(t1) ∈ C[t1], the following equality
holds in C[t1, t2]:
(31) P (t1, t2)u(t1, t2) + Q(t1, t2)v(t1, t2) = w(t1).
To each pair of coprime integers ( a1, a2), consider the homomorphism h(a1,a2) : Z2 → Z
deﬁned by h(a1,a2)(t1) = ta1 and h(a1,a2)(t2) = ta2 and let ϕ(a1,a2) = h(a1,a2) ◦ ϕ. Using
Proposition 4 and by the ﬁrst part of the proof (for one variable), we know that:
∆
ϕ(a1 ,a2 )⊗Ad◦ρ
M (t) = ∆ ϕ⊗Ad◦ρ
M (ta1, ta2 ) = P (ta1 , ta2)
Q(ta1, ta2 ) ∈ C[t].
Thus there exists a polynomial R(t) ∈ C[t] such that P (ta1 , ta2) = R(t)Q(ta1 , ta2). Hence
by substituting ta1 and ta2 to t1 and t2 respectively, Equation (31) turns into
Q(ta1, ta2 ){R(t)u(ta1, ta2) + v(ta1 , ta2 )} = w(ta1 ).
From our assumption a2 can be chosen suﬃciently large. Since we suppose that
Q(t1, t2) is not constant in t2, by changing a2 into a suﬃcient large integer, we obtain an
arbitrary large degree polynomial Q(ta1, ta2 ). This contradicts the fact that the degree
of Q(ta1 , ta2) must be less or equal to that of w(ta1 ). Therefore Q(t1, t2) is constant in
t2.
Similarly, we can also conclude that Q(t1, t2) is constant in t1. As a consequence, the
polynomial Q(t1, t2) is constant which proves that ∆ ϕ⊗Ad◦ρ
M (t1, t2) is a polynomial in two
variables.
By an inductive argument (in descending order of ai), the general case works in the
same way: ∆ ϕ⊗Ad◦ρ
M (t1, . . . , tn) ∈ C[t1, . . . , tn]. The multivariable case in Theorem 12 is
also proved.
Remark 16. Actually, in the multivariable case of Theorem 12, it is suﬃcient to assu me
that there exists some positive integer N0 such that for any N /greaterorequalslantN0 we have a dual
surfaces S(a1,...,an) satisfying that |ai − aj| > N for all distinct i, j.
22
