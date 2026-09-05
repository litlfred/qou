# The archimedean-suffix convention is the wrong instrument — and the corpus already has the right one

**Date:** 2026-09-05
**Beans:** follow-on from the mirror-drift arc (PR #6797)
**Status:** 🛑 **RETRACTION of my own recommendation**, with the measurement that overturns it.
No convention is introduced. One Lean probe is added.

---

## What I recommended, and why it was wrong

Closing the mirror-drift arc I wrote, as the natural follow-on:

> Six of them are §7c wall-pairs where the *sibling* is the correct statement and the
> library holds an older `ℝ` twin under the same name — closing those needs a
> corpus-wide archimedean-naming convention.

The author endorsed it. Before designing anything I checked whether the corpus already
had a convention, and it has something better: **a mechanism that makes the second
declaration unnecessary**, together with a written principle that a suffix convention
would quietly contradict.

[`QOU/Archimedean/GroundRingEval.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/GroundRingEval.lean)
states it in its own words:

> *"`ArchimedeanRealisation` bundles a categorical `SubstrateParameter`, a choice of
> `q₀`, and the two archimedean axioms stated about the realised values.
> `toArchimedeanSubstrateField` then produces the archimedean layer rather than letting
> it be posited independently. … What is no longer assumed is the field itself."*

That file constructs `evalAt (q0 : ℝˣ) : R_q →+* ℝ` — the specialisation `ι : q ↦ q₀` —
as a **ring hom with proved computation rules** (`evalAt_T`, `evalAt_q_param`,
`evalAt_q_param_mul_inv`), and derives the archimedean layer through it.

**A suffix convention names the thing that file exists to eliminate.** Calling the pair
`speedOfLight` / `speedOfLightArch` would bless two independent definitions of one
quantity and make the duplication permanent and tidy, which is worse than duplication
that is visibly untidy. The corpus's own move was in the opposite direction: derive the
archimedean side, do not posit it beside the categorical one.

## The measurement: the library twin *is* the generic definition at `k := ℝ`

Not an argument — checked in Lean.
[`2026-09-05-archimedean-twin-is-the-generic-at-R-probe.lean`](2026-09-05-archimedean-twin-is-the-generic-at-R-probe.lean),
`lean`-direct **exit 0**:

```lean
def speedOfLightGeneric {k : Type*} [Field k] (d : kˣ) : k := (↑d⁻¹ : k)   -- the sibling
noncomputable def speedOfLightArch (q : ℝ) : ℝ := 1 / (q - 1)             -- the library twin

theorem arch_is_generic_at_R (q : ℝ) (d : ℝˣ) (hd : (d : ℝ) = q - 1) :
    speedOfLightArch q = speedOfLightGeneric d := by
  unfold speedOfLightArch speedOfLightGeneric
  rw [← hd, one_div, ← Units.val_inv_eq_inv_val]
```

So the ℝ version is not a second object needing a second name. It is the generic one
instantiated at `k := ℝ`, and the right relationship between them is a **theorem**, not
a naming scheme.

### And the twin is not merely redundant — it is weaker

The same probe proves:

```lean
theorem arch_is_junk_at_one : speedOfLightArch 1 = 0
```

At `q = 1` the library version returns **`0`**, because Lean's `1/0 = 0`. The generic
version **cannot be formed there at all**: it requires `d : kˣ`, and `q − 1 = 0` is not
a unit. The classical limit `q → 1` is exactly where the speed of light is supposed to
diverge — the library's own docstring says *"Diverges at classicality (q → 1)"* — and
the `ℝ` formulation silently returns zero instead.

**A suffix convention would have preserved that.** It would have given the defective
declaration a tidy name and closed the ticket.

## Scope — what this does and does not establish

- **Established:** for `speedOfLight`, the twin is the generic definition at `ℝ` and is
  junk at the one point that matters. Proved.
- ~~**Not established:** that the same holds for the other five pairs.~~
  **✅ NOW ESTABLISHED — all five proved**, in
  [`2026-09-05-archimedean-twins-are-instantiations-probe.lean`](2026-09-05-archimedean-twins-are-instantiations-probe.lean)
  (`lean`-direct exit 0, no `sorryAx`). The caveat is struck rather than deleted so the
  sequence stays visible: when written, the claim rested on shape; it no longer does.

  **And proving them found a defect class the shape argument could not have.** The
  weaker-form count is **not** two, as this document anticipated — it is **four**, and
  the fourth is a different kind of defect:

  | pair | junk point | why |
  |---|---|---|
  | `speedOfLight` | `q = 1` | dropped invertibility; Lean's `1/0 = 0` |
  | `operationalEntropy` | `q = 0` | dropped invertibility |
  | `informationBandwidth` | `q = 1` | dropped invertibility — **at classicality, where the bandwidth is meant to diverge** |
  | `gravitationalConstant` | `q = 1/2` | **not** a dropped hypothesis — a worse algebraic *route* |

  The last one is the find, and nothing about the naming or the wall would have
  surfaced it. The library computes `S_cell = η·ℏ²/(1 − ℏ²)`; the sibling computes
  `u²/q³`. Those are equal — `cellEntropy_arch_eq_simple` proves it — but the library
  route divides by `1 − ℏ² = (2q − 1)/q²`, which vanishes at `q = 1/2`. That
  singularity is an **artifact of how the expression was written**, not a property of
  the quantity. `cellEntropy_arch_junk_at_half` proves the library form returns `0`
  there where the true value is `2`.
- **Not established:** that `evalAt` is the bridge for all six. It is specifically
  `R_q → ℝ`; only `qReebVectorField`'s sibling is stated over `R_q`. The other four are
  generic over an *arbitrary* commutative ring, where the archimedean version is a plain
  instantiation and needs no hom at all. Two different mechanisms, and conflating them
  would be its own error.

## What the right follow-on is

Not a naming convention. Per pair, in this order:

1. **Prove the twin is the generic instantiation** (a probe like the one added here).
2. **Replace the twin's body** with the instantiation, so there is one definition and the
   ℝ form is a `theorem` or an `abbrev` over it — the `GroundRingEval` pattern.
3. **Where the twin is weaker** (a dropped invertibility hypothesis, as here), that is a
   correctness fix and should be reported as one, not as hygiene.

That is real mathematical work with a correctness finding already inside it, and it is a
different, larger job than the one I proposed. It is **not started here** — this document
retracts a recommendation and supplies the evidence; it does not substitute a bigger
plan for it without being asked.

## The reusable lesson

I proposed a convention to regularise a duplication before checking whether the
duplication was necessary. It was not: one side is derivable from the other, and the
derivable side is wrong at the interesting point. **A naming convention over a
redundancy makes the redundancy permanent** — and this is the third time in this arc
that a population counted by symptom (48 "dead pointers" with zero rot; 12 "live
shadows" with one defect; six "wall-pairs needing names" that need a theorem) turned out
to be a different and smaller problem than its symptom suggested.
