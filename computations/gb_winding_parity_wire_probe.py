#!/usr/bin/env python3
"""gb_winding_parity_wire_probe.py — GAP-2 (bean qou-rbfr): can the winding
class / parity be READ OFF the Gröbner–Shirshov reduction certificate of a
braid word, rather than asserted from its w^n presentation?

Context. The merged #4401 result gives a sign mechanism for the S-channel:
sign Im 𝔙₄₁ = sign G(m,ℓ) on the cusp-torus winding lattice, with the physical
reading that the canonical knots are powers of the half-figure-eight word
w = σ₁σ₂⁻¹ (4₁ = w², Borromean L6a4 = w³) and the sign follows the parity of n.
That reading was labelled *transport by analogy* precisely because the winding
datum was asserted from the presentation. This probe asks whether the GS/Hecke
reduction — the corpus's own `gb_filtration_jet_tracker` — supplies it instead.

RESULT (derive-then-check; two gradings, two different answers):

  [G1] The COXETER grading cannot do it. The image of w^n in S₃ is (s₁s₂)ⁿ,
       and s₁s₂ is a 3-cycle, so the permutation support / length profile of
       the certificate is periodic with period **3**, not 2. The Coxeter
       (filtration-grade) layer sees n mod 3 and is blind to the parity.
  [G2] The q-GRADING does it exactly. The certificate's total coefficient sum
       Σ_w c_w(q) is a Laurent polynomial of degree exactly 2n−1 with leading
       coefficient exactly (−1)ⁿ — the winding parity, read off the reduction
       output rather than the input word.
  [G3] But it is a FRAMED readout, not yet a knot invariant. Under Markov
       stabilisation the coefficient sum is *unchanged* by a positive
       stabilisation (β ↦ βσ_n) and *multiplied by (1 − h)*, h = q − q⁻¹, by a
       negative one (β ↦ βσ_n⁻¹) — i.e. it transforms by the writhe. On the
       canonical family this is harmless because w^n has exponent sum 0
       (n positive and n negative letters), so no writhe correction is needed
       and the parity readout is stable; for a general braid the readout must
       be writhe-normalised first.

HONEST SCOPE. This is a *partial* wire and is reported as such. It converts the
parity from "asserted from the w^n presentation" to "read off the reduction
certificate of that word", and it identifies WHICH grading carries it (q, not
Coxeter) — a real narrowing. It does NOT yet deliver the full winding class
(m,ℓ), and the identification "leading sign = winding parity" is verified on
the zero-writhe canonical family only; knots outside that family are untested
and would need the writhe normalisation of [G3] first. No Δ_λ value, no c_k,
no magnitude, nothing wired to production.
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

from gb_filtration_jet_tracker import (  # noqa: E402
    HeckeElement, coxeter_length, perm_apply_s, q, H)
from witness_base import WitnessBuilder  # noqa: E402

# NOTE: `q` and `H` are imported from the tracker rather than re-declared.
# Re-declaring `sp.Symbol("q", positive=True)` mints a DIFFERENT sympy symbol
# from the tracker's (same name, different assumptions), so any comparison
# against a `sympify`-ed certificate string silently never simplifies to 0.
W = [1, -2]                      # the half-figure-eight word w = σ₁σ₂⁻¹
NMAX = 8


def build(n_strands: int, word: list) -> HeckeElement:
    E = HeckeElement.identity(n_strands)
    for g in word:
        E = E.right_mul_T(abs(g)) if g > 0 else E.right_mul_T_inv(abs(g))
    return E


def coeff_sum(E: HeckeElement):
    """Σ_w c_w(q) — the certificate's total coefficient, a Laurent poly in q."""
    return sp.expand(sp.simplify(sum(sp.sympify(c) for c in E.terms.values())))


def laurent_top(expr):
    """(degree, leading coefficient) of a Laurent polynomial in q."""
    e = sp.cancel(sp.together(expr))
    num, den = sp.fraction(e)
    pn = sp.Poly(sp.expand(num), q)
    pd = sp.Poly(sp.expand(den), q)
    return pn.degree() - pd.degree(), sp.simplify(pn.LC() / pd.LC())


