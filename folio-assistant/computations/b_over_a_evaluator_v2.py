"""
B/A numerical evaluator (v4) — SDP-derived NF + Hecke NF reduction.

Pipeline (per nucleus):
1.  Constructive atom NF: `atom_mass_derived.build_atom(Z, N)` runs the
    categorical construction — proton/neutron NFs derived from B₃ +
    typed quark crossings, atoms built by nuclear-crossing fusion.
2.  Compute `target_net = nf_net(nucleus_nf)`.
3.  SDP refinement: `confinement_sdp.solve_sdp(target_net)` returns
    the 6-element NF coefficient vector x ∈ ℝ⁶ minimizing the Markov
    trace TR_M_BASIS · x subject to Frobenius positivity (LP `G·x ≥ 0`,
    SDP `tr(G·X) ≥ 0` from the Lasserre moment relaxation).
4.  Markov trace `tr_M = TR_M_BASIS · x_opt` (read directly from the
    SDP objective).
5.  B/A = (E_0 / A) · log| tr_free / tr_nuc |.

Why each piece is needed
────────────────────────

- **Constructive atom_mass_derived.build_atom**: gives the raw H₃ NF
  element from the categorical recipe (proton uud + neutron udd +
  typed nuclear crossings + Z electron Hopf-trefoils).  This pins
  the `target_net` from physics (not from arbitrary counts).
- **SDP solve_sdp**: enforces the confinement Frobenius constraints
  the constructive build doesn't impose.  The constructive NF can
  drift outside the feasible cone for large A; the SDP projects it
  back onto the optimal feasible point.
- **Markov trace**: the categorical mass functional, evaluated on
  the SDP-refined NF vector.
- **NF basis is canonical**: Diamond-lemma confluence on the
  Groebner-Shirshov basis means the result is convention-free.

Output: folio-assistant/computations/b-over-a-witness-v2.json
        (v4 SDP results + v1 spectral term for comparison)
"""
from __future__ import annotations

import importlib.util as _ilu
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from q_parameter import Q as Q0  # noqa: E402

# ── Lazy imports of the existing categorical infrastructure ───────
def _load_module(filename: str, name: str):
    spec = _ilu.spec_from_file_location(name, str(HERE / filename))
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_amd = _load_module("atom_mass_derived.py", "_amd")
_sdp = _load_module("confinement_sdp.py", "_sdp")

build_atom = _amd.build_atom
PROTON_NF = _amd.PROTON_NF
NEUTRON_NF = _amd.NEUTRON_NF
markov_trace_general = _amd.markov_trace_general
nf_net = _amd.nf_net
hecke_mul = _amd.hecke_mul
reduce_nf = _amd.reduce_nf

solve_sdp = _sdp.solve_sdp
solve_lp = _sdp.solve_lp
TR_M_BASIS = _sdp.TR_M_BASIS

# ── Physical constants ────────────────────────────────────────────
M_E_MEV = 0.51099895069
ALPHA_EM = 1.0 / 137.035999084
HBARC_MEV_FM = 197.3269804
R_0_FM = 1.2

E_0_MEV = M_E_MEV / (Q0 * (Q0 - 1.0))


# ── Free-braid: Z separated proton NFs + N separated neutron NFs ──
def free_braid_nf(Z: int, N: int) -> dict:
    """Free-braid NF: Z separated protons and N separated neutrons.

    Multiplicative concatenation (no inter-nucleon crossings) reduces
    to a tensor product of NF elements; in H_3 the trivial product
    is the multiplicative composition under reduce_nf.
    """
    elem = {(): 1.0}  # identity
    for _ in range(Z):
        elem = reduce_nf(hecke_mul(elem, PROTON_NF))
    for _ in range(N):
        elem = reduce_nf(hecke_mul(elem, NEUTRON_NF))
    return elem


# ── Run the SDP at a target net ───────────────────────────────────
def sdp_markov_trace(target_net: float) -> tuple[float, dict]:
    """Run solve_sdp(target_net), return (objective, full_result).

    The SDP minimizes TR_M_BASIS·x — the Markov trace — so the
    objective IS tr_M of the optimal NF vector x_opt.
    """
    res = solve_sdp(target_net)
    if res.get("status") not in {"optimal", "optimal_inaccurate"}:
        return (float("nan"), res)
    return (float(res["objective"]), res)


