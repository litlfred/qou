---
doc_id: arxiv-1904.05612v3
doc_title: "ON ORTHOGONAL SYSTEMS, TWO-SIDED BASES AND REGULAR SUBFACTORS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1904.05612v3.pdf
source_sha256: 49de771ab5b79489
toc_source: outline
doc_brief: "ON ORTHOGONAL SYSTEMS, TWO-SIDED BASES AND REGULAR SUBFACTORS — We prove that a regular subfactor of type II1 with ﬁnite Jones index always admits a two-sided Pimsner-Popa basis."
---
Let N ⊂M be a unital inclusion of von Neumann algebras equipped with a faithful
normal conditional expectation E from M onto N. Then, a ﬁnite set B := {λ1, . . . , λn} ⊂
M is called a left Pimsner-Popa basis for M over N via E if every x ∈M can be expressed
as x = Pn
i=1 E(xλ∗
i )λi - see [14, 17, 16, 9, 20] and the references therein. Similarly, B is
called a right Pimsner-Popa basis for M over N via E if every x ∈M can be expressed
as x = Pn
j=1 λjE(λ∗
jx). And, B is said to be a two-sided basis if it is simultaneously a left
and a right Pimsner-Popa basis. It is readily seen that a type II1 subfactor that admits a
two-sided basis is always extremal (Proposition 3.1).
An extensively exploited result of Pimsner and Popa (from [14]) states that if N ⊂M
is a subfactor of type II1 with ﬁnite Jones index ([7]), then there always exists a left
(equivalently, a right) Pimsner-Popa basis for M over N via the unique trace preserving
conditional expectation EN : M →N. As noted above, non-extremal subfactors do not
admit two-sided bases. So, it is natural to ask whether there always exists a two-sided basis
for every ﬁnite index extremal subfactor or not. In fact, it has also been asked publicly by
Vaughan Jones at various places, see, for instance the talk 1 by M. Izumi in the workshop
organized in honour of V. S. Sunder’s 60th birthday in Chennai during March-April 2012.
Given the fact that every irreducible regular subfactor of ﬁnite index is a group subfactor,
it is not surprising that such a subfactor always admits a two-sided orthonormal basis, as
was illustrated in [6] (also see [1]) . However, it seems to be a diﬃcult question to answer
in general. In this article, we answer this question in aﬃrmative for all regular subfactors
of type II1 with ﬁnite Jones index (without assuming extremality) in:
Theorem 3.10. Let N ⊂M be a regular subfactor of type II1 with ﬁnite Jones index.
Then, M admits a two-sided basis over N.
As a consequence, we deduce that every ﬁnite index regular subfactor of type II1 is
extremal.
Recall that an inclusion Q ⊂P of von Neumann algebras is said to be regular if its
group of normalizers NP(Q) := {u ∈U(P) : uQu∗= Q} generates P as von Neumann
2010 Mathematics Subject Classiﬁcation. 46L37.
Key words and phrases. Orthogonal system, Pimsner-Popa basis, subfactor, regularity.
The ﬁrst named author was supported partially by a postdoctoral fellowship of the National Board of
Higher Mathematics (NBHM), India.
1https://www.youtube.com/watch?v=x4JN6kSie4g (51:30 onward)
1
2
K C BAKSHI AND V P GUPTA
algebra, i.e., NP(Q)′′ = P. Our proof is essentially self contained and does not depend on
any structure theorem for regular subfactors.
An eﬀort has been made to keep this article as self-contained as possible. The reader is
assumed only to have some basic knowledge of subfactor theory, for instance, as discussed
in the ﬁrst few chapters of [9].
Here is a brief outline of the content of this article.
As mentioned in the abstract, we ﬁrst revisit, in Section 2, Popa’s ([17]) notion of an
orthogonal system for an inclusion of von Neumann algebras N ⊂M with a faithful normal
conditional expectation from M onto N. This generalizes the notion of an orthonormal
basis for a subfactor N ⊂M of type II1 introduced by Pimsner and Popa in [14]. Dropping
orthogonality, Jones and Sunder, in [9], generalized the notion of orthonormal basis and
gave another formulation of basis for M over N (as recalled in the ﬁrst paragraph of
Introduction). Very much on the lines of [9], we introduce and discuss the notion of a
Pimsner-Popa system, which generalizes Popa’s notion of an orthogonal system.
If N ⊂M is an inclusion of ﬁnite von Neumann algebras with a ﬁxed faithful normal
tracial state tr on M, then for any Pimsner-Popa system {λ1, · · · , λk} for N ⊂M with
respect to the unique tr-preserving conditional expectation from M onto N, it turns out
that the positive operator f := Pn
i=1 λie1λ∗
i is a projection in M1 (Lemma 2.3), which
we call the support of the system, where as usual e1 denotes the Jones projection for the
canonical basic construction N ⊂M ⊂M1. An astute reader must have already noticed
that, if the support of {λi} equals 1, then it is in fact a Pimsner-Popa basis (in the sense
of [9]) for M over N.
On the other hand, for a ﬁnite index subfactor N ⊂M of type II1, we observe that
for every projection f ∈M1 there exists a Pimsner-Popa system with support f (Proposi-
tion 2.8). An useful consequence of this observation yields:
Theorem 2.10 Let N ⊂M be a subfactor of type II1 with ﬁnite index. Then, any Pimsner-
Popa system {λ1, · · · , λk} for M over N can be extended to a Pimsner-Popa basis for M
over N.
One application being that we deduce in Corollary 2.14 that every subfactor of ﬁnite
index admits a Pimsner-Popa basis (not necessarily orthonormal) containing at least |G|
many unitaries, where G is the generalized Weyl group of the subfactor (as deﬁned in the
next paragraph).
Given its importance, an important example of an orthogonal system for a ﬁnite index
subfactor N ⊂M that we illustrate (in Corollary 2.13) consists of a set containing coset
representatives of, what we call, the generalized Weyl group of the subfactor N ⊂M,
namely, the quotient group
G := NM(N)/U(N)U(N ′ ∩M).
This group was ﬁrst considered by Loi in [12]. Clearly, this group agrees with the Weyl group
of the subfactor if the subfactor is irreducible, i.e., N ′ ∩M = C. Such coset representatives
were also considered in [4, 8, 14, 15, 11, 6] in the irreducible setup and used eﬀectively.
Our second important class of examples of Pimsner-Popa systems comes from unital
inclusions of ﬁnite dimensional C∗-algebras - see Section 2.2.2. This is done by employing
the formalism of path algebras introduced independently by Sunder ([19]) and Ocneanu
([13]). Apart from these, Section 2 is also devoted to a detailed discussion of certain other
useful properties related to Pimsner-Popa systems.
Finally, in Section 3, we settle the question of existence of two-sided basis for any ﬁnite
index regular subfactor N ⊂M. This is achieved through a twofold strategy, namely, we
ON ORTHOGONAL SYSTEMS, TWO-SIDED BASES AND REGULAR SUBFACTORS
3
ﬁrst appeal to the formalism of path algebras to get hold of a two-sided basis for N ′∩M over
C with respect to the restriction of trM (in Proposition 3.3), which also turns out to be a two-
sided basis for R := N ∨(N ′ ∩M) over N (Lemma 3.4), and then, thanks to the regularity
of N ⊂M, every set of coset representatives of the generalized Weyl group of N ⊂M turns
out to be a two-sided orthonormal basis consisting of normalizing unitaries for M over R
(Proposition 3.7). Ultimately, with an appropriate patching technique (Proposition 3.9),
we deduce (in Theorem 3.10) that the product of these two two-sided bases forms a two-
sided Pimsner-Popa basis for M over N.
And ﬁnally, employing the two-sided bases
mentioned above and Watatani’s notion of index of a conditional expectation, we derive (in
Theorem 3.12) that
[M : N] = |G|dimC(N ′ ∩M),
where G again denotes the generalized Weyl group of the subfactor N ⊂M.
