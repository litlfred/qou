---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-004-3-equilibrium-measures
section_title: "Equilibrium measures"
section_number: 3
pages: 10-16
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.991
---
\label{section: eq}

It will be convenient to introduce a new parameter $x \in \mathbb{R}^{+} \cup \{+\infty\}$ defined by
\begin{equation}\label{sx}
s = e^{-xn},
\end{equation}
such that $f$ can be written as $f(e^{i\theta}) = e^{W(e^{i\theta})}e^{-nV(e^{i\theta})}$, where 
\begin{equation}\label{V}
V(e^{i\theta}) = \begin{cases}
0, & \mbox{ for } e^{i\theta} \in \gamma, \\
x, & \mbox{ for } e^{i\theta} \in S_{1} \setminus \gamma.
\end{cases}
\end{equation}
An important ingredient for the large $n$ analysis of the orthogonal polynomials and the RH problem for $Y$ is the following minimization problem:
find the measure $\mu=\mu^{(x)}$ which minimizes 
\begin{equation} \label{inf_prob}
 \iint \log |z-s|^{-1} d\mu(z)d\mu(s) + \int V(z)d\mu(z)
\end{equation}
among all Borel probability measures on the unit circle $S_{1}$.




This measure, which is unique and absolutely continuous with respect to the Lebesgue measure, is called the equilibrium measure, is denoted $d\mu^{(x)}=u^{(x)}(e^{i\theta})d\theta$, and its support is denoted $J^{(x)}$.
The equilibrium measure $\mu=\mu^{(x)}$ and its support $J=J^{(x)}$ are uniquely determined by the following Euler-Lagrange variational conditions \cite{BDJ, SaTo}:
there exists a real constant $\ell=\ell^{(x)}$ such that
\begin{align}
&\label{EL_1}
2 \int_{-\pi}^{\pi} \log | z-e^{i\theta} | d\mu(e^{i\theta}) - V(z) + \ell = 0, &\mbox{ for } z \in J,\\&\label{EL_2}
2 \int_{-\pi}^{\pi} \log | z-e^{i\theta} | d\mu(e^{i\theta}) - V(z) + \ell \leq 0, &\mbox{ for } z \in S_{1}\setminus J.
\end{align}
The support and density of the equilibrium measure can be computed explicitly.

