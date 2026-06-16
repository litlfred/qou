# Binding is split across ≥3 incompatible trace conventions (2026-06-09)

**Status:** exploratory finding / blocker triage (no production wiring).
This is the **real blocker** for closing per-isotope binding
`B(K) = m_e·Σ_λ y_λ χ^λ(β_K) Δ_λ(K)` — not a compute gap, a
**convention-reconciliation** one. Captured so the next session reconciles
*before* running more sums.

## The finding

Attempting to extend #1742's archimedean abs-sum binding
(`m_e·Σ_λ y_λ|χ^λ(q₀)|`, deuteron +3.6%) to A≥3 surfaced that the binding
effort is scattered across **at least three different `(tr_M, χ^λ)`
conventions that disagree by factors of ~7 in χ** and give wildly
different binding:

| # | convention | deuteron χ^(6) | abs-sum `m_e·Σy\|χ\|` | codebase status |
|---|------------|----------------|----------------------|-----------------|
| **A** | matrix-M parabolic (`chi_via_matrix_m_mpfr`; **PR #2082's tr_M=1.332**) | 11.02 (=q₀²³, sign-only crossings) | **−68%** (deuteron, complete) | the A≥4 χ infra (#2062/#2080) |
| **B** | `mass_at_3A_proper.markov_trace_3A` (Plancherel `d_q²/[3A]_q!`; averaged crossings) | 1.56 | not summed | **DEPRECATED — docstring: "Do not use for new binding calculations"** |
| **C** | `markov_trace_canonical.tr_M_element` (Jones–Markov, `tr_M(σ_0)=z≈0.499`) | — | **never used for the abs-sum** | **the canonical trace** (per B's own deprecation note) |
| (#1742) | its own per-block archimedean realization | — | **+3.6%** | merged |

`markov_trace_3A`'s docstring (mass_at_3A_proper.py:354–365): *"This is NOT
the canonical Jones–Markov trace specified in prop:categorical-mass-markov…
Use `markov_trace_canonical.tr_M_element` for the canonical trace… Do not
use for new binding calculations."*

## Consequences (honest)

- **PR #2082's "canonical tr_M = O(1) = 1.332" is the matrix-M convention
  (A)** — which the codebase does *not* treat as the binding-canonical
  trace. The #2082 correction of #2076 (scale gate is H₃-local) **stands**
  (the H₃-local NF is genuinely not the binding object), but "1.332 is
  canonical" should be qualified: it's matrix-M (A), not Jones–Markov (C).
- **Encoding B is deprecated for binding.**
- **#1742's +3.6%** and the matrix-M abs-sum (−68%) are **not comparable** —
  different χ encodings.
- **The codebase's own canonical trace (C) has never been used for the
  abs-sum binding.** That is the gap.

## The bar product is separately rejected

Independent of the convention question, the owner-proposed trace-level bar
product `tr_M(q₀)·tr_M(q₀⁻¹)` was tested (validated matrix-M machinery,
cross-check `tr_M(deuteron,q₀)=1.33178` exact) and **rejected**: deuteron
`tr_M(q₀⁻¹)=0.00029` (tiny, q<1) → required Δ' = 11245 (underbinds). The
`q→q⁻¹` bar is not the binding realization at any level (extends #1742's
per-block bar negative to the trace). See
[`atom_vhyp_bar_trace_test.py`](../../computations/atom_vhyp_bar_trace_test.py).

## Reusable byproduct

**Validated machinery to compute `tr_M(β_K, q)` at *arbitrary* q** via the
native matrix-M bindings (`trace_weights_n(3A, q)` +
`chi_via_matrix_m_mpfr(λ, word_left, bridge_sign, word_right, k_split=3,
q_str, dps)`), cross-checked to <1e-9. Reusable for whatever object the
reconciliation lands on.

## RESOLUTION (corpus-first, 2026-06-09)

Corpus-grep settles it — the reconciliation is **already done in-repo**, and
this session's binding objects were all **off-convention**:

- **Canonical trace = C**: `computations/markov/markov_trace_canonical.py::tr_M_element`
  (the deprecation pointer was right — it's in `markov/`). Confirmed by the
  canonical content block
  [`markov-axioms-primitive.md`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md)
  (`prop:categorical-mass-markov`): the Jones–Markov trace `τ_M` with
  `z = 1/(√q + 1/√q)`, forced by the four Jones/Wenzl axioms.
- **Canonical binding is ALREADY implemented** in `binding_canonical.py`:

      B(Z,N) = E_0 · ( tr_M(W_free) − tr_M(W_atom) )      [free−bound DIFFERENCE on C]

  — **not** an abs-sum (#1742), **not** a bar product, **not** signed
  `tr_M(atom)` alone (#2082). It already contrasts the Plancherel
  `binding_3A`, the tower, and AME.
- **It's run + witnessed** (`binding-canonical.witness.json`):

  | atom | A | B_AME | B_pred (canonical C) | B_AME/B_pred |
  |---|---|---|---|---|
  | D | 2 | 2.225 | 0.466 | 4.8× |
  | T | 3 | 8.482 | 0.629 | 13.5× |
  | ³He | 3 | 7.718 | 0.658 | 11.7× |
  | ⁴He | 4 | 28.296 | 0.714 | **39.7×** |

  The canonical binding **under-predicts AME by a factor that GROWS with A**
  (4.8×→39.7×). **That growing factor IS the per-nucleus Δ_λ(K)** on the
  canonical convention — small mass error (<1%, since binding is ~1% of
  mass) but large *binding* error.

**Consequence for this session's PRs:** the abs-sum (#1742-aligned), the bar
product (#2082's `atom_vhyp_bar_trace_test`), and the matrix-M signed-tr_M
(`atom_vhyp_closure_matrix_m`) are **off-convention explorations** — they do
not feed the canonical binding. #2082's *correction* of #2076 (scale gate is
H₃-local) still stands; but the Δ̄ numbers there are matrix-M (A), not the
canonical difference. The validated arbitrary-q `tr_M` machinery remains a
useful byproduct.

## Recommendation (next session)

1. **Pin the binding trace to convention C** (`markov_trace_canonical.tr_M_element`)
   — the codebase's stated canonical trace.
2. **Redo #1742's abs-sum and #2082's Δ̄ on C**, consistently, so the
   numbers are comparable.
3. **Coordinate across** #1742 (merged abs-sum), #2080 (A≥4 χ), #2082
   (matrix-M tr_M), and the `markov_trace_canonical` module — they
   currently use different traces. Ledger:
   [`docs/coordination/atom-vhyp-delta-lambda.md`](../coordination/atom-vhyp-delta-lambda.md).
4. **Do not run more abs-sums until C is pinned** — otherwise it's a fourth
   number on an unreconciled pile.
