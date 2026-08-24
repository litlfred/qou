#!/usr/bin/env python3
"""
gap2b_irreducible_demand.py — GAP-2 continuation (bean qou-ooqh → qou-3lsb/GAP-4 bridge):
what many-body count does the data DEMAND, and does it track any nucleon-level deltahedral
invariant? Answer: NO — the residual is roughly CONSTANT across the Li isotopes while the
nucleon 3-clique count grows +43%, so the many-body term is α-CLUSTER-structural (GAP-4),
not a nucleon-level μ̄ count.

Context. GAP-1 (#3630) fixed the 2-body max-contact backbone (undershoots, ratio ~0.7–0.8);
GAP-2 (#3633) showed the nucleon 3-clique count OVERSHOOTS ⇒ M₃ is the Milnor-irreducible
subset. The natural next step is the graph→framed-link promotion to COUNT the irreducible
(Borromean μ̄₁₂₃≠0) triples. But before choosing a link (an arbitrary choice = a hidden fit),
this DIAGNOSTIC asks what the data demands and whether a nucleon-level count can supply it.

Method (diagnostic, NOT a fit — inverts the residual to read off the demanded count, à la
#3545 Part 6's "#bonds implied"; nothing wired). Per-order energies pinned on D (e₂) and T
(e₃, M₃=1). For each nucleus:
  residual(K)   = B_strong(K) − e₂·M₂(K),   M₂ = max-contact 3A−6 (GAP-1)
  demanded_M₃(K) = residual(K) / e₃
and compare demanded_M₃ + residual to the nucleon-level deltahedral invariants (3-clique
count, #triangular faces).

FINDING (scope-(a)): across ⁵Li/⁶Li/⁷Li the many-body residual is roughly CONSTANT
(~8.2 MeV, CV ≈ 6%) while the nucleon 3-clique count GROWS +43% (7→8→10) — they DECOUPLE.
The demanded_M₃ (~4.3–4.9) matches NO nucleon deltahedral invariant. So a universal-e₃ ×
nucleon-level count cannot supply the residual. The near-constant residual is the signature of
the α-CLUSTER structure: ⁵Li=α+p, ⁶Li=α+d, ⁷Li=α+t share a common α-core-plus-valence
many-body binding (~constant), NOT a monolithic nucleon deltahedron whose 3-body count grows.
⇒ the many-body term is at the α-cluster level (GAP-4 / #3551 Brink deltahedra of α's), and the
nucleon-level μ̄-irreducible count is the WRONG level. This PRUNES the nucleon-link-promotion
route and redirects GAP-2's remainder into GAP-4.

Anti-fit checkpoint: e₂,e₃ pinned on D,T (2 anchors); residual + demanded count are diagnostic
read-outs, not tuned matches; the conclusion is a decoupling (structural), not a closure.
Nothing wired. EXPLORATORY, scope-(a).

Audit: docs/audits/2026-07-11-gap2b-irreducible-demand.md
Workplan: docs/workplans/2026-07-11-mnk-derivation-gaps.md (GAP-2 → GAP-4 bridge)
"""
from __future__ import annotations
import sys
from math import comb
from pathlib import Path
from statistics import mean, pstdev

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps
set_compute_dps()
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_LI5_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_LI7_MEV_VALIDATION,
)
from coulomb_energy import coulomb_energy_mev  # noqa: E402
try:
    from witness_base import WitnessBuilder
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

# (B_AME, Z, A, cluster-label). 3-clique counts from GAP-2's explicit deltahedra.
ISO = {
    "D":   (AME_B_DEUTERON_MEV_VALIDATION, 1, 2, "—"),
    "T":   (AME_B_TRITIUM_MEV_VALIDATION,  1, 3, "—"),
    "4He": (AME_B_HE4_MEV_VALIDATION,      2, 4, "α (core)"),
    "5Li": (AME_B_LI5_MEV_VALIDATION,      3, 5, "α + p"),
    "6Li": (AME_B_LI6_MEV_VALIDATION,      3, 6, "α + d"),
    "7Li": (AME_B_LI7_MEV_VALIDATION,      3, 7, "α + t"),
}
THREE_CLIQUES = {"D": 0, "T": 1, "4He": 4, "5Li": 7, "6Li": 8, "7Li": 10}


def max_contacts(A):
    return 1 if A == 2 else 3 * A - 6

def b_strong(B, Z, A):
    return mp.mpf(str(B)) + mp.mpf(str(coulomb_energy_mev(Z, A)))


