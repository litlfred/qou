---
doc_id: arxiv-2604.16077v1
doc_title: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement"
section_id: sec-012-31-functions-in-the-qhi-state-sums
section_title: "Functions in the QHI state sums"
section_number: 3.1
pages: 20-31
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.969
doc_brief: "Volume Conjecture and quantum hyperbolic invariants: the figure eight knot complement — We compute the real part of the semi-classical limit of the sequence of quantum hyperbolic invariants (QHI) of"
---
\label{FUNCNOT}  Consider the rational functions $\omega_N(.,.|n)$, $n\in \mn$, defined on the curve $\mathcal{F}_N :=\{(x,y)\in \mc^2\vert \ x^N+y^N=1\}$ by
\begin{equation}\label{functomegadef}
\omega_N(x,y|0)=1\ ,\ \omega_N(x,y|n)=\prod_{j=1}^n \frac{y}{1-x\zeta^{j}}\ {\rm if} \ n\geq 1.
\end{equation}
Since $(1-x)(1-x\zeta)\ldots (1-x\zeta^{N-1}) = 1-x^N=y^N$, we have
$$\omega_N(x,y|N+n) = \omega_N(x,y|n).$$
These functions are closely related to Faddeev's \cite{Fad,FKV} {\it non compact quantum dilogarithm} $\Phi_\rmb$, and therefore to the classical Euler dilogarithm ${\rm Li_2}$. The function $\Phi_\rmb$ is defined as follows; it can be regarded as a kind of double Barnes' sine function (\cite{GR}). Let $\rmb\in \mc$ be such that $\mathfrak{R}(\rmb)\ne 0$. Define
$$\sqrt{\hbar} := \frac{1}{\rmb+\rmb^{-1}}.$$
Denote by $\mr +i0$ the real axis directed from $-\infty$ to $\infty$, slightly deformed near $0$ so as to pass above $0$. Then $\Phi_\rmb$ is the holomorphic function defined in the strip $\vert \mathfrak{I}(z)\vert < \vert \mathfrak{I}(i/2\sqrt{\hbar})\vert$ by the integral formula 
\begin{equation}\label{intrepS}
\Phi_{{\rmb}}(z) =\exp\left(\frac{1}{4} \int_{\mr +i0} \frac{e^{-2izw}\ dw}{w\sinh(\rmb w)\sinh(\rmb^{-1} w)}\right).
\end{equation}
Denote by $\Log(\Phi_{{\rmb}}(z))$ the integral on the RHS. It satisfies the functional equation
\begin{equation}\label{eqfuncphibLog}
\Log\left(\Phi_{{\rmb}}\left(z-i\frac{\rmb^{\pm 1}}{2}\right)\right) = \Log\left(\Phi_{{\rmb}}\left(z+i\frac{\rmb^{\pm 1}}{2}\right)\right) + \Log(1+e^{2\pi\rmb^{\pm 1}z}) .
\end{equation}
Therefore $\Phi_{{\rmb}}$ can be extended to a meromorphic function of $z\in \mc$, satisfying the functional equation
\begin{equation}\label{eqfuncphib}
\Phi_{{\rmb}}\left(z-i\frac{\rmb^{\pm 1}}{2}\right) = (1+e^{2\pi\rmb^{\pm 1}z}) \Phi_{{\rmb}}\left(z+i\frac{\rmb^{\pm 1}}{2}\right).
\end{equation}
The poles and zeros of $\Phi_\rmb$ are the points $\textstyle z=\frac{i}{2\sqrt{\hbar}} +mi\rmb+ni\rmb^{-1}$ and $\textstyle z=-(\frac{i}{2\sqrt{\hbar}}+mi\rmb+ni\rmb^{-1})$ respectively, where $m,n\in \mn$.

