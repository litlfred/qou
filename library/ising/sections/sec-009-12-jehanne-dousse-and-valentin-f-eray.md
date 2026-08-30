---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-009-12-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 12
pages: 12-14
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
This uses the same argument as in [13, Eq. (5.29)]:
∑
X: x1∈X
|ϕ(X)|
r∏
i=1
W(β′,h1)(Ei,Bi)≤
∑
r≥1
r
∑
(E1,B1):
x1∈V (E1,B1)
∑
(E2,B2),...,(Er,Br)
⏐⏐ϕ((Ei,Bi)i≤s)
⏐⏐
r∏
i=1
W(β′,h1)(Ei,Bi)
≤
∑
(E1,B1):
x1∈V (E1,B1)
W(β′,h1)(E1,B 1)e|V (E1,B1)|≤|V (∅,{x1})| = 1,
where we used Lemma 3.3 and [13, Theorem 5.4]. This proves (3.6).
Let us ﬁx a value β′ as above. There exists a constant ε< 1 such that for β small enough, we have
tanhβ <ε tanhβ′. We can now write, for β small enough and|h|≤ h1,
∑
X: x1∈Xand e(X)≥R
|ϕ(X)| (tanhβ)e(X)| tanhβh|b(X)
≤εR ∑
X: x1∈Xand e(X)≥R
|ϕ(X)| (tanhβ′)e(X)(tanhβ′h1)b(X)≤εR,
where the last inequality uses (3.6). This ends the proof of the lemma. □
Combining Eq. (3.5) and Lemma 3.6, we get the desired bound: for β≤βht
jc (d),
|κβ,h(σx1,...,σ xr)|≤ ε𝓁T (A).
3.2. At very low temperature, without magnetic ﬁeld.
3.2.1. The cluster expansion of the partition function. We now turn to the regime without magnetic
ﬁeld (h = 0) and very low temperature (β large). Intuitively, in that case, the spin conﬁgurations with
fewer pairs of neighbours having opposite spins appear with higher probability. To emphasize the role
of these pairs, we rewrite the Hamiltonian as follows:
Hη
Λ;β,0(ω) =−β|Eη
Λ|− β
∑
{i,j}∈Eη
Λ
(σi(ω)σj(ω)− 1).
The only non-zero terms in the sum are those where two neighbours i and j have opposite spins. Let
us consider a ﬁnite subset Λ ⊂ Zd with + boundary condition. A typical spin conﬁguration will then
look as a sea of +’s with some islands of −’s. Therefore the interesting macroscopic components for
the cluster expansion in that case are the frontiers between the areas of +’s and those of −’s, which
are called contours. Let us deﬁne them more rigorously.
Given ω∈ Ω+
Λ, let Λ−(ω) denote the set of lattice points i where σi(ω) =−1. For each i∈ Zd we
deﬁneSi :=i + [−1
2 , 1
2]d to be the unit cube of Rd centred at i. Now let
U(ω) :=
⋃
i∈Λ−(ω)
Si,
and consider the set of maximal connected components of the boundary of U(ω), which we denote
Γ′(ω) ={γ1,...,γ r}.
Each of the γi’s is a contour of ω. Contours are connected sets of closed ( d− 1)-dimensional faces of
the cubesSi. We denote by|γi| the number of such faces inγi. Let Γ Λ :={γ∈ Γ′(ω) :ω∈ Ω+
Λ} denote
the set of all possible contours in Λ . Finally, a collection of contours Γ′⊂ ΓΛ is said to be admissible
if there exists a spin conﬁguration ω∈ Ω+
Λ such that Γ′(ω) = Γ′.
We say that Λ is c-connected if Rd\⋃
i∈ΛSi is connected, which we will assume from now on in this
paper. Then, according to [13, eq (5.42)], the partition function can be rewritten as
Z+
Λ;β,0 =eβ|E+
Λ| Ξ+
Λ;β,0,
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 13
where
Ξ+
Λ;β,0 :=
∑
Γ′⊂ΓΛadmissible
∏
γ∈Γ′
e−2β|γ|.
The cluster expansion is an expression of log Ξ +
Λ;β,0 as an absolutely convergent series. In this case,
an (ordered) cluster is a list X = (γ1,...,γ s) of contours. We denote by X the support of X, ie
X =∪γ∈Xγ. In the following we write X⊆ Λ to say that X⊆∪ i∈ΛSi as subsets of Rd.
In can be shown (see e.g. [13, Chapter 5]) that the cluster expansion converges for β large enough.
Proposition 3.7. There exists βlt
ce(d) such that for all β >βlt
ce(d),
log Ξ+
Λ;β,0 =
∑
X:X⊆Λ
ϕ(X)e−2β ∑s
i=1|γi|,
where
ϕ(γ1,...,γ s) = 1
s!
∑
G⊆Gsconnected
∏
{i,j}∈G
ζ(γi,γj),
ζ(γi,γj) :=
{
0 if γi∩γj =∅,
−1 otherwise,
and Gs denotes as above the complete graph on s vertices.
3.2.2. Bounds on joint cumulants. This cluster expansion can be used to compute expectations and
therefore deduce some bounds on joint cumulants.
Let A⊆ Λ and let us deﬁne σA :=∏
i∈Aσi. Its expectation is given by
⟨σA⟩+
Λ;β,0 =
∑
ω∈Ω+
Λ
σA(ω)e−HΛ;β,0(ω)
Z+
Λ;β,0
.
For any spin conﬁguration ω∈ Ω+
Λ and any contour γ∈ Γ′(ω), let us deﬁne the interior of γ (written
Int(γ)) as the set of points of Λ which would have spin −1 if γ was the only contour of ω. We also
write Int(X) :=⋃
γ∈X Int(γ) for any collection X of contours. Thus for any ω∈ Ω+
Λ and any i∈ Λ,
σi(ω) = (−1)|{γ∈Γ′(ω):i∈Int(γ)}|,
and thus
σA(ω) = (−1)
∑
i∈A|{γ∈Γ′(ω):i∈Int(γ)}|
= (−1)
∑
γ∈Γ′(ω)|{i∈A:i∈Int(γ)}|.
Therefore one can write
⟨σA⟩+
Λ;β,0 =
Ξ+,A
Λ;β,0
Ξ+
Λ;β,0
,
where
Ξ+,A
Λ;β,0 :=
∑
Γ′⊆ΓΛadmissible
∏
γ∈Γ′
(−1)|{i∈A:i∈Int(γ)}|e−2β|γ|.
The cluster expansion of log Ξ +,A
Λ;β,0 converges, which means that we have an analogue of Proposition
3.7 for Ξ +,A
Λ;β,0, replacing e−2β|γ| by (−1)|{i∈A:i∈Int(γ)}|e−2β|γ|. Thus⟨σA⟩+
Λ;β,0 can be expressed as
⟨σA⟩+
Λ;β,0 = exp

 ∑
X:X⊆Λ
ΨA
β (X)−
∑
X:X⊆Λ
Ψ∅
β(X)

,
where for a cluster X = (γ1,...,γ s),
ΨA
β (X) :=ϕ(X) (−1)
∑r
j=1|{i∈A:i∈Int(γj)}|e−2β ∑r
j=1|γj|.