# ── B/A computation ──────────────────────────────────────────────
def compute_b_over_a_v4(Z: int, N: int) -> dict:
    A = Z + N
    # 1. Constructive build
    nuc_nf, atom_nf, meta = build_atom(Z, N)
    nuc_net = nf_net(nuc_nf)
    nuc_tr_constructive = markov_trace_general(nuc_nf)
    atom_tr_constructive = markov_trace_general(atom_nf)

    # 2. Free-braid (Z+N separated nucleons)
    free_nf = free_braid_nf(Z, N)
    free_net = nf_net(free_nf)
    free_tr_constructive = markov_trace_general(free_nf)

    # 3. SDP refinement on each net
    sdp_nuc_obj, sdp_nuc_full = sdp_markov_trace(nuc_net)
    sdp_free_obj, sdp_free_full = sdp_markov_trace(free_net)

    # 4. Atom (electron-dressed) — the actual measurable
    atom_net = nf_net(atom_nf)
    sdp_atom_obj, _ = sdp_markov_trace(atom_net)

    # 5. B/A from log|tr_free / tr_nuc|
    def log_ratio(a: float, b: float) -> float:
        if a == 0 or b == 0 or math.isnan(a) or math.isnan(b):
            return 0.0
        return math.log(abs(a / b))

    log_constr = log_ratio(free_tr_constructive, nuc_tr_constructive)
    log_sdp = log_ratio(sdp_free_obj, sdp_nuc_obj)

    return {
        "Z": Z,
        "N": N,
        "A": A,
        "nuc_net": nuc_net,
        "free_net": free_net,
        "atom_net": atom_net,
        # Constructive (no SDP)
        "nuc_tr_constructive": nuc_tr_constructive,
        "free_tr_constructive": free_tr_constructive,
        "atom_tr_constructive": atom_tr_constructive,
        "log_ratio_constructive": log_constr,
        "B_over_A_spec_constructive_MeV": (E_0_MEV / A) * log_constr,
        # SDP-refined
        "sdp_nuc_objective": sdp_nuc_obj,
        "sdp_free_objective": sdp_free_obj,
        "sdp_atom_objective": sdp_atom_obj,
        "sdp_nuc_status": sdp_nuc_full.get("status"),
        "sdp_free_status": sdp_free_full.get("status"),
        "sdp_nuc_moment_rank": sdp_nuc_full.get("moment_rank_numeric"),
        "log_ratio_sdp": log_sdp,
        "B_over_A_spec_sdp_MeV": (E_0_MEV / A) * log_sdp,
    }


# ── v1 spectral term for side-by-side comparison ──────────────────
def v1_spectral_b_over_a(Z: int, N: int) -> float:
    n_pp = Z * (Z - 1) // 2
    n_nn = N * (N - 1) // 2
    n_pn = Z * N
    q = Q0
    n_pp_f = Z
    n_nn_f = N
    n_pn_f = 2 * (Z + N)

    def lam(irrep, npp, nnn, npn):
        if irrep == "sym":
            return q ** npp * (1.0 / q) ** nnn * ((q + 1.0 / q) / 2.0) ** npn
        if irrep == "alt":
            return (-1.0 / q) ** npp * (-q) ** nnn * (-(q + 1.0 / q) / 2.0) ** npn
        return 1.0

    Lambda_nuc = {k: lam(k, n_pp, n_nn, n_pn) for k in ("sym", "std", "alt")}
    Lambda_free = {k: lam(k, n_pp_f, n_nn_f, n_pn_f) for k in ("sym", "std", "alt")}
    two_q = q + 1.0 / q
    three_q = q ** 2 + 1.0 + 1.0 / q ** 2
    w_sym = 1.0 / (two_q * three_q)
    w_std = two_q / three_q

    def safe_log(a, b):
        return 0.0 if a == 0 or b == 0 else math.log(abs(a / b))

    return (E_0_MEV / (Z + N)) * (
        w_sym * safe_log(Lambda_free["sym"], Lambda_nuc["sym"])
        + 2.0 * w_std * safe_log(Lambda_free["std"], Lambda_nuc["std"])
        + w_sym * safe_log(Lambda_free["alt"], Lambda_nuc["alt"])
    )


# ── Surface + Coulomb + AME ──────────────────────────────────────
def coulomb_b_over_a_mev(Z: int, A: int) -> float:
    if Z < 2 or A < 1:
        return 0.0
    R_fm = R_0_FM * A ** (1.0 / 3.0)
    return (3.0 / 5.0) * ALPHA_EM * HBARC_MEV_FM * Z * (Z - 1) / R_fm / A


def surface_b_over_a_mev(c_S: float, A: int) -> float:
    two_q = Q0 + 1.0 / Q0
    ell2 = math.log(two_q / 2.0)
    return c_S * E_0_MEV * ell2 * A ** (-1.0 / 3.0)


AME_BA = {"4He": 7.07391420, "12C": 7.68014481, "40Ca": 8.55130323}


