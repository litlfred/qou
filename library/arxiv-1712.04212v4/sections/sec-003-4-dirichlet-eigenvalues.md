---
doc_id: arxiv-1712.04212v4
doc_title: "1. Introduction"
section_id: sec-003-4-dirichlet-eigenvalues
section_title: "Dirichlet eigenvalues"
section_number: 4
pages: 19-22
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.959
doc_brief: "1. Introduction — In this paper, we consider a concentration of measure problem on Riemannian manifolds with boundary."
---
\label{sec:Dirichlet eigenvalues}
In what follows,
let $(M,d_{M},m_{M,f})$ denote an $n$-dimensional weighted Riemannian manifold with boundary defined as (\ref{eq:weighted volume measure}) such that $m_{M,f}$ is a Borel probability measure.
We study the metric measure space with boundary $(M,f)$ defined as (\ref{eq:weighted Riemannian manifold}).



\subsection{Boundary separation distances and Dirichlet eigenvalues}
Let us show the following relation between the boundary separation distance and the Dirichlet eigenvalue:
\begin{lem}\label{lem:Dirichlet eigenvalue and Dirichlet separation distance}
Let $M$ be compact.
Then for all $\eta_{1},\dots,\eta_{k}>0$
we have
\begin{equation*}
\DS\left((M,f);\eta_{1},\dots,\eta_{k}\right)\leq \frac{2}{\sqrt{\nu_{f,k}(M)\, \min_{\alpha=1,\dots,k} \eta_{\alpha}}},
\end{equation*}
where $\nu_{f,k}(M)$ is the $k$-th Dirichlet eigenvalue of $\Delta_{f}$ defined as $(\ref{eq:notation of Dirichlet eigenvalue})$.
\end{lem}
\begin{proof}
We set $S:=\DS((M,f);\eta_{1},\dots,\eta_{k})$.
We may assume $S>0$.
Let us fix a sufficiently small $\epsilon>0$.
There exists a sequence $\{\Omega_{\alpha}\}^{k}_{\alpha=1} \in \mathcal{S}_{(M,f)}(\eta_{1},\dots,\eta_{k})$ such that $S-\epsilon<\mathcal{D}_{(M,f)}\bigl(\{\Omega_{\alpha}\}^{k}_{\alpha=1}\bigl)$.
Put $S_{\epsilon}:=S-\epsilon$.
For each $\alpha$,
we define a Lipschitz function $\phi_{\alpha}:M\to \mathbb{R}$ by
\begin{equation*}
\phi_{\alpha}(x):=\max \left\{1-\frac{2}{S_{\epsilon}}\,d_{M}(x,\Omega_{\alpha}),0\right\}.
\end{equation*}
Notice that
the support of $\phi_{\alpha}$ coincides with $B_{S_{\epsilon}/2}(\Omega_{\alpha})$.
Furthermore,
the following properties hold:
\begin{enumerate}\setlength{\itemsep}{+1.5mm}
\item $\phi_{\alpha} \equiv 0$ on $B_{S_{\epsilon}/2}(\bm)$; \label{item:vanish on boundary}
\item $\phi_{\alpha} \equiv 0$ on $B_{S_{\epsilon}/2}(\Omega_{\beta})$ for every $\beta=1,\dots,k$ with $\beta \neq \alpha$; \label{item:vanish on another domain}
\item $\phi_{\alpha} \equiv 1$ on $\Omega_{\alpha}$; \label{item:identity}
\item $\Vert \nabla \phi_{\alpha} \Vert \leq 2/S_{\epsilon}$ $m_{M,f}$-almost everywhere on $M$. \label{item:gradient estimate}
\end{enumerate}
By (\ref{item:vanish on boundary}),
$\phi_{\alpha}$ belongs to the Sobolev space $H^{1}_{0}(M,m_{M,f})$.
By (\ref{item:vanish on another domain}),
the functions $\phi_{1},\dots,\phi_{k}$ are orthogonal to each other in $H^{1}_{0}(M,m_{M,f})$.
Let $L_{0}$ be the $k$-dimensional subspace of $H^{1}_{0}(M,m_{M,f})$ spanned by $\phi_{1},\dots,\phi_{k}$.
From (\ref{item:identity}) and (\ref{item:gradient estimate}),
for every $\phi \in L_{0}\setminus \{0\}$
we deduce
\begin{align*}
\int_{M}\,\phi^{2}\,dm_{M,f}&=\sum^{k}_{\alpha=1}\,c^{2}_{\alpha}\,\int_{M}\,\phi^{2}_{\alpha}\,dm_{M,f} \geq \sum^{k}_{\alpha=1}\,c^{2}_{\alpha}\, \eta_{\alpha} \geq \min_{\alpha} \eta_{\alpha}\,\sum^{k}_{\alpha=1}\,c^{2}_{\alpha} ,\\
\int_{M}\,\Vert \nabla \phi \Vert^{2}\,dm_{M,f}&=\sum^{k}_{\alpha=1}\,c^{2}_{\alpha}\,\int_{M}\, \Vert \nabla \phi_{\alpha} \Vert^{2}\,dm_{M,f} \leq \left(\frac{2}{S_{\epsilon}}\right)^{2} \sum^{k}_{\alpha=1}\,c^{2}_{\alpha},
\end{align*}
where $c_{1},\dots,c_{k}$ are determined by $\phi=\sum^{k}_{\alpha=1}\,c_{\alpha} \phi_{\alpha}$.
Hence
we have
\begin{equation*}
R_{f}(\phi)=\frac{\int_{M} \,\Vert \nabla \phi \Vert^{2} \,dm_{M,f}}{\int_{M} \,\phi^{2} \,dm_{M,f}} \leq \frac{1}{\min_{\alpha} \eta_{\alpha}}\left(\frac{2}{S_{\epsilon}}\right)^{2},
\end{equation*}
where $R_{f}(\phi)$ is the Rayleigh quotient of $\phi$ defined as (\ref{eq:Rayleigh quotient}).
From the min-max principle (\ref{eq:min-max principle})
we derive
\begin{equation*}
\nu_{f,k}(M) \leq \sup_{\phi \in L_{0}\setminus \{0\}}\,R_{f}(\phi) \leq \frac{1}{\min_{\alpha} \eta_{\alpha}}\left(\frac{2}{S_{\epsilon}}\right)^{2}.
\end{equation*}
Letting $\epsilon \to 0$,
we conclude the inequality.
\end{proof}

