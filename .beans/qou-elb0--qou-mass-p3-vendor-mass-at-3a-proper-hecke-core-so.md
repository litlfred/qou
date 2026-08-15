---
# qou-elb0
title: 'qou-mass P3: vendor mass_at_3A_proper + hecke_core so canonical_braid has a live path'
status: completed
type: task
priority: normal
created_at: 2026-08-15T00:12:22Z
updated_at: 2026-08-15T00:53:30Z
---


## PARTIAL 2026-08-15 — vendoring is DONE and generated; the live path is blocked one layer up

Owner picked 'still do the full vendor'.

DONE:
* scripts/sync-qou-mass-vendor.py — computes the transitive cone from entry points (42 modules), copies flat, applies exactly two transforms (flatten substrate//hecke//markov/; drop the _path_bridge shim), and carries the 17 witness JSONs those modules load. --check/--apply/--list.
* All 42 modules + 17 witnesses synced. Package 6.1M -> 7.5M. Tests 19 passed / 1 skipped; predict() and canonical_braid() both verified working.

WHY A SCRIPT AND NOT 22 MORE HAND COPIES: measured first — 14 of 14 existing vendored modules had drifted (witness_base 815 lines, q_parameter 418, canonical_braid_crossings a whole generation). Inspected: the drift is pure rot, the vendored-only lines are older docstrings, no package-specific adaptation anywhere. So generation is safe AND the hand-copy approach is empirically 0-for-14. Hand-vendoring 22 more would have been indefensible.

TWO TRANSFORM BUGS FOUND BY TESTING, both worth recording:
1. Stripping only the single-line 'import _path_bridge' left the 4-line substrate preamble's 'del _sys, _Path, _bridge' referring to an unbound name — every substrate module died with NameError. The transform now drops _bridge from del lists too.
2. Witnesses cannot live under data/. The modules resolve Path(__file__).parent.parent, which inside the wheel is qou_mass/, so data/ FileNotFoundErrors. Sync writes them to the package root and pyproject's package-data was widened to match.

STILL BLOCKED — live canonical_braid(). Not a vendoring gap; two path assumptions in the UPSTREAM computations/ modules:
* the parent.parent witness convention above (worked around, not fixed);
* computations/substrate/codata_constants.py:187 builds _WITNESS_DIR.parent / 'qou-mass' / 'src' / 'qou_mass' / 'data' / 'ame2020.json' — the compute layer reaching INTO the package layer by repo-relative path. Vendored, that doubles to .../qou-mass/src/qou-mass/src/... This is a layering inversion and fixing it means giving those modules a package-aware resolver, i.e. editing computations/, not the vendor script.

So the vendor is complete and current; the live path needs a resolver change upstream. Recommend keeping canonical_braid() on the bundled shard until that lands.



## CLOSED 2026-08-15 — live path works; the blocker was ONE upstream layering inversion

Owner said go. The remaining blocker turned out to be a single real defect, not the two I had estimated:

* computations/substrate/codata_constants.py located ame2020.json as _WITNESS_DIR.parent / 'qou-mass' / 'src' / 'qou_mass' / 'data' -- the COMPUTE layer reaching into the PACKAGE layer that vendors it, by repo-relative path. In-repo it resolves; vendored, _WITNESS_DIR is qou_mass/ and the repo segment appears twice, so every AME lookup raised FileNotFoundError. Replaced with a layout candidate search that raises naming every path tried. In-repo resolution is byte-identical (verified: same file, same 4He entry).
* The parent.parent witness convention needed no code change after all -- placing vendored witnesses at the package root satisfies it, which the sync script already does and documents.
* qou_substrate turned out to be a genuine missing INSTALL DEP, not a path bug. Added with pyhecke to pyproject dependencies, with a comment that they are hard requirements of the live path (the vendored modules are shims that re-export from them), not accelerators.

RESULT: canonical_braid() computes live outside the shard's 8 rows. 7Li (not in the shard): 83 crossings, sigma 40 / sigma_inv 28 / averaged 14 / averaged_weighted 1. The shard is still tried FIRST on purpose -- it is the recorded artifact, so preferring it keeps answers reproducible against a published witness rather than varying with the installed dependency set.

test_canonical_braid_4he UN-SKIPPED. Suite is 20 passed, 0 skipped (was 19+1).

The live-path except is deliberately broad, and the comment says why: this session alone saw it fail as NameError (half-applied vendoring transform), FileNotFoundError (path convention) and ModuleNotFoundError (missing dep). A strand-count query should not become a crash for any of them.
