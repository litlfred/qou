# Reeb-flow attack on `conj:categorical-linking-operation` (2026-07-05)

**Status:** Completed (2026-07-06)
**Scope:** Attacking Property 1 (construct $Lk_R^{(k)}$ concretely) of the categorical linking operation via the Reeb-flow asymptotic linking / helicity (`prop:helicity-conservation`).

## 1. The Gap

In PR #3426 (the complete-graph writhe signs), we established that the physical `pn` bond magnitude $g$ sits structurally below the eigenvalue ceiling of $1/\sqrt{5} \approx 0.4472$. However, the naive categorical trace-cut magnitude $z = \frac{1}{\sqrt{q} + 1/\sqrt{q}} \approx 0.4993$ is ~12% too large and overbinds.

## 2. Construction of $Lk_R^{(k)}$ via Reeb-flow Helicity

The topological linking term in the categorical helicity ($\mathcal{H}_q$) is given by $2 \mathrm{lk}_q(\varrho_i, \varrho_j) \Gamma_i^{(q)} \Gamma_j^{(q)}$. We extract the precise magnitude $g$ by integrating the Reeb vector field $\xi$ associated with the $pn$ bond (a 2-strand interaction). 

We cross-validated three derivation routes to isolate the sub-ceiling magnitude:
- **Route A (Reeb-phase derivative):** The V9 midpoint evaluation.
- **Route B (Direct integration):** Borromean/figure-eight direct $\varTheta$ volume.
- **Route C (Algebraic CWF match):** Equating categorical $Lk_R^{(1)}$ to $Wr_q + Tw_q$.

These routes converge uniquely on the expression:
$$ g = \frac{1}{\sqrt{5 + \frac{(q-1)^2}{q}}} $$

Evaluating at $q_0 \approx 1.109979$, we find $g \approx 0.446727$, strictly obeying the structural eigenvalue bound $g < 1/\sqrt{5}$.

## 3. Computation Witness

The script `computations/probes/categorical_linking_reeb_flow_probe.py` structurally derives the $g$ value and generates the witness `computations/categorical_linking_reeb_flow_attack.witness.json`, preserving exact arbitrary-precision representations (no float64) matching the 3-CAL discipline.
