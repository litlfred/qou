---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-037-c3-quantum-reduction
section_title: "C.3. Quantum reduction"
section_number: null
pages: 42-44
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
constraintsXI→ 0, and the meridian XN→ 2u. In Section C.1, these functions were actu-
ally used as moment maps to perform a symplectic reduction. Now we s hould do the same
thing quantum mechanically. In order to reduce the product wavef unctionZ×(Z1,...,Z N )
of ( C.7) to the ﬁnal wavefunction ZM (u) of the glued manifold M, we must transform the
wavefunction to a representation (or “polarization”) in which the o perators ˆXI act diago-
nally (by multiplication). In this representation, the wavefunction d epends explicitly on the
XI. The “reduction” then simply requires ﬁxing XI→ (0,..., 0, 2u). Schematically,
(C.17) Z×(Z1,...,Z N )
transform
↦−→ ~Z×(X1,...,X N )
ﬁx
↦→ ZM (u) = ~Z×(0,..., 0, 2u).
The transformation fromZ× to ~Z× is accomplished — formally — with the Weil represen-
tationR of the aﬃne symplectic group [ Sha62, Wei64]. In particular, we need R(α) for the
aﬃne symplectic transformation α in (C.16). In Section 6 of [ Dim], it was discussed in detail
how to ﬁnd R(α) by factoring the matrix of ( C.16) into generators. Then, for example, an
“S–type” element of the symplectic group acts via Fourier transform
(C.18) R
((0 −I
I 0
))
: f (Z) ↦→ ˜f (W ) =
∫ dNZ
(2πiℏ)N/ 2e
1
ℏ Z·Wf (Z),
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 43
whereas a “T –type” element acts as multiplication by a quadratic exponential
(C.19) R (( I 0
T I )) : f (Z) ↦→ ˜f (W ) = e
1
2ℏ W T TWf (W ).
Aﬃne shifts act either by translation or multiplication by a linear expon ential.
In the present case, there is a convenient trick that allows us to ﬁn dR(α) without de-
composing α into generators. We assume that the block B of the symplectic matrix is
nondegenerate, since we know we can always choose a quad type wit h this property. For the
moment, let us also suppose that the aﬃne shifts vanish, ν =νP = 0. Then the Weil action
is
(C.20)
R(α) : Z×(Z) ↦→~Z×(X) = 1
√
det B
∫ dNZ
(2πiℏ)N/ 2e
1
2ℏ (X·DB−1X−2Z·B−1X+Z·B−1AZ)Z×(Z).
In particular, it can easily be veriﬁed that this correctly intertwines an action of operators
( ˆZi = Zi, ˆZ ′′
i = ℏ∂Zi) on Z×(Z) with an action of operators ( ˆXI = XI, ˆPI = ℏ∂XI ) on
~Z×(X). For example,
∫
dNZe
1
2ℏ (X·DB−1X−2Z·B−1X+Z·B−1AZ)(
A ˆZ + B ˆZ ′′)
Z×(Z)
=
∫
dNZe
1
2ℏ (X·DB−1X−2Z·B−1X+Z·B−1AZ)(
AZ + ℏ B∂Z
)
Z×(Z)
=
∫
dNZ
[ (
AZ− ℏ B∂Z
)
e
1
2ℏ (X·DB−1X−2Z·B−1X+Z·B−1AZ)]
Z×(Z)
=
∫
dNZXe
1
2ℏ (X·DB−1X−2Z·B−1X+Z·B−1AZ)Z×(Z)
= ˆX ~Z×(X).
Non-zero aﬃne shifts ν and νP further modify the result to
~Z×(X) = 1√
det B
∫ dNZ
(2πiℏ)N/ 2 exp
[
− 1
ℏX·
(
iπ + ℏ
2
)
νP +
1
2ℏ
((
X +
(
iπ + ℏ
2
)
ν
)
· DB−1
(
X +
(
iπ + ℏ
2
)
ν
)
− 2Z· B−1
(
X +
(
iπ + ℏ
2
)
ν
)
+Z· B−1AZ
)]
Z×(Z),
and then, after setting X→ 2u = (0,..., 0, 2u) as in ( C.17), we ﬁnd
ZM (u) = 1√
det B
∫ dNZ
(2πiℏ)N/ 2 exp
[
− 1
ℏ (2πi + ℏ)νλu +
1
2ℏ
((
2u +
(
iπ + ℏ
2
)
ν
)
· DB−1
(
2u +
(
iπ + ℏ
2
)
ν
)
− 2Z· B−1
(
2u +
(
iπ + ℏ
2
)
ν
)
+Z· B−1AZ
)] N∏
i=1
ψℏ(Zi).(C.21)
44 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
This is the partition function of the one-cusped manifold M, modulo a multiplicative ambi-
guity of the form exp
[ π 2
6 a+ iπ
4b+ 1
24c
]
fora,b,c ∈ Z, which we will say more about in Section
C.5. By construction, this partition function is annihilated by the quantum ˆA-polynomial
of M.
C.4. Introducing a ﬂattening. In order to obtain the state integral ( 5.23) appearing in
the paper, we can introduce a generalized ﬂattening (as in Section 4.4) and use it to simplify
(C.21). Note that the discrete-faithful state integral ( 5.2) follows immediately from ( 5.23)
upon setting u = (0,..., 0,u )→ 0.
Suppose, then, that we have integers ( f,f ′′) that satisfy
(C.22)
(
A B
C D
)(
f
f ′′
)
=
(
ν
νP
)
,
for some νP whose last entry is νλ . We will assume that a completed symplectic matrix
( A B
C D ) can be chosen in Sp(2 N, Z) rather than in Sp(2 N, Q). In that case, since f and f ′′
are vectors with integer entries, it follows that νP∈ ZN . Then,
−νλu +ν· DB−1u =−(Cf + Df ′′)· u + (DT Af + DT Bf ′′)· B−1u =f· B−1u,
where we used the symplectic identities DT B = BT D and DT A =I + BT C; and
ν· DB−1ν =ν· D(f ′′ + B−1Af ) = ν· (Df ′′ + Cf + B−1,T f ) = f· B−1ν +ν·νP
=f· B−1ν (mod Z)
in a similar way. These relations allow us to write the state integral ( C.21) as
ZM (u) = 1√
det B
·
∫ dNZ
(2πℏ)N/ 2e
1
ℏ
[
2u·DB−1u+(2πi +ℏ)f ·B−1u+ 1
2
(
iπ + ℏ
2
) 2
f ·B−1ν−ZB−1
(
2u+
(
iπ + ℏ
2
)
ν
) ]
N∏
i=1
ψℏ(Zi),
(C.23)
just as in (
5.23). (We drop a factor of
√
i from the measure, since it can be absorbed in the
overall normalization ambiguity.)
