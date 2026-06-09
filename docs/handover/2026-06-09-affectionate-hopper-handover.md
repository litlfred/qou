# Handover — `claude/affectionate-hopper-seYEv` session (2026-06-09)

> **Audience:** the next agent (cold start — no access to this session's chat).
> **Owner is away ~1 week.** This doc is the source of truth for what to do next.
> **Author session:** branch `claude/affectionate-hopper-seYEv`, merged as PR #2003.

---

## 0. TL;DR — pick up here

The owner's standing 4-item plan (priority order **3 → 1 → 2 → 4**):

| # | Item | Status |
|---|------|--------|
| 3 | `/prepare-merge` + merge **PR #2003** (molecular bonds / WS-D) | ✅ **MERGED** (`8eb7386b`) |
| 1 | **WS-D** γγ→benzene assembly spine (validate predictive models) | ✅ **DONE** (in #2003) |
| 2 | **CI code-quality gates** (import-grep + ruff + clippy) | ⏳ **TODO** → new branch |
| 4 | **WS-B de-hardcode** + `not_started`→`not_checked` migration | ⏳ **TODO** → new branch |

**Owner authorized new branches for items 2 & 4.** Start with **Item 2**.

---

## 1. What landed in PR #2003 (on `main` now)

Theme: **molecular bonds from the universal-ILP / Wedderburn chain.**

- **`bond order = LP active-set cardinality`** — orthogonal-channel LP with ab-initio octet valence (`V = 10 − Z`): O₂/N₂/CO covalent → **2 / 3 / 2** (CO's observed triple = 2 covalent σ⊥π **+ 1 dative** O→C, isoelectronic with N₂). Single-chain topology refuted (active-set 1; π pairs anti-bind). Witness `co-bond-order-active-set`.
- **`def:embeddable-knot-operator`** (lateral-π) — overlap-weighted binding `𝔈(K)=𝔈₀·w` (axial σ w=1, transverse π w<1); cardinality weight-independent. **Lean `QOU.Molecular.EmbeddableKnotOperator`, sorry-free, `lake build` green (2220 jobs).** Key theorem **`orthogonal_channels_le_dim`**: ≤3 pairwise-orthogonal nonzero vectors in `EuclideanSpace ℝ (Fin 3)` ⇒ **no p-block bond exceeds order 3** (proven, not a fit).
- **WS-D γγ→benzene spine** (`folio-assistant/computations/benzene_assembly_spine.py` + `rem:benzene-assembly-spine`): consumes the light→¹²C chain (Breit–Wheeler → qq̄ → Borromean nucleon → A=12, sibling-owned) and **validates** acetylene C≡C=**3**, benzene C–C=**1.5** (6 equal, D₆), cyclohexane=**1.0** vs observed. Zero fitted constants.
- **D4** `rem:assembly-shortest-production` (canonical path = Hecke/GS normal form via confinement min-action) + **D5** `rem:assembly-emission-ledger` (net emission = ΔNF·𝔈₀; photon categorical + phonon archimedean; partial ledger).
- Review: 8 Copilot comments (2 passes) all addressed (LP-degeneracy guard, `add_upstream` drift-tracking, field de-confusion, symmetric octet rule, title↔prop, dup-key). Gemini was **daily-quota-blocked** (~24 h) — a fresh `/gemini review` once quota resets would be a good post-merge check, but not blocking.

Workplan/audit context (on `main`): `docs/workplans/2026-06-08-organic-chem-redo-workplan.md`, `docs/audits/2026-06-08-organic-chem-redo-audit.md`.

---

## 2. Item 2 — CI code-quality gates  → branch `claude/ci-code-quality-gates-2026-06-09`

Owner ask: *"anything we can formally pick up across compute infra easily?"* Yes — three cheap gates.

1. **Lean bare-import gate (highest value).** A CI grep gate failing on `^import Mathlib$`.
   - **2 current offenders** (cause the >9-min full-library build timeout):
     - `content/quantum-observable-universe/mass-theory/alpha-k-derivation-procedure.lean`
     - `content/quantum-observable-universe/lean/QOU/AppendixSurreals/FigureEightCasimirWeight.lean`
   - **Fix each** via targeted imports (run Lean's `#min_imports` after restoring the olean cache — see §4). Then the gate is green and prevents regressions.
2. **Python:** `ruff --select F401,F403` over `folio-assistant/computations/` + `tools/` (exclude `_deprecated/`). Live wildcard offenders: `universal-ilp.py`, `substrate/{witness_base,_precision,q_parameter}.py` (the substrate ones are package-facade re-exports — likely keep, add `# noqa: F403` or `__all__`).
3. **Rust:** `clippy -D clippy::wildcard_imports` in `tools/`. ~58 hits, mostly `use super::*` in tests / prelude — **ratchet** (gate new code), don't fail-all on day 1.

Wire as a new workflow (model on `.github/workflows/section-title-audit.yml`'s structure). Make the Lean grep gate **fail** (after fixing the 2 files); ruff/clippy can start **warn-only** then tighten.

---

## 3. Item 4 — WS-B de-hardcode + status migration  → branch `claude/ws-b-dehardcode-notchecked-2026-06-09`

1. **De-hardcode molecular literals → `:val` witness-pin.**
   - `content/.../molecular-construction/benzene-bond-equalization.md`: `1.40 Å` (bond length), `1.54`/`1.34` (single/double refs) — pin to a witness or move to `experimental_constants.py` with `±`.
   - The ~25 bare literals catalogued in WS-B of the organic-chem workplan (`193–386`, `200–400`, `150 kJ/mol`; `11.09`, `8.28`, `3.21`, `3.60`, `0.2083…` eV).
   - Pattern: `:val[name]{precision=N, witness=folio-assistant/computations/<w>.witness.json}`.
2. **Migrate legacy `lean.validation: "not_started"` → `"not_checked"`** (~55 blocks). The rebased schema enum dropped `"not_started"`; current canonical is `"not_checked"`. Sweep with `grep -rl '"not_started"' content/*/*/*.ts`, sed-replace, `bun run validate`.

---

## 4. ⚠ Environment gotchas (these WILL bite you)

- **Lean toolchain:** `elan` / `release.lean-lang.org` is **firewalled** — the `failed to parse release data` SessionStart errors are **benign**. The toolchain works at `$HOME/.elan/bin` (and `/tmp/lean-v4.24.0/bin`). `export PATH="$HOME/.elan/bin:$PATH"`.
- **Restore the olean cache BEFORE any Lean work** (don't rebuild Mathlib from scratch — ~15 min cold):
  ```bash
  ROOT=$(git rev-parse --show-toplevel); TGZ=$(mktemp)
  SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)   # v4.24.0 -> v4-24-0
  git fetch --depth=1 origin "lake-cache/qou-$SLUG" \
    && git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort \
       | while read -r p; do git show "FETCH_HEAD:$p"; done > "$TGZ" \
    && tar xzf "$TGZ" -C "$ROOT" && echo "restored lake-cache/qou-$SLUG"
  ```
  ~767 MB, ~2 min. Then `lake build QOU.<Module>` is seconds. **NB:** git operations touch source mtimes → `lake` may still re-verify the import cone (the PiL2 cone ≈ 8–10 min once); subsequent builds are fast. **SEED the cache branch after a clean build** so the next agent restores instead of rebuilding.
- **Rust kernel `pyhecke_native` is NOT built** in the sandbox → `cross_check_trM_1ppb.py` raises `NotImplementedError: precision=mpfr_50dps requires the Rust kernel`. For witness drift, **take `origin/main`'s `cross-check-trM-1ppb.witness.json`** (CI has the kernel and regenerates authoritatively).
- **`send_later` MCP tool is NOT available** this session — rely on PR webhooks for review/CI events; they don't deliver CI **success** or new pushes, so re-check via `mcp__github__pull_request_read get_check_runs`.

---

## 5. Repo conventions you must honor (from CLAUDE.md)

- **ALWAYS-PR:** branch + PR from commit #1; microcommit; push often. Branch name `claude/<theme>-<utc-ymd>`.
- **Merge method = `rebase`** (CLAUDE.md rule 8) — this **overrides** the `/prepare-merge` skill's "merge-commit default." Only `squash` if the user says "squash"; only `merge`-commit for sub-merges.
- **`/prepare-merge` skill is mandatory before any merge**, then explicit owner merge-word. (Owner is away — **do not merge to `main` without their return-word** unless they pre-authorized that specific PR.)
- **Sidecar discipline:** editing any `content/<chapter>/*.ts` manifest changes its `section-title-audit.qa.json` hash → **regenerate** or CI `audit` fails:
  `bun run content/pipeline/qa-section-title-audit.ts --report-only --write-sidecar --thorough`
- **Witness discipline:** commit the producer script first, *then* re-run so `scriptCommitSha` populates; use `WitnessBuilder.add_upstream(path)` for cross-witness reads (drift tracking).
- **Validate gate:** `cd content && bun run validate quantum-observable-universe` (clean = "✓ Valid — 1 issue" — the lone `proton-mass-substrate-identity` warning is pre-existing/unrelated).

---

## 6. "Prepare-merge ALL open PRs" — the sweep (29 others)

**Constraint:** each PR's branch needs **its own session** to `/prepare-merge` (rebase+push is per-branch-auth). One session cannot sweep all. Recommended order + tool:

- **Tool:** `/integration-backlog <axis>` (batches an axis → PR → prepare-merge per batch) or `/coordinate` (cross-PR triage). Run one branch at a time.
- **Quick/low-risk first:** #2019 (bib one-liner) · #2023 (matrix-M det order) · #1977 (gap-a4 cleanup) · #1976 (voice batch).
- **QA-drains (mechanical):** #2020 · #2022 · #1918 · #1941 · #1928 · #1944.
- **Lean-repair (coordinate, touches `QOU` lib — verify green first):** #2001.
- **Content/math (need review):** #1942 · #1933 · #1990 · #1808 · #1839 · #1765 · #2024 · #1762 · #1569 · #1562.
- **Infra/compute:** #2017→#2023 stack · #1741 · #2011 · #2008 · #2006 · #1878 · #1975.
- **Drafts — hold:** #1062 · #411.
- ⚠ Any PR touching `section-title-audit.qa.json` or `molecular-construction.ts` will hit the recurring **mechanical sidecar/manifest conflict** — resolve by union + sidecar-regen (§5).

---

_Generated by [Claude Code](https://claude.ai/code/session_011bERzXzg7utf3gztgBV96B)_
