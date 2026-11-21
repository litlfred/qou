---
doc_id: arxiv-1712.04212v4
doc_title: "1. Introduction"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.934
doc_brief: "1. Introduction — In this paper, we consider a concentration of measure problem on Riemannian manifolds with boundary."
---
In the present paper,
we consider a concentration of measure problem on manifolds with boundary.
We study concentration phenomena of non-negative $1$-Lipschitz functions with Dirichlet boundary condition.



\subsection{Motivations}
Let us recall the following well-known fact:
The normalized volume measure on the $n$-dimensional unit sphere concentrates around the equator when $n$ is large.
One can rephrase this fact as follows:
The normalized volume measure on the $n$-dimensional unit hemisphere concentrates around the boundary when $n$ is large.

We call a triple $X=(X,d_{X},\mu_{X})$ a \textit{(smooth) metric measure space with boundary}
when $X$ is a connected complete Riemannian manifold with boundary,
$d_{X}$ is the Riemannian distance,
and $\mu_{X}$ is a Borel probability measure on $X$.
Let $\partial X$ denote its boundary.
In this paper,
we consider the following problem:
\textit{For a given sequence $\{X_{n}\}$ of metric measure spaces with boundary $X_{n}=(X_{n},d_{X_{n}},\mu_{X_{n}})$,
does the measure $\mu_{X_{n}}$ concentrate around $\partial X_{n}$ when $n$ is large ?}
We will observe that
$\mu_{X_{n}}$ concentrates around $\partial X_{n}$ if and only if
every $1$-Lipschitz function $\varphi_{n}:X_{n}\to [0,\infty)$ with $\varphi_{n}|_{\partial X_{n}}=0$ is closed to zero (more precisely, see Remark \ref{rem:characterization of Dirichlet Levy} and Proposition \ref{prop:characterization of Dirichlet Levy}).
From this point of view,
we investigate concentration phenomena of non-negative $1$-Lipschitz functions with Dirichlet boundary condition around zero.
We call such phenomena \textit{boundary concentration phenomena}.



\subsection{Observable inscribed radii}
Gromov \cite{G} has established theory of geometry of metric measure spaces
based on the idea of concentration of measure phenomena discovered by L\'evy \cite{Le}, and developed by V. D. Milman \cite{M1}, \cite{M2}.
He has introduced some important invariants on metric measure spaces.
One of them is the so-called \textit{observable diameter}
that measures the difference between $1$-Lipschitz functions and constants.
The observable diameter has been widely studied from the view point of the study of concentration phenomena of $1$-Lipschitz functions (see e.g., \cite{G}, \cite{L2}, \cite{Sh} and the references therein).

We now introduce a new invariant on metric measure spaces with boundary called the \textit{observable inscribed radius}
that measures the difference between non-negative $1$-Lipschitz functions with Dirichlet boundary condition and zero.
We will refer to the formulation of the observable diameter on metric measure spaces.

Let $X=(X,d_{X},\mu_{X})$ be a metric measure space with boundary.
Let $\rho_{\partial X}:X\to [0,\infty)$ stand for the distance function from the boundary $\partial X$ defined as $\rho_{\partial X}(x):=d_{X}(x,\partial X)$.
The function $\rho_{\partial X}$ is $1$-Lipschitz with $\rho_{\partial X}|_{\partial X}=0$.
The \textit{inscribed radius $\IR X$ of $X$} is defined to be the supremum of the distance function $\rho_{\partial X}$ over $X$.
We extend the notion of the inscribed radius to all subsets of $X$.
For $\Omega \subset X$,
we define the \textit{inscribed radius $\IR \Omega$ of $\Omega$} as follows:
If $\Omega \neq \emptyset$,
then
\begin{equation}\label{eq:inscribed radius}
\IR \Omega:=\sup_{x \in \Omega} \rho_{\partial X}(x);
\end{equation}
if $\Omega=\emptyset$,
then $\IR \Omega:=0$.
For $\xi \in (-\infty,1]$,
let us define the \textit{$\xi$-partial inscribed radius $\PI(X;\xi)$ of $X$} by
\begin{equation}\label{eq:partial inscribed radius}
\PI(X;\xi):=\inf_{\Omega \subset X}\,\IR \Omega,
\end{equation}
where the infimum is taken over all Borel subsets $\Omega$ with $\mu_{X}(\Omega) \geq \xi$.

