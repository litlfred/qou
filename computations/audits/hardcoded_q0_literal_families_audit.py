#!/usr/bin/env python3
"""Hardcoded muon-q0 literals: at least four mutually inconsistent families.

Bean `qou-o922` (the muon-pin register drain), bean `qou-bred` (A-vs-C),
successor to `docs/audits/2026-08-19-codata-edition-straddle-corpus-sweep.md`.

WHAT PROMPTED IT
----------------
Draining the undeclared-muon-pin risk register, 19 of its 40 members turned out
to HARDCODE q0 as a string literal rather than resolve it. That makes the
register's premise wrong for them: it flags producers that would "resolve
PROTON on re-run", and a producer whose q0 is a literal never resolves at all.

Checking those literals against the canonical pin then produced a larger
finding, which is what this audit records.

THE FINDING
-----------
The corpus does not carry one hardcoded muon q0. It carries several, and they
disagree with each other AND with the canonical pin. Grouping every literal of
the form `1.10997859555...` by the character at which it first diverges from
`_q0_value_for_anchor("muon")`:

  * a large family diverging at char 13 -- the `...5541805...` value, i.e. the
    CODATA-stale-edition derivation (`Vol(4_1)/206.7682830`). Several match it
    to 33-51 chars, so these are transcriptions of a value the corpus has since
    superseded;
  * literals diverging at chars 18 and 19 -- A-family, but wrong from the 18th
    digit on. Neither the canonical pin nor the stale one;
  * literals diverging at chars 50 and 52 -- deep-tail divergence, consistent
    with rounding at transcription;
  * clean truncated prefixes of the canonical pin, at lengths from 14 to 70 --
    correct but at wildly varying precision.

Only the last group is defensible, and even there a 14-character transcription
of a 70-character constant is a precision decision nobody recorded.

WHY IT MATTERS, AND WHY IT IS NOT JUST TIDINESS
------------------------------------------------
This is the same lesson the CODATA edition sweep drew -- "read the authority,
do not transcribe it" -- one layer down. That sweep fixed the CONSTANTS
registry to read the NIST table. These sites transcribe the *derived substrate
pin*, so they are immune to that fix: `qou_substrate.constants` can be perfectly
correct and a probe carrying `Q0 = "1.1099785955541810"` still computes at a
superseded value.

A transcribed constant also defeats the anchor machinery entirely. Such a
producer cannot be re-pinned, cannot be flipped by `QOU_Q0_ANCHOR`, and reports
a `q0Anchor` that describes the label rather than the computation.

SCOPE
-----
Scope-(a) MEASUREMENT. It classifies literals; it changes none of them, wires
nothing, and asserts nothing about which value any given producer SHOULD use --
that turns on the A-vs-C question, which is an owner ruling (bean `qou-bred`).
Ratcheted so the count cannot grow silently.

Usage:
    python3 computations/audits/hardcoded_q0_literal_families_audit.py
    python3 ... --strict       # exit 1 if the divergent count grows
    python3 ... --self-test    # prove the ratchet fires; writes nothing

Output:
    computations/audits/hardcoded-q0-literal-families.witness.json
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder, _q0_value_for_anchor  # noqa: E402

_T0 = time.monotonic()

#: Ratchet on literals that DIVERGE from the canonical pin (not mere
#: truncations). Drains as sites are migrated to read the pin; must never grow.
BASELINE_DIVERGENT = 71


def ratchet_fires(count: int, baseline: int) -> bool:
    """The ratchet's ONE predicate. ``main()`` and ``_self_test()`` must both
    call this -- that shared call is the whole point.

    Previously each spelled the comparison out separately, and the self-test
    spelled it against literals: ``fires = n > (n - 1)``, ``holds = not (n > n)``.
    Both are tautologies for every ``int``, so ``--self-test`` returned 0
    unconditionally and could not report failure. It printed the numbers while
    never touching the predicate it claimed to test; flipping ``>`` to ``>=``
    in ``main()`` would not have moved it.

    Routed through here, a flipped operator is caught: ``>=`` breaks the
    ``holds`` leg (``not (n >= n)`` is False) and ``<`` breaks the ``fires``
    leg. The test can now fail, which is the only property that made it worth
    having.
    """
    return count > baseline

#: Only literals long enough to be a deliberate transcription rather than a
#: display rounding. 14 chars still discriminates muon from proton.
_MIN_LEN = 14
_LITERAL = re.compile(r'["\'](1\.10997859555[0-9]{1,})["\']')

_SCAN_ROOT = HERE.parent


def _acceptable(lit: str, canon: str) -> bool:
    """Is `lit` the canonical pin, truncated or correctly rounded to its length?

    Truncation and round-half-up at the literal's own precision are both
    faithful transcriptions. Only a value that is neither is a finding.
    Implemented on the digit string with `decimal`, so no float64 anywhere.
    """
    if canon.startswith(lit):
        return True
    from decimal import Decimal, ROUND_HALF_UP, getcontext
    n_sig = len(lit.replace(".", "").lstrip("0"))
    if n_sig < 1 or n_sig > len(canon):
        return False
    getcontext().prec = len(canon) + 10
    try:
        rounded = Decimal(canon).quantize(
            Decimal(1).scaleb(-(len(lit) - lit.index(".") - 1)),
            rounding=ROUND_HALF_UP)
    except Exception:  # noqa: BLE001
        return False
    return str(rounded) == lit


def scan() -> dict:
    canon = _q0_value_for_anchor("muon") or ""
    if not canon:
        raise RuntimeError("cannot load the canonical muon pin to compare against")

    families: dict[int | None, list] = defaultdict(list)
    for p in sorted(_SCAN_ROOT.rglob("*.py")):
        rel = p.relative_to(_SCAN_ROOT)
        if "worktrees" in rel.parts or "_deprecated" in rel.parts:
            continue
        try:
            src = p.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        for lit in set(_LITERAL.findall(src)):
            if len(lit) < _MIN_LEN:
                continue
            # A literal is ACCEPTABLE if it is the canonical pin either
            # truncated or correctly ROUNDED to its own length. Rounding is
            # not an error and must not be reported as one: 75 sites carry
            # `…878015…` rendered at 51 figures as `…87802`, which is right.
            # Classifying that as divergence would have reported the corpus's
            # single largest correctly-transcribed family as defective.
            at = None if _acceptable(lit, canon) else next(
                (k for k in range(min(len(lit), len(canon)))
                 if lit[k] != canon[k]), None)
            if at is None and not _acceptable(lit, canon):
                at = min(len(lit), len(canon))  # differs only by being longer
            families[at].append({"file": str(p.relative_to(HERE.parents[1])),
                                 "literal": lit, "length": len(lit)})
    return {"canonical": canon, "families": families}


def _self_test() -> int:
    """Prove the ratchet fires WITHOUT writing a witness.

    Deliberately does not call main(): main() saves, and a self-test whose
    side effect is writing its own forced-failure output into the committed
    artifact is the defect this pattern exists to avoid (see the sibling
    undeclared_muon_pin_flip_risk_audit, where exactly that happened).
    """
    fams = scan()["families"]
    n = sum(len(v) for k, v in fams.items() if k is not None)
    fires = ratchet_fires(n, n - 1)   # the REAL predicate, at baseline n-1
    holds = not ratchet_fires(n, n)   # and at baseline n
    print(f"self-test: {n} divergent literals")
    print(f"  ratchet FIRES at baseline {n - 1}: {fires}  (expect True)")
    print(f"  ratchet HOLDS at baseline {n}:     {holds}  (expect True)")
    agree = "" if BASELINE_DIVERGENT == n else f"  <-- DISAGREES with live {n}"
    print(f"  BASELINE_DIVERGENT in source: {BASELINE_DIVERGENT}{agree}")
    print("  no witness written")
    return 0 if (fires and holds) else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if the divergent-literal count exceeds the baseline")
    ap.add_argument("--self-test", action="store_true",
                    help="prove the ratchet fires; writes nothing")
    args = ap.parse_args(argv)
    if args.self_test:
        return _self_test()

    r = scan()
    canon, fams = r["canonical"], r["families"]
    clean = fams.get(None, [])
    divergent = {k: v for k, v in fams.items() if k is not None}
    n_div = sum(len(v) for v in divergent.values())

    print("=" * 76)
    print("Hardcoded muon-q0 literals, grouped by first divergence from the pin")
    print("=" * 76)
    print(f"  canonical pin ({len(canon)} chars): {canon[:52]}…\n")
    print(f"  clean prefixes (correct, truncated) : {len(clean)}")
    if clean:
        lens = sorted(x["length"] for x in clean)
        print(f"      lengths {lens[0]}..{lens[-1]}  <- precision varies "
              f"{lens[-1] - lens[0]} chars across sites")
    print(f"  DIVERGENT literals                  : {n_div}"
          f"   (baseline {BASELINE_DIVERGENT})")
    for at in sorted(divergent):
        grp = divergent[at]
        print(f"\n    diverges at char {at}  ({len(grp)} site(s))")
        print(f"      canonical: …{canon[at:at + 12]}")
        for e in grp[:6]:
            print(f"      lit …{e['literal'][at:at + 12]}  [{e['length']}]  {e['file']}")
        if len(grp) > 6:
            print(f"      … and {len(grp) - 6} more")

    grew = ratchet_fires(n_div, BASELINE_DIVERGENT)
    assertions = [
        {"name": "1_divergent_set_has_not_grown", "passed": not grew,
         "detail": f"{n_div} divergent literals vs baseline {BASELINE_DIVERGENT}. "
                   "Growth means a new site transcribed a q0 that disagrees with "
                   "the canonical pin."},
        {"name": "2_more_than_one_family_exists", "passed": len(divergent) > 1,
         "detail": f"{len(divergent)} distinct divergence points "
                   f"({sorted(divergent)}). More than one means the corpus "
                   "carries mutually inconsistent hardcoded pins, not a single "
                   "stale value -- which is the finding."},
    ]
    all_passed = all(a["passed"] for a in assertions)

    payload = {
        "computation_method": (
            "Regex-scans computations/**/*.py (excluding _deprecated and agent "
            "worktrees) for string literals matching 1.10997859555…, and groups "
            "them by the first character index at which they disagree with "
            "_q0_value_for_anchor('muon'). Pure string comparison; no float64, "
            "no arithmetic."),
        "description": (
            "The corpus carries several mutually inconsistent HARDCODED muon-q0 "
            "literals, not one. Grouped by first divergence from the canonical "
            "pin they fall into distinct families -- including a large one that "
            "transcribes the CODATA-stale-edition derivation, and others wrong "
            "from the 18th-19th digit. Clean truncated prefixes also vary in "
            "precision from 14 to 70 characters. Found while draining the "
            "undeclared-muon-pin register, where 19 of 40 members turned out to "
            "hardcode q0 and so were never at risk of the flip the register "
            "detects."),
        "audit_only": True,
        "tier": "empirical",
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no substrate value as an input. It loads the canonical muon "
            "pin as a reference STRING and compares other strings against it "
            "character-wise, computing nothing from any of them."),
        "scope": (
            "scope-(a) MEASUREMENT. Classifies literals; changes none, wires "
            "nothing, and asserts nothing about which value a given producer "
            "SHOULD use -- that turns on A-vs-C, an owner ruling (bean "
            "qou-bred)."),
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "canonical_pin": canon,
            "clean_prefix_count": len(clean),
            "clean_prefix_lengths": sorted(x["length"] for x in clean),
            "divergent_count": n_div,
            "baseline_divergent": BASELINE_DIVERGENT,
            "families": {str(k): v for k, v in sorted(divergent.items())},
            "caveat_not_split_source_vs_doc": (
                "This count is SITES, not defects. It has NOT been split into "
                "code that computes with the literal versus documentation, "
                "docstrings, test fixtures and audits that quote it on purpose "
                "-- this audit's own file and muon_pin_three_values_probe are "
                "both in the char-13 group precisely because they DOCUMENT the "
                "stale value. The predecessor CODATA sweep made exactly this "
                "mistake and had to correct itself: its 'code that computes a "
                "wrong number' bullet was 'wrong for 87 % of its own count'. "
                "Do not quote 65 as a defect count. The split is the next step."),
            "verdict": (
                "Transcribed pins defeat the anchor machinery: such a producer "
                "cannot be re-pinned, cannot be flipped by QOU_Q0_ANCHOR, and "
                "reports a q0Anchor describing its label rather than its "
                "computation. This is the CODATA sweep's 'read the authority, "
                "do not transcribe it' one layer down -- that sweep fixed the "
                "CONSTANTS registry, and these sites transcribe the DERIVED "
                "substrate pin, so they are immune to it."),
        },
        "context": {
            "beans": ["qou-o922", "qou-bred"],
            "predecessor": "docs/audits/2026-08-19-codata-edition-straddle-corpus-sweep.md",
            "register_premise_defect": (
                "19 of the 40 undeclared-muon-pin register members hardcode q0, "
                "so the register's premise -- 'would resolve PROTON on re-run' "
                "-- does not hold for them. They are not at risk of that flip."),
        },
    }
    b = WitnessBuilder.wrap_legacy(
        "hardcoded-q0-literal-families", payload, script_path=__file__,
        engine="python", output_dir=HERE, start_time=_T0)
    out = b.save()
    print(f"\nwitness -> {out}")
    if args.strict and grew:
        print(f"STRICT: divergent set grew {BASELINE_DIVERGENT} -> {n_div}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
