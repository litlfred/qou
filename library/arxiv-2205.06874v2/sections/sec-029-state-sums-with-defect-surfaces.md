---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-029-state-sums-with-defect-surfaces
section_title: "State sums with defect surfaces"
section_number: null
pages: 51-59
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.976
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
In the following, we assume that all triangulations are generic and transversal at the boundary. 
Our first example is a defect sphere without defect lines or vertices embedded inside a 3-ball.  We suppose that the embedding is \emph{unknotted} in the sense of Zeeman \cite{Z}. This means that there is a PL homeomorphism from the 3-ball to itself that  sends the defect sphere to the boundary of a tetrahedron, see also Footnote 1  \cite{Z}.

\begin{example} \label{ex:tetrahedronsphere} Let $M$ be a 3-ball with an unknotted defect sphere  in its interior. Suppose the boundary of $M$ is labeled by a spherical fusion category $\mac$ and the defect sphere by 
 a $(\mac, \mad)$-bimodule category  $\mam$ with a bimodule trace.  Then for all boundary labelings $l_{\partial M}$, $b_{\partial M}$ the state sum of $M$ is
 \begin{align}\label{eq:bublle}
\mathcal Z(M, l_{\partial M},b_{\partial M})=\frac{\dim\mam}{\dim \mad}\cdot \mathcal Z(M', l_{\partial M}, b_{\partial M}), 
\end{align}
where $M'$ is a triangulated 3-ball labeled by $\mac$ with the same  boundary triangulation, but without defects. 
\end{example}


\begin{proof} As the defect sphere is unknotted, there is a PL homeomorphism from $M$ to itself that sends $D$ to the boundary of a tetrahedron.
By Theorem \ref{th:fulltopinv}, Corollary \ref{cor:generalinvariant} and because 
 different boundary triangulations  are related by elementary shellings and inverse shellings, it is sufficient to prove the claim for the triangulation
 \begin{center}
\def\svgwidth{.52\columnwidth}
 
\end{center}
 

We evaluate the state sum by gluing the polygon diagrams for the four tetrahedra in the triangulation. Gluing the bottom tetrahedron to the three tetrahedra above   with identity \eqref{pic:gluepoly} yields for the rescaled state sum 
\begin{align*}
&\begin{tikzpicture}[scale=.24]
\node at (-28,8) {$\mathcal Z'(M, l_{\partial M},b_{\partial M})=\frac 1 {\dim \mad}
\sum_{\substack{ {m,n,p,q}\\{\alpha,\beta,\gamma}}} \dim m\dim n\dim p\dim q$};
\draw[line width=1.5pt, color=blue, dotted] (-6,8) node[anchor=east]{$p$}--(6,8) node[anchor=west]{$n$};
\draw[line width=1.5pt, color=blue, dotted] (-6,8)--(0,0);
\draw[line width=1.5pt, color=blue, dotted] (6,8)--(0,0);

\draw[line width=1.5pt, color=blue] (-6,8)--(0,16) node[anchor=south]{$m$};
\draw[line width=1.5pt, color=blue] (6,8)--(0,16);

\draw[line width=1.5pt, color=blue] (-12,0)node[anchor=east]{$m$}--(-6,8);
\draw[line width=1.5pt, color=blue] (-12,0)--(0,0) node[anchor=north]{$q$};

\draw[line width=1.5pt, color=blue] (12,0) node[anchor=west]{$m$}--(6,8);
\draw[line width=1.5pt, color=blue] (12,0)--(0,0);

\draw[line width=.5pt] (0,5)--(0,10) node[pos=.3, anchor=east]{$g$} node[sloped, pos=.3, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-3,12)--(0,10)node[pos=.5, anchor=north]{$i$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,10)--(3,12) node[pos=.5, anchor=north]{$k$} node[sloped, pos=.5, allow upside down]{\arrowOut};

\draw[line width=.5pt] (-6,3)--(0,5) node[pos=.7, anchor=south]{$j$} node[sloped, pos=.7, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-6,3)--(-9,4) node[pos=.5, anchor=south]{$i$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-6,0)--(-6,3) node[pos=.5, anchor=east]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};

\draw[line width=.5pt] (0,5)--(6,3) node[pos=.3, anchor=south]{$l$} node[sloped, pos=.3, allow upside down]{\arrowOut};
\draw[line width=.5pt] (9,4)--(6,3) node[pos=.5, anchor=south]{$k$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (6,3)--(6,0) node[pos=.5, anchor=east]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};

\draw[fill=black] (0,10) circle (.2) node[anchor=south]{$\lambda$};
\draw[fill=black] (0,5) circle (.2) node[anchor=north]{$\mu$};
\draw[fill=black] (-6,3) circle (.2) node[anchor=south]{$\nu$};
\draw[fill=black] (6,3) circle (.2) node[anchor=south]{$\rho$};

