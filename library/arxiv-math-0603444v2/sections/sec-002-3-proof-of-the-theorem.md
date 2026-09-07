---
doc_id: arxiv-math-0603444v2
doc_title: "QUASIHOMOGENEITY OF ISOLATED HYPERSURF ACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY"
section_id: sec-002-3-proof-of-the-theorem
section_title: "Proof of the theorem"
section_number: 3
pages: 2-5
source_pdf: 0603444v2.pdf
source_sha256: 46edfcddca963d08
doc_brief: "QUASIHOMOGENEITY OF ISOLATED HYPERSURF ACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY — W e characterize quasihomogeneity of isolated hypersurfac e singu- larities by the injectivity of the map induced"
---
We denote the nth local cohomology module of O supported at the origin by
H :=H n
0 (O) = H n− 1(Cn /integerdivide{0}, O) =
O[ 1
x1···xn
]
∑ n
i=1 O[ 1
x1···ˆ xi···xn
].
QUASIHOMOGENEITY OF ISOLATED HYPERSURF ACE SINGULARITIES 3
By right exactness of the tensor product ⊗ := ⊗O, this implies
H n
0 (Ω 1(logD)) = H n− 1(Cn /integerdivide{0}, Ω 1(logD)) = Ω 1(logD) ⊗H.
The total diﬀerential d : O → Ω 1(logD) induces a natural map
d1 :H =H n
0 (O) →H n
0 (Ω 1(logD)) = Ω 1(logD) ⊗H
in local cohomology. The perfect pairing Der( − logD) ⊗ Ω 1(logD) → O [Sai80,
Lem. 1.6] identiﬁes Ω 1(logD) to Hom(Der( − logD), O). Applying ⊗H, it induces
a pairing
(1) ⟨, ⟩ : Der(− logD) ⊗H n
0 (Ω 1(logD)) = Der( − logD) ⊗ (Ω 1(logD) ⊗H) →H.
such that ⟨δ, (ω ⊗ [g])⟩ = ⟨δ,ω ⟩[g]. In particular, d1([g]) = ∑ n
i=1dxi ⊗ [∂i(g)] for
g ∈ O [ 1
x1···xn
] and hence
(2) ⟨δ,d 1([g])⟩ =
n∑
i=1
⟨δ,dx i⟩[∂i(g)] = δ([g]).
Denoting Hom = Hom O, the pairing (1) corresponds to the natural map
(3) Hom(Der(− logD), O) ⊗H = Ω 1(logD) ⊗H
π /d47/d47Hom(Der(− logD),H ).
According to [HM98, Lem. 1.11], Ω 1(logD) = O · d f
f + Ω 1 and there is an exact
sequence
(4) 0 /d47/d47O
αt
/d47/d47On+1 ∼= O ⊕ Ω 1 β /d47/d47Ω 1(logD) /d47/d470
whereα = (f,f 1,...,f n) andβ = ( d f
f , −dx1,..., −dxn). Dualizing against O yields
0 /d47/d47Der(− logD)
βt
/d47/d47On+1 α /d47/d47J /d47/d470, J := ⟨f,f 1,...,f n⟩,
and Ext 1(Ω 1(logD), O) ∼= O/J . Dualizing against O and H yields the sequences
0 /d47/d47Hom(J, O) /d47/d47On+1 (βt)t
/d47/d47Hom(Der(− logD), O) /d47/d470,(5)
0 /d47/d47Hom(J,H ) /d47/d47H n+1 /d47/d47Hom(Der(− logD),H ) /d47/d47Ext1(J,H ) /d47/d470.(6)
By reﬂexivity of Der( − logD) [Sai80, Cor. 1.7], the sequences (4) and (5) coincide.
In particular, (βt)t =β is surjective and Hom(J, O) = O as the kernel of β which is
directly obvious. From sequences (5) and (6), we obtain the commu tative diagram
(7) Hom(J, O) ⊗H /d47/d47
/d15/d15
H n+1 β⊗ 1 /d47/d47/d47/d47Hom(Der(− logD), O) ⊗H
π
/d15/d15
Hom(J,H )/d31 /d127 ι /d47/d47H n+1 γ /d47/d47Hom(Der(− logD),H )
involving the map π in (3).
Lemma 2. If D is not Euler homogeneous then trδ0 = 0 for all δ ∈ Der(− logD).
In particular, π(d1([ 1
x1...xn
]))(δ) = ⟨δ,d 1([ 1
x1...xn
])⟩ = 0 for all δ ∈ Der(− logD).
4 MICHEL GRANGER AND MATHIAS SCHULZE
Proof. By the formal structure theorem [GS06, Thm. 5.4], there is a syste m of
generators S of the m-adic completion ˆDer(− logD) of Der( − logD) such that,
for δ ∈ S , either δ0 is nilpotent and hence tr δ0 = 0 or δ = δ0 is semisimple and
δ( ˆf ) ∈ Q· ˆf where ˆf := ˆu·f for some unit ˆu ∈ ˆO⋆. In the second case, δ ∈ Annˆ Der( ˆf )
if D and hence ˆf is not Euler homogeneous. Since D is an isolated singularity,
Annˆ Der( ˆf ) = ⟨ ˆfi∂j − ˆfj∂i | 1 ≤i<j ≤n⟩, ˆfi :=∂i( ˆf ).
By a formal coordinate change [Arn72, Lem. 4.1], ˆf =x2
1 +· · ·+x2
k +g(xk+1,...,x n)
with g ∈ ˆm3 and trδ0 = 0 follows also in the second case from
δ0 ∈ Annˆ Der( ˆf )0 = ⟨xi∂j −xj∂i | 1 ≤i<j ≤k⟩.
Since Der( − logD)0 = ˆDer(− logD)0 and by additivity and coordinate invariance
of tr δ0, this proves the ﬁrst claim. The second follows from (2) and the obv ious
formulaδ([ 1
x1...xn
]) = tr(δ0)[ 1
x1...xn
] for any δ ∈ m · Der. □
We continue our study of diagram (7) under the assumption that D is not Euler
homogeneous. By Lemma 2, π(d1([ 1
x1···xn
])) = 0 and d1([ 1
x1···xn
]) = ( β ⊗ 1)(ψ)
where ψ = (0,u 1,...,u n) ∈ H n+1 and ui = −∂i([ 1
x1···xn
]) = [ 1
x1···x2
i ···xn
]. Then
γ(ψ) = 0 and hence ψ =ι(ϕ) where ϕ ∈ Hom(J,H ) is characterised by
(8) ϕ(fi) =
[ 1
x1 · · ·x2
i · · ·xn
]
, ϕ (f ) = 0.
By injectivity of ι, d1([ 1
x1···xn
]) = 0 if and only if ϕ extends to O.
Lemma 3. The map ϕ ∈ Hom(J,H ) which fulﬁls (8) extends to a ˜ϕ ∈ Hom(O,H ).
Proof. Denote by A := C[x1,...,x n] ⊆ O the polynomial ring and by M ⋆ :=
HomC(M, C) the algebraic dual of an A- or O-module M . The residue pairing
[Ems78, Sect. B.1] ⟨, ⟩ :H ⊗C O → C is deﬁned by ⟨[g],h ⟩ := res([g ·h]) where the
residue map res : H → C sends [g] ∈ H to the coeﬃcient of 1
x1···xn
in g. More
explicitly, ⟨[ ∑
i∈ Nn
ai
xi1+1
1 · · ·xin+1
n
]
,
∑
i∈ Nn
bixi1
1 · · ·xin
n
⟩
=
∑
i∈ Nn
aibi.
The residue pairing deﬁnes an injection of H into O⋆. Restricted to A, the pairing
injects H into A⋆ = C[[x− 1
1 ,...,x − 1
n ]] · 1
x1···xn
. By (8), ϕ annihilates the ideal
K := ⟨f ⟩ + m2 · ⟨f1,...,f n⟩ and induces a ¯ϕ ∈ Hom(J/K,H ). Since K has ﬁnite
colength, mN +1 ⊆K for some N >0 and hence the ﬁnite vector space
K ⊥ ⊆ (mN +1)⊥ =
⨁
|i|≤ N
C
xi1+1
1 · · ·xin+1
n
identiﬁes to (K ∩A)⊥ ⊆A⋆. Then the residue pairing induces an isomorphism
ℓ :K ⊥ = (K ∩A)⊥ → (A/K ∩A)⋆ = (O/K)⋆
deﬁned by ℓ([g])([h]) = ⟨[g],h ⟩ = res([g ·h]) for [g] ∈K ⊥ and [h] ∈ O/K. Thus, the
linear form res ◦ ¯ϕ ∈ (J/K )⋆ extends to ℓ([g]) for some [ g] ∈K ⊥ which means that
res(ϕ(h)) = res([g ·h]) for all h ∈J. Now, deﬁne ˜ϕ ∈ Hom(O,H ) by ˜ϕ(h) := [g ·h]
for all h ∈ O. Then, for h ∈J,
⟨˜ϕ(h),x α⟩ = ⟨[g ·h],x α⟩ = res([g ·xαh]) = res(ϕ(xαh)) = ⟨ϕ(h),x α⟩
QUASIHOMOGENEITY OF ISOLATED HYPERSURF ACE SINGULARITIES 5
for all α ∈ Nn and hence ˜ϕ(h) = ϕ(h) which implies that ˜ϕ is an extension of ϕ. □
Proof of Theorem 1. For isolated singularities, Euler and quasihomogeneity are
equivalent by [Sai71] and hp(H n
0 (Ω • (logD))) = 0 for all p by [HM98, Cor. 1.8].
For non Euler homogeneous D, 0 ⁄= [ 1
x1···xn
] ∈ kerd1 by Lemma 3. □
