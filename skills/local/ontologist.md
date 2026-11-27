---
name: ontologist
roles: [collaborator, owner]
description: >
  Semantic Ontologist — audits narrative `.md` blocks and `defines: [...]`
  glossary slugs under `folio/` for mathematical ambiguity, maps paper
  terminology to Mathlib4 / Two-Tier Reservoir / QOU Lean 4 identifiers, and
  enforces `:defterm` / `:refterm` + universe polymorphism (`BP005c`) before
  formalization proceeds.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Semantic Ontologist (Ambiguity Detection, Glossary & Mathlib4 Type Alignment)

## 1. Overview

This skill acts as the **Gatekeeper** for mathematical definitions across `folio/<paper>/`. Before narrative-to-Lean formalization proceeds, every mathematical term must have an unambiguous type assignment in Lean 4 (either an existing `Mathlib.*` type documented via a `glossary/` block, a Tier-B Lean Reservoir community type, or a `def:` content-object triple in `QOU.*`).

> **Source-of-truth note (post-migration):** Authoritative content lives in `.ts` + `.md` (+ `.lean`) content-object triples under `folio/quantum-observable-universe/`, **never** in generated `chapters/*.tex` files, legacy `.github/scripts/ontologist.py`, or `blueprint/src/content.tex`.

---

## 2. Lean MCP & Offline Search Tools

| Task | Preferred MCP tool | Offline CLI fallback (CPU-throttled) |
|---|---|---|
| Check resolved type | `lean_hover_info` | Read target `.lean` file |
| Search project declarations | `lean_local_search` | `nice -n 15 python3 scripts/lean-static-census.py` or `rg` under `folio/*/lean/` |
| Check if a type exists in Mathlib4 | `lean_leansearch` / `lean_loogle` | `grep -rn "structure Foo\|class Foo" .lake/packages/mathlib/Mathlib/` |
| Verify `.ts` `defines:` / glossary integrity | `content_validate` | `nice -n 15 python3 scripts/lib/definition-glossary.py` & `nice -n 15 bun run folio/pipeline/definition-clarity-audit.ts` |

---

## 3. Ambiguity Detection & Standing Disambiguation Rulings

### 3.1 Trigger phrases requiring explicit type disambiguation
- "The mapping" — without specifying domain/codomain types or linearity/functoriality
- "The space" — without specifying `TopologicalSpace`, `IsManifold`, `Module`, or `Scheme`
- "The group" — without specifying `Group`, `TopologicalGroup`, or `Matrix` subgroup
- Bare symbols (`M`, `X`, `G`, `R`) without binder/typeclass level (`[CommRing R]`, `[Field R]`, §7c)

### 3.2 Standing author disambiguation rulings (v2 — STRICT)

| Term | Ruling | Notes |
|---|---|---|
| **energy** (bare) | Replace with `κ` (Hecke cost) | Ban bare "energy"; always use `κ(ξ)`, or qualify as binding/kinetic/crossing |
| **crossing** | OK unqualified | Both braid crossing and nuclear crossing are unambiguous in context |
| **shell** | Always "orbital shell" | Qualify by occupancy `λ` and degree `[n]`, NOT by occupant; formal object `𝔖_ℓ` |
| **trace** | Two traces only: **categorical** and **Markov** | (1) **Categorical trace** (`∫_A`); write "categorical trace of the descended/transient part", never invent separate trace species. (2) **Markov trace** `tr_M` on $H_n(q)$ |
| **dimension** | Always qualify | Quantum dimension $d_\lambda(q)$, Hausdorff dimension $d_H$, categorical dim, topological dim |
| **volume** | Always qualify | Hyperbolic $\mathrm{Vol}(K)$, traced volume $\widehat{V}$, categorical volume, physical volume |
| **force** | Transfer matrix IS the force operator | Interactions are transfer-matrix compositions; no separate classical force primitive |
| **numerical values** | Never `=` for observed values; always `≈` | Write `g_A ≈ 1.275` (unless accompanied by explicit `± δ` or `O(ε)` error bounds); algebraic identities over $\mathbb{Z}[q, q^{-1}]$ use `=` |
| **particle** | Always "knot-particle" or use `𝒦` | A particle IS a knot equivalence class `𝒦_x` |
| **`𝔈_{anything}`** | BANNED | Use `κ` (Hecke cost) or specific qualified term |
| **`T_{m,n}` for torus knot** | BANNED | Use `τ(r,s)` for torus knot label; `T` is reserved for transfer matrices |
| **bar notation on `𝒩`** | BANNED | `𝒩_{Z,N}` is in Gröbner normal form; write `𝒩^{\mathrm{unred}}` if unreduced |

