---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-001-2-riemann-hilbert-theory
section_title: "Riemann-Hilbert Theory"
section_number: 2
pages: 8-13
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
---
\label{s-PII}

In this section, we first summarize some basic facts about RHP's in general,   
and then discuss the RHP for the PII equation in some detail.
Basic references for RHP's are \cite{CG}, \cite{GK}, and 
the material on PII is taken from \cite{DZ}.

\medskip
Let $\Sigma$ be an oriented curve in the plane (see, 
for example, Figure~\ref{fig-rh1}).
\begin{figure}[ht]
 \centerline{\epsfig{file=rh1.eps, width=6cm}}
 \caption{}\label{fig-rh1}
\end{figure}
By convention, the $(+)$-side (resp., $(-)$-side) of an arc in $\Sigma$ 
lies to the left (resp., right) as one traverses the arc in the direction 
of the orientation.
Thus, corresponding to Figure~\ref{fig-rh1}, we have Figure~\ref{fig-rh2}.
\begin{figure}[ht]
 \centerline{\epsfig{file=rh2.eps, width=6cm}}
 \caption{}\label{fig-rh2}
\end{figure}
Let $\Sigma_0=\Sigma-\{\text{points of self-intersection}\}$ and $v$ 
be a smooth map from $\Sigma_0\to Gl(n,\C)$, for some $n$.
If $\Sigma$ is unbounded, we require that $v(z)\to I$ as $z\to\infty$ 
along $\Sigma$.
The RHP $(\Sigma,v)$ consists of the following (see, e.g., \cite{CG}) : 
establish the existence and uniqueness of an $n\times n$ matrix valued 
function $Y(z)$ (the \emph{solution} of the RHP $(\Sigma,v)$) 
such that 
\begin{equation}\label{e-tec1}
  \begin{cases}
     Y(z) \qquad\text{is analytic $\C-\Sigma$,}\\
     Y_+(z)=Y_-(z)v(z) \quad z\in\Sigma_0,\\
     Y(z)\to I \qquad\text{as $z\to\infty$.}
  \end{cases}
\end{equation}
Here $Y_{\pm}(z)=\lim_{z'\to z}Y(z')$ where 
$z'\in (\pm)-\text{side of $\Sigma$}$.
The precise sense in which these boundary values are attained, and also 
the precise sense in which $Y(z)\to I$ as $z\to\infty$, are 
technical matters 
that should be specified for any given RHP $(\Sigma,v)$. 
In \emph{this} paper, by a solution $Y$ of a RHP $(\Sigma,v)$, we always mean 
that 
\begin{equation}\label{e-tec2}
  \begin{split}
   &\text{$Y(z)$ is analytic in $\C-\Sigma$ and continuous up to the 
boundary}\\
&\text{(including the points in $\Sigma-\Sigma_0$) in each component.}\\ 
&\text{The jump relation $Y_+(z)=Y_-(z)v(z)$ is taken in the sense of}\\
&\text{continuous boundary values, and $Y(z)\to I$ as $z\to\infty$ means}\\
&\text{$Y(z)=I+O\bigl( \frac1{|z|} \bigr)$ uniformly as 
$z\to\infty$ in $\C-\Sigma$.}
  \end{split}
\end{equation}
Given $(\Sigma,v)$, the existence of $Y$ under appropriate 
technical assumptions on $\Sigma$ and $v$, is in general 
a subtle and difficult question.
However, for the RHP~\eqref{e-Y}, and hence for all RHP's obtained by 
deforming~\eqref{e-Y} (see, e.g.,~\eqref{e-m1orig}), we will prove the 
existence of $Y$ directly by construction (see, Lemma~\ref{lem-exi}) : 
uniqueness, as we will see, is a simple matter.

