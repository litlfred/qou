# Deuteron W3 wall — adjudicated: the canonical braid-closure rule makes Vol = 0, and 6₂ is non-canonical

**Date:** 2026-08-21 · **Arc:** bk-crossing-coordination, open item 4 (deuteron knot identity) · **PR:** (arc follow-up)
**Resolves:** the W3 wall of [`2026-08-16-two-row-cap-proved-and-deltalambda-magnitude.md`](2026-08-16-two-row-cap-proved-and-deltalambda-magnitude.md) §W3 — "you cannot derive a knot invariant while the knot is undetermined."
**Discipline:** adjudication from corpus evidence + the corpus's own canonical rule; no new compute; scope-(a).

## The dispute

Three candidates for the canonical deuteron knot/link:

| candidate | Vol | tier | key evidence |
|---|--:|---|---|
| (a) braid-closure trefoil `T(2,3)` | **0** (flat) | principled-derivation | `deuteron-octahedral-gluing.witness.json` (SnapPy: Vol=0, shapes {½,2}); `BlochVolumeLegFlatVanishing.lean` `deuteron_volume_leg_eq_zero` (proved) |
| (b) linear-chain Hopf `L2a1` | **0** (Seifert) | principled (coordination frame) | `recursive-atom-knot-atlas-registry.md` (`D = [𝔭,𝔫]_{L_H}`); `volume-binding-four-point.witness.json:87` |
| (c) census `6₂` | 4.40083 | **manual-historical-volume-match** | `knot_volumes.py::_vol_6_2`; registry `:73/:135`; `B_pred = m_e·Vol(6₂) = 2.249` (+1.09%) |

## The tie-breaker — the corpus's own canonical rule

`recursive-atom-knot-atlas-registry.md` (methodology table) defines the top tier as
**`principled-derivation` = "the closure of an explicit σ-braid word in `H_{n₀}(q₀)`, `Vol_hyp`
computed via `hp_volume_of_link_closure`"** (e.g. electron `σ₁³ → 3₁`, proton `(σ₁σ₂⁻¹)³ → B₃`);
`r5_full_canonical_knot_solver.py` (`prop:atom-knot-mass-derivation`) selects the canonical knot as
the closure of the T_w word chosen by the joint PSD-feasibility + binding SDP. **The canonical rule
is braid-closure of the T_w word, not volume-match.**

Under that rule both principled readings of the deuteron are flat:

- **Δ_λ / octahedral frame:** `σ₁³` closes to the trefoil `T(2,3)` → **Vol = 0** (committed SnapPy;
  Lean `deuteron_volume_leg_eq_zero` proves `∑ D(zᵢ) = D(½)+D(2) = 0` from Bloch–Wigner conjugation
  antisymmetry, **triangulation-independent** — no finer triangulation or heavier flat nucleus can
  make it nonzero, and a flattening shifts only `Im`, not `D`).
- **Coordination frame:** `𝔭 ⊕ 𝔫 ⊕ L_H` binding link → Hopf `L2a1` → **Vol = 0** (Seifert-fibred).

## Verdict — Vol(deuteron) = 0 is canonical; 6₂ is a non-canonical volume-match

- **6₂ has no principled-derivation basis.** Every 6₂ assignment traces to
  `manual-historical-volume-match`, which the registry itself flags as *"well-established but the
  GB-NF derivation in `H_{n₀}(q₀)` has **not been computed yet**."* Worse: it is **SDP-infeasible**
  (`r5-full-canonical-knot-solver.witness.json`: deuteron `6_2` `psd_feasible: false`, `alpha_gap
  0.89`; the SDP's own deuteron winner is a *different* word), and it is **internally contradicted**
  — the same registry block that closes to 6₂ (`:135`) also assigns the deuteron binding link as the
  Hopf link `L_H` (Vol 0, `:61/:131`).
- **So the corpus-consistent A=2 anchor is Vol = 0.** This aligns with the independent result on
  this branch (`qou-brng`): binding is **not** a hyperbolic-volume defect — so the deuteron's
  ≈2.2 MeV binding is not the volume of its own closure.

## Consequence — binding magnitude, if Bloch, lives in the CS/torsion leg

With Vol = 0 provably fixed, the surviving half of the Bloch route is the **`i·CS` / torsion leg**,
which audit §W4 notes is "determined only mod π²." The corpus's live foothold is **bean `qou-fl4t`**
(restore the Dimofte–Garoufalidis flattening monomial + global ½ in `whitehead_c_sigma_torsion.py`
so `|τ|` becomes triangulation-invariant). Caveat (§W4, stands): pinning CS to a definite MeV value
by choosing the π² branch to match AME would be "the forbidden fit in hyperbolic-geometry costume."
So item 4 resolves **which knot** (braid-closure ⇒ Vol 0); it does **not** hand over a derived
deuteron binding — that remains open on the CS/torsion leg.

## Recommendation (owner call — not executed here)

The atlas registry still **ships** 6₂ with a +1.09% binding match and no block has been retired.
Adjudication says 6₂ is non-canonical (volume-match tier, SDP-infeasible, self-contradicted).
Recommend flagging/retiring the 6₂ deuteron assignment to the canonical Vol=0 closure — but this
edits a live per-isotope prediction, so it is left as an explicit owner decision rather than done
unilaterally. Bean `qou-985x` (W3, todo) is the tracker; `qou-fl4t` (in-progress) owns the CS leg.
