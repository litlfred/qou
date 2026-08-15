---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds Stefano Francaviglia12"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds Stefano Francaviglia12 — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2"
---
LetW be a compact manifold and let ρ be a representation of its fundamental
group into PSL(2, C) ≃ Isom+(H3). The volume of ρ is deﬁned by taking any
ρ-equivariant map from the universal cover ~W to H3 and then by integrating
the pull-back of the hyperbolic volume form on a fundamental domain . This
volume does not depend on the choice of the equivariant map becaus e two
1Author address: Stefano Francaviglia, Dipartimento di Matematic a Applicata “U.
Dini”, via Bonanno 25b, I-56126 Pisa, e-mail: s.francaviglia@sns.it.
2This work was partially written while the author was a PhD student at t he Scuola Nor-
male Superiore di Pisa, and was partially supported by the C.R.M. (Univ ersit´ at Autonoma
de Barcelona).
1
equivariant maps are always equivariantly homotopic and the cohomo logy-
class of the pull-back of the volume form is invariant under homotopy .
In [D] this deﬁnition is extended to the case of a non compact cusped
3-manifold M (see Deﬁnitions 4.1 and 2.5). When M is not compact, some
problems of integrability arise if one tries to use the above deﬁnition o f the
volume of a representation. The idea of Dunﬁeld for overcoming the se diﬃ-
culties is to use a particular (and natural) class of equivariant maps, called
pseudo-developing maps (see Deﬁnition 2.5), that have a nice behavior on the
cusps of M allowing to control their volume. Concerning the well-deﬁnition
of the volume, working with non-compact manifolds, two pseudo-de veloping
maps in general are not equivariantly homotopic and in [D] it is not prov ed
that the volume of a representation does not depend on the chose n pseudo-
developing map.
In this paper we show that the volume of a representation is well-deﬁ ned
even in the non-compact case, and we generalize to non-compact m anifolds
some results know in the compact case. We restrict to the orientab le case.
The paper is structured as follows.
In Sections 2 and 3 we introduce the notion of pseudo-developing ma p for
a given representation ρ :π1(M) → Isom+(H3) and the notion of straighten-
ing of such a map.
In Section 4 we prove that for each orientable cusped 3-manifold M and
for each representation ρ : π1(M) → Isom+(H3), the volume of ρ is well-
deﬁned and depends only on ρ. The main theorems are:
Theorem 4.9 Let Dρ and Fρ be two pseudo-developing maps for ρ. Then
vol(Dρ) = vol(Fρ).
Theorem 4.10 For any pseudo-developing map Dρ forρ we have vol(Dρ) =
Strvol(Dρ).
Roughly speaking, Theorem 4.10 says that the volume of ρ can be com-
puted by straightening any ideal triangulation of M and then summing the
volume of the straight version of the tetrahedra.
In Section 5, generalizing the techniques used for the proof of The o-
rem 4.10, we show that the volume of a representation ρ is bounded from
above by the relative simplicial volume:
Theorem 5.1 For all representations ρ : π1(M) → Isom+(H3) we have
|vol(ρ)|<v 3 · ||(
M,∂M )||, where v3 is the volume of a regular ideal tetrahe-
dron in H3.
2
In Section 6 we prove the following rigidity theorem for representat ions
of the fundamental group of a hyperbolic manifold:
Theorem 6.1 Let M be a non-compact, complete, orientable hyperbolic 3-
manifold of ﬁnite volume. Let Γ ∼= π1(M) be the sub-group of PSL(2, C)
such that M = H3/Γ . Let ρ : Γ → PSL(2, C) be a representation. If
|vol(ρ)| = vol(M) then ρ is discrete and faithful. More precisely there ex-
ists ϕ ∈ PSL(2, C) such that for any γ ∈ Γ
ρ(γ) = ϕ ◦γ ◦ϕ−1.
In Section 7 we give some corollaries. In particular we show how from
Theorem 6.1 one can get a proof of Mostow’s rigidity for non-compac t mani-
folds (see [P] and [BCS] for a more general statement and a diﬀere nt proof):
Theorem 7.1 (Mostow’s rigidity for non-compact manifold) Let f :
M → N be a proper map between two orientable non-compact, complet e
hyperbolic 3-manifolds of ﬁnite volume. Suppose that vol(M)=deg(f )vol(N).
Then f is properly homotopic to a locally isometric covering with t he same
degree as f .
Other corollaries that can be useful for checking the hyperbolicity of a
3-manifold are also shown.
I would like to thank Carlo Petronio and Joan Porti for the very many
very interesting conversations about this theme.
2 General deﬁnitions
We ﬁx here the class of manifolds we consider, namely the class of idea lly
triangulated cusped manifolds. Since we work with cusped manifolds, we
want to ﬁx a structure on the cusps.
Deﬁnition 2.1 (Cusped manifold) An orientable manifold M is called
cusped manifold if it is diﬀeomorphic to the interior of a compact manifold
with boundary
M . A cusp of M is a closed regular neighborhood of a com-
ponent of ∂M . In the following we require M to have dimension 3 and ∂M
to be a union of tori, so each cusp is homeomorphic to T 2 × [0, ∞).
We deﬁne ˆM as the compactiﬁcation of M obtained by adding one point
for each cusp of M. Called ~M the universal cover of M, we call ˆ~M the space
obtained by adding to ~M one point for each lift of each cusp of M.
3
We call the points added to M (or ~M) ideal points of M (or ~M ). For
each ideal point p of M, we ﬁx a smooth product structure Tp × [0, ∞) on
the cusp relative to p. Such a structure induces a cone structure, obtained
from Tp × [0, ∞] by collapsing Tp × {∞} to p, on a neighborhood Cp of p in
ˆM .
We lift such structures to the universal cover. Let ~p be an ideal point of
~M that projects to the ideal point p of M. We denote by N~p the cone at ~p.
The cone N~p is homeomorphic to P~p × [0, ∞] where P~p covers the torus Tp
and P~p × {∞} is collapsed to ~p.
Remark 2.2 In the deﬁnition of cusped manifold we have included a ﬁxed
product structure on the cusps. This is for technical reasons, h owever we will
show that the results about the volume of representations do not depend on
the chosen structure.
Remark 2.3 Let ~M be the universal cover of M. In the following, when we
speak about π1(M), we tacitly assume that a base-point and one of its lifts
have been ﬁxed. If p is an ideal point of M, then π1(Tp) is well-deﬁned only
up to conjugation. Called {~pi} the set of the lifts of p, there is a one-to-one
correspondence between the stabilizers Stab( ~pi) of ~pi in the group of deck
transformations of ~M →M and the conjugates of π1(Tp) in π1(M). Such a
correspondence is uniquely determined once the base-points have been ﬁxed.
To avoid pathologies, since we are working with cusped manifolds, we
need that the maps we use have a nice behavior “at inﬁnity.” Namely, w e
will often require that a map from a cusp to H3 is a cone-map in the following
sense.
Deﬁnition 2.4 (Cone-map) Let A be a set, c ∈ R and C be the cone
obtained from A × [c, ∞] by collapsing A × {∞} to a point, which we call
∞. A map f :C →
H
n
is a cone-map if:
• f (C) ∩∂Hn = {f (∞)};
• ∀a ∈A the map f|a×[c, ∞] is either the constant to f (∞) or the geodesic
ray from f (a,c ) to f (∞), parametrized in such a way that the param-
eter (t −c), t ∈ [c, ∞], is the arc-length.
We recall here the deﬁnition of pseudo-developing map for a repres enta-
tion (see [D]).
4
Deﬁnition 2.5 (Pseudo-developing map) Let M be a cusped manifold
and let ρ : π1(M) → Isom+(H3) be a representation. A pseudo-developing
map for ρ is a piecewise smooth map Dρ : ~M → H3 which is equivariant
w.r.t. the actions of π1(M) on ~M via deck transformations and on H3 viaρ.
Moreover we require Dρ to extend to a continuous map, which we still call
Dρ, from ˆ~M to H
3
that maps the ideal points to ∂H3 (see Remark 2.6 for
comments on this property). Finally we require that there exists tDρ ∈ R+
such that for each cusp Np = Pp × [0, ∞] of ~M , the restriction of Dρ to
Pp × [tDρ, ∞] is a cone-map.
Let γ ⁄= id be an isometry of H3 and let Fix(γ) be the set of ﬁxed points
of γ. Then Fix( γ) ∩∂H3 consists of either one or two points. Moreover, if
γ1 and γ2 commute, then Fix( γ1) is γ2-invariant. It follows that if Γ is an
Abelian subgroup of orientation-preserving isometries and γ ∈ Γ, then Fix(γ)
is Γ-invariant. Actually, for almost all Abelian Γ and for any γ1,γ 2 ∈ Γ \ {id}
we have
Fix(γ1) = Fix(γ2).
The only cases in which this is not true are when Γ is a dihedral group
generated by two rotations of angle π around orthogonal axes. Such a group
is isomorphic to Z2 × Z2 and its unique ﬁxed point is the intersection of the
axes. It follows that any Abelian group Γ of orientation-preserving isometries
has a ﬁxed point in H
3
and, if Γ is not dihedral, then it has a ﬁxed point in
∂H3.
Let now p be an ideal point of ˆ~M . Since Stab(p) is Abelian, then either it
is dihedral or it has a ﬁxed point in ∂H3. If ρ is a representation of π1(M) and
Dρ is a pseudo-developing map for ρ, thenDρ(p) is a ﬁxed point of ρ(Stab(p)).
It follows that, using Deﬁnition 2.5, in order for a pseudo-developing map to
exist, ρ(Stab(p)) must have a ﬁxed point in ∂H3.
Remark 2.6 We included in Deﬁnition 2.5 the requirement that Dρ maps
ideal points to ∂H3 only for simplicity. No pathologies do occur if some ideal
point is mapped to the interior of H3. Coherently with this fact, from now
on we suppose that:
For each boundary torus T , the group ρ(π1(T )) is not dihedral.
As above we notice that this is only for simplicity and one can easily chec k
that all the results of this paper remain true, mutatis mutandis , without this
assumption.
5
Lemma 2.7 Let M be a cusped manifold and let ρ :π1(M) → Isom+(H3) be
a representation. Then a pseudo-developing map Dρ exists.
Proof. The proof is the same as in [D], we recall it by completeness. We
construct a pseudo-developing map inductively on the n-skeleta. Let p be
an ideal point of ~M . Since Stab( p) is Abelian and not dihedral, then its
ρ-image has at least one ﬁxed point q ∈∂H3. We deﬁne Dρ(p) = q and, for
all α ∈ π1(M) we set Dρ(α(p)) = ρ(α)(q). We do the same for the other
ideal points. Now for each ideal point p we deﬁne Dρ on Pp × {0} in any
Stab(p)-equivariant way and then we make the cone over Dρ(p) in such a
way that Dρ has the cone property. Then we extend Dρ in any equivariant
way. The extension is possible because H3 is contractible.
✷
Remark 2.8 Let p be an ideal point of ˆ~M. If ρ(Stab(p)) is a parabolic
non-trivial group, then it has a unique ﬁxed point. It follows that Dρ(p) is
uniquely determined. Thus, if all the ρ-images of the stabilizers of the ideal
points are parabolic, then the Dρ-images of all the ideal points are uniquely
determined.
Deﬁnition 2.9 (Ideally triangulated manifold) LetM be a cusped man-
ifold. An ideal triangulation of M is a triangulation of ˆM having the set of
ideal points as 0-skeleton. An ideally triangulated manifold is a cusped man-
ifold equipped with a ﬁnite smooth ideal triangulation τ . We require the
triangulation to be compatible with the product structure. That is, for each
cuspNp we requireτ ∩(Tp×{0}) to be a triangulation of Tp and the restriction
to Np of τ to be the product triangulation.
We will often consider the simplices of an ideal triangulation of a manifo ld
M as subsets of ˆM .
Remark 2.10 It is well-known that any cusped manifold can be ideally
triangulated (see for example [BP]).
