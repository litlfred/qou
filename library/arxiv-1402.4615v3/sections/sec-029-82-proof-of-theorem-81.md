---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-029-82-proof-of-theorem-81
section_title: "Proof of Theorem 8.1"
section_number: 8.2
pages: 56-58
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
Olshanski is to prove that u(1)
k and t(1)
k are in
(
Λ (1)
⋆
) ext
and fulﬁll
u(1)
k =
Ch(1)
(k+1)
(k + 1) Ch(k+1)/2
(1)
+ terms of negative degree for deg4;(45)
t(1)
k =
Ch(1)
(k−1)
Ch(k−1)/2
(1)
+ terms of negative degree for deg4.(46)
These equations are respectively the last equations of Sections 7 and 8 in paper
[IO02]. As the notations are a little bit different here, let us give a few precisions.
• The quantity ηk+1 in [IO02] is deﬁned by equation (6.5) and deﬁnition 3.1.
• In [IO02], it is shown that the reminder has negative degree in the ﬁltration
deg{1}, while here we use the gradation deg4. But we have proven in
Lemma 8.2 that both notions coincide on Λ (1)
⋆ .
• The identities in [IO02] are equalities of random variables, that is of func-
tions on the set of Young diagrams of size n (which is here the probability
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 57
space) ; as they are valid for any n, we have in fact identities of functions
on the set of Young diagrams, as claimed above.
Note that, as equalities of functions on the set of Young diagrams, one can evaluate
them on continuous diagrams, in particular on Aα(λ).
Our goal is to establish similar formulas in the general α-case. From the deﬁni-
tion, it is straight-forward that
u(α)
k (λ) = u(1)
k
(
Aα(λ)
)
;(47)
t(α)
k (λ) = t(1)
k
(
Aα(λ)
)
.(48)
Therefore, applying equations (45) and (46) on Aα(λ), we get:
u(α)
k (λ) =
Ch(1)
(k+1)
(
Aα(λ)
)
(k + 1)
(
Ch(1)
) (k+1)/2 + terms of negative degree for deg4;(49)
t(α)
k (λ) =
Ch(1)
(k−1)
(
Aα(λ)
)
(
Ch(1)
) (k−1)/2 + terms of negative degree for deg4.(50)
Of course in general, although both quantities lie in Λ (α)
⋆ ,
Ch(1)
(k)
(
Aα(λ)
)
⁄= Ch (α)
(k) (λ).
The following lemma compares the highest degree terms of quantities above:
Lemma 8.3. For any integerm ≥ 1 we have that
(51) Ch(1)
(k)
(
Aα(λ)
)
= Ch (α)
(k) (λ) − γ
(
Ch(1)
) (k/2) [k is even]
+ terms of degree less than k with respect to deg4 .
Proof. We know, by Corollary 3.8, that for anyk ≥ 2,
deg1
(
Ch(1)
(k)
(
Aα(λ)
)
− Ch(α)
(k) (λ)
)
= k.
Let us consider its~Chµ expansion:
Ch(1)
(k)
(
Aα(λ)
)
− Ch(α)
(k) (λ) =
∑
µ
ak
µ~Chµ.
Since deg4(~Chµ) ≤ deg1(~Chµ) with equality only for µ = (1 m) for some non-
negative integer m, one has that
Ch(1)
(2m+1)
(
Aα(λ)
)
= Ch (α)
(2m+1)(λ)
+ terms of degree less than 2m + 1 with respect to deg4;
Ch(1)
(2m)
(
Aα(λ)
)
= Ch (α)
(2m)(λ) − a2m
(1m)
(
Ch(1)
) m
+ terms of degree less than 2m with respect to deg4 .
But
a2m
(1m) = [
(
R(α)
2 (λ)
) m
]
(
Ch(α)
(2m)(λ) − Ch(1)
(2m)
(
Aα(λ)
) )
= [Rm
2 ] Ch(α)
(2m)(λ) = γ,
58 M. DOŁ ˛ EGA AND V . FÉRAY
by [Las09, Theorem 10.3] or Proposition A.3 here (the coefﬁcient of Rm
2 in Ch(1)
(2m)
is zero for parity reason). This ﬁnishes our proof. □
Corollary 8.4. One has the following equalities in
(
Λ (α)
⋆
) ext
:
u(α)
k =
Ch(α)
(k+1)
(k + 1)
(
Ch(1)
) (k+1)/2 − γ
k + 1 [k is odd] + terms of negative degree;
(52)
t(α)
k =
Ch(α)
(k−1)
(
Ch(1)
) (k−1)/2 − γ [k is odd] + terms of negative degree.
(53)
Proof. For any Young diagram λ, equation (52) evaluated at λ is obtained from
equation (49) and Lemma 8.3. Similarly, equation (53) is a co nsequence of equa-
tion (50) and Lemma 8.3. □
Now, we will prove that elements of negative degree are asymptotically negligi-
ble.
Lemma 8.5. Let f ∈
(
Λ (α)
⋆
) ext
be a function of degree less than 0. Then, as
n → ∞,
f (λ(n)) d− →0,
where the distribution of λ(n) is Jack measure of size n.
Proof. It is enough to show that, as n → ∞
(54) ~Chµ(λ(n))
(
Ch1(λ(n))
) −m/2 d− →0
for |µ| < m, where the distribution of λ(n) is Jack measure of size n. But this is a
consequence of Theorem 1.2. Indeed, let (Ξ k)k=2,3,... be a family of independent
standard Gaussian random variables. Then Theorem 1.2 states that
~Chµ(λ(n)) n−|µ|/2 d− →
∏
i
√
µi Ξ µi.
As Ch1(λ(n)) ≡ n, this implies (54) and ﬁnishes the proof. □
Finally, Theorem 8.1 follows from Corollary 8.4, Theorem 1.2 and Lemma 8.5.
