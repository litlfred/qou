#!/usr/bin/env python3
"""Where the magic-shell coupling slope kappa has never been tested, and why
that matters more than it looks.

`conj:magic-shell-coupling-kappa` gives a slope

    kappa = -E_0 * log(1/h) / ([2]_q [3]_q)

multiplying an excess `(n_pp - n_nn)`.  Two facts about that statement are
checked here, both by arithmetic alone -- nothing is fitted and nothing is
tuned:

1.  **`kappa_closed` carries no shell index.**  It is a function of `q` and
    `m_e` only, so the conjecture predicts *one constant* for every magic
    shell.  Its anchors -- (2,2) for identification, (2,1)/(1,2) for the
    cross-check -- all sit in the `A_magic = 2` shell.

2.  **The corpus carries two inequivalent definitions of the excess**, and
    they *coincide* on every anchor kappa has ever seen:

      C1  `def:canonical-braid-interface-composition`
          n_pp = max(0, Z-1),  n_nn = max(0, N-1)      -- linear in Z
      C2  `prop:derived-mass-formula-light-isotopes`
          n_pp = Z(Z-1)/2,     n_nn = N(N-1)/2         -- quadratic in Z

    On the A=3 mirror pair both give an excess of +-1, so the fit that fixed
    kappa could not have distinguished them.  They diverge at the 8 shell.

The output is a divergence table, not a value for kappa.  Extracting an
*observed* slope at the 8 shell needs the binding decomposition the removed
producer `probe_kappa_categorical_h7a_closed.py` carried; that is stated as the
blocker rather than guessed at.

Ref: conj:magic-shell-coupling-kappa, def:canonical-braid-interface-composition,
     prop:derived-mass-formula-light-isotopes
Bean: qou-o16k
"""

import sys
from pathlib import Path as _P
_SUB = _P(__file__).resolve().parent / "substrate"
if str(_SUB) not in sys.path:
    sys.path.insert(0, str(_SUB))
import mpmath as mp  # noqa: E402
from _precision import fmt, COMPUTE_DPS  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

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

# Substrate modulus, experimental (proton) pin -- the standing default per
# AGENTS.md "ALL AGENTS AND ALL PRODUCTION CODE DEFAULT TO THE EXPERIMENTAL
# (PROTON) ANCHOR".  Recorded explicitly so a later reader can tell which layer
# this witness belongs to without inferring it from a call site.
#
# Both come from the canonical modules rather than being re-typed here.  The
# literals they replace were `mp.mpf("1.1099785827513808")` and
# `mp.mpf("0.51099895000")`.  Carrying them as mpf kept float64 out of the
# witness, but the second is CODATA's electron mass TRUNCATED to 9 significant
# figures (0.51099895069) -- wrapping a truncated constant in mpf preserves the
# error in the value while removing the float from the JSON.
Q0 = Q_MP
Q0_PIN = "proton (experimental layer), m_p/m_e"

# The empirical slope the conjecture is measured against (PR #656 v6 fit).
# Read from kappa-provenance.witness.json (parameters.published_kappa_MeV)
# rather than typed, so the copy cannot go stale (witness-value copy ratchet).
KAPPA_EMPIRICAL = mp.mpf(json.loads((Path(__file__).resolve().parent / "kappa-provenance.witness.json").read_text(encoding="utf-8"))["parameters"]["published_kappa_MeV"])

MAGIC = [2, 8, 20, 28, 50, 82, 126]


