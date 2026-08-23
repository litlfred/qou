---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-008-23-the-q-borel-and-the-q-laplace-transforms
section_title: "The q-Borel and the q-Laplace transforms"
section_number: 2.3
pages: 14-17
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
Bκ (for a rational number κ) deﬁned by
Bκ
( ∞∑
ℓ=0
aℓtℓ
)
(ξ, q) =
∞∑
ℓ=0
(−1)ℓqκℓ(ℓ+1)/2aℓξℓ . (55)
Its role is to convert divergent series, e.g., of the form ∑ ∞
ℓ=0 q−κℓ(ℓ+1)/2aℓtℓ (where aℓ is
bounded and κ > 0) to convergent ones at ξ = 0.
An inverse of the q-Borel transform is the q-Laplace transform, whose role is to construct
analytic solutions to the linear q-diﬀerence equation with prescribed asymptotics. It is
deﬁned for κ > 0 by
Lκ(f )(t, λ, q) = 1
θ(λ; qκ)
∑
ℓ∈/CI
(−1)ℓqκℓ(ℓ+1)/2λℓf (qκℓλt, q) =
∑
ℓ∈/CI
f (qκℓλt, q)
θ(qκℓλ; qκ) , (56)
MODULAR q-HOLONOMIC MODULES 15
and for κ < 0, by
Lκ(f )(t, q) =
∮
f (ξ, q)θ(t/ξ; q−κ) dξ
2πiξ . (57)
The q-Laplace transform for positive κ is more common, however, in the computation of the
monodromy of the 4 1 knot, we will use κ < 0, following analogous computations of Morita
[48].
In some sense, the two tranformations are inverse to each other . More precisely, for all κ
and all natural numbers n, we have
LκBκ(tn)(t, λ, q) = tn . (58)
(Interestingly, the right hand side is independent of λ.) Indeed, for κ > 0, we have
LκBκ(tn) = 1
θ(λ; qκ)
∑
ℓ∈/CI
(−1)ℓqκℓ(ℓ+1)/2λℓ(−1)nqκn(n+1)/2qκℓnλntn
= 1
θ(λ; qκ)
∑
ℓ∈/CI
(−1)ℓ+nqκ(ℓ+n)(ℓ+n+1)/2λℓ+ntn
= 1
θ(λ; qκ)
∑
ℓ∈/CI
(−1)ℓqκℓ(ℓ+1)/2λℓtn = tn .
(59)
A similar calculation using the residue theorem shows ( 58) for κ < 0. More generally, the
fact solutions constructed by Borel transforms followed by itera ted Laplace transforms are
asymptotic to the original formal power series is known in the literat ure as Watson’s lemma,
a modern proof of which may be found for instance in Miller [ 46, p. 53, Prop. 2.1]. An
analogous lemma holds for the q-case, see [ 16, Prop.2.9].
By its very deﬁnition, Lκ for κ > 0 depends on the variable λ in an elliptic way
Lκ(f )(t, qκλ, q) = Lκ(f )(t, λ, q) (60)
whereas Lκ for κ < 0 does not involve a variable λ. The next lemma, whose proof follows
from an elementary application of the residue theorem, concerns t he dependence of the
q-Laplace transform on the auxiliary variable λ, and may be of independent interest.
Lemma 2.1. Assuming that
lim
ε→0
∮
|ξ|=ε±
f (ξt, q)θ(µ−1λ−1ξ; q)
θ(ξµ−1; q)θ(ξλ−1; q)
dξ
2πiξ = 0 (61)
where ε avoids the poles of the integrand we have
L1(f )(t, λ, q) − L1(f )(t, µ, q)
= θ(λ−1µ; q)(q; q)3
∞
θ(λ−1; q)θ(µ; q)
∑
x∈poles of f
Resξ=x
f (ξ, q)θ(λ−1µ−1t−1ξ; q)
θ(ξλ−1t−1; q)θ(ξµ−1t−1; q) . (62)
Note that the assumption on f is mild since as t approaches 0 or ∞ bounded away from
the poles, the quotient of θ’s approaches 0. Note also that the lemma can be extended to
the case of Lκ for κ > 0 by substituting q ↦→qκ except in the argument of f .
16 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Proof. We compute
0 =
∑
ξ∈poles
Resξ
f (ξt, q)θ(µ−1λ−1ξ; q)
θ(ξµ−1; q)θ(ξλ−1; q)
dξ
2πiξ
=
∑
k
Resξ=qkλ
f (ξt, q)θ(µ−1λ−1ξ; q)
θ(ξµ−1; q)θ(ξλ−1; q)
dξ
2πiξ +
∑
k
Resξ=qkµ
f (ξt, q)θ(µ−1λ−1ξ; q)
θ(ξµ−1; q)θ(ξλ−1; q)
dξ
2πiξ
+
∑
x∈poles of f
Resξ=t−1x
f (ξt, q)θ(µ−1λ−1ξ; q)
θ(ξµ−1; q)θ(ξλ−1; q)
dξ
2πiξ
=
∑
k
(−1)kqk(k+1)/2λk f (qkλt, q)θ(µ−1; q)
θ(µ−1λ; q)(q; q)3
∞
+
∑
k
(−1)kqk(k+1)/2µk f (qkµt, q)θ(λ−1; q)
θ(µλ−1; q)(q; q)3
∞
+
∑
x∈poles of f
Resξ=t−1x
f (ξt, q)θ(µ−1λ−1ξ; q)
θ(ξµ−1; q)θ(ξλ−1; q)
dξ
2πiξ
= θ(µ−1; q)θ(λ; q)
θ(µ−1λ; q)(q; q)3
∞
L1(f )(t, λ, q) + θ(µ; q)θ(λ−1; q)
θ(µλ−1; q)(q; q)3
∞
L1(f )(t, µ, q)
+
∑
x∈poles of f
Resξ=x
f (ξ, q)θ(µ−1λ−1t−1ξ; q)
θ(ξµ−1t−1; q)θ(ξλ−1t−1; q)
dξ
2πiξ .
(63)
□
This type of residue formula for the Laplace transform is similar to th e deﬁnition of the
Laplace transform for κ < 0. We can ﬁnd a similar expression for a single Laplace transform
using a special function. The Appell-Lerch sum will be studied later in S ection 4.2 but we
will deﬁne it here.
L(t, λ, q) = 1
θ(λ; q)
∑
k∈/CI
(−1)k qk(k+1)/2λk
1 − qkλt . (64)
Using this we have the following integral expression for the Laplace t ransform for κ > 0.
Lemma 2.2. For κ > 0, we have
(Lκf )(t, λ, q) =
∑
k∈/CI
Resξ=qκk L(ξ−1λ−1, λ, qκ)f (ξλt, q) dξ
2πiξ . (65)
Deforming the contour and the residue theorem give the following lem ma.
Lemma 2.3. Assuming that
lim
ε→0
∮
|ξ|=ε±
L(ξ−1λ−1, λ, qκ)f (ξλt, q) dξ
2πiξ = 0 (66)
where ε avoids the poles of the integrand we have
(Lκf )(t, λ, q) = −
∑
x∈poles of f
L(x−1t, λ, q)Resξ=xf (ξ, q) dξ
2πiξ (67)
MODULAR q-HOLONOMIC MODULES 17
Notice that all the dependence on t and λ is now in the arguments of the Appell-Lerch
sums. This illustrates the important role the residues of the Borel t ransform play in the
resummation. An application of this lemma leads to the following remark able formula.
Corollary 2.4.
f (1)(t, λ, q) = −θ(t; q)
∞∑
k=0
(
L(q1/4+k/2t, λ, q1/2)R+(k, q) + L(−q1/4+k/2t, λ, q1/2)R−(k, q)
)
(68)
where f (1) is given in Equation ( 202) and R± is given in Equation ( 232).
