---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-030-511-sphericity-of-pivotalization
section_title: "Sphericity of pivotalization"
section_number: 5.11
pages: 22-24
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.949
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
In this Section we allow the ground field to have a positive
characteristic, different from $2$.

Let $A$ be a quasitriangular weak Hopf algebra, i.e., such that
$\Rep(A)$ is a braided monoidal category. Let $\R\in (A\otimes A)\Delta(1)$ 
be the $R$-matrix of $A$.
It was shown in \cite{NTV} that the Drinfeld element $u = S(\R\II)\R\I$ is invertible,
satisfies  $S^2(h)=uhu^{-1}$ for all $h$ in $A$, and
\begin{equation}
\label{delta u}
\Delta(u^{-1}) = \R_{21}\R (u^{-1}\otimes u^{-1}).
\end{equation}
Furthermore, the element $uS(u)^{-1}$ is group-like and implements $S^4$ via the
adjoint action.

Observe that for any group-like element $\eta\in G(A^*)$ the element  
$g_\eta  = \R\I\la \eta,\, \R\II\ra$ is group-like in $A$ and the map
$\eta\mapsto g_\eta$ is a group homomorphism from $G(A^*)$ to $G(A^{op})$.

Recall that distingusihed elments of $A$ and $A^*$ were defined in 
Section~\ref{subsection about integrals}. In the next Lemma we extend
a result of Radford \cite{R2} relating the distinguished elements and $uS(u)^{-1}$. 

\begin{lemma}
\label{uS(u)-1 vs a}
Let $a\in A$ and $\alpha\in A^*$ be a pair of distinguished group-like elements
chosen as in Section~\ref{subsection about integrals}. Then $g_\alpha a = S(u)u^{-1}$.
\end{lemma}

\begin{proof}
Let $\ell\in A$ be a non-degenerate integral from which $a$ and $\alpha$ are constructed.
It follows from \cite[Section 5]{N} that 
\begin{eqnarray*}
\ell\2 \otimes \ell\1 &=& \ell\1 \otimes S^2(\ell\2)a^{-1}\\
\ell\1 h \otimes \ell\2 &=& \ell\1 \otimes \ell\2 S(h\actr \alpha),\qquad h\in A.
\end{eqnarray*}
Using these identities and properties of integrals and $R$-matrices we compute
\begin{eqnarray*}
\ell\2 S(\R\II \actr\alpha) \R\I \otimes \ell\1 
&=&  \ell\2  \R\I \otimes \ell\1 \R\II \\
&=&  \R\I \ell\1 \otimes \R\II \ell\2 \\
&=& \R\I  S(\R\II) \ell\1 \otimes \ell\2 \\
&=& \R\I  S(\R\II)  S^2(\ell\2)a^{-1} \otimes \ell\1, 
\end{eqnarray*}
whence $S(\R\II \actr\alpha) \R\I = \R\I  S(\R\II) a^{-1} = S(u)a^{-1}$ 
by  non-degeneracy of $\ell$. On the other hand,
from the axioms of $R$-matrix we have  $S(\R\II \actr\alpha) \R\I= S(\R\II) \R\I g_\alpha
=  u g_\alpha$, which completes the proof. 
\end{proof}

Recall \cite[Section 7]{NTV} that a central $\nu\in A$ is a ribbon
element if $\nu=S(\nu)$ and $\Delta(\nu) =
\R_{21}\R (\nu\otimes \nu)$. A quasitriangular weak Hopf algebra $A$
has a ribbon element if and only if $\Rep(A)$ is a ribbon category.

\begin{corollary}
\label{ribonness}
Suppose that $A$ is a unimodular quasitriangular weak Hopf algebra and that
$\alpha$ is gauged to be $\epsilon$. If $g\in A$ is a group-like element such that
$g^2 = a^{-1}$ and $S^2(h)=ghg^{-1}$ for all $h\in A$ then $\nu = u^{-1}g$ is
a ribbon element of $A$.
\end{corollary}

\begin{proof}
In this case we have $g_\alpha= 1$.
Since both $u$ and $g$ implement $S^2$, the element $\nu$ is central.
It follows from Equation~\eqref{delta u}  that $\Delta(\nu) =
\R_{21}\R (\nu\otimes \nu)$. Finally, $S(\nu) = S(u)^{-1}g^{-1} = u^{-1}g = \nu$
by Lemma~\ref{uS(u)-1 vs a}.
\end{proof}


Recall that in Remark \ref{pivotalization},
it was shown that to every fusion category 
$\mC$ one can associate a twice bigger 
fusion category $\tilde\mC$, which has a canonical pivotal
structure. 

\begin{proposition}\label{sphpiv} If $\dim\mC\ne 0$ then 
the canonical pivotal stucture of the category $\tilde \mC$  
is in fact a spherical structure. 
\end{proposition}

\begin{proof}
Let us realize $\tilde\mC$ as the representation category of a
regular weak Hopf algebra $A$. In this case, 
the pivotal structure of $\tilde\mC$ is defined 
by a grouplike element $g\in A$, such that $g^2=a^{-1}$, 
where $a$ is the distinguished group-like element of $A$.
Assume that the distinguished group-like element $\alpha\in
A^*$ is gauged to be $\epsilon$.
Consider the Drinfeld center $Z(\tilde \mC)$, i.e., the
representation category of the Drinfeld double $D(A)$. 

One can check that $a$ is also the distinguished 
grouplike element for $D(A)$.
Since $g$ is a grouplike element such that $gxg^{-1}=S^2(x)$
for $x\in D(A)$, and $g^2=a^{-1}$, it follows from 
Corollary~\ref{ribonness} that $D(A)$ is ribbon, hence,
$Z(\tilde\mC)$ is ribbon.

Thus, we have $\dim(V)=\dim(V^*)$ in $Z(\tilde\mC)$ \cite{K}. 
Hence, the same holds in $\tilde \mC$
(i.e., $\tilde \mC$ is spherical). 
Indeed, let $I: \tilde \mC\to Z(\tilde \mC)$ be the
induction functor defined in subsection \ref{indfu}. 
Then by Proposition \ref{I(1)}, for any $V\in \tilde\mC$, 
$I(V)=\oplus_{X\in Irr(\tilde\mC)} X\otimes
V\otimes X^*$ as an object of $\tilde\mC$. 
Hence, $\dim I(V)=\dim V\dim \tilde \mC$. On the other hand,
$I(V)^*=I(V^*)$, which implies the statement. 
\end{proof}

\begin{corollary}\label{posroot} In any pivotal fusion category $\mC$
over $\CC$, the dimension of a simple object
is a positive number times a root of unity. 
\end{corollary} 

\begin{proof} 
Consider the category $\tilde\mC$. It has two pivotal structures
$b_1,b_2: V\to V^{**}$. Namely, $b_1$ comes from 
$\mC$ and $b_2$ is the canonical pivotal structure. 
By Proposition \ref{sphpiv}, $b_2$ is spherical. 
On the other hand, $b_2^{-1}\circ b_1$ is a tensor 
endomorphism of the identity functor, 
which obviously acts by roots of unity on simple objects. 
This implies the statement. 
\end{proof}



\begin{section}{The co-Hochschild complex of a cosemisimple 
unimodular weak Hopf algebra and its subcomplex of invariants}
