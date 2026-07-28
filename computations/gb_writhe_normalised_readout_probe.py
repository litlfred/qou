#!/usr/bin/env python3
"""gb_writhe_normalised_readout_probe.py — GAP-2 [G3] follow-up (bean qou-rbfr):
the writhe normalisation, DERIVED and then tested.

WHAT [G3] LEFT OPEN. `gb_winding_parity_wire_probe.py` established that the GS
reduction certificate's total coefficient sum S(β) = Σ_w c_w(q) carries the
winding parity in its q-grading, but that it is a FRAMED quantity:

    positive stabilisation  β ↦ β σ_n   :  S ↦ S          (e ↦ e+1, n ↦ n+1)
    negative stabilisation  β ↦ β σ_n⁻¹ :  S ↦ (1−h)·S    (e ↦ e−1, n ↦ n+1)

It concluded "a general braid needs writhe-normalisation first" WITHOUT saying by
what factor. That is the gap this closes.

THE FACTOR IS FORCED, NOT CHOSEN (Lean: QOU.QBeta.WritheNormalisation,
sorry-free, generic CommRing). Seek a monomial correction A^e·B^n in the exponent
sum e and strand count n. Invariance under the two moves above is exactly

    A * B = 1            (positive: e and n both rise)
    A = (1 − h) * B      (negative: e falls, n rises)

and `writhe_factor_sq` proves those two force A² = 1 − h. So the normalisation is

    Ŝ(β) = S(β) · (1 − h)^{(e(β) − n(β))/2}

with BOTH the base and the exponent derived — `writhe_factor_unique_up_to_sign`
shows any two solutions have equal squares, so there is no tuning freedom. This
matters: a factor picked to make the numbers work would be a fit, and the whole
point is that this one could not have been picked otherwise.

WHAT THIS PROBE MEASURES (derive-then-check, all symbolic in q):

  [N1] Invariance. Ŝ is unchanged by BOTH stabilisations, on braids of nonzero
       writhe — where the unnormalised S is not. Tested by applying each move to
       words with e ≠ 0, which is where [G3]'s caveat actually bites.
  [N2] The canonical family is untouched. On wⁿ = (σ₁σ₂⁻¹)ⁿ the exponent sum is
       0 and the strand count is 3 for every n, so the correction is one constant
       across the family — confirming [G3]'s escape clause and, crucially, that
       the (−1)ⁿ parity readout of [G2] SURVIVES normalisation rather than being
       an artifact of the framing.
  [N3] The boundary. At h = 1 the constraints are contradictory and no monomial
       normalisation exists (Lean: `no_normalisation_at_h_eq_one`); checked here
       as the vanishing of the negative-stabilisation ratio.

To avoid half-integer powers the tests use Ŝ² = S²·(1−h)^{e−n}, which carries the
same invariance content over the ring and needs no square root — the same
discipline as the Lean file, where A appears only via A * B = 1.

HONEST SCOPE. This fixes the unique monomial normalisation compatible with the
two stabilisation rules and verifies it. It does NOT prove the normalised readout
is a knot invariant — the Markov conjugation move is untouched here — and it does
NOT deliver the full winding class (m,ℓ). Nothing wired to production.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

from gb_winding_parity_wire_probe import (  # noqa: E402
    H, W, build, coeff_sum, laurent_top, q)
from witness_base import WitnessBuilder  # noqa: E402


def exponent_sum(word: list) -> int:
    return sum(1 if g > 0 else -1 for g in word)


def norm_sq(word: list, n_strands: int):
    """Ŝ² = S²·(1−h)^{e−n} — the squared writhe-normalised coefficient sum.

    Squared so the derived half-integer exponent (e−n)/2 never appears; the
    invariance content is identical over the ring.
    """
    S = coeff_sum(build(n_strands, word))
    return sp.simplify(sp.cancel(S ** 2 * (1 - H) ** (exponent_sum(word) - n_strands)))


def main() -> int:
    print("=" * 78)
    print(" GAP-2 [G3]: the writhe normalisation, derived then tested")
    print("=" * 78)
    print(" derived factor (Lean writhe_factor_sq):  Ŝ = S·(1−h)^{(e−n)/2},  A² = 1−h")
    print(" tested as Ŝ² = S²·(1−h)^{e−n} (no square root needed)")

    # ---- [N1] invariance under BOTH stabilisations, at nonzero writhe -------
    print("\n [N1] Markov stabilisation invariance where it actually bites (e ≠ 0)")
    print("      braid                    e  n | S invariant? | Ŝ² invariant?")
    cases = [("σ₁³ (trefoil)", [1, 1, 1], 3),
             ("σ₁²σ₂ ", [1, 1, 2], 3),
             ("σ₁σ₂⁻¹σ₁ ", [1, -2, 1], 3),
             ("σ₁⁻³ ", [-1, -1, -1], 3)]
    n1 = True
    rows = []
    for label, word, ns in cases:
        e = exponent_sum(word)
        base_S = coeff_sum(build(ns, word))
        base_N = norm_sq(word, ns)
        pos_word, neg_word = word + [ns], word + [-ns]
        pos_S = coeff_sum(build(ns + 1, pos_word))
        neg_S = coeff_sum(build(ns + 1, neg_word))
        pos_N = norm_sq(pos_word, ns + 1)
        neg_N = norm_sq(neg_word, ns + 1)

        S_inv = (sp.simplify(pos_S - base_S) == 0) and (sp.simplify(neg_S - base_S) == 0)
        N_inv = (sp.simplify(pos_N - base_N) == 0) and (sp.simplify(neg_N - base_N) == 0)
        n1 &= bool(N_inv)
        rows.append({"braid": label.strip(), "word": word, "e": e, "n_strands": ns,
                     "S_invariant": bool(S_inv), "Shat_sq_invariant": bool(N_inv)})
        print(f"      {label:24s}{e:+2d} {ns} | {str(bool(S_inv)):12s} | {bool(N_inv)}")
    print(f"      ⇒ Ŝ² invariant under both moves on every nonzero-writhe case: {bool(n1)}")
    print("        (the unnormalised S is not — that is exactly [G3]'s caveat)")

    # ---- [N2] the canonical family: correction constant, parity survives ----
    print("\n [N2] canonical family wⁿ — does the (−1)ⁿ parity readout survive?")
    print("      n | e | correction exponent e−n | deg Ŝ² | leading coeff of Ŝ²")
    n2 = True
    fam = []
    for n in range(1, 7):
        word = W * n
        e = exponent_sum(word)
        N = norm_sq(word, 3)
        d, lc = laurent_top(N)
        # S itself had leading coeff (−1)ⁿ, so S² has +1; the parity is carried by
        # the SIGN of the unnormalised leading coeff, which the constant factor
        # (1−h)^{0−3} cannot alter.
        _, lc_S = laurent_top(coeff_sum(build(3, word)))
        parity_ok = sp.simplify(lc_S - (-1) ** n) == 0
        const_corr = (e == 0)
        n2 &= bool(parity_ok and const_corr)
        fam.append({"n": n, "e": e, "corr_exponent": e - 3,
                    "leading_coeff_S": str(lc_S), "parity_matches": bool(parity_ok)})
        print(f"      {n} | {e:+d} | {e - 3} | {d} | {lc}")
    print(f"      exponent sum 0 and leading coeff (−1)ⁿ for all n: {bool(n2)}")
    print("      ⇒ the correction is ONE constant (1−h)^(−3) across the family, so the")
    print("        [G2] parity readout survives normalisation — it was not a framing")
    print("        artifact. This is why [G3]'s escape clause held.")

    # ---- [N3] the boundary at h = 1 ----------------------------------------
    print("\n [N3] boundary: at h = 1 no monomial normalisation exists")
    ratio_at_h1 = sp.simplify((1 - H).subs(H, 1))
    n3 = ratio_at_h1 == 0
    print(f"      negative-stabilisation ratio (1−h) at h=1 = {ratio_at_h1}  ⇒ the")
    print(f"      correction base vanishes and cannot be inverted: {bool(n3)}")
    print("      (Lean no_normalisation_at_h_eq_one: the two constraints are")
    print("       contradictory there. Only NECESSITY is claimed — h ≠ 1 is not")
    print("       sufficient, since existence also needs 1−h to be a square.)")

    print("\n ⇒ GAP-2 [G3] CLOSED: the normalisation is Ŝ = S·(1−h)^{(e−n)/2}, derived")
    print("   from the two stabilisation rules with no tuning freedom, verified")
    print("   invariant on nonzero-writhe braids, and shown not to disturb the")
    print("   canonical-family parity readout. Conjugation move still untouched, so")
    print("   this is stabilisation-invariance, NOT yet a knot invariant.")

    wb = WitnessBuilder("gb-writhe-normalised-readout", engine="sympy")
    wb.set_description(
        "GAP-2 [G3] follow-up (bean qou-rbfr): closes the normalisation gap left open by "
        "gb_winding_parity_wire_probe.py, which found the GS coefficient sum S(β)=Σ_w c_w(q) "
        "carries the winding parity but is FRAMED (S↦S under positive stabilisation, S↦(1−h)S "
        "under negative) and said a general braid 'needs writhe-normalisation first' without "
        "saying by what. DERIVED, not chosen: seeking a monomial correction A^e·B^n makes "
        "Markov-stabilisation invariance equivalent to A*B=1 and A=(1−h)B, and those force "
        "A²=1−h (Lean QOU.QBeta.WritheNormalisation.writhe_factor_sq, sorry-free, generic "
        "CommRing), i.e. Ŝ(β)=S(β)·(1−h)^{(e−n)/2} with base AND exponent both derived; "
        "writhe_factor_unique_up_to_sign leaves no tuning freedom. Tested as Ŝ²=S²·(1−h)^{e−n} "
        "to avoid half-integer powers. MEASURED: [N1] Ŝ² is invariant under BOTH stabilisations "
        "on four nonzero-writhe braids (trefoil σ₁³, σ₁²σ₂, σ₁σ₂⁻¹σ₁, σ₁⁻³) where the "
        "unnormalised S is not — exactly where [G3]'s caveat bites; [N2] on the canonical family "
        "wⁿ=(σ₁σ₂⁻¹)ⁿ the exponent sum is 0 and the strand count 3 for every n, so the correction "
        "is a single constant (1−h)^(−3) and the [G2] (−1)ⁿ parity readout SURVIVES "
        "normalisation — it was not a framing artifact, which is why [G3]'s escape clause held; "
        "[N3] at h=1 the correction base vanishes and no monomial normalisation exists (Lean "
        "no_normalisation_at_h_eq_one; only NECESSITY claimed — h≠1 is not sufficient, existence "
        "also needs 1−h to be a square). SCOPE: this is stabilisation-invariance, NOT a knot "
        "invariant — the Markov conjugation move is untouched — and the full winding class (m,ℓ) "
        "is still not delivered. Nothing wired to production.")
    wb.set_content_block("prop:winding-lattice-norm-form")
    wb.add_data("writhe_normalisation", {
        "derived_factor": "Ŝ = S·(1−h)^{(e−n)/2},  A² = 1−h  (A*B=1, A=(1−h)B)",
        "tested_form": "Ŝ² = S²·(1−h)^{e−n}  (no square root)",
        "lean": ("QOU.QBeta.WritheNormalisation: writhe_factor_sq, writhe_factor_B_sq, "
                 "writhe_factor_unique_up_to_sign, no_normalisation_at_h_eq_one"),
        "N1_stabilisation_cases": rows,
        "N2_canonical_family": fam,
        "N3_boundary": "at h=1 the base 1−h vanishes; no monomial normalisation (necessity only)",
        "verdict": ("normalisation derived with no tuning freedom, verified invariant on "
                    "nonzero-writhe braids, canonical-family parity readout unaffected; "
                    "conjugation move untouched so NOT yet a knot invariant")})
    wb.add_assertion("normalised_readout_stabilisation_invariant", str(bool(n1)), "True")
    wb.add_assertion("canonical_family_parity_survives_normalisation", str(bool(n2)), "True")
    wb.add_assertion("no_normalisation_at_h_eq_one", str(bool(n3)), "True")
    wb.save()
    print("\nwitness → gb-writhe-normalised-readout.witness.json")
    ok = n1 and n2 and n3
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
