*Step 1 — the cluster sub-braid sits at its jet degree.* The canonical
$3A$-strand atomic braid builds $\mathcal{B}_K$ by concatenating one
$3$-strand block per nucleon and inserting the inter-nucleon crossings. Adding
a nucleon to an $(n-1)$-cluster appends its block and the crossings binding it
to the cluster, raising the Gröbner--Shirshov normal-form length by a fixed
increment ([Gröbner–Shirshov spectral sequence proposition](#prop:gb-spectral-sequence)). Reading
this length through the jet-prefix order
([jet prefix Gröbner–Shirshov filtration proposition](#prop:jet-prefix-gb-filtration)) places the
$n$-nucleon cluster sub-word at jet vertical degree $n$.

*Step 2 — the graded component is the cluster term.* Because the GS filtration
is exhaustive and the spectral sequence collapses at $E_2$, the
associated-graded $\mathrm{gr}_n$ is spanned by exactly the normal forms of
filtration degree $n$, i.e. the $n$-nucleon cluster contributions. No
contribution escapes a finite cluster degree (every sub-word has finite GS
length), so the filtration is exhaustive.

*Conclusion.* Summing the graded components reconstructs the binding, and by
Steps 1--2 the degree-$n$ component equals the $n$-body term:
$\sum_n(\text{$n$-body term})=\sum_n\mathrm{gr}_n$. Combining the
graded match (Steps 1--2) with exhaustiveness yields the
[body-order and jet-graded sum identity](#lem:bond-order-eq-jet-degree). $\qquad\blacksquare$
