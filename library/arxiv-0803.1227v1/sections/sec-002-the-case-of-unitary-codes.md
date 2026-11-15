---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-002-the-case-of-unitary-codes
section_title: "The case of unitary codes"
section_number: null
pages: 3-5
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.992
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
As a particular case we set $G=\U_n(\C)\times \U_n(\C)$ and $X=\U_n(\C)$. For $g=U\times V$ and $x=M$ we set $gx=UMV^{-1}$. In this context the orbit of a pair $(x,y)$ is characterized by the eigenvalues $(e^{i\theta_1},...,e^{i\theta_n})$ of the unitary matrix $xy^{-1}$. The Peter-Weil theorem gives a decomposition of $L^2(X)$ into irreducible subspaces $$\label{dec}
L^2(X)=\oplus (V_{\chi}\otimes V_{\conj{\chi}})$$ where the sum runs over all irreducible representations $V_{\chi}$ of $\U_n(\C)$. It is worth noticing that the $G$-subspaces $V_{\chi}\otimes V_{\conj{\chi}}$ are pairwise non isomorphic. From this decomposition one can deduce the following theorem :

::: proposition
The zonal functions associated to this decomposition are $$P_\chi(x,y)=\chi(xy^{-1})$$ where $\chi$ denotes any [irreducible character of]{.roman} $\U_n(\C)$.
:::

The irreducible characters of $\U_n(\C)$ are known to be finite dimensional and to have a nice description using Schur polynomials ([@FULTON]). We recall briefly some notations and definitions concerning those polynomials.

For any integer $k$, a partition of $k$ in $n$ parts is a finite decreasing sequence of $n$ non negative integers which sum exactly to $k$ ($k$ is also called the degree of the partition). A partition $\lambda$ is dominating $\mu$ (noted $\lambda \succ \mu$) if $\forall r\le n,\ \sum_{i=1}^r \lambda_i \ge \sum_{i=1}^r \mu_i$. Given a partition $\lambda=[\lambda_1,...,\lambda_n]$ we define the elementary symmetric polynomials $m_\lambda \in \Z[x_1,...,x_n]$ as the renormalization to a monic polynomial of $$\sum_{\sigma \in \mathfrak{S}_n}  x_{\sigma(1)}^{\lambda_1}x_{\sigma(2)}^{\lambda_2}...x_{\sigma(n)}^{\lambda_n}.$$ These polynomials form a basis of the set of symmetric polynomials $\Z[x_1,...,x_n]^{\textrm {Sym}}$. Schur polynomials have been intensively studied and have several definitions. For our purpose we will define the Schur polynomials $S_\lambda$ as $$S_\lambda = \sum_{\lambda \succ \mu} K_{\lambda,\mu} m_\mu,$$ where the $K_{\lambda,\mu} \in \N$ are the so called Kostka numbers. For more precision on those numbers see [@SAGAN]. It is clear that Schur polynomials form another basis of $\Z[x_1,...,x_n]^{\textrm {Sym}}$.

It is well known that the irreducible polynomial characters of $\U_n(\C)$ are expressed using Schur polynomials (we refer to [@FULTON] for details) in the following way: let $(e^{i\theta_1},...,e^{i\theta_n})$ denote the eigenvalues of a unitary matrix $M$, and $\lambda$ a partition. Then $$\chi_\lambda(M)=S_\lambda(e^{i\theta_1},...,e^{i\theta_n}).$$ One obtains all irreducible characters of $\U_n(\C)$ by multiplying the characters $\chi_{\lambda}$ by a relative power of $\det(M)=\prod
e^{i\theta_k}$. All together, we obtain the theorem:

::: theorem
For all partition $\lambda$ and $s\in \Z$, let $$\label{P1}
P_{\lambda,s}(x_1,\dots,x_n)=(x_1\dots x_n)^sP_{\lambda}(x_1,\dots, x_n).$$ These rational fractions give the zonal functions associated to the irreducible decomposition [\[dec\]](#dec){reference-type="eqref" reference="dec"} in the following way: if $\chi\simeq \det^s\otimes\lambda$, if the eigenvalues of $xy^{-1}$ are $(e^{i\theta_1},...,e^{i\theta_n})$, then $$P_{\chi}(x,y)=P_{\lambda,s}(e^{i\theta_1},...,e^{i\theta_n}).$$
:::

.

We are now almost ready to compute bounds for unitary codes $\Code \subset \U_n(\C)$. Let $$d_\Sigma^2(e^{i\theta_1},...,e^{i\theta_n}):=\frac{1}{2n} {\sum_{i=1}^n (1-\cos \theta_i)}$$ and $$d_\Pi^2(e^{i\theta_1},...,e^{i\theta_n}):=\frac{1}{2}  \left(\prod_{i=1}^n (1-\cos \theta_i) \right)^{\frac{1}{n}}.$$ and define $d_\Sigma^2(x,y)$ (resp. $d_\Pi^2(x,y)$) to be the above functions evaluated at the eigenvalues of $xy^{-1}$. These functions are related to the diversity sum and diversity product by $$\Sigma \Nu = \min_{\substack{x,y \in \Code\\x\ne y}} d_\Sigma(x,y) \textrm{ and }
 \Pi \Nu = \min_{\substack{x,y \in \Code\\x\ne y}} d_\Pi(x,y).$$ We recall that the orbit of a pair $(x,y)$ is characterized by the eigenvalues of $xy^{-1}$, so $d_\Sigma$ and $d_\Pi$ are constant on $G$-orbits. We may now define, with the notations of Section II, the sets $S$ related to each diversity function: $$S_\Sigma(\delta):=\{ (e^{i\theta_1},...,e^{i\theta_n}) :  d_\Sigma(e^{i\theta_1},...,e^{i\theta_n}) \ge \delta \}$$ $$S_\Pi(\delta):=\{ (e^{i\theta_1},...,e^{i\theta_n}) :  d_\Pi(e^{i\theta_1},...,e^{i\theta_n}) \ge \delta \}.$$
