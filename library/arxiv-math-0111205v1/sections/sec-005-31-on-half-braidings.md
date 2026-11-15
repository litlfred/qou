---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-005-31-on-half-braidings
section_title: "On half braidings"
section_number: 3.1
pages: 8-9
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.912
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
We begin with the definition of the quantum double $\2Z_1(\2C)$ of a (strict) monoidal
category $\2C$. 
\bdefin Let $\2C$ be a strict monoidal category and let $X\in\2C$. A half braiding
$e_X$ for $X$ is a family $\{e_X(Y)\in\Hom_\2C(XY,YX),\ Y\in\2C\}$ of morphisms satisfying 
\begin{itemize}
\item[(i)] Naturality w.r.t.\ the argument in brackets, i.e.
\begin{equation}t\otimes\id_X\mcirc e_X (Y)= e_X(Z)\mcirc\id_X
  \otimes t \quad\forall t: Y\rarr Z.
\label{hb-i}\end{equation}
\item[(ii)] The braid relation
\begin{equation} e_X(Y\otimes Z)=\id_{Y}\otimes e_X(Z) \mcirc
    e_X(Y)\otimes\id_{Z} \quad \forall Y,Z\in\2C. \label{hb-ii}\end{equation}
\item[(iii)] All $e_X(Z)$ are isomorphisms.
\item[(iv)] Unit property:
\begin{equation} e_X(\11)=\id_X. \label{hb-iv}\end{equation}
\end{itemize}
\label{hb}\edefin

\blemma \label{iii-iv}
Let $\{ e_X(Y), Y\in\2C \}$ satisfy (i) and (ii). Then (iii)$\impl$(iv). If (iv) holds 
and $Y$ has a right dual $Y^*$ then $e_X(Y)$ is invertible.
\elemma
\prf Considering (\ref{hb-ii}) with $Y=Z=\11$ gives $e_X(\11)=e_X(\11)^2$. Thus (iii)
implies $e_X(\11)=\id_X$. Let $Y^*$ a right dual of $Y$ with
$\ve_Y:\11\rarr Y^*\otimes Y, \eta_Y: Y\otimes Y^*\rarr\11$. Then using (i) and (iv) we
find
\[
\begin{tangle}
\coev\mobj{\eta_Y}\Step\xx\mobj{e_X(Y)}\\
\id\Step\xx\step[-.3]\mobj{e_X(Y^*)}\step[2.3]\id\\
\id\Step\id\Step\ev\step[-.5]\mobj{\ve_Y}\\
\object{Y}\Step\object{X}
\end{tangle}
\quad=\quad
\begin{tangle}
\coev\Step\id\step[1.5]\id\\
\hh\id\Step\id\mobj{Y^*}\Step\id\step\frabox{e_X(\11)}\\
\id\Step\ev\step[1.5]\id\\
\object{Y}\step[5.5]\object{X}
\end{tangle}
\quad=\quad
\begin{tangle}
\id\Step\id\\
\id\Step\id\\
\object{Y}\Step\object{X}
\end{tangle}
\]
Thus $e_X(Y)$ has a right inverse, which by a similar computation is seen to be also a
left inverse.
\qed

For later use we record the following alternative characterization of half braidings.
\blemma \label{halfbr}
Let $\2C$ be semisimple and $\{X_i, i\in \Gamma\}$ a basis of simple objects. Let $Z\in\2C$.
Then there is a one-to-one correspondence between (i) families of morphisms 
$\{ e_Z(X_i)\in\Hom_\2C(Z X_i,X_iZ),\ i\in \Gamma\}$ such that
\begin{multline} t \otimes\id_Z \mcirc  e_Z(X_k)=\id_{X_i}\otimes e_Z(X_j)
   \mcirc e_Z(X_i)\otimes\id_{X_j}\mcirc\id_Z\otimes t \\
   \forall i,j,k\in \Gamma,\ t\in\Hom_\2C(X_k,X_iX_j), 
