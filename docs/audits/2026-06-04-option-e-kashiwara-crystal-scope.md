# Option E (Kashiwara crystal) for Δ_λ closure — formalize-first scope

**Date:** 2026-06-04
**Trigger:** [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md) listed seven ansätze for the Δ_λ binding-energy closure. Six were tested and **all failed**:

| Option | Ansatz | Verdict |
|---|---|---|
| A | Occam single-support | underdetermined; arbitrary |
| B | Frobenius co-Casimir `1/dim_q(λ)` | residual −2.30 MeV (wrong sign) |
| C | Demazure-fibre `y_λ·D_w/D_w₀` | tautological (reproduces M_LO) |
| D-Plancherel | LP shadow price minimising `Σ\|Δ_λ\|·w_λ` | shifts underdetermination to cost |
| D-Frobenius | LP alt cost | same problem (different singleton) |
| F | Wenzl-bridge augmented Markov | closure-pickle bug on first attempt |
| **E** | **Kashiwara crystal at q→1** | **TBD** ← this PR |

AGENTS.md is explicit: **"Do not propose a seventh fit-based ansatz"**. The Δ_λ-gate cap is hard. This PR therefore tests Option E as a **parameter-free, multi-candidate structural test** — natural crystal-graph invariants for `λ ⊢ 6` (deuteron, A=2, n=6, 11 partitions) plugged into the existing `Σ_λ y_λ(q₀)·χ^λ(β_D)·Δ_λ` machinery, no LP, no fitted scalar. If a candidate matches the empirical target `-4.353` to better than 5 % with zero free parameters, it's a finding. If all candidates refute, the simple crystal-statistic family is closed and only research-grade categorical paths (GAP-A-3, GAP-A-4) remain.

---

## §1. The target

For the deuteron (Z=1, N=1, A=2, n=6) the audit-doc equation
`B(D) = m_e · Σ_{λ⊢6} y_λ(q₀)·χ^λ(β_D)·Δ_λ` together with the empirical
B(D) ≈ 2.225 MeV gives

  `Σ_{λ⊢6} y_λ(q₀)·χ^λ(β_D)·Δ_λ = -B_D / m_e = -4.353`     (target, m_e units)

`y_λ(q₀)` is cached at 50 dps (`y-lambda-at-q0.witness.json`, n=2..12).
`χ^λ(β_D, q₀)` is cached at 50 dps (`chi-deuteron-h6-at-q0-50dps.witness.json`).
The only thing the audit-doc table did **not** close is `Δ_λ(D)`.

A parameter-free ansatz `Δ_λ = c(λ)` for some specific function `c` of the
partition `λ` gives `c(λ)` for every `λ ⊢ 6` deterministically, so the
left-hand side is a single number — comparable to the target with no free
scalar.

## §2. Five no-fit crystal-statistic candidates

The Kashiwara crystal `B(λ)` of the irrep V_λ at q→1 has a small number of
canonical numerical invariants that depend on `λ` alone (no atom data, no
free parameter). The cheapest **formalize-first** test is to evaluate each
of these as the closed-form `Δ_λ` and check the deuteron sum.

| Candidate | Δ_λ formula | Crystal interpretation |
|---|---|---|
| **E1** Macdonald `n(λ)` | `n(λ) = Σ_{x∈λ} (row(x) − 1) = Σ_i (i−1)·λ_i` | the standard Macdonald row-index statistic (NOT the cell-content `col(x)−row(x)`; the two coincide only on column-strict shapes) — canonical bias toward column shapes |
| **E2** conjugate `n(λ')` | `n(λ') = Σ_{x∈λ} (col(x) − 1) = Σ_i C(λ_i, 2)` | Macdonald statistic of the conjugate partition; canonical bias toward row shapes (`n(λ) + n(λ') = C(\|λ\|, 2)`) |
| **E3** dim ratio at q₀ | `f^λ / dim_q(V_λ)\|_{q₀}` | the **classical-to-q dimension ratio at q₀** (NOT a q→1 limit, which would be 1) — measures how far the q-deformation at the substrate anchor deviates from the classical irrep dimension |
| **E4** constant-zero control | `Δ_λ ≡ 0` for every `λ` | sanity control on the summation pipeline (charge is **not** in general 0 on column-strict tableaux — that mis-statement was caught in Copilot review; the control is a pure constant-zero, with the witness assertion `\|S\| < 1e-40` confirming no arithmetic bug) |
| **E5** crystal cardinality `\|B(λ)\| = f^λ` | `f^λ = n! / Π hook(x)` | the ordinary irrep dimension; sometimes proposed as the "natural categorical weight" but already structurally identical to several earlier ansätze |

