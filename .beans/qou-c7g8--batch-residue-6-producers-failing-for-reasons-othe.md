---
# qou-c7g8
title: 'Batch residue: 6 producers failing for reasons other than the qou_substrate stamp import'
status: in-progress
type: bug
priority: normal
created_at: 2026-08-30T15:52:44Z
updated_at: 2026-08-30T18:35:00Z
---

Recorded so they are not lost. Measured in the `qou-j0nv` regeneration batch
(43 producers, serial, 600s cap). The 16 `qou_substrate` failures are
`qou-ya1e`; these are the rest, and they are **six distinct defects**, not one.

## The six

| producer | rc | time | symptom |
|---|---|---|---|
| `deltalambda/he4_binding_k_averaged_interface_probe.py` | 1 | 31s | non-zero exit, **no error text captured** by the batch's regex |
| `deltalambda/he4_binding_k_fingerprint_stage1_probe.py` | 124 | 600s | hit the cap — unknown whether slow or hung |
| `q0_migration_decompose.py` | 124 | 600s | hit the cap — same question |
| `probes/baldfn_theta_limit_probe.py` | 1 | 42s | `AssertionError: ('qt=2', 'reliable window too short', 0)` — a genuine assertion, not an environment fault |
| `qbeta/qbeta_counit_trace_transport_overshoot_probe.py` | 1 | 0s | `ModuleNotFoundError: codata_constants` — same SHAPE as qou-ya1e (missing path bridge) but a different module |
| `three_quark_borromean_lp_sweep.py` | 1 | 0s | `ModuleNotFoundError: matplotlib` — a genuinely absent third-party dependency, unrelated to the bridge |

## Notes

- The first one is a gap in my instrumentation, not necessarily in the producer:
  the batch captured `^[A-Za-z.]*(Error|Exception)` and this failure printed
  something that pattern missed. Re-run it alone and read the output.
- The two timeouts are NOT known to be hangs. `q0_migration_decompose` is a
  corpus-wide scan and may simply need more than 600s.
- `matplotlib` is a real dependency question: either install it, or the producer
  should degrade without plotting rather than fail to write its witness.

## Todo

- [ ] Re-run `he4_binding_k_averaged_interface_probe` alone and capture the real error.
- [ ] Time the two cap-hitters without a cap to separate "slow" from "hung".
- [ ] `baldfn_theta_limit_probe`: decide whether the assertion is a real
      regression or a threshold that no longer suits the data.
- [ ] `qbeta_counit_trace_transport_overshoot_probe`: fold into qou-ya1e's fix if
      that fix is "ensure the bridge is imported", since the cause is the same.
- [ ] `three_quark_borromean_lp_sweep`: install matplotlib or make it optional.

## 2026-08-30 — 2 of 6 closed, and neither was the defect it looked like

### 1. `he4_binding_k_averaged_interface_probe.py` — NOT A DEFECT

Ran it alone as the note suggested. It completes, writes its witness, and exits
**1** — because `allPassed: false`, not because anything threw. There was no
error text for the batch's `^[A-Za-z.]*(Error|Exception)` regex to capture
because there was never an exception. The failing assertion is honest science:

    label   "averaged interface improves on plain best (3.8% < 14.7%)"
    passed  false        rel Δ = 0.227913  vs plain best 0.147

**The instrumentation gap is real though**: a batch that classifies producers by
regex over stderr cannot distinguish "crashed" from "ran and reported a red
assertion". Those need different responses. Classify on exit code + presence of
a witness, not on stderr shape.

Re-running it was a strict gain: the committed witness (2026-08-23) carried NO
provenance at all, and the run added `scriptFile`, `scriptHash`,
`scriptCommitSha`, `commitSha`, `durationMs`, `q0Anchor: proton` and `q0Value`.
No science value moved (verified field-by-field).

Two loose ends, NOT fixed here (they are science/schema, not batch defects):
- the assertion uses `label`, with no `computed`/`expected` — a schema deviation
  from every other witness's `name`/`computed`/`expected`/`passed`;
- the verdict prose says "3.8%" and "96.2% captured" while the computed rel Δ is
  22.79% and the assertion compares 0.2279 against 0.147. Those disagree.

### 2. `qbeta_counit_trace_transport_overshoot_probe.py` — FIXED, exit 0

Not the same shape as qou-ya1e. The real cause was two lines hardcoding an
absolute path into a **different machine's checkout**:

    sys.path.insert(0, "/home/user/qou/computations")
    sys.path.insert(0, "/home/user/qou/computations/substrate")

This repo is at `/workspace/qou`, so both inserts resolved to nothing. Replaced
with `__file__`-relative paths. Now exits 0; witness diff is ephemeral only.

### The class behind it — 27 hardcoded `/home/user/qou` paths

Fixed 7 in 4 files (6 `sys.path.insert` + 1 Lean output path in
`gen_l6a4_angle_structure_lean.py`, which was writing to an unreachable
directory and dying with FileNotFoundError before emitting its file).

