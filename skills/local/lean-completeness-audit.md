---
name: lean-completeness-audit
roles: [collaborator, owner]
description: >
  Audit Lean 4 formalization completeness, root reachability, `lean.ref`
  integrity, Two-Tier Reservoir subgraph purity, vacuity freedom, and witness
  freshness across `folio/` using `lean-static-census.py`,
  `lean-kg-detangler.py`, `lean-best-practices-lint.py`,
  `lean-root-coverage-audit.py`, `dead-lean-pointer-audit.py`, and
  `folio/pipeline/lean-vacuity-axiom-audit.ts`.
allowed-tools: Read Bash Grep Glob Agent
---

# Lean Completeness & Subgraph Hygiene Audit (`lean-completeness-audit`)

## 1. Role & Mandatory CPU Discipline

Verify that every paper's Lean 4 formalization under `folio/<paper>/` (`quantum-observable-universe`, `unital-groebner-bases`, `fred2005-formal-groups`) is structurally complete, acyclic, non-vacuous, and aligned with Mathlib4 / Lean Reservoir standards.

Always export single-thread caps and run under `nice -n 15` (see [`lean-build-hygiene.md`](lean-build-hygiene.md)):
```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
```

---

## 2. Canonical Automated Audit Suite (`< 15s` Static Gates)

| Audit Dimension | Canonical Tool | Invocation |
|---|---|---|
| **1. Static parity, decl FQNs, comment-stripped `sorry`/`axiom` counts** | [`scripts/lean-static-census.py`](../../scripts/lean-static-census.py) | `nice -n 15 python3 scripts/lean-static-census.py --digest` |
| **2. Subgraph DAG, SCCs, orphans, §7c, & 6 Reservoir `lean_lib` cut-edges** | [`scripts/lean-kg-detangler.py`](../../scripts/lean-kg-detangler.py) | `nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only` |
| **3. Mathlib4 & Reservoir style / §7c / vacuity / `BP008` import boundary** | [`scripts/lean-best-practices-lint.py`](../../scripts/lean-best-practices-lint.py) | `nice -n 15 python3 scripts/lean-best-practices-lint.py --diff` (or `--package all-community`) |
| **4. Library root (`QOU.lean`) transitive import coverage** | [`scripts/lean-root-coverage-audit.py`](../../scripts/lean-root-coverage-audit.py) | `nice -n 15 python3 scripts/lean-root-coverage-audit.py` |
| **5. Content `.ts` `lean.ref` resolution & dead pointers** | [`scripts/dead-lean-pointer-audit.py`](../../scripts/dead-lean-pointer-audit.py) | `nice -n 15 python3 scripts/dead-lean-pointer-audit.py` |
| **6. Semantic vacuity & review-ledger freshness** | [`folio/pipeline/lean-vacuity-axiom-audit.ts`](../../folio/pipeline/lean-vacuity-axiom-audit.ts) | `nice -n 15 bun run folio/pipeline/lean-vacuity-axiom-audit.ts folio/quantum-observable-universe --check-ledger docs/audits/lean-vacuity-review-ledger.json` |
| **7. Keystone `#print axioms` regression guard** | [`scripts/lean-axiom-guard.py`](../../scripts/lean-axiom-guard.py) | `nice -n 15 python3 scripts/lean-axiom-guard.py` |
| **8. Python computation `.witness.json` staleness** | [`computations/witness_staleness_triage.py`](../../computations/witness_staleness_triage.py) | `nice -n 15 python3 computations/witness_staleness_triage.py` |

> **Historical traps (do NOT use):**
> - `proof-objects.json` is frozen since the April 2026 content-object migration ([`docs/audits/2026-06-03-proof-objects-json-extractor-broken.md`](../../docs/audits/2026-06-03-proof-objects-json-extractor-broken.md)).
> - `docs/audits/lean-compile-diagnostics.json` can go stale within days of Lean edits ([`docs/audits/2026-06-03-proof-axis-629-fails-stale-diagnostics.md`](../../docs/audits/2026-06-03-proof-axis-629-fails-stale-diagnostics.md)).
> - Class-body `sorry`s inside §3b-cond conjectural classes are catalogued in [`docs/audits/2026-06-03-lean-3b-cond-class-sorries-catalog.md`](../../docs/audits/2026-06-03-lean-3b-cond-class-sorries-catalog.md); always strip comments/strings (or use `\bsorry\b(?!-)`) so `sorry-free` in docstrings is never counted.

---

## 3. Step-by-Step Audit Protocol

1. **Workspace & Toolchain Parity:**
   - Verify [`/lean-toolchain`](../../lean-toolchain) and all `folio/*/lean/lean-toolchain` files pin the identical Lean version, and all `lakefile.toml` files pin the identical Mathlib commit `rev` with `autoImplicit = false`.
2. **Import Closure vs. Build Glob Coverage:**
   - Note that `folio/quantum-observable-universe/lean/lakefile.toml` sets `globs = ["QOU", "QOU.+"]`, so `QOU` builds the whole tree, while `lean-root-coverage-audit.py` + `lean-kg-detangler.py` measure which modules are orphaned from `QOU.lean` vs referenced by `.ts` `lean.ref`s.
3. **Content Block → Lean Coverage:**
   - `definition` blocks MUST carry a resolving `lean.ref` URI (`"<pkg>:<Decl>"` in [`schemas/lean-packages.ts`](../../schemas/lean-packages.ts)); `theorem`/`lemma`/`proposition`/`corollary` blocks are expected to resolve and carry matching `.md` `**Proof.**` narratives.
4. **Two-Tier Community Library Purity:**
   - Run `lean-kg-detangler.py` and `lean-best-practices-lint.py --package all-community` to verify zero `sorry`, zero custom `axiom`, §7c base-ring generality, and track `community_to_qou_cut_edges` toward `0`.
5. **Single-Threaded Cone Compile Verification:**
   - Verify changed cones with `nice -n 15 bash scripts/lean-direct-cone.sh -j 1 <TargetModule>` (never bare `lake build`).

---

## 4. Checklist

- [ ] All `lean-toolchain` and `lakefile.toml` Mathlib pins match across `/`, `qou`, `ugb`, and `fred2005`
- [ ] `lean-static-census.py` reports 0 unexpected `sorry` or `axiom` growth
- [ ] `dead-lean-pointer-audit.py` and `scripts/run-validate.ts` pass cleanly
- [ ] `lean-best-practices-lint.py --diff` reports `critical=0` (`BP001`–`BP009`)
- [ ] `lean-kg-detangler.py` reports `0` module-level SCC cycles and non-increasing `community_to_qou_cut_edges`
- [ ] `lean-vacuity-axiom-audit.ts --check-ledger` and `computations/witness_staleness_triage.py` are clean