\begin{proposition}\label{thm200}
\begin{itemize}
\item[(a)] For $x = +\infty$, the support of the equilibrium measure and its density are given by
\begin{equation}\label{uinfty}
J=J^{(\infty)}=\gamma,\qquad u(e^{i\theta})=u^{(\infty)}(e^{i\theta}) = \frac{1}{2\pi} \sqrt{\frac{\cos \theta + 1}{\cos \theta - \cos \theta_{0}}}.
\end{equation}
The constant $\ell=\ell^{(\infty)}$ in the variational conditions (\ref{EL_1})-(\ref{EL_2}) is given by
\begin{equation}\label{linfy}
\ell^{(\infty)} = - 2 \ln \sin \frac{\theta_{0}}{2},
\end{equation}
and the variational inequality (\ref{EL_2}) is strict for $z\in S_1\setminus{\gamma}$.
\item[(b)]Let $x_c$ be given by (\ref{xcintro}). For $x \geq x_{c}$, we have the same result as for $x=+\infty$:
\begin{equation}\label{ux1}
J = \gamma \hspace{0.1cm},\qquad u(e^{i\theta}) = u^{(\infty)}(e^{i\theta}),\qquad \ell = \ell^{(\infty)}.
\end{equation}
Moreover, the variational inequality (\ref{EL_2}) is strict for $z\in S_1\setminus{\gamma}$ if $x\neq x_c$; if $x=x_c$, it is strict for $z\in S_1\setminus\left(\gamma \cup\{-1\}\right)$, and there is equality for $z=-1$.
\item[(c)] For $0 < x < x_{c}$, the support of $\mu$ consists of two disjoint arcs: we have
\begin{equation}\label{ux2}
J = \{ e^{i\theta} : \theta \in [-\theta_{0},\theta_{0}] \cup [\pi-\theta_{1},\pi + \theta_{1}] \} ,
\end{equation}
where $\theta_1=\theta_1(x)\in (0,\pi-\theta_0)$ is the unique solution of 
\begin{equation}\label{bijection_theta1_x}
2\int_{[-\theta_{0},\theta_{0}] \cup [\pi-\theta_{1},\pi + \theta_{1}]} \log \left| \frac{1+e^{i\theta}}{1-e^{i\theta}} \right| u(e^{i\theta}) d\theta = x,
\end{equation}
and the density is given by 
\begin{equation}
u(e^{i\theta}) = \frac{1}{2\pi} \sqrt{\frac{\cos \theta + \cos \theta_{1}}{\cos \theta - \cos \theta_{0}}}.
\end{equation}
The constant $\ell$ is given by
\begin{equation}\label{lx}
\ell = - \int_{0}^{1} \frac{1}{s} \left( 1 - \sqrt{\frac{s^2 + 2\cos (\theta_{1}) s +1}{s^2 - 2\cos (\theta_{0}) s +1}} \right) ds,
\end{equation}
and the variational inequality (\ref{EL_2}) is strict for $z\in S_1\setminus{J}$.
\end{itemize}
\end{proposition}
\begin{remark}
Although part (c) of the proposition is not needed for the proof of Theorem \ref{theorem: extensionWidom}, we present it here for completeness and to support the heuristic arguments in Section \ref{section: elliptic}, where we will discuss asymptotics for $D_n$ if $x< x_c$.
\end{remark}
\begin{proof}
Note first that the equation (\ref{bijection_theta1_x}) has indeed a unique solution $\theta_1$ for $x<x_c$, since the function
\begin{equation*}
\theta_{1} \mapsto 2\int_{[-\theta_{0},\theta_{0}] \cup [\pi-\theta_{1},\pi + \theta_{1}]} \log \left| \frac{1+e^{i\theta}}{1-e^{i\theta}} \right| u(e^{i\theta}) d\theta
\end{equation*} decreases as a function of $\theta_{1} \in (0,\pi-\theta_{0})$, and is bijective from $(0,\pi-\theta_{0})$ to $(0,x_c)$. 

\medskip

The equilibrium measure $\mu$ is uniquely characterized by the conditions \eqref{EL_1}-\eqref{EL_2}, which means that it is sufficient for us to show that the measure $\mu$ defined in cases (a), (b), and (c) satisfy these variational conditions. 
To do so, consider the function
\begin{equation}
f(z) =2\int \log | z-e^{i\theta}| d\mu^{(x)}(e^{i\theta}).
\end{equation}
If we define $\theta_1>0$ as the unique solution of (\ref{bijection_theta1_x}) if $x<x_c$, and if we let $\theta_1=0$ for $x\geq x_c$, we have
\begin{equation}
f(e^{i\alpha})=\frac{1}{\pi}\int_{[-\theta_0,\theta_0]\cup[\pi-\theta_1,\pi+\theta_1]} \log | e^{i\alpha}-e^{i\theta}|\sqrt{\frac{\cos \theta + \cos \theta_{1}}{\cos \theta - \cos \theta_{0}}}d\theta.
\end{equation}
The derivative $\frac{d}{d\alpha} f(e^{i\alpha})$ can be written as a contour integral 
\begin{equation}
\frac{d}{d\alpha} f(e^{i\alpha})=-\frac{1}{2\pi i}\int_\Sigma \frac{1}{\xi}\frac{\xi+e^{i\alpha}}{\xi-e^{i\alpha}}\left(\frac{(\xi-z_1)(\xi-\overline{z_1})}{(\xi-z_0)(\xi-\overline{z_0})}\right)^{1/2}d\xi, \qquad z_{1} = e^{i\theta_{1}},
\end{equation}
where the square root is analytic off $J$ and tends to $1$ as $\xi\to\infty$, and
where the contour $\Sigma$ consists of one (if $x\geq x_c$) or two (if $x<x_c$) counterclockwise oriented circles around the arc(s) of $J$. If $e^{i\alpha}\in S_1\setminus J$, the contour has to be chosen sufficiently small such that $e^{i\alpha}$ lies in the exterior of $\Sigma$.