We will use the following version of $\Phi_\rmb$. Let $\textstyle \rmb = \frac{1}{\sqrt{N}}$, and set 
\begin{equation}\label{defShat}
\textstyle \hat{S}_N(z) := \Phi_{\frac{1}{\sqrt{N}}}\left(\frac{\sqrt{N}}{2\pi}\left(z-i(\pi-\frac{\pi}{N})\right)\right).
\end{equation}
Denote by $\Log(\hat{S}_N(z))$ the integral obtained from the one in \eqref{intrepS} by the change of variable in \eqref{defShat}. Then $\Log(\hat{S}_N(z))$ is a holomorphic function of $z$ in the strip $\textstyle -\frac{2\pi}{N}<\mathfrak{I}(z) < 2\pi$, and it satisfies the functional equation
\begin{equation}\label{eqfunchatSLog} 
\textstyle \Log(\hat{S}_N(z)) = \Log(\hat{S}_N(z+\frac{2i\pi}{N})) + \Log(1-e^{z+\frac{2i\pi}{N}}).
\end{equation}
\noindent Therefore it can be extended to an analytic function on $\mc$ with cuts $\textstyle [0,+\infty[+i(2\pi + \frac{2\pi p}{N})$, $p\in\mn$, and $\textstyle [0,+\infty[-i(l+1)\frac{2\pi}{N}$, $l\in\mn$. All this implies that $\hat{S}_N$ is holomorphic and without zeros in the strip $\textstyle -\frac{2\pi}{N}<\mathfrak{I}(z) < 2\pi$, it satisfies the functional equation
\begin{equation}\label{eqfunchatS} 
\textstyle\hat S_{N}(z) = \hat S_{N}(z+\frac{2i\pi}{N})(1-e^{z+\frac{2i\pi}{N}}),
\end{equation}
and it can be extended to a meromorphic function on $\mc$ with sets of poles and simple poles
\begin{equation}\label{PP1}
\textstyle P=\{2i\pi+i\frac{2p\pi}{N},\ p\in \mn\}\ ,\ P_1=\{2i\pi+i\frac{2p\pi}{N},\ p\in \{0,\ldots,N-1\}\}
\end{equation}
respectively, and zeroes
$$\textstyle Z=\{-(l+1)i\frac{2\pi}{N},\ l\in \mn\}.$$
Moreover the functional equation \eqref{eqfunchatS} yields
\begin{equation}\label{relomS0}
\omega_N(e^{z},y| n) = \prod_{j=1}^{n} \frac{y}{1-e^{z}\zeta^j} = y^n\ \frac{\hat S_N(z+2n i\pi/N)}{\hat S_N(z)}
\end{equation}
for every $y,z\in \mc$ such that $y^N = 1-e^{Nz}$. 
The function $\Phi_\rmb$ has a number of remarkable properties, see \cite{FKV,AK}. In particular, its ''semi-classical limit'', as $\rmb \ra 0^+$, recovers the Euler dilogarithm function (see \cite{Z} and Lemma \ref{estimatehatS} below),
\begin{equation}\label{Li2def}{\rm Li_2}(x) = -\int_0^x\frac{\Log(1-t)}{t}dt,\quad x\in \mc\setminus [1,+\infty[.
\end{equation}
Basically, the connection between the two functions can be guessed by comparing the formula \eqref{intrepS} with the following integral representation. It is well-known, but we recall a proof for it is short and illuminating.
\begin{lem}\label{Li2intrep} For all $y\in \mr+i(-\pi,\pi)$ we have $\frac{1}{2\pi i}{\rm Li_2}(-e^y) = \frac{1}{4} \int_{\mr +i0} \frac{e^{-i\frac{yv}{\pi}}\ dv}{v^2\sinh(v)}.$
\end{lem}
\proof The integral above is a holomorphic function of $y$. Taking the derivative twice we get
$$\partial_{y}^2 \left( \int_{\mr +i0} \frac{e^{-i\frac{yv}{\pi}}\ dv}{v^2\sinh(v)}\right)  = -\frac{1}{\pi^2} \int_{\mr +i0} \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)} = -\frac{1}{\pi^2 (1+e^{y})}\ \biggl( \int_{\mr +i0} - \int_{\mr +i0+\pi i} \biggr)\ \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)}$$
where, using a simple change of variable, we note that
$$\int_{\mr +i0+\pi i} \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)} = -e^{y}\ \int_{\mr +i0} \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)}.$$
Now, let $R>0$ and consider the contour $\Gamma_R$ formed by the concatenation of the oriented segments $[-R,R]+i0$, $R+i\pi[0,1]$, $-([-R,R]+i0)+i\pi$ and $-R-i\pi [0,1]$. We have
$$\lim_{R \rightarrow +\infty} \int_{\pm R+i\pi[0,1]} \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)} = \lim_{R \rightarrow +\infty} \int_0^1 \frac{e^{-i\frac{y}{\pi}(\pm R + \pi it)}}{\sinh(\pm R + \pi it)} \ dt = 0$$
and therefore
\begin{align*}\biggl( \int_{\mr +i0} - \int_{\mr +i0+\pi i} \biggr)\ \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)} & = \lim_{R \rightarrow +\infty} \biggl( \int_{\Gamma_R} - \int_{R+i\pi[0,1]} - \int_{-R-i\pi[0,1]}\biggr) \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)} \\ & = \lim_{R \rightarrow +\infty} \int_{\Gamma_R} \frac{e^{-i\frac{yv}{\pi}}\ dv}{\sinh(v)}. 
\end{align*}
This integral is constant in $R$, and equal to $\textstyle 2\pi i .{\rm Res}\left( \frac{e^{-i\frac{yv}{\pi}}}{\sinh(v)}, v=i\pi\right) =-2\pi i e^y$ by the residue theorem. We deduce
$$\partial_{y}^2 \left( \int_{\mr +i0} \frac{e^{-i\frac{yv}{\pi}}\ dv}{v^2\sinh(v)}\right) =\frac{2ie^y}{\pi (1+e^{y})}.$$
Finally, we can integrate twice along a path running from $-\infty$ along the real axis up to $\mathfrak{R}(y)$, and then along a straight segment up to $y\in \mr+i(-\pi,\pi)$, since the integrands are continuous in this strip:
\begin{align*}
\partial_{y} \left( \int_{\mr +i0} \frac{e^{-i\frac{yv}{\pi}}\ dv}{v^2\sinh(v)}\right) & =\frac{2i}{\pi} \int_{-\infty}^y \frac{e^s}{1+e^{s}}ds =\frac{2i}{\pi} \Log(1+e^y)\\ \int_{\mr +i0} \frac{e^{-i\frac{yv}{\pi}}\ dv}{v^2\sinh(v)}& = \frac{2i}{\pi} \int_{-\infty}^y \Log(1+e^s) ds = -\frac{2i}{\pi} {\rm Li}_2(-e^y).
\end{align*}
The result follows.\cvd
\medskip


\subsection{Asymptotics of $\hat{S}_N(z)$ and $g_N(z)$}\label{sec:asySNfev26}

Let us start with a straightforward lemma.


\begin{lem}\label{lem:bound:exp:1-exp}
For all $\delta\in ]0,\pi[$, for all $z \in ]-\infty,M] + i([\delta, 2\pi-\delta]+2\pi k)$, $k\in \mz$, we have:
$$
\left \vert
\dfrac{e^z}{1-e^z}
\right \vert \leq \dfrac{e^{M/2}}{\delta\sqrt{1- \frac{\pi^2}{24}}}.
$$
\end{lem}

\begin{proof} It is enough to do the case $k=0$. For $\delta\in ]0,\pi[$ and $z = x+iy \in ]-\infty,M] + i[\delta, 2\pi-\delta]$, we have
 \begin{align*}
 \left\vert \dfrac{e^z}{1-e^z}
 \right \vert^2 = 
 \dfrac{e^{2x}}{|1-e^z|^2} = 
\dfrac{e^{2x}}{1+e^{2x}-2e^x \cos(y)} & = 
\dfrac{e^{x}}{2\cosh(x)-2\cos(y)} \\ & \leq 
 \dfrac{e^M}{2\cosh(x)-2\cos(y)}.
 \end{align*}
For $y \in [\delta,2\pi-\delta]$ fixed, 
$\dfrac{1}{2\cosh(x)-2\cos(y)}$ is maximal at $x=0$, where it is equal to
$$\dfrac{1}{2-2\cos(y)}
= \dfrac{1}{2-2+4\sin(y/2)^2}
= \dfrac{1}{4 \sin(y/2)^2} .
$$
Moreover, for $y\in [\delta,2\pi-\delta]$ we have $\sin(y/2)\geq \sin(\delta/2)$, and since $0<\delta/2 <\pi/2$, a Taylor-Lagrange expansion with remainder at order $4$ gives $\textstyle \sin(\delta/2) \geq \delta/2 - \frac{1}{6}(\delta/2)^3>\delta/2\left (1-\frac{\pi^2}{24}\right )>0$. Therefore
$$\dfrac{1}{4 \sin(y/2)^2} \leq \dfrac{1}{4(\delta/2 - \frac{1}{6}(\delta/2)^3)^2} \leq \dfrac{1}{\delta^2(1- \frac{\pi^2}{24})}.$$
The lemma follows.
\end{proof}
 
