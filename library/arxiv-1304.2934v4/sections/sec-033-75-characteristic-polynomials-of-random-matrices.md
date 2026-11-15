---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-033-75-characteristic-polynomials-of-random-matrices
section_title: "Characteristic polynomials of random matrices in a compact Lie group"
section_number: 7.5
pages: 61-64
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.83
latex_coverage_ratio: 0.953
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:rmtpol}
Introduce the classical compact Lie groups of type $\mathrm{A}$, $\mathrm{C}$, $\mathrm{D}$:
\begin{align*}
\mathrm{U}(n)&=\{g \in \mathrm{GL}(n,\C)\,\,|\,\,gg^{\dagger}=g^{\dagger}g=I_{n}\}\qquad\qquad\quad\,\,\,\,\,\,\text{(unitary group)}\\
\mathrm{USp}(n)&=\{g \in \mathrm{GL}(n,\mathbb{H})\,\,|\,\,gg^{\star}=g^{\star}g=I_{n}\}\qquad\qquad\quad\,\,\,\,\,\text{(compact symplectic group)}\\
\mathrm{SO}(2n)&=\{g \in \mathrm{GL}(2n,\R)\,\,|\,\,gg^{t}=g^{t}g=I_{2n} \,\,;\,\,\det g =1\}\quad\text{(special orthogonal group)}
\end{align*}
where for compact symplectic groups $g^{\star}$ denotes the transpose conjugate of a quaternionic matrix, the conjugate of a quaternionic number $q=a+\I b+\mathrm{j} c+\mathrm{k} d$ being $q^{\star}=a-\I b-\mathrm{j} b- \mathrm{k}d$. In the following we shall consider quaternionic matrices as complex matrices of size $2n \times 2n$ by using the map
$$
a+\I b+\mathrm{j} c+\mathrm{k} d \mapsto \begin{pmatrix} a+\I b & c+\I d \\ -c + \I d & a-\I b\end{pmatrix}.
$$
The eigenvalues of a matrix $g \in G=\mathrm{SO}(2n) \text{ or }\mathrm{U}(n)\text{ or }\mathrm{USp(n)}$ are on the unit circle $\mathbb{S}^{1}$, and the value of the characteristic polynomial $\det(1-g)$ factorizes as
$$\det(1-g) = \prod_{i=1}^n (1-\E^{\I \theta_i}) $$
if $G=\mathrm{U}(n)$ and $\mathrm{Sp}(g) = (\E^{\I \theta_1},\ldots,\E^{\I \theta_n})$, and
$$\det(1-g) = \prod_{i=1}^{n} (1-\E^{\I\theta_i})(1-\E^{-\I\theta_i}) = \prod_{i=1}^n |1-\E^{\I\theta_i}|^2 $$
if $G=\mathrm{SO}(2n)$ or $\mathrm{USp}(n)$ and $\mathrm{Sp}(g) = (\E^{\I \theta_1},\E^{-\I \theta_1},\ldots,\E^{\I \theta_n},\E^{-\I\theta_n})$.
We define
\[Y_{n}^{\mathrm{A},\mathrm{C},\mathrm{D}}=
\begin{cases}
    \Re \big[ \log\det(1-g) \big] & \text{ in type $\mathrm{A}$;}\\
    \log\det(1-g) & \text{ in types $\mathrm{C}$ and $\mathrm{D}$.}
\end{cases}\]
An exact formula for the Laplace transform of $\log \det(1-g)$, and the corresponding asymptotics have been given in \cite{KS2,KS1,HKO01}, see also \cite[Sections 3 and 4]{KN12}. Hence, in type A,
$$\esper\!\left[\E^{z_1\,\Re(\log \det(1-g)) +z_2\,\mathrm{Im}(\log \det(1-g))}\right] = \prod_{j=1}^n \frac{\Gamma(j)\,\Gamma(j+z_1)}{\Gamma(j+\frac{z_1+\I z_2}{2}) \,\Gamma(j+\frac{z_1-\I z_2}{2} )}$$
for every $z_1$ with $\Re(z_1)>-1$, and every $z_2 \in \C$ (see \emph{e.g.} \cite[Formula (71)]{KS1}. In particular, if $\Re(z)>-1$, then
\begin{align*}
\esper\!\left[\E^{z Y_n^{\mathrm{A}}}\right] &= \prod_{j=1}^n \frac{\Gamma(j)\,\Gamma(j+z)}{\Gamma(j+\frac{z}{2})^2} \\
&= \frac{G(1+\frac{z}{2})^2}{G(1+z)}\,n^{\frac{z^2}{4}}\,(1+o(1)).
\end{align*}
Here $G$ denotes Barnes' $G$-function, which is the entire solution of the functional equation $G(z+1)=\Gamma(z)\,G(z)$ with $G(1)=1$. To go from the exact formula with ratios of Gamma functions, to the asymptotic formula with Barnes' functions, one has to interpret the formula as a Toeplitz determinant with one Fisher-Hartwig singularity, see the details in the aforementioned paper \cite{KN12} (the arguments therein apply \emph{mutatis mutandi} to the case of a complex random variable in the Laplace transform $z$, since the exact formula holds as long as $\Re(z)>-1$, and the theory of Toeplitz determinants works from the outset with complex functions). Therefore, $(Y_n^{\mathrm{A}})_{n \in \N}$ converges in the mod-Gaussian sense with parameters $t_n=\frac{\log n}{2}$, limiting function
$$\psi^{\mathrm{A}}(z)= \frac{G(1+\frac{z}{2})^2}{G(1+z)},$$
and on the band $\mathcal{S}_{(-1,+\infty)}$.\bigskip


Similarly, in type $\mathrm{C}$ and $\mathrm{D}$, one has the exacts formulas
\begin{align*}
\esper\!\left[\E^{zY_n^{\mathrm{C}}}\right] &= 2^{2n\,z}\,\prod_{j=1}^n \frac{\Gamma(j+n+1)\,\Gamma(z+j+\frac{1}{2})}{\Gamma(j+\frac{1}{2})\,\Gamma(z+j+n+1)}\quad\text{for }\Re(z)>-\frac{3}{2};\\
\esper\!\left[\E^{zY_n^{\mathrm{D}}}\right] &= 2^{2n\,z}\,\prod_{j=1}^n \frac{\Gamma(j+n-1)\,\Gamma(z+j-\frac{1}{2})}{\Gamma(j-\frac{1}{2})\,\Gamma(z+j+n-1)}\quad\text{for }\Re(z)>-\frac{1}{2}
\end{align*}
as well as the asymptotic formulas
\begin{align*}
\esper\!\left[\E^{zY_n^{\mathrm{C}}}\right] &= \left(\frac{\pi n}{2}\right)^{\frac{z}{2}}\,\left(\frac{n}{2}\right)^{\frac{z^2}{2}}\,\frac{G(\frac{3}{2})}{G(\frac{3}{2}+z)}\,(1+o(1));\\
\esper\!\left[\E^{zY_n^{\mathrm{D}}}\right] &= \left(\frac{8\pi}{n}\right)^{\frac{z}{2}}\,\left(\frac{n}{2}\right)^{\frac{z^2}{2}}\,\frac{G(\frac{1}{2})}{G(\frac{1}{2}+z)}\,(1+o(1))
\end{align*}
which hold in the same range for $z$, locally uniformly. Therefore, setting
\begin{align*}
X_n^{\mathrm{C}} &= Y_n^{\mathrm{C}} - \frac{1}{2}\,\log \frac{\pi n}{2} \\
X_n^{\mathrm{D}} &= Y_n^{\mathrm{D}} - \frac{1}{2}\,\log \frac{8\pi}{n}
\end{align*}
then $(X_n^{\mathrm{C}})_{n \in \N}$ and $(X_n^{\mathrm{D}})_{n \in \N}$ converges in the mod-Gaussian sense, with parameters $t_n = \log \frac{n}{2}$, limiting functions
$$\psi^{\mathrm{C}}(z)= \frac{G(\frac{3}{2})}{G(\frac{3}{2}+z)}\quad\text{and}\quad \psi^{\mathrm{D}}(z)= \frac{G(\frac{1}{2})}{G(\frac{1}{2}+z)}, $$
and respectively on $\mathcal{S}_{(-\frac{3}{2},+\infty)}$ and on $\mathcal{S}_{(-\frac{1}{2},+\infty)}$.
\bigskip

Now, our large deviation theorems apply and one obtains:

\begin{theorem}\label{thm:characteristicpolynomial}
Over $\mathrm{U}(n)$, one has:
\begin{align*}
\forall x>0,\,\,\,\proba_{n}\!\left[\,|\det(1-g)| \geq n^{\frac{x}{2}}\right]
&= \frac{G(1+\frac{x}{2})^{2}}{G(1+x)}\,\frac{1}{x\,n^{\frac{x^2}{4}}\, \sqrt{\pi \log n}}\, (1+o(1)); \\
\forall x \in (0,1),\,\,\,\proba_{n}\!\left[\,|\det(1-g)| \leq n^{-\frac{x}{2}}\right]
&= \frac{G(1-\frac{x}{2})^{2}}{G(1-x)}\,\frac{1}{x\,n^{\frac{x^2}{4}}\, \sqrt{\pi \log n}}\, (1+o(1)).
\end{align*}
Over $\mathrm{USp}(n)$, one has:
\begin{align*}
\forall x>0,\,\,\,\proba_{n}\!\left[\frac{\det(1-g)}{\sqrt{\frac{\pi}{2}}} \geq n^{\frac{1}{2}+x}\right] & = \frac{G(\frac{3}{2})}{G(\frac{3}{2}+x)}\frac{1}{x\,n^{\frac{x^{2}}{2}}\,2^{\frac{x^2+x}{2}}\,\sqrt{2\pi \log n}}\, (1+o(1));\\
\forall x\in \left(\!0\,,\frac{3}{2}\right)\!,\,\,\,\proba_{n}\!\left[\frac{\det(1-g)}{\sqrt{\frac{\pi}{2}}} \geq n^{\frac{1}{2}-x}\right] & = \frac{G(\frac{3}{2})}{G(\frac{3}{2}-x)}\,\frac{1}{x\,n^{\frac{x^{2}}{2}}\,2^{\frac{x^2-x}{2}}\,\sqrt{2\pi \log n}}\, (1+o(1)).
\end{align*}
Finally, over $\mathrm{SO}(2n)$, one has: 
\begin{align*}\forall x>0,\,\,\,\proba_{n}\!\left[\frac{\det(1-g)}{\sqrt{8\pi}} \geq n^{-\frac{1}{2}+x}\right] &= \frac{G(\frac{1}{2})}{G(\frac{1}{2}+x)}\,\frac{1}{x\,n^{\frac{x^{2}}{2}}\,2^{\frac{x^2-x}{2}}\,\sqrt{2\pi \log n}}\, (1+o(1));\\
\forall x\in \left(\!0\,,\frac{1}{2}\right)\!,\,\,\,\proba_{n}\!\left[\frac{\det(1-g)}{\sqrt{8\pi}} \leq n^{-\frac{1}{2}-x}\right] &= \frac{G(\frac{1}{2})}{G(\frac{1}{2}-x)}\,\frac{1}{x\,n^{\frac{x^{2}}{2}}\,2^{\frac{x^2+x}{2}}\,\sqrt{2\pi \log n}}\, (1+o(1)).
\end{align*}
\end{theorem}
\medskip

\begin{proof}
These are immediate computations by using Theorem \ref{thm:mainnonlattice}.
\end{proof}\bigskip

\begin{remark}
From Proposition \ref{prop:normalityzone}, one also gets normality zones for the random variables $X_n/\sqrt{t_n}$. On the other hand, the computations performed in the unitary case hint at a phenomenon of $2$-dimensional mod-Gaussian convergence for the complex numbers $\log \det(1-g)$, with $g \in \mathrm{U}(n)$. In \cite{Multidim}, we shall prove this rigorously, and compute various probabilistic consequences, for instance, estimates of large deviations for the random vectors $\log \det (1-g)$.
\end{remark}

\begin{remark}
The analogue of Theorem \ref{thm:characteristicpolynomial} in the setting of random matrices in the $\beta$-ensembles, or of general Wigner matrices, has been studied in the recent paper \cite{DE13}. They can be easily restated in the mod-Gaussian language, since their proofs rely on the computation of the asymptotics of the cumulants of the random variables $X_{n}=\log|\det M_{n}|$, with for instance $(M_{n})_{n \in \N}$ random matrices of the Gaussian unitary ensembles.
\end{remark}
\bigskip
\bigskip


















\section{\for{toc}{Mod-Gaussian convergence from a factorization of the PGF} \except{toc}{Mod-Gaussian convergence from a factorization\texorpdfstring{\\}{} of the probability generating function}}
\label{sec:zeros} 
Let $(X_n)_{n \in \N}$ be a sequence of bounded random variables with nonnegative integer values such that $\sigma_n^2:=\Var(X_n)$ tends to infinity. Denote $P_n(t)= \esper[t^{X_n}]$ the {\em probability generating function} of $X_n$.  Each $P_n(t)$ is a polynomial in $t$. Then, it is known that a sufficient condition so that $X_n$ is asymptotically Gaussian is that $P_n(t)$ has negative real roots (see references below). In this section, we prove that if the third cumulant $L_n^3:=\kappa^{(3)}(X_n)$ also tends to infinity such that $L_n=o(\sigma_n)$, then a suitable renormalized version of $X_n$ converges in the mod-Gaussian sense. We then give an application for the number of blocks in a uniform set-partition of $[n]$.
\bigskip
