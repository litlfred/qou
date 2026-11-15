---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-007-3-pseudo-gradient-flow-for-the-distance-function
section_title: "Pseudo-gradient flow for the distance function"
section_number: 3
pages: 9-12
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.947
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
\label{sec:pseudo}
The globally defined vector field $V$ constructed in Proposition \ref{prop:vf}
for the set $M\subset\R^n$ satisfying the local distortion bound induces
geometric flows on the complement $\R^n\setminus M$ increasing or decreasing the distance
to $M$. To construct a \emph{distance-increasing} flow $h_M^+:\R^n\setminus M\times [0,1]\to
\R^n\setminus M$ take a cut-off function $\varphi\in C^\infty(\R^n)$ with
\begin{equation}\label{eq:varphi}
\begin{cases}
\varphi\ge 0 & \ON\R^n,\\
\varphi\equiv 1 & \ON B_{\frac12{r_M}-\rho}(M),\\
\varphi\equiv 0 & \ON \R^n\setminus B_{\frac12{r_M}}(M)
\end{cases}
\end{equation}
for some $\rho\in (0,\frac12{r_M})$. Now, define 
\begin{equation}\label{eq:vtilde}
\tilde{V}:=\frac12 r_M\varphi\cdot V\in C^\infty(\R^n,\R^n),
\end{equation}
and consider the initial value problem
\begin{equation}\label{eq:awp}
\begin{cases}
\frac{d}{dt}h(x,t)=\tilde{V}(h(x,t))&\Fo x\in\R^n\setminus M,\,t\in\R,\\
\quad\! h(x,0)=x.
\end{cases}
\end{equation}
According to the Picard-Lindel\"of theorem \eqref{eq:awp} possesses a unique
smooth solution for all times $t\in\R$
with smooth dependence on the initial data.
Define $h_M^+\in C^\infty(\R^n\setminus M\times [0,1],\R^n)$ to be the 
restriction of that solution to the time interval $[0,1]$.
\begin{theorem}[Distance-increasing flow]\label{thm:dist-inc-flow}
Let $M\subset\R^n$ be a non-empty, closed and path-connected set with local distortion
$\delta(M,r_M)<g_n$ at scale $r_M>0$ for $g_n$ as defined in \eqref{eq:dekster-jung}.
Then for every $\rho\in (0,\frac12{r_M})$ there is a function $h_{M,\rho}^+\equiv
h_M^+
\in C^\infty(\R^n\setminus M\times [0,1],\R^n)$ with image $h_M^+(\R^n\setminus
M\times [0,1])\subset \R^n\setminus M$, satisfying
\begin{enumerate}
\item[\rm (1+)] $h_M^+(\cdot,0)=\Id_{\R^n\setminus M},$
\item[\rm (2+)] $h_M^+(\R^n\setminus M,1)\subset \R^n\setminus B_{\frac12{r_M}-\rho}(M)$,
\item[\rm (3+)] $h_M^+(\cdot,t)|_{\R^n\setminus B_{\frac12{r_M}}(M)}=\Id_{\R^n\setminus
B_{\frac12{r_M}}(M)}$ for all $t\in [0,1]$.
\end{enumerate}
Furthermore, the map $h_M^+(\cdot,t):\R^n\setminus M\to\R^n$ is an
embedding for every $t\in [0,1]$, and the function $t\mapsto\dist(h_M^+(x,t),M)$
is non-decreasing on $[0,1]$ for each $x\in\R^n\setminus M$.
\end{theorem}
\begin{proof}
We construct $h_M^+$ as above as the smooth and unique solution to \eqref{eq:awp}
restricted to $[0,1]$.
Uniqueness secures that $h_M^+(\cdot,t):\R^n\setminus M\to\R^n$ is an embedding for
each $t\in [0,1]$. The prescribed initial value in \eqref{eq:awp} guarantees condition
(1+). For $x\in\R^n\setminus B_{\frac12{r_M}}(M)$ the constant function $t\mapsto
h_M^+(x,t):=x$ is the unique solution to \eqref{eq:awp} since 
$\tilde{V}(h_M^+(x,t))=\tilde{V}(x)=\frac12{r_M}\varphi(x)V(x)=0$ because of
\eqref{eq:varphi}, which settles claim (3+). 

