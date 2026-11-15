---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-008-9-double-kostka-polynomials
section_title: "§9. Double Kostka polynomials"
section_number: null
pages: 10-11
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
toc_source: inferred
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spaces."
---
Kostka polynomials Kλ,µ(t) (λ, µ ∈Pn) was generalized to double Kostka poly-
nomials Kλ,µ(t) (λ, µ ∈Pn,2). (See [S1, S2], where they are deﬁned for any r-
partitions. Here we only consider the special case where r = 2). Recall the dis-
cussion in Section 6.
Here we prepare two types of variables x′ = (x′
1, x′
2, . . . ),
x′′ = (x′′
1, x′′
2, . . . ) and consider Ξ = L
n≥0 Λ(x′)⊗Λ(x′′), the ring of symmetric func-
tions with respect to x = (x′, x′′). Put Ξ[t] = Ξ ⊗Z Z[t]. For λ = (λ′, λ′′) ∈Pn,2,
one can deﬁne the Schur function sλ(x) = sλ′(x′)sλ′′(x′′) and Hall-Littlewood func-
tions Pλ(x; t). (Note that the deﬁnition of Pλ(x; t) is rather complicated.) Then
{sλ(x) | λ ∈Pn,2}, {Pλ(x; t) | λ ∈Pn,2} give two Z[t]-bases of Ξn[t] = Ξn ⊗Z Z[t].
We deﬁne the double Kostka polynomial Pλ,µ(t) ∈Z[t] by
(9.1)
sλ(x) =
X
µ∈Pn,2
Kλ,µ(t)Pµ(x; t).
For λ = (λ′, λ′′) ∈Pn,2, deﬁne an a-function a : Pn,2 →Z≥0 by
(9.2)
a(λ) = 2(n(λ′) + n(λ′′)) + |λ′′|.
The a-function has a role of n-function in the case of Pn,2. It is known that Kλ,µ(t)
is a monic of degree a(µ) −a(λ). As an analogue of (6.4), we deﬁne a modiﬁed
double Kostka polynomial eKλ,µ(t) by
(9.3)
eKλ,µ(t) = ta(µ)Kλ,µ(t−1).
The following result was proved by [AH], which is an analogue of Theorem 6.1,
and gives a geometric realization of double Kostka polynomials.
Theorem 9.1 ([AH]). For λ ∈Pn,2, put Aλ = IC(Oλ, ¯Ql). Then we have
(i) H iAλ = 0 for odd i.
(ii) Take λ, µ ∈Pn,2 such that µ ≤λ. For z ∈Oµ ⊂Oλ, we have
(9.4)
eKλ,µ(t) = ta(λ) X
i≥0
(dim H 2i
z Aλ)t2i.
Remark 9.2 If we compare the formula (9.4) with the formula (6.6) in Theorem
6.1, we notice the discrepancy of the relations between ti and cohomology sheaves.
11
In fact, in (6.6) ti corresponds to H 2i
x Aλ, while in (9.4) t2i corresponds to H 2i
z Aλ.
Later, we also consider the geometric realization of double Kostka polynomials by
means of exotic symmetric space. In that case, this discrepancy is removed (see
Theorem 13.4).