\label{hb-v}\end{multline}  
and (ii) families of morphisms $\{ e_Z(X)\in\Hom_\2C(Z X,XZ),\ X\in\2C\}$ satisfying 1.\
and 2.\ from Definition \ref{hb}. All $e_Z(X), X\in\2C$ are isomorphisms iff all $e_Z(X_i),
i\in \Gamma$ are isomorphisms. 
\label{l17}\elemma
\prf (ii)$\impl$(i). Obvious: just restrict $e_Z(\cdot)$ to 
$X\in\{X_i, i\in \Gamma\}$. Then (\ref{hb-i}, \ref{hb-ii}) imply (\ref{hb-v}).\\
(i)$\impl$(ii). Let $X\cong\bigoplus_i n_i X_i$ and let
$\{ x_i^\alpha, \alpha=1,\ldots, n_i\}$, $\{ {x'_i}^\alpha, \alpha=1,\ldots, n_i\}$ be 
dual bases in $\Hom_\2C(X_i,X)$ and $\Hom_\2C(X, X_i)$, respectively. Then define
\[  e_Z(X)=\sum_{i\in \Gamma}\sum_{\alpha=1}^{n_i} x_i^\alpha\otimes\id_Z
   \mcirc e_Z(X_i)\mcirc\id_Z\otimes {x'}_i^\alpha. \]
Independence of  $e_Z(X)\in\Hom_\2C(Z X,XZ)$ of the choice of the $x_i^\alpha$ follows
from duality of the bases $\{x_i^\alpha\}, \{{x'_i}^\alpha\}$. In order to prove
naturality (\ref{hb-ii}) consider $Y\cong\bigoplus_i m_i X_i$ and corresponding
intertwiners $y_i^\alpha, {y'_i}^\alpha$ and let $t\in \Hom_\2C(X,Y)$. Then 
${y'_j}^\beta tx_i^\alpha\in\Hom(X_i,X_j)$, which vanishes if $i\ne j$. Thus 
\[ t=\sum_{i\in \Gamma}\sum_{\alpha=1}^{n_i}\sum_{\beta=1}^{m_i}
   c(i,\alpha,\beta) y_i^{\beta} {x'}_i^\alpha, \]
where $c(i,\alpha,\beta)\in\7F$. Therefore,
\[ t\otimes\id_Z\mcirc e_Z(X)=  \sum_{i\in \Gamma}\sum_{\alpha=1}^{n_i}\sum_{\beta=1}^{m_i}
  c(i,\alpha,\beta) \ y_i^{\beta}\otimes\id_Z\mcirc e_Z(X_i)\mcirc\id_Z \otimes
  {x'}_i^\alpha, \] 
which coincides with $e_Z(Y)\mcirc\id_Z\otimes t$.
If now $t\in\Hom_\2C(X_k, X_iX_j)$ then naturality implies
$t\otimes\id_Z\circ e_Z(X_k)= e_Z(X_iX_j)\mcirc\id_Z\otimes t$.
Together with (\ref{hb-v}) this implies 
\[  e_Z(X_iX_j)\mcirc\id_Z\otimes t=\id_{X_i}\otimes e_Z
  (X_j)\mcirc e_Z(X_i)\otimes\id_{X_j}\mcirc\id_Z\otimes t, \]
and since this holds for all $t\in\Hom_\2C(X_k,X_iX_j)$ (\ref{hb-ii}) follows.
(This is a consequence of
\[ \sum_{k\in \Gamma}\sum_{\alpha=1}^{N_{ij}^k} t_k^\alpha\circ {t'}_k^\alpha=
  \id_{X_iX_j}, \]
where the $\{t_k^\alpha, \alpha=1,\ldots,N_{ij}^k\}$ are  bases in 
$\Hom_\2C(X_k,X_iX_j)$.) \qed
