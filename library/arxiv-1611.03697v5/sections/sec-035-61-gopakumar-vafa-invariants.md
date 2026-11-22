---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-035-61-gopakumar-vafa-invariants
section_title: "Gopakumar-Vafa invariants"
section_number: 6.1
pages: 29-30
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let $X$ be a smooth projective Calabi-Yau threefold. For the sake of notational simplicity we will assume that the group $H_2(X,\bZ)$ is torsion-free. The Gromov-Witten potential  of $X$ is a formal series
\begin{equation}
\label{help}F(x,\lambda)=\sum_{g\geq 0}\sum_{\beta\in H_2(X,\bZ)} \GW(g,\beta) \cdot x^\beta \cdot \lambda^{2g-2},\end{equation}
where $\GW(g,\beta)\in \bQ$ is the genus $g$ Gromov-Witten invariant for stable maps  of class $\beta\in H_2(X,\bZ)$. Note that by definition these invariants are nonzero only for  effective curve classes $\beta\geq 0$. The symbols $x^\beta$ are  formal variables  living in a suitable completion of the effective cone in the group ring of $H_2(X,\bZ)$, and  $\lambda$ is a formal parameter corresponding to the string coupling.

We can split the series \eqref{help} into contributions from constant and non-constant maps
\[F(x,\lambda)=F_0(x,\lambda)+F'(x,\lambda).\]
The contribution from the constant maps  \cite[Theorem 4]{FP} is
\begin{equation}
\label{cons}F_0(x,\lambda)=a_0(x) \lambda^{-2} +a_1(x) +\chi(X)\cdot \sum_{g\geq 2}  \frac{(-1)^{g-1}\cdot B_{2g}\cdot B_{2g-2}}{4g\cdot (2g-2)\cdot (2g-2)!}\lambda^{2g-2},\end{equation}
where the expressions $a_0(x)$ and $a_1(x)$ can be found for example in \cite{P}. Although the precise form of these expressions  will not be relevant here it is worth noting  that, unlike the higher genus terms, they involve the variables $x^\beta$.
Turning now to the contributions from non-constant maps, the Gopakumar-Vafa conjecture \cite{GV, P} claims that there exist integers  $\GV(g,\beta)\in \bZ$, such that
\[F'(x,\lambda)=\sum_{\beta> 0}\sum_{g\geq 0} \GV(g,\beta)\sum_{k\geq 1} \frac{1}{k} \,\Big(2\sin \Big( \frac{k\lambda}{2} \Big)\Big)^{2g-2} \, x^{k\beta}.\]

We will be particularly interested in the expression
\begin{equation}
\label{yp}\sum_{\beta>0}\GV(0,\beta)\sum_{k\geq 1} \frac{1}{k} \, \Big(2\sin \Big( \frac{k\lambda}{2} \Big)\Big)^{-2} \, x^{k\beta},\end{equation}
which gives the
contribution from genus 0 Gopakumar-Vafa invariants.
Note that using the Laurent expansion
\[(2\sin(s/2))^{-2} = \frac{1}{s^2}-\frac{1}{12}+ \sum_{g\geq 2} \frac{(-1)^{g-1} B_{2g}}{2g(2g-2)!} \cdot  s^{2g-2},\]
we can write the coefficient of $\lambda^{2g-2}$ in \eqref{yp} as
\begin{equation}
\label{blag}
\sum_{\beta>0} \GV(0,\beta) \cdot \frac{(-1)^{g-1} B_{2g}}{2g(2g-2)!} \cdot  \Li_{3-2g}(x^\beta),\end{equation}
at least  for $g\geq 2$.
