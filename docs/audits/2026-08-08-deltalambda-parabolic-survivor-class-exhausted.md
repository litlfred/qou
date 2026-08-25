# The Δ_λ parabolic/skew-quotient survivor class is exhausted (2026-08-08)

**Tier:** compute probe (exact enumeration) · **Wired:** nothing · **No fit, no AME inversion.**
Producer: [`deltalambda_parabolic_survivor_enumeration.py`](../../computations/deltalambda/deltalambda_parabolic_survivor_enumeration.py) ·
witness: `computations/deltalambda/deltalambda-parabolic-survivor-enumeration.witness.json`.

Follows on from
[`2026-07-25-deltalambda-perpair-bond-scalar.md`](2026-07-25-deltalambda-perpair-bond-scalar.md)
(PR #4300), which proved the single-knob two-anchor no-go sorry-free and closed
by naming the surviving candidate class:

> *"parabolic / skew quotients of `[A]_q!` whose truncation level is `A`-locked by
> a stated principle (not a fitted knob)"*

**That class is now enumerated exhaustively, and it is empty.**

---

## 0. What was already closed — not re-run here

The 07-25 audit proved, sorry-free (`JetFiltrationTwoAnchorNoGo.lean`):

- **(S) step-lock** — `[4]_q ≥ 4` for all `q ≥ 1`, AME-independent
- **(M) monotonicity** — `ρ_grad(3)` and `ρ_grad(4)` both increase in `q`
- **(N) two-anchor no-go** — reaching `ρ_strong(3)` forces overshooting
  `ρ_strong(4)`, margin 2.2196
- **SU(4) row restriction** `ℓ(λ) ≤ 4` is **vacuous** for `A ≤ 4`

The W5 workplan item *"Lean-state the invariant any graded-dimension family must
satisfy"* is therefore **done**, not open. None of it is re-derived below.

## 1. Why the enumeration is finite

The 07-25 audit framed `q` as "the knob". In production it is not a knob at all:
the substrate is pinned to the experimental proton anchor
`q₀ = 1.1099785827513808` (AGENTS.md §q₀-anchor, owner directive 2026-08-07).

At fixed `q`, a parabolic quotient of `[A]_q!` is determined by a composition `μ`
of `A` — the `q`-multinomial `[A]_q! / ∏ᵢ [μᵢ]_q!`, the Poincaré polynomial of the
corresponding partial flag variety. There are `2^{A−1}` compositions of `A`, so the
entire class at `A ≤ 4` is **2 + 4 + 8 = 14 objects**, and a candidate family is one
composition per `A`: **64 families**. That is a table, not a search.

## 2. Result

Targets (DERIVED-ELSEWHERE comparison constants, isospin/Coulomb-corrected AME
#3986/#3990 — used **only as bounds**, never inverted):

```
rho_strong(3) = 3.8128     rho_strong(4) = 13.0316
required step  rho(4)/rho(3) = 3.41786
det cap (must exceed):  rho_3 > 3,  rho_4 > 6
```

| quantity | value |
|---|---:|
| candidate families | 64 |
| clearing the determinant cap | 19 |
| landing **both** anchors within 1% | **0** |
| within 5% of the required **step** | **0** |

The closest families reproduce the 07-25 numbers exactly (`ρ₃ = 3.34203`, −12.35%;
`ρ₄ = 15.7396`, +20.78%) — i.e. the `[A]_q!` case itself — which is the
consistency check that the enumeration is measuring the right object.

## 3. The sharp statement — a gap in the step spectrum

The informative quantity is not the anchor errors but the **step** `ρ(4)/ρ(3)`.
At fixed `q₀` the parabolic class realises a **discrete** set of steps, and the
required 3.41786 sits in a gap:

```
nearest achievable steps:   2.23207   and   4.70958
required:                   3.41786
```

It is not near either end — it is roughly in the middle of an empty interval,
34.7% above the lower and 37.8% below the upper. So the failure is not "close but
needs a small correction"; the class does not have a member of the right *shape*,
and no `A`-locking principle can conjure one, because every principle can only
select among these 14 objects.

This strengthens (N) in a specific way. (N) says the single `q`-knob cannot land
both anchors. This says that even *granting* an arbitrary `A`-dependent choice of
parabolic truncation — exactly the freedom the 07-25 audit hoped would supply the
missing `A`-dependent damping `d(A)` — the resulting step is still never right.

## 4. Scope — what is and is not excluded

**Scope-(a).** The parabolic/skew-quotient class is exhausted **as a single per-`A`
multiplier**. That is what was proposed and that is what is closed.

It is **not** a structural exclusion of these objects as *ingredients*. Per
AGENTS.md §"Before declaring refuted", permanence principle 2: a compositional or
additive object is already many-body, and showing a term insufficient by itself
says nothing about whether it belongs in a multi-term closure. `[A]_q!` and its
parabolic quotients may still appear as **factors inside** a larger closure —
in particular alongside the separate additive ≥3-body extensive term that the
2026-08-02 Δ_λ audit identified as the actual missing object. Nothing here
forbids that, and no invariant is cited that would.

What this does remove is the specific hope carried forward from 07-25 §3: that a
principled `A`-locked truncation of `[A]_q!` is the damping. It is not.

## 5. Anti-fit statement

`ρ_strong(3)` and `ρ_strong(4)` appear only as comparison bounds. **No composition
was selected on the anchors** — the enumeration is exhaustive and reports every
family, including the failures, ranked by error. Selecting the best-fitting
composition and wiring it would be the forbidden seventh ansatz; the point of an
exhaustive enumeration is precisely that there is nothing to select.

Nothing is wired; no content block, no tier change, no production edit.

## 6. Where the Δ_λ magnitude now stands

- **Value:** proved, sorry-free, general-`n` (`Δ_λ = (−1)^{n(λ)}·dim V_λ`).
- **Lower side:** exchange-determinant-cumulant family machine-excluded.
- **Upper side:** `[A]_q!` closed by the single-knob no-go (07-25); its
  parabolic/skew quotients closed here.
- **Still open:** the additive, non-normalized, irreducibly ≥3-body extensive
  term. Both sides of the two-sided bracket are now closed as *single multipliers*,
  which is consistent with — and sharpens — the 2026-08-02 conclusion that the
  missing object is **not** a per-block reweight of any kind.
