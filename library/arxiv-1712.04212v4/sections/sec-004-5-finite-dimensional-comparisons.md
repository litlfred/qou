---
doc_id: arxiv-1712.04212v4
doc_title: "1. Introduction"
section_id: sec-004-5-finite-dimensional-comparisons
section_title: "Finite dimensional comparisons"
section_number: 5
pages: 22-26
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.91
doc_brief: "1. Introduction — In this paper, we consider a concentration of measure problem on Riemannian manifolds with boundary."
---
\label{sec:Comparisons}



\subsection{Estimates}
To prove Theorem \ref{thm:main theorem},
we begin with the following:
\begin{lem}\label{lem:key lemma}
Let $\bm$ be compact.
For $N\in [n,\infty)$,
let us assume $\ric^{N}_{f,\bm^{\perp}}\geq (N-1)\kappa$ and $H_{f,\bm} \geq (N-1)\lambda$.
Suppose additionally that
$\IR M\leq D$ for some $D>0$.
For $\eta \in (0,1)$,
let $\Omega \subset M$ be a Borel subset with $m_{M,f}(\Omega)\geq \eta$ and $d_{M}(\Omega,\bm)>0$.
Then we have
\begin{equation*}
s_{N,\kappa,\lambda}(d_{M}(\Omega,\bm)) \leq s_{N,\kappa,\lambda}(D)(1-\eta),
\end{equation*} 
where $s_{N,\kappa,\lambda}$ is the function defined as $(\ref{eq:one dimensional volume growth})$.
\end{lem}
\begin{proof}
We put $r:=d_{M}(\Omega,\bm)$.
Since the open $r$-neighborhood of $\bm$ and $\Omega$ are mutually disjoint,
we see
\begin{equation*}
\eta \leq m_{M,f}(\Omega)\leq 1-m_{M,f}(B_{r}(\bm)).
\end{equation*}
From $\IR M\leq D$
we derive $M=B_{D}(\bm)$;
in particular,
we have $m_{M,f}(B_{D}(\bm))=1$.
Therefore,
Theorem \ref{thm:volume comparison} leads to
\begin{equation*}
\eta \leq 1-\frac{m_{M,f}(B_{r}(\bm))}{m_{M,f}(B_{D}(\bm))}\leq 1-\frac{s_{N,\kappa,\lambda}(r)}{s_{N,\kappa,\lambda}(D)}.
\end{equation*}
This yields the lemma.
\end{proof}

One can also show the following lemma by using Theorem \ref{thm:twisted volume comparison} instead of Theorem \ref{thm:volume comparison} in the proof of Lemma \ref{lem:key lemma}.
We omit the proof.
\begin{lem}\label{lem:twisted key lemma}
Let $\bm$ be compact.
Assume $\ric^{1}_{f,\bm^{\perp}}\geq (n-1) \,\kappa \,e^{\frac{-4f}{n-1}}$ and $H_{f,\bm}\geq (n-1)\,\lambda\,e^{\frac{-2f}{n-1}}$.
Suppose additionally that
$\IR M\leq D$ and $f\leq (n-1) \delta$ for some $D>0$ and $\delta \in \mathbb{R}$.
We further assume that
one of the following holds:
\begin{enumerate}
\item $\kappa$ and $\lambda$ satisfy the convex-ball-condition;
\item $\kappa \leq 0$ and $\lambda=\sqrt{\vert \kappa \vert}$.
\end{enumerate}
For $\eta \in (0,1)$,
let $\Omega \subset M$ be a Borel subset with $m_{M,f}(\Omega)\geq \eta$ and $d_{M}(\Omega,\bm)>0$.
Then we have
\begin{equation*}
s_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(d_{M}(\Omega,\bm)) \leq s_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(D)(1-\eta).
\end{equation*} 
\end{lem}

Recall that
$s_{\kappa,\lambda}(t)$ is the solution of the equation $\psi''(t)+\kappa\, \psi(t)=0$ with $\psi(0)=1,\,\psi'(0)=-\lambda$.
For $N \in (1,\infty)$,
and $\kappa$ and $\lambda$ satisfying the ball-condition,
we define a function $v_{N,\kappa,\lambda}:[0,\const]\to [0,1]$ by
\begin{equation}\label{eq:ball function}
v_{N,\kappa,\lambda}(r):=\frac{\int^{\const}_{r}\,s^{N-1}_{\kappa,\lambda}(t)\,dt}{\int^{\const}_{0}\,s^{N-1}_{\kappa,\lambda}(t)\,dt}.
\end{equation}

