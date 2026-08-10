# Lepton number is not a ℤ-grading by smoothing count

**Date:** 2026-08-10
**Branch:** `claude/lepton-number-skein-grading-2026-08-10`
**Bean:** `qou-kl39`
**Status:** proved sorry-free; scope-(b) exclusion of one construction

## Why this was looked at

`HyperchargeBatteryReduction.lean` (merged, PR #4597) proved that the
eightfold-way hypercharge battery reduces to a single condition: on the
left-handed sector, `Y = B − L`. The `B` half has a named candidate
(`μ̄₁₂₃`, PR #4597). The `L` half was beaned as blocked (`qou-kl39`) because
`def:lepton-number-categorical` defines `L` as a count along a **transition**
(a β-decay), while `Y` must be a property of a **state**.

`lepton-number-categorical-properties.md` supplied the intended bridge:

> **Lepton number as a ℤ-grading.** The Skein module `𝒦(S³; q)` admits a
> natural ℤ-grading by the smoothing count. Links in the nuclear sector have
> grade `0`. Each smoothing shifts the grade by `+1`. Hecke relations act
> within a fixed grade.

This audit tests that bridge before building on it — the forward
formalize-first prune.

## Result: the bridge as stated cannot exist

The skein relation (AGENTS.md §7a) is

```
L₊ − L₋ = (q − q⁻¹) · L₀
```

Under the claimed grading, `L₊` and `L₋` are grade `g` and `L₀` is grade
`g + 1`; scalars are grade-preserving, so the right side is grade `g + 1`
while the left, a difference of grade-`g` classes, is grade `g`. A grading's
defining property is that distinct homogeneous components meet only in `0`.
Hence **both sides vanish**.

Proved in
[`LeptonNumberGradingObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/LeptonNumberGradingObstruction.lean):

| Theorem | Statement |
|---|---|
| `skein_forces_vanishing` | `Lp, Lm ∈ piece g`, `S ∈ piece (g+1)`, `Lp − Lm = S` ⟹ `S = 0 ∧ Lp = Lm` |
| `skein_grading_kills_smoothing` | with the coefficient exhibited: `(q − q⁻¹) • L₀ = 0` |
| `lepton_number_would_be_trivial` | if every grade-`(g+1)` class arises as a skein term, the whole positive-degree part is `0` |

The consequence is sharp: imposing the grading annihilates every smoothing,
so it would make lepton number **identically zero** — the one value it cannot
take, since `L(e⁻) = +1`.

Note the hypothesis used is deliberately weak. `SmoothingGrading` requires
only that distinct components intersect in `0`, *not* a full internal
direct-sum decomposition. The obstruction bites without the stronger
structure, so it cannot be evaded by weakening what "grading" means.

## Honest scope

**Scope-(b)**, with the justifying invariant cited (disjointness of distinct
homogeneous components vs the inhomogeneity of the skein relation). It
excludes exactly one construction — `L` as a ℤ-grading by smoothing count.

It does **not** refute:

- lepton number itself, or the `def:lepton-number-categorical` values;
- the Skein module;
- the `Y = B − L` route, or `μ̄₁₂₃ = B`.

## Where the repair probably lives — untested

An inhomogeneous relation is precisely what a **filtration** tolerates: the
skein relation *lowers* filtration degree by one rather than preserving a
grade. That is the Vassiliev / finite-type filtration, and the corpus already
carries it — `QOU/KnotTheory/Vassiliev/` (`finiteTypeSubmodule_mono` is the
increasing family, `IsFiniteType`, `symbol`, `MilnorVassilievBridge`).

Two reasons this is the natural place to look, neither of them a result:

1. The filtration is by powers of `(q − q⁻¹)`, which is exactly the
   coefficient the skein relation attaches to a smoothing — so "number of
   smoothings" and "finite-type degree" are plausibly the same counter.
2. `μ̄₁₂₃`, the `B`-half candidate, is a **degree-2 Vassiliev** invariant
   (`MilnorVassilievBridge`). If `L` is also a filtration degree, then `B`
   and `L` would live in one structure rather than two unrelated ones.

**Nothing here shows that works.** It is a direction, not a finding. `L` as a
state function remains open; `qou-kl39` stays open with its next step
narrowed from "find a state→L map" to "test whether the Vassiliev filtration
degree supplies one, and whether it returns 0 on a single quark."

## Verification

- `lean`-direct v4.24.0 against restored Mathlib oleans: **exit 0**.
- `#print axioms` on all three theorems: `[propext, Classical.choice,
  Quot.sound]` — no `sorryAx`.
- **Negative control**: replacing `sub_eq_zero.mp hz` with `hz` makes the
  file fail, confirming the harness is not silently passing. (Recorded
  because `sorry` yields exit 0 with only a warning, so exit 0 alone never
  proves sorry-freeness.)
- 0 `sorry`, 0 `native_decide`, 0 `axiom` declarations.
- Generic `AddCommGroup` / `CommRing` (§7c): no ordering, no `Real`, no
  division, no characteristic hypothesis.
- CI unavailable repo-wide (auto-triggers disabled); the above is the gate.

## Corpus correction

`lepton-number-categorical-properties.md` asserted the grading as fact. That
paragraph is replaced with the obstruction, the scope note, and the pointer
to the filtration.

---

## Follow-up (same day): a stronger obstruction, and a correction to this audit

Testing the filtration direction suggested above turned up two things, one of
which corrects this document.

### 1. The Vassiliev filtration grades *invariants*, not *states*

`FiniteTypeInvariant.lean` defines `IsFiniteType (m : ℕ) (v : K → R)` and
`finiteTypeSubmodule m : Submodule R (K → R)`. The filtration is on the space
of **invariants** — functions `K → R` — not on knots. So it does not, on its
own, supply the state→`L` map that `Y = B − L` needs. The suggestion in
§"Where the repair probably lives" above was structurally confused on this
point, and is withdrawn in that form.

### 2. No function of the unframed knot type can work at all

Sharper, and it subsumes the grading obstruction. The corpus's own carrier
table assigns

| particle | carrier | `L` |
|---|---|---|
| `νₑ` | `K_{0₁}` (unknot) | `+1` |
| `ν̄ₑ` | `K_{0₁}^σ` (mirror unknot) | `-1` |

The unknot is **amphichiral** — it bounds a disk, so it is isotopic to its
mirror. The two rows therefore assign `+1` and `-1` to **the same knot**. No
function of the knot type can do that.

Proved in
[`LeptonNumberCarrierChirality.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/LeptonNumberCarrierChirality.lean):

| Theorem | Statement | Axioms |
|---|---|---|
| `no_lepton_number_on_amphichiral_carrier` | `mirror x = x` ⟹ no `L` with `L x = 1`, `L (mirror x) = -1` | **none** |
| `mirror_must_move_the_carrier` | such an `L` forces `mirror x ≠ x` | **none** |
| `chiral_carrier_admits_lepton_number` | `mirror x ≠ x` ⟹ such an `L` exists | `[propext]` |

The third theorem is what keeps this honest: the obstruction is **exactly**
amphichirality and nothing more. It rules out the unknot as the neutrino
carrier, not the idea of a knot-valued lepton number.

Note the charged rows are unaffected — the trefoil is chiral, so `T(2,3)` and
its mirror are genuinely different knots.

### The two repairs, and only two

1. **Give the neutrino a chiral carrier.** The unknot cannot work.
2. **Let `L` see the framing.** A framed unknot with framing `+n` and one with
   `-n` are distinct framed objects even though the underlying knot is
   amphichiral, so the mirror acts freely there.

Route 2 is the more interesting: the framing datum is `T(t)`
(`def:strand-twist-datum`), the same object the eightfold-way chapter carries
for hypercharge. If `L` needs framing and `Y` needs a framing-independent
second invariant, that is a constraint worth having explicit. Neither route is
pursued here.

`qou-kl39` stays open. Its next step is now: **pick a chiral neutrino carrier,
or define `L` on framed knots** — not "search for a state→`L` map".
