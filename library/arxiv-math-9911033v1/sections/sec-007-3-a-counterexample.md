---
doc_id: arxiv-math-9911033v1
doc_title: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface"
section_id: sec-007-3-a-counterexample
section_title: "A counterexample"
section_number: 3
pages: 11-12
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
text_source: latex
latex_prose_ratio: 0.705
latex_coverage_ratio: 0.984
doc_brief: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface — 18 sections: Introductions 1; A lower bound estimate 4; A counterexample 11"
---
\label{sec3}

In the last section, we give a lower bound estimate of~\eqref{quan}
in terms of the injective radius of $M$.
In this section, we  give a counterexample that the 
uniform estimate is not true. More precisely, we are going to
disapprove the following:

{\bf Conjecture.} Let $K_M$ be the canonical line bundle of  a Riemann
surface $M$ of genus $g\geq 2$ and constant Gauss curvature $(-1)$. Then
for $m$ sufficiently large, there is a number $C(m,g)>0$,
depending only on $m$ and  $g$,
 such that for
any
orthonormal basis $S_1,\cdots,S_d$ of $H^0(M,K_M^m)$, we have
\[
\inf \sum_{i=1}^d||S_i||^2\geq C(m,g).
\]
In order to give the counterexample,
we use the following Collar Theorem of Keen~\cite[p264]{Keen}:

\begin{theorem}[Keen]\label{keen}
Consider the region $T$ of $U$, the upper half plane, bounded
by the curve $r=1$, $r=e^l$, $\theta=\theta_0$ and $\theta=\pi-\theta_0$.
Let
$\gamma$ be a closed geodesic on $M$ with length $l$. Then there is a
conformal
isometric mapping $\phi: T\rightarrow M$ such that $\phi(iy)=\gamma$.
The image $\phi(T)$ of $T$ is called a collar.
Then we can choose $\theta_0$ small enough such that
the area of the Collar is at least $\frac{8}{\sqrt 5}$.
\end{theorem}




The following theorem
gives the counterexample and implies Theorem~\ref{second}:




\begin{theorem}\label{counterexample} 
For any $\eps>0$ and $m\geq 2$, there is a Riemann surface $M$ of
constant curvature $(-1)$ and genus $g\geq 2$ such that there is a point
$x_0\in M$ satisfying
\[
||S||(x_0)\leq\eps
\]
for any $S\in H^0(M,K_M^m)$ with $||S||_{L^2}=1$.
\end{theorem}

The idea of the proof is that when the length of a closed geodesic 
line tends to zero, the collar will be longer and longer in order
to keep the area of the collar having a lower bound. Topologically,
a collar is a cylinder. By expanding the functions on the corollary using
the Fourier series, we can find the suitable $x_0$ and the estimates. 
We begin by discussing some elementary properties of a collar.




Let $R>0$ be a large real number. Let $(\rho, \theta)
\in (-R,R)\times\R$.
Let the group $\Z$ acting on the space $(-R,R)\times\R$ by
\[
(n,\rho,\theta)\mapsto(\rho,\theta+n\delta)
\]
for $n\in\Z$,
where $\delta>0$ satisfies
\[
\delta\sinh R=\eps_1(=\frac{8}{\sqrt{5}}).
\]
as in Theorem~\ref{keen}.
Define the metric 
\[
ds^2=d\rho^2+(\cosh\rho)^2 d\theta^2
\]
on $(-R,R)\times\R$ which descends to a metric on 
\[
C=(-R,R)\times\R/\Z.
\]
The curvature of the metric is $(-1)$. Note that on $C$, $\rho$ is a
global function but $\theta$ is only locally defined.

We call $C$  a collar
of parameter $\delta$.


