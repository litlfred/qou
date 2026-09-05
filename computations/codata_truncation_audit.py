#!/usr/bin/env python3
# polynomial_q_not_applicable: infra audit; no symbolic-q logic.
"""Hand-typed CODATA constants that are TRUNCATED, not merely duplicated.

`qou-46ke` has tracked "hidden CODATA literals" since 2026-06-22 as a
53-script rollup, and its last note (2026-06-23) files the remaining tail as
*"low value — diminishing returns"*. This audit exists because that assessment
is measurably wrong, and because the interesting subset was never separated
out.

The distinction this makes
--------------------------

A hardcoded CODATA value is one of two very different things:

* **Duplication** — the literal equals the canonical value. Bad practice (it
  goes stale when CODATA is revised) but it computes the right number today.
* **Truncation** — the literal is a *prefix* of the canonical value, shorter
  than it. This computes a **different number**, silently, forever.

Only the second changes results, and it is invisible to every precision gate
in the tree: the NO-FLOAT64 family checks how a number is *carried and
serialized*, never whether it was *right when typed*. Wrapping a truncated
literal in `mpmath.mpf` — the standard drain — removes the float64 while
preserving the error, and looks like a fix.

Measured on 2026-08-10, three instances landed in one day:

    m_e     0.51099895000  vs  0.51099895069   worth 1.35e-9 in kappa
    q0      1.10998        vs  1.1099785827…   worth 1.9e-7  in contRatio
    proton  938.272        vs  938.27208943    worth ~1e-9   in vol ratios

all three orders of magnitude above the L1 1-ppQ (1e-15) compute target the
corpus holds itself to. The `m_e` figure is measured rather than assumed: f64
arithmetic on the *same* inputs contributes 5.06e-16, so the literal was the
entire discrepancy.

The canonical table is READ, not typed
--------------------------------------

Every reference value comes from `codata_constants` at run time. A checker for
hardcoded constants must not hardcode them: if it did, it would go stale on the
next CODATA revision in exactly the way it is meant to detect, and would then
report the corpus as wrong while being wrong itself.

Usage
-----

    python3 computations/codata_truncation_audit.py
    python3 computations/codata_truncation_audit.py --list
    python3 computations/codata_truncation_audit.py --strict   # CI gate

`--strict` exits 1 on any TRUNCATED occurrence. Exact duplicates are reported
as a separate count and never block — that is `qou-46ke`'s original scope and a
much larger, much less urgent sweep.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge
import argparse
import ast
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from codata_constants import (  # noqa: E402
    M_E_MEV, M_N_MEV_VALIDATION, M_P_MEV_VALIDATION, M_MU_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION, U_MEV,
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
    AME_B_LI5_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION,
    AME_B_LI7_MEV_VALIDATION,
)
from q_parameter import Q_MP, Q_MUON_50_DIGIT_STR  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def _canon_str(v) -> str:
    """Full-precision decimal for a registry constant.

    ``str(mpf)`` renders at the AMBIENT ``mp.dps``, which is mpmath's default
    **15** when this module is imported -- nothing here calls
    ``set_compute_dps()``, and importing ``_precision`` does not raise it.
    So ``_canon_str(Q_MP)`` returned ``1.10997858275138``: the canonical q0 truncated
    to 15 of its 50 digits.

    That is this audit's own defect class, in this audit. The consequence was
    not cosmetic -- ``classify()`` asks ``canon.startswith(lit)``, so against a
    15-digit canonical every q0 literal LONGER than 15 digits failed the prefix
    test and was reported clean. The literals most likely to be hand-copied are
    exactly the long ones.

    ``strip_zeros`` keeps a short constant (m_e is 11 published digits) from
    being padded out to 50 digits of binary noise.
    """
    from mpmath import mp as _mp
    with _mp.workdps(60):
        return _mp.nstr(v, 50, strip_zeros=True)

# name -> (canonical value read from the registry, the constant to use instead)
CANON: dict[str, tuple[str, str]] = {
    "m_e":   (_canon_str(M_E_MEV), "codata_constants.M_E_MEV"),
    "m_p":   (_canon_str(M_P_MEV_VALIDATION), "codata_constants.M_P_MEV_VALIDATION"),
    "m_n":   (_canon_str(M_N_MEV_VALIDATION), "codata_constants.M_N_MEV_VALIDATION"),
    "m_mu":  (_canon_str(M_MU_MEV_VALIDATION), "codata_constants.M_MU_MEV_VALIDATION"),
    "m_pi":  (_canon_str(M_PI_PM_MEV_VALIDATION),
              "codata_constants.M_PI_PM_MEV_VALIDATION"),
    "u_MeV": (_canon_str(U_MEV), "codata_constants.U_MEV"),
    "q0":    (_canon_str(Q_MP), "q_parameter.Q_MP"),
    # The MUON pin is a second legitimate anchor, not a botched proton one.
    # It sits 11.6 ppb from q0 -- inside DIVERGENT_REL_TOL -- so without its
    # own CANON row every correct muon-pinned literal was reported WRONG.
    # 78 such occurrences on main. classify() picks the NEAREST canonical, so
    # a muon literal now resolves against the muon anchor.
    "q0_muon": (Q_MUON_50_DIGIT_STR, "q_parameter.Q_MUON_50_DIGIT_STR"),
    # AME2020 binding energies. The registry reads these from
    # qou-mass/src/qou_mass/data/ame2020.json at run time; a script that types
    # them instead is the same defect one dataset over, and was invisible here
    # until 2026-09-05 because CANON held CODATA only.
    "B_2H":  (_canon_str(AME_B_DEUTERON_MEV_VALIDATION),
              "codata_constants.AME_B_DEUTERON_MEV_VALIDATION"),
    "B_3H":  (_canon_str(AME_B_TRITIUM_MEV_VALIDATION),
              "codata_constants.AME_B_TRITIUM_MEV_VALIDATION"),
    "B_3He": (_canon_str(AME_B_HE3_MEV_VALIDATION),
              "codata_constants.AME_B_HE3_MEV_VALIDATION"),
    "B_4He": (_canon_str(AME_B_HE4_MEV_VALIDATION),
              "codata_constants.AME_B_HE4_MEV_VALIDATION"),
    "B_5Li": (_canon_str(AME_B_LI5_MEV_VALIDATION),
              "codata_constants.AME_B_LI5_MEV_VALIDATION"),
    "B_6Li": (_canon_str(AME_B_LI6_MEV_VALIDATION),
              "codata_constants.AME_B_LI6_MEV_VALIDATION"),
    "B_7Li": (_canon_str(AME_B_LI7_MEV_VALIDATION),
              "codata_constants.AME_B_LI7_MEV_VALIDATION"),
}

# A DIVERGENT literal must be at least this close to the canonical value before
# it is called a botched copy of it rather than an unrelated number. 1e-4 is
# ~9 orders above the L1 1-ppQ target, so anything inside it is far too close
# to be coincidence and far too far to be acceptable.
DIVERGENT_REL_TOL = "1e-4"

# A literal must share at least this many significant digits with a canonical
# value before it is called a truncation of it. Below that, agreement is
# coincidence: "938.2" is not a truncated proton mass, it is a different number
# that happens to start the same way.
MIN_SHARED_DIGITS = 6

NUMBER = re.compile(r"\d+\.\d+")

# The registry itself. A CODATA value here is the source of truth, not a copy
# of one — flagging it would be the audit reporting its own reference as wrong.
REGISTRY_FILES = {"codata_2022_source.py", "codata_constants.py",
                  "q_parameter.py"}

# A number inside a regex or a match-prefix is a PATTERN, not a computed value.
# Without this the audit flags other detectors — including its own siblings —
# for containing the very literals they exist to find.
PATTERN_MARKERS = ("re.compile", "re.search", "re.match", "re.finditer",
                   r"\d", "_MATCH_", "pattern", "PATTERN", "regex")


def canonical_digits(v: str) -> str:
    return v.replace(".", "").replace("-", "").lstrip("0")


def _shared_prefix_digits(a: str, b: str) -> int:
    """Count leading significant digits two decimal strings agree on."""
    da, db = canonical_digits(a), canonical_digits(b)
    n = 0
    for x, y in zip(da, db):
        if x != y:
            break
        n += 1
    return n


def classify(lit: str) -> tuple[str, str, str] | None:
    """(name, verdict, canonical) if `lit` relates to a canonical value.

    Three verdicts, and the third one is why this function was rewritten:

    * ``EXACT``      -- the literal IS the canonical value. Duplication only.
    * ``TRUNCATED``  -- the literal is a short *prefix*. Loses digits.
    * ``DIVERGENT``  -- the literal agrees to MIN_SHARED_DIGITS and then
      *disagrees*. It is not short, it is **wrong** -- a stale CODATA/AME
      edition, or a typo.

    The original implementation opened with ``if not canon.startswith(lit):
    continue``, so DIVERGENT returned ``None`` and the whole class was
    invisible to the detector built to find it. Measured case, live on main
    2026-09-05: ``computations/substrate/binding_manybody_series.py:43`` types
    ``mp.mpf("28.295673")`` for the He-4 binding energy whose canonical value
    is ``28.2956624``. It shares six digits, is not a prefix, and sits
    3.75e-7 away -- eight orders above the L1 1-ppQ target. A prefix-only
    detector reports it as clean, which is worse than not checking: the
    truncation gate going green is taken as evidence the value is right.

    This is the detector-blindness class AGENTS.md catalogues; the counter is
    to decide on the VALUE (how far apart are they) rather than on the SHAPE
    (does one string start with the other).
    """
    from mpmath import mp, mpf  # local: keeps module import cheap
    best: tuple[str, str, str] | None = None
    best_rel = None
    if len(canonical_digits(lit)) < MIN_SHARED_DIGITS:
        return None
    # Exact/prefix match against the LONGEST canonical that admits it, so a
    # literal shared by two anchors resolves to the more specific one.
    pref = [(n, c) for n, (c, _) in CANON.items() if c.startswith(lit)]
    if pref:
        name, canon = max(pref, key=lambda nc: len(nc[1]))
        return (name, "EXACT" if lit == canon else "TRUNCATED", canon)
    for name, (canon, _) in CANON.items():
        # Not a prefix. Is it nonetheless a copy of this constant?
        if _shared_prefix_digits(lit, canon) < MIN_SHARED_DIGITS:
            continue
        with mp.workdps(80):
            try:
                rel = abs(mpf(lit) - mpf(canon)) / abs(mpf(canon))
            except (ValueError, ZeroDivisionError):
                continue
            if rel >= mpf(DIVERGENT_REL_TOL):
                continue
            # CORRECTLY ROUNDED vs WRONG -- the distinction that stops this
            # detector over-flagging by ~20x. `1.109978582751380808` is not a
            # botched q0: it is q0 round-to-nearest at 19 digits, because
            # ...3808075916 rounds up. Round the canonical value to the
            # literal's own length and compare; only a literal that differs
            # from its own best short form is WRONG rather than merely SHORT.
            nsig = len(canonical_digits(lit))
            best_short = mp.nstr(mpf(canon), nsig, strip_zeros=False)
            verdict = ("ROUNDED" if mpf(best_short) == mpf(lit)
                       else "DIVERGENT")
        # NEAREST canonical wins. Picking the first match instead made every
        # muon-pinned q0 literal a "wrong proton q0".
        if best_rel is None or rel < best_rel:
            best_rel, best = rel, (name, verdict, canon)
    return best


# Numeric constructors: a decimal STRING handed to one of these is a real
# value and is in scope. `mp.mpf("2.224566")` is the canonical defect shape.
_NUMERIC_CTORS = {"mpf", "mpmathify", "Decimal", "Fraction", "float",
                  "mpc", "mpi"}


def _fixture_string_lines(src: str) -> set[tuple[int, str]]:
    """(line, literal) pairs where the number sits in a NON-constructor string.

    A detector's own test fixtures are string data, not computed values:

        ("def protonCodata : R := 938.27208816  -- ...", "938.27208816", MP)

    Those 25 lines in `codata_corpus_literal_scan.py` are the expected inputs
    of a different audit. Rewriting them to import from the registry would
    break that audit while reporting progress on this one -- the drain
    damaging the corpus it is cleaning.

    The discrimination is the ENCLOSING CALL, not the quoting: a string inside
    `mpf(...)` is a value and stays in scope; a bare string in a list or tuple
    is data. Keying on "is it quoted" alone would exempt the entire defect
    class this gate exists to catch.
    """
    out: set[tuple[int, str]] = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    protected: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = getattr(fn, "id", None) or getattr(fn, "attr", None)
            if nm in _NUMERIC_CTORS:
                for a in ast.walk(node):
                    if isinstance(a, ast.Constant) and isinstance(a.value, str):
                        protected.add(id(a))
    for node in ast.walk(tree):
        if (isinstance(node, ast.Constant) and isinstance(node.value, str)
                and id(node) not in protected):
            for m in NUMBER.finditer(node.value):
                for ln in range(node.lineno, (node.end_lineno or
                                              node.lineno) + 1):
                    out.add((ln, m.group(0)))
    return out


def _prose_lines(src: str) -> set[int]:
    """Line numbers that are documentation or console output, not computation.

    A truncated constant in a docstring or a `print()` is describing a value,
    not computing with one. Replacing it with an import changes nothing and
    would often make the prose worse. Excluding them is not leniency — it is
    the difference between a finding and a typo in a sentence.

    Why AST and not a regex: `mp.mpf("0.51099895")` is a string literal and IS
    a genuine defect, while `"m_e = 0.51099895 MeV"` in a docstring is not. No
    lexical test separates those; the parse tree does — one is an argument to a
    numeric constructor, the other is a bare expression-statement string or a
    `print` argument.

    History: the first published run of this audit reported 86 truncations. It
    excluded only lines starting with `#`, so docstrings, prints, and — in
    three cases — a sibling detector's own list of patterns to match were all
    counted. That number was inflated and is corrected here.
    """
    skip: set[int] = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return skip

    def mark(node) -> None:
        lo = getattr(node, "lineno", None)
        hi = getattr(node, "end_lineno", lo)
        if lo:
            skip.update(range(lo, (hi or lo) + 1))

    for node in ast.walk(tree):
        # Bare string expression-statements: module/class/function docstrings
        # and the free-floating comment-strings this corpus uses liberally.
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            mark(node)
        # print(...) — console narration.
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "print":
            mark(node)

        # ── DELIBERATELY-TRUNCATED COMPARATORS ────────────────────────
        # A prefix matcher MUST be shorter than the value it matches, and a
        # window bound MUST NOT equal the value it brackets. "Fixing" these to
        # the full canonical constant breaks the check they implement:
        # `q.startswith(Q_MP)` is trivially true, and `x > M_E_MEV` as a lower
        # bound excludes the very value it is meant to admit.
        #
        # This is the third false-positive class this audit has had, after
        # regex patterns and prose. They share a root: a numeric literal that
        # *looks like* a constant but is playing a structural role. The lesson
        # is in the detector's history rather than only its output — a
        # high-recall matcher on numeric text needs the parse tree to tell
        # role from resemblance.

        # `x.startswith("1.10997…")`
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr in ("startswith", "endswith"):
            mark(node)
        # `lo < x`, `x > bound`, `x == "1.109…"` — the literal is a threshold.
        if isinstance(node, ast.Compare):
            mark(node)
        # Names that announce the role: PREFIX / SIG / SIGNATURE / _LO / _HI.
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                name = getattr(tgt, "id", "") or ""
                if any(m in name.upper()
                       for m in ("PREFIX", "_SIG", "SIGNATURE", "_LO", "_HI")):
                    mark(node)
    return skip


def scan() -> tuple[list[dict], int]:
    rows: list[dict] = []
    exact = 0
    for f in sorted(ROOT.joinpath("computations").rglob("*.py")):
        if "_deprecated" in f.parts or "__pycache__" in f.parts:
            continue
        if f.name == Path(__file__).name or f.name in REGISTRY_FILES:
            continue
        try:
            src = f.read_text()
        except OSError:
            continue
        lines = src.splitlines()
        prose = _prose_lines(src)
        fixtures = _fixture_string_lines(src)
        for i, line in enumerate(lines, 1):
            if i in prose:
                continue
            s = line.strip()
            # Comments and import lines are prose/plumbing, not computed values.
            if s.startswith("#") or "codata_constants" in line or (
                    line.lstrip().startswith(("import ", "from "))):
                continue
            if any(mk in line for mk in PATTERN_MARKERS):
                continue
            for m in NUMBER.finditer(line):
                if (i, m.group(0)) in fixtures:
                    continue
                got = classify(m.group(0))
                if not got:
                    continue
                name, verdict, canon = got
                if verdict == "EXACT":
                    exact += 1
                    continue
                rows.append({
                    "file": str(f.relative_to(ROOT)),
                    "line": i,
                    "constant": name,
                    "literal": m.group(0),
                    "canonical": canon,
                    "verdict": verdict,
                    "use_instead": CANON[name][1],
                })
    return rows, exact


def _selftest() -> int:
    """Assert the classifier still sees all three verdicts.

    A detector that has been narrowed reports a clean tree, and a clean tree
    reads as good news. These fixtures are the tripwire: each is a real
    value taken from this corpus, so a change that stops detecting one of
    them fails here rather than silently in production.
    """
    canon_me = CANON["m_e"][0]
    canon_he4 = CANON["B_4He"][0]
    cases = [
        # (literal, expected verdict, why this fixture exists)
        (canon_me, "EXACT",
         "the canonical value itself must classify as duplication, not loss"),
        ("0.51099895", "TRUNCATED",
         "the 8-figure m_e prefix, 25 live occurrences on main"),
        ("1.109978582751380808", "ROUNDED",
         "q0 round-to-nearest at 19 digits — right but short; scoring this "
         "DIVERGENT over-flagged the corpus ~20x"),
        ("1.1099785955573347", "TRUNCATED",
         "the retired MUON pin — a second anchor, not a botched proton q0; "
         "48 occurrences were scored DIVERGENT before it had a CANON row"),
        ("28.295673", "DIVERGENT",
         "binding_manybody_series.py:43 — agrees to 6 digits then diverges; "
         "a prefix-only classifier scores this CLEAN"),
    ]
    failures = 0
    print("selftest — classifier fixtures")
    for lit, want, why in cases:
        got = classify(lit)
        verdict = got[1] if got else "NONE"
        ok = verdict == want
        failures += not ok
        print(f"  [{'ok ' if ok else 'FAIL'}] {lit:<24s} "
              f"want {want:<9s} got {verdict:<9s}  {why}")
    if failures:
        print(f"\nSELFTEST FAILED: {failures} fixture(s) — the classifier has "
              "been narrowed; its clean runs are no longer evidence.")
        return 1
    print("\nselftest ok — all three verdicts reachable")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list", action="store_true", help="print every finding")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any TRUNCATED or DIVERGENT literal "
                         "is present")
    # The harness in scripts/precision-gates.sh invokes `--self-test`
    # (hyphenated). A gate whose flag does not match is reported as a
    # self-test FAILURE, which is how this one entered the array red.
    ap.add_argument("--self-test", "--selftest", dest="selftest",
                    action="store_true",
                    help="verify the classifier still detects each verdict")
    ap.add_argument("--baseline", action="store_true",
                    help="ratchet mode: exit 1 only on findings absent from "
                         "the baseline (blocks NEW truncations)")
    ap.add_argument("--write-baseline", action="store_true",
                    help="record the current findings as the baseline")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()

    rows, exact = scan()
    by_const: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_const[r["constant"]].append(r)

    # Write the artifact BEFORE the human-readable report, not after.
    # Caught by this script failing on itself: piped through `head`, the
    # console output raised BrokenPipeError part-way and the process died
    # before ever reaching json.dump, so the run produced no witness while
    # appearing to succeed. That is precisely the failure class its sibling
    # witness_producer_executes_audit.py exists to detect -- a producer that
    # cannot write its own witness. Emit the durable output first; the
    # printing is a courtesy and must not be able to prevent it.
    out = HERE / "codata-truncation-audit.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload = {
        "engine": "python-stdlib",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "codata-truncation-audit",
        "scriptFile": "codata_truncation_audit.py",
        "description": (
            "Hand-typed CODATA/substrate constants that are a short prefix of "
            "the canonical value, and so compute a different number. Separates "
            "that class from exact duplication, which is qou-46ke's original "
            "and much larger scope. Canonical values are read from "
            "codata_constants / q_parameter at run time, never typed here."
        ),
        "min_shared_digits": MIN_SHARED_DIGITS,
        "truncated_total": sum(1 for r in rows
                               if r.get("verdict") == "TRUNCATED"),
        "truncated_files": len({r["file"] for r in rows
                                if r.get("verdict") == "TRUNCATED"}),
        "divergent_total": sum(1 for r in rows
                               if r.get("verdict") == "DIVERGENT"),
        "divergent_files": len({r["file"] for r in rows
                                if r.get("verdict") == "DIVERGENT"}),
        "rounded_total": sum(1 for r in rows
                             if r.get("verdict") == "ROUNDED"),
        "rounded_files": len({r["file"] for r in rows
                              if r.get("verdict") == "ROUNDED"}),
        "blocking_total": len(rows),
        "by_constant": {k: len(v) for k, v in by_const.items()},
        "exact_duplicates": exact,
        "findings": rows,
    }
    _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(_prov_payload, indent=2) + "\n")

    trunc = [r for r in rows if r.get("verdict") == "TRUNCATED"]
    diverg = [r for r in rows if r.get("verdict") == "DIVERGENT"]
    rounded = [r for r in rows if r.get("verdict") == "ROUNDED"]

    print("=" * 74)
    print("REFERENCE-LITERAL AUDIT — hand-typed CODATA / AME values that do")
    print("                          not match the registry they came from")
    print("=" * 74)
    print(f"  TRUNCATED : {len(trunc):4d} occurrence(s) in "
          f"{len({r['file'] for r in trunc})} file(s)  (short prefix)")
    print(f"  DIVERGENT : {len(diverg):4d} occurrence(s) in "
          f"{len({r['file'] for r in diverg})} file(s)  (agrees then DISAGREES"
          " — WRONG, not short)")
    print(f"  ROUNDED   : {len(rounded):4d} occurrence(s) in "
          f"{len({r['file'] for r in rounded})} file(s)  (correctly rounded, "
          "so right but SHORT)")
    for name, items in sorted(by_const.items(), key=lambda kv: -len(kv[1])):
        canon = CANON[name][0]
        print(f"    {name:6s} {len(items):4d}  e.g. {items[0]['literal']}"
              f"   canonical {canon[:22]}")
    print(f"  exact duplicates (not blocking): {exact}")
    print("\n  Truncation computes a DIFFERENT number, silently. No precision")
    print("  gate sees it: the NO-FLOAT64 family checks how a value is carried")
    print("  and serialized, never whether it was right when typed. Wrapping a")
    print("  truncated literal in mpf removes the float and keeps the error.")

    if rows:
        print("\n  Findings:" if args.list else "\n  Findings (first 25):")
        for r in (rows if args.list else rows[:25]):
            print(f"    [{r.get('verdict','?'):9s}] {r['file']}:{r['line']}"
                  f"  {r['constant']} = {r['literal']}"
                  f"  (canonical {r['canonical'][:20]})"
                  f"  ->  {r['use_instead']}")
        if not args.list and len(rows) > 25:
            print(f"    ... and {len(rows) - 25} more (--list)")

    print(f"\n  witness -> {out.name}")

    # ---- ratchet -------------------------------------------------------
    # HARD GATE, without being red on arrival. AGENTS.md records that a gate
    # which fails from its first run gets skipped, and a skipped gate is how a
    # checker goes quiet -- so the 970-item backlog is baselined and every NEW
    # truncation blocks immediately. The baseline DRAINS, never grows: adding
    # to it to go green is the move this whole gate exists to prevent.
    bl_path = HERE / "codata-truncation-baseline.json"
    key = lambda r: f"{r['file']}:{r['line']}:{r['literal']}"  # noqa: E731
    if args.write_baseline:
        bl_path.write_text(json.dumps(
            {"_comment": "Pre-existing reference-literal findings. DRAINS, "
                         "never grows. Never add an entry to go green — fix "
                         "at the call site by importing from the registry.",
             "entries": sorted(key(r) for r in rows)}, indent=2) + "\n")
        print(f"\nbaseline written: {len(rows)} entries -> {bl_path.name}")
        return 0
    if args.baseline:
        try:
            known = set(json.loads(bl_path.read_text())["entries"])
        except (OSError, ValueError, KeyError):
            known = set()
        new_rows = [r for r in rows if key(r) not in known]
        print(f"\n  RATCHET: {len(known)} baselined, {len(new_rows)} NEW")
        if new_rows:
            print("  NEW findings — fix at the call site, do NOT baseline:")
            for r in new_rows[:20]:
                print(f"    [{r.get('verdict')}] {r['file']}:{r['line']}"
                      f"  {r['constant']} = {r['literal']}"
                      f"  ->  {r['use_instead']}")
            return 1
        return 0

    if args.strict and rows:
        print(f"\nSTRICT: {len(trunc)} truncated + {len(diverg)} divergent "
              f"+ {len(rounded)} rounded literal(s) — exiting 1")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