As soon as we have proven
that the function $t\mapsto
D(t):=\dist(h_M^+(x,t),M)$ is non-decreasing for each $x\in\R^n\setminus M$, we also know
that $h_M^+(\R^n\setminus M\times [0,1])\subset\R^n\setminus M$.  To prove this
monotonicity it suffices to consider $x\in B_{\frac12{r_M}}(M)\setminus M$ because of
of (3+). Notice that the image $H_x:=h_M^+(x,[0,1])\subset\R^n$ is compact, so that 
by means of (1+)
\begin{equation}\label{eq:Delta}
\Delta_x:=\max_{y\in H_x}\dist(y,M) > 0
\qquad\text{for any }x\in B_{\frac12r_M}(M)\setminus M.
\end{equation}
Therefore,
\begin{equation}\label{eq:Kx}\tag{$*$}
\textstyle\dist(y,M)=\inf_{z\in M}|y-z|=\min_{z\in K_x}|y-z|
=\dist(y,K_x)
\quad\Foa y\in H_x
\end{equation}
where we have set $K_x:=\overline{B_{2\Delta_x}(H_x)}\cap M$. Since $K_x$
is compact we may apply
\cite[Theorem~2.1(4)]{clarke_1975} and 
\cite[Exercise 9.13, p.~99]{clarke-etal_1998}
to infer that the Clarke gradient $\partial (\dist(y,M))$ of the $1$-Lipschitz
function $y\mapsto\dist(y,M)$ is given by
\begin{equation}\label{eq:clarke-gradient}
\textstyle
\partial (\dist(y,M))=\conv \big(\big\{\frac{y-z}{|y-z|}:z\in\Gamma_{K_x}(y)\big\}\big)
\quad\Foa y\in H_x\setminus M \stackrel{\eqref{eq:Delta}}=H_x,
\end{equation}
where $\conv(A)$ denotes the convex hull of a set $A\subset\R^n$, and
$\Gamma_A(y):=\{z\in A:\dist(y,A)=|y-z|\}$. (Notice that here,
$\Gamma_{K_x}(y)=\Gamma_M(y)
$ for all $y\in H_x\setminus M\stackrel{\eqref{eq:Delta}}=H_x$.\footnote{
``$\subset$'' follows by $K_x\subset M$ and~\eqref{eq:Kx}.
``$\supset$'' follows by~\eqref{eq:Kx} and $\dist(y,M)\le\Delta_x$,
so any $z\in M$ with $\dist(y,M)=|y-z|$ satisfies $z\in \overline{B_{\Delta_x}(y)}
\subset\overline{B_{\Delta_x}(H_x)}$.})
Since $h_M^+$ is smooth, the function $D(t)=\dist(h_M^+(x,t),M)$ is
Lipschitz continuous on $[0,1]$, and we can apply the non-smooth
vectorial mean-value theorem \cite[Proposition 2.6.5]{clarke_1990} to deduce
for $0<t_1<t_2<1$ that
\begin{equation}\label{eq:mean-value}
D(t_2)-D(t_1)\in\conv\big(\partial D([t_1,t_2])(t_2-t_1)\big),
\end{equation}
which means that the difference $D(t_2)-D(t_1)$ is contained in the convex hull of the 
set $\{Z(t_2-t_1):Z\in\partial D(u)\,\,\textnormal{for some $u\in [t_1,t_2]$}\}$.
To obtain information about the Clarke gradient $\partial D(u)$ we apply
Clarke's non-smooth chain rule \cite[Theorem~2.3.9]{clarke_1990} which implies
for $u\in[t_1,t_2]$
\begin{equation}\label{eq:chain-rule}
\textstyle
\partial D(u)\subset\overline{\conv}\big(\big\{\langle\alpha,\zeta\rangle_{\R^n}:
\zeta=\frac{d}{dt}|_{t=u}h_M^+(x,t),\,\alpha\in\partial\big(\dist(
y,M)\big)
{},y=h_M^+(x,u)\big\}\big).
\end{equation}
With \eqref{eq:clarke-gradient} for $y:=h_M^+(x,u)\in H_x\setminus M$ and
$\alpha\in\partial(\dist(y,M))$ we can represent $\alpha$ as a convex combination
(where the number $J_u\in\N$ of summands depends on $u$)
$$
\textstyle
\alpha=\sum_{i=1}^{J_u}\lambda_i\frac{y-z_i}{|y-z_i|},\,\,\,
\lambda_i\in [0,1]\,\,\forall\,
i=1,\ldots,J_u,\,\,\,
\sum_{i=1}^{J_u} \lambda_i=1,
$$
where $z_i\in M$ satisfy $d_y=\dist(y,M)=|y-z_i|$ for all $i=1,\ldots,J_u.$
Consequently, by \eqref{eq:awp} and \eqref{eq:vf} in Proposition \ref{prop:vf}
\begin{align}\label{eq:alpha-times-zeta}
\langle\alpha,\zeta\rangle_{\R^n}&
\textstyle
=\sum_{i=1}^{J_u}\lambda_i\big\langle
\frac{y-z_i}{|y-z_i|},\frac{d}{dt}|_{t=u}h_M^+(x,t)\big\rangle_{\R^n}
\overset{\eqref{eq:awp}}{=}
\sum_{i=1}^{J_u}\lambda_i\big\langle\frac{y-z_i}{|y-z_i|},\tilde{V}(h_M^+(x,u))
\big\rangle_{\R^n}\notag\\
&\textstyle
=\frac12 r_M\varphi(y)\sum_{i=1}^{J_u}\lambda_i\big\langle\frac{y-z_i}{|y-z_i|},
{V}(y)\big\rangle_{\R^n}\overset{\eqref{eq:vf}}{\ge}\frac12 r_M\varphi(y)\ge 0,
\end{align}
if $y=h_M^+(x,u)\in B_{r_M}(M)\setminus M$, which is certainly the case
if $t_2\ll 1$ by continuity of the flow and our initial condition 
$h_M^+(x,0)=x\in B_{\frac12{r_M}}(M)\setminus M$. So, combining \eqref{eq:chain-rule}
with \eqref{eq:alpha-times-zeta} we obtain 
\begin{align}
\partial D(u) & 






 \subset \big[\tfrac12 r_M\varphi(h_M^+(x,u)),\infty\big),\label{eq:clarke-gradient-D}
