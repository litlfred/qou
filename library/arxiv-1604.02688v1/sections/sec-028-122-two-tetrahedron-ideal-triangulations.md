---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-028-122-two-tetrahedron-ideal-triangulations
section_title: "Two tetrahedron ideal triangulations"
section_number: 12.2
pages: 42-44
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.771
latex_coverage_ratio: 0.816
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Up to relabelling, there are 10 triangulations of orientable cusped 
3-manifolds that decompose into two tetrahedra, and these 10 triangulations 
correspond to seven manifolds up to homeomorphism. The relevant data are 
presented in Table \ref{tab:twoTetCensus}.

\begin{table}[ht]
\begin{tabular}{|c|c|c|}
\hline
signature & name & 1-efficient\\
\hline
\hline
cMcabbgds & {\bf $S^1\times D^2$} & Yes\\
\hline
cMcabbgij &$S^1\times D^2$ & Yes\\
\hline
cMcabbgik &$S^1\times D^2$ & Yes\\
\hline
\hline
cPcbbbalm &{\bf $SFS[D^2(3,1)(3,1)]$} & Yes\\
\hline
\hline
cPcbbbali &{\bf $SFS[D^2(3,1)(3,2)]$} & Yes\\
\hline
\hline

cPcbbbadh &{\bf $SFS[D^2(2,1)(3,1)]$} & Yes\\
\hline
cPcbbbadu &{\bf $SFS[D^2(2,1)(3,1)]$} & Yes\\
\hline
\hline
cPcbbbdxm& {\bf Figure 8 sister (m003)} & Yes\\
\hline
\hline
cPcbbbiht &{\bf Figure 8 (m004)} & Yes\\
\hline
\hline
cPcbbbdei &{\bf $SFS[D^2(2,1)(3,1)] \cup SFS[A^2(2,1)]$} & No \\
\hline

\end{tabular}
\caption{\label{tab:twoTetCensus} The complete census of ideal 
triangulations with two tetrahedra. The homeomorphism descriptions come 
from an appeal to the surgery description given by Martelli and Petronio 
\cite{MP},  (which the diligent reader can verify using a tangle computation). 
}
\end{table}

\break
\noindent
{\bf Some Pachner Paths.} 

To provide a certificate of a path in the Pachner graph we list the 
vertices and also provide the face consumed by a 2-3 move or the edge 
consumed by a 3-2 move. In the first case, we take the index of the face 
in the labelled triangulation determined by the isomorphism signature. 
In the second, we take $-index -1$ of the edge (the minus sign indicates 
that an edge is being consumed and shifting by $-1$ removes the ambiguity 
of $-0$ and $+0$ that would arise if we were required to perform a 3-2 
along edge 0). 

\begin{ex} 
{\bf Solid Torus.} 
The (open) solid torus has 3 minimal ideal triangulations with 2 tetrahedra. 
The paths shown in Table \ref{solid_torus_paths}
are 1-efficient paths in the Pachner graph
connecting these minimal triangulations. 

\begin{table}[ht]
\begin{tabular}{|c|c||c|c||c|c|}
\hline
Path 1 & & Path 2 & & Path 3& \\
\hline
isoSig & 2-3 move &isoSig & 2-3 move&isoSig & 2-3 move\\
\hline
`cMcabbgds' & 0 &`cMcabbgds'& 0&`cMcabbgij' & 0\\
 \hline
 `dLQbcccaego' & 0 & `dLQbcccaego' & 4 &`dLQbcccahgc'& 5\\
\hline
`eLPkbcdddhgcgj'& -3 & `eLPkbcdddhcgcf' & -2 &`eLAkbccddaegtr' & -3\\
\hline
`dLQbcccahgc' & -3 & `dLQacccjrgr' & 2 & `dLQbcbcaekv'& 2\\
\hline
`cMcabbgij' & `end' & `eLPkbcdddhcgbf'& -1 & `eLAkbccddaegtn' & -4\\
\hline
- & - & `dLQbcccahgo' & -3 & `dLQbcccahgo'& -3\\
\hline
- & - & `cMcabbgik' & `end' & `cMcabbgik' & `end'\\
\hline
\end{tabular}
\caption{\label{solid_torus_paths}Some 1-efficient paths for 
triangulations of the solid torus}
\end{table}
\end{ex}

\begin{rmk} 
This analysis shows that the 1-efficient Pachner graph (of ideal 
triangulations) of the solid torus is not connected. Specifically, we can 
say the following: Both `gLLAQbecefefaaopaaj' and `gLLAQbecefefaaopaan' are 
six tetrahedral triangulations of the solid torus that 
1) have no degree 3 edges and 2) each 2-3 move along a face in either 
triangulation results in a not 1-efficient triangulation. 
However, we can still relate the 3D-index to the 3D-index of the 
triangulations of the solid torus in Table \ref{tab:twoTetCensus}. 
In fact, both of these six tetrahedral triangulations have (three) degree 
two edges. After performing a 2-0 move on any degree two edge of one of 
these triangulations, the resulting triangulation is 1-efficient 
and connected to the triangulation  `cMcabbgij' via a path of 1-efficient 
triangulations. Therefore, the 3D-index is consistent with the two 
tetrahedral triangulation of an ideal solid torus `cMcabbgij' 
by \cite[Theorem 5.1]{GHRS}. 
\end{rmk} 

