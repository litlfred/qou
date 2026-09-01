#!/usr/bin/env python3
"""
brng_hbarq2_saturation_genericity_probe — is B/A/m_N ≈ ℏ_q² a derivation or numerology?

Bean qou-brng, residual R3. The arc records that the saturated nuclear binding fraction
B/A/m_N rises toward ℏ_q² with A (⁴He 0.77·ℏ_q² → ⁵⁶Fe 0.95·ℏ_q²). The volume-defect
mechanism was refuted (2026-08-21), so the ≈ℏ_q² match has no candidate mechanism. This
probe MEASURES how special the match is, WITHOUT forcing it (numerology guard; scope-(a)).

The discriminating question: WHICH saturation value is ℏ_q² being compared to?

  (i)  the empirical B/A PEAK (~8.79 MeV at ⁵⁶Fe / ~8.795 at ⁶²Ni) — a volume MINUS
       surface MINUS Coulomb balance, and NOT a fundamental constant: it is A-dependent,
       peaks near A≈60, and DECREASES for heavy nuclei; or
  (ii) the fundamental nuclear VOLUME coefficient a_V ≈ 15.75 MeV (semi-empirical mass
       formula) — the true A→∞ bulk binding per nucleon before surface/Coulomb.

If ℏ_q² matches (i) but not (ii), it is matching an accidental balance point, not a
saturation constant — evidence for numerology, not derivation.

NO FLOAT64: all arithmetic in mpmath.mpf. Floats appear only inside display f-strings.
"""

import mpmath as mp

mp.mp.dps = 50

# ── inputs (all as exact-string mpf) ───────────────────────────────────────────
# proton-anchored substrate modulus q₀ (AGENTS.md: default experimental pin)
Q0 = mp.mpf("1.1099785827513808")
HBAR_Q = 1 - 1 / Q0
HBAR_Q2 = HBAR_Q ** 2

# average nucleon mass scale (MeV) — the arc's m_N in B/A/m_N
M_N = mp.mpf("939.0")

# AME2020 binding energies B (MeV) and mass number A. Standard values.
# (B is total binding; B/A is binding per nucleon.)
AME = [
    ("2H",   mp.mpf("2.224566"),   2),
    ("4He",  mp.mpf("28.295674"),  4),
    ("12C",  mp.mpf("92.161728"),  12),
    ("16O",  mp.mpf("127.619336"), 16),
    ("40Ca", mp.mpf("342.052087"), 40),
    ("56Fe", mp.mpf("492.253892"), 56),
    ("62Ni", mp.mpf("545.259126"), 62),   # the actual B/A peak
    ("120Sn", mp.mpf("1020.544"),  120),
    ("238U", mp.mpf("1801.693"),   238),  # heavy: B/A has fallen back
]

# Bethe–Weizsäcker VOLUME coefficient a_V (MeV). Standard fits give ~15.5–15.8 MeV;
# use a representative value and also bracket it.
A_V = mp.mpf("15.75")
A_V_LO = mp.mpf("15.5")
A_V_HI = mp.mpf("15.8")


def fmt(x, n=6):
    return mp.nstr(x, n)


