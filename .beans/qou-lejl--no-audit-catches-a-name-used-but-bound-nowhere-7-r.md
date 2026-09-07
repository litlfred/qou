---
# qou-lejl
title: No audit catches a name used but bound nowhere — 7 real defects found by an ad-hoc scan this session
status: completed
type: task
priority: normal
created_at: 2026-09-06T11:01:16Z
updated_at: 2026-09-07T09:48:03Z
---

## The gap

Every mechanism here that could catch a `NameError` requires EXECUTION, and the
files that break this way are exactly the ones nothing executes.

- `producer_importability_audit` imports each producer, so it sees names
  undefined at **module level** only. A name used inside a function is
  invisible: the import succeeds, the module looks healthy, and the NameError
  waits for whoever calls that function.
- `tests/` + `tools/qou-substrate/tests/` run 209 tests and execute **none** of
  the 300+ probes. A probe can be dead for weeks and stay green.

## Evidence it is not hypothetical

An ad-hoc version of this scan found **7 live defects** this session that both
mechanisms had passed — and every one has the same shape: **a block rewrite
dropped a definition while its consumer, elsewhere in the file, survived.**
Merges, bulk transforms and convention migrations all produce it; none is
careless, the consumer is simply outside the diff's line range.

| where | name | what dropped it |
|---|---|---|
| `hecke_core_legacy` | `_is_sparse_sigma` | merge took HEAD for 12 hunks, call site auto-merged outside them |
| `qbeta_cosine_parametrisation…` | `_os_sidu` | bulk transform injected the import INSIDE the docstring |
| `witness_failed_assertion_audit` | `_os_sidu` | same |
| `qbeta_delta_vs_deltaTbeta_settled…` | `Path` | `pathlib` never imported; dead at import for six days |
| `he_nu_sdp_barfold_h9_test` | `RAIL` | q0-anchor migration rewrote the `Q0 = …` / `RAIL = …` block |
| `he_nu_sdp_psd_count_test` | `H` | same |
| `he_nu_sdp_saturation_obstruction` | `RAIL` | same |

Only the first was caught by a suite, and only because it happened to be
module-level (46 tests red). The three `he_nu_sdp` names sit on the **LP success
path** and all three publish witnesses.

## Built: `computations/audits/undefined_name_audit.py`

Static AST over every tracked `.py`. **No execution.** Whole-file scoping
deliberately — a name bound anywhere counts as bound — so it under-reports
rather than false-alarms, which is the right side to err on for a detector
nobody trusts after its third bad call.

`--selftest` proves the classifier on **15** cases, including the calibrated
false positives that a naive version gets wrong.

### Calibration mattered — the first run was 14 findings, 7 of them wrong

- **Lambda parameters.** Without binding them, `key=lambda kv: kv[1]` reports
  `kv`: **95 false positives** in the very first run.
- **Annotation-only loads.** `derivation_chain.py` has
  `M_HECKE_PIPELINE_AT_Q0: dict[str, mp.mpf]` with mpmath never imported. Under
  `from __future__ import annotations` that annotation is a string and is never
  evaluated — no runtime error. Reporting it would have put a false alarm on a
  module **27 files import**. A name is now reported only when some load of it
  is OUTSIDE an annotation.
- **`exec()` / `eval()`.** `computations/hecke/jm_*_probe.py` (5 files) exec a
  sibling probe's source for its `build`. The name IS defined at runtime and no
  static pass can see it, so such files are skipped as unsound, like
  `from x import *`.

## Result: 7 NEW findings, on top of the 7 already fixed

    scanned 4503 tracked .py | star-import skipped 12 | exec/eval skipped 39

| file | line | name |
|---|---|---|
| `computations/crt_markov.py` | 352 | `_q_sym` |
| `computations/deltalambda/a4_interface_operator_driver_search_probe.py` | 77 | `Q_50_DIGIT_STR` |
| `computations/from_scratch/derive_he3.py` | 66 | `tr_M_q0` |
| `computations/markov/hecke_regular_nf_table.py` | 187 | `_HERE_W` |
| `computations/probes/finite_q_volume_conjecture_probe.py` | 158 | `vol41` |
| `fluid_part2.py` | 98 | `append_to_file` |
| `qou-mass/.../schur_principal_mpmath.py` | 258 | `_pb` |

