---
doc_id: ant-v14-n7-s-p02
doc_title: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values"
section_id: sec-001-1-preliminaries
section_title: "Preliminaries"
section_number: 1
pages: 6-14
source_pdf: ant-v14-n7-s-p02.pdf
source_sha256: fd2121feb180b282
toc_source: inferred
doc_brief: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values — 10 sections: Front matter; Introduction; Preliminaries"
---
In this section we establish the framework of this paper. We review some deﬁnitions and properties about
the pro-unipotent fundamental groupoid of P1 \ {0, µN, ∞}, some results from [Jarossay 2015] and we
add to them a few new deﬁnitions and notations. Throughout this paper, N and N∗will denote the set of
nonnegative and positive integers, respectively.
1A. The pro-unipotent fundamental groupoid of P1 \ {0, µN, ∞}.
1A1. The de Rham realization. Let X be P1 \ {0, µN, ∞} over the p-adic ﬁeld K, with the notations
of Section 0A. The de Rham pro-unipotent fundamental groupoid πun,dR
1
(X), in the sense of [Deligne
1989], is a groupoid in pro-afﬁne schemes over X. Its base points are the points of X and the nonzero
tangent vectors at {0, µN, ∞} ⊂P1, called tangential base-points. The groupoid structure is deﬁned by
the morphisms πun,dR
1
(X K, z, y) × πun,dR
1
(X K, y, x) →πun,dR
1
(X K, z, x) for any base-points x, y, z. By
[loc. cit., Section 12.9], each πun,dR
1
(X, y, x) is canonically isomorphic to the spectrum of the shufﬂe
Hopf algebra OX,e0∪µN over the alphabet e0∪µN = {ex | x ∈{0}∪µN(K)}. This isomorphism is compatible
with the groupoid structure.
Following [Deligne and Goncharov 2005], for any N-th root of unity ξ ∈µN(K), we denote by
5ξ,0 = πun,dR
1
(X,⃗1ξ,⃗10). Let f 7→f (ξ) be the isomorphism 51,0 →5ξ,0 induced by the automorphism
x 7→ξx of X by functoriality of πun,dR
1
.
Let K⟨⟨e0∪µN ⟩⟩be the noncommutative K-algebra of formal power series over the noncommuting
variables ex, x ∈{0∪µN(K)}. We will write an element f ∈K⟨⟨e0∪µN ⟩⟩as f ((ex)x) = f ((ex)x∈{0}∪µN(K))
or f (e0, (eξ)ξ) = f (e0, (eξ)ξ). The coefﬁcient in f of a word w on the alphabet e0∪µN is denoted by
f [w]. This notation extends by linearity to linear combinations of words, and if for any n ≥0 wn is
a linear combination of words of weight n, we denote by f
P∞
n=0 wn