If $e^{i\alpha} \in J$, a residue calculation shows that $\frac{d}{d\alpha} f(e^{i\alpha})=0$.
If $e^{i\alpha} \in S_{1}\setminus J$ on the other hand, we have
\begin{equation} \label{derivative_of_EL}
\frac{d}{d\alpha} f(e^{i\alpha})  
 = \begin{cases}
 \sqrt{\frac{\cos \theta_{1} + \cos \alpha}{ \cos \theta_{0} - \cos \alpha}}, & \mbox{ if } \theta_{0} < \alpha < \pi-\theta_{1}, \\[0.4cm]
 -\sqrt{\frac{\cos \theta_{1} + \cos \alpha}{ \cos \theta_{0} - \cos \alpha}}, & \mbox{ if } \pi+\theta_{1} < \alpha < 2\pi-\theta_{0}.
\end{cases} 
\end{equation}
It follows that $f(e^{i \alpha})$ is constant on $[-\theta_0,\theta_0]\cup[\pi-\theta_1,\pi+\theta_1]$, and that it achieves its maximum on $[\pi-\theta_1,\pi+\theta_1]$ (i.e.\ at $\pi$ if $x\geq x_c$). 
We have
\begin{align}
&\label{f1}f(e^{i\alpha})=f(1),&\mbox{ for $-\theta_0\leq \alpha\leq \theta_0$},\\
&f(e^{i\alpha})=f(-1),&\mbox{ for $\pi-\theta_1\leq \alpha\leq \pi+\theta_1$},\\
&\label{f3}f(e^{i\alpha})< f(-1),&\mbox{ for $\alpha\notin [\pi-\theta_1,\pi+\theta_1]$}.
\end{align}
If we show that 
\begin{align}
&\label{toshowf1}f(1)=-\ell, \ f(-1)<f(1)+x, & \mbox{ for $x>x_c$},\\
&\label{toshowf2}f(1)=-\ell, \ f(-1)=f(1)+x, & \mbox{ for $x\leq x_c$},
\end{align}
then (\ref{f1})-(\ref{f3}) imply the Euler-Lagrange conditions (\ref{EL_1})-(\ref{EL_2}).



For the case $x\geq x_c$, using  (\ref{derivative_of_EL}), we obtain after a straightforward calculation, \begin{equation*}
f(-1) - f(1) =f(e^{i\pi})-f(e^{i\theta_0})= \int_{\theta_0}^{\pi} \sqrt{\frac{1+\cos \theta}{\cos \theta_{0} - \cos \theta}}d\theta= -2 \ln \tan \frac{\theta_{0}}{4} = x_c \leq x,
\end{equation*}
which proves the inequality in (\ref{toshowf1}), and the fact that there is equality at $-1$ if $x=x_c$.
Moreover, using an other residue calculation, we get
\begin{equation*}
f(1) = \int_{0}^{1} f^{\prime}(s) ds = \int_{0}^{1} \frac{1}{s}\left( 1 - \frac{1+s}{\sqrt{s^{2}-2\cos (\theta_{0})s + 1}} \right)ds = 2\ln \sin \frac{\theta_{0}}{2} = -\ell^{(\infty)}.
\end{equation*}
This proves the equality in (\ref{toshowf1}).
For $0 < x < x_{c}$, by
(\ref{derivative_of_EL}), 
\begin{equation*}
f(-1) - f(1) =f(e^{i(\pi-\theta_1)})-f(e^{i\theta_0})= \int_{\theta_0}^{\pi-\theta_1} \sqrt{\frac{\cos\theta_1+\cos \theta}{\cos \theta_{0} - \cos \theta}}d\theta = x,
\end{equation*}
by definition of $f$ and $\theta_{1}$,
and 
\begin{equation*}
f(1)= \int_{0}^{1} \frac{1}{s}\left( 1 - \sqrt{\frac{s^2 + 2\cos (\theta_{1}) s +1}{s^2 - 2\cos (\theta_{0}) s +1}} \right) ds = -\ell.
\end{equation*}
This completes the proof.
\end{proof}







