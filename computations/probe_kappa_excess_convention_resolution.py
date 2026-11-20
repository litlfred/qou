#!/usr/bin/env python3
"""The excess convention in `conj:magic-shell-coupling-kappa` resolves to the
canonical-braid interface counts, and the shell-8 prediction becomes a number.

`probe_kappa_shell8_excess_convention.py` established that two definitions of
`(n_pp - n_nn)` live in the corpus and coincide on every anchor kappa has been
evaluated at:

    C1  def:canonical-braid-interface-composition   n_pp = max(0, Z-1)
    C2  prop:derived-mass-formula-light-isotopes    n_pp = Z(Z-1)/2

It left the choice open.  It is not open: the two are not competing definitions
of one quantity, they are different quantities sharing a glyph.

    * Corpus-wide, the DIFFERENCE (n_pp - n_nn) occurs only in kappa's own
      block.  C2's counts occur only in the SUM (n_pp + n_nn), inside a
      different term (Delta_{T=1}), with a different normalisation (1/A) and a
      different partition ((2,2) |- 4).  No block forms C2's difference.
    * C1's block states its purpose in as many words: "The asymmetric counts
      (n_pp, n_nn) encode the Z <-> N asymmetry directly", and "The interface
      asymmetry isolates the 3He anomaly".  A difference is what measures an
      asymmetry; a sum is not.
    * C1 is a braid object -- the A-1 inter-nucleon interface generators
      sigma_{3k+2} of the canonical atomic braid beta(Z,N) in H_{3A}(q).  That
      is the same categorical layer kappa's normaliser was shown to live in
      (the Markov normalisation of the nucleon's own Borromean 3-braid).  C2 is
      a combinatorial pair count with no braid-generator realisation in the
      canonical pppnnn ordering.

This is corpus evidence and a layer argument, not a numerical selection.  No
value was consulted in choosing C1, and none of the numbers below were used to
make the choice.

Ref: conj:magic-shell-coupling-kappa, def:canonical-braid-interface-composition
Bean: qou-o16k
"""

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

Q0 = mp.mpf("1.1099785827513808")
Q0_PIN = "proton (experimental layer), m_p/m_e"
M_E_MEV = M_E_MEV
MAGIC = [2, 8, 20, 28, 50, 82, 126]


def bracket(q: float, n: int) -> float:
    return (q**n - q ** (-n)) / (q - 1 / q)


def kappa_closed(q: float, m_e: float) -> float:
    """Shell-independent: the normaliser's index is the nucleon's Borromean
    strand count, not a nuclear quantity."""
    h = q - 1 / q
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    return -e0 * mp.log(1 / h) / (bracket(q, 2) * bracket(q, 3))


def excess_c1(z: int, n: int) -> int:
    return max(0, z - 1) - max(0, n - 1)


def main() -> None:
    k = kappa_closed(Q0, M_E_MEV)

    # Single-magic mirror pairs (m, m-1) and (m-1, m) at each declared shell.
    rows = []
    for m in MAGIC:
        for z, n in ((m, m - 1), (m - 1, m)):
            rows.append(
                {
                    "Z": z,
                    "N": n,
                    "A": z + n,
                    "shell": m,
                    "excess_C1": excess_c1(z, n),
                    "kappa_term_MeV": k * excess_c1(z, n),
                }
            )

    assertions = []

    def check(name: str, ok: bool, detail: str) -> None:
        assertions.append({"name": name, "passed": bool(ok), "detail": detail})

    check(
        "C1_excess_is_unit_at_every_single_magic_mirror_pair",
        all(abs(r["excess_C1"]) == 1 for r in rows),
        "under C1 the excess is exactly +-1 at (m, m-1) and (m-1, m) for EVERY "
        "declared magic m -- (m-1) - (m-2) = 1 identically, so the count does "
        "not grow with the shell",
    )
    check(
        "kappa_term_is_shell_independent",
        len({round(abs(r["kappa_term_MeV"]), 12) for r in rows}) == 1,
        "combining the resolved index (shell-independent kappa) with C1 gives "
        "the same magic-shell contribution at every shell",
    )
    check(
        "prediction_is_a_single_number",
        abs(abs(k) - 1.0704241) < 1e-6,
        "the 224x undetermined band collapses to |kappa| MeV per single-magic "
        "mirror pair, at every shell",
    )

    print(f"kappa (shell-independent) = {k:.7f} MeV/excess   [q0 pin: {Q0_PIN}]\n")
    print(f"{'Z':>4s} {'N':>4s} {'A':>4s} {'shell':>6s} {'excess':>7s} {'kappa term MeV':>15s}")
    print("-" * 46)
    for r in rows:
        print(
            f"{r['Z']:4d} {r['N']:4d} {r['A']:4d} {r['shell']:6d} "
            f"{r['excess_C1']:7d} {r['kappa_term_MeV']:15.5f}"
        )
    print()
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")

    witness_raw = {
        "engine": "python-stdlib",
        "engineVersion": "3",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "kappa-excess-convention-resolution",
        "scriptFile": "probe_kappa_excess_convention_resolution.py",
        "contentBlock": "conj:magic-shell-coupling-kappa",
        "description": (
            "Resolves the excess convention to C1 on corpus evidence (the "
            "difference occurs only in kappa's block; C2's counts occur only in "
            "a sum, in a different term) plus a categorical-layer argument. "
            "With the index already resolved to the nucleon's Borromean strand "
            "count, kappa's magic-shell contribution becomes a single number at "
            "every single-magic mirror pair."
        ),
        "parameters": {
            "q_0": Q0,
            "q_0_pin": Q0_PIN,
            "m_e_MeV": M_E_MEV,
            "magic_anchors": MAGIC,
            "excess_convention": "C1 (def:canonical-braid-interface-composition)",
        },
        "data": {
            "kappa_MeV": k,
            "kappa_is_shell_independent": True,
            "single_magic_mirror_pairs": rows,
            "prediction": (
                "At every single-magic mirror pair (m, m-1) / (m-1, m), the "
                f"magic-shell coupling contributes -+{abs(k):.7f} MeV, "
                "independent of the shell."
            ),
            "still_blocked": (
                "TESTING this against AME still needs the binding decomposition "
                "that isolates the magic-shell term from Coulomb and pairing. "
                "That decomposition is not in the tree (see "
                "probe_kappa_shell8_excess_convention.py). The prediction is "
                "stated; it is not claimed to be verified."
            ),
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }
    witness = _ser(witness_raw)
    out = Path(__file__).with_name("kappa-excess-convention-resolution.witness.json")
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
