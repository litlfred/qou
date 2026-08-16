---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of aﬃne Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen"
section_id: sec-001-1-preliminaries
section_title: "Preliminaries"
section_number: 1
pages: 5-7
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
doc_brief: "Hochschild homology of affine Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen — Let H = H(R,q ) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not"
---
1.1 Aﬃne Hecke algebras
Let a be a ﬁnite dimensional real vector space and let a∗ be its dual. Let Y ⊂ a be
a lattice and X = Hom Z(Y, Z) ⊂ a∗ the dual lattice. Let
R = (X,R,Y,R ∨, ∆) .
be a based root datum. Thus R is a reduced root system in X, R∨ ⊂ Y is the
dual root system and ∆ is a basis of R. Furthermore we are given a bijection
R →R∨,α ↦→α∨ such that ⟨α, α∨⟩ = 2 and such that the corresponding reﬂections
sα :X →X (resp. s∨
α :Y →Y ) stabilize R (resp. R∨). We do not assume that R
spans a∗.
The reﬂections sα generate the Weyl group W = W (R) of R, and S∆ := {sα |
α ∈ ∆ } is the collection of simple reﬂections. We have the aﬃne Weyl group
W aﬀ = ZR ⋊W and the extended (aﬃne) Weyl group W e = X ⋊W . Both can
be considered as groups of aﬃne transformations of a∗. We denote the translation
corresponding to x ∈X by tx. As is well known, W aﬀ is a Coxeter group, and the
basis of R gives rise to a set Saﬀ of simple (aﬃne) reﬂections. More explicitly, let
∆∨
M be the set of maximal elements of R∨, with respect to the dominance ordering
coming from ∆. Then
Saﬀ =S∆ ∪ {tαsα |α∨ ∈ ∆∨
M }.
We write
X + := {x ∈X | ⟨x, α∨⟩ ≥ 0 ∀α ∈ ∆ },
X− := {x ∈X | ⟨x, α∨⟩ ≤ 0 ∀α ∈ ∆ } = −X +.
It is easily seen that the centre of W e is the lattice
Z(W e) = X + ∩X−.
The length function ℓ of the Coxeter system ( W aﬀ,S aﬀ ) extends naturally to W e.
The elements of length zero form a subgroup Ω ⊂W e andW e =W aﬀ ⋊ Ω. With R
we also associate some other root systems. There is the non-r educed root system
Rnr :=R ∪ {2α |α∨ ∈ 2Y }.
5
Obviously we put (2 α)∨ = α∨/2. Let Rl be the reduced root system of long roots
in Rnr:
Rl := {α ∈Rnr |α∨ ⁄∈2Y }.
We introduce a complex parameter function for R in two equivalent ways. Firstly,
it is a map q : Saﬀ → C× such that q(s) = q(s′) if s and s′ are conjugate in
W e. This extends naturally to a map q : W e → C× which is 1 on Ω and satisﬁes
q(ww′) = q(w)q(w′) if ℓ(ww′) = ℓ(w) +ℓ(w′). Secondly, a parameter function is a
W -invariant map q : R∨
nr → C×. The relation between the two deﬁnitions is given
by
qα∨ =q(sα) = q(tαsα) if α ∈R ∩Rl,
qα∨ =q(tαsα) if α ∈R \Rl,
qα∨/2 =q(sα)q(tαsα)−1 if α ∈R \Rl.
(1)
We speak of equal parameters if q(s) = q(s′) ∀s,s′ ∈Saﬀ and of positive parameters
if q(s) ∈ R>0 ∀s ∈Saﬀ .
We ﬁx a square root q1/2 :Saﬀ → C×. The aﬃne Hecke algebra H = H(R,q ) is
the unique associative complex algebra with basis {Nw |w ∈W } and multiplication
rules
NwNv =Nwv if ℓ(wv) = ℓ(w) +ℓ(v),(
Ns −q(s)1/2)(
Ns +q(s)−1/2)
= 0 if s ∈Saﬀ. (2)
In the literature one also ﬁnds this algebra deﬁned in terms o f the elementsq(s)1/2Ns,
in which case the multiplication can be described without sq uare roots. This explains
whyq1/2 does not appear in the notation H(R,q ).
Notice that Nw ↦→Nw−1 extends to a C-linear anti-automorphism of H, so H
is isomorphic to its opposite algebra. The span of the Nw with w ∈ W is a ﬁnite
dimensional Iwahori–Hecke algebra, which we denote by H(W,q ).
Now we describe the Bernstein presentation of H. For x ∈ X + we put θx :=
Ntx . The corresponding semigroup morphism X + → H (R,q )× extends to a group
homomorphism
X → H(R,q )× :x ↦→θx.
Theorem 1.1. (Bernstein presentation)
(a) The sets {Nwθx |w ∈W,x ∈X} and {θxNw |w ∈W,x ∈X} are bases of H.
(b) The subalgebra A := span{θx |x ∈X} is isomorphic to C[X].
(c) The centre of Z(H(R,q )) of H(R,q ) is AW , where we deﬁne the action of W
on A by w(θx) = θwx.
(d) Forf ∈ A and α ∈ ∆
fN sα −Nsαsα(f ) = q(sα)−1/2(
f −sα(f )
)
(q(sα)cα − 1).
Here the c-functions are deﬁned as
cα =



