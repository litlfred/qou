# Option B scoping — H₃ ⊂ H₄ Bratteli induction-restriction multiplicities

**Date:** 2026-06-04
**Trigger:** PR #1808 Option E audit ("Most promising lead: Markov / induction axis, specifically the box-adding induction functor `Ind_{H₃}^{H₄}` under the Markov trace") + PR #1762 §5 Option B.
**Sibling:** PR #1816 (Option A) — the data-side counterpart that just confirmed the H₃→H₄ gap empirically across {p, n, D, T, ³He, ⁴He} at A=1..4 (`Δper-block` grows from −57 % to −95 %; `Δuniform` stays tight at +2.8 to +3.7 %).
**Scope of THIS document:** read-only scoping doc + a cheap, EXPLORATORY probe plan. No production code change.

---

## §1. The H₃ → H₄ jump (recap)

PR #1762 §2 identified the **derivation gap** at the heart of the
`Geom_full` bridge:

- The proton braid lives in **H₃** (3-strand braid `𝓑₃`).
- Production `linking_weight_family_a(q)` = `(3q²+4+3q⁻²)/4 ≈ 2.53`
  is the **H₄** half-Wedderburn count = `(1/2) · Σ_{λ⊢4} dim_q(V_λ)` —
  it sums over partitions of **4**, not 3.