Spot-checked four by reading the code: all genuinely used and bound nowhere —
`_q_sym` inside a loop, `vol41` in a print, `_pb` loading a witness path.

The witness asserts `findings == 0` and is therefore **red at 7**, which is the
ratchet. That is the convention here: 18 of 48 audit witnesses are red.

## NOT fixed here — unclaimed

This is a DETECTOR. A finding is a question ("where did this name go?"), not a
verdict, and the answer belongs with whoever knows the intent. The three
`he_nu_sdp` names were recovered from the commit each witness records in
`scriptCommitSha` rather than invented from a plausible magnitude; the 7 above
deserve the same treatment and have not had it.

---

## Wired into the gates array (2026-09-06)

`scripts/precision-gates.sh` now carries it, blocking:

    "…|--strict --no-witness|yes|yes"

**Ratchet, not bare `--strict`.** A blocking gate that is red on arrival gets
skipped — the failure mode that file's own header warns about — so it tolerates
the committed backlog via a `*-baseline.json` and blocks only what is NEW or
GREW. `--rebaseline` refuses to run if any count went up: draining only.

Confirmed by EXECUTION, not by reading the array:

- green at its own baseline (exit 0) under the harness's exact invocation;
- **red on an injected regression** — a throwaway probe with one unbound name
  made it exit 1 and name the file, then was removed. A detector that cannot be
  shown to fire is a no-op, which is why the harness self-tests at all.

### The harness caught a defect in the wiring itself

`precision-gates.sh` invokes `python3 <script> --self-test` — **hyphenated** —
and treats a non-zero exit as "a detector that cannot be shown to fire". Both
audits were written with `--selftest` only (copied from
`retired_pin_live_code_audit.py`, which is in no array and so never had to
match). They would have failed their gate on arrival, silently, for a reason
having nothing to do with what they detect. Both spellings are accepted now.

That is the qou-j6gb lesson landing a third time: a gate outside the array is a
gate nobody runs — and a gate inside it that the harness cannot invoke is the
same thing wearing a badge.

### Not verified here

The full `precision-gates.sh` run fails PREFLIGHT in this container
(`missing: qou_substrate`, needs `pip install -e tools/qou-substrate`). The
script itself says that is not a gate failure. So the two gates were exercised
by replaying the harness's own `--self-test` + `$args` sequence against them,
not by a whole-suite run; the remaining 25 gates are unexercised here.

### The same defect was already live in the array — found by looking

Wiring my own gates surfaced the `--self-test` / `--selftest` mismatch, so I
checked whether anything else in the array had it. It did:

    scripts/word-provenance-gate.py    declared selftest=yes, accepts only
                                       --selftest, so `--self-test` exits 2
                                       ("unrecognized arguments") and the
                                       harness has been recording a SELF-TEST
                                       FAILURE for it — for a reason having
                                       nothing to do with braid-word
                                       provenance. Confirmed by running it.

Fixed in two places, because one of them is the recurrence:

- the script now accepts both spellings;
- **`precision-gates.sh` now tries either**, so the next script cannot repeat
  it. If a self-test genuinely fails, both spellings fail and it is still
  reported — the OR only forgives the flag name, never the result.

Verified by EXECUTING all 22 gates that declare `selftest=yes`: 22/22 pass.
Before this, one was failing and the two added today would have made three.

---

## 2026-09-07 — 7 → 5, and the graft splits the rest three ways

Worked the detector's own findings. First the clone had to be deepened
(`git fetch --depth=2000`): at `--depth 1` **every** `git log` answer is a graft
artifact, so the recovery method that settled `RAIL`/`H` — read the definition
back from the commit where the name WAS bound — could not run at all. After
deepening: 16184 commits, one boundary at `3f2744fc13` (2026-07-18).

That boundary is what makes the results honest, because it splits the seven:

**Full history available — the "never defined" verdict is trustworthy (3)**

| file | name | outcome |
|---|---|---|
| `markov/hecke_regular_nf_table.py` | `_HERE_W` | **FIXED** |
| `deltalambda/a4_interface_operator_driver_search_probe.py` | `Q_50_DIGIT_STR` | **FIXED** |
| `qou-mass/.../schur_principal_mpmath.py` | `_pb` | needs a decision |

**History truncated at the graft — verdict UNKNOWN, not "never defined" (4)**

