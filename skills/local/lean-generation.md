---
name: lean-generation
roles: [collaborator, owner]
description: >
  Author new Lean 4 modules and content-block `.lean` siblings from `.ts` +
  `.md` content-object triples under `folio/`. Enforces Lean 4.24+ imports-first
  header order, `set_option autoImplicit false`, Mathlib4 naming, §7c base-ring
  generality, Two-Tier Reservoir subgraph placement, and single-threaded
  `lean-overlay-env.sh` / `lean-best-practices-lint.py --diff` verification.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Lean 4 Module & Content-Sibling Generation (`lean-generation`)

## 1. Overview (Content-Object Source of Truth)

Content-object triples (`.ts` + `.md` + `.lean`) under `folio/<paper>/<chapter>/` and library modules under `folio/<paper>/lean/` are the **sole authoritative source**.

> **Purged legacy workflow:** Never invoke removed LaTeX scrapers (`.github/scripts/extract_proof_objects.py`, `generate_lean_stubs.py`, `update_proof_status.py`), never write `\lean{...}` / `\leanok` into generated `.tex` files, and never read/write the frozen `proof-objects.json` manifest.

---

## 2. Placement Gate: Two-Tier Reservoir vs. Canonical `QOU.<Subgraph>`

Before creating a new `.lean` file, classify its home (see [`lean-mathlibext-curator.md`](lean-mathlibext-curator.md) and [`content-graph.md`](content-graph.md)):

1. **General-purpose non-QOU mathematics (`0` QOU model/physics coupling):**
   - **Tier A (`MathlibExt`):** small general `mathlib4` core PR candidates (`-- TODO upstream: Mathlib.<Path>`).
   - **Tier B (6 Lean Reservoir `lean_lib` packages):** `HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion` (plus [`folio/unital-groebner-bases/lean/`](../../folio/unital-groebner-bases/lean/) `UGB`).
   - **Hard rule (`BP008`):** Tier-A and Tier-B modules have **zero `QOU.*` model imports**, **zero `sorry`**, and **zero custom `axiom`s**.
2. **QOU model / chapter formalization:**
   - Library declarations shared by ≥2 blocks go in the single canonical chapter subgraph (`QOU.Core`, `QOU.LiftingDescent`, `QOU.BraidsAndKnots`, `QOU.BringsSurface`, `QOU.Confinement`, `QOU.EightfoldWay`, `QOU.MassTheory`, `QOU.Nuclear`, `QOU.StandardModel`, `QOU.FluidDynamics`, `QOU.InformationTheory`, `QOU.Observations`). **Never** create new synonym folders (`BP009`).
   - Block-specific formalizations live as `folio/<paper>/<chapter>/<block>.lean` siblings paired with `<block>.ts` and `<block>.md` (and **never** shadow a real library declaration with `: True := trivial`!).

---

## 3. Canonical Lean 4.24+ File Template (`BP001`–`BP005`)

Every generated `.lean` file MUST place `import` statements **before** `/-! ... -/` module docstrings (`BP002a`), disable `autoImplicit` (`BP001`), use targeted `Mathlib.*` imports (`BP003`), and start over generic §7c base rings (`BP005`):

```lean
/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

/-!
# Concise Module Title

Summary of main definitions, theorems, §7c base-ring generality, and `[bibkey]` references.
-/

set_option autoImplicit false

namespace TwistedFrobeniusHopf

/-- Public structures/classes/types use `UpperCamelCase` (`BP004a`). -/
structure PairingDatum (R : Type*) [CommRing R] where
  val : R

/-- Theorems and lemmas proving `Prop` use `snake_case` (`BP004b`). -/
@[simp]
theorem val_add_zero {R : Type*} [CommRing R] (d : PairingDatum R) :
    d.val + 0 = d.val := by
  ring

end TwistedFrobeniusHopf
```

---

## 4. Content-Object `.ts` Wiring (`schemas/lean-packages.ts`)

| Block kind | Lean required? | `.ts` `lean.ref` URI shape |
|---|---|---|
| `definition` | **Yes** (enforced) | `lean: { ref: "qou:QOU.<Subgraph>.<UpperCamelTypeOrSnakeDef>" }` |
| `theorem`, `lemma`, `proposition`, `corollary` | **Expected** | `lean: { ref: "qou:QOU.<Subgraph>.<snake_case_thm>" }` + matching `**Proof.**` in `.md` |
| `conjecture` | Optional (§3b-cond) | `lean: { ref: "qou:QOU.<Subgraph>.<ConjectureClass>" }` |
| `prose`, `equation`, `diagram`, `table` | N/A | Omit `lean` field |

Parse and validate URIs via [`schemas/lean-packages.ts`](../../schemas/lean-packages.ts) (`qou`, `ugb`, `fred2005`).

---

## 5. Trivial-Model Consistency Witness for §3b-cond Conjecture Classes

Whenever a genuine open conjecture is axiomatised as a `class` (per AGENTS.md §3b-cond, carrying **hypotheses** from which downstream theorems derive — never carrying the conclusion itself per [`lean-proof-vacuity-audit.md`](lean-proof-vacuity-audit.md) §1 & §10!), emit a paired consistency witness `def trivialModel` (as a **`def`**, NEVER an `instance`!) showing the hypothesis bundle is non-contradictory without polluting typeclass synthesis.

---

## 6. CPU-Throttled Verification & Linter Gate (`lean-build-hygiene.md`)

**NEVER** run bare `lake build`. Verify every generated `.lean` file single-threaded:

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1

# 1. Static Mathlib4/Reservoir hygiene gate (BP001-BP009):
nice -n 15 python3 scripts/lean-best-practices-lint.py --diff

# 2. Type-check library module + sibling via private symlink-farm overlay:
nice -n 15 bash scripts/lean-overlay-env.sh init
nice -n 15 bash scripts/lean-overlay-env.sh build QOU/<Subgraph>/<Module>.lean
nice -n 15 bash scripts/lean-overlay-env.sh check folio/quantum-observable-universe/<chapter>/<block>.lean

# 3. Validate content manifest & cross-references:
nice -n 15 bun run scripts/run-validate.ts
```

## 7. Checklist

- [ ] Imports precede `/-! ... -/` docstring (`BP002a`) and `set_option autoImplicit false` is present (`BP001`)
- [ ] Minimal targeted `Mathlib.*` imports (`BP003`); zero `QOU.*` upward imports in Tier-A/Tier-B (`BP008`); zero new synonym dirs (`BP009`)
- [ ] `UpperCamelCase` types/classes and `snake_case` theorems/lemmas (`BP004`) with `/-- ... -/` docstrings
- [ ] §7c generic base ring (`[CommRing R]` / `[Field R]`) unless genuinely Archimedean (`BP005`, `BP006`)
- [ ] Zero `: True` / self-assuming vacuity (`BP007`); matching `**Proof.**` narrative written in `.md`
- [ ] Verified with `LEAN_NUM_THREADS=1 nice -n 15` overlay check + `lean-best-practices-lint.py --diff`
