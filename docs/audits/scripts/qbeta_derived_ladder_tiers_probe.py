"""Q_β is derived, not fitted — the honest tier map of the ladder.

Directive: "derive Q_β". Answer: it already IS derived, cleanly, to
1.28 ppm — and (unlike the m_p Habiro tower dropped in PR #3280) every
step is a derived or proved categorical object, with NO CODATA fit.

Self-contained (docs/audits/scripts convention): all constants inlined
with provenance; no repo imports.

The production ladder (computations/derived_masses.py::
q_beta_kashiwara_n2_mev), factored into its tiers:

    Q_A   = m_e·|q²−2q−1|(q+1)/(2q³)          DERIVED  (prop:neutron-qvalue-symbolic)
    Q_N1  = Q_A·cos(α − b·ℏ_q²/2)             DERIVED  (c_1 = b, Kashiwara edge weight;
                                                        α, b from Hoefsmit/crystal data)
    Q_N2  = Q_N1·(1 − b²·ℏ_q⁴) = Q_N1·(1−u²)  PROVED   (c_2 = −1,
                                                        prop:q-beta-c-2-eq-neg-one-structural)

    with h = q−q⁻¹, ℏ_q = (q−1)/q, z = 1/(√q+1/√q), α = (z−1)h/2,
    b = √(1 − q²/(q²+1)²) = Hoefsmit b, u = b·ℏ_q² ≈ 0.00852.

Tier ladder at q₀ (proton pin):

    Q_A   → +1677.6 ppm   (derived base)
    Q_N1  → +73.8 ppm     (× derived c_1 = b)
    Q_N2  → +1.28 ppm     (× PROVED c_2 = −1)          ← production stops here

The NEXT order c_3 = −2 = J_Hopf(q=1) is a near-match (recovered to 3 ppm
by the proved O(u₀²) bias-correction identity, q-beta-c-k-leading-bias-
correction-identity-proof), NOT a clean derivation: it is the SETTLED,
s5bb-gated frontier (6-entry flip-flop history in docs/coordination/
1ppq-qbeta.md; PR #1580 settled it as non-wireable). This probe does NOT
re-attempt it — per the AGENTS.md anti-flip-flop discipline.

Contrast with m_p (PR #3280): the m_p `(1+46u⁴)…` tower was a CODATA fit
(c₄ affine in the q₀ pin, 0→46) and was dropped. Q_β has no such fit —
its 1.28 ppm is the honest derived value; it misses the L2 100× target
(7.8 ppb) by ~164× because the derivation stops at the proved c_2, not
because anything was removed.

Exit 0.
"""

from __future__ import annotations

import sys
from pathlib import Path

from mpmath import cos, mp, mpf, nstr, sqrt

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "computations" / "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Inlined constants (provenance): repo experimental_constants / codata_constants,
# verbatim (M_E_MEV, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION, Q_50_DIGIT_STR).
M_E = mpf("0.51099895069")            # m_e (MeV)
M_N = mpf("939.56542052")             # M_N_MEV_VALIDATION
M_P = mpf("938.27208816")             # M_P_MEV_VALIDATION
# proton-pinned q₀ (documented raw proton pin; canonical source
# qou_substrate.constants.Q_50_DIGIT_STR, mirrored by q_parameter shims).
Q0 = mpf("1.1099785827513808075916690956107688798744991218736")

with mp.workdps(50):
    Q_CODATA = +(M_N - M_P - M_E)


def q_A(q):
    """Derived base — prop:neutron-qvalue-symbolic."""
    return M_E * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def ladder(q):
    h = q - 1 / q
    z = 1 / (sqrt(q) + 1 / sqrt(q))
    hbar = (q - 1) / q
    alpha = (z - 1) * h / 2
    b = sqrt(1 - q ** 2 / (q ** 2 + 1) ** 2)          # Hoefsmit b
    u = b * hbar ** 2
    QA = q_A(q)
    QN1 = QA * cos(alpha - b * hbar ** 2 / 2)          # × derived c_1 = b
    QN2 = QN1 * (1 - u ** 2)                            # × PROVED c_2 = −1
    return QA, QN1, QN2, b, u


def main():
    QA, QN1, QN2, b, u = ladder(Q0)
    def ppm(x):
        return float((x / Q_CODATA - 1) * 1e6)

    rows = [
        ("Q_A   base", "derived", "prop:neutron-qvalue-symbolic", QA),
        ("Q_N1  × c_1=b", "derived", "Kashiwara edge weight (Hoefsmit b)", QN1),
        ("Q_N2  × c_2=−1", "PROVED", "prop:q-beta-c-2-eq-neg-one-structural", QN2),
    ]

    print("=" * 72)
    print("Q_β is DERIVED (not fitted) — honest tier map")
    print("=" * 72)
    print(f"q₀ = {nstr(Q0, 16)}   Q_β CODATA = {nstr(Q_CODATA, 12)} MeV")
    print(f"u = b·ℏ_q² = {nstr(u, 8)}   (u² = {nstr(u ** 2, 6)})")
    print()
    print(f"{'step':16s} {'tier':8s} {'Q_β err':>12s}   provenance")
    for name, tier, prov, val in rows:
        print(f"{name:16s} {tier:8s} {ppm(val):>10.3f}ppm   {prov}")
    print()
    print("→ production stops at the PROVED c_2 = −1: Q_β = 1.28 ppm, fully")
    print("  derived (NO CODATA fit — contrast the m_p tower dropped in #3280).")
    print("  Next order c_3 = −2 = J_Hopf(q=1) is a near-match, s5bb-gated")
    print("  (settled non-wireable, PR #1580); NOT re-attempted here.")
    print()
    print(f"L2 100× target for Q_β = 7.8 ppb; derived value 1.28 ppm misses")
    print(f"  by ~{ppm(QN2) * 1000 / 7.8:.0f}× — because the derivation stops at the")
    print("  proved c_2, not because a fit was removed.")

    # sanity: each tier strictly improves and c_2 factor is exactly (1−u²)
    assert abs(ppm(QA)) > abs(ppm(QN1)) > abs(ppm(QN2)), "tiers must improve"
    assert abs((1 - u ** 2) - QN2 / QN1) < mpf(10) ** (-mp.dps + 8), "c_2 factor ≠ (1−u²)"
    print("\nchecks: tiers strictly improve ✓ ; c_2 factor = (1−u²) exact ✓")


if __name__ == "__main__":
    main()
