# ³He brane-tower charge-asymmetry + pair-knot composite — synthesis & open-item scope

**Date:** 2026-06-18
**Status:** EXPLORATORY synthesis. No production rewire, no fit, no fourth calibration.
**PR:** #2478
**Witnesses:**
[`he3-tower-charge-asymmetry.witness.json`](../../computations/he3-tower-charge-asymmetry.witness.json),
[`he3-pairknot-composite-lp.witness.json`](../../computations/he3-pairknot-composite-lp.witness.json)

## Purpose

The #2467 ³He structural-gap diagnosis closed with a *fix direction* — "an
LP-dual pair-knot composite for the proton near-pole pair + an explicit Z(Z−1)
Coulomb term". This doc executes the corpus-grep that #2467 did not, connects
three already-existing threads, and reports an honest, non-fit verdict on what
is **done**, what is **open**, and what is **forbidden** in that fix direction.

## The three threads (corpus-grep first)

1. **The brane-tower charge-asymmetry** (#2467 + this PR's Deliverable 1).
   The per-generator brane tower `Σ_i −Li₂^q(−|V̂_i^full|)` is *charge-asymmetric
   the wrong way* for the A=3 mirror pair.

2. **The structural Coulomb (already derived, ~31%).**
   [`def:coulomb-charge`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md)
   gives `Q(𝔥) = ½(n₊−n₋)`, a crossing-energy split with Coulomb/strong ratio
   `tanh(ln q)`;
   [`prop:coulomb-strong-ratio-q-rational`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-strong-ratio-q-rational.md)
   proves (Lean) `tanh(ln q) = (q²−1)/(q²+1)` for `q>0`.
   [`charge_coulomb_tn3he_derived.py`](../../computations/charge_coulomb_tn3he_derived.py)
   applies these: the derived pp-Coulomb reduction `tanh(ln q₀)·B_pp ≈ 0.238 MeV`
   covers **~31%** of the 0.764 MeV T−³He split — right sign, right order, 3.2×
   short. Its own docstring flags: *"a concrete close beyond this would be a
   CAL-4 fit"* — i.e. **forbidden** (Δ_λ gate).

3. **The no-κ proof.**
   [`mirror_isospin_coulomb_split.py`](../../computations/mirror_isospin_coulomb_split.py)
   proves symbolically that the categorical chirality split (`A⁻¹`) and the
   Coulomb split (`A⁻¹ᐟ³`) share the isospin factor `Z(Z−1)−N(N−1)` but scale
   differently, so **no constant rescaling κ** maps one onto the other; the
   Coulomb length `r₀ ≈ 1.5 fm` is the pion Compton wavelength (CAL-3 consistent).

## Deliverable 1 — the brane-tower asymmetry, quantified

| atom | tower `Σ−Li₂^q(−|V̂_i|)` |
|------|--------------------------|
| deuteron | 3.393 |
| tritium (1p2n) | 5.072 |
| ³He (2p1n) | 5.350 |

- `Δtower = tower(³He) − tower(³H) = +0.278` — **favors ³He, the wrong sign**
  (³He is the *less*-bound mirror member).
- Fractional asymmetry `Δtower/tower(³H) = 5.49%` (scale-free; the sign is the
  rigorous result).
- At the canonical scale `E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV`,
  `E₀·Δtower = 1.165 MeV` = **1.53× the entire physical Coulomb split (0.764 MeV)**.

**Reading.** A charge-symmetric force (which the strong interaction is) must give
`tower(³He) ≈ tower(³H)`. The brane tower instead carries a *spurious* asymmetry
that is not a small correction — it is larger than the split it would corrupt,
and opposite-signed. So a ³He-reducing Coulomb term would have to overcome the
physical gap **plus** this spurious asymmetry. This quantifies why the z-Habiro
brane tower is non-production (#2467 "blocked, not enabled").

> Cross-model caveat: the per-generator-tower → binding wiring is the z-Habiro
> hypothesis verdicted non-production in #2467, so `E₀·Δtower` is an
> order-of-magnitude comparison, not a binding prediction. The **sign** of
> `Δtower` is scale-free and rigorous.

## Deliverable 3 — the LP-dual pair-knot composite

**Part 1 — canonical H_3 operator-selection LP-dual is DEGENERATE.**
Routing the proton through `lp_dual_solver.solve_operator_selection_lp` on the
canonical NF basis `{γ,σ₀,σ₁,L₊,L₋,e⁻}` (the
[`aK_via_lp_dual_hecke_basis.py`](../../computations/aK_via_lp_dual_hecke_basis.py)
pattern) gives `y0* = 0`, only the identity `γ` active, `duality_gap = 3.5e-15`.
A free nucleon has `W_free = W_atom` — there is no binding constraint to select
against. The pair-knot is intrinsically a 2-nucleon (H_6) object, where the full
720-element basis LP is intractable and the block-diagonal LP is also degenerate
(audit §7d). **A direct operator-selection LP-dual does not isolate the
pair-knot invariant at any tractable level.**

**Part 2 — the pair-knot composite is the right *object*.**
Canonical bond strengths `L = log(tr_M^full/tr_M^atom)` (from `tr_m_atom_zn`,
50 dps): `pp = 0.6945`, `pn = 0.9292`, `nn = 1.2370`. The proton pair-knot
composite carries `Q_pp = +1` (`def:coulomb-charge`); its Coulomb reduction
`tanh(ln q₀)·B_pp = 0.238 MeV` (with `tanh(ln q₀) = (q₀²−1)/(q₀²+1)` verified
*exact* at 50 dps, residual `1.7e-52`). The composite **replaces** the two
individual near-pole proton generators (whose per-generator over-count *is* D1's
spurious `E₀·Δtower = 1.165 MeV`, wrong sign) with one pp bond whose
charge-asymmetric part is the **correct-sign** derived Coulomb (31%).

## Verdict

The pair-knot composite is the **right object** — it removes the spurious
per-generator over-count and carries the correct `def:coulomb-charge` sign — but
its **magnitude closure is the known-open "categorical two-like-charge
brane-pairing invariant"** (`charge_coulomb_tn3he_derived.py:22`), at 31% with
the residual 3.2× forbidden-to-fit (CAL-4). A **direct LP-dual cannot supply it**
(degenerate at H_3, intractable/degenerate at H_6); the invariant must come from
the analytical `C_λ·S_λ` factorisation (`prop:mass-coefficient-shadow-price` /
audit §7d) or a genuinely new categorical construction. **This work scopes the
open item; it does not close it.**

## Open item (precise statement for the next agent)

> Define the **categorical two-like-charge brane-pairing invariant** that, on the
> proton pair-knot composite, supplies the EM-linking / nuclear-geometry
> normalisation beyond the 31% structural `tanh(ln q₀)·B_pp`. Constraints it
> must respect: (a) `mirror_isospin_coulomb_split` — it is **not** a constant
> rescaling κ of the categorical split; (b) it is **not** a direct
> operator-selection LP-dual (degenerate/intractable, this PR); (c) closing the
> magnitude by fitting to 0.764 MeV is a **forbidden CAL-4 fit** (Δ_λ gate). The
> tractable canonical route is the analytical `C_λ·S_λ` factorisation at H_6.

## Side finding — stale witness (found AND refreshed in this PR)

[`charge-coulomb-tn3he-derived.witness.json`](../../computations/charge-coulomb-tn3he-derived.witness.json)
was found **stale**: it stored `ratio = tanh(ln q₀) = 0.10396371005`, differing
from the current value `0.10396372147` by `~1.1e-8` (`dHe` drift `~2.6e-8`) — it
**predated the 2026-05-28 proton-anchor q₀ re-pin**. It has been **refreshed in
this PR** (re-ran the producer at current q₀: `ratio = 0.10396372146`,
`dHe = 0.237670225`, `B_pp = 2.286 MeV`, 31.1% / 3.21× unchanged); D3 now cites
it with drift `2.1e-17`. The probe retains a generic `cc_witness_stale` guard
that re-fires on any future re-pin drift.

## Discipline checklist

- No fit, no fourth calibration; the only derived inputs are `q₀` (substrate),
  `m_e` (CAL-1), and the already-derived `def:coulomb-charge` structure.
- LP-dual fields (`y0_star`/`y_star`/`active_set`/`primal`/`dual`/`gap`) emitted
  per AGENTS.md §LP/SDP duals.
- Probes are `_probe`-suffixed and `auditOnly`; no production mass table is
  rewired (the z-Habiro brane tower is non-production per #2467).
- Builds on the existing Coulomb cluster (does not duplicate it); the new content
  is the *quantification* (D1) and the *LP-degeneracy + object/magnitude split*
  (D3).
