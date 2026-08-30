---
# qou-ckbv
title: 'DEFECT: 26 hyperbolic-volume literals wrong or over-claiming precision (corpus-wide)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:33:05Z
updated_at: 2026-08-30T12:55:00Z
---

## Measured, not estimated

`computations/hyperbolic_volume_literal_audit.py` (added in PR #5407) checks
every hand-typed hyperbolic volume against SnapPy. First run, 2026-08-21, on
114 literals:

    WRONG          2   disagree within the digits they print
    OVER_CLAIMED  24   print materially more digits than are correct
    OK            50
    UNRECOGNISED  38   not matched to a census manifold -- NOT a pass

### WRONG (2) -- fix first

`VOL_6_2 = 4.40083298054544839393`, annotated "SnapPy census", in

  - computations/vol_density_deuteron_perknot_probe.py:39
  - computations/per_knot_density_deuteron_perknot_probe.py:39

True value `4.40083251612304610144`. Wrong at digit 9 (1.06e-7 relative),
while printing 21. The corpus already holds the CORRECT 6_2 value at
`probes/gap_a4_T2_per_knot_vol_probe.py:72`, so this is a transcription, not
a disagreement about the manifold. Both are deuteron per-knot density probes,
so the wrong value is upstream of a per-knot density number.

### OVER_CLAIMED (24) -- one bad string, copy-pasted

Eight files carry the SAME Vol(4_1) literal, printing 53 digits and correct
to 20:

    lit    2.0298832128193072500 115978049904475264466050157561096
    exact  2.0298832128193072500 42405108549040571883378615060599584

33 fabricated digits. Sites: canonical_lepton_braid_words.py:201,
q_beta_complex_q_test1_phaseA{,_v2}.py, t6_lepton_h3_3channel_convention.py:46,
xi_ell_phi_q_probe.py:158, f_ell_derivation_via_per_braid_mass_tower.py:64,
lepton_tower_probe_1_cinquefoil_muon.py:54, t6_three_halves_factor_probes.py:43,
per_generator_V_hat_general.py:162 (+ truncations of the same string in
whitehead_kashaev_volume.py:72, figure_eight_kashaev_volume.py:38,
whitehead_c0_mpmath.py:38).

A second cluster of five in `computations/qbeta/qbeta_c3_*` prints 36, correct
to 17.

**Vol(4_1) needs no literal at all** -- it is `2*Cl_2(pi/3)`, i.e.
`2*mp.clsin(2, mp.pi/3)`, which `qou_substrate.constants.vol_4_1_at()` already
computes. The drain for this cluster is deletion, not re-transcription.

### Why SnapPy is the reference

Measured: `snappy.Manifold("4_1").volume(bits_prec=500)` agrees with
`2*mp.clsin(2, mp.pi/3)` to 55 digits, relative error exactly 0. So
"correct to N digits" above is a statement about the literal, not about
SnapPy's resolution.

## Scope note -- why this was NOT drained in PR #5407

That PR fixed the three files it was already touching (the qou-substrate
constant, the rd4 search table, the 6_1 kappa-series constant) and added the
audit. The remaining 26 sites are spread across probes whose CONCLUSIONS may
move when the constant changes -- e.g. the two 6_2 sites feed a per-knot
density. Each needs its producer re-run and its witness regenerated, and a
few are long-compute. That is a separate, careful pass, not an idle-drain.

## Suggested order

1. The 2 WRONG 6_2 sites (real error at 1e-7, feeds a density).
2. The 8-file Vol(4_1) cluster -- replace with the closed form, one commit.
3. The 5 qbeta_c3_* sites -- same closed form.
4. The remaining singletons.
5. Triage the 38 UNRECOGNISED (VOL_PHASE4_Z1/Z2 = 12.776/12.554,
   VOL_HYP_D, PRE_REGISTERED_VOL4 = 8.048, VOL_7_SQ_1, VOL_BRINGS): decide
   per name whether it is a census volume that the audit should learn, or a
   derived quantity that should be excluded by name.

Gate: `python3 computations/hyperbolic_volume_literal_audit.py --strict`
exits 1 while any WRONG or OVER_CLAIMED remains. Requires snappy
(`pip install snappy`); exits 77 without it, deliberately NOT 0.


---

## Update 2026-08-21 — the 2 WRONG are FIXED (PR #5407); 24 OVER_CLAIMED remain

`VOL_6_2 = 4.40083298054544839393` corrected to the census value in both
deuteron per-knot density probes. Audit now reports **WRONG 0**. The
remaining scope of this bean is the 24 OVER_CLAIMED plus the 38
UNRECOGNISED triage.

## Two adjacent findings, opened by this work

### A. Half-applied rename broke 4 modules (FIXED in #5407)

`a4d9906659` migrated "VolDensity" -> "PerKnotDensity" across callers but
never renamed the functions in `_li_2_q_util`. Measured by AST over every
`from _li_2_q_util import` in the tree: 4 modules raised ImportError at
import time on main, from 2 missing names.

Repaired by aliasing (`per_knot_density_per_block = vol_density_per_block`,
same for `_borromean`) rather than renaming -- 71 sites still use the
`vol_density_*` spelling, so flipping the canonical name risks a second
partial pass. **Open question for the owner, NOT decided:** which spelling
should ultimately be canonical? AGENTS.md's mass-formula banner says
`vol_density_per_block` "stays valid for binding ratios only", which reads
like the migration was intentional and unfinished.

### B. An unanchored witness, not committed

`probes/per_knot_density_borromean_q_locality_probe.py` had not run since
that rename landed -- its witness has NEVER existed in the repo. With the
aliases in place it runs and emits, but the emitted witness is hand-rolled
rather than built by `WitnessBuilder`: no `q0Anchor`, no `q0Value`, no
`assertions`. It was deliberately NOT committed, because adding an
unanchored witness is the class of defect this arc drains.

Follow-up: port that probe to `WitnessBuilder`, declare it in
`q0_anchor_manifest.json`, then commit its witness. Check whether the other
three repaired modules have the same shape before committing anything they
emit.


---

## `--n12`: unrecorded parameter provenance, demonstrated a second time

Regenerating `whitehead-c0-mpmath.witness.json` after the Vol(4_1) fix
produced a diff FAR larger than a digit-21 correction, and one part of it was
a **lost data point**:

    committed   "10": 7062.35924065477,  "12": 29287.27767465885
    fresh run   "10": 7062.35924065477
    factor      1.9678009716166576  ->  1.8973391741766672

The producer gates N=12 behind an opt-in flag:

    EXTEND_N12 = "--n12" in sys.argv        # line 47

The committed witness contains N=12, so it was generated WITH `--n12` -- and
nothing in the witness records that. A plain re-run silently drops the point
and moves the headline `factor` by 3.6%. The verdict survives ("nearest
prediction: FACTOR 2; excludes factor 1 & 4: YES"), but only by luck.

This is exactly the class `tools/hecke-engine/src/provenance.rs` documents --
*"The parameters were not recorded at all ... none of them wrote it down"* --
now demonstrated on a Python producer as well as the Rust ones. Worth
generalising: **before regenerating any witness, check whether its producer
has argv-gated behaviour, because the witness will not tell you.**

Re-running with `--n12` to produce a comparable artifact.

Other pre-existing drift in the same diff (field renames
`whitehead_c0_run` -> `whitehead_c0_mpmath`,
`figure_eight_reference_c0_Nge8` -> `_c0_2term`, a dropped
`whitehead_c0_fits` block) confirms the committed witness predates a
substantial producer rewrite, independently of the flag.

## Method note: a monitoring bug I reported from

I watched that compute with a background waiter:

    until ! pgrep -f whitehead_c0_mpmath; do sleep 10; done

`pgrep -f` matches full command lines, so **the waiter matched itself** and
could never terminate. It reported "[still running]" indefinitely, and I
repeated that in a status update after the process had in fact exited. Caught
by `ps -eo pid,etime,args`, which showed no such process at all.

Use a pattern that cannot match the watcher (a pidfile, `$!`, or
`pgrep -f "script.py --flag"` checked with `ps`), and prefer confirming
"finished" from the artifact or the log's own completion line rather than
from process absence.

---

## 2026-08-30 — the audit was reporting a clean corpus because it could not see

Claimed this bean and re-ran its own gate. It said **WRONG 0, OVER_CLAIMED 0**.
That was false, and the reason is the interesting part.

### Why the gate was green

`hyperbolic_volume_literal_audit.py` asked three questions in a row, every one
of them answered by the variable's **name**:

1. `grep -E '= *(mp\.)?mpf\("[0-9]'` — the literal had to sit inside a literal
   `mpf(` call;
2. `if "VOL" not in name.upper(): continue`;
3. `resolve()` then needed a known knot key inside that name.

So it only ever checked constants that already followed the naming convention.
Everything named `v_6_2` or `_SNAPPY_HP_50` was invisible — not correct,
**unexamined**. A detector whose recall depends on the author having named
things well cannot find what a careless author wrote.

It also read line by line, so implicit string concatenation
(`mpf("4.4008…" "5458…")`) showed it only the first fragment, understating
every printed width in the PSLQ basis.

### What was actually wrong

| site | what it held | good digits |
|---|---|---|
| `substrate/knot_volumes.py` `_vol_8_11` | 20 real digits + **30 fabricated zeros**, in a variable named `_SNAPPY_HP_50` | 20 / 50 claimed |
| `tier_1_hyperbolic_3braid_pslq.py` | **all eight** basis volumes | 2–13 of 32–96 printed |
| `tier_2_hyperbolic_bridge3_pslq.py` | same eight, copied | 2–13 |
| `tier_2` `TIER2_LITERATURE` | six "KnotInfo ~15 dps" values | **0–6**; four wrong at digit 1 |
| `m_tau_knot_prediction.py` `KNOT_VOL_TABLE` | 21 of 25 hyperbolic entries, under "All values verified to 8+ dps" | 1–11 of 20 |

Six of the eight PSLQ literals match **no manifold in SnapPy's censuses**
(searched 200,067), so they were corrupted numbers, not correct volumes under
wrong labels. Two entries in the m_tau table *were* mislabels: `L5a1` held
Vol(9_42) while the same table's `Whitehead` entry — the same manifold — was
correct; and `9_46` held Vol(9_42) under the comment "cosmetic surgery with
9_42", which is false (4.0569 vs 4.7517). That comment is what made a wrong
entry look deliberate.

### The consequence that matters most

PSLQ searches for an integer relation among its basis. Fed noise past digit
2–13 at `mp.dps = 100`, it reports a relation among wrong numbers. Both Tier-1
and Tier-2 publish a **negative** ("no small relation"), and a negative is what
a corrupted basis produces whether or not the true basis has one — the finding
could not have failed for the reason it claimed.

Re-run after correction: **both negatives survive**, with no assertion flips.
So the conclusions stand — but they now mean something, which they did not
before.

`TIER2_LITERATURE` is the fallback taken exactly when SnapPy is *absent*, i.e.
in the pipeline image it exists to serve. Wrong at the first digit, it did not
degrade gracefully; it silently substituted noise. Both paths now agree to
50 dps, so the result no longer depends on whether SnapPy happens to be
installed — which it previously did, at the first significant digit.

### Fixed

- `_vol_8_11` → SnapPy 50-dps. f64 view is **bit-identical**, so f64 consumers
  are unaffected and only mpf consumers move — which is where the error was
  real. Vendor mirror re-synced.
- Both PSLQ bases → 100-dps values matching `mp.dps`, each confirmed against a
  **randomized re-triangulation** of the same manifold (volume is a topological
  invariant, so that is a genuine second route, not a re-read). Method
  controlled on the two volumes with closed forms: SnapPy agrees with
  2·Cl₂(π/3) to 4.5e-64 and 8·G to 2.6e-65.
- `KNOT_VOL_TABLE` → 21 entries corrected, each printing only the digits it is
  good for; the false "cosmetic surgery" comment removed.
- The audit rewritten to identify by **name OR value**, parsing with `ast` so
  concatenation and non-`mpf(` idioms are caught. Both routes are needed:
  `v_7_4` was off at the second digit (7.6e-3), which no value-matcher can
  recognise — only the name knows; `_SNAPPY_HP_50` is a precision tag, not a
  knot — only the value knows. New `MISLABELLED` verdict for name/value
  disagreement, and `--strict` now fails on it.

Audit on the same corpus: **0 → 14 WRONG** surfaced, then **14 → 4** after the
fixes above.

### Still open

- 4 WRONG (`binding_ladder_catalog.py` ×2, `tau_amphichiral_sdp_probe.py`,
  `fivetwo_stokes_matrix_zq.py`) — all "prints 15, good 9–11", f64-grade
  values in probe tables. Small, but they print more than they have.
- 12 OVER_CLAIMED, incl. six `VOL_4_1_STR` sites at 29 printed / 19 good — the
  qou-f8lit 20-digit carrier again, and `Vol(4_1)` needs no literal at all
  (`2*clsin(2, pi/3)`).
- 38 UNRECOGNISED triage (item 5 of the original suggested order) — untouched.
- `m_tau_knot_prediction` witness not regenerated in this pass.

### Environment note

snappy is **not** in this container by default; `pip install snappy` was needed
and did not survive a mid-session container restart. The gate exits 77 without
it, so in CI this audit is skipped, not passed — worth confirming the pipeline
image actually carries it, or this hardening buys nothing there.
