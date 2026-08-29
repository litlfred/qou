---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-006-7-applications-of-the-representation-theory-42
section_title: "Applications of the representation theory 42"
section_number: 7
pages: 2-5
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
7.1 The Jones conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
7.2 Unitarity of the Burau representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
7.3 Norm estimates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
7.4 Skein polynomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
7.5 Recovering the Burau trace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
7.5.1 Conditions on the eigenvalues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
7.5.2 Applications and examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
7.6 Mahler measures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.6.1 3-braids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.6.2 Skein polynomial and generalized twisting . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.7 Knots with unsharp MWF inequality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
A Postliminaries 61
A.1 Fibered Dean knots (Hirasawa-Murasugi) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
A.2 A-decomposition (joint with Hirasawa-Ishiwata) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
1. Introduction
Originating from the pioneering work of Alexander [Al2] and Artin [Ar, Ar2], braid theory has become intrinsically
interwoven with knot theory, and over the years, braid repre sentations of different types have been studied, many of
them with motivation coming from ﬁelds outside of knot theory, for example dynamical systems [Wi] or 4-dimensional
QFTs [Kr].
The systematic study of closed 3-braids was begun by Murasug i [Mu2]. Later 3-braid links have been classiﬁed in
[BM], in the sense that 3-braid representations of the same link are exactly described. This is, up to a few exceptions,
mainly just conjugacy. The conjugacy problem of 3-braids has a series of solutions, starting with Schreier’s algorithm
[Sc], going over Garside [Gr] (for arbitrary braid groups), Xu [Xu] (and later more generally Birman-Ko-Lee [BKL]),
until, for example, a recent algorithm of linear complexity due to Fiedler and Kurlin [FK]. So Birman-Menasco’s
work allows to decide if two 3-braids have the same closure link.
However, many properties of links (except achirality and invertibility) are not evident from (3-strand) braid represen-
tations, and thus to classify 3-braid links with special properties remains a non-trivial task. A ﬁrst result was given i n
[Mu] for rational links, and then improved in [St2], where we completed this project for alternating links.
3
From the opposite point of view, a natural question concerning braid representations of links is:
Question 1.1 If a braid representation of a particular type exists, does a lso one exist with the minimal number of
strands (among all braid representations of the link)?
The minimal number of strands for a braid representation of a link L is called the braid index of the link, and will be
denoted by b(L).
In [Be], Bennequin studied in relation to contact structure s braid representations by bands, independently considere d
by Rudolph [Ru] in the context of algebraic curves, and more recently in [BKL] from a group theoretic point of view.
A band representation naturally spans a Seifert surface of the link. See ﬁgure 1.
Figure 1: A braided Seifert surface obtained from a band representation
Bennequin proved in [Be] that a minimal genus band representation always exists on 3-braids. Such surface was called
by Birman-Menasco [BM2] a Bennequin surface. Later, by examples found by Ko and Lee, and Hirasawa and myself,
the existence of Bennequin surfaces on the minimal number of strands was found not to extend to 4-braids. (We will
see in this paper, though, among many other things, that it does extend for alternating links.) Since by Rudolph’s work
[Ru], a Bennequin surface exists for any link, on a possibly large number of strands, the answer to the question 1.1 is
negative for minimal genus band representations.
A special case of band representations are the positive ones , called strongly quasi-positive in [Ru]. For such repre-
sentations the above examples do not apply. The existence of minimal such representations is a question of Rudolph,
whose answer is not known. Our ﬁrst result is a positive answer to Rudolph’s question for 3-braids.
Theorem 1.1 If L is a strongly quasi-positive link, and has braid index 3, the n L is has a strongly quasi-positive
3-braid representation.
This result is an application of the work in [St2] on Xu’s norm al form [Xu]. It legitimizes the term “strongly quasi-
positive 3-braid link”, which otherwise would be linguistically sloppy, for it may mean a 3-braid link that is strongly
quasi-positive, or the link (which is the closure) of a strongly quasi-positive 3-braid.
As an (a-priori-so-seeming) improvement of Bennequin’s theorem, Birman-Menasco proved [BM2] that for 3-braid
links not only some but in fact any minimal genus surface is a Bennequin surface. Xu used this re sult and the
classiﬁcation in [BM] to conclude that most 3-braid links ha ve a unique minimal genus surface. Unfortunately, she
failed to deal (in the oriented sense) with some exceptions, which we complete in section 3 (see theorem 3.1).
The following work involves a further study of Xu’s normal form. A natural relation of this form to the skein polyno-
mial was exhibited in [St2]. Here we extend this study to the A lexander polynomial ∆. As a result, we can describe
3-braid links with given ∆, and in particular show no non-trivial 3-braid knot has triv ial polynomial. In [B], Birman
constructed some pairs of different 3-braid links with the s ame polynomials and proposed the problem to understand
4 1 Introduction
the values of the various link polynomials on 3-braid links. Our work solves (to a large extent at least) Birman’s
problem for the Alexander polynomial. We also have a solutio n for the Jones and Brandt-Lickorish-Millett-Ho Q
polynomial.
Parallel to the Alexander polynomial description, and using a recent result of Hirasawa-Murasugi, we classify among
3-braid links the ﬁbered ones. (This result was proved indep endently by Yi Ni in [Ni], apparently unaware of this
work, which I did to make widely public immediately.) We will see then that a 3-braid knot is ﬁbered if (and only if)
its Alexander polynomial is monic, but that this is not true for 2- or 3- component links.
The fact that most 3-braid links were found ﬁbered, and this c ould be proved independently from Bennequin and
Birman-Menasco, opened the hope for a more natural approach to some of their results. Finally we were indeed able
to complete this project, with the assistance of M. Hirasawa and M. Ishiwata, obtaining
Theorem 1.2 Any 3-braid link has a unique (non-closed) incompressible surface.
This result subsumes all previous uniqueness theorems. Bes ides, its proof is entirely different, in that it fully avoid s
the contact geometry approach of Bennequin and the considerable complexity in Birman-Menasco’s subsequent braid
foliation work. Instead, we use the sutured manifold theory of Gabai [Ga, Ga2] (to deal with the ﬁbered links) and
Kobayashi-Kakimizu [Ko, Kk] (for the remaining cases), as w ell as some of our preceding work on the Alexander
polynomial (to rule out disconnected Seifert surfaces). Si nce Kobayashi-Kakimizu use a slightly stronger notion of
uniqueness (see the beginning of §3.2), theorem 1.2 is an improvement even for minimal genus surfaces. Moreover, its
proof underscores the geometric meaning of Xu’s form, that remained unclear in [BM]. While we still cannot provide
an “easy” proof of Birman-Menasco’s classiﬁcation theorem(see remark on p. 34 of [BM]), our work will likely lead
to simpliﬁcations in their very lengthy treatment, which makes heavy use of incompressible surfaces.
The study and applications of Xu’s form occupy the ﬁrst main part of the paper. Then some related results are included,
whose treatment requires different methods. These results are dealt with in the later sections of the paper.
As a ﬁrst such topic, more substantial effort will be made to p rove an analogous result to theorem 1.1 for positive (in
the usual Artin generators) braid representations.
Theorem 1.3 If L is a positive braid link, and has braid index 3, then L is a positive 3-braid link.
So our work here can be understood to answer question 1.1 for b raid index 3 and strongly quasi-positive or positive
braid links. (The state of quasi-positive links, and of quasi-positive braid representations with regard to question 1.1, in
contrast remains open. There is, however, an algorithm, found by orevkov [Or] to decide if a 3-braid is quasi-positive.)
The proof of theorem 1.3 requires a study of positive braids w here the braid index bound in the Morton-Williams-
Franks inequality [Mo, FW] is 3. This study builds on and exte nds (but also considerably simpliﬁes) the work of
Nakamura [Na] for Morton-Williams-Franks bound 2. Then some detailed case distinction and calculation are neces-
sary. In [St3] it was shown, again, that theorem 1.3 is not tru e for 4-braids: there are two 16 crossing knots that have
positive 16 crossing 5-braid representations, but braid in dex 4 (and consequently only non-positive 4-braid represen -
tations). It is in fact for these examples that I was led to investigate about the theorem.
In section 5.2, using the arguments in the proof of theorem 1. 3 and a criterion of Yokota [Yo], we consider 3-braid
representations of links that are (diagrammatically) posi tive. We obtain strong restrictions on such representation s,
and in particular determine which of the links are not ﬁbered. (See theorem 5.5.)
Another problem proposed by Birman, in [Mo2], was to understand the relation of alternation of links (as a pre-eminent
diagram deﬁned property) and braid representations. Early substantial results on the braid index of alternating links
were due to Murasugi [Mu], who determined the braid index for rational and ﬁbered alternating links. In [St2] we
used Xu’s form to classify the braid index 3 alternating links. Here, in §6, we will easily recover this result and push
it forward to braid index 4. For this we use an argument based o n the Jones polynomial, and connect the celebrated
Kauffman-Murasugi-Thistlethwaite work [Ka2, Mu3, Th2] to braid representations. The existence of the Bennequin
surface of alternating links on a 4 string braid (corollary 6.4) is among several easy consequences we obtain.
The last section §7 discusses some applications of the Squier unitarization [ Sq] of the Burau representation, that
concern also braids on more strings. A ﬁrst series of conditi ons are estimates on the norm of special values of the
5
Alexander and Jones polynomial. They relate to and partly ex tend estimates of Jones in [J]. In particular, we will
see that the Alexander polynomial provides conditions for e very given braid index. Some properties of the skein
polynomial, and a relation to Mahler measure are also discussed.
In the case of a 4-braid, one can go further and (almost) ident ify the Eigenvalues of the Burau matrix from the
Alexander and Jones polynomial (of its closure). Using this , a criterion for braid index 4 is derived. We show
examples exhibiting the efﬁciency of this test, including s uch where not only the Morton-Williams-Franks inequality
itself, but also its 2-cable version fails (and so our test seems the only practicable option).
In the appendix we collect some work of Hirasawa, Ishiwata an d Murasugi, which completes the proof of several of
our results.
