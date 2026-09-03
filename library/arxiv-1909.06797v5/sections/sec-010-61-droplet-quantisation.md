---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-010-61-droplet-quantisation
section_title: "Droplet quantisation"
section_number: 6.1
pages: 19-25
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
---
The single particle Hamiltonian (2.16) is not in diagonal form. We deﬁne a new variable
¯h = h− S (θ). (6.1)
In terms of this new variables (¯h,θ ) the Hamiltonian density is given by
h(¯h,θ ) =
¯h2
2 − π2
2ρ(θ)2 (6.2)
5Please note the diﬀerence in notation. Here u is Young diagram density and h is hook number.
19
and the droplet boundary is given by
¯h±(θ) =±πρ(θ). (6.3)
The phase space Hamiltonian (2.18) can be calculated by integrating over ¯h from ¯h−(θ) to ¯h+(θ)
and is given by,
Hh = 1
3πℏ
∫
dθπ 3ρ(θ)3. (6.4)
The phase space boundary is doubly degenerate, i.e. for a given θ there are two boundaries, ¯h±
corresponding to two signs on the right hand side of (6.3). Hence, we write the Hamiltonian (6.4)
over the two segments of droplets [45]
Hh = 1
6πℏ
[∫
+
dθ ¯h3
+(t,θ )−
∫
−
dθ ¯h3
−(t,θ )
]
. (6.5)
From the single particle Hamiltonian (6.2) we ﬁnd that the equations of motion satisﬁed by the
droplet boundaries are given by6,
˙¯h±(t,θ ) = ¯h±(t,θ )¯h′
±(t,θ ) (6.7)
where the dot and prime denote derivative with respect to t andθ respectively 7.
In order to quantise the droplets we ﬁnd a simplectic form such that the Hamilton’s equation
˙¯h±(t,θ ) ={¯h±(t,θ ), Hh} (6.8)
would coincide with (6.7) [45, 49]. To achieve the above goal we introduce Poisson brackets
between ¯h±(t,θ ) and ¯h±(t,θ′)
{¯h±(t,θ ), ¯h±(t,θ′)} =±πℏδ′(θ−θ′) and {¯h+(t,θ ), ¯h−(t,θ′)} = 0. (6.9)
6Equations of motion from (6.2) are given by
˙¯h(t) =−∂h
∂θ =π2ρ(θ)ρ′(θ), ˙θ(t) = ∂h
∂¯h = ¯h(t) (6.6)
Substituting the boundary relations (6.3) in these equations, one ﬁnds (6.7).
7At this point one should note that (6.7) is in the standard from of an inviscid Burger’s equation, which is a KdV
type equation. The appearance of KdV type equations is quite common in random matrix theories which indicates that
the problem is exactly solvable. For the Fermi ﬂuid picture that appears in the context of unitary matrix model one can
actually construct an inﬁnite set of commuting Hamiltonians/conserved charges [46, 47], signifying the integrability
of the system. In fact, in [47] the authors have used analogous variables of (2.9) to deduce the Lax pairs with the
same Hamiltonian as (6.5). Further, the commuting Hamiltonians described in [47, 48] can be shown to be similar to
diﬀerent moments of the diagram (3.15) and the resolvent (5.13) or similarly the moment generating function (3.16)
includes information about the full spectrum of the Hamiltonians. Therefore from the integrability structure emergent
from the matrix model side one can show that all the moments of the diagram as described by [5] is conserved. In
the current context we are interested in canonically quantising the droplets, rather than looking at the underlying
integrability structure of (6.5).
20
It is easy to check that using these Poisson brackets, equation (6.8) boils down to (6.7). Also,
{Hh,A} = 0 (6.10)
where
A =
∫ π
−π
dθ (h+(t,θ )− h−(t,θ )) (6.11)
is the area of the phase space droplets. This implies that the area is preserved under classical time
evolution.
The circular droplet (ρ(θ) = 1
2π) corresponds to ¯h±(t,θ ) =± 1
2 and satisfy the classical equations of
motion (6.7). We consider quantum ﬂuctuations about this classical circular droplet
¯h±(t,θ ) =±1
2 + ℏ ˜h±(t,θ ). (6.12)
We also assume that the ﬂuctuations preserve the total area of the droplet. This implies that
∫ π
−π
dθ(˜h+(t,θ )− ˜h−(t,θ )) = 0. (6.13)
The Hamiltonian (6.5) for these ﬂuctuations is given by
Hh = 1
12ℏ + ℏ
4π
∫ π
−π
(˜h2
+(t,θ ) + ˜h2
−(t,θ )
)
dθ + ℏ2
6π
∫ π
−π
(˜h3
+(t,θ )− ˜h3
−(t,θ )
)
dθ. (6.14)
From equation (6.9), we ﬁnd that the Poisson bracket for ˜h±(t,θ ) are given by
{˜h±(t,θ ), ˜h±(t,θ′)} =±π
ℏδ′(θ−θ′) and {˜h+(t,θ ), ˜h−(t,θ′)} = 0. (6.15)
To quantise the above classical system we promote the Poisson brackets (6.15) to commutation
relations [˜h±(t,θ ), ˜h±(t,θ′)
]
=±πiδ′(θ−θ′) and [ ˜h+(t,θ ), ˜h−(t,θ′)] = 0. (6.16)
We decompose ˜h±(t,θ ) into Fourier modes
˜h+(t,θ ) =
∞∑
n=−∞
a−n(t)einθ (6.17)
and
˜h−(t,θ ) =−
∞∑
n=−∞
bn(t)einθ. (6.18)
From the constraint equation (6.13), we see that the zero-modes a0 and b0 are equal up to a
sign
a0 =−b0 =π0. (6.19)
21
It follows from equation (6.15) that the Fourier modes an and bn satisfy U(1) Kac-Moody alge-
bra
[am(t), an(t)] = 1
2mδm+n, [bm(t), bn(t)] = 1
2mδm+n, and [ am(t), bn(t)] = 0. (6.20)
Since ˜h±(t,θ ) are real we have a−n = a†
n and b−n = b†
n. The Hamiltonian (6.14) in terms of these
modes is given by (up to over all constant factors)
˜H = H+ + H− (6.21)
where
H+ =ℏ
2 a2
0 + ℏ2
3 a3
0− ℏ2
24 a0 + ℏ(1 + 2ℏa0)
∑
n>0
a†
nan
+ ℏ2
∑
m,n>0
(
a†
m+naman + h.c.
) (6.22)
and H− has a similar expression in terms of modes bn’s.
Sinceπ0 commutes with all the an, bn and hence with ˜H, application of an’s andbn’s cannot change
the eigenvalue of π0. Therefore the Hilbert space is constructed upon a one parameter family of
vacua|s, s⟩≡| s⟩ where,
an|s⟩ = 0, bn|s⟩ = 0 for n> 0
and a0|s⟩ =−b0|s⟩ =π0|s⟩ = s|s⟩. (6.23)
Starting with the primary|s⟩ we can now construct a Hilbert spaceH which is a s charged module.
Let us denote H+ andH− as Hilbert spaces associated with a and b sectors respectively. The
commutativity of a and b operators implies that the full Hilbert space is factorizable intoH+ and
H− i.e.H =H+⊗H−.
A generic excited state inH is given by
|⃗k,⃗l⟩ =
∞∏
n,m=1
(
a†
n
)kn (
b†
m
)lm
|s⟩. (6.24)
The⃗k and⃗l vectors correspond to excitations in the upper and lower Fermi surfaces. Since an and
bn commute, generic excitation|⃗k,⃗l⟩∈H can be written as a direct product of states belonging to
the two sectors i.e.|⃗k,⃗l⟩ =|⃗k⟩⊗|⃗l⟩.
The excited states inH+ are orthogonal with the normalization
⟨⃗k′|⃗k⟩ = z⃗kδ⃗k⃗k′ where z⃗k =
∏
j
k j!
( j
2
)k j
(6.25)
22
and hasπ0 eigenvalue s. They also satisfy the completeness relation
∑
⃗k
1
z⃗k
|⃗k⟩⟨⃗k| = IH+ (6.26)
and hence form a basis inH+. The particle like excited states |⃗k⟩ in either sectors are eigenstates
of the free Hamiltonian of the corresponding sectors
H±
free|⃗k⟩ = ℏ(1± 2sℏ)

