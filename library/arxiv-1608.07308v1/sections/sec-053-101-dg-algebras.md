---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-053-101-dg-algebras
section_title: "Dg algebras"
section_number: 10.1
pages: 71-72
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
comes endowed with a grading:
V =
⨁
n∈Z
Vi
and a differentiald : V•→ V•+1 such thatd2 = 0. A vector v∈ V is called homogeneous if
v∈Vi for some integeri. If this is the case, then we will write degv =i.
Deﬁnition 10.1. A dg algebra A• is a dg vector space concentrated in non-positive degrees
(An = 0 forn> 0), which is endowed with a multiplication that preserves the grading:
Ai·Aj⊂Ai+j ∀i,j ∈ N0
and the differential via the graded Leibniz rule:
(10.1) d(a·a′) = (da)·a′ + (−1)degaa· (da′) ∀a,a′∈A
We impose the usual axioms on the dg algebraA•, such as associativity and unit 1∈A0.
All the dg algebras in this paper will be commutative, in the sense that:
(10.2) a·a′ = (−1)(dega)(dega′)a′·a ∀a,a′∈A•
We will write H0(A) for the 0–th cohomology of A•, which is a usual commutative algebra.
All the dg algebras studied in this paper will be ﬁnitely generated overH0(A).
Deﬁnition 10.2. A dg moduleM• for a dg algebraA• is a dg vector spaceM• with a map:
A•⊗M•−→M•
which is associative, preserves the grading, and satisﬁes the graded Leibniz rule (i.e. (10.1)
witha′ replaced bym). Note that all the cohomologiesHi(M•) are modules forH0(A•).
72 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
When the grading will not be particularly crucial, we may simplify notation by writingA =
A• andM =M•. We will only studied the derived categoryA–modules:
A–Mod =
{
dg modulesM ↶A
}
/quasi–isomorphism
When the dg algebra A is ﬁnitely generated over H0(A), we will call an object of A–Mod
ﬁnitely presented if all its cohomologies have this property overH0(A). Then we write:
A–mod⊂A–Mod
for the full subcategory of ﬁnitely presented modules. The category of dg modules behaves
much like that of usual modules, but with certain particular features. First of all is the existence
of the grading shift:
M•[1] =M•+1
Given two A–modules M and M′, one can deﬁne the space of degree preserving homomor-
phisms between them as HomA(M,M′). But it is more naturally to consider instead:
(10.3) Hom•
A(M,M′) =
⨁
n∈Z
HomA(M,M′[n])
which is actually a dg vector space with respect to:
d(f) =d◦f− (−1)nf◦d ∀f :M→M′[n]
The spaces (10.3) make A–Mod andA–mod into dg categories, which just means a category
whose Hom spaces are dg vector spaces. We may inquire about the ordinary categories:
(10.4) H0(A–Mod) and H0(A–mod)
whose Hom spaces are, by deﬁnition, the 0–th cohomologies of (10.3). Because the zero–cycles
of (10.3) are degree and differential preserving mapsf :M→M′, while the zero–boundaries
are homotopies between such maps, we conclude that (10.4) is nothing but the homotopy cate-
gory ofA–modules. So the dg categoryA–mod supersedes the homotopy category.
