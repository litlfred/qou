---
doc_id: arxiv-1112.5179v1
doc_title: "Prepared for submission to JHEP 3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA "
section_id: sec-018-62-symplectic-action
section_title: "Symplectic action"
section_number: 6.2
pages: 62-65
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA 2Trinity College, Cambridge CB2 1TQ, UK — We"
---
We would like to deﬁne an aﬃne symplectic action on the Hilbert spaceH≡H 0,s (or products
thereof) that intertwines an obvious symplectic action in the algebra of operators (6.20). This
was already done in Section 2 for the index, but we want to rediscover it here from the point
of view of Chern-Simons theory and geometric quantization.
Fortunately, a holomorphic version of the desired symplectic action was deﬁned in [31].
There, the relevant tetrahedron (say) phase space was viewed as a complexiﬁcation of
(
PR, i
2ℏΩR
)
,
wherePR is the slice of P with X, P∈ R, and Ω R is the corresponding real restriction
of the holomorphic symplectic form (6.11). Quantization then produced a Hilbert space
HSL(2)≃ L2(R) containing functions f(X; ℏ). Actual Chern-Simons wavefunctions had the
additional property that they were locally analytic inX and ℏ. Such analytic “SL(2)” wave-
functions were identiﬁed with ellipsoid partition functions of theories TM in [9, 19, 27]. We
recall from [31] that the symplectic groupSp(2, Z) acted on wavefunctionsf(Z; ℏ) in the Weil
33The same technicalities involving convergence and univalent edges from Section 4 appear in Chern-Simons
theory too. We mean a non-rigorous, physical “proof.”
– 61 –
representation [77, 78]. In particular, the generators T and S were implemented as
T : f(X; ℏ) ↦→ (T◦f)(X′; ℏ) =e
1
2ℏX′2
f(X; ℏ), (6.25a)
S : f(X; ℏ) ↦→ (S◦f)(X′; ℏ) = 1√
2πiℏ
∫
R
dXe
1
ℏXX′
f(X; ℏ). (6.25b)
These generate a projective representation of Sp(2, Z) on L2(R) — projective because the
group relations (ST )3 =id and S2 =C only hold up to a phase.
In the present case of SL(2, C) Chern-Simons at k = 0, the complex phase space
(P,ω 0,s) can roughly 34 be considered a product of holomorphic and antiholomorphic copies
of
(
PR,± i
2ℏΩR
)
. This is easy to see from the expression (6.15) for ω0,s. We can then guess
what the appropriate symplectic action on (P,ω 0,s) should be by combining holomorphic and
antiholomorphic copies of (6.25).
For example, let us work in representation (b) of the Hilbert space H, so that wavefunc-
tions f (b)(x,x;q) depend non-holomorphically on x = exp(X). The natural guess for the T
action is
T : f(x,x;q) ↦→ (T◦f)(x′,x′;q) =e
1
2ℏX′2− 1
2ℏX′2
f(x′,x′;q), (6.26)
withX′ = logx′. It is important to check that the right-hand side of (6.26) is still an element
ofH, namely that it is periodic as X′→ X′ + 2πi, and that Re X′∈ ℏ
2 Z is quantized. The
latter condition is automatic, sincef(x,x;q) was only initially deﬁned for ReX = log|x|∈ ℏ
2 Z;
so let us set Re X′ =m′ ℏ
2. Then the exponential in (6.26) becomes
e
1
2ℏX′2− 1
2ℏX′2
=eim′ ImX′
, (6.27)
enforcing the required periodicity in Im X′.
Similarly, a ﬁrst guess for the S transformation would be
S : f(x,x;q) ?↦→ (S◦f)(x′,x′;q) =
∫
dXdXe
1
ℏXX′− 1
ℏXX′
f(x,x;q), (6.28)
with some appropriate normalization. Now, setting Re X = m ℏ
2 and Re X′ = m′ ℏ
2, the
exponent becomes 1
ℏXX′− 1
ℏXX
′
= im′ ImZ +im ImX′ . Therefore, quantization of Re X
ensures periodicity in ImX′, while requiring quantization of ReX′ makes the entire integrand
in (6.28) periodic in Im X. This is almost as desired, except that the integration measure∫
dXdX does not quite make sense. The correct interpretation of
∫
dXdX is as an integration
over a fundamental domain where f(x,x;q) is deﬁned, i.e.
∫
dXdX → ∑
m∈Z
∫ 2π
0 d ImX . If
we use the notation x =q
m
2ζ, x′ =q
m′
2 ζ′, then the proper transformation becomes
S : f(m,ζ ;q) ↦→ (S◦f)(m′,ζ′;q) =
∑
m∈Z
∫ dζ
2πiζ ζm′
ζ′mf(m,ζ ;q), (6.29)
34A precise statement is that the analytic continuation of ( P,ω 0,s), with independent complex coordinates
X,P and X,P , is isomorphic to ( P, i
2ℏΩ)× (P,− i
2ℏΩ). We do not want to analytically continue anything
here, though.
– 62 –
with integration done over the unit circle. The normalizations in (6.26) and (6.29) are just
right to ensure that T andS generate a true representation of Sp(2, Z) acting on our Hilbert
spaceH.
It should now be clear that the transformations (6.26)–(6.29) coincide with the Sp(2, Z)
action on the index, described in [17] and in Section 2.1 above. To make the correspondence
even clearer, we could use a “charge basis” for wavefunctions in H, option (d) of Table 1.
Using Fourier transform to relate polarizations (b) and (d), we then recover the more familiar
symplectic action
T : f(m,e ;q) ↦→ f(m′−e′,e′;q), S : f(m,e ;q) ↦→ f(e′,−m′;q), (6.30)
or more generally,
g : f(m,e ;q) ↦→ f
(
g−1·
(me
)
;q), (6.31)
cf. (2.7). This last expression generalizes nicely to an Sp(2N, Z) action on products of Hilbert
spacesH.
Note that both the options ( a−d) in Table 1 and the present Sp(2, Z) action can be
understood as choices of basis in H, or of polarization for P. More precisely, it is a choice
of element g∈ Sp(2, Z) together with a choice ( a−d) from Table 1 that fully determines
a polarization. The two choices are largely independent. The element g ∈ Sp(2, Z) acts
holomorphically on the phase space P, viewed as C∗× C∗, and makes a rough selection of
“position” (X′) and “momentum” (P′) coordinates, with
(X′
P′
)
= g
(X
P
)
. The choice ( a−d)
then splits the real and imaginary parts of X′ and P′ to provide a speciﬁc real polarization
for (P,ω 0,s). In terms of an index, the former comes from an Sp(2, Z) action on 3d SCFT’s,
while the latter is a choice of fugacity-vs-charge basis for writing the index. The one relation
between the two choices is that switching (b)↔ (c) is equivalent to applying S∈Sp(2, Z).
In addition to a symplectic action, both Chern-Simons theory and the index require an
action of aﬃne shifts. In the holomorphic version of Chern-Simons theory discussed in [31],
such shifts in position or momentum always came in multiples of iπ + ℏ
2, with iπ the classical
shift and ℏ/2 a quantum correction. Now, for full SL(2, C) Chern-Simons theory, we would
expect a shift σX in position X to act as
σX : f(x,x;q) ↦→ f(−q− 1
2x,−q
1
2x;q), or σX : f(m,ζ ;q) ↦→ f(m,−q− 1
2ζ;q), (6.32)
intertwining the operator algebra transformation
( ˆX, ˆX
)
↦→
( ˆX +iπ + ℏ
2, ˆX−iπ− ℏ
2
)
. Note
that the quantum correction has a diﬀerent sign for the holomorphic and antiholomorphic
coordinates, due to the opposite signs appearing in the symplectic structure ω0,s (6.15).
Similarly, a shift by iπ + ℏ
2 in momentum P acts as
σP : f(x,x;q) ↦→ e
1
ℏX(iπ+ ℏ
2 )− 1
ℏX(−iπ− ℏ
2 )f(x,x;q) =
(
−q
1
2
)mf(x,x;q). (6.33)
Again, these transformations are consistent with the combined fermion number and R-charge
shifts of the index deﬁned in Section 2.2.
– 63 –
In contrast to analytically continued Chern-Simons theory, where the representation of
the aﬃne symplectic group on wavefunctions is only projective, and leads to normalization
ambiguities for wavefunctions of 3-manifolds, the present actions in SL(2, C) Chern-Simons
theory at k = 0 deﬁne a true, faithful representation of Sp(2, Z) ⋉
[(
iπ + ℏ
2
)
Z
]2 onH. It is
straightforward to check that group relations such as (2.20) hold on the nose. More generally,
we have a true representation ofSp(2N, Z)⋉
[(
iπ+ ℏ
2
)
Z
]2N onH⊗N. Therefore, wavefunctions
obtained via a symplectic gluing procedure — the procedure outlined in Section 4.1 — should
be unambiguously deﬁned. As already mentioned above, invariance of gluing under 2-3 moves
completely ﬁxes the normalization of the basic building block for any triangulated 3-manifold,
the wavefunction of tetrahedron.
The ﬁnal step in constructing wavefunctions for a triangulated 3-manifold is a “symplectic
reduction,” the quantum equivalent to setting internal edge coordinates CI→ 2πi. We ﬁnish
this discussion by commenting brieﬂy on it. In the analytically continued Chern-Simons
theory, the reduction is implemented by transforming a wavefunction to a (holomorphic)
polarization such thatCI is a position coordinate, and simply settingCI→ 2πi+ℏ, where the
‘+ℏ’ is the usual quantum correction. For the non-holomorphic SL(2, C) wavefunction, this
translates to setting CI→ 2πi + ℏ≃ ℏ andCI→− 2πi− ℏ≃− ℏ; or, with xI =eCI =q
mI
2 ζI,
setting mI→ 0 and ζI→q. In a charge basis, this means
reduction : Z(mI,m,e I,e ;q) ↦→
∑
eI∈Z
qeIZ(0,m,e I,e ;q), (6.34)
just as in (4.6), the last step of the index gluing rules. This completes the argument that the
Chern-Simons wavefunction at k = 0 is fully equivalent to the index.