\begin{ex}
{\bf Trefoil Complement.} The trefoil complement ($SFS[D^2(2,1)(3,1)]$) 
has two minimal triangulations that are connected along a path of length 
6 (see Figure \ref{fig:chartPPTrefoil} and Table \ref{tab:ppTrefoil}) and 
a 1-efficient path of length 12 (see Figure \ref{fig:chartPPTrefoil} and 
Table \ref{tab:ppOETrefoil}).

\begin{figure}[htpb!]
\resizebox{16 cm}{!}{\xymatrix{
g\ar@{..}[rrrrr]    &&&& & O_4\ar@{-}@[red][dr]\ar@{..}[rrrr]  &&&& 
O_8\ar@{-}@[red][dr]\ar@{..}[rrrrr]  &&&&& 6\\
f\ar@{..}[rrrr]    &&&& O_3\ar@{-}@[red][ur]\ar@{..}[rr]  & 
&O_5\ar@{-}@[red][dr]\ar@{..}[r]& T_3\ar@{-}@[green][drr]\ar@{..}[r] 
& O_7\ar@{-}@[red][ur]\ar@{..}[rr] & &O_9\ar@{-}@[red][dr]\ar@{..}[rrrr] 
&&&&5\\
e\ar@{..}[rrr]  & & & O_2\ar@{-}@[red][ur]\ar@{..}[rr] & & 
T_2\ar@{-}@[green][urr]\ar@{..}[rr]  & &
O_6\ar@{-}@[red][ur]\ar@{..}[rr]\ar@{--}@[blue][ddrrrrrr]&&
T_4\ar@{-}@[green][drr]\ar@{..}[rr] &&O_{10}\ar@{-}@[red][dr]\ar@{..}[rrr] 
&&& 4\\
d\ar@{..}[rr] & & O_1 \ar@{-}@[red][ur]\ar@{..}[r] & 
T_1 \ar@{-}@[green][urr] \ar@{..}[rrrrrrrr] & &&&&&&&
T_5\ar@{-}@[green][drr]\ar@{..}[r] & O_{11}\ar@{-}@[red][dr]\ar@{..}[rr] 
&&  3\\
c\ar@{..}[r] &T_s  \ar@{-}@[red][ur]\ar@{.}[rrrrrrrrrrrr] 
\ar@{-}@[green][urr] \ar@{--}@[blue][uurrrrrr]  & &&&&&&&&&&& 
T_f\ar@{..}[r]  & 2
}
}

\caption{\label{fig:chartPPTrefoil} A shortest Pachner path between 
minimal triangulations of the trefoil (green) and a longer 1-efficient 
path (red). Note, the 1-efficient path is a shortest path through 
1-efficient triangulations using 2-3/3-2 moves. If 0-2/2-0, moves are 
allowed then the red and green paths shorten to $\{T_s, O_6, T_f\}$ (blue 
dashed). Also, a computation in Regina shows all triangulations on the 
green path except $T_s$ and $T_f$ are not 1-efficient.
} 
\end{figure}

\begin{table}
\begin{tabular}{|c|c|c|}
\hline
Figure name & isoSig & move \\
\hline
$T_s$ & `cPcbbbadh' & 2\\ 
\hline
$T_1$ & `dLQacccbgjs' & 1\\
\hline
$T_2$ & `eLPkbcdddacrnn' & 4\\
\hline
$T_3$ & `fvPQccdedeeccvbfb' &  -1\\ 
\hline
$T_4$ & `eLPkbcdddackjj' &  -2\\ 
\hline
$T_5$ & `dLQacccbgbk' & -3 \\
\hline
$T_f$ & `cPcbbbadu' & `end'\\
\hline
\end{tabular}
\caption{\label{tab:ppTrefoil} A shortest Pachner path between the two 
minimal triangulations of the trefoil complement.}
\end{table}

\begin{table}
\begin{tabular}{|c|c|c|}
\hline
Figure name & isoSig & move \\
\hline
$T_s$ & `cPcbbbadh' & 1\\ 
\hline
$O_1$ & `dLQacccjgjb' & 5\\ 
\hline
$O_2$ & `eLAkbbcdddugaj' & 2\\
\hline
$O_3$ & `fLLQcccddeeabvnln'& 5\\ 
\hline
$O_4$ & `gLvQQadfeeffjatxcfj' & -5\\ 
\hline
$O_5$ & `fLAPcacceeejgjffc' & -3 \\
\hline
$O_6$ & `eLMkbbdddadiih' & 0\\
\hline
$O_7$ & `fLAPcacceeejgjcrc' & 6\\
\hline
$O_8$ & `gLvQQadfeeffjaaxcfj'& -4\\  
\hline
$O_9$ &`fLLQcccddeeabvrln'& -4\\ 
\hline
$O_{10}$ & `eLAkbbcdddurar'& -2 \\
\hline
$O_{11}$ & `dLQacccjgjs'&-3 \\
\hline
$T_f$ & `cPcbbbadu' & `end'\\
\hline
\end{tabular}
\caption{\label{tab:ppOETrefoil} A shortest one-efficient Pachner path 
between the two minimal triangulations of the trefoil complement.}
\end{table}
\end{ex}
