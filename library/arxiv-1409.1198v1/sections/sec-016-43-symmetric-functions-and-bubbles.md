---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-016-43-symmetric-functions-and-bubbles
section_title: "Symmetric functions and bubbles"
section_number: 4.3
pages: 27-32
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.974
---
\label{sec_sym-bub}



The calculus of closed diagrams in the 2-category $\Ucat_Q(\mf{sl}_n)$ is remarkably rich.   A prominent role is played by the non-nested dotted bubbles of a fixed orientation since any closed diagram in the graphical calculus for $\Ucat_Q(\mf{sl}_n)$ can be reduced to composites of such diagrams.

There is a beautiful analogy between dotted bubbles in the graphical calculus and various bases for the ring of symmetric functions.  In \cite{Lau1} it is shown that there is an isomorphism

\begin{eqnarray}
  \psi_{\lambda} \maps \;\;{\rm Sym} & \;\; \longrightarrow\;\;& Z(\l)= \Ucat_Q(\mf{sl}_2)(\onel,\onel) \\
  h_r & \;\;\mapsto \;\; &  \xy
  (0,0)*{\icbub{\spadesuit+r}{i}};
  (8,8)*{\lambda};
  \endxy \nn \\
   (-1)^s e_s& \;\;\mapsto \;\; & \xy
  (0,0)*{\iccbub{\spadesuit+s}{i}};
  (8,8)*{\lambda};
  \endxy \nn
\end{eqnarray}
where ${\rm Sym}$ denotes the ring of symmetric functions, $h_r$ denotes the complete symmetric function of degree $r$, and $e_{s}$ denotes the elementary symmetric function of degree $s$.  In fact, under this isomorphisms the well known relationship between complete and elementary symmetric functions becomes the infinite Grassmannian equation~\eqref{eq_infinite_Grass}.

It is well known that for a partition $\lambda = (\lambda_1, \dots, \lambda_n)$ with $\lambda_1 \geq \lambda_2 \geq \dots \geq \lambda_n$, products of elementary symmetric functions $e_{\lambda} = e_{\lambda_1} \dots e_{\lambda_n}$ form a basis for ${\rm Sym}$, see for example \cite{McD}.  Likewise, products of complete symmetric functions also provide a basis for $\sym$.  This mirrors the fact that any closed diagram in the graphical calculus for $\Ucat_Q(\mf{sl}_2)$ can be reduced to a product on non-nested bubbles of a given orientation.

In the $\mf{sl}_n$ calculus of the 2-category $\Ucat(\mf{sl}_n)$,  we have the isomorphism
$$ \psi_{\lambda} \maps \;\; \prod_{i\in I}{\rm Sym}  \;\; \longrightarrow\;\; Z(\l)= \Ucat_Q(\mf{sl}_n)(\onel,\onel) $$
 since any closed diagram can still be reduced to products of non-nested closed bubbles labelled by $i \in I$.

In what follows, it will be interesting to consider which products of closed diagrams correspond to the basis of $\sym$ given by the power sum $p_r$ symmetric functions.
Using a formula that expresses power sum symmetric functions in terms of products of complete and elementary symmetric functions, we can denote by $p_{i,r}(\lambda)$ for $r>0$, the image of the power symmetric polynomial on $i$-labelled strands in $Z(\l)$:
\begin{equation} \label{eq_defpil}
 p_{i,r}(\lambda) := \sum_{a+b=r} (a+1)
 \xy
   (0,-2)*{\icbub{\spadesuit+a}{i}};
   (12,-2)*{\iccbub{\spadesuit+b}{i}};
  (8,8)*{\lambda};
 \endxy
 =  - \sum_{a+b=r} (b+1)
 \xy
   (0,-2)*{\icbub{\spadesuit+a}{i}};
   (12,-2)*{\iccbub{\spadesuit+b}{i}};
  (8,8)*{\lambda};
 \endxy =  -\sum_{a+b=r} a
 \xy
   (0,-2)*{\icbub{\spadesuit+b}{i}};
   (12,-2)*{\iccbub{\spadesuit+a}{i}};
  (8,8)*{\lambda};
 \endxy
\end{equation}
For later convenience we set $p_{i,0}(\l) = \lambda_i$.

\begin{exercise}
Using the bubble slide formulas from exercise~\ref{exercise_bubble-slides}, show that
\[
 p_{i,r}(\lambda) =
\begin{cases} \quad -\;\;
 \text{$\xy
 (-6,0)*{};
  (6,0)*{};
  (15,12)*{\lambda};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(.02)*\dir{>}
   ?(1)*\dir{>} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs \spadesuit +r};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{<} ?(1)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs \spadesuit+0};
  \endxy $}
  & \mbox{if } \lambda_i  \geq 0  \\
