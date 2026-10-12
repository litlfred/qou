---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-014-51-the-newton-polygon
section_title: "The Newton polygon"
section_number: 5.1
pages: 22-23
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
---
We summarize results from [51] (2).
2.2.1. The Newton polygon. — The contents of this section are valid as
well in the analytic as in the formal setting. To the (analytic or formal) q-
diﬀerence operator P = P aiσi
q ∈Dq, we associate the Newton polygon N(P),
deﬁned as the convex hull of {(i, j) ∈Z2 | j ≥v0(ai)}, where v0 denotes the
z-adic valuation in C({z}), C((z)). Multiplying P by a unit aσk
q of Dq just
translates the Newton polygon by a vector of Z2, and we shall actually consider
N(P) as deﬁned up to such a translation (or, which amounts to the same,
choose a unitary entire P). The relevant information therefore consists in the
lower part of the boundary of N(P), made up of vectors (r1, d1), . . . , (rk, dk),
ri ∈N∗, di ∈Z. Going from left to right, the slopes µi := di
ri
are rational
numbers such that µ1 < · · · < µk. Their set is written S(P) and ri is the
multiplicity of µi ∈S(P). The most convenient object is however the Newton
function rP : Q →N, such that µi 7→ri and null out of S(P).
Theorem 2.2.1. — (i) For a given q-diﬀerence module M, all unitary entire
P such that M ≃Dq/DqP have the same Newton polygon; the Newton polygon
of M is deﬁned as N(M) := N(P), and we put S(M) := S(P), rM := rP .
(ii) The Newton polygon is additive: for any exact sequence,
0 →M′ →M →M′′ →0 =⇒rM = rM′ + rM′′.
(iii) The Newton polygon is multiplicative:
∀µ ∈Q , rM1⊗M1(µ) =
X
µ1+µ2=µ
rM1(µ1)rM2(µ2).Also: rM∨(µ) = rM(−µ).
(iv) Let ℓ∈N∗, introduce a new variable z′ := z1/ℓ(ramiﬁcation) and make
K′ := C((z))[z′] = C((z′)) or C({z})[z′] = C({z′}) a diﬀerence ﬁeld extension
by putting σ′(z′) = q′z′, where q′ is any ℓth root of q. The Newton polygon of
the q′-diﬀerence module M′ := K′ ⊗M (computed w.r.t. variable z′) is given
by the formula:
rM(µ) = rM′(ℓµ).
2. Note however that, from [38], we changed our terminology: the slopes of a q-diﬀerence
module are the opposites of what they used to be (see herebelow subsection 2.2.1); and what
we call a pure isoclinic, resp. pure module was previously called pure, resp. tamely irregular
(see herebelow subsection 2.2.2).
