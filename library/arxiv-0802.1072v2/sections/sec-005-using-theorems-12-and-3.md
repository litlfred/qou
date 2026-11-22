---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-005-using-theorems-12-and-3
section_title: "Using Theorems 1,2, and 3"
section_number: null
pages: 6-9
source_pdf: 0802.1072v2.pdf
source_sha256: 6f4d93f0b7ba5cd7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
{\bf Theorems 1 and 2}. \ \ We need two more results before we can make Theorems~\ref{T:topological} and \ref{T:invertibility}  into results that can be used computationally.  First, we need to be able to recognize when the closure of a 3-braid has braid index less than 3. Table I  gives the Xu symbols $\Sigma^\star(W)$  in the cases when the closed braid associated to $W$ has braid index less than 3.  Using it, we can decide when a closed 3-braid is a link of braid index 3, by computing its Xu-invariant and verifying whether it is or is not the symbol for a  3-braid of braid index less than 3.  In the table the symbol $1^{u}$ means $u$ syllables of length 1.  For example, Table I tells us that a 3-braid $X$ whose Xu-invariant is $(-5; (1^4, 2)) = (-5; (1, 1, 1, 1, 2))$ is conjugate to the 3-braid  $a_1^{-5}a_2$, which closes to the type (2,5) torus knot.  Therefore the closure of $X$ has braid index 2. 

\medskip

\centerline{
\begin{tabular}{ |c | c| }
\hline
$W$ & $\Sigma^\star(W)$  \\
\hline
\hline
$a_1^k a_2$,  \ $k = 1 \ {\rm and} \ 2$  &$(1; \ (k-1))$ \\ \hline
$a_1^k a_2$,  \ $k \geq 3$  &$(-1; \ (k+1))$ \\ \hline
 $a_1^k a_2^{-1}$, \   $k\geq 2$      &  $(-1; \ (1,k))$   \\ \hline
$a_1^k a_2$,  \ \ \ $k\leq -2$ & $(k; (1^{-k-1},2))$ \\  \hline
\ \ \ $a_1^k a_2^{-1}$, \   $k \leq -1$, \   & $(k; \ (1^{-k-1}))$    \\ \hline
$a_1^{-1}a_2$ and $a_1a_2^{-1}$  &  $(-1; (2))$    \\ \hline
$a_2$  &  $(0; (1))$    \\ \hline
$a_2^{-1}$  &  $(-1; (1))$ \\ \hline
 \end{tabular} }
\medskip
\centerline{\bf Table I: Conjugacy classes of links of braid index less than 3}

Next, if we are given two 3-braids $W,W'$ and find that they have distinct Xu-invariants, we cannot be sure that they determine distinct links until we determine whether they are flype-admissible.  
To answer this question, we need the following Lemma, which is due to K.H.Ko and S.J.Lee:

\begin{lemma}{\rm K.H.Ko and S.J.Lee, \cite{KL}}
\label{L:properties of flypes}  \ \ \  {\rm (i)} The flype  in {\rm (\ref{E:flype-admissible form})} is non-degenerate if and only if  $|v|\geq 2$, also $u,v+\epsilon,w$ are pairwise distinct, also  $u,w \not= 0, \epsilon,  2\epsilon$. 
{\rm (ii)} The conjugacy class of a negative flype-admissible braid $L$ contains a braid that admits a positive flype  if and only if  $u=1$ or $w = 1$, or $v = 2$.  
\end{lemma}

In Table II we give the Xu symbols for all non-degenerate flype-admissible braids, up to cyclic permutation of the tail symbol.  There are 16 cases, because the exponents $u,v,w,\epsilon$ can either be positive or negative. To keep track of the signs, replace $u,v,w$ by $\pm p, \pm q, \pm r$, where $p,q,r>0$.  Now observe that only  8 of the 16 cases are needed, because a given braid $K$ admits a non-degenerate flype if and only if the Xu-symbol for $K$ or for $K^{-1}$ coincides with one of the 8 symbols that are given in Table II. 

