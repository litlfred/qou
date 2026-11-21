---
doc_id: download-1
doc_title: "Central and L p -concentration of 1-Lipschitz maps into R -trees"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 1-4
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
toc_source: inferred
doc_brief: "Central and L p -concentration of 1-Lipschitz maps into R -trees — In this paper, we study the Le´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
Introduction.
This paper is devoted to investigating the Le´vy-Milman concentration
phenomenon of 1-Lipschitz maps from mm-spaces (metric measure spaces) to
R-trees. Here, an mm-space is a triple ðX; dX; XÞ of a set X, a complete separable
distance function dX on X, and a ﬁnite Borel measure X on ðX; dXÞ. Let
fðXn; dXn; XnÞg1
n¼1 be a sequence of mm-spaces and fðYn; dYnÞg1
n¼1 a sequence of
metric spaces. Given a sequence ffn : Xn ! Yng1
n¼1 of 1-Lipschitz maps, we
consider the following three properties:
(i) (Concentration property) There exist points mfn 2 Yn, n 2 N, such that
Xnðfxn 2 Xn j dYnðfnðxnÞ; mfnÞ  "gÞ ! 0 as n ! 1
for any " > 0.
(ii) (Central concentration property) The maps fn, n 2 N, concentrate to the
center of mass of the push-forward measure ðfnÞðXnÞ. In other words, the
concentration property (i) holds in the case where mfn is the center of mass.
(iii) (Lp-concentration property) For a number p > 0, we have
2000 Mathematics Subject Classiﬁcation.
Primary 53C23.
This work was partially supported by Research Fellowships of the Japan Society for the
Promotion of Science for Young Scientists.
Key Words and Phrases.
median, mm-space, observable Lp-variation, observable diameter,
observable central radius, R-tree.
#2009 The Mathematical Society of Japan
J. Math. Soc. Japan
Vol. 61, No. 2 (2009) pp. 483–506
Z Z
XnXn
dYnðfnðxnÞ; fnðynÞÞpdXnðxnÞdXnðynÞ ! 0 as n ! 1:
Each target metric space Yn, n 2 N, is called a screen. Chebyshev’s inequality
proves that the Lp-concentration (iii) implies the concentration property (i) for
any p > 0. If each screen Yn, n 2 N, is an Euclidean space Rk, then the
Lp-concentration (iii) for p  1 yields the central concentration property (ii) (see
Corollary 2.19). The central concentration (ii) is stronger than the concentration
property (i). There is an example of maps fn, n 2 N, with the concentration
property (i), but not having the central concentration property (ii) (see Remark
2.17). In some special cases, the concentration (i) implies the central and
Lp-concentration properties (ii) and (iii) (see [3, Subsection 2.4] and [7, Section
3(1/2).31]).
Vitali D. Milman ﬁrst introduced the concentration and the central
concentration properties (i) and (ii) for 1-Lipschitz functions (i.e., Yn ¼ R for
all n 2 N) and emphasized their importance in his investigation of asymptotic
geometric analysis (see [11]). Nowadays those properties are widely studied in
large literature and blend with various areas of mathematics (see [7], [9], [12],
[13], [14], [16], [17] and the references therein for further information). M.
Gromov ﬁrst considered the case of general screens in [5], [6], and [7, Chapter
3(1/2)]. See [3], [4], and [10] for other works of general screens. In [7], Gromov
considered the concentration and central concentration properties (i) and (ii) for
1-Lipschitz maps by introducing observable diameter ObsDiamY ðX; Þ and
observable central radius ObsCRadY ðX; Þ for an mm-space X, a metric space Y ,
and  > 0 (see Section 2 for the precise deﬁnitions). The L2-concentration
property (iii) ﬁrst appeared in Gromov’s paper [5]. Motivated by [5], the author
introduced in [3] the observable Lp-variation Obs Lp-VarY ðXÞ to study the
property (iii) (see Section 2 for the deﬁnition). Note that given a sequence
fXng1
n¼1 of mm-spaces and fYng1
n¼1 of metric spaces, ObsDiamYnðXn; Þ (resp.,
ObsCRadYnðXn; Þ, Obs Lp-VarYnðXnÞ) converges to zero as n ! 1 for any  >
0 if and only if any sequence ffn : Xn ! Yng1
n¼1 of 1-Lipschitz maps (resp., central,
Lp-)concentrates.
In this paper, we treat the case of R-tree screens.
THEOREM 1.1.
Let fXng1
n¼1 be a sequence of mm-spaces. Then, the
following (1.1) and (1.2) are equivalent to each other.
ObsDiamRðXn; Þ ! 0 as n ! 1 for any  > 0:
ð1:1Þ
supfObsDiamTðXn; Þ j T is an R-treeg ! 0 as n ! 1 for any  > 0:ð1:2Þ
484
K. FUNANO
Theorem 1.1 is a complete solution to Gromov’s exercise in [7, Section
3(1/2).32]. In [3, Section 5], the author proved it only for simplicial tree screens.
The implication (1.2) ) (1.1) is obvious. For the proof of the converse, we deﬁne
the notion of a median for a ﬁnite Borel measure on an R-tree in Section 3 and
prove that any 1-Lipschitz maps fn from Xn into R-trees concentrate to medians
of the push-forward measures ðfnÞðXnÞ.
To study the central and Lp-concentration (ii) and (iii) into R-trees, we
estimate the distance between the center of mass and the median of a ﬁnite Borel
measure on an R-tree from above in Section 5. For this estimate, we partially
extend K-T. Sturm’s characterization of the center of mass on a simplicial tree to
the case of an R-tree (see Proposition 2.12 and Section 4). From the estimate, we
bound ObsCRadTðX; Þ (resp., Obs Lp-VarTðXÞ) from above in terms of
ObsCRadRðX; Þ (resp., Obs Lp-VarRðXÞ) (see Propositions 5.6 and 5.8). As a
result, we obtain
THEOREM 1.2.
Let fXng1
n¼1 be a sequence of mm-spaces. Then, the
following (1.3) and (1.4) are equivalent to each other.
ObsCRadRðXn; Þ ! 0 as n ! 1 for any  > 0:
ð1:3Þ
supfObsCRadTðXn; Þ j T is an R-treeg ! 0 as n ! 1 for any  > 0: ð1:4Þ
THEOREM 1.3.
Let fXng1
n¼1 be a sequence of mm-spaces and p  1. Then,
the following (1.5) and (1.6) are equivalent to each other.
Obs Lp-VarRðXnÞ ! 0 as n ! 1:
ð1:5Þ
supfObs Lp-VarTðXnÞ j T is an R-treeg ! 0 as n ! 1:
ð1:6Þ
The condition (1.3) is stronger than (1.1) (see Lemma 2.16 and Remark 2.17),
and (1.5) implies (1.3) (see Corollary 2.19). It seems that the conditions (1.3) and
(1.5) are not equivalent, but we have no counterexample.
In our previous work, the author investigated the above properties (i), (ii),
and (iii) for 1-Lipschitz maps into Hadamard manifolds (see [3, Theorems 1.3, 1.4,
and Lemma 4.4]). The L2-concentration property (iii) in that case is also studied
by Gromov (see [5, Section 13]). Our theorems are thought of as a 1-dimensional
analogue to these works.
Central and Lp-concentration of 1-Lipschitz maps into R-trees
485
