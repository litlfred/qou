---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-010-22-character-twists-and-convolution
section_title: "Character twists and convolution"
section_number: 2.2
pages: 34-38
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
In this section we show that twisting by a character χ deﬁnes a tensor
functor ACU in the sense of [86, chapt. I, sect. 4.2.4] on the symmetric
monoidal category Db
c (X,Λ) with respect to convolution. Recall that this
means that we have natural isomorphisms (K ∗L)χ ∼= Kχ ∗Lχ for all K,L
in Db
c (X,Λ), compatible with the associativity, commutativity and unity
constraints. This observation will be crucial for lemma 2.11 below, but
its proof is rather formal and may be skipped at a ﬁrst reading.
PROPOSITION 2.1. For any character χ, the auto-equivalence K 7→Kχ
of the category Db
c (X,Λ) deﬁnes a tensor functor ACU which is compatible
with degree shifts and perverse truncations.
Proof. The functor K 7→Kχ preserves semi-perversity, so it is t-exact
with respect to the perverse t-structure since D(Kχ) ∼= D(K)χ−1. It remains
to check tensor functoriality. Clearly 1χ ∼= 1.
Depending on the context, put R = Zl, R = Z or R = Z/nZ, including
the case where p = char(k) divides n. We claim that in all these cases
the group law a : X ×X −→X induces on the ﬁrst cohomology groups the
diagonal morphism
a∗: H1(X,R) −→H1(X ×X,R) = H1(X,R)⊕H1(X,R), x 7→(x,x).
For R = Zl or R = Z this follows from the formula preceding lemma 15.2
in [75]. For a ﬁnite coefﬁcient ring R = Z/nZ with p ∤n we have R ∼= µn
since the ground ﬁeld k is algebraically closed; then our claim follows from
the identiﬁcation H1(X,µn) ∼= Pic0(X)[n] in [74, cor. III.4.18], since for
coherent line bundles L ∈Pic0(X) one has a∗(L ) ∼= pr∗
1(L ) ⊗pr∗
2(L )
2.2. Character twists and convolution
27
by [75, prop. 9.2]. It remains to deal with R = Z/nZ when n = pr for some
integer r ∈N. In that case H1(X,Z/nZ) ∼= H1(X,Wr)F by [95, prop. 13],
and our claim then follows by taking Frobenius invariants and using the
isomorphism H1(X ×X,Wr) ∼= H1(X,Wr)⊕H1(X,Wr) of [98, p. 136].
Now, using [75, rem. 15.5] for R = Zl and [95, p. 50] for R = Z/nZ we
have in all cases a natural identiﬁcation
H1(X,R) = Hom(π1(X,0),R),
where in the ´etale setting homomorphisms are required to be continuous. If
we write the group structure on fundamental groups additively, it follows
that
a∗: π1(X,0)×π1(X,0) = π1(X ×X,0) −→π1(X,0)
is the addition morphism (x,y) 7→x + y. For ψ ∈Hom(π1(X,0),R) this
implies ψ(a∗(x,y)) = ψ(x + y) = ψ(x) + ψ(y), i.e. ψ ◦a∗= ψ ⊠ψ as an
additive character on π1(X,0)×π1(X,0) = π1(X ×X,0). For multiplicative
characters χ : π1(X,0) →Λ∗this implies
χ(a∗(x,y)) = χ(x+y) = χ(x)· χ(y),
i.e.
χ ◦a∗= χ ⊠χ.
Indeed, for Λ ⊆C one has Hom(π1(X,0),R) ⊗R C∗= Hom(π1(X,0),C∗)
taking R = Z. For Λ ⊆Ql any multiplicative character χ takes values in
E∗∼= Z ×F∗×U, where F is the residue ﬁeld of a ﬁnite extension ﬁeld E
of Ql and U is its group of 1-units. By continuity we have χ = χF · χU for
certain characters χF and χU with values in F∗resp. U. The character χU
can be handled as above, and the discussion for the character χF is covered
by the case R = Z/nZ with n = #F∗.
For the local system L = Lχ deﬁned by a character χ : π1(X,0) →Λ∗
this gives an isomorphism of local systems on X ×X
ϕ : a∗L
∼
−→L⊠L
which is uniquely determined up to multiplication by an scalar in Λ∗. In
what follows, we ﬁx a choice of ϕ once and for all. The choice of ϕ will
not matter for the commutativity of the diagrams below, as long as we use
the same ϕ consistently. However, we remark that the datum of a tensor
functor consists not only of the underlying functor but also comprises the
isomorphisms that describe the compatibility of the functor with the tensor
product. In this sense, different choices of ϕ will lead to different (though
of course isomorphic) tensor functors. For us, it will be most convenient
to ﬁx a trivialization λ : L0 ∼= Λ of the stalk L0 at the origin 0 of X, and to
require that the stalk morphism ϕ0 : a∗L(0,0) −→(L⊠L)(0,0) = L0 ⊗Λ L0 at
28
Chapter 2 – Proof of the vanishing theorem(s)
the origin (0,0) of X ×X makes the following diagramm commutative:
(a∗L)(0,0)
ϕ0
/ L0 ⊗Λ L0
λ⊗λ

