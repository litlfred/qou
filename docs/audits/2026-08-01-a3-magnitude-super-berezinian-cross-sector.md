# A=3 magnitude ROUTE 2 — the super-Berezinian even/odd cross-sector mixing supplies `r*` only as a FIT (scope-(a) underdetermination) (2026-08-01)

**Branch:** `claude/a3-magnitude-super-berezinian-cross-sector-2026-08-01`.
**Bean:** `qou-6r6d`. **Feeds:** the super-DM / Berezinian wall
(`qCubicGradedSplit`, bean `qou-jqof`, PR #4140, off-main). **Constraint, not
closure. No fit wired. `free_parameters = 0` in every derived reading.**

## The question

The A=3 magnitude factor
`r* = μ₃/c₃ ≈ 1.585` (`μ₃ = +0.4708` MeV, the AME residual 3-body moment,
additive-residual simplex #4320; `c₃ = +0.297` MeV, the single-trace derived
Borromean H₉ cluster deficit #4364) is **bracketed out of every single-Markov-
trace ingredient** — LEVEL, geometric `W_λ`, coordination-EDGE, exact-order
`μ̄_A`, and the Vassiliev finite-type weight all give the same `c₃ = 0.63·μ₃`
(`option-e.md`, the 2026-07-26/-08-01 rows). The last row records the missing
`1.585×` "needs structure outside the single-deficit filtration (e.g. an
**operator-valued cross-channel combiner**)". ROUTE 2 tests the *only* genuinely
cross-**sector** candidate: the super-Berezinian even↔odd mixing term
`t = B·D⁻¹·C` coupling the bar-even (cosh / mass / C1) and bar-odd (sinh / decay
/ GGM) faces (hook `qou-1dnr`).

## What was already established (parity — NOT re-proved here)

The cross-term's **parity** is fully worked on main; this route is the distinct
**magnitude** angle:

- `QOU.QBeta.OddDecayWeightParity` (`2026-07-25-odd-face-parity-constraint.md`)
  — `t = g·γ` is bar-ODD; its classical `q=1` shadow vanishes
  (`classical_shadow_on_even_face`).
- `QOU.QBeta.BerezinianSelfAdjointCrossTerm`
  (`2026-07-31-berezinian-selfadjoint-crossterm-bar-even.md`) — a self-adjoint
  off-block pair `C = −σB` forces `t` bar-EVEN (`|B|²/D`); a genuinely bar-ODD
  `c₃` therefore requires **non-self-adjoint, INDEPENDENT** off-blocks `B, C`
  (≥ 2 free amplitudes).

## The result (magnitude)

**The even-face multiplicative correction `(A − t)/A` the cross-term supplies is
a FREE parameter of the off-block.** Lean
`QOU/QBeta/SuperBerezinianA3Magnitude.lean` (sorry-free, `lean`-direct exit 0,
generic `[Field R]`, §7c-clean):

| decl | statement |
|------|-----------|
| `evenFaceCorrection_no_mixing` | block-diagonal (`B = 0`) → correction `≡ 1` (no lift) |
| `evenFaceCorrection_eq_one_iff` | for `A ≠ 0`, correction `= 1` ⟺ `t = 0` (a lift needs a nonzero cross-term) |
| **`crossTerm_magnitude_surjective`** | **for fixed nonzero `A, C, D`, `B ↦ (A − B·D⁻¹·C)/A` is SURJECTIVE onto `R`** — any target (incl. `r*`) is hit by `B = A(1−r)DC⁻¹` |
| `A3CrossTermMagnitudeClosed` | §3b-tax **dependent** conjecture, **NO instance** — the DM-cubic-*derived* (not fitted) off-block yields the physical magnitude; closing it IS `qou-jqof` |

Two structural readings frame the verdict:

1. **Why single-trace is bracketed.** Any block-diagonal / single-Markov-trace
   ingredient has `t = 0` ⇒ correction `≡ 1` — it *cannot* move the coefficient
   at all. This is the structural reason LEVEL / `W_λ` / EDGE / `μ̄_A` /
   Vassiliev all sit at the same `0.63×`.
2. **Why the cross-term is not a magic bullet.** The cross-term is the *unique*
   source of a lift, but its size is unconstrained: the correction map is onto.
   Bar-oddness already forces `B, C` independent (≥ 2 free amplitudes), so the
   route can hit any sign *and* any magnitude. Reaching `r*` pins one real
   combination of `B, C` — a **fit**.

## Empirical companion (`a3_magnitude_berezinian_crossterm_probe.py`, 0 fit)

Witness `a3-magnitude-berezinian-crossterm.witness.json`:

- `r* = 1.5852 ≈ log₂3 = 1.5850` — a flagged irrational coincidence
  (`VassilievMagnitudeA3.no_integer_weight_eq_rStar`), not a target.
- No mixing (`t = 0`) → correction `= 1.0000` (the single-trace bracket).
- **0/13** natural parameter-free substrate readings of `ρ = t/A`
  (`ℏ_q, h, h², (1+q)/2−1, ±(odd/even ratio), ±1, ±2`) land `r*` within 2%; the
  corrections scatter across `0.0 … 3.0`. No natural substrate constant sits at
  the required `ρ = 1 − r* = −0.585`.
- The fit witness `B* = A(1−r*)DC⁻¹ = −0.585` reproduces `r*` exactly — the
  surjectivity map made concrete.

`μ₃/c₃` are never inverted to *derive* a substrate constant; the probe
DEMONSTRATES the free-parameter structure, it does not fit-to-close.

## Verdict — scope-(a), honest negative on closure

The super-Berezinian cross-term does **not** *derive* `r*`. Its magnitude is set
by the off-diagonal mixing blocks `B, C`, which the framework does not derive —
that derivation IS the open keystone `conj:qdifference-kernel-prolongation-symbol`
/ `qCubicGradedSplit` (`qou-jqof`). Matching `r*` is one real constraint on an
unconstrained off-block, i.e. a **fit**; the magnitude is a **hidden degree of
freedom** (Rule 14), directly analogous to the q-dim-convention hidden DOF
(`option-e.md`, 2026-06-28).

This is **not** a scope-(b) exclusion: unlike every bracketed single-trace
ingredient (all give a parameter-free `0.63×`), the cross-term CAN reach `r*` —
it is the **first A=3-magnitude route not excluded on magnitude grounds**. But
it **relocates** the wall from "which single trace" to "**derive the mixing
blocks `B, C`**". That wall (`qou-jqof`) stays open; only a *derived* off-block
(from the Bring DM q-cubic period datum) would turn the correction into a
prediction rather than a fit.

**Net for the magnitude gate.** The cross-channel combiner the `option-e.md`
Vassiliev row invoked as the escape from the finite-type bracket is structurally
*available* (it reaches `O(1)`), but it introduces exactly the free amplitudes
that make `r*` a fit. Closing A=3 magnitude therefore reduces — with no residual
single-trace slack — to the DM-cubic derivation of the graded off-blocks. No
seventh fit-based ansatz; nothing wired; `μ₃`/`c₃` never inverted.
