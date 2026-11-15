---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Introduction
Let T := (R2∖Z2)/Z2 be the once-punctured torus endowed with its differential
structure and an orientation. The group G of isotopy classes of orientation-preserving
diffeomorphisms ϕ: T →T (or the mapping class group of T) is identiﬁed as
G ≃SL2(Z), so each such map ϕ has well-deﬁned eigenvalues in C. For [ϕ] in G,
deﬁne the punctured torus bundle
Vϕ := T × [0, 1]/ ∼
where ∼identiﬁes (x, 0) with (ϕ(x), 1) for all x in T. Then Vϕ is a differentiable
oriented 3–manifold, well-deﬁned up to diffeomorphism. Thurston’s Hyperbolization
Theorem [21] implies the following theorem as a very special case.
Theorem 1.1 If ϕ has two distinct real eigenvalues, the punctured torus bundle Vϕ
admits a ﬁnite-volume, complete hyperbolic metric.
The aim of this paper is to prove Theorem 1.1 by elementary and, to some extent,
constructive arguments. The strategy is to exhibit a canonical, geodesic triangulation H
of Vϕ into ideal tetrahedra (hyperbolic tetrahedra whose vertices are at inﬁnity).
Combinatorially, H (sometimes called the Floyd–Hatcher or monodromy triangulation)
is found by expressing a certain conjugate of ±ϕ as a product of positive transvection
matrices. Once such combinatorial data for a triangulation is given, the problem of
Published: 16 September 2006
DOI: 10.2140/gt.2006.10.1239
1240
Franc¸ois Gu´eritaud and David Futer
making it hyperbolic lends itself to two approaches. One is complex, explicit and
“local”: cross-ratio computations, particular hyperbolic isometries, etc (see eg Neumann
and Zagier [20]). The other approach, ﬁrst described by Rivin [22], de Verdi`ere [25]
and Casson, is real-analytic and “global”: in order to make the structure complete, one
kills its monodromy by maximizing the total hyperbolic volume (but combinatorial
obstructions might arise). In the case of Vϕ, the combinatorial structure of H is
sufﬁciently well-understood to allow a nice interplay between the two approaches,
yielding useful “medium-range” results (Section 8). The philosophy of such results is
that if the structure with maximal volume is noncomplete, it should still be complete at
“most” places, enabling us to make geometric statements.
Akiyoshi [4], combining the methods of Akiyoshi, Sakuma, Wada and Yamashita [5]
and Minsky [18], proved that the “combinatorially canonical” triangulation H must
also be “geometrically canonical,” ie topologically dual to the Ford–Voronoi domain of
Vϕ. Lackenby [13], assuming the existence of the hyperbolic metric, derived the same
result by a normal surface argument. In [10], we apply the methods of the present paper
to extend the Akiyoshi–Lackenby theorem to quasifuchsian groups (where pleating
laminations of the convex core replace the attractive and repulsive laminations of the
monodromy ϕ).
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
{−1, 0, 1}, then [ϕ] has ﬁnite order and Vϕ is Seifert ﬁbered. If τ = ±2, then ϕ
preserves a nontrivial simple closed curve γ (parallel to a rational eigenvector) in the
punctured torus, and γ deﬁnes an incompressible torus or Klein bottle in Vϕ. In any
case we get a topological obstruction to the existence of the hyperbolic metric.
An attempt to be self-contained will be made in proving Theorem 1.1. The proof will
deal primarily with the case where the eigenvalues of ϕ are positive. The other case
is only a minor variant (in particular, V−ϕ can be obtained by ungluing the metric
tetrahedra of Vϕ and regluing them in a slightly different way).
Geometry & Topology 10 (2006)
Canonical triangulations
1241
Section 2 is standard and recalls the classiﬁcation of conjugacy classes in SL2(Z) in
order to deﬁne the triangulation H. The latter is studied in greater detail in Section 3
and Section 4. Positive angles for H (a “linear hyperbolic structure”) are provided
in Section 5. Section 6 explains the role played by hyperbolic volume maximization,
allowing us to deal with the easy cases in Section 7. Section 8 presents the essential
geometric lemma for the ﬁnal attack, carried out in Section 9. Section 10 is devoted
to a numerical example. In Section 11, we quickly recall the connection between
once-punctured tori and 4–punctured spheres. In the Appendix, David Futer builds on
that connection to prove an analogue of Theorem 1.1 for the complements of two-bridge
links and computes geometric estimates.
The symbol “=” is preceded (resp. followed) by a colon (:=, resp. =:) when the
equality serves as a deﬁnition for its left (resp. right) member.
I would like to thank Francis Bonahon and Fr´ed´eric Paulin for numerous insights and
the great improvements this paper owes to them. Exciting discussions with David Futer
and with Makoto Sakuma also gave invaluable input. This paper reached its pre-ﬁnal
form during a stay at the Institut Bernoulli (EPFL, Lausanne) for whose kind hospitality
I express my deep gratitude. Finally, thanks are due to the referee for many helpful
comments. This work was partially supported by NSF grant DMS-0103511.
2
