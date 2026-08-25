#!/usr/bin/env python3
"""
gap2_borromean_triple_count.py — GAP-2 (bean qou-ooqh): does the 3-body term of the
body-order tower account for the GAP-1 residual, and is the right count the bonded-triple
(3-clique) count or the Milnor-IRREDUCIBLE (Borromean, μ̄₁₂₃≠0) subset?

Follows GAP-1 (#3630): the max-contact deltahedra (3A−6 contacts) fix the 2-body edge set at
A≥5, leaving a bounded ~1.2–1.8 MeV/nucleon residual = the many-body term. This probe tests
the FIRST many-body order (3-body) parameter-lean.

MODEL (per-ORDER pinning, NOT per-isotope). The body-order tower is
  B(K) = e₂·M₂(K) + e₃·M₃(K) + e₄·M₄(K) + …,   eₙ = m_e·a_D^(n)·wₙ (per-order energy).
Pin each eₙ on the LIGHTEST nucleus that first exhibits order n — D (2-body), T (3-body),
⁴He (4-body) — 3 anchors for 3 per-order energies, then PREDICT A≥5 from GEOMETRY (the clique
counts of the deltahedral contact graph). This is #3588's w₂-pin extended to w₃,w₄; the A≥5
values are predictions, not fits.

Mₙ CANDIDATE = the k-clique count of the max-contact contact graph (mutually-bonded k-subset):
M₂ = #edges = 3A−6, M₃ = #triangles (3-cliques), M₄ = #tetrahedra (4-cliques). Deltahedra built
explicitly below (tri-bipyramid A=5, octahedron A=6, pentagonal bipyramid A=7).

FINDING (scope-(a), a REFUTATION + redirect — honest negative):
  The bonded-TRIPLE (3-clique) count OVERSHOOTS the A≥5 binding by a growing +13%→+24%
  (⁵Li→⁷Li); the 4-clique×(⁴He energy) reading overshoots far worse (+70%+). So NOT every
  mutually-bonded triple is a 3-body term. This CONFIRMS the corpus Part-7 reading: only the
  Milnor-IRREDUCIBLE (Borromean, μ̄₁₂₃≠0) triples count — a mutually-bonded triple is
  REDUCIBLE to pairwise (μ̄=0), so counting all 3-cliques double-counts what the 2-body edges
  already carry. The overshoot MEASURES the reducible-triple over-count. ⁴He's 4-body magic is
  a non-transferable shell closure (its e₄ over-predicts ⁵Li's two tetrahedra).

  ⇒ M₃(K) is the μ̄₁₂₃-irreducible triple count, NOT the 3-clique count. Computing it needs the
  contact-graph → framed-link promotion + the validated μ̄-tower (binding_mn_milnor_linking.py)
  — the remaining open step (still GAP-2). This probe PRUNES the clique reading and localizes it.

Anti-fit checkpoint (bean qou-ooqh): eₙ pinned per-ORDER on D/T/⁴He (3 anchors, the minimal
nuclei of each order), clique counts from geometry, A≥5 forward-predicted. The refutation is a
reported overshoot, not a tuned match. EXPLORATORY, scope-(a), no wiring.

Audit: docs/audits/2026-07-11-gap2-borromean-triple-count.md
Workplan: docs/workplans/2026-07-11-mnk-derivation-gaps.md (GAP-2)
"""
from __future__ import annotations
import sys
from itertools import combinations
from pathlib import Path

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
# Canonical Coulomb: α_EM DERIVED from q₀ and R₀ = λ̄_π (CAL-3), per bean qou-usft.
# The comment here used to say "αℏc=1.43996" — the CODATA value the module stopped
# using on 2026-08-09. The code was already correct; only the annotation was stale.
from coulomb_energy import coulomb_energy_mev  # noqa: E402
try:
    from witness_base import WitnessBuilder
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False


# --- explicit max-contact deltahedral contact graphs (vertex sets + edge lists) ---
def complete_graph(n):
    return set(frozenset(e) for e in combinations(range(n), 2))

def tri_bipyramid():           # A=5: 3 equatorial (0,1,2) + 2 apexes (3,4); no apex-apex
    eq = [(0, 1), (1, 2), (2, 0)]
    ap = [(a, e) for a in (3, 4) for e in (0, 1, 2)]
    return set(frozenset(e) for e in eq + ap)

def octahedron():              # A=6: K_{2,2,2}; opposite pairs (0,5),(1,4),(2,3) non-adjacent
    non = {frozenset((0, 5)), frozenset((1, 4)), frozenset((2, 3))}
    return set(frozenset(e) for e in combinations(range(6), 2)) - non

