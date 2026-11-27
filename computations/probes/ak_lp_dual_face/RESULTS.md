# Results: the a_K LP dual is not identified on the c_λ = 0 rows

Beans `qou-ssf9`, `qou-fu8c`. Predictions in `PREREGISTRATION.md` (committed
first, `076ab8fb4ff`). Probe: `ak_lp_dual_face_probe.py`; witness:
`computations/ak-lp-dual-face.witness.json` (`q0Anchor: proton`). Exact
rational arithmetic throughout (own two-phase simplex, Bland's rule, on
`fractions.Fraction`); no float64.

## Claim

On every row where the LP's cost `c_λ = y_λ·χ^λ` is exactly zero, the dual
variable `u_λ` (published as `u_lambda_star`) **ranges over [0, +∞)** on the
optimal dual face. It is not determined by the LP at all. Every other dual
coordinate is identified: `u_λ = 1` exactly on `c_λ ≠ 0` rows, `y0 = 0`,
`w = 0`, and primal optimum = dual optimum = 0 exactly.

So the 2026-11-24 move of `u_λ*` by exactly ×10⁻⁴ on those rows (#9395) is a
solver choosing a different point of an unbounded face. Neither the old nor the
new value is a property of the LP. The hypothesis holds on proton, neutron,
deuteron, tritium and helium-3. **Helium-4 is the exception**: its cache has
`1e-73`–`1e-149` residue instead of exact zeros, so the exact LP identifies
every coordinate there, and the published helium-4 duals are outside that
identified face (below).

## Why, in one line

`G = diag(|c|)`, so a zero `c_j` makes `u_j`'s coefficient zero in every dual
constraint and in the dual objective. `u_j` then appears nowhere except its own
bound `u_j ≥ 0`. The column-`j` constraint reduces to `y0 + w_j = 0`, which
with `w_j ≥ 0` and the `−M Σ w` objective forces `y0 = 0`, `w = 0`.

## Measured, per atom (exact)

| atom | partitions | rows with c = 0 | u on c ≠ 0 rows | u on c = 0 rows | y0 | primal* = dual* |
|---|---|---|---|---|---|---|
| proton | 3 | 1 (`[1,1,1]`) | 1, identified | [0, +∞) | 0 | 0 |
| neutron | 3 | 1 (`[1,1,1]`) | 1, identified | [0, +∞) | 0 | 0 |
| deuteron | 11 | 7 | 1, identified | [0, +∞) | 0 | 0 |
| tritium | 30 | 25 | 1, identified | [0, +∞) | 0 | 0 |
| helium-3 | 30 | 25 | 1, identified | [0, +∞) | 0 | 0 |
| helium-4 (cache as is) | 77 | **0** | identified, `1 − y0/|c_λ|` (see below) | — | `1.45018846915730…e-149`, identified | `1.62963735132993…e-151` |
| helium-4, `ℓ ≥ 3` set to exact 0 (arm) | 77 | 70 | 1, identified | [0, +∞) | 0 | 0 |

The set of `c = 0` rows equals the set of `y_λ = 0` rows exactly on all six
atoms (P0), and every one has `ℓ(λ) ≥ 3`.

Published values check against the face: on `c ≠ 0` rows both the old and new
witness carry `0.99999999999999999…`, i.e. 1 to solver precision; on `c = 0`
rows the old values (5931.63, 4091.19, 536.98, 92.54, 177.86 per atom) and the
new ones (0.593163, 0.409119, 0.0536978, 0.00925357, 0.0177864) are all ≥ 0, so
both lie in the face (P6). Within an atom the solver returns the same value on
every `c = 0` row, which is what a symmetric interior-point centre does on a
face that is symmetric in those coordinates.

## What else is therefore not identified

These published fields inherit the non-identification:

- **`active_set` / `is_active` / `n_active`.** A row is active when
  `u > dual_tol`; on a `c = 0` row that is a property of the solver's point. All
  `c = 0` rows are currently marked active.
- **`chirality_dual_sum` and `self_conjugate_dual_sum`.** Both sum `u` over
  active rows, and every atom except helium-4 has a non-self-conjugate
  partition in its zero set, so `chirality_dual_sum` is unidentified on five
  atoms (it went 5932.63 → 1.593163 on the proton). `self_conjugate_dual_sum`
  is unidentified on deuteron, tritium, helium-3 (their zero sets contain a
  self-conjugate shape) and identified, = 1, on proton and neutron.
- **`x_star` on `c = 0` rows when there are two or more of them.** The primal is
  degenerate too: mass may sit on any zero-cost column, so on deuteron,
  tritium and helium-3 each such `x_λ` ranges over `[−M, n + M(k−1)]`
  (`M = 10^6`, `k` = number of zero rows). On proton and neutron (`k = 1`) it is
  identified, `x = n = tr_M`. `x = 0` is identified on every `c ≠ 0` row.

`a_K_via_lp_dual` is `null` before and after, and its consumers
(`mass-coefficient-shadow-price.ts` prose, the two `o3prime_*` probes) read
`y0_star` and the degeneracy flag only, both identified. So nothing a reader of
the paper sees moved.

## Helium-4: the exception, and why it did not move

The helium-4 chi cache does **not** carry exact zeros on its `ℓ(λ) ≥ 3` rows.
It carries residues of order `1e-73` (e.g. `y_λ = 1.034e-73`, contribution
`−1.580e-73`), where the tritium and helium-3 caches carry `0.0`. Under
convention D those weights vanish identically (`qou-u2jg`, Lean), so these are
numerical residue, not values. With every cost nonzero the LP is
non-degenerate in this sense, and the exact solve gives:

- `y0 = min_λ |c_λ| = 1.45018846915730442068611261478…e-149`, attained at
  `λ = [2,2,2,2,1,1,1,1]`; primal = dual = `n·y0 = 1.62963735132993754…e-151`.
  (Exact rationals in the witness; the denominators run to ~250 digits.)
- every `u_λ` is identified, `u_λ = 1 − y0/|c_λ|`: `0` at the argmin, within
  `1e-15` of 1 on 60 rows, further from 1 on 17.

The published helium-4 values do **not** lie in that face: the witness carries
`u = 6.32886147866252470833…` on all 70 `ℓ ≥ 3` rows, before and after the
refresh. That is what one expects if Clarabel, at 50 digits, sees costs of
`1e-73` to `1e-149` as zero and solves the degenerate LP; it is not the exact
answer to the LP it was handed. The sensitivity arm, which replaces those
residues by the exact zero convention D fixes, puts helium-4 in the same
structure as the other five (row 2 of the table above), and every prediction
holds there.

So the pre-registered predictions P2, P3 and P6 **fail on helium-4 as the
cache stands**, and hold on the other five atoms and on the helium-4 exact-zero
arm. The failure is caused by the input, not by the structure of the LP.

Helium-4 is also the one atom whose row did not move in the refresh
(`chirality_dual_sum` `431.0337…` before and after, `u = 6.3288…` before and
after). That is **not explained** by the face structure alone: to the solver
its `ℓ ≥ 3` columns are as degenerate as the other atoms' exact zeros. One
reading consistent with the data is that the forked Clarabel treats an exact
zero cost differently from a tiny nonzero one, so only atoms with exact zeros
moved; it is not established here. The attribution of the ×10⁻⁴ to
`0b5b85fbaf6` stays "likely", as in the #9395 trace.

The cache residue is a separate data-hygiene item for the chi-cache producer
(`chi_at_q0_via_hoefsmit_mpfr.py`, which computed helium-4 at 50 dps and the
others at 80). It is not fixed here.

## Scope

Scope (a): a statement about this LP as posed by `aK_via_lp_dual_full.py` on
the current chi caches. It says nothing about whether another LP recovers
`a_K`; `qou-fu8c` and `probes/ak_lp_dual_quotient_probe.py` cover that.

The producer hands Clarabel the costs through float64. Zeros stay zero, so the
face structure above is the face of the LP actually solved; only the identified
nonzero values could differ, in the last float64 digits.

## Owner decision: what to publish for an unidentified dual coordinate

Nothing changes in the producer until this is decided. Measured blast radius:
`computations/a-K-via-lp-dual-full.witness.json` only; no content block and no
probe reads `u_lambda_star`, `active_set`, `n_active` or the two dual sums from
it.

1. **Intervals.** Emit `u_lambda_star: null` plus
   `u_lambda_star_interval: ["0", "+inf"]` and `u_identified: false` on `c = 0`
   rows; compute `active_set` and the two sums over identified rows only, or
   emit them `null` with a reason. *Costs:* about 30 lines in the producer and
   one witness regeneration. *Risks:* field types change to nullable, and the
   LP-dual validator must accept a null `y_star` entry. *Commits to:* the
   witness says what the LP determines and nothing more; it stops moving on
   solver bumps.
2. **Canonical point by a stated rule.** For example the minimum-norm optimal
   dual, which here sets `u = 0` on every `c = 0` row (they appear in no
   constraint), so those rows drop out of `active_set`. *Costs:* the same edit.
   *Risks:* a convention prints a number where the LP has none, and `u = 0`
   reads as "inactive", which is a choice, not a finding. *Commits to:* every
   future reader must know the rule.
3. **Re-pose the LP on the `c ≠ 0` support** (the two-row quotient `qou-fu8c`
   asked for). *Costs:* a different LP; `ak_lp_dual_quotient_probe.py` already
   shows `y0` becomes nonzero there and `a_K` is still not recovered.
   *Commits to:* changing the producer's object, not just its reporting.
4. **No-op (default).** The witness keeps publishing an arbitrary point; it
   moves on every Clarabel change, and `active_set`, `n_active` and
   `chirality_dual_sum` stay solver artifacts.

*Recommendation (judgement, not finding): 1.* It is the only option that
reports exactly what was measured, and with no consumers reading these fields
the cost is the producer edit alone.

## Reproduce

```sh
PYTHONPATH=tools/qou-substrate/python:tools/pyhecke/python:computations \
  python3 -u computations/probes/ak_lp_dual_face/ak_lp_dual_face_probe.py
```

Runtime: under a minute for the first five atoms; helium-4 (77 partitions,
155 dual variables, 2×155 face LPs in exact arithmetic) dominates at
about 8.5 min per helium-4 run (two runs: cache as is, and the exact-zero arm).
