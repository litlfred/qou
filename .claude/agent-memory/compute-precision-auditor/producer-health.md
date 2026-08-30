# producer-health — how to run a `computations/` producer and judge the result

Detail split out of `MEMORY.md` (which is injected into the system prompt and
is capped at 200 lines / 25 KB). Read this file when you are about to run
producers in bulk, or when one appears to be broken.

## TRAP — a non-zero exit is not a defect, and a traceback is not either

Established 2026-08-24, after "14 crash" was corrected to **2**:

- **4 exit non-zero BY DESIGN** and explain themselves on **stdout**, which
  a stderr-only harness never sees. `low_isotope_mass_table` refuses when
  precision would fall below `target_dps`; `qbeta_braid_nf_sdp_offset_probe`
  refuses because `mp.lu_solve` would *not* raise and running would "publish
  laundered numbers". Two more write their witness successfully and *then*
  exit non-zero.
- **1 raises its guard instead of exiting** — `qbeta_habiro_phase5q_dn` dies
  on `AmDifferenceInvalid`, a `ValueError` subclass defined for exactly
  this. The discriminator is whether the exception type is one the
  producer's own cone defines.

A producer-runner must do all seven or its verdicts are about itself: set
`PYTHONPATH`; skip scripts declaring required positionals; clean the tree
**before** each run as well as after; try both `cwd=<producer dir>` and
`cwd=<repo root>` (some paths are repo-root-relative); capture **stdout** as
well as stderr; check for a **traceback** rather than trusting the exit
code; then check whether that traceback's type is a guard the corpus
defines.

## TRAP — setting `PYTHONPATH` MASKS a whole defect class

Requirement one above is necessary for the runner and is exactly what hides
a script whose `import _path_bridge` precedes the `sys.path` bootstrap that
resolves it. Same file, same commit, varying only the environment: without
`PYTHONPATH`, `ModuleNotFoundError: No module named '_path_bridge'`; with
it, 4/4 checks pass. **Six such scripts were live on `main`** — including
`qbeta_d_frame_trace_baseline_probe`, whose `gap_over_ladder_ratio =
92.1058` the Δ fork-pricing probe calibrates against — and none appears in
the "2 real defects" list, because the runner that produced it set
`PYTHONPATH` by its own rule.

So read that 2 as *"2 that survive a PYTHONPATH-equipped runner"*, not as
*"2 that a user can run"*. Guard:
`computations/audits/path_bridge_bootstrap_audit.py`, which narrows by
pattern but **decides by executing each candidate with `PYTHONPATH`
stripped**. Its own count was 28 before correction to 6: the first pass
matched only `sys.path.insert(` and missed `sys.path[:0] = [...]` — 22 false
positives from one unknown spelling. Bean `qou-0e1t`.

