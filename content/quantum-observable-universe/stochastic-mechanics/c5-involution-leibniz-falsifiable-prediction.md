## Falsifiable prediction

Any future rung $c_k$ at $k \geq 8$ whose order $\hbar_q^{2k}$
coincides with an **averaging-resonance** position (= a $k$-fold
cyclic substructure including at least one averaged crossing)
will pick up similar $1/2$ fingerprints.

Specifically, the proton braid has 11 typed crossings: 7 pure
$\sigma_0$, 4 pure $\sigma_1$, 1 averaged $\sigma_0$ (at coefficient
$-h/2$), 1 averaged $\sigma_1$ (at coefficient $-h/2$), 3 inverted
$\sigma_1^{-1}$ (at coefficient $-h$). The averaging-resonance
rungs are determined by the positions where two averaged crossings
interact at a given order in $\hbar_q^{2k}$.

By combinatorial counting of pairs of averaged positions among the
11 typed crossings, the predicted averaging-resonance rungs are
those $k$ for which $\binom{2}{2} \cdot (\text{combinatorial weight})$
peaks. **$k = 5$** is the first; subsequent peaks predicted at
**$k = 8, 11, \ldots$** (every 3 rungs by the 3-strand
sub-braid combinatorics).

This is testable by extending SDP-$T_\beta$ extraction to $k \geq 8$
and checking whether c_8 has a $1/2$ fingerprint — the probe is
queued in
[`computations/qbeta/qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py).
