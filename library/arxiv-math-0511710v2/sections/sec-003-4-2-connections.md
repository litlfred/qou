---
doc_id: arxiv-math-0511710v2
doc_title: "Higher gauge theory"
section_id: sec-003-4-2-connections
section_title: "2-Connections"
section_number: 4
pages: 19-27
source_pdf: 0511710v2.pdf
source_sha256: f88f50d459080490
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.943
doc_brief: "Higher gauge theory — Just as gauge theory describes the parallel transport of point particles using connections on bundles, higher gauge theory describes the parallel transport of 1-dimensional"
---
\label{section: 2-Connections}

For a trivial bundle, 
the holonomy of a connection assigns elements of the structure
group to paths in space.  Similarly, a 2-connection
assigns objects and morphisms of the structure 2-group to 
paths and surfaces in space.  To make this precise we need 
the notion of a `path 2-groupoid'.  

We described the path groupoid of a smooth space $M$
in Example \ref{2space.3}.  This has points of $M$ as
objects:
\[    \bullet \, {\textstyle{\small{\textit{x}}}}  \]
and thin homotopy classes of paths in $M$ as morphisms:
\[
\xymatrix{
 {\textstyle{\small{\textit{x}}}}  \,
   \bullet \ar@/^1pc/[rr]^{\gamma}
&& \bullet \, {\textstyle{\small{\textit{y}}}}   
}
\]
The path 2-groupoid also has 2-morphisms, which are
thin homotopy classes of 2-dimensional surfaces like this: 
\[
\xymatrix{
 {\textstyle{\small{\textit{x}}}} \, 
   \bullet \ar@/^1pc/[rr]^{\gamma_1}_{}="0"
           \ar@/_1pc/[rr]_{\gamma_2}^{}="1"
&& \bullet \, {\textstyle{\small{\textit{y}}}}   
\ar@{=>}"0";"1"^{\Sigma}
}
\]
We call these `bigons':

\begin{definition} \et 
\label{parametrized bigon}
  Given a smooth space $M$, a {\bf parametrized bigon} in $M$
  is a smooth map
  \[
    \Sigma \maps [0,1]^2 \to M
  \]
  which is constant near $s = 0$, constant near $s = 1$, 
  independent of $t$ near $t = 0$, and independent of $t$ near $t = 1$.
  We call $\Sigma\of{\cdot,0}$ the {\bf source} of the 
  parametrized bigon $\Sigma$, and $\Sigma\of{\cdot,1}$ the 
  {\bf target}.  If $\Sigma$ is a parametrized bigon with
  source $\gamma_1$ and target $\gamma_2$, we write $\Sigma \maps
  \gamma_1 \to \gamma_2$.   
\end{definition}

\begin{definition} \et
\label{bigon}
Suppose $\Sigma \maps \gamma_1 \to \gamma_2$ and
$\Sigma' \maps \gamma'_1 \to \gamma'_2$ are parametrized
bigons in a smooth space $M$.  A {\bf thin homotopy} between
$\Sigma$ and $\Sigma'$ is a smooth map 
\[
  H \maps [0,1]^3 \to M
\]
with the following properties:
\begin{itemize}

\item 
$H\of{s,t,0} = \Sigma\of{s,t}$ and $H\of{s,t,1} = \Sigma'\of{s,t}$,

\item 
$H\of{s,t,u}$ is independent of $u$ near $u = 0$ and near $u = 1$,

\item 
For some thin homotopy $F_1$ from $\gamma_1$ to $\gamma_1'$,
$H\of{s,t,u} = F_1\of{s,u}$ for $t$ near $0$, and
for some thin homotopy $F_2$ from $\gamma_2$ to $\gamma_2'$, 
$H\of{s,t,u} = F_2\of{s,u}$ for $t$ near $1$,

\item 
$H(s,t,u)$ is constant for $s = 0$ and near $s = 1$,

\item 
$H$ does not sweep out any volume: the rank of the
differential $dH(s,t,u)$ is $< 3$ for all $s,t,u \in [0,1]$.

\end{itemize}

