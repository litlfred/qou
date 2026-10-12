---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-002-14-comparing-grothendieck-group-and-trace
section_title: "Comparing Grothendieck group and trace"
section_number: 1.4
pages: 3-7
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.98
---
We have now described two flavors of decategorification.  One which we will refer to as the {\em Grothendieck decategorification} which is closely connected to the notion of dimension, graded dimension, and Euler characteristic.
Our second notion of decategorification, which we will call the {\em trace decategorification}, seems to generalize the Grothendieck group decategorification in much the same way that the trace of linear map generalizes the dimension of a vector space $\dim(V) = \tr(1_V)$.   The trace decategorification is closely connected with the usual trace and it gives rise to a notion of traced Euler characteristic.

These two notions of decategorification can actually produce the same results in some very interesting examples.
One of the most spectacular examples is the categorification
of the Jones polynomial by the Khovanov complex of graded $\Z$-modules, where
the Jones polynomial can be recovered as the graded Euler characteristic~\cite{Kh1,Kh2}.
Bar-Natan generalized Khovanov's construction by defining the so-called Khovanov bracket:
a complex over an additive category of special 2-dimensional cobordisms.
In his setting, one recovers the Jones polynomial by means of the
traced Euler characteristic (Theorem 6 \cite{Dror}). Hence,   the
functor $\Tr$ or the zeroth Hochschild--Mitchell homology replaces $K_0$ in the Bar-Natan setting.







This survey paper is devoted to the comparison of $K_0$ and $\Tr$ as decategorification functors.  The interplay between these two notions of decategorification is surprisingly rich.  It can be thought of as a categorical counterpart to the Chern character map, see for example~\cite{CW}.





















\subsection{Quantum group categorifications}





There is a strong interplay between quantum link invariants and algebraic objects known as quantum groups. Given the existence of link homology theories categorifying link invariants, it is perhaps not surprising to discover that quantum groups can also be categorified.  In this article we will examine how the two notions of decategorification given by the Grothendieck group and the trace can be applied to categorified quantum groups.


Quantum groups are Hopf algebras associated to Lie algebras $\mf{g}$.  They are obtained by $q$-deforming the universal enveloping algebra $\mathbf{U}(\mf{g})$.   Lusztig's modified, or idempotented, form $\dot{\mathbf{U}}(\mf{g})$ of the quantum group $\mathbf{U}_q(\mf{g})$ is well suited for categorification. These algebras are equipped with a family of orthogonal idempotents $1_{\lambda}$ indexed by the weight lattice $X$ of $\mf{g}$.  Any $\k$-algebra $A$ equipped with orthogonal idempotents indexed by a set $X$ can be regarded as an additive category whose objects are the elements of $X$.  Given two elements $\lambda, \mu \in X$,  $\k$-vector space of maps from $\lambda$ to $\mu$ can be defined by $1_{\mu} A 1_{\lambda}$.  In this framework, the idempotents $1_{\lambda}$ are thought of as identity morphisms from the object $\lambda$ to itself.  Composition in the category
\[
1_{\mu'} A 1_{\lambda'} \times 1_{\mu} A 1_{\lambda}\to \delta_{\mu,\lambda'} 1_{\mu'} A 1_{\lambda}
\]
is given by multiplication in $A$.



By thinking of a quantum group $\mathbf{U}_q(\mf{g})$ as a linear category in this way, we are naturally led to consider a categorification of $\mathbf{U}_q(\mf{g})$ given by the structure of a 2-category and our decategorification map must reduce a linear 2-category to a linear 1-category.











Associated to a field $\k$ and a symmetrizable Kac-Moody algebra $\mf{g}$, a 2-category $\UcatD(\mf{g})$ was defined in \cite{KL3} generalizing the $\mf{sl}_2$ case from \cite{Lau1}.   The 2-category $\UcatD(\mf{g})$ is the idempotent completion, or Karoubi envelope, of a 2-category $\Ucat(\mf{g})$ defined in terms of a graphical calculus.  More precisely, the objects of the category $\Ucat(\mf{g})$ are indexed by the weight lattice $X$ of $\mf{g}$.  The morphisms are formal direct sums of composites of maps $\onel \maps \lambda \to \lambda$, $\cal{E}_i \onel \maps \lambda \to \lambda + \alpha_i$, and $\cal{F}_i\onel \maps \lambda \to \lambda-\alpha_i$ corresponding to the Chevalley basis of $\mf{g}$.  For each 1-morphism $x$ there is also a grading shifted 1-morphism $x\la t\ra$ in $\Ucat(\mf{g})$.  The 2-morphisms are given by $\Bbbk$-linear degree preserving combinations of certain planar diagrams modulo local relations. See Figure~\ref{fig_Ucat-diagram} for an example of planar diagram in $\Ucat(\mf{g})$.