Why H₄ and not H₃? An UNEXPLAINED jump in the production code.
The Option A diagnostic (PR #1816) now confirms it's a load-bearing
choice: dropping the H₄ count (per-block route) undershoots m_p by
2.38× — and grows to 21× undershoot at ⁴He.

PR #1808's literature-import audit
([`2026-06-04-h3-h4-jump-literature-import.md`](./2026-06-04-h3-h4-jump-literature-import.md))
located the most-promising direction as the **box-adding induction
functor** `Ind_{H₃}^{H₄}` under the Markov trace `tr_M`, and proposed
this cheap experiment as its concrete test.

## §2. The Bratteli induction-restriction diagram

The Hecke algebra tower

  H₀ ⊂ H₁ ⊂ H₂ ⊂ H₃ ⊂ H₄ ⊂ …

is multiplicity-free; the branching is the **box-adding diagram on
Young diagrams**:

```
λ ⊢ n  ──Ind──▶  {λ⁺ : λ⁺ ⊢ n+1, λ⁺ obtained by adding one box}
λ ⊢ n  ──Res──▶  {λ⁻ : λ⁻ ⊢ n-1, λ⁻ obtained by removing one box}
```

For `n = 3 → 4` the box-adding from the 3 partitions of 3 reaches
the 5 partitions of 4:

```
  λ ⊢ 3        boxes added         λ⁺ ⊢ 4
  ─────        ───────────         ──────
  (3)          □(end)              (4)
  (3)          □(below row 1)      (3,1)
  (2,1)        □(end of row 1)     (3,1)
  (2,1)        □(end of row 2)     (2,2)
  (2,1)        □(below row 2)      (2,1,1)
  (1,1,1)      □(end of row 1)     (2,1,1)
  (1,1,1)      □(below row 3)      (1,1,1,1)
```

Seven box-additions from 3 partitions of 3 to 5 partitions of 4. The
**induction multiplicity** `m_{λ⁺ ← λ}` is 1 when `λ⁺/λ` is a single
box (which it always is in the Hecke / S_n tower — they're skew shapes
of size 1), 0 otherwise.

## §3. The Markov-weighted box-adding hypothesis

The Family-A `linking_weight_family_a(q)` is:

  λ_A(q) = (1/2) · Σ_{λ⁺ ⊢ 4} dim_q(V_{λ⁺}) = (3q² + 4 + 3q⁻²)/4

(The 5/2 = `(3+4+3)/4·1` = `(λ⊢4 dim_q sum at q=1)/4` = `2·5/4` is
half the q=1 H₄ Wedderburn dimension; the `(3/4)·h²` is the q-expansion
of the same sum around q=1.)

**Question:** can this be derived as a Markov-weighted box-adding sum
over the H₃→H₄ Bratteli step? Concretely:

  Σ_{λ⊢3} [some weight w(λ)] · Σ_{λ⁺ ⊃ λ} [some kernel K(λ⁺, λ)] · dim_q(V_{λ⁺})

with weights `w(λ)` natural to the Markov-trace structure
(`y_λ` Wenzl-bridge weights, or `χ^λ(e)/dim λ` projector weights, or
the symmetric-power Schur traces) and `K(λ⁺, λ)` natural to the
induction functor (1 if `λ⁺ ⊃ λ`, 0 otherwise; or the Pieri rule
multiplicity, which equals 1 for single-box additions).

**Sub-hypothesis B1 (cleanest):** `λ_A = (1/2) · Σ_{λ⊢3, λ⁺⊃λ} dim_q(V_{λ⁺})`
without per-edge weighting — the **uniform** box-adding sum. If this
recovers `(3q² + 4 + 3q⁻²)/4`, it derives the H₄ count purely
combinatorially from H₃ via induction.

**Sub-hypothesis B2:** the same with `w(λ) = y_λ(q)` — the Markov-trace
weighting. The Markov-trace identity (Wenzl) says the
H_{n+1} trace of a stabilised braid equals an H_n trace times a
scalar; this might force a specific weighting.

**Sub-hypothesis B3 (refutation of "uniform" framing):** the box-adding
sum is NOT translation-invariant — there is a special `λ_special ⊢ 3`
that the proton braid actually inducts FROM, and the sum is just
`Σ_{λ⁺ ⊃ λ_special} dim_q(V_{λ⁺})`. Tests: the Wenzl branching identity
already implemented in `wedderburn_jones_markov.y_lambda_at` and the
`canonical_tr_m_via_chi_cache.py` summation might already encode this.

If all three are refuted, the box-adding axis is wrong and the H₃→H₄
jump comes from somewhere else (Markov stabilization analog at the
trace level, not the algebra-tower level).

## §4. Cheap probe plan

A self-contained `mpmath`/`sympy` probe that:

1. **Builds the H₃→H₄ Bratteli induction map** from partitions of 3 to
   partitions of 4 — pure combinatorics (Young-diagram box-adding); no
   Hecke algebra construction needed.
2. **Loads `dim_q(V_λ)` for λ ⊢ 4** symbolically in q (5 values, all
   classical — the q-hook-length formula via
   `wedderburn_jones_markov` or direct hook-length product).
3. **Evaluates the three sub-hypotheses** B1 / B2 / B3 symbolically and
   numerically at q₀:
   - B1: uniform sum
   - B2: y_λ-weighted sum (loads y_λ ⊢ 3 from `y-lambda-at-q0.witness.json`
     for the q₀ point; symbolic via `y_lambda_at(3)` for the q-form)
   - B3: per-source-λ test (does any single λ ⊢ 3's box-additions give
     2.53 alone?)
4. **Compares to `linking_weight_family_a(q)`** — does the closed-form
   `(3q²+4+3q⁻²)/4` emerge from B1, B2, or B3?
5. Emits `option-b-h3-h4-bratteli-probe.witness.json` with verdicts
   per sub-hypothesis (REFUTED / SUPPORTS / EXACT-MATCH).

EXPLORATORY: production untouched, no Δ_λ-gate ansatz (the
box-adding combinatorics is structural, not a per-partition fit).

## §5. Owner decision NOT needed for this PR

Unlike Option A — where the per-block flip changes `m_p` — this probe
is purely **combinatorial/algebraic**. It either derives `λ_A` from a
known structural identity (in which case PR #1762 §2's H₃→H₄ gap
closes) or refutes the box-adding axis (in which case Option E's
analysis advances by eliminating one candidate).

No production code changes either way. The PR is doc + probe + witness.

## §6. Sibling coordination

- **PR #1816 (Option A)** — provides the empirical signal this probe
  tries to explain (the +2.8 to +3.7 % uniform overshoot vs the
  57-95 % per-block undershoot). When this probe completes its
  verdict will be cross-referenced back to #1816's interpretation
  text.
- **PR #1808 (Option E literature-import)** — proposed this exact
  experiment as the cheapest concrete test of the Markov-induction
  axis. This PR is the deliverable.
- **PR #1762 (1ppQ roadmap)** — Option B from §5; the probe closes or
  refutes one of the five attack options.
