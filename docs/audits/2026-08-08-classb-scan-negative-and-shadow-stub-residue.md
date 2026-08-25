# Class B scan: a negative — plus the residue of the 2026-06-14 shadow drain

**Date:** 2026-08-08
**Skill:** [`local/proof-narrative-lean-equivalence`](../../.claude/skills/local/proof-narrative-lean-equivalence.md)
**Follows:** [`2026-08-08-narrative-lean-equivalence-nonempty-kernels.md`](2026-08-08-narrative-lean-equivalence-nonempty-kernels.md) (the `Nonempty` sweep + its addendum)

## The scan, and why it reports nothing new

Having landed the `A2 — Nonempty X kernels` sub-signature, the obvious next
pass was **Class B (scope mismatch)** — the class the `Nonempty` sweep's
addendum turned up one instance of (`quantum-characteristic-classes-exists`:
narrative quantifies over all `n`, Lean is `Nonempty` at one level).

Signature scanned: a `.md` **statement** carrying a universal cue (*for
every / for all / for each / ∀*) whose `.lean` sibling binds **nothing**
universally — no `∀`, no binder. Comments stripped first, `.lake` excluded,
per the A2 triage rules.

**27 candidates. Zero new findings.** Every candidate collapsed into one of
two already-catalogued classes:

| pattern | already recorded in |
|---|---|
| `class C where holds : Prop` — a carrier asserting nothing | [`2026-06-07-klr-gs-order-formalization-plan.md` §Layer 1](2026-06-07-klr-gs-order-formalization-plan.md): *"The current stub `class CrystalGraphRealization where holds : Prop` is vacuous."* Also [`2026-06-24-devils-advocate-wave10.md`](2026-06-24-devils-advocate-wave10.md) (`reduction_holds : Prop`) and [`2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md`](2026-06-01-qhyperbolic-nonabelian-stokes-wiring.md) (catalogues `class … holds : Prop` as *the* conjecture representation). |
| `def X := trivial` sibling shadowing a library decl | [`2026-06-14-lean-vacuous-proof-audit.md` §stub-shadow manifest](2026-06-14-lean-vacuous-proof-audit.md) — 219 stubs, 147 classified SHADOW→delete; codified as AGENTS.md §0a. |

This is the corpus-grep checklist doing its job: the scan's raw output looked
like two fresh systemic defects, and both were known. **Recording the negative
so the next agent running a Class B pass does not re-derive it.**

## The one thing worth acting on: the drain has a residue

The 2026-06-14 manifest prescribed deleting 147 SHADOW stubs. Measured today:

| | 2026-06-14 | 2026-08-08 |
|---|---|---|
| sibling-resolution stub files | 219 | **38** |
| of those, a library decl of the same name exists (SHADOW) | 147 | **13** |

The drain largely ran (~91% of shadows cleared) and stopped short. Of the 13
residual shadows, 8 have a `lean.ref` whose decl path resolves to an existing
library file (candidate 2), making them safe to delete per §0a.

**7 deleted** — each verified to be vacuous (`:= trivial`, or a
`holds : Prop` carrier) *and* to have a real library twin:

| deleted sibling | now resolves to |
|---|---|
| `knots-particles-confinement/quantum-dilogarithm-disambiguation.lean` | `QOU/BraidKnot/QuantumDilogarithm.lean` (`phi_q_ne_li2_q` et al.) |
| `appendix-surreals/birthday-grading.lean` | `QOU/AppendixSurreals/BirthdayGrading.lean` |
| `appendix-surreals/surreal-blowup-calculus.lean` | `QOU/AppendixSurreals/BlowupCalculus.lean` (5 decls, real fields) |
| `information-theory/jet-horizon.lean` | `QOU/JetHorizon.lean` |
| `mass-theory/canonical-braid-interface-composition.lean` | `QOU/BraidKnot/InterfaceComposition.lean` (7 decls) |
| `mass-theory/gs-archimedean-agreement-trace.lean` | `QOU/BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean` |
| `mass-theory/gs-archimedean-agreement-residue.lean` | `…/protonExample/archimedean_agreement.lean` |

**Caveat on the last two.** Their library twins are themselves thin (a
`residual : ℝ` field whose own docstring says *"placeholder shape: refine to
match the actual claim"*). Deleting the shadow is still correct under §0a, but
the honesty gain there is marginal — it replaces a `holds : Prop` with a
slightly-less-empty placeholder, not with a formalisation.

## The near-miss, recorded deliberately

`mass-theory/reidemeister-mass-invariance.lean` was in the safe-delete set on
the first pass and **is not a stub** — it carries a real proof (`obtain` /
`refine` / `div_pos` over `ReidemeisterMassInvarianceContext`). It qualified
only because a library decl shares its name.

**"A library twin exists" is not sufficient grounds to delete a sibling.** The
sibling must independently be verified vacuous. A name-match classifier alone
would have deleted working Lean here. This is the same failure shape as the
comment-stripping trap: the cheap signal is directionally right and specifically
wrong, and only reading the file separates the two.

## Verification

`bun run scripts/run-validate.ts content/quantum-observable-universe` → **exit 0**
both before and after the deletions, with a byte-identical issue list (5
pre-existing warnings on unrelated blocks). A stub deletion that broke a
`lean.ref` would surface as a new *"no Lean declaration yet"* warning on the
affected block; none appeared. No `.lean` under `lean/QOU/**` was touched, so
no library formalisation changed.

## Residue left undrained

- **5 shadows** among the 13 not deleted: 1 (`hyperbolic-volume-transcendence`)
  whose candidate-2 path exists but does not declare the referenced leaf, and
  `reidemeister-mass-invariance` (real code — must stay). The rest need
  per-item inspection.
- **29 stubs with no candidate-2 resolution** — these are the `MISMATCH`
  (decl in a mis-named library file) and `NEEDED` (genuinely unformalised)
  classes of the 2026-06-14 manifest. §0a says *align*, not delete; each needs
  a decl/file rename, which is not mechanical.
- **18 `holds : Prop` carriers with no library twin** — the genuine vacuity
  gap. Known; the klr plan shows the repair shape (encode the claim as class
  fields) for one of them.
