---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-092-f-bruhat-tits-building
section_title: "Bruhat-Tits building."
section_number: F
pages: 225-226
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
First we survey the construction of a certain simplicial complex, called
Bruhat-Tits building (attached to PGL(n + 1, K)), which will be closely
related with the Drinfeld symmetric space. Let n be a positive integer and V
an n+1 dimensional vector space over K. A lattice in V is a ﬁnitely generated
R-submodule of V which spans V over K. Every lattice is therefore a free
R-module of rank n + 1. Let e∆0 be the set of all lattices in V . We say
that two lattices M1 and M2 are similar if there exists λ ∈K× such that
M1 = λM2. The similarity is obviously an equivalence relation. We denote
by ∆0 the set of all similarity classes of lattices in V .
Deﬁnition 1.1. The Bruhat-Tits building (attached to PGL(n + 1, K)) is
the ﬁnite dimensional simplicial complex ∆with the vertex set ∆0 deﬁned
as follows: A ﬁnite subset {Λ0, . . . , Λl} of ∆0 forms an l-simplex if and
only if, after permuting indices if necessary, one can choose Mi ∈Λi for
0 ≤i ≤n + 1 such that
M0 ⊋M1 ⊋· · · ⊋Ml ⊋πM0.
The role of M0 is by no means important; for example, one can shift the
indices like M1 ⊋· · · ⊋Ml ⊋πM0 ⊋πM1.
To understand the structure of ∆, let us ﬁx one vertex Λ = [M]. Suppose
{Λ0, . . . , Λl} is an l-simplex having Λ as a vertex; we may assume Λ = Λ0,
and can take Mi ∈Λi for 1 ≤i ≤l such that M ⊋M1 ⊋· · · ⊋Ml ⊋πM.
Set Mi : = Mi/πM. Then we get a ﬂag
M ⊋M1 ⊋· · · ⊋Ml ⊋0
221
222
B. OVERVIEW OF THEORY OF p-ADIC UNIFORMIZATION.
of length l + 1 consisting of subspaces of the n + 1-dimensional k-vector
space M = M/πM. Moreover, by the elementary algebra one ﬁnds that
this yields a one-to-one correspondence between l-simplices containing Λ
and length l + 1 frags in M = M/πM. By this quite easy observation one
knows
(i) ∆is an n-dimensional locally ﬁnite simplicial complex,
(ii) every simplex in ∆is a face of a chamber, a simplex having maximal
(= n) dimension.
Furthermore, by the construction,
(iii) the group AutK(V )/K×(∼= PGL(n + 1, K)) naturally acts on ∆sim-
plicially.
Example 1.2 (n = 1 case). In n = 1 case, the vertices adjacent to a ﬁx
vertex Λ are in one-to-one correspondence with the set of all k-rational
points of the projective line P1
k; in particular, each vertex has exactly q + 1
adjacent vertices.
Moreover, it can be seen that the simplicial complex
∆= ∆1 is a tree. The following picture shows how it looks like in case
q = 2:
r
r
❍❍r
✟
✟
r
✟✟r
❍
❍
r
r
✟✟r
r
❍
❍
r
♣♣♣♣♣♣
♣♣♣♣♣♣
♣♣♣
♣♣♣
♣♣♣♣♣♣
♣♣♣
♣♣♣
♣♣♣♣♣♣
In general, the geometrical realization |∆| of ∆is known to be a con-
tractible topological space.
Example 1.3 (n = 2 case). Already in case n = 2, the structure of ∆= ∆2
is fairly complicated. For a ﬁxed vertex Λ, the set of all vertices adjacent
of Λ is divided in two; one for those corresponding to q2 + q + 1 k-rational
points in P2
k and the other for those corresponding to q2 + q + 1 k-rational
lines in P2
k. So it is convenient to consider the surface B which is obtained
by blowing-up of P2
k at every k-rational points. Two vertices adjacent to Λ
forms with Λ a 2-simplex if and only if the corresponding lines in B intersect.
