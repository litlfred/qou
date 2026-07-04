"""c₄ ("46 u⁴") is the μ–p tension in disguise — a pin-dependence probe.

Task: "derive c₄ ≈ 46 at u⁴ on F_Bor categorically; if a categorical
derivation produces 46-exactly the μ–p tension closes parameter-free."

This probe answers it decisively, in the negative, at current substrate
precision, and quantifies WHY.

Setup (production m_p, computations/m_p_substrate_identity_50dps.py):

    F_Bor(q)      = |tr_M(β_Bor)| · [3]_q! / q³            (exact closed form)
    m_μ(q)        = m_e · Vol(4₁) / ℏ_q²                    (muon anchor formula)
    base(q)       = 2·m_μ·F_Bor − 12·m_e                    (3-term formula, N=0)
    u(q)          = b(q)·ℏ_q²,  b = √((q⁴+q²+1)/(q²+1)²)
    m_p(q)        = base · (1 + c₄u⁴)(1 + 4u⁵)(1 − 29u⁶)

`c₄` is the u⁴ coefficient production currently pins to 4143/90 ≈ 46.033
(comment: "derived geometrically from s5bb 5-manifold U(1) colour Reeb
index" — a route that is itself an honest-negative, see
docs/audits/2026-06-16-s5so3-reeb-resonance-probe-negative.md).

The probe solves for the *exact* c₄ that lands m_p on CODATA, as a
function of the q₀ pin, and shows:

  1. c₄ is EXACTLY LINEAR in the q₀ pin offset.
  2. c₄ = 0 at the proton pin (base already hits CODATA by construction).
  3. c₄ = 46.04 at the muon pin.
  4. slope ≈ 3.98 per ppb of q₀ over the 11.5 ppb muon↔proton window.

Conclusion: c₄ carries no categorical information. It equals
`slope · (q₀ − q₀^proton)`; the value "46" is exactly the choice to
calibrate on the muon rather than the proton — a convention, not a
derivation. Deriving "46 categorically" would require deriving q₀
itself (Subgoal-2, owner-declined) or the 11.5 ppb μ–p splitting.

Scope (AGENTS.md "before declaring refuted"): this is a scope-(a)
result — c₄, *as a fixed categorical constant*, is not derivable at
current precision. It does NOT structurally exclude a future closure
via a derived q₀ or a derived μ–p splitting.

Exit 0 + witness JSON.
"""

from __future__ import annotations

import json
from pathlib import Path

from mpmath import findroot, mp, mpf, nstr

mp.dps = 60

HERE = Path(__file__).resolve().parent
COMP = HERE.parent.parent.parent / "computations"
import sys

sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

from q_parameter import vol_4_1_at  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_MU_MEV_VALIDATION  # noqa: E402

M_E = mpf(M_E_MEV)
M_P = mpf(M_P_MEV_VALIDATION)
M_MU = mpf(M_MU_MEV_VALIDATION)

# production companion coefficients (held fixed; each is ~1e2/1e4× smaller
# than the u⁴ term so they do not affect the argument)
C5, C6 = mpf(4), mpf(-29)


