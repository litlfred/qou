#!/usr/bin/env python3
"""
LOCATE the Δ_λ chirality sign: it is a cyclotomic (q=i, NON-SEMISIMPLE H_n) fibre
signature -- structurally invisible to every real-q_0 construction.

Follows the T(2,5) sign probe (t25_cinquefoil_deltalambda_sign_probe.py), which
found: the chiral T(2,5) character produces mixed signs (selection rule confirmed)
but is not the exact Δ_λ sign map, and NO real-q re-framing helps because the twist
θ_λ = q^{2(n(λ')-n(λ))} > 0 at real q_0.

This probe pins WHERE the sign lives. The target simplifies exactly to

    sgn(Δ_λ) = sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)},    n(λ) = Σ_i (i-1)λ_i,

and (-1)^{n(λ)} = (q^2)^{n(λ)} |_{q^2 = -1} = q^{2 n(λ)} |_{q=i}. So the sign is a
value at q = i, a primitive 4th root of unity -- which is a NON-SEMISIMPLE point of
H_n(q) for n ≥ 4 ([2]_q = q + q^{-1} = 0 at q=i; the seminormal 1/[d] entries have
poles when q^{2d}=1). At real q_0 > 0 the same object q^{2 n(λ)} is strictly
POSITIVE (no sign). So:

  * the chirality sign is a CYCLOTOMIC / non-semisimple degeneration signature
    (the fibre / Im(q)≠0 level), NOT an archimedean real-q>0 quantity;
  * this UNIFIES why every real-q Δ_λ ansatz fails on the sign (positive-combination
    ansätze: SelectionRules.nonneg_sum_ne_neg_target; re-framed traces: θ_λ>0), and
    mirrors the c_3 fibre-vs-archimedean split (AGENTS.md Im(q) banner);
  * OPEN (not claimed): the exact chiral operator whose per-λ character realizes
    q^{2 n(λ)}, and the magnitude |Δ_λ| = dim(λ). This LOCATES the sign; it does not
    derive Δ_λ. NOTHING wired.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from t25_cinquefoil_deltalambda_sign_probe import (  # noqa: E402
    partitions, conjugate, target_sign)
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def n_lambda(lam):
    return sum(i * p for i, p in enumerate(lam))


def main():
    q = sp.I                                  # q = i, primitive 4th root of unity
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # 1) target = (-1)^{n(λ)} = q^{2 n(λ)} at q=i, for all λ⊢{3,5,6}
    ok_all = True
    for N in (3, 5, 6):
        for lam in partitions(N):
            lhs = target_sign(lam)
            rhs = int(sp.simplify(sp.I ** (2 * n_lambda(lam))).as_real_imag()[0])
            if lhs != rhs:
                ok_all = False
    check("target_equals_q2n_at_qi", ok_all,
          "sgn(w_0^{S_{λ'}}) = (-1)^{n(λ)} = q^{2n(λ)}|_{q=i}, all λ⊢{3,5,6}")

    # 2) q=i is a NON-SEMISIMPLE point of H_n (n≥4): [2]_q = q+q^{-1} = 0 at q=i,
    #    and the seminormal 1/[d] entries have poles when q^{2d}=1 (d=2: q^4=1).
    two_q = sp.simplify(sp.I + 1 / sp.I)
    check("bracket2_vanishes_at_qi", two_q == 0,
          f"[2]_q = q + q^{{-1}} = {two_q} at q=i  =>  H_n non-semisimple for n≥2·(via [2]) ")
    # axial distance d=2 occurs in λ⊢5 (=> a genuine seminormal pole at q=i)
    d2_pole = sp.simplify(1 - sp.I ** (-2 * 2))      # 1 - q^{-2d}, d=2, q=i
    check("seminormal_denominator_vanishes_d2_qi", d2_pole == 0,
          f"1 - q^{{-2·2}} = {d2_pole} at q=i  =>  seminormal M_tt pole (H_5 non-semisimple, ℓ=4≤5)")

    # 3) at real q_0 > 0 the SAME object q^{2n(λ)} is strictly positive -> NO sign.
    #    The chirality sign exists ONLY at the cyclotomic point, not archimedean.
    q0 = sp.Rational(11, 10)                          # any real q>1
    pos_all = all(sp.N(q0 ** (2 * n_lambda(lam))) > 0 for lam in partitions(5))
    signs_absent = all(int(sp.sign(sp.N(q0 ** (2 * n_lambda(lam))))) == 1
                       for lam in partitions(5))
    check("q2n_positive_at_real_q0_no_sign", pos_all and signs_absent,
          "q^{2n(λ)} > 0 for all λ⊢5 at real q_0>0  =>  sign is invisible archimedean")

    # 4) the mixed sign IS present at q=i (it is exactly the target) -> non-trivial
    signs = [target_sign(lam) for lam in partitions(5)]
    mixed = (1 in signs) and (-1 in signs)
    check("sign_mixed_at_cyclotomic_point", mixed,
          f"q^{{2n(λ)}}|_{{q=i}} over λ⊢5 = {signs} (mixed: {signs.count(1)}+/{signs.count(-1)}-)")

    # 5) REALIZABILITY of the carrier q^{2n(λ)} as a canonical central operator.
    #    center(H_n) = symmetric functions of the JM elements, whose scalar on V_λ is
    #    a function of the content multiset {q^{2c(box)}}. If the content multiset
    #    determines λ (=> determines n(λ)), then q^{2n(λ)} IS such a central character
    #    (realizable by a JM/framing element), not merely the abstract central idempotent.
    def contents(lam):
        return tuple(sorted(c - r for r, row in enumerate(lam) for c in range(row)))
    collision_free = True
    for N in range(2, 9):
        seen = {}
        for lam in partitions(N):
            seen.setdefault(contents(lam), []).append(lam)
        if any(len(v) > 1 for v in seen.values()):
            collision_free = False
    check("carrier_is_a_JM_central_character_realizable", collision_free,
          "content multiset determines λ (no collision, n≤8) => q^{2n(λ)} is a central "
          "character realizable by JM symmetric functions, not just the abstract projector")

    # 6) the carrier is NOT a framing power: neither the full twist θ_λ=q^{2(n(λ')-n(λ))}
    #    nor the framing/half-twist sqrt θ_λ^{1/2}=q^{n(λ')-n(λ)} reproduces the sign at q=i.
    #    (θ|_{q=i}=i^{2cs} misses λ=[3,1,1],[2,1,1,1]; θ^{1/2}|_{q=i}=i^{cs} is often ±i, not ±1.)
    #    So the sign carrier is a genuine JM-symmetric central element, not any framing power.
    def cont_sum(lam):
        return n_lambda(conjugate(lam)) - n_lambda(lam)
    ft_fail = any(int(sp.re(sp.I ** (2 * cont_sum(lam)))) != target_sign(lam)
                  for lam in partitions(5))
    ht_fail = any((sp.im(sp.I ** cont_sum(lam)) != 0)
                  or (int(sp.re(sp.I ** cont_sum(lam))) != target_sign(lam))
                  for lam in partitions(5))
    check("carrier_is_not_a_framing_power", ft_fail and ht_fail,
          "sign ≠ full twist θ_λ (fails λ=[3,1,1],[2,1,1,1]) AND ≠ framing sqrt θ_λ^{1/2} "
          "(i^{cs} often ±i) => a genuine JM-symmetric central element, not a framing power; "
          "exact braid form + |Δ_λ|=dim open")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "LOCATED (structural; nothing derived): the Δ_λ chirality sign is a CYCLOTOMIC "
        "fibre signature. sgn(Δ_λ)=sgn(w_0^{S_{λ'}})=(-1)^{n(λ)}=q^{2n(λ)}|_{q=i}, and "
        "q=i is a NON-SEMISIMPLE point of H_5 ([2]_i=0; the seminormal 1/[d] poles hit at "
        "d=2). At real q_0>0 the same object q^{2n(λ)} is strictly positive -- no sign. So "
        "the chirality lives precisely at the non-semisimple cyclotomic degeneration (the "
        "fibre / Im(q)≠0 level), invisible to every real-q_0 construction. This UNIFIES the "
        "Δ_λ real-q failures (positive combos: nonneg_sum_ne_neg_target; re-framed traces: "
        "θ_λ>0) and mirrors the c_3 fibre-vs-archimedean split (Im(q) banner). OPEN, NOT "
        "claimed: the exact chiral operator realizing q^{2n(λ)}, and the magnitude "
        "|Δ_λ|=dim. Locates the sign; does not derive Δ_λ. NOTHING wired."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_HERE, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "deltalambda-sign-cyclotomic-locus",
        "description": "The Δ_λ chirality sign sgn(w_0^{S_{λ'}})=(-1)^{n(λ)}=q^{2n(λ)}|_{q=i} "
                       "is a cyclotomic (q=i, non-semisimple H_5) fibre signature -- absent at "
                       "real q_0 (q^{2n(λ)}>0). Locates the sign; does not derive Δ_λ.",
        "auditOnly": "docs/audits/2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md",
        "tier": "symbolic-exact (sympy; algebraic identities at q=i and real q_0)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "target_closed_form": "(-1)^{n(λ)} = q^{2n(λ)}|_{q=i}",
            "cyclotomic_point": "q = i (primitive 4th root); [2]_i = 0; non-semisimple H_n, n≥4",
            "real_q_sign": "q^{2n(λ)} > 0 (no sign) -- archimedean-invisible",
            "verdict": verdict,
        },
        "context": {
            "follows": "t25_cinquefoil_deltalambda_sign_probe.py (framing prune)",
            "selection_rule": "QOU.SelectionRules.nonneg_sum_ne_neg_target",
            "target_source": "Lean deltaSign_mixed (QOU.BraidsAndKnots.S5SO3FiberAction.PartitionOf5)",
            "open": "exact chiral operator realizing q^{2n(λ)}; magnitude |Δ_λ|=dim (Track A)",
            "gate": "Δ_λ gate -- structural locating result, no fit, nothing wired",
        },
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    # Payload carries a top-level `assertions` mapping → stamp preserves it.
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = os.path.basename(__file__)
    out = os.path.join(_HERE, "deltalambda-sign-cyclotomic-locus.witness.json")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial. `os.replace` is atomic on POSIX within a
    # filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