\end{align}
which inserted into \eqref{eq:mean-value} yields
\begin{align*}
D(t_2)-D(t_1)&\in\conv\Big(\big\{Z\cdot (t_2-t_1):Z\in \big[\textstyle\frac12 r_M\varphi
(h_M^+(x,u)),\infty\big)\quad\textnormal{for some $u\in [t_1,t_2]$}\big\}\Big)\\
& \subset \big[\textstyle\frac12 r_M\min_{u\in [t_1,t_2]}\varphi(h_M^+(x,u))(t_2-t_1),
\infty
\big)\subset [0,\infty).
\end{align*}
Therefore, 
\begin{equation}\label{eq:D-diff}
D(t_2)-D(t_1)\ge \frac12 r_M\min_{u\in [t_1,t_2]}\varphi(h_M^+(x,u))(t_2-t_1)
\ge 0\qquad
\Foa 0<t_1<t_2<1,
\end{equation}
as long as $h_M^+(x,[0,t_2])\subset B_{r_M}(M)\setminus M$. 
This means that the distance $D(t)=\dist(h_M^+(x,t),M)$ is non-decreasing as long
as $h_M^+(x,t)\in B_{r_M}(M)\setminus M$, and as soon as
$D(t)=\frac12{r_M}$ it remains constant by means of the already established
property 
(3+) and uniqueness of the solution to \eqref{eq:awp}, 
so that $D(t_2)-D(t_1)\ge 0$ for all $0\le t_1<t_2\le 1$
by continuity of $D$.

