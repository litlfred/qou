#!/usr/bin/env python3
"""Cross-block epistemic-status checker: does one block call X *derived* while
another calls X *assumed*?

Bean `qou-vud6`. Every status-bearing checker in this repo is PER-BLOCK — the
`.qa.json` sidecar model scores a block against its own source hashes. Nothing
compares blocks. Two failures got through because of that:

  #5044  `interactions-are-pairwise-intro`  "forced by the braiding rather than assumed"
         `…-decomposition-proof`            "Part 1 is the hexagon axiom, solved for"
         Three blocks apart, one section, written in one sitting. Contradictory.

  #5047  `braiding-eigenvalue-extraction-novelty`  q "precisely and completely
                                                   constrained by the braiding"
         `epistemic-status-of-calibrations`        "We defined q_0 to enforce it."
         Different chapters. Contradictory, on the three-calibration claim.

Note the two have different topologies: the first is intra-section, the second is
cross-chapter with no `uses[]` edge between them. A graph walk would have missed
the second. So this checker keys on TERMS, not on the dependency graph.

## How it works

1. Build an ASSUMED-TERM TABLE from the corpus itself — terms the corpus declares
   to be calibrations, axioms, conjectures, or definitions. Sources: blocks of
   kind `definition`/`conjecture`; prose declaring a calibration ("CAL-1/2/3",
   "calibration input", "we defined X to enforce"); Lean `axiom`/`class` names;
   and Mathlib class fields for structures the paper builds on.
2. Scan every block's prose for CONTRASTIVE DERIVATION CLAIMS ("not imposed",
   "rather than assumed", "forced by", "completely constrained").
3. Flag a claim whose subject matches an assumed term.

## It proposes; it does not decide

High-recall, agent-confirmed — the same posture as the Lean vacuity classes. A
claim can legitimately be contrastive about the *role* of a term while its
*value* is calibrated (that is exactly the fibre/archimedean split), so the
verdict needs a reader. Findings go in the review ledger, not a hard gate.

Usage:
  python3 -u docs/audits/scripts/epistemic_status_crosscheck.py
  python3 -u docs/audits/scripts/epistemic_status_crosscheck.py --json
"""
from __future__ import annotations

import json
import os
import re
import sys
from glob import glob
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CONTENT = REPO / "content/quantum-observable-universe"
OUT = Path(__file__).with_suffix(".witness.json")

CONTRASTIVE = re.compile(
    r"(?:not\s+(?:assumed|imposed|postulated|stipulated|imported)"
    r"|rather\s+than\s+(?:assumed|imposed|postulated|stipulated)"
    r"|forced\s+by"
    r"|completely\s+constrained"
    r"|already\s+determined\s+by)",
    re.I,
)

# Terms whose assumed-status the corpus itself declares, with the phrase that
# establishes it. Seeded from measured corpus statements, not from belief.
ASSUMED_SEEDS = {
    r"\bq_?0\b|\bq₀\b|substrate parameter|deformation parameter": (
        "q0 is CAL-2, a calibration input: "
        "'We defined q_0 to enforce it' (epistemic-status-of-calibrations)"
    ),
    r"hexagon": (
        "hexagon_forward / hexagon_reverse are class FIELDS of Mathlib's "
        "BraidedCategory — axioms of the structure"
    ),
    r"\bbraiding\b": (
        "the braiding is assumed data: def:quantum-universe tuple item 1 is a "
        "braided monoidal category"
    ),
    r"\bm_e\b|electron mass": "m_e is CAL-1, a calibration input",
    r"\bm_\\pi\b|pion (?:mass|decay width)": "m_pi / D_pi is CAL-3, a calibration input",
}


def sentences(text: str):
    for para in text.split("\n\n"):
        flat = " ".join(para.split())
        for s in re.split(r"(?<=[.!?])\s+", flat):
            if s.strip():
                yield s.strip()


def corpus_assumed_labels() -> dict[str, str]:
    out = {}
    for ts in glob(str(CONTENT / "*/*.ts")):
        try:
            src = open(ts).read()
        except Exception:
            continue
        m = re.search(r'label:\s*"([^"]+)"', src)
        if not m:
            continue
        if re.search(r"\bconjecture\(\{", src):
            out[m.group(1)] = "conjecture (open by declaration)"
        elif re.search(r"\bdefinition\(\{", src):
            out[m.group(1)] = "definition (names a construction; proves nothing)"
    return out


