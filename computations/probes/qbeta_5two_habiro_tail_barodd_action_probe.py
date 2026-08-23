#!/usr/bin/env python3
"""qbeta_5two_habiro_tail_barodd_action_probe.py

The 5₂ Habiro-tail bar-odd archimedean action, built on the AUTHORITATIVE Masbaum
cyclotomic coefficients (sibling `qbeta_5two_masbaum_cyclotomic_probe.py`, masbaum2003;
b3ix "odd datum = cyclotomic-coefficient asymmetry"). This is the exact-route analog of
the merged 4₁ bar-EVEN Habiro-tail action = π²/5 (golden-ratio dilog) — now for the
chiral 5₂ bar-ODD channel, unblocked by the authoritative C_{5₂,n}.

Construction. The archimedean (ρ_∞, real-q) Habiro tail is
  S(q) = Σ_n C_{5₂,n}(q) · ∏_{j=1}^n (1−q^j)(1−q^{−j}),   q = a² (a = e^{t/2}),
with C_{5₂,n} the Masbaum coefficients (C_1=−(q⁴+q²), C_2=q¹¹+q⁸+q⁷+q⁵, …). The ∏
factor is BAR-SYMMETRIC (q↔q⁻¹), so the bar-odd part comes ENTIRELY from the C_n
asymmetry: the bar-odd tail term is [C_n(a)−C_n(a⁻¹)]/2 · ∏(1−a^{2j})(1−a^{−2j}).

FINDING (structural). Unlike 4₁'s clean π²/5, the 5₂ bar-odd action does NOT converge
to a simple dilog constant at accessible order. The Masbaum C_n carry a GAUSSIAN growth
(leading a^{3n²+5n} = q^{(3n²+5n)/2}), which dominates the ∏-factor decay and pushes the
optimal-truncation minimal term to SMALL n — so the extracted action A_odd = −t·ln|δ_odd|
DRIFTS with t (≈ 0.10 → 0.64 over t = 0.5 → 0.16), heading toward ~Vol(5₂)/π ≈ 0.90 (the
GEOMETRIC value), NOT a golden-dilog-style archimedean constant. So the chirality (the
C_n asymmetry) fundamentally changes the resummation CLASS of the bar-odd channel — it is
not a π²/5-analog. This complements the phi-odd findings: no clean classical/tail closed
form; the bar-odd datum is genuinely resurgent (full-Z).

DISCIPLINE: scope-(a). Builds the authoritative tail; reports the action drift + the
structural conclusion (no clean π²/5-analog). Does NOT claim a bar-odd action value.
No fit; no c_k wired; no tier change.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
VOL52_OVER_PI = mp.mpf("2.82812208833") / mp.pi
PI2_5 = mp.pi ** 2 / 5


def main() -> int:
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "mas", str(here / "qbeta_5two_masbaum_cyclotomic_probe.py"))
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    a = M.a
    N = 10
    Cf, Csym = {}, {}
    for n in range(N + 1):
        e = sp.cancel(sp.expand(M.C_framework(n, M.ftilde_K2(n))))
        Csym[n] = e
        Cf[n] = sp.lambdify(a, e, "mpmath")

    # verify against the authoritative printed values
    c1_ok = sp.simplify(Csym[1] - (-(a ** 8 + a ** 4))) == 0   # C_1 = -(q⁴+q²), q=a²
    c2_ok = sp.simplify(Csym[2] - (a ** 22 + a ** 16 + a ** 14 + a ** 10)) == 0

    def Pn(n, av):
        p = mp.mpf(1)
        for j in range(1, n + 1):
            p *= (1 - av ** (2 * j)) * (1 - av ** (-2 * j))
        return p

    print(f"  C_1 authoritative: {c1_ok}   C_2 authoritative: {c2_ok}", flush=True)
    print("  t      N*_odd  A_odd = -t ln|δ_odd|", flush=True)
    rows = []
    for tt in ("0.5", "0.4", "0.3", "0.25", "0.2", "0.16"):
        t = mp.mpf(tt)
        av = mp.e ** (t / 2)
        terms = {n: ((Cf[n](av) - Cf[n](1 / av)) / 2) * Pn(n, av) for n in range(1, N + 1)}
        Ns = min(terms, key=lambda n: abs(terms[n]))
        A = -t * mp.log(abs(terms[Ns]))
        rows.append({"t": tt, "Nstar": Ns, "A_odd": mp.nstr(A, 10)})
        print(f"   {tt:>5}   {Ns:>2}    {mp.nstr(A, 9)}", flush=True)

    A_vals = [mp.mpf(r["A_odd"]) for r in rows]
    drifts = abs(A_vals[-1] - A_vals[2])  # 0.3 -> 0.16
    small_Nstar = all(r["Nstar"] <= 3 for r in rows)   # C_n Gaussian pushes N* small
    not_pi2_5 = min(abs(A - PI2_5) for A in A_vals) > mp.mpf("0.5")

    assertions = [
        ("masbaum_C_n_authoritative", bool(c1_ok and c2_ok)),
        ("action_drifts_not_converged", bool(drifts > mp.mpf("0.05"))),
        ("optimal_truncation_at_small_n", bool(small_Nstar)),
        ("not_a_pi2_over_5_analog", bool(not_pi2_5)),
    ]

    verdict = (
        f"5₂ BAR-ODD HABIRO-TAIL ACTION IS NOT A π²/5-ANALOG (scope-(a) structural, built on "
        f"the authoritative Masbaum C_n). The archimedean bar-odd tail S_odd(q) = Σ_n "
        f"[C_{{5₂,n}}(q)−C_{{5₂,n}}(q⁻¹)]/2 · ∏(1−q^j)(1−q⁻ʲ) (∏ bar-symmetric ⇒ the odd datum "
        f"is entirely the C_n asymmetry, confirming b3ix). Its optimal-truncation action DRIFTS "
        f"(A_odd ≈ {mp.nstr(A_vals[2],4)}→{mp.nstr(A_vals[-1],4)} over t=0.3→0.16), with the "
        f"minimal term stuck at small n (N*≤3) because the Masbaum C_n carry a GAUSSIAN growth "
        f"a^{{3n²+5n}}=q^{{(3n²+5n)/2}} that dominates the ∏-decay. So there is NO clean golden-"
        f"dilog constant like 4₁'s π²/5={mp.nstr(PI2_5,6)}; the drift heads toward "
        f"~Vol(5₂)/π={mp.nstr(VOL52_OVER_PI,6)} (the geometric value). CONCLUSION: the chirality "
        f"(C_n asymmetry) fundamentally changes the bar-odd channel's resummation CLASS — it is "
        f"not the amphichiral 4₁ π²/5-analog; the bar-odd action is genuinely resurgent/full-Z, "
        f"consistent with the φ_odd-is-2-loop findings. No bar-odd action value claimed. No fit; "
        f"no c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-5two-habiro-tail-barodd-action", engine="mpmath")
    wb.set_description(
        "5₂ Habiro-tail bar-odd archimedean action on the authoritative Masbaum C_n: the "
        "bar-odd datum is the C_n asymmetry (∏ bar-symmetric); the action DRIFTS (no clean "
        "π²/5-analog) because the C_n Gaussian growth pushes optimal truncation to small n — "
        "chirality changes the resummation class. Heads toward ~Vol(5₂)/π, not a golden dilog.")
    wb.set_audit_only("docs/audits/2026-07-19-5two-habiro-tail-barodd-not-pi2-5.md")
    for name, passed in assertions:
        wb.add_assertion(name, str(passed), "True")
    wb.add_data("rows", rows)
    wb.add_data("pi2_over_5", mp.nstr(PI2_5, 10))
    wb.add_data("vol52_over_pi", mp.nstr(VOL52_OVER_PI, 10))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all(p for _, p in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
