---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.782
latex_coverage_ratio: 0.951
doc_brief: "On the spherical partition algebra — For k ∈N we introduce an idempotent subalgebra, the spherical partition algebra SPk, of the partition algebra Pk, that we define using an embedding associated"
---
The {\it partition algebra} $ \ParAlg  $ arose around thirty years ago 
in the second named author's work on the Potts model in statistical mechanics, 
see \cite{PMartin}. 
Since then it has been understood that $ \ParAlg $ is in fact connected 
with many other areas of mathematics
and physics, including Deligne's category $ \underline{\rm Rep}(S_t) $, 
the Kronecker problem in the representation theory of 
the symmetric group, Schur algebras, and symmetric function theory, see for example
\cite{BOdV}, \cite{CO}, \cite{MartinWoodcock}, \cite{OrellanaZabrocki}.

\medskip
By definition, $ \ParAlg $ is a $\CC[x]$-algebra with basis
indexed by the 
set partitions on $  \{ 1,2 \ldots, k \} \cup 
\{ 1^{\prime},2^{\prime} \ldots, k^{\prime} \}$.
{\color{black}{There are many important 
subalgebras of the partition algebra, including
the half-integer partition algebra}}, the quasi-partition algebra,
the Temperley-Lieb algebra, the Motzkin algebra, 
the Brauer algebra, the quasi-Brauer algebra, the Rook algebra, the group algebra of
the symmetric group $\Si_k $, and so on,
see for example \cite{CST}, \cite{OrellanaDaugherty}, \cite{Scrimshaw} and references therein,
and it is also closely related to the $bt$-algebra of knot theory, see 
\cite{AicardiJuyumaya}, \cite{ArcisEspinoza}, \cite{Banjo}, \cite{ERH}, \cite{RH1}, \cite{RH2}. 
  
\medskip
In the present paper we introduce and study yet another subalgebra
of $ \ParAlg $, that we call the {\it spherical partition algebra} $ \SpheAlg  $.
By definition, $ \SpheAlg  $ is the $ \CC[x] $-algebra given by idempotent truncation of $ \ParAlg$, as follows
\begin{equation}
 \SpheAlg = e_k \ParAlg e_k 
\end{equation}  
where $  e_k = \iota_k\left ( \frac{1}{k! } \sum_{ \sigma \in \Si_k } \sigma\right)  $
and $ \iota_{\color{black}{k}}: \CC \Si_k \rightarrow  \ParAlg$ is the inclusion map, and so it may be seen as the
partition algebra analogue of the {\it spherical Cherednik algebra}, 
considered for example in \cite{Rouquier}. For any $t \in \CC$, 
there is a specialization map 
$ x \mapsto t $ for $ \SpheAlg $ and we denote by $  \SpheAlg(t) $ the corresponding 
specialized algebra. 
We show that the $  \SpheAlg(t) $'s, for $ t $ running over $ \CC$, are algebras of fundamental
interest in the representation theory of diagram algebras, and even beyond that.  

\medskip
A first main result of our paper, given in Theorem \ref{lemma2}, 
is the determination
of the rank $  \rank_{\CC[x]} \,  \SpheAlg $ of $ \SpheAlg $. We find 
that $  \rank_{\CC[x]} \,  \SpheAlg = bp_k $ where $ bp_k $ is the
cardinality of {\it bipartite partitions} $ \BiPar_k $ of $k$.
Bipartite partitions are classical combinatorial objects whose 
history goes back more than a century to the work of Macmahon and others, see for example \cite{MacMahon}.
The sequence $ (bp_0, bp_1, bp_2, bp_3,  bp_4, bp_5, \ldots ) = (1, 2, 9, 31, 109, 339, \ldots ) $
is A002774 in the On-Line Encyclopedia of Integer Sequences.


