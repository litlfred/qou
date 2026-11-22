---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-004-rank-of-the-spherical-partition-algebra
section_title: "Rank of the Spherical Partition Algebra"
section_number: null
pages: 7-9
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.934
doc_brief: "On the spherical partition algebra — For k ∈N we introduce an idempotent subalgebra, the spherical partition algebra SPk, of the partition algebra Pk, that we define using an embedding associated"
---
\label{Rank of the}
As a $ \CC[x]$-module $ \SpheAlg $ is automatically free,
since $ \CC[x]$ is a PID 
and $ \SpheAlg $ is 
a submodule of the free $ \CC[x]$-module $ \ParAlg $, and hence torsion-free. 
Our first task is to determine the rank of $ \SpheAlg $. 

\medskip
For this, we first observe that any diagrammatic
representation of $ b \in \BiPar_k $ may be viewed 
as an element of 
$\SetPar_{2k} $. For example, for $ b  $ as in \eqref{dib3}, 
and hence $ \norm(b) $ as in \eqref{dib11}, we have
\begin{equation}
b = \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib12.pdf}}, \, \, \,  \, \, \, 
\norm(b) = \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib11.pdf}}
\raisebox{-6\height}{.}
\end{equation}
We next recall some results and conventions from \cite{Xi}.
For $ d \in  \SetPar_{2k}$ there is a canonical diagrammatic representation $ \normC(d) $ for $ d$
in which the propagating
blocks all appear with only one propagating line, which connects the leftmost points of the
corresponding top and bottom blocks. 
For example, for $ d $ as in \eqref{dib5}, we have
\begin{equation}\label{13}
d=   \raisebox{-.4\height}{\includegraphics[scale=0.8]{dib5.pdf}}, \, \, 
\normC(d) =   \raisebox{-.4\height}{\includegraphics[scale=0.8]{dib13.pdf}} 
\end{equation}
where we indicate with red and blue the two propagating blocks of $ \normC(d) $. 
For $l =0,1,2, \ldots, k $ we now let $  {\mathcal C}_l  $ 
be the set 
\begin{equation}\label{2.19}
  {\mathcal C}_l = \left\{ (d, S)  \,\middle\vert\, \begin{array}{l}
    d = (d_1, d_2, \ldots, d_p) \mbox{ is a set partition on } \{1,2,\ldots,k\} \mbox{ for } p \ge l \\
    S \subseteq \{ d_1, d_2, \ldots, d_p \} \mbox{ and } | S | = l
\end{array} 
  \right\}
\raisebox{-6\height}{.}
\end{equation}
Then, by \cite{Xi}, there is a bijection $ f $
\begin{equation}\label{bijection}
f:  \SetPar_{2k} {\, \, \cong \, \, }  \coprod_{l=0}^{k} { \mathcal C }_l  \times  \Si_l  \times { \mathcal C }_l \, . 
\end{equation}
For example, for $ d $ as in \eqref{13}, we have 
\begin{equation}
  f(d) = f(\normC(d) ) = 
  \big( ( d_1, {\color{red}{d_2}}, {\color{blue}{d_3}}), ( {\color{red}{d_2}}, {\color{blue}{d_3}}) \big) \times
  (1,2) \times   \big( (  {\color{blue}{d_1^{\prime}}}, d_2, {\color{red}{d_3^{\prime}}}, d_4^{\prime}), ( {\color{blue}{d_1^{\prime}}}, {\color{red}{d_3^{\prime}}}) \big)
\end{equation}
where, reading from left to right, $ d_1 = \{ 1 \} $,   $ {\color{red}{d_2}} = \{ {\color{red}{2,3,7,8,9}} \} $, corresponding to the first 
two intersection top blocks of $ d $, etc.

