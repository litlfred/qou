#!/usr/bin/env python3
"""q = 1 interface selectivity — does a q -> 1 layer separate leptons from baryons?

Bean qou-itdn.  EXACT arithmetic throughout (sympy Rational / symbolic); no
float appears in any computation, per the NO-FLOAT64 discipline, which binds
probes exactly as it binds producers (AGENTS.md, owner directive 2026-08-18).

THE QUESTION.  At q = 1 the Hecke algebra H_n(1) collapses to the group algebra
C[S_n] and the braid group surjects onto S_n, so knotting is forgotten.  The
bean asks whether that collapse is SELECTIVE: leptons trivialise but baryons
do not, which would make a q = 1 surface transparent to one and not the other.

WHAT THIS PROBE ESTABLISHES (and what it does not).
  1. VERIFIES, on explicit Jones polynomials taken from the literature, that
     V_L(1) = (-2)^(c-1) depends ONLY on the component count c.  This is a
     standard fact (Jones 1985); it is CHECKED here, not assumed.
  2. EVALUATES it on the corpus's own particle assignments.
  3. States precisely the gap between that and any transport claim.

It does NOT establish that a q = 1 region separates charge.  That needs a
transport calculation this probe does not perform -- see VERDICT below.
"""
import sys
import sympy as sp

t = sp.symbols('t')

# ── Jones polynomials, V_L(t), from the literature.  INPUTS, not derived here.
#    Ref: Jones (1985); Lickorish, "An Introduction to Knot Theory", Table 3.1;
#    Kauffman (1987).  Each is checked below against the component-count law,
#    which is what makes a transcription error visible rather than silent.
LINKS = {
    # name                     components, V_L(t)
    "0_1 unknot":              (1, sp.Integer(1)),
    "3_1 trefoil":             (1, -t**(-4) + t**(-3) + t**(-1)),
    "4_1 figure-eight":        (1, t**(-2) - t**(-1) + 1 - t + t**2),
    "5_1 cinquefoil":          (1, -t**(-7) + t**(-6) - t**(-5) + t**(-4) + t**(-2)),
    "5_2 three-twist":         (1, -t**(-6) + t**(-5) - t**(-4) + 2*t**(-3) - t**(-2) + t**(-1)),
    # 2-component
    "Hopf link":               (2, -t**sp.Rational(-5,2) - t**sp.Rational(-1,2)),
    "unlink of 2":             (2, -t**sp.Rational(-1,2) - t**sp.Rational(1,2)),
    # 3-component
    "Borromean rings":         (3, -t**(-3) + 3*t**(-2) - 2*t**(-1) + 4 - 2*t + 3*t**2 - t**3),
    "unlink of 3":             (3, (-t**sp.Rational(-1,2) - t**sp.Rational(1,2))**2),
}

# ── The corpus's own particle -> diagram assignments.
#    electron = trefoil sigma_1^3  (computations/canonical_lepton_braid_words.py:13,63)
#    muon     = 4_1 figure-eight   (canonical paper; same file, lines 21-36)
#    proton/neutron = Borromean linking of 3 quarks
#                    (computations/complex_fibre_cross_ratio.py:329)
QOU_ASSIGNMENT = {
    "electron": "3_1 trefoil",
    "muon":     "4_1 figure-eight",
    "proton":   "Borromean rings",
    "neutron":  "Borromean rings",
}


def component_count_law(c: int) -> sp.Expr:
    """The claim under test: V_L(1) = (-2)^(c-1), a function of c ALONE."""
    return sp.Integer(-2) ** (c - 1)


