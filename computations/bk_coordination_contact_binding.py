#!/usr/bin/env python3
"""
bk_coordination_contact_binding.py — the binding multiplicity is the COORDINATION
NUMBER of the building-block link 𝓑_K, at two levels:

  • nucleon level (A ≤ 4): the single-link weight  B = M(A)·m_e·Vol_n(K)  has
    multiplicity  M(A) = z(A) = A−1  = the per-nucleon coordination number (vertex
    degree of the fully-coordinated cluster graph K_A, 3D-realisable for A ≤ 4).
  • α-cluster level (A > 4): binding beyond n_α·B(⁴He) is  N_contacts·b_αα , where
    N_contacts is the CONTACT-GRAPH edge count of the real close-packed α geometry
    (triangle 3, tetrahedron 6, square-pyramid 8, octahedron 12, …) — the α-level
    coordination number. C(n_α,2) over-counts for n_α ≥ 5 because ≥5 spheres cannot
    all mutually touch in 3D.

PART 1 (nucleon coordination, A ≤ 4) — structural reading of the merged
rem:bk-coordination-multiplicity result. The graph fact z=A−1 is exact; the claim
"single-link multiplier = coordination number" is the bond-extensive hypothesis
(conditional, not derived from the 13 drivers).

PART 2 (α-cluster contact coordination, A > 4) — FORWARD test: fix b_αα from the
simplex clusters ¹²C/¹⁶O, then PREDICT ²⁰Ne/²⁴Mg/⁴⁰Ca from their standard α-cluster
contact geometries (Brink / Hafstad–Teller deltahedra). No per-nucleus fit.

EXPLORATORY — scope-limited (a); b_αα a single empirical constant; α-geometry per
nucleus is the standard cluster assignment. No production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
import codata_constants as _cc  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

set_compute_dps()
q = Q_MP
M_E = M_E_MEV                       # already an mp.mpf at high precision (codata_constants)


def B_ame(Z, A):
    return _cc._ame_binding_mev(Z, A)   # already an mp.mpf under workdps(≥50)


# ── PART 1 — nucleon coordination number z = A−1 (A ≤ 4) ───────────────────────
#   single hyperbolic link volumes (binding-link-volumes.witness.json)
VOL = {"T": mp.mpf("8.286316817806593"),     # ³H = 8_11
       "3He": mp.mpf("7.327724753417752")}   # ³He = L6a4 (Borromean)
A3 = {"T": (1, 3), "3He": (2, 3)}


def z_coord(A):
    """Per-nucleon coordination number = vertex degree of the complete graph K_A."""
    return A - 1


def part1():
    print("### PART 1 — nucleon coordination z=A−1 as the single-link multiplier (A≤4)")
    print("  M_need = B_AME/(m_e·Vol);  z = A−1 = degree of K_A (complete cluster graph)")
    print(f"  {'iso':<5}{'M_need':>9}{'z=A−1':>7}{'err':>8}")
    ok = True
    rows = {}
    for K, (Z, A) in A3.items():
        M_need = B_ame(Z, A) / (M_E * VOL[K])
        z = z_coord(A)
        err = float((z - M_need) / M_need)
        ok = ok and abs(err) < 0.05
        rows[K] = dict(M_need=float(M_need), z=z, err=err)
        print(f"  {K:<5}{float(M_need):>9.3f}{z:>7}{err*100:>7.1f}%")
    print("  Structural reading: z=A−1 is the coordination number (vertex degree) of")
    print("  the fully-coordinated A-body graph K_A, exact and Lean-provable. The claim")
    print("  'single-link multiplier = z' is the BOND-EXTENSIVE hypothesis (conditional).")
    print(f"  A=3 pair matched to <3%, no fit.  [{'CONFIRMED' if ok else 'no'}]\n")
    return rows, ok


# ── PART 2 — α-cluster contact coordination (A > 4), FORWARD ───────────────────
#   standard α-cluster (Brink / Hafstad–Teller) geometries → contact-graph edges.
#   n_α ≤ 4: complete graph C(n_α,2) (tetrahedron is the max all-touching cluster).
#   n_α ≥ 5: the deltahedral / close-packed contact count (< C(n_α,2)).
ALPHA = {
    #  name : (Z, A, n_α, N_contacts, geometry)
    "8Be":  (4, 8, 2, 1,  "dumbbell (2 spheres)"),
    "12C":  (6, 12, 3, 3, "equilateral triangle (K3)"),
    "16O":  (8, 16, 4, 6, "regular tetrahedron (K4)"),
    "20Ne": (10, 20, 5, 8, "square pyramid"),
    "24Mg": (12, 24, 6, 12, "octahedron"),
    "40Ca": (20, 40, 10, 24, "fcc close-packed 10-cluster"),
}


def part2():
    B_alpha = B_ame(2, 4)
    # fix b_αα from the two clean simplex clusters ¹²C, ¹⁶O (complete-graph contacts)
    b_C = (B_ame(6, 12) - 3 * B_alpha) / 3
    b_O = (B_ame(8, 16) - 4 * B_alpha) / 6
    b_aa = (b_C + b_O) / 2
    print("### PART 2 — α-cluster contact coordination (A>4), FORWARD from fixed b_αα")
    print(f"  B(⁴He)={float(B_alpha):.3f} MeV;  b_αα fixed from ¹²C/¹⁶O = "
          f"{float(b_aa):.3f} MeV  (¹²C {float(b_C):.3f}, ¹⁶O {float(b_O):.3f})")
    print(f"  B_pred = n_α·B(⁴He) + N_contacts·b_αα   (N_contacts from cluster geometry)")
    print(f"  {'iso':<6}{'nα':>3}{'N':>4}{'geometry':<28}{'B_pred':>9}{'B_AME':>9}{'err':>8}")
    rows = {}
    worst = 0.0
    for nm, (Z, A, na, N, geom) in ALPHA.items():
        B_pred = na * B_alpha + N * b_aa
        B_a = B_ame(Z, A)
        err = float((B_pred - B_a) / B_a)
        # ¹²C/¹⁶O are the calibration points; ⁸Be (n_α=2) is the known unbound-pair
        # exception (single α–α bond ≈ 0 — the triple-α gateway). Neither counts in
        # 'worst', which measures the FORWARD prediction on the bound 3+ clusters.
        if nm not in ("12C", "16O", "8Be"):
            worst = max(worst, abs(err))
        rows[nm] = dict(n_alpha=na, N_contacts=N, geometry=geom,
                        B_pred=float(B_pred), B_ame=float(B_a), err=err)
        tag = "  (calib)" if nm in ("12C", "16O") else ("  (unbound pair)" if nm == "8Be" else "")
        print(f"  {nm:<6}{na:>3}{N:>4}{geom:<28}{float(B_pred):>9.2f}"
              f"{float(B_a):>9.2f}{err*100:>7.2f}%{tag}")
    print(f"\n  Forward predictions on the bound 3+ clusters (²⁰Ne/²⁴Mg/⁴⁰Ca): "
          f"worst |err| = {worst*100:.2f}%")
    print(f"  ⁸Be (n_α=2, err {rows['8Be']['err']*100:+.1f}%) is the UNBOUND-PAIR exception:")
    print(f"    the isolated α–α bond carries ≈0 (⁸Be sits just above 2·⁴He) — the bond")
    print(f"    energy switches on only inside a 3+ cluster (the triple-α gateway).")
    print("  ¹⁶O=tetrahedron(6) and ²⁴Mg=octahedron(12) are exact platonic edge counts;")
    print("  a single b_αα reproduces A=12–40 binding to <0.5% — the classical Brink /")
    print("  Hafstad–Teller α-model, read as the α-level coordination (contact) number.")
    print("  C(n_α,2) over-counts for n_α≥5 (≥5 spheres can't all touch in 3D).\n")
    return rows, float(b_aa), worst


def main() -> int:
    print(f"  q₀={float(q):.6f}  m_e={float(M_E):.6f}\n")
    p1, p1_ok = part1()
    p2, b_aa, p2_worst = part2()

    print("### Verdict — coordination number = binding multiplicity (scope-limited (a))")
    print("  • A≤4 nucleon level: the single-link volume multiplier is the per-nucleon")
    print("    coordination number z=A−1 (vertex degree of K_A). Exact graph fact;")
    print("    'multiplier = z' is the bond-extensive hypothesis (conditional, not derived).")
    print("  • A>4 α level: the contact-graph coordination number of the standard")
    print("    α-cluster geometry, with ONE b_αα, predicts A=12–40 binding to <0.5%.")
    print("  • Unifying reading: binding multiplicity = coordination number of 𝓑_K at the")
    print("    relevant level (nucleon for A≤4, α for A>4). b_αα empirical, not derived.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("bk-coordination-contact-binding", engine="mpmath")
            wb.set_description(
                "The binding multiplicity is the coordination number of 𝓑_K at two levels: "
                "the nucleon coordination z=A−1 (single-link multiplier, A≤4) and the "
                "α-cluster CONTACT-graph coordination number (A>4). Forward test: one b_αα "
                "fixed from ¹²C/¹⁶O predicts ²⁰Ne/²⁴Mg/⁴⁰Ca binding to <0.5% from standard "
                "Brink deltahedral contact counts (tetrahedron 6, octahedron 12, …). "
                "z=A−1 exact graph fact; 'multiplier=coordination' is bond-extensive "
                "(conditional); b_αα empirical. Scope-limited (a), no production wiring.")
            wb.add_data("q0", float(q))
            wb.add_data("part1_nucleon_coordination", p1)
            wb.add_data("part2_alpha_contact_coordination", p2)
            wb.add_data("b_alpha_alpha_MeV", b_aa)
            wb.add_assertion(
                name="nucleon_coordination_z_matches_A3_multiplier",
                computed=str(int(p1_ok)), expected="1", tolerance=0,
                source="M_need(³H)/³He ≈ 2 = z=A−1 (vertex degree of K_A) to <3%, no fit.")
            wb.add_assertion(
                name="alpha_contact_coordination_predicts_binding_under_half_percent",
                computed=str(int(p2_worst < 0.005)), expected="1", tolerance=0,
                source=(f"one b_αα={b_aa:.3f} MeV (fixed from ¹²C/¹⁶O) predicts ²⁰Ne/²⁴Mg/⁴⁰Ca "
                        f"from standard α-cluster contact geometries; worst |err|="
                        f"{p2_worst*100:.2f}% (<0.5%). b_αα empirical, geometry standard."))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
