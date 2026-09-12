---
# qou-oiz3
title: excise float64 from the UIC resolvent cone (mu_lambda, s_*) -- owner directive 2026-09-12
status: in-progress
type: task
priority: normal
created_at: 2026-09-12T20:47:33Z
updated_at: 2026-09-12T21:52:06Z
---

## Measured surface and the residual (2026-09-12)

Owner directive, verbatim: **excise float64**. Follows PR #7237 / bean `qou-t6be`.

**The surface was NINE sites, not the two #7237 cited** — plus a tenth that is
not a line at all. `origin/main` line numbers:

| site | main | was |
|---|---|---|
| `q_laplacian_eigenvalue` | :292 | `casimir_sum = 0.0` over the float64 `q_int` |
| `S_REEB_PLANCK` | :520 | `(q0 - 1.0) / q0` |
| `q_resolvent_weight` | :325 | `1.0 / (mu + s)`, float64 default s |
| `_partition_table` | :544 | `_resolvent = 1.0 / (_mu + S_REEB_PLANCK)` |
| `_partition_table` | :539 | `math.log` on an mpf |
| `partition_spectral_log_rate` | :508 | `math.log(ratio)` |
| `partition_character_sigma1` | :491 | exact SYT counts x float64 q0/qi/h |
| `conjugate_pair_cross_term` / `_jet` | :2517,:2527,:2641 | `float(h)`, `math.sqrt` on an mpf MeV scale |
| `atom_markov_trace` / `atom_frobenius_norm_sq` | :2781,:2830 | `math.exp` on an mpf log-norm (the `binding_from_frobenius_pairing` leg) |

**Tenth:** `_partition_table` is a CACHE built at whatever ambient `mp.dps` its
first toucher was at — 70 under `unified_iterative_correction`'s own `workdps`,
**15** under any other consumer, no signal either way. Now wrapped.

**Numbers** (mp.dps 70, proton pin, k_exact 4, baseline from
`git show origin/main:...` loaded by path, totals read as mpf out of
`per_step[-1]` rather than through the public `float()` return):

- worst per-atom gated move **8.44176e-16** at Z=4 N=4; worst absolute
  **2.54345e-17 MeV** (at Z=2 N=1).
- worst ungated move **6.65778e-15**, also Z=4 N=4.
- float64 eps is 2.22045e-16, so **the totals DO exceed the floor** — 3.8x
  gated, 30x ungated. Mechanism is **cancellation**, not error growth: ⁸Be's
  ungated total is 1.3e-3 MeV out of O(1) contributions and its absolute shift
  is 1.04e-17 MeV like everything else. So #7237's per-block bound is right
  per block and does not transfer to a total.
- at k_exact 6 nothing exceeds 3e-16.

**OPEN, and it is larger than what was fixed.** `q_hook_product`,
`q_factorial` and `wedderburn_weight` return `mpf` and accumulate
`mp.mpf(1) * q_int(k)` over the **float64** `q_int` — mpf-typed,
float64-VALUED. Measured over the 31 weighted blocks: this excision removes at
most **2.4946976e-16** and leaves **1.0212424e-15** at lambda = (2,2), i.e. 4x
more than it removed. Root fix is `q_int` itself: **124 python files, 243
witnesses**. That is a corpus-wide sweep AGENTS.md excludes from the precision
exemption, so it is put to the owner rather than run.

**Second, smaller residual:** `_Q_MP` is built from `Q_50_DIGIT_STR` and sits
9.9102461e-52 from `q_at(90)` — ~50 digits, BELOW `OUTPUT_DPS = 60`.

PR #7245; audit `docs/audits/2026-09-12-uic-float64-excision.md`.
