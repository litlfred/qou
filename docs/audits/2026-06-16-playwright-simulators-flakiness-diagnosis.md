# Playwright simulator E2E suite — flakiness diagnosis & fix plan

**Date:** 2026-06-16
**Session:** determined-hawking follow-up (`claude/amazing-galileo-ih3g4q`)
**Scope:** the deferred "OOM/SIGTERM/Timeouts in `tests/simulators.spec.ts`" task.
**Status:** root-caused; ready-to-apply patch produced and **live-verified —
7/7 tests pass against Chrome 149 with no OOM/SIGTERM** (see *Verification*).

> **Where the code lives.** The simulators and their Playwright harness are in
> the **`litlfred/folio-assistant`** repo, not `qou` (the platform was migrated
> out; `folio-assistant/` is gitignored here and wired in via
> `scripts/setup-folio-assistant.sh`). This session cannot push to
> folio-assistant, so the fix ships as a **patch file** in this repo:
> [`2026-06-16-playwright-simulators.patch`](2026-06-16-playwright-simulators.patch).
> Apply it in a folio-assistant checkout (see *How to apply*).

---

## TL;DR

The task assumed an existing flaky spec to repair. It does not exist: the
`tests/simulators.spec.ts` that `TEST_READY.md` claims was "implemented" was an
**uncommitted working-tree artifact lost in the platform migration** — it is in
neither repo's git history. What survived migration is a `playwright.config.ts`
that (a) references a `test-server.cjs` that **also doesn't exist**, (b) carries
several flakiness anti-patterns, and the two WebGL simulators reference a
**`three.min.js` that is not vendored anywhere** (a separate, real broken-asset
bug). The fix is therefore a *reconstruction*: a robust spec, a static server,
a corrected config, plus turnkey vendoring of `three.min.js` (the sims' missing
global build).

---

## How this surfaced

`TEST_READY.md` / `TEST_INFRA.md` (in qou root) document a 4-tier E2E plan and a
checklist that claims the suite was implemented and "fails correctly on the
current codebase." But:

| Expected file | Reality |
|---|---|
| `tests/simulators.spec.ts` | **Absent** from qou *and* folio-assistant; not in any branch's git history of either repo; no stash. |
| `test-server.cjs` (config `webServer.command`) | **Absent** — `playwright test` cannot even start the web server. |
| `playwright.config.ts` | Present in folio-assistant; committed. |
| `simulators/three.min.js` (referenced by 2 sims) | **Absent** — not tracked, no LFS, not in `.gitignore`, not in `node_modules`. |

The "deferred flakiness" was, in effect, the suite never reaching a committed,
runnable state before the migration carried the platform (minus the spec) to
folio-assistant.

---

## Root causes

1. **Spec never committed (lost in migration).** Must be reconstructed.
   The reconstruction asserts against **selectors/params read from the simulator
   source**, because the prose plan has drifted from the code:
   - beta-decay reads `shell` (not `showShellCorrection`);
   - the knot table has **no `signature` color option** (real options:
     `block, binding, alpha, spin, gm, alexander`);
   - `#sl-q` ranges clamp (beta `[1.005, 2.0]`, knot `[1.001, 2.0]`), so the
     plan's `q=0.95` would silently clamp — the spec uses in-range values.

2. **`test-server.cjs` missing.** The config's `webServer.command` is
   `node test-server.cjs`, but no such file exists ⇒ web-server startup fails ⇒
   every test errors before navigation. Added a zero-dependency Node static
   server (core `http`/`fs` only) rooted at the folio-assistant tree.