θα +q(sα)−1/2q(tαsα)1/2
θα + 1
θα −q(sα)−1/2q(tαsα)−1/2
θα − 1 α ∈R \Rl
(θα −q(sα)−1)(θα − 1)−1 α ∈R ∩Rl.
6
Proof. These results are due to Bernstein, see [Lus2, §3]. ✷
Consider the complex algebraic torus
T = Hom Z(X, C×) ∼
=Y ⊗Z C×,
so A ∼
= O(T ) and Z(H) = AW ∼
= O(T/W ). From Theorem 1.1 we see that H is of
ﬁnite rank over its centre. Let t = Lie(T ) and t∗ be the complexiﬁcations of a and
a∗. The direct sum t = a ⊕ia corresponds to the polar decomposition
T =Trs ×Tun = Hom Z(X, R>0) × HomZ(X,S 1)
of T into a real split (or positive) part and a unitary part. The ex ponential map
exp : t →T is bijective on the real parts, and we denote its inverse by lo g : Trs → a.
An automorphism of the Dynkin diagram of the based root syste m (R, ∆) is a
bijection γ : ∆ → ∆ such that
⟨γ(α), γ(β)∨⟩ = ⟨α, β∨⟩ ∀ α,β ∈ ∆ . (3)
Such a γ naturally induces automorphisms of R,R∨,W and W aﬀ . It is easy to
classify all diagram automorphisms of ( R, ∆): they permute the irreducible compo-
nents of R of a given type, and the diagram automorphisms of a connected Dynkin
diagram can be seen immediately.
We will assume that the action of γ on W aﬀ has been extended in some way to
W e, and then we call it a diagram automorphism of R. For example, this is the
case if γ belongs to the Weyl group of some larger root system containe d in X. We
regard two diagram automorphisms as the same if and only if th eir actions on W e
coincide.
Let Γ be a ﬁnite group of diagram automorphisms of R and assume that qα∨ =
qγ(α∨) for all α ∈Rnr. Then Γ acts on H by algebra automorphisms ψγ that satisfy
ψγ(Nw) = Nγ(w) w ∈W,
ψγ(θx) = θγ(x) x ∈X. (4)
Hence one can form the crossed product algebra Γ ⋉ H = H ⋊ Γ, whose natural basis
is indexed by the group ( X ⋊W ) ⋊ Γ = X ⋊ (W ⋊ Γ). It follows easily from (4)
and Theorem 1.1.c that Z(H ⋊ Γ) = AW ⋊Γ . We say that the central character of an
(irreducible) H ⋊ Γ-representation is positive if it lies in T rs/(W ⋊ Γ).
