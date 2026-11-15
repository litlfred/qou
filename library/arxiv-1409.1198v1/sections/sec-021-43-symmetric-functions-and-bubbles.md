---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-021-43-symmetric-functions-and-bubbles
section_title: "Symmetric functions and bubbles"
section_number: 4.3
pages: 27-29
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.681
latex_coverage_ratio: 0.915
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
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
