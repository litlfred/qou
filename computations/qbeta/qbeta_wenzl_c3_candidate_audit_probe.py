#!/usr/bin/env python3
"""The Wenzl c_3 candidate: a fitted near-match whose "formal derivation" is `rfl`.

Bean `qou-cds1`, tranche S1.  A worked instance of the gate-exhaustion finding in
`qbeta_d_gate_inventory_is_exhausted_probe.py` (10/10): a candidate can carry a
categorical story, pass every gate named for the D-frame generator, and still be
a fit that does not match.

`docs/coordination/2026-06-13-qbeta-habiro-element-ledger.md` records:

    "Swept q-deformed fractions against the empirical c_3 = -2.06249 from
     Kashiwara truncation."
    "Finding: The residual EXACTLY matches -2 - (3/2) W_4(q), where
     W_4(q) = 1/[4]_q! is the alternating Wenzl weight."
    "Status: Structural decomposition identified. Proceeding to formal
     derivation."

Three things this file measures, none of which is a claim that the Wenzl weight
is the wrong object -- only that this identification is not established.

1. THE SELECTION METHOD IS A FIT, by the ledger's own wording: a sweep of
   candidate fractions against an empirically extracted target.

2. "EXACTLY MATCHES" IS NOT SUPPORTED at the precision measured -- not even
   against the ledger's own stated target.

3. THE PROMISED FORMAL DERIVATION IS A TAUTOLOGY.
   `folio/quantum-observable-universe/lean/QOU/BraidKnot/QBetaWenzlDecomposition.lean`
   defines

       noncomputable def q_beta_c3_wenzl_coefficient (q : R) : R :=
         -2 - (3/2 : R) * wenzlAltWeight 4 q

   and then "proves"

       theorem q_beta_c3_wenzl_decomposition_exact {q : R} :
         q_beta_c3_wenzl_coefficient q = -2 - (3/2 : R) * wenzlAltWeight 4 q := by
         rfl

   which unfolds the definition and proves it equals itself.  Its docstring says
   "Here we formally assert the Wenzl weight identity for the c_3 scalar"; it
   asserts nothing.  This is `X = X := rfl`, banned by AGENTS.md
   "No trivial trues, no tautologies, no laundering" rule 5, and the def's OWN
   docstring says the value was "Empirically identified".

   Sorry-free is not derived.  Nothing in that file connects the Wenzl weight to
   c_3; it restates the definition.

Exact mpmath at 50 dps; no float64; emits no witness (it audits a claim).
"""
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import pathlib
import sys

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
mp.mp.dps = 50

from qou_substrate.constants import M_E_MEV, Q_NEUTRON_MEV, q_at  # noqa: E402
from qbeta_utils import c3_proton_extracted  # noqa: E402

ME = mp.mpf(str(M_E_MEV))
QEXP = mp.mpf(str(Q_NEUTRON_MEV))
MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"


def qint(n, q):
    return (q**n - q ** (-n)) / (q - 1 / q)


def wenzl_W4(q):
    return 1 / (qint(1, q) * qint(2, q) * qint(3, q) * qint(4, q))


