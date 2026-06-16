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
"deriving $\lambda_{\mathrm{scale}}$" — see CLAUDE.md's critical-
framing block on `λ_scale`.*
