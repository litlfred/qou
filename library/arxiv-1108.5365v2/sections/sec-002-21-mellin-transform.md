---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-002-21-mellin-transform
section_title: "Mellin transform"
section_number: 2.1
pages: 9-10
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.986
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:Pre:Mellin}
In this subsection, let us recall the Mellin transform of a function and its properties. 

\begin{Thm}Let $f(x)$ be a continuous function on the half line $0<x<\oo$. Then its Mellin transform is defined by
\Eq{\phi(s):=(\cM f)(s)=\int_0^\oo x^{s-1} f(x)dx,} whenever the
integration is absolutely convergent for $a<Re(s)<b$. By the Mellin
inversion theorem, $f(x)$ is recovered from $\phi(s)$ by
\Eq{f(x):=(\cM\inv\phi)(x)=\frac{1}{2\pi}\int_{c-i\oo}^{c+i\oo}x^{-s}\phi(s)ds,}
where $c\in\R$ is any values in between $a$ and $b$.
\end{Thm}

We have the following analyticity theorem \cite{PK}:
\begin{Thm}\label{MTpole}
(Strip of analyticity) If $f(x)$ is a locally integrable function on $(0,\oo)$ such that it has decay property:
\Eq{\label{growth}f(x)=\left\{\begin{array}{cc}O(x^{-a-\e})&x\to 0^+\\O(x^{-b+\e})&x\to +\oo \end{array}\right.} 
for every $\e>0$ and some $a<b$, then the Mellin transform defines an analytic function $(\cM f)(s)$ in the strip
$$a<Re(s)<b.$$

(Analytic continuation) Assume $f(x)$ behaves algebraically for $x\to 0^+$, i.e. 
\Eq{f(x)\sim \sum_{k=0}^\oo A_k x^{a_k},} 
where $Re(a_k)$ increases monotonically to $\oo$ as $k\to\oo$. Then the Mellin transform $(\cM f)(s)$ can be
analytically continued into $Re(s)\leq a=-Re(a_0)$ as a meromorphic function with simple poles at the points $s=-a_k$
with residue $A_k$.

A similar analytic property holds for the continuation to the right half plane.

(Growth) If $f(x)$ is a holomorphic function of the complex variable $x$ in the sector $-\a<\arg x<\b$ where
$0<\a,\b\leq \pi$, and satisfies the growth property \eqref{growth} uniformly in any sector interior to the above
sector, then $(\cM f)(s)$ has exponential decay in $a<Re(s)<b$ with
\Eq{(\cM f)(s)=\left\{\begin{array}{cc}O(e^{-(\b-\e)t})&t\to+\oo\\O(e^{(\a-\e)t})&t\to -\oo \end{array}\right.} 
for any $\e>0$ uniformly in any strip interior to $a<Re(s)<b$, where $s=\s+it$.

(Parseval's Formula) 
\Eq{\int_0^\oo f(x)g(x)x^{z-1}dx =\frac{1}{2\pi i}\int_{c-i\oo}^{c+i\oo} (\cM f)(s)(\cM g)(z-s)ds,} 
where $Re(s)=c$ lies in the common strip for $\cM f$ and $\cM g$. In
particular we have 
\Eq{\int_0^\oo |f(x)|^2 dx =\frac{1}{2\pi}\int_{-\oo}^\oo |(\cM f)(\frac{1}{2}+it)|^2dt.}
\end{Thm}
