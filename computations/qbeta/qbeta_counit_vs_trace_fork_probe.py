#!/usr/bin/env python3
"""Is Q_A the object Im(frak V)? NO -- Q_A is the COUNIT, frak V is the TRACE.

BEAN `qou-cds1`. Resolves the fork left by
`qbeta_sinh_partner_object_identification_probe.py`, which found that the
"bar-odd sinh partner" is Im(frak V) -- the Chern-Simons-analogue part of the
complex volume -- and then measured the computed chain's bar-ratio at +1.687
where bar-oddness needs -1. That left two possibilities the corpus did not
distinguish:

  (i)  Q_A is NOT Im(frak V) -- different objects, no contradiction; or
  (ii) the conjecture's parity claim fails for the computed object.

IT IS (i), and the corpus says so explicitly once you find the derivation.

`nuclear-interactions/qbeta-counit-closed-form.md` derives the closed form as a
FROBENIUS COUNIT evaluation:

    eps(Delta) * E_0 = m_e (q+1)(q^2 - 2q - 1) / (2 q^3),
    E_0 = m_e / (q(q-1)),   Delta = NF(n) - NF(p) in H_3(q),

and states the distinction outright:

    eps(Delta) = h^2/2 - h,        tr_M(Delta) = h^2/2 - h z
    "The counit is the Markov trace evaluated at the trivial loop value. The two
     agree precisely when z = 1. The trivial-loop value is never attained on the
     substrate. THE COUNIT AND THE MARKOV TRACE ARE GENUINELY DISTINCT
     FUNCTIONALS ON THE SUBSTRATE."

whereas conj:binding-qbeta-complex-volume defines
    frak-V(K) = E_0 * tr_M((Pi_free - 1) . M),   Q_beta = Im frak-V,
a MARKOV TRACE object. So Q_A (counit) and Im frak-V (trace) are different
functionals by construction, and the +1.687-vs--1 bar-ratio is NOT a corpus
contradiction: Q_A was never the object the parity claim is about.

VERIFIED HERE: eps(Delta)*E_0 reproduces the committed closed form exactly
(-0.783645827375 vs +0.783645827375; the closed form's |q^2-2q-1| discards the
sign, which is itself worth noting since a bar-odd object is signed).

THE STRUCTURAL IDENTITY THIS EXPOSES. Subtracting the two functionals:

    eps(Delta) - tr_M(Delta) = h(z - 1) = 2 * alpha,     alpha = (z-1)h/2

verified symbolically (difference simplifies to 0). So

    *** the ladder's phase alpha is EXACTLY half the counit-minus-trace gap ***

alpha is therefore not an arbitrary parameterisation: the precision ladder is
implicitly TRANSPORTING the evaluation from the counit to the trace, and alpha
measures precisely that gap. This also locates the unjustified step -- it is the
COSINE, i.e. exponentiating a difference into cos(alpha - u/2), and that is
exactly the piece which is axiomatised (QOU.Interactions.QBetaCosResummation).

MEASURED ONCE, AND NOT PURSUED. If the transport were a bare ratio of these
functionals on Delta, F would be one of:

    convention C:  trM/eps = 0.44087    odd(trM)/eps = 0.55761
    convention D:  trM/eps = 0.56748    odd(trM)/eps = 0.68421

against F_required = 0.998325. None is close, so the transport is not a bare
ratio of eps and tr_M on Delta. Recorded and deliberately NOT explored further:
hunting combinations that land near 0.998 is the fit this bean forbids.

Scope-(a): identification plus measurement. Nothing derived, nothing wired.
"""
from __future__ import annotations

import sys

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

ANCHORS = {
    "proton": mp.mpf("1.10997858275138080759166909561076887987449912187357873607281"),
    "muon": mp.mpf("1.10997859555418057528159407960950937799328227995868622546675"),
}
M_E = mp.mpf("0.51099895069")
Q_CODATA = mp.mpf("0.78233341")


def main() -> int:
    ok = True
    for name, q in ANCHORS.items():
        h = q - 1 / q
        E0 = M_E / (q * (q - 1))
        eps = h**2 / 2 - h                      # Frobenius counit on Delta
        qa_counit = eps * E0
        qa_closed = M_E * abs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)

        print(f"=== anchor {name}")
        print(f"  eps(Delta)*E_0        = {mp.nstr(qa_counit, 12)} MeV")
        print(f"  committed closed form = {mp.nstr(qa_closed, 12)} MeV")
        print(f"  |difference|          = {mp.nstr(abs(abs(qa_counit) - qa_closed), 6)}"
              f"   <- same object; closed form's |.| drops the sign")

        # The counit reproduces the closed form (up to the discarded sign).
        ok &= abs(abs(qa_counit) - qa_closed) < mp.mpf("1e-30")

        # alpha is exactly half the counit-minus-trace gap, for ANY z.
        for zname, z in (("C", mp.sqrt(q) / (q + 1)), ("D", q**3 / (q**2 + 1))):
            trM = h**2 / 2 - h * z
            alpha = (z - 1) * h / 2
            ok &= abs((eps - trM) - 2 * alpha) < mp.mpf("1e-30")
            print(f"  [{zname}] eps-trM = {mp.nstr(eps-trM, 10)}   "
                  f"2*alpha = {mp.nstr(2*alpha, 10)}   "
                  f"trM/eps = {mp.nstr(trM/eps, 8)}")

        Freq = Q_CODATA / abs(qa_counit)
        print(f"  F_required = {mp.nstr(Freq, 12)}   "
              f"(no bare ratio above is close to it)")
        print()

    print("FORK RESOLVED: Q_A is the COUNIT evaluation; Im(frak V) is a TRACE")
    print("  evaluation. qbeta-counit-closed-form.md states they are 'genuinely")
    print("  distinct functionals on the substrate', agreeing only at z=1 which")
    print("  is never attained. So the +1.687-vs--1 bar-ratio is NOT a corpus")
    print("  contradiction -- Q_A was never the object the parity claim concerns.")
    print()
    print("IDENTITY: alpha = (eps(Delta) - tr_M(Delta)) / 2, exactly.")
    print("  The ladder's phase IS the counit-minus-trace gap, so the ladder is")
    print("  implicitly transporting counit -> trace. The unjustified step is the")
    print("  COSINE -- and that is precisely the axiomatised piece")
    print("  (QOU.Interactions.QBetaCosResummation).")
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
