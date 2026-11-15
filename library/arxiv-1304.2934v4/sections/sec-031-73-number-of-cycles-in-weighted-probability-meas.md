---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-031-73-number-of-cycles-in-weighted-probability-meas
section_title: "Number of cycles in weighted probability measure"
section_number: 7.3
pages: 55-58
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.965
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:cycles}


We consider here the number of cycles of random permutations under the so-called weighted probability measure.
This example was already considered in \cite{NZ13} and we follow the presentation of this article.
\bigskip

Denote $X_{n}(\sigma)$ the number of disjoint cycles (including fixed points) of a permutation $\sigma$  in the symmetric group $\mathfrak{S}(n)$. We write $C_j(\sigma)$ for the number of cycles of length $j$ in the decomposition of $\sigma$ as a product of disjoint cycles; thus, $X_{n}(\sigma) =\sum_{j=1}^n C_j(\sigma)$ and $n = \sum_{j=1}^n j\,C_j(\sigma)$. Let $\Theta=(\theta_m)_{m\geq1}$ be given with $\theta_m\geq 0$. The generalized weighted measure is defined as the probability measure $\mathbb{P}_{\Theta} $ on the symmetric group $\mathfrak{S}(n)$:
$$\mathbb P_{\Theta}[\sigma]=\dfrac{1}{h_n\, n!}\prod_{m=1}^n (\theta_m)^{C_m(\sigma)}$$ with $h_n$ a normalization constant (or a partition function) and $h_0=1$. This model  is coming from statistical mechanics and the study of Bose quantum gases (see \cite{NZ13} for more references and details). It generalizes the classical cases of the uniform measure (corresponding to $\theta_m\equiv 1$) and the Ewens measure (corresponding to the case $\theta_m\equiv\theta>0$). It has been an open question to prove a central limit theorem for the total number of cycles $X_n$ under such measures (or more precisely under some specific regimes related to the asymptotic behavior of the $\theta_m$'s; such a central limit theorem was already known for Ewens measure). We refer to \cite{EU14} for a nice survey of this question. The difficulty comes from the fact the there is nothing such as the Feller coupling anymore, and we cannot apply the same method as in Example \ref{ex:cycle}. We now show how singularity analysis allows us to prove mod-Poisson convergence, and hence the central limit theorem, but also distributional approximations and precise large deviations.
\medskip

We consider the generating series 
$$g_\Theta(t)=\sum_{n=1}^\infty \dfrac{\theta_n}{n} \,t^n.$$ 
It is well known that 
\begin{equation}\label{eq:gf_hn}
\sum_{n=0}^\infty h_n \,t^n=\exp(g_\Theta(t)).
\end{equation}
Set $F(t,w)=\exp(w g_\Theta(t))$. Using elementary combinatorial arguments (which are detailed in \cite{NZ13}),
one can prove for each $z\in\mathbb{C}$ the following identity as formal power series:
\begin{equation}\label{eq:combtheta}
\sum_{n=0}^\infty h_n \,\mathbb E_{\Theta} [\exp(z X_n)]\,t^n=\exp(\E^z g_\Theta(t))=F(t,\E^z).
\end{equation}
Our goal is to obtain an asymptotic for $h_n$ and for the moment generating function of $X_n$. Note that in general (and unlike the case of Ewens measure), neither $h_n$ nor $\mathbb E_{\Theta} [\exp(z X_n)]$ have a closed expression.
Nevertheless, they correspond to the coefficient of $t^n$ in $F(t,1)$ (respectively $F(t,\E^z)$) and, thus, using Cauchy formula, they can be expressed as a contour integral. The idea of singularity analysis is to choose the contour in a clever way such that, asymptotically, the main part of this contour integral comes from the integral near the singularity. In this way, the integral depends asymptotically only of the type of singularity of $F(t,1)$ (resp. $F(t,\E^z)$).\bigskip


We note $r$ the radius of convergence of $g_\Theta(t)$.  We need suitable assumptions on the analyticity properties of $g$ together with assumptions on the nature of its singularity at the point $r$ on the circle of convergence. This motivates the next definition:

\begin{definition}
Let $0<r<R$ and $0<\phi<\pi/2$ be given. We then define
$$\Delta_0=\Delta_0(r,R,\phi)=\{z\in\mathbb C;\; |z|<R,z\neq r, |\arg (z-r)|>\phi\},$$
see Figure \ref{fig:domaindelta}. Assume we are further given $g(t)$, $\theta\geq0$ and $r>0$. We then say that $g(t)$ is in the class $\mathcal F(r,\theta)$ if\vspace{2mm}
\begin{enumerate}[(i)]
\item there exists $R>r$ and $0<\phi<\pi/2$ such that $g(t)$ is holomorphic in $\Delta_0(r,R,\phi)$;\vspace{2mm}
\item there exists a constant $K$ such that 
$$g(t)=\theta \log \left(\dfrac{1}{1-t/r}\right)+K+O(t-r)\;\; \text{ as } t\to r.$$
\end{enumerate}
\end{definition}

\begin{center}
\begin{figure}[ht]
\includegraphics{domaindelta.pdf}\caption{Domain $\Delta_0(r,R,\phi)$.\label{fig:domaindelta}}
\end{figure}
\end{center}

One readily notes that the generating series corresponding to the Ewens measure (\emph{i.e.} $\theta_m\equiv\theta$) is of class $\mathcal F(1,\theta)$ since in this case
$$g_\Theta(t)\equiv \theta\log\left(\dfrac{1}{1-t}\right).$$ Consequently our results will provide alternative proofs to this case as well.
The next theorem due to Hwang plays a key role in our example (we use the following notation: if $G(t)=\sum_{n=0}^\infty g_n t^n$,  we denote $[t^n][G]\equiv g_n$ the coefficient of $t^n$ in $G(t)$).
\begin{theorem}[Hwang, \cite{Hwa94}] \label{thm:hwang94}
Let $F(t,w)=\exp(w g(t))\,S(t,w)$ be given. Suppose\vspace{2mm}
\begin{enumerate}[(i)]
\item $g(t)$ is of class $\mathcal F(r,\theta)$,\vspace{2mm}
\item $S(t,w)$ is holomorphic in a domain containing $\{(t,w)\in\mathbb C^2;\;\; |t|\leq r, |w|\leq \hat r\}$, where $\hat r>0$ is some positive number.\vspace{2mm}
\end{enumerate}
Then 
$$[t^n][F(t,w)]=\dfrac{\E^{Kw}n^{w\theta-1}}{r^n}\left(\dfrac{S(r,w)}{\Gamma(\theta w)}+O\!\left(\dfrac{1}{n}\right)\right)$$
uniformly for $|w|\leq\hat r$ and with the same $K$ as in the definition above.
\end{theorem}
The idea of the proof consists in taking a suitable Hankel contour and to estimate the integral over each piece.  There exist several other versions of this theorem where one can replace $\log (1-t/r)$ by other functions and we refer the reader to the monograph \cite{FSe09}, chapter VI.5. As an application of Theorem \ref{thm:hwang94}, we obtain an asymptotic for $h_n$.

\begin{lemma}\label{lem:hn}
Let $\theta>0$ and assume that $g_\Theta(t)$ is of class $\mathcal F(r,\theta)$. We then have
$$h_n=\dfrac{\E^{K}n^{\theta-1}}{r^n\,\Gamma(\theta)}\left(1+O\!\left(\dfrac{1}{n}\right)\right).$$
\end{lemma}

\begin{proof}
We have already noted that $\sum_{n=1}^\infty h_n t^n=\exp(g_\Theta(t))$. We can apply Theorem \ref{thm:hwang94} with $g(t)=g_\Theta(t)$, $w=1$ and $S(t,w)=1$.
\end{proof}
\bigskip


Using identity \eqref{eq:combtheta} and Theorem \ref{thm:hwang94}, we can also obtain an asymptotic for the Laplace transform $\esper_{\Theta} [\exp(w X_n)]$:

\begin{theorem}[Nikeghbali-Zeindler, \cite{NZ13}]
If $g_\Theta(t)$ is of class $\mathcal F(r,\theta)$, then
$$ \esper_{\Theta} [\exp(z X_n)]=n^{\theta(\E^z-1)} \E^{K(\E^z-1)}\left(\dfrac{\Gamma(\theta)}{\Gamma(\theta \E^z)}+O\!\left(\dfrac{1}{n}\right)\right).$$
Consequently, the sequence $(X_n)_{n \in \N}$ converges in the mod-Poisson sense, with parameters $t_n=K+\theta \log n$ and limiting function $\psi(z)=\frac{\Gamma(\theta)}{\Gamma(\theta \E^z)}$. The convergence takes place of the whole complex plane with speed $O(1/n)$.
\label{thm:modpoissonNZ}
\end{theorem}

\begin{proof}
An application of Theorem \ref{thm:hwang94} yields
$$[t^n][\exp(\E^z g_\Theta(t))]=\dfrac{\E^{K\E^z}n^{\E^z\theta-1}}{r^n}\left(\dfrac{1}{\Gamma(\theta \E^z)}+O\!\left(\dfrac{1}{n}\right)\right),$$
with $O(\cdot)$ uniform for bounded $z\in\C$. Now a combination of identity (\ref{eq:combtheta}) and Lemma \ref{lem:hn} gives the desired result.
\end{proof}
\bigskip

The above theorem not only implies the central limit theorem, but also Poisson approximations and precise large deviations. We only state here the precise large deviation result which extends earlier work of Hwang in the case $\theta=1$ as a consequence of Theorem \ref{thm:mainlattice} and refer to \cite{NZ13} for the distributional approximations results.

\begin{proposition}[Nikeghbali-Zeindler, \cite{NZ13}]
Let $Y_n=X_n-1$ and let $x\in\mathbb R$ such that $t_nx\in\mathbb N$ with $t_n=K+\theta \log n$. We note $k=t_n x$. Then
$$\mathbb P[Y_n=x t_n]=\E^{-t_n}\dfrac{(t_n)^k}{k!}\left(\dfrac{\Gamma(\theta)}{x\,\Gamma(\theta x)}+O\!\left(\dfrac{1}{ t_n}\right)\right).$$
\end{proposition}
\noindent In fact, an application of Theorem \ref{thm:mainlattice} would immediately yield an arbitrary long expansion for $\mathbb P[Y_n=x t_n]$ and also for $\mathbb P[Y_n\geq x t_n]$, since the speed of convergence is fast enough.
\bigskip

\begin{remark}
    Equations \eqref{eq:gf_hn} and \eqref{eq:combtheta} fit naturally in the framework of 
    {\em labelled combinatorial classes}~\cite[Chapter II]{FSe09}:
    a permutation is a {\em set} of cycles and the weighted exponential generating series of cycles is $g_{\Theta}(t)$.
    Using this framework, one could give a more general statement with the same proof.
    Let $\mathcal{A}$ be a (weighted) labelled combinatorial class and
    consider the class $\mathcal{B}=\Set(\mathcal{A})$.
    We denote $X_n$ the number of components in a random element of size $n$ of $\mathcal{B}$
    (the probability of taking an element of $\mathcal{B}$ being proportional to its weight).
    Assume that the generating series of $\mathcal{A}$ is in the class $\mathcal{F}(r,\theta)$.
    Then $(X_n)_{n \in \N}$ converges in the mod-Poisson sense as in Theorem \ref{thm:modpoissonNZ}.
    We refer to \cite[Section 4.1]{Hwa96} for a similar discussion.\medskip

   However, the hypothesis that the generating series of $\mathcal{A}$ is in the class $\mathcal{F}(r,\theta)$
   is mainly natural in the case of cycles and permutations, which explains why we
   focused on this example here.
\end{remark}

\begin{remark}
   Singularity analysis is closely related to the Selberg-Delange method 
   used in previous Section.
   In both cases we do not have a closed expression for the Laplace transform of our variable,
   but for an appropriate sum of them --- Dirichlet series for arithmetic functions
   and exponential generating functions for cycles in weighted permutations.
    From Perron's or Cauchy's formula, 
    we get an integral formula for the Laplace transform.
    Then choosing an appropriate integral contour allows to find the asymptotics.
    It is quite striking that these closely related methods both
    yield mod-Poisson convergence. However, we are not aware of a way to bring both under one roof.
\end{remark}
\bigskip
