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
2. ~~**`q0_anchor_ratchet.py` self-perturbs**~~ — **RETRACTED, this was my
   error.** Re-measured on a genuinely clean tree, three consecutive runs give
   `NEW=39` every time and dirty **zero** files. The script writes nothing on
   its read path (`BASELINE.write_text` is reached only under `--rebaseline`;
   the other writes are its self-test's tmpdir), and it **already excludes**
   audit-emitted witnesses — it imports `AUDIT_SUFFIXES` from
   `q0_anchor_consistency_audit` and filters on them at `_is_in_scope`.

   The `153 → 154` I reported came from the same contaminated sequence as the
   retracted `1748 vs 1630` figure: the tree was dirty with witnesses my own
   probe runs had rewritten, and I was checking out `origin/main --
   computations` between measurements. I retracted the pair and kept the
   mechanism, which was not independently checked. I had also conflated two
   scripts — `q0_anchor_consistency_audit.py` **does** write a witness via
   `WitnessBuilder`, but that witness ends in `-audit.witness.json` and is
   excluded by the very convention above.

   **The general lesson survives and is the one to keep: never measure a gate
   on a tree your own runs have written to.** It is just not what this
   particular gate does. #6453 spent three verification runs answering the
   false version of this question.
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


---

## Continuation: the raw-float64 ratchet + float64-cap drain (PR #7318, 2026-09-14)

Same audit family, adjacent tier. Recorded here rather than in a new ledger
because the findings below bear directly on this ledger's own acceptance
criterion.

### Scope map — every sibling is `(none, independent, none)`

Measured by diff, not by title, across the nine open sibling PRs plus this
ledger's own branch. "ratchet surface" = `raw-float64-baseline` /
`float64-padding-baseline` / either audit witness / `precision-gates.sh`.

| branch | ratchet surface | `computations/` files | file overlap with #7318 |
|---|---:|---:|---|
| genus-completeness-observable-target | 0 | 6 | none |
| hjf4-demote-and-pole-vertex | 0 | 0 | none |
| dead-prop-fields-and-name-collision | 0 | 0 | none |
| cds1-ladder-bounded-by-cos | 0 | 6 | none |
| rev-run-and-edge-closed-form | 0 | 6 | none |
| gifted-feynman-fhjzwv | 0 | 2 | none |
| reading3-budget-unconstrained | 0 | 4 | none |
| d2-convention-d-ck-rederivation | 0 | 4 | none |
| magic-numbers-bring-duplicate | 0 | 0 | none |
| cheat-sheet-derivation-gaps-0ykco4 | 0 | 21 | `casimir_macdonald_probe.py` + witness — **already on `main`** |

Per the skill's rule (`(none, independent, none)` needs no comment), **no
intent comments were posted on any sibling**. The one overlap is additive and
already landed: that branch drained macdonald's *serializer* and left the
*cap*, which #7318 fixes — `git diff origin/main <branch> -- <that file>` is
empty.

**The one cross-PR dependency worth checking was measured and is clean.** Five
siblings add **10 new witnesses**; a dirty one would land as ratchet `NEW` on
#7318 and force an attribution. All 10 carry **0** raw floats.

**§2-bis does not bind #7318.** The appendix
`content/quantum-observable-universe/appendix-mass-binding-algorithms/` (89
files) references **none** of the 24 producers it touches — verified against a
positive control (`binding_canonical.py`, `canonical_mass.py`,
`lp_dual_solver.py` *are* referenced there). The changes alter no algorithm,
script path or witness path.

### This ledger's acceptance criterion is SOUND — I nearly filed against it

Seeing `LAUNDERED — none.` with three live `mp.mpf(str(Q))` sites in the
casimir family, I took it for a detector blind spot and was one step from
filing it against bean `qou-tj98` (`completed`) and this ledger.

**The audit is correct.** Those three imported `from q_parameter import Q_MP
as Q`, so the local `Q` was already the mpf and there was no f64 to launder;
`f64_into_mpmath_audit.py` tracks the import `asname` and reporting nothing is
the right answer. `"Q"` *is* in its `F64_NAMES` and its self-test at line 621
asserts the `mp.mpf(str(...))` form, so neither the attributed call nor the
name was the issue — the binding was. **The audit reads bindings; grep reads
spellings.** Taxonomy row 46.

### Independent confirmation of this ledger's class-(a) figure

This ledger records class (a) as carrying **6.8395e-18**. Re-measured
independently today from `Q_MP` rather than from a sweep: `mpf(str(Q))` sits
**6.839e-18** from the true pin, against **2.725e-17** for `mpf(Q)` — the
two spellings are **4x apart** and are not interchangeable defects.

### Findings this drain adds

- **A clean raw-float64 count is evidence about the RECORDED value, not about
  the computation.** `casimir-macdonald-probe` read 0 on the ratchet while its
  producer computed from a double; the fix moved 183 of 405 fields. Taxonomy
  row 47.
- **Rank off disk, never off the baseline.** Macdonald's baseline says 196 and
  its live count was 0 — baselines never move down by design, and I mis-ranked
  the family's largest target off one.
- **The two ratchets are not redundant.** A `float()` → `fmt()` change drains
  the raw ratchet *by construction*; whether that is a drain or a relabelling
  depends on how the value entered. On `casimir_epsilon_vacuum` the padding
  ratchet caught 9 NEW hits and exposed a producer running at `mp.dps = 15`.
- **`never_raises_dps_audit.py` cannot see a file that never NAMES mpmath**
  (its mpf arrives by import) — 5 live files, bean `qou-0p2h`.