\quad  \;\;\;\text{$\xy
 (-6,0)*{};
  (6,0)*{};
  (15,12)*{\lambda};
  (-4,0)*{}="t1";  (4,0)*{}="t2";
 "t2";"t1" **\crv{(4,6) & (-4,6)}; ?(0)*\dir{<}
   ?(.96)*\dir{<} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(4,-6) & (-4,-6)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-3)*{\scs \spadesuit +r};
  (-12,0)*{}="t1";  (12,0)*{}="t2";
  "t2";"t1" **\crv{(12,15) & (-12,15)}; ?(0)*\dir{>} ?(1)*\dir{>} ?(.3)*\dir{}+(2,2)*{\scs i};
  "t2";"t1" **\crv{(12,-15) & (-12,-15)};
  ?(.7)*\dir{}+(0,0)*{\bullet}+(2,-4)*{\scs \spadesuit+0};
  \endxy $}
  & \mbox{if }  \lambda_i  \leq 0,
\end{cases}
\]
so that the formulas defining $p_r(\lambda)$ can be obtained by simplifying a degree $r$ bubble with one orientation nested inside of a degree zero bubble with the opposite orientation.
\end{exercise}

Note that other interesting basis for symmetric functions also have natural graphical analogs.  In \cite{KLMS} diagrams corresponding to the basis of Schur functions are given.

