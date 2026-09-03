---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-003-22-nets-of-c-algebras
section_title: "Nets of C*-algebras."
section_number: 2.2
pages: 7-9
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
A net 3 of C*-algebras over ∆ is given by a family A = {Aa}a∈∆ of unital C*-algebras, and unital
*-monomorphisms (called the net structure )
a′a :Aa →Aa′ : a′′a′ ◦a′a =a′′a , ∀a ⊆a′ ⊆a′′ .
We shall use the notation A = (A, )∆ . Morphisms ν : A → A′ of nets of C*-algebras are deﬁned
by families of *-morphisms
νa :Aa →A′
a : νa′ ◦a′a =′
a′a ◦νa , ∀a ⊆a′ .
In algebraic quantum ﬁeld theory it is customary to consider nets su ch that there is a Hilbert space
H with Aa ⊆BH for any a ∈ ∆, and any a′a , a ⊆a′ , is the inclusion map. In this case we write
A = (A, )∆ ⊂BH .
Net bundles ([33, 34, 37]). When every a′a is an isomorphism we say that A is a C*-net
bundle ; picking a family ν of *-isomorphisms νa :Aa →A∗ , ∀a ∈ ∆, and deﬁning
′
a′a ∈ autA∗ ,  ′
a′a :=νa′ ◦a′a ◦ν−1
a , ∀a ⊆a′ ,
we obtain a C*-net bundle A′ = (A′, ′)∆ with constant ﬁbre A′
a ≡A∗ and isomorphic to A . We
call ν a choice of the standard ﬁbre of A , and denote the set of C*-net bundles with ﬁbre isomorphic
to A∗ by
bun(∆ ,A ∗) .
To be concise we write aa′ := −1
a′a , ∀a ⊆ a′ . For any b ∈ Σ 1(∆) we deﬁne b := ∂0b |b| ◦|b|∂1b ,
and, assuming that a choice of the standard ﬁbre A∗ has been made,
χp :=bn ◦... ◦b1 ∈ autA∗ , ∀p =bn ∗... ∗b1 :a →a . (2.7)
The map χp , p : a → a, factorizes through homotopy, so it yields the C*-dynamical system
χ :π1(∆) → autA∗ . Indeed, assigning the holonomy
A ↦→χ (2.8)
deﬁnes an equivalence from the category of C*-net bundles to the one of π1(∆)-dynamical C*-
systems.
3Here we should use the term precosheaf, nevertheless we prefer to maintain the traditional termin ology.
7
Analogous deﬁnitions, notations and properties hold in the cases of group net bundles and Hilbert
net bundles. In the ﬁrst case we have group isomorphisms ıa′a :Ga →Ga′ , ∀a ⊆ a′ , deﬁning the
group net bundle G = (G,ı )∆ , whilst in the second case we have unitaries Ua′a : Ha → Ha′ ,
∀a ⊆a′ , deﬁning the Hilbert net bundle H = (H,U )∆ . We have the composition of equivalences
P
(2.8 )
− → χ
(2.4 )
− → Pχ , (2.9)
assigning to any net bundle P the locally constant bundle Pχ , which holds when the ﬁbres are
C*-algebras, Hilbert spaces and topological groups. The geometric c ontent of (2.9) is that χ is the
holonomy of P or, equivalently, the monodromy of Pχ , whilst P can be understood as a precosheaf
of local sections of Pχ .
Representations ([9, 37]). Let A = (A, )∆ be a net of C*-algebras. A representation of A is
a pair ( π,U ), where H = {Ha}a∈∆ is a family of Hilbert spaces, U = {Ua′a :Ha →Ha′}a⊆a′ is a
family of unitary operators and πa :Aa →BHa , a ∈ ∆, is a family of Hilbert space representations
such that
Ua′′a =Ua′′a′Ua′a , adUa′a ◦πa =πa′ ◦a′a , a ⊆a′ ⊆a′′ .
Deﬁning the Hilbert net bundle H = (H,U )∆ we obtain the C*-net bundle BH = (BH, adU )∆ and
(π,U ) can be regarded as a morphism π : A → BH. When H is trivial 4 we have Hilbert space
representations, that are those commonly used in algebraic quant um ﬁeld theory.
Commutators on Hilbert net bundles. We give a notion of commutator for operators on
Hilbert net bundles, designed to be coherent with the underlying net structure and not depending,
like the one used in [9, Eq.3.6], on the choice of the standard ﬁbre. We s hall use this notion to
propose a reﬁned notion of causality for nets in generic spacetimes (see §4).
Let H = (H,U )∆ be a Hilbert net bundle. We say that H is trivial on Ω ⊆ ∆ whenever the
restriction HΩ := (H,U )Ω is a trivial Hilbert net bundle. Given a,o ∈ ∆, we say that a path
p :o →a, p =bn ∗... ∗b1 , is trivialized by H whenever there is Ω ⊆ ∆ such that: (1) H is trivial
on Ω ; (2) bi ∈ Σ 1(Ω), ∀i = 1,...,n . We denote the set of paths trivialized by H by π0(∆ , H).
Given a,o ∈ ∆ and T ∈BHa , T ′ ∈BHo , we write [ T,T ′]net
± = 0 whenever
[T,T ′]p
± := T ·UpT ′U ∗
p ±UpT ′U ∗
p ·T = 0 , ∀p :o →a , p∈π0(∆ , H) , (2.10)
where Up :=Ubn · · ·Ub1 , p =bn ∗... ∗b1 (recall that we set Ub :=U∂0b|b|U|b|∂1b , ∀b ∈ Σ 1(∆)). Note
that the previous expression makes sense since UpT ′U ∗
p ∈ BHa . Moreover (2.10) is symmetric in
the sense that [ T,T ′]p
± = 0 if, and only if,
p[T,T ′]± := UpTU ∗
p ·T ′ ±T ′ ·UpTU ∗
p = 0 ,
where p ∈π0(∆ , H), p :a →o, is the opposite path. Note that:
• the fact that p is trivialized by H means that there is a Hilbert space H ′ with unitaries
Ve :He →H ′ , e ∈ Ω , such that Ue′e =V ∗
e′Ve , ∀e ⊆e′ ∈ Ω . So we have
Up = V ∗
aV|bn| · · ·V ∗
|b1|Vo = V ∗
aVo ,
and Up is independent of the choice of the path p with 1-simplices in Σ 1(Ω). When a =o we
have Up = 1 for any p ∈π0(∆ , H), p :a →a; thus [ T,T ′]net
± is the usual (anti)commutator
of BHa .
4That is, H is isomorphic to the constant Hilbert net bundle H0 = (H 0,U 0)∆ , H 0
a ≡H∗ , U 0
a′a ≡ 1H∗ .
8
• if H is trivial then any path is trivialized by H. In particular, when H is the constant Hilbert
net bundle, Up ≡ 1 and we have the usual (anti)commutator;
• if Ω ⊆ ∆ is such that π1(Ω) = 0 and p is made of 1-simplices in Σ 1(Ω), then p is automatically
trivialized by H; for example, we may take Ω directed. Note that restrictions to sim ply
connected subsets of ∆ appear in [9, §3.2] to deﬁne sharp excitations of the vacuum state.
Gauge actions ([39]). Let A = (A, )∆ be a net of C*-algebras and G = (G,ı )∆ a group net
bundle (we assume that the ﬁbres of G are locally compact and Hausdorﬀ). A gauge action of G
on A is given by a family of strongly continuous actions αo :Go → autAo , ∀o ∈ ∆, such that
{αo′(ıo′o(g))} ◦o′o =o′o ◦αo(g) , ∀g ∈Go , o ⊆o′ . (2.11)
When G is the constant net bundle (that is, any ıo′o is the identity of a ﬁxed group G∗ ), we
have a group action of G∗ on A by net automorphisms. A morphism ν : A → A′ is said to be
G-equivariant whenever
νa ◦αa(g) = α′
a(g) ◦νa , ∀a ∈ ∆ , g ∈Ga .
The notion of gauge action can be deﬁned for a Hilbert net bundle H = (H,U )∆ as above, requiring
that each αo(g), o ∈ ∆, g ∈ Go , is a unitary operator on Ho . The category of G-equivariant
Hilbert net bundles over ∆, that we denote by
HilbG(∆) ,
is a symmetric tensor C*-category (see §2.3 for an explanation of these terms); it has a simple unit
in the cases of interest, that is, when ∆ is path-connected or, equ ivalently, when M is arcwise
connected (see [34, §5]).