The solution of a RHP $(\Sigma, v)$ can be expressed in terms of 
the solution of an associated singular integral equation on $\Sigma$ 
(see,~\eqref{e-sam4},~\eqref{e-tec4} below) as follows.
Let $C_\pm$ be the Cauchy operators
\begin{equation}\label{e-sam3}
   (C_\pm f)(z)=\lim_{z'\to z_\pm} \int_{\Sigma}
\frac{f(s)}{s-z'} \frac{ds}{2\pi i}, \quad z\in\Sigma,
\end{equation}
where $z'\to z_\pm$ denotes the non-tangential limit from the $\pm$ side
of $\Sigma$ respectively.
A useful reference for Cauchy operators on curves which may have points of 
self-intersection is \cite{GK}.
Under mild assumptions on $\Sigma$, which will always be satisfied 
for the curves that arise in this paper, the non-tangential limits 
in~\eqref{e-sam3} will exist pointwise a.e.~on $\Sigma$.
Furthermore, if $f\in L^p(\Sigma,|dz|)$, $1<p<\infty$, then 
the boundary values (appropriately interpreted at the points 
$\Sigma-\Sigma_0$ of self-intersection) 
of $\int_{\Sigma} \frac{f(s)}{s-z} \frac{ds}{2\pi i}$ 
are also taken in the sense of $L^p$ and 
$\|C_\pm f\|_{L^p(\Sigma,|dz|)} \le c_p\|f\|_{L^p(\Sigma,|dz|)}$.
A simple calculation shows that  
\begin{equation}\label{e-tec5}
  C_+-C_-=1.
\end{equation}

Let 
\begin{equation}\label{e-sam2}
    v=b^{-1}_-b_+ \equiv (I-w_-)^{-1}(I+w_+)
\end{equation}
be any factorization of $v$.
We assume $b_\pm$, and hence $w_\pm$, are smooth on $\Sigma_0$, and 
if $\Sigma$ is unbounded, we assume $b_\pm(z)\to I$ as $z\to\infty$ 
along $\Sigma$.
Define the operator
\begin{equation}\label{e-tec3}
   C_w(f)\equiv C_+(fw_-)+C_-(fw_+).  
\end{equation}
By the above discussion, if $w_\pm\in L^{\infty}(\Sigma,|dz|)$, then 
$C_w$ is bounded from $L^2(\Sigma,|dz|)\to L^2(\Sigma,|dz|)$.
Suppose that the equation 
\begin{equation}\label{e-sam4}
   (1-C_w)\mu=I \quad\text{on $\Sigma$}
\end{equation}
has a solution $\mu\in I+L^2(\Sigma)$,
Or more precisely, suppose $\mu-I\in L^2(\Sigma)$ solves 
\begin{equation}\label{e-tec4}
   (1-C_w)(\mu-I)=C_wI=C_+(w_-)+C_-(w_+),
\end{equation}
which is a well-defined 
equation in $L^2(\Sigma)$ provided that 
$w_\pm\in L^\infty\cap L^2(\Sigma,|dz|)$.
Then the solution of the RHP~\eqref{e-tec1} is given by 
(see, \cite{CG},\cite{BC}) 
\begin{equation}\label{e-sam5}
   Y(z)=I+\int_{\Sigma} \frac{\mu(s)(w_+(s)+w_-(s))}{s-z}
\frac{ds}{2\pi i}, \quad z\notin\Sigma.
\end{equation}
Indeed for a.e. $z\in\Sigma$, from~\eqref{e-sam4} and~\eqref{e-tec5}, 
\begin{equation*}
  \begin{split}
     Y_+(z)&=I+C_+(\mu(s)(w_+(s)+w_-(s)))\\
     &=I+C_w(\mu) + (C_+-C_-)(\mu w_+)\\
     &=\mu+\mu w_+\\
     &=\mu(z)b_+(z),
  \end{split}
\end{equation*}
and similarly $Y_-(z)=\mu(z)b_-(z)$, so that $Y_+(z)=Y_-(z)b_-^{-1}(z)b_+(z)
=Y_-(z)v(z)$ a.e. on $\Sigma$.
Under the appropriate regularity assumptions on $\Sigma$ and $v$, 
one then shows that $Y(z)$ solves the RHP $(\Sigma, v)$ 
in the sense of~\eqref{e-tec2}.

As indicated, the above approach to the RHP goes through for any 
factorization $v=(I-w_-)^{-1}(I+w_+)$. 
Different factorization may be used at different points in the 
analysis of any given problem (see e.g. \cite{DZ1}).
However, in this paper we will \emph{always} take $w_-=0$, so that 
$v=(I+w_+)$.
Thus $C_w$ always denotes the operator $C_-\bigl(\cdot(v-I) \bigr)$.

In this paper we will not develop the general theory for the solution 
of RHP's, giving conditions under which~\eqref{e-sam4} has a (unique) 
solution, etc. 
Rather, for the convenience of the reader who may not be familiar with 
Riemann-Hilbert theory, we will use the above calculations 
and computations as a guide, 
and verify all the steps directly as they arise.







\bigskip
We now consider the RHP for the PII equation 
(\cite{FN}, \cite{JMU} : see also \cite{IN}, \cite{FZ}, \cite{DZ}).
We will consider two equivalent versions of the RHP for PII.
These two RHP's  
will be used in the later sections for the construction of parametrices 
for the solution of~\eqref{e-Y}.

Let $\Sigma^{PII}$ denote the oriented contour consisting of 6 rays 
in Figure~\ref{fig-PII}.
Thus $\Sigma^{PII}=\cup_{k=1}^{6}\{ \Sigma^{PII}_{k}=e^{i(k-1)\pi/3} \R_+ \}$,
with associated jump matrix $v^{PII} : \Sigma^{PII} \to M_2(\C)$, 
where the monodromy data $p,q$ and $r$ are 
complex numbers satisfying the relation
\begin{equation}\label{e-mon}
  p+q+r+pqr=0.
\end{equation}
\begin{figure}[ht]
 \centerline{\epsfig{file=PII.eps, width=8cm}}
 \caption{$v^{PII}$ and $\Sigma^{PII}$}\label{fig-PII}
\end{figure}
For $x\in\R$ and $z\in\Sigma^{PII}-\{0\}$, set
\begin{equation}
  \begin{split}
     v_x^{PII}(z)&=e^{-i\theta_{PII}\sigma_3}v^{PII}
e^{i\theta_{PII}\sigma_3}\\
     &\equiv e^{-i\theta_{PII}ad\sigma_3}v^{PII}, 
  \end{split}
\end{equation}
where
\begin{equation}
    \theta_{PII}\equiv \frac{4z^3}3+xz.
\end{equation}
The contour $\Sigma^{PII}$ consists precisely of the set $Re(i4z^3/3)=0$.
This implies, in particular, that $v_x^{PII}(z)-I \notin L^2(\Sigma^{PII})$.
For example, as $z\to +\infty$ along the real axis, 
$v_x^{PII}(z)-I$ is oscillatory 
(on the other rays, $\Sigma^{PII}_{k}$, $k=1,2,4,5$, $v_x^{PII}(z)-I$ 
could grow), and so we cannot expect that the RHP 
$(\Sigma^{PII},v_x^{PII})$ has a solution in the sense of~\eqref{e-tec2}.
However, if we rotate $\Sigma^{PII}$ in the clockwise direction by any  
angle $\theta_0$, $0<\theta_0<\pi/3$, $\Sigma^{PII}\to 
\Sigma^{PII}_{\theta_0}\equiv e^{-i\theta_0}\Sigma^{PII}$, then it is 
easy to see that $v_x^{PII}(z)-I\in 
L^2\cap L^{\infty}(\Sigma^{PII}_{\theta_0})$, 
and we may expect that the RHP $(\Sigma^{PII}_{\theta_0},v_x^{PII})$ 
has a solution in the sense of~\eqref{e-tec2}.
Moreover, as $v_x^{PII}(z)$ is analytic, it is clear that if one can 
solve $(\Sigma^{PII}_{\theta_0},v_x^{PII})$ for some $0<\theta_0<\pi/3$, 
then one can solve $(\Sigma^{PII}_{\wt{\theta}_0},v_x^{PII})$ 
for any other $0<\wt{\theta}_0<\pi/3$, and the solution of the 
$\wt{\theta}_0$-problem can be obtained from the $\theta_0$-problem 
by an analytic continuation, and vice versa.
So suppose that for some fixed $0<\theta_0<\pi/3$, and for 
$x\in\R$,  
$m_{\theta_0}^{PII}(z;x)$ is a ($2\times 2$ matrix) solution of the RHP 
$(\Sigma_{\theta_0}^{PII}, v_x^{PII})$, 
\begin{equation}\label{e-mPII}
  \begin{cases}
     m^{PII}_{\theta_0}(z) \qquad  
\text{analytic in} \qquad   \C -\Sigma_{\theta_0}^{PII},\\
     \bigl(m_{\theta_0}^{PII}\bigr)_+(z)=
\bigl(m_{\theta_0}^{PII}\bigr)_-(z) v_x^{PII}(z) , 
\qquad 0\neq z\in \Sigma_{\theta_0}^{PII},\\
     m^{PII}_{\theta_0}(z)\to I \qquad \text{as} \qquad z\to\infty, 
  \end{cases}
\end{equation}
in the sense of~\eqref{e-tec2}.
Let $m_1^{PII}(x)$ denote the residue at $\infty$ of 
$m_{\theta_0}^{PII}(z)$, given by
\begin{equation*}
   m_{\theta_0}^{PII}(z;x)=I+\frac{m_1^{PII}(x)}{z}+O(\frac1{z^2})
\end{equation*}
as $z\to\infty$.
Then 
\begin{equation}\label{e-z4}
   u(x)\equiv 2im_{1,12}^{PII}(x)=-2im_{1,21}^{PII}(x)
\end{equation}
solves PII (see \cite{FN}, \cite{JMU}), 
\begin{equation*}
   u_{xx}=2u^3+xu,\qquad x\in\R,
\end{equation*}
where $m_{1,12}^{PII}(x)$ (resp., $m_{1,21}^{PII}(x)$) denotes 
the $(12)$-entry (resp, $(21)$-entry) of $m_1^{PII}(x)$.
It is easy to see that $m_1^{PII}(x)$, and hence $u(x)$ in~\eqref{e-z4}, 
is independent of the choice of $\theta_0\in (0,\pi/3)$ 

A solution of the RHP $(\Sigma_{\theta_0}^{PII}, v_x^{PII})$ 
for some $\theta_0$, hence for all $\theta_0\in (0,\pi/3)$, may not exist 
for all $p,q,r$ satisfying~\eqref{e-mon} and $x\in\R$.
A sufficient condition (see \cite{FZ})  
for the RHP to have a unique solution (in the sense of~\eqref{e-tec2}) 
for all $x\in\R$, is that
\begin{equation*}
   |q-\bar{p}|<2 \qquad \text{and} \qquad r\in\R.  
\end{equation*}
In this paper, we need the singular case 
\begin{equation}
   p=-q=1 \qquad \text{and} \qquad r=0.
\end{equation}
\begin{figure}[ht]
 \centerline{\epsfig{file=PII1.eps, width=8cm}}
 \caption{$p=-q=1,r=0$ case ; $\Sigma_{\theta_0}^{PII,1}$ and 
$v^{PII,1}$}\label{fig-PII1}
\end{figure}
The latter condition $r=0$ implies that 
there is no jump across the rays $\pm e^{i(2\pi/3-\theta_0)}$, 
and we may replace $\Sigma^{PII}_{\theta_0}$ by $\Sigma^{PII,1}_{\theta_0}$ 
as in Figure~\ref{fig-PII1} (note that the orientations across the rays 
$e^{-i\theta_0}, e^{i(2\pi/3-\theta_0)}$ have been reversed). 
As noted in \cite{DZ}, a unique solution in the sense of~\eqref{e-tec2} 
still exists in this singular case 
for all $x\in\R$ : a proof of this fact is not given in \cite{DZ}, 
but can be found in [DKMVZ3 ; nonregular case, Case II]. 
In addition, the solution has the property that 
\begin{equation}\label{e-unif}
  \begin{split}
   &m_{\theta_0}^{PII,1}(z;x) \ \ \text{and its inverse are uniformly bounded}\\
&\text{for}\ \  (z,x)\in(\C-\Sigma_{\theta_0}^{PII,1})\times[-M,M],
  \end{split}
\end{equation}
for any fixed $M>0$.
As $m^{PII,1}_{\theta_0}(z;x)$ solves~\eqref{e-mPII} 
in the sense of~\eqref{e-tec2}, we see 
in particular that~\eqref{e-unif} holds up to the boundary in each sector.

The asymptotics of $u(x)=2im_{1,12}^{PII,1}(x)$  
given in~\eqref{e-asyPII}, is computed in ~\cite{DZ} via the above RHP and 
from the proof in \cite{DZ}, one learns that 
\begin{equation}\label{e-aympm_1}
  \begin{split}
   &m^{PII,1}_{1,22}(x)=O\biggl(\frac{e^{-(4/3)x^{3/2}}}{x^{1/4}}\biggr) 
\quad \text{as} \quad x\to\infty,\\
   &m^{PII,1}_{1,22}(x)\sim \frac{i}8 x^2 \quad \text{as} \quad x\to -\infty,
  \end{split}
\end{equation}
where $m^{PII,1}_{1,22}$ denotes the $(22)$-entry of $m^{PII}_{1}$.
Also, using the methods in \cite{DZ}, for example, 
one obtains the relation
\begin{equation}\label{e-um1PII}
   \frac{d}{dx} 2im^{PII,1}_{1,22}(x) = u^2(x).
\end{equation}
and verifies directly that $2im^{PII,1}_{1,22}(x)$ is real-valued.

\bigskip
\begin{figure}[ht]
 \centerline{\epsfig{file=PII2.eps, width=8cm}}
 \caption{$\Sigma^{PII,2}$ and $v^{PII,2}$}\label{fig-PII2}
\end{figure}
For the first of the two equivalent RHP's advertised above, 
we consider Figure~\ref{fig-PII2}, which consists of 
the real axis (the dotted line), $\Sigma^{PII,1}_{\theta_0}$ for some 
fixed, small $\theta_0>0$ (the dashed lines), and a contour 
$\Sigma^{PII,2}$ consisting of a pair of curved solid lines. 
The contour $\Sigma^{PII,2}$ is of the general shape indicated 
in the Figure, with one component in $\C_+$ and one component in $\C_-$, 
and we require that $\Sigma^{PII,2}$ is asymptotic to straight lines 
lying \emph{strictly} within 
the region $\{ |arg z|<\pi/3 \}\cup\{ 2\pi/3 <arg z< 4\pi/3 \}$.
Together with the line $\{xe^{-i\theta_0} : x\in\R \}$, 
these contours divide 
the complex plane into 4 open regions, 
$\Omega^{PII,2}_k$, $k=1,2,3,4$, as shown in Figure ~\ref{fig-PII2}.
Let $v^{PII,2}$ be the jump matrix on $\Sigma^{PII,2}$ which is given by 
$\bigl(\begin{smallmatrix} 1&0\\1&1 \end{smallmatrix}\bigr)$ in $\C_+$ 
and by $\bigl(\begin{smallmatrix} 1&-1\\0&1 \end{smallmatrix}\bigr)$ in $\C_-$.
We define
\begin{equation*}
  \begin{cases}
    m^{PII,2}=m_{\theta_0}^{PII,1}e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&0\\1&1 \end{smallmatrix} \bigr)^{-1}
\quad\text{in}\quad{\Omega^{PII,2}_1\cap\Omega^{PII,1}_2},\\
    m^{PII,2}=m_{\theta_0}^{PII,1}e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&0\\1&1 \end{smallmatrix} \bigr)
