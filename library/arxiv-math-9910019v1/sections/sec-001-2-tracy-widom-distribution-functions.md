---
doc_id: arxiv-math-9910019v1
doc_title: "Symmetrized random permutations"
section_id: sec-001-2-tracy-widom-distribution-functions
section_title: "Tracy-Widom distribution functions"
section_number: 2
pages: 4-7
source_pdf: 9910019v1.pdf
source_sha256: 07dd7ab7068b1482
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.977
doc_brief: "Symmetrized random permutations — 8 sections: Front matter; Introduction; Tracy-Widom distribution functions"
---
\label{sec-dist}


Let $u(x)$ be the solution of the Painlev\'e II (PII) equation,
\begin{equation}\label{as10}
  u_{xx}=2u^3+xu,
\end{equation}
with the boundary condition
\begin{equation}\label{as11}
  u(x)\sim -Ai(x)\quad\text{as}\quad x\to +\infty,
\end{equation}
where $Ai$ is the Airy function.
The proof of the (global) existence and the uniqueness of the solution 
was first established in \cite{HM} : 
the asymptotics as $x\to -\infty$ are 
(see e.g. \cite{HM,DZ2}) 
\begin{eqnarray}
\label{as17}  u(x) &=&
-Ai(x) + O\biggl( \frac{e^{-(4/3)x^{3/2}}}{x^{1/4}}\biggr),
\qquad\text{as $x\to +\infty$,}\\
\label{as18}  u(x) &=&
-\sqrt{\frac{-x}{2}}\biggl( 1+O\bigl(\frac1{x^2}\bigr)\biggr),
\qquad\text{as $x\to -\infty$.}
\end{eqnarray}
Recall that $Ai(x)\sim \frac{e^{-(2/3)x^{3/2}}}{2\sqrt{\pi}x^{1/4}}$
as $x\to +\infty$.
Define
\begin{equation}\label{as12}
  v(x):= \int_{\infty}^{x} (u(s))^2 ds,
\end{equation}
so that $v'(x)= (u(x))^2$.


We introduce the Tracy-Widom distributions.

(Note that $q:=-u$, which Tracy and Widom used in their papers,
solves the same
differential equation with the boundary condition
$q(x)\sim +Ai(x)$ as $x\to\infty$.)

\begin{defn}[Tracy-Widom distribution functions]\label{def1}
Set
\begin{eqnarray}
\label{as46-1}   F(x) &:=& \exp\biggl(\frac12\int_x^{\infty} v(s)ds\biggr)
= \exp\biggl(-\frac12\int_x^{\infty} (s-x)(u(s))^2ds\biggr),\\
\label{as47-1}   E(x) &:=& \exp\biggl(\frac12\int_x^{\infty} u(s)ds\biggr),
\end{eqnarray}
and set
\begin{eqnarray}
   F_2(x) :=& F(x)^2 &=\exp\biggl(-\int_x^{\infty} (s-x)(u(s))^2ds\biggr),\\
   F_1(x) :=& F(x)E(x) &= \bigl(F_2(x)\bigr)^{1/2}
e^{\frac12\int_x^{\infty} u(s)ds} ,\\
   F_4(x) :=& F(x)\bigl[E(x)^{-1}+E(x)\bigr]/2
&= \bigl(F_2(x)\bigr)^{1/2}
\biggl[ e^{-\frac12\int_x^{\infty} u(s)ds} +
e^{\frac12\int_x^{\infty} u(s)ds} \biggr] /2 .
\end{eqnarray}
\end{defn}

In \cite{TW1} and \cite{TW2},
Tracy and Widom proved that under proper centering
and scaling, the distribution of the largest eigenvalue of
a random GUE/GOE/GSE matrix converges to $F_2(x)$ / $F_1(x)$ / $F_4(x)$
as the size of the matrix becomes large.
We note that from the asymptotics \eqref{as17} and \eqref{as18},
for some positive constant $c$,
\begin{eqnarray}
\label{as46}   F(x) &=& 1+ O\bigl( e^{-cx^{3/2}}\bigr)
\qquad \text{as $x\to+\infty$,}\\
\label{as47}   E(x) &=& 1+ O\bigl( e^{-cx^{3/2}}\bigr)
\qquad \text{as $x\to+\infty$,}\\
\label{as48}   F(x) &=& O\bigl( e^{-c|x|^{3}}\bigr)
\qquad\qquad \text{as $x\to-\infty$,}\\
\label{as49}   E(x) &=& O\bigl( e^{-c|x|^{3/2}}\bigr)
\quad\qquad \text{as $x\to-\infty$.}
\end{eqnarray}
Hence in particular, $\lim_{x\to+\infty} F_\beta(x) = 1$ and
$\lim_{x\to-\infty} F_\beta(x) = 0$, $\beta=1,2,4$.
Monotonicity of $F_\beta(x)$ follows from the fact that $F_\beta(x)$
is the limit of a sequence of distribution functions.
Therefore $F_\beta(x)$ is indeed a distribution function.











