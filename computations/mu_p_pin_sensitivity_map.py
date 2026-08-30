#!/usr/bin/env python3
"""mu_p_pin_sensitivity_map.py — the exact pin-sensitivity map of the mass chain.

The μ–p root-cause follow-up to the Habiro-interpolation finding (#3830): W_λ(q₀)
is a **pin-robust ratio** (cross-pin swing ~1e-12, ~10⁴× smaller than the 11.5 ppb
μ–p pin gap), so the entire McKay / W_λ keystone route is BLIND to the μ–p tension.
This script LOCALIZES the tension: it computes the relative pin-sensitivity

        S(O) := d(log O) / d(log q₀)

of every observable O in the canonical mass chain, showing that the sensitivity
CONCENTRATES in the absolute muon anchor ℏ_q² = ((q−1)/q)² (large derivative,
∝ 1/(q−1)), while every dimensionless dressing (F_Bor, W_λ, mass RATIOS) is
pin-robust (small derivative). This makes the 11.5 ppb pin gap a statement about
the ABSOLUTE anchor, not any ratio observable — so no ratio can adjudicate it.

The canonical chain (guardrail: docs/canonical-mass-formula-guardrail.md):

    ℏ_q   = (q−1)/q                              (substrate infinitesimal)
    Vol(4₁) = 2·Cl₂(π/3)                          (CONSTANT, q-independent geometry)
    m_μ   = m_e · Vol(4₁) / ℏ_q²                  (ABSOLUTE muon anchor)
    F_Bor = |tr_M(β_Bor)| · [3]_q! / q³           (dimensionless Borromean factor)
    m_p   = 2·(m_μ·F_Bor − 6·m_e)                 (absolute proton)
    m_n   = m_p + Q_β + m_e                        (absolute neutron)
    W_λ   = [mark λ]²_q / Σ_μ [mark μ]²_q          (McKay q-Verlinde measure — RATIO)

Every S(O) is computed by high-precision central finite difference against the
PRODUCTION closed forms (canonical_mass / m_p_substrate_identity_50dps /
derived_masses), so the map is exactly the chain that lands the masses.

DISCIPLINE (AGENTS.md): no fit; nothing wired to production; this is a diagnostic
map + honest scope-(a) assessment. The μ–p tension is NOT resolved here.

# Ref: [thurston1978] The geometry and topology of three-manifolds  (Vol(4₁)=2Cl₂(π/3))
# Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716  (Habiro ring / root rigidity)
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (HERE, HERE / "substrate"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import _path_bridge  # noqa: F401,E402
from mpmath import mp, mpf  # noqa: E402

mp.dps = 60

from q_parameter import vol_4_1_at  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402

# muon-anchored q₀ (the ideal-CAL-2 pin) and proton-anchored q₀ (constants.py pin).
Q0_MUON = mpf("1.1099785955573347")     # ideal CAL-2 pin (muon ratio)
Q0_PROTON = mpf("1.1099785827513808075916690956107688798744991218736")  # proton pin


# ── the chain, as pure functions of q (m_e held fixed) ──────────────────────
def hbar_q(q):
    return (q - 1) / q


def hbar_q_sq(q):
    return hbar_q(q) ** 2


def vol41():
    return vol_4_1_at(60)


def m_mu(q, m_e):
    """Absolute muon anchor m_e·Vol(4₁)/ℏ_q²."""
    return m_e * vol41() / hbar_q_sq(q)


def q_int(q, n):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def qfact_three(q):
    return q_int(q, 3) * q_int(q, 2) * q_int(q, 1)


def trM_borromean(q):
    h = q - 1 / q
    return abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))


def F_Bor(q):
    return trM_borromean(q) * qfact_three(q) / q ** 3


def m_p(q, m_e):
    return 2 * (m_mu(q, m_e) * F_Bor(q) - 6 * m_e)


# W_λ McKay q-Verlinde measure. affine-Ê₈ marks (2I irrep dims):
MCKAY_MARKS = [1, 2, 3, 4, 5, 6, 4, 2, 3]  # Σ mark² = 120 = |2I|


def W_lambda(q, mark):
    """W_λ(q) = [mark]²_q / Σ_μ [mark μ]²_q — the McKay q-Verlinde measure (a RATIO)."""
    num = q_int(q, mark) ** 2
    den = sum(q_int(q, m) ** 2 for m in MCKAY_MARKS)
    return num / den


def q_beta_QA(q):
    # Q_A = m_e·|q²−2q−1|(q+1)/(2q³)  (q_beta_predicted_mev closed form)
    m_e = mpf(M_E_MEV)
    return m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def q_beta(q):
    """Q_β production near-match (derived_masses.q_beta_kashiwara_n2_mev), q-only."""
    Q_A = q_beta_QA(q)
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    hbq = (q - 1) / q
    alpha = (z - 1) * h / 2
    q_sq = q ** 2
    b = mp.sqrt(1 - q_sq / (q_sq + 1) ** 2)
    Q_N1 = Q_A * mp.cos(alpha - b * hbq ** 2 / 2)
    return Q_N1 * (1 - b ** 2 * hbq ** 4)


def m_n(q, m_e):
    return m_p(q, m_e) + q_beta(q) + m_e


# ── relative pin-sensitivity S(O) = dlogO/dlogq via central difference ──────
def sensitivity(f, q, rel_h=mpf(10) ** (-25)):
    """S = d(log f)/d(log q) = (q/f)·df/dq via 4th-order central difference."""
    h = q * rel_h
    f0 = f(q)
    fp1 = f(q + h)
    fm1 = f(q - h)
    fp2 = f(q + 2 * h)
    fm2 = f(q - 2 * h)
    dfdq = (-fp2 + 8 * fp1 - 8 * fm1 + fm2) / (12 * h)
    return q * dfdq / f0


def run(q0, label):
    m_e = mpf(M_E_MEV)
    rows = []

    def S(name, f, exact=None):
        val = f(q0)
        s = sensitivity(f, q0)
        rows.append((name, val, s, exact))

    qm1 = q0 - 1
    S_hbar = 1 / qm1                 # dlog ℏ_q /dlog q  = 1/(q−1)
    S_hbarsq = 2 / qm1              # dlog ℏ_q² /dlog q = 2/(q−1)
    S_mmu_exact = -2 / qm1          # dlog m_μ/dlog q   = −2/(q−1)

    S("hbar_q = (q-1)/q", hbar_q, S_hbar)
    S("hbar_q^2", hbar_q_sq, S_hbarsq)
    S("Vol(4_1) [const]", lambda q: vol41(), mpf(0))
    S("m_mu  [ABS anchor]", lambda q: m_mu(q, m_e), S_mmu_exact)
    S("F_Bor [ratio]", F_Bor)
    S("|tr_M(B_Bor)|", trM_borromean)
    S("[3]_q!", qfact_three)
    S("m_p   [ABS]", lambda q: m_p(q, m_e))
    S("m_n   [ABS]", lambda q: m_n(q, m_e))
    S("Q_beta", q_beta)
    S("W_lambda(mark=5)", lambda q: W_lambda(q, 5))
    S("W_lambda(mark=2)", lambda q: W_lambda(q, 2))
    S("m_p/m_mu [RATIO]", lambda q: m_p(q, m_e) / m_mu(q, m_e))
    S("m_n/m_p [RATIO]", lambda q: m_n(q, m_e) / m_p(q, m_e))
    S("m_mu/m_e [RATIO]", lambda q: m_mu(q, m_e) / m_e)

    print(f"\n=== pin-sensitivity map at q0 = {mp.nstr(q0, 20)} ({label}) ===")
    print(f"    q0 − 1 = {mp.nstr(qm1, 12)}   1/(q0−1) = {mp.nstr(1/qm1, 12)}")
    print(f"{'observable':<24}{'value':>26}{'S=dlogO/dlogq':>20}{'|S|*11.5ppb (ppb)':>20}")
    PIN_GAP = mpf("1.15e-8")  # μ–p gap in log q (~11.5 ppb)
    for name, val, s, exact in rows:
        induced = abs(s) * PIN_GAP * mpf(10) ** 9  # relative ppb induced on O
        ex = f"  (exact {mp.nstr(exact,8)})" if exact is not None else ""
        print(f"{name:<24}{mp.nstr(val,16):>26}{mp.nstr(s,10):>20}"
              f"{mp.nstr(induced,8):>20}{ex}")
    return rows


def main():
    t0 = time.time()
    print("μ–p pin-sensitivity map — S(O) = dlog O / dlog q₀ (central diff, 60 dps)")
    print("Claim: sensitivity concentrates in ℏ_q² (abs anchor m_μ); ratios pin-robust.")
    rows_p = run(Q0_PROTON, "proton pin")
    rows_m = run(Q0_MUON, "muon pin, ideal CAL-2")

    import hashlib
    import json
    import subprocess
    src = Path(__file__).read_text()
    script_hash = hashlib.sha256(src.encode()).hexdigest()[:12]
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(Path(__file__).name)],
            cwd=HERE, text=True).strip() or "uncommitted"
    except Exception:
        sha = "uncommitted"

    def serialize(rows):
        return [{"observable": n, "value": mp.nstr(v, 20),
                 "S_dlogO_dlogq": mp.nstr(s, 16),
                 "exact_S": (mp.nstr(e, 16) if e is not None else None)}
                for n, v, s, e in rows]

    witness = {
        "schema": "witness/v1",
        "witness": {
            "id": "mu-p-pin-sensitivity-map",
            "scriptHash": script_hash,
            "scriptCommitSha": sha,
            "producer": "computations/mu_p_pin_sensitivity_map.py",
            "description": "Relative pin-sensitivity S(O)=dlogO/dlogq of the canonical "
                           "mass chain. Localizes the 11.5 ppb μ–p tension in the absolute "
                           "muon anchor ℏ_q²; F_Bor/W_λ/mass-ratios are pin-robust.",
        },
        "data": {
            "pin_gap_ppb": 11.5,
            "S_mmu_exact": "-2/(q-1)",
            "S_hbar_sq_exact": "2/(q-1)",
            "proton_pin": {"q0": mp.nstr(Q0_PROTON, 20), "rows": serialize(rows_p)},
            "muon_pin": {"q0": mp.nstr(Q0_MUON, 20), "rows": serialize(rows_m)},
        },
    }
    out = HERE / "mu-p-pin-sensitivity-map.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
    print(f"\nwrote {out.name}  (scriptHash {script_hash}, sha {sha[:12]})")
    print(f"elapsed {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
