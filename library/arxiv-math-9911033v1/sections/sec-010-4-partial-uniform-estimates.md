---
doc_id: arxiv-math-9911033v1
doc_title: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface"
section_id: sec-010-4-partial-uniform-estimates
section_title: "Partial uniform estimates"
section_number: 4
pages: 17-22
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "On the lower bound estimates of sections of the canonical bundles over a Riemann surface — 18 sections: Introductions 1; A lower bound estimate 4; A counterexample 11"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
---
Let
$M$ be a Riemann surface of genus $g$ and constant
 curvature $(-1)$.
In this section, we
prove that there is a (positive) lower bound of ~\eqref{quan} depending
only
on the injective radius of the point. More precisely,
for $m$ large 
enough, for any $x\in M$, there is a section $S\in H^0(M,K_M^m)$
such that $||S||_{L^2}=1$ and $||S||(x)\geq C(\delta_x)$
where $C(\delta_x)$ is a positive constant
depending only on $\delta_x$
 and $\delta_x$ is the
injective radius  at $x$.

Note that in the result the lower bound 
doesn't depend on the injective radius of $M$, which will go to zero as 
$M$ approaches the boundary of the Teichm\"uller space.

We  use all the notations of in \S ~\ref{sec3} about the
collars and the functions on them. The following proposition is a
corollary of the collar theorem:

\begin{prop}\label{prop31}
Let $M$ be a Riemann surface of genus $g\geq 2$ and constant
curvature $(-1)$. Let $\gamma_1,\cdots,\gamma_s$ be the closed geodesics
on $M$ such that
\[
length(\gamma_i)\leq\frac{1}{1000},\qquad
1\leq i\leq s.
\]
Let $C_{\gamma_i} (1\leq i\leq s)$ be the corresponding collars embedded
in
$M$ (Theorem~\ref{keen}). Then for any 
$x\in M\backslash U_{i=1}^s C_{\gamma_i}$,
there is an absolute constant $\eps_2>0$ such that
\[
\delta_x\geq\eps_2.
\]
\end{prop}


{\bf Proof.} 
 Let $\delta=\frac{1}{4000}$.
Let $x\in M\backslash\cup_{i=1}^sC_{\gamma_i}$ and $inj(x)\geq\delta_x>0$.
Then there
is a
point
$y\in M$
such that there are two geodesics $l_1$ and $l_2$
connecting $x$ and $y$ but $l_1$ and $l_2$ are not
homotopic to each other.
If $\delta_x>1$, the theorem has been proved. Otherwise, let $\gamma'$
be the shortest closed curve homotopic to the closed curve $l_1^{-1}l_2$
in
\[
D'=M\backslash\underset{length(\gamma_i)<2\delta}{\cup}
C_{\gamma_i}(R_i-2),
\]
where 
\[
C_{\gamma_i}(R_i-2)=\{
x| dist(x,\gamma_i)< R_i-2\}.
\]
Since
$D'$ is a compact set. If $\gamma'$ doesn't touch any of the
boundary $\pa C_{\gamma_i}(R_i-2)$ for any $i$, then $\gamma'$ must be a
closed
geodesic and by the definition, we have $length(\gamma)\geq
\frac{1}{1000}$ and
thus
$\delta_x\geq\frac{1}{2000}$. Otherwise either $\delta_x>1$ or
$\gamma'\subset
C_{\gamma_i}(R_i-1)\backslash C_{\gamma_i}(R_i-2)$ for some $i$. In the
latter
 case, since $\gamma'$ is not homotopic to zero,
