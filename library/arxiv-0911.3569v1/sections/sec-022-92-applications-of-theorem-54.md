---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-022-92-applications-of-theorem-54
section_title: "Applications of Theorem 5.4."
section_number: 9.2
pages: 27-29
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
anaogue of the multiplier sequences studied by P´ olya and Schur. Letλ : Nm→ R,
and deﬁne a linear transformation Tλ : C[x]→ C[x] by Tλ(xα) = λ(α)xα for all
α∈ Nm, and linear extension. For which λ does Tλ preserve real stability? The
answer: just the ones you get from the P´ olya-Schur Theorem, and no more.
Theorem 9.3 (Theorem 1.8 of [4].) . Let λ : Nm→ R. Then Tλ preserves real
stability if and only if there are univariate multiplier sequences λi : N→ R for
i∈ [m] and ϵ∈{− 1, +1} such that
λ(α) =λ1(α(1))··· λm(α(m))
for all α∈ Nm, and either ϵ|α|λ(α)≥ 0 for all α∈ Nm, or ϵ|α|λ(α)≤ 0 for all
α∈ Nm.
Theorem 5.4 (and similarly Propositions 9.1 and 9.2) can be used to derive a
wide variety of results of the form: such-and-such an operation preserves stability
(or Schur or Hurwitz stability). Here is a short account of Hinkkanen’s proof of the
Lee-Yang Circle Theorem, taken from Section 8 of [6].
28 DAVID G. WAGNER
Forf,g ∈ C[x]MA, say f =∑
S⊆[m]a(S)xS and g =∑
S⊆[m]b(S)xS, let
f•g =
∑
S⊆[m]
a(S)b(S)xS
be the Schur-Hadamard product of f and g.
Theorem 9.4 (Hinkkanen, Theorem 8.5 of [6]) . If f,g ∈ C[x]MA are Schur stable
then f•g is Schur stable.
Proof. Let Tg : C[x]MA→ C[x]MA be deﬁned by f ↦→ f•g. By Proposition 9.1,
to show that Tg preserves Schur stability it suﬃces to show that Tg((1 + xy)[m])
is Schur stable. Clearly Tg((1 + xy)[m]) = g(x1y1,...,x mym) is Schur stable since
g(x) is. Hence Tg preserves Schur stability, and so f•g is Schur stable. □
Theorem 9.5 (Lee-Yang Circle Theorem, Theorem 8.4 of [6]) . LetA = (aij) be a
Hermitian m-by-m matrix with|aij|≤ 1 for all i,j ∈ [m]. Then the polynomial
f(x) =
∑
S⊆[m]
xS∏
i∈S
∏
j⁄∈S
aij
is Schur stable. The diagonalization g(x) = f(x,...,x ) is such that xmg(1/x) =
g(x), and it follows that all roots of g(x) are on the unit circle.
Proof. Fori<j in [m] let
fij = (1 +aijxi +aijxj +xixj)
∏
h∈[m]r{i,j}
(1 +xh).
One can check that each fij is Schur stable. The polynomial f(x) is the Schur-
Hadamard product of all the fij for{i,j}⊆ [m]. By Theorem 9.4, f(x) is Schur
stable. □
Section 8 of [6] contains many many more results of this nature.
9.3. A converse to the Grace-Walsh-Szeg˝ o Theorem.The argument of Sec-
tions 4.2 and 4.3 can be used to prove the following.
Exercise 9.6. If f∈ S[x]MA is multiaﬃne and stable then
TS(m)(f) = 1
m!
∑
σ∈S(m)
σ(f)
is multiaﬃne and stable.
This is in fact equivalent to the GWS Theorem, since for all f ∈ C[x]MA,
TS(m)f(x) = Polmf(x,...,x ). For which transitive permutation groups G≤ S(m)
does the linear transformation TG =|G|−1∑
σ∈Gσ preserve stability? The answer:
not many, and they give nothing new.
Theorem 9.7 (Theorem 6 of [9].). LetG≤ S(m) be a transitive permutation group
such that TG preserves stability. Then TG =TS(m).
MULTIVARIATE STABLE POLYNOMIALS 29
