---
# qou-j6gb
title: mpf_import_time_dps_audit is NOT wired into precision-gates.sh — 288 findings, 185 proven lossy, gate silent
status: in-progress
type: bug
created_at: 2026-08-10T02:36:03Z
updated_at: 2026-08-10T02:36:03Z
---


## The finding

`computations/mpf_import_time_dps_audit.py` exists, is position-aware, runs, and
exits **1** under `--strict`:

    module-scope mpf built before precision is raised: 288  [witness-emitting scripts]
       proven lossy (literal arg):                     185
       position-risky (expr arg, not statically provable): 103
    files affected: 91

It is **not in `scripts/precision-gates.sh`'s `GATES` array.** The eight that are:

    q0-anchor flip            q0_anchor_consistency_audit.py
    mpf(<float>) source       mpf_float_source_audit.py
    float64-padding ratchet   witness_float64_padding_audit.py
    mp.dps no-op              mpf_context_dps_audit.py
    module-const precision    module_const_precision_audit.py
    raw-float64 ratchet       witness_raw_float64_audit.py
    q0-value drift ratchet    q0_value_drift_audit.py
    no-free-parameter cert    no_free_parameter_certificate.py   (advisory)

Per bean `qou-mnrd` and AGENTS.md §"QA is agent-owned; CI is a backup",
`precision-gates.sh` **is** the gate — `witness-staleness.yml` is dispatch-only
under the owner's 2026-06-30 Actions-billing directive, reaffirmed 2026-08-09.
So an audit outside that array is an audit nobody runs.

## Why this matters more than the raw count

The defect it detects hit **five times in the drain arc** (`qou-mnrd`), each time
found by accident when something happened to print at high dps, each time a
one-line fix:

    VOL_41              one_loop_c_sigma_tetrahedral_probe.py
    q0                  gram_qtrace_hutchinson_probe.py
    TOLERANCE_PPQ       cross_check_trM_1ppb.py
    REG_ZC / REG_ZD     y_lambda_su_n.py                      (two constants)

All five were caught by *other* gates (`module-const precision`,
`float64-padding`) reacting to downstream symptoms. The audit built specifically
for the cause was sitting right there, unrun. `qou-brkp` records that this same
audit was ALSO silent on two files its own remediation had broken — that bug is
fixed, but the audit went from "silent for a parse reason" to "silent because
nothing calls it", which is the same outcome by a different route.

## Why it is probably unwired, and what to do about it

Almost certainly because adding it blocking turns the gates red on day one: 288
findings is not a thing anyone drains in one sitting.

**Wire it as a ratchet, not as a pass/fail.** That is exactly the shape that took
`witness_raw_float64_audit.py` from red to green over this arc:

  1. baseline the current 288 into a `mpf-import-time-dps-baseline.json`, with
     the audit's own "do NOT add a file to the baseline to silence this" warning
     in its header;
  2. block only NEW and REGRESSED entries;
  3. add it to `GATES` with `blocking=yes`, and to the workflow's step list —
     `precision-gates.sh` carries an explicit instruction to keep those two in
     sync.

Then the 185 proven-lossy are a background drain like the float64 ones, and a
sixth instance cannot land.

**Do the 185 before the 103.** "Proven lossy (literal arg)" means a decimal
string was parsed at 15 dps and the digits are gone — statically certain, and the
fix is the idempotent `set_compute_dps()` above the constant. The 103
"position-risky (expr arg)" are not statically provable and some will be fine;
mixing them into the same ratchet dilutes a signal that is currently exact.

## Not done here

Not wired, not baselined. Wiring a new blocking gate changes what every agent's
pre-commit and `/prepare-merge` must pass, which is a scoped decision rather than
a drive-by — and the 288 number should be re-measured at the moment it is
baselined, not taken from this bean.

---

## DONE — wired as a ratchet, 2026-08-10

Owner said "do ratchet". Implemented exactly the shape recommended above, in the
same idiom as `witness_raw_float64_audit.py`.

### Baseline

    computations/mpf-import-time-dps-baseline.json
    91 files / 185 literal / 103 expr

Matches the pre-wiring measurement exactly, so nothing was reclassified on the
way in.

### `literal` and `expr` are baselined and compared SEPARATELY

Per the recommendation above, and it is the one design point worth defending: a
`literal` finding is statically certain (a decimal string parsed at 15 dps —
the digits are gone), an `expr` finding is only position-risky and some are
fine. If the ratchet summed them, a file could gain a proven defect and drain an
unproven one in the same edit and show no change. Separate counts make that
impossible.

### Unparseable files are never baselined and always fail

Not a stylistic choice. Bean `qou-brkp` records this audit having reported
*clean* for two files its own remediation had just broken, because `scan_file`
returned zero rows on a parse failure — "no information" rendered as "no
findings". The parse bug is fixed, but the ratchet would have re-introduced the
same hole if a broken file could be baselined at zero. There are **0** such
files at baseline time, so this cannot be red on arrival; if one appears it is a
real regression.

### Verified by making it fail, not only by watching it pass

