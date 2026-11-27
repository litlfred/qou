# Canonical Router for `scripts/*lean*` Tools (`qou-lskl`)

Historically, `scripts/` accumulated ~75 overlapping `*lean*` wrappers across multiple cache, build, and vacuity epochs. **Always use the 7 canonical entry points below** rather than invoking legacy or superseded wrappers.

## 1. Mandatory CPU & Cache Safety Preamble

Every local Lean / Python / Bun invocation on an 8-core (4P+4E) workstation or shared sandbox MUST export single-thread caps and run under `nice`:

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
```

**NEVER run bare `lake build`** on a restored `.olean` tree — Lake re-resolves package manifests and can evict ~3,400 cached Mathlib `.olean`s (`qou-r13s`).

---

## 2. The 7 Canonical Entry Points

| Task | Canonical Script | Typical Invocation |
|---|---|---|
| **1. Edit + verify library `.lean` + importers (isolated write overlay)** | [`../lean-overlay-env.sh`](../lean-overlay-env.sh) | `LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-overlay-env.sh init && LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-overlay-env.sh build QOU/Foo/Bar.lean` |
| **2. Topologically compile an import cone (`lean`-direct, `-j 1`)** | [`../lean-direct-cone.sh`](../lean-direct-cone.sh) (driver: [`../lean_cone_build.py`](../lean_cone_build.py)) | `LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-direct-cone.sh -j 1 QOU.Foo.Bar` |
| **3. Verify leaf / content-block sibling `.lean` (read-only)** | [`../lean-verify.sh`](../lean-verify.sh) | `LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-verify.sh folio/quantum-observable-universe/<ch>/<blk>.lean` |
| **4. Mathlib4 & Reservoir style / §7c / vacuity / boundary linter** | [`../lean-best-practices-lint.py`](../lean-best-practices-lint.py) | `nice -n 15 python3 scripts/lean-best-practices-lint.py --diff` (or `--package <Pkg>`) |
| **5. Knowledge-Graph DAG, SCC, orphan & Reservoir cut-edge audit** | [`../lean-kg-detangler.py`](../lean-kg-detangler.py) | `nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only` |
| **6. Keystone `#print axioms` regression gate** | [`../lean-axiom-guard.py`](../lean-axiom-guard.py) | `LEAN_NUM_THREADS=1 nice -n 15 python3 scripts/lean-axiom-guard.py` |
| **7. Restore prebuilt Mathlib/QOU `.olean` cache** | [`../lean-cache-restore.sh`](../lean-cache-restore.sh) | `nice -n 15 bash scripts/lean-cache-restore.sh` |

---

## 3. Specialized Audit & Infrastructure Scripts (Active, Scoped Use)

- **Static Parity & Coverage:**
  - [`../lean-static-census.py`](../lean-static-census.py) — Deterministic SHA-256 + declaration FQN + comment-stripped `sorry`/`axiom` census (`--rev`, `--check`).
  - [`../lean-root-coverage-audit.py`](../lean-root-coverage-audit.py) — Transitive import-closure gap from `QOU.lean`.
  - [`../dead-lean-pointer-audit.py`](../dead-lean-pointer-audit.py) — Checks `.ts` `lean.ref` URIs against real Lean declarations.
  - [`../lean-duplicate-fqn-audit.py`](../lean-duplicate-fqn-audit.py) — Detects colliding fully-qualified declaration names across modules.
- **Vacuity & Soundness Detectors (backing [`../../folio/pipeline/lean-vacuity-axiom-audit.ts`](../../folio/pipeline/lean-vacuity-axiom-audit.ts)):**
  - [`../lib/lean_decl_scan.py`](../lib/lean_decl_scan.py) — Shared comment-blanking & bracket-aware declaration span scanner.
  - [`../lean-borrowed-name-audit.py`](../lean-borrowed-name-audit.py) — Flags `no-import-wrapper` (`Int`/`Bool` fake Lean).
  - [`../lean-definition-collapsed-audit.py`](../lean-definition-collapsed-audit.py) — Flags `sub-zero-tautology` (`X - X = 0`) and open-claim collapses.
  - [`../lean-self-assuming-audit.py`](../lean-self-assuming-audit.py) & [`../lean-vacuous-theorem-scan.py`](../lean-vacuous-theorem-scan.py) — Self-assuming projection and `: True` detectors.
  - [`../lean-carrier-inhabited-check.py`](../lean-carrier-inhabited-check.py) & [`../lean-context-class-inhabitation-probe.py`](../lean-context-class-inhabitation-probe.py) — Checks §3b-cond context classes for vacuity or refutability.
- **Cache Seeding & Gap Filling (Maintainer / Cache-Refresh Only):**
  - [`../build-missing-oleans.py`](../build-missing-oleans.py) — Bottom-up `lean`-direct builder for out-of-cache Mathlib modules.
  - [`../lean-content-mathlib-gap.sh`](../lean-content-mathlib-gap.sh) — Closes Mathlib `.olean` gaps required by content-block siblings.
  - [`../lean-olean-cache-seed.sh`](../lean-olean-cache-seed.sh) & [`../lean-toolchain-cache-restore.sh`](../lean-toolchain-cache-restore.sh) — Orphan-branch `.olean` and compiler cache management.
  - [`../gen-lean-blocks-shadow.py`](../gen-lean-blocks-shadow.py) — Generates identifier-safe symlink trees (`QOUBlocks`, `QOUAudits`).

---

## 4. Superseded / Legacy Wrappers (Do Not Use in New Workflows)

| Legacy Script | Superseded By | Reason |
|---|---|---|
| `verify-lean-direct.sh`, `leancheck-worktree.sh` | `lean-verify.sh` / `lean-overlay-env.sh` | Older `LEAN_PATH` construction; misses sibling `folio/*/lean` roots or write-overlay safety |
| `lean-build-cone.py`, `lean/compile-cone.sh` | `lean-direct-cone.sh -j 1` (`lean_cone_build.py`) | Superseded by `lean_freshness.py`-aligned cone builder with root aggregator + `--keep-going` |
| `lean-verify-changed.sh`, `lean-verify-cone.sh`, `lean-verify-siblings.sh` | `lean-overlay-env.sh` + `lean-best-practices-lint.py --diff` | Thin convenience wrappers; prefer explicit overlay `build`/`check` + `--diff` lint |
| `lean-sorry-count.py`, `lean-orphan-modules.sh` | `lean-static-census.py` / `lean-kg-detangler.py` | Old regexes over-counted `sorry-free` in docstrings or missed transitive root closure |
