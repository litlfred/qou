#!/usr/bin/env python3
"""What are the indices in kappa's normaliser [2]_q [3]_q, and why the A=3
anchor cannot tell you.

The recovered producer `probe_kappa_categorical_h7a_closed.py` describes the
normaliser as

    "[2]_q * [3]_q -- the quantum dimension of V_2 (x) V_3 (the LR fusion of
     the two relevant magic-shell channels FOR A=3 ANCHORS)"

That phrase fixes the *value* at A=3 but not the *rule*.  At least three index
rules reproduce `[2]_q [3]_q` there and disagree everywhere else:

    R1  (A_magic, A)            -- magic number and mass number
    R2  (2, 3), fixed           -- sl_2 irreps V_2, V_3; shell-independent
    R3  (A_magic, A_magic + 1)  -- the shell and its successor

All three give (2, 3) at the A=3 single-magic anchors, which is the only place
kappa has ever been evaluated.  They give (8, 15), (2, 3) and (8, 9) at the
8-shell anchors 15O / 15N.

This probe does not choose between them.  Choosing on the numbers would be a
fit, and it is the fit that got `prop:magic-shell-coupling-kappa` demoted to a
conjecture in the first place.  What it does is measure the spread, which is
the honest statement of how underdetermined the conjecture currently is, and
show that the A=3 anchor is degenerate for the index rule in exactly the way
it is already known to be degenerate for the excess convention (see
`probe_kappa_shell8_excess_convention.py`).

Ref: conj:magic-shell-coupling-kappa
Bean: qou-o16k
"""

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
from pathlib import Path as _P
_SUB = _P(__file__).resolve().parent / "substrate"
if str(_SUB) not in sys.path:
    sys.path.insert(0, str(_SUB))
import mpmath as mp  # noqa: E402
from _precision import fmt, COMPUTE_DPS  # noqa: E402

mp.mp.dps = COMPUTE_DPS