\qquad\text{in}\quad{\Omega^{PII,2}_2\cap\Omega^{PII,1}_1},\\
    m^{PII,2}=m_{\theta_0}^{PII,1}e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&-1\\0&1 \end{smallmatrix} \bigr)^{-1}
\quad\text{in}\quad{\Omega^{PII,2}_3\cap\Omega^{PII,1}_4},\\
    m^{PII,2}=m_{\theta_0}^{PII,1}e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&-1\\0&1 \end{smallmatrix} \bigr)
\qquad\text{in}\quad{\Omega^{PII,2}_4\cap\Omega^{PII,1}_3},\\
    m^{PII,2}=m_{\theta_0}^{PII,1}\quad\text{otherwise},
  \end{cases}
\end{equation*}
where the regions $\Omega^{PII,1}_{k}$,$k=1,2,3,4$ are defined  
in Figure ~\ref{fig-PII1}.
A straightforward calculation with the jump relations for 
$m_{\theta_0}^{PII,1}$, 
shows that 
$m^{PII,2}$ solves the new RHP
\begin{equation}\label{e-RHPm2}
  \begin{cases}
    m^{PII,2}\quad\text{is analytic in}\quad\C-\Sigma^{PII,2},\\
    m^{PII,2}_+=m^{PII,2}_-v^{PII,2}_x\quad\text{on}