∞∑
n=1
nkn
|⃗k⟩, (6.27)
but not an eigenstate of the full Hamiltonian. The interaction Hamiltonian is such that its action on
an excited state doesn’t change the level of the state. Explicitly stated, the interaction Hamiltonian
takes a state|⃗k⟩ to|⃗k′⟩ satisfying ∑
n nkn = ∑
n nk′n. The expectation value of ¯h+(t,θ ) operator in|⃗k⟩
state is (1/2 + ℏs). The quantum dispersion, ∆¯h+ in|⃗k⟩ state is O(ℏ) and hence a generic|⃗k⟩ state
can be interpreted as quantum ﬂuctuations over the ground state.
A generic coherent state inH+ can be deﬁned as8
|τ+
⟩ = exp

∞∑
n=1
2τ+
n a†
n
nℏ
|s⟩. (6.28)
The state|τ+
⟩ is not normalised. The normalization is given by
⟨τa
+|τb
+
⟩ = exp

∑
n
4τa
n+τb
n+
nℏ2
. (6.29)
The coherent state|τ+
⟩ is an eigenstate of an (∀ n> 0) operator with eigenvalueτ+
n/ℏ. A coherent
state|τ+
⟩ can be expanded in|⃗k⟩ basis in the following way
|τ+
⟩ =
∑
⃗k
τ+
⃗k
z⃗k
|⃗k⟩, where τ+
⃗k =
∏
m
(τ+
m
ℏ
)km
. (6.30)
The expectation value of ¯h+ operator in a coherent state|τ+
⟩ is given by
ωτ+(z) =
⟨τ+|
¯h+(z)
π |τ+
⟩
⟨τ+|τ+
⟩ = 1
2π + sℏ
π + 1
π
∑
n>0
τ+
n
(
zn + 1
zn
)
. (6.31)
Value ofωτ+(z) on the unit circle (|z| = 1) in the complex z plane is given by,
ωτ+(θ)≡ωτ+(z = eiθ) = 1
2π + sℏ
π + ˜ωτ+(θ)
where ˜ωτ+(θ) = 2
π
∑
n>0
τ+
n cos nθ.
(6.32)
8A rather interesting feature of coherent states written in this form is pointed out by [50–52]. One can show that
the inner product between the coherent state (6.28) and a state lying in the Grassmannian is tau function of the KP
hiererchy.
23
Since the quantum dispersion of ¯h+ in a coherent state is zero, we call such states classical.
We set up a map between a state|ψ⟩∈H + and shape of the upper Fermi surface
|ψ⟩→{ ⟨ψ|¯h+(θ)|ψ⟩}. (6.33)
This maps the following three types of states inH+ to three diﬀerent types of shapes of the upper
Fermi surface ¯h+. Such a mapping has been also discussed in [22]. Expectation value of ¯h+ in
ground state is given by 1
2 + sℏ and has zero dispersion. Thus, ground state |s⟩ corresponds to an
overall shift of ¯h+ by an amount s/N over the classical value. Generic normalised excited states
correspond toO(ℏ) ripples on ¯h+. In this case, the expectation value of ¯h+ picks up a non-zero
dispersion atO(ℏ).O(1) deformation to the upper Fermi surface ¯h+ is mapped to coherent states
|τ+
⟩ inH+ as is evident from 6.32. Here we have assumed⟨τ+|¯h+(θ)|τ+⟩ is a single valued function
ofθ. An important thing to note here is that the classical deformations do not disturb the quadratic
proﬁle of the droplets i.e for a givenθ, there exists unique values of h±(θ).
We now consider the mapping between the automodel diagrams and states in the Hilbert space.
The automodel diagrams corresponds to
¯h±(θ) =±
(1
2 +ξ cosθ
)
. (6.34)
The set of coherent states with τ1 = ξ/2 , τn = 0∀n > 1 are mapped to the automodel diagrams.
In particular, the state corresponding to the limit shape is given by
|τ∗⟩ = exp