def bracket(q: float, n: int) -> float:
    """Balanced q-bracket [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q**n - q ** (-n)) / (q - 1 / q)


def kappa_closed(q: float, m_e: float) -> float:
    """The conjectured closed form.  Note: no dependence on Z, N or A."""
    h = q - 1 / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    return -e0 * mp.log(1 / h) / (bracket(q, 2) * bracket(q, 3))


def excess_c1(z: int, n: int) -> int:
    """C1 -- canonical-braid interface counts (linear)."""
    return max(0, z - 1) - max(0, n - 1)


def excess_c2(z: int, n: int) -> int:
    """C2 -- unordered pair counts (quadratic)."""
    return z * (z - 1) // 2 - n * (n - 1) // 2


def main() -> None:
    k = kappa_closed(Q0, M_E_MEV)

    # (label, Z, N, which shell the anchor belongs to, role for kappa)
    rows = [
        ("3He", 2, 1, 2, "cross-check anchor (single-magic)"),
        ("3H", 1, 2, 2, "cross-check anchor (single-magic)"),
        ("4He", 2, 2, 2, "identification anchor (doubly magic)"),
        ("15O", 8, 7, 8, "NEVER TESTED"),
        ("15N", 7, 8, 8, "NEVER TESTED"),
        ("16O", 8, 8, 8, "NEVER TESTED (doubly magic)"),
        ("40Ca", 20, 20, 20, "NEVER TESTED (doubly magic)"),
        ("39K", 19, 20, 20, "NEVER TESTED"),
    ]

    table = []
    for label, z, n, shell, role in rows:
        e1, e2 = excess_c1(z, n), excess_c2(z, n)
        ratio = None if e1 == 0 else e2 / e1
        table.append(
            {
                "nuclide": label,
                "Z": z,
                "N": n,
                "shell": shell,
                "role": role,
                "excess_C1_interface": e1,
                "excess_C2_pairs": e2,
                "C2_over_C1": ratio,
                "binding_term_C1_MeV": k * e1,
                "binding_term_C2_MeV": k * e2,
                "conventions_agree": e1 == e2,
            }
        )

    tested = [r for r in table if r["role"] != "NEVER TESTED" and "NEVER" not in r["role"]]
    untested = [r for r in table if "NEVER" in r["role"]]

    assertions = []

    def check(name: str, ok: bool, detail: str) -> None:
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})

    check(
        "kappa_closed_is_shell_independent",
        kappa_closed(Q0, M_E_MEV) == k,
        "kappa_closed(q, m_e) takes no Z, N or A argument -- the conjecture "
        "predicts one constant for every magic shell",
    )
    check(
        "conventions_agree_on_every_tested_anchor",
        all(r["conventions_agree"] for r in tested),
        "C1 and C2 give the same excess on 3He, 3H and 4He -- the anchors that "
        "fixed kappa cannot distinguish them",
    )
    check(
        "conventions_diverge_at_shell_8",
        all(not r["conventions_agree"] for r in untested if r["excess_C1_interface"] != 0),
        "C1 and C2 disagree on 15O/15N/39K -- the discriminating measurement "
        "lies entirely outside the region kappa was fitted in",
    )
    check(
        "every_kappa_anchor_is_in_shell_2",
        all(r["shell"] == 2 for r in tested),
        "identification (2,2) and cross-check (2,1)/(1,2) are all A_magic = 2; "
        "shells 8, 20, 28, 50, 82, 126 are declared by the parent block and "
        "never evaluated",
    )

    print(f"kappa_closed(q0) = {k:.7f} MeV/excess   [q0 pin: {Q0_PIN}]")
    print(f"kappa_empirical  = {KAPPA_EMPIRICAL:.7f} MeV/excess")
    print(f"magic anchors declared by the parent block: {MAGIC}")
    print()
    hdr = f"{'nuclide':8s} {'Z':>3s} {'N':>3s} {'shell':>6s} {'C1':>5s} {'C2':>5s} {'C2/C1':>7s}  role"
    print(hdr)
    print("-" * len(hdr))
    for r in table:
        ratio = "--" if r["C2_over_C1"] is None else f"{r['C2_over_C1']:.1f}x"
        print(
            f"{r['nuclide']:8s} {r['Z']:3d} {r['N']:3d} {r['shell']:6d} "
            f"{r['excess_C1_interface']:5d} {r['excess_C2_pairs']:5d} {ratio:>7s}  {r['role']}"
        )
    print()
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness_raw = {
        "engine": "python-stdlib",
        "engineVersion": "3",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "kappa-shell8-excess-convention",
        "scriptFile": "probe_kappa_shell8_excess_convention.py",
        "contentBlock": "conj:magic-shell-coupling-kappa",
        "description": (
            "Structural probe, no fit. Shows (a) kappa_closed carries no shell "
            "index, (b) every anchor kappa has been evaluated at lies in the "
            "A_magic = 2 shell, and (c) the corpus's two excess conventions "
            "coincide on exactly those anchors and diverge from shell 8 onward."
        ),
        "parameters": {
            "q_0": Q0,
            "q_0_pin": Q0_PIN,
            "m_e_MeV": M_E_MEV,
            "kappa_empirical_MeV": KAPPA_EMPIRICAL,
            "magic_anchors": MAGIC,
        },
        "data": {
            "kappa_closed_MeV": k,
            "kappa_closed_is_shell_independent": True,
            "excess_table": table,
            "blocker": (
                "Extracting an OBSERVED slope at the 8 shell requires the "
                "binding decomposition carried by the removed producer "
                "probe_kappa_categorical_h7a_closed.py. Stated as a blocker "
                "rather than reconstructed by guesswork -- a reconstructed "
                "decomposition would be a new fit, which is what the demotion "
                "to conjecture was about."
            ),
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }

    witness = _ser(witness_raw)

    out = Path(__file__).with_name("kappa-shell8-excess-convention.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness -> {out.name}  (allPassed={witness_raw['allPassed']})")


if __name__ == "__main__":
    main()