def main() -> int:
    print("=" * 74)
    print("q = 1 INTERFACE SELECTIVITY  (bean qou-itdn)")
    print("=" * 74)

    print("\n[1] V_L(1) depends only on the component count -- CHECKED, not assumed\n")
    print(f"    {'link':<24} {'c':>2}  {'V_L(1)':>8}  {'(-2)^(c-1)':>11}  match")
    print(f"    {'-'*24} {'-'*2}  {'-'*8}  {'-'*11}  -----")
    all_ok = True
    values = {}
    for name, (c, V) in LINKS.items():
        at1 = sp.simplify(V.subs(t, 1))
        law = component_count_law(c)
        ok = sp.simplify(at1 - law) == 0
        all_ok &= ok
        values[name] = at1
        print(f"    {name:<24} {c:>2}  {str(at1):>8}  {str(law):>11}  {'OK' if ok else 'FAIL'}")

    if not all_ok:
        print("\n    A row FAILED. Either a polynomial is mistranscribed or the law is")
        print("    wrong; the probe cannot tell which, so it stops rather than guess.")
        return 1
    print(f"\n    {len(LINKS)}/{len(LINKS)} agree, exactly (sympy Rational, no float).")

    print("\n[2] The sharp form of the collapse\n")
    print("    Distinct KNOTS (c=1) with distinct V_L(t) all collapse to the SAME")
    print("    value at t=1.  Demonstrated on the c=1 rows above:")
    knots = [(n, v) for n, (c, _) in LINKS.items() if c == 1 for v in [values[n]]]
    distinct_polys = len({sp.srepr(sp.expand(LINKS[n][1])) for n, _ in knots})
    distinct_at1 = len({sp.srepr(v) for _, v in knots})
    print(f"      {len(knots)} knots, {distinct_polys} distinct polynomials, "
          f"{distinct_at1} distinct value(s) at t=1")
    assert distinct_at1 == 1, "knots must collapse to a single value"
    print("    So at q = 1 the Jones invariant retains EXACTLY ONE BIT of the")
    print("    topology: the component count.  All knotting is forgotten.")

    print("\n[3] Evaluated on the corpus's particle assignments\n")
    print(f"    {'particle':<10} {'diagram':<24} {'c':>2}  {'V(1)':>6}  transparent?")
    print(f"    {'-'*10} {'-'*24} {'-'*2}  {'-'*6}  ------------")
    for particle, diagram in QOU_ASSIGNMENT.items():
        c, _ = LINKS[diagram]
        v1 = values[diagram]
        transparent = (v1 == 1)
        print(f"    {particle:<10} {diagram:<24} {c:>2}  {str(v1):>6}  "
              f"{'YES (= unknot)' if transparent else 'no'}")

    print("\n[4] The selectivity statement, exactly\n")
    print("    V_L(1) = 1  <->  (-2)^(c-1) = 1  <->  c = 1,")
    print("    since |-2| > 1 makes the map c -> (-2)^(c-1) injective on c >= 1.")
    for c in range(1, 7):
        v = component_count_law(c)
        print(f"      c = {c}:  (-2)^(c-1) = {str(v):>4}   "
              f"{'<- the ONLY c with the unknot value' if v == 1 else ''}")

    print("\n[5] VERDICT -- scope (a), and the gap is named\n")
    print("    ESTABLISHED: at q = 1 the Jones invariant of a lepton (c=1) equals")
    print("    that of the unknot, while a baryon's (c=3, Borromean) equals 4.")
    print("    The collapse is therefore SELECTIVE ON COMPONENT COUNT, and the")
    print("    lepton/baryon split in this framework is exactly a c=1 / c=3 split.")
    print()
    print("    NOT ESTABLISHED -- and this is the whole distance to the bean's")
    print("    question:  that the interface ACTS through the Jones invariant.")
    print("    'V_L(1) equals the unknot's value' is a statement about an")
    print("    INVARIANT, not about transmission, energy cost, or flux.  Reading")
    print("    it as 'the layer is transparent to leptons' requires a transport")
    print("    calculation -- what a wavefunction does crossing a region where q")
    print("    varies -- which nothing in this corpus performs.  Without it, the")
    print("    charge-separation claim is an analogy, not a derivation.")
    print()
    print("    Note also that charge is NOT a function of component count: the")
    print("    neutron and the proton share the Borromean assignment and c = 3,")
    print("    so this mechanism CANNOT distinguish them.  Any charge-separation")
    print("    story built on c alone therefore fails at its first test case.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