L0
λ
/ Λ
Here L0 = e∗
X(L) = e∗
X×X(a∗(L)) = (a∗L)(0,0) since a◦eX×X = eX holds for
the unit sections
eX : {0} −→X
and
eX×X : {(0,0)} −→X ×X.
With the above normalization, the unique element v ∈L0 with λ(v) = 1 then
satisﬁes ϕ−1
0 (α ·v⊗β ·v) = αβ ·v for all α,β ∈Λ.
Let A,B ∈Db
c (X,Λ), and let p1, p2 : X ×X →X be the projections onto
the two factors. Using our ﬁxed choice of ϕ, we get an isomorphism
ψ : (A∗B)χ
∼
−→Aχ ∗Bχ
deﬁned by the commutative diagram
(A∗B)χ
ψ
/ Aχ ∗Bχ
(Ra∗(A⊠B))⊗L
Ra∗((A⊗L)⊠(B⊗L))
Ra∗((A⊠B)⊗a∗L)
Ra∗(id⊗ϕ)
/ Ra∗((A⊠B)⊗(L⊠L))
∼= Ra∗(id⊗S′⊗id)
O
where by S′ : p∗
2(B) ⊗p∗
1(L)
∼
−→p∗
1(L) ⊗p∗
2(B) we denote the symmetry
constraint of the usual tensor product on the derived category.
The isomorphisms ψ are compatible with the symmetry constraint S of
the symmetric monoidal category (Db
c (X,Λ),∗), i.e. for all A,B in Db
c (X,Λ)
the diagram
(A∗B)χ
Sχ

ψ
/ Aχ ∗Bχ
S

(B∗A)χ
ψ
/ Bχ ∗Aχ
is commutative. Indeed, unravelling the deﬁnition of S in [106] one sees that
the commutativity of the above diagram is equivalent to the commutativity
2.2. Character twists and convolution
29
of the diagram
a∗L
ϕ
/ L⊠L
p∗
1L⊗p∗
2L
σ∗a∗L
σ∗(ϕ) / σ∗(L⊠L)
p∗
2L⊗p∗
1L
S′
∼=
O
where σ : X × X →X × X is the morphism (x,y) 7→(y,x) and S′ is the
symmetry constraint of the ordinary tensor product. Since in any case our
diagram commutes up to a scalar in Λ∗, it sufﬁces to check commutativity
on the stalks at the origin (0,0). There everything boils down to the fact
that (λ ⊗λ)(u⊗v) = (λ ⊗λ)(v⊗u) for all u,v ∈L0.
Next we claim that the isomorphisms ψ are also compatible with the
associativity constraint of the symmetric monoidal category (Db
c (X,Λ),∗).
Indeed, by strictness [106, p. 11] the associativity constraints are the iden-
tity morphisms, so it sufﬁces to show that the diagram
((A∗B)∗C)χ
ψ
/ ((A∗B)χ)∗Cχ
ψ∗id
/ (Aχ ∗Bχ)∗Cχ
(A∗(B∗C))χ
ψ
/ Aχ ∗((B∗C)χ)
id∗ψ
/ Aχ ∗(Bχ ∗Cχ)
commutes for all A,B,C ∈Db
c (X,Λ). Writing
((A∗B)∗C)χ = Ra∗R(a×id)∗(((A⊠B)⊠C)⊗(a×id)∗a∗L)
and similarly for the other convolutions, the commutativity of the diagram
becomes equivalent to the commutativity of the diagram on X ×X ×X
(a×id)∗a∗L
(a×id)∗ϕ/ (a×id)∗L⊠L = a∗L⊠L
ϕ⊠id / (L⊠L)⊠L
(id ×a)∗a∗L
(id×a)∗ϕ/ (id ×a)∗L⊠L = L⊠a∗L
id⊠ϕ / L⊠(L⊠L)
Again it sufﬁces to check the commutativity on stalks at (0,0,0). The upper
arrow becomes the composition
(ϕ ⊗id)◦ϕ : L0 −→L0 ⊗Λ L0 −→(L0 ⊗Λ L0)⊗Λ L0.
The inverse morphism maps (α ·v⊗β ·v)⊗γ ·v to (αβ)γ ·v. By a similar
computation for the lower row, the commutativity of the diagram hence
boils down to the associativity law (αβ)γ = α(βγ) of the ﬁeld Λ.
□
As a trivial by-product, the tensor functoriality provides a simple proof
of the following result of [59].
30
Chapter 2 – Proof of the vanishing theorem(s)
COROLLARY 2.2. For K ∈Db
c (X,Λ) the Euler characteristic of Kχ does
not depend on the character χ.
Proof. In [106, lemma 8 on p. 28] it has been deduced from the K¨unneth
formula that hypercohomology deﬁnes a tensor functor ACU
H•(X,−) : (Db
c (X,Λ),∗) −→(Vects
Λ,⊗s)
where the right hand side denotes the rigid symmetric monoidal category
of super vector spaces over Λ, i.e. Z/2Z-graded vector spaces where the
symmetry constraint is twisted by the usual sign rule. Hence the Euler
characteristic of K is equal, as an element of EndDbc (X,Λ)(1) = Λ, to the
composite morphism
1
coevK / K ∗K∨
SK,K∨/ K∨∗K
evK
/ 1,
and as such it is invariant under character twists by proposition 2.1.
□
