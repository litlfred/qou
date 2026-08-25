---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-004-23-nets-and-presheaves-of-tensor-categories
section_title: "Nets and presheaves of tensor categories."
section_number: 2.3
pages: 9-14
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
In the present section we recall some properties of nets and pres heaves of tensor categories, that
constitute one of the main objects of study in the present paper. More detailed references on this
topic are [31, 39].
DR-categories. A C*-category is a category C whose spaces of arrows are Banach spaces endowed
with an antilinear involution ∗ : (ρ,σ ) → (σ,ρ ), ∀ρ,σ ∈ obj C , such that ( t ◦t′)∗ = t′∗ ◦t∗ ,
‖t∗ ◦t‖ = ‖t‖2 for any pair of composable arrows t,t ′ . Since the composition of arrows is assumed
to be linear, this implies that any ( ρ,ρ ), ρ ∈ obj C , is a C*-algebra.
We assume that functors between C*-categories preserve the involution structure. Following
the terminology of [28, §I.3], we say that a functor: is an embedding, whenever it is faithful on
the spaces of arrows; is full, whenever it is surjective on the spaces of arrows; is an isomorphism,
whenever it has an inverse functor and, in particular, an automorphism, whenever the initial and
target categories coincide.
A tensor product on C is given by a bilinear bifunctor ⊗ :C ×C →C , and the identity object
ι ∈ obj C is characterized by the property that ι ⊗ρ =ρ ⊗ι =ρ for any ρ ∈ obj C . To be concise,
in the sequel we shall write ρσ :=ρ ⊗σ , ∀ρ,σ ∈ obj C . We say that C has a simple unit whenever
(ι,ι ) = C1ι , where 1 ι is the identity arrow. We say that the tensor product is symmetric whenever
there is a family ǫρ,σ ∈ (ρσ,σρ ) of unitary arrows, inducing the ﬂip ( t ⊗t′) ◦ǫρ,ρ′ =ǫσ,σ′ ◦ (t′ ⊗t),
t ∈ (ρ,σ ), t′ ∈ (ρ′,σ ′), and fulﬁlling the properties in [16, §1]. In this case we write C⊗,ǫ .
9
The category of ﬁnite dimensional, unitary representations (that is, the dual ) of a compact group
is the basic class of examples for a symmetric tensor C*-category with simple unit. A symmetric
tensor C*-category with simple unit, conjugates, direct sums and subobjec ts in the sense of [16, §1]
is said to be a DR-category, and is automatically isomorphic to the dual of a compact group, uniq ue
up to isomorphism ([16, Theorem 6.9]).
Nets of tensor categories. A net of tensor C*-categories over ∆ is given by a family T =
{Ta}a∈∆ of tensor C*-categories and a family of tensor embeddings
a′a :Ta →Ta′ : a′′a′ ◦a′a =a′′a , ∀a ⊆a′ ⊆a′′ .
We shall use the notation T⊗ = (T, )∆ . We say that T⊗ is simple whenever every Ta , a ∈ ∆,
has a simple unit. When every a′a is an isomorphism we say that T⊗ is a net bundle of tensor
C*-categories. When every Ta , a ∈ ∆, has symmetry ξa and a′a(ξa;ρ,σ) = ξa′;a′ a(ρ),a′a(σ) for any
a ⊆a′ , ρ,σ ∈ obj Ta , we say that T⊗ is symmetric and write T⊗,ξ .
The next class of examples is motivated by the analysis of superselec tion structures in algebraic
quantum ﬁeld theory.
Example 2.1. (See [31, §27] and [22, §3.3]). Let A be a unital C*-algebra. Then the semigroup
endA of unital *-endomorphisms of A deﬁnes a tensor C*-category with sets of arrows
(ρ,σ ) := {t ∈A : tρ(v) = σ(v)t , ∀v ∈A} , ∀ρ,σ ∈ endA , (2.12)
whose composition is given by the product of A; the tensor product is given by
ρ ⊗σ :=ρσ :=ρ ◦σ , t ⊗t′ :=tρ(t′) , ∀ρ,σ,ρ ′,σ ′ ∈ endA , t∈ (ρ,σ ) , t′ ∈ (ρ′,σ ′) . (2.13)
Let now H be a Hilbert space and R = (R, )∆ ⊂BH a net of C*-algebras on H . For any a ∈ ∆
we consider the C*-algebra
Ra := C∗{Ro}o⊇a ⊆BH
(note that Ra ⊆ Ra ) and, given ρ,σ ∈ endRa , the space (ρ,σ ) ⊆ Ra of (2.12). We deﬁne the
categories
Ta :=
{ obj Ta := {ρ ∈ endRa :ρ(Ro) ⊆Ro, ∀o ⊃a} ,
arrTa := {(ρ,σ )a :=Ra ∩ (ρ,σ ) , ∀ρ,σ ∈ obj Ta} ,
having tensor product (2.13). We have
Ra ⊆Ra′ , Ra′
⊆Ra , ∀a ⊆a′ ,
and by deﬁnition any ρ ∈ obj Ta restricts to an endomorphism a′aρ ∈ obj Ta′ . Moreover we have
inclusions
a′a : (ρ,σ )a → (a′aρ,a′aσ)a′ , ρ,σ ∈ obj Ta ,
and this yields the net T = (T, )∆ . Finally, it is trivial to verify that  preserves the tensor
structure, so T⊗ is a tensor net. Note that the identity of Ta is the identity automorphism ιa ∈
endRa , so (ιa,ιa)a =Ra ∩ (Ra)′ .
10
Presheaves. There is a natural notion dual to the one of net: a presheaf of C*-categories is given
by a family of embeddings
raa′ :Ta′ →Ta : raa′ ◦ra′a′′ =raa′′ , ∀a ⊆a′ ⊆a′′ .
We shall write T = (T,r )∆ . A presheaf morphism η : T → T′ is a family of functors
ηa :Ta →T ′
a : ηa ◦raa′ =r′
aa′ ◦ηa′ , ∀a ⊆a′ .
Notation and terminology for presheaves are analogous to the one s of nets, so we say that T⊗ is
simple whenever every Ta , a ∈ ∆, is simple, and write T⊗,ξ to indicate presheaves endowed with a
symmetric tensor structure. In particular, we say that η is a symmetric tensor presheaf morphism
whenever the involved structures are preserved by η .
We say that T is full whenever every raa′ , a ⊆ a′ , is a full functor. In particular, a presheaf
bundle is a presheaf T = (T,r )∆ where any raa′ is an isomorphism. The map
T = (T, )∆ ↦→ T′ = (T,r )∆ , raa′ :=−1
a′a , ∀a ⊆a′ ,
yields an isomorphism from the category of net bundles to the one of presheaf bundles. Given a
symmetric tensor C*-category T⊗,ǫ , we denote the set of symmetric tensor presheaf bundles with
ﬁbre T⊗,ǫ by pbun↑(∆ ,T ⊗,ǫ). Reasoning as in (2.7), we obtain the one-to-one correspondenc e
pbun↑(∆ ,T ⊗,ǫ) ↔ hom(π1(∆) , autT⊗,ǫ) , T⊗,ξ ↦→χ ,
where autT⊗,ǫ is the group of symmetric tensor automorphisms of T⊗,ǫ . We call χ the holonomy
of T⊗,ξ .
Example 2.2. Let d ∈ N and πG : G → U(d) denote the deﬁning representation of a compact
Lie group G ⊆ U(d) . We denote the category of tensor powers of πG by ˆπG , which is a tensor
C*-category with symmetry θ . The group G deﬁnes a C*-algebra OG , the ﬁxed-point algebra of the
natural G-action on the Cuntz algebra Od ([15]). We deﬁne
QG := NG/G ,
where NG ⊆ U(d) is the normalizer of G. Since there are maps
QG → autˆπG;⊗,θ , QG → autOG
(see [38, §3]), by the previous considerations we obtain maps
hom(π1(∆) ,QG ) → pbun↑(∆ , ˆπG;⊗,θ) , hom(π1(∆) ,QG ) → bun(∆ , OG) . (2.14)
Sections. By deﬁnition, the category of sections of the symmetric tensor presheaf T⊗,ξ = (T,r )∆
has objects and, respectively, arrows
{
̺ = {̺a ∈ obj Ta}a∈∆ : raa′ (̺a′) = ̺a , ∀a ⊆a′ ,
t = {ta ∈ (̺a,ςa)}a∈∆ : raa′ (ta′) = ta , ∀a ⊆a′ .
We denote it by ~T⊗,ξ . It is easily veriﬁed that ~T⊗,ξ is a symmetric tensor C*-category, and we say
that T⊗,ξ is a DR-presheaf whenever ~T⊗,ξ is a DR-category.
11
Remark 2.1. Given the symmetric tensor presheaf T⊗,ξ = (T,r )∆ , for any a ∈ ∆ we denote the
full subcategory of Ta with objects ̺a , ̺ ∈ obj ~T⊗,ξ , by T ↓
a . Any raa′ , a ⊆ a′ , restricts to an
embeddingr↓ :T ↓
a′ →T ↓
a , ∀a ⊆a′ , and this yields the symmetric tensor presheaf T↓
⊗,ξ = (T ↓,r ↓)∆ .
By construction the section categories of T⊗,ξ , T↓
⊗,ξ coincide, that is ~T⊗,ξ = ~T↓
⊗,ξ .
To illustrate a Tannaka duality for categories of sections we give the notion of embedding, that
is, a symmetric tensor presheaf morphism
I : T⊗,ξ = (T,r )∆ → C⊗,ϑ = (C,r ′)∆ ,
such that: (1) C⊗,ϑ is a full presheaf; (2) any Ca , a ∈ ∆, is a full symmetric tensor subcategory of
the one of ﬁnite-dimensional Hilbert spaces; (3) any Ia , a ∈ ∆, is an embedding.
Theorem 2.2 (Tannaka duality, [39]). Let T⊗,ξ = (T,r )∆ be a simple, symmetric tensor presheaf
having an embedding. Then there is a group net bundle G = (G,i )∆ with a full symmetric tensor
embedding ~T⊗,ξ → HilbG(∆) .
Now, any section ̺ ∈ obj ~T⊗,ξ deﬁnes a presheaf bundle β ˆ̺ = ( ˆ̺,r̺)∆ , constructed as follows.
Given a ∈ ∆, the ﬁbre ˆ̺a has objects the tensor powers ̺n
a =̺ ⊗... ⊗̺, n ∈ N, and arrows
β(̺n
a,̺m
a ) := {ta : t ∈ (̺n,̺m)≥a} , (2.15)
where, for any ̺,ς ∈ obj ~T⊗,ξ , we use the notation
(̺,ς )≥a := {t = {to ∈ (̺o,ςo)}o⊇a : roo′(to′ ) = to , ∀o ⊆o′}
(see [39, Prop.3.4] for details). The restriction functors r̺
aa′ : ˆ̺a′ → ˆ̺a , a ⊆a′ , are deﬁned by the
identity on the objects and by restricting raa′ to ˆ̺a′ on the arrows. The following result describes
β ˆ̺ in terms of the presheaf bundles of Ex.2.2:
Theorem 2.3 (Holonomy, [39]) . Let T⊗,ξ = (T,r )∆ be a DR-presheaf. Then for any section
̺ ∈ obj ~T⊗,ξ there are a compact Lie group G̺ ⊆ U(d) such that, up to isomorphism of the ﬁbre,
β ˆ̺ ∈ pbun↑(∆ , ˆπG̺;⊗,θ)
and a morphism
χ̺ :π1(∆) →QG̺ :=NG̺/G̺ ,
which is the holonomy of β ˆ̺ . If there is an embedding of T⊗,ξ then for any section ̺ there must
be a lift ˆχ̺ :π1(∆) →NG̺ , χ̺ = ˆχ̺ mod G̺ .
The existence of embeddings can be described in cohomological term s:
Theorem 2.4 (Gerbes, [39]) . Any section ̺ of a DR-presheaf deﬁnes the cochain
u̺ : Σ 1(∆) →NG̺ : du̺(c) := u̺(∂0c)u̺(∂2c)u̺(∂1c)∗ ∈G̺ , ∀c ∈ Σ 2(∆) .
(Eventual) lifts of χρ are in one-to-one correspondence with pairs (v,g ), v : Σ 0(∆) → NG̺ ,
g : Σ 1(∆) →G̺ , such that
z(b) := v(∂0b)g(b)u̺(b)v(∂1b)∗ ∈NG̺ , ∀b ∈ Σ 1(∆) , (2.16)
is a cocycle, i.e. dz(c) = 1 , ∀c ∈ Σ 2(∆) .
12
3 Presheaves in quantum ﬁeld theory.
In the present section we give the main result of the present paper , showing that the superselec-
tion structures over globally hyperbolic spacetimes introduced by B runetti and Ruzzi ([9]) can be
interpreted as section categories of simple, symmetric tensor pre sheaves.
Actually, the fact that a superselection structure deﬁnes a net T of tensor C*-categories was
recognized in [22, §3], [31, §27] (see Ex.2.1). Nevertheless T does not suﬃce to characterize the
superselection structure itself (see [22, §3.3], [9, §5.1]), so, rather than *-endomorphisms as in [22, 31],
we make use of cocycles, a point of view introduced by J.E. Roberts ( [30]).
Sectors with nontrivial holonomy . Let M be a globally hyperbolic spacetime. Then we have
a causal disjointness relation , that is, a binary, symmetric relation ⊥ deﬁned on subsets of M , see
[22, §2.1]. The physical meaning of ⊥ is that it encodes Einstein causality, which states that events
localized in causally disjoint regions of M do not interfere one each other.
In the following ∆ shall denote the base of diamonds generating the t opology of M (see [22,
§2.1] or, more shortly, [9, §3.1]), thus the abstract results of the previous section apply. We n ote
that any a ∈ ∆ has proper, compact closure a . To be concise we write e<a whenever the closure
of e ∈ ∆ is a proper subset of a ∈ ∆, and set ∆ a := {e ∈ ∆ : e<a } . By [9, Lemma B.5], for any
e ∈ ∆ a there is o ∈ ∆ a with o ⊥e .
Given the Hilbert space H , a Haag-Kastler net over M is given by a net of von Neumann
algebras R = (R,j )∆ ⊂BH , fulﬁlling the following properties:
1. Einstein causality: Ro ⊆R′
e for any e ⊥o;
2. Irreducibility: ∩aR′
a = C1 ;
3. Outer regularity: Ra = ∩a<oRo for any a ∈ ∆;
4. Borchers property: for any a ∈ ∆, e<a and projection E ∈Re there is an isometry Va ∈Ra
such that E =VaV ∗
a .
5. Punctured Haag duality: if x ∈M , then we have Ra = ∩{R′
o :o ∈ ∆ ,o ⊥a,o ⊥ {x}} for any
a ∈ ∆ with a ⊥ {x} .
The crucial property from the viewpoint of physical signiﬁcance is E instein causality, which states
the principle that spacelike separated quantum observables must c ommute and hence there is not
uncertainty between them. The standard way to construct Haag -Kastler nets on curved spacetimes
is the use of free ﬁelds ([11, 12, 4]). About (punctured) Haag dualit y, see [41, 36] and related
references.
We now deﬁne the C∗ -category Z 1(R) with objects unitary cocycles
z := {z(b) ∈UR |b|}b∈Σ 1(∆) : dz(c) := z(∂0c)z(∂2c)z(∂1c)∗ = 1 , ∀c ∈ Σ 2(∆) ,
and arrows
(z,z ′) := { t = {ta ∈Ra}a∈∆ : t∂0bz(b) = z′(b)t∂1b , ∀b ∈ Σ 1(∆) } .
For any path p :a →o, we set
z(p) := z(bn) · · ·z(b1) , p =bn ∗... ∗b1 .
13
In particular, we have the identity cocycle ι(b) := 1 , ∀b ∈ Σ 1(∆). Note that if t ∈ (ι,ι ) then
ta ≡t0 , ∀a ∈ ∆, with t0 ∈ ∩aRa ; we have
∩a∋xRa = C1 , ∀x ∈M (3.1)
(see [9, §3.2],[35, Eq.23]) and this implies ( ι,ι ) = C1 .
As argued in [9, §4], Z 1(R) encodes a superselection structure that gives rise to quantum c harges
aﬀected by the topology of M : for any z ∈ obj Z 1(R) we deﬁne Hz
a :=H , a ∈ ∆, and unitaries
Uz
a′a :=z(a,a ′;a′) : Hz
a →Hz
a′ ⇒ Uz
a′′a′Uz
a′a =Uz
a′′a , ∀a ⊆a′ ⊆a′′ .
This deﬁnes the Hilbert net bundle Hz := (Hz,U z)∆ , which, on turns, yields the C*-net bundle
BHz = (BHz, adUz)∆ and the representation
πz : R → BHz , πz
a(t) := z(p)tz(p)∗ , ∀a ∈ ∆ , t ∈Ra , with p :a →o , o⊥a (3.2)
(see [9, Appendix A]). When Hz is trivial we have sectors in the classical sense (topologically trivial
sectors), that deﬁne representations of Fredenhagen’s univer sal algebra ⃗R ([21]). When M is the
Minkowski spacetime Z 1(R) is the well-known DHR-superselection structure (see [30]).
The conjugation structure on Z 1(R), which encodes the particle-antiparticle correspondence in
the setting of superselection sectors, is deﬁned in the following sta ndard way ([16, 17, 22, 35, 9]): a
cocycle ¯z ∈ obj Z 1(R) is said to be a conjugate of z ∈ obj Z 1(R) whenever there are r ∈ (ι, ¯z ⊗z)
and ¯r ∈ (ι,z ⊗ ¯z) fulﬁlling the conjugate equation
¯r∗ ⊗ 1z · 1z ⊗r = 1z , r ∗ ⊗ 1¯z · 1¯z ⊗ ¯r = 1 ¯z
(about the meaning of ⊗ we refer the reader to [9, §5], anyway it should be clear by reading the
next subsection). In accord with the discussion of [9, §5.3], the full subcategory Z 1,•(R) of Z 1(R)
with objects cocycles admitting a conjugate is a DR-category and y ields the set of sectors with ﬁnite
statistics.
The rest of the section is devoted to the proof that Z 1(R) is the section category of a simple,
symmetric tensor presheaf. This automatically gives to Z 1(R) the structure of a symmetric tensor
C*-category with simple unit, that, as we shall see, coincides with the o ne deﬁned in [9, §5]. For
reader’s convenience, and due to the fact that we shall work with r estricted nets that may not fulﬁll
Haag duality, often we shall write explicitly standard computations.