\section{Riemann-Hilbert analysis for $x\geq x_c$}\label{section: RH}
We will now perform an asymptotic analysis of the RH problem for $Y$ as $n\to\infty$ with $x\geq x_c$. Our analysis uses the Deift/Zhou steepest descent method \cite{Deift, DKMVZ2, DKMVZ1} and shows many similarities with the analysis done in \cite{Krasovsky} for $s=0$ (or $x=+\infty$). An important difference is that we need to modify the Bessel parametrices around the points $z_0, \overline{z_0}$, see Section \ref{section: Bessel} below.




\subsection{First transformation $Y \to T$}
We define $g$ by
\begin{equation}\label{g}
g(z)=\int_{-\theta_{0}}^{\theta_{0}}\log(z-e^{i\theta})d\mu^{(\infty)}(e^{i\theta}).
\end{equation}
Below we write $\mu=\mu^{(\infty)}$, $u=u^{(\infty)}$, and $\ell=\ell^{(\infty)}$.
We have that $e^g$ is analytic for $z\in\mathbb C\setminus\gamma$, and by the Euler-Lagrange variational conditions (\ref{EL_1})-(\ref{EL_2}), we also have 
\begin{align}
&\label{g1}g_{+}(z) + g_{-}(z) - \log(z) -i\pi + \ell = 0 ,&&\mbox{ for } z\in \gamma\setminus\{z_{0},\overline{z_{0}}\},\\
&\label{g2}2g(z)  - \log(z) -i\pi+\ell<0,&&\mbox{ for }z\in S_{1}\setminus \gamma,\\
&\label{g3}g_{+}^{\prime}(z) - g_{-}^{\prime}(z)=-\frac{2\pi}{z}u(z),&&\mbox{ for }z\in \gamma\setminus\{z_{0},\overline{z_{0}}\}.
\end{align}
Define
\begin{equation}\label{def T}
T(z) = e^{\frac{n\pi i}{2}\sigma_{3}} e^{\frac{n\ell}{2}\sigma_{3}} Y(z) e^{-ng(z)\sigma_{3}} e^{-\frac{n\ell}{2}\sigma_{3}}e^{-\frac{n\pi i}{2}\sigma_{3}}.
\end{equation}
Then it is straightforward to check that $T$ satisfies the following conditions.


\subsubsection{RH problem for $T$}
\begin{itemize}
\item[(a)] $T : \mathbb{C}\setminus S_{1} \to \mathbb{C}^{2\times 2}$ is analytic.
\item[(b)] $T$ satisfies the jump relation
\begin{equation}
T_{+}(z) = T_{-}(z) J_{T}(z),\qquad \mbox{ on } S_{1}\setminus \left\{z_{0},\overline{z_{0}}\right\},
\end{equation}
with
\begin{equation*}
J_{T}(z) = \begin{pmatrix}
\displaystyle e^{-n(g_{+}(z)-g_{-}(z))} & \displaystyle (-1)^{n}z^{-n}e^{-nV(z)}e^{n\ell}e^{n(g_{+}(z)+g_{-}(z))}e^{W(z)} \\
\displaystyle 0 & \displaystyle e^{n(g_{+}(z)-g_{-}(z))}
\end{pmatrix}.
\end{equation*}
\item[(c)] $T(z) = I + \bigO(z^{-1})$ as $z \to \infty$.
\item[(d)] As $z\to z_0=e^{i\theta_0}$ or $z\to\overline {z_0}=e^{-i\theta_0}$, we have
\begin{equation*}
\begin{array}{l l}
T(z) = \begin{pmatrix}
\bigO(1) & \bigO(\ln |z-z_0|) \\ \bigO(1) & \bigO(\ln |z-z_0|)
\end{pmatrix},  &  \mbox{ as } z \to z_0, \\ [0.8cm]
T(z) = \begin{pmatrix}
\bigO(1) & \bigO(\ln |z-\overline{z_0}|) \\ \bigO(1) & \bigO(\ln |z-\overline{z_0}|)
\end{pmatrix}, &  \mbox{ as } z \to \overline{z_0}.
\end{array}
\end{equation*}
\end{itemize}

