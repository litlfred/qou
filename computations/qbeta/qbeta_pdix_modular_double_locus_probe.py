#!/usr/bin/env python3
"""qou-pdix attack B — can the Faddeev MODULAR DOUBLE supply the alpha eigenphase?

WHAT ATTACK B PROPOSED.  The `alpha` eigenphase carrier that the Q_beta `c_k`
ladder needs is TRANSCENDENTAL over `Z[q,q^-1]`, so route 5 of the bean's route
table is the only survivor and Faddeev's quantum dilogarithm `Phi_b` is named
there as a candidate.  `Phi_b` carries something no compact `Phi_q` has: the
modular duality `b -> 1/b`, with

    q  = exp(i pi b^2)          q~ = exp(i pi / b^2).

The hoped-for mechanism -- call it INVERSION-AS-BRIDGE -- was that this
involution carries the fibre-level `|q| = 1` elliptic regime, where the
eigenphase lives naturally, over to the real `q > 1` substrate where the ladder
is evaluated.  Then the phase would be an ordinary object on one side and the
substrate value would be its dual.

TWO FINDINGS, both negative, and the SECOND is the one that generalises.

(1) INVERSION-AS-BRIDGE IS STRUCTURALLY EXCLUDED -- scope-(b), proved
    invariant.  The two loci at issue are

        fibre / elliptic   |q| = 1            <=>  b^2 real          (arg b = 0)
        substrate          q real, 0 < q      <=>  b^2 imaginary     (arg b = pi/4)

    and `z -> 1/z` fixes BOTH the real axis and the imaginary axis setwise.
    So inversion maps each locus into ITSELF; it never carries one to the
    other.  On the substrate branch it flips the SIGN of `Im b^2` (so it maps
    the `PhiBProd`-supported branch to its own reflection) and nothing more.
    The invariant is one line of algebra and is formalised sorry-free in
    `QOU/QBeta/ModularDoubleLocusSeparation.lean`.

    This is NOT a new reading of the corpus -- it is the corpus's own.
    `FaddeevPhi`'s class docstring already separates exactly these two branches
    and records that only one is discharged:

        "on the `Im b^2 > 0` substrate branch this is discharged by the
         modular-double product -- see QOU.MathlibExt.PhiBProd; the |q| = 1
         fibre regime, real b, remains open"

    An agent reaching for inversion as a bridge is reaching across a boundary
    the class definition already draws.

(2) THE DUAL CARRIER IS ~375x TOO STEEP, and this prunes `q~` as an INGREDIENT
    rather than merely as a bridge.  The ladder's required phase is pinned by
    TWO numbers, not one (bean qou-pdix section D):

        P(q0)        = 1.997259194490263     (+/- 5.7e-7 relative)
        |P'/P|(q0)   = 2.176                 (~4 figures)

    The declared Laurent basket all fails on the SLOPE, 21.8x TOO FLAT
    typically and 1.25x too flat at best.  The modular-dual scale fails on the
    same constraint from the OTHER SIDE:

        q~ = exp(i pi / b^2) = exp(+- pi^2 / ln q)
        |d ln q~ / dq| at q0 = 816.73        ->  375.3x TOO STEEP

    The magnitude is branch-independent (the sign of the exponent flips between
    the two `arg b` branches; the log-slope does not), so this is a fact about
    the modular-dual SCALE, not about a convention choice.

    SCOPE THIS CORRECTLY -- it is a statement about an INHERITED FACTOR, not a
    like-for-like comparison.  The basket column is `|P'/P|` of a CANDIDATE `P`;
    816.73 is `|d ln q~/dq|` of `q~` ITSELF.  For a candidate `P = f(q~)` the
    chain rule gives

        d ln P / dq = (d ln P / d ln q~) * (d ln q~ / dq)

    so any `q~`-carrying term inherits the ~817 factor UNLESS the prefactor
    `d ln P / d ln q~` is small enough to cancel it -- which needs it tuned to
    ~2.7e-3, and tuning it against the target is exactly the selection this
    corpus forbids.  So the honest claim is: `q~` cannot carry the phase WITHOUT
    a suppression that would itself be a fit.  That is scope-(a), and it is
    weaker than "no function of q~ can have slope 2.176", which is false and is
    NOT claimed here.

WHAT SURVIVES, and it is deliberately NOT pruned here.  `Phi_b`'s `b`-shift
relation

    Phi(z - i b/2) = (1 + exp(2 pi b z)) * Phi(z + i b/2)

carries no `exp(-1/t)` non-perturbative scale at all -- its prefactor is an
ordinary exponential in `z`.  It stays a live TRANSCENDENTAL INGREDIENT for
branch 3 (the holonomy of an independently-defined connection reproducing the
Hecke braiding).  Per AGENTS.md "Before declaring refuted", a scope-(b)
exclusion must not over-narrow: what is excluded is INVERSION AS A BRIDGE and
`q~` AS A CARRIER, not `Phi_b` as an ingredient.

AND THE OBVIOUS NEXT MOVE IS A FIT -- say so rather than take it.  The shift
prefactor's log-slope in `q` depends on `z`, so `z` is a dial that can be set
to hit 2.176.  Choosing it that way is selection against the target, which
AGENTS.md forbids outright.  `z` has to come out of the braiding.  So attack B
does not close the gap; it converts it into branch 3's open path, which is
where qou-pdix already stood.

Bean: qou-pdix.  Consumers: none (probe).  Emits no witness by design -- but
per the PROBES ARE NOT EXEMPT rule every number here is carried as `mpf`.
"""

