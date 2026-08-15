---
# qou-cu0a
title: 65 lean.refs resolve to QOU.lean (the import aggregator) — checkers audit an import list and pass vacuously
status: todo
type: task
priority: normal
created_at: 2026-08-15T20:32:39Z
updated_at: 2026-08-15T23:13:52Z
---

Found while adjudicating `def:yekutieli-triple` (session `qou-xz6t`, branch `claude/mtcx-7c-verify-close-2026-08-15`).

## The failure mode — silent, not loud

A `lean.ref` naming a declaration that does not exist does **not** resolve to nothing. `parseLeanRef` splits at the last dot, so `qou:QOU.YekutieliTripleMapping` has module `QOU` — and the resolver's final *safe fallback* returns the direct module-path file, `lean/QOU.lean`. That is the **954-line root import aggregator**: a file of `import` lines that declares nothing.

Every checker consuming such a block's `.lean` therefore audits a bare import list — and **passes**. `wall-side-correct` sees no archimedean markers: pass. `q-usage-*` sees no `q`: pass/na. `proof-no-bare-sorries` sees no `sorry`: pass. The block looks formalised and green while nothing of the kind was checked.

This is worse than an unresolved ref, which at least yields an honest `n/a`.

## Measured across the corpus (2026-08-15)

Scanned every `.ts` block under `content/quantum-observable-universe/` carrying a `qou:` ref, resolving through the canonical `qa-utils.resolveCanonicalLean` with a shared Lake-tree cache:

| | count |
|---|---|
| blocks with a `qou:` lean.ref | 1220 |
| **resolve to `QOU.lean` (aggregator)** | **65** |
| unresolved (no file at all) | 319 |

Examples: `braids-and-knots/so3-generators.ts` (`qou:QOU.So3Generators`), `brings-surface/hyperelliptic-quintic.ts` (`qou:QOU.HyperellipticQuintic`), `fluid-dynamics/observable-mtc.ts` (`qou:QOU.ObservableMTC`), `information-theory/q-heat-kernel-peter-weyl.ts` (`qou:QOU.qHeatKernelPeterWeyl`).

The common shape is a **single-segment decl name** (`QOU.Foo`): module `QOU` → `QOU.lean`.

## This is a deliberate trade-off, not an implementation bug

`resolveCanonicalLean` already *has* aggregator rejection — candidate (a) is gated on `fileDeclaresName`, and candidates (b)/(c) try basename and fully-qualified-decl lookups. But the function ends with:

```
// (safe fallback) preserve legacy behaviour: a ref that resolved to the
//   direct module-path before the (a)-gate still resolves to it, so no
//   previously-resolving ref regresses to `undefined`.
if (directExists) return direct;
```

So the gate fires and the fallback hands the aggregator back anyway. That choice was made to avoid regressing refs to `undefined`; the cost, now measured, is 65 vacuous passes. **The question this bean poses is whether an honest `n/a` beats a false green** — I did not change the resolver, since that is a folio-assistant-side policy call with corpus-wide blast radius.

## Options

1. **Per-block (safe, incremental).** Repoint each of the 65 at a real module, as done for `yekutieli-triple.ts` in this branch. Note the module segment must be the **file**, not the Lean namespace — see that block's comment for the trap.
2. **Resolver-side (one change, corpus-wide).** Drop or narrow the safe fallback so an aggregator-only match returns `undefined`. Turns 65 false greens into honest `n/a`s; needs a folio-assistant PR + a re-sweep, since cached sidecar verdicts would flip.
3. **Checker-side.** Have the QA layer treat "resolved file declares nothing / is import-only" as `n/a` regardless of how resolution got there.

## Relation to existing beans

Distinct from `qou-qe41` (29 sibling stubs with no candidate-2 resolution) and `qou-ref10` (ten refs with no formalisation): both are about refs that **fail** to resolve. This bean is about refs that **succeed** into the wrong file and therefore never surface. The 319-unresolved figure above suggests those two beans undercount their own class as well.


## SCALE CORRECTION + FIX LANDED (2026-08-15)

**The 65 figure in the title undercounts by ~5×.** It counted only refs resolving to the *root* `QOU.lean`. Refs also fell back to **other** import-only aggregators — e.g. `QOU/BraidKnot.lean`, whose entire non-`import` content is a module-index docstring and which declares **nothing** — and those were invisible to my original scan because they are neither "the root aggregator" nor "unresolved".

Measured on the same 1220 blocks, before → after the resolver fix:

| | before | after |
|---|---|---|
| resolve to the `QOU.lean` root aggregator | 65 | **0** |
| unresolved (honest `n/a`) | 319 | **558** |

The `+239` are the non-root aggregator cases. So **~304 of 1220 blocks — a quarter of the corpus — were being audited against a list of `import` lines and passing.**

### Fix (option 2 of the three recorded above), landed upstream

