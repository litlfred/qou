# Corpus trace — which existing objects supply pieces 1–3 of the `conj:s5-so3-fiber-action` construction

**Date:** 2026-06-20
**Branch:** `claude/s5so3-pieces-corpus-trace-2026-06-20`
**Kind:** reporting only — no new math. Consolidates the corpus objects the construction-scope doc
([`2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md))
relies on for its **settled** ingredients, with every cited path verified to resolve on this branch.

## Why this trace

The scope doc reduces `conj:s5-so3-fiber-action` to a five-ingredient program and reports ingredients **1–3
settled**, the **ingredient-4 algebraic leg concrete**, and only the **ingredient-4 geometric leg** open
(plus ingredient-5 refuted). "Settled" there means *the corpus already supplies the object* — but the scope
doc names several of those objects by concept rather than path. This trace pins each to its verified
`.md` / `.lean` / checker source so the next agent can read the actual construction instead of re-deriving it
(the failure mode §Refutations item 4 exists to stop).

## Piece 1 — the spin lift: divisor $\mathbb{CP}^1$ = Klein's icosahedral $\mathbb{P}^1$, action through $2I\subset\mathrm{SU}(2)$

**Claim (settled):** the icosahedral fibre action *is* the spin $\mathrm{SU}(2)_S$ lift — the same lift the
corpus already uses, not a new object. $A_5\cong I\subset\mathrm{SO}(3)$ has no faithful 2-dim rep, so it acts
on the spinor $\mathbb{C}^2$ only through the binary icosahedral $2I$; globally $S^3/2I$ is the Poincaré
homology sphere = link of the E₈ singularity.

| Object the scope doc relies on | Verified source | What it supplies |
|---|---|---|
| Bundle structure group is the spin cover $\mathrm{SU}(2)\cong\mathrm{Sp}(1)$; $\mathrm{SO}(3)$ holonomy lifts via $\mathrm{Ad}$ | [`braids-and-knots/quaternion-so3-motivation.md`](../../content/quantum-observable-universe/braids-and-knots/quaternion-so3-motivation.md) | the cover that makes a binary lift *exist* |
| "Every finite $\mathrm{SO}(3)$ subgroup lifts to a binary subgroup of $\mathrm{SU}(2)$; for $S_3\cong D_3$ the lift is binary dihedral $\mathrm{Dic}_3$ (order 12)" | [`brings-surface/su2-generators.md`](../../content/quantum-observable-universe/brings-surface/su2-generators.md) | the **binary-lift principle**, worked for $S_3$ — the $A_5\to 2I$ template |
| The $\mathrm{SU}(2)_S$ spin lift = ingredient 1's $2I$ lift (same lift, not two) | [`particle-interactions/spin-from-so3-fiber.md`](../../content/quantum-observable-universe/particle-interactions/spin-from-so3-fiber.md) (+ sibling `.lean`) | identifies the fibre action as the spin lift |
| $\Sigma_4$ is a **genus-4 curve**, $\mathrm{Aut}=S_5$ — so the $\mathbb{CP}^1$ is the **spin/state-bundle fibre**, not a curve blow-up | [`brings-surface/fivefold-symmetry.md`](../../content/quantum-observable-universe/brings-surface/fivefold-symmetry.md) | locates *where* the icosahedral $S^2$ lives |
| McKay $2I\leftrightarrow$E₈ anchors ($\sum d^2=120$, $\sum\text{marks}=h=30$, $\lvert 2I\rvert=4h$, $\dim$E₈$=8\cdot31$); $A_5$ branching $V_1\to T_1$, $V_2\to H$, $V_3\to T_2\oplus G$; $(3,1,1)$ self-conj $T_1\oplus T_2$ | [`lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean) (#2424) | machine-checked the rep-theory that **forces** geometric $A_5$ to icosahedral $T_1$ |

**Caveat (de-vacuification, #2480).** The Lean scaffold's `partition_to_rotation` map was de-vacuified on
2026-06-18 (`BringFiberAction`: removed the provably-false `respects_conjugate`, the vacuous
`hits_five_conjugacy_classes : True`; domain corrected to the 5 $A_5$ irreps `A5Irrep`). The McKay/branching
anchors above stand; the *geometric fibre map itself* stays open. Do not read the scaffold as a closure.

## Piece 2 — the $2I$-equivariant Reeb field

**Claim (inherits the precedent):** the q-Reeb field $\xi_q$ ($\dot\psi=q$) on the Hopf bundle $S^3\to S^2$
commutes with the binary cover; the existing $S_3\to\mathrm{Dic}_3$ Reeb construction is *already* binary-
equivariant, so $2I$ is the direct analogue.

| Object | Verified source | What it supplies |
|---|---|---|
| The existing $S_3$-side Reeb construction: $\mathcal{S}_p\cong\mathbb{CP}^1=S^2$, Hopf bundle $S^3\to S^2$, six $S_3$ knot operators, $S_3$-Galois boundary monodromy | [`mass-theory/exceptional-divisor-reeb-intro.md`](../../content/quantum-observable-universe/mass-theory/exceptional-divisor-reeb-intro.md) | the geometric $=$ algebraic identity **at the 3-strand base** (ingredient-4 piece 1) |
| The q-Reeb field $\xi_q$ ($\dot\psi=q$) itself | [`mass-theory/q-reeb-flow-on-coral-coords.md`](../../content/quantum-observable-universe/mass-theory/q-reeb-flow-on-coral-coords.md) (+ sibling `.lean`, and [`lean/QOU/CategoricalReeb/QReebFlowOnCoralCoords.lean`](../../content/quantum-observable-universe/lean/QOU/CategoricalReeb/QReebFlowOnCoralCoords.lean)) | the flow whose $2I$-equivariance is asserted |

**What remains (not piece 2's fault).** Piece 2 supplies the *binary-equivariant Reeb field*; the open object
is the **5-strand** extension of this flow (ingredient 4 geometric leg), not the equivariance of the field.

## Piece 3 — the two bridging branchings (VERIFIED this keystone session)

**Claim (verified):** $\mathrm{SO}(3)\downarrow A_5$ ($V_1\to T_1$, $V_2\to H$, $V_3\to T_2\oplus G$) and
$S_5\downarrow A_5$ ($(3,1,1)\to T_1\oplus T_2$; $(3,2),(2,2,1)\to H$) connect the geometric level $\ell$ to
the already-verified $S_5\downarrow S_3$ combinatorics. This was the cheap formalize-first step.

| Object | Verified source | What it supplies |
|---|---|---|
| Backbone + bridge checker (the verification driver) | [`docs/audits/scripts/s5so3_branching_backbone_verify.py`](scripts/s5so3_branching_backbone_verify.py) | re-runnable proof of the branching tables |
| Backbone-verified audit | [`2026-06-16-s5so3-branching-backbone-verified.md`](2026-06-16-s5so3-branching-backbone-verified.md) | the narrative of pieces 3 |
| Lean: $S_5\downarrow S_3$ restriction dimension-consistency, all 7 blocks (#2431); $S_3$-rotation branching $\ell\le4$ (#2436); $A_5$ branching content (#2424) | [`lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean), [`lean/QOU/BraidsAndKnots/GapA4MuonBranching.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/GapA4MuonBranching.lean) | machine-checked branching backbone |

## Net

Pieces **1–3 are corpus-realized and now path-pinned**; the single open object is the **ingredient-4
geometric leg** — a $2I$-equivariant 5-strand Reeb (contact/Sasakian) realization on the Bring spin bundle
whose Markov trace is the (Ocneanu-forced, zero-free-parameter) $H_5(q)$ trace. Because the production weight
is the full-Hecke principal specialization (infinite-variable), a finite-dim Sasakian is ruled out; the
realization must be infinite-dim/direct-limit (the WRT$(S^3/2I)$ = Lawrence–Zagier home, #2503). This trace
adds no math — it ensures the next agent reads pieces 1–3 instead of rebuilding them.

## Cross-references

- [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md) — the five-ingredient program (source of the "settled" classification)
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — master ledger (§Refutations, §Sessions log)
- [`docs/audits/2026-06-13-bring-fiber-action-falsification.md`](2026-06-13-bring-fiber-action-falsification.md) — the #2480 de-vacuification basis