def _ser(o):
    """Serialize every real to a _precision.fmt string; ints stay ints.

    The NO-FLOAT64 family forbids raw float64 in a witness. Values are carried
    as mpmath.mpf from their source above and rendered here, so no float64 ever
    reaches the JSON.
    """
    if isinstance(o, bool) or isinstance(o, int):
        return o
    if isinstance(o, (float, mp.mpf)):
        return fmt(mp.mpf(o))
    if isinstance(o, dict):
        return {k: _ser(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_ser(v) for v in o]
    return o


import json
import math
from datetime import datetime, timezone
from pathlib import Path
from codata_constants import M_E_MEV

# Experimental (proton) pin -- the standing default for new compute.
Q0 = mp.mpf("1.1099785827513808")
Q0_PIN = "proton (experimental layer), m_p/m_e"
M_E_MEV = M_E_MEV
# Read from kappa-provenance.witness.json (parameters.published_kappa_MeV)
# rather than typed, so the copy cannot go stale (witness-value copy ratchet).
KAPPA_EMPIRICAL = mp.mpf(json.loads((Path(__file__).resolve().parent / "kappa-provenance.witness.json").read_text(encoding="utf-8"))["parameters"]["published_kappa_MeV"])


def bracket(q: float, n: int) -> float:
    return (q**n - q ** (-n)) / (q - 1 / q)


def kappa_with_normaliser(q: float, m_e: float, norm: float) -> float:
    h = q - 1 / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    return -e0 * mp.log(1 / h) / norm


# (rule id, description, index function of (A_magic, A))
RULES = [
    ("R1", "(A_magic, A) -- magic number and mass number", lambda m, a: (m, a)),
    ("R2", "(2, 3) fixed -- sl_2 irreps V_2, V_3, shell-independent", lambda m, a: (2, 3)),
    ("R3", "(A_magic, A_magic+1) -- the shell and its successor", lambda m, a: (m, m + 1)),
]

# (label, A_magic, A, status)
ANCHORS = [
    ("A=3 single-magic (3He / 3H)", 2, 3, "the only anchors kappa has seen"),
    ("A=15 single-magic (15O / 15N)", 8, 15, "never evaluated"),
    ("A=39 single-magic (39K)", 20, 39, "never evaluated"),
]


def main() -> None:
    quantum = (_qbeta_e0.order_zero_scaled(M_E_MEV, Q0)) * mp.log(1 / (Q0 - 1 / Q0))

    results = []
    for label, magic, a, status in ANCHORS:
        per_rule = {}
        for rid, desc, idx in RULES:
            i, j = idx(magic, a)
            norm = bracket(Q0, i) * bracket(Q0, j)
            per_rule[rid] = {
                "indices": [i, j],
                "normaliser": norm,
                "kappa_MeV": kappa_with_normaliser(Q0, M_E_MEV, norm),
            }
        kappas = [v["kappa_MeV"] for v in per_rule.values()]
        spread = max(kappas) - min(kappas)
        results.append(
            {
                "anchor": label,
                "A_magic": magic,
                "A": a,
                "status": status,
                "by_rule": per_rule,
                "kappa_spread_MeV": spread,
                "rules_agree": spread < 1e-12,
            }
        )

    a3 = results[0]
    assertions = []

    def check(name: str, ok: bool, detail: str) -> None:
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})

    check(
        "all_rules_coincide_at_the_A3_anchor",
        a3["rules_agree"],
        "R1, R2 and R3 all give indices (2,3) at A=3, so the anchor that fixed "
        "kappa cannot distinguish the index rule -- the same degeneracy the "
        "excess conventions have there",
    )
    check(
        "A3_value_reproduces_the_published_closed_form",
        abs(a3["by_rule"]["R2"]["kappa_MeV"] - (-1.0704241)) < 1e-6,
        "the shared A=3 value is the published kappa_closed, so this probe is "
        "reading the same object the conjecture states",
    )
    check(
        "rules_diverge_at_every_untested_shell",
        all(not r["rules_agree"] for r in results[1:]),
        "R1, R2 and R3 disagree at the 8 and 20 shells -- the discriminating "
        "measurement lies entirely outside the fitted region",
    )
    check(
        "no_rule_selected",
        True,
        "this probe deliberately does not choose a rule; selecting one on the "
        "numbers would be a new fit, which is what the demotion was about",
    )

    print(f"E_0*log(1/h) = {quantum:.7f} MeV   [q0 pin: {Q0_PIN}]")
    print(f"kappa_empirical = {KAPPA_EMPIRICAL:.7f} MeV/excess\n")
    for r in results:
        print(f"{r['anchor']}   (A_magic={r['A_magic']}, A={r['A']})   -- {r['status']}")
        for rid, desc, _ in RULES:
            v = r["by_rule"][rid]
            i, j = v["indices"]
            print(
                f"   {rid}  [{i}]_q*[{j}]_q = {v['normaliser']:10.5f}"
                f"   -> kappa = {v['kappa_MeV']:10.5f} MeV     {desc}"
            )
        verdict = "ALL RULES AGREE" if r["rules_agree"] else f"spread {r['kappa_spread_MeV']:.5f} MeV"
        print(f"   => {verdict}\n")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness_raw = {
        "engine": "python-stdlib",
        "engineVersion": "3",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "kappa-normaliser-index-rule",
        "scriptFile": "probe_kappa_normaliser_index_rule.py",
        "contentBlock": "conj:magic-shell-coupling-kappa",
        "description": (
            "Underdetermination probe, no fit and no rule selected. Three index "
            "rules for kappa's normaliser all reproduce [2]_q[3]_q at the A=3 "
            "anchors -- the only place kappa has been evaluated -- and diverge "
            "at every magic shell above 2."
        ),
        "parameters": {
            "q_0": Q0,
            "q_0_pin": Q0_PIN,
            "m_e_MeV": M_E_MEV,
            "kappa_empirical_MeV": KAPPA_EMPIRICAL,
            "rules": [{"id": rid, "description": desc} for rid, desc, _ in RULES],
        },
        "data": {"quantum_E0_log_inv_h_MeV": quantum, "anchors": results},
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }
    witness = _ser(witness_raw)
    out = Path(__file__).with_name("kappa-normaliser-index-rule.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness -> {out.name}  (allPassed={witness_raw['allPassed']})")


if __name__ == "__main__":
    main()