⚠️ My first count of "6 live" was WRONG — it filtered on `sys.path.insert`
alone and missed `sys.path[:0] = [...]`, `for _p in ("...",)` loops, and
`Path("/home/user/qou")` roots. **20 live occurrences across 12 files remain**,
beaned separately as a portability defect rather than refactored mid-bean.

### Still open here

- `he4_binding_k_fingerprint_stage1_probe.py` — 600s cap, slow-vs-hung unknown
- `q0_migration_decompose.py` — 600s cap, same question
- `baldfn_theta_limit_probe.py` — AssertionError ('qt=2', 'reliable window too
  short', 0), a genuine assertion
- `three_quark_borromean_lp_sweep.py` — matplotlib absent

### 3. `three_quark_borromean_lp_sweep.py` — FIXED, exit 0 without matplotlib

Took the bean's second option (degrade, don't install): an ephemeral container's
`pip install` helps nobody else, whereas the real defect is durable — a
module-level `import matplotlib` meant that on any machine without it the
producer died at IMPORT and never wrote its witness at all. An entire LP sweep
was lost because a PNG could not be drawn. The witness is the deliverable; the
plot is drawn FROM the sweep rows the witness already carries, never into them.

Import is now guarded, the plot block is conditional, and the witness records
`plot_rendered: false` + `plot_skipped_no_matplotlib` so a reader can tell "no
plot because matplotlib was absent" from "no plot because the run failed" —
otherwise the two are indistinguishable.

### ⚠️ Operational note for the whole campaign: this container has NEWER libs

Re-running the sweep moved LP duals at ~1e-11 (`-0.04063618418327389` ->
`-0.04063618417431147`). That is NOT nondeterminism: two consecutive runs here
are bit-identical (0 non-ephemeral differences). It is an ENVIRONMENT
difference — scipy 1.17.1 / numpy 2.4.6 now, versus whatever built the
2026-08-24 witness. The `c-knot` witness showed the same shape
(`engineVersion: mpmath 1.3.0 -> 1.4.1`).

**So any mass re-run of producers in this container will produce float64-level
churn across the corpus that has nothing to do with the change being made.**
Budget for it, and diff non-ephemeral values before attributing drift to a fix.
Raw-float64 count for this witness is unchanged (104 -> 104), so no ratchet
regression.

### 4. `baldfn_theta_limit_probe.py` — diagnosed; NOT precision, and NOT a regression

First, the framing in this bean was too generous: `baldfn-theta-limit.witness.json`
has **never been committed** (`git log --diff-filter=A` over all refs: empty).
This probe has never completed a run. So the AssertionError is not something
that broke — it is the probe's standing state.

The failure is in `block_b4`, per rung:

    assert j_rel >= 4, (r["label"], "reliable window too short", j_rel)
    AssertionError: ('qt=2', 'reliable window too short', 0)

`j_rel` is an ORDER-STABILITY window: coefficient `c_j` is retained only if
reconstructions of order `M = j+2 .. j+7` agree on it to 1e-6. `j_rel = 0` means
even `c_1` fails that test at qt=2.

#### The obvious explanation is RULED OUT

qt=2 is configured far below its siblings, which looked like the answer:

    rung       N     J    dps     B3 gauge
    qt=2       340   40   1500    1.58e-30
    qt=36/25   1000  48   6000    3.0e-66
    qt=6/5     1300  48   4000    7.55e-45

I raised qt=2 to qt=36/25's exact configuration and re-ran. The gauge improved
from `1.58e-30` to **`5.91e-126`** — 96 orders of magnitude — and `j_rel` was
**still 0**. So the reconstruction is order-unstable at qt=2 no matter how well
converged the input is. **This is structural, not numerical. Do not spend more
time on precision.** (Experiment reverted; the file is untouched.)

#### Where to look instead — qt=2 is a DEGENERATE point

The B3 line for qt=2 differs in kind from the others, not in quality:

    qt=2       C = 1.119076609   c1 = 1.119076609   SW 1.0        <- C == c1 exactly
    qt=36/25   C = 1.265767841   c1 = 2.876745094   SW 2.2727273
    qt=6/5     C = 1.381066535   c1 = 6.905332676   SW 5.0

At qt=2, `qt - 1 = 1`, so `c1 = C/(qt-1) = C` identically and SW collapses to
1.0. The B4 cross-check `c1_cross = |-cs[0]/(C/(qt-1)) - 1|` is therefore
degenerate there too. qt=2 looks like a boundary case of the reconstruction
basis, not a rung that needs more terms.

#### Structural defect, independent of the science

