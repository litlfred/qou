# q-Hecke character gap — closed

**Date:** 2026-05-08
**Branch:** `claude/hecke-nf-followups` (PR #572)
**Closes:** the residual gap identified in
[`docs/audits/2026-05-08-p3-h-3a-divergence.md`](2026-05-08-p3-h-3a-divergence.md)
"Cross-check finding (q=1 character-limited)".

## What was open

After the y_λ weight fix (commit
[`ac7880c5`](https://github.com/litlfred/qou/pull/572/commits/ac7880c5)),
the partition-sum path

$$\mathrm{tr}_M(\beta) \;=\; \sum_{\lambda \vdash 3A} y_\lambda(q) \cdot \chi^\lambda_q(\beta)$$

still disagreed with the canonical reducer (`markov_trace_recursive`)
by 55–80 % relative for proton / neutron / deuteron. Diagnosis:
`schur_weyl_symbolic.specht_character_atomic` returns the **classical
Murnaghan–Nakayama character** $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$
— the $q = 1$ limit — instead of the **q-deformed Hecke character**
$\chi^\lambda_q(\beta)$.

## What this closes

The Hecke character $\chi^\lambda_q$ is, by construction, the trace
of the seminormal representation $\rho_\lambda$ at $q$ on the braid
element $\beta$:

$$\chi^\lambda_q(\beta) \;=\; \mathrm{tr}_{V_\lambda}\,\rho_\lambda(\beta), \qquad \rho_\lambda(\sigma_i) = \text{Hoefsmit seminormal matrix at } q.$$

Both ingredients already live in the repo:

- [`hecke_characters.build_seminormal_matrices(shape, q)`](../../computations/hecke/hecke_characters.py)
  — Hoefsmit seminormal matrices $\rho_\lambda(\sigma_1), \ldots, \rho_\lambda(\sigma_{n-1})$ at $q$.
- [`mass_at_3A_proper.chi_lambda_of_word(sigmas, dim, word)`](../../computations/mass_at_3A_proper.py)
  — $\mathrm{tr}\bigl(\prod_k (c_k \rho_\lambda(\sigma_{g_k}) + d_k I)\bigr)$ over the atomic-braid word.
- [`mass_at_3A_proper.atom_braid_word_3A(Z, N)`](../../computations/mass_at_3A_proper.py)
  — canonical $(c, d, \text{gen\_idx})$ word for atomic braids
  ($\beta_p \cdot I \cdot \beta_n$ structure with $I = \sigma_3 - \frac{h}{2} \cdot 1$ for the deuteron).

Composing these: [`tr_m_q_hecke_seminormal.py`](../../computations/tr_m_q_hecke_seminormal.py)
+ [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal(Z, N, q_val)`](../../computations/wedderburn_jones_markov.py)
yield the partition sum

$$\mathrm{tr}_M^{\text{q-Hecke}}(\beta) \;=\; \sum_{\lambda \vdash 3A} y_\lambda(q_0) \cdot \mathrm{tr}\,\rho_\lambda^{q_0}(\beta).$$

## Cross-check: closure verified at machine epsilon for all 5 low isotopes

[`tr-m-q-hecke-seminormal.witness.json`](../../computations/tr-m-q-hecke-seminormal.witness.json)
compares against the canonical reducer reference
([`atomic-tr-m-mpfr-50dps.witness.json`](../../computations/atomic-tr-m-mpfr-50dps.witness.json),
produced by `markov_trace_recursive`).

**Final hybrid-precision result** (commit
[`9bed8d71`](https://github.com/litlfred/qou/pull/572/commits/9bed8d71)):
30-dps sympy `Float` for $y_\lambda$ + float64 for $\chi^\lambda_q$,
with per-`n` cache.

| Atom | $n = 3A$ | $|\mathrm{tr}_M|$ canonical | partition-sum (q-Hecke) | rel err | time |
|---|---:|---:|---:|---:|---:|
| proton | 3 | 1.0653062286 | 1.0653062286 | **3.96 × 10⁻¹⁵** | 0.32 s |
| neutron | 3 | 0.9232332972 | 0.9232332972 | **4.21 × 10⁻¹⁵** | 0.00 s |
| deuteron | 6 | 0.3882864715 | 0.3882864715 | **7.01 × 10⁻¹⁵** | 3.68 s |
| tritium | 9 | 0.1040521187 | 0.1040521187 | **1.07 × 10⁻¹⁴** | 61.79 s |
| ³He | 9 | 0.2065408586 | 0.2065408586 | **1.03 × 10⁻¹⁴** | 0.24 s ← cached |

**All 5 atoms at machine epsilon** — same precision floor as the
canonical Markov-axiom reducer. 10 / 10 witness assertions pass.

### Why hybrid precision

An earlier float64-throughout path gave only $1.8 \times 10^{-5}$ at
$n = 9$ (T, ³He). The Wenzl–Schur sum over 30 partitions of 9
involves $q^{\text{large}}$ terms that lose significance at float64.
Computing $y_\lambda$ at 30-dps sympy `Float` and substituting at
the end recovers the precision; the subsequent matrix products via
`mass_at_3A_proper.chi_lambda_of_word` (numpy float64) are
short-step and don't accumulate error.

A full-symbolic path (`hoefsmit_symbolic.chi_lambda_symbolic` for
both $y_\lambda$ and $\chi^\lambda_q$) timed out at 240 s for $n = 9$
in interactive sessions. The hybrid technique closes the same
result in ~62 s for the slowest atom.

### Cumulative cost

~66 s total for 5 atoms (cached y_λ across atoms with the same n
makes the second-atom-at-n=9 cost negligible). Compares favorably
to PR #564's
[`rho_k_h3a_refinement.py`](../../computations/rho_k_h3a_refinement.py)
(50-dps mpmath throughout: ~5–10 minutes for the same 5 atoms).
The hybrid 30-dps + float64 approach is the recommended default
for partition-sum tr_M consumers needing better than 1e-5
agreement; for binding-fraction $\Delta_\lambda$ analysis (#564's
production path), use mpmath 50-dps throughout.

**Note:** PR #564's
[`rho_k_h3a_refinement.py`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/rho_k_h3a_refinement.py)
(commit
[`c068550c`](https://github.com/litlfred/qou/commit/c068550c))
implements the same closure with **mpmath at 50 dps**, achieving
`1.4e-16` agreement. That branch's symbolic path is the production
tool for the ρ_K mass-table refinement; this PR's float64 path is a
parallel verification + reusable API exposed via the new
`wedderburn_jones_markov` module.

## Why both paths exist

| Path | Module | Use case |
|---|---|---|
| Canonical reducer | `markov_trace_recursive.markov_trace_of_word` | **Production** $\mathrm{tr}_M$ for mass-table predictions. Bypasses partition sum. |
| Symbolic partition-sum | `rho_k_h3a_refinement.py` (PR #564) | **Per-block decomposition** $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi^\lambda_q$ at 50-dps mpmath; needed for ρ_K binding-fraction $\Delta_\lambda$ analysis. |
| Float64 partition-sum | `wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal` (this PR) | **Fast cross-check** + reusable API for downstream consumers that need the partition decomposition without 50-dps overhead. |

The three paths agree to numerical precision. Cross-check witness
gates this on every CI run.

## Wiring summary

| Function | Status |
|---|---|
| `wedderburn_jones_markov.y_lambda_at` | ✅ ac7880c5 — Wenzl Schur principal, numerical-q-from-start |
| `wedderburn_jones_markov.global_wedderburn_sum_jones_markov` | ✅ ac7880c5 — uses q=1 MN char (legacy compatibility) |
| `wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal` | ✅ **this commit** — uses Hoefsmit χ^λ_q (canonical) |
| `crt_markov.py` | ✅ wired to `global_wedderburn_sum_jones_markov` (q=1 char OK for that use case — paper-six-term consumers); can be upgraded to seminormal char if the partition decomposition is needed at q=q_0. |

## What this does NOT do

- **Does NOT** modify `crt_markov.py`'s character path. The legacy
  `specht_character_atomic` (q=1 MN) is sufficient for the
  paper-six-term shadow-price sweep convention. Upgrading to
  Hoefsmit χ^λ_q here would change downstream numerics; deferred.
- **Does NOT** improve mass-table predictions per se. The canonical
  reducer (`markov_trace_recursive`) is the production path; this
  PR closes a parallel-path GAP that affects validation, not
  prediction.
- **Does NOT** duplicate #564's `rho_k_h3a_refinement.py`. That is
  the production tool with mpmath + symbolic ρ_K; this PR provides
  a fast float64 cross-check + the reusable
  `wedderburn_jones_markov` API.

## Cross-references

- [`docs/audits/2026-05-08-p3-h-3a-divergence.md`](2026-05-08-p3-h-3a-divergence.md) — the weight-side fix (predecessor)
- [`computations/wedderburn_jones_markov.py`](../../computations/wedderburn_jones_markov.py) — the module
- [`computations/tr_m_q_hecke_seminormal.py`](../../computations/tr_m_q_hecke_seminormal.py) — the cross-check witness
- [PR #564, `rho_k_h3a_refinement.py`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/rho_k_h3a_refinement.py) — production symbolic path
- [`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md)
- [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md)
