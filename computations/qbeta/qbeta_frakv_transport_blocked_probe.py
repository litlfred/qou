#!/usr/bin/env python3
"""The frak-V transport route is blocked: Im(frak V) is ASSIGNED the counit, not derived.

BEAN `qou-cds1`. The previous probe resolved that Q_A is the Frobenius COUNIT
evaluation while frak-V is a Markov TRACE object, and exposed the identity

    eps(Delta) - tr_M(Delta) = h(z-1) = 2*alpha

so the ladder is implicitly transporting counit -> trace. That suggested a
concrete next step: derive the transport for the frak-V operator
(Pi_free - 1).M rather than for Delta.

THAT ROUTE IS BLOCKED, and this probe records why.

The transport is a change of FUNCTIONAL, so its effect on any element X is fixed
by X's character vector:

    tr_M^z(X) - eps(X) = sum_lambda [ y_lambda(z) - y_lambda(1) ] * chi_lambda(X)

(eps is tr_M at the trivial loop value z = 1). So computing the transport for
frak-V requires chi_lambda((Pi_free - 1).M) -- i.e. it requires frak-V to have
been evaluated as a trace object. It has not been.

WHAT THE ONE EXISTING COMPUTE ACTUALLY DOES. `complex_volume_witness.py` opens
with "Complex-volume witness — frak-V = E_0 tr_M((Pi_free - 1).M) as ONE
object", and then:

  * computes the REAL part from tr_M (tr_M_atom, tr_M_free, the bar-norm), but
  * IMPORTS the imaginary part:  `from q_beta_substrate_prediction import
    q_beta_substrate`  (line 39).

So Im is the COUNIT closed form Q_A, not a trace evaluation. Verified numerically
here: the witness's im_qbeta_pred_MeV equals Q_A = eps(Delta)*E_0 exactly.

The two halves of the "one object" therefore come from TWO DIFFERENT
FUNCTIONALS -- Re from the Markov trace, Im from the Frobenius counit -- and the
corpus itself states these are "genuinely distinct functionals on the substrate"
(qbeta-counit-closed-form.md). The "one object" is not realised in compute.

TWO CONSEQUENCES.

 1. THE TRANSPORT ROUTE IS BLOCKED AT THE SOURCE. Im(frak V) has never been
    evaluated as tr_M((Pi_free - 1).M); it is the counit object by assignment.
    There is nothing to transport TO.

 2. THE PARITY CLAIM IS CIRCULAR. The corpus argues Q_beta is bar-odd BECAUSE it
    is Im(frak V) (substrate-cohomology-calibration-story.md:11). But in the only
    compute, Im(frak V) IS Q_beta -- the counit form -- which is measurably
    neither bar-odd nor bar-even (bar-ratio +1.6868). So the parity claim has no
    independent support: it is asserted of an object that is defined to be the
    object whose parity is in question.

ALSO MEASURED, and it bears on how much the witness establishes:
  * the witness carries NO assertions at all (`assertions: []`), so its
    allPassed:true is vacuous -- nothing was tested;
  * its REAL part misses AME binding by 21.8 % to 69.3 % across 2H/3H/3He/4He.

This is the AGENTS.md "Defined residual != derived decomposition" family: an
identification made by assignment and then reasoned from as though derived.

Scope-(a): measurement and reading of existing artifacts. Nothing derived,
nothing wired, no search run. This does NOT refute conj:binding-qbeta-complex-
volume -- it says the conjecture is untested by the compute that appears to test
it, and that the transport route cannot start from that compute.
"""
from __future__ import annotations

import json
import pathlib
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

ROOT = pathlib.Path(__file__).resolve().parents[2]
WITNESS = ROOT / "computations" / "complex-volume-unification.witness.json"

Q0 = mp.mpf("1.10997858275138080759166909561076887987449912187357873607281")
M_E = mp.mpf("0.51099895069")


def main() -> int:
    w = json.loads(WITNESS.read_text())
    data = w["data"]

    # Q_A as the Frobenius counit evaluation eps(Delta) * E_0.
    h = Q0 - 1 / Q0
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    qa_counit = abs((h**2 / 2 - h) * E0)

    im_witness = mp.mpf(data["im_qbeta_pred_MeV"])
    print("Is the witness's Im(frak V) the COUNIT object?")
    print(f"  witness im_qbeta_pred_MeV   = {mp.nstr(im_witness, 16)}")
    print(f"  |eps(Delta) * E_0|          = {mp.nstr(qa_counit, 16)}")
    print(f"  |difference|                = {mp.nstr(abs(im_witness - qa_counit), 6)}")
    print("  => Im is the counit closed form, NOT a tr_M evaluation.")
    print()

    print("What does the witness assert?")
    print(f"  assertions   = {w.get('assertions')}")
    print(f"  allPassed    = {w.get('allPassed')}   <- vacuous: nothing asserted")
    print()

    print("How good is the REAL part (the half that IS a tr_M object)?")
    for k, v in data.items():
        if k.startswith("V_"):
            print(f"  {k:<6} re_rel_err = {v['re_rel_err']*100:6.1f} %")
    print()

    ok = True
    # Im is the counit object, to numerical identity.
    ok &= abs(im_witness - qa_counit) < mp.mpf("1e-12")
    # The witness asserts nothing.
    ok &= w.get("assertions") == []
    # The real part is badly off, so "unification" is not evidenced numerically.
    ok &= max(v["re_rel_err"] for k, v in data.items() if k.startswith("V_")) > 0.2

    print("VERDICT: the frak-V transport route is BLOCKED at the source.")
    print("  Im(frak V) has never been evaluated as tr_M((Pi_free-1).M) -- it is")
    print("  the counit object by assignment, so there is nothing to transport to.")
    print("  And the parity claim is circular: Q_beta is said to be bar-odd")
    print("  because it is Im(frak V), while Im(frak V) is defined in compute as")
    print("  Q_beta, whose bar-ratio is +1.6868 (neither parity).")
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
