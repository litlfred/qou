#!/usr/bin/env python3
"""witness_raw_float64_audit.py — raw float64 in committed witnesses.

WHAT THIS GATES, AND WHY IT IS NOT THE PADDING AUDIT
----------------------------------------------------

AGENTS.md states the rule broadly: *"NO-FLOAT64 means none may enter a
witness."*  `witness_float64_padding_audit.py` does not enforce that rule.
It enforces a narrower and different one: **fake precision** — a float64
serialized past ~17 digits so that binary-expansion garbage reads as exact.

A witness that stores float64 *at float64 width* is honest about being f64
and sails through the padding audit. It still violates the stated rule.

That gap is not hypothetical. `jpsi-boundstate-mass.witness.json` reached
`main` carrying **30 raw float64 fields** with the padding audit green
(13/13, NEW 0) — the merge's other gates (content validation, Lean,
reproducibility) do not look at precision at all. Two of those fields were
not merely imprecise but wrong about what they were: a Chern-Simons value
that is exactly `-1/12` was stored as `-0.08333333333333312`, and one that
is exactly `0` (the braid is amphichiral — a structural fact) was stored as
`8.324194211187791e-16`, indistinguishable from a noise floor.

WHAT THIS DOES — AND DELIBERATELY DOES NOT DO
----------------------------------------------

It does **not** drain anything. Draining raw float64 at the producer is
PR #4677's work: an entry tracer that patches mpmath's `from_float` to read
entry lines directly, which localized the residual to three library-level
source lines rather than eighteen independent bugs.

This is the **ratchet** that stops the class growing while that drain runs.
The existing backlog is large — 1586 of 2404 live witnesses, 542,034 fields
— so it is recorded in `raw-float64-baseline.json` and tolerated, exactly as
the padding audit tolerates its own backlog. Under `--strict`:

  * a witness **not** in the baseline that carries raw float64 fails —
    this is the case that would have caught the J/psi probe;
  * a baselined witness whose count **increases** fails.

Counts can shrink, never grow. A file that drains to zero, or disappears,
is progress and is reported as such.

BASELINE GRANULARITY
--------------------

Per-FILE with a count, not per-field. Per-field would mean a 542,034-key
baseline — unreviewable, and it would churn on every legitimate re-run
since field paths move. Per-file counts are compact, and they carry the
ratchet just as well: the quantity that must not grow is how much float64
a given witness carries.

THE FIX IS AT THE PRODUCER, NEVER THE WITNESS
----------------------------------------------

Do not hand-edit a number, and do not add a file to the baseline to silence
it. Carry the value as `mpmath.mpf` from its source and serialize it with
`_precision.fmt`; see `jpsi_boundstate_mass_probe.py` for a worked
conversion, including the case where a library (SnapPy) has its own
precision ceiling that must be recorded rather than assumed.

Output: `witness-raw-float64-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASELINE = HERE / "raw-float64-baseline.json"


def _baseline_path(scan_root: "Path | None") -> "Path":
    """Baseline file for a run — DERIVED from the scan root, never shared.

    Exactly the `_output_name` defect (qou-pgdw) one step removed, and it is
    why the audits-tree gate could not be made blocking. The OUTPUT name was
    scoped when that bug was fixed; the BASELINE was left global, so the
    advisory `--scan-root docs/audits/scripts` run reads a baseline whose 1572
    entries are all `computations/` paths and therefore contains none of its
    own. Every witness under that tree is reported NEW on every run, forever —
    not because anything regressed, but because the ratchet has no memory for
    that tree.

    A ratchet with no memory cannot be blocking: it is red on arrival, and a
    gate that is red on arrival gets skipped, which is how a checker goes quiet
    (the rule this file's own header states). Giving each scan root its own
    baseline is what makes "no NEW dirty here" a question the gate can answer.

    This does NOT grow `raw-float64-baseline.json`. It is a separate file for a
    tree that was previously outside the discipline altogether; the corpus
    baseline is untouched and still drains-only.
    """
    if scan_root is None:
        return BASELINE
    slug = scan_root.relative_to(ROOT).as_posix().strip("/").replace("/", "-")
    return HERE / f"raw-float64-baseline--{slug}.json"

# These audits embed findings — including float values — in their own
# witnesses, so scanning them re-detects the audit's own output every run.
# Same exclusion the padding audit makes, for the same reason.
SELF_OUTPUTS = {
    "witness-raw-float64-audit.witness.json",
    "witness-float64-padding-audit.witness.json",
    "q0-value-drift-audit.witness.json",
    "no-free-parameter-certificate.witness.json",
}

# Prefix covering this audit's per-scan-root outputs (see `_output_name`), so a
# derived advisory witness is self-excluded exactly like the default one. The
# double dash is what separates the family from the plain
# `witness-raw-float64-audit.witness.json`, which does NOT match this prefix and
# stays covered by SELF_OUTPUTS above.
SELF_OUTPUT_PREFIX = "witness-raw-float64--"

# Every derived name must still end in this, because it is what the repo-wide
# audit-self-output convention keys on: `AUDIT_SUFFIXES` in
# `computations/audits/q0_anchor_consistency_audit.py` classifies a witness as
# Q0_AUDIT_EXEMPT by SUFFIX, not by prefix. A derived name ending in the scan
# slug (…--docs-audits-scripts.witness.json) misses that suffix and gets filed
# as Q0_ANCHOR_MISSING instead — measured: 1889 -> 1890, with this audit's own
# output sitting in the "no q0 anchor declared" inventory while its identically
# generated sibling is exempt. Keeping the suffix keeps the two consistent and
# needs no special case in the other audit.
AUDIT_SUFFIX = "-audit.witness.json"


def _output_name(scan_root: Path | None) -> str:
    """Output filename for a run — DERIVED from the scan root, never shared.

    Both `precision-gates.sh` invocations used to write the same file: the
    gating run (full corpus) at line 63, then the narrow advisory run
    (`--scan-root docs/audits/scripts`) which OVERWROTE it. The committed
    witness was left reading `dirty_witnesses 1561 -> 5`,
    `drained_files 14 -> 1572`, with every carve-out record dropped.

    That is not merely wrong, it is wrong in a shape that reads as a normal
    staleness prompt — "a count moved, commit the regenerated witness" — so
    committing it would swap a corpus-wide audit for a five-file one and drain
    the carve-out records. Deriving the name (rather than adding an --out flag
    someone must remember to pass) makes the collision impossible for any
    future scan root too. Bean qou-pgdw.

    The slug is infixed rather than appended so the name still ends in
    `AUDIT_SUFFIX` — see the note there for why the suffix is load-bearing.
    """
    if scan_root is None:
        return f"witness-raw-float64{AUDIT_SUFFIX}"
    slug = scan_root.relative_to(ROOT).as_posix().strip("/").replace("/", "-")
    return f"{SELF_OUTPUT_PREFIX}{slug}{AUDIT_SUFFIX}"


# ── LP-dual carve-out (bean qou-ftuv, owner decision 2026-08-11) ─────────
#
# THIS IS A CARVE-OUT AND IS NAMED AS ONE. It is not a precision improvement
# and it does not drain anything; it declares a class of fields out of scope.
#
# These are the primal/dual variables of the operator-selection LP/SDP, i.e.
# raw solver output. On the scipy path the solver IS float64 — there is no
# `mpmath.mpf` upstream to carry, so the standing fix ("carry mpf from the
# source, serialize with `_precision.fmt`") has nothing to act on. And they
# cannot simply become strings: `lp_dual_solver.to_dict()` documents that every
# existing consumer does arithmetic on them, so stringifying breaks readers
# silently rather than loudly.
#
# Deliberately NARROW. It names seven fields and nothing else. In
# `a-K-via-lp-dual-full` these account for 801 of 867 floats; the remaining ~66
# are the probe's OWN results (`a_K_via_lp_dual`, `dual_vs_C_ppm`, `tolerance`,
# …), which are not solver output and stay counted — a producer-level fix is
# the right treatment for those, and this carve-out must not hide them.
#
# Every excused field is COUNTED and REPORTED as `carved_out`. A carve-out that
# cannot be seen is indistinguishable from a hole.
LP_DUAL_F64_FIELDS = frozenset({
    "x_star", "y_star", "y0_star", "u_lambda_star",
    "primal_obj", "dual_obj", "duality_gap",
})

# ── float64-integrator carve-out (qou-7kq3, owner-approved 2026-08-15) ──
#
# The sibling of the LP-dual carve-out, for the same reason: output that is
# f64 BY CONSTRUCTION, with no higher-precision source to carry from.
#
# The q-NS shell-model probes integrate an ODE system with float64 RK2 and say
# so in their own docstrings ("Precision tier: float64 RK2, adaptive nonlinear
# CFL"). For those, the standing instruction — "carry mpmath.mpf from the
# source and serialize with _precision.fmt" — has no source: the integrator IS
# the source. Stringifying would dress an f64 number as preserved precision,
# which is what that instruction exists to prevent; rewriting the integrator in
# mpmath would make it a different object at prohibitive cost.
#
# DELIBERATELY NOT keyed on `tier: exploratory`. That marker is worn by many
# probes that are not integrators, and carving on it would let this quietly
# widen to cover ordinary f64 sloppiness — the failure mode a carve-out has to
# be designed against. A producer must opt in EXPLICITLY by declaring
#
#     w.add_data("precision_tier", "float64-integrator")
#
# so the excuse is a claim its author made on the record, not a property the
# auditor inferred.
#
# Every excused field is COUNTED and REPORTED separately from the LP-dual
# total. A carve-out that cannot be seen is indistinguishable from a hole.
F64_INTEGRATOR_TIER = "float64-integrator"


def _declares_f64_integrator(doc) -> bool:
    """Has this witness explicitly claimed the float64-integrator tier?"""
    if not isinstance(doc, dict):
        return False
    for holder in (doc, doc.get("data"), doc.get("result")):
        if isinstance(holder, dict) and \
                holder.get("precision_tier") == F64_INTEGRATOR_TIER:
            return True
    return False


# ── deprecated-float64 carve-out (owner ruling 2026-08-15) ────────────────
#
# A THIRD carve-out, and deliberately not a widening of the one above.
#
# The owner's rule: "mpmath on anything in production; if not production,
# deprecate it with precision_tier = float64." Walking the
# production-vs-exploratory decision tree, a producer that reaches none of the
# named production locations (m_p_borromean_verification_50dps, mass_table_ppb,
# codata_constants, the two dashboards, the canonical mass/binding facades) is
# EXPLORATORY, and an exploratory f64 probe is not worth an mpmath rewrite.
#
# Why it is NOT `float64-integrator`. That tier means f64 BY CONSTRUCTION with
# no higher-precision source to carry from — an ODE integrator IS the source.
# These producers are the opposite: a 50-dps source exists (q_0, h from
# q_parameter) and numpy was simply cheaper for the matrix algebra. Filing them
# under `float64-integrator` would be exactly the "ordinary f64 sloppiness"
# that carve-out's own comment says it must be designed against. They get their
# own name so the two reasons never blur.
#
# Opt-in requires BOTH fields, on the record:
#
#     w.add_data("precision_tier", "float64")
#     w.add_data("deprecated", {"reason": ..., "not_production": ...})
#
# `precision_tier: "float64"` alone excuses nothing — otherwise any producer
# could silence the ratchet by naming its own sloppiness. The `deprecated`
# field is what makes it a retirement rather than an excuse, and it must say
# WHY the producer is not production so a reader can check the claim against
# the decision tree instead of taking it on faith.
#
# Counted and reported separately, like the other two. A carve-out that cannot
# be seen is indistinguishable from a hole.
F64_DEPRECATED_TIER = "float64"


def _declares_deprecated_f64(doc) -> bool:
    """Has this witness declared BOTH the float64 tier and its deprecation?"""
    if not isinstance(doc, dict):
        return False
    for holder in (doc, doc.get("data"), doc.get("result")):
        if not isinstance(holder, dict):
            continue
        if holder.get("precision_tier") == F64_DEPRECATED_TIER \
                and holder.get("deprecated"):
            return True
    return False

# A binary64 carries at most 17 significant decimal digits. A `*_str`
# companion is only a genuine full-precision shadow if it carries MORE than
# that — otherwise it is just the same f64 spelled as text.
_F64_SIG_DIGITS = 17


def _sig_digits(s: str) -> int:
    """Significant decimal digits in a numeric string ('1.20e-3' -> 3)."""
    mantissa = s.strip().lstrip("+-").split("e")[0].split("E")[0]
    return len(mantissa.replace(".", "").lstrip("0"))


def _is_full_precision_shadow(value, companion) -> bool:
    """Is `companion` a `*_str` carrying MORE precision than `value`?

    The guard on `_sig_digits` is the whole point, and it is not optional.
    Without it the rule is a laundering hole: any producer could silence the
    ratchet by emitting `x_str = str(x)` beside its f64 and claiming a shadow.
    That is not hypothetical — bean `qou-t0rf` records exactly that bug, where
    `_lp_result_from_dict` built `*_str` from the f64 key, so every `*_str`
    since was "f64 wearing a string". A shadow rule that accepted those would
    have certified the bug as a fix.

    So a companion counts only when it demonstrably carries digits the double
    could not hold.
    """
    if isinstance(value, float) and isinstance(companion, str):
        return _sig_digits(companion) > _F64_SIG_DIGITS
    if isinstance(value, list) and isinstance(companion, list):
        if not value or len(value) != len(companion):
            return False
        pairs = list(zip(value, companion))
        if not all(isinstance(v, float) and isinstance(c, str) for v, c in pairs):
            return False
        return all(_sig_digits(c) > _F64_SIG_DIGITS for _, c in pairs)
    return False


def count_raw_floats(obj) -> int:
    """Number of JSON numbers parsed as float (i.e. non-integer literals).

    JSON integers arrive as Python `int`, so this counts exactly the
    values written with a decimal point or an exponent — the float64
    payload. `bool` is a subclass of `int` and so is never counted.

    SHADOW RULE (bean `qou-ftuv`, owner decision 2026-08-11). An f64 that sits
    beside a `<key>_str` companion carrying more than 17 significant digits is
    a **shadow, not a defect**: the value IS present at full precision in the
    same witness, and the float is a convenience for consumers that do
    arithmetic on it. `lp_dual_solver.to_dict()` emits exactly this pair and
    documents why the float cannot simply become a string — every existing
    consumer computes on it (`sum(r["y_star"] …)`, `r["duality_gap"] < 1e-6`),
    so stringifying would break readers silently rather than loudly.

    This does NOT weaken the ratchet. A shadow must prove itself by carrying
    digits a double cannot hold; see `_is_full_precision_shadow`.
    """
    return _count(obj)[0]


def count_carved(obj) -> int:
    """How many f64 the LP-dual carve-out excused. Reported, never silent."""
    return _count(obj)[1]


def _count(obj) -> tuple[int, int]:
    """(counted, carved_out) — one traversal, both numbers."""
    if isinstance(obj, dict):
        total = carved = 0
        for k, v in obj.items():
            if k.endswith("_str"):
                t, c = _count(v)
                total += t
                carved += c
                continue
            companion = obj.get(f"{k}_str")
            if companion is not None and _is_full_precision_shadow(v, companion):
                continue  # shadowed at full precision — not raw float64
            if k in LP_DUAL_F64_FIELDS:
                carved += _count(v)[0]
                continue  # carve-out: solver output, f64 by construction
            t, c = _count(v)
            total += t
            carved += c
        return total, carved
    if isinstance(obj, list):
        total = carved = 0
        for v in obj:
            t, c = _count(v)
            total += t
            carved += c
        return total, carved
    return (1 if isinstance(obj, float) else 0), 0


CARVED: dict[str, int] = {}
#: Per-file tally for the float64-integrator carve-out, kept SEPARATE from
#: `CARVED` so the two excuses can never be read as one number.
CARVED_INTEGRATOR: dict[str, int] = {}
CARVED_DEPRECATED: dict[str, int] = {}


def scan(scan_root: Path | None = None) -> dict[str, int]:
    """{repo-relative path: raw float64 count} for every live witness.

    Also populates the module-level `CARVED` with what the LP-dual carve-out
    excused per file, so `main` can report it. A carve-out is only defensible
    while it is visible.
    """
    found: dict[str, int] = {}
    CARVED.clear()
    CARVED_INTEGRATOR.clear()
    CARVED_DEPRECATED.clear()
    for p in sorted((scan_root or HERE).rglob("*.witness.json")):
        if (p.name in SELF_OUTPUTS
                or p.name.startswith(SELF_OUTPUT_PREFIX)
                or "_deprecated" in p.parts):
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        n, carved = _count(d)
        rel = p.relative_to(ROOT).as_posix()
        # An explicit float64-integrator declaration moves this file's REMAINING
        # count into the integrator carve-out. Applied at witness level, not
        # field level, because an integrator's output has no fixed field names —
        # which is exactly why it needs a producer's on-the-record claim rather
        # than a name list.
        if n and _declares_f64_integrator(d):
            CARVED_INTEGRATOR[rel] = n
            n = 0
        # Same witness-level application for the deprecated-exploratory tier.
        # Checked AFTER the integrator tier so a producer that (wrongly) claims
        # both is counted under the narrower, better-justified one.
        if n and _declares_deprecated_f64(d):
            CARVED_DEPRECATED[rel] = n
            n = 0
        if n:
            found[rel] = n
        if carved:
            CARVED[rel] = carved
    return found


def self_test() -> int:
    """Prove the detector fires, and does not fire on the exempt shapes.

    Asserted rather than assumed: a gate that cannot be shown to FAIL on a
    violation is indistinguishable from a no-op.
    """
    cases = [
        # (payload, expected raw-float64 count)
        ({"v": 1.5}, 1),                                  # plain float
        ({"v": 128.04411076744893}, 1),                   # the J/psi shape
        ({"v": 8.324194211187791e-16}, 1),                # exponent form
        ({"v": 1.0}, 1),                                  # integral-valued float
        ({"v": -0.08333333333333312}, 1),                 # negative
        ({"v": "1.5"}, 0),                                # string — the fix
        ({"v": 3}, 0),                                    # int
        ({"v": True}, 0),                                 # bool is not a float
        ({"v": None}, 0),
        ({"a": [1.5, 2.5], "b": {"c": 3.5}}, 3),          # nested
        ({"a": ["1.5", {"c": "3.5"}]}, 0),                # nested, serialized
        ({}, 0),

        # ── shadow rule (qou-ftuv) ────────────────────────────────────
        # An f64 beside a *_str carrying MORE than 17 significant digits is
        # the value at full precision, not a defect.
        ({"y0_star": 0.012246289813934,
          "y0_star_str": "1.224628981393451974336267854072680408e-2"}, 0),
        # Same, for the list shape the LP duals actually use.
        ({"y_star": [0.5, 0.25],
          "y_star_str": ["5.000000000000000000000000000000e-1",
                         "2.500000000000000000000000000000e-1"]}, 0),

        # ── the laundering guard, which is the point ──────────────────
        # A *_str that is merely the f64 spelled as text proves nothing and
        # must still count. This is the qou-t0rf bug shape: *_str built from
        # the f64 key. If this case ever returns 0, the rule has become a
        # bypass and the ratchet is defeated.
        ({"v": 0.1, "v_str": "0.1"}, 1),
        ({"v": 0.012246289813934, "v_str": "0.012246289813934"}, 1),
        # Length mismatch is not a shadow.
        ({"v": [0.5, 0.25],
          "v_str": ["5.00000000000000000000000000e-1"]}, 2),
        # A *_str beside a non-float is irrelevant, and must not crash.
        ({"v": "x", "v_str": "5.0000000000000000000000000e-1"}, 0),

        # ── LP-dual carve-out (qou-ftuv route 3) ──────────────────────
        # Named solver-output fields are excused...
        ({"y_star": [0.5, 0.25], "duality_gap": 1e-9}, 0),
        ({"x_star": [1.0], "y0_star": 0.5, "primal_obj": 2.5}, 0),
        # ...and NOTHING else in the same witness is. This is the
        # discrimination that keeps the carve-out narrow: a-K's own results
        # (a_K_via_lp_dual, dual_vs_C_ppm, tolerance) are not solver output
        # and must still count.
        ({"y_star": [0.5], "a_K_via_lp_dual": 1.5, "tolerance": 1e-9}, 2),
        # A same-named key nested anywhere is still solver output.
        ({"per_atom": [{"lp_dual": {"y_star": [0.5, 0.25]}}]}, 0),
    ]
    bad = [(p, e, count_raw_floats(p)) for p, e in cases
           if count_raw_floats(p) != e]
    if bad:
        print("SELF-TEST FAILED:")
        for p, e, g in bad:
            print(f"   {p}  expected {e}, got {g}")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases: raw float64 detected in "
          "plain/exponent/nested/negative form; strings, ints and bools not "
          "flagged; an f64 with a >17-digit *_str companion treated as a "
          "shadow, and one with a same-precision *_str still counted (the "
          "laundering guard).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument(
        "--scan-root", default=None, metavar="DIR",
        help="directory to scan instead of computations/ (repo-relative). "
             "The baseline is keyed on computations/ paths, so any OTHER root "
             "reports every dirty file as NEW — that is honest for a "
             "previously-unscanned tree, but it means such a run belongs in "
             "precision-gates.sh as ADVISORY, never blocking, until the files "
             "are drained. Do NOT rebaseline against a different root: it "
             "would grow the baseline, which the discipline forbids "
             "(bean qou-irzg).")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on a NEW dirty witness or an INCREASED count")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (draining only — totals must go DOWN)")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    scan_root = (ROOT / args.scan_root).resolve() if args.scan_root else None
    if scan_root is not None:
        if not scan_root.is_dir():
            print(f"--scan-root: not a directory: {scan_root}")
            return 2
        # --rebaseline WITH --scan-root used to be refused outright: the write
        # would have put that root's dirty files into a baseline keyed on
        # computations/ paths, growing it, and baselines drain-never-grow.
        #
        # It is now permitted, because `_baseline_path` sends it to that root's
        # OWN file. The corpus baseline is unreachable from a non-default root,
        # so the thing the refusal protected cannot happen. What this enables is
        # ESTABLISHING coverage over a tree that had none — which is a different
        # act from silencing a regression in a tree that already has it, and is
        # the only way the ratchet can hold a line here at all.
        _bp = _baseline_path(scan_root)
        _cov = "own baseline: " + _bp.name if _bp.exists() else (
            "NO baseline yet — every dirty file below reads as NEW; "
            "--rebaseline to establish coverage")
        print(f"  scan root                      : {args.scan_root}  [{_cov}]")
        _unused_banner = (
              f"[non-default — baseline does not cover it, so every dirty\n"
              f"                                   file below is reported as "
              f"NEW; treat this run as ADVISORY]")
    found = scan(scan_root)
    baseline_path = _baseline_path(scan_root)
    prior: dict[str, int] = {}
    if baseline_path.exists():
        prior = json.loads(baseline_path.read_text())["files"]

    new_files = {f: n for f, n in found.items() if f not in prior}
    grew = {f: (prior[f], n) for f, n in found.items()
            if f in prior and n > prior[f]}
    drained = {f: (prior[f], found.get(f, 0)) for f in prior
               if found.get(f, 0) < prior[f]}

    total = sum(found.values())
    base_total = sum(prior.values()) if prior else 0

    print("=" * 74)
    print("RAW-FLOAT64 AUDIT — float64 that entered a witness at all")
    print("=" * 74)
    print(f"  witnesses carrying raw float64 : {len(found)}")
    print(f"  total raw float64 fields       : {total:,}")
    if CARVED_INTEGRATOR:
        print(f"  f64-integrator carve-out       : "
              f"{sum(CARVED_INTEGRATOR.values()):,} field(s) in "
              f"{len(CARVED_INTEGRATOR)} witness(es)  [NOT drained — declared "
              f"precision_tier={F64_INTEGRATOR_TIER!r}]")
        for _f, _n in sorted(CARVED_INTEGRATOR.items(), key=lambda t: -t[1]):
            print(f"      {_n:6,d}  {_f}")
    if CARVED_DEPRECATED:
        print(f"  deprecated-f64 carve-out       : "
              f"{sum(CARVED_DEPRECATED.values()):,} field(s) in "
              f"{len(CARVED_DEPRECATED)} witness(es)  [NOT drained — declared "
              f"precision_tier={F64_DEPRECATED_TIER!r} + deprecated, "
              f"i.e. exploratory and retired rather than rewritten]")
        for _f, _n in sorted(CARVED_DEPRECATED.items(), key=lambda t: -t[1]):
            print(f"      {_n:6,d}  {_f}")
    if CARVED:
        print(f"  LP-dual carve-out excused      : {sum(CARVED.values()):,} "
              f"field(s) in {len(CARVED)} witness(es)  [NOT drained — see "
              f"LP_DUAL_F64_FIELDS]")
    if prior:
        print(f"  baseline files / fields        : {len(prior)} / {base_total:,}")
        print(f"  drained since baseline         : {len(drained)} file(s), "
              f"{base_total - total:+,} field(s)")
    print(f"  NEW dirty witnesses            : {len(new_files)}")
    print(f"  REGRESSED (count increased)    : {len(grew)}")

    if new_files:
        print("\n  NEW witnesses carrying raw float64 — fix AT THE PRODUCER")
        print("  (carry mpmath.mpf from the source, serialize with _precision.fmt),")
        print("  then re-run it. Do NOT add the file to the baseline to silence this.")
        for f, n in sorted(new_files.items(), key=lambda kv: -kv[1])[:25]:
            print(f"    {n:6d}  {f}")
        if len(new_files) > 25:
            print(f"    ... and {len(new_files) - 25} more")

    if grew:
        print("\n  REGRESSED — these witnesses gained raw float64:")
        for f, (was, now) in sorted(grew.items(), key=lambda kv: kv[1][0] - kv[1][1])[:25]:
            print(f"    {was:6d} -> {now:<6d}  {f}")

    if drained:
        print(f"\n  Drained (progress): {len(drained)} file(s)")
        for f, (was, now) in sorted(drained.items(),
                                    key=lambda kv: kv[1][1] - kv[1][0])[:10]:
            print(f"    {was:6d} -> {now:<6d}  {f}")

    if args.rebaseline:
        baseline_path.write_text(json.dumps(
            {"note": "Witnesses known to carry raw float64, by count. The "
                     "backlog is tolerated; it must only SHRINK. Regenerate "
                     "ONLY when draining. Adding a file here to silence a "
                     "failure defeats the gate — fix at the producer instead.",
             "enforced_rule": "AGENTS.md: NO-FLOAT64 means none may enter a witness.",
             "drain_owner": "PR #4677 (float64 residual, producer-side)",
             "files_count": len(found),
             "fields_count": total,
             "files": dict(sorted(found.items()))}, indent=2) + "\n")
        print(f"\nRebaselined: {len(found)} files / {total:,} fields recorded.")

    out = HERE / _output_name(scan_root)
    out.write_text(json.dumps({
        "schema": "witness/v1",
        "name": "witness-raw-float64-audit",
        "description": "Witnesses carrying raw float64 JSON numbers. Enforces "
                       "the stated NO-FLOAT64 rule, which the padding audit "
                       "does not: that gate catches only FAKE precision "
                       "(float64 padded past ~17 digits), so honest float64 "
                       "passes it. Ratchet only — draining is PR #4677.",
        "data": {
            "dirty_witnesses": len(found),
            "total_fields": total,
            # The carve-out, recorded in the witness so it is auditable rather
            # than only visible in console output.
            "lp_dual_carved_out_fields": sum(CARVED.values()),
            "lp_dual_carved_out_by_file": dict(sorted(CARVED.items())),
            "lp_dual_carved_out_field_names": sorted(LP_DUAL_F64_FIELDS),
            # The float64-integrator carve-out, recorded on the SAME terms as
            # the LP-dual one above. Console output is not auditability: a
            # reviewer reading the committed artifact must be able to see what
            # was excused and on whose declaration, without re-running the
            # script. Emitting it only to stdout would have made this carve-out
            # exactly the unseeable kind its own comment warns against.
            "f64_integrator_carved_out_fields": sum(CARVED_INTEGRATOR.values()),
            "deprecated_f64_carved_out_fields": sum(CARVED_DEPRECATED.values()),
            "deprecated_f64_carved_out_by_file": dict(CARVED_DEPRECATED),
            "f64_integrator_carved_out_by_file": dict(
                sorted(CARVED_INTEGRATOR.items())),
            "f64_integrator_declared_tier": F64_INTEGRATOR_TIER,
            "baseline_files": len(prior),
            "baseline_fields": base_total,
            "new_not_baselined": len(new_files),
            "regressed": len(grew),
            "drained_files": len(drained),
        },
    }, indent=2) + "\n")
    print(f"\nWrote {out.name}")
    return 1 if (args.strict and (new_files or grew)) else 0


if __name__ == "__main__":
    sys.exit(main())