\begin{rem}
In the forthcoming paper \cite{FSa},
Funano and the author prove the following refined estimate for $k=1$ (see Theorem 2.3 in \cite{FSa}):
For every $\eta>0$
we have
\begin{equation*}
\DS\left((M,f);\eta\right)\leq \frac{1}{\sqrt{\nu_{f,1}(M)}} \,\log \frac{e}{\eta}.
\end{equation*}
\end{rem}

\begin{rem}
Colbois and Savo \cite{CS} have shown a similar estimate for the $k$-th closed eigenvalue of the Laplacian (see Lemma 5 in \cite{CS}). 
\end{rem}

\begin{rem}
Chung, Grigor'yan and Yau \cite{CGY} have estimated the $k$-th closed eigenvalue and Robin eigenvalue of the Laplacian in terms of the separation distance (see Theorem 1.1 in \cite{CGY}).
By applying the same argument in \cite{CGY} to our setting,
we see the following estimate for $\nu_{f,k}(M)$:
Suppose that $M$ is compact.
Then for every integer $k>2$,
and for every sequence $\{\Omega_{\alpha}\}^{k}_{\alpha=1}$ of Borel subsets with $\min_{\alpha \neq \beta} d_{M}(\Omega_{\alpha},\Omega_{\beta})\geq D$,
\begin{equation*}
\nu_{f,k}(M)-\nu_{f,1}(M) \leq \frac{1}{D^{2}}\,\max_{\alpha \neq \beta} \,\left( \log\,\frac{4}{\int_{\Omega_{\alpha}} \,\phi^{2}_{f,1}\,dm_{M,f} \, \int_{\Omega_{\beta}} \,\phi^{2}_{f,1}\,dm_{M,f}   }  \right)^{2},
\end{equation*}
where $\phi_{f,1}$ is an $L^{2}$-normalized eigenfunction for $\nu_{f,1}(M)$.
\end{rem}



\subsection{Observable inscribed radii and Dirichlet eigenvalues}
Now,
Lemma \ref{lem:Dirichlet eigenvalue and Dirichlet separation distance} together with Lemma \ref{lem:observable inscribed radius is smaller than Dirichlet separation distance}
leads us to the following relation between the observable inscribed radius and the Dirichlet eigenvalue:
\begin{prop}\label{prop:logarithmic Dirichlet eigenvalue and observable inscribed radius}
Let $M$ be compact.
Then for every $\eta>0$,
\begin{equation*}
\OI((M,f);-\eta)\leq \frac{2}{\sqrt{\nu_{f,1}(M)\, \eta}}.
\end{equation*}
\end{prop}

\begin{rem}
Under the curvature condition (\ref{eq:finite dimensional curvature bound}) and $\IR M \leq D$,
the author \cite{S1} has provided a lower bound of $\nu_{f,1}(M)$ depending only on $\kappa,\,\lambda,\,N$ and $D$ (see Theorem 1.6 in \cite{S1} and Remark \ref{rem:remark on the curvature assumption},
and also pioneering works of Li-Yau \cite{LY} and Kasue \cite{K2}).
Combining Proposition \ref{prop:logarithmic Dirichlet eigenvalue and observable inscribed radius} with the lower estimate tells us that
we have an upper bound of $\OI((M,f);-\eta)$ depending only on $\kappa,\,\lambda,\,N,\,D$ and $\eta$.

Similarly,
under the condition (\ref{eq:one dimensional curvature bound}) for $\kappa$ and $\lambda$ satisfying the convex-ball-condition,
and under $f\leq (n-1)\delta$,
the author \cite{S2} has obtained a lower bound of $\nu_{f,1}(M)$ depending only on $n,\,\kappa,\,\lambda$ and $\delta$ (see Theorem 8.5 in \cite{S2}).
In virtue of Proposition \ref{prop:logarithmic Dirichlet eigenvalue and observable inscribed radius},
we possess an upper bound of $\OI((M,f);-\eta)$ depending only on $n,\,\kappa,\,\lambda,\,\delta$ and $\eta$.
\end{rem}