\centerline{
\begin{tabular}{|c | c |c |  }
\hline
$\epsilon$ & $W$ &$\Sigma^\star(W)$, up to cyclic permutation of tail symbol  \\
\hline
\hline
$pos$ & $a_1^pa_2^qa_1^ra_2$ &$(3 \ ; \  (p-2, \ q-1, \ r-2))$ \\ \hline
$$ & $a_1^{-p}a_2^qa_1^ra_2$  & $(1-p \ ; \  (q, \ r-1, 1^p))$    \\ \hline
$$ & $a_1^pa_2^{-q}a_1^ra_2$   &   $(2-q \ ; \ (p-1, \ 1^{q-1}, \  r-1))$  \\ \hline
$$ & $a_1^pa_2^qa_1^{-r}a_2$ & $(1-r \ ; \  (p -1, \ q, \ 1^r ))$  \\ \hline
$neg$ & $a_1^pa_2^qa_1^ra_2^{-1}$ &   $(0 \ ; \  (p, \ q-1, \ r))$   \\ \hline
$$ & $a_1^{-p}a_2^qa_1^ra_2^{-1}$ &    $(-p \ ; \ (q, \ r+1, \ 1^{p-2}))$    \\ \hline
$$ &$a_1^pa_2^{-q}a_1^ra_2^{-1}$  &     $(-q-1 \ ; \ (r+1, \ p+1, \  1^{q-1}))$       \\ \hline
$$ & $a_1^pa_2^{q}a_1^{-r}a_2^{-1}$ &       $(-r \ ; \ (p+1, \ q, \ 1^{r-2}))$  \\ \hline
\end{tabular} }
\medskip
\centerline{{\bf Table II: Conjugacy classes admitting non-degenerate flypes}}
\medskip
We remark that the data in Table II is  only given up to cyclic permutation of the tail symbol, because the lexicographically smallest choice  depends upon the relative numerical values of $p,q,r$. 

We now have essentially all the data needed to implement Theorems 1,2 and 3, however an additional issue arises if one wishes to use any of our three theorems on low crossing examples which admit non-degenerate flypes.  For example, one might wish to test a potential invariant which was difficult to compute on knots which had large crossing number.   We give, in Table III, a list of all of the knots of braid index 3 which admit non-degenerate negative flypes, and do not also admit positive flypes, and have braid crossing number $c_b = |u|+|v|+|w| + 1\leq 12$.  Note that $c_b$ is not the same as minimum crossing number for all possible projections of the knot associated to our closed braid (although for all but one of the examples in Table 1 the two are actually the same), rather it is crossing number for closed 3-braid representatives which are in flype position. 

The knots are identified, in Table III, using both classical notation (e.g as in \cite{Rolfsen}) and the newer notation of Dowker-Thistlethwaite (used in all the newer tables).  The former only exist through 10 crossings.

\