a†
1ξ
ℏ
|0⟩. (6.35)
Thus Plancherel growth of Young diagrams is mapped to evolution of classical states [22]. One
can also compute the transition amplitude of such evolution process. The ground state ξ = 0 is an
eigenstate of the Hamiltonian and hence its evolution is trivial. Therefore, we take our initial state
as
|τi
⟩ = exp 2a†
1|s⟩. (6.36)
Such state corresponds to a droplet with 1
2 + ℏ cosθ. The transition amplitude for evolution from
this state to a automodel state in time T is therefore given by [22]
T∼
∑
R
(dim R
k!
)2 (ξ
ℏ
)|R|
eiT ℏC2(R) (6.37)
where C2(R) is given by
C2(R) = N
∑
i=1
li +
∑
i=1
li(li− 2i + 1) (6.38)
Here li is the number of boxes in the ith row of the Young diagram R.
24
Excitations over this state correspond toO(ℏ) ﬂuctuations of the limit shape. Consider the states
exp

a†
1ξ
ℏ +
∑
n>1
2αna†
n
√n
|0⟩ (6.39)
The expectation value of ¯h+(θ) in such a state gives
1
2 +ξ cosθ + 2ℏ
∑
n>1
√nαn cos nθ (6.40)
which is essentially the result (3.20) of Ivanov and Olshanki [9].
