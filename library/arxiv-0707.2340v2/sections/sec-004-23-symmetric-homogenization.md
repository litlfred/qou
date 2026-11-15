---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-004-23-symmetric-homogenization
section_title: "Symmetric Homogenization"
section_number: 2.3
pages: 10-10
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.98
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s22}
We will now define a symmetric homogenization 
procedure for arbitrary measures in $\fP_n$. This natural construction 
proves to be quite useful for studying strongly Rayleigh measures 
(\S \ref{s-gar}).

\begin{definition}\label{d-sh}
Given a measure $\mu\in\fP_n$ define a new measure $\mu_{sh}\in\fP_{2n}$ 
called the {\em symmetric homogenization} of $\mu$ by
$$
\mu_{sh}(S) = 
\begin{cases}
\mu(S\cap[n])\binom{n}{|S\cap [n]|}^{-1} \mbox{ if } |S|=n, \\
0 \mbox{ otherwise. } 
\end{cases} 
$$
\end{definition}

Note that the generating polynomial of $\mu_{sh}$ may be written as
$$g_{\mu_{sh}}(z_1,\ldots,z_n,z_{n+1},\ldots,z_{2n})=
\sum_{S \subseteq [n]} \mu(S)\binom{n}{|S|}^{-1} z^S 
e_{n-|S|}(z_{n+1},\ldots, z_{2n}),
$$
where $z=(z_1,\ldots,z_n)$ and $e_k$, $0\le k\le n$, denotes the $k$-th 
elementary symmetric function. Clearly, $g_{\mu_{sh}}$ is symmetric in the 
variables $z_{n+1},\ldots,z_{2n}$ and $\mu_{sh}$ projects to $\mu$, that is,
$g_{\mu_{sh}}(z_1,\ldots,z_n,1,\ldots,1)=g_{\mu}(z_1,\ldots,z_n)$. It is not 
difficult to show that 
$g_{\mu_{sh}}$ is actually the unique polynomial
in $\PP_{2n}$ of total degree $n$ that is 
symmetric in $z_{n+1},\ldots,z_{2n}$ and satisfies the latter identity. 
Therefore, $\mu_{sh}$ is canonically 
determined by the aforementioned conditions.
