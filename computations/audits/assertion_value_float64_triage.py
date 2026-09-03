#!/usr/bin/env python3
"""The float64 class PR #5910 deferred: `.assertions[].computed` / `.expected`.

#5910 drained `.assertions[].tolerance` -- 1232 fields -- and named what it was
deliberately leaving:

    ".assertions[].computed (84) and .assertions[].expected (27) in the
     small-file group. These are results, not thresholds -- the same argument
     does not apply and each needs its producer."

That figure is for the small-file group (witnesses with 1-4 raw fields).
Corpus-wide the class is an order of magnitude bigger, and this measures it so
the next agent starts from a scoped tranche rather than a grep.

WHY IT IS NOT ONE CLASS, and why a blanket stringify would be wrong. #5910's
whole argument for tolerance was that a threshold is DECLARED -- `1e-9` is a
number the author typed, nothing was measured to that precision. That argument
transfers to some of these and not others:

  * `computed`  is a MEASUREMENT almost by definition. A float() cast on an
    mpmath value here silently truncates a 50-dps result to binary64. Fixing it
    is a producer change (`fmt(x)`, not `float(x)`), and the value MOVES -- so
    it cannot be done by textual repair the way tolerance was.
  * `expected`  is mixed, exactly as tolerance was. `17.4`, `34.14`, `1.0` are
    author-typed targets; `0.9980774473848675` is a computed comparand. Only
    the first kind is a serialization question.

INTEGRAL VALUES ARE EXCUSED, not counted, matching the raw-float64 ratchet:
`0.0` and `1.0` are exact in binary64 and carry no lost precision. That
exclusion is most of the corpus occurrences, which is why a bare grep for
`computed=float(` (639 sites / 312 files) badly overstates the defect.

Worked instance, fixed in the q0-flip drain: `c_k_beta_decay_witness.py` wrote
`computed=float(max_ge_ratio_dev)` on a 50-dps residual. It was INVISIBLE while
the value happened to be exactly 0.0 -- integral, excused -- and became a
REGRESSED gate the moment a re-run produced a real residual, 9.96e-71. So the
integral majority is not safe by nature; it is safe by accident of its current
value.

Writes no witness. Read-only over committed artifacts.
"""
from __future__ import annotations

import argparse
import ast
import collections
import glob
import json
import os
import pathlib
import re
import sys


def is_intlike(v) -> bool:
    try:
        return float(v) == int(float(v))
    except (ValueError, OverflowError):
        return False


# ---------------------------------------------------------------------------
# --by-precision: does the producer actually COMPUTE in mpf?
# ---------------------------------------------------------------------------
#
# WHY THIS EXISTS (added 2026-08-29, bean qou-p77d).
#
# This script's own READING says the repair "recovers digits the cast threw
# away". That is true for most of the population and FALSE for a third of it,
# and the two need opposite treatment:
#
#   A. the producer raises mp.dps, so the mpf carries real digits and the
#      float() cast genuinely discards them -> repair as prescribed.
#   B. the producer NEVER raises mp.dps (or pins it <= 15), so the computation
#      is float64-equivalent no matter how much mpmath it imports. Serializing
#      it with mp.nstr(x, 40) prints forty digits of a double. That is not a
#      repair, it is LAUNDERING -- AGENTS.md: "Never report a float64 agreement
#      as 'exact', 'identical', or 'to N digits'."
#
# The distinction is not cosmetic and it inverts the work order. Measured on
# the 883: A=583, B=291, C=9 (no producer found) -- and the "worst offenders"
# ranking this script prints is DOMINATED BY B. The single largest entry,
# channel_product_mass.py at 64 fields (7% of the whole tranche), imports
# mpmath, calls mp.log, and casts back at three sites -- while every one of its
# inputs (M_E_MEV, M_P_MEV, m_n_derived_3input, Q) is a plain Python float and
# mp.dps is never raised off its default 15. Starting from the top of the
# ranking, as the bean suggested, starts in exactly the wrong bucket.
#
# B is not "already fine" either. Those producers are float64 while PRESENTING
# as mpmath computations, which is its own defect -- but the fix is upstream
# precision (mpf(str(CONST)) at the constant, plus a real dps), not a
# serialization change at the assertion. Different job, different bean.
#
# 🛑 AND A VALUE THAT "ROUND-TRIPS THROUGH FLOAT64" IS NOT PROOF OF EITHER
# BUCKET. This looks like the decisive runtime test the static split cannot
# give you, and it is not. Measured over the 302 fields drained in the first
# pass, the test flagged 55 -- and all 55 were EXACT residuals of the form
# k * 2^-235 for k in {0.5, 1, 1.5, 2, 3}, the ULP scale of a ~71-dps
# computation, meaning "the two sides agreed to within a few ULPs". A power of
# two is exactly representable in binary64, so those values survive the round
# trip losslessly however many decimal digits they take to write, and every
# digit printed is true. "Rendered from a double" and "exactly representable
# in a double" leave IDENTICAL numerical evidence; only provenance separates
# them. Use the signal to flag for reading, never to decide.
_DPS_RAISE = re.compile(
    r"mp\.dps\s*=\s*(\d+)|mp\.mp\.dps\s*=\s*(\d+)|set_compute_dps\s*\(")


