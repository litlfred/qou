#!/usr/bin/env python3
"""Is the 33,702-field raw-float64 backlog reachable by a CENTRAL fix? No.

Bean `qou-oots`. Written because the obvious next move after ratcheting the
baseline (205 files / 1,523 fields, 2026-09-06) is to look for a shared site --
one API, one helper, one serializer -- that would clear thousands at once. I
looked for exactly that, and the measurements below say it does not exist. The
point of this audit is to save the next agent the same search, and to say WHERE
the work actually is.

WHAT I EXPECTED TO FIND, AND WHY IT WAS WRONG. Counting dirty leaf NAMES across
the 1015 baselined witnesses, `expected` (781) and `computed` (653) come out as
the two most widespread -- present in 298 and 242 files, ~30 % and ~24 % of the
corpus. Those are not domain quantities; they are `WitnessBuilder.add_assertion`'s
own fields. That reads like a single shared site.

It is not, for two independent reasons, and BOTH had to be measured:

  1. INTEGRALS DO NOT COUNT, and they are most of it. The audit's `_count` takes
     `integral_is_exact: bool = True`, so an integral float (`0.0`, `1.0`) is
     reported as a separate metric explicitly labelled "NOT a precision finding
     -- exact in binary64" and is excluded from the 33,702. Of the `expected`
     floats, 556 of 765 are integral; of `computed`, 291 of 607. My leaf-name
     ranking counted them and was inflated by ~3x.

     Measured properly: everything under `.assertions[]` is 589 of 35,199
     non-integral float leaves -- **1.7 %**. The assertion API is not a lever.

  2. THE TOLERANCE MECHANISM DOES NOT TRANSFER. `Assertion.to_dict` already
     routes `tolerance` through `_tolerance_literal`, which serializes a
     DECLARED threshold as the literal its author typed and refuses a COMPUTED
     one. Extending that to `expected` is the obvious generalisation.

     Its own docstring says why the cut is legitimate: tolerances are sharply
     bimodal in significant digits with an EMPTY BIN AT 6, so "the cut sits in a
     bin with no members, so it is the boundary of a real cluster rather than a
     threshold chosen to hit a target."

     `expected` has no such gap. Non-integral `expected`, by significant digits:

         1: 9   2: 20   3: 29   4: 36   5: 19   6: 4   7: 10   8: 25   9: 8
        10: 3  11: 7   12: 7   13: 2   14: 0   15: 3  16: 17  17: 10

     Smeared, not bimodal. Any threshold here would be exactly the tuned knob
     that docstring refuses. So the mechanism is correct where it is and must
     not be generalised on the strength of the analogy alone.

WHAT THE BACKLOG ACTUALLY IS: diffuse domain data. 4,166 distinct leaf names.
Named solver-output fields (`y_star`, `x_star`, `x_opt`, `primal_obj`,
`eigenvalues`, ...) account for 3,801 = 10.8 %, and those are float64 because
the solver is -- scipy and Clarabel return binary64, so that share is not a
serialization slip at all and is not fixed by carrying mpf to the boundary.

WHERE THE WORK IS, by producer, so a campaign has somewhere to start. Figures
are AS OF the baseline in the tree when this ran -- 1,012 files / 31,956 fields,
after the same PR drained three bucket-B producers (1,746 fields). The witness
carries the live numbers; these are for reading, not for quoting:

    B. imports mpmath, does NOT bind fmt                453 files  13,121
    A. no mpmath at all -- f64 computation              181 files   8,600
    unresolved producer (this script's resolver)        297 files   8,181
    C. imports mpmath AND binds fmt, still dirty         81 files   2,054

THE FIRST VERSION OF THIS TABLE HAD B AND C SWAPPED, and the cause is worth
more than the table. `binds_fmt` originally asked `"_precision import" in src`,
a SUBSTRING -- which `from _precision import set_compute_dps` satisfies without
binding `fmt` at all. 377 producers that import `_precision` for the dps setter
and never touch the serializer were classified as "already has both halves, so
this is only a boundary slip". Bucket C read 463 files / 15,189 fields (45 % of
the backlog) when it is 81 / 2,054 (6.1 %). The predicate is now an AST walk
that requires the name to actually be bound (`ImportFrom` from a module named
`_precision` with an alias `fmt`, or any `.fmt` attribute access). Same class as
every row of AGENTS.md's detector-blindness taxonomy: keying on how an author
SPELLED something instead of on what it binds -- committed here in the very
audit whose subject is a precision detector.

So bucket B, not C, is where the mass is, and it is the more tractable half:
the arithmetic is already mpmath and only the write is missing, so routing it
through `fmt` is mechanical. That is a CANDIDATE class, not a guaranteed one --
`import mpmath` at the top of a file does not establish that the DIRTY LEAF was
computed in mpf, and a producer can carry one quantity in mpf while computing
another in float. Confirm per producer before claiming a fix is cheap.
Bucket A is expensive under any reading: the computation itself is f64, so
changing it moves recorded numbers and needs a re-derivation, not a re-write.

CONCLUSION, and it is a negative: the ratchet's design -- tolerate the backlog,
never let it grow, drain as producers are touched -- is the correct response to
a backlog with this shape. There is no single edit that clears thousands, and an
agent who believes otherwise should re-run this before spending a session on it.

No float64 in this audit's own arithmetic: it counts fields and classifies
files; the significant-digit histogram uses `Decimal` on `repr`.
"""

