# The ³H–³He mirror-split 1/3 factor: datum only — the S₃/Milnor multiplicity is structural, the unit Coulomb/strong coefficient is not derived

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** FINDING (reproducible, no fit). Formalize-first test of the candidate
mechanism named by the redirect audit
([`2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md`](2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md)):
*"If `1/3` were derived (e.g. one active pair among three Borromean components,
or a color factor) it would close target 1."* Verdict: **it does not close** —
the multiplicity has a structural candidate origin, but one mechanism step is
missing and in tension with the already-derived Coulomb/strong ratio.

Probe: [`computations/deltalambda/mirror_split_milnor_one_third_probe.py`](../../computations/deltalambda/mirror_split_milnor_one_third_probe.py)
(witness [`mirror-split-milnor-one-third.witness.json`](../../computations/deltalambda/mirror-split-milnor-one-third.witness.json),
4/4 assertions pass, mpmath at the production floor).

## The mechanism, decomposed (formalize-first, compute-author §3.3)

The claim `split = B_pp/3` factors into three steps. Each was checked against
the proved/structural corpus **before** any numerics:

| step | statement | status |
|---|---|---|
| **S1** | ³He's link L6a4 = Borromean has all pairwise linking numbers 0 and Milnor `μ̄(123) = ±1`; a pairwise linking-mediated EM coupling is structurally zero, so any linking route to the Coulomb split is triple-channel | **PROVED, exact** — recomputed by the validated integer Magnus machinery of [`binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py): `lk = (0,0,0)`, `μ̄(123) = +1` |
| **S2** | the 1/3 multiplicity: an S₃ component-permutation-equivariant weight on the Borromean link's 3 components/pairs is equal = 1/3 each; exactly one pair (pp) is EM-active in ³He | **structural, conditional** — sourced only from the S₃ symmetry of the link itself; **not** supplied by the equal-weight coordination result (see below) |
| **S3** | the EM-active energy per pair-channel equals the **full** strong per-block bond `B_pp` (unit Coulomb/strong coefficient), so `split = 1·B_pp·(1/3)` | **UNPROVED — the gate.** The only derived Coulomb/strong ratio in the corpus is `tanh(ln q₀) ≈ 0.10396` (`def:coulomb-charge`, [`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md)), not 1 |

### Why the equal-weight witness does NOT supply S2

The check requested ("does `bond_extensivity_equal_weight` already prove
per-pair equal weights?") comes out **negative**, twice over
([`bond-extensivity-equal-weight.witness.json`](../../computations/bond-extensivity-equal-weight.witness.json)):

1. Equal weight **fails at the nucleon level** — the derived #2089 bond
   energies have a `ε_nn/ε_pp = 1.781×` spread (recomputed in the probe);
   equal weight is exact only for identical α–α bonds.
2. Even where equal weight held, it predicts **zero** mirror split: both A=3
   mirrors get `3·⟨ε⟩`. Equal weighting of the *strong* bond energies cannot
   produce a split at all.

So the precise statement S2 needs is different from what the equal-weight
witness proves: it must be a claim about an **EM coupling functional defined
on the link components** (where the S₃ symmetry of L6a4 genuinely forces
1/3 per component/pair), not about the charge-labelled strong bonds (where
the symmetry is broken by construction). That link-level functional is not
yet defined in the corpus — it is the same open "EM-linking / geometric"
object the redirect audit points at.

## Numbers (probe output; nothing hardcoded)

| quantity | value | provenance |
|---|---|---|
| `B_pp` (per-block H₆ diproton, free − interacting) | **2.286088 MeV** | recomputed via the exact code path of [`charge_coulomb_tn3he_derived.py`](../../computations/charge_coulomb_tn3he_derived.py); matches its witness `2.2860881` to 3×10⁻⁷ relative (dps difference 30→50) |
| AME split `B(³H) − B(³He)` | **0.763755 MeV** | `codata_constants._ame_binding_mev(1,3) − (2,3)` (AME2020) |
| `split/B_pp` | 0.334088 | |
| `split·3/B_pp` | **1.002265** (deviation **+0.226%**) | the guarded datum |
| `tanh(ln q₀)` | 0.103964 | derived Coulomb/strong ratio |
| tanh-route coverage `tanh(ln q₀)·B_pp / split` | **31.12%** | the derived piece of [`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md) |
| 1/3-route coverage `(B_pp/3) / split` | **99.77%** | the near-match |

**The tension, explicitly:** the two pieces are **competing, not additive** —
together they would cover 130.9% of the split. The tanh route is *derived*
(from `def:coulomb-charge`, q₀-only) and covers 31%; the 1/3 route is a
*near-match* covering 99.8%. For `split = B_pp/3` to be the story, the derived
`tanh(ln q₀)` coefficient would have to be **superseded** at the triple channel
by a unit coefficient — and no derivation does that. They cannot both stand.

**Numerology-guard datum (reported, not identified):** `tanh(ln √2) = 1/3`
*exactly* (`(2−1)/(2+1)`; verified to 10⁻⁷²). I.e. the derived Coulomb/strong
*form* evaluated at `q = √2` instead of `q₀` reproduces the 1/3 — and
`√2 = 1/x*` where `x* = 1/√2` is the deuteron Borel-singularity coupling of
target 2 in the same redirect audit. Two coincidences sharing a `√2` is still
a coincidence pattern: no derivation moves the evaluation point off the
substrate `q₀`. Filed under the numerology guard alongside `0.3341 ≈ 1/3`.

## Classification (anti-fit discipline, STRICT)

**(ii) Datum only — mechanism step S3 missing.** Scope-(a) phrasing:

> The candidate mechanism "one active pair among three Borromean components,"
> **as it stands, does not derive** `split = B_pp/3`. Its multiplicity piece is
> structurally available (S1 proved exact: pairwise linking vanishes, coupling
> is triple-channel; S2 conditional on an S₃-equivariant link-level EM
> functional not yet defined). The missing step is **S3: a derived unit
> Coulomb/strong coefficient at the triple channel** — which would also have to
> supersede the derived `tanh(ln q₀) = 0.104`. Until S3 (or a replacement
> derivation of the triple-channel coefficient) exists, `split/B_pp = 0.3341 ≈
> 1/3` (0.23%) remains a **datum** constraining the open EM-linking magnitude.

This is a scope-limited negative: nothing here excludes the 1/3 *ingredient* —
the probe measures exactly which step a future derivation must supply. What is
excluded (by the arithmetic above) is holding **both** the derived tanh route
and the 1/3 route as simultaneous full stories.

Not derived ⇒ not wired: no production change, no tier change, no content-block
edit. The pp-Coulomb block status remains as stated in the redirect audit
(derived 31% + open geometric/Milnor scale).

## What would close it (for the next agent)

1. Define the **link-level EM coupling functional** on the components of
   `𝓑_{³He}` (the object S2 needs) — S₃ equivariance then *derives* the 1/3
   multiplicity structurally.
2. Derive its **magnitude**: show the triple-channel (μ̄-mediated) Coulomb
   coefficient per active pair is 1 (in `B_pp` units), or derive whatever it
   actually is — replacing, not coexisting with, the pairwise-derived
   `tanh(ln q₀)`. This is the same "derived magnitude/scale" gate the redirect
   audit identifies as the single obstruction across targets 1 and 2.
3. If a derivation instead lands on the `q = √2` evaluation point
   (`tanh(ln √2) = 1/3` exactly, `√2 = 1/x*`), it must derive the evaluation
   point — until then that identity stays under the numerology guard.

## Files

- probe: [`computations/deltalambda/mirror_split_milnor_one_third_probe.py`](../../computations/deltalambda/mirror_split_milnor_one_third_probe.py) (new)
- witness: [`computations/deltalambda/mirror-split-milnor-one-third.witness.json`](../../computations/deltalambda/mirror-split-milnor-one-third.witness.json) (new, audit-only, 4/4 pass)
- this audit: `docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md`
- context consumed (unchanged): [`2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md`](2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md), [`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md), [`computations/binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py), [`computations/bond_extensivity_equal_weight.py`](../../computations/bond_extensivity_equal_weight.py), [`computations/mirror_split_coulomb_diagnosis.py`](../../computations/mirror_split_coulomb_diagnosis.py), [`computations/charge_symmetric_coulomb_binding.py`](../../computations/charge_symmetric_coulomb_binding.py), [`computations/gap2_borromean_triple_count.py`](../../computations/gap2_borromean_triple_count.py)
