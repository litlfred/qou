*Interpretation of the [one-dimensional QOU channel](#def:one-dim-qou-channel).*

The information transmitted by a single fibre is encoded in its braid word $\beta$. The receiver reads out the Markov trace $\mathrm{tr}_M(\beta)$. The **capacity** of the channel is therefore the entropy of the reachable trace image. This counts the number of distinguishable values $\mathrm{tr}_M(\beta)$ can take as $\beta$ ranges over the admissible braids on the fibre's $n$ strands. Braid words sharing the same trace are indistinguishable to the receiver. Capacity counts trace-classes, not raw braids.

Each elementary crossing provides at most the operational entropy $\eta_q = (2q-1)/q^3$ of information. The capacity of an $n$-strand fibre carrying a length-$\ell$ braid is bounded by $\ell\,\eta_q$ $q$-bits. This realizes the one-dimensional specialisation of the Bekenstein and Bremermann limits. 

Parallel fibres do not interact. The total capacity is strictly additive. The joint Markov trace of $k$ cladded fibres multiplies, meaning their log-capacities add. A bundle of $k$ independent fibres carries $k$ times the single-fibre rate. This is the categorical analogue of the classical rule that independent channels add their capacities.
