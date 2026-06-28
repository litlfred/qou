## Path A categorical verification of `18` (proton)

The atomic-shift exponent $\mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_K)$
that controls the $u$-power in the $D(u)$ denominator
([`prop:per-nucleon-shift-additive-linearity`](per-nucleon-shift-additive-linearity.md))
is now categorically verified for the proton by direct symbolic
Hoefsmit pole-order analysis
([`per_irrep_pole_proton_h3.py`](../../../computations/per_irrep_pole_proton_h3.py),
witness:
[`per-irrep-pole-proton-h3.witness.json`](../../../computations/per-irrep-pole-proton-h3.witness.json)):

$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\mathcal{B}_p)\bigr) \;=\; 19 \;=\; 18 \cdot Z + 21 \cdot N + 1 \quad \text{at } (Z, N) = (1, 0).
$$

**Cross-confirmation:** the orthogonal computation in
[`shift_from_nf_basis.py`](../../../computations/shift_from_nf_basis.py)
(NF-basis decomposition, recorded in
[`shift-from-nf-basis.witness.json`](../../../computations/shift-from-nf-basis.witness.json))
independently reports `shift_proton_h3 = 19` — two independent
symbolic methods agree exactly on the per-proton u-pole.

**Multi-nucleon verification (deuteron):**
[`per_irrep_pole_deuteron_h6.py`](../../../computations/per_irrep_pole_deuteron_h6.py)
(witness:
[`per-irrep-pole-deuteron-h6.witness.json`](../../../computations/per-irrep-pole-deuteron-h6.witness.json))
extends Path A to $A = 2$ via three optimisations: cached
symbolic $y_\lambda(q)$ for $n = 6$, auto-cached symbolic
$\chi^\lambda_q(\beta_D)$
([`chi-deuteron-h6.witness.json`](../../../computations/chi-deuteron-h6.witness.json)),
and per-term pole order. The per-term maximum is uniquely $40$
at $\lambda = (4, 1, 1)$, so

$$
  \mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\beta_D)\bigr) \;=\; 40 \;=\; 18 \cdot 1 + 21 \cdot 1 + 1
$$

rigorously (lower-order per-term poles cannot cancel a strict
maximum). Multi-nucleon Path A closed.

The "$18$" in $18Z + 21N + 1$ is the per-proton additive
coefficient of the FULL summed $u$-pole order, not the q-pole
order of any per-irrep $\chi^\lambda_q$ (per-irrep max at $H_3$
is $11$ at $\lambda = (2, 1)$).
