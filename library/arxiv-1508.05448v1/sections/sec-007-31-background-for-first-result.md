---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-007-31-background-for-first-result
section_title: "Background for First Result"
section_number: 3.1
pages: 36-41
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.539
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
In a recent work of Chatterjee and Ledoux on concentration of measure for random submatrices [@ChatLed], it is proved that for an arbitrary Hermitian matrix of order $n$ and $k\leq n$ sufficiently large, the distribution of eigenvalues is almost the same for any principal submatrix of order $k$. Their proof uses the random transposition walk on the symmetric group $S_n$ and concentration of measure techniques. To further generalize their results, we observe that it is important to use a Markov chain which does not change too many matrix entries all at once and whose spectral gap is known. Instead of looking at a Markov chain on $S_n$, we first consider a Markov chain on the special orthogonal group $SO(n)$. $SO(n)$ is the group of $n\times n$ orthogonal matrices with determinant $1$. As a linear transformation, every element of $SO(n)$ is a rotation and preserves distances. We introduce Kac's walk on $SO(n)$ and demonstrate that it is sufficiently similar to the transposition Markov chain to allow for Chatterjee and Ledoux's results to carry over to the more general case of operator compressions. It should be noted that a similar result has been proved by Meckes and Meckes [@MeckesMeckes] using different techniques. In a more recent work [@MeckesMeckes2], Meckes and Meckes have extended their techniques to include several other classes of random matrices and prove almost sure convergence of the empirical spectral measure. The purpose of this paper is to highlight the fact that the methods of Chatterjee and Ledoux can be extended to include more general cases, provided the Markov chain used satisfies appropriate conditions. To emphasize this point, we also apply the method to get a concentration of measure result for a compression by a matrix of Gaussians using Kac's walk coupled to a thermostat. We also show an application of this method applied to the length of the longest increasing subsequence of a random walk evolving under the asymmetric exclusion process. The results of this section can be found in [@SNandMW].\
\
Following the notation of Chatterjee and Ledoux, for a given Hermitian matrix $A$ of order $n$, with eigenvalues given by $\lambda_1,\dots,\lambda_n$, we let $F_A$ denote the empirical spectral distribution function of $A$. This is defined as $$F_A(x):=\frac{\#\{i:\lambda_i\leq x\}}{n}$$