def main():
    print("=" * 74)
    print("brng R3 — is B/A/m_N ≈ ℏ_q² a derivation or numerology? (scope-(a) measure)")
    print("=" * 74)
    print(f"q₀ (proton)   = {fmt(Q0, 12)}")
    print(f"ℏ_q = 1−1/q₀  = {fmt(HBAR_Q, 10)}")
    print(f"ℏ_q²          = {fmt(HBAR_Q2, 10)}  (= {fmt(HBAR_Q2*100,6)} %)")
    print(f"m_N           = {fmt(M_N)} MeV")
    print()

    # ── (i) the empirical B/A curve and its ratio to ℏ_q² ──────────────────────
    print("-" * 74)
    print("(i) empirical B/A/m_N vs ℏ_q²  —  does it saturate AT ℏ_q², or peak below it?")
    print("-" * 74)
    print(f"{'nuc':>6} {'A':>4} {'B/A(MeV)':>10} {'B/A/m_N':>11} {'÷ℏ_q²':>9}")
    peak_ratio = mp.mpf("0")
    peak_nuc = None
    for name, B, A in AME:
        BA = B / A
        frac = BA / M_N
        ratio = frac / HBAR_Q2
        if ratio > peak_ratio:
            peak_ratio = ratio
            peak_nuc = name
        print(f"{name:>6} {A:>4} {fmt(BA,6):>10} {fmt(frac,6):>11} {fmt(ratio,5):>9}")
    print()
    print(f"peak of B/A/m_N ÷ ℏ_q²  = {fmt(peak_ratio,5)}  at {peak_nuc}")
    print(f"  → the curve PEAKS at {fmt(peak_ratio,4)}·ℏ_q² (< 1) near A≈60 and then FALLS")
    print(f"    (²³⁸U back down to {fmt((AME[-1][1]/AME[-1][2])/M_N/HBAR_Q2,4)}·ℏ_q²).")
    print(f"    So B/A/m_N does NOT saturate at ℏ_q² — it never reaches it, and the")
    print(f"    'approach' reverses. The match is to an A-dependent BALANCE point.")
    print()

    # ── (ii) the fundamental volume coefficient a_V ────────────────────────────
    print("-" * 74)
    print("(ii) the FUNDAMENTAL bulk coefficient a_V/m_N  —  the true A→∞ saturation")
    print("-" * 74)
    for tag, av in (("a_V=15.5", A_V_LO), ("a_V=15.75", A_V), ("a_V=15.8", A_V_HI)):
        r = (av / M_N) / HBAR_Q2
        print(f"  {tag:>10} MeV : a_V/m_N = {fmt(av/M_N,6)} = {fmt(r,5)}·ℏ_q²")
    print()
    r_av = (A_V / M_N) / HBAR_Q2
    print(f"  → the fundamental volume coefficient is ≈ {fmt(r_av,4)}·ℏ_q², NOT ℏ_q².")
    print(f"    ℏ_q² ≈ 0.95·(B/A peak) but ≈ {fmt(1/r_av,4)}·a_V/m_N. The peak matches")
    print(f"    because volume MINUS surface MINUS Coulomb happens to land near ℏ_q²·m_N")
    print(f"    at A≈60; the bulk binding itself is ~{fmt(r_av,3)}× larger.")
    print()

    # ── genericity: how wide is the window of 'nice' constants matching the peak? ─
    print("-" * 74)
    print("genericity — how special is ℏ_q² among simple substrate constants?")
    print("-" * 74)
    peak_frac = (AME[6][1] / AME[6][2]) / M_N   # 62Ni peak B/A/m_N
    print(f"target (⁶²Ni peak B/A/m_N) = {fmt(peak_frac,6)}")
    cands = [
        ("ℏ_q²",          HBAR_Q2),
        ("ℏ_q²·(q₀)",     HBAR_Q2 * Q0),
        ("(1−1/q₀)²",     HBAR_Q2),
        ("ℏ_q³ + ℏ_q²",   HBAR_Q**3 + HBAR_Q2),
        ("1/102",         mp.mpf(1)/102),
        ("(q₀−1)²",       (Q0-1)**2),
        ("ℏ_q²/0.95",     HBAR_Q2/mp.mpf("0.95")),
    ]
    print(f"{'constant':>14} {'value':>12} {'/target':>9}")
    within = 0
    for nm, v in cands:
        rr = v / peak_frac
        mark = "  ← within 6%" if abs(rr - 1) < mp.mpf("0.06") else ""
        if abs(rr - 1) < mp.mpf("0.06"):
            within += 1
        print(f"{nm:>14} {fmt(v,6):>12} {fmt(rr,4):>9}{mark}")
    print()
    print(f"  {within} of {len(cands)} simple constants land within 6% of the peak — ℏ_q²")
    print(f"  is not uniquely picked out; several substrate expressions match equally.")
    print()

    print("=" * 74)
    print("VERDICT (scope-(a), numerology guard): the ≈ℏ_q² match is to the empirical")
    print("B/A PEAK — an A-dependent volume−surface−Coulomb balance near A≈60 — NOT to")
    print("the fundamental volume coefficient a_V/m_N ≈ %s·ℏ_q², and not a saturation" % fmt(r_av,3))
    print("LIMIT (the curve peaks below ℏ_q² and falls). With the volume-defect")
    print("mechanism already refuted and no substrate route selecting the balance")
    print("point, R3 is MORE numerology-suspect, not less. Do NOT wire; do NOT force to 1.")
    print("=" * 74)


if __name__ == "__main__":
    main()
