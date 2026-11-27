---
name: lean-build-hygiene
roles: [collaborator, owner]
user_invocable: true
description: >
  Canonical CPU-throttled Lean 4 build, overlay-cone verification, script router,
  and Mathlib4 / Lean Reservoir community `lean_lib` hygiene gate. Enforces
  single-threaded `LEAN_NUM_THREADS=1 nice -n 15` execution, forbids bare
  `lake build`, routes across the ~75 `scripts/*lean*` helpers, and gates
  every Lean diff with `scripts/lean-best-practices-lint.py` and
  `scripts/lean-kg-detangler.py`.
allowed-tools: Read Edit Write Bash Grep Glob
---

# Lean Build & Community-Library Hygiene (`lean-build-hygiene`)

## 1. Non-Negotiable CPU & Cache Rules (`watch cpu!`)

1. **Single-thread environment variables on EVERY shell command:**
   ```bash
   export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
          OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
   ```
2. **Always `nice -n 15` and `-j 1`:**
   - Prefix every `lean`, `python3`, `bun`, or `git` audit/build command with `nice -n 15`.
   - Pass `-j 1` to [`scripts/lean-direct-cone.sh`](../../scripts/lean-direct-cone.sh) (its default `nproc - 1` saturates P-cores on multi-worktree hosts).
   - **Never** launch multiple background `lean` compilations (`&`) in parallel.
3. **NEVER run bare `lake build`:**
   - At repo root, bare `lake build` builds **0 targets** while exiting 0 (see `/lakefile.toml`).
   - Inside `folio/quantum-observable-universe/lean/`, `lake build` against a restored `.olean` cache can detect URL/trace drift, delete `.lake/packages/mathlib`, and trigger a 60-minute Mathlib rebuild (`qou-r13s`).
   - Always verify via **`lean`-direct** (`lean-overlay-env.sh`, `lean-direct-cone.sh -j 1`, or `lean-verify.sh`).
4. **NEVER run bare `git fetch origin`:**
   - Always fetch a specific branch (`git fetch origin main`), avoiding multi-GB `lake-cache/*` orphan refs and mutable `FETCH_HEAD` races.

---

## 2. Canonical Verification Workflow (Router over `scripts/*lean*`)

Full script index: [`scripts/lean/README.md`](../../scripts/lean/README.md).

### A. Editing an existing library module (`folio/quantum-observable-universe/lean/{MathlibExt,<TierBLib>,QOU/<Chapter>}/...`)

`folio/quantum-observable-universe/lean/` hosts **`7 + 1` top-level `[[lean_lib]]` targets** sharing the single `.lake/build/lib/lean/` root (`MathlibExt`, `QCalculus`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `HeckeTemperleyLieb`, `BraidKnotOctonion`, plus `QOU` consolidated into its `12` canonical `QOU/<Chapter>/` subgraphs). If rebasing an open PR authored against legacy `QOU/<OldSynonym>/` paths, run `nice -n 15 python3 scripts/apply-lean-reservoir-migration.py --fixup-branch` first.

When you edit a library `.lean` file, any downstream importer reading the shared `.lake` tree would silently load the **stale** `.olean`. Use the private symlink-farm overlay ([`scripts/lean-overlay-env.sh`](../../scripts/lean-overlay-env.sh)):

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1

# 1. Initialize complete symlink farm once per session (~seconds)
nice -n 15 bash scripts/lean-overlay-env.sh init

# 2. Compile your edited module into the private overlay (e.g. HeckeTemperleyLieb/Foo.lean or QOU/MassTheory/Bar.lean)
nice -n 15 bash scripts/lean-overlay-env.sh build <LibOrQOU>/<Path>.lean

# 3. Check downstream importers or content-block siblings against your rebuilt .olean
nice -n 15 bash scripts/lean-overlay-env.sh check folio/quantum-observable-universe/<chapter>/<block>.lean
```

> **Trap warning:** Never create a hand-rolled partial `LEAN_PATH=/tmp/my-ovl:$LEAN_PATH` directory! Lean resolves a namespace prefix in the **first** matching root and does **not** fall through for sibling modules. Always use `lean-overlay-env.sh init`.

### B. Compiling a multi-file dependency cone

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 bash scripts/lean-direct-cone.sh -j 1 QOU.<Subgraph>.<TargetModule>
```

(`lean_cone_build.py` automatically passes `-DautoImplicit=false` and `-s 65536`.)

### C. Checking a leaf or content-block sibling `.lean` (no library edits)

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 bash scripts/lean-verify.sh folio/quantum-observable-universe/<chapter>/<block>.lean
```

### D. Filling a missing Mathlib `.olean` (cache gap, NOT a proof bug)

If `lean` reports `object file '.../Mathlib/Foo/Bar.olean' does not exist`, restore the cache first (`bash scripts/lean-cache-restore.sh`), and if the module lies outside the cached cone, build **only** the missing Mathlib delta:

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
source scripts/lean-direct-env.sh
nice -n 15 python3 -u scripts/build-missing-oleans.py Mathlib.Foo.Bar
```

---

## 3. Mandatory Pre-Commit Linter & KG Boundary Gates

Before committing any new or modified `.lean` file, run **both** static gates (`< 15s` deterministic Python):

### Gate 1 — Mathlib4 & Lean Reservoir Best-Practices Linter (`BP001`–`BP009`)

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1

