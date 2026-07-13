# The c₃ bar-odd `S` as `conj:im-q-physical-role` candidate (iii) — the decay projection `Im(q)`

**Date:** 2026-07-11 · **Branch:** `claude/c3-wall-reeb-rotation-phase-2026-07-11` ·
**Tier:** structural connection + non-fitting extraction (scope-(a); C14; no fit).
**Probe:** [`qbeta_c3_imq_decay_projection_probe.py`](../../computations/qbeta/qbeta_c3_imq_decay_projection_probe.py).
**Origin:** owner lead (2026-07-11) — "physically observed things correspond to
small-ish imaginary q; maybe [the archimedean] projection is this."

## The connection

The lead is exactly **candidate (iii)** of
[`conj:im-q-physical-role`](../../content/quantum-observable-universe/mass-theory/conj-im-q-physical-role.md):
`Im(q)` as the **non-Hermitian / open-system (decay-width Γ)** parameter. The
conjecture records that candidate (iii) "needs a categorical formula for decay
widths Γ." The c₃ bar-odd `S = Q_β/E₀` (the β-decay Q-value) **is** a decay-sector
observable with a categorical (bar-odd trace) formula — the Γ-observable candidate
(iii) was waiting for. So the two open threads join: the **c₃ S wall** (open phase
`arg(u(q₀))`) is candidate (iii)'s **`Im(q)`**.

## The non-fitting test

Is `S` the first-order response of the figure-eight complex volume `Im 𝔙` to a
small imaginary part of `q`? Using only derived ingredients:

- meridian holonomy = multiplication by `q` (#3579, `holonomy_hyperbola`), so the
  deformation `u = 2 log q`;
- leading Neumann–Zagier `Im 𝔙 ≈ (√3/2)|u|² sin(2 arg u)` (`√3` = derived cusp
  shape `τ = 2√−3`, this session's Lean `cuspShape_barOdd_sq`);
- put `q = q₀ + iε`. Then `arg u ≈ ε/(q₀ log q₀)`, so to first order
  `S ≈ (4√3 · log q₀ / q₀) · ε`, giving `ε = S·q₀/(4√3 log q₀)`.

Inverting (S is the input, ε the read-out — **not** a fit of a formula to S):

| anchor | `S` | required `ε = Im(q)` | `Im/Re` |
|---|---|---|---|
| muon | `+0.00968` | `+0.01487` | `+1.34%` |
| proton | `−0.03946` | `−0.06059` | `−5.46%` |

**Small-ish (1–5%) and SIGN-FLIPPED.** The two real `q₀` differ by only `~10⁻⁸`,
so `ε` cannot be a function of `Re(q₀)` at this resolution — it is an **independent
DOF**, exactly as candidate (iii) requires. A real `q₀` can never flip the sign of
`S`; a sign-flipped small `Im(q)` does it naturally. This is the candidate-(iii)
**signature**, and it explains the `dc₃/dq ≈ 4.66×10⁶` hypersensitivity: it lives in
the **imaginary (decay) DOF**, not in `Re(q)`.

## What this does and does not do

- **Does:** gives the wall a physical **identity** (`arg(u(q₀))` = the decay
  projection's `Im(q)`), explains the sign-flip, and realizes candidate (iii)'s
  decay-width test with a concrete categorical observable.
- **Does not:** close the wall. The map `q₀ ↦ ε(q₀)` is the **same** open object as
  `arg(u(q₀))`, re-read as "the decay projection's imaginary part." The `|ε|`
  magnitude is `u`-map-dependent (uses `u = 2 log q`); a different derived `u(q)`
  rescales `|ε|`, but the **sign-flip is robust** (`= sign S`, preserved by any
  monotone response). Robust claim: required `Im(q)` is small (1–5%) and
  sign-flipped; exact magnitude conditional on the `u`-map.

## No conflict with `Im(q₀) = 0`

`lusztig_q_0_imaginary_part_zero` fixes `Im(q₀) = 0` for the **bar-even mass**
evaluation. That is untouched: masses are the value **at** `Im(q) = 0`; the bar-odd
decay `S` is the **`∂/∂Im(q)` response**. `conj:im-q-physical-role` itself states
`Im(q₀) = 0` is a convention "pending an Im-sensitive measurement" — `S` is that
measurement. Nothing is wired; no `c_k` value; the conjecture stays a conjecture.

## Cross-references

- Wall structure: [`2026-07-11-c3-wall-branch-structure.md`](2026-07-11-c3-wall-branch-structure.md)
- Reeb angle: [`qbeta_c3_reeb_rotation_phase_probe.py`](../../computations/qbeta/qbeta_c3_reeb_rotation_phase_probe.py); `rem:figure-eight-reeb-theta-value`
- Cusp shape `barOdd² = −3`: #3573 / #3579 `CuspShapeBarParity.lean`
- Nuclear-model / Elliott context: [`observations/q-deformed-nuclear-models-comparison.md`](../../content/quantum-observable-universe/observations/q-deformed-nuclear-models-comparison.md)
