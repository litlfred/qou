---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-024-moves-between-triangulated-pl-manifolds
section_title: "Moves between triangulated PL manifolds"
section_number: null
pages: 39-41
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.984
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
\label{subsec:PLsubsec}


To establish triangulation independence for  state sum models with defects, we require some background from PL topology. We consider different moves on triangulations that relate PL homeomorphic 3-manifolds with and without boundary. The main references  are the articles \cite{P, Pshell}  by Pachner, see also  the articles \cite{L} by Lickorish and \cite{Cas} by Casali.  


\begin{theorem}\cite[Th.~5.5]{P},\cite[Th.~5.9]{L}\\
Two closed triangulated $n$-dimensional PL manifolds are PL homeomorphic iff they are related by  a finite sequence of bistellar  moves.
\end{theorem}

\begin{theorem}\cite{Cas}\label{th:pachbound}\\
Two triangulated $n$-dimensional PL manifolds with boundary, whose boundary triangulations coincide, are PL homeomorphic iff they are related by bistellar moves.
\end{theorem}


The {\bf bistellar moves} for a 3-manifold are the  2-3 move and the 1-4 move depicted in Figure \ref{fig:bistellar}. The 1-4 move  subdivides a tetrahedron into four  by inserting a new vertex in its interior  or reverses this step. The 2-3 move replaces two tetrahedra that share a triangle by three tetrahedra that share an edge  or reverses this step. 


\begin{figure}
\begin{center}
\def\svgwidth{.41\columnwidth}
 
\end{center}
\caption{Bistellar moves for a tetrahedron.}
\label{fig:bistellar}
\end{figure}


We also consider {\bf stellar subdivisions}, see for instance \cite{RS}. The stellar subdivision for a tetrahedron is  the 1-4 move  from Figure \ref{fig:bistellar}. The stellar subdivisions for a triangle and an edge are shown in Figure \ref{fig:stellar}.
A stellar subdivision of a triangle $\Delta$ inserts a vertex in the interior of $\Delta$ and connects it to the vertices of $\Delta$ and to the  opposite vertices of all tetrahedra containing $\Delta$. 
A stellar subdivision of an edge $e$ inserts a vertex in the interior of $e$ and connects it to the opposite vertices of all triangles containing $e$. 

It is shown in \cite{BW} that stellar subdivisions are composites of 1-4 and 2-3 moves. The stellar subdivision for a triangle $\Delta$ is obtained by to first applying a 1-4 move   to one of the two tetrahedra containing $\Delta$ and then a 2-3 move to the other tetrahedron and the adjacent tetrahedron created by the 1-4 move, see the proof of Theorem 4.6 in \cite{BW}. The stellar subdivision for an edge $e$ shared by $n$ tetrahedra  is obtained by first applying a 1-4  move  to one of the tetrahedra containing $e$.  Then one applies a sequence of $(n-2)$  2-3  moves  clockwise to the remaining tetrahedra containing  $e$. These 2-3 moves  connect the new vertex  to the vertices of these  tetrahedra.  Finally one applies a 2-3  move that removes $e$, see the proof of Theorem 4.6 in  \cite{BW}.  





\begin{figure}
\begin{center}
\def\svgwidth{.41\columnwidth}
 
\end{center}
\caption{Stellar subdivisions for a triangle and an edge of a triangulation.}
\label{fig:stellar}
\end{figure}




For 3-manifolds with boundaries one also needs to consider elementary shellings and their inverses. An {\bf elementary shelling} of a PL 3-manifold $M$ removes a 3-simplex $t$ that is the  join $t=A\star B=\mathrm{conv}(A\cup B)$ of two simplexes $A$ and $B$ with $A\cap M=\partial A$ and $B\star \partial A\subset \partial M$ and replaces $M$ by the closure of $M\setminus A\star B$, see \cite[Def.~5.2]{L}. This amounts to removing the tetrahedron $t$, which has  one, two or three faces in the boundary $\partial M$, such that its remaining faces become boundary faces, as shown in Figure \ref{fig:shellingdef}. Correspondingly, an {\bf inverse shelling} amounts to adding a tetrahedron to $M$ that shares  one, two  or three triangles with $\partial M$. 
 
 \begin{figure}
\begin{center}
\def\svgwidth{.37\columnwidth}
 
