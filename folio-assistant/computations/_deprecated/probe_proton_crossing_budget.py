#!/usr/bin/env python3
"""Probe — proton crossing-budget alternatives to close the 1.84% m_p residual.

Per the user's error budget:
  ¹H source #3 (verify 11-crossing budget) is the only remaining
  candidate after #1 (Φ_q truncation), #2 (f64 precision), #4
  (pentagon-truncation), and #5 ((2A+1) ud-count) were ruled out
  by the Habiro-exact 50-dps probe and by direct counting.

The current proton budget (per hecke_core.nucleon_gen_chains(['u','u','d'])
+ 2 gluons per nucleon_gen_chains) totals 11 crossings:

  gen 0: 3·σ (B_3 confinement)
       + 1·σ (uu quark pair)
       + 1·½(σ + σ⁻¹) (ud quark pair, position (0,2))
       + 2·σ (gluon self-coupling)
  gen 1: 3·σ⁻¹ (B_3 confinement)
       + 1·½(σ + σ⁻¹) (ud quark pair, position (1,2))

  Total: 11 crossings, 2 ud-halves.

This probe varies the gluon count (currently 2) and the B_3 power
(currently 3 per gen) to find which budget gives m_p/m_e ≈ 1836.15
(CODATA), instead of the current 1869.85 (+1.84%).

NO Vol_hyp.  NO knot identification.  NO census search.

Output: probe-proton-crossing-budget.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV, M_P_MEV
from witness_base import WitnessBuilder

mp.mp.dps = 50

# Compute q_0 at 50 dps
VOL_FIGURE_EIGHT = mp.mpf("2.029883212819307")
MASS_RATIO_MU_E  = mp.mpf("206.7682830")
HBAR_Q_SQ        = VOL_FIGURE_EIGHT / MASS_RATIO_MU_E
HBAR_Q           = mp.sqrt(HBAR_Q_SQ)
Q0               = mp.mpf(1) / (mp.mpf(1) - HBAR_Q)
QI0              = mp.mpf(1) / Q0
HA               = Q0 - QI0
Z_MARK           = mp.mpf(1) / (mp.sqrt(Q0) + mp.sqrt(QI0))


def qint(k):
    if k == 0:
        return mp.mpf(0)
    return (Q0**k - QI0**k) / HA


# Q-deformed Wedderburn weights for n=3
QDIM_SYM = mp.mpf(1)
QDIM_STD = qint(2)
QDIM_ALT = mp.mpf(1)
NF3      = qint(1) * qint(2) * qint(3)
W_SYM = QDIM_SYM**2 / NF3
W_STD = QDIM_STD**2 / NF3
W_ALT = QDIM_ALT**2 / NF3
W_TOT = W_SYM + W_STD + W_ALT
W_SYM /= W_TOT
W_STD /= W_TOT
W_ALT /= W_TOT


def Phi_q_mpfr(z, max_k=2000):
    if abs(z) >= Q0:
        return mp.inf
    product = mp.mpf(1)
    qi_pow = QI0
    eps = mp.mpf(10) ** (-(mp.mp.dps + 5))
    for _ in range(max_k):
        term = qi_pow * z
        factor = mp.mpf(1) - term
        if mp.fabs(factor) < eps:
            return mp.inf
        product /= factor
        if mp.fabs(term) < eps:
            break
        qi_pow *= QI0
    return product


def additive_wedderburn_volumes(crossings_per_gen, n_strands):
    vols = []
    for gen in range(n_strands - 1):
        a, b = mp.mpf(0), mp.mpf(1)
        sp_val = mp.mpf(1)
        ap_val = mp.mpf(1)
        for c, d in crossings_per_gen.get(gen, []):
            c_mp = mp.mpf(c)
            d_mp = mp.mpf(d)
            a, b = (a * c_mp * HA + a * d_mp + b * c_mp,
                    a * c_mp + b * d_mp)
            sp_val *= c_mp * Q0 + d_mp
            ap_val *= -c_mp * QI0 + d_mp
        Vs = Z_MARK * a + b
        Vf = W_SYM * sp_val + W_STD * Vs + W_ALT * ap_val
        vols.append({"std": Vs, "sym": sp_val, "alt": ap_val, "full": Vf})
    return vols


def mass_from_tower(vols):
    n = len(vols)
    desc = mp.mpf(1)
    for v in vols:
        desc *= v["full"]
    desc = mp.fabs(desc)
    single = mp.mpf(0)
    for v in vols:
        single += Phi_q_mpfr(mp.fabs(v["full"]))
    cross = mp.mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            cross += Z_MARK**2 * Phi_q_mpfr(
                mp.fabs(vols[i]["full"] * vols[j]["full"])
            )
    return desc, single, cross, desc + single + cross


# Reference electron at trefoil σ_1³ (3 crossings)
def electron_total():
    crossings = {0: [(1, 0)] * 3}
    vols = additive_wedderburn_volumes(crossings, 2)
    _, _, _, total = mass_from_tower(vols)
    return total


def proton_total(n_gluon, n_b3):
    """Proton with n_gluon σ-self-coupling crossings on gen 0,
    and B_3 power n_b3 (default 3 = standard)."""
    h_neg = -float(HA)
    h_neg_half = h_neg / 2
    crossings = {
        # gen 0: B_3 + uu + ud + gluons
        0: ([(1, 0)] * n_b3            # B_3 confinement
            + [(1, 0)]                  # uu quark pair
            + [(1, h_neg_half)]         # u-d pair (position 0,2)
            + [(1, 0)] * n_gluon),      # gluon self-coupling
        # gen 1: B_3 inverse + ud
        1: [(1, h_neg)] * n_b3 + [(1, h_neg_half)],
    }
    vols = additive_wedderburn_volumes(crossings, 3)
    _, _, _, total = mass_from_tower(vols)
    return total, vols


def main():
    print("=" * 78)
    print("Probe — proton crossing-budget alternatives at 50 dps")
    print("=" * 78)
    print(f"  q_0 = {mp.nstr(Q0, 30)}")
    print(f"  m_e = {M_E_MEV} MeV; m_p = {M_P_MEV} MeV")
    print(f"  CODATA m_p/m_e = {M_P_MEV/M_E_MEV:.6f}")
    print(f"  Current (n_b3=3, n_gluon=2): m_p_pred/m_e = 1869.85 (+1.84% off)")
    print()
    e_tot = electron_total()
    print(f"  e_total = {mp.nstr(e_tot, 30)}  (reference)")
    print()

    target = mp.mpf(M_P_MEV) / mp.mpf(M_E_MEV)

    rows = []
    print(f"  {'n_b3':>4} {'n_glu':>5} {'V̂_0':>10} {'V̂_1':>10} "
          f"{'m_p_pred':>12} {'m_p/m_e':>10} {'err%':>9}  verdict")
    print("  " + "-" * 80)
    for n_b3 in (2, 3, 4):
        for n_gluon in range(0, 5):
            try:
                p_tot, vols = proton_total(n_gluon, n_b3)
                ratio = p_tot / e_tot
                err_pct = float((ratio - target) / target * 100)
                v0 = float(vols[0]["full"])
                v1 = float(vols[1]["full"])
                marker = "  <==" if abs(err_pct) < 0.1 else ""
                print(f"  {n_b3:>4} {n_gluon:>5} {v0:>10.4f} {v1:>10.4f} "
                      f"{float(p_tot):>12.0f} {float(ratio):>10.2f} "
                      f"{err_pct:>+9.4f}{marker}")
                rows.append({
                    "n_b3": n_b3,
                    "n_gluon": n_gluon,
                    "n_total_crossings": n_b3 * 2 + 1 + 1 + n_gluon + 1,  # B_3 + uu + ud(0) + ud(1) + gluons
                    "V_0": float(v0),
                    "V_1": float(v1),
                    "m_p_pred_in_me_units_50dps": mp.nstr(p_tot, 30),
                    "m_p_over_m_e": float(ratio),
                    "err_pct_vs_codata": err_pct,
                    "matches_within_0.1pct": abs(err_pct) < 0.1,
                })
            except Exception as exc:
                rows.append({
                    "n_b3": n_b3, "n_gluon": n_gluon,
                    "error": str(exc),
                })

    print()
    matches = [r for r in rows if r.get("matches_within_0.1pct")]
    if matches:
        print(f"  ✓ MATCHES (|err%| < 0.1%): {len(matches)}")
        for m in matches:
            print(f"      n_b3={m['n_b3']}, n_gluon={m['n_gluon']}: "
                  f"m_p/m_e = {m['m_p_over_m_e']:.4f} (err {m['err_pct_vs_codata']:+.4f}%)")
    else:
        print("  ✗ NO budget within 0.1% of CODATA found in scanned range.")
        print("  → 1.84% residual is NOT explained by simple crossing-count")
        print("    permutations.  Structural source is elsewhere.")

    # Witness
    w = (
        WitnessBuilder("probe-proton-crossing-budget", engine="python+mpmath")
        .set_description(
            "Probe of proton crossing-budget alternatives at 50 dps. "
            "Current budget (B_3 power 3, 2 gluons, 11 total crossings) "
            "gives m_p/m_e = 1869.85 (+1.84% off CODATA). Scans n_b3 ∈ "
            "{2, 3, 4} and n_gluon ∈ {0..4} to identify any (n_b3, "
            "n_gluon) combination that yields CODATA m_p/m_e = 1836.15 "
            "exactly (within 0.1%). NO Vol_hyp, NO knot identification, "
            "NO census search — pure mpmath at 50 dps."
        )
        .set_content_block("rem:photon-channel-wedderburn-chain")
        .add_parameter("q_0_mpf50", mp.nstr(Q0, 50))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("m_p_AME_MeV", M_P_MEV)
        .add_parameter("target_m_p_over_m_e_codata", float(target))
        .add_parameter("mpmath_dps", mp.mp.dps)
        .add_data("scan_results", rows)
        .add_data("matches_count", len(matches))
        .add_caveat(
            "If no match is found, the 1.84% residual is structurally "
            "encoded outside the simple crossing-count parameter space. "
            "Possible structural sources: (a) crossing TYPE distribution "
            "(σ vs σ⁻¹ vs ud-half), (b) Φ_q tower truncation at order 2 "
            "(but ¹H has only 2 gens, so no order-3+), (c) Wedderburn "
            "weight choice (q-deformed vs Plancherel), (d) calibration "
            "of m_e (currently CODATA leptonic input)."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
