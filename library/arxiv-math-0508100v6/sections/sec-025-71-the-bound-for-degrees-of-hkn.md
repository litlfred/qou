---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-025-71-the-bound-for-degrees-of-hkn
section_title: "The bound for degrees of HK,n"
section_number: 7.1
pages: 16-17
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.853
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
Note that
$$
\deg_\pm (fg) = \deg_\pm(f) + \deg_\pm(g),
\quad  \text{and} \quad \maxdeg(f+g) \le \max(\maxdeg(f), \maxdeg(g)).
$$
From $\deg_\pm \{k\} = \pm k/2$, we get
$$
\deg_\pm  (\{k\}!) = \pm k(k+1)/4,
\qquad \deg_\pm  (\qbinom{n}{k}) = \pm k(n-k)/2.
$$
From these and Equation \eqref{33} we get
$$
\maxdeg(H_{K,n}(q)) \le \max_{1\le k \le n+1 }
\left(  -\frac{(2n+2)(2n+3)}{4} + k +
\frac{k}{2}+ \frac{(n+1+k)(n+1-k)}{2} + \maxdeg (J_{K,k}) \right).
$$

Using Proposition \ref{21} for the upper bound of $\maxdeg
(J_{K,k})$, after a simplification, we get
$$
\maxdeg(H_{K,n}(q)) \le \max_{1\le k \le n+1 }
\left(  -\frac{n(n+3)}{2} + \frac{c (k-1)^2}{4} +
\frac{(k-1)s_+}{2} + \frac{|\w|(k^2-1)}{4}\right).
$$
The right hand side reaches maximum when $k=n+1$. Using $\w \le
c+2$,  we have
$$
\maxdeg(H_{K,n}(q)) \le n^2c/2 + n(s_+ +c-1)/2.
$$
A similar calculation shows that
$$
\mindeg(H_{K,n}(q)) \ge -( n^2c/2 + n(s_- +c-1)/2).
$$
If we choose $A_0$ bigger than  $c$ and $|s_\pm +c -1|$, then we
have $|\deg_\pm (H_{K,n}) |\le A_0 n^2$. This proves the first
statement of Theorem \ref{thm.boundC}.
