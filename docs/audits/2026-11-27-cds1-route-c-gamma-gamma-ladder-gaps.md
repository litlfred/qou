# Route C: what the γγ work of Nov 20–23 leaves undone of the 2026-10-11 ladder ask

Bean `qou-cds1`, route C (owner choice 2026-11-27, "Lean A + short C gap audit"). Companion to
route A, `QOU.MassTheory.ClimbingFamilyNeutralExclusion`.

## The ask

Owner, 2026-10-11, verbatim (bean `qou-4f8t`): *"let's go through gamma-gamma production step
by step to get to one and two nucleons. each collision/interaction shifts things up the
tower."* As scoped on 2026-11-14: build the H₆→H₃ (one nucleon) and H₁₂→H₆ (two nucleon)
ladder with quark letters, and record the γγ residue per step with no magnitude expectation.
Binding rulings: gluon tail allowed (2026-10-11); "every level" means every strand count
(2026-10-12); quark signs are to be derived, not picked (2026-10-12, 2026-11-22).

## What later work delivered, and what it did not

| piece of the ask | delivered by | status |
|---|---|---|
| one-nucleon **endpoint** in H₃ | `GammaGammaNeutralSelectionAllN` (Nov 22): among words of the ruled photon grammar on 3 strands, neutrality + reading 3 select `V³ = β_Bor`, every length | **done**, but as a selection *inside* H₃ |
| one-nucleon **descent** H₆→H₃ | nothing | **open**. That file's scope says "Three strands only. Four or more strands is a different grammar and is not covered." No construction starts from collisions on more strands and descends. |
| quark letters on the nucleon | production blocks `proton = V³·S A A S S`, `neutron = V³·A A I S S` (`light_nuclei_a2_a3/hecke_flint.py:130`) | **open**. The five letters after `V³` are not γγ-selected; the owner ruled the quark charges must be derived (2026-11-22). |
| two-nucleon level | light-nuclei chain (Nov 22, `2026-11-22-light-nuclei-a2-a3-gg-chain.md`): two finished 3-strand blocks joined by a ruled `V³` bond on 6 strands | **partly**. It is a two-nucleon word, but built by placing blocks, not by H₁₂→H₆ descent. Result: the chain unbinds for every q > 1 (scope (b), invariant `μ_x − 1 > 0`). |
| γγ residue per step | Nov 14 scalar-per-step probe (`gg_scalar_per_step_probe.py`): `q²` per step on the `e₀e₂Σ₁ᶜ` family | **withdrawn**. Route A proves that family is removed by term-by-term neutrality for every c ≥ 1, so that residue is not a residue of the ruled grammar. Nothing is recorded for the ruled grammar on ≥ 4 strands. |
| lepton pair coupling (for Q_β) | `2026-11-23-qbeta-gg-pair-gb-reduction.md`: the pair word reduces by braid relations only, has no nucleon strand | **open**. The word coupling the pair to a nucleon is an owner input. |

## What route A changes for C

Term-by-term neutrality forces writhe 0 on every kept word. Any ladder step built from
positive cabled crossings (like `Σ₁`) is removed whole. So a ladder that respects the ruling
can only climb through writhe-0 letters such as `V = σᵢσᵢ₊₁⁻¹`, and the magnitude it carries
has to come from those, not from a per-step `q²`.

## What would close C (not started; for the owner)

1. Extend the neutral selection of `GammaGammaNeutralSelectionAllN` to the ruled photon grammar
   `γᵢ`, `i = 0..4`, on 6 strands: enumerate neutral words, apply reading 3, record survivors.
2. Define the H₆→H₃ step as the Ocneanu conditional expectation at `z_D` and record the residue
   of each survivor, with no magnitude expectation.
3. Repeat for H₁₂→H₆ with two nucleons.

Steps 1–3 give quark letters only if the survivors carry them; whether they do is the measurement.
No number in this note is compared to experiment.
