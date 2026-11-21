---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-007-the-decomposition-numbers-for-sp-kn-when-sp-kn-i
section_title: "The decomposition numbers for SP k(n) when SP k(n) is non-semisimple."
section_number: null
pages: 22-24
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.624
latex_coverage_ratio: 0.982
doc_brief: "On the spherical partition algebra — For k ∈N we introduce an idempotent subalgebra, the spherical partition algebra SPk, of the partition algebra Pk, that we define using an embedding associated"
---
\label{decompositionnumbers}
In this section we shall use the results of the previous sections to determine the decomposition numbers for $ \SpheAlg(n) $ when $ \SpheAlg(n) $ is
quasi-hereditary and non-semisimple, that is 
when $ n \in \{1,2,\ldots, 2k-2\} $. 

\medskip
Our arguments depend crucially on \cite{PMartin1} in which the decomposition numbers for $  \ParAlg(n)$ are determined.
The results in \cite{PMartin1} are formulated in terms of the notion of {\it $n$-pairs of partitions}, which we need to explain.
For this, let $ \lambda \in \Par_l $ and let $ u \in  \lambda $ be the $(i,j)^{\color{black} \rm th} \,$node of $ \lambda$. For $ Q \in \Z $ we then define
the {\it $Q $-content of $u $}
as $  c_{\lambda}^Q(u)  = Q +j -i $ and let the {\it $Q $-content diagram of $\lambda $} be 
the diagram obtained from the Young diagram of $ \lambda $ by writing $   c_{\lambda}^Q(u)  $ in each node $ u \in \lambda$. 
For example, for $ \lambda = (5,3,3,2,2)$ the $2$-content diagram is as follows
\begin{equation}\label{nYoung}
   \raisebox{-.5\height}{\includegraphics[scale=0.8]{dib60.pdf}}
\raisebox{-33\height}{.} 
\end{equation}
\begin{definition}
Let $ (\lambda, \mu) $ be a pair of partitions of different orders. We then say that $ (\lambda, \mu) $ is {\it an $n$-pair} if
$ \lambda \subset \mu$ and the Young diagram for $ \mu $ is obtained from the Young diagram for $ \lambda $ by adding nodes
in exactly one row. Furthermore, the rightmost of these nodes should be of $| \lambda | $-content $n$. 
\end{definition}
Below we give two examples of $n$-pairs, in the first we choose $ n=4$ and in the second $ n = 15$.
\begin{equation}\label{npairs}
   \left( \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib62.pdf}} \right), \, \, \, \, \, \, \, \, \, \, \, \, 
 \left( \raisebox{-.45\height}{\includegraphics[scale=0.8]{dib61.pdf}} \right) 
\raisebox{-25\height}{.} 
  \end{equation}

Note that there exists an alcove geometric description of $n$-pairs, see \cite{BdVK}.


\medskip
The following Lemma is immediate from Definition \ref{nYoung}.
\begin{lemma}\label{isimmediate}
  Suppose that $ n \in \Z $ and $ \lambda \in \Par $. Then there exists at most one $ \mu \in \Par $ such that
  $ (\lambda, \mu )$ is an $n$-pair.
\end{lemma}
\begin{proof}
  Let $ \lambda= (\lambda_1^{a_1}, \lambda_2^{a_2}, \ldots, \lambda_p^{a_p}) \in \Par_l$.
  If $ \mu \in \Par $ is obtained from $ \lambda $ by adding nodes to the $i^{\color{black} \rm th} \,$row, then we must have 
  $ i \in  \{1, a_1+1, a_1+a_2+1, \ldots, a_1+a_2+\ldots+a_p +1\} $. Since the $ | \lambda | $-contents are
  constant along the diagonals of $ \lambda $, we conclude from this that the possible values of $ n $ are all distinct,
  which shows the Lemma.
  Below we illustrate on the example $ \lambda = (9^1, 5^3, 3^2) $, where we have indicated with
  red the possible values of $ n$.
