---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-003-13-definition-and-properties
section_title: "Definition and properties"
section_number: 1.3
pages: 3-5
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.984
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.def}

To explain the new concept, consider the linear $q$-difference equation
\be
\label{qdiff}
\s X = A X
\ee
for a vector-valued function $X=X(t,q)$, where $(\s X)(t,q)=X(qt,q)$ denotes the
shift operator, $A(t,q) \in \GL_r(\BQ(t,q))$ and $q$ is a nonzero complex number
with $|q|\neq1$. 
Fix a fundamental matrix solution $U$ to~\eqref{qdiff} at $t=0$, which we assume
is filtration-preserving and of weight $\kappa_{U}=\diag(\tau^{\kappa_{U,1}},\dots,
\tau^{\kappa_{U,r}})$ and define 
\be
\label{Om}
\Om_{U,\gamma} =(U|_{\kappa_{U}}\gamma)U^{-1},
\qquad \gamma=\sma abcd \in \SL_2(\BZ)
\ee
where the slash operator $|_{\kappa_{U}}\gamma$ is defined in Section~\ref{sub.slash}
below. The map $\gamma \mapsto \Om_{U,\gamma}$ is a cocycle of $\SL_2(\BZ)$, i.e.,
it satisfies
\be
\label{Omcoc}
\Om_{U,\gamma \gamma'}(z,\tau)
= \Om_{U,\gamma}(\gamma'(z,\tau))  \Om_{U,\gamma'}(z,\tau) 
\ee
for all $\gamma, \gamma' \in \SL_2(\BZ)$.
Likewise, let $V$ denote a filtration-preserving fundamental solution at $t=\infty$,
and $\vM=V^{-1}U$ denote the monodromy matrix (often called ``connection matrix'').
The monodromy is always an elliptic function (i.e., $\s$-invariant).
If it satisfies the equation
\be
\label{Mmod}
\vM = \Delta_{\kappa_V,\gamma} (\vM|_{\kappa_U} \gamma),
\qquad \gamma=\sma abcd \in \SL_2(\BZ)
\ee
for some $\gamma=\sma abcd \in \SL_2(\BZ)$ then the cocycle matrices associated to
$U$ and $V$ are equal: 
\be
\label{OmUV}
\Om_{U,\gamma} = \Om_{V,\gamma} \qquad \gamma=\sma abcd \in \SL_2(\BZ) \,.
\ee
(The converse holds, too, and the equivalence of~\eqref{OmUV} and~\eqref{Mmod}
holds for each fixed $\gamma$). A priori, $\Om_{\gamma}=\Om_{U,\gamma}=\Om_{V,\gamma}$
is a holomorphic function of $\tau \in \BC\setminus\BR$ and a
meromorphic function of $z$ (with $t=\e(z)$) with poles in a finite union of
translates of the lattice $\BZ+\tau\BZ$. For an element
$\gamma=\sma abcd \in \SL_2(\BZ)$, we let $\BC_\gamma$ denote the cut
plane $\BC\setminus (-\infty,-d/c]$ (if $c>0$),
$\BC\setminus [-d/c,\infty)$ (if $c<0$) and $\BC\setminus\BR$ when $c=0$. 
The next definition concerns an improved analytic property of $\Om_{\gamma}$.
\begin{definition}
  \label{def.qmm}
  We say that a $q$-difference equation is \emph{modular} if for all $\gamma
  \in \SL_2(\BZ)$, its cocycle $\Om_{\gamma}$ extends to a meromorphic function
  of $(z,\tau)\in\BC\times\BC_\gamma$ with potential poles at
  $z \in S_\gamma + \BZ + \tau \BZ$ for a finite set $S_\gamma$. 
\end{definition}

\noindent
We make several comments concerning this definition. 

\noindent 1. 
For a modular $q$-difference equation, the two sides of $\tau \in \BC\setminus\BR$
communicate: the restriction of $\Om_{\gamma}$ on the one side of the plane
$\Im(\tau)>0$ uniquely determines (and is determined by) the function on the
other side $\Im(\tau)<0$.

\noindent 2. 
In a sense, our notion of modular linear $q$-difference equation is a $q$-analogue
of the second, third and fourth order modular linear differential 
equations studied by Kaneko, Nagatomo, Zagier and others~\cite{Arike:fourth-order, 
Kaneko:third-order,Kaneko-Zagier} in relation to Conformal Field Theory 
and Vertex Operator Algebras. The characters of a VOA (under a mild $C_2$-condition)
are solutions to a modular linear differential equation
~\cite{Dong:modular-invariance,Zhu:modular-invariance}. An alternative title of
our paper could be
``Modular linear $q$-difference equations'' in direct analogy with the
modular linear differential equations of CFTs and VOAs. On the other hand, the
  current title emphasises the ``module'' aspect as opposed to the ``equation
  aspect''. 

\noindent 3. 
Our notion explains conceptually the improved analyticity properties conjectured
in relation to the structure of exact and perturbative invariants of Chern--Simons
theory~\cite{GGM:peacock,GGM,GGMW:trivial,GZ:qseries,GZ:kashaev}, as well as the
work of Gukov et al relating logarithmic CFTs and VOAs to Chern--Simons
theory~\cite{Cheng:VOA}. 
  
\noindent 4. 
Modular linear differential equations seem rare. On the other hand,
modular linear $q$-difference equations appear abundant: we conjecture
(see the end of Section~\ref{sec.intro}) that the $\hat A$-polynomial of a knot
(i.e., the linear $q$-difference equation satisfied by the colored Jones polynomial
of a knot~\cite{GL}) is a modular linear $q$-difference equation. This brings
a new perspective to the Jones polynomial of a knot.

\noindent 5. 
The modularity of the monodromy for modular $q$-holonomic modules is a restricted
condition, which leads to the complete determination of the monodromy even when a
fundamental solution is defined by $q$-Borel resummation. This in turn
completely determines the so-called $q$-Stokes phenomenon coming from the
change of the ray of the $q$-Laplace transform.

\noindent 6. 
The cocycle $\Omega_{U,\gamma}$ as a function of a fundamental solution of a
linear $q$-difference equation appears new and different from the matrices
considered in Etingof~\cite{Etingof} that generate the Galois group of the equation.

\noindent 7. 
The above definition involves all elements of $\SL_2(\BZ)$, although it
imposes no improved extension when $\gamma_{2,1}=0$.  The third part of the next
theorem (under the hypothesis that $\Om_T=I$ which is satisfied in all of our
examples), rephrases the modularity of Definition~\ref{def.qmm}
in terms of $\Om_S$ alone, where $S=\sma 0{-1}10$ and $T=\sma 1101$ of
$\SL_2(\BZ)$ are the standard generators of $\SL_2(\BZ)$. Recall that
$\BC'=\BC_S=\BC\setminus(-\infty,0]$.  

\begin{theorem}
\label{thm.ST}
{\rm (a)} If Equation~\eqref{Mmod} for the monodromy holds for $\gamma=S$
and $\gamma=T$, then it holds for all $\gamma \in \SL_2(\BZ)$.
\newline
{\rm (b)} If $\Om$ is an $\SL_2(\BZ)$-cocycle with $\Om_T=I$, then $\Om_S$
satisfies the 4-term and the 3-term functional equations

\begin{subequations}
\begin{align}
  \label{OmS1}
  1 &= 
  \Om_S\left(-\frac{z}{\tau},-\frac{1}{\tau}\right)
  \Om_S\left(-z,\tau\right)
  \Om_S\left(\frac{z}{\tau},-\frac{1}{\tau}\right)
  \Om_S(z,\tau) \\
  \label{OmS2}
  \Om_S(z,\tau) &= \Om_S\left(\frac{z}{\tau+1}, \frac{\tau}{\tau+1}\right)
  \Om_S(z,\tau+1) \,.
\end{align}
\end{subequations}
Conversely, given $\Om_T=I$ and $\Om_S$ that satisfies the above functional
equations, there is a $\SL_2(\BZ)$-cocycle with those values.
\newline
{\rm (c)} If $\Omega$ is a cocycle such that $\Om_T=I$ and $\Om_S$ extends as
a meromorphic function of $(z,\tau) \in \BC \times \BC'$, then $\Om_\gamma$
extends as a meromorphic function of $(z,\tau) \in \BC \times \BC_\gamma$
for all $\gamma \in \SL_2(\BZ)$. 
\end{theorem}

Note that with the assumptions of part (c) above, we have
\be
\label{Om-I}
\Om_{-I}(z,\tau) = \Om_S\left(\frac{z}{\tau},-\frac{1}{\tau}\right)
\Om_S(z,\tau)
\ee
which is meromorphic on $\BC\times (\BC\setminus\BR)$, in general does not extend
any further; see for instance the cocycle of Theorem~\ref{thm.ex1} below.

\noindent 8. 
Our final comment concerns the distinction between a linear $q$-difference equation
to a $q$-holonomic module. A linear $q$-difference equation leads to a pair
$(M,e)$ of a $q$-holonomic module $M$ over the $q$-Weyl algebra
$\calW=\BQ(q,t) \langle \s \rangle/(\s t-q t \s)$ and a cyclic vector $e$ of $M$. 
The category $\calM$ of $q$-holonomic modules is an abelian category,
which admits a multivariable extension closed under the usual operations on sheaves.
For a detailed introduction, see~\cite{Coutinho} and~\cite{Sabbah}, and
also~\cite{GL:survey}. Whereas $D$-modules over the Weyl algebra have
only one dual (see for example, ~\cite[Sec.2.2]{Singer:galois-differential}), modules
over the $q$-Weyl algebra have two duals $M^{\wedge}$ (the usual $\mathrm{Hom}$-dual
as in the case of $D$-modules) and a dual $M^{\vee}$ coming from the involution
$q \mapsto q^{-1}$, discussed in Section~\ref{sub.duality} below.

The next lemma summarises some categorical properties of modular $q$-holonomic
modules.

\begin{lemma}
\label{lem.cat}
  \rm{(a)} Modularity of a $q$-holonomic module is independent of the choice
  of a cyclic vector.
  \newline
  \rm{(b)} If $0 \to M' \to M \to M'' \to 0$ is a short exact sequence of
  $q$-holonomic modules and $M$ is modular, then $M$ and $M'$ are also modular.
  \newline
  \rm{(c)} $M$ is a modular, then $M^\wedge$ and $M^\vee$ are modular with
  cocycles given by
  \be
\label{Omduals}
\Om^\wedge(z,\tau):=\Om(z,-\tau), \qquad \text{and}
\qquad \Om^\vee=(\Om^{-1})^t
\ee
where $\Om$ is a cocycle of $M$. 
\end{lemma}
