---
doc_id: arxiv-1101.0956v3
doc_title: "Algebraic constructions in the category of vector bundles"
section_id: sec-003-2-the-category-of-generalized-lie-algebroids
section_title: "The category of generalized Lie algebroids"
section_number: 2
pages: 18-38
source_pdf: 1101.0956v3.pdf
source_sha256: 28fffdb404e88501
doc_brief: "Algebraic constructions in the category of vector bundles — In this paper we present the category of generalized Lie algebroids ."
---
In general, if C is a category, then we denote |C| the class of objects and for any
A, B ∈ |C|, we denote C (A, B ) the set of morphisms of A source and B target. Let V ect,
Liealg, Mod, Man and Bv be the category of real vector spaces, Lie algebras, modules ,
manifolds and vector bundles respectively.
We know that if ( E, π, M ) ∈ | Bv| , Γ (E, π, M ) = {u ∈ Man (M, E ) : u ◦ π = Id M }
and F (M ) = Man (M, R) , then (Γ ( E, π, M ) , +, ·) is a F (M )-module. If ( ϕ, ϕ 0) ∈
Bv ((E, π, M ) , (E′, π ′, M ′)) such that ϕ 0 ∈ Iso Man (M, M ′) , then, using the operation
F (M ) × Γ (E′, π ′, M ′) ·− − − − →Γ (E′, π ′, M ′)
(f, u ′) ↦− → f ◦ ϕ −1
0 · u′
it results that (Γ ( E′, π ′, M ′) , +, ·) is a F (M )-module and we obtain the Mod-morphism
Γ (E, π, M )
Γ( ϕ,ϕ 0)− − − − − − − − − − →Γ (E′, π ′, M ′)
u ↦− → Γ (ϕ, ϕ 0) u
deﬁned by
Γ (ϕ, ϕ 0) u (y) = ϕ
(
uϕ −1
0 (y)
)
,
for any y ∈ M ′.
3
We know that a Lie algebroid is a vector bundle ( F, ν, N ) ∈ | Bv| such that there
exists
(ρ, Id N ) ∈ Bv ((F, ν, N ) , (T N, τ N , N ))
and an operation
Γ (F, ν, N ) × Γ (F, ν, N )
[, ]F− − → Γ (F, ν, N )
(u, v ) ↦− → [u, v ]F
with the following properties:
LA1. the equality holds good
[u, f · v]F = f [u, v ]F + Γ ( ρ, Id N ) (u) f · v,
for all u, v ∈ Γ (F, ν, N ) and f ∈ F (N ) ,
LA2. the 4-tuple (Γ ( F, ν, N ) , +, ·, [, ]F ) is a Lie F (N )-algebra,
LA3. the Mod-morphism Γ ( ρ, Id N ) is a LieAlg-morphism of (Γ ( F, ν, N ) , +, ·, [, ]F )
source and (Γ ( T N, τ N , N ) , +, ·, [, ]T N) target.
Deﬁnition 2.1 Let M, N ∈ |Man| , h ∈ Iso Man (M, N ) and η ∈ Iso Man (N, M ).
If ( F, ν, N ) ∈ |Bv| so that there exists
(ρ, η ) ∈ Bv ((F, ν, N ) , (T M, τ M , M ))
and an operation
Γ (F, ν, N ) × Γ (F, ν, N )
[, ]F,h
− − − →Γ (F, ν, N )
(u, v ) ↦− → [u, v ]F,h
with the following properties:
GLA1. the equality holds good
[u, f · v]F,h = f [u, v ]F,h + Γ ( T h ◦ ρ, h ◦ η) (u) f · v,
for all u, v ∈ Γ (F, ν, N ) and f ∈ F (N ) .
GLA2. the 4-tuple
(
Γ (F, ν, N ) , +, ·, [, ]F,h
)
is a Lie F (N )-algebra,
GLA3. the Mod-morphism Γ ( T h ◦ ρ, h ◦ η) is a LieAlg-morphism of
(
Γ (F, ν, N ) , +, ·, [, ]F,h
)
source and
(Γ (T N, τ N , N ) , +, ·, [, ]T N)
target, then we will say that the triple
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
is a generalized Lie
algebroid. The couple
(
[, ]F,h , (ρ, η )
)
will be called generalized Lie algebroid structure.
4
Deﬁnition 2.2 We deﬁne the set of morphisms of
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
source and ( (
F ′, ν ′, N ′)
, [, ]F ′,h ′ ,
(
ρ′, η ′) )
target as being the set
{(ϕ, ϕ 0) ∈ Bv ((F, ν, N ) , (F ′, ν ′, N ′))}
such that ϕ 0 ∈ Iso Man (N, N ′) and the Mod-morphism Γ ( ϕ, ϕ 0) is a LieAlg-morphism
of (
Γ (F, ν, N ) , +, ·, [, ]F,h
)
source and (
Γ
(
F ′, ν ′, N ′)
, +, ·, [, ]F ′,h ′
)
target.
So, we can discuss about the category GLA of generalized Lie algebroids. Examples
of objects of this category are presented in the paper [1] . We remark that GLA is a
subcategory of the category Bv.
Let
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
be an arbitrary object of the category GLA.
• Locally, for any α, β ∈ 1, p, we set [ tα , t β ]F,h = Lγ
αβ tγ . We easily obtain that
Lγ
αβ = −Lγ
βα , for any α, β, γ ∈
1, p.
The real local functions Lγ
αβ , α, β, γ ∈
1, p will be called the structure functions of
the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
• We assume the following diagrams:
F
ρ− − − − − → T M T h− − − − − − →T N
↓ ν ↓ τM ↓ τN
N
η− − − − − → M h− − − − − → N
(
χ ˜ı, z α ) (
xi, y i) (
χ ˜ı, z ˜ı)
where i, ˜ı ∈ 1, m and α ∈ 1, p.
If (
χ ˜ı, z α )
− →
(
χ ˜ı′ (
χ ˜ı)
, z α ′ (
χ ˜ı, z α ))
,
(
xi, y i)
− →
(
xi´(
xi)
, y i´(
xi, y i) )
and (
χ ˜ı, z ˜ı)
− →
(
χ ˜ı′ (
χ ˜ı)
, z ˜ı′ (
χ ˜ı, z ˜ı))
,
then
zα´ = Λ α´
α zα ,
yi´ = ∂x i´
∂x i yi
and
z˜ı′ = ∂χ ˜ı′
∂χ ˜ı z˜ı.
5
• We assume that ( θ, µ )
put
= ( T h ◦ ρ, h ◦ η). If zα tα ∈ Γ (F, ν, N ) is arbitrary, then
(2. 1)
Γ (T h ◦ ρ, h ◦ η) (zα tα ) f (h ◦ η (κ)) =
=
(
θ˜ı
α zα ∂f
∂ κ˜ı
)
(h ◦ η (κ)) =
( (
ρi
α ◦ h
)
(zα ◦ h) ∂f ◦h
∂x i
)
(η (κ)) ,
for any f ∈ F (N ) and κ ∈ N.
The coeﬃcients ρi
α respectively θ˜ı
α change to ρi´
α´ respectively θ˜ı´
α´ according to the
rule:
(2. 2) ρi´
α´ = Λ α
α´ρi
α
∂x i´
∂x i ,
respectively
(2. 3) θ˜ı´
α´ = Λ α
α´θ˜ı
α
∂κ˜ı´
∂κ˜ı,
where
‖Λ α
α´‖ =
‖
‖
‖Λ α´
α
‖
‖
‖
−1
.
Remark 2.1 The following equalities hold good:
(2. 4) ρi
α ◦ h ∂f ◦ h
∂x i =
(
θ˜ı
α
∂f
∂κ˜ı
)
◦ h, ∀f ∈ F (N ) .
and
(2. 5) (
Lγ
αβ ◦ h
) (
ρk
γ ◦ h
)
=
(
ρi
α ◦ h
) ∂
(
ρk
β ◦ h
)
∂x i −
(
ρj
β ◦ h
) ∂
(
ρk
α ◦ h
)
∂x j .
3 Interior Diﬀerential Systems
Let
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
be an object of the category GLA.
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
Proposition 3.1 The set
AF F
put
= ⋃
(U,ξ U )∈AF T M , (V,s V )∈AF F
U ∩h−1(V )⁄=φ
{(
U ∩ h−1 (V ) , ¯sU ∩h−1(V )
)}
is a vector ﬁbred m + p-atlas for the vector bundle (h∗F, h ∗ν, M ) .
6
If z = zα tα ∈ Γ (F, ν, N ) , then we obtain the section
Z = (zα ◦ h) Tα ∈ Γ (h∗F, h ∗ν, M )
such that Z (x) = z (h (x)) , for any x ∈ U ∩ h−1 (V ) .
Theorem 3.1 Let
( h∗F
ρ , Id M
)
be the Bv-morphism of (h∗F, h ∗ν, M ) source and
(T M, τ M , M ) target, where
(3. 1) h∗F
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
(3. 2)
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
is a Lie algebroid which is called the pull-back Lie algebroid of the generalized Lie alge-
broid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
Deﬁnition 3.1 Any vector subbundle ( E, π, M ) of the pull-back vector bundle
(h∗F, h ∗ν, M ) will be called interior diﬀerential system (IDS) of the generalized Lie
algebroid (
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
In particular, if h = Id N = η, then we obtain the deﬁnition of the IDS of a Lie
algebroid. (see [2])
Remark 3.1 If ( E, π, M ) is an IDS of the generalized Lie algebroid
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
7
Proposition 3.1 If (E, π, M ) is an IDS of the generalized Lie algebroid
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
Deﬁnition 3.2 The IDS ( E, π, M ) of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
will be called involutive if [ S, T ]h∗F ∈ Γ (E, π, M ) , for any S, T ∈ Γ (E, π, M ) .
Proposition 3.2 If (E, π, M ) is an IDS of the generalized Lie algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
and {S1, ..., S r} is a base for the F (M )-submodule (Γ (E, π, M ) , +, ·) then (E, π, M )
is involutive if and only if [Sa, S b]h∗F ∈ Γ (E, π, M ) , for any a, b ∈ 1, r.
4 Exterior diﬀerential calculus
We propose an exterior diﬀerential calculus in the general fr amework of generalized Lie
algebroids. As any Lie algebroid can be regarded as a general ized Lie algebroid, in
particular, we obtain a new point of view over the exterior di ﬀerential calculus for Lie
algebroids. Let
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
∈ |GLA| be.
Deﬁnition 4.1 For any q ∈ N we denote by (Σ q, ◦) the permutations group of the
set {1, 2, ..., q } .
Deﬁnition 4.2 We denoted by Λ q (F, ν, N ) the set of q-linear applications
Γ (F, ν, N )q ω− − − → F (N )
(z1, ..., z q) ↦− → ω (z1, ..., z q)
such that
ω
(
zσ (1), ..., z σ (q)
)
= sgn (σ ) · ω (z1, ..., z q)
for any z1, ..., z q ∈ Γ (F, ν, N ) and for any σ ∈ Σ q.
The elements of Λ q (F, ν, N ) will be called diﬀerential forms of degree q or diﬀerential
q-forms.
Remark 4.1 If ω ∈ Λ q (F, ν, N ), then ω (z1, ..., z, ..., z, ...z q ) = 0 . Therefore, if ω ∈
Λ q (F, ν, N ), then
ω (z1, ..., z i, ..., z j , ...z q) = −ω (z1, ..., z j , ..., z i, ...z q) .
Theorem 4.1 If q ∈ N , then (Λ q (F, ν, N ) , +, ·) is a F (N )-module.
Deﬁnition 4.3 If ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N ), then the ( q + r)-form ω ∧ θ
deﬁned by
ω ∧ θ (z1, ..., z q+r) = ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) ω
(
zσ (1), ..., z σ (q)
)
θ
(
zσ (q+1), ..., z σ (q+r)
)
= 1
q!r!
∑
σ ∈Σ q+r
sgn (σ ) ω
(
zσ (1), ..., z σ (q)
)
θ
(
zσ (q+1), ..., z σ (q+r)
)
,
8
for any z1, ..., z q+r ∈ Γ (F, ν, N ) , will be called the exterior product of the forms ω and θ.
Using the previous deﬁnition, we obtain
Theorem 4.2 The following aﬃrmations hold good:
1. If ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N ), then
(4. 1) ω ∧ θ = (−1)q·r θ ∧ ω.
2. For any ω ∈ Λ q (F, ν, N ), θ ∈ Λ r (F, ν, N ) and η ∈ Λ s (F, ν, N ) we obtain
(4. 2) ( ω ∧ θ) ∧ η = ω ∧ (θ ∧ η) .
3. For any ω, θ ∈ Λ q (F, ν, N ) and η ∈ Λ s (F, ν, N ) we obtain
(4. 3) ( ω + θ) ∧ η = ω ∧ η + θ ∧ η.
4. For any ω ∈ Λ q (F, ν, N ) and θ, η ∈ Λ s (F, ν, N ) we obtain
(4. 4) ω ∧ (θ + η) = ω ∧ θ + ω ∧ η.
5. For any f ∈ F (N ), ω ∈ Λ q (F, ν, N ) and θ ∈ Λ s (F, ν, N ) we obtain
(4. 5) ( f · ω ) ∧ θ = f · (ω ∧ θ) = ω ∧ (f · θ) .
Theorem 4.3 If
Λ ( F, ν, N ) = ⊕
q≥0
Λ q (F, ν, N ) ,
then
(Λ ( F, ν, N ) , +, ·, ∧)
is a F (N )-algebra. This algebra will be called the exterior diﬀerential algebra of the
vector bundle (F, ν, N ) .
Remark 4.2 If
{
tα , α ∈
1, p
}
is the coframe associated to the frame
{
tα , α ∈ 1, p
}
of the vector bundle ( F, ν, N ) in the vector local ( n + p)-chart U , then
tα 1 ∧ ... ∧ tα q
(
zα
1 tα , ..., z α
q tα
)
= 1
q! det
‖
‖
‖
‖
‖
‖
zα 1
1 ... z α q
1
... ... ...
zα 1
q ... z α q
q
‖
‖
‖
‖
‖
‖
,
for any q ∈
1, p.
Remark 4.3 If
{
tα , α ∈ 1, p
}
is the coframe associated to the frame
{
tα , α ∈ 1, p
}
of the vector bundle ( F, ν, N ) in the vector local ( n + p)-chart U , then, for any q ∈ 1, p
we deﬁne C q
p exterior diﬀerential forms of the type
tα 1 ∧ ... ∧ tα q
such that 1 ≤ α 1 < ... < α q ≤ p.
The set
{tα 1 ∧ ... ∧ tα q , 1 ≤ α 1 < ... < α q ≤ p}
is a base for the F (N )-module
(Λ q (F, ν, N ) , +, ·) .
9
Therefore, if ω ∈ Λ q (F, ν, N ), then
ω = ω α 1...α q tα 1 ∧ ... ∧ tα q .
In particular, if ω is an exterior diﬀerential p-form ω, then we can written
ω = a · t1 ∧ ... ∧ tp,
where a ∈ F (N ) .
Deﬁnition 4.4 If
ω = ω α 1...α q tα 1 ∧ ... ∧ tα q ∈ Λ q (F, ν, N )
such that
ω α 1...α q ∈ C r (N ) ,
for any 1 ≤ α 1 < ... < α q ≤ p, then we will say that the q-form ω is diﬀerentiable of
C r-class.
Deﬁnition 4.5 For any z ∈ Γ (F, ν, N ), the F (N )-multilinear application
Λ ( F, ν, N )
Lz− − − − − →Λ ( F, ν, N ) ,
deﬁned by
Lz (f ) = Γ ( T h ◦ ρ, h ◦ η) z (f ) , ∀f ∈ F (N )
and
Lzω (z1, ..., z q) = Γ ( T h ◦ ρ, h ◦ η) z (ω ((z1, ..., z q)))
−
q∑
i=1
ω
((
z1, ..., [z, z i]F,h , ..., z q
))
,
for any ω ∈ Λ q (F, ν, N ) and z1, ..., z q ∈ Γ (F, ν, N ) , will be called the covariant Lie
derivative with respect to the section z.
Theorem 4.4 If z ∈ Γ (F, ν, N ) , ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N ), then
(4. 6) Lz (ω ∧ θ) = Lzω ∧ θ + ω ∧ Lzθ.
Proof. Let z1, ..., z q+r ∈ Γ (F, ν, N ) be arbitrary. Since
Lz (ω ∧ θ) (z1, ..., z q+r) = Γ ( T h ◦ ρ, h ◦ η) z ((ω ∧ θ) (z1, ..., z q+r))
−
q+r∑
i=1
(ω ∧ θ)
((
z1, ..., [z, z i]F,h , ..., z q+r
))
= Γ ( T h ◦ ρ, h ◦ η) z




∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) · ω
(
zσ (1), ..., z σ (q)
)
·θ
(
zσ (q+1), ..., z σ (q+r)
))
−
q+r∑
i=1
(ω ∧ θ)
((
z1, ..., [z, z i]F,h , ..., z q+r
))
= ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) · Γ (T h ◦ ρ, h ◦ η) z
(
ω
(
zσ (1), ..., z σ (q)
))
·θ
(
zσ (q+1), ..., z σ (q+r)
)
+ ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) · ω
(
zσ (1), ..., z σ (q)
)
·Γ (T h ◦ ρ, h ◦ η) z
(
θ
(
zσ (q+1), ..., z σ (q+r)
))
− ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ )
·
q∑
i=1
ω
(
zσ (1), ...,
[
z, z σ (i)
]
F,h , ..., z σ (q+r)
)
· θ
(
zσ (q+1), ..., z σ (q+r)
)
10
− ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ )
q+r∑
i=q+1
ω
(
zσ (1), ..., z σ (q)
)
·θ
(
zσ (q+1), ...,
[
z, z σ (i)
]
F,h , ..., z σ (q+r)
)
= ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) Lzω
(
zσ (1), ...,
[
z, z σ (i)
]
F,h , ..., z σ (q+r)
)
·θ
(
zσ (q+1), ..., z σ (q+r)
)
+ ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ )
q+r∑
i=q+1
ω
(
zσ (1), ..., z σ (q)
)
·Lzθ
(
zσ (q+1), ...,
[
z, z σ (i)
]
F,h , ..., z σ (q+r)
)
= (Lzω ∧ θ + ω ∧ Lzθ) (z1, ..., z q+r)
it results the conclusion of the theorem. q.e.d.
Deﬁnition 4.6 For any z ∈ Γ (F, ν, N ), the F (N )-multilinear application
Λ ( F, ν, N )
iz− − − →Λ ( F, ν, N )
Λ q (F, ν, N ) ∋ ω ↦− → izω ∈ Λ q−1 (F, ν, N ) ,
where
izω (z2, ..., z q) = ω (z, z 2, ..., z q) ,
for any z2, ..., z q ∈ Γ (F, ν, N ), will be called the interior product associated to the
section z.
For any f ∈ F (N ), we deﬁne izf = 0.
Remark 4.4 If z ∈ Γ (F, ν, N ) , ω ∈ Λ p (F, ν, N ) and U is an open subset of N such
that z|U = 0 or ω |U = 0, then ( izω )|U = 0.
Theorem 4.5 If z ∈ Γ (F, ν, N ), then for any ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N )
we obtain
(4. 7) iz (ω ∧ θ) = izω ∧ θ + (−1)q ω ∧ izθ.
Proof. Let z1, ..., z q+r ∈ Γ (F, ν, N ) be arbitrary. We observe that
iz1 (ω ∧ θ) (z2, ..., z q+r) = ( ω ∧ θ) (z1, z 2, ..., z q+r)
= ∑
σ (1)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) · ω
(
zσ (1), ..., z σ (q)
)
· θ
(
zσ (q+1), ..., z σ (q+r)
)
= ∑
1=σ (1)<σ (2)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) · ω
(
z1, z σ (2), ..., z σ (q)
)
· θ
(
zσ (q+1), ..., z σ (q+r)
)
+ ∑
σ (1)<...<σ (q)
1=σ (q+1)<σ (q+2)<...<σ (q+r)
sgn (σ ) · ω
(
zσ (1), ..., z σ (q)
)
· θ
(
z1, z σ (q+2), ..., z σ (q+r)
)
= ∑
σ (2)<...<σ (q)
σ (q+1)<...<σ (q+r)
sgn (σ ) · iz1ω
(
zσ (2), ..., z σ (q)
)
· θ
(
zσ (q+1), ..., z σ (q+r)
)
+ ∑
σ (1)<...<σ (q)
σ (q+2)<...<σ (q+r)
sgn (σ ) · ω
(
zσ (1), ..., z σ (q)
)
· iz1θ
(
zσ (q+2), ..., z σ (q+r)
)
.
11
In the second sum, we have the permutation
σ =
( 1 ... q q + 1 q + 2 ... q + r
σ (1) ... σ (q) 1 σ (q + 2) ... σ (q + r)
)
.
We observe that σ = τ ◦ τ′, where
τ =
( 1 2 ... q + 1 q + 2 ... q + r
1 σ (1) ... σ (q) σ (q + 2) ... σ (q + r)
)
and
τ′ =
( 1 2 ... q q + 1 q + 2 ... q + r
2 3 ... q + 1 1 q + 2 ... q + r
)
.
Since τ (2) < ... < τ (q + 1) and τ′ has q inversions, it results that
sgn (σ ) = ( −1)q · sgn (τ) .
Therefore,
iz1 (ω ∧ θ) (z2, ..., z q+r) = ( iz1ω ∧ θ) (z2, ..., z q+r)
+ (−1)q ∑
τ(2)<...<τ (q)
τ(q+2)<...<τ (q+r)
sgn (τ) · ω
(
zτ (2), ..., z τ (q)
)
· iz1θ
(
zτ(q+2), ..., z τ (q+r)
)
= (iz1ω ∧ θ) (z2, ..., z q+r) + (−1)q (ω ∧ iz1θ) (z2, ..., z q+r) .
q.e.d.
Theorem 4.6 For any z, v ∈ Γ (F, ν, N ) we obtain
(4. 8) Lv ◦ iz − iz ◦ Lv = i[z,v ]F,h
.
Proof. Let ω ∈ Λ q (F, ν, N ) be arbitrary. Since
iz (Lvω ) (z2, ...z q) = Lvω (z, z 2, ...z q)
= Γ ( T h ◦ ρ, h ◦ η) v (ω (z, z 2, ..., z q)) − ω
(
[v, z ]F,h , z 2, ..., z q
)
−
q∑
i=2
ω
((
z, z 2, ..., [v, z i]F,h , ..., z q
))
= Γ ( T h ◦ ρ, h ◦ η) v (izω (z2, ..., z q)) −
q∑
i=2
izω
(
z2, ..., [v, z i]F,h , ..., z q
)
−i[v,z ]F (z2, ..., z q) =
(
Lv (izω ) − i[v,z ]F,h
)
(z2, ..., z q) ,
for any z2, ..., z q ∈ Γ (F, ν, N ) it result the conclusion of the theorem. q.e.d.
Deﬁnition 4.7 If f ∈ F (N ) and z ∈ Γ (F, ν, N ) , then we deﬁne
dF f (z) = Γ ( T h ◦ ρ, h ◦ η) (z) f.
Theorem 4.7 The F (N )-multilinear application
Λ q (F, ν, N ) dF
− − − →Λ q+1 (F, ν, N )
ω ↦− → dω
12
deﬁned by
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
(4. 9) Lz = dF ◦ iz + iz ◦ dF , ∀z ∈ Γ (F, ν, N ) .
This F (N )-multilinear application will be called the exterior diﬀerentiation operator
for the exterior diﬀerential algebra of the generalized Lie a lgebroid ((F, ν, N ), [, ]F,h , (ρ, η )).
Proof. We verify the property (4 . 9) Since
(
iz0 ◦ dF )
ω (z1, ..., z q) = dω (z0, z 1, ..., z q)
=
q∑
i=0
(−1)i Γ (T h ◦ ρ, h ◦ η) zi (ω (z0, z 1, ..., ˆzi, ..., z q))
+ ∑
0≤i<j
(−1)i+j ω
(
[zi, z j]F,h , z 0, z 1, ..., ˆzi, ..., ˆzj , ..., z q
)
= Γ ( T h ◦ ρ, h ◦ η) z0 (ω (z1, ..., z q))
+
q∑
i=1
(−1)i Γ (T h ◦ ρ, h ◦ η) zi (ω (z0, z 1, ..., ˆzi, ..., z q))
+
q∑
i=1
(−1)i ω
(
[z0, z i]F,h , z 1, ..., ˆzi, ..., z q
)
+ ∑
1≤i<j
(−1)i+j ω
(
[zi, z j]F,h , z 0, z 1, ..., ˆzi, ..., ˆzj , ..., z q
)
= Γ ( T h ◦ ρ, h ◦ η) z0 (ω (z1, ..., z q))
−
q∑
i=1
ω
(
z1, ..., [z0, z i]F,h , ..., z q
)
−
q∑
i=1
(−1)i−1 Γ (T h ◦ ρ, h ◦ η) zi (iz0ω ((z1, ..., ˆzi, ..., z q)))
− ∑
1≤i<j
(−1)i+j−2 iz0ω
((
[zi, z j]F,h , z 1, ..., ˆzi, ..., ˆzj , ..., z q
))
=
(
Lz0 − dF ◦ iz0
)
ω (z1, ..., z q) ,
for any z0, z 1, ..., z q ∈ Γ (F, ν, N ) it results that the property (4 . 9) is satisﬁed.
In the following, we verify the uniqueness of the operator dF .
Let d′F be an another exterior diﬀerentiation operator satisfying t he property (4 . 9) .
Let S =
{
q ∈ N : dF ω = d′F ω, ∀ω ∈ Λ q (F, ν, N )
}
be.
Let z ∈ Γ (F, ν, N ) be arbitrary.
We observe that (4 . 9) is equivalent with
(1) iz ◦
(
dF − d′F )
+
(
dF − d′F )
◦ iz = 0.
Since izf = 0, for any f ∈ F (N ) , it results that
((
dF − d′F )
f
)
(z) = 0 , ∀f ∈ F (N ) .
Therefore, we obtain that
(2) 0 ∈ S.
13
In the following, we prove that
(3) q ∈ S =⇒ q + 1 ∈ S
Let ω ∈ Λ p+1 (F, ν, N ) be arbitrary . Since izω ∈ Λ q (F, ν, N ), using the equality (1),
it results that
iz ◦
(
dF − d′F )
ω = 0.
We obtain that,
((
dF − d′F )
ω
)
(z0, z 1, ..., z q) = 0 , for any z1, ..., z q ∈ Γ (F, ν, N ) .
Therefore dF ω = d′F ω, namely q + 1 ∈ S.
Using the Peano’s Axiom and the aﬃrmations (2) and (3) it results that S = N.
Therefore, the uniqueness is veriﬁed. q.e.d.
Note that if ω = ω α 1...α q tα 1 ∧ ... ∧ tα q ∈ Λ q (F, ν, N ), then
dF ω
(
tα 0, t α 1, ..., t α q
)
=
q∑
i=0
(−1)i θ
˜k
α i
∂ω α 0,..., ˆα i...α q
∂κ˜k
+∑
i<j
(−1)i+j Lα
α iα j · ω α,α 0,..., ˆα i,..., ˆα j ,...,α q .
Therefore, we obtain
(4. 10)
dF ω =
( q∑
i=0
(−1)i θ
˜k
α i
∂ω α 0,..., ˆα i...α q
∂κ˜k
+∑
i<j
(−1)i+j Lα
α iα j · ω α,α 0,..., ˆα i,..., ˆα j,...,α q
)
tα 0 ∧ tα 1 ∧ ... ∧ tα q .
Remark 4.5 If dF is the exterior diﬀerentiation operator for the generalized Lie
algebroid (
(F, ν, N ) , [, ]F,h , (ρ, η )
)
,
ω ∈ Λ q (F, ν, N ) and U is an open subset of N such that ω |U = 0, then
(
dF ω
)
|U = 0.
Theorem 4.8 The exterior diﬀerentiation operator dF given by the previous theorem
has the following properties:
1. For any ω ∈ Λ q (F, ν, N ) and θ ∈ Λ r (F, ν, N ) we obtain
(4. 11) dF (ω ∧ θ) = dF ω ∧ θ + (−1)q ω ∧ dF θ.
2. For any z ∈ Γ (F, ν, N ) we obtain
(4. 12) Lz ◦ dF = dF ◦ Lz.
3. dF ◦ dF = 0.
Proof.
1. Let S =
{
q ∈ N : dF (ω ∧ θ) = dF ω ∧ θ + (−1)q ω ∧ dF θ, ∀ω ∈ Λ q (F, ν, N )
}
be. Since
dF (f ∧ θ) (z, v ) = dF (f · θ) (z, v )
= Γ ( T h ◦ ρ, h ◦ η) z (f ω (v)) − Γ (T h ◦ ρ, h ◦ η) v (f ω (z)) − f ω
(
[z, v ]F,h
)
= Γ ( T h ◦ ρ, h ◦ η) z (f ) · ω (v) + f · Γ (T h ◦ ρ, h ◦ η) z (ω (v))
−Γ (T h ◦ ρ, h ◦ η) v (f ) · ω (z) − f · Γ (T h ◦ ρ, h ◦ η) v (ω (z)) − f ω
(
[z, v ]F,h
)
= dF f (z) · ω (v) − dF f (v) · ω (z) + f · dF ω (z, v )
=
(
dF f ∧ ω
)
(z, v ) + (−1)0 f · dF ω (z, v )
=
(
dF f ∧ ω
)
(z, v ) + (−1)0 (
f ∧ dF ω
)
(z, v ) , ∀z, v ∈ Γ (F, ν, N ) ,
14
it results that
(1. 1) 0 ∈ S.
In the following we prove that
(1. 2) q ∈ S =⇒ q + 1 ∈ S.
Without restricting the generality, we consider that θ ∈ Λ r (F, ν, N ) . Since
dF (ω ∧ θ) (z0, z 1, ..., z q+r) = iz0 ◦ dF (ω ∧ θ) (z1, ..., z q+r)
= Lz0 (ω ∧ θ) (z1, ..., z q+r) − dF ◦ iz0 (ω ∧ θ) (z1, ..., z q+r)
= (Lz0ω ∧ θ + ω ∧ Lz0θ) (z1, ..., z q+r)
−
[
dF ◦ (iz0ω ∧ θ + (−1)q ω ∧ iz0θ)
]
(z1, ..., z q+r)
=
(
Lz0ω ∧ θ + ω ∧ Lz0θ −
(
dF ◦ iz0ω
)
∧ θ
)
(z1, ..., z q+r)
−
(
(−1)q−1 iz0ω ∧ dF θ + (−1)q dF ω ∧ iz0θ
)
(z1, ..., z q+r)
− (−1)2q ω ∧ dF ◦ iz0θ (z1, ..., z q+r)
=
((
Lz0ω − dF ◦ iz0ω
)
∧ θ
)
(z1, ..., z q+r)
+ω ∧
(
Lz0θ − dF ◦ iz0θ
)
(z1, ..., z q+r)
+
(
(−1)q iz0ω ∧ dF θ − (−1)q dF ω ∧ iz0θ
)
(z1, ..., z q+r)
=
[ ((
iz0 ◦ dF )
ω
)
∧ θ + (−1)q+1 dF ω ∧ iz0θ
]
(z1, ..., z q+r)
+
[
ω ∧
((
iz0 ◦ dF )
θ
)
+ (−1)q iz0ω ∧ dF θ
]
(z1, ..., z q+r)
=
[
iz0
(
dF ω ∧ θ
)
+ (−1)q iz0
(
ω ∧ dF θ
)]
(z1, ..., z q+r)
=
[
dF ω ∧ θ + (−1)q ω ∧ dF θ
]
(z1, ..., z q+r) ,
for any z0, z 1, ..., z q+r ∈ Γ (F, ν, N ), it results (1 . 2) .
Using the Peano’s Axiom and the aﬃrmations (1 . 1) and (1 . 2) it results that S = N.
Therefore, it results the conclusion of aﬃrmation 1.
2. Let z ∈ Γ (F, ν, N ) be arbitrary.
Let S =
{
q ∈ N :
(
Lz ◦ dF )
ω =
(
dF ◦ Lz
)
ω, ∀ω ∈ Λ q (F, ν, N )
}
be.
Let f ∈ F (N ) be arbitrary. Since
(
dF ◦ Lz
)
f (v) = iv ◦
(
dF ◦ Lz
)
f =
(
iv ◦ dF )
◦ Lzf
= (Lv ◦ Lz) f −
((
dF ◦ iv
)
◦ Lz
)
f
= (Lv ◦ Lz) f − L[z,v ]F,h f + dF ◦ i[z,v ]F,h f − dF ◦ Lz (ivf )
= (Lv ◦ Lz) f − L[z,v ]F,h f + dF ◦ i[z,v ]F,h f − 0
= (Lv ◦ Lz) f − L[z,v ]F,h f + dF ◦ i[z,v ]F,h f − Lz ◦ dF (ivf )
= (Lz ◦ iv)
(
dF f
)
− L[z,v ]F,h f + dF ◦ i[z,v ]F,h f
= (iv ◦ Lz)
(
dF f
)
+ L[z,v ]F,h f − L[z,v ]F,h f
= iv ◦
(
Lz ◦ dF )
f =
(
Lz ◦ dF )
f (v) , ∀v ∈ Γ (F, ν, N ) ,
it results that
(2. 1) 0 ∈ S.
In the following we prove that
(2. 2) q ∈ S =⇒ q + 1 ∈ S.
15
Let ω ∈ Λ q (F, ν, N ) be arbitrary. Since
(
dF ◦ Lz
)
ω (z0, z 1, ..., z q) = iz0 ◦
(
dF ◦ Lz
)
ω (z1, ..., z q)
=
(
iz0 ◦ dF )
◦ Lzω (z1, ..., z q)
=
[
(Lz0 ◦ Lz) ω −
((
dF ◦ iz0
)
◦ Lz
)
ω
]
(z1, ..., z q)
=
[
(Lz0 ◦ Lz) ω − L[z,z 0]F,h ω
]
(z1, ..., z q)
+
[
dF ◦ i[z,z 0]F,h
ω − dF ◦ Lz (iz0ω )
]
(z1, ..., z q)
ip.
=
[
(Lz0 ◦ Lz) ω − L[z,z 0]F,h
ω
]
(z1, ..., z q)
+
[
dF ◦ i[z,z 0]F,h ω − Lz ◦ dF (iz0ω )
]
(z1, ..., z q)
=
[
(Lz ◦ iz0)
(
dF ω
)
− L[z,z 0]F,h ω + dF ◦ i[z,z 0]F,h ω
]
(z1, ..., z q)
=
[
(iz0 ◦ Lz)
(
dF ω
)
+ L[z,z 0]F,h ω − L[z,z 0]F,h ω
]
(z1, ..., z q)
= iz0 ◦
(
Lz ◦ dF )
ω (z1, ..., z q)
=
(
Lz ◦ dF )
ω (z0, z 1, ..., z q) , ∀z0, z 1, ..., z q ∈ Γ (F, ν, N ) ,
it results (2 . 2) .
Using the Peano’s Axiom and the aﬃrmations (2 . 1) and (2 . 2) it results that S = N.
Therefore, it results the conclusion of aﬃrmation 2.
3. It is remarked that
iz ◦
(
dF ◦ dF )
=
(
iz ◦ dF )
◦ dF = Lz ◦ dF −
(
dF ◦ iz
)
◦ dF
= Lz ◦ dF − dF ◦ Lz + dF ◦
(
dF ◦ iz
)
=
(
dF ◦ dF )
◦ iz,
for any z ∈ Γ (F, ν, N ) .
Let ω ∈ Λ q (F, ν, N ) be arbitrary. Since
(
dF ◦ dF )
ω (z1, ..., z q+2) = izq+2 ◦ ... ◦ iz1 ◦
(
dF ◦ dF )
ω = ...
= izq+2 ◦
(
dF ◦ dF )
◦ izq+1 (ω (z1, ..., z q))
= izq+2 ◦
(
dF ◦ dF )
(0) = 0 , ∀z1, ..., z q+2 ∈ Γ (F, ν, N ) ,
it results the conclusion of aﬃrmation 3. q.e.d.
Theorem 4.9 If dF is the exterior diﬀerentiation operator for the exterior di f-
ferential F(N )-algebra (Λ( F, ν, N ), +, ·, ∧), then we obtain the structure equations of
Maurer-Cartan type
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
16
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
Using the equalities (1) and (2) it results the structure equ ation ( C1).
Let ˜ı ∈
1, n be arbitrarily. Since
dF κ˜ı(tα ) = θ˜ı
α , ∀α ∈
1, p
it results the structure equation ( C2). q.e.d.
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
and dh∗F is the
exterior diﬀerentiation operator for the exterior diﬀeren tial F (M )-algebra
(Λ ( h∗F, h ∗ν, M ) , +, ·, ∧) ,
then we obtain the following structure equations of Maurer- Cartan type
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
1, m .
This equations will be called the structure equations of Maurer-Cartan type associ-
ated to the pull-back Lie algebroid
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
.
Theorem 4.10 ( of Cartan type) Let (E, π, M ) be an IDS of the generalized Lie
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
Proof: Let {S1, ..., S r} be a base for the F (M )-submodule (Γ ( E, π, M ) , +, ·)
17
Let {Sr+1, ..., S p} ∈ Γ (h∗F, h ∗ν, M ) such that
{S1, ..., S r, S r+1, ..., S p}
is a base for the F (M )-module
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
is a base for the F (M )-module
(
Γ
( ∗
h∗F ,
∗
h∗ν, M
)
, +, ·
)
.
For any a, b ∈ 1, r and α, β ∈ r + 1, p , we have the equalities:
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
1, r ∧ α, β, γ ∈ r + 1, p are real local functions such
that Aα
bc = −Aα
cb and C α
βγ = −C α
γβ .
Using the formula
(2)
dh∗F Θ α (Sb, S c) = Γ
( h∗F
ρ , Id M
)
Sb (Θ α (Sc))−Γ
( h∗F
ρ , Id M
)
Sc (Θ α (Sb))−Θ α ([Sb, S c]h∗F ) ,
we obtain that
(3) Aα
bc = −Θ α ([Sb, S c]h∗F ) , ∀
(
b, c ∈
1, r ∧ α ∈ r + 1, p
)
.
We admit that ( E, π, M ) is an involutive IDS of the generalized Lie algebroid(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
As
[Sb, S c]h∗F ∈ Γ (E, π, M ) , ∀b, c ∈ 1, r
18
it results that
Θ α ([Sb, S c]h∗F ) = 0 , ∀
(
b, c ∈ 1, r ∧ α ∈ r + 1, p
)
.
Therefore,
Aα
bc = 0, ∀
(
b, c ∈
1, r ∧ α ∈ r + 1, p
)
and we obtain
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
βγ Θ β ∈ Λ 1 (h∗F, h ∗ν, M ) , ∀α, β ∈ r + 1, p
it results the ﬁrst implication.
Conversely, we admit that it exists
Ω α
β ∈ Λ 1 (h∗F, h ∗ν, M ) , α, β ∈
r + 1, p
such that
(4) dh∗F Θ α = Σ β ∈
r+1,p Ω α
β ∧ Θ β , ∀α ∈
r + 1, p.
Using the aﬃrmations (1) , (2) and (4) we obtain that
Aα
bc = 0, ∀
(
b, c ∈
1, r ∧ α ∈ r + 1, p
)
.
Using the aﬃrmation (3), we obtain
Θ α ([Sb, S c]h∗F ) = 0 , ∀
(
b, c ∈ 1, r ∧ α ∈ r + 1, p
)
.
Therefore,
[Sb, S c]h∗F ∈ Γ (E, π, M ) , ∀b, c ∈ 1, r.
Using the Proposition 3.2, we obtain the second implication. q.e.d.
Let
(
(F ′, ν ′, N ′) , [, ]F ′,h ′ , (ρ′, η ′)
)
be an another generalized Lie algebroid.
Deﬁnition 4.8 For any morphism ( ϕ, ϕ 0) of
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
source and ( (
F ′, ν ′, N ′)
, [, ]F ′,h ′ ,
(
ρ′, η ′) )
target we deﬁne the application
Λ q (F ′, ν ′, N ′)
(ϕ,ϕ 0)∗
− − − − − − →Λ q (F, ν, N )
ω ′ ↦− → (ϕ, ϕ 0)∗ ω ′ ,
where
((ϕ, ϕ 0)∗ ω ′) (z1, ..., z q) = ω ′ (Γ (ϕ, ϕ 0) (z1) , ..., Γ (ϕ, ϕ 0) (zq)) ,
for any z1, ..., z q ∈ Γ (F, ν, N ) .
19
Remark 4.5 It is remarked that the Bv-morphism (T h ◦ ρ, h ◦ η) is a GLA-morphism of
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
source and (
(T N, τ N , N ) , [, ]T N,Id N , (Id T N, Id N )
)
target.
Moreover, for any ˜ı ∈ 1, n , we obtain
(T h ◦ ρ, h ◦ η)∗ (
dκ˜ı)
= dF κ˜ı,
where d is the exterior diﬀerentiation operator associated to the ex terior diﬀerential Lie
F (N )-algebra
(Λ ( T N, τ N , N ) , +, ·, ∧) .
Theorem 4.11 If (ϕ, ϕ 0) is a morphism of
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
iΓ( ϕ,ϕ 0)zω ′)
.
3. If N = N ′ and
(T h ◦ ρ, h ◦ η) =
(
T h′ ◦ ρ′, h ′ ◦ η′)
◦ (ϕ, ϕ 0) ,
then we obtain
(4. 15) (ϕ, ϕ 0)∗ ◦ dF ′
= dF ◦ (ϕ, ϕ 0)∗ .
Proof. 1. Let ω ′ ∈ Λ q (F ′, ν ′, N ′) and θ′ ∈ Λ r (F ′, ν ′, N ′) be arbitrary. Since
(ϕ, ϕ 0)∗ (
ω ′ ∧ θ′)
(z1, ..., z q+r) =
(
ω ′ ∧ θ′)
(Γ (ϕ, ϕ 0) z1, ..., Γ ( ϕ, ϕ 0) zq+r)
= 1
(q + r)!
∑
σ ∈Σ q+r
sgn (σ ) · ω ′ (Γ (ϕ, ϕ 0) z1, ..., Γ ( ϕ, ϕ 0) zq)
·θ′ (Γ (ϕ, ϕ 0) zq+1, ..., Γ ( ϕ, ϕ 0) zq+r)
= 1
(q + r)!
∑
σ ∈Σ q+r
sgn (σ ) · (ϕ, ϕ 0)∗ ω ′ (z1, ..., z q) (ϕ, ϕ 0)∗ θ′ (zq+1, ..., z q+r)
=
(
(ϕ, ϕ 0)∗ ω ′ ∧ (ϕ, ϕ 0)∗ θ′)
(z1, ..., z q+r) ,
for any z1, ..., z q+r ∈ Γ (F, ν, N ), it results the conclusion of aﬃrmation 1.
20
2. Let z ∈ Γ (F, ν, N ) and ω ′ ∈ Λ q (F ′, ν ′, N ′) be arbitrary. Since
iz ((ϕ, ϕ 0)∗ ω ′) (z2, ..., z q) = ω ′ (Γ (ϕ, ϕ 0) z, Γ (ϕ, ϕ 0) z2, ..., Γ ( ϕ, ϕ 0) zq)
= iΓ( ϕ,ϕ 0)zω ′ (Γ (ϕ, ϕ 0) z2, ..., Γ ( ϕ, ϕ 0) zq)
= (ϕ, ϕ 0)∗ (
iΓ( ϕ,ϕ 0)zω ′)
(z2, ..., z q) ,
for any z2, ..., z q ∈ Γ (F, ν, N ), it results the conclusion of aﬃrmation 2 .
3. Let ω ′ ∈ Λ q (F ′, ν ′, N ′) and z0, ..., z q ∈ Γ (F, ν, N ) be arbitrary. Since
(
(ϕ, ϕ 0)∗ dF ′
ω ′
)
(z0, ..., z q) =
(
dF ′
ω ′
)
(Γ (ϕ, ϕ 0) z0, ..., Γ ( ϕ, ϕ 0) zq)
=
q∑
i=0
(−1)i Γ (T h′ ◦ ρ′, h ′ ◦ η′) (Γ (ϕ, ϕ 0) zi)
·ω ′
((
Γ (ϕ, ϕ 0) z0, Γ (ϕ, ϕ 0) z1, ..., ˆΓ (ϕ, ϕ 0) zi, ..., Γ ( ϕ, ϕ 0) zq
))
+ ∑
0≤i<j
(−1)i+j · ω ′
(
Γ (ϕ, ϕ 0) [zi, z j]F,h , Γ (ϕ, ϕ 0) z0, Γ (ϕ, ϕ 0) z1, ...,
· ˆΓ (ϕ, ϕ 0) zi, ..., ˆΓ (ϕ, ϕ 0) zj, ..., Γ ( ϕ, ϕ 0) zq
)
and
dF ((ϕ, ϕ 0)∗ ω ′) (z0, ..., z q)
=
q∑
i=0
(−1)i Γ (T h ◦ ρ, h ◦ η) (zi) · ((ϕ, ϕ 0)∗ ω ′) (z0, ..., ˆzi, ..., z q)
+ ∑
0≤i<j
(−1)i+j · ((ϕ, ϕ 0)∗ ω ′)
(
[zi, z j]F,h , z 0, ..., ˆzi, ..., ˆzj , ..., z q
)
=
q∑
i=0
(−1)i Γ (T h ◦ ρ, h ◦ η) (zi) · ω ′
(
Γ (ϕ, ϕ 0) z0, ..., ˆΓ ( ϕ, ϕ 0) zi, ..., Γ ( ϕ, ϕ 0) zq
)
+ ∑
0≤i<j
(−1)i+j · ω ′
(
Γ (ϕ, ϕ 0) [zi, z j]F,h , Γ (ϕ, ϕ 0) z0, Γ (ϕ, ϕ 0) z1, ...,
ˆΓ (ϕ, ϕ 0) zi, ..., ˆΓ ( ϕ, ϕ 0) zj, ..., Γ ( ϕ, ϕ 0) zq
)
it results the conclusion of aﬃrmation 3. q.e.d.
Deﬁnition 4.9 For any q ∈ 1, n we deﬁne
Z q (F, ν, N ) = {ω ∈ Λ q (F, ν, N ) : dω = 0} ,
the set of closed diﬀerential exterior q-forms and
Bq (F, ν, N ) =
{
ω ∈ Λ q (F, ν, N ) : ∃η ∈ Λ q−1 (F, ν, N ) | dη = ω
}
,
the set of exact diﬀerential exterior q-forms.
5 Exterior Diﬀerential Systems
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
21
Deﬁnition 5.1 Any ideal (I, +, ·) of the exterior diﬀerential algebra of the pull-back
Lie algebroid
(
(h∗F, h ∗ν, M ) , [, ]h∗F ,
( h∗F
ρ , Id M
))
closed under diﬀerentiation operator
dh∗F , namely dh∗F I ⊆ I , will be called diﬀerential ideal of the generalized Lie algebroid(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
In particular, if h = Id N = η, then we obtain the deﬁnition of the diﬀerential ideal
of a Lie algebroid.(see[2])
Deﬁnition 5.2 Let ( I, +, ·) be a diﬀerential ideal of the generalized Lie algebroid(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
If it exists an IDS ( E, π, M ) such that for all k ∈ N∗ and ω ∈ I ∩ Λ k (h∗F, h ∗ν, M )
we have ω (u1, ..., u k) = 0 , for any u1, ..., u k ∈ Γ (E, π, M ) , then we will say that ( I, +, ·)
is an exterior diﬀerential system (EDS) of the generalized Li e algebroid
(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
.
In particular, if h = Id N = η, then we obtain the deﬁntion of the EDS of a Lie
algebroid.(see[2])
Theorem 5.1 ( of Cartan type) The IDS (E, π, M ) of the generalized Lie algebroid(
(F, ν, N ) , [, ]F,h , (ρ, η )
)
is involutive, if and only if the ideal generated by the F (M )-
submodule
(
Γ
(
E0, π 0, M
)
, +, ·
)
is an EDS of the same generalized Lie algebroid.
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
Using the Theorems 4.8 and 4.10 we obtain
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
22
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
Using the Theorem 4.10, it results that ( E, π, M ) is an involutive IDS. q.e.d.