\bigskip
As indicated in Introduction, we need new classes of distribution 
functions to describe the phase transitions from 
$\chi_{\text{GSE}}$ to $\chi_{\text{GOE}}$ 
and from $\chi_{\text{GUE}}$ to $\chi_{\text{GOE}^2}$.
First we consider the Riemann-Hilbert problem (RHP) for the Painlev\'e II 
equation \cite{FN, JMU}.
Let $\Gamma$ be the real line  $\R$, oriented from $+\infty$ to $-\infty$.
Let $m(\cdot\thinspace;x)$ be the solution of the following RHP :
\begin{equation}\label{as20}
 \begin{cases}
    m(z;x) \qquad \text{is analytic in $z\in\C\setminus\Gamma$,}\\
    m_+(z;x)=m_-(z;x) \begin{pmatrix} 1& -e^{-2i(\frac43z^3+xz)}\\
e^{2i(\frac43z^3+xz)}& 0 \end{pmatrix} \quad \text{for $z\in\Gamma$,}\\
    m(z;x) = I+O\bigl(\frac1{z}\bigr) \qquad \text{as $z\to\infty$.}
 \end{cases}
\end{equation}
Here $m_+(z;x)$ (resp,. $m_-$) is the limit of $m(z';x)$ as $z'\to z$
from the left (resp., right) of the contour $\Gamma$ :
$m_\pm(z;x)=\lim_{\epsilon\downarrow 0}m(z\mp i\epsilon;x)$.
Relation \eqref{as20} corresponds to 
the RHP for the PII equation with the special monodromy data
$p=-q=1, r=0$ (see \cite{FN, JMU}, also \cite{FZ,DZ2}).
In particular if the solution is expanded at $z=\infty$,
\begin{equation}\label{as7.27}
   m(z;x) = I+ \frac{m_1(x)}{z} + O\bigl(\frac1{z^2}\bigr),
\qquad \text{as $z\to\infty$},
\end{equation}
we have
\begin{eqnarray}
\label{as22}   2i(m_1(x))_{12} = -2i(m_1(x))_{21} &=& u(x), \\
\label{as23}   2i(m_1(x))_{22} = -2i(m_1(x))_{11}&=& v(x),
\end{eqnarray}
where $u(x)$ and $v(x)$ are defined in \eqref{as10}-\eqref{as12}.
Therefore the Tracy-Widom distributions above are expressed in terms of
the residue at $\infty$ of the solution to the RHP \eqref{as20}. 
It is noteworthy that the new distributions below which interpolate the 
Tracy-Widom distributions require additional information 
of the solution of RHP.

\begin{defn}\label{def3}
  Let $m(z;x)$ be the solution of RHP \eqref{as20} and
denote by $m_{jk}(z;x)$ the $(jk)$-entry of $m(z;x)$.
For $w>0$, define
\begin{equation}\label{as61}
   F^\symmO(x;w) :=
F(x) \biggl\{\bigl[m_{22}(-iw;x)-m_{12}(-iw;x) \bigr]E(x)^{-1}
+ \bigl[m_{22}(-iw;x)+m_{12}(-iw;x)\bigr]E(x) \biggr\}/2,
\end{equation}
and for $w<0$, define
\begin{equation}\label{as62}
 \begin{split}
   F^\symmO(x;w) &:=
e^{\frac83w^3-2xw}F(x) \\
&\times \biggl\{\bigl[-m_{21}(-iw;x)+m_{11}(-iw;x) \bigr]E(x)^{-1}
- \bigl[m_{21}(-iw;x)+m_{11}(-iw;x)\bigr]E(x) \biggr\}/2.
 \end{split}
\end{equation}
Also define
\begin{eqnarray}
   F^\symmu(x;w) &:=& m_{22}(-iw;x)F_2(x),
\quad\qquad\qquad\qquad w>0,\\
   F^\symmu(x;w) &:=& -e^{\frac83w^3-2xw}m_{21}(-iw;x)F_2(x),
\qquad w<0.
\end{eqnarray}
\end{defn}

\medskip
First $F^\symmO(x;w)$ and $F^\symmu(x;w)$ are real 
from Lemma \ref{lem12} (i) below.
Note that $F^\symmO(x;w)$ and $F^\symmu(x;w)$ are continuous at $w=0$
since at $z=0$, the jump condition of the RHP \eqref{as20} implies
$(m_{12})_+(0;x)= -(m_{11})_-(0;x)$ and
$(m_{22})_+(0;x)= -(m_{21})_-(0;x)$.
In fact, $F^\symmO(x;w)$ and $F^\symmu(x;w)$ are entire
in $w\in\C$ from the RHP \eqref{as20}.

From \eqref{as46}-\eqref{as49} and \eqref{as94}-\eqref{as97} below,
we see that
\begin{equation}
  \lim_{x\to+\infty} F^\symmO(x;w), F^\symmu(x;w) =1, \qquad
\lim_{x\to-\infty} F^\symmO(x;w), F^\symmu(x;w) = 0
\end{equation}
for any fixed $w\in\R$.
Also Theorem \ref{thm3} below shows 
that $F^\symmO(x;w)$ and $F^\symmu(x;w)$
are limits of distribution functions, implying that
they are monotone in $x$.
Therefore, $F^\symmO(x;w)$ and $F^\symmu(x;w)$ are indeed
distribution functions for each $w\in\R$.







We close this section summarizing some properties of $m(-iw;x)$ in the 
following lemma. 
In particular the lemma implies
that $F^\symmO(x;w)$ interpolates between $F_4(x)$ and $F_1(x)$, 
and $F^\symmu(x;w)$ interpolates between $F_2(x)$ and $F_1(x)^2$ 
(see Corollary \ref{cor16}).

\begin{lem}\label{lem12}
  Let $\sigma_3=\bigl(\begin{smallmatrix} 1&0\\0&-1 \end{smallmatrix}
\bigr)$, $\sigma_1=\bigl(\begin{smallmatrix} 0&1\\1&0 \end{smallmatrix}
\bigr)$, and set $[a,b]=ab-ba$.
\begin{enumerate}
\item 
  For real $w$, $m(-iw;x)$ is real.
\item
For fixed $w\in\R$, we have
\begin{eqnarray}
\label{as94}  m(-iw;x) &=& \bigl( I+\bigl( e^{-cx^{3/2}} \bigr) \bigr)
\begin{pmatrix}
1 & -e^{\frac83w^3-2xw} \\ 0 & 1
\end{pmatrix}, \qquad  \text{$w>0$, $x\to+\infty$,}\\
\label{as95}  m(-iw;x) &=& \bigl( I+\bigl( e^{-cx^{3/2}} \bigr) \bigr)
\begin{pmatrix}
1 & 0 \\ -e^{-\frac83w^3+2xw} & 1
\end{pmatrix}, \qquad  \text{$w<0$, $x\to+\infty$,}\\
\label{as96}  m(-iw;x) &\sim& \frac1{\sqrt{2}} \biggl( \begin{smallmatrix}
1&-1\\ 1&1 \end{smallmatrix} \biggr)
e^{(-\frac43w^3+xw)\sigma_3}
e^{(\frac{\sqrt{2}}3(-x)^{3/2}+\sqrt{2}w^2(-x)^{1/2})\sigma_3},
\quad  \text{$w>0$, $x\to-\infty$,}\\
\label{as97}  m(-iw;x) &\sim& \frac1{\sqrt{2}} \biggl( \begin{smallmatrix}
1&1\\ -1&1 \end{smallmatrix} \biggr)
e^{(-\frac43w^3+xw)\sigma_3}
e^{(-\frac{\sqrt{2}}3(-x)^{3/2}-\sqrt{2}w^2(-x)^{1/2})\sigma_3},
\quad  \text{$w<0$, $x\to-\infty$.}
\end{eqnarray}
\item 
  For any $x$, we have
\begin{equation}\label{as98}
  \lim_{w\to 0^+} m(-iw;x) =
\lim_{w\to 0^-} \sigma_1 m(-iw;x)\sigma_1  = \begin{pmatrix}
\frac12\bigl(E(x)^2+E(x)^{-2}\bigr) & -E(x)^2 \\
\frac12\bigl(-E(x)^2+E(x)^{-2}\bigr) & E(x)^2
\end{pmatrix}.
\end{equation}
\item 
   For fixed $w\in\R\setminus\{0\}$,
$m(-iw;x)$ solves the differential equation
\begin{equation}\label{as62.5}
   \frac{d}{dx}m = w[m,\sigma_3]+ u(x)\sigma_1 m,
\end{equation}
where $u(x)$ is the solution of the PII equation \eqref{as10}, \eqref{as11}.
\end{enumerate}
\end{lem}

\begin{cor}\label{cor16}
   We have
\begin{eqnarray}
   F^\symmO(x;0) &=& F_1(x),\\
   \lim_{w\to\infty} F^\symmO(x;w) &=& F_4(x), \\
   \lim_{w\to-\infty} F^\symmO(x;w) &=& 0, \\
\label{as116}   F^\symmu(x;0) &=& F_1(x)^2, \\
   \lim_{w\to\infty} F^\symmu(x;w) &=& F_2(x), \\
   \lim_{w\to-\infty} F^\symmu(x;w) &=& 0.
\end{eqnarray}
\end{cor}

\begin{proof}
   The values at $w=0$ follow from \eqref{as98}.
For $w\to\pm\infty$, note that from the RHP \eqref{as20},
we have $\lim_{z\to\infty} m(z;x)= I$.
\end{proof}
