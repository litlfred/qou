---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-003-4-the-symmetric-case-of-degree-8
section_title: "The symmetric case of degree 8"
section_number: 4
pages: 7-8
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 0.878
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
\label{sec-degree8}
\setcounter{equation}{0}

In this section we prove the computability of the set ${\E}_{8}^{m,s}$ of 
symmetric rational functions with denominator of degree $8$ and establish an 
explicit formula for the integral 
\ba
N_{n,8}(a_{1},a_{2};m) & = & \int_{0}^{\infty} 
\frac{z^{2n} \; dz} { (z^{8} + a_{2} z^{6} + 2a_{1}z^{4} + a_{2}z^{2} 
+ 1)^{m+1} } \nn
\ea
\no
where $0 \leq n \leq 4m+3$ is required for convergence. Observe that 
(\ref{symrule}) reduces the discussion to the case  $0 \leq n \leq 2m+1$. 
The expression (\ref{ep}), with $p=2$,  produces
$E_{2}(a_{1},a_{2};z) = (1 + a_{1} + a_{2}) z^{4} + 2(a_{2} + 4)z^{2} + 8$. 

\begin{Thm}
\label{thmsym8}
Every function in ${\E}_{8}^{m,s}$ is computable. More specifically, define
$c_{1} := a_{2} + 4, \; c_{2} := 1 + a_{1} + a_{2}$, and
\ba
t_{k,j}(m,n;a_{1},a_{2}) & := &  \pi  2^{-(3m+2+k+j)/2} 
c_{2}^{(m-k-j)/2} (c_{1} + \sqrt{8c_{2}})^{j-m-1/2} \times  \nn \\
 & \times & \binom{4m-n-k+2}{k-n} \binom{2m-2j}{m-j} \binom{m-k+j}{2j}
\binom{2j}{j} \binom{m}{j}^{-1}. \nn
\ea
\no
Then for $m+1 \leq n \leq 2m+1, \; 1+a_{1}+a_{2} > 0$ and 
$a_{2}+4 > -8\sqrt{8(1+a_{1}+a_{2})}$, 
\ba
\int_{0}^{\infty} \frac{z^{2n} \; dz}{(z^{8} + a_{2}z^{6} + 2a_{1}z^{4} +
a_{2} z^{2} + 1)^{m+1} } & = & 
\sum_{k=n}^{2m+1} \sum_{j=0}^{k-m-1} t_{k,j}(m,n;a_{1},a_{2}), \nn
\ea
\no
and for $0 \leq n \leq m$, 
\ba
\int_{0}^{\infty} \frac{z^{2n} \; dz}{(z^{8} + a_{2}z^{6} + 2a_{1}z^{4} +
a_{2} z^{2} + 1)^{m+1} }  = \nn \\
\sum_{k=n}^{m} \sum_{j=0}^{m-k} t_{k,j}(m,n;a_{1},a_{2}) +
\sum_{k=m+1}^{2m+1} \sum_{j=0}^{k-m-1} t_{k,j}(m,n;a_{1},a_{2}). \nn
\ea
\end{Thm}
\begin{proof}
The reduction formula yields 
\ba
\int_{0}^{\infty} \frac{z^{2n} \; dz}{(z^{8} + a_{2}z^{6} + 2a_{1}z^{4} +
a_{2} z^{2} + 1)^{m+1} }  = \nn \\
2^{3m+2} \sum_{k=n}^{2m+1} 2^{-2k} \binom{4m-n-k+2}{k-n} 
\int_{0}^{\infty} \frac{ z^{2k} \; dz}{ (c_{2} z^{4} + 2c_{1} z^{2} + 8)^{m+1} 
}. \label{label1}
\ea
\no
We then use Corollary \ref{cor62} to evaluate (\ref{label1}). 
\end{proof}
