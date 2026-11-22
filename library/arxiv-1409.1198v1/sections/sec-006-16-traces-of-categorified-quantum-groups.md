---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-006-16-traces-of-categorified-quantum-groups
section_title: "Traces of categorified quantum groups"
section_number: 1.6
pages: 5-7
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.973
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
In this article we hope to emphasize that the trace decategorification map $\Tr$ has various
advantages to $K_0$.
\begin{itemize}
  \item Using $\Tr$ we can work with the 2-category $\Ucat(\mf{g})$ rather than its Karoubi envelope, since $\Tr$ does not change under the passage to the Karoubi envelope.  This is a nice advantage as the passage to the Karoubi envelope often takes us out of the purely diagrammatic world.
\item Trace is defined for linear categories; in order for $K_0$ to be defined the category needs to be additive.
  \item The trace can have a richer structure than $K_0$ as is demonstrated by Theorems \ref{qqq} and \ref{thm_main}.


\end{itemize}

We outline the methods and tools used in studying $K_0$ and traces for categorified quantum groups.




\subsubsection{Trace and $K_0$ of $\UcatD$}



Just as the Euler characteristic and traced Euler characteristic agree for Khovanov homology,  we will explain that the 2-categories $\Ucat(\mf{g})$ simultaneously categorify the quantum group $\mathbf{U}(\mf{sl}_n)$ via the Grothendieck group decategorification functor $K_0$ and the trace decategorification functor $\Tr$.

\begin{thm}[\cite{KL3,BGHL}]
Let $\k$ be a field of characteristic $0$ and $\g=\fsl_n$.
Then there are isomorphisms
\[
 \Tr(\Ucat) \cong K_0(\UcatD) \otimes_\Z \k \cong \dot{\mathbf{U}}.
\]
and $\HH_i(\Ucat)=0$ for $i>0$.
\end{thm}




Again, this result is somewhat surprising since these two decategorification procedures need not agree in general.  We will explain that there is a large class of examples closely connected to geometric settings where this phenomenon is likely to occur.


Very recently a direct connection was established between categorified quantum groups and $\mf{sl}_n$ link homology theories~\cite{LQR,QR}.  Working in an enhanced foam category introduced by Christian Blanchet, one can realize all the foam relations in a Bar-Natan like setting as arising from the relations in the categorified quantum group $\Ucat(\mf{sl}_n)$ via so called foamation functors first studied in \cite{MackFoam}.   Once translated through these foamation functors, the theorem above immediately implies that the
traced and usual Euler characteristics in the  $\mf{sl}_n$ link homology theories coincide.

\begin{cor}
In $\fsl_n$ link homology theories, traced and usual Euler characteristics do coincide.
\end{cor}



\subsubsection{Trace and $K_0$ of $\Ucat^{\ast}$}





By allowing homogeneous, but not necessarily grading preserving 2-morphisms in $\Ucat(\mf{g})$ we can define a version of the 2-category with larger 2-hom spaces.  Let $\Ucat^{\ast}(\mf{g})$ denote the 2-category with the same objects and one morphisms as $\Ucat(\mf{g})$, but with 2-hom spaces between one morphisms $X \onel$ and $Y\onel$ given by
\[
 \Ucat^{\ast}(\mf{g})(X\onel, Y\onel) := \bigoplus_{t\in \Z} \Ucat(\mf{g})(X\onel, Y\onel \la t \ra).
\]
One can alternatively think of $\Ucat^{\ast}$ as the result of adding isomorphisms $X\onel \to X\onel \la t\ra $ for all $t\in \Z$.  This essentially kills the grading making Grothendieck ring $K_0(\Ucat^{\ast})$ only a $\Z$-module, rather than a $\Z[q,q^{-1}]$-module.  While this version of the 2-category is less interesting from a $K_0$ perspective, it has interesting consequences for the trace.


The trace of the graded version $\U^*$ of the categorified quantum $\fsl_2$ is isomorphic
to  the idempotent form of the current algebra $\bfU(\fsl_2[t]):=\bfU(\fsl_2\otimes \Q[t])$ \cite{BHLZ}. In \cite{BHLZ}
it is also shown that for the integral version $\U_\Z(\fsl_2)$ ($\k$ is replaced by $\Z$ in the definition), we have $$\Tr(\U_\Z)=K_0(\Udot_\Z)=K_0(\Udot)\, .$$
It is interesting that one loses the $q$ by considering the graded category $\U^{\ast}$, but one sees the positive part of the loop algebra $\mf{sl}_2 \otimes \Q[t,t^{-1}]$ appear.