\begin{figure}[h]
 $
 \vcenter{
    \xy 0;/r.16pc/:
  (-8,-4)*{\fecross};(8,-4)*{\fecross};
  (0,2)*{\scap};(0,4)*{\lcap};
  (0,-10)*{\scupfe};(0,-14)*{\lcupef};
  (13,-12)*{\scs i}; (13,5)*{\scs k};
   (-18,-18)*{\lambda'};
  \endxy} \;\;
  \vcenter{\xy 0;/r.16pc/:
 (-4,-15)*{}; (-20,25) **\crv{(-3,-6) & (-20,4)}?(0)*\dir{<}?(.6)*\dir{}+(0,0)*{\bullet};
 (-12,-15)*{}; (-4,25) **\crv{(-12,-6) & (-4,0)}?(0)*\dir{<}?(.6)*\dir{}+(.2,0)*{\bullet};
 ?(0)*\dir{<}?(.75)*\dir{}+(.2,0)*{\bullet};?(0)*\dir{<}?(.9)*\dir{}+(0,0)*{\bullet};
 (-28,25)*{}; (-12,25) **\crv{(-28,10) & (-12,10)}?(1)*\dir{>};
  ?(.2)*\dir{}+(0,0)*{\bullet}?(.35)*\dir{}+(0,0)*{\bullet};
 (-36,-15)*{}; (-36,25) **\crv{(-34,-6) & (-35,4)}?(1)*\dir{>};
 (-28,-15)*{}; (-42,25) **\crv{(-28,-6) & (-42,4)}?(1)*\dir{>};
 (-42,-15)*{}; (-20,-15) **\crv{(-42,-5) & (-20,-5)}?(1)*\dir{>};
 (6,10)*{\cbub{m}{}};
 (-23,0)*{\cbub{}{}};
 (-2,-12)*{\scs i}; (-14,-12)*{\scs k};  (-19,-12)*{\scs i};
    (-46,22)*{\scs \ell}; (-33,22)*{\scs i}; (-10,22)*{\scs j};
    (8,18)*{\scs j}; (-20,7)*{\scs \ell};
 \endxy}
 \vcenter{ \xy 0;/r.16pc/: (-14,8)*{\xybox{
 (0,-10)*{}; (-16,10)*{} **\crv{(0,-6) & (-16,6)}?(.5)*\dir{};
 (-16,-10)*{}; (-8,10)*{} **\crv{(-16,-6) & (-8,6)}?(1)*\dir{}+(.1,0)*{\bullet};
  (-8,-10)*{}; (0,10)*{} **\crv{(-8,-6) & (-0,6)}?(.6)*\dir{}+(.2,0)*{\bullet}?
  (1)*\dir{}+(.1,0)*{\bullet};
  (0,10)*{}; (-16,30)*{} **\crv{(0,14) & (-16,26)}?(1)*\dir{>};
 (-16,10)*{}; (-8,30)*{} **\crv{(-16,14) & (-8,26)}?(1)*\dir{>};
  (-8,10)*{}; (0,30)*{} **\crv{(-8,14) & (-0,26)}?(1)*\dir{>}?(.6)*\dir{}+(.25,0)*{\bullet};
 (-18,-8)*{\scs i}; (-6,-8)*{\scs i}; (2,-8)*{\scs k};
   }};
 (5,0)*{\lambda};
 \endxy}$
\caption{An example of a diagram representing a 2-morphism in $\Ucat(\mf{g})$ from
$
\cal{E}_i^2\cal{E}_{\ell}\cal{F}_i \cal{F}_k \cal{F}_i \cal{E}_i\cal{E}_i \cal{E}_k \onel
$
to $
 \cal{E}_{\ell} \cal{E}_i \cal{F}_j \cal{F}_j \cal{F}_i \cal{E}_j \cal{E}_i \cal{E}_k \cal{E}_i\onel\la t\ra
$.  The degree $\la t \ra$ of this 2-morphism is determined by the relationship between the simple roots $i,j,k, \ell$ in the Cartan datam associated to $\mf{g}$.} \label{fig_Ucat-diagram}
\end{figure}

Extending the split Grothendieck group decategorification map for linear categories, it is possible to define the split Grothendieck group $K_0$ of a linear 2-category.  It was shown in \cite{KL3} for $\mf{g}=\mf{sl}_n$ that applying this notion of decategorification to the Karoubi envelope $\UcatD(\mf{sl}_n)$ of the 2-category $\Ucat(\mf{sl}_n)$ produces the integral idempotented form of the quantum enveloping algebra $\mathbf{U}_q(\mf{sl}_n)$.  Hence, with this notion of decategorification the 2-category $\UcatD(\mf{sl}_n)$ can be viewed as a categorification of the quantum group $\mathbf{U}_q(\mf{sl}_n)$.  The $n=2$ case of this result was proven in~\cite{Lau1} and the case of general $\mf{g}$ appears in \cite{Web5}.  For a closely related construction see ~\cite{Rou2}.


More recently it has been shown that using a 2-categorical analog of the trace as the decategorification map produces some very rich structures~\cite{BHLZ,Marko,BGHL}.   The trace relation can be realized diagrammatically by considering the diagrams for $\Ucat(\mf{g})$ on an annulus.
\[
 \vcenter{ \xy 0;/r.16pc/:
 (8,0)*{
 \hackcenter{\begin{tikzpicture}
  \path[draw,blue, very thick, fill=blue!10]
   (-2,-.6) to (-2,.6) .. controls ++(0,1.85) and ++(0,1.85) .. (2,.6)
   to (2,-.6)  .. controls ++(0,-1.85) and ++(0,-1.85) .. (-2,-.6);
    \path[draw, blue, very thick, fill=white]
    (-0.25,0) .. controls ++(0,.35) and ++(0,.35) .. (0.25,0)
            .. controls ++(0,-.35) and ++(0,-.35) .. (-0.25,0);
\end{tikzpicture}}
 };
(10,8)*{\lambda}; (-15,12)*{\lambda'};
  (8,8)*{\lcap};
  (8,14)*{\xlcap};

 
 (8,-14)*{\xlcupef};
 (-8,0)*{\ecross};
 (20,0)*{\sfline};
 (28,0)*{\sfline};
 (8,-10)*{\lcupef};
(-2,-3)*{\scs i}; (-15,-3)*{\scs i};
 (-10,1)*{\bullet};
 \endxy}
\]
The invariance of the graphical calculus of $\Ucat(\mf{g})$ under planar deformations allows us to slide portions of the diagram around the annulus imposing the trace relation.








\subsection{Traces of categorified quantum groups}




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