We define 
\begin{equation}\label{def phi}
\phi(z)=2g(z)-\log z -i\pi+\ell, 
\end{equation}
so that $e^\phi$ is analytic in a neighborhood of $\gamma$ with the exception of $\gamma$ itself.
For $z\in\gamma\setminus\{z_{0},\overline{z_{0}}\}$, we have
\begin{eqnarray}\label{phi g}
\phi_+(z)&=&(g_+(z)+g_-(z)-\log z-i\pi+\ell)+(g_+(z)-g_-(z))\\
&=&g_+(z)-g_-(z),
\end{eqnarray}
by (\ref{g1}). But $g_+(z_0)=g_-(z_0)$, and integrating (\ref{g3}) between $z_0$ and $z$, and then substituting it into (\ref{phi g}), we obtain
\begin{equation}
\phi_+(z)=-2\pi\int_{z_0}^z\frac{u(\xi)}{\xi}d\xi.
\end{equation}
Analytically continuing the left and right hand side, we obtain
\begin{equation}\label{phi int}
\phi(z)=\int_{z_0}^{z} \frac{\xi+1}{\left((\xi-z_{0})(\xi-\overline{z_{0}})\right)^{1/2}} \frac{d\xi}{\xi},
\end{equation}
where the branch cut of the square root is chosen on $\gamma$. It is now convenient to express $J_T$ in terms of $\phi$:
\begin{equation*}
J_{T}(z) = \begin{cases} \begin{pmatrix}
e^{-n\phi_+(z)} & e^{W(z)} \\
0 & e^{-n\phi_-(z)}
\end{pmatrix}, & z \in \gamma\setminus\{z_{0},\overline{z_{0}}\}, \\
\begin{pmatrix}
1 & e^{-nx}e^{n\phi(z)}e^{W(z)} \\
0 & 1
\end{pmatrix}, & z \in S_{1} \setminus \gamma.
\end{cases}
\end{equation*}



\subsection{Second transformation $T \to S$}

