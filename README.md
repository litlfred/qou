# cat/cat-harness/fsh-guts

The kept trashcan of `qou`: deprecated or relocated material that is never rendered or published. It is a named-subgraph special branch, the same shape as the platform's own `cat/cat-harness/fsh-guts` (declared in folio-assistant `cat-harness/scripts/special-branches.json`).

- **Layout:** paths mirror the checkout (`fsh-guts/**`). The root `manifest.json` (`state-manifest/v1`, `keyedBy: tip`) is what makes this a state branch.
- **Contents at seed:**
  - `fsh-guts/` = qou `main`'s `fsh-guts/` tree (122 files).
  - `fsh-guts/deprecated/computations/` = `computations/_deprecated/` (1738 files).
  - `fsh-guts/deprecated/docs/audits/` = `docs/audits/_deprecated/` (66 files).
  - `fsh-guts/deprecated/qou-mass/src/qou_mass/data/` = `qou-mass/src/qou_mass/data/_deprecated/` (18 files).
  - Each file is byte-identical to main at seed commit 2a34fae18d.
- **Status: SEED.** `main` is still the source of truth. Nothing has been removed from `main`. Cut-over (removing these trees from `main` and re-pointing the live readers) is a separate, owner-approved step.
- **Writes:** spliced onto the tip and never force-pushed. This branch is never merged into `main`.

Owner, 2026-10-10: "_deprecated is now branch cat/cat-harness/fsh-guts (or should be. migrate if not)".
