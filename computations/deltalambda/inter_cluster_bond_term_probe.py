#!/usr/bin/env python3
"""inter_cluster_bond_term_probe.py — derive-or-refute the INTER-CLUSTER BOND
TERM (the object three independent 2026-07-13 results converged on).

CONTEXT (R5-a)
--------------
Alpha-cluster additivity is a zero-fit LOWER BOUND on binding
(docs/audits/2026-07-13-atom-knot-rule-a5plus-constraints.md; witness
alpha-cluster-volume-additivity.witness.json, committed, allPassed): the
deficit B_AME - B_add IS the missing inter-cluster bond term, and the
implied per-bond volumes are NON-CONSTANT (2.9 -> 12.8, guarded).  The
n = 4 tower term cannot be one link volume (census gap;
2026-07-13-he4-vol4-prediction-test.md), and the theta_lambda carrier is an
intensive mean (2026-07-13-carrier-saturation-crossover-mechanism.md) —
extensivity lives in the volume tower.  This probe asks, formalize-first
(compute-author.md §3.3): WHAT IS THE STRUCTURE of the deficit?

DESIGN (all inputs committed; NOTHING recomputed, NOTHING tuned)
----------------------------------------------------------------
[1] Load the committed additivity witness; cross-check its deficits
    against the vendored AME2020 (consistency assertion only).
[2] PRE-REGISTERED q-rotational hypotheses (zero freedom; every factor
    derived per binding_qhamiltonian_rotational_scale.py: mu0 =
    m_e/(3(q-q^-1)/2) ~ 1.6295 MeV, hbar_q = 1 - 1/q, J_q^2(j) =
    [j]_q [j+1]_q; the corpus deuteron channel is mu0*hbar_q*J_q^2(3)
    = 2.02 MeV = B_D - 9%):
      H1 (cluster-spin):  j_bond = measured ground-state spin sum of the
          two clusters (alpha 0+, d 1+, t 1/2+, n 1/2+; ENSDF/NNDC
          ground-state spins — every bond has an alpha end, so j_bond =
          spin of the light cluster; alpha.alpha -> j = 0).
      H2 (deuteron-channel): every inter-cluster bond carries the
          deuteron's own derived rotor E_D = mu0*hbar_q*J_q^2(3)
          ("the deuteron IS the alpha.d bond's model"); j = 3 = n/2 with
          n = 6 strands, the corpus convention, not tuned.
      H3 (strand-count): j = n_light/2 = 3*A_light/2 — the corpus j = n/2
          convention applied to the light cluster of the bond.
    Bond lists come from the witness decompositions (linear chain of
    clusters, k-1 bonds); the 9Be alternative reading (two alpha.n bonds)
    is reported alongside.
[3] CAL-3 bond-quantum family comparison (m_pi-scale units, from the
    continuum-EM work 2026-07-13-mirror-split-continuum-em-derivation-
    attempt.md): alpha_EM*m_pi, m_pi*hbar_q^2, (3/5)*alpha*m_pi/A^(1/3).
    Ratios reported; single-point near-matches quarantined as numerology
    hazards.
[4] STRUCTURAL CHARACTERIZATION of the deficit data:
      (a) contact nucleons: not extractable from the committed data (the
          composite reading has disjoint clusters); covered by (b).
      (b) per-bond deficit vs light-cluster size A_light (one-bond family);
      (c) per-bond deficit vs the light cluster's own binding (B_D, B_t);
      (d) pair-graph (complete-graph C(k,2)) recounting: pure-alpha
          per-pair flatness (12C vs 16O) and the 8Be k = 2 switch-off.

EXPECTED SHAPE (registered before the run)
------------------------------------------
H1 is the structurally motivated form but its magnitudes (<= 0.33 MeV for
j <= 1) sit far below the 0.8-6.5 MeV/bond deficits, and it predicts
exactly 0 for every alpha.alpha bond — where the deficits are largest.  If
it misses, the failure shape (intensive bound? wrong j-dependence?) is the
deliverable.

Run:  python3 -u computations/deltalambda/inter_cluster_bond_term_probe.py \\
        2>&1 | tee /tmp/inter_cluster_bond.log

EXPLORATORY — audit-only witness; no production wiring; no fitted constant.
Audit: docs/audits/2026-07-13-inter-cluster-bond-term-derive-or-refute.md
"""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, M_PI_PM_MEV_VALIDATION, _ame_binding_mev  # noqa: E402
from experimental_constants import ALPHA_EM_INV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

