# Keystone tower-convergence gate — Path A (n=6) + Path B (substrate crossing model)

**Date:** 2026-06-18
**Branch:** `claude/keystone-tower-n6-gate-2026-06-18`
**Upstream:** builds on #2453 (merged) — the §4a physical-weight reconciliation.

## Where this starts (banked by #2453)

The bar-odd brane-tower keystone identifies the bar-odd sector with the
Hahn–Exton q-Bessel (E_q(2) contraction) matrix coefficient. The sharp §4a test:
the bar-odd `sinh((2m+1)η)` coefficients should be `2·J_{2m+1}(x)` at a single
substrate-fixed `x(q₀)`. #2453 established:

- The §4a tower object is **first-principles**: `χ_λ(𝓑_n − 𝓑_p)` — the explicit
  typed-`B₃` neutron-minus-proton braid difference (`𝓑_p` uud, `𝓑_n` udd),
  Lean-proved sorry-free closed forms (`chi-per-irrep-cyclotomic-closed-forms.lean`).
  **Not** the min-norm `T_β∝t` SDP fit (that was a misattribution, corrected).
- At n=3 (orders {1,3,5}), the single-x over-determination residual is **6.8%**
  with the physical Wenzl weights `y_λ(q₀)` **frozen** at the substrate anchor.
  Both harnesses (`qbeta_reeb_tower_jacobi_anger_physical_weight.py` and the
  reconciled `qbeta_jacobi_anger_tower_general.py`) compute this same object.

The decisive gate: recompute the y-frozen single-x residual at **n = 6, 9, 12**.
**Shrinks → 0 monotonically** ⇒ the bar-odd tower IS the q-Bessel contraction
object (keystone support). **Plateaus / grows** ⇒ clean refutation.

## Path A — extend `χ_λ(𝓑_n − 𝓑_p)` to λ⊢6 (then 9)

### A0. Formalize-first gating question (DO THIS BEFORE ANY n=6 COMPUTE)

The orders {7,9} the q-Bessel object needs live at λ⊢6 (more strands). But
`χ_λ(𝓑_n − 𝓑_p)` is only defined at H₃ today. **The gate is not well-posed until
the level-6 proton/neutron braids `𝓑_p^{(6)}`, `𝓑_n^{(6)}` are defined.** Per the
formalize-first discipline (CLAUDE.md), pin this structurally before scanning:

- **What is "brane-tower level 6"?** Candidate constructions to adjudicate against
  the corpus (NOT to invent): (i) Markov/Wenzl stabilization of the B₃ baryon braid
  (add strands with canonical crossings); (ii) a di-baryon / 3+3 strand product;
  (iii) an existing categorical brane-tower construction in the framework. The
  answer must come from the corpus's brane-tower definition, not a fresh ansatz.
- **Invariant check:** whatever the embedding, it must reduce to `𝓑_p`, `𝓑_n` at
  n=3 and preserve the bar-odd parity structure (the `sinh` sector). A candidate
  that breaks bar-parity or fails the n=3 limit is refuted up front.
- **Output of A0:** either a pinned, corpus-grounded definition of `𝓑_{p,n}^{(6)}`
  (⇒ proceed to A1), or a finding that the framework does not yet define the
  higher-tower baryon braids (⇒ that IS the gate's blocker; Path B / a categorical
  brane-tower construction is then prerequisite).

### A1. Revive/extend the typed-braid character compute to n=6

`χ_λ(𝓑)` for typed braids (with averaged crossings `½(σ+σ⁻¹)`) was computed by
the now-`_deprecated/` infra (`atomic_braid_to_crossings`, `q_character_on_braid_word`,
`probe_per_wedderburn_block_ck.py`). For λ⊢6 (d_λ up to 16), build the Hoefsmit
seminormal matrices, evaluate `χ_λ(𝓑_n^{(6)} − 𝓑_p^{(6)})(q)` per Wedderburn block.

### A2. Run the gate

`bar_odd_coeffs` (symbolic Laurent → sinh) + `physical_W` (y-frozen at q₀) +
`single_x_residual` from `qbeta_jacobi_anger_tower_general.py` apply UNCHANGED.
Report the residual at n=6 vs the n=3 baseline 6.8%, TIERED. Then n=9 if feasible.

## Path B — derive the uud/udd typed-crossing model from the substrate

The remaining honest caveat (#2453): the uud/udd crossing assignments
(`𝓑_p` = 6σ+3σ⁻¹+2 avg; `𝓑_n` = 5σ+4σ⁻¹+2 avg) are a **flavour braid model**, not
substrate-derived — categorically different from an L2 fit to Q_β, but not yet
first-principles at the crossing-count level. Path B derives the crossing
assignments from the substrate flavour structure. This is the deeper tranche and
also informs A0 (the higher-tower braid should inherit the same derivation).

## Discipline (standing)

- Three-calibration; no 7th fit. The gate is derive-or-refute with a cross-anchor
  check; a per-anchor refit is a refutation, not a result.
- Formalize-first: A0 (pin the braid embedding) gates A1/A2 (the compute).
- TIERED (proved / near-match / fitted). Nothing wired; c_3/Q_β stay cal-anchored.

## Status

- [x] #2453 reconciliation merged (n=3 baseline 6.8%, object corrected to first-principles).
- [ ] A0 — corpus-ground the level-6 proton/neutron braid embedding (formalize-first).
- [ ] A1 — typed-braid χ_λ compute at λ⊢6.
- [ ] A2 — run the n=6 gate; report residual vs 6.8% (TIERED).
- [ ] Path B — substrate derivation of the uud/udd crossing model.
