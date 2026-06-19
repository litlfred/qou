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
   b. Compute χ^λ(K) via the Step 3 fine-Bratteli transfer matrix
      (lossless over all λ ⊢ n_K; no d_λ Hoefsmit rep materialised).
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
have all failed on the deuteron. The current
direction is Option E (Kashiwara crystal) — see
`alg:delta-lambda-closure`.*

### Complexity

*The $\chi^\lambda$ trace (step 2b) is computed by the Step 3
transfer matrix — a fine-Bratteli edge sweep (a few thousand edges
at $n = 21$), not the $d_\lambda$-dimensional Hoefsmit
representation — so the per-isotope cost is the partition count
$p(3A)$ times that sweep, not $n!$. Mass-table sweeps therefore
reach $A \geq 6$ ($^6$Li $\approx 0.2$ s, $^7$Li $\approx 0.6$ s),
where the former per-basis-vector path hit the $d_\lambda$ wall
(markov\_peel $\approx 17$ min at $^6$Li). The open gate is
$\Delta_\lambda$ (step 2c), not the trace compute.*

### Python API entry point

```python
from qou_mass import predict

p = predict(atom="deuteron", observable="binding_energy")
B = p.value   # MeV
```

*Binding-energy is selected by the `observable` keyword on the
unified `predict()` entry point; there is no separate
`binding_energy(...)` function. The mass-table sweep is the
script [`canonical_mass_table_extended.py`](../../../computations/canonical_mass_table_extended.py).
Its `--method auto` routes per-atom over the mixed nucleon+composite
set: free nucleons ($A < 2$) use the direct $H_3$ Hoefsmit path
`laurent_q_rust` (pyhecke-native Rust + MPFR); composites ($A \geq 2$)
use the `branching` combiner, whose $\chi^\lambda$ comes from the
operator-valued Wenzl recursion at $A = 2$ and the lossless
fine-Bratteli transfer matrix at $A \geq 3$ (`chi_monotone_transfer` —
all $p(3A)$ partitions at 50 dps, no $d_\lambda$ wall, pure mpmath, with
the color-weighted p-n crossing handled internally). All routes are MPFR
at the 50-dps floor; `auto` is the only setting that spans a table mixing
free nucleons and composites in one run.*

### Witness contract

*Provisional witness:
[`canonical-mass-table-242ppb.witness.json`](../../../computations/canonical-mass-table-242ppb.witness.json).
Records per-isotope predicted $B(K)$, the AME experimental anchor,
and an explicit `open_gate = delta_lambda` flag marking
$\Delta_\lambda$ as the open Track-A gate. It is a hand-authored
summary (`auditOnly`, no producer run): the $B(K)$ values are not a
derived $\Delta_\lambda$ result and await a producer-backed
regeneration once the $\Delta_\lambda$ closure lands.*

### Notes

*This is the **Track A blocker**: $\Delta_\lambda$ closure is the
single open piece preventing the per-isotope binding from
reaching L2 (100× L2 target) for the four currently-missing
observables. See [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../../../docs/audits/2026-05-18-delta-lambda-gating-context.md).*

*Inter-nucleon interface convention (canonical default): the p-n
averaged crossing is **color-weighted**, $\sigma - h\,(1/2 - \delta/4)\cdot\mathbf{1}$
with $\delta = $ `flavor_split_subleading`$(q_0)$ (the substrate
$(m_n - m_p)/M_N$ flavor split), set in
[`mass_at_3A_proper.atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py)
(`pn_convention="bring_color_weighted"`). The p-p ($\sigma$) and
n-n ($\sigma^{-1}$) interfaces are isospin-distinct and carry no
extra color weight. The color shift is at the $\Delta m_{pn}$ scale
($\delta/4 \approx 3.4\times10^{-4}$) — not the dominant binding
residual, which is the inter-nucleon multiplicity (the $C(A,2)$
bond count) plus per-bond growth. See
[`docs/audits/2026-06-03-color-averaging-wiring-audit.md`](../../../docs/audits/2026-06-03-color-averaging-wiring-audit.md)
and [`docs/audits/2026-06-03-nuclear-a3-dpn-plan.md`](../../../docs/audits/2026-06-03-nuclear-a3-dpn-plan.md).*

*Production wiring (atom-trace compute): the canonical color-weighted
$\mathrm{tr}_M(\beta_{\text{atom}})$ feeding step 2b is assembled by
[`tr_m_atom_via_transfer.tr_m_atom_zn`](../../../computations/tr_m_atom_via_transfer.py),
through which the binding consumers
[`binding_canonical`](../../../computations/binding_canonical.py)
(default path) and
[`canonical_tr_m_via_branching`](../../../computations/canonical_tr_m_via_branching.py)
($A \geq 3$) now route — replacing the symbolic `tr_M_element` and
the native `chi_lambda_all_partitions_mpfr` per-partition paths.
Lossless (all $p(3A)$ partitions kept; the active-set truncation is a
$\sim10^{-3}$ error rejected for 1-ppQ per
[`docs/audits/2026-06-10-binding-active-set-compute-optimization.md`](../../../docs/audits/2026-06-10-binding-active-set-compute-optimization.md)),
validated $\mathrm{tr}_M$-transfer $\equiv$ full Hoefsmit
(`char_fast`) to $4.7\times10^{-15}$.*
