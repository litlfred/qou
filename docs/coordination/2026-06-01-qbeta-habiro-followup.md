# Q_β Habiro follow-up — coordination ledger

**Branch:** `claude/qbeta-habiro-followup-2026-06-01`
**PR:** [#1618](https://github.com/litlfred/qou/pull/1618)
**Goal:** Three follow-up tracks on the Q_β Habiro keystone, after PR #1579 merged the structural findings (cyclotomic strand-doubling Lean lemma, Δa_m factorization with `−u^15·(u−1)(u+1)·P_8`, a_8 partition-function match, Φ_8² categorical interpretation).

## Tracks

1. **Convention-resolution gate** (highest-impact) — Phase 5q re-factorization on (D−n); does Φ_8² survive in the canonical convention?
2. **Lean-formalize a_8 partition identity** (concrete) — `a_8 = Σ p(n)·u^(5−n)` via Mathlib's `Nat.partition`.
3. **Generate canonical Phase 5q ³He/⁴He Habiro coefficients** — unlocks strand-doubling Φ_16/Φ_32 falsifiable predictions test.

## Context from PR #1579

Recent merge (commit `57b5fa2d3a`) consolidated 22 commits with the structural picture:

- Single-nucleon: Φ_4(u) = u²+1 (in p, n denominators)
- Isospin doublet (n−p): Φ_1·Φ_2 = u²−1 (classical-limit kill)
- A=1→A=2 atomic step (D−n): Φ_8² = (u^4+1)² (in Habiro-witness convention — strand-doubling Φ_8(u) = Φ_4(u²))
- Top-shared shell (a_8): partition function p(1..5) = (1, 2, 3, 5, 7)
- a_7 Padé denominator: irreducible cubic, no clean categorical match
- u^15 depth: braid-pair first-disagreement fingerprint

## Convention caveat

The Φ_8² finding lives in the Habiro-witness convention (`include_inter=True`, tr_M(D) = 0.3883 at q₀). Phase 5q canonical gives tr_M(D) = 0.7281. Whether the cyclotomic prefactor pattern survives the convention switch is the gating test for Track 1.

## Master ledger cross-link

- 1ppQ Q_β master: [`docs/coordination/1ppq-qbeta.md`](1ppq-qbeta.md)
- PR #1579 (merged 2026-06-01): commit [`57b5fa2d3a`](https://github.com/litlfred/qou/commit/57b5fa2d3a) HEAD

## Tracks 1 + 3 follow-up: Φ_8² mechanism investigation (2026-06-01)

After Tracks 1 + 3 jointly established that Φ_8² is convention-invariant and
universal across atomic-step pairs (NOT strand-doubling), a follow-up probe
tested the conjecture that Φ_8² arises from the `z(q)²` interface factor.

**Probe:** [`computations/probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py`](../../computations/probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py)
**Audit:** [`docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md`](../audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md)

**Verdict: FROM-POCHHAMMER-BOUNDARY (not z(q)²).**

- `z(q)^k` alone Habiro-expands to a pure monomial `u^k` (NO cyclotomic
  factor). The Φ_4(u)^k denominator is cleared by `to_u_polynomial` into
  the normalisation prefactor.
- The Pochhammer boundaries are `(u;u)_8` (first Φ_8) and `(u;u)_16`
  (first Φ_8²).
- The ACTUAL Δa_m prefix sums acquire Φ_8 at M=7 (before the m=8 Pochhammer
  enters) and Φ_8² at M=12 (D−n) or M=15 (helium pairs). The pre-m=8 Φ_8
  appearance is a **structural Δa_m interference signature**, not mechanical
  boundary behaviour.
- The proposed "z(q)² → Φ_8²" mechanism in the FALSIFIED audit §Possible
  re-interpretations option (2) is **WRONG** (there is no u → u² substitution
  in the pipeline; z(q) = u/(u²+1) directly in u). The audit needs revision
  to reflect this finding.

The categorical content of the universal Φ_8² Δa_m signature remains
**open** — neither z(q)^k nor the m=8 Pochhammer boundary alone explains
its appearance at M=7. Probable next directions: study the Δa_m algebraic
configuration directly for a categorical witness of `ζ_8 = e^{iπ/4}`.

---

## 2026-06-27 — binding-side cyclotomic tower (lever-1 / z2bn, PR #2899)

A second, independent cyclotomic signature on the **binding** side (not Q_β),
worth cross-linking here because both live in the Habiro / cyclotomic-completion
ring.

Probe `computations/substrate/lever1_qinvolution_kernel_test.py` q-deforms the
proved identity `Σ_λ f^λ = #involutions`. The binding selection-rule period
`lw(c) = S(c+1)/(c+1)` with `S(m) = Σ_{λ⊢m} dim_q(λ)` satisfies the q-involution
recurrence `S(m) = S(m−1) + [m−1]_q·S(m−2)` exactly at the seed `m=2,3`
(q=1 → involution numbers). The correction
`D(m) = S(m) − (S(m−1)+[m−1]_q·S(m−2))` carries a **universal `(q−1)²`** prefactor
(deviation `O(h²)`, pure fibre effect) and a **cyclotomic factor tower**:
`D₄∋Φ₃`, `D₆∋Φ₅`, `D₇∋Φ₃²Φ₅`, `D₈∋Φ₃Φ₅Φ₇`.

**Resonance + distinction with the Q_β Δa_m Φ₈ signature above.** Both sides
exhibit cyclotomic structure in their Habiro expansion. But the *cyclotomics
differ*: the Q_β Δa_m side sees `Φ₈` (ζ₈ = e^{iπ/4}, a ζ-fibre/complex
phenomenon); the binding `D(m)` tower is `Φ₃/Φ₅/Φ₇` over **real-q `ℤ[q]`**.
Per #2452 + the AGENTS.md *Im(q) at fibre vs observable level* banner, these are
the **same ring class, distinct localisations** — the binding kernel is real-q
integral, the Q_β c_k Habiro element is ζ-localised. So this is corroboration at
the *ring-class* level, **not** a claim that the two cyclotomic towers are the
same element. Independent corroboration of the period's identity also landed on
the q-Bessel side (#2325 / #2822: `lw` = q-deformed involution / Rogers–Szegő
moment).

Audit: `docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md`.
Open next: fit `D(m)` to a single Habiro element (real-q), verify held-out `m`;
separately, test whether #2409's full-Hecke trace Ohtsuki coefficients match
`Σ_λ dim_q(λ)` (the rung-linking cross-check).
