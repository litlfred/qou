---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-027-6-action-on-center-of-objects-in
section_title: "Action on center of objects in"
section_number: 6
pages: 43-45
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.946
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
\label{action}



This section is devoted to the proof of Theorem \ref{2-reps}. The action of the current algebra on the trace of any 2-representation follows
directly from the functotiality of the trace. The rest of the section establishes the action on the center.




\subsubsection{Centers of categories}




The center $Z(\C)$ of an additive category $\C$ is the endomorphism ring of the identity functor $\Id_{\C}$ on $\C$.  Note that an endomorphism of $\Id_{\C}$ is a natural transformation $\alpha \maps \Id_{\C} \To \Id_{\C}$.  Such a natural transformation consists of a map $\alpha_x \maps x \to x$ for each object $x$ of $\C$ satisfying the requirement that for any map $f \maps x \to y$ in $\C$, we get a commutative square
\[
 \xymatrix{
 x \ar[r]^{f} \ar[d]_{\alpha_x} & y \ar[d]^{\alpha_y} \\ x \ar[r]_{f} & y
 }
\]
\begin{exercise}
Show that $Z(\C)$ is commutative ring. Hint: use the Eckmann--Hilton argument.
\end{exercise}

An additive category is an object of the linear 2-category \cat{AdCat} of additive categories, additive functors, and natural transformations.  For an arbitrary, linear 2-category $\CC$ we define the center $Z(x)$ of an object $x \in \Ob( \CC)$ as the ring of endomorphisms $\CC(1_{x}, 1_{x})$, see \cite{GK}.  Define the {\em center of objects} of the 2-category $\CC$ as the $Z(\CC) = \bigoplus_{x \in \Ob(\CC)} Z(x)$.


The relationship between Hochschild homology and cohomology described in section~\ref{subsec_HHco} can now be recast in a more general framework.

\begin{exercise}
Let $\CC$ be a linear 2-category $\CC$. Show that for each $x \in \Ob(\CC)$, the abelian group $\Tr(\CC(x,x))$ is a module over the ring $Z(x)$.
\end{exercise}





\begin{example} \label{examp_sl2}
In the 2-category $\Ucat(\mf{sl}_2)$, an element in the center $Z(\lambda)$ for an object $\lambda \in \Ob(\Ucat(\mf{sl}_2))$ is given by any closed diagram in the graphical calculus.  It was shown in Section 8 of \cite{Lau1} that any such closed diagram can be reduced to a product of non-nested dotted bubbles with the same orientation.  As explained in section~\ref{sec_sym-bub}, this provides an isomorphism between $Z(\lambda)$ and the ring $\sym$ of symmetric functions.
\end{example}


Given a 2-endomorphism $f \maps \onelp x \onel \To \onelp x \onel$ in $\Ucat^{\ast}(\mf{sl}_n)$, we can interpret the class $[f]$ as a diagram on the annulus.  If we forget that the diagram is on an annulus, we are left with a diagram representing an endomorphism of $\onelp$.
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
 \endxy} \;\; \in \Tr(\Ucat^{\ast})
 \qquad \rightsquigarrow \qquad
 \vcenter{ \xy 0;/r.18pc/:
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
 \endxy} \;\; \in Z(\lambda')
\]
By choosing scalars $t_ij=t_{ji}=1$ for all $i\neq j$, the 2-category $\Ucat(\mf{sl}_n))=\Ucat_Q(\mf{sl}_n))$ is cyclic and the resulting diagram is independent of the choice of representative for the class $[f] \in \Tr(\Ucat(\mf{sl}_n))$.
In this way, $[f]$ gives rise to a map $Z(\lambda) \to Z(\lambda')$ given by placing an element from $Z(\lambda)$ inside the annulus and regarding the result as an element in $Z(\lambda')$.  Hence, we have the following proposition.


