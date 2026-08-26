---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-030-ribbon-invariants-from-line-defects
section_title: "Ribbon invariants from line defects"
section_number: null
pages: 59-68
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
In this section we show how defect lines on trivial defect surfaces give rise to ribbon invariants. These surfaces
are labeled by a spherical fusion categoryC as a (C,C)-bimodule category. AsC is a spherical fusion category,
its centerZ(C) is a ribbon category, see for instance [TV10, Lemma 10.1]. By Example 1.10, the monoidal
category EndC(C) is monoidally equivalent toZ(C). Under this monoidal equivalence, an object(a,σ−,a) of
Z(C) corresponds to the(C,C)-bimodule functorF =a⊗− :C→C with coherence data
sF
c,c′ =ac,a,c′◦ (σ−1
c,a⊗ 1c′)◦a−1
a,c,c′ :a⊗ (c⊗c′)→ (a⊗c)⊗c′→ (c⊗a)⊗c′→c⊗ (a⊗c′), (104)
tF
c,c′ =aa,c,c′ : (a⊗c)⊗c′→a⊗ (c⊗c′)
and a morphismα :a→b inZ(C) to the (C,C)-bimodule natural transformationν =α⊗− :a⊗−⇒ b⊗−
from Example 1.10.
Any diagram representing a ribbon tangle forZ(C) can be realised as a defect graph on a trivial defect disc.
This amounts to replacing over- and undercrossings in the diagram with defect vertices labeled by (inverse)
braidings and maxima and minima by defect vertices labeled with the (co)evaluations inZ(C). Every diagram
D for a (0, 0)-ribbon tangle then defines a morphismα∈ EndZ(C)(e) and a bimodule natural transformation
ν =α⊗− : idC⇒ idC with νx = tr(α)1x = ev(D)1x :x→x for everyx∈IC.
Example 6.5. LetC be a spherical fusion category andt a tetrahedron as in Figure 2 (b) with a trivial defect
surface that contains a diagramD for a (0, 0)-ribbon tangle labeled withZ(C). Then one has
Z′(t,l∂M,b∂M ) = ev(D)· 6j(t′,l∂M,b∂M ),
wheret′ is the tetrahedron with the same labels and without the defects andev(D)∈ C the evaluation ofD.
Proof. The 6j symbol of the defect tetrahedront is obtained from the associated polygon diagram
q
nm
p
j
D
i
α
β
γ
δ
where the dashed circle labeledD contains the diagramD. This diagram superimposes the 6j symbol fort′
and the diagramD. By (104), overcrossings of the line labeledi over lines inD correspond to half-braidings
σ±1
i,a, while overcrossings of lines inD overj correspond to associators inC. The line labeledi describes the
functor i⊗− :C→C and the line labeledj the functor−⊗ j :C→C . Identities(39) to (43) allow one to
separate the two diagrams and yield the result.
Example 6.5 shows that ribbon invariants can be realised as line and point defects on a trivial defect plane.
However, this involves ribbon diagrams rather than ribbons in three-dimensional space, and the braidings are
external input, namely defect data labeling vertices. We now show how ribbon invariants are obtained from
line defects in a 3-ball that are not confined to a plane and where the braidings arise from the state sum.
Example 6.6. LetC be spherical fusion category as a(C,C)-bimodule category andF =a⊗− :C→C and
G =b⊗− :C→C the bimodule functors for(a,σ−,a), (b,σ−,b)∈ ObZ(C) with coherence data as in(104).
We consider the following three tetrahedra labeled with objects inIC:
p q
m n
j
F
i k
p q
m n
j
p q
m n
l
G
k
59
Glue the first tetrahedron to the second along the two faces labeled withj,m,n and j,p,q and the second
to the third along the two faces labeled withk,m,p and k,n,q . This yields a triangulated 3-ballM with a
one-holed torus as a trivial defect surface. Then the rescaled state sumZ′(M,l∂M,b∂M ) is the 6j symbol of
the tetrahedron
p q
m n
l
G
F
i
=
b
p
p
lq
n
m
ia
ν
µ
β
δ
where the crossing of the lines labeledF and G on the defect surface is assigned the(C,C)-bimodule natural
transformationν =σ−1
a,b⊗− : (b⊗a)▷−⇒ (a⊗b)▷−.
Proof. The polygon diagram and the associated 6j symbols for the first tetrahedron are given by
q
nm
p
j
i
F
α
β
γ
δ
p
p
j
iF
q
n
m
α
β
γ
δ
p
p
q
j
n
ia
m
α
β
γ
δ
where the first diagram for the 6j symbol is in the diagrammatic notation of the previous sections and the
second the usual diagram for a spherical fusion category as in [TV92, BW96], with the objects fromZ(C)
highlighted in colour. It is obtained from the second diagram by inserting the functor−⊗ j :C→C for the
line labeledj and the functorF (i⊗− ) =a⊗ (i⊗− ) :C→C for the lines withF and i.
The polygon diagram and 6j symbols for the second tetrahedron are given by
m
nq
p
j
k
ρ
γ
τ
α
p
p
j
k
m
n
q
ρ
γ
τ
α
p
p
m
k
n
j
q
ρ
γ
τ
α
Note that here the polygon diagram is viewed from the back, not the front, since the trivial defect plane is
oriented in the opposite direction. Again, the second diagram for the 6j symbol is the standard diagram for a
spherical fusion category obtained by inserting the functorsk⊗− :C→C and−⊗ j :C→C for the black
line labeledk and the grey line labeledj in the second diagram.
60
The polygon diagram and the 6j symbols for the third tetrahedron are given by
q
nm
p
lG
k
ν
τ
µ
ρ
p
p
G l
k
q
n
m
ν
τ
µ
ρ
b
p
p
q l
n
k
m
ν
τ
µ
ρ
Here, the second 6j symbol is obtained from the first by inserting the functork⊗− :C→C for the black line
labeled k and the functorG(−⊗ l) =b⊗ (−⊗ l) :C→C for the lines labeledG and l. The crossing in the
second 6j symbol stands for the morphismσ−1
k,b :b⊗k→k⊗b associated withb.
The rescaled state sum is obtained by multiplying the three 6j symbols and the dimensions of the internal
edges, summing over the labelsj,k∈IC and over the morphismsα,γ,ρ,τ assigned to the glued faces
Z′(M,l∂M,b∂M ) =∑
j,k
α,γ,ρ,τ
dim(j) dim(k)
p
p
q
j
n
ia
m
α
β
γ
δ
p
p
m
k
n
j
q
ρ
γ
τ
α
b
p
p
q l
n
k
m
ν
τ
µ
ρ
To compute this state sum we first use(66) to glue the polygon diagrams along the faces labeled by the
objects k,m,p and q,j,p and the morphismsρ and α. We then simplify the resulting expressions with(64)
and apply (2) together with the naturality of the half-braiding. This gives
b
Z′(M,l∂M,b∂M )
(66)
= ∑
j,k
γ,τ
dim(j)
dim(k)
p
p
q l
n
k
m
n
q j
n
m
ia
ν
τ
µ
τ
γ
β
γ
δ
b
(64)
= ∑
k,τ dim(k)
p
p
q l
n
k
mq
i
n
a
ν
τ
µ
τ
β
δ
b
(2)
= ∑
k,τ dim(k)
p
p
q
l
n
k
mq
i
n
a
ν
τ
µ
τ
β
δ
61
Applying again identities (64) and (2) together with the naturality of the half-braiding yields
Z′(M,l∂M,b∂M )
(64)
=
b
p
p
lq
m
n
ia
ν
µ
β
δ
(2)
=
b
p
p
lq
n
m
ia
ν
µ
β
δ
Example 6.6 allows one to construct any ribbon link invariant for the centreZ(C) of a spherical fusion
categoryC from state sums that involve only defect surfaces and defect lines. This is achieved by considering
a ribbon diagram and realising each crossing as in Example 6.6.
Example 6.7. LetC be a spherical fusion category with centerZ(C) and L a ribbon link whose connected
components are labeled by objects ofZ(C). LetM be the following triangulated 3-manifold with defect data:
1. Realise a ribbon diagramDL for L as a PL diagram that is the horizontal and vertical composite of the
following squares and the ones obtained by rotating them, reversing orientation in the third square and
replacing an over- by an undercrossing in the last square
a a
b
a
2. Assign to a dashed line with label(a,σ−,a) inZ(C) the (C,C)-bimodule functorFa =a⊗− :C→C with
coherence data as in(104), to a crossing with labelsa,b the bimodule natural transformation given by
σ±1
a,b, as in Example 6.6, and to the midpoint of the second and third diagram either the identity or the
(co)units of the adjunctionFl
a⊣Fa.
3. Draw solid vertical and horizontal lines in each square that connect the midpoints of the boundary edges
and end to the left of the dashed lines, viewed in the direction of their orientation. Let the vertical line
cross under and the horizontal line over all other lines of the diagram.
4. Label each vertex of the square and each solid line by a simple object ofC, such that the labels match at
the vertices and edges where the squares are glued to form the diagramDL. Label each endpoint of lines
at the boundary by a morphism in the appropriate morphism space inC
q
nm
p
j
i
α
β
γ
δ
q
nm
p
j
i
a
α
β
γ
δ
q
nm
p
j
i
a
α
β
γ
δ
b
q
nm
p
j
i
a
α
β
γ
δ
5. Assign to each square in 4. a defect tetrahedron for the(C,C)-bimodule categoryC whose 6j symbol is
the polygon diagram in 4. , as in Figure 13. Construct the last defect tetrahedron in Figure 13 as in
Example 6.6 by gluing three tetrahedra with defect planes without crossings.
62
6. The polygon diagrams glue to a diagram that superimposesDL with additional edges labeled by objects
ofC, whose endpoints are labeled by morphisms inC. This defines a gluing pattern for the associated
tetrahedra, as in Figure 14, that yields a triangulated 3-ballM with a ribbon linkL′ in the interior.
The state sum ofM is
Z(M,l∂M,b∂M ) = ev(DL)·Z (M′,l∂M,b∂M ),
whereZ(M′,l∂M,b∂M ) is the state sum of the 3-ballM′ with the same labels, but without defects.
Proof. As the dimension factors for boundary edges and vertices coincide forM and M′, it is sufficient to
consider the rescaled state sums. By Proposition 5.11 and Example 6.6, the rescaled state sum forM is the
evaluation of the polygon diagram obtained by gluing all defect squares. This is the ribbon diagramDL,
superimposed with a graph labeled byC, which is the dual of the triangulation on∂M.
The evaluation of this polygon diagram is computed as in Example 6.5. By(104) overcrossings of solid
lines over lines inT correspond to half-braidings of objects ofZ(C) with objects inC, while undercrossings
correspond to associators inC. As all vertices involve only solid lines, one can use identities(39) to (43) to
separate the graph labeled byC and the diagramDL. This yields the product of the rescaled state sum
Z′(M′,l∂M,b∂M ) and the evaluation ofDL.
Example 6.7 constructs a specific example of a triangulated 3-ball with a ribbon link as a defect. An analogous
factorisation of the state sum is obtained for any ribbon link labeled byZ(C) in any triangulated 3-ball
labeled byC. This follows from the triangulation independence of the state sum and the fact that it is
invariant under∆-moves, which encode ambient isotopies of ribbon links.
Proposition 6.8. LetM be a triangulated 3-ball labeled by a spherical fusion categoryC. LetL be a ribbon
link in the interior ofM that is blackboard-framed with respect to a disc bisectingM and labeled byZ(C).
Then the state sum is given by
Z(M,l∂M,b∂M ) =Z(M′,l∂M,b∂M )· ev(DL),
whereZ(M′,l∂M,b∂M ) is the state sum of the 3-ballM′ with the same labels, but without the link, andDL a
ribbon diagram obtained by projectingL on the disc.
Proof. 1. We first show that the state sum is invariant under PL ambient isotopy of the ribbon link. By a
result of Graeub [G], see also Burde and Zieschang [BZ, Prop. 1.10] and Yetter [Y, Sec. 2.2], two PL links in
a 3-ball are ambient isotopic iff they are related by a finite sequence of∆-moves. A ∆-move places a triangle
on the link that intersects it only in one side and replaces this side by the other two sides of the triangle.
∆
An analogous result holds for ambient isotopies of blackboard-framed ribbon links if one restricts attention to
∆-moves that respect the framing, that is, keep the links blackboard framed and can be realised without
introducing kinks, see for instance [Y, Sec. 2.2]. Thus it is sufficient to show that the state sum is invariant
under ∆-moves that respect the blackboard framing ofL.
Consider a blackboard framed∆-move with a triangle∆. By Corollary 5.13 and Lemma 5.7, suppose without
loss of generality that the tetrahedra intersecting∆ form a fine neighbourhood of∆ and that gluing all
tetrahedra that intersect∆ yields a triangulated 3-ballB bisected by a defect plane that extends∆.
By Proposition 5.11 the state sums forB before and after the∆-move are obtained by projecting the dual of
its boundary triangulation on the defect plane and evaluating the resulting polygon diagram. This yields
ribbon diagrams that superimpose a ribbon segment labeled byZ(C) with the boundary diagrams labeled by
C. The polygon diagrams before and after the∆-move are related by a∆-move on the ribbon segment in the
polygon. Identities (39) to (42) imply that the evaluations of these polygon diagrams are equal. AsM\B is
not affected by the∆-move, the state sum ofM is invariant under the∆-move by Corollary 4.10.
63
p q
m n
j
i
q
nm
p
j
i
α
β
γ
δ
p q
m n
j
Fa
i
q
nm
p
j
i
a
α
β
γ
δ
p q
m n
j
Fa
i
q
nm
p
j
i
a
α
β
γ
δ
p q
m n
j
Fb
Fa
i b
q
nm
p
j
i
a
α
β
γ
δ
Figure 13: Defect tetrahedra assigned to the square diagrams from Example 6.7. The last tetrahedron is
obtained by gluing three tetrahedra without crossings as in Example 6.6.
64
p
m n
q
b
a
i
j
q
n s
r
c
a
i
j′
m
k l
n
b
d
i′
j
n
l t
s
c
d
i′
j′
p
k t
rq
s
l
m
d
a
cb
i
i′
j j′
Figure 14: Gluing four defect tetrahedra and the associated polygon diagram.
2. By applying 2d isotopies to the ribbon diagramDL, one can transform it into a diagramD′ as in Example
6.7 and construct a triangulated 3-ballN with a ribbon linkL′ in the interior that projects toD′ =DL′. By
Example 6.7 one hasZ(N,l∂N,b∂N ) =Z(N′,l∂N,b∂N )· ev(DL′), whereN′ is the 3-ball withoutL′.
As the boundary triangulations ofM and N are related by elementary shellings and inverse shellings with
tetrahedra that do not intersectL and L′, it is sufficient to show thatZ(M,l∂M,b∂M ) =Z(N,l∂N,b∂N ), if
the labeled boundary triangulations forM and N agree. As the link diagramsDL and DL′ are isotopic, one
has ev(DL) = ev(DL′) and the linksL and L′ that project toDL and DL′ are ambient isotopic. This allows
one to transformL intoL′ by a finite sequence of∆-moves. The first part of the proof implies that this does
not affect the state sum. By the triangulation independence of the usual Turaev-Viro-Barrett-Westbury state
sum, one hasZ(M′,l∂M,b∂M ) =Z(N′,l∂N,b∂N ), and with Theorem 5.16 this yields
Z(M,l∂M,b∂M )
1.
=Z(N,l∂N,b∂N )
6.7
= ev(DL′)·Z (N′,l∂N,b∂N )
5.16
= ev( DL)·Z (M′,l∂M,b∂M ).
Proposition 6.8 can be generalised to ribbon tangles realised as defect graphs on trivial defect surfaces. One
can also generalise it to ribbon links embedded in more general 3-manifolds. Embedding a ribbon linkL
labeled byZ(C) in a single tetrahedron labeled byC and gluing it to the tetrahedron with the opposite
orientation along all four faces yields the state sum for a 3-sphereL in the interior
Z(S3,L ) = ev(DL)
dimC .
This coincides with Turaev and Virelizier’s state sum graph TQFT for a 3-sphere containing a ribbon link
in [TV17, Th. 16.1]. In fact, we expect that our state sums with defect lines and vertices on trivial defect
surfaces always coincide with the corresponding graph TQFTs with ribbons from [TV17, Ch. 16] and [TV10].
It would be nice to show this in full generality and to compare with the results by Balsam and Kirillov in
[KB10, B10] that also involve ribbons labeled byZ(C).
We also expect that our state sum is related to the modular functor constructed from bimodule categories
over finite tensor categories by Fuchs et al. [FSS19] if one restricts the latter to our categorical data. However,
is not clear to us how our construction is related to the work [LY20] by Lee and Yetter, which also constructs
65
triangulation independent state sums with defect surfaces. However, the defect surfaces in [LY20] are labeled
with different categorical data, namely bicategories equipped with spherical duals and certain 2-functors.
They should be thought of as defects with additional structure, according to the authors. We believe that
this is a different type of defect that cannot be related directly to our construction.
The examples in this section show that the state sum models with defects give relevant information about
defect surfaces and are easy to compute for simple categorical data. It would be feasible to investigate further
examples that involve defect lines and points on non-trivial defect surfaces, at least for spherical fusion
categoriesC = VecG andD = VecG′ and bimodule categories defined by finite transitiveG×G′op-sets. In
this case, the categorical defect data for defect lines and defect points can be worked out explicitly to describe
defects of all codimensions for Dijkgraaf-Witten theory [DW90]. It would also be interesting to investigate
knotted defect surfaces beyond the torus and with less trivial categorical data.
With the results by Balsam and Kirillov [BK12, Kr11] on the relation between Turaev-Viro-Barrett-Westbury
state sums, Levin-Wen models [LW05] and Kitaev’s quantum double models [Ki03], it should also be possible
to apply our state sums with defects to those models and to make contact with the work [KK12] by Kitaev
and Kong. In the long run it would be desirable to determine if our state sum model with defects defines a
defect TQFT in the sense of the works [CMS20, CRS19] by Carqueville et al. and to relate it to the works
[CRS18, KMRS21] by Carqueville et al. and by Koppen et al. on defects and domain walls in the context of
Reshetikhin-Turaev TQFTs. We leave these questions for future work.
Acknowledgements
This article originated from discussions with John W. Barrett. We had originally planned to work on this
project together, but this became impossible due to the Covid-19 pandemic and its impact on research and
teaching. I am extremely grateful to him for helpful discussions, encouragement and comments on drafts of
this article. I am also grateful to Gregor Schaumann for remarks and discussions on bimodule categories and
bimodule traces, to Andreas Knauf for discussions and comments on drafts of this article and to the referee
for helpful comments and suggestions.
References
[AC93] Daniel Altschuler and Antoine Coste. Invariants of three-manifolds from finite group cohomology.
Journal of Geometry and Physics, 11(1):191– 203, 1993.
[B10] Balsam, B. (2010). Turaev-Viro invariants as an extended TQFT III. arXiv preprint
arXiv:1012.0560.
[BK12] Balsam, B., & Kirillov Jr, A. (2012). Kitaev’s lattice model and Turaev-Viro TQFTs. arXiv
preprint arXiv:1206.2308.
[BMG07] Barrett, J. W., Faria Martins, J., & García-Islas, J. M. (2007). Observables in the Turaev-Viro
and Crane-Yetter models. Journal of Mathematical Physics, 48(9), 093508.
[BMS12] Barrett, J. W., Meusburger, C., & Schaumann, G. (2012). Gray categories with duals and their
diagrams. arXiv preprint arXiv:1211.0529.
[BW96] Barrett, J., & Westbury, B. (1996). Invariants of piecewise-linear 3-manifolds. Transactions of the
American Mathematical Society, 348(10), 3997-4022.
[BZ] Burde, G., & Zieschang, H. (2008, August). Knots. In Knots. de Gruyter.
[CMS20] Carqueville, N., Meusburger, C., & Schaumann, G. (2020). 3-dimensional defect TQFTs and their
tricategories. Advances in Mathematics, 364, 107024.
[CRS18] Carqueville, N., Runkel, I., & Schaumann, G. (2018). Line and surface defects in Reshetikhin-
Turaev TQFT. Quantum Topology, 10(3), 399-439.
[CRS19] Carqueville, N., Runkel, I., & Schaumann, G. (2019). Orbifolds of n-dimensional defect TQFTs.
Geometry & Topology, 23(2), 781-864.
[C95] Casali, M. R.(1995). Anote about bistellar operations onPL-manifoldswith boundary. Geometriae
Dedicata, 56(3), 257-262.
[DSS20] Douglas, C., Schommer-Pries, C., & Snyder, N. (2020). Dualizable tensor categories (Vol. 268,
No. 1308). American Mathematical Society.
66
[DW90] Dijkgraaf, R., & Witten, E. (1990). Topological gauge theories and group cohomology. Communi-
cations in Mathematical Physics, 129(2), 393-429.
[EGNO] Etingof, P., Gelaki, S., Nikshych, D., & Ostrik, V. (2016). Tensor categories (Vol. 205). American
Mathematical Soc.
[ENO05] Etingof, P., Nikshych, D., & Ostrik, V. (2005). On fusion categories. Annals of Mathematics,
581-642.
[E66] Epstein, D. B. (1966). Curves on 2-manifolds and isotopies. Acta Mathematica, 115, 83-107.
[FSS19] Fuchs, J., Schaumann, G., & Schweigert, C. (2019). A modular functor from state sums for finite
tensor categories and their bimodules. arXiv preprint arXiv:1911.06214.
[G] Graeub, W. (1950). Die semilinearen Abbildungen. In Die semilinearen Abbildungen (pp. 3–70).
Springer, Berlin, Heidelberg.
[JS91] Joyal, A., & Street, R. (1991). The geometry of tensor calculus, I. Advances in mathematics,
88(1), 55-112.
[KS93] Karowski, M., & Schrader, R. (1993). A combinatorial approach to topological quantum field
theories and invariants of graphs. Communications in mathematical physics, 151(2), 355-402.
[KB10] Kirillov Jr, A., & Balsam, B. (2010). Turaev-Viro invariants as an extended TQFT. arXiv preprint
arXiv:1004.1533
[Kr11] Kirillov Jr, A. (2011). String-net model of Turaev-Viro invariants. arXiv preprint arXiv:1106.6033.
[Ki03] Kitaev, A. Y. (2003). Fault-tolerant quantum computation by anyons. Annals of Physics, 303(1),
2-30.
[KK12] Kitaev, A., & Kong, L. (2012). Models for gapped boundaries and domain walls. Communications
in Mathematical Physics, 313(2), 351-373.
[KMRS21] Koppen, V., Mulevicius, V., Runkel, I., & Schweigert, C. (2021). Domain walls between 3d phases
of Reshetikhin-Turaev TQFTs. arXiv preprint arXiv:2105.04613.
[L] Lee, J. (2010). Introduction to topological manifolds (Vol. 202). Springer Science & Business
Media.
[LY20] Lee, I. J., & Yetter, D. N. (2020). Bicategories for TQFTs with Defects with Structure. arXiv
preprint arXiv:2003.06538.
[Li99] Lickorish, W. B. R. (1999). Simplicial moves on complexes and manifolds. Geometry and Topology
Monographs, 2(299-320), 314.
[LW05] Levin, M. A., & Wen, X. G. (2005). String-net condensation: A physical mechanism for topological
phases. Physical Review B, 71(4), 045110.
[Mu03] Mueger, M. From subfactors to categories and topology. I: Frobenius algebras in and Morita
equivalence of tensor categories. J. Pure Appl. Algebra, 180(1-2):81–157, 2003.
[P91] Pachner, U. (1991). PL homeomorphic manifolds are equivalent by elementary shellings. European
journal of Combinatorics, 12(2), 129-145.
[P90] Pachner, U. (1990). Shellings of simplicial balls and pl manifolds with boundary. Discrete
mathematics, 81(1), 37-47.
[RS] Rourke, C. P., & Sanderson, B. J. (2012). Introduction to piecewise-linear topology. Springer
Science & Business Media.
[Sa57] Sanderson, D. E. (1957). Isotopy in 3-Manifolds I. Isotopic Deformations of 2-Cells and 3-Cells.
Proceedings of the American Mathematical Society, 8(5), 912-922.
[S13] Schaumann, G. (2013). Traces on module categories over fusion categories. Journal of Algebra,
379, 382-425.
[S15] Schaumann, G. (2015). Pivotal tricategories and a categorification of inner-product modules.
Algebras and Representation Theory, 18(6), 1407-1479.
[ST] Birman, J. S., & Eisner, J. (1980). Seifert and Threlfall, A Textbook of Topology. Academic Press.
[T] Turaev, V. G. (2020). Quantum invariants of knots and 3-manifolds (Vol. 18). Walter de Gruyter
GmbH & Co KG.
[TV10] Turaev, V., & Virelizier, A. (2010). On two approaches to 3-dimensional TQFTs. arXiv preprint
arXiv:1006.3501.
[TV17] Turaev, V., & Virelizier, A. (2017). Monoidal categories and topological field theory (Vol. 322, pp.
xii+-523). Basel: Birkhäuser.
67
[TV92] Turaev, V. G., & Viro, O. Y. (1992). State sum invariants of 3-manifolds and quantum 6j-symbols.
Topology, 31(4), 865-902.
[Y] Yetter, D. N. (2001). Functorial Knot Theory: Categories of Tangles, Coherence, Categorical
Deformations and Topological Invariants (Vol. 26). World Scientific.
[Ze60] Zeeman, E. C. (1960). Unknotting spheres. Annals of Mathematics, 350-361.
[Zi98] Ziegler, G. M. (1998). Shelling polyhedral 3-balls and 4-polytopes. Discrete & Computational
Geometry, 19(2), 159-174.
68