A ratchet that has never been seen to fire is a no-op — the same principle the
`--self-test` flags in this family exist for. Three cases:

    A  new file with a lossy module-scope mpf   → exit 1, listed by name   ✓
    B  baselined file gains one constant        → exit 1, REGRESSED shown  ✓
    C  probe removed / file restored            → exit 0                   ✓

Plus `--self-test` green (8 cases) and `--strict` green at baseline
(0 NEW, 0 REGRESSED, +0/+0).

`--rebaseline` refuses to run under `--all`: that scan includes scripts emitting
no witness, which the baseline does not cover, so rebaselining from it would
silently widen the tolerated set by ~100 files.

### Wired in BOTH lists

    scripts/precision-gates.sh   GATES[]  →  "import-time dps ratchet|…|--strict|yes|yes"
    .github/workflows/witness-staleness.yml  →  matching step

The script's header carries an instruction to keep those two in sync, and the
whole point of this bean is that a detector in neither list is not a gate. Added
a note to that header saying so in as many words, with this bean as the worked
example.

## Still open — the 185

The ratchet stops a sixth instance; it does not fix the five that landed. The
backlog is now a visible, shrinking number instead of an unrun script.

**Do the 185 `literal` ones first.** Each is statically proven lossy and the fix
is one line — `set_compute_dps()` at module scope above the constant. The 103
`expr` ones are not statically provable and some will be fine; working them
first would spend effort on maybes while certainties sit.

Largest single offenders at baseline:

    48  computations/inverse-markov-qvalues.py
    14  computations/binding_block_multiplicative.py
    14  computations/meson_mass_from_hecke.py
     8  computations/m_tau_complex_volume_search.py

Bean stays open with status in-progress until the `literal` count reaches 0.

## Drain pass 1+2 — 185 → 80 proven-lossy, 42 files

    literal (proven lossy)   185 -> 80    (-105)
    expr    (position-risky) 103 -> 90    (-13, incidental: same files)
    files drained             42
    NEW / REGRESSED            0 / 0      throughout

Applied via AST, not text anchoring — see the commit for why (`qou-brkp`'s
insertion-inside-a-dict-literal). Verified three ways each pass: every changed
file parses, every changed file **imports** (the check `qou-brkp`'s breakage
would have failed), and the full gate family stays green.

Pass 2 widened one refusal that was too narrow. Pass 1 skipped any file that did
not *import* `set_compute_dps`; but `a4_interface_kl_subpath_closure.py` and
`a4_option_e_color_tube_closure.py` **define their own** local
`set_compute_dps()` and never call it at module scope. The name was available
all along. Genuine findings, not false positives — and worth remembering as a
shape: a helper defined and never invoked reads as "handled" to a grep.

## Remaining: 80 literal across 26 files, and they need a decision

Every one of the 26 is blocked on the same thing — the name `set_compute_dps` is
neither imported nor defined, so the one-line fix has nowhere to land. Two routes,
and they are not equivalent:

  * **add `from _precision import set_compute_dps`** — canonical, and what the
    other 152 producers do. Needs `computations/substrate` on `sys.path`, which
    is what `_path_bridge` provides; ~19 of the 26 already import it.
  * **insert `mp.dps = 50` at module scope** — no import needed, accepted by the
    audit's `_raises_dps`, and already the idiom in the option_e and probe
    families. But it hard-codes the precision instead of deferring to
    `_precision`, so it drifts if the canonical value ever changes.

Route 1 where `_path_bridge` is present, route 2 elsewhere, is the obvious split
— but adding an import to 19 files is a wider blast radius than inserting a call,
and it should be someone's deliberate call rather than a third automated pass.

Largest remaining, all literal counts:

    12  computations/meson_mass_from_hecke.py
     8  computations/inverse-markov-qvalues.py
     8  computations/meson_gen3_eta_phi.py
     6  computations/deltalambda/perknot_pn_bond_resolved_extensivity_probe.py
     6  computations/probes/yardstick_free_phase_binding_probe.py

## Drain COMPLETE for the proven-lossy class — 185 → 0

    literal (proven lossy)   185 -> 0     (-185)
    expr    (position-risky) 103 -> 51    (-52, incidental)
    files drained             68
    NEW / REGRESSED            0 / 0      throughout all three passes

Pass 3 took the last 26, where the name `set_compute_dps` was neither imported
nor defined. Two routes, chosen per file from what the file can actually reach:

    route 1  (19 files)  imports `_path_bridge`, so `from _precision import
                         set_compute_dps` is reachable — canonical, matches the
                         other 152 producers.
    route 2  ( 7 files)  no bridge; assign dps directly.

Route 2 has a trap worth recording: **both `mp.dps = 50` and `mp.mp.dps = 50`
satisfy the audit's `_raises_dps`, but only one works at runtime**, and which
depends on the import style —

    from mpmath import mp   ->  mp.dps = 50
    import mpmath as mp     ->  mp.mp.dps = 50

