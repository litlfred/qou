---
# qou-dke6
title: 'LP/SDP witnesses: 107 of 241 dual records are f64-era or unattributable; re-running moves residuals ~36 orders'
status: todo
type: task
priority: normal
created_at: 2026-09-04T08:14:33Z
updated_at: 2026-09-04T12:20:10Z
---

Found while wiring `qou-fr4d` (certified LP duality residuals). NOT caused by
that change -- established by measurement, see the attribution test below.

## The measurement

Scanning all 3488 tracked `computations/*.witness.json` for records carrying
the full LP/SDP dual field set (`y0_star`, `y_star`, `primal_obj`, `dual_obj`,
`duality_gap`) -- 54 files, 241 records:

    clarabel-mpfr        134
    <no backend field>   105    <- predates the field; nothing says how solved
    scipy-highs            2

So **107 of 241 (44%) are explicitly float64 or unattributable.**

## Why that matters, measured on three producers

Re-running three LP producers in an environment where the clarabel-MPFR
binary IS present, against their committed witnesses:

| producer | changed existing values |
|---|---|
| `derive_e_0_lp_dual_h3` | 304 |
| `pn_alpha_lp_dual` | 2292 |
| `rho_k_h3a_lp_dual` | 86 |

and the movement is not noise, it is the backend transition:

    duality_gap   committed 1.3871930965660104e-15   re-run 5.3455294201843912e-51
    x_star[2]     committed 6.293838348221709e-15    re-run -8.888369995547171e-39
    y_star_str[4] committed 3.82694087248660635e-14  re-run 3.8269387334409869e-102

The committed values sit at the **float64 noise floor**; the re-run values are
genuine. This is precisely the hazard `lp_dual_solver.py` documents in its own
source: *"the same producer run in CI, in a fresh container, and on a developer
box could write witnesses differing by ~28 orders of magnitude in residual with
nothing in the file saying which had happened."* Here it is, live on `main`,
and the `<no backend field>` bucket is the population where it is undetectable
from the file.

## Attribution -- this is NOT the qou-fr4d solver change

Tested rather than reasoned, because a code read is not evidence. Reverted the
solver to HEAD and re-ran with the UNMODIFIED code:

- `rho_k_h3a_lp_dual`: `primal_obj` still moves 3.2843401771028216 ->
  3.283906568708643 (that producer does not even call the canonical entry
  point -- it uses `scipy.optimize.linprog` directly).
- `derive_e_0_lp_dual_h3`: **the identical 304** changed values.

So the drift is entirely pre-existing.

## What NOT to do

Do not mass-regenerate. Two reasons:

1. Regeneration is **environment-dependent by construction** -- the value you
   get depends on whether the clarabel-MPFR binary is on the box. A sweep run
   without it would rewrite 134 good MPFR records as f64, which is strictly
   worse than the current state. Any sweep must set `QOU_REQUIRE_CLARABEL=1`
   so a missing binary is an error rather than a silent downgrade.
2. These are real numbers that downstream analysis has read. A 36-order move
   in a residual may or may not change a conclusion; that is per-producer work.

## Cheapest first step

Not a sweep: an **audit** that reports, per LP/SDP witness, which backend its
dual records claim and whether the producer reproduces them under
`QOU_REQUIRE_CLARABEL=1`. That separates "stale because f64-era" from "stale
for some other reason" without rewriting anything, and gives the sweep a
denominator. The 105 unattributable records are the ones worth resolving first
-- they are the bucket where the file itself cannot tell you.

## Related

- `qou-fr4d` -- the certified-residuals wiring that surfaced this.
- `qou-ftuv` (completed) -- states the LP path is f64-only, which is stale.


## 🛑 CORRECTION TO THIS BEAN, by the audit it asked for

This bean says "107 of 241 (44%) are explicitly float64 or unattributable" and
frames it as a population needing a staged sweep. **The count is right; the
framing overstates the problem by an order of magnitude.**