\begin{equation}\label{uniquepair}
  \lambda =  \raisebox{-.5\height}{\includegraphics[scale=0.8]{dib63.pdf}} 
\raisebox{-40\height}{.} 
  \end{equation}

\end{proof}

In \cite{PMartin1} the following important Theorem was proved.
\begin{theorem}\label{mainPaul}
  Let $ n \in \{1,2,\ldots, 2k-2 \} $. For $ \lambda \in \Lambda^k $ let $ L_k(\lambda) = \Delta_k(\lambda)/\rad(\lambda) $
be the irreducible $ \ParAlg(n)$-module associated with $ \lambda$. 
Then the following statements hold. 
  \phantomsection\label{importantThmPaul}
  \begin{description}
  \item[a)] Let $ \lambda, \mu \in \Lambda^k $ with $ \lambda \neq \mu$. Then there is a nonzero homomorphism of $ \ParAlg(n)$-modules
    $ \Delta_k(\mu) \rightarrow \Delta_k(\lambda) $ if and only if $ (\lambda, \mu) $ is an $n$-pair. 
  \item[b)] Let $ \lambda \in \Lambda^k$. If there is no $ \mu \in \Lambda^k $ such that $ (\lambda, \mu ) $ is an $n$-pair then
    $ \Delta_k(\lambda) $ is irreducible. Otherwise, $ \Delta_k(\lambda) $ has decomposition factors $ L_k(\lambda) $ and
    $ L_k(\mu) $ where $ (\lambda, \mu ) $ is the unique $n$-pair with $ \lambda $ in the first factor. 
  \item[c)] Let $ \lambda \in \Lambda^k $ and suppose that $ ( \lambda^1, \lambda^2, \ldots, \lambda^p) $
    is a chain of partitions in $ \Lambda^k$ such that $ \lambda= \lambda^1 $ and such that each $ (\lambda^i, \lambda^{i+1}) $ is an $n$-pair
    for $ i =1,2,\ldots, p-1$. Furthermore, assume that the chain is maximal in the sense that there is no $n$-pair $ (\lambda^p, \mu) $
    with $ \mu \in \Lambda^k$. Then there is a resolution of $ \ParAlg(n)$-modules
    \begin{equation}\label{resolution}
      0 \rightarrow \Delta_k(\lambda^p) \rightarrow \cdots \rightarrow \Delta_k(\lambda^2)\rightarrow \Delta_k(\lambda^1 ) \rightarrow L_k(\lambda  )
\rightarrow 0.
    \end{equation}    
  \end{description}
  
\end{theorem}

Note that \eqref{resolution} gives rise to the formula 
\begin{equation}
\dim L_k(\lambda) = \sum_{i=1}^p (-1)^{i+1} \dim \Delta_k(\lambda^i). 
\end{equation}  
In view of \eqref{bytheconstruction}, this is an explicit formula for $ \dim L_k(\lambda) $. 

\medskip
In order to apply Theorem \ref{mainPaul} we need the following Lemma.
\begin{lemma}\label{weneedthe}
  Suppose that $ \lambda \in \Lambda_{sph}^{k}$. Then $ e_k L_k(\lambda) \neq 0 $. It is an irreducible $ \SpheAlg(n) $-module and
  the set $ \{  e_k L_k(\lambda)  \, | \,  \lambda \in \Lambda_{sph}^{k} \} $ is a complete set of representatives for the
  isomorphism classes of irreducible the $ \SpheAlg(n) $-modules. 
  \end{lemma}
\begin{proof}

In follows from Corollary \ref{quasiheriditarySphe} that $ e_k L_k(\lambda) \neq 0 $ when $ \lambda \in 
\Lambda_{sph}^{k} $. From this the remaining statements of the Lemma follow from the
general cellular algebra theory, see \cite{GL}. 
\end{proof}

