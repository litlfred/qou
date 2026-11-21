---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-005-32-review-on-the-character-varieties-of-twobridg
section_title: "Review on the character varieties of two–bridge knots"
section_number: 3.2
pages: 5-5
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
\label{ReviewCharK}
Here we briefly review Riley's method~\cite{Riley} for describing the non--abelian part of the representation space of two--bridge knot groups.

The knot group of a two--bridge knot $K$ admits a presentation of the following form:
\begin{equation}\label{P:G2B} 
\Pi(K)=\left\langle {x,y \, | \, \Omega x=y \Omega} \right\rangle  \text{ where } \Omega=x^{\epsilon_1}y^{\epsilon_n}x^{\epsilon_2}y^{\epsilon_{n-1}}\dotsb x^{\epsilon_n}y^{\epsilon_1}, \; \epsilon_i = \pm 1.
\end{equation}
  
  We consider the following matrices: 

$C_1=
  \begin{pmatrix}
    \sqrt{s}&1\\
    0&{1}/{\sqrt{s}}
  \end{pmatrix},\ 
D_1=
  \begin{pmatrix}
   \hphantom{-}\sqrt{s}&0\\
   -u&{1}/{\sqrt{s}}
  \end{pmatrix};
$
and 
$
C_2=
  \begin{pmatrix}
    \sqrt{s}&{1}/{\sqrt{s}}\\
    0&{1}/{\sqrt{s}}
  \end{pmatrix},\ 
D_2=
  \begin{pmatrix}
    \hphantom{-t}\sqrt{s}&0\\
    -\sqrt{s}u&{1}/{\sqrt{s}}
  \end{pmatrix};
$
where $s \in \CC^*$, $\sqrt{s}$ is some square root, and $u \in \CC$.
\begin{remark}\label{remCD}
Note that $C_2$ and $D_2$ are respectively conjugate to $C_1$ and $D_1$ via $U=\bigl(
   \begin{smallmatrix}
     s^{-1/4}&0\\
     0&s^{1/4}
   \end{smallmatrix}
\bigr)$.
\end{remark}





 
 
 
 



 




 

For a two--bridge knot $K$, 
$x$ and $y$ are conjugate elements in $\Pi(K)$ and represent meridians of the knot,
 therefore $\rho(x)$ and $\rho(y)$ have same traces. 
If $\rho(x)$ and $\rho(y)$ do not commute, i.e. if $\rho$ is non--abelian, 
then up to a conjugation 
one can assume that $\rho(x)$ and $\rho(y)$ are the matrices $C_1$ and $D_1$ 
respectively. With this notation, we have the following result due to Riley~\cite{Riley}.










\begin{proposition} 
The homomorphism $\rho \colon \Pi(K) \to \mathrm{SL}_2(\CC)$ 
defined by $\rho(x)=C_1$ and $\rho(y)=D_1$ 
is a non--abelian representation of $\Pi(K)$ 
if and only if the pair $(s,u) \in \CC^2$ satisfies the following equation: 
\begin{equation}\label{eq:R}
  w_{1, 1}+({1}/{\sqrt{s}}-\sqrt{s})w_{1, 2}=0
\end{equation}
where $W=\rho(\Omega)$. 

Conversely, every non--abelian representation is conjugated to a representation satisfying Eq.~(\ref{eq:R}).
\end{proposition}

\begin{remark}
Similarly, if $\rho(x)=C_2$ and $\rho(y)=D_2$, then Riley's equation is 
\begin{equation}\label{eq:R_alternative}
w_{1, 1}+(1-s)w_{1, 2}=0.
\end{equation}
\end{remark}

\begin{notation}
We let $\phi_K(s, u) = w_{1, 1}+(1-s)w_{1, 2}$ denote the left hand side of
Eq. $(\ref{eq:R_alternative})$ 
and call it the \emph{Riley polynomial} of $K$.
\end{notation}