\end{center}
\caption{Elementary shellings: removing a tetrahedron with one, two or three faces in the boundary.}
\label{fig:shellingdef}
\end{figure}
 
 
Elementary shellings and their inverses on a 3-manifold $M$ induce bistellar moves on the boundary $\partial M$. These are the 1-3 move, which subdivides a boundary triangle into three  by adding a vertex in its interior or reverses this step, and the 2-2 move, which replaces a common edge  shared by two boundary triangles with the edge connecting their remaining two vertices, as  in Figure \ref{fig:shellingdef}. It is shown  in \cite{Pshell, P} that  triangulations of a PL manifold with boundary are related by bistellar moves, elementary shellings and their inverses. 

\begin{theorem}\cite[Th.~4.14]{P}, \cite[Th.~2]{Pshell} \label{the:pachschellstell}\\
Two triangulated $n$-dimensional PL manifolds $M,M'$ with boundary are PL homeomorphic iff $M$ can be transformed into $M'$ by a finite number of elementary shellings and bistellar moves.
\end{theorem}

\begin{theorem}\cite[Th.~6.3]{P}, \cite[Th.~5.10]{L}\\  \label{th:pachshell}Two connected triangulated $n$-dimensional PL manifolds with non-empty boundary are PL homeomorphic iff they are related by a finite sequence of elementary shellings and  inverse shellings.
\end{theorem}




If a triangulated $n$-manifold $M$ is transformed  into  $M'$ by a finite number of elementary shellings, one says that $M$ {\bf shells} to $M'$. A triangulated $n$-manifold $M$ is called {\bf shellable} if it shells to an $n$-simplex. It is well-known that every triangulation and, more generally, CW-decomposition of a $2$-disc is shellable. 
This does not hold for  triangulations or CW-decompositions of the 3-ball, see Ziegler \cite{Zi} and the references therein.



The triangulation independence of the  Turaev-Viro-Barrett-Westbury  state sum  from \cite{TV,BW} follows from its invariance under bistellar moves.
It is shown in \cite{BW} and \cite{T} that the invariance of the state sum
 under the 2-3 move in Figure \ref{fig:bistellar} encodes the pentagon relation for the associator of a spherical fusion category. Its invariance under the 1-4 move in Figure \ref{fig:bistellar}  corresponds to an equivalent relation  obtained by inverting one of the associators in the pentagon relation.  It follows from the invariance under the 2-3 move and  under a \emph{bubble move}. The latter corresponds to the invertibility of the associator and  states that gluing two tetrahedra with  opposite orientations along  four faces yields the trivial state sum.  
 
 The pentagon relation for the associator is encoded in the Biedenharn-Elliott relations for the 6j symbols and the invertibility of the associator in their orthogonality relations
