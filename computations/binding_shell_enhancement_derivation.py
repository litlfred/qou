#!/usr/bin/env python3
"""
binding_shell_enhancement_derivation.py — can a DERIVED per-magic-shell
enhancement close A≥3 binding on top of the scalar endomorphism?
(Derive-or-refute. No AME fitting — only substrate-derived constants.)

CONTEXT. The scalar mass-endomorphism analogue
    B_endo(K) = m_e · Vol(𝓑₃) · Δtr,   Δtr = |tr_M(free)| − |tr_M(atom)|
is EXACT for the deuteron (+0.19%, zero parameters; Vol(𝓑₃)=8G derived)
but undershoots A≥3 by ~60% because Δtr is INTENSIVE (it saturates) while
binding is EXTENSIVE. The paper's shell theory says the missing extensive
piece is the inter-shell torus-knot gap |λ₊/λ₋| = q^{2n_s}
(torus-knot-shell-binding.md). This script tests whether that — or any
single DERIVED q-quantity — supplies the enhancement, evaluated as
    B(K) = B_endo(K) · f^{n_closures(K)},
where n_closures = #{magic-2 shell closures} (D:0, T:1, ³He:1, ⁴He:2)
and f is a DERIVED candidate (never fitted to AME).

RESULT (honest refutation + structural finding):
  1. B_endo is exact for D (resid 0.998) — the deuteron is derived.
  2. The enhancement actually needed is ~multiplicative per closure,
     f ≈ 2.45–2.88 (17% spread).
  3. The torus-knot gap q^{2n_s} is REFUTED: q⁴ (n_s=2 nucleons) = 1.518
     is far too small (T −46%, ⁴He −72%); q¹² (n_s=6 strands) = 3.50 is
     too big (+24%/+48%). No clean q-power lands at ~2.7.
  4. [3]_q = 3.044 is the closest single derived quantity (T +8%,
     ⁴He +12%) but misses ³He by +24%.
  5. THE KILLER (structural): T (neutron shell closed, f=2.82) ≠
     ³He (proton shell closed, f=2.45) — both are A=3 with one magic
     closure, yet differ by 15%. The enhancement is proton/neutron
     ASYMMETRIC; no p/n-blind q-factor f can produce it. So a single
     derived scalar enhancement cannot close A≥3 — the missing
     structure must carry the p/n distinction (as binding_canonical's
     Δtr already does via pp/nn/pn interface factors, the shell
     enhancement must too).

CONCLUSION. The simplest derived inter-shell candidate (torus-knot
q^{2n_s}) is refuted, and the p/n asymmetry rules out ANY scalar
q-factor. This narrows the open A≥3 problem to a p/n-asymmetric,
per-magic-closure enhancement — stated without fitting. The honest
status remains: deuteron derived; A≥3 open.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs, catalan, sqrt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    Q_BETA_MEV,
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from binding_canonical import binding_canonical  # noqa: E402


def _real(s):
    # Full-precision real part — never via float64 complex() (precision ban).
    s = str(s).strip("()")
    try:
        return mpf(s)
    except (ValueError, TypeError):
        body = s[:-1] if s.endswith("j") else s
        for i in range(len(body) - 1, 0, -1):
            if body[i] in "+-" and body[i - 1] not in "eE":
                return mpf(body[:i] or "0")
        return mpf("0")


def main():
    set_compute_dps()
    wb = WitnessBuilder("binding-shell-enhancement-derivation", engine="mpmath")

    q = Q_MP
    m_e = mpf(str(M_E_MEV))
    VOL_B3 = 8 * catalan

    def br(n):
        return (q**n - q**-n) / (q - q**-1)  # [n]_q

    AME = {
        "D": float(AME_B_DEUTERON_MEV_VALIDATION),
        "T": float(AME_B_TRITIUM_MEV_VALIDATION),
        "3He": float(AME_B_HE3_MEV_VALIDATION),
        "4He": float(AME_B_HE4_MEV_VALIDATION),
    }
    cases = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
    # magic-2 shell closures: a proton (Z≥2) and/or neutron (N≥2) shell
    n_close = {"D": 0, "T": 1, "3He": 1, "4He": 2}

    # B_endo and the residual enhancement each atom needs
    endo = {}
    for iso, Z, N in cases:
        # Q_β value is irrelevant here (we use the q-only traces, not the
        # B output), but use the canonical high-precision constant per the
        # E_0/Q_β calibration discipline.
        r = binding_canonical(Z, N, Q_beta_n_mev=float(Q_BETA_MEV),
                              use_closed_form=True, verbose=False)
        dtr = fabs(_real(r["tr_M_free"])) - fabs(_real(r["tr_M_atom"]))
        B_endo = m_e * VOL_B3 * dtr
        resid = mpf(str(AME[iso])) / B_endo
        endo[iso] = {"dtr": dtr, "B_endo": B_endo, "resid": resid,
                     "n_close": n_close[iso]}

    print("=" * 72)
    print("SHELL-ENHANCEMENT DERIVATION  B = m_e·Vol(𝓑₃)·Δtr · f^{n_closures}")
    print("=" * 72)
    print(f"{'atom':5s}{'Δtr':>9s}{'B_endo':>10s}{'B_AME':>9s}"
          f"{'resid':>9s}{'closures':>10s}{'f/closure':>11s}")
    f_needed = {}
    for iso, _, _ in cases:
        d = endo[iso]
        f = (d["resid"] ** (mpf(1) / d["n_close"])) if d["n_close"] else mpf(1)
        f_needed[iso] = f
        print(f"{iso:5s}{float(d['dtr']):>9.4f}{float(d['B_endo']):>10.4f}"
              f"{AME[iso]:>9.3f}{float(d['resid']):>9.4f}"
              f"{d['n_close']:>10d}{float(f):>11.4f}")

    fs = [float(f_needed[i]) for i in ["T", "3He", "4He"]]
    f_spread = (max(fs) / min(fs) - 1) * 100
    print(f"\nf needed per closure: {min(fs):.3f}–{max(fs):.3f} "
          f"({f_spread:.0f}% spread, ~multiplicative).")
    print(f"p/n asymmetry: T (n-shell, f={float(f_needed['T']):.3f}) ≠ "
          f"³He (p-shell, f={float(f_needed['3He']):.3f}) "
          f"— same A=3, one closure each.")

    # Derived candidates for f (NO fit)
    cands = {
        "q^2": q**2, "q^4 (torus-knot gap n_s=2)": q**4, "q^6": q**6,
        "q^12 (n_s=6 strands)": q**12, "[2]_q": br(2), "[3]_q": br(3),
        "Vol(B3)/[3]_q": VOL_B3 / br(3),
    }
    print("\nDERIVED candidates  B = B_endo · f^{closures}  (no fit):")
    print(f"{'f candidate':28s}{'value':>8s}   "
          + "  ".join(f"{i:>5s}" for i, _, _ in cases))
    cand_results = {}
    best_name, best_maxabs = None, None
    for name, f in cands.items():
        errs = {}
        for iso, _, _ in cases:
            Bp = endo[iso]["B_endo"] * (f ** endo[iso]["n_close"])
            errs[iso] = float((Bp - mpf(str(AME[iso]))) /
                              mpf(str(AME[iso])) * 100)
        maxabs = max(abs(errs[i]) for i in ["T", "3He", "4He"])
        cand_results[name] = {"value": mp.nstr(f, 8), "err_pct": errs,
                              "max_abs_err_A3": maxabs}
        if best_maxabs is None or maxabs < best_maxabs:
            best_maxabs, best_name = maxabs, name
        print(f"{name:28s}{float(f):>8.3f}   "
              + "  ".join(f"{errs[i]:>+5.0f}" for i, _, _ in cases))

    print(f"\nBest single candidate: {best_name} "
          f"(max |err| on A≥3 = {best_maxabs:.0f}%).")
    print("No derived q-factor closes A≥3 within 10%. The p/n asymmetry")
    print("(T≠³He) rules out ANY scalar q-factor: the enhancement must")
    print("carry the proton/neutron distinction. Torus-knot q^{2n_s}: refuted.")

    wb.set_description(
        "Derive-or-refute: does a DERIVED per-magic-closure enhancement "
        "f^{n_close} close A≥3 binding on top of the scalar endomorphism "
        "B_endo = m_e·Vol(𝓑₃)·Δtr? No AME fitting. Findings: B_endo exact "
        "for D (resid 0.998); A≥3 needs f≈2.45–2.88/closure; the torus-knot "
        "gap q^{2n_s} is refuted (q⁴=1.52 too small, q¹²=3.50 too big); "
        "[3]_q=3.04 is closest but misses ³He by +24%; and T (n-shell, "
        "f=2.82) ≠ ³He (p-shell, f=2.45) is a p/n asymmetry no scalar "
        "q-factor can produce. Deuteron derived; A≥3 open."
    )
    wb.add_data("endomorphism", {
        iso: {"dtr": mp.nstr(endo[iso]["dtr"], 10),
              "B_endo_MeV": mp.nstr(endo[iso]["B_endo"], 10),
              "B_AME_MeV": AME[iso],
              "resid": mp.nstr(endo[iso]["resid"], 8),
              "n_close": endo[iso]["n_close"],
              "f_per_closure": mp.nstr(f_needed[iso], 8)}
        for iso, _, _ in cases})
    wb.add_data("f_per_closure_spread_pct", f_spread)
    wb.add_data("pn_asymmetry", {
        "T_neutron_shell": mp.nstr(f_needed["T"], 6),
        "3He_proton_shell": mp.nstr(f_needed["3He"], 6),
        "ratio": mp.nstr(f_needed["T"] / f_needed["3He"], 6),
        "implication": "p/n-asymmetric — no scalar q-factor can close A≥3",
    })
    wb.add_data("derived_candidates", cand_results)
    wb.add_data("conclusion", {
        "deuteron": "derived (B_endo exact, resid 0.998, 0 closures)",
        "torus_knot_q2ns": "REFUTED (q^4=1.52 too small; q^12=3.50 too big)",
        "best_candidate": best_name,
        "best_max_abs_err_A3_pct": best_maxabs,
        "structural_blocker": "p/n asymmetry T≠³He rules out any scalar f",
        "status": "A≥3 open — needs p/n-asymmetric per-closure enhancement, "
                  "no fitting",
    })
    wb.add_assertion(
        "deuteron_endomorphism_exact",
        computed=endo["D"]["resid"],
        expected=1.0,
        tolerance=0.01,
        source="B_endo = m_e·Vol(𝓑₃)·Δtr closes D (resid 0.998, 0 closures)",
    )
    # Was `computed=round(best_maxabs, 0), expected=round(best_maxabs, 0)`
    # under `tolerance=1` (bean `qou-26f2`) — the same expression on both
    # sides, so the tolerance had nothing to measure and the assertion held
    # for any `best_maxabs`, including 0, which would mean a scalar f *does*
    # close A>=3 and refute the name.
    #
    # The `source` string states the real claim: "best derived f leaves >=12%
    # on A>=3". That is a lower bound on `best_maxabs`, and it is the whole
    # negative result — so it is now asserted as one. If some derived f ever
    # gets the residual under 12%, this fails, which is exactly when someone
    # should be told.
    wb.add_assertion(
        "no_derived_scalar_f_closes_A3",
        computed=bool(best_maxabs >= 12.0),
        expected=True,
        source=f"best derived f ({best_name}) leaves {best_maxabs:.1f}% "
               f">= 12% on A>=3; p/n asymmetry blocks any scalar f",
    )
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    wb.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    wb.save()


if __name__ == "__main__":
    main()
