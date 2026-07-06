# QOU optimization techniques — workplan

Consolidated plan for the four computational improvement techniques
identified for the QOU framework, plus the hybrid procedure required to
make heavy / magic-number atoms tractable. Each technique is mapped to
the parts of the repo that already realize it, the gaps that remain,
and the verification path.

All work lands on `claude/qou-optimization-techniques-tE5KW`.

The four techniques (and the hybrid composition for large atoms):

1. **TM** — Symbolic rewriting → matrix representations (transfer matrices)
2. **DC** — Diagrammatic calculus (Temperley–Lieb / Kauffman / Skein)
3. **BD** — Cellular bases + Wedderburn–Artin block diagonalization
4. **L4** — Lean 4 confluent-decider formalization
5. **MN** — Magic-number folding: TM (local) ∘ BD (global) ∘ DC (Reidemeister)

Each phase is independent enough to pick up cold; phases are ordered by
expected effort and by which downstream phases depend on them.

---

## Phase TM — Transfer-matrix engine consolidation

**Goal:** the inductive 2×2 transfer-matrix evaluator becomes the single
entry point for every per-atom mass / energy computation. Symbolic
GS-string reduction is reserved for normal-form *audits*, not the hot
path.

**Where it lives today:**
- `content/quantum-observable-universe/appendix-transfer-matrices/`
  (notation, knot-pairs, interactions, inductive construction,
  heavy-atom examples, worked examples, completeness)
- `content/quantum-observable-universe/lean/QOU/AtomicMass.lean`,
  `Calculations.lean`, `ArchimedeanMassFormula.lean`

**Gaps to close:**
- TM1. Audit `appendix-transfer-matrices/tm-inductive-construction.md`
  and confirm the `\binom{A}{2}`-step evaluator is stated as the
  canonical complexity bound (not "polynomial-time" hand-wave).
- TM2. Cross-reference `tm-heavy-atom-examples.md` against the
  hybrid recipe in Phase MN — the heavy examples should explicitly
  hand off to a folded shell operator at the first closed shell.
- TM3. Add a `proposition` block bounding the bit-size of intermediate
  entries in `M_2(\mathbb{Z}[q^{\pm 1/2}])` after `k` reductions, so
  TM has a *space* bound, not just a step count.
- TM4. Lean: a `theorem` in `QOU/AtomicMass.lean` (or a new file
  `QOU/TransferMatrix/Bounds.lean`) stating
  `P_N = ∏_{i=0}^{A-2} V_i` where each generator volume
  `V_i = z · (M_i)_{11} + (M_i)_{21}` is read off the inductive
  matrix product `M_i`, with `sorry` permitted only at the
  arithmetic identity.

**Verification:**
- `bun run validate quantum-observable-universe`
- `lake build QOU` (the new bound-statement file must compile)
- Spot-check three worked examples (`tm-worked-examples.md`) end up
  with the same numeric mass as `appendix-atomic-mass-calculations`.

---

## Phase DC — Diagrammatic / Skein evaluator

**Goal:** any time a computation can be answered by Reidemeister moves
or the Skein relation, the pipeline routes through the diagrammatic
evaluator instead of expanding the Hecke word.

**Where it lives today:**
- `content/quantum-observable-universe/braids-and-knots/` (Hecke
  presentation, Skein relation, Jones polynomial)
- `content/quantum-observable-universe/appendix-knot-operations/`
- Lean: `QOU/BraidKnot/`, hooks into `QOU.AtomicMass`

**Gaps to close:**
- DC1. Confirm the Skein convention matches §7a of AGENTS.md
  (`(\sigma_i - q)(\sigma_i + q^{-1}) = 0`, generator `$\sigma_i$`,
  Jones `$J_K(q)$`). Any block still using `$T$`, `$t$`, `$A$`, or
  `$V_K$` is a bug.
- DC2. Add a remark block (with `interprets:` to the Skein
  proposition) stating the Reidemeister-invariance corollary used by
  TM at every crossing. Today this is implicit.
- DC3. Ensure the photon (`0_1`), electron (`3_1`), proton
  (Borromean `B_3`) identifications cite the diagrammatic evaluator
  via `uses[]`, not just the algebraic mass formula.
- DC4. Lean: `QOU/BraidKnot/Skein.lean` should expose
  `skein_relation` as a usable rewriter (not just a stated equation).

**Verification:**
- `bun run validate quantum-observable-universe`
- `lake build QOU`
- `bun run pipeline/find-dangling-remarks.ts` returns clean for the
  braids-and-knots chapter.

---

## Phase BD — Wedderburn / cellular-basis block diagonalization

**Goal:** the projector to (sym, std, alt) blocks is the canonical
preprocessor before any LP/SDP, and is the *only* place where Pauli
exclusion enters the calculation.

**Where it lives today:**
- `content/quantum-observable-universe/appendix-atomic-mass-calculations/amc-wedderburn-method.md`
- The three-invariant atomic mass formula (sym/std/alt traces and
  determinants)
- Lean: `QOU/ChannelSeparation.lean`, `QOU/AtomicMass.lean`