\medskip
We define $ \SetPar_{2k}^l   \subseteq \SetPar_{2k} $ as the set partitions whose 
diagrammatic representations
have exactly $ l $ propagating blocks and get that 
$ f $ induces a bijection $ \SetPar_{2k}^l  \cong 
{ \mathcal C }_l  \times  \Si_l  \times { \mathcal C }_l  $. 
\medskip

There are natural commuting left and right $ \Si_k $-actions on $\SetPar_{2k}^l  $ and so we also get   
left and right $ \Si_k $-actions on $ { \mathcal C }_l  \times  \Si_l  \times { \mathcal C }_l  $, via $ f$. 
These $ \Si_k $-actions on $ { \mathcal C }_l  \times  \Si_l  \times { \mathcal C }_l  $ are{\color{black}{,}} on the other
hand{\color{black}{,}} not
immediately  \lq visible\rq\, and so our first goal  
is to give another description of
$ { \mathcal C }_l  \times  \Si_l  \times { \mathcal C }_l  $ 
from which they can be read off. This
will be useful for describing a basis for $ \SpheAlg = e_k \ParAlg e_k$.

\medskip

Let $ \s,  \s_1, \T, \T_1 $ be row standard tableaux
whose shapes 
are compositions of $ k $, such that $ \s $ and $ \T $ are of length $ r $ whereas
$ \s_1  $ and $ \T_1 $ are of length $ r_1 $, where
$r $ and $ r_1  $ are both greater than or equal to $ l$. 
We then write $ (\s, \s_1) \sim_l  (\T, \T_1) $ if
$ (\s, \s_1) =  ( \rho \T, \rho_1 \T_1) $ where $ \rho $ and $ \rho_1  $
are \emph{row permutations} of $ \T $ and $ \T_1$, by which we mean 
that $ \rho $ and $  \rho_1  $ permute the rows of $ \T $ and $ \T_1 $ together with the numbers
appearing in them. 
We further require that
$ \rho $ and $  \rho_1  $
permute the first $ l $ rows of $ \T $ and $ \T_1 $ simultaneously, whereas 
they may permute the rows 
strictly below the $ l^{\color{black} \rm th} \, $row of $ \T$ and $ \T_1 $ independently.
In other words, $ \rho \in \Si_r $ and $  \rho_1 \in \Si_{r_1} $ and
$   \rho|_{ \{1, 2, \ldots, l \}} =  \rho_1|_{ \{1, 2, \ldots, l \}} $ where 
$ \rho|_{ \{1, 2, \ldots, l \}} $ and $ \rho_1|_{ \{1, 2, \ldots, l \}} $ 
denote the restrictions of $ \rho $ and $ \rho_1 $ to $ \{1, 2, \ldots, l  \} $. 
Here is an example with $  l= 3$. We indicate with red the separation of the top
$ l $ rows from the remaining lower rows of the tableaux. 
\begin{equation}\label{2.21}
  \left( \raisebox{-.5\height}{\includegraphics[scale=0.8]{dib38.pdf}} \right) \,  \sim_3 \, 
  \left( \raisebox{-.5\height}{\includegraphics[scale=0.8]{dib39.pdf}} \right) 
\raisebox{-39\height}{.}
\end{equation}
It is easy to check that $ \sim_l $ is an equivalence relation on pairs of row standard tableaux
of length greater than $ l $, 
and we define $ ( \s, \T )_{ \sim_l} $ as the equivalence class represented by $ ( \s , \T  ) $. 
Let $ i \mapsto {\rm min}_{\T}(i) $ be the function that gives the minimal (first)
number of the $ i^{\color{black} \rm th} $

row
of the row standard tableau $ \T $.
Then any class $  ( \s, \T )_{ \sim_l}  $ has a distinguished representative $  ( \s^{incr}, \T^{incr} ) $
for which $ {\rm min}_{  \s^{incr}}   $ is increasing on the restriction to $ \{1, \ldots, l \} $ 
and $ {\rm min}_{  \s^{incr}}   $ and $ {\rm min}_{  \T^{incr}}   $ are both increasing on the
restriction to $ \{l+1, l+2,  \ldots \} $. For example, in \eqref{2.21} the second pair
is the distinguished representative for its class. 

