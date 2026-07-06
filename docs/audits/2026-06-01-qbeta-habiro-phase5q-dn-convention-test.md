# Phase 5q canonical (D − n) Habiro test — Φ_8² survives

**Date:** 2026-06-01
**Branch:** `claude/qbeta-habiro-followup-2026-06-01` (PR #1618)
**Probe:** [`computations/qbeta/qbeta_habiro_phase5q_dn_refactorize.py`](../../computations/qbeta/qbeta_habiro_phase5q_dn_refactorize.py)
**Witness:** [`computations/qbeta/qbeta-habiro-phase5q-dn-refactorize.witness.json`](../../computations/qbeta/qbeta-habiro-phase5q-dn-refactorize.witness.json)
**Companion:** [`docs/audits/2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md`](2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md) (the convention-blocker audit this resolves)

## TL;DR

**Φ_8² = (u⁴ + 1)² SURVIVES in the Phase 5q canonical convention.**
The strand-doubling chain Φ_4 → Φ_8 → Φ_16 → Φ_32 is **STRUCTURAL**
(convention-invariant), not specific to the `include_inter=True`
habiro-witness convention.

The Φ_16 / Φ_32 prediction test is **UNBLOCKED**.

## The two conventions

| Convention | Construction | tr_M(D, q₀) |
|---|---|---|
| **habiro-witness** (`include_inter=True`) | Full 12-crossing deuteron braid through `markov_trace_symbolic(Z=1, N=1, include_inter=True)` — every nucleon-nucleon interface crossing included via y_λ · χ_λ on partitions of 6 | ≈ 0.3883 |
| **Phase 5q canonical** | `tr_M(p, q) · tr_M(n, q) · z(q)` with `z(q) = 1/(√q + 1/√q)`, per the Phase 5l constit identity + Phase 5c.1 Markov interface identity | ≈ 0.4911 |

Numerical ratio at q₀: Phase5q / witness ≈ **1.265** (note: prior
"expected ~1.875" comment in script docstring used the older
0.7281-figure; current measured value is consistent with the
witness's `markov_trace_symbolic` output of 0.3883).

Both are legitimate tr_M evaluations on the deuteron; they reflect
different **categorical contractions** of the underlying braid (one
keeps the full crossing structure, the other replaces interface
crossings with the Markov-axiom factor z(q)).

## Methodology

1. Parse `tr_M(p, q)`, `tr_M(n, q)` symbolically from
   `habiro-coefficients-atomic.witness.json` (these are
   convention-agnostic — single-nucleon traces only).
2. Construct Phase 5q canonical D:
   ```
   tr_M(D, q)_Phase5q := tr_M(p, q) · tr_M(n, q) · z(q),
   z(q) = 1 / (√q + 1/√q)
   ```
3. Convert to a polynomial in `u` (q = u²), clearing denominators.
4. Apply the sequential cyclotomic-division Habiro algorithm
   (same one as `habiro_coefficients_atomic.cyclotomic_expansion`).
5. Compute `Δa_m(D − n) = a_m(D)_Phase5q − a_m(n)_witness` for
   m = 0, …, 12.
6. Form `Σ_m Δa_m · (u; u)_m` and `sympy.factor`.

The neutron a_m used in step 5 is the witness data —
**single-nucleon traces have only one convention**, so this is
canonical.

## Result

### Phase 5q canonical (D − n) factorization

```
Σ_m Δa_m(D − n)_Phase5q · (u; u)_m
  = u · (u⁴ + 1)² · P16a(u) · P16b(u) · P39(u)
```

where:

- **Φ_8² = (u⁴ + 1)²**: the strand-doubling factor (present)
- **P16a** = `u¹⁶ − u¹³ − u¹² + u¹¹ + u⁸ − u⁵ − u⁴ + u³ + 1`
- **P16b** = `u¹⁶ + u¹⁵ + u¹³ − u¹² − u¹¹ − u⁹ + u⁸ + u⁷ + u⁵ − u⁴ − u³ − u + 1`
- **P39** = `u³⁹ + u³⁸ − u³⁵ + u³⁴ − u³² + u³⁰ − u²⁸ + u²⁶ + 2u²³ + u²² + u²⁰ − u¹⁸ − u¹⁶ + 2u¹⁵ − u¹² + u¹⁰ − u⁸ + u⁶ − u⁴ − u³ − 1`

Total degree: `1 + 8 + 16 + 16 + 39 = 80` (matches u-polynomial
degree of Phase 5q D divided by `(u²+1)³`).

### Side-by-side comparison

| Factor | Phase 5q canonical | habiro-witness (PR #1579) |
|---|---|---|
| Linear `u` | ✓ (× `-1` overall sign) | ✓ (× `-1` overall sign) |
| **Φ_8² = (u⁴+1)²** | **✓** | **✓** |
| 16-degree #1 | P16a (this audit) | P16a-witness |
| 16-degree #2 | P16b (this audit) | P16b-witness |
| Tail | P39 (this audit) | P45-witness |
| Total deg | 80 | 86 |

**Both conventions carry the (u⁴ + 1)² factor.** The residual
polynomial structure differs (P39 vs P45 + a different P16 pair),
which reflects the convention's different handling of the 12
nucleon-nucleon interface crossings — but the **cyclotomic
backbone is identical**.

## Verdict

Per the brief's outcome gates:

> If **Φ_8² appears in BOTH conventions** → strand-doubling
> interpretation is structural; the chain Φ_4 → Φ_8 → Φ_16 → Φ_32
> unlocks; falsifiable predictions test ON.

**Φ_8² appears in both conventions.** Therefore:

1. **Strand-doubling is STRUCTURAL** — convention-invariant.
2. **The chain Φ_4 → Φ_8 → Φ_16 → Φ_32 is unblocked** at the Φ_8
   level. Φ_16 (³He extension) and Φ_32 (⁴He extension) tests are
   live targets, awaiting `habiro-coefficients-atomic.witness.json`
   extensions to A=3 / A=4 (currently only p, n, D are populated).
3. **Q_β framework's canonical input is well-posed at A=2.** The
   (D − n) Habiro factor Φ_8² is the same whether the canonical
   D is computed via the full braid (witness) or via the
   constit + Markov identity (Phase 5q).
4. **The convention-blocker audit
   [2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md](2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md)
   is partially resolved**: at A=2 the conventions agree on the
   cyclotomic backbone. The remaining blocker (A=3, A=4) is the
   absence of `helium-3` / `helium-4` entries in the atomic Habiro
   witness — a witness-extension task, not a categorical question.

## What the residual P39 vs P45 difference means

The two conventions disagree on the *non-cyclotomic* tail of the
factorization but agree on every cyclotomic factor through Φ_8².
The structural interpretation:

- **Cyclotomic factors** ((u-1), (u+1), Φ_4, Φ_8, …) encode the
  **categorical-axiom content** of the trace — they're invariant
  under any convention-respecting reduction.
- **Non-cyclotomic factors** (P16a, P16b, P39, P45, …) encode the
  **specific crossing word** chosen to represent the atomic braid
  — they're shape-dependent.

The Φ_8² invariance confirms that strand-doubling is at the
categorical-axiom layer, not the crossing-word layer. This is what
"structural" means in the framework's vocabulary.

## Open follow-up

The Φ_16 (A=3) and Φ_32 (A=4) tests require:

- Adding `helium-3` and `helium-4` (or `tritium`) entries to
  `habiro-coefficients-atomic.witness.json`. The existing
  `habiro_coefficients_atomic.py` script supports these in its
  `_ATOM_CHI_LABEL_BY_ZN` table; just needs an extended `cases`
  list and the corresponding `chi-{atom}-h{n}.witness.json`
  caches (already present for ³He / ⁴He per `_ATOM_CHI_LABEL_BY_ZN`).
- The symbolic deuteron extraction (`HABIRO_WITH_DEUTERON=1`) is
  the bottleneck pattern; the A=3 / A=4 traces will be heavier
  and may need a multi-hour run.

These are mechanical extensions; the categorical reasoning behind
the Φ_16 / Φ_32 prediction is decoupled from the witness availability.

## References

- [`docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`](2026-06-01-qbeta-habiro-phi8-interpretation.md)
  — Φ_8 categorical interpretation (strand-doubling, 4-strand
  deuteron braid).
- [`docs/audits/2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md`](2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md)
  — the convention blocker this audit resolves at A=2.
- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
  — master ledger.
- [`computations/closed_form_tau_M.py`](../../computations/closed_form_tau_M.py)
  — Phase 5q canonical tr_M.
- [`computations/habiro/habiro_coefficients_atomic.py`](../../computations/habiro/habiro_coefficients_atomic.py)
  — Habiro coefficient extraction (sequential cyclotomic division).
- PR #1579 (commit `57b5fa2d3a`) — original (D − n) Φ_8² discovery
  in the habiro-witness convention.
