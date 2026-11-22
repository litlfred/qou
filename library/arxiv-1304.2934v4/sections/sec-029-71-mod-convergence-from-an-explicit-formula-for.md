---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-029-71-mod-convergence-from-an-explicit-formula-for
section_title: "Mod-convergence from an explicit formula for the Laplace transform"
section_number: 7.1
pages: 48-50
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.955
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:explicit}
Examples where mod-convergence is proved using an explicit formula for the Laplace transform were already given in Section \ref{subsec:basicexamples}. We provide here two additional examples of mod-Gaussian convergence that can be obtained by this method.

\begin{example}
    \label{ex:zeros_randomfunction}
Let $f(z)=\sum_{n=0}^\infty a_n\,z^n$ be a random analytic function, where the coefficients $a_n$ are independent standard complex Gaussian variables. The random function $f$ has almost surely its radius of convergence equal to $1$, and its set of zeroes $\mathcal{Z}(f)=\{z \in \mathcal{D}_{(0,1)}\,\,|\,\,f(z)=0 \}$ is a determinantal point process on the unit disk, with kernel 
$$\mathcal{K}(w,z)=\frac{1}{\pi(1-w\overline{z})^2}=\frac{1}{\pi}\sum_{k=1}^\infty k(w\overline{z})^{k-1}.$$
We refer to \cite{Zero} for precisions on these results. It follows then from the general theory of determinantal point processes, and the radial invariance of the kernel, that the number $N_r$ of points of $\mathcal{Z}(f) \cap B_{(0,r)}$ can be represented in law as a sum of independent Bernoulli variables of parameters $\{r^{2k}\}_{k \geq 1}$:
$$N_r=\mathrm{card}\{z \in \mathcal{Z}(f)\,\,|\,\,|z|\leq r\} =_{\text{law}} \sum_{k=1}^\infty\mathcal{B}(r^{2k}).$$
This representation as a sum of independent variables allows one to estimate the moment generating function of $N_r$ under various renormalizations. Let us introduce the hyperbolic area $$h=\frac{4\pi\,r^2}{1-r^2}$$ of $\mathcal{D}_{(0,r)}$, and denote $N_r=N^h$; we are interested in the asymptotic behavior of $N^h$ as $h$ goes to infinity, or equivalently as $r$ goes to $1$. Since $\esper[\E^{zN_r}]=\prod_{k=1}^\infty (1+r^{2k}(\E^z-1))$, one has
$$
\log \left(\esper\!\left[\E^{\frac{zN^h}{h^{1/3}}}\right]\right)=\sum_{k=1}^\infty \,\log\left(1+r^{2k}\left(\E^\frac{z}{h^{1/3}}-1\right)\right) =\frac{h^{2/3}z}{4\pi}+ \frac{h^{1/3}z^2}{16\pi}+\frac{z^3}{144\pi}+o(1)
$$
with a remainder that is uniform when $z$ stays in a compact domain of $\C$. Therefore, $$\frac{N^h-\frac{h}{4\pi} }{h^{1/3}}\,\text{ converges mod-Gaussian with }\begin{cases} &\!\!\text{parameters } t_h=\frac{h^{1/3}}{8\pi},\\
 &\!\!\text{limiting function }\psi(z)=\exp\left(\frac{z^3}{144\pi}\right). 
 \end{cases}$$
Again, the limiting function is the exponential of a simple monomial. By Proposition \ref{prop:normalityzone}, 
$$X^h = \frac{N^h - \frac{h}{4\pi}}{\sqrt{\frac{h}{8\pi}}}$$
converges as $h \to \infty$ to a Gaussian law, with normality zone $o(h^{1/6})$. Moreover, by Theorem \ref{thm:mainnonlattice}, at the edge of this normality zone,
$$\proba\!\left[N^h - \frac{h}{4\pi} \geq \frac{h^{2/3}}{4\pi}\,x\right] = \frac{\E^{-\frac{h^{1/3}\,x^2}{4\pi}}}{h^{1/6}\,x}\,\exp\left(\frac{x^3}{18\pi}\right)\,(1+o(1))$$
for any $x>0$.
\end{example}
\medskip

\begin{example}\label{ex:ising}
Consider the Ising model on the discrete torus $\Z/n\Z$. Thus, we give to each spin configuration $\sigma : \Z/n\Z \to\{\pm1\}$ a probability proportional to the factor $\exp(-\beta \sum_{i \sim j} \mathbbm{1}_{\sigma(i)\neq \sigma(j)})$, the sum running over neighbors in the circular graph $\Z/n\Z$. The technique of the transfer matrix (see \cite[Chapter 2]{Baxter82}) ensures that if $M_n=\sum_{i=1}^n \sigma(i)$ is the total magnetization of the model, then
$$\esper[\E^{zM_n}]=\frac{\mathrm{tr}\, (T(z))^n}{\mathrm{tr}\, (T(0))^n},\qquad\text{where }T(z)=\begin{pmatrix}\E^{-z} & \E^{z-\beta}\\
\E^{-z-\beta}&\E^z\end{pmatrix}.$$
The two eigenvalues of $T(z)$ are $\cosh z \pm \sqrt{(\sinh z)^2 +\E^{-2\beta}}$, and their Taylor expansion shows that
$$\log \left(\esper\!\left[\E^{\frac{zM_n}{n^{1/4}}}\right]\right)=\frac{\E^\beta\,n^{1/2}\,z^2}{2}-\frac{(3\E^{3\beta}-\E^\beta)\,z^4}{24}+o(1).$$
So, one has mod-Gaussian convergence for $n^{-1/4}\,M_n$, and the estimates
$$\proba[M_n \geq n^{3/4}x]=\frac{\E^{-\frac{n^{1/2}\,\E^\beta\,x^2}{2}}}{x\,\sqrt{2\pi n^{1/2}}}\,\exp\left(-\frac{(3\E^{3\beta}-\E^\beta)\,x^4}{24}\right)\,(1+o(1)).$$
In particular, $\frac{M_n}{n^{1/2}\,\E^{\beta/2}}$ satisfies a central limit theorem with normality zone $o(n^{1/4})$.
\end{example}
\medskip

\begin{remark}
If instead of $\Z/n\Z$ we consider the graph $1 \leftrightarrow 2 \leftrightarrow \cdots \leftrightarrow n$ (\emph{i.e.}, one removes the link $n \leftrightarrow 1$), then one can realize the spins $\sigma(i)$ of the Ising model as the $n$ first states of a Markov chain with space of states $\{\pm 1\}$. The magnetization $M_n$ appears then as a linear functional of the empirical measure of this Markov chain. More generally, if $S_n = \sum_{i=1}^n f(X_i)$ is a linear functional of a Markov chain on a finite space, then under mild hypotheses this sum satisfies the Markov chain central limit theorem (\emph{cf.} for instance \cite{Cog72}). In \cite{FMN14}, we shall use arguments of the perturbation theory of operators in order to prove that one also has mod-Gaussian convergence for such linear functionals of Markov chains.
\end{remark}
\bigskip
