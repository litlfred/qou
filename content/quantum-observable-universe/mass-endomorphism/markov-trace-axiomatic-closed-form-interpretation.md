## Methodology generalisation

The proof transcribes verbatim to any closed braid $K \in B_n$
whose word factors as $\sigma_{i_1}^{k_1} \sigma_{i_2}^{k_2} \cdots$
with disjoint or commuting generator clusters: each generator power
$\sigma_i^{k}$ reduces via the recurrence $(a_k, b_k)$, and the
resulting linear combination is read off the $H_n(q)$ basis. For
non-disjoint clusters (e.g. neutron $\sigma_1^6 \sigma_2^4 \sigma_1^{-1}$
with mixed signatures), the same recurrence applies after using
$\sigma_i^{-1} = \sigma_i - h$ from the Hecke quadratic.

Outstanding work towards full automation is captured in
[`markov-axiom-recursive-ascent`](#def:markov-axiom-recursive-ascent):
a recursive symbolic reducer for general $H_n$ words, currently
implemented in `markov_trace_recursive.py` with a known truncation
bug for $n \geq 4$ that does not affect the $H_3$ proton case.