We will use the following {\it uniform} estimate of the relation between ${\rm Li}_2$ and the semi-classical limit of the function $\hat S_N$.
\begin{lem}\label{estimatehatS} There exists constants $B',B''>0$ such that for all  $\delta\in ]0,\pi[$, $M \in \R$,  large enough $N\geq 3$ odd, and $z\in ]-\infty,M] +i[\textstyle \delta-\frac{\pi}{N}, 2\pi-\delta-\frac{\pi}{N}]$ we have
\begin{equation}\label{equalitylemmaasyoct25}\Log(\hat{S}_N(z)) = \frac{N}{2i\pi}{\rm Li_2}(e^{z}) -\frac{1}{2} \Log(1-e^{z}) + \frac{1}{N}\Psi_N(z),
\end{equation}
where $\Psi_N$ is a holomorphic function of $z$, with formula given by \eqref{defXiNjanv26}-\eqref{defPsiNjanv26}, satisfying
\begin{equation}\label{UboundPsi}
\vert \Psi_N(z)\vert \leq B_\delta+\dfrac{\pi e^{M/2}}{2\delta\sqrt{1- \frac{\pi^2}{24}}},\ \mathrm{with}\ B_\delta := B'/\delta+B''.
\end{equation}  
Moreover, setting $\mathrm{c}_M:=\sqrt{1+e^M}$, we have
 $$\left\vert \mathfrak{R}\left(\Log(\hat{S}_N(z)) -\frac{N}{2i\pi}{\rm Li_2}(e^{z})\right) \right\vert \leq \Log(\mathrm{c}_M) + \frac{B_\delta}{N}$$
 or equivalently
$$ \dfrac{1}{\mathrm{c}_M}\exp\left(-\frac{B_\delta}{N}\right) \leq
\left\vert \hat{S}_N(z)\exp\left( -\frac{N}{2i\pi}{\rm Li_2}(e^z)\right) \right\vert \leq \mathrm{c}_M\exp\left(\frac{B_\delta}{N}\right).$$
\end{lem}
\begin{remark}\label{rem:largeN} {\rm (i) The condition ``large enough $N\geq 3$'' is in place to ensure that $\textstyle \delta-\frac{\pi}{N}>0$, so that the half-strip $\textstyle ]-\infty,M] +i[\textstyle \delta-\frac{\pi}{N}, 2\pi-\delta-\frac{\pi}{N}]$ avoids cuts in the domain \eqref{holdomPsiN}. Thus, if $\mathfrak{R}(z)<0$ this condition is unnecessary and $\textstyle \delta-\frac{\pi}{N}\leq 0$ is admissible.\\
(ii) The definition of $\Psi_N$ from $\Xi_N$ (see \eqref{defXiNjanv26}-\eqref{defPsiNjanv26}) shows that the identity \eqref{equalitylemmaasyoct25} holds true for all $z$ in the strip $\mr +i]\textstyle -\frac{\pi}{N}, 2\pi-\frac{\pi}{N}[$.\\
(iii) The lemma generalizes immediately to the situation where one considers distinct constants $\delta^-, \delta^+\in ]0,\pi[$  instead of $\delta$, and takes $z\in ]-\infty,M] +i[\textstyle \delta^--\frac{\pi}{N}, 2\pi-\delta^+-\frac{\pi}{N}]$. Then one has \eqref{UboundPsi} with $\delta:= \min(\delta^-,\delta^+)$. This may be useful when one is willing sharp uniform bounds on specific sets.\\ 
(iv)  We can give explicit numerical values for the constants $B',B''>0$ in Lemma \ref{estimatehatS}, following the computations in \cite[Lemma 7.13]{BGP-N} (see the formula of $B_\delta$ on page 367 of that paper).
}\end{remark}
\proof It follows from Lemmas 7.13 and 7.14 in \cite{BGP-N} by a change of variable and a very small adaptation. Let us give a few details. First we consider the inequalities, since for them the adaptation is simpler to describe.

Lemmas 7.13 and 7.14 in \cite{BGP-N} deal with $\textstyle \Phi_{\rmb}(\frac{y}{2\pi \rmb})$, with the assumptions $\mathfrak{I}(y)\in [\delta,\pi-\delta]$ and $\mathfrak{I}(y)\in [-\pi+\delta,-\delta]$ respectively. From the proof of these lemmas, it is easy to see that these assumptions, keeping the same conclusions, can be extended to $\mathfrak{I}(y)\in [0,\pi-\delta]$ and $\mathfrak{I}(y)\in [-\pi+\delta,0]$ respectively. By setting $\rmb:= 1/\sqrt{N}$ and $y=z-i\pi+i\pi/N$, these conclusions imply immediately that, given $\delta>0$, $N$, and $\textstyle z\in \mr + i[\delta-\frac{\pi}{N}, 2\pi-\frac{\pi}{N}-\delta]$, there exists a constant $B_\delta>0$ as in the statement such that
 $$\left\vert \mathfrak{R}\left(\Log(\hat{S}_N(z)) -\frac{N}{2i\pi}{\rm Li_2}(e^{z+\frac{i\pi}{N}})\right) \right\vert \leq \frac{B_\delta}{N}.$$
 More precisely, denoting 
$$\epsilon(z):= \dfrac{1}{z^2}\left (\dfrac{z}{\sinh(z)}-1\right )$$ (the Taylor remainder at $0$ of order $2$ of the function $z \mapsto z/\sinh(z)$), and $\Omega\subset \C$ a contour equal to $\R$ except near $0$ where it avoids $0$ upwards while staying in a disk $D(0,R)$ with center $0$ and radius $R\in ]0,\pi[$, we have
\begin{equation}\label{eq:BAGPN:Xi}
\Log(\hat{S}_N(z)) -\frac{N}{2i\pi}{\rm Li_2}(e^{z+\frac{i\pi}{N}})
= \dfrac{1}{N} \Xi_N(z)
\end{equation}
for $\textstyle z\in \mr + i[\delta-\frac{\pi}{N}, 2\pi-\frac{\pi}{N}-\delta]$, where 
\begin{equation}\label{defXiNjanv26}
\Xi_N(z) :=
 \int_{v\in \Omega} \epsilon\left (\frac{v}{N}\right ) 
\dfrac{\exp(-i\frac{z v}{\pi}-v+\frac{v}{N})}{4 \sinh(v)}dv
\end{equation}
is holomorphic in the open strip $\mr +i]\textstyle -\frac{\pi}{N}, 2\pi-\frac{\pi}{N}[$ and satisfies $\vert \Xi_N(z)\vert \leq B_\delta$ on the closed substrip $\mr +i[\textstyle \delta-\frac{\pi}{N}, 2\pi-\delta-\frac{\pi}{N}]$. (We stress that in Lemma 7.13 of  \cite{BGP-N} the stated upper bound is $\vert \mathfrak{R}(\Xi_N(z))\vert \leq B_\delta$, where the constant $B_\delta:= B'/\delta+B''$ is described explicitly on page 367, but the conclusion is deduced from the inequality $\vert \mathfrak{R}(\Xi_N(z))\vert \leq\vert \Xi_N(z)\vert$ and an upper bound for $\vert \Xi_N(z)\vert$).

We want to replace the term $\textstyle \frac{N}{2i\pi}{\rm Li_2}(e^{z+\frac{i\pi}{N}})$ with $\textstyle \frac{N}{2i\pi}{\rm Li_2}(e^{z})$. For this, we will use a Taylor expansion.

Recall that we take $z\in ]-\infty,M] +i[\textstyle \delta-\frac{\pi}{N}, 2\pi-\delta-\frac{\pi}{N}]$, with $N$ large enough so that $\textstyle \delta-\frac{\pi}{N}>0$. In particular, the arguments of the logarithms and dilogarithms in the following formulas will avoid the cuts of these functions. Since
\begin{equation}\label{Taylor0}
{\rm Li_2}(e^{z+\frac{i\pi}{N}}) - {\rm Li_2}(e^{z}) = - \frac{i\pi}{N} \int_0^1 \Log(1-e^{z+\frac{i\pi}{N}t}) dt,
\end{equation}
we have
$$ \mathfrak{R}\left(\frac{N}{2i\pi}{\rm Li_2}(e^{z+\frac{i\pi}{N}})
- \frac{N}{2i\pi}{\rm Li_2}(e^{z})\right) = - \frac{1}{2} \int_0^1 \Log\left\vert 1-e^{z+\frac{i\pi}{N}t}\right\vert dt
= -  \int_0^1 \Log\left\vert 1-e^{z+\frac{i\pi}{N}t}\right\vert^{\frac{1}{2}} dt. $$