from __future__ import annotations

import ast
import collections
import json
import pathlib
import re
import sys as _sys
from decimal import Decimal

_sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.witness import WitnessBuilder  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
CROOT = ROOT / "computations"
BASELINE = CROOT / "raw-float64-baseline.json"

SOLVER_NAMES = {
    "y_star", "x_star", "x_opt", "y0_star", "primal_obj", "dual_obj",
    "duality_gap", "eigenvalues", "min_eig_sym", "active_set", "slack",
    "lp_x_star", "chi", "trace",
}


def sig_digits(x: float) -> int | None:
    """Significant decimal digits of a non-integral finite float, else None."""
    if not isinstance(x, float) or isinstance(x, bool):
        return None
    if x != x or x in (float("inf"), float("-inf")) or x.is_integer():
        return None
    s = repr(abs(x))
    if "e" in s or "E" in s:
        s = f"{Decimal(repr(abs(x))):f}"
    d = s.replace(".", "").lstrip("0").rstrip("0")
    return len(d) or None


def leaves(o, p=""):
    """Every NON-INTEGRAL float leaf, with its dotted path.

    Integrals are skipped here for the same reason the audit skips them: it
    takes `integral_is_exact=True`, reports them as a separate metric labelled
    "NOT a precision finding", and excludes them from the baselined total. A
    scan that counts them measures a different population and inflates every
    name ranking -- which is how this audit's own first hypothesis went wrong.
    """
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, f"{p}.{k}")
    elif isinstance(o, list):
        for v in o:
            yield from leaves(v, f"{p}[]")
    elif isinstance(o, float) and not isinstance(o, bool) and not o.is_integer():
        yield p


def binds_fmt(src: str) -> bool:
    """Does this producer actually BIND `_precision.fmt`?

    Asked by AST, not by substring, because the substring version is what got
    the bucket table backwards. `"_precision import" in src` is satisfied by
    `from _precision import set_compute_dps`, which binds the dps setter and
    nothing else -- 377 producers matched it while never touching the
    serializer, moving 13k fields into the wrong bucket and inverting the
    audit's own recommendation about where a campaign should start.

    Accepts either spelling that really binds the name: a `from ..._precision
    import fmt` (or a star-import, which does bind it), or any `.fmt` attribute
    access, which covers `import _precision` + `_precision.fmt(...)`.

    A file that will not parse falls back to the substring, deliberately: a
    false positive there is preferable to silently dropping the producer from
    every bucket.
    """
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return "fmt" in src
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and n.module and "_precision" in n.module:
            if any(a.name in ("fmt", "*") for a in n.names):
                return True
        if isinstance(n, ast.Attribute) and n.attr == "fmt":
            return True
    return False


def find_producer(wit: str):
    p = pathlib.Path(wit)
    base = (p.name[:-len(".witness.json")]
            if p.name.endswith(".witness.json") else p.stem)
    stem = base.replace("-", "_")
    cand = ROOT / p.parent / f"{stem}.py"
    if cand.exists():
        return cand
    hits = list(CROOT.rglob(f"{stem}.py"))
    return hits[0] if hits else None