def ladder_N3(q, c3):
    """The ledger's own N=3 ansatz, at a stated c_3.

    Q_beta = Q_A * cos(alpha_N1) * (1 - b^2 hbar^4) * (1 + c_3 b^3 hbar^6)

    Convention C (the frame the ledger was written in).  `w_blind` and the
    Q_A form are taken verbatim from `qbeta_ladder_convention_fee_probe`.
    """
    h = q - 1 / q
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    # CONVENTION C, DELIBERATELY, AND SAID SO — this was the silent part.
    #
    # `z_C = sqrt(q)/(q+1) = 1/(sqrt(q) + 1/sqrt(q)) = 0.49932033418369445241`
    # at the proton pin, against the canonical `z_D = q^3/(q^2+1) =
    # 0.61268803714646525160` (owner ruling 2026-08-15). This site fed the
    # ladder's `alpha = (z-1)h/2` from C while declaring nothing — neither the
    # variable name nor the module docstring said which frame it was in, so a
    # reader had no way to know (bean `qou-qgtk`, measured down to three such
    # sites on 2026-09-15).
    #
    # NOT SWAPPED TO z_D, and that is not caution — it is the rule.
    # `qbeta_ladder_convention_fee_probe` records that the published agreement
    # needs z_C, that substituting z_D sends the ladder to 601192 ppb, and that
    # this number is NOT "what convention D gives": AGENTS.md and
    # `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` both state the ladder must be
    # RE-DERIVED under D and that **a z-swap is not a valid move**. If the decay
    # channel's decomposition kills the third row then its trace IS z_D, and the
    # existing C-frame ladder is not that trace. Excising C here therefore means
    # DECLARING it, the `qou-cexc` precedent ("declared, not silent"), and
    # leaving the re-derivation to the arc that owns it.
    z = mp.sqrt(q) / (q + 1)
    eps = (q - 1 / q) / 2 * h - h
    QA = abs(_qbeta_e0.order_zero_scaled(eps * ME, q))
    al = (z - 1) * h / 2
    return (QA * mp.cos(al - b * hb**2 / 2)
            * (1 - b**2 * hb**4)
            * (1 + c3 * b**3 * hb**6))


def ppm(v):
    return (v - QEXP) / QEXP * mp.mpf(10) ** 6


