---
# qou-cm7l
title: 'Vacuous-pass assertions: 8 producers compare two zero-initialised counters with no guard'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T09:37:58Z
updated_at: 2026-10-04T15:25:26Z
parent: qou-5vkl
---

## The shape

    n_pass  = 0            # zero-initialised
    n_total = 0
    for target in targets:
        if <target unavailable>:
            continue       # skips WITHOUT incrementing n_total
        n_total += 1
        ...
        if ok: n_pass += 1

    w.add_assertion("...", computed=n_pass, expected=n_total)

`n_pass == n_total` is **trivially true when both are 0**, and both are 0
whenever every target is skipped — typically because an upstream cache is
missing. The producer then emits `allPassed: true` having verified nothing.

This is the compute-side analogue of `theorem X : True := trivial`, which
AGENTS.md bans outright in Lean (*"tautological conclusions are banned … any
proposition that is provable without using any hypothesis"*). There is no
equivalent rule, and no checker, for the Python side.

## Measured, 2026-08-26

Detector: AST over the 3226 tracked `computations/**/*.py` (normalised through
`_source_normalise.code_only`, so a docstring cannot match). Flags
`add_assertion(computed=X, expected=Y)` where **both** X and Y are names that
are assigned literal `0` somewhere and are the target of a `+=` somewhere —
i.e. both are counters that start at zero.

    3226   producers scanned
       9   assertions comparing two zero-initialised counters
       1   already fixed (sublemma_2_1_h12_he4_phase25, commit 60386f4e4)
    ----
       8   remaining, and ALL EIGHT are unguarded

| producer | line | computed / expected |
|---|---|---|
| `all_nuclides_wedderburn_spectral_v2.py` | 525 | `n_parity_ok` / `n_total` |
| `delta_lambda_v_hat_z_transfer_phase5d_4.py` | 186 | `flavor_rule_passes` / `flavor_rule_total` |
| `probes/A_operator_per_interface_probe.py` | 252 | `n_linearity_ok` / `n_linearity_total` |
| `qbeta/qbeta_hoefsmit_stage_b_per_block_ck_probe.py` | 227 | `n_match` / `n_total` |
| `sublemma_2_1_A_operator_extract_h9.py` | 539 | `n_consistent` / `n_overdet` |
| `sublemma_2_1_h12_he4_branching.py` | 235 | `n_pass` / `n_total` |
| `sublemma_2_1_h9_tritium_verify.py` | 453 | `n_overdet_pass` / `n_overdet` |
| `v_hat_to_delta_lambda_bridge.py` | 350 | `one_dim_matches` / `one_dim_total` |

## The near-miss that is worth more than the list

`v_hat_to_delta_lambda_bridge.py` **looks** guarded — grep finds
`elif one_dim_total == 0:` at line 434. It is not a guard. It sits in the
stdout CONCLUSION block and prints *"no 1-dim channels in scope"*, while the
assertion at line 350 still evaluates `0 == 0` and the witness still records
`allPassed`. The author noticed the zero case, handled it **in prose**, and
left the machine-readable claim vacuously green.

That is arguably worse than not noticing, because it defeats exactly the check
a reviewer would run. Do not accept a `== 0` grep hit as evidence of a guard —
confirm it dominates the assertion.

## Status of each: CANDIDATE, not defect

Only **one** of the nine has been *observed* passing vacuously
(`sublemma_2_1_h12_he4_phase25`, where `load_f1_cache()` returned 0 entries on
this container so all 8 targets were skipped). For the other eight the shape is
present and unguarded, but whether the zero case is reachable depends on which
upstream each needs. **Do not report eight defects.** Report eight unguarded
candidates and one confirmed.

`sublemma_2_1_h12_he4_branching.py` is the most likely of the eight to be live:
it is the direct sibling of the confirmed one, shares the `n_pass`/`n_total`
naming, has three `continue` statements that skip targets, and additionally
`return 0 if n_pass == n_total else 1` — so a fully-skipped run exits **0** too.

## Suggested fix

The same guard used in `60386f4e4`: refuse before writing when the count is
zero, naming the count, the cause and the remedy. One `raise SystemExit` each.
It follows the repo's own idiom for a guard that must not be silently
satisfiable (cf. `low_isotope_mass_table` refusing below its target precision).

**A residual the guard does not cover:** a PARTIAL upstream (3 of 8 targets)
still reports "Verified 3/3" while 8 were targeted. Tightening that changes
behaviour beyond the bug and should be decided per producer.

## Found by

`qou-poi1` — chasing the raw-float64 ratchet's blind spot. The float64 was the
lesser defect; this was underneath it.


## 2026-08-26 — the 8 do NOT take a uniform fix. Do not sweep them.

I recommended "guard the 8 with the same one-line refusal". That is wrong for at
least one of them, and possibly more, because **zero can be a legitimate
outcome rather than a missing upstream**.

`v_hat_to_delta_lambda_bridge` is the clear case. Its zero branch prints

    CONCLUSION: no 1-dim channels in scope.

That reads as a valid scientific result for a filtered run, not an error. A
`raise SystemExit` there would refuse a legitimate outcome. The defect is
narrower than "no guard": the producer states the empty case correctly in prose
while its **machine-readable** claim (`computed=0, expected=0, allPassed`)
asserts a verification that did not happen.

So the fix space has (at least) two shapes:

* **Refuse** — when zero means an upstream is missing and the run is
  meaningless. `sublemma_2_1_h12_he4_phase25` (fixed) is this: the F1 cache was
  absent and it had nothing to verify.
* **Do not assert** — when zero is a legitimate scope outcome. Omit the
  assertion, or record it as not-applicable, so the witness stops claiming a
  passed verification over an empty set. Refusing would be wrong here.

Deciding which applies needs reading each producer's zero case. That is 8
judgement calls, not a sed.

### Reachability is still unmeasured for all 8

`sublemma_2_1_h12_he4_branching` was the one I expected to be live, being the
direct sibling of the confirmed case. It is **not settled**: it produces no
output within 100 s (setup work before its first print) and timed out at 120 s
in the earlier sweep, which is *weak evidence it does process targets* — a
fully-skipped run should be fast, as the phase25 sibling's 0.8 s was. A
long-budget run is in flight; until it reports, do not claim either way.

**Consequence for whoever picks this up:** the bean's list is a list of
unguarded shapes. It is not a list of eight bugs, and it is not a batch.


## 2026-08-26 — all 8 classified from the source. The discriminator is WHERE
## THE INCREMENT SITS relative to the skip.

The question is not "is there a guard" but **what does zero mean here**, and
that is answered by reading three lines around the `+= 1`:

| where `n_total += 1` sits | zero means | fix |
|---|---|---|
| **after** a `continue` that skips unavailable targets | the upstream is missing; the run verified nothing | **REFUSE** |
| **after** a `continue` that filters *scope* | nothing was in scope — a legitimate result | **DO NOT ASSERT** |
| inside a branch of a status split (`if underdet / else`) | every case is in the other state — legitimate | **DO NOT ASSERT** |
| **first statement in the loop**, no `continue` before it | only reachable if the input list is empty | **low risk** |

### The 8

**REFUSE — zero implies a missing upstream**

* `all_nuclides_wedderburn_spectral_v2:525` — `n_total` counts entries with
  `A >= 1`; zero only if the nuclide table failed to load.
* `qbeta_hoefsmit_stage_b_per_block_ck_probe:227` — `n_total` counts
  `fnd[side]["nf_terms"]`; zero means the upstream witness carried no terms.

**DO NOT ASSERT — zero is a legitimate outcome, refusing would be wrong**

* `v_hat_to_delta_lambda_bridge:350` — two `continue`s filter channels; zero =
  "no 1-dim channels in scope", which the producer already prints as a
  CONCLUSION.
* `sublemma_2_1_A_operator_extract_h9:539` — `n_overdet` increments only in the
  `elif consistent` branch of an `if underdet` split; zero = every λ is
  underdetermined, a real Phase-2 state.
* `sublemma_2_1_h9_tritium_verify:453` — same shape (`n_overdet` in the `else`
  of `if underdet`).

**LOW RISK — the increment is unconditional**

* `sublemma_2_1_h12_he4_branching:235` — `n_total += 1` is the **first**
  statement in `for lam, d in targets:`, with no `continue` before it. It
  therefore counts every target and **cannot** silently skip while reporting
  zero. Reachable only if `targets` itself is empty, i.e. via an explicit
  `--max-dim` that filters everything out — user error, not a silent upstream
  failure.

  **This corrects my own prediction.** I called it "the most likely of the eight
  to be live", on the strength of it being the confirmed case's direct sibling
  with identical `n_pass`/`n_total` naming. The naming is identical and the
  structure is not: `phase25` has `if lam not in chi_a: continue` **before** its
  increment, which is the entire defect. Sibling-by-name is not sibling-by-shape.

**STILL AMBIGUOUS — need a further read**

* `delta_lambda_v_hat_z_transfer_phase5d_4:186` — `flavor_rule_total` counts
  rows where `r["is_interface"]`. Zero could be "`per_atom` empty" (refuse) or
  "no row is an interface" (do not assert). Distinguishing needs the upstream's
  contract.
* `probes/A_operator_per_interface_probe:252` — same question for interfaces.

### Method note

This classification cost four greps and no compute. I had queued a long-budget
producer run to settle whether `sublemma_2_1_h12_he4_branching` was live; the
source answered it, and better — a run can only show what happens with *this*
container's upstreams, whereas the increment's position settles it for all
inputs.


## 2026-08-26 — the last two resolved. Full classification of all 8.

**`probes/A_operator_per_interface_probe:252` — REFUSE (mixed).** Its lambda
loop carries TWO skips before the increment:

    for lam in parts_sum:
        support = [... for (mu, nu, lam_), c in lr_table.items() if lam_ == lam]
        if not support:
            continue                      # <- upstream: empty lr_table skips EVERY lambda
        ...
        if n_eq < n_unknowns:
            results[...] = {"status": "panel_too_small", ...}
            continue                      # <- legitimate per-lambda outcome, and RECORDED
        ...
        n_linearity_total += 1

So zero has two causes with different meanings. An empty `lr_table` skips every
lambda and is an upstream failure — that is the refuse case. Every lambda being
`panel_too_small` is legitimate, and note the producer already records each one
in `results` with that status, so the information is not lost. The clean fix is
therefore two-part: refuse on an empty `lr_table`, and do not assert when
`n_linearity_total == 0` for the benign reason.

**`delta_lambda_v_hat_z_transfer_phase5d_4:186` — DO NOT ASSERT / low risk.**
`per_atom` is built INTERNALLY, `for name, Z, N in ATOMS:`, from a module
constant — it is not read from an upstream witness, and the producer emits it
(`builder.add_data("per_atom", per_atom)`) rather than consuming it. So an empty
`per_atom` would require an empty `ATOMS` constant. Zero therefore means "no row
is an interface", a property of the computation, not a missing input.

### Final classification — all 8

| producer | verdict | why |
|---|---|---|
| `all_nuclides_wedderburn_spectral_v2:525` | REFUSE | zero only if the nuclide table failed to load |
| `qbeta_hoefsmit_stage_b_per_block_ck_probe:227` | REFUSE | zero means the upstream witness carried no `nf_terms` |
| `probes/A_operator_per_interface_probe:252` | REFUSE (mixed) | empty `lr_table` skips every lambda; `panel_too_small` is benign and recorded |
| `v_hat_to_delta_lambda_bridge:350` | DO NOT ASSERT | zero = "no 1-dim channels in scope", already printed as a conclusion |
| `sublemma_2_1_A_operator_extract_h9:539` | DO NOT ASSERT | zero = every lambda underdetermined, a real Phase-2 state |
| `sublemma_2_1_h9_tritium_verify:453` | DO NOT ASSERT | same `if underdet / else` split |
| `delta_lambda_v_hat_z_transfer_phase5d_4:186` | DO NOT ASSERT | `per_atom` built internally from a constant |
| `sublemma_2_1_h12_he4_branching:235` | LOW RISK | increment is unconditional, first statement in the loop |

**3 REFUSE, 4 DO NOT ASSERT, 1 LOW RISK.** None of them is the sweep I first
proposed, and the split is close to even — which is the point.

### What is now known vs still unknown

**Known, from the source, for all inputs:** which of the two fixes each producer
needs, and that one of the eight is not really at risk.

**Still unknown:** whether any of the seven at-risk cases is *currently* firing
on this container's data. That needs a run each. It does not change which fix
applies — the fix follows from what zero MEANS, not from whether zero happens
today.

In-progress in Round 102 PR litlfred/qou#8453.