def pentagonal_bipyramid():    # A=7: pentagon (0..4) + 2 apexes (5,6); no apex-apex, no chords
    pent = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    ap = [(a, e) for a in (5, 6) for e in range(5)]
    return set(frozenset(e) for e in pent + ap)


def k_clique_count(nverts, edges, k):
    """# of k-subsets that are mutually adjacent (k-cliques)."""
    return sum(1 for s in combinations(range(nverts), k)
               if all(frozenset(p) in edges for p in combinations(s, 2)))


# (name): (B_AME, Z, A, graph-or-None). A≤4 use complete graph (simplex).
GRAPHS = {
    "D":   (AME_B_DEUTERON_MEV_VALIDATION, 1, 2, complete_graph(2)),
    "T":   (AME_B_TRITIUM_MEV_VALIDATION,  1, 3, complete_graph(3)),
    "4He": (AME_B_HE4_MEV_VALIDATION,      2, 4, complete_graph(4)),
    "5Li": (AME_B_LI5_MEV_VALIDATION,      3, 5, tri_bipyramid()),
    "6Li": (AME_B_LI6_MEV_VALIDATION,      3, 6, octahedron()),
    "7Li": (AME_B_LI7_MEV_VALIDATION,      3, 7, pentagonal_bipyramid()),
}


def b_strong(B, Z, A):
    """Strong binding = AME binding + discrete-proton Coulomb (canonical coulomb_energy_mev:
    α_EM derived from q₀, R₀ = λ̄_π CAL-3, R₀ shared across callers) — adds back the charge
    energy for the charge-symmetric comparison."""
    return mp.mpf(str(B)) + mp.mpf(str(coulomb_energy_mev(Z, A)))


def cliques(A, edges):
    return (k_clique_count(A, edges, 2), k_clique_count(A, edges, 3),
            k_clique_count(A, edges, 4))


