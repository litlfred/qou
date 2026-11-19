*The operator that adds the $(A{+}1)$-th nucleon to a nucleus of mass number $A$ has a definite knot type:*

| Transition | Operator | Dominant NF | Knot type |
|:----------:|:--------:|:-----------:|:---------:|
| $p \to D$ | $\sigma_0 - h/2$ | $\sigma_0$ | single crossing |
| $D \to {}^3\!H$ | $\sigma_1^{-1}(\sigma_0{-}h/2)$ | $L_-$ | Hopf link |
| $D \to {}^3\!\mathrm{He}$ | $(\sigma_1{-}h/2)\sigma_0$ | $L_-$ | Hopf link |
| ${}^3\!H \to {}^4\!\mathrm{He}$ | $(\sigma_0{-}h/2)(\sigma_1{-}h/2)\sigma_0$ | $e^-$ | trefoil |
| ${}^3\!\mathrm{He} \to {}^4\!\mathrm{He}$ | $(\sigma_0{-}h/2)\sigma_1^{-1}(\sigma_0{-}h/2)$ | $e^-$ | trefoil |

The p-n factors are written $\sigma - h/2$, the $\delta = 0$ convention; the
canonical colour-tube-weighted form is $\sigma - h(1/2 - \delta/4)$, with
$\delta$ the substrate flavour split of
[flavor split substrate proposition](#prop:flavor-split-substrate). **The Dominant NF
and Knot type columns are unaffected.** Recomputing the $H_3$ normal form of all
five operators under both conventions returns the same dominant basis element in
every case, with dominance margins of $4.7\times$ to $9.6\times$ against a
relative perturbation of only $\delta/2 \approx 6.9 \times 10^{-4}$ on the p-n
shift — four orders of magnitude of headroom
([`knot_operator_transition_convention_robustness_probe.py`](../../../computations/probes/knot_operator_transition_convention_robustness_probe.py),
8 assertions). The convention is recorded because the operators are written in
it, not because the conclusion depends on it.

*The knot hierarchy progresses from unknot (1 nucleon) to single crossing (2) to Hopf link (3) to trefoil (4). The 4th nucleon completes the trefoil topology, explaining why ${}^4\!\mathrm{He}$ has the strongest binding per nucleon among light nuclei.* $\square$
