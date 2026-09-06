---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER — 26 sections: Introduction; The canonical triangulation; Diago"
---
Let T := (R2rZ2)/Z2 be the once-punctured torus endowed with its differential
structure and an orientation. The group G of isotopy classes of orientation-preserving
diffeomorphisms ϕ : T → T (or the mapping class group of T ) is identiﬁed as
G≃ SL2(Z), so each such map ϕ has well-deﬁned eigenvalues in C. For [ϕ] in G,
deﬁne the punctured torus bundle
Vϕ := T× [0, 1]/∼
where∼ identiﬁes ( x, 0) with (ϕ(x), 1) for all x in T . Then Vϕ is a differentiable
oriented 3–manifold, well-deﬁned up to diffeomorphism. Thurston’s Hyperbolization
Theorem [21] implies the following theorem as a very special case.
Theorem 1.1 If ϕ has two distinct real eigenvalues, the punctured torus bundle Vϕ
admits a ﬁnite-volume, complete hyperbolic metric.
The aim of this paper is to prove Theorem 1.1 by elementary and, to some extent,
constructive arguments. The strategy is to exhibit a canonical, geodesic triangulationH
of Vϕ into ideal tetrahedra (hyperbolic tetrahedra whose vertices are at inﬁnity).
Combinatorially,H (sometimes called the Floyd–Hatcher or monodromy triangulation)
is found by expressing a certain conjugate of±ϕ as a product of positive transvection
matrices. Once such combinatorial data for a triangulation is given, the problem of
Published: 16 September 2006 DOI: 10.2140/gt.2006.10.1239
1240 Franc ¸ois Gu´eritaud and David Futer
making it hyperbolic lends itself to two approaches. One is complex, explicit and
“local”: cross-ratio computations, particular hyperbolic isometries, etc (see eg Neumann
and Zagier [20]). The other approach, ﬁrst described by Rivin [ 22], de Verdi`ere [25]
and Casson, is real-analytic and “global”: in order to make the structure complete, one
kills its monodromy by maximizing the total hyperbolic volume (but combinatorial
obstructions might arise). In the case of Vϕ, the combinatorial structure of H is
sufﬁciently well-understood to allow a nice interplay between the two approaches,
yielding useful “medium-range” results (Section 8). The philosophy of such results is
that if the structure with maximal volume is noncomplete, it should still be complete at
“most” places, enabling us to make geometric statements.
Akiyoshi [4], combining the methods of Akiyoshi, Sakuma, Wada and Yamashita [5]
and Minsky [18], proved that the “combinatorially canonical” triangulationH must
also be “geometrically canonical,” ie topologically dual to the Ford–V oronoi domain of
Vϕ. Lackenby [13], assuming the existence of the hyperbolic metric, derived the same
result by a normal surface argument. In [10], we apply the methods of the present paper
to extend the Akiyoshi–Lackenby theorem to quasifuchsian groups (where pleating
laminations of the convex core replace the attractive and repulsive laminations of the
monodromyϕ).
Knowing the space of angle structures also allows for easy volume estimates, some of
which are worked out in the Appendix: these estimates make the constants of Brock [8]
explicit (and sharp) for the class of manifolds under consideration. Although the main
results of the present paper are known, our ambition is to demonstrate that hyperbolic
geometry and combinatorics (of the curve complex, say) can interact more intimately
than at the level of coarse geometry, a phenomenon which seems to extend beyond
punctured torus groups and begs to be further explored. Other references closely related
to this subject include the beautiful article of Akiyoshi, Sakuma, Wada and Yamashita
[6], which builds on the work of Jørgensen and partly motivated our work [10], and the
examples compiled in Alestalo and Helling [7], Helling [11] and Koch [12].
The converse of Theorem 1.1 is true. If the trace τ of the monodromy map ϕ is in
{−1, 0, 1}, then [ϕ] has ﬁnite order and Vϕ is Seifert ﬁbered. If τ =±2, then ϕ
preserves a nontrivial simple closed curveγ (parallel to a rational eigenvector) in the
punctured torus, andγ deﬁnes an incompressible torus or Klein bottle in Vϕ. In any
case we get a topological obstruction to the existence of the hyperbolic metric.
An attempt to be self-contained will be made in proving Theorem 1.1. The proof will
deal primarily with the case where the eigenvalues ofϕ are positive. The other case
is only a minor variant (in particular, V−ϕ can be obtained by ungluing the metric
tetrahedra of Vϕ and regluing them in a slightly different way).
Geometry &Topology 10 (2006)
Canonical triangulations 1241
Section 2 is standard and recalls the classiﬁcation of conjugacy classes in SL2(Z) in
order to deﬁne the triangulationH. The latter is studied in greater detail in Section 3
and Section 4. Positive angles for H (a “linear hyperbolic structure”) are provided
in Section 5. Section 6 explains the role played by hyperbolic volume maximization,
allowing us to deal with the easy cases in Section 7. Section 8 presents the essential
geometric lemma for the ﬁnal attack, carried out in Section 9. Section 10 is devoted
to a numerical example. In Section 11, we quickly recall the connection between
once-punctured tori and 4–punctured spheres. In the Appendix, David Futer builds on
that connection to prove an analogue of Theorem 1.1 for the complements of two-bridge
links and computes geometric estimates.
The symbol “ =” is preceded (resp. followed) by a colon (: =, resp. =:) when the
equality serves as a deﬁnition for its left (resp. right) member.
I would like to thank Francis Bonahon and Fr´ed´eric Paulin for numerous insights and
the great improvements this paper owes to them. Exciting discussions with David Futer
and with Makoto Sakuma also gave invaluable input. This paper reached its pre-ﬁnal
form during a stay at the Institut Bernoulli (EPFL, Lausanne) for whose kind hospitality
I express my deep gratitude. Finally, thanks are due to the referee for many helpful
comments. This work was partially supported by NSF grant DMS-0103511.
2 Conjugacy in SL2(Z) and the Farey tesselation
Proposition 2.1 Letϕ be an element of SL2(Z) with two distinct eigenvalues in R∗
+.
Then the conjugacy class ofϕ in SL2(Z) contains an element of the form
AϕA−1 =
(1 a1
0 1
)( 1 0
b1 1
) ( 1 a2
0 1
)( 1 0
b2 1
)
...
(1 an
0 1
)( 1 0
bn 1
)
where n> 0 and the ai and bi are positive integers. Moreover, the right hand side is
unique up to cyclic permutation of the factors
( 1 ai
0 1
)( 1 0
bi 1
)
. Conversely, any nonempty
product of such factors is an element of SL2(Z) with two distinct eigenvalues in R∗
+.
We sketch a proof of this popular fact, mainly in order to introduce thecyclic word Ω
associated to ϕ. The converse implication is easy (just check that the trace is larger
than 2), so we focus on the direct statement.
Consider the upper half-plane model of the hyperbolic plane H2, endowed with the
Farey tessellation F (the ideal triangle 01∞ iteratedly reﬂected in its sides). We identify
Geometry &Topology 10 (2006)
1242 Franc ¸ois Gu´eritaud and David Futer
PSL2(R) with the group of isometries of H2 via the isomorphism Ψ deﬁned by
Ψ
(a b
c d
)
: z↦→ dz + c
bz + a.
(Under this slightly unusual convention, the slopes of the eigenvectors of M are the
ﬁxed points of Ψ(M), rather than their inverses as would normally be the case.) It is
known that the group of orientation-preserving isometries of H2 preserving F is thus
identiﬁed with PSL 2(Z).
If D is the oriented hyperbolic line running from the repulsive ﬁxed point of±ϕ to the
attractive one, then D crosses inﬁnitely many Farey triangles (... t−1, t0, t1, t2,... ) of
F. We can formally write down a bi-inﬁnite word
Ω =... LRRRLLR...
where the k–th letter is R (resp. L) if D exits tk to the Right (resp. Left) of where it
enters. We will also say that D makes a Right (resp. Left) at tk . The word Ω contains at
least one R and one L, because the ends of D are distinct. The image of t0 underϕ is a
certain tm (m> 1), and Ω is periodic of period m.
Next, deﬁne the standard transvection matrices
R :=
(1 1
0 1
)
and L :=
(1 0
1 1
)
.
These are parabolic transformations of H2 whose respective ﬁxed points are 0 and
∞. Let M be any subword of Ω of length m: we see M as a product of standard
transvection matrices, and therefore as an element of SL2(Z). By studying the actions
of R and L on F, it is then easy to see thatϕ and M are conjugates in PSL2(Z), and
therefore in SL2(Z) since both have positive trace. This proves the existence statement
for the (ai, bi).
Uniqueness is checked as follows: on one hand, if ϕ andϕ′ are conjugates, a certain
element of PSL2(Z) (preserving F) takes the axis of ϕ to the axis of ϕ′, so they deﬁne
the same word Ω up to translation. On the other hand, looking at the actions of R and
L on H2, one sees that a product of standard transvection matrices (as in the statement
of Proposition 2.1) will deﬁne the word Ω = Ra1Lb1... RanLbn , concatenated inﬁnitely
many times with itself.
In the language of Proposition 2.1, the sequence (a1, b1,..., an, bn) can be shown to be
(a positive power of) the period of the continued fraction expansion of the slope of the
expanding eigenvector ofϕ. The word Ω will be seen either as inﬁnite periodic, or as
ﬁnite cyclic, depending on the context.
Geometry &Topology 10 (2006)
Canonical triangulations 1243
