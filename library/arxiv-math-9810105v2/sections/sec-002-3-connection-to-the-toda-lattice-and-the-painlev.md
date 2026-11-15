---
doc_id: arxiv-math-9810105v2
doc_title: "arXiv:math/9810105v2 [math.CO] 26 Mar 1999"
section_id: sec-002-3-connection-to-the-toda-lattice-and-the-painlev
section_title: "Connection to the Toda Lattice and the Painlev'e III Equation"
section_number: 3
pages: 16-50
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.973
---
\label{s-TL}

In this Section, we discuss the connection of the RHP~\eqref{e-Y} 
for $\kappa^2_k$ and the RHP for the Toda lattice 
and the Painlev\'e III equation. 
In the RH context, the connection results from 
the specific form of the weight, $e^{\sqrt{\lambda}(z+z^{-1})}$. 
Connections can also be seen from the Toeplitz determinant/orthogonal 
polynomial point of view as in \cite{PS}, \cite{Hi} and \cite{Wi}.
The purpose of this short Section is purely to establish the 
various connection, but we do not use the results in the sequel.

\bigskip
Write $q=k+1$ in~\eqref{e-Y}.
We define 
\begin{equation}\label{e-sTL1}
   m^{TL}(z;q)=
   \begin{cases}
\biggl( \begin{smallmatrix} 0&-1\\1&0 \end{smallmatrix} \biggr) Y(z;q)
\biggl( \begin{smallmatrix} z^{-q}e^{\sqrt{\lambda}z^{-1}}&0\\
0&z^{q}e^{-\sqrt{\lambda}z^{-1}} \end{smallmatrix} \biggr)
\biggl( \begin{smallmatrix} 0&1\\-1&0 \end{smallmatrix} \biggr) \quad |z|>1,\\
\biggl( \begin{smallmatrix} 0&-1\\1&0 \end{smallmatrix} \biggr)Y(z;q)
\biggl( \begin{smallmatrix} e^{\sqrt{\lambda}z}&0\\
0&e^{-\sqrt{\lambda}z} \end{smallmatrix} \biggr) \quad |z|<1.
 \end{cases}
\end{equation}
A simple calculation shows that $m^{TL}$ solves the following RHP,
\begin{equation}\label{e-TL3}
  \begin{cases}
   &m^{TL}(z) \quad\text{is analytic in} \quad \C-\Sigma,\\
   &m^{TL}_+(z)=m^{TL}_-(z)\begin{pmatrix}
0&-z^{-q}e^{-\sqrt{\lambda}(z-z^{-1})}\\
z^{q}e^{\sqrt{\lambda}(z-z^{-1})}&1 \end{pmatrix}\\
   &m^{TL}(z)\to I \quad\text{as} \quad z\to\infty.
  \end{cases}
\end{equation}
Once again, the RHP for $Y$ is equivalent to the RHP for $m^{TL}$ 
in the sense that a solution of one problem yields a solution
of the other problem.

Recall that the RHP related to the Toda Lattice problem, for 
$-\infty<m<\infty$, 
\begin{equation}
  \begin{split}
     \frac{da_m}{dt}=2(b^2_{m}-b^2_{m-1})\\
     \frac{db_m}{dt}=b_{m}(a_{m+1}-a_{m}), 
  \end{split}
\end{equation}
under initial data decaying at infinity is the following (see,e.g.,\cite{Ka}).
Suppose that there are no solitons and denote the   
reflection coefficient by $r(z)$, $z\in\Sigma$.  
Then we find $Q(z)$ such that 
\begin{equation}
  \begin{cases}
     Q(z) \qquad\text{is analytic in $\C-\Sigma$}\\
     Q_+(z)=Q_-(z)\begin{pmatrix} 1-|r(z)|^2&-\bar{r}(z)z^{2m}e^{-t(z-z^{-1})}\\
r(z)z^{-2m}e^{t(z-z^{-1})}&1 \end{pmatrix}\\
     Q(z)\to I \qquad\text{as $z\to\infty$}.
  \end{cases}
\end{equation}
When $q$ is even, if we set $\sqrt{\lambda}=t$ and $q=-2m$ in~\eqref{e-TL3}, 
then the RHP is identical with the above RHP 
with $r(z)\equiv 1$.

For the connection to the Painlev\'e III equation, 
define 
\begin{equation}
  m^{PIII}(z)=
  \begin{cases}
     (-1)^qm^{TL}(z) &\quad |z|<1,\\
     m^{TL}(z) &\quad |z|>1.
  \end{cases}
\end{equation}
Note in~\eqref{e-TL3}, 
\begin{equation}
   (-1)^q\negthickspace\begin{pmatrix}
0\negthickspace&\negthickspace-z^{-q}e^{-\sqrt{\lambda}(z-z^{-1})}\\
z^{q}e^{\sqrt{\lambda}(z-z^{-1})}&1 \end{pmatrix}\negthickspace
= \negthickspace(-1)^qe^{-\frac{\sqrt{\lambda}}2(z-z^{-1})ad\sigma_3}z^{-\frac{q}2ad\sigma_3}  
\negthickspace\begin{pmatrix} 1&1\\-1&0 \end{pmatrix} ^{-1}
\end{equation}
where $z^{\frac{q}2}$ is analytic in 
$\C-(-\infty,0]$ and real-valued for real $z$.
If we set $\sqrt{\lambda}=-ix$, then
this is the same RHP for the particular  
Painlev\'e III equation (see \cite{FMZ} for results and notations)
\begin{equation*}
   u_{xx}=\frac{u_x^2}{u}-\frac1{x}u_x
+\frac1{x}\bigl( -4qu^2+4(1-q)\bigr) +4u^3+\frac{-4}{u}
\end{equation*}
with monodromy data 
\begin{equation*}
  \begin{split}
    &\theta_{\infty}=-\theta_0=q,\\
    &a_0=b_0=a_{\infty}=b_{\infty}=0,\\
    &E=\bigl( \begin{smallmatrix} 1&1\\-1&0 \end{smallmatrix} \bigr).
  \end{split}
\end{equation*}

In the RHP~\eqref{e-Y}, we are interested directly in the quantity 
$-Y_{21}(0;k+1,\lambda)$, or by~\eqref{e-sTL1}, $m^{TL}_{11}(0;q)$. 
On the other hand, for the Toda lattice and the PIII equation, one is 
interested in quantities other than $m^{TL}_{11}(0;q)$ which are 
related to the respective RHP's. 
For example, the solution $u(x)$ of PIII equation is given by 
$u(x)=-ix(m^{PIII}_1)_{12}$ where $m^{PIII}=I+\frac{m^{PIII}_1}{z}
+O(\frac1{z})$, which is clearly different from $(-1)^qm^{PIII}_{11}(0;q)$.
However, the importance of the connection of~\eqref{e-Y} to the RHP's 
for Toda lattice and the PIII equation lies precisely in the fact that 
$(a_m,b_m)$ (resp., $u(x)$) solve differential-difference 
(resp., differential) equations which in turn imply that the coefficients  
of the generating function $\phi_n(\lambda)$, $2\sqrt{\lambda}=-ix$, 
must satisfy a certain class of identities. 
We plan to investigate these relations in a later publication.

Finally, note that for PIII, the interesting asymptotic question is 
to evaluate the limit $x=i\sqrt{\lambda}\to\infty$, with $q$ fixed. 
In this paper, as in the Toda lattice, we are interested in the double 
limit when $\lambda\to\infty$ and $q$ is allowed to vary 
(note that in \cite{Ka}, the singular case $r(z)\equiv 1$ is not 
considered). 
When $\lambda\to\infty$, $\frac{2\sqrt{\lambda}}{q}\sim 1$, 
we are in a region where the solution of PIII equation degenerates 
to a solution of PII equation, and this explains the appearance of 
PII in the parametrix for the solution of $Y$ of the RHP~\eqref{e-Y}. 





\section{{\bf Equilibrium Measure and $g$-function}}
\label{s- Begin}

In this Section, the equilibrium measure is explicitly calculated 
for each $\gamma>0$ (Lemma~\ref{lem-ourg}) and, using this equilibrium measure, 
the $g$-function~\eqref{4.8} is introduced in order to 
convert the RHP~\eqref{e-Y} 
into a RHP which is normalized to be $I$ at $\infty$.

\bigskip
Let $\Sigma$ denote the unit circle oriented counterclockwise 
and $f(e^{i\theta})=f(z)$ be a non-negative, periodic, smooth  
function on $\Sigma$.
Let $p_q(z)=\kappa_qz^q+\cdots$ be the $q$-th normalized orthogonal 
polynomial with respect to the weight 
$f(e^{i\theta})\frac{d\theta}{2\pi}$ on the unit circle.
Define the polynomial $p_q^{*}(z)\equiv z^q\bar{p}_q(1/z)
=z^q\overline{p_q(1/\bar{z})}$ (see \cite{Sz}).
We consider the following RHP : 
Let $Y(z)$ be the $2\times 2$ matrix-valued function satisfying 
\begin{equation}\label{e-beg1}
  \begin{cases}
    Y(z) \qquad  \text{is analytic in} \quad  \C -\Sigma,\\
    Y_+(z)=Y_-(z)\begin{pmatrix}1&\frac{1}{z^{k+1}}f(z)\\0&1
\end{pmatrix} \quad\text{on} \quad  \Sigma,\\
    Y(z)z^{-(k+1)\sigma_3}=I+O(\frac1z) \quad\text{as} \quad z\rightarrow \infty.
  \end{cases}
\end{equation}
The following Lemma is the starting point of our calculations.
\begin{lem}\label{lem-exi}
  (cf. \cite{FIK}, \cite{DKMVZ}) The RHP~\eqref{e-beg1} has a unique solution
  \begin{equation*}
    Y(z)=\begin{pmatrix}
    \frac1{\kappa_{k+1}}p_{k+1}(z)& \frac1{\kappa_{k+1}}
\int_{\Sigma}\frac{p_{k+1}(s)}{s-z}\frac{f(s)ds}{2\pi i s^{k+1}}\\
    -\kappa_{k}p^{*}_{k}(z)& -\kappa_{k}
\int_{\Sigma}\frac{p^{*}_{k}(s)}{s-z}\frac{f(s)ds}{2\pi i s^{k+1}}
       \end{pmatrix}.
  \end{equation*}
\end{lem}
\begin{proof}
  Existence : Using the property of Cauchy operator $C_+-C_-=I$, where
$Ch(z)\equiv\int_{\Sigma} \frac{h(s)}{s-z} ds$,
it is a straightforward calculation
to show that the above expression for $Y$ satisfies the jump condition.
The asymptotics at $\infty$ codes in precisely the fact that the $p_k's$ 
are the normalized orthogonal polynomials for the weight 
$f(e^{i\theta})d\theta$. 

  Uniqueness : Suppose that there is another solution $\tilde{Y}$ of RHP. Noting

$det \biggl( \begin{smallmatrix} 1&\frac{1}{z^{k+1}}f(z)\\0&1
\end{smallmatrix} \biggr) =1$, we have that $\det \tilde{Y}$ is entire, 
and $\to 1$
as $z\to\infty$. Therefore by Liouville's theorem, $\det \tilde{Y}\equiv 1$.
In particular, $\tilde{Y}$ is invertible.
Now set $Z=Y\tilde{Y}^{-1}$. Then it has no jump on $\Sigma$ 
hence is entire. 
Also, $Z\to I$ as $z\to\infty$, and therefore $Z\equiv I$.
\end{proof}
From this Lemma,  we have
\begin{equation}
  \kappa^2_{k}=-Y_{21}(0)
\end{equation}
Therefore the RHP~\eqref{e-Y} has a unique solution 
and~\eqref{e-Y21} is verified.


\bigskip
Again set $q=k+1$ and 
\begin{equation}
  \gamma=\frac{2\sqrt{\lambda}}{q}.
\end{equation}
We are interested in the case when $q$ and $2\sqrt{\lambda}$ 
are of the same order
, or more precisely, $\gamma\to 1$.
In this Section, and also in Sections~\ref{s-K1} and~\ref{s-K2}, we consider 
the RHP~\eqref{e-Y} with parameter $\gamma$ and $q$, 
\begin{equation}\label{RHP-Y}
  \begin{cases}
     Y(z;q) \quad \text{analytic in} \quad  \C -\Sigma,\\
     Y_+(z;q)=Y_-(z;q)
\begin{pmatrix}1&\frac{1}{z^q}e^{\frac{q\gamma}{2}(z+z^{-1})}\\0&1
\end{pmatrix} \quad\text{on}\quad \Sigma,\\
     Y(z;q)=\bigl( I+O(\frac1z) \bigr)z^{q\sigma_3} 
\quad\text{as}\quad z\rightarrow \infty,
  \end{cases}
\end{equation}
rather than $\lambda$ and $q$.
With $\gamma$ fixed, the RHP~\eqref{RHP-Y} is of the Plancherel-Rotach type  
with \emph{varying} exponential weight 
$e^{\frac{q\gamma}{2}(z+z^{-1})}$ on the unit circle 
(see \cite{Sz}, \cite{DKMVZ}).
Similar problem on the real line is analyzed in \cite{DKMVZ} 
without double scaling limit ($\gamma$ is kept fixed).
Our goal is to find the large $q$ behavior of $Y_{21}(0;q)$ for all $\gamma > 0$.
\begin{figure}[ht]
 \centerline{\epsfig{file=branch.eps, width=6cm}}
 \caption{branch cut of $\log (z-e^{i\theta})$}\label{fig-branch}
\end{figure}

Let $d\mu(s)$ be a probability measure on the unit circle.
Define 
\begin{equation}
  g(z) \equiv \int_{\Sigma}\log (z-s) d\mu(s)
\end{equation}
where for each $\theta$, the branch is chosen such that $\log(z-e^{i\theta})$
is analytic in $\C-(-\infty,-1]\cup \{ e^{it}:-\pi\le t\le\theta \}$
 (see Figure ~\ref{fig-branch})
and $\log(z-e^{i\theta}) \sim \log{z}$ for real $z\to\infty$.
The following Lemma is based on related calculations in \cite{DKM}.
\begin{lem}\label{lem-gfun}
Suppose $d\mu(z)=u(\theta) d\theta$ is an absolutely continuous probability 
measure on the unit circle and $u(\theta)=u(-\theta)$. 
Then $g(z)$ has the following properties : 
\begin{enumerate}
\item $g$ is analytic in $\C -\Sigma\cup (-\infty ,-1).$
\item On $(-\infty ,-1), g_+(z)-g_-(z)=2\pi i.$
\item $g(z)=\log z+O(\frac1z)$  as  $z\rightarrow \infty.$
\item $e^{qg(z)}$ is analytic in $\C-\Sigma.$
\item $e^{qg(z)}=z^q( 1+O(\frac1z))$ as $z\rightarrow \infty.$
\item $g(0)= \pi i.$
\item $g_+(z)+g_-(z)=2\int_{-\pi}^{\pi}\log |z-s| d\mu(s)
      + i(\phi +\pi)$ on $z\in\Sigma$  where $\phi=arg(z).$
\item $g_+(z)-g_-(z)=2\pi i\int_{\phi}^{\pi} d\mu(s)$ on z$\in\Sigma.$
\end{enumerate}
\end{lem} 

\begin{proof}
  (i)-(v) are trivial. 
For (vi), 
$$g(0)=\int_{-\pi}^{\pi} \log{(0-e^{i\theta})} u(\theta)d\theta
=\int_{-\pi}^{\pi} i(\theta+\pi) u(\theta)d\theta = \pi i$$
using the evenness of $u(\theta)$.

For (vii), fix $z=e^{i\phi}\in\Sigma$. 
Then $arg(z-e^{i\theta})$ is analytic if $-\pi<\theta<\phi$ and 
  \begin{equation*}
    \begin{split}
      g_+(z)&=\int_{-\pi}^{\pi}\log |z-e^{i\theta}| d\mu(z)
+i\int_{-\pi}^{\phi} arg(z-e^{i\theta}) d\mu(z)
+i\int_{\phi}^{\pi} arg_+(z-e^{i\theta}) d\mu(z),\\
      g_-(z)&=\int_{-\pi}^{\pi}\log |z-e^{i\theta}| d\mu(z)
+i\int_{-\pi}^{\phi} arg(z-e^{i\theta}) d\mu(z)
+i\int_{\phi}^{\pi} arg_-(z-e^{i\theta}) d\mu(z).
    \end{split}
  \end{equation*}
  Note that for $\phi <\theta <\pi$, 
$$arg_+(e^{i\phi}-e^{i\theta}) - arg_-(e^{i\phi}-e^{i\theta}) = 2\pi.$$
  This yields
$$g_+(z)+g_-(z)=2\int_{-\pi}^{\pi}\log |z-e^{i\theta}| d\mu(z)
+2i\int_{-\pi}^{\pi}arg_+(e^{i\phi}-e^{i\theta}) d\mu(z)
-i\int_{\phi}^{\pi} 2\pi d\mu(z).$$
  Set 
$$F(\phi)=2\int_{-\pi}^{\phi} arg(e^{i\phi}-e^{i\theta}) d\mu(z)
+2\int_{\phi}^{\pi} arg_+(e^{i\phi}-e^{i\theta}) d\mu(z)
-2\pi\int_{\phi}^{\pi} d\mu(z) -\phi$$
  If we show $F(\phi)\equiv\pi$, then (vii) is proved.
  Note that (a) $arg(e^{i\phi}-e^{i\phi_-})=\phi+\frac{\pi}2$, 
(b) $arg_+(e^{i\phi}-e^{i\phi_+})=\phi+\frac{3\pi}2$ and 
(c) $\frac{d}{d\phi} arg(e^{i\phi}-e^{i\theta}) \equiv \frac12$.
  This gives us $F'(\phi)=2arg(e^{i\phi}-e^{i\phi_-})u(\phi)-2arg_+(e^{i\phi}-e^{i\phi_+})u(\phi)+2\pi u(\phi) \equiv 0$. But $F(\pi)=\pi$. Therefore $F(\phi)\equiv\pi$

  For (viii), 
  \begin{equation*}
    \begin{split}
      g_+(z)-g_-(z)&=i\int_{\phi}^{\pi}
[arg_+(e^{i\phi}-e^{i\theta}) - arg_-(e^{i\phi}-e^{i\theta})] d\mu(z)\\
      &=i\int_{\phi}^{\pi} 2\pi d\mu(z).
    \end{split}
  \end{equation*}
\end{proof}


\bigskip
Let $M$ be the set of probability measures on $\Sigma$.
The equilibrium measure $d\mu_V(z)$ for potential $V(z)=-\frac{\gamma}2(z+z^{-1})$
on the unit circle is defined by the following minimization problem,
\begin{equation}
   \inf_{\mu\in M} \iint_{\Sigma\times\Sigma} \log|z-w|^{-1} d\mu(z) d\mu(w)
+ \int_{\Sigma} V(z) d\mu(z).
\end{equation}
The infimum is achieved uniquely (see, e.g. \cite{ST}) at the 
equilibrium measure.
Let $J$ denote the support of $d\mu_V$.
The equilibrium measure and its support are uniquely determined 
by the following Euler-Lagrange variational conditions :
\begin{equation}\label{e-varicon}
  \begin{split}
  &\text{there exits a real constant $l$ such that},\\
  &\quad 2\int_{\Sigma} \log{|z-s|}d\mu_V(s) - V(z)+l=0 \ \ \text{for $z\in \bar{J}$},\\
  &\quad 2\int_{\Sigma} \log{|z-s|}d\mu_V(s) - V(z)+l \le 0 \ \
