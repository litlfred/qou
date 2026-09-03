---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-039-63-path-morphisms
section_title: "Path morphisms"
section_number: 6.3
pages: 40-41
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
Deﬁnition 4 For (W,S ) a Coxeter system andx∈W we deﬁne the Reduced
expressions graph of x or simply Rex(x) as the graph with nodes the set of
reduced expressions of x and two reduced expressions are joined by an edge
if they differ by a single braid relation.
For every reduced expressions we have associated a Bott-Samelson bimodule
Bs. If two Bott-Samelson bimodulesB,B′ differ by just one braid relation one
has a morphism of the type id⊗fsr⊗ id∈ Hom(B,B′). For example, for the
braid move pq srs u→ pq rsr u(here we suppose srs = rsr ) we have an
associated morphism between the corresponding Bott-Samelson bimodules
id2⊗fsr⊗ id :BpBq(BsBrBs)Bu→BpBq(BrBsBr)Bu.
This means that for each path p in Rex(x) one can uniquely associate a mor-
phism f(p) between the corresponding Bott-Samelson bimodules. We call it a
path morphism.
Deﬁnition 5 A Complete path in a graph is a path passing through every
vertex of the graph at least once.
The following conjecture is due to the author.
Question 6.2 (Forking path conjecture) Letx∈Sn. Letp andq be two com-
plete paths in Rex(x). Then f(p) =f(q).
Some remarks about this conjecture
Remark 4 There has been some serious computer checking of this conjecture
by the author and Antonio Behn, using Geordie Williamson’s programs. That
this conjecture was checked in huge cases (Rex graphs of over 100.000 vertices)
was extremely surprising for the author. There is no conceptual understanding
of why this conjecture could be true. It seems utterly strange.
Remark 5 If this conjecture was proved, then one would have a new and nat-
ural basis for the Hecke algebra, by applying the character map to the image of
this (unique, for any element of Sn) projector. The author believes this would
give a rich combinatorial basis of the Hecke algebra, and a very natural set of
Soergel bimodules that in our dreams should play a role in the understanding
of thep-canonical basis4.
4We will explain in a future paper of this saga what is this basis and why it is so
important.
40
Remark 6 The conjecture is not true for any Coxeter group. There are counter-
examples for F4 (although not easy to ﬁnd). Nonetheless, in [Li3] the author
proves an analogue of the Forking path conjecture for “extra-large Coxeter
groups”, i.e. groups in whichm(s,r )> 3 for alls,r∈S, so it is quite mysteri-
ous for what groups this should be true.
Remark 7 There is a 55 pages paper of Elias [El] published in a ﬁne journal
whose central result is that a certain path morphism in Rex(w0) is an idempo-
tent, wherew0 is the longest element ofSn, and that it projects to the indecom-
posable Soergel bimodule. To prove that this path morphism is an idempotent
has aproximately the same level of difﬁculty as to prove the Forking path con-
jecture for the particular case of the longest element w0 and for two speciﬁc
complete paths p0 and q0. This gives an idea of how hard the Forking path
conjecture can be, and also the kind of methods one can use to attack it (for ex-
ample, the beautiful topology appearing in the higher Bruhat order of Manin
and Schechtman).
If one has a reduced expression t1··· ti of some element x∈ W , then by the
important property in Section 2.7 we know that, if xs < sfor some s∈ S ,
then there is at least one path in Rex(x) starting int1··· ti and ending in some
reduced expression with s in the far-most right position. One considers the
path morphism associated to a path like this and call it a path morphism from
t1··· ti takings to the right.
