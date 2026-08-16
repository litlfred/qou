---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action Bogus/suppress law Broda1 Department of Theoretical Physics University of /suppress L´ od´ z Pomorska 149/153 PL 90–236 /suppress L´ od´ z Pola"
section_id: sec-020-222-holomorphic-approach
section_title: "Holomorphic approach"
section_number: 2.2.2
pages: 21-27
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action Bogus/suppress law Broda1 Department of Theoretical Physics University of /suppress Lódź Pomorska 149/153 PL 90–236 /suppress Lódź Poland — In this short review"
---
Quantum-mechanics background For our further convenience let us for-
mulate an auxiliary “Schr¨ odinger problem” governing the parallel-transport op-
erator 10 for the Abelian gauge potential A,
i dz
dt = − ˙xiAiz, (23)
which expresses the fact that the “wave function” z should be covariantly con-
stant along the line L, i.e.
Dtz
def
=
( d
dt − i ˙xiAi
)
z = 0,
21
where Dt is the absolute covariant derivative.
First of all, let us derive the path-integral expression for the parallel-transport
operator U along L. To this end, we should consider the non-Abelian formula
(diﬀerential equation) analogous to Eq.23,
i dzk
dt = − ˙xi(t)Aa
i [x(t)]T a
klzl, (24)
or
(Dtz)k
def
=
{
δkl
d
dt − i ˙xiAa
i [x(t)]T a
kl
}
zl = 0,
where z is an auxiliary “wave function” in an irreducible representation R of the
gauge Lie group G, which is to be parallelly transported along L parametrized
by xi(t), t′ ≤ t ≤ t′′. Formally, Eq.24 can be instantaneously integrated out
yielding
zk(x′′) = Ukl(x′′, x′)zl(x′),
where x′′ = x(t′′), x′ = x(t′), and
U(x′′, x′) ≡ U(t′′, t′) = P exp
(
i
∫ t′′
t′
˙xi(t)Ai[x(t)] dt
)
,
as expected.
Let us now consider the following auxiliary classical-mechanics problemwith
the classical Lagrangian
L (¯z, z) = i¯zDtz. (25)
The equation of motion for z following from Eq.25 reproduces Eq.24, and yields
the classical Hamiltonian
H = i ˙xi(t)Aa
i [x(t)]T a
klπkzl = − ˙xi(t)Aa
i [x(t)]T a
kl ¯zkzl. (26)
The corresponding auxiliary quantum-mechanics problem is given, according to
Eq.26, by the Schr¨ odinger equation
i d
dt |Φ⟩ = ˆH(t)|Φ⟩, (27)
with
ˆH(t) = − ˆA(t) = − ˙xi(t)Aa
i [x(t)] ˆT a = − ˙xi(t)Aa
i [x(t)]T a
klˆa+
k ˆal ≡ Hkl(t)ˆa+
k ˆal,
22
where the creation and anihilation operators satisfy the standard commutation
(−) or anticommutation (+) relations
[ˆak, ˆa+
l ]∓ = δkl, [ˆa+
k , ˆa+
l ]∓ = [ˆak, ˆal]∓ = 0.
It can be easily checked by direct computation that we have really ob tained a
realization of the Lie algebra g in a Hilbert (Fock) space,
[ ˆT a, ˆT b]− = if abc ˆT c,
in accordance with 11, where ˆT a = T a
klˆa+
k ˆal. For an irreducible representation
R the second-order Casimir operator C2 is proportional to the identity operator
I, which in turn, is equal to the number operator ˆN in our Fock representation,
i.e. if T a → ˆT a, then I → ˆN = δklˆa+
k ˆal. Thus, we obtain an important for our
further considerations constant of motion ˆN,
[ ˆN , ˆH]− = 0. (28)
It is interesting to note that this approach works equally well for co mmutation
relations as well as for anticommutation relations.
Path integral Let us now derive the holomorphic path-integral representation
for the kernel of the parallel-transport operator,
⟨
¯z′′
⏐
⏐
⏐
⏐
⏐P exp
[
i
∫ t′′
t′
ˆA(t) dt
] ⏐
⏐
⏐
⏐
⏐z′
⟩
= lim
N →∞
∫
. . .
∫ ⟨
¯zN
⏐
⏐
⏐
(
1 + iǫ ˆAN
)⏐
⏐
⏐zN −1
⟩
e−¯zN −1zN −1 d¯zN −1 dzN −1
2πi
⟨
¯zN −1
⏐
⏐
⏐
(
1 + iǫ ˆAN −1
)⏐
⏐
⏐zN −2
⟩
e−¯zN −2zN −2 d¯zN −2 dzN −2
2πi
. . . e−¯z1z1 d¯z1 dz1
2πi
⟨
¯z1
⏐
⏐
⏐
(
1 + iǫ ˆA1
)⏐
⏐
⏐z0
⟩
. (29)
Now we should calculate the single expectation value
⟨
¯zn
⏐
⏐
⏐
(
1 + iǫ ˆAn
)⏐
⏐
⏐zn−1
⟩
= ⟨¯zn |zn−1 ⟩+ i
⟨
¯zn
⏐
⏐
⏐ˆAn
⏐
⏐
⏐zn−1
⟩
ǫ.
Here
⟨¯zn |zn−1 ⟩ = e¯znzn−1,
23
whereas
i
⟨
¯zn
⏐
⏐
⏐ˆAn
⏐
⏐
⏐zn−1
⟩
ǫ = i ⟨¯zn |¯znAnzn−1| zn−1⟩ǫ
= iǫ¯znAnzn−1 ⟨¯zn | zn−1⟩.
Thus
⟨
¯zn
⏐
⏐
⏐
(
1 + iǫ ˆAn
)⏐
⏐
⏐zn−1
⟩
= e¯znzn−1 + iǫ¯znAnzn−1e¯znzn−1
= e¯znzn−1
[
1 + iǫ¯znAnzn + O
(
ǫ2)]
= e¯znzn−1e+iǫ¯znAnzn+O(ǫ2).
Combining this expression with the exponent in 29 we obtain
e−¯znzne¯znzn−1+iǫ¯znAnzn+O(ǫ2) = e−¯zn(zn−zn−1)+iǫ¯znAnzn+O(ǫ2)
= exp
[
(−¯zn ˙zn + ǫ¯znAnzn) ǫ + O
(
ǫ2)]
.
Finally,
U(¯z′′, z′; t′′, t′) =
⟨
¯z′′
⏐
⏐
⏐
⏐
⏐P exp
[
−i
∫ t′′
t′
ˆH(t)dt
] ⏐
⏐
⏐
⏐
⏐z′
⟩
≡
⟨
¯z′′
⏐
⏐
⏐
⏐
⏐P exp
[
i
∫ t′′
t′
ˆA(t) dt
] ⏐
⏐
⏐
⏐
⏐z′
⟩
=
∫ [
D2z
]
exp
{
¯z(t′′)z(t′′) + i
∫ t′′
t′
[i¯z(t) ˙z(t)
+¯z(t)A(t)z(t)] dt} ,
≡
∫ [
D2z
]
exp
[
¯z(t′′)z(t′′) + i
∫ t′′
t′
L dt
]
,
where
[
D2z
]
=
∏
t′<t<t′′
d¯z(t) dz(t)
2πi ,
and L is of “classical” form 25.
Let us conﬁne our attention to the one-particle subspace of the F ock space.
As the number operator ˆN is conserved by virtue of Eq.28, if we start from the
one-particle subspace of the Fock space, we shall remain in this subspace during
all the evolution. The transition amplitude Ukl(t′′, t′) between the one-particle
24
states |1k⟩ = ˆa+
k |0⟩ and |1l⟩ = ˆa+
l |0⟩ is given by the following scalar product in
the holomorphic representation
Ukl =
⟨
1k
⏐
⏐
⏐
⏐
⏐P exp
[
i
∫ t′′
t′
ˆA(t) dt
] ⏐
⏐
⏐
⏐
⏐1l
⟩
=
∫
⟨1k |z′′ ⟩
⟨
¯z′′
⏐
⏐
⏐
⏐
⏐P exp
[
i
∫ t′′
t′
ˆA(t) dt
] ⏐
⏐
⏐
⏐
⏐z′
⟩
⟨¯z′ |1l ⟩
e−¯z′′z′′−¯z′z′ d¯z′′ dz′′ d¯z′ dz′
(2πi)2
=
∫
D2z zk(t′′)¯zl(t′) exp
[
−¯z(t′)z(t′) + i
∫ t′′
t′
L dt
]
, (30)
where now
D2z =
∏
t′≤t≤t′′
d¯z(t) dz(t)
2πi .
Depending on the statistics, there are the two ( ∓) possibilities (fermionic and
bosonic)
zk¯zl ∓ ¯zlzk = ¯zk¯zl ∓ ¯zl¯zk = zkzl ∓ zlzk = 0,
equivalent as far as one-particle subspace of the Fock space is con cerned, which
takes place in our further considerations.
One can easily check that Eq.30 represents the object we are lookin g for.
Namely, from the Schr¨ odinger equation (Eq.27) it follows that for t he general
one-particle state αkˆa+
k |0⟩ (summation after repeating indices) we have
i d
dt(αmˆa+
m|0⟩) = Hkl(t)ˆa+
k ˆalαmˆa+
m|0⟩ = Hkl(t)αl(ˆa+
k |0⟩). (31)
Using the property of linear independence of Fock-space vectors in Eq.31, and
comparing Eq.31 to Eq.24, we can see that Eq.30 really represents th e matrix
elements of the parallel-transport operator. For closed paths, x(t′) = x(t′′) = x,
Eq.30 gives the holonomy operator Ukl(x) and Ukk is the Wilson loop. Interest-
ingly enough, the Wilson loop, which is supposed to describe a quark-a ntiquark
interaction, is represented by a “true” quark and antiquark ﬁeld, z and ¯z, re-
spectively. So, the mathematical trick can be interpreted “physic ally”.
Obviously, the “full” trace of the kernel in Eq. 3.9 is obtained by impos -
ing appropriate boundary conditions, and integrating with respect to all the
25
variables without the boundary term. Analogously, one can also der ive the
parallel-transport operator (a generalization of the one just considered) for sym-
metric n-tensors (bosonic n-particle states) and for n-forms (fermionic n-particle
states).
The non-Abelian Stokes theorem Let us now deﬁne a (bosonic or fermionic)
Euclidean two-dimensional “topological” quantum ﬁeld theory of mult icompo-
nent ﬁelds ¯z, z transforming in an irreducible representation R of the Lie algebra
g on the compact surface S, dim S = 2 , ∂S = C, S ⊂ M, dim M = d, in an
external non-Abelian gauge ﬁeld A, by the classical action
Scl =
∫
S
(
iDi¯zDjz + 1
2 ¯zFijz
)
dxi ∧ dxj, i, j = 1, . . . , d, (32)
or in a parametrization xi(σ1, σ2), by the action
Scl =
∫
S
Lcl(¯z, z)d2σ (33)
=
∫
S
εAB
(
iDA¯zDBz + 1
2 ¯zFABz
)
d2σ, A, B = 1, 2,
where
DA = ∂AxiDi, D i
def
= ∂i − iAi, F AB = ∂Axi∂Bxj Fij.
At present, we are prepared to formulate a holomorphic path-integral version
of the non-Abelian Stokes theorem,
∫
D2z z′′
k ¯z′
k exp
(
−¯z′z′ + i
∮
C
i¯z Dz
)
(34)
=
∫
D2z z′′
k ¯z′
k exp (−¯z′z′ + iScl),
or in the polar parametrization xi(σ1, σ2) t′ ≤ σ1 ≡ t ≤ t′′, 0 ≤ σ2 ≡ s ≤ 1,
∫
D2z zk(t′′)¯zk(t′) exp
{
−¯z(t′)z(t′) + i
∫ t′′
t′
L[¯z(t), z(t)]dt
}
(35)
=
∫
D2z zk(t′′, 1)¯zk(t′, 1) exp
[
−¯z(t′, 1)z(t′, 1) + i
∫ 1
0
∫ t′′
t′
Lcl dt ds
]
,
26
where L(z, ¯z) and Lcl(¯z, z) are deﬁned by Eq.25 and Eq.33, respectively. The
