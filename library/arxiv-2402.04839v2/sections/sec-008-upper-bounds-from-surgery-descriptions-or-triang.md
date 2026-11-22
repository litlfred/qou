---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-008-upper-bounds-from-surgery-descriptions-or-triang
section_title: "Upper bounds from surgery descriptions or triangulations"
section_number: null
pages: 8-11
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.981
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{ssec:upperlower}

Suppose the $3$--manifold $M$ is given by surgery on a hyperbolic link $L \subset S^3.$ By definition of the surgery diagram, there is a link $L^* \subset M$ such that $S^3 \setminus L = M\setminus L^*.$ We thus have $\volh (S^3 \setminus L) = \volh (M \setminus L^*) \geq \volt (M)$. 

\begin{example}
The 3--torus $T^3$ is given by $0$-surgery on all components of the Borromean rings $B$ (a hyperbolic link). Thus there is a hyperbolic link $B^* \subset T^3$ with the same complement as $B$ in $S^3.$ In particular, we have $\volt(T^3)\leq \volh(B)<7.33$. The topological volume of $T^3$ (and other product manifolds) is further studied in~\cite{volt2}. In particular, it is conjectured that $\volt(T^3)$ is realised by the Borromean rings and that there is no minimiser with fewer components. Thus $T^3$ is a candidate to have $h(T^3)>1$.
\end{example}

The following theorem expands on this idea to give a general upper bound.

\begin{reptheorem}{thm:surgery_bound}
    Let $M$ be a closed, orientable 3--manifold given by surgery along a nontrivial $n$-component link $L\subset S^3$ with crossing number $c=c(L)$. Then 
    \begin{equation*}
        \volt(M)\leq \big(9c+15n-20\big)v_{oct}+4v_{tet}
    \end{equation*}
    where $v_{oct}\approx3.6638$ and $v_{tet}\approx1.01494$ are the volumes of a regular hyperbolic ideal octahedron and a regular hyperbolic ideal tetrahedron respectively.
\end{reptheorem}

\begin{proof}
	The link $L$ may not be hyperbolic. We first show how to construct a hyperbolic link $\bar L$ in $S^3$, so that the complement of $L$ is a Dehn filling of the complement of $\bar L$. In other words, the complement of $\bar L$ is the complement of a hyperbolic link in $M$, so by computing an upper bound for the volume of $\bar L$ we obtain an upper bound on the topological volume of $M$. Note that in general $L$ will not be a sublink of $\bar L$.
	
	To construct $\bar L$ we follow an algorithm due to Adams~\cite{Adams_Augmented}. In that process we keep track of the new crossing number. Following this algorithm more carefully in specific examples will usually improve the stated bound in the theorem. We now describe the algorithm. 
	
	\begin{enumerate}
		\item We start with a diagram $D$ of $L$ that has the minimal number of crossings $c=c(L)$. First, we introduce a circle (an augmentation) around each twist region of the link diagram. This introduces $4$ new crossings for every twist region. Since the number of twist regions is bounded from above by the number of crossings, we obtain a link diagram $D_1$, with at most $5c$ crossings, consisting of the old diagram $D$ and augmentations $C_1$ around each twist region of $D$.
		
		\item We remove or change crossings in the twist regions of $D$ until we get a diagram $D_2$, consisting of a diagram of an alternating link $A_2$ together with circles $C_2=C_1$ around each twist region of $A_2$. This does not increase the number of crossings and thus $D_2$ has at most $5c$ crossings. Note that here $A_2$ is no longer isotopic to our original link $L$. However by cutting along disks bounded by the components of $C_1$ and twisting, we see that the complement of $L$ arises as a Dehn filling of the complement of $D_2$, which is all we need.
		
		\item We add unknotted components to $A_2$ (that introduce no new crossings with the augmentations) to transform it into a non-split alternating diagram. This will add at most $4(n-1)$ additional crossings to the link diagram $D_2$ and at most $2(n-1)$ twist regions to $A_2$, and produce a link diagram $D_3$ with at most $5c+4n-4$ crossings that consists of a non-split alternating diagram $A_3$ together with some augmentations $C_3=C_2$.
		
		\item For each reducing sphere of the diagram $A_3$, we add one unknotted component to the diagram to get a non-split, prime, alternating diagram $A_4$. This can be done in such a way that the new unknotted components have no crossings with the augmentation circles. The diagram $A_3$ has at most $c+4n-4$ crossings and thus it contains at most $(c+4n-4)/3$ reducing spheres. The unknotted components can be added in such a way that we introduce for each unknotted component $4$ crossings and two additional twist regions. Thus we get a diagram $D_4$ consisting of a non-split, prime, alternating diagram $A_4$ together with augmentations $C_4$ around all but at most $(2c+14n-14)/3$ twist regions. The diagram $D_4$ has at most $(19c+28n-28)/3$ crossings.
		
		\item We add augmentations around the at most $(2c+14n-14)/3$ twists regions of $A_4$ that are not already augmented. This yields a diagram $D_5$ of a link $\bar L$ that is augmented alternating and has at most $9c+15n-15$ crossings.
		
	\end{enumerate}
	The construction ensures that the link $\bar L$ is augmented alternating. It is thus hyperbolic by a result of Adams~\cite{Adams_Augmented}. Hence    \begin{equation*}
		\volt(M)\leq\volh(\bar L).
	\end{equation*}
	The claimed inequality in the theorem statement follows from another result of Adams~\cite{Adams_Bound}, based on a construction by Weeks~\cite[Section 3]{handbookknottheory}, stating that for every hyperbolic link $J$ in $S^3$ with more than $4$ crossings, the volume is bounded from above by $(c(J)-5)v_{oct}+4v_{tet}$.
