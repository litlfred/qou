---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-013-nilpotent-slodowy-slices-and-collapsing-levels-f
section_title: "Nilpotent Slodowy slices and collapsing levels for W-algebras"
section_number: null
pages: 41-44
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Anne Moreau
(joint work with Tomoyuki Arakawa)
Let G be a complex connected simple algebraic group of adjoint type, with Lie
algebra g. The nilpotent Slodowy slice associated with a nilpotent orbit O in g and
an sl2-triple (e, h, f) of g is the intersection
SO,f := O ∩Sf,
where Sf ∼= f +ge is the Slodowy slice of the sl2-triple (e, h, f). Nilpotent Slodowy
slices associated with the principal nilpotent orbit Oprin and a subregular nilpotent
element fsubreg for the types A, D, E have a simple singularity of the same type
as G. More generally, the singularities of an arbitrary nilpotent Slodowy slices are
understood best for Gf a minimal degeneration of O [13, 14, 10].
In another direction, it is known that nilpotent Slodowy slices appear as associ-
ated varieties of W-algebras [2, 5], as we explain below. With every vertex algebra
V one associates a Poisson algebra RV , called the Zhu C2-algebra, as follows. Let
C2(V ) be the subspace of V spanned by the elements a(−2)b, where a, b ∈V , and
set RV = V/C2(V ). Here a(n), n ∈Z, stands for the Fourier mode of the ﬁeld
a(z) = P
n∈Z a(n)z−n−1 corresponding to a ∈V . Then RV has naturally a Pois-
son algebra structure and the associated variety of V is the aﬃne Poisson variety
XV := Specm RV .
The universal W-algebra associated with (g, f) at level k ∈C is
Wk(g, f) := H0
DS,f(V k(g)),
where H•
DS,f(?) is the BRST cohomology functor of the quantized Drinfeld-Sokolov
reduction associated with (g, f), [8, 11]. The associated variety XWk(g,f) is isomor-
phic to the Slodowy slice Sf, [9]. For any quotient V of the universal aﬃne vertex
algebra V k(g) associated with g at level k, H0
DS,f(V ) is a quotient of Wk(g, f)
provided that it is nonzero, and we have [2]: XH0
DS,f (V ) = XV ∩Sf, which is a
C∗-invariant subvariety of Sf.
In particular, if XLk(g) is the Zariski closure O of some nilpotent orbit O
in g, where Lk(g) is simple quotient vertex algebra of V k(g), and if f ∈O, then
XWk(g,f) ⊂SO,f (conjecturally, the equality holds), where Wk(g, f) is the simple
quotient vertex algebra of Wk(g, f). It is known that this occurs if k is an ad-
missible level1 by [2], or else if g belongs to the Deligne exceptional series and if
k = −h∨/6 −1 + n, where n ∈Z≥0 is such that k̸ ∈Z≥0 by [4].
Deﬁnition 1. Let g♮be the centralizer in g of the sl2-triple (e, h, f). We say
that the level k is collapsing if Wk(g, f) ∼= Lk♮(g♮), where k♮is a complex number
entirely determined by the level k and the reductive Lie algebra g♮. For example,
if Wk(g, f) ∼= C, then k is collapsing.
1A level k is admissible if Lk(g) is an admissible bg-module which happens if and only if
k = −h∨+ p/q, with p, q ∈Z>0, (p, q) = 1 and either (q, r∨) = 1 and p ≥h∨, or (q, r∨) = r∨
and p ≥h. Here r∨is the lacety of g, and h (resp. h∨) is its (resp. dual) Coxeter number [12].
3122
Oberwolfach Report 52/2018
The notion of collapsing levels goes back to Adamovi´c et al. [1]. There is a full
classiﬁcation of collapsing levels for the case where f = fmin is a minimal nilpotent
element2 [1], as well as of pairs (g, k) such that Wk(g, fmin) ∼= C, [4, 1].
Although the minimal nilpotent case is well-understood, little or almost nothing
is known for collapsing levels for non-minimal nilpotent elements. In this context,
associated varieties and singularities of nilpotent Slodowy slices are proving to be
very useful tools to ﬁnd new collapsing levels. Let us outline the main idea.
It may happen that a nilpotent Slodowy slice SO,f is isomorphic to a nilpotent
orbit Zariski closure O♮in the reductive Lie algebra g♮. Many examples can be
exhibited from [13, 14, 10]. If so, and if O and O♮are the associated varieties of
some aﬃne vertex algebras Lk(g) and Lk♮(g♮), respectively, one may ask whether
k is a collapsing level. Naturally, the knowledge of the associated varieties is far
from suﬃcient to ensure that given vertex algebras are isomorphic, but in some
favourable cases we are able to conclude.
If k is an admissible level, and if V is either the simple aﬃne vertex algebra Lk(g)
or its Drinfeld-Sokolov reduction H0
DS,f(Lk(g)), then its normalized character χV
admits a “nice” asymptotic behavior [12]. Then we prove the following.
Theorem 2 (Arakawa-Moreau). Assume that k and k♮are admissible levels for
g and g♮, respectively, that f ∈XLk(g) and that χH0
DS,f (Lk(g))(τ) ∼χLk♮(g♮)(τ), as
τ ↓0. Then H0
DS,f(Lk(g)) ∼= Wk(g, f) is simple and k is a collapsing level.
In this way we discovered a large number of collapsing levels for f̸ = fmin.
Theorem 3 (Arakawa-Moreau). Assume that g = sln (we have similar results
for son and spn). Write n = mq + s, with m, q > 0 and s ≥0. Assume that
(q, s) = 1 and that the partition associated with the nilpotent orbit Gf is (qm, 1s).
Then W−n+n/q(sln, f) ∼= L−s+s/q(sls) so that k = −n + n/q is a collapsing level.
Example 4. Here are a few examples in the exceptional types (we do not list all the
examples obtained), where we write for f the label in the Bala-Carter classiﬁcation
of its nilpotent orbit:
W−12+12/5(E6, A4) ∼= L−2+2/5(A1),
W−18+18/3(E7, E6) ∼= L−2+2/13(A1),
W−18+18/7(E7, (A5)′′) ∼= L−4+4/7(G2),
W−9+9/7(F4, B3) ∼= L−2+2/7(A1),
etc.
All these examples are obtained by exploiting [2] and [10] to detect the levels, and
then applying Theorem 2 to prove that the isomorphisms indeed hold.
It was observed by physicists that nilpotent Slodowy slices appear as the Higgs
branches of Argyres-Douglas theories in four-dimensional N = 2 superconformal
ﬁeld theories (see e.g. [15]).
The Higgs branch of a four-dimensional N = 2
superconformal ﬁeld theory T is conjecturally [7] isomorphic to the associated
variety of the vertex algebra corresponding to T via the 4d/2d-duality discov-
ered in [6]. The reader is referred to [3] for a recent survey on this conjecture.
Now, typical examples of vertex algebras corresponding to the Argyres-Douglas
theories are the vertex algebras L−h∨+h∨/q(g), W−h∨+h∨/q(g, f), for g of type
2The work of Adamovi´c et al. [1] includes the case where g is a simple aﬃne Lie superalgebra.
Enveloping Algebras and Geometric Representation Theory
3123
A, D, E. Such exemples have occured in Theorem 3 and Example 4. As noticed
in [15], a given Argyres-Douglas theory can be realized in several ways. When-
ever this happens, it means that we have an isomorphisms between W-algebras.
We believe that such a phenomenon essentially reﬂects that the level is collaps-
ing, provided that one of the W-algebras in an aﬃne vertex algebra. Actually,
from the geometry of nilpotent Slodowy slices, it is sometimes possible to predict
isomorphisms between non-trivial W-algebras. For example, we conjecture that
W−7+7/3(sl7, f) ∼= W−4+4/3(sl4, f ′), where f belongs to the nilpotent orbit of sl7
associated with the partition (3, 22) and f ′ to that of sl4 associated with (22).
Acknowledgments. Part of this work was done during author’s stay at the RIMS
of Kyoto as a visiting professor. The author wishes to express her thanks to this
institute for its hospitality. She is supported by the ANR Project GeoLie Grant
number ANR-15-CE40-0012 and the Labex CEMPI (ANR-11-LABX-0007-01).
References
[1] D. Adamovi´c, V. Kac, F. M¨oseneder, P. Papi and O. Perˇse, An application of collapsing
levels to the representation theory of aﬃne vertex algebras, to appear in IMRN.
[2] T. Arakawa, Associated varieties of modules over Kac-Moody algebras and C2-coﬁniteness
of W -algebras, IMRN 2015 (2015), n◦22, 11605–11666.
[3] T. Arakawa, Associated varieties and Higgs branches (a survey), Contemp. Math. 711
(2018), 37–44.
[4] T. Arakawa and A. Moreau, Joseph ideals and lisse minimal W-algebras, J. Inst. Math.
Jussieu, 17 (2018), n◦2, 397–417.
[5] T. Arakawa and A. Moreau, On the irreducibility of associated varieties of W-algebras, J.
of Algebra, 500 (2018), 542–568.
[6] C. Beem, M. Lemos, P. Liendo, W. Peelaers, L. Rastelli, and B. C. van Rees, Inﬁnite chiral
symmetry in four dimensions, Comm. Math. Phys. 336 (2015), n◦3, 1359–1433.
[7] C. Beem and Leonardo Rastelli, Vertex operator algebras, Higgs branches, and modular
diﬀerential equations, preprint, arXiv:1707.07679[hep-th].
[8] B. Feigin and E. Frenkel, Quantization of the Drinfel′d-Sokolov reduction, Phys. Lett. B
246 (1990), n◦1-2, 75–81.
[9] A. De Sole and V. Kac, Finite vs aﬃne W-algebras, Jpn. J. Math. 1 (2006), n◦1, 137–261.
[10] B. Fu, D. Juteau, P. Levy, and E. Sommers, Generic singularities of nilpotent orbit closures,
Adv. Math. 305 (2017), 1–77.
[11] V. Kac, S. Roan, and M. Wakimoto, Quantum reduction for aﬃne superalgebras, Comm.
Math. Phys. 241 (2003), n◦2-3, 307–342.
[12] V. Kac and M. Wakimoto, Classiﬁcation of modular invariant representations of aﬃne
algebras, Adv. Ser. Math. Phys. 7, 138–177. World Sci. Publ., Teaneck, NJ, 1989.
[13] H. Kraft and C. Procesi, Minimal singularities in GLn, Invent. Math. 62 (1981), n◦3,
503–515.
[14] H. Kraft and C. Procesi, On the geometry of conjugacy classes in classical groups, Comment.
Math. Helv. 57 (1982), n◦4, 539–602.
[15] J. Song, D. Xie, and W. Yan, Vertex operator algebras of Argyres-Douglas theories from
M5-branes, J. High Energy Phys. 12 (2017), n◦123, front matter+35.
3124
Oberwolfach Report 52/2018
