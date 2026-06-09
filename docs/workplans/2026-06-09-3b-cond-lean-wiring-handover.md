# Handover — §3b-cond Lean class-hypothesis wiring (follow-up to PR #1988)

**Date:** 2026-06-09
**Author leaving:** ~1 week (offline). No blocking questions outstanding.
**Status of the parent work:** ✅ **PR #1988 merged** (rebase-merge) — conjecture
triage refresh (tier-tag completion + §3b provable-uses-conjecture sweep).
**This doc:** the single tracked follow-up that #1988 deferred.

---

## TL;DR for the next agent

PR #1988 disclosed, on the **narrative side**, that 10 provable blocks are
*conditional on a conjecture* (added `(conditional on conj:X)` banners). The
**Lean side** of the §3b-cond contract — putting the conjecture's `class` as an
explicit `[Instance]` hypothesis on each downstream theorem — was **not done**
(Lean toolchain is network-blocked in the web sandbox; see §Environment). That
is the entire remaining task. It is **mostly mechanical**: 9 of the 10
conjecture classes **already exist**; the work is adding the instance hypothesis
to each downstream `.lean` and (for 1 conjecture) locating/creating its class.

**Good news:** no new mathematics. Each downstream proof already works; you are
adding a hypothesis it is *allowed* to assume, then the
`conjectural-propagation-audit` reclassifies the block from "silent violation"
to "conditional-on-class" (the honest state).

---

## The 10 blocks to wire (block → conjecture)

