---
# qou-78bm
title: 'GAP: the qou-mass vendor mirror has RE-DRIFTED (7 modules, 2026-09-26) — qou-hp3g''s drain does not hold, because nothing blocks on --check'
status: todo
type: task
priority: normal
created_at: 2026-09-26T21:22:59Z
updated_at: 2026-09-27T17:00:17Z
parent: qou-weeq
---


## Measured 2026-09-26 on `main` `4bca933828`, while doing PR #7471

`python3 scripts/sync-qou-mass-vendor.py --check` is **RED**. `--apply` rewrites **7**
`qou-mass/src/qou_mass/_internal/` modules that no branch touched:

    canonical_trm_reference   closed_form_tau_M        codata_2022_source
    experimental_constants    mass_at_3A_proper        wedderburn_jones_markov
    y_lambda_wenzl_bridge

plus it creates an untracked `qou-mass/src/qou_mass/binding-canonical.witness.json`.

**These are real source changes the mirror never picked up, not noise.** Sampled two:

- `y_lambda_wenzl_bridge` — the source gained `-> mp.mpf` on
  `y_lambda_wenzl_bridge_numeric`, and its own added comment says the annotation
  **feeds a gate**: *"`mpf_mixed_arithmetic_audit.py` builds a registry of corpus
  functions from …"*. So the mirror is behind on something a gate reads.
- `closed_form_tau_M` — an inlined `mp.mpf(str(...))` concatenation replaced by a named
  helper.

**Why this is a NEW bean and not a reopen.** `qou-hp3g` is **completed** and correctly so —
it measured *"1 missing + 9 drifted"* on 2026-08-21 and drained it. The finding here is the
**recurrence**: five weeks later the mirror is drifted again, by 7, with no branch having
hand-edited it. So the drain is not the fix; the mirror re-drifts the moment
`computations/` moves, which is continuously. `qou-cdj8` covers what `--check` *sees*
(42 `.py`, ignoring 157); this bean is about **nothing blocking on what it already sees**.

**The actual question, and it is an owner call.** `--check` is described in AGENTS.md as
"the gate", and it is a gate nobody invokes: it is not in a commit hook, and CI is
`workflow_dispatch`-only repo-wide, so a drifted mirror reaches `main` unremarked. Options,
none started:

1. **Leave it and drain periodically.** Cost: nothing now; the drift recurs, and each drain
   is a large mechanical diff. Risk: a stale mirror silently diverges from a source a gate
   reads (already true of `y_lambda_wenzl_bridge`). This is the status quo and the default.
2. **Add `--check` to the warn-only pre-commit hook** beside
   `precommit-precision-warn.sh`. Cost: one line plus the runtime. Risk: low — the existing
   hook is warn-only by design because a bare container lacks `mpmath`/`numpy`, and the same
   reasoning applies. Commits to `qou-mass` or `computations/` would print the drift.
3. **Stop vendoring and import from `computations/`.** Cost: large, and `qou-mass` is the
   external-researcher facade, so it presumably vendors deliberately. Forecloses the
   facade's independence. Not recommended without knowing why vendoring was chosen.

**Recommendation (my judgement, not a finding): option 2.** It makes the gate visible at the
moment the drift is created, at the cost of one hook line, and it does not require deciding
anything about vendoring. Option 1 is safe and is what happens if nothing is done.

**Why it is not fixed in #7471.** That PR is a citation-correction tranche. `--apply`
regenerates all 51 modules at once, so fixing my one module swept all 7 in; I reverted them
and left `--check` red exactly as it was, because carrying another arc's mechanical drain
inside a prose PR is scope-widening. **`wedderburn_jones_markov` is in that PR's own arc
cone**, which is why I looked rather than ignoring it.


## 2026-09-27 — DRAINED. 7 drifted + 1 missing; exactly 7 files moved.

Commit 5c6ed636b6 on claude/two-row-count-eq-dimhlf-2026-09-27 (PR #7481), its own
scoped commit so it can be reverted alone. Bean stays open (rule 13a) -- see bottom.

  BEFORE  MISSING 1: binding-canonical.witness.json
          DRIFTED 7: canonical_trm_reference, closed_form_tau_M, codata_2022_source,
                     experimental_constants, mass_at_3A_proper,
                     wedderburn_jones_markov, y_lambda_wenzl_bridge
  AFTER   "vendored copies are in sync (51 modules, 26 witness JSON,
           122 package-data witness JSON)"

### The bean's own warning, measured

This bean warns `--apply` regenerates ALL 51 modules and so sweeps in pre-existing
drift. Measured: exactly SEVEN files moved -- the seven named -- plus the one missing
witness added. The other 44 were already in sync and are byte-unchanged. So the
warning is about the MECHANISM, not about a realised blast radius here.

### No number moves

The mirror is a generated copy of `computations/` into a package that is NOT published
(PyPI 404, no dist/, no publish step) with 5 in-repo importers. Two spot-checks confirm
the regenerated copies ARE their sources: wedderburn_jones_markov 24369 B -> 24264 B,
closed_form_tau_M 28299 -> 28194, each with the source's tail verbatim in the mirror;
the ~105 B delta is the path bootstrap the vendoring strips.

Worth noting one drift was a live hazard rather than cosmetic: a `-> mp.mpf`
annotation that FEEDS a gate via `mpf_mixed_arithmetic_audit`.

`canonical_braid_marshalling` reads "not in cone" before AND after -- pre-existing,
untouched.

### WHY THIS BEAN STAYS OPEN

The drain is done; the RECURRENCE is the bean's subject and nothing here prevents it.
The mirror re-drifted once already, which is what this bean records. The standing
recommendation -- wire `sync-qou-mass-vendor.py --check` into the warn-only
pre-commit hook so drift is caught at the commit that causes it -- is UNTOUCHED and
is an owner decision (it changes a hook, not a number, so neither exemption applies).
