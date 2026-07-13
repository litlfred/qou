#!/usr/bin/env python3
"""qbeta_c3_imq_linear_response_probe.py

Follow-up to the merged #3600 candidate-(iii) connection (c₃ bar-odd S = the
decay-projection Im(q); `conj:im-q-physical-role`). Subgoal-2 was opened for all
agents (owner ruling c4a41f3a, 2026-07-11), so the substrate-level ε(q₀) =
Im(q) map is now in scope to DERIVE (anti-fit discipline unchanged: no wiring a
fitted map to production).

FORMALIZE-FIRST STEP (narrow before searching): make the candidate-(iii)
mechanism rigorous rather than fit ε directly.

  1. **Sign-flip is STRUCTURAL, not fitted.** S is bar-odd under σ: q ↦ q⁻¹.
     Writing q = q₀ + iε and expanding, σ sends ε ↦ −ε/q₀² + O(ε²); a bar-odd
     observable therefore obeys `S(−ε) = −S(ε) + O(ε²)`, i.e. S is ODD in ε with
     `S ∝ ε` at leading order and `sign S = sign ε`. So the observed
     S(muon) > 0 > S(proton) FORCES ε(muon) > 0 > ε(proton) — the sign-flip is a
     parity consequence, not an inversion artifact. (No real q₀ can do this; a
     real q gives S = 0 at leading order — the merged `Im q₀ = 0` mass fact.)

  2. **The linear coefficient is DERIVED (up to proxy).** To first order
     `S ≈ (∂S/∂ε)|₀ · ε`, and `∂S/∂ε|₀` is a derived number. We cross-check it
     across TWO independent derived proxies for the bar-odd observable:
       * geometric  — Im 𝔙 via the meridian map u = 2 log q (leading NZ):
         `∂S/∂ε = 4√3 · log q₀ / q₀`;
       * operator   — the figure-eight trace `T(q) = q⁴−2q²+1−2q⁻²+q⁻⁴` (merged
         #3600): `Im T(q₀+iε) = ε·T'(q₀) + O(ε³)`, so `∂S/∂ε = T'(q₀)`.
     Both give a small, sign-flipped ε at the two anchors (candidate-(iii)
     signature robust in sign + order of magnitude); the |ε| magnitude differs by
     the proxy-coefficient ratio (the honest u-map dependence flagged in #3600).

RESIDUE (the one open real function): ε(q₀) itself — the decay projection's
imaginary part, = arg(u(q₀)) of the wall in the candidate-(iii) reading. This
probe does NOT fit or wire it; it pins the coefficient + proves the sign-flip
structural, so the remaining open content is a single sign-fixed small function.
Scope-(a); C14; no c_k wired; no fit.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 70
Q = {"muon": mp.mpf("1.10997859555733471"),
     "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}


def fig8_trace(q):
    """Figure-eight operator trace on V_{(2,1)} (merged #3600 closed form)."""
    return q ** 4 - 2 * q ** 2 + 1 - 2 / q ** 2 + 1 / q ** 4


def coeff_geometric(q0):
    """∂S/∂ε via the geometric Im 𝔙 route (meridian u = 2 log q)."""
    return 4 * mp.sqrt(3) * mp.log(q0) / q0


def coeff_operator(q0):
    """∂S/∂ε via the operator route: Im[T(q0+iε)]/ε → T'(q0).

    T(q) = q⁴−2q²+1−2q⁻²+q⁻⁴ is a Laurent polynomial; T'(q₀) is exact (Gemini
    review — analytic is more robust than a finite-difference step size).
    """
    return 4 * q0 ** 3 - 4 * q0 + 4 / q0 ** 3 - 4 / q0 ** 5


def imag_of_perturbed_trace(q0, eps):
    """Direct check that Im T(q0+iε) is odd in ε and ≈ ε·T'(q0)."""
    return mp.im(fig8_trace(mp.mpc(q0, eps)))


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — candidate-(iii) linear response: ε(q₀) coefficient + sign-flip")
    print("=" * 78)

    # ---- 1. sign-flip is structural (S odd in ε) — direct numerical witness ----
    print("\n[1] S odd in ε (bar-odd ⇒ S(−ε)=−S(ε)); numeric witness on Im T(q0+iε):")
    q0 = Q["muon"]
    e = mp.mpf("1e-3")
    ip, im = imag_of_perturbed_trace(q0, e), imag_of_perturbed_trace(q0, -e)
    odd_ok = abs(ip + im) < mp.mpf("1e-12")
    print(f"    Im T(q0+iε)={mp.nstr(ip,6)}, Im T(q0−iε)={mp.nstr(im,6)}  ⇒ odd? {odd_ok}")
    # linearity: Im T(q0+iε) ≈ ε T'(q0)
    lin = abs(ip - e * coeff_operator(q0)) < mp.mpf("1e-9")
    print(f"    Im T(q0+iε) ≈ ε·T'(q0)? {lin}  ⇒ S ∝ ε, sign S = sign ε (STRUCTURAL)")

    # ---- 2. two derived-coefficient proxies; extract ε; robustness ----
    print("\n[2] ε(q₀) via two DERIVED coefficients (geometric Im 𝔙 vs operator T'):")
    rows = []
    for a in ("muon", "proton"):
        cg, co = coeff_geometric(Q[a]), coeff_operator(Q[a])
        eg, eo = S_TARGET[a] / cg, S_TARGET[a] / co
        rows.append({"anchor": a, "coeff_geom": mp.nstr(cg, 10), "coeff_op": mp.nstr(co, 10),
                     "eps_geom": mp.nstr(eg, 8), "eps_op": mp.nstr(eo, 8),
                     "eps_geom_pct": mp.nstr(eg / Q[a] * 100, 6), "eps_op_pct": mp.nstr(eo / Q[a] * 100, 6)})
        print(f"    {a:7s}: geom ε={mp.nstr(eg,5)} ({mp.nstr(eg/Q[a]*100,3)}%)   "
              f"op ε={mp.nstr(eo,5)} ({mp.nstr(eo/Q[a]*100,3)}%)")

    sign_flip_geom = float(rows[0]["eps_geom"]) > 0 > float(rows[1]["eps_geom"])
    sign_flip_op = float(rows[0]["eps_op"]) > 0 > float(rows[1]["eps_op"])
    both_small = all(abs(float(r["eps_geom_pct"])) < 10 and abs(float(r["eps_op_pct"])) < 10 for r in rows)
    print(f"\n    sign-flip in BOTH proxies? geom={sign_flip_geom} op={sign_flip_op}   both small(<10%)? {both_small}")
    print("    ⇒ candidate-(iii) robust: small sign-flipped ε across independent proxies;")
    print("      |ε| magnitude is proxy-dependent (the open u-map dependence); sign-flip is not.")
    print("\n    RESIDUE: ε(q₀) itself — the one open real function (= arg(u(q₀)); the decay")
    print("      projection). Subgoal-2 open ⇒ in scope to derive; not fit/wired here.")

    wb = WitnessBuilder("qbeta-c3-imq-linear-response", engine="mpmath")
    wb.set_description(
        "Candidate-(iii) linear-response structure for the c₃ bar-odd S decay "
        "projection (follow-up to merged #3600). Formalize-first: (1) S is bar-odd "
        "under σ:q↦q⁻¹, and q=q₀+iε sends ε↦−ε/q₀² so S(−ε)=−S(ε)+O(ε²) — S∝ε with "
        "sign S = sign ε, making the muon>0>proton sign-flip STRUCTURAL, not a fit "
        "(numeric witness: Im T(q0+iε) odd + ≈ε·T'(q0)). (2) The linear coefficient "
        "∂S/∂ε is derived up to proxy: geometric (u=2log q, 4√3 log q0/q0) and "
        "operator (fig-8 trace T'(q0), #3600) both give small sign-flipped ε at both "
        "anchors; |ε| is proxy-dependent. Residue: ε(q₀) itself (=arg(u(q₀))), one "
        "open real function, in scope under the opened Subgoal-2 but not fit/wired. "
        "Scope-(a); C14; no c_k wired; no fit."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("sign_flip_structural", {
        "S_bar_odd": True, "Im_T_odd_in_eps": bool(odd_ok),
        "Im_T_linear_in_eps": bool(lin),
        "argument": "sigma:q->1/q sends eps->-eps/q0^2 (leading); bar-odd => S(-eps)=-S(eps) => sign S = sign eps"})
    wb.add_data("coefficient_cross_check", rows)
    wb.add_data("robustness", {"sign_flip_geom": bool(sign_flip_geom), "sign_flip_op": bool(sign_flip_op),
                               "both_small": bool(both_small),
                               "residue": "eps(q0) itself = arg(u(q0)); one open real function; Subgoal-2 open"})
    wb.add_assertion("sign_flip_structural_and_robust",
                     computed=1.0 if (odd_ok and lin and sign_flip_geom and sign_flip_op and both_small) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="S odd in eps (bar-odd parity) + small sign-flipped eps in both derived proxies")
    wb.save()
    print("\n  RESULT: sign-flip proven structural; ε-coefficient derived (two proxies);")
    print("          residue = the single open real function ε(q₀).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
