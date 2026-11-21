---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-000-1-introduction-and-statement-of-main-results
section_title: "Introduction and statement of main results"
section_number: 1
pages: 1-1
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 9 sections: Front matter; Introduction and statement of main; The Hecke algebra and permutation"
---
The irreducible representations of the symmetric groups and their
Iwahori-Hecke algebras have been classified and constructed by
James~\cite{James:SnIrr} and Dipper and James~\cite{DJ:reps}, yet
simple properties of these modules, such as their dimensions, are
still not known. Every irreducible representation of these algebras is
constructed by quotienting out the radical of a bilinear form on a
particular type of module, known as a Specht module. The bilinear
forms on the Specht modules are the objects of our study.  

One way of determining the dimension of the simple modules would be to
first find the elementary divisors of its Gram matrix over
$\Z[q,q^{-1}]$ and then specialize. This would also give the
dimensions of the subquotients of the Jantzen filtrations of the
Specht modules over an arbitrary field; see \cite{JM:Jantzen}.  In
general, such an approach is not possible because, as Andersen has
shown, Gram matrices need not be diagonalizable over $\Z[q,q^{-1}]$;
see~\cite[Remark~5.11]{Andersen:Tilting}. We also give some examples
of non--diagonalizable Specht modules in section~\ref{SecCounterEx}.

Let $G(\lambda)$ be the Gram matrix of the Specht module $S(\lambda)$.
Then the first result in this paper shows that $G(\lambda)$ is
diagonalizable if and only if $G(\lambda')$ is diagonalizable,
where~$\lambda'$ is the partition conjugate to $\lambda$. Moreover, if
$G(\lambda)$ is divisibly diagonalizable (that is, $G(\lambda)$ is
equivalent to a diagonal matrix $\diag(d_1,\dots,d_m)$ such that $d_i$
divides~$d_{i+1}$, for $1\le i<m$), then so is $G(\lambda')$. In this
case we can speak of elementary divisors and we show how the
elementary divisors of $G(\lambda)$ and $G(\lambda')$ determine each
other. This is a $q$--analogue of the corresponding result for the
symmetric group~\cite{KN}.

We next consider the elementary divisors for the hook partitions. We
show that when $\lambda = (n-k,1^k)$, for $0\le k<n$, the Gram matrix
$G(\lambda)$ is always divisibly diagonalizable over $\Z[q,q^{-1}]$,
and we determine the elementary divisors. Again, this is a
$q$--analogue of the corresponding result for the symmetric
groups~\cite{KN}, however, the proof in the Hecke algebra case is more
involved and requires some interesting combinatorics.
