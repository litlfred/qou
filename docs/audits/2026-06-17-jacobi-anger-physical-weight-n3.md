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

## The decisive tower test — precise requirement + blocker (2026-06-17)

Following the chain to nail what the n→∞ convergence gate actually needs:

- The n=3 `chi_block_{3,21,111}` are `χ_λ(Δ_{T_β})(q)` — the per-Wedderburn-block
  characters of the **T_β operator-selected element** over H₃ (Hoefsmit seminormal;
  `QBetaPerBlockChiClosedForms.lean`, source witness
  `qbeta-per-block-paper-closed-forms.witness.json`). T_β is the SDP shape-collapse
  selector (`T_β = S·1`, `qbeta_decay_sdp_solver.py`), not a single generator —
  hence the bar-odd orders {1,3,5} at n=3.

- The tower-convergence test therefore requires `χ_λ(Δ_{T_β})` for **λ⊢6 and λ⊢9**:
  weight by `y_λ(q₀)`, bar-odd-decompose into `sinh(ℓη)` (orders up to 11, 17), and
  re-run the single-x over-determination check. The keystone holds iff the residual
  shrinks monotonically (6.8% at n=3 → … → 0).

- **Blocker (corpus-verified):** there is **no H₆/H₉ per-block selector character**
  in the corpus — `Δ_{T_β}` is defined only at H₃ (the n=6 hits are all
  `computations/_deprecated/`). Producing `χ_λ(Δ_{T_β})` at H₆/H₉ requires **extending
  the T_β operator-selection (SDP shape-collapse) to those levels** — genuine
  keystone-level work (the SDP selector at higher H_n), not a mechanical character
  evaluation. This is the precise spec for the next tranche: extend
  `qbeta_decay_sdp_solver` to H₆/H₉, emit `χ_λ(Δ_{T_β})` per λ, then this script's
  `physical_W` + `solve_single_x` apply unchanged.

So the n=3 physical-weight result here is the **furthest the gate can be advanced
without the H≥6 T_β selector** — and it pins exactly what unblocks the rest.

## CRITICAL-DISTANCE FINDING — the tower object is FIT-derived (2026-06-17)

Tracing the provenance of `χ_λ(Δ_{T_β})` (the n=3 `chi_block`, hence this whole
tower test) shows it is built on a **min-norm empirical fit**, not a first-
principles object:

- `qbeta_per_block_symbolic.py:101-105` computes `χ_λ(T_β)(q)` by loading
  `T_beta_nf_coefficients` from `qbeta-decay-sdp-knot-operator.witness.json`.
- `qbeta_decay_sdp_solver.py:90-94` sets that `T_β` as the **min-L2-norm**
  solution `x* = (n_target/(t·t))·t` of the single scalar constraint
  `t·x = Q_β/E_0` — i.e. `T_β ∝ t` (the Markov-trace vector). The script
  flags it (lines 20-24): *"the cleanest form of T_β that reproduces Q_β…
  Path 3 would derive T_β from the typed-crossings braid structure rather than
  from a min-norm SDP — that would give T_β as a first-principles object rather
  than an empirical fit."*

**Consequence.** The bar-odd sector tested here is the c₃ near-match/fit sector,
and "extend the SDP selector to H₆/H₉" extends a fit. A fit-tower converging to
q-Bessel would be *suggestive* but would **not close the keystone** (fit ≠
derivation); a non-convergence would show the keystone needs the first-principles
object. Report TIERED, fit-caveat explicit.

### Two forward paths (precise specs)

**Path A — extend the min-norm fit to H₆/H₉ (TIERED, fit-caveated).**
The NF/GS basis of `H_n` is `{T_w : w ∈ S_n}` (dim `n!`): 6 at H₃, **720 at H₆,
362 880 at H₉**. For level n: enumerate reduced words `w∈S_n`; per word compute
`τ_M(T_w)(q)` (Markov trace) and `χ_λ(T_w)(q)=tr ρ_λ(T_w)` (seminormal) as
functions of q; form `T_β=(n_target/(t·t))·t`, `χ_λ(T_β)=Σ_w x*_w χ_λ(T_w)`;
then `physical_W`/`solve_single_x` (this PR) apply. H₆ is feasible (720 words,
d_λ≤16); **H₉ symbolic is likely infeasible** (362 880 words) — needs a
trace-contraction closed form for `Σ_w τ_M(T_w)ρ_λ(T_w)` first.

**Path B — first-principles Δ_{T_β} (the real keystone, open even at H₃).**
Derive the β-decay selector from the typed-crossings braid structure (Path 3 of
the SDP-solver roadmap), so `Δ_{T_β}` is a canonical braid element, not a
min-norm fit. Only then does the tower-convergence test bear on the keystone
rather than on the fit. This is the honest keystone-closing direction.
