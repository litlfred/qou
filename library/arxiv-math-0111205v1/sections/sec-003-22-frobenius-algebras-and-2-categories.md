---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-003-22-frobenius-algebras-and-2-categories
section_title: "Frobenius algebras and 2-categories"
section_number: 2.2
pages: 6-8
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.972
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\bdefin \label{d-Frob}
Let $\2A$ be a (strict) monoidal category. A Frobenius algebra in $\2A$ is a
quintuple $\5Q=(Q,v,v',w,w')$, where $Q$ is an object in $\2A$ and 
$v:\11\rightarrow Q, v': Q\rightarrow\11, w: Q\rightarrow Q^2, w':Q^2\rightarrow Q$ 
are morphisms satisfying the following conditions:
\begin{equation} \label{W1}
   w\otimes\id_Q\mcirc w=\id_Q\otimes w\mcirc w, 
\end{equation}
\begin{equation} \label{W1'}
   w' \mcirc w'\otimes\id_Q=w' \mcirc \id_Q\otimes w', 
\end{equation}
\begin{equation} \label{W2}
   v'\otimes\id_Q\mcirc w = \id_Q = \id_Q\otimes v'\mcirc w,
\end{equation}
\begin{equation} \label{W2'}
   w' \mcirc v\otimes\id_Q = \id_Q = w' \mcirc \id_Q\otimes v,
\end{equation}
\begin{equation} \label{W3}
   w'\otimes\id_Q \mcirc \id_Q\otimes w = w\mcirc w' = \id_Q\otimes w'\mcirc w\otimes \id_Q. 
\end{equation} 
A Frobenius algebra $\5Q$ in a $\7F$-linear category is canonical if
\bea w'\circ w &=& \lambda_1 \id_Q, \label{W4} \\
   v'\mcirc v &=& \lambda_2 \id_\11\label{W5}\eea
with $\lambda_1,\lambda_2\in\7F^*$. $\5Q$ is normalized if $\lambda_1=\lambda_2$.
\edefin

Let $X$ be an object in a spherical category $\2A$. Then the quintuple
\[ (X\ol{X},\ \ve(X),\ \ol{\ve}(X),\ \id_X\otimes\ve(\ol{X})\otimes\id_{\ol{X}},\ 
   \id_X\otimes\ol{\ve}(\ol{X})\otimes\id_{\ol{X}}) \]
is easily seen to be a normalized canonical Frobenius algebra in $\2A$. The following
theorem, which combines the Theorems 3.12 and 5.13 from \cite{mue09}, shows that in fact
every canonical Frobenius algebra in a tensor category arises in this way, provided one is
ready to embed the category as a corner into a bicategory.

\btheor \label{Main}
Let $\2A$ be a strict $\7F$-linear tensor category and $\5Q=(Q,v,v',w,w')$ a canonical
Frobenius algebra in $\2A$. Then:
\begin{itemize}
\item[(i)] There is a bicategory $\2E$ such that
\begin{enumerate}
\item The sets of 2-morphisms in $\2E$ are finite dimensional $\7F$-vector spaces and the
horizontal and vertical compositions are bilinear.
\item Idempotent 2-morphisms in $\2E$ split. 
\item $\displaystyle \obj\,\2E=\{\6A,\6B\}$.
\item There is an equivalence
$\displaystyle\HOM_\2E(\6A,\6A)\stackrel{\otimes}{\simeq}\ol{\2A}^p$ of tensor categories,
thus an equivalence
$\displaystyle\HOM_\2E(\6A,\6A)\stackrel{\otimes}{\simeq}\2A$ if $\2A$ has subobjects.
\item There are 1-morphisms $J: \6B\rarr \6A$ and $\oj : \6A\rarr \6B$ such that
$Q=J\oj $.  
\item $J$ and $\oj $ are mutual two-sided duals, i.e.\ there are 2-morphisms
\[ e_J: \11_\6A\rarr J\oj,\ \ \ve_J: \11_\6B\rarr\oj J,\ \ d_J: \oj J\rarr\11_\6B,\ \ 
   \eta_J: J\oj\rarr\11_\6A \]
satisfying the usual equations.
\item We have
\bean v &=& e_J:\ \11_\6A\rarr Q=J\oj , \\
   v' &=& \eta_J:\ Q=J\oj \rarr\11_\6A, \\
   w &=& \id_J\otimes\ve_J\otimes\id_{\oj }:\ Q=J\oj \rarr J\oj J\oj =Q^2, \\
   w' &=& \id_J\otimes d_J\otimes\id_{\oj }:\ Q^2=J\oj J\oj \rarr J\oj =Q
\eean
and therefore $d_J\circ\ve_J=\lambda_1\id_{\11_\6B}$, $\eta_J\circ e_J=\lambda_2\id_{\11_\6A}$.
\item $\2E$ is uniquely determined up to equivalence by the above properties. Isomorphic
Frobenius algebras $\5Q, \tilde{\5Q}$ give rise to isomorphic bicategories 
$\2E, \tilde{\2E}$. 
\end{enumerate}
\item[(ii)] If $\2A$ has direct sums then $\2E$ has direct sums of 1-morphisms.
\item[(iii)] If the multiplicity of $\11$ in $Q$ is exactly one (it is at least one due to
the existence of $v,v'$) then $J, \oj, \11_\6B$ are simple. (There is a weaker condition
implying only simplicity of $\11_\6B$.)
\item[(iv)] If $\7F=\7C$ and $\2A$ has a positive $*$-operation then $\2E$ has a positive
$*$-operation and is semisimple.
\item[(v)] If $\2A$ is strict spherical and $\5Q$ satisfies (iii) and is normalized 
then $\2E$ is spherical. If, furthermore, $\2A$ is semisimple and $\7F$ is algebraically
closed then $\2E$ is semisimple. 
\item[(vi)] If (iv) or (v) apply then the tensor category $\2B=\HOM_\2E(\6B,\6B)$
satisfies $\dim\2B=\dim\2A$. 
\end{itemize}
\etheor

\brem 1. If two tensor categories $\2A, \2B$ are `corners' of a 2-category as above we
call them weakly monoidally Morita equivalent. This is an equivalence relation which is
considerably weaker than the usual equivalence, yet it implies that $\2A$ and $\2B$ have
the same dimension and define the same triangulation invariant \cite{bw1, gk} for
3-manifolds. See \cite{mue09} for the details. 

2. Unfortunately, the above statement of the theorem will not be sufficient for our
purposes since beginning in Subsection \ref{fff} we will make use of the concrete structure
of the bicategory $\2E$, which is explicitly constructed in the proof of Theorem
\ref{Main}. This is not the place to explain the latter which occupies the larger part of 
\cite{mue09}. We can only hope that the above statement of the theorem and its r\^{o}le in
this paper are sufficient to motivate the reader to acquire some familiarity with
\cite{mue09}. 
\erem