In order to settle claim (2+) it suffices to assume that the starting point
$h_M^+(x,0)=x$ is contained in $B_{\frac12{r_M}}(M)\setminus M$ because of (3+).
We have to show that $D(1)=\dist(h_M^+(x,1),M)\ge\frac12{r_M}-\rho$.
If $D(t)\ge \frac12{r_M}-\rho$ for some $t\in [0,1)$ then $D(1)\ge D(t)\ge
\frac12{r_M}-\rho$ since $D(\cdot)$ was just shown to be non-decreasing
on $[0,1]$. If, on the other hand, $D(s)<\frac12{r_M}-\rho$ for all $s\in [0,1)$ then
by definition \eqref{eq:varphi} of $\varphi$ one has $\varphi(h_M^+(x,s))=1$
for all $s\in [0,1)$ (even for $s=1$ by continuity of $\varphi\circ h_M^+(x,\cdot)$),
and we can apply \eqref{eq:D-diff} to all $0<t_1<t_2<1$, for example
for $t_1:=\sigma$ and $t_2:=1-\sigma$ for any $\sigma\in (0,\frac12).$
Hence,
$$
\textstyle
D(1-\sigma)\overset{\eqref{eq:D-diff}}{\ge} D(\sigma)+\frac12 r_M(1-2\sigma),
$$
from which we deduce $D(1)\ge D(0)+\frac12 r_M>\frac12 r_M-\rho$ also in this
case, by sending $\sigma$ to zero.
\end{proof}
For future reference we draw the immediate conclusion, that having reached 
a certain
distance
from the set $M$ at time $t=1$ according to property (2+) of Theorem~
\ref{thm:dist-inc-flow}, means that we have also moved away from sets $A$
close to $M$
with respect to the Hausdorff distance $\dist_{\HH}$.
More precisely, we can state then following assertion.
\begin{corollary}[Complements of nearby sets under $h_M^+$]\label{cor:nearby-sets}
Let $M\subset\R^n$ be a non-empty, closed and path-connected set with
$\delta(M,r_M)<g_n$ at some scale $r_M>0$, and suppose a set $A\subset\R^n$ 
satisfies
\begin{equation}\label{eq:nearby-sets}
\dist_{\HH}(M,A)<\frac12{r_M} -\rho\quad\textnormal{for some $\rho\in (0,
\frac12{r_M}).$}
\end{equation}
Then the image of the function $h_M^+(\cdot,1)$ 
in Theorem~\ref{thm:dist-inc-flow} for this
$\rho$ satisfies the inclusion
\begin{equation}\label{eq:nearby-complements}
h_M^+(\R^n\setminus M,1)\subset\R^n\setminus A.
\end{equation}
\end{corollary}
\begin{proof}
Property (2+) in Theorem~\ref{thm:dist-inc-flow} implies by means of 
\eqref{eq:nearby-sets} for all $x\in\R^n\setminus M$
\[
\textstyle
\dist(h_M^+(x,1),A)\ge\dist(h_M^+(x,1),M)-\dist_{\HH}(M,A)\overset{\textnormal{(2+)}}{
\ge}\frac12{r_M} -\rho-\dist_{\HH}(M,A)\overset{\eqref{eq:nearby-sets}}{>} 0.\qedhere
\]
\end{proof}
In a similar fashion we can flow \emph{towards} $M$.
\begin{theorem}[Distance-decreasing flow]\label{thm:dist-dec-flow}
If $M\subset\R^n$ satisfies the assumptions of Theorem~\ref{thm:dist-inc-flow},
then for every $0<\rho <\delta < r_M$ there is a function $h_{M,\rho,\delta}^-
\equiv h_M^-\in C^\infty (\R^n\setminus M\times [0,1],\R^n)$ with 
$h_M^-(\R^n\setminus M\times [0,1])\subset\R^n\setminus M$ such that
\begin{enumerate}
\item[\rm (1-)] $h_M^-(\cdot,0)=\Id_{\R^n\setminus M},$
\item[\rm (2-)] $h_M^-(B_\delta(M)\setminus M,1)\subset B_{\rho}(M)\setminus M$,
\item[\rm (3-)] $h_M^-(\cdot,t)|_{(B_{\frac12{\rho}}(M)\setminus M)\cup(\R^n\setminus B_{r_M}(M))}=
\Id_{(B_{\frac12{\rho}}(M)\setminus M)\cup(\R^n\setminus B_{r_M}(M))}$
 for all $t\in [0,1]$.
\end{enumerate}
Moreover, the map $h_M^-(\cdot,t):\R^n\setminus M\to\R^n$ is an
embedding for every $t\in [0,1]$, and the function $t\mapsto\dist(h_M^-(x,t),M)$
is non-increasing on $[0,1]$ for each $x\in\R^n\setminus M$.
\end{theorem}
\begin{proof}
Choose a cut-off function $\psi\in C^\infty(\R^n)$ with $\psi\ge 0$ on
$\R^n$, $\psi\equiv 0$ on $B_{\frac12{\rho}}(M)\cup(\R^n\setminus B_{r_M}(M))$,
and $\psi\equiv 1$ on $B_\delta(M)\setminus B_\rho(M)$. We take the unique
smooth solution $h\in C^\infty((\R^n\setminus M)\times \R,\R^n)$ of 
\eqref{eq:awp} with the vector field $\tilde{V}$ replaced by $\tilde{W}:=-r_M\psi\cdot
V$, where $V\in C^\infty(\R^n,\R^n)$ is the vector field constructed in
Proposition \ref{prop:vf}. Define $h_M^-\in C^\infty(\R^n\setminus M\times [0,1],
\R^n)$ as the restriction of $h$ to the interval $[0,1]$. Again (1-) immediately
follows from the initial condition in \eqref{eq:awp}, and uniqueness of the solution
implies that $h_M^-(\cdot,t):\R^n\setminus M\to\R^n$ is an embedding for each 
$t\in [0,1]$. Property (3-) follows from the fact that $\psi$ vanishes on
$B_{\frac12{\rho}}(M)\cup(\R^n\setminus B_{r_M}(M))$ since the constant function 
$t\mapsto h_M^-(x,t):=x$ is the unique solution to \eqref{eq:awp} on regions
where the right-hand side of \eqref{eq:awp} vanishes. This already implies that
$h_M^-(\R^n\setminus M\times [0,1])\subset\R^n\setminus M.$

