---
doc_id: arxiv-1712.04212v4
doc_title: "1. Introduction"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 8-14
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.975
doc_brief: "1. Introduction — In this paper, we consider a concentration of measure problem on Riemannian manifolds with boundary."
---
\label{sec:Preliminaries}
Throughout this section,
let $(M,d_{M},m_{M,f})$ denote an $n$-dimensional weighted Riemannian manifold with boundary defined as (\ref{eq:weighted volume measure}). 



\subsection{Curvatures}\label{sec:Curvatures}
We denote by $\ric_{g}$ the Ricci curvature on $M$ determined by the Riemannian metric $g$,
and by $\ric_{M}$ the infimum of $\ric_{g}$ on the unit tangent bundle over $M$.
For $N\in (-\infty,\infty]$,
the \textit{$N$-weighted Ricci curvature} $\ric^{N}_{f}$ is defined as follows:
If $N \in (-\infty,\infty)\setminus \{n\}$,
then
\begin{equation*}
\ric^{N}_{f}:=\ric_{g}+\Hess f-\frac{d f \otimes d f}{N-n},
\end{equation*}
where $d f$ and $\Hess f$ are the differential and the Hessian of $f$,
respectively;
otherwise,
if $N=\infty$,
then $\ric^{N}_{f}:=\ric_{g}+\Hess f$;
if $N=n$,
and if $f$ is constant,
then $\ric^{N}_{f}:=\ric_{g}$;
if $N=n$,
and if $f$ is not constant,
then $\ric^{N}_{f}:=-\infty$ (\cite{BE}, \cite{L}).
For a function $\mathcal{F}:M\to \mathbb{R}$,
we mean by $\ric^{N}_{f,M}\geq \mathcal{F}$ for every $x \in M$,
and for every unit tangent vector $v$ at $x$
it holds that $\ric^{N}_{f}(v)\geq \mathcal{F}(x)$.

\begin{rem}\label{rem:monotonicity of weighted Ricci curvature}
Traditionally,
$N$ has been chosen from $[n,\infty]$ (see e.g., \cite{Lo}, \cite{Q}, \cite{WW}).
On the other hand,
recently,
various properties have begun to be studied in the complemental case of $N \in (-\infty,n)$ (see e.g., \cite{K}, \cite{KM}, \cite{Mi4}, \cite{O1}, \cite{O2}, \cite{OT1}, \cite{OT2}, \cite{W}, \cite{WY}).
We notice the monotonicity of $\ric^{N}_{f}$ with respect to $N$:
If $N_{1},\,N_{2} \in [n,\infty]$ with $N_{1}\leq N_{2}$,
then $\ric^{N_{1}}_{f} \leq \ric^{N_{2}}_{f}$;
if $N_{1} \in [n,\infty]$ and $N_{2} \in (-\infty,n)$,
then $\ric^{N_{1}}_{f} \leq \ric^{N_{2}}_{f}$;
if $N_{1},\,N_{2} \in (-\infty,n)$ with $N_{1}\leq N_{2}$,
then $\ric^{N_{1}}_{f} \leq \ric^{N_{2}}_{f}$.
\end{rem}

