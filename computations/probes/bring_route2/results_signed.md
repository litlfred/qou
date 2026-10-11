# Route 2 correction: the seen candidates were analysed without their signs

> **Update 2026-10-11 (`results_pure.md`):** §3 below describes the old route 2 rule. Under the pre-registered pure-braid rule, every γγ word gets a well-defined Bring loop (the core: L = 16.1692), because all three placements agree.

Producer: `signed_candidates_probe.py`. 5/5 checks pass. SL(2,ℤ) arithmetic is exact (integers); Bring lengths use mpmath. No Q_β, CODATA or mass input.

This is a correction measurement, not a selection: nothing here is ranked.

## 1. What went wrong

Route 2 and options 1, 1b, 1c and 1d took the "seen candidates" from `qbeta_candidate_closures_are_links_probe.CANDIDATES`.

- **That list records only which generator each letter uses.** For example, nuc9 = `[0,1,0,1,0,1,0,0,1]`.
- **The sign was dropped on purpose there**, and correctly: that probe counts link components, and the strand permutation does not see the sign.
- **Route 2 does see it.** In SL(2,ℤ), σ₁ maps to L = [[1,0],[−1,1]] but σ₁⁻¹ maps to L⁻¹ = [[1,0],[1,1]].

The canonical nucleon, `pyhecke.atom.build_nucleon_nf`, is, for the proton:

    (σ₀σ₁⁻¹)³ · σ₀ [uu] · ½(σ₀ + σ₀⁻¹) [ud] · ½(σ₁ + σ₁⁻¹) [ud] · σ₀σ₀ [gluon]

For the neutron, the uu letter σ₀ becomes the dd letter σ₀⁻¹. This differs from the list route 2 used in two ways:

- the γγ core has **σ₁⁻¹**, not σ₁;
- each ud letter is an **average** of σ and σ⁻¹, so the nucleon is **a sum of four braids**, not a single braid.

## 2. What route 2 gives on the actual element

| | SL(2,ℤ) trace | Bring loop | L |
|---|---|---|---|
| route 2's sign-erased nuc11 (what options 1 to 1d used) | 2 (parabolic) | **none** | — |
| proton term, σ₀⁺ σ₁⁺ | −26 | loop | 9.2064 |
| proton term, σ₀⁺ σ₁⁻ | 126 | loop | 15.9431 |
| proton term, σ₀⁻ σ₁⁺ | 16 | loop | **6.3677** |
| proton term, σ₀⁻ σ₁⁻ | 52 | loop | 20.4442 |
| neutron term, σ₀⁺ σ₁⁺ | 16 | loop | 6.3677 |
| neutron term, σ₀⁺ σ₁⁻ | 52 | loop | 20.4442 |
| neutron term, σ₀⁻ σ₁⁺ | 58 | loop | 23.0159 |
| neutron term, σ₀⁻ σ₁⁻ | −22 | none (elliptic/parabolic in Δ(2,4,5)) | — |

In each term, the first sign is that of the σ₀ from the first ud letter and the second is that of the σ₁ from the second.

**Every proton term has a Bring loop, and three of the four neutron terms do.** The sign-erased word route 2 used is parabolic and has none.

## 3. γγ words under route 2

On three strands, every γγ word is (σ₀σ₁⁻¹)^k (`QOU.Mass.AltCharShiftMultiset`, sorry-free). The vertex σ₀σ₁⁻¹ maps to [[2,1],[1,1]], so its k-th power is a Fibonacci matrix with trace L₂ₖ: 3, 7, 18, 47, 123, 322. Every power is hyperbolic, so each γγ word is a genuine closed geodesic on the modular surface.

**Route 2's rule never gives a γγ word a Bring loop, and the reason is the rule, not the geometry.**

Route 2 picks the Γ₀(2)-conjugate by requiring the strand permutation to fix exactly one point of P¹(F₂).
- **If 3 ∤ k**, the permutation is a 3-cycle and fixes no point. The element lies in no conjugate of Γ₀(2), so route 2 cannot place it at all.
- **If 3 | k**, the γγ core included, the braid is pure and fixes all three points. It lies in every conjugate. The rule as written ("exactly one") then declares it out of scope, although all three choices are available.

So the answer to "does the γγ construction force a Bring loop?" is: **not under route 2 as pre-registered, because route 2 cannot see γγ words.** That is a limit of route 2's subgroup rule, scope (a).

## 4. What this changes

**Withdrawn.** Every statement in route 2 and options 1 to 1d about the *seen candidates* concerned sign-erased words, not the scored element. That includes the 2026-10-11 read-across: "Rule A picks the braid of nuc11_interleaved; Rule B picks class A". The same holds for `results.md` §0's "γγ core Δ² = (σ₀σ₁)³ maps to −I": the actual core is (σ₀σ₁⁻¹)³ ↦ [[13,8],[8,5]], which is hyperbolic.

**Unaffected.** The results about **fresh positive words** stand as statements about positive words:
- loops tie (option 1);
- equal length means the same loop (1b);
- word classes collapse into braids (1c);
- both rules are decided at 11 letters (1d).

How much positive words bear on the real element is now an open question, because the real element is neither positive nor a single braid.

**Route 1 has the same problem.** Route 1, `../ohara_link_energy/` (the O'Hara energy probe, PR #7582), labels its candidate list "corpus words, verbatim" (`braid_topology.py:131`, `run_candidate.py:8`), but the list is the same sign-erased one. Route 1's linking numbers and self-writhes depend on the signs, so its candidate rows likely need redoing too. That route belongs to another thread, and this file does not edit it. The q-length probe imports `R2.CANDIDATES` and is covered by the withdrawal above.
