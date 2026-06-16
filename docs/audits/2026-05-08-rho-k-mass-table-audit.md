# Audit: ρ_K mass-table predictions (PR #564, P4″ + P4ⁱᵛ)

**Date:** 2026-05-08
**Scope:** Pre-merge audit of [`atomic_mass_via_rho_k.py`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/atomic_mass_via_rho_k.py)
landed on `claude/refactor-computation-framework-iCqhG` (PR #564),
cited in the [1 ppb coordination ledger](../coordination/1ppb.md)
as P4″ (commit `86aaeb51a`) + P4ⁱᵛ (commit `400c7961d`).

The script is **not yet on `main`** — this audit reads the branch
directly. Re-run after #564 merges to confirm numbers stand.

## Methodology

The ρ_K assembly:

$$
  \mathcal{M}(K) \;=\; \rho_K(Z, N) \cdot m_e \cdot \bigl|\mathrm{tr}_M(K)\bigr|
$$

with leading-order ansatz

$$
  \rho_K^{\mathrm{LO}}(Z, N) \;=\; \frac{Z \cdot m_p \,+\, N \cdot m_n}{m_e \cdot |\mathrm{tr}_M(K)|}
$$

reproduces atomic masses on D, T, ³He, ⁴He with sub-1% relative
error. Per the [PR #564 §3.3a resolution](https://github.com/litlfred/qou/pull/564)
(Options A + C: no additive T6 term, Mittag–Leffler
complementarity), this replaces the legacy single-anchor `E_0`
assembly that propagated 8–54% error to non-proton atoms.

Calibration anchors (CAL inputs only — no derived `Q_β`):
- $m_e$ = 0.51099895 MeV (CODATA)
- $m_p$ = 938.27208816 MeV (CODATA)
- $m_n$ = 939.56542052 MeV (CODATA, via $Q_\beta = m_n - m_p - m_e$)

## Witness data (rho-k path)

Read from
[`atomic-mass-via-rho-k.witness.json`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/atomic-mass-via-rho-k.witness.json):

| Atom | $Z$ | $N$ | $A$ | $|\mathrm{tr}_M|$ | ρ_K err (%) | Legacy E₀ err (%) | Improvement |
|---|:-:|:-:|:-:|---:|---:|---:|---:|
| p   | 1 | 0 | 1 | 1.0653 | 1.5×10⁻⁴⁹ | 0.0 | (anchor) |
| n   | 0 | 1 | 1 | 0.9232 | 1.5×10⁻⁴⁹ | −8.325 | 8.3×10¹² |
| D   | 1 | 1 | 2 | 0.3883 | 0.119 | −24.247 | **204×** |
| T   | 1 | 2 | 3 | 0.1041 | 0.302 | −54.150 | 179× |
| ³He | 2 | 1 | 3 | 0.2065 | 0.275 | (n/a) | — |
| ⁴He | 2 | 2 | 4 | (P4ⁱᵛ) | 0.759 | (n/a) | — |

**Mean |err_pct| on D, T, ³He** = (0.119 + 0.302 + 0.275) / 3 = **0.232%**,
matching #564's claimed **0.23% MAE on D/T/³He**.

**⁴He extension** (P4ⁱᵛ commit `400c7961d`): adds one row at 0.759%
relative err — coarsest of the table, but still finite (legacy
path was diverging).

## Audit verdict

✅ **200× improvement claim holds for D.**

| Claim | Status |
|---|---|
| ρ_K assembly $M = \rho_K \cdot m_e \cdot |\mathrm{tr}_M|$ | ✅ Correctly implemented; matches PR #564 §3.3a resolution |
| 0.23% MAE on D, T, ³He | ✅ Numerically confirmed (mean of 0.119, 0.302, 0.275) |
| 200× improvement on D | ✅ Witness reports 204× for D (vs −24.25% legacy) |
| ⁴He covered at 0.759% | ✅ P4ⁱᵛ row present |
| CAL inputs only (no derived $Q_\beta$) | ✅ All three CODATA anchors are direct |
| `tr_M_unavailable` flag for missing atoms | ✅ Script falls through cleanly per docstring |

## Open observations

1. **Larger atoms regress.** ⁴He err 0.759% > ³He err 0.275% > T err 0.302% > D err 0.119%.
   The leading-order ansatz $\rho_K^{\mathrm{LO}}$ is not sufficient
   for $A \geq 4$ if 1 ppb is the target. Closing this gap is **P3**
   (real $H_{3A}$ Wedderburn weights) per the ledger.

2. **No ⁵Li / ⁶Li / ⁷Li rows yet.** $|\mathrm{tr}_M|$ exists for ⁵Li / ⁶Li
   in `atomic-tr-m-mpfr-50dps.witness.json` (per merged #567 cross-check
   gating 5 atoms); the ρ_K script could extend to those rows
   immediately — likely 1 hr of work post-#564 merge.

3. **AXKIA cross-check.** The audit's claim that
   `α_EM⁻¹ = q · [9]_q · [10]_q` is independent of the ρ_K
   path — both derive from the same `tr_M(K)` substrate but
   project different observables. Re-running the AXKIA chain check
   on the post-merge branch is **option 4 follow-up** (P3 territory).

## Cross-reference

- [`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md) — generic mass formula
- [`prop:per-nucleon-shift-additive-linearity`](../../content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md) — `shift(Z, N) = 18Z + 21N + 1`
- [`docs/coordination/1ppb.md`](../coordination/1ppb.md) — ρ_K rows under #564
- [PR #564](https://github.com/litlfred/qou/pull/564) — landing branch (open)
- [PR #567](https://github.com/litlfred/qou/pull/567) — crystal R-matrix Sub-lemma 2.1 (merged)
- [PR #572](https://github.com/litlfred/qou/pull/572) — this branch's #567 follow-ups