= P∞
n=0 f [wn] if this series
converges. We have a canonical inclusion Spec(OX,e0∪µN )(K) ⊂K⟨⟨e0∪µN ⟩⟩; namely, Spec(OX,e0∪µN )(K)
is the group of elements satisfying the shufﬂe equation: for all words w, w′, f [w] f [w′] = f [wXw′]
where X is the shufﬂe product of words on the alphabet e0∪µN .
1A2. Motivic Galois action and byproducts. The motivic version of πun
1 (P1 \{0, µN, ∞}) is constructed
in [Deligne and Goncharov 2005, Section 5].
Let Gω be the motivic Galois group associated with the Tannakian category of mixed Tate motives
over kN unramiﬁed at p prime to N, and with the canonical ﬁber functor ω. There is a semidirect product
decomposition Gω = Gm ⋉Uω where Uω is pro-unipotent.
One has an action of Gω on 51,0. Let V ω be the group of automorphisms deﬁned in [Deligne and
Goncharov 2005, Section 5.10]. There is a morphism U ω →V ω sending the action of U ω on 51,0 to an
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1717
action of V ω on 51,0. This action makes 51,0 a torsor under V ω. Thus one can consider the isomorphism
of schemes V ω ≃51,0, v 7→v(110) where 110 is the canonical de Rham path in the sense of [Deligne
1989, Section 12]. This isomorphism sends the action of V ω on 51,0 to the Ihara action [Deligne and
Goncharov 2005, Section 5.11], namely, the group law ◦∫1,0 on 51,0 deﬁned by
g ◦∫1,0 f = g(e0, (eξ)ξ) × f (e0, (g(ξ)−1eξg(ξ))ξ).
(1-1)
The motivic Galois action of Gm on 51,0 is
τ : (λ, f ((ex)x)) 7→f ((λex)x),
(1-2)
i.e., λ acts by multiplying the term of weight n in f by λn, for all n ∈N. Let the collection of maps (τn)n∈N
be deﬁned by the equality P
n∈N τn( f )λn = τ(λ)( f ) for all λ. Namely, τn sends f = P
w word f [w]w to
P
w word, weight(w)=n f [w]w. These formulas also deﬁne an action on K⟨⟨e0∪µN ⟩⟩for which we will use
the same notations.
1A3. The crystalline realization. Let σ be the Frobenius automorphism of K. For α ∈N∗, let X(pα) be
the pull back of X by σ iterated α times.
Let φ be the Frobenius of the crystalline pro-unipotent fundamental groupoid of P1 \ {0, µN, ∞}
[Deligne 1989, Sections 11 and 13.6]. It is a σ-linear isomorphism of groupoids πun,dR
1
(X(p))
∼
−→
πun,dR
1
(X). For any α ∈N∗, the Frobenius iterated α times is φα = (σ α−1)∗φ ◦· · · ◦σ ∗(φ) ◦φ. It is a σ α-
linear isomorphism of groupoids πun,dR
1
(X(pα))
∼
−→πun,dR
1
(X). When α is divisible by o = log(p)/log(q),
then σ α = id, thus φα is K-linear in the usual sense, its source and target are the same, and it is equal to
φo iterated α/o times: we will write α = o˜α, and φo˜α = φ ˜α
o . We denote by φ−α = φ−1
α .
Let us now consider the Frobenius at base-points (1, 0) = (⃗11,⃗10): φα : 5(pα)
1,0
∼
−→51,0 where
5(pα)
1,0 = πun,dR
1
(X(pα),⃗11,⃗10). The noncommutative generating series of p-adic cyclotomic multiple zeta
values are 8p,α = τ(pα)φα(1) ∈51,0(K), and 8p,−α = φ−α(1) ∈5(pα)
1,0 (K). Let us denote again by
σ the map K⟨⟨e0∪µN ⟩⟩→K⟨⟨e0∪µN ⟩⟩deﬁned by applying the Frobenius σ of K to each coefﬁcient of a
formal power series. The formal properties of the Frobenius imply the following formulas:
τ(pα)φα : f ∈5(pα)
1,0 (K) 7→8p,α ◦∫1,0 σ −α( f ) ∈51,0(K),
(1-3)
φ−α : f ∈51,0(K) 7→8p,−α ◦∫1,0 τ(pα)σ α( f ) ∈5(pα)
1,0 (K).
(1-4)
One also has the other notion 8KZ
q
∈51,0(K) of a noncommutative generating series of p-adic cyclotomic
multiple zeta values, deﬁned by the following equality:
φlog(q)/log(p)(8KZ
q ) = 8KZ
q ,
(1-5)
where the existence and uniqueness of a ﬁxed point of φlog(q)/log(p) in 51,0(K) follows from the theory
of Coleman integration [Coleman 1982; Besser 2002; Vologodsky 2003]. Item (ii) of the notation below
will be justiﬁed by the results of Section 2.
1718
David Jarossay
Notation 1A.1.
(i) For any ˜α ∈Z \ {0}, let 8q,˜α = 8p,log(q)/log(p)·˜α.
(ii) Let 8q,−∞= 8KZ
q , and let 8q,∞be the inverse of 8q,−∞for the Ihara product ◦∫1,0.
(iii) For α ∈Z∪{±∞}\{0}, the p-adic cyclotomic multiple zeta values are the numbers ζq,˜α((ni)d; (ξi)d)=
(−1)d8q,˜α[end−1
0
eξd · · · en1−1
0
eξ1] (and similarly for ζp,α and 8p,α.)
1A4. Around the adjoint action Ad(e1). We use the convention that the adjoint action Ad(·)(x) on 51,0
is f 7→f −1x f (instead of the usual f 7→f x f −1, due to our convention of reading the groupoid
multiplication from the right to the left). The adjoint Ihara action, deﬁned in [Jarossay 2015], is the group
law on Ad51,0(e1) deﬁned by
h ◦
∫1,0
Ad f = f (e0, (h(ξ))ξ).
(1-6)
Let ˜51,0 be the subgroup scheme of 51,0 deﬁned by the equations f [e1] = f [e0] = 0 (see Section 1A1);
Ad(e1) induces an isomorphism of groups ( ˜51,0(K), ◦∫1,0)
∼
−→(Ad ˜51,0(K)(e1), ◦
∫1,0
Ad ).
By (1-1) and (1-2), one has a semidirect product Gm ⋉˜51,0, which acts on ˜51,0. Similarly, by (1-6)
and (1-2), one has a semidirect product Gm ⋉Ad ˜51,0(e1), which acts on Ad ˜51,0(e1). The map id × Ad(e1)
induces an isomorphism between these two group actions. For all f, g ∈51,0(K), λ ∈K ∗, n ∈N, we
have
g ◦∫1,0 (τ(λ)( f )) =
X
n∈N
λng ◦∫1,0 (τn f ).
(1-7)
We have
τn+1 ◦Ad(e1) = Ad(e1) ◦τn,
(1-8)
Adg(e1) ◦
∫1,0
Ad
τ(λ)
λ
Ad f (e1) =
X
n∈N
λn Adg(e1) ◦
∫1,0
Ad τn+1 Ad f (e1).
(1-9)
1B. An ultrametric structure on the K-points of the de Rham pro-unipotent fundamental groupoid.
As reviewed in Section 1A, each 5y,x = πun,dR
1
(P1 \ {0, µN, ∞}, y, x) is an afﬁne scheme over K, and
we have a canonical embedding 5y,x(K) ⊂K⟨⟨e0∪µN ⟩⟩. We consider now an enrichment of K⟨⟨e0∪µN ⟩⟩
into a ultrametric complete normed K-algebra: we review facts from [Jarossay 2015], and we add a
few complements. In particular, in Section 1B3 we add a notion of contraction and we apply it to the
Frobenius at base-points (1, 0).
1B1. From afﬁne schemes to ultrametric normed algebras over K. For n, d ∈N∗, let Wd∗,d(e0∪µN ), resp.
Wdn,d(e0∪µN ) the set of words on e0∪µN that are of depth d, resp. of weight n and depth d. Let 3 and D
be two formal variables.
Let K⟨⟨e0∪µN ⟩⟩<∞⊂K⟨⟨e0∪µN ⟩⟩, be the subset of the elements f such that, for each d ∈N∗, we
have supw∈Wd∗,d(e0∪µN )| f [w]|p < ∞. We say that the elements of K⟨⟨e0∪µN ⟩⟩<∞are bounded. Let
K⟨⟨e0∪µN ⟩⟩o(1) ⊂K⟨⟨e0∪µN ⟩⟩<∞be the subset of the elements f such that, for each d ∈N∗, we have
sup w ∈Wdn,d(e0∪µN )| f [w]|p
n→∞
−−−→0. We say that the elements of K⟨⟨e0∪µN ⟩⟩o(1) are summable.
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1719
Let
N3,D : f ∈K⟨⟨e0∪µN ⟩⟩7→
X
(n,d)∈N2
(
max
w∈Wdn,d(e0∪µN )| f [w]|p)3n Dd ∈R+[[3, D]],
and
ND : f ∈K⟨⟨e0∪µN ⟩⟩<∞7→
X
d∈N
(
sup
w∈Wd∗,d(e0∪µN )
| f [w]|p)Dd ∈R+[[D]].
One can check that these deﬁnitions give structures of complete normed ultrametric K-algebra on
K⟨⟨e0∪µN ⟩⟩, K⟨⟨e0∪µN ⟩⟩<∞and K⟨⟨e0∪µN ⟩⟩o(1) [Jarossay 2015, Proposition 1.3.3].
1B2. Compatibility between the ultrametric structure and the usual algebraic operations. By [Jarossay
2015, Proposition 1.3.6], the Ihara product (1-1), the adjoint Ihara action (1-6), and the action τ (1-2) are
continuous relative to the topologies deﬁned by N3,D and ND on 51,0(K) and the p-adic topology on
K. And for all f, g ∈51,0(K), λ ∈K ×, we have (by [Jarossay 2015, proof of Proposition 1.3.6])
N3,D(Ad f (e1)) ⩽3DN3,D( f ),
(1-10)
N3,D(g◦∫1,0 f ) ⩽N3,D(g) × N3,D( f ),
(1-11)
N3,D(τ(λ)( f ))(3, D) = N3,D( f )(λ3, D).
(1-12)
These equations imply similar equations with ND instead of N3,D by passing to supremums.
Let us add another compatibility, which concerns the maps τn deﬁned in Section 1A2.
Lemma 1B.1.
(i) For all n ∈N∗, for all f ∈K⟨⟨e0∪µN ⟩⟩, we have N3,D(τn( f )) ⩽N3,D( f ), and in
particular τn is a continuous linear map for the N3,D-topology.
(ii) K⟨⟨e0∪µN ⟩⟩<∞and K⟨⟨e0∪µN ⟩⟩o(1) are stable by τn.
(iii) For all f, g ∈51,0(K) and n ∈N we have
N3,D(Ad(g◦∫1,0τn( f ))(e1)) ⩽3DN3,D(g)N3,D( f ).
(1-13)
Proof. (i) and (ii) are clear from the deﬁnitions. (iii) follows from (1-10), (1-11) and (i).
□
1B3. The weighted Ihara action and contraction mappings. We deﬁne a notion of contraction mappings
within the topological framework reviewed above. The exponent −1∫1,0 means the inverse for the Ihara
product (1-1).
Deﬁnition 1B.2. Let κ ∈K ∗with |κ|p < 1. We say that a map ψ : 51,0(K) →51,0(K) is a κ-contraction
(with respect to N3,D and ◦∫1,0) if, for all f1, f2 ∈51,0(K), we have
N3,D(ψ( f2)−1R
1,0 ◦∫1,0 ψ( f1))(3, D) ⩽N3,D( f
−1R
1,0
2
◦∫1,0 f1)(κ3, D).
(1-14)
Indeed, let ψ : 51,0(K) →51,0(K) be a contraction in the sense of Deﬁnition 1B.2. Then, by the
submultiplicativity of the Ihara product with respect to N3,D ((1-11)) and the fact that K⟨⟨e0∪µN ⟩⟩is
complete with respect to the distance deﬁned by N3,D (Section 1B), a standard proof tells us that ψ
is continuous (with respect to N3,D) and has a unique ﬁxed point, equal to ﬁxψ = lima→∞ψa( f ) for
1720
David Jarossay
all f ∈51,0(K). Thus the contractions in the sense of Deﬁnition 1B.2 satisfy the usual properties of
contractions regarding ﬁxed points.
Deﬁnition 1B.3. Let (λ, g) ∈Gm(K) × 51,0(K). We call weighted Ihara action by g with parameter λ
and we denote by (λ, g)◦∫1,0 the map
51,0(K) →51,0(K),
f 7→(λ, g) ◦∫1,0 f = g ◦∫1,0 τ(λ)( f ).
We now relate the two previous deﬁnitions in the case where λ is small.
Proposition 1B.4.
(i) Let (λ, g) ∈Gm(K) × 51,0(K) such that |λ|p < 1. The map (λ, g)◦∫1,0 is a
λ-contraction. More precisely, the inequality (1-14) is an equality if κ = λ.
(ii) For all (λ, g) ∈Gm(K) × 51,0(K), the Ihara action of g weighted by λ is an automorphism of the
scheme 51,0 ×Spec Q Spec K, whose inverse is
f 7→τ(λ−1)(g−1∫1,0 ◦∫1,0 f ).
Proof. (i) We have
((λ, g) ◦∫1,0 ( f2))−1R
1,0 ◦∫1,0 ((λ, g) ◦∫1,0 ( f1)) = (g ◦∫1,0 τ(λ)( f2))−1R
1,0 g ◦∫1,0 τ(λ)( f1)
= τ(λ)( f2)−1R
1,0 ◦∫1,0 g−1R
1,0 ◦∫1,0 g ◦∫1,0 τ(λ)( f1)
= τ(λ)( f2)−1R
1,0 ◦∫1,0 τ(λ)( f1)
= τ(λ)(( f2)−1R
1,0 ◦∫1,0 f1).
Thus
N3,D((λ, g) ◦∫1,0 ( f2))−1R
1,0 ◦∫1,0 ((λ, g) ◦∫1,0 ( f1))(3, D) = N3,Dτ(λ)(( f2)−1R
1,0 ◦∫1,0 f1)(3, D)
= N3,D(( f2)−1R
1,0 ◦∫1,0 f1)(λ3, D)
by (1-12).
(ii) Follows from the deﬁnitions.
□
Knowing that we have a family of contractions, we consider their ﬁxed points and their iterations.
Deﬁnition 1B.5. Let (λ, g) 7→ﬁxλ,g be the ﬁxed point map which sends (λ, g) ∈{z ∈K | 0 < |z|p < 1}×
51,0(K) to the unique ﬁxed point of the weighted Ihara action (λ, g)◦∫1,0.
It follows from the deﬁnitions that the map ﬁxλ : g 7→ﬁxλ,g is an automorphism of the scheme
51,0×Spec QSpec K, whose inverse is ﬁx−1
λ : f 7→f ◦∫1,0τ(λ)( f )−1∫1,0. The ﬁxed point map is characterized
by the equation
g(e0, (eξ)ξ) ﬁxλ,g(λe0, λ(g−1
ξ eξgξ)ξ) = ﬁxλ,g(e0, (eξ)ξ).
(1-15)
Note that the inversion for the Ihara product on 51,0(K) is characterized by
g(e0, (eξ)ξ).g−1∫1,0(e0, (g−1
ξ eξgξ)ξ) = 1.
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1721
Deﬁnition 1B.6. Let a ∈N∗. Let the map of iteration a times of the Ihara action weighted by λ,
iter
∫1,0
a,λ : 51,0(K) →51,0(K) be deﬁned by g 7→ga(◦∫1,0,λ) where
ga(◦∫1,0,λ) = (λ, g) ◦∫1,0 · · · ◦∫1,0 (λ, g)
|
{z
}
a
◦∫1,01 = g ◦∫1,0 τ(λ)(g) ◦∫1,0 · · · ◦∫1,0 τ(λa−1)(g).
(1-16)
Thus ga(◦∫1,0,λ) is the unique element of 51,0(K) such that we have, for all f ∈51,0(K),
(λ, g) ◦∫1,0 · · · ◦∫1,0 (λ, g)
|
{z
}
a
◦∫1,0 f = (λa, ga(◦∫1,0,λ)) ◦∫1,0 f.
The iteration map is expressed in terms of the usual de Rham multiplication on 51,0(K) by
iter
∫1,0
a,λ (g) = g(e0, (eξ)ξ∈µN(K))g(λe0, (λ Adgξ (eξ))ξ) · · · g(λa−1e0, (λa−1 Adga−1
ξ
(eξ))ξ).
(1-17)
1B4. Application to the Frobenius. We apply the previous paragraphs to study the iteration of Frobenius
at the base-points (1, 0) which we view as a map φ : 5(p)
1,0(K) →51,0(K).
Lemma 1B.7. The map φ−log(q)/log(p) : 51,0(K) →51,0(K) is a (1/q)-contraction. If 5(p)
1,0(K) is
identiﬁed to 51,0(K) by the isomorphism deﬁned by e0 7→e0 and eξ(pα) 7→eξ for all ξ ∈µN(K), the map
φ−1 : 51,0(K) →5(p)
1,0(K) is a (1/p)-contraction.
Proof. This follows from the formula (1-3), from Proposition 1B.4 and from the fact that σ is an isometry
of K for the p-adic metric.
□
In the rest of this paper, for simplicity, we will deal mostly with the iterations of φ−log(q)/log(p). This
is sufﬁcient, knowing that, for any α ∈N∗, writing the Euclidean division α = r + u log(q)/log(p), we
have φα = φu
log(q)/log(p) ◦φr.
1C. Prime weighted cyclotomic multiple harmonic sums. The numbers harqα((ni)d; (ξi)d+1) will play
a central role; here, we formally explain how to study them.
1C1. The three frameworks of computation. Multiple polylogarithms are the solutions to the Knizhnik–
Zamolodchikov differential equation, which is the universal connection associated with πun,dR
1
(P1 \
{0, µN, ∞}) (in the sense of [Deligne 1989, Section 12]), and whose crystalline Frobenius structure is φ.
Their power series expansion at 0 is the following, which relates them to cyclotomic multiple harmonic
sums:
Li[(ni)d; (ξi)d](z) =
X
0<m1<···<md
  ξ2