The assert is PER-RUNG but aborts the WHOLE probe. B1–B3 all succeeded and
their results were discarded, and no witness was written — the same shape as the
matplotlib defect fixed above: a late failure destroying earlier valid work.
Not fixed here because `block_b4` sets `r["cs"]`, `r["ginf"]`, `r["j_rel"]`
that `block_b4b` and `block_b5` consume, so skipping a rung is not a local
change and needs the probe owner's call on whether qt=2 belongs in B4 at all.

### 5. `q0_migration_decompose.py` — NOT HUNG. The 600s cap was simply too short.

Re-ran with a 2400s cap: completes, **EXIT=0**, total ~1802s.

    [1/2]  1800.3s  hadron_knot_table            FAIL(m=-9,p=-9)  TIMEOUT >900s
    [2/2]     2.0s  q0_anchor_consistency_audit  anchor+drift
    of 2: 1 moved by the ANCHOR, 1 also carried pre-existing DRIFT

It is a DRIVER that runs other producers under its own internal 900s per-producer
cap. `FAIL(m=-9,p=-9)` is the muon and proton runs each SIGKILLed at 900s —
2 × 900 = the 1800.3s wall. So no batch cap below ~1810s can ever let this
script finish, and the "timeout" told us nothing about this script at all: it
was reporting a nested producer's timeout.

**Instrumentation lesson, the second this bean has produced:** a driver's wall
time is the SUM of its children's caps. Capping a driver at 600s when it runs
two 900s children measures the harness, not the code. (The first lesson was
classifying failures by stderr regex — see item 1.)

### 🔴 The two open items are THE SAME PRODUCER

Re-running the nested audit surfaced that `hadron_knot_table` is also the
corpus's single remaining **Q0_FLIP**:

    hadron-knot-table.witness.json: anchor=muon but q0Value=1.10997859555733…
                                    (expected 1.109978595642…)

That is the retired vintage **A** carried under a `muon` label whose current pin
is **C** — the within-layer vintage straddle this campaign keeps finding, and
exactly what `q0Value` exists to catch. The witness is dated **2026-06-17**,
over two months stale.

So: the one producer whose timeout blocks `q0_migration_decompose` is the same
one whose stale pin blocks `q0_anchor_consistency_audit --strict`. It cannot be
repinned by re-running because it does not finish inside 900s. Whether it
finishes at all is being measured now (3000s cap).

### Audit witness refreshed properly

The nested driver ran `q0_anchor_consistency_audit` WITHOUT `--strict`, which
would have replaced a strict artifact with a weaker one. Re-ran it with
`--strict` so the witness records the stricter invocation. Counts are identical
either way — `--strict` gates only the exit code — and they show real progress:

    Q0_OK             1087 -> 1121   (+34)
    Q0_ANCHOR_MISSING 1629 -> 1601   (-28)
    Q0_INDEPENDENT      59 ->   67   (+8)
    Q0_AMBIGUOUS         3 ->    4   (+1, the c_knot stamp from this bean)

`--strict` now fails on exactly ONE thing: the single Q0_FLIP above.

(I briefly suspected `Q0_AMBIGUOUS_NO_REASON` 13 -> 14 was my c_knot stamp
missing its reason. It is not — that witness carries both `q0Anchor` and
`q0AnchorReason` at top level, verified. The +1 is a different witness.)

### 🔴 ROOT CAUSE CANDIDATE for the hadron timeout: `pyhecke_native` is STALE

The long hadron run emits this on every gram call:

    pyhecke_native is installed but DIVERGES from pyhecke.gram at q0
    (convention-D self-check failed). This is almost certainly a wheel built
    before the qou-m7py convention-D port (2026-08-15): its trace_weights
    still ends z^3 and/or Q_0 is the muon pin. REBUILD it --
    `bash scripts/build-pyhecke-native.sh` ... Refusing rather than silently
    returning divergent numbers.

So the compiled accelerator is refused (correctly — it is convention-C-era and
would return divergent numbers) and everything falls back to pure Python. That
is the obvious candidate for why `hadron_knot_table` cannot finish inside 900s,
and it would explain the timeout WITHOUT the producer being defective at all.

If so, one `bash scripts/build-pyhecke-native.sh` unblocks the whole knot:

    stale wheel -> native refused -> pure-Python fallback -> hadron_knot_table
    exceeds 900s -> q0_migration_decompose "times out" AND the corpus's single
    Q0_FLIP (hadron-knot-table.witness.json, retired pin A under a muon label,
    stale since 2026-06-17) cannot be repinned by re-running.

NOT rebuilt yet: a long hadron run is in flight and rebuilding a native
extension underneath it would invalidate the measurement. Rebuild after it
lands, then re-time.

⚠️ Note the wheel's staleness is ALSO a convention-C residue — "trace_weights
still ends z^3 and/or Q_0 is the muon pin" — so this sits on the excision
campaign as well, not only on this bean. And `per_channel_wenzl_level.py`
independently flags `pyhecke.gram` as "registry says C, code is D — registry
STALE", i.e. two separate signals that the pyhecke layer is out of step.
