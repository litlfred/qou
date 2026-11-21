---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
arXiv:math/0606435v2  [math.GT]  10 Oct 2007
PROPERTIES OF CLOSED 3-BRAIDS
AND OTHER LINK BRAID REPRESENTATIONS
A. Stoimenow∗
Research Institute for Mathematical Sciences,
Kyoto University, Kyoto 606-8502, Japan
e-mail: stoimeno@kurims.kyoto-u.ac.jp
WWW: http://www.kurims.kyoto-u.ac.jp/˜stoimeno/
Current version: August 8, 2007 First version: September 22, 2004
Abstract. We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and
can be effectively determined. We classify among closed 3-braids strongly quasi-positive and ﬁbered ones, and
show that 3-braid links have a unique incompressible Seifert surface. We also classify the positive braid words with
Morton-Williams-Franks bound 3 and show that closed positive braids of braid index 3 are closed positive 3-braids.
For closed braids on more strings, we study the alternating links occurring. In particular we classify those of braid
index 4, and show that their Morton-Williams-Franks inequality is exact. Finally, we use the Burau representation to
obtain new braid index criteria, including an efﬁcient 4-braid test.
Keywords: link polynomial, positive braid, strongly quasi-positive link, 3-braid link, alternating link, Seifert surface,
ﬁber, incompressible surface, braid index, Burau representation
AMS subject classiﬁcation: 57M25 (primary), 20F36, 32S55 (secondary)
Contents
Introduction
2
2
Preliminaries, basic deﬁnitions and conventions
5
2.1
Links and link diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.2
Polynomial link invariants
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.3
Semiadequacy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.4
Braids and braid words . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.5
Braid representations of links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.6
Gauß sum invariants
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3
Xu’s form and Seifert surfaces
11
3.1
Strongly quasi-positive links among links of braid index 3
. . . . . . . . . . . . . . . . . . . . . . .
11
3.2
Uniqueness of minimal genus Seifert surfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.3
Fiberedness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
∗Supported by 21st Century COE Program.
1
2
1
Introduction
4
Polynomial invariants
15
4.1
Alexander polynomial
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
4.2
Jones polynomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
4.3
Q polynomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
5
Positivity of 3-braid links
26
5.1
Positive braid links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
5.1.1
The Morton-Williams-Franks bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
5.1.2
Maximal subwords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
5.1.3
The proof of Theorem 5.1: Initial simpliﬁcations . . . . . . . . . . . . . . . . . . . . . . . .
28
5.1.4
Two mountains . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
5.1.5
More than two mountains
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
5.1.6
4-braids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
5.2
Positive links
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
6
Studying alternating links by braid index
38
7
Applications of the representation theory
42
7.1
The Jones conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
7.2
Unitarity of the Burau representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
7.3
Norm estimates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
7.4
Skein polynomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
7.5
Recovering the Burau trace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
7.5.1
Conditions on the eigenvalues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
7.5.2
Applications and examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
7.6
Mahler measures
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
7.6.1
3-braids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
7.6.2
Skein polynomial and generalized twisting
. . . . . . . . . . . . . . . . . . . . . . . . . . .
58
7.7
Knots with unsharp MWF inequality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
A Postliminaries
61
A.1
Fibered Dean knots (Hirasawa-Murasugi) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
A.2
A-decomposition (joint with Hirasawa-Ishiwata) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
1.
Introduction
Originating from the pioneering work of Alexander [Al2] and Artin [Ar, Ar2], braid theory has become intrinsically
interwoven with knot theory, and over the years, braid representations of different types have been studied, many of
them with motivation coming from ﬁelds outside of knot theory, for example dynamical systems [Wi] or 4-dimensional
QFTs [Kr].
The systematic study of closed 3-braids was begun by Murasugi [Mu2]. Later 3-braid links have been classiﬁed in
[BM], in the sense that 3-braid representations of the same link are exactly described. This is, up to a few exceptions,
mainly just conjugacy. The conjugacy problem of 3-braids has a series of solutions, starting with Schreier’s algorithm
[Sc], going over Garside [Gr] (for arbitrary braid groups), Xu [Xu] (and later more generally Birman-Ko-Lee [BKL]),
until, for example, a recent algorithm of linear complexity due to Fiedler and Kurlin [FK]. So Birman-Menasco’s
work allows to decide if two 3-braids have the same closure link.
However, many properties of links (except achirality and invertibility) are not evident from (3-strand) braid represen-
tations, and thus to classify 3-braid links with special properties remains a non-trivial task. A ﬁrst result was given in
[Mu] for rational links, and then improved in [St2], where we completed this project for alternating links.
3
From the opposite point of view, a natural question concerning braid representations of links is:
Question 1.1 If a braid representation of a particular type exists, does also one exist with the minimal number of
strands (among all braid representations of the link)?
The minimal number of strands for a braid representation of a link L is called the braid index of the link, and will be
denoted by b(L).
In [Be], Bennequin studied in relation to contact structures braid representations by bands, independently considered
by Rudolph [Ru] in the context of algebraic curves, and more recently in [BKL] from a group theoretic point of view.
A band representation naturally spans a Seifert surface of the link. See ﬁgure 1.
Figure 1: A braided Seifert surface obtained from a band representation
Bennequin proved in [Be] that a minimal genus band representation always exists on 3-braids. Such surface was called
by Birman-Menasco [BM2] a Bennequin surface. Later, by examples found by Ko and Lee, and Hirasawa and myself,
the existence of Bennequin surfaces on the minimal number of strands was found not to extend to 4-braids. (We will
see in this paper, though, among many other things, that it does extend for alternating links.) Since by Rudolph’s work
[Ru], a Bennequin surface exists for any link, on a possibly large number of strands, the answer to the question 1.1 is
negative for minimal genus band representations.
A special case of band representations are the positive ones, called strongly quasi-positive in [Ru]. For such repre-
sentations the above examples do not apply. The existence of minimal such representations is a question of Rudolph,
whose answer is not known. Our ﬁrst result is a positive answer to Rudolph’s question for 3-braids.
Theorem 1.1 If L is a strongly quasi-positive link, and has braid index 3, then L is has a strongly quasi-positive
3-braid representation.
This result is an application of the work in [St2] on Xu’s normal form [Xu]. It legitimizes the term “strongly quasi-
positive 3-braid link”, which otherwise would be linguistically sloppy, for it may mean a 3-braid link that is strongly
quasi-positive, or the link (which is the closure) of a strongly quasi-positive 3-braid.
As an (a-priori-so-seeming) improvement of Bennequin’s theorem, Birman-Menasco proved [BM2] that for 3-braid
links not only some but in fact any minimal genus surface is a Bennequin surface. Xu used this result and the
classiﬁcation in [BM] to conclude that most 3-braid links have a unique minimal genus surface. Unfortunately, she
failed to deal (in the oriented sense) with some exceptions, which we complete in section 3 (see theorem 3.1).
The following work involves a further study of Xu’s normal form. A natural relation of this form to the skein polyno-
mial was exhibited in [St2]. Here we extend this study to the Alexander polynomial ∆. As a result, we can describe
3-braid links with given ∆, and in particular show no non-trivial 3-braid knot has trivial polynomial. In [B], Birman
constructed some pairs of different 3-braid links with the same polynomials and proposed the problem to understand
4
