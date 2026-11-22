---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-018-a-general-properties-of-determinantal-point-proc
section_title: "General properties of determinantal point processes"
section_number: A
pages: 35-36
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
processes
In this Appendix, we collected some necessary facts about determi-
nantal point processes, their correlation functions, Fredholm determi-
nants, and convergence of trace class operators.
Let X be a countable set, let Conf(X) = 2X be the set of subsets of
X and denote by Conf(X)0 ⊂Conf(X) the set of ﬁnite subsets of X.
We call elements of Conf(X) conﬁgurations. Let L be a kernel on X,
that is, a function on X × X also viewed as a matrix of an operator in
H = ℓ2(X).
By a determinantal point process on X (in [10] such processes are
called fermion point processes) we mean a probability measure on
Conf(X)0 such that
Prob(X) =
det

L(xi, xj)

xi∈X
det(1 + L)
,
X ∈Conf(X)0 .
Here the determinant in the numerator is the usual determinant of
linear algebra, whereas the determinant in the denominator is, in gen-
eral, a Fredholm determinant. Some suﬃcient conditions under which
det(1 + L) makes sense are described in the following subsection.
36
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