\end{proof}

\begin{remark}
For a specific given surgery presentation, the bound above can be greatly improved. For example, in the case that a closed, orientable 3--manifold $M$ is described as surgery on a knot $K$, the main result of \cite{BAR-altvolume} implies that $\volt(M)\leq 10(5c(K)-1)v_{tet}$. The key ingredient of \cite{BAR-altvolume} is a result of \cite{Blair-altaug}, showing that the complement of every knot $K\subset S^3$ contains an unknot $U$ so that the link $K\sqcup U$ is hyperbolic. In \cite{BAR-altvolume} it is shown that the hyperbolic volume of the link $K\sqcup U$ is bounded above by $10(5c(K)-1)v_{tet}$. Since $S^3\smallsetminus (K\sqcup U)$ is naturally a submanifold of $M$, our claim follows.
\end{remark}

The above bound can be applied to the standard surgery diagram of a Seifert fibered space. However, in this specific situation the above strategy can be improved as follows.

\begin{proposition}\label{cor:SFS_bound}
    Let $SFS(g;r_1,\ldots,r_N)$ be the Seifert fibered space over a closed surface of genus $g$ with Seifert invariants $(r_1,\ldots,r_N)$. Then 
    \begin{equation*}
        \volt(SFS(g;r_1,\ldots,r_N))\leq \begin{cases}
        	v_{oct}<3.67 \, \textrm{ if $(g,N)=(0,0)$ or $(0,1)$}\\
(10g+6N-9)v_{oct}+4v_{tet}< 37g+22N-28 \,\textrm{ otherwise.}
        \end{cases}
    \end{equation*}
\end{proposition}

\begin{proof}
Consider the standard surgery diagram of the Seifert fibered space $SFS(g;r_1,\ldots,r_N)$ shown in~\cref{fig:SFS}, see for example Section 6.1 in \cite{GS}. The surgery link is a connected sum of $g$ copies of the Borromean rings and $N$ copies of the Hopf link. Add $N+g-1$ many further unknots to that surgery diagram as indicated in \cref{fig:SFS} to obtain a connected prime alternating diagram of a link $L$ that contains the surgery link of $SFS(g;r_1,\ldots,r_N)$ as a sublink. Since $L$ also contains the Borromean rings as a sublink, it is not a torus link. Now a result of Menasco~\cite{Menasco84} implies that $L$ is hyperbolic.
	
	Since $SFS(g;r_1,\ldots,r_N)$ is obtained by surgery on $L$, the volume of $L$ is an upper bound on the topological volume of $SFS(g;r_1,\ldots,r_N)$. From~\cref{fig:SFS} we see that $L$ has crossing number $10g+6N-4$ and thus the result of Adams~\cite{Adams_Bound} mentioned above implies the stated bound.
\end{proof}