so the alias is read off the AST rather than guessed. A gate that accepts both
forms cannot tell you that you picked the wrong one; the source check would go
green on a file whose constants are still built at 15 dps.

Which is why pass 3 was verified at RUNTIME, not just by parsing:

    26 files: import OK 26/26, and mpmath.mp.dps >= 50 after import 26/26

with dps reset to 15 before each import, so one module's raise cannot mask
another's failure. That check is what proves the alias detection right; parsing
and importing would both have passed a wrong alias silently.

## Remaining: 51 `expr` findings, and they are a different question

Not statically provable — `mpf(<expr>)` where the argument is computed. Some are
genuinely fine (an expression over already-high-precision values), some are the
same defect wearing a different sleeve. They need reading, not a fourth
automated pass, and the ratchet holds the line at 51 meanwhile.

Bean stays in-progress on that account. The class it was opened for — the one
that landed five times unnoticed — is closed and cannot recur silently: the gate
is wired in both lists, the proven-lossy count is 0, and anything new fails.

## CORRECTION — the drain does NOT only drain the padding ratchet

The pass-1 commit (`e089dcd1a`) claimed:

> Committed witnesses still carry values computed with the lossy constants;
> they correct themselves when their producers are next run, and that can only
> DRAIN the padding ratchet, never regress it — a constant that gains digits
> removes padding rather than adding it.

**Wrong, and caught by the gate rather than by me.** The reasoning holds for the
constant itself and stops there. Raising module-scope dps also raises the OUTPUT
precision of everything else the producer serializes — including values that are
genuinely float64. Those were previously printed at ~15 digits and looked clean;
at 50 dps they print the binary64 expansion, which is exactly what the padding
audit is built to catch.

Observed, on three producers whose witnesses got rewritten when the pass-3
verification imported them (they write at import time, no `__main__` guard):

    inverse-markov-qvalues   nucleon_results[*].Q_exp, quark_results[*].Q_exp
    meson-mass-from-hecke
    u1-hypercharge-assignment

    committed  "0.782333409310022"                     (15 digits, dps=15)
    after fix  "0.78233340931002215423717416342697..."  (binary64 expansion)

    float64-padding ratchet: 13 baseline -> 18 found, 5 NEW  → RED

The underlying `Q_exp` was **always float64**. Nothing became less precise; the
drain removed the mask. Those three witnesses were reverted here — they were
written by an import side effect, not by a deliberate producer run — and the
padding ratchet is back to 13/13, 0 NEW.

### What this means for the rest of the drain

68 producers now build their constants at 50 dps. Any of them that ALSO carries
a genuine float64 will go red on the padding ratchet the first time it is
deliberately re-run. That is the drain working — a hidden float64 becoming
visible is the point — but it is a **downstream cost that has to be planned**,
not discovered one producer at a time. Three are already identified above.

Concretely, before re-running any of the 68: expect padding findings, and fix
them at the producer (carry the value as a string/mpf from its source) rather
than reverting the dps fix. Reverting would re-hide the float64.

### Method note

The witnesses were rewritten by the verification step itself, because those
three producers write at import time. An import smoke test is not side-effect
free in this corpus. It is still the right check — it is what proved route 2's
alias detection correct — but it needs a `git status` sweep afterwards, which is
how these were caught.

## State on main, 2026-08-15 (re-measured after main moved 1021 commits)

    literal (proven lossy)   0      exit 0
    expr    (position-risky) 51
    drained since baseline   68 files
    NEW / REGRESSED          0 / 0

The drain survived 1021 commits of other people's work intact. Worth stating
plainly because it was not obvious it would: 68 producers were edited, and the
window included at least one incident (recorded on PR #4903 by the #4899 arc)
where a merge resolution taken "to ours" silently reverted a float64 drain on
four witnesses. That the `literal` count is still 0 was checked, not assumed.

The bean's original class — the one that landed five times unnoticed — is
**closed**: the gate is wired in both lists, `literal` is 0, and anything new
fails.

## The remaining 51 `expr`, and a target handed over from #4899

Still not statically provable, still needing reading rather than a fourth
automated pass.

But #4899 flagged a related gap that this bean's gate **cannot** see, and it is
worth recording here because it is the natural next target and the reasoning is
not obvious:

> `markov_trace_recursive.py` never called `set_compute_dps()`, so every `mpf`
> in it ran at the default 15 dps — the producer was float64 wearing 60 digits,
> and `mpf_context_dps_audit` reported the gated paths clean throughout.

A producer that **never raises its working precision at all** is invisible to
this gate, to the padding scan, and to the raw-float64 scan alike — because the
numbers it emits are *honestly* float64. There is no fake precision to detect
and no mpf built too early; the whole computation is simply low. What exposed it
was tightening a comparison until three assertions failed at digit 17 with
dyadic tails.

So the gate family has a blind spot shaped exactly like its own premise: every
member assumes precision was raised *somewhere* and asks whether a value got in
before it. None asks whether it was raised at all. A "producer never calls
set_compute_dps / mp.dps and emits a witness" check would be cheap and static,
and would be a genuinely new axis rather than a fourth variation.