\medskip
Combining, we obtain the following Theorem.
\begin{theorem}
\phantomsection\label{mainThm}
\begin{description}
  \item[a)] $ \{  e_k L_k(\lambda)  \, | \,  \lambda \in \Lambda_{sph}^{k} \} $ is a complete set of representatives for the
  isomorphism classes of irreducible the $ \SpheAlg(n) $-modules.
  \item[b)] Let $ \lambda \in \Lambda_{sph}^k$. If there is no $ \mu \in \Lambda_{sph}^k $ such that $ (\lambda, \mu ) $ is an $n$-pair then
    $ e_k\Delta_k(\lambda) $ is an irreducible $ \SpheAlg(n) $-module.
    Otherwise, $ e_k\Delta_k(\lambda) $ has decomposition factors $ e_kL_k(\lambda) $ and
    $ e_kL_k(\mu) $ where $ (\lambda, \mu ) $ is the unique $n$-pair with $ \lambda $ in the first factor. 
  \item[c)] Let $ \lambda \in \Lambda_{sph}^k $ and suppose that $ (\lambda^1, \lambda^2, \ldots, \lambda^p) $
    is a chain of partitions in $ \Lambda_{sph}^k$ such that $ \lambda= \lambda^1 $ and such that each $ (\lambda^i, \lambda^{i+1}) $ is an $n$-pair
    for $ i =1,2,\ldots, p-1$. Furthermore, assume that the chain is maximal in the sense that there is no $n$-pair $ (\lambda^p, \mu) $
    with $ \mu \in \Lambda_{sph}^{k} $. Then there is a resolution of $ \SpheAlg(n)$-modules
    \begin{equation}\label{resolutionA}
      0 \rightarrow e_k\Delta_k(\lambda^p) \rightarrow \cdots \rightarrow e_k\Delta_k(\lambda^2)\rightarrow e_k\Delta_k(\lambda^1 ) \rightarrow e_kL_k(\lambda  )
\rightarrow 0.
    \end{equation}    
  \end{description}
  
\end{theorem}
\begin{proof}
  The statement in ${ \bf a)} $ has already appeared in Lemma \ref{weneedthe}. The statement in ${ \bf c)} $
  follows from ${ \bf c)} $ of Theorem \ref{importantThmPaul} and the fact that left multiplication with $ e_k$ is
  an exact functor. To show the first statement of ${ \bf b)} $, we observe that under the hypothesis on $ \lambda $ the resolution
  \eqref{resolutionA} becomes 
    \begin{equation}\label{resolutionshoert}
      0 \rightarrow e_k\Delta_k(\lambda^1 ) \rightarrow e_kL_k(\lambda  )
\rightarrow 0
    \end{equation}
    which shows that $   e_k\Delta_k(\lambda ) $ is irreducible, as claimed. Finally, the second statement of
    ${ \bf b)} $ follows from the corresponding statement in ${ \bf b)} $ of Theorem \ref{importantThmPaul} and
    exactness of left multiplication with $e_k$.
\end{proof}

As above, we note that the resolution \eqref{resolutionA}, combined with \eqref{48}, gives rise to an explicit formula for
the dimensions of the irreducible $ \SpheAlg(n)$-modules, as follows
\begin{equation}
\dim e_k L_k(\lambda) = \sum_{i=1}^p (-1)^{i+1} \dim e_k \Delta_k(\lambda^i). 
\end{equation}  


Let us consider the example $ \lambda = (1) \in \Lambda^3_{sph}$ with $ k=n=3$. 
Then the chain in ${ \bf c)} $ of Theorem \ref{mainThm} has the form $ \{ \lambda^1, \lambda^2 \} $ where
$ \lambda^1 = \lambda $ and $ \lambda^2 = (3) $ and so the resolution in 
\eqref{resolutionA} becomes 
\begin{equation}
0 \rightarrow e_3\Delta_3(\lambda^2 ) \rightarrow e_3\Delta_3(\lambda^1 ) \rightarrow e_3L_3(\lambda  )
\rightarrow 0.
\end{equation}
Using ${ \bf b)} $ of Theorem \ref{stateandproveA} we get $ \dim e_3\Delta_3(\lambda^1 )= 4$ and
$ \dim e_3\Delta_3(\lambda^2 )= 1$ and so we find that $ \dim e_3L_k(\lambda^1 )= 3$. 

