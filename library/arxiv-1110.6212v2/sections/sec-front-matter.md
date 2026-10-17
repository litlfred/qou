---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
toc_source: outline
doc_brief: "On calibrated representations and the Plancherel Theorem for aﬃne Hecke algebras — This paper has two main purposes."
---
arXiv:1110.6212v2  [math.RT]  26 May 2014
On calibrated representations and the Plancherel Theorem for
aﬃne Hecke algebras
James Parkinson∗
November 28, 2013
Abstract
This paper has two main purposes. Firstly we generalise Ram’s combinatorial construc-
tion [23] of calibrated representations of the aﬃne Hecke algebra to the multi-parameter
case (including the non-reduced BCn case). We then derive the Plancherel formulae for all
rank 1 and rank 2 aﬃne Hecke algebras, using our calibrated representations to construct
all representations involved.
Introduction
In this paper we extend Ram’s combinatorial construction of calibrated representations of aﬃne
Hecke algebras to the multi-parameter case (including the non-reduced case), and we use these
representations to derive explicit Plancherel formulae for all rank 1 and rank 2 aﬃne Hecke
algebras, following the work of Opdam ([18], [19]).
Let us discuss the relevance and signiﬁcance of each of these objectives. Aﬃne Hecke algebras
arise in the study of representation theory of groups G of Lie type deﬁned over local ﬁelds such
as Fq((t)) or Qp. If I is an Iwahori subgroup of G then complex representations of G with vectors
ﬁxed by I can be studied via corresponding representations of the associated aﬃne Hecke algebra
H = Cc(I\G/I) of continuous compactly supported I bi-invariant complex valued functions
on G (see [2], [16]). On the one hand the representation theory of aﬃne Hecke algebras is well
behaved (for example, the irreducible representations of these inﬁnite dimensional algebras are
all ﬁnite dimensional), while on the other hand the representation theory is rather delicate (for
instance see the remarkable geometric classiﬁcation of the irreducibles given in [12] using the
K-theory of the ﬂag variety).
Aﬃne Hecke algebras have a basis {Tw | w ∈W} indexed by elements of an aﬃne Weyl
group W, and depend on parameters q0, . . . , qn (one parameter for each Coxeter generator
s0, . . . , sn of W). The most studied case is the 1-parameter case, where qi = q for all i. It
is to this case that the geometric classiﬁcation mentioned above applies. In [23] Ram introduced
an explicit combinatorial construction of the class of calibrated representations of 1-parameter
aﬃne Hecke algebras. These are the modules which have a basis of simultaneous eigenvectors
for all the elements of a natural large commutative subalgebra of the Hecke algebra. While
not all representations of an aﬃne Hecke algebra are calibrated, the calibrated representations
are of particular interest to combinatorialists since they are the generalisation of the classical
∗Partially supported under the Australian Research Council (ARC) discovery grant DP110103205.
2010 Mathematics Subject Classiﬁcation: 20C08
Keywords: Aﬃne Hecke algebra, Calibrated representations, Plancherel measure.
1
combinatorial constructions for Weyl groups to (one parameter) Hecke algebras. Our ﬁrst aim
in this paper is to extend the construction of calibrated representations to the multi-parameter
case (see Theorem 2.6). We suspect that a full classiﬁcation of calibrated representations, along
the lines of the one parameter case, is possible, although we defer this investigation to later
work and instead the focus here is on constructing calibrated representations. In Section 2.3 we
give some explicit examples of our calibrated representations, and in Section 2.4 we develop the
character theory of calibrated representations in preparation for the Plancherel Theorems.
In the second part of this paper we derive the Plancherel Theorem for rank 1 and 2 aﬃne
Hecke algebras. The Plancherel Theorem is the spectral decomposition of the canonical trace
functional Tr : H →C with Tr(Tw) = δw,1 for w in the aﬃne Weyl group W. It is the analogue
of the formula
Tr(a) =
X
π∈Irrep(H )
mπχπ(a)
for ﬁnite dimensional Hecke algebras, where mπ are the generic degrees (see [8, Chapter 11]).
For aﬃne Hecke algebras the sum becomes an integral over representations of a C∗-algebra
completion of H , and the weights mπ become the Plancherel measure.
The Plancherel Theorem has been proven in general by Heckman and Opdam [10] and
Opdam [19] in a veritable tour-de-force paralleling Harish-Chandra’s work [9] on the Plancherel
Theorem for real and p-adic Lie groups (see also Reeder [26]). The Plancherel Theorem has
been further developed by Delorme-Opdam, Opdam, Opdam-Solleveld, and Ciubotaru-Kato-
Kato ([5], [20], [21], [4]). Therefore we should explain the value of our direct calculations in
ranks 1 and 2.
Firstly, while the general formulation of the Plancherel Theorem in [19] is essentially com-
plete, there are some constants that are not explicitly computed (they are conjectured in [19,
Conjecture 2.27] to be rational numbers). Thus it is desirable to have a complete and direct
calculation in ranks 1 and 2 which evaluate all constants involved. (We note that in the case
of the aﬃne Hecke algebra of the general linear group over a non-archimedean local ﬁeld, the
Plancherel Formula if entirely known, see [1, Remark 5.6]).
Secondly, for concrete applications of the Plancherel Theorem (for example, probabilistic
calculations like in [22]) one may need explicit constructions of the representations involved in
the Plancherel formula. For the non-expert this may be a diﬃcult task to fulﬁll, and so we
believe that the combination of both parts of this paper, with a very concrete matching up
of representations and terms in the Plancherel Theorem, is of value. In particular the use of
calibrated representations makes the Plancherel Theorem accessible at a combinatorial level.
Finally we hope that the explicit calculations may in some ways serve as an introduction
to the general theory, and illustrate the complexity involved in the sophisticated work [19],
[4]. The starting point and general philosophy for our derivation of the Plancherel Theorems
is similar to that in [19], but since we restrict to the rank 1 and 2 cases the calculations can
be carried out by hand. In fact our calculations form an extension of Matsumoto’s inﬂuential
rank 1 calculations [16, §2.6], and hence provides a companion piece to [16] (see also Kutzko
and Morris [13]).
