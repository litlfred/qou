---
# qou-rtg9
title: 'Stale-shard consumer audit: qou-mass was never published; the drift masked an upstream shim defect'
status: completed
type: task
priority: normal
created_at: 2026-08-15T03:29:57Z
updated_at: 2026-08-15T03:29:57Z
---

Audit asked: did anything consume qou-mass 0.1.0a1's convention-C traces during the 3 months the shard was stale?

ANSWER: NO, and my earlier framing was wrong.

1. qou-mass is NOT PUBLISHED. pypi.org/pypi/qou-mass/json -> HTTP 404 (qou-substrate likewise). No dist/, no git tags, no publish workflow. So there were never any external consumers, and my statement that 'anyone who pulled tr_M from the published package has numbers that disagree by up to 471%' was an overclaim -- retracted.

2. THE STALE SHARD HAD ZERO CONSUMERS. The only reader of canonical-mass-table-extended.witness.json inside the package is api.py, and nothing in-repo imports qou_mass.api. The computations/ scripts that grep-match the name read the IN-REPO witness, which was always correct (convention D since #4928).

3. AGENTS.md UNDERSTATES THE IMPORTER COUNT: it says '1 in-repo importer (the canonical wiring example)'. Actual: 5 -- jet_order_pivots, jet_algebraic_independence_probe, hecke/hecke_symbolic (all three importing _internal.markov_trace_recursive), tools/qou-substrate/tests/test_ephemeral_mask_sync (importing _internal.witness_base), plus the wiring example. Doc-currency defect.

4. Those importers use the VENDORED modules -- the ones that had rotted 14-of-14 -- so the real question was whether the drift changed math. For markov_trace_recursive the entire code-level drift was PATH PLUMBING (sys.path lines + the bridge preamble); no mathematical change. Those three scripts were never computing wrong traces.

## The find: the drift was MASKING an upstream defect

computations/substrate/witness_base.py is a shim re-exporting a HAND-LISTED set of private helpers from qou_substrate.witness. _EPHEMERAL_META_FIELDS was missing from that list, and `import *` does not pick up underscore names -- which is the whole reason the explicit block exists. So `from witness_base import _EPHEMERAL_META_FIELDS` was FAILING IN-REPO, on main, before I touched anything.

Nothing caught it because its one consumer, test_ephemeral_mask_sync.py, reads the name from the VENDORED mirror -- and that mirror was a stale copy of the pre-shim implementation, which still defined it directly. The test exists PRECISELY to detect mirror divergence, and it was green only because the mirror had not been updated. The drift was hiding the defect the test was written to find.

Generating the mirror made it faithful and the failure surfaced on the next run. Fixed at the source (added to the shim's re-export list, with the history recorded there); in-repo import works, mirror test 2 passed.

Verification: qou-mass 20 passed, ctype coverage PASS, sync --check in sync (42 modules).
