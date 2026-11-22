---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-001-11-complex-convergence-and-interpretation-of-the
section_title: "Complex convergence and interpretation of the residue"
section_number: 1.1
pages: 3-5
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.954
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
\label{subsec:brisesymm}
We consider again a sequence of real-valued random variables $(X_n)_{n \in \N}$, but this time we assume that their Laplace transforms $\esper[\E^{zX_n}]$ are convergent in an open disk of radius $c>0$. In this case, they are automatically well-defined and holomorphic in a band of the complex plane $\mathcal{B}_c = \{z \in \CC,\,\,|\mathrm{Re}(z)|<c\}$ (see \cite[Theorem 6]{LS52}, and \cite{Ess45} for a general survey of the properties of Laplace and Fourier transforms of probability measures).\medskip

\begin{definition}\label{def:mod2}
The sequence $(X_n)_{n \in \N}$ is said to converge in the complex mod-Gaussian sense with parameters $t_n$ and limiting function $\psi$ if, locally uniformly on $\mathcal{B}_c$,
$$\esper[\E^{z X_n}]\,\E^{-\frac{t_n\,z^2}{2}} = \psi(z) \,(1+o(1)),$$
where $\psi$ is a continuous function on $\mathcal{B}_c$ with $\psi(0)=1$. Then, one has in particular convergence in the sense of Definition \ref{def:mod}, with $\theta(t)=\psi(\I t)$.
\end{definition}

In this setting which is more restrictive than before, the residue $\psi$ has a natural interpretation as a measure of "breaking of symmetry" when one tries to push the estimates of the central limit theorem from the scale $\sqrt{t_n}$ to the scale $t_n$. The previously mentioned central limit theorem \eqref{eq:clt} tells us that:
$$\proba\!\left[ X_n \geq a\sqrt{t_n}\right] = \left(\frac{1}{\sqrt{2\pi}} \int_{a}^\infty \E^{-\frac{x^2}{2}}\,dx \right)(1+o(1))$$
for any $a \in \R$. In the setting of complex mod-Gaussian convergence, this estimate remains true with $a=o(\sqrt{t_n})$, so that if $\eps=o(1)$, then
\begin{align*}\proba\left[ X_n \geq \eps\, t_n\right] &=\left(\frac{1}{\sqrt{2\pi}} \int_{\eps \sqrt{t_n}}^\infty \E^{-\frac{x^2}{2}}\,dx \right)(1+o(1)),\\
&=\frac{\E^{-\frac{t_n \eps^2}{2}}}{\sqrt{2\pi t_n} \,\eps}\,(1+o(1))\quad\text{ if }1 \gg \eps \gg \frac{1}{\sqrt{t_n}}\,,
\end{align*}where the notation $a_n \gg b_n$ stands for $b_n=o(a_n)$.
Then, at scale $t_n$, the limiting residue $\psi$ comes into play, with the following estimate that holds without additional hypotheses than those in Definition \ref{def:mod2}:
\begin{equation}\forall x \in (0,c),\,\,\,\proba[X_n \geq xt_n] = \frac{\E^{-\frac{t_n x^2}{2}}}{\sqrt{2\pi t_n} \,x}\,\psi(x)\,(1+o(1)),
\label{eq:upbound}
\end{equation}
the remainder $o(1)$ being uniform when $x$ stays in a compact set of $\R_+^*\cap(0,c)$. This estimate of positive large deviations has the following counterpart on the negative side:
$$\forall x  \in (0,c),\,\,\,\proba[X_n \leq -xt_n] = \frac{\E^{-\frac{t_n x^2}{2}}}{\sqrt{2\pi t_n} \,x}\,\psi(-x)\,(1+o(1)).$$
So for instance, if $(Y_n)_{n \in \N}$ is a sequence of i.i.d.~random variables with convergent moment generating function, mean $0$, variance $1$ and third moment $\esper[Y]>0$, then $X_n=\frac{1}{n^{1/3}}\sum_{i=1}^n Y_i$ converges in the \emph{complex} mod-Gaussian sense with parameters $n^{1/3}$ and limiting function $\psi(z)=\exp(\esper[Y^3]\,z^3/6)$, and therefore for $x>0$,
$$\proba\!\left[\sum_{i=1}^n Y_i \geq xn^{2/3}\right] = \proba\!\left[\mathcal{N}(0,1)\geq xn^{1/6}\right]\,\,\exp\!\left(\frac{\esper[Y^3]\,x^3}{6}\right)\,(1+o(1)).$$
Thus, at scale $n^{2/3}$, the fluctuations of the sum of i.i.d.~random variables are no more Gaussian, and the residue $\psi(x)$ measures this "breaking of symmetry": in the previous example, it makes moderate deviations on the positive side more likely than moderate deviations on the negative side, since $\psi(x)>1>\psi(-x)$ for $x>0$. \bigskip

\begin{remark}
The problem of finding the normality zone, i.e. the scale up to which the central limit theorem is valid, is a known problem in the case of i.i.d. random variables (see \emph{e.g.} \cite{IL71}). The description of the "symmetry breaking" is new and moreover the mod-Gaussian framework covers many examples with dependent  random variables (see also \cite{FMN13} for more examples). 
\end{remark}

Thus, the observation of large deviations of the random variables $X_n$ provides a first probabilistic interpretation of the residue $\psi$ in the deconvolution of a sequence of characteristic functions of random variables by a sequence of large Gaussian variables. In Section \ref{sec:l1}, we shall provide another interpretation of $\psi$, which is inspired by some classical results from statistical mechanics (\emph{cf.} \cite{EN78,ENR80}).
\medskip