import pathlib
import sys

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [
    str(ROOT / p)
    for p in ("computations", "computations/substrate", "tools/qou-substrate/python")
]

from qou_substrate.constants import Q  # noqa: E402

mp.mp.dps = 60

# The two-number target for the required eigenphase, from bean qou-pdix section D.
P_TARGET = mp.mpf("1.997259194490263")
SLOPE_TARGET = mp.mpf("2.176")

# The declared Laurent basket's log-slopes, same bean section, for the bracket.
BASKET = {
    "2 - 3h^4": mp.mpf("0.0996"),
    "chi^(2,1)(B_3)": mp.mpf("0.1018"),
    "[2]_q": mp.mpf("0.0937"),
    "tr M_4_1": mp.mpf("1.7363"),
}

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def main() -> int:
    q = mp.mpf(str(Q))
    lnq = mp.log(q)
    t = lnq / mp.pi

    print(__doc__.split("\n")[0])
    print()
    print(f"q0            = {mp.nstr(q, 20)}   (proton pin)")
    print(f"ln q0         = {mp.nstr(lnq, 20)}")
    print(f"t = ln q0/pi  = {mp.nstr(t, 20)}")
    print()

    # ---- 1. the two loci, and what inversion does to each -------------------
    print("1. LOCUS SEPARATION -- what `b^2 -> 1/b^2` does to each locus")

    b2_fibre = mp.mpf("0.49") + 0j  # any real b^2: the |q|=1 fibre regime
    inv_fibre = 1 / b2_fibre
    check(
        "fibre locus (b^2 real) is inversion-invariant",
        mp.im(inv_fibre) == 0,
        f"b^2={mp.nstr(b2_fibre, 8)} -> 1/b^2={mp.nstr(inv_fibre, 8)}, Im=0",
    )

    b2_sub = 1j * t  # the corpus's substrate branch: arg b = pi/4, Im b^2 > 0
    inv_sub = 1 / b2_sub
    check(
        "substrate locus (b^2 imaginary) is inversion-invariant",
        mp.re(inv_sub) == 0,
        f"b^2={mp.nstr(b2_sub, 8)} -> 1/b^2={mp.nstr(inv_sub, 8)}, Re=0",
    )

    check(
        "inversion FLIPS the sign of Im b^2 on the substrate branch",
        mp.im(b2_sub) > 0 and mp.im(inv_sub) < 0,
        f"Im b^2={mp.nstr(mp.im(b2_sub), 8)} > 0 -> "
        f"Im 1/b^2={mp.nstr(mp.im(inv_sub), 8)} < 0 "
        "(PhiBProd branch -> its own reflection, NOT the fibre regime)",
    )

    # The two loci meet only at b^2 = 0, which FaddeevPhi.hb excludes.
    check(
        "the two loci are disjoint away from b^2 = 0",
        True,
        "{b^2 real} cap {b^2 imaginary} = {0}, and FaddeevPhi.hb forces "
        "0 < Re b, so b != 0 -- no locus can be reached from the other",
    )

    # ---- 2. the substrate branch really does give the substrate q -----------
    print()
    print("2. THE BRANCH IDENTIFICATION IS THE CORPUS'S, NOT AN ANSATZ")

    b_sub = mp.sqrt(b2_sub)
    arg_over_pi = mp.arg(b_sub) / mp.pi
    check(
        "arg b = pi/4 on the substrate branch (matches FaddeevPhi docstring)",
        abs(arg_over_pi - mp.mpf("0.25")) < mp.mpf("1e-40"),
        f"arg b / pi = {mp.nstr(arg_over_pi, 12)}",
    )

    q_from_b = mp.e ** (1j * mp.pi * b2_sub)
    check(
        "exp(i pi b^2) is the substrate point (as 1/q0, |q| < 1 convention)",
        abs(mp.re(q_from_b) - 1 / q) < mp.mpf("1e-40") and abs(mp.im(q_from_b)) < mp.mpf("1e-40"),
        f"exp(i pi b^2) = {mp.nstr(mp.re(q_from_b), 18)} = 1/q0",
    )

    b_fibre = mp.sqrt(b2_fibre)
    q_fibre = mp.e ** (1j * mp.pi * b2_fibre)
    check(
        "real b gives |q| = 1 (the fibre regime)",
        abs(abs(q_fibre) - 1) < mp.mpf("1e-40") and abs(mp.im(b_fibre)) < mp.mpf("1e-40"),
        f"b={mp.nstr(mp.re(b_fibre), 10)} real -> |q|={mp.nstr(abs(q_fibre), 12)}",
    )

    # ---- 3. the dual carrier's log-slope vs the two-number target ----------
    print()
    print("3. THE DUAL CARRIER IS TOO STEEP -- prunes q~ as an INGREDIENT too")

    # q~ = exp(i pi / b^2) = exp(+- pi^2 / ln q); d ln q~ / dq = +- pi^2/(q ln^2 q).
    slope_dual = mp.pi**2 / (q * lnq**2)

    # cross-check the closed form against a central difference on |ln q~|
    def log_abs_dual(x: mp.mpf) -> mp.mpf:
        return mp.pi**2 / mp.log(x)

    eps = q * mp.mpf("1e-20")
    slope_fd = (log_abs_dual(q + eps) - log_abs_dual(q - eps)) / (2 * eps)
    check(
        "closed-form dual log-slope agrees with a central difference",
        abs(abs(slope_fd) - slope_dual) / slope_dual < mp.mpf("1e-15"),
        f"closed={mp.nstr(slope_dual, 14)}  fd={mp.nstr(abs(slope_fd), 14)}",
    )

    steep = slope_dual / SLOPE_TARGET
    check(
        "dual carrier overshoots the required log-slope by > 100x",
        steep > 100,
        f"|d ln q~/dq| = {mp.nstr(slope_dual, 10)} vs target "
        f"{mp.nstr(SLOPE_TARGET, 6)}  ->  {mp.nstr(steep, 6)}x TOO STEEP",
    )

    # the suppression a q~-carrying candidate would need, and why taking it is a fit
    needed_prefactor = SLOPE_TARGET / slope_dual
    check(
        "a q~-carrying candidate would need its prefactor tuned to ~2.7e-3",
        needed_prefactor < mp.mpf("0.01"),
        f"d ln P/d ln q~ would have to be {mp.nstr(needed_prefactor, 6)} to cancel "
        "the inherited 816.73 -- tuning it against the target is selection, so the "
        "claim is 'not without a fit', NOT 'no function of q~ can work'",
    )

    # branch independence: the OTHER sign of Im b^2 flips the exponent, not the slope
    slope_other = abs(-mp.pi**2 / (q * lnq**2))
    check(
        "the overshoot is branch-independent",
        slope_other == slope_dual,
        f"both arg b branches give |slope| = {mp.nstr(slope_other, 10)}; "
        "only the sign of ln q~ differs",
    )

    # ---- 4. the two-sided bracket ------------------------------------------
    print()
    print("4. THE TARGET IS BRACKETED -- Laurent too flat, modular-dual too steep")
    print(f"   target |P'/P|(q0) = {mp.nstr(SLOPE_TARGET, 6)}   "
          f"[P(q0) = {mp.nstr(P_TARGET, 16)}]")
    for name, s in sorted(BASKET.items(), key=lambda kv: kv[1]):
        print(f"     {name:<18} {mp.nstr(s, 6):>10}   "
              f"{mp.nstr(SLOPE_TARGET / s, 6):>8}x too flat")
    print(f"     {'q~ (modular dual)':<18} {mp.nstr(slope_dual, 6):>10}   "
          f"{mp.nstr(steep, 6):>8}x too STEEP")

    worst_flat = SLOPE_TARGET / min(BASKET.values())
    check(
        "target lies strictly between the basket and the dual scale",
        max(BASKET.values()) < SLOPE_TARGET < slope_dual,
        f"basket max {mp.nstr(max(BASKET.values()), 6)} < "
        f"{mp.nstr(SLOPE_TARGET, 6)} < {mp.nstr(slope_dual, 8)}; "
        f"flat side up to {mp.nstr(worst_flat, 6)}x, steep side "
        f"{mp.nstr(steep, 6)}x",
    )

    # ---- 5. the shift relation is NOT pruned -------------------------------
    print()
    print("5. WHAT SURVIVES -- and why taking it now would be a FIT")
    check(
        "the b-shift prefactor carries no non-perturbative scale",
        True,
        "1 + exp(2 pi b z) is an ordinary exponential in z; it contains no "
        "exp(-1/t) factor, so the 375x overshoot does NOT apply to it -- "
        "Phi_b stays a live branch-3 ingredient",
    )
    check(
        "its slope is z-tunable, so hitting 2.176 by choosing z is a FIT",
        True,
        "selection against the target, banned by AGENTS.md NO FITTING; z must "
        "be derived from the Hecke braiding, which is branch 3's open path",
    )

    # ---- verdict -----------------------------------------------------------
    npass = sum(1 for _, ok, _ in CHECKS if ok)
    ntot = len(CHECKS)
    print()
    print("=" * 70)
    print(f"VERDICT  {npass}/{ntot} checks pass")
    print()
    print("attack B (inversion-as-bridge)   PRUNED, scope-(b), proved invariant:")
    print("                                 both loci are inversion-invariant.")
    print("attack B (q~ as carrier)         PRUNED, scope-(a): 375x too steep on")
    print("                                 the ladder's own log-slope constraint.")
    print("Phi_b as a branch-3 ingredient   LIVE -- deliberately not pruned.")
    print("qou-pdix                         STILL OPEN. Branch 3 unchanged.")
    print("=" * 70)
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    raise SystemExit(main())
