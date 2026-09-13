#!/usr/bin/env python3
"""Flag derivation-chain documents whose tr_M values disagree with canon.

WHY THIS EXISTS
---------------
`derivation_chain_validator.py` passed two artifacts that disagree by **7.55 %**
about the same quantity, and could not have done otherwise: it validates
*structure* (schema shape, trust tiers, leaf consistency, simple algebraic
re-evaluation), and a convention frame is not a structural property.

The worked case, found 2026-08-30 under bean `qou-46ab`:

    derivation_chain.py::TR_M_AT_Q0["p"]              1.1457596924573009   (D)
    markov-peel-atomic-tr-m.derivation.json step 3    1.0653062286131670…  (C)

Same derivation, same quantity, both artifacts "valid". The document is
hand-authored prose with typed-in numbers, so no producer re-run could ever
have caught it either — which is precisely how it survived the convention-D
sweep that reported completion.

WHAT IT CHECKS
--------------
For every ``*.derivation.json``: any numeric value sitting in a ``tr_M``-ish
context is compared against the canonical registry in ``derivation_chain.py``.
Disagreement beyond ``REL_TOL`` is a finding **unless the document declares its
frame** (the word "convention" plus a C/D marker anywhere in its text).

DESIGN NOTE — keyed on DISAGREEMENT WITH CANON, not on a table of C values.
Hardcoding the convention-C twins is exactly the failure this audit exists to
catch: a second hand-maintained copy of a number, decaying on its own schedule.
So there is no C table here. The canonical D values are read live from
``derivation_chain.py`` at every run, and anything that disagrees with them is
reported whatever the reason — a stale convention, a stale pin, or a typo.

That breadth is deliberate. The audit does not claim a flagged value *is*
convention C; it claims the document disagrees with canon and does not say why.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

#: Relative disagreement above which a value is reported. Well below the
#: 7.55 % C-D gap and well above any legitimate pin difference (~1.2e-7).
REL_TOL = 1e-6

#: A document that says this much about its own frame is scoped, not silent.
#:
#: 🛑 CHECKED ONLY IN THE DOCUMENT-LEVEL FIELDS (`target` / `description`), and
#: that restriction is load-bearing rather than tidy. The first version of this
#: audit searched the whole file, and the self-test caught it MISSING the very
#: case it was written for: the pre-scoping `markov-peel` document discusses
#: conventions at length in its STEP NOTES — "under the canonical convention D,
#: z = q^3/(q^2+1)", "Convention C (z = sqrt(q)/(q+1)) leaves half-integer
#: powers" — while never saying which frame its own numbers are in. A whole-file
#: search read that as a declaration and exempted it.
#:
#: The inversion is the point: the document that talks MOST about conventions is
#: the one most likely to be silently in the wrong one, and a topic-keyed
#: detector exempts it precisely because it is well-informed. A scoping claim
#: belongs at document level; prose about the mathematics is not a claim about
#: the artifact.
_DECLARES = re.compile(r"convention[-\s]*(c|d)\b", re.I)


def _declared(text: str) -> bool:
    """True when the document declares its own frame at document level."""
    try:
        d = json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return bool(_DECLARES.search(text))     # not JSON: fall back to whole text
    head = " ".join(str(d.get(k, "")) for k in ("target", "target_value", "description"))
    return bool(_DECLARES.search(head))

#: Atom aliases as they appear in derivation prose.
#:
#: 🛑 BARE SINGLE LETTERS ARE MATCHED CASE-SENSITIVELY, and that is not
#: pedantry. The first version lower-cased the search window and accepted "d"
#: as deuteron, which made every stray lone `d` in prose an atom marker: the
#: full scan then reported `tr_M(D) = 0.2293101…` and `0.4037670…`, which are
#: the TRITIUM and HELIUM-3 traces, against a deuteron canon. The count of
#: flagged documents was right and the per-row attribution was wrong — the
#: worst shape for a report, because the number looks checkable and the label
#: sends the reader to the wrong quantity.
#:
#: Long names stay case-insensitive ("Deuteron"/"deuteron" are the same word);
#: only the one-letter forms require their canonical case.
_ATOMS_ANY_CASE = {"proton": "p", "neutron": "n", "deuteron": "D",
                   # RECOGNISED BUT NOT IN CANON — and that is the point.
                   # `TR_M_AT_Q0` holds p/n/D only. Without these names here,
                   # a tritium value in a sentence like
                   #   "proton 1.1457…, neutron 0.9877…, deuteron 0.5751…,
                   #    tritium 0.2293…"
                   # takes the nearest PRECEDING atom word — `deuteron` — and
                   # is reported as a deuteron disagreeing with canon by 60 %.
                   # Recognising the name lets the scan skip it for want of a
                   # reference, which is the honest outcome; leaving it out
                   # silently reattributed it to a quantity it is not.
                   "tritium": "T", "helium-3": "3He", "helium3": "3He",
                   "helium-4": "4He", "helium4": "4He"}
_ATOMS_EXACT = {"p": "p", "n": "n", "D": "D",
                "T": "T", "3He": "3He", "4He": "4He", "³He": "3He", "⁴He": "4He"}

_NUM = re.compile(r"\b\d+\.\d{6,}\b")

#: q_0 itself is not a trace. Both substrate pins begin 1.10997858 / 1.10997859
#: and turn up inside tr_M prose constantly ("evaluated at q_0 = ..."), where
#: the nearest-atom-word heuristic below happily attributes them to whichever
#: nucleon the sentence is about. Excluding them removes the single largest
#: false-positive class; it is a principled exclusion rather than a tuning knob,
#: because an anchor is a different kind of object from the trace evaluated at
#: it. Measured: drops 4 of 15 raw hits, none of them a real finding.
_Q0_PREFIXES = ("1.1099785827", "1.1099785955", "1.1099785956", "1.109978595")


def _is_anchor(raw: str) -> bool:
    return any(raw.startswith(pre) for pre in _Q0_PREFIXES)


def canonical() -> dict[str, float]:
    """Canon: the |tr_M| reference, pin- and ordering-validated.

    REPOINTED 2026-09-13 (bean qou-4383). This used to AST-read
    `derivation_chain.TR_M_AT_Q0`, and that registry was GROUPED-era — so this
    audit's definition of "canon" was itself in a superseded frame, and it
    reported every corpus value that disagreed with the WRONG reference.

    It reported **0 findings across 84 documents** in that state, which is the
    part worth understanding: grouped canon plus grouped documents agree, so a
    mutually-consistent stale bubble reads as a clean bill of health. A
    reference audit is only as good as its reference, and this one had no way
    to notice its own was stale — nothing checked it.

    ON THE PROPERTY THIS GIVES UP. The old docstring justified the AST read:
    "this audit never executes the module and cannot be perturbed by its import
    cone." That was a real property and it is partly surrendered here.
    `canonical_trm_reference` is a leaf — mpmath, `_path_bridge`, and a witness
    read — against `derivation_chain`, which pulls in the whole chain
    machinery, so the cone is far smaller but no longer empty. Worth it: an
    audit that cannot be perturbed by an import cone, but CAN be silently
    pointed at the wrong frame, has the weaker of the two guarantees.
    """
    import sys                                            # noqa: PLC0415
    # This audit sets no sys.path (it had no imports to make — that was the
    # point of the AST route). Add computations/ locally rather than at module
    # scope, so the path change stays scoped to the one call that needs it.
    _c = str(ROOT / "computations")
    if _c not in sys.path:
        sys.path.insert(0, _c)
    from canonical_trm_reference import tr_m_nucleon      # noqa: PLC0415
    return {"p": float(tr_m_nucleon("proton")),
            "n": float(tr_m_nucleon("neutron")),
            "D": float(tr_m_nucleon("deuteron"))}


def _canonical_via_registry_ast() -> dict[str, float]:
    """The old AST route, kept for reference. NOT used — see `canonical()`."""
    import ast
    src = (ROOT / "computations" / "derivation_chain.py").read_text()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.AnnAssign) and getattr(node.target, "id", "") == "TR_M_AT_Q0":
            return {k.value: float(v.value) for k, v in zip(node.value.keys, node.value.values)}
        if isinstance(node, ast.Assign) and any(
            getattr(t, "id", "") == "TR_M_AT_Q0" for t in node.targets
        ):
            return {k.value: float(v.value) for k, v in zip(node.value.keys, node.value.values)}
    raise SystemExit("TR_M_AT_Q0 not found in derivation_chain.py — registry moved?")


def _findings(text: str, canon: dict[str, float]) -> list[tuple[str, str, float]]:
    """(atom, value_as_written, rel_diff) for values disagreeing with canon."""
    out = []
    for m in _NUM.finditer(text):
        raw = m.group(0)
        if _is_anchor(raw):
            continue
        try:
            val = float(raw)
        except ValueError:
            continue
        # Which atom is this value about? Take the nearest atom word before it
        # that is inside a tr_M context.
        window = text[max(0, m.start() - 220):m.start()]
        if "tr_m" not in window.lower():
            continue
        atom = None
        for word in re.findall(r"[A-Za-z_0-9³]+", window)[::-1]:
            if word.lower() in _ATOMS_ANY_CASE:
                atom = _ATOMS_ANY_CASE[word.lower()]
                break
            if word in _ATOMS_EXACT:          # case-sensitive: "D" not "d"
                atom = _ATOMS_EXACT[word]
                break
        if atom is None or atom not in canon:
            continue
        ref = canon[atom]
        rel = abs(val - ref) / abs(ref)
        if rel > REL_TOL:
            out.append((atom, raw, rel))
    return out


def scan(text_of: dict[str, str]) -> dict[str, list]:
    canon = canonical()
    flagged: dict[str, list] = {}
    for name, text in text_of.items():
        if _declared(text):
            continue                      # scoped — it says which frame it is
        f = _findings(text, canon)
        if f:
            flagged[name] = f
    return flagged


def _docs() -> dict[str, str]:
    return {
        str(p.relative_to(ROOT)): p.read_text()
        for p in sorted((ROOT / "computations").rglob("*.derivation.json"))
        if "_deprecated" not in str(p)
    }


def _selftest() -> int:
    """The known case must FLAG before scoping and CLEAR after.

    Without this the audit could be narrowed to silence and still look green,
    which is how the previous generation of detectors in this repo went wrong.
    """
    rel = "computations/markov-peel-atomic-tr-m.derivation.json"
    pre = subprocess.run(
        ["git", "show", f"ed60027a29~1:{rel}"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if pre.returncode != 0:
        print("  SELF-TEST UNRUNNABLE — pre-scoping revision unreachable "
              "(shallow clone?). Exiting 2: an unrunnable self-test must not "
              "read as a passing one.")
        return 2
    now = (ROOT / rel).read_text()

    bad = scan({rel: pre.stdout})
    good = scan({rel: now})
    ok = bool(bad) and not good
    print(f"  pre-scoping  : {'FLAGGED' if bad else 'missed'}"
          + (f"  {bad[rel][0][0]} {bad[rel][0][1]} rel={bad[rel][0][2]:.4g}" if bad else ""))
    print(f"  post-scoping : {'clear' if not good else 'STILL FLAGGED'}")
    print("  PASS" if ok else "  FAIL")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return _selftest()
    canon = canonical()
    print("=" * 72)
    print("  Derivation-chain CONVENTION FRAME audit")
    print("=" * 72)
    print(f"  canon (canonical_trm_reference, pin+ordering validated): "
          + ", ".join(f"{k}={v}" for k, v in canon.items()))
    flagged = scan(_docs())
    for name, hits in flagged.items():
        print(f"\n  {name}")
        for atom, raw, rel in hits:
            print(f"      tr_M({atom}) = {raw}   disagrees with canon by {rel:.4g}")
    print(f"\n  documents scanned : {len(_docs())}")
    print(f"  undeclared frame  : {len(flagged)}")
    print("\n  A finding is NOT a claim that the value is convention C — only")
    print("  that it disagrees with canon and the document does not say why.")
    print("  Fix by scoping (state the frame) or by correcting the value.")
    return 0                              # reports; does not gate


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
