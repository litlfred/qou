---
doc_id: arxiv-1901.08945v2
doc_title: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES"
section_id: sec-002-3-gerbes
section_title: "Gerbes"
section_number: 3
pages: 13-16
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
doc_brief: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group decomposes accordi ng to the char- acters of"
---
In this section, we collect some results from the theory on gerbes, bandings by
abelian groups and the relation to cohomology. Throughout the sec tion, S will be
an arbitrary algebraic stack. By a stack we mean a, not necessarily algebraic, stack
in groupoids over the big fppf site of schemes over S. The symbol ∆ will always
denote an abelian group in Sfppf . Later on, we will specialize to the situation when
∆ is a diagonalizable group. Accordingly, we will use multiplicative notatio n for ∆
and its cohomology groups H i(Sfppf, ∆).
Deﬁnition 3.1 ([LMB00, Deﬁnition 3.15], [ SP19, Tag 06NZ]). A gerbe overS is
a stack (in groupoids) α : X →S satisfying the following conditions.
(a) The diagonal X →X×SX is an epimorphism (see [ LMB00, Deﬁnition 3.6]).
(b) The structure morphism α :X →S is an epimorphism.
A gerbe is called trivial if the structure morphism in (b) splits.
The prototypical example of a gerbe is the classifying stack BG for a group G
in Sfppf . In fact, any gerbe can be viewed as an fppf -form of a classifying stack.
For any stack α : X → S, we may consider its inertia stack IX/S → X ([SP19,
Tag 034I]), which is a group object in Xfppf . Its points over a morphism x : U →X
14 DANIEL BERGH AND OLAF M. SCHN ¨URER
are simply the 2-automorphisms γ of x mapping to the identity under the compo-
sitionα ◦x. Any object F inXfppf is endowed with a canonical right action by the
inertia IX/S , called the inertial action . Explicitly, it is given on sections over x by
(3.1) F (x) ×IX/S (x) → F (x), (s,γ ) ↦→ F(γ)(s).
We recall the following fundamental fact about the inertial action.
Proposition 3.2. Let α : X →S be a gerbe. Then the functor α∗ : Sfppf →Xfppf
is fully faithful with essential image consisting of sheave s on which the inertia IX/S
acts trivially.
Proof. See for instance [ Lie04, Lemma 2.1.1.17]. □
Deﬁnition 3.3. A gerbe α :X →S is called abelian if the inertia group IX/S →X
is abelian. We denote the full subcategory of stacks over S which are abelian gerbes
by AbGerbe(S).
The inertia acts on itself by conjugation. In particular, Proposition 3.2 shows
that the inertia group of an abelian gerbe α :X →S descends to an abelian group
object in Sfppf , namely α∗IX/S . Furthermore, given any 1-morphism ρ : X →Y of
stacks over S, we get an induced group homomorphism IX/S → ρ∗IY/S in Xfppf ,
and if X and Y are abelian gerbes, this descends to a group homomorphism in
Sfppf . This association gives a functor
(3.2) Band : AbGerbe(S) → AbGroup(S)
to the category of abelian group objects in Sfppf .
Deﬁnition 3.4. Let ∆ be an abelian group object in Sfppf . The essential ﬁber of
the functor ( 3.2) over ∆ is called the category of gerbes banded by ∆ or of ∆ -gerbes.
Explicitly, a ∆-gerbe is given by a pair ( α,ι ) where α : X →S is an abelian gerbe
andι : ∆
∼
− →α∗IX/S is a group isomorphism called a banding ofα by ∆. The group
∆ is called the band of ( α,ι ). A morphism of ∆-gerbes is simply a morphism of
stacks such that corresponding morphism on inertia induces the ide ntity on ∆ via
the bandings. By abuse of notation, we usually denote a ∆-gerbe ( α,ι ) by α or
evenX.
Remark 3.5. Giraud introduces a more general notion of banding applying to non-
abelian gerbes [ Gir71, Chapter IV]. We will not need this, more complicated, theory
here.
Note that a 1-morphism of gerbes over S is always an epimorphism ([ LMB00,
Lemma 3.17]), and that it is an isomorphism if and only if it induces an isomo rphism
on inertia. In particular, the category of ∆-gerbes is a 2-groupoid .
Example 3.6. LetS be an algebraic stack, and let ∆ and ∆ ′ be abelian groups in
Sfppf .
(a) The classifying stack B ∆ is endowed with a canonical structure o f ∆-gerbe.
(b) Given a pair of abelian gerbes X and X ′ over S, banded by ∆ and ∆ ′,
respectively, the productX×SX ′ has a naturally deﬁned banding by ∆ ×∆ ′.
The following example illustrates that it is very natural to consider ge rbes over
genuine algebraic stacks.
Example 3.7. Let S be an algebraic stack. Assume that we have a central ex-
tension 1 → ∆ →G →H → 1 of groups in Sfppf . Then the induced morphism of
classifying stacks BG → BH has a canonical structure of a ∆-gerbe. The following
examples are two important special cases with S = Spec Z.
DECOMPOSITIONS 15
(a) The morphism G →H is the quotient map GL n → PGLn. In this case we
obtain a Gm-gerbe B GLn → B PGLn.
(b) The morphism G →H is the morphism Gm → Gm given byx ↦→xn. In this
case the corresponding µn-gerbe B Gm → B Gm can be thought of as the
n-th root stack of the universal line bundle [ A1/Gm] on B Gm (cf. [ Cad07,
Deﬁnition 2.2.6]).
Next we discuss functoriality of banded gerbes with respect to cha nge of group.
Construction 3.8. Letϕ : ∆ → ∆ ′ be a homomorphism of abelian group objects in
S, and let α : X →S be a gerbe banded by ∆. We construct a gerbe ϕ∗α :ϕ∗X →S
banded by ∆ ′ together with a morphism
(3.3) ρ : X →ϕ∗X
of gerbes over S inducing the homomorphism ϕ on the bands as follows.
Consider X × B ∆ ′ with its natural banding by ∆ × ∆ ′. We deﬁne ϕ∗X as
the rigidiﬁcation (see [ AOV08, Appendix A]) of X × B ∆ ′ in the kernel of the
epimorphism ∆ × ∆ ′ → ∆ ′ given by ( a,b ) ↦→ϕ(a)b. The morphism ρ is the
composition of the obvious map X →X × B ∆ ′ followed by the rigidiﬁcation map.
The construction above shows that given a gerbe banded by ∆, any morphism
ϕ : ∆ → ∆ ′ lifts to a morphism of banded gerbes. The following proposition, which
we surprisingly could not ﬁnd in the literature, shows that this lift is es sentially
unique. In particular, Construction 3.8 is functorial in a weak sense.
Proposition 3.9. Let ∆ be an abelian group in Sfppf , and let α :X →S be a gerbe
banded by ∆ . Then the obvious functor
(3.4) Band X/ : AbGerbe(S)X/ → AbGroup(S)∆ /
from the category of abelian gerbes over S underX to the category of abelian groups
in Sfppf under ∆ is an equivalence of categories.
Proof. Construction 3.8 shows that the functor Band X/ is essentially surjective on
objects. Let ρ : X →Y and ρ′ : X →Y ′ be objects of AbGerbe(S)X/ , and denote
their images in AbGroup(S)∆ / by ϕ : ∆ → Γ and ϕ′ : ∆ → Γ ′, respectively. We
need to show that
(3.5) Hom X/ (ρ,ρ ′) → Hom∆ / (ϕ,ϕ ′)
is and equivalence of categories. To do so, we ﬁrst note that ( 3.5) is functorial in S,
and that we in fact have a morphism of stacks
(3.6) Φ : HomX/ (ρ,ρ ′) → Hom∆ / (ϕ,ϕ ′)
overS. Explicitly, this morphism is constructed as the canonical map in the d iagram
(3.7) Hom∆ / (ϕ,ϕ ′)
/d15/d15
/d47/d47S
ϕ ′
/d15/d15
HomX/ (ρ,ρ ′)
/d15/d15
/d47/d47
Φ
/d104/d104PPPPPPPPPPPP
S
id
/d55/d55♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
ρ ′
/d15/d15
Hom(Y,Y ′)
−◦ρ /d47/d47
/d118/d118♠♠♠♠♠♠♠♠♠♠♠♠ Hom(X,Y ′)
/d39/d39PPPPPPPPPPPP
Hom(Γ, Γ ′)
−◦ϕ /d47/d47 Hom(∆ , Γ ′),
where the inner and the outer squares are cartesian.
16 DANIEL BERGH AND OLAF M. SCHN ¨URER
To verify that Φ is an isomorphism, we may work locally on S. In particular, we
may assume that the stacksX,Y andY ′ are the classifying stacks B ∆, B Γ and B Γ ′,
respectively. Furthermore, we may assume that the morphisms ρ and ρ′ are given
by extension of torsors along ϕ and ϕ′, respectively. In this situation, we have
Hom(X,Y ′) ∼= [Hom(∆ , Γ ′)/Γ ′], where Γ ′ acts trivially, and the map to Hom(∆ , Γ ′)
is induced by forgetting the group action (see e.g. Abramovich et al. [AOV08,
Lemma 3.9(1)] and its proof). Plugging this into ( 3.7), together with the similar
description for Hom(Y,Y ′) and the obvious descriptions for ρ′ and − ◦ρ, it becomes
clear that Φ is an isomorphism. □
Construction 3.10. Let ∆ be an abelian group in Sfppf , and let α,β : X →S be
∆-gerbes. Denote the multiplication map on ∆ by m : ∆ × ∆ → ∆, and the n-th
power map, for n ∈ Z, by pn : ∆ → ∆. Using Construction 3.8, we deﬁne
(3.8) αβ :=m∗(α ×β), α n := (pn)∗α.
Morally, Construction 3.10 gives the 2-groupoid of ∆-gerbes the structure of
an abelian group, a statement which presumably could be made precis e by use of
Proposition 3.9. At least, it is clear that the set of isomorphism classes of ∆-gerbes
forms an abelian group.
It is easy to see that we also have functoriality with respect to chan ge of stacks.
That is, let f : T → S be a morphism of algebraic stacks and let α : X → S be a
∆-gerbe. Then the pull-back f ∗α has a natural structure of f ∗∆-gerbe.
Theorem 3.11 (Giraud). Let S be an algebraic stack and let ∆ be an abelian
group in Sfppf . Then the group H2(Sfppf, ∆) is canonically isomorphic to the set of
isomorphism classes of ∆ -gerbes over Sfppf , with its group structure induced by the
operations in Construction 3.10. Given a ∆ -gerbeα over Sfppf , we denote its class
in H2(Sfppf, ∆) by [α]. We have the following functorial properties:
(a) Given a morphism f : T →S of algebraic stacks, we have [f ∗α] = f ∗[α] in
H 2(Tfppf,f ∗∆) .
(b) Given a homomorphism of abelian groups ϕ : ∆ → ∆ ′, we have [ϕ∗α] =
ϕ∗[α] in H 2(Sfppf, ∆ ′).
Proof. This is worked out in various places in [ Gir71]. Functoriality with respect to
change of groups is described in Section IV.3.1. Comparison with usua l cohomology
is in Section IV.3.4, and functoriality with respect to change of topos in Section V.1.
□
