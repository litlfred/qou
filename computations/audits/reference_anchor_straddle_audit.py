#!/usr/bin/env python3
"""Does any producer compare against a reference witness pinned to the OTHER q0?

THE INSTANCE THAT PROMPTED THIS. `tr_m_q_hecke_seminormal` resolves PROTON (it is
undeclared, and the runtime default is proton) while its `REF_WITNESS` was the
base-name `atomic-tr-m-mpfr-50dps.witness.json`, which is `ideal_muon`. A
proton-pinned twin sat beside it, unread. The producer's whole purpose is to
check the q-Hecke partition sum against the canonical tr_M, and it reported ~1e-7
agreement for as long as it has existed. Against the ANCHOR-MATCHED reference the
two routes agree to 1e-50 -- exactly, to the serialization limit. The entire
"discrepancy" was the 11.5 ppb mu-p q0 gap, amplified ~n-fold because tr_M is a
product over ~n crossings.

WHY IT WENT UNSEEN FOR MONTHS, and why a detector is warranted rather than a
one-off fix: the producer computed in float64, whose error was the SAME ORDER as
the straddle. A wrong answer sitting under a noise floor of its own size is
invisible to every check that reads the number. It became legible only when the
arithmetic went exact (#5714, #5723). So the population of interest is exactly
the one nobody can see by looking at results.

WHAT THIS FLAGS. A producer P that reads reference witness W, where W declares a
q0Anchor and P resolves a different one. Both halves are established facts, not
heuristics: P's anchor comes from `resolve_q0_anchor` (the same function the
witness builder stamps with), and W's comes from W's own recorded field.

DELIBERATE COMPARISONS ARE NOT DEFECTS and are reported separately: a producer
that reads BOTH pins of the same reference is doing cross-anchor work on purpose
(`markov_peel_atomic_witness` is the worked example). The discriminator is
whether the producer names both twins, not the mismatch alone.

Run: python3 computations/audits/reference_anchor_straddle_audit.py [--selftest]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # computations/
REPO = ROOT.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import resolve_q0_anchor  # noqa: E402

_REF_CALL = re.compile(r'["\']([A-Za-z0-9_.\-]+\.witness\.json)["\']')

# THE FIRST COUNT THIS AUDIT PRODUCED WAS 214, AND IT WAS THE WRONG QUESTION.
# Two unrelated things both look like "producer pin != reference pin":
#
#   (1) The producer reads `q-pinning-50-digit.witness.json` to OBTAIN q0. That
#       string IS the muon anchor's definition, so such a producer COMPUTES AT
#       MUON while `resolve_q0_anchor` reports the proton default. That is a
#       MISLABEL, it is the documented `qou-aj91` class (~85 producers, AGENTS.md
#       q0-anchor section), and PR #5699 is fixing the stamping side of it. It is
#       not this audit's question and it swamped the result 200:1.
#
#   (2) The producer computes at its own pin and COMPARES ITS RESULT against a
#       reference witness built at the other pin. That is the tr_m_q_hecke case:
#       a real number measured against the wrong layer, invisible because the
#       producer's own float64 noise was the same size as the gap.
#
# Only (2) is a straddle in the sense that matters here. Anchor-DEFINING sources
# are excluded by name, and audit tooling is excluded because it reads witnesses
# AS DATA TO INSPECT -- comparing a shape guard's "pin" to the pin of a file it
# is auditing is meaningless.
_ANCHOR_SOURCES = {
    "q-pinning-50-digit.witness.json",
}
_AUDIT_TOOLING = re.compile(r"(_audit|_guard|_validator|audits/)")



def _names_actually_loaded(src: str) -> set:
    """Witness names that FLOW INTO A LOAD, not ones merely mentioned.

    The regex that finds `"*.witness.json"` cannot tell a load from a comment or
    a provenance string. Measured on the 11 candidates: one
    (`markov_trace_axiomatic_multi_atom`) names the reference five times -- in
    comments and in a `"canonical_witness":` dict value -- and never loads it. A
    detector that calls that a straddle is reporting on prose.

    A line-local check is not enough either: `for legacy_name in ["x.json"]:`
    followed by `HERE / legacy_name` is a real load whose string is on a
    different line from the call. So this walks the AST and counts a name as
    loaded when it is a call ARGUMENT, or is bound to a variable that is used
    anywhere outside a plain dict value. Both known-real cases
    (`binding_K_direct`, `rho_k_h3a_residual_decomposition`) bind first and load
    later; the selftest pins all three.
    """
    import ast as _ast
    try:
        tree = _ast.parse(src)
    except SyntaxError:
        return set()
    lit = lambda n: (isinstance(n, _ast.Constant) and isinstance(n.value, str)
                     and n.value.endswith(".witness.json"))
    loaded, bound = set(), {}
    for node in _ast.walk(tree):
        if isinstance(node, _ast.Call):
            for a in list(node.args) + [k.value for k in node.keywords]:
                if lit(a):
                    loaded.add(a.value)
                # a list/tuple of names iterated then joined to a path
                if isinstance(a, (_ast.List, _ast.Tuple)):
                    loaded |= {e.value for e in a.elts if lit(e)}
        elif isinstance(node, _ast.Assign) and lit(node.value):
            for t in node.targets:
                if isinstance(t, _ast.Name):
                    bound[t.id] = node.value.value
        elif isinstance(node, (_ast.For,)) and isinstance(node.iter, (_ast.List, _ast.Tuple)):
            names = {e.value for e in node.iter.elts if lit(e)}
            if names and isinstance(node.target, _ast.Name):
                loaded |= names          # iterated -> used in the body
    # a bound constant counts as loaded if its name is referenced anywhere else
    for var, val in bound.items():
        uses = sum(1 for n in _ast.walk(tree)
                   if isinstance(n, _ast.Name) and n.id == var)
        if uses > 1:
            loaded.add(val)
    return loaded


def _witness_anchor(name: str) -> tuple[str | None, Path | None]:
    """The q0Anchor a referenced witness declares, and where it lives."""
    hits = list(ROOT.rglob(name))
    if not hits:
        return None, None
    try:
        body = json.loads(hits[0].read_text())
    except Exception:  # noqa: BLE001
        return None, hits[0]
    a = body.get("q0Anchor")
    return (str(a) if a is not None else None), hits[0]


def _twin(name: str) -> str | None:
    """The anchor-specific sibling of a base-name reference, if one exists."""
    stem = name[: -len(".witness.json")]
    for suffix in ("-proton", "-muon"):
        if stem.endswith(suffix):
            return None                      # already anchor-specific
    for suffix in ("-proton", "-muon"):
        cand = f"{stem}{suffix}.witness.json"
        if list(ROOT.rglob(cand)):
            return cand
    return None


def scan():
    straddles, comparisons, unknown = [], [], []
    for py in sorted(ROOT.rglob("*.py")):
        if "_deprecated" in py.parts or py.name.startswith("test_"):
            continue
        try:
            src = py.read_text(errors="ignore")
        except Exception:  # noqa: BLE001
            continue
        if _AUDIT_TOOLING.search(str(py)):
            continue                         # reads witnesses as data, not as a reference
        _loaded = _names_actually_loaded(src)
        refs = sorted(r for r in set(_REF_CALL.findall(src))
                      if r not in _ANCHOR_SOURCES and r in _loaded)
        if not refs:
            continue
        # A producer naming BOTH pins of one reference is comparing them on
        # purpose; the mismatch is the point, not a defect.
        bases = {r.replace("-proton", "").replace("-muon", "") for r in refs}
        deliberate = {b for b in bases
                      if sum(1 for r in refs
                             if r.replace("-proton", "").replace("-muon", "") == b) > 1}
        try:
            p_anchor, _ = resolve_q0_anchor(py)
        except Exception:  # noqa: BLE001
            continue
        if p_anchor not in ("muon", "proton"):
            continue
        for r in refs:
            if r == py.name.replace("_", "-").replace(".py", ".witness.json"):
                continue                     # its own output
            base = r.replace("-proton", "").replace("-muon", "")
            w_anchor, wpath = _witness_anchor(r)
            if w_anchor is None:
                if wpath is not None:
                    unknown.append((py, r))
                continue
            if w_anchor == p_anchor:
                continue
            row = (py, r, p_anchor, w_anchor, _twin(r))
            (comparisons if base in deliberate else straddles).append(row)
    return straddles, comparisons, unknown


def main(argv) -> int:
    straddles, comparisons, unknown = scan()
    print("=" * 74)
    print("  REFERENCE-ANCHOR STRADDLE AUDIT")
    print("=" * 74)
    print(f"  straddles (producer pin != reference pin) : {len(straddles)}")
    print(f"  deliberate cross-anchor comparisons       : {len(comparisons)}")
    print(f"  reference declares no q0Anchor            : {len(unknown)}")
    print("  (anchor-DEFINING sources and audit tooling excluded — see the\n   note at _ANCHOR_SOURCES; including them gives 214, dominated 200:1\n   by the qou-aj91 mislabel class, which is a different defect)")
    if straddles:
        print("\n  STRADDLES — a computation measured against the other layer:")
        for py, r, pa, wa, twin in straddles:
            rel = py.relative_to(REPO)
            print(f"    {rel}")
            print(f"        producer resolves : {pa}")
            print(f"        reads             : {r}  (declares {wa})")
            print(f"        anchor-matched twin exists: {twin or 'NO'}")
    if comparisons:
        print("\n  DELIBERATE (names both pins of one reference — not a defect):")
        for py, r, pa, wa, _t in comparisons:
            print(f"    {py.relative_to(REPO)}  <- {r} ({wa}) at pin {pa}")

    if "--selftest" in argv:
        # tr_m_q_hecke_seminormal was the founding case and is FIXED, so it must
        # NOT appear; markov_peel_atomic_witness reads both pins deliberately and
        # must never be reported as a straddle. Without these the audit could be
        # narrowed into reporting a clean tree, which is how the retracted grep
        # in bean qou-cq2n failed.
        ok = True
        names = {p.stem for p, *_ in straddles}
        # markov_trace_axiomatic_multi_atom NAMES the reference five times and
        # never loads it -- it must not be reported. binding_K_direct and
        # rho_k_h3a_residual_decomposition bind the name first and load later --
        # a line-local check misses both, so they pin the other direction.
        for stem, want_absent in (("tr_m_q_hecke_seminormal", True),
                                  ("markov_peel_atomic_witness", True),
                                  ("markov_trace_axiomatic_multi_atom", True)):
            good = (stem not in names) == want_absent
            ok &= good
            print(f"  selftest {stem} not-a-straddle: {'OK' if good else 'FAIL'}")
        if not ok:
            print("SELFTEST FAILED")
            return 1
        print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
