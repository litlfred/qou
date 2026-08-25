---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-002-21-lie-groupoids-and-groupoid-actions-on-manifol
section_title: "Lie Groupoids and Groupoid Actions on Manifolds"
section_number: 2.1
pages: 5-6
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
We assume that the reader is familiar with the notions of Lie groupoids , smooth functors and
smooth natural transformations. In this paper, the following exa mples of Lie groupoids appear:
Example 2.1.1.
(a) Every smooth manifold M deﬁnes a Lie groupoid denoted by Mdis whose objects and morphisms
are M , and all of whose structure maps are identities.
(b) Every Lie group G deﬁnes a Lie groupoid denoted by BG, with one object, with G as its smooth
manifold of morphisms, and with the composition g2 ◦g1 :=g2g1.
(c) Suppose X is a smooth manifold and ρ :H ×X /d47/d47 X is a smooth left action of a Lie group
H on X. Then, a Lie groupoid X/ /His deﬁned with objects X and morphisms H ×X, and
with
s(h,x ) := x , t(h,x ) := ρ(h,x ) and id x := (1,x ).
The composition is
(h2,x 2) ◦ (h1,x 1) := (h2h1,x 1),
– 5 –
where x2 =ρ(h1,x 1). The Lie groupoid X/ /His called the action groupoid of the action of H
on X.
(d) Let t :H /d47/d47 G be a homomorphism of Lie groups. Then,
ρ :H ×G /d47/d47 G : (h,g ) ✤ /d47/d47 (t(h)g)
deﬁnes a smooth left action of H on G. Thus, we have a Lie groupoid G/ /H.
(e) To every Lie groupoid Γ one can associate an opposite Lie groupoid Γ op which has the source
and the target map exchanged.
We say that a right action of a Lie groupoid Γ on a smooth manifold M is a pair (α,ρ ) consisting
of smooth maps α :M /d47/d47 Γ 0 and ρ :M α ×t Γ 1 /d47/d47 M such that
ρ(ρ(x,g ),h ) = ρ(x,g ◦h) , ρ(x, idα (x)) = x and α(ρ(x,g )) = s(g)
for all possible g,h ∈ Γ 1,p ∈ Γ 0 andx ∈M . The map α is called anchor. Later on we will replace
the letter ρ for the action by the symbol ◦ that denotes the composition of the groupoid. A left
action of Γ on M is a right action of the opposite Lie groupoid Γ op. A smooth map f :M /d47/d47 M ′
between Γ-spaces with actions ( α,ρ ) and (α′,ρ ′) is called Γ -equivariant if
α′ ◦f =α and f (ρ(x,g )) = ρ′(f (x),g ).
Example 2.1.2.
(a) Let Γ be a Lie groupoid. Then, Γ acts on the right on its morphisms Γ 1 byα :=s and ρ := ◦ .
It acts on the left on its morphisms by α :=t and ρ := ◦ .
(b) Let G be a Lie group. Then, a right/left action of the Lie groupoid BG (see Example 2.1.1 (b))
on M is the same as an ordinary smooth right/left action of G on M .
(c) Let X be a smooth manifold. A right/left action of Xdis (see Example 2.1.1 (a)) on M is the
same as a smooth map α :M /d47/d47 X.