def _producer_index() -> dict:
    """basename -> path, over every non-deprecated .py in the tree."""
    idx = {}
    for p in pathlib.Path(".").rglob("*.py"):
        s = str(p)
        if ".git" in s or "_deprecated" in s:
            continue
        idx.setdefault(p.name, p)
    return idx


def _module_level_dps_raise(path) -> str | None:
    """The dps raise this module performs AT IMPORT, or None.

    NOT USED BY `classify_producer` -- read the note there before wiring it in.
    Kept because it is the correct implementation of the question it asks, and
    the two wrong implementations that preceded it are worth not writing again.

    AST, not regex, and deliberately so. The regex version read the file
    line-wise and skipped comments by testing `line[0] != "#"` -- which let
    through a DOCSTRING line beginning with a backtick. `knot_volumes.py`
    documents its API in prose containing the words `dps=100` and
    `set_compute_dps`, and three producers were reclassified on the strength of
    that sentence. An AST walk cannot match prose.

    Module level ONLY, and `def`/`class` bodies are skipped: a module-level
    `def go(): mp.dps = 90` DECLARES a raise, it does not perform one, so
    walking into it would call the module an import-time raiser. (Both errors
    were caught by this module's selftest, not by review.)
    """
    try:
        tree = ast.parse(pathlib.Path(path).read_text(encoding="utf-8",
                                                      errors="replace"))
    except Exception:
        return None
    for node in tree.body:
        # A def/class at module level DECLARES a body; it does not run it, so
        # walking into it would count `def go(): mp.dps = 90` as an import side
        # effect. (Caught by this module's own selftest, syn_fn_only.)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                             ast.ClassDef)):
            continue
        for sub in ast.walk(node):
            if (isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name)
                    and sub.func.id == "set_compute_dps"):
                return "set_compute_dps()"
            if isinstance(sub, ast.Assign):
                for t in sub.targets:
                    if isinstance(t, ast.Attribute) and t.attr == "dps":
                        v = getattr(sub.value, "value", None)
                        if isinstance(v, int) and v > 15:
                            return f"mp.dps={v}"
    return None


def _imported_modules(path) -> list:
    try:
        tree = ast.parse(pathlib.Path(path).read_text(encoding="utf-8",
                                                      errors="replace"))
    except Exception:
        return []
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and n.module:
            out.append(n.module.split(".")[0])
        elif isinstance(n, ast.Import):
            out.extend(al.name.split(".")[0] for al in n.names)
    return out


