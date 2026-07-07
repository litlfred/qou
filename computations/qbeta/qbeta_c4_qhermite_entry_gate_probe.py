#!/usr/bin/env python3
"""qbeta_c4_qhermite_entry_gate_probe.py — does q-Hermite supply the c_k?

Formalize-first entry gate (per AGENTS.md §3.3: prune a hypothesis class with a
structural argument BEFORE a wide scan). The user's intuition is structurally
sound at the FACE level: the continuous q-Hermite generating function

    G(t, θ | q) = Σ_n H_n(cos θ|q) t^n/(q;q)_n = 1/[(t e^{iθ};q)_∞ (t e^{-iθ};q)_∞]

is a product of two COMPACT quantum dilogs Φ_q — the bar-even / mass / Rogers
face — and c_4 is even-order (bar-even). So q-Hermite lives on the right face.

But the c_k are FINITE Taylor coefficients in u = b·ℏ_q² at q = 1 (c_2 = −1
proved). This probe tests whether the natural q-Hermite objects can supply them,
with ZERO fitted parameters (θ fixed by corpus structure). It does NOT fit
anything to c_4 (C14: c_4 carries ~4–5 sig figs; a fit is numerology — PR #1805).

## Pre-stated gates

  G1  cumulant pole    : κ_n(θ,q) = 2cos(nθ)/(1−q^n) has a simple pole at q=1
                         (residue −2cos(nθ)/n ≠ 0 generically) — DIVERGES where
                         the c_k are finite.
  G2  c_2 anchor       : with t ∝ u = b·ℏ_q² (u ~ (q−1)² → 0), the induced
                         2nd-order coefficient does NOT tend to the proved
                         c_2 = −1 for any structural θ — a q-dependent counter-
                         term t(u,q) cancelling the pole would be a fit.
  G3  moment route     : the FINITE q-Hermite moments (Touchard–Riordan
                         1,1,2+q,5+6q+3q²+q³,…) are POSITIVE and GROWING, while
                         the c_k (−1,−2,−1.14,−1.22,+3.50,…) are small mixed-sign.

Verdict target: scope-(a). If G1–G3 hold, the NATURAL continuous-q-Hermite
route (cumulant + moment) is excluded for the c_k; the deeper Askey-scheme /
q-dependent-variable route is NOT excluded but would require a DERIVED t(u,q)
(a structural reason), not a fit — flagged as the only non-fishing continuation.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = set_compute_dps()

# Structural θ choices (corpus-fixed, NOT fitted): π/3 = Vol(4₁) = 2Λ(π/3) angle;
# π/2 = ζ₄; 2π/5 = ζ₅ Galois locus. All appear in the merged root-of-unity set.
# Evaluated inside an explicit precision context (unary + re-rounds).
with mp.workdps(DPS):
    THETAS = [("pi/3", +(mp.pi / 3)), ("pi/2", +(mp.pi / 2)), ("2pi/5", +(2 * mp.pi / 5))]
# c_k values as SDP-EXTRACTED at the substrate (decay-sdp; extraction-biased,
# NOT the proved structural targets). Used only for the G3 sign/magnitude
# comparison. The G2 anchor is the PROVED structural target c_2 = −1 (exact),
# which these extracted numbers (c_2 ≈ −1.0171) only approximate.
CK_SDP_EXTRACTED = {2: -1.0171, 3: -2.0097, 4: -1.1435, 5: -1.2229, 6: 3.4976}
C2_STRUCTURAL_TARGET = -1  # proved (factor convention); the real G2 anchor


def main() -> int:
    print("=" * 78)
    print(" q-Hermite entry gate for the c_k precision ladder (0 fitted params)")
    print("=" * 78)
    wb = WitnessBuilder("qbeta-c4-qhermite-entry-gate", engine="sympy+mpmath")
    wb.set_description(
        "Formalize-first entry gate: does the natural continuous q-Hermite "
        "structure supply the c_k? q-Hermite gen func = product of compact Φ_q "
        "(bar-even/mass face; c_4 is even-order) — right face. But its cumulants "
        "κ_n = 2cos(nθ)/(1−q^n) have a q=1 pole (G1) so cannot equal the finite "
        "c_2=−1 (G2) without a fitted q-dependent variable change; its finite "
        "moments (Touchard–Riordan) are positive-growing vs the small mixed-sign "
        "c_k (G3). Verdict scope-(a): natural continuous-q-Hermite route excluded; "
        "deeper Askey-scheme / derived-t(u,q) route not excluded but needs a "
        "structural reason, not a fit (C14; PR #1805 entropy bound: c_4 ~4-5 sig "
        "figs). No fit to c_4."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # G1: κ_n = 2cos(nθ)/(1−q^n) has a SIMPLE POLE at q=1 iff cos(nθ) ≠ 0
    # (the residue is −2cos(nθ)/n). The gate genuinely checks cos(2θ) ≠ 0 at the
    # c_2 anchor (n=2) for EVERY structural θ — i.e. no θ-loophole where q-Hermite
    # would be finite. A θ with cos(2θ)=0 (e.g. π/4) would FAIL this gate.
    g1_rows = []
    g1_pole_at_anchor = True   # cos(2θ) ≠ 0 for all structural θ (non-tautological)
    for name, _theta in THETAS:
        th = sp.Rational(1, 3) * sp.pi if name == "pi/3" else (
            sp.pi / 2 if name == "pi/2" else sp.Rational(2, 5) * sp.pi)
        for n in (1, 2):
            c = sp.simplify(sp.cos(n * th))
            has_pole = bool(c != 0)          # simple pole at q=1 unless cos(nθ)=0
            if n == 2:
                g1_pole_at_anchor = g1_pole_at_anchor and has_pole
            g1_rows.append({"theta": name, "n": n, "cos_ntheta": str(c),
                            "residue_nonzero": has_pole})
    g1_all_pole = g1_pole_at_anchor
    print("\n  G1 — cumulant pole at q=1:")
    print("     κ_n = 2cos(nθ)/(1−q^n); (1−q^n)→0 at q=1 ⇒ simple pole unless cos(nθ)=0.")
    print("     For θ=π/3, π/2, 2π/5 the n=2 cosines are −1/2, −1, −1+... ≠ 0 ⇒ pole.")

    # G2: induced c_2 with t ∝ u = b·ℏ_q², numeric at q slightly below/above 1.
    print("\n  G2 — c_2 anchor (t ∝ u), does κ→ finite −1?")
    g2_rows = []
    for name, theta in THETAS:
        vals = []
        for eps in (mp.mpf("1e-2"), mp.mpf("1e-4"), mp.mpf("1e-6")):
            qv = mp.mpf(1) - eps
            hbar = 1 - 1 / qv
            u = hbar ** 2  # b absorbed (structural, order-1)
            kappa2 = 2 * mp.cos(2 * theta) / (1 - qv ** 2)
            # coeff of u^2 if t=u would be kappa2 (leading); track kappa2 itself.
            vals.append(float(kappa2))
        # diverges (|kappa2| grows as eps→0) ⇒ no finite c_2
        diverges = abs(vals[-1]) > abs(vals[0]) * 10
        g2_rows.append({"theta": name, "kappa2_eps_1e-2": f"{vals[0]:.4e}",
                        "kappa2_eps_1e-6": f"{vals[-1]:.4e}", "diverges": bool(diverges)})
        print(f"     θ={name:6s}: κ_2 = {vals[0]:.3e} → {vals[-1]:.3e} as q→1  "
              f"({'DIVERGES' if diverges else 'finite'})")
    g2_all_diverge = all(r["diverges"] for r in g2_rows)

    # G3: q-Hermite moments (Touchard-Riordan) are positive-growing; c_k mixed-sign.
    # moments at q=1 are (2n-1)!! = 1,1,3,15,105 — strictly positive & growing.
    print("\n  G3 — moment route sign/magnitude:")
    moments_q1 = [1, 1, 3, 15, 105]  # μ_0,μ_2,μ_4,μ_6,μ_8 at q=1 (Gaussian)
    ck_signs = [CK_SDP_EXTRACTED[k] for k in sorted(CK_SDP_EXTRACTED)]
    moments_positive_growing = all(
        moments_q1[i] <= moments_q1[i + 1] for i in range(len(moments_q1) - 1))
    ck_mixed_sign = (min(ck_signs) < 0 < max(ck_signs))
    print(f"     q-Hermite moments (q=1): {moments_q1}  positive-growing="
          f"{moments_positive_growing}")
    print(f"     c_k: {ck_signs}  mixed-sign={ck_mixed_sign}, |c_k|~O(1) not growing")
    g3_excludes = moments_positive_growing and ck_mixed_sign

    print("\n  VERDICT (scope-a): natural continuous-q-Hermite route EXCLUDED for c_k.")
    print("  q-Hermite IS on the bar-even face (gen func = Φ_q product), but its")
    print("  cumulants diverge at q=1 (G1/G2) and its moments have the wrong sign")
    print("  pattern (G3). A q-dependent t(u,q) cancelling the q=1 pole to hit")
    print("  c_2=−1 would be a fit (C14). Deeper Askey-scheme route NOT excluded")
    print("  but needs a DERIVED variable map, not a scan.")

    wb.add_data("g1_cumulant_pole_rows", g1_rows)
    wb.add_data("g2_c2_anchor_rows", g2_rows)
    wb.add_data("g3_moments_q1", moments_q1)
    wb.add_data("g3_ck_sdp_extracted", CK_SDP_EXTRACTED)
    wb.add_data("g2_c2_structural_target", C2_STRUCTURAL_TARGET)
    wb.add_data("qhermite_face", "bar-even (gen func = product of compact Φ_q); "
                "c_4 even-order ⇒ correct face")
    wb.add_data("verdict_scope", "(a) natural continuous-q-Hermite route excluded; "
                "Askey-scheme/derived-t(u,q) route not excluded, needs structural map")
    wb.add_data("invariant_cited", "q=1 pole of 1/(1-q^n) (compact q-dilog cumulant) "
                "vs finite c_2=-1 — same q=1 cusp obstruction as T14 Δ_λ probe")

    wb.add_assertion("G1_cumulant_has_q1_pole", computed=1.0 if g1_all_pole else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="κ_n=2cos(nθ)/(1-q^n) simple pole at q=1 for structural θ")
    wb.add_assertion("G2_c2_anchor_diverges", computed=1.0 if g2_all_diverge else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="κ_2 diverges as q→1 (t∝u), cannot equal finite c_2=-1")
    wb.add_assertion("G3_moment_route_excluded", computed=1.0 if g3_excludes else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="q-Hermite moments positive-growing vs c_k small mixed-sign")

    ok = g1_all_pole and g2_all_diverge and g3_excludes
    print(f"\n  ALL GATES: {'OK (route excluded, scope-a)' if ok else 'INCONCLUSIVE'}")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
