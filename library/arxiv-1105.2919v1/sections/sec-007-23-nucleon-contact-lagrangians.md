---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-007-23-nucleon-contact-lagrangians
section_title: "Nucleon contact Lagrangians"
section_number: 2.3
pages: 15-16
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
Two-nucleon contact interactions consist of four nucleon ﬁelds (four nucleon legs) and no meson ﬁelds.
Such terms are needed to renormalize loop integrals, to make results reasonably independent of regulators,
and to parametrize the unresolved short-distance dynamics of the nuclear force. For more on the role of
contact terms, see Section 4.3.
Because of parity, nucleon contact interactions come only in even powers of derivatives, thus,
ˆLNN = ˆL(0)
NN + ˆL(2)
NN + ˆL(4)
NN +... (2.60)
The lowest order (or leading order) NN Lagrangian has no derivatives and reads [50, 51]
ˆL(0)
NN =−1
2CS ¯NN ¯NN− 1
2CT ( ¯N⃗ σN)· ( ¯N⃗ σN), (2.61)
where N is the heavy baryon nucleon ﬁeld ( ¯N = N†). CS and CT are unknown constants which are
determined by a ﬁt to the NN data. The second order NN Lagrangian can be stated as follows [54]
ˆL(2)
NN = −C′
1
[
( ¯N⃗∇N)2 + (⃗∇NN )2
]
−C′
2( ¯N⃗∇N)· (⃗∇NN )−C′
3 ¯NN
[
¯N⃗∇2N +⃗∇2NN
]
−iC′
4
[
¯N⃗∇N· (⃗∇N×⃗ σN) + (⃗∇N)N· ( ¯N⃗ σ×⃗∇N)
]
−iC′
5 ¯NN (⃗∇N·⃗ σ×⃗∇N)−iC′
6( ¯N⃗ σN)· (⃗∇N×⃗∇N)
− (C′
7δikδjl +C′
8δilδkj +C′
9δijδkl)
[ ¯Nσk∂iN ¯Nσl∂jN +∂iNσkN∂jNσlN
]
− (C′
10δikδjl +C′
11δilδkj +C′
12δijδkl) ¯Nσk∂iN∂jNσlN
−
(1
2C′
13(δikδjl +δilδkj) +C′
14δijδkl
)[
∂iNσk∂jN +∂jNσk∂iN
] ¯NσlN. (2.62)
For a thorough discussion of second order contact Lagrangians, see Refs. [124, 125].
Similar to CS and CT of Eq. (2.61), the C′
i of Eq. (2.62) are unknown constants which are ﬁxed in a ﬁt
to the NN data. Obviously, these contact Lagrangians blow up quite a bit with increasing order, which is
why we do not give ˆL(4)
NN explicitly here. The NN contact potentials that emerge from these Lagrangians
are given in Section 4.3.
Besides the above contact Lagrangians involving two nucleons, there exist contact interactions among
three or more nucleons representing nuclear many-body forces (cf. last term of Eq. (2.66), below, and
Section 5).
2.4. Summary: Eﬀective Lagrangians organized by interaction index ∆
To summarize, the eﬀective Lagrangian needed to derive nuclear forces includes the following parts:
Leﬀ =Lππ +LπN +LNN +..., (2.63)
where the ellipsis stands for terms that involve two nucleons plus pions and three or more nucleons with or
without pions, relevant for nuclear many-body forces (cf. last two terms of Eq. (2.66), below, and Section 5).
In previous sections, we organized the Lagrangians by the number of derivatives or pion-mass insertions.
This is the standard way, appropriate particularly for considerations of π-π andπ-N scattering. As it turns
15
out (cf. Section 3.1), for interactions among nucleons, it is sometimes useful to also consider the so-called
index of the interaction,
∆≡d + n
2− 2, (2.64)
where d is the number of derivatives or pion-mass insertions and n the number of nucleon ﬁeld operators
(nucleon legs). We will now re-write the HB Lagrangian in terms of increasing values of the parameter ∆.
The leading-order Lagrangian reads,
ˆL∆=0 = 1
2∂µπ·∂µπ− 1
2m2
ππ2
+1− 4α
2f2π
(π·∂µπ)(π·∂µπ)− α
f2π
π2∂µπ·∂µπ + 8α− 1
8f2π
m2
ππ4
+ ¯N
[
i∂0− gA
2fπ
τ· (⃗ σ·⃗∇)π− 1
4f2π
τ· (π×∂0π)
]
N
+ ¯N
{gA(4α− 1)
4f3π
(τ·π)
[
π· (⃗ σ·⃗∇)π
]
+ gAα
2f3π
π2
[
τ· (⃗ σ·⃗∇)π
]}
N
−1
2CS ¯NN ¯NN− 1
2CT ( ¯N⃗ σN)· ( ¯N⃗ σN) + ... , (2.65)
and subleading Lagrangians are,
ˆL∆=1 = ¯N
{ ⃗∇2
2MN
− igA
4MNfπ
τ·
[
⃗ σ·
(←
∇∂0π−∂0π
→
∇
)]
− i
8MNf2π
τ·
[←
∇·(π×⃗∇π)− (π×⃗∇π)·
→
∇
]}
N
+ ¯N
[
4c1m2
π− 2c1
f2π
m2
ππ2 +
(
c2− g2
A
8MN
) 1
f2π
(∂0π·∂0π)
+ c3
f2π
(∂µπ·∂µπ)−
(
c4 + 1
4MN
) 1
2f2π
ϵijkϵabcσiτa(∂jπb)(∂kπc)
]
N
− D
4fπ
( ¯NN ) ¯N
[
τ· (⃗ σ·⃗∇)π
]
N− 1
2E( ¯NN )( ¯NτN)· ( ¯NτN) + ... , (2.66)
ˆL∆=2 = L(4)
ππ + ˆL(3)
πN + ˆL(2)
NN + ... , (2.67)
ˆL∆=4 = ˆL(4)
NN + ... , (2.68)
where the ellipses represent terms that are irrelevant for the derivation of nuclear forces up to fourth order.