\text{for $z\in\Sigma -\bar{J}$}.
  \end{split}
\end{equation}
In Lemma ~\ref{lem-ourg} below, we find $d\mu_V$,
its support and $l$ explicitly from this variational condition 
with the aid of Lemma ~\ref{lem-gfun}.
Let 
\begin{equation}\label{4.8}
  g(z)=g_V(z) \equiv \int_{\Sigma}\log (z-s) d\mu_V(s)
\end{equation}
where $d\mu_V$ is the equilibrium measure.
Following \cite{DKMVZ}, we define 
$$\m1 \equiv 
e^{\frac{ql}{2}\sigma_3}Y(z)e^{-qg(z)\sigma_3} e^{-\frac{ql}{2}\sigma_3}.$$
Then $m^{(1)}$ solves the following new RHP,
\begin{equation}\label{e-m1orig}
  \begin{cases} 
    \m1 \qquad\text{is analytic in}\quad \C-\Sigma,\\
    \mpl1 = \mni1 v^{(1)} \quad\text{on}\quad\Sigma,\\
    \m1=I+O(\frac1z) \quad\text{as}\quad z\rightarrow \infty
  \end{cases}
\end{equation}
where $v^{(1)}=\begin{pmatrix} e^{q(g_--g_+)}& 
\frac{1}{z^q}e^{q(g_++g_--V+l)}\\
0& e^{q(g_+-g_-)} \end{pmatrix}$, 
and 
\begin{equation}\label{e-Korig}
   \kappa^2_{q-1}=-Y_{21}(0;q)=-m_{21}^{(1)}(0)e^{ql}e^{qg(0)}
=-(-1)^qm^{(1)}_{21}(0)e^{ql},
\end{equation}
from Lemma~\ref{lem-gfun} (vi).

Once again we note that this RHP for $m^{(1)}$ is equivalent to 
the RHP for $Y$ in the sense that 
a solution of one RHP yields a solution of the other RHP, and vice versa.
Using Lemma ~\ref{lem-gfun}, the jump matrix $v^{(1)}$ is given by 
\begin{equation}\label{e-Omega}
  \begin{cases}
    \text{inside the support of $d\mu_V$},\\
    \qquad\begin{pmatrix} e^{-2q\pi i\int_{\phi}^{\pi} d\mu_V(\theta)}& (-1)^q\\
          0& e^{2q\pi i\int_{\phi}^{\pi} d\mu_V(\theta)} \end{pmatrix}.\\
    \text{outside the support of $d\mu_V$}, \\
    \qquad\begin{pmatrix} e^{-2q\pi i\int_{\phi}^{\pi} d\mu_V(\theta)}& 
(-1)^qe^{q\bigl[ 2\int_{-\pi}^{\pi}\log |z-e^{i\theta}| d\mu_V(\theta) 
-V(z)+l\bigr] }\\
0&e^{2q\pi i\int_{\phi}^{\pi} d\mu_V(\theta)} \end{pmatrix}.
  \end{cases}
\end{equation}
As indicated in the Introduction, the purpose of the $g$-function is to 
turn exponentially growing terms in the jump matrix for the RHP,  
into oscillatory or exponentially decaying terms : this can be seen 
explicitly in~\eqref{e-Omega}, using~\eqref{e-varicon}.


\bigskip
We have explicit formulae for the equilibrium measure and $l$.
For $0<\gamma\leq 1$, the equilibrium measure has the whole circle 
as its support but for $\gamma > 1$, a gap opens up. 
See, also \cite{GW} and \cite{Johan}.

Notation : $\chi_B(\theta)$ denotes the indicator function of the set 
$B\subset\Sigma$.

\begin{lem}\label{lem-ourg}
For the weight $V(z)=-\frac{\gamma}{2}(z+z^{-1})$, the equilibrium measure and $l$ are given as follows : 
\begin{enumerate}
\item If $0\leq \gamma \leq 1$, then
\begin{equation}\label{e-lem4.3.1} 
  d\mu_V(\theta)=\frac{1}{2\pi}(1+\gamma \cos{\theta}) d\theta
\end{equation}
and $l=0$.
\item If $\gamma > 1$, then
\begin{equation}\label{e-lem4.3.2}
  d\mu_V(\theta)=\frac{\gamma}{\pi} \cos(\frac{\theta}{2})
      \sqrt{\frac{1}{\gamma} - \sin^2(\frac{\theta}{2})} 
\chi_{[-\theta_c, \theta_c]}(\theta) d\theta
\end{equation}
and 
\begin{equation}\label{e-lem4.3.3}
  l=-\gamma +\log\gamma +1,
\end{equation}
      where $\sin^2\frac{\theta_c}{2}=\frac{1}{\gamma}, 0< \theta_c<\pi$. 
In this case, the inequality in the variational 
condition ~\eqref{e-varicon} is strict.
\end{enumerate}
\end{lem}

\begin{proof}
  (i) First, it is easy to check that $d\mu_V(\theta)$ defined above 
in~\eqref{e-lem4.3.1} is a positive probability measure. We set 
    $$g(z)=\int_{-\pi}^{\pi}\log (z-e^{i\theta})\frac{1}{2\pi}(1+\gamma \cos{\theta}) d\theta.$$
  Then $$g'(z)=\frac1{2\pi i} \int_{\Sigma} \frac1{z-s}(1+\frac{\gamma}2(s+s^{-1}))\frac{ds}{s}.$$
  Using a residue calculation with $g(z)=\log{z}+O(\frac1{z})$ as 
$z\to\infty$ and $g(0)=\frac1{2\pi} \int_{-\pi}^{\pi} 
\log{e^{i(\theta+\pi)}}(1+\gamma\cos{\theta})d\theta=\pi i$, we have
  \begin{equation}\label{e-g1} g(z)=
    \begin{cases}
      \log{z}-\frac{\gamma}{2z}& |z|>1, z\notin (-\infty,-1),\\
      -\frac{\gamma}2 z+\pi i& |z|<1.
    \end{cases}
  \end{equation}
  Therefore we have $$g_+(z)+g_-(z)=\log{z}-\frac{\gamma}2(z+z^{-1})+\pi i.$$
  From Lemma ~\ref{lem-gfun} (vii), we have
  $$2\int_{-\pi}^{\pi}\log |z-e^{i\theta}| \frac1{2\pi} 
(1+\gamma\cos{\theta}) d\theta +\frac{\gamma}2(z+z^{-1}) = 0$$
  for any $z=e^{i\phi}$ with $l=0$ as $\log{z}=i\phi$.

  (ii) It is straightforward to check that the above 
measure~\eqref{e-lem4.3.2} is 
a positive probability measure.
For $g(z)$ defined in as before, we have
  \begin{equation*}
    \begin{split}
      g'(z)&= \int_{-\theta_c}^{\theta_c} \frac1{z-e^{i\theta}} 
\frac{\gamma}{\pi} \cos(\frac{\theta}{2}) 
\sqrt{\frac1{\gamma}-\sin^2\frac{\theta}{2}} d\theta \\
      &= \frac{\gamma}{4\pi i} \int_{-\theta_c}^{\theta_c} 
\frac1{z-s}
\frac{s+1}{s^2} \sqrt{(s-\xi)(s-\bar{\xi})} ds
    \end{split}
  \end{equation*}
  where $\xi=e^{i\theta_c}$, and the branch is chosen to be analytic in 
$\C-\{ e^{i\theta} : \theta_c\le |\theta| \le \pi \}$ 
and $\sqrt{(s-\xi)(s-\bar{\xi})}>0$ for real $s>>0$. 
From a residue calculation, we obtain
  $$g'(z)= \frac1{2z}-\frac{\gamma}4(1-z^{-2}) +\frac{\gamma}4\frac{z+1}{z^2}\sqrt{(z-\xi)(z-\bar{\xi})}.$$
  Integrating, we have for $|z|>1$, $z\notin (-\infty,-1)$, 
  \begin{equation*}
    g(z)=\frac12\log{z} -\frac{\gamma}{4} (z+z^{-1}) +\frac{\gamma}2
    +\frac{\gamma i}4 \int_{1_{+0}}^{z} \frac{s+1}{s}\sqrt{(s-\xi)(s-\bar{\xi})}
    \frac{ds}{si} +g_-(1)
  \end{equation*}
and for $|z|<1$, $z\notin (-1,0]$,
  \begin{equation*}
    g(z)=\frac12\log{z} -\frac{\gamma}{4} (z+z^{-1}) +\frac{\gamma}2
    +\frac{\gamma i}4 \int_{1_{-0}}^{z} \frac{s+1}{s}\sqrt{(s-\xi)(s-\bar{\xi})}
    \frac{ds}{si} +g_+(1)
  \end{equation*}
 where $g_+$, $g_-$ denote the limit from inside and outside each and 
$1_{+0}$, $1_{-0}$ denote the outside and inside limits.

  (a) For $|\phi| \le \theta_c$,
  \begin{equation*}
    g_+(z)+g_-(z)=\log{z} -\frac{\gamma}2(z+z^{-1}) +\gamma +g_+(1)+g_-(1)
  \end{equation*}
  From Lemma ~\ref{lem-gfun} (vii), we obtain 
  \begin{equation*} 
    \begin{split}
      g_+(1)+g_-(1)&= 2\int_{-\theta_c}^{\theta_c} \log|1-e^{i\theta}| 
\frac{\gamma}{\pi} \cos{\frac{\theta}2} \sqrt{\frac1{\gamma} 
-\sin^2 \frac{\theta}2} d\theta +i(0+\pi)\\
      &= \frac{4\gamma}{\pi} \int_{0}^{\theta_c} \log(2|\sin{\frac{\theta}2}|)
\cos{\frac{\theta}2} \sqrt{\frac1{\gamma} -\sin^2 \frac{\theta}2} d\theta +\pi i\\
      &= 2\log{2} -\log{\gamma} +\frac8{\pi} \int_{0}^{\frac{\pi}2}
\log(\sin{\theta}) \cos^2 \theta d\theta +\pi i\\
      &= 2\log{2} -\log{\gamma} -1 +\frac4{\pi} \int_{0}^{\frac{\pi}2}
\log(\sin{\theta}) d\theta +\pi i,
    \end{split}
  \end{equation*}
 after simple change of variables and integration by parts.
  But we have $\int_{0}^{\frac{\pi}2} \log(\sin{\theta}) d\theta 
= -\frac{\pi}2 \log{2}$ from
   \begin{equation*}  
    \begin{split}
      2\int_{0}^{\frac{\pi}2} \log(\sin{\theta}) d\theta 
      &= \int_{0}^{\frac{\pi}2} \log(\sin{\theta}) d\theta 
+ \int_{0}^{\frac{\pi}2} \log(\cos{\theta}) d\theta \\
      &= \int_{0}^{\frac{\pi}2} \log(\frac12 \sin{2\theta}) d\theta \\
      &=-\frac{\pi}2 \log{2} 
+ \int_{0}^{\frac{\pi}4} \log(\sin{2\theta}) d\theta 
+ \int_{\frac{\pi}4}^{\frac{\pi}2} \log(\sin{2\theta}) d\theta \\
      &=-\frac{\pi}2 \log{2} +\int_{0}^{\frac{\pi}2} \log(\sin{\theta}) d\theta.
    \end{split}
  \end{equation*}
  Therefore  
$$g_+(z)+g_-(z)=\log{z} -\frac{\gamma}2(z+z^{-1})+\gamma-\log{\gamma}-1+\pi i.$$
  From Lemma ~\ref{lem-gfun} (vii), we obtain the desired result 
for $|\phi| \le \theta_c$, $z=e^{i\phi}$,
  \begin{equation*}
    2\int_{-\pi}^{\pi}\log |z-e^{i\theta}| d\mu_V(\theta)
+ \frac{\gamma}2(z+z^{-1}) -\gamma +\log\gamma +1 =0.
  \end{equation*}

  (b) for $\theta_c <\phi <\pi$ ($-\pi <\phi <-\theta_c$ case is similar),
  \begin{equation*}
    \begin{split}
      g_+(z)+g_-(z)&= \log{z} -\frac{\gamma}2(z+z^{-1}) +g_+(1)+g_-(1)\\
      &\qquad +\frac{\gamma}2 \int_{\theta_c}^{\phi} \frac{s+1}{s^2}\sqrt{(s-\xi)(s-\bar{\xi})} ds.
    \end{split}
  \end{equation*}
  But 
$$\frac{\gamma}2 \int_{\theta_c}^{\phi} \frac{s+1}{s^2}\sqrt{(s-\xi)(s-\bar{\xi})} ds = -\frac{\gamma}2 \int_{\theta_c}^{\phi} \cos{\frac{\theta}2} \sqrt{\sin^2 \frac{\theta}2 -\frac1{\gamma}} d\theta < 0.$$
  Therefore, using Lemma ~\ref{lem-gfun} (vii) and 
calculations in (a), we obtain for $|\phi|>\theta_c$,
  \begin{equation*}
    2\int_{-\pi}^{\pi}\log |z-e^{i\theta}| d\mu_V(\theta)
+ \frac{\gamma}2(z+z^{-1}) -\gamma +\log\gamma +1 <0.
  \end{equation*}
\end{proof}

In the following Sections, we distinguish the two cases, 
$\gamma\le1$ and $\gamma>1$, 
due to the difference of the supports of their equilibrium measures.





\section{$\mathbf{ 0\leq \gamma \le 1}$}
\label{s-K1}

From ~\eqref{e-g1}, we have the explicit formula for the $g$-function :
\begin{equation*}  g(z)=
    \begin{cases}
      \log{z}-\frac{\gamma}{2z}& |z|>1, z\notin (-\infty,-1)\\
      -\frac{\gamma}2 z+\pi i& |z|<1.
    \end{cases}
\end{equation*}
With this $g$, $l=0$ from Lemma~\ref{lem-ourg} (i), and our 
RHP ~\eqref{e-m1orig},  
or equivalently ~\eqref{e-Omega}, becomes
\begin{equation}
\begin{cases}
m^{(1)} \ \ \text{analytic in} \ \ \C-\Sigma,\\
m_+^{(1)}= m_-^{(1)} \begin{pmatrix} (-1)^qz^qe^{\frac{q\gamma}{2}(z-z^{-1})}& (-1)^q\\
                              0& (-1)^qz^{-q}e^{\frac{-q\gamma}{2}(z-z^{-1})}
              \end{pmatrix} \ \ \text{on} \ \  \Sigma,\\
m^{(1)}=I+O(\frac1z) \ \ \text{as} \ \  z\rightarrow \infty\\
\end{cases}
\end{equation}
and $\kappa^2_{q-1}=-(-1)^qm_{21}^{(1)}(0)$ from ~\eqref{e-Korig}.\\
We define $m^{(2)}$ in terms of $m^{(1)}$ as follows :
\begin{equation}\label{e-conju}
 \begin{split}
  &\text{for even $q$,} \\
  &\quad \begin{cases}
    m^{(2)} \equiv m^{(1)}& \quad |z|>1,\\ 
    m^{(2)} \equiv m^{(1)} \bigl( \begin{smallmatrix} 0& -1\\ 1&0 
\end{smallmatrix} \bigr)& \quad |z|<1. \end{cases}\\
  &\text{for odd $q$,}\\
  &\quad\begin{cases}
    m^{(2)} \equiv \bigl( \begin{smallmatrix} 1&0\\0&-1 
\end{smallmatrix} \bigr)  m^{(1)} \bigl( 
\begin{smallmatrix} 1&0\\0&-1 \end{smallmatrix} \bigr)& \quad |z|>1,\\
    m^{(2)} \equiv \bigl( \begin{smallmatrix} 1&0\\0&-1 
\end{smallmatrix} \bigr) m^{(1)} \bigl( 
\begin{smallmatrix} 0&-1\\-1&0 \end{smallmatrix} \bigr)& 
\quad |z|<1. \end{cases}
 \end{split}
\end{equation}
Then we have a new equivalent RHP
\begin{equation}
\begin{cases}
m^{(2)}_+=m^{(2)}_- v^{(2)}\quad\text{on} \quad\Sigma,\\
m^{(2)}=I+O(\frac1z) \ \ \text{as}\ \ z\rightarrow \infty\\
\end{cases}
\end{equation}
where $v^{(2)}= \begin{pmatrix} 
1& -(-1)^qz^qe^{\frac{q\gamma}{2}(z-z^{-1})} \\
(-1)^qz^{-q}e^{\frac{-q\gamma}{2}(z-z^{-1})}&0 \end{pmatrix}$ 
and $\kappa^2_{q-1}=m_{22}^{(2)}(0)$. \\

\begin{figure}[ht]
 \centerline{\epsfig{file=gammale1.eps, width=6cm}}
 \caption{$\Sigma^{(3)}$ and $\Omega^{(3)}$}\label{fig-ga<1}
\end{figure}
Introduce $\Sigma^{(3)}=\Sigma^{(3)}(\gamma)=\Sigma^{(3)}_{in}\cup\Sigma^
{(3)}_{out}$ (see Figure~\ref{fig-ga<1}) as follows.
For fixed $\pi/2 <|\theta|\le\pi$, 
\begin{equation}\label{e-z8}
  F(\rho)\equiv F(\rho,\theta)=
  Re\bigl( \frac{\gamma}2(z-z^{-1})+\log{z} \bigr)
  =\frac{\gamma}2 (\rho-\rho^{-1})\cos{\theta}+\log{\rho}, 
\end{equation}
where $z=\rho e^{i\theta}$, $0<\rho\le 1$, has the minimum at  
\begin{equation}\label{e-z9}
  \rho=\rho_{\theta}\equiv \frac{1-\sqrt{1-\gamma^2\cos^2 \theta}}
  {-\gamma\cos{\theta}}
\end{equation}
and 
$F(\rho_{\theta})<0$. 
( Note that $\rho_{\theta}<0$ for $|\theta|<\pi/2$. )
For $\frac12\le\gamma\le1$, we take 
\begin{equation}\label{e-Sig}
  \begin{split}
   &\Sigma^{(3)}_{in}=\{\rho_{\theta}e^{i\theta} : 
3\pi/4 \le |\theta|\le\pi \} \cup\{\rho_{3\pi/4}e^{i\theta} : 
|\theta|\le 3\pi/4 \},\\
   &\Sigma^{(3)}_{out}=\{\rho_{\theta}^{-1}e^{i\theta} :
3\pi/4 \le |\theta|\le\pi \} \cup\{\rho_{3\pi/4}^{-1}e^{i\theta} : 
|\theta|\le 3\pi/4 \}.
  \end{split}
\end{equation}
Orient $\Sigma^{(3)}$ as in Figure~\ref{fig-ga<1}. 
And finally, for $0\le\gamma\le\frac12$, set 
$\Sigma^{(3)}(\gamma)=\Sigma^{(3)}(\frac12)$.

