# Sidecar re-triage, 2026-11-21: knots-particles-confinement

Scope: the 15 stale statement (`proof-narrative-lean-equiv`) and proof
(`da-non-sequitur`) verdicts in this chapter. Method as in #8766: read the diff
since each verdict, re-stamp wording-only changes, review the rest in full,
and check every block against `docs/coordination/owner-rulings.md`. Reviewer id
`agent:sidecar-review-2026-11-21`.

## Re-stamped (9)

Wording-only diffs; the earlier result stands and the new evidence names the diff.

- stable-atom-decidable-proof (no text change), hadron-exists-proof ('Hopf-link'
  dropped), c-equals-bar-iff-all-1dim, compound-beta-shell-calibration,
  shell-schur-weyl-self-duality-proof, fermion-boson-knot-link-proof,
  atom-knot-exists-proof, pairwise-interaction-decomposition-proof.
- c-equals-bar-iff-all-1dim-proof: re-stamped fail, with a ruling note (below).

## Full review (6)

| block | before | now | why |
|---|---|---|---|
| electroweak-triplet-charge-spin-from-involution | fail | **pass** | The class now carries only inputs, and charge and sector label are computed from them. Every md claim has a sorry-free Lean theorem. |
| …-proof | fail | **pass** | The self-contradicting bar-parity step is gone. Minor: the closing σ₅⁸ section argues a different claim. |
| hoefsmit-ew-cell-content | fail | **pass** | The vacuous `: True` carrier is replaced. All four items are proved over a generic ring. |
| confinement-level-unique | pass (no evidence) | pass | Antisymmetry, `ConfinementLevel.unique`. |
| lepton-meson-torus-knot-dictionary | fail | fail | Still lookup tables plus `rfl`. **Conflicts with the electron ruling** (below). |
| …-proof | fail | fail | Same conflict. Empirical proxies are still in the table after the proof. |

## Conflicts with current owner rulings

- **lepton-meson-torus-knot-dictionary** (statement and proof). These blocks
  make the electron the trefoil T(2,3), the closure of σ₁³ in H₂(q). The
  2026-11-21 ruling makes it σ₀σ₁σ₀ ∈ B₃ with Hopf-link closure, and keeps
  the trefoil only as a backup. The first row of the table, and the "lepton
  sector = H₂" reading, need the owner's decision or a rewrite.
- **c-equals-bar-iff-all-1dim-proof** says H₂ is "the lepton sector", which is
  the same out-of-date reading. The statement is false for other reasons in
  any case.

None of the 15 uses the photon form or the Lagrangian trace.
