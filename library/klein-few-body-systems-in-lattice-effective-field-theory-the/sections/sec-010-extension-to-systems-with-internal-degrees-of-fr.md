---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-010-extension-to-systems-with-internal-degrees-of-fr
section_title: "Extension to systems with internal degrees of freedom and coupled channels"
section_number: null
pages: 23-24
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
As we use nucleons as degrees of freedom, the partial waves must be characterized by their spin and
isospin content as well. This is why Eq. (2.36) does not hold generally for angular momentum larger than
zero, and one has to sum over all magnetic quantum numbers as well. Consequently, the partial waves
are described by orbital angular momentum, its magnetic quantum number and the internal degrees of
freedom spin and isospin, which are summarized in the spin-isospin vectorχi,
Ψ(⃗r) =
∑
i
Ψi
(⃗r) =
∑
l
l∑
lz=−l
∑
i
ui,l,lz(r)
r Yl,lz(θ,φ )χi. (2.48)
Now the radial projected Schrödinger equation reads
− 1
2µ∆r + l(l + 1)
2µr2
 ui,l,lz(r) +
∑
i′,l′,l′
z
V(i, l, lz;, i′, l′, l′
z)ui′,l′,l′
z(r) = Eui,l,lz(r). (2.49)
Here, V(i, l, lz; i′, l′, l′
z) is the projected potential
V(i, l, lz; i′, l′, l′
z) =
⟨
Yl,lz
(θ,φ )χi
⏐⏐⏐⏐ V
⏐⏐⏐⏐Yl′l′
z
(θ,φ )χi′
⟩
. (2.50)
The new radial Schrödinger equation generally couples diﬀerent partial wave channels. In the case of
nucleon-nucleon scattering, we have partial waves with the same total angular momentum j but diﬀerent
orbital angular momentum l, which couple for l = j± 1. Examples are 3S 1−3 D1, 3P2−3 F2 and
3D3−3 G3.
After expanding the wave function with speciﬁc internal degree of freedom i,
Ψi
(⃗r) =
∑
l
∑
lz
ui,l,lz
(r)
r Yl,lz
(θ,φ ), (2.51)
the wave function can be rewritten in terms of the S -matrix,
Ψi′
(⃗r) =δi,i′ exp(iqiz)
+ exp(iqir)
r
∑
l′,l′
z
Yl′,lz′ (θ,φ ) i
∑
l
il−l′
√
π(2l + 1)
qiqi′
(
δi,i′δl,l′δ0,l′
z− S i,l,0;i′,l′,l′
z
)
. (2.52)
Even though the parametrization in the single channel case is straightforward, there are generally two
possibilities in the coupled channel case, the Blatt and Biedenharn parametrization [58, 59] as well as the
17
Chapter 2 Theory
Stapp parametrization [60]. Using the Stapp parametrization, the S-matrix is given by
S =

exp
(
iδ j−1
)
0
0 exp
(
iδ j+1
)


cos
(
2ϵ j
)
i sin
(
2ϵ j
)
−i sin
(
2ϵ j
)
cos
(
2ϵ j
)


exp
(
iδ j−1
)
0
0 exp
(
iδ j+1
)
, (2.53)
whereϵ j is the mixing angle between both channels. Again, the S-matrix can be used to propagate the
incoming wave function Ψin,
Ψin =−
exp
[
−i
(
qr− jπ
2
)]
2iqr

exp
(
−iπ
2
)
0
0 exp
(
iπ
2
)

[C
D
]
, (2.54)
via Eq. (2.31) to the outgoing function Ψout,
Ψout = S Ψin =−
exp
[
−i
(
qr− jπ
2
)]
2iqr
×

C exp
(
iπ
2 + 2iδ j−1
)
cos
(
2ϵ j
)
+ iD exp
(
iπ
2 +δ j−1 +δ j+1
)
sin
(
2ϵ j
)
D exp
(
−iπ
2 + 2iδ j−1
)
cos
(
2ϵ j
)
+ iC exp
(
−iπ
2 +δ j−1 +δ j+1
)
sin
(
2ϵ j
)
.
(2.55)
A more detailed derivation can be found in [61]. After having deﬁned the incoming and outgoing wave
functions, one should follow the procedure in the uncoupled case, where one redeﬁnes the full wave in
terms of a standing wave. Further details for the concrete calculation of phase shifts and mixing angles
are given in Subsec. 3.4.2.