\cite[Prop.~5.2]{BW}.  They  are obtained by expressing the associator on simple objects of $\mac$ as in \eqref{eq:a6j} and using its naturality.
In our notation they read
\begin{align}
\label{eq:biedenharneliotsph}
&\begin{tikzpicture}[scale=.3]
\node at (-5,0) [anchor=east]{$\sum_{\beta}$};
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (-.5,5)--(.5,5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (-.5,-5)--(.5,-5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (0,3)--(-3,1) node[midway, anchor=south east]{$k$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0) node[pos=.7, anchor=south]{$\;j$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3) node[midway, anchor=north east]{$i$};
\node at (0,1.5) [anchor=west, color=black]{$n$};
\node at (0,-1.5) [anchor=west, color=black]{$p$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\alpha\;$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\delta$};

\begin{scope}[shift={(7,0)}]
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (-.5,5)--(.5,5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (-.5,-5)--(.5,-5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (0,3)--(-3,1) node[midway, anchor=south east]{$a$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0) node[pos=.7, anchor=south]{$\;b$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3) node[midway, anchor=north east]{$k$};
\node at (0,1.5) [anchor=west, color=black]{$q$};
\node at (0,-1.5) [anchor=west, color=black]{$n$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\phi\;$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\rho$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\sigma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\beta$};
\end{scope}
\node at (9,0)[anchor=west]{$=\sum_{c,\lambda,\mu,\nu}\dim(c)$};

\begin{scope}[shift={(24,0)}]
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (-.5,5)--(.5,5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (-.5,-5)--(.5,-5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (0,3)--(-3,1) node[midway, anchor=south east]{$a$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0) node[pos=.7, anchor=south]{$\;c$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3) node[midway, anchor=north east]{$i$};
\node at (0,1.5) [anchor=west, color=black]{$q$};
\node at (0,-1.5) [anchor=west, color=black]{$n$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\lambda\;$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\rho$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\mu$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\delta$};
\end{scope}
\begin{scope}[shift={(31,0)}]
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (-.5,5)--(.5,5) node[anchor=west] {$a$};
\draw[line width=.5pt, color=black] (-.5,-5)--(.5,-5) node[anchor=west] {$a$};
\draw[line width=.5pt, color=black] (0,3)--(-3,1) node[midway, anchor=south east]{$k$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0) node[pos=.7, anchor=south]{$\;j$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3) node[midway, anchor=north east]{$i$};
\node at (0,1.5) [anchor=west, color=black]{$b$};
\node at (0,-1.5) [anchor=west, color=black]{$c$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\alpha\;$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\phi$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\nu$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\lambda$};
\end{scope}
\begin{scope}[shift={(38,0)}]
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (-.5,5)--(.5,5) node[anchor=west] {$p$};
\draw[line width=.5pt, color=black] (-.5,-5)--(.5,-5) node[anchor=west] {$p$};
\draw[line width=.5pt, color=black] (0,3)--(-3,1) node[midway, anchor=south east]{$c$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0) node[pos=.7, anchor=south]{$\;b$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3) node[midway, anchor=north east]{$j$};
\node at (0,1.5) [anchor=west, color=black]{$q$};
\node at (0,-1.5) [anchor=west, color=black]{$n$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\nu\;$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\mu$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\sigma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\gamma$};
\end{scope}
\end{tikzpicture}
\end{align}
\begin{align}
\label{eq:orthogonalitysph}
&\begin{tikzpicture}[scale=.3]
\node at (-5,0) [anchor=east]{$\sum_{p,\gamma,\delta} \dim(p)\dim(k)$};
\node at (9,0)[anchor=west]{$=\delta_{\alpha\sigma}\delta_{\beta\rho}\delta_{kl}$};
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (-.5,5)--(.5,5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (-.5,-5)--(.5,-5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (0,3)--(-3,1) node[midway, anchor=south east]{$k$};
\draw[line width=.5pt, color=black] (-3,1)--(0,0) node[pos=.7, anchor=south]{$\;j$};
\draw[line width=.5pt, color=black] (-3,1)--(0,-3) node[midway, anchor=north east]{$i$};
\node at (0,1.5) [anchor=west, color=black]{$n$};
\node at (0,-1.5) [anchor=west, color=black]{$p$};
\draw[color=black, fill=black] (-3,1) circle (.2) node[anchor=east]{$\alpha\;$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\beta$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\delta$};

\begin{scope}[shift={(7,0)}]
\draw[line width=.5pt, color=black] (0,5)--(0,-5);
\draw[line width=.5pt, color=black] (-.5,5)--(.5,5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (-.5,-5)--(.5,-5) node[anchor=west] {$m$};
\draw[line width=.5pt, color=black] (0,3)--(-3,-1) node[midway, anchor=south east]{$i$};
\draw[line width=.5pt, color=black] (-3,-1)--(0,0) node[pos=.7, anchor=south]{$\;j$};
\draw[line width=.5pt, color=black] (-3,-1)--(0,-3) node[midway, anchor=north east]{$l$};
\node at (0,1.5) [anchor=west, color=black]{$p$};
\node at (0,-1.5) [anchor=west, color=black]{$n$};
\draw[color=black, fill=black] (-3,-1) circle (.2) node[anchor=east]{$\sigma\;$};
\draw[color=black, fill=black] (0,3) circle (.2) node[anchor=west]{$\delta$};
\draw[color=black, fill=black] (0,0) circle (.2) node[anchor=west]{$\gamma$};
\draw[color=black, fill=black] (0,-3) circle (.2) node[anchor=west]{$\rho$};
\end{scope}
\end{tikzpicture}
\end{align}

These relations yield a direct proof of the triangulation independence of the state sum for closed 3-manifolds \cite[Th.~5.1]{BW}.  For 3-manifolds  with boundary one has the following result.

\begin{theorem} \label{th:pachinv}\cite[Th.~1.4]{TV}, \cite[Th.~1.7]{T}\\
Let $M, M'$ be compact triangulated 3-manifolds with boundary whose boundary triangulations and boundary labelings $l_{\partial M}$ and $b_{\partial M}$ coincide. Then their  state sums \eqref{eq:statesumsph} are equal.
\end{theorem}