Let
\begin{equation}\label{z1}
\left\{
\begin{array}{l}
x=\theta\\
y=2\arctan e^\rho-\frac\pi 2.
\end{array}
\right.
\end{equation}
Define $z=x+iy$. Clearly $z$ is not a global function of $C$. But it 
defines a complex structure of $C$.

Let 
\begin{equation}\label{w1}
w=e^{\frac{2\pi i}{\delta}(\theta+2i(\arctan e^\rho-\frac\pi 4))}
=e^{\frac{2\pi i}{\delta}z}.
\end{equation}
Then $w$ is a global holomorphic function on $C$. Consequently
\begin{equation}\label{dz}
dz=\frac{\delta}{2\pi i}\frac{dw}{w}
\end{equation}
is a global holomorphic 1-form on $C$.

Let $f$ be a holomorphic function on 
a neighborhood of
$\bar C$. Then $f$ is a period
function on $[-R,R]\times\R$, satisfying
\[
f(\rho,\theta\pm\delta)=f(\rho,\theta).
\]

Let the Fourier expansion of $f(-R,\theta)$ and $f(R,\theta)$ be
\begin{align*}
& f(-R,\theta)=\sum_{k=-\infty}^{+\infty} A_ke^{\frac{2\pi
i}{\delta}k\theta};\\
&f(R,\theta)=\sum_{k=-\infty}^{+\infty}B_k
e^{\frac{2\pi i}{\delta}k\theta}.
\end{align*}
Define
\begin{align}\label{g}
\begin{split}
&g_1=\sum_{k=1}^\infty A_ke^{-\frac{4\pi}{\delta}k(\frac{\pi}{4}-\arctan
e^{-R})}w^k,\\
& g_2=B_0,\\
&g_3=\sum_{k=-\infty}^{-1}B_k e^{-\frac{4\pi}{\delta}k(\frac\pi 4-
\arctan e^R)} w^k,
\end{split}
\end{align}
where $w$ is in~\eqref{w1}.
We have the following lemma:

\begin{lemma}\label{lem31}
With the notations as above,
$g_1,g_2,g_3$ are holomorphic functions on $C$. Furthermore
\[
f=g_1+g_2+g_3.
\]
\end{lemma}

{\bf Proof.} 
$g_2$ is a constant. So it is automatically holomorphic.
By equation ~\eqref{w1}, we have
\[
|w|\leq e^{-\frac{4\pi}{\delta}(\arctan e^\rho-\frac\pi 4)}.
\]
Thus we have
\begin{align*}
&|g_1|= |\sum_{k=1}^\infty A_ke^{-\frac{4\pi}{\delta}k(
\frac{\pi}{4}-\arctan e^{-R})} w^k|\\
&\leq\sum_{k=1}^\infty |A_k|e^{-\frac{4\pi}{\delta}k
(\arctan e^\rho-\arctan e^{-R})}\\
&\leq(\sum_{k=1}^\infty|A_k|^2)^{\frac 12}
(\sum_{k=1}^\infty e^{-\frac{8\pi}{\delta}k(\arctan e^\rho-\arctan
e^{-R})})^{\frac 12}.
\end{align*}
By the Bessel inequality,
we have
\[
\sum_{k=1}^{+\infty}|A_k|^2\leq
\frac 1\delta\int_M|f(-R,\theta)|^2 d\theta.
\]
Thus
if $\rho>-R$, the series is convergent absolutely.
So $g_1$ defines a holomorphic function on $\{-R<\rho< R\}$.

By the same argument, $g_3$ is also holomorphic.

\qed


In order to prove that 
\[
f=g_1+g_2+g_3,
\]
we just need to prove that on the set $\{\rho=0\}$, $f=g_1+g_2+g_3$.
Define
\begin{equation}\label{pd}
p_k(\rho)=\int_0^\delta f(\rho,\theta)e^{-\frac{2\pi i}{\delta}
\theta k} d\theta
\end{equation}
for $k\in\Z$.
Apparently
\[
p_k(R)=B_k\delta,\qquad p_k(-R)=A_k\delta
\]
for $k\in\Z$.
By the definition of $z$ in~\eqref{z1}, we have
\[
\frac{\pa}{\pa\bar z}=\frac 12
(\sqrt{-1}\cosh\rho\frac{\pa}{\pa\rho}+\frac{\pa}{\pa\theta}).
\]
Using the equation $\frac{\pa f}{\pa\bar z}=0$, from~\eqref{pd},
we have
\[
p_k'=-\frac{2\pi k}{\delta\cosh\rho}p_k.
\]
Solving the above differential equation gives 
\begin{align}\label{p}
\begin{split}
&p_k(0)=A_ke^{-\frac{4\pi}{\delta}k(\frac\pi 4-\arctan e^{-R})},
\qquad  k=1,2,\cdots,\\
& p_0(0)=B_0,\\
& p_k(0)=B_k e^{-\frac{4\pi}{\delta}k(\frac\pi 4-\arctan e^R)},
\qquad k=-1,-2,\cdots.
\end{split}
\end{align}

From ~\eqref{g} and~\eqref{p}, we see that 
\[
f|_{\rho=0}=(g_1+g_2+g_3)|_{\rho=0}.
\]
Thus
\[
f=g_1+g_2+g_3
\]
on $C$
because both sides are holomorphic functions.

\qed


Let $M$ be a Riemann surface of curvature $(-1)$ and genus $g\geq 2$.
Assume that there is a closed geodesic $\gamma$ on $M$ such that
$length(\gamma)=\delta>0$. Assume that $\delta$ is small enough. Let
$\theta$ be the arc length parameter and $\rho$ be the distance function
to the geodesic. Then

\begin{lemma} $(\rho,\theta)$ is the local coordinate system of $M$ as
long
as 
\[
\sinh\rho\cdot\delta\leq\eps_1=\frac{8}{\sqrt{5}}.
\]
\end{lemma}

{\bf Proof.} 
Note that the area of $\{-R_0<\rho<R_0\}$ is $\delta\sinh R_0$
for any $R_0>0$. The lemma follows from Theorem~\ref{keen}.

\qed

Let $C=\{-R<\rho<R\}$, where
$R$ satisfies $\delta\sinh R=\eps_1$.
Then $z=x+iy$
defines a complex structure of $C$
where $x$ and $y$ are in~\eqref{z1}. We have

\begin{lemma}
Either $z=x+iy$ or $z=x-iy$ is holomorphic on $M$.
\end{lemma}

{\bf Proof.}
A straightforward computation gives
\[
ds^2=(\cosh\rho)^2 dz d\bar z.
\]
Thus $z$ defines a conformal structure which is the same as the one on
$M$. So either $z$ or $\bar z$ is holomorphic.

\qed
 
Without losing generality, we assume that $z$ is
holomorphic.
Fixing $m\geq 2$. 
Let $S\in H^0(M,K_M^m)$. We choose an $x_0\in M$ as follows:
let $\rho_0<0$ be the number such that
\[
\delta (\cosh\rho_0)^2=\eps_1.
\]
Then $\rho_0\rightarrow -\infty$, $\rho_0+R\rightarrow +\infty$ as
$\delta\rightarrow 0$.

By~\eqref{dz}, we see that $(dz)^m\in H^0(C,K_M^m)$. Furthermore
$(dz)^m\neq 0$ on $C$. Thus for any $S\in H^0(M,K_M^m)$, there is
a holomorphic function $f$ on $C$ such that
\[
S|_C=f (dz)^m.
\]
Let
\[
f=g_1+g_2+g_3,
\]
where $g_1,g_2,g_3$ are defined in Lemma~\ref{lem31}. Let
\begin{equation}\label{defs}
S_i=g_i (dz)^m,\qquad i=1,2,3.
\end{equation}

























\begin{lemma} With the notations as above, let
$x_0=(\rho_0,0)$. Then
\[
\underset{\delta\rightarrow 0}{\lim}\frac{||S_i||^2(x_0)}
{||S_i||^2_{L^2(C)}}=0
\]
for $i=1,2,3$.
\end{lemma}

{\bf Proof.} By~\eqref{w1}, we have 
\[
w(x_0)=e^{-\frac{4\pi}{\delta}(\arctan e^{\rho_0}-\frac\pi 4)}.
\]
Thus
\begin{align}\label{s1}
\begin{split}
&||S_1||^2(x_0)=\frac{1}{(\cosh\rho_0)^{2m}}
|\sum_{k=1}^\infty A_ke^{-\frac{4\pi}{\delta}k(\arctan e^{\rho_0}
-\arctan e^{-R})+\frac{2\pi i}{\delta}k\theta}|^2\\
&\leq
\frac{1}{(\cosh\rho_0)^{2m}}
\sum_{k=1}^\infty |A_k|^2e^{-\frac{8\pi}{\delta}k(\arctan
e^{\rho_0-1}
-\arctan e^{-R})}\\
\qquad\qquad\qquad
&\cdot
\sum_{k=1}^\infty e^{-\frac{8\pi}{\delta}k(\arctan e^{\rho_0}-\arctan 
e^{\rho_0-1})}\\
&\leq\sum_{k=1}^\infty|A_k|^2e^{-\frac{8\pi}{\delta}k
(\arctan e^{\rho_0-1}-\arctan e^{-R})}\cdot
\sum_{k=1}^{\infty}e^{-\frac{4\pi k}{\delta\cosh(\rho_0-1)}}.
\end{split}
\end{align}
We assume that $\delta$ is so small that
\[
\frac{4\pi}{\delta\cosh(\rho_0-1)}\geq\frac{\mu}{\sqrt{\delta}}>0,
\]
where $\mu$ is an absolute constant. In addition, assume that
$e^{-\frac{\mu}{\sqrt{\delta}}}<\frac 12$. Then

\begin{equation}\label{s1-1}
\sum_{k=1}^\infty e^{-\frac{4\pi k}{\delta\cosh(\rho_0-1)}}
\leq\sum_{k=1}^\infty e^{-\frac{\mu k}{\sqrt{\delta}}}
\leq 2e^{-\frac{\mu}{\sqrt{\delta}}}.
\end{equation}
On the other hand
\[
||S_1||^2_{L^2(C)}=\delta\int_{-R}^R\frac{1}{
(\cosh\rho)^{2m-1}}\sum_{k=1}^\infty |A_k|^2 e^{-\frac{8\pi k}
{\delta} (\arctan e^\rho-\arctan e^{-R})} d\rho.
\]
Assuming $\rho_0-1+R>1$ and $\cosh R<2\sinh R$, we have
\begin{align}\label{s1-2}
\begin{split}
&||S_1||^2_{L^2(C)}\\
&\geq\delta\int_{-R}^{\rho_0-1}
\frac{1}{(\cosh R)^{2m-1}}\sum_{k=1}^\infty
|A_k|^2 e^{-\frac{8\pi k}{\delta}(\arctan e^{\rho_0-1}
-\arctan e^{-R})} d\rho\\
&\geq \frac{\delta}{(\frac{\eps_1}{2\delta})^{2m-1}}
\sum_{k=1}^\infty |A_k|^2 e^{-\frac{8\pi k}{\delta}
(\arctan e^{\rho_0-1}-\arctan e^{-R})}.
\end{split}
\end{align}

By~\eqref{s1}, ~\eqref{s1-1} and~\eqref{s1-2}, we have
\begin{equation}\label{s1-c}
\frac{||S_1||^2(x_0)}{||S_1||^2_{L^2(C)}}
\leq\frac{2^{2m-1}\eps_1^{2m-1}}{\delta^{2m}e^{-\frac{\mu}{\sqrt{\delta}}}}
\rightarrow 0
\end{equation}
for $\delta\rightarrow 0$.


The idea for estimating $S_2$ and $S_3$ are almost the same. 
By~\eqref{defs}, we have
\begin{align}\label{s2}
\begin{split}
& ||S_2||^2(x_0)=\frac{1}{(\cosh\rho_0)^{2m}}|B_0|^2,\\
&||S_2||^2_{L^2(C)}=\delta\int^R_{-R}
\frac{1}{(\cosh\rho)^{2m-1}}|B_0|^2 d\rho.
\end{split}
\end{align}
If $\delta\rightarrow 0$, then $R\rightarrow +\infty$. Thus if
$R$ is large enough, we have
\[
\int_{-R}^R\frac{1}{(\cosh\rho)^{2m-1}} d\rho\geq\mu_1>0,
\]
where $\mu_1$ is a constant only depending on $m$. Thus
\begin{equation}\label{s2-c}
\frac{||S_2||^2(x_0)}{||S_2||^2_{L^2(C)}}=\frac{1}{\mu_1}
\frac{1}{\delta(\cosh\rho_0)^{2m}}
=\frac{1}{\mu_1\eps_1^m}\delta^{m-1}\rightarrow 0
\end{equation}
for $\delta\rightarrow 0$.

For $S_3$, we have
\begin{align}\label{s3}
\begin{split}
&||S_3||^2(x_0)=\frac{1}{(\cosh\rho_0)^{2m}}
|\sum_{k=-\infty}^{-1}B_ke^{-\frac{4\pi}{\delta}k
(\arctan e^{\rho_0}-\arctan e^R)}|^2\\
&\leq\sum_{k=-\infty}^{-1}|B_k|^2 e^{-\frac{8\pi}{\delta}k(\frac\pi
4-\arctan e^R)}
\sum_{k=-\infty}^{-1} e^{-\frac{8\pi}{\delta}k(\arctan e^{\rho_0}-
\frac\pi 4)}.
\end{split}
\end{align}
Since $\rho_0\rightarrow -\infty$, we can assume
\[
\arctan e^{\rho_0}<\frac{\pi}{8}.
\]
Thus
\begin{equation}\label{s3-1}
\sum_{k=-\infty}^{-1} e^{-\frac{8\pi}{\delta}k(\arctan e^{\rho_0}-\frac\pi
4)}
\leq\sum_{k=-\infty}^{-1}e^{\frac{\pi^2}{\delta}k}
\leq 2e^{-\frac{\pi^2}{\delta}}
\end{equation}
for $e^{-\frac{\pi}{\delta^2}}<\frac 12$.
On the other hand,
\begin{align}\label{s3-2}
\begin{split}
&||S_3||^2_{L^2(C)}=\delta
\int_{-R}^R\frac{1}{(\cosh\rho)^{2m-1}}\sum_{k=-\infty}^{-1}
|B_k|^2 e^{-\frac{8\pi k}{\delta}(\arctan e^\rho-\arctan e^R)} d\rho\\
&\geq \delta\int^R_0\frac{1}{(\cosh\rho)^{2m-1}}
\sum_{k=-\infty}^{-1}|B_k|^2 e^{-\frac{8\pi k}{\delta}(\frac\pi 4-\arctan
e^R)} d\rho\\
&\geq\frac{\delta R}{(\cosh R)^{2m-1}}\sum_{k=-\infty}^{-1}
|B_k|^2 e^{-\frac{8\pi k}{\delta}(\frac\pi 4-\arctan e^R)}.
\end{split}
\end{align}

By ~\eqref{s3},~\eqref{s3-1} and~\eqref{s3-2}, we have
\begin{align}\label{s3-c}
&\frac{||S_3||^2(x_0)}{||S_3||^2_{L^2(C)}}
\leq\frac{2e^{-\frac{\pi^2}{\delta}}}{\delta R}
(\cosh R)^{2m-1}
\leq \frac{2^{2m}}{\delta^{2m}}2e^{-\frac{\pi^2}{\delta}}
\rightarrow 0.
\end{align}

Thus for any $\eps>0$ and $m\geq 2$,
from ~\eqref{s1-c}, ~\eqref{s2-c} and~\eqref{s3-c},
 we can find $M$ 
such that there is a closed geodesic with the length sufficiently small
and
an $x_0\in M$ such that
\[
\frac{||S_i||^2(x_0)}{||S_i||^2_{L^2(C)}}\leq\eps
\]
for $i=1,2,3$.

One can check that 
\[
(S_i, S_j)_{L^2(C)}=0.
\]
Thus for any $S\in H^0(M,K_M^m)$ with $||S||_{L^2(M)}$ and
$x_0\in M$,
\[
||S||^2(x_0)\leq\frac{||S||^2(x_0)}{||S||^2_{L^2(C)}}
\leq 3\frac{\sum_{i=1}^3||S_i||^2(x_0)}
{\sum_{i=1}^3||S_i||^2_{L^2(C)}}\leq 3\eps.
\]
Theorem~\ref{counterexample} is proved.

\qed