`crt_markov.py:_q_sym`, `from_scratch/derive_he3.py:tr_M_q0`,
`probes/finite_q_volume_conjecture_probe.py:vol41`,
`fluid_part2.py:append_to_file`. Their oldest reachable commit IS the boundary,
so "the name was never bound" is exactly what a truncated history says whether
or not it is true. Left alone.

### `_HERE_W` — one bad paste, two defects

The definition existed, inside `LEAN_TEMPLATE`:

    import Mathlib.Tactic.FinCases

    from pathlib import Path as _PathW  # noqa: E402 — witness output root
    _HERE_W = _PathW(__file__).resolve().parent

    /-!
    # QOU.Machinery.H4 — ...

Two lines of Python pasted into a Lean source string, between the Mathlib
imports and the doc block. So (i) `_HERE_W` was undefined in Python and the
witness write `json.dump(open(_HERE_W / "...witness.json","w"))` raised
NameError, and (ii) the emitted `QOU.Machinery.H4` carried two lines of Python,
which is not valid Lean. Moving them out fixes both.

Same shape as the `import os as _os_sidu` a bulk rewrite dropped into a
docstring: **a definition that landed inside a string literal**. Verified by
parsing `LEAN_TEMPLATE` as an AST string constant, not by grepping — a text
search matches the explanatory comment I added and reports a false positive.

### `Q_50_DIGIT_STR` — a fallback that could not fall back

    try:
        from q_parameter import Q_MP
        return mp.mpf(Q_MP)
    except Exception:
        return mp.mpf(Q_50_DIGIT_STR)      # never imported

Reading q0 BY NAME (bean qou-9ugp) replaced a hardcoded literal here without
adding the matching import, so the `except` raised NameError instead of falling
back — and only on the path taken when the `try` already failed. Fixed with the
local import the `try` itself models; the canonical form appears 619 times.

### `_pb` — NOT fixed, deliberately

`_pb.witness_path(...)` clearly means `computations/_path_bridge`, the only
module defining `witness_path`. But this file is in `qou-mass`, whose `__main__`
puts only its own directory on `sys.path` — `_path_bridge` is not reachable
there, and `qou-mass` has no `witness_path` of its own (its convention is a
local `_WITNESS_DIR`). So the fix is a **decision** — should `qou-mass` depend
on `computations/_path_bridge`, or use its own convention — not a missing line.
That is the case this audit's docstring describes: a finding is a question.

Baseline drained 7 → 5; the ratchet is green at the new baseline.

---

## 2026-09-07 — the shallow clone was the blocker; 7 → 1, and one real defect

**The four "UNKNOWN" verdicts were an artifact of `--depth`, not of the code.**
`git fetch --unshallow` gives **36771 commits and one real root**
(`2e1c6929e0`) with no graft. Re-asked against that, all four names were
introduced **already unbound**, at ordinary single-parent commits 14104 and
17964 deep. The verdict is *never defined*, same as the three settled earlier.
This is the general lesson: "the oldest reachable commit is the boundary" and
"the name was never bound" are indistinguishable at `--depth 1`, and the only
way to tell them apart is to deepen — not to reason harder.

### `_q_sym` — the SW path has never executed, in the file's whole life

`crt_markov.tower_mass_symbolic_eval` builds its Schur-Weyl per-stratum tower
inside a `try`, and `per_stratum_sum_symbolic(A, {i}, _q_sym)` raises
`NameError` on the **first iteration of every call**. The `except` names
`NameError` explicitly and says it "covers the SW-desc-failed case where
`_sp` / `_q_sym` are unbound" — but `_q_sym` is unbound *unconditionally*, so
that branch is not a fallback, it is the only path.

What runs instead is the legacy per-generator `V_full × Φ_q` sum — the path the
comment four lines above describes as what "drove single + cross to spurious
millions". Measured, A=1, proton anchor, 30 dps:

| | desc | single | cross | **total** |
|---|---|---|---|---|
| legacy fallback (what shipped) | 0.505404 | 16 969 232.838 | 656 993.570 | **17 626 226.914** |
| SW path (what was intended) | 0.505404 | 3 700.476 | 694.555 | **4 395.536** |

A factor of ~4009. The stderr line `[crt_markov] SW tower fallback (NameError:
name '_q_sym' is not defined)` was printed on every call and read as a
legitimate conditional fallback.