\begin{figure}[htbp] 
	\centering
	\def\svgwidth{\columnwidth}
	\begingroup
  \makeatletter
  \providecommand\color[2][]{
    \errmessage{(Inkscape) Color is used for the text in Inkscape, but the package 'color.sty' is not loaded}
    \renewcommand\color[2][]{}
  }
  \providecommand\transparent[1]{
    \errmessage{(Inkscape) Transparency is used (non-zero) for the text in Inkscape, but the package 'transparent.sty' is not loaded}
    \renewcommand\transparent[1]{}
  }
  \providecommand\rotatebox[2]{#2}
  \newcommand*\fsize{\dimexpr\f@size pt\relax}
  \newcommand*\lineheight[1]{\fontsize{\fsize}{#1\fsize}\selectfont}
  \ifx\svgwidth\undefined
    \setlength{\unitlength}{532.72735392bp}
    \ifx\svgscale\undefined
      \relax
    \else
      \setlength{\unitlength}{\unitlength * \real{\svgscale}}
    \fi
  \else
    \setlength{\unitlength}{\svgwidth}
  \fi
  \global\let\svgwidth\undefined
  \global\let\svgscale\undefined
  \makeatother
  \begin{picture}(1,0.3030013)
    \lineheight{1}
    \setlength\tabcolsep{0pt}
    \put(0,0){\includegraphics[width=\unitlength,page=1]{SFS.pdf}}
    \put(0.46684641,0.15399914){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$0$\end{tabular}}}}
    \put(0.37604205,0.18033997){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$0$\end{tabular}}}}
    \put(0.22612052,0.17981216){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$0$\end{tabular}}}}
    \put(0.1598761,0.17875652){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$0$\end{tabular}}}}
    \put(0.11006829,0.17770089){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$0$\end{tabular}}}}
    \put(0.04183159,0.17717307){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$0$\end{tabular}}}}
    \put(0.05378548,0.00493048){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$r_1$\end{tabular}}}}
    \put(0.12941184,0.00334703){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$r_2$\end{tabular}}}}
    \put(0.26837566,0.28097825){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$g$\end{tabular}}}}
    \put(0.8095995,0.28742205){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$g$\end{tabular}}}}
    \put(0.2285294,0.01918151){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$N$\end{tabular}}}}
    \put(0.33810661,0.0054583){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$r_N$\end{tabular}}}}
    \put(0.31129189,0.17928434){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$0$\end{tabular}}}}
    \put(0,0){\includegraphics[width=\unitlength,page=2]{SFS.pdf}}
    \put(0.76631286,0.02527104){\color[rgb]{0,0,0}\makebox(0,0)[lt]{\lineheight{1.25}\smash{\begin{tabular}[t]{l}$N$\end{tabular}}}}
    \put(0,0){\includegraphics[width=\unitlength,page=3]{SFS.pdf}}
  \end{picture}
\endgroup
	\caption{Left: The standard surgery diagram of a Seifert fibered space with genus $g$ and $N$ exceptional fibres. The surgery link is a connected sum of $g$ copies of the Borromean rings and $N$ copies of the Hopf link. Right: A hyperbolic link that contains the standard surgery diagram of a Seifert fibered space as a sublink.}
	\label{fig:SFS}
\end{figure}	

Although the bound from \cref{cor:SFS_bound} improves the general bound from \cref{thm:surgery_bound}, it is far from optimal. For example,  using SnapPy \cite{snappy} to compute the volume of $L$ for $g=2$ and $N=3$ gives a bound slightly smaller than $70$, while the upper bound from \Cref{cor:SFS_bound} is $112$.

\begin{proposition}
Let $M$ be a closed, orientable 3--manifold. Denote the Heegaard genus of $M$ by $g(M).$
There does not exist a function $f:~\mathbb{N} \to \mathbb{N}$ such that all 3--manifolds $M$ satisfy
        \begin{equation*}
            \volt(M)\leq f(g(M)).
        \end{equation*}
\end{proposition}

\begin{proof}
It suffices to demonstrate the existence of an infinite family of hyperbolic manifolds with unbounded volumes but bounded Heegaard genus. Indeed, there exist Berge knots with arbitrarily large volume~\cite[Theorem~4.1]{Baker_Berge_knots}. On the other hand, Berge knots have tunnel number one~\cite{Berge} and thus the knot exterior of a Berge knot has Heegaard genus $2$. Since Dehn surgery cannot increase the Heegaard genus, we obtain an infinite family of closed hyperbolic manifolds of Heegaard genus $2$ but arbitrarily large volume. 
\end{proof}

\begin{proposition}
    For a closed, orientable 3--manifold $M$, let $t(M)$ be the triangulation complexity of $M$, i.e. the minimal number of tetrahedra needed to triangulate $M$. 
 There exists an increasing function $f\colon \mathbb{N} \to \mathbb{N}$ such that for each $M$, we have
        \begin{equation*}
            \volt(M)\leq f(t(M)).
        \end{equation*}
\end{proposition}

\begin{proof}
This essentially follows from~\cite{My82}. For every triangulation of $M$, an explicit hyperbolic knot $K \subset M$ is constructed. From this construction we obtain an upper bound on the number of ideal tetrahedra needed to ideally triangulate the complement of $K$ in $M$. This bound only depends on the number of tetrahedra used to triangulate $M$, and not on the topology of $M$ or $M \setminus K$. The upper bound on the number of ideal tetrahedra gives an upper bound on the topological volume of $M$.
\end{proof}

\begin{remark}
	On the other hand, there is no function $f\colon \mathbb{N} \to \mathbb{N}$ that tends to infinity, such that 
	$$\volt(M) > f( t(M) ).$$
	This can be seen for example as follows. From \Cref{prop:lens-space-limit} we get that there exist infinitely many manifolds $M_n$ (lens spaces) with volt bounded by the volume of the Whitehead link. But since there are only finitely many manifolds with a given tetrahedral complexity $t$, it follows that $t(M_n)$ is unbounded. Thus such an inequality cannot exist. 
\end{remark}
