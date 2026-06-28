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

## Note on PR #3029 (A=4 reconciliation, merged same day)

The A=4 `f^λ` binding in #3029 used the **`sign-only-crossings`** `-matrix-m`
χ. The Option-E binding-trace convention is the **averaged** one ("NOT the
averaged-crossing binding trace" is how the sign-only producer distinguishes
itself). This does **not** change #3029's qualitative verdict — A=4 lands at
−80% under sign-only and the averaged convention is no closer to closing 28.30
MeV — but the convention used should be stated explicitly when that number is
cited. Tracked here rather than reopening the merged PR.
