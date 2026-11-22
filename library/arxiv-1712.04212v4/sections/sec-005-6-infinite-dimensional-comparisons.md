---
doc_id: arxiv-1712.04212v4
doc_title: "1. Introduction"
section_id: sec-005-6-infinite-dimensional-comparisons
section_title: "Infinite dimensional comparisons"
section_number: 6
pages: 26-30
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.951
doc_brief: "1. Introduction — In this paper, we consider a concentration of measure problem on Riemannian manifolds with boundary."
---
\label{sec:Infinite dimensional comparisons}



\subsection{Relative volume comparisons}\label{sec:Relative volume comparisons}
In order to prove Theorem \ref{thm:infinite dimensional main theorem},
we develop comparison geometry of manifolds with boundary under the curvature condition (\ref{eq:infinite dimensional curvature bound}).
We notice that
in our comparison theorems in this subsection,
$m_{M,f}$ need not be a probability measure.

We first show the following Laplacian comparison:
\begin{lem}\label{lem:Laplacian comparison}
Let $z\in \bm$.
Let us assume that
$\ric^{\infty}_{f}(\gamma'_{z}(t))\geq K$ for all $t \in (0,\tau(z))$,
and $H_{f,z}\geq \Lambda$.
Then for all $t \in (0,\tau(z))$
\begin{equation*}
\Delta_{f} \rho_{\bm}(\gamma_{z}(t))\geq Kt+\Lambda.
\end{equation*}
\end{lem}
\begin{proof}
Define $h_{f,z}:=\left(\Delta_{f}\rho_{\bm}\right) \circ \gamma_{z}$.
By applying the Bochner formula (\ref{eq:Bochner formula}) to the distance function $\rho_{\bm}$,
we obtain
\begin{align*}
0 &   =   \ric^{\infty}_{f}(\gamma'_{z}(t))+\Vert \Hess \rho_{\bm}\Vert^{2}_{\HS}\left(\gamma_{z}(t)\right)-g\left(\nabla \Delta_{f}\rho_{\bm},\nabla \rho_{\bm}  \right)(\gamma_{z}(t))\\
   &\geq K-h'_{f,z}(t).
\end{align*}
It holds that $h_{f,z}(t)\to H_{f,z}$ as $t\to 0$,
and hence
\begin{equation*}
h_{f,z}(t) \geq Kt +H_{f,z}\geq Kt +\Lambda.
\end{equation*}
We arrive at the desired inequality.
\end{proof}

Furthermore,
we prove the following volume element comparison:
\begin{lem}\label{lem:volume element comparison}
Let $z\in \bm$.
Let us assume that
$\ric^{\infty}_{f}(\gamma'_{z}(t))\geq K$ for all $t \in (0,\tau(z))$,
and $H_{f,z}\geq \Lambda$.
Then for all $t_{1},t_{2} \in [0,\tau(z))$ with $t_{1}\leq t_{2}$
\begin{equation*}
\frac{\theta_{f}(t_{2},z)}{ \theta_{f}(t_{1},z)}\leq \frac{e^{-\frac{K}{2}\,t^{2}_{2}-\Lambda\,t_{2}}}{ e^{-\frac{K}{2}\,t^{2}_{1}-\Lambda\,t_{1}}    },
\end{equation*}
where $\theta_{f}(t,z)$ is defined as $(\ref{eq:volume element})$.
\end{lem}
\begin{proof}
By (\ref{eq:Laplacian representation}) and Lemma \ref{lem:Laplacian comparison},
for all $t \in (0,\tau(z))$
we see
\begin{equation*}
\frac{d}{dt}\log \frac{\theta_{f}(t,z)}{  e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}  }=-\Delta_{f}\rho_{\bm}(\gamma_{z}(t))+\left(Kt +\Lambda  \right) \leq 0.
\end{equation*}
This implies the lemma.
\end{proof}

We now conclude the following relative volume comparison:
\begin{thm}\label{thm:relative volume comparison}
Let $\bm$ be compact.
Let us assume that
$\ric^{\infty}_{f,\bm^{\perp}}\geq K$ and $H_{f,\bm}\geq \Lambda$.
Then for all $r,R>0$ with $r\leq R$
\begin{equation*}
\frac{m_{M,f}(B_{R}(\bm))}{ m_{M,f}(B_{r}(\bm))}\leq \frac{  \int^{R}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t} \,dt }{  \int^{r}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t} \,dt }.
\end{equation*}
\end{thm}
\begin{proof}
Using Lemma \ref{lem:volume element comparison},
for all $t_{1},t_{2}\geq 0$ with $t_{1}\leq t_{2}$ we have
\begin{equation*}
\bar{\theta}_{f}(t_{2},z)\; e^{-\frac{K}{2}\,t^{2}_{1}-\Lambda\,t_{1}} \leq \bar{\theta}_{f}(t_{1},z)\; e^{-\frac{K}{2}\,t^{2}_{2}-\Lambda\,t_{2}},
\end{equation*}
where $\bar{\theta}_{f}$ is defined as (\ref{eq:extended volume element}).
Let us integrate the both sides over $[0,r]$ with respect to $t_{1}$,
and over $[r,R]$ with respect to $t_{2}$.
It follows that
\begin{equation*}
\frac{\int^{R}_{r}\bar{\theta}_{f}(t_{2},z)\,dt_{2}}{\int^{r}_{0}\bar{\theta}_{f}(t_{1},z)\,dt_{1}}\leq \frac{\int^{R}_{r}\,  e^{-\frac{K}{2}\,t^{2}_{2}-\Lambda\,t_{2}}   \,dt_{2}}{  \int^{r}_{0}\,  e^{-\frac{K}{2}\,t^{2}_{1}-\Lambda\,t_{1}}   \,dt_{1}   }.
\end{equation*}
The formula (\ref{eq:integration formula}) yields
\begin{equation*}
          \frac{m_{M,f}( B_{R}(\bm))}{ m_{M,f}( B_{r}(\bm))  }\leq 1+\frac{\int^{R}_{r}\,  e^{-\frac{K}{2}\,t^{2}_{2}-\Lambda\,t_{2}}   \,dt_{2}}{  \int^{r}_{0}\,  e^{-\frac{K}{2}\,t^{2}_{1}-\Lambda\,t_{1}}   \,dt_{1}   }
    =      \frac{  \int^{R}_{0}\,e^{-\frac{K}{2}\,t^{2}_{2}-\Lambda\,t_{2}} \,dt_{2} }{  \int^{r}_{0}\,e^{-\frac{K}{2}\,t^{2}_{1}-\Lambda\,t_{1}} \,dt_{1} }.
