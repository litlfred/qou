# Running-example placement audit: where the SU(2) example starts, and which definitions lack their `ex:*-su2`

**Date:** 2026-09-15 · **Bean:** `qou-zq1r` · **Branch:** `claude/chi-arc-e3-followups-2026-09-15` · **Session:** `qou-dgce`

The style guide's primary reader (a second-year graduate student, `.claude/skills/local/one-voice-style-guide.md` §The primary reader) is served by one running example, $G = \mathrm{SU}(2)$, threaded through the foundational chapters as `ex:<block>-su2` blocks. This audit measures (a) how many such blocks exist and whether the block each one interprets points back to it through its `examples[]` field, and (b) which definitions in the three foundational chapters have no SU(2) example at all. Measured with a Python walk over every `content/quantum-observable-universe/*/*.ts` manifest on this branch; the script is inline in the session transcript and takes ten lines, so it is re-runnable from this description.

## 1. Where the example starts

The first `ex:*-su2` block in reading order is `ex:rigid-monoidal-vect` → `ex:quantum-universe-su2` (chapter 1, section "Uniqueness and the SU(2) realisation"), which verifies axioms (i)–(iv) of `def:quantum-universe` for $\mathrm{Rep}(\mathrm{SU}(2))$ and now continues in `ex:su2-characters-and-quantum-dimension` (characters, the two evaluations of the Chern character). The example therefore starts *after* the definition it illustrates and in the same section, which is the placement the style guide asks for.

Its Lean sibling `quantum-universe-su2.lean` packages the data as a record `SU2QuantumUniverseData` (dimension of the Lie algebra, faithfulness of the fibre functor) rather than as an instance of the library structure `QOU.QuantumUniverse` in `CategoricalFoundations.lean`. The `lean.ref` `qou:QOU.Examples.su2QuantumUniverse` resolves to that sibling (an earlier entry on the bean said it was dangling; that was a grep restricted to `lean/QOU/` and is corrected on the bean). The running example is not yet a `QuantumUniverse ℂ` in the library's sense — that is the one Lean gap in the example's spine, and it is not small (it needs $\mathrm{Rep}(\mathrm{SU}(2))$ as a braided pivotal category with its Wedderburn blocks).

## 2. Back-links from the interpreted block (measured, then fixed on this branch)

| quantity | count |
|---|---:|
| `ex:*-su2` blocks in the paper | **35** |
| … whose interpreted block did **not** list them in `examples[]` (before this branch) | **14** |
| … after this branch | **1** (`ex:tannaka-krein-su2` → `conj:tannaka-krein-isomorphism`: the conjecture schema declares no `examples[]` field, so the back-link cannot be recorded there; the example's own `interprets:` is the only edge) |

The fourteen were: `ex:braid-group-su2` → `def:braid-group`; `ex:brane-boundary-su2` → `def:brane-boundary`; `ex:categorical-connection-su2` → `def:categorical-connection`; `ex:descent-eigenspaces-su2` → `prop:descent-eigenspaces`; `ex:descent-involution-su2` → `def:descent-involution`; `ex:descent-lemma-su2` → `lem:descent`; `ex:direct-limit-algebra-su2` → `def:direct-limit-algebra`; `ex:frobenius-relation-su2` → `prop:frobenius-relation`; `ex:mass-identity-su2` → `def:mass-identity`; `ex:positive-dagger-su2` → `prop:positive-definite-dagger`; `ex:tannaka-krein-su2` → `conj:tannaka-krein-isomorphism`; `ex:topological-mass-su2` → `thm:topological-mass`; `ex:vacuum-state-su2` → `prop:vacuum-state`; `ex:weight-decomposition-su2` → `thm:weight-decomposition-exists`. Thirteen `examples[]` entries were added mechanically (the field created where absent); the fourteenth target is a `conjecture`, whose schema has no such field; this is the corpus agreeing with itself — the example already declares `interprets:` — and is the kind of change the 2026-09-07 ask-first rule exempts (derived from the corpus).

## 3. Definitions without an SU(2) example, by chapter

| chapter | definitions | with an `ex:*-su2` | lacking |
|---|---:|---:|---|
| quantum-universes | 15 | 6 | `def:categorical-jet`, `def:chern-character`, `def:fundamental-object`, `def:grothendieck-group-of-a-qou`, `def:hochschild-homology`, `def:poisson-object`, `def:rigid-monoidal-category`, `def:snake-identity`, `def:tannaka-dual` |
| quantum-observable-universes | 37 | 6 | 31 (see below) |
| lifting-and-descent | 13 | 6 | `def:arc-space`, `def:categorical-q-reeb-flow`, `def:ccg-cosimplicial-identities`, `def:localized-knot`, `def:motivic-galois-character`, `def:motivic-substrate`, `def:yekutieli-triple` |

The 31 in the QOU chapter: `brings-coordinate-ring`, `categorical-dirac-operator`, `categorical-fourier`, `categorical-instanton`, `categorical-lagrangian`, `categorical-laplace`, `categorical-point`, `categorical-q-connection`, `categorical-q-ext-deriv`, `categorical-q-lie-bracket`, `categorical-reeb-derivation`, `commutative-qou`, `contact-affine-chart`, `exceptional-divisor`, `fermion-boson-decomposition`, `frobenius-hopf-substrate`, `observation`, `q-deformed-commutator`, `q-dilogarithm`, `q-exponential`, `q-harmonic-form`, `q-heat-equation`, `q-hodge-star`, `q-logarithm`, `q-resolvent`, `quantum-flatness`, `quantum-gauge-group`, `quantum-planck-constant`, `rigid-dualizing-complex`, `substrate-parameter-planck`, `weight-decomposition`.

Three qualifications, so the counts are not over-read. First, `def:chern-character`, `def:grothendieck-group-of-a-qou` and `def:hochschild-homology` are new on PR #7426 and are covered by `ex:su2-characters-and-quantum-dimension`, which `interprets` the first of them; the walk counts an example against exactly one block. Second, `def:rigid-monoidal-category` is covered by `ex:rigid-monoidal-vect`, which is the SU(2) example under another name. Third, several QOU-chapter definitions are $q$-calculus primitives (`q-exponential`, `q-logarithm`, `q-dilogarithm`, `q-deformed-commutator`) for which "the SU(2) example" is the evaluation on a single generator and would be a one-line block; the reader is better served by the worked examples in the tensor-picture blocks of the mass chapter.

## 4. What this audit does and does not decide

It establishes the coverage numbers and repairs the back-links. It does **not** write the missing examples: which of the 47 uncovered definitions deserve an SU(2) example is an editorial choice about the reader's path, and the style guide's rule ("examples are the reader's own") argues for the ones that touch second-year material first — `def:categorical-point` (points of $\mathrm{Spec}\,\mathcal{O}(\mathrm{SU}(2))$ are group elements), `def:categorical-reeb-derivation` (the Reeb field of the Hopf fibration), `def:fundamental-object` ($V = \mathbb{C}^{2}$), `def:tannaka-dual` (Tannaka–Krein for a compact group), `def:weight-decomposition` (weights of $V_n$). Those five are the recommendation, recorded on bean `qou-zq1r`; they are queued, not written.