# ── derived scales (all corpus-derived; binding_qhamiltonian_rotational_scale.py)
Q = Q_MP
M_E = mp.mpf(str(M_E_MEV))
M_PI = mp.mpf(str(M_PI_PM_MEV_VALIDATION))
H = Q - 1 / Q                       # q - q^-1
HBAR_Q = 1 - 1 / Q                  # q-Planck constant
MU0 = M_E / (3 * H / 2)             # per-crossing mass scale (DERIVED)
E_UNIT = MU0 * HBAR_Q               # ~0.161 MeV


def qint(x) -> mp.mpf:
    """[x]_q = (q^x - q^-x)/(q - q^-1) (symmetric quantum number)."""
    x = mp.mpf(x)
    return (Q**x - Q**(-x)) / H


def Jq2(j) -> mp.mpf:
    """q-angular momentum Casimir J_q^2(j) = [j]_q [j+1]_q (corpus convention,
    q-angular-momentum / binding_qhamiltonian_rotational_scale.py)."""
    return qint(j) * qint(mp.mpf(j) + 1)


def E_rot(j) -> mp.mpf:
    """Derived q-rotational bond energy mu0 * hbar_q * J_q^2(j) in MeV."""
    return E_UNIT * Jq2(j)


# ── PRE-REGISTERED cluster data (measured ground-state spins, ENSDF/NNDC) ────
# spins: 4He 0+, 2H 1+, 3H 1/2+, n 1/2+  (standard evaluated data)
SPIN = {"4He": mp.mpf(0), "d": mp.mpf(1), "t": mp.mpf("0.5"), "n": mp.mpf("0.5")}
A_OF = {"4He": 4, "d": 2, "t": 3, "n": 1}
ISO_A = {"6Li": 6, "7Li": 7, "8Be": 8, "9Be": 9, "11B": 11, "12C": 12,
         "14N": 14, "16O": 16, "19F": 19}
ISO_ZA = {"6Li": (3, 6), "7Li": (3, 7), "8Be": (4, 8), "9Be": (4, 9),
          "11B": (5, 11), "12C": (6, 12), "14N": (7, 14), "16O": (8, 16),
          "19F": (9, 19)}


def chain_bonds(pieces: list[str]) -> list[tuple[str, str]]:
    """Linear-chain bonds between consecutive pieces (k-1 bonds; witness
    convention n_intercluster_bonds = len(pieces) - 1)."""
    return [(pieces[i], pieces[i + 1]) for i in range(len(pieces) - 1)]


def pair_bonds(pieces: list[str]) -> list[tuple[str, str]]:
    """Complete-graph C(k,2) pairs (alternative geometric counting —
    triangle for 3 alphas, tetrahedron for 4)."""
    return [(pieces[i], pieces[j])
            for i in range(len(pieces)) for j in range(i + 1, len(pieces))]


def bond_j_spin(x: str, y: str) -> mp.mpf:
    """H1: bond spin = stretched coupling of measured cluster spins
    (every bond here has an alpha end -> j = spin of the other cluster)."""
    return SPIN[x] + SPIN[y]


def bond_j_strand(x: str, y: str) -> mp.mpf:
    """H3: j = n/2 with n = 3*A_light strands of the LIGHTER cluster
    (the corpus deuteron convention j = n/2 applied to the light piece)."""
    a_light = min(A_OF[x], A_OF[y])
    return mp.mpf(3 * a_light) / 2


