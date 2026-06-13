**Algorithm ($\Delta_\lambda$ closure — open gate).**
*Compute the per-partition binding density $\Delta_\lambda(K)$
for an isotope knot $K$, consumed by Step 9b
([`alg:per-isotope-binding`](#alg:per-isotope-binding)).*

### Input

- *Isotope knot $K$ + braid index $n_K$.*
- *Partition $\lambda \vdash n_K$.*

### Output

- *Per-partition density $\Delta_\lambda(K) \in \mathbb{R}$.*

### Status (2026-06-02)

**Open gate.** Six closure ansätze have been refuted on the
deuteron:

| Ansatz | Source | Refuted on |
|--------|--------|------------|
| Frobenius co-Casimir | Track-A early proposals | deuteron |
| Demazure-fibre | symmetric-crystal early attempts | deuteron |
| LP-Plancherel | LP-based ansatz | deuteron |
| LP-Frobenius | LP-based ansatz | deuteron |
| crystal-graph naïve | KLR / Kashiwara level-0 | deuteron |
| augmented Markov | Markov-extension ansatz | deuteron |

The current direction is **Option E** (Kashiwara crystal, q-Reeb
+ isospin mirror — `option_e_v9.py`), with PROBE 4 cheap-pass
refutation logged on PR #1516 and the full-order $\theta_\lambda$
approach on PR #1726.

### Correctness conditions

*[`prop:term6-binding-density`](#prop:term6-binding-density)
fixes the binding sum's algebraic shape; the open piece is
identifying the categorical realisation of $\Delta_\lambda$.*

*[`conj:crystal-graph-realization`](#conj:crystal-graph-realization)
is the conjectural input under which Option E aims to close the
gate — its monotonicity property mirrors the cemetery-group
emergence pattern (Section: cemetery group).*

### Algorithm (current candidate — Option E v9)

```
1. Build the Kashiwara crystal for sl_{n_K} at the partition λ.
2. Apply q-Reeb deformation and isospin mirror.
3. Extract per-block volume + spectral data.
4. Combine into the Δ_λ candidate.
5. Cross-check against AME deuteron binding.
```

### Witness contract

*No verified witness yet — Option E v9 is candidate code, not
production. Cross-PR coordination tracked in
[`docs/coordination/2026-06-02-mba-appendix-maintenance-contract.md`](../../../docs/coordination/2026-06-02-mba-appendix-maintenance-contract.md);
sibling PRs #1516, #1726, #1714 are active on this gate.*

### Notes

*Per CLAUDE.md "Δ_λ gate (Track A blocker)" rule: **do not
propose a seventh fit-based ansatz**. The three-calibration
discipline review will catch it. Productive directions: GAP-A-3,
GAP-A-4 (categorical brane-tower level selection / ρ general
rule) and Option E (Kashiwara crystal). Full context:
[`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../../../docs/audits/2026-05-18-delta-lambda-gating-context.md).*