\medskip
Now $ {\rm min}_{  \T^{incr}}   $ need not be increasing on the restriction to $ \{1, \ldots, l \} $,
but there exists a row permutation $ \rho $ such that 
$ {\rm min}_{ \rho^{-1} \T^{incr}}   $ is increasing on the restriction to $ \{1, \ldots, l \} $. 
We may view $ \rho $ as an element of $ \Si_l$. For example, in \eqref{2.21} we have
$ \rho = (1,3,2) $ in permutation notation. But $ \rho $ only depends on $ (\s, \T ) $ through its 
class $ ( \s, \T )_{  \sim_l } $, 
and so we
define $\rho_{  ( \s, \T )_{ \sim_l }} =  \rho   $. 

\medskip
We next observe that any element $  d $ of $\SetPar_{2k}^l  $
gives rise to a class $ ( \s, \T  )_{\sim_l} $, by associating the intersection top blocks of $ d $ with the rows of 
$ \s $ and the intersection bottom blocks of $ d $ with the rows of $ \T $, in such a way that 
intersection top and bottom blocks that are intersections of propagating blocks for $ d $
are associated with 
the first $ l $ rows of $ \s $ and $ \T $, and with rows of the same 
row number 
if and only {\color{black}{if}} they are intersections of the same propagating block. For example, for $ d$ as in
\eqref{13} the corresponding
class is 
\begin{equation}\label{2.22}
  \left( \raisebox{-.5\height}{\includegraphics[scale=0.8]{dib40.pdf}} \right)_{ \! \! \sim_2}
\raisebox{-28\height}{.} 
\end{equation}



One notes that the association just defined is a bijection between $\SetPar_{2k}^l  $ and
the set of classes $ ( \s, \T )_{ \sim_l } $. 
Note also that the $ \Si_k $-actions on
$ \SetPar_{2k}^l  $, under this bijection, correspond to the natural $ \Si_k $-actions on $  \s $ and $ \T $, 
as explained in \eqref{dib17}, although the action on $ \T $ should be chosen as a right action. 




There is however also an obvious bijection between the set of classes $ ( \s, \T )_{\sim l} $ and 
$  { \mathcal C }_l  \times  \Si_l  \times { \mathcal C }_l  $. It maps $  ( \s, \T )_{\sim l} $ to
$ (d_\s, S_\s)  \times \rho_{ ( \s, \T )_{\sim l} }  \times (d_\T, S_\T) $ where $ d_\s $ is the set partition 
whose blocks are the rows of $ \s $, with $ S_\s $ being the blocks of the first $ l $ rows of $ \s $, 
and similarly for $ d_\T $ and $ S_\T $. Combining this with the bijection of the previous paragraph we have
achieved our goal of describing the $ \Si_k $-actions on
$  { \mathcal C }_l  \times  \Si_l  \times { \mathcal C }_l  $. 



\medskip
We now use it to prove the following Theorem. 
\begin{theorem}\label{lemma2}
  The map $ F: \BiPar_k \rightarrow \SpheAlg$ given by $ b \mapsto e_k{\normalfont
    \norm(b)} e_k $ is injective. Moreover,
  the image of $ F $, that is