Now $\vert 1-e^z\vert^{\frac{1}{2}}\leq \sqrt{1+ \vert e^z\vert} \leq \sqrt{1+e^M}$ for all $\textstyle z\in ]-\infty,M] +i[\delta-\frac{\pi}{N}, 2\pi-\delta]$. Define $\mathrm{c}_M:=\sqrt{1+e^M}$. We get, for every $z\in ]-\infty,M] +i[\textstyle \delta-\frac{\pi}{N}, 2\pi-\delta-\frac{\pi}{N}]$:

$$\left\vert \mathfrak{R}\left(\Log(\hat{S}_N(z)) -\frac{N}{2i\pi}{\rm Li_2}(e^{z})\right) \right\vert \leq \Log(\mathrm{c}_M) + \frac{B_\delta}{N}.$$
The pair of inequalities in the statement immediately follows. 


Let us now prove the equality \eqref{equalitylemmaasyoct25} and the upper bound \eqref{UboundPsi}.
From (\ref{eq:BAGPN:Xi}) and (\ref{Taylor0}), we obtain
\begin{align*}
\Log(\hat{S}_N(z)) 
&= \frac{N}{2i\pi}{\rm Li_2}(e^{z+\frac{i\pi}{N}})
+ \dfrac{1}{N} \Xi_N(z)\\
&= \frac{N}{2i\pi}{\rm Li_2}(e^{z})  - \frac{1}{2} \int_0^1 \Log(1-e^{z+\frac{i\pi}{N}t}) dt
+ \dfrac{1}{N} \Xi_N(z).
\end{align*}
Another Taylor expansion gives us
\begin{equation}\label{eq:taylor:log:exp}
\Log(1-e^{z+\frac{i\pi}{N}t}) = \Log(1-e^{z}) - \frac{1}{N}\mathcal{E}_N(z,t),
\end{equation}
where $\mathcal{E}_N(z,t):= (i\pi t) \int_0^1 \dfrac{e^{z+\frac{i\pi}{N}ts}}{1-e^{z+\frac{i\pi}{N}ts}}ds$. Hence we obtain
$$
\Log(\hat{S}_N(z)) 
= \frac{N}{2i\pi}{\rm Li_2}(e^{z})  - \frac{1}{2}  \Log(1-e^{z}) 
+ \frac{1}{2N}\int_0^1\mathcal{E}_N(z,t)dt
 + \dfrac{1}{N} \Xi_N(z).
$$
This gives (\ref{equalitylemmaasyoct25}), by setting
\begin{equation}\label{defPsiNjanv26}
\Psi_N(z):= \Xi_N(z)+\dfrac{1}{2}\int_0^1\mathcal{E}_N(z,t)dt
=\Xi_N(z)+\dfrac{i\pi}{2}\int_{t=0}^1 t \int_{s=0}^1\dfrac{e^{z+\frac{i\pi}{N}ts}}{1-e^{z+\frac{i\pi}{N}ts}}dsdt.
\end{equation}
Consider the strip $]-\infty,M] +i[\textstyle \delta-\frac{\pi}{N}, 2\pi-\delta-\frac{\pi}{N}]$. We know that $|\Xi_N(z)|\leq B_\delta$, and from Lemma \ref{lem:bound:exp:1-exp} the second term gives:
$$\left |
\dfrac{i\pi}{2}\int_{t=0}^1 t \int_{s=0}^1\dfrac{e^{z+\frac{i\pi}{N}ts}}{1-e^{z+\frac{i\pi}{N}ts}}dsdt
\right | \leq \dfrac{\pi}{2 } \int_{s=0}^1\left |
 \dfrac{e^{z+\frac{i\pi}{N}ts}}{1-e^{z+\frac{i\pi}{N}ts}} \right | ds
 \leq \dfrac{\pi e^{M/2}}{2\delta\sqrt{1- \frac{\pi^2}{24}}}.$$
By the triangle inequality, \eqref{UboundPsi} follows at once.\cvd
\medskip

Let us draw the following important though easy consequence of Lemma \ref{estimatehatS} and the functional equation \eqref{eqfunchatSLog}. It will be used in Lemma \ref{lem:reformintqjui25}.