**It was safe to land**: every live call site is inside `crt_markov.py`'s own
self-test, every external caller is under `_deprecated/`, and the file's own
line 16 records that its witness was moved to `_deprecated/` in PR #554. No
published number moves. Had there been a live consumer this would have been an
owner sequencing call like `qou-zbws`.

### `tr_M_q0` — and a prior defect hiding behind it

A rename moved the `_print` display suffix onto the **definition**
(`tr_M_q0_print = float(...)`) and left the four uses on the old name — three
of which are compute, not display. Restored as a value (`sympy` Float at 30
digits) plus a separate `_print` cast, so the float64 stays in the formatter
where the `compute_no_mpf_to_float_cast` exemption expects it.

Running it to check exposed something the AST could not: `derive_he3.py` and
`derive_t_h5.py` import `experimental_constants` / `codata_constants` by bare
name with **no `_path_bridge`**, and those modules moved to
`computations/substrate/` in the Phase 6 refactor. Both died at
`ModuleNotFoundError` *before* the NameError could be reached. Nothing else in
`from_scratch/` (7 files) has the defect. Both now run end to end and both
pass their own hardcoded cross-checks — `tr_M(³He) = 0.998367` against
Wenzl-Schur, and T likewise. **That is the check worth having**: the script
verifies itself against an independently computed value, so "it runs" and "it
is right" are answered together.

### `vol41` — bound as `VOL_41`, read as `vol41` six times

So the probe raised NameError at the first print and never reached `w.save()`;
its committed witness predates the rename. Renamed the binding.

Not folded in, deliberately: `2.0298832128` is still a **hand-typed volume
literal** (correct to 11 digits against Vol(4₁) = 2.029883212819307…). Sourcing
it from the canonical registry is **`qou-ckbv`**'s excision. Doing it here
would move a published number under cover of a NameError fix.

### `_pb` — not the decision the bean thought it was

Held as "should `qou-mass` depend on `computations/_path_bridge`?". It is
neither option: the source file **already** does `import _path_bridge as _pb`,
and `scripts/sync-qou-mass-vendor.py` drops every line starting
`import _path_bridge`. The strip removed the **binding** and kept the **use**.

That is not rot the vendored copies suffer — it is rot the sync **creates**,
silently, and invisibly in review, because the deleted line and the surviving
call are 200 lines apart. It is also the *same shape* as the `del ..., _bridge`
bug that function's own docstring already records as paid for once.

Two changes: the upstream file got a seam that needs no bridge in either layout
(try `HERE`, then `HERE.parent` — which is `computations/` in one and the
package root in the other, where the sync's own `WITNESS_DEST` note says
vendored witnesses land); and `render()` now **raises** when a dropped bridge
import bound an alias the module still loads. Per the script's own rule —
"if a module ever needs a genuine package-specific adaptation, it does NOT
belong in this script; give it a real seam upstream" — a loud failure is what
routes the next one there. An AST scan over the 49-module cone confirms this
was the only instance.

Also re-synced the **8 vendored files the `qou-zv46` regeneration left
drifted** (7 modules + 2 witnesses); `--check` is clean.

### `append_to_file` — by construction; recommending deletion, not deleting

`run_part2.py` defines the helper, reads `fluid_part2.py` as **text**, strips
its last line, `exec`s it, then calls the helper itself. So the unbound name in
`fluid_part2.py` is how the thing was meant to work.

It is spent one-shot authoring scaffolding: it writes to a hardcoded
`/Users/litlfred/space_cats/qou/amalgamated_done/` path that exists on no
machine here, its target `fluid-dynamics_seq6.md` is not in the repo, and its
three markdown blocks **already landed as folio blocks** under
`content/quantum-observable-universe/fluid-dynamics/`
(`levi-degeneracy-conjecture`, `townsend-biot-savart-strain`,
`vorticity-lower-bound` — prose compared, not just filenames).

**Recommendation: delete `fluid_part2.py`, `fluid_part3.py`, `run_part2.py`.**
Left in place — deleting three root-level files is the owner's call, not a
side effect of a name audit. Baseline rebaselined **5 → 1** and green, so this
one entry is the whole remaining ratchet.

Verified: `tests/` 64 passed, `tools/qou-substrate` 145 passed, `qou-mass`
unchanged at 7 failed / 13 passed (the pre-existing `qou-qe81` set),
`sync-qou-mass-vendor --check` clean.

**Open on this bean: nothing but the owner's call on the three fluid files.**
