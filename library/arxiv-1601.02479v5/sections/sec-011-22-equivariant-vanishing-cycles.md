---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-011-22-equivariant-vanishing-cycles
section_title: "Equivariant vanishing cycles"
section_number: 2.2
pages: 20-25
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
full six functor and vanishing cycles functor formalism for equivaria nt monodromic
mixed Hodge modules via a theory of monodromic mixed Hodge modules o n stacks.
Instead we mimic the constructions of [4] and Totaro’s approximat ion [49] of the
Chow ring of classifying spaces by ﬁnite-dimensional algebraic appro ximations to
produce only the deﬁnitions and constructions we will need for the r est of this
paper.
We will want to be able to work with equivariant monodromic mixed Hodge
modules, in the following generality. We assume that we have a G-action on a
smooth algebraic variety X, for G an aﬃne algebraic group, and a regular function
f on the stack X/G, i.e. a G-invariant regular function on X. Furthermore we
assume that we are given a map of stacks p : X/G → Y , where Y is a locally ﬁnite
type scheme. We will also assume that G is special, i.e. all ´ etale locally trivial
principal G-bundles are Zariski locally trivial — see [23, Def.2.1] for a concise
discussion of this condition in this context, or [8] for the original ref erences. As
noted in [23], all such G are connected.
The element H
(
p∗φ mon
f IC X (Q)
)
will be an element of D≥(MMHM(Y )), the
derived category of bounded below complexes of monodromic mixed H odge modules
on Y .
We deﬁne H
(
p∗φ mon
f IC X (Q)
)
as follows. Let V1 ⊂ V2 ⊂ . . . be a chain of in-
clusions of G-representations, and let U1 ⊂ U2 ⊂ . . . be an ascending chain of sub-
varieties of the underlying vector spaces of V1, V2, . . ., considered as G-equivariant
COHAS AND QUANTUM ENVELOPING ALGEBRAS 21
algebraic varieties. We suppose that G acts scheme-theoretically freely on each Ui,
that each principal bundle quotient Ui → Ui/G exists in the category of schemes,
and that codim Vi (Vi \ Ui) → ∞ as i → ∞. The map X × Ui → X ×G Ui exists as
a principal bundle quotient in the category of schemes by [15, Prop.2 3]. We deﬁne
fi : X ×G Ui → C to be the induced map, and ιi : X ×G Ui → X ×G Ui+1 to be the
inclusion.
To ﬁx notation, we ﬁx an embedding G ⊂ GLt(C) for some t. We set
Vi := Hom(Ci, Ct),
and deﬁne Ui ⊂ Vi to be the subscheme of surjective maps; if i ≥ t then Ui does
indeed carry a free G-action via the GL t(C)-action on Ct. For each i, we deﬁne
Xi := X ×G Ui. We obtain an explicit sequence of maps
pi+1,∗φ mon
fi+1 QXi+1 → pi+1,∗ιi,∗φ mon
fi QXi = pi,∗φ mon
fi QXi
and so a sequence of mixed Hodge modules
Fi := pi,∗φ mon
fi QXi
and morphisms Fi′ → F i for i′ > i.
Proposition 2.16. Fix n ∈ N. Then for i ≫ 0 the map
(31) Λ : Hn(Y, Fi+1) → H n(Y, Fi)
in MMHM(Y ) is an isomorphism.
Proof. Since the functor forg mon
Y : MMHM( Y ) → Perv(Y ) of equation (28) is faith-
ful, it suﬃces to show that (31) induces an isomorphism at the level o f perverse
sheaves. So let Fi denote the complex of perverse sheaves pi,∗φ fi QXi. Say we can
prove the same proposition, but with the map Λ replaced by the map
Λ con : Hn
con(Y, Fi+1) → H n
con(Y, Fi)
of constructible sheaves on Y (here and below we use Hcon to denote constructible
cohomology sheaves). Then for suﬃciently large i,
cone(Fi+1 → F i) ∈ D ≥n+1
con (Y ) ⊂ pD≥n+1(Y )
and the original proposition follows.
Consider the space Ui,i+1 ⊂ Hom(Ci+1, Ct) of linear maps which are surjective
after precomposing with the map
π i,i+1 : Ci+1 → Ci+1
given by ( z1, . . . , zi+1) ↦→(z1, . . . , zi, 0). This subspace is open and dense for i ≥ t.
We denote by ji the inclusion
ji : Ui,i+1֒→Ui+1.
Note that G acts freely on Ui,i+1, and there is a G-equivariant aﬃne ﬁbration
τi,i+1 : Ui,i+1 → Ui
(τi,i+1g)(z) := g(z, 0).
Deﬁne Xi,i+1 := X ×G Ui,i+1, denote by fi,i+1 : Xi,i+1 → C the function induced
by f , and denote by
(32) ιi,i+1 : Xi,i+1 → Xi+1
the open embedding induced by ji. The projection τi,i+1 induces an aﬃne ﬁbration
ti,i+1 : Xi,i+1 → Xi
and we deﬁne the induced morphism
(33) pi,i+1 : Xi,i+1
ti,i +1
− − − →Xi
pi
− →Y.
22 BEN DA VISON AND SVEN MEINHARDT
We factorise Λ con as the composition
Hn
con(pi+1,∗φ fi+1 QXi+1)
a
− → Hn
con(pi+1,∗ιi,i+1,∗φ fi,i +1 QXi,i +1) → H n
con(pi,∗φ fi QXi)
where the second map is an isomorphism by homotopy invariance. So it is enough
to show that the map a is an isomorphism for suﬃciently large i.
Consider the function
f i+1 : X ×Ui+1 → C given by the composition X ×Ui+1
π
− →
X
f
− →C, and deﬁne f i,i+1 : X × Ui,i+1 → C similarly. Let ιi,i+1 : X × Ui,i+1 →
X × Ui+1 be the inclusion. Then
φ f i+1
QX×Ui+1
∼
=φ f QX ⊠ QUi+1
and
(
φ
f i+1
QX×Ui+1 → ιi,i+1,∗φ f i,i +1
QX×Ui,i +1
)
= idφ f QX ⊠(QUi+1 → ji,∗QUi,i +1).
For ﬁxed m, Hm
con(QUi+1 ) → H m
con(QUi,i +1) is an isomorphism for suﬃciently large
i, since the codimension of Ui+1 \ Ui,i+1 inside Ui+1 goes to inﬁnity as i goes to
inﬁnity. Since the external tensor product is exact, we deduce th at for ﬁxed m and
suﬃciently large i,
Hm
con(φ
f i+1
QX×Ui+1 → ιi,i+1,∗φ f i,i +1
QX×Ui,i +1)
is an isomorphism. On the other hand, taking a Zariski open subspac e C ⊂ Xi+1
such that the principal bundle C = C ×Xi+1 (X × Ui+1) → C is trivial, we have
that
Hcon(φ f i+1
QX×Ui+1 → ιi,i+1,∗φ f i,i +1
QX×Ui,i +1)|C
∼
=
Hcon(φ fi+1 QXi+1 → ιi,i+1,∗φ fi,i +1 QX×GUi,i +1 )) ⊠ idQG ,
and so using exactness of external tensor product again, we ded uce that for ﬁxed
n and suﬃciently large i, the map
Hn
con(φ fi+1 QXi+1 → ιi,i+1,∗φ fi,i +1 QXi,i +1 ))
is an isomorphism. The pushforward pi+1,∗ maps D≥n+1
con (Xi+1) → D ≥n+1
con (Y ), and
so
cone
(
pi+1,∗φ fi+1 QXi+1 → pi+1,∗ιi,i+1,∗φ fi,i +1 QXi,i +1
)
∈ D ≥n+1
con (X)
and the map a is an isomorphism for suﬃciently large i, as required. □
Proposition 2.17. The complex
(34) . . .
0
− →lim
i↦→∞
Hn−1(pi,∗φ mon
fi QXi )
0
− →lim
i↦→∞
Hn(pi,∗φ mon
fi QXi )
0
− →. . . .
is well deﬁned up to canonical isomorphism in D(MMHM(Y )).
Proof. The proposition says that if, for l = 1, 2 we have two choices V (l)
i , and U (l)
i
for the spaces Vi and Ui in the deﬁnition of Hn(pi,∗φ mon
fi QXi ), and we deﬁne X (l)
i ,
p(l)
i etc. with reference to them, then there is a canonical isomorphism , for each n,
and for suﬃciently large i:
Hn(p(1)
i,∗φ mon
f (1)
i
QX (1
i
) → H n(p(2)
i,∗φ mon
f (2)
i
QX (2)
i
).
By another application of [15, Prop.23], Xi × (U (1)
i × U (2)
i ) is a principal G-bundle
over X (12)
i := Xi ×Gi (U (1)
i × U (2)
i ). We denote by p(12)
i : X (12)
i → Y the projec-
tion; note that it factors through both p(1)
i and p(2)
i . Via the same argument as
COHAS AND QUANTUM ENVELOPING ALGEBRAS 23
Proposition 2.16, each of the morphisms
τ : Hn(p(1)
i,∗φ mon
f (1)
i
QX (1)
i
) → Hn(p(12)
i,∗ φ mon
f (12)
i
QX (12)
i
)
κ : Hn(p(2)
i,∗φ mon
f (2)
i
QX (2
i
) → Hn(p(12)
i,∗ φ mon
f (12)
i
QX (12)
i
)
is an isomorphism, and σ (12) = κ−1τ is the desired isomorphism. From the obvious
commutative diagrams of projections between diﬀerent principal G-bundles, there
are equalities σ (23)σ (12) =σ (13) andσ (11) = id. □
We denote by H
(
p∗φ mon
f QX
)
the element deﬁned in Proposition 2.17.
If M =∐
s∈S Ms, with Ms ∼
= Xs/Gs and each Xs a smooth algebraic variety,
and each Gs a special aﬃne algebraic group, and p : M → Y =∐
s∈S Ys is a map
to a locally ﬁnite type scheme respecting the decompositions of the s ource and the
target, for c ∈ Z we deﬁne
H
(
p∗φ mon
f
⨁
s∈S
QMs
)
:=
⨁
s∈S
H
(
p∗φ mon
f |Xs /G s
QXs/Gs
)
H
(
p∗φ mon
f
⨁
s∈S
Lc/2
Ms
)
:=
⨁
s∈S
H
(
p∗φ mon
f |Xs /G s
Lc/2
Xs/Gs
)
and
H
(
p∗φ mon
f
⨁
s∈S
IC Ms (Q)
)
:=
⨁
s∈S
H
(
p∗φ mon
f |Xs /G s
L(dim(Gs)−dim(Xs))/2
Xs/Gs
)
.
We deﬁne H
(
p!φ mon
f
⨁
s∈S QMs
)
∈ D (MMHM(Y )) in similar fashion. We give
the deﬁnition in the case that M = X/G, for X a smooth irreducible variety and G
a special aﬃne algebraic group, and extend to the case of a disjoint union of such
stacks as above.
Consider the isomorphism
H(ιi,i+1,!φ mon
fi,i +1 QXi,i +1 ) ∼
= H(φ mon
fi QXi) ⊗ Ldim(Xi+1)−dim(Xi)
where ιi,i+1 is as deﬁned in (32). Arguing as in Proposition 2.16, for ﬁxed n the
natural map
H2 dim(Ui+1)+n
con ((Xi,i+1 → Xi+1)!φ mon
fi,i +1 QXi,i +1 ) → H 2 dim(Ui+1)+n
con (φ mon
fi+1 QXi+1)
is an isomorphism for suﬃciently large i, and we can deﬁne Hn
(
p!φ mon
f QX/G
)
to
be the limit of Hn
(
pi,!φ mon
fi L− dim(Ui)
Xi
)
as i tends to inﬁnity, and we set
Hn
(
p!φ mon
f Lc
X/G
)
:=Lc ⊗ Hn(
p!φ mon
f QX/G
)
H
(
p!φ mon
f IC X/G(Q)
) := H
(
p!φ mon
f L(dim(G)−dim(X))/2
X/G
)
.
Remark 2.18. Note that we do not oﬀer here a deﬁnition of p∗φ mon,f QX/G, or
p!φ mon,f QX/G as objects of the derived category, but instead limit oursel ves to deﬁn-
ing the total cohomology of these direct images with respect to the natural t-structure
on D(MMHM(Y )). Of course in case X/G is an actual scheme, p∗φ mon
f QX/G and
p!φ mon
f QX/G are well deﬁned monodromic mixed Hodge modules before passi ng to
cohomology, and our deﬁnitions of H
(
p∗φ mon
f QX/G
)
and H
(
p!φ mon
f QX/G
)
re-
cover their respective total perverse cohomology.
24 BEN DA VISON AND SVEN MEINHARDT
Remark 2.19. As a special case of the above construction, if τ : → NQ0 is a stack
over a monoid of dimension vectors, with each Md ∼
= Xd/Gd, we deﬁne
H

M,
⨁
d∈NQ0
φ mon
f QMd

 :=
⨁
d∈NQ0
H
(
τ∗φ mon
f QXd/Gd
)
and H(M,⨁
dφ mon
f IC Md(Q)), Hc(M,⨁
dφ mon
f IC Md (Q)) etc. similarly. This is
the deﬁnition used in [30, Sec.7] in the deﬁnition of the underlying NQ0 -graded
monodromic mixed Hodge structure of the critical cohomolog ical Hall algebra.
Deﬁnition 2.20. Let X/G → NQ0 be as in Proposition 2.17, and let υ : X S/G →
X/G be an inclusion of stacks. We denote by
υi : X S ×G Ui → X ×G Ui
the induced map, and by pS
i the restriction of pi to X S ×G Ui. We deﬁne the
restricted absolute critical cohomology as the complex of l imits with zero diﬀerential
(35) H
(
X S/G,φ mon
f QX/G
) :=
⨁
n∈Z
lim
i↦→∞
Hn(
(Y → pt)∗pS
i,∗υ∗
iφ mon
fi QXi
)
[−n]
and likewise we deﬁne
Hc
(
X S/G,φ mon
f QX/G
) :=
⨁
n∈Z
lim
i↦→∞
Hn
(
(Y → pt)!pS
i,!υ∗
iφ mon
fi L− dim(Ui)
Xi
)
[−n].
Let h : X ′ → X be a morphism of G-equivariant varieties over the G-invariant
locally ﬁnite type scheme Y . Then for each i we obtain maps hi : X ′
i → Xi. There
are natural maps
δ1 : pi,∗φ mon
fi hi,∗QX ′
i → pi,∗hi,∗φ mon
fi◦hiQX ′
i
which are isomorphisms if h is proper or an aﬃne ﬁbration (see Proposition 2.13).
We precompose with the natural map
δ2 : pi,∗φ mon
fi QXi → pi,∗φ mon
fi hi,∗QX ′
i
and let i ↦→ ∞, deﬁning maps
H
(
p∗φ mon
f QX/G
)
→ H
(
(ph)∗φ mon
f ◦h QX ′/G
)
.
Now assume that X ′ and X are smooth, or that h is. Taking H(DY (δ1 ◦δ2)) and
letting i ↦→ ∞, we deﬁne the map
H
(
(ph)!φ mon
f ◦h QX ′/G
)
→ Ldim(X ′)−dim(X) ⊗ H
(
p!φ mon
f QX/G
)
.
Finally, let υ : H → G be an inclusion of groups — the only examples we will
consider are when υ is the inclusion of a parabolic subgroup inside GL n(C), or the
inclusion L ⊂ P of the Levi subgroup of a parabolic subgroup of GL n(C). Let G act
on X as above, with f a G-invariant regular function on X. Let h : X/H → X/G
be the associated morphism of stacks. Then we obtain maps
X ×H Ui
hi
− →X ×G Ui
(x, z) ↦→(x, z)
which we use in the same way as above to obtain the map
H
(
p∗φ mon
f QX/G
)
→ H
(
(ph)∗φ mon
f QX/H
)
and the map
H
(
(ph)!φ mon
f QX/H
)
→ H
(
p!φ mon
f Ldim(G)−dim(H)
X/G
)
.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 25
Remark 2.21. If֒→G is the inclusion of a parabolic subgroup, then the induced
maps hi are proper. As such, there is a natural isomorphism φ mon
fi hi,∗QX×H Ui
∼
=
hi,∗φ mon
fi QX×H Ui. From the maps hi,∗DX×H Ui QX×H Ui → DX×GUi QX×GUi given
by the natural isomorphism hi,∗ ∼
= hi,! and Verdier duality, we obtain, in the limit,
the map
H
(
(ph)∗φ mon
f QX/H
)
→ H
(
p∗φ mon
f Ldim(G)−dim(H)
X/G
)
.
