#!/usr/bin/env python3
"""
Probe — the deuteron has exactly ONE chain bond, so it isolates L_pn.

The canonical braid word is an `A-1` linear chain, so the number of bonds is
`A-1`. At `A = 2` that is **one bond**, and the chain reduces to a single term:

    B_chain(2H) = alpha * L_pn        (no L_pp, no L_nn, no sum)

That makes the deuteron the one place in the table where the chain makes a
prediction with **no internal freedom at all** — one derived constant against
one measured number. Every other isotope mixes three constants, so a
disagreement there can be re-apportioned; here it cannot.

## Why this is the right test for the cross-channel program

The open question on this axis is what supplies the collective binding term `R`
(see `collective_term_budget_probe.py`: mixed-sign in `A`, plateau ~1.9x a
bond's worth per nucleon, extensive in the LINEAR bond count). The natural
candidate class -- the one suggested by cross-channel / non-scalar
representation structure -- is an **interference between bonds**: an off-diagonal
object in the Wedderburn decomposition, which is naturally mixed-sign (it is not
a square) and so passes the sign screen that kills every manifestly non-negative
candidate.

But an interference between bonds **requires at least two bonds**. Any such term
vanishes identically at `A = 2`. So the deuteron is a clean decision point:

* if the chain's single-bond prediction MATCHES at `A = 2`, a
  vanishing-at-one-bond interference term is consistent with the data, and the
  whole budget `R` can be interference;
* if it MISSES, then either the collective term does **not** vanish at one bond
  (so it is not a pure bond-bond interference), or the derived `L_pn` is wrong
  by the size of the miss. One of those two must be true.

This probe measures which, and by how much. It is a comparison of a derived
number against a measured one -- no fit, no ansatz, no coefficient.

## What is NOT claimed

Nothing about what the collective term is. The fork above is a constraint on
candidates, not a derivation. In particular the probe does **not** re-fit `L_pn`
to the deuteron: that would convert a prediction into an anchor and is exactly
the move the three-calibration discipline forbids. The deuteron-implied value is
printed as a *diagnostic of the size of the disagreement*, and must not be wired.

NO WITNESS: one derived constant against one AME row; the printed lines
reproduce it.

Bean qou-x66y follow-on; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import math
import sys

import mass_binding_dashboard as mbd

# (name, Z, N) for the light band -- bond count is A-1 in every case.
LIGHT = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
         ("6Li", 3, 3), ("7Li", 3, 4)]


def main() -> int:
    me, q0, E0 = mbd._constants()
    alpha = float(E0)
    L = mbd._bond_type_L()
    if isinstance(L, dict):
        Lpp, Lpn, Lnn = float(L["pp"]), float(L["pn"]), float(L["nn"])
    else:
        Lpp, Lpn, Lnn = (float(x) for x in L)
    ame = mbd._ame_table()

    print("The deuteron isolates L_pn — one bond, one constant, no freedom\n")
    print(f"  alpha = E0 = {alpha:.6f} MeV      q0 = {q0!r}")
    print(f"  L_pp = {Lpp:.6f}   L_pn = {Lpn:.6f}   L_nn = {Lnn:.6f}   [DERIVED]\n")

    t2 = ame.get((1, 2))
    if not t2:
        print("  no AME row for 2H — cannot run.")
        return 1
    B2 = float(t2[0])
    pred2 = alpha * Lpn
    rel = (pred2 - B2) / B2

    print("BOND COUNT along the chain (A-1), and how many constants each row mixes:\n")
    print("| iso  |  A | bonds | terms in B_chain                  |")
    print("| ---- | -: | ----: | --------------------------------- |")
    for name, Z, N in LIGHT:
        A = Z + N
        terms = []
        if Z - 1:
            terms.append(f"{Z-1}*L_pp")
        terms.append("L_pn")
        if N - 1:
            terms.append(f"{N-1}*L_nn")
        print(f"| {name:<4} | {A:>2} | {A-1:>5} | {' + '.join(terms):<33} |")
    print("\n  -> only 2H has a single bond, hence a single constant. It is the only")
    print("     row where the chain cannot re-apportion a disagreement.\n")

    print("THE ONE-BOND TEST:\n")
    print(f"  B_chain(2H) = alpha * L_pn = {pred2:.6f} MeV     [DERIVED, no freedom]")
    print(f"  B_AME(2H)                  = {B2:.6f} MeV     [MEASURED]")
    print(f"  -> the chain OVER-binds the deuteron by {rel*100:+.2f} %\n")

    matched = abs(rel) < 0.01
    print(f"  single-bond prediction matches to 1 %: {matched}\n")

    print("## The fork this forces\n")
    if not matched:
        print(f"  The miss is {abs(rel)*100:.1f} %, far outside any measurement error")
        print("  (AME binding energies are known to ~1e-7 relative). So at least one")
        print("  of these is true:\n")
        print("   (i)  the collective term is NONZERO at one bond -- so it is not a")
        print("        pure bond-bond interference, and the cross-channel candidate")
        print("        class must include a term that survives at A = 2; or")
        print("   (ii) a single CONTENT-KEYED p-n bond is the wrong model for the")
        print("        deuteron.\n")
        print("  (ii) is not a hypothesis -- it is already PROVED in the corpus, and")
        print("  that is what makes this measurement worth having. Nature has FOUR")
        print("  two-nucleon channels, and the two p-n rows (3S1 bound at +2.2246,")
        print("  1S0 virtual at -0.066) have IDENTICAL nucleon content and opposite")
        print("  boundness. Any interface assigned from the unordered species pair --")
        print("  which is exactly what a single L_pn is -- must give them the same")
        print("  energy. Formalised sorry-free as `content_keyed_interface_refuted`")
        print("  (QOU/QBeta/InterfaceScalar.lean); see")
        print("  docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md.")
        print("  The variable that works is isospin T, via the Hecke spectral")
        print("  projectors P+- -- free, since their scalars are the n=2 Wedderburn")
        print("  weights y_(2), y_(1,1).\n")
        print(f"  So what this probe adds is the MAGNITUDE: the content-keyed model is")
        print(f"  wrong by {abs(rel)*100:.1f} % at the one place where it has no freedom to")
        print("  hide it. That sizes the isospin splitting the T-resolved replacement")
        print("  has to supply, and it is a number the qualitative refutation could")
        print("  not give. Note also that L_pn is NOT itself in error: it reproduces")
        print("  the exact p(3A) transfer trace to 4.4e-16 (see")
        print("  chain_binding_hyperbola_no_peak_probe.py CHECK 1b). The defect is in")
        print("  what the bond is keyed ON, not in the trace that evaluates it.")
        print("\n  Note the sign agrees with the budget probe: R(2H) < 0 there is the")
        print("  same fact as 'the chain over-binds at A = 2' here. The deuteron is")
        print("  the ONLY row where the chain over-binds, and it is also the only row")
        print("  with a single bond. That coincidence is the content of this probe.")
    else:
        print("  The single-bond prediction holds, so a collective term that vanishes")
        print("  at one bond (a pure bond-bond interference) is consistent with the")
        print("  data. The cross-channel candidate class survives this screen.")

    # ---- the diagnostic value, and an explicit anti-numerology guard --------
    implied = B2 / alpha
    ratio = implied / Lpn
    print("\n## Diagnostic (NOT an anchor, NOT to be wired)\n")
    print(f"  L_pn implied by the deuteron = B(2H)/alpha = {implied:.9f}")
    print(f"  derived L_pn                              = {Lpn:.9f}")
    print(f"  implied / derived                         = {ratio:.9f}")
    print("\n  Re-fitting L_pn to this value would convert a prediction into a")
    print("  fourth anchor. Printed to size the disagreement only.")

    # The ratio sits very close to pi/4. Kill it here rather than let a later
    # session rediscover it and treat it as a lead.
    pi4 = math.pi / 4
    dev = abs(ratio - pi4) / pi4
    print(f"\n  COINCIDENCE CHECK — the ratio sits {dev*100:.4f} % from pi/4 = {pi4:.9f}.")
    print("  This is NOT evidence, and the reason is precision, not taste:")
    print(f"    B(2H) is measured to ~1e-7 relative; alpha and L_pn are derived to")
    print("    50 dps. So if the ratio WERE pi/4 exactly, it would agree to ~1e-7.")
    print(f"    It agrees to {dev:.1e} -- three to four orders of magnitude worse")
    print("    than the data permits for an identity.")
    print("  So pi/4 is excluded as an exact relation by the data quality itself.")
    print("  Recorded here so the near-miss is not rediscovered and chased later;")
    print("  no such relation is proposed, and nothing downstream uses it.")

    print("\n(no witness by design — one derived constant against one AME row.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