We set a screen $I:= [0,\infty)$.
For a $1$-Lipschitz function $\varphi:X\to I$ with $\varphi|_{\partial X}=0$,
we call the metric measure space with boundary
\begin{equation}\label{eq:screen}
I_{\varphi}:=\left(I,d_{I},m_{I,\varphi}\right)
\end{equation}
the \textit{$\varphi$-screen},
where $m_{I,\varphi}$ denotes the push-forward $\varphi_{\#}\mu_{X}$ of $\mu_{X}$ by $\varphi$.

We now define the following quantity:
\begin{defi}\label{defi:observable inscribed radius}
For $\eta>0$,
we define the \textit{$\eta$-observable inscribed radius $\OI(X;-\eta)$ of $X$} by
\begin{equation*}
\OI(X;-\eta):=\sup_{\varphi}\,\PI(I_{\varphi};1-\eta),
\end{equation*}
where the supremum is taken over all $1$-Lipschitz functions $\varphi:X\to I$ with $\varphi|_{\partial X}=0$.
\end{defi}
We remark that
$\OI(X;-\eta)=0$ for all $\eta \geq 1$.
Furthermore,
$\OI(X;-\eta)$ is monotone non-increasing in $\eta$.

We also introduce the following notion:
\begin{defi}\label{defi:Dirichlet Levy family}
We say that
a sequence $\{X_{n}\}$ of metric measure spaces with boundary is a \textit{boundary concentration family} if
for every $\eta>0$
\begin{equation*}
\lim_{n\to \infty} \, \OI \left(X_{n};-\eta \right)=0.
\end{equation*}
\end{defi}

\begin{rem}\label{rem:characterization of Dirichlet Levy}
Let $\{X_{n}\}$ denote a sequence of metric measure spaces with boundary $X_{n}=(X_{n},d_{X_{n}},\mu_{X_{n}})$.
By the definition of the observable inscribed radius,
$\{X_{n}\}$ is a boundary concentration family if and only if
for every sequence $\{\varphi_{n}\}$ of $1$-Lipschitz functions $\varphi_{n}:X_{n}\to I$ with $\varphi_{n}|_{\partial X_{n}}=0$,
we have $d_{KF}(\varphi_{n},0) \to 0$ as $n\to \infty$,
where $d_{KF}(\varphi_{n},0)$ is the \textit{Ky Fan metric} between $\varphi_{n}$ and $0$ defined as
\begin{equation*}
d_{KF}(\varphi_{n},0):=\inf \left\{\, \epsilon \geq 0 \mid \mu_{X_{n}} \left(  \left\{\, x\in X_{n} \mid \varphi_{n}(x)>\epsilon \right\} \right) \leq \epsilon \,\right\}.
\end{equation*}
We further see that the following are equivalent (see Proposition \ref{prop:characterization of Dirichlet Levy}):
\begin{enumerate}\setlength{\itemsep}{+0.7mm}
\item $\{X_{n}\}$ is a boundary concentration family;
\item for every sequence $\{\Omega_{n}\}$ of Borel subsets $\Omega_{n} \subset X_{n}$ satisfying $\liminf_{n\to \infty} \mu_{X_{n}}(\Omega_{n})>0$,
         we have $\lim_{n\to \infty}\, d_{X_{n}}(\Omega_{n},\partial X_{n})=0$;
\item $\lim_{n\to \infty}\,\mu_{X_{n}}(B_{r}(\partial X_{n}))=1$ for every $r>0$,
         where $B_{r}(\partial X_{n})$ is the closed $r$-neighborhood of $\partial X_{n}$.
\end{enumerate}
\end{rem}



\subsection{Dirichlet eigenvalues and concentration phenomena}
We study relation between boundary concentration phenomena and large spectral gap phenomena for Dirichlet eigenvalues of Laplacian.
For $n\geq 2$,
let $(M,d_{M},m_{M,f})$ be an $n$-dimensional weighted Riemannian manifold with boundary,
namely,
$M=(M,g)$ be an $n$-dimensional,
connected complete Riemannian manifold with boundary,
$d_{M}$ is the Riemannian distance on $M$,
and
\begin{equation}\label{eq:weighted volume measure}
m_{M,f}:=e^{-f} \,\vol_{M}
\end{equation}
for some smooth function $f:M\to \mathbb{R}$,
where $\vol_{M}$ is the Riemannian volume measure on $M$.
The \textit{weighted Laplacian $\Delta_{f}$} is defined by
\begin{equation}\label{eq:weighted Laplacian}
\Delta_{f}:=\Delta+g(\nabla f,\nabla \cdot),
\end{equation}
where $\nabla$ is the gradient,
and $\Delta$ is the Laplacian defined as the minus of the trace of Hessian.
In the case where $M$ is compact,
we consider the following Dirichlet eigenvalue problem with respect to $\Delta_{f}$:
\begin{equation*}
\begin{cases}
  \Delta_{f}\, \phi=\nu\, \phi & \text{in $\inte M$};\\
  \phi=0                        & \text{on $\bm$},
\end{cases}
\end{equation*}
where $\inte M$ denotes the interior of $M$.
We denote by
\begin{equation}\label{eq:notation of Dirichlet eigenvalue}
0< \nu_{f,1}(M) < \nu_{f,2}(M) \leq \dots \leq \nu_{f,k}(M)\leq \dots \nearrow +\infty
\end{equation}
the all Dirichlet eigenvalues of $\Delta_{f}$,
counting multiplicity.

For a smooth function $f:M\to \mathbb{R}$ such that $m_{M,f}$ is a Borel probability measure,
we study the metric measure space with boundary
\begin{equation}\label{eq:weighted Riemannian manifold}
(M,f):=(M,d_{M},m_{M,f}).
\end{equation}
Our first main result is the following:
\begin{thm}\label{thm:Dirichlet eigenvalue and Dirichlet Levy family}
Let $\{(M_{n},f_{n})\}$ be a sequence of compact metric measure spaces with boundary defined as $(\ref{eq:weighted Riemannian manifold})$.
If we have $\nu_{f_{n},1}(M_{n})\to \infty$ as $n\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{thm}
This is an analogue of the Gromov-V. D. Milman theorem for closed manifolds (compact manifolds without boundary) (see Theorem 4.1 and its corollary in \cite{GM}).
We show Theorem \ref{thm:Dirichlet eigenvalue and Dirichlet Levy family} by using relation between the observable inscribed radii and $\nu_{f,1}(M)$ (see Proposition \ref{prop:logarithmic Dirichlet eigenvalue and observable inscribed radius}).

For higher eigenvalues,
we will establish the following assertion under $\ric^{\infty}_{f,M}\geq 0$ and $H_{f,\bm}\geq 0$,
where $\ric^{\infty}_{f,M}$ and $H_{f,\bm}$ are the infimum of the $\infty$-weighted Ricci curvature and the weighted mean curvature on $M$ and on $\bm$,
respectively (more precisely, see Subsection \ref{sec:Curvatures}):
\begin{thm}\label{thm:higher order Dirichlet eigenvalue and Dirichlet Levy family}
Let $\{(M_{n},f_{n})\}$ be a sequence of compact metric measure spaces with boundary defined as $(\ref{eq:weighted Riemannian manifold})$.
Assume that
$\ric^{\infty}_{f_{n},M_{n}}\geq 0$ and $H_{f_{n},\bm_{n}}\geq 0$.
If there exists $k\geq 1$ such that $\nu_{f_{n},k}(M_{n})\to \infty$ as $n\to \infty$,
then $\{(M_{n},f_{n})\}$ is a boundary concentration family.
\end{thm}

Theorem \ref{thm:higher order Dirichlet eigenvalue and Dirichlet Levy family} is an analogue of the Funano-Shioya theorem for closed manifolds of non-negative $\infty$-weighted Ricci curvature (see Corollary 1.4 in \cite{FSh}).
One of key ingredients of the proof is to obtain an upper bound of the ratio $\nu_{f,k}(M)/\nu_{f,1}(M)$ in terms of $C\,k^{2}$ for some universal constant $C>0$ under $\ric^{\infty}_{f,M}\geq 0$ and $H_{f,\bm}\geq 0$ (see Theorem \ref{thm:universal inequality}).
We obtain such universal estimate by combining an improved Cheeger inequality of Kwak, Lau, Lee, Oveis Gharan and Trevisan \cite{KLLOT},
and an isoperimetric inequality of Wang \cite{Wa} (see Subsections \ref{sec:Dirichlet isoperimetric constants}, \ref{sec:Isoperimetric inequalities}).



\subsection{Comparisons and concentration phenomena}\label{sec:Comparisons and concentration phenomena}
To understand boundary concentration phenomena,
we establish comparison theorems of the observable inscribed radii under a lower curvature Ricci curvature bound,
and a lower mean curvature bound for the boundary.

We first present finite dimensional comparisons.
Let $M$ be an $n$-dimensional,
connected complete Riemannian manifold with boundary with $\vol_{M}(M)<\infty$.
We study metric measure space with boundary
\begin{equation}\label{eq:normalized metric measure space with boundary}
M:=(M,d_{M},m_{M}),\quad m_{M}:=\frac{1}{\vol_{M} (M)} \,\vol_{M}.
\end{equation}
Let $\ric_{\bm^{\perp}}$ stand for the infimum of the Ricci curvature in the $\bm$-radial direction on $M$,
and $H_{\bm}$ the infimum of the mean curvature on $\bm$ (more precisely, see Subsection \ref{sec:Curvatures}).

For $\kappa \in \mathbb{R}$,
let $M^{n}_{\kappa}$ be the $n$-dimensional space form with constant curvature $\kappa$.
For $\lambda \in \mathbb{R}$,
we say that $\kappa$ and $\lambda$ satisfy the \textit{ball-condition}
if there exists a closed ball $\ball$ in $M^{n}_{\kappa}$ whose boundary has constant mean curvature $(n-1)\lambda$.
Let $\const$ denote its radius.
Note that $\kappa$ and $\lambda$ satisfy the ball-condition if and only if either
(1) $\kappa>0$; 
(2) $\kappa=0$ and $\lambda>0$;
or (3) $\kappa<0$ and $\lambda>\sqrt{\vert \kappa \vert}$.
We say that $\kappa$ and $\lambda$ satisfy the \textit{convex-ball-condition}
if they satisfy the ball-condition and $\lambda \geq 0$.

Let us prepare the following finite dimensional model spaces: 
(1) For $\kappa$ and $\lambda$ satisfying the ball-condition,
we call the metric measure space with boundary
\begin{equation}\label{eq:ball model}
\ball=\bigl(\ball,d_{\ball},m_{\ball} \bigl)
\end{equation}
the \textit{ball-model-space};
(2) For $\kappa<0$ and $\lambda:=\sqrt{\vert \kappa \vert}$,
we consider the warped product space $M^{n}_{\kappa,\lambda}:=([0,\infty) \times \mathbb{S}^{n-1},dt^{2}+e^{-2\lambda t}\,ds_{n-1}^{2})$,
where $(\mathbb{S}^{n-1},ds_{n-1}^{2})$ is the $(n-1)$-dimensional standard unit sphere.
We call the metric measure space with boundary
\begin{equation}\label{eq:warped product model}
M^{n}_{\kappa,\lambda}=\bigl(M^{n}_{\kappa,\lambda},d_{M^{n}_{\kappa,\lambda}},m_{M^{n}_{\kappa,\lambda}}\bigl)
\end{equation}
the \textit{warped-product-model-space} (cf. Remark \ref{rem:formulation of finite dimensional model spaces}).

We have the following finite dimensional comparison theorem:
\begin{thm}\label{thm:main theorem}
Let $\bm$ be compact.
We assume $\ric_{\bm^{\perp}}\geq (n-1)\kappa$ and $H_{\bm}\geq (n-1)\lambda$.
Then for every $\eta \in (0,1]$
the following hold:
\begin{enumerate}
\item if $\kappa$ and $\lambda$ satisfy the ball-condition,
         then
         \begin{equation*}
         \OI(M;-\eta) \leq \OI(\ball;-\eta);
         \end{equation*}
\item if $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$,
         then
         \begin{equation*}
         \OI(M;-\eta) \leq \OI(M^{n}_{\kappa,\lambda};-\eta).
         \end{equation*}
\end{enumerate}
\end{thm}
\begin{rem}\label{rem:finite volume}
For (1) of Theorem \ref{thm:main theorem},
we always have $\vol_{M} (M)<\infty$.
Indeed,
the Heintze-Karcher theorem (Theorem 2.1 in \cite{HK}) leads to
\begin{equation*}
\frac{\vol_{M} (M)}{\vol_{\bm} (\bm)}\leq \frac{\vol_{\ball} (\ball)}{\vol_{\partial \ball} (\partial \ball)}.
\end{equation*}
Similarly,
for (2),
the Heintze-Karcher theorem guarantees that
the Riemannian volume $\vol_{M} (M)$ of $M$ is finite.
\end{rem}

The proof of Theorem \ref{thm:main theorem} is based on comparison geometry of manifolds with boundary
established by Heintze and Karcher \cite{HK}, Kasue \cite{K1}, \cite{K2}, the author \cite{S1}, \cite{S2}, and so on (see Subsection \ref{sec:Comparison theorems}).
We first estimate observable inscribed radii under lower weighted curvature bounds by using relative volume comparison theorems for metric neighborhoods of boundaries (see Theorems \ref{thm:weighted main theorem} and \ref{thm:twisted weighted main theorem}).
We conclude Theorem \ref{thm:main theorem} by computing the observable inscribed radii of finite dimensional model spaces (see Lemma \ref{lem:observable and separation on model}).

We next produce infinite dimensional comparisons for metric measure spaces with boundary $(M,f)$ defined as (\ref{eq:weighted Riemannian manifold}) under $\ric^{\infty}_{f,\bm^{\perp}}\geq K$ and $H_{f,\bm}\geq \Lambda$ for $K,\Lambda\in \mathbb{R}$,
where $\ric^{\infty}_{f,\bm^{\perp}}$ is the infimum of the $\infty$-weighted Ricci curvature in the $\bm$-radial direction on $M$ (see Subsection \ref{sec:Curvatures}).
We prepare the following infinite dimensional model spaces: 
(1) For $K>0,\,\Lambda \in \mathbb{R}$,
we call the metric measure space with boundary
\begin{equation}\label{eq:Gaussian model space}
G_{K,\Lambda}:=\left(I,d_{I}, \frac{e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}}{\int_{I}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}\,    dt} \vol_{I} \right)
\end{equation}
the \textit{half-Gaussian-model-space};
(2) For $\Lambda>0$,
we call
\begin{equation}\label{eq:exponential model space}
E_{\Lambda}:=\left(I,d_{I}, \Lambda\,e^{-\Lambda\,t} \vol_{I} \right)
\end{equation}
the \textit{exponential-model-space}.
We remark that
for $K,\Lambda\in \mathbb{R}$,
the value $\int_{I}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}\,    dt$ is finite if and only if
either (1) $K>0$;
or (2) $K=0$ and $\Lambda>0$.
Moreover,
if $K=0$ and $\Lambda>0$,
then we see
\begin{equation*}
\frac{e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}}{\int_{I}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}\,    dt}=\Lambda\,e^{-\Lambda\,t}.
\end{equation*}
We observe that
our infinite dimensional model spaces appear as limits of sequences of finite dimensional model spaces (see Subsection \ref{sec:Infinite dimensional model spaces and distribution laws}).

