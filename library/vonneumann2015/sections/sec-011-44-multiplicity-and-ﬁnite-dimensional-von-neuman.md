---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-011-44-multiplicity-and-ﬁnite-dimensional-von-neuman
section_title: "Multiplicity and ﬁnite dimensional von Neumann algebras."
section_number: 4.4
pages: 27-29
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
mann algebras.
Theorem 4.2.1 shows that type I factors on Hilbert space are completely
classiﬁed by two cardinalities (n1, n2) according to:
27
n1 = rank of a minimal projection in M, and
n2 = rank of a minimal projection in M ′.
We see that the isomorphism problem splits into “abstract isomorphism”
(determined by n2 alone), and “spatial isomorphism”, i.e. unitary equivalence.
A type In factor is by deﬁnition one for which n = n2.
It is abstractly
isomorphic to B(H) with dim H = n.
The integer n1 is often called the
multiplicity of the type I factor.
We will now determine the structure of all ﬁnite dimensional von Neu-
mann algebras quite easily. Note that in the following there is no requirement
that H be ﬁnite dimensional.
Theorem 4.4.1. Let M be a ﬁnite dimensional von Neumann algebra on
the Hilbert space H. Then M is abstractly isomorphic to ⊕k
i=1Mni(C) for
some positive integers k, n1, n2, ..., nk. (Mn(C) is the von Neumann algebra
of all n × n matrices on n-dimensional Hilbert space.) Moreover there are
Hilbert spaces Ki and a unitary u : ⊕iℓ2(Xi, Ki) →H (with |Xi| = ni) with
u∗Mu = ⊕iB(ℓ2(Xi)) ⊗1.
Proof. The centre Z(M) is a ﬁnite dimensional abelian von Neumann al-
gebra.
If p is a minimal projection in Z(M), pMp is a factor on pH.
The theorem follows immediately from theorem 4.2.1 and the simple facts
that Z(M) = ⊕k
i=1piC where the pi are the minimal projections in Z(M)
(two distinct minimal projections p and q in Z(M) satisfy pq = 0), and
M = ⊕ipiMpi.
The subject of ﬁnite dimensional von Neumann algebras is thus rather
simple. It becomes slightly more interesting if one considers subalgebras N ⊆
M. Let us deal ﬁrst with the factor case of this. Let us point out that the
identity of M is the same as that of N.
Theorem 4.4.2. If M is a type In factor, its type Im factors are all uniquely
determined, up to conjugation by unitaries in M, by the integer (or ∞)
k > 0 such that pMp is a type Ik factor, p being a minimal projection in
the subfactor N and mk = n.
Proof. Let N1 and N2 be type Im subfactors with generating s.m.u.’s {eij}
and {fij} respectively. If k is the integer (in the statement of the theorem)
for N1 then 1 = Pm
1 eii and each eii is the sum of k mutually orthogonal
minimal projections of M, hence n = mk. The same argument applies to
N2. Build a partial isometry u with uu∗= e11 and u∗u = f11 by adding
together partial isometries between maximal families of mutually orthogonal
projections less than e11 and f11 respectively. Then it is easy to check that
w = P
i ej1uf1j is a unitary with wfklw∗= ekl. So wN2w∗= N1.
28
Now we can do the general (non-factor) case. If N = ⊕n
i=1Mki(C) and
M = ⊕m
j=1Mrj(C) and N ⊆M as von Neumann algebras, let pj be minimal
central projections in M and qi be those of N. Then for each (i, j), pjqiMqipj
is a factor and pjqiN is a subfactor so we may form the matrix Λ = (λij)
where λij is the integer associated with pjqiN ⊆pjqiMqipj by theorem 4.4.2.
Exercise 4.4.3. Show that the integer λij deﬁned above is the following:
if ei is a minimal projection in the factor qiN, λij = trace of the matrix
pjei ∈MrjC.
Example 4.4.4. Let M = M5(C) ⊕M3(C) and N be the subalgebra of ma-
trices of the form:
 X 0 0
0 X 0
0
0 z

⊕( X 0
0 z )
where z ∈C and X is a 2×2 matrix. Then N is isomorphic to M2(C)⊕C
and if p1 = 1 ⊕0, q1 = 1 ⊕0, etc., we have
Λ = ( 2 1
1 1 ) .
The matrix Λ is often represented by a bipartite graph with the number
of edges between i and j being λij. The vertices of the graph are labelled by
the size of the corresponding matrix algebras. Thus in the above example
the picture would be:
This diagram is called the Bratteli diagram for N ⊆M.
Exercise 4.4.5. Generalise the above example to show that there is an in-
clusion N ⊆M corresponding to any Bratteli diagram with any set of di-
mensions for the simple components of N.