We expect that these results generalize to finite type simply-laced Kac-Moody algebras $\mf{g}$.  However, to ease the exposition in this article, we set $\mf{g}=\fsl_n$ and describe evidence for the following conjecture in section~\ref{current-sln}.

\begin{conjecture}
For $\g=\fsl_n$, we have
$$K_0(\Udot_\Z)=
\Tr(\U_\Z)=K_0(\Udot)$$
and $\Tr(\U^\ast_\Z)$ coincides with the integral idempotented version of the current algebra
$\bfU(\fsl_n[t]) $ defined in Section \ref{current-sln}.
\end{conjecture}




In this paper we  construct a homomorphism $\bfU(\fsl_n[t]) \to \Tr(\Ucat^{\ast}(\fsl_n))$ utilizing the graphical
calculus and verifying relations directly  (see Proposition \ref{prop-cur}).  This implies that

the center of objects
$Z(\Udot):=\bigoplus_{\lambda \in X}\End_{\Udot}(\onel)$ of $\Udot$ (see section~\ref{action} for more details) is a module over the current algebra $\bfU(\fsl_n[t])$.
An immediate consequence of this result is the following theorem.

\begin{thm}\label{2-reps}
Any 2-representation $\U(\fsl_n) \to \K$ gives rise to an action of the current algebra
$\bfU(\fsl_n[t])$ on $\Tr(\K)$ and the
center $Z(\K)$ of objects in $\K$.
\end{thm}


This theorem is proven in Section \ref{action}. Let us discuss one implication of this result.   Brundan made the surprising discovery that one could define an action of the Lie algebra $\hat{\mf{g}}:=\mf{gl}_{\infty}(\mathbb{C})$ on the center $Z(\cal{O}) = \bigoplus_{\nu} Z(\cal{O}_{\nu})$ of all integral blocks $\cal{O}_{\nu}$ of category $\cal{O}$~\cite{Brundan}.
In this action, the Chevalley generators of $\hat{\mf{g}}$ act as certain trace maps associated to canonical adjunction maps between special translation functors that arise from tensoring with a $\mf{g}$-module and its dual.
In \cite{BO} it is explained that this action is closely connected to Ginzburg's geometric construction of representations of the general linear group~\cite{Gin}.
Theorem \ref{2-reps} provides a context  for understanding this surprising action by traces on category $\cal{O}$.  Indeed, Brundan's action is part of a broad phenomenon that occurs within the context of higher representation theory:  any categorified representation
of the quantum group $\mathbf{U}_q(\mf{sl}_n)$ immediately gives rise to an action of $\bfU(\mf{sl}_n[t])$ on the center of objects in the 2-representation via categorical traces. In particular,
an action of $\UcatD(\mf{sl}_n)$ on graded category $\cal{O}$ would automatically imply and generalize Brundan's result.  More details about this action will be given in \cite{BGHL}.





\subsubsection{Organization of this paper}


This paper is organized as follows. After recalling the
 diagrammatics for the trace  in pivotal categories, taking as example
 $\cat{Vect}_\k$,  we define the trace functor for linear and additive 1- and 2-categories and study its properties.
In Section 3 we recall the notion of (strongly) upper-triangular category from \cite{BHLZ}, which is
particularly convenient for computing all Hochschild--Mitchell homology groups.
In the next sections  different versions of the categorified
 quantum  $\fsl_n$ are defined and their decategorifications by means
of $K_0$ and $\Tr$ are compared.
The last chapter is devoted to the proof of Theorem \ref{2-reps}.

To make this  paper more  accessible for graduate students,
each section is supplied with many examples, exercises, pictures and references to textbooks.
Places where special knowledge  is required
are marked and can be ignored in the first reading.

\bigskip

\noindent {\bf Acknowledgments:}
A.B. and Z.G. were  supported by Swiss National Science Foundation under Grant PDFMP2-141752/1.
K.H. was partially supported by JSPS Grant-in-Aid for Scientific Research (C) 24540077.
A.D.L  was partially supported by NSF grant DMS-1255334 and by the John Templeton Foundation.
A.D.L is extremely grateful to Mikhail Khovanov for sharing his insights and vision about higher representation theory.
Some of the ideas and calculations appearing in this article were done as part of this collaboration.  He is also grateful to Arun Ram for helpful decategorification discussions.
A.B. would like to thank Benjamin Cooper  for helpful conversations.
