---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-001-11-deforming-the-volume-of-a-three-manifold
section_title: "Deforming the volume of a three-manifold"
section_number: 1.1
pages: 2-4
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.938
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜no [9] that perturbative series associated with the hyperbolic knots 41 and 52 are resurgent and"
---
In this paper, we will consider a two parameter family of examples of asymptotic series similar to those that would come from a knot. These examples were considered in~\cite{GK:qser}. In particular, for some $A,B\in\BZ_{>0}$ with~$A\neq B$, we will consider the function
\be\label{eq:V}
  V:\Sigma\rightarrow\BC/\BZ
  \qquad\text{such that}\qquad
  V(z,m)\=B\frac{\Li_{2}(\e(z))}{(2\pi i)^2}+\frac{B}{24}+\frac{A}{2}z(z+1)+mz\,,
\ee
where $\e(z)=\exp(2\pi iz)$ and $\Sigma$ is the associated Riemann surface. In particular, $\Sigma$ is defined by taking points $p=(z,m)$ where $z\in\BC\backslash(\BZ-i\BR)$ and $m\in\BZ$ with the equivalences 
\be\label{eq:surface}
\begin{aligned}
(k+0+iy,m)&\sim(k-0+iy,m+B)\qquad\text{for }y<0\,,\;k\in\BZ\,,\\
(z,m+A)&\sim(z+1,m)\,.
\end{aligned}
\ee
Given the second equivalence relation, we can always represent points $p\in\Sigma$ as $p=(z,m)$ with $m=0,\cdots,A-1$. The critical points of $V$ are in bijective correspondence with the roots of the polynomial
\be
  P(x)\=(-x)^A-(1-x)^B\,.
\ee
Indeed, to each root $P(x_0)=0$ the point
\be\label{eq:crit.pts}
  p_0
  \=
  (z_0,m_0)
  \=
  \Big(\frac{\log(x_0)}{2\pi i},\frac{B}{2\pi i}\log(1-x_0)-A\frac{\log(x_0)}{2\pi i}-\frac{A}{2}\Big)
\ee
is a critical point of $V$. These roots are all distinct and therefore the critical points are non-degenerate (see Appendix~\ref{app:crit.pts}). Notice that all ambiguities in the logarithms lead to equivalent points in $\Sigma$. The function $V$ computes the volumes of the $4_1$ and $5_2$ knots with the parameters $(A,B)=(1,2)$ and $(2,3)$, respectively. Indeed, we find that $(z_1,m_1)=(-1/6,0)$ and $(z_2,m_2)=(-5/6,0)$ are the two critical points when $A=1$ and $B=2$ and these have volumes
\be\label{eq:41.crit.val}
  V(-1/6,0)\=0.051418\cdots i\,,
  \qquad
  V(-5/6,0)\=-0.051418\cdots i\,.
\ee
We will denote the collection $(A,B,p_0)$ by $\Xi$. Let $\mathcal{V}\subset\BC$ denote the set of critical values, which includes $\BZ$. Denote the set of rays $\BR_{\geq0}\frac{2\pi i}{\mathcal{V}-V_0}$ by $\mathcal{S}(V_{0})\subseteq\BC$. These form a peacock pattern so that $\BC\backslash\mathcal{S}(V_{0})$ consists of a countable set of cones, see Figure~\ref{fig:41.stokes}.

\medskip

We are interested in a perturbative expansion of certain integrals at the critical points of the function $V$. These integrals involve the formal series $\Psi(z,\hbar)\in\BC\llbracket\hbar\rrbracket$ defined by
\be
  \Psi(z,\hbar)
  \=
  \mu_8\exp\Big(-\frac{(2\pi i)^2}{24\hbar}-\frac{\hbar}{24}-\sum_{k=0}^{\infty}\frac{B_{k}}{k!}\Li_{2-k}(\e(z))\hbar^{k-1}\Big)\,,
\ee
where $\mu_8^8=1$ is an eighth root of unity and $B_k$ denotes the $k$-th Bernoulli number. Explicitly, for each $\Xi$ the formal series is defined by
\be\label{eq:form.int}
  \Phi_{\Xi}(\hbar)\=\int \Psi(z,\hbar)^B\exp\Big(-\frac{A}{2\hbar}(2\pi i)^2z\Big(z+1-\frac{\hbar}{2\pi i}\Big)+(2\pi i)^2\frac{m_0z}{\hbar}\Big)dz\,,
\ee
where we take the formal Gaussian integration around the critical point $z_0$. More precisely, consider the series
\be
\sum_{k=0}^{\infty}\sum_{\ell=-\lfloor k/3\rfloor}^{\infty}a_{k,\ell}w^k\hbar^\ell\in\BC\llbracket\hbar\,,w\rrbracket
\ee
defined through the following equation
\be
\begin{aligned}
  &\exp\Big(-\frac{V(z_0,m_0)}{\hbar}-\frac{\delta}{\hbar} w^2\Big)
  \sum_{k=0}^{\infty}\sum_{\ell=-\lfloor k/3\rfloor}^{\infty}a_{k,\ell}w^k\hbar^\ell\\
  &=\;
  \Psi(z_0+w,\hbar)^B\exp\Big(-\frac{A}{2\hbar}(2\pi i)^2(z_0+w)\Big(z_0+w+1-\frac{\hbar}{2\pi i}\Big)-(2\pi i)^2\frac{m_0(z_0+w)}{\hbar}\Big)\,,
\end{aligned}
\ee
for some constant $\delta$. 
Then, formal Gaussian integration gives
\be\label{eq:def.phi}
  \Phi_{\Xi}(\hbar)\=
  \sqrt{\frac{-2\pi i\hbar}{\delta}}
  \exp\Big(-\frac{V(z_0,m_0)}{\hbar}\Big)
  \sum_{k=0}^{\infty}\sum_{\ell=-\lfloor 2k/3\rfloor}^{\infty}a_{2k,\ell}\frac{(2k-1)!!}{\delta^k}\hbar^{\ell+k}.
\ee
Given that $B_{k}\Li_{2-k}(x)=O((k!)^2(2\pi|\log(x)|)^{-k})$ and exponentiation preserves the property of being Gevery-1~\cite[Thm.~5.55]{diverg-resurg-i}, it is easy to see that these series are Gevery-1, i.e. the coefficient of $\hbar^k$ grows like $A\,k!\,C^k$ as $k\to\infty$. We will prove that $\Phi_{\Xi}$ is in fact Borel--Laplace summable in Theorem~\ref{thm:main_intro}. Importantly, for $(A,B)=(1,2)$ and $(2,3)$, the series $\Phi_{\Xi}$ give the series $\Phi_{4_1}$ and $\Phi_{5_2}$ respectively. This was explicitly illustrated in~\cite[Sec.~7]{GSW} but known in previous work such as~\cite[Sec.~1.3]{GK:qser}.