def classify_producer(script_file, index) -> str:
    """'A' (mpf real) / 'B' (float64-equivalent) / 'C' (producer not found).

    🛑 THIS IS A STATIC HEURISTIC AND IT CANNOT SETTLE THE QUESTION. Read
    before quoting its split (recorded 2026-08-29, after getting it wrong in
    both directions in one sitting).

    The A/B question is a RUNTIME property -- "did the mpf handed to the builder
    carry more than binary64's digits?" -- and no reading of the source answers
    it:

      * File-local reading misses precision that arrives from elsewhere.
      * So I added a one-hop import-cone check and reported 13 producers / 52
        fields as misfiled. THAT NUMBER WAS WRONG and is retracted. Its top
        entry inherited `set_compute_dps()` from `mass_at_3A_proper`, where the
        call sits INSIDE A FUNCTION under a docstring saying callers must
        invoke it themselves -- so importing raises nothing. The hits came from
        an `ast.walk` that descended into `def` bodies.
      * And the corrected version is not right either, only differently wrong:
        a function-level raiser IS a real raise when the producer calls it, and
        an import-side-effect test scores that as B.

    So this stays FILE-LOCAL, which is the cheap approximation, and the honest
    verdict lives at the drain: removing a cast and finding the emitted value
    round-trips exactly through float64 proves it was float64-equivalent no
    matter what the source looked like. Treat the A/B split below as a work
    ORDER, never as evidence about any single producer.
    """
    if not script_file:
        return "C"
    prod = index.get(os.path.basename(script_file))
    if prod is None:
        return "C"
    try:
        src = prod.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return "C"
    m = _DPS_RAISE.search(src)
    if not m:
        return "B"
    dps = m.group(1) or m.group(2)
    # `set_compute_dps(...)` matches with no numeric group -- it is the repo's
    # precision helper and always raises, so treat it as A.
    return "B" if (dps is not None and int(dps) <= 15) else "A"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="name every affected file")
    ap.add_argument("--field", choices=("computed", "expected", "both"), default="both")
    ap.add_argument("--by-precision", action="store_true",
                    help="split the population by whether the producer really "
                         "computes in mpf (A) or is float64-equivalent (B)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    fields = ("computed", "expected") if a.field == "both" else (a.field,)
    counts = collections.Counter()
    per_file: dict[str, int] = collections.Counter()
    index = _producer_index() if a.by_precision else {}
    bucket = collections.Counter()
    bucket_files = collections.defaultdict(collections.Counter)
    for p in glob.glob("computations/**/*.witness.json", recursive=True):
        if "_deprecated" in p:
            continue
        try:
            d = json.load(open(p))
        except Exception:
            counts["unparseable"] += 1
            continue
        if not isinstance(d, dict):
            continue
        here = 0
        for asrt in (d.get("assertions") or []):
            if not isinstance(asrt, dict):
                continue
            for k in fields:
                v = asrt.get(k)
                if isinstance(v, bool) or not isinstance(v, float):
                    continue
                if is_intlike(v):
                    counts[f"{k}: integral (excused, exact in binary64)"] += 1
                else:
                    counts[f"{k}: NON-integral (lost precision)"] += 1
                    per_file[p] += 1
                    here += 1
        if here and a.by_precision:
            cls = classify_producer(d.get("scriptFile"), index)
            bucket[cls] += here
            bucket_files[cls][d.get("scriptFile") or os.path.basename(p)] += here

    print("committed witnesses — .assertions[] value fields\n")
    for k in sorted(counts):
        print(f"  {k:<44} {counts[k]}")
    actionable = sum(v for k, v in counts.items() if "NON-integral" in k)
    print(f"\n  {'ACTIONABLE fields':<44} {actionable}")
    print(f"  {'files carrying at least one':<44} {len(per_file)}")

    if per_file:
        print("\n  worst offenders:")
        for p, n in per_file.most_common(10):
            print(f"    {n:>4}  {os.path.relpath(p)}")
    if a.list:
        print("\n  all affected files:")
        for p in sorted(per_file):
            print(f"    {per_file[p]:>4}  {os.path.relpath(p)}")

    if a.by_precision:
        _A = "A. dps RAISED — mpf real, the cast IS the defect  (repair as prescribed)"
        _B = "B. float64-equivalent — the prescribed fix would LAUNDER"
        _C = "C. producer not found"
        print("\n  BY PRODUCER PRECISION:")
        for key, lbl in (("A", _A), ("B", _B), ("C", _C)):
            print(f"    {bucket[key]:>5}  {lbl}")
        for key, lbl in (("B", "B — do NOT serialize more digits; fix precision upstream"),
                         ("A", "A — draining is correct here")):
            print(f"\n  top of bucket {lbl}:")
            for name, n in bucket_files[key].most_common(8):
                print(f"    {n:>4}  {name}")
        print("\n  🛑 The 'worst offenders' ranking above is DOMINATED BY B.")
        print("     Working it top-down starts in the bucket where the")
        print("     prescribed repair is wrong. Rank within A instead.")

    print("\nREADING: this is NOT drainable the way tolerance was. A `computed`")
    print("field is a measurement, so the repair changes the VALUE (it recovers")
    print("digits the cast threw away) and must happen at the producer -- one at")
    print("a time, with the producer re-run. `expected` is mixed and its")
    print("author-typed half could follow #5910's serialization argument; its")
    print("computed half cannot. Nothing here is a candidate for a textual sweep.")
    return 0


def selftest() -> int:
    """Pin the A/B discriminator against real files in the tree.

    A classifier whose two buckets have never been shown to separate is a
    classifier you cannot read a split from — and this one carries the whole
    work-order claim, so it needs more than "it ran".
    """
    import tempfile
    print("assertion_value_float64_triage --selftest")
    ok = True
    idx = _producer_index()

    cases = [
        ("channel_product_mass.py", "B",
         "the #1 offender: imports mpmath, never raises dps — and its import "
         "cone does not either, so the one-hop check must NOT rescue it"),
        ("probe_he4_canonical_tr_m_fingerprint.py", "A",
         "top of bucket A: dps genuinely raised"),
        ("probe_9b_laurent_degree_10a5.py", "B",
         "no dps raise of its own. A one-hop import check promoted it to A on "
         "mass_at_3A_proper's set_compute_dps() — which is INSIDE A FUNCTION, "
         "so importing raises nothing. Pinned as B to keep that retracted."),
    ]
    for name, want, why in cases:
        if name not in idx:
            print(f"  SKIP  {name} not in tree ({why})")
            continue
        got = classify_producer(name, idx)
        good = got == want
        ok &= good
        print(f"  {'PASS' if good else 'FAIL'}  {name} -> {got} (want {want}) — {why}")

    # Synthetic, so the discriminator is pinned independently of any file that
    # may later be fixed out from under this test.
    with tempfile.TemporaryDirectory() as td:
        mk = lambda n, s: (pathlib.Path(td, n).write_text(s), pathlib.Path(td, n))[1]
        syn = {
            "syn_none.py": ("B", "from mpmath import mp\nx = mp.log(2)\n"),
            "syn_low.py": ("B", "from mpmath import mp\nmp.dps = 15\n"),
            "syn_high.py": ("A", "from mpmath import mp\nmp.dps = 60\n"),
            "syn_helper.py": ("A", "from qou_substrate.precision import set_compute_dps\nset_compute_dps()\n"),
            # --- the one-hop import cone -------------------------------------
            "syn_dep_raises.py": (None, "from mpmath import mp\nmp.dps = 80\n"),
            "syn_dep_prose.py": (None,
                                 '"""Call `set_compute_dps()` yourself; this'
                                 ' module does not.\n\n`mp.dps = 100` is the'
                                 ' caller\'s job.\n"""\nX = 1\n'),
            "syn_dep_infn.py": (None,
                                "from mpmath import mp\n"
                                "def go():\n    mp.dps = 90\n"),
            # B, deliberately: the classifier is FILE-LOCAL. A one-hop import
            # check that promoted this to A was tried and retracted — see
            # classify_producer's note. Pinned so it is not silently re-added.
            "syn_inherits.py": ("B", "import syn_dep_raises\nx = 1\n"),
            "syn_prose_only.py": ("B", "import syn_dep_prose\nx = 1\n"),
            "syn_fn_only.py": ("B", "import syn_dep_infn\nx = 1\n"),
        }
        local = {n: mk(n, s) for n, (_, s) in syn.items()}
        for n, (want, _) in syn.items():
            if want is None:        # a dependency fixture, not a case
                continue
            got = classify_producer(n, local)
            good = got == want
            ok &= good
            print(f"  {'PASS' if good else 'FAIL'}  synthetic {n} -> {got} (want {want})")

    # A missing producer must be C, never silently A or B.
    got = classify_producer("definitely_not_a_real_producer_xyz.py", idx)
    good = got == "C"
    ok &= good
    print(f"  {'PASS' if good else 'FAIL'}  unknown producer -> {got} (want C)")

    print("selftest:", "OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
