---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-010-24-the-slash-operator-and-proof-of-theorem-12
section_title: "The slash operator and proof of Theorem 1.2"
section_number: 2.4
pages: 17-20
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.961
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.slash}

In this section we recall the slash operator, an important ingredient to
express modularity. We will use the usual conventions for the modular
$q=\e(\tau)$ and the Jacobi $t=\e(z)$, $\lambda_{i}=\e(u_{i})$, $\mu_{i}=\e(v_{i})$,
$x=\e(w)$ variables, i.e., $\ti q=\e(-1/\tau)$, $\ti t=\e(z/\tau)$ and
$\e(x)=e^{2\pi i x}$.
Now recall the slash operator $f|_\kappa \gamma$ (see, eg.~\cite[p.13]{123}
and~\cite{EZ}) for $\gamma=\sma abcd \in\SL_{2}(\BZ)$ acting on a function
$f(z,\tau)$ by 
\be
\label{fslash}
(f|_\kappa \gamma)(z,\tau) = (c \tau+d)^{-\kappa} f(\gamma(z,\tau)),
\qquad \gamma(z,\tau) = \left(\frac{z}{c\tau+d},\frac{a\tau+b}{c\tau+d}\right) \,.

\ee
This action can be extended to a matrix-valued
function $F(z,\tau)$ of weight $\kappa=\diag(\kappa_1,\dots,\kappa_r)$ by 
\be
\label{Fslash}
  (F|_\kappa\gamma)(z,\tau)
  =
  F(\gamma(z,\tau))
 \diag((c \tau+d)^{-\kappa}) \,.
 \ee
 This extension satisfies
 \be
 \label{slashprops}
 \begin{aligned}
   (F|_\kappa\gamma)|_\kappa\gamma' &= F|_\kappa\gamma\gamma' \\
   (F G)|_\kappa\gamma &= (F|_\kappa\gamma) \Delta_\gamma
   (G|_\kappa\gamma) 
 \end{aligned}
 \ee
 for matrix-valued functions $F$ and $G$ and for $\gamma, \gamma' \in \SL_2(\BZ)$
 where $\Delta_\gamma(\tau)=\diag((c \tau+d)^{\kappa})$. We can extend these
 definitions to include half integral weight using a multiplier system as
 done for the Dedekind $\eta$-function. In all our examples the relative weights
 $\kappa_{i}-\kappa_{j}$ are integers and the absolute weights are either always
 integers, or always half-integers. Our choice of absolute weight depends on the
 normalisation of our solutions, and multiplying them by $\eta$-functions leads to
 a shift of the absolute weights by half-integers, but has no effect on the modularity
 of the linear $q$-difference equation. 

Recall the cocycle $\Om_{U,\gamma}$ from Equation~\eqref{Om}, and the corresponding
cocycle $\Om_{V,\gamma}$. If the monodromy matrix $M=V^{-1}U$ satisfies Equation
~\eqref{Mmod}, it follows that the cocycle matrices associated to $U$ and $V$
are equal:
\be
\label{WU=WV}
\begin{aligned}
  \Om_{U,\gamma} &=  (V\vM|_{\kappa_U}\gamma)(V\vM)^{-1}
  = (V|_{\kappa_{V}}\gamma) \Delta_{\kappa_V,\gamma}(\vM|_{\kappa_U}\gamma)(V\vM)^{-1}
  \\ &= (V|_{\kappa_V}\gamma)
  \Delta_{\kappa_V,\gamma}(\vM|_{\kappa_U}\gamma)\vM^{-1}V^{-1}
  = (V|_{\kappa_V}\gamma)V^{-1} = \Om_{V,\gamma} \,.
\end{aligned}
\ee

We remark that sometimes the monodromy matrix of the fundamental bases $U$
and $V$ that come from the algorithm of Section~\ref{sub.algorithm}
satisfies Equation~\eqref{Mmod} on a finite index subgroup of $\SL_2(\BZ)$
(this happens, e.g., in Theorem~\ref{thm.41}) which contains a conjugate
of a congruence subgroup of $\SL_2(\BZ)$. In this case, an averaging of
the monodromy leads to fundamental solutions whose cocycle extends for all
$\gamma \in \SL_2(\BZ)$.

In the rest of this subsection, we give a proof of Theorem~\ref{thm.ST}