\medskip
It is interesting to compare this with $ \dim G_3(\mu) $ where $ \mu =(2,1) \in  \Par_{sph}^{3, 3}$.
Note that $ \overline{\mu} = \lambda $ where $ \overline{\mu} $ 
is defined by $ \overline{ \mu } = ( \mu_2, \ldots, \mu_l)  $ for
$ \mu = (\mu_1, \mu_2, \ldots, \mu_l)$. 
Using
${ \bf c)} $ of Theorem \ref{joining the results} we obtain $ \dim G_3(\mu)  = 3$, that is 
$   \dim G_3(\mu) =  \dim e_3L_k(\lambda ) $.

\medskip 
We think that this equality is no coincidence. To be precise, for $ \lambda \in \ParSph$
we think that it should be true that
\begin{equation}\label{conjecture}
\dim G_k(\lambda ) = \dim e_kL_k(\overline{\lambda} ).
\end{equation}
We note that we have verified \eqref{conjecture} for $ k \le 11 $ using SageMath. We also note that
for $ \ParAlg(n) $ the statement corresponding to \eqref{conjecture} should be true as well but appears not to have been proved
in the literature.



\section{Tilting modules for $ \ParAlg(n) $ and $ \SpheAlg(n)$}\label{tilting}
We already saw that $  \ParAlg(n) $ are quasi-hereditary algebras when 
$ n \neq 0$ and therefore, in particular, they 
are endowed with families of {\it tilting modules}, see the appendix to \cite{Donkin}. 
In this section we take the opportunity to 
describe the structure of these tilting modules, using standard 
arguments from the theory of
quasi-hereditary algebras.
We observe that the same arguments also provide us 
with a description of the tilting modules for $ \SpheAlg(n)$. 

\medskip
We assume $ n \in \{1,2,\ldots, 2k-2\} $
in which case $   \ParAlg(n) $, as we already saw, is non-semisimple quasi-hereditary on the poset $ \Lambda^k $
defined in \eqref{poserpar}. Correspondingly, the category $ \ParAlg(n) $-mod of finite dimensional 
$ \ParAlg(n) $-modules is a {\it highest weight category} where the 
standard modules $ \{ \Delta_k(\lambda) \, | \, \lambda \in 
\Lambda^k \} $ are as described in the paragraphs between \eqref{before dd} and \eqref{6.9} and
the irreducible
modules $ \{ L_k(\lambda) \, | \, \lambda \in 
\Lambda^k \} $ as described in $ { \bf c)} $ of Theorem \ref{mainPaul}.

\medskip
$ \ParAlg(n) $-mod is equipped with a duality $ M \mapsto M^{\ast} $ via 
$ M^{\ast} = \Hom_{\CC}(M, \CC) $ where the $    \ParAlg(n) $-structure on $ M^{\ast} $ is given by 
\begin{equation}
af(m) = f(a^{\ast} m)  \mbox{ for } a \in  \ParAlg(n), f \in M^{\ast},  m \in M
\end{equation}
for $ a \mapsto a^{\ast} $ the anti-automorphism coming from the cellular structure on $    \ParAlg(n) $. 
Note that the $L_k(\lambda) $'s are self dual $ L_k(\lambda) = L_k(\lambda)^{\ast}$ via 
\begin{equation}
L_k(\lambda) \rightarrow L_k(\lambda)^{\ast}, v \mapsto  \langle \cdot , v \rangle_{\lambda} .
\end{equation}
The {\it costandard modules}
$ \{ \nabla_k(\lambda)   \, | \,  \lambda \in \Lambda^k \}$
for $    \ParAlg(n) $ are defined by $ \nabla_k(\lambda) = \Delta_k(\lambda)^{\ast}$.

