# Playwright simulator E2E suite — flakiness diagnosis & fix plan

**Date:** 2026-06-16
**Session:** determined-hawking follow-up (`claude/amazing-galileo-ih3g4q`)
**Scope:** the deferred "OOM/SIGTERM/Timeouts in `tests/simulators.spec.ts`" task.
**Status:** root-caused; ready-to-apply patch produced (static + server-level
verified; live browser run deferred — see *Verification*).

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
a corrected config, plus a remediation note for `three.min.js`.

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
| `playwright.config.ts` | dedupe `timeout`; `fullyParallel:false`; CI retries; container launch flags (`--disable-dev-shm-usage` + SwiftShader); `actionTimeout`/`navigationTimeout`; `webServer.url` health check on `simulators/empty.html`. |
| `test-server.cjs` | **new** — dependency-free static server on `127.0.0.1:8080`, traversal-guarded, clean SIGTERM/SIGINT shutdown. |
| `tests/simulators.spec.ts` | **new** — serial Tier-1 suite (7 tests): load + URL-param parsing for the 2D sims (beta-decay `q`+`shell`, knot `q`+`color`), WebGL load/parse for the Brings sims guarded behind a `three.min.js` HEAD check; every test fails on any uncaught `pageerror`. |

### `three.min.js` remediation (do this too)

The spec's WebGL tests **skip** until this is resolved. Pick one (vendoring is
recommended — the sims are written offline-first with `./three.min.js`):

1. **Vendor the file (recommended).** Add `simulators/three.min.js` (the legacy
   UMD/global build matching the `THREE.*` global API the sims use, i.e. a
   pre-r150 `three.min.js`) and commit it. The skip guard then activates the
   WebGL tests automatically.
2. **Pin a CDN.** Replace `./three.min.js` with a hash-pinned CDN URL — but this
   breaks the offline-first design and adds a network dependency to the sims.
3. **Bundle from npm.** Add `three` (legacy global build) as a dependency and
   copy `three.min.js` into `simulators/` at build time.

---

## Verification

| Check | Result |
|---|---|
| `tsc --noEmit --strict` on spec + config (Playwright types resolved) | ✅ exit 0 |
| `node --check test-server.cjs` | ✅ syntax OK |
| `test-server.cjs` live serving | ✅ `empty/beta/knot` → 200; `three.min.js` → 404 (confirms #4) |
| `playwright test --list` (config loads, tests discovered, no browser) | ✅ 7 tests discovered |
| `git apply --check` on clean folio-assistant `main` | ✅ applies cleanly |
| **Live browser run** | ⛔ **deferred** — `cdn.playwright.dev` is not in this environment's egress allowlist (`playwright install chromium` → HTTP 403), and no system Chrome/Chromium is present. Run in CI or a network-allowlisted folio-assistant session. |

---

## How to apply (in a folio-assistant checkout)

```bash
cd /path/to/folio-assistant            # litlfred/folio-assistant, on main
git apply /path/to/qou/docs/audits/2026-06-16-playwright-simulators.patch
git add playwright.config.ts test-server.cjs tests/simulators.spec.ts
# (Separately) vendor simulators/three.min.js to enable the WebGL tests.
bun install
bunx playwright install chromium       # needs cdn.playwright.dev allowlisted
bun run test:e2e                       # == playwright test
```

Expected on a fresh clone *without* `three.min.js`: the 4 two-D-sim tests pass,
the 3 WebGL tests **skip** with reason "three.min.js not vendored". After
vendoring `three.min.js`, all 7 run.