\draw[fill=blue, color=blue] (-3,12) circle (.2) node[anchor=east]{$\alpha\;$};
\draw[fill=blue, color=blue] (3,12) circle (.2) node[anchor=west]{$\;\beta$};
\draw[fill=blue, color=blue] (-9,4) circle (.2) node[anchor=east]{$\alpha\;$};
\draw[fill=blue, color=blue] (9,4) circle (.2) node[anchor=west]{$\;\beta$};
\draw[fill=blue, color=blue] (-6,0) circle (.2) node[anchor=north]{$\;\gamma$};
\draw[fill=blue, color=blue] (6,0) circle (.2) node[anchor=north]{$\;\gamma$};
\end{tikzpicture}
\end{align*}
Applying identity \eqref{pic:closepoly} to eliminate the  summation over $\alpha$, $p$ yields
\begin{align*}
&\begin{tikzpicture}[scale=.24]
\node at (-30,0) {$\mathcal Z'(M, l_{\partial M},b)=\frac 1 {\dim \mad}\sum_{\substack{ {m,n,q}\\{\beta,\gamma}}} \dim m\dim n\dim q$};
\draw[line width=1.5pt, color=blue] (-10,0) node[anchor=east]{$m$}--(0,10) node[anchor=south]{$n$};
\draw[line width=1.5pt, color=blue] (10,0) node[anchor=west]{$m$}--(0,10);
\draw[line width=1.5pt, color=blue] (-10,0)--(0,-10) node[anchor=north]{$q$};
\draw[line width=1.5pt, color=blue] (10,0)--(0,-10);

\draw[line width=.5pt](5,5)--(5,0) node[pos=.5, anchor=west]{$k$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt](5,0)--(5,-5) node[pos=.5, anchor=west]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt](0,0)--(5,0)node[pos=.5, anchor=south]{$l$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt](-5,-2)--(0,0) node[pos=.5, anchor=north]{$j$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt](0,0)--(-5,2) node[pos=.5, anchor=south]{$g$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt](-5,-2)--(-5,2) node[pos=.7, anchor=west]{$i$} node[sloped, pos=.7, allow upside down]{\arrowOut};
\draw[line width=.5pt](-5,-5)--(-5,-2) node[pos=.5, anchor=west]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt](-5,2)--(-5,5) node[pos=.5, anchor=west]{$k$} node[sloped, pos=.5, allow upside down]{\arrowOut};

\draw[fill=blue, color=blue] (-5,5) circle (.2) node[anchor=south east]{$\;\beta$};
\draw[fill=blue, color=blue] (5,5) circle (.2) node[anchor=south west]{$\;\beta$};
\draw[fill=blue, color=blue] (-5,-5) circle (.2) node[anchor=north east]{$\;\gamma$};
\draw[fill=blue, color=blue] (5,-5) circle (.2) node[anchor=north west]{$\;\gamma$};

