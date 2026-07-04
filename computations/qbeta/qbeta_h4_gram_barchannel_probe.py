#!/usr/bin/env python3
"""H4 n=4 cup-diagram Gram bar-channel split (bean 8we6, Brunnian/SDP route groundwork).

The two explicit appended-strand route-A objects (lepton, brane) fail the c2/c3
stability gate — at full coupling AND at linear order in the coupling — because
appending a sigma_2 crossing to B3.(3-quark) redistributes NF weight across all
word lengths (audit 2026-07-04-8we6-h4-route-a-explicit-strand-gate-scan.md).
The structurally-correct survivor is a CHANNEL-PROJECTED construction: the
bar-even singlet channel of the n=4 cup-diagram space, orthogonal to the
nucleon's short-word structure.

This probe records the well-defined input to that route — the n=4 Frobenius/
Temperley-Lieb Gram in the cup basis {u1=cups(12)(34), u2=nested(14)(23)} and its
bar-even / bar-odd eigenchannel split (the analogue of the 2-strand e_+/e_-).
It does NOT compute a c_4^even value: the SDP objective weights t / net target
n_target for the singlet selection, and the channel -> Q_beta-ladder linkage, are
owner-gated framework choices (NOT agent ansatz), per the route-B-prune audit.

audit_only. No production wiring, no fit.

`-- Ref:` alpha_k_four_strand_singlet_selection.py (the same n=4 Gram + the
Catalan(m) singlet ladder); prop:operator-selection-lp (the LP/SDP dual infra).
"""
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE.parent), str(_HERE.parent / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main():
    q = sp.Symbol("q", positive=True)
    delta = q + 1 / q  # [2]_q
    G = sp.Matrix([[delta**2, delta], [delta, delta**2]])

    v_even = sp.Matrix([1, 1])   # u1 + u2  (symmetric -> bar-even)
    v_odd = sp.Matrix([1, -1])   # u1 - u2  (antisymmetric -> bar-odd)
    ev_even = sp.factor(sp.simplify((v_even.T * G * v_even)[0] / (v_even.T * v_even)[0]))
    ev_odd = sp.factor(sp.simplify((v_odd.T * G * v_odd)[0] / (v_odd.T * v_odd)[0]))

    # both eigenvalues are bar-even functions (delta is bar-invariant)
    bar_even_invariant = sp.simplify(ev_even.subs(q, 1 / q) - ev_even) == 0
    bar_odd_invariant = sp.simplify(ev_odd.subs(q, 1 / q) - ev_odd) == 0

    q0 = sp.Rational(110998, 100000)
    result = {
        "gram_basis": "{u1 = cups(12)(34), u2 = nested cups(14)(23)}",
        "gram_matrix": "[[delta^2, delta], [delta, delta^2]], delta = [2]_q = q + 1/q",
        "bar_even_channel": {
            "eigenvector": "u1 + u2",
            "eigenvalue": str(ev_even),
            "eigenvalue_factored": "delta*(delta+1) = (q^2+1)(q^2+q+1)/q^2",
            "role": "where a c_4^even rung must live (symmetric singlet)",
            "value_at_q0": float(ev_even.subs(q, q0)),
        },
        "bar_odd_channel": {
            "eigenvector": "u1 - u2",
            "eigenvalue": str(ev_odd),
            "eigenvalue_factored": "delta*(delta-1) = (q^2+1)(q^2-q+1)/q^2",
            "role": "bar-odd channel (the 4-strand analogue of e_-)",
            "value_at_q0": float(ev_odd.subs(q, q0)),
        },
        "delta_at_q0": float(delta.subs(q, q0)),
        "singlet_dim_n4": "Catalan(2) = 2  (dim Hom(1, A^{tensor 4}), generic q)",
        "owner_gated_linkage": (
            "The SDP objective weights t and net target n_target for the n=4 "
            "singlet selection, and the selected-channel -> Q_beta net-route "
            "ladder linkage, are framework choices (NOT agent ansatz). This "
            "probe fixes only the Gram + its bar-channel split."
        ),
    }

    payload = {
        "computation": "qbeta-h4-gram-barchannel-split",
        "description": "n=4 cup-diagram Gram + bar-even/bar-odd eigenchannel split — "
                       "input groundwork for the Brunnian/SDP route-A c_4^even attempt "
                       "(bean 8we6). audit_only; no c_4 value computed (owner-gated linkage).",
        "audit_only": True,
        "tier": "structural-exact (symbolic Gram eigenchannel split; no fit, no anchor sweep)",
        "assertions": [
            {"name": "bar_even_eigenvalue_bar_invariant", "passed": bool(bar_even_invariant)},
            {"name": "bar_odd_eigenvalue_bar_invariant", "passed": bool(bar_odd_invariant)},
        ],
        "allPassed": bool(bar_even_invariant and bar_odd_invariant),
        "result": result,
        "context": {
            "axis": "Q_beta 1ppQ achievable-arm — H4 c_4^even rung (Brunnian/SDP route)",
            "predecessor_scan": "docs/audits/2026-07-04-8we6-h4-route-a-explicit-strand-gate-scan.md",
            "gram_source": "computations/alpha_k_four_strand_singlet_selection.py",
            "ledger": "docs/coordination/1ppq-qbeta.md",
        },
    }
    out = WitnessBuilder.wrap_legacy(
        "qbeta-h4-gram-barchannel-split", payload,
        script_path=__file__, engine="sympy",
    ).save()

    print("=== n=4 Gram bar-channel split (Brunnian/SDP route groundwork) ===")
    print("  bar-EVEN (u1+u2): eigenvalue", ev_even, " @q0 =", float(ev_even.subs(q, q0)))
    print("  bar-ODD  (u1-u2): eigenvalue", ev_odd, " @q0 =", float(ev_odd.subs(q, q0)))
    print("  both bar-invariant:", bool(bar_even_invariant and bar_odd_invariant))
    print("  witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
