---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-002-21-geometry-of-posets
section_title: "Geometry of posets."
section_number: 2.1
pages: 5-7
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
Let M be a connected manifold. We say that a base ∆ for the topology of M is good whenever
any a ∈ ∆ has compact closure and is arcwise and simply connected. For exam ple, we have the
Minkowski spacetime, that has a good base given by the set of doub le cones, or, more generally, a
globally hyperbolic spacetime, that has a good base base given by the set of diamonds ([22, 9]). In
the present paper we shall always consider good bases.
Now, ∆ becomes a poset (partially ordered set) when endowed with the order relation given b y
the inclusion, and encodes some geometric invariants of M . As a ﬁrst step we consider the simplicial
set deﬁned by ∆, whose sets at lower degrees are deﬁned as follows ([32, 33]):
• Σ 0(∆) := ∆, the set of 0 -simplices, that are the analogues of ”points”;
• Σ 1(∆), the set of 1 -simplices, is the set of ”oriented lines” of the type
b := (∂1b,∂ 0b; |b|) : ∂1b,∂ 0b, |b| ∈ ∆ and ∂1b,∂ 0b ⊆ |b|.
• Finally we deﬁne the set Σ 2(∆) of 2 -simplices (”oriented triangles”) with elements quadruples
c = (∂0c,∂ 1c,∂ 2c ∈ Σ 1(∆); |c| ∈ ∆) such that
∂hkc :=∂h∂kc =∂k∂h+1c , |∂hc| ⊆ |c| , ∀h ≥k . (2.1)
Using 1 -simplices we deﬁne paths, in terms of sequences
p :=bn ∗... ∗b1 : ∂0bk =∂1bk+1 , ∀k = 1,...,n .
To emphasize the initial and ending ”points” of p we use the notation
p :a →o , a =∂1b1 , o =∂0bn .
The opposite path of p is given by p := b1 ∗... ∗bn : o → a, where any bk , k = 1,...,n , is the
1-simplex deﬁned by
∂1bk :=∂0bk , ∂ 0bk :=∂1bk , |bk| := |bk|.
A path frame with pole ω ∈ ∆ is a set
Pω = {paω :ω →a , ∀a ∈ ∆ } (2.2)
5
such that pωω =bω := (ω,ω ;ω) ∈ Σ 1(∆). To be concise we write
pωa :=paω .
Paths of the type p :a →o, p′ :o →e can be composed by deﬁning p′ ∗p :=b′
m ∗... ∗b′
1 ∗bn ∗...b 1 ,
so in particular the set of paths of the type p : a → a, called loops, is a semigroup. There is an
equivalence relation on paths, called homotopy, and the quotient π1(∆) of the set of loops starting
and ending at a ∈ ∆ is a group, whose isomorphism class does not depend on a. There is an
isomorphism
π1(∆) ≃ π1(M ), (2.3)
where π1(M ) is the fundamental group; this implies π1(M ) = 0 when ∆ is directed (see [35]).
Finally, in the spirit of [29], we mention that the above constructions a pply to a category C
in place of a poset 2, as for example the category of globally hyperbolic spacetimes at th e root
of locally covariant quantum ﬁeld theory [5]. One deﬁnes Σ 0(C) = obj C , Σ 1(C) as the set of
pairs b = (b1,b 0) of arrows having the same target |b| ∈ obj C and so on, obtaining the notion of
fundamental group of C .
Characteristic classes for representations of π1(∆) . Let G be a topological group and
χ :π1(∆) →G
a morphism. Using (2.3) we identify π1(∆) with the fundamental group and recall that the universal
cover ˜M deﬁnes a principal π1(∆)-bundle q : ˜M → M , so any ﬁbre q−1(x), x ∈ M , is a right
π1(∆)-space. Given a left G-space F with action g,v ↦→gv , g ∈G, v ∈F , this yields the induced
F -bundle
qχ :Pχ →M , (2.4)
where Pχ is the quotient of ˜M ×F by the equivalence relation
(y,v ) ∼ (yp,χ (p)v) , p ∈π1(∆) ,
and qχ(y,v )∼ :=q(y), for any ( y,v )∼ ∈Pχ . A F -bundle of the above kind is called locally constant
bundle, see [24, §I.2].
Let now F be a manifold and G a Lie group. We consider a F -bundle P →M , not necessarily
locally constant, and a characteristic class ζ deﬁning the 2 k -form ζ(P ) ∈ Z 2k
deRham(M ), k ∈ N.
We say that ζ has periods in the ring K ⊂ R whenever
∫
c
ζ(P ) ∈ K
for any 2 k -cycle c ∈Z2k(M ). In [10] it is proved that there is a unique morphism
ζ↑(P ) : C2k−1(M ) → R/K,
where C2k−1(M ) is the group of singular (2 k − 1)-chains, such that
{ζ↑(P )}(∂ℓ) =
∫
ℓ
ζ(P ) modK , ∀ℓ ∈C2k(M ) ,
2This approach has been object of (unpublished) work by J. Rob erts, G. Ruzzi and the author.
6
where ∂ :C2k(M ) →Z2k−1(M ) is the boundary map.
Since it is well-known that ζ(Pχ) = 0 for any locally constant bundle Pχ (see [24, §II.3]), we have
that ζ↑(Pχ) vanishes on ∂C2k(M ), so it yields a cocycle deﬁning a class in singular cohomology,
ζ↑(χ) := [ζ↑(Pχ)] ∈H 2k−1(M, R/K), (2.5)
which by construction vanishes when χ is the trivial morphism. For example, it is well-known
that the Chern classes ck(P ) ∈Z 2k
deRham(M ), k ∈ N, have periods in Z, so for any representation
χ :π1(∆) → U(d) there are classes
c↑
k(χ) ∈H 2k−1(M, R/Z) , k = 1,...,d . (2.6)
