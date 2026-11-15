---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-016-17-exotic-symmetric-spaces-of-higher-level-the-c
section_title: "§17. Exotic symmetric spaces of higher level, the case H = SpN"
section_number: null
pages: 20-23
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
toc_source: inferred
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spaces."
---
In this section, we consider the Springer correspondence for the exotic symmetric
spaces of higher level associated to symplectic groups. As was remarked in Section
11, the crucial diﬃculty in this case is that the number of H-orbits is not necessarily
ﬁnite if r ≥3.
Assume H = SpN ≃Sp(V ), and consider Gιθ
uni × V r−1 (r ≥1), with diagonal
action of H. Let M1 ⊂· · · ⊂Mn ⊂V be the total isotropic ﬂag whose stabilizer in
H is equal to BH. Consider the variety
f
X = {(x, v, gBH) ∈Gιθ
uni × V r−1 × BH | g−1xg ∈Bιθ, g−1v ∈Mr−1
n
}
and deﬁne a map π : f
X →Gιθ
uni × V r−1 by (x, v, gBH) 7→(x, v).
Let Qn,r = {m = (m1, . . . , mr) ∈Zr
≥0 | P mi = n}, and put Q0
n,r = {m ∈
Qn,r | mr = 0}. For given m ∈Qn,r, deﬁne p1, . . . , pr−1 by pk = Pk
i=1 mi. Put, for
m ∈Q0
n,r,
Xm =
[
g∈H
g(Uιθ ×
Y
1≤i<r
Mpi).
Let πm : π−1(Xm) →Xm be the restriction of π on π−1(Xm). Then πm is
proper, surjective, but π−1(Xm) is not necessarily smooth nor irreducible.
Let Wn,r = Sn ⋉(Z/rZ)n be the complex reﬂection group. We denote by Pn,r
the set of r-partitions λ = (λ(1), . . . , λ(r)) such that P
i |λ(i)| = n. Then it is known
that
(17.1)
W ∧
n,r ≃Pn,r,
eVλ ↔λ.
21
For m ∈Q0
n,r, we deﬁne a subset P(m)0 ⊂Pn,r by
P(m)0 = {λ ∈Pn,r | |λ(i)| = mi (i ≤r −2), |λ(r−1)| + |λ(r)| = mr−1}.
The following result holds for any r ≥1. Note that if r = 2, this coincides with
the formula in Theorem 13.3. Also note that since Xm has inﬁnitely many H-orbits,
we need to construct a suitable variety Xλ instead of an H-orbit Oλ.
Theorem 17.1 ([S3]). Assume m ∈Q0
n,r, and put dm = dim Xm. Then (πm)∗¯Ql[dm]
is a semisimple perverse sheaf on Xm, equipped with Wn,r-action, and is decomposed
as
(πm)∗¯Ql[dm] ≃
M
λ∈P(m)0
eVλ ⊗IC(Xλ, ¯Ql)[dim Xλ],
where Xλ is an H-stable, smooth, irreducible, locally closed sub-variety of Gιθ
uni ×
V r−1. If r ≥3, Xλ is an inﬁnite union of H-orbits.
Assume m ∈Q0
n,r, and take λ ∈P(m)0. Then Xλ ⊂Xm. Put
(17.2)
dλ = (dim Xm −dim Xλ)/2.
For z = (x, v) ∈Xm, deﬁne the Springer ﬁbre BH
z ≃π−1(z) by
(17.3)
BH
z = {gBH ∈BH | g−1xg ∈Bιθ, g−1v ∈Mr−1
n
}
Then Hi(BH
z , ¯Ql) has a structure of Wn,r-module, which is called the Springer rep-
resentation of Wn,r. As a corollary of Theorem 17.1, we obtain the following result,
which is the Springer correspondence for the complex reﬂection group Wn,r.
Proposition 17.2. There exists an open dense subset X0
λ of Xλ satisfying the fol-
lowing. For z ∈X0
λ, dim BH
z = dλ, and H2dλ(BH
z , ¯Ql) ≃eVλ. In particular, the
map Xλ 7→H2dλ(BH
z , ¯Ql) gives a bijective correspondence
{Xλ | λ ∈Pn,r} =
a
m∈Q0n,r
{Xλ | λ ∈P(m)0} ≃
a
m∈Q0n,r
{eVλ | λ ∈P(m)0} = W ∧
n,r.
§18. Exotic symmetric spaces, the case H = SO2n+1
In this section, assume that H = SO2n+1. Consider the variety Gιθ
uni × V r−1
and the isotropic ﬂag (Mi)i similarly as in Section 17. We ﬁx ξ = (N0, ν, σ) ↔
(L, O1, E1) ∈CGιθ, hence LH ≃(GL1)a × SON0 with N0 = N −2a. Consider the
diagram
(18.1)
Lιθ
α
←−−−
X
ψ
−−−→
f
X
π
−−−→Gιθ × V r−1,
22
where
c
X = {(x, v, g) ∈Gιθ × V r−1 × H | g−1xg ∈P ιθ, g−1v ∈Mr−1
a
},
f
X = {(x, v, gPH) ∈Gιθ × V r−1 × H/PH | g−1xg ∈P ιθ, g−1v ∈Mr−1
a
},
and the maps are deﬁned as
ψ : (x, v, g) 7→(x, v, gPH),
π : (x, gPH) 7→x,
α : (x, v, g) 7→ηP(g−1xg),
where ηP : P ιθ →Lιθ is the natural map induced from the projection P →L ≃
P/UP. Note that unless P = B, the map f
X →Lιθ can not be deﬁned directly.
For m ∈Qa,r, put
Xm =
[
g∈H

η−1
P (Lιθ
uni) ×
Y
1≤i<r
Mpi

As the restriction of the diagram (18.1) on Xm, we have a diagram
(18.2)
Lιθ
αm
←−−−
c
Xm
ψm
−−−→
f
Xm
πm
−−−→Xm,
where f
Xm = π−1(Xm),
c
Xm = ψ−1( f
Xm), and αm, ψm, πm are deﬁned as restrictions
of α, ψ, π, respectively.
Put Kξ = IC(O1, E1)[dim O1]. We deﬁne a complex eK(m)
ξ
on f
Xm by the condi-
tion
(18.3)
α∗
mKξ[a] ≃ψ∗
m eK(m)
ξ
[b],
where a (resp. b) is the dimension of the ﬁbre of αm (resp. ψm). We consider the
complex (πm)∗eK(m)
ξ
on Xm.
Put P(m) = {λ ∈Pa,r | |λ(i)| = mi (1 ≤i ≤r)}. Since the number of H-orbits
is inﬁnite for Gιθ
uni, we need to construct subvarieties Xλ as in Section 17.
Proposition 18.1. Let m ∈Qa,r. For each λ ∈P(m), one can deﬁne a subvariety
Xλ of Xm and an H-orbit O[λ] in Gιθ
uni satisfying the following;
(i) Xλ is a locally closed, smooth, irreducible, H-stable subset of Xm.
(ii) The map (x, v) 7→x gives a locally trivial ﬁbration fλ : Xλ →O[λ],
whose ﬁbre is isomorphic to an open dense subset of Q
1≤i<r Mpi.
(iii) If r = 1, Xλ coincides with O[λ] = O2λ(1)+ν.
For O = O[λ], there exists a unique pair (O, E ) ∈N (ξ)
G
appearing in indG
P Kξ.
We deﬁne a local sytem Eλ on Xλ by Eλ = f ∗
λE .
23
Theorem 18.2 ([S4]). For each m ∈Qa,r, (πm)∗eK(m)
ξ
is a semisimple perverse
sheaf on Xm, equipped with Wa,r-action, and is decomposed as
(πm)∗eK(m)
ξ
≃
M
λ∈P(m)
eVλ ⊗IC(Xλ, Eλ)[dim Xλ].
In particular, for each ξ ∈SGιθ, we have a bijection
{Xλ | λ ∈Pa,r} =
a
m∈Qa,r
{Xλ | λ ∈P(m)} ≃
a
m∈Qa,r
{eVλ | λ ∈P(m)} = W ∧
a,r
Remark 18.4.
The construction of (πm)∗eK(m)
ξ
is essentially the same as the
construction of the induction indG
P Kξ in Section 16, which is a variant of the induc-
tion functor of Lusztig. But in contrast to the cases of reductive groups or of Gιθ
uni
for H = SO2n+1, (πm)∗eK(m)
ξ
is not a priori a semisimple complex. So the previous
discussion can not be applied directly, and we need a special care.
