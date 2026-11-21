---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-010-6-harmonic-substitution
section_title: "Harmonic substitution"
section_number: 6
pages: 17-23
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.968
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
\label{sec:harmonic}
In this section we study the effects on the local distortion of
a curve if we replace some subarcs of
a curve by straight segments, since this is
what we will do later to adequately modify minimizing sequences  for the
M\"obius energy. By Blatt's characterization \cite[Theorem~1.1]{blatt_2012a}
of the corresponding
energy space we can assume  arclength parametrized  curves of class 
$W^{\frac32,2}(\R/\Z,\R^n)$, but keep in mind 
that such a replacement by straight
segments generally destroys this fractional Sobolev regularity.

We begin with a result that basically reflects the embedding of $W^{\frac32,2}$
into the space of bounded mean oscillation (BMO). Denote the integral mean of a function
$f$  over a set $A$ by 
$$
(f)_A\equiv\mvint_A f(z)\,dz := \frac{1}{|A|}\int_A f(z)\,dz,
$$
and abbreviate the annular
region 
\begin{equation}\label{eq:annular}
A_{r,\theta}(x):= B_r(x)\setminus B_{\theta r}(x)\subset\R/\Z\quad\Fo \theta\in (0,1),
\,x\in\R/\Z,
\end{equation}
with measure 
\begin{equation}\label{eq:measure-annulus}
|A_{r,\theta}(x)|=2r(1-\theta).
\end{equation}
\begin{lemma}[Quantitative embedding $W^{\frac32,2}\hookrightarrow \,\textnormal{BMO}$]
\label{lem:quant-embed}
Assume that for an arclength parametrized curve $\eta\in W^{\frac32,2}(\R/\Z,\R^n)$
there is a parameter
$x\in\R/\Z$ and there exist constants $\theta,r\in (0,\frac12)$, such that
\begin{equation}\label{eq:frac-seminorm-theta}
\lfloor \eta'\rfloor^2_{\frac12,2,A_{r,\theta}(x)} < \theta.
\end{equation}
Then we have
\begin{equation}\label{eq:bmo1}
\mvint_{B_r(x)}|\eta'(z)-(\eta')_{B_r(x)}|^2\,dz < 8\theta,
\end{equation}
and if $\theta < \frac18 $ in addition, then $|(\eta')_{B_r(x)}|>0$ and
\begin{equation}\label{eq:bmo2}
\mvint_{B_r(x)}|\eta'(z)-\nu|^2\,dz < 32\theta,
\end{equation}
where 
\begin{equation}\label{eq:bmo3}
\nu\equiv \nu_{B_r(x)}
:=\frac{(\eta')_{B_r(x)}}{|(\eta')_{B_r(x)}|}\in\S^{n-1}.
\end{equation}
\end{lemma}
\begin{proof}
We start with  estimates for
the mean quadratic deviation on the annulus  $A:=
A_{r,\theta}(x)$
with \eqref{eq:measure-annulus}, Jensen's inequality, and \eqref{eq:frac-seminorm-theta}:
\begin{eqnarray}\label{eq:mean-deviation-annulus}
\textstyle\mvint_{A}|\eta'(z)\!-\!(\eta')_A|^2dz 
& \overset{\eqref{eq:measure-annulus}}{=} &
\textstyle\frac1{2r(1-\theta)}\int_A|\eta'(z)\!-\!\mvint_A\eta'(u)du|^2dz\notag
\overset{\eqref{eq:measure-annulus}}{\le}
\textstyle
\frac1{4r^2(1-\theta)^2}\int_A\int_A|\eta'(z)\!-\!\eta'(u)|^2dudz\notag\\
&\le &\textstyle
\frac1{(1-\theta)^2}\int_A\int_A\frac{|\eta'(z)-\eta'(u)|^2}{|z-u|^2}dudz
 \overset{\eqref{eq:frac-seminorm-theta}}{<} 
