#!/usr/bin/env python3
"""`sigma^k - sigma^-k` is a scalar only at ODD k -- and delta's numerator is k = 2.

WHAT THIS ESTABLISHES
---------------------
`QOU.FlavorSplit.topological_flavor_split_of_central` proves the proton/neutron
crossing reversal `sigma^3 - sigma^-3` is the central scalar `h(h^2+3) = q^3 -
q^-3`, and `conj:flavor-split-habiro-derivation` builds on it.  (Corrected
2026-09-13: this line read "builds an H_4 alternating-channel route to the
substrate flavour split on it".  The block's alternating channel is its choice for
the RESIDUAL -- the 0.128 % refinement -- not for the split; see section 7 and
`flavour_split_baseline_is_augmentation_trace_probe.py`.)  Its baseline is

    delta = (q-1)^2 (1 - q^-4)/3 = hbar_q^2 * h * [2]_q / 3 ,   [2]_q = q + 1/q.

This probe measures the parity that result is an instance of, and shows the route
is blocked at exactly the exponent delta needs.

    sigma^k - sigma^-k   is CENTRAL  <=>  k is ODD,  and then equals  q^k - q^-k .

At even k it is `A_k * (sigma + sigma^-1)`, a central multiple of the resolvent
`u = sigma + sigma^-1 = 2 sigma - h`, which is not central.  The invariant behind
it is `u^2 = h^2 + 4` (central), so even powers of u are central and odd ones are
not; equivalently the odd subsequence closes on itself with a central coefficient,
`D_{k+4} = (h^2+2) D_{k+2} - D_k`.

Formalised (sorry-free, generic `Ring R` with `h` central, left inverse only) as
`QOU.Hecke.CrossingReversalParity`: `resolvent_sq`, `reversal_two`,
`reversal_four`, `reversal_five`, `reversal_rec`,
`reversal_two_forces_resolvent_central`.  **Only those INSTANCES are proved; the
general-k statement is what this probe measures, to k = 11.**

THE PRUNE
---------
delta's numerator is `h * [2]_q = q^2 - q^-2`, i.e. the k = 2 member of the family
`q^k - q^-k = h*[k]_q` that the odd reversals realise as scalars.  k = 2 is exactly
where the parity fails:

    sigma^2 - sigma^-2 = h * (sigma + sigma^-1)   -- NOT a scalar

Its two values on the Hecke spectrum `{q, -1/q}` are `+(q^2 - q^-2)` and
`-(q^2 - q^-2)`: the right magnitude with an undetermined sign.  So reaching
delta's numerator through a crossing reversal requires CHOOSING the symmetric
channel, and the algebra does not supply that choice.

**SUPERSEDED IN PART, 2026-09-13 -- the algebra DOES supply it, through the trace
rather than through a channel.**  Because the element is `2 h sigma - h^2`, the
Markov trace is fixed on it by `tr(1) = 1` and `tr(sigma) = z` alone:
`tr_z(sigma^2 - sigma^-2) = 2hz - h^2`.  That reproduces `q^2 - q^-2` EXACTLY at
the augmentation `z = q`, and `alpha = (q^4+1)/(q^2+1)^2` times it at convention D
`z_D = q^3/(q^2+1)`.  So the open step is not "choose a channel" but "choose a
Markov parameter", which is the same fork as Q_beta (bean qou-99qc) with the same
alpha.  See `flavour_split_baseline_is_augmentation_trace_probe.py` and
`QOU/Hecke/MarkovCrossingReversal.lean`.  The parity measurement below is
unaffected.

Scope (b) within the single-generator family `sigma^k - sigma^-k`, invariant named
(the parity).  Nothing here excludes `h*[2]_q` arising from some other Hecke
element -- it says the one exact result the conjecture rests on does not reach it,
and names the step a repair must supply.

Run: python3 computations/qbeta/crossing_reversal_parity_probe.py
"""

from __future__ import annotations

import sympy as sp
from mpmath import mp, mpf

mp.dps = 60

KMAX = 11

_q = sp.symbols("q", positive=True)
_s = sp.symbols("sigma")                  # the Hecke generator, kept formal
H = _q - 1 / _q


def sigma_pow(k: int):
    """`sigma^k = A_k*sigma + B_k`, reduced by the quadratic `sigma^2 = h*sigma+1`.

    Solved from the two eigenvalues `q` and `-1/q` rather than by unfolding the
    recursion, so the reduction is not assumed.
    """
    A, B = sp.symbols("A B")
    sol = sp.solve([A * _q + B - _q**k, -A / _q + B - (-1 / _q) ** k], [A, B], dict=True)[0]
    return sp.simplify(sol[A]), sp.simplify(sol[B])


