#!/usr/bin/env python3
"""
ξ_ℓ probe — Faddeev Φ_q tower vs symmetric (Rogers) Li_2^q tower.

Tests the Phase-4 obstruction's indicated resolution
(`content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md`
§"Two-constraint obstruction"): the symmetric Li_2^q tower gives
O(1) lepton mass ratios because Li_2^q(z) = Σ z^n/(n[n]_q) → Li_2(z)
as q→1 — NO 1/ℏ enhancement. The Faddeev quantum dilogarithm
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
    """log of the Faddeev / q-Pochhammer quantum dilogarithm
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


def main() -> int:
    mp.mp.dps = 50

    # Substrate at q_0 — muon-anchored canonical (same pin as the
    # per-generator-V-hat-general witness this probe extends).
    Vol_4_1 = mp.mpf("2.0298832128193072500115978049904475264466050157561096")
    cal2 = M_MU_OVER_M_E
    cal_tau = mp.mpf("3477.23")
    hbar_q_sq = Vol_4_1 / cal2
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)
    h = q0 - 1 / q0
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))
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

    print(f"{'lepton':24s} {'max|V̂|':>8s} {'(a)Li2q':>10s} {'(b)Φq':>11s} {'(c)logΦq':>11s}")
    print("-" * 70)
    for name, b in leptons.items():
        print(f"{name:24s} {b['maxV']:8.4f} {float(b['m_li2q']):10.4f} "
              f"{float(b['m_phi']):11.4f} {float(b['m_logphi']):11.4f}")
    print()

    e = leptons["electron σ_1³ T(2,3)"]
    print(f"{'ratio to electron':24s} {'CODATA':>10s} {'(a)Li2q':>10s} "
          f"{'(b)Φq':>11s} {'(c)logΦq':>11s}")
    print("-" * 78)
    out_ratios = {}
    for name in ["muon T(2,5) σ_1⁵", "muon 4_1 (σ_1σ_2⁻¹)²", "tau T(2,7) σ_1⁷"]:
        b = leptons[name]
        cod = cal2 if "muon" in name else cal_tau
        r_li2q = b["m_li2q"] / e["m_li2q"]
        r_phi = b["m_phi"] / e["m_phi"]
        r_logphi = b["m_logphi"] / e["m_logphi"]
        print(f"{name:24s} {float(cod):10.2f} {float(r_li2q):10.4f} "
              f"{float(r_phi):11.4f} {float(r_logphi):11.4f}")
        out_ratios[name] = {
            "codata": str(cod),
            "ratio_li2q_sym": str(r_li2q),
            "ratio_phi_direct": str(r_phi),
            "ratio_log_phi": str(r_logphi),
        }
    print()
    print("=== Reading ===")
    print("(a) symmetric Li_2^q: O(1) ratios — reproduces the Phase-4 obstruction.")
    print("(b)/(c) Faddeev Φ_q: 1/ℏ enhancement near the convergence radius |V̂|→q_0.")
    print("    If (b) or (c) ratios approach CODATA → Faddeev Φ_q is the C2 fix;")
    print("    if still far → the missing structure is elsewhere (honest negative).")

    witness = {
        "description": "ξ_ℓ Faddeev Φ_q vs symmetric Li_2^q per-braid tower probe (proper Wedderburn V̂_i)",
        "computation": "xi_ell_faddeev_phi_q_probe",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "tests": "lepton-mass-tower-canonical.md §Two-constraint obstruction (Phase 4)",
            "hypothesis": "Faddeev Φ_q (log Φ_q ~ Li_2/ℏ) supplies the ~100× the symmetric Li_2^q tower lacks while staying nonzero on torus knots",
            "V_hat_source": "per_generator_V_hat_general (proper Plancherel Wedderburn, NOT crude |tr_M|^(1/n))",
            "q0_pin": "muon-anchored canonical (matches per-generator-V-hat-general.witness.json)",
        },
        "constants": {"q_0": str(q0), "hbar_q": str(hbar_q),
                      "inv_hbar_q_sq": str(1 / hbar_q_sq), "z": str(z)},
        "leptons": {
            name: {
                "V_hat": [str(v) for v in b["V"]],
                "max_abs_V": b["maxV"],
                "m_li2q_sym": str(b["m_li2q"]),
                "m_phi_direct": str(b["m_phi"]),
                "m_log_phi": str(b["m_logphi"]),
            } for name, b in leptons.items()
        },
        "ratios_to_electron": out_ratios,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "xi-ell-faddeev-phi-q-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
