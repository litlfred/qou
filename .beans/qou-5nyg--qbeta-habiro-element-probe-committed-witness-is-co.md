---
# qou-5nyg
title: 'qbeta-habiro-element-probe: committed witness is convention-C, live data is D'
status: todo
type: task
created_at: 2026-08-24T09:01:49Z
updated_at: 2026-08-24T09:01:49Z
---


## What the committed witness says vs what the data says

`qbeta_habiro_element_probe` has been dead on `main` since the upstream
`habiro-coefficients-atomic.witness.json` was respelled `check_q` -> `u`
(the crash is `TypeError: 'NoneType' object is not subscriptable`, from
CPython falling back to `__builtins__["u"]` when `__builtins__` is `None`).
Fixed on the branch for `qou-geqa` by binding both spellings, the established
`term6_full_pole_sum` fix.

With it running, the committed witness turns out to be **convention-C
throughout**, while the data it reads is **convention D** — canonical since
the 2026-08-15 owner ruling R1:

| field | committed (C) | fresh run (D) |
|---|---|---|
| `p_denom` | `4*check_q**21 + 4*check_q**19` = 4u¹⁹(u²+1) | `4*u**26 + 8*u**22 + 4*u**18` = 4u¹⁸(u⁴+1)² |
| `n_denom` | same as p | `4*u**18` |
| `shared` | `true` | `false` |
| `p_a_0` / `n_a_0` | `4` / `4` | `8` / `2` |
| A: `tr_M_habiro` (p) | 1.06530614… | 1.14575969… |
| A: `rel_ppm` (p) | 0.079187 | **0.000000** (5.3e-17) |
| C6 `diff_a_m` | computed, in `check_q` | **refused** |

Two things worth separating. The **stale-witness** part is the mechanism
AGENTS.md §4 already documents — a producer that cannot run has a permanently
frozen witness. The part that is *not* in that text: this frozen witness is
not merely stale provenance, it carries **convention-C conclusions asserted as
current findings**, including a `shared denominator` claim that is false under
the canonical convention. A reader had no signal; the file looks fine.

Note the reconstruction also got *better*, not worse: sub-task A goes from
0.079 ppm to 5.3e-17, i.e. exact to the arithmetic. The C-frame 8e-8 residual
was the mismatch, not a limit of the method.

## Why the witness is NOT committed with the fix

Two reasons, either sufficient:

1. **Environment downgrade.** `witness_base`'s own guard fires: this container
   records python 3.11.15 / numpy 2.4.6 / scipy 1.17.1 against the witness's
   3.13.12 / 2.5.0 / 1.18.0. The interpreter cannot be changed here, so the
   guidance ("install it and re-run rather than committing the weaker record")
   is unsatisfiable in this session.
2. **Scope.** Flipping a witness from the C frame to the D frame is a
   *convention migration*, tracked under the `qou-cds1` tranche — not a crash
   fix. Landing it inside a "fix crashing producers" PR would bury a migration
   in an unrelated change. Same call, same reason, as holding the pentagon
   float64 drain (`qou-5mao`) off that PR.

## Next step

Re-run on a container matching the recorded environment and commit the D-frame
witness as part of the convention-D tranche, citing this bean. The script fix
is already landed and is a precondition — before it, the producer could not
produce *any* witness, C or D.
