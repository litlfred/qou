#!/usr/bin/env python3
"""|tr_M| for the nucleons, read from the witness built at THIS RUN'S pin.

WHY THIS EXISTS.  Fifteen files hardcoded `mp.mpf("1.0653062286131670…")` as
the proton's Markov trace. That number is **convention C** — proved to 50
digits by `audits/he4_witness_convention_attribution_probe.py` — and convention
D has been canonical since the owner ruling of 2026-08-15. The D value is
`1.14575969245730086968…` at the proton pin, so every one of those sites was
**7.55 %** out.

Seven of them were not comparing against it, they were multiplying by it:

    pred_0 = tr_M * plancherel_ratio * vol_over_hsq      # habiro_h9_*
    S      = hab_sum / pred_0                            # => 7.552 % high

WHY NOT JUST SUBSTITUTE THE D LITERAL.  Because that is how the corpus got
here. A hardcoded D constant is stale the moment the anchor or the convention
moves again, and it carries no way for a reader to tell which frame it is in.
Worse, the previous migration could not have caught it: `.work/convention-c-regen*.jsonl`
logs `markov_weights_symbolic.py` as **`ok`, 5.2 s** and its C constant is
still there today, because re-running a producer cannot change a literal. A
regeneration sweep is the wrong instrument for this class and reports success
against it.

So: read the value, at the pin the caller is actually running at.

TWO PINS, SELECTED BY THE ARTIFACT'S OWN STAMP.  `atomic-tr-m-mpfr-50dps.witness.json`
is muon-built and `…-proton.witness.json` is proton-built; this picks whichever
records the q₀ that `q_parameter` resolves for the *running producer's stem*,
and raises if neither does. Same shape as the fixes in
`y_lambda_symbolic_validate.load_mpfr_witness` and
`atomic_tr_m_helium4._pick_witness_for_pin` (bean qou-y313) — reconciling
against the recorded stamp rather than trusting a filename.

STRAND COUNT IS NOT A PARAMETER, AND THAT IS NOT AN OVERSIGHT.  The Markov
trace is invariant under stabilisation, so tr_M of the proton braid is the same
computed in H₃ or H₉. The habiro/ callers say "H₉" and the witness rows are
built at 3A strands; both are the same number, and a caller does not need to
say which.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

import mpmath as mp                                        # noqa: E402

# Guarantee our own precision rather than inheriting it. (Copilot, PR #6116.)
#
# The reference is a 50-dps decimal string; parsing it at mpmath's default
# dps=15 would silently round it before a caller serialises it back into a
# witness, defeating the point of a 50-dps reference.
#
# Measured: this did NOT bite — dps was 70 by the time a caller reached us.
# But it was 70 by ACCIDENT, set as a side-effect somewhere in the import
# chain (`mp.dps` is 15 before importing `markov_weights_symbolic` and 70
# after). A guarantee that depends on who imported you first is not a
# guarantee; re-ordering an unrelated import would silently truncate every
# value this module returns. So state the requirement here, where the
# obligation actually lives.
if mp.mp.dps < 60:
    mp.mp.dps = 60

#: Proton-built first only as a hint; the recorded q₀ decides.
_WITNESSES = ("atomic-tr-m-mpfr-50dps-proton.witness.json",
              "atomic-tr-m-mpfr-50dps.witness.json")

_CACHE: dict[str, mp.mpf] = {}


#: The canonical intra-nucleon ordering, per the 2026-09-05 owner ruling
#: (bean `qou-hu1f`). Read from `atom_braid_word_3A`'s own default rather than
#: written out, so a future ruling that moves the default moves this check with
#: it — a hardcoded frame name here would be the same defect one level up.
def _canonical_ordering() -> str:
    from mass_at_3A_proper import atom_braid_word_3A      # noqa: PLC0415
    import inspect                                        # noqa: PLC0415
    return inspect.signature(atom_braid_word_3A).parameters["intra_order"].default


def _require_canonical_ordering(name: str, w: dict, d: dict) -> None:
    """Refuse a witness in the wrong intra-nucleon ordering, or in none.

    WHY THIS EXISTS (bean `qou-y4gi`). Until 2026-09-13 this module validated
    the PIN and nothing else, and its docstring promised callers it "cannot
    silently serve the wrong frame". It could, and it did: it served the
    grouped-era contents of `atomic-tr-m-mpfr-50dps-proton.witness.json`
    (2026-08-19) for five weeks after the ruling that superseded them, with no
    complaint, because that file is at the right *pin*. Pin and ordering are
    two axes that can differ silently; this is the pin guard applied to the
    second one.

    AN UNDECLARED FRAME RAISES. It does NOT default to canonical, and that is
    the load-bearing choice: EVERY pre-ruling witness is undeclared, so a
    permissive default would wave through precisely the population this exists
    to catch — and would have waved through the exact file that motivated it.
    The cost is that a stale witness now stops a caller instead of quietly
    misinforming it, which is the same trade the pin guard already makes and
    justifies two functions down.
    """
    frame = w.get("intra_ordering_frame") or d.get("intra_ordering_frame")
    want = _canonical_ordering()
    if frame == want:
        return
    if frame is None:
        raise ValueError(
            f"{name} declares no `intra_ordering_frame`, so which "
            f"intra-nucleon word produced it is unknown. Every witness "
            f"predating the 2026-09-05 ordering ruling (bean qou-hu1f) is "
            f"undeclared, and this guard deliberately does NOT assume "
            f"canonical for them — that assumption is what let this module "
            f"serve grouped-era values for five weeks. Regenerate with "
            f"`QOU_Q0_ANCHOR=<anchor> python3 "
            f"computations/atomic_tr_m_mpfr_50dps.py --anchor <anchor>`, "
            f"which stamps the field from the word builder's own default."
        )
    raise ValueError(
        f"{name} was produced in the {frame!r} intra-nucleon ordering, but "
        f"{want!r} is canonical (bean qou-hu1f). These are different elements "
        f"of H_3(q) and their |tr_M| differ by ~82% at the proton, so this is "
        f"not a tolerance question. Regenerate the witness."
    )


def _rows_for_pin() -> dict[str, dict]:
    from q_parameter import Q_50_DIGIT_STR                  # noqa: PLC0415
    want = mp.mpf(Q_50_DIGIT_STR)
    seen = []
    # In computations/, the witnesses sit beside this file (_HERE); in the
    # vendored layout (qou_mass/_internal/), they sit one directory up in
    # qou_mass/ (_HERE.parent). Search both (bean qou-72f8).
    search_dirs = (_HERE, _HERE.parent)
    for name in _WITNESSES:
        p = next((d / name for d in search_dirs if (d / name).exists()), None)
        if p is None:
            continue
        d = json.loads(p.read_text())
        w = d.get("witness", d)
        q_rec = ((w.get("parameters") or {}).get("q_0") or w.get("q_0")
                 or d.get("q_0_50dps") or w.get("q_0_50dps"))
        seen.append((name, str(q_rec)[:26]))
        if q_rec is not None and abs(mp.mpf(str(q_rec)) - want) < mp.mpf("1e-40"):
            _require_canonical_ordering(name, w, d)
            return {r["atom"]: r
                    for r in (w.get("results") or d.get("results") or [])}
    raise FileNotFoundError(
        f"no |tr_M| witness recorded at this run's pin "
        f"{str(Q_50_DIGIT_STR)[:26]}…; inspected {seen}. Regenerate "
        f"atomic_tr_m_mpfr_50dps.py at this anchor rather than reading the "
        f"other layer — a silent cross-layer read is the defect this avoids."
    )


def tr_m_nucleon(atom: str) -> mp.mpf:
    """|tr_M(atom)| at the running producer's pin, convention D.

    `atom` is `"proton"` or `"neutron"`. Raises rather than falling back to the
    other pin: a 78 ppb cross-layer error that reads as a successful load is
    worse than a stack trace.
    """
    if atom not in _CACHE:
        rows = _rows_for_pin()
        if atom not in rows:
            raise KeyError(f"{atom!r} not in the |tr_M| witness; have "
                           f"{sorted(rows)}")
        _CACHE[atom] = abs(mp.mpf(rows[atom]["tr_M_at_q0_50dps"]))
    return _CACHE[atom]


def tr_m_proton() -> mp.mpf:
    """Convenience alias — the value 15 files used to hardcode."""
    return tr_m_nucleon("proton")


def tr_m_neutron() -> mp.mpf:
    return tr_m_nucleon("neutron")


def _self_test() -> int:
    """The ordering guard must FIRE, not merely exist (bean qou-y4gi).

    A guard nobody has watched reject is indistinguishable from a no-op, and
    this module shipped for five weeks with a docstring promising a protection
    it did not provide. Three cases: canonical passes, a wrong frame raises, an
    ABSENT frame raises. The third is the one that matters — it is the state
    every pre-ruling witness is in.
    """
    want = _canonical_ordering()
    cases = [
        ("canonical passes", {"intra_ordering_frame": want}, None),
        ("wrong frame raises", {"intra_ordering_frame": "grouped"}, "grouped"),
        ("absent frame raises", {}, "declares no"),
    ]
    fails = []
    for label, doc, expect in cases:
        try:
            _require_canonical_ordering("<fixture>", doc, {})
            got = None
        except ValueError as e:
            got = str(e)
        if expect is None:
            ok = got is None
        else:
            ok = got is not None and expect in got
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
        if not ok:
            fails.append(label)
    # And the live witnesses must actually load, or the guard is too strict.
    try:
        for a in ("proton", "neutron"):
            tr_m_nucleon(a)
        print("  [PASS] the committed witnesses load under the guard")
    except Exception as e:
        print(f"  [FAIL] committed witnesses rejected: {str(e)[:120]}")
        fails.append("live load")
    print(f"  self-test: {'PASS' if not fails else 'FAIL ' + ', '.join(fails)} "
          f"(1 must-pass, 2 must-raise, 1 live load)")
    return 1 if fails else 0


if __name__ == "__main__":
    mp.mp.dps = 50
    if "--self-test" in sys.argv:
        raise SystemExit(_self_test())
    for a in ("proton", "neutron"):
        print(f"  {a:8} {tr_m_nucleon(a)}")