# Pre-commit branch diff check (exits 1 on any critical violation):
nice -n 15 python3 scripts/lean-best-practices-lint.py --diff

# Audit a specific Reservoir community candidate package:
nice -n 15 python3 scripts/lean-best-practices-lint.py --package TwistedFrobeniusHopf
```

Enforced rules in [`scripts/lean-best-practices-lint.py`](../../scripts/lean-best-practices-lint.py):
- **`BP001` (`autoImplicit`):** `set_option autoImplicit false` required on standalone & Reservoir community modules; `set_option autoImplicit true` is a critical error everywhere.
- **`BP002` (Headers & Docstrings):** `import` statements MUST precede `/-! ... -/` module docstrings (Lean 4.24+ syntax); `/-! ... -/` module docstrings, Apache-2.0 copyright headers, and `/-- ... -/` public declaration docstrings (`docBlame`) required for community packages.
- **`BP003` (Minimal Targeted Imports):** Bare `import Mathlib` and `import QOU` are forbidden (`critical`); avoid broad `import Mathlib.Tactic` in favor of `import Mathlib.Tactic.<Specific>`.
- **`BP004` (Mathlib4 Naming):** `UpperCamelCase` for `structure`/`class`/`inductive` types; `snake_case` for `theorem`/`lemma` proofs of `Prop`.
- **`BP005` (§7c Ring & Universe Generality):** No gratuitous `: ℝ` when `[CommRing R]`, `[Field R]`, or `[LinearOrderedField R]` suffices; no mixing generic `[CommRing R]` and concrete `ℝ` in one file; universe-polymorphic `Category.{v} C`.
- **`BP006` (Zero Empirical / Float Literals):** Zero decimal literals (`1.1097`, `938.272`), `Float`, `CODATA`, or `substrate_q` inside pure-math community libraries and pre-wall chapters.
- **`BP007` (Zero Vacuity & Axiom Hygiene):** Zero `: True` conclusions or carrier fields, zero self-assuming projections (`:= d.claim_foo`), zero `X - X = 0` definitional-subtraction tautologies, zero `native_decide`, zero `sorry` or custom `axiom` in Tier-A/Tier-B libraries.
- **`BP008` (Strict Zero-`QOU.*` Upward Import Boundary):** Tier-A (`MathlibExt`) and Tier-B Reservoir community libraries (`HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`) MUST NEVER import QOU physics/model modules.
- **`BP009` (No Synonym-Directory Sprawl):** Blocks creation of unapproved new top-level subdirectories under `folio/quantum-observable-universe/lean/QOU/`.

### Gate 2 — Knowledge-Graph Subgraph & Cut-Edge Detangler

Whenever adding imports across subgraphs or curating pure-math modules for Tier-A / Tier-B extraction, verify that `community_to_qou_cut_edges` and directory SCC tangles do not grow:

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only
```

Full architecture options & baseline metrics live in [`docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-options.md`](../../docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-options.md).

---

## 4. Two-Tier Community Packaging Standards (Mathlib4 + Lean Reservoir)

Non-QOU-specific mathematics developed in this repository follows a strict Two-Tier architecture (see [`lean-mathlibext-curator.md`](lean-mathlibext-curator.md)):

1. **Tier A — `MathlibExt` (Selective `leanprover-community/mathlib4` Core PRs):**
   Small, general-purpose lemmas (`List`/sort/foldl, elementary matrix/trace/Cauchy–Binet, ordered-field/sqrt inequalities, general Borel/Dirichlet/Čech helpers) carrying `-- TODO upstream: Mathlib.<Path>`.
2. **Tier B — 6 Standalone Lean Reservoir `lean_lib` Community Packages:**
   - `HeckeTemperleyLieb` (coupled with [`folio/unital-groebner-bases/lean/`](../../folio/unital-groebner-bases/lean/))
   - `TwistedFrobeniusHopf`
   - `ToricConicOpt`
   - `CompactQuantumMetrics`
   - `QCalculus`
   - `BraidKnotOctonion`

**Hard invariants for every Tier-A and Tier-B module:**
- **Zero `QOU.*` model imports** (only `Mathlib.*`, `Std.*`, `UGB.*`, or lower-tier community libraries).
- **Zero `sorry` and zero custom `axiom`s** (`#print axioms` shows at most `[propext, Classical.choice, Quot.sound]`).
- **`set_option autoImplicit false`** at the top of the file after `import`s + `/-! ... -/`.
- **`#lint` clean** (`docBlame`, `simpNF`, `unusedArguments`, `dupNamespace`).

---

## 5. Pre-Commit Checklist

- [ ] Exported `LEAN_NUM_THREADS=1 ...` and used `nice -n 15` (`-j 1`) on every command
- [ ] Verified edited library files via `scripts/lean-overlay-env.sh build` + importer `check` (never bare `lake build`)
- [ ] `nice -n 15 python3 scripts/lean-best-practices-lint.py --diff` exits 0 (`critical=0`)
- [ ] `bash scripts/check-sidecars.sh` inspected for §7c base-ring & QA sidecar criteria
- [ ] `nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only` confirms zero new `Tier-A/B -> QOU.*` cut-edges
- [ ] Inspected `git status` and `git diff --name-status` (zero `.olean`/`.ilean`/`.trace` artifacts or sparse-checkout deletions)
