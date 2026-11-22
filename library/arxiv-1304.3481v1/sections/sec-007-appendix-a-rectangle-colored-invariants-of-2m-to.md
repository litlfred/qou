---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-Graded Colored Homology of Knots"
section_id: sec-007-appendix-a-rectangle-colored-invariants-of-2m-to
section_title: "Appendix A. Rectangle-colored invariants of (2,m) torus knots"
section_number: null
pages: 68-69
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.831
doc_brief: "Quadruply-Graded Colored Homology of Knots — We conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
As we use the quantum invariants of $(2,m)$ torus knots colored
by the representations labeled by the rectangular Young diagrams in many examples throughout the paper, we would like
to provide a reader with a handy formula for them.

Let us first recall the general formula for the colored invariants of torus knots \cite{LZ,RJ,stevan}. Define the coefficients $c_{\lambda,n}^{\mu}$ by the equation
\begin{equation}
s_{\lambda}(x_1^n,x_2^n,\ldots)=\sum_{|\mu|=n|\lambda|}c_{\lambda,n}^{\mu}s_{\mu}.
\end{equation}
The $\lambda$-colored invariant of the $(n,m)$ torus knot can be expressed via the colored invariants of the unknot by the following formula (we omit an overall scaling factor):
\begin{equation}
\label{plethysm}
P^{\lambda}(T(n,m))=\sum_{|\mu|=n|\lambda|}q^{-\frac{m}{n}\kappa(\mu)}c_{\lambda,n}^{\mu}P^{\mu}(\unknot),
\end{equation}
where $\kappa(\mu)=\sum_{(i,j)\in \mu}(i-j)=\frac{1}{2}\sum_{j}\mu_j(\mu_j-2j+1)$ is the content of $\mu$.

Therefore to compute $P^{\lambda}(T(m,n))$, one just has to determine the
``plethysm'' coefficients $c_{\lambda,n}^{\mu}$.There is no closed formula for them  for general $\lambda,\mu$ and $n$. However, for $n=2$ and $\lambda=(S^{R})$, a simple formula for the coefficients $c_{\lambda,n}^{\mu}$ was found in \cite{CRemmel}.

A Young diagram $\mu=(\mu_1,\ldots,\mu_{2R})$ is called $(S,R)$--balanced, if
$$\mu_i+\mu_{2R+1-i}=2S\ \mbox{for all}\ 1\le i\le R$$
Balanced diagrams are in 1-to-1 correspondence with splittings of the $S\times R$ rectangle into pairs of complimentary diagrams, as shown
on Figure \ref{CRemmelfig}.

\begin{figure}[ht]
\begin{tikzpicture}
\draw (0,0)--(0,3)--(5,3)--(5,0)--(0,0);
\draw (0,3)--(0,6)--(2,6)--(2,5)--(3,5)--(3,4)--(4,4)--(4,3);
\draw (5,3)--(6,3)--(6,2)--(7,2)--(7,1)--(8,1)--(8,0)--(5,0);
\draw (6,1) node {$\alpha$};
\draw (1,4) node {$\beta$};
\draw (5,4)--(5,7)--(10,7)--(10,4)--(5,4);
\draw (6,7)--(6,6)--(7,6)--(7,5)--(8,5)--(8,4);
\draw (6,5) node {$\alpha$};
\draw (9,6) node {$\beta$};
\end{tikzpicture}
\caption{Diagram $\mu$ is balanced if diagrams $\alpha$ and $\beta$ fill the rectangle}
\label{CRemmelfig}
\end{figure}

For an $(S,R)$--balanced diagram $\mu$, let
${\rm sgn}(\mu)=(-1)^{|\beta|}=(-1)^{\sum_{i=1}^{R}\mu_i}$. Let $B(S,R)$ denote the set of  $(S,R)$--balanced diagrams. By \cite[Theorem 1]{CRemmel}, one has
$$s_{(S^R)}(x_1^2,x_2^2,\ldots)=\sum_{\mu\in B(S,R)}(-1)^{{\rm sgn}(\mu)}s_{\mu},$$
hence
\begin{equation}
\label{CRemmeleq}
c_{(S^R),2}^{\mu}=\begin{cases}(-1)^{{\rm sgn}(\mu)},\ \mbox{if}\ \mu\in B(S,R),\\ 0,\ \mbox{otherwise}\end{cases}.
\end{equation}
The equations (\ref{plethysm}) and (\ref{CRemmeleq}) determine the invariant $P^{(S^R)}(T(2,m))$ completely.