def main() -> int:
    ok = True

    print(f"1. PARITY OF THE CROSSING REVERSAL  (symbolic over q, k = 1..{KMAX})")
    print("   k   central?   sigma-coefficient        value if central")
    for k in range(1, KMAX + 1):
        Ap, Bp = sigma_pow(k)
        Am, Bm = sigma_pow(-k)
        coeff = sp.simplify(Ap - Am)
        const = sp.simplify(Bp - Bm)
        central = coeff == 0
        expected_central = (k % 2 == 1)
        good = central == expected_central
        if central:
            good &= sp.simplify(const - (_q**k - _q**-k)) == 0
        ok &= good
        tag = "CENTRAL " if central else "not     "
        val = f"q^{k} - q^-{k}" if central else "-"
        print(f"  {k:>2}   {tag}   {str(coeff)[:24]:<24} {val:<14}"
              f" {'OK' if good else 'MISMATCH'}")
    print("   -> central exactly at ODD k, with value q^k - q^-k:",
          "CONFIRMED" if ok else "NOT CONFIRMED")

    print()
    print("2. THE INVARIANT  u^2 = h^2 + 4,  u = sigma + sigma^-1 = 2*sigma - h")
    # sigma^2 = h*sigma + 1 reduces u^2 with no eigenvalue input
    u = 2 * _s - H
    u2 = sp.expand(u**2)
    u2_red = sp.expand(u2.subs(_s**2, H * _s + 1))
    d = sp.simplify(u2_red - (H**2 + 4))
    ok &= d == 0
    print(f"   (2*sigma - h)^2 reduced by sigma^2 = h*sigma + 1 : {sp.simplify(u2_red)}")
    print(f"   minus (h^2 + 4) = {d}   {'OK' if d == 0 else 'MISMATCH'}")
    print("   -> u^2 is CENTRAL, so even powers of u are and odd ones are not.")

    print()
    print("3. THE ODD SUBSEQUENCE CLOSES WITH A CENTRAL COEFFICIENT")
    print("   D_{k+4} = (h^2+2)*D_{k+2} - D_k   (h^2+2 = u^2 - 2)")
    for k in (1, 3, 5, 7):
        Dk = _q**k - _q**-k
        Dk2 = _q ** (k + 2) - _q ** (-(k + 2))
        Dk4 = _q ** (k + 4) - _q ** (-(k + 4))
        r = sp.simplify(Dk4 - ((H**2 + 2) * Dk2 - Dk))
        ok &= r == 0
        print(f"   k = {k}: residual {r}   {'OK' if r == 0 else 'MISMATCH'}")

    print()
    print("4. DELTA'S NUMERATOR IS THE k = 2 MEMBER  (symbolic over q)")
    delta = (_q - 1) ** 2 * (1 - _q**-4) / 3
    hbar = 1 - 1 / _q
    two_q = _q + 1 / _q
    e1 = sp.simplify(delta - hbar**2 * H * two_q / 3)
    e2 = sp.simplify(H * two_q - (_q**2 - _q**-2))
    ok &= (e1 == 0) and (e2 == 0)
    print(f"   delta - hbar_q^2 * h * [2]_q / 3 = {e1}   {'OK' if e1 == 0 else 'MISMATCH'}")
    print(f"   h * [2]_q - (q^2 - q^-2)         = {e2}   {'OK' if e2 == 0 else 'MISMATCH'}")
    print("   -> delta = hbar_q^2 * (q^2 - q^-2) / 3, and q^2 - q^-2 is the k = 2")
    print("      member of the family q^k - q^-k the ODD reversals realise.")

    print()
    print("5. THE k = 2 REVERSAL AND ITS TWO CHANNEL VALUES")
    A2p, B2p = sigma_pow(2)
    A2m, B2m = sigma_pow(-2)
    coeff2 = sp.simplify(A2p - A2m)
    const2 = sp.simplify(B2p - B2m)
    # h*(sigma + sigma^-1) = h*(2 sigma - h)
    shape = sp.simplify(coeff2 * _s + const2 - H * (2 * _s - H))
    ok &= shape == 0
    print(f"   sigma^2 - sigma^-2 = ({sp.factor(coeff2)})*sigma + ({sp.simplify(const2)})")
    print(f"   minus h*(2*sigma - h) = {shape}   {'OK' if shape == 0 else 'MISMATCH'}")
    sym = sp.simplify((coeff2 * _s + const2).subs(_s, _q))            # symmetric channel
    anti = sp.simplify((coeff2 * _s + const2).subs(_s, -1 / _q))      # antisymmetric
    target = sp.simplify(_q**2 - _q**-2)
    gs = sp.simplify(sym - target)
    ga = sp.simplify(anti + target)
    ok &= (gs == 0) and (ga == 0)
    print(f"   value at sigma =  q     (symmetric)     : {sp.factor(sym)}"
          f"   == +(q^2-q^-2)? {gs == 0}")
    print(f"   value at sigma = -1/q   (antisymmetric) : {sp.factor(anti)}"
          f"   == -(q^2-q^-2)? {ga == 0}")
    print("   -> the magnitude is right in BOTH channels and the SIGN is not fixed")
    print("      by the algebra. Selecting the symmetric channel is the unproved step.")

    print()
    print("6. NUMERICAL, AT THE PROTON-PINNED q0  (mpmath, dps=60)")
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP          # noqa: PLC0415
    q0 = Q_MP
    sub = {_q: sp.Float(str(q0), 50)}
    for lbl, expr in (
        ("h = q - 1/q", H),
        ("u^2 = h^2 + 4", H**2 + 4),
        ("D_3 = h(h^2+3)   [central, corpus k=3]", H * (H**2 + 3)),
        ("D_5 = h(h^4+5h^2+5) [central, new k=5]", H * (H**4 + 5 * H**2 + 5)),
        ("q^2 - q^-2       [delta's numerator]", _q**2 - _q**-2),
        ("delta", delta),
    ):
        v = mpf(str(sp.N(expr.subs(sub), 45)))
        print(f"   {lbl:<42} = {mp.nstr(v, 20)}")
    d3 = mpf(str(sp.N((H * (H**2 + 3)).subs(sub), 45)))
    q3 = mpf(str(sp.N((_q**3 - _q**-3).subs(sub), 45)))
    rel = abs(d3 - q3) / abs(q3)
    good = rel < mpf("1e-40")
    ok &= good
    print(f"   D_3 vs q^3 - q^-3: rel {mp.nstr(rel, 3)}   {'OK' if good else 'MISMATCH'}")

    print()
    print("7. THE TWO ONE-DIMENSIONAL CHANNELS ARE EXACT NEGATIVES")
    print("   [RETRACTED HEADING -- this section read 'the conjecture's own channel")
    print("    gives the wrong sign', quoting the block's 'strictly left-handed ...")
    print("    fully alternating channel of H_4'.  That conflated the block's two")
    print("    LEVELS: the alternating channel is its choice for the RESIDUAL (the")
    print("    0.128 % Schwinger-analogue refinement), not for the baseline.  See")
    print("    flavour_split_baseline_is_augmentation_trace_probe.py.  The algebra")
    print("    below is correct and unchanged; only the reading was wrong.]")
    print("   Evaluate the k = 2 reversal on sigma -> q and sigma -> -q^-1:")
    hbar2 = (1 - 1 / _q) ** 2
    sym_split = sp.simplify(hbar2 * sym / 3)
    alt_split = sp.simplify(hbar2 * anti / 3)
    e_sym = sp.simplify(sym_split - delta)
    e_alt = sp.simplify(alt_split + delta)
    ok &= (e_sym == 0) and (e_alt == 0)
    print(f"   hbar_q^2 * (symmetric)   / 3 - delta = {e_sym}"
          f"   {'OK' if e_sym == 0 else 'MISMATCH'}")
    print(f"   hbar_q^2 * (alternating) / 3 + delta = {e_alt}"
          f"   {'OK' if e_alt == 0 else 'MISMATCH'}")
    v_alt = mpf(str(sp.N(alt_split.subs(sub), 45)))
    v_sym = mpf(str(sp.N(sym_split.subs(sub), 45)))
    neg = v_alt < 0
    ok &= neg and (v_sym > 0)
    print(f"   at the proton q0:  symmetric = {mp.nstr(v_sym, 14)}   "
          f"alternating = {mp.nstr(v_alt, 14)}")
    print(f"   -> alternating < 0 (m_n < m_p), symmetric > 0: "
          f"{'CONFIRMED' if neg else 'NOT CONFIRMED'}")
    print("   WHERE THIS IS USED: the two are exact negatives, and the corpus's own")
    print("   three-channel weights are EQUAL on them, w_sym = w_alt = q^2/(q^4+4q^2+1)")
    print("   (docs/audits/2026-06-17-hecke-channel-chirality-binding.md), so the")
    print("   equal-weight average of the reversal VANISHES identically.  That is a")
    print("   scope-(b) exclusion of the averaged reading -- invariant = the weight")
    print("   equality plus the exact negation -- and says nothing about the standard")
    print("   channel or about unequal weights.")
    print("   CONDITIONAL on the identification 'delta's numerator IS the k = 2")
    print("   reversal', which is THIS PROBE's reading and not the block's -- the")
    print("   block calls (q-1)^2(1-q^-4)/3 'a structured near-match, not a derived")
    print("   closed form'.  That reading now has a TRACE behind it rather than a")
    print("   channel: tr_z(sigma^2-sigma^-2) = 2hz - h^2 reproduces the block's")
    print("   expression exactly at the augmentation z = q.")

    print()
    print("VERDICT:", "PASS — the reversal is central only at odd k, and delta's "
          "numerator sits at k = 2, where it is not" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