All 10 already have the **narrative banner** (done in #1988) and the conjecture
in `uses[]` (done). The `.lean` instance-hypothesis is the TODO.

| # | Downstream block (`.md`/`.lean`) | conditional on `conj:` | conj `.lean` `class`? | downstream `.lean` already has `[…]` hyp? |
|---|---|---|---|---|
| 1 | `mass-theory/binding-genfun-qdifference` | `binding-manybody-eq-jet-filtration` | ❌ **no `.lean` found by name** — locate or create the class FIRST | 0 |
| 2 | `mass-theory/knot-mass-formula-unified` | `knot-factor-frobenius-pairing` | ✅ 1 | 1 (verify it's the right class) |
| 3 | `mass-theory/mass-element-nf` | `mass-endomorphism` | ✅ 2 | 0 |
| 4 | `mass-theory/hook-weight-derivation` | `shell-transition-knot` | ✅ 1 | 0 |
| 5 | `mass-theory/rho-k-h3a-refinement` | `hoefsmit-scattering-pipeline` | ✅ 1 | 0 |
| 6 | `mass-theory/jet-prefix-gb-filtration` | `confinement-grading-correspondence` | ✅ 2 | 0 |
| 7 | `mass-theory/force-carrier-intertwining-correspondence` | `e-hartree-categorical-derivation` | ✅ 2 | 0 |
| 8 | `mass-theory/knot-operator-lp-selection` | `weak-spectral-completeness` | ✅ 2 | 6 (may be partly wired — verify) |
| 9 | `mass-theory/knot-indexed-convolution-grid` | `joint-galois-braid-action` | ✅ 2 | 0 |
| 10 | `fluid-dynamics/p2-critical-exponent` | `regularity-breakdown` | ✅ 1 | 2 (see coordination note — sibling #1997 touches this cone) |

> The "`[…]` hyp count" column came from a crude `grep -cE '\[[A-Z][A-Za-z]*[^]]*\]'`
> on the `.lean` (counts square-bracket instance-binder-like patterns). Treat it
> as a hint, not ground truth — open each file and confirm whether the bracket is
> the *right* conjecture class or an unrelated typeclass (`[CommRing R]`, etc.).

**Item 1 (`binding-manybody-eq-jet-filtration`) is the only non-mechanical one:**
its conjecture `.lean` was not found by a name-grep. Either the file is named
differently, or the class doesn't exist yet. Resolve by:
`grep -rl "binding.manybody\|jet.filtration" content/quantum-observable-universe/**/*.lean`
and read the `uses[]` of `binding-genfun-qdifference.ts` for the exact `conj:` label
+ its `lean.ref`.

---

## The §3b-cond recipe (per CLAUDE.md §"§3b-cond — Conditional-class exception")

For each block, all four must hold for the audit to classify it
**conditional-on-class** instead of a propagation violation:

1. **Class axiomatisation** — `conj:C` has `class C (…) where …` in its `.lean`
   (the `sorry` in any instance = the conjecture). ✅ 9/10 already done.
2. **Explicit hypothesis on Lean side** — downstream `.lean` decl carries the
   class as an explicit `[C …]` instance binder, e.g.
   ```lean
   theorem downstream_result {M : Type*} [C M] : … := by
     -- proof may use C.field1, C.field2; otherwise fully verified.
   ```
   ⬅ **THIS is the TODO for ~9 of the 10.**
3. **Narrative banner** — `.md` opens with `**… (conditional on [conj:C](…)).**`
   ✅ done in #1988 for all 10.
4. **`uses[]` names the conj** — ✅ done.

**Verify with:** `bun run` the propagation audit and confirm these 10 land in the
*conditional-on-class* bucket, not the violation bucket:
```
content/pipeline/conjectural-propagation-audit.ts
```
(Run `cd content && bun run pipeline/conjectural-propagation-audit.ts` or via the
project's standard runner; check how #1988 invoked it — it regenerated
`docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json`.)

---

## What is ALREADY DONE (do not redo)

- **All 10 narrative banners** — `(conditional on conj:X)` in the `.md`. ✅
- **4 edge-drops** (NOT conditional — proved unconditionally, `conj:` removed from
  `uses[]`): `bring-trilog-imaginary-tate-rational`, `reeb-u1-chart-swap`,
  `blowup-yekutieli`, `ns-obstruction-computation`. **No Lean class needed.** ✅
- **1 no-op:** `lambda-scale-substrate-form` (already honest, deprecation
  authorNote). ✅
- **§H disposition table** in `docs/audits/2026-06-07-conjecture-triage.md` is
  correct (10 banner / 4 edge-drop / 1 no-op = 15). ✅ (Copilot caught it stale;
  fixed in #1988 commit `222fa6ed1c`.)

---

## Environment gotchas (READ before touching Lean)

- **Toolchain IS installed:** `leanprover/lean4:v4.24.0` at `/root/.elan/`;
  `lake`+`elan` on PATH at `/root/.elan/bin`. The repeating SessionStart
  `failed to parse release data: https://release.lean-lang.org` errors are
  **harmless** override-resolution noise (that host is firewalled, but the
  toolchain is already present).
- **`lake exe cache get` → 403** (mathlib cache server firewalled). No fast
  mathlib oleans over the network.
- **`lake-cache/qou-v4-24-0` orphan branch** has prebuilt oleans (732 MB tgz →
  2.8 G in root `.lake/`), BUT it is **STALE**: ~729 QOU `.lean` files changed
  since the cache commit (`1fa64a6b`), so restoring it then `lake build QOU`
  triggers a **full Mathlib-from-source rebuild = hours**. Restore recipe is in
  CLAUDE.md §"Mathlib cache 403 fallback", but it will NOT give you a fast build
  right now.
- **Therefore:** either (a) **rely on CI** (`lean_ci.yml` has proper caching) for
  Lean validation — author carefully, push, let CI gate; or (b) seed a fresh
  `lake-cache/qou-v4-24-0` from a full build first (hours) and **re-seed the
  branch** per CLAUDE.md §"PRESERVE THE BUILD" so the *next* agent restores fast.
- **lean-lsp MCP tools** (`lean_goal`, `lean_diagnostic_messages`, …) will be
  **cold / time out** until valid oleans exist. Don't iterate blind — establish
  an LSP context first (see CLAUDE.md §"Manual fallback when auto-detection fails").

---

## Coordination notes

- **Sibling PR #1997 (`core-levi-form`, fluid-dynamics non-NS slice)** works the
  **same conjecture cone** as item #10 (`regularity-breakdown`, plus
  `q-aubin-lions`/`ns-counterexample`). The owner stated #1997 keeps the
  §3b-cond pattern with **5 `[Instance]` hyps** on `core-levi-form`'s theorem.
  → Before wiring `p2-critical-exponent → regularity-breakdown`, **check if #1997
  merged** and reuse whatever class shape it established for `regularity-breakdown`.
  Don't author a competing class. (Original heads-up was on PR #1988; comment by
  owner.)
- **`main` moves FAST** — during the #1988 session it advanced ~3 commits every
  few minutes (active Rust/compute: `hecke-engine`, `pyhecke-native`,
  `derived_chi_catalogue`). **Rebase frequently**; expect to re-rebase several
  times in any prepare-merge.

---

## Suggested plan for the next agent

1. New branch `claude/3b-cond-lean-wiring-<utc-ymd>` (combine all 10 — one
   coherent PR; per CLAUDE.md "combine related work").
2. Resolve **item 1** first (locate/create `binding-manybody-eq-jet-filtration`
   class).
3. Add the `[ConjClass …]` instance binder to each of the 10 downstream `.lean`
   theorem statements; adjust the proof only if Lean now needs to *use* a class
   field (most won't — the hypothesis is just present).
4. Coordinate item 10 with **#1997** (see above).
5. Run `conjectural-propagation-audit.ts`; confirm all 10 → conditional-on-class;
   regenerate its witness.
6. `/prepare-merge` — Lean gated by CI (`lean_ci.yml`), not the local sandbox
   build (which is network-blocked). Note that explicitly in the review request,
   as #1988 did.

---

## Pointers

- Parent PR: `litlfred/qou#1988` (merged) · triage doc:
  `docs/audits/2026-06-07-conjecture-triage.md` (§H = disposition table).
- §3b-cond contract: `CLAUDE.md` → "§3b-cond — Conditional-class exception (Option B)".
- Propagation audit: `content/pipeline/conjectural-propagation-audit.ts`.
- Merged-but-undeleted branch from the #1988 session:
  `claude/serene-albattani-fZOjM` (safe to delete).
