---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-002-1-preliminaries
section_title: "Preliminaries"
section_number: 1
pages: 4-6
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
---
Here we recall the deﬁnitions and notations of our most impor tant objects of
study. Several things described in this section can be found in more detail elsewhere
in the literature, see in particular [Lus1, Opd1, OpSo1, Sol 3].
1.1. Aﬃne Hecke algebras. Let a be a ﬁnite dimensional real vector space and
let a∗ be its dual. Let Y ⊂ a be a lattice and X = Hom Z(Y, Z) ⊂ a∗ the dual lattice.
Let
R = (X,R 0,Y,R ∨
0,F 0).
be a based root datum. Thus R0 is a reduced root system in X, R∨
0 ⊂ Y is the
dual root system, F0 is a basis of R0 and the set of positive roots is denoted R+
0 .
Furthermore we are given a bijection R0 →R∨
0, α↦→α∨ such that ⟨α, α∨⟩ = 2 and
such that the corresponding reﬂections sα :X →X (resp. s∨
α :Y →Y ) stabilize R0
(resp. R∨
0 ). We do not assume that R0 spans a∗.
The reﬂections sα generate the Weyl group W0 =W (R0) of R0, and S0 := {sα :
α ∈ F0} is the collection of simple reﬂections. We have the aﬃne Weyl group
W aﬀ = ZR0 ⋊W0 and the extended (aﬃne) Weyl group W e =X ⋊W0. Both can
be regarded as groups of aﬃne transformations of a∗. We denote the translation
corresponding to x ∈X bytx.
As is well known, W aﬀ is a Coxeter group, and the basis of R0 gives rise to a
set Saﬀ of simple (aﬃne) reﬂections. The length function ℓ of the Coxeter system
A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS 5
(W aﬀ,S aﬀ ) extends naturally to W e. We write
X + := {x ∈X : ⟨x, α∨⟩ ≥ 0 ∀α ∈F0},
X − := {x ∈X : ⟨x, α∨⟩ ≤ 0 ∀α ∈F0} = −X +.
It is easily seen that the center of W e is the lattice
Z(W e) = X + ∩X −.
We say that R is semisimple if Z(W e) = 0 or equivalently if R0 spans a∗. Thus a
root datum is semisimple if and only if the corresponding red uctive algebraic group
is so.
With R we also associate some other root systems. There is the non-r educed root
system
Rnr :=R0 ∪ {2α :α∨ ∈ 2Y }.
Obviously we put (2 α)∨ = α∨/2. Let R1 be the reduced root system of long roots
in Rnr:
R1 := {α ∈Rnr :α∨ ⁄∈2Y }.
Consider a positive parameter function for R, that is, a function q :W e → R>0 such
that
(5) q(ω) = 1 if ℓ(ω) = 0,
q(wv) = q(w)q(v) if w,v ∈W e and ℓ(wv) = ℓ(w) +ℓ(v).
Alternatively it can be given by W0-invariant mapq :R∨
nr → R>0, the relation being
(6)
qα∨ =q(sα) = q(tαsα) if α ∈R0 ∩R1,
qα∨ =q(tαsα) if α ∈R0 \R1,
qα∨/2 =q(sα)q(tαsα)−1 if α ∈R0 \R1.
The aﬃne Hecke algebra H = H(R,q ) is the unique associative complex algebra
with basis {Nw :w ∈W e} and multiplication rules
(7) NwNv =Nwv if ℓ(wv) = ℓ(w) +ℓ(v),(
Ns −q(s)1/2)(
Ns +q(s)−1/2)
= 0 if s ∈Saﬀ.
In the literature one also ﬁnds this algebra deﬁned in terms o f the elementsq(s)1/2Ns,
in which case the multiplication can be described without sq uare roots. The algebra
H is endowed with a conjugate-linear involution, deﬁned on ba sis elements by N ∗
w :=
Nw−1.
Forx ∈ X + we put θx := Ntx . The corresponding semigroup morphism X + →
H(R,q )× extends to a group homomorphism
X → H(R,q )× :x ↦→θx.
A part of the Bernstein presentation [Lus1, §3] says that the subalgebra A :=
span{θx : x ∈ X} is isomorphic to C[X], and that the center Z(H) corresponds
to C[X]W0 under this isomorphism. Let T be the complex algebraic torus
T = Hom Z(X, C×) ∼=Y ⊗Z C×,
so A ∼= O(T ) and Z(H) = AW0 ∼= O(T/W 0). This torus admits a polar decomposi-
tion
T =Trs ×Tun = Hom Z(X, R>0) × HomZ(X,S 1)
into a real split (or positive) part and a unitary part.
6 ERIC OPDAM AND MAARTEN SOLLEVELD
Let Mod f (H) be the category of ﬁnite dimensional H-modules, and Mod f,W0t(H)
the full subcategory of modules that admit the Z(H)-characterW0t ∈T/W 0. We let
G(H) be the Grothendieck group of Mod f (H) and we write GC(H) = C ⊗ZG(H).
Furthermore we denote by Irr( H), respectively Irr W0t(H), the set of equivalence
classes of irreducible objects in Mod f (H), respectively Mod f,W0t(H). We will use
these notations also for other algebras and groups.