\quad\Sigma^{PII,2},\\
    m^{PII,2}\to I\quad\text{as}\quad z\to\infty,
  \end{cases}
\end{equation}
where $v^{PII,2}_{x}=e^{-i(\theta_{PII})ad\sigma_3}v^{PII,2}$ 
and $v^{PII,2}$ is given in Figure~\ref{fig-PII2}.
This deformed RHP is clearly equivalent to the original RHP 
for $m_{\theta_0}^{PII,1}$
in the sense that a solution of the one RHP yields a solution 
of the other RHP, and vice versa.
Also we have 
\begin{equation}\label{e-RHPm2'}
   (m_{\theta_0}^{PII,1})_1=m_1^{PII,2},
\end{equation}
for the residues of $m_{\theta_0}^{PII,1}$ (resp, $m^{PII,2}$) at $\infty$.
From~\eqref{e-unif}, 
we see that for any fixed $M>0$, 
\begin{equation}\label{e-unif2}
 \begin{split}
   &m^{PII,2}(z;x) \quad\text{and its inverse are uniformly bounded}\\
   &\text{for}\quad  (z,x)\in(\C-\Sigma^{PII,2})\times[-M,M].
 \end{split}
\end{equation}
A particular choice of contour $\Sigma^{PII}$ will be made in 
Section~\ref{s-K1} (see below).

\bigskip
\begin{figure}[ht]
 \centerline{\epsfig{file=PII3.eps, width=8cm}}
 \caption{$\Sigma^{PII,3}$}\label{fig-PII3}
\end{figure}
The second of the equivalent RHP's is restricted to the case $x<0$, 
and we consider 
Figure~\ref{fig-PII3}, which consists of the real axis (the dotted line), 
$\Sigma^{PII,1}_{\theta_0}$ for some fixed small $\theta_0>0$ 
(the dashed lines) and a contour $\Sigma^{PII,3}=
\cup_{k=1}^{5}\Sigma^{PII,3}_{k}$ consisting of 5 straight lines, one 
finite and four infinite.
The regions $\Omega^{PII,3}_k$, $1\le k\le 4$, are the components 
of $\C-\Sigma^{PII,3}$.

The infinite lines make an angle strictly between $0$ and $\pi/3$ 
with the real axis.
Set 
\begin{equation}\label{e-z5}
   g^{PII}(z)=\frac43 \bigl(z^2+\frac{x}2 \bigr)^{3/2}
\end{equation}
which is defined to be analytic in $\C-[-\sqrt{\frac{-x}2}, 
\sqrt{\frac{-x}2}]$, and behaves like 
$\frac43 z^3+xz+\frac{x^2}{8z}+O(\frac1{z^3}) = \theta_{PII}(z)+O(\frac1{z})$ 
as $z\to\infty$.
Therefore for any $M>0$, 
\begin{equation}\label{e-z6}
    e^{i(g^{PII}(z)-\theta_{PII}(z))} \quad \text{is bounded for}
\quad (z,x)\in (\C-[-\sqrt{\frac{-x}2},\sqrt{\frac{-x}2}]) \times [-M,0]
\end{equation}
and
\begin{equation}\label{e-z7}
    e^{i(g^{PII}(z)-\theta_{PII}(z))} \to 1 \quad \text{as $z\to\infty$ 
uniformly for $-M\le x\le 0.$}
\end{equation}
We define $m^{PII,3}$ by 
\begin{equation*}
  \begin{cases}
    m_{\theta_0}^{PII,1}[e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&0\\1&1 \end{smallmatrix} \bigr)^{-1}]
