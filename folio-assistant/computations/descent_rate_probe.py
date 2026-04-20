#!/usr/bin/env python3
"""
Descent-rate probe: empirically fit 𝒫_n partial-descent weights.

Parameterize the pair blow-up contribution at jet level n as

   z² · Σ_{i<j}  β(|i−j|) · Φ_q(|V̂_i V̂_j|)

where β(d) ∈ [0, 1] is the "independence fraction" at generator
distance d:
  β(d) = 1       → pair is an independent jet-n centre (not descended)
  β(d) = 0       → pair fully descends to jet level n−1 (already counted)
  β(d) ∈ (0,1)   → partial descent

Special cases:
  prop's adjacent-only:    β(1) = 1, β(d≥2) = 0
  full all-pairs (probe):  β(d) = 1  for all d ≥ 1

This module scans one-parameter families of β(d) and finds the α that
minimizes |Δm/m|% against B_AME on stable atoms A ≥ 6.

Families probed:
  exponential:  β(d) = α^(d-1)               — 1 at d=1; α controls decay
  step:         β(d) = 1 if d ≤ α else 0     — cutoff distance α
  1/d:          β(d) = α^0=1 for d=1, α/(d-1) for d≥2   — 1/d decay
  linear:       β(d) = max(0, 1 - α·(d-1))   — linear decay to 0

"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import q0, Phi_q, z_mark
from pyhecke.gram import atom_per_generator_volumes


def mass_with_beta(vols, beta_fn):
    """Tower mass with pair weights β(|i−j|)."""
    n = len(vols)
    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = sum(Phi_q(abs(v["full"])) for v in vols)
    cross = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            b = beta_fn(j - i)
            if b == 0:
                continue
            cross += b * (z_mark ** 2) * Phi_q(
                abs(vols[i]["full"] * vols[j]["full"]))
    return desc + single + cross


def get_ilp_ground(Z, N):
    p = Path(__file__).parent / "confinement-level-walk.witness.json"
    if not p.exists():
        return {"m_pp": 1, "m_pn": 1, "m_nn": 1}
    w = json.loads(p.read_text())
    atoms = w.get("levels", {}).get("3", {}).get("atoms", {})
    for _k, d in atoms.items():
        if d.get("Z") == Z and d.get("N") == N and not d.get("unstable"):
            return d["ground_state"]
    return {"m_pp": 1, "m_pn": 1, "m_nn": 1}


def B_pred(Z, N, beta_fn, E_0=938.272 / 1178995.5254):
    gs = get_ilp_ground(Z, N)
    va = atom_per_generator_volumes(
        Z, N, include_inter=True,
        m_pp=gs["m_pp"], m_pn=gs["m_pn"], m_nn=gs["m_nn"])
    vf = atom_per_generator_volumes(Z, N, include_inter=False)
    return E_0 * (mass_with_beta(vf, beta_fn) - mass_with_beta(va, beta_fn))


# Families

def beta_exp(alpha):
    return lambda d: alpha ** (d - 1)


def beta_step(cutoff):
    return lambda d: 1.0 if d <= cutoff else 0.0


def beta_oneoverd(alpha):
    def b(d):
        if d == 1:
            return 1.0
        return alpha / (d - 1)
    return b


def beta_linear(slope):
    return lambda d: max(0.0, 1.0 - slope * (d - 1))


# Benchmark atoms
ATOMS = [
    ("D",    1, 1,  2.22452),
    ("6Li",  3, 3, 32.0),
    ("9Be",  4, 5, 58.1650),
    ("10B",  5, 5, 64.750),
    ("12C",  6, 6, 92.161728),
    ("14N",  7, 7, 104.659),
    ("16O",  8, 8, 127.619),
]


def mean_err_pct(beta_fn, atoms=ATOMS):
    errs = []
    for name, Z, N, B_AME in atoms:
        try:
            B = B_pred(Z, N, beta_fn)
            if not math.isfinite(B):
                continue
            dm = abs(B - B_AME) / ((Z + N) * 938.272) * 100
            errs.append(dm)
        except Exception:
            continue
    return sum(errs) / len(errs) if errs else float("inf"), len(errs)


if __name__ == "__main__":
    print("=" * 100)
    print("DESCENT-RATE PROBE: fitting β(d) = P(pair at distance d is independent)")
    print(f"q₀ = {q0:.6f}, z² = {z_mark**2:.4f}")
    print(f"Atoms: {[a[0] for a in ATOMS]}")
    print("=" * 100)

    # Baselines
    print("\nBaselines (reference):")
    adj, n_adj = mean_err_pct(beta_step(1))
    full, n_full = mean_err_pct(beta_step(9999))
    print(f"  adjacent-only  (β(1)=1, β(d≥2)=0):  mean |Δm/m|% = {adj:.4f}%  (n={n_adj})")
    print(f"  full all-pairs (β(d)=1 ∀d):         mean |Δm/m|% = {full:.4f}%  (n={n_full})")

    results = {"baselines": {"adjacent": adj, "full": full}}

    # Exponential decay: β(d) = α^(d-1)
    print("\nExponential decay: β(d) = α^(d-1)")
    best_exp = (None, float("inf"))
    exp_scan = []
    for alpha in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0]:
        err, n = mean_err_pct(beta_exp(alpha))
        exp_scan.append({"alpha": alpha, "err_pct": err, "n": n})
        marker = ""
        if err < best_exp[1]:
            best_exp = (alpha, err)
            marker = "  ←"
        print(f"  α = {alpha:.2f}: mean |Δm/m|% = {err:.4f}% (n={n}){marker}")
    print(f"  best exp:  α* = {best_exp[0]}, err = {best_exp[1]:.4f}%")
    results["exp"] = {"scan": exp_scan, "best": best_exp}

    # Step cutoff: β(d) = 1 if d ≤ cutoff else 0
    print("\nStep cutoff: β(d) = 1 if d ≤ cutoff else 0")
    best_step = (None, float("inf"))
    step_scan = []
    for cutoff in [1, 2, 3, 5, 7, 10, 15, 20, 30, 50]:
        err, n = mean_err_pct(beta_step(cutoff))
        step_scan.append({"cutoff": cutoff, "err_pct": err, "n": n})
        marker = ""
        if err < best_step[1]:
            best_step = (cutoff, err)
            marker = "  ←"
        print(f"  cutoff = {cutoff:>2d}: mean |Δm/m|% = {err:.4f}% (n={n}){marker}")
    print(f"  best step: cutoff* = {best_step[0]}, err = {best_step[1]:.4f}%")
    results["step"] = {"scan": step_scan, "best": best_step}

    # 1/d decay: β(d=1)=1, β(d≥2) = α/(d-1)
    print("\n1/d decay: β(1)=1, β(d≥2) = α/(d−1)")
    best_od = (None, float("inf"))
    od_scan = []
    for alpha in [0.0, 0.1, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]:
        err, n = mean_err_pct(beta_oneoverd(alpha))
        od_scan.append({"alpha": alpha, "err_pct": err, "n": n})
        marker = ""
        if err < best_od[1]:
            best_od = (alpha, err)
            marker = "  ←"
        print(f"  α = {alpha:.2f}: mean |Δm/m|% = {err:.4f}% (n={n}){marker}")
    print(f"  best 1/d:  α* = {best_od[0]}, err = {best_od[1]:.4f}%")
    results["oneoverd"] = {"scan": od_scan, "best": best_od}

    # Linear decay: β(d) = max(0, 1 - slope·(d-1))
    print("\nLinear decay: β(d) = max(0, 1 − slope·(d−1))")
    best_lin = (None, float("inf"))
    lin_scan = []
    for slope in [0.0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
        err, n = mean_err_pct(beta_linear(slope))
        lin_scan.append({"slope": slope, "err_pct": err, "n": n})
        marker = ""
        if err < best_lin[1]:
            best_lin = (slope, err)
            marker = "  ←"
        print(f"  slope = {slope:.3f}: mean |Δm/m|% = {err:.4f}% (n={n}){marker}")
    print(f"  best linear: slope* = {best_lin[0]}, err = {best_lin[1]:.4f}%")
    results["linear"] = {"scan": lin_scan, "best": best_lin}

    # Per-atom table for the empirical best
    best_family, best_val = "full", full
    for name, data in results.items():
        if name == "baselines":
            continue
        if data["best"][1] < best_val:
            best_val = data["best"][1]
            best_family = name
    print(f"\nBest overall family: {best_family}, mean err = {best_val:.4f}%")

    # Per-atom breakdown of best
    print(f"\nPer-atom breakdown of best β (and baselines):")
    fns = {
        "adjacent": beta_step(1),
        "full": beta_step(9999),
        f"exp(α*={best_exp[0]})": beta_exp(best_exp[0]),
        f"step(cutoff*={best_step[0]})": beta_step(best_step[0]),
    }
    print(f"  {'Atom':>6} {'B_AME':>8}  " + "  ".join(f"{n:>18}" for n in fns))
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        M_total = A * 938.272
        line = f"  {name:>6} {B_AME:>8.3f}  "
        for label, bf in fns.items():
            try:
                B = B_pred(Z, N, bf)
                if not math.isfinite(B):
                    line += f"{'inf':>18}  "
                else:
                    dm = abs(B - B_AME) / M_total * 100
                    line += f"{dm:>17.4f}%  "
            except Exception:
                line += f"{'err':>18}  "
        print(line)

    # Witness
    witness = {
        "computation": "descent-rate-probe",
        "description": (
            "Empirical fit of partial-descent weights β(|i−j|) for "
            "pair blow-up centres in prop:mass-endomorphism-tower. "
            "Parameterizes the deviation from adjacent-only (β=δ_{d,1}) "
            "and full all-pairs (β=1 uniform) as one-parameter "
            "families (exponential, step, 1/d, linear).  Minimizes "
            "mean |Δm/m|% on stable atoms A≥6 and D."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "z_markov_sq": z_mark ** 2},
        "atoms": [{"atom": a[0], "Z": a[1], "N": a[2], "B_AME": a[3]}
                   for a in ATOMS],
        "results": results,
        "best_family": best_family,
        "best_mean_err_pct": best_val,
    }
    out = Path(__file__).parent / "descent-rate-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
