---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-015-41-d-modules-on-schemes
section_title: "D-modules on schemes"
section_number: 4.1
pages: 27-28
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
[DrG1].
As explained in [DrG1], while this material is well-known at the level of triangulated
categories (standard references include Bernstein’s lecture notes [B] and the books by Borel [Bo] and
Kashiwara [K] for D-modules on varieties, and Bernstein-Lunts’ book [BL] and Beilinson-Drinfeld’s
manuscript [BD, Chapters 1 and 7] for D-modules on stacks), no comprehensive account seems to
exist yet at the level of dg categories (though the aspects of the theory that concern pullbacks are
developed in [GR]).
4.1. D-modules on schemes. Throughout what follows, by a scheme, we will always mean a
quasi-compact, separated derived scheme over C.
To any scheme X, there is attached a dg category D(X) of D-modules on X, deﬁned by taking
ind-coherent sheaves on the de Rham stack of X. The category D(X) is insensitive to the derived
or non-reduced structure of X, so one may assume X is a reduced classical scheme for concreteness.
When X is smooth, D(X) can be canonically identiﬁed with the traditional dg derived category of
right DX-modules (as well as that of left DX-modules).
Given a map f : X →Y of schemes, there are continuous functors
f∗: D(X)
/ D(Y )
f ! : D(Y )
/ D(X).
They satisfy standard composition identities: given a sequence of maps
X
f
/ Y
g
/ Z
there are canonical equivalences of functors (gf)∗≃g∗f∗, (gf)! ≃f !g!. (See Remark 4.1 for more
on the functoriality of the assignment X 7→D(X).)
Note that D(pt) ≃VectC. For the map π : X →pt, we set ωX := π!C ∈D(X), so that f !ωY ≃ωX
for any map f : X →Y . By deﬁnition, the functor of de Rham cohomology is given by pushforward
along π : X →pt which we denote by
ΓdR := π∗: D(X)
/ D(pt) ≃VectC
It is representable by an object denoted by CX ∈D(X) in the sense that there is a functorial
isomorphism
ΓdR(M) ≃HomD(X)(CX, M)
M ∈D(X)
For a map f : X →Y of schemes, the functors f !, f∗satisfy the following standard properties:
• Base change: given a Cartesian square
X ×Y Z
˜g
/
˜f

X
f

Z
g
/ Y
there is a canonical equivalence of functors
˜g∗˜f ! ≃f !g∗.
• Projection formula: there is a functorial equivalence
f∗(f !(N) ⊗M) ≃f∗(M) ⊗N
M ∈D(X), N ∈D(Y )
• If f is proper, there is an adjunction (f∗, f !), and so in particular, f∗is quasi-proper.
27
• If f is an open embedding, there is an adjunction (f !, f∗). More generally, if f is smooth, there
exists a functor
f ∗: D(Y )
/ D(X)
along with an adjunction (f ∗, f∗) and canonical isomorphism
f ∗≃f ![−2(dim X −dim Y )]
In particular f ∗, f ! are quasi-proper, and moreover, f ∗CY ≃CX.
• Kashiwara’s lemma: for i : Z →X a closed embedding, i∗induces an equivalence between
D(Z) and the full subcategory DZ(X) ⊂D(X) of D-modules on X vanishing on X \ Z. The inverse
is given by the restriction of i!.
Remark 4.1. As explained in [FG, DrG1], a natural setting for a complete formulation of the
structure carried by the functors f !, f∗on D-modules is to consider the assignment X 7→D(X) as
a functor on the ∞-category of derived schemes with morphisms given by correspondences. This
automatically encodes base change (as the composition law) as well as the proper and smooth
adjunctions and all the relevant compatibilities.
