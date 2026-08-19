---
doc_id: arxiv-1012.1039v2
doc_title: "where vn is the volume of a regular ideal hyperbolic n–simplex. This result gener- alizes the fact that hyperbolic Dehn ﬁlling of a 3–manifold d oes not increase hyperbolic volume"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
Simplicial volume was deﬁned for manifolds by Gromov in [Gro82]. For an
n-dimensional closed manifold M of constant sectional curvature K = −1, the
simplicial volume ‖M ‖ is proportional to the (Riemannian) volume Vol( M ), and
the ratio is the volume of a regular ideal hyperbolic n–simplex; in particular, it
depends only on the dimension [Gro82, 0.4]. More generally, [Gro82, 0.3 ,0.5], for
constantsa ≤b< 0, there is a constant C =C(a,b,n )> 1 so that if the sectional
curvaturesK satisfy a ≤K ≤b, then
(1) Vol( M )/C ≤ ‖M ‖ ≤ CVol(M ).
This note is motivated in part by the (apparently open) question:
Question 1.1. Fixv >0, and let Mn,v be the set of (homotopy classes of ) closed n-
manifolds whose sectional curvatures are all negative, and whose simplicial volume
is bounded above by v. Is Mn,v ﬁnite whenever n ≥ 4?
Some comments, ﬁxing n ≥ 4 and v >0:
• The set Mn,v contains only ﬁnitely many constant curvature manifolds,
even up to diﬀeomorphism. This follows from Wang’s ﬁniteness theore m
[Wan72] together with the proportionality of simplicial volume to hype r-
bolic volume for closed manifolds (see, e.g., [BP92, C.4]).
• Fixb> 0. The set Mn,v contains only ﬁnitely many diﬀeomorphism classes
of manifolds with sectional curvaturesK pinched between −1 andb. Indeed,
as noted in the inequality (1), the curvature assumption −1 ≤K ≤b <0
Koji Fujiwara is supported in part by a Grant-in-Aid for Scie ntiﬁc Research (No. 19340013).
Jason Manning is supported in part by NSF grant DMS-0804369.
1
2 K. FUJIW ARA AND J. F. MANNING
together with an upper bound on the simplicial volume gives an upper
bound on the volume [Gro82, 0.3, 1.2]. On the other hand, the conditio n
−1 ≤K <0 together with the upper bound on the volume gives an upper
bound on the diameter [Gro78, 1.2] and a lower bound on the volume
[Gro78, 1.3 A]. Now, Cheeger’s ﬁniteness theorem applies [Gro78, 1.4].
Thus if there are inﬁnitely many diﬀeomorphism types of closed n–
manifolds of bounded volume, with sectional curvatures ≤ − 1, there can-
not be any uniform lower bound on their sectional curvatures, so lo ng
as n ≥ 4. So a negative answer to Question 1.1 would have to involve
manifolds without uniformly pinched curvature. For n >3 there do exist
sequences of negatively curved manifolds whose curvatures cann ot be uni-
formly pinched. Gromov–Thurston [GT87, 0.5] describe a sequence {Vi}
of negatively curved closed manifolds which are i-fold ramiﬁed covers of
a ﬁxed closed manifold V of constant negative curvature, and show the
curvatures of the Vi cannot be uniformly pinched. We remark that such a
sequence of ramiﬁed covers Vi must satisfy 0 <i ‖V ‖ ≤ ‖Vi‖, so it does not
imply a negative answer to Question 1.1.
• The sets M3,v are inﬁnite for large enough v, even if one restricts to con-
stant curvature. This is because of Thurston’s hyperbolic Dehn su rgery
theorem, and Thurston’s theorem (which we generalize in this note) that
volume decreases under hyperbolic Dehn ﬁlling.
It is easy to extend the deﬁnition of simplicial volume to closed pseudo manifolds.
This is explained in Section 2 (cf. [Yam97]). Pseudomanifold versions of the bounds
in (1) have been established by Yamaguchi [Yam97, Theorem 0.2 and 0 .5] as follows.
First, if X is an orientable n-dimensional, compact, geodesically complete (locally)
CAT(−1) pseudo-manifold, then
(2) Vol( X) ≤ π
(n − 1)! ‖X‖.
Yamaguchi conjectures that the factor of π
(n−1)! in (2) can be replaced by the volume
of a regular ideal hyperbolic n–simplex. Second, if X is an n-dimensional compact
orientable geodesic space without boundary such that K ≥ − 1 in the sense of
Alexandrov and X is “locally Lipschitz contractible”, then
‖X‖ ≤ n!(n − 1)nVol(X),
where Vol(X) is the n-dimensional Hausdorﬀ measure of X. Both bounds cannot
be applied at once except in the manifold setting, since upper and lowe r curvature
bounds can only coexist in a manifold. We do not use either bound in this paper,
except in Remark 1.11 below.
We do not answer Question 1.1, but we answer the analogous questio n for neg-
atively curved pseudomanifolds:
Question 1.2. Letn ≥ 4. Fix v >0, and let Pn,v be the set of (homotopy classes
of ) closed locally CAT (−1) n–pseudomanifolds whose simplicial volume is bounded
above by v. Is Pn,v ﬁnite?
Speciﬁcally, we apply a “Dehn ﬁlling” construction to give a negative an swer to
Question 1.2.
LetM be a compact n–manifold with boundary a union of m tori, whose interior
V = Int(M ) admits a complete hyperbolic metric of ﬁnite volume. Let
M ∼
= M
SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS 3
be a compact manifold obtained from V by removing horospherical neighborhoods
of the cusps. The manifold M has m boundary components N1,...,N m, each of
which inherits a ﬂat metric from the hyperbolic metric on Int( M ). In [FM10], we
deﬁned and studied ﬁllings of M , which are topological spaces obtained by gluing
the product of a torus with the cone on another torus to each bou ndary component
of M . Here is an equivalent deﬁnition.
Deﬁnition 1.3. For eachi ∈ {1,...,m }, let Ti<N i be a ki–dimensional subman-
ifold which is totally geodesic in Ni. The ( n − 1)–torus Ni is foliated by parallel
copies of Ti, with leaf space Vi homeomorphic to an (n − 1 −ki)–dimensional torus.
Lethi : Ni →Vi be the quotient map, and deﬁne M (T1,...,T m) to be the quotient
M/ ∼, where x ∼ x′ if hi(x) = hi(x′) for some i. The space M (T1,...,T m) is
called a ﬁlling of M . If all of the tori Ti have injectivity radius strictly larger than
π, M (T1,...,T m) is called a 2 π–ﬁlling of M .
In caseM is 3–dimensional, and eachTi is one-dimensional, ﬁllings M (T1,...,T m)
are the same as ordinary Dehn ﬁllings of M . In [FM10], we generalize work in
[BH96, Sch89, MS97] (including the Gromov-Thurston 2 π Theorem) to prove:
Theorem 1.4. [FM10] LetM be an n–dimensional hyperbolic manifold as above.
Every 2π–ﬁlling M (T1,...,T m) of M admits a locally CAT (0) metric, so the uni-
versal cover is CAT (0) with isolated ﬂats. If every Ti has dimension at least n − 2,
then M (T1,...,T m) admits a locally CAT (−1) metric.
Each ﬁlling of M is a closed pseudomanifold with singular set equal to a disjoint
union of tori of dimensions n − (1 + dim(T1)),...n − (1 + dim(Tm)) (see Deﬁnition
2.1 for these terms). In particular, its simplicial volume is well-deﬁned [Yam97].
The main result of the current paper is that these ﬁllings have positiv e simplicial
volume, bounded above by the simplicial volume of M .
Theorem 1.5. LetM be a compact n–manifold with boundary a union of (n − 1)–
tori, and suppose that V = Int(M ) admits a complete hyperbolic metric of ﬁnite
volume Vol(V ). Let M (T1,...,T m) be a 2π–ﬁlling of Int(M ). Then
0< ‖M (T1,...,T m)‖ ≤ Vol(V )
vn
,
wherevn is the volume of a regular ideal hyperbolic n-simplex.
Corollary 1.6. The answer to Question 1.2 is “no,” for v equal to the volume of
any hyperbolic n–manifold with torus cusps.
Proof. LetM ,M ,N1,...,N m be as in the discussion preceding Deﬁnition 1.3. For
each j ∈ { 1,...,m }, choose a sequence {T j
i }i∈N of totally geodesic codimension
1 tori in Nj, all with inj > π, and so that lim i→∞ inj(T j
i ) = ∞. Let Mi be the
ﬁllingM (T 1
i,...,T m
i ). Proposition 2.12 of [FM10] implies that for any i only ﬁnitely
manyMj have fundamental group isomorphic to π1Mi, so the set {Mi}i∈N contains
inﬁnitely many homotopy classes. Theorem 1.4 implies that 0 < ‖Mi‖ ≤ Vol(V )
vn
for
all i. □
Remark 1.7. In [RT05], Ratcliﬀe and Tschantz describe some nonpositively curve d
4–dimensional homology spheres. These homology spheres are obt ained by 2 π–
ﬁlling of a cusped hyperbolic manifold described by Ivanˇ si´ c in [Iva04 ]. They seem
to be the ﬁrst exmples of 4–dimensional homology spheres with Riema nnian metrics
4 K. FUJIW ARA AND J. F. MANNING
of non-positive sectional curvature (see the paragraph after R emark 5 in [NW00]).
Belegradek in [Bel06] asked if these homology spheres have positive s implicial vol-
ume. Our main theorem answers this question aﬃrmatively, but the m ain part
of our argument is to do with the upper bound on simplicial volume. The reader
primarily interested in positivity of simplicial volume can stop with Subse ction 2.1.
In particular, we answer Belegradek’s question with Corollary 2.5 at t he end of that
subsection.
It would be interesting to get some further information on the poss ible volumes
of ﬁllings of M . Hyperbolic Dehn ﬁlling of a 3–manifold strictly decreases volume,
and the volume diﬀerence goes to zero as the length of the ﬁlling slope goes to
inﬁnity (see [Thu80, 6.5.6] for strictness and [NZ85, HK05a, FKP08 ] for estimates
of the diﬀerence). We conjecture that similar phenomena hold in high er dimensions.
Conjecture 1.8. The volumes ‖M (T1,...,T m)‖ accumulate on Vol(V )
vn
but do not
attain it.
Question 1.9. Letǫ> 0. Is there some R so that if every torus Ti has injectivity
radius bigger than R, then
Vol(V )
vn
−ǫ< ‖M (T1,...,T m)‖< Vol(V )
vn
?
Question 1.10. Consider the set of fundamental groups of 2π–ﬁllings of M as a
subspace of the space of “marked groups” generated by some ﬁx ed set of generators
of π1M . Is the simplicial volume a continuous function on this spac e?
Remark 1.11. It is possible to analyze the metrics constructed in [FM10] and
apply Yamaguchi’s inequality (2) to deduce that the CAT( −1) ﬁllings of a ﬁxed M
have simplicial volume bounded away from zero, but this is about all we know for
certain.
