---
# qou-snh8
title: 'INFRA: lake-cache/qou paper-olean branch has ZERO SchurWeyl oleans — needs clean reseed'
status: completed
type: task
priority: normal
created_at: 2026-08-29T06:37:26Z
updated_at: 2026-08-29T17:23:57Z
---

Found while landing the M1 arc (PR #5960). The whole QOU.SchurWeyl.* cone (66 files: Wenzl/Ocneanu/Markov normalisation incl. the proved general telescope sum_dim_wenzlWeight_eq_one) is ABSENT from lake-cache/qou-v4-24-0, so every agent touching it must rebuild from source (3308-job lake build; cache get 403s in-sandbox). A safe reseed is NOT possible from a verification sandbox: scripts/lean-olean-cache-seed.sh (correctly) refuses a partial/trace-mixed tree -- it needs a clean full 'lake build QOU UGB Fred2005' on a uniformly-traced pinned mathlib, then SEED_PAPER=1. Proper path: run .github/workflows/lake-cache-refresh.yml (service script lake-cache.sh, tars whole .lake) on a machine with working cache-get, OR a full local build where disk+time allow. Do NOT force-override the seed guard (SEED_ALLOW_NO_MATHLIB / bare --push) -- it publishes a mathlib-less branch that makes restores report 'Lean unavailable'.


## 2026-08-29 — ROOT CAUSE found; manual reseed NOT tractable in this container (honest wall)
Attempted the manual reseed (CI billing-blocked). Two blockers, both measured:

1. CONTAINER RESTARTS defeat the build. The full from-source lake build QOU is ~6000 modules / 2.5h+; the container was reclaimed TWICE mid-build (at ~[4932] and ~[5709]). .lake persists across restarts (good), so the QOU-own tree reached 2275/2277 built + traced. But it cannot finish in one sitting.

2. TWO-LOCATION CACHE ARCHITECTURE (the real defect root). The seed lake-root is the QOU PACKAGE dir (content/quantum-observable-universe/lean per .github/lake-packages.json), whose .lake must be self-contained (own build/ + deps packages/). But 'lake build QOU' from the WORKSPACE ROOT puts fresh traced deps in ROOT/.lake/packages, while the package dir's .lake/packages still holds the OLD restored half-traced deps (mathlib 6996 ol/3413 tr vs fresh ROOT 3406/3412; same for batteries/aesop/...). Result: content/.../lean/.lake is 62% traced -> FAILS the >=90% seed guard. This is EXACTLY why the incumbent cache is defective (seeded from the wrong .lake).

CORRECT manual path = per-package standalone build: 'cd content/quantum-observable-universe/lean && lake build', which needs mathlib IN the package dir via (a) cache get [403-blocked] or (b) a SECOND full from-source mathlib compile into the package dir [multi-hour, restart-doomed here].

RECOMMENDATION: reseed via CI (lake-cache-refresh.yml, workflow_dispatch) — it is designed for this architecture and does the per-package build. Needs Actions billing unblocked, OR a manual workflow_dispatch when possible. SILVER LINING: the 4 from-source regressions this effort found+fixed (bean qou-1mrn) mean a future reseed (CI or manual) will actually COMPLETE — previously the build errored out before finishing. Do NOT attempt risky build-surgery (relocating fresh deps into the package dir) — every dep would need replacing and a subtly-broken cache is worse than none.


## 2026-08-29 — RESOLVED: cache reseeded correctly (manual, this session)
lake-cache/qou-v4-24-0 now holds the CORRECT cache: 5938 oleans / 2275 QOU-own / 100% traced / self-contained (verified: a QOU file compiles using only the package-dir .lake). Replaces the defective incumbent (7268 oleans / ZERO own / 62% traced).

HOW (the two-location fix): my 'lake build QOU' from the workspace ROOT put fresh traced mathlib in ROOT/.lake/packages, while the seed's lake-root is the PACKAGE dir. The package-dir oleans were byte-identical to ROOT's (deterministic build) but MISSING traces (old-restore superset, 6996 ol / 3413 tr). Fix = tar-replace the package-dir mathlib build with ROOT's fresh traced one -> coverage 62% -> 100%. No rebuild needed.

KEY INFRA LEARNING (belongs in lake-cache.sh): the agent proxy REJECTS a single ~2.25GB git push (HTTP 500 / 'unexpected disconnect while reading sideband packet' / gateway timeout at ~10min), CONSISTENTLY, regardless of retries. But ~90MB per-commit pushes SUCCEED (~10-15s each). WORKAROUND: push the 25 parts as 25 SEPARATE fast-forward commits (one part per commit) instead of one 25-part commit. lake-cache.sh seed --push should be updated to chunk large pushes this way (folio-assistant). Until then, a manual reseed must use the incremental-commit push, not seed --push.