We have the following infinite dimensional comparison:
\begin{thm}\label{thm:infinite dimensional main theorem}
Let $\bm$ be compact.
Let us assume $\ric^{\infty}_{f,\bm^{\perp}}\geq K$ and $H_{f,\bm}\geq \Lambda$.
Then for every $\eta \in (0,1]$
the following hold:
\begin{enumerate}
\item if $K>0$ and $\Lambda \in \mathbb{R}$,
         then
         \begin{equation*}
         \OI((M,f);-\eta) \leq \OI(G_{K,\Lambda};-\eta);
         \end{equation*}
\item if $K=0$ and $\Lambda>0$,
         then
         \begin{equation*}
         \OI((M,f);-\eta) \leq \OI(E_{\Lambda};-\eta).
         \end{equation*}
\end{enumerate}
\end{thm}
To prove Theorem \ref{thm:infinite dimensional main theorem},
we develop comparison geometry of manifolds with boundary under $\ric^{\infty}_{f,\bm^{\perp}}\geq K$ and $H_{f,\bm}\geq \Lambda$ for $K,\Lambda\in \mathbb{R}$ (see Subsection \ref{sec:Relative volume comparisons}).
We will show a relative comparison theorem for metric neighborhoods of boundaries (see Theorem \ref{thm:relative volume comparison}).

