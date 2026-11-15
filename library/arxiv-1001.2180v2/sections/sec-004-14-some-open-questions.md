---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-004-14-some-open-questions
section_title: "Some open questions"
section_number: 1.4
pages: 4-5
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.986
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
### Precise behavior of the first line

Proposition [\[prop:SW_first_row\]](#prop:SW_first_row){reference-type="ref" reference="prop:SW_first_row"} (respectively Corollary [\[th:SW_lis_upbound\]](#th:SW_lis_upbound){reference-type="ref" reference="th:SW_lis_upbound"}) gives only an upper bound for the behavior of the first row of the diagrams (respectively the length of the longest non-decreasing subsequence of a random word). It would be nice to obtain the precise behavior (equivalent and perhaps fluctuation) of these random variables. If we follow [@Okounkov99], the first step is to study the asymptotic behavior of the observable $p_k$ with a parameter $k$ which also tends to infinity (as quickly as some power of $n$ for example). Such a result could be deduced from the expression of $p_\rho$ in terms of $\varSigma$'s (normalized characters), but unfortunately, equation ([\[eq:p_fct_sigma\]](#eq:p_fct_sigma){reference-type="ref" reference="eq:p_fct_sigma"}) is hard to invert.

### Concrete realization of power sums in the center of the symmetric group algebras

We will see in section [\[sect:observables\]](#sect:observables){reference-type="ref" reference="sect:observables"} that the relations between some functions on Young diagrams can be understood as relations in the center of the symmetric group algebras via the abstract Fourier transform. Therefore, if we want to understand better the expression of the $p_\rho$'s in terms of the $\varSigma$'s (and we would like to, see the first open problem!), one way to do it would be to describe in a nice way the image of the $p_\rho$'s by the abstract Fourier transform. One could also use the power sums of Jucys-Murphy elements which have a simple definition in $\mathbb{C}\mathfrak{S}_n$ and have the same top homogeneous component as the $p_\rho$ (with a shift of index and up to a multiplicative constant).

### Approximation by a sum of independant random vectors

It is interesting to note that the covariance matrix appearing in Theorem [\[th:second_order_as_rows\]](#th:second_order_as_rows){reference-type="ref" reference="th:second_order_as_rows"} is exactly the same as the one obtained by A. Borodin in a very different context (the limiting distribution of the sizes of the blocks of the Jordan form of a random upper triangular nilpotent matrix over a finite field, see [@Borodin:limitJordan]). In his paper, A. Borodin found this covariance matrix by approximating his random partition by a sum of independent random vectors. This suggests that the $q$-Plancherel measure could perhaps be approximated the same way. Such a result could be obtained by using the limit form of the diagrams (Theorem [\[th:first_order_as_rows\]](#th:first_order_as_rows){reference-type="ref" reference="th:first_order_as_rows"}) and computing the error on the corresponding transition probabilities. Unfortunately, the transition probabilities for the $q$-Plancherel measure (see Figure [\[qplancherelprocess\]](#qplancherelprocess){reference-type="ref" reference="qplancherelprocess"}) are hard to deal with and we do not know if this method would succeed in our context.
