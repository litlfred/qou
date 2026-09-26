---
# qou-78bm
title: 'GAP: the qou-mass vendor mirror has RE-DRIFTED (7 modules, 2026-09-26) — qou-hp3g''s drain does not hold, because nothing blocks on --check'
status: todo
type: task
created_at: 2026-09-26T21:22:59Z
updated_at: 2026-09-26T21:22:59Z
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
