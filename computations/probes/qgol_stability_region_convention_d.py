"""q-GoL stability region under convention D — the substrate is OUTSIDE it.

`prop:q-game-of-life` states the stability condition as *"the Toffoli diagonal
P_77(q) and the q-AND amplitude Phi(q) are strictly positive ... this requires
the physical regime q > 1 ... q_0 lies safely inside the stable regime"*, and
`prop:q-game-of-life-proof` derives that region from three operator zeros:
q_star = 1/phi^2 ~ 0.3820, q_Phi ~ 0.4656, and q = 1.

All three of those inputs are convention-C.  Under the canonical
z_D = q^3/(q^2+1) the corpus now carries D-frame closed forms for both
amplitudes (`toffoli-lp-stability.md`, `toffoli-q-and.md`, derived on main
under bean qou-3j5m):

    P_77^D(q) = q^3 (q^4 + 1) / (q^2 + 1)^2
    Phi^D(q)  = -(q-1)(q+1)(q^6 + q^4 + 2q^2 + 1) / (2 q (q^2+1)^2)

This probe checks what those two forms imply for the stability REGION, which
is the part the q-GoL blocks assert and which no committed probe covers.  It
re-derives nothing: the closed forms are taken from the corpus and only their
signs are measured.

Result (see the assertions): P_77^D has no positive root at all, so the
golden-ratio threshold does not survive the convention change; and Phi^D is
positive exactly on 0 < q < 1, so the region where BOTH are strictly positive
is 0 < q < 1 — not q > 1.  The substrate q_0 ~ 1.11 sits where Phi^D < 0.

SETTLED 2026-08-30 (owner ruling, bean qou-nmqd): the criterion is
NON-VANISHING, `Phi != 0`, not strict positivity.  The blocks now state the
well-definedness region as `q != 1`, which contains the substrate.

That does not make this probe obsolete -- it makes it the record of why.  The
signs below are what forced the question: under D, strict positivity would put
the region at 0 < q < 1 and exclude the substrate, while non-vanishing -- the
condition `toffoli-q-and.md`'s universality argument already used, and the one
invertibility of the tick requires -- holds for every q != 1.  The two give
opposite verdicts at q_0 and could not both be the criterion.

Read the table below as two facts that stand whichever criterion is adopted:
the golden-ratio threshold does not survive the convention change (P_77^D has
no positive root at all), and Phi^D's single zero on q > 0 sits at q = 1, the
classical limit, where the q-deformation contributes nothing.
"""

# Bootstrap sys.path BEFORE importing _path_bridge: the bridge lives in
# computations/, and a script in a cluster subdir has sys.path[0] set to its
# own directory, so the import fails without this (AGENTS.md, bean qou-0e1t).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60


def p77_D(q):
    """Toffoli diagonal, convention D. Closed form from toffoli-lp-stability.md."""
    return q**3 * (q**4 + 1) / (q**2 + 1) ** 2


def phi_D(q):
    """q-AND amplitude P_{7,6}, convention D. Closed form from toffoli-q-and.md."""
    return -((q - 1) * (q + 1) * (q**6 + q**4 + 2 * q**2 + 1)) / (
        2 * q * (q**2 + 1) ** 2
    )


