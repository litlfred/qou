#!/usr/bin/env python3
"""qbeta_habiro_citation_and_termination_probe.py — the `habiro_integral`
docstring cited evidence that does not say what it claimed, four ways.

Bean `qou-cds1`.  Scope-(b): each discrepancy is a checkable fact about a
committed file, not a modelling judgement.

## What the docstring said

`QOU.BraidKnot.habiro_integral` in `habiro-precision-ladder-equivalence.lean`
closed with:

    (Verified computationally for proton (M=8), neutron (M=8), deuteron
     (M=12), 3He (M=16), 4He (M=20) —
     habiro-expansion-atomic-probe.witness.json, all_integral: true.)

## Four discrepancies, each measured

1. **The named field is in a DIFFERENT file.**  `all_integral` does not occur
   anywhere in `habiro-expansion-atomic-probe.witness.json`.  It occurs in
   `habiro-coefficients-atomic.witness.json`.  The cited probe's corresponding
   assertion is named `all_a_m_have_integer_coefficients`.

2. **The deuteron M is wrong.**  Its expansion terminates at **M = 13**, not 12.

3. **4He is not in the corpus at all.**  No `4He` / `helium-4` / `A=4` entry
   exists in the atomic witness.  The list named an atom for which no
   expansion exists.

4. **Tritium IS, and was omitted.**  `T (tritium, A=3)` is present with M = 16.

Points 3 and 4 are the pair worth noticing: the citation both invented an atom
and dropped a real one, so its *count* of five looked right.

## What the evidence actually supports — which is MORE than was claimed

The cited probe (`cor:habiro-expansion-atomic`, 3/3) asserts three things, not
one: integrality, the degree bound `deg_u a_m <= m`, and **termination within
`m_max <= ceil(sqrt(2 * deg_u p(u)))`**.  That last is a derived structural
bound on where the expansion stops, and re-measured here against the live
witness it holds for all five atoms:

    atom          M    deg_u p    ceil(sqrt(2 deg_u p))
    proton         8      44             10
    neutron        8      36              9
    deuteron      13     100             15
    tritium       16     136             17
    3He           16     144             17

Recording it because a session hunting for "what fixes the termination degree"
can otherwise re-derive it from the five M values by pattern-matching — which
is how this probe started, before the corpus-grep found the bound already
proved.

## Precision

Exact integer arithmetic (`math.isqrt`-free `math.ceil(math.sqrt(...))` is
avoided; the bound is computed with `math.isqrt` on exact integers).  No
float64 in any claim: no `float(` outside display, no `statistics`.
"""
from __future__ import annotations

import json
import math
import pathlib as _pl
import re
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

from witness_base import WitnessBuilder                         # noqa: E402

RESULTS: list[dict] = []


def record(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


ATOMIC = _COMP / "habiro" / "habiro-coefficients-atomic.witness.json"
PROBE = _COMP / "probes" / "habiro-expansion-atomic-probe.witness.json"
A = json.load(open(ATOMIC))
P = json.load(open(PROBE))
A_TXT, P_TXT = json.dumps(A), json.dumps(P)


def ceil_sqrt(n: int) -> int:
    """ceil(sqrt(n)) by exact integer arithmetic — no float rounding."""
    r = math.isqrt(n)
    return r if r * r == n else r + 1


rows = {}
for k, d in A["results"].items():
    M = max(c["m"] for c in d["habiro_coefficients"])
    rows[k] = {"M": M, "deg_p_u": d["deg_p_u"], "bound": ceil_sqrt(2 * d["deg_p_u"])}

record(
    "cited_witness_does_not_contain_the_named_field",
    ("all_integral" not in P_TXT) and ("all_integral" in A_TXT),
    "`all_integral` occurs 0 times in habiro-expansion-atomic-probe.witness.json "
    "(the file the docstring cites) and does occur in "
    "habiro-coefficients-atomic.witness.json. The cited probe's assertions are "
    + ", ".join(a["name"] for a in P.get("assertions", []))
    + " — the integrality one is `all_a_m_have_integer_coefficients`.",
)

deut = rows["D (deuteron, A=2)"]["M"]
record(
    "deuteron_M_is_13_not_12",
    deut == 13,
    f"the deuteron's Habiro expansion terminates at M = {deut}; the docstring "
    f"said 12.",
)

record(
    "helium4_is_absent_and_tritium_was_omitted",
    not re.search(r"4\s*He|helium-4|A=4", A_TXT) and any("tritium" in k for k in rows),
    "no 4He / helium-4 / A=4 entry exists anywhere in the atomic witness, so "
    "the docstring named an atom for which no expansion exists; meanwhile "
    "`T (tritium, A=3)` IS present (M=16) and was omitted. The citation both "
    "invented an atom and dropped a real one, which is why its count of five "
    "looked right. Atoms actually present: " + ", ".join(rows),
)

record(
    "termination_bound_holds_on_the_live_witness",
    all(r["M"] <= r["bound"] for r in rows.values()),
    "m_max <= ceil(sqrt(2 * deg_u p)) for all five atoms: "
    + "; ".join(f"{k.split(' ')[0]} M={r['M']}<= {r['bound']}" for k, r in rows.items())
    + ". This is the cited probe's own Claim 3, re-measured against the current "
    "witness contents (which have moved since: tritium added, deuteron M 12->13). "
    "It is the derived structural answer to 'what fixes the termination degree' "
    "— found by corpus-grep, not by pattern-matching the five M values.",
)

out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "does habiro_integral's docstring cite evidence that says what it claims?",
    "answer": "No — four discrepancies: the named field is in a different file, "
              "the deuteron M is 13 not 12, 4He does not exist in the corpus, and "
              "tritium was omitted. The real evidence supports MORE than was "
              "claimed: integrality, a degree bound, and a termination bound.",
    "scope": "(b) — checkable facts about committed files.",
    "atoms": rows,
    "cited_witness_assertions": [a["name"] for a in P.get("assertions", [])],
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
wpath = _HERE.parent / "qbeta-habiro-citation-and-termination.witness.json"
wpath.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wpath}")
print(f"allPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