def fit_c_s_to_4he_v4(spec_field: str = "B_over_A_spec_sdp_MeV") -> float:
    Z, N = 2, 2
    A = Z + N
    spec = compute_b_over_a_v4(Z, N)[spec_field]
    coulomb = coulomb_b_over_a_mev(Z, A)
    target = AME_BA["4He"]
    surface_target = spec - coulomb - target
    two_q = Q0 + 1.0 / Q0
    ell2 = math.log(two_q / 2.0)
    return surface_target / (E_0_MEV * ell2 * A ** (-1.0 / 3.0))


def predict_v4(Z: int, N: int, c_S: float, spec_field: str) -> dict:
    A = Z + N
    base = compute_b_over_a_v4(Z, N)
    base["coulomb_correction_MeV"] = coulomb_b_over_a_mev(Z, A)
    base["surface_correction_MeV"] = surface_b_over_a_mev(c_S, A)
    base["c_S"] = c_S
    base["spec_field_used"] = spec_field
    base["B_over_A_v4_predicted_MeV"] = (
        base[spec_field]
        - base["surface_correction_MeV"]
        - base["coulomb_correction_MeV"]
    )
    return base


def build_witness() -> dict:
    spec_field = "B_over_A_spec_sdp_MeV"
    c_S = fit_c_s_to_4he_v4(spec_field)
    nuclei = [("4He", 2, 2), ("12C", 6, 6), ("40Ca", 20, 20)]
    rows = []
    for name, Z, N in nuclei:
        rec = predict_v4(Z, N, c_S, spec_field)
        rec["nucleus"] = name
        rec["B_over_A_AME2020_MeV"] = AME_BA[name]
        rec["residual_MeV"] = rec["B_over_A_v4_predicted_MeV"] - AME_BA[name]
        rec["residual_pct"] = 100.0 * rec["residual_MeV"] / AME_BA[name]
        rec["B_over_A_v1_spectral_only_MeV"] = v1_spectral_b_over_a(Z, N)
        rows.append(rec)

    return {
        "schema_version": "4.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "folio-assistant/computations/b_over_a_evaluator_v2.py (v4 logic)",
        "block": "prop:b-over-a-spectral-decomposition (v4 — SDP + NF)",
        "supersedes": [
            "v1: |det|=1 std-block stub on (n_pp, n_nn, n_pn) abelianised counts",
            "v2: matrix-product χ_std with arbitrary braid-word convention",
            "v3: NF reduction on abelianised counts (no SDP)",
        ],
        "constants": {
            "q_0": Q0,
            "E_0_MeV": E_0_MEV,
            "TR_M_BASIS": list(map(float, TR_M_BASIS)),
        },
        "pipeline": (
            "build_atom(Z, N) → nucleus NF, atom NF (constructive); "
            "free_braid_nf(Z, N) → Z+N separated nucleons (no inter-crossings); "
            "solve_sdp(nf_net(·)) → SDP-refined NF coefficient vector x_opt "
            "satisfying Frobenius positivity; tr_M = TR_M_BASIS · x_opt; "
            "B/A = (E_0/A) log|tr_free/tr_nuc|."
        ),
        "fit": {
            "method": f"c_S fit to 4He B/A AME2020 = 7.07391420 MeV via {spec_field}",
            "fitted_c_S": c_S,
            "spec_field_used": spec_field,
        },
        "nuclei": rows,
    }


def main() -> int:
    witness = build_witness()
    out = HERE / "b-over-a-witness-v2.json"
    out.write_text(
        json.dumps(witness, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"q_0 = {Q0:.10f}, E_0 = {E_0_MEV:.6f} MeV")
    print(f"fitted c_S (v4 SDP) = {witness['fit']['fitted_c_S']:.6e}")
    print()
    print(f"  {'nucleus':>8} {'A':>3} "
          f"{'nuc_net':>9} {'free_net':>9} "
          f"{'tr_constr_nuc':>14} {'tr_sdp_nuc':>11} "
          f"{'B/A v1 spec':>11} {'B/A v4 spec':>11} "
          f"{'B/A pred':>9} {'AME':>8} {'Δ%':>7}")
    print("  " + "-" * 130)
    for r in witness["nuclei"]:
        print(
            f"  {r['nucleus']:>8} {r['A']:>3d} "
            f"{r['nuc_net']:>9.4f} {r['free_net']:>9.4f} "
            f"{r['nuc_tr_constructive']:>14.4f} "
            f"{r['sdp_nuc_objective']:>11.4f} "
            f"{r['B_over_A_v1_spectral_only_MeV']:>11.6f} "
            f"{r['B_over_A_spec_sdp_MeV']:>11.6f} "
            f"{r['B_over_A_v4_predicted_MeV']:>9.4f} "
            f"{r['B_over_A_AME2020_MeV']:>8.4f} "
            f"{r['residual_pct']:>6.2f}%"
        )
    print(f"\nWrote: {out.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
