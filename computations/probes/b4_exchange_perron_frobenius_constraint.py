#!/usr/bin/env python3
"""Value leg — Perron–Frobenius EXCLUDES the positive-factor exchange matrix.

Scoping: docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md.
The functional form is pinned (b4_slater_dictionary_functional_form): the [1^4]
connected binding is `B = −ln det(I + G_exchange)` with a dominant-NEGATIVE
eigenvalue (net-attractive) exchange matrix `G`. This unit builds `G` from the
framework's nucleon-flavor pair factors and tests the eigenvalue-sign requirement.

BUILD. ⁴He = 4 nucleons (p,p,n,n); `G` is the 4×4 exchange matrix, 0 diagonal,
off-diagonal the pair factors (all POSITIVE at q₀):
    g_pp = g_nn = z = 0.4993,   g_pn = z − h/2 = 0.3948.

RESULT (scope-(b), Perron–Frobenius — a THEOREM, not a fit):
  eigenvalues(G) = (−0.499, −0.499, −0.290, **+1.289**) ⇒ dominant = **+1.289 > 0**.
  Perron–Frobenius: a nonnegative irreducible matrix has its largest-modulus
  eigenvalue POSITIVE. So the POSITIVE pair factors can NEVER give the required
  dominant-negative eigenvalue — they are EXCLUDED for the exchange matrix.

CONSEQUENCE. The exchange matrix `G` must have NEGATIVE entries — the exchange is
the SIGN-CARRYING channel, not the (bar-even, positive) binding factors `z`. This
closes the chain and connects the value to the bar-parity decomposition:
  • I-par proved `z` bar-EVEN, `h` bar-ODD (the sign-carrying channel);
  • the binding SCALE uses `z` (bar-even), but the EXCHANGE that antisymmetrizes
    the [1^4] shell must use the bar-ODD / writhe channel (sign-carrying);
  • this is the same chirality-sign channel that solved the 3-body sign
    (option-e ledger 2026-06-24), now identified as the source of the ⁴He
    connected magnitude.

So the [1^4] value = `−ln det(I + G)` with `G` built from the bar-ODD (writhe /
`h`, sign-carrying) exchange — NOT the positive binding factors. Deriving the
principled bar-odd exchange ENTRIES (which `h`-combination, with what writhe
signs) is the remaining research core; it must NOT be fitted to 9.243. This probe
records the PF exclusion + the bar-odd identification, the maximal rigorous
narrowing before that derivation.

`-- Ref:` b4_slater_dictionary_functional_form.py (functional form);
b4_connected_bar_parity_probe.py (I-par: z even, h odd); option-e.md (chiral sign).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import closed_form_tau_M as C  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)


def main() -> int:
    q = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
    z = C.markov_z(q)
    h = q - 1 / q
    g_pp = g_nn = z
    g_pn = z - h / 2

    G = mp.matrix([
        [0, g_pp, g_pn, g_pn],
        [g_pp, 0, g_pn, g_pn],
        [g_pn, g_pn, 0, g_nn],
        [g_pn, g_pn, g_nn, 0],
    ])
    E, _ = mp.eig(G)
    ev = sorted([mp.re(x) for x in E])
    lam_dom = max(ev, key=lambda x: abs(x))
    dom_is_positive = lam_dom > 0

    result = {
        "pair_factors": {"g_pp": mp.nstr(g_pp, 8), "g_pn": mp.nstr(g_pn, 8), "all_positive": True},
        "he4_exchange_eigenvalues": [mp.nstr(x, 6) for x in ev],
        "dominant_eigenvalue": mp.nstr(lam_dom, 8),
        "dominant_is_positive": bool(dom_is_positive),
        "perron_frobenius": ("nonnegative irreducible ⇒ largest-modulus eigenvalue positive ⇒ "
                             "positive pair factors CANNOT give the required λ<0 (EXCLUDED)"),
        "consequence": ("the [1^4] exchange matrix must have NEGATIVE entries — the exchange is "
                        "the SIGN-CARRYING (bar-ODD / writhe) channel, not the bar-even positive "
                        "binding factors z. Same chirality-sign channel that solved the 3-body sign."),
        "verdict": (
            "Perron–Frobenius EXCLUDES the positive-pair-factor exchange matrix (dominant "
            "eigenvalue +1.289 > 0, required < 0). The [1^4] connected magnitude therefore comes "
            "from the bar-ODD (sign-carrying / writhe) exchange in −ln det(I+G), not the bar-even "
            "binding factors. Deriving the principled bar-odd exchange ENTRIES is the remaining "
            "research core (must not be fitted to 9.243). Scope-(b), no fit."),
    }

    payload = {
        "computation": "b4-exchange-perron-frobenius-constraint",
        "description": ("Perron–Frobenius excludes the positive-pair-factor [1^4] exchange matrix "
                        "(dominant eigenvalue +1.289 > 0, needs <0) ⇒ the exchange must be "
                        "sign-carrying (bar-ODD/writhe), not the bar-even binding factors. "
                        "audit-only, no fit."),
        "tier": "structural (Perron–Frobenius theorem on the framework exchange matrix)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] value leg, exchange-matrix sign constraint",
            "spec": "docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md",
            "next_unit": "derive the bar-odd (writhe/h) exchange entries; read −ln det vs 9.243 (verdict, not fit)",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-exchange-perron-frobenius-constraint", payload,
        script_path=__file__, engine="python+mpmath", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("positive_factor_dominant_eigenvalue_positive",
                     computed=str(bool(dom_is_positive)), expected="True")
    wb.add_assertion("positive_factors_excluded_for_attractive_exchange",
                     computed=str(bool(dom_is_positive)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Perron–Frobenius exclusion of the positive-factor exchange ===")
    print(f"  g_pp=g_nn={float(g_pp):.4f}  g_pn={float(g_pn):.4f}  (all > 0)")
    print(f"  ⁴He exchange eigenvalues: {[f'{float(x):+.4f}' for x in ev]}")
    print(f"  dominant = {float(lam_dom):+.4f}  (needs < 0)  ⇒ EXCLUDED by Perron–Frobenius")
    print("  ⇒ exchange must be SIGN-CARRYING (bar-ODD / writhe), not the bar-even z factors.")
    print("  NEXT: derive the bar-odd exchange entries; read −ln det vs 9.243 (verdict, not fit).")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
