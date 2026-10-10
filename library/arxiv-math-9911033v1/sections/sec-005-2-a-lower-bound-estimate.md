---
doc_id: arxiv-math-9911033v1
doc_title: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface"
section_id: sec-005-2-a-lower-bound-estimate
section_title: "A lower bound estimate"
section_number: 2
pages: 4-7
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
text_source: latex
latex_prose_ratio: 0.68
latex_coverage_ratio: 0.975
doc_brief: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface — 18 sections: Introductions 1; A lower bound estimate 4; A counterexample 11"
---
Suppose that $M$ is a Riemann surface of genus $g\geq 2$.
Let $K_M$ be the canonical line  bundle over $M$ with the Hermitian
metric $H$. We assume that the curvature $\omega_g$ of $H$ is positive
and $\omega_g$ defines a K\"ahler metric of $M$.

 Let $K$ be
the Gauss curvature of the metric $\omega_g$. Let $K_1$ and $K_2$ be two
nonnegative
constants such that
\begin{equation}\label{kbd}
-K_1\leq K\leq K_2.
\end{equation}
Let $\delta'$ be the injective radius of $M$ with  and
\begin{equation}\label{delta}
\delta=\min(\delta',\frac{1}{\sqrt{K_1+K_2}}).
\end{equation}
 Let $x_0\in M$ be a
fixed
point. Let $U$ be the open set 
\[
U=\{dist(x,x_0)<\delta\}. 
\]
It is well known that at each point of $U$ there is an isothermal
coordinate. 
In the first part of this section,
we prove that there is a holomorphic
function $z$ on $U$ which gives the isothermal coordinate of $U$ with 
the \textsl{required} estimate.

Consider the equation
\begin{equation}\label{defh}
\left\{
\begin{array}{l}
\Delta h=K/2\\
h|_{\pa U}=0,
\end{array}
\right.
\end{equation}
where $\Delta$ is the (complex) Laplacian of $M$. The solution $h$ exists
and is
unique.
Let $ds^2$ be the Riemann metric of $U$. Then we have

\begin{lemma}\label{lem21}
The metric $e^h ds^2$ on $U$ is a flat metric.
\end{lemma}

{\bf Proof.} A straightforward computation using~\eqref{defh}.


\qed

Since $U$ is an open set which is differmorphic to an open set in the
Euclidean plane, we can assume that there are global frames on $U$.
Let $\omega^1$ and $\omega^2$ be 1-forms on $U$ such that 
\[
e^hds^2=\omega_1^2+\omega_2^2.
\]
Let $\omega_{12}$ be the connection 1-form defined by
\begin{equation}\label{stru}
\begin{array}{l}
d\omega_1=\omega_{12}\wedge\omega_2,\\
d\omega_2=-\omega_{12}
\wedge\omega_1.
\end{array}
\end{equation}
Then by Lemma~\ref{lem21}, $d\omega_{12}=0$.
It follows that there is a  real smooth function $\sigma$ on $U$ such that
\begin{equation}\label{conn}
\omega_{12}=d\sigma.
\end{equation}
Let 
\[
\xi=e^{i\sigma}(\omega_1+i\omega_2).
\]
Then by~\eqref{stru} and ~\eqref{conn}, we have
\[
d\xi=0.
\]
Thus  there is a function $z$ on $U$ such that
\[
\xi=dz,
\]
and 
\begin{equation}\label{flat}
e^hds^2=dzd\bar z.
\end{equation}
Either $z$ or $\bar
z$ will be holomorphic because it defines a conformal structure of $U$.
Without losing generality, we assume that $z$ is holomorphic
and at $x_0$, $z=0$.

We have the following lemma:

\begin{lemma}\label{esti}
 Let $\rho$ be the distance to the point
$x_0$. $\rho(x)=dist(x,x_0)$. Then
\begin{equation}\label{27}
\frac 13\rho\leq |z|\leq 3\rho 
\end{equation}
for $\rho<\delta$.
\end{lemma}

{\bf Proof.} By the Gauss Lemma~\cite[page 8]{CE}, the Riemann metric
$ds^2$ can be
written as
\[
ds^2=d\rho^2+f^2(\rho,\theta)d\theta^2
\]
for the polar coordinate $(\rho,\theta)$
where $f(\rho,\theta)$ is a smooth function satisfying
\[
f(0,\theta)=0, \frac{\pa f}{\pa\rho}(0,\theta)=1,
\]
and 
\[
\frac{\pa^2 f}{\pa\rho^2}=-Kf.
\]
By the Hessian comparison theorem~\cite[page 4]{SY}, we have
\[
\Delta\rho\geq\frac{\sqrt{K_2}}{4}\cot\sqrt{K_2}\rho.
\]
In particular, $\Delta\rho\geq 0$ on $U$.
Noting that $\Delta$ is the complex Laplacian, we have 
\begin{equation}\label{dist}
\Delta\rho^2=\frac 12|\nabla\rho |^2+2\rho\Delta\rho\geq \frac 12.
\end{equation}

By ~\eqref{dist}, we have
\[
\begin{array}{l}
\Delta(h+K_1\rho^2)\geq K/2+K_1/2\geq 0,\\
\Delta(h-K_2\rho^2)\leq K/2-K_2/2\leq 0.
\end{array}
\]
By the maximal principle, we have
\begin{equation}\label{h}
-1\leq -K_2\delta^2\leq h|_{\pa U}-K_2\rho^2\leq h\leq
h|_{\pa U}+K_1\rho^2\leq K_1\delta^2
\leq 1.
\end{equation}
Let $ds_1^2=e^h ds^2$ denotes the flat metric. Then
\[
e^{-1} ds^2\leq ds_1^2\leq e ds^2.
\]
By~\eqref{flat}, $|z|$ is the distance to the point $x_0$
with respect to the metric $ds_1^2$.
Thus by~\eqref{h},
\[
\frac 13\rho\leq e^{-1}\rho\leq |z|\leq e\rho
\leq 3\rho.
\]

\qed

{\bf Proof of Theorem~\ref{main}.}
Define a smooth function $\eta: \R^+\rightarrow\R$ such that
\begin{equation}\label{eta}
\eta(t)=\left\{
\begin{array}{ll}
0 & t\geq 1,\\
1 & 0\leq t\leq \frac 12.
\end{array}
\right.
\end{equation}
We assume that 
$|\eta'|\leq 4$ and $|\eta''|\leq 4$.

In the rest of this paper $C_1, C_2,\cdots,$ are absolute constants, 
unless otherwise stated.


Let
$\delta_1=\frac 14\delta$.
Define the smooth  function $r$ on $M$ such that 
\begin{equation}\label{deff}
r=\left\{
\begin{array}{ll}
\eta(\frac{|z|}{\delta_1})\log (\frac{|z|}{\delta_1}) &
x\in U,\\
0 & x\notin U.
\end{array}
\right.
\end{equation}
$r$ is well defined.  
For if $x\in\pa U$, then $\rho=\delta$. By the Lemma~\ref{esti},
$|z|\geq\frac 43 \delta_1$ and thus $r|_{\pa U}=0$ using either
expression.


Note that if $z\neq 0$, then $\Delta\log (|z|)=0$. Define the
function
$\psi$ such that $\psi=\Delta r$ for $z\neq 0$ and $\psi=0$ for 
$z=0$. We have

\begin{lemma}\label{lem23}
There is a constant $C_1>0$ such that
\begin{equation}\label{esti2}
\left\{
\begin{array}{l}
|\psi|\leq \frac{C_1}{\delta^2},\\
\int_M|\psi|\leq C_1.
\end{array}
\right.
\end{equation}
\end{lemma}

{\bf Proof.}
A straightforward computation gives
\begin{equation}\label{psi}
\psi=\Delta r=\frac 14 e^h(\frac{1}{\delta_1^2}\eta''\log(
\frac{|z|}{\delta_1})+\eta'\frac{1}{\delta_1|z|}\log(
\frac{|z|}{\delta_1})+2\eta'\frac{1}{\delta_1|z|})
\end{equation}
for $\frac{\delta_1}{2}<z<\delta_1$. Using~\eqref{h},~\eqref{eta},
we have the estimate
\[
|\psi|\leq \frac{C_2}{\delta^2}
\]
for some constant $C_2$.
To get the estimate of the $\int_M|\psi|$, we first see that by the 
volume comparison theorem~\cite[page 11]{SY}, 
\[
vol(U)\leq2\pi(\frac{\cosh \sqrt{K_1}\delta-1}{K_1}).
\]
Since $\sqrt{K_1}\delta\leq 1$, there is a constant $C_3$
such that
\begin{equation}\label{vol}
vol(U)\leq C_3\delta^2.
\end{equation}
The lemma follows by setting $C_1=\max(C_2, C_2C_3)$.

\qed

Let $G(x,y)$ be the Green's function of $M$. That is,
\[
\left\{
\begin{array}{l}
\Delta_x G(x,y)=\frac 14({-\delta_x(y)+\frac{1}{vol(M)}}),\\
\int_M G(x,y) dx=0,
\end{array}
\right.
\]
where $\Delta_x$ is the (complex) Laplacian with respect to $x$
and $\delta_x(\cdot)$ is the Dirac function.
Let $b$ be the function on $M$ such that
\[
\left\{
\begin{array}{l}
\Delta b=K/4+1/2,\\
\int_M b=0.
\end{array}
\right.
\]
Since the K\"ahler metric $\omega_g\in -c_1(M)$, the above 
equation
 has a
unique solution.


Let the function $a: M\rightarrow\R$ defined by
\begin{equation}\label{xxa}
a=G(x,x_0)+\frac{1}{2\pi}(r-\frac{1}{vol(M)}\int_Mr)+b,
\end{equation}
where $x_0$ is the fixed point of $M$ and $r$ is defined in
~\eqref{psi}. Then $a$ is a smooth function on $M$.
We have
\begin{equation}\label{defa}
\left\{
\begin{array}{l}
\Delta a=\frac{1}{4vol(M)}+\frac{1}{2\pi}\psi+K/4+1/2,\\
\int_M a=0.
\end{array}
\right.
\end{equation}





\begin{lemma}\label{lema}
There is a constant $C_5$ such that
\[
|a|\leq\frac{C_5g^3}{\delta^6},
\]
where $g$ is the genus of the Riemann surface $M$.
\end{lemma}

{\bf Proof.} Let $\lambda_1$ be the first eigenvalue of $M$, then 
by the Poincare inequality,
we have
\begin{equation}\label{lambda}
\lambda_1\int_M a^2\leq\int_M|\nabla a|^2.
\end{equation}
Integration by parts using~\eqref{defa}, we have
\begin{equation}\label{nabla}
\int_M|\nabla a|^2\leq\int_M |a(\frac{1}{2\pi}\psi+\frac{1}{4vol(M)}
+\frac{
K_1+K_2}{4}+\frac 12)|.
\end{equation}
Let $g$ be the genus of $M$.
By the Gauss-Bonnet Theorem, $vol(M)=4\pi(g-1)$. On the other hand,
$K_1+K_2\leq\frac{1}{\delta^2}$. Let $a(x')=\max |a|$.
By~\eqref{lambda}, ~\eqref{nabla} and Lemma~\ref{lem23},
\begin{equation}\label{aest}
\int_M a^2\leq\frac{(C_1+6\pi)g}{\lambda_1\delta^2}a(x').
\end{equation}
Consider a neighborhood $U'$ of $x'$ defined by 
\[
U'=\{ x| dist (x,x')	<\delta\}.
\]
Let $z$ be the holomorphic function in Lemma~\ref{esti} such that
$z(x')=0$. Let
\[
U_1=\{|z|<\frac 13\delta\}.
\]
Let $\tilde\Delta=\frac{\pa^2}{\pa z\pa\bar z}$ be the Euclidean Laplacian
on $U_1$. Then by~\eqref{h}, ~\eqref{esti2} and~\eqref{defa}, we have
\begin{equation}
|\tilde\Delta a|\leq 3(2+\frac{C_1+1}{\delta^2}).
\end{equation}
It follows from an elementary fact that there is a constant $C_4$
such that
\begin{equation}\label{aest1}
a(x')\leq C_4(\log\frac 1\delta
+\frac{1}{\delta}
(\int_{U_1} a^2(x))^{\frac 12}).
\end{equation}
On the other hand, Cheeger's inequality~\cite[page 91]{SY} gives
\begin{equation}\label{chee}
\lambda_1\geq\frac{1}{4g^2}\delta^2.
\end{equation}
Combining~\eqref{aest},
~\eqref{aest1} and ~\eqref{chee}, we have the
required estimate.

\qed



Let 
\begin{equation}\label{phi1}
\phi=-4\pi(G(x,x_0)+b).
\end{equation}
Then for $x\neq x_0$, we have
\begin{equation}\label{pine}
\frac{\sqrt{-1}}{2\pi}\pa\bar\pa\phi\geq
(-\frac{1}{2vol(M)}-\frac K2-1)\omega_g.
\end{equation}

\begin{lemma}\label{lem25}
There is a constant $C_6$ such that
\[
\phi\leq\frac{C_6g^{3}}{\delta^6},
\]
and for $|z|\leq\delta_1$,
\[
\phi\geq-\frac{C_6g^{3}}{\delta^{6}}+2\log |z|.
\]
\end{lemma}

{\bf Proof.}
By~\eqref{xxa}, 
\[
\phi=-4\pi(a-\frac{1}{2\pi}(r-\frac{1}{vol(M)}\int_M r))
\]
The lemma follows from Lemma
~\ref{lema} and~\eqref{deff}.

\qed






We need the following proposition from Demailly (see~\cite{T5}):

\begin{prop}\label{del}
Suppose that $(M,g)$ is a complete K\"ahler manifold of complex dimension
$n$, $L$ is a line bundle on $M$ with the Hermitian metric $h$,and
$\phi$ is a function on $M$, which can be approximated by a decreasing
sequence of smooth functions
$\{\phi_l\}_{1\leq l<+\infty}$. If
\[
<\pa\bar\pa\phi_l+\frac{2\pi}{\sqrt{-1}}(Ric(h)+Ric(g)),v\wedge\bar v>_g
\geq C||v||_g^2
\]
for any tangent vector $v$ of type $(1,0)$ at any point of $M$
and for each $l$, where $C>0$ is a constant independent of $l$, 
and $<\cdot ,\cdot >_g$ is the inner product induced by $g$, then 
for any $C^\infty$ $L$-valued $(0,1)$-form $u_1$ on $M$ with
$\bar\pa u_1=0$ and $\int_M||u_1||^2e^{-\phi} dV_g$ finite, there 
exists a $C^\infty$ $L$-valued function $u$ on $M$ such that
$\bar\pa u=u_1$ and
\[
\int_M||u||^2 e^{-\phi} dV_g\leq\frac 1C\int_M||u_1||^2
e^{-\phi} dV_g,
\]
where $dV_g$ is the volume form $g$ and the norm $||\cdot||$ is
induced by $h$. The function $\phi$ is called the weight function.
\end{prop}

\qed

Let $L=K_M^m$ for $m\geq 2$. $H^m$ gives the positive Hermitian
metric on $K_M^m$. Let $\omega_g$ be the K\"ahler
form defined by the curvature of $H$ on $K_M$.
Let $\phi_l=\max(\phi,-l)$ for $l\in\Z^+$, where $\phi$ is defined in
~\eqref
{phi1}. Then by ~\eqref{pine}, we have

\begin{equation}\label{low}
<\pa\bar\pa\phi_l+\frac{2\pi}{\sqrt{-1}}(Ric(H)+Ric(\omega_g)),
v\wedge\bar v>\geq
(m-1-\frac{1}{2vol(M)})||v||^2.
\end{equation}


In order to prove Theorem~\ref{main}, we need to proved that 
for any $m\geq 2$ and $x_0\in M$, there is a section
$S\in H^0(M,K_M^m)$ such that
\[
||S||^2(x_0)/||S||^2_{L^2}\geq e^{-\frac{Cg^{3}}{\delta^6}}.
\]
We will use Proposition~\ref{del} to construct such a section.

Let $e^p$ be the local representation of the metric $H$. That is,
\[
-\frac{\sqrt{-1}}{2\pi}\pa\bar\pa p=\omega_g.
\]





Let 
\[
u_1=\bar\pa\rho(\frac{\sqrt m|z|}{\delta})
e^{-m\frac{\pa p}{\pa\bar z}(x_0)\cdot z} (dz)^m.
\] 
Then $u_1\in \Gamma(M,K_M^m)$. By~\eqref{flat},~\eqref{27}
and~\eqref{eta},
we have
\begin{equation}\label{u-1}
||u_1||^2\leq\frac{12m}{\delta^2}e^{m(p-2 Re\frac{\pa p}{\pa\bar z}
(x_0)z)}
\end{equation}
for $\frac{\delta}{2\sqrt{m}}\leq |z|\leq\frac{\delta}{\sqrt m}$. 
Let 
$U_1=\{x||z|<\frac 13\delta\}$.
Let $\tilde\Delta$ be the Euclidean Laplacian, by
~\eqref{h}, we see
that
\[
|\tilde\Delta p|\leq 3
\]
on $U_1$.
Using the Possion formula we see that there is a constant $C_7$ such that
\[
|\tilde\nabla^2 p(z)|\leq\frac{C_7}{\delta^2}
\]
for $|z|\leq\frac 12\delta$. Thus
\[
|p-2 Re\frac{\pa p}{\pa\bar z}(x_0) z
-p(x_0)|\leq\frac{C_7}{m}
\]
for $|z|<\frac{\delta}{m}$.
Using this estimate and ~\eqref{u-1}, we have
\[
||u_1||^2\leq\frac{12m}{\delta^2} e^{C_7} e^{mp(x_0)}
\]
for $\frac{\delta}{2\sqrt{m}}\leq |z|\leq\frac{\delta}{\sqrt m}$.
Thus by Lemma ~\ref{lem25} and~\eqref{vol},
\[
\int_M||u_1||^2 e^{-\phi}=\int_{\frac{\delta}{2\sqrt m}\leq |z|
\leq\frac{\delta}{\sqrt m}}||u_1||^2 e^{-\phi}
\leq \frac{48C_3 m}{\delta^2}
e^{C_7}
 e^{\frac{C_6g^{3}}{\delta^6}}
e^{m p(x_0)}.
\]

By Proposition~\ref{del} and ~\eqref{low}, there is a
$u\in\Gamma(M,K_M^m)$ such that
$\bar \pa u=u_1$ and,
\[
\int_M||u||^2 e^{-\phi}\leq\frac{1}{m-1-\frac{1}{2vol(M)}}
\int_M||u_1||^2 e^{-\phi}.
\]
Using Lemma~\ref{lem25} again, for $m\geq 2$, there is a $C_8$
such that
\begin{equation}\label{ue}
\int_M||u||^2\leq\
\frac{C_8}{\delta^2} e^{\frac{2C_6 g^{3}}{\delta^6}}
e^{mp(x_0)}.
\end{equation}

On the other hand, we have
\begin{equation}\label{pe}
\int_M||\rho(\frac{m|z|}{\delta}) 
e^{-m\frac{\pa p}{\pa\bar z_0}(x_0)z}
(dz)^m||^2
\leq e^{C_7}\int_{|z|\leq\frac{\delta}{\sqrt m}} e^{mp(x_0)}
\leq e^{mp(x_0)} C_3 e^{C_7}\frac{\delta^2}{m}.
\end{equation}

Let $S=\rho(\frac{|z|}{\delta_1})
e^{-m\frac{\pa p}{\pa\bar z}(x_0)z}
(dz)^m-u$. Then $\bar\pa S=0$.
Since
$\int_Me^{-\phi}=+\infty$, $u(x_0)=0$. In particular, $S\neq 0$. 
Using~\eqref{ue},~\eqref{pe}, we have
\[
||S||^2(x_0)/||S||^2_{L^2}\geq
1/\left (
2C_3e^{C_7}\frac{\delta^2}{m}+
2\frac{C_8}{\delta^2}e^{\frac{2C_6g^{3}}{\delta^6}}
\right)
\]
Thus for $m\geq 2$, there is
a $C$ such that
\[
||S||/||S||_{L^2}\geq e^{-\frac{Cg^3}{\delta^6}}.
\]
This completes the proof of Theorem~\ref{main}.
