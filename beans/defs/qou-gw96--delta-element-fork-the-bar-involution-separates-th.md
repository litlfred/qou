---
# qou-gw96
title: 'Delta element fork: the bar involution separates the two models — Delta_S is exactly bar-odd, Delta_L has no definite parity'
status: in-progress
pr: 8268
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T00:50:31Z
updated_at: 2026-10-04T15:12:17Z
parent: qou-v2om
---

## Measured (scope-(a)), `qbeta_delta_bar_parity_probe.py`, 14/14

`ConventionDAdmissibleRoots.lean` settles the FUNCTIONAL side of the fork
(exactly two admissible Markov parameters, z ∈ {q, z_D}; z_C and z=1 both
excluded by the same criterion). This measures the ELEMENT side.

**Q1 — does the descent criterion pick an element? NO.**
The element analogue would be "vanishing (1³) component, i.e. lives in the
two-row Wenzl quotient". Neither Δ does:
χ^(1,1,1)(Δ_S) = (q−1)(q+1)(q²+1)/(2q²) ≠ 0, χ^(1,1,1)(Δ_L) = −0.171539 ≠ 0.
The admissible-root criterion is about the functional alone.

**And the fork SURVIVES descent** — it is not a convention artefact.
χ^(2,1)(Δ_S) = 0 while χ^(2,1)(Δ_L) = −0.106814 ≠ 0, so the two differ
already in the two-row part: no admissible functional identifies them, and
no rescaling does either. Confirmed from the functional side — tr_M differs
at z = q (−0.210199 vs −0.260388) AND at z = z_D (−0.106236 vs −0.158016).
Consequence: the adjudication CANNOT be deferred to the z-side.

**Q2 — a different canonical criterion DOES separate them.**
The Kazhdan–Lusztig bar involution (ring hom, bar(q)=q⁻¹, bar(T_s)=T_s⁻¹;
verified here to be an involution on all six basis elements and independent
of the reduced word):

* **Δ_S is EXACTLY bar-odd**, bar(Δ_S) = −Δ_S, identically in q.
* **Δ_L has no definite bar parity** — neither odd nor even; its bar-even
  part is nonzero (counit −0.039565), and its bar-odd part is NOT a multiple
  of Δ_S, so Δ_S is not recoverable from Δ_L by projection.

**The stronger form — bar-oddness FORCES the coefficient the ladder uses.**
On the corpus's own shape x = c·1 + d(σ₀+σ₁) (symmetric under the diagram
automorphism), bar(x) = (c̄ − 2h·d̄) + d̄(σ₀+σ₁), so bar(x) = −x reduces to
exactly two equations: d̄ = −d, and c + c̄ = −2hd. The corpus's d = −h/2
already satisfies the first. The second then forces the **bar-even part of c
to be exactly h²/2** — adding the bar-odd h keeps it bar-odd, adding the
bar-even h² destroys it — leaving c's bar-odd part free. And h²/2 is not an
incidental coefficient: net(Δ_S) = h²/2 − h = εNPq, the counit the published
ladder is built from. So h²/2 is DERIVED from the involution, not fitted.

## Honest scope — what this does NOT establish

Bar-oddness is a canonical criterion (KL) and the framework independently
asserts Q_β is the bar-odd sinh partner of the bar-even cosh meson scale
(AGENTS.md canonical chain); bean `qou-quv8` records μ₀ ∝ (q−q⁻¹) bar-odd on
the same convention. But **whether that stated bar-odd character is a
requirement on the ELEMENT or only on the OBSERVABLE is exactly the open
question**, and this probe does not settle it. Disclosure: the criterion was
suggested by noticing χ(Δ_S) = (a, 0, −a) before the involution was tested —
the criterion has independent standing, the order of discovery does not.

Nothing is wired; no c_k is proposed; the fork is NOT adjudicated here.
Remains an owner call.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