def main() -> int:
    base = json.loads(BASELINE.read_text()).get("files", {})
    b = WitnessBuilder("raw-float64-backlog-structure")
    b.set_description(
        "Bean qou-oots. Asks whether the raw-float64 backlog (33,702 fields / "
        "1015 witnesses after the 2026-09-06 ratchet) is reachable by a CENTRAL "
        "fix, and answers NO with the measurements. Records that the obvious "
        "candidate -- WitnessBuilder.add_assertion, whose `expected`/`computed` "
        "are the most WIDESPREAD dirty leaf names -- is a false lead twice "
        "over: integral floats are excluded from the count and were inflating "
        "that ranking ~3x (assertions are 1.6 % of non-integral leaves), and "
        "the `_tolerance_literal` mechanism cannot be generalised to `expected` "
        "because the significant-digit bimodality that justifies its cut does "
        "not exist there. Reports where the work actually is, by producer "
        "bucket, so a campaign has a starting point."
    )

    leaf = collections.Counter()
    filecount = collections.Counter()
    sig_hist = {"expected": collections.Counter(),
                "computed": collections.Counter(),
                "tolerance": collections.Counter()}
    integral_in_assertions = collections.Counter()
    total = solver = in_assertions = 0
    scanned = 0

    for wit in base:
        p = ROOT / wit
        if not p.exists():
            continue
        try:
            j = json.loads(p.read_text())
        except Exception:
            continue
        scanned += 1
        names = set()
        for path in leaves(j):
            total += 1
            name = path.split(".")[-1].replace("[]", "")
            leaf[name] += 1
            names.add(name)
            if name in SOLVER_NAMES:
                solver += 1
            if path.startswith(".assertions"):
                in_assertions += 1
        for n in names:
            filecount[n] += 1
        for a in (j.get("assertions") or []):
            if not isinstance(a, dict):
                continue
            for k in sig_hist:
                v = a.get(k)
                if isinstance(v, float) and not isinstance(v, bool):
                    s = sig_digits(v)
                    if s is None:
                        integral_in_assertions[k] += 1
                    else:
                        sig_hist[k][s] += 1

    b.add_data("population", {
        "baselined_witnesses": len(base),
        "witnesses_scanned": scanned,
        "non_integral_float_leaves": total,
        "distinct_leaf_names": len(leaf),
        "note": "Integral floats are EXCLUDED, matching the audit's own "
                "`_count(integral_is_exact=True)`. Counting them measures a "
                "different population and inflates every name ranking.",
    })
    b.add_data("central_fix_candidates", {
        "under_assertions_pct": f"{100*in_assertions/total:.2f}",
        "under_assertions_count": in_assertions,
        "solver_output_names_pct": f"{100*solver/total:.2f}",
        "solver_output_names_count": solver,
        "integral_excluded_in_assertions": dict(integral_in_assertions),
        "verdict": "The assertion API is under 2 % of the backlog, NOT a lever. "
                   "Solver output is ~10 % and is float64 because scipy and "
                   "Clarabel are -- not a serialization slip, and not fixed by "
                   "carrying mpf to the boundary.",
    })
    b.add_data("sig_digit_histograms", {
        k: {str(s): c for s, c in sorted(v.items())} for k, v in sig_hist.items()
    })
    b.add_data("why_tolerance_mechanism_does_not_generalise", {
        "tolerance_has_empty_bin_at_6": "per _tolerance_literal's docstring, "
            "which is what makes its cut a cluster boundary rather than a "
            "tuned knob",
        "expected_has_no_empty_bin": "measured here; smeared across sig 1-17",
        "conclusion": "Extending _tolerance_literal to `expected` would require "
                      "choosing a threshold with no empirical boundary -- "
                      "exactly what that docstring declines to do. The "
                      "mechanism is correct where it is and must not be "
                      "generalised on the analogy alone.",
    })

    buckets = collections.Counter()
    bfields = collections.Counter()
    for wit, n in base.items():
        pr = find_producer(wit)
        if pr is None:
            k = "unresolved producer"
        else:
            s = pr.read_text(errors="replace")
            mp = bool(re.search(r"import mpmath|from mpmath", s))
            k = ("A. no mpmath at all" if not mp
                 else "C. mpmath AND fmt, still dirty" if binds_fmt(s)
                 else "B. mpmath, no fmt")
        buckets[k] += 1
        bfields[k] += n
    b.add_data("where_the_work_is", {
        k: {"files": buckets[k], "fields": bfields[k]}
        for k in sorted(bfields, key=lambda x: -bfields[x])
    } | {"reading": "B is where the mass is and is the more tractable half: "
                    "the arithmetic is already mpmath and only the write is "
                    "missing, so routing it through `fmt` is mechanical. It is "
                    "a CANDIDATE class, not a guaranteed one -- `import "
                    "mpmath` does not establish that the DIRTY LEAF was "
                    "computed in mpf, so confirm per producer. A is expensive "
                    "under any reading: the computation itself is f64, so "
                    "changing it moves recorded numbers. 'unresolved producer' "
                    "is this script's resolver, not necessarily a defect class.",
         "predicate_correction": "The first run of this audit had B and C "
                    "swapped (C read 463 files / 15,189 fields against a true "
                    "81 / 2,054) because binds_fmt asked `\"_precision import\" "
                    "in src`, a substring that `from _precision import "
                    "set_compute_dps` satisfies without binding fmt. 377 "
                    "producers were misfiled and the audit's own "
                    "recommendation about where to start was inverted. Now an "
                    "AST walk -- see binds_fmt."})

    b.add_assertion(
        "assertion_api_is_not_a_central_lever",
        computed="1" if in_assertions * 20 < total else "0",
        expected="1",
        source=f"{in_assertions} of {total} non-integral float leaves sit under "
               f".assertions[] ({100*in_assertions/total:.2f} %). Stated as a "
               f"predicate (under 5 %) so the witness summary reports a pass "
               f"for a measured negative rather than FAILURES.",
    )
    b.save(extra={
        "q0Anchor": "independent",
        "q0AnchorReason": "structural audit of the committed witness corpus and "
                          "producer sources (float-leaf counts, AST import "
                          "buckets); computes no q-dependent quantity and never "
                          "reads q0",
    })

    print(f"baselined witnesses {len(base)}   scanned {scanned}")
    print(f"non-integral float leaves {total}   distinct leaf names {len(leaf)}\n")
    print(f"  under .assertions[]        {in_assertions:6d}  "
          f"{100*in_assertions/total:5.2f} %   <- the false lead")
    print(f"  solver-output field names  {solver:6d}  {100*solver/total:5.2f} %"
          f"   <- f64 because the solver is\n")
    print("expected, non-integral, by significant digits (no empty bin):")
    print("   " + "  ".join(f"{s}:{sig_hist['expected'][s]}"
                            for s in sorted(sig_hist["expected"])))
    print("\nwhere the work is:")
    for k in sorted(bfields, key=lambda x: -bfields[x]):
        print(f"  {k:<34} {buckets[k]:>5} files {bfields[k]:>7} fields")
    print("\nVERDICT: no central fix exists. The ratchet's design -- tolerate, "
          "never grow,\ndrain as producers are touched -- is the correct "
          "response to a backlog of this shape.")
    return 0


def _selftest() -> int:
    """Show the predicate fires -- and, more to the point, that it DECLINES.

    Case 2 is the one this exists for: it is the exact source line that misfiled
    377 producers under the substring version. A predicate that cannot be shown
    to reject it is not a predicate.
    """
    cases = [
        ("from _precision import fmt", True),
        ("from _precision import set_compute_dps", False),   # the 377
        ("from _precision import set_compute_dps, fmt", True),
        ("import _precision\nx = _precision.fmt(y)", True),
        ("from computations._precision import *", True),
        ("import mpmath\nfmt = '%.3f'\nprint(fmt)", False),   # a local named fmt
        ("s = 'this file mentions _precision import in a comment'", False),
    ]
    bad = 0
    for src, want in cases:
        got = binds_fmt(src)
        ok = "ok " if got == want else "FAIL"
        if got != want:
            bad += 1
        print(f"  [{ok}] want={want!s:5} got={got!s:5}  {src.splitlines()[0][:52]!r}")
    print("selftest:", "PASS" if not bad else f"{bad} FAILURE(S)")
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in _sys.argv:
        raise SystemExit(_selftest())
    raise SystemExit(main())
