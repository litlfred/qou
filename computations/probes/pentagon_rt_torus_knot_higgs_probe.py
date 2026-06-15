"""Q2: Reshetikhin-Turaev at root-of-unity → Higgs mass candidate via T(2, 8).

Per Q3 finding (`torus_knot_markov_trace_closed_form.py`): torus knots
have Vol = 0; the canonical VolDensity mass formula gives zero. The
Higgs/W/Z/strong-force-torus masses need a separate categorical chain.

The standard alternative for torus knots is **Reshetikhin-Turaev (RT)
TQFT** at root-of-unity q. The colored Jones polynomial $J_N(K, q)$
of a knot K, evaluated at $q = e^{2\pi i/N}$ for the N-dim irrep
of $U_q(\mathfrak{sl}_2)$, is the RT-invariant; it gives a
finite-dimensional topological invariant that does NOT depend on
hyperbolic volume.

This probe:

1. Computes $J_N(T(2, 8), q)$ for $N = 2, 3, 4, 5, 6, 8$ using the
   standard closed form for torus links T(2, n).
2. Evaluates at:
   - $q = q_0 \approx 1.1097$ (substrate)
   - $q = e^{2\pi i / N}$ (root of unity at level N)
   - $q = e^{2\pi i / (N+2)}$ (level k = N, k+2 standard RT shift)
3. For each (N, q) combination, computes a candidate "mass scale" via
   $|J_N| \cdot m_e$ or $\log|J_N| \cdot m_e \cdot k$ for various k.
4. Compares to the actual Higgs mass $m_H = 125.10\;\text{GeV}
   \approx 2.447 \times 10^5 \cdot m_e$.

If a substrate-natural (N, q) gives $J_N \approx 2.447 \times 10^5$
or any easily-related scale, that's a candidate Higgs mass formula via
the RT route.

Status: EXPLORATORY. Probe document; first numerical look at whether
RT-at-root-of-unity can produce a Higgs mass scale.

## Reference: J_N for T(2, n) torus link

For the (p, q) = (2, n) torus link, the unnormalized colored Jones
in the N-dim irrep of $U_q(\mathfrak{sl}_2)$ admits the closed form
(see Morton 1995, Hikami 2004):

  J_N(T(2, n), q) = (1/[N]) · Σ_{j=0}^{N-1} (-1)^j q^{n(N-1-2j)(N+1-2j)/4}

where [N] = (q^{N/2} - q^{-N/2}) / (q^{1/2} - q^{-1/2}) is the quantum
integer.

Status: EXPLORATORY (per `local/production-vs-exploratory-discipline`).
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import subprocess
import sys
from pathlib import Path

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mpmath import mpc, mpf

mp.mp.dps = 50

# Substrate + physical constants
Q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
M_E_MEV = mpf("0.510998950")
M_HIGGS_GEV = mpf("125.10")
M_HIGGS_MEV = M_HIGGS_GEV * 1000
M_H_OVER_M_E = M_HIGGS_MEV / M_E_MEV  # ≈ 244811


def quantum_integer(N: int, q):
    """[N]_q = (q^{N/2} - q^{-N/2}) / (q^{1/2} - q^{-1/2})."""
    sq = mp.sqrt(q)
    sqi = mpf(1) / sq
    return (sq ** N - sqi ** N) / (sq - sqi)


def colored_jones_T2n(N: int, n: int, q) -> mpc:
    """Unnormalized colored Jones J_N(T(2, n), q) for the N-dim irrep
    of U_q(sl_2). Uses the standard torus-link closed form:

      J_N(T(2,n), q) = (1/[N]) · Σ_{j=0}^{N-1} (-1)^j q^{n(N-1-2j)(N+1-2j)/4}

    Returns complex (works for both real q and root-of-unity q).
    """
    bracket_N = quantum_integer(N, q)
    if bracket_N == 0:
        return mp.nan
    total = mpc(0)
    for j in range(N):
        exponent = mpf(n) * (N - 1 - 2 * j) * (N + 1 - 2 * j) / 4
        sign = (-1) ** j
        total += sign * q ** exponent
    return total / bracket_N


def evaluate_at(q, N: int, n: int, q_label: str) -> dict:
    """Evaluate J_N(T(2, n), q) at given q, return summary."""
    try:
        j = colored_jones_T2n(N, n, q)
        magnitude = abs(j)
        return {
            "q_label": q_label,
            "q_real": float(q.real) if hasattr(q, 'real') else float(q),
            "q_imag": float(q.imag) if hasattr(q, 'imag') else 0.0,
            "J_N_real": float(j.real),
            "J_N_imag": float(j.imag),
            "J_N_magnitude": float(magnitude),
            # Keep substrate precision via mp.mpf (numeric, not string —
            # downstream needs val>0 / format / division per Copilot #2050).
            "log_J_N_magnitude": (mp.log(magnitude) if magnitude > 0 else None),
        }
    except Exception as e:
        return {"q_label": q_label, "error": str(e)}


def mass_scale_candidates(j_value: mpc, N: int) -> dict:
    """For a J_N value, compute candidate mass scales and compare to Higgs."""
    mag = abs(j_value)
    if mag == 0:
        return {"applicable": False}
    log_mag = mp.log(mag) if mag > 0 else mpf(0)
    candidates = {
        "|J_N| · m_e (MeV)": float(mag * M_E_MEV),
        "log|J_N| · m_e (MeV)": float(log_mag * M_E_MEV) if log_mag > 0 else 0,
        "exp(|J_N|) · m_e (MeV)": (
            # mp.mpf preserves substrate precision AND remains numeric
            # for downstream val>0 / format / division (per Copilot
            # #2050 review — mp.nstr broke numeric ops).
            mp.exp(mag) * M_E_MEV if mag < 50 else None  # avoid overflow
        ),
        "|J_N|² · m_e (MeV)": float(mag ** 2 * M_E_MEV),
        "(|J_N|·N) · m_e (MeV)": float(mag * N * M_E_MEV),
        "(|J_N|·N²) · m_e (MeV)": float(mag * N ** 2 * M_E_MEV),
    }
    ratios = {}
    for label, val in candidates.items():
        if val is not None and val > 0:
            ratios[label + " / m_H"] = float(mpf(str(val)) / M_HIGGS_MEV)
    return {"candidates_MeV": candidates, "ratios_to_higgs": ratios}


def main() -> None:
    print("Q2: RT colored Jones J_N(T(2, 8)) → Higgs mass candidate via root-of-unity")
    print(f"50-dps mpmath; substrate q_0 = {Q_0}")
    print(f"Higgs target: m_H = {float(M_HIGGS_GEV)} GeV = {float(M_HIGGS_MEV):.2f} MeV")
    print(f"             m_H / m_e = {float(M_H_OVER_M_E):.1f}")
    print("=" * 75)

    # Higgs = T(2, 8), so n = 8
    n_torus = 8
    print(f"\nTarget: T(2, {n_torus}) = Higgs boson H per electroweak-higgs-torus-link-triplet.md")

    # Test multiple N (color dimension) values
    N_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    results = []
    for N in N_values:
        # 1. At substrate q_0 (real, not root of unity)
        eval_q0 = evaluate_at(Q_0, N, n_torus, f"q_0={float(Q_0):.4f}")
        # 2. At root of unity q = exp(2πi/N) (level N RT)
        q_root_N = mp.exp(mpc(0, 2 * mp.pi / N))
        eval_root_N = evaluate_at(q_root_N, N, n_torus, f"exp(2πi/{N})")
        # 3. At shifted root of unity q = exp(2πi/(N+2)) (level k = N+2 standard RT)
        q_root_Np2 = mp.exp(mpc(0, 2 * mp.pi / (N + 2)))
        eval_root_Np2 = evaluate_at(q_root_Np2, N, n_torus, f"exp(2πi/{N+2})")

        # Mass-scale candidates at q_0
        if "J_N_magnitude" in eval_q0:
            jmag = mpf(eval_q0["J_N_magnitude"])
            j_complex = mpc(eval_q0["J_N_real"], eval_q0["J_N_imag"])
            mass_at_q0 = mass_scale_candidates(j_complex, N)
        else:
            mass_at_q0 = {}

        # At root-of-unity
        if "J_N_magnitude" in eval_root_N:
            j_complex_root = mpc(eval_root_N["J_N_real"], eval_root_N["J_N_imag"])
            mass_at_root = mass_scale_candidates(j_complex_root, N)
        else:
            mass_at_root = {}

        results.append({
            "N": N,
            "eval_q0": eval_q0,
            "eval_root_N": eval_root_N,
            "eval_root_Np2": eval_root_Np2,
            "mass_candidates_at_q0": mass_at_q0,
            "mass_candidates_at_root_N": mass_at_root,
        })

        print(f"\nN = {N} (color dim):")
        if "J_N_magnitude" in eval_q0:
            print(f"  at q_0:        |J_{N}(T(2,{n_torus}))| = {eval_q0['J_N_magnitude']:.4f}")
        if "J_N_magnitude" in eval_root_N:
            print(f"  at exp(2πi/{N}):  |J_{N}(T(2,{n_torus}))| = {eval_root_N['J_N_magnitude']:.4f}")
        if "J_N_magnitude" in eval_root_Np2:
            print(f"  at exp(2πi/{N+2}):  |J_{N}(T(2,{n_torus}))| = {eval_root_Np2['J_N_magnitude']:.4f}")

    # Find any candidate close to m_H / m_e ≈ 244811
    print("\n" + "=" * 75)
    print(f"BEST CANDIDATES vs m_H/m_e = {float(M_H_OVER_M_E):.1f}")
    print("=" * 75)
    print(f"{'N':<4} {'q_label':<20} {'candidate':<35} {'value':>14} {'ratio/m_H':>13}")
    print("-" * 90)
    best_ratio = None
    best_info = None
    for r in results:
        N = r["N"]
        for q_label, mass_dict in [
            ("q_0", r.get("mass_candidates_at_q0", {}).get("candidates_MeV", {})),
            ("root_N", r.get("mass_candidates_at_root_N", {}).get("candidates_MeV", {})),
        ]:
            for cand_label, val in mass_dict.items():
                if val is None or val <= 0:
                    continue
                ratio = val / float(M_HIGGS_MEV)
                # interested in ratios within 5 orders of magnitude
                if 0.01 < ratio < 100:
                    print(f"{N:<4} {q_label:<20} {cand_label:<35} {val:>14.4f} {ratio:>13.6f}")
                    if best_ratio is None or abs(mp.log(mpf(str(ratio)))) < abs(mp.log(mpf(str(best_ratio)))):
                        best_ratio = ratio
                        best_info = {"N": N, "q_label": q_label, "candidate": cand_label, "value_MeV": val, "ratio_m_H": ratio}

    print("\n" + "=" * 75)
    print("VERDICT")
    print("=" * 75)
    if best_info:
        print(f"Best candidate: N={best_info['N']}, q={best_info['q_label']}")
        print(f"  formula: {best_info['candidate']}")
        print(f"  value:   {best_info['value_MeV']:.4f} MeV")
        print(f"  ratio to m_H: {best_info['ratio_m_H']:.6f}")
        if 0.5 < best_info['ratio_m_H'] < 2.0:
            print(f"  → WITHIN 2× of Higgs mass! Investigate this combination further.")
        elif 0.1 < best_info['ratio_m_H'] < 10:
            print(f"  → within 10× of Higgs mass; partial structural signature")
        else:
            print(f"  → off by >10×; no immediate Higgs candidate via these formulas")
    else:
        print("No candidate within (0.01, 100) × m_H ratio range — likely need different RT chain")

    # Witness
    witness = {
        "compute": "pentagon_rt_torus_knot_higgs_probe",
        "description": (
            "Q2: Reshetikhin-Turaev colored Jones J_N(T(2,8)) probe for "
            "candidate Higgs mass via RT-at-root-of-unity. Tests N = 2..12 "
            "at substrate q_0 and at roots of unity exp(2πi/N), "
            "exp(2πi/(N+2)). Mass-scale candidates: |J_N|·m_e, log|J_N|·m_e, "
            "etc. Compares to actual m_H/m_e ≈ 244811."
        ),
        "parameters": {
            "precision": "mpfr",
            "dps": 50,
            "Q_0": str(Q_0),
            "torus_link": "T(2, 8) = Higgs per electroweak-higgs-torus-link-triplet.md",
            "n_torus": n_torus,
            "N_color_range": N_values,
            "m_higgs_target_MeV": float(M_HIGGS_MEV),
            "m_higgs_over_m_e": float(M_H_OVER_M_E),
        },
        "results": results,
        "best_candidate": best_info,
        "interpretation": (
            "Exploratory first look at RT-at-root-of-unity for Higgs mass. "
            "Looks for structurally-derivable scales matching m_H. The "
            "best ratio found is reported above; if within order-of-"
            "magnitude of unity, the corresponding (N, q) combination "
            "warrants deeper investigation. If far from unity across all "
            "tested combinations, the RT chain likely needs additional "
            "categorical structure (e.g., per-shell Geom evaluation, "
            "Chern-Simons partition function, or quantum-group level-k "
            "tensoring with the matter charge sector)."
        ),
        "status": "exploratory",
        "tags": [
            "rt-route",
            "colored-jones",
            "root-of-unity",
            "higgs",
            "T28",
            "torus-knot-mass",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "pentagon-rt-torus-knot-higgs-probe.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