### 3.3 §7c Ground-ring & Category Universe Rulings (`BP005`)

- **Algebraic & combinatorial definitions** MUST be stated over generic `{R : Type*} [CommRing R]` / `[Field R]` / `[LinearOrderedField R]`, never `ℝ`. Concrete `ℝ` realisations belong post-wall only (see [`formalizer.md`](formalizer.md) §Base ring convention).
- **Category-theoretic universe polymorphism (`BP005c`):**
  | Concept | Lean 4 Signature | Universe Rule |
  |---|---|---|
  | Category `C` | `(C : Type u) [Category.{v} C]` | Distinct object `u` and hom `v` universes (never monomorphic `(C : Type) [Category C]`) |
  | Small category | `(C : Type u) [SmallCategory C]` | Objects and homs in `u` |
  | Monoidal / Braided / Rigid | `[Category.{v} C] [MonoidalCategory C] [BraidedCategory C] [RigidCategory C]` | Targeted `Mathlib.CategoryTheory.*` imports (`BP003`) |

---

## 4. Glossary Block vs. Definition Block Policy (`folio/quantum-observable-universe/glossary/`)

| Criterion | Glossary block (`remark` in `glossary/`) | Definition block (`definition` in chapter) |
|---|---|---|
| Semantic novelty | **None** — synonym or light specialization of an existing `Mathlib4` type | Introduces new mathematical/QOU structure or Tier-B Reservoir definition |
| Lean file required? | Not required (points to `Mathlib.*` in `.md`) | **Yes** (`lean.ref` URI in `.ts` + concrete `structure`/`class`/`def` — **never** `:= sorry` type stubs!) |
| Label prefix | `rem:glossary-<term>` | `def:<term>` |
| Mathlib4 naming (`BP004`) | Documents `UpperCamelCase` / `snake_case` Mathlib identifier | Enforces `UpperCamelCase` types/classes, `snake_case` defs/lemmas |

### Wrap-every-occurrence (`:defterm` / `:refterm`)
Every slug declared in a block's `defines: [...]` array must be wrapped with `:defterm[…]{#slug}` once at its canonical defining `.md` site and `:refterm[…]{#slug}` at every other narrative mention (see [`glossary-build.md`](glossary-build.md)).

---

## 5. Checklist

- [ ] New mathematical term checked against `Mathlib4` (`lean_loogle` / offline `.lake/packages/mathlib/Mathlib/` grep) and `folio/quantum-observable-universe/glossary/`
- [ ] Standing v2 disambiguation rulings applied (no bare `energy`, qualified `trace`/`dimension`/`volume`, `τ(r,s)` for torus knots)
- [ ] Definition `.lean` uses concrete `structure` / `class` / `def` (zero `Type* := sorry` stubs) with §7c generic ring & `Category.{v} C` universe polymorphism
- [ ] `.ts` manifest carries valid `defines: [...]` slug and `lean: { ref: "<pkg>:<Decl>" }` (`schemas/lean-packages.ts`)
- [ ] `nice -n 15 python3 scripts/lean-best-practices-lint.py --diff` and `nice -n 15 bun run scripts/run-validate.ts` pass cleanly