Proposition \ref{prop:logarithmic Dirichlet eigenvalue and observable inscribed radius} enables us to prove Theorem \ref{thm:Dirichlet eigenvalue and Dirichlet Levy family}.
\begin{proof}[Proof of Theorem \ref{thm:Dirichlet eigenvalue and Dirichlet Levy family}]
Let $\{(M_{n},f_{n})\}$ be a sequence of compact metric measure spaces with boundary defined as $(\ref{eq:weighted Riemannian manifold})$.
By Proposition \ref{prop:logarithmic Dirichlet eigenvalue and observable inscribed radius},
if $\nu_{f_{n},1}(M_{n})\to \infty$ as $n\to \infty$,
then $\OI((M_{n},f_{n});-\eta)\to 0$.
Hence,
$\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{proof}

We also derive the following from Proposition \ref{prop:logarithmic Dirichlet eigenvalue and observable inscribed radius} and Theorem \ref{thm:universal inequality}:
\begin{thm}\label{thm:higer order Dirichlet eigenvalue and observable inscribed radius}
Let $M$ be compact.
If $\ric^{\infty}_{f,M}\geq 0$ and $H_{f,\bm}\geq 0$,
then there is a universal constant $C>0$ such that
for all $k\geq 1$ and $\eta>0$,
\begin{equation*}
\OI((M,f);-\eta)\leq \frac{C\,k}{\sqrt{\nu_{f,k}(M)\, \eta}}.
\end{equation*}
\end{thm}

Let us give a proof of Theorem \ref{thm:higher order Dirichlet eigenvalue and Dirichlet Levy family} by using Theorem \ref{thm:higer order Dirichlet eigenvalue and observable inscribed radius}.
\begin{proof}[Proof of Theorem \ref{thm:higher order Dirichlet eigenvalue and Dirichlet Levy family}]
Let $\{(M_{n},f_{n})\}$ denote a sequence of compact metric measure spaces with boundary defined as $(\ref{eq:weighted Riemannian manifold})$.
Assume that
$\ric^{\infty}_{f_{n},M_{n}}\geq 0$ and $H_{f_{n},\bm_{n}}\geq 0$.
Due to Theorem \ref{thm:higer order Dirichlet eigenvalue and observable inscribed radius},
if $\nu_{f_{n},k}(M_{n})\to \infty$ for $k$,
then $\OI((M_{n},f_{n});-\eta)\to 0$.
We complete the proof.
\end{proof}

\begin{rem}\label{rem:conjecture}
The author wonders whether the following statement of E. Milman type holds (see \cite{Mi1}, \cite{Mi2}, and Theorem 9.46 in \cite{Sh}):
Under the same setting as in Theorems \ref{thm:Dirichlet eigenvalue and Dirichlet Levy family}, \ref{thm:higher order Dirichlet eigenvalue and Dirichlet Levy family},
if $\ric^{\infty}_{f_{n},M_{n}}\geq 0$ and $H_{f_{n},\bm_{n}}\geq 0$,
and if $\{(M_{n},f_{n})\}$ is a boundary concentration family,
then $\nu_{f_{n},1}(M_{n})\to \infty$.
If it is true,
then
in virtue of Theorems \ref{thm:Dirichlet eigenvalue and Dirichlet Levy family}, \ref{thm:higher order Dirichlet eigenvalue and Dirichlet Levy family},
we can say that
under $\ric^{\infty}_{f_{n},M_{n}}\geq 0$ and $H_{f_{n},\bm_{n}}\geq 0$,
the following are equivalent:
\begin{enumerate}\setlength{\itemsep}{+0.7mm}
\item $\{(M_{n},f_{n})\}$ is a boundary concentration family;
\item $\nu_{f_{n},1}(M_{n})\to \infty$ as $n\to \infty$;
\item $\nu_{f_{n},k}(M_{n})\to \infty$ as $n\to \infty$ for some $k\geq 1$.
\end{enumerate}

The author also wonders if
one can extend the above equivalence to a weaker setting $\ric^{N}_{f_{n},M_{n}}\geq 0$ and $H_{f_{n},\bm_{n}}\geq 0$ for $N\in (-\infty,1]$ (see Remark \ref{rem:monotonicity of weighted Ricci curvature}).
Under $\ric^{N}_{f,\bm^{\perp}}\geq 0$ and $H_{f,\bm}\geq 0$ for $N\in (-\infty,1]$,
the author \cite{S1.5} has proved a dimension free inequality
\begin{equation*}
\nu_{f,1}(M)\geq \pi^{2} (2\IR M)^{-2},
\end{equation*}
of Li-Yau, Kasue type,
and a rigidity result for the equality case (see Corollary 6.5 in \cite{S1.5}, and also \cite{LY}, \cite{K2}, and cf. Remarks \ref{rem:Li-Yau dimension free} and \ref{rem:remark on the curvature assumption}).
\end{rem}