\end{equation*}
We complete the proof of Theorem \ref{thm:relative volume comparison}.
\end{proof}

\begin{rem}
The author \cite{S1} has shown Lemmas \ref{lem:Laplacian comparison}, \ref{lem:volume element comparison} and Theorem \ref{thm:relative volume comparison} when $K=0$ and $\Lambda=0$ (see Lemmas 3.2, 3.4 and Theorem 5.5 in \cite{S1}, and cf. Remark \ref{rem:remark on the curvature assumption}).
\end{rem}

\begin{rem}
Under the same setting as in Theorem \ref{thm:relative volume comparison},
Morgan \cite{Mo} has obtained a similar absolute volume comparison theorem of Heintze-Karcher type (see Theorem 2 in \cite{Mo}).
\end{rem}



\subsection{Distribution laws}\label{sec:Infinite dimensional model spaces and distribution laws}
Before we show Theorem \ref{thm:infinite dimensional main theorem},
we present distribution laws concerning our infinite dimensional model spaces.

We observe that
our infinite dimensional model spaces appear as the limits of a sequence of hemispheres $\{B^{n}_{\kappa/n,0}\}$,
and that of Euclidean balls $\{B^{n}_{0,\lambda/n}\}$ for $\kappa,\lambda>0$ by letting $n\to \infty$.
\begin{prop}\label{prop:ball distribution laws}
Let us assume that
$\kappa$ and $\lambda$ satisfy the ball-condition.
Then the following distribution laws hold:
\begin{enumerate}
\item if $\kappa>0$ and $\lambda=0$,
         then
         \begin{equation*}
         \frac{d m_{I,\rho_{  \partial B^{n}_{\kappa/n,0   }     }}    }{dt} \to \frac{e^{-\frac{\kappa}{2}\,t^{2}}}{\int_{I}\,e^{-\frac{\kappa}{2}\,t^{2}}\,    dt}
         \end{equation*}
         as $n\to \infty$,
         where $m_{I,\rho_{ \partial B^{n}_{\kappa/n,0   }}}$ denotes the Borel probability measure of the $\rho_{ \partial B^{n}_{\kappa/n,0   }}$-screen $I_{\rho_{ \partial B^{n}_{\kappa/n,0   }}}$ defined as $(\ref{eq:screen})$;
         in particular,
         $m_{I,\rho_{ \partial B^{n}_{\kappa/n,0   }}}$ weakly converges to the Borel probability measure of the half-Gaussian-model-space $G_{\kappa,0}$ defined as $(\ref{eq:Gaussian model space})$;