\begin{proof}[Proof of Theorem~\ref{thm.ST}]
  Using the behaviour of the slash operator on the product of two
  matrices~\eqref{slashprops}, it is easy to see that if Equation~\eqref{Mmod}
  holds for two elements of $\SL_2(\BZ)$, it also holds for their product. Since
  $S$ and $T$ generate $\SL_2(\BZ)$, part (a) follows.

  Part (b) follows from the presentation of $\SL_2(\BZ)$ given by
  \be
  \label{SL2Z}
  \SL_2(\BZ) = \langle S,T \,\, | \,\, S^4=I, TSTST=S \rangle
  \ee
  and from the cocycle property, which implies that
  if $\gamma=T^{a_0} S T^{a_1} S T^{a_2} \dots S T^{a_r} S T^{a_{r+1}}$, then
  \be
  \label{OmST}
  \Om_\gamma(z,\tau) = \prod_{j=1}^r
  \Om_S( (T^{a_j} S T^{a_{j+1}} \dots T^{a_r} S T^{a_{r+1}})(z,\tau))\,.
  \ee

  The idea for part (c) is to use reduction theory, with attention paid
  to the domain of extension. Fix a cocycle $\Om$ that satisfies $\Om_T=I$ and
  $\Om_S$ extends as a meromorphic function to $\BC\times\BC'$. Below, when
  we say that $\Om_\gamma$ extends, we will mean that it extends to
  $\BC \times \BC_\gamma$. We will give the proof in several steps.

  \noindent {\bf Step 1.}
  The cocycle property implies that
  \be
  \Om_{\gamma^{-1}}(z,\tau) = \left(\Om_\gamma(\gamma^{-1}(z,\tau))\right)^{-1}\,.
  \ee
  This, together with the fact that $\gamma^{-1}(\tau)-\gamma^{-1}(\infty)=
  1/(c(-c\tau+a))$ imply that $\Om_\gamma$ extends if and only if $\Om_{\gamma^{-1}}$
  extends. In particular, applying it to $\gamma=S$, where $\gamma^{-1}=-S$, we
  obtain that
  \be
  \label{Om-S}
  \Om_{-S}(z,\tau) = (\Om_S(-z/\tau,-1/\tau))^{-1} \,.
  \ee
  Using our assumptions on $\Om_S$, it follows that $\Om_{-S}$ extends. 

  \noindent {\bf Step 2.}
  Suppose now that $\gamma=\sma abcd \in \SL_2(\BZ)$ with $a>0$ and $c>0$.
  It follows by Gauss reduction theory that we can write
  \be
  \label{gammaST}
  \gamma = T^{a_0} S T^{a_1} S \dots T^{a_r} S T^{a_{r+1}}
  \ee
  for integers $a_i$ where $a_0 \geq 0$ and $a_1, \dots, a_r >0$. Moreover, 
  $a_0, \dots, a_r$ can be obtained from the negative continued fraction
  expansion (using nearest integers from above, rather than from below)
  \be
  \label{contfrac}
  \frac{a}{c} = [a_0,a_1,\dots,a_r]:= a_0 -1/(a_1 -1/(a_2 - \dots))\,.
  \ee
  The continued fraction expansion shows that the first column of $\gamma$
  agrees with that of the product $T^{a_0} S T^{a_1} S \dots T^{a_r} S$, and
  the last integer $a_{r+1}$ is chosen so that Equation~\eqref{gammaST} holds.
  Equation~\eqref{OmST} implies that $\Om_\gamma(z,\tau)$ is a product of $r$
  matrices $\Om_S$ matrices evaluated suitably, and $\Om_\gamma$ extends to
  real $\tau$ that satisfy $(T^{a_j} S T^{a_{j+1}} \dots T^{a_r} S T^{a_{r+1}})(\tau)>0$
  for all $j=1,\dots,r$. The key property is that the first
  column of the matrices $T^{a_j} S T^{a_{j+1}} \dots T^{a_r} S T^{a_{r+1}}$
  for $j=1,\dots,r$  consists of positive integers (with the possible exception
  of $j=r+1$ where the $(2,1)$ entry may be zero). It follows that the system
  of inequalities cascades, and becomes equivalent to the single inequality
  $\tau > -d/c$. It follows that $\Om_\gamma$ extends in the case when
  $\gamma=\sma +*+* \in \SL_2(\BZ)$. 

  The above argument is best explained by an example. Consider the matrix
  $\gamma=\sma {17}{29}{7}{12}$. We expand the rational number $17/7$ of its
  first column in negative continued fractions 
  $$
  \frac{17}{7} = [3,2,4] = 3-\frac{4}{7} = 3-\frac{1}{7/4} = 3-\frac{1}{2-1/4}
  $$
  and obtain that the matrix
  $T^3 S T^2 S T^4 S=\begin{pmatrix} 17 & -5 \\ 7 & -2 \end{pmatrix}$,

  which further adjusting it by multiplying it on the right by $T^2$, gives
  $$
  \gamma =
  \begin{pmatrix} 17 & -5 \\ 7 & -2 \end{pmatrix} T^2 =
  T^3 S T^2 S T^4 S T^2 \,.
  $$
  The cocycle property and the fact that 
  $$
  T^2 S T^4 S T^2=\begin{pmatrix}
    7 & 12 \\ 4 & 7 \end{pmatrix}, \qquad T^4 S T^2=\begin{pmatrix}
    4 & 7 \\ 1 & 2 \end{pmatrix}, \qquad T^2= \begin{pmatrix}
    1 & 2 \\ 0 & 1 \end{pmatrix}
  $$
  implies that
  \be
  \Om_\gamma(z,\tau) =
  \Om_S\left(\frac{z}{4\tau+7}, \frac{7\tau+12}{4\tau+7}\right)
  \Om_S\left(\frac{z}{\tau+2}, \frac{4\tau+7}{\tau+2}\right)
  \Om_S(z, \tau+2)\,.
  \ee
  The right hand side extends when $\tau$ is real that satisfies
  $$
  \frac{7\tau+12}{4\tau+7} >0, \qquad \frac{4\tau+7}{\tau+2} >0, \qquad
  \tau+2 >0
  $$
  which (when reading the inequalities from last to first and simplifying)
  is equivalent to the system $\tau+2>0, 4\tau+7>0, 7\tau+12>0$, which is
  equivalent to $\tau> -12/7=\gamma^{-1}(\infty)$.

  \noindent {\bf Step 3.}
  We will now use the element $\ve=\sma {-1}001 \in \GL_2(\BZ)$ of order
  2, and observe that $\ve \sma abcd \ve = \sma a{-b}{-c}d \in \SL_2(\BZ)$
  for all $\sma abcd \in \SL_2(\BZ)$. In particular, $\ve T \ve = T^{-1}$
  and $\ve S \ve = -S$. It follows that if $\gamma=\sma abcd \in \SL_2(\BZ)$
  with $a>0$ and $c>0$ is given by~\eqref{gammaST}, then
  \be
  \label{egammaST}
  \ve\gamma\ve = \begin{pmatrix} a & -b \\ -c & d \end{pmatrix}=
    T^{-a_0} (-S) T^{-a_1} (-S) \dots T^{-a_r} (-S) T^{-a_{r+1}} \,.
  \ee
  The cocycle property implies that
  \be
  \label{OmSTe}
  \Om_{\ve\gamma\ve}(z,\tau) = \prod_{j=1}^r
  \Om_{-S}( (T^{-a_j} (-S) T^{-a_{j+1}} \dots T^{-a_r} (-S) T^{-a_{r+1}})(z,\tau))
  \ee
  where $\Om_{-S}(z,\tau)$ extends for $\tau<0$ by Step 1. Thus
  $\Om_{\ve\gamma\ve}$ extends when the inequalities 
  $(T^{-a_j} (-S) T^{-a_{j+1}} \dots T^{-a_r} (-S) T^{-a_{r+1}})(\tau)<0$
  for $j=1,\dots,r$. The key point now is that these inequalities cascade to
  a single inequality, namely, $\tau < d/c=(\ve\gamma\ve)^{-1}(\infty)$.
  It follows that $\Om_\gamma$ extends when $\gamma = \sma +*{-}* \in \SL_2(\BZ)$.
  In our running example above $\gamma=\sma {17}{29}{7}{12}$, we have
  \be
  \begin{pmatrix} 17 & -20 \\ -7 & 12 \end{pmatrix} =
  \ve \gamma \ve = T^{-3} (-S) T^{-2} (-S) T^{-4} (-S) T^{-2}
  \ee
  and the cocycle property and the fact that 
  $$
  T^{-2} (-S) T^{-4} (-S) T^{-2}=\mat 7{-12}{-4}7, \qquad
 T^{-4} (-S) T^{-2}=\mat 4{-7}{-1}2, \quad
 T^{-2}=\mat 1{-2}{0}1
 $$
 implies that
  \be
  \Om_{\ve \gamma \ve} =
  \Om_{-S}\left(\frac{z}{-4\tau+7}, \frac{7\tau-12}{-4\tau+7}\right)
  \Om_{-S}\left(\frac{z}{-\tau+2}, \frac{4\tau-7}{-\tau+2}\right)
  \Om_{-S}(z, \tau-2) \,.
  \ee
  The right hand side extends when $\tau$ is real that satisfies
  $$
  \frac{7\tau-12}{-4\tau+7} <0, \qquad \frac{4\tau-7}{-\tau+2} <0, \qquad
  \tau-2 <0
$$
which is equivalent to the system $7\tau-12<0, 4\tau-7<0, \tau-2<0$ which
is equivalent to $\tau < 12/7=(\ve\gamma\ve)^{-1}(\infty)$.

  \noindent {\bf Step 4.}
  The cocycle property and the triviality of $\Om_T=I$ implies that 
$\Om_{T \gamma}=\Om_\gamma$. Since $T \sma abcd =\sma {a+c}{b+d}cd$, it follows
that $\Om_\gamma$ (and hence its extension) depends only on the bottom row
$(c,d)$ of $\gamma$. When $\gamma_{2,1} \neq 0$, the extension follows from
either Step 2 or Step 3, depending on the sign of $\gamma_{2,1}$.

This concludes the proof of the theorem.  
\end{proof}