\medskip
Let $ V {\color{black}{=V_n}} $ be a vector space of dimension $n$. 
Then the second named author and V. Jones
independently proved that $ \ParAlg(n)$ is in Schur-Weyl duality with the group algebra
$ \CC \Si_n $, acting 
diagonally on $ V_n^{\otimes k } $, see \cite{Jones}, \cite{PMartin}. 
This is an important {\it double centralizer property} that allows us to pass
representation{\color{black}{-}}theoretic information back and forth between the 
module categories for $ \CC \Si_n $ and $ \ParAlg(n)$. 

\medskip
A main motivation for our work is to establish an analogous
{\it double centralizer property} involving $ \SpheAlg(n) $ and $ \CC \Si_n $, but this time with
commuting actions 
on the symmetric power space $ S^k V_n $, and to study some of its consequences.
We achieve this goal in section \ref{Schur-Weyl duality}
of our paper, culminating in our Theorems \ref{teorem 6} and \ref{joining the results}. 
We obtain an isomorphism of $ (\CC \Si_n, \SpheAlg(n)) $-bimodules
\begin{equation}\label{symmetricpower}
S^k V_n \cong \bigoplus_{ \lambda \in  \ParSph} S(\lambda) \otimes G_k(\lambda) 
\end{equation}
where $ S(\lambda) $ is the Specht module for $ \CC \Si_n $ and $ G_k(\lambda)  $ is 
a simple module for $ \SpheAlg(n) $, 
for $ \ParSph \subseteq \Par_k $ 
a concretely defined subset of the set of partitions of $ k $, see \eqref{defineLambaSph}. 
Moreover, for $ \lambda \in \ParSph $
we obtain an explicit dimension formula
\begin{equation}\label{keyingredient}
 \dim G_k(\lambda) =
    \sum_{ \nu \in \Par_k^{\le n} } {  K_{\lambda,  \Phi(\nu)} }
\end{equation}
where $  K_{\lambda,  \Phi(\nu)} $ is the Kostka number, and $ \Phi:  \Par_k^{\le n} \rightarrow \Par_n $
is a \lq multiplicity\rq\ function defined on the partitions of $ k $ of length less than $ n $.
A key ingredient in the proof of \eqref{keyingredient} is a direct sum decomposition of $  S^k V_n $
in terms of {\it permutation modules} for $ \CC \Si_n $. A related version of this decomposition
was obtained by Harman in \cite{Harman}, 
but for the reader's convenience we provide its (simple) proof 
in Theorem \ref{firstthm}.

\medskip

It is clear, {\color{black}{however,}} that the $ G_k(\lambda) $'s do not exhaust
all the simple $ \SpheAlg(n)$-modules, 
and therefore we embark on 
a systematic study of the representation theory of $ \SpheAlg(t)$,
for all specializations $ x \mapsto t \in \CC $ (except $ t=0 $ that we sometimes omit for
brevity of the presentation). We find that
$ \SpheAlg(t)$ is semisimple if $ t \not\in \{0,1,2,\ldots, 2k-2 \} $
but not if $ t \in \{1,2,\ldots, 2k-2 \} $
(although 
$ S^k V_n $ is always a semisimple $ \SpheAlg(n)$-module, as can be read off from 
\eqref{symmetricpower}). 



