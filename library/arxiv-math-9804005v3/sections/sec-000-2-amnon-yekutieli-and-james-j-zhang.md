---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-000-2-amnon-yekutieli-and-james-j-zhang
section_title: "AMNON YEKUTIELI AND JAMES J. ZHANG"
section_number: 2
pages: 1-2
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
Abstract. A ring with an Auslander dualizing complex is a generalizati on
of an Auslander-Gorenstein ring. W e show that many results w hich hold for
Auslander-Gorenstein rings also hold in the more general se tting. On the
other hand we give criteria for existence of Auslander duali zing complexes
which show these occur quite frequently.
The most powerful tool we use is the Local Duality Theorem for connected
graded algebras over a ﬁeld. Filtrations allow the transfer of results to non-
graded algebras.
W e also prove some results of a categorical nature, most nota bly the func-
toriality of rigid dualizing complexes.
Contents
0. Introduction 1
1. Dualizing complexes 4
2. Auslander Dualizing Complexes 10
3. Rigid Dualizing Complexes 16
4. Dualizing Complexes over Graded Algebras 20
5. Graded Algebras with Some Commutativity Hypothesis 25
6. Noetherian Connected Filtrations 30
References 38
0. Introduction
Dualizing complexes play an essential role in the Serre-Grothendieck Duality
Theory on schemes (see [RD]). The duality formalism was generalized t o noncom-
mutative rings by the ﬁrst author, in order to answer some questio ns which arose
in this context, mainly regarding local duality for noncommutative gr aded alge-
bras (see [Ye1]). A version of Serre duality for noncommutative pro jective schemes
was established using dualizing complexes (see Jørgensen’s [Jo2] and our [YZ1]).
Dualizing complexes, and more generally derived categories, are pow erful tools for
proving abstract properties of noncommutative rings. For examp les, consider the
noncommutative graded versions of the Auslander-Buchsbaum Th eorem, The Bass
Theorem and the No-Holes Theorem for Bass numbers (see [Jo1] Th eorems 3.2, 4.5,
4.6 and 4.8). Under the synonym “cotilting complexes,” dualizing comple xes were
Date: 8 September 1998.
1991 Mathematics Subject Classiﬁcation. Primary: 16D90; Secondary: 16E30, 16L30, 16P60.
Both authors were supported by the US-Israel Binational Sci ence Foundation. The second
author was also supported by the NSF and Sloan Research Fello wship.
1
2 AMNON YEKUTIELI AND JAMES J. ZHANG
studied by Miyachi [Mi2]. Cotilting bimodules occur often in papers on re presen-
tations of ﬁnite-dimensional algebras, cf. [Ha].
In this paper we will provide further evidence that the dualizing comp lex (Deﬁ-
nition 1.1) is an eﬀective tool for studying noncommutative rings. We are especially
interested in those dualizing complexes which satisfy an extra homolo gical condi-
tion called the Auslander property (Deﬁnition 2.1). The basic idea here is that
if a statement holds for Auslander-Gorenstein rings in the sense of [Bj], then an
appropriate version of the statement should hold for rings with Aus lander dualiz-
ing complexes. The Gorenstein condition, i.e. the ring itself having ﬁnit e injective
dimension, is considered to be very restrictive; in contrast, having an Auslander
dualizing complex is considered to be a mild condition.
There are a few ways to show existence of Auslander dualizing comple xes. For
example, if A is a connected graded algebra (over a ﬁeld k) with enough normal
elements, then A has an Auslander dualizing complex. Recall that a connected
gradedk-algebraA has enough normal elements if every graded prime factor A/p ⁄=
k has a nonzero normal element of positive degree. This class of rings has been
studied recently by many algebraists, because of developments in q uantum groups
and noncommutative algebraic geometry.
In this paper we prove a diverse collection of results, whose common thread is
that their proofs are based on the existence of an Auslander dualiz ing complex.
Throughout k denotes a ﬁxed base ﬁeld, and a k-algebra means an associative
algebra with 1.
First we generalize [GL] Theorem 1.6, by dropping the Gorenstein con dition.
Note that the hypothesis on gr A in next theorem is easy to check in practice (see
Example 6.11), and we suspect it can even be weakened.
Theorem 0.1. Assume A is a normally separated ﬁltered k-algebra such that grA
is a noetherian connected graded k-algebra with enough normal elements. Then
SpecA is catenary.
This is proved after Corollary 6.22.
We generalize some results in [ASZ], two of which are:
Theorem 0.2. Assume A is a noetherian k-algebra with an Auslander dualizing
complex. Then there is a step duality between the category ModfA of ﬁnitely gener-
ated left A-modules and the category ModfA◦ of ﬁnitely generated right A-modules.
Actually we prove a more general result involving two algebras – see T heorem
