# Trefoil AJ annihilation (assembled) + Masbaum literature cross-check (PR #3279)

**Date:** 2026-07-04
**Beans:** `6q9g` + `rz8b` (trefoil, done), `6zub` (trefoil eval cores,
follow-up), `xcyc` (Masbaum cross-check, done).
**Lineage:** the 4₁ program (PR #3263: division-free certificate telescope,
`StrongAJFigureEight` sorry-free) — this tranche extends the machinery to the
second corpus knot (trefoil) and cross-checks both against the literature.
**Borromean stage 1** was split to a follow-up PR (R-matrix inverse blocker at
color ≥ 3); see that PR / bean `moqg`.

## Trefoil: annihilation assembled, sorry narrowed to two evaluation cores

[`AJTrefoilAnnihilation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/AJTrefoilAnnihilation.lean)
(lean-direct, exactly 2 cited-sorry warnings). No qZeilberger certificate is
needed at order 1: the Rosso–Jones tower extends by one term per color, so
with `P(n) = Σ_{j≤n} (−1)^j w^{6j(j+1)} [2j+1]_{w²}` the tower is
`J(n+1) = (−1)^n w^{−6n(n+2)} P(n)/[n+1]_v` (`coloredJonesTrefoil_eq_P_form`,
proved — all quadratic exponents cancel in the operator's ratios), and the
annihilation reduces to two rational identities [C1]/[C2] in `(w, Y = (w²)^N)`
— pre-verified exactly in
[`aj_trefoil_telescope_assembly_check.py`](../../computations/aj_trefoil_telescope_assembly_check.py)
and proved in the generic case.

**The finding worth reading first:** `coloredJonesTrefoil` divides by
`qInt (w²) N`, which vanishes exactly at `x = (w⁴)^N = 1`, where the Lean
value is the division-by-zero junk `0`, not the analytic value. The merged
class field quantifies over ALL `w ≠ 0` — and it remains *true* there only
because of a three-way conspiracy: the operator's own coefficients vanish at
the junk slots (`a₀ ∝ (x−1)`, `a₁ ∝ (xq−1)`), and the surviving term then
requires the **root-of-unity evaluation** `J = 1` at the neighboring color
(RJ-sum periodicity; verified numerically to 40 dps for both slots). The case
split (`w⁴ = 1` collapse / generic / two degenerate slots) is fully proved;
the two evaluation lemmas (`trefoil_eval_at_root_prev`/`_next`) are the
remaining cited cores — strictly smaller than the superseded broad general-`N`
sorry (removed from `AJTrefoil.lean`; instance moved, per the 4₁ pattern).
The induction through the singular slot breaks (`[N]_v = 0` kills the generic
step at exactly the color the chain needs), so the cores need a genuine sum
evaluation — queued as bean `6zub`.

Contrast with 4₁: there the division-free telescope avoided ALL denominators,
so the proof needed no case split and no root-of-unity lemmas. The trefoil's
tower *definition* carries the `1/[N]_v` normalization, so the degeneracy is
intrinsic to the statement, not the proof method.

## Masbaum cross-check + provenance correction (bean xcyc)

The owner uploaded `library/0306345v1/0306345v1.pdf` (arXiv egress proxy-blocked).
**Reading it corrected a mis-attribution**: G. Masbaum, *Skein-theoretical
derivation of some formulas of Habiro* (AGT 3 (2003) 537–556, math/0306345) is
about **twist knots** K_p (his Fig. 3; K₁ = left-handed trefoil, K₋₁ =
figure-eight), and carries **no Borromean formula** — the Borromean rings are
not twist knots. The earlier "Masbaum's Borromean c_k" framing came from my
own memory plus a hallucinated web-search summary, not the source. The actual
simple-links reference is **Habiro [H1]** (*On the colored Jones polynomial of
some simple links*, RIMS Kokyuroku 1172), which this paper cites and which is
not available here. Recorded per the critical-distance / "before declaring"
disciplines.

**What the paper DID validate — the two corpus knots (exact, 40 dps,
[`aj_masbaum_crosscheck.py`](../../computations/aj_masbaum_crosscheck.py),
witness `aj-masbaum-crosscheck`):**

- **Figure-eight**: the Lean 4₁ Habiro double-Pochhammer tower
  (`HabiroNewtonLadder.coloredJones41`, PR #3263) equals Masbaum's
  `J'_{K₋₁}(N)` exactly — his `f_{K₋₁,n} = 1` is the all-ones Newton ladder
  the Lean proves. Independent literature confirmation of the merged 4₁ work.
- **Trefoil**: the Lean Rosso–Jones tower (`AJTrefoil.coloredJonesTrefoil`,
  this tranche) equals Masbaum's left-handed `J'_{K₁}(N)` exactly, under
  `q_Masbaum = 1/q_corpus` — the two conventions agree up to the bar
  involution q↔1/q (the standard Kauffman-A-vs-A⁻¹ split). The trefoil tower
  is now **literature-anchored** (Masbaum's left-handed K₁), upgrading the
  earlier "self-anchored against V(3₁)" status.

## Status

- Trefoil: assembled; `6zub` queued (the two evaluation cores).
- Masbaum cross-check: done, both corpus knots validated.
- Borromean stage 1: split to a follow-up PR (R-matrix inverse blocker at
  color ≥ 3); bean `moqg` / `1iqq` track it there.
