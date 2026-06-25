# Lean library-tree §7c coverage gap — audit + calibration

**Date:** 2026-06-25
**Branch:** `claude/lean-library-7c-audit-2026-06-25`
**Trigger:** the §7c miss in #2782 (a gratuitous `(q : ℝ)` / `SL₂(ℝ)` on a purely-algebraic τ-kernel
lemma in a standalone library Lean file with no sidecar) raised the question: *how many other library
Lean files carry the same class of leak, and why didn't the mechanical checkers catch them?*

## Finding 1 — the coverage gap is structural and large

- **839** Lean files live under `content/quantum-observable-universe/lean/QOU/**`.
- **2280** `.qa.json` sidecars exist; **0** of them are inside a `lean/` tree. Every sidecar is
  co-located with a **content block** (`.md`/`.ts`) in a chapter directory.
- Content blocks reference the formalization via `lean.ref` (`ref: "qou:QOU.BraidKnot…"`), which
  resolves to the **library tree** (candidate-2 resolution). So the file the agent actually edits
  has **no co-located sidecar**.

The per-block checkers (`q-usage-*`, `wall-side-correct`) key off the content block. **Open question
(could not verify locally — the checkers moved to `folio-assistant` per the miga migration):** does the
per-block checker read the *resolved* library-tree Lean (transitive coverage), or only a chapter-dir
sibling? If the latter, the 839-file library tree — where most formalization lives — escapes the §7c
mechanical sweep entirely. This must be confirmed before any claim that the tree is "uncovered" is made
durable. **Tracked for the bean.**

## Finding 2 — a grep heuristic is a triage aid, NOT a verdict (no over-claim)

The enhanced `scripts/check-sidecars.sh` (this branch) flags two leak classes on library Lean:
**MIXED** (a file with both generic `{R}`/`CommRing` and archimedean `: ℝ`/`Real.*`/`linarith`
markers → the wall-side "split per §7c" signal) and **ℝ-in-algebraic-path** (archimedean markers in a
dir like `BraidKnot/`, `HeckeAlgebra/`). A whole-tree sweep produced **96 flags** (~17 MIXED).

**96 is NOT 96 violations.** Per the AGENTS.md "refuted/ruled-out" discipline, a flag is not a finding
until verified:

- The `ℝ-in-algebraic-path` heuristic **over-fires**: `BraidKnot/` is a catch-all that holds
  legitimately-archimedean files — `QRogersPentagonArchimedean`, the `QBeta*` ladder (Q_β is an
  archimedean observable), `PerNucleusMassDerivation`, the dilog files. ℝ there is correct.
- The strongest MIXED candidate — **`Mathlib/HeckeAlgebra.lean` (2003 lines, 44 generic / 7
  archimedean markers)** — was **verified legit-by-design**: a generic Hecke-algebra core *plus* an
  intentional concrete ℝ realization (`H2.markovTrace (q : ℝ)`, `nlinarith [sq_nonneg q]` positivity,
  `linarith` Poincaré-non-vanishing). §7c would *prefer* this split into two files, but it is a
  deliberate structure, **not** a gratuitous-ℝ bug. Splitting a 2003-line file with many downstream
  importers is a major refactor, not a clean win.

So the 96/17 are a **review queue** requiring per-file judgment, not a fix list. The one genuinely
clean bug (the small, purely-ℝ, purely-algebraic `TauQuantumIntegerForm.lean`) is **already fixed**
(#2782). No mass-refactor is warranted here.

## Conclusion + the proper fix

- **`check-sidecars.sh` is right-sized for its real use** — PER-COMMIT, on an agent's 1–5 changed
  files: there the flags are a genuine review prompt (it caught both the `TauQuantumIntegerForm`
  gratuitous-ℝ and a `norm_num`-in-generic-file slip in #2782). The over-firing only appears on a
  whole-tree sweep, which is not how the tool is used. A calibration note was added to the script.
- **The systematic fix is NOT a grep sweep.** It is: (1) confirm whether the per-block
  `q-usage`/`wall-side` checker reads the resolved library-tree Lean; (2) if not, extend it to do so
  (it already has the per-block regime logic — chapter→expected-regime profile — that a path heuristic
  only crudely approximates); (3) triage the MIXED review queue with that real per-file judgment.
  This is a `folio-assistant` pipeline change. **Bean'd** (see `.beans/`).

## Checker-extension spec (turn-key — for when `folio-assistant` is in scope)

The proper fix lives in `litlfred/folio-assistant` (the checkers moved there in miga). That repo is
**not reachable from a `qou`-scoped session** — the egress proxy returns a 403 policy denial on
`git clone …/folio-assistant.git`, and the `add_repo`/`list_repos` tools are absent here (attempted
2026-06-25). When the repo is in scope, this is the change:

1. **Confirm the gap first.** In `folio-assistant`, read `content/pipeline/qa-checkers-q-usage.ts`
   (`qa-checkers-voice.ts` for `checkWallSide`) and find how it loads the block's Lean source. If it
   reads only the **chapter-dir sibling** `<rootName>.lean`, then every block whose `lean.ref` resolves
   via **candidate-2** (`<lakeRoot>/<Decl/Path>.lean` in the library tree — the common case, e.g.
   `ref: "qou:QOU.BraidKnot.…"`) is audited against a **non-existent or stub** sibling, i.e. unswept.
2. **Resolve through the real `lean.ref` logic.** Have the checker call the same `parseLeanRef()` /
   resolution the pipeline uses (sibling → `<lakeRoot>/<Decl/Path>.lean` → grep fallback) and run the
   regime / wall-side detection on the **resolved** file's content. This brings the 839 library files
   under the per-block audit with the **content-based** regime detector (not a path grep).
3. **Use the existing regime profile, content-not-path.** `CHAPTER_EXPECTED_REGIMES` keys off the
   content block's **chapter** (already correct: categorical chapters expect `generic-R`, archimedean
   expect `ℝ`). Because resolution maps library-tree decls back to their owning block, the chapter
   profile applies automatically — no fragile lean-tree-dir heuristic needed (the `BraidKnot/`
   catch-all over-fire in `check-sidecars` is exactly what this avoids).
4. **Triage the true list.** Re-run; the output is the **content-verified** violation set (expected to
   be a small fraction of the 96 grep flags). Triage with real judgment; split genuine mixed files,
   generalise genuine gratuitous-`ℝ`, leave the legit-by-design ones (e.g. `Mathlib/HeckeAlgebra.lean`).

Until then, `check-sidecars.sh` (this PR) is the authoring-time stopgap, and the one known clean bug is
already fixed (#2782).

## Cross-references
- [`docs/audits/2026-06-25-z2bn-pf-monodromy-synthesis.md`](2026-06-25-z2bn-pf-monodromy-synthesis.md) — the §7c fix (#2782) that triggered this.
- `AGENTS.md §7c` (base-ring convention), §"QA is agent-owned; CI is a backup".
- [`.claude/skills/local/formalizer.md` §Pre-commit base-ring GATE](../../.claude/skills/local/formalizer.md).
- [`.claude/skills/local/q-usage-watcher.md`](../../.claude/skills/local/q-usage-watcher.md) — the per-block checker with the regime profile to extend.
