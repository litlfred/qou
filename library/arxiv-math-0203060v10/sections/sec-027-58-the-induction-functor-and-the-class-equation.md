---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-027-58-the-induction-functor-and-the-class-equation
section_title: "The induction functor and the class equation for fusion categories"
section_number: 5.8
pages: 21-22
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.917
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
\label{indfu}

In finite group theory, an important role is played 
by the ``class equation'' $\sum_{s}\frac{1}{|G_s|}=1$, where 
the summation is over conjugacy classes of a finite group $G$, and 
$G_s$ are the corresponding centralizers. There is a similar
formula for semisimple Hopf algebras (due to G.I.Kac and Y.Zhu,
see \cite{Ka}, \cite{Zhu}), 
which is also very useful. 
Here we will prove a class equation for any fusion category,
which generalizes the results of Kac and Zhu. 

Let $\mC$ be a fusion category. 
Let $I:\mC\to Z(\mC)$ be the induction functor, 
defined by the condition $\Hom_{Z(\mC)}(I(V),X)=\Hom_{\mC}(V,X)$,
$V\in \mC$, $X\in Z(\mC)$. 

Let $[X:Y]$ denote the multiplicity of a simple object $Y$ in an
object $X$. For $X\in Z(\mC)$, let $X|_\mC$ denote the
corresponding object of $\mC$. 
Then $I(V)=\oplus_{X\in Irr(Z(\mC))}[X|_{\mC}:V]X$. 

\begin{proposition}\label{I(1)}
One has $I(V)|_\mC=\oplus_{Y\in
  Irr(\mC)}Y\otimes V\otimes Y^*$. 
\end{proposition}

\begin{example} If $G$ is a finite group and $\mC=\Rep(G)$, 
then $I(\mathbf 1)$ is the following representation of the quantum double
$D(G)=\Bbb C[G]\ltimes \mathcal O(G)$: it is the regular
representation of the function algebra
$\mathcal O(G)$, on which $G$ acts by conjugation.
In this case proposition \ref{I(1)} for trivial $V$ is the standard fact that 
for conjugation action, $\mathcal O(G)=\oplus_{Y\in
  Irrep(G)}Y\otimes Y^*$. 
\end{example}

\begin{proof}
Let $\mC=\Rep(A)$, where $A$ is a weak
Hopf algebra. Then $Z(\mC)=\Rep(D(A))$, where $D(A)$ is the
quantum double of $A$ (see \cite{NTV}). As a space, 
$D(A)=A^*\otimes_{A_{min}}A$. So we have 
$I(V)|_\mC=D(A)\otimes_A V=A^*\otimes_{A_{min}}V$, with the
action of $A$ defined by 
$h(\phi\otimes v) = h\3 \actl \phi \actr S(h\1) \otimes h\2 v$
for all $h\in A,\, \phi\in A^*,\, v\in V$.
This yields exactly 
$\oplus_{Y\in Irr(\mC)}Y\otimes V\otimes Y^*$, 
where the tensor product is
taken in the representation category of $A$. The proposition is
proved. 
\end{proof}

\begin{proposition}\label{numobj} The number 
$\sum_{X\in Irr(Z(\mC))}[X|_{\mC}:\mathbf 1]^2$ 
is equal to the number of simple objects of $\mC$.
\end{proposition}
 
\begin{proof} 
This sum equals $\dim{\rm End}(I(\mathbf
1))$, which is the same as $[I(\mathbf 1)|_{\mC}:\mathbf 1]$. But
by Proposition \ref{I(1)} we
know that $I(\mathbf 1)|_{\mC}=\oplus_{Y\in Irr(\mC)}Y\otimes Y^*$, 
so the result follows.
\end{proof}

\begin{proposition} (The class equation)\label{cleq}
Let $\mC$ be a spherical fusion category. Then one has 
$$
\sum_{X\in Irr(Z(\mC)):[X|_{\mC}:\mathbf 1]\ne
  0}[X|_{\mC}:\mathbf 1]\frac{1}{m_X}=1,
$$
where $m_X=\frac{\dim \mC}{\dim X}$ is an algebraic integer. 
\end{proposition}

\begin{proof}
The proposition is immediately obtained 
by computing the dimension of $I(\mathbf 1)$ in two ways. 
On the one hand, this dimension is equal to $\dim \mC$ by 
Proposition \ref{I(1)}. On the other hand, it equals $\sum
[X|_\mC:\mathbf 1]\dim X$. The fact that $m_X$ is an algebraic
integer follows from Proposition \ref{moddivi}.
The proposition is proved. 
\end{proof}

\begin{example} Let $\mC=\Rep(G)$.
In this case $Z(\mC)=\Rep D(G)$, so simple objects 
are parametrized by pairs 
(conjugacy class, irreducible representation of the
centralizer). The simple objects $X\in Z(\mC)$ for which
$X|_\mC$ contains $\mathbf 1$ are exactly those for which 
the representation of the centralizer is trivial. 
Thus, the equation of Proposition \ref{cleq} is exactly 
the class equation for $G$. 
\end{example}

\end{section}
