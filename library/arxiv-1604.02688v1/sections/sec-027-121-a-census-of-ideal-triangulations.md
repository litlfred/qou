---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-027-121-a-census-of-ideal-triangulations
section_title: "A census of ideal triangulations"
section_number: 12.1
pages: 41-42
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.955
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
These examples were obtained by first compiling a list of all ideal 
triangulations with at most six tetrahedra using Regina's {\tt tricensus} 
function. Then it was determined if these triangulations were solid tori. 
Of the remaining triangulations, we then (i) determined their irreducibility 
and (ii) checked for incompressible tori and Klein bottles. The first 
condition was checked using a light adaptation of Regina's 
{\tt isThreeSphere} function and the second determined using Regina's 
{\tt isSolidTorus} and a new function {\tt isT2xI} (see \cite{regina}). 
The latter function is similar to Haraway's 
algorithm \cite[Corollary 15]{haraway2014determining}, but instead of 
using an analysis of spun normal  annuli, it relies on the fact that if 
$M$ is a 2-cusped manifold with three $S^1\times D^2$ surgeries along 
slopes $\{\gamma_1,\gamma_2,\gamma_3\}$, then $M$ is homeomorphic to 
$T^2 \times I$ the Berge manifold \cite{berge1991knots,gabai1989surgery}, 
or is Seifert fibred over the annulus with one exceptional fibre. However, 
all of the $S^1\times D^2$ fillings of the Berge manifold are 
pairwise distance one from each other, and so if a manifold admits 
$S^1\times D^2$ fillings along slopes 
$\{\frac{1}{0}, -\frac{1}{1}, \frac{2}{1}\}$ 
then it must be $T^2\times I$ or Seifert fibred over the annulus. 
The latter can be ruled out since at least one of the fillings 
$\{\frac{1}{0}, -\frac{1}{1}, \frac{2}{1}\}$ will result in a Seifert 
fibred space over the disk with two (non-trivial) exceptional fibres.

This allows for a decomposition into prime and atoroidal pieces. Those 
pieces were then classified by searching the Pachner graph of the 
corresponding triangulations and simplifying the triangulation to that 
of either a Snappy {\tt OrientableCuspCensus} triangulation (using 
SnapPy's {\tt identify} function) or until it was equivalent via Pachner 
moves to a known triangulation of a lens space (in the case of some prime 
summands) or a cusped Seifert fibered space (using a dictionary of 
triangulations also included with the code). While a larger library of 
closed triangulations would be needed for more complicated prime and 
JSJ decompositions, this was sufficient for our purposes. 

After this coarse classification, the triangulations were then analysed 
for 1-efficiency. The results of this census are summarised in 
Tables \ref{table:smalltetcensus} and \ref{hypCensus} below;
the code used is available as an ancillary file to the arxiv version 
of this paper. 

\begin{table}[h]
\begin{tabular}{|c|c|c|c|c|c|c|c|c||c|c|}
\hline
n &	total& 	$S^1\times D^2$ &	$T^2 \times I$	& $P \times S^1$ &	Red.	& Tor. &	SFS & Hyp. &Taut	&1-efficient\\
\hline
2&	10&	   3&	    0&	  0&	0&	1&	 4&	2&	7&	9\\
\hline
3&	129&	   65	&    1&	  0&	0&	15&	 36&	12&		53&	102\\
\hline
4&	1852& 917& 11& 0&	107&	188& 	491&	138&		441&	1082\\
\hline
5 &26909&	14324&	197&	1&	2533& 	2164&	6344&	1346& 3310 &	12130\\
\hline
6&414946  &219080 &2981 & 32& 58508& 29451& 89933 &14961 &134538 & 28405  \\
\hline
\end{tabular}

\caption{\label{table:smalltetcensus} This table provides information on 
the various types of (orientable) ideal triangulations that can be built 
from $n=2,3,4,5,6$ tetrahedra. Total is the total number of triangulations 
for each value of $n$, $S^1\times D^2$ is the number of solid tori, 
similarly for $T^2\times I$ and $P\times S^1$. Red.~counts the number of 
reducible manifolds and Tor.~counts the number of toroidal manifolds which 
are not homeomorphic to $SFS[D(2,1)(2,1)]$. Instead $SFS[D(2,1)(2,1)]$ is 
counted in SFS which record the number of SFS over the disk or annulus 
with two or one exceptional fibres respectively. Finally, Hyp.~counts the 
number of hyperbolic manifolds observed. Note that in each case, this 
computation is rigorous, in the sense that the triangulation was connected 
to a known triangulation via Pachner moves. Finally, Taut records the number 
of triangulations admitting a taut angle structure and 1-efficient records 
the number of 1-efficient triangulations.}
\end{table}

\begin{table}[h]
\begin{tabular}{|c|c|c|c|c|c|c|c|}
\hline
n & Hyp. &Geom. &Semi-Geom. & Strict Ang. Struct. & Semi-Ang.&  Taut & 1-efficient\\
\hline
2&	2&	  2&	    2&	  2 &2 &2 &2\\
\hline
3&	12& 12 & 12 & 12& 12& 12&12\\
\hline
4&	138& 110& 121 & 119 & 134 & 134 & 134\\
\hline
5&	1346&670&798&801&1165 & 1118&1190\\
\hline
6&	14961&3857&4923&5221&10908&9927&11512\\
\hline
\end{tabular}

\caption{\label{hypCensus} This table provides data on the ideal 
triangulations of hyperbolic manifolds in the census. Hyp.~gives the 
total number of hyperbolic manifolds. Geom.~gives the number of 
triangulations which SnapPy found an approximate hyperbolic structure 
and Semi-Geom.~records the number of triangulations which SnapPy found 
an approximate hyperbolic structure possibly with flat (and non-degenerate) 
tetrahedra. Strict.~Ang.~Struct.~records the number of triangulations 
admitting a strict angle structure, while Semi-Ang.~records the number of 
triangulations admitting a semi-angle structure. Finally, Taut records the 
number of triangulations admitting a Taut structure and 1-efficient records 
the number of 1-efficient triangulations of hyperbolic manifolds.}
\end{table}
