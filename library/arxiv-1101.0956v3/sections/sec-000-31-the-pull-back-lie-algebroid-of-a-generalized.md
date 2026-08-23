---
doc_id: arxiv-1101.0956v3
doc_title: "Algebraic constructions in the category of vector bundles"
section_id: sec-000-31-the-pull-back-lie-algebroid-of-a-generalized
section_title: "The pull-back Lie algebroid of a generalized Lie algebroid"
section_number: 3.1
pages: 7-15
source_pdf: 1101.0956v3.pdf
source_sha256: 28fffdb404e88501
doc_brief: "Algebraic constructions in the category of vector bundles — In this paper we present the category of generalized Lie algebroids ."
---
Let
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
be a generalized Lie algebroid.
Let AF F be a vector ﬁbred ( n + p)-atlas for the vector bundle ( F, ν, N ) and let
AF T M be a vector ﬁbred ( m + m)-atlas for the vector bundle ( T M, τ M , M ).
Let ( h∗F, h ∗ν, M ) be the pull-back vector bundle through h.
If ( U, ξ U ) ∈ AF T M and ( V, s V ) ∈ AF F such that U ∩ h−1 (V ) ⁄= φ, then we deﬁne
the application
h∗ν−1(U ∩h−1(V )))
¯sU ∩h−1(V )
− − − − − − − →
(
U ∩h−1(V )
)
×Rp
(κ, z (h (κ))) ↦− →
(
κ, t −1
V,h (κ)z (h (κ))
)
.
Proposition 3.1.1 The set
AF F
put
= ⋃
(U,ξ U )∈AF T M , (V,s V )∈AF F
U ∩h−1(V )⁄=φ
{(
U ∩ h−1 (V ) , ¯sU ∩h−1(V )
)}
is a vector ﬁbred m + p-atlas for the vector bundle (h∗F, h ∗ν, M ) .
If z = zα tα ∈ Γ (F, ν, N ) , then we obtain the section
Z = (zα ◦ h) Tα ∈ Γ (h∗F, h ∗ν, M )
such that Z (x) = z (h (x)) , for any x ∈ U ∩ h−1 (V ) .
Theorem 3.1.1 Let
( h∗F
ρ , Id M
)
be the Bv-morphism of (h∗F, h ∗ν, M ) source and
(T M, τ M , M ) target, where
(3. 1. 1) h∗F
h∗F
ρ− − → T M
Z α Tα (x) ↦− →
(
Z α · ρi
α ◦ h
) ∂
∂x i (x)
Using the operation
Γ (h∗F, h ∗ν, M ) × Γ (h∗F, h ∗ν, M )
[, ]h∗F− − − − − − − − →Γ (h∗F, h ∗ν, M )
deﬁned by
(3. 1. 2)
[Tα , T β ]h∗F =
(
Lγ
αβ ◦ h
)
Tγ ,
[Tα , f T β ]h∗F = f
(
Lγ
αβ ◦ h
)
Tγ +
(
ρi
α ◦ h
) ∂f
∂x i Tβ ,
[f Tα , T β ]h∗F = − [Tβ , f T α ]h∗F ,
for any f ∈ F (M ) , it results that
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
ia a Lie algebroid which is called the pull-back Lie algebroid of the generalized Lie
algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
7
3.2 Interior Diﬀerential Systems
Let
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
be the pull-back Lie algebroid of the generali-
zed Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
Deﬁnition 3.2.1 Any vector subbundle (E, π, M ) of the vector bundle ( h∗F, h ∗ν, M )
will be called interior diﬀerential system (IDS) of the generalized Lie alge broid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
In particular, if h = Id N = η, then any vector subbundle ( E, π, N ) of the vector
bundle ( F, ν, N ) will be called interior diﬀerential system of the Lie algebroid
((F, ν, N ) , [, ]F , (ρ, Id N )) .
Remark 3.2.1 If ( E, π, M ) is an IDS of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
,
then we obtain a vector subbundle
(
E0, π 0, M
)
of the vector bundle
( ∗
h∗F ,
∗
h∗ν, M
)
such that
Γ
(
E0, π 0, M
) put
=
{
Ω ∈ Γ
( ∗
h∗F ,
∗
h∗ν, M
)
: Ω ( S) = 0 , ∀S ∈ Γ (E, π, M )
}
.
The vector subbundle
(
E0, π 0, M
)
will be called the annihilator vector subbundle of
the IDS (E, π, M ) .
Proposition 3.2.1 If (E, π, M ) is an IDS of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
such that Γ (E, π, M ) = ⟨S1, ..., S r⟩, then it exists Θ r+1, ..., Θ p ∈ Γ
( ∗
h∗F ,
∗
h∗ν, M
)
linearly independent such that Γ
(
E0, π 0, M
)
=
⟨
Θ r+1, ..., Θ p⟩
.
Deﬁnition 3.2.2 The IDS ( E, π, M ) of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
will be called involutive if [ S, T ]h∗F ∈ Γ (E, π, M ) , for any S, T ∈ Γ (E, π, M ) .
Proposition 3.2.2 If (E, π, M ) is an IDS of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
and {S1, ..., S r} is a base for the F (M )-submodule (Γ (E, π, M ) , +, ·) then (E, π, M )
is involutive if and only if [Sa, S b]h∗F ∈ Γ (E, π, M ) , for any a, b ∈
1, r.
8
4 Exterior diﬀerential calculus
Let
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
be a generalized Lie algebroid. We denoted by Λ q (F, ν, N )
the set of diﬀerential forms of degree q. We remark that if
Λ ( F, ν, N ) = ⊕
q≥0
Λ q (F, ν, N ) ,
then we obtain the exterior diﬀerential algebra (Λ ( F, ν, N ) , +, ·, ∧) .
Deﬁnition 4.1 For any z ∈ Γ (F, ν, N ), the application
Λ ( F, ν, N )
Lz− − − − − →Λ ( F, ν, N ) ,
deﬁned by
Lz (f ) = Γ ( T h ◦ ρ, h ◦ η) z (f ) ,
for any f ∈ F (N ) and
Lzω (z1, ..., z q) = Γ ( T h ◦ ρ, h ◦ η) z (ω ((z1, ..., z q)))
−
q∑
i=1
ω
((
z1, ..., [z, z i]F,h , ..., z q
))
,
for any ω ∈ Λ q (F, ν, N ) and z1, ..., z q ∈ Γ (F, ν, N ) , is called the covariant Lie derivative
with respect to the section z.
Theorem 4.1 If z ∈ Γ (F, ν, N ) , ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N ), then
(4. 1) Lz (ω ∧ θ) = Lzω ∧ θ + ω ∧ Lzθ.
Deﬁnition 4.2 For any z ∈ Γ (F, ν, N ), the application
Λ ( F, ν, N )
iz− − − →Λ ( F, ν, N )
Λ q (F, ν, N ) ∋ ω ↦− → izω ∈ Λ q−1 (F, ν, N ) ,
deﬁned by izf = 0, for any f ∈ F (N ) and
izω (z2, ..., z q) = ω (z, z 2, ..., z q) ,
for any z2, ..., z q ∈ Γ (F, ν, N ), is called the interior product associated to the section z.
Theorem 4.2 If z ∈ Γ (F, ν, N ), then for any ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N )
we obtain
(4. 2) iz (ω ∧ θ) = izω ∧ θ + (−1)q ω ∧ izθ.
Theorem 4.3 For any z, v ∈ Γ (F, ν, N ) we obtain
(4. 3) Lv ◦ iz − iz ◦ Lv = i[z,v ]F,h .
Theorem 4.4 The application
Λ q (F, ν, N ) dF
− − − →Λ q+1 (F, ν, N )
ω ↦− → dω
9
deﬁned by dF f (z) = Γ ( T h ◦ ρ, h ◦ η) (z) f, for any z ∈ Γ (F, ν, N ) , and
dF ω (z0, z 1, ..., z q) =
q∑
i=0
(−1)i Γ (T h ◦ ρ, h ◦ η) zi (ω ((z0, z 1, ..., ˆzi, ..., z q)))
+ ∑
i<j
(−1)i+j ω
((
[zi, z j]F,h , z 0, z 1, ..., ˆzi, ..., ˆzj , ..., z q
))
,
for any z0, z 1, ..., z q ∈ Γ (F, ν, N ) , is unique with the following property:
(4. 4) Lz = dF ◦ iz + iz ◦ dF , ∀z ∈ Γ (F, ν, N ) .
This application will be called the exterior diﬀerentiation operator for the exterior
diﬀerential algebra of the generalized Lie algebroid ((F, ν, N ), [, ]F,h , (ρ, η )).
Theorem 4.5 The exterior diﬀerentiation operator dF given by the previous theorem
has the following properties:
1. For any ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N ) we obtain
(4. 5) dF (ω ∧ θ) = dF ω ∧ θ + (−1)q ω ∧ dF θ.
2. For any z ∈ Γ (F, ν, N ) we obtain Lz ◦ dF = dF ◦ Lz.
3. dF ◦ dF = 0.
Theorem 4.6 (of Maurer-Cartan type)
If ((F, ν, N ), [, ]F,h , (ρ, η )) is a generalized Lie algebroid and dF
is the exterior diﬀerentiation operator for the exterior di ﬀerential F(N )-algebra
(Λ( F, ν, N ), +, ·, ∧), then we obtain the structure equations of Maurer-Cartan type
(C1) dF tα = − 1
2 Lα
βγ tβ ∧ tγ , α ∈
1, p
and
(C2) dF κ˜ı = θ˜ı
α tα , ˜ı ∈
1, n,
where
{
tα , α ∈ 1, p
}
is the coframe of the vector bundle (F, ν, N ) .
This equations will be called the structure equations of Maurer-Cartan type associa-
ted to the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
Proof. Let α ∈ 1, p be arbitrary. Since
dF tα (tβ , t γ ) = −Lα
βγ , ∀β, γ ∈
1, p
it results that
(1) dF tα = − ∑
β<γ
Lα
βγ tβ ∧ tγ .
Since Lα
βγ = −Lα
γβ and tβ ∧ tγ = −tγ ∧ tβ , for nay β, γ ∈
1, p, it results that
(2)
∑
β<γ
Lα
βγ tβ ∧ tγ = 1
2 Lα
βγ tβ ∧ tγ
10
Using the equalities (1) and (2) it results the structure equ ation ( C1).
Let ˜ı ∈ 1, n be arbitrarily. Since dF κ˜ı(tα ) = θ˜ı
α , for any α ∈
1, p, it results the
structure equation ( C2). q.e.d.
Corollary 4.1 If
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
is the pull-back Lie algebroid
associated to the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
and dh∗F is the exte-
rior diﬀerentiation operator for the exterior diﬀerential F (M )-algebra
(Λ ( h∗F, h ∗ν, M ) , +, ·, ∧), then we obtain the following structure equations of Maurer -
Cartan type
(C′
1) dh∗F T α = − 1
2
(
Lα
βγ ◦ h
)
T β ∧ T γ , α ∈
1, p
and
(C′
2) dh∗F xi =
(
ρi
α ◦ h
)
T α , i ∈
1, m.
This equations will be called the structure equations of Maurer-Cartan type associated
to the pull-back Lie algebroid
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
.
Theorem 4.7 ( of Cartan type) Let (E, π, M ) be an IDS of the generalized Lie
algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
. If
{
Θ r+1, ..., Θ p}
is a base for the F (M )-submodule(
Γ
(
E0, π 0, M
)
, +, ·
)
, then the IDS (E, π, M ) is involutive if and only if it exists
Ω α
β ∈ Λ 1 (h∗F, h ∗ν, M ) , α, β ∈
r + 1, p
such that
dh∗F Θ α = Σ β ∈r+1,p Ω α
β ∧ Θ β ∈ I
(
Γ
(
E0, π 0, M
))
.
Proof. Let {S1, ..., S r} be a base for the F (M )-submodule (Γ ( E, π, M ) , +, ·)
Let {Sr+1, ..., S p} ∈ Γ (h∗F, h ∗ν, M ) such that {S1, ..., S r, S r+1, ..., S p} is a base for
the F (M )-module
(Γ (h∗F, h ∗ν, M ) , +, ·) .
Let Θ 1, ..., Θ r ∈ Γ
( ∗
h∗F ,
∗
h∗ν, M
)
such that
{
Θ 1, ..., Θ r, Θ r+1, ..., Θ p}
is a base for
the F (M )-module (
Γ
( ∗
h∗F ,
∗
h∗ν, M
)
, +, ·
)
.
For any a, b ∈
1, r and α, β ∈ r + 1, p , we have the equalities:
Θ a (Sb) = δa
b
Θ a (Sβ ) = 0
Θ α (Sb) = 0
Θ α (Sβ ) = δα
β
We remark that the set of the 2-forms
{
Θ a ∧ Θ b, Θ a ∧ Θ β , Θ α ∧ Θ β , a, b ∈
1, r ∧ α, β ∈ r + 1, p
}
11
is a base for the F (M )-module
(
Λ 2 (h∗F, h ∗ν, M ) , +, ·
)
.
Therefore, we have
(1) dh∗F Θ α = Σ b<cAα
bcΘ b ∧ Θ c + Σ b,γ Bα
bγ Θ b ∧ Θ γ + Σ β<γ C α
βγ Θ β ∧ Θ γ ,
where, Aα
bc, B α
bγ and C α
βγ , a, b, c ∈
1, r, α, β, γ ∈ r + 1, p are real local functions such
that Aα
bc = −Aα
cb and C α
βγ = −C α
γβ .
Using the formula
(2) dh∗F Θ α (Sb, S c) = Γ
( h∗F
ρ , Id M
)
Sb (Θ α (Sc)) − Γ
( h∗F
ρ , Id M
)
Sc (Θ α (Sb))
−Θ α ([Sb, S c]h∗F ) ,
we obtain that
(3) Aα
bc = −Θ α ([Sb, S c]h∗F ) ,
for any b, c ∈
1, r and α ∈ r + 1, p.
We admit that ( E, π, M ) is an involutive IDS of the generalized Lie algebroid(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
As [ Sb, S c]h∗F ∈ Γ (E, π, M ) , for any b, c ∈ 1, r, it results that Θ α ([Sb, S c]h∗F ) = 0 ,
for any b, c ∈ 1, r and α ∈ r + 1, p. Therefore, for any b, c ∈ 1, r and α ∈ r + 1, p, we
obtain Aα
bc = 0 and
dh∗F Θ α = Σ b,γ Bα
bγ Θ b ∧ Θ γ + 1
2 C α
βγ Θ β ∧ Θ γ
=
(
Bα
bγ Θ b + 1
2 C α
βγ Θ β
)
∧ Θ γ .
As
Ω α
γ
put
= Bα
bγ Θ b + 1
2 C α
βγ Θ β ∈ Λ 1 (h∗F, h ∗ν, M ) ,
for any α, β ∈ r + 1, p, it results the ﬁrst implication.
Conversely, we admit that it exists
Ω α
β ∈ Λ 1 (h∗F, h ∗ν, M ) , α, β ∈
r + 1, p
such that
(4) dh∗F Θ α = Σ β ∈
r+1,p Ω α
β ∧ Θ β ,
for any α ∈
r + 1, p.
Using the aﬃrmations (1) , (2) and (4) we obtain that Aα
bc = 0 , for any b, c ∈
1, r
and α ∈ r + 1, p.
Using the aﬃrmation (3), we obtain Θ α ([Sb, S c]h∗F ) = 0 , for any b, c ∈ 1, r and
α ∈ r + 1, p.
Therefore, we have [ Sb, S c]h∗F ∈ Γ (E, π, M ) , for any b, c ∈ 1, r.
Using the Proposition 3.2.2, we obtain the second implication. q.e.d.
If
(
(F ′, ν ′, N ′) , [, ]F ′,h ′ , (ρ′, η ′)
)
is an another generalized Lie algebroid and ( ϕ, ϕ 0)
is a GLA-morphism of (
(F, ν, N ) , [, ]F,h , (ρ, η )
)
12
source and ( (
F ′, ν ′, N ′)
, [, ]F ′,h ′ ,
(
ρ′, η ′) )
target, then obtain the application
Λ q (F ′, ν ′, N ′)
(ϕ,ϕ 0)∗
− − − − − − →Λ q (F, ν, N )
ω ′ ↦− → (ϕ, ϕ 0)∗ ω ′ ,
where
((ϕ, ϕ 0)∗ ω ′) (z1, ..., z q) = ω ′ (Γ (ϕ, ϕ 0) (z1) , ..., Γ (ϕ, ϕ 0) (zq)) ,
for any z1, ..., z q ∈ Γ (F, ν, N ) .
Theorem 4.8 If (ϕ, ϕ 0) is a GLA-morphism of
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
source and ( (
F ′, ν ′, N ′)
, [, ]F ′,h ′ ,
(
ρ′, η ′) )
target, then the following aﬃrmations are satisﬁed:
1. For any ω ′ ∈ Λ q (F ′, ν ′, N ′) and θ′ ∈ Λ r (F ′, ν ′, N ′) we obtain
(4. 13) ( ϕ, ϕ 0)∗ (
ω ′ ∧ θ′)
= (ϕ, ϕ 0)∗ ω ′ ∧ (ϕ, ϕ 0)∗ θ′.
2. For any z ∈ Γ (F, ν, N ) and ω ′ ∈ Λ q (F ′, ν ′, N ′) we obtain
(4. 14) iz ((ϕ, ϕ 0)∗ ω ′) = ( ϕ, ϕ 0)∗ (
iϕ (z)ω ′)
.
3. If N = N ′ and (T h ◦ ρ, h ◦ η) = ( T h′ ◦ ρ′, h ′ ◦ η′) ◦ (ϕ, ϕ 0) , then we obtain
(4. 15) (ϕ, ϕ 0)∗ ◦ dF ′
= dF ◦ (ϕ, ϕ 0)∗ .
4.1 Exterior Diﬀerential Systems
Let
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
be the pull-back Lie algebroid of the generali-
zed Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
Deﬁnition 4.1.1 Any ideal ( I, +, ·) of the exterior diﬀerential algebra of the pull-
back Lie algebroid
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
closed under diﬀerentiation op-
erator dh∗F , namely dh∗F I ⊆ I , will be called diﬀerential ideal of the generalized Lie
algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
In particular, if h = Id N = η, then any ideal ( I, +, ·) of the exterior diﬀeren-
tial algebra of the Lie algebroid (( F, ν, N ) , [, ]F , (ρ, Id M )) closed under diﬀerentiation
operator dF , namely dF I ⊆ I , will be called diﬀerential ideal of the Lie algebroid
((F, ν, N ) , [, ]F , (ρ, Id M )) .
Deﬁnition 4.1.2 Let (I, +, ·) be a diﬀerential ideal of the generalized Lie algebroid(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
or of the Lie algebroid (( F, ν, N ) , [, ]F , (ρ, Id M )) respectively .
13
If it exists an IDS ( E, π, M ) such that for all k ∈ N∗ and ω ∈ I ∩ Λ k (h∗F, h ∗ν, M )
we have ω (u1, ..., u k) = 0 , for any u1, ..., u k ∈ Γ (E, π, M ) , then we will say that ( I, +, ·)
is an exterior diﬀerential system (EDS) of the generalized Li e algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
In particular, if h = Id N = η and it exists an IDS ( E, π, M ) such that for all k ∈ N∗
and ω ∈ I ∩Λ k (F, ν, M ) we have ω (u1, ..., u k) = 0 , for any u1, ..., u k ∈ Γ (E, π, M ) , then
we will say that ( I, +, ·) is an exterior diﬀerential system (EDS) of the Lie algebroid
((F, ν, N ) , [, ]F , (ρ, Id N )) .
Theorem 4.1.1 ( of Cartan type) The IDS (E, π, M ) of the generalized Lie al-
gebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
is involutive, if and only if the ideal generated by
the F (M )-submodule
(
Γ
(
E0, π 0, M
)
, +, ·
)
is an EDS of the generalized Lie algebroid(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
Proof. Let ( E, π, M ) be an involutive IDS of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
Let
{
Θ r+1, ..., Θ p}
be a base for the F (M )-submodule
(
Γ
(
E0, π 0, M
)
, +, ·
)
.
We know that
I
(
Γ
(
E0, π 0, M
))
= ∪q∈N {Ω α ∧ Θ α , {Ω r+1, ..., Ω p} ⊂ Λ q (h∗F, h ∗ν, M )} .
Let q ∈ N and {Ω r+1, ..., Ω p} ⊂ Λ q (h∗F, h ∗ν, M ) be arbitrary.
Using the Theorems 4.5 and 4.7 we obtain
dh∗F (Ω α ∧ Θ α ) = dh∗F Ω α ∧ Θ α + (−1)q+1 Ω β ∧ dh∗F Θ β
=
(
dh∗F Ω α + (−1)q+1 Ω β ∧ Ω β
α
)
∧ Θ α .
As
dh∗F Ω α + (−1)q+1 Ω β ∧ Ω β
α ∈ Λ q+2 (h∗F, h ∗ν, M )
it results that
dh∗F
(
Ω β ∧ Θ β
)
∈ I
(
Γ
(
E0, π 0, M
))
Therefore,
dh∗F I
(
Γ
(
E0, π 0, M
))
⊆ I
(
Γ
(
E0, π 0, M
))
.
Conversely, let ( E, π, M ) be an IDS of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
such that the F (M )-submodule
(
I
(
Γ
(
E0, π 0, M
))
, +, ·
)
is an EDS of the generalized
Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
Let
{
Θ r+1, ..., Θ p}
be a base for the F (M )-submodule
(
Γ
(
E0, π 0, M
)
, +, ·
)
. As
dh∗F I
(
Γ
(
E0, π 0, M
))
⊆ I
(
Γ
(
E0, π 0, M
))
it results that it exists
Ω α
β ∈ Λ 1 (h∗F, h ∗ν, M ) , α, β ∈
r + 1, p
such that
dh∗F Θ α = Σ β ∈r+1,p Ω α
β ∧ Θ β ∈ I
(
Γ
(
E0, π 0, M
))
.
Using the Theorem 4.7, it results that ( E, π, M ) is an involutive IDS. q.e.d.
14
