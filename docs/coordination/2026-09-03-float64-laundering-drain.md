# Coordination — float64 laundering drain (`LAUNDERED` tier)

**Goal.** Drain the `LAUNDERED` tier of
[`computations/f64_into_mpmath_audit.py`](../../computations/f64_into_mpmath_audit.py)
— `mpf(str(<f64>))`, a float64 read as exact at a widened working
precision. Bean `qou-b7cf`.

## Scope map

| PR | branch | relationship | same-file collisions |
|---|---|---|---|
| **#6489** (this) | `claude/laundered-sweep-2026-09-03` | drains `LAUNDERED` on **producers** — 35 sites in `computations/probes` + `computations/qbeta`, plus `pyhecke.atom` / `hecke_core` | — |
| #6453 | `claude/ratchet-red-drain-2026-09-03` | **adjacent tier** — drains the raw-float64 ratchet on **witnesses** (5 files); same audit family, different tier | **none** (4 files in my scope dirs, 0 shared) |
| #6496 | `claude/cool-johnson-t1wveh` | **overlapping lane** — carries a float64-ratchet item (`qou-6sts`) among four unrelated drains | **none** (4 in scope dirs, 0 shared) |
| #6493 | `claude/four-body-mover-resolution-2026-09-03` | **adjacent question** — concludes "0 of 93 are environment drift"; I have an undetermined drift case | **none** (7 in scope dirs, 0 shared) |
| #6442 | `claude/wedderburn-weight-hook-inversion-2026-09-03` | thematic only — a documented weight diverging from the code, verdicts surviving; same *shape* as the stale-twin find, no scope overlap | none (0 in scope dirs) |

No sibling touches a file this PR touches, so there is no conflict risk in
either direction. Intent posted on #6453, #6496 and #6493; **not** on #6442
(pattern similarity is not scope overlap, and the skill's rule is not to
blanket-post).

## What the drain established

- **35 sites, three classes, only two of them defects.** Class (a) — 38
  expressions over 35 files reading `q_parameter.Q` (`_solve_q_proton_f64`)
  — carried **6.8395e-18** at a working precision of 25–65 dps; fixed with
  `q_at(mp.mp.dps)`. Class (c) — `D_PN` (**2.0087e-16**, from the float64
  `pyhecke.gram.q0`) and `build_nucleon_nf` (returns floats) — fixed.
- **Class (b) is NOT a defect: 21 sites, left alone.** `codata_constants`
  already holds `mpf` at prec=169 built from exact decimal literals, so
  `mpf(str(v)) - v` measures exactly `0.0`. A producer-side `_STR`-companion
  rewrite was planned for these and would have been pure churn.
- **`build_atom_nf` has no correct exact route** — its `Fraction` twin runs
  at the rational model `q = 111/100`, 1.93e-5 off the substrate, i.e.
  float-free and far worse. Those 2 sites stay float64 and say so.
- **0 verdict changes across 34 probes** run twice in one environment from a
  clean tree; exit codes identical (32/1/124, both failures pre-existing).

## Findings other sweeps should inherit

1. **A sweep keyed on "files I changed" cannot close a defect class.** The
   count was recorded as zero, then `precision-gates.sh --changed` found a
   35th site on `main` that the sweep list had never contained. Re-run the
   detector; the diff is not the population.
2. **`q0_anchor_ratchet.py` self-perturbs** — `NEW: 153` then `154` on two
   consecutive runs of an unchanged tree, because the run writes its own
   witness into its own scope.
3. **Probes write SIBLING witnesses.** A before/after sweep dirtied 32
   `*.witness.json` and mutated the tree it measured; restore
   `computations/` after every run.
4. **`git checkout <ref> -- <path>` STAGES.** A later `git add <unrelated>
   && git commit` swept 56 reverted `.py` files into a commit labelled for
   something else — invisible in the log, caught only because a re-run gave
   impossible results (16 of 17 probes "identical" for a change that moves
   q₀ from a float64 read to a 40-dps solve). Reverted in `5119c3dcea`.
5. **An additive `_mp` twin with no consumers will go stale silently.**
   `build_nucleon_nf_mp` drifted **2288 %** behind its float sibling after
   the 2026-08-30 gluon term while its docstring still advertised
   `1.4e-16`. A twin needs a *test* that fails on divergence, not a
   docstring recording a measurement nothing re-runs.

## Corrections made to my own claims

- **There is no anchor-manifest gate.** I twice told the owner the branch
  would land red without registering the 35 in `q0_anchor_manifest.json`.
  `q_parameter` selects muon only for stems in `ideal_muon` and otherwise
  falls through to proton; `Q0_ANCHOR_MISSING` is "a tolerated, visible
  state" per `witness.py`. Not registering.
- **The red precision gates are `main`'s, not this branch's** — proved, not
  measured: the ratchets read `*.witness.json`, and between merge base and
  HEAD exactly 4 witnesses differ, all byte-identical to `origin/main`'s.
  An earlier reading of 1748/153 vs 1630/39 was invalid (it compared my
  *base* to *current* main, and my "branch-only" file list was measuring
  output verbosity, not content).

## Open, filed not fixed

`pyhecke.gram.q0` is a float64 module constant; that file's own comment
records that 1027 of 1929 witness-writing producers reach it through
`pyhecke.atom`. Bean `qou-bfdb` — needs scoping, with finding 5 above as
the design caution.
