---
doc_id: arxiv-hep-th-0006183v1
doc_title: "Fine-tuning and the Wilson renormalization group"
section_id: sec-002-2-renormalization-group-ﬂow
section_title: "Renormalization group ﬂow"
section_number: 2
pages: 3-4
source_pdf: 0006183v1.pdf
source_sha256: 2c9c4d97ce4f71a3
toc_source: inferred
doc_brief: "Fine-tuning and the Wilson renormalization group — We use the Wilson renormalization group (RG) formulation to solve the ﬁne-tuning proce- dure needed in renormalization schemes breaking the gauge"
---
Consider the SU(2) gauge theory described by the classical Lagrangian (in the Feynman
gauge)
SY M =
Z
d4x

−1
4Fµν · F µν −1
2 (∂µAµ)2 −¯c · ∂µDµc

,
where the gauge stress tensor and the covariant derivative are given by Fµν = ∂µAν −
∂νAµ + g Aµ ∧Aν, Dµc = ∂µc + g Aµ ∧c and we have introduced the usual scalar and
external SU(2) products. This action is invariant under the BRS transformation [9]
δAa
µ = 1
gη Dab
µ cb ,
δca = −1
2 η ǫabccb cc ,
δ¯ca = −1
g η ∂µAa
µ
with η a Grassmann parameter.
Introducing the sources ua
µ, va associated to the variations of Aa
µ, ca respectively one
has the BRS action [9]
SBRS[Φ, γ] = SY M +
Z
d4x
1
gua
µDab
µ cb −1
2ǫabcva cb cc

(1)
where we have denoted by Φ and γ the ﬁelds and the BRS sources
ΦI = { Aa
µ, ca, ¯ca} ,
γi = {wa
µ, va} ,
and wa
µ = ua
µ + g∂µ¯ca (no source is introduced for ¯ca).
According to Wilson [1, 2] the ﬁelds with frequencies Λ2 < p2 < Λ2
0 are integrated in
the path integral giving
Z[J, γ] = N[J; Λ, Λ0]
Z
DΦ exp i{−1
2(Φ D−1Φ)0Λ + (JΦ)0Λ + Seﬀ[Φ, γ; Λ, Λ0] } ,
(2)
where N[J; Λ, Λ0] contributes to the quadratic part of Z[J, γ] and the functional Seﬀis the
Wilsonian eﬀective action which is the generator of the connected amputated cutoﬀGreen
functions (except the tree-level two-point function). Seﬀcontains cutoﬀpropagators DΛΛ0
given by the free propagators D(p) multiplied by a cutoﬀfunction KΛΛ0 which is one for
Λ2 ∼< p2 ∼< Λ2
0 and rapidly vanishes outside. In (2) we have also introduced the cutoﬀscalar
products between ﬁelds and sources
1
2(Φ D−1Φ)ΛΛ0 ≡
Z
p
K−1
ΛΛ0(p) p2  1
2Aa
µ(−p) Aa
µ(p) −¯ca(−p) ca(p)
	
,
Z
p
≡
Z
d4p
(2π)4 ,
(JΦ)ΛΛ0 ≡
Z
p
K−1
ΛΛ0(p)

ja
µ(−p) Aa
µ(p) + [¯χa(−p) −i
gpµua
µ(−p)] ca(p) + ¯ca(−p) χa(p)

.
Notice that at Λ = Λ0 the Wilsonian eﬀective action coincides with the bare action.
The requirement that Z[J, γ] is independent of the infrared cutoﬀΛ can be translated
into a ﬂow equation for Seﬀ, referred to as the exact RG equation. For our purposes it is
convenient to perform a Legendre transform on Seﬀin order to obtain the so-called “cutoﬀ
eﬀective action” Γ[Φ, γ; Λ, Λ0], which is the generator of 1PI cutoﬀvertex functions and
2
reduces to the physical quantum eﬀective action in the limits Λ →0 and Λ0 →∞. The
ﬂow equation can be written as [10]-[12]
Λ∂Λ Π[Φ, γ; Λ, Λ0] = −i
2
Z
q
hΛ∂D−1
ΛΛ0(q)
∂Λ
i
AB (−1)δA
h δ2Γ[Φ, γ; Λ, Λ0]
δΦA(q)δΦB(−q)
i−1
,
(3)
where δA = 1 if ΦA is a fermionic ﬁeld and 0 otherwise and
Π[Φ, γ; Λ, Λ0] = Γ[Φ, γ; Λ, Λ0] + 1
2(Φ, D−1Φ)ΛΛ0 −1
2(Φ, D−1Φ)0Λ0 .
(4)
This equation can be integrated by giving boundary conditions in Λ. In order to set them
we distinguish between relevant couplings and irrelevant vertices according to their mass
dimension. Relevant couplings have non-negative mass dimension and are deﬁned as the
value of some vertices and their derivatives at a given normalization point (see [4] for their
deﬁnition). For the SU(2) theory there are nine relevant couplings which are the coeﬃcients
of the following monomials
1
2Aµ(gµν∂2 −∂µ∂ν) · Aν ,
wµ · ∂µ c ,
1
2Aµ · Aµ ,
1
2(∂µAµ)2 ,
(∂νAµ) · Aµ ∧Aν ,
wµ · c ∧Aµ ,
1
2v · c ∧c ,
(5)
1
4(Aµ ∧Aν) · (Aµ ∧Aν) ,
1
4(Aµ · Aν) · (Aµ · Aν) .
To set the boundary conditions, one observes that the cutoﬀeﬀective action Γ[Φ, γ; Λ, Λ0]
at Λ = Λ0 becomes the bare action and to ensure perturbative renormalizability it must
be local, thus irrelevant vertices must vanish at Λ = Λ0. As far as the relevant couplings,
the boundary conditions must provide the physical coupling g(µ) and guarantee symmetry.
In fact the cutoﬀΛ explicitly breaks gauge invariance and one has to show that at the
physical point Λ = 0 and Λ0 →∞the Slavnov-Taylor identity can be recovered. As shown
in refs. [3, 4] the symmetry is ensured if the relevant couplings are properly ﬁxed at some
value of Λ. In the next section we brieﬂy recall how this procedure can be implemented.
Once the boundary conditions are given, equation (3) can be thought as an alternative
deﬁnition of the theory which in principle is non-perturbative. On the other hand the
iterative solution of (3) reproduces the usual loop expansion and, as shown by Polchinski [2],
the Λ0 →∞limit of Γ[Φ, γ; Λ, Λ0] is ﬁnite for all values of Λ 1. In the following this limit
will be taken and Γ[Φ, γ; Λ, ∞] will be denoted by Γ[Φ, γ; Λ]. Notice that, once this limit
has been performed, the irrelevant vertices of Γ[Φ, γ; Λ] do not vanish at Λ = Λ0 but are
only suppressed by inverse powers of Λ0.
