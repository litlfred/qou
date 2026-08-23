---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-556-663-in-elk98-table-2-one-ﬁnds-a-table-of-rationa
section_title: "In [ Elk98, Table 2], one ﬁnds a table of rational CM points z (ratio-"
section_number: 6.6.3
pages: 209-213
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
nal points which correspond to abelian surfaces with comple x multiplication
by an order in M2(Q(
√
−d)) for some fundamental discriminant −d); with
the notation of loc. cit., they are given by z =B/(B−A) =±B/|C|. Some
of them are:
z d =−disc
−33/2272 d = 22.3.7
−53/37 d = 23.5
210/74 d = 3.17
−210/37 d = 19.
Notice that for the ﬁrst value of z, F ( 1
24, 7
24, 5
6 ;−33
2272 )3 converges. More-
over, since ( 22.7
3 ) = +1, it follows from I.4.6.4, I.5.3.9, that the triadic “pe ri-
ods” attached to the abelian surface A−33/2272 with complex multiplication
byM2(Q[
√
−d]) parametrized by z = 1, is algebraic (like the periods of A0).
By 5.6.3, it follows that the triadic number F ( 1
24, 7
24, 5
6 ;−33
2272 )3 is algebraic
(can one compute this algebraic number?).
On the other hand since Q(
√
−d)⁄= Q(√−3) in that case ( d = 2 2.3.7),
the real number F ( 1
24, 7
24, 5
6 ;−33
2272 ) is transcendental; this follows from Wol-
fart’s theorem [ W ol88] (whose proof has been recently completed by work
of Cohen-W¨ ustholz [CW01] and Edixhoven-Yafaev).
It can be proved, a contrario, that if the complex evaluation F ( 1
24, 7
24, 5
6 ;ξ)
is algebraic for some algebraic value ξ in the disc of convergence, then any p-
adic evaluation F ( 1
24, 7
24, 5
6 ;ξ)p which makes sense is also algebraic: indeed,
by [W ol88], [ CW01], such a ξ parametrizes a CM abelian surface by some
order in M2(Q[√−3]), and one concludes again using p-adic Betti lattices
as in I.5.3.
This is actually a very special case of a general, but conject ural, “prin-
ciple of global relations” for special values of solutions o f Gauss-Manin con-
nections, cf. [And95].
206 . p-ADIC ORBIFOLDS AND MONODROMY.
APPENDIX A
Rapid Course in p-adic Analysis.
By F. Kato
1. Introduction.
In this appendix, K always denotes a complete ﬁeld with respect to a
non-archimedean valuation|·| : K→ R≥0. The norm |·| is almost always
assumed to be non-trivial, unless otherwise stated.
Let us assume for a while that K is algebraically closed. We view the
ﬁeld K as an aﬃne space, as we do in complex analysis; K is a metrized
space with the metric induced from the valuation |·| . We can then follow
the lines of classical complex analysis and deﬁne convergen ce of power series,
Taylor and Laurent expansions, etc...
For instance let us deﬁne “holomorphic” functions to be K-valued func-
tions which are locally expressed by convergent power serie s(1) (cf. [Gou97,
Chap. 4]). This approach drives us however to several proble ms, which come
mainly from the fact that K with the metric topology is totally disconnected;
for example:
(i) for an open set U⊆K the ring of all such holomorphic functions on
U is huge. So is already the subring of all locally constant fun ctions.
(ii) It can be shown that the sheaf of germs of such functions s atisﬁes the
principle of unique continuation; but not in a satisfactory way. In
particular, Lemma 1.1.2 of Chapter I holds but is of no use, be cause
there is no non-empty connected open subset.
The trouble becomes more apparent when we think the local repre-
sentability by convergent power series in terms of coverings. In the complex
analytic situation, when we speak of the holomorphy of a func tionf deﬁned
over a connected open set U , we tacitly take a open covering {Ui}i∈I of U
consisting of suﬃciently small open neighborhoods such tha tf restricted on
each member Ui can be seen as evaluation of a power series convergent in
Ui. The point is that, since U is connected, members of {Ui} must have
overlaps so that the local properties can be transmitted to w hole U . But,
in the non-archimedean situation, such coverings may be reﬁ ned in such a
way that there are no overlap. This is why the analytic contin uation does
(1)The reader may wonder whether there is another approach by me ans of Cauchy-
Riemann type diﬀerential equations. This is unlikely becau se the diﬀerential calculus does
not go well, see [ Gou97, Chap. 4].
207
208 A. RAPID COURSE IN p-ADIC ANALYSIS.
not work well. So, for the sake of a reasonable analytic theor y, we have to
“limit” coverings so that we cannot take arbitrarily ﬁne reﬁ nements.
A ﬁrst method is due to Krasner. He introduced the so-called quasi-
connected sets and, on such subsets, deﬁned analytic functions as uniform
convergent limits of rational functions.
A more modern and systematic treatment was introduced by Tat e, with
the so-called Rigid Analysis . Let us brieﬂy view the main idea: we ﬁrst set
K{t1,... ,t n}
=
{ ∑
ν1,... ,νn≥0
aν1,... ,νntν1
1 ··· tνn
n ∈K[[t1,... ,t n]]
⏐
⏐
⏐
⏐
⏐
aν1,... ,νn→ 0 for
ν1 +··· +νn→∞
}
,
which is now called the Tate algebra overK. This is the ring of all functions
expressed by power series convergent on the closed disk D(0, 1+) = {z∈
K n|| zi|≤ 1}. The algebra K{t1,... ,t n} is endowed with the sup-norm
‖·‖, also called the Gauss norm . We list up some known properties (cf.
[BGR84, 5.2], [ FvdP81, II.3]):
(i) The ring K{t1,... ,t n} satisﬁes the Weierstrass Preparation Theo-
rem.
(ii) The ring K{t1,... ,t n} is Noetherian and factorial.
(iii) Every ideal of K{t1,... ,t n} is closed.
(iv) For any maximal ideal m ofK{t1,... ,t n}, the ﬁeld K{t1,... ,t n}/m
is a ﬁnite extension of K.
If, moreover, K is algebraically closed, the set of all maximal ideals, en-
dowed with the natural topology, coincides with D(0, 1+). So the situation is
analogous to classical algebraic geometry; D(0, 1+) to the aﬃne n-space, and
K{t1,... ,t n} to the coordinate ring. In fact, quotients A =K{t1,... ,t n}/I
by ideals I (called aﬃnoid algebras ), and their associated maximal spectra,
Spm(A), called aﬃnoids , forms the fundamental patches from which the
non-archimedean function theory will be developed. Althou gh the natural
metric topology on Spm( A) is terrible for the same reason as above, the
situation becomes much better as far as we deal only with thos e functions
coming from A. The trick is that, if the algebra A is integral, then we can
pretend that the space Spm( A) is “connected”; for example, the closed disk
D(0, 1+) is “connected” in this sense. So, basically according to th is point
of view, we can globalize the situation by gluing aﬃnoid patc hes to obtain
a reasonable theory of analytic functions. The actual recip e to do it is fur-
nished by the notion of Grothendieck topology, which censor s the plethora
of coverings. We will see this a little more precisely in what follows.
Remark 1.1. Although the rigid analysis seems to provide the reasonable
topological and analytical framework, one must not expect i t to be as nice
as the complex case. Firstly, in classical complex analysis , when we expand
a holomorphic function centered at a point inside its region of convergence,
the resulting Taylor expansion may have a diﬀerent region of convergence
