# The two open binding knobs, correctly scoped: the A=3 split is geometric/Milnor (not pairwise), the deuteron coupling sits at the Borel singularity

**Date:** 2026-07-13 · **Branch:** `claude/a3-mirror-derived-and-deuteron-coupling-2026-07-13` ·
**Type:** FINDING (reproducible, no fit). Advances — but does **not** close — the
two derivation targets left open by the CKRecursion resolve (#3723) and the
deuteron trans-series negative (#3736). Both remain gated on objects the
framework does not yet supply; this records *where* each gate actually is.

## Target 1 — a derived replacement for the inserted ³H–³He split

**State (checkcorpus).** The split is Coulomb, not SU(4): charge-symmetric
strong binding + the two-proton Coulomb repulsion in ³He
([`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md),
`def:coulomb-charge`). The derived piece is
`E_coul = tanh(ln q₀)·B_pp = 0.1040 · 2.2861 = 0.2377 MeV`, **31.1%** of the
`0.7638 MeV` split, zero fit. The remaining **3.21×** was named "the per-pair
EM-linking invariant, not yet defined."

**New observation (the redirect).** ³He's link is **L6a4 = the Borromean rings**,
whose **pairwise linking number is 0** for every pair. So the two protons'
*per-pair* EM-linking invariant is **structurally zero** — a pairwise topological
proxy *cannot* carry the Coulomb split. This explains why the derived 31% comes
entirely from the strong-bond proxy `B_pp` and none from linking, and it
**re-scopes the open gate**: the Coulomb split must come from a **geometric**
quantity (the hyperbolic cusp separation of the two proton components in L6a4) or
the **Milnor triple-linking** `μ̄(123) = ±1` (the *defining* Borromean invariant,
nonzero where all pairwise ones vanish) — **not** a pairwise invariant. Future
work on target 1 should stop searching for a pairwise EM-linking object and build
the geometric / Milnor one.

**Data, not identified (numerology guard).** The effective Coulomb/strong ratio
the full split needs is `split/B_pp = 0.3341`, which is within `0.2%` of `1/3`.
Reported as a datum only: a single-number near-match is not a derivation, and
tuning any pp-Coulomb constant to `0.764 MeV` would be a CAL-4 fit (forbidden).
If `1/3` were *derived* (e.g. one active pair among three Borromean components, or
a color factor) it would close target 1 — but that derivation is not in hand.

**The Reeb coordinate is the geometric candidate — but bare, it undershoots
~270×.** The framework's geometric phase is the q-Reeb coordinate
`θ_λ = arccos(χ^λ/d_λ)`, which *can* carry the Borromean/triple information the
pairwise linking cannot. Tested parameter-free (Markov-weighted, cached
`χ^λ`/`y_λ`): the mirror difference is
`m_e·Σ y_λ(θ_λ^{³H} − θ_λ^{³He}) = 0.0028 MeV = 0.37%` of the `0.7638 MeV` split
— i.e. the bare Reeb phase gives the right object but is `~270×` too small. This
reproduces the corpus's retraction of the "θ_λ closes the mirror to 2%" claim as
a **C_knot scale fit** (PR #1417): the Reeb coordinate names the geometric object
and gets the shape, but its **magnitude needs a scale that is not derived** —
tuning it is the forbidden fit.

**Net for the block.** The honest replacement for the CKRecursion's inserted
`1.4947 m_e` is: *charge-symmetric strong + 2p Coulomb, of which `tanh(ln q₀)·B_pp`
= 31% is derived; the geometric object is the Reeb coordinate `θ_λ` (Borromean-
capable, pairwise route provably empty), but its bare magnitude undershoots ~270×
— the open piece is the θ_λ **scale**, not the mechanism.* That is the accurate
status — not "exact SU(4) closure."

## The unifying gate — magnitude, not mechanism

Every parameter-free object tried this session gets the *shape/sign* right and
**undershoots the magnitude** by a scale factor: the deuteron resummation ~37×
(#3736), the sgn·dim Δ_λ base 70–89% (#3723), the Reeb-phase mirror ~270×, the
derived Coulomb 3.21×. The recurring open gate is the same one — a **derived
magnitude/scale** (the "C_knot" / EM-linking / entanglement-coupling object)
that the framework's topological+geometric data determine up to normalization but
do not yet *fix*. That is the honest single obstruction behind both targets, and
behind the A≥3 θ_λ magnitude gate (`2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md`):
mechanism derivable, magnitude open.

## Target 2 — a derived coupling for the deuteron entanglement-dual resummation

**State (#3736).** The full level-1/2 Borel–Laplace resummation of the Gevrey-1/2
binding period reaches `B_D = 2.225 MeV` only as the coupling `x → 1/√2 ≈ 0.707`,
the Borel singularity; at every substrate-fixed coupling (`ℏ_q² , ℏ_q , t = ln q₀
≈ 0.10`) it undershoots ~37×. So the "one free knob" is the coupling, and a
closure needs `x` **derived** at `≈ 0.707`, not at the substrate `≈ 0.10`.

**Assessment.** There is no derived reason for the deuteron coupling to sit at
`1/√2` rather than the substrate `ℏ_q`. The value `1/√2` is the *Borel radius*
(an internal feature of the period's growth), not an external coupling — pinning
`x = 1/√2` would be identifying the coupling with the singularity, which is
circular, not a derivation. Unless the entanglement-dual frame supplies an
*independent* `x` (e.g. a Hopf-link entanglement parameter derived from the
substrate that happens to equal `≈ 0.707`), the route stays a one-parameter fit.
Target 2 is therefore gated on a **derived entanglement coupling**, and the
honest current answer for the deuteron remains the separate q-rotational
`μ₀·ℏ_q·J_q²` channel (`B_D` to −9%, 0 params), not the resummation.

## Honest scope

Neither target is closed. Both are advanced by *correctly locating the gate*:
target 1's is geometric/Milnor (the pairwise route is provably zero — Borromean);
target 2's is a derived entanglement coupling (the substrate value undershoots
37×, and `1/√2` is the period's own singularity, not an external input). No fit;
no wiring; no tier change. The `0.3341 ≈ 1/3` and `x* ≈ 1/√2` coincidences are
reported as data under the numerology guard.