we see  that
\[
length(\gamma')\geq length(\gamma_i) \cosh(R_i-2)\geq\frac {1}{18}\eps_1
\]
(remember $length(\gamma_i)\sinh R_i=\eps_1$).
Thus
\[
\delta_x\geq\frac 12 length(\gamma')\geq \frac{1}{36}\eps_1\geq\eps_2
\]
for $\eps_2=\frac{1}{36}\eps_1$.

\qed




Using the above lemma, we know that outside the collars whose shortest
closed geodesics are small, the injective radius has a lower bound and
the weight function in Proposition~\ref{del} can be constructed in the
ordinary way.
If $x\in C_{\gamma_i}$ for some $i$, we are going to construct the  weight
functions having the compact support within $C_{\gamma_i}$. For this
reason, let's first assume that $C_\delta$ is a collar with 
$\delta<\frac{1}{1000}$ and do some analysis on it.

Let's fix some notations:
there are
absolute constants $\eps_3, \eps_4>0$ such that
\begin{equation}\label{eps2}
\eps_3<\delta\cosh R, \delta\cosh(R\pm 4),\delta\sinh (R\pm 4),
\delta e^{R\pm 4}<\eps_4.
\end{equation}

Let $(\rho,\theta)$ be the local coordinate of the collar
$C=C_\delta$ as in \S ~\ref{sec3}. Then
\begin{equation}\label{3-defw}
w=e^{\frac{2\pi i}{\delta}\theta-\frac{4\pi}{\delta}(\arctan
e^\rho-\frac\pi 4)}
\end{equation}
is the holomorphic function on $C_\delta$.
Let $x_0$ and $p_0$ be the points on $C_\delta$ such that
the local coordinate of $x_0$ and $p_0$ can be represented as:
 $x_0=(\rho_0,0)$ for $R-4>\rho_0\geq 0$ and
$p_0=(R-1,0)$. The function $w$ at $x_0$ and $p_0$
has the values
\begin{align}\label{3-defw0}
\begin{split}
&w_0=e^{-\frac{4\pi}{\delta}(\arctan e^{\rho_0}-\frac\pi 4)},\\
& w_{p_0}=e^{-\frac{4\pi}{\delta}(\arctan e^{R-1}-\frac\pi 4)}
\end{split}
\end{align}
at $x_0$ and $p_0$ respectively.
Let
\begin{equation}\label{alpha}
\alpha=\frac{2\arctan e^{\rho_0}}{\pi},
\end{equation}
and define the functions $\phi_1$, $\phi_2$ and $\phi_3$ 
on $C_\delta$ 
to be

\begin{align}\label{defphi}
\begin{split}
&\phi_1=\log |\frac{w}{w_0}-1|,\\
&\phi_2=\log |\frac{w}{w_{p_0}}-1|,\\
&\phi_3=\phi_1-\alpha\phi_2.
\end{split}
\end{align}


The Riemann metric on $C_\delta$ can be represented as
\begin{equation}\label{rie}
ds^2=d\rho^2+(\cosh\rho)^2 d\theta^2.
\end{equation}
Let the injective radius at $x_0$, $p_0$ and $x$ be
$\delta_{x_0}$, $\delta_{p_0}$ and $\delta_x$. Then we have an
absolute
constant $\eps_5>0$ such that
\begin{equation}\label{ddelta}
\left\{
\begin{array}{l}
\frac 12\delta\cosh\rho_0>\delta_{x_0}>\eps_5\delta\cosh\rho_0,\\
\frac 12\eps_1>\delta_{p_0}>\eps_5,\\
\frac 12\delta\cosh\rho>\delta_x>\eps_5\delta\cosh\rho.
\end{array}
\right.
\end{equation}

We establish some elementary properties of the function
$\phi_3$. 
Let $d=d(x)$ be the distance function to the point $x_0$. Then we have


\begin{lemma}\label{4-lem31}
With the notations as above,
there are constants $C_9, C_{10}>0$ such that
\begin{equation}\label{3-phi3}
\phi_3\leq C_9,
\end{equation}
for $-R+1\leq\rho\leq R-2$
and 
\begin{equation}\label{3-phi31}
\phi_3\geq\log d(x)-\frac{4\pi}{\delta e^\rho}-C_{10}
\end{equation}
for $d(x)\leq\delta_{x_0}$.
\end{lemma}

{\bf Proof.} By ~\eqref{3-defw} and~\eqref{3-defw0}, we have
\begin{align}\label{wfrac}
\begin{split}
&\frac{w}{w_0}=e^{\frac{2\pi i}{\delta}\theta-\frac{4\pi}{\delta}
(\arctan e^\rho-\arctan e^{\rho_0})},\\
&\frac{w}{w_{p_0}}=e^{\frac{2\pi i}{\delta}\theta-\frac{4\pi}{\delta}
(\arctan e^\rho-\arctan e^{R-1})}.
\end{split}
\end{align}

From ~\eqref{wfrac},
we have
\begin{align}\label{basic}
\left\{
\begin{array}{ll}
 \log |\frac{w}{w_0}-1|\leq\log 2&\rho_0\leq\rho\leq R-2,\\
\log|1-\frac{w_0}{w}|\leq\log 2 &-R+1\leq\rho\leq\rho_0,\\
\log |\frac{w}{w_{p_0}}|\geq 0& -R+1\leq\rho\leq R-1,\\
 \log|1-\frac{w_{p_0}}{w}|
\geq\log(1-e^{-\frac{2\pi}{\eps_4}})&
-R+1\leq\rho\leq R-2.
\end{array}
\right.
\end{align}

If $\rho_0\leq\rho\leq R-2$, then we can write
\[
\phi_3=\log|\frac{w}{w_0}-1|-\alpha\log|\frac{w}{w_{p_0}}|
-\alpha\log|1-\frac{w_{p_0}}{w}|.
\]
By ~\eqref{basic}, we have
\begin{equation}\label{phi3-1}
\phi_3\leq\log 2-\log (1-e^{-\frac{2\pi}{\eps_4}}).
\end{equation}

If $-R+1\leq\rho\leq\rho_0$. We can write
\begin{equation}\label{3-phi3r}
\phi_3=\log|\frac{w}{w_0}|-\alpha\log|\frac{w}{w_{p_0}}|
+\log|1-\frac{w_0}{w}|-\alpha\log|1-\frac{w_{p_0}}{w}|.
\end{equation}
Using~\eqref{wfrac},
we have
\begin{align}\label{mainp}
\begin{split}
&\log|\frac{w}{w_0}|-\alpha\log|\frac{w}{w_{p_0}}|\\
&=-\frac 8\delta (\frac\pi 2-\arctan e^{\rho_0})
\arctan e^\rho
+\frac{8}{\delta}\arctan e^{\rho_0}
(\frac\pi 2-\arctan e^{R-1}).
\end{split}
\end{align}
Thus by~\eqref{eps2} and~\eqref{ddelta}
\begin{equation}\label{mains}
-\frac{4\eps_5}{\delta_{x_0}}\leq
\log|\frac{w}{w_0}|-\alpha\log|\frac{w}{w_{p_0}}|
\leq\frac{4\pi}{\eps_3}.
\end{equation}
By~\eqref{basic},~\eqref{3-phi3r} and ~\eqref{mains}, we have
\begin{equation}\label{phi3-2}
\phi_3\leq\frac{4\pi}{\eps_3}+\log 2-\log (1-e^{-\frac{2\pi}{\eps_4}}).
\end{equation}
Thus by ~\eqref{phi3-1} and ~\eqref{phi3-2}, we have $\phi_3\leq C_9$ for
\[
C_9=\frac{4\pi}{\eps_3}+\log 2-\log (1-e^{-\frac{2\pi}{\eps_4}}).
\]


Let's now assume that $d(x)<\delta_{x_0}$. Then by the triangle
inequality
we have 
\begin{equation}
\left\{
\begin{array}{ll}
|\rho-\rho_0|+|\theta|\cosh\rho_0\geq d(x) & 0\leq\theta
\cosh\rho_0<d(x),\\
|\rho-\rho_0|+|\theta-\delta\cosh\rho_0|\geq d(x) & \delta\cosh\rho_0-d(x)
\\&
<\theta\cosh\rho_0<\delta\cosh\rho_0.
\end{array}
\right.
\end{equation}
Without losing generality we assume that $0\leq\theta\leq d(x)$
and $|\rho-\rho_0|+|\theta|\cosh\rho_0\geq d(x)$. If $\theta
\cosh\rho_0\geq\frac 14 d(x)$,
then
\begin{equation}\label{3-sub-1}
|\frac{w}{w_0}-1|\geq
e^{-\frac{4\pi}{\delta}(\arctan e^\rho-\arctan e^{\rho_0})}
\sin\frac{2\pi}{\delta}\theta
\geq\frac\pi 4 e^{-\pi} d(x).
\end{equation}
On the other hand, if $|\rho-\rho_0|\geq\frac 12 d(x)$, then 
\begin{equation}\label{3-sub-2}
|\frac{w}{w_0}-1|\geq e^{-\pi}\frac{2\pi}{\eps_1}d.
\end{equation}
By~\eqref{3-sub-1} and~\eqref{3-sub-2},
there is a
constant $C_{11}>0$ such that
\begin{equation}\label{3-sub-3}
\log|\frac{w}{w_0}-1|\geq\log d -C_{11}.
\end{equation}
We also have
\begin{equation}\label{3-last}
\log|\frac{w}{w_{p_0}}-1|\leq\log 2+\frac{4\pi}{\delta e^\rho}.
\end{equation}
for $d\leq\delta_{x_0}$. By~\eqref{3-sub-3} and ~\eqref{3-last},
from ~\eqref{defphi}
\[
\phi_3\geq\log d-C_{11}-(\log 2+\frac{4\pi}{\delta e^\rho}).
\]
This completes the proof of Lemma~\ref{4-lem31}.

\qed

\begin{lemma}\label{4-lem32}
There is a constant $C_{12}>0$ such that
\[
|\phi_3|\leq C_{12},\qquad |\nabla\phi_3|\leq C_{12}
\]
for $R-3<|\rho|<R-2$.
\end{lemma}

{\bf Proof.} By the above lemma, we see that
\[
\phi_3\leq C_9
\]
for the  constant $C_9$. 
Thus we just need to prove the lower bound of $\phi_3$ and the 
bound for the derivative of $\phi_3$.

If $R-3<\rho<R-2$, 
by~\eqref{wfrac},
we have
\begin{equation}
|\frac{w}{w_0}|\leq e^{-\frac{2\pi}{\eps_1}}.
\end{equation}
Thus
\begin{equation}
\phi_1\geq\log(1-e^{-\frac{2\pi}{\eps_1}}).
\end{equation}
Also we have
\begin{equation}
|\frac{w}{w_{p_0}}|\leq e^{\frac{4\pi}{\eps_3}}
\end{equation}
for $R-3<\rho<R-2$.
Thus
\begin{equation}\label{3-sub-lower1}
\phi_3\geq\log(1-e^{-\frac{2\pi}{\eps_1}})
-\log(1+e^{\frac{4\pi}{\eps_3}}).
\end{equation}
If $R-3<-\rho<R-2$, then by ~\eqref{mainp}, we have
\[
\log|\frac{w}{w_0}|-\alpha\log|\frac{w}{w_{p_0}}|
\geq-\frac{8}{\delta}(\frac\pi 2-\arctan e^{\rho_0})\arctan e^{-(R-3)}
\geq -\frac{2}{\eps_2}.
\]
By~\eqref{3-phi3r}, we have
\begin{equation}\label{3-sub-lower2}
\phi_3\geq -\frac{8}{\eps_3}+\log (1-e^{-\frac{\pi^2}{2}})
-\log 2.
\end{equation}
Combining ~\eqref{3-sub-lower1} and~\eqref{3-sub-lower2}, we get the 
lower bound of $\phi_3$.
Next let's  consider $\nabla\phi_3$. Obviously
\[
|\nabla\phi_3|\leq|\nabla\phi_1|+|\nabla\phi_2|.
\]
Thus we just need to estimate
$|\nabla\phi_1|$ and $|\nabla\phi_2|$. 
By~\eqref{rie}, the Riemann metric under the
coordinate $w$ can be written as 
\[
ds^2=\frac{\delta^2(\cosh\rho)^2}{4\pi^2|w|^2}dw d\bar w.
\]
Thus
\begin{align*}
&|\nabla\phi_1|^2=\frac{4\pi^2|w|^2}{\delta^2(\cosh\rho)^2}
\cdot\frac{1}{|w-w_0|^2}=\frac{4\pi^2}{\delta^2(\cosh\rho)^2}
\cdot\frac{1}{|1-\frac{w_0}{w}|^2},\\
&|\nabla\phi_2|^2=\frac{4\pi^2|w|^2}{\delta^2(\cosh\rho)^2}
\cdot\frac{1}{|w-w_{p_0}|^2}
=\frac{4\pi^2}{\delta^2(\cosh\rho)^2}     
\cdot\frac{1}{|1-\frac{w_{p_0}}{w}|^2}.
\end{align*}
Using the same elementary estimates as above, we get,
\begin{equation}
\left\{
\begin{array}{ll}
|\frac{w_0}{w}|\geq e^{\frac{2\pi}{\eps_1}}&
R-3<\rho<R-2,\\
|\frac{w_0}{w}|\leq e^{-\frac{\pi^2}{2\delta}}&
R-3<-\rho<R-2,\\
|\frac{w_{p_0}}{w}|\leq e^{-\frac{2\pi}{\eps_1}}&
R-3<\rho<R-2,\\
|\frac{w_{p_0}}{w}|\leq e^{-\frac{\pi^2}{2\delta}}
&
R-3<-\rho<R-2.
\end{array}
\right.
\end{equation}
Using these results, we get the bound for the gradient of $\phi_1$ and
$\phi_2$. 
This completes the proof of the lemma.

 \qed



The following proposition summarizes the technical results of this
section.
\begin{prop}\label{tech}
Suppose $M$ is a compact Riemann surface of genus $g\geq 2$ and
constant curvature $(-1)$. Then for any $x_0\in M$, there is a function
$\phi=\phi_{x_0}$ such that $\phi$ is smooth on $M\backslash\{x\}$ and 
\begin{enumerate}
\item In a neighborhood $U_x$ of $x$, $\phi$ can be written as
\[
\phi=2\log d(x)+\psi,
\]
where $\psi$ is a smooth function on $U_x$. Consequently,
\begin{equation}\label{infty}
\int_{U_x} e^{-\phi}=+\infty.
\end{equation}
\item There is a constant $C_{13}$ such that
\begin{equation}\label{t-lower}
\frac{\sqrt{-1}}{2\pi}\pa\bar\pa\phi\geq -C_{13}\omega_g
\end{equation}
on $M\backslash\{x\}$, where $\omega_g$ is the K\"ahler form
of $M$;
\item $\phi$ satisfies
\begin{equation}\label{t-upper}
\phi\leq C_{13}
\end{equation}
on $M$ and
\begin{equation}\label{t-lowerb}
\phi\geq 2\log d(x)-\frac{2\pi}{\delta_{x_0}}-C_{13}
\end{equation}
for $d(x)\leq\delta_{x_0}$.
\end{enumerate}
\end{prop}

{\bf Proof.} Let $\gamma_1,\cdots,\gamma_s$ be the closed geodesics
such that $length(\gamma_i)<\frac{1}{1000}$. Let
$C_{\gamma_i}$ be the corresponding collars. Let
\[
C_{\gamma_i}(R_i-4)=\{
x| dist(x,\gamma_i)\leq R_i-4\}\quad i=1,\cdots s.
\]

For any $x_0\in M$, if $x_0\in C_{\gamma_i}(R_i-4)$ for some $i$,
then let $C_\delta=C_{\gamma_i}$ and
 define
$\phi=\phi_{x_0}:M\rightarrow \R$ as follows

\begin{equation}\label{defphi1}
\phi=\left\{
\begin{array}{ll}
2\eta(\rho-(R-3))\phi_3 & \rho\geq 0\quad and\quad x\in C_\delta,\\
2\eta(-\rho-(R-3))\phi_3 & \rho<0\quad and\quad x\in C_\delta,\\
0 & otherwise,
\end{array}
\right.
\end{equation}
where the function $\eta$ is defined in ~\eqref{eta}.
By Lemma~\ref{4-lem31}, Lemma~\ref{4-lem32} and the fact that
$\phi_3$ is harmonic on $C_\delta\backslash\{x_0\}\backslash\{p_0\}$,
it is easy to check that the function $\phi$ satisfies all the  
assertions in the proposition. On the other hand, if $x_0\notin
C_{\gamma_i}(R_i-4)$ for any
$1\leq i\leq s$, then by Proposition~\ref{prop31}, $\delta_{x_0}\geq
\eps_2$. The argument becomes quiet standard: define
\begin{equation}\label{defphi2}
\phi=2\eta(\frac{d(x)}{\eps_2})\log(\frac{d(x)}{\eps_2})
\end{equation}
Then we can prove that $\phi$ satisfies all the requirements by using the
same
method as in
Lemma~\ref{lem23}.

\qed

\begin{theorem}
Let $M$ be a Riemann surface of genus $g\geq 2$ and constant curvature
$(-1)$. Then there are absolute constants $m_0>0$ and $D>0$ such that for
any $m>m_0$
and any $x_0\in M$, there is a section $S\in H^0(M,K_M^m)$ with
$||S||_{L^2}=1$ such that
\begin{equation}
||S||(x_0)\geq\frac{\sqrt m}{D(1+\frac{1}{\sqrt m\delta_{x_0}^2}
e^{\frac{\pi}{\delta_{x_0}}})}.
\end{equation}
\end{theorem}

{\bf Proof.}
Let $x_0\in M$ and $U_{x_0}=\{x| dist(x,x_0)<\delta_{x_0}\}$. Let $z_1$ be
the holomorphic function  on $U_{x_0}$ such that the hermitian metric
can be represented as
\[
ds^2=\frac{1}{(1-\frac 14|z_1|^2)^2}dz_1 d\bar z_1.
\]
For $m>0$ large enough, let
\[
u_1=\bar\pa(\eta(\frac{2|z_1|}{\delta_{x_0}}))(dz_1)^m.
\]
Then $\bar \pa u_1=0$ and 
\[
||\bar\pa
u_1||^2\leq\frac{16}{\delta^2_{x_0}}
(1-\frac 14|z_1|^2)^{m+1}
\]
for $\frac 14\delta_{x_0}\leq|z_1|\leq\frac 12\delta_{x_0}$.
Thus
there is a $C_{14}>0$ such that
\[
\int_M||\bar\pa u_1||^2 e^{-\phi_{x_0}}\leq
\frac 1m\frac{C_{14}}{\delta^4_{x_0}} e^{\frac{2\pi}{\delta_{x_0}}}.
\]

Let $m_0=C_{13}+2$. 
By Proposition~\ref{del}, for $m>m_0$,  
 we can find a $u\in\Gamma(M,K_M^m)$ such that $\bar\pa u=u_1$ with
\begin{equation}\label{defu1}
\int_M||u||^2e^{-\phi_{x_0}}\leq
\frac{1}{m(m-C_{13}-1)}
\frac{C_{14}}{\delta^4_{x_0}}e^{\frac{2\pi}
{\delta_{x_0}}}.
\end{equation}
Let $S=\eta(\frac{2|z_1|}{\delta_{x_0}}) (dz_1)^m-u$. Then
$\bar\pa S=0$. Thus $S$ is an element of $H^0(M,K_M^m)$. Furthermore,
since $\int_M e^{-\phi_{x_0}}=+\infty$, we must have $u(x_0)=0$. So
\begin{equation}\label{u0}
||S||(x_0)=1.
\end{equation}
On the other hand,
\[
||S||^2_{L^2}\leq 2(\int_M||u||^2+\int_M||\eta (dz_1)^m||^2).
\]
By~\eqref{defu1} and ~\eqref{t-upper}, we have
\begin{equation}\label{u2}
\int_M||u||^2\leq
\frac{1}{m(m-C_{13}-1)}\cdot
\frac{C_{14} e^{C_{13}}}{\delta^4_{x_0}}
e^{\frac{2\pi}{\delta_{x_0}}}.
\end{equation}
We also have
\begin{equation}\label{u3}
\int_M||\eta (dz_1)^m||^2\leq\frac{\pi}{m}.
\end{equation}
The theorem follows from ~\eqref{u0},~\eqref{u2}
and~\eqref{u3}.

\qed
