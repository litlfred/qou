*Within the QOU framework, time-reversal $T$ acts as **word reversal on braid words at the Markov-trace level**:*

$$
  T \;:\;
  \sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_\ell}^{\epsilon_\ell}
  \;\longmapsto\;
  \sigma_{i_\ell}^{\epsilon_\ell} \cdots \sigma_{i_1}^{\epsilon_1}.
$$

*By the Markov trace cyclicity axiom $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$, word reversal is trace-invariant for the Markov closure. The Jones polynomial of $K$ and of its time-reversed counterpart $K^T$ coincide. The operator $T$ is an involution ($T^2 = \mathrm{id}$). It preserves $q$, color-sheet flavors, and Hecke generator signs. It acts purely on the ordering of crossings.*

For a braid word $\beta$, define $\beta^T$ as the reversed word. Trace cyclicity gives $\mathrm{tr}_M(\beta) = \mathrm{tr}_M(\beta^T)$. The reversed word produces the mirror-orientation link, which has the same Jones polynomial as the original. $T$ alone is the trace-cyclicity dual. Composed with $C$ and $P$, it recovers the bar-involution = $CPT$ composite.

## Status (2026-11-27): proved

The invariance $\mathrm{tr}(\beta^T) = \mathrm{tr}(\beta)$ is a theorem, for every number of strands, over any commutative ring and any Hecke quadratic. Two remarks on the argument above. Cyclicity alone gives invariance under rotation of a word, not under reversal. What does give reversal is the anti-involution $\iota$ of $H_n(q)$ that fixes every generator, $\iota(\sigma_{i_1}\cdots\sigma_{i_\ell}) = \sigma_{i_\ell}\cdots\sigma_{i_1}$.

- Every trace on $H_n(q)$ satisfies $\mathrm{tr}\circ\iota = \mathrm{tr}$. This covers every representation character, not only the Markov trace. The proof is an induction along $H_1 \subset H_2 \subset \cdots$ that uses only the double-coset decomposition $H_{k+1} = H_k + H_k\,\sigma_k\,H_k$. Lean: `QOU.IwahoriHecke.HeckeTraceReversal.trace_rev`, and the instance `QOU.BraidsAndKnots.TFromTraceCyclicityAll.tFromTraceCyclicity` of the carrier class for every $n$ and $d$.
- For the Markov trace there is a second proof through Markov uniqueness, applied in the opposite algebra: `QOU.IwahoriHecke.MarkovTraceSymmetries.markov_reverse`.