To show that $D(t):=\dist(h_M^-(x,t),M)$ is non-increasing on $[0,1]$ it suffices
to consider $x\in B_{r_M}(M)\setminus B_{\frac12{\rho}}(M)$ since for all other
$x\in\R^n\setminus M$ the distance $D(t)$ is constant on $[0,1]$ by virtue
of the already established property (3-). The characterization 
\eqref{eq:clarke-gradient}
of the Clarke gradient 
$\partial (\dist(y,M))$ for $y\in h_M^-(x,[0,1])\setminus M$
continues to hold true, as well as the vectorial mean-value inclusion 
\eqref{eq:mean-value} for $0<t_1<t_2<1$, and the inclusion \eqref{eq:chain-rule}
for $\partial D(u)$, $u\in [t_1,t_2]$. For $y:=h_M^-(x,u)\in h_M^-(x,[0,1])\setminus
M$ we use \eqref{eq:clarke-gradient} and the differential equation
\eqref{eq:awp} with $\tilde{W}$ instead of $\tilde{V}$ to conclude by means of
\eqref{eq:vf} for
$\alpha\in\partial\dist(y,M))$ and $\zeta=\frac{d}{dt}|_{t=u}h_M^-(x,t),$
\begin{align*}
\langle\alpha,\zeta\rangle_{\R^n}&
\textstyle
=\sum_{i=1}^{J_u}\lambda_i\big\langle
\frac{y-z_i}{|y-z_i|},\tilde{W}(y)\big\rangle_{\R^n}
 = -r_M\psi(y)\sum_{i=1}^{J_u}\lambda_i\big\langle
\frac{y-z_i}{|y-z_i|},V(y)\big\rangle_{\R^n}\le -r_M\psi(y)
\end{align*}
where $\lambda_i\in [0,1]$, $\sum_{i=1}^{J_u}
\lambda_i=1$, $z_i\in M$ such that $d_y=\dist(y,M)=|y-z_i|$
for all $i=1,\ldots,J_u$,
if $y=h_M^-(x,u)\in B_{r_M}(M)\setminus M$, which holds true for sufficiently
small $t_2\in (0,1)$ by continuity. So, we obtain for such $t_2$ and $u\in [t_1,t_2]$
\begin{align*}
\partial D(u)







& \subset \big(-\infty,-r_M\psi(h_M^-(x,u))\big].
\end{align*}
Inserting  this into \eqref{eq:mean-value} yields
\begin{equation}\label{eq:Dmonotone}
D(t_2)\le D(t_1)-r_M\min_{u\in [t_1,t_2]}\psi(h_M^-(x,u))(t_2-t_1)\le D(t_1)
\end{equation}
for all $0<t_1<t_2<1$ 
subject to $h_M^-(x,[0,t_2])\subset B_{r_M}(M)\setminus M$,
which proves that $D(\cdot)$ is non-increasing as long as the flow remains
in $B_{r_M}(M)\setminus M$. But as soon as 
$D(\cdot)$ reaches the value $\frac{\rho}2$
it


remains constant due to (3-) and uniqueness of the flow.

To finally establish (2-) we may
assume that 
\begin{equation}\label{eq:contraD}
\delta>D(0)\ge D(s)\ge\rho\quad\Foa
s\in [0,1),
\end{equation}
since if $D(s)<\rho$ for
some $s\in [0,1)$, then by the monotonicity we just proved we find $D(1)<\rho$ as well,
which settles (2-).
So, with \eqref{eq:contraD}
we are in the situation that we can apply \eqref{eq:Dmonotone}
for all $0<t_1<t_2<1$ and that $\psi(h_M^-(x,s))= 1$ for all $s\in [0,1)$.
Consequently, by \eqref{eq:Dmonotone} for $t_1:=\sigma,$ $t_2:=1-\sigma$, $\sigma\in (0,\frac12)$ we find $D(1-\sigma)\le D(\sigma)-r_M(1-2\sigma).$ Upon $\sigma\to 0$ we obtain
by continuity and \eqref{eq:contraD} the inequality
$
0\le D(1)\le D(0)-r_M <\delta-r_M<0$, a contradiction, so that the situation 
\eqref{eq:contraD}  can never occur.
\end{proof}