Under the curvature condition (\ref{eq:finite dimensional curvature bound}),
we produce the following:
\begin{thm}\label{thm:weighted main theorem}
Let $\bm$ be compact.
For $N\in [n,\infty)$,
let us assume $\ric^{N}_{f,\bm^{\perp}}\geq(N-1)\kappa$ and $H_{f,\bm}\geq (N-1)\lambda$.
Then for every $\eta \in (0,1]$
the following hold:
\begin{enumerate}
\item if $\kappa$ and $\lambda$ satisfy the ball-condition,
         then
         \begin{equation*}
         \OI((M,f);-\eta) \leq v^{-1}_{N,\kappa,\lambda}(\eta);
         \end{equation*}
\item if $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$,
         then
         \begin{equation*}
         \OI((M,f);-\eta) \leq \frac{1}{(N-1)\lambda}\,\log \frac{1}{\eta}.
         \end{equation*}
\end{enumerate}
\end{thm}
\begin{proof}
We may assume that $\eta<1$.
By Lemma \ref{lem:observable inscribed radius is smaller than Dirichlet separation distance},
it suffices to prove that
$\DS((M,f);\eta)$ is at most the right hand side of the desired inequality in each case.
We may assume that
$\DS((M,f);\eta)$ is positive.
We fix a Borel subset $\Omega \subset M$ with $m_{M,f}(\Omega)\geq \eta$ and $d_{M}(\Omega,\bm)>0$.

Let us consider the case where
$\kappa$ and $\lambda$ satisfy the ball-condition.
In this case,
Theorem \ref{thm:inscribed radius comparison} implies $\IR M\leq \const$.
By using Lemma \ref{lem:key lemma},
\begin{equation*}
\eta \leq 1-\frac{s_{N,\kappa,\lambda}(d_{M}(\Omega,\bm))}{s_{N,\kappa,\lambda}(\const)}=v_{N,\kappa,\lambda}(d_{M}(\Omega,\bm)).
\end{equation*}
Hence,
$d_{M}(\Omega,\bm) \leq v^{-1}_{N,\kappa,\lambda}(\eta)$.
This proves $\DS((M,f);\eta)\leq v^{-1}_{N,\kappa,\lambda}(\eta)$.
We arrive at the desired inequality.

We next consider the case where
$\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$.
Notice that $s_{\kappa,\lambda}(t)=e^{-\lambda t}$.
In view of Lemma \ref{lem:key lemma},
we see
\begin{equation*}
\eta \leq 1-\frac{s_{N,\kappa,\lambda}(r)}{s_{N,\kappa,\lambda}(\IR M)} \leq 1-\frac{s_{N,\kappa,\lambda}(r)}{\int^{\infty}_{0}\, s^{N-1}_{\kappa,\lambda}(t)\,dt}=e^{-(N-1)\lambda \,r},
\end{equation*}
where we put $r:=d_{M}(\Omega,\bm)$.
In particular,
$d_{M}(\Omega,\bm)$ is smaller than or equal to the right hand side of the desired one.
We obtain
\begin{equation*}
\DS((M,f);\eta)\leq \frac{1}{(N-1)\lambda}\,\log \frac{1}{\eta}.
\end{equation*}
Thus,
we complete the proof.
\end{proof}

We also have the following estimate under the condition (\ref{eq:one dimensional curvature bound}):
\begin{thm}\label{thm:twisted weighted main theorem}
Let $\bm$ be compact.
Assume
$\ric^{1}_{f,\bm^{\perp}}\geq (n-1) \,\kappa \,e^{\frac{-4f}{n-1}}$ and $H_{f,\bm}\geq (n-1)\,\lambda\,e^{\frac{-2f}{n-1}}$.
Suppose additionally that
$f\leq (n-1) \delta$ for some $\delta \in \mathbb{R}$.
Then for every $\eta \in (0,1]$
the following hold:
\begin{enumerate}
\item if $\kappa$ and $\lambda$ satisfy the convex-ball-condition,
         then
         \begin{equation*}
         \OI((M,f);-\eta) \leq v^{-1}_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(\eta);
         \end{equation*}
\item if $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$,
         then
         \begin{equation*}
         \OI((M,f);-\eta) \leq \frac{1}{(n-1)\lambda\,e^{-2\delta}}\,\log \frac{1}{\eta}.
         \end{equation*}
\end{enumerate}
\end{thm}
\begin{proof}
The proof is similar to that of Theorem \ref{thm:weighted main theorem}.
For a fixed $\Omega \subset M$ with $m_{M,f}(\Omega)\geq \eta,\,d_{M}(\Omega,\bm)>0$,
it suffices to estimate $d_{M}(\Omega,\bm)$ from above by the right hand side of the desired inequality in each case.