Of course, $\Sigma^{(3)}$ varies with $\gamma\in [0,1]$. 
However, using estimates from \cite{GK}, it is not difficult to 
show that the Cauchy operators $C_\pm$ on $L^2(\Sigma^{(3)})$ 
are uniformly bounded, 
\begin{equation}\label{e-Cau}
   \|C_\pm \|_{L^2(\Sigma^{(3)})\to L^2(\Sigma^{(3)})} \le C <\infty
\end{equation}
for all $0\le\gamma\le 1$.
Observe also that in the limit $\gamma\to 1$, $\Sigma^{(3)}$ takes the 
form of the cross 
\begin{equation}\label{e-z10}
  y=\pm |x+1| \quad \text{for $z=x+iy$ near $-1$}.
\end{equation}

Apart from the neighborhood of $z=-1$, there is considerable freedom 
in the choice of $\Sigma^{(3)}$. 
For example, $3\pi/4$ could be replaced by any angle between 
$\pi/2$ and $\pi$. 
Also the form of the contour for $|\theta|<3\pi/4$ is not critical, 
as long as it has the general shape drawn in Figure~\ref{fig-ga<1} : 
all that we really need is that the jump matrix $v^{(3)}$ below 
has the property $\sup_{\{z\in\Sigma^{(3)} : |\arg(z)|<3\pi/4\}} 
|v^{(3)}-I|\to 0$ 
exponentially as $q\to\infty$.

Using the factorization 
\begin{equation*}
    v^{(2)}= \begin{pmatrix} 1&0\\
(-1)^qz^{-q}e^{\frac{-q\gamma}{2}(z-z^{-1})}&1\end{pmatrix}
    \begin{pmatrix} 1&-(-1)^qz^qe^{\frac{q\gamma}{2}(z-z^{-1})}\\0&1\end{pmatrix}
\equiv (b_-^{(2)})^{-1}b_+^{(2)},
\end{equation*}
we define 
\begin{equation*}
  \begin{cases}
     m^{(3)}=m^{(2)} (b_+^{(2)})^{-1}
\qquad\text{in}\quad \Omega^{(3)}_2,\\
     m^{(3)}=m^{(2)} (b_-^{(2)})^{-1}
\qquad\text{in}\quad \Omega^{(3)}_3,\\
     m^{(3)}=m^{(2)} 
\qquad\text{in}\quad \Omega^{(3)}_1, \Omega^{(3)}_4.
  \end{cases}
\end{equation*}
Then $m^{(3)}$ solves the RHP $(\Sigma^{(3)},v^{(3)})$ where 
\begin{equation}\label{e-sec2.5}
  \begin{cases}
    v^{(3)} = \begin{pmatrix} 1&-(-1)^qz^qe^{\frac{q\gamma}{2}(z-z^{-1})}\\0&1
              \end{pmatrix} \quad\text{on}\quad\Sigma_{in}^{(3)},\\
    v^{(3)} = \begin{pmatrix} 1&0\\(-1)^qz^{-q}e^{\frac{-q\gamma}{2}(z-z^{-1})}&1
              \end{pmatrix} \quad\text{on}\quad\Sigma_{out}^{(3)},
  \end{cases}
\end{equation}\\
and 
\begin{equation}\label{e-z1}
  \kappa^2_{q-1}= m_{22}^{(3)}(0). 
\end{equation}

As $q\to\infty$, $v^{(3)}(z)\to I$.
Set $\Sigma^{\infty}=\Sigma^{(3)}$.
The RHP 
\begin{equation}
\begin{cases}
m^{\infty}_+=m^{\infty}_-\text{I} \quad\text{on}\quad \Sigma^{\infty}, \\
m^{\infty}=I+O(\frac1z) \quad\text{as}\quad z\rightarrow \infty\\
\end{cases}
\end{equation}
has, of course, the unique solution, $m^{\infty}(z)\equiv I$. 

\bigskip
Let $0\le\gamma\le 1-\delta_1$ for some $0< \delta_1< 1$.
From the choice of $\Sigma^{(3)}$, 
\begin{equation}\label{e-sec2.13}
 \begin{split}
   \|v^{(3)}-I\|_{L^\infty(\Sigma^{(3)})} 
&=\sup_{3\pi/4 \le\theta\le 5\pi/4} |e^{F(\rho_\theta,\theta)}|
\le \sup_{3\pi/4 \le\theta\le 5\pi/4} |e^{F(\rho_{\pi},\theta)}|\\
&\le e^{F(\rho_{\pi},\pi)}
=e^{q(\sqrt{1-\gamma^2} +\log \frac{1-\sqrt{1-\gamma^2}}{\gamma})}.
 \end{split}
\end{equation}
But, for $0<\gamma \le 1$, a straightforward estimate shows that 
\begin{equation}\label{e-sec2.14}
   \sqrt{1-\gamma^2} +\log (1-\sqrt{1-\gamma^2}) -\log\gamma 
\le -\frac{2\sqrt{2}}{3} (1-\gamma)^{3/2}
\end{equation}
so that 
\begin{equation}\label{e-sec2.15}
   \|w^{(3)}\|_\infty =\|v^{(3)}-I\|_\infty
\le e^{-\frac{2\sqrt{2}}{3}\delta_1^{3/2}q} \to 0 
\quad\text{as}\quad q\to\infty.
\end{equation} 
Since $\|C_{w^{(3)}}\|_{L^2\to L^2} \le C\|w^{(3)}\|_\infty$, for 
some constant $C$ independent of $\gamma$ (see~\eqref{e-Cau}), 
$(I-C_{w^{(3)}})^{-1}$ is invertible for large $q$ and 
the solution for the RHP $(\Sigma^{(3)},v^{(3)})$ is given by 
(see~\eqref{e-sam5}) 
\begin{equation}\label{e-z2}
      m^{(3)}(z)=I+\int_{\Sigma^{(3)}} 
\frac{((I-C_{w^{(3)}})^{-1}I)(s)(v^{(3)}(s)-I)}{s-z}
\frac{ds}{2\pi i}, \quad z\notin\Sigma^{(3)},
\end{equation}
and (see~\eqref{e-z1})
\begin{equation}
   \kappa_{q-1}^2=m^{(3)}_{22}(0)
=1+\biggl( \int_{\Sigma^{(3)}} 
\frac{((I-C_{w^{(3)}})^{-1})I)(s)(v^{(3)}(s)-I)}{s}
\frac{ds}{2\pi i} \biggr)_{22}.
\end{equation}
Now from the fact that the length of $\Sigma^{(3)}$ is uniformly 
bounded and $dist(0, \Sigma) \geq c>0$ for all $\gamma\in [0,1]$, we obtain, 
\begin{equation}\label{e-sec2.18}
   |  \kappa_{q-1}^2 -1 |
\le C\|v^{(3)}-I\|_\infty
\le Ce^{-\frac{2\sqrt{2}}{3}\delta_1^{3/2}q}.
\end{equation}



\bigskip
The above calculation also applies to the case when $\gamma\to 1$ slowly.
Indeed, suppose $\frac12 \le \gamma \le 1-\frac{M_1}{2^{1/3}q^{2/3}}$, 
where $M_1>0$ is a fixed, sufficiently large number.
(The lower bound $\frac12$ is chosen for convenience. Any fixed number 
between 0 and 1 would work.) 
From~\eqref{e-sec2.14},~\eqref{e-sec2.15}, for some constant $C$
which is independent of $\gamma$,
\begin{equation}\label{e-sec3.6}
  \|C_{w^{(3)}}\|_{L^2\to L^2}
\le Ce^{-\frac{2\sqrt{2}}3q(1-\gamma)^{3/2}}
\le Ce^{-\frac{2\sqrt{2}}3M_1^{3/2}} \le \frac12 <1,
\end{equation}
if $M_1$ is sufficiently large. 
For convenience, we only consider $M_1\geq 1$.
From~\eqref{e-z2},
\begin{equation*}
  \begin{split}
    m^{(3)}&=I+\frac1{2\pi i} \int_{\Sigma^{(3)}} \frac{[(I-C_{w^{(3)}})^{-1
}I](s)w^{(3)}(s)}{s-z}\,ds\\
   &=I+\frac1{2\pi i} \int_{\Sigma^{(3)}} \frac{w^{(3)}(s)+[(I-C_{w^{(3)}})^
{-1}C_{w^{(3)}}I](s)w^{(3)}(s)}{s-z} \,ds
  \end{split}
\end{equation*}
and, as $diag(w^{(3)})=0$,
\begin{equation}
   \kappa^2_{q-1}=m^{(3)}_{22}(0)
    =1+\bigl( \frac1{2\pi i} \int_{\Sigma^{(3)}}
[(I-C_{w^{(3)}})^{-1}C_{w^{(3)}}I](s)w^{(3)}(s)
    \frac{ds}{s} \bigr)_{22}.
\end{equation}
Hence, we have
\begin{equation}
  \begin{split}
    |\kappa^2_{q-1}-1|&\le
\|(I-C_{w^{(3)}})^{-1}C_{w^{(3)}}I\|_{L^2}
\|\frac{w^{(3)}(s)}{2\pi is}\|_{L^2}\\
    &\le \|(I-C_{w^{(3)}})^{-1}\|_{L^2\rightarrow L^2}
\|C_{w^{(3)}}I\|_{L^2} \|\frac{w^{(3)}(s)}{2\pi is}\|_{L^2}\\
    &\le C\|w^{(3)}\|_{L^2}^2\\
    &\le C\|w^{(3)}\|_{L^\infty} \|w^{(3)}\|_{L^1}\\
    &\le Ce^{-\frac{2\sqrt{2}}3q(1-\gamma)^{3/2}} \|w^{(3)}\|_{L^1},
  \end{split}
\end{equation}
where the (final) constant $C$ is independent of $\gamma,q$ and $M_1$ 
(sufficiently large), provided that 
$0\le\gamma\le 1-\frac{M_1}{2^{1/3}q^{2/3}}$.

Since the length of $\Sigma^{(3)}$ is bounded, we have $\|w^{(3)}\|_{L^1} 
\le Ce^{-\frac{2\sqrt{2}}3q(1-\gamma)^{3/2}}$, which is 
the same estimation~\eqref{e-sec2.18} as in the case $\gamma<1-\delta_1$. 
But for future calculations (see~\eqref{e-z3} below), we need a sharper result.
We estimate $\|w^{(3)}\|_{L^1}$ as follows :
  Focus on $\Sigma^{(3)}_{in}$.
For $\Sigma^{(3)}_{out}$, similar computations apply.
Only the $12$-component of $w^{(3)}$ is non-zero.
  Set $\wt{\theta}=\frac1{q^{1/3}}\log{q}$.
  $$\int_{\Sigma^{(3)}_{in}}|z^qe^{\frac{q\gamma}{2}(z-z^{-1})}||dz|= (1)+(2
)$$
  where $(1)$ is an integration over $|\theta|\le \pi-\wt{\theta}$
and $(2)$ covers the remainder.
  Note from~\eqref{e-z10} that $|dz|\le Cd\theta$. 
Substituting $\rho_\theta$~\eqref{e-z9} into $F(\rho,\theta)$~\eqref{e-z8}, 
we obtain on $\Sigma^{(3)}_{in}$, 
\begin{equation}\label{e-z11}
    |z^qe^{\frac{q\gamma}2(z-z^{-1})}|\le e^{
q\bigl(\sqrt{1-\gamma^2\cos^2\theta}+\log(1-\sqrt{1-\gamma^2\cos^2\theta})
-\log(-\gamma\cos\theta)\bigr)}.
\end{equation}
Setting, $\gamma\to -\gamma\cos\theta$ in~\eqref{e-sec2.14}, 
we obtain for $z\in\Sigma^{(3)}_{in}$, 
\begin{equation}\label{e-z12}
    |z^qe^{\frac{q\gamma}2(z-z^{-1})}|\le
e^{-\frac{2\sqrt{2}q}{3}(1+\gamma\cos\theta)^{3/2}}
\le e^{-Cq(\pi-|\theta|)^3}
\end{equation}
Hence, adjusting the constants $C$ if necessary, 
we have 
  $$(1)\le Ce^{-Cq\wt{\theta}^3} \le \frac{C}{q^{1/3}}$$
and $$(2)\le C\int_0^{\wt{\theta}} e^{-Cq\theta^3} d\theta
\le C\int_0^{\log{q}} e^{-Ct^3} \frac{dt}{q^{1/3}} \le \frac{C}{q^{1/3}}.$$
Therefore, 
\begin{equation}\label{6.9}
   \|w^{(3)}\|_{L^1}\le \frac{C}{q^{1/3}}
\end{equation}
and we obtain
\begin{equation}\label{e-sec3f}
   |\kappa^2_{q-1}-1|\le
\frac{C}{q^{1/3}}e^{-\frac{2\sqrt{2}}3q(1-\gamma)^{3/2}}.
\end{equation}


\bigskip
Let $M_2>0$ be a fixed number 
and consider $1-\frac{M_2}{2^{1/3}q^{2/3}} \le \gamma \le 1$.
For this case, as $q\to\infty$, $\gamma\to 1$ and 
$\rho_{\theta=\pi} \to 1$. 
We need to devote special attention to the neighborhood of $z=-1$, 
where we will introduce a parametrix for the RHP,  
which is related to the special solution of the Painlev\'e II (PII)
equation~\eqref{e-int1} given in Section~\ref{s-PII}.
For a discussion of parametrices in RHP's, see e.g. \cite{DZ}, \cite{DKMVZ}.
Set $\gamma=1-\frac{t}{2^{1/3}q^{2/3}}$. 
The region above corresponds to $0\le t\leq M_2$.
Let $\mathcal{O}$ be a small neighborhood of size $\epsilon$ around
$z=-1$, where $\epsilon>0$ is a fixed number which is small enough  
so that first, 
\begin{equation}\label{e-z18}
  \text{the map $u$ defined below is a bijection from $\mathcal{O}$,} 
\end{equation}
and second, 
\begin{equation}\label{e-z19}
  \text{the inequality~\eqref{e-z20} below is satisfied.}
\end{equation} 
The goal is to solve 
the RHP for $m^{(3)}$ explicitly in this small region.

Let $u=\frac12(z-z^{-1})$ in $\mathcal{O}$.
\begin{figure}[ht]
 \centerline{\epsfig{file=map.eps, width=11cm}}
 \caption{}\label{fig-map}
\end{figure}
As noted above, we choose and fix $\epsilon>0$ sufficiently small 
(in fact, any number $0<\epsilon<1$ would do.) so that $z\to u(z)$ 
is a bijection 
from $\mathcal{O}$ onto some open neighborhood of $0$ in the $u$-plane : 
under the bijection, 
$\Sigma\cap\mathcal{O}$ becomes a part of
the imaginary axis.
Set $$\lambda(z)=\frac{q^{1/3}u(z)}{i2^{4/3}}=
\frac{q^{1/3}}{i2^{4/3}}\frac12(z-z^{-1}).$$
Note that with $\epsilon$ fixed, there are constants $c_1,c_2>0$ 
such that  
\begin{equation}\label{e-z13}
  c_1 q^{1/3}\le |\lambda(z)| \le c_2 q^{1/3},  
\end{equation}
for all $z\in\partial\mathcal{O}$.
Under the map $z\to\lambda(z)$, $\Sigma\cap\mathcal{O}$ now becomes 
part of the real axis  and 
\begin{equation}
   \lambda(\Sigma^{(3)}\cap\mathcal{O}) = \{ x+iy : 
y^2=\frac{\frac{q^{2/3}}{2^{8/3}}(1-\gamma^2)+x^2}
{1+\frac{2^{8/3}\gamma^2 x^2}{q^{2/3}}}, |x|\le cq^{1/3} \},
\end{equation}
where $c$ is a fixed small number.
As $\frac{q^{2/3}}{2^{8/3}}(1-\gamma^2)=\frac{t}4\bigl(
1-\frac{t}{2^{4/3}q^{2/3}} \bigr)$, $0\le t\le M_2$, we see that 
the contour $\lambda(\Sigma^{(3)}\cap\mathcal{O})$ makes an angle 
$\le \pi/4$ and uniformly bounded away from zero as $q\to\infty$, 
hence has the general shape of the contour in 
Figure~\ref{fig-PII2}, Section~\ref{s-PII}, 
within the ball $\lambda(\mathcal{O})$.
We \emph{define} 
\begin{equation}
   \Sigma^{PII,2}\cap\lambda(\mathcal{O}) \equiv 
\lambda(\Sigma^{(3)}\cap\mathcal{O})
\end{equation}
and extend $\Sigma^{PII,2}$ smoothly outside $\lambda(\mathcal{O})$ 
in such a way that it is asymptotic to straight lines making angles 
between 0 and $\pi/3$ with the real axis.
It is clear from the estimation in Section~\ref{s-PII}, and the 
preceding calculations, that for such a contour $\Sigma^{PII,2}$, 
the bound~\eqref{e-unif2} for the solution $m^{PII,2}(z,t)$ 
of $(\Sigma^{PII,2},v_t^{PII,2})$
\begin{equation}\label{e-z15}
   \text{is uniform for $\gamma, q$ satisfying the relation 
$1-\frac{M_2}{2^{1/3}q^{2/3}}\le \gamma\le 1$.}
\end{equation}


Introduce the parametrix around $z=-1$ as follows.
Define 
\begin{equation*}
  \begin{cases}
    m_p(z)=m^{PII,2}(\lambda(z),t) \quad
\text{in}\quad\mathcal{O}-\Sigma^{(3)}, \\
    m_p(z)=I \quad\text{in}\quad\mathcal{\bar{O}}^c-\Sigma^{(3)}.
  \end{cases}
\end{equation*}
As $q\to\infty$, $|\lambda(z)|\to\infty$ for $z\in\partial\mathcal{O}$,  
and we have for $v_p(z)\equiv v_t^{PII,2}(\lambda(z))$, 
\begin{equation}
 \begin{cases}
   m_p(z) \ \ \text{is analytic in} \ \ 
\C-(\Sigma^{(3)}\cup\partial\mathcal{O})\\
   m_{p+}(z)=m_{p-}(z)v_p(z) \ \ 
\text{on} \ \ \mathcal{O}\cap\Sigma^{(3)}\\
   m_{p+}(z)=m_{p-}(z)I \ \ \text{on} \ \ \mathcal{O}^c\cap\Sigma^{(3)}\\
   m_{p+}(z)=I+\frac{m^{PII,2}_{1}(t)}{\lambda(z)}+O(\frac{1}{\lambda(z)^2}) 
\ \ \text{on} \ \ \partial\mathcal{O} \ \  
\text{as} \ \ q\rightarrow\infty.
 \end{cases}
\end{equation}

The key fact is that $v_p$ is an approximation to  
$v^{(3)}$ with error of order $\frac{1}{q^{2/3}}$. 
We compare, for example, the 12-components of $v^{(3)}$ and 
$v_p$ on $\Sigma^{(3)}$.
We focus on $\mathcal{O}\cap\Sigma_{in}^{(3)}$.
Using the $u$ variable, the $12$-entries of $v^{(3)}$ and $v_p$ are 
$$-\exp(q[\gamma u+\log(\sqrt{1+u^2}-u)])$$ 
and $$-\exp(q[\gamma u-u+\frac16u^3])$$
respectively.
By~\eqref{e-z11} and~\eqref{e-z12}, we have for 
$z\in\mathcal{O}\cap\Sigma_{in}^{(3)}$, 
\begin{equation*}
  |e^{q[\gamma u+\log(\sqrt{1+u^2}-u)]}|