\noindent
We say two parametrized bigons $\Sigma,\Sigma'$
lie in the same {\bf thin homotopy class}
if the pair $(\Sigma, \Sigma')$ lies in the closure of the 
thin homotopy equivalence relation.  
A {\bf bigon} is a thin homotopy class $[\Sigma]$ of parametrized bigons.
\end{definition}

\begin{definition} \et
\label{2-groupoid of bigons}
  The {\bf path 2-groupoid} 
  $\P_2\of{M}$
  of a smooth space $M$ is the 2-category in which:
  \begin{itemize}
    \item 
      objects are points $x \in M$:
      \[   \bullet \, {\textstyle{\small{\textit{x}}}}  
      \] 
    \item 
      morphisms are thin homotopy classes of paths $\gamma$ in
      $M$ that are constant near $s = 0$ and $s = 1$: 
     \[
      \xymatrix{
       x \ar@/^1pc/[rr]^{[\gamma]} 
       && y 
      }
      \]
    \item
      2-morphisms are bigons in $M$
 \[
\xymatrix{
   x \ar@/^1pc/[rr]^{[\gamma_1]}_{}="0"
           \ar@/_1pc/[rr]_{[\gamma_2]}_{}="1"
           \ar@{=>}"0";"1"^{{}_{[\Sigma]}}
&& y
}
\]
  \end{itemize}
and whose composition operations are defined as:
\begin{itemize}

\item   \hskip 3em
$
\xymatrix{
   x \ar@/^1pc/[rr]^{[\gamma_1]}
&& y \ar@/^1pc/[rr]^{[\gamma_2]}
&& z
}
  =
\xymatrix{
   x \ar@/^1pc/[rr]^{[\gamma_1 \circ \gamma_2]}
&& z 
}
$ 
\hfill\break
\vskip 1em \noindent
where
 \[ 
    \left(\gamma_1\circ \gamma_2\right)\of{s}
    :=
    \left\lbrace
      \begin{array}{cl}
         \gamma_1\of{2s} & \mbox{for $0 \leq s \leq 1/2$}\\
         \gamma_2\of{2s-1} & \mbox{for $1/2\leq s \leq 1$}
      \end{array}
      \right.
\]

\item \hskip 3em
$
\xymatrix{
   x \ar@/^2pc/[rr]^{[\gamma_1]}_{}="0"
           \ar[rr]^<<<<<<{[\gamma_2]}_{}="1"
           \ar@{=>}"0";"1"^{[\Sigma_1]}
           \ar@/_2pc/[rr]_{[\gamma_3]}_{}="2"
           \ar@{=>}"1";"2"^{[\Sigma_2]}
&& y
}
=
\xymatrix{
   x \ar@/^1pc/[rr]^{[\gamma_1]}_{}="0"
           \ar@/_1pc/[rr]_{[\gamma_3]}_{}="1"
           \ar@{=>}"0";"1"^{{}_{[\Sigma_1 \Sigma_2]}}
&& y
}
$
\hfill\break
\vskip 1em \noindent
where
\[
    \left(\Sigma_1\Sigma_2\right)\of{s,t}
    :=
    \left\lbrace
      \begin{array}{cl}
         \Sigma_1\of{s,2t} & \mbox{for $0 \leq t \leq 1/2$}\\
         \Sigma_2\of{s,2t-1} & \mbox{for $1/2\leq t \leq 1$}
      \end{array}
     \right.
\]
    
\item  \hskip 3em
$
\xymatrix{
   x \ar@/^1pc/[rr]^{[\gamma_1]}_{}="0"
           \ar@/_1pc/[rr]_{\gamma_1^\prime}_{}="1"
           \ar@{=>}"0";"1"^{[\Sigma_1]}
&& y \ar@/^1pc/[rr]^{[\gamma_2]}_{}="2"
           \ar@/_1pc/[rr]_{[\gamma_2^\prime]}_{}="3"
           \ar@{=>}"2";"3"^{[\Sigma_2]}
&& z
}
 =
\xymatrix{
   x \ar@/^1pc/[rr]^{[\gamma_1 \circ \gamma_2]}_{}="0"
           \ar@/_1pc/[rr]_{[\gamma_1^\prime\circ\gamma_2^\prime]}_{}="1"
           \ar@{=>}"0";"1"^{{}_{[\Sigma_1 \circ\Sigma_2]}}
&& z 
}
$
\hfill\break
\vskip 1em \noindent
where
\[
    \left(\Sigma_1\circ\Sigma_2\right)\of{s,t}
    :=
    \left\lbrace
      \begin{array}{cl}
         \Sigma_1\of{2s,t} & \mbox{for $0 \leq s \leq 1/2$}\\
         \Sigma_2\of{2s-1,t} & \mbox{for $1/2\leq s \leq 1$}
      \end{array}
    \right.  
\]

  \end{itemize}
\end{definition}

\noindent
One can check that these operations are well-defined, where
for vertical composition we must choose suitable representatives 
of the bigons being composed.  One can also check that
$\P_2(M)$ is indeed a 2-category.  Furthermore, 
the objects, morphisms and 2-morphisms in $\P_2(M)$ all form 
smooth spaces, by an elaboration of the ideas
in Example \ref{2space.3}, and all the 2-category operations are then 
smooth maps.   We thus say $\P_2(M)$ is a {\bf smooth 2-category}:
that is, a 2-category in ${\rm C}^\infty$.  Indeed, the usual definitions 
\cite{KellyStreet} of 2-category, 2-functor, pseudonatural transformation, 
and modification can all be internalized in ${\rm C}^\infty$, and we 
use these `smooth' notions in what follows.
Furthermore, both morphisms and 2-morphisms in $\P_2(M)$ have strict 
inverses, and the operations of taking inverses are smooth, so we say
$\P_2(M)$ is a {\bf smooth 2-groupoid}. 

We obtain the notion of `2-connection' by categorifying
the concept of connection.  The following result 
suggests a strategy for doing this:

\begin{theorem} \et 
\label{central proposition concerning connections}
   For any smooth group $G$ and smooth space $B$, 
   suppose $E \to B$ is a principal $G$-bundle equipped with local
   trivializations over open sets $\{U_i\}_{i \in I}$ covering $B$.
   Let $g_{ij}$ be the transition functions.
   Then there is a one-to-one correspondence between connections on
   $E$ and data of the following sort:
\begin{itemize}
\item 
       for each $i \in I$ a smooth map between smooth 2-spaces:
\[
    \hol_i \maps \P_1\of{U_i} \to G
\]
 called the {\bf local holonomy functor},
 from the path groupoid of $U_i$ 
 to the group $G$ regarded as a smooth 2-space with a single
 object $\bullet$,
\end{itemize}
such that:
\begin{itemize} 
\item
  for each $i,j\in I$, the transition function $g_{ij}$
  defines a smooth natural isomorphism:
  \[
    \hol_i|_{U_{ij}} \stackto{g_{ij}} \hol_j|_{U_{ij}}
  \]
  called the {\bf transition natural isomorphism}.   
  In other words, this diagram commutes:
\begin{center}
\begin{picture}(100,100)
  \includegraphics{pathtransition.eps}
  \put(-60,90){$g_{ij}\of{x}$}
  \put(-60,-5){$g_{ij}\of{y}$}
  \put(-120,42){$\hol_i(\gamma)$}
  \put(0,42){$\hol_j(\gamma)$}
\end{picture}
\vskip 1em
\end{center}
\noindent
for any path $\gamma \maps x \to y$ in $U_{ij}$.
\end{itemize}
\end{theorem}

\Proof 
See Baez and Schreiber \cite{BaezSchreiber:2004}.
\endofproof

\noindent
In addition, it is worth noting that whenever we have a connection, 
for each $i,j,k \in I$ this triangle commutes:

\begin{center}
  \begin{picture}(70,75)
  \includegraphics{triangle_withoutdots.eps}
  \put(-78,40){$g_{ij}$}
  \put(-18,40){$g_{jk}$}
  \put(-50,-7){$g_{ik}$}
  \put(-97,-5){$\hol_i$}
  \put(-50,75){$\hol_j$}
  \put(0,-5){$\hol_k$}
  \end{picture}
\end{center}
\vskip 1em 

The idea behind the above result is that:

  \begin{itemize}
    \item
      The local holonomy functors $\hol_i$ are specified by
      1-forms 
      \[
        A_i \in \Omega^1\of{U_i,\g}\,.
      \]
    \item
      The transition natural isomorphisms $g_{ij}$ 
      are specified by smooth functions
      \[
        g_{ij} \maps U_{ij} \to G\,,
      \] 
      satisfying the equation
      \[
        A_i = g_{ij}A_j g_{ij}^{-1} + g_{ij} \extd g_{ij}^{-1}
      \]
      on $U_{ij}$.
   \item
    The commuting triangle for the triple intersection
    $U_{ijk}$ is equivalent to the equation
    \[
     g_{ij}g_{jk} = g_{ik} 
    \]
     on $U_{ijk}$.
  \end{itemize}

Categorifying all this, we make the following definition:

\begin{definition} \et
  \label{def: 2-connection on a 2-bundle}  
   For any smooth 2-group $\twogroup$, 
   suppose that $E \to B$ is a principal $\twogroup$-2-bundle equipped with 
   local trivializations over open sets $\{U_i\}_{i \in I}$ covering $B$, 
   and let the transition functions $g_{ij}$, 
   $h_{ijk}$ and $k_i$ be given as in Theorem
   \ref{2-bundle cocycle conditions}.  Suppose for simplicity that
   $k_i = 1$.  Then a {\bf 2-connection} on $E$
   consists of the following data:
   \begin{itemize}
\item
   for each $i \in I$ a smooth 2-functor
\begin{eqnarray*}
  \begin{array}{rcccc}
    \hol_i &\maps& \P_2\of{U_i} &\to& \twogroup
    \\
    &&
\xymatrix{
   x \ar@/^1pc/[rr]^{\gamma}="0"
           \ar@/_1pc/[rr]_{}_{\eta}="1"
           \ar@{=>}"0";"1"^{\Sigma}
&& y
}
&\mapsto& 
\xymatrix{
   \bullet \ar@/^1pc/[rr]^{\hol_i\of{\gamma}}="0"
           \ar@/_1pc/[rr]_{}_{\hol_i\of{\eta}}="1"
           \ar@{=>}"0";"1"^{\hol_i\of{\Sigma}}
&& \bullet
}
  \end{array}
\end{eqnarray*}
  called the {\bf local holonomy 2-functor},
  from the path 2-groupoid $\P_2\of{U_i}$ 
  to the 2-group $\twogroup$ regarded as a smooth 2-category with a single 
  object $\bullet$, 
\end{itemize}
such that:
\begin{itemize}
\item
  For each $i,j$ a pseudonatural isomorphism:
  \[
   g_{ij} \maps \hol_i|_{\P(U_i \cap U_j)}  \to
   \hol_j|_{\P(U_i \cap U_j)} 
  \]
  extending the transition function $g_{ij}$.
  In other words, for each path
  $\gamma \maps x \to y$ in $U_i \cap U_j$ a morphism in $\G$:
\vskip 0.5em
\begin{center}
\begin{picture}(100,100)
  \includegraphics{filled_square.eps}
  \put(-60,90){$g_{ij}\of{x}$}
  \put(-60,-8){$g_{ij}\of{y}$}
  \put(-120,42){$\hol_i(\gamma)$}
  \put(0,42){$\hol_j(\gamma)$}
  \put(-75,50){$g_{ij}\of{\gamma}$}
\end{picture}
\vskip 0.5em
\end{center}
\noindent
depending smoothly on $\gamma$, such that this diagram commutes:
\vskip 0.5em
\begin{eqnarray*}
\begin{picture}(240,140)
 \includegraphics{tincan.eps}
 \put(-3,-17){	
 \begin{picture}(0,0)
 \put(122,0){
  \begin{picture}(0,0)
   \put(-385,90){$\hol_i\of{\gamma}$}
   \put(-290,100){${}_{\hol_i\of{\eta}}$}
   \put(-333,100){$\hol_i\of{\Sigma}$}
   \put(-242,50){${}_{g_{ij}\of{\eta}}$}
   \put(-268,125){${g_{ij}\of{\gamma}}$}
   \put(-250,163){$g_{ij}\of{x}$}
   \put(-250,10){$g_{ij}\of{y}$}
  \end{picture}
 }
 \put(288,0){
  \begin{picture}(0,0)
   \put(-382,90){$\hol_j\of{\gamma}$}
   \put(-290,100){${}_{\hol_j\of{\eta}}$}
   \put(-333,100){$\hol_j\of{\Sigma}$}
  \end{picture}
 }
 \end{picture}
}
\end{picture}
\end{eqnarray*}
for any bigon $\Sigma \maps \gamma \To \eta$ in $U_{ij}$,
\item
  for each $i,j,k \in I$ the transition function
  $h_{ijk}$ defines a modification:
\begin{center}
 \begin{picture}(100,80)
  \includegraphics{triangle_filled_withoutdots.eps}
  \put(-95,0){$\hol_i$}
  \put(-48,75){$\hol_j$}
  \put(2,0){$\hol_k$}
  \put(-78,40){$g_{ij}$}
  \put(-17,40){$g_{jk}$}
  \put(-50,-7){$g_{ik}$}
  \put(-64,24){$h_{ijk}$}
  \end{picture}
  \vskip 1em
\end{center}
In other words, this diagram commutes:
\begin{center}
\begin{picture}(180,270)
\includegraphics{prism.eps}
  \put(-3,100){$\hol_k\of{\gamma}$}
  \put(-190,100){$\hol_i\of{\gamma}$}
  \put(-80,160){${}_{\hol_j\of{\gamma}}$}
  \put(-100,-7){$g_{ik}\of{y}$}
  \put(-100,187){$g_{ik}\of{x}$}
  \put(-138,43){${}_{g_{ij}\of{y}}$}
  \put(-138,237){${}_{g_{ij}\of{x}}$}
  \put(-47,43){${}_{g_{jk}\of{y}}$}
  \put(-47,237){${}_{g_{jk}\of{x}}$}
  \put(-95,16){${}_{h_{ijk}\of{y}}$}
  \put(-95,212){${}_{h_{ijk}\of{x}}$}
  \put(-100,90){$g_{ik}\of{\gamma}$}
  \put(-150,124){${}_{g_{ij}\of{\gamma}}$}
  \put(-50,117){${}_{g_{jk}\of{\gamma}}$}
\end{picture}
\end{center}
for any bigon $\Sigma \maps \gamma \To \eta$ in $U_{ijk}$.
\end{itemize}
\end{definition}

\noindent
In addition, it is worth noting that 
whenever we have a 2-connection, for each $i,j,k,l \in I$ 
this tetrahedron commutes:

\begin{eqnarray*}
\begin{picture}(140,140)
  \includegraphics{tetrahedron_withoutdots.eps}
  \put(-117,46){${}_{g_{ij}}$}
  \put(-50,46){${}_{g_{jk}}$}
  \put(-90,-7){$g_{ik}$}
  \put(-130,80){$g_{il}$}
  \put(-37,80){$g_{kl}$}
  \put(-78,101){${}_{g_{jl}}$}
  \put(-170,-3){$\hol_i$}
  \put(3,-3){$\hol_k$}
  \put(-85,62){${}_{\hol_j}$}
  \put(-85,145){${}_{\hol_l}$}

  \put(-100,14){${}^{h_{ijk}}$}
  \put(-70,30){$h_{ikl}$}
  \put(-68,85){${}_{h_{jkl}}$}
  \put(-110,80){${}_{h_{ijl}}$}
\end{picture}
\end{eqnarray*}

\vskip 1 em
In analogy to the situation for ordinary connections on bundles, one
would like to obtain 2-connections from Lie-algebra-valued
differential forms.  This is our next result.  In what follows,
$(G,H,t,\alpha)$ will be the smooth crossed module corresponding to
the smooth 2-group $\twogroup$.  We think of the transition function
$g_{ij}$ as taking values in $\Ob(\twogroup) = G$, and think of
$h_{ijk}$ as taking values in $H$.  Actually $h_{ijk}$ takes values in
$\Mor(\twogroup) \iso G \semidir H$, but its $G$ component is determined
by its source, so only its $H$ component is interesting.  In these
terms, the fact that
\[    h_{ijk}(x) \maps g_{ij}(x) g_{jk}(x) \stackto{\sim} g_{ik}(x)  \]
translates into the equation
\[  g_{ij}(x) \, g_{jk}(x) \, t(h_{ijk}) = g_{ik}(x)  ,\]
and the associative law of Theorem \ref{2-bundle cocycle conditions}
(i.e.\ the above tetrahedron) becomes a cocycle 
condition familiar from the theory of nonabelian gerbes:
\[
  h_{ijk} \, h_{ikl} 
 = 
  \alpha(g_{ij})(h_{jkl}) \, h_{ijl} 
 \,.
\]

\begin{theorem} \et
\label{central proposition concerning 2-connections}
   For any smooth 2-group $\twogroup$ and smooth space $B$,
   suppose that $E \to B$ is a principal $\twogroup$-2-bundle equipped with 
   local trivializations over open sets $\{U_i\}_{i \in I}$ covering $B$, 
   with the transition functions $g_{ij}$, $h_{ijk}$ and 
   $k_i$ given as in Theorem \ref{2-bundle cocycle conditions}.   
   Suppose for simplicity that $k_i = 1$.  
   Let $(G,H,t,\alpha)$ be the smooth crossed module corresponding to
   $\twogroup$, and let $(\g,\h,dt,d\alpha)$ be the corresponding 
   differential crossed module.
   Then there is a one-to-one correspondence between 
   2-connections on $E$ and Lie-algebra-valued 
   differential forms $(A_i,B_i,a_{ij})$ satisfying certain 
   equations, as follows:

\begin{itemize}

\item
  The local holonomy 2-functor $\hol_i$ is specified by 
  differential forms
  \begin{eqnarray*}
     A_i \in \Omega^1\of{U_i,\g}
     \\
     B_i \in \Omega^2\of{U_i,\h}
  \end{eqnarray*}
  satisfying
  \[
    F_{A_i} + dt\of{B_i} = 0
    \,,
  \]
  where $F_{A_i} = \extd A_i + A_i \wedge A_i$ 
  is the curvature 2-form of $A_i$.

 \item
   The transition pseudonatural isomorphism  
  $\hol_i \stackto{g_{ij}} \hol_j$
  is specified by the transition functions $g_{ij}$ together
  with differential forms
   \begin{eqnarray*}
     a_{ij} &\in& \Omega^1\of{U_{ij}, \h}
   \end{eqnarray*}
   satisfying the equations:
  \begin{eqnarray*}
    A_i &=& g_{ij}A_jg_{ij}^{-1} + g_{ij} \extd g_{ij}^{-1} - dt(a_{ij})
    \nonumber\\
    B_i &=& \alpha\of{g_{ij}}\of{B_j} + k_{ij}
  \end{eqnarray*}
  on $U_{ij}$,
  where
  \[
    k_{ij} = \extd a_{ij} + a_{ij}\wedge a_{ij} + d\alpha\of{A_i}\wedge a_{ij}
    \,.
  \]

 \item
  The modification 
  $g_{ij}\circ g_{jk} \stackto{h_{ijk}} g_{ik}$ 
  is specified by the transition functions $h_{ijk}$.  
  For this, the differential forms $a_{ij}$ are
  required to satisfy the equation:
  \[
  a_{ij} + \alpha(g_{ij}) a_{jk} = 
  h_{ijk} a_{ik} h_{ijk}^{-1} + (\extd h_{ijk})  h_{ijk}^{-1} + 
  d\alpha(A_i)(h_{ijk}) \, h_{ijk}^{-1} 
   \]
on $U_{ijk}$.

\end{itemize}
\end{theorem}

\Proof 
See Baez and Schreiber \cite{BaezSchreiber:2004}.
The `vanishing fake curvature' condition $F_{A_i} + dt\of{B_i} = 0$ 
is necessary for the holonomy 2-functor to preserve the source and
target of 2-morphisms.  It also guarantees that the holonomy over a
parametrized bigon is invariant under thin homotopies. 
\endofproof

The reader familiar with gerbes will recognize that Lie-algebra-valued
differential forms of the above sort give a \emph{connection on an
abelian gerbe} when $\twogroup$ is of the special form described in
Example \ref{crossed.1}.  Similarly, they give rise to a \emph{connection
with vanishing fake curvature on a nonabelian gerbe} when $\twogroup$
is of the form described in Example \ref{crossed.2}.

The vanishing fake curvature condition is a strong one.  As Breen has
emphasized, it implies that the $\h$-valued `curvature' 3-form $H =
\extd B + d\alpha(A) \wedge B$ actually takes values in the kernel of
$dt$, which is an abelian ideal of $\h$.  So, the existence of
well-behaved holonomies forces a 2-connection to be somewhat abelian
in nature.