# The three sentences this checker exists to catch, as they read BEFORE they
# were fixed. A checker that no longer flags anything because the corpus was
# repaired proves nothing; these keep it honest.
REGRESSION_FIXTURES = [
    (
        "#5044 interactions-are-pairwise-intro",
        "The answer is the second, and it is forced by the braiding rather than "
        "assumed.",
    ),
    (
        "#5047 braiding-eigenvalue-extraction-novelty (para 1)",
        "The deformation parameter $q$ is not imposed externally.",
    ),
    (
        "#5047 braiding-eigenvalue-extraction-novelty (para 2)",
        "the mathematical novelty here is treating this extraction not as a "
        "definition of $q$, but as a rigorous proof that the macroscopic "
        "substrate parameter governing the fluid PDE is precisely and "
        "completely constrained by the microscopic categorical braiding of the "
        "observable universe.",
    ),
    (
        "#5047 tannaka-krein-overview",
        "The deformation parameter $q$ is not imposed. When the braiding "
        "$c_{V,V}$ is non-symmetric, $q$ is the eigenvalue of $c_{V,V}$ on $S^2 V$.",
    ),
]


def selftest() -> int:
    """Assert the detector fires on every historical true positive."""
    bad = 0
    print("regression self-test — each of these MUST be flagged:\n")
    for name, sentence in REGRESSION_FIXTURES:
        contrastive = bool(CONTRASTIVE.search(sentence))
        hits = [why for pat, why in ASSUMED_SEEDS.items() if re.search(pat, sentence, re.I)]
        ok = contrastive and bool(hits)
        bad += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            print(f"        contrastive={contrastive} assumed-term-hits={len(hits)}")
    print(f"\n{'all fixtures flagged' if bad == 0 else f'{bad} FIXTURE(S) MISSED'}")
    return 1 if bad else 0


def main() -> None:
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    as_json = "--json" in sys.argv
    labels = corpus_assumed_labels()
    findings = []

    for md in sorted(glob(str(CONTENT / "*/*.md"))):
        rel = os.path.relpath(md, REPO)
        try:
            text = open(md).read()
        except Exception:
            continue
        for s in sentences(text):
            if not CONTRASTIVE.search(s):
                continue
            hits = []
            for pat, why in ASSUMED_SEEDS.items():
                if re.search(pat, s, re.I):
                    hits.append(why)
            # a contrastive claim naming a conjecture/definition label directly
            for lab, why in labels.items():
                if lab in s:
                    hits.append(f"{lab}: {why}")
            if hits:
                findings.append(
                    {
                        "file": rel,
                        "sentence": s[:400],
                        "conflicts_with": sorted(set(hits)),
                        # a sentence that ALREADY carries the hedge is likely fine
                        "self_hedged": bool(
                            re.search(
                                r"conditional|calibrat|assumed data|not (?:a )?derivation"
                                r"|does not settle|fibre level|archimedean",
                                s,
                                re.I,
                            )
                        ),
                    }
                )

    unhedged = [f for f in findings if not f["self_hedged"]]
    if not as_json:
        print(f"assumed-kind labels from corpus: {len(labels)}")
        print(f"contrastive claims touching an assumed term: {len(findings)}")
        print(f"  of which NOT self-hedged (candidates): {len(unhedged)}\n")
        for f in unhedged[:40]:
            print(f"  {f['file']}")
            print(f"    {f['sentence'][:170]}")
            print(f"    ⚠ {f['conflicts_with'][0][:120]}\n")
        if len(unhedged) > 40:
            print(f"  … {len(unhedged) - 40} more (see witness JSON)")

    OUT.write_text(
        json.dumps(
            {
                "schema": "qou-audit-probe/v1",
                "bean": "qou-vud6",
                "purpose": (
                    "Flag prose that denies assumption for a term the corpus "
                    "elsewhere declares assumed (calibration / axiom / conjecture / "
                    "definition). Keys on TERMS, not the uses[] graph, because the "
                    "#5047 instance spanned chapters with no edge between them."
                ),
                "posture": "high-recall, agent-confirmed; not a hard gate",
                "counts": {"total": len(findings), "unhedged": len(unhedged)},
                "findings": findings,
                "known_true_positives_now_fixed": [
                    "quantum-observable-universes/braiding-eigenvalue-extraction-novelty.md (#5047)",
                    "quantum-universes/tannaka-krein-overview.md (#5047)",
                    "knots-particles-confinement/interactions-are-pairwise-intro.md (#5044)",
                ],
            },
            indent=2,
        )
        + "\n"
    )
    if not as_json:
        print(f"\nwrote {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
