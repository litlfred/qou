#!/usr/bin/env python3
"""
Probe — the framework BINDS the diproton and the dineutron. Nature does not.

The three per-bond log-suppressions are not free parameters and they are not
abstractions: `_bond_type_L` defines each one as the isolated two-nucleon
log-trace-ratio

    L_X = ln( tr_M(free) / tr_M(atom) )    at   (Z,N) = (2,0), (1,1), (0,2)

so `L_pp` IS the isolated two-proton system, `L_nn` IS the isolated two-neutron
system, and `L_pn` IS the deuteron. That makes all three directly falsifiable
against the two-nucleon data, with no many-body reasoning in between.

Run:

    system           B_framework      nature        verdict
    pn  (deuteron)     +2.8328       +2.2246 BOUND    bound, 27.3 % over
    pp  (diproton)     +2.5416       ~ -0.10 UNBOUND  *** WRONG SIGN ***
    nn  (dineutron)    +3.3069       ~ -0.10 UNBOUND  *** WRONG SIGN ***

Two of the three two-nucleon systems come out **qualitatively** wrong: the
framework predicts bound states at +2.5 and +3.3 MeV where nature has none. The
non-existence of the diproton and the dineutron is textbook, and it is precisely
what makes the deuteron special.

This is not a normalisation artifact. The un-normalised exact traces are +2.0507
(pp) and +3.7978 (nn) — same sign, both bound — so it survives with or without
the writhe factor.

## Why this matters more than the magnitude misses

The binding axis has been sized by *magnitude* residuals: the chain is 3.01x low
at its A -> infinity asymptote, and 27.3 % over at the deuteron. Those framings
understate the problem. A magnitude residual invites a missing additive term; a
**sign** error in 2 of 3 directly-constructed channels says the per-bond object
is not the physical two-nucleon interaction at all.

It also puts a load-bearing corpus result in a different light. The chirality
ordering reported as a positive structural finding —

    b_nn > b_pn > b_pp   ("n-n crossings bind hardest, p-p softest")

is an ordering among three numbers **two of which have the wrong sign**. The
ordering may still encode something real; it cannot be read as an ordering of
two-nucleon binding strengths.

And every `B_sym` for `Z >= 2` or `N >= 2` carries `(Z-1)` pp bonds and `(N-1)`
nn bonds at these values, so the defect is not confined to the two-nucleon rows:
it is (A-2)-fold in the production chain for larger nuclei.

## What the corpus already knew, and what is new here

Known and documented (`docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`):
nature's pp / nn / pn-1S0 channels are unbound; and the Hecke spectral projectors
"can never produce an unbound channel" since `mu_+ + mu_- = 1` forces `mu < 1`.

New here: the production path does not merely *fail to unbind* pp and nn — it
**binds them, at +2.54 and +3.31 MeV**, and those values are consumed by every
multi-nucleon `B_sym`. The projector statement is about a mechanism; this is
about the numbers actually in production.

## Scope (STRICT)

**Scope-(a).** This does not refute the chain's additivity (independently
verified to 1.78e-15 against the exact p(3A) trace), any Lean theorem, or the
framework generally. It is a statement about the per-bond VALUES.

Two readings this does NOT license:

* "the bond is a many-body object, so the comparison is unfair" — it would be,
  except the framework itself constructs `L_pp` from the isolated `(2,0)` word.
  The comparison is the framework's own definition evaluated at its own inputs.
* "therefore some other sign convention fixes it" — not tested here. The
  companion probe (`stacked_interface_writhe_normalised_probe.py`) shows
  unbinding IS available at even-negative stacked powers, so a repair direction
  exists; it is not proposed, and its magnitudes (-0.613 MeV for sigma^-2 vs
  nature's -0.1) are 6-9x off.

NO WITNESS: three derived constants against three textbook facts.

Beans qou-0pzi / qou-brg3; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp

import mass_binding_dashboard as mbd
from _precision import set_compute_dps  # noqa: E402

# (label, Z, N, bond key, nature value MeV, nature is-bound)
SYSTEMS = [
    ("pn  (deuteron)", 1, 1, "pn", +2.2246, True),
    ("pp  (diproton)", 2, 0, "pp", -0.10, False),
    ("nn  (dineutron)", 0, 2, "nn", -0.10, False),
]


def main() -> int:
    set_compute_dps()
    me, q0, E0 = mbd._constants()
    alpha = mp.mpf(str(E0))
    L = mbd._bond_type_L()

    print("The framework's two-nucleon sector vs nature\n")
    print(f"  alpha = E0 = {float(alpha):.6f} MeV     q0 = {q0!r}")
    print("  Each L_X is the framework's OWN isolated two-nucleon log-trace-ratio,")
    print("  so these are its predictions for the two-nucleon systems themselves.\n")
    print("| system          | B_framework | nature   |          | verdict          |")
    print("| --------------- | ----------: | -------: | :------- | :--------------- |")

    wrong = []
    for lbl, Z, N, key, nat, nat_bound in SYSTEMS:
        B = float(alpha * mp.mpf(str(L[key])))
        pred_bound = B > 0
        if pred_bound != nat_bound:
            verdict = "*** WRONG SIGN ***"
            wrong.append((lbl, B, nat))
        else:
            verdict = f"bound, {(B - nat) / abs(nat) * 100:+.1f} % over"
        kind = "BOUND" if nat_bound else "UNBOUND"
        print(f"| {lbl:<15} | {B:>+11.4f} | {nat:>+8.4f} | {kind:<8} | {verdict:<16} |")

    print("\nNot a normalisation artifact — the UN-normalised exact traces:\n")
    try:
        from tr_m_atom_via_transfer import tr_m_atom_zn
    except ImportError as exc:                        # pragma: no cover
        print(f"  (transfer trace unavailable: {exc})")
    else:
        for lbl, Z, N, key, nat, nat_bound in SYSTEMS:
            ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
            raw = float(alpha * mp.log(tf / ta))
            print(f"  {lbl:<15} B_exact_raw = {raw:>+9.4f} MeV"
                  f"   {'(still bound)' if raw > 0 else '(unbound)'}")

    print("\n## Verdict\n")
    print(f"  two-nucleon systems with the WRONG SIGN: {len(wrong)} of {len(SYSTEMS)}")
    for lbl, B, nat in wrong:
        print(f"    {lbl}: framework {B:+.4f} MeV, nature {nat:+.2f} MeV (no bound state)")
    if wrong:
        print("\n  The non-existence of the diproton and the dineutron is textbook, and is")
        print("  exactly what makes the deuteron special. A magnitude residual invites a")
        print("  missing additive term; a SIGN error in 2 of 3 directly-constructed")
        print("  channels says the per-bond object is not the two-nucleon interaction.")
        print("\n  Consequence for the chirality ordering b_nn > b_pn > b_pp reported as a")
        print("  positive structural result: it is an ordering among three numbers two of")
        print("  which have the wrong sign. It may encode something real; it cannot be read")
        print("  as an ordering of two-nucleon binding strengths.")
        print("\n  And it is not confined to the two-nucleon rows: every B_sym with Z >= 2")
        print("  or N >= 2 consumes (Z-1) pp and (N-1) nn bonds at these values.")

    print("\n## Scope\n")
    print("  Scope-(a). Does NOT refute the chain's additivity (verified to 1.78e-15")
    print("  against the exact p(3A) trace), any Lean theorem, or the framework at large.")
    print("  A statement about the per-bond VALUES. The 'it's a many-body bond, unfair")
    print("  comparison' reading is unavailable: the framework builds L_pp from the")
    print("  isolated (2,0) word itself.")
    print("\n(no witness by design — three derived constants against three textbook facts.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