=|z^qe^{\frac{q\gamma}2(z-z^{-1})}|\le
e^{-\frac{2\sqrt{2}q}{3}(1+\gamma\cos\theta)^{3/2}}.
\end{equation*}
From the Taylor expansion of the odd function $\log(\sqrt{1+u^2}-u)$, 
$$\log(\sqrt{1+u^2}-u)=-u+\frac16u^3+u^5r(u),$$
where $r(0)=-\frac3{40}$ and $r(u)$ is bounded for small $u$, 
say $|u|\le\frac12$.
Set $\hat{c}=\sup_{|u|\le\frac12} |r(u)|$.
Note that for $z=\rho_{\theta}e^{i\theta}
\in\mathcal{O}\cap\Sigma^{(3)}_{in}$ (see~\eqref{e-z9}), 
as $q\to\infty$, we have 
$|u|\leq \wt{c}(1+\gamma \cos \theta)^{1/2}\le \wt{c}(c'\epsilon)^{1/2}$.
Therefore, if we have chosen $\epsilon>0$ small enough 
so that 
\begin{equation}\label{e-z20}
  -\frac{2\sqrt{2}}3+\hat{c}(\wt{c})^5c'\epsilon\le -\frac12, 
\end{equation}
we obtain, as $q\to\infty$,
\begin{equation}\label{e-z14}
 \begin{split}
   &|e^{q[\gamma u+\log(\sqrt{1+u^2}-u)]}-e^{q[\gamma u-u+\frac16u^3]}| \\
   &\qquad = |e^{q[\gamma u+\log(\sqrt{1+u^2}-u)]}||1-e^{-qu^5r(u)}| \\
   &\qquad \leq e^{-\frac{2\sqrt{2}q}3(1+\gamma \cos \theta)^{3/2}}\times 
q|u|^5\|r\|_{L^\infty(\{|u|\le\frac12\})}
e^{q\hat{c}(\wt{c})^5(1+\gamma \cos \theta)^{5/2}} \\
   &\qquad \leq Cq(1+\gamma \cos \theta)^{5/2}
e^{q(-\frac{2\sqrt{2}}3+\hat{c}(\wt{c})^5c'\epsilon)(1+\gamma \cos \theta)^{3/2}} \\
   &\qquad \leq Cq(1+\gamma \cos \theta)^{5/2} 
e^{-\frac{q}2(1+\gamma \cos \theta)^{3/2}} \\
   &\qquad \leq \frac{C}{q^{2/3}},
 \end{split}
\end{equation}
where we have used the basic inequality 
$|1-e^z|\le |z|e^{|z|}$ and the fact that 
$\|x^{5/3}e^{-x^{3/2}}\|_{L^{\infty}_{(0,\infty)}} \le C$.
Since 
\begin{equation*}
   v^{(3)}v_p^{-1}= 
   \begin{pmatrix} 1& -e^{q[\gamma u+\log(\sqrt{1+u^2}-u)]}+
e^{q[\gamma u-u+\frac16u^3]}\\ 0&1 
   \end{pmatrix} \ \ \text{on} \ \ \mathcal{O}\cap\Sigma_{in}^{(3)},
\end{equation*}
we have $$\|v^{(3)}v_p^{-1}-I\|_{L^{\infty}
(\mathcal{O}\cap\Sigma^{(3)}_{in})}=O(\frac1{q^{2/3}}).$$
For $\mathcal{O}\cap\Sigma_{out}^{(3)}$, we have a similar estimation.
On the other hand, for 
$\mathcal{O}^c$, the error is exponentially small ; 
$\|v^{(3)}v_p^{-1}-I\|_{L^\infty(\mathcal{O}^c\cap\Sigma^{(3)})}
=\|v^{(3)}-I\|_{L^\infty(\mathcal{O}^c\cap\Sigma^{(3)})}=O(e^{-cq})$.

Now define $R(z)=m^{(3)}m_p^{-1}$.
The ratio is analytic in $\C-(\Sigma^{(3)}\cup\partial\mathcal{O})$ 
and the above calculations show that the jump matrix 
$v_R=m_{p-}v^{(3)}v_p^{-1}m_{p-}^{-1}$ satisfies 
\begin{equation}\label{e-z16}
  \begin{cases}
    \|v_R-I\|_\infty\le\frac{C(M_2)}{q^{2/3}}
&\text{on $\mathcal{O} \cap \Sigma^{(3)}$},\\
    \|v_R-I\|_\infty\le Ce^{-cq} 
&\text{on $\mathcal{O}^c \cap \Sigma^{(3)}$},\\
    v_R=v_{p}^{-1}=m_{p+}^{-1}=I-\frac{m^{PII,2}_1(t)}{\lambda(z)}+
O_{M_2}(\frac{1}{\lambda(z)^2}) 
&\text{on $\partial \mathcal{O}$, as $q\to\infty$.}
  \end{cases}
\end{equation}
In~\eqref{e-z16}, we have used the fact that $m^{PII,2}(z,t)$, 
and hence $m_{p}$, is invertible 
and bounded for $(z,t)\in\C\times [0,M_2]$. (see,~\eqref{e-z15}).

From~\eqref{e-z16} and~\eqref{e-z13}, we see that 
$\|v_R-I\|_\infty=\|w_R\|_\infty\le\frac{C(M_2)}{q^{1/3}}$.
In particular, $(I-C_{w_R})$ is invertible for large $q$ and 
by~\eqref{e-sam5}, $R$ is given by
$$R(z)=I+\frac1{2\pi i} \int_{\Sigma^{(3)}\cup\partial\mathcal{O}} 
\frac{\mu(s)(v_R-I)}{s-z} \,ds$$
where $\mu$ solves $(I-C_{w_R})\mu=I.$
As $\|v_R-I\|_\infty\le\frac{C(M_2)}{q^{1/3}}$, we have 
$\|\mu-I\|_{L^2}=O_{M_2}(\frac1{q^{1/3}})$, and also   
$$R_{22}(0)=1+\frac1{2\pi i} \int_{\Sigma^{(3)}\cup\partial\mathcal{O}} 
(v_R-1)_{22}(s) \frac{ds}{s} 
+O_{M_2}(\frac1{q^{2/3}}).$$
Thus, using $\|v_R-I\|_\infty\le\frac{C(M_2)}{q^{2/3}}$ in~\eqref{e-z16} 
for the second equality, and  $m^{PII,2}_1=m^{PII,1}_1$ 
(see ~\eqref{e-RHPm2'}) for the last equality, we obtain 
\begin{equation}\label{e-R22K1}
  \begin{split}
    \kappa^2_{q-1}&=R_{22}(0)\\
    &= 1+\frac1{2\pi i} \int_{\partial\mathcal{O}} (v_R-1)_{22}(z) \frac{dz}{z} 
+O_{M_2}(\frac1{q^{2/3}})\\
    &=1-\frac1{2\pi i} \int_{\partial\mathcal{O}} 
\frac{m^{PII,2}_{1,22}(t)}{\lambda(z)} \frac{dz}{z} +
O_{M_2}(\frac1{q^{2/3}})\\
    &=1-\frac{m^{PII,2}_{1,22}(t)}{2\pi i} \int_{u(\partial\mathcal{O})} 
\frac{1}{-i\frac{q^{1/3}}{2^{4/3}}u} \,\frac{du}
{(-\sqrt{u^2+1})} +O_{M_2}(\frac1{q^{2/3}})\\
    &=1+\frac{i2^{4/3}}{q^{1/3}}m^{PII,2}_{1,22}(t)+O_{M_2}(\frac1{q^{2/3}})\\
    &=1+\frac{i2^{4/3}}{q^{1/3}}m^{PII,1}_{1,22}(t)+O_{M_2}(\frac1{q^{2/3}}).
  \end{split}
\end{equation}
Note that error in~\eqref{e-R22K1} is uniform for $0\le t\le M_2.$

We summarize as follows.
\begin{lem}\label{lem-K1}
  Let $M_1>0$ be a fixed number which is sufficiently large so 
that~\eqref{e-sec3.6} is satisfied. 
Also let $M_2>0$ and  
$0<\delta_1 <1$ be fixed numbers.
As $q\to \infty$, we have the following results.
\begin{enumerate}
    \item If $0\le \gamma \le 1-\delta_1$,  
then, for some constants $C,c$ which may depend on $\delta_1$,
\begin{equation*}
  |\kappa^2_{q-1}- 1 |\le Ce^{-cq}.
\end{equation*}
    \item If $\frac12 \le \gamma \le 1-\frac{M_1}{2^{1/3}q^{2/3}}$, 
then, 
for some constant $C$ which is independent of $M_1$ satisfying~~\eqref{e-sec3.6}, 
\begin{equation*}
  |\kappa^2_{q-1}-1| \le \frac{C}{q^{1/3}}
e^{-\frac{2\sqrt{2}}3q(1-\gamma)^{3/2}}.
\end{equation*}
    \item If $1-\frac{M_2}{2^{1/3}q^{2/3}} \le \gamma \le 1$, 
\begin{equation*}
  \bigl|\kappa^2_{q-1}-1-\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(t)\bigr|
\le \frac{C(M_2)}{q^{2/3}}, 
\end{equation*}
where $t$ is defined by $\gamma=1-\frac{t}{2^{1/3}q^{2/3}}$.
\end{enumerate}
\end{lem}





\bigskip

\section{$\mathbf{\gamma > 1}$}
\label{s-K2}

Let $\theta_c$ be given in Lemma ~\ref{lem-ourg}, 
$\sin^2\frac{\theta_c}{2}=\frac{1}{\gamma}, 0< \theta_c<\pi$.
Decompose $\Sigma=\overline{C_1}\cup C_2$ where 
$C_1=\{ e^{i\theta} : \theta_c < |\theta | \le \pi \}$
and $C_2=\Sigma-\overline{C_1}$.
Note that on the support of the measure $d\mu_V$ in~\eqref{e-lem4.3.2}, 
$d\mu_V(\theta)=\frac{\gamma}{\pi} \cos(\frac{\theta }{2}) 
\sqrt{\frac{1}{\gamma} - \sin^2(\frac{\theta}{2})} 
\chi_{[-\theta_c, \theta_c]}(\theta) d\theta
=\frac\gamma{4\pi i} \frac{s+1}{s^2}\sqrt{(s-\xi)(s - \xi^{-1})}ds$ 
for $s=e^{i\theta}$.
\begin{figure}[ht]
 \centerline{\epsfig{file=Cinout_mod.eps, width=9cm}}
 \caption{$\Sigma$ and $\Sigma^{(3)}$}\label{fig-Cinout}
\end{figure}

\begin{lem}\label{lem-alpha}
Define 
$\alpha(z) = -\frac{\gamma}4 \int^z_\xi  
\frac{s+1}{s^2}\sqrt{(s-\xi)(s - \xi^{-1})}ds$ 
where $\xi=e^{i\theta_c}$ and the branch is chosen to 
be analytic in $\C-\overline{C_1}$
and $\sqrt{(s-\xi)(s - \xi^{-1})}>0$ for real $s>0$. Then
\begin{enumerate}
\item $e^{2\alpha}$ is independent of the path in $\C-(\bar{C_1}\cup\{0\})$,.
\item $\exp\bigl( -2\pi i 
\int_{\theta_c}^\phi d\mu_V(\theta)\bigr) 
= \exp\bigl( 2\alpha(z)\bigr) \quad \text{for} \quad z=e^{i\phi}, 
|\phi|<\theta_c$.
\item $\exp\bigl( 2\int_{-\pi}^{\pi}\log |z-e^{i\theta}| d\mu_V(\theta) 
-V(z)+l\bigr)  = \exp\bigl( -2\alpha_-(z)\bigr) \quad \text{for} 
\quad z=e^{i\phi}, |\phi|>\theta_c$.
\end{enumerate}
\end{lem}
\begin{proof}
   Property (i) follows from a standard reside calculation 
: the change in $\alpha(z)$ around
the point at $0$ is $-\pi i$, and the change in $\alpha(z)$
around $C_1$ is $0$. Property (ii) follows from the definition of $\alpha(z)$.
For (iii), set 
\begin{equation*}
   F(\phi)=2\int_{-\pi}^{\pi}\log |e^{i\phi}-e^{i\theta}| d\mu_V(\theta)
+\gamma\cos{\phi} +l +2\alpha_-(e^{i\phi})
\end{equation*}
for $z=e^{i\phi}$, $|\phi|>\theta_c$.
From the variational condition ~\eqref{e-varicon}, we have $F(\theta_c)=0$.
Differentiating,
\begin{equation*}
  \begin{split}
   F'(\phi)&=\int_{-\theta_c}^{\theta_c} i\bigl[ 
\frac{2e^{i\phi}}{e^{i\phi}-e^{i\theta}}-1 \bigr] d\mu_V(\theta)
-\frac{\gamma}{2i} \bigl( e^{i\phi}-e^{-i\phi} \bigr)\\
   &\qquad -\frac{i\gamma}2\frac{e^{i\phi}+1}{e^{i\phi}}
\sqrt{(e^{i\phi}-\xi)(e^{i\phi} - \xi^{-1})}_-\\
  &= \frac{\gamma}{2\pi} \int_{C_2} \frac{z}{z-s} \frac{s+1}{s^2} 
\sqrt{(s-\xi)(s - \xi^{-1})} ds\\
   &\qquad -i-\frac{\gamma}{2i}(z-z^{-1}) -\frac{i\gamma}2\frac{z+1}{z}
\sqrt{(z-\xi)(z - \xi^{-1})}_-.
  \end{split}
\end{equation*}
A residue calculation similar to that in (i), now shows that $F'(\phi)=0$.
Therefore we have $F(\phi)\equiv 0$.
\end{proof}

Note that $e^{2q\pi i\int_{\phi}^{\pi} d\mu_V(\theta)}=1$ for $\phi$ 
outside the support of $d\mu_V$ , i.e.~for $|\phi|>\theta_c$. 
By~\eqref{e-Omega} and above Lemma, our RHP becomes 
\begin{equation}
\begin{cases}
m^{(1)}(z) \ \ \text{is analytic in} \ \ \C-\Sigma, \\
m^{(1)}_+=m^{(1)}_- \begin{pmatrix} e^{-2q\alpha}& (-1)^q\\ 0& e^{2q\alpha} \end{pmatrix} \ \ \text{on} \ \ C_2,\\
m^{(1)}_+=m^{(1)}_- \begin{pmatrix} 1& (-1)^qe^{-2q\alpha_-}\\ 0&1 \end{pmatrix} \ \ \text{on} \ \ C_1,\\
m^{(1)}=I+O(\frac1z) \ \ \text{as}\ \  z\rightarrow \infty
\end{cases}
\end{equation}
and $\kappa^2_{q-1}=-(-1)^qm^{(1)}_{21}(0)e^{ql}=
-(-1)^qe^{q(-\gamma+\log \gamma+1)}m^{(1)}_{21}(0)$
by~\eqref{e-Korig} and~\eqref{e-lem4.3.3}.

We use the same conjugation ~\eqref{e-conju} 
for $m^{(1)}$ as in the case $\gamma\le 1$.
Then our new jump matrices for $m^{(2)}$ are 
\begin{equation}\label{e-m2tilde}
\begin{cases}
v^{(2)}= \begin{pmatrix} 1& -e^{-2q\alpha}\\ e^{2q\alpha}&0 \end{pmatrix} \ \ \text{on} \ \ C_2\\
v^{(2)}= \begin{pmatrix} e^{-2q\alpha_-}& -1\\ 1&0 \end{pmatrix} \ \ \text{on} \ \ C_1
\end{cases}
\end{equation}
and $\kappa^2_{q-1}=e^{q(-\gamma+\log \gamma+1)}m^{(2)}_{22}(0)$.

Set $\Sigma^{(3)}=\overline{C_1}\cup \wt{C}_{inside} \cup \wt{C}_{outside}$ 
where $\wt{C}_{inside}$ and $\wt{C}_{outside}$ are open arcs as  chosen below.
Note the factorization $v^{(2)}=
\begin{pmatrix} 1&0\\e^{2q\alpha}&1 \end{pmatrix}
\begin{pmatrix} 1& -e^{-2q\alpha}\\0&1 \end{pmatrix}$on $C_2$. 
Set $Re \alpha =R$, $Im \alpha =I$ so that $\alpha =R+iI$.
Recall the Cauchy-Riemann equations in polar coordinates $(r,\theta)$,
\begin{equation*}
   r\frac{\partial R}{\partial r} =\frac{\partial I}{\partial\theta},
\quad r\frac{\partial I}{\partial r} =-\frac{\partial R}{\partial\theta}. 
\end{equation*}
For $z=e^{i\theta}\in C_2$, 
$\alpha(z)=-\pi i \int_{\theta_c}^{\theta} d\mu_V(\theta')$ 
is pure imaginary and 
\begin{equation*}
\frac{\partial I}{\partial\theta}
=\frac{\partial}{\partial\theta} (-i\alpha)=-\pi\frac{\gamma}{\pi}
\cos(\frac{\theta }{2})
\sqrt{\frac{1}{\gamma} - \sin^2(\frac{\theta}{2})} <0.
\end{equation*}
Hence 
\begin{equation*}
   R=0  \quad\text{and}\quad
   \frac{\partial R}{\partial r} =\frac{\partial I}{\partial\theta} <0
\quad\text{on}\quad C_2. 
\end{equation*}
Therefore for fixed $\theta$, $e^{i\theta}\in C_2$, there is 
$\epsilon_1=\epsilon_1(\theta) >0$ 
such that $R=Re \alpha >0$ (resp. $<0$) for $z=re^{i\theta}$ with 
$1-\epsilon_1 < r< 1$ (resp. $1<r<1+\epsilon_1$).
We take $\wt{C}_{inside}$ (resp, $\wt{C}_{outside}$) 
such that $|e^{-2\alpha}|<1$ (resp, $|e^{2\alpha}|<1$) 
on $\wt{C}_{inside}$ (resp, $\wt{C}_{outside}$).
Clearly there exist $0<\rho_1, \rho_2 <1$ such that $|e^{-2\alpha}|<\rho_1$ 
(resp, $|e^{2\alpha}|<\rho_2$), for all $z\in\wt{C}_{inside}$ 
(resp, $z\in\wt{C}_{outside}$), apart from a small neighborhood 
of the endpoints.
Introduce the regions $\Omega^{(3)}_{k}$, $k=1,2,3,4$ 
as in Figure~\ref{fig-Cinout}.
Define $m^{(3)}$ as follows, 
\begin{equation*}
  \begin{cases}
     &m^{(3)}=m^{(2)} \begin{pmatrix} 1&-e^{-2q\alpha}\\0&1 \end{pmatrix}^{-1}
\quad\text{in}\quad \Omega^{(3)}_2,\\
     &m^{(3)}=m^{(2)} \begin{pmatrix} 1&0\\e^{2q\alpha}&1 \end{pmatrix}
\qquad\text{in}\quad \Omega^{(3)}_3,\\
     &m^{(3)}=m^{(2)} \qquad\qquad\text{in}\quad \Omega^{(3)}_1,\Omega^{(3)}_4.
  \end{cases} 
\end{equation*}
Then $v^{(3)}$ is given by
\begin{equation*}
  \begin{cases}
     &\begin{pmatrix} 1&-e^{-2q\alpha}\\0&1 \end{pmatrix}
\quad\text{on}\quad \wt{C}_{inside},\\
     &\begin{pmatrix} 1&0\\e^{2q\alpha}&1 \end{pmatrix}
\qquad\text{on}\quad \wt{C}_{outside},\\
     &\begin{pmatrix} e^{-2q\alpha_-}&-1\\1&0 \end{pmatrix}
\quad\text{on}\quad C_1,
  \end{cases}
\end{equation*}
and 
\begin{equation}\label{e-Km3K2}
   \kappa^2_{q-1}=e^{q(-\gamma+\log \gamma+1)}m^{(3)}_{22}(0).
\end{equation}

From Lemma ~\ref{lem-alpha} (iii) and the second variational 
condition in~\eqref{e-varicon}, we have, for any $z\in C_1$,
\begin{equation*}
   e^{-2q\alpha_-}\to 0 \quad\text{as} \quad q\to\infty.
\end{equation*}
(Recall that the inequality in ~\eqref{e-varicon} is strict
from Lemma ~\ref{lem-ourg} (ii)).
Also from the choice of $\wt{C}_{inside}$ and $\wt{C}_{outside}$, 
\begin{equation*}
   e^{-2q\alpha}\to 0, \quad e^{2q\alpha}\to 0
\quad\text{as} \quad q\to\infty
\end{equation*}
on $\wt{C}_{inside}$, $\wt{C}_{outside}$, respectively.
Therefore $v^{(3)} \rightarrow v^\infty$ as $q\rightarrow \infty$,
\begin{equation}
\begin{cases}
v^\infty =
 \begin{pmatrix} 1&0\\0&1 \end{pmatrix} \ \ \text{on} \ \ 
\wt{C}_{inside}\cup\wt{C}_{outside},\\
v^\infty =
 \begin{pmatrix} 0&-1\\1&0 \end{pmatrix} \ \ \text{on} \ \ 
C_1.
\end{cases}
\end{equation} 


The following result can be verified by direct calculation.
\begin{lem}\label{lem-minfty}
RHP $(C_1, v^\infty)$ can be solved explicitly.
\begin{equation}
m^\infty = \begin{pmatrix} \frac12(\beta+\beta^{-1})& \frac1{2i}(\beta-\beta^{-1})\\
                           -\frac1{2i}(\beta-\beta^{-1})& \frac12(\beta+\beta^{-1}) \end{pmatrix}
\end{equation}
where $\beta(z)\equiv (\frac{z-\xi}{z-\xi^{-1}})^{1/4}, \ \ 
\text{is analytic in} \ \ \C-\bar{C}_1 \ \ \text{such that} \ \ 
\beta\sim +1 \ \ \text{as} \ \ z\rightarrow \infty$
\end{lem}
Hence we expect from~\eqref{e-Km3K2}, 
$\kappa^2_{q-1}\sim e^{q(-\gamma+\log \gamma+1)}\frac1{\sqrt{\gamma}},$ 
because $m^\infty_{22}(0)=\frac1{\sqrt{\gamma}}$.

Our goal now is to show that indeed $m^{(3)}\to m^{\infty}$ 
as $q\to\infty$. As in Section ~\ref{s-K1}, we must control 
the behavior of the solution of the RHP for $m^{(3)}$ near the 
endpoints, where the rate of exponential convergence 
$v^{(3)}\to v^{\infty}$, becomes smaller and smaller.



\bigskip
Let $\delta_3, M_4>0$ be fixed numbers, let $0< \delta_4<1$ 
be a fixed, sufficiently small number satisfying~\eqref{e-z30} below, 
and let $M_3 >0$ be a fixed, sufficiently large number 
satisfying~\eqref{e-z29} and~\eqref{e-z28} below.
We consider 3 cases for $\gamma$ : 
\begin{enumerate}
    \item $1+\delta_3 \le \gamma$
    \item $1+\frac{M_3}{2^{1/3}q^{2/3}} \le \gamma \le 1+\delta_4$
    \item $1\le \gamma \le 1+\frac{M_4}{2^{1/3}q^{2/3}}$
\end{enumerate}

\bigskip
Calculations similar to those that are needed for the asymptotics 
of the orthogonal polynomial on the real line (see, \cite{DKMVZ}), 
show that for $\gamma>1+\delta_3$,
\begin{equation}\label{8.1}
  \kappa^2_{q-1}= e^{q(-\gamma+\log \gamma+1)}\frac1{\sqrt{\gamma}}(1+O(\frac1{q})).
\end{equation}
The error is uniform for $1+\delta_3 \le \gamma \le L$ for any fixed $L<\infty$.
However, we will not use this result, utilizing instead (stronger) estimates 
from \cite{Johan} (see next section).

\bigskip
\begin{figure}[ht]
 \centerline{\epsfig{file=umap2.eps, height=4cm}}
 \caption{}\label{fig-umap2}
\end{figure}
We consider case (iii).
Set $\gamma =1+\frac{t}{2^{1/3}q^{2/3}}$ with $0\le t \le M_4$ and $u_0=\sin{\theta_c}=\frac2{\gamma} \sqrt{\gamma-1}$.
In defining $\Sigma^{(3)}$ above, there is some freedom in the choice 
of $\wt{C}_{inside}$ and $\wt{C}_{outside}$.
We make the following choice (see~\eqref{e-z23} below). 
Set $x=-\frac{q^{2/3}u_0^2}{2^{5/3}}=
-t(1+\frac{t}{2^{1/3}q^{2/3}})^{-2} \sim -t<0$ as $q\to\infty$,  
and let $\Sigma^{PII,3}$ be the contour defined in Figure~\ref{fig-PII3} 
for this specific $x$.
Let $\Sigma'=\{ u=\frac{2^{4/3}}{q^{1/3}}\lambda : \lambda\in\Sigma^{PII,3} \}
=\cup_{k=1}^5 \Sigma'_k$, 
and let $\epsilon' >0$ be small and fixed (see~\eqref{e-z21},~\eqref{e-z22} below).
For definiteness, we can, and do assume that the rays 
$\Sigma'_1,\dots,\Sigma'_4$ make an angle of $\pi/6$ with the real axis.
Consider $\mathcal{O}'=\{ u : |u|<\epsilon' \}$.
If $q$ is large enough, then $u_0\in\mathcal{O}'$.
Set $u=u(z)=\frac1{2i}(z-z^{-1})$. 
We choose $\epsilon'$ such that (cf.~\eqref{e-z18}) 
\begin{equation}\label{e-z21}
   \text{$u$ is a bijection from an open neighborhood of $z=-1$ onto $\mathcal{O}'$.}
\end{equation}
Clearly there are constants $c_1,c_2>0$ such that 
$c_1\le |z(u)|\le c_2$ for all $u\in\partial\mathcal{O}'$.

Under $u^{-1}$, the points $u_0, -u_0$ are mapped into $\xi, \bar{\xi}$ respectively,  
and $u^{-1}(\Sigma'_5)=C_1$. 
Consider a point $z\in u^{-1}(\Sigma'_4 \cap\mathcal{O}')$, the inverse image of 
a point $u\in\Sigma'_4 \cap\mathcal{O}$.
Changing variables twice, 
$v=\frac1{2i}(s-s^{-1})$ and $w=v^2$, 
\begin{equation}\label{8.2}
  \begin{split}
    -2\alpha(z)
    &= \frac{i\gamma}{2} \int^z_\xi \bigl(\sqrt{s}+\sqrt{s}^{-1}\bigr)
\sqrt{(s+s^{-1})-(\xi+\xi^{-1})} \frac{ds}{is}\\
    &= -i\gamma \int_{u_0}^u \biggl( \sqrt{1-u_0^2}-\sqrt{1-v^2}\biggr)^{1/2}
\frac{\sqrt{1-\sqrt{1-v^2}}}{\sqrt{1-v^2}} dv\\
    &= \frac{-i\gamma}2 \int_{u_0}^u \biggl( \frac{v^2-u_0^2}
{1+k(u_0^2)+k(v^2)}\biggr)^{1/2} v\bigl( 1+h(v^2)\bigr) dv\\
    &= -\frac{i\gamma}4 \int_{u_0^2}^{u^2} (w-u_0^2)^{1/2}
\bigl[ 1+(h(w)-h(u_0^2))+h(u_0^2)\bigr] dw\\
    &\qquad -\frac{i\gamma}4 \int_{u_0^2}^{u^2} (w-u_0^2)^{1/2}
\frac{\bigl[ (k(u_0^2)-k(w))-2k(u_0^2)\bigr] (1+h(w))dw}
{(1+k(u_0^2)+k(w))^{1/2}
\bigl[ 1+(1+k(u_0^2)+k(w))^{1/2}\bigr]}\\
    &= \frac{-i\gamma}{6} (u^2-u_0^2)^{3/2}
+O\biggl( |u^2-u_0^2|^{5/2}\biggr)
+O\biggl( |u^2-u_0^2|^{3/2}u_0^2\biggr),
  \end{split}
\end{equation}
where $\sqrt{u^2-u_0^2}$ is defined to be analytic in $\C-[-u_0,u_0]$ and 
positive for real $u>u_0$ ; 
$h(w)=\frac{\sqrt{2}\sqrt{1-\sqrt{1-w}}}{\sqrt{w}\sqrt{1-w}}-1$,
which is analytic in $|w|\le\epsilon'$ and $h(0)=0$ ; 
$k(w)=\frac12(\sqrt{1-w}-1)$, which is also analytic
in $|w|\le\epsilon'$ and $k(0)=0$.
Since $\Sigma'_4$ is a straight ray of angle $\frac{-\pi}{6}$ 
at $u_0$, $Re(-i(u^2-u_0^2)^{3/2}) \le -\frac12|u^2-u_0^2|^{3/2}$, 
which yields 
\begin{equation}\label{e-z31}
   |\exp(-2\alpha(z))|\le 
\exp\bigl(-\frac1{24}|u^2-u_0^2|^{3/2}\bigr) < 1, 
\end{equation} 
provided  $\epsilon'$ is sufficiently small so that 
\begin{equation}\label{e-z22}
   O(|u^2-u_0^2|^{5/2})+O(|u^2-u_0^2|^{3/2}u_0^2)
\le c|u^2-u_0^2|^{3/2}(|u^2-u_0^2|+u_0^2) \le\frac1{24} |u^2-u_0^2|^{3/2}
\end{equation}
for $u\in\Sigma'_4\cap\mathcal{O}'$, where the terms on the LHS 
are given in~\eqref{8.2}.
The same choice of $\epsilon'$ gives rise the same 
result for $z\in u^{-1}(\Sigma'_3 \cap\mathcal{O}')$, and 
also $|\exp(2\alpha(z))|\le \exp(-\frac1{24}|u^2-u_0^2|^{3/2}) < 1$ 
for $z\in u^{-1}((\Sigma'_1\cup\Sigma'_2)\cap\mathcal{O}')$.
We thus fix $\Sigma^{(3)}$ by choosing 
\begin{equation}\label{e-z23}
   \Sigma^{(3)}\equiv u^{-1}(\Sigma'\cap\mathcal{O}') 
\quad\text{inside $\mathcal{O}'$}, 
\end{equation}
and extending it to a contour of the general shape 
$\bar{C}_1\cup\wt{C}_{inside}\cup\wt{C}_{outside}$ 
as in Figure~\ref{fig-Cinout}.

Define 
\begin{equation}
  \begin{cases}
    m_p(z)=m^{PII,3}\bigl(\frac{q^{1/3}}{2^{4/3}}u(z),x\bigr)& 
\quad\text{in} \quad\mathcal{O}-\Sigma^{(3)},\\
    m_p(z)= I& \quad\text{in}\quad\bar{\mathcal{O}}^c-\Sigma^{(3)},
  \end{cases}
\end{equation}
where $m^{PII,3}(z,x)$ solves the RHP of Painlev\'e II equation 
given by~\eqref{e-z17} and~\eqref{e-vPII4}.
Then $m_p$ solves the RHP on $\Sigma^{(3)}\cup\partial\mathcal{O}$ 
in which the jump matrix $v_p(z)$ is given by 
\begin{equation}
  \begin{cases}
    v^{PII,3}(\frac{q^{1/3}}{2^{4/3}}u(z))&\quad 
z\in\Sigma^{(3)}\cap\mathcal{O},\\
    I& \quad z\in\Sigma^{(3)}\cap\mathcal{O}^c,\\
    m_{p+}(z)& \quad z\in\partial\mathcal{O},
  \end{cases}
\end{equation}
where $v^{PII,3}$ is given in~\eqref{e-vPII4}.

We compare 
$v^{(3)}$ and $v_p$.
First, let $z\in \Sigma^{(3)}\cap\mathcal{O}$
such that $u(z)\in\Sigma'_4\cap\mathcal{O}'$. 
The $12$-entries of $v^{(3)}$ and $v_p$ are 
$-\exp(-2q\alpha(z))$ and $-\exp(-2ig^{PII}(\frac{q^{1/3}}{2^{4/3}}u(z)))
=-\exp(-\frac{iq}6(u^2-u_0^2)^{3/2})$, respectively.
With $\epsilon'$ chosen small as above, using 
\begin{align*}
  &Re(-i(u^2-u_0^2)^{3/2})\le -\frac12|u^2-u_0^2|^{3/2},\\
  &u_0^2\le \frac{4M_4}{q^{2/3}},\\
  &\|x^{5/2}e^{-x^{3/2}}\|_{L^{\infty}[0,\infty)} \le C,\\
  &\gamma-1 \le \frac{M_4}{2^{1/3}q^{2/3}},
\end{align*}
we obtain from~\eqref{8.2},
\begin{equation}
  \begin{split}
    &|e^{-2q\alpha(z)} - e^{-2ig^{PII}(\frac{q^{1/3}}{2^{4/3}}u(z))}|\\ 
    &\qquad \le e^{Re(-\frac{iq}6(u^2-u_0^2)^{3/2})} 
|e^{-2q\alpha(z)+2ig^{PII}(\frac{q^{1/3}}{2^{4/3}}u(z))} -1|\\
    &\qquad \le Ce^{-\frac{q}{24}|u^2-u_0^2|^{3/2}} 
\bigl[ q|u^2-u_0^2|^{3/2}(|u^2-u_0^2|+u_0^2+(\gamma-1)) \bigr]\\
    &\qquad \le \frac{C(M_4)}{q^{2/3}}.
  \end{split}
\end{equation}
In a similar manner, for $z$ such that $u(z)\in\Sigma'_3\cap\mathcal{O}'$, 
same result holds and for $z\in\wt{C}_{outside}\cap\mathcal{O}$, 
the difference of the $21$-entries of $v^{(3)}$ and $v_p$ satisfies 
$|e^{2q\alpha(z)} - e^{2ig^{PII}(\frac{q^{1/3}}{2^{4/3}}u(z))}|
\le\frac{C(M_4)}{q^{2/3}}$.
For $z\in C_1$,  
$Re(-i(u^2-u_0^2)_-^{3/2})=-|u^2-u_0^2|^{3/2}$.  
Again by~\eqref{8.2}, 
the difference of the $11$-entries of $v^{(3)}$ and $v_p$ satisfies
$|e^{-2q\alpha_-(z)} - e^{-2ig_-^{PII}(\frac{q^{1/3}}{2^{4/3}}u(z))}|
\le\frac{C(M_4)}{q^{2/3}}$.
Therefore, we have
\begin{equation}\label{8.7}
   \|v^{(3)}v_p^{-1} -I\|_{L^{\infty}(\Sigma^{(3)}\cap\mathcal{O})}
\le\frac{C(M_4)}{q^{2/3}}.
\end{equation}

Secondly, for $z\in\Sigma^{(3)}\cap\mathcal{O}^c$, 
$|z-\xi|,|z-\xi^{-1}|\geq c>0$ implies 
exponential decay for $e^{-2q\alpha(z)}$ and $e^{2q\alpha(z)}$ 
for $z\in\wt{C}_{inside}\cap\mathcal{O}^c$ and 
$z\in\wt{C}_{outside}\cap\mathcal{O}^c$, respectively.
Therefore we have 
\begin{equation}\label{8.8}
   \|v^{(3)}v_p^{-1} -I\|_{L^{\infty}(\Sigma^{(3)}\cap\mathcal{O}^c)} 
\le Ce^{-cq}.
\end{equation}

Finally, for $z\in\partial\mathcal{O}$, 
$|u(z)|=\epsilon'$ and 
\begin{equation}\label{8.9}
   m_{p+}(z)=m^{PII,3}\bigl(\frac{q^{1/3}}{2^{4/3}}u(z),x\bigr)
=I+\frac{m^{PII,3}_1(x)}{\frac{q^{1/3}}{2^{4/3}}u(z)}+ 
O_{M_4}(\frac1{q^{2/3}}),
\end{equation}
by~\eqref{e-z17}.
Here the error is uniformly for $0\le x\le 2M_4$.

Now as in the case $\gamma\le 1$, 
define $R(z)=m^{(3)}m_p^{-1}$. Then the jump matrix for $R$ is given by 
$v_R=m_{p-}v^{(3)}v_p^{-1}m_{p-}^{-1}$. From~\eqref{8.7},~\eqref{8.8} and ~\eqref{8.9}, 
and also~\eqref{e-unif4}, 
we have 
\begin{equation}
  \begin{cases}
    \|v_R-I\|_{L^{\infty}(\Sigma^{(3)}\cap\mathcal{O})} 
\le\frac{C(M_4)}{q^{2/3}}& \text{on $\mathcal{O} \cap \Sigma^{(3)}$},\\
    \|v_R-I\|_{L^{\infty}(\Sigma^{(3)}\cap\mathcal{O}^c)}
\le Ce^{-cq}& \text{on $\mathcal{O}^c \cap \Sigma^{(3)}$},\\
    v_R=m_{p+}^{-1}=I-\frac{2^{4/3}m^{PII,3}_1(x)}{q^{1/3}u(z)}
+O_{M_4}(\frac{1}{q^{2/3}})& 
\text{on $\partial \mathcal{O}$}.
  \end{cases}
\end{equation}

As in ~\eqref{e-R22K1} for the case $\gamma \le 1$, 
using $m_{1,22}^{PII}=m_{1,22}^{PII,3}+(ix^2/8)$
from ~\eqref{e-mPmP4},
\begin{equation}\label{e-z34}
  \begin{split}
    m_{22}^{(3)}(0)&= R_{22}(0)\\
    &= 1+\frac{i2^{4/3}}{q^{1/3}}m^{PII,3}_{1,22}(x)+O_{M_4}(\frac1{q^{2/3}})\\
    &= 1+\frac{i2^{4/3}}{q^{1/3}} \biggl[m^{PII}_{1,22}(x) 
-\frac{it^2}{8}\bigl( 1+\frac{t}{2^{1/3}q^{2/3}}\bigr)^{-4}\biggr] 
+O_{M_4}(\frac1{q^{2/3}})\\
    &= 1+\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(x) +
\frac{t^2}{2^{5/3}q^{1/3}} +O_{M_4}(\frac1{q^{2/3}}).
  \end{split}
\end{equation}
Therefore, from ~\eqref{e-Km3K2} 
using  $x=-t(1+\frac{t}{2^{1/3}q^{2/3}})^{-2}=-t+O_{M_4}(\frac1{q^{2/3}})$
and the fact that $\frac{d}{dt}m^{PII}_{1,22}(t)$ is bounded for $0\le t\le M_4$,
(this follows, for example from~\eqref{e-um1PII} and the boundedness of 
$u(x)=2im_{1,12}^{PII}$ ; alternatively statements like~\eqref{e-unif4} are true also 
for all the $x$-derivatives of $m^{PII,3}(z;x)$, etc.), 
\begin{equation}
  \begin{split}
  \kappa^2_{q-1}&=e^{q(-\gamma+\log \gamma+1)}m^{(3)}_{22}(0)\\
  & =e^{q(-\gamma+\log \gamma+1)} \biggl( 1 +\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(x) +\frac{t^2}{2^{5/3}q^{1/3}} +O_{M_4}(\frac1{q^{2/3}}) \biggr)\\
  & = \biggl( 1-\frac{t^2}{2^{5/3}q^{1/3}} +O_{M_4}(\frac1{q}) \biggr) 
\biggl( 1 +\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(x) 
+\frac{t^2}{2^{5/3}q^{1/3}} +O_{M_4}(\frac1{q^{2/3}}) \biggr) \\
  & =1 +\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(x) +O_{M_4}(\frac1{q^{2/3}})\\
  & =1 +\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(-t) +O_{M_4}(\frac1{q^{2/3}}).
  \end{split}
\end{equation}


\bigskip
Finally we consider the case (ii), $1+\frac{M_3}{2^{1/3}q^{2/3}}\le 
\gamma\le 1+\delta_4$.
We conjugate $m^{(2)}$ with jump matrix $v^{(2)}$ given 
by~\eqref{e-m2tilde}, as follows.\\
\begin{equation}
 \begin{cases}
    m^{(4)} \equiv m^{(2)} \qquad |z|>1,\\
    m^{(4)} \equiv m^{(2)} \bigl(\begin{smallmatrix} 0& 1\\-1&0 \end{smallmatrix} \bigr)
\quad |z|<1.
 \end{cases}
\end{equation}
Define $\wt{\alpha}(z)= -\pi i \int^z_\xi \frac\gamma{4\pi i} 
\frac{s+1}{s^2}\sqrt{(s-\xi)(s - \xi^{-1})}ds$, 
where $\wt{\alpha}(z)$ is the same as $\alpha(z)$ in Lemma~\ref{lem-alpha}, but 
now we choose the branch so that 
$\sqrt{(s-\xi)(s - \xi^{-1})}$ is analytic in $\C-\bar{C}_2$, and 
$\sqrt{(s-\xi)(s - \xi^{-1})} \sim +s$ as $s\to\infty$.
Then the jump matrix $v^{(4)}$ for $m^{(4)}$ is given by
\begin{equation}
 \begin{cases}
  v^{(4)}= \begin{pmatrix} e^{2q\wt{\alpha}_+} &1\\ 0&e^{2q\wt{\alpha}_-} 
\end{pmatrix} \ \ \text{on} \ \ C_2,\\
  v^{(4)}= \begin{pmatrix} 1&e^{-2q\wt{\alpha}}\\ 0&1 \end{pmatrix} \ \ \text{on} 
\ \ C_1
 \end{cases}
\end{equation}
and $\kappa^2_{q-1}=-e^{q(-\gamma+\log \gamma+1)}m^{(4)}_{21}(0)$.
\begin{figure}[ht]
 \centerline{\epsfig{file=Ctilde.eps, width=6cm}}
 \caption{}\label{fig-Ctilde}
\end{figure}
Noting the factorization $v^{(4)}=\begin{pmatrix} 
1&0\\ e^{2q\wt{\alpha}_-}&1 \end{pmatrix}$
$\begin{pmatrix} 0&1\\-1&0 \end{pmatrix}$
$\begin{pmatrix} 1&0\\e^{2q\wt{\alpha}_+}&1 \end{pmatrix}$ on $C_2$,
we define (see Figure~\ref{fig-Ctilde}) 
\begin{equation*}
  \begin{cases}
     m^{(5)}=m^{(4)} \begin{pmatrix} 1&0\\ e^{2q\wt{\alpha}}&1 \end{pmatrix}^{-1}
\quad\text{in}\quad \Omega^{(5)}_2,\\
     m^{(5)}=m^{(4)} \begin{pmatrix} 1&0\\ e^{2q\wt{\alpha}}&1 \end{pmatrix}
\qquad\text{in}\quad \Omega^{(5)}_3,\\
     m^{(5)}=m^{(4)} 
\qquad\text{in}\quad \Omega^{(5)}_1\cup\Omega^{(5)}_4,
  \end{cases}
\end{equation*}
so that 
\begin{equation*}
  \begin{cases}
    v^{(5)}=\begin{pmatrix} 0&1\\-1&0 \end{pmatrix} \quad\text{on}\quad C_2,\\
    v^{(5)}=\begin{pmatrix} 1&e^{-2q\wt{\alpha}}\\ 0&1 \end{pmatrix} \quad\text{on}\quad C_1,\\
    v^{(5)}=\begin{pmatrix} 1&0\\ e^{2q\wt{\alpha}}&1 \end{pmatrix}
\quad\text{on}\quad \wt{C}_{inside}\cup \wt{C}_{outside}.
  \end{cases}
\end{equation*}

As in the case of $\alpha$, we have $|e^{-\wt{\alpha}(z)}|<1$ for $z\in C_1$ and 
$|e^{\wt{\alpha}(z)}|<1$ for $z\in \wt{C}_{inside}\cup \wt{C}_{outside}$.
Therefore taking $q\to\infty$, we have 
\begin{equation}
\begin{cases}
v^{(5,\infty)} =
 \begin{pmatrix} 0&1\\-1&0 \end{pmatrix} \ \ \text{on} \ \ C_2,\\
v^{(5,\infty)} =
 \begin{pmatrix} 1&0\\0&1 \end{pmatrix} \ \ \text{on} \ \ C_1.
\end{cases}
\end{equation}
This RHP can be solved explicitly as in Lemma ~\ref{lem-minfty}, 
and we find
\begin{equation}\label{e-z24}
m^{(5,\infty)} = \begin{pmatrix} \frac12(\wt{\beta}+\wt{\beta}^{-1})& 
\frac1{2i}(\wt{\beta}-\wt{\beta}^{-1})\\
      -\frac1{2i}(\wt{\beta}-\wt{\beta}^{-1})& 
\frac12(\wt{\beta}+\wt{\beta}^{-1}) \end{pmatrix}
\end{equation}
where $\wt{\beta}(z)\equiv (\frac{z-\xi}{z-\xi^{-1}})^{1/4}$ 
is now analytic in $\C-\bar{C}_2$ and 
$\wt{\beta}\sim +1$ as $z\to\infty$.
From~\eqref{e-z24}, we have $m^{(5,\infty)}_{21}(0)=-\frac1{\sqrt{\gamma}}$ and 
$\kappa^2_{q-1}\sim e^{q(-\gamma+\log \gamma+1)}\frac1{\sqrt{\gamma}}$ 
as $q\to\infty$.
Again, we need to construct parametrices around $\xi$ and $\xi^{-1}$ 
in order to prove 
that indeed $m^{(5)}\to m^{(5,\infty)}$.
Note that $\det m^{(5,\infty)}=1$ : this follows either by direct calculation 
or by a general argument as $\det v^{(5,\infty)}=1$.

Let $\Sigma''$ be the contour $\Sigma''=\R\cup\R_+e^{2\pi i/3}\cup\R_+e^{4\pi i/3}$ 
shown in Figure~\ref{fig-Sigma2}.
\begin{figure}[ht]
 \centerline{\epsfig{file=Sigma2.eps, width=7cm}}
 \caption{$\Sigma''$ and $v_{\Psi}$}\label{fig-Sigma2}
\end{figure}
Let $\omega=e^{2\pi i/3}$ and set (see \cite{DZ})
\begin{equation}
  \begin{cases}
        \Psi(s)=\begin{pmatrix}Ai(s)&Ai(\omega^2s)\\
Ai'(s)&\omega^2Ai'(\omega^2s) \end{pmatrix}
e^{-\frac{i\pi}{6}}\sigma_3, &\quad 0< arg s < \frac{2\pi}{3},\\
        \Psi(s)=\begin{pmatrix}Ai(s)&Ai(\omega^2s)\\
Ai'(s)&\omega^2Ai'(\omega^2s) \end{pmatrix}
e^{-\frac{i\pi}{6}\sigma_3}\begin{pmatrix}1&0\\-1&1\end{pmatrix}, 
&\quad \frac{2\pi}{3}< arg s <\pi, \\
        \Psi(s)=\begin{pmatrix}Ai(s)&-\omega^2Ai(\omega s)\\
Ai'(s)&-Ai'(\omega s) \end{pmatrix}
e^{-\frac{i\pi}{6}\sigma_3}\begin{pmatrix}1&0\\1&1\end{pmatrix}, 
&\quad \pi < arg s < \frac{4\pi}{3}, \\
        \Psi(s)=\begin{pmatrix}Ai(s)&-\omega^2Ai(\omega s)\\
Ai'(s)&\omega Ai'(\omega s) \end{pmatrix}
e^{-\frac{i\pi}{6}}\sigma_3, &\quad \frac{4\pi}{3}<arg s <2\pi,\\
\end{cases}
\end{equation}
where $Ai(s)$ is the Airy function.
Then $\Psi$ satisfies the jump conditions 
\begin{equation}
  \begin{cases}
        \Psi_+=\Psi_-\begin{pmatrix}1&1\\0&1\end{pmatrix}& \quad z\in \R_+,\\
        \Psi_+=\Psi_-\begin{pmatrix}0&1\\-1&0\end{pmatrix}& \quad z\in \R_-,\\
        \Psi_+=\Psi_-\begin{pmatrix}1&0\\1&1\end{pmatrix}& 
\quad z\in \R_+e^{2\pi i/3}, \R_+e^{4\pi i/3}.\\
  \end{cases}
\end{equation}

Let $\mathcal{O}_{\xi}$ and ${\mathcal{O}}_{\bar{\xi}}$ be neighborhoods 
around $\xi$ and $\bar{\xi}$ of size 
$\epsilon''\sqrt{\gamma-1}$, respectively, where $\epsilon''>0$ is a small,  
fixed number chosen to satisfy~\eqref{e-z25},~\eqref{e-z26} below.
Since $\frac12 |\xi-\bar{\xi}|=\frac2{\gamma}\sqrt{\gamma-1} > 
\epsilon''\sqrt{\gamma-1}$, 
$\mathcal{O}_{\xi}$ and ${\mathcal{O}}_{\bar{\xi}}$ have no intersection, 
provided 
\begin{equation}\label{e-z25}
   0<\epsilon''<1.
\end{equation}
For definiteness we assume that $\partial\mathcal{O}_{\xi}$ and 
$\partial{\mathcal{O}}_{\bar{\xi}}$ are oriented counterclockwise.
In $\mathcal{O}_{\xi}$, a simple substitution shows that 
$\wt{\alpha}(z)=\frac23(z-\xi)^{3/2}G(z)$,
where $G$ is analytic and $G(\xi)=(\gamma-1)^{3/4}
e^{-i(\frac32\theta_c+\frac34\pi)}$.
Here $(z-\xi)^{3/2}=|z-\xi|^{3/2}e^{\frac32 i arg(z-\xi)}$ and
$\theta_c-\pi/2 < arg(z-\xi) <\theta_c+ 3\pi /2$.
Define
\begin{equation}
\lambda(z)\equiv (z-\xi)(G(z))^{2/3},
\end{equation}
where $(G(z))^{2/3}$ is analytic in $\mathcal{O}_{\xi}$ and 
$(G(z))^{2/3}\to (\gamma-1)^{1/2}e^{-i(\theta_c+\pi /2)}$ as $z\to\xi$.
Of course, $\lambda^{3/2}=\frac32 \wt{\alpha}$.
\begin{figure}[ht]
 \centerline{\epsfig{file=maptil.eps, width=10cm}}
 \caption{}\label{fig-maptil}
\end{figure}
It is a simple calculus question to verify that we may choose $\epsilon''$ 
sufficiently small so that 
\begin{equation}\label{e-z26}
  \begin{split}
   &\text{$z\to\lambda(z)$ is a bijection from $\mathcal{O}_{\xi}$ 
onto an open neighborhood}\\
   &\text{of $0$ in the $\lambda$-plane, 
of radius $\sim (\gamma-1)$.}
  \end{split}
\end{equation}

Define $\Sigma^{(5)}\cap\mathcal{O}_{\xi}\equiv 
\{ z\in\mathcal{O}_{\xi} : \lambda(z)\in\Sigma''\}$.
As in the construction in \cite{DZ}, set (cf. (4.34) in \cite{DZ}) 
\begin{equation}\label{8.20}
   E(z) =\begin{pmatrix}1&-1\\-1&-1\end{pmatrix}
\sqrt\pi e^{i\pi/6}q^{\frac{\sigma_3}{6}}
\biggl((z-\bar\xi)(G(z))^{2/3}\biggr)^{\frac{\sigma_3}{4}}, 
\end{equation}
and for $z\in\mathcal{O}_{\xi}-\Sigma^{(5)}$, define the parametrix 
for $m^{(5)}$ by  
\begin{equation}
    m_p(z)=E(z)\Psi(q^{2/3}\lambda(z))e^{q\wt{\alpha}(z)\sigma_3}.
\end{equation}
Then $m_p$ satisfies the same jump conditions 
on $\Sigma^{(5)}\cap\mathcal{O}_{\xi}$ as $m^{(5)}$ ; $m_{p+}=m_{p-}v^{(5)}$.
And if $q$ becomes large, then 
for $z\in\partial\mathcal{O}_{\xi}$,
$|q^{2/3}\lambda(z)|\geq cq^{2/3}(\gamma-1) 
\geq cM_3/2^{1/3}$.
Therefore, 
\begin{equation}\label{e-z29}
 \begin{split}
  &\text{if $M_3$ is sufficiently large so that the leading terms dominate}\\ 
  &\text{in the asymptotics for the Airy functions in $\Psi(q^{2/3}\lambda(z))$ 
(see e.g.\cite{AS}),}
 \end{split}
\end{equation}
then by the explicit choice of $E(z)$ in~\eqref{8.20}, we find 
for $z\in\partial\mathcal{O}_{\xi}$, 
\begin{equation}\label{e-z27}
  m_{p+}=m^{(5,\infty)}(z)\biggl(I+O\bigl(\frac1{q\lambda^{3/2}(z)}\bigr)\biggr)
=m^{(5,\infty)}(z)\biggl(I+O\bigl(\frac1{q(\gamma-1)^{3/2}}\bigr)\biggr). 
\end{equation}

Noting the symmetry $m^{(5)}=\overline{m^{(5)}(\bar{z})}$, 
define $\Sigma^{(5)}\cap\mathcal{O}_{\bar{\xi}}\equiv 
\overline{\Sigma^{(5)}\cap\mathcal{O}_{\xi}}$, and 
for $z\in\mathcal{O}_{\bar{\xi}}-\Sigma^{(5)}$ 
set $m_p(z)=\overline{m_p(\bar{z})}$.
We now extend $\Sigma^{(5)}\cap(\mathcal{O}_{\xi}\cup\mathcal{O}_{\bar{\xi}})$ 
to $\Sigma^{(5)}$ to have the same general shape as in Figure~\ref{fig-Ctilde}. 
Finally, for $z\in\C-({\mathcal{O}}_\xi 
\cup {\mathcal{O}}_{\bar{\xi}} \cup\Sigma^{(5)})$, 
define $m_p(z)=m^{(5,\infty)}$.

Set $\mathcal{O}= {\mathcal{O}}_\xi\cup {\mathcal{O}}_{\bar{\xi}}$.
Then $\wt{R}\equiv m^{(5)}m_p^{-1}$ solves a RHP on 
$\Sigma^{(5)}\cup\partial\mathcal{O}$ with 
the jump matrix $v_{\wt{R}}=m_{p-}v^{(5)}v_p^{-1}m_{p-}^{-1}$, 
\begin{equation}
  \begin{cases}
    v_{\wt{R}}= I& \text{on} \quad (\Sigma^{(5)}\cap\mathcal{O})\cup C_2,\\
    v_{\wt{R}}= m^{(5,\infty)} \begin{pmatrix} 1&e^{-2q\wt{\alpha}}\\ 0&1 
\end{pmatrix} (m^{(5,\infty)})^{-1}& 
\text{on} \quad  C_1 \cap\bar{\mathcal{O}}^c, \\
    v_{\wt{R}}= m^{(5,\infty)} \begin{pmatrix} 1&0\\ 
e^{2q\wt{\alpha}}&1 \end{pmatrix}
(m^{(5,\infty)})^{-1}& \text{on} \quad 
(\wt{C}_{inside}\cup\wt{C}_{outside})\cap\bar{\mathcal{O}}^c ,\\
    v_{\wt{R}}=I+O(\frac1{q(\gamma-1)^{3/2}})& \text{on} 
\quad \partial\mathcal{O}.\\
  \end{cases}
\end{equation}

Let $\epsilon_1>0$ be a fixed, small number : for example, we may take 
$\epsilon_1=\epsilon'$ satisfying~\eqref{e-z21},~\eqref{e-z22} above.
Choose $\delta_4$ sufficiently small so that 
\begin{equation}\label{e-z30}
   \xi,\bar{\xi} \in \{z : |z+1|\le\epsilon_1\}
\end{equation}
for $1\le\gamma\le 1+\delta_4$.
By calculations similar to~\eqref{8.2} and~\eqref{e-z31}, 
$Re(2\tilde\alpha(z))\leq -c(\gamma-1)^{3/2}$ for
$z\in (\wt{C}_{inside}\cup\wt{C}_{outside})\cap \{|z+1|\le\epsilon_1\}
\cap \bar{\mathcal{O}}^c$ (in fact the estimate is true on the full set 
$(\wt{C}_{inside}\cup\wt{C}_{outside})\cap \{|z+1|\le\epsilon_1\}$) 
and also $|e^{2q\tilde\alpha(z)}|\leq e^{-cq}$ for 
$z\in (\wt{C}_{inside}\cup\wt{C}_{outside})\cap \{|z+1|>\epsilon_1\}$.
Thus, 
$|e^{2q\tilde\alpha(z)}|\leq e^{-cq(\gamma-1)^{3/2}}$ for 
$z\in (\wt{C}_{inside}\cup\wt{C}_{outside})\cap \mathcal{O}^c$. 
Also, by calculations similar to~\eqref{8.2} and~\eqref{e-z31} again,
$Re(-2\tilde\alpha(z))\leq -c(\gamma-1)^{3/2}$ for 
$z\in C_1\cap \mathcal{O}^c$. 
Therefore we have $L^{\infty}$ estimation 
\begin{equation}\label{e-z32}
   \|v_{\wt{R}} -I \|_{L^\infty(\Sigma^{(5)}\cap\mathcal{O}^c)}
\leq Ce^{-cq(\gamma-1)^{3/2}}.
\end{equation}

Furthermore, from calculations similar to~\eqref{6.9},  
on $\wt{C}_{inside}\cap\mathcal{O}^c\cap \{Im(z)\geq0\}$,  
using $|u+u_0|\geq |u-u_0|$ on the integration contour for the second inequality, 
\begin{equation}
  \begin{split}
    \int |e^{-2q\wt{\alpha}(z)}||dz|
    &\le \int_{\{u=u_0+xe^{-i\pi/3} : x\geq c\sqrt{\gamma-1}\}}
Ce^{-qc|u^2-u^2_0|^{3/2}}du + Ce^{-cq}\\
    &\le \int_{c\sqrt{\gamma-1}}^{\infty} 
Ce^{-qcx^{3}} dx + Ce^{-cq}\\
    &\le  \frac{C}{q(\gamma-1)}.
  \end{split}
\end{equation}
The same calculations apply to the other part of 
$\wt{C}_{inside}\cap\mathcal{O}^c$ and also 
to $\wt{C}_{outside}\cap\mathcal{O}^c$, 
so that 
$\|v_{\wt{R}}-I\|_{L^1((\wt{C}_{inside}\cup\wt{C}_{outside})\cap\mathcal{O}^c)}
\le \frac{C}{q(\gamma-1)}$.
On the other hand, $length(\partial\mathcal{O})\le C\sqrt{\gamma-1}$ and 
$length(C_1\cap\mathcal{O}^c)\le C\sqrt{\gamma-1}$, and hence, by the 
above $L^\infty$ estimates,  
$\|v_{\wt{R}}-I\|_{L^1(\partial\mathcal{O})}\le C/(q(\gamma-1))$ and 
$\|v_{\wt{R}}-I\|_{L^1(C_1\cap\mathcal{O}^c)}\le C/(q(\gamma-1))$.
Thus 
\begin{equation}\label{e-z33}
   \|v_{\wt{R}}-I\|_{L^1(\Sigma^{(5)}\cup\partial\mathcal{O})}\le 
\frac{C}{q(\gamma-1)}.
\end{equation}

Using the choice of $\mathcal{O}_{\xi}$ and $\mathcal{O}_{\bar{\xi}}$, direct 
calculation shows that $m^{(5,\infty)}$, hence $(m^{(5,\infty)})^{-1}$ (as 
$\det m^{(5,\infty)}=1$), are uniformly bounded for $\gamma$ in the region 
$1+\frac{M_3}{2^{1/3}q^{2/3}}\le \gamma \le 1+\delta_4$,  
for $z\in\mathcal{O}^c - \Sigma^{(5)}$.
On the other hand, even though the contour $\Sigma^{(5)}\cup\partial\mathcal{O}$ 
varies with $\gamma$ and $q$, the length of $\Sigma^{(5)}\cup\partial\mathcal{O}$ 
is uniformly bounded for $1+\frac{M_3}{2^{1/3}q^{2/3}}\le \gamma \le 1+\delta_4$.
Also a simple scaling argument shows that the Cauchy operators $C_\pm$ on 
$L^2(\Sigma^{(5)}\cup\partial\mathcal{O})$ are uniformly bounded for 
$1+\frac{M_3}{2^{1/3}q^{2/3}}\le \gamma \le 1+\delta_4$.
Therefore,  
\begin{equation}\label{e-z28}
  \begin{split}
    \|C_{w_{\wt{R}}}\|_{L^2(\Sigma^{(5)}\cup\partial\mathcal{O})
\to L^2(\Sigma^{(5)}\cup\partial\mathcal{O})} 
&\le C\|w_{\wt{R}}\|_{L^\infty(\Sigma^{(5)}\cup\partial\mathcal{O})}\\
    &\le \frac{C}{q(\gamma-1)^{3/2}}+Ce^{-Cq(\gamma-1)^{3/2}}\\
    &\le \frac{C}{M_3^{2/3}}+Ce^{-CM_3^{3/2}}\\
    &\le \frac12 <1
  \end{split}
\end{equation}
provided that $M_3$ is sufficiently large.

From~\eqref{e-sam5} and~\eqref{e-z33}, we have 
\begin{equation*}
  \begin{split}
    |\wt{R}_{22}(0) -1| &= \biggl| \frac1{2\pi i} 
\int_{\Sigma^{(5)}\cup\partial\mathcal{O}} \biggl( 
\frac{w_{\wt{R}}-[(I-C_{w_{\wt{R}}})^{-1}C_{w_{\wt{R}}}I](z)
w_{\wt{R}}(z)}{z}\,ds 
\biggr)_{22} \biggr|\\
    &\le C(\|w_{\wt{R}}\|_{L^1(\Sigma^{(5)}\cup\partial\mathcal{O})}+
\|w_{\wt{R}}\|^2_{L^2(\Sigma^{(5)}\cup\partial\mathcal{O})}) \\
    &\le C\|w_{\wt{R}}\|_{L^1(\Sigma^{(5)}\cup\partial\mathcal{O})} 
\qquad\text{, as $\|w_{\wt{R}}\|
_{L^\infty(\Sigma^{(5)}\cup\partial\mathcal{O})}$ is bounded,}\\
    &\le\frac{C}{q(\gamma-1)},
  \end{split}
\end{equation*}
and 
\begin{equation*}
 |\wt{R}_{21}(0)| \le \frac{C}{q(\gamma-1)}.
\end{equation*}
Therefore, from $m^{(5)}_{21}(0)=\wt{R}_{22}(0)m^{(5,\infty)}_{21}(0)+
\wt{R}_{21}(0)m^{(5,\infty)}_{11}(0)$, we obtain 
\begin{equation}
  \kappa^2_{q-1}
=-e^{q(-\gamma+\log \gamma+1)}m^{(5)}_{21}(0)
=e^{q(-\gamma+\log \gamma+1)} \frac1{\sqrt{\gamma}} 
\biggl(1+O\bigl( \frac1{q(\gamma-1)} \bigr)\biggr).
\end{equation}
Note that this is consistent with the result~\eqref{8.1} for case (i) 
where $\gamma-1\geq \delta_3$.


Summarizing, we have proven the following results.
\begin{lem}\label{lem-K2}
  Let $\delta_3, M_4>0$ be fixed numbers.
  Let $\delta_4>0$ be a fixed sufficiently 
small number satisfying~\eqref{e-z30}, 
and $M_3>0$ be a fixed, sufficiently large number 
satisfying~\eqref{e-z29} and~\eqref{e-z28}.
As $q \to \infty$, we have the following asymptotics.
  \begin{enumerate}
    \item If $1+\delta_3 \le \gamma$,
\begin{equation*}
  \kappa^2_{q-1}
= e^{q(-\gamma+\log \gamma+1)}\frac1{\sqrt{\gamma}}
\biggl(1+O\bigl(\frac1{q}\bigr)\biggr),
\end{equation*}
where the error is uniform for $1+\delta_4 \le \gamma\le L$ for 
any fixed $L< \infty$.
    \item If $1+\frac{M_3}{2^{1/3}q^{2/3}} \le \gamma \le 1+\delta_4$,
\begin{equation*}
  \kappa^2_{q-1}=e^{q(-\gamma+\log \gamma+1)} \frac1{\sqrt{\gamma}}
\biggl(1+O\bigl(\frac1{q(\gamma-1)}\bigr) \biggr),
\end{equation*}
where the error is uniform in the region.
    \item If $1< \gamma \le 1+\frac{M_4}{2^{1/3}q^{2/3}}$, 
\begin{equation*}
  \bigl|\kappa^2_{q-1}
- 1 -\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(-t)\bigr|\le  \frac{C(M_4)}{q^{2/3}},
\end{equation*}
where $t$ is defined by $\gamma=1+\frac{t}{2^{1/3}q^{2/3}}$, $0\le t\le M_4$.
  \end{enumerate}
\end{lem}

Note that, comparing Lemma ~\ref{lem-K2} (iii) with Lemma ~\ref{lem-K1} (iii), 
we have same result everywhere in the region $1-\frac{M}{2^{1/3}q^{2/3}} \le 
\gamma \le 1+\frac{M}{2^{1/3}q^{2/3}}$, 
\begin{equation}\label{e-z36}
     \bigl|\kappa^2_{q-1}
- 1 -\frac{i2^{4/3}}{q^{1/3}}m^{PII}_{1,22}(t)\bigr|\le  \frac{C(M)}{q^{2/3}},
\end{equation}
where $t$ is defined by $\gamma=1-\frac{t}{2^{1/3}q^{2/3}}$, 
and $M$ is any fixed positive number.

Also note from Lemma~\ref{lem-K2} (ii), that as $q\to\infty$, 
\begin{equation}\label{e-z37}
   \log\kappa^2_{q-1}\le q(-\gamma+\log\gamma +1) + \frac{C^{\#}}{q(\gamma-1)},
\end{equation}
where $C^{\#}$ is independent of $M_3$ and is fixed once $\delta_4$ 
satisfying~\eqref{e-z30} is determined.





\bigskip

\section{\bf{Asymptotics of $\mathbf{\phi_n(\lambda)}$ as $\mathbf{ n\to\infty}$ }}
\label{s-phi}

In this Section, using Lemmas~\ref{lem-K1} and~\ref{lem-K2}, 
we obtain the large $n$ behavior of $\phi_n(\lambda)$.
In the following $\delta_5,\delta_6,\delta_7$ are fixed numbers 
between $0$ and $1$, and 
$M_5,M_6,M_7$ are fixed and positive.
These numbers are free apart from the following requirements : 
\begin{align*}
   &\text{(a) $\delta_6$ satisfies~\eqref{e-z30},}\\
   &\text{(b) $M_5\geq 1$ satisfies~\eqref{e-sec3.6},}\\
   &\text{(c) $\frac12 M_6\geq 1$ satisfies~\eqref{e-sec3.6}, and}\\
   &\text{(d) $M_7\geq 1$ satisfies~\eqref{e-z29}, ~\eqref{e-z28} 
and condition~\eqref{e-z39} below.}
\end{align*}
We consider the following five cases for $\lambda>0$ and $n$ :
\begin{enumerate}
   \item $0\le \frac{2\sqrt{\lambda}}{n+1}\le 1-\delta_5$
   \item $\frac12 \le \frac{2\sqrt{\lambda}}{n+1} 
\le 1-\frac{M_5}{2^{1/3}{(n+1)}^{2/3}}$
   \item $1-\frac{M_6}{2^{1/3}{(n+1)}^{2/3}} \le \frac{2\sqrt{\lambda}}{n+1} 
\le 1+\frac{M_6}{2^{1/3}{(n+1)}^{2/3}}$
   \item $1+\frac{M_7}{2^{1/3}{(n+1)}^{2/3}} \le \frac{2\sqrt{\lambda}}{n+1}
\le 1+\delta_6$
   \item $1+\delta_7 \le \frac{2\sqrt{\lambda}}{n+1}$
\end{enumerate}

\bigskip
Consider case (i). 
For any $k\geq n$, $\frac{2\sqrt{\lambda}}{k+1}\le 1-\delta_5$. 
From Lemma~\ref{lem-K1} (i), we have as $n\to\infty$, 
\begin{equation}
   |\log{\phi_n(\lambda)}|
   =\bigl|\sum_{k=n}^{\infty} \log{\kappa^2_k}(\lambda)\bigr|
   \le \sum_{k=n}^{\infty} Ce^{-ck} \le Ce^{-cn}.
\end{equation}

\bigskip
Consider case (ii).
We split the sum into two pieces.
\begin{equation*}
   \begin{split}
      \log{\phi_n(\lambda)}
      &=\sum_{k=n}^{\infty} \log{\kappa^2_k}(\lambda)\\
      &=\sum_{(1)} \log{\kappa^2_{k}}(\lambda)
      + \sum_{(2)} \log{\kappa^2_{k}}(\lambda)
  \end{split}
\end{equation*}
where $(1)$ and $(2)$ represent the regions
\begin{align*}
  (1)\ \  &n+1\le k+1 \le 4\sqrt{\lambda},\\
  (2)\ \  &4\sqrt{\lambda} <k+1. 
\end{align*}
For $(1)$, $\frac12 \le \frac{2\sqrt{\lambda}}{k+1}\le
1-\frac{M_5}{2^{1/3}(k+1)^{2/3}}$.
From Lemma~\ref{lem-K1} (ii), for some constant $C$, independent of $M_5$ 
satisfying~\eqref{e-sec3.6},
\begin{equation*}
  \bigl| \log \kappa^2_k(\lambda) \bigr|
\le C\frac{ {e^{-\frac{2\sqrt{2}}{3}(k+1)
{(1-\frac{2\sqrt\lambda}{k+1})}^{3/2}}}}{{(k+1)}^{1/3}}.
\end{equation*}
Using the fact that 
$f(x)=\frac1{x^{1/3}}e^{-\frac{2\sqrt{2}}{3}x(1-\frac{2\sqrt{\lambda}}{x})^{3/2}}$ 
is monotone decreasing in the second inequality below, 
we have, as $n\to\infty$,  
\begin{equation}\label{e-z3}
  \begin{split}
    \bigl|\sum_{(1)} \log{\kappa^2_{k}}(\lambda) \bigr|
    &\le C\sum_{(1)} \frac{e^{-\frac{2\sqrt{2}}{3}(k+1)
(1-\frac{2\sqrt{\lambda}}{k+1})^{3/2}}}
{{(k+1)}^{1/3}}\\
    &\le C\int_{n+1}^{4\sqrt{\lambda}}
e^{-\frac{2\sqrt{2}}{3}x(1-\frac{2\sqrt{\lambda}}{x})^{3/2}}
\frac{dx}{x^{1/3}}
+C\frac{e^{-\frac{2\sqrt{2}}{3}(n+1)
(1-\frac{2\sqrt{\lambda}}{n+1})^{3/2}}}{{(n+1)}^{1/3}}\\
    &\le C(2\sqrt{\lambda})^{2/3}\int_{\frac{(n+1)}{2\sqrt{\lambda}}-1}^{1}
e^{-\frac{4\sqrt{2\lambda}y^{3/2}}{3(1+y)^{1/2}}}
\frac{dy}{(1+y)^{1/3}}
+Ce^{-\frac12(n+1)(1-\frac{2\sqrt{\lambda}}{n+1})^{3/2}}\\
    &\le C(2\sqrt{\lambda})^{2/3}\int_{\frac{(n+1)}{2\sqrt{\lambda}}-1}^{1}
e^{-\sqrt{\lambda}y^{3/2}} dy
+Ce^{-\frac12(n+1)(1-\frac{2\sqrt{\lambda}}{n+1})^{3/2}}\\
    &\le C\int_{\sqrt{\lambda}(\frac{(n+1)}{2\sqrt{\lambda}}-1)^{3/2}}^{\infty}
e^{-s}\frac{ds}{s^{1/3}}
+Ce^{-\frac12(n+1)(1-\frac{2\sqrt{\lambda}}{n+1})^{3/2}}\\
    &\le Ce^{-\sqrt{\lambda}(\frac{(n+1)}{2\sqrt{\lambda}}-1)^{3/2}}
+Ce^{-\frac12(n+1)(1-\frac{2\sqrt{\lambda}}{n+1})^{3/2}}\\
    &\le C\exp\biggl(-\frac12(n+1)
\bigl(1-\frac{2\sqrt{\lambda}}{n+1}\bigr)^{3/2}\biggr).
  \end{split}
\end{equation}
We use the change of variable $y=\frac{x}{2\sqrt{\lambda}}-1$ for 
the integral in the third line.
The fifth inequality is obtained from the substitution 
$s=\sqrt{\lambda}y^{3/2}$, 
and at the end, we have used $\frac{2\sqrt{\lambda}}{n+1} \le 1$.

For $(2)$, $\frac{2\sqrt{\lambda}}{k+1}\le \frac12$.
Therefore, from Lemma~\ref{lem-K1} (i), we have
\begin{equation*}
   \bigl|\sum_{(2)} \log{\kappa^2_k}(\lambda)\bigr|
   \le \sum_{k+1=[4\sqrt{\lambda}]}^{\infty} Ce^{-ck} \le Ce^{-cn}.
\end{equation*}

Summing up the above two calculations, we have, for case (ii), 
\begin{equation}\label{e-z35}
   |\log{\phi_n(\lambda)}| \le C\exp\biggl(-c(n+1)
\bigl(1-\frac{2\sqrt{\lambda}}{n+1}\bigr)^{3/2}\biggr),
\end{equation}
as $n\to\infty$.
Note again that the constants C,c can be taken independent of $M_5$.
 


 
\bigskip
Consider case (iii).
Set 
\begin{equation}\label{e-z38}
   \frac{2\sqrt{\lambda}}{n+1}=1-\frac{t}{2^{1/3}{(n+1)}^{2/3}}
\end{equation}
so that $-M_6\le t\le M_6$. 
We divide the sum into three pieces,  
\begin{equation*}
  \begin{split}
     \log{\phi_n(\lambda)}
     &=\sum_{k=n}^{\infty} \log{\kappa^2_k}(\lambda)\\
     &=\sum_{(1)} \log{\kappa^2_{k}}(\lambda) 
     + \sum_{(2)} \log{\kappa^2_{k}}(\lambda) 
     + \sum_{(3)} \log{\kappa^2_{k}}(\lambda)
  \end{split}
\end{equation*}
where $(1),(2)$ and $(3)$ indicate the following regions :
\begin{align*}
  (1)\ \  &n+1\le k+1 \le (n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}\\
  (2)\ \  &(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3} <k+1 
< \frac32(n+1)-\frac{t}{2^{1/3}}(n+1)^{1/3}\\
  (3)\ \  &\frac32(n+1)-\frac{t}{2^{1/3}}(n+1)^{1/3} \le k+1.
\end{align*}

\medskip
For $(1)$, as $n\to\infty$,  
\begin{equation*}
  1-\frac{6M_6}{2^{1/3}{(k+1)}^{2/3}} \le 
\frac{2\sqrt{\lambda}}{k+1} \le 1+\frac{2M_6}{2^{1/3}{(k+1)}^{2/3}}.
\end{equation*} 
Hence from~\eqref{e-z36}, 
we have as $k\geq n\to\infty$,  
\begin{equation*}
\log \kappa^2_k(\lambda)
= \frac{i2^{4/3}}{{(k+1)}^{1/3}} m^{PII}_{1,22}
\biggl(2^{\frac13}{(k+1)}^{\frac23}(1-\frac{2\sqrt{\lambda}}{k+1})\biggr) 
+O_{M_6}\bigl(\frac1{k^{2/3}}\bigr).
\end{equation*}
This leads to 
\begin{equation*}
  \begin{split}
    &\sum_{(1)} \log{\kappa^2_{k}}(\lambda)\\
    &= \sum_{k+1=n+1}^{[(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}]} 
\biggl[ \frac{i2^{4/3}}{{(k+1)}^{1/3}} 
m^{PII}_{1,22}(2^{\frac13}{(k+1)}^{\frac23}(1-\frac{2\sqrt{\lambda}}{k+1})) 
+ O_{M_6}\bigl(\frac1{k^{2/3}}\bigr) \biggr]\\
    &= \int_{(n+1)}^{(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}} 
\frac{i2^{4/3}}{x^{1/3}} 
m^{PII}_{1,22}(2^{1/3}x^{2/3}(1-\frac{2\sqrt{\lambda}}{x})) dx  +
O_{M_6}\bigl(\frac1{n^{1/3}}\bigr)\\
    &= \int_{0}^{\frac{(M_6-t)}{2^{1/3}}} i2^{4/3} 
m^{PII}_{1,22}\biggl(2^{1/3}{(n+1)}^{2/3}
(1+\frac{2s}{3{(n+1)}^{2/3}} +\cdots)\\ 
    &\qquad \bigl(1-\frac{(n+1)-\frac{t}{2^{1/3}}(n+1)^{1/3}}
{(n+1)+s{(n+1)}^{1/3}}\bigr)\biggr)
     \frac{ds}
{(1+\frac{s}{3{(n+1)}^{2/3}}+\cdots)} +
O_{M_6}\bigl(\frac1{n^{1/3}}\bigr)\\
    &=\int_0^{\frac{(M_6-t)}{2^{1/3}}} i2^{4/3} 
m^{PII}_{1,22}\biggl((t+2^{1/3}s)(1-\frac{s}{3{(n+1)}^{2/3}} +\cdots)\biggr)(1-\frac{s}{3{(n+1)}^{2/3}} +\cdots)ds \\
&\qquad + O_{M_6}\bigl(\frac1{n^{1/3}}\bigr)\\
    &= \int_0^{\frac{(M_6-t)}{2^{1/3}}} i2^{4/3} 
m^{PII}_{1,22}(t+2^{1/3}s) ds 
+O_{M_6}\bigl(\frac1{n^{1/3}}\bigr)\\
    &= \int_{t}^{M_6} 2im^{PII}_{1,22}(y) dy 
+O_{M_6}\bigl(\frac1{n^{1/3}}\bigr).
  \end{split}
\end{equation*}
The fourth equation is obtained using the change of variable 
$x=(n+1)+s{(n+1)}^{1/3}$, and for the sixth equation, 
we use the fact that $\frac{d}{dt}m^{PII}_{1,22}(t)$ 
is uniformly bounded for $-M_6\le t\le M_6$ 
(see the remark below~\eqref{e-z34}).
To pass from the second to the third line, note that 
for integers $b>a$, 
\begin{equation}\label{e-z40}
  \begin{split}
     |\sum_{n=a}^{b-1} f(x) - \int_a^b f(x)| &\le 
\sum_{n=a}^{b-1} sup\{ |f(\alpha)-f(\beta)| : n\le \alpha,\beta\le n+1\}\\ 
     & \le \|f'\|_{L^{\infty}(a,b)}(b-a).
  \end{split}
\end{equation}
For the case at hand, a simple calculation shows that 
$$\|f'\|_{L^\infty\bigl(n+1,[(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}]\bigr)} 
\le C(M_6)/n^{2/3}.$$
Also, the contribution to the integral from the interval 
$\bigl((n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3},
[(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}]+1\bigr)$ is $O_{M_6}(1/n^{1/3})$.

\medskip
For $(2)$, 
\begin{equation*}
   \frac12 \le \frac{2\sqrt\lambda}{k+1} \le 
1-\frac{\frac12M_6}{2^{1/3}(k+1)^{2/3}}\quad 
\text{as}\quad  k\geq n\rightarrow \infty.
\end{equation*}
As $n\to\infty$, by a calculation similar to the case (ii), again using 
the monotonicity of $f(x)=\frac1{x^{1/3}}
e^{-\frac{2\sqrt{2}}{3}x(1-\frac{2\sqrt{\lambda}}{x})^{3/2}}$ 
for the second inequality, 
we have  
\begin{equation*}
  \begin{split}
    \bigl|\sum_{(2)} \log{\kappa^2_{k}}(\lambda) \bigr| 
    &\le C\sum_{(2)} \frac{e^{-\frac{2\sqrt{2}}{3}(k+1)
(1-\frac{2\sqrt{\lambda}}{k+1})^{3/2}}}
{{(k+1)}^{1/3}}\\
    &\le C\int_{(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}}
^{\frac32(n+1)-\frac{t}{2^{1/3}}(n+1)^{1/3}} 
e^{-\frac{2\sqrt{2}}{3}x(1-\frac{2\sqrt{\lambda}}{x})^{3/2}} 
\frac{dx}{x^{1/3}}
+Ce^{-(\frac{M_6}2)^{3/2}}\\
    &\le C(2\sqrt{\lambda})^{2/3}
\int_{\frac{M_6(n+1)^{1/3}}{2^{4/3}\sqrt{\lambda}}}
^{\frac{(n+1)}{4\sqrt{\lambda}}} 
e^{-\frac{4\sqrt{2\lambda}}{3}(\frac{y^3}{1+y})^{1/2}}
\frac{dy}{(1+y)^{1/3}}
+Ce^{-(\frac{M_6}2)^{3/2}}\\
    &\le C(2\sqrt{\lambda})^{2/3}
\int_{\frac{M_6(n+1)^{1/3}}{2^{4/3}\sqrt{\lambda}}}
^{\frac{(n+1)}{4\sqrt{\lambda}}} 
e^{-\sqrt{\lambda}y^{3/2}} dy
+Ce^{-(\frac{M_6}2)^{3/2}}\\
    &\le C \int_{(\frac{n+1}{2\sqrt{\lambda}})^{\frac12}
(\frac{M_6}{2})^{\frac32}}^{\infty} 
e^{-s} \frac{ds}{s^{1/3}}
+Ce^{-(\frac{M_6}2)^{3/2}}\\
    &\le C\int_{\frac14M_6^{3/2}}^{\infty} \frac{e^{-s}}{s^{1/3}} ds
+Ce^{-(\frac{M_6}2)^{3/2}}\\
    &\le Ce^{-\frac14M_6^{3/2}}
+Ce^{-(\frac{M_6}2)^{3/2}}
\le Ce^{-\frac14M_6^{3/2}}.
  \end{split}
\end{equation*}
The first inequality follows from Lemma~\ref{lem-K1} (ii) (note that, 
by assumption, $\frac12 M_6$ satisfies~\eqref{e-sec3.6}).
For the second line, in order to control the contribution 
to the integral from the interval 
$[[(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}], 
(n+1)+\frac{(M_6-t)}{2^{1/3}}{(n+1)}^{1/3}]$, we use the inequality 
$1+\frac{M_6-t}{2^{1/3}(n+1)^{2/3}} \le 1+\frac{2^{2/3}M_6}{(n+1)^{2/3}}
\le \frac{32}{9}$ for large enough $n$.
For the third line, we use the change of variable 
$y=\frac{x}{2\sqrt{\lambda}}-1$, and 
for the fourth line, we use the inequality 
$\frac{4\sqrt{\lambda}}{(n+1)\delta} \geq 1-\frac{M_6}{2^{1/3}(n+1)^{2/3}}
\geq \frac9{23}$ for sufficiently large $n$. 
The fifth equation is obtained from the substitution $s=\sqrt{\lambda}y^{3/2}$,
and for the sixth line, we have used the inequality 
$\frac{2\sqrt{\lambda}}{n+1} \le 1+\frac{M_6}{2^{1/3}(n+1)^{2/3}} 
\le 2$ for sufficiently large $n$.

\medskip
For $(3)$, as $n\to\infty$,  $0\le \frac{2\sqrt\lambda}{k+1} \le \frac34$, 
which yields, from Lemma~\ref{lem-K1} (i), 
\begin{equation*}
   \bigl| \sum_{(3)} \log{\kappa^2_{k}(\lambda)} \bigr| \le Ce^{-cn}.
\end{equation*}

Summing up all these calculations, for 
$\frac{2\sqrt{\lambda}}{n+1} = 1- \frac{t}{2^{1/3}{(n+1)}^{2/3}}$ 
with $-M_6\le t\le M_6$, we have, as $n\to\infty$, 
\begin{equation*}
  \bigl| \log{\phi_n(\lambda)} - \int_{t}^{M_6} 2im^{PII}_{1,22}(y) dy \bigr|
\le \frac{C(M_6)}{n^{1/3}}+Ce^{-\frac14M_6^{3/2}}, 
\end{equation*}
for a constant $C(M_6)$ which depends on $M_6$, and for a 
constant $C$ which is independent of $M_6$. 
Using the asymptotics of $m^{PII}_{1,22}(x)$ as 
$x\rightarrow +\infty$ (see~\eqref{e-aympm_1}), we have 
(recall $\frac12 M_6\geq 1$) 
\begin{equation}
  \bigl| \log{\phi_n(\lambda)} - \int_{t}^{\infty} 2im^{PII}_{1,22}(y) dy \bigr|
\le \frac{C(M_6)}{n^{1/3}}+Ce^{-\frac14M_6^{3/2}}. 
\end{equation}


\bigskip
Now we consider case (iv), 
$1+\frac{M_7}{2^{1/3}{(n+1)}^{2/3}} \le 
\frac{2\sqrt{\lambda}}{n+1} \le 1+\delta_6$.
We write 
\begin{equation*}
     \log{\phi_n(\lambda)} 
     =\sum_{(1)} \log{\kappa^2_{k}} + \sum_{(2)} \log{\kappa^2_{k}},
\end{equation*}
where $(1),(2)$ indicate the following regions : 
\begin{align*}
  (1)\quad  &n+1\le k+1 \le 2\sqrt\lambda - \frac{M_7}{2^{1/3}}(n+1)^{1/3}\\ 
  (2)\quad  &2\sqrt\lambda - \frac{M_7}{2^{1/3}}(n+1)^{1/3}\leq k+1.
\end{align*}

\medskip
For $(1)$, we have for $n$ sufficiently large,  
$1+\frac{M_7}{2^{1/3}(k+1)^{2/3}} \leq \frac{2\sqrt\lambda}{k+1} \leq 1+\delta_6$.
Therefore, using~\eqref{e-z37}, we obtain 
\begin{equation}\label{e-z41}
\begin{split}
  &\sum_{(1)} \log{\kappa^2_{k}(\lambda)}\\
  &\le \sum_{k+1=n+1}^{[2\sqrt\lambda -\frac{M_7}{2^{1/3}}(n+1)^{1/3}]}
        (k+1) \biggl( -\frac14(\frac{2\sqrt\lambda}{k+1}-1)^2\biggr) 
      +\frac{C^{\#}}{2\sqrt{\lambda}-(k+1)}\\
  &\leq -\frac14\int_{n+1}^{2\sqrt\lambda -\frac{M_7}{2^{1/3}}(n+1)^{1/3}}
       x\bigl(\frac{2\sqrt\lambda}{x}-1\bigr)^2 dx
       + \int_{n+1}^{2\sqrt\lambda -\frac{M_7}{2^{1/3}}(n+1)^{1/3}}
       \frac{C^{\#}}{2\sqrt{\lambda}-x}dx +C(M_7)\\
  &\leq -\frac14\int_{\frac{n+1}{2\sqrt\lambda}}
   ^{1-\frac{M_7}{2^{1/3}(n+1)^{2/3}}\frac{n+1}{2\sqrt\lambda}}
    (2\sqrt\lambda)^2 \frac{(1-y)^2}{y} dy
    + C^{\#}\log\biggl(\frac{2\sqrt{\lambda}-(n+1)}{(n+1)^{1/3}} \biggr)
    +C(M_7)\\
  &\leq -\frac14\int_{\frac{n+1}{2\sqrt\lambda}}
   ^{1-\frac{M_7}{2^{1/3}(n+1)^{2/3}}\frac{n+1}{2\sqrt\lambda}}
    (2\sqrt\lambda)^2 (1-y)^2 dy
    + C^{\#}\frac{2\sqrt{\lambda}-(n+1)}{(n+1)^{1/3}} 
    +C(M_7)\\
  &\leq \frac14\int_{1-\frac{n+1}{2\sqrt\lambda}}
   ^{\frac{M_7}{2^{1/3}(n+1)^{2/3}}\frac{n+1}{2\sqrt\lambda}}
    (2\sqrt\lambda)^2 z^2 dz
    + C^{\#}(n+1)^{2/3}(\frac{2\sqrt\lambda}{n+1}-1)
    +C(M_7)\\
  &\leq \frac1{12}(2\sqrt\lambda)^2
    \biggl[( \frac{M_7}{2^{1/3}(n+1)^{2/3}}\frac{n+1}{2\sqrt\lambda})^3
    - (1-\frac{n+1}{2\sqrt\lambda})^3 \biggr]\\
  & \qquad + C^{\#}(n+1)^{2/3}(\frac{2\sqrt\lambda}{n+1}-1)
    +C(M_7)\\
  &\leq \frac{M_7^3}{24}(\frac{n+1}{2\sqrt\lambda}) 
    -\frac{n+1}{24\sqrt\lambda}(n+1)^2(\frac{2\sqrt\lambda}{n+1}-1)^3 
    + C^{\#}(n+1)^{2/3}(\frac{2\sqrt\lambda}{n+1}-1)
    +C(M_7)\\
  &\leq - \frac1{48}\biggl[2^{1/3}(n+1)^{2/3}
    (\frac{2\sqrt\lambda}{n+1}-1)\biggr]^3 
    + C^{\#}(n+1)^{2/3}(\frac{2\sqrt\lambda}{n+1}-1)
    +C(M_7)\\
  &\le - \frac1{96}\biggl[2^{1/3}(n+1)^{2/3}
    (\frac{2\sqrt\lambda}{n+1}-1)\biggr]^3 +C(M_7).
\end{split}
\end{equation}
The first line follows from the inequality 
$ -\gamma + \log \gamma +1 \leq -\frac{(\gamma-1)^2}{4}$ 
for $1\le \gamma \le 2$ ( note from~\eqref{e-z37} that $C^{\#}$ is independent of 
$M_7$).
In the second line, we use the monotonicity of 
$x(\frac{2\sqrt{\lambda}}{x}-1)^2$ and of $(2\sqrt{\lambda}-x)^{-1}$ 
in the region $n+1\le x\le 2\sqrt{\lambda}-\frac{M_7}{2^{1/3}}(n+1)^{1/3}$.
In the succeeding lines, we have used the changes of variables 
$x=2\sqrt{\lambda} y$, $1-y=z$ and $2\sqrt{\lambda} z^{3/2}=s$.
For the last line, note that $2^{1/3}(n+1)^{2/3}(\frac{2\sqrt\lambda}{n+1}-1)
\geq M_7$, and we require 
\begin{equation}\label{e-z39}
    M_7\geq \sqrt{96C^{\#}}.
\end{equation}

\textbf{Remark} : In estimating the sum in the second line of~\eqref{e-z41} 
by an integral, the monotonicity of the integrand plays a crucial role : 
we cannot, for example, use an estimate of the form~\eqref{e-z40}, as 
the derivative is not sufficiently small.


For $(2)$, we have 
$\frac{2\sqrt{\lambda}}{k+1} \le 1+\frac{2M_7}{2^{1/3}{(k+1)}^{2/3}}$.
Calculations similar to 
the previous cases (i), (ii) and (iii) show that 
\begin{equation*}
   \sum_{(2)} \log{\kappa^2_{k}(\lambda)} 
   \le  \bigl| \int_{-2M_7}^{\infty} 2im^{PII}_{1,22}(y) dy \bigr|
+ \frac{C(M_7)}{n^{1/3}}+Ce^{-M_7} \le C(M_7).
\end{equation*}
The result follows by splitting the sum $\sum_{(2)}$ into the following 
regions $2\sqrt{\lambda}-\frac{M_7}{2^{1/3}}(n+1)^{1/3}\le k+1 \le
2\sqrt{\lambda}+\frac{M_7}{2^{1/3}}(n+1)^{1/3}$, 
$2\sqrt{\lambda}+\frac{M_7}{2^{1/3}}(n+1)^{1/3} < k+1 <3\sqrt{\lambda}$ and 
$3\sqrt{\lambda} \le k+1$  : we leave the detail to the reader.

Therefore, for $1+\frac{M_7}{2^{1/3}{(n+1)}^{2/3}} \le 
\frac{2\sqrt{\lambda}}{n+1}
\le 1+\delta_6$, we have 
\begin{equation}
   \log \phi_n(\lambda) \le - \frac1{96}\biggl[2^{1/3}(n+1)^{2/3}
    (\frac{2\sqrt\lambda}{n+1}-1)\biggr]^3 + C(M_7) 
\end{equation}

\bigskip
For case (v), we use the estimation of \cite{Johan} given in the 
Lemma~\ref{lem-phi} (v) below.

\bigskip
Summarizing, we have
\begin{lem}\label{lem-phi}
  Let $0<\delta_5,\delta_6,\delta_7<1$ and $M_5,M_6,M_7>0$ be fixed number.
  Suppose that $\delta_6, M_5, M_6$ and $M_7$ satisfy conditions 
(a),(b),(c) and (d) given at the beginning of this Section, respectively.
  Set 
\begin{equation}\label{e-z42}
    t=2^{1/3}(n+1)^{2/3}\bigl(1-\frac{2\sqrt{\lambda}}{n+1}\bigr)
\quad\text{so that}\quad 
\frac{2\sqrt{\lambda}}{n+1}=1-\frac{t}{2^{1/3}(n+1)^{2/3}}.
\end{equation}
  We have the following estimates for the large $n$ 
behavior of $\phi_n(\lambda)$ : 
  \begin{enumerate}
    \item If $0\le \frac{2\sqrt{\lambda}}{n+1} \le 1-\delta_5$,  
\begin{equation*}
  \bigl| \log{\phi_n(\lambda)} \bigr| \le C\exp(-cn), 
\end{equation*}
for some constants $C,c$ which may depend on $\delta_5$.
    \item If $\frac12 \le \frac{2\sqrt{\lambda}}{n+1} 
\le 1-\frac{M_5}{2^{1/3}{(n+1)}^{2/3}}$ ,
\begin{equation*}
  \bigl| \log{\phi_n(\lambda)} \bigr| \le C\exp(-ct^{3/2}),
\end{equation*}
for constants C,c independent of $M_5$.
    \item If $1-\frac{M_6}{2^{1/3}{(n+1)}^{2/3}} \le 
\frac{2\sqrt{\lambda}}{n+1} \le 1+\frac{M_6}{2^{1/3}{(n+1)}^{2/3}}$, 
so that $-M_6\le t\le M_6$, 
there is a constant $C(M_6)$ which depends on $M_6$, 
and a constant $C$ which is independent of $M_6$,  
such that 
\begin{equation*}
  \bigl| \log{\phi_n(\lambda)} - \int_{t}^{\infty} 2im^{PII}_{1,22}(y) dy \bigr|
\le \frac{C(M_6)}{n^{1/3}}+Ce^{-\frac14M_6^{3/2}}.
\end{equation*}
    \item If $1+\frac{M_7}{2^{1/3}{(n+1)}^{2/3}} \le \frac{2\sqrt{\lambda}}{n+1}
\le 1+\delta_6$, 
\begin{equation*}
      \log \phi_n(\lambda) \le \frac1{96}t^3 + C(M_7),
\end{equation*}
for a constant $C(M_7)$.
   \item \cite{Johan} If $1+\delta_7 \le \frac{2\sqrt{\lambda}}{n+1}$,
\begin{equation*}
   \phi_n(\lambda)\le Ce^{-C\lambda} \le Ce^{-cn^2}.
\end{equation*}
  \end{enumerate}
\end{lem}
The really new results in this Lemma are (iii) and (iv).
Indeed, (i) and (ii) can also be obtained from~\eqref{e-J1.13'}, 
and as indicated, (v) is given in \cite{Johan}.





\bigskip
