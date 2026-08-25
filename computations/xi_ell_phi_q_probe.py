#!/usr/bin/env python3
"""
ξ_ℓ probe — compact q-dilog Φ_q tower vs symmetric (Rogers) Li_2^q tower.

Tests the Phase-4 obstruction's indicated resolution
(`content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md`
§"Two-constraint obstruction"): the symmetric Li_2^q tower gives
O(1) lepton mass ratios because Li_2^q(z) = Σ z^n/(n[n]_q) → Li_2(z)
as q→1 — NO 1/ℏ enhancement. The compact quantum dilogarithm
(q-Pochhammer) Φ_q(z) = ∏_{k≥1}(1 - q^{-k} z)^{-1} has
log Φ_q ~ Li_2/ℏ, an O(1/ℏ) enhancement, so its tower can in
principle supply the ~100× the ratios are missing while staying
nonzero on torus knots (electron T(2,3), tau T(2,7)).

This swaps Li_2^q → Φ_q in the per-braid mass tower using the SAME
proper Plancherel-weighted Wedderburn V̂_i as
`per_generator_V_hat_general.py` (NOT the crude |tr_M|^(1/n)
placeholder). Three tower variants are reported side by side so the
effect of the dilog choice is visible and honest:

  (a) symmetric Li_2^q  (the form the existing probes used)
        m = Σ_i  −Li_2^q(−|V̂_i|)  + z² Σ_{i<j} −Li_2^q(−|V̂_i V̂_j|)
  (b) Φ_q direct  (per-braid-mass-tower.md literal form, Φ_q(0)=1)
        m = |∏ V̂_i| + Σ_i Φ_q(|V̂_i|) + z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)
  (c) log Φ_q  (additive 1/ℏ-enhanced analog of (a))
        m = Σ_i  log Φ_q(|V̂_i|) + z² Σ_{i<j} log Φ_q(|V̂_i V̂_j|)

CODATA targets: m_μ/m_e = 206.7683, m_τ/m_e = 3477.23. No coupling
is tuned — this is a falsification probe of a fixed structural
formula, reporting whatever ratios result.

Audit-only; no production wiring.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from per_generator_V_hat_general import per_generator_V_hat_general  # noqa: E402
from _precision import str_at_true_precision  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def li2q_sym(z_arg: mp.mpf, q: mp.mpf, max_terms: int = 600) -> mp.mpf:
    """Symmetric (Rogers) q-dilog Li_2^q(z) = Σ z^n / (n·[n]_q),
    [n]_q = (q^n - q^{-n})/(q - q^{-1}). → Li_2(z) as q→1 (no 1/ℏ)."""
    h = q - 1 / q
    s = mp.mpf(0)
    for n in range(1, max_terms + 1):
        qn = (q ** n - q ** (-n)) / h
        t = z_arg ** n / (n * qn)
        s += t
        if mp.fabs(t) < mp.mpf(10) ** (-55):
            break
    return s


def log_phi_q(z_arg: mp.mpf, q: mp.mpf, max_k: int = 100000) -> mp.mpf:
    """log of the compact (q-Pochhammer) quantum dilogarithm — legacy "Faddeev" mislabel corrected
    Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}, i.e.
        log Φ_q(z) = − Σ_{k≥1} log(1 - q^{-k} z).
    Converges for |z| < q (q^{-k} z → 0 geometrically).
    As q→1, log Φ_q(z) ~ Li_2(z)/ℏ — the O(1/ℏ) enhancement."""
    s = mp.mpf(0)
    qi = 1 / q
    term = qi  # q^{-1}
    for k in range(1, max_k + 1):
        x = term * z_arg          # q^{-k} z
        s += -mp.log(1 - x)
        term *= qi                # q^{-(k+1)}
        if mp.fabs(x) < mp.mpf(10) ** (-55):
            break
    return s


def phi_q(z_arg: mp.mpf, q: mp.mpf) -> mp.mpf:
    return mp.e ** log_phi_q(z_arg, q)


def tower_li2q(V: list[mp.mpf], q: mp.mpf, z: mp.mpf) -> mp.mpf:
    """(a) symmetric-Li_2^q tower (descended-dropped)."""
    n = len(V)
    s = sum(-li2q_sym(-mp.fabs(v), q) for v in V)
    for i in range(n):
        for j in range(i + 1, n):
            s += -z * z * li2q_sym(-mp.fabs(V[i] * V[j]), q)
    return s


def tower_phi_direct(V: list[mp.mpf], q: mp.mpf, z: mp.mpf) -> mp.mpf:
    """(b) Φ_q-direct tower (per-braid-mass-tower.md literal, descended
    term |∏V̂_i| included; Φ_q(0)=1 so each generator carries a unit
    offset)."""
    n = len(V)
    prod = mp.mpf(1)
    for v in V:
        prod *= mp.fabs(v)
    s = prod
    for v in V:
        s += phi_q(mp.fabs(v), q)
    for i in range(n):
        for j in range(i + 1, n):
            s += z * z * phi_q(mp.fabs(V[i] * V[j]), q)
    return s


def tower_log_phi(V: list[mp.mpf], q: mp.mpf, z: mp.mpf) -> mp.mpf:
    """(c) log-Φ_q tower — the additive 1/ℏ-enhanced analog of (a)."""
    n = len(V)
    s = sum(log_phi_q(mp.fabs(v), q) for v in V)
    for i in range(n):
        for j in range(i + 1, n):
            s += z * z * log_phi_q(mp.fabs(V[i] * V[j]), q)
    return s


def tower_phi_rescaled(V: list[mp.mpf], q: mp.mpf, z: mp.mpf) -> mp.mpf:
    """(d) Φ_q-direct on the RESCALED argument V̂/q_0. Motivation: the
    near-singular muon-4_1 behaviour in (b) (V̂≈1.009 sitting ON the
    radius q_0) says Φ_q should act on a normalised argument bounded
    well inside the disk. V̂/q_0 ∈ [0,1) for all leptons here."""
    n = len(V)
    Vr = [mp.fabs(v) / q for v in V]
    prod = mp.mpf(1)
    for v in Vr:
        prod *= v
    s = prod
    for v in Vr:
        s += phi_q(v, q)
    for i in range(n):
        for j in range(i + 1, n):
            s += z * z * phi_q(Vr[i] * Vr[j], q)
    return s


def tower_log_phi_rescaled(V: list[mp.mpf], q: mp.mpf, z: mp.mpf) -> mp.mpf:
    """(e) log-Φ_q on the rescaled argument V̂/q_0 (descended-dropped)."""
    n = len(V)
    Vr = [mp.fabs(v) / q for v in V]
    s = sum(log_phi_q(v, q) for v in Vr)
    for i in range(n):
        for j in range(i + 1, n):
            s += z * z * log_phi_q(Vr[i] * Vr[j], q)
    return s


def main() -> int:
    set_compute_dps()

    # Substrate at q_0 — muon-anchored canonical (same pin as the
    # per-generator-V-hat-general witness this probe extends).
    # Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 53 digits, correct to 19 (qou-ckbv)
    Vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)
    cal2 = M_MU_OVER_M_E
    cal_tau = mp.mpf("3477.23")
    hbar_q_sq = Vol_4_1 / cal2
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)
    h = q0 - 1 / q0
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1).  Was z_C = 1/(sqrt q + 1/sqrt q), excised.
    z = q0 ** 3 / (q0 ** 2 + 1)
    h_f = float(h)

    print(f"=== Substrate: q_0 = {float(q0):.10f}, ℏ_q = {float(hbar_q):.6f}, "
          f"1/ℏ_q² = {float(1/hbar_q_sq):.4f} ===\n")

    leptons = {
        "electron σ_1³ T(2,3)":  {"n": 2, "word": [(1.0, 0.0, 0)] * 3},
        "muon T(2,5) σ_1⁵":      {"n": 2, "word": [(1.0, 0.0, 0)] * 5},
        "muon 4_1 (σ_1σ_2⁻¹)²":  {"n": 3, "word": [(1.0, 0.0, 0), (1.0, -h_f, 1),
                                                    (1.0, 0.0, 0), (1.0, -h_f, 1)]},
        "tau T(2,7) σ_1⁷":       {"n": 2, "word": [(1.0, 0.0, 0)] * 7},
    }

    # Proper Plancherel-weighted Wedderburn V̂_i (reused machinery)
    for name, b in leptons.items():
        Vd = per_generator_V_hat_general(b["n"], b["word"])
        b["V"] = [mp.mpf(d["full"]) for d in Vd]
        b["maxV"] = float(max((abs(float(v)) for v in b["V"]), default=0))
        b["m_li2q"] = tower_li2q(b["V"], q0, z)
        b["m_phi"] = tower_phi_direct(b["V"], q0, z)
        b["m_logphi"] = tower_log_phi(b["V"], q0, z)
        b["m_phi_rs"] = tower_phi_rescaled(b["V"], q0, z)
        b["m_logphi_rs"] = tower_log_phi_rescaled(b["V"], q0, z)

    e = leptons["electron σ_1³ T(2,3)"]
    print(f"{'ratio to electron':24s} {'CODATA':>9s} {'(a)Li2q':>8s} "
          f"{'(b)Φq':>10s} {'(c)logΦq':>9s} {'(d)Φq/q0':>10s} {'(e)logΦq/q0':>11s}")
    print("-" * 86)
    out_ratios = {}
    for name in ["muon T(2,5) σ_1⁵", "muon 4_1 (σ_1σ_2⁻¹)²", "tau T(2,7) σ_1⁷"]:
        b = leptons[name]
        cod = cal2 if "muon" in name else cal_tau
        r = {
            "li2q": b["m_li2q"] / e["m_li2q"],
            "phi": b["m_phi"] / e["m_phi"],
            "logphi": b["m_logphi"] / e["m_logphi"],
            "phi_rs": b["m_phi_rs"] / e["m_phi_rs"],
            "logphi_rs": b["m_logphi_rs"] / e["m_logphi_rs"],
        }
        print(f"{name:24s} {float(cod):9.2f} {float(r['li2q']):8.3f} "
              f"{float(r['phi']):10.3f} {float(r['logphi']):9.3f} "
              f"{float(r['phi_rs']):10.3f} {float(r['logphi_rs']):11.3f}")
        out_ratios[name] = {
            "codata": str(cod),
            "ratio_li2q_sym": str(r["li2q"]),
            "ratio_phi_direct": str(r["phi"]),
            "ratio_log_phi": str(r["logphi"]),
            "ratio_phi_rescaled": str(r["phi_rs"]),
            "ratio_log_phi_rescaled": str(r["logphi_rs"]),
        }
    print()
    print("=== Reading ===")
    print("(a) symmetric Li_2^q: O(1) ratios — reproduces the Phase-4 obstruction.")
    print("(b)/(c) compact q-dilog Φ_q bare arg: 1/ℏ enhancement; (b) overshoots knot-sensitively.")
    print("(d)/(e) Φ_q on rescaled arg V̂/q_0: tames the near-radius singularity.")
    print("    Closest-to-CODATA column = the candidate normalization (honest report).")

    witness = {
        "description": "ξ_ℓ compact q-dilog Φ_q vs symmetric Li_2^q per-braid tower probe (proper Wedderburn V̂_i)",
        "computation": "xi_ell_phi_q_probe",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "tests": "lepton-mass-tower-canonical.md §Two-constraint obstruction (Phase 4)",
            "hypothesis": "compact q-dilog Φ_q (log Φ_q ~ Li_2/ℏ) supplies the ~100× the symmetric Li_2^q tower lacks while staying nonzero on torus knots",
            "V_hat_source": "per_generator_V_hat_general (proper Plancherel Wedderburn, NOT crude |tr_M|^(1/n))",
            "q0_pin": "muon-anchored canonical (matches per-generator-V-hat-general.witness.json)",
        },
        "constants": {"q_0": str(q0), "hbar_q": str(hbar_q),
                      "inv_hbar_q_sq": str(1 / hbar_q_sq), "z": str(z)},
        "leptons": {
            name: {
                # V̂ comes from per_generator_V_hat_general, which computes in
                # float (the braid words above carry float literals), so each
                # entry is a 53-bit value promoted by mpf(d["full"]).
                "V_hat": [str_at_true_precision(v) for v in b["V"]],
                "max_abs_V": b["maxV"],
                "m_li2q_sym": str(b["m_li2q"]),
                "m_phi_direct": str(b["m_phi"]),
                "m_log_phi": str(b["m_logphi"]),
            } for name, b in leptons.items()
        },
        "ratios_to_electron": out_ratios,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "xi-ell-phi-q-probe.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