Having Theorems \ref{thm:main theorem} and \ref{thm:infinite dimensional main theorem} at hand,
we will study various boundary concentration phenomena of sequences of metric measure spaces with boundary (see Section \ref{sec:Boundary concentration phenomena}).
For instance,
for a sequence of ball-model-spaces,
we conclude the following:
\begin{cor}\label{cor:ball model Levy family}
If $\kappa$ and $\lambda$ satisfy the convex-ball-condition,
then the sequence $\{\ball\}$ is a boundary concentration family.
\end{cor}
\begin{rem}
In the case where $\kappa>0$ and $\lambda<0$,
the sequence $\{\ball\}$ is not a boundary concentration family.
Indeed,
for $r\in (0,\const-C_{\kappa,0})$,
if we define $\Omega_{n} \subset \ball$ as the $r/2$-neighborhood of the metric sphere with same center as $\ball$ and radius $C_{\kappa,0}$,
then $\liminf_{n\to \infty} m_{\ball}(\Omega_{n})>0$ and $\lim_{n\to \infty} d_{\ball}(\Omega_{n},\partial \ball)>0$ (see Remark \ref{rem:characterization of Dirichlet Levy} and Proposition \ref{prop:characterization of Dirichlet Levy}).
\end{rem}



\subsection{Organization}
In Section \ref{sec:Preliminaries},
we review basics of weighted Riemannian manifolds with boundary,
and examine their geometric and analytic properties.
In Section \ref{sec:Invariants},
we introduce some invariants on metric measure spaces with boundary,
and investigate their fundamental properties.
In Section \ref{sec:Dirichlet eigenvalues},
we prove Theorems \ref{thm:Dirichlet eigenvalue and Dirichlet Levy family} and \ref{thm:higher order Dirichlet eigenvalue and Dirichlet Levy family}.
In Section \ref{sec:Comparisons},
we prove Theorem \ref{thm:main theorem}.
In Section \ref{sec:Infinite dimensional comparisons},
we prove Theorem \ref{thm:infinite dimensional main theorem}.

Section \ref{sec:Boundary concentration phenomena} is devoted to the collection of boundary concentration phenomena of sequences of metric measure spaces with boundary.
We will determine the critical scale orders of some sequences of finite dimensional model spaces (see Theorems \ref{thm:sequence of hemisphere}, \ref{thm:sequence of Euclidean ball}, \ref{thm:warped product model Levy family}).
We also prove Corollary \ref{cor:ball model Levy family}.
Furthermore,
we construct several non-trivial examples of boundary concentration families (see Examples \ref{ex:finite dimensional example} and \ref{ex:one dimensional example}).



\subsection{{\rm Acknowledgements}}
The author expresses his gratitude to Ryunosuke Ozawa and Kohei Suzuki for fruitful discussions and encouragement.
The author would like to thank Shin-ichi Ohta for his useful comments.
One of his comment leads to the study of Section \ref{sec:Infinite dimensional comparisons}.
The author would also like to thank Daisuke Kazukawa for informing him of Proposition \ref{prop:Kazukawa} with its proof.
The author is deeply grateful to Kei Funano for his interests in this paper,
valuable comments,
and informing him of \cite{CGY}.