def main() -> int:
    checks = []

    q_pr = q_at(50)
    q_mu = mp.mpf(str(json.loads(MUON_WITNESS.read_text())
                      ["derived_50_digit"]["q"]))

    W4 = wenzl_W4(q_pr)
    cand = -2 - mp.mpf(3) / 2 * W4

    ledger_target = mp.mpf("-2.06249")          # the ledger's own stated target
    live_proton = c3_proton_extracted()         # live extracted c_3, proton pin (recomputed)
    # NOT recomputed (out of scope of the 2026-10-13 proton trace): this muon literal
    # is 2.2e-9 from the CODATA-2018 muon-pin extraction (-2.0202002350213) and
    # 1.7e-4 from the live CODATA-2022 one (-2.0198603119); see the PR that added
    # c3_proton_extracted.
    live_muon = mp.mpf("-2.0202002328")         # extracted c_3, muon pin (typed)

    print("Convention C (the ledger's frame).  mpmath, 50 dps.\n")
    print(f"  q0 (proton)        = {mp.nstr(q_pr, 15)}")
    print(f"  [4]_q!             = {mp.nstr(1 / W4, 12)}")
    print(f"  W_4 = 1/[4]_q!     = {mp.nstr(W4, 12)}")
    print(f"  candidate  -2-(3/2)W_4 = {mp.nstr(cand, 12)}\n")

    print("  claimed 'EXACTLY matches' -- measured:")
    rows = [("ledger's own target", ledger_target),
            ("live extracted, proton pin", live_proton),
            ("live extracted, muon pin", live_muon)]
    for name, tgt in rows:
        err = abs(cand - tgt) / abs(tgt) * 100
        print(f"    vs {name:28} {mp.nstr(tgt, 12):>16}   {mp.nstr(err, 4):>9} %")

    # 1. Not exact against ANY of them -- including the ledger's own target.
    for name, tgt in rows:
        err = abs(cand - tgt) / abs(tgt)
        checks.append((f"NOT exact vs {name} (>0.1%)", err > mp.mpf("0.001")))

    # 2. It passes the bar-parity filter -- as every symmetric q-integer
    #    expression does.  This is the gate-exhaustion point, instantiated.
    Q = sp.symbols("Q", positive=True)
    qi = lambda n: (Q**n - Q ** (-n)) / (Q - 1 / Q)   # noqa: E731
    W4s = 1 / (qi(1) * qi(2) * qi(3) * qi(4))
    ratio = sp.simplify(W4s.subs(Q, 1 / Q) / W4s)
    checks.append(("W_4 is bar-invariant (passes the parity FILTER)",
                   sp.simplify(ratio - 1) == 0))
    cand_s = -2 - sp.Rational(3, 2) * W4s
    ratio_c = sp.simplify(cand_s.subs(Q, 1 / Q) / cand_s)
    checks.append(("so is the whole candidate -2-(3/2)W_4",
                   sp.simplify(ratio_c - 1) == 0))

    # 3. The ledger's headline "-0.0005 ppm" is about the LADDER, not c_3.
    #    Check it at both pins, using the ledger's own N=3 ansatz.
    print("\n  the ledger's headline is a LADDER error, not a c_3 error.")
    print("  its N=3 ansatz at each pin, ppm vs CODATA:\n")
    print(f"    {'pin':8} {'c_3 used':28} {'residual (ppm)':>18}")
    res = {}
    for label, q0 in (("proton", q_pr), ("muon", q_mu)):
        W = wenzl_W4(q0)
        for tag, c3 in (("Wenzl  -2-(3/2)W_4", -2 - mp.mpf(3) / 2 * W),
                        ("bare   -2", mp.mpf(-2))):
            v = ppm(ladder_N3(q0, c3))
            res[(label, tag)] = v
            print(f"    {label:8} {tag:28} {mp.nstr(v, 8):>18}")

    claimed = mp.mpf("-0.0005")
    best = min(abs(res[k] - claimed) for k in res)
    checks.append(("no pin reproduces the claimed -0.0005 ppm within 0.001",
                   best > mp.mpf("0.001")))

    print(f"\n    claimed in the ledger: {mp.nstr(claimed, 4)} ppm")
    print(f"    closest reconstruction is {mp.nstr(best, 4)} ppm away")

    print("\n--- checks ---")
    ok = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok = ok and bool(passed)
    print(f"\n{sum(1 for _, p in checks if p)}/{len(checks)}")

    print("""
FINDING

  The Wenzl c_3 identification is a FIT that does not match, and its recorded
  formalization proves nothing:

    selection      a sweep against an empirically extracted target
                   (the ledger's own wording)
    "exactly"      0.14 % off the ledger's own target; 0.47 % off the live
                   proton-pin c_3; 1.95 % off the muon-pin one
    formalization  `theorem ... := by rfl` on its own definition -- X = X

  And it PASSES the bar-parity gate, because W_4 is built from symmetric
  q-integers and every such expression is bar-invariant.  That is the
  gate-exhaustion finding instantiated: a candidate with a categorical story
  that clears every named gate and is still a fit.

WHICH OF THESE ARE RECONSTRUCTION-INDEPENDENT

  Findings 1-3 do not depend on how this file rebuilds the ladder:
    - "0.14 % off the ledger's own target" compares two stated numbers;
    - the `rfl` tautology is read directly off the .lean;
    - bar-invariance of W_4 is symbolic.
  The FOURTH -- that no pin reproduces the claimed -0.0005 ppm -- DOES depend on
  the reconstruction (this file fixes the published colour-blind `w`, today's
  CODATA, and the N=3 truncation the ledger states).  Treat it as the weakest of
  the four: it says this reconstruction does not reproduce the figure, not that
  the figure is wrong.  The same caution that applied to table 3 in `qou-54g5`.

SCOPE (a).  This does NOT claim the Wenzl weight is the wrong object, that
1/[4]_q! plays no role, or that the ledger's categorical reasoning is wrong.
It claims only that this identification is UNESTABLISHED: not exact, selected by
fitting, and not derived by the Lean that was written for it.

WHAT WOULD ESTABLISH IT: a derivation of c_3 FROM the H_4 Wenzl projector -- the
same route the ledger says produced 1/[4]_q! in the m_n-m_p split -- with the
Lean deriving the coefficient rather than restating it.  Not attempted here.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
