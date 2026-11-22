---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-031-52-solution-in-the-doubled-a1-case
section_title: "Solution in the doubled A1 case"
section_number: 5.2
pages: 24-26
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.988
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
The formula
\begin{equation}
\label{cheedale}\Lambda(w)=\frac{e^w \cdot\Gamma(w)}{\sqrt{2\pi}\cdot w^{w-\half}}\end{equation}
defines a  meromorphic  function of $w\in \bC^*$, which is multi-valued due to the   factor
\[w^{w-\half}=\exp\big({(w-\half)\log w}\big).\]
Since $\Gamma(w)$ is meromorphic on $\bC$ with poles only at the non-positive integers, it follows that
$\Lambda(w)$ is holomorphic on $\bC^*\setminus\bR_{<0}$. We specify it uniquely by taking the principal branch of $\log$.

The Stirling expansion \cite[Section 12.33]{WW} gives an asymptotic expansion
\begin{equation}\label{stirling}\log \Lambda(w)
\sim  \sum_{g=1}^{\infty} \frac{B_{2g}}{2g(2g-1)}w^{1-2g},
\end{equation}
where $B_{2g}$ denotes the $(2g)$th Bernoulli number. This expansion is valid as $w\to \infty$ in the complement of a closed sector containing the ray  $\bR_{<0}$. It implies in particular that $\Lambda(w)\to 1$.


\begin{prop}
\label{twotier}
 When $\xi=1$, Problem \ref{eps} has a unique solution, namely 
\[\Psi_+(t)=\Lambda\Big(\frac{z}{2\pi i t}\Big), \qquad \Psi_-(t)=\Lambda\Big(\frac{-z}{2\pi i t}\Big)^{-1}.\]
\end{prop}

\begin{proof}
Note that the function $\Psi_+(t)$ is indeed holomorphic on the domain $\bC^*\setminus i\ell_+$  as required, because if we set $w=z/2\pi it$ then \[t\in i\ell_+ \iff w\in \bR_{<0}.\]
Similarly $\Psi_-(t)$ is holomorphic on $\bC^*\setminus i\ell_-$.

The
Euler reflection formula  gives
\[\Gamma(w)\cdot \Gamma(1-w) =\frac{\pi}{\sin(\pi w)},\quad w\in \bC\setminus\bZ.\]
Since $\Gamma(n)=(n-1)!$ for $n\in \bZ_{>0}$, it follows that  $\Gamma(w)$ is nowhere vanishing. The same is therefore true of  $\Lambda(w)$.
The reflection formula also implies that for $w\in \bC\setminus \bZ$
\[\Lambda(w)\cdot \Lambda(-w)=\frac{1}{2\pi}\cdot  \frac{\pi }{\sin(\pi w)}\cdot e^{-( (w-\half)\log(w)+(-w+\half)\log(-w))},\]
where we used $\Gamma(1-w)=(-w)\cdot \Gamma(-w)$.
For the principal branch of $\log$ we have \[\log(w)=\log(-w)\pm \pi i\text{ when }\pm \Im(w)>0.\]
Thus we conclude that
\begin{equation}
\label{luminy}\Lambda(w)\cdot \Lambda(-w)=\frac{i\cdot e^{-\pi i(w-\half)}} {e^{\pi iw}-e^{-\pi i w}}=(1-e^{2\pi iw})^{-1}\end{equation}
when $\Im(w)>0$.
Note that if $w=z/2\pi i t$ then \[ t\in \bH_{\ell_-}\iff \Im(w)>0,\]
so we get the second of the relations \eqref{rabbit}. The other follows in the same way.
Property (ii) is immediate from the Stirling expansion \eqref{stirling}. Property (iii) is a simple consequence of the fact that $\Gamma(w)$ has a simple pole at $w=0$. Finally, the uniqueness statement follows from Lemma \ref{brownpaperbag}.
\end{proof}
