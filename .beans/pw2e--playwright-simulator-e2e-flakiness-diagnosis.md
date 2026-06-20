---
# pw2e
title: 'Playwright simulator E2E flakiness — diagnose + patch + live-verify (folio-assistant)'
status: completed
type: task
priority: normal
tags:
    - folio-assistant
created_at: 2026-06-16T02:46:00Z
updated_at: 2026-06-16T03:35:00Z
parent: w5q7
---

Deferred "OOM/SIGTERM/Timeouts in tests/simulators.spec.ts" task. The harness
lives in the external litlfred/folio-assistant repo (gitignored in qou), so the
fix shipped as a patch + diagnosis doc in qou.

FINDINGS: the referenced spec was never committed (lost in the platform
migration — not in either repo's history); test-server.cjs was missing;
playwright.config.ts had anti-patterns (duplicate timeout key, fullyParallel
vs workers:1, no container launch flags); and the two WebGL sims reference an
unvendored three.min.js (real broken-asset bug). Root flakiness drivers:
small CI /dev/shm + no-GPU WebGL + networkidle waits against rAF loops.

DELIVERED (PR #2350, MERGED): docs/audits/2026-06-16-playwright-simulators-
flakiness-diagnosis.md + .patch (5 files) — disable-dev-shm-usage + SwiftShader
+ serial + domcontentloaded waits; dependency-free test-server.cjs;
reconstructed source-accurate serial spec; turnkey three.min.js vendoring
(three@0.149.0 devDep + scripts/vendor-three.cjs + pretest:e2e).

LIVE-VERIFIED (follow-up PR, branch claude/playwright-e2e-live-verify-2026-06-16):
7/7 tests pass in 6.8s against Chrome 149 (@sparticuz/chromium via npm/GitHub,
since cdn.playwright.dev is egress-blocked) — incl. all 3 WebGL tests and the
heaviest Quantum Brings scene; no OOM/SIGTERM/timeout. Added a
PLAYWRIGHT_CHROMIUM_PATH executablePath hook + an egress-restricted CI recipe.

Note: applying the patch + (optionally) committing simulators/three.min.js for
production is folio-assistant-repo work, out of this session's GitHub scope.