e^{i(g^{PII}(z)-\theta_{PII}(z))\sigma_3}
\quad\text{in}\quad 
\Omega^{PII,3}_1\cap(\Omega^{PII,1}_2\cup\Omega^{PII,1}_3),\\
    m_{\theta_0}^{PII,1}[e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&0\\1&1 \end{smallmatrix} \bigr)]
e^{i(g^{PII}(z)-\theta_{PII}(z))\sigma_3}
\qquad\text{in}\quad{\Omega^{PII,3}_3\cap\Omega^{PII,1}_1},\\
    m_{\theta_0}^{PII,1}[e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&-1\\0&1 \end{smallmatrix} \bigr)^{-1}]
e^{i(g^{PII}(z)-\theta_{PII}(z))\sigma_3}
\quad\text{in}\quad{\Omega^{PII,3}_2\cap\Omega^{PII,1}_4},\\
    m_{\theta_0}^{PII,1}[e^{-i(\theta_{PII})ad\sigma_3}
\bigl(\begin{smallmatrix} 1&-1\\0&1 \end{smallmatrix} \bigr)]
e^{i(g^{PII}(z)-\theta_{PII}(z))\sigma_3}
\qquad\text{in}\quad
\Omega^{PII,3}_4\cap(\Omega^{PII,1}_2\cup\Omega^{PII,1}_3),\\
    m_{\theta_0}^{PII,1}\quad\text{otherwise}.
  \end{cases}
