#!/usr/bin/env python3
"""
Option E v6 — combined canonical formula.

The cheat sheet documents TWO distinct canonical derivations:

1. q-Hamiltonian rotational scale (binding_qhamiltonian_rotational_scale.py):
     E_rot(K) = μ₀ · ℏ_q · J_q²(n/2)
   with μ₀ = m_e/(3(q-q⁻¹)/2), ℏ_q = 1-q⁻¹, J_q²(j) = [j]_q·[j+1]_q.
   Closes D to −9% from fully-derived quantities; A≥3 undershoots by 44-72%.

2. Markov-weighted q-Reeb phase (binding_reeb_phase_decomposition.py):
   Closes A=3 mirror pair (³H − ³He DIFFERENCE) to 2% with no fit, via
   the per-rep phase shifts Δθ_λ = arccos(χ_atom/d) - arccos(χ_free/d).
   The scalar tr_M collapses this.

v6 reproduces both canonical results and tests an explicit COMBINATION:

   B_canonical(K) := μ₀ · ℏ_q · J_q²(n/2)     (rotational scale)
                   + γ · Σ_rot y_λ Δθ_λ        (per-rep phase correction)

where γ is a derived scale to be determined (candidates: μ₀, m_e, ℏ_q).

This v6 directly REPRODUCES the canonical-script outputs (E_rot)
as a verification baseline, then probes how the phase correction
shifts B for the mirror pair (³H/³He).

Output:
  option-e-v6-combined-canonical.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp, fabs, acos
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
mp.dps = 50


M_E_MEV = mpf("0.51099895069")
Q_0 = mpf("1.1097090249")

H = Q_0 - 1 / Q_0
HBAR_Q = 1 - 1 / Q_0
MU_0 = M_E_MEV / (mpf(3) * H / mpf(2))

AME_MeV = {"D": mpf("2.224566"), "T": mpf("8.481798"),
           "3He": mpf("7.71806")}
N_STRANDS = {"D": 6, "T": 9, "3He": 9}


def br(x):
    """q-bracket [x]_q = (q^x - q^-x) / (q - q^-1)."""
    return (Q_0**x - Q_0**(-x)) / (Q_0 - Q_0**(-1))


def Jq2(j):
    """q-angular momentum J_q² = [j]_q · [j+1]_q."""
    return br(j) * br(j + 1)


def E_rot(n):
    """Canonical q-Hamiltonian rotational energy E_rot = μ₀ · ℏ_q · J_q²(n/2)."""
    j = mpf(n) / 2
    return MU_0 * HBAR_Q * Jq2(j)


def dim_sn(lam):
    lam = list(lam)
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def load_chi_free_atom(repo_root, atom_label):
    fn_map = {"D": "d", "T": "t", "3He": "3he"}
    fn = (repo_root / "computations"
          / f"atom-chi-rust-{fn_map[atom_label]}.witness.json")
    with fn.open() as f:
        data = json.load(f)["data"]
    chi_free, chi_atom = {}, {}
    for cfg, target in [("free", chi_free), ("atom", chi_atom)]:
        for e in data[cfg]["by_partition"]:
            part = e["partition"]
            if isinstance(part, str):
                part = tuple(eval(part))
            else:
                part = tuple(part)
            target[part] = mpf(str(e["chi_lambda"]))
    return chi_free, chi_atom


def load_y_lambda(repo_root, atom_label):
    name_map = {"D": "deuteron-h6", "T": "tritium-h9", "3He": "helium-3-h9"}
    fn = (repo_root / "computations"
          / f"chi-{name_map[atom_label]}-at-q0-50dps.witness.json")
    with fn.open() as f:
        data = json.load(f)
    y = {}
    for e in data["by_partition"]:
        part = e["partition"]
        if isinstance(part, str):
            part = tuple(eval(part))
        else:
            part = tuple(part)
        y[part] = mpf(e["y_lambda"])
    return y


def reeb_phase_sum(chi_free, chi_atom, y_lambda):
    """Σ_rot y_λ · Δθ_λ + decomposition data."""
    rot_sum_abs = mpf(0)
    rot_sum_signed = mpf(0)
    rot_count = 0
    growth_count = 0
    growth_y_chi_diff = mpf(0)  # Σ_growth y_λ · (|χ_atom| - |χ_free|)
    blocks = []
    for part in chi_free:
        d = mpf(dim_sn(part))
        r_f = chi_free[part] / d
        r_a = chi_atom[part] / d
        y = y_lambda.get(part, mpf(0))
        is_rot = (fabs(r_f) <= 1) and (fabs(r_a) <= 1)
        if is_rot:
            th_f = acos(r_f)
            th_a = acos(r_a)
            dth = th_a - th_f
            rot_sum_abs += y * fabs(dth)
            rot_sum_signed += y * dth
            rot_count += 1
            blocks.append({"part": str(part), "type": "rot",
                           "delta_theta": float(dth), "y": float(y)})
        else:
            growth_count += 1
            growth_y_chi_diff += y * (fabs(chi_atom[part]) - fabs(chi_free[part]))
            blocks.append({"part": str(part), "type": "growth",
                           "chi_diff": float(fabs(chi_atom[part]) - fabs(chi_free[part])),
                           "y": float(y)})
    return {
        "rot_sum_abs": rot_sum_abs,
        "rot_sum_signed": rot_sum_signed,
        "rot_count": rot_count,
        "growth_count": growth_count,
        "growth_y_chi_diff": growth_y_chi_diff,
        "blocks": blocks,
    }


def main() -> int:
    set_compute_dps()
    repo_root = Path(__file__).resolve().parent.parent

    print(f"DERIVED SCALES:")
    print(f"  μ₀     = {float(MU_0):.6f} MeV")
    print(f"  ℏ_q    = {float(HBAR_Q):.6f}")
    print(f"  μ₀·ℏ_q = {float(MU_0 * HBAR_Q):.6f}")
    print(f"  q_0    = {float(Q_0):.6f}")
    print(f"  h      = {float(H):.6f}\n")

    # Part 1: Reproduce canonical q-Hamiltonian rotational result
    print(f"=== Canonical formula 1: B = μ₀ · ℏ_q · J_q²(n/2) ===")
    print(f"  {'atom':5s}{'n':>4s}{'j':>5s}{'J_q²':>10s}{'E_rot':>10s}"
          f"{'B_AME':>10s}{'err':>8s}")
    canonical_results = {}
    for atom in ["D", "T", "3He"]:
        n = N_STRANDS[atom]
        j = mpf(n) / 2
        J = Jq2(j)
        Erot = E_rot(n)
        Btgt = AME_MeV[atom]
        err = float((Erot - Btgt) / Btgt * 100)
        canonical_results[atom] = {
            "n": n, "j": float(j), "Jq2": str(J),
            "E_rot_MeV": str(Erot), "B_target_MeV": str(Btgt),
            "rel_err_pct": err,
        }
        print(f"  {atom:5s}{n:>4d}{float(j):>5.1f}{float(J):>10.4f}"
              f"{float(Erot):>10.4f}{float(Btgt):>10.4f}{err:>+7.1f}%")
    print()

    # Part 2: Reeb-phase decomposition for ³H, ³He, D
    print(f"=== Reeb phase decomposition (per atom) ===")
    reeb_results = {}
    for atom in ["D", "T", "3He"]:
        chi_free, chi_atom = load_chi_free_atom(repo_root, atom)
        y_lam = load_y_lambda(repo_root, atom)
        r = reeb_phase_sum(chi_free, chi_atom, y_lam)
        reeb_results[atom] = {
            "rot_count": r["rot_count"],
            "growth_count": r["growth_count"],
            "Σ_rot_y_|Δθ|": str(r["rot_sum_abs"]),
            "Σ_rot_y_Δθ_signed": str(r["rot_sum_signed"]),
            "Σ_growth_y_(|χ_atom|-|χ_free|)": str(r["growth_y_chi_diff"]),
        }
        print(f"  {atom}: rot={r['rot_count']}, growth={r['growth_count']}")
        print(f"    Σ_rot y |Δθ|     = {float(r['rot_sum_abs']):.6f}")
        print(f"    Σ_rot y Δθ signed = {float(r['rot_sum_signed']):.6f}")
        print(f"    Σ_growth y (|χ_a|-|χ_f|) = {float(r['growth_y_chi_diff']):.6f}")
    print()

    # Part 3: Mirror pair ³H − ³He (the "2% closure" claim)
    print(f"=== Mirror pair ³H - ³He difference ===")
    Btgt_T = AME_MeV["T"]
    Btgt_He3 = AME_MeV["3He"]
    diff_target = Btgt_T - Btgt_He3  # +0.7638 MeV
    print(f"  Target: B_T - B_³He = {float(diff_target):.4f} MeV")
    # E_rot identical for T and ³He (same n=9, same j=9/2)
    # Difference must come from per-rep Reeb decomposition
    diff_rot_signed = (mpf(reeb_results["T"]["Σ_rot_y_Δθ_signed"])
                      - mpf(reeb_results["3He"]["Σ_rot_y_Δθ_signed"]))
    diff_rot_abs = (mpf(reeb_results["T"]["Σ_rot_y_|Δθ|"])
                   - mpf(reeb_results["3He"]["Σ_rot_y_|Δθ|"]))
    diff_growth = (mpf(reeb_results["T"]["Σ_growth_y_(|χ_atom|-|χ_free|)"])
                  - mpf(reeb_results["3He"]["Σ_growth_y_(|χ_atom|-|χ_free|)"]))
    print(f"  Σ y Δθ (T) - Σ y Δθ (³He) signed = {float(diff_rot_signed):.6f}")
    print(f"  Σ y |Δθ| (T) - Σ y |Δθ| (³He)    = {float(diff_rot_abs):.6f}")
    print(f"  growth diff (T) - growth diff (³He) = {float(diff_growth):.6f}")
    print()

    # Probe a few scale candidates for the mirror-pair difference
    print(f"=== Mirror-pair scale candidates ===")
    candidates = {
        "μ₀ · Σ_rot y Δθ signed":  MU_0 * diff_rot_signed,
        "μ₀ · Σ_rot y |Δθ|":       MU_0 * diff_rot_abs,
        "μ₀ · growth_diff":         MU_0 * diff_growth,
        "μ₀ · ℏ_q · Σ_rot y Δθ":   MU_0 * HBAR_Q * diff_rot_signed,
        "m_e · Σ_rot y Δθ signed":  M_E_MEV * diff_rot_signed,
        "m_e · growth_diff":        M_E_MEV * diff_growth,
    }
    for name, value in candidates.items():
        err = float((value - diff_target) / diff_target * 100)
        marker = "  ✓✓" if abs(err) <= 2 else "  ✓" if abs(err) <= 10 else "   "
        print(f"{marker} {name:35s}: {float(value):+9.5f} MeV  (target {float(diff_target):+.4f}, err {err:+7.1f}%)")

    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-v6-combined-canonical",
        "description": (
            "Option E v6: reproduces canonical q-Hamiltonian rotational "
            "energy AND tests Markov-weighted Reeb phase mirror pair "
            "decomposition (³H - ³He) per docs/canonical-derivation-cheat-sheet.md"
        ),
        "scriptFile": "option_e_v6_combined_canonical.py",
        "precisionMetadata": {"compute_dps": 50, "output_dps": 30},
        "derived_scales": {
            "mu_0_MeV": str(MU_0),
            "hbar_q": str(HBAR_Q),
            "q_0": str(Q_0),
            "h": str(H),
        },
        "canonical_rotational_results": canonical_results,
        "reeb_phase_results": reeb_results,
        "mirror_pair_difference": {
            "target_MeV": str(diff_target),
            "candidates": {
                name: {
                    "value_MeV": str(value),
                    "rel_err_pct": float((value - diff_target) / diff_target * 100),
                    "closes_2pct": abs(float((value - diff_target) / diff_target * 100)) <= 2.0,
                }
                for name, value in candidates.items()
            },
        },
    }

    out_path = (
        repo_root / "computations"
        / "option-e-v6-combined-canonical.witness.json"
    )
    with out_path.open("w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