ξ1
m1 · · ·
  z
ξd
md
mn1
1 · · · mnd
d
.
(1-18)
We proved in [Jarossay 2015, (0.3.7)] that prime weighted multiple harmonic sums are expressed in
the following way (where f 7→f (ξ) is the natural map 51,0(K) →5ξ,0(K)):
harpα((ni)d; (ξi)d+1) = (−1)d
∞
X
l=0
X
ξ
ξ −pα Ad8(ξ)
p,α(eξ)[el
0eξd+1end−1
0
eξd · · · en1−1
0
eξ1].
(1-19)
1722
David Jarossay
We have a total of three ways to deal with prime weighted multiple harmonic sums, which makes three
frameworks for computations:
(i) Via their expression in terms of p-adic cyclotomic multiple zeta values (1-19).
(ii) Via their expression as coefﬁcients of power series expansions of multiple polylogarithms (1-18).
(iii) Via their deﬁnition as elementary explicit iterated sums (0-2).
We will symbolize these three frameworks by, respectively, the notations
R
1,0,
R
and 6.
In [Jarossay 2015] we have expressed the “harmonic Frobenius” in the frameworks
R
and 6 and we
have compared the two expressions. Here we are going to express the “iteration of the harmonic Frobenius”
in the frameworks
R
1,0 and 6 and compare the two expressions. Keeping in mind the distinction between
these three frameworks
R
1,0,
R
and 6 will be essential in this paper and in subsequent ones. We note that
the frameworks 6 and
R
make sense for all weighted cyclotomic multiple harmonic sums whereas the
framework
R
1,0 makes sense only for the prime weighted cyclotomic multiple harmonic sums and follows
from a theorem.
1C2. The generalization to negative numbers of iterations of the Frobenius. The indices of p-adic
cyclotomic multiple zeta values, of the form ((ni)d; (ξi)d), are distinct from the indices of cyclotomic
weighted multiple harmonic sums (0-2), of the form ((ni)d; (ξi)d+1).
Deﬁnition 1C.1. A harmonic word over e0∪µN , is a tuple ((ni)d; (ξi)d+1), with d ∈N∗(ni)d ∈(N∗)d,
(ξi)d+1 ∈µN(K)d+1.
We sometimes identify it with eξd+1end−1
0
eξd · · · en1−1
0
eξ1.
Let us denote by
Wdhar(e0∪µN ) the set of harmonic words over e0∪µN .
We now deﬁne, using (1-19), an analogue of multiple harmonic sums associated with negative numbers
of iterations of the Frobenius, and another analogue associated with the ﬁxed point of the Frobenius. The
notation “har” that we are going to use is justiﬁed by [Jarossay 2014; 2016a; 2016b] and the notion of
“cyclotomic multiple harmonic values”. Below, f [1/(1 −e0) · w] = P∞
l=0 f [el
0w].
Deﬁnition 1C.2. For any w = eξd+1end−1
0
eξd · · · en1−1
0
eξ1 = ((ni)d; (ξi)d+1) we call generalized prime
weighted multiple harmonic sums the following numbers:
(i) For any α ∈N∗, let
harp,α(w) = harpα(w)
and
harp,−α(w) = (−1)d X
ξ
ξ −pα Ad8(ξ)
p,−α(eξ)