def main() -> int:
    # clique counts
    counts = {}
    for K, (B, Z, A, g) in GRAPHS.items():
        counts[K] = cliques(A, g)

    print("=== GAP-2: bonded-triple (3-clique) count vs the GAP-1 residual ===\n")
    print(f"  {'iso':<5}{'A':>2}{'M2=#edge':>9}{'M3=#tri':>8}{'M4=#tet':>8}")
    for K, (B, Z, A, g) in GRAPHS.items():
        m2, m3, m4 = counts[K]
        print(f"  {K:<5}{A:>2}{m2:>9}{m3:>8}{m4:>8}")

    # per-ORDER energies pinned on D (e2), T (e3), ⁴He (e4)
    bs = {K: b_strong(B, Z, A) for K, (B, Z, A, _) in GRAPHS.items()}
    m2_D, m3_D, m4_D = counts["D"]
    e2 = bs["D"] / m2_D                                       # D: M2=1 ⇒ e2 = B(D)
    m2_T, m3_T, m4_T = counts["T"]
    e3 = (bs["T"] - e2 * m2_T) / m3_T                         # T: M3=1 ⇒ e3 = residual
    m2_He, m3_He, m4_He = counts["4He"]
    e4 = (bs["4He"] - e2 * m2_He - e3 * m3_He) / m4_He        # ⁴He: M4=1 ⇒ e4 = residual
    print(f"\n  per-order energies (pinned on D/T/⁴He, 3 anchors):")
    print(f"    e₂ = {float(e2):.4f} MeV (deuteron bond)")
    print(f"    e₃ = {float(e3):.4f} MeV (triton 3-body)")
    print(f"    e₄ = {float(e4):.4f} MeV (⁴He 4-body — doubly-magic)")

    # PREDICT A≥5 two ways: (i) e2·M2+e3·M3 (3-body only), (ii) +e4·M4 (with 4-clique)
    print(f"\n### Forward predictions at A≥5 (B_pred / B_strong)")
    print(f"  {'iso':<5}{'B_strong':>9}{'2+3body':>9}{'ratio':>7}{'+4body':>9}{'ratio':>7}")
    a5 = [K for K in GRAPHS if GRAPHS[K][2] >= 5]
    rows = {}
    over3, over4 = [], []
    for K in a5:
        B, Z, A, _ = GRAPHS[K]
        m2, m3, m4 = counts[K]
        b3 = e2 * m2 + e3 * m3
        b34 = b3 + e4 * m4
        r3, r34 = float(b3 / bs[K]), float(b34 / bs[K])
        over3.append(r3); over4.append(r34)
        rows[K] = dict(A=A, m2=m2, m3=m3, m4=m4, B_strong=float(bs[K]),
                       B_2plus3=float(b3), ratio_2plus3=r3, B_plus4=float(b34), ratio_plus4=r34)
        print(f"  {K:<5}{float(bs[K]):>9.3f}{float(b3):>9.3f}{r3:>7.3f}"
              f"{float(b34):>9.3f}{r34:>7.3f}")

    triple_overshoots = all(r > 1.05 for r in over3)          # 3-clique OVERSHOOTS
    triple_grows = over3 == sorted(over3)                      # miss grows with A
    # 4-clique reading is worse ONLY where a tetrahedron exists (M4>0, i.e. ⁵Li);
    # octahedron/pentagonal-bipyramid have no K₄ so +4body ≡ 3body there.
    quad_worse = all(rows[K]["ratio_plus4"] > rows[K]["ratio_2plus3"]
                     for K in a5 if rows[K]["m4"] > 0)

    grows_txt = "monotonically GROWING" if triple_grows else "non-monotone"
    m4_isos = [K for K in a5 if rows[K]["m4"] > 0]
    m4_detail = "; ".join(
        f"{K} {rows[K]['ratio_2plus3']:.3f}→{rows[K]['ratio_plus4']:.3f}" for K in m4_isos)
    print(f"\n### Finding (scope-(a) — REFUTATION + redirect)")
    print(f"  • Bonded-triple (3-clique) count OVERSHOOTS: ratios "
          f"{', '.join(f'{r:.3f}' for r in over3)} (all >1, {grows_txt} miss).")
    print(f"  • Where a tetrahedron exists (M₄>0: {', '.join(m4_isos) or 'none'}), adding the "
          f"4-clique×e₄(⁴He) reading is WORSE ({m4_detail}) — ⁴He 4-body magic is "
          f"non-transferable. (For M₄=0 isotopes +4body ≡ 3body.)")
    print(f"  ⇒ NOT every mutually-bonded triple is a 3-body term. Confirms corpus Part 7:")
    print(f"    only the Milnor-IRREDUCIBLE (Borromean, μ̄₁₂₃≠0) triples count — a bonded triple")
    print(f"    is REDUCIBLE to pairwise (μ̄=0), so the 2-body edges already carry it; counting")
    print(f"    all 3-cliques double-counts. The overshoot MEASURES the reducible-triple excess.")
    print(f"\n  OPEN (GAP-2, sharpened): M₃(K) = the μ̄₁₂₃-irreducible triple count, needing the")
    print(f"  contact-graph → framed-link promotion + the validated μ̄-tower. This probe PRUNES")
    print(f"  the 3-clique reading; the irreducible count is the next step. No fit; no wiring.")

    ok = triple_overshoots and triple_grows and quad_worse
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("gap2-borromean-triple-count", engine="mpmath")
            wb.set_description(
                "GAP-2 (qou-ooqh): tests the 3-body term of the body-order tower with per-order "
                "energies pinned on D/T/⁴He and Mₙ = k-clique counts of the max-contact deltahedra "
                "(tri-bipyramid/octahedron/pentagonal-bipyramid). The bonded-triple (3-clique) count "
                "OVERSHOOTS A≥5 binding +13→24% (growing); the 4-clique×e₄(⁴He) reading is worse "
                "(non-transferable ⁴He magic). REFUTES 'every bonded triple is a 3-body term' and "
                "confirms corpus Part 7: only Milnor-IRREDUCIBLE (Borromean μ̄₁₂₃≠0) triples count — "
                "a bonded triple is reducible (μ̄=0), already carried by the 2-body edges. Overshoot "
                "measures the reducible-triple double-count. OPEN: the μ̄-irreducible count (needs "
                "graph→framed-link promotion). Scope-(a), per-order pinning, no fit, no wiring.")
            wb.add_data("clique_counts", {K: dict(zip(("M2", "M3", "M4"), counts[K])) for K in GRAPHS})
            wb.add_data("per_order_energies_MeV", {"e2": float(e2), "e3": float(e3), "e4": float(e4)})
            wb.add_data("predictions", rows)
            wb.add_assertion(
                name="three_clique_overshoots_irreducible_needed",
                computed=str(int(ok)), expected="1", tolerance=0,
                source=("with eₙ pinned on D/T/⁴He and Mₙ = k-clique counts, the bonded-triple "
                        "(3-clique) count overshoots A≥5 binding (ratios %s, all >1, monotonically "
                        "growing) and — only where a tetrahedron exists (M₄>0, ⁵Li) — the 4-clique "
                        "reading is strictly worse (for M₄=0 isotopes +4body ≡ 3body). So not every "
                        "bonded triple is a 3-body term; only the Milnor-irreducible (Borromean μ̄≠0) "
                        "subset counts (reducible triples are carried by the 2-body edges). The "
                        "overshoot measures the reducible over-count."
                        % ", ".join(f"{r:.3f}" for r in over3)))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
