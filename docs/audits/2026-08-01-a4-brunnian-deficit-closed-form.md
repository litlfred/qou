# A=4 Brunnian deficit — the closed form, derived exactly (the measured leg promoted)

**Date:** 2026-08-01
**Branch:** `claude/quantum-observable-formalization-dif0iv` · PR #4458
**Axis:** Δ_λ / Option-E sign leg · Milnor-parity sign law (#4389 follow-up)
**Free parameters introduced:** 0 · **Nothing wired** · derive-then-check

## The gap

[`2026-07-27-deltalambda-milnor-parity-sign-law.md`](2026-07-27-deltalambda-milnor-parity-sign-law.md)
(#4389) formalised the A-indexed Brunnian cluster law

* leading Milnor order `= 2(A−1)`,
* deficit sign `= (−1)^(A−1)`,

with a deliberate and honest **epistemic split**: A=3 **PROVED** from the closed
form `1 − τ_Borr = h⁴(3+h²)/(h²+4)`, A=4 only **MEASURED**
(`τ_L₄ ≈ 1.000145898`, leading order a log-log *slope estimate* `≈ 6.06`). That
file recorded the A=4 inputs as `def`s, not theorems, precisely so no declaration
would restate a measured value as an established premise (the
"conditional-proved ≠ premise-established" discipline).

The open item was therefore: **derive the A=4 closed form**, so the second data
point of the law stops being a measurement.

## What was done

New probe
[`computations/deltalambda/a4_brunnian_deficit_closed_form.py`](../../computations/deltalambda/a4_brunnian_deficit_closed_form.py)
(witness `a4-brunnian-deficit-closed-form.witness.json`) derives the perblock
deficit `1 − τ_A` **exactly**, for both known A, through one identical pipeline:

* **Words.** The genuine Brunnian band commutators `w₃ = [A₀₁, A₁₂]` and
  `w₄ = [[A₀₁, A₁₂], A₂₃]` — the same objects the measuring probe used. The
  reproduced band factors are **asserted against the measuring witness's recorded
  `band_factors`**, so the word is provably the same object, not a lookalike.
* **Exact characters.** `χ_λ` from the **symbolic** Hoefsmit seminormal form over
  `ℚ(q)`; `y_λ` the symbolic Jones–Markov weights. Same perblock convention
  `g = Σ_λ y_λ |χ_λ|` as the measurement.
* **The absolute value, resolved not assumed.** `w₃`/`w₄` are *pure* braids, so
  `χ_λ(q=1) = dim_λ > 0`; the probe verifies by exact rational arithmetic that
  every `χ_λ` is strictly positive across a `q`-grid spanning `(1, q₀]`, whence
  `|χ_λ| = χ_λ` and the deficit is an honest rational function.
* **The right variable.** The `y_λ` carry half-integer `q`-powers, so the deficit
  is rational in `s = √q`, not in `q`. Working in `s` is what makes the algebra
  tractable (see §Cost below).
* **Leading order by valuation, not series.** With `D(s) = N(s)/M(s)` cancelled
  and `M(1) ≠ 0`, the vanishing order is the exact multiplicity of the root
  `s = 1` in `N` — plain polynomial expansion, no floating-point series. Since
  `q = s²` has `dq/ds|₁ = 2 ≠ 0`, the order in `(s−1)` **equals** the order in
  `(q−1)` (a local diffeomorphism); the leading *coefficients* differ by exactly
  `2^order`, and the probe reports both.
* **Sign by exact rational arithmetic.** Pinning a **rational** `s₀` makes
  `q = s₀²` an exact rational agreeing with `q₀` to ~20 digits, so the deficit at
  the pin is exactly rational and its sign carries no floating point at all.

## Result

| A | leading `(q−1)`-order | leading `(q−1)` coeff | deficit sign at `q₀` | `τ_A(q₀)` |
|---|---|---|---|---|
| 3 | **4** `= 2(3−1)` | `+12` | `+` (exact rational) | `0.998366623` |
| 4 | **6** `= 2(4−1)` | `−96` | `−` (exact rational) | `1.000145898` |

Two independent confirmations that the pipeline is sound:

1. **A=4 reproduces the independent measurement.** `τ_L₄(q₀) = 1.000145898` from
   the exact symbolic pipeline matches the f64 `pyhecke_native` measurement
   (`a4-h12-brunnian-deficit-measure.witness.json`) to the recorded precision.
2. **A=3 reproduces the corpus's proved behaviour** (positive deficit, order 4)
   through the *same* code path — and its `(s−1)` leading coefficient `192`
   converts to `192/2⁴ = 12`, matching an independent pure-`q` run of the same
   pipeline. The `2^order` conversion is therefore checked, not assumed.

## The epistemic upgrade

* **Order law now exact at both known A.** At A=4 it was a slope estimate
  `≈ 6.06`; it is now the exact valuation `6`.
* **A=4 sign now derived.** The leading coefficient is `−96 < 0` at *even* order
  `6`, so `1 − τ₄ < 0` on a punctured neighbourhood of `q = 1`
  (`(q−1)⁶ > 0` there) — a structural statement, independent of any pin — *and*
  the sign is exactly negative at the substrate pin. Previously the sign entered
  the law only as the measured `tauL4Measured > 1`.

Recorded in Lean, sorry-free:
[`QOU/MassTheory/BrunnianDeficitLeadingOrderDerived.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BrunnianDeficitLeadingOrderDerived.lean).

**Structure of that file (a correction worth recording).** The first version
stated things like `leadingCoeff 4 < 0 := by decide` over a hardcoded `−96`.
That is **not a theorem** — `leadingCoeff 4` is *defined* to be `−96`, so the
statement is true by unfolding and says nothing about the physics; it is exactly
the "true by `rfl`/`decide` ⇒ notation, not a proof" anti-pattern of AGENTS.md
§8 (Strict Lean Discipline), and dressing witness output as a proved theorem is
the laundering the anti-fit rules forbid. Five of nine declarations had that
shape.

The file now splits the two sides so their agreement is **falsifiable**:

* `witnessedOrder` / `witnessedLeadingCoeff` — **DATA**, transcribed from the
  witness; they assert nothing.
* `leadingOrder = 2(A−1)` / `paritySign = (−1)^(A−1)` — **THE LAW**, defined
  without reference to the data.
* `law_reproduces_witnessed_order`, `law_matches_witnessed_sign` — the agreement
  theorems. These **can fail**: a witnessed order of `5`, or a *positive* A=4
  coefficient, would not compile. That is the content, and it is the actual
  scientific claim (the law predicts what the computation found).

Genuinely general lemmas are kept as such: `leadingOrder_even` (∀ A), and the
ordered-ring "sign is carried by the leading coefficient at even order" lemma
with its A=4 instantiation.

## What is NOT claimed (scope)

* **The closed form is not re-derived inside Lean.** It is a degree-34 rational
  function in `s`; Lean records the derived *leading data* and proves the
  arithmetic of the law from it. The exact closed form lives in the witness.
* **The general-`A` law remains a conjecture.** Two data points do not establish
  `2(A−1)` / `(−1)^(A−1)` for all `A`.
  `MilnorParitySignLaw.MilnorParitySignConjecture` still carries it and **no
  instance is provided**.
* **This is not a Δ_λ closure.** It fixes the A=4 *sign and order* of the
  irreducible Brunnian cluster; the per-λ magnitude gate is untouched and remains
  open (`docs/coordination/option-e.md`). Scope-(a) throughout.
* **Nothing is wired to production.** No dashboard, no mass/binding path consumes
  this.

## Cost note (long-compute discipline)

The derivation took four configurations to land; each failure was diagnostic and
is recorded because the failure modes are reusable:

1. **`sympy.factor` hung** (>2 h) on the degree-127/2-in-`q` A=4 expression. The
   factored form was cosmetic → replaced by `cancel`.
2. **`sympy.series` stalled** on the same object → replaced by exact numerator
   valuation (§above), which completes in well under a second.
3. **A too-strict assertion** (`sign evaluation must be exactly rational`)
   aborted an otherwise-good run → replaced by exact-when-possible with a
   documented high-precision fallback under an explicit margin guard.
4. **A real bug — stray `q`.** The `y_λ` cache round-trips through
   `str()` → `sympify()`, which **loses the symbol's assumptions**: the parsed
   `Symbol('q')` is a *different object* from `Symbol('q', positive=True)`, so
   `subs(q, s²)` silently missed every `y_λ` term and stray `q` survived into the
   deficit (surfacing much later as a `Relational` truth-value error on a
   `q**51`-bearing expression). This is why the **cold** run worked and the
   **cached** runs did not. Fixed by unifying the symbol on load, with a guard
   asserting the deficit's only free symbol is `s` — so any future leak of this
   class fails at the source rather than ~8 minutes downstream.

Wall cost is dominated by the symbolic `y_λ(4)` solve (~17 min), now cached.

## Cross-references

- [`2026-07-27-deltalambda-milnor-parity-sign-law.md`](2026-07-27-deltalambda-milnor-parity-sign-law.md) — the law + the epistemic split this promotes.
- [`2026-07-26-deltalambda-a4-h12-brunnian-measure.md`](2026-07-26-deltalambda-a4-h12-brunnian-measure.md) — the f64 measurement now reproduced exactly.
- [`2026-07-26-deltalambda-borromean-3body-cluster.md`](2026-07-26-deltalambda-borromean-3body-cluster.md) — the A=3 proved leg.
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — the still-open Δ_λ magnitude gate.