\draw[fill=black] (-5,2) circle (.2) node[anchor=east]{$\;\lambda$};
\draw[fill=black] (-5,-2) circle (.2) node[anchor=south east]{$\;\nu$};
\draw[fill=black] (0,0) circle (.2) node[anchor=south]{$\;\mu$};
\draw[fill=black] (5,0) circle (.2) node[anchor=west]{$\;\rho$};
\end{tikzpicture}
\end{align*}
and applying identity \eqref{pic:closepoly} to eliminate the summation over $\beta,n$ gives 
\begin{align*}
&\begin{tikzpicture}[scale=.24]
\node at (-28,0) {$\mathcal Z'(M, l_{\partial M},b_{\partial M})=\frac 1 {\dim \mad}\sum_{m,q,\gamma} \dim m\dim q$};
\draw[line width=1.5pt, color=blue] (10,0) node[anchor=west]{$m$}.. controls (2,-10) and (-2,-10)..(-10,0) node[anchor=east]{$q$};
\draw[line width=1.5pt, color=blue] (10,0) .. controls (2,10) and (-2,10)..(-10,0) ;

\draw[line width=.5pt] (0,7.5)--(0,4) node[pos=.5, anchor=west]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,-4)--(0,-7.5) node[pos=.5, anchor=west]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,4)--(3,-1) node[pos=.5, anchor=south west]{$i$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,4)--(-3,1) node[pos=.5, anchor=south east]{$j$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-3,1)--(3,-1) node[pos=.5, anchor=south]{$g$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (3,-1)--(0,-4) node[pos=.5, anchor=north west]{$k$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-3,1)--(0,-4) node[pos=.5, anchor=north east]{$l$} node[sloped, pos=.5, allow upside down]{\arrowOut};

\draw[fill=blue, color=blue] (0,7.5) circle (.2) node[anchor=south]{$\gamma$};
\draw[fill=blue, color=blue] (0,-7.5) circle (.2) node[anchor=north]{$\gamma$};

\draw[fill=black] (0,4) circle (.2) node[anchor=west]{$\;\nu$};
\draw[fill=black] (0,-4) circle (.2) node[anchor=west]{$\;\rho$};
\draw[fill=black] (-3,1) circle (.2) node[anchor=east]{$\mu\;$};
\draw[fill=black] (3,-1) circle (.2) node[anchor=west]{$\;\lambda$};
\end{tikzpicture}
\end{align*}
Applying identity \eqref{pic:2gon} to this diagram yields the result
\begin{align*}
\quad\begin{tikzpicture}[scale=.23]
\node at (-15,0) {$\mathcal Z'(M, l_{\partial M},b_{\partial M})=\frac{\dim \mam}{\dim\mad}\quad$};

\draw[line width=.5pt] (0,7.5)--(0,4) node[pos=.5, anchor=west]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,-4)--(0,-7.5) node[pos=.5, anchor=west]{$h$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,4)--(3,-1) node[pos=.5, anchor=south west]{$i$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,4)--(-3,1) node[pos=.5, anchor=south east]{$j$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-3,1)--(3,-1) node[pos=.5, anchor=south]{$g$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (3,-1)--(0,-4) node[pos=.5, anchor=north west]{$k$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (-3,1)--(0,-4) node[pos=.5, anchor=north east]{$l$} node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,7.5).. controls (0,10.5) and (-6,10.5)..(-6,7.5);
\draw[line width=.5pt] (-6,-7.5)--(-6,7.5) node[sloped, pos=.5, allow upside down]{\arrowOut};
\draw[line width=.5pt] (0,-7.5).. controls (0,-10.5) and (-6,-10.5)..(-6,-7.5);

\draw[fill=black] (0,4) circle (.2) node[anchor=west]{$\;\nu$};
\draw[fill=black] (0,-4) circle (.2) node[anchor=west]{$\;\rho$};
\draw[fill=black] (-3,1) circle (.2) node[anchor=east]{$\mu\;$};
\draw[fill=black] (3,-1) circle (.2) node[anchor=west]{$\;\lambda$};
\node at (14,0) {$=\frac{\dim \mam}{\dim \mad}\cdot \mathcal Z'(M', l_{\partial M},b_{\partial M}).$};
\end{tikzpicture}\\[-8ex]
\end{align*}
\end{proof}

Note that  Example \ref{ex:tetrahedronsphere}  yields the  usual Turaev-Viro-Barrett-Westbury invariant for a 3-ball without defects,
if one chooses for $\mam$ a spherical fusion category $\mac=\mad$ as a bimodule category over itself. 

State sums with defect surfaces of genus $g\geq 1$ are more difficult to compute.  We therefore restrict attention to the spherical fusion category $\mac=\mathrm{Vec}_G$ for a finite group $G$ from Example \ref{ex:vectgomega},  equipped  with  a trivial 3-cocycle and the standard spherical structure. 
The associated Turaev-Viro-Barrett-Westbury state sums are a special case of  the Dijkgraaf-Witten models from \cite{DW}, see also  Altschuler and Coste \cite{AC}.  

By Example \ref{ex:vectgomega} simple objects in $\mathrm{Vec}_G$ correspond to group elements $g\in G$. For simplicity, we denote them by $g$ instead of $\delta^g$ in the following. One has $\dim(g)=1$ for all $g\in G$ and $\dim(\mac)=|G|$ as well as
\begin{align}\label{homvecg0}
 \Hom_\mac(k, i\oo j)\cong \Hom_\mac(i\oo j, k)\cong \delta_k(ij)\C\qquad\qquad\forall i,j,k\in G.
 \end{align} 
By Examples \ref{ex:modvectgomega} and \ref{ex:tracevect}, every finite transitive $G\times G'^{op}$-set $X$ defines an  indecomposable  semisimple $(\mathrm{Vec}_G, \mathrm{Vec}_{G'})$-bimodule category $\mam$ with a bimodule trace, whose simple objects are in bijection  with elements of $X$. In the following, we only consider the case, where the cocycle defining $\psi \in H^2(L,\C^{\times})$ from Example  \ref{ex:modvectgomega} is trivial.  One  has $\dim(x)=1$ for all $x\in X$ and $\dim(\mam)=|X|$ as well as  
\begin{align}\label{eq:homvecg}
&\Hom_\mam(x, g\rhd y)\cong \Hom_\mam (g\rhd y, x) \cong \delta_x(g\rhd y) \C\\  
&\Hom_\mam(x,  y\lhd g')\cong \Hom_\mam (y\lhd g', x) \cong \delta_x( y\lhd g') \C \qquad \forall x,y\in X,\, g\in G, \, g'\in G'.\nonumber
\end{align} 
Hence, any 6j symbol vanishes, unless for each triangle with edges labeled by  $x, y\in X$ and by $g\in G$ or $g'\in G'$, the objects $x$ and $y$ are related by the action of $g$ or $g'$. Similarly,  for any triangle with labeled  elements of $G$ or $G'$, the oriented product of the group elements must be trivial by \eqref{homvecg0}. 
Morphism labels for triangles are just numbers in $\C$, and all sums over bases of morphism spaces become trivial.

\begin{example}  \label{ex:surface}Let  $\mac=\mathrm{Vec}_G$ and $\mad=\mathrm{Vec}_{G'}$  for finite groups $G,G'$ and $\mam$ the indecomposable $(\mac,\mad)$-bimodule category with bimodule trace defined by a finite transitive  $G\times G'^{op}$-set $X$. 

Let $\Sigma$ be a closed oriented triangulated surface of genus $g\geq 1$ and $M=[0,1]\times\Sigma$ the fine neighbourhood of $\Sigma$
obtained by replacing each triangle in $\Sigma$ by a prism as in Figure \ref{eq:prism}, with a defect surface $\{\tfrac 1 2\}\times\Sigma$ labeled by  $\mam$ and boundary components $\{1\}\times\Sigma$ and $\{0\}\times\Sigma$ labeled by $\mac$ and $\mad$.  Suppose that all boundary triangles with non-trivial morphism spaces are labeled with identity morphisms. 

Then the rescaled state sum of $M$ is 
\begin{align*}
 &\mathcal Z'(M, l_{\partial M}, b_{\partial M})=\begin{cases}
|X^{\rho(\pi_1(\Sigma))}|   & \text{if the oriented product of the group elements in each triangle}\\[-.5ex]
&  \text{on $\{0\}\times\Sigma$ and $\{1\}\times\Sigma$ is trivial,}\\[+1ex]
0 & \text{else},
\end{cases}
\end{align*}
where  $\rho: \pi_1(\Sigma)\to G\times G'$ is the group homomorphism defined by the labels on $\{0\}\times\Sigma$ and $\{1\}\times\Sigma$ and
$X^{\rho(\pi_1(\Sigma))}$ the fixed point set for the induced action of $\pi_1(\Sigma)$. 

In particular:
\begin{itemize}
\item {\bf trivial defect surface:} If $G=G'=X$ with the standard $G\times G^{op}$-set structure, then 
$\mathcal Z'(M, l_{\partial M},b_{\partial M})=0$ unless the oriented product of the group elements in each triangle on $\{0\}\times\Sigma$ and $\{1\}\times\Sigma$ is trivial and the associated group homomorphisms $\rho_0,\rho_1: \pi_1(\Sigma)\to G$ are conjugated. Then
$\mathcal Z'(M, l_{\partial M},b_{\partial M})=|\mathrm{Stab}(\rho_0)|$, where $\mathrm{Stab}(\rho_0)$ is the stabiliser of $\rho_0$ for the conjugation action of $G$ on $\Hom_{\mathrm{Grp}}(\pi_1(\Sigma), G)$. 


\item {\bf trivial $G\times G'^{op}$-set:} For a trivial $G\times G'$-set $X=\{\bullet\}$, one has  
$\mathcal Z'(M, l_{\partial M}, b_{\partial M})=1$, whenever
the oriented product of the group elements in each triangle on $\{0\}\times\Sigma$ and $\{1\}\times\Sigma$ is trivial. 


\item {\bf normal subgroup:} If $X=G\times G'^{op}/N$ for a normal subgroup $N\subset G\times G'^{op}$ one has $\mathrm{Stab}(m)=\mathrm{Stab}(m')=N$ for all $m,m'\in X$. This implies  
$\mathcal Z'(M, l_{\partial M},b_{\partial M})=|X|$, whenever 
the oriented product of the group elements in each triangle on $\{0\}\times\Sigma$ and $\{1\}\times\Sigma$ is trivial and the labelings of $\{1\}\times\Sigma$  and $\{0\}\times\Sigma$  define a group homomorphism $\rho: \pi_1(\Sigma)\to N$. 
\end{itemize}
\end{example}


\begin{proof}
  Orient the top and bottom triangle of each prism as the associated triangle of $\Sigma$,  the vertical edges of each prism according to the orientation of $\Sigma$. Subdivide each prism into three tetrahedra as  in Figure \ref{eq:prism}. Label its top and bottom edges  with 
 elements of $G$ and $G'$   and the vertical  edges with elements of $X$.
  \begin{figure}
\begin{center}
\begin{tikzpicture}[scale=.35]
\draw[color=gray, line width=1pt] (5,0)--(-5,0) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=north]{$j'$};
\draw[color=gray, line width=1pt] (3,5)--(5,0) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south west]{$i'$};
\draw[color=gray, line width=1pt] (3,5)--(-5,0) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south east]{$k'$};

\draw[color=black, line width=1pt] (5,12)--(-5,12) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$j$};
\draw[color=black, line width=1pt] (3,17)--(5,12) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south west]{$i$};
\draw[color=black, line width=1pt] (3,17)--(-5,12) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south east]{$k$};

\draw[color=blue, line width=1pt] (-5,0)--(-5,12) node[sloped, pos=0.6, allow upside down]{\arrowIn} node[pos=.6, anchor=east]{$m$};
\draw[color=blue, line width=1pt] (5,0)--(5,12) node[sloped, pos=0.6, allow upside down]{\arrowIn} node[pos=.6, anchor=west]{$n$};
\draw[color=blue, line width=1pt] (3,5)--(3,17) node[sloped, pos=0.7, allow upside down]{\arrowIn} node[pos=.7, anchor=west]{$p$};
\draw[line width=1pt, color=blue] (3,5)--(-5,12) node[sloped, pos=0.75, allow upside down]{\arrowIn} node[pos=.75, anchor=south west]{$s$};
\draw[line width=1pt, color=blue] (3,5)--(5,12) node[sloped, pos=0.7, allow upside down]{\arrowIn} node[pos=.7, anchor=south east]{$q$};

\draw[draw=none, fill=white] (1.6,4.2) circle (.3);
\draw[color=blue, line width=1pt, fill=white] (-5,6)--(5,6)--(3,11)--(-5,6);
\draw[draw=none, fill=blue, fill opacity=.1] (-5,6)--(5,6)--(3,11)--(-5,6);
\node at (2.5,7.5) [color=blue]{$\Sigma$};
\draw[line width=.5pt, color=blue, -stealth] (2.5,6)--(2.5,7);
\draw[line width=1pt, color=blue] (5,6)--(-5,6) node[sloped, pos=0.7, allow upside down]{\arrowIn};
\draw[line width=1pt, color=blue] (3,11)--(-5,6) node[sloped, pos=0.7, allow upside down]{\arrowIn};
\draw[line width=1pt, color=blue] (3,11)--(5,6) node[sloped, pos=0.7, allow upside down]{\arrowIn};

\draw[line width=1pt, color=blue] (5,0)--(-5,12) node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=north east]{$r$};
\draw[line width=1pt, dashed, color=blue] (0,6)--(-1.1,8.5);
\draw[line width=1pt, dashed, color=blue] (3.75,8.5)--(-1.1,8.5);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[scale=.4]
\draw[color=blue, line width=1pt] (10,0) node[anchor=west]{$n$}--(-10,0) node[anchor=east]{$m$}; 
\draw[color=blue, line width=1pt] (6,10) node[anchor=south]{$p$}--(10,0); 
\draw[color=blue, line width=1pt] (6,10)--(-10,0); 
\draw[color=blue, line width=1pt, dashed] (8,5) node[anchor=south west]{$q$}--(-2,5) node[anchor=south east] {$s$} --(0,0) node[anchor=north]{$r$};
\draw[line width=.5pt, color=gray] (9,2.5)--(-1,2.5) node[sloped, pos=0.7, allow upside down]{\arrowIn} node[pos=.7, anchor=south]{$i'$};
\draw[color=white, fill=white] (4,2.5) circle(.4);
\draw[line width=.5pt, color=black] (3,5)--(5,0) node[sloped, pos=0.3, allow upside down]{\arrowIn} node[pos=.3, anchor=west]{$\;j$};
\draw[line width=.5pt,color=black] (4,7)--(3,5) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=west]{$\;j$};
\draw[line width=.5pt, color=black] (4,7)--(7,7.5) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$\;i$};
\draw[line width=.5pt, color=black] (2,7.5)--(4,7) node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=north]{$k$};
\draw[color=black, fill=black] (4,7) circle (.15) node[anchor=south]{$\alpha$};

