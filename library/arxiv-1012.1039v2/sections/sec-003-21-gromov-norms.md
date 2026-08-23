---
doc_id: arxiv-1012.1039v2
doc_title: "where vn is the volume of a regular ideal hyperbolic n–simplex. This result gener- alizes the fact that hyperbolic Dehn ﬁlling of a 3–manifold d oes not increase hyperbolic volume"
section_id: sec-003-21-gromov-norms
section_title: "Gromov norms"
section_number: 2.1
pages: 4-6
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
for some Y ⊂X. The Gromov norm of ω is the smallest l1–norm of a real singular
chain representing ω,
‖ω‖ = inf
{ k∑
i=1
|αi|
⏐
⏐
⏐
⏐
⏐
[k∑
i=1
αiσi
]
=ω
}
.
(Since this inﬁmum may be zero, the “Gromov norm” is only a seminorm in general.)
This quantity only depends on ω and the homotopy type of the pair ( X,Y ). In the
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS 5
absolute case, we can use it to deﬁne the Gromov norm of any ω ∈H∗(G), where
G is a discrete group, by choosing X to be a K(G, 1).
Ifω is an integral cycle and η is the canonical map from integral to real homology,
then we set ‖ω‖ = ‖η(ω)‖.
The Gromov norm of a cycle can be computed via the pairing between b ounded
cohomology and l1 homology: If ω ∈ Hk(X) and H k
b (X; R) is the k–dimensional
bounded cohomology of X, then
(3) ‖ω‖ = sup
({ 1
‖φ‖∞
⏐
⏐
⏐
⏐φ ∈H k
b (X; R), ⟨φ,ω ⟩ = 1
}
∪ {0}
)
.
See [BP92, Proposition F.2.2] for a proof.
For M a closed orientable n–manifold, Gromov deﬁned the simplicial volume
‖M ‖ to be the Gromov norm of the fundamental class in Hn(M ; R). For a man-
ifold with boundary, it is natural to deﬁne ‖M,∂M ‖ to be the Gromov norm of
the fundamental class in Hn(M,∂M ; R). It is clear from the deﬁnition that this
volume only depends on the homotopy type of ( M,∂M ). For closed hyperbolic
manifolds the simplicial volume is proportional to the volume. More gen erally, if
M is compact, and the interior of M admits a complete ﬁnite volume hyperbolic
metric of volume Vol, then
‖M,∂M ‖ = 1
vn
Vol,
where vn is the volume of a hyperbolic regular ideal simplex of dimension n. (See
[BP92, C.4] for the closed case; we show how to extend to the ﬁnite v olume case in
Appendix A.)
In [Yam97], Yamaguchi extended the notion of simplicial volume to orie ntable
pseudomanifolds, deﬁned as follows.
Deﬁnition 2.1. [Yam97, Deﬁnition 2.1] A locally compact, Hausdorﬀ, locally ho-
mologically n–connected space X is called an orientedn–pseudomanifold if it con-
tains a closed subset S (the singular set ) so that:
(i) X /integerdivideS is an orientable n–manifold,
(ii) dim(S) ≤n − 1, and
(iii) dim(S ∩
X /integerdivideS) ≤n − 2.
Remark 2.2. In this deﬁnition, we allow the possibility that S is not “really”
singular. For example, X could be a manifold and S a codimension 2 submanifold.
This is important in applying Proposition 2.3 to 2 π–ﬁllings which happen to be
manifolds, as in Corollary 2.5 below.
In [Yam97, Proposition 2.2], Yamaguchi shows that an oriented n–pseudomani-
foldX has a fundamental class [ X] in Hn(X) = Hn(π1(X)) so that the orientation
cocycleβ ∈H n(X) is dual to this class. For such a pseudomanifold X, the simplicial
volume of X is deﬁned to be the Gromov norm of [ X], and written ‖X‖.
IfX is compact with CAT( −1) universal cover, then X is aspherical and π1(X)
is (word) hyperbolic [Gro87]. In this case the orientation cocycle is co homologous
to a bounded cocycle by the main theorem of [Min02], and so ‖X‖ > 0 by the
duality equation (3).
IfX is compact and the universal cover is CAT(0) with isolated ﬂats, the nX is
again aspherical, but π1(X) is only relatively hyperbolic, relative to fundamental
groups of images of ﬂats in X [HK05b]. In this case, we will need the following
corollary of a theorem of Mineyev–Yaman:
6 K. FUJIW ARA AND J. F. MANNING
Proposition 2.3. LetM be a closed orientable aspherical n–dimensional pseudo-
manifold with singular set V ⊂ M which is a disjoint union of aspherical compo-
nents V = ∪m
i=1Vi. Suppose that π1(M ) is hyperbolic relative to the collection of
subgroups {π1(Vi) |i ∈ {1,...,n }}. Then ‖M ‖> 0.
Proof. The inclusion of pairs ( M, ∅) → (M,V ) gives a natural map
H n(M,V ; R) →H n(M ; R).
Since dim(V ∩
M /integerdivideV ) ≤ n − 2, the Mayer–Vietoris exact sequence shows this
map to be an isomorphism (cf. [Yam97, Proposition 2.2]). The main resu lt of
Mineyev–Yaman [MY] implies that the map
H n
b (π1(M ), {π1(Vi)}m
i=1; R) →H n(π1(M ), {π1(Vi)}m
i=1; R)
is surjective, since π1(M ) is hyperbolic relative to the fundamental groups of the
components of V . Since M and the components of V are aspherical, this is the
same as saying that the map
(4) H n
b (M,V ; R) →H n(M,V ; R) = H n(M ; R)
is surjective. It follows that the orientation cocycle of M is cohomologous to a
bounded cocycle α. (The cocycle moreover can be chosen to vanish on chains in V ,
but we don’t use this.) Equation (3) gives ‖M ‖ ≥ 1
‖α‖ ∞
> 0. □
Applying Theorem 1.4, we immediately obtain the lower bound of Theore m 1.5.
Corollary 2.4. If M (T1,...,T m) is a 2π–ﬁlling as in Theorem 1.5, then
‖M (T1,...,T m)‖> 0.
The special case of nonpositively curved manifolds obtained by 2π–ﬁlling of ≥ 4–
dimensional hyperbolic manifolds has been studied before us by Schr oeder, Ander-
son and others [Sch89, And06]. Ivanˇ si´ c describes in [Iva04] a pa rticular cusped
hyperbolic manifold which is the complement of ﬁve linked 2–tori in the 4 –sphere.
Ratcliﬀe and Tschantz point out in [RT05] that appropriately chosen 2π–ﬁllings of
this hyperbolic manifold are homology 4–spheres. In [Bel06, Question 7.2], Bele-
gradek asked if such ﬁllings have positive simplicial volume. As a special case of
2.4 above, we give an aﬃrmative answer.
Corollary 2.5. Every manifold obtained by 2π–ﬁlling of an orientable hyperbolic
n–manifold with torus cusps has positive simplicial volume. In particular, the as-
pherical homology 4–spheres constructed by Ratcliﬀe and Tschantz have positiv e
simplicial volume.
Theorem 1.5 gives further information (an upper bound) on the simp licial vol-
ume.