\medskip
The following definitions and results are part of the general theory of quasi-hereditary algebras. 
Let $ {\cal F}_k(\Delta) $ be the subcategory of $   \ParAlg(n) $-modules
whose objects have $ \Delta$-filtrations, 
in other words, a $   \ParAlg(n) $-module $ M $ belongs to $ {\cal F}_k(\Delta) $ if there is a filtration
of $   \ParAlg(n) $-modules $ 0 \subset M_1 \subset M_2 \subset \ldots \subset M_r = M $ such
that for each $ i=1,2,\ldots, r $ there is a $ \lambda_i \in \Lambda^k$
such that 
$ M_i / M_{i-1} = \Delta_k(\lambda_i ) $.
We define $ {\cal F}_k(\nabla) $ in a similar way, that is $ M\in {\cal F}_k(\nabla) $ if and only if 
$ M^{\ast} \in  {\cal F}_k(\Delta) $. 

\medskip
For $ \lambda \in \Lambda^k $ we let $P_k(\lambda) $ be the projective cover of $ L_k(\lambda) $
in $ \ParAlg(n) $-mod. 
Then $ P_k(\lambda ) \in  {\cal F}_k(\Delta) $ and for any $ \Delta $-filtration
$ 0 \subset M_1 \subset M_2 \subset \ldots \subset M_{r-1} \subset  M_r = P_k(\lambda ) $
with $ M_i/ M_{i-1} = \Delta_k(\lambda_i) $ 
we have $ \lambda_r  =\lambda  $ whereas $ \lambda_j  \rhd \lambda $ for $ j <r$. 
For $ M \in {\cal F}_k(\Delta) $ we define $ (M: \Delta_k(\lambda)) = \dim \Hom_{\ParAlg(n)}(M, \nabla_k(\lambda))$
which is the number of times $ \Delta_k(\lambda) $ occurs as a subfactor in
a $ \Delta$-filtration of $ M$. We then have the Brauer-Humphreys reciprocity formula 
\begin{equation}\label{reciprocity}
(P_k(\lambda): \Delta_k(\mu))  = [ \Delta_k(\mu): L_k(\lambda) ] \, \, \, \mbox{for } \lambda, \mu \in \Lambda^k
\end{equation}  
where $ [ \Delta_k(\mu): L_k(\lambda) ] $ denotes decomposition number multiplicity. 