def main() -> int:
    print("=" * 76)
    print(" INTER-CLUSTER BOND TERM — derive-or-refute (R5-a; zero fit,")
    print(" all j pre-registered from measured cluster spins / corpus strand rule)")
    print("=" * 76)

    # ── [1] load committed witness; consistency cross-check ─────────────────
    wsrc = _HERE / "alpha-cluster-volume-additivity.witness.json"
    W = json.load(open(wsrc))
    ADD = W["alpha_cluster_additivity_AME_level"]
    max_dev = 0.0
    for iso, row in ADD.items():
        Z, A = ISO_ZA[iso]
        b_ame = _ame_binding_mev(Z, A)
        b_add = sum(
            (_ame_binding_mev(*{"4He": (2, 4), "d": (1, 2), "t": (1, 3)}[p])
             if p != "n" else mp.mpf(0))
            for p in row["pieces"])
        dev = abs(float(b_ame - b_add) - row["deficit_MeV"])
        max_dev = max(max_dev, dev)
    witness_consistent = max_dev < 1e-9
    print(f"\n[1] committed witness {wsrc.name}: deficits reproduce from the "
          f"vendored AME2020\n    to {max_dev:.2e} MeV (consistency only; no recompute of the test).")

    print(f"\n    derived scales: mu0 = {mp.nstr(MU0, 6)} MeV, hbar_q = "
          f"{mp.nstr(HBAR_Q, 6)}, mu0*hbar_q = {mp.nstr(E_UNIT, 6)} MeV")
    print(f"    E_rot(j): j=1/2 -> {mp.nstr(E_rot('0.5'), 5)}   j=1 -> "
          f"{mp.nstr(E_rot(1), 5)}   j=3 (deuteron ch.) -> {mp.nstr(E_rot(3), 6)} MeV")

    # ── [2] pre-registered q-rotational tests ────────────────────────────────
    print("\n[2] PRE-REGISTERED q-rotational tests  deficit(X.Y) =? sum_bonds "
          "mu0*hbar_q*J_q^2(j)")
    print(f"    {'iso':5s} {'bonds (chain)':22s} {'deficit':>8s} "
          f"{'H1 spin':>8s} {'r1':>6s} {'H2 j=3':>8s} {'r2':>6s} "
          f"{'H3 strand':>9s} {'r3':>6s}")
    E_D_CH = E_rot(3)                       # deuteron-channel quantum, 2.0204
    rows = {}
    for iso, row in ADD.items():
        pieces, deficit = row["pieces"], mp.mpf(str(row["deficit_MeV"]))
        bonds = chain_bonds(pieces)
        h1 = sum(E_rot(bond_j_spin(x, y)) for x, y in bonds)
        h2 = E_D_CH * len(bonds)
        h3 = sum(E_rot(bond_j_strand(x, y)) for x, y in bonds)
        blab = "+".join(f"{x}-{y}" for x, y in bonds)

        def ratio(p):
            return float(p / deficit) if abs(float(deficit)) > 1e-12 else float("inf")
        rows[iso] = {
            "pieces": pieces, "bonds_chain": [list(b) for b in bonds],
            "deficit_MeV": float(deficit),
            "H1_spin_pred_MeV": float(h1), "H1_pred_over_deficit": ratio(h1),
            "H2_deuteron_channel_pred_MeV": float(h2), "H2_pred_over_deficit": ratio(h2),
            "H3_strand_pred_MeV": float(h3), "H3_pred_over_deficit": ratio(h3),
        }
        print(f"    {iso:5s} {blab:22s} {float(deficit):>+8.3f} "
              f"{float(h1):>8.3f} {ratio(h1):>6.2f} {float(h2):>8.3f} "
              f"{ratio(h2):>6.2f} {float(h3):>9.3f} {ratio(h3):>6.2f}")
    # 9Be alternative reading: two alpha.n bonds (task-flagged)
    alt_9be = {
        "bonds": [["4He", "n"], ["4He", "n"]],
        "H1_pred_MeV": float(2 * E_rot(SPIN["n"])),
        "H3_pred_MeV": float(2 * E_rot(mp.mpf(3) / 2)),
        "deficit_MeV": rows["9Be"]["deficit_MeV"],
    }
    print(f"    9Be alt (2x alpha-n):        H1 = {alt_9be['H1_pred_MeV']:.3f}  "
          f"H3 = {alt_9be['H3_pred_MeV']:.3f}  vs deficit {alt_9be['deficit_MeV']:+.3f}")

    # H1 verdict data
    one_bond = ["6Li", "7Li"]
    h1_undershoot = [rows[i]["deficit_MeV"] / rows[i]["H1_spin_pred_MeV"] for i in one_bond]
    pure_alpha = ["12C", "16O"]
    h1_zero_on_big = all(rows[i]["H1_spin_pred_MeV"] == 0.0 and rows[i]["deficit_MeV"] > 7
                         for i in pure_alpha)
    h1_bound = float(E_rot(1))              # max H1 bond value at j <= 1
    print(f"\n    H1 (cluster-spin): undershoots 6Li x{h1_undershoot[0]:.1f}, "
          f"7Li x{h1_undershoot[1]:.1f}; predicts EXACTLY 0 for the pure-alpha")
    print(f"    composites carrying the LARGEST deficits (12C +7.27, 16O +14.44 MeV);")
    print(f"    intensive bound: max per-bond value (j<=1) = {h1_bound:.3f} MeV. NEGATIVE.")

    # H2 verdict data
    h2_r6, h2_r7 = rows["6Li"]["H2_pred_over_deficit"], rows["7Li"]["H2_pred_over_deficit"]
    h2_8be_viol = abs(rows["8Be"]["H2_deuteron_channel_pred_MeV"]
                      - rows["8Be"]["deficit_MeV"])
    h2_ratios_pos = [rows[i]["H2_pred_over_deficit"] for i in rows if i != "8Be"]
    h2_spread = max(h2_ratios_pos) / min(h2_ratios_pos)
    print(f"    H2 (deuteron channel, j=3 fixed): right ORDER at one-bond "
          f"(6Li {h2_r6:+.2f}x, 7Li {h2_r7:+.2f}x)\n    but 8Be violated by "
          f"{h2_8be_viol:.2f} MeV (predicts 2.02 vs -0.09) and pred/deficit "
          f"spans x{h2_spread:.1f}. NEGATIVE as universal quantum.")

    # H3 verdict data: overshoot monotone in A_light for the bond family
    fam = [("alpha-n", 1, alt_9be["H3_pred_MeV"] / 2, rows["9Be"]["deficit_MeV"] / 2),
           ("alpha-d", 2, float(E_rot(3)), rows["6Li"]["deficit_MeV"]),
           ("alpha-t", 3, float(E_rot(mp.mpf(9) / 2)), rows["7Li"]["deficit_MeV"]),
           ("alpha-alpha(k>=3)", 4, float(E_rot(6)),
            (rows["12C"]["deficit_MeV"] / 3 + rows["16O"]["deficit_MeV"] / 6) / 2)]
    h3_ratios = [p / d for _, _, p, d in fam]
    h3_monotone = all(a < b for a, b in zip(h3_ratios, h3_ratios[1:]))
    print("    H3 (strand-count j = 3*A_light/2): pred/deficit "
          + ", ".join(f"{n} {r:.2f}" for (n, _, _, _), r in zip(fam, h3_ratios)))
    print("    -> overshoot grows monotonically with A_light (q-exponential J_q^2")
    print("       vs the data's ~linear growth). NEGATIVE; failure shape recorded.")

    # ── [3] CAL-3 bond-quantum family (m_pi-scale) ───────────────────────────
    alpha_codata = 1 / mp.mpf(str(ALPHA_EM_INV))
    q9, q10 = qint(9), qint(10)
    alpha_der = 1 / (Q * q9 * q10)          # prop:alpha-em-categorical-trace-ratio
    fam3 = {
        "alpha_der*m_pi": alpha_der * M_PI,
        "alpha_codata*m_pi": alpha_codata * M_PI,
        "m_pi*hbar_q^2": M_PI * HBAR_Q**2,
    }
    print("\n[3] CAL-3 bond-quantum family vs per-chain-bond deficits (ratios; GUARDED):")
    onebond_deficits = {"9Be": rows["9Be"]["deficit_MeV"] / 2,
                        "6Li": rows["6Li"]["deficit_MeV"],
                        "7Li": rows["7Li"]["deficit_MeV"]}
    cal3 = {}
    for name, qv in fam3.items():
        rats = {iso: float(d / qv) for iso, d in onebond_deficits.items()}
        cal3[name] = {"quantum_MeV": float(qv), "deficit_over_quantum": rats}
        print(f"    {name:18s} = {float(qv):6.4f} MeV : " +
              "  ".join(f"{i} {r:5.2f}" for i, r in rats.items()))
    # A^{-1/3} continuum form at the composite A
    cont = {iso: float(mp.mpf(3) / 5 * alpha_der * M_PI / mp.cbrt(ISO_A[iso]))
            for iso in onebond_deficits}
    cal3["continuum_(3/5)a*m_pi/A^(1/3)"] = {
        "pred_MeV": cont,
        "deficit_over_pred": {i: onebond_deficits[i] / cont[i] for i in cont}}
    no_universal_cal3 = all(
        max(abs(r - 1) for r in v["deficit_over_quantum"].values()) > 0.30
        for v in cal3.values() if "deficit_over_quantum" in v)
    print("    -> no single family member matches the one-bond deficits at")
    print("       multiplier 1 (all deviate > 30% somewhere). m_pi*hbar_q^2 vs the")
    print("       6Li deficit alone is +7.6% — single-point, QUARANTINED as a")
    print("       numerology hazard (1 point, huge q0-expression entropy).")

    # ── [4] structural characterization ─────────────────────────────────────
    print("\n[4] STRUCTURAL CHARACTERIZATION of the deficit (descriptive, guarded):")
    # (b) one-bond family vs light-cluster size (witness chain-bond counting)
    size_fam = [("9Be", 1, onebond_deficits["9Be"]), ("6Li", 2, onebond_deficits["6Li"]),
                ("7Li", 3, onebond_deficits["7Li"])]
    per_a = [d / a for _, a, d in size_fam]
    c_mean = sum(per_a) / len(per_a)
    lin_dev = max(abs(x / c_mean - 1) for x in per_a)
    print(f"    (b) one-bond deficit/A_light: " +
          ", ".join(f"{i}(A={a}) {d / a:.3f}" for i, a, d in size_fam) +
          f"  — mean {c_mean:.3f} MeV/nucleon, max dev {lin_dev * 100:.1f}%")
    print("        deficit is ~LINEAR in light-cluster nucleon count (3 points —")
    print("        GUARDED regularity, extensive-in-size, NOT a spin function).")
    # (c) vs the light cluster's own binding
    r_bd = rows["6Li"]["deficit_MeV"] / float(_ame_binding_mev(1, 2))
    r_bt = rows["7Li"]["deficit_MeV"] / float(_ame_binding_mev(1, 3))
    print(f"    (c) deficit/B(light): 6Li/B_D = {r_bd:.3f}, 7Li/B_t = {r_bt:.3f}")
    print("        -> NOT the light cluster's own binding (ratios differ x2.3).")
    # spin non-function: same-j bonds differ
    same_j_ratio = rows["7Li"]["deficit_MeV"] / (rows["9Be"]["deficit_MeV"] / 2)
    print(f"        same-j contrast: alpha-t vs alpha-n (both j=1/2) deficits differ "
          f"x{same_j_ratio:.2f} -> deficit is not a function of bond spin.")
    # (d) pair-graph recounting
    print("    (d) complete-graph C(k,2) pair recounting (per-pair deficits):")
    pair_rows = {}
    for iso, row in ADD.items():
        k = len(row["pieces"])
        npair = k * (k - 1) // 2
        pair_rows[iso] = {"n_pairs": npair,
                          "deficit_per_pair_MeV": row["deficit_MeV"] / npair}
    for iso in ("8Be", "9Be", "11B", "12C", "14N", "16O", "19F"):
        pr = pair_rows[iso]
        print(f"        {iso:5s} pairs={pr['n_pairs']:2d}  "
              f"deficit/pair = {pr['deficit_per_pair_MeV']:+7.3f} MeV")
    flat_12_16 = abs(pair_rows["12C"]["deficit_per_pair_MeV"]
                     / pair_rows["16O"]["deficit_per_pair_MeV"] - 1)
    aa_k2 = rows["8Be"]["deficit_MeV"]
    aa_k3 = pair_rows["12C"]["deficit_per_pair_MeV"]
    print(f"        PURE-ALPHA FLATNESS: 12C {pair_rows['12C']['deficit_per_pair_MeV']:.4f} vs "
          f"16O {pair_rows['16O']['deficit_per_pair_MeV']:.4f} MeV/pair — agree to "
          f"{flat_12_16 * 100:.1f}%")
    print(f"        CONTEXT SWITCH: the SAME alpha-alpha pair gives {aa_k2:+.3f} MeV at k=2")
    print(f"        (8Be) but ~{aa_k3:.2f} MeV/pair at k>=3 — the pair term is MANY-BODY-")
    print("        ACTIVATED, not pairwise-additive with a universal quantum.")
    print("        (9Be counterexample: 2.41 for its alpha-alpha pair would force a")
    print("        NEGATIVE alpha-n term — the pair-graph reading also fails mixed.)")
    print(f"        GUARDED near-misses for the k>=3 alpha-alpha value ~2.41 MeV:")
    print(f"        B_D = 2.2246 (-8%), deuteron-channel rotor 2.0204 (-16%) — single-")
    print("        family, NOT claimed, quarantined.")

    # ── verdict ──────────────────────────────────────────────────────────────
    verdict = (
        "NEGATIVE (scope-(a)) for the pre-registered q-rotational inter-cluster "
        "bond term deficit(X.Y) = sum_bonds mu0*hbar_q*J_q^2(j): with j from "
        "measured cluster spins (H1) the form undershoots the one-bond deficits "
        f"x{h1_undershoot[0]:.1f}-x{h1_undershoot[1]:.1f} and predicts exactly 0 "
        "for the pure-alpha composites carrying the largest deficits (its values "
        "are intensively bounded at 0.32 MeV for j<=1 — same obstruction as the "
        "carrier-saturation result); with the fixed deuteron-channel quantum "
        "(H2, j=3, 2.02 MeV/bond) the one-bond cases land at +37%/-18% but 8Be "
        "is violated by 2.1 MeV and the residual spans x8; with the strand-count "
        "rule (H3, j=3*A_light/2) the overshoot grows monotonically with light-"
        "cluster size (0.78 -> 3.3): the q-exponential Casimir grows too fast. "
        "No CAL-3 m_pi-scale quantum matches at multiplier 1. THE FAILURE SHAPE "
        "IS THE FINDING: the deficit is (i) not a function of bond spin (same-j "
        "bonds differ x3.1), (ii) ~linear (extensive) in the light-cluster "
        "nucleon count for one-bond composites (0.78 MeV/nucleon, 3 points, "
        "guarded), (iii) many-body-activated for alpha-alpha (0 at k=2/8Be vs a "
        "flat ~2.41 MeV/pair at k>=3 — 12C vs 16O agree to 0.8% under complete-"
        "graph counting, but the same value forces a negative alpha-n term at "
        "9Be, so no universal pair quantum exists either). Scope-(a): this "
        "constrains the q-rotational and universal-pair-quantum forms AS SOLE "
        "MECHANISMS; the rotor channel, the volume tower, and the pair graph "
        "remain admissible ingredients of a many-body closure. Nothing tuned; "
        "nothing wired; all j pre-registered."
    )
    print(f"\nVERDICT: {verdict}")

    # ── witness ──────────────────────────────────────────────────────────────
    wit = {
        "computation": "inter-cluster-bond-term-derive-or-refute",
        "description": (
            "R5-a derive-or-refute of the inter-cluster bond term (the alpha-"
            "cluster additivity deficit). Pre-registered q-rotational tests "
            "deficit = sum_bonds mu0*hbar_q*J_q^2(j) with j from measured "
            "cluster spins (H1), the fixed deuteron channel j=3 (H2), and the "
            "strand-count rule j=3*A_light/2 (H3); CAL-3 m_pi-scale quantum "
            "family; structural characterization (spin non-function, ~linear "
            "in light-cluster size, many-body-activated alpha-alpha pair term). "
            "All inputs from the committed alpha-cluster-volume-additivity "
            "witness; nothing recomputed, nothing tuned."),
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath (symbolic-exact; witness-fed, no new tr_M compute)",
        "inputs": {
            "deficit_source": "alpha-cluster-volume-additivity.witness.json (committed; consistency-checked to 1e-9 MeV)",
            "m_e_MeV": {"value": float(M_E), "source": "codata_constants.M_E_MEV (CODATA 2022, CAL-1)"},
            "q0": {"value": Q_50_DIGIT_STR[:20] + "...", "source": "q_parameter.Q_50_DIGIT_STR"},
            "m_pi_MeV": {"value": float(M_PI), "source": "codata_constants.M_PI_PM_MEV_VALIDATION (CAL-3)"},
            "cluster_spins_PRE_REGISTERED": {
                "4He": "0 (ENSDF 0+)", "d": "1 (ENSDF 1+)",
                "t": "1/2 (ENSDF 1/2+)", "n": "1/2"},
            "derived_scales": {
                "mu0_MeV": float(MU0), "hbar_q": float(HBAR_Q),
                "mu0_hbar_q_MeV": float(E_UNIT),
                "E_rot_deuteron_channel_j3_MeV": float(E_D_CH),
                "source": "binding_qhamiltonian_rotational_scale.py (all derived, 0 free params)"},
        },
        "q_rotational_tests": rows,
        "alt_9Be_two_alpha_n_bonds": alt_9be,
        "H3_bond_family": [
            {"bond": n, "A_light": a, "pred_MeV": p, "deficit_MeV": d,
             "pred_over_deficit": p / d} for n, a, p, d in fam],
        "cal3_family_GUARDED": cal3,
        "characterization": {
            "contact_nucleons_note": "not extractable from committed data (disjoint-cluster composite reading); size characterization below is the operative version",
            "one_bond_deficit_per_A_light_MeV": {i: d / a for i, a, d in size_fam},
            "linear_in_A_light_mean_MeV_per_nucleon": c_mean,
            "linear_in_A_light_max_dev": lin_dev,
            "guard": "3 points only — descriptive regularity, not a model",
            "deficit_over_B_light": {"6Li_over_B_D": r_bd, "7Li_over_B_t": r_bt},
            "same_j_bonds_deficit_ratio_alpha_t_vs_alpha_n": same_j_ratio,
            "pair_graph_recounting": pair_rows,
            "pure_alpha_per_pair_flatness_12C_vs_16O": flat_12_16,
            "alpha_alpha_pair_k2_MeV": aa_k2,
            "alpha_alpha_pair_k3plus_MeV": aa_k3,
            "pair_graph_failure": "universal ~2.41 MeV/pair forces negative alpha-n at 9Be",
            "guarded_near_misses_NOT_claimed": {
                "B_D_2.2246_vs_2.41": "-8%", "deuteron_rotor_2.0204_vs_2.41": "-16%"},
        },
        "verdict": verdict,
        "scope": "(a) — constrains q-rotational / universal-pair forms as sole mechanisms; no ingredient excluded",
        "assertions": [
            {"label": "committed witness deficits reproduce from vendored AME2020 to 1e-9 MeV",
             "passed": bool(witness_consistent)},
            {"label": "H1 (cluster-spin rotor) undershoots one-bond deficits by >= 4x",
             "passed": bool(min(h1_undershoot) >= 4.0)},
            {"label": "H1 predicts exactly 0 for pure-alpha composites with deficits > 7 MeV (decisive negative)",
             "passed": bool(h1_zero_on_big)},
            {"label": "H1 intensive bound: max per-bond value (j<=1) < min multi-alpha per-pair deficit",
             "passed": bool(h1_bound < aa_k3)},
            {"label": "H2 (deuteron channel/bond): one-bond within 40% (6Li +37%, 7Li -18%) BUT 8Be violated by > 1.5 MeV -> not universal",
             "passed": bool(abs(h2_r6 - 1) <= 0.40 and abs(h2_r7 - 1) <= 0.40
                            and h2_8be_viol > 1.5)},
            {"label": "H3 (strand-count) pred/deficit strictly increasing in A_light (wrong j-dependence: q-exponential vs ~linear)",
             "passed": bool(h3_monotone)},
            {"label": "no CAL-3 family member matches one-bond deficits at multiplier 1 (all deviate > 30% somewhere)",
             "passed": bool(no_universal_cal3)},
            {"label": "one-bond deficit ~linear in A_light (max dev < 10% about 0.78 MeV/nucleon; GUARDED, 3 points)",
             "passed": bool(lin_dev < 0.10)},
            {"label": "pure-alpha per-pair flatness: 12C vs 16O deficit/pair agree to < 2%",
             "passed": bool(flat_12_16 < 0.02)},
            {"label": "alpha-alpha pair term many-body-activated: |k=2 value| < 0.1 MeV while k>=3 value > 2 MeV",
             "passed": bool(abs(aa_k2) < 0.1 and aa_k3 > 2.0)},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = _HERE / "inter-cluster-bond-term.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = _os.path.basename(__file__)
    json.dump(wit, open(out, "w"), indent=1)
    print(f"\nwitness -> {out.name}   allPassed: {wit['allPassed']}")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
