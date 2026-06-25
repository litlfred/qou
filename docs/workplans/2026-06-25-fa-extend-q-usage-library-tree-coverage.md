# Task for a `folio-assistant` agent: extend the §7c QA checkers to cover the qou Lean **library tree**

**Audience:** an agent working in **`litlfred/folio-assistant`** (the platform repo that holds the
content pipeline + QA checkers). You likely have **no `qou` context** — this doc is self-contained.

**Origin:** raised from `litlfred/qou` (audit
`docs/audits/2026-06-25-lean-library-tree-7c-coverage-gap.md`, PR #2789). It could not be done in the
qou session because `folio-assistant` is outside that session's repo scope (egress proxy 403s the
clone). Do it here, where the checkers live.

---

## 1. The problem (one paragraph)

`qou` enforces a **base-ring convention** ("§7c"): a Lean declaration that holds over a generic
commutative ring must be stated over a type variable `{R : Type*} [CommRing R]` / `[Field R]`, **not**
silently specialised to `ℝ`. `ℝ` is reserved for genuinely archimedean constructs (`Real.sqrt`,
ordering `0 < q`, `linarith`/`positivity`/`nlinarith`/`norm_num`, CODATA literals). Two QA criteria
encode this — `q-usage-archimedean-in-categorical-chapter` (in `qa-checkers-q-usage.ts`) and
`wall-side-correct` (`checkWallSide` in `qa-checkers-voice.ts`).

**The gap:** those checkers run **per content block** and read the block's Lean **via the block's
`lean.ref`**. A content block's `lean.ref` (format `"qou:QOU.Decl.Path"`) resolves in up to three
ways (qou AGENTS.md §0a):
1. sibling `<rootName>.lean` next to the block's `.md`/`.ts` (chapter dir);
2. **`<lakeRoot>/<Decl/Path>.lean` in the Lean library tree** (`qou/content/quantum-observable-universe/lean/QOU/**`);
3. grep fallback.

In qou, **most formalisation lives in the library tree (candidate 2)** — 839 files — and **none of
them has a co-located `<block>.qa.json` sidecar** (verified: 2280 sidecars exist, 0 inside any `lean/`
tree). So **if the checker reads only the candidate-1 sibling, the entire 839-file library tree is
unswept for §7c.** A gratuitous `(q : ℝ)` already slipped through there (qou #2782 — the
`TauQuantumIntegerForm` τ-kernel lemma; the owner caught it by eye).

---

## 2. Step 1 — confirm the gap (do this first; do not assume)

In `folio-assistant`, read:
- `content/pipeline/qa-checkers-q-usage.ts` (regime detector + `CHAPTER_EXPECTED_REGIMES`)
- `content/pipeline/qa-checkers-voice.ts` → `checkWallSide`
- the `lean.ref` resolver (look for `parseLeanRef` / the resolution that the LaTeX/validate pipeline
  already uses; `schemas/lean-packages.ts` has the package registry `qou`/`ugb`/`fred2005`).