\end{equation*}
Then from the jump relations for $m_{\theta_0}^{PII,1}$,  
we see that $m^{PII,3}$ solves the new RHP 
$(\Sigma^{PII,3}, v_{x}^{PII,3})$ in the sense of~\eqref{e-tec2}, 
\begin{equation}\label{e-z17}
  \begin{cases}
    m^{PII,3}\quad\text{is analytic in}\quad\C-\Sigma^{PII,3},\\
    m^{PII,3}_+=m^{PII,3}_-v^{PII,3}_x\quad\text{on}
\quad\Sigma^{PII,3},\\
    m^{PII,3}\to I\quad\text{as}\quad z\to\infty,
  \end{cases}
\end{equation}
where $v^{PII,3}_{x}$ is given by 
\begin{equation}\label{e-vPII4}
  \begin{cases}
     \begin{pmatrix}1&0\\e^{2ig^{PII}}&1 \end{pmatrix}
\qquad\text{on}\quad \Sigma_1^{PII,3},\Sigma_2^{PII,3}\\
     \begin{pmatrix}1&-e^{-2ig^{PII}}\\0&1 \end{pmatrix}
\quad\text{on}\quad \Sigma_3^{PII,3},\Sigma_4^{PII,3}\\
     \begin{pmatrix}e^{-2ig_{-}^{PII}}&-1\\1&0 \end{pmatrix}
\quad\text{on}\quad \Sigma_5^{PII,3}.\\
  \end{cases}
\end{equation}
Also we have
\begin{equation}\label{e-mPmP4}
   m_1^{PII}=m_1^{PII,3}-\bigl( \frac{ix^2}{8} \bigr)\sigma_3,
\end{equation}
for the respective residues of $m_{\theta_0}^{PII,1}$ and $m^{PII,3}$ 
at $\infty$. 
Finally, from~\eqref{e-unif} and~\eqref{e-z6}, 
we see that, for any fixed $M\in\R$
\begin{equation}\label{e-unif4}
  \begin{split}
   &m^{PII,3}(z;x) \quad\text{and its inverse are uniformly bounded}\\
&\text{for}\quad  (z,x)\in(\C-\Sigma^{PII,3})\times[-M,0].
  \end{split}
\end{equation}
