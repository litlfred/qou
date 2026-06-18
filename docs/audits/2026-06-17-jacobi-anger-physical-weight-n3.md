# Jacobi–Anger §4a test with physical Wenzl weights (n=3) — 12.8% → 6.8%, tower gate sharpened

**Date:** 2026-06-17
**Compute:** [`qbeta_reeb_tower_jacobi_anger_physical_weight.py`](../../computations/qbeta/qbeta_reeb_tower_jacobi_anger_physical_weight.py)
**Status:** derive-or-refute result, TIERED. Nothing wired; c_3 stays cal-anchored.

## Context

The n→∞ brane-tower contraction keystone identifies the bar-odd brane-tower sector
with the Hahn–Exton q-Bessel (E_q(2) contraction) matrix coefficient. The sharp
falsifiable test is §4a of
[`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md):
the bar-odd `sinh((2m+1)η)` coefficients should be the Bessel values `2·J_{2m+1}(x)`
at a single substrate-fixed `x = x(q₀)`, reproduced at both anchors with no refit.

The committed witness `qbeta-reeb-tower-jacobi-anger.witness.json` ran §4a only on the
**unit-weighted** block sum — over-determination residual **0.128 (12.8%)** — with an
explicit note that this is *"NOT the physical Wenzl-weighted Markov trace."* So the
physical version of §4a was an open gap.

## Result

Running §4a with the **physical Wenzl/Jones–Markov weights** `y_λ(q₀)` (the weights
that actually appear in `tr_M = Σ_λ y_λ χ^λ`), at n=3:

| weighting | over-determination residual (single x) |
|---|---|
| unit (committed witness) | 0.128 (12.8%) |
| **physical y_λ (this)** | **0.0684 (6.8%)** |

- Solving `x` from the scale-free ratio `W_3/W_1 = J_3(x)/J_1(x)` gives
  `x* ≈ 4.5249` at both anchors; the predicted `W_5/W_1 = J_5(x)/J_1(x)` then misses
  the actual `W_5/W_1` by **6.8%**.
- Cross-anchor single-x swing is **1.8e-9** (the proton/muon anchors differ by ~1.3e-8,
  so x* tracks q₀ smoothly — no per-anchor refit needed at this truncation).
- The physical bar-odd order-3 coefficient `W_3 ≈ −1/4` is essentially anchor-stable.

## Reading (TIERED — refinement + sharper gate, NOT a closure)

1. **The physical weighting moves toward the q-Bessel structure.** Halving the
   residual (12.8% → 6.8%) when the arbitrary unit weights are replaced by the
   *physical* tr_M weights is supporting evidence that the real object is closer to the
   single-x Bessel form than the unit toy — not proof, but a directional signal.

2. **n=3 truncation alone does NOT close it (6.8% ≫ 1%).** This is exactly the audit's
   own caveat: a single `λ⊢3` trace is a finite sum of a few `sinh(kη)` terms — *not* a
   Bessel function. The Bessel object is the **infinite brane-tower**, carrying orders
   `7, 9, …` from levels `n = 6, 9, 12, …` that the n=3 truncation omits.

3. **The decisive gate is now sharp: does the residual → 0 as the tower extends?**
   The single-x over-determination residual, recomputed with physical weights at
   `n = 3, 6, 9, 12`, must **shrink monotonically toward 0** if the bar-odd tower is
   the q-Bessel contraction object. A residual that **plateaus or grows** with `n` is a
   clean refutation, on the same footing as the f-map and the unit-weighted run,
   quantified. This is the formalize-first gate that should run **before** any
   master-theorem Lean (the `lim_{n→∞} spectrum = q-Bessel zeros` formalization is
   premature until the numerical convergence is established).

## Discipline

- No fit (the ratio solve is a derive-or-refute over-determination check, not a curve
  fit); TIERED; nothing wired; c_3/Q_β stay cal-anchored regardless.
- Bessel here is the **ordinary** `J_ν` of the Jacobi–Anger identity (the proved
  `q→1` backbone, `ReebTowerJacobiAnger.lean`); the Hahn–Exton q-Bessel refinement at
  finite q is the next layer once the ordinary-J tower convergence is settled.

## The decisive tower test — precise requirement + blocker (2026-06-17; object-ID corrected 2026-06-18)

> **Object-identification corrected 2026-06-18** — see the CORRECTED section below.
> The `chi_block` are the **explicit `χ_λ(𝓑_n − 𝓑_p)`** typed-braid difference
> (Lean-proved closed forms), **not** the SDP-selector `Δ_{T_β}`. The requirement +
> blocker below are restated accordingly.

Following the chain to nail what the n→∞ convergence gate actually needs:

- The n=3 `chi_block_{3,21,111}` are `χ_λ(𝓑_n − 𝓑_p)(q)` — the per-Wedderburn-block
  characters of the **explicit typed-`B₃` neutron-minus-proton braid difference**
  (Hoefsmit seminormal; `chi-per-irrep-cyclotomic-closed-forms.lean`, source witness
  `qbeta-per-block-paper-closed-forms.witness.json`; `qbeta_utils.chi_block_*`). These
  are first-principles Lean-proved closed forms, **not** the min-norm SDP selector
  `T_β` of `qbeta_decay_sdp_solver.py`. The bar-odd orders {1,3,5} at n=3 are the
  Laurent degrees of those closed forms.

- The tower-convergence test therefore requires `χ_λ(𝓑_n − 𝓑_p)` for **λ⊢6 and λ⊢9**:
  weight by `y_λ(q₀)`, bar-odd-decompose into `sinh(ℓη)` (orders up to 11, 17), and
  re-run the single-x over-determination check. The keystone holds iff the residual
  shrinks monotonically (6.8% at n=3 → … → 0).

- **Blocker (corpus-verified):** there is **no H₆/H₉ `χ_λ(𝓑_n − 𝓑_p)`** in the
  corpus — the explicit proton/neutron braids are defined only at H₃ (the n=6 hits
  are all `computations/_deprecated/`). Producing them at H₆/H₉ requires **embedding
  the typed-crossings braids `𝓑_p`, `𝓑_n` at brane-tower levels 6, 9** (first-
  principles braid construction), then evaluating `χ_λ` per Wedderburn block — not a
  mechanical character evaluation, but **not** "extend the SDP fit" either. Then this
  script's `physical_W` + `solve_single_x` (and the harness's `bar_odd_coeffs`) apply
  unchanged.

So the n=3 physical-weight result here is the **furthest the gate can be advanced
without the H≥6 typed proton/neutron braids** — and it pins exactly what unblocks
the rest.

## ~~CRITICAL-DISTANCE FINDING — the tower object is FIT-derived~~ — CORRECTED (2026-06-18)

> **This section's original claim was a MISATTRIBUTION; struck through and
> corrected below.** The original 2026-06-17 text asserted the §4a tower object
> is the min-norm SDP fit `T_β ∝ t`. That is wrong: it traced the wrong script.
> The reconciliation work (`qbeta_jacobi_anger_tower_general.py`, 2026-06-18)
> established the correct provenance.

### What was claimed (2026-06-17, INCORRECT)

The note traced `χ_λ(Δ_{T_β})` → `qbeta_per_block_symbolic.py:101-105` (which
loads `T_beta_nf_coefficients` from `qbeta-decay-sdp-knot-operator.witness.json`)
→ `qbeta_decay_sdp_solver.py` min-L2 solution `T_β ∝ t`, and concluded the §4a
tower object is an empirical fit.

### What is actually true (2026-06-18, CORRECTED)

The §4a bar-odd data does **not** come from the min-norm `χ_λ(T_β)`. Both the
committed unit-weighted run (`qbeta_reeb_tower_jacobi_anger.py`) and the
physical-weight run (`qbeta_reeb_tower_jacobi_anger_physical_weight.py`) take
their per-block characters from `qbeta_utils.chi_block_{3,21,111}` /
`qbeta_per_block_paper_closed_forms.py`, which are the **explicit
`χ_λ(𝓑_n − 𝓑_p)`** — the typed-`B₃` neutron-minus-proton braid difference
(`𝓑_p` uud, `𝓑_n` udd), with closed forms

```
χ_(3)(𝓑_n−𝓑_p)     = -(q²+1)²(q²-1)/(4q)
χ_(2,1)(𝓑_n−𝓑_p)   = -(q⁴+1)(q²-1)/(4q³)
χ_(1,1,1)(𝓑_n−𝓑_p) = -(q²+1)²(q²-1)/(4q⁵)
```

that are **Lean-proved sorry-free** (`chi-per-irrep-cyclotomic-closed-forms.lean`,
`field_simp + ring`; content block `chi-per-irrep-cyclotomic-closed-forms.md`).
Their bar-odd sinh-decomposition gives the `BAR_ODD_COEFFS` `{(3):{3:-¼,5:-¼},
(2,1):{1:½,3:-½}, (1,1,1):{3:-¼,5:-¼}}` exactly (verified symbolically in
`qbeta_jacobi_anger_tower_general.bar_odd_coeffs`). The min-norm `χ_λ(T_β)` (a
*different* object in `qbeta_per_block_symbolic.py`) has q₀-dependent numeric
coefficients, **not** these clean rationals — confirming the two are distinct and
that the §4a test uses the explicit braids, not the fit.

**Corrected consequence.** The §4a tower object is **first-principles** (the
explicit typed-crossings proton/neutron braids; Lean-proved closed forms), *not*
a min-norm fit. The remaining honest caveat is one level deeper: the typed-
crossing assignments themselves (uud = 6σ+3σ⁻¹+2 avg; udd = 5σ+4σ⁻¹+2 avg) are a
*braid model* of the flavour content, not derived from the substrate — but that is
categorically different from an L2 fit to reproduce Q_β (the braids are built from
the flavour structure, not fitted to the answer). So a converging tower **would**
bear on the keystone (it tests a first-principles object), not merely on a fit.

## Reconciliation — general harness reproduces 6.8% (2026-06-18)

`qbeta_jacobi_anger_tower_general.py` previously used the WRONG object — the
min-norm autocorrelation `Σ_w t_w·τ_M(T_w)(q)` (= `τ_M(T_β)` for `T_β∝t`,
*y-varying*) — and did not reproduce 6.8%. It now builds the correct §4a object:
the proved `χ_λ(𝓑_n−𝓑_p)` closed forms, bar-odd-decomposed symbolically, weighted
by `y_λ(q₀)` **frozen** at the substrate anchor (§4a's `Σ_ℓ w_ℓ sinh(ℓη)` form
requires η-independent `w_ℓ`, which forces frozen y). It reproduces the
physical-weight residual **0.0683508** and `x* ≈ 4.5249` at **both** anchors
(swing 1.8e-9), with the symbolically-derived `BAR_ODD_COEFFS` asserted equal to
the hardcoded set. The two harnesses now compute the same object.

### Two forward paths (precise specs, corrected)

**Path A — extend the first-principles `χ_λ(𝓑_n−𝓑_p)` to λ⊢6,9 (TIERED).**
The blocker is *not* "extend the SDP fit". It is: produce `χ_λ(𝓑_n−𝓑_p)` at
λ ⊢ 6, 9 by embedding the typed-crossings proton/neutron braids `𝓑_p`, `𝓑_n` at
brane-tower levels 6, 9, then `bar_odd_coeffs` + `physical_W` + `single_x_residual`
apply unchanged (y stays frozen at q₀). No such higher-tower braid (nor proved
closed form) exists in the corpus today, and the typed-braid character infra is in
`computations/_deprecated/` — so reviving/extending it is the genuine work. The
general-n Markov-trace machinery (`validate_markov_infra`, via `pyhecke_native`) is
validated and ready to consume those braids once they exist.

**Path B — first-principles substrate-derivation of the typed-crossing braid
model.** Deeper than Path A: derive the uud/udd crossing assignments themselves
from the substrate (rather than taking them as the flavour braid model). This is
the level at which the remaining (model-not-fit) caveat above would close.
