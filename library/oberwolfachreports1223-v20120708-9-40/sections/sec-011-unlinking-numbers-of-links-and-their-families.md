---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-011-unlinking-numbers-of-links-and-their-families
section_title: "Unlinking numbers of links and their families"
section_number: null
pages: 24-27
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Slavik Jablan
The main topic of this talk is the Bernhard-Jablan Conjecture [2, 8, 9] and
recent results related to it. The term “link” will be used for both knots and links.
In this setting we have the following deﬁnition:
Deﬁnition 1.
a) The unlinking number u(D) of a link diagram D is the minimal number of
crossing changes on the diagram required to obtain a diagram representing
an unlink.
b) The uM(L) of a link L in R3 is the minimum of u(D) over all minimal
crossing number diagrams D representing L.
c) The unlinking number u(L) of a link L in R3 is the minimum of u(D)
over all diagrams D representing L.
Computing unlinking number is usually very diﬃcult and complex problem.
Therefore we deﬁne BJ-unlinking number which is computable due to the algo-
rithmic nature of its deﬁnition.
Deﬁnition 2. For a given crossing v of a diagram D representing link L let Dv
denote the link diagram obtained from D by switching crossing v.
a) The BJ-unlinking number uBJ(D) of a diagram D is deﬁned recursively
in the following manner:
(1) uBJ(D) = 0 iﬀD represents an unlink.
(2) uBJ(D) = 1+min
Dv uBJ(Dv) where the ﬁrst minimum is taken over all
crossings v of D and the second minimum is taken over all minimal
diagrams of a link represented by Dv for which the value is already
deﬁned.
b) The BJ-unlinking number uBJ(L) of a link L uBJ(L) = min
D
uBJ(D)
where the minimum is taken over all minimal diagrams D representing L.
Bernhard [2] in 1994 and independently Jablan in 1995, conjectured that for
every link L we have that u(L) = uBJ(L).
Invariants in Low-Dimensional Topology and Knot Theory
25
Deﬁnition 3. Let S denote the set of numbers in the unreduced1 Conway sym-
bol C(L) of a link L [3]. Given C(L) and an arbitrary (non-empty) subset ˜S =
{a1, a2, . . . , am} of S, the family F ˜S(L) of knots or links derived from L is con-
structed by substituting each ai ∈˜S, ai̸ = 1 in C(L) by sgn(a)(|a|+n), for n ∈N +.
For even integers n ≥0 this construction preserves the number of components,
i.e., we obtain (sub)families of links with the same number of components. If all
parameters in a Conway symbol of a knot or link are 1, 2, or 3, such a link is called
generating.
For alternating knots, signature can be computed by using a combinatorial for-
mula derived by P. Traczyk [14]. We will use this formula, proved by J. Przytycki,
in the following form, taken from [13], Theorem 7.8, Part (2):
Theorem 1. If D is a reduced alternating diagram of an oriented knot, then
σD = −1
2w + 1
2(W −B) = −1
2w + 1
2(|Ds+| −|Ds−|),
where w is the writhe of D, W is the number of white regions in the checkerboard
coloring of D, which is for alternating minimal diagrams equal to the number of
cycles |Ds+| in the state s+, and B is the number of black regions in the checker-
board coloring of D equal to the number of the cycles |Ds−| in the state s−.
Introducing orientation of a knot, every n-twist (chain of digons) becomes par-
allel or anti-parallel.
Lemma 2. By replacing n-twist (n ≥2) by (n+ 2)-twist in the Conway symbol of
an alternating knot K, the signature changes by −2 if the replacement is made in a
parallel twist with positive crossings, the signature changes by +2 if the replacement
is made in a parallel twist with negative crossings, and remains unchanged if the
replacement is made in an anti-parallel twist.
Theorem 3. The signature σK of an alternating knot K given by its Conway
symbol is
σK =
!
P
−2
*ni
2
+
ci + 2c0,
where the sum is taken over all parallel twists ni, ci ∈{1, −1} is the sign of
crossings belonging to a parallel twist ni, and 2c0 is an integer constant which can
be computed from the signature of the generating knot.
The proof of this theorem follows directly form the preceding Lemma, claiming
that only additions of twists in parallel twists in a Conway symbol result in the
change of signature, and that by every such addition, signature changes by −2ci.
Notice that the condition that we are making twist replacements in the standard
Conway symbols, i.e., Conway symbols with the maximal twists, is essential for
computation of general formulae for the signature of alternating knot families.
1The Conway notation is called unreduced if 1’s denoting elementary tangles in vertices are
not omitted in symbols of polyhedral links.
26
Oberwolfach Report 28/2012
K. Murasugi [11] proved the lower bound for the unknotting number of knots,
u(K) ≥|σK|
2 . Using this criterion, for many (sub)families of knots we can conﬁrm
that their BJ-unknotting numbers, i.e., unknotting numbers computed according
to Bernhard-Jablan Conjecture, represent the actual unknotting numbers of these
families.
Let be given the Conway symbol of a knot family F with parameters p1, p2, . . . ,
pn denoting twists (pi > 1, i = 1, . . . , n). The polynomial with variables p1, p2, . . . ,
pn and integer coeﬃcients, obtained as the evaluation of the Conway polynomial
of the family F for x = 2i, where i is the imaginary unit, will be called the critical
polynomial.
Conjecture 4. For every knot or link, the maximal degree of every variable in its
critical polynomial is 1.
If Conjecture 4 is true, following the changes of the sign of critical polynomial,
we will be able to obtain general formulae for the signature of particular subfamilies
of nonalternating knots and links and conﬁrm their unknotting numbers estimated
according to BJ-conjecture.
Except the above mentioned problems, we will consider a few other topics re-
lated to unknotting: ascending numbers [12, 7], knot distances [4], smoothing
numbers (band unknotting numbers) [1], pseudodiagrams and their trivializing
and knotting numbers [5, 6], as well as unknotting numbers related to virtual
knots and links [10, 6].
References
[1] T. Abe and T. Kanenobu, Unoriented Band Surgery on Knots and Links, arXiv:1112.2449.
[2] J. A. Bernhard, Unknotting numbers and their minimal knot diagrams, J. Knot Theory
Ramiﬁcations, 3, no. 1 (1994) 1–5.
[3] J. Conway, An enumeration of knots and links and some of their related properties, in Com-
putational Problems in Abstract Algebra, Proc. Conf. Oxford 1967 (Ed. J. Leech), 329–358,
Pergamon Press, New York (1970).
[4] I. K. Darcy, D. W. Sumners, Rational Tangle Distances on Knots and Links, Mathematical
Proceedings of the Cambridge Philosophical Society, 128 (2000), no. 3, 497–510.
[5] R. Hanaki, Pseudodiagrams of knots, links and spatial graphs, Osaka J. of Mathematics, 47
(2010), 863–883.
[6] A. Henrich, N. Macnaughton,
S. Narayan, O. Pechenik, J. Townsend, Classical and
Virtual Pseudodiagram Theory and New Bounds on Unknotting Numbers and Genus,
arXiv:0908.1981.
[7] S. V. Jablan, Unknotting and Ascending Numbers of Knots and their Families, arXiv:
1107.2110.
[8] S. V. Jablan, R. Sazdanovi´c, LinKnot – Knot Theory by Computer, World Scientiﬁc, New
Jersey, London, Singapore (2007), (http://math.ict.edu.rs/).
[9] S. V. Jablan, R. Sazdanovi´c, Unlinking number and unlinking gap, J. Knot Theory Ramiﬁ-
cations, 16, 10 (2007) 1331–1355.
[10] L. H. Kauﬀman, Virtual Knot Theory, Europ. J. Combinatorics, 20 (1999) 663–691.
[11] K. Murasugi, On a certain numerical invariant of link types, Trans. Amer. Math. Soc., 117
(1965) 387–422.
[12] M. Ozawa, Ascending number of knots and links, J. Knot Theory Ramiﬁcations, 9, no. 1
(2010) 15–25.
Invariants in Low-Dimensional Topology and Knot Theory
27
[13] J. Przytycki, From Goeritz matrices to quasi-alternating links, arXiv:
0909.1118.
[14] P. Traczyk, A combinatorial formula for the signature of alternating diagrams, Fundamenta
Mathematicae 184 (2004), 311–316 (a new version of the unpublished manuscript, 1987).
