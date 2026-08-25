---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds"
section_id: sec-006-6-foth-leitner
section_title: "Foth, Leitner"
section_number: 6
pages: 6-7
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
doc_brief: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-ve ctor ﬁelds on quaternionic ﬂag manifolds, which geometrically determ ine"
---
We begin by deﬁning an element Λ of ∧4sp2 in terms of the following basis
for sp2:
E =
(
0 1
−1 0
)
Sx =
(
0 x
x 0
)
Hx =
( x 0
0 −x
)
Mx =
( x 0
0 x
)
wherex is one of{i, j, k}. For convenience we denote S−x :=−Sx,H−x :=−Hx,
and M−x :=−Mx. We now can note the following commutator relations:
[Mx,E ] = 0 [ Hx,E ] = 2·Sx [Sx,E ] = 2·Hx
[Mx,My] = [Hx,Hy] = [Sx,Sy] =
{
2·Mx·y x⁄=y
0 x =y
[Sx,Hy] =
{
0 x⁄=y
−2·E x =y
[Sx,My] =
{
0 x =y
2·Sx·y x⁄=y
[Hx,My] =
{
0 x =y
2·Hx·y x⁄=y
We may now deﬁne:
Λ := E∧Si∧Sj∧Sk.
and denoting by Λ L and Λ R the left and right invariant 4-vector ﬁelds on Sp(2)
with value Λ at the identity element, we let:
κ = Λ L− ΛR.
Proposition 4.1 The 4-vector ﬁeld κ is a quatrisson structure on Sp(2). More-
over,κ descends to a vector ﬁeld, ℵ, on HP1≃ Σ\Sp(2) inducing a Σ -invariant
quatrisson structure on HP1 called the Bruhat quatrisson structure
Proof. The fact that κ is a quatrisson structure on Sp(2) is nothing more than
the fact that [κ,κ ]∈ ⋀ 7χ(Sp(2)) = 0. To show that ℵ is Σ-invariant, and hence
descends, we may apply the same formalism of the Poisson case and s how that
for any X∈ s we have adX (Λ) = [ X, Λ] = 0. This follows readily from the
above commutator relations and the Leibniz rule of the Schouten br acket. It is
clear that [ℵ,ℵ] = 0. ✷
We can make use of the Bruhat decomposition to describe the vecto r ﬁeld ex-
plicitly. As above, we denote by Ce andC(12) the cells of Fn corresponding to
Quatrisson structures and H-ﬂags 7
the North pole and the H components. It is clear, that at the North pole κ is
the zero vector. For x∈C (12) we choose a convenient coset representative in
Sp(2), namely:
kx = 1√
1 +ρ2
·
(
−¯v 1
1 v
)
,
where ρ =|v| =√v¯v. In fact, the identiﬁcation of S4 as a natural SO(5)≃
Sp(2)/(Z/2) -invariant submanifold of R5 with H plus the point at inﬁnity using
stereographic projection sends v∈ H to a point in S4 at the height 1 − 1
1 +|v|2
and the same Sp(1)-angular coordinate.
To computeℵ atx, we identify T xSp(2) with T eSp(2) by right translations
so that we have Λ R = Λ and Λ L is simply conjugation of Λ by kx. We have
thus expressed ℵ = f (v)∂v1∧∂v2∧∂v3∧∂v4 in terms of the coordinates v =
v1 +v2· i +v3· j +v4· k. We would like more natural coordinates for H, namely
if v = ρ· exp(θ1· i)exp(θ2· j)exp(θ3· k)∈ H, then we have ℵ = g(ρ)
ρ3 ∂ρ∧ Θ,
for Θ = ∂θ1∧∂θ2∧∂θ3 - the Sp(1)-invariant 3-vector ﬁeld on Sp(1)≃S3. To
ﬁnd g(ρ), we divide ℵ by its value at v = 0, the South pole. After a computer
assisted computation 1 we see that g(ρ) = (1 + 3ρ4)
(1 +ρ2)3 . Thus we have proved that:
Proposition 4.2 The invariant quatrisson structure on S4≃ HP1 is given by:
χ := (1 +ρ2)4
ρ3 ∂ρ∧ Θ
and the Bruhat quatrisson structure is given by:
ℵ = (1 +ρ2)(1 + 3ρ4)
ρ3 ∂ρ∧ Θ.
In particular we have that:
ℵ = 1 + 3ρ4
(1 +ρ2)3χ.
One can easily see that ℵ has rank four everywhere except for at the North
pole, where it vanishes. Thus the two cells are characterized by the rank ofℵ.
