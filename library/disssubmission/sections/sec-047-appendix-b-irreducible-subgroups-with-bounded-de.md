---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-047-appendix-b-irreducible-subgroups-with-bounded-de
section_title: "Irreducible subgroups with bounded determinant"
section_number: Appendix B
pages: 165-171
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
In this appendix we discuss the facts from representation theory that
have been used to obtain the ﬁniteness result in lemma 3.19. The basis for
this is the following extended version of the fundamental result of [109],
where by P(X) = Perv(X,C) we denote as before the category of perverse
sheaves on a complex abelian variety X.
LEMMA B.1. Let P ∈P(X) be a semisimple perverse sheaf, G = G(P)
the associated Tannaka group and H = G0 its connected component. Then
the group π = G/H of connected components is a ﬁnite abelian group
whose conjugation action is trivial on the torus Hab = H/[H,H].
Proof. By loc. cit. the group π = G/H of connected components is a
ﬁnite abelian group, and its characters correspond to skyscraper sheaves δx
supported on torsion points x ∈X. Thus the group Hom(π,C∗) of characters
can be identiﬁed in a natural way with a ﬁnite subgroup K ⊆X of torsion
points. Consider then the ´etale isogeny
f :
X −→Y = X/K.
Since |K| = [G : H], lemma 1 in loc. cit. shows that the component H = G0
coincides with the Tannaka group H = G(f∗(P)) of the direct image and
that the adjoint functors
P(X)
f∗
)
P(Y)
f ∗
i
correspond to
RepC(G)
ResG
H
+
RepC(H).
IndG
H
k
Now put m = |K|. For any closed point y ∈Y the pull-back f ∗(δy) is a direct
sum of rank one skyscraper sheaves supported on the m distinct point of the
ﬁbre f −1(y), hence f∗(f ∗(δy)) = (δy)⊕m is an isotypic multiple of δy. In
other words
ResG
H(IndG
H(χ))
is isotypic for all
χ ∈Hom(H,C∗).
Going back to the construction of induced representations, it follows that
every character χ : H −→C∗is invariant under conjugation by G. Via the
equivalence between connected tori and their character groups this implies
that G/H acts trivially on the torus Hab = H/[H,H].
□
157
158
Appendix B – Irreducible subgroups with bounded determinant
With this input from geometry, the rest of the argument for the desired
ﬁniteness result will be an exercise in representation theory. Recall that a
complex algebraic group G is reductive iff the abelian category RepC(G)
of its ﬁnite-dimensional representations over C is semisimple, which is the
case iff G admits a faithful irreducible representation. This is in particular
the case for any irreducible subgroup G ,→Gl(V) of the general linear group
attached to a ﬁnite-dimensional complex vector space V, where as usual by
an irreducible subgroup we mean a subgroup which acts irreducibly on the
given vector space. The result we are looking for is the following.
LEMMA B.2. Fix an integer n ∈N, and let V be a ﬁnite-dimensional
complex vector space. Then up to conjugacy there exist only ﬁnitely many
irreducible algebraic subgroups G ,→Gl(V) such that
(a) the quotient π = G/H by the connected component H = G0 is a
ﬁnite abelian group, and
(b) via conjugation π acts trivially on Hab = H/[H,H], and
(c) the determinant det(V) is a character of G of order at most n.
Proof. Using the structure theory of connected reductive groups and
the fact that every such group has at most ﬁnitely many representations
of any given dimension, one checks that up to conjugation there are only
ﬁnitely many connected reductive algebraic subgroups H ,→Gl(V). So it
will be enough to show that for any given H there exist only ﬁnitely many
irreducible subgroups G ,→Gl(V) with connected component G0 = H such
that (a) – (c) hold. For this we will show that every such subgroup G can
be recovered from the connected component G0 = H together with certain
ﬁnite data. We proceed in the following steps.
Step 1. Let G∗⊆G be a normal subgroup of ﬁnite index, and decompose
the restriction of the given representation asV|G∗= Lm
i=1Vi with irreducible
representations Vi ∈RepC(G∗). Then we claim that for each index i the
determinant character
det(Vi) :
G∗−→C∗
is a character of order at most m · n. Indeed, by the bound in (c) it will be
enough to show that det(Vi) does not depend on i. Note that each g ∈G
deﬁnes an automorphism int(g) : G∗−→G∗, and since V is an irreducible
representation of G, all the irreducible constituents Vi of the restriction V|G∗
are conjugate to each other by such inner automorphisms. Hence it follows
from assumption (b) that the restriction det(Vi)|H does not depend on the
index i. Again by the bound in (c) this restriction is then a torsion character
of the connected group Hab and as such it must be trivial. Thus all the
det(Vi) are characters of the quotient group G∗/H. By assumption (a) the
adjoint action of G on this quotient group is trivial, so our claim follows.
159
Step 2. We now apply step 1 as follows. Let U ⊆V|H be an irreducible
constituent of the restriction of V to the connected component G0 = H, and
consider the stabilizer
G∗=

