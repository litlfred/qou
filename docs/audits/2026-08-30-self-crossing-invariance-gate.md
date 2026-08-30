# The mass=self / binding=mutual assignment has a hidden hypothesis — and Călugăreanu says it is not free

**Date:** 2026-08-30 · **Bean:** `qou-brng` · **Arc:** bk-crossing mass-binding · **PR:** #6226
**Tier:** scope-**(a)** — nothing refuted, no ingredient excluded, no number moved, nothing wired.
**Lean:** [`QOU/Mass/SelfCrossingInvarianceGate.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/SelfCrossingInvarianceGate.lean)
— `lean`-direct exit 0, 0 `sorry`, all 8 declarations on `propext / Classical.choice / Quot.sound`.
**Compute:** none. No producer re-run, no witness touched, so no precision gate applies.

## 0. Why this document exists, and a framing correction

This session was dispatched on `qou-brng`'s "linking-vs-self-energy amplitude assignment" as the
arc's **one real open problem**, with the Moffatt–Ricca OCR tier named as the strongest
**unexplored** lead. The corpus-grep checklist overturned both halves of that brief before any Lean
was written, and the correction is worth recording because it is the discipline working:

- **Path 6 (`.beans/`).** `qou-brng` carries **three** updates landed the same day — `qou-d3i9`
  (#6125, type question PROVED, `QOU.Mass.BrunnianBindingChannel`), `qou-xjup` (#6145, R1 + R2
  PROVED, R3 measured numerology), `qou-0qkt` (#6145, R2 residual LIFTED,
  `QOU.Mass.ArchimedeanTraceBridge`). None of that was in the brief.
- **Path 1 (`docs/audits/`).** The helicity lead was explored and closed the same day, in
  [`2026-08-30-helicity-ladder-cannot-supply-the-he4-surplus.md`](2026-08-30-helicity-ladder-cannot-supply-the-he4-surplus.md)
  — rung 2 bilinear ⇒ intrinsically ≤ 2-body; rung 3 = the Milnor μ̄ route in different notation.

So: **this document does not close `qou-brng`, and does not reopen it.** It reports what an
adversarial read of the freshly-landed closure found.

## 1. The claim

[`QOU.Mass.SelfMutualPartition`](../../content/quantum-observable-universe/lean/QOU/Mass/SelfMutualPartition.lean)
proves `binding_eq_neg_mutualEnergy` — binding is exactly minus the inter-component energy, hence
mass ↔ self and binding ↔ mutual. **The derivation is correct.** But its `binding` is *defined* as

```lean
noncomputable def binding (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] : ℝ :=
  selfEnergy E energy isInter - assemblyEnergy E energy
```

and the docstring supplies the justification for `selfEnergy` sitting in the first slot:

> "the sum of isolated masses is `selfEnergy` (**the self crossings are exactly those present in
> isolation**)"

The mass-deficit definition of binding is `B = (Σ isolated component masses) − (assembled mass)`.
Writing `selfEnergy` for the first term presumes that assembling the components changes **no
component's own self-crossing content**. That is a hypothesis. It is argued in prose and it does not
appear in any statement, so no consumer of `binding_eq_neg_mutualEnergy` can see that it is carrying
one.

This is the shape AGENTS.md §"Defined residual ≠ derived decomposition" describes, one file over:
a quantity written with `:=` and then reasoned about as though the identification it encodes had
been derived.

## 2. What was formalized

### §1 of the Lean file — the gate, exhibited

| declaration | statement |
|---|---|
| `bindingOfIsolated E energy isolatedMassTotal` | binding by the mass deficit, isolated-mass total as **free data** |
| `selfDefect` | `isolatedMassTotal − selfEnergy` — the self reorganisation residual |
| `binding_eq_neg_mutual_add_selfDefect` | `binding = −mutual + selfDefect` |
| `binding_eq_neg_mutualEnergy_iff_selfDefect_zero` | `binding = −mutual` **⟺** `selfDefect = 0` |
| `binding_eq_neg_mutualEnergy_of_gate` | recovers the landed result under the gate |
| `gate_has_content` | the falsifiable witness (below) |

The landed theorem is precisely the `selfDefect = 0` slice of the general identity. **Nothing is
retracted** — `binding_eq_neg_mutualEnergy_of_gate` reproduces it. What changes is that the gate is
now in the type instead of in a docstring.

`gate_has_content` is what makes this more than bookkeeping. One fixed assembly — a single
inter-component crossing and a single self-crossing, unit energy each — read two ways:

| reading | `isolatedMassTotal` | mutual energy | binding |
|---|--:|--:|--:|
| the self-crossing pre-existed (gate holds) | 1 | 1 | −1 |
| the self-crossing was created by assembly (type-I move; gate fails) | 0 | 1 | **−2** |

The mutual energy is `1` in both. So **binding is not a function of the mutual part** once the gate
is dropped, and `SelfMutualPartition.binding_indep_of_self` — "binding sees only inter-component
structure" — is a consequence of the gate rather than of the crossing partition.

### §2 — the Călugăreanu reason the gate is not automatic

Călugăreanu–White–Pohl: `SL = Wr + Tw`. Only the **sum** is the isotopy invariant. Formalized
generic over `[AddCommGroup R]` (§7c — the exchange is pure algebra; no ordering, no `Real.sqrt`,
no archimedean construct):

- `selfLinking_inflexionMove` — `SL` is fixed by the writhe↔twist exchange;
- `writhe_inflexionMove_ne` — the writhe alone moves by exactly `d`;
- `selfEnergy_invariant_of_factorsThroughSelfLinking` — a self-energy factoring through `SL` passes
  the gate;
- `selfLinking_fixed_writhe_moved` — the two side by side over `ℝ`.

## 3. The source, and the tier it was hiding in

Moffatt & Ricca, *Helicity and the Călugăreanu invariant*, Proc. R. Soc. Lond. A **439** (1992)
411–429 — held at `library/procrsoclondona92/`, reference key `moffatt-ricca-helicity`
(`content/schema/references.ts:13694`). From §1 (`ocr/page-002.txt:29–45`), verbatim:

> "If C is continuously deformed through an inflexional configuration … 𝒯 is discontinuous by ±1,
> but 𝒩 is simultaneously discontinuous by an equal and opposite amount ∓1 … so that the sum
> 𝒯+𝒩 does vary continuously."

> "**any deformation whose projection on any plane involves a type I Reidemeister move … must
> involve passage through an inflexional configuration. General deformations (or 'ambient
> isotopies') do therefore typically involve such passage** and consideration of the associated
> behaviour of 𝒯 and 𝒩 cannot be avoided."

and Pohl's `SL = W + T` (their 1.4) is stated for **regular** isotopy — "continuous deformation of
C not passing through any [inflexion]".

A type-I Reidemeister move is precisely the creation or removal of a **self**-crossing. So a
self-energy read off a bare self-crossing count is **not** ambient-isotopy invariant, and Moffatt &
Ricca's own wording is that such deformations are *typical*, not exotic. The gate is a real
constraint.

**This citation is invisible to the documented corpus-grep.** `library/procrsoclondona92/sections/`
is **1,916 bytes** of JSTOR download banner against **46,511 bytes** of real text in `ocr/` (4.1 %),
so path 5 as written (`grep -rln <topic> library/<doc-id>/sections/`) returns nothing for *helicity*
or *Călugăreanu* on this document. Only `grep -rln <topic> library/*/ocr/` finds it. AGENTS.md
already carries that warning (§"FOURTH TIER"); this is a worked instance where the OCR tier carried
the load-bearing citation rather than a corroborating one.

## 4. Why this matters to the framework specifically

The mass multiplier is `lw`, a **self-linking weight**; the binding multiplier is the mutual
coordination count `M`. §2 says the two candidate readings of a self quantity behave differently
under exactly the move that assembly performs:

- a self-energy factoring through `SL = Wr + Tw` is invariant, so `selfDefect = 0` and the
  mass=self / binding=mutual assignment holds as landed;
- a self-energy read off the writhe (self-crossing count) alone is not, so `selfDefect ≠ 0` and
  `binding = −mutual` fails by the amount of the reorganisation.

That is a **statable, checkable criterion** on the self multiplier, and it is the useful output of
this session. It does not decide which reading `lw` is — that is the honest next question, recorded
below rather than guessed at here.

## 5. Scope, stated per the (a)/(b) discipline

**Scope-(a).** This construction shows one landed theorem carries an unstated hypothesis; it does
**not** show that the hypothesis fails, does **not** refute the mass=self / binding=mutual
assignment, and excludes **no** ingredient. No proved invariant is cited to forbid anything, so no
scope-(b) claim is made or licensed. The numerical corpus is untouched.

## 6. What is open after this

1. **Is `lw` `SL`-valued or writhe-valued?** The criterion in §4 is stated; applying it needs the
   definition of `lw` traced to whether it reads a framing-independent self-linking or a
   self-crossing count. Not attempted here — asserting an answer without tracing it would be exactly
   the defect this document is about.
2. **Is `selfDefect = 0` for the framework's carriers?** If `lw` turns out writhe-valued, the size
   of the defect is a measurable question (and a *magnitude* question, hence subject to the anti-fit
   discipline — inverting AME to fix it would be a fit).
3. The three items `qou-brng` already records as remaining — the carrier's crossing structure (R1's
   topological input), and the two named modelling inputs of `ArchimedeanTraceBridge` — are
   unaffected by this document.

## 7. Verification

CI auto-triggers are disabled repo-wide (`workflow_dispatch`-only, owner directive 2026-06-30), so
the agent's own verification is the gate:

```
bash scripts/leancheck-worktree.sh --dep QOU.Mass.SelfMutualPartition -- \
    content/quantum-observable-universe/lean/QOU/Mass/SelfCrossingInvarianceGate.lean
=== exit 0
grep -c sorry <file>  =>  0
#print axioms (all 8 declarations)  =>  propext / Classical.choice / Quot.sound only
```

**No `lake` command was run.** This session worked in a git worktree with no `.lake/`; the oleans
are a *restored* cache in the main checkout marked `.lake/RESTORED-NO-TRACES`, and `lake` treats
restored oleans as stale, rebuilds from source and evicts the restore (measured 6990 → 334, silently
— bean `qou-r13s`). [`scripts/leancheck-worktree.sh`](../../scripts/leancheck-worktree.sh) exists
for this: `LEAN_PATH` points at the main checkout **read-only**, and any missing QOU dependency is
compiled `lean`-direct into a gitignored worktree-local `.leanscratch/`.
