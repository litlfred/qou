---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-003-the-partition-algebra-and-the-spherical-partitio
section_title: "The partition algebra and the spherical partition algebra"
section_number: null
pages: 6-7
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.941
doc_brief: "On the spherical partition algebra — For k ∈N we introduce an idempotent subalgebra, the spherical partition algebra SPk, of the partition algebra Pk, that we define using an embedding associated"
---
\label{The partition algebra}
We next recall the partition algebra $ \ParAlg$; it was 
introduced by the second named author via considerations
in statistical mechanics, see \cite{PMartin}.
Let $ \SetPar_k $ be the set of set partitions on $ \{ 1,2 \ldots, k \} $, 
that is the set of equivalence relations
$ d $ on $ \{ 1,2 \ldots, k \}$. For even subscript $ 2 k $ we
shall usually think of $ \SetPar_{2k} $ as set partitions on $ \{ 1,2 \ldots, k \} \cup 
\{ 1^{\prime},2^{\prime} \ldots, k^{\prime} \}$. 
If $ d \in \SetPar_{k} $ we
write $ d = \{ d_1, d_2, \ldots, d_a   \} $ where the $ d_i $'s are the classes, or {\it blocks}, of $ d $.
If furthermore $ d \in \SetPar_{2k}$, we represent $d$ diagrammatically using two parallel
horizontal lines of points,
just as for elements of $\BiPar_k$, but this time labeling the top points
$ \{ 1, 2, \ldots, k\} $ and the bottom points $ \{ 1^{\prime}, 2^{\prime}, \ldots, k^{\prime}\} $,
from left to right. We draw lines between these points in such a way that the connected components,
in {\color{black}{the graph-theoretic}} sense, 
of the corresponding graph are exactly the blocks of $ d $, for example
\begin{equation}\label{dib5}
  \{ \{1\}, \{2,3, 7,8,9, 6^{\prime}, 7^{\prime}, 8^{\prime}\}, \{ 4,5,6,1^{\prime}, 2^{\prime}\},
\{ 3^{\prime}, 4^{\prime}, 5^{\prime} \}, 
  \{ 9^{\prime} \}
     \} \,  \mapsto  \,  \raisebox{-.4\height}{\includegraphics[scale=0.8]{dib5.pdf}}
\raisebox{-4.3\height}{.}
\end{equation}
Note that, just as for elements of $\BiPar_k$, this diagrammatic representation of $ d \in \SetPar_{2k} $ is
not unique.

For $ d = \{ d_1, d_2, \ldots, d_a \} \in \SetPar_{2k} $, we say that a block $ d_i $ is {\it propagating}
if $ d_i \cap \{ 1,2, \ldots, k  \} \neq \emptyset $ and 
$ d_i \cap \{ 1^{\prime},2^{\prime}, \ldots, k^{\prime}  \} \neq \emptyset $. 
If $ d_i \cap \{ 1,2, \ldots, k  \} \neq \emptyset $ we say that $ d_i \cap \{ 1,2, \ldots, k  \}$
is an \emph{intersection top block} for
$d $ and if $ d_i \cap \{ 1^{\prime},2^{\prime}, \ldots, k^{\prime}  \} \neq \emptyset $
we say that $ d_i \cap \{ 1^{\prime},2^{\prime}, \ldots, k^{\prime}  \} $ is an \emph{intersection
  bottom block} for $d $. 





\medskip
{\color{black}{We define $ \ParAlg$ as the $ \CC[x]$-algebra that, as a $ \CC[x]$-module,}} is free on  
$ \SetPar_{2k} $, and that has multiplication defined as follows. For elements
$ d, d_1 \in \SetPar_{2k} $, let $ d \circ_1 d_1 $ be the concatenation 
of $ d $ and $ d_1 $ with $ d$ on top of $ d_1$. There may be one or several \lq internal\rq\ connected components
of $ d \circ_1 d_1 $, 
that is components that do not intersect any of the top or bottom points of $ d \circ_1 d_1 $. 
Let $ d \circ_2 d_1 $
be the diagram obtained from $ d \circ_1 d_1 $ by removing these $ N $, say, internal 
components. There may still one or several \lq internal points\rq\ of $ d \circ_2 d_1 $, that is points that are
neither top or bottom points of $ d \circ_2 d_1 $, and we let $ d \circ_3 d_1 $
be the diagram obtained from $ d \circ_2 d_1 $ by eliminating these points. 
We may now view $ d \circ_3 d_1 $ as the diagram of a set partition and 
the product in $ \ParAlg $ of $ d $ and $d_1 $ is defined as $ d d_1 = x^N d \circ_3 d_1 $. 
The product of two general elements of $ \ParAlg $ is defined
{\color{black}{by the linear extension of the multiplicative operation we have defined.}} 

\medskip
For example, if
\begin{equation}\label{components}
  d=  \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib6.pdf}},\, \,\, \,\, \,
  d_1=  \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib7.pdf}}
\end{equation}
we have that 
\begin{equation}
  d d_1 =  \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib8.pdf}}=\, \,\, 
     x^3 \,  \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib9.pdf}}
\raisebox{-6\height}{.}
\end{equation}
One checks that this rule gives rise to a well-defined associative 
multiplication on $  \ParAlg$, in other words, $ d d_1 $ does not depend on the choices of
diagrammatic representations for $ d $ and $ d_1 $. 

\medskip

For any $ t \in \CC $ we define the specialized partition algebra 
$\ParAlg(t) =  \ParAlg \otimes_{\CC[x] } \CC $ where $ \CC $ is made into an $ \CC[x] $-algebra
via $ x \mapsto t $. 

\medskip
As is well known, $ \Si_k $ is a Coxeter group on generators $ S = \{s_1, s_2, \ldots, s_{k-1} \} $
where $ s_i $ is the simple transposition $ s_i = (i,i+1) $.
Let $\CC[x] \Si_k $ be the group algebra for $ \Si_k $ over $ \CC[x] $. Then 
there is a natural algebra inclusion $ \iota_k:  \CC[x] \Si_k \xhookrightarrow{} \ParAlg $
given by 
\begin{equation}\label{dib10}
  s_i  \mapsto  \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib10.pdf}}
\raisebox{-5\height}{.}
\end{equation}
Let $ \displaystyle e_k = \iota_k\left ( \dfrac{1}{k! } \sum_{ \sigma \in \Si_k } \sigma\right)  $. 
Then $ e_k $ is an idempotent of $ \ParAlg $. We use it to introduce the protagonist
of the present paper. 
\begin{definition}
  The spherical partition algebra $\SpheAlg $ is defined as the idempotent truncation
  of $ \ParAlg $ with idempotent $ e_k $, that is
\begin{equation}
 \SpheAlg = e_k \ParAlg e_k. 
\end{equation}
Similarly, for $ t \in \CC $ we define the specialized spherical partition algebra
$\SpheAlg(t) $ as $\SpheAlg(t) = e_k \ParAlg(t) e_k  $. 
 \end{definition} 
Note that $\SpheAlg $ is a subalgebra of $ \ParAlg $, but not a unital subalgebra, since
the one-element for $\SpheAlg $ is $ e_k $, and similarly for $ \SpheAlg(t) $.
