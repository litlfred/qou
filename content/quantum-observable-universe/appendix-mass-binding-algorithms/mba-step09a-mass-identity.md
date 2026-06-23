**Algorithm (Mass identity at $q = q_0$).**
*Evaluate the categorical mass scalar
$\mathfrak{m}(K) = m_e \cdot \mathrm{VolDensity}(K, q_0)$
for a knot $K$ via the canonical chain
Steps 1 $\to$ 5 $\to$ 7 $\to$ 8 $\to$ here.*

### Input

- *Knot $K$ as a closed braid word $w_K \in B_n$ (canonical
  choice: $\mathcal{B}_3$ for the proton, the figure-eight for
  the neutron, etc.).*
- *Substrate parameter $q_0 \in \mathbb{R}_{> 1}$ (CAL-2 anchor).*
- *Electron mass $m_e$ in MeV (CAL-1 anchor).*

### Output

- *Predicted mass $\mathfrak{m}(K) \in \mathbb{R}_{> 0}$ in MeV.*

### Algorithm

```
1. Compute Markov trace tr_M(NF(w_K)) symbolically (Steps 1–3).
2. Wedderburn-decompose into Σ_λ y_λ(q) · χ^λ (Step 5).
3. Apply GB filtration / E_2 collapse to identify the leading
   geometric factor VolDensity(K, q) (Steps 7–8).
4. Evaluate at q = q_0 with default 65-dps mpmath precision.
5. Multiply by m_e (MeV).
```

### Correctness conditions

1. *[`prop:mass-identity-exists`](#prop:mass-identity-exists) gives
   existence of the mass identity in the QOU premise.*
2. *[`prop:mass-identity-unique`](#prop:mass-identity-unique) makes
   the identity unique modulo the calibration choice.*
3. *[`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
   ties the categorical scalar to the archimedean MeV observable.*

### Complexity

*Dominated by Step 5 (Wedderburn). End-to-end wall time on the
proton ($\mathcal{B}_3$) is sub-second on the native Rust core
at 65 dps.*

### Python API entry point

```python
from qou_mass import predict

m_proton_MeV = predict(atom="proton").value
```

### Witness contract

*Canonical witness:
[`per-observable-100x-status.witness.json`](../../../computations/per-observable-100x-status.witness.json).
Records per-observable predicted mass, experimental anchor, ratio
$\sigma_{\mathrm{pred}} / \sigma_{\mathrm{exp}}$ vs the 100× L2
target, and the L1 cross-method agreement.*

### Notes

*Current status: 3/7 observables meet L2 (m_p, m_e, m_K / m_π);
m_p shows a +2.89 % gap to CODATA after the proton-anchor re-pin.
The open R&D is **refining `VolDensity($\mathcal{B}_3$)`**, not
"deriving $\lambda_{\mathrm{scale}}$" — see AGENTS.md's critical-
framing block on `λ_scale`.*

*Linking-weight component = one per-component selection rule.* The
linking-weight factor of $\mathrm{VolDensity}$ is
$\mathrm{lw}(c) = \frac{1}{c+1}\sum_{\lambda \vdash c+1} \dim_q V_\lambda$
(canonical q-hook $\dim_q$), reproducing the established anchors
$\mathrm{lw}(1)=1$ (muon) and
$\mathrm{lw}(3) = (3q^2+4+3q^{-2})/4$ (proton, Family-A — **bit-for-bit**
equal to the production `linking_weight_family_a`), and giving the new
$c=2$ (2-component link, e.g. Hopf) value
$\mathrm{lw}(2) = (q+1)^2/(3q)$
([`prop:selection-rule-c2-prediction`](../climax-volume-mass/selection-rule-c2-prediction.md)).
Unified + regression-tied to production by
[`binding_selection_rule_tau_closure.py`](../../../computations/binding_selection_rule_tau_closure.py)
$\to$ [witness](../../../computations/binding-selection-rule-tau-closure.witness.json).
The same $\mathrm{lw}(c)$ values are the SW-period anchors of the depth-2
binding kernel — see [`mba-step09b`](mba-step09b-per-isotope-binding.md).*
