---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-045-appendix-a1-notation-and-conventions
section_title: "Appendix A.1 Notation and conventions"
section_number: null
pages: 59-61
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The contravariant space-time four-vector is given by
xµ = (t,⃗x)
(A.1)
and the four-momentum vector reads
pµ = (E,⃗p) .
(A.2)
We use units such that ℏ= c = 1.
Greek indices µ, ν, etc. run over the four space-time coordinate labels 0, 1, 2, 3, with x0 = t the time
coordinate. Latin indices i, j, k, and so on run over the three space coordinate labels 1, 2, 3. The metric is
diagonal with
gµν = gµν =




1
0
−1
−1
0
−1




(A.3)
and the covariant versions of the above-mentioned vectors are
xµ = gµνxν = (t, −⃗x) ,
pµ = gµνpν = (E, −⃗p) ,
(A.4)
where summation over repeated indices is always understood; also
x2 = xµxµ = t2 −⃗x2 .
(A.5)
While for an ordinary three-vector we have, in general,⃗x = (x1, x2, x3), there is caution in place with the
(three-dimensional) nabla operator which is deﬁned to be⃗
∇= (∇1, ∇2, ∇3) =
 ∂
∂xi

= (∂i) =

−∂
∂xi

= (−∂i)
(A.6)
The four-momentum operator reads
pµ
=
i ∂
∂xµ
= i∂µ =

i∂0, −i⃗∇

=

i ∂
∂t,⃗p

,
(A.7)
pµ
=
i ∂
∂xµ = i∂µ =

i∂0, i⃗∇

=

i ∂
∂t, −⃗p

.
(A.8)
The relativistic nucleon ﬁeld satisﬁes the free Dirac equation
(p/ −MN) Ψ(x) ≡(γµpµ −MN) Ψ(x) = 0
(A.9)
where MN denotes the nucleon mass and γµ the Dirac matrices which we apply in Dirac-Pauli representation
γ0 =
 I
0
0
−I

γi =

0
σi
−σi
0

(A.10)
with I the two-dimensional identity matrix and σi the Pauli matrices
σ1 =

0
1
1
0

σ2 =
 0
−i
i
0

σ3 =
 1
0
0
−1

.
(A.11)
59

σi, σj
=
σiσj −σjσi = 2iϵijkσk ,
{σi, σj} = σiσj + σjσi = 2δij ,
(A.12)
σiσj
=
iϵijkσk + δij ,
(A.13)
with
ϵijk =



+1
if (i, j, k) even permutation of (1, 2, 3)
−1
if odd permutation
0
otherwise
(A.14)
Following convention, we denote the Pauli matrices by τ a (a = 1, 2, 3) when operating in isospin space, with
τ aτ b = iϵabcτ c + δab .
(A.15)
Notice that, for isospin components, it does not make sense to distinguish between upper and lower indices
and, therefore, subscripts and superscripts have the same meaning.
The Dirac matrices have the properties
{γµ, γν} = 2 gµν ,
γ0† = γ0γ0γ0 = γ0 ,
γi† = γ0γiγ0 = −γi .
(A.16)
The γ5-matrix is deﬁned by
γ5 = γ5 = iγ0γ1γ2γ3 =
 0
I
I
0

.
(A.17)
{γµ, γ5} = 0 ,
(γ5)2 = 1 ,
γ5† = γ5 .
(A.18)
Commutator of γ matrices:
σµν = i
2 [γµ, γν] ,
γµγν = gµν −iσµν ,
(A.19)
σij = ϵijk
 σk
0
0
σk

,
σ0i = i
 0
σi
σi
0

= −σi0
(A.20)
The relativistic Dirac ﬁeld for positive-energy nucleons is
Ψ(x) =
X
s,t
Z
d3p
(2π)3/2
s
MN
Ep
u(⃗p, s) ξt e−ip·x b(⃗p, s, t)
(A.21)
with the Dirac spinor given by
u(⃗p, s) =
r
Ep + MN
2MN
 
I⃗
σ·⃗p
Ep+MN
!
χs
(A.22)
where Ep = p0 =
p⃗
p2 + M 2
N. The Pauli spinors χs and ξt describe, respectively, the spin and isospin of the
nucleon. Further, b(⃗p, s, t) and b†(⃗p, s, t) are destruction and creation operators for a nucleon with momentum⃗
p, and spin and isospin quantum numbers s and t, respectively. They satisfy the anti-commutation relations

b(⃗p, s, t), b†(⃗p ′, s′, t′)
	
= δs,s′δt,t′δ3(⃗p −⃗p ′) ,
(A.23)
{b(⃗p, s, t), b(⃗p ′, s′, t′)} =

b†(⃗p, s, t), b†(⃗p ′, s′, t′)
	
= 0 .
(A.24)
¯Ψ ≡Ψ†γ0
(A.25)
In the heavy-baryon formalism, the free ﬁeld equation for nucleons is, in leading order and using vµ =
(1, 0, 0, 0),
i∂0N(x) = 0
(A.26)
60
and the nucleon ﬁeld is
N(x) =
X
s,t
Z
d3l
(2π)3/2 χs ξt e−il·x b(⃗l, s, t)
(A.27)
where l0 = 0 at leading order and⃗l2/2MN at NLO.
¯N ≡N †γ0 = N †
(A.28)
The pion ﬁelds are in terms of their cartesian components (i = 1, 2, 3; no distinction between upper and
lower index i)
πi(x) =
Z
d3q
(2π)3/2
1
√
2ω
h
e−iq·xai(⃗q) + eiq·xa†
i(⃗q)
i
(A.29)
where ω = q0 =
p⃗
q2 + m2π and ai and a†
i are, respectively, the destruction and creation operators obeying
the commutation relations
h
ai(⃗q), a†
j(⃗q ′)
i
= δijδ3(⃗q −⃗q ′) ,
(A.30)
[ai(⃗q), aj(⃗q ′)] =
h
a†
i(⃗q), a†
j(⃗q ′)
i
= 0 .
(A.31)
The charged and neutral pion ﬁelds are given by
π+
=
1
√
2 (π1 + iπ2) ,
(A.32)
π−
=
1
√
2 (π1 −iπ2) ,
(A.33)
π0
=
π3 .
(A.34)
Throughout this article, we state amplitudes in terms of the “potential” V which is deﬁned by
V = i M
(A.35)
where M is the invariant amplitude, calculated according to Feynman rules. The relation of M to the
S-matrix is
⟨p1
′p2
′|S|p1p2⟩
=
δ3(⃗p1 −⃗p1
′) δ3(⃗p2 −⃗p2
′)
+ (2π)4 δ4(p1 + p2 −p1
′ −p2
′)
1
(2π)6

M 4
N
E′
1E′
2E1E2
 1
2
× M(p1
′, p2
′; p1, p2) .
(A.36)