For $z\in \bm$,
let $u_{z}$ denote the unit inner normal vector for $\bm$ at $z$,
and let $\gamma_{z}:[0,T)\to M$ denote the geodesic with $\gamma_{z}'(0)=u_{z}$.
We put
\begin{equation*}
\tau(z):=\sup \{\,t>0 \mid \rho_{\bm}(\gamma_{z}(t))=t\,\}.
\end{equation*}
Let $\ric_{\bm^{\perp}}$ be the \textit{infimum of the Ricci curvature in the $\bm$-radial direction on $M$} defined as $\inf_{z,t} \ric_{g}(\gamma'_{z}(t))$,
where the infimum is take over all $z\in \bm,\,t \in (0,\tau(z))$.
For $\mathcal{F}:M\to \mathbb{R}$,
we mean by $\ric^{N}_{f,\bm^{\perp}} \geq \mathcal{F}$ for all $z \in \bm,\,t \in (0,\tau(z))$
we have $\ric^{N}_{f}(\gamma'_{z}(t))\geq \mathcal{F}(\gamma_{z}(t))$.

For vector fields $v_{1},\,v_{2}$ on $\bm$,
the second fundamental form $S(v_{1},v_{2})$ is defined as the normal component of $\nabla^{g}_{v_{1}}v_{2}$ with respect to $\bm$,
where $\nabla^{g}$ denotes the Levi-Civita connection induced from $g$.
For $z\in \bm$,
let $T_{z}\bm$ denote the tangent space at $z$ on $\bm$.
The shape operator $A_{u_{z}}:T_{z}\bm \to T_{z}\bm$ for $u_{z}$ is defined as
\begin{equation*}
g(A_{u_{z}}v_{1},v_{2}):=g(S(v_{1},v_{2}),u_{z}).
\end{equation*}
The mean curvature $H_{z}$ at $z$ is defined as the trace of $A_{u_{z}}$.
Put $H_{\bm}:=\inf_{z\in \bm} H_{z}$.
The \textit{weighted mean curvature} $H_{f,z}$ at $z$ is defined by
\begin{equation*}
H_{f,z}:=H_{z}+g((\nabla f)_{z},u_{z}).
\end{equation*}
For a function $\mathcal{G}:\bm\to \mathbb{R}$,
we mean by $H_{f,\bm}\geq \mathcal{G}$
we have $H_{f,z} \geq \mathcal{G}(z)$ for all $z\in \bm$.

We mainly study the following three curvature conditions:
For $\kappa,\lambda \in \mathbb{R}$ and $K,\Lambda \in \mathbb{R}$,
\begin{align}\label{eq:finite dimensional curvature bound}
N \in [n,\infty),\,\, &\ric^{N}_{f,\bm^{\perp}}\geq (N-1)\kappa,\,\, H_{f,\bm}\geq (N-1)\lambda;\\ \label{eq:infinite dimensional curvature bound}
N=\infty,\,\,&\ric^{\infty}_{f,\bm^{\perp}}\geq K,\, H_{f,\bm}\geq \Lambda; \\ \label{eq:one dimensional curvature bound}
N=1,\,\,&\ric^{1}_{f,\bm^{\perp}}\geq (n-1)\kappa\, e^{\frac{-4f}{n-1}},\,\, H_{f,\bm}\geq (n-1)\lambda\, e^{\frac{-2f}{n-1}}.
\end{align}

\begin{rem}
We give a historical comment for the curvature condition (\ref{eq:one dimensional curvature bound}).
First,
Wylie \cite{W} has obtained a splitting theorem of Cheeger-Gromoll type under $\ric^{N}_{f,M}\geq 0$ for $N\in (-\infty,1]$.
After that
Wylie and Yeroshkin \cite{WY} have introduced the condition $\ric^{1}_{f,M}\geq (n-1)\kappa\, e^{\frac{-4f}{n-1}}$ from the view point of study of affine connections,
and established comparison geometry.
Furthermore,
the author \cite{S2} has studied comparison geometry of manifolds with boundary under the curvature condition $\ric^{N}_{f,M}\geq (n-1)\kappa\, e^{\frac{-4f}{n-1}}$ and $H_{f,\bm}\geq (n-1)\lambda\, e^{\frac{-2f}{n-1}}$ for $N\in (-\infty,1]$.
\end{rem}



\subsection{Laplacians and Dirichlet eigenvalues}
For the weighted Laplacian $\Delta_{f}$ defined as (\ref{eq:weighted Laplacian}),
the following formula of Bochner type is well-known (see e.g., Chapter 14 in \cite{V}):
For every smooth $\psi:M\to \mathbb{R}$,
\begin{equation}\label{eq:Bochner formula}
-\frac{1}{2}\,\Delta_{f}\,\Vert \nabla \psi \Vert^{2}=\ric^{\infty}_{f}(\nabla \psi)+\Vert \Hess \psi \Vert^{2}_{\HS}-g\left(\nabla \Delta_{f}\,\psi,\nabla \psi \right),
\end{equation}
where $\Vert \cdot \Vert$ and $\Vert \cdot \Vert_{\HS}$ are the canonical norm and the Hilbert-Schmidt norm induced from $g$,
respectively.

For $z\in \bm$,
the value $\Delta_{f}\rho_{\bm}(\gamma_{z}(t))$ converges to $H_{f,z}$ as $t\to 0$.
For $t \in (0,\tau(z))$,
and for the volume element $\theta(t,z)$ of the $t$-level surface of $\rho_{\bm}$ at $\gamma_{z}(t)$,
we set
\begin{equation}\label{eq:volume element}
\theta_{f}(t,z):=e^{-f(\gamma_{z}(t))}\, \theta(t,z).
\end{equation}
For all $t\in (0,\tau(z))$
it holds that
\begin{equation}\label{eq:Laplacian representation}
\Delta_{f}\, \rho_{\bm}(\gamma_{z}(t)) =-\frac{\theta_{f}'(t,z)}{\theta_{f}(t,z)}.
\end{equation}
We also have the following (see e.g., \cite{S1}):
If $\bm$ is compact,
then
\begin{equation}\label{eq:integration formula}
m_{M,f}( B_{r}(\bm))=\int_{\bm} \int^{r}_{0}\bar{\theta}_{f}(t,z)\,dt\,d\vol_{h}
\end{equation}
for all $r>0$,
where $\vol_{h}$ is the Riemannian volume measure on $\bm$ induced from $h$,
and $\bar{\theta}_{f}:[0,\infty) \times \bm \to \mathbb{R}$ is a function defined as
\begin{equation}\label{eq:extended volume element}
  \bar{\theta}_{f}(t,z) := \begin{cases}
                                     \theta_{f}(t,z) & \text{if $t< \tau(z)$}, \\
                                             0           & \text{if $t \geq \tau(z)$}.
                                    \end{cases}
\end{equation}

Let $M$ be compact.
For $\phi \in H^{1}_{0}(M,m_{M,f})\setminus \{0\}$,
its Rayleigh quotient is defined as
\begin{equation}\label{eq:Rayleigh quotient}
R_{f}(\phi):=\frac{\int_{M}\, \Vert \nabla \phi \Vert^{2}\,d\,m_{M,f}}{\int_{M}\, \phi^{2}\,d\,m_{M,f}}.
\end{equation}
For the $k$-th Dirichlet eigenvalue $\nu_{f,k}(M)$ of the weighted Laplacian $\Delta_{f}$ defined as $(\ref{eq:notation of Dirichlet eigenvalue})$,
the min-max principle states
\begin{equation}\label{eq:min-max principle}
\nu_{f,k}(M)=\inf_{L} \sup_{\phi \in L\setminus \{0\}} R_{f}(\phi),
\end{equation}
where the infimum is taken over all $k$-dimensional subspaces $L$ of the Sobolev space $H^{1}_{0}(M,m_{M,f})$.



\subsection{Dirichlet isoperimetric constants}\label{sec:Dirichlet isoperimetric constants}
For a Borel subset $\Omega \subset M$,
\begin{equation*}
m^{+}_{M,f}(\Omega):=\liminf_{r\to 0}\frac{m_{M,f}(U_{r}(\Omega))-m_{M,f}(\Omega)}{r},
\end{equation*}
where $U_{r}(\Omega)$ is the open $r$-neighborhood of $\Omega$.
The \textit{Dirichlet isoperimetric constant} is defined as
\begin{equation*}
\mathcal{I}_{f}(M):=\inf_{\Omega} \frac{m^{+}_{M,f}(\Omega)}{m_{M,f}(\Omega)},
\end{equation*}
where the infimum is taken over all Borel subsets $\Omega \subset \inte M$ (cf. Definition 9.1 in \cite{L}).
The following inequality of Cheeger type is well-known (see \cite{C}, and cf. Corollary 9.7 in \cite{L}):
If $M$ is compact,
then
\begin{equation}\label{eq:Dirichlet Cheeger inequality}
\mathcal{I}_{f}(M) \leq 2 \sqrt{\nu_{f,1}(M)}.
\end{equation}

In the graph setting,
Kwak, Lau, Lee, Oveis Gharan and Trevisan \cite{KLLOT} have established an improved Cheeger inequality in terms of the smallest and higher eigenvalues of the Laplacian and the conductance (see Theorem 1.1 in \cite{KLLOT}).
In the manifold setting,
to answer a question of Funano \cite{F},
Liu \cite{Liu} has pointed out that
a similar improved Cheeger inequality holds for closed eigenvalues of the Laplacian and the Cheeger constant via the same argument as in \cite{KLLOT} (see Theorem 1.6 in \cite{Liu}).

Now,
we further point out that
the following improvement of (\ref{eq:Dirichlet Cheeger inequality}) holds in our setting via the same argument as in \cite{KLLOT}:
\begin{thm}[\cite{KLLOT}, \cite{Liu}]\label{thm:higer order eigenvalue and isoperimetric}
Let $M$ be compact.
Then for all $k\geq 1$,
\begin{equation}\label{eq:higer order eigenvalue and isoperimetric}
\mathcal{I}_{f}(M) \leq 8\sqrt{2}k\frac{\nu_{f,1}(M)}{\sqrt{\nu_{f,k}(M)}}.
\end{equation}
\end{thm}
One can verify (\ref{eq:higer order eigenvalue and isoperimetric}) by applying the same argument as in the proof of Lemmas 3.2 and 3.3 in \cite{Liu} (replace the role of the $k$-th closed eigenvalue with that of $\nu_{f,k}(M)$) to a non-negative eigenfunction of $\nu_{f,1}(M)$,
here we recall that any eigenfunctions of $\nu_{f,1}(M)$ are either always positive or always negative on $\inte M$.
Note that
for such an eigenfunction,
the $2k$ disjointly supported Lipschitz functions constructed in the proof of Lemma 3.3 in \cite{Liu} also satisfy the Dirichlet boundary condition.



\subsection{Dirichlet eigenvalue estimates}\label{sec:Isoperimetric inequalities}
Wang \cite{Wa} has produced a gradient estimate of Bakry-Ledoux type for the Dirichlet heat semigroup associated with the weighted Laplacian under a lower (unweighted) Ricci curvature bound,
a lower (unweighted) mean curvature bound for the boundary,
and a density bound (see Theorem 1.1 in \cite{Wa}, and also \cite{BL}).
From the same argument as in the proof of Theorem 1.1 in \cite{Wa},
we can derive the following (cf. (1.10) in \cite{Wa} for unweighted case):
\begin{thm}[\cite{Wa}]\label{thm:gradient estimate}
If $\ric^{\infty}_{f,M}\geq 0$ and $H_{f,\bm}\geq 0$,
then we have
\begin{equation*}
\Vert \Vert \nabla P_{t}\psi \Vert \Vert_{L^{\infty}}\leq \frac{\sqrt{1+2^{1/3}}\,(1+4^{2/3})}{2\sqrt{\pi}} \frac{\Vert \psi \Vert_{L^{\infty}}}{\sqrt{t}}
\end{equation*}
for all $t>0$ and non-negative, bounded measurable functions $\psi$ on $M$,
where $P_{t}$ is the Dirichlet heat semigroup generated by $-\Delta_{f}$.
\end{thm}
Wang \cite{Wa} has proved Theorem \ref{thm:gradient estimate} when $f=0$.
One can see Theorem \ref{thm:gradient estimate} only by using Lemma 3.4 in \cite{S1} (or Lemma \ref{lem:Laplacian comparison} below) instead of Lemma 2.3 in \cite{Wa},
and using the inequality (2.3) in \cite{CW} instead of (2.5) in \cite{Wa} along the line of the proof of Theorem 1.1 in \cite{Wa}.

In virtue of the gradient estimate,
Wang \cite{Wa} has obtained an isoperimetric inequality of Buser and Ledoux type based on the idea of Ledoux \cite{L1} (see Theorem 1.2 in \cite{Wa}, and also \cite{Bu}, \cite{L1}).
Theorem \ref{thm:gradient estimate} together with the same argument as in the proof of Theorem 1.2 in \cite{Wa} yields:
\begin{thm}[\cite{Wa}]\label{thm:Buser Ledoux}
Let $M$ be compact.
If $\ric^{\infty}_{f,M}\geq 0$ and $H_{f,\bm}\geq 0$,
then we have
\begin{equation}\label{eq:Buser Ledoux}
\mathcal{I}_{f}(M) \geq \frac{2\sqrt{\pi}}{\sqrt{1+2^{1/3}}\,(1+4^{2/3})}\,\sup_{t>0}\frac{1-e^{-t}}{\sqrt{t}}\, \sqrt{\nu_{f,1}(M)}.
\end{equation}
\end{thm}

Combining (\ref{eq:higer order eigenvalue and isoperimetric}), (\ref{eq:Buser Ledoux}) implies the following universal inequality:
\begin{thm}\label{thm:universal inequality}
Let $M$ be compact.
If $\ric^{\infty}_{f,M}\geq 0$ and $H_{f,\bm}\geq 0$,
then there is a universal constant $C>0$ such that
for all $k\geq 1$
we have
\begin{equation}\label{eq:universal inequality}
\nu_{f,k}(M)\leq C\,k^{2}\,\nu_{f,1}(M).
\end{equation}
\end{thm}
Funano and Shioya \cite{FSh}, Funano \cite{F}, Liu \cite{Liu} have formulated similar inequalities for closed manifolds of non-negative $\infty$-weighted Ricci curvature (see Theorem 1.1 in \cite{FSh}, Theorem 1.2 in \cite{F} and Theorem 1.1 in \cite{Liu}).
The inequality (\ref{eq:universal inequality}) corresponds to that of Liu \cite{Liu}.

\begin{rem}\label{rem:Li-Yau dimension free}
Under similar setting $\ric^{\infty}_{f,\bm^{\perp}}\geq 0$ and $H_{f,\bm}\geq 0$ to that in Theorem \ref{thm:universal inequality},
the author \cite{S1} has shown a dimension free inequality
\begin{equation}\label{eq:Li-Yau dimension free}
\nu_{f,1}(M)\geq \pi^{2} (2\IR M)^{-2}
\end{equation}
of Li-Yau, Kasue type,
and a rigidity result for the equality case (see Corollary 7.6 in \cite{S1}, and also \cite{LY}, \cite{K2}, and cf. Remarks \ref{rem:remark on the curvature assumption} and \ref{rem:conjecture}).
\end{rem}

\begin{rem}\label{rem:dimension dependent inequality}
Let $M$ be compact,
and let $\nu_{k}(M)$ be the $k$-th Dirichlet eigenvalue of the Laplacian $\Delta$.
Let us mention a dimension dependent estimate of the ratio $\nu_{k}(M)/\nu_{1}(M)$ induced from a classical method by Cheng \cite{Ch}, Li-Yau \cite{LY}.
We possess the following estimate by modifying the proof of Corollary 2.2 in \cite{Ch} (take a unit speed minimal geodesic $\gamma:[0,\IR M]\to M$ with $\gamma((0,\IR M])\subset \inte M$ that is orthogonal to $\bm$ at $\gamma(0)$,
set $k$ disjoint open balls in $\inte M$ centered at $\gamma((2\alpha-1)(2k)^{-1} \IR M)$ with radius $(2k)^{-1} \IR M$ for $\alpha=1,\dots,k$,
and apply the argument of proof of Theorem 2.1 in \cite{Ch}):
If $\ric_{M}\geq 0$,
then
\begin{equation}\label{eq:Cheng dimension dependent}
\nu_{k}(M)\leq 2n(n+4)k^{2} (\IR M)^{-2}
\end{equation}
for all $k\geq 1$.
By (\ref{eq:Li-Yau dimension free}), (\ref{eq:Cheng dimension dependent}),
we obtain the following:
If $\ric_{M}\geq 0$ and $H_{\bm}\geq 0$,
then there is $C_{n}>0$ depending only on $n$ such that
\begin{equation}\label{eq:Li-Yau-Cheng dimension dependent inequality}
\nu_{k}(M)\leq C_{n}\,k^{2}\,\nu_{1}(M)
\end{equation}
for all $k\geq 1$.
Theorem \ref{thm:universal inequality} is a refinement of (\ref{eq:Li-Yau-Cheng dimension dependent inequality}) in the sense that
the upper bound of $\nu_{k}(M)/\nu_{1}(M)$ does not depend on $n$.
\end{rem}



\subsection{Comparisons}\label{sec:Comparison theorems}
The author \cite{S1}, \cite{S2} has obtained inscribed radius comparison theorems,
and rigidity results for the equality case.
We first recall the following comparison (see Theorem 1.1 in \cite{S1}):
\begin{thm}[\cite{S1}]\label{thm:inscribed radius comparison}
For $N\in [n,\infty)$,
we assume $\ric^{N}_{f,\bm^{\perp}}\geq (N-1)\kappa$ and $H_{f,\bm}\geq (N-1)\lambda$.
If $\kappa$ and $\lambda$ satisfy the ball-condition,
then
\begin{equation*}
\IR M \leq \const.
\end{equation*}
\end{thm}
\begin{rem}
Kasue \cite{K1} has proved Theorem \ref{thm:inscribed radius comparison},
and rigidity result for the equality case in the unweighted case where $f=0$ and $N=n$.
Li and Wei have done in \cite{LW2} when $\kappa=0$,
and in \cite{LW1} when $\kappa<0$.
\end{rem}

We also have the following comparison (see Theorem 6.3 in \cite{S2}):
\begin{thm}[\cite{S2}]\label{thm:twisted inscribed radius comparison}
Assume
$\ric^{1}_{f,\bm^{\perp}}\geq (n-1) \,\kappa \,e^{\frac{-4f}{n-1}}$ and $H_{f,\bm}\geq (n-1)\,\lambda\,e^{\frac{-2f}{n-1}}$.
Suppose additionally that
$f\leq (n-1)\delta$ for some $\delta \in \mathbb{R}$.
If $\kappa$ and $\lambda$ satisfy the ball-condition,
then we have
\begin{equation*}
\IR M \leq C_{\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}.
\end{equation*}
\end{thm}

For $\kappa,\lambda \in \mathbb{R}$,
let $s_{\kappa,\lambda}(t)$ be a unique solution of the Jacobi equation $\psi''(t)+\kappa\, \psi(t)=0$ with $\psi(0)=1,\,\psi'(0)=-\lambda$.
Notice that
$\kappa$ and $\lambda$ satisfy the ball-condition if and only if
the equation $s_{\kappa,\lambda}(t)=0$ has a positive solution;
moreover,
$\const=\inf \{\,t>0 \mid s_{\kappa,\lambda}(t)=0\, \}$.
We define $\bar{C}_{\kappa,\lambda}$ as follows:
If $\kappa$ and $\lambda$ satisfy the ball-condition,
then $\bar{C}_{\kappa,\lambda}:=\const$;
otherwise,
$\bar{C}_{\kappa,\lambda}:=\infty$.
For $N\in (1,\infty)$,
let us define a function $s_{N,\kappa,\lambda}:(0,\infty]\to (0,\infty]$ by
\begin{equation}\label{eq:one dimensional volume growth}
\bar{s}_{\kappa,\lambda}(t) := \begin{cases}
                                            s_{\kappa,\lambda}(t) & \text{if $t< \bar{C}_{\kappa,\lambda}$},\\
                                            0                     & \text{if $t\geq    \bar{C}_{\kappa,\lambda}$},
                                 \end{cases}
                                 \quad s_{N,\kappa,\lambda}(r):=\int^{r}_{0}\, \bar{s}^{N-1}_{\kappa,\lambda}(t)\,dt.
\end{equation}

\begin{rem}\label{rem:formulation of finite dimensional model spaces}
For $\kappa,\lambda\in \mathbb{R}$,
the value $s_{n,\kappa,\lambda}(\bar{C}_{\kappa,\lambda})$ is finite if and only if
either (1) $\kappa$ and $\lambda$ satisfy the ball-condition;
or (2) $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$ (cf. formulation of finite dimensional model spaces in Subsection \ref{sec:Comparisons and concentration phenomena}).
\end{rem}

For $r>0$ and $\Omega \subset M$,
let $B_{r}(\Omega)$ stand for the closed $r$-neighborhood of $\Omega$.
We next recall the following relative volume comparison theorem for metric neighborhoods of boundaries (see Theorem 5.4 in \cite{S1}):
\begin{thm}[\cite{S1}]\label{thm:volume comparison}
Let $\bm$ be compact.
For $N\in [n,\infty)$,
we assume $\ric^{N}_{f,\bm^{\perp}}\geq (N-1)\kappa$ and $H_{f,\bm}\geq (N-1)\lambda$.
Then for all $r,R>0$ with $r\leq R$
we have
\begin{equation*}
\frac{m_{M,f}(B_{R}(\bm))}{m_{M,f}(B_{r}(\bm))}\leq \frac{s_{N,\kappa,\lambda}(R)}{s_{N,\kappa,\lambda}(r)}.
\end{equation*}
\end{thm}
\begin{rem}
Under the same setting as in Theorem \ref{thm:volume comparison},
Bayle \cite{B} has stated a similar absolute volume comparison of Heintze-Karcher type (see Theorem E.2.2 in \cite{B}, and see also \cite{HK}, \cite{Mi3}, \cite{Mi4}, \cite{Mo}).
\end{rem}

We further recall the following comparison (see Theorem 7.6 in \cite{S2}):
\begin{thm}[\cite{S2}]\label{thm:twisted volume comparison}
Let $\bm$ be compact.
Let us assume $\ric^{1}_{f,\bm^{\perp}}\geq (n-1) \,\kappa \,e^{\frac{-4f}{n-1}}$ and $H_{f,\bm}\geq (n-1)\,\lambda\,e^{\frac{-2f}{n-1}}$.
Suppose additionally that
$f\leq (n-1)\delta$ for some $\delta \in \mathbb{R}$.
Assume that
one of the following holds:
\begin{enumerate}
\item $\kappa$ and $\lambda$ satisfy the convex-ball-condition;
\item $\kappa \leq 0$ and $\lambda=\sqrt{\vert \kappa \vert}$.
\end{enumerate}
Then for all $r,R>0$ with $r\leq R$
we have
\begin{equation*}
\frac{m_{M,f}(B_{R}(\bm))}{m_{M,f}(B_{r}(\bm))}\leq \frac{s_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(R)}{s_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(r)}.
\end{equation*}
\end{thm}

\begin{rem}\label{rem:remark on the curvature assumption}
In \cite{S1},
the author has stated that
the comparison inequalities in Theorems \ref{thm:inscribed radius comparison} and \ref{thm:volume comparison} hold
under the curvature condition $\ric^{N}_{f,M}\geq (N-1)\kappa$ and $H_{f,\bm}\geq (N-1)\lambda$.
Actually,
the author \cite{S1} has proved such comparison inequalities under the curvature condition $\ric^{N}_{f,\bm^{\perp}}\geq (N-1)\kappa$ and $H_{f,\bm}\geq (N-1)\lambda$ relying on the Laplacian comparison for the distance function $\rho_{\bm}$.
We can say the same thing for the inequalities in Theorems \ref{thm:twisted inscribed radius comparison} and \ref{thm:twisted volume comparison} (see \cite{S2}).
\end{rem}