1
1 −e0
· w

.
(ii) For ϵ ∈{±1}, let
harq,ϵ∞(w) = (−1)d X
ξ
ξ −1 Ad8(ξ)
q,ϵ∞(eξ)

1
1 −e0
· w

.
(iii) If pα = q ˜α, with ˜α ∈Z, we denote by harq,˜α = harp,α.
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1723
1C3. The noncommutative generating series. We now deﬁne generating series of prime weighted cyclo-
tomic multiple harmonic sums, the numbers (0-2) with m = pα.
We have deﬁned in [Jarossay 2015] two variants of K⟨⟨e0∪µN ⟩⟩∫adapted to multiple harmonic sums:
K⟨⟨e0∪µN ⟩⟩∫
har ⊂K⟨⟨e0∪µN ⟩⟩the vector subspace of the elements f such that, for all words w on e0∪µN , the
sequence ( f [el
0w])l∈N is constant and f [w′e0] = 0 for all words w′; and K⟨⟨e0∪µN ⟩⟩6
har = K Wdhar(e0∪µN ).
Here is the third variant:
Deﬁnition 1C.3.
(i) Let
K⟨⟨e0∪µN ⟩⟩
∫1,0
har = { f ∈K⟨⟨e0∪µN ⟩⟩| ∀l > 0, ∀r > 0, ∀w word on e0∪µN , f [el
0wer
0] = 0}.
(ii) Let
K⟨⟨e0∪µN ⟩⟩
∫1,0
har,0 = { f ∈K⟨⟨e0∪µN ⟩⟩
∫1,0
har | ∀d ∈N∗, ni ∈N∗(1 ⩽i ⩽d), ξi ∈µN(K)(1 ⩽i ⩽d + 1),
f [eξξd+1end−1
0
eξξd · · · en1−1
0
eξξ1] = ξ −1 f [eξd+1end−1
0
eξξd · · · en1−1
0
eξ1]}.
The map f 7→P
w∈Wdhar(e0∪µN ) f [w]1/(1 −e0) · w clearly deﬁnes an isomorphism
K⟨⟨e0∪µN ⟩⟩
∫1,0
har
∼
−→K⟨⟨e0∪µN ⟩⟩∫
har
of topological K-vector spaces, with topology deﬁned by ND. However, we denote K⟨⟨e0∪µN ⟩⟩
∫1,0
har and
K⟨⟨e0∪µN ⟩⟩∫
har differently in order to keep in mind the important distinction between the frameworks
R
1,0,
R
, 6.
Let us deﬁne the noncommutative generating series of the generalized prime weighted cyclotomic
multiple harmonic sums.
Deﬁnition 1C.4. For any ˜α ∈Z ∪{±∞} \ {0}, let harq,˜α = P
w∈Wdhar(e0∪µN ) harq,˜α(w)w ∈K⟨⟨e0∪µN ⟩⟩
∫1,0
har .
We note that, for ˜α ∈N∗, we have harq,˜α ∈K⟨⟨e0∪µN ⟩⟩
∫1,0
har,0, because we have, for all ξ ∈µN(K),
ξ −q ˜α = ξ −q = ξ −1.
1D. The pro-unipotent harmonic actions and the harmonic Frobenius. We review deﬁnitions from
[Jarossay 2015] of the pro-unipotent harmonic actions ◦∫
har and ◦6
har, and the harmonic Frobeniuses
(τ(pα)φα)∫
har and (τ(pα)φα)6
har.
Let Ad ˜51,0(K)(e1)o(1) = Ad ˜51,0(K)(e1) ∩K⟨⟨e0∪µN ⟩⟩o(1); by [Jarossay 2015, Proposition 1.3.5], it is a
subgroup of Ad ˜51,0(K)(e1) for the usual group structure of Spec(OX,e0∪µN ), and for the adjoint Ihara
product ◦
∫1,0
Ad ; it is a complete topological group with the topology deﬁned by ND, for both group structures.
1D1. In the framework of integrals. We review deﬁnitions from [Jarossay 2015] which will be useful in
what follows.
Let K⟨⟨e0∪µN ⟩⟩lim ⊂K⟨⟨e0∪µN ⟩⟩be the vector subspace consisting of the elements f ∈K⟨⟨e0∪µN ⟩⟩such
that, for all words w on e0∪µN , the sequence ( f [el
0w])l∈N has a limit in K, and f [w′e0] = 0 for all
words w′. Let the map lim : K⟨⟨e0∪µN ⟩⟩lim →K⟨⟨e0∪µN ⟩⟩∫
har be deﬁned by, for all words w over e0∪µN ,
1724
David Jarossay
(lim f )[w] = liml→∞f [el
0w]. The p-adic pro-unipotent harmonic action of integrals [Jarossay 2015,
Deﬁnition 2.2.2] is the map ◦∫
har : Ad ˜51,0(K)o(1)(e1) × (K⟨⟨e0∪µN ⟩⟩∫
har)N →(K⟨⟨e0∪µN ⟩⟩∫
har)N deﬁned by
(g, (hm)m∈N) 7→g ◦∫
har (hm)m∈N = (lim(hm(e0, (τ(m)(g(ξ))ξ)))m∈N)
The harmonic Frobenius of integrals [Jarossay 2015, Deﬁnition 2.3.5] is the map (τ(pα)φα)∫
har :
(K⟨⟨e0∪µN ⟩⟩∫
har)N →(K⟨⟨e0∪µN ⟩⟩∫
har)N deﬁned by
f 7→8−1
p,αe18p,α ◦∫
har σ α( f ).
1D2. In the framework of series. The p-adic pro-unipotent harmonic action of series [Jarossay 2015,
Proposition–Deﬁnition 4.3.1] is a counterpart of ◦∫
har found in terms of series. It is a map
◦6
har : K⟨⟨e0∪µN ⟩⟩6
har,o(1) × (K⟨⟨e0∪µN ⟩⟩6
har)N →(K⟨⟨e0∪µN ⟩⟩6
har)N
where K⟨⟨e0∪µN ⟩⟩6
har,o(1) is deﬁned in [Jarossay 2015, Deﬁnition 4.1.3].
The harmonic Frobenius of series is
f 7→harpα ◦6
harσ α( f ).
We proved in [Jarossay 2015] that the harmonic Frobenius of integrals and the harmonic Frobenius of
series are equal [loc. cit., (0.3.3) and (0.3.5)]. Thus, we see that the harmonic Frobenius is characterized by
8−1
p,αe18p,α or, equivalently, by harpα. This is why studying harpα is equivalent to studying the harmonic
Frobenius and, in the next sections, we will see harpα as a function of α, which amounts to studying the
harmonic Frobenius as a function of α.
Remark 1D.1. We can deﬁne natural analogues of all the structures which are at base-points (1, 0) and
which are mentioned in this Section 1, at base-points (0, ξ) for any ξ ∈µN(K), which are compatible
with the morphism (x 7→ξx)∗. All the results of this Section 1 have natural analogues at base-points
(0, ξ) for any ξ ∈µN(K). This will be used implicitly in the proofs of the next section.