def main() -> int:
    bs = {K: b_strong(B, Z, A) for K, (B, Z, A, _) in ISO.items()}
    e2 = bs["D"] / max_contacts(2)                       # D: M₂=1
    e3 = bs["T"] - e2 * max_contacts(3)                  # T: M₃=1 ⇒ e₃ = residual

    print("=== GAP-2b: does the demanded many-body count track a nucleon deltahedral invariant? ===\n")
    print(f"  e₂ = {float(e2):.4f} MeV (D bond)   e₃ = {float(e3):.4f} MeV (T 3-body)\n")
    print(f"  {'iso':<5}{'cluster':<9}{'A':>2}{'B_strong':>9}{'2body':>8}{'residual':>10}"
          f"{'dem_M3':>8}{'3-clique':>9}{'#faces':>8}")
    rows = {}
    for K, (B, Z, A, cl) in ISO.items():
        b = bs[K]
        two = e2 * max_contacts(A)
        resid = float(b - two)
        dem = float((b - two) / e3)
        faces = 0 if A < 4 else 2 * A - 4          # closed-deltahedron triangular faces
        rows[K] = dict(A=A, cluster=cl, B_strong=float(b), two_body=float(two),
                       residual=resid, demanded_M3=dem,
                       three_clique=THREE_CLIQUES[K], faces=faces)
        print(f"  {K:<5}{cl:<9}{A:>2}{float(b):>9.3f}{float(two):>8.3f}{resid:>10.3f}"
              f"{dem:>8.2f}{THREE_CLIQUES[K]:>9}{faces:>8}")

    li = ["5Li", "6Li", "7Li"]
    resid_li = [rows[K]["residual"] for K in li]
    clique_li = [rows[K]["three_clique"] for K in li]
    resid_cv = pstdev(resid_li) / mean(resid_li)
    clique_growth = clique_li[-1] / clique_li[0] - 1.0

    print(f"\n### Finding (scope-(a) — DECOUPLING ⇒ α-cluster level, not nucleon μ̄ count)")
    print(f"  • Li many-body residual: {', '.join(f'{r:.2f}' for r in resid_li)} MeV — "
          f"mean {mean(resid_li):.2f}, CV {100*resid_cv:.1f}% (roughly CONSTANT).")
    print(f"  • Li nucleon 3-clique count: {clique_li} — grows +{100*clique_growth:.0f}%.")
    print(f"  • demanded_M₃ ~{min(rows[k]['demanded_M3'] for k in li):.1f}–"
          f"{max(rows[k]['demanded_M3'] for k in li):.1f} matches NO nucleon invariant "
          f"(3-clique {clique_li}, faces {[rows[k]['faces'] for k in li]}).")
    print(f"  ⇒ the residual DECOUPLES from any nucleon-level deltahedral count: a universal-e₃ ×")
    print(f"    nucleon count cannot supply it. The near-constant residual is the α-CLUSTER")
    print(f"    signature — ⁵Li=α+p, ⁶Li=α+d, ⁷Li=α+t share a ~constant α-core many-body binding.")
    print(f"  ⇒ the many-body term lives at the α-cluster level (GAP-4 / #3551 Brink deltahedra),")
    print(f"    NOT the nucleon-level μ̄-irreducible count. Prunes the nucleon-link-promotion route.")
    print(f"\n  OPEN (redirected to GAP-4): the α-cluster contact structure (α+valence for Li). The")
    print(f"  nucleon-level graph→link promotion is the WRONG level; GAP-4's Brink-deltahedra of α's")
    print(f"  is where the constant many-body residual is built. No fit; no wiring.")

    decoupled = (resid_cv < 0.10) and (clique_growth > 0.30)
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("gap2b-irreducible-demand", engine="mpmath")
            wb.set_description(
                "GAP-2b diagnostic (qou-ooqh→GAP-4 bridge): with e₂,e₃ pinned on D,T and the "
                "max-contact 2-body backbone (GAP-1), the many-body residual across ⁵Li/⁶Li/⁷Li is "
                "roughly CONSTANT (~8.2 MeV, CV~6%) while the nucleon 3-clique count grows +43% — "
                "they DECOUPLE, and the demanded_M₃ (~4.3–4.9) matches no nucleon deltahedral "
                "invariant. So a universal-e₃ × nucleon count cannot supply the residual; the "
                "near-constant residual is the α-cluster signature (⁵Li=α+p, ⁶Li=α+d, ⁷Li=α+t share "
                "a ~constant α-core many-body binding). The many-body term is at the α-cluster level "
                "(GAP-4 / #3551 Brink deltahedra), NOT the nucleon-level μ̄-irreducible count — this "
                "prunes the nucleon-link-promotion route. Diagnostic (inverts residual, à la Part 6), "
                "not a fit; scope-(a); no wiring.")
            wb.add_data("per_order_energies_MeV", {"e2": float(e2), "e3": float(e3)})
            wb.add_data("per_isotope", rows)
            wb.add_data("li_residual_MeV", resid_li)
            wb.add_data("li_residual_cv", resid_cv)
            wb.add_data("li_three_clique_growth", clique_growth)
            wb.add_assertion(
                name="manybody_residual_decouples_from_nucleon_count",
                computed=str(int(decoupled)), expected="1", tolerance=0,
                source=("the Li many-body residual is roughly constant (%s MeV, CV %.1f%% < 10%%) "
                        "while the nucleon 3-clique count grows +%.0f%% (>30%%) — decoupled ⇒ the "
                        "many-body term is not a nucleon-level count but the α-cluster structure "
                        "(GAP-4), so the nucleon graph→link promotion is the wrong level."
                        % (", ".join(f"{r:.2f}" for r in resid_li), 100 * resid_cv, 100 * clique_growth)))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