**Gaps to close:**
- BD1. Verify `amc-wedderburn-method.md` states the orthogonality
  of the three blocks as a `proposition` (not a remark) with a
  Lean sibling.
- BD2. The LP / SDP sections (Ch 10, §10.29–10.45) should cite the
  block decomposition via `uses[]` so the dependency graph shows the
  preprocessing order.
- BD3. Add a `proposition` linking "fully closed shell" ⇒ "alt
  channel only" — this is the bridge that Phase MN consumes.
- BD4. Lean: `QOU/ChannelSeparation.lean` should export a lemma
  `closed_shell_pure_alt` consumable by `QOU/AtomicMass.lean`.

**Verification:**
- `bun run validate quantum-observable-universe`
- `lake build QOU`
- Channel-separation theorems' `uses[]` reach back to the
  Wedderburn–Artin definition.

---

## Phase L4 — Lean 4 confluent-decider architecture

**Goal:** the GS reduction is *certified confluent* in Lean, so every
optimization above (TM, DC, BD) inherits termination + uniqueness
without re-proving it per call site.

**Where it lives today:**
- `content/quantum-observable-universe/lean/`
  (`Basic.lean`, `Elaboration.lean`)
- `content/quantum-observable-universe/algebraic-substrate/`

**Gaps to close:**
- L41. Audit every `sorry` in QOU/ for the `-- Ref:` citation
  required by §1 of AGENTS.md; flag any without one.
- L42. Confluence statement: a single theorem
  `gs_reduction_confluent` (probably under `QOU/AlgebraicSubstrate/`)
  that TM, DC, and BD can all `import`.
- L43. Wire the package URI: every block citing the confluence
  theorem must use `lean: { ref: "qou:QOU.AlgebraicSubstrate.gs_reduction_confluent" }`.
- L44. Verify root `lake build` (workspace) succeeds, not just per-paper.

**Verification:**
- `lake build` from repo root
- `grep -nR "sorry" content/quantum-observable-universe/lean/ | grep -v "Ref:"` returns nothing
  (or only entries with `-- Ref:` on the previous line).

---

## Phase MN — Magic-number / heavy-atom hybrid

**Goal:** make the inductive procedure described in the second message
explicit in the manuscript and in Lean. This is the composition

```text
add nucleon → reduce to NF (TM) → if shell closes: fold to T_{2,k} (DC) → reproject (BD)
```

and is the technique that keeps `A` up to ~250 tractable.

**Where it lives today:**
- `appendix-atomic-mass-calculations/amc-method.md` (general method)
- `appendix-transfer-matrices/tm-heavy-atom-examples.md` (worked
  heavy nuclei)
- `appendix-knot-periodic-table/` (shell structure)

**Gaps to close — primary deliverables:**
- MN1. New `proposition` block:
  `prop:magic-shell-folding` — "after a closed shell, the next
  nucleon interacts with a single torus-knot operator `$T_{2,k}$`
  (where `$k$` is the shell size) instead of `k` individual
  generators". `.ts` + `.md` + `.lean` triple, under
  `appendix-knot-periodic-table/` or
  `appendix-transfer-matrices/`.
- MN2. New `remark` block (with `interprets: "prop:magic-shell-folding"`):
  `rem:palindromic-histogram-test` — operational criterion for
  detecting shell closure (palindrome in NF histogram).
- MN3. New worked example covering one of `Z=2, 8, 20, 28, 50, 82`
  showing the fold step explicitly. Add to
  `tm-heavy-atom-examples.md` or as a new sibling.
- MN4. Tie back: Phase TM's `tm-inductive-construction.md` gets a
  cross-reference (`uses[]`) to MN1 so the `\binom{A}{2}` bound is
  stated as a *worst case* that the fold improves on.
- MN5. Lean: `QOU/AtomicMass/MagicShells.lean` (or extend
  `QOU/AtomicMass.lean`) with `magic_shell_fold` consuming
  `closed_shell_pure_alt` (BD4) and the Skein rewriter (DC4).

**Verification:**
- `bun run validate quantum-observable-universe`
- `lake build QOU`
- `bun run pipeline/find-dangling-remarks.ts` — MN2 must resolve.
- Numeric check: the MN3 worked example produces the same mass as
  the existing AMC pipeline for that isotope (regression test).

---

## Phase order

```text
L4 ──────────┐
             ↓
TM ───→ MN  ←── BD
             ↑
DC ──────────┘
```

L4 is foundational and cheap; do it first. TM, DC, BD are independent
and can be parallelized. MN composes all three and must come last.

## Cross-cutting checks (run after every phase)

- `bun run validate quantum-observable-universe`
- `bun run validate-refs`
- `lake build` (root workspace)
- `bun run pipeline/find-dangling-remarks.ts`
- `bun run pipeline/prune-transitive-deps.ts --check`

## Out of scope for this branch

- Folio-assistant UI changes (no viewer routes touched).
- Bibliography additions beyond what the new MN propositions require.
- Any edits to whitelist files (`deploy/google-viewers.txt`,
  `deploy/github-collaborators.txt`, `.github/CODEOWNERS`).
