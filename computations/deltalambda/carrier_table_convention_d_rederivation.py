#!/usr/bin/env python3
"""
carrier_table_convention_d_rederivation.py — INDEPENDENT re-derivation of the
carrier table under convention D. No fit, no tuning, no re-baselining.

# Ref: docs/audits/2026-08-26-carrier-saturation-five-failures-diagnosis.md
# Ref: docs/audits/2026-07-13-carrier-saturation-crossover-mechanism.md
# Ref: content/quantum-observable-universe/mass-theory/wedderburn-trace-identity.md

WHY THIS EXISTS, AND WHY IT IS NOT carrier_saturation_mechanism_probe.py.

The carrier audit table (2026-07-13) was computed before convention C was
excised on 2026-08-09. Its `m_e·S` and `𝒜` columns are therefore
convention-C-frame, while `carrier_saturation_mechanism_probe.py` now computes
in convention D — which is the whole of the five-assertion failure diagnosed in
the audit above.

Re-deriving the table means recomputing those columns under D. The tempting
shortcut is to copy the probe's output into the probe's own expected literals.
That is numerically the same edit and epistemically its opposite: an assertion
that checks a script against itself asserts nothing. So this module recomputes
the same quantities through a DIFFERENT PATH and the literals are taken from
here, leaving the probe's assertions a genuine two-path cross-check.

WHERE THE INDEPENDENCE ACTUALLY IS (it is not independence of DATA — both paths
read the same cached χ; it is independence of CODE, which catches transcription
and arithmetic error, not a bad input):

  quantity   probe                              here
  ────────   ────────────────────────────────   ──────────────────────────────
  y_λ        reads the cached `y_lambda` field  RECOMPUTES y_lambda_su_n(3A,q₀,2)
  θ          reads `delta_theta_rad`            RECOMPUTES arccos(χ/dim) per side
  Δθ         reads it                           θ_atom − θ_free, formed here
  dim_λ      hook length                        hook length (same formula)

SCOPE, stated because it bounds what the output may be used for. The four
anchors D/T/³He/⁴He have a cached per-block free AND atom χ
(`binding-reeb-phase-decomposition.witness.json`), so both factors can be
rebuilt from primary quantities. ⁵Li/⁶Li do NOT: their free χ is produced by the
Littlewood–Richardson path inside the probe, and re-deriving them here would
mean calling the probe's own functions — the same code, so not a cross-check.
They are therefore OUT OF SCOPE and this module says so rather than emitting a
number that looks independent and is not.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported. Without
# this the module is unresolvable and the script cannot run standalone.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402
from mpmath import mp  # noqa: E402

_COMP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_COMP))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
    AME_B_LI5_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION,
)

set_compute_dps()

q0 = mp.mpf(Q_50_DIGIT_STR)
M_E = mp.mpf(str(M_E_MEV))

B_AME = {
    "D": mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
    "T": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
    "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
    "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION)),
}
A_OF = {"D": 2, "T": 3, "3He": 3, "4He": 4, "5Li": 5, "6Li": 6}
ANCHORS = ["D", "T", "3He", "4He"]
REEB = "binding-reeb-phase-decomposition.witness.json"

# ⁶Li: atom χ from the cached H_18 witness; free χ from the Frobenius path
# (chi_free_via_frobenius), which is independent of the probe's LR route.
LARGE_A_ATOM = {
    "5Li": "chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json",
    "6Li": "chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json",
}
LARGE_A_ZN = {"5Li": (3, 2), "6Li": (3, 3)}
B_AME["5Li"] = mp.mpf(str(AME_B_LI5_MEV_VALIDATION))
B_AME["6Li"] = mp.mpf(str(AME_B_LI6_MEV_VALIDATION))


def dim_sn(lam) -> int:
    """f^λ by hook length. Same formula both paths use; there is only one."""
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def theta_of(r: mp.mpf) -> mp.mpf:
    """arccos on the rotation channel, arccosh on the growth channel.

    Matches `theta()` in the probe. |r| <= 1 is the bounded rotation case; the
    outer (n)/(1^n) channels can exceed 1 and carry q^{±writhe} growth instead.
    """
    return mp.acos(r) if mp.fabs(r) <= 1 else mp.acosh(mp.fabs(r))


def rederive(atom: str, reeb: dict) -> dict:
    rows = reeb["data"]["per_atom"][atom]["by_partition"]
    n = 3 * A_OF[atom]

    # y_λ RECOMPUTED under convention D, not read from any cache.
    y_fresh = y_lambda_su_n(n, q0, 2)
    y_by_key = {tuple(sh): v for sh, v in y_fresh.items()}

    S = mp.mpf(0)
    W = mp.mpf(0)
    used = 0
    for r in rows:
        lam = tuple(r["partition"]) if isinstance(r["partition"], list) \
            else tuple(int(x) for x in str(r["partition"]).strip("[]").split(","))
        y = y_by_key.get(lam)
        if y is None:
            raise KeyError(f"{atom}: no fresh y_λ for {lam}")
        d = dim_sn(lam)

        # θ REBUILT from χ/dim, not read from `delta_theta_rad`.
        r_free = mp.mpf(str(r["chi_free"])) / d
        r_atom = mp.mpf(str(r["chi_atom"])) / d
        dtheta = theta_of(r_atom) - theta_of(r_free)

        p = y * d
        W += p
        S += p * mp.fabs(dtheta)
        used += 1

    me_S = M_E * S
    return {"n_blocks": used, "W": W, "S": S, "me_S": me_S,
            "A_req": B_AME[atom] / me_S}


def rederive_large_a(atom: str) -> dict:
    """⁶Li with the free χ from the Frobenius path, not the probe's LR path.

    This is what lets `li6_amplification_pinned` become a real assertion: the
    expected value no longer descends from the script being checked.
    """
    from chi_free_via_frobenius import chi_free_frobenius  # noqa: E402

    w = json.loads((_COMP / LARGE_A_ATOM[atom]).read_text())
    if w.get("partial") or w.get("tr_M_partial"):
        raise RuntimeError(f"{atom} atom witness is partial — regenerate")
    if int(w["n_partitions"]) != int(w["n_partitions_total"]):
        raise RuntimeError(f"{atom} atom witness skipped partitions")

    Z, N = LARGE_A_ZN[atom]
    chi_free = chi_free_frobenius(Z, N)
    n = 3 * (Z + N)
    y_fresh = {tuple(sh): v for sh, v in y_lambda_su_n(n, q0, 2).items()}

    S = mp.mpf(0)
    W = mp.mpf(0)
    used = 0
    for e in w["by_partition"]:
        lam = tuple(e["partition"])
        d = dim_sn(lam)
        r_atom = mp.mpf(str(e["chi_lambda"])) / d
        r_free = chi_free[lam] / d
        dtheta = theta_of(r_atom) - theta_of(r_free)
        p = y_fresh[lam] * d
        W += p
        S += p * mp.fabs(dtheta)
        used += 1

    me_S = M_E * S
    return {"n_blocks": used, "W": W, "S": S, "me_S": me_S,
            "A_req": B_AME[atom] / me_S}


def main() -> int:
    reeb = json.loads((_COMP / REEB).read_text())
    wb = WitnessBuilder("carrier-table-convention-d-rederivation",
                        engine="mpmath")
    wb.set_description(
        "Independent convention-D re-derivation of the carrier table's "
        "m_e*S and A columns for the four anchors. y_lambda is RECOMPUTED "
        "from y_lambda_su_n and theta is REBUILT from chi/dim, so the "
        "probe's expected literals are not checked against the probe's own "
        "output. 5Li/6Li are out of scope: their free chi comes from the "
        "probe's own LR path, which would not be a cross-check.")

    print("=" * 74)
    print(" carrier table — INDEPENDENT convention-D re-derivation")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q0, 12)}   m_e = {mp.nstr(M_E, 9)} MeV")
    print(f"  y_lambda: RECOMPUTED (y_lambda_su_n, convention D)")
    print(f"  theta:    REBUILT from chi/dim via arccos/arccosh\n")
    print("  atom   A  blocks   W=Σp          m_e·S MeV     𝒜=B/(m_e·S)")

    out = {}
    for a in ANCHORS:
        r = rederive(a, reeb)
        out[a] = r
        print(f"  {a:>4s}  {A_OF[a]:>2d}  {r['n_blocks']:>5d}  "
              f"{mp.nstr(r['W'], 11):>13s}  {mp.nstr(r['me_S'], 8):>12s}  "
              f"{mp.nstr(r['A_req'], 8):>12s}")

    # The normalisation is the one thing that must hold exactly, in either
    # convention -- it is the Markov-trace identity, not a convention artefact.
    for atom in ("5Li", "6Li"):
        r = rederive_large_a(atom)
        out[atom] = r
        print(f"  {atom:>4s}  {A_OF[atom]:>2d}  {r['n_blocks']:>5d}  "
              f"{mp.nstr(r['W'], 11):>13s}  {mp.nstr(r['me_S'], 8):>12s}  "
              f"{mp.nstr(r['A_req'], 8):>12s}   [free χ: Frobenius, not LR]")

    ALL = list(ANCHORS) + ["5Li", "6Li"]
    max_W_dev = max(mp.fabs(out[a]["W"] - 1) for a in ALL)
    print(f"\n  max |W − 1| over the {len(ALL)} atoms = "
          f"{mp.nstr(max_W_dev, 6)}")

    wb.add_assertion(
        "markov_normalization_recomputed_weights",
        computed=fmt(max_W_dev), expected="0", tolerance="1e-40",
    )
    for a in ALL:
        wb.add_data(f"me_S_MeV_{a}", fmt(out[a]["me_S"]))
        wb.add_data(f"A_req_{a}", fmt(out[a]["A_req"]))
    wb.add_data("scope_note",
                "D/T/3He/4He rebuild theta from the cached per-block free AND "
                "atom chi. 6Li has no cached free chi, so its free half comes "
                "from chi_free_via_frobenius -- the power-sum/Murnaghan-"
                "Nakayama route, which forms no Littlewood-Richardson "
                "coefficient and is therefore independent of the probe's LR "
                "path. 5Li is still excluded: no independent check was built "
                "for it.")
    out = wb.save()
    print(f"\n  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
