# Two decisions for the author: `qou-bdpo` and `qou-gh8l`

**2026-09-04.** Both arose from PR #6584. Both were framed as judgement calls;
both have now been **measured**, and the measurements change the picture — one
decision gets cheaper, the other gets smaller. Nothing here is speculation about
what would happen: each claim below is a command that was run.

---

# Decision 1 — `qou-bdpo`: discharge the `BlochWignerD` opaque?

## What is being decided

`content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.lean`
declares

```lean
opaque BlochWignerD : UpperHalfPlane → ℝ
```

and the conjecture class's hypothesis reads `pole_cusp_matched : volume =
BlochWignerD shape`. The corpus separately owns a **real definition** of the
same function — `QOU.Archimedean.BlochWigner_lob : ℂ → ℝ`
(`BlochWignerLobachevsky.lean:478`), Milnor's `Λ(α)+Λ(β)+Λ(γ)`. The decision is
whether to replace the opaque with

```lean
noncomputable def BlochWignerD (z : UpperHalfPlane) : ℝ :=
  QOU.Archimedean.BlochWigner_lob (z : ℂ)
```

## What was measured (2026-09-04)

The substitution was **applied to a scratch copy and compiled**, not reasoned
about:

| check | result |
|---|---|
| `lean`-direct on the whole file with the import + definition | **exit 0**, 16 s |
| all 12 declarations still elaborate | yes |
| `#print axioms algebraic_geometric_equivalence` | `[propext, Classical.choice, Quot.sound]` |
| `#print axioms AlgebraicGeometricEquivalence.asymptotic_volume` | `[propext, Classical.choice, Quot.sound]` |
| axiom delta vs. the opaque version | **none — byte-identical axiom lists** |

So the two most plausible objections — *"it will not compile"* and *"it will
drag in axiom debt"* — are both **false**, measured.

Blast radius, measured earlier the same day across `content/`, `docs/`,
`computations/` and `.beans/`: **no instance of the class exists anywhere**, and
**nothing outside the file consumes `BlochWignerD`**. The only external mention
is a docstring line at `shared-denominator-cusp-holonomy.lean:17` which
explicitly says there is no type-level binder.

## Option A — discharge it

**What it means.** The conjecture stops saying *"volume equals some
uninterpreted `D` at the shape"* and starts saying *"volume equals Milnor's
Λ-sum at the shape"*.

**What it costs.** One import line and one `def`. Verified: 16 s, exit 0, no
axiom change, no consumer to update. It is, mechanically, the cheapest change on
either bean.

**What it risks.** One thing, and it is not mechanical: it **pins the
identification**. If the `D` intended in this conjecture is the *deformed
complex* volume of the bar-odd leg (`conj:binding-qbeta-complex-volume`) rather
than the real Lobachevsky form, then the file would now assert something
specific and wrong, where today it asserts something vague and safe.

**What it commits to.** That the alg-geom route's volume is the **real**
hyperbolic volume. Consistent with everything else in the file (the whole §2 is
about `D(z) = Vol_hyp`), but it forecloses reading `D` as the complex volume
later without an edit.

## Option B — leave it opaque

**What it means.** Status quo. The class is correctly typed after the
`UpperHalfPlane` retyping and is honestly open.

**What it costs.** Nothing now. Later: every reader must be told separately what
`D` is, and the class can never be instantiated, because an `opaque` has no
value to instantiate against.

**What it risks.** The specific failure this file already had once. An
uninterpreted symbol invites a wrong *type* (it carried `ℝ → ℝ` for months) and
a wrong *reading*. Opaqueness is not neutrality — it is unexamined-ness.

**What it commits to.** Nothing, which is the point.

## Blast radius, in real terms

`algebraic-geometric-dilog-equivalence` is cited by the definition index and by
`shared-denominator-cusp-holonomy`'s docstring. It has **no compute consumer**:
no witness, no producer, no dashboard reads it, so **no number in the paper
moves under either option**. What changes is what a reader — and a future
instance-builder — is told the conjecture claims.

## Default if you say nothing

The opaque stays. The class is correctly typed, honestly open, and the audit
records the option. Nothing breaks, and nothing is misstated.

## Recommendation (my judgement, not a finding)

**Discharge it (A)** — with one condition. The measurement removed every
mechanical objection, and the remaining risk is a *mathematical* question you
can answer in one word: is the `D` of `conj:algebraic-geometric-dilog-equivalence`
the real Lobachevsky volume, or the deformed complex volume? If real: discharge,
and the conjecture becomes falsifiable at no cost. If complex, or if you are not
sure: **leave it opaque** — a vague-but-safe assertion beats a sharp-and-wrong
one, and this file has already been wrong once in exactly that direction.

---

# Decision 2 — `qou-gh8l`: wire the new Lean files into `QOU.lean`?

## What is being decided, and it is smaller than the bean says

