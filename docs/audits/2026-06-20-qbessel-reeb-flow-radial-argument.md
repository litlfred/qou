# The Reeb flow supplies the radial argument — qbk2 reopened (forced + surviving, scale open)

**Date:** 2026-06-20
**Branch:** `claude/qbk2-reeb-flow-radial-2026-06-20`
**Status:** Owner-steered reopening — derive-or-refute, no fit, nothing wired
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md) (binding direction **REOPENED**)
**Supersedes (partially):** PR #2538 R2
**Script:** [`computations/qbeta/qbessel_reeb_flow_radial_forced.py`](../../computations/qbeta/qbessel_reeb_flow_radial_forced.py) (`EXPLORATION COMPLETE`)

## The owner's steer

> "Keep exploring the radial argument. Did you use the Reeb bundle? There is a
> rotational flow on knot operations."

**Direct answer: no — I used the Reeb *phase*, not the Reeb *flow / bundle*.** PR #2538's
R2 claimed "the Markov trace supplies only the angular `θ_λ`, not a radial coordinate."
That was **incomplete**. The owner's correction:

> The rotation/growth split **is** the angular/radial split. The **rotational flow on
> knot operations** (the Reeb flow, ~writhe/framing) supplies the radial datum.

| sector | `r_λ = χ_λ/dim_λ` | `θ_λ` | character |
|--------|-------------------|-------|-----------|
| rotation | `|r_λ| ≤ 1` | `arccos(r_λ)` | a genuine **angle** (phase `e^{iθ}`) |
| growth | `|r_λ| > 1` | `arccosh(|r_λ|)` | a **flow length** (the extensive `q^{writhe}` channel) — **radial** |

So the radial coordinate **is** substrate-forced: `x_λ = θ_λ` (the Reeb-flow length),
with **no map freedom** — #2536's alternatives (`sinθ`, `2sinh(θ/2)`) were non-canonical.

## What changes

Two of the four obstructions that produced #2536's "DO NOT WIRE" are now addressed:

- **#2536 obstruction 1 (the decisive one): RESOLVED.** With the Reeb-flow principle,
  `x_λ = θ_λ` is canonical and `ν_λ = dim_λ − 1` (PR #2538 R1) — **both forced**. The
  63% map-swing was an artifact of considering non-canonical argument maps. The
  correction is now a **single definite number**, not a family.
- **#2538 R2 (radial missing): SUPERSEDED.** The radial datum is the Reeb-flow length.
  (R1 stands: integer order ⇒ the proper 2nd solution is the **log-Neumann** `Y_n`; the
  coincidence propagator `P_λ = (πx/2)J_n(x)Y_n(x)` is well-defined for `x = θ_λ > 0`.)

## Result (deuteron, classical `q→1` first pass)

`δ = Σ_λ [P_λ(x_atom) − P_λ(x_free)]`, `P_λ = (πx/2)J_n(x)Y_n(x)`, `n = dim_λ−1`,
`x_λ = θ_λ`:

| Test | Outcome |
|------|---------|
| **(F) Forced — no knob** | **YES** — `x=θ`, `ν=dim−1` both substrate-fixed |
| **(S) Survives free→atom** | **YES** — `δ = −0.172 ≠ 0` (66% growth-sector; does not cancel) |
| **(C) Right scale** | **not yet** — `δ` is ~4% of `B(D)/m_e ≈ 4.35` (~25× small) |
| **(X) Cross-anchor** | stable (q₀ vs muon-anchor) |

## Honest status — REOPENED, not closed

PR #2538's "binding direction CLOSED" was **premature**; the owner's Reeb-flow steer
fixes the decisive obstruction. The current honest position is **forced + surviving,
scale open**:

- **Solid:** the correction is now genuinely **parameter-free** (F) and **does not
  cancel** (S). That is a real advance over #2536/#2538.
- **Open:** the raw magnitude is ~25× too small **at the classical first pass**. This
  check is crude — it uses **uniform weights** (no `y_λ χ_λ` Markov factor) and the
  **classical `q→1` Bessel**. The large-order suppression (`ν` up to 15 → `J_15(x)Y_15(x)`
  is tiny at `x~1`) dominates, and the substrate q-deformation at `ν=15`, `q₀≈1.11`
  (`q^ν ≈ 4.8`) could change the scale substantially.

## The legitimate next test (NOT a fit)

Promote to the **q-deformed Hahn–Exton log-Neumann** `Y_ν(x;q)` at integer order, with
the **real `y_λ` Markov weights** and the `χ_λ` factor — all **forced** substitutions,
not tuning. If the forced q-deformed + weighted `δ` lands on the binding scale with a
definite bar-parity, the direction promotes to a Lean lemma + wiring candidacy. If it
stays off-scale, the refinement is: the Reeb-flow radial fixes the map but the
**large-order Bessel suppression** is the residual blocker — and whether `ν = dim−1` is
the right order (its largeness drives the suppression) becomes the next scrutiny point.

**Caveat (critical distance):** closing the ~25× gap must come from the *forced*
q-deformation/weights, **not** from choosing a normalization to hit `B(D)`. The moment
the scale is reached only by a tuned prefactor, it is a fit and fails the discipline.

No fit; nothing wired; `c_k`/`Δ_λ` stay cal-anchored. The owner's steer is credited:
the direction is live again.
