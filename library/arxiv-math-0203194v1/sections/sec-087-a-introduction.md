---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-087-a-introduction
section_title: "Introduction."
section_number: A
pages: 211-213
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
In this appendix, K always denotes a complete ﬁeld with respect to a
non-archimedean valuation | · |: K →R≥0. The norm | · | is almost always
assumed to be non-trivial, unless otherwise stated.
Let us assume for a while that K is algebraically closed. We view the
ﬁeld K as an aﬃne space, as we do in complex analysis; K is a metrized
space with the metric induced from the valuation | · |. We can then follow
the lines of classical complex analysis and deﬁne convergence of power series,
Taylor and Laurent expansions, etc...
For instance let us deﬁne “holomorphic” functions to be K-valued func-
tions which are locally expressed by convergent power series(1) (cf. [Gou97,
Chap. 4]). This approach drives us however to several problems, which come
mainly from the fact that K with the metric topology is totally disconnected;
for example:
(i) for an open set U ⊆K the ring of all such holomorphic functions on
U is huge. So is already the subring of all locally constant functions.
(ii) It can be shown that the sheaf of germs of such functions satisﬁes the
principle of unique continuation; but not in a satisfactory way. In
particular, Lemma 1.1.2 of Chapter I holds but is of no use, because
there is no non-empty connected open subset.
The trouble becomes more apparent when we think the local repre-
sentability by convergent power series in terms of coverings. In the complex
analytic situation, when we speak of the holomorphy of a function f deﬁned
over a connected open set U, we tacitly take a open covering {Ui}i∈I of U
consisting of suﬃciently small open neighborhoods such that f restricted on
each member Ui can be seen as evaluation of a power series convergent in
Ui. The point is that, since U is connected, members of {Ui} must have
overlaps so that the local properties can be transmitted to whole U. But,
in the non-archimedean situation, such coverings may be reﬁned in such a
way that there are no overlap. This is why the analytic continuation does
(1)The reader may wonder whether there is another approach by means of Cauchy-
Riemann type diﬀerential equations. This is unlikely because the diﬀerential calculus does
not go well, see [Gou97, Chap. 4].
207
208
A. RAPID COURSE IN p-ADIC ANALYSIS.
not work well. So, for the sake of a reasonable analytic theory, we have to
“limit” coverings so that we cannot take arbitrarily ﬁne reﬁnements.
A ﬁrst method is due to Krasner. He introduced the so-called quasi-
connected sets and, on such subsets, deﬁned analytic functions as uniform
convergent limits of rational functions.
A more modern and systematic treatment was introduced by Tate, with
the so-called Rigid Analysis. Let us brieﬂy view the main idea: we ﬁrst set
K{t1, . . . , tn}
=
(
X
ν1,... ,νn≥0
aν1,... ,νntν1
1 · · · tνn
n ∈K[[t1, . . . , tn]]

aν1,... ,νn →0 for
ν1 + · · · + νn →∞
)
,
which is now called the Tate algebra over K. This is the ring of all functions
expressed by power series convergent on the closed disk D(0, 1+) = {z ∈
Kn | |zi| ≤1}. The algebra K{t1, . . . , tn} is endowed with the sup-norm
∥· ∥, also called the Gauss norm. We list up some known properties (cf.
[BGR84, 5.2], [FvdP81, II.3]):
(i) The ring K{t1, . . . , tn} satisﬁes the Weierstrass Preparation Theo-
rem.
(ii) The ring K{t1, . . . , tn} is Noetherian and factorial.
(iii) Every ideal of K{t1, . . . , tn} is closed.
(iv) For any maximal ideal m of K{t1, . . . , tn}, the ﬁeld K{t1, . . . , tn}/m
is a ﬁnite extension of K.
If, moreover, K is algebraically closed, the set of all maximal ideals, en-
dowed with the natural topology, coincides with D(0, 1+). So the situation is
analogous to classical algebraic geometry; D(0, 1+) to the aﬃne n-space, and
K{t1, . . . , tn} to the coordinate ring. In fact, quotients A = K{t1, . . . , tn}/I
by ideals I (called aﬃnoid algebras), and their associated maximal spectra,
Spm(A), called aﬃnoids, forms the fundamental patches from which the
non-archimedean function theory will be developed. Although the natural
metric topology on Spm(A) is terrible for the same reason as above, the
situation becomes much better as far as we deal only with those functions
coming from A. The trick is that, if the algebra A is integral, then we can
pretend that the space Spm(A) is “connected”; for example, the closed disk
D(0, 1+) is “connected” in this sense. So, basically according to this point
of view, we can globalize the situation by gluing aﬃnoid patches to obtain
a reasonable theory of analytic functions. The actual recipe to do it is fur-
nished by the notion of Grothendieck topology, which censors the plethora
of coverings. We will see this a little more precisely in what follows.
Remark 1.1. Although the rigid analysis seems to provide the reasonable
topological and analytical framework, one must not expect it to be as nice
as the complex case. Firstly, in classical complex analysis, when we expand
a holomorphic function centered at a point inside its region of convergence,
the resulting Taylor expansion may have a diﬀerent region of convergence