By the domains where $\Log(\hat{S}_N(z))$ (deduced after \eqref{eqfunchatSLog}) and ${\rm Li_2}(e^{z})$  and $\Log(1-e^{z})$ are holomorphic functions (here, $\textstyle \mc\setminus \left(\cup_{k\in \mz} \left(2i\pi k +[0,+\infty[\right)\right)$), the identity (\ref{equalitylemmaasyoct25}) immediately shows that $\Psi_N$ has a holomorphic extension on the domain 
\begin{equation}\label{holdomPsiN}
\mc \setminus \left(\bigcup_{p\in \mn} \left([0,+\infty[+i\left(2\pi + \frac{2\pi p}{N}\right)\right) \bigcup \left(\bigcup_{l\in \mn}\left( [0,+\infty[-i(l+1)\frac{2\pi}{N}\right)\right) \bigcup [0,+\infty[ \right).
\end{equation}
In particular $\Psi_N$ is holomorphic on the domain (see Figure \ref{fig:Uet+})
$$U:=\left \lbrace z\in \mc\ \vert\ \mathfrak{R}(z) <0 \right \rbrace \bigcup \left \lbrace z\in \mc\ \vert \ 0 < \mathfrak{I}(z) < 2\pi\right\rbrace.$$
In the following lemma, for every $M\in \mr$, $\alpha\in ]0,1[$, $k\in \mz_{\leq 0}$, $K>2\pi$, and $c>0$ we consider the sets $U_{M,\alpha,k,K,c}\subset \mc$ formed by the points $z$ such that (see Figure \ref{fig:Uet+}):
\begin{itemize}
\item $\mathfrak{R}(z)\leq M$ and $\textstyle (\alpha-1)\frac{\pi}{N}< \mathfrak{I}(z)< 2\pi-(\alpha+1)\frac{\pi}{N}$, or 
\item $\mathfrak{R}(z)<0$ and $\textstyle 2\pi k + (\alpha-1)\frac{\pi}{N}\leq \mathfrak{I}(z)\leq (\alpha-1)\frac{\pi}{N}$, or 
\item $\textstyle \mathfrak{R}(z)< -c$ and $\textstyle 2\pi-(\alpha+1)\frac{\pi}{N}\leq \mathfrak{I}(z)\leq K$.
\end{itemize}
\medskip

\begin{figure}[!h]
\begin{tikzpicture}
\draw[->] (-6,0)--(6,0);
\draw[->] (0,-6)--(0,6);

\draw (0,0-.03) node {\Huge $\cdot$};
\draw (0+.3,0+.3) node {$0$};
\draw (0,2-.03) node {\Huge $\cdot$};
\draw (0+.5,2-.03+.3) node {$2i\pi$};

\draw[color=blue,thick] (0,6)--(0,2)--(6,2);
\draw[color=blue,thick] (0,-6)--(0,0)--(6,0);

	\draw[white,fill=blue!30,opacity=0.5, ] (-6,6)--(0,6)--(0,2)--(6,2)--(6,0)--(0,0)--(0,-6)--(-6,-6);
	
\draw (-2,5) node {\Huge \color{blue} $U$};

	\draw[red ,fill=red!50,opacity=0.5, ] (-6,3.5)--(-2,3.5)--(-2,1.7)--(4,1.65)--(4,-0.15)--(0,-0.15)--(0,-4-0.15)--(-6,-4.15);
	
\draw[color=red] (-2,3.5-.03) node {\Huge $\cdot$};
\draw[color=black] (-2,3.5+.3) node {\scriptsize $-c+i K$};

\draw[color=red] (-2,1.7-.03) node {\Huge $\cdot$};
\draw[color=black] (-3.8,1.6) node { \scriptsize $-c+i \left (2\pi-(\alpha+1)\frac{\pi}{N}\right )$};

\draw[color=red] (4,1.7-.07) node {\Huge $\cdot$};
\draw[color=black] (5.7,1.6) node { \scriptsize $M+i \left (2\pi-(\alpha+1)\frac{\pi}{N}\right )$};

\draw[color=red] (4,-.19) node {\Huge $\cdot$};
\draw[color=black] (5.2,-.5) node { \scriptsize $M+i (\alpha-1)\frac{\pi}{N}$};

\draw[color=red] (0,-.19) node {\Huge $\cdot$};
\draw[color=black] (.9,-.55) node { \scriptsize $i(\alpha-1)\frac{\pi}{N}$};

\draw[color=red] (0,-4-.19) node {\Huge $\cdot$};
\draw[color=black] (1.5,-4-.2) node { \scriptsize $i\left ((\alpha-1)\frac{\pi}{N}+2k\pi\right )$};


\draw (-3,-2) node {\Huge \color{red!40!black} $U_{M,\alpha,k,K,c}$};

\end{tikzpicture}
\caption{The domain $U$ and the sets $U_{M,\alpha,k,K,c}$.}\label{fig:Uet+}
\end{figure}
\begin{lem}\label{extboundPsiNjanv26} (i) The sequence of functions $\Psi_N$ converges simply to a holomorphic function on the strip $0 < \mathfrak{I}(z) < 2\pi$.\\
(ii) The function $\textstyle \vert \exp(\frac{1}{N} \Psi_N)\vert$ is bounded from above by a constant independent of $N$ on each set $U_{M,\alpha,k,K,c}$.\\
(iii) The sequence of functions $\textstyle \exp(\frac{1}{N} \Psi_N)$ converges uniformly to the constant function with value $1$ on  compact subsets of $U$.
\end{lem}
\begin{remark}{\rm (i) The condition $\textstyle \mathfrak{R}(z)< -c$ for some $c>0$ when $\textstyle 2\pi-(\alpha+1)\frac{\pi}{N}\leq \mathfrak{I}(z)\leq K$ is in place to ensure that the half-space stays at distance from the singular points $2i\pi+ 2i\pi p/N$, $p\in \mn$, of $\Psi_N$.\\ 
(ii) The proof below provides an explicit upper bound of $\textstyle \vert \exp(\frac{1}{N} \Psi_N)\vert$ on $U_{M,\alpha,k,K,c}$.} \end{remark} 

\begin{proof} (i) Any point of $\textstyle \mr +i]0, 2\pi[$ is contained in $\textstyle \mr +i]-\frac{\pi}{N}, 2\pi-\frac{\pi}{N}[$  for $N$ large enough, where $\Psi_N$ has the integral formula given by \eqref{defPsiNjanv26} and \eqref{defXiNjanv26}. By using Lemma \ref{lem:bound:exp:1-exp} and Lebesgue's dominated convergence theorem it is clear that the second summand in the formula \eqref{defPsiNjanv26} converges simply on $\textstyle \mr +i]0, 2\pi[$. Thus it remains to prove it also for $\Xi_N$. 

Recall the function $\epsilon$ in \eqref{defXiNjanv26}. It is easy to see that $\epsilon$ is holomorphic on $\mr\cup D(0,R)$, that $\textstyle \lim_{x\to 0}\epsilon(x) = -\frac{1}{6}$, and that there is a scalar $\sigma_R>0$ such that $\vert \epsilon(x)\vert \leq \sigma_R$ for all $x\in  \Omega \cup D(0,R)$ (see \cite[pp. 364-365]{BGP-N} for details). Let us split $\Xi_N(z)$ as
\begin{multline} \Xi_N(z) = \int_{v\in \Omega\cap D(0,R) } \epsilon\left (\frac{v}{N}\right ) \dfrac{\exp(-i\frac{z v}{\pi}-v+\frac{v}{N})}{4 \sinh(v)}dv \\ + \int_{v\in ]-\infty,-R]} \epsilon\left (\frac{v}{N}\right ) \dfrac{\exp(-i\frac{z v}{\pi}-v+\frac{v}{N})}{4 \sinh(v)}dv + \int_{v\in [R,+\infty[} \epsilon\left (\frac{v}{N}\right ) \dfrac{\exp(-i\frac{z v}{\pi}-v+\frac{v}{N})}{4 \sinh(v)}dv.
\end{multline}
Note that for all $N$ the integrand is a holomorphic function of $z$ and $v$. It has modulus less than $\sigma_R  \textstyle \vert \frac{\exp(-i\frac{z v}{\pi}-v+R)}{4 \sinh(v)} \vert$ for $v\in \Omega\cap D(0,R)$, where this function is continuous and hence integrable. Now set $z=x+iy$, so  that $0<y<2\pi$. For a real $v\ne 0$ we have 
\begin{align*}\left\vert \epsilon\left (\frac{v}{N}\right ) \dfrac{\exp(-i\frac{z v}{\pi}-v+\frac{v}{N})}{4 \sinh(v)} \right\vert & \leq \sigma_R  \left \vert \frac{\exp(-i\frac{z v}{\pi}-v+\frac{v}{N})}{4 \sinh(v)} \right\vert \\ & = \sigma_R  \frac{\exp(v(-1 + \frac{y}{\pi}+\frac{1}{N}))}{4 \sinh(v)}.
\end{align*}
Let $c^-, c^+$ be positive real numbers such that $\textstyle 0<c^-<\frac{y}{\pi}<c^+<2$, and assume that $N$ is large enough so that $\textstyle \frac{y}{\pi}+\frac{1}{N}<c^+$.  Then the RHS is $\leq \textstyle \sigma_R  \frac{\exp(v(c^+ -1))}{4 \sinh(v)}$ on $[+R,+\infty[$ and $\leq \textstyle \sigma_R  \frac{\exp(v(c^- -1))}{4 \sinh(v)}$ on $[-\infty,-R[$, where these functions are integrable on these intervals. Then we can apply Lebesgue's dominated convergence theorem to the three integrals. By summing the results we get
$$\lim_{N\rightarrow +\infty}  \Xi_N(z) = -\frac{1}{6} \int_{v\in \Omega} \dfrac{\exp(-i\frac{z v}{\pi}-v)}{4 \sinh(v)}dv,$$
The arguments above show also that the integral on the RHS is a holomorphic function of $z$ in the strip $\mr+i]0, 2\pi[$, which concludes the proof of (i).\\ 
(ii) First consider $\textstyle \vert \exp(\frac{1}{N} \Psi_N)\vert$ on $\textstyle ]-\infty,M] +i]-\frac{\pi}{N}, 2\pi-\frac{\pi}{N}[$. Let $\alpha>0$ be fixed, and apply \eqref{UboundPsi} with $\delta$ of the form $\delta_N:=\textstyle \alpha\frac{\pi}{N}$. For any $z\in \textstyle ]-\infty,M] +i[\delta_N-\frac{\pi}{N}, 2\pi-\delta_N-\frac{\pi}{N}]$, we find 
\begin{equation}\label{boundPsiNseqstripjanv26}
\frac{1}{N}\vert \Psi_N(z)\vert\leq \frac{B'}{\alpha\pi} +\dfrac{\pi e^{M/2}}{2\alpha\pi\sqrt{1- \frac{\pi^2}{24}}}+\frac{B''}{N},
\end{equation}
which is bounded from above by a constant independent of $N$. This proves the claim on the strip $\textstyle (\alpha-1)\frac{\pi}{N}< \mathfrak{I}(z)< 2\pi-(\alpha+1)\frac{\pi}{N}$.\\
Assume now that $\mathfrak{R}(z)<0$. Denote by $C_{M,\alpha,B',B''}$ the constant on the RHS of \eqref{boundPsiNseqstripjanv26}. By repeated use of \eqref{eqfunchatSLog} we can shift $z$ by $-2i\pi$, thus getting $\textstyle \mathfrak{R}(\Log (\hat S_{N}(z-2i\pi))) = \mathfrak{R}(\Log (\hat S_{N}(z))) + \sum_{k=1}^N \Log\vert 1-e^{z+\frac{2i\pi}{N}}\vert = \mathfrak{R}(\Log (\hat S_{N}(z))) + \Log\vert 1-e^{Nz}\vert$. Then the difference of \eqref{equalitylemmaasyoct25} with the same identity where $z$ is replaced by $z-2i\pi$ has real part 
\begin{equation}\label{shiftby2pi}
\mathfrak{R}(\Psi_N(z)) - \mathfrak{R}(\Psi_N(z-2i\pi)) = -N\Log\vert 1-e^{Nz}\vert.
\end{equation}
Therefore $\mathfrak{R}\left(\Psi_N(z-2i\pi)\right) \leq \mathfrak{R}\left(\Psi_N(z)\right)+N\Log(1+\vert e^{Nz}\vert)\leq \mathfrak{R}\left(\Psi_N(z)\right)+N\Log(2)$, and hence $\textstyle \vert \exp(\frac{1}{N} \Psi_N(z))\vert = \exp(\frac{1}{N} \mathfrak{R}\left(\Psi_N(z)\right))\leq \exp(C_{M,\alpha,B',B''}+k\Log(2))$ for any $z$ in a  half-strip $\textstyle ]-\infty,0[ +i(2\pi k'+[\delta_N-\frac{\pi}{N}, 2\pi-\delta_N-\frac{\pi}{N}])$, where $k\leq k'\leq 0$.

To fix the ideas take now for instance $\textstyle \alpha:= \frac{1}{2}$ (namely, in the following discussion $\alpha$ must be chosen so that the width of the ``narrow'' half-strips defined below is $\textstyle <\frac{2\pi}{N}$, hence the width $2\pi - 2\delta_N$ of the above half-strips is $> \textstyle 2\pi - \frac{2\pi}{N}$, whence $\alpha\in ]0,1[$). Denote by $U'$ the union of the above half-strips, $\textstyle ]-\infty,0[ +i(2\pi k'+[-\frac{\pi}{2N}, 2\pi-\frac{3\pi}{2N}])$, where $k\leq k'\leq 0$. The set $U_{M,\alpha,k,K,c}$ is the union of $U'$ with the ``narrow'' half-strips $\textstyle ]-\infty,0[ +i\left( 2\pi k'+ [-\frac{3\pi}{2N},-\frac{\pi}{2N}]\right)$, $k-1\leq k'\leq 0$, and $\textstyle ]-\infty,-c[ +i[2\pi-\frac{3\pi}{2N}, K]$.

Thus it remains to prove the bound when $z$ lies within these half-strips. Consider first the ``narrow'' ones, with $k-1\leq k'\leq 0$. For any such a point $z$, we have $z+\textstyle{\frac{2i\pi}{N}}\in U'$. Therefore we consider the identity \eqref{eqfunchatSLog}. By means of \eqref{equalitylemmaasyoct25} it yields
\begin{multline*}
\frac{1}{N}  \left(\Psi_N(z-\textstyle{\frac{2i\pi}{N}}) - \Psi_N(z)\right)   \\ = \frac{N}{2i\pi}\left({\rm Li_2}(e^{z})-{\rm Li_2}(e^{z-\frac{2i\pi}{N}}) \right) +\frac{1}{2}\left(\Log(1-e^{z-\frac{2i\pi}{N}})-\Log(1-e^{z}) \right)+ \Log(1-e^{z}).
\end{multline*}
Using the Taylor expansion $\textstyle {\rm Li_2}(e^{z-\frac{2i\pi}{N}}) - {\rm Li_2}(e^{z})  = - \frac{2i\pi}{N} \int_0^1 \Log(1-e^{z-\frac{2i\pi}{N}t}) dt$ and changing $z$ to $\textstyle  z+\frac{2i\pi}{N}$ this can be written
$$\frac{1}{N}  \left(\Psi_N(z) - \Psi_N\left((z+\frac{2i\pi}{N}\right)\right) = \int_0^1 \Log(1-e^{z+\frac{2i\pi}{N}t}) dt +\frac{1}{2}\left(\Log(1-e^{z+\frac{2i\pi}{N}})+\Log(1-e^{z}) \right).$$
Since we assume $\mathfrak{R}(z)<0$, the real part of the RHS is bounded from above by $2\Log(2)$, and hence
\begin{multline*}\left\vert \exp\left(\frac{1}{N} \Psi_N(z)\right)\right\vert \leq \exp\left(\frac{1}{N} \mathfrak{R}\left(\Psi_N\left(z+\frac{2i\pi}{N}\right)\right)+2\log(2)\right)\\ \leq \exp(C_{M,\alpha,B',B''}+(k+2)\Log(2)).
\end{multline*}
Finally, assume that $\mathfrak{R}(z)<-c$, $c>0$. Since $\Log\vert 1-e^{z}\vert\ge \Log\vert 1-\vert e^{z}\vert \vert \geq \Log( 1-e^{-c})$, similarly as above we obtain $\textstyle \vert \exp(\frac{1}{N} \Psi_N(z))\vert \leq \exp(\frac{1}{N} \mathfrak{R}(\Psi_N(z-\frac{2i\pi}{N}))- 2\Log( 1-e^{-c}))\leq \exp(C_{M,\alpha,B',B''}- 2\Log( 1-e^{-c}))$ for $z\in \textstyle ]-\infty,-c[ +i[2\pi-\frac{3\pi}{2N}, 2\pi]$. When $2\pi \leq \mathfrak{I}(z)\leq K$, the bound of $\textstyle \vert \exp(\frac{1}{N} \Psi_N(z))\vert$ is obtained similarly by using \eqref{shiftby2pi}. This concludes the proof of (ii).\\ 
(iii) First note that any compact subset of $U$ is contained in $U_{M,\alpha,k,K,c}$ for some $M,\alpha,k,K$ and $c$, for $N$ large enough. By (ii) above and Montel's theorem, it follows that the sequence of functions $\textstyle \exp(\frac{1}{N} \Psi_N(z))$ is a {\it normal family} (that is, it has a subsequence which converges uniformly on compact subsets) on $U$. Since by (i) it converges simply to $1$ on a subset of $U$ having a limit point, by Vitali's Theorem on the convergence of holomorphic functions, the convergence is uniform on all compact subsets of $U$. This concludes the proof.
\end{proof}
 
\color{black}

Recall that $y^{1/N}:=\exp(\Log(y)/N)$ for any $y\in \mc^*$. Put 
\begin{equation}\label{gfunctiondef}
g_N(z):=\prod_{j=1}^{N-1} (1-z\zeta^{-j})^{j/N}.
\end{equation}
In order to prove Theorem \ref{asyinvteo}, we will need to study asymptotics of $g_N(e^z)$ for $z=\bl_{0,N}$ of the form \eqref{defseqNcolor}. First note that, by collecting conjugate terms it is immediate that $\vert g_N(1)^N\vert =N^{\frac{N}{2}}$, and factorizing by $\zeta^{-j/2}$ each term in the product yields
$$ g_N(1)^N = e^{\frac{\pi i}{12}(N-2)(N-1)(2N-1)} \prod_{j=1}^{N-1}2^j\sin\left(\frac{\pi j}{N}\right)^j$$
where the product is real positive. Therefore 
\begin{equation}\label{cstBBP}
g_N(1)^N  = N^{\frac{N}{2}}e^{\frac{\pi i}{12}(N-2)(N-1)(2N-1)}.
\end{equation}

Before considering $g_N(e^z)$ for more general $z$, let us do some rewriting. We have, for any odd integer $N$ and any $z \notin (2 i \pi/N) \Z$ (so that the following quotients are defined):
\begin{align}  g_N(e^z) & = \prod_{k=1}^{N-1} \bigl(1-e^z\zeta^{-k}\bigr)^{k/N}\nonumber  \\ & =  \prod_{k=1}^{N-1} \biggl(\frac{\hat S_N(z + 2(N-(k+1))i\pi/N)}{\hat S_N(z+ 2(N-k)i\pi/N)}\biggr)^{k/N}\nonumber\\  & =   \hat S_N(z)^{(N-1)/N}\ \prod_{k=1}^{N-1} \hat S_N\left(z+2(N-k)i\pi/N\right)^{-1/N} \nonumber \\ & =  \hat S_N(z) \ \prod_{k=1}^{N} \hat S_N\left(z+2ki\pi/N\right)^{-1/N}.\label{prodformgN} \end{align}

Now, it is tempting to use Lemma \ref{estimatehatS} to compare $g_N(e^z)$ to
\begin{equation}\label{ratiogNclass0mars25}
\exp\left( \frac{N}{2i\pi}{\rm Li_2}(e^z)\right) \cdot 
\prod_{k=1}^{N} \exp\left( \frac{N}{2i\pi}{\rm Li_2}(e^{z+2ki\pi/N})\right)^{-1/N}, 
\end{equation}
an expression that can be simplified thanks to the following factorization formula (see for example \cite[page 7]{Z}):

\begin{prop}
For any $x \in \C$, and any positive integer $N$, we have:
$${\rm Li_2}(x)=N \sum_{y \in \C, \ y^N=x} {\rm Li_2}(y).$$
\end{prop}

In particular, for any $z \in \C$ and any positive integer $N$, we have:
$$ \sum_{k=1}^N {\rm Li_2}(e^{z+2ki\pi/N})=\dfrac{1}{N} {\rm Li_2}(e^{Nz}).$$

It immediately follows that $g_N(e^z)$ should be ``comparable" (again, we are speaking non-rigorously for now) to 
\begin{equation}\label{ratiogNclassmars25}
\exp\left( \frac{N}{2i\pi}{\rm Li_2}(e^z)- \frac{1}{2i\pi N}{\rm Li_2}(e^{Nz})\right),
\end{equation}
whose asymptotics look much simpler to study.

Let us now turn back to rigor. We need to be careful about both the requirements that $z \notin (2 i \pi/N) \Z$ and that all the points  $z+2ki\pi/N$ live in a domain where Lemma \ref{estimatehatS} can be applied (and if not, we need to keep track of correction terms).

\begin{lem}\label{factorest} Let $u_0\in \mc\setminus \mr$, and for any odd integer $N$, let $\bl_{0,N}$ be such that $\bu_{0,N}:= e^{\bl_{0,N}}$ satisfies $\bu_{0,N}^N = u_0$, and $\bl_{0,N} = \bl_{0,\infty} + O_{N\to \infty}\left (N^{-1}\right )$, where $\bl_{0,\infty}\in i\mr$. We have:

(i) $\vert g_N(\bu_{0,N})\vert$ is bounded from below and above by the product of $e^{\frac{N}{2\pi} \mathfrak{I}({\rm Li_2}(e^{\bl_{0,\infty}}))}$ with a positive constant independent of $N$. In particular, if ${\rm Li_2}(e^{\bl_{0,\infty}})\in \mr$, then $\vert g_N(\bu_{0,N})\vert$ is bounded from below and above by a positive constant independent of $N$.

(ii) the same result holds true by replacing $g_N(\bu_{0,N})$ with $\hat{S}_N(\bl_{0,N})$. 		
\end{lem}

\proof First assume that $\Im(u_0) > 0$. Set
$$\textstyle \bl_{0,N} = \dfrac{1}{N}(\Log(u_{0})+2\pi i a_{0,N}' )$$
where $a_{0,N}'\in \{0, 1, \ldots, N-1\}$. Define
\begin{equation}\label{defdeltaM}
\delta_N:= \dfrac{1}{N}\min\{\Im(\Log(u_0)), \pi - \Im(\Log(u_0))\} \ \ \text{and} \ \ M:= |\Re(\Log(u_0))|.
\end{equation}
We want to apply the reasoning preceding Lemma \ref{factorest} to the terms $\hat S_N\left(z+2ki\pi/N\right)$ on the right side of \eqref{prodformgN}, taking $z=\bl_{0,N}$. We first notice that $\delta_N>0$, and $\bl_{0,N} \notin (2 i \pi/N) \Z$ as required (since $u_0\ne 1$). We then immediately see that
\begin{equation}\label{chaine}
\bl_{0,N}, \bl_{0,N} + \frac{2i\pi}{N}, \ldots,  \bl_{0,N} + \frac{2i\pi(N-1-a'_{0,N})}{N} \in [-M,M]+i[\delta_N-\frac{\pi}{N},2\pi - \delta_N-\frac{\pi}{N}]
\end{equation}
and
$$ \bl_{0,N} + \frac{2i\pi(N-a'_{0,N})}{N}, \ldots,  \bl_{0,N} + \frac{2i\pi(N-1)}{N} \in [-M,M]+i[2\pi+\delta_N-\frac{\pi}{N},4\pi - \delta_N-\frac{\pi}{N}].$$
These two sequences of scalars realize all the arguments on the right side of \eqref{prodformgN} but the last of the product, $ \bl_{0,N} + 2i\pi$. We can directly apply the inequalities of Lemma \ref{estimatehatS} for $z$ being any one among the $N-a'_{0,N}$ values of the sequence \eqref{chaine}. The error bound is 
\begin{equation}\label{errorboundgNoct25}
\Log(\mathrm{c}_M)+ \dfrac{B_{\delta_N}}{N} = \Log(\mathrm{c}_M) + \dfrac{B'}{\delta_N N} + \dfrac{B''}{N},
\end{equation}
which by \eqref{defdeltaM} is bounded from above by a constant independent of $N$. For $\bl_{0,N} + 2i\pi$ or any of the $a'_{0,N}$ values of the sequence below \eqref{chaine}, we need to modify the corresponding terms $\hat S_N\left(z+2ki\pi/N\right)$ on the right side of \eqref{prodformgN}, by re-shifting $z_k:=z+2ki\pi/N$ using $N$ times the formula \eqref{eqfunchatS}. We have
$$\hat{S}_N(z_k) = \dfrac{\hat{S}_N(z_k-2i\pi)}{1-e^{Nz_k}},$$
each factor $1-e^{Nz_k} = 1-u_0$ is raised at the power $-1/N$ in \eqref{prodformgN}, and these factors are no more numerous than $N$. So the re-shiftings add at worst a bounded non zero term to the error bound \eqref{errorboundgNoct25}, which changes only $\mathrm{c}_M$. Eventually, the ratio of \eqref{prodformgN} over \eqref{ratiogNclass0mars25}, or equivalently \eqref{ratiogNclassmars25}, is bounded from above and below by the product of $N+1$ positive constants independent of $N$, with $N$ of them raised at the power $1/N$. Hence the ratio \eqref{prodformgN}/\eqref{ratiogNclassmars25} is bounded by a constant. To conclude, it therefore suffices to prove that
\begin{equation}\label{ratiojuil25}
\exp\left( \frac{N}{2i\pi}{\rm Li_2}(e^{\bl_{0,N}})- \frac{1}{2i\pi N}{\rm Li_2}(e^{N\bl_{0,N}})
\right)
\end{equation}
is bounded from above and below by constants independent of $N$ multiplied with $e^{\frac{N}{2\pi} \mathfrak{I}({\rm Li_2}(e^{\bl_{0,\infty}}))}$. But ${\rm Li_2}(e^{N\bl_{0,N}})={\rm Li_2}(u_0)$, and $\bl_{0,N} = \bl_{0,\infty} + O_{N \to \infty}\left (N^{-1}\right )$ implies
$$ {\rm Li_2}(e^{\bl_{0,N}}) ={\rm Li_2}(e^{\bl_{0,\infty}})+O_{N \to \infty}(1/N)$$
by a Taylor expansion as in \eqref{Taylor0} (which is valid, since ${\rm Li_2}$ is differentiable on $\mc \setminus [1,+\infty[$, and $e^{N\bl_{0,N}}=u_0\notin ]1,+\infty[$ implies $e^{\bl_{0,N}} \notin ]1,+\infty[$). It follows
$$\exp\left( \frac{N}{2i\pi}{\rm Li_2}(e^{\bl_{0,N}})\right )= \exp\left(\frac{N}{2\pi} \mathfrak{I}({\rm Li_2}(e^{\bl_{0,\infty}}))\right)\exp (O_{N \to \infty}(1)).$$
This proves the last claim, and concludes the proof of the lemma when $\Im(u_0) > 0$. Similar arguments apply when $\Im(u_0) < 0$: take $\delta_N=\pi/N$, and start the sequence \eqref{chaine} at $\bl_{0,N}+ 2i\pi/N$. Only the arguments $\bl_{0,N}$ and $\bl_{0,N} + 2i\pi$ on the right side of \eqref{prodformgN} are missing from this sequence and the following one. With these changes one can conclude by reasoning as when $\Im(u_0) > 0$. \cvd