\centerline{
\begin{tabular}{|c|c | c | c | c |c |  }
\hline
$\mathcal K$(classical) & $\mathcal K$(Dowker-Thistlethwaite) & $\beta$ & $c_b$ &$(u,v,w)$ & $(w,v,u)$ \\
\hline
\hline
$8_{10}$ & $8_{a3}$ & -1 &  8 & (3,-2,2) & (2,-2,3) \\ \hline
$10_{47}$ & $10_{a15}$ &  +1  & 10 &(5,-2,2) & (2,-2,5) \\\hline
$10_{62}$ & $10_{a 41}$ & +1 &  10  & (3,-2,4) & (4,-2,3)\\\hline
$10_{48}$ & $10_{a79}$ & -3 &   10 & (3,-4,2) & (2,-4,3)\\ \hline
$10_{127}$ & $10_{n16}$ &  -9       &  10    & (-5,-2,2) & (2,-2,-5)\\\hline
$10_{143}$ & $10_{n  26}$ & -7 &  10  & (3,-2,-4) & (-4,-2,3) \\\hline
$***$ & $11_{a240}$ & +7  &   12 & (5,3,3)& (3.3.5)  \\ \hline
$***$ & $12_{a 146}$ & +3 &   12 & (7,-2,2)& (2,-2,7)  \\\hline
$***$ & $12_{a 369}$ & +3 &   12  & (5,-2,4) &  (4,-2,5) \\\hline
$***$ & $12_{a 576}$ & +3 &  12  & (3,-2,6) & (6,-2,3)  \\\hline
$***$ & $12_{a  835}$ &-5 &   12  & (3,-6,2)& (2,-6,3) \\\hline
$***$ & $12_{a  878}$ & -1 &    12  & (5,-4,2) & (2,-4,5)  \\\hline
$***$ & $12_{a  1027}$ & -1 &    12  & (3,-4,4) & (4,-4,3)  \\\hline
$***$ & $12_{a  1233}$ & +1 &   12   &(5,-3,3) & (3,-3,5)  \\\hline
$***$ & $12_{n 234}$ & -11 &    12 & (-7,-2,2)&  (2,-2,-7) \\\hline
$***$ & $12_{n  466}$ & -9 &   12  & (-5,-3,3) & (3,-3,-5)  \\\hline
$***$ & $12_{n  467}$ & -7 &   12  & (-3,-4,4) & (4,-4,-3)  \\\hline
$***$ & $12_{n  468}$ & -5 &    12  & (-3,-3,5) & (5,-3,-3) \\\hline
$***$ & $12_{n  472}$ & -15 &    12  & (-3,-4,-4)& (-4,-4,-3)  \\\hline
$***$ & $12_{n  570}$ & -9 &   12  & (-3,-5,3)& (3,-5,-3)    \\
\hline
\end{tabular} }

\medskip

\centerline{{\bf Table III:  A list of all examples of non-transversally simple }}

\centerline{{\bf  closed 3-braids with braid crossing number $c_b\leq 12$}}

To assemble the data in Table III we began by listing all possible numbers $(\pm|u|,\pm|v|,\pm|w|)$   with $c_b=|u|+|v|+|w|+1$, deleting those that do not satisfy the constraints of the two lemmas.  Next we used Knotscape \cite{Knot} to sort the survivors  into classes which had the same  topological knot type.  For each topological knot type, some of the examples had non-minimal braid crossing number, so we deleted those. For example, $(-3,4,2)$ appeared as an example with $c_b=10$, but  its conjugacy class also has an 8-crossing example, $(3,-2,2)$, so we deleted $(-3,4,2)$.  After that, for each topological knot type we divided the representing closed braids into conjugacy classes belonging to the braids before and after the flype.  In every case it turned out that there were two distinct  conjugacy classes in $B_3$, as must be the case, by Theorem~\ref{T:topological}.  Finally, we chose exactly one representative from each conjugacy class, whenever it happened that the list of survivors had more than one representative.   In this regard we note that, for example, $\sigma_1^{-5}\sigma_2^{3}\sigma_1^{-3}\sigma_2^{-1}\approx 
\sigma_1^{2}\sigma_2^{-2}\sigma_1^{-5}\sigma_2^{-1} \approx 
\sigma_1^{-3}\sigma_2^{-4}\sigma_1^{2}\sigma_2^{-1}$.  This shows that conjugate braids which admit flypes need not have the same braid crossing number $c_b$. In this case the first has braid crossing number  12 and the other two have crossing number $10$. There are examples where  all three have the same crossing number, and examples where one has minimal crossing number and the other two have higher crossing number.  This issue arises when we enumerate the low-crossing number examples.

The examples in Table III are given by specifying,  for each pair of transversal knot types, the topological knot type $\mathcal{K}$ in the standard tables, the  Bennequin number $\beta = u+v+w-4$, the minimum closed braid crossing number $c_b=|u|+|v|+|w|+1$, and the two closed 3-braid representatives ${\mathcal {TK}}_1, {\mathcal {TK}}_2$. The closed braids are determined by the triplets $(u,v,w)$ and $ (w,v,u)$, i.e. as negative flype-related braids $\sigma_1^u\sigma_2^v\sigma_1^w\sigma_2^{-1}$ and $\sigma_1^w\sigma_2^v\sigma_1^u\sigma_2^{-1}$.