\begin{exercise} \label{exercise_power-slides}
Using the bubble sliding equations from exercise~\ref{exercise_bubble-slides}, prove the following power sum slide rules
\begin{eqnarray}
\label{eq_powerslide1}
\xy 0;/r.18pc/:
  (12,6)*{\lambda-\alpha_j};
  (0,0)*{\bbe{}};
  (0,-12)*{\scs j};
  (14,-2)*{p_{i,r}(\lambda-\alpha_j)};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 & = &
 \begin{cases}
   \xy 0;/r.18pc/:
  (-10,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (-10,-2)*{p_{i,r}(\lambda)};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 \;\; - \;\; 2\;\; \;\;\xy 0;/r.18pc/:
  (-8,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (0,2)*{\bullet}+(3,1)*{r};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy & \mbox{if } i = j, \\ & \\
    \xy 0;/r.18pc/:
  (-10,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (-10,-2)*{p_{i,r}(\lambda)};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 & \mbox{if } i \cdot j = 0, \\ & \\
    \xy 0;/r.18pc/:
  (-10,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (-10,-2)*{p_{i,r}(\lambda)};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 \;\; - \;\; (-t_{ij}^{-1}t_{ji})^r\;\;\;\;\xy 0;/r.18pc/:
  (-8,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (0,2)*{\bullet}+(3,1)*{r};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 & \mbox{if } i \cdot j = -1
 \end{cases}
 \\  \label{eq_powerslide2}
   \xy 0;/r.18pc/:
  (10,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (-14,-2)*{p_{i,r}(\lambda+\alpha_j)};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 & = &
 \begin{cases}
\xy 0;/r.18pc/:
  (14,6)*{\lambda};
  (0,0)*{\bbe{}};
  (0,-12)*{\scs j};
  (10,-2)*{p_{i,r}(\lambda)};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 \;\; + \;\; 2\;\;\xy 0;/r.18pc/:
  (10,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (0,2)*{\bullet}+(3,1)*{r};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy & \mbox{if } i = j, \\ & \\
\xy 0;/r.18pc/:
  (14,6)*{\lambda};
  (0,0)*{\bbe{}};
  (0,-12)*{\scs j};
  (10,-2)*{p_{i,r}(\lambda)};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 \;\; + \;\; (-t_{ij}^{-1}t_{ji})^r\;\;\xy 0;/r.18pc/:
  (10,6)*{\lambda};
  (0,0)*{\bbe{}};
  (2,-7)*{\scs j};
  (0,2)*{\bullet}+(3,1)*{r};
  (0,6)*{ }+(7,-1)*{\scs  };
 \endxy
 & \mbox{if } i \cdot j = -1
 \end{cases}
\end{eqnarray}
\end{exercise}




\subsection{$\Kar$, $K_0$ and $\Tr$ for 2-categories} \label{sec_traceK0-2cats}



We can extend many of the constructions from section \ref{sec_trace_lincat} defined for (additive) linear categories to the 2-categorical setting.  A 2-category $\CC$ is linear if the categories $\CC(x,y)$ are linear for all $x,y\in \Ob(\CC)$ and the composition functor preserves the linear structure (see \cite{Bor} for more details).  Similarly, an additive linear 2-category is a linear 2-category in which the categories $\CC(x,y)$ are also additive and composition is given by an additive functor.

The following definitions extend the Karoubi envelope, split Grothendieck group, and trace to the 2-categorical setting.
\begin{itemize}
\item Given an additive linear 2-category $\CC$, define the split Grothendieck group $K_0(\CC)$ of $\CC$ to be the linear category with $\Ob(K_0(\CC)) = \Ob(\CC)$ and with $K_0(\CC)(x,y) := K_0(\CC(x,y))$
for any two objects $x,y \in \Ob(\CC)$.  For $[f]_{\cong} \in
\Ob(K_0(\CC)(x,y))$ and $[g]_{\cong} \in \Ob(K_0(\CC)(y,z)) $ the
composition in $K_0(\CC)$ is defined by $[g]_{\cong} \circ [f]_{\cong}
:= [g \circ f]_{\cong}$.

\item The trace $\Tr(\CC)$ of a linear 2-category is the linear category with $\Ob(\Tr(\CC)) = \Ob(\CC)$ and with $\Tr(\CC)(x,y) := \Tr(\CC(x,y))$ for any two objects $x,y \in \Ob(\CC)$. For $\sigma \in \End_{\CC(x,y)}$ and
$\tau \in \End_{\CC(y,z)}$, we have
$[\tau ]\circ[\sigma ]=[\tau \circ\sigma ]$.
The identity morphism for $x\in \Ob(\TrCC)=\Ob(\CC)$ is given by
$[1_{I_x}]$.

\item The Karoubi envelope $\Kar(\CC)$ of a linear 2-category $\CC$ is the linear 2-category with $\Ob(\Kar(\CC)) = \Ob(\CC)$ and with hom categories $\Kar(\CC)(x,y) := \Kar(\CC(x,y))$.  The composition functor
$\Kar(\CC)(y,z) \times \Kar(\CC)(x,y) \to \Kar(\CC)(x,z)$ is induced
by the universal property of the Karoubi envelope from the composition
functor in $\CC$.  The fully-faithful additive functors $\CC(x,y) \to
\Kar(\CC(x,y))$ combine to form an additive $2$-functor $\CC \to
\Kar(\CC)$ that is universal with respect to splitting idempotents in
the  Hom-categories $\CC(x,y)$.
\end{itemize}














For categorification using $K_0$ it is necessary to consider the 2-category $\Kar(\Ucat(\mf{sl}_n))$.
We will denote by $\Udot$ the Karoubi envelope of $\U$.

The homomorphisms $h_{\CC(x,y)}$ taken over all objects $x,y \in \Ob(\CC)$ give rise to a linear functor
\begin{equation} \label{eq_chernchar}
h_{\CC} \col \K_0(\CC) \to \Tr(\CC)
\end{equation}
which is the identity map on objects and sends $K_0(\CC)(x,y) \to \Tr(\CC)(x,y)$ via the homomorphism $h_{\CC(x,y)}$.  It is easy to see that this assignment preserves composition since
\begin{align}
  h_{\CC}([g]_{\cong} \circ [f]_{\cong}) = h_{\CC}([g \circ f]_{\cong}) = [1_{g \circ f}]
   = [1_g \circ 1_f] = [1_g] \circ [1_f] = h_{\CC}([g]_{\cong}) \circ h_{\CC}([f]_{\cong}).
\end{align}

In the following sections we study the trace and $K_0$ for the 2-categories $\UcatD(\mf{sl}_n)$.







\subsection{Two categorifications of Lusztig's integral form $\UA(\mathfrak{sl}_2)$}


Here we present the results of \cite{Lau1,KLMS} computing $K_0$ and
of \cite{BHLZ} computing $\Tr$ of $\Ucat(\mf{sl}_2)$.

The algebra $\UA(\mf{sl}_2)$ has a well-known basis, called
Lusztig's canonical basis $\Bbb B$ consisting of
\begin{enumerate}[(i)]
     \item $E^{(a)}F^{(b)}1_{n} \quad $ for $a,b\geq 0$,
     $n\in\Z$, $n\leq b-a$,
     \item $F^{(b)}E^{(a)}1_{n} \quad$ for $a$,$b\geq 0$, $n\in\Z$,
     $n\geq
     b-a$,
\end{enumerate}
where $E^{(a)}F^{(b)}1_{b-a}=F^{(b)}E^{(a)}1_{b-a}$.
Let $_m\Bbb B_n$ be set of elements in $\Bbb B$ belonging to $1_m(\UA)1_n$.

















We associate to
 each $x \in \Bbb B$  a $1$-morphism in $\UcatD$ as follows:
\begin{equation} \label{eq_basis}
  x \mapsto \cal{E}(x) := \left\{
\begin{array}{cl}
  \cal{E}^{(a)}\cal{F}^{(b)}\onen & \text{if $x=E^{(a)}F^{(b)}1_n$,} \nn \\
  \cal{F}^{(b)}\cal{E}^{(a)}\onen & \text{if $x=F^{(b)}E^{(a)}1_n$.} \nn
\end{array}
  \right.
\end{equation}
Let $\B=\{\E(x)\mid x\in\Bbb B\}$
and $_m\B_n =\{\E(x)\mid x\in\, _m{\Bbb B_n}\}$.


The first categorification of $\UA$ was given in \cite{Lau1} where the decategorification functor is given by $K_0$.  The original proof worked with the 2-category $\UcatD(\mf{sl}_2)$ defined over a field $\k$, so that spaces of 2-morphisms formed vector spaces and the Krull-Schmidt property could be utilized.  In rank one the choice of scalars $Q$ does not enter the definition.  Later this result was enhanced in \cite{KLMS} to prove the result when working over the integers.   Unique decomposition for spaces of 2-morphisms follows as a corollary of these results, implying that the category $\U_{\Z}(\mf{sl}_2)$ is Krull-Schmidt. Very recently, it was shown in \cite{BHLZ} that $\Udot_\Z$ also categorifies $\UA$ via the alternative trace decategorification functor $\Tr$.

\begin{thm}\label{K0}
(\cite{KLMS}, \cite{BHLZ}) For ${\fsl}_2$,
$\B$ is the strongly upper triangular basis of $\Udot_\Z$.
The maps
\[ \begin{array}{rrr}
\gamma\maps  \UA & \longrightarrow& K_0(\UcatD_\Z)
\\
   x & \mapsto & [\cal{E}(x)]_{\cong} \end{array}\quad{\text{and}}\quad
\begin{array}{rrr}
  h_{\Udot_\Z}\maps K_0(\Udot_\Z)&\longrightarrow& \Tr(\U_\Z)\\
 x &\mapsto & [1_x] \\
\end{array}\]
are isomorphisms of graded linear categories, providing two categorifications of $\UA$.
\end{thm}






\subsubsection{Strategy of the Proof}



In section 6 of \cite{BHLZ}, based on the results of  \cite{KLMS} we give an
explicit presentation of the subcategory $\Udot(n,m)_\Z|_{_m\B_n}$
by generators and relations, which shows that this category is strongly upper triangular.
Hence, the indecomposable 1-morphisms from $\B$ generates $K_0$ and, by Proposition \ref{r24}, also $\Tr$ as $\Z[q,q^{-1}]$-modules. In \cite{KLMS} explicit isomorphisms in $\Udot_\Z$ are given lifting the
the defining relations of $\UA$, showing that $\gamma$ is an isomorphism of graded categories. Since the functor $h_{\Udot}: K_0(\Udot_\Z) \to \Tr(\Udot_\Z)$ preserves composition.
Finally, we use that $\Tr(\Udot)=\Tr(\U)$, the result follows.







\subsection{Two categorifications of $\UA ({\mathfrak sl}_n)$}


Here we present the results of  \cite{KL3} computing $K_0$ and
of \cite{BGHL} computing $\Tr$ for general $n$.

There is a special choice of scalars, where all $t_{i\, j}=1$  for $1\leq i< n-1$.  In this case, the graphical calculus is cyclic with respect to the biadjoint structure, so that isotopic diagrams represent the same 2-morphism.   This will be our default choice of $Q$ in sections unless explicitly stated otherwise. We will omit explicitly mentioning $Q$ in the notation when no confusion is likely to arise.




Theorem \ref{K0} was possible because the explicit isomorphisms constructed in \cite{KLMS} provide decompositions of arbitrary 1-morphisms into indecomposables.   However, the lack of an explicit description of the canonical basis for $\UA$ beyond $\mf{sl}_2$ presents an obstacle to generalizing this result beyond $\mf{sl}_2$.   However, if one works with the 2-category $\Ucat(\mf{sl}_n)$ defined over a field $\k$ of characteristic 0, then one can utilize various connections between this category and known geometric constructions to prove the following result.


\begin{thm}\label{K0n}
(\cite{KL3}, \cite{BGHL}) Let $\k$ be a field of characteristic $0$.
For ${\mathfrak {sl}}_n$,
the 2-category $\Udot$
is strongly upper triangular (see Remark~\ref{rem-overk}).
Moreover,
$$K_0(\Udot)=\UA$$
as graded linear categories and
$$\Tr(\U)=K_0(\Udot)\otimes_\Z \k, \quad
\HH_i(\U)=0 \quad{\text {for}}\quad i>0.$$
\end{thm}



Following a recommendation
of the first author, the $\fsl_3$ case of this theorem was studied in
\cite{Marko}.





\subsubsection{Strategy of the Proof}


Let us make few remarks about the proof.
The result about $K_0$ was proved in \cite{KL3}. It relies on the fact that
$\Udot$ is Krull-Schmidt.  To control the size of $K_0$ an action of $\Udot$ was defined on the cohomology rings of partial flag varieties.
Even when for $n>2$, the explicit form of the Lusztig canonical basis is not known,
but the results of \cite{VV} and \cite{Web4} allows us to deduce that
$\Udot$ is strongly upper triangular.
The full argumentation will be given in \cite{BGHL}.





\subsubsection{Applications}




In \cite{LQR,QR} it was shown that $\mf{sl}_n$ link homology theories can be obtained
from $\Udot(\fsl_m)$ by means of the so-called foamation functors $F$, first studied in \cite{MackFoam}.
More precisely, there is an extended version $2{\rm BFoam}$ of the Bar-Natan foam category introduced by Blanchet~\cite{Blan}.   (The advantage of Blanchet's version is that it
is functorial with respect to link cobordisms, when Bar-Natan version is functorial up to sign.)
In \cite{LQR,QR} an analog $n{\rm BFoam}$ of the Blanchet foam category for $\mf{sl}_2$ is defined for $\mf{sl}_n$ and families of 2-representations $F$ for were defined from $\Udot(\fsl_m)$ into the foam categories $n{\rm BFoam}$.


A general procedure was laid out by Cautis ~\cite{Cautis-clasp} using categorical skew Howe duality to pull back complexes associated to a tangle to a complex in $\Kom(\Udot)$.  Combining this with the foamation functors allows one to pull back the complexes of foams associated to a tangle to a complex in $\Kom(\Udot)$.   It was shown that all of the foam relations used for $\mf{sl}_n$-link homology arise from relations in $\Udot(\fsl_m)$ via foamation functors.  These foamation functors categorify a skew Howe functor defined at the decategorified level by Cautis, Kamnitzer, and Morrison that realize web relations from relations in the quantum group $\dot{\mathbf{U}}_q(\mf{sl}_m)$~\cite{CKM}.



Recall that we have two flavors of Euler characteristic associated with $K_0$ and $\Tr$,
\begin{eqnarray*}
\chi_{\tr}: &\Kom(F(\U)) \to \Tr(F(\U))\\
\chi: &\Kom(F(\Udot)) \to K_0(F(\Udot))  .
\end{eqnarray*}
Below is one of the applications of Theorem \ref{K0n}.

\begin{cor}\label{chi}
In $\mf{sl}_n$ link homologies theories, we have
$$\chi_{tr}=\chi\, .$$
\end{cor}


\begin{remark}
The $\mf{sl}_2$ case of  Corollary \ref{chi} was first proven  by Cooper-Krushkal~\cite[Section 3]{CK2}.
\end{remark}


\begin{proof}

Let $\C:=F(\Udot(\fsl_m))$. We have the Chern character map
$h_\C: K_0(\C) \to \Tr(\C)$ sending $[x]_{\cong} \to [1_x]$. The induced  map $\chi \to \chi_{\tr}$ is surjective,
since $\chi_{\tr}$ uses trace classes of the identity maps only.
It remains to show that this map is injective.
Note that $K_0(\Udot)$ is freely generated by indecomposables and $h_{\Udot}$ is an isomorphism after tensoring with any field of zero characteristic by Theorem \ref{K0n}, so
 $h_{\Udot}$ is injective. Hence, $F(K_0(\Udot))=F(h_{\Udot}(K_0(\Udot)))$. The fact that any linear functor commutes with $K_0$ implies the result.
\end{proof}
