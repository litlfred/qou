---
doc_id: arxiv-2006.02042v1
doc_title: "The Strong AJ Conjecture for the Figure 8 Knot"
section_id: sec-004-2-proof-of-theorem
section_title: "Proof of Theorem ??"
section_number: 2
pages: 3-4
source_pdf: 2006.02042v1.pdf
source_sha256: 9de75ced3a3360bb
toc_source: outline
doc_brief: "The Strong AJ Conjecture for the Figure 8 Knot — Motivated by the theory of quantum A-ideals of Frohman-Gelca-LoFaro, the theory of q-holonomicity of quantum invariants of Garoufalidis-Le and the AJ"
---
For the ﬁgure eight knot E, it is known that the AJ conjecture holds true [Ga] and the
A-polynomial A′
E = L + L−1 −M4 −M−4 + M2 + M−2 + 2 does not have any nontrivial
nontrivial factors depending on M only. Hence, by [Tr4, Lemma 3.1],
p
ε(Aσ
E) ⊂pE.
For the converse
p
ε(Aσ
E) ⊂pE we will apply the following.
Lemma 2.1. Suppose there exists P ∈R[M±1, L±1] such that PJK ∈R[M±1], σ(P) = P
and ε(P) = MkLl(A′
K)2m for some integers k, l, m. Then pK ⊂
p
ε(Aσ
K).
Proof. Since PJK ∈R[M±1], by [Tr4, Lemma 3.3] there exists R ∈R[L±1] such that
σ(R) = R, ε(R) = (L + L−1 −2)r and RPJK = 0 for some integer r ≥1.
Let Q = RmP r ∈R[M±1, L±1]. Then QJK = 0, σ(Q) = Q and ε(Q) = ε(R)mε(P)r =
MkrLlr−mr((L −1)A′
K)2mr. Hence, by [Tr4, Lemma 3.2] we obtain pK ⊂
p
ǫ(Aσ
K).
□
By Lemma 2.1 we will ﬁnd P ∈R[M±1, L±1] such that PJE ∈R[M±1], σ(P) = P and
ε(P) = (A′
E)2. Note that
(A′
E)2 = ˜a2(M)L2 + ˜a−2(M)L−2 + ˜a1(M)L + ˜a−1(M)L−1 + ˜a0(M),
where
˜a2(M)
=
˜a−2(M) = 1,
˜a1(M)
=
˜a−1(M) = −2M4 −2M−4 + 2M2 + 2M−2 + 4,
˜a0(M)
=
M8 + M−8 −2M6 −2M−6 −3M4 −3M−4 + 2M2 + 2M−2 + 10.
To ﬁnd P, we start with a non-homogeneous recurrence polynomial for JE. Let
α′
E(t, M, L) = a1(t, M)L + a−1(t, M)L−1 + a0(t, M)
where
a1(t, M)
=
t−2M2 −t2M−2,
a−1(t, M)
=
t2M2 −t−2M−2,
a0(t, M)
=
(M2 −M−2)(−M4 −M−4 + M2 + M−2 + t4 + t−4).
By [CM, Proposition 4.4] we have α′
EJE ∈R[M±1].
Observe that if B(t, M, L) is a rational function such that Bα′
E is a Laurent polynomial
in t, M, L then Bα′
E is another non-homogeneous recurrence polynomial for JE. Namely
Bα′
EJE ∈R[M±1]. This suggests that we may consider P ∈R[M±1, L±1] of the form
P = Bα′
E where
B(t, M, L) = b1(t, M)L + b−1(t, M)L−1 + b0(t, M)
and bi’s are rational functions in t and M. Explicitly we have
P(t, M, L) = p2(t, M)L2 + p−2(t, M)L−2 + p1(t, M)L + p−1(t, M)L−1 + p0(t, M)
4
HOANG-AN NGUYEN AND ANH T. TRAN
where
p2(t, M)
=
b1(t, M)a1(t, t2M),
p−2(t, M)
=
b−1(t, M)a−1(t, t−2M),
p1(t, M)
=
b0(t, M)a1(t, M) + b1(t, M)a0(t, t2M),
p−1(t, M)
=
b0(t, M)a−1(t, M) + b−1(t, M)a0(t, t−2M),
p0(t, M)
=
b0(t, M)a0(t, M) + b−1(t, M)a1(t, t−2M) + b1(t, M)a−1(t, t2M).
Since PJK = Bα′
EJK ∈R[M±1], the remaining conditions for P are σ(P) = P and
ε(P) = (A′
E)2. These conditions are equivalent to the followings
p2(t, M)
=
p−2(t, M−1),
(2.1)
p1(t, M)
=
p−1(t, M−1),
(2.2)
p0(t, M)
=
p0(t, M−1),
(2.3)
and
p2(1, M)
=
˜a2(M),
(2.4)
p−2(1, M)
=
˜a−2(M),
(2.5)
p1(1, M)
=
˜a1(M),
(2.6)
p−1(1, M)
=
˜a−1(M),
(2.7)
p0(1, M)
=
˜a0(M).
(2.8)
We will call the ﬁrst set of conditions the symmetric conditions and the second set
the initial conditions. We also note that pi’s must be polynomials in t, M, L, and we call
these conditions the polynomial conditions. We now give a detailed method for solving
the system of equations (2.1)–(2.8).