`computations/audits/lp_dual_backend_inference_audit.py` infers the backend
from the numbers, needing NO producer run. The two backends leave floors ~28
orders apart and the floor is visible in `log10(duality_gap / max|x*|)`.

**Calibrated on the records that DO declare a backend** -- which is what makes
it a measurement rather than a guess:

    clarabel-mpfr   n=117   min -53.7   median -48.8   max -37.9

Every labelled MPFR record sits below -37.9. The undeclared population has a
median of -16.8, the float64 epsilon signature. Cut placed at -30, inside the
empty band; the -37.9..-30 interval is reported AMBIGUOUS rather than forced.

**Result over the 105 undeclared records:**

| | count |
|---|---|
| unclassifiable -- **no `x_star`** | **84** |
| inferred f64-era | 9 |
| unclassifiable -- gap exactly 0 | 7 |
| inferred mpfr-era (just unlabelled) | 5 |

and of the 9 inferred f64-era, **EIGHT are under `computations/_deprecated/`**.

**The live f64-era exposure is ONE record** -- `borromean-axial-coupling`,
rel = -20.8 -- and it is already fixed in PR #6619. **There is no sweep to
run.** The staged-migration plan this bean proposes is not needed.

## The real gap is different, and larger

**84 of the 105 carry no `x_star` at all.** That is not a contract violation --
AGENTS.md's LP-dual required list is y0_star / y_star / active_set /
primal_obj / dual_obj / duality_gap, and `x_star` is not on it. But it means
BOTH this audit AND the certified-residual check from `qou-fr4d` (PR #6609)
are structurally blind to them: with no primal vector there is no scale to
normalise the gap against, and no certificate to re-derive it from.

So the question worth asking is not "which of the 105 were solved in f64" --
that is answered, and the answer is one. It is **"should `x_star` be a
required LP-dual field?"** If it were, 84 records would become checkable by
two independent mechanisms that currently cannot see them. That is an owner
decision about the shared contract in AGENTS.md, not something to change
unilaterally, and it is the honest successor to this bean.


## 🛑 SECOND CORRECTION — this bean's own headline is inflated by a double-count

"107 of 241 (44%)" and the "105 undeclared" figure in the correction above are
both wrong, by the same defect: **54 of the 241 five-key matches are WRAPPERS,
not records.**

Producers hoist `primal_obj` / `dual_obj` / `duality_gap` / `active_set` /
`y0_star` / `y_star` onto a parent dict alongside a nested key holding the real
record. Counting both double-counts the solve -- and because the hoisted copy
omits `x_star`, it also manufactures a phantom "record with no primal vector".

Worked case: `pn-alpha-lp-dual.witness.json` reported 41 records WITH `x_star`
and 41 WITHOUT. They are **the same 41 solves**; the x* is one level down on
`.lp_dual`. That producer has **zero** genuinely x*-less solves.

Corrected figures (leaf records only):

|  | before | after |
|---|---:|---:|
| five-key matches | 241 | 241 |
| of which WRAPPERS | — | **54** |
| genuine leaf records | 241 | **187** |
| undeclared backend | 105 | **56** |
| no `x_star` | 84 | **36** |
| inferred f64-era | 9 | **8** (7 deprecated + 1 live) |

**The conclusion is unchanged and slightly stronger: one live f64-era record,
already fixed. No sweep.**

## The x_star successor question is SMALLER than stated, and is not a contract question

The correction above proposed asking the owner whether `x_star` should join
the LP-dual required-field list, on the strength of "84 records blind to the
certified-residual check". The real figure is **44 across all leaf records,
and 27 of those are a SINGLE producer** --
`sigma-f-electron-shell-chain`, whose `.data.sigma_f_chain[i].dual` blocks
carry `y0_star`/`y_star`/`active_set` and no primal vector at all. The
remaining 17 are one record each.

**A contract change is the wrong instrument for that shape.** One producer is.
Withdrawing the owner question: it was raised on an inflated number, and the
honest form is a small fix to `sigma_f_electron_shell_chain` to serialize the
primal it already computes -- if it does. That is worth checking before
anything else here.
