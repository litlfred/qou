# χ-witness crossing-convention label audit (bean b0vf)

**Date:** 2026-06-28
**Branch / PR:** `claude/b0vf-chi-he4-stale-partial-2026-06-28` → #3047
**Bean:** `b0vf` ("chi-helium-4-h12-at-q0-50dps only 17/77 complete — needs producer re-run")

## TL;DR

The bean's framing — *incomplete, needs a re-run* — was **wrong**. The real
defect is a **missing crossing-convention label** on the Hoefsmit/native χ
witness families. The complete ⁴He χ value already exists on `main`
(`chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json`, 77/77); it simply uses a
**different convention** than the partial `chi-helium-4-h12-at-q0-50dps.witness.json`,
so the two are not interchangeable and must each say which convention they are.

## The two conventions

χ^λ(β_atomic(Z,N)) at q₀ is computed two ways in the corpus, and they give
**different character values by design** because each takes the trace of a
*different braid word*:

| Convention | Braid encoding | Producers | Output files |
|---|---|---|---|
| **`sign-only-crossings`** | Geck–Pfeiffer `chi_q_via_gp`: word = `(sign, gen)` pairs, every crossing ±1 | `chi_at_q0_via_matrix_m_mpfr.py`, `chi_4he_via_rust_lossless.py`, `chi_via_rust_lossless.py` (`rust-chi-q-via-gp-lossless`, `matrix-m-chi-q-via-gp`) | `chi-*-at-q0-50dps-matrix-m`, `chi-at-q0-matrix-m-*`, `chi-*-rust-lossless-*` |
| **`averaged-crossings`** | Hoefsmit seminormal, full `atom_braid_word_3A(Z,N)` triples — `d ≠ 0` entries weight crossings by per-color factors | `chi_at_q0_via_hoefsmit_mpfr.py` (q₀), `chi_at_q_inv_via_native_mpfr.py` (q₀⁻¹ bar-image, same word) | plain `chi-*-at-q0-50dps`, `chi-*-at-qinv-50dps` |

**Smoking gun** (from `chi_at_q0_via_matrix_m_mpfr.py`'s own docstring): on the
deuteron the two paths give χ^(6) = **1.56** (sign-only) vs **11.02 = q₀²³**
(averaged) at q₀ ≈ 1.11. Empirically here, the 22 overlapping ⁴He partitions
between the partial Hoefsmit cache and the complete `-matrix-m` cache disagree
on **all 22** — exactly as expected for two distinct conventions, not corruption.

A character/trace is **basis-independent**, so the difference is **not** the
basis name ("Hoefsmit seminormal"); it is the **braid word** (sign-only vs
full averaged crossings).

## The bug class

An unlabeled χ witness can be consumed by a downstream binding / τ_M compute
under the **wrong** convention. Because the two value sets differ by large
factors, the resulting binding number is silently wrong. The `*-matrix-m`
files already declared `"convention": "sign-only-crossings"`; the
Hoefsmit/native families declared nothing.

## Fix delivered

1. **`computations/chi_convention_audit.py`** — a flag tool. A producer-identity
   registry maps each producer → expected convention; each `chi-*.witness.json`
   is classified `ok` / `mismatch` / `unknown-convention` / `missing-inferable`
   / `missing-ambiguous`.
   - `--strict` exits 1 on the hard contradictions (`mismatch`, `unknown`) —
     currently **0** of each.
   - `--fix` stamps the inferable labels into the witnesses (idempotent;
     records `convention_inferred_by` for provenance).
   - Output: `chi-convention-audit.witness.json`.
2. **Stamped 14 witnesses** via `--fix` (4 sign-only, 10 averaged).
3. **Patched the producers** `chi_at_q0_via_hoefsmit_mpfr.py` (both on-disk
   payloads) and `chi_at_q_inv_via_native_mpfr.py` to emit
   `"convention": "averaged-crossings"` natively, so the gap does not recur on
   the next run.

## Current audit state

```
42 scanned · 22 ok · 0 mismatch · 0 unknown · 0 missing-inferable · 20 missing-ambiguous
```

## Follow-up — the 20 `missing-ambiguous`

These carry no producer field the registry recognises and were **not**
auto-stamped (honest flag, not a guess):

- **free-braid variants** (`chi-*-free-h*-at-q0/qinv-50dps`, 6) — the
  disjoint reference braid; convention not yet pinned.
- **symbolic catalogue** (`chi-{atom}-h{n}`, producer
  `delta_lambda_empirical_tabulation.py`, 6) — symbolic Laurent χ; convention
  defined by the catalogue, needs confirmation.
- **misc** `chi-content-eigenbasis`, `chi-content-single-mode`,
  `chi-free-via-lr`, `chi-helium-4-h12-numeric`,
  `chi-lambda-he4-full-partition-table`,
  `chi-lambda-multi-block-first-measurement` (8).

Classifying these is a follow-up; each needs its producer inspected before a
label is stamped.

## Canonical reconciliation — which convention is canonical

Going to the canonical derivation (`docs/canonical-derivation-cheat-sheet.md`
§Phase 5q + the prior `docs/audits/2026-06-09-binding-trace-convention-split.md`)
settles which of the two conventions is canonical. The convention-split audit
already enumerated these exact two values:

| this audit's label | convention-split label | deuteron χ^(6) | status |
|---|---|---|---|
| **`sign-only-crossings`** | **A** (matrix-M / `chi_q_via_gp`; the production χ infra #2062/#2080) | **11.02 = q₀²³** | **canonical per-λ character** |
| **`averaged-crossings`** | **B** (`markov_trace_3A` Plancherel) | **1.56** | **DEPRECATED for binding** |

**`sign-only-crossings` (A) is canonical** for the per-λ character:

- It is the **production** character convention — `marshal_to_chi_lambda_braid`
  maps the averaged p-n form `(c=1, d=−h/2)` → `(sign=+1)` (the explicit
  `# averaged → σ convention` line), so production `chi_lambda_braid` and the
  `derived_chi_catalogue` use sign-only.
- It is **consistent with the canonical Jones–Markov trace C**
  (`markov/markov_trace_canonical.tr_M_element`, `prop:categorical-mass-markov`).

**`averaged-crossings` (B) is deprecated for binding** — `markov_trace_3A`'s
own docstring: *"This is NOT the canonical Jones–Markov trace… Do not use for
new binding calculations."* It survives only as an opt-in audit-trail probe
(`pn_convention="strict_averaged"`). The audit reports these as
**off-canonical** (informational; they are valid probes, not errors, so they
do not fail `--strict`).

**Corpus state (this audit):** of 38 labeled χ caches, **12 are canonical
(sign-only / A)** and **26 are off-canonical (averaged / B)**. A downstream
*binding* consume should use the sign-only sibling; whether any specific
consumer currently misuses an averaged cache is a separate follow-up
(compute-integration-watcher), not asserted here.

## Note on PR #3029 (A=4 reconciliation, merged same day) — CORRECTED

The A=4 `f^λ` binding in #3029 used the **`sign-only-crossings`** `-matrix-m`
χ — which the reconciliation above shows is the **canonical (A)** per-λ
convention, *not* an off-convention choice. (An earlier draft of this note had
the canonicity backwards, calling the averaged form the binding-canonical one;
the convention-split audit corrects that — averaged (B) is the deprecated form.)
So #3029 used the right convention. Its verdict (A=4 does not close, −80%)
stands and is convention-robust.