The bean says "six/seven Lean files". **Measured: it is six.** The seventh,
`mass-theory/algebraic-geometric-dilog-equivalence.lean`, is a **content-block
sibling** — it lives outside the `lean/` Lake root, is resolved through its
block's `lean.ref`, and is not a Lake module at all. It cannot be imported and
was never a candidate. Correcting my own bean.

The six are:

* `QOU/Eightfold/ContactDistributionRank.lean`
* `QOU/Eightfold/CommutativeImageDegeneration.lean`
* `QOU/Eightfold/HyperbolicVolumeFormType.lean`
* `QOU/QuantumObservableUniverse/SelfDualityDegree.lean`
* `QOU/QuantumObservableUniverse/CalculusDimensionObstruction.lean`
* `QOU/BringsSurface/CoveringDegreeRamification.lean`

None appears among `QOU.lean`'s **848** imports, so `lake build QOU` never
elaborates them.

## What was measured (2026-09-04)

Every one of the six is a **Mathlib-only leaf**:

| file | imports |
|---|---|
| `ContactDistributionRank` | `Nat.Choose.Basic`, `Tactic.Linarith`, `Tactic.NormNum` |
| `SelfDualityDegree` | same three |
| `CalculusDimensionObstruction` | same three |
| `HyperbolicVolumeFormType` | same three |
| `CommutativeImageDegeneration` | `Algebra.Ring.Defs`, `RingTheory.Ideal.Span`, `Mathlib.Tactic` |
| `CoveringDegreeRamification` | `GroupTheory.Perm.Sign`, `Perm.Cycle.Type`, `Tactic.Linarith`, `Tactic.NormNum` |

**`grep '^import QOU' ` over all six returns nothing.** That is the fact that
settles the risk question: with no intra-`QOU` dependency, adding six import
lines to `QOU.lean` **cannot** create a cycle, cannot impose an ordering
constraint, and cannot change the elaboration of anything already there. The
only Mathlib module any of them needs that is even slightly unusual is
`Nat.Choose.Basic`, which `QOU.lean` at 848 imports certainly already reaches.

## Option A — add the six imports

**What it means.** `lake build QOU` elaborates them, so an upstream Mathlib bump
or a refactor that breaks one is caught by the build rather than by nobody.

**What it costs.** Six lines. **But it cannot be verified in this container:**
the tree carries `.lake/RESTORED-NO-TRACES`, and running `lake build` would
treat every restored olean as stale, rebuild from source and **evict the
restore** (measured, bean `qou-r13s`: 6990 → 334 mathlib oleans in ten minutes,
silently). So the edit would be pushed unverified, and confirmed only on a
machine that can build.

**What it risks.** Low, and now quantified: no `QOU` imports means no cycle and
no ordering constraint. The residual risk is that `lake build QOU` is red for
*pre-existing* reasons and the six get blamed.

**What it commits to.** That these six are library content rather than working
notes — a reasonable claim for all six.

## Option B — leave them standalone

**What it means.** Status quo, and it is the **existing pattern**: this is how
every file on this branch already sits, and the `lean`-direct gate is what
AGENTS.md's Phase-4 verification actually asks for, given that CI auto-triggers
are disabled repo-wide.

**What it costs.** Nothing now. Later: an upstream change can break all six
silently, and only an agent re-running `lean`-direct by hand would notice.

**What it risks.** Exactly that silence. Note this compounds a gap AGENTS.md
already names — a standalone library `.lean` has no `.qa.json` sidecar and
escapes every per-block checker; being unreachable from the root removes the
second net too.

**What it commits to.** Nothing.

## Option C — add them on a machine that can build

**What it means.** Defer the edit to a session with a working Lake cache, where
`lake build QOU` confirms the root still elaborates before the push.

**What it costs.** The delay, and remembering.

**What it risks.** Being forgotten — which is what a bean is for.

## Blast radius, in real terms

`QOU.lean` is the library root that `lake build QOU` and the doc-gen4 /
blueprint pipelines consume. Adding six leaf imports affects **build coverage
only** — no proof changes, no witness moves, no number in the paper changes
under any option. What is at stake is solely whether a future breakage is caught
by a machine or by a person.

## Default if you say nothing

They stay standalone, verified by hand exactly like every other file in this
tree. Nothing breaks today.

## Recommendation (my judgement, not a finding)

**Option C.** The measurement moved me off my earlier "leave it": with zero
`QOU` imports across all six, the *mathematical* risk is gone and only the
*verification* risk remains — and that one is an artifact of this container, not
of the change. So it should be done, just not blind. Adding six imports and
pushing them unverified would be exactly the "one validated push beats three
speculative ones" failure, on a change whose whole purpose is to increase
verification.

If you would rather not carry the deferral: **Option B is safe and costs
nothing today**, and it is what the corpus already does everywhere else.
