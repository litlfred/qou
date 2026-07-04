"""∂_q continuity law for the QOU mass–energy relation — the Magueijo–Barrow analogue.

Follow-up #2 of the 2026-07-02 Bekenstein/VSL review (bean 4big, §3.3 + §5):
Magueijo–Barrow's central technical content is the *modified continuity
equation* — what sources what when c varies. The review flagged that the QOU
corpus proves E = 𝔪·c_q² at each fixed q but has no ∂_q statement of whether
mass, energy, or neither is conserved as q flows. This probe supplies the
rigorous ∂_q identity (calculus on a PROVED theorem — not a new postulate) and
tests the review's candidate identification of the source term.

Objects (all from the corpus, exact):
    c_q = 1/(q−1)                        thm:mass-energy-equivalence / def:information-speed-of-light
    E   = 𝔪·c_q² = 𝔪/(q−1)²             thm:mass-energy-equivalence (proved)
    ℏ_q = (q−1)/q
    F_q ∝ (q−1)                          prop:germ-commutator-q-curvature (F_q = (q−1)𝓕_q^intr)

Results (all sympy-exact):
  1. c_q obeys the autonomous ODE  dc_q/dq = −c_q²  (its defining property).
  2. Differentiating E = 𝔪(q)·c_q² gives the CONTINUITY LAW
         dE/dq + 2 c_q E = c_q² · d𝔪/dq.
     The 2 c_q E term is the c_q-variation source — the QOU analogue of
     Magueijo–Barrow's −(ċ/c)·ρc² source; it vanishes iff q is fixed.
  3. With 𝔪 q-independent (the topological/fibre content is scale-free),
     dE/dq = −2 c_q E ≠ 0: crossing energy is NOT conserved along the q-flow —
     it scales as c_q². Categorical mass is the q-invariant; energy is
     created/destroyed by the varying c_q, exactly the MB phenomenology.
  4. The review's candidate "tie the source to the germ-commutator F_q" does
     NOT hold: the source coefficient 2c_q ∝ (q−1)⁻¹ scales INVERSELY to
     F_q ∝ (q−1). The source is intrinsically the c_q ODE (−c_q²), not F_q.

SELF-CONTAINED (docs/audits/scripts convention): pure sympy, no repo imports.
Scope: the ∂_q identity is rigorous; the cosmological reading (q = cosmic time)
is bracketed-speculative per the corpus (q-harmonic-flow is a conjecture/ansatz,
not a derived PDE). NOT wired, NOT a fit, CAL untouched.

Exit 0.
"""

from __future__ import annotations

import sympy as sp


def main():
    q, m = sp.symbols("q m", positive=True)
    c = 1 / (q - 1)                       # c_q
    hbar = (q - 1) / q                    # ℏ_q

    checks = {}

    # 1. autonomous ODE
    checks["dc_q/dq = -c_q^2"] = sp.simplify(sp.diff(c, q) - (-c ** 2)) == 0

    # 2. continuity law for E = m(q) c_q^2
    mq = sp.Function("m")(q)
    E = mq * c ** 2
    residual = sp.diff(E, q) + 2 * c * E - c ** 2 * sp.diff(mq, q)
    checks["dE/dq + 2 c_q E = c_q^2 dm/dq"] = sp.simplify(residual) == 0

    # 3. m q-independent => E not conserved (dE/dq = -2 c_q E)
    dEdq_const_m = sp.diff(E, q).subs(sp.diff(mq, q), 0).subs(mq, m)
    checks["const m: dE/dq = -2 c_q E (=> not conserved)"] = (
        sp.simplify(dEdq_const_m - (-2 * c * m * c ** 2)) == 0
        and dEdq_const_m != 0
    )

    # 4. germ-commutator tie-in fails: 2 c_q ~ (q-1)^-1 vs F_q ~ (q-1)^+1
    #    (opposite sign of the (q-1) exponent — no clean identification)
    exp_source = sp.degree(sp.together(2 * c).as_numer_denom()[1], q)  # denom power
    checks["source 2 c_q scales as (q-1)^-1 (inverse of F_q ~ (q-1))"] = exp_source == 1

    # bonus corpus relation
    checks["c_q * hbar_q = 1/q"] = sp.simplify(c * hbar - 1 / q) == 0

    print("=" * 66)
    print("∂_q mass–energy continuity law — QOU / Magueijo–Barrow analogue")
    print("=" * 66)
    print("c_q = 1/(q−1),  E = 𝔪·c_q²,  ℏ_q = (q−1)/q  (all from the corpus)\n")
    print("  CONTINUITY LAW:   dE/dq + 2 c_q E = c_q² · d𝔪/dq")
    print("  (2 c_q E = the c_q-variation source; the MB −(ċ/c)ρc² analogue)\n")
    for name, ok in checks.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print()
    print("Conserved quantity: categorical mass 𝔪 (topological/fibre, scale-free)")
    print("is the q-invariant; crossing energy E = 𝔪·c_q² is NOT conserved along")
    print("the q-flow — it scales as c_q², so a varying c_q sources energy exactly")
    print("as in minimal Magueijo–Barrow VSL.")
    print()
    print("Review's germ-commutator tie-in: DOES NOT HOLD — source 2c_q ∝ (q−1)⁻¹")
    print("scales inversely to F_q ∝ (q−1); the source is the intrinsic c_q ODE.")
    print()
    print("Scope: ∂_q identity rigorous (calculus on a proved theorem); the")
    print("q = cosmic-time reading stays bracketed-speculative (q-harmonic-flow")
    print("is a conjecture/ansatz, not a derived PDE).")

    assert all(checks.values()), "a symbolic check failed"


if __name__ == "__main__":
    main()