\item if $\kappa=0$ and $\lambda>0$,
         then
         \begin{equation*}
         \frac{d   m_{I,\rho_{  \partial B^{n}_{0, \lambda/n  }     }} }{dt} \to \lambda\, e^{-\lambda t};
         \end{equation*}
         as $n\to \infty$;
         in particular,
         $m_{I,\rho_{  \partial B^{n}_{0,\lambda/n   }}}$ weakly converges to the measure of the exponential-model-space $E_{\lambda}$ defined as $(\ref{eq:exponential model space})$.
\end{enumerate}
\end{prop}
\begin{proof}
We notice that
if $\kappa$ and $\lambda$ satisfy the ball-condition,
then
\begin{align}\label{eq:basic calculation}
\frac{d m_{I,\rho_{ \partial \ball    }}    }{dt}&=\frac{s^{n-1}_{\kappa,\lambda}(t)}{\int^{\const}_{0}\,s^{n-1}_{\kappa,\lambda}(t)\,dt          },\,\, s_{\kappa,\lambda}(t)=-\sqrt{\kappa+\lambda^{2}}\,s_{\kappa}(t-\const),\\ \notag
\const&=\begin{cases}
                                       \dfrac{1}{\sqrt{\kappa}}\left(\dfrac{\pi}{2}-\tan^{-1}\dfrac{\lambda}{\sqrt{\kappa}} \right) & \text{if $\kappa>0$}, \\
                                       \lambda^{-1}                         & \text{if $\kappa =0$},\\
                                       \dfrac{1}{2\,\sqrt{\vert \kappa \vert}}\,\log \dfrac{\lambda+\sqrt{\vert \kappa \vert}}{\lambda-\sqrt{\vert \kappa \vert}} & \text{if $\kappa<0$},
                                   \end{cases}
\end{align}
where $s_{\kappa}(t)$ is a unique solution of the Jacobi equation $\psi''(t)+\kappa\, \psi(t)=0$ with $\psi(0)=0,\,\psi'(0)=1$;
in particular,
if $\kappa>0$,
then
\begin{equation}\label{eq:positive explicit calculation}
s_{\kappa,\lambda}(t)=\sqrt{1+\frac{\lambda^{2}}{\kappa}}\,\cos\sqrt{\kappa} \left(t+\frac{1}{\sqrt{\kappa} }\tan^{-1}  \frac{\lambda}{\sqrt{\kappa}} \right),
\end{equation}
and if $\kappa=0$,
then $s_{0,\lambda}(t)=1-\lambda\,t$.
Therefore,
in the case where $\kappa>0$ and $\lambda=0$,
the desired convergence follows from (\ref{eq:basic calculation}), (\ref{eq:positive explicit calculation}) and
\begin{equation*}
\cos^{n-1}\frac{t}{\sqrt{n}}\to e^{-\frac{t^{2}}{2}}.
\end{equation*}
In the case where $\kappa=0$ and $\lambda>0$,
the formula (\ref{eq:basic calculation}) yields
\begin{equation*}
\frac{d m_{I,\rho_{  \partial B^{n}_{0,\lambda/n   }     }}    }{dt}=\lambda\,\left(1-\frac{\lambda}{n}\,t \right)^{n-1}\to \lambda\, e^{-\lambda t}
\end{equation*}
as $n\to \infty$.
We complete the observation.
\end{proof}

We further mention that
the exponential-model-space also appears as the limit of a sequence of warped-product-model-spaces $\{M^{n}_{\kappa/n^{2},\lambda/n,}\}$ for $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$
when $n\to \infty$,
here $\lambda/n=\sqrt{\vert \kappa/n^{2} \vert}$.
\begin{prop}\label{prop:exponential distribution laws}
Let $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$.
Then
\begin{equation*}
\frac{d   m_{I,\rho_{  \partial M^{n}_{\kappa/n^{2},\lambda/n}   }} }{dt} \to \lambda\, e^{-\lambda t};
\end{equation*}
as $n\to \infty$;
in particular,
$m_{I,\rho_{ \partial M^{n}_{\kappa/n^{2},\lambda/n}   }}$ weakly converges to the Borel probability measure of the exponential-model-space $E_{\lambda}$.
\end{prop}
\begin{proof}
Let us note that
if $\kappa<0$ and $\lambda=\sqrt{\vert \kappa \vert}$,
then $s_{\kappa,\lambda}(t)=e^{-\lambda t}$
and 
\begin{equation*}
\frac{d m_{I,\rho_{ \partial M^{n}_{\kappa,\lambda}    }}    }{dt}=\frac{s^{n-1}_{\kappa,\lambda}(t)}{\int_{I}\,s^{n-1}_{\kappa,\lambda}(t)\,dt          }=(n-1)\,\lambda\,e^{-(n-1)\lambda t}.
\end{equation*}
This proves the assertion.
\end{proof}



