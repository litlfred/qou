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

### 2. A level constraint — and a correction I had to make

My first reading of this was wrong, and the author caught it. I claimed the
corpus's carrier table was internally inconsistent: it sends `νₑ` to the
unknot with `L = +1` and `ν̄ₑ` to the *mirror* unknot with `L = -1`, and the
unknot is amphichiral, so those rows appeared to assign `+1` and `-1` to the
same knot.

**That reading is wrong.** The corpus's antiparticle operation
(`QOU/Torsion/antiparticle_crossing_reversal.lean`) is
`mirror : Braid → Braid`, the involution `σᵢ ↦ σᵢ⁻¹` on **braid words**, and
it explicitly records `impl_topological_mass_invariance` — *"the mirror
preserves the knot type"*. What separates particle from antiparticle there is
the crossing energy under the bar involution `q ↔ q⁻¹` (`E_anti = -E_bar`)
and the Coulomb charge, both valued in `R`. The corpus therefore already
holds that the knot type does *not* distinguish them, and the labels
`K_{0₁}` / `K_{0₁}^σ` denote braid-level (framed) objects. "Unknot" is a
projection that discards exactly the writhe/framing data doing the work.

At `q₀ ≈ 1.11 > 1` the bar involution is non-trivial, so nothing here is
fixed by the mirror and the obstruction does not fire.

What survives is a **level constraint**, proved in
[`LeptonNumberCarrierChirality.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/LeptonNumberCarrierChirality.lean):

| Theorem | Statement | Axioms |
|---|---|---|
| `no_lepton_number_on_amphichiral_carrier` | `mirror x = x` ⟹ no `L` with `L x = 1`, `L (mirror x) = -1` | **none** |
| `mirror_must_move_the_carrier` | such an `L` forces `mirror x ≠ x` | **none** |
| `chiral_carrier_admits_lepton_number` | `mirror x ≠ x` ⟹ such an `L` exists | `[propext]` |

Read correctly this is **scope-(a)**, not scope-(b): `L` cannot factor
through the *unframed knot type*, so it must be defined where the mirror acts
freely — braid word, framing, or the `q`-side. The corpus already works
there. The third theorem bounds the claim: the obstruction is *exactly*
mirror-fixedness and vanishes the moment the carrier moves.

### The tension worth recording

If `L` needs **framing** to separate particle from antiparticle, while the
eightfold-way hypercharge programme needs a second invariant *independent* of
the framing/writhe, then `L` and that invariant cannot be the same datum.
Both requirements are now explicit; the compatibility question is open.

`qou-kl39` stays open. Next step: define `L` at braid/framing level and check
it returns `0` on a single quark — not "search for a knot invariant".

---

## Resolution (2026-08-10): the carrier is the braid word, and it was never missing

`sm-open-problems.md` records "framework braid words per chiral fermion still
missing" as the blocker. They are fixed by the corpus's own `chi = -6`
constraint: `T(2,n)` with odd `n <= 7` exhausts the fermion spectrum, and
`T(2,n)` **is** the closure of `sigma_1^n`. So the carriers are
`nu_e = sigma_1`, `e- = sigma_1^3`, antiparticles `sigma_1^-1`, `sigma_1^-3`;
the hadron words (`gluon unit sigma_0 sigma_1^-1`, `B_3 = its cube`) were
already there.

Proved in `ChiralFermionBraidWords.lean` (all `[propext]` only except one):

| Theorem | Content |
|---|---|
| `writhe_sigma1Pow_carriers`, `writhe_gluon`, `writhe_borromean` | writhes **derived** from the words; gluon unit and `B_3` are writhe `0` |
| `mirror_moves_carrier` | on all four carriers `n ∈ {1,3,5,7}` the mirror changes the writhe — the chirality obstruction is **discharged** |
| `leptonNumber_matches_corpus` | `L = sign(writhe)` reproduces **6/6** stated rows |
| `Y_not_factoring_through_writhe` | baryon and gluon unit at **equal derived writhe 0** with different `B` ⟹ `Y` is not a function of `w` |
| `Y_eq_B_sub_L_left_handed` | conditional on the quark writhe, the four LH rows come out right |

Two consequences worth recording.

**The chirality obstruction is discharged, exactly as predicted.** `nu` and
`nubar` are `sigma_1` and `sigma_1^-1` — different braid words that both close
to the amphichiral unknot. The braid word is the carrier; the knot type is the
projection that loses the distinction.

**The writhe-independence requirement is now closed from derived premises.**
`sm-hypercharge-invariant.lean`'s `exists_writhe_degenerate_pair` and
`SecondCrossingInvariant.lean`'s `baryon_vacuum_separating` both *assumed* a
writhe-degenerate pair. The gluon unit and `B_3` supply one with the writhes
**computed from the braid words**. So the requirement stands — on a correct
argument, replacing the p/n non-sequitur documented in
`2026-08-10-writhe-independence-criterion.md`.

**The framing collision dissolves.** `L = sign(w)` is writhe-*dependent*, which
is consistent: `Y = B - L` still does not factor through `w` because `B` varies
at fixed `w`. The invariant that must be independent of the writhe is `B`
(`mu-bar_123`), not `L` — and `L` needs the braid word, which carries writhe,
not a free framing datum. So `tr_M`'s writhe prefactor and the strand-twist
datum `T(t)` are answering different questions, and `L` needs neither.

**Not a closure.** `sign` is a choice, not derived. The **quark braid word is
still genuinely absent** — every quark row rests on assuming its writhe is `0`.
Chirality `u_L` vs `u_R` is unrepresented. `qou-kl39` stays open, with the
blocker narrowed from "braid words per chiral fermion" to "the quark braid word
and a chirality grading".

### Red-team pass: the candidate is refuted as a link function

`L = sign(writhe)` matching 6/6 rows is weaker evidence than it looks, and it
fails a test the corpus itself imposes.

**It is close to circular.** The carriers were assigned as `sigma_1^n` for
particles and the mirror `sigma_1^-n` for antiparticles, and `L = ±1` *is* the
particle/antiparticle label. So `sign(writhe)` recovering it is largely the
assignment read back out — the same definition-unfolding failure mode caught in
`TwistBatteryVacuity.lean`. The only rows carrying independent content are the
two writhe-`0` hadrons.

**It is refuted as a state function on links.** Markov II sends `β` to `βσ_n`
with the same closure and raises the writhe by `1`. The baryon has writhe `0`,
so its stabilisation has writhe `1` and `L` jumps `0 → 1`. Conservation clause 3
of `lepton-number-categorical-properties.md` requires `ΔL = 0` under Markov
moves. Proved: `leptonNumber_not_markov_invariant`.

**The one escape** is that states are Gröbner–Shirshov normal forms
(`mba-step02-gs-reduction.md`: "every downstream algorithm consumes `NF(w)`, not
the raw braid"), fixing a canonical representative so Markov moves do not act
within the state space. Then `L = sign(writhe)` is well-defined — but clause 3
is then about a different object, and which one is unresolved.

Net: the braid-word carriers and the derived writhe-`0` pair stand (they close
the writhe-independence requirement). `L = sign(writhe)` does **not** stand as a
link invariant.
