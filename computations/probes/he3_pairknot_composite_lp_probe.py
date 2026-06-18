"""³He proton pair-knot composite — LP-dual + def:coulomb-charge probe.

The #2467 fix direction for the inverted A=3 mirror ordering was "an LP-dual
pair-knot composite for the proton near-pole pair + an explicit Z(Z−1) Coulomb
term". The Coulomb half is ALREADY derived (def:coulomb-charge, Q_pp=+1, ratio
tanh(ln q₀); charge_coulomb_tn3he_derived.py covers ~31%, residual is a known-
open, forbidden CAL-4 magnitude). This probe tests the *pair-knot composite*
half — the candidate for the open "categorical two-like-charge brane-pairing
invariant" (charge_coulomb_tn3he_derived.py:22) — and reports an honest,
non-fit verdict on whether a direct LP-dual yields it.

Two tractable, canonical parts (no fit, no fourth calibration):

PART 1 — canonical H_3 operator-selection LP-dual (per nucleon).
  Mirrors aK_via_lp_dual_hecke_basis.py: NF basis {γ,σ₀,σ₁,L₊,L₋,e⁻},
  Frobenius Gram G_ij = tr_M(b_i b_j), n_target = |tr_M(proton)|, route via
  lp_dual_solver.solve_operator_selection_lp. RESULT: the single-nucleon LP is
  DEGENERATE (y0* = 0, only the identity γ active) — a free nucleon has
  W_free = W_atom, so there is no binding constraint to select against. The
  pair-knot is intrinsically a 2-nucleon (H_6) object, where the full 720-
  element basis LP is intractable and the block-diagonal LP is also degenerate
  (audit §7d). So a DIRECT operator-selection LP-dual does NOT isolate the
  pair-knot invariant at any tractable level. (LP is scipy f64 — the canonical
  pattern of aK_via_lp_dual_hecke_basis.py; used here only to exhibit the
  qualitative degeneracy, not a precision-critical value.)

PART 2 — pair-knot composite via the canonical bond traces + def:coulomb-charge.
  Bond strengths L_pp/L_pn/L_nn = log(tr_M^full/tr_M^atom) from tr_m_atom_zn
  (50 dps). The proton pair-knot composite carries Coulomb charge Q_pp = +1
  (def:coulomb-charge), with Coulomb/strong ratio tanh(ln q₀) = (q₀²−1)/(q₀²+1)
  (prop:coulomb-strong-ratio-q-rational, Lean-proved — cross-checked here to
  the 50-dps floor). The composite REPLACES the two individual near-pole proton
  generators (whose per-generator over-count is the spurious Δtower of
  he3_tower_charge_asymmetry_probe.py, E₀·Δtower ≈ 1.165 MeV, WRONG sign) with
  ONE pp bond whose charge-asymmetric part is the DERIVED Coulomb reduction
  ratio·B_pp ≈ 0.238 MeV (correct sign — reduces ³He), i.e. the 31% of
  charge_coulomb_tn3he_derived.py.

VERDICT (honest, non-fit): the pair-knot composite is the right *object* — it
removes the spurious per-generator asymmetry and carries the correct
def:coulomb-charge sign — but its magnitude closure is the known-open invariant
(31% covered; the residual 3.2× would be a forbidden CAL-4 fit). A direct
LP-dual cannot supply it (degenerate/intractable); the invariant must come from
the analytical C_λ·S_λ factorisation (prop:mass-coefficient-shadow-price /
audit §7d) or a new categorical construction. This probe SCOPES the open item;
it does not close it.

EXPLORATORY / audit-only. LP: scipy f64 (canonical pattern); cross-checks: 50 dps.
Audit: docs/audits/2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import numpy as np

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate"),
           str(_COMP.parent / "tools" / "pyhecke" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from pyhecke.gram import NF_NAMES, TR_M, gram_matrix  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

mp.mp.dps = 50

# NF-basis Wedderburn dominant blocks (from aK_via_lp_dual_hecke_basis.py):
# self-conjugate (charge-symmetric / strong) = (2,1) = L₊,L₋; the rest
# (γ,σ₀,σ₁→(3); e⁻→(1,1,1)) are non-self-conjugate = the chirality / Coulomb
# channels of def:coulomb-charge (the q↔q⁻¹-antisymmetric part).
SELF_CONJUGATE = (False, False, False, True, True, False)


def _load_json(name: str) -> dict:
    return json.loads((_COMP / name).read_text(encoding="utf-8"))


def main() -> int:
    self_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(self_path.read_bytes()).hexdigest()[:12]
    q0 = mp.mpf(str(Q0))

    # ── PART 1: canonical H_3 operator-selection LP-dual (proton) ──────────
    n_target = mp.mpf(_load_json("chi-proton-h3-at-q0-50dps.witness.json")["tr_M_at_q0"])
    t = np.asarray([float(x) for x in TR_M], dtype=float)
    G = np.asarray(gram_matrix(), dtype=float)
    res = solve_operator_selection_lp(t, G, float(n_target), backend="scipy")
    y_star = list(res.y_star)
    chi_y = sum(y for y, sc in zip(y_star, SELF_CONJUGATE) if not sc)
    sc_y = sum(y for y, sc in zip(y_star, SELF_CONJUGATE) if sc)
    lp_degenerate = abs(res.y0_star) < 1e-6

    # ── PART 2: pair-knot composite via canonical bond traces + Coulomb ────
    bonds = {}
    for key, (Z, N) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
        r = tr_m_atom_zn(Z, N, dps=50)
        ta, tf = mp.mpf(str(r[0])), mp.mpf(str(r[1]))
        bonds[key] = mp.log(tf / ta)

    # Coulomb/strong ratio: analytic tanh(ln q₀) vs the q-rational (Lean-proved
    # prop:coulomb-strong-ratio-q-rational). Exact equality at the 50-dps floor.
    ratio_tanh = mp.tanh(mp.log(q0))
    ratio_qrat = (q0 ** 2 - 1) / (q0 ** 2 + 1)
    ratio_residual = abs(ratio_tanh - ratio_qrat)
    ratio_exact = ratio_residual < mp.mpf(10) ** (-40)

    # Cite (do NOT recompute) the derived pp-Coulomb from charge_coulomb_tn3he_derived.
    cc = _load_json("charge-coulomb-tn3he-derived.witness.json")
    cc_d = cc.get("data", cc)
    B_pp = mp.mpf(str(cc_d["B_pp_strong_MeV"]))
    frac_covered = mp.mpf(str(cc_d["fraction_of_split_covered"]))
    dHe_cited = mp.mpf(str(cc_d["derived_coulomb_dHe_MeV"]))
    dHe_recomputed = ratio_tanh * B_pp                  # ratio·B_pp at CURRENT q0
    dHe_drift = abs(dHe_recomputed - dHe_cited)
    # Guard against a stale cited witness: tolerance 1e-6 absorbs a q0-repin
    # drift between witnesses computed at different times. The charge-coulomb
    # witness was refreshed at the current q0 in PR #2478 (drift now ~1e-17); if
    # a future re-pin makes it drift again (>1e-10) cc_witness_stale re-fires.
    dHe_consistent = dHe_drift < mp.mpf("1e-6")
    cc_witness_stale = dHe_drift > mp.mpf("1e-10")

    # Connect to D1: the spurious per-generator over-count the composite removes.
    d1 = _load_json("he3-tower-charge-asymmetry.witness.json")
    spurious_asym_MeV = mp.mpf(d1["data"]["E0_times_delta_tower_MeV"])

    # The composite's Coulomb has the CORRECT sign (reduces ³He: dHe > 0), the
    # OPPOSITE of the spurious tower asymmetry (which favored ³He): right object.
    pairknot_correct_sign = bool(dHe_recomputed > 0 and spurious_asym_MeV > 0)

    print("PART 1 — canonical H_3 operator-selection LP-dual (proton):")
    print(f"  y0* = {res.y0_star:.3e}   active_set = {res.active_set}   "
          f"feasible = {res.feasible}")
    print(f"  y* = {[round(y, 4) for y in y_star]}  (NF: {' '.join(NF_NAMES)})")
    print(f"  Σy*(self-conj/strong) = {sc_y:.4f}   Σy*(chirality/Coulomb) = {chi_y:.4f}")
    print(f"  duality_gap = {res.duality_gap:.2e}")
    print(f"  => DEGENERATE: {lp_degenerate}  (single nucleon: W_free=W_atom; "
          f"A=2 pair needs H_6, intractable/degenerate — audit §7d)")
    print()
    print("PART 2 — pair-knot composite (bond traces + def:coulomb-charge):")
    print(f"  bond L (log tr_M^full/atom): pp={mp.nstr(bonds['pp'],6)}  "
          f"pn={mp.nstr(bonds['pn'],6)}  nn={mp.nstr(bonds['nn'],6)}")
    print(f"  Coulomb/strong ratio: tanh(ln q₀)={mp.nstr(ratio_tanh,12)}  "
          f"(q₀²−1)/(q₀²+1)={mp.nstr(ratio_qrat,12)}  exact={ratio_exact}")
    print(f"  pp pair-knot: Q_pp=+1, B_pp={mp.nstr(B_pp,6)} MeV, "
          f"Coulomb reduction ratio·B_pp={mp.nstr(dHe_recomputed,6)} MeV "
          f"({mp.nstr(frac_covered*100,4)}% of split)")
    print(f"  vs D1 spurious E₀·Δtower = {mp.nstr(spurious_asym_MeV,6)} MeV "
          f"(wrong sign, removed by the composite)")
    if cc_witness_stale:
        print(f"  [QA flag] charge-coulomb witness STALE: dHe drift "
              f"{mp.nstr(dHe_drift,3)} vs fresh ratio·B_pp — predates the "
              f"2026-05-28 q0 re-pin; refresh recommended (31% robust to it).")
    print()
    print("VERDICT: the pair-knot composite is the RIGHT OBJECT (removes the "
          "spurious per-generator over-count; carries def:coulomb-charge Q_pp=+1, "
          "correct sign) but its magnitude is the known-OPEN invariant (31% "
          "covered; residual forbidden-to-fit). A DIRECT LP-dual is "
          "degenerate/intractable — the invariant must come analytically "
          "(C_λ·S_λ, audit §7d). Scopes the open item; does not close it. No fit.")

    assertions = [
        {"name": "h3_single_nucleon_lp_degenerate",
         "computed": 1 if lp_degenerate else 0, "expected": 1, "tolerance": 0,
         "note": "|y0*| < 1e-6: direct operator-selection LP does not isolate the "
                 "pair-knot invariant (free nucleon W_free=W_atom)"},
        {"name": "coulomb_ratio_q_rational_exact_50dps",
         "computed": 1 if ratio_exact else 0, "expected": 1, "tolerance": 0,
         "note": "tanh(ln q₀) == (q₀²−1)/(q₀²+1) to <1e-40 "
                 "(prop:coulomb-strong-ratio-q-rational, Lean-proved)"},
        {"name": "pairknot_coulomb_consistent_modulo_qrepin",
         "computed": 1 if dHe_consistent else 0, "expected": 1, "tolerance": 0,
         "note": f"ratio·B_pp reproduces charge_coulomb_tn3he_derived dHe (Q_pp=+1) "
                 f"to {mp.nstr(dHe_drift, 3)} at current q0 "
                 f"(witness refreshed in PR #2478)"},
        {"name": "pairknot_correct_sign_vs_spurious",
         "computed": 1 if pairknot_correct_sign else 0, "expected": 1, "tolerance": 0,
         "note": "composite Coulomb reduces ³He (right sign), opposite to the "
                 "spurious tower asymmetry it replaces"},
        {"name": "magnitude_open_partial_not_closed",
         "computed": 1 if (mp.mpf("0.1") < frac_covered < mp.mpf("1.0")) else 0,
         "expected": 1, "tolerance": 0,
         "note": "31% covered — right order, partial, residual is the open "
                 "(forbidden-to-fit) brane-pairing invariant"},
    ]
    all_passed = all(a["computed"] == a["expected"] for a in assertions)

    witness = {
        "engine": "scipy+mpmath",
        "engineVersion": f"mpmath {mp.__version__}; numpy {np.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "he3-pairknot-composite-lp",
        "scriptFile": self_path.name,
        "scriptHash": script_hash,
        "contentBlock": "def:coulomb-charge",
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-06-18-he3-tower-charge-asymmetry-and-pairknot.md",
        "description": (
            "Tests the LP-dual proton pair-knot composite (the #2467 fix "
            "direction + candidate for the open categorical brane-pairing "
            "invariant). The canonical H_3 operator-selection LP-dual is "
            "degenerate (single nucleon W_free=W_atom; A=2 pair H_6 "
            "intractable/degenerate, audit §7d), so a direct LP cannot isolate "
            "the invariant. The pair-knot composite (def:coulomb-charge Q_pp=+1, "
            "ratio tanh(ln q₀)=(q₀²−1)/(q₀²+1)) is the right object — it removes "
            "the spurious per-generator over-count (he3-tower-charge-asymmetry) "
            "and carries the correct-sign Coulomb (31%, charge_coulomb_tn3he_"
            "derived) — but the residual magnitude is the known-open, forbidden-"
            "to-fit gap. EXPLORATORY; scopes, does not close. No fit."
        ),
        "parameters": {
            "q_0_50dps": mp.nstr(Q0, 50),
            "lp_backend": "scipy linprog (f64) — canonical aK_via_lp_dual pattern; "
                          "exhibits degeneracy only, not a precision-critical value",
            "n_target_proton": mp.nstr(n_target, 50),
            "nf_basis": list(NF_NAMES),
        },
        # LP/SDP dual fields (CLAUDE.md §LP/SDP duals — first-class infra)
        "y0_star": res.y0_star,
        "y_star": y_star,
        "active_set": list(res.active_set),
        "primal_obj": res.primal_obj,
        "dual_obj": res.dual_obj,
        "duality_gap": res.duality_gap,
        "data": {
            "lp_proton": {
                "y0_star": res.y0_star, "y_star": y_star,
                "active_set": list(res.active_set),
                "self_conjugate_y_sum": sc_y, "chirality_y_sum": chi_y,
                "feasible": res.feasible, "degenerate": lp_degenerate,
            },
            "bonds_log_ratio": {k: mp.nstr(v, 16) for k, v in bonds.items()},
            "coulomb_ratio_tanh_ln_q0": mp.nstr(ratio_tanh, 30),
            "coulomb_ratio_q_rational": mp.nstr(ratio_qrat, 30),
            "coulomb_ratio_residual": mp.nstr(ratio_residual, 6),
            "pp_pairknot": {
                "Q_pp": 1, "B_pp_strong_MeV": mp.nstr(B_pp, 12),
                "coulomb_reduction_MeV": mp.nstr(dHe_recomputed, 12),
                "fraction_of_split_covered": mp.nstr(frac_covered, 12),
                "cited_from": "charge-coulomb-tn3he-derived.witness.json",
            },
            "spurious_tower_asymmetry_MeV": mp.nstr(spurious_asym_MeV, 12),
            "charge_coulomb_witness_qrepin_drift": mp.nstr(dHe_drift, 6),
            "charge_coulomb_witness_stale": cc_witness_stale,
            "stale_note": (
                "charge-coulomb-tn3he-derived.witness.json is STALE (drift "
                f"{mp.nstr(dHe_drift, 3)} > 1e-10 from current q0; predates the "
                "2026-05-28 re-pin) — refresh recommended."
                if cc_witness_stale else
                "charge-coulomb-tn3he-derived.witness.json is current (drift "
                f"{mp.nstr(dHe_drift, 3)}); refreshed in PR #2478."
            ),
        },
        "assertions": assertions,
        "allPassed": all_passed,
        "provenance": [
            "pyhecke.gram (NF basis, Frobenius Gram)",
            "lp_dual_solver.solve_operator_selection_lp",
            "chi-proton-h3-at-q0-50dps.witness.json (n_target)",
            "tr_m_atom_via_transfer.tr_m_atom_zn (pp/pn/nn bonds)",
            "def:coulomb-charge, prop:coulomb-strong-ratio-q-rational",
            "charge-coulomb-tn3he-derived.witness.json (31%, B_pp — cited)",
            "he3-tower-charge-asymmetry.witness.json (spurious Δtower)",
        ],
    }
    out = _COMP / "he3-pairknot-composite-lp.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"\nwrote {out}   allPassed={all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
