---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-020-35-on-the-ohtsuki-series-at-roots-of-unity
section_title: "On the Ohtsuki series at roots of unity"
section_number: 3.5
pages: 14-15
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.929
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
\label{Oht}
 Suppose $M$ is a rational
homology 3--sphere with $|H_1(M,\Z)|=b$.
By Theorem \ref{main}, for any root of unity $\xi$ of order $pr$
$$\tau'_M(\xi)\in \Z[1/b][e_{pr}] \simeq \frac{\Z[1/b,e_r][x]}{(f_p(x+e_r))}\; .$$ where
\[
f_p(t):= \frac{t^p - e_r^p}{t-e_r}.
\]
Hence we can write
\be\label{Ohtsuki}
\tau'_M(e_{r}e_{p})= \sum_{n=0}^{p-2} a_{p,n} x^n
\ee
where  $a_{p,n}\in \Z[1/b,e_r]$.
The following proposition proven in \cite{BBL}
shows that the coefficients $a_{p,n}$
stabilize as $p\to \infty$.
\begin{proposition}{\rm [Beliakova--B\"uhler--Le]}
\label{main-cor1} Suppose $M$ is a
rational homology 3--sphere with $|H_1(M,\Z)|=b$, and $r$ is an odd
positive integer.
For every non--negative integer $n$,
there exists a unique invariant $a_n= a_n(M) \in \Z[1/b,e_r]$ such that
for every prime $p > \max (b,r)$,
 we have
\begin{equation}
a_n\equiv a_{p,n} \pmod p\;\;\; \text{in $ \Z[1/b,e_r]$ for} \;\;\;
0\le n \le  p-2.
\label{5501}
\end{equation}
Moreover, the formal series $\sum_{n} a_n (q-e_r)^n$ is equal to the Taylor
 expansion of the unified invariant $I_M$ at $e_r$.
\end{proposition}