\begin{prop} \label{thm_center-action}
The linear category $\Tr(\Ucat^{\ast}(\mf{sl}_n))$ acts by endomorphisms on the commutative ring
$Z\left(\Ucat^{\ast}(\mf{sl}_n) \right)$.  Under this action the class $[f]$ of endomorphisms $f \maps \onelp x \onel \To \onelp x \onel$ in $\Ucat^{\ast}(\mf{sl}_n)$ is sent to the linear operator sending a closed diagram $D$ representing an element of $Z(\lambda)$ to the element in $Z(\lambda')$ obtained by removing the annulus from the diagram $[f.D]$.
\end{prop}
\vspace*{3mm}

\noindent
{\bf Remark for experts}.
Being able to define an action of the trace on the center of objects in a 2-category essentially amounts to having enough ``coherent" duality in the 2-category so that the trace takes
values in the center of objects.  This idea is captured by the notion of a pivotal 2-category~\cite{Muger}.  This can be seen as a many object version of a pivotal monoidal category, see \cite{GMV} where
traces in this context are studied.  M\"{u}ger points out in \cite[page 11]{Muger} a strict pivotal 2-category can be defined from Mackaay's work~\cite{MackSphere} on spherical
2-categories by ignoring the monoidal structure.  It is also equivalent to a 2-category in which  every 1-morphism has a specified cyclic biadjoint (see \cite{CKS,Lau1}).





\subsubsection{A current algebra action on centers}



In what follows we represent a generic 2-morphism $f \in Z(\lambda)$, $f \maps
\onel \To \onel$, by the diagram
\[






 \xy
  (0,0)*{*};(0,-4)*{};
  (8,6)*{\lambda};
 \endxy
\]
where we use the $*$ to represent any linear combination of closed diagrams
describing $f$.


\begin{thm} \label{thm_main}
The vector space
\begin{equation}
 Z := \bigoplus_{\lambda \in \UcatD} Z(\lambda)
\end{equation}
is a $\bfU(\fsl_n[t])$-module with
\begin{eqnarray}
  1_{\lambda} \maps Z &\lra & Z(\lambda ) \\
 \xy
  (0,0)*{\ast};
  (8,6)*{\lambda'};
 \endxy & \mapsto &
  \delta_{\lambda,\lambda'} \left(\;\;   \xy
  (0,0)*{\ast};
  (8,6)*{\lambda};
 \endxy\;\;\;\right)
   \nn\\
  x^+_{i,r}  \maps Z(\lambda) &\lra & Z(\lambda+\alpha_i) \\
 \xy
  
  (0,0)*{\ast};
  (8,6)*{\lambda};
 \endxy
& \mapsto & (-1)^{(i+1)r}\;\;
  \xy
(0,0)*{\lcbub{i}};
  (-8,-8)*{\bullet}+(-3,-2)*{r};
  (0,0)*{\ast};
  (4,6)*{\lambda};
  (22,6)*{\lambda+\alpha_i};
 \endxy\;\;
   \nn\\
 x^-_{i,s} \maps Z(\lambda) &\lra & Z(\lambda-\alpha_i) \\
 \xy
  
  (0,0)*{\ast};
  (8,6)*{\lambda};
 \endxy
& \mapsto & (-1)^{(i+1)s} \;\;
 \xy
(0,0)*{\lccbub{i}};
(-8,-8)*{\bullet}+(-3,-2)*{s};
  
  (0,0)*{\ast};
  (4,6)*{\lambda};
  (22,6)*{\lambda-\alpha_i};
 \endxy
 \nn \\
   \xi_{i,r} \maps Z(\lambda)& \lra & Z(\lambda)  \\
   \xy
  (0,0)*{\ast};
  (8,6)*{\lambda};
 \endxy & \mapsto & (-1)^{(i+1)r}
     \xy
     (0,-6)*{};
  (-9,0)*{p_{i,r}(\lambda)};
  (0,0)*{\ast};
  (8,6)*{\lambda};
 \endxy
\end{eqnarray}

\end{thm}


\begin{proof}
This theorem follows immediately from Proposition ~\ref{prop-cur}.
In particular, the fact that the current algebra relations hold in the trace $\Tr(\Ucat^\ast(\mf{sl}_n))$ imply that these relations hold under the action described above.
\end{proof}





\subsubsection{An action of the current algebra on centers of 2-representations}




\begin{defn}
A 2-representation of $\UcatD_Q(\mf{sl}_n)$ is a graded additive $\Bbbk$-linear 2-functor $\Psi \maps \UcatD_Q(\mf{sl}_n)\to \cal{K}$ for some graded, additive 2-category $\cal{K}$.
\end{defn}

When all of the Hom categories $\cal{K}(x,y)$ between objects $x$ and $y$ of $\cal{K}$ are idempotent complete, in other words
$\Kar(\cal{K}) \cong \cal{K}$, then any graded additive $\Bbbk$-linear 2-functor $\Ucat_{Q}(\mf{sl}_n) \to \cal{K}$ extends uniquely to a 2-representation of $\UcatD_Q(\mf{sl}_n)$.

Any 2-representation $\Psi$ induces a map on traces
\begin{align}
\Tr(\UcatD_Q(\mf{sl}_n)) &\to \Tr(\cal{K}) \\ \nn
[f] & \mapsto [\Psi(f)].
\end{align}
When looking at $\U^\ast$ as
\[
\Ucat^{\ast}(x,y) := \bigoplus_{t \in \Z} \Ucat(x, y \la t\ra),
\]
we can easily extend this map to
\begin{align*}
\Tr(\U^\ast(\mf{sl}_n)) &\to \Tr(\cal{K}).
\end{align*}

Hence by the same procedure described in Proposition~\ref{thm_center-action}, the trace $\Tr(\U^\ast(\mf{sl}_n))$ acts on the center $Z(\cal{K})$ of any 2-representation.  Since
Proposition~\ref{prop-cur} shows that the current algebra is contained in the trace, it follows that the current algebra acts on any 2-representation.
