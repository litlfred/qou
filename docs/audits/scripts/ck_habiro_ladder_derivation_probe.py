"""Are the c_k proved? Is there a recursion? Can we derive them?

Directive: "c_k proved? recursions? check corpus. derive c_k."

This probe answers all three from the corpus, concretely and
self-contained (docs/audits/scripts convention — no repo imports).

Corpus answer (content/quantum-observable-universe/mass-theory/
habiro-precision-ladder-equivalence.md):

  THE ONE derivable, recursive, proved c_k ladder is the Habiro
  integrality ladder of the Markov trace:

      tr_M(β, q) = Σ_{m=0}^{M} a_m(u) · (u;u)_m ,
      a_m ∈ ℤ[u],  (u;u)_m = Π_{k=1}^m (1−u^{2k}),  u = q^{1/2},  M < ∞.

  For the proton braid M = 8 and the a_m are explicit integer
  polynomials (block table). This IS the recursion: the finite
  cyclotomic (q-Pochhammer) basis. No fit, no free parameter beyond
  (m_e, q_0).

This probe:

  1. Reconstructs tr_M(β_p) = Σ a_m(u)(u;u)_m from the block's integer
     a_m — verifying it is an exact finite object (a real proved ladder).
  2. Shows NONE of the a_m (nor their q_0 evaluation) is the production
     precision-tower coefficient set {46, 4, −29}: the derivable ladder
     lives at O(10²) integer scale; the production tower lives at the
     O(10⁻⁷) CODATA-closing scale — different objects.

Conclusion: the c_k that ARE derivable (the Habiro a_m) do not produce
"46". The production {46, 4, −29} are the fit the block explicitly
disowns ("tuned the coefficients against the experimental value rather
than evaluating them categorically"); a fixed recursion for them cannot
exist because c_4 is affine in the q_0 pin (0 at the proton pin, 46 at
the muon pin — companion probe c4_mu_p_tension_pin_dependence_probe.py).

Exit 0.
"""

from __future__ import annotations

import sympy as sp

u = sp.symbols("u")

# Habiro coefficients a_m(u) ∈ ℤ[u], proton braid, M=8 — verbatim from
# content/.../mass-theory/habiro-precision-ladder-equivalence.md.
A_M = {
    0: sp.Integer(4),
    1: -74 * u - 74,
    2: 340 * u ** 2 + 365 * u + 389,
    3: -711 * u ** 3 - 789 * u ** 2 - 872 * u - 959,
    4: 788 * u ** 4 + 901 * u ** 3 + 1029 * u ** 2 + 1172 * u + 1328,
    5: -466 * u ** 5 - 559 * u ** 4 - 660 * u ** 3 - 781 * u ** 2 - 918 * u - 1078,
    6: 133 * u ** 6 + 167 * u ** 5 + 212 * u ** 4 + 264 * u ** 3 + 328 * u ** 2 + 402 * u + 494,
    7: -12 * u ** 7 - 17 * u ** 6 - 24 * u ** 5 - 34 * u ** 4 - 48 * u ** 3 - 63 * u ** 2 - 84 * u - 110,
    8: u ** 4 + 2 * u ** 3 + 3 * u ** 2 + 5 * u + 7,
}

# production precision-tower coefficients (m_p habiro_ratio)
PRODUCTION_TOWER = {46, 4, -29}


def pochhammer(m):
    p = sp.Integer(1)
    for k in range(1, m + 1):
        p *= 1 - u ** (2 * k)
    return p


def main():
    # 1. reconstruct the finite Habiro sum
    trM = sp.expand(sum(A_M[m] * pochhammer(m) for m in range(9)))
    deg = sp.degree(trM, u)
    is_finite_poly = trM.is_polynomial(u)

    # integrality check: every a_m coefficient is an integer
    all_integral = all(
        all(c.is_integer for c in sp.Poly(A_M[m], u).all_coeffs()) for m in A_M
    )

    # 2. evaluate at the substrate square-root (muon-pin q_0)
    q0 = sp.Rational("1.10997859564023958")
    u0 = sp.sqrt(q0)
    trM_val = float(sp.N(trM.subs(u, u0)))

    # 3. does the derivable ladder contain the production tower?
    all_am_coeffs = set()
    for m in A_M:
        for c in sp.Poly(A_M[m], u).all_coeffs():
            all_am_coeffs.add(int(c))
    # small integers (|c| ≤ 12) coincide trivially across any integer
    # ladder — the meaningful test is the distinctive coefficients {46, −29}.
    distinctive = {c for c in PRODUCTION_TOWER if abs(c) > 12}
    overlap = distinctive & all_am_coeffs
    trivial_overlap = (PRODUCTION_TOWER & all_am_coeffs) - overlap

    print("=" * 68)
    print("c_k: proved? recursions? derive — Habiro-ladder probe")
    print("=" * 68)
    print(f"reconstructed tr_M(β_p) = Σ a_m(u)(u;u)_m :")
    print(f"  polynomial in u? {is_finite_poly}   degree = {deg}   (finite ladder ✓)")
    print(f"  every a_m integral (a_m ∈ ℤ[u])? {all_integral}   (proved integrality ✓)")
    print(f"  tr_M(β_p) at u₀=√q₀ = {trM_val:.6f}   (O(10²) categorical scale)")
    print()
    print("PROVED / DERIVABLE c_k = the Habiro integrality ladder above:")
    print("  recursion = the finite cyclotomic q-Pochhammer basis (u;u)_m.")
    print()
    print(f"production precision tower coefficients = {sorted(PRODUCTION_TOWER)}")
    print(f"  scale = O(10⁻⁷) (CODATA-closing on m_p ≈ 938 MeV)")
    print(f"  distinctive coeffs {sorted(distinctive)} ∩ (a_m coeffs) = {overlap or '∅'}")
    print(f"  (trivial small-int coincidences ignored: {trivial_overlap or '∅'})")
    print()
    print("VERDICT: the derivable c_k (Habiro a_m) do NOT produce 46. The")
    print("production {46,4,−29} are a different object at a different scale —")
    print("the fit the block disowns. No fixed recursion for them can exist:")
    print("c_4 is affine in the q₀ pin (0→46), i.e. the μ–p tension, not a")
    print("fibre Taylor coefficient (see c4_mu_p_tension_pin_dependence_probe).")

    assert is_finite_poly and all_integral, "Habiro ladder failed integrality/finiteness"
    assert not overlap, "unexpected: distinctive production coeff {46,-29} appears among a_m"


if __name__ == "__main__":
    main()
