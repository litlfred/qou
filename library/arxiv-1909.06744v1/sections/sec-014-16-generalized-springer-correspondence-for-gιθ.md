---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-014-16-generalized-springer-correspondence-for-gιθ
section_title: "§16. Generalized Springer correspondence for Gιθ"
section_number: null
pages: 18-20
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
toc_source: inferred
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spaces."
---
uni, the case H = SO2n+1
In this section, we consider the generalized Springer correspondence for Gιθ
uni
with H = SON (N = 2n + 1).
16.1.
First we will give a combinatorial description of NGιθ.
Let λ =
(λ1, . . . , λN) ∈PN be a partition with λN ≥0. We deﬁne a symbol τ = (τ1, . . . , τN)
of type λ as follows;
(i) τi = ±1, and τi = 1 if λi = 0.
(ii) τi = τj if λi = λj.
(iii) τk = 1 if λk is the largest odd number among λ1, . . . , λN.
Then by Proposition 12.3, the set of symbols of type λ is in bijection with the
set AH(x)∧for x ∈Oλ. Note that the condition (iii) is related to the diﬀerence
between AGθ(x) and AH(x). Now the set NGιθ can be expressed combinatorially by
a set ΨN as follows;
(16.1)
ΨN := {(λ, τ) | λ ∈PN, τ: type λ} ≃NGιθ.
An element (λ, τ) ∈ΨN is called a cuspidal symbol if
(i) λi −λi+1 ≤2 for i = 1, . . . , N ( here we put λN+1 = 0 ),
(ii) If λi −λi+1 = 2, then τi̸ = τi+1.
We denote by Ψ(0)
N the set of cuspidal symbols in NGιθ.
16.2.
Lusztig’s theory of the generalized Springer correspondence for reductive
groups can be extended to the case of symmetric spaces Gιθ
uni, namely
• The notion of a cuspidal pair for (O, E ) ∈NGιθ,
• The notion of induction indG
P for a θ-stable parabolic subgroup P and its
θ-stable Levi subgroup L,
indG
P : {LH-equiv. perverse sheaves on Lιθ } →{ semisimple complexes on Gιθ }
19
The induction functor is deﬁned by modifying the arguments in Section 5.
The following result was proved in [SY].
Proposition 16.3. Under the identiﬁcation NGιθ ≃ΨN, the pair (O, E ) is cuspidal
if and only if the corresponding symbol (λ, τ) ∈ΨN is cuspidal.
Remark 16.4.
In general, θ-stable Levi subgroup L has the form
LH ≃GLa1 × Ga2 × · · · × GLar × SON0,
where N0 = N −2 P
i ai. Among them, Lιθ
uni has a cuspidal pair (O1, E1) only when
LH ≃(GL1)a × SON0 for some 0 ≤a ≤n.
16.5.
We give here some example of cuspidal pairs. It would be interesting to
compare this with the case of reductive groups (Remark 5.2).
(i) For λ = (2a, 1N−2a), the pair (Oλ, E ) is always cuspidal, for any local system
E .
(ii) In particular, for Oλ = {1} with λ = (1N),
the pair (Oλ, ¯Ql) is cuspidal
(iii) The number |Ψ(0)
N | is always large. For example, for N = 3, 5, 7, we have
|Ψ(0)
N | = 3, 7, 16.
In general, we can determine the generating function of |Ψ(0)
N |.
Lemma 16.6. We deﬁne a function q1(n) for n ≥0 by
∞
Y
i=1
(1 + ti)2 =
X
n≥0
q1(n)tn
Then we have |Ψ(0)
2n+1| = 1
2q1(2n + 1).
16.7.
We prepare some notations for formulating the generalized Springer cor-
respondence. We deﬁne SGιθ as the set of triples, (L, O1, E1), up to the conjugation
action of H, where L is a θ-stable Levi subgroup of a θ-stable parabolic subgroup P,
and (O1, E1) is a cuspidal pair in Lιθ
uni. Since LH ≃(GL1)a×SON0 with N0 = N −2a
(Remark 16.4), we have
(16.2)
SGιθ ≃CN := {(N0, ν, σ) | N ≥N0 : odd, (ν, σ) ∈Ψ(0)
N0}
Take ξ = (N0, ν, σ) ∈CN corresponding to (L, O1, E1) ∈SGιθ, and put Kξ =
IC(O1, E1)[dim O1]. Since Kξ is an LH-equivariant perverse sheaf on Lιθ, one can
consider the complex indG
P Kξ on Gιθ
uni.
For each ξ = (N0, ν, σ) ∈CN, deﬁne a map Γξ : Pa 7→ΨN as follows. Put
eσ = (σ1, . . . , σN) = (σ1, . . . , σN0, 1, . . . , 1) for σ = (σ1, . . . , σN0). For µ ∈Pa, put
λ = ν + 2µ ∈PN, and deﬁne
(16.3)
Γξ(µ) = (λ, eσ) ∈ΨN.
The following result gives the generalized Springer correspondence for Gιθ
uni,
which is an analogue of Theorem 5.1.
20
Theorem 16.8 ([SY]).
(i) For ξ ∈CN ≃SGιθ, indG