`folio-assistant` commit `ef80839`, branch `claude/gracious-dijkstra-0ijp2l`: `resolveCanonicalLean`'s safe fallback is **narrowed, not removed** — it still returns the direct module-path file, unless that file declares nothing at all. New helper `fileDeclaresAnything()` gates it.

Verified: five spot-checked decl-bearing refs still resolve (`TauQuantumIntegerForm`, `QChebyshevFunction`, `CosimplicialCrossedGroupoid.YekutieliTriple`, `QJucysMurphy`, `Torsion.YekutieliTriple`); an aggregator ref now returns `undefined`. Regression test added; folio-assistant suite **643 pass / 0 fail**.

### What qou must do before adopting

This **flips ~304 cached sidecar verdicts from `pass` to `n/a`**. That is the intended correction — those passes were never real — but it is not a silent upgrade:

1. Re-sweep after picking up the folio-assistant change, so sidecars reflect `n/a` rather than stale greens.
2. Expect QA coverage numbers to *drop*. That drop is the removal of false coverage, not a regression.
3. The 63 blocks whose refs name declarations existing **nowhere** (per the triage above) are now honestly `n/a`. They remain genuinely unformalised — repointing them is not possible; they need formalisation or removal of the `lean.ref`.


## Dispositioned (2026-08-15) — 65 → 6 fixed, 2 ambiguous, 57 backlog

Every `qou:QOU.<Name>` ref that fails to resolve (i.e. the set that used to land on the root aggregator) is now triaged. Matching was normalised (case/underscore-insensitive) against a decl index built from the whole Lean tree, and **every proposed fix was verified through the canonical resolver before being written** — an earlier naive pass produced false positives by matching generic last segments like `.exists`, and was discarded.

### FIXED — 6 refs were casing/style mismatches, not missing formalisation

Each named a real declaration under a different spelling. The corrected ref uses the **file** as the module segment and the **exact** decl name as the last segment; all six verified to resolve to the intended file:

| block | was | now | resolves to |
|---|---|---|---|
| `braids-and-knots/so3-generators.ts` | `QOU.So3Generators` | `QOU.PathIntegrals.SO3Generators` | `QOU/PathIntegrals.lean` |
| `braids-and-knots/su2-basis.ts` | `QOU.Su2Basis` | `QOU.PathIntegrals.SU2Basis` | `QOU/PathIntegrals.lean` |
| `glossary/glossary-observed-value.ts` | `QOU.ObservedValue` | `QOU.BringsSurface.observedValue` | `QOU/BringsSurface.lean` |
| `lifting-and-descent/qu-to-qou.ts` | `QOU.QuToQou` | `QOU.Torsion.YekutieliTriple.qu_to_qou` | `QOU/Torsion/YekutieliTriple.lean` |
| `lifting-and-descent/yekutieli-lifting.ts` | `QOU.YekutieliLifting` | `QOU.BringsSurface.yekutieli_lifting` | `QOU/BringsSurface.lean` |
| `lifting-and-descent/brane-boundary.ts` | `QOU.braneBoundary` | `QOU.Torsion.Descent.BraneBoundary` | `QOU/Torsion/Descent.lean` |

### AMBIGUOUS — 2, deliberately NOT auto-fixed

- `brings-surface/hyperelliptic-quintic.ts` → `qou:QOU.HyperellipticQuintic` names a **directory** (`QOU/HyperellipticQuintic/` holds `minimal_z5_classification`, `zeta5_residue_monodromy`, `ScratchZeta5`, `CheckAbs`); no single decl is obviously the target. Needs an author's call.
- `mass-endomorphism/mass-identity.ts` → `qou:QOU.categoricalMass` matches **two distinct declarations**: `QOU/PhotonThreading.lean:81` (generic `{M : Type*} (sp : SubstrateParameter M)`) and `QOU/BraidKnot/MassFormulaCategorical.lean:71` (`(rho) (m_e : ℝ) (T_w) : ℝ`). **That collision is itself a finding** — two `categoricalMass` decls on opposite sides of the §7c wall.

### BACKLOG — 57 name a declaration that exists nowhere

These are genuinely **unformalised**, not mis-referenced: no decl matches even under normalised matching. Examples: `QOU.QuantumFlatness`, `QOU.ReebGaugeGroup`, `QOU.DescentData`, `QOU.S3Group`, `QOU.ObservableMTC`, `QOU.qHeatKernelPeterWeyl`, `QOU.ColorSectorCoords`, `QOU.LocalizedHadron`.

**Deliberately left in place.** After the upstream resolver fix they report an honest `n/a` rather than a false green, and the ref still records the *intended* formalisation target, which is useful to whoever writes it. Removing 57 refs would delete that intent and is a content-owner decision, not a tooling one — and §7c discipline is explicit that this class of sweep is not a mass-fix. Note that omitting `lean:` entirely is well-precedented (2345 of 3567 blocks carry no `lean:` field), so removal is available if the owner prefers it.
