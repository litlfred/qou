---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-038
section_title: "Page 38"
section_number: null
pages: 38-38
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
range is the set of all (not necessarily compactly supported) probability measures
on R. (Note that in [Ke4], the symbol M refers to the latter set.)
Formula (8.1) means that the two sequences,

−k
Z
R
xk−1σ′(x)dx

k=1,2,...
and
Z
R
xkµ(dx)

k=1,2,...
,
are related to each other in exactly the same way as the two systems of generators
of the algebra Λ, {pk}k=1,2,... and {hk}k=1,2,....
From now on and up to the end of this section we restrict ourselves to measures
µ from the subset M0.
Deﬁnition 8.2. Recall that the algebra A can be realized as the image of Λ under
the morphism (2.18), and let eh2, eh3, . . . denote the image in A of the elements
h2, h3, . . . .
We realize A as an algebra of functions on M0 by setting
ehk[µ] =
Z
R
xkµ(dx),
µ ∈M0,
k = 2, 3, . . . .
Equivalently, for any f ∈A, we set f[µ] = f[ω], where ω ↔µ and f[ω] is understood
according to Deﬁnition 2.10 b).
Proposition 8.3. Let ω = λ( · ), where λ is a Young diagram, and let {xi}m+1
i=1 ,
{yj}m
j=1 be the local extrema of λ(x), see §2. Then the transition measure of ω is
supported by the ﬁnite set {x1, . . ., xm+1} and is given by the following formula:
µ =
m+1
X
i=1
µiδxi,
(8.2)
where δx denotes the Dirac mass at x and the weights µ1, . . ., µm+1 are the coeﬃ-
cients in the expansion
Qm
j=1(z −yj)
Qm+1
i=1 (z −xi)
=
m+1
X
i=1
µi
z −xi
.
(8.3)
Proof. See [Ke2], [Ke4].
□
The measure µ deﬁned by (8.2)–(8.3) is called the transition measure of a given
Young diagram λ. For a justiﬁcation of this term and more details, see [Ke2], [Ke3],
[Ke4].
Proposition 8.4. The transition measure of Ω∈D0 is the “semi–circle distribu-
tion” µs-c supported by [−2, 2],
µs-c(dx) =
1
2π
p
4 −x2.
(8.4)
Proof. See [Ke2], [Ke4].
□
38