\subsection{Proof of Theorem \ref{thm:infinite dimensional main theorem}}\label{sec:Observable inscribed radius comparisons}
One can prove the following result only by replacing the role of Theorem \ref{thm:volume comparison} with that of Theorem \ref{thm:relative volume comparison} in the proof of Lemma \ref{lem:key lemma}.
The proof is left to the reader.
\begin{lem}\label{lem:infinite dimensional key lemma}
Let $\bm$ be compact.
Let us assume $\ric^{\infty}_{f,\bm^{\perp}}\geq K$ and $H_{f,\bm} \geq \Lambda$.
Suppose additionally that
$\IR M\leq D$ for some $D>0$.
For $\eta \in (0,1)$,
let $\Omega \subset M$ be a Borel subset with $m_{M,f}(\Omega)\geq \eta$ and $d_{M}(\Omega,\bm)>0$.
Then we have
\begin{equation*}
\int^{d_{M}(\Omega,\bm)}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t} \,dt \leq (1-\eta)\,  \int^{D}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t} \,dt.
\end{equation*} 
\end{lem}

We are now in a position to prove Theorem \ref{thm:infinite dimensional main theorem}.
\begin{proof}[Proof of Theorem \ref{thm:infinite dimensional main theorem}]
Let $\bm$ be compact.
Let us assume $\ric^{\infty}_{f,\bm^{\perp}}\geq K$ and $H_{f,\bm}\geq \Lambda$.
Suppose either (1) $K>0$ and $\Lambda \in \mathbb{R}$;
or (2) $K=0$ and $\Lambda >0$.
We note again that
in this case,
$\int^{\infty}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}\,dt$ is finite.

We can assume $\eta<1$.
We prove the desired statement by estimating $\DS((M,f);\eta)$ from above.
We may assume $\DS((M,f);\eta)>0$.
Let $\Omega \subset M$ denote a Borel subset with $m_{M,f}(\Omega)\geq \eta$ and $d_{M}(\Omega,\bm)>0$.
Lemma \ref{lem:infinite dimensional key lemma} leads us to
\begin{equation*}
\eta \leq 1-\frac{\int^{d_{M}(\Omega,\bm)}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t} \,dt}{\int^{\IR M}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t} \,dt}
       \leq \mathcal{S}_{K,\Lambda}(d_{M}(\Omega,\bm)),
\end{equation*}
where $\mathcal{S}_{K,\Lambda}:[0,\infty]\to [0,1]$ is a function defined as
\begin{equation*}
\mathcal{S}_{K,\Lambda}(r):=\frac{\int^{\infty}_{r}\,  e^{-\frac{K}{2}\,t^{2}-\Lambda\,t} \,dt}{\int^{\infty}_{0}\,e^{-\frac{K}{2}\,t^{2}-\Lambda\,t}\,dt}.
\end{equation*}
It follows that $d_{M}(\Omega,\bm) \leq \mathcal{S}^{-1}_{K,\Lambda}(\eta)$;
in particular,
$\DS((M,f);\eta)\leq \mathcal{S}^{-1}_{K,\Lambda}(\eta)$.
Here,
we can check that
\begin{align}\label{eq:calculation of infinite dimensional model}
\mathcal{S}^{-1}_{K,\Lambda}(\eta)&=\begin{cases}
                                                           \DS(G_{K,\Lambda};\eta) & \text{if $K>0$ and $\Lambda \in \mathbb{R}$}, \\
                                                           \DS(E_{\Lambda};\eta)     & \text{if $K=0$ and $\Lambda>0$},
                                                           \end{cases}\\ \notag
                                                        &=\begin{cases}
                                                           \OI(G_{K,\Lambda};-\eta) & \text{if $K>0$ and $\Lambda \in \mathbb{R}$}, \\
                                                           \OI(E_{\Lambda};-\eta)     & \text{if $K=0$ and $\Lambda>0$},
                                                           \end{cases}
\end{align}
where we used Proposition \ref{prop:Kazukawa} in the second equality.
By combining Lemma \ref{lem:observable inscribed radius is smaller than Dirichlet separation distance}, $\DS((M,f);\eta)\leq \mathcal{S}^{-1}_{K,\Lambda}(\eta)$ and (\ref{eq:calculation of infinite dimensional model}),
we obtain 
\begin{align*}
&\quad \,\,\OI((M,f);-\eta)\leq \DS((M,f);\eta)\\
                                        &\leq \begin{cases}
                                                   \OI(G_{K,\Lambda};-\eta) & \text{if $K>0$ and $\Lambda \in \mathbb{R}$}, \\
                                                   \OI(E_{\Lambda};-\eta)     & \text{if $K=0$ and $\Lambda>0$}.
                                                  \end{cases}
\end{align*}
Thus,
we conclude Theorem \ref{thm:infinite dimensional main theorem}.
\end{proof}