In the case where
$\kappa$ and $\lambda$ satisfy the convex-ball-condition,
from Theorem \ref{thm:twisted inscribed radius comparison} and Lemma \ref{lem:twisted key lemma}
we derive
\begin{equation*}
\eta \leq 1-\frac{s_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(d_{M}(\Omega,\bm))}{s_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(C_{\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}})}=v_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(d_{M}(\Omega,\bm)).
\end{equation*}
In particular,
$d_{M}(\Omega,\bm) \leq v^{-1}_{n,\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(\eta)$.
This is the desired one.

If $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$,
then in view of Lemma \ref{lem:twisted key lemma} we see
\begin{equation*}
\eta \leq 1-\frac{s_{n,\kappa \,e^{-4\delta},\lambda \,e^{-2\delta}}(r)}{\int^{\infty}_{0}\, s^{n-1}_{\kappa\,e^{-4\delta},\lambda\,e^{-2\delta}}(t)\,dt}=e^{-(n-1)\lambda \,e^{-2\delta} \,r},
\end{equation*}
where $r:=d_{M}(\Omega,\bm)$.
From the above inequality,
we deduce
\begin{equation*}
d_{M}(\Omega,\bm) \leq \frac{1}{(n-1)\lambda e^{-2\,\delta}}\,\log \frac{1}{\eta}.
\end{equation*}
This completes the proof of Theorem \ref{thm:twisted weighted main theorem}.
\end{proof}



\subsection{Proof of Theorem \ref{thm:main theorem}}

In order to conclude Theorem \ref{thm:main theorem},
we calculate the invariants of the finite dimensional model spaces.
\begin{lem}\label{lem:observable and separation on model}
For every $\eta \in (0,1]$
the following hold:
\begin{enumerate}
\item for the ball-model-space $\ball$ defined as $(\ref{eq:ball model})$,
         \begin{equation*}
         \OI(\ball;-\eta)=\DS(\ball;\eta)=v^{-1}_{n,\kappa,\lambda}(\eta);
         \end{equation*}
\item for the warped-product-model-space $M^{n}_{\kappa,\lambda}$ defined as $(\ref{eq:warped product model})$,
         \begin{equation*}
         \OI(M^{n}_{\kappa,\lambda};-\eta)=\DS(M^{n}_{\kappa,\lambda};\eta)=\frac{1}{(n-1)\lambda}\,\log \frac{1}{\eta}.
         \end{equation*}
\end{enumerate}
\end{lem}
\begin{proof}
Let us present the equality for $\ball$.
We show
\begin{equation}\label{eq:separation equal ball model}
\DS(\ball;\eta)=v^{-1}_{n,\kappa,\lambda}(\eta).
\end{equation}
Let $B_{\eta} \subset \ball$ denote the closed geodesic ball with same center as $\ball$ and $m_{\ball}(B_{\eta})=\eta$.
For the radius $r_{\eta}$ of $B_{\eta}$,
we see
\begin{equation*}
\DS \left(\ball;\eta \right)=d_{\ball}\left(B_{\eta},\partial \ball \right)=\const-r_{\eta}.
\end{equation*}
It holds that
\begin{equation*}
\eta=m_{\ball}(B_{\eta})=\frac{\int^{\const}_{\const-r_{\eta}}\,s^{n-1}_{\kappa,\lambda}(t)\,dt}{\int^{\const}_{0}\,s^{n-1}_{\kappa,\lambda}(t)\,dt}=v_{n,\kappa,\lambda}\left(\const-r_{\eta}\right);
\end{equation*}
in particular,
$\const-r_{\eta}=v^{-1}_{n,\kappa,\lambda}(\eta)$.
This yields (\ref{eq:separation equal ball model}).
Since $\supp m_{\ball}$ coincides with $\ball$,
Proposition \ref{prop:Kazukawa} and (\ref{eq:separation equal ball model}) imply the desired one.

For the warped-product-model-space $M^{n}_{\kappa,\lambda}$,
the same argument as in the proof of $\ball$ leads to the desired equality.
\end{proof}

We are now in a position to prove Theorem \ref{thm:main theorem}.

\begin{proof}[Proof of Theorem \ref{thm:main theorem}]
Let $\bm$ be compact.
Assume $\ric_{\bm^{\perp}}\geq (n-1)\kappa$ and $H_{\bm}\geq (n-1)\lambda$.
Letting $f=\log \vol_{M}(M)$ and $N=n$ in Theorem \ref{thm:weighted main theorem},
for $\eta \in (0,1]$
we have the following (cf. Remark \ref{rem:finite volume}):
\begin{enumerate}
\item if $\kappa$ and $\lambda$ satisfy the ball-condition,
         then
         \begin{equation*}
         \OI(M;-\eta) \leq v^{-1}_{n,\kappa,\lambda}(\eta);
         \end{equation*}
\item if $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$,
         then
         \begin{equation*}
         \OI(M;-\eta) \leq \frac{1}{(n-1)\lambda}\,\log \frac{1}{\eta}.
         \end{equation*}
\end{enumerate}
By Lemma \ref{lem:observable and separation on model},
we complete the proof of Theorem \ref{thm:main theorem}.
\end{proof}