def perm_image(word: list, n_strands: int) -> tuple:
    p = tuple(range(1, n_strands + 1))
    for g in word:
        p = perm_apply_s(p, abs(g))
    return p


def main() -> int:
    print("=" * 78)
    print(" GAP-2: is the winding parity readable from the GS reduction certificate?")
    print("=" * 78)

    # ---- [G1] Coxeter grading: period 3, blind to parity --------------------
    print("\n [G1] Coxeter layer — image of w^n in S₃ and the grade profile")
    print("      n | perm image | ℓ | grades present")
    images, profiles = [], []
    for n in range(1, NMAX + 1):
        E = build(3, W * n)
        img = perm_image(W * n, 3)
        grades = tuple(sorted(E.filtration_certificate().keys()))
        images.append(img)
        profiles.append((img, grades))
        print(f"      {n} | {img} | {coxeter_length(img)} | {list(grades)}")
    period3 = all(images[i] == images[i + 3] for i in range(len(images) - 3))
    parity_blind = images[1] != images[3]          # n=2 vs n=4: same parity, ≠ image
    g1 = period3 and parity_blind
    print(f"      period-3 in n: {period3};  parity-blind (image(2) ≠ image(4)): {parity_blind}")
    print(f"      ⇒ the Coxeter/filtration grading sees n mod 3, NOT the parity: {bool(g1)}")

    # ---- [G2] q-grading: degree 2n−1, leading coefficient (−1)^n ------------
    print("\n [G2] q-grading — total coefficient sum Σ_w c_w(q)")
    print("      n | deg | leading coeff | (−1)ⁿ | match")
    g2 = True
    degs, leads = [], []
    for n in range(1, NMAX + 1):
        d, lc = laurent_top(coeff_sum(build(3, W * n)))
        degs.append(d)
        leads.append(lc)
        ok = (d == 2 * n - 1) and (sp.simplify(lc - (-1) ** n) == 0)
        g2 &= ok
        print(f"      {n} | {d} | {lc} | {(-1)**n} | {'OK' if ok else 'MISMATCH'}")
    print(f"      degree = 2n−1 and leading coeff = (−1)ⁿ for all n ≤ {NMAX}: {bool(g2)}")
    print("      ⇒ the q-grading DOES carry the winding parity, read off the reduction.")

    # ---- [G3] Markov behaviour: framed, not yet a knot invariant ------------
    print("\n [G3] Markov stabilisation — is the readout a knot invariant?")
    g3 = True
    for n in (2, 3):
        base = coeff_sum(build(3, W * n))
        pos = coeff_sum(build(4, W * n + [3]))
        neg = coeff_sum(build(4, W * n + [-3]))
        same_pos = sp.simplify(pos - base) == 0
        neg_ratio = sp.simplify(sp.cancel(neg / base))
        is_1mh = sp.simplify(neg_ratio - (1 - H)) == 0
        g3 &= same_pos and is_1mh
        knot = "4₁" if n == 2 else "Borromean"
        print(f"      n={n} ({knot}): +stab unchanged: {same_pos};  "
              f"−stab ratio = {neg_ratio}  = (1−h): {is_1mh}")
    exps = [sum(1 if g > 0 else -1 for g in W * n) for n in range(1, NMAX + 1)]
    zero_writhe = all(e == 0 for e in exps)
    g3 &= zero_writhe
    print(f"      exponent sum of w^n is 0 for all n: {zero_writhe}")
    print("      ⇒ FRAMED readout (transforms by the writhe); harmless on the")
    print("        zero-writhe canonical family, but a general braid needs")
    print("        writhe-normalisation before the parity readout is knot-level.")

    # ---- [G4] machinery cross-check against the tracker's ground truth ------
    print("\n [G4] cross-check: σ₁³ in H₂ (tracker docstring ground truth)")
    E = build(2, [1, 1, 1])
    # use the live sympy coefficients (tracker symbols), not the stringified cert
    bygrade = {coxeter_length(w): c for w, c in E.terms.items()}
    c1 = sp.simplify(bygrade[1] - (H**2 + 1))
    c0 = sp.simplify(bygrade[0] - H)
    g4 = (c1 == 0) and (c0 == 0)
    print(f"      grade1 coeff = (q−q⁻¹)²+1: {c1 == 0};  grade0 coeff = q−q⁻¹: {c0 == 0}")
    print(f"      ⇒ reduction machinery driven correctly: {bool(g4)}")

    print("\n ⇒ PARTIAL WIRE. Parity is readable from the certificate — via the")
    print("   q-grading, not the Coxeter grading — as a framed quantity that is")
    print("   stable on the zero-writhe canonical family. Full (m,ℓ) not delivered.")

    wb = WitnessBuilder("gb-winding-parity-wire", engine="sympy")
    wb.set_description(
        "GAP-2 (bean qou-rbfr, epic qou-xu6t): whether the winding parity behind the merged "
        "#4401 sign mechanism can be READ OFF the Gröbner–Shirshov reduction certificate of a "
        "braid word rather than asserted from its w^n presentation (w = σ₁σ₂⁻¹, 4₁ = w², "
        "Borromean = w³). Two gradings answer differently. COXETER grading: the image of w^n "
        "in S₃ is (s₁s₂)ⁿ with s₁s₂ a 3-cycle, so the permutation support / grade profile is "
        "periodic with period 3 — it sees n mod 3 and is blind to the parity. q-GRADING: the "
        "certificate's total coefficient sum is a Laurent polynomial of degree exactly 2n−1 "
        "with leading coefficient exactly (−1)ⁿ — the winding parity, verified n = 1..8. "
        "MARKOV: that readout is FRAMED, not yet a knot invariant — unchanged under positive "
        "stabilisation, multiplied by (1−h) under negative stabilisation (h = q−q⁻¹); harmless "
        "on the canonical family because w^n has exponent sum 0, but a general braid needs "
        "writhe-normalisation first. PARTIAL WIRE, reported as such: converts the parity from "
        "presentation-asserted to certificate-derived and identifies which grading carries it, "
        "but does not deliver the full winding class (m,ℓ), and is verified on the zero-writhe "
        "canonical family only. No Δ_λ, no c_k, no magnitude, nothing wired.")
    wb.set_content_block("prop:winding-lattice-norm-form")
    wb.add_data("wire_readout", {
        "coxeter_layer": "image of w^n in S₃ = (s₁s₂)ⁿ, period 3 ⇒ sees n mod 3, parity-blind",
        "q_layer": "Σ_w c_w(q) has degree 2n−1, leading coefficient (−1)ⁿ (n = 1..8)",
        "degrees": str(degs),
        "leading_coeffs": str([str(l) for l in leads]),
        "markov_positive_stabilisation": "coefficient sum unchanged",
        "markov_negative_stabilisation": "coefficient sum × (1 − h), h = q − q⁻¹",
        "canonical_family_writhe": "exponent sum of w^n = 0 for all n (no correction needed)",
        "verdict": ("PARTIAL WIRE — parity is certificate-derivable via the q-grading (not the "
                    "Coxeter grading), as a framed quantity stable on the zero-writhe canonical "
                    "family; full (m,ℓ) still open, general-braid case needs writhe "
                    "normalisation")})
    wb.add_assertion("coxeter_grading_period3_parity_blind", str(bool(g1)), "True")
    wb.add_assertion("q_grading_leading_sign_equals_winding_parity", str(bool(g2)), "True")
    wb.add_assertion("readout_is_framed_zero_writhe_family_stable", str(bool(g3)), "True")
    wb.add_assertion("tracker_ground_truth_sigma1_cubed", str(bool(g4)), "True")
    wb.save()
    print("\nwitness → gb-winding-parity-wire.witness.json")
    ok = all([g1, g2, g3, g4])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
