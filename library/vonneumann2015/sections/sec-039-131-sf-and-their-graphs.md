---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-039-131-sf-and-their-graphs
section_title: "S,F and their graphs."
section_number: 13.1
pages: 94-96
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
S,F and their graphs.
Throughout this section M will be a von Neumann algebra on H and Ω∈H
a cyclic and separating vector for M and hence M ′. (The same data as a
faithful normal state.) Let S0 and F0 be the conjugate linear operators with
domains MΩand M ′Ωdeﬁned by S0(xΩ) = x∗Ωand F0(xΩ) = x∗Ωfor
x ∈M and M ′ respectively.
Lemma 13.1.1. In the sense of unbounded operators F0 ⊆S∗
0 and S0 ⊆F ∗
0
so that S0 and F0 have densely deﬁned adjoints and hence are preclosed.
Proof. To show S∗
0(a′Ω) is deﬁned if ⟨S0(aΩ), a′Ω⟩extends to a bounded
conjugate linear map on all of H. But ⟨S0(aΩ), a′Ω⟩= ⟨(a′)∗Ω, aΩ⟩which
is bounded as a function of aΩby Cauchy-Schwartz. Hence a′Ωis in the
domain of S∗
0 and S∗
0(a′Ω) = (a′)∗Ω= F0(a′Ω). Interchanging S0 and F0 we
get the other inclusion.
Deﬁnition 13.1.2. Let S and F be the closures of S0 and F0 respectively.
Let S = J∆1/2 be the polar decomposition of S.
Observe that S0 = S−1
0
so S is injective and S2 = 1 in the sense of
unbounded operators. Thus ∆1/2 has zero kernel, J2 = 1 and J∆1/2J =
∆−1/2. The same goes for F and its polar decomposition, but we shall now
see that F = S∗.
Theorem 13.1.3. (Takesaki,[].) S∗= F, F ∗= S and the graph of S is the
set of all (cΩ, c∗Ω) where c is a closed densely deﬁned operator aﬃliated with
M and Ω∈D(c) ∩D(c∗).
Proof. Let (ξ, F ∗ξ) be in the graph of F ∗. By the deﬁnition of F we know
that ⟨ξ, (a′)∗Ω⟩= ⟨a′Ω, F ∗ξ⟩. Now deﬁne operators a and b with domain
M ′Ωby ax′Ω= x′ξ and bx′Ω= x′F ∗ξ. Then a and b are closable for if x′
and y′ are in M ′ we have
⟨a(x′Ω), y′Ω⟩= ⟨x′ξ, y′Ω⟩= ⟨ξ, (x′)∗y′Ω⟩
94
= ⟨(y′)∗x′Ω, F ∗ξ⟩= ⟨x′Ω, y′F ∗ξ⟩= ⟨x′Ω, b(y′Ω)⟩
so that as before a ⊆b∗and b ⊆a∗.
Let c be the closure of a.
Then cΩ= aΩ= ξ and c∗= a∗⊇b so
c∗Ω= F ∗ξ. Now by construction the domain of a is invariant under the
unitary group of M ′ and on it a commutes with the unitaries in M ′. This
means that c is aﬃliated with M. At this stage we have shown that the graph
of F ∗consists of all (cΩ, c∗Ω) where c is a closed densely deﬁned operator
aﬃliated with M and Ω∈D(c) ∩D(c∗).
We now want to show that the graph of F ∗is contained in the graph of S.
This is not hard. Let c be as above and c =
√
c∗c be its polar decomposition.
Then if fn(t) = t for 0 ≤t ≤n and fn(t) = 0 for t > n we have that
fn(
√
c∗c) →
√
c∗c on any vector in the domain of c, and since c is aﬃliated
with M, fn(
√
c∗c) ∈M so that ufn(
√
c∗c)Ωis in the domain of S and tends
to ξ. Moreover fn(
√
c∗c)u∗Ωtends to c∗Ω= F ∗ξ so (ξ, F ∗ξ) is in the graph
of S.
Thus F ∗⊆S and we have already observed that S ⊆F ∗. Hence S = F ∗
and S∗= F.
Corollary 13.1.4. The polar decomposition of F is J∆−1/2.
We now prove a crucial result connecting M and M ′.
Lemma 13.1.5. Let λ ∈R+ be given. Then for a′ ∈M ′ there is an a ∈M
with aΩin the domain of F and a′Ω= (λS + λ−1F)aΩ.
Proof. Assuming ||a′|| ≤1 we may apply theorem 8.2.1 to the ψ deﬁned by
ψ(x) = ⟨xΩ, a′Ω⟩and φ(x) = ⟨xΩ, Ω⟩to obtain the existence of an a ∈M
with
⟨xΩ, a′Ω⟩= λ⟨axΩ, Ω⟩+ λ−1⟨xaΩ, Ω⟩
= λ⟨xΩ, a∗Ω⟩+ λ−1⟨aΩ, x∗Ω⟩.
Provided aΩis in the domain of F this equation reads a′Ω= (λS +λ−1F)aΩ.
On the other hand rearranging the equation gives
⟨aΩ, x∗Ω⟩= λ⟨xΩ, a′Ω−λa∗Ω⟩
so by Cauchy Schwartz aΩis in the domain of F = S∗.
Corollary 13.1.6. For each ξ ∈D(∆1/2) ∩D(∆−1/2) there is a sequence
an ∈M with anΩ→ξ,
∆1/2anΩ→∆1/2ξ and ∆−1/2anΩ→∆−1/2ξ.
95
Proof. Set η = (S + F)ξ and choose a sequence a′
n ∈M ′ with a′
n →η. By
the previous lemma there are an ∈M with (S + F)anΩ= a′
nΩ. But S +
F = J(∆1/2 + ∆−1/2) has bounded inverse (in the usual sense of unbounded
operators) so put ξn = (S + F)−1(a′
nΩ). So anΩ= (S + F)−1a′
nΩ→ξ.
Moreover
∆1/2anΩ= ∆1/2(∆1/2 + ∆−1/2)−1Ja′
nΩ
and ∆1/2(∆1/2 + ∆−1/2)−1 is bounded by spectral theory. So ∆1/2anΩ→
∆1/2(S + F)−1(S + F)ξ = ∆1/2ξ. In the same way ∆−1/2anΩ→∆−1/2ξ.
We put everything together with a lemma linking M and M ′ on a dense
subspace to which many functions of ∆can be applied.
Lemma 13.1.7. If ξ and η are in D(S) ∩D(F), a′, λ and a as in 13.1.5,
then
λ⟨SaSξ, η⟩+ λ−1⟨FaFξ, η⟩= ⟨a′ξ, η⟩.
Proof. By moving one S and F to the other side of the inner products, we
see by the previous lemma that we may assume ξ and η are xΩand yΩ
respectively, both in D(F), for x and y in M. But on MΩ, SaS acts by right
multiplication by a∗so ⟨SaSξ, η⟩= ⟨xa∗Ω, yΩ⟩= ⟨SaΩ, x∗yΩ⟩. On the other
hand, systematically using F ∗= S we obtain ⟨FaFxΩ, yΩ⟩= ⟨y∗xΩ, aΩ⟩=
⟨Sx∗yΩ, aΩ⟩= ⟨FaΩ, x∗yΩ⟩. Combining these two we see
λ⟨SaSξ, η⟩+ λ−1⟨FaFξ, η⟩= ⟨(λSa + λ−1Fa)Ω, x∗yΩ⟩.
But by 13.1.5 this is ⟨a′Ω, x∗yΩ⟩= ⟨a′ξ, η⟩.
