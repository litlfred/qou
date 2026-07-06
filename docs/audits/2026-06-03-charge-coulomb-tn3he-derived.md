# Derived Coulomb gets the T-vs-³He split to 31% (charge, not color)

**Status:** FINDING (reproducible, no fit). The ³H−³He binding split
(0.764 MeV ≈ 9.5%) is the Coulomb repulsion of ³He's two protons. This
records how far the **already-derived** categorical Coulomb structure gets
toward it, and names the remaining gate.

Probe: [`charge_coulomb_tn3he_derived.py`](../../computations/charge_coulomb_tn3he_derived.py)
(witness `charge-coulomb-tn3he-derived.witness.json`).

## Derived inputs (zero fit)

From `def:coulomb-charge` ([`coulomb-charge.lean`](../../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.lean)):

`E_cross = ½(n₊+n₋)(q+q⁻¹)` (strong) `+ Q·(q−q⁻¹)` (Coulomb), with
`Q_pp = (n₊−n₋)/2 = +1` for two protons (repulsive) and the Coulomb/strong
ratio `tanh(ln q₀) ≈ 0.104` (q₀-only). The α_EM Habiro element
`[2]_q·(1−h²α)` is independently derived (4 ppm).

## Result

| quantity | value |
|---|---|
| Coulomb/strong ratio `tanh(ln q₀)` | 0.10396 |
| pp strong bond `B_pp` (per-block, H₆) | 2.2861 MeV |
| derived pp-Coulomb ³He reduction `tanh(ln q₀)·B_pp` | **0.2377 MeV** |
| AME T−³He split | 0.7638 MeV |
| **fraction covered** | **31.1%** (vs color's 4.5%) |
| remaining factor | **3.21×** |

## Verdict

- **Charge is the right mechanism** (right sign, right order) — the derived
  Coulomb covers 31% with no fit, ~7× better than the color (flavor)
  weighting (4.5%). This confirms the color-vs-charge finding
  ([`2026-06-03-color-vs-charge-crossing-tn3he.md`](2026-06-03-color-vs-charge-crossing-tn3he.md)).
- **The open gate is the remaining 3.2×**: the per-interface **EM-linking /
  nuclear-geometry normalization** — a categorical *two-like-charge
  brane-pairing invariant* (analogous to the Frobenius pairing but for like
  charges) that is **not yet defined** in the framework. The global knot
  charge `Q(H)` exists (`u1_hypercharge_assignment.py`, writhe-based,
  derived); the **per-pair** EM linking does not.
- **Discipline:** a concrete close beyond the derived 31% would require that
  EM-linking invariant. Tuning a pp-Coulomb constant to hit 0.764 MeV would
  be a **CAL-4 fit** — out of bounds. So task 1 (charge crossing) is gated on
  the open EM-linking derivation, the same pattern as the other Wall-A items
  (the magnitude needs a categorical object the structure does not yet
  supply).

## Next

The productive direction is **deriving the two-like-charge EM-linking
invariant** (then the pp-Coulomb magnitude is `Q_pp · EM-linking · α_EM-norm`
evaluated at q₀, and 0.764 MeV becomes a post-hoc check, not the input).
Until then the pp-Coulomb crossing stays exploratory. Coordinate with the
α_EM cluster (#1521 Habiro element, #1523 categorical α_EM, #1549 Schwinger).
