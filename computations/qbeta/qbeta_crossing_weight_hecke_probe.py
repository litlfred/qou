#!/usr/bin/env python3
"""
Q_beta crossing-weight from the H_3 Groebner-Shirshov reducer -- W1/W2 gates.

Executes the pre-registered gates of
`docs/scope/2026-07-07-qbeta-crossing-weight-hecke-determination.md` (PR #3477)
now that `pyhecke` / the symbolic H_3 GS machinery is importable. Determines the
Q_beta crossing weight from the Hecke/Markov structure ITSELF (the augmentation
of the reduced nucleon normal form), NOT by inverting the observed ladder.

Objects (all EXACT, symbolic in q; NO CODATA, NO fit, NO anchor):
  Delta(net)(q) = augmentation(nucleon_nf(u,d,d)) - augmentation(nucleon_nf(u,u,d))
                  -- the first-principles categorical Q_beta net (H_3 GS reducer,
                     reproduces the committed free-neutron-decay witness at N=0).
  counit        = h^2/2 - h,  h = q - 1/q  (the N=0 truncation / KC18 counit).
  Q_A           = m_e*|q^2-2q-1|(q+1)/(2q^3) = |counit * E_0|, E_0 = m_e/(q(q-1)).
  Q_N1          = Q_A * cos(alpha - b*hbar^2/2)  (production cos-dressed base).
  u             = b*hbar^2,  b = sqrt((h^2+3)/(h^2+4)),  hbar = (q-1)/q.

W1 (counit reproduction): the Frobenius pairing <(n-p)_{N=0}, G^{-1}1>_G equals
  net = h^2/2 - h (numeric via pyhecke.gram, if available), AND the full GS
  Delta(net) agrees with the counit through O(hbar^2).  -> PASS.

W2 (departure order / ladder match): the effective crossing weight
  w = (h^2/2 - Delta(net))/h  and its departure  w - 1  from the GS net; the
  ratio Q_beta^GS/Q_N1 - 1 must be of pure ladder shape  sum_{k>=2} c_k u^k
  (leading order u^2 ~ hbar^4).  It is NOT: it carries a leading O(hbar^2)=O(u)
  term (coeff 9/8), BELOW the c_2 u^2 rung.  -> KILL (scope-(a)): the full
  first-principles GS augmentation is NOT the production cos*(1+c_k u^2) ladder;
  the categorical higher orders push Q_beta AWAY from CODATA (+0.75% full-GS vs
  +0.17% N=0 Q_A).  This does not refute the ladder ansatz or any c_k; it refutes
  the hypothesis "full GS net == production ladder".

W3 is N/A: W2 kills the identification, so the "does the stabilization reproduce
c_2 = -1" check is moot for the full-GS-net-as-ladder hypothesis.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (
    _ROOT,
    os.path.join(_ROOT, "tools", "pyhecke", "python"),
    os.path.join(_ROOT, "tools", "qou-substrate", "python"),
    os.path.join(_ROOT, "tools", "pyhecke-native", "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import computations.qbeta.qbeta_h4_nucleon_assembly as h4  # noqa: E402


def _repo_head_sha():
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_HERE, text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha -- refusing to emit witness")
    return sha


def main():
    q = h4.q
    h = q - 1 / q
    t = sp.symbols("t", positive=True)          # t = hbar_q = (q-1)/q ; q = 1/(1-t)
    N = 8
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed),
                           "skipped": False, "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    def skip(name, reason):
        # A skipped check is NOT a pass: recorded with skipped=True and
        # passed=False so a green `allPassed` cannot hide an un-run gate.
        assertions.append({"name": name, "passed": False,
                           "skipped": True, "detail": f"SKIPPED: {reason}"})
        print(f"  [SKIP] {name}  {reason}")

    def ser(expr):
        return sp.expand(sp.series(expr.subs(q, 1 / (1 - t)), t, 0, N).removeO())

    # --- first-principles categorical net (exact symbolic) ---
    dnet = sp.cancel(
        h4.augmentation(h4.nucleon_nf(["u", "d", "d"]))
        - h4.augmentation(h4.nucleon_nf(["u", "u", "d"]))
    )
    counit = h ** 2 / 2 - h

    # ---- W1: counit reproduction ----
    dnet_t = ser(dnet)
    counit_t = ser(counit)
    # agree through O(t^2): coefficients of t^0,t^1,t^2 equal
    agree_2 = all(dnet_t.coeff(t, k) == counit_t.coeff(t, k) for k in (0, 1, 2))
    check("W1_gs_net_matches_counit_through_hbar2", agree_2,
          f"dnet={dnet_t.coeff(t,1)}*t+{dnet_t.coeff(t,2)}*t^2..., counit same to O(t^2)")
    # first deviation is at t^3 (dnet has -t^3, counit +t^3)
    check("W1_first_deviation_at_hbar3",
          dnet_t.coeff(t, 3) != counit_t.coeff(t, 3)
          and dnet_t.coeff(t, 2) == counit_t.coeff(t, 2),
          f"dnet[t^3]={dnet_t.coeff(t,3)} vs counit[t^3]={counit_t.coeff(t,3)}")

    # Numeric Frobenius-pairing cross-checks against the actual pyhecke Gram
    # matrix G (needs pyhecke+numpy). These are G-DEPENDENT (they fail if the
    # committed G / z drift) -- unlike the model identity ε=<·,G^-1 1>=net, which
    # holds for any G by construction and is therefore NOT a drift gate.
    try:
        import numpy as np
        from pyhecke import gram
        hv, zv = gram.h, gram.z
        v = np.array([hv * hv / 2, -hv / 2, -hv / 2, 0.0, 0.0, 0.0])
        # (a) Markov trace tr_M(v) = <v, e_γ>_G = h^2/2 - h*z : uses G's Markov
        # column non-trivially -> genuine G-dependent check.
        egamma = np.array([1, 0, 0, 0, 0, 0.0])
        trM_pairing = float(v @ gram.G @ egamma)
        check("W1_trM_pairing_G_dependent",
              abs(trM_pairing - float(hv * hv / 2 - hv * zv)) < 1e-12,
              f"<v,e_γ>_G={trM_pairing:.12g} vs h^2/2-h*z={float(hv*hv/2-hv*zv):.12g}")
        # (b) the cointegral ω = G^-1·1.
        #
        # 🛑 UNDER CONVENTION D THIS OBJECT DOES NOT EXIST, and the previous
        # `np.linalg.solve(gram.G, np.ones(6))` here was not merely unguarded
        # (bean qou-yof3) — it was ILL-POSED. Measured: numpy raises nothing
        # and returns a vector of order 1e14 with residual ||G·ω − 1|| = 0.14.
        #
        # Both fixes the bean proposed are refuted, exactly, over ℚ(q):
        #
        #   G's radical is spanned by the q-antisymmetriser v_i = (−1/q)^len(w_i)
        #   (gram.py closed form). The all-ones RHS pairs with it as
        #
        #       ⟨v, 1⟩ = 1 − 2/q + 2/q² − 1/q³ = (q−1)(q²−q+1) / q³
        #
        #   which vanishes ONLY at q = 1 (and at the primitive 6th roots of
        #   unity, which are not real). At the substrate q₀ it is ≈ 0.0902372.
        #
        #   • ⟨v,1⟩ ≠ 0 ⇒ 1 ∉ range(G) ⇒ G·ω = 1 is INCONSISTENT, so no
        #     pseudo-inverse recovers a solution. Routing through
        #     `safe_inverse`/`pinv` (the bean's option 1) returns a
        #     least-squares vector for an unsolvable system — it converts a
        #     loudly wrong answer into a quietly wrong one.
        #   • The same ≠ 0 means the all-ones functional does not annihilate
        #     the radical, so the RHS does not descend to H₃/rad. Solving on
        #     the TL₃ quotient (the bean's option 2, and qou-8iru's move) does
        #     not rescue THIS system either.
        #
        # So the honest check is the obstruction itself: it is exact, it is
        # G-dependent (it moves if the radical or the convention drifts), and
        # it is the well-posed statement of what the old assertion was groping
        # at. The net-ansatz reference ω = [0.601, …] is a convention-C object
        # and is retained in the detail string for provenance only.
        import sympy as _sp
        _q = _sp.symbols("q", positive=True)
        _obstruction = _sp.simplify(sum(_sp.Integer(-1) ** len(w) / _q ** len(w)
                                        for w in gram.NF_BASIS))
        _num = _sp.factor(_sp.numer(_sp.together(_obstruction)))
        check("W1_cointegral_obstruction_is_exactly_(q-1)(q^2-q+1)/q^3",
              _sp.simplify(_num - (_q - 1) * (_q ** 2 - _q + 1)) == 0,
              f"⟨v,1⟩ numerator = {_num}; the cointegral G^-1·1 does not exist "
              f"under D (C-frame net-ansatz was [0.601, 0.188, 0.188, 0.396, "
              f"0.396, 0.026])")
        # Nonvanishing is STRUCTURAL, not numerical — no q₀ evaluation, hence
        # no float64 anywhere in this leg (AGENTS.md: probes are not exempt).
        # For real q > 1: (q−1) > 0, and q²−q+1 has discriminant 1−4 = −3 < 0
        # with positive leading coefficient, so it is positive for ALL real q.
        # Hence ⟨v,1⟩ > 0 strictly on the whole substrate regime.
        _disc = _sp.discriminant(_q ** 2 - _q + 1, _q)
        check("W1_cointegral_obstruction_nonzero_for_every_real_q_gt_1",
              _disc == -3 and _sp.simplify(_num.subs(_q, 1)) == 0,
              f"disc(q²−q+1) = {_disc} < 0 ⇒ no real root ⇒ ⟨v,1⟩ ≠ 0 for every "
              f"real q > 1 ⇒ 1 ∉ range(G): G·ω = 1 is inconsistent at every "
              f"substrate value, so neither pinv nor the TL₃ quotient rescues it")
    except Exception as e:  # pragma: no cover
        skip("W1_trM_pairing_G_dependent",
             f"pyhecke/numpy unavailable ({type(e).__name__}); symbolic W1 stands")
        skip("W1_cointegral_matches_net_ansatz",
             f"pyhecke/numpy unavailable ({type(e).__name__})")

    # ---- W2: does the full GS net match the production cos-ladder? ----
    ratio_A = ser(sp.cancel(dnet / counit))     # Q_beta^GS / Q_A
    # production cos-dressed base Q_N1/Q_A
    z = q**3 / (q**2 + 1)
    alpha = (z - 1) * h / 2
    b = sp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    hbar = (q - 1) / q
    arg = ser(alpha) - ser(b * hbar ** 2 / 2)
    cosfac = sp.expand(sp.series(sp.cos(arg), t, 0, N).removeO())
    resid = sp.expand(sp.series(ratio_A / cosfac - 1, t, 0, N).removeO())
    u_t = ser(b * hbar ** 2)

    # Q_beta^GS/Q_A - 1 leading term is +t^2 (cosh-like), coeff exactly 1
    check("W2_gs_ratio_leading_is_plus_hbar2_coshlike",
          ratio_A.coeff(t, 2) == 1 and ratio_A.coeff(t, 1) == 0,
          f"Q_beta^GS/Q_A - 1 = {ratio_A.coeff(t,2)}*t^2 {ratio_A.coeff(t,3)}*t^3 ...")
    # u ~ (sqrt(3)/2) t^2, so u^2 ~ O(t^4). The ladder sum_{k>=2} c_k u^k starts at t^4.
    check("W2_ladder_variable_u_is_order_hbar2",
          u_t.coeff(t, 1) == 0 and u_t.coeff(t, 2) != 0,
          f"u = {u_t.coeff(t,2)}*t^2 + ...  => u^2 ~ O(t^4)")
    # KILL: the residual Q_beta^GS/Q_N1 - 1 has a NONZERO t^2 (=O(u)) term,
    # below the c_2 u^2 (t^4) rung => not of pure ladder shape.
    resid_t2 = sp.nsimplify(resid.coeff(t, 2))
    check("W2_KILL_residual_has_order_u_term_below_c2_rung",
          resid_t2 != 0,
          f"Q_beta^GS/Q_N1 - 1 has [t^2]={resid_t2} (=O(u)) != 0; c_2 u^2 lives at O(t^4)")

    # ---- accuracy: full GS net is WORSE than the N=0 truncation ----
    try:
        import mpmath as mp
        mp.mp.dps = 40
        # Centralized constants (precision-safe) rather than hard-coded literals.
        from qou_substrate.constants import q_at
        from computations.substrate import codata_constants as C
        q0 = q_at(40)                                  # proton-pinned substrate q₀
        me = mp.mpf(str(C.M_E_MEV))
        Qcod = mp.mpf(str(C.Q_BETA_MEV))
        ratioA_f = sp.lambdify(q, sp.cancel(dnet / counit), "mpmath")
        Q_A = me * abs(q0 ** 2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0 ** 3)
        err_N0 = float((Q_A / Qcod - 1) * 100)
        err_GS = float((Q_A * abs(ratioA_f(q0)) / Qcod - 1) * 100)
        check("W2_full_gs_worse_than_N0_truncation",
              abs(err_GS) > abs(err_N0),
              f"N=0 Q_A err={err_N0:.3f}%  vs  full-GS err={err_GS:.3f}% (worse)")
    except Exception as e:  # pragma: no cover
        skip("W2_full_gs_worse_than_N0_truncation",
             f"mpmath/constants unavailable ({type(e).__name__}); symbolic W2 stands")

    ran = [a for a in assertions if not a["skipped"]]
    skipped = [a for a in assertions if a["skipped"]]
    all_ran_passed = all(a["passed"] for a in ran)
    all_ran = len(skipped) == 0
    all_passed = all_ran_passed and all_ran   # green only if every gate actually ran
    if skipped:
        print(f"  NOTE: {len(skipped)} gate(s) SKIPPED (env) -> not fully green: "
              + ", ".join(a["name"] for a in skipped))
    verdict = (
        "W1 PASS + W2 KILL (scope-(a)). The first-principles categorical Q_beta net "
        "-- the augmentation Delta(net) of the H_3 GS-reduced nucleon NF -- reproduces "
        "the counit through O(hbar^2) (W1), but the FULL GS net is NOT the production "
        "cos*(1 + c_k u^2) ladder: Q_beta^GS/Q_A = 1 + hbar^2 - 2 hbar^3 - ... is "
        "cosh-like (leading +hbar^2), and Q_beta^GS/Q_N1 - 1 carries a leading "
        "O(hbar^2)=O(u) term (coeff 9/8) BELOW the c_2 u^2 (O(hbar^4)) rung, so it is "
        "not of pure ladder shape. Numerically the full GS net gives Q_beta = +0.75% vs "
        "CODATA, WORSE than the N=0 truncation Q_A (+0.17%): the categorical higher "
        "orders push away from the ladder. scope-(a): this refutes the hypothesis "
        "'full GS augmentation == production ladder', NOT the ladder ansatz or any c_k. "
        "W3 (c_2 reproduction) is moot under this kill. NO c_k value; nothing wired."
        + ("" if all_ran else
           f"  [NOTE: {len(skipped)} numeric cross-check(s) skipped in this env; "
           "the symbolic W1/W2 gates that ran carry the finding.]")
        if all_ran_passed else
        "INCONCLUSIVE -- a gate assertion that RAN failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-crossing-weight-hecke",
        "description": "W1/W2 gates for the independent Q_beta crossing-weight determination "
                       "from the H_3 GS reducer. W1 PASS (counit reproduction); W2 KILL "
                       "(full GS augmentation is not the production cos*(1+c_k u^2) ladder; "
                       "disagrees at O(u), +0.75% vs +0.17% N=0). scope-(a).",
        "audit_only": True,
        "tier": "structural-exact (symbolic; + numeric cross-checks; no fit, no CODATA in the algebra)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "allRan": all_ran,
        "ranPassed": all_ran_passed,
        "skippedCount": len(skipped),
        "result": {
            "Q_beta_GS_over_Q_A_minus_1": str(sp.expand(ratio_A - 1)),
            "Q_beta_GS_over_Q_N1_minus_1": str(resid),
            "u_of_hbar": str(u_t),
            "verdict": verdict,
        },
        "context": {
            "scope": "docs/scope/2026-07-07-qbeta-crossing-weight-hecke-determination.md (PR #3477)",
            "builds_on": "KC19 (PR #3473) crossing-weight affine narrowing",
            "gs_reducer": "computations/qbeta/qbeta_h4_nucleon_assembly.py (reproduces free-neutron-decay witness)",
            "production_ladder": "computations/qbeta/qbeta_utils.py (Q_A, Q_N1, u, c3_target_at)",
            "flip_flop_guard": "registry section 8 -- no c_k wired",
        },
    }
    out = os.path.join(_HERE, "qbeta-crossing-weight-hecke.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("=== Q_beta crossing-weight from H_3 GS reducer (W1/W2) ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    # Exit 0 iff every gate that RAN passed (the finding holds); skipped numeric
    # cross-checks are surfaced via witness allRan/skippedCount, not hidden.
    return 0 if all_ran_passed else 1


if __name__ == "__main__":
    sys.exit(main())