\medskip
For $ \lambda \in \Lambda^k$ we let $ \ParAlg(n) \mbox{-mod}^{\le \lambda}$ be the subcategory 
of $ \ParAlg(n) $-mod consisting of modules 
with composition factors in $ \{ L_k(\mu) \,|  \, \mu \unlhd \lambda\}$. Then $ \ParAlg(n) \mbox{-mod}^{\le \lambda}$ is a highest weight category with standard modules
$ \{ \Delta_k(\mu) \, | \, \mu \unlhd \lambda \} $ and costandard modules
$ \{ \nabla_k(\mu) \, | \, \mu \unlhd \lambda \} $ and so we deduce from the description
of projective covers 
that $ \Delta_k(\lambda) $ is the projective cover of $ L_k(\lambda) $ in
$\ParAlg(n) \mbox{-mod}^{\le \lambda} $. If $ \mu \lhd \lambda  $ we then get
from $ { \bf b)} $ of Theorem \ref{importantThmPaul} and Proposition A3.3 in \cite{Donkin} that
\begin{equation}\label{84}
\dim   \Ext^1_{\ParAlg(n) \mbox{-mod}}(L_k(\lambda), L_k(\mu) )  =
 \dim \Ext^1_{\ParAlg(n) \mbox{-mod}^{\le \lambda}}(L_k(\lambda), L_k(\mu) )  =
 \left\{ \begin{array}{ll} 1 & \mbox{ if }  (\lambda, \mu ) \mbox{ is an } \,n\mbox{-pair} \\
0 & \mbox{ otherwise } \end{array} \right.
\end{equation}  
and if $ \lambda \lhd \mu  $ we get 
\begin{equation}\label{85}
\dim   \Ext^1_{\ParAlg(n) \mbox{-mod}}(L_k(\lambda), L_k(\mu) )  =
 \dim \Ext^1_{\ParAlg(n) \mbox{-mod}}(L_k(\mu)^{\ast}, L_k(\lambda)^{\ast} )  =
 \left\{ \begin{array}{ll} 1 & \mbox{ if }  (\mu, \lambda ) \mbox{ is an } \,n\mbox{-pair} \\
0 & \mbox{ otherwise } \end{array} \right.
\end{equation}  
since $ L_k(\mu)^{\ast} = L_k(\mu) $ and $ L_k(\lambda)^{\ast} = L_k(\lambda) $. 


\medskip
We now fix a chain of partitions ${\cal C}= \{ \lambda^1, \lambda^2, \ldots, \lambda^p \} $ 
in $ \Lambda^k $ such that $(\lambda^i, \lambda^{i+1} ) $ is an $ n$-pair
for $ i=1,2,\ldots, p-1$. Suppose furthermore that the chain is maximal in both directions, in other words 
there is no $ \mu \in \Lambda^k $ such that $ (\mu, \lambda^1) $ is an $n$-pair or such that 
$ (\lambda^p, \mu ) $ is an $n$-pair. By Lemma \ref{isimmediate}, each $ \lambda \in \Lambda^k $ belongs to
a unique such maximal chain $ \cal C$.
Defining
\begin{equation}
  \ParAlg(n) \mbox{-mod}^{\cal C} = \{ M \in \ParAlg(n) \mbox{-mod}  \mid  [M:L_k(\lambda)] \neq 0
  \implies \lambda \in {\cal C}\} 
 \end{equation}
we get from \eqref{84} and \eqref{85} that 
$ \ParAlg(n ) = \oplus_{\cal C} \ParAlg(n) \mbox{-mod}^{\cal C} $ is the block decomposition
of $  \ParAlg(n) \mbox{-mod} $ where $ \cal C$ runs over maximal chains in the above sense.



\medskip
A $ \ParAlg(n)$-module $T$ is called a {\it tilting module} if $ T \in {\cal F}_k(\Delta) \cap {\cal F}_k(\nabla) $. 
For each $ \lambda \in \Lambda^k $ there exists a unique indecomposable tilting module $ T_k(\lambda) $
satisfying $ [ T_k(\lambda): L_k(\lambda) ] = 1 $ and that $ [ T_k(\lambda): L_k(\mu) ] \neq 0
\implies \mu \unlhd \lambda $. 
Each tilting module $ T $ is a direct sum of such $  T_k(\lambda) $'s. 



\medskip
Part $   { \bf a)} $ of the following Theorem was obtained already
in \cite{PMartin1}, but still we include it for completeness. 


\begin{theorem} With the above notation, we have the following results. 
\phantomsection\label{mainThmLoewy}
\begin{description}
\item[a)] If $ j = 2, 3, \ldots, p-1$ then the Loewy structure for $ P_k(\lambda^j) $ is as follows
  \begin{equation}\raisebox{-.43\height}{\includegraphics[scale=1]{dib64.pdf}}
\! \!\!\!\!\!\!\!\!\!\!\! \! \!\!\! \!\!\!
\raisebox{-16\height}{.}   
  \end{equation}

\item[b)] If $ j= 1 $ then the Loewy structure for $ P_k(\lambda^1) $ is as follows
\begin{equation}
  \raisebox{-.35\height}{\includegraphics[scale=1]{dib65.pdf}}
\raisebox{-7\height}{.} 
    \end{equation}  
