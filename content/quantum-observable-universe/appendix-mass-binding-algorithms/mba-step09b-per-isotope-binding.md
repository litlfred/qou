**Algorithm (Per-isotope binding energy, conditional on $\Delta_\lambda$).**
*Evaluate the binding energy
$B(K) = m_e \cdot \sum_\lambda y_\lambda(q_0)\, \chi^\lambda(K)\, \Delta_\lambda(K)$
for an isotope-coded knot $K$ via the Wedderburn-Frobenius
decomposition plus the per-partition binding density
$\Delta_\lambda$.*

### Input

- *Isotope knot $K$ (canonical braid encoding — see
  Appendix Knot Periodic Table).*
- *Substrate $q_0$, electron mass $m_e$ (CAL-1, CAL-2 anchors).*
- *Per-partition $\Delta_\lambda(K)$ — currently **open**, see
  `alg:delta-lambda-closure` sidecar.*

### Output

- *Predicted binding energy $B(K) \in \mathbb{R}_{> 0}$ in MeV.*

### Algorithm

```
1. Compute the partition-decomposition (Step 5) at the isotope's
   braid index n_K.
2. For each λ ⊢ n_K:
   a. Compute y_λ(q_0) (Wedderburn weight).
   b. Compute χ^λ(K) (Hoefsmit character on the isotope braid).
   c. Look up Δ_λ(K) from the candidate closure ansatz
      (currently: Option-E / crystal — see sidecar).
3. Sum λ contributions and multiply by m_e.
```

### Correctness conditions

1. *[`rem:term6-binding-density`](#rem:term6-binding-density)
   gives the binding-density formula at $q = q_0$.*
2. *[`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
   ties the partition sum to the archimedean MeV observable.*

*The remaining conjectural input is $\Delta_\lambda(K)$ itself —
six closure ansätze (Frobenius co-Casimir, Demazure-fibre,
LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov)
have all failed on the deuteron as of 2026-05-31. The current
direction is Option E (Kashiwara crystal) — see
`alg:delta-lambda-closure`.*

### Complexity

*Dominated by Step 5; same scaling as Step 9a per isotope.
Mass-table sweeps over $A \leq 4$ take seconds.*

### Python API entry point

```python
from qou_mass import predict

p = predict(atom="deuteron", observable="binding_energy")
B = p.value   # MeV
```

*Binding-energy is selected by the `observable` keyword on the
unified `predict()` entry point; there is no separate
`binding_energy(...)` function. The mass-table sweep is the
script [`canonical_mass_table_extended.py`](../../../folio-assistant/computations/canonical_mass_table_extended.py).*

### Witness contract

*Canonical witness:
[`canonical-mass-table-242ppb.witness.json`](../../../folio-assistant/computations/canonical-mass-table-242ppb.witness.json).
Records per-isotope predicted $B(K)$, AME experimental anchor,
the $\Delta_\lambda$ choice used, and a clear flag when
$\Delta_\lambda$ is the open gate.*

### Notes

*This is the **Track A blocker**: $\Delta_\lambda$ closure is the
single open piece preventing the per-isotope binding from
reaching L2 (100× L2 target) for the four currently-missing
observables. See [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../../../docs/audits/2026-05-18-delta-lambda-gating-context.md).*

*Inter-nucleon interface convention (canonical default): the p-n
averaged crossing is **color-weighted**, $\sigma - h\,(1/2 - \delta/4)\cdot\mathbf{1}$
with $\delta = $ `flavor_split_subleading`$(q_0)$ (the substrate
$(m_n - m_p)/M_N$ flavor split), set in
[`mass_at_3A_proper.atom_braid_word_3A`](../../../folio-assistant/computations/mass_at_3A_proper.py)
(`pn_convention="bring_color_weighted"`). The p-p ($\sigma$) and
n-n ($\sigma^{-1}$) interfaces are isospin-distinct and carry no
extra color weight. The color shift is at the $\Delta m_{pn}$ scale
($\delta/4 \approx 3.4\times10^{-4}$) — not the dominant binding
residual, which is the inter-nucleon multiplicity (the $C(A,2)$
bond count) plus per-bond growth. See
[`docs/audits/2026-06-03-color-averaging-wiring-audit.md`](../../../docs/audits/2026-06-03-color-averaging-wiring-audit.md)
and [`docs/audits/2026-06-03-nuclear-a3-dpn-plan.md`](../../../docs/audits/2026-06-03-nuclear-a3-dpn-plan.md).*
