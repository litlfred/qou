---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-003-167-we-prepare-some-notations-for-formulating-th
section_title: "We prepare some notations for formulating the generalized Springe r cor-"
section_number: 16.7
pages: 19-24
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spa ces."
---
respondence. We deﬁne SGιθ as the set of triples, ( L, O1, E1), up to the conjugation
action of H, where L is a θ-stable Levi subgroup of a θ-stable parabolic subgroup P ,
and (O1, E1) is a cuspidal pair in Lιθ
uni. Since LH≃ (GL1)a×SON0 withN0 =N−2a
(Remark 16.4), we have
(16.2) SGιθ≃ CN :={(N0,ν,σ )|N≥N0 : odd, ( ν,σ )∈ Ψ (0)
N0}
Takeξ = (N0,ν,σ )∈ CN corresponding to ( L, O1, E1)∈ SGιθ , and put Kξ =
IC(
O 1, E1)[dim O1]. Since Kξ is an LH -equivariant perverse sheaf on Lιθ, one can
consider the complex ind G
PKξ on Gιθ
uni.
For each ξ = (N0,ν,σ )∈ CN , deﬁne a map Γξ : Pa↦→Ψ N as follows. Put
~σ = (σ1,...,σ N ) = (σ1,...,σ N0, 1,..., 1) for σ = (σ1,...,σ N0). For µ∈ Pa, put
λ =ν + 2µ∈ PN , and deﬁne
(16.3) Γξ(µ) = (λ, ~σ)∈ Ψ N.
The following result gives the generalized Springer correspondence for Gιθ
uni,
which is an analogue of Theorem 5.1.
20
Theorem 16.8 ([SY]). (i) For ξ∈ CN ≃ SGιθ , indG
PKξ is a semisimple per-
verse sheaf on Gιθ
uni, equipped with Sa-action, and is decomposed as
indG
PKξ =
⨁
µ ∈Pa
Vµ⊗ IC(
O, E )[dim O],
whereΓξ(µ)↔ (O, E ) under the identiﬁcation Ψ N≃ NGιθ
(ii) Forξ∈ SGιθ , let N (ξ)
Gιθ be the subset of NGιθ corresponding to{Γξ(µ)|µ∈
Pa}⊂ Ψ N . Then we have
NGιθ =
∐
ξ∈SGιθ
N (ξ)
Gιθ.
(iii) The correspondence (O, E )↔Γξ(µ)↔Vµ gives a bijection
NGιθ≃
∐
ξ∈SGιθ
S∧
a (generalized Springer correspondence )
§17. Exotic symmetric spaces of higher level, the case H =SpN
In this section, we consider the Springer correspondence for the exotic symmetric
spaces of higher level associated to symplectic groups. As was rem arked in Section
11, the crucial diﬃculty in this case is that the number of H-orbits is not necessarily
ﬁnite if r≥ 3.
Assume H = SpN≃ Sp(V ), and consider Gιθ
uni×Vr−1 (r≥ 1), with diagonal
action of H. Let M1⊂···⊂ Mn⊂V be the total isotropic ﬂag whose stabilizer in
H is equal to BH. Consider the variety
~X ={(x, v,gBH)∈Gιθ
uni×Vr−1× BH|g−1xg∈Bιθ,g −1v∈Mr−1
n }
and deﬁne a map π : ~X →Gιθ
uni×Vr−1 by (x, v,gBH)↦→(x, v).
Let Qn,r ={m = (m1,...,m r)∈ Zr
≥0| ∑ mi = n}, and put Q0
n,r ={m∈
Qn,r |mr = 0}. For given m∈ Qn,r , deﬁne p1,...,p r−1 bypk = ∑ k
i=1mi. Put, for
m∈ Q0
n,r ,
Xm =
⋃
g∈H
g(Uιθ×
∏
1≤i<r
Mpi).
Let πm : π−1(Xm)→ Xm be the restriction of π on π−1(Xm). Then πm is
proper, surjective, but π−1(Xm) is not necessarily smooth nor irreducible.
Let Wn,r =Sn ⋉ (Z/rZ)n be the complex reﬂection group. We denote by Pn,r
the set of r-partitions λ = (λ(1),...,λ (r)) such that ∑
i|λ(i)| =n. Then it is known
that
(17.1) W ∧
n,r ≃ Pn,r, ~Vλ↔ λ.
21
For m∈ Q0
n,r , we deﬁne a subset P(m)0⊂ Pn,r by
P(m)0 ={λ∈ Pn,r ||λ(i)| =mi (i≤r− 2),|λ(r−1)| +|λ(r)| =mr−1}.
The following result holds for any r≥ 1. Note that if r = 2, this coincides with
the formula in Theorem 13.3. Also note that since Xm has inﬁnitely many H-orbits,
we need to construct a suitable variety Xλ instead of an H-orbit Oλ .
Theorem 17.1 ([S3]). Assume m∈ Q0
n,r , and put dm = dim Xm. Then (πm)∗ ¯Ql[dm]
is a semisimple perverse sheaf on Xm, equipped with Wn,r -action, and is decomposed
as
(πm)∗ ¯Ql[dm]≃
⨁
λ ∈P(m)0
~Vλ⊗ IC(X λ, ¯Ql)[dimXλ ],
where Xλ is an H-stable, smooth, irreducible, locally closed sub-variety of Gιθ
uni×
Vr−1. If r≥ 3, Xλ is an inﬁnite union of H-orbits.
Assume m∈ Q0
n,r , and take λ∈ P(m)0. Then Xλ⊂ Xm. Put
(17.2) dλ = (dim Xm− dimXλ )/2.
Forz = (x, v)∈ Xm, deﬁne the Springer ﬁbre BH
z ≃π−1(z) by
(17.3) BH
z ={gBH∈ BH|g−1xg∈Bιθ,g −1v∈Mr−1
n }
Then Hi(BH
z , ¯Ql) has a structure of Wn,r -module, which is called the Springer rep-
resentation of Wn,r . As a corollary of Theorem 17.1, we obtain the following result,
which is the Springer correspondence for the complex reﬂection gr oup Wn,r .
Proposition 17.2. There exists an open dense subset X 0
λ of Xλ satisfying the fol-
lowing. For z∈ X 0
λ , dim BH
z = dλ , and H 2dλ (BH
z , ¯Ql)≃ ~Vλ . In particular, the
map Xλ↦→H 2dλ (BH
z , ¯Ql) gives a bijective correspondence
{Xλ| λ∈ Pn,r} =
∐
m∈Q0n,r
{Xλ| λ∈ P(m)0}≃
∐
m∈Q0n,r
{ ~Vλ| λ∈ P(m)0} =W ∧
n,r.
§18. Exotic symmetric spaces, the case H =SO2n+1
In this section, assume that H = SO2n+1. Consider the variety Gιθ
uni×Vr−1
and the isotropic ﬂag ( Mi)i similarly as in Section 17. We ﬁx ξ = (N0,ν,σ )↔
(L, O1, E1)∈ CGιθ , hence LH≃ (GL1)a×SON0 with N0 = N− 2a. Consider the
diagram
(18.1) Lιθ α
←−−−ˆX
ψ
−−−→~X
π
−−−→Gιθ×Vr−1,
22
where
ˆX ={(x, v,g )∈Gιθ×Vr−1×H|g−1xg∈Pιθ,g −1v∈Mr−1
a },
~X ={(x, v,gPH)∈Gιθ×Vr−1×H/PH|g−1xg∈Pιθ,g −1v∈Mr−1
a },
and the maps are deﬁned as
ψ : (x, v,g )↦→(x, v,gPH), π : (x,gPH)↦→x, α : (x, v,g )↦→ηP (g−1xg),
where ηP : Pιθ→ Lιθ is the natural map induced from the projection P → L≃
P/UP . Note that unless P =B, the map ~X →Lιθ can not be deﬁned directly.
For m∈ Qa,r , put
Xm =
⋃
g∈H
(
η−1
P (Lιθ
uni)×
∏
1≤i<r
Mpi
)
As the restriction of the diagram (18.1) on Xm, we have a diagram
(18.2) Lιθ α m
←−−−ˆXm
ψ m
−−−→~Xm
π m
−−−→Xm,
where ~Xm =π−1(Xm), ˆXm =ψ−1( ~Xm), andαm,ψ m,π m are deﬁned as restrictions
of α,ψ,π , respectively.
Put Kξ = IC(
O 1, E1)[dim O1]. We deﬁne a complex ~K (m)
ξ on ~Xm by the condi-
tion
(18.3) α∗
mKξ[a]≃ψ∗
m ~K (m)
ξ [b],
where a (resp. b) is the dimension of the ﬁbre of αm (resp. ψm). We consider the
complex (πm)∗ ~K (m)
ξ on Xm.
Put P(m) ={λ∈ Pa,r ||λ(i)| =mi (1≤i≤r)}. Since the number of H-orbits
is inﬁnite for Gιθ
uni, we need to construct subvarieties Xλ as in Section 17.
Proposition 18.1. Let m∈ Qa,r . For each λ∈ P(m), one can deﬁne a subvariety
Xλ of Xm and an H-orbit O[λ ] in Gιθ
uni satisfying the following;
(i) Xλ is a locally closed, smooth, irreducible, H-stable subset of Xm.
(ii) The map (x, v)↦→x gives a locally trivial ﬁbration fλ :Xλ→ O[λ ],
whose ﬁbre is isomorphic to an open dense subset of ∏
1≤i<rMpi.
(iii) If r = 1, Xλ coincides with O[λ ] = O2λ (1)+ν.
For O = O[λ ], there exists a unique pair ( O, E )∈ N (ξ)
G appearing in ind G
PKξ.
We deﬁne a local sytem Eλ on Xλ by Eλ =f ∗
λ E .
23
Theorem 18.2 ([S4]). For each m∈ Qa,r , (πm)∗ ~K (m)
ξ is a semisimple perverse
sheaf on Xm, equipped with Wa,r -action, and is decomposed as
(πm)∗ ~K (m)
ξ ≃
⨁
λ ∈P(m)
~Vλ⊗ IC(X λ, Eλ )[dimXλ ].
In particular, for each ξ∈ SGιθ , we have a bijection
{Xλ| λ∈ Pa,r} =
∐
m∈Qa,r
{Xλ| λ∈ P(m)}≃
∐
m∈Qa,r
{ ~Vλ| λ∈ P(m)} =W ∧
a,r
Remark 18.4. The construction of ( πm)∗ ~K (m)
ξ is essentially the same as the
construction of the induction ind G
PKξ in Section 16, which is a variant of the induc-
tion functor of Lusztig. But in contrast to the cases of reductive groups or of Gιθ
uni
for H =SO2n+1, (πm)∗ ~K (m)
ξ is not a priori a semisimple complex. So the previous
discussion can not be applied directly, and we need a special care.
§19. Symmetric spaces in characteristic 2
The discussion in Section 11 makes sense even if p = 2, and one can deﬁne a
symmetric space Gιθ
uni associated to classical groups in characteristic 2. In this case,
a diﬀerent phenomenon appears since the fundamental propertie s given in Section
10 do not hold. However, an analogue of the Springer corresponde nce still holds for
them. The Springer correspondence for Gιθ
uni was studied in [DSY], which we brieﬂy
explain below.
Let V ′ be an N-dimensional vector space over k with p = 2, and consider
G =GL(V ′). The involution θ :G→G is deﬁned as in Section 11, and we consider
Gθ and Gιθ. Here Gθ≃ Sp(V ), where V is an 2 n-dimensional subspace of V ′ if
N = 2n + 1 and V = V ′ if N = 2n. Put H = Sp(V ) and h = Lie H. Then
h = sp(V ): the symplectic Lie algebra with p = 2. θ induces an involution θ on
g = LieG, and we consider the subalgebra gθ ={x∈ g|θ(x) = x}. The case where
N is even, the situation is rather simple, namely we have
Proposition 19.1. Assume that N = 2n. Then
(i) gθ≃ LieH = sp(V ): the symplectic Lie algebra over k.
(ii) Gιθ
uni≃ gθ
nil, compatible with the action of H.
By the above result, considering the Springer correspondence fo r Gιθ
uni is equiv-
alent to considering it for sp(V )nil. The Springer correspondence for the nilpotent
cone of the Lie algebras in characteristic 2 was established by T. Xue [X]. Thus the
Springer correspondence for Gιθ
uni follows from her result. In particular, Gιθ
uni/∼H is
in bijection with Pn, 2, via Oλ↔ λ , and the following formula holds.
(19.1) π∗ ¯Ql[dimGιθ
uni]≃
⨁
λ ∈Pn, 2
~Vλ⊗ IC(
O λ, ¯Ql)[dim Oλ ],
where ~Vλ is the irreducible representation of Wn, 2 corresponding to λ∈ Pn, 2.
24
Next consider the case where N is odd. In this case, a quite diﬀerent situation
occurs. We have
Proposition 19.2. Assume that N = 2n + 1. Then
(i) Gιθ
uni≃ gθ
nil, compatible with the action of H≃Gθ.
(ii) gθ≃ h×V× k, where H acts on h×V diagonally, and acts on k trivially.
Remarks 19.3. (i) Lie Gθ⁄= gθ.
(ii) The number of H-orbits in gθ
nil is inﬁnite, hence the number of Gθ-orbits in Gιθ
uni
is inﬁnite. (This gives a counter example for Proposition 10.2 in the cas e p = 2.)
(iii) The situation is similar to the exotic case, namely the action of H on Gιθ
corresponds to the diagonal action of H on h×V . But the nilpotent part gθ
nil is
not exactly the same as hnil×V . In our case, we have gθ
nil = ( hnil×V )∩ gnil for
g = LieG = gl(V ′).
The Springer correspondence for Gιθ was established in [DSY]. Note that in this
case, it occurs a very similar phenomenon as in the case of exotic sym metric space
of level r = 3. In fact, since Gιθ
uni has inﬁnitely many H-orbits, we need to consider
the varieties such as Xλ in Section 17. In this case, Xλ is parametrized by λ∈ Pn, 3,
and the Springer correspondence is described by using the complex reﬂection group
Wn, 3.
The reason why W ∧
n, 3 appears in the Springer correspondence is explained as
follows. It is proved by Kato [K2], by using the deformation argument s on the
schemes over Z, that the Springer correspondence for the exotic symmetric spa ce
g−θ
nil× V for H = Sp(V) in the case p⁄= 2 can be interpreted by the Springer
correspondence for sp(V )nil in the case p = 2. Thus, as a generalization of his result,
one can expect that
(19.2) sp(V )nil×V≈ g−θ
nil× V2≈Gιθ
uni× V2.
In [DSY] it is proved that this certainly holds. Note that the right han d side is the
exotic symmetric space of r = 3.