\textstyle\frac{\theta}{(1-\theta)^2} < 4\theta,
\end{eqnarray}
since $\theta\in (0,\frac12)$. With $|\eta'|=1$ a.e.\@ on $\R/\Z$ we have the rough
estimate $|\eta'(\cdot)-(\eta')_A|\le 2$ a.e., which implies for the mean deviation from
$(\eta')_A$ on the full ball $B:=B_r(x)$
\begin{eqnarray}\label{eq:deviation-annulus-ball}
\textstyle\mvint_B|\eta'(z)-(\eta')_A|^2dz & = &
\textstyle
\frac1{2r}\int_A|\eta'(z)-(\eta')_A|^2 dz + \frac1{2r}\int_{B_{\theta r}(x)}
|\eta'(z)-(\eta')_A|^2 dz\notag\\
& \overset{\eqref{eq:measure-annulus}}{=} &
\textstyle
\frac{2r(1-\theta)}{2r}\mvint_A
|\eta'(z)-(\eta')_A|^2 dz+\frac{2\theta r}{2r}\mvint_{B_{\theta r}(x)}
|\eta'(z)-(\eta')_A|^2 dz\notag\\
& \overset{\eqref{eq:mean-deviation-annulus}}{<} &
(1-\theta)4\theta + 4\theta < 8\theta.
\end{eqnarray}
This proves \eqref{eq:bmo1}
since the function $c\mapsto\mvint_B|\eta'(z)-c|^2dz$ is minimized
on $\R^n$ by the mean value $c^*:=(\eta')_B\in\R^n$.

If $\theta\in (0,\frac18)$, 
then take the integral mean of the inequality
$|(\eta')_B|\ge |\eta'(z)|-|\eta'(z)-(\eta')_B|$ over $B=B_r(x)$
to obtain with \eqref{eq:bmo1} and H\"older's inequality
$|(\eta')_B|>1-\sqrt{8\theta}>0$, so that the vector $\nu$ in
\eqref{eq:bmo3} is well-defined. With the help of 
$|b-\frac{b}{|b|}|^2=|\frac{b|b|-b}{|b|}|^2=||b|-1|^2$ for $b:=(\eta')_B\in\R^n\setminus
\{0\}$ we obtain 
\begin{align*}
\textstyle
\mvint_B|(\eta')_B-\nu|^2 dz& =
\textstyle
\mvint_B\big|1-|(\eta')_B|\big|^2 dz =\mvint_B\big||\eta'(z)|-|(\eta')_B|\big|^2 dz
\le 
\mvint_B|\eta'(z)-(\eta')_B|^2 dz,
&
\end{align*}
so that by means of \eqref{eq:bmo1}
\[
\textstyle
\mvint_B|\eta'(z)-\nu|^2dz \le 2\big\{\mvint_B|\eta'(z)-(\eta')_B|^2dz
+\mvint_B|(\eta')_B-\nu|^2dz\big\}\overset{\eqref{eq:bmo1}}{<} 2 
\{8\theta +8\theta\}=
32\theta.\qedhere
\]
\end{proof}
To find suitable subarcs to be replaced by straight segments on a given curve,
we pick up an idea of Semmes \cite{semmes_1991a} 
from his study of 
chord-arc surfaces with small constants. 

Define for a fixed parameter $x\in\R/\Z$ and constants $r\in (0,\frac12)$ and
$\theta\in (0,\frac1{20})$ the \emph{localized excess function} on the
ball $B:=B_r(x)$ as
\begin{equation}\label{eq:loc-excess}
e_B(z):=\big(  \eta'(z)-\nu \big)\chi_B(z)\quad\Fo z\in\R,
\end{equation}
where $\nu\equiv\nu_B=\nu_{B_r(x)}\in\S^{n-1}$ is the vector defined
in \eqref{eq:bmo3} of Lemma \ref{lem:quant-embed}, and $\chi_A$ denotes
the characteristic function of a set $A\subset\R/\Z$. Moreover, we consider the
Hardy--Littlewood maximal function of the excess,
\begin{equation}\label{eq:hardy-littlewood}
\big( Me_B\big)(y):=\sup_{\rho >0}\,\mvint_{B_\rho(y)}|e_B(z)|\,dz
\end{equation}
satisfying the weak-type inequality (see, e.g., \cite[Chapter 3, 
Theorem~1.1, p.~101]{stein-shakarchi_2005})
\begin{align*}
\big|\big\{y\in\R: (Me_B)(y)>t\big\} \big| & 
\textstyle
\le \frac3{t}\|e_B\|_{L^1(\R)}=
\frac3{t}\int_B|\eta'(z)-\nu|dz\\
&\textstyle
\le\frac{6r}t \big(\mvint_B |\eta'(z)-\nu|^2 dz\big)^{\frac12}
\overset{\eqref{eq:bmo2}}{<}\frac{6r}t \sqrt{32\theta}<36
\sqrt{\theta}\cdot\frac{r}t\quad
\Foa t>0,
\end{align*}
where we used H\"older's inequality and \eqref{eq:bmo2}. Choosing $t:=\theta^{\frac14}$
we obtain
\begin{align*}
\textstyle
\big|\big\{y\in\R:(Me_B)(y)\le\theta^{\frac14} \big\}\cap B_{\frac{r}8}(x\pm\frac{r}2)
\big|&\ge\textstyle
|B_{\frac{r}8}(x\pm \frac{r}2)|-\big|\big\{y\in\R: (Me_B)(y)>\theta^{\frac14}\big\} 
\big|\\
& >\frac{r}4\big(1-144\cdot\theta^{\frac14}\big) >0
\end{align*}
for 
\begin{equation}\label{eq:theta1}
0<\theta<\theta_1:=\frac1{144^4}<\frac18.
\end{equation}
Consequently, the sets
\begin{equation}\label{eq:G-set}
\textstyle
G_\pm(x,\theta,r):=\big\{y\in\R: (Me_{B_r(x)})(y)\le\theta^{\frac14}\big\}\cap
B_{\frac{r}8}(x\pm\frac{r}2)\subset B_r(x)
\end{equation}
of \emph{good} endpoints of replaceable subarcs near the two parameters $x\pm\frac{r}2$ 
have positive measure if $\theta\in (0,\theta_1)$. 
The next lemma clarifies the term ``good'' in this context, by stating
that difference quotients of the curve $\eta$ rooted
at points in the set $G_\pm(x,\theta,r)$
can be approximated well by the unit vector $\nu=\nu_{B_r(x)}\in\S^{n-1}.$
\begin{lemma}[Difference quotients close to $\nu$]
\label{lem:difference-quotients}
Assume that the arclength parametrized curve $\eta\in W^{\frac32,2}(\R/\Z,\R^n)$
satisfies
\begin{equation}\label{eq:fractional-seminorm-theta2}
\textstyle
\lfloor\eta' \rfloor^2_{\frac12,2,A}<\theta\quad\textnormal{for some
$x\in\R/\Z$, $\theta\in (0,\theta_1)$ and $r\in (0,\frac12)$,}
\end{equation}
where $\theta_1$ is defined in \eqref{eq:theta1}, and $A:=A_{r,\theta}(x)=
B_r(x)\setminus B_{\theta r}(x)$. Then one has for
$\nu:=\nu_{B_r(x)}$ defined in \eqref{eq:bmo3}
\begin{equation}\label{eq:difference-quotients}
1\ge\Big\langle\frac{\eta(y)-\eta(x_0)}{y-x_0},\nu\Big\rangle_{\R^n}\ge
1-2\theta^{\frac14}\quad\AND\quad
\Big|
\Pi_{(\R\nu)^\perp}\Big(\frac{\eta(y)-\eta(x_0)}{y-x_0}\Big)\Big|
\le 2\theta^\frac18
\end{equation}
for all $y\in B_r(x)$ and $x_0\in G_\pm(x,\theta,r)$ as defined
in \eqref{eq:G-set}. Here, $\Pi_V$ denotes the orthogonal projection of $\R^n$ onto
a linear subspace $V\subset\R^n$.
\end{lemma}
\begin{proof}
The very left inequality in \eqref{eq:difference-quotients} is obvious since $\|\eta'
\|_{L^\infty}=1$ by assumption, and $|\nu|=1$. The second inequality can be 
derived with the fundamental theorem of calculus as follows:
\begin{align*}
\textstyle
1-\big\langle\frac{\eta(y)-\eta(x_0)}{y-x_0},\nu\big\rangle_{\R^n} & =
\textstyle
\frac1{y-x_0}\int_{x_0}^y\langle \nu-\eta'(u),\nu\rangle_{\R^n}du\\
&
\textstyle
\le\frac1{|y-x_0|}\int_{[x_0,y]}|\nu-\eta'(u)|du=
\frac1{|y-x_0|}\int_{[x_0,y]}|e_{B_r(x)}(u)|du,
\end{align*}
since both $y$ and $x_0$ are contained in $B_r(x)$.

The last integral may be bounded from above by
$$
\textstyle
\frac1{|y-x_0|}\int_{B_{|y-x_0|}(x_0)}|e_{B_r(x)}(u)|du
=2\mvint_{B_{|y-x_0|}(x_0)}|e_{B_r(x)}(u)|du\le 2\big(Me_{B_r(x)}\big)(x_0)\le
2\theta^{\frac14},
$$
because $x_0\in G_\pm(x,\theta,r)$, which proves the first chain of
inequalities
in \eqref{eq:difference-quotients}. The last inequality
follows from the first via
$\textstyle\big|\Pi_{(\R\nu)^\perp}(\zeta)\big|^2=
\big|\zeta-\langle\zeta,\nu\rangle\nu\big|^2=
|\zeta|^2-\langle\zeta,\nu\rangle^2\le 1-\langle\zeta,\nu\rangle^2=
(1+\langle\zeta,\nu\rangle)(1-\langle\zeta,\nu\rangle)\le 
2(1-\langle\zeta,\nu\rangle)
$ for all $\zeta\in\overline{B_1(0)}\subset\R^n$
(where we abbreviated 
$\langle\cdot,\cdot\rangle_{\R^n}$ by $\langle\cdot,\cdot\rangle$).
\end{proof}
Given a curve $\eta:\R/\Z\to\R^n$ and $N$ distinct parameters $x_1,\ldots,x_N\in
\R/\Z$, as well as $\theta\in (0,\theta_1)$, 
\begin{equation}\label{eq:little-r}
0<r<\frac12\min\big\{|x_i-x_k|_{\R/\Z}: i\not= k,\,i,k\in\{1,\ldots,N\}\big\}\le \frac14,
\end{equation}
and good sets $G_\pm^ i:=G_\pm(x_i,\theta,r)$ as defined  in \eqref{eq:G-set} for
$i=1,\ldots,N$, containing the parameters $x^i_\pm\in G_\pm^i$,
we replace the $N$ subarcs $\eta([x_-^i,x_+^i])$ by straight segments to define
the \emph{modified curve}
\begin{equation}\label{eq:modified-curve}
\tilde{\eta}(z):=\begin{cases}
\eta(x_-^i)+\frac{z-x_-^i}{x_+^i-x_-^i}\big(\eta(x_+^i)-\eta(x_-^i)\big) & \Fo
z\in [x_-^i,x_+^i], i=1\ldots,N,\\
\eta(z) & \Fo z\in\R/\Z\setminus\bigcup_{i=1}^N[x_-^i,x_+^i].
\end{cases}
\end{equation}
We call this procedure a \emph{harmonic substitution} comparable to Courant's and 
Morrey's  method in the theory of classic two-dimensional minimal surfaces
\cite[p. 25]{courant_1977}, \cite[Theorem~4.3.2]{morrey_1966}. But in the present
context, even if $\eta$ were smooth, the modified curve $\tilde{\eta}$ may not
even be of class $W^{\frac32,2}$. Or, in terms of the M\"obius energy, $\emob(\tilde{\eta})$ may be infinite even if $\tilde{\eta}$ is embedded and if the original curve $\eta$
has finite energy. Nevertheless, $\tilde{\eta}$ is 
$L^\infty$-close to $\eta$, and
its distortion  quotient remains under control.
\begin{lemma}[Distortion under harmonic substitution]
\label{lem:harmonic-substitution}
Let $\eta\in W^{\frac32,2}(\R/\Z,\R^n)$ be an arclength parametrized curve satisfying
\begin{equation}\label{eq:fractional-seminorm-theta3}
\lfloor \eta'\rfloor^2_{\frac12,2,A_{r,\theta}(x_i)}<\theta
\end{equation}
for 
finitely 
many distinct parameters $x_1,\ldots,x_N\in\R/\Z$ with $r\in (0,\frac14)$
chosen as in \eqref{eq:little-r},
and $\theta\in (0,\theta_2)$ for
$\theta_2:=256^{-4}$, and let $\tilde{\eta}$ be the modified curve defined
by harmonic substitution as in \eqref{eq:modified-curve}. Then
\begin{align}
\|\eta-\tilde{\eta}\|_{L^\infty}&< 6\theta^{\frac18}r\quad\AND\quad
\label{eq:linfty-dist-theta}\\
\max\Big\{\sup_{y,z\in [x_i-r,x_+^i]\atop y\not= z}{\textstyle\frac{d_{\tilde{\eta}}(\tilde{\eta}(y),\tilde{\eta}(z))}{|\tilde{\eta}(y)-
\tilde{\eta}(z)|},}\sup_{y,z\in [x_-^i,x_i+r]\atop y\not= z}
{\textstyle\frac{d_{\tilde{\eta}}(\tilde{\eta}(y),\tilde{\eta}(z))}{|\tilde{\eta}(y)-
\tilde{\eta}(z)|}}\Big\}&<1+4\theta^\frac14\Foa i=1,\ldots,N.\notag

\end{align}
\end{lemma}
\begin{proof}
Note that $0<\theta_2=256^{-4}<\theta_1<\frac18$
so that Lemmas \ref{lem:quant-embed}
and \ref{lem:difference-quotients} are applicable here. The first inequality
in \eqref{eq:difference-quotients} for $y:=x_+^i\in G_+^i\subset B_r(x_i)$ 
and $x_0:=
x_-^i\in G_-^i$ for an arbitrary fixed $i\in\{1,\ldots,N\}$ implies for
$\nu_i:=\nu_{B_r(x_i)}\in\S^{n-1}$ as in \eqref{eq:bmo3}, and
$\Delta_i:=\frac{\eta(x_+^i)-\eta(x_-^i)}{x_+^i-x_-^i}\in \overline{B_1(0)}
\subset\R^n$
\begin{equation}\label{eq:nuDelta}
|\nu_i-\Delta_i|^2=1+|\Delta_i|^2-2\langle\nu_i,\Delta_i\rangle_{\R^n}\le
2\big(1-\langle\nu_i,\Delta_i\rangle_{\R^n}\big)
\overset{\eqref{eq:difference-quotients}}{\le}
4\theta^\frac14.
\end{equation}
Therefore, by virtue of \eqref{eq:bmo2} in Lemma \ref{lem:quant-embed} for
$\nu:=\nu_i$, $x:=x_i$, and $z\in [x_-^i,x_+^i]\subset B_r(x_i)$,
\begin{eqnarray*}
|\eta(z)-\tilde{\eta}(z)|& 
= &\textstyle
|\eta(z)-\eta(x_-^i)+\tilde{\eta}(x_-^i)-\tilde{\eta}(z)|=\big|\int_{x_-^i}^z
\big(\eta'(u)-
\tilde{\eta}'(u)\big)du\big|\\
& = & 
\textstyle
 \big|\int_{x_-^i}^z\big(\eta'(u)-\Delta_i\big)du\big|\le
2r\mvint_{B_r(x_i)}\big(|\eta'(u)-\nu_i|+|\nu_i-\Delta_i|\big)du\\
& \le & 
\textstyle
 2r\big(\mvint_{B_r(x_i)}|\eta'(u)-\nu_i|^2 du\big)^\frac12+2r|\nu_i-\Delta_i|\\
 & \overset{\eqref{eq:bmo2},\eqref{eq:nuDelta}}{<} &
 \textstyle
 2r\big(\sqrt{32\theta}
 +\sqrt{4\theta^\frac14}\big)=2r\theta^\frac18\big(\sqrt{32}
 \theta^\frac38+2\big)<6\theta^\frac18 r,
\end{eqnarray*}
which proves the first inequality in \eqref{eq:linfty-dist-theta}, since
$z\in [x_-^i,x_+^i]$ was arbitrarily chosen as well as the index
$i\in\{1,\ldots,N\}$.

Before proving the second inequality in \eqref{eq:linfty-dist-theta} let us insert
an auxiliary result comparing the intrinsic distance on $\eta$ with that on 
$\tilde{\eta}$, which turns out to be useful later, too. As in some
proofs before, we
abbreviate the intrinsic distance $d_\eta(\eta(y),\eta(z))$ on $\eta$ as 
$d_\eta(y,z)$, analogously on the modified curve $\tilde{\eta}$.
\begin{lemma}[Comparison of intrinsic distances]
\label{lem:compare-intrinsic}
Under the assumptions of Lemma \ref{lem:harmonic-substitution} one has
\begin{equation}\label{eq:compare-intrinsic}
\frac78 d_\eta(y,z)<(1-2\theta^\frac18)d_\eta(y,z)\le d_{\tilde{\eta}}(y,z)\le d_\eta(y,z)\quad\Foa
y,z\in\R/\Z, y\ne z,
\end{equation}
and the length $\mathscr{L}(\tilde{\eta})$ of $\tilde{\eta}$ is contained in the
interval $[1-2\theta^\frac18 , 1]\subset [\frac78,1]$.
\end{lemma}
\begin{proof}
As in the previous proof we set $\Delta_i:=\frac{\eta(x_+^i)-\eta(x_-^i)}{x_+^i-x_-^i}
\in\overline{B_1(0)}\subset\R^n$ and $\nu_i:=\nu_{B_r(x_i)}\in\S^{n-1}$ 
as in \eqref{eq:bmo3},
for $i=1,\ldots,N$. Use \eqref{eq:nuDelta} to infer
$$
\big|1-|\Delta_i|\big|=\big||\nu_i|-|\Delta_i|\big|\le |\nu_i-\Delta_i|\overset{
\eqref{eq:nuDelta}}{\le}2\theta^\frac18,
$$
so that the tangent vector of the modified curve $\tilde{\eta}$ satisfies
\begin{equation}\label{eq:modified-speed}
|\tilde{\eta}'(z)|=
\begin{cases}
|\eta'(z)| =1 & \textnormal{f.a.e.\@ $z\in\R/\Z\setminus\bigcup_{i=1}^N(x_-^i,x_+^i),$}\\
|\Delta_i|\in [1-2\theta^\frac18,1] & \textnormal{for all $z\in (x_-^i,x_+^i),i=1,\ldots,
N.$}
\end{cases}
\end{equation}
Consequently, we can estimate the length of $\tilde{\eta}$ as
\begin{equation}\label{eq:modified-length}
\mathscr{L}(\tilde{\eta})=\textstyle
\int_0 ^1|\tilde{\eta}'(u)|du\in [1-2\theta^\frac18,1]\subset [\frac78,1].
\end{equation}
For the proof of \eqref{eq:compare-intrinsic} we may assume $0\le y<z<1$.
If $d_\eta(y,z)=\int_y^z|\eta'(u)|du$ then by  \eqref{eq:modified-speed},
$$
d_{\tilde{\eta}}(y,z)\le\textstyle
\int_y^z|\tilde{\eta}'(u)|du\overset{\eqref{eq:modified-speed}}{\le} d_\eta(y,z).
$$
If, on the other hand, $d_\eta(y,z)=1-\int_y^z|\eta'(u)|du=\int_z^{1+y}|\eta'(u)|du$,
then 
$$
\textstyle
d_{\tilde{\eta}}(y,z)\le\int_z^{1+y}|\tilde{\eta}'(u)|du
\overset{\eqref{eq:modified-speed}}{\le}d_\eta(y,z),
$$ 
which proves the right
inequality in \eqref{eq:compare-intrinsic}.

Similarly, if $d_{\tilde{\eta}}(y,z)=\int_y^z|\tilde{\eta}'(u)|du$, then
$$
\textstyle
d_{\tilde{\eta}}(y,z)\overset{\eqref{eq:modified-speed}}{\ge}(1-2\theta^\frac18)
|z-y|_{\R/\Z}\ge
(1-2\theta^\frac18)
d_\eta(y,z)>\frac78 d_\eta(y,z).
$$
If $d_{\tilde{\eta}}(y,z)=\mathscr{L}(\tilde{\eta})-\int_y^z|\tilde{\eta}'(u)|du=
\int_z^{1+y}|\tilde{\eta}'(u)|du$, then
\[
\textstyle
d_{\tilde{\eta}}(y,z)\overset{\eqref{eq:modified-speed}}{\ge}(1-2\theta^\frac18)
\int_z^{1+y}|\eta'(u)|du\ge (1-2\theta^\frac18)d_\eta(y,z)>
\frac78 d_\eta(y,z).\qedhere
\]
\end{proof}
Now we return to the

\noindent
{\it Proof of Lemma \ref{lem:harmonic-substitution}.}\,
It remains to establish the estimate for the distortion quotient in
\eqref{eq:linfty-dist-theta}. Fix $i\in\{1,\ldots,N\}$, abbreviate
$x:=x_i$, $x_\pm:=x_\pm^i$, and consider the intervals
$\mathcal{A}:=[x-r,x_-]$, $\mathcal{B}:=[x_-,x_+]$, and $\mathcal{C}:=[x_+,x+r]$.
If $y,z\in \mathcal{B}$ 
then $d_{\tilde{\eta}}(y,z)=|\tilde{\eta}(y)-\tilde{\eta}(z)|$ due to $r<\frac14$,
which implies the right inequality in \eqref{eq:linfty-dist-theta},
since
we are on the straight segment in that case. 

So, we distinguish two remaining cases:
\begin{enumerate}
\item[\rm I.] $(y,z)\in \mathcal{A}\times \mathcal{A},$ (or $(y,z)\in 
\mathcal{C}\times \mathcal{C}$),


\item[\rm II.]
$(y,z)\in \mathcal{A}\times \mathcal{B},$ (or $(y,z)\in 
\mathcal{B}\times \mathcal{C}$, or  $\mathcal{C}
\times \mathcal{B}$, or $\mathcal{B}\times \mathcal{A}$).
\end{enumerate}
It suffices in each case to treat the situation named first, the alternatives in brackets
can then be proved analogously.

\noindent
{\it Case I.}\,
For any $\zeta\in \mathcal{A}$ one has
\begin{align*}
|\zeta-x|&\textstyle
\ge |x_- - x|=|x_- -(x-\frac{r}2)+(x-\frac{r}2)-x|\ge\frac{r}2-|x_- -(x-\frac{r}2)|
 >\frac{r}2 -\frac{r}8=\frac38 r>\theta r,
\end{align*}
so that $\mathcal{A}
\subset A_{r,\theta}(x)=B_r(x)\setminus B_{\theta r}(x)$. Therefore, our
assumption \eqref{eq:fractional-seminorm-theta3} implies that we
can apply
Corollary 
\ref{cor:seminorm-bilip} to the interval  $I:=\mathcal{A}$, $\g:=\eta|_\mathcal{A}$,
to deduce from \eqref{eq:seminorm-bilip2} 
by definition \eqref{eq:modified-curve} of $\tilde{\eta}$
\begin{equation}\label{eq:dist-A}
\textstyle
\frac{d_{\tilde{\eta}}(y,z)}{|\tilde{\eta}(y)-\tilde{\eta}(z)|}
\overset{\eqref{eq:modified-curve}}{=}
\frac{d_{\eta}(y,z)}{|\eta(y)-\eta(z)|}
=\frac{|y-z|_{\R/\Z}}{|\eta(y)-\eta(z)|}
\overset{\eqref{eq:seminorm-bilip2}}{<}
\frac1{\sqrt{1-\frac{\theta}2}}<1+\theta^\frac14.
\end{equation}

\noindent
{\it Case II.}\,
For $(y,z)\in \mathcal{A}\times \mathcal{B}$ 
and $\nu:=\nu_{B_r(x)}\in\S^{n-1}$ as defined 
in \eqref{eq:bmo3} we infer from the definition \eqref{eq:modified-curve},
\eqref{eq:difference-quotients} of
Lemma \ref{lem:difference-quotients}, 
and \eqref{eq:compare-intrinsic} of Lemma
\ref{lem:compare-intrinsic}
\begin{align*}
\textstyle
|\tilde{\eta}(z)-\tilde{\eta}(y)|& 
\textstyle
\ge
\langle\tilde{\eta}(z)-\tilde{\eta}(y),\nu\rangle_{\R^n}=
\langle\tilde{\eta}(x_-)-\tilde{\eta}(y),\nu\rangle_{\R^n}+
\langle\tilde{\eta}(z)-\tilde{\eta}(x_-),\nu\rangle_{\R^n}\\
&\overset{\eqref{eq:modified-curve}}{=}\textstyle
\langle\tilde{\eta}(x_-)-\tilde{\eta}(y),\nu\rangle_{\R^n}+
\frac{z-x_-}{x_+-x_-}\langle\eta(x_+)-\eta(x_-),\nu\rangle_{\R^n}\\
&\overset{\eqref{eq:difference-quotients}}{\ge}
\textstyle
(1-2\theta^\frac14)\big[(x_--y)+(z-x_-)\big]=
(1-2\theta^\frac14)(z-y)\\
&\textstyle =(1-2\theta^\frac14)d_\eta(y,z)\overset{\eqref{eq:compare-intrinsic}}{\ge}(1-2\theta^\frac14)d_{\tilde{\eta}}(y,z),
\end{align*}
which implies
$$
\textstyle
\frac{d_{\tilde{\eta}}(y,z)}{|\tilde{\eta}(y)-\tilde{\eta}(z)|}
\le\frac1{1-2\theta^\frac14}=1+\frac{2\theta^\frac14}{1-2\theta^\frac14}<
1+4\theta^\frac14,
$$
because $0<\theta<\theta_2=256^{-4}.$
\end{proof}
Finally we show how to control the distortion quotient globally
under harmonic substitution, which may be reinterpreted as
controlling the bilipschitz constant of $\tilde{\eta}$ measured
in its intrinsic distance $d_{\tilde{\eta}}(\cdot,\cdot)$.
\begin{lemma}[Bilipschitz control under harmonic substitution]
\label{lem:bilip-control-harmonic}
Let $\eta\in W^{\frac32,2}(\R/\Z,\R^n)$ be an arclength parametrized
curve satisfying \eqref{eq:fractional-seminorm-theta3} for finitely
many distinct parameters $x_1,\ldots,x_N\in\R/\Z$ with
$r\in (0,\frac14)$ as in \eqref{eq:little-r} and $\theta\in (0,\theta_3]$,
where
\begin{equation}\label{eq:theta3}
\theta_3:=\frac1{4^{24}L^8}=\big(\frac1{64L}\big)^8,
\end{equation}
with $L\in [1,\infty)$ such that
\begin{equation}\label{eq:bilip-eta}
|\eta(y)-\eta(z)|\ge\frac1{L}|y-z|_{\R/\Z}\quad\Foa y,z\in\R/\Z.
\end{equation}
If $\tilde{\eta}$ is the modified curve obtained from $\eta$ by
harmonic substitution as in \eqref{eq:modified-curve}, then
there exists some number $\tilde{L}\in [L,2L]$ such that
\begin{equation}\label{eq:bilip-tilde-eta}
|\tilde{\eta}(y)-\tilde{\eta}(z)|\ge\frac1{\tilde{L}}d_{\tilde{\eta}}(y,z)
\quad\Foa y,z\in\R/\Z.
\end{equation}
\end{lemma}
\begin{proof}
Note that the smallness assumption \eqref{eq:theta3} implies
$0<\theta\le\theta_3<\theta_2=256^{-4}<\theta_1=144^{-4},$ so that
all previous lemmas in the present section are applicable. We
distinguish three (partly overlapping) cases:
\begin{enumerate}
\item[\rm I.] $y,z\in [x_i-r,x_+^i]$ (or $y,z\in [x^i_-,x_i+r]$) for some 
$i\in\{1,\ldots,N\}$,
\item[\rm II.] $y,z\in\R/\Z\setminus \bigcup_{i=1}^N[x_-^i,x_+^i],$
\item[\rm III.] $y\in [x_-^i,x_+^i]$, $z\in\R/\Z\setminus
[x_i-r,x_i+r]$ for some $i\in\{1,\ldots,N\}$.
\end{enumerate}
\noindent
{\it Case I.}\,
We apply \eqref{eq:linfty-dist-theta} of Lemma 
\ref{lem:harmonic-substitution} to deduce for $d_{\tilde{\eta}}(y,z)\equiv
d_{\tilde{\eta}}(\tilde{\eta}(y),\tilde{\eta}(z))$
\begin{equation}\label{eq:bilip-tilde1}
\textstyle
\frac{1024}{1025}d_{\tilde{\eta}}(y,z)\le
\frac{d_{\tilde{\eta}}(y,z)}{1+4\theta^\frac14}\overset{\eqref{eq:linfty-dist-theta}}{<}|\tilde{\eta}(y)-\tilde{\eta}(z)|\quad\Foa y,z\in [x_i-r,x_+^i]
(\textnormal{or $[x_-^i,x_i+r]$}).
\end{equation}
\noindent
{\it Case II.}\,
For $y,z\in\R/\Z\setminus \bigcup_{i=1}^N[x_-^i,x_+^i]$ we have by 
means of \eqref{eq:compare-intrinsic} $d_{\tilde{\eta}}(y,z)
\le d_\eta(y,z)$ and $|\tilde{\eta}(y)-\tilde{\eta}(z)|=|\eta(y)-\eta(z)|$,
so that by assumption \eqref{eq:bilip-eta} 
\begin{equation}\label{eq:bilip-tilde2}
\textstyle
\frac1{L}d_{\tilde{\eta}}(y,z)\le
\frac1{L}d_{\eta}(y,z)=\frac1{L}|y-z|_{\R/\Z}
\overset{\eqref{eq:bilip-eta}}{\le}
|\eta(y)-\eta(z)|=
|\tilde{\eta}(y)-\tilde{\eta}(z)|.
\end{equation}
\noindent
{\it Case III.}\,
For $y\in [x_-^i,x_+^i]$ and $z\notin [x_i-r,x_i+r]$ we find by
\eqref{eq:compare-intrinsic}, the first inequality in
\eqref{eq:linfty-dist-theta} of Lemma \ref{lem:harmonic-substitution},
and
assumptions \eqref{eq:bilip-eta} and \eqref{eq:theta3}
\begin{align}
\textstyle\frac{d_{\tilde{\eta}}(y,z)}{|\tilde{\eta}(y)-\tilde{\eta}(z)|}&
\textstyle
\stackrel{\eqref{eq:linfty-dist-theta}, \eqref{eq:compare-intrinsic}}{<}
\frac{d_{\eta}(y,z)}{|\eta(y)-\eta(z)|-12\theta^\frac18 r}=\big(
\frac{|\eta(y)-\eta(z)|}{|y-z|_{\R/\Z}}-\frac{12\theta^\frac18
r}{
|y-z|_{\R/\Z}}\big)^{-1}\overset{\eqref{eq:bilip-eta}}{<}
\big(\frac1{L}-\frac{12\theta^\frac18}{3/8}\big)^{-1}
\overset{\eqref{eq:theta3}}{\le}2L,
\end{align}
since $|y-z|_{\R/\Z}\ge |z-x|_{\R/\Z}-\max\{|x-x_-^i|,
|x-x_+^i|\}
>r-\frac58 r=\frac38 r.$
\end{proof}
