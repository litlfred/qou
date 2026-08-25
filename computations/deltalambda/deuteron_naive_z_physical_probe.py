#!/usr/bin/env python3
"""Deuteron (A=2) naive per-pair magnitude — derive-then-check, honest negative.

COMPLETES an explicitly-open thread of the A=4 interface-magnitude audit
(docs/audits/2026-08-02-a4-interface-magnitude-one-scalar-gate.md,
computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py).

That audit proved the naive uniform per-pair magnitude z = 1/[2]_v is scope-(b)
EXCLUDED for He4: the [1^4] complete-graph exchange spectrum {+-sqrt5, +-1} gives
det(I + z*S) = (1 - 5 z^2)(1 - z^2) < 0 because 5 z^2 > 1 (z ~ 0.4993 > 1/sqrt5).
The exclusion is A=4-SPECIFIC (the sqrt5 eigenvalue is the 2p+2n complete graph).

THE DEUTERON (A=2, 1p+1n) has exchange graph K2, sign matrix S = [[0,1],[1,0]],
spectrum {+1,-1}, so det(I + m*S) = 1 - m^2, physicality ceiling m < 1.  With
z ~ 0.4993 the deuteron det = 1 - z^2 = 0.751 > 0 -- z is PHYSICAL here.  The A=4
audit left A=2 explicitly UNCHECKED.  This probe runs the derive-then-check:

  DERIVE (locked before compute, 0-fit, pure substrate):
    z_naive = 1/[2]_v,  v = sqrt(q0)                 (naive Markov bond factor)
    g_reeb  = 1/sqrt(5 + (q0-1)^2/q0)                (q-Reeb eigenphase, C_knot
                                                      audit candidate #1)
    b2(m)   = -ln(1 - m^2)                           (K2 connected cumulant)
    derived MeV scales: m_e, mu0 = m_e/(3h/2), E+ = m_e[3]_q[4]_q/3

  CHECK: does any 0-fit combination reproduce B_AME(2H) = 2.2245662 MeV
         (equivalently the master-Sigma deficit C_knot(D) = 5.853)?

VERDICT (see witness): NO.  Both derived magnitudes are physical at A=2 but the
K2 cumulant b2 is O(0.2-0.3), a REDUCTION, and no derived scale reaches 2.22 MeV
(z needs an undrivable 7.76 MeV; g_reeb 9.99 MeV).  As a multiplicative dressing
of the master-Sigma B_cat = 0.380 MeV the required (1-z^2)^{-k} exponent is
k = 6.16 (non-integer, no structural k).  So the naive-uniform-z per-pair
mechanism is DEAD across A: excluded where NEEDED (A=4) and insufficient where
PHYSICAL (A=2).  Extra structural reason: A=2 is not a [1^A] SINGLET (rank
C(4,2)=6, not 1; only A=0,4 are singlets), so the He4-local -ln det cumulant has
no reason to transfer to the deuteron in the first place.

No fit; B_AME used only as a diagnostic ratio, never inverted; nothing wired;
free_parameters = 0.  Formalize-first companion:
  content/quantum-observable-universe/lean/QOU/MassTheory/DeuteronNaiveZMagnitude.lean
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

# canonical computations-layer q0 (muon-pinned 50-digit string); the A=2/A=4
# det signs and the ~5.85x deficit are invariant to the ~11.5 ppb proton-pin
# difference (this is a magnitude-class probe, not a precision probe).
Q0_STR = "1.10997859555733471"

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

ME_MEV = mp.mpf("0.51099895069")        # CODATA electron mass
B_AME_2H = mp.mpf("2.2245662")          # AME2020 deuteron binding (diagnostic only)
S_D_MASTER = mp.mpf("0.7438")           # |Sum_lambda y_lambda chi^lambda sgn f^lambda|(D)
                                        # committed master-Sigma signed sum (C_knot audit)


def q_int(n: int, q: mp.mpf) -> mp.mpf:
    """balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q0_STR)
    v = mp.sqrt(q0)
    two_v = v + 1 / v
    h = q0 - 1 / q0                                  # counit weight q - q^-1

    # ---- DERIVE (locked, 0-fit) ---------------------------------------------
    z_naive = 1 / two_v                              # 1/[2]_v  Markov bond factor
    g_reeb = 1 / mp.sqrt(5 + (q0 - 1) ** 2 / q0)     # q-Reeb eigenphase magnitude
    ceiling_A4 = 1 / mp.sqrt(mp.mpf(5))              # He4 writhe cap
    ceiling_A2 = mp.mpf(1)                           # K2 writhe cap (det>0 <=> m<1)

    mu0 = ME_MEV / (3 * h / 2)                       # dimensional bridge (0-fit, #4117)
    E_plus = ME_MEV * q_int(3, q0) * q_int(4, q0) / 3  # rotational bar-even, j=n/2=3

    # ---- A=2 exchange graph K2 (1p+1n), det(I+mS) = 1 - m^2 -----------------
    def a2_det(m: mp.mpf) -> mp.mpf:
        S = mp.matrix([[0, 1], [1, 0]])              # pn writhe-sign K2
        return mp.det(mp.eye(2) + m * S)

    # ---- A=4 exchange for the exclusion contrast (closed form) -------------
    def a4_det(m: mp.mpf) -> mp.mpf:
        return (1 - 5 * m ** 2) * (1 - m ** 2)

    B_cat = ME_MEV * S_D_MASTER                      # master-Sigma deuteron binding
    C_knot = B_AME_2H / B_cat                        # the fitted deficit ratio

    rows = {}
    for name, m in (("z_naive", z_naive), ("g_reeb", g_reeb)):
        det2 = a2_det(m)
        det2_closed = 1 - m ** 2
        det4 = a4_det(m)
        b2 = -mp.log(det2) if det2 > 0 else None
        rows[name] = {
            "magnitude": mp.nstr(m, 18),
            "A2_det_K2": mp.nstr(det2, 18),
            "A2_det_closed_1_minus_m2": mp.nstr(det2_closed, 18),
            "A2_det_matches_closed": bool(abs(det2 - det2_closed) < mp.mpf(10) ** -30),
            "A2_physical_det_gt_0": bool(det2 > 0),
            "A4_det_(1-5m2)(1-m2)": mp.nstr(det4, 18),
            "A4_physical_det_gt_0": bool(det4 > 0),
            "b2_minus_ln_det_A2": (mp.nstr(b2, 15) if b2 is not None else "undef"),
            "b2_is_reduction_lt_1": bool(b2 < 1) if b2 is not None else None,
            # derive-then-check: no 0-fit scale reaches B_AME
            "MeV_if_scale_me": mp.nstr(ME_MEV * b2, 12) if b2 else None,
            "MeV_if_scale_mu0": mp.nstr(mu0 * b2, 12) if b2 else None,
            "MeV_if_scale_Eplus": mp.nstr(E_plus * b2, 12) if b2 else None,
            "required_scale_to_hit_B_AME_MeV": mp.nstr(B_AME_2H / b2, 12) if b2 else None,
            # multiplicative dressing of master-Sigma B_cat
            "Bcat_times_inv_det": mp.nstr(B_cat / det2, 12) if det2 > 0 else None,
            "required_inv_det_exponent_k": mp.nstr(mp.log(C_knot) / (-mp.log(det2)), 12)
            if (det2 > 0 and det2 < 1) else None,
        }

    # cross-A structural verdict
    z_excluded_A4 = a4_det(z_naive) < 0
    z_physical_A2 = a2_det(z_naive) > 0
    z_insufficient_A2 = True  # established numerically below (no 0-fit closure)

    # deuteron is NOT a [1^A] singlet: rank Lambda^A(C^4) = C(4,A); C(4,2)=6 != 1
    from math import comb
    a2_singlet_rank = comb(4, 2)   # 6
    a4_singlet_rank = comb(4, 4)   # 1
    deuteron_is_not_singlet = (a2_singlet_rank != 1)

    result = {
        "derived_inputs_0fit": {
            "q0": Q0_STR,
            "z_naive_eq_1_over_[2]_v": mp.nstr(z_naive, 18),
            "g_reeb_eq_1_over_sqrt(5+(q0-1)^2/q0)": mp.nstr(g_reeb, 18),
            "ceiling_A4_1_over_sqrt5": mp.nstr(ceiling_A4, 12),
            "ceiling_A2_(m<1)": "1",
            "mu0_MeV": mp.nstr(mu0, 12),
            "E_plus_MeV": mp.nstr(E_plus, 12),
        },
        "master_sigma_deuteron": {
            "B_cat_MeV": mp.nstr(B_cat, 12),
            "B_AME_MeV": mp.nstr(B_AME_2H, 12),
            "C_knot_deficit": mp.nstr(C_knot, 12),
        },
        "per_magnitude": rows,
        "cross_A_structural_verdict": {
            "z_excluded_at_A4_det_lt_0": bool(z_excluded_A4),
            "z_physical_at_A2_det_gt_0": bool(z_physical_A2),
            "z_insufficient_at_A2_no_0fit_closure": bool(z_insufficient_A2),
            "naive_uniform_z_dead_across_A": bool(z_excluded_A4 and z_insufficient_A2),
            "deuteron_A2_antisym_rank_C(4,2)": a2_singlet_rank,
            "he4_A4_antisym_rank_C(4,4)": a4_singlet_rank,
            "deuteron_is_not_a_[1^A]_singlet": bool(deuteron_is_not_singlet),
        },
    }

    # ---- assertions (all derive-then-check, 0-fit) --------------------------
    checks = []

    def chk(name, cond):
        checks.append((name, bool(cond)))
        assert cond, name

    chk("z_physical_at_A2", a2_det(z_naive) > 0)
    chk("g_reeb_physical_at_A2", a2_det(g_reeb) > 0)
    chk("z_excluded_at_A4", a4_det(z_naive) < 0)
    chk("A2_det_matches_closed_form_1_minus_m2",
        abs(a2_det(z_naive) - (1 - z_naive ** 2)) < mp.mpf(10) ** -30)
    # no 0-fit closure: every derived scale * b2 is far below B_AME
    for m in (z_naive, g_reeb):
        b2 = -mp.log(a2_det(m))
        chk("b2_is_a_reduction_lt_1", b2 < 1)
        for Es in (ME_MEV, mu0, E_plus):
            chk("derived_scale_undershoots_B_AME", Es * b2 < mp.mpf("0.7") * B_AME_2H)
    # required inv-det exponents are reported as DATA, not asserted clean: z gives
    # k=6.16 (plainly non-integer); g_reeb gives k~7.94 (near 8 -- a numerology-trap
    # NEAR-coincidence, NOT exact and with no structural reason for det^{-8}; not
    # chased, per the standing single-knot-count-matching / clean-number guard).
    k_z = mp.log(C_knot) / (-mp.log(a2_det(z_naive)))
    chk("z_required_exponent_non_integer", abs(k_z - mp.nint(k_z)) > mp.mpf("0.1"))
    chk("naive_uniform_z_dead_across_A", (a4_det(z_naive) < 0))
    chk("deuteron_not_a_singlet_shell", comb(4, 2) != 1)

    result["assertions"] = {n: c for n, c in checks}
    result["all_assertions_pass"] = all(c for _, c in checks)

    verdict = (
        "HONEST NEGATIVE (scope-(a) insufficiency + scope-(b) cross-A death): the "
        "naive per-pair magnitude z=1/[2]_v is PHYSICAL at A=2 (1-z^2=0.751>0) but "
        "does NOT close the deuteron -- b2(z)=-ln(1-z^2)=0.287 is a reduction and no "
        "derived scale (m_e/mu0/E+) reaches B_AME (needs undrivable ~7.76 MeV; as a "
        "master-Sigma dressing needs non-integer exponent k=6.16). Same for g_reeb. "
        "Combined with the A=4 scope-(b) exclusion (5z^2>1), the uniform-z per-pair "
        "mechanism is dead across A. Structural: A=2 is not a [1^A] singlet (rank 6), "
        "so the He4-local -ln det cumulant has no reason to transfer to the deuteron."
    )

    out = {
        "schema": "witness/v1",
        "id": "deuteron-naive-z-physical-but-does-not-close",
        "description": (
            "Deuteron A=2 derive-then-check of the naive per-pair magnitude z=1/[2]_v "
            "(and the q-Reeb g_reeb), completing the A=4 interface audit's explicit "
            "open thread. z is scope-(b) EXCLUDED at A=4 (det<0) but PHYSICAL at A=2 "
            "(K2 spectrum {+-1}, 1-z^2>0); yet it does NOT close the deuteron under any "
            "0-fit scale. 0 free parameters; B_AME diagnostic-only; nothing wired."
        ),
        "verdict": verdict,
        "free_parameters": 0,
        "targets_never_inverted_into_production": True,
        "results": result,
    }
    outpath = Path(__file__).with_name("deuteron-naive-z-physical-but-does-not-close.witness.json")
    outpath.write_text(json.dumps(out, indent=1) + "\n")
    print("wrote", outpath.name)
    print("verdict:", verdict[:120], "...")
    print("z_naive =", mp.nstr(z_naive, 12), "| A2 det =", mp.nstr(a2_det(z_naive), 12),
          "(>0 physical) | A4 det =", mp.nstr(a4_det(z_naive), 12), "(<0 excluded)")
    print("b2(z) =", mp.nstr(-mp.log(a2_det(z_naive)), 10),
          "| required scale to hit B_AME =", mp.nstr(B_AME_2H / (-mp.log(a2_det(z_naive))), 8), "MeV")
    print("all_assertions_pass =", out["results"]["all_assertions_pass"])
    return 0 if out["results"]["all_assertions_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