$ im  F =  \{ e_k {\normalfont \norm(b)} e_k \, | \, b \in \BiPar_k \} $, is a $\CC[x]$-basis for $ \SpheAlg $ and 
so $ \rank_{\CC[x]} \,  \SpheAlg = bp_k$. 
\end{theorem}
\begin{dem}
We first show simultaneously that $ F $ is injective and that $ im F $ is a linearly independent set. 
Let $ b \in \BiPar_k $ and consider 
$  \norm(b) $ as an element of $ \SetPar_{2k} $. Let $  ( \s, \T )_{\sim_l} $ be the class associated with
$  \norm(b) $ under the bijection explained in the paragraph before \eqref{2.22} and
let $  ( \s^{incr}, \T^{incr} ) $ be its distinguished representative, 
as defined above. Here is an example
\begin{equation}\label{2.22new}
( \s^{incr}, \T^{incr} ) =   \left\{ \raisebox{-.5\height}{\includegraphics[scale=0.8]{dib41.pdf}} \right\}
\raisebox{-45\height}{.} 
\end{equation}
Two properties can be observed in \eqref{2.22new} and hold for general $ ( \s^{incr}, \T^{incr} )$. 
\begin{itemize}
    \item[I.] We have $ \rho_{ (  \s, \T )_{\sim l} } = 1 $ and so $ \T^{incr} $ is the \emph{row reading tableau},
in which the numbers $ \{ 1,2,\ldots, k \} $ appear in order from left to right down the rows. Or, equivalently, 
$ {\rm min}_{  \T^{incr}}   $ is an increasing function.
\item[II.] Let $ \lambda $ be the shape of $ \s^{incr} $.  
Then $ {\rm min}_{  \s^{incr} }   $ is also increasing, but only upon restriction to
subsets $ I  $ of the row indices for $ \lambda $, for which
$\{  \lambda_i | i \in I \} $ is constant.
\end{itemize} 




Using

{\color{black}{these properties,}}
we may now argue as follows. 
Let $ \sigma, \sigma_1 \in \Si_k $ and suppose that $ \sigma \norm(b) \sigma_1 $ is of
the form $ \norm(b_1 ) $ for some $ b_1 \in \BiPar_k $. Then, passing to the pair $ ( \s^{incr}, \T^{incr} ) $
and using the properties, one sees that the only way
to obtain a{\color{black}{n}} element in normal form by acting
$ \sigma $ on $\s^{incr}$ and $ \sigma_1 $  on $\T^{incr}$ is that these two simultaneous actions only
interchange numbers appearing in the same row. 
With this, 
we deduce that 
$ b = b_1 $. 
In other words, $ \norm(b)$ is the only element
from $ \BiPar_k $ in normal form that appears in the expansion of $ e_k \norm(b) e_k $.
But this implies
that $ F $ is injective and that 
$ im F  $ is a linearly independent set, as claimed. 

\medskip
In order to prove that $ im  F $ is a spanning set, it is enough to show that  
$ e_k d e_k $ belongs to $ im  F $ for any $ d \in \SetPar_{2k} $. 
Let therefore $ ( \s, \T )_{\sim_l } $ be the class for $ d $ under
the bijection constructed before \eqref{2.22}. We first  
choose row permutations $ \rho $ and $ \rho_1 $
satisfying the conditions described in the paragraph before \eqref{2.21}, such that
$ (\rho \s, \rho_1  \T )  $ has the shape of an element corresponding to $ \norm(b) $ 
under the bijection, for some $ b \in \BiPar_k $. To be precise, 
by \eqref{lexi} this means that,
when restricted to the top $ l $
rows, the shape of $ \rho \s $ is a partition, and so are the shapes of $ \rho \s $ and $ \rho_1 \T $,
when restricted to the 
rows strictly below the $ l^{\color{black} \rm th} \,$th row, whereas $ \rho_1 \T $ is only a partition on 
the restriction to the the equally sized rows of $ \sigma \s $. Note that 
$ ( \s, \T )_{\sim l} = ( \rho \s, \rho_1 \T )_{\sim l} $. But we may at this stage choose $ \sigma, \sigma_1 \in \Si_k $
such that $ ( \sigma  \rho \s, \sigma_1 \rho_1 \T ) $ is the distinguished representative of $ \norm(b) $, for
some $ b \in \BiPar_k $ as described below \eqref{2.22new}, which shows the claim.

\end{dem}
