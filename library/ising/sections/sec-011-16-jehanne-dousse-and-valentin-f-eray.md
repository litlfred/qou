---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-011-16-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 16
pages: 16-16
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
Thus|κβ,0 (σj;j∈A)|≤ Dre
−cdβ𝓁T (A)
2 , as claimed. □
3.3. With a strong magnetic ﬁeld. The last regime we consider is the Ising model with a strong
magnetic ﬁeld, i.e. h is bigger than some value h1 > 0 (h1 is to be determined later). The case of
negativeh (smaller than−h1 < 0) is obviously symmetric.
In this regime, there is also a well-known cluster expansion for the partition function [13, Section
5.7]. Let us present it brieﬂy.
Fix Λ ⊂ Zd and consider the Ising model on Λ with + boundary conditions. We ﬁrst write its
partition function in a suitable form. For a subset Λ − of Λ, we denote
δeΛ− ={{i,j}∈E b
Λ, i∈ Λ−, j /∈ Λ−}.
Deﬁne also W(Λ−) = exp(−2β|δeΛ−|− 2h|Λ−|). Then we have:
Lemma 3.11 (strong magnetic ﬁeld representation). With the above notation,
Z+
Λ,β,h = exp
(
β|Eb
Λ| +h|Λ|
)

 ∑
Λ−⊆Λ
W(Λ−)

.
Proof: The proof is not diﬃcult and can be found, e.g., in [13, Section 5.7]. It is important to
note that the sum over Λ −⊆ Λ corresponds to the sum over spin conﬁgurations in the deﬁnition of
the partition function: the correspondence simply associates with a spin conﬁguration the set Λ − of
positions of its minus spins. □
Let A be a subset of Λ. It is straightforward to modify the argument to ﬁnd a similar expression for
the numerator of⟨σA⟩ (as in Section 3.2) or of
⟨
exp
(∑
i∈Atiσi
)⟩
(as in Section 3.1).
(3.9)
∑
ω∈ΩΛ
σA(ω) exp
(
−H+
Λ;β,h(ω)
)
= exp
(
β|Eb
Λ| +h|Λ|
)

 ∑
Λ−⊆Λ
(−1)|A∩Λ−| W(Λ−)

.
(3.10)
∑
ω∈ΩΛ
exp
(
−H+
Λ;β,h(ω) +
∑
i∈A
tiσi
)
= exp
(
β|Eb
Λ| +h|Λ| +
∑
i∈A
ti
)
 ∑
Λ−⊆Λ
[ ∏
i∈A∩Λ−
exp(−2ti)
]
W(Λ−)

.
A set Λ−⊆ Λ can be seen as a subgraph of the lattice Zd. As such, it admits a unique decomposition
as disjoint union of its connected components Λ− =S1⊔S2⊔···⊔ Sr. The weight W behaves multi-
plicatively with respect to this decomposition W(Λ−) =∏r
i=1 W(Si); the same is true for the modiﬁed
weights (−1)|A∩Λ−| W(Λ−) and
[∏
i∈A∩Λ− exp(−2ti)
]
W(Λ−) which appear in Eqs. (3.9) and (3.10)
above. This enables us to use the technique of cluster expansion.
The convergence of this cluster expansion is proved for the partition function in [13, Section 5.7].
The argument can be directly adapted to get a cluster expansion of the expression in Eqs. (3.9)
and (3.10) above. The same reasoning as in Section 3.1 or in Section 3.2 leads to similar bounds on
joint cumulants, which proves Theorem 1.1 in the strong magnetic ﬁeld regime.