\draw[line width=.5pt, color=gray] (-1,2.5)--(-4,2)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=south]{$i'$};
\draw[line width=.5pt, color=gray] (-5,0)--(-4,2)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=west]{$j'$} ;
\draw[line width=.5pt, color=gray] (-4,2)--(-6,2.5)  node[sloped, pos=0.5, allow upside down]{\arrowIn} node[pos=.5, anchor=north]{$k'$};
\draw[color=gray, fill=gray] (-4,2) circle (.15) node[anchor=south]{$\alpha'$};

\draw[color=blue, fill=blue] (2,7.5) circle (.15) node[anchor=south east] {$\lambda$};
\draw[color=blue, fill=blue] (7,7.5) circle (.15) node[anchor=west] {$\mu$};
\draw[color=blue, fill=blue] (9,2.5) circle (.15) node[anchor=west] {$\nu$};
\draw[color=blue, fill=blue] (5,0) circle (.15) node[anchor=north] {$\rho$};
\draw[color=blue, fill=blue] (-5,0) circle (.15) node[anchor=north] {$\sigma$};
\draw[color=blue, fill=blue] (-6,2.5) circle (.15) node[anchor=south east] {$\tau$};
\end{tikzpicture}
\end{center}
\caption{A labeled triangular prism and the  associated polygon diagram.}
\label{eq:prism}
\end{figure}


\begin{figure}
\begin{center}
\def\svgwidth{.75\columnwidth}
 
\end{center}
\caption{Polygon diagram $P$ for $M=[0,1]\times\Sigma$ for triangulated defect surface $\Sigma$ of genus 2. \newline
$\bullet$ The orientation of the blue lines indicates the orientation of the triangulation on $\Sigma$. \newline
$\bullet$ The group elements on the unlabeled edges are determined by the labels.\newline 
$\bullet$ $\mathrm{ev}(P)=0$ unless $[a_1, b_1]\cdots [a_g, b_g]=1$ and $[a'_1,b'_1]\cdots [a'_g,b'_g]=1$ and $(a_i,a'_i), (b_i, b'_i)\in \mathrm{Stab}(m)$ for $i=1,2$.}
\label{fig:polygonsurface}
\end{figure}

By Proposition \ref{lem:polystatesum} the state sum of each labeled  prism is given by the evaluation of  the  polygon diagram in Figure \ref{eq:prism}. Also by Proposition \ref{lem:polystatesum}, the state sum for $M$ is given by the evaluation of any polygon diagram $P$ obtained by  gluing the polygons of the prisms to a disc and summing over the objects at its boundary. We can assume without loss of generality that $P$  is a $4g$-gon with every vertex labeled by  $m\in X$, as in Figure \ref{fig:polygonsurface}. This yields
$$\mathcal Z'(M, l_{\partial M},b_{\partial M})=\sum_{m\in X} \mathrm{ev}(P).$$
By identity \eqref{homvecg0},  the evaluation of $P$ vanishes, unless at each  vertex of $P$ that involves only edges labeled by $G$ or $G'$,  the oriented product of these group elements  is trivial.  By choosing maximal trees in the graphs labeled by $G$ and $G'$, one can express the group elements on the trees in terms of the  $2g$ group elements on edges that intersect $\partial P$, where $g$ is the genus of $\Sigma$. The labels on these $2g$ edges  then define
 a group homomorphism $\rho: \pi_1(\Sigma)\to G\times G'$, as shown in Figure \ref{fig:polygonsurface}.


By identity \eqref{eq:homvecg} the evaluation  $\mathrm{ev}(P)$ vanishes unless the group elements $(a_i,a'_i), (b_i, b'_i)\in G\times G'^{op}$ on each side of $P$ are contained in the stabiliser  of $m\in X$ or, equivalently, 
the group homomorphism $\rho$ takes values in $\mathrm{Stab}(m)$.
In that case, one has $\mathrm{ev}(P)=1$. 
Summation over all elements $m\in X$ then yields the result. 
\end{proof}



\begin{figure}
\begin{center}
\def\svgwidth{.98\columnwidth}
 
 \end{center}
\caption{Gluing a surface of genus $g=2$ inside a 3-ball.}
 \label{fig:handle}
\end{figure}

Example \ref{ex:surface} gives intuition how the data for the spherical fusion categories interacts with the defect data in state sums of defect 3-manifolds.  The next example shows that  state sums for defect surfaces in the interior of a 3-ball  detect the genus of the defect surface. 



\begin{example} \label{ex:genusg}Let  $\mac=\mathrm{Vec}_G$ and $\mad=\mathrm{Vec}_{G'}$ for finite groups $G,G'$ and
 $\mam$ the $(\mac,\mad)$-bimodule category with bimodule trace  defined by a finite transitive  $G\times G'^{op}$-set $X$. 
 Let $M$ be the triangulated 3-ball from Figure \ref{fig:handle} with an embedded defect surface of genus $g\geq 1$ in its interior. Then 
\begin{align}\label{eq:genussurf}
\mathcal Z(M, l_{\partial M},b_{\partial M})= \frac {|X|\cdot  |\mathrm{Stab}_G|^g\cdot  |\mathrm{Stab}_{G'}|^g}  {|G'|}  \cdot \mathcal Z(M', l_{\partial M}, b_{\partial M}),
\end{align}
where $M'$ is the 3-ball  with the same boundary triangulation and labeling, but without defects and $|\mathrm{Stab}_G|$, $|\mathrm{Stab}_{G'}|$ are the cardinalities of the stabilisers for the $G$- and $G'$-actions on $X$.
\end{example}

\begin{proof}
The triangulated defect 3-manifold in Figure \ref{fig:handle} is constructed as follows:
\begin{compactitem}
\item take $2g$ triangular double-pyramids formed by three tetrahedra each,  with a cylinder labeled by $\mam$ around the interior edge labeled by $\mad$,
\item glue them pairwise along  adjacent top and bottom faces to form $g$ rectangular double-pyramids,
\item glue the four bottom faces of each rectangular double-pyramid to the four top faces of the next one, 
\item glue a rectangular pyramid subdivided into four tetrahedra with defect triangles to the top and the bottom of the resulting polyhedron. 
\end{compactitem}
If the edges are labeled by group elements as in Figure \ref{fig:handle}, then
the edges labeled $ i,j,k,l, w_s,x_s,y_s, z_s\in G$  for $s=1,2$ are boundary edges.  The edges labeled by  $d_r,d'_r\in G'$, by $c_r\in G$ for $r=1,...,g$ and by $m_s,n_s,p_s,q_s, t,b\in X$  for $s=1,...,g+1$ are internal, and their labels are summed over.  Conditions \eqref{homvecg0} and \eqref{eq:homvecg} on the  morphism spaces imply that the state sum  is zero unless the following conditions are met:
\begin{itemize}
\item boundary edges of top and bottom pyramid:
\begin{align}
\label{eq:topcond}
&x_s=y_s\cdot i=w_s\cdot j,\quad z_s= y_s\cdot k=w_s\cdot l & &s\in\{1,2\},
\end{align}
\item defect edges of top and bottom pyramid:
\begin{align}\label{eq:topint}
&m_1=x_1^\inv\rhd t, & &n_1=y_1^\inv \rhd t, & &p_1=w_1^\inv\rhd t, & &q_1=z_1^\inv\rhd t,\\
&m_{g+1}=x_2^\inv\rhd b, & &n_{g+1}=y_2^\inv \rhd b, & &p_{g+1}=w_2^\inv\rhd b, & &q_{g+1}=z_2^\inv\rhd b,\nonumber
\end{align}
\item  double-pyramids: for $r\in \{1,...,g\}$
\begin{align}\label{eq:doublep}
&n_r=i\rhd m_r=k\rhd q_r, \quad p_r=c_r\rhd n_r=j\rhd m_r=l\rhd q_r,\\
&m_{r+1}=m_r\lhd d_r, \quad n_{r+1}=n_r\lhd d_r=n_r\lhd d'_r, \quad p_{r+1}=p_r\lhd d_r=p_r\lhd d'_r, \quad q_{r+1}=q_r\lhd d_r=q_r\lhd d'_r.\nonumber
\end{align}
\end{itemize}
Condition \eqref{eq:topcond} just states that the state sum is zero, unless the oriented product over the group elements of each boundary triangle is trivial. The first condition in \eqref{eq:topint} and the second condition in \eqref{eq:doublep} imply 
\begin{align} \label{eq:iter}
&m_{r+1}=x_1^\inv\rhd t\lhd d_1\cdots d_r & &q_{r+1}=w_1^\inv\rhd t\lhd d'_1\cdots d'_r\\
&n_{r+1}=y_1^\inv\rhd t\lhd d_1\cdots d_r=y_1^\inv\rhd t\lhd d'_1\cdots d'_r & 
&p_{r+1}=z_1^\inv\rhd t\lhd d_1\cdots d_r=z_1^\inv\rhd t\lhd d'_1\cdots d'_r\nonumber
\end{align}
for all $r\in\{1,...,g\}$.  This expresses  $m_s, n_s, p_s, q_s\in X$ as functions of $t\in X$, $d_1,...,d_g, d'_1,....,d'_n\in G'$ and of the group elements on the boundary edges and eliminates the summation over $m_s, n_s, p_s, q_s$. The equations in the second  line of \eqref{eq:iter} are satisfied simultaneously iff for all $r\in \{1,...,.g\}$
\begin{align}\label{eq:dcond}
d_1'\cdots d'_rd_r^\inv\cdots d_1^\inv\in \mathrm{Stab}_{G'}(t)=\{g\in G'\mid t\lhd g'=t\}.
\end{align}
Combining \eqref{eq:iter} with the second line in \eqref{eq:topint} yields
\begin{align}\label{eq:bexp}
b=w_2w_1^\inv\rhd t\lhd d_1\cdots d_r=x_2x_1^\inv\rhd t\lhd d_1\cdots d_r=y_2y_1^\inv\rhd t\lhd d_1\cdots d_r=z_2z_1^\inv\rhd t\lhd d_1\cdots d_r.
\end{align}
As \eqref{eq:topcond} implies $x_2x_1^\inv=y_2y_1^\inv=w_2w_1^\inv=z_2z_1^\inv$, equation \eqref{eq:bexp} just expresses $b$ in terms of $t$ and $d_1,...,d_r$ and thus eliminates the summation over $b$ from the state sum.  The first line in \eqref{eq:doublep} is then equivalent to \eqref{eq:iter}, \eqref{eq:topcond} and the additional condition
\begin{align}\label{eq:crcond}
w_1c_r y_1^\inv\in \mathrm{Stab}_G(t)=\{g\in G\mid g\rhd t=t\}\quad\forall r\in\{1,...,g\}.
\end{align}
 For fixed $t$ and $d_1,...,d_g$, the summations over $d'_1,...,d'_g$ and  $c_1,...,c_g$ 
contribute  factors $|\mathrm{Stab}_{G'}(t)|^g$ and $|\mathrm{Stab}_G(t)|^g$, respectively, to the state sum. As $X$ is a transitive $G\times G'^{op}$-set, all stabilisers have the same cardinality, and the summation over $t$ contributes a factor $|X|$.  
As each of the $g+1$ internal  vertices with incident edges from $\mad$  contributes a factor $\dim(\mad)^\inv=|G'|^\inv$ and the summation over  $d_1,...,d_g$ yields a factor $\dim(\mad)^g=|G'|^g$ we obtain
\begin{align*}
\mathcal Z'(M, l_{\partial M}, b_{\partial M})
&=
 \frac{|X| |\mathrm{Stab}_G|^g |\mathrm{Stab}_{G'}|^g}{|G'| } C,
\end{align*}
where $C$ is a factor that depends only on the labeling of the boundary triangles.
For $\mam=\mac=\mad=\mathrm{Vec}_G$ as a bimodule category over itself,  one has $|X|=|G'|=|G|$, $|\mathrm{Stab}_G|=|\mathrm{Stab}_{G'}|=1$. 
 \end{proof}
 
It is instructive to compare  Examples  \ref{ex:tetrahedronsphere} and  \ref{ex:genusg}.  If one  restricts the data in Example \ref{ex:tetrahedronsphere} to the bimodule category given by a finite $G\times G'^{op}$-set $X$ from Example \ref{ex:genusg}, then formula \eqref{eq:bublle} for the state sum of a 3-ball with a defect sphere becomes
$
\mathcal Z(M, l_{\partial M},b_{\partial M})= |X|/ |G'|  \cdot \mathcal Z(M', l_{\partial M}, b_{\partial M})$,
which is formula \eqref{eq:genussurf} for $g=0$. 

 
 
 
 Examples \ref{ex:tetrahedronsphere} to \ref{ex:genusg} show that the state sums detect properties of the bimodule categories labeling a defect surface and properties of the surface. The next example shows that the state sum models with defects  depend on the \emph{embeddings} of defect surfaces  into the  3-manifold, and not just on their topology.  

This is manifest even for very simple non-trivial defect data. 
 By taking a tubular neighbourhood of a knot $K$ embedded into $S^3$ and labeling it with the $\mathrm{Vec}_G$-module category defined by a trivial $G$-set, one obtains a triangulation of the knot complement with trivial data at the boundary. The associated state sum gives the number of conjugacy classes of group homomorphisms $\rho:\pi_1(S^3\setminus K)\to G$ and hence is  sensitive to the embedding of the toroidal defect surface.

 
 \begin{example}\label{ex:knotcomplement} Let $K\subset S^3$ be a knot, realised as a subgraph of the dual cell complex of 
 a triangulation $T$ of 
  $S^3$. Let $M$ be the triangulated 3-manifold with defect data constructed as follows: 
  \begin{enumerate}
\item   Refine $T$ to a triangulation $T'$ by 
applying a 1-4  move to each tetrahedron $t$  in $T$ with $t\cap K\neq \emptyset$ and a stellar move to each triangle $\Delta$ in $T$ with $\Delta \cap K\neq \emptyset$, such that $K$ connects the midpoints of two faces of $t$ with the vertex in its interior, as shown in Figure \ref{fig:knotcomplement}.  

\item Form a tubular neighbourhood of $K$ by  inserting a defect plane as in Figure \ref{fig:dectet} (b) into each tetrahedron of $T'$ that contains an  edge in $K$ and a defect plane as in  Figure \ref{fig:dectet} (a) into each tetrahedron of $T'$ that contains a vertex, but not an edge of $K$, as shown in Figure \ref{fig:knotcomplement}. 
 
 \item Label the region of $T'$ that does not contain $K$ with  $\mac=\mathrm{Vec}_G$ for a finite group $G$ and the region containing  $K$ with the spherical fusion category $\mad=\mathrm{Vec}_{\{1\}}=\mathrm{Vect}_\C$. Label  the defect surface with the  $(\mac,\mad)$-bimodule category $\mam$ defined by the trivial $G$-set $X=\{\bullet\}$. 
 \end{enumerate}
 Then the state sum of  $M$ is the number of  conjugacy classes of group homomorphisms from the fundamental group $\pi_1(S^3\setminus K)$  into $G$ 
 $$
 \mathcal Z(M)=|\Hom_{\mathrm{Grp}}(\pi_1(S^3\setminus K), G)/G|.
 $$
 \end{example}
 
 
 \begin{figure}
\begin{center}
\def\svgwidth{.5\columnwidth}
 
 \end{center}
\caption{A piece of a knot (red)  in the dual complex of a triangulation and the associated defect surface. The state sum vanishes unless $g_3=g_1g_2$ and $g_5=g_1g_4$.}
 \label{fig:knotcomplement}
\end{figure}


 \begin{proof} Denote by $r_\mac$ the region labeled by $\mac=\mathrm{Vec}_G$.
  By subdividing the triangulation as in Lemma \ref{lem:finetriang}, 
 we can assume that each  vertex, edge or triangle in $T'$ that contained in  $r_\mac$  is part of a tetrahedron contained in $r_\mac$. This does not change the state sum by Theorem \ref{th:fulltopinv}. 
The union of the tetrahedra  in $r_\mac$ is then PL homeomorphic to the knot complement $S^3\setminus K'$, where $K'$ is a solid torus $S^1\times D^2$ embedded as a tubular neighbourhood of $K$. This defines a triangulation $T''$ of $S^3\setminus K'$ labeled by $\mathrm{Vec}_G$. 
 

The remaining tetrahedra are as in Figure \ref{fig:knotcomplement}. By construction, all red edges in Figure \ref{fig:knotcomplement} are labeled with the simple object $\C$ of $\mathrm{Vect}_\C$, all blue edges by the simple object $\bullet$ in $\mam$, while the black edges are labeled with elements of $G$.   Each triangle $\Delta$ with $\Delta\cap t\neq \emptyset$ has two edges labeled by $\bullet$, one edge labeled by a group element $g\in G$ and is assigned the morphism space $\Hom(\bullet, \bullet)\cong \C$ for any $g\in G$. The triangles $\Delta$ in Figure \ref{fig:knotcomplement} with $\Delta\cap D=\emptyset$ are part of tetrahedra contained in $r_\mac$. Their labeling is determined by the labeling of $T''$, and their morphism spaces are $\Hom(\Delta)\cong \C$ if the oriented product of the group elements on their edges
 is trivial and $\Hom(\Delta)\cong \{0\}$ else.  
 
 Let $l: E''\to G$ be a labeling  of the oriented edges of $T''$ with elements of $G$.  
 As each triangle in $T'$ occurs in exactly two tetrahedra and all morphism spaces are zero- or one-dimensional,  the product of all generalised 6j symbols in $T'$ is one if the oriented product of the group elements on each triangle $\Delta$ in $T''$ vanishes and zero else. It follows that the state sum is  proportional to  the number of labelings $l$ that satisfy this condition
\begin{align}
\label{eq:statesumknotcomp}
\mathcal Z(M)=\frac { |\{l: E''\to G\mid \Pi_{e\in f}l(e)=1\;\forall f\in \Delta'' \}|} {|G|^{|V''|}},
\end{align}
 where $V''$, $E''$ and $\Delta''$ are the sets of vertices, edges and triangles of $T''$.
 
 Every such  labeling $l$  defines a group homomorphism $\rho_l:\pi_1(S^3\setminus K)\to G$, and every group homomorphism $\rho:\pi_1(S^3\setminus K)\to G$ is obtained from such a labeling.  The group homomorphisms $\rho_l,\rho_{l'}$ for two labelings $l,l': E''\to G$ are conjugate  iff there is a map $f: V''\to G$, $v\mapsto g_v$ such that
$l'(e)=g_{t(e)}\cdot l(e)\cdot g_{s(e)}$  for all $e\in E''$, where $s(e)$ and $t(e)$ denote the starting and target vertex of  $e$. 
This shows that $\mathcal Z(M)$ is the number of conjugacy classes of group homomorphisms $\rho:\pi_1(S^3\setminus K)\to G$. 
 \end{proof}
 
 Although the data in Example \ref{ex:knotcomplement} is quite trivial, it shows that the state sum with defects can distinguish non-isotopic embeddings of surfaces. It would be interesting to  investigate this further and to see if it can distinguish  knotted embeddings of  spheres.