3. **`playwright.config.ts` anti-patterns:**
   - **Duplicate `timeout` key** — `120000` then `180000`; the second silently
     wins (JS object-literal shadowing). Collapsed to a single `120_000`.
   - **`fullyParallel: true` with `workers: 1`** — contradictory intent. Made
     `fullyParallel: false` to bound peak memory (one heavy page at a time).
   - **No container launch flags** beyond `--no-sandbox` (see #5).
   - **`retries: 0`** turned transient WebGL warm-up hiccups into hard failures;
     now `process.env.CI ? 2 : 0`.

4. **`three.min.js` not vendored (real bug, distinct from flakiness).**
   `brings_surface.html` and `quantum_brings_surface.html` both
   `<script src="./three.min.js">`, using the global `THREE.*` API (40 and 104
   references). With the asset absent, both pages throw `THREE is not defined`
   on load — so the WebGL tests **cannot pass** regardless of stability work.
   Remediation below; the spec **guards** on the asset so a fresh clone *skips*
   (stable) rather than *fails red* (flaky).

5. **OOM / SIGTERM / Timeout drivers** (the original symptom):
   - **Small `/dev/shm` in CI containers** (Docker default 64 MB). Headless
     Chromium puts shared memory there; heavy WebGL overflows it and the
     renderer/GPU process is killed → **SIGTERM/SIGBUS**. *(This sandbox has a
     7.9 GB `/dev/shm`, which is why the symptom is CI-specific.)* Fix:
     **`--disable-dev-shm-usage`** (spill to `/tmp`) — the single highest-impact
     change.
   - **No GPU in CI** → WebGL context creation can crash or throw. Fix: force
     software WebGL via **SwiftShader** (`--disable-gpu --use-gl=angle
     --use-angle=swiftshader --enable-unsafe-swiftshader`) so Three.js gets a
     real context instead of throwing.
   - **`networkidle` waits against `requestAnimationFrame` loops.** Every
     simulator runs a rAF render loop, so the page never reaches network-idle; a
     `networkidle` wait runs out the test timeout. The spec uses
     **`waitUntil: 'domcontentloaded'`** plus element/auto-retrying assertions.
   - **Concurrency.** Serial execution (`fullyParallel:false`, `workers:1`,
     `test.describe.configure({ mode: 'serial' })`) keeps only one heavy scene
     resident.

---

## The fix

Three files (patch: `2026-06-16-playwright-simulators.patch`):

| File | Change |
|---|---|
| `playwright.config.ts` | dedupe `timeout`; `fullyParallel:false`; CI retries; container launch flags (`--disable-dev-shm-usage` + SwiftShader); `actionTimeout`/`navigationTimeout`; `webServer.url` health check on `simulators/empty.html`; optional `PLAYWRIGHT_CHROMIUM_PATH` executablePath hook for egress-restricted CI. |
| `test-server.cjs` | **new** — dependency-free static server on `127.0.0.1:8080`, traversal-guarded, clean SIGTERM/SIGINT shutdown. |
| `tests/simulators.spec.ts` | **new** — serial Tier-1 suite (7 tests): load + URL-param parsing for the 2D sims (beta-decay `q`+`shell`, knot `q`+`color`), WebGL load/parse for the Brings sims guarded behind a `three.min.js` HEAD check; every test fails on any uncaught `pageerror`. |
| `scripts/vendor-three.cjs` | **new** — idempotent, non-fatal vendoring of the global `three.min.js` from the `three` devDep into `simulators/`. |
| `package.json` | add `three@0.149.0` devDep; `vendor:three` script; `pretest:e2e` hook so `bun run test:e2e` self-provisions the asset. |

### `three.min.js` remediation — wired into the patch (turnkey)

The patch makes vendoring automatic: `three@0.149.0` (the **last UMD/global
build** — r150+ is ESM-only, and the sims use the `THREE.*` global) is a
devDependency, and `pretest:e2e` runs `scripts/vendor-three.cjs`, which copies
`node_modules/three/build/three.min.js` → `simulators/three.min.js` if missing.
So `bun install && bun run test:e2e` provisions the asset and the WebGL tests
un-skip — no manual step.

> **Version caveat.** The originally-vendored `three.min.js` was never committed,
> so its exact version is unknown; r149 is the principled pin (last global
> build). If a simulator uses an API that changed since the version it was
> authored against, bump the pin in `package.json`.

> **Production note.** devDependencies are not deployed, so for the **live
> viewer** prefer committing `simulators/three.min.js` (the script then simply
> respects the committed file). The vendor script is the test-time convenience;
> committing the asset is the production fix.

---

## Verification

| Check | Result |
|---|---|
| `tsc --noEmit --strict` on spec + config (Playwright types resolved) | ✅ exit 0 |
| `node --check test-server.cjs` | ✅ syntax OK |
| `test-server.cjs` live serving | ✅ `empty/beta/knot` → 200; `three.min.js` → 404 before / 200 after vendoring (confirms #4) |
| `scripts/vendor-three.cjs` | ✅ provisions the 608 KB build when missing; idempotent no-op when present; non-fatal when `three` absent |
| `playwright test --list` (config loads, tests discovered, no browser) | ✅ 7 tests discovered |
| `git apply --check` on clean folio-assistant `main` (5 files) | ✅ applies cleanly |
| **Live browser run** | ✅ **7/7 passed in 6.8 s** — Chrome 149 (`@sparticuz/chromium`, fetched via npm/GitHub since `cdn.playwright.dev` is egress-blocked), incl. all 3 WebGL tests (SwiftShader) and the heaviest Quantum Brings scene (2.6 s); **no OOM/SIGTERM/timeout**. See *Running in an egress-restricted environment*. |

---

## How to apply (in a folio-assistant checkout)

```bash
cd /path/to/folio-assistant            # litlfred/folio-assistant, on main
git apply /path/to/qou/docs/audits/2026-06-16-playwright-simulators.patch
git add playwright.config.ts test-server.cjs tests/simulators.spec.ts \
        scripts/vendor-three.cjs package.json
bun install                            # installs three@0.149.0 (+ @playwright/test)
bunx playwright install chromium       # if cdn.playwright.dev is blocked, see "egress-restricted" below
bun run test:e2e                       # pretest:e2e vendors three.min.js, then runs
```

`bun run test:e2e` self-provisions `simulators/three.min.js` via the
`pretest:e2e` hook, so all 7 tests run. (If `three` is absent for any reason the
vendor step is non-fatal and the 3 WebGL tests **skip** with a clear reason
while the 4 two-D-sim tests still pass.) For production, also commit
`simulators/three.min.js` (see *Production note*).

---

## Running in an egress-restricted environment (locked-down CI / this sandbox)

`bunx playwright install chromium` fetches from `cdn.playwright.dev`, which is
often **not** in a CI egress allowlist (HTTP 403). `github.com` + the npm
registry usually **are** — so provision Chromium from there instead:

```bash
# Chrome 149 build, released on GitHub, mirrored to npm — matches Playwright 1.60.
bun add -d @sparticuz/chromium@149.0.0
export PLAYWRIGHT_CHROMIUM_PATH="$(node -e \
  "require('@sparticuz/chromium').executablePath().then(p=>console.log(p))")"
bun run test:e2e   # config's launchOptions.executablePath reads PLAYWRIGHT_CHROMIUM_PATH
```

This is exactly how the live run above (7/7, no OOM/SIGTERM) was produced from a
sandbox with `cdn.playwright.dev` blocked. `@sparticuz/chromium` bundles
SwiftShader, so the WebGL tests pass too. No config change beyond setting the env
var — the `executablePath` hook is already in the patched `playwright.config.ts`.
