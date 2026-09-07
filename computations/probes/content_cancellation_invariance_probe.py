#!/usr/bin/env python3
"""content_cancellation_invariance_probe.py — which ℏ_q coefficients survive the ruling, and why.

THE CRITERION. Owner ruling `qou-hu1f` (2026-09-05) reordered each nucleon's confinement core, and
the fallout has been case-by-case: `c₀` survived, `c₁` moved by up to `163×` (`qou-pdg9`), `c₂` moved
by `10×`–`217×` (`qou-qqm4`), the ⁴He first-order chain ratio `24/7` survived, the mirror difference
survived at first order and not at second. This probe gives the rule behind that list:

    A linear combination of same-A isotope coefficients whose NET NUCLEON CONTENT IS ZERO is
    invariant under any intra-nucleon reordering, at EVERY order.

**Why.** Such a combination cancels every per-nucleon contribution identically, so only *interface*
data survives it — and interfaces are single letters sitting **outside** the nucleon blocks, which no
reordering *within* a nucleon can reach. The reordering is therefore invisible to it, whatever order
of ℏ_q is being computed. Combinations that do not cancel nucleon content keep per-nucleon terms and
have no such protection.

MEASURED, exact rationals, both orderings (`c₂` from the exact ε-series; see
`c2_is_stale_on_the_reordered_atom_word_probe`):

    combination                       net nucleons   c₁ canon / grouped   c₂ canon / grouped
    X(pp) + X(nn) − 2X(pn)   [A=2]         0          0      / 0          −15/32 / −15/32  ✓
    X(3p) + X(3n) − X(T) − X(³He) [A=3]    0          0      / 0            9/64 /   9/64  ✓
    X(T) − X(³He)            [A=3]      −1p +1n      −7/64  / −7/64       −29/64 / −83/64  ✗

The third row is the control and it behaves as the criterion says it must: content does **not**
cancel, and `c₂` is **not** invariant.

THE SECOND ROW IS A HELD-OUT TEST. The criterion was stated from the `A = 2` row alone; the `A = 3`
combination was then chosen because `3p + 3n` and `T + ³He` carry the same content (`3p + 3n`), and
`c₂(3p)`, `c₂(3n)` were computed afterwards, for both orderings, purely to test it. It returns
`9/64` on both. Nothing was tuned — the combination has integer coefficients fixed by the content
bookkeeping, not by fitting.

WHAT IT EXPLAINS, and it is the whole earlier list:

- **`c₀` survives** — it is a pure cycle count, blind to letter order for a stronger reason still.
- **`c₁` and `c₂` individually move** — a single isotope has non-zero content.
- **The ⁴He first-order chain ratio `24/7` survives** — `pp + pn + nn` against `⁴He` is `2p+2n` on
  both sides, so the ratio's numerator and denominator carry equal content, and
  `PairwiseChainLeadingOrder.chain_over_atom_He4_of_letters` proves the invariance algebraically.
- **The `T` and `³He` chain ratios move** — those have `Z ≠ N` and no such balance.

🛑 AND IT SHARPENS A CAVEAT I FLAGGED EARLIER RATHER THAN REMOVING IT. `MirrorAsymmetrySign.lean`
survives the ruling, and its docstring says that is "measured on two words, not structural". The
third row confirms that reading: the mirror difference does **not** cancel content, so the criterion
gives it no protection, and its first-order invariance is exactly the coincidence that
`P − Q = (S_p − S_n)/2` happens to be `5` for both words. Its **second**-order invariance duly
fails. Do not promote that file's invariance to a structural one.

WHAT THIS IS NOT. Not a proof — a criterion stated from one case, tested on a second, with a control.
The mechanism (per-nucleon terms cancel; interfaces are outside the blocks) is an argument about
where the reordering can act, and it is verified at orders 0, 1 and 2 only. Nor does it give a closed
form for `c₂`: it constrains *combinations*, not individual values, and six exact points still do not
fix a form in `(Z, N)`.

SCOPE — (a) scope-limited. Exact `Fraction` arithmetic on values computed elsewhere; no `q` is
evaluated here, no float. No witness, nothing wired, no Lean.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F

# Exact c₁ — canonical from PR #6920's closed form, grouped from qou-pdg9. The four A=3 species
# were verified against the closed form as they were computed (19/64, 181/64, 19/8, −5/32).
C1 = {
    "borromean": {"pp": F(1, 8), "pn": F(1, 16), "nn": F(0), "T": F(1, 64),
                  "³He": F(1, 8), "3p": F(19, 64), "3n": F(-5, 32)},
    "grouped": {"pp": F(19, 8), "pn": F(37, 16), "nn": F(9, 4), "T": F(163, 64),
                "³He": F(85, 32), "3p": F(181, 64), "3n": F(19, 8)},
}
# Exact c₂ = [ε¹]+[ε²] of Δtr(1+ε), qou-qqm4's convention. Canonical values computed through the
# corpus's own validated ε-series (c1_leading_coefficient_derived_probe.tr_M_series); the grouped
# pp/pn/nn/T/³He are qou-qqm4's recorded values, reproduced by that same driver as a self-test.
C2 = {
    "borromean": {"pp": F(33, 32), "pn": F(25, 32), "nn": F(1, 16), "T": F(99, 128),
                  "³He": F(157, 128), "3p": F(117, 64), "3n": F(5, 16)},
    "grouped": {"pp": F(357, 32), "pn": F(403, 32), "nn": F(217, 16), "T": F(3285, 128),
                "³He": F(3451, 128), "3p": F(963, 32), "3n": F(1451, 64)},
}
# (protons, neutrons) per species, for the content bookkeeping the criterion is stated in.
CONTENT = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2), "T": (1, 2), "³He": (2, 1),
           "3p": (3, 0), "3n": (0, 3)}

# Each combination as {species: integer coefficient}. Coefficients are fixed by the content
# bookkeeping, never fitted.
COMBOS = (
    ("X(pp) + X(nn) − 2X(pn)", 2, {"pp": 1, "nn": 1, "pn": -2}, "stated the criterion"),
    ("X(3p) + X(3n) − X(T) − X(³He)", 3, {"3p": 1, "3n": 1, "T": -1, "³He": -1},
     "HELD OUT — chosen for its content, computed after"),
    ("X(T) − X(³He)", 3, {"T": 1, "³He": -1}, "CONTROL — content does not cancel"),
)


def content(combo):
    """Net (protons, neutrons) of a combination. Zero means every per-nucleon term cancels."""
    p = sum(k * CONTENT[s][0] for s, k in combo.items())
    n = sum(k * CONTENT[s][1] for s, k in combo.items())
    return p, n


def evaluate(table, combo):
    return sum(k * table[s] for s, k in combo.items())


def main():
    print("[content] A same-A combination with ZERO NET NUCLEON CONTENT is invariant under any")
    print("[content] intra-nucleon reordering, at every order: only interface data survives it,")
    print("[content] and interfaces sit outside the nucleon blocks. Exact Fractions throughout.\n")

    print(f"    {'combination':<32}{'A':>3}{'net (p,n)':>12}"
          f"{'c₁ canon':>12}{'c₁ grouped':>12}{'c₂ canon':>12}{'c₂ grouped':>12}  verdict")
    ok = True
    for label, A, combo, note in COMBOS:
        p, n = content(combo)
        zero = (p == 0 and n == 0)
        c1c, c1g = evaluate(C1["borromean"], combo), evaluate(C1["grouped"], combo)
        c2c, c2g = evaluate(C2["borromean"], combo), evaluate(C2["grouped"], combo)
        inv = (c1c == c1g) and (c2c == c2g)
        # The criterion predicts invariance exactly when content cancels. A row that cancels
        # content and is NOT invariant refutes it; a row that does not cancel and IS invariant at
        # BOTH orders would mean the criterion is not the operative mechanism.
        good = (zero == inv)
        ok = ok and good
        print(f"    {label:<32}{A:>3}{f'({p},{n})':>12}"
              f"{str(c1c):>12}{str(c1g):>12}{str(c2c):>12}{str(c2g):>12}"
              f"  {'as predicted' if good else 'REFUTES THE CRITERION'}")
        print(f"      {note}")
    print(f"\n  ⇒ {'3/3 as the criterion predicts.' if ok else 'THE CRITERION IS REFUTED — do not quote it.'}")

    print("\n  Note the first-order column: BOTH content-cancelling combinations are 0 at c₁, not")
    print("  merely equal. So at first order the surviving interface terms cancel too (the pp −4")
    print("  and nn +4 against the pn 0). At second order they do not — −15/32 and 9/64 — and that")
    print("  is the substance: interface-interface cross terms appear one order up.")
    print("\n  🛑 This SHARPENS the MirrorAsymmetrySign caveat rather than removing it. That file")
    print("  survives the ruling and its docstring calls the invariance 'measured on two words, not")
    print("  structural'. Row 3 confirms it: the mirror difference does not cancel content, so the")
    print("  criterion gives it no protection — its c₁ invariance is the coincidence that")
    print("  P − Q = (S_p − S_n)/2 is 5 for both words, and its c₂ invariance duly FAILS.")
    print("\n  NOT a proof: a criterion stated from one case, tested on a second, with a control,")
    print("  at orders 0, 1 and 2 only. It constrains COMBINATIONS, not individual values, so it")
    print("  gives no closed form for c₂.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