g ∈G | gU ∼= U in RepC(H)
	
⊆G.
We deﬁne the isotypic part W ⊆V|H to be the sum of all subrepresentations
of V|H which are isomorphic to the chosen representation U. Then W is a
representation of G∗, and a version of Mackey’s lemma shows that
V ∼= IndG
G∗(W)
is isomorphic to the representation induced from W. Since V ∈RepC(G)
is irreducible, it follows that W ∈RepC(G∗) is irreducible as well. But
the group π∗= G∗/H of connected components is abelian by (a) and the
restriction W|H is isotypic, hence lemma B.3 below shows that even W|H
is irreducible. Hence in step 1 we can take V1 = W, and accordingly each
of the conjugate representations V1,...,Vm is stable under the group G∗and
irreducible. For the centralizer of the subgroup H in G then
ZG(H) ,→ZG∗(H) ,→
m
∏
i=1
C∗·idVi,
where the ﬁrst inclusion comes from the fact that the centralizer preserves
each isotypic component and is therefore contained in G∗and where the
second inclusion comes from Schur’s lemma. So each element of ZG(H)
acts on each Vi by a scalar, and by step 1 this scalar is a root of unity of
bounded order. Hence ZG(H) is a ﬁnite group of bounded order.
Step 3. This being said, let us ﬁx as before a connected and reductive
subgroup H ,→Gl(V). By [99, cor. 2.14] the short exact sequence of inner
and outer automorphism groups admits a splitting
1
/ Int(H)
/ Aut(H)
/ Out(H)
/
∃s
x
1
with some section s. In what follows we will ﬁx such a section once and
for all. If G ,→Gl(V) is an irreducible algebraic subgroup with G0 = H
and such that (a) – (c) hold, we want to show that G can be recovered
from certain ﬁnite data involving H and s. To achieve this, consider the
conjugation action
int :
G −→Aut(H)
and denote by F = int−1(Im(s)) ⊂G the preimage of the section s. By
construction we have an exact sequence
1
/ ZG(H)
/ F
ϕ
/ Out(H)
160
Appendix B – Irreducible subgroups with bounded determinant
where ZG(H) = ker(ϕ) denotes the centralizer of H in G. By Step 2 this
centralizer and hence also F is ﬁnite of bounded order. Furthermore, from
the deﬁnitions one checks that the homomorphism
π :
H ⋊ϕ F −→G,
(h, f) 7→hf
is an epimorphism and that ker(π) ⊆Z(H) ⋊ϕ F where Z(H) denotes the
center of H. Note that by Schur’s lemma this center acts by a scalar on each
isotypic component of V|H, in particular Z(H) is a ﬁnite group of bounded
order in view of the bound for the determinant in step 1.
Thus any irreducible algebraic subgroup G ,→Gl(V) with G0 = H and
with properties (a) – (c) is isomorphic to a quotient
G ∼= (H ⋊ϕ F)/K
where F is a ﬁnite group of bounded order, acting on the group H via a
homomorphism ϕ : F →Aut(H) with image in the ﬁnite group s(Out(H)),
and where K is a subgroup of the ﬁnite group Z(H) ⋊ϕ F. Hence for the
isomorphism type of G there are only ﬁnitely many possibilities.
Finally, for (F,ϕ,K) as above, any embedding (H ⋊ϕ F)/K ,→Gl(V)
which extends the given embedding of H is determined uniquely by the
homomorphism ρ : F −→Gl(V) it induces. We claim that under the given
conditions there exist only ﬁnitely many such ρ. Indeed, if ˜ρ is any other
such homomorphism, then for any f ∈F one computes that
ρ(f)· ˜ρ(f)−1 ∈ZGl(V)(H) =
m
∏
i=1
C∗·idVi
where the last equality holds by Schur’s lemma, and in view of the bound
on the determinant in step 1 the centralizer ZGl(V)(H) is ﬁnite.
□
In step 2 of the above proof we have used the following fact, where we
reset our notations and replace G∗by G for simplicity.
LEMMA B.3. Let W be a ﬁnite-dimensional complex vector space, G
an irreducible subgroup of Gl(W) whose group G/G0 of components is
abelian, and H ,→G a subgroup of ﬁnite index such that the restriction W|H
is isotypic. Then in fact W|H is irreducible.
Proof. By d´evissage for the ﬁnite abelian group G/H it will be enough
to show this when G/H ∼= Z/mZ is a ﬁnite cyclic group. Furthermore, by
the assumption of being isotypic we can write
W|H = U ⊗Cn
for some irreducible representation U ∈RepC(H) and some n ∈N. We
must show n = 1. Since G/G0 is abelian, the ﬁnite index subgroup H ⊆G
161
is automatically a normal subgroup. Hence
G ,→NGl(W)(H) = NGl(U)(H)⊗Gln(C)
where the last equality follows via a block matrix calculation from Schur’s
lemma; here the tensor product on the right hand side denotes the image of
the natural homomorphism f : NGl(U)(H)×Gln(C) −→Gl(U ⊗Cn). Now
let ˜G = f −1(G). If 1 denotes the trivial subgroup of Gln(C), then we have
an epimorphism
˜G/(H ×1) ↠G/H
with central kernel (this follows from the fact that f has central kernel). But
by assumption the group G/H is cyclic, and any central extension of a cyclic
group is an abelian group — being generated by a central subgroup together
with a single further element. Hence ˜G/(H × 1) is an abelian group. On
the other hand this abelian group must act irreducibly on Cn because G acts
irreducibly on W. So it follows that n = 1.
□
We conclude this appendix with the following result which does not
directly depend on the above but also involves a Mackey-type argument
and has been used in lemma 4.13 to control the possible non-connectedness
of the Tannaka group attached to the theta divisor.
LEMMA B.4. Let G be a complex reductive group whose group G/G0
of connected components is abelian, and let V ∈RepC(G) be an irreducible
representation. If the restriction V|G0 is reducible, then for some non-trivial
character χ : G −→C∗there exists an isomorphism V ∼= V ⊗C χ.
Proof. Consider the tensor product W = V ⊗C V ∨∈RepC(G) of the
given representation with its dual. We must show that this tensor product
contains a non-trivial one-dimensional representation χ : G −→C∗as a
direct summand. Note that since H = G0 is a normal subgroup of G, the
space of H-invariants
W H = {w ∈W | hw = w ∀h ∈H} ⊂W
is stable under the action of G and hence deﬁnes a representation of the ﬁnite
abelian group G/H. As such it splits into a direct sum of one-dimensional
representations. Among these the trivial representation 1 occurs precisely
once because by adjunction dimC(HomG(1,W)) = dimC(HomG(V,V)) = 1,
using that V is an irreducible representation of G so that Schur’s lemma
applies. So it will be enough to show that
dimC(W H) > 1
if
V|H
is reducible.
But this follows from the observation that if the restriction U = V|H splits
into n direct summands, then W|H = U ⊗CU∨contains at least n copies of
the one-dimensional trivial representation.
□
APPENDIX C
