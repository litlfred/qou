# Handover: ~19 substantive naked conjectures lack class-axiomatised Lean stubs

**REVISION (2026-05-18 round 2):** the original handover counted
32, but a follow-up discovery refinement (testing `lean.ref`
resolution via namespace-walk of the matching Lean file, NOT
just sibling `.lean` presence) found that:

| Class | Count | Action |
|-------|------:|--------|
| `lean.ref` resolves correctly, declaration exists, watcher discovery was wrong | 8 (BraidKnot + StaircaseCornerHook) | Queue clears as `wontfix-already-resolved`; no action |
| `lean.ref` namespace was wrong, declaration exists | 5 (4 q-gl in #707, 1 q-clt in #712) | Fixed in PRs |
| Genuinely naked (no Lean anywhere) | **~19** | **Real formalizer dispatch needed** |

This handover doc's per-chapter listing below is from the
**original** 32-item count. The ~19 actually-naked subset is a
strict subset of that listing, modulo the 8 BraidKnot / Staircase
items that are already wired and should be skipped.

**Scope:** every `conjecture`-kind content block under
`content/quantum-observable-universe/` whose `.ts` manifest does
NOT carry the `open-problem` tag, is NOT a famously unsolved
millennium-style problem, AND has no resolvable `lean.ref`. These
are the *real research conjectures* that the framework states and
treats as anchors, but for which no class-axiomatised Lean
encoding (per AGENTS.md §3b-cond) exists yet.

**Discovered by:** `proof-integration-watcher` backlog sweep on
2026-05-18 (refined heuristic, round 2).

**Severity:** major — these conjectures are part of the paper's
framework but lack the Lean-class scaffolding that would let
**downstream conditional theorems** type-check against them
(per the conditional-class exception in AGENTS.md §3b-cond).

**Estimated effort:** ~30 minutes per block to author a
class-axiomatised stub (no proof — just the `class C { … : sorry }`
shape with the conjecture's content as fields). ~19 blocks →
~10 hours total, split across chapters.

**Sibling references for the refinement work:**
- #707 (4 q-gl `lean.ref` namespace fixes + new `q_gl_kummer_filtration`)
- #712 (1 q-clt `lean.ref` namespace fix + watcher Slot G refinement)

## What the watcher found

After filtering the 65 raw `naked-conjecture` queue items:

- **33 dropped** as `open-problem`-tagged or famously unsolved
  (RH, P=NP, BSD, Collatz, Yang-Mills mass gap, etc.)
- **32 substantive** remain — listed below by chapter.

The watcher attempted §4d Auto-discharge ("naked conjecture
special case: attempt discharge via `local/formalizer` +
`local/lean-generation` before defaulting to author-assist") but
reading the top 3 by tractability
(`complex-chirality-rotation`, `q-oper-hecke`,
`electron-shells-hopf`) showed they are **substantive research
conjectures**, not lazy placeholders. The mission clause *"if a
conjecture is a placeholder for something to be proved, try"*
does not apply — these are real conjectures.

The right next step per AGENTS.md §3b-cond is **class
axiomatisation**, not full proofs.

## Suggested approach

For each block:

1. Read the `.md` to extract the conjecture's content (what
   functor / map / inequality / equation is being asserted).
2. Write a Lean `class C { … }` whose fields encode that content,
   each field's body being `sorry` (the conjecture proper, per
   §3b-cond).
3. Cite the conjecture's bibliographic source in a `-- Ref:`
   above each `sorry`.
4. Optionally, write a `theorem c_class_inhabited : C M :=
   ⟨…⟩` instance whose existence is the conjecture; this lets
   downstream blocks take `[C M]` as a hypothesis.

This is **not** the same as proving the conjecture. It's
encoding it in Lean so that:

- The paper's logical dependence on the conjecture is auditable
  (Lean tracks who consumes the `[C M]` class).
- Downstream blocks can be rigorous-conditional theorems per
  AGENTS.md §3b-cond.
- A future agent (or human) attempting a proof has a Lean
  target with a well-typed statement.

## Specialist skill recommended

`local/formalizer` (collaborator role) — designed for exactly
this kind of "write the Lean shape, leave the math as sorry"
work. Optionally followed by `local/lean-generation` if any of
the conjectures' `uses[]` cone is itself partially formalised
and could provide structural hints.

## Acceptance criteria

For each block:

- [ ] `.lean` sibling exists at `content/<paper>/<chapter>/<block>.lean`
- [ ] Lean file declares a `class` (or `axiom` per §3b-cond
      pattern) encoding the conjecture's content as fields
- [ ] Every `sorry` (one per class field) carries a `-- Ref:`
      citation to the bibliographic entry in
      `content/schema/references.ts`
- [ ] The block's `.ts` manifest's `lean.ref` is updated to
      point at the new declaration (per the Lake package
      registry in `folio-assistant/schemas/lean-packages.ts`)
- [ ] `cd content && bun run validate quantum-observable-universe`
      remains clean (the `lean-ref-resolves` rule must pass)
- [ ] Conditional-class banner audit (`bun run
      content/pipeline/conditional-class-banner-audit.ts
      --strict`) remains clean

Aggregate:

- [ ] CI green on the PR (or §5f flake documented)
- [ ] One-voice sweep applied to any `.md` edits (most blocks
      shouldn't need new narrative)
- [ ] Per-chapter PR (not one giant PR): one focused PR per
      chapter so reviewers can absorb the framing in context

## Per-chapter listing

- Recommended approach: dispatch `local/formalizer` for class-axiomatised Lean stubs (per AGENTS.md §3b-cond), NOT full proofs.

## Per-chapter listing

### `braids-and-knots` (18 blocks)

| Label | Title | .md lines |
|-------|-------|----------:|
| [`conj:bring-figure-eight-depth-2-witness`](../../content/quantum-observable-universe/braids-and-knots/bring-figure-eight-depth-2-witness.md) | Bring figure-8 volume as depth-2 grouplike value (50-digit numerica... | 104 |
| [`conj:bring-trilog-depth-3-witness`](../../content/quantum-observable-universe/braids-and-knots/bring-trilog-depth-3-witness.md) | Bring trilog at $\\zeta_5$ as depth-3 grouplike value (50-digit fun... | 131 |
| [`conj:cemetery-group-emergence`](../../content/quantum-observable-universe/braids-and-knots/cemetery-group-emergence.md) | Cemetery group as the kernel of the observation functor | 46 |
| [`conj:confinement-grading-correspondence`](../../content/quantum-observable-universe/braids-and-knots/confinement-grading-correspondence.md) | Confinement levels coincide with KLR $\\mathbb{Z}$-grading shifts | 37 |
| [`conj:confinement-nf-structure-forcing`](../../content/quantum-observable-universe/braids-and-knots/confinement-nf-structure-forcing.md) | Confinement → NF-structure forcing: $\\mathrm{shift}_{\\mathrm{NF}}... | 75 |
| [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/braids-and-knots/crystal-graph-realization.md) | Hecke normal forms realise crystal highest-weight vectors | 47 |
| [`conj:gs-archimedean-agreement-residue`](../../content/quantum-observable-universe/braids-and-knots/gs-archimedean-agreement-residue.md) | Archimedean agreement (proton instance): degree-48 Habiro trace at ... | 73 |
| [`conj:gs-archimedean-agreement-trace`](../../content/quantum-observable-universe/braids-and-knots/gs-archimedean-agreement-trace.md) | Archimedean agreement: Habiro polynomial trace evaluates to GB mass | 71 |
| [`conj:gs-graded-markov-trace-existence`](../../content/quantum-observable-universe/braids-and-knots/gs-graded-markov-trace-existence.md) | Existence of the graded Markov trace on the GS filtration | 68 |
| [`conj:gs-residue-at-root-existence`](../../content/quantum-observable-universe/braids-and-knots/gs-residue-at-root-existence.md) | Existence of the cyclotomic residue at each filtration level | 66 |
| [`conj:gs-spectral-decomposition-existence`](../../content/quantum-observable-universe/braids-and-knots/gs-spectral-decomposition-existence.md) | Spectral decomposition of the mass into descended trace and residue... | 64 |
| [`conj:gs-spectral-sum-finite`](../../content/quantum-observable-universe/braids-and-knots/gs-spectral-sum-finite.md) | Finiteness of the GS residue spectral sum | 73 |
| [`conj:hecke-anyonic-substrate`](../../content/quantum-observable-universe/braids-and-knots/hecke-anyonic-substrate.md) | Iwahori–Hecke algebra is the anyon algebra: every QOU particle is a... | 37 |
| [`conj:jet-convergence-classical-limit`](../../content/quantum-observable-universe/braids-and-knots/jet-convergence-classical-limit.md) | Jet-filtered knot invariant converges to classical dimension-weight... | 143 |
| [`conj:kazhdan-lusztig-classical-limit`](../../content/quantum-observable-universe/braids-and-knots/kazhdan-lusztig-classical-limit.md) | As $q \\to 1$, the KLR canonical basis flattens to the Kazhdan–Lusz... | 50 |
| [`conj:root-of-unity-mtc-truncation`](../../content/quantum-observable-universe/braids-and-knots/root-of-unity-mtc-truncation.md) | At $q = e^{2\\pi i / k}$, the KLR algebra truncates to a Modular Te... | 41 |
| [`conj:staircase-ew-residual`](../../content/quantum-observable-universe/braids-and-knots/staircase-ew-residual.md) | Staircase EW-residual: $q^{1/(2k-1)}$ as pairwise eigenvalue ratio ... | 69 |
| [`conj:symmetric-crystal-pair-production`](../../content/quantum-observable-universe/braids-and-knots/symmetric-crystal-pair-production.md) | Type-B folding forces matter/antimatter to be created in conjugate-... | 57 |

### `descartes-universe` (3 blocks)

| Label | Title | .md lines |
|-------|-------|----------:|
| [`conj:electron-shells-hopf`](../../content/quantum-observable-universe/descartes-universe/electron-shells-hopf.md) | Electron shells as closed sub-Hopf links of the trefoil chain | 129 |
| [`conj:elliptic-stability-locus`](../../content/quantum-observable-universe/descartes-universe/elliptic-stability-locus.md) | The nuclear degeneracy locus is an elliptic curve over the Bring's ... | 217 |
| [`conj:skein-shell-correction`](../../content/quantum-observable-universe/descartes-universe/skein-shell-correction.md) | Shell corrections from Skein polynomial factorization of the multi-... | 138 |

### `information-theory` (2 blocks)

| Label | Title | .md lines |
|-------|-------|----------:|
| [`conj:aeon-boundary-generates-chart`](../../content/quantum-observable-universe/information-theory/aeon-boundary-generates-chart.md) | Aeon recycling: $\\Phi_1^q \\circ \\mathrm{CMB}$ lands in $\\mathrm... | 65 |
| [`conj:quantum-computational-universality`](../../content/quantum-observable-universe/information-theory/quantum-computational-universality.md) | Quantum computational universality via descent to roots of unity | 82 |

### `observations` (4 blocks)

| Label | Title | .md lines |
|-------|-------|----------:|
| [`conj:complex-chirality-rotation`](../../content/quantum-observable-universe/observations/complex-chirality-rotation.md) | Chirality as continuous phase rotation in the pre-observable sector | 66 |
| [`conj:higgs-t28`](../../content/quantum-observable-universe/observations/higgs-t28.md) | The Higgs boson as $T(2,8)$: the link spanning three exceptional di... | 104 |
| [`conj:q-clt-non-commutative`](../../content/quantum-observable-universe/observations/q-clt-non-commutative.md) | q-Central Limit Theorem for Hecke transfer matrices — categorical q... | 127 |
| [`conj:shell-threading-energy`](../../content/quantum-observable-universe/observations/shell-threading-conjecture.md) | Shell energy from the Skein smoothing at the beta-decay vertex | 175 |

### `particle-interactions` (1 blocks)

| Label | Title | .md lines |
|-------|-------|----------:|
| [`conj:periodic-table-demand`](../../content/quantum-observable-universe/particle-interactions/periodic-table-demand-conjecture.md) | The valley of stability is the demand-minimizing locus in $(Z, N)$-... | 91 |

### `q-geometric-langlands` (4 blocks)

| Label | Title | .md lines |
|-------|-------|----------:|
| [`conj:q-gl-classical-limit`](../../content/quantum-observable-universe/q-geometric-langlands/q-gl-classical-limit.md) | Classical limit of the $q$-Geometric Langlands correspondence | 25 |
| [`conj:q-gl-fiber-functor`](../../content/quantum-observable-universe/q-geometric-langlands/q-gl-fiber-functor.md) | Fibre-functor mediation of the $q$-Langlands correspondence | 24 |
| [`conj:q-gl-kummer-filtration`](../../content/quantum-observable-universe/q-geometric-langlands/q-gl-kummer-filtration.md) | Kummer filtration on $q$-local systems | 46 |
| [`conj:q-oper-hecke`](../../content/quantum-observable-universe/q-geometric-langlands/q-oper-hecke.md) | $q$-Opers are $q$-Hecke eigensheaves | 26 |