def qint(q, n):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def base_and_u(q):
    h = q - 1 / q
    trM = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    F = trM * qint(q, 3) * qint(q, 2) * qint(q, 1) / q ** 3
    hbar2 = ((q - 1) / q) ** 2
    m_mu = M_E * vol_4_1_at(60) / hbar2
    b = ((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2) ** mpf("0.5")
    u = b * hbar2
    return 2 * m_mu * F - 12 * M_E, u


def exact_c4(q):
    base, u = base_and_u(q)
    comp = (1 + C5 * u ** 5) * (1 + C6 * u ** 6)
    return ((M_P / (base * comp)) - 1) / u ** 4


def main():
    # the two legitimate q₀ pins
    q_muon = findroot(
        lambda q: M_E * vol_4_1_at(60) / ((q - 1) / q) ** 2 - M_MU,
        mpf("1.10997859555733"),
    )
    q_proton = findroot(lambda q: base_and_u(q)[0] - M_P, mpf("1.109978"))
    ppb = lambda x: (x / q_proton - 1) * mpf(10) ** 9  # noqa: E731

    c4_muon = exact_c4(q_muon)
    c4_proton = exact_c4(q_proton)
    q_spread_ppb = (q_muon / q_proton - 1) * mpf(10) ** 9
    slope = c4_muon / q_spread_ppb  # per ppb

    # linearity check: sample the pin window
    samples = []
    max_nonlin = mpf(0)
    for k in range(11):
        t = mpf(k) / 10
        q = q_proton + (q_muon - q_proton) * t
        c4 = exact_c4(q)
        pred_linear = c4_proton + (c4_muon - c4_proton) * t
        nonlin = abs(c4 - pred_linear)
        max_nonlin = max(max_nonlin, nonlin)
        samples.append(
            {"t": float(t), "q_offset_ppb": float(ppb(q)), "c4": float(c4)}
        )

    # the candidate "closed forms" vs the exact muon-pin target.
    # NB the committed Q_50_DIGIT_STR is offset ~0.3 ppb from the exact muon
    # pin, so its own exact target (~45.74) is yet a THIRD value — reinforcing
    # that c₄ tracks the pin, not a categorical constant.
    candidates = {
        "46 (integer)": mpf(46),
        "4143/90 (production)": mpf(4143) / 90,
        "muon-pin target": c4_muon,
    }

    print("=" * 68)
    print("c₄ is the μ–p tension in disguise — pin-dependence probe")
    print("=" * 68)
    print(f"q_muon   = {nstr(q_muon, 18)}")
    print(f"q_proton = {nstr(q_proton, 18)}")
    print(f"μ↔p q₀ spread = {nstr(q_spread_ppb, 6)} ppb")
    print()
    print("exact c₄ required to land m_p on CODATA, vs q₀ pin:")
    print(f"  proton pin  → c₄ = {nstr(c4_proton, 10)}   (≈ 0: base hits CODATA)")
    print(f"  muon pin    → c₄ = {nstr(c4_muon, 10)}")
    print(f"  slope       = {nstr(slope, 6)} per ppb of q₀")
    print(f"  max deviation from linear across window = {nstr(max_nonlin, 4)}")
    print()
    print("candidate fixed 'closed forms' vs the exact muon-pin target:")
    for nm, c4 in candidates.items():
        print(f"  c₄={nm:14s} = {nstr(c4, 10):>14s}   Δ={nstr(c4 - c4_muon, 4)}")
    print()
    print("VERDICT (scope-a): c₄ carries no categorical information. It equals")
    print("slope·(q₀−q₀_proton); '46' is exactly the muon-pin selection — a")
    print("calibration convention, not a derivation. 4143/90 neither matches the")
    print("target nor has a derivation trail; its cited 'colour Reeb index' route")
    print("is an honest-negative (2026-06-16-s5so3-reeb-resonance-probe-negative).")

    witness = {
        "schema": "witness/v1",
        "id": "c4-mu-p-tension-pin-dependence",
        "description": (
            "c₄ ('46 u⁴' Habiro dressing on F_Bor) is the μ–p tension in "
            "disguise: exact c₄ is linear in the q₀ pin offset, = 0 at the "
            "proton pin, 46.04 at the muon pin, slope 3.98/ppb. No categorical "
            "constant; the value 46 is the muon-pin calibration choice."
        ),
        "verdict": (
            "scope-a: c₄ not derivable as a fixed categorical constant at "
            "current substrate precision (pin-dependent, sweeps 0→46). Does "
            "not structurally exclude closure via a derived q₀ or μ–p splitting."
        ),
        "data": {
            "q_muon": nstr(q_muon, 50),
            "q_proton": nstr(q_proton, 50),
            "mu_p_q0_spread_ppb": float(q_spread_ppb),
            "c4_at_proton_pin": float(c4_proton),
            "c4_at_muon_pin": float(c4_muon),
            "slope_c4_per_ppb_q0": float(slope),
            "max_deviation_from_linear": float(max_nonlin),
            "pin_window_samples": samples,
            "production_c4_value": float(mpf(4143) / 90),
            "production_c4_source_comment": (
                "4-loop anomaly derived geometrically from s5bb 5-manifold "
                "U(1) colour Reeb index"
            ),
            "production_c4_derivation_trail": "none found (git -S, docs, witnesses)",
            "cited_route_status": (
                "honest-negative — docs/audits/"
                "2026-06-16-s5so3-reeb-resonance-probe-negative.md"
            ),
        },
    }
    out = HERE / "c4-mu-p-tension-pin-dependence.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nwitness → {out.relative_to(HERE.parent.parent.parent)}")


if __name__ == "__main__":
    main()