Each `c(λ)` is **fixed** (no fitting, no free scalar). The probe computes
`S = Σ_{λ⊢6} y_λ(q₀)·χ^λ(β_D)·c(λ)` for each candidate and reports
`(S, target, rel_err)`.

## §3. Pre-formalize-first observations (sanity)

- **E4 is trivial by construction.** `Δ_λ ≡ 0` is a pure constant-zero
  control: the sum is identically 0 (≠ −4.353). The witness assertion
  `\|S_E4\| < 1e-40` confirms no arithmetic bug in the summation
  pipeline — if E4's `S` is non-zero, every other candidate's verdict
  is suspect.  (Earlier draft mis-described E4 as "charge of standard
  column-strict tableaux on λ is always 0" — that's not true in
  general; corrected per Copilot review.)
- **E5 = f^λ.** With y_λ derived from Wenzl/Jones-Markov such that
  `Σ_λ y_λ(q) · dim_q(V_λ) = 1` (the normalized-trace identity), the
  classical-limit `q→1` analog `Σ_λ y_λ(1) · f^λ = 1` likely holds; testing it
  gives `S ≈ 1 ≠ -4.353`. Sanity-only.
- **The non-trivial candidates are E1, E2, E3.** Formalize-first
  expectation: E1 and E2 are simple linear-in-content statistics, both
  candidates with a clean categorical interpretation; E3 is the q-deformation
  obstruction measure.

If E1, E2, E3 all fall outside `\|rel_err\| < 0.05`, the no-fit crystal-
statistic family is **closed** for deuteron. Per Δ_λ-gate discipline, the
remaining productive directions are GAP-A-3 (categorical brane-tower level
selection) and GAP-A-4 (ρ general rule), both research-grade.

## §4. Probe plan (`option_e_kashiwara_crystal_delta_lambda_probe.py`)

Pure `sympy`+`mpmath`; reads existing 50-dps witnesses; no Hecke
construction. Algorithm:

1. Load `y_λ(q₀)` for `n=6` from `y-lambda-at-q0.witness.json` (11 values).
2. Load `χ^λ(β_D, q₀)` per partition from
   `chi-deuteron-h6-at-q0-50dps.witness.json` (11 values).
3. For each of E1..E5, compute `c(λ)` exactly:
   - E1: `n(λ) = Σ_i (i−1)·λ_i` (1-indexed rows)
   - E2: `n(λ') = sum of co-contents` (equivalently `Σ_i C(λ_i, 2)` for the conjugate)
   - E3: `f^λ` from hook-length formula, divided by `dim_q(V_λ)\|_{q₀}` (closed form, 50 dps)
   - E4: `0` (control)
   - E5: `f^λ` (hook-length formula)
4. For each: `S = Σ_λ y_λ · χ^λ · c(λ)`, `target = -4.353` (use the
   audit-doc convention `target_signed = -B_D / m_e`).
5. Verdict per candidate: `EXACT-MATCH` if `\|rel_err\| < 1e-12`,
   `NEAR-MATCH (< 5%)` if `\|rel_err\| < 0.05`, else `REFUTED`.
6. Emit `option-e-kashiwara-crystal-delta-lambda-probe.witness.json` with
   `discipline: "EXPLORATORY"`, `production_wired: false`.

## §5. Honest expected outcome

Per AGENTS.md's "Δ_λ-gate" framing and the six prior failures, **the
formalize-first expectation is**: all five candidates REFUTED, advancing
the analysis by closing the no-fit crystal-statistic family. This is a
clean negative result, not a fit. If any candidate matches, the Δ_λ gate
opens for deuteron — a major finding that would warrant immediate Lean
formalization of the categorical derivation behind the matching statistic.

## §6. Discipline

- **EXPLORATORY**, no production code, content blocks, or production
  witnesses touched.
- **Not a 7th fit ansatz** — every candidate is parameter-free
  (`Δ_λ = c(λ)` with `c` fixed in closed form before the probe runs).
- **Formalize-first** (PR #1826) — multi-candidate structural test, not a
  wide scan.
- The Δ_λ-gate discipline review will catch any 7th fit; this PR is
  designed to pass that review.

## §7. Sibling coordination

- Builds directly on the gate doc
  [`2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md)
  (Option E listed as TBD).
- Companion to the just-merged [`#1853` consolidated audit](./2026-06-04-h3-h4-jump-both-axes-refuted.md)
  which closed Options B + E for the H₃→H₄ jump (separate axis); this PR
  attacks the orthogonal Δ_λ binding-energy question.
- Per the [Δ_λ phase-4 audit](./2026-05-19-delta-lambda-phase4-z4N-closure.md),
  the productive long-term direction (if Option E refutes here) is
  GAP-A-3 / GAP-A-4 — categorical brane-tower level selection — which is
  research-grade and beyond this PR's scope.
