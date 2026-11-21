---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-028-47-a-note-on-modularity
section_title: "A note on modularity"
section_number: 4.7
pages: 57-58
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.936
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.mod}

Modular forms at roots of unity give rise to special elements associated to torsion
classes in $K_3$. We will consider two simple examples: one coming from a quadratic
Gauss sum (and hence related to the asymptotics of Jacobi $\th$-series) and the other
related to the Roger-Ramanujan functions, which are well known to be modular.

\begin{example}[A quadratic Gauss sum]
Consider
\be
\begin{aligned}
F_{m}(x)&\=\frac{1}{m}\bigg(\sum_{k\in\BZ/m\BZ}\z_m^{k^2}\bigg)
\bigg(\sum_{k\in\BZ/m\BZ}\z_m^{-k^2}\bigg)
\= \frac{1}{2}(1+\z_4^{m})(1+\z_4^{-m})\\
&\=
\left\{
\begin{array}{cl}
1 & \text{if }m\equiv 1\pmod{4}\,,\\
0 & \text{if }m\equiv 2\pmod{4}\,,\\
1 & \text{if }m\equiv 3\pmod{4}\,,\\
2 & \text{if }m\equiv 4\pmod{4}\,.
\end{array}
\right.
\end{aligned}
\ee
We see that this gives an almost trivial element of the Habiro ring
$\calH_{\BZ[1/2]}$. We can also consider
\be
G_{m}(x)\=\frac{\z_4}{m}\bigg(\sum_{k\in\BZ/m\BZ}\z_m^{k^2}\bigg)^2
\= \frac{1}{2}(1+\z_4^{m})^2
\=
\left\{
\begin{array}{cl}
i & \text{if }m\equiv 1\pmod{4}\,,\\
0 & \text{if }m\equiv 2\pmod{4}\,,\\
-i & \text{if }m\equiv 3\pmod{4}\,,\\
2 & \text{if }m\equiv 4\pmod{4}\,,
\end{array}
\right.
\ee
giving a slightly less trivial element of $\calH_{\BZ[i,1/2]}$.
\end{example}

\begin{example}[Rogers-Ramanujan symmetrised]
The Rogers-Ramanujan function has an associated field $\BQ(\sqrt{5})$, which has an
abelian Galois group over $\BQ$. Consider
\be
J(z,q) \= \sum_{k=0}^{\infty}\frac{q^{k(k+1)}z^{2k}}{(qz;q)_{k}}
\inn \calH_{\BQ(z)}\,.
\ee
This $J$ has the special property that
\be
J(z,\z_m(1-u)) \inn \BZ[z,(1-z^m-z^{2m})^{-1}][\z_m]\llbracket u\rrbracket\,.
\ee
We define for $\xi^{2}+\xi-1=0$
\be
F_{m}(u) \= \sum_{\th^{m}=\xi} \Res{z=\th} J(z,\z_m(1-u))\frac{dz}{z}\,.
\ee
Each $F_m(u)$ in $\BQ(\sqrt{5},\z_m)$ is constant, the first five values being:
\be
\begin{small}
\begin{aligned}
F_{1}(u)
&\=-\frac{1}{2}-\frac{\sqrt{5}}{10}\,,\qquad\qquad\qquad\qquad
F_{2}(u)
&\=-\frac{1}{2}+\frac{\sqrt{5}}{10}\,,\\
F_{3}(u)
&\=-\frac{1}{2}+\frac{\sqrt{5}}{10}\,,\qquad\qquad\qquad\qquad
F_{4}(u)
&\=-\frac{1}{2}-\frac{\sqrt{5}}{10}\,,\\
F_{5}(u)
&\=\frac{\sqrt{5}}{5}\z_5^3 + \frac{\sqrt{5}}{5}\z_5^2 -\frac{1}{2}
+\frac{\sqrt{5}}{10}\,.
\end{aligned}
\end{small}
\ee
Note that, depending on the embeddings, $F_5(u)$ is equal to either $0$ or $-1$ in
$\BC$. In fact, using the modularity of the Rogers-Ramanujan functions, one can show
that
\be
-5F_{m}^{2}(u)-5F_{m}(u)
\=
\bigg\{
\begin{array}{cl}
1 & \text{if }(m,5)\=1\,,\\
0 & \text{otherwise}\,,
\end{array}
\ee
the expressions on either side being the value at $\z_m(1-u)$ of an element of
$\calH_{\BZ[1/5]}$. More generally, $\calH_{\BZ[1/5]}$ contains an element $\chi_N$
sending $\z_m$ to $\delta_{v_{5}(m),N}$.  These elements can be constructed using the
operation $f(q)\mapsto f(q^5)$ --- which does act on
the usual Habiro ring of~$\BZ$. Note
that the operation $f(q)\mapsto f(q^k)$ is in general only defined
on the Habiro
ring of a ring $R$ if it contains $1/k$. For example for $k=2$ we see that
$f((1-u)^2)=f((-(1-u))^2)$ and hence the re-expansion will not require a Frobenius
$\varphi_2$, which it should.)

This example illustrates how the different roots of unity can be disconnected
by denominators. This viewpoint will be pushed further in the next section; where
it will be used to give an alternative approach to the Habiro ring of a number field.
\end{example}