def main() -> int:
    q0 = Q_MP

    # The three convention-C thresholds the q-GoL proof cites, plus q_0 and a
    # spread of sample points either side of q = 1.
    q_star = (3 - mp.sqrt(5)) / 2          # 1/phi^2, the golden-ratio zero
    q_phi = mp.mpf("0.4656")               # the published phase-reversal point
    samples = [
        ("0.1", mp.mpf("0.1")),
        ("q_star = 1/phi^2", q_star),
        ("q_Phi ~ 0.4656", q_phi),
        ("0.9", mp.mpf("0.9")),
        ("0.999", mp.mpf("0.999")),
        ("1", mp.mpf(1)),
        ("1.001", mp.mpf("1.001")),
        ("q_0 (proton pin)", q0),
        ("5", mp.mpf(5)),
    ]

    print("=" * 74)
    print("q-GoL stability region under convention D")
    print("=" * 74)
    print(f"  q_0 = {mp.nstr(q0, 30)}")
    print()
    print(f"  {'q':<20} {'P_77^D':>18} {'Phi^D':>18}   both > 0")
    for label, q in samples:
        a, b = p77_D(q), phi_D(q)
        print(
            f"  {label:<20} {mp.nstr(a, 12):>18} {mp.nstr(b, 12):>18}"
            f"   {'yes' if (a > 0 and b > 0) else 'NO'}"
        )
    print()

    # P_77^D positivity. The numerator q^3(q^4+1) and denominator (q^2+1)^2 are
    # both strictly positive for q > 0, so there is no root to find; check it
    # on a dense sweep rather than asserting the algebra.
    p77_min = min(p77_D(mp.mpf(k) / 200) for k in range(1, 2001))
    print(f"  min P_77^D over q in (0.005, 10], 2000 pts = {mp.nstr(p77_min, 12)}")
    print(f"  P_77^D at the golden threshold              = {mp.nstr(p77_D(q_star), 12)}")
    print("    -> the golden-ratio zero does NOT survive the convention change")
    print()

    # Phi^D sign: carried entirely by (q-1); the sextic has no positive real root.
    sextic_roots = mp.polyroots([1, 0, 1, 0, 2, 0, 1], maxsteps=200, extraprec=200)
    n_pos_real = sum(
        1 for r in sextic_roots if abs(mp.im(r)) < mp.mpf("1e-40") and mp.re(r) > 0
    )
    print(f"  positive real roots of q^6+q^4+2q^2+1       = {n_pos_real}")
    print(f"  Phi^D(q_0)                                  = {mp.nstr(phi_D(q0), 12)}")
    print("    -> Phi^D > 0 exactly on 0 < q < 1; the substrate is where it is NEGATIVE")
    print()
    print("  Strict positivity would give the region 0 < q < 1, excluding q_0.")
    print("  NON-VANISHING (Phi != 0) is the criterion -- owner ruling 2026-08-30,")
    print("  bean qou-nmqd -- so the region is q != 1 and DOES contain q_0. The")
    print("  two facts above hold either way: no golden threshold under D, and")
    print("  Phi^D's only zero on q > 0 is the classical limit q = 1.")

    w = WitnessBuilder("qgol-stability-region-convention-d", engine="mpmath")
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("P_77_D", "q^3 (q^4+1) / (q^2+1)^2  [toffoli-lp-stability.md]")
    w.add_parameter(
        "Phi_D", "-(q-1)(q+1)(q^6+q^4+2q^2+1) / (2q(q^2+1)^2)  [toffoli-q-and.md]"
    )
    w.add_assertion("P77_D_positive_at_golden_threshold", 1 if p77_D(q_star) > 0 else 0, 1)
    w.add_assertion("P77_D_has_no_positive_root", 1 if p77_min > 0 else 0, 1)
    w.add_assertion("sextic_has_no_positive_real_root", n_pos_real, 0)
    w.add_assertion("Phi_D_negative_at_q0", 1 if phi_D(q0) < 0 else 0, 1)
    w.add_assertion("Phi_D_positive_below_one", 1 if phi_D(mp.mpf("0.999")) > 0 else 0, 1)
    w.add_data("P77_D_at_q0", mp.nstr(p77_D(q0), 30))
    w.add_data("Phi_D_at_q0", mp.nstr(phi_D(q0), 30))
    w.add_data("P77_D_at_golden_threshold", mp.nstr(p77_D(q_star), 30))
    w.add_data("stability_region_both_strictly_positive", "0 < q < 1")
    w.add_data("region_asserted_by_proposition", "q > 1")
    w.set_description(
        "Measures the sign of the two convention-D Toffoli amplitudes across the "
        "region prop:q-game-of-life asserts. P_77^D has no positive root, so the "
        "golden-ratio threshold the q-GoL proof once cited is a convention-C "
        "artifact; Phi^D has a single zero on q > 0, at q = 1. SETTLED "
        "2026-08-30 (owner ruling, bean qou-nmqd): the criterion is NON-VANISHING "
        "(Phi != 0), not strict positivity, so the well-definedness region is "
        "q != 1 and contains the substrate. Strict positivity would have given "
        "0 < q < 1 and excluded it; these signs are the record of why the "
        "question had to be asked."
    )
    w.save({"q0Anchor": "proton", "q0Value": str(Q_50_DIGIT_STR)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
