---
# qou-brng
title: 'OPEN KERNEL: derive that the saturated nuclear binding fraction = ℏ_q² (mass/binding rung)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:05:00Z
updated_at: 2026-08-30T07:33:05Z
---

Arc bk-crossing-coordination, item 3b→1 crux (PR #5346). The mass/binding ℏ_q-rung split was
attacked in `computations/binding_mass_rung_derivation_probe.py` /
`docs/audits/2026-08-21-binding-mass-rung-derivation.md`. What CLOSED:

- **Traced** — the mass multiplier's `1/ℏ_q²` is the CAL-2 muon-anchor cusp factor
  (`m_μ/m_e = Vol(4₁)/ℏ_q²`), not a free choice; the binding ansatz `B = m_e·Vol·M` does not
  re-apply it.
- **Proved (Lean, sorry-free)** — `QOU.Mass.BindingMassRung`: the analytic dichotomy — mass
  multiplier `lw/ℏ_q²` is an order-2 pole with residue `lw` (rest mass diverges as ℏ_q→0);
  `binding/mass = (M/lw)·ℏ_q² → 0` (binding is an O(ℏ_q²) quantum correction, regular at q=1).

What is OPEN (this bean): a **first-principles proof that the mass-difference cancellation lands
binding at EXACTLY the ℏ_q² rung** — i.e. that the *saturated* nuclear binding fraction `B/A/m_N`
is `ℏ_q²` and not merely `O(ℏ_q²)`. Empirically the fraction rises monotonically toward ℏ_q² with
A (²H 0.12·ℏ_q² → ⁴He 0.77 → ⁴⁰Ca 0.93 → ⁵⁶Fe 0.95·ℏ_q²); the ≈0.95·ℏ_q² Fe value is a scope-(a)
forward observation under the numerology guard, NOT a derivation.

Candidate routes:
- ~~The volume-defect picture `B = (m_e·lw/ℏ_q²)·ΔVol`~~ — **REFUTED 2026-08-21 (scope-a)**,
  `computations/binding_volume_defect_route_refuted.py`. The knot-volume defect `ΔVol/Vol` is O(1)
  (1.65 ³H, 2.00 ³He, 3.00 ⁴He), NOT O(ℏ_q²), so `B_pred ~ GeV`, overpredicting binding by 102–250×
  (≈1/ℏ_q²). Binding is not a mass-scale volume defect; the O(1/ℏ_q²) mass terms do not cancel to
  O(ℏ_q²) at the volume level.
- Why the coordination count `M` (integer, cusp-independent) is the correct binding multiplier
  while the mass carries the q-dim-weighted `lw` — a categorical statement about linking (mutual)
  vs self-energy (self-linking) amplitudes in the substrate. **Still open — the surviving route.**

**Updated verdict (2026-08-21):** with the volume-defect route refuted, the saturated-fraction
≈ ℏ_q² coincidence has lost its one candidate mechanism and is — on current evidence — **more
likely numerology than a derived prediction**. Do NOT wire the 0.95·ℏ_q² match; do NOT fit a
correction to force it to 1·ℏ_q². The honest state: analytic dichotomy proved (Lean); the exact
ℏ_q² saturation value is open AND now more suspect. Needs a genuinely new structural mechanism
(the linking-vs-self-energy route) or a scoped owner decision on whether it is worth pursuing.


---
**Update 2026-08-30 (session qou-d3i9, PR #6125).** Partial progress on the surviving
(linking-vs-self-energy) route — the TYPE question is resolved; two sub-questions stay open.

CORPUS CORRECTION that reframed it: the ³He/⁴He carrier L6a4 is BRUNNIAN (pairwise Gauss
lk ≡ 0), so M cannot be a linking number — it is a coordination COUNT (graph degree z=A−1).
The em-linking sibling thread proved the same obstruction (docs/audits/2026-08-01-em-linking-reads-round1.md,
O1 antisymmetry + topological-vs-metric pairing).

PROVED (Lean, sorry-free — QOU.Mass.BrunnianBindingChannel, built on the proved
CrossingEnergy.decomposition): the mutual crossing energy splits into a signed writhe/linking
channel (n₊−n₋=2·lk) and an unsigned count/coordination channel (n₊+n₋). For a Brunnian pair
n₊=n₋ so the signed channel is ZERO and the whole binding energy is the unsigned count channel,
strictly positive for a crossing pair at q>1 — binding SURVIVES the Brunnian vanishing where the
linking number does not. This is why M is a coordination count, discrete analogue of the
em-linking thread's "route around O1 is an UNSIGNED quantity" (Khesin Rmk 3.5). Audit:
docs/audits/2026-08-30-brunnian-binding-channel.md.

STILL OPEN (the sharpened kernel — a future attack aims here):
1. exact map n₊+n₋ → z=A−1 (the channel is proved; the coefficient is not);
2. why the surviving count channel enters as a BARE INTEGER while the self/mass channel keeps the
   full q-dim self-trace lw (self = closed quantum trace over Wedderburn channels; mutual = pairing
   of two fixed components, no internal channel sum — plausible but NOT proved);
3. the exact ℏ_q² saturation value stays numerology-suspect (unchanged; not touched, not forced).