We can factorize $J_{T}$ on $\gamma$ as follows:
\begin{multline}
\begin{pmatrix}
e^{-n\phi_+(z)} & e^{W(z)} \\
0 & e^{-n\phi_-(z)}
\end{pmatrix} = \begin{pmatrix}
1 & 0 \\ e^{-n\phi_-(z)}e^{-W(z)} & 1
\end{pmatrix}\\
\times\ \begin{pmatrix}
0 & e^{W(z)} \\ -e^{-W(z)} & 0
\end{pmatrix}\begin{pmatrix}
1 & 0 \\ e^{-n\phi_+(z)}e^{-W(z)} & 1
\end{pmatrix}.
\end{multline}
Using this factorization, we can split the jump on $\gamma$ into three different jumps on a lens-shaped oriented contour, see Figure \ref{fig_S}. It is important that the jump contour lies in the region where $W$ is analytic.
Denote by $\gamma_{+}$ and $\gamma_{-}$ the lenses around $\gamma$ on the $|z|<1$ side and the $|z|>1$ side respectively. Define
\begin{equation}\label{def S}
S(z) = \left\{ \begin{array}{l l}

T(z) \begin{pmatrix}
1 & 0 \\ -e^{-n\phi(z)}e^{-W(z)} & 1
\end{pmatrix}, &
|z|<1, z \mbox{ inside the lenses around }\gamma, \\[0.6cm]
T(z) \begin{pmatrix}
1 & 0 \\ e^{-n\phi(z)}e^{-W(z)} & 1
\end{pmatrix}, &
|z|>1, z \mbox{ inside the lenses around }\gamma, \\[0.6cm]

T(z),  &   z \mbox{ outside the lenses.}                 \\

\end{array} \right.
\end{equation}
Then $S$ solves the following RH problem.

\subsubsection{RH problem for $S$}









\begin{figure}[t]
    \begin{center}
    \setlength{\unitlength}{1truemm}
    \begin{picture}(100,55)(-5,10)
        \cCircle(50,40){25}[f]
        \put(65,60){\thicklines\circle*{1.2}}
        \put(65,19.8){\thicklines\circle*{1.2}}
	    \qbezier(65,60)(73,40)(65,19.8)
	    \qbezier(65,60)(100,40)(65,19.8)
        \put(65,61){$z_0$}
        \put(72,36){$\gamma$}
        \put(65,36){$\gamma_+$}
        \put(78.5,36){$\gamma_-$}
        \put(21,36){$\gamma^c$}      
        \put(65,17){$\overline{z_0}$}
        \put(75,41){\thicklines\vector(0,1){.0001}}
        \put(69,41){\thicklines\vector(0,1){.0001}}
        \put(82.5,41){\thicklines\vector(0,1){.0001}}
        \put(25,39){\thicklines\vector(0,-1){.0001}}
    \end{picture}
    \caption{The jump contour for $S$.}
    \label{fig_S}
\end{center}
\end{figure}

\begin{itemize}
\item[(a)] $S : \mathbb{C}\setminus (S_{1}\cup \gamma_{-} \cup \gamma_{+}) \to \mathbb{C}^{2\times 2}$ is analytic.
\item[(b)] $S$ satisfies the jump relations
\begin{equation}\label{jump S}
S_{+}(z) = S_{-}(z)J_S(z),\qquad \mbox{ for $z\in S_1\cup\gamma_-\cup\gamma_+$},
\end{equation}
where $S_+$ ($S_-$) denotes the boundary value from the left (right) of the contour, and where
\begin{equation}\label{JS}
J_S(z) = \begin{cases}\begin{pmatrix}
1 & e^{-nx}e^{n\phi(z)}e^{W(z)} \\ 0 & 1
\end{pmatrix}, & \mbox{ for } z \in S_{1}\setminus \gamma, \\
\begin{pmatrix}
0 & e^{-W(z)} \\ -e^{-W(z)} & 0
\end{pmatrix},  & \mbox{ for } z \in \gamma\setminus\{z_{0},\overline{z_{0}}\}, \\
\begin{pmatrix}
1 & 0 \\ e^{-n\phi(z)}e^{-W(z)} & 1
\end{pmatrix},  & \mbox{ for } z \in \gamma_{+}\cup\gamma_-.
\end{cases}
\end{equation} 
\item[(c)] $S(z) = I + \bigO(z^{-1})$ as $z \to \infty$.
\item[(d)] As $z\to z_0=e^{i\theta_0}$ or $z\to\overline {z_0}=e^{-i\theta_0}$, we have
\begin{equation}
S(z)=\bigO(\ln|z-z_0|),\qquad S(z)=\bigO(\ln|z-\overline{z_0}|).
\end{equation}










\end{itemize}



By (\ref{def phi}) and (\ref{g2}), we observe that the jump matrices for $S$ converge to the identity matrix on $S_{1}\setminus \gamma$ as $n\to\infty$, except at $-1$ if $x=x_c$.
On $\gamma_{+} \cup \gamma_{-}$, one shows that $\Re\phi(z)>0$ and consequently the jump matrices for $S$ also converge to the identity matrix on $\gamma_{+} \cup \gamma_{-}$.
The convergence of the jump matrices is point-wise in $z$ and breaks down as $z$ approaches $z_0, \overline{z_0}$, and also as $z$ approaches $-1$ if $x=x_c$. Therefore, we will need to construct approximations to $S$ for large $n$ in different regions of the complex plane: local parametrices will be constructed in small disks $D(z_0,r), D(\overline{z_0},r), D(-1,r)$ surrounding $z_0, \overline{z_0}, -1$, and a global parametrix will be constructed in $\mathbb C\setminus(\overline{D(z_0,r)\cup D(\overline{z_{0}},r)\cup D(-1,r)})$.
