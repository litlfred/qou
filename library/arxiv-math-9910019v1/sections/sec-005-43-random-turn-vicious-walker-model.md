---
doc_id: arxiv-math-9910019v1
doc_title: "Symmetrized random permutations"
section_id: sec-005-43-random-turn-vicious-walker-model
section_title: "Random turn vicious walker model"
section_number: 4.3
pages: 11-12
source_pdf: 9910019v1.pdf
source_sha256: 07dd7ab7068b1482
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.991
doc_brief: "Symmetrized random permutations — 8 sections: Front matter; Introduction; Tracy-Widom distribution functions"
---
Random permutations and random involutions arise also in certain random 
walk process in a one dimensional integer lattice.
We call a particle left-movable (resp. right-movable) 
if its left (resp. right) site is vacant.
Initially, $p$ particles are located at the points $1,2,3,\cdots,p$.
At each time step $t$ ($t=1,2,\cdots$), 
one particle 
among the left-movable particles 
is selected at random,  
and is moved to its left site
(so at $t=1$, the leftmost particle is moved.)
Suppose this process is repeated for $n$ time steps. 
It is found that \cite{forrester99}
there is a bijection between all the possible configurations 
and the set of Young tableaux with at most $p$ rows of size $n$ : 
simply, in the $k^{\text{th}}$ row, write the times 
when the particle is originally at the point $k$ (see Figure \ref{fig-walk}).
\begin{figure}[ht]
 \centerline{\epsfig{file=walk.eps, width=13cm}}
 \caption{random turn vicious walkers and Young tableaux}
\label{fig-walk}
\end{figure}
In this correspondence the number of moves made by the $k^{\text{th}}$ 
particle (counted from the left) is the number of boxes 
in the $k^{\text{th}}$ row of the corresponding Young tableau.
If we take the limit $p\to\infty$, we remove the constraint 
on the number of rows. 
In other words, we start with countably many particles located at 
$1,2,3,\cdots$ and at each 
time step, we move a randomly selected left-movable particle 
to its left site.
Then the statistics of the number of moves made by the leftmost particle 
in $n$ time steps 
is identical to that of the number of boxes 
in the first row of a random Young 
diagram under the probability $M^1_n$ (or the length of the longest 
increasing subsequence of a random involution).
Hence in the large $n$ limit, we obtain GOE fluctuation.

Now suppose after $n$ steps of left moves, 
by taking $n$ steps of right moves, 
we want the particles brought back to their original positions.
The first $n$ steps gives a Young tableaux and the next $n$ step gives another 
Young tableaux.
So we are in the situation of pairs of Young tableaux, i.e. $\beta=2$ case.
Especially if the number of particles are infinite, 
the statistics of the moves made by the leftmost 
particle is identical to the length of the longest increasing 
subsequence of a random permutation : GUE fluctuation
\cite{forrester99}.
