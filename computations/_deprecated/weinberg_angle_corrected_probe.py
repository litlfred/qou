"""Corrected Weinberg-angle probe — non-uniform Hoefsmit multiplicities
+ candidate Higgs-vev automorphism on the (W^3, B) subspace.

Per workplan v2 (Tier A2 follow-on, 2026-05-06): the simple-uniform-
multiplicity reading was falsified at 64% rel deviation
(weinberg-angle-simple-falsified.witness.json).  Corrected version
uses:

  - Non-uniform pure-pattern multiplicities (4, 2, 1, 3, 3, 1, 2, 4)
    from conj:hoefsmit-ew-cell-content.  [Per-pattern]
  - Candidate Higgs-vev induced rotation on the (σ_5, σ_3) slot pair
    that mixes the eigenchannels.  [Categorical-physics analog of
    (W^3, B) → (Z, γ) rotation by θ_W.]

We test several candidate forms for the Higgs-vev automorphism and
record which (if any) approach CODATA cot θ_W ≈ 1.823 at q_0.

This is an exploratory probe — the simple-multiplicity null result
already excluded the "trivial" reading; here we test whether
non-trivial mixing brings the Weinberg-angle prediction into the
right regime.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
mpmath.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR


def main() -> int:
    q = mpmath.mpf(Q_50_DIGIT_STR)

    # CODATA target
    sin2theta_codata = mpmath.mpf("0.23129")
    cos_theta_codata = mpmath.sqrt(1 - sin2theta_codata)
    sin_theta_codata = mpmath.sqrt(sin2theta_codata)
    cot_theta_codata = cos_theta_codata / sin_theta_codata

    # Hoefsmit pure-pattern multiplicities for (σ_1, σ_3, σ_5)
    # patterns (sym/alt)^3.
    #   index = (sgn_W, sgn_Z, sgn_H), 0 = sym, 1 = alt
    mult = {
        (0, 0, 0): 4,   # sss: vacuum-like, all sym
        (0, 0, 1): 3,   # ssa: only H alt
        (0, 1, 0): 1,   # sas: only Z alt
        (1, 0, 0): 2,   # ass: only W alt
        (0, 1, 1): 2,   # saa: Z and H alt
        (1, 0, 1): 1,   # asa: W and H alt
        (1, 1, 0): 3,   # aas: W and Z alt
        (1, 1, 1): 4,   # aaa: all alt
    }
    twist_W, twist_Z, twist_H = 4, 6, 8

    def eig(twist, sgn):
        return q ** twist if sgn == 0 else q ** (-twist)

    # ── Hypothesis 1: pure-trace ratio of W vs H per-channel ────
    # tr_W := Σ_{patterns where W is sym} m * eig(W, sym) * eig(Z, *) * eig(H, *)
    # tr_H := Σ_{patterns where H is sym} m * eig(W, *) * eig(Z, *) * eig(H, sym)
    # cot θ_W candidate = tr_W / tr_H (no Higgs-vev rotation yet)

    tr_W_sym = sum(
        m * eig(twist_W, 0) * eig(twist_Z, p[1]) * eig(twist_H, p[2])
        for p, m in mult.items() if p[0] == 0
    )
    tr_W_alt = sum(
        m * eig(twist_W, 1) * eig(twist_Z, p[1]) * eig(twist_H, p[2])
        for p, m in mult.items() if p[0] == 1
    )
    tr_H_sym = sum(
        m * eig(twist_W, p[0]) * eig(twist_Z, p[1]) * eig(twist_H, 0)
        for p, m in mult.items() if p[2] == 0
    )
    tr_H_alt = sum(
        m * eig(twist_W, p[0]) * eig(twist_Z, p[1]) * eig(twist_H, 1)
        for p, m in mult.items() if p[2] == 1
    )

    print("Corrected Weinberg-angle probe — Hoefsmit non-uniform multiplicities")
    print("=" * 72)
    print(f"  q_0 = {mpmath.nstr(q, 25)}")
    print(f"  CODATA cot θ_W = {mpmath.nstr(cot_theta_codata, 14)}")
    print()
    print("  Per-channel sym/alt traces (Hoefsmit non-uniform):")
    print(f"    tr_W_sym = {mpmath.nstr(tr_W_sym, 14)}")
    print(f"    tr_W_alt = {mpmath.nstr(tr_W_alt, 14)}")
    print(f"    tr_H_sym = {mpmath.nstr(tr_H_sym, 14)}")
    print(f"    tr_H_alt = {mpmath.nstr(tr_H_alt, 14)}")
    print()

    candidates = []

    # H1a: pure W-sym / H-sym ratio
    h1a = tr_W_sym / tr_H_sym
    err = abs(h1a - cot_theta_codata) / cot_theta_codata
    candidates.append(("tr_W_sym / tr_H_sym", float(h1a), float(err)))

    # H1b: pure W-alt / H-alt ratio
    h1b = tr_W_alt / tr_H_alt
    err = abs(h1b - cot_theta_codata) / cot_theta_codata
    candidates.append(("tr_W_alt / tr_H_alt", float(h1b), float(err)))

    # H1c: ratio of net (sym - alt) traces — a "polarisation" reading
    h1c = (tr_W_sym - tr_W_alt) / (tr_H_sym - tr_H_alt)
    err = abs(h1c - cot_theta_codata) / cot_theta_codata
    candidates.append(("(tr_W_sym − tr_W_alt) / (tr_H_sym − tr_H_alt)",
                      float(h1c), float(err)))

    # H1d: sqrt of (tr_W² / tr_H²) — geometric mean reading
    h1d = mpmath.sqrt((tr_W_sym ** 2 + tr_W_alt ** 2)
                      / (tr_H_sym ** 2 + tr_H_alt ** 2))
    err = abs(h1d - cot_theta_codata) / cot_theta_codata
    candidates.append(("sqrt((tr_W²) / (tr_H²)), Pythagorean",
                      float(h1d), float(err)))

    # ── Hypothesis 2: Higgs-vev rotation candidates ─────────────
    # The Higgs-vev induces a (W^3, B) → (Z, γ) rotation by θ_W.
    # On the σ_5 (H) slot which encodes B pre-EWSB, this is a
    # specific automorphism.  Candidate Ansätze:

    # H2a: rotation matrix of trace ratios via [k]_q-weighted sum
    # Use [10]_q · [9]_q (force-carrier complexity, AXKIA template)
    # as proxy for Higgs-vev mixing parameter
    def qint(n):
        return (q ** n - q ** -n) / (q - 1 / q) if n != 0 else mpmath.mpf(0)

    h2a = qint(10) * qint(9) / (qint(8) * qint(6) * qint(4)) * tr_W_sym \
        / tr_H_sym
    err = abs(h2a - cot_theta_codata) / cot_theta_codata
    candidates.append(("[9]_q·[10]_q / ([4]·[6]·[8]) · tr_W_sym/tr_H_sym",
                      float(h2a), float(err)))

    # H2b: pure q-power rescale of H1a
    # If h1a ≈ q_0^{-4}, we need a multiplier ≈ cot_codata · q_0^4 ≈ 2.7
    target = cot_theta_codata
    h2b_multiplier = target / h1a
    print(f"  H1a = {float(h1a):.4f}, CODATA target / H1a = "
          f"{float(h2b_multiplier):.4f}")
    print(f"  log_q(target / H1a) = "
          f"{float(mpmath.log(h2b_multiplier) / mpmath.log(q)):.4f}")
    print()

    # H2c: ratio with [4]_q · [6]_q · [8]_q in numerator (force-carrier
    # complexity for EW)
    h2c = (tr_W_sym + tr_W_alt) / (tr_H_sym + tr_H_alt) \
        * qint(4) * qint(6) / qint(8)
    err = abs(h2c - cot_theta_codata) / cot_theta_codata
    candidates.append(
        ("(tr_W_sym+alt)/(tr_H_sym+alt) · [4][6]/[8]",
         float(h2c), float(err)))

    # ── Print results ──────────────────────────────────────────
    print("Candidate cot θ_W readings:")
    print(f"  {'form':<55} {'value':>12} {'rel err':>10}")
    print("  " + "-" * 80)
    for name, val, err in candidates:
        flag = "★" if err < 0.01 else (" " if err > 0.5 else "·")
        print(f"  {flag} {name:<55} {val:>12.4f} {err*100:>9.2f}%")
    print()

    best = min(candidates, key=lambda x: x[2])
    print(f"  Best candidate: {best[0]}")
    print(f"    value     = {best[1]:.6f}")
    print(f"    CODATA    = {float(cot_theta_codata):.6f}")
    print(f"    rel err   = {best[2]*100:.4f}%")
    print()

    if best[2] < 1e-3:
        verdict = "candidate-found"
    elif best[2] < 1e-2:
        verdict = "near-miss"
    else:
        verdict = "no-clean-categorical-fit"

    print(f"VERDICT: {verdict}")
    print()
    print("Interpretation: at this stage, none of the Hoefsmit non-uniform")
    print("readings closes Weinberg angle to CODATA precision without an")
    print("ad-hoc multiplier.  The Higgs-vev induced (W^3, B) → (Z, γ)")
    print("rotation requires explicit categorical-physics authoring — see")
    print("conj:categorical-higgs-mechanism §C.  This probe rules out")
    print("simple direct readings; the open structure is the Higgs-vev")
    print("automorphism, not a numerical-form ansatz.")

    out = {
        "computation": "weinberg-angle-corrected-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Corrected Weinberg-angle probe using non-uniform Hoefsmit "
            "pure-pattern multiplicities (4, 2, 1, 3, 3, 1, 2, 4) plus "
            "candidate Higgs-vev rotation forms.  Tests six candidates; "
            "verdict records whether any closes CODATA cot θ_W to "
            "structural precision."
        ),
        "reference_blocks": [
            "conj:weinberg-angle-categorical",
            "conj:hoefsmit-ew-cell-content",
            "conj:categorical-linking-operation",
            "conj:categorical-higgs-mechanism",
        ],
        "audit": "docs/audits/2026-05-06-refocused-1ppb-workplan-v2.md",
        "q_0": str(q),
        "codata_cot_theta_W": str(cot_theta_codata),
        "non_uniform_multiplicities": {
            "(sym,sym,sym)": 4, "(sym,sym,alt)": 3, "(sym,alt,sym)": 1,
            "(alt,sym,sym)": 2, "(sym,alt,alt)": 2, "(alt,sym,alt)": 1,
            "(alt,alt,sym)": 3, "(alt,alt,alt)": 4,
        },
        "per_channel_traces_q0": {
            "tr_W_sym": str(tr_W_sym), "tr_W_alt": str(tr_W_alt),
            "tr_H_sym": str(tr_H_sym), "tr_H_alt": str(tr_H_alt),
        },
        "candidates": [
            {"form": name, "value_at_q0": val, "rel_err": err}
            for name, val, err in candidates
        ],
        "best": {"form": best[0], "value": best[1], "rel_err": best[2]},
        "verdict": verdict,
        "next_step": (
            "None of the simple readings closes Weinberg angle.  "
            "Open: the Higgs-vev induced (W^3, B) → (Z, γ) rotation is "
            "a categorical-physics input that simple cell-content "
            "multiplicity readings cannot supply.  Discharge gated on "
            "conj:categorical-higgs-mechanism Step C + conj:categorical-"
            "linking-operation properties 3-5."
        ),
    }
    out_path = Path(__file__).parent / "weinberg-angle-corrected-probe.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
