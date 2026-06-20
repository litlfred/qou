# Archimedean dependency + existence/uniqueness audit (2026-04-17)

Two parallel audits of the Quantum Observable Universe paper, run on
branch `claude/categorical-exponentials-finite-fields-31vfI`:

1. **Archimedean hygiene** — where does the paper genuinely need
   $\mathbb{R}$/$\mathbb{C}$/Haar/norms vs. where is the commitment
   premature?
2. **Existence/uniqueness companions** — which categorical
   definitions lack `prop:<name>-exists` and `prop:<name>-unique`
   propositions (with Lean proofs) needed to make the universal-
   property definition well-posed?

---

## 1. Archimedean dependency audit

### 1.1 Verdict: EXCELLENT

The paper is remarkably clean about the archimedean/categorical
separation. Core definitions (Chs 1–5) are base-ring independent;
archimedean commitment is appropriately deferred to the CR-geometry
realisation in Ch 6 (`c-quantum-universe.md`,
`c-quantum-observable-universe.md`) and convergence-dependent
results in Ch 9 (information theory).

### 1.2 Chapter-by-chapter

| Chapter | Archimedean status |
|---------|-------------------|
| Ch 1 Quantum Universes | Fully categorical |
| Ch 2 Quantum Observable Universes | Fully categorical (post three-context refactor) |
| Ch 3 Fluid dynamics | Categorical core; q-NS well-posedness uses algebraic damping, not topological completeness |
| Ch 4 Braids/knots | Categorical; Hecke algebra is base-ring-independent formal object |
| Ch 5 Lifting/descent | Mostly categorical; `yekutieli-archimedean-band.md` needs scope clarity |
| Ch 6 Descartes universe / Bring | Categorical with explicit CR realisation |
| Ch 7 Physical observations | **First mandatory archimedean commitment** |
| Ch 8 Glossary | Mathlib wrappers; N/A |
| Ch 9 Information theory | Needs $\mathbb{C}/\mathbb{R}$ for heat kernel, Julia set |

### 1.3 First mandatory archimedean commitment

**Ch 6 `c-quantum-universe.md`**: requires CR manifold, Levi form,
pseudo-Hermitian structure — intrinsically $\mathbb{C}$.
**Justified**: this IS the archimedean realisation, not the abstract
theory. Readers who want finite-field / $p$-adic universes can stop
after Ch 5 with a complete theory.

### 1.4 Top 5 de-archimedeanisation candidates

| # | File | Issue | Fix |
|---|------|-------|-----|
| 1 | `lifting-and-descent/yekutieli-archimedean-band.md` | Unclear if intrinsic | Audit content; mark as realisation remark |
| 2 | `lifting-and-descent/weight-decomposition-su2.md` (Step 2) | Torus integral in definition proof | Move integral to "archimedean verification" remark |
| 3 | `quantum-observable-universes/levi-generalisation.md` lines 18–26 | Mixes categorical $q(p)$ and Levi realisation | Separate the two |
| 4 | `models-of-qous/q-yang-mills-levi.md` | Possible categorical/Levi conflation | Review and split if needed |
| 5 | `information-theory/q-exponential-taylor.md` | Taylor convergence proof | Already categorical; confirm |

---

## 2. Existence/uniqueness companion audit

### 2.1 Verdict: CRITICAL GAP

Only 3 definitions paper-wide have existence companions (1 fully
proved, 2 axiomatic). **Zero uniqueness companions.** For
universal-property definitions ("the unique X such that P"), this is
a foundational hole — the definition is not well-posed without
existence + uniqueness.

### 2.2 Complete definitions

| Definition | Exists companion | Unique companion |
|------------|------------------|------------------|
| `def:weight-decomposition` | `thm:weight-decomposition-exists` ✓ | ✗ |
| `def:categorical-reeb` | `thm:categorical-reeb-exists` ⚠ (axiom) | ✗ |
| `def:substrate-parameter` | `thm:substrate-parameter-exists` ⚠ (depends on Reeb axiom) | ✗ |

### 2.3 Top 10 priority gaps (pre-Phase-1)

| # | Definition | Deps | Missing |
|---|------------|------|---------|
| 1 | `def:categorical-reeb` | 17 | `-unique` (exists is axiom) |
| 2 | `def:quantum-observable-universe` | 46 | both |
| 3 | `def:frobenius-pairing` | 32 | both |
| 4 | `def:mass-identity` | 31 | both |
| 5 | `def:quantum-characteristic-classes` | 34 | both |
| 6 | `def:categorical-q-ext-deriv` | 14 | both |
| 7 | `def:categorical-action` | 14 | both |
| 8 | `def:categorical-proton` | 15 | both |
| 9 | `def:categorical-instanton` | 11 | both |
| 10 | `def:q-exponential` | — | both |

### 2.4 Phase 1 work (this branch)

Created on branch
`claude/categorical-exponentials-finite-fields-31vfI`:

| Block | Status |
|-------|--------|
| `prop:q-exponential-exists` | Created (.ts/.md/.lean) |
| `prop:q-exponential-unique` | Created (.ts/.md/.lean) |
| `prop:q-logarithm-exists` | Created (.ts/.md/.lean) |
| `prop:q-logarithm-unique` | Created (.ts/.md/.lean) |
| `prop:frobenius-pairing-exists` | Created (.ts/.md/.lean) |
| `prop:frobenius-pairing-unique` | Created (.ts/.md/.lean) |
| `prop:categorical-reeb-unique` | Created (.ts/.md/.lean) |
| `def:q-resolvent` | Created (.ts/.md/.lean) |

All Lean proofs stubbed with `-- Ref: [kassel1995]` or
`-- Ref: [witten1988]` citations pending Milnor--Moore and q-shuffle
Hopf algebra infrastructure in Mathlib.

### 2.5 Phase 2 work (next branches)

Remaining high-priority gaps, from the top 10:

- `prop:quantum-observable-universe-exists` (instance constructor)
- `prop:categorical-q-ext-deriv-exists` + `-unique`
- `prop:categorical-action-exists` + `-unique`
- `prop:categorical-instanton-exists`
- `prop:mass-identity-exists`
- `prop:categorical-proton-exists`
- `prop:quantum-characteristic-classes-exists`

### 2.6 Uniqueness specifically

Zero uniqueness propositions exist paper-wide. Every universal-
property definition needs one. Standard pattern:
- Take two candidates satisfying the defining property.
- Construct the canonical iso between them from the universal
  property.
- Prove the iso is the identity (or unique up to a scalar in the
  Frobenius case).

This is boilerplate once the existence + universal property are
pinned down.

---

## 3. Notation cleanup (concurrent)

Three collisions on $H_q$ uncovered during this audit:

| Sense | Old | New |
|-------|-----|-----|
| $q$-shuffle Hopf algebra | $H_q$ | $\mathcal{H}_q$ |
| $q$-Hamiltonian | $H_q$ | $\hat{H}_q$ |
| Hook-length product | $H_q(\lambda)$ | (unchanged; always with arg) |

Notation register updated in `AGENTS.md §7aa`. Rename applied across
all shuffle-Hopf-algebra `.md` files and Lean comments.

---

## 4. Three-context $p$-adic extensions (concurrent)

Added $\mathbb{F}_p$ / $\mathbb{Q}_p$ / $\mathbb{C}_p$ treatment to:
- `q-exponential.md` (via `rem:q-exp-finite-field-obstruction`,
  new `rem:q-exp-p-adic`)
- `q-logarithm.md`
- `q-dilogarithm.md`
- `categorical-laplace-transform.md`
- `categorical-fourier-transform.md`

New `def:q-resolvent` with same three-context treatment.