\item[c)]  If $ j= p $ then the Loewy structure for $ P_k(\lambda^p) $ is as follows
\begin{equation}
  \raisebox{-.35\height}{\includegraphics[scale=1]{dib66.pdf}}
 \!\!\!  \!\!
\raisebox{-12\height}{.} 
    \end{equation} 
  \end{description}
  
\end{theorem}
\begin{dem}
  To prove $   { \bf a)} $ we first observe that
$ { \bf b)} $ of Theorem \ref{importantThmPaul} together with \eqref{reciprocity}
imply that  $ (P_k(\lambda^j): \Delta_k(\lambda^i) ) = 1 $ for
$ j = i $ or $ j = i+1$ and otherwise $ (P_k(\lambda^j): \Delta_k(\lambda^i) ) = 0 $. 
Therefore there are two $\Delta$-factors in the $ \Delta$-filtration for $P_k(\lambda^j) $, namely $\Delta_k(\lambda^j) $
and $\Delta_k(\lambda^{j-1}) $. 
On the other hand, defining $ Q_k(\lambda) = {\rm ker}(P_k(\lambda) \rightarrow L_k(\lambda) )$
we get from \eqref{84} and \eqref{85} that $ \dim  \Hom_{\ParAlg(n)}(Q_k(\lambda^j), L_k(\lambda^i)) = 1 $ 
if $ i = j-1 $ or $ i = j+1$ and otherwise $ \dim  \Hom_{\ParAlg(n)}(Q_k(\lambda^j), L_k(\lambda^i)) = 0 $.
Hence the Loewy structure for $ P_k(\lambda^j) $ must be as indicated in $   { \bf a)} $.


To prove $   { \bf b)} $ we once again use
Theorem \ref{importantThmPaul} and \eqref{reciprocity}, but this time we find that $ \Delta_k(\lambda^1) $
is the only $ \Delta $-factor of $P_k(\lambda^1) $, which shows $   { \bf b)} $.

Finally, to show $   { \bf c)}$ we first note that
$   { \bf b)} $ of 
Theorem \ref{importantThmPaul} gives
$ \Delta_k(\lambda^p) = L_k(\lambda^p) $. Since $ P_k(\lambda^p) $ has $ \Delta$-factors
$  \Delta_k(\lambda^p) $ and $  \Delta_k(\lambda^{p-1}) $, as one sees from
Theorem \ref{importantThmPaul} and \eqref{reciprocity}, the structure of $ P_k(\lambda^p) $
must be the one indicated in $   { \bf c)}$. This proves the Theorem. 
\end{dem}


\medskip
We now get the following Theorem, describing the indecomposable tilting modules for $ \ParAlg(n)$.


\begin{theorem}\label{maintilting} The tilting module $ T_k(\lambda^i) $ for $ i=1,2,\ldots, p$ are given by the following.
\phantomsection\label{mainThmLoewyTilting}
\begin{description}
\item[a)] If $ j = 1, 2, \ldots, p-1$ then $  T_k(\lambda^{j}) = P_k(\lambda^{j+1}) $.
\item[b)]  $  T_k(\lambda^p) = \Delta_k(\lambda^p) $.
\end{description}
  \end{theorem}
\begin{dem}
  The modules in $   { \bf a)}$ are described in
  $   { \bf a)}$ and $   { \bf c)}$ of Theorem \ref{mainThmLoewy}. They are self-dual
  and therefore tilting modules. The missing tilting module is $  T_k(\lambda^p) = \Delta_k(\lambda^p) $,
  given in $   { \bf b)}$.
\end{dem}

\medskip
We finally mention that 
there are versions of Theorem \ref{mainThmLoewy} and Theorem \ref{maintilting} 
for $ \SpheAlg(n) $ instead of $ \ParAlg(n) $.  In view of Theorem \ref{mainThm}
the statements and proofs are here 
exactly the same as for Theorem \ref{mainThmLoewy} and Theorem \ref{maintilting}.
