"""β_EW(Δ_I^minimal) eigenvalue spectrum on the 2 surviving + 18
mixed Hoefsmit tableaux of partitions of 6.

The 2 simultaneously-diagonal tableaux are:
  b_+: standard tableau of shape (6) — every σ_i: sym → eigenvalue +q
       Hoefsmit-action of σ_i^{2k}: q^{2k}; so β_EW(Δ_I^minimal)
       acts on b_+ as
           q^4 · q · q · q · q^6 · q · q · q · q^8 · q · q · q
         = q^4 · q^3 · q^6 · q^3 · q^8 · q^3
         = q^(4 + 3 + 6 + 3 + 8 + 3) = q^27
  b_-: standard tableau of shape (1^6) — every σ_i: alt
       eigenvalue -q^{-1}; σ_i^{2k}: q^{-2k}; σ_i: -q^{-1}
       β_EW(Δ_I^minimal) on b_-:
           q^{-4} · (-q^{-1}) · (-q^{-1}) · (-q^{-1}) · q^{-6}
         · (-q^{-1})^3 · q^{-8} · (-q^{-1})^3
       = q^{-4} · (-q^{-1})^3 · q^{-6} · (-q^{-1})^3 · q^{-8} · (-q^{-1})^3
       = q^{-4} · (-1)^3 q^{-3} · q^{-6} · (-1)^3 q^{-3} · q^{-8} · (-1)^3 q^{-3}
       = -q^{-4-3} · -q^{-6-3} · -q^{-8-3}
       = -q^{-7} · -q^{-9} · -q^{-11}
       = (-1)^3 q^{-27} = -q^{-27}

So β_EW(Δ_I^minimal) on b_+ = q^{27}, on b_- = -q^{-27}.

Apply the Weinberg-angle reading (corrected, using Δ_I-spectrum):

  cos θ_W := tr_M(e_W^+ · β_EW · e_W^+) / norm

where e_W^+ corresponds to the 'sym' projection on the σ_1 slot.

Since b_+ is the 'all-sym' eigenstate, it's the photon-like
unbroken-EM survivor (γ); cos θ_W reading should map γ to the
appropriate (W^3, B) projection.

This script:
  1. Computes the b_+ and b_- eigenvalues exactly.
  2. Identifies the 2-dim invariant subspace = span(b_+, b_-).
  3. Computes a candidate cot θ_W from the eigenvalue ratio.
  4. Compares to CODATA cot θ_W ≈ 1.823.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sympy as sp
from q_parameter import Q_50_DIGIT_STR


def main() -> int:
    q = sp.Symbol("q", positive=True)

    # β_EW(Δ_I^minimal) = σ_1^4 · (σ_2 σ_4 σ_2) · σ_3^6 · (σ_2 σ_4 σ_2)
    #                  · σ_5^8 · (σ_2 σ_4 σ_2)
    #
    # On b_+ (row tableau): every σ_i has eigenvalue +q (sym)
    #   σ_1^4 → q^4
    #   σ_2 → q (sym), 3× → q^3
    #   σ_3^6 → q^6
    #   σ_2 σ_4 σ_2 → q^3
    #   σ_5^8 → q^8
    #   σ_2 σ_4 σ_2 → q^3
    #   total: q^(4+3+6+3+8+3) = q^27
    eig_plus = q ** (4 + 3 + 6 + 3 + 8 + 3)
    # = q^27

    # On b_- (column tableau): every σ_i has eigenvalue -q^{-1} (alt)
    #   σ_1^4 → (-q^{-1})^4 = q^{-4}
    #   σ_2 → -q^{-1}, 3× → (-q^{-1})^3 = -q^{-3}
    #   σ_3^6 → (-q^{-1})^6 = q^{-6}
    #   σ_2 σ_4 σ_2 → (-q^{-1})^3 = -q^{-3}
    #   σ_5^8 → (-q^{-1})^8 = q^{-8}
    #   σ_2 σ_4 σ_2 → (-q^{-1})^3 = -q^{-3}
    #   total: q^{-4} · (-q^{-3}) · q^{-6} · (-q^{-3}) · q^{-8} · (-q^{-3})
    #        = (-1)^3 q^{-(4+3+6+3+8+3)} = -q^{-27}
    eig_minus = -q ** (-(4 + 3 + 6 + 3 + 8 + 3))
    # = -q^{-27}

    print("β_EW(Δ_I^minimal) eigenvalue spectrum on Δ_I-invariant tableaux:")
    print(f"  b_+ (row tableau, shape (6)):   eigenvalue = {eig_plus}")
    print(f"  b_- (column tableau, shape (1^6)): eigenvalue = {eig_minus}")
    print()

    # Bar-self-duality check at the 2-dim invariant level:
    # Under ι: q → q^{-1}, eig_plus → q^{-27} = -eig_minus^{-1} · (-1)
    # i.e. ι(eig_plus) = -ι(eig_minus^{-1})... let me verify
    bar_plus = eig_plus.subs(q, 1/q)  # = q^{-27}
    bar_minus = eig_minus.subs(q, 1/q)  # = -q^{27}
    print("Bar-involution behavior:")
    print(f"  ι(eig_+) = {sp.simplify(bar_plus)}  vs eig_- = {eig_minus}")
    print(f"  ι(eig_+) + eig_- = {sp.simplify(bar_plus + eig_minus)}")
    # ι(eig_+) = q^{-27}, eig_- = -q^{-27}.
    # ι(eig_+) + eig_- = q^{-27} - q^{-27} = 0. ✓
    # So ι(eig_+) = -eig_-, i.e. eig_+ + bar(eig_-) = 0.
    print(f"  → ι(eig_+) = −eig_- (bar-anti-self-dual pair)")
    print()

    # Numerical specialization at q_0
    q_0 = sp.Rational(Q_50_DIGIT_STR)
    eig_plus_num = float(eig_plus.subs(q, q_0))
    eig_minus_num = float(eig_minus.subs(q, q_0))
    print(f"At q_0 ≈ {float(q_0):.10f}:")
    print(f"  eig_+ = q_0^27          ≈ {eig_plus_num:.6e}")
    print(f"  eig_- = −q_0^{{−27}}      ≈ {eig_minus_num:.6e}")
    print(f"  |eig_+| / |eig_-|        = q_0^54 ≈ {float(q_0**54):.6e}")
    print()

    # ── Candidate Weinberg-angle reading via Δ_I-spectrum ──────
    # The two invariant eigenvalues represent the two 1-dim
    # post-EWSB projectors that survive the Higgs-vev rotation.
    # In the Standard Model these are (γ, fully-broken extreme)
    # — so cos θ_W governs the rotation rate from (W^3, B) to
    # (Z, γ) in the 18-dim mixed sub-space.
    #
    # Candidate forms for cot θ_W from the 2-dim invariant data:
    print("Candidate cot θ_W readings from Δ_I^minimal-invariant spectrum:")
    print(f"  {'form':<55} {'value':>14} {'rel err':>10}")
    print("  " + "-" * 80)

    cot_codata = sp.sqrt(1 - sp.Rational("0.23129")) / sp.sqrt(sp.Rational("0.23129"))
    cot_codata_num = float(cot_codata)
    print(f"  CODATA cot θ_W: {cot_codata_num:.6f}")
    print()

    candidates = []

    # H1: |eig_+| / |eig_-|  = q^54
    h1 = q_0 ** 54
    candidates.append(("|eig_+| / |eig_-| = q_0^54", float(h1)))

    # H2: |eig_+|^{1/27} (degree-normalized)
    h2 = q_0 ** 1
    candidates.append(("(|eig_+|)^{1/27} = q_0", float(h2)))

    # H3: log(|eig_+| / |eig_-|) / log(q_0) = 54 → not a number
    # H4: ratio via degree-1 normalization q^{27/27} = q vs q^{-1}
    h4 = q_0 / (1 / q_0)  # = q^2
    candidates.append(("q_0 / q_0^{-1} = q_0^2", float(h4)))

    # H5: ratio of 27-th roots? = q · 1/(-q^{-1})^{1/27} ... unclear
    # H6: simpler — sqrt(q^54) = q^27, normalized
    h6 = q_0 ** (sp.Rational(27, 27))  # = q
    # already H2

    # H7: 1 + h(q^54)/h(1)  — H ansatz family
    # Actually let's try the simpler structural reading:
    # cot θ_W = (eig_+ - eig_-) / (eig_+ + eig_-)  (a "weighted ratio")
    # = (q^27 + q^{-27}) / (q^27 - q^{-27})   [eig_- has − sign so
    #                                          eig_+ - eig_- = q^27 + q^{-27}
    #                                          eig_+ + eig_- = q^27 - q^{-27}]
    h7 = (q_0 ** 27 + q_0 ** (-27)) / (q_0 ** 27 - q_0 ** (-27))
    candidates.append(
        ("(eig_+ − eig_-)/(eig_+ + eig_-) = coth(27 ln q_0)",
         float(h7)))

    # H8: tanh form
    h8 = (q_0 ** 27 - q_0 ** (-27)) / (q_0 ** 27 + q_0 ** (-27))
    candidates.append(
        ("(eig_+ + eig_-)/(eig_+ − eig_-) = tanh(27 ln q_0)",
         float(h8)))

    # H9: log-ratio normalized by 27
    h9 = sp.log(q_0 ** 54) / sp.log(q_0 ** 27)  # = 2
    candidates.append(("log_q_0(|eig_+|^2 /|eig_-|^2) / 27 = 2",
                      float(h9)))

    # H10: scaling by [27]_q analog
    def qint(n):
        return (q_0 ** n - q_0 ** -n) / (q_0 - 1 / q_0) if n != 0 else 0
    h10 = qint(27) / qint(1)
    candidates.append(("[27]_q / [1]_q", float(h10)))

    for name, val in candidates:
        rel_err = abs(val - cot_codata_num) / cot_codata_num
        flag = "★" if rel_err < 0.01 else ("·" if rel_err < 0.1 else " ")
        print(f"  {flag} {name:<55} {val:>14.4f} {rel_err*100:>9.2f}%")
    print()

    best = min(candidates, key=lambda x: abs(x[1] - cot_codata_num))
    best_err = abs(best[1] - cot_codata_num) / cot_codata_num
    print(f"  Best: {best[0]}")
    print(f"    value     = {best[1]:.6f}")
    print(f"    CODATA    = {cot_codata_num:.6f}")
    print(f"    rel err   = {best_err*100:.4f}%")
    print()

    if best_err < 0.001:
        verdict = "candidate-found-precision-1e-3"
    elif best_err < 0.01:
        verdict = "near-miss-precision-1e-2"
    else:
        verdict = "no-clean-fit-on-2dim-invariant-only"

    print(f"VERDICT: {verdict}")
    print()
    print("Interpretation: the 2-dim Δ_I-invariant subspace alone")
    print("is structurally insufficient to close cot θ_W to CODATA")
    print("precision.  This is expected: the Weinberg rotation lives")
    print("in the 18-dim Δ_I-mixed sub-space, NOT in the invariant")
    print("part.  The next probe must extract eigenvalues from the")
    print("18-tableau mixed sub-space (off-diagonal Hoefsmit blocks).")

    out = {
        "computation": "beta-ew-delta-I-eigenvalues",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Symbolic eigenvalue extraction of β_EW(Δ_I^minimal) on "
            "the 2 Δ_I-invariant tableaux of partitions of 6 "
            "(b_+ = row shape (6), b_- = column shape (1^6)).  "
            "Eigenvalues exactly q^27 and -q^{-27} respectively — "
            "bar-anti-self-dual pair: ι(eig_+) = -eig_-.  Tests "
            "candidate cot θ_W readings from this 2-dim spectrum; "
            "structural conclusion: invariant subspace alone is "
            "insufficient to close Weinberg angle, the rotation "
            "lives in the 18-dim Δ_I-mixed complement."
        ),
        "reference_blocks": [
            "def:ew-interface-knot",
            "conj:hoefsmit-ew-cell-content",
            "conj:weinberg-angle-categorical",
            "conj:categorical-linking-operation",
        ],
        "audit": "docs/audits/2026-05-06-delta-I-interface-knot-refinement.md",
        "delta_I_word": "σ_2 σ_4 σ_2",
        "beta_EW_word": (
            "σ_1^4 · (σ_2 σ_4 σ_2) · σ_3^6 · (σ_2 σ_4 σ_2) · σ_5^8 "
            "· (σ_2 σ_4 σ_2)"
        ),
        "invariant_eigenvalues_R": {
            "b_plus_row_tableau_shape_6": "q^27",
            "b_minus_column_tableau_shape_1_to_6": "-q^{-27}",
        },
        "invariant_eigenvalues_at_q0": {
            "b_plus": eig_plus_num,
            "b_minus": eig_minus_num,
        },
        "bar_involution_pairing": {
            "iota_of_eig_plus": "q^{-27}",
            "minus_eig_minus": "q^{-27}",
            "iota_eig_plus_equals_minus_eig_minus": True,
            "interpretation": (
                "bar-anti-self-dual pair — the photon (b_+) and "
                "fully-broken extreme (b_-) are interchanged by ι "
                "with a sign, consistent with the Higgs-vev "
                "rotation flipping orientation."
            ),
        },
        "candidate_cot_theta_W_readings": [
            {"form": name, "value": val,
             "rel_err": abs(val - cot_codata_num) / cot_codata_num}
            for name, val in candidates
        ],
        "best_candidate": {
            "form": best[0], "value": best[1],
            "rel_err": best_err,
        },
        "codata_cot_theta_W": cot_codata_num,
        "verdict": verdict,
        "next_step": (
            "Extract eigenvalue spectrum of β_EW(Δ_I^minimal) on "
            "the 18 Δ_I-mixed tableaux (off-diagonal Hoefsmit "
            "blocks); the Weinberg rotation lives there, not in "
            "the 2-dim invariant subspace.  This is a substantive "
            "categorical-physics computation requiring the full "
            "Hoefsmit seminormal-form action on multi-dim irreps."
        ),
    }
    out_path = Path(__file__).parent / "beta-ew-delta-I-eigenvalues.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