\medskip
A main ingredient in our study is  
the fact, shown for example by \ppmG{K\"onig},
Xi and Doran-Wales, that $ \ParAlg$ is 
a {\it cellular algebra} in the sense of Graham and Lehrer, 
and therefore 
$ \SpheAlg$ is a cellular algebra too, being an idempotent truncation
of a cellular algebra, see eg. \cite{DW}, \cite{GL}, \cite{KoXi} and \cite{Xi}.
The cell modules are of the form $ e_k \Delta_k(\lambda) $ where
the $ \Delta_k(\lambda)$'s are cell modules for $ \ParAlg$ and
$ \lambda \in \Lambda^k  = \bigcup_{l=0}^{k} \Par_l $. 


\medskip
In section 
\ref{sectioncellularity}, we combine results due to Murphy, see \cite{Murphy},
with specific diagrammatic calculations in order to obtain 
a basis for $ e_k \Delta_k(\lambda) $. 
In particular, in Theorem \ref{stateandproveA} we show 
\begin{equation}
\dim e_k \Delta_k(\lambda) =
    \sum_{i=l}^k \sum_{\substack{  \nu \in \Par_i  \\  \Psi(\nu) \in \Par_l }} K_{\lambda,  \Psi(\nu)} |  \Par_{{k-i}} |
\end{equation}
where $ \Psi:  \Par_i \rightarrow  \bigcup_{ k=0}^{\infty} \Par_k$ is a new multiplicity function. 
In Corollary \ref{sphpar}, we deduce from this that $ e_k \Delta_k(\lambda) \neq 0 $ if and only if $ \lambda \in \Lambda_{sph}^{k}$
where $ \Lambda_{sph}^{k} \subseteq \Lambda^k$ is another concretely defined subset of $ \Lambda^k$, see
\eqref{concretelydefined2}. 



\medskip
The set $ \Lambda_{sph}^{k} $ is the natural index set for the representation theory of
$ \SpheAlg(t) $.
\ppm{It follows immediately from the construction that
  $ ( k ) \in \Lambda_{sph}^{k} $
  whereas $ ( 1^k ) \notin \Lambda_{sph}^{k} $ if $ k\ge 2 $.
  However the primitive idempotents associated with these cell modules
  are of  
  intrinsic interest, so let us
(upon the suggestion of the referee) 
  add a remark in this direction.}
{\color{black}{For $ n \ge 2k $
the primitive idempotents 
associated with the cell modules for 
$ \ParAlg(n) $ 
were
determined by the second named author and Woodcock in \cite{MartinWoodcock2}. 
Recently,  Benkart-Halverson and Campbell found cancellation-free
expressions for the idempotents associated with
the cell modules $ \Delta_k (k) $ and $ \Delta_k( 1^k ) $, see \cite{BH} and \cite{Campbell}. 

\ppm{The forms of these expressions are indeed of intrinsic interest, and
  of course they verify}
that 
$ ( k ) \in \Lambda_{sph}^{k} $
whereas $ ( 1^k ) \notin \Lambda_{sph}^{k} $ if $ k\ge 2 $. }}


\medskip
The 
simple $ \SpheAlg(t) $-modules  
are $ \{ e_k L_k(\lambda) \, | \, \lambda \in \Lambda_{sph}^{k} \} $,
obtained via multiplication with $ e_k $ on the simple $ \ParAlg(t)$-modules $ L_k(\lambda) $. 
This, combined with results by the second named author, see
\cite{PMartin1}, leads
to our main Theorem \ref{mainThm} that describes  
the decomposition numbers and dimensions of the simple modules for $ \SpheAlg(t) $, 
in all cases except $ t=0$.

\medskip
Our proofs rely heavily on
Corollary \ref{quasiheriditarySphe},
stating that $ \SpheAlg(t)$ is a quasi-hereditary algebra when $ t \neq 0 $.
{\color{black}{This may be regarded as a key property of $ \SpheAlg(t)$, and also $ \ParAlg(t)$ has this
property.}}
In the final section \ref{tilting} of the paper, we take the opportunity to determine the
indecomposable projective modules and the indecomposable tilting modules for both algebras. 

\medskip
In \cite{NaPaulSriva}, S. Narayanan, D. Paul and S. Srivastava introduced the {\it multiset partition algebra}
$ \mathcal{MP}_k $ via an explicit combinatorial definition of its structure coefficients. It was
further generalized and studied by R. Orellana and M. Zabrocki in \cite{OrellanaZabrocki2} and
by A. Wilson in \cite{Wilson}. 
In \cite{NaPaulSriva} it was proved that $ \mathcal{MP}_k(n) $ is in Schur-Weyl 
duality with $ \mathbb{C} \Si_n $ on $ S^k V_n $ and so it follows that 
$ \SpheAlg(n) $ and $ \mathcal{MP}_k(n) $ are isomorphic when $ n \ge 2k $. Actually
A. Wilson has kindly informed us of a(n unpublished) proof showing that $ \SpheAlg(t) $ and $ \mathcal{MP}_k(t) $
are isomorphic in general. Given this, it is likely that the simple modules
for $ \mathcal{MP}_k(n) $ that are described in \cite{NaPaulSriva}, \cite{OrellanaZabrocki2} and \cite{Wilson} in 
terms of
{\it semistandard multiset tableaux}, are the $ G_k(\lambda)$'s of the present paper. In this sense, the Schur-Weyl duality results of our section
\ref{Schur-Weyl duality} may be considered as a complimentary approach to some of the results for $ \mathcal{MP}_k(n) $, 
developed in \cite{NaPaulSriva}, \cite{OrellanaZabrocki2} and \cite{Wilson}. On the other hand, our main results 
in sections \ref{sectioncellularity}, \ref{decompositionnumbers} and \ref{tilting},
for example the complete classification of the simple modules for $ \SpheAlg(n) $, 
and the description of these modules in 
Theorem \ref{mainThm}, have not been obtained in the 
$\mathcal{MP}_k(n) $-setting. 


\medskip
Let us give a brief overview of the organization of the paper. In the following section
\ref{Basic notation} we fix the basic notation to be used throughout the paper. This
concerns integer partitions, Young tableaux and other concepts related to the representation
theory of the symmetric group. In section \ref{Bipartite partitions} we recall the notion
of bipartite partitions $ \BiPar_k $ and introduce the corresponding diagrammatic representations.
For $ b \in \BiPar_k$, we further recall the lexicographic normal form $ \norm(b) $ and Garsia and Gessel's
normal form $GG(b)$ from \cite{GG}. In section \ref{The partition algebra} we recall the partition
algebra $ \ParAlg$ and introduce the spherical partition algebra $ \SpheAlg$, the main protagonist of
our paper. In section \ref{Rank of the} we show that $ \rank_{\CC[x]} \SpheAlg = bp_k $,
by constructing a concrete basis for $ \SpheAlg$. This uses diagrammatic arguments
involving the normal form $\norm(b)$ from section \ref{Bipartite partitions}. 
In section \ref{Schur-Weyl duality} we construct commuting actions of $ \SpheAlg(n) $ and $ \CC \Si_n $
on $ S^k V_n $ and show that they satisfy a double centralizer property. Motivated by
a recent paper of Benkart, Halverson and Harman, see \cite{BHH}, 
we find a direct sum decomposition of $  S^k V_n $ 
in terms of permutation modules for $ \CC \Si_n $, which allows us to determine 
the dimension of the irreducible $ \SpheAlg(n) $-modules $ G_k(\lambda) $ that appear in $  S^k V_n $. 

\medskip

In section \ref{sectioncellularity} we show that $ \SpheAlg $ is a cellular algebra, determine a basis for its cell modules
and determine the parametrizing poset for $ \SpheAlg $. Using Garsia and Gessel's normal form
for bipartite partitions, we further construct a Robinson-Schensted-Knuth type bijection for 
$ \SpheAlg $. Finally, we show that $ \SpheAlg(t) $ is quasi-hereditary when $ t \neq 0$. 

\medskip
In section \ref{decompositionnumbers} we obtain the main Theorems involving the decomposition
numbers for $ \SpheAlg(t)$ and finally, in section \ref{tilting}, we obtain the Loewy structure
of the indecomposable projective modules and tilting modules. 
  


\subsection{{\color{black}{Acknowledgements}}}
The authors would like to express their gratitude to Stephen Griffeth and Luc Lapointe for 
insightful comments on the results of the paper. They are especially grateful to Alexander Wilson for
pointing out the connection to the multiset partition algebra and for mentioning the references
\cite{NaPaulSriva}, \cite{OrellanaZabrocki2} and \cite{Wilson}.   
Finally, they wish to express their gratitude to the anonymous referee
{\color{black}{for indicating several research projects related to the present work
and for communicating detailed suggestions that helped them improve substantially the clarity and presentation
of the paper.}}
