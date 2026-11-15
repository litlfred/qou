---
doc_id: arxiv-hep-th-0006183v1
doc_title: "Fine-tuning and the Wilson renormalization group"
section_id: sec-003-3-eﬀective-st-identity
section_title: "Eﬀective ST identity"
section_number: 3
pages: 4-5
source_pdf: 0006183v1.pdf
source_sha256: 2c9c4d97ce4f71a3
toc_source: inferred
doc_brief: "Fine-tuning and the Wilson renormalization group — We use the Wilson renormalization group (RG) formulation to solve the ﬁne-tuning proce- dure needed in renormalization schemes breaking the gauge"
---
In the RG formulation the ST identity for the physical eﬀective action Γ[Φ, γ] ≡Γ[Φ, γ; 0, ∞]
is ensured if the cutoﬀeﬀective action satisﬁes a modiﬁed ST [3]-[7]. As usual in studying
1For a generalization of this proof to gauge theories see for instance [4].
3
ST identities, it is convenient to remove from the functional Π given in (4) the gauge ﬁxing
term and introduce the Slavnov operator [13]
SΠ′ = −i
Z
p

δ Π′
δΦi(−p)
δ
δγi(p) + δ Π′
δγi(p)
δ
δΦi(−p)

,
Φi = {Aµ, c}
with
Π′[Φ, γ; Λ] = Π[Φ, γ; Λ] + 1
2
Z
p
pµ pν Aµ(−p) · Aν(p).
The modiﬁed ST identity then reads
∆Γ(Λ) ≡SΠ′Π′[Φ, γ; Λ] + ˆ∆Γ(Λ) = 0 ,
(6)
where
ˆ∆Γ[Φ, γ; Λ] = −ℏ
Z
p,q
K0Λ(p)(−1)δL 
D−1
Λ∞(−p)

Li

δ2Γ[Φ, γ; Λ]
δΦL(−p)δΦJ(−q)
−1
×
δ2
δΦJ(q)δγi(p)

Π[Φ, γ; Λ] −1
g
Z
x
uµ∂µc

.
(7)
The factor ℏhas been inserted to put into evidence that ˆ∆Γ vanishes at tree-level. Notice
that at the physical point Λ = 0 the gauge symmetry condition (6) reduces to the usual ST
identity, since Π becomes the physical eﬀective action and ˆ∆Γ vanishes. It can be shown
that if ∆Γ vanishes up to loop ℓthen at the next loop ∆Γ is Λ-independent and therefore
can be analyzed at every value of Λ. If one imposes (6) at Λ = 0, one gets the boundary
conditions for the relevant part of the eﬀective action given in terms of the physical coupling
g(µ). Alternatively, in (6) one can choose Λ much bigger than all external momenta, namely
Λ = Λ0, and determine the cutoﬀdependent couplings of UV action. Both these procedures
provide the boundary conditions of the RG ﬂow for the non-invariant relevant couplings of
the cutoﬀeﬀective action. We will adopt the latter possibility in the present paper.
At Λ = Λ0 the functional ∆Γ is local, or more precisely, its irrelevant contributions
vanish as inverse powers of Λ0 and disappear in the Λ0 →∞limit (see [6] for a proof).
This is obviously true for the functional SΠ′ Π′(Λ0), due to the boundary conditions imposed
on the irrelevant vertices of Π, and can be shown by a direct calculation for the functional
ˆ∆Γ(Λ0). Therefore in the Λ0 →∞limit the eﬀective ST identity (6) reduces to a ﬁnite
set of equations (the so called ﬁne-tuning equations) obtained by requiring the vanishing
of relevant part of ∆Γ. In fact this system of equations overdetermines the UV couplings
and in order to prove its solvability one must exploit the so-called consistency conditions
which reduce the number of independent equations [3]. In the next section we will solve
these ﬁne-tuning equations at one-loop order tuning the couplings of the UV action at this
order. Besides determining these couplings this calculation provides a direct check of the
solvability of the ﬁne-tuning problem.
