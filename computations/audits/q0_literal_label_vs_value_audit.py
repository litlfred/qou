#!/usr/bin/env python3
"""q0_literal_label_vs_value_audit.py — hardcoded q0 pins whose LABEL in source
contradicts their VALUE.

Bean `qou-fd0e`. This is a FOURTH anchor-checking seam, and nothing else in the
corpus is on it. The three that exist compare:

  `Q0_OK` / `Q0_FLIP`     a witness envelope against another envelope
  `payload_mislabels`     a payload field's NAME against that field's VALUE
  `envelope_vs_payload`   the envelope's stamped anchor against the payload

All three read *witnesses*. None reads the SOURCE, so none can see a producer
that hardcodes a pin and describes it as the other one.

WHY THE EXISTING PIN AUDITS CANNOT CATCH THIS. `q0_hardcoded_pin_audit`,
`undeclared_muon_pin_flip_risk_audit`, `hardcoded_q0_literal_families_audit` and
`hardcoded_literal_audit` all ratchet on literals that **DIVERGE** from the
canonical pin — wrong digits, stale truncations, off-pin families. A literal
that reproduces the canonical pin to the last digit is precisely the case they
are built to pass over. But a *correct muon pin* sitting under the comment
"proton-mass-anchored" is still a defect: it is 11.5371 ppb from what it claims
to be, and every reader downstream inherits the claim, not the value.

FOUND BY HAND, WHICH IS WHY THIS EXISTS. `computations/probes/_gap_a4_qsafe.py`
carried

    # Substrate parameter (proton-mass-anchored q_0, 50 dps).
    Q_0_50DPS: str = "1.10997859555733471989976322048322502665620840878.."

— the canonical MUON pin, 4.5e-24 ppb from pin A and 11.5371 ppb from the proton
pin, labelled proton. **17 producers import that constant** (the `gap_a4_T4`
through `T18` series plus `borromean_trace_cross_validator`), so one comment
mislabelled the anchor of a whole probe family. It is the second instance of the
shape in `qou-fd0e`; `he_nu_sdp_psd_count_test` is the first. Two instances, one
of them reaching 17 producers through a module written specifically to
de-duplicate, is a class rather than a typo.

METHOD. Walk every `*.py` outside `_deprecated/`. AST-parse, take every string
or float constant that is q0-shaped, and classify its VALUE by mpmath distance
to the two pins — not by prefix matching, so a 17-digit truncation classifies
the same as a 50-digit one. Then read the LABEL from the source text around it:
the inline comment on that line, the comment block immediately above, and the
name it is bound to. Disagreement is reported; agreement is not.

WHAT THIS DELIBERATELY DOES NOT DO. It does not change a literal, and it must
not: whether a mislabelled constant should have its label corrected or its value
corrected is a question about INTENT, and getting it backwards moves every
downstream consumer by 11.5 ppb. The audit reports; a human rules.

SCOPE IS PRINTED WHETHER OR NOT IT IS FLATTERING. A literal with no label nearby
is *unexamined*, not *clean*, and is counted and shown separately. A file that
does not parse is unexamined too. Neither is folded into the pass count — that
substitution is the defect `qou-i5jy` exists for.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parent

mp.dps = 60

#: The two layers. Values are exact strings; no float64 anywhere in this audit.
PIN_MUON = mpf("1.10997859555733471989976322048322502665620840878")
PIN_PROTON = mpf("1.1099785827513808075916690956")

#: A literal within this many ppb of a pin is that pin. The muon B/C closed
#: forms sit 0.08 ppb from A, so this tolerance treats the whole muon family as
#: muon — which is right here: the question is WHICH LAYER, not which vintage.
PIN_TOL_PPB = mpf("1")

#: Cheap pre-filter before the (much more expensive) mpf conversion.
_Q0_SHAPED = re.compile(r"^1\.109[0-9]")

_SKIP = {"_deprecated", ".git", "__pycache__", "node_modules", ".beans"}


def _layer(text: str):
    """(layer, ppb-from-that-pin) for a q0-shaped literal, or (None, None)."""
    try:
        v = mpf(text)
    except Exception:  # noqa: BLE001 — not a number we can judge
        return None, None
    dm = (v - PIN_MUON) / PIN_MUON * mpf(10) ** 9
    dp = (v - PIN_PROTON) / PIN_PROTON * mpf(10) ** 9
    if abs(dm) < PIN_TOL_PPB:
        return "muon", dm
    if abs(dp) < PIN_TOL_PPB:
        return "proton", dp
    return "off-pin", None


def _label_near(lines: list, lineno: int, name: str | None):
    """What does the SOURCE CLAIM this literal is?

    Looks at the binding name, the trailing comment on the literal's own line,
    and the contiguous comment block immediately above it. A context naming both
    anchors is `ambiguous`, not a mislabel — a cross-anchor comparison legitimately
    mentions both, and calling that a defect is how a detector earns its
    false positives.
    """
    ctx = []
    if name:
        ctx.append(name)
    i = lineno - 1
    if 0 <= i < len(lines):
        line = lines[i]
        if "#" in line:
            ctx.append(line.split("#", 1)[1])
    j = i - 1
    while j >= 0 and (lines[j].strip().startswith("#") or lines[j].strip() == ""):
        if lines[j].strip().startswith("#"):
            ctx.append(lines[j])
        j -= 1
        if i - j > 8:
            break
    blob = " ".join(ctx).lower()
    has_p = "proton" in blob
    has_m = "muon" in blob or "mu_e" in blob or "m_mu" in blob
    if has_p and has_m:
        return "ambiguous"
    if has_p:
        return "proton"
    if has_m:
        return "muon"
    return None


def _scan():
    findings, unlabelled, offpin = [], [], []
    n_files = n_unparseable = n_literals = n_agree = 0
    unparseable = []
    for f in sorted(REPO.rglob("*.py")):
        if _SKIP & set(f.parts):
            continue
        try:
            src = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:  # noqa: BLE001
            continue
        if "1.109" not in src:          # cheap reject; nothing q0-shaped here
            continue
        n_files += 1
        try:
            tree = ast.parse(src)
        except Exception as exc:  # noqa: BLE001
            n_unparseable += 1
            unparseable.append(f"{f.relative_to(REPO)}: {exc.__class__.__name__}")
            continue
        lines = src.splitlines()
        # bind lineno -> assignment target name, for the label context
        names = {}
        for n in ast.walk(tree):
            if isinstance(n, (ast.Assign, ast.AnnAssign)):
                tgts = n.targets if isinstance(n, ast.Assign) else [n.target]
                for t in tgts:
                    if isinstance(t, ast.Name):
                        names[n.lineno] = t.id
        for n in ast.walk(tree):
            if not isinstance(n, ast.Constant):
                continue
            raw = n.value
            if isinstance(raw, float):
                raw = repr(raw)
            if not isinstance(raw, str) or not _Q0_SHAPED.match(raw):
                continue
            n_literals += 1
            layer, ppb = _layer(raw)
            rel = str(f.relative_to(REPO))
            if layer is None:
                continue
            if layer == "off-pin":
                offpin.append(f"{rel}:{n.lineno}  {raw[:26]}")
                continue
            claim = _label_near(lines, n.lineno, names.get(n.lineno))
            if claim is None:
                unlabelled.append(f"{rel}:{n.lineno}  {layer}  {raw[:24]}")
            elif claim == "ambiguous":
                n_agree += 1          # names both layers: a comparison, not a defect
            elif claim == layer:
                n_agree += 1
            else:
                findings.append({
                    "file": rel, "line": n.lineno,
                    "labelled": claim, "value_is": layer,
                    "literal": raw[:32],
                    "ppb_from_claimed_pin": mp.nstr(
                        (mpf(raw) - (PIN_PROTON if claim == "proton" else PIN_MUON))
                        / (PIN_PROTON if claim == "proton" else PIN_MUON)
                        * mpf(10) ** 9, 6),
                })
    return {
        "findings": findings, "unlabelled": unlabelled, "offpin": offpin,
        "unparseable": unparseable,
        "n_files": n_files, "n_unparseable": n_unparseable,
        "n_literals": n_literals, "n_agree": n_agree,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any label contradicts its value")
    ap.add_argument("--show", type=int, default=12)
    args = ap.parse_args()
    r = _scan()

    print("=" * 74)
    print(" q0 literals whose LABEL contradicts their VALUE")
    print("=" * 74)
    print(f"  files containing '1.109'          {r['n_files']}")
    print(f"    of those, UNPARSEABLE           {r['n_unparseable']}   <- unexamined")
    print(f"  q0-shaped literals found          {r['n_literals']}")
    print(f"    label agrees with value         {r['n_agree']}")
    print(f"    label CONTRADICTS value         {len(r['findings'])}   <- the finding")
    print(f"    no label in context             {len(r['unlabelled'])}   <- UNEXAMINED, not clean")
    print(f"    off-pin (neither layer)         {len(r['offpin'])}   <- other audits' population")

    if r["findings"]:
        print("\n  MISLABELLED — the source says one layer and holds the other:")
        for x in r["findings"]:
            print(f"    {x['file']}:{x['line']}")
            print(f"      labelled {x['labelled']!r}, value is {x['value_is']!r}"
                  f"  ({x['ppb_from_claimed_pin']} ppb from what it claims to be)")
            print(f"      {x['literal']}")
    else:
        print("\n  None. Every q0 literal with a label agrees with its own value.")

    for title, key in (("no label in context", "unlabelled"),
                       ("unparseable", "unparseable")):
        if r[key]:
            print(f"\n  {title} ({len(r[key])}), first {args.show}:")
            for x in r[key][:args.show]:
                print(f"    {x}")

    if args.strict and r["findings"]:
        print("\n  --strict: exiting 1 on a label that contradicts its value.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