**Determine:** when a block's `lean.ref` resolves via **candidate 2** (library tree, no sibling), does
the checker (a) read and audit that resolved file, or (b) only look for a chapter-dir sibling and audit
nothing / a stub? If (a), coverage already exists — **verify with a spot check** (pick a block whose
`ref` is `"qou:QOU.BraidKnot.…"` and confirm its `q-usage-*`/`wall-side-correct` sidecar reflects the
library file's content) and you may be done. If (b), proceed to Step 2.

---

## 3. Step 2 — the fix

Make the checker audit the **resolved** Lean file:

1. **Resolve through the real `lean.ref` logic** (the same candidate-1 → candidate-2 → grep resolution
   the pipeline already implements — reuse it, don't reinvent). Run the regime / wall-side detection on
   the **resolved file's content**.
2. **Keep the regime profile content-based, NOT path-based.** `CHAPTER_EXPECTED_REGIMES` keys off the
   owning content block's **chapter** (categorical chapters expect `generic-R`/`symbolic`; archimedean
   chapters expect `real-positive`/`fixed-q0`). Because resolution maps a library decl back to the
   block that references it, the chapter profile applies automatically. **Do not** infer the regime
   from the lean-tree directory name.

   > **Why (hard-won, do not skip):** qou tried a directory heuristic as a stopgap
   > (`scripts/check-sidecars.sh`, "ℝ in an algebraic-domain path"). It **over-fired — 96 flags, mostly
   > false** — because `lean/QOU/BraidKnot/` is a **catch-all** holding plenty of *legitimately
   > archimedean* files (`QRogersPentagonArchimedean`, the `QBeta*` ladder, `PerNucleusMassDerivation`,
   > the dilog files). Only the content (what the file actually *proves* + the owning chapter's regime)
   > distinguishes gratuitous-ℝ from legitimate-ℝ.

3. **Optional second mode:** a direct library-tree walk (`lean/QOU/**/*.lean`) that runs the same
   content detector, for files reachable by no block's `lean.ref` (orphan library files). Same
   content-based rule.

---

## 4. Step 3 — run, then triage with judgment (NOT a mass-fix)

Re-run the q-usage / wall-side audit across the qou corpus. The output is the **content-verified**
violation set — expected to be a **small fraction** of the 96 raw grep flags.

**Triage discipline (qou's "refuted/ruled-out" + "over-claim" rules apply):**
- A flag is **not** a violation until you confirm the file's *statement* is algebraic yet typed over `ℝ`.
- **Split** a genuine mixed file (both generic and archimedean content) into two files per §7c.
- **Generalise** a genuine gratuitous-`ℝ` decl to `{R}`/`[Field R]`.
- **Leave legit files alone.** Worked examples from the qou audit:
  - **Clean bug (fix):** `QOU/Mass/TauQuantumIntegerForm.lean` — small, purely-ℝ, purely-algebraic
    (`det = 1` is `CommRing`-universal; the bar-even `[2]_q` identity is over `ℚ(q)`). *Already fixed in
    qou #2782* — use it as the positive example.
  - **Legit-by-design (do NOT flag):** `QOU/Mathlib/HeckeAlgebra.lean` (2003 lines) — a generic Hecke
    core **plus an intentional concrete ℝ realisation** (`H2.markovTrace (q : ℝ)`,
    `nlinarith [sq_nonneg q]` positivity). §7c would *prefer* a split, but it is deliberate, not a bug;
    splitting a 2003-line file with many importers is out of scope for an audit pass.

Do **not** declare "N violations" from raw counts — that is the over-claim qou's disciplines forbid.

---

## 5. Deliverable + coordination

- A `folio-assistant` PR: the checker change + (if you ran the audit) the triaged fixes to qou Lean, or
  a short report of the verified violation list if the fixes belong in a qou PR.
- Land a **new criterion or extended scope note** in `qa-criteria-registry.ts` if the coverage change
  warrants it, and bump the relevant `script_hash` (a checker-logic change invalidates cached sidecar
  entries — treat as a full re-sweep, per qou's `q-usage-watcher` skill §Slot I).
- Comment back on qou PR #2789 / the audit doc so the qou side can close the follow-up.

## 6. References (in qou; ask if you cannot see them)

- `docs/audits/2026-06-25-lean-library-tree-7c-coverage-gap.md` — the audit that raised this.
- `AGENTS.md §7c` (base-ring convention) and §"QA is agent-owned; CI is a backup".
- `.claude/skills/local/q-usage-watcher.md` — the checker's behaviour, the q-regime taxonomy, the
  `CHAPTER_EXPECTED_REGIMES` partition, and the dispensation mechanism.
- `.claude/skills/local/formalizer.md` §"Base ring convention" + §"Pre-commit base-ring GATE".
- `scripts/check-sidecars.sh` — qou's authoring-time stopgap (per-commit); shows the path heuristic to
  *avoid* in the real checker.
