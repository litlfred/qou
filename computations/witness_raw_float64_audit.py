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
#: Runtime timing METADATA — not payload numbers, and not a precision finding.
#: Sourced from ``qou_substrate.witness._EPHEMERAL_META_FIELDS`` rather than
#: re-typed, because that module already declares these names reserved
#: ("the masked names are reserved for runtime-metadata semantics across the
#: witness corpus") and strips them RECURSIVELY, by name, for comparison. A
#: hand-copied list here could drift from the mask it is supposed to mirror;
#: `test_ephemeral_mask_sync` already guards the one other copy.
#:
#: Only the DURATION names are carved out. `environment`, `commitSha`,
#: `computedAt`, `scriptCommitSha` are also in that mask but carry no floats,
#: and carving a whole subtree would be a much broader excuse than this needs.
#:
#: WHY THIS IS NOT BASELINE-WIDENING. These fields are wall-clock seconds. No
#: value is being hidden and no producer is excused from carrying `mpf`: a
#: duration is not a measurement of the physics and re-running changes it. The
#: gate was ALREADY GREEN when this was added (NEW 0 / REGRESSED 0), so it
#: turns no red green — it removes false positives from a passing gate's
#: reported backlog, which is what makes a future NEW trustworthy. Same shape
#: as the 2026-08-24 integral-float reclassification, and reported the same
#: way: as a reclassification, never as draining.
#: True iff `_EPHEMERAL_META_FIELDS` was importable.  When False the carve-out
#: is empty BY DESIGN (see below) and every count in this audit is degraded in
#: the STRICT direction -- correct as a gate, wrong to persist.  See bean
#: `qou-qvg6`.
EPHEMERAL_PROVENANCE_OK = True


def _ephemeral_timing_fields() -> frozenset[str]:
    global EPHEMERAL_PROVENANCE_OK
    try:
        import sys as _s
        from pathlib import Path as _P
        _s.path.insert(0, str(_P(__file__).resolve().parents[1]
                              / "tools" / "qou-substrate" / "python"))
        from qou_substrate.witness import _EPHEMERAL_META_FIELDS as _M
        # THIS IS A SUBSTRING TEST OVER THAT SET, NOT THE SET ITSELF, and the
        # difference is a trap worth naming here (bean qou-hhm3 / #5793).
        # Measured on main: the mask holds 9 names, this carves 5. So ADDING A
        # NAME TO _EPHEMERAL_META_FIELDS DOES NOT CARVE IT HERE unless the name
        # happens to contain "dur" or "elapsed" -- `wall_sec` contains neither.
        #
        # That matters because it fails SILENTLY. Broadening the filter is the
        # dangerous move and the self-test below warns about it loudly (a /time/
        # test excuses `y_times_chi`, the Frobenius pairing, 177 fields). This
        # is the quiet one: extend the mask expecting these counts to drop, and
        # nothing happens, with no error and no diff to explain it. An agent
        # did exactly that and had to retract the prescription.
        #
        # Widening coverage therefore needs BOTH halves -- the name declared in
        # the mask AND reachable by whatever selects from it here -- which is
        # the open question on qou-ywee, not a one-sided edit.
        return frozenset(n for n in _M if "dur" in n.lower() or "elapsed" in n.lower())
    except Exception:
        # Never let provenance-import failure silently widen the gate: an empty
        # set carves out nothing, so the audit stays STRICTER, not looser.
        #
        # That is right for the GATE and is deliberately unchanged.  What is
        # NOT right is persisting the degraded numbers: `qou_substrate` is not
        # on PyPI, so a bare container -- the DEFAULT per AGENTS.md -- silently
        # produces dirty_witnesses UP and drained_files DOWN, and any agent
        # committing the result pushes a fake drain reversal into the ratchet
        # everyone reads as the baseline.  Baselines drain, never grow.
        # The refusal to write lives at the `out.write_text` call below.
        EPHEMERAL_PROVENANCE_OK = False
        return frozenset()


EPHEMERAL_TIMING_FIELDS = _ephemeral_timing_fields()

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

    **AND when it agrees with the float it shadows** (added 2026-08-23, bean
    `qou/ftuv`). The digit-count guard alone leaves a second laundering hole,
    a sibling of the one above: a companion carrying 50 digits of a DIFFERENT
    number excuses its f64 just as well. Found by walking into it — a producer
    wrote `round(primal_obj, 6)` beside a full-precision companion, and since
    the value was ~4.2e-44 the rounding wrote **`0.0`**. The pair then read as
    "f64 convenience copy + exact value" while the f64 was not a lossy copy of
    the value but a different number entirely, and a consumer doing arithmetic
    on it — the very consumers this rule exists to keep served — would get
    zero.

    Measured before landing: of 236 shadow pairs in the live corpus, **236
    agree and 0 disagree**, so this rejects nothing that was already honest.

    The tolerance is deliberately LOOSE — 1e-9 relative, not f64 epsilon. The
    defect being guarded against is a companion describing a *different
    number*, which is a total mismatch (`0.0` against `4.2e-44` is a relative
    error of 1). Demanding correct rounding would also reject hand-written
    fixtures and any producer that truncated its float for display, which is
    sloppy but not laundering, and would make the rule brittle for no gain.
    """
    _AGREE_REL_TOL = 1e-9

    def _agrees(v: float, c: str) -> bool:
        try:
            # float64-ok: the downcast IS the comparison. This asks whether the
            # `*_str` companion round-trips to the f64 actually recorded, so
            # the companion must be brought to f64 to be compared with it.
            # Comparing at full precision would answer a different question.
            cv = float(c)  # float64-ok: see above
        except ValueError:
            return False
        if cv == v:
            return True
        scale = max(abs(v), abs(cv))
        return scale > 0 and abs(cv - v) <= _AGREE_REL_TOL * scale

    if isinstance(value, float) and isinstance(companion, str):
        return _sig_digits(companion) > _F64_SIG_DIGITS and _agrees(value, companion)
    if isinstance(value, list) and isinstance(companion, list):
        if not value or len(value) != len(companion):
            return False
        pairs = list(zip(value, companion))
        if not all(isinstance(v, float) and isinstance(c, str) for v, c in pairs):
            return False
        return all(
            _sig_digits(c) > _F64_SIG_DIGITS and _agrees(v, c) for v, c in pairs
        )
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


def count_integral(obj) -> int:
    """How many floats hold an exactly-integral value (`0.0`, `54.0`).

    Not a precision finding — see `_count`. Whether such a field was MEANT to
    be an integer is `witness_integer_field_audit`'s question, not this one.
    """
    return _count(obj)[2]


def _count(obj, integral_is_exact: bool = True) -> tuple[int, int, int, int]:
    """(counted, carved_out, integral) — one traversal, all three numbers.

    INTEGRAL IS NOT A PRECISION FINDING, and separating it is the point.
    This gate exists to catch a value that a double cannot hold. A float whose
    value is an integer -- `0.0`, `54.0` -- is exact in binary64, so nothing
    was lost and there is nothing here for this gate to say. Counting it as
    "raw float64" made a JSON serialisation detail indistinguishable from a
    dropped digit.

    That is not hypothetical. Re-running eight producers on 2026-08-24 flipped
    82 fields and the ratchet called every one a REGRESSION. Checked pair by
    pair: 80 were `int -> float` with the VALUE UNCHANGED (80 equal, 0 changed),
    46 of them literally `0` -> `0.0`, and the producers were untouched -- the
    flip came from this container's library versions, not from any edit. The
    gate was red on a serialisation artifact while the same branch drained
    3,555 real fields.

    Corpus-wide the split matters even more: 225,385 integral floats across 856
    live witnesses, **218,697 of them exactly 0.0**, overwhelmingly `matrix_im`
    and `matrix_re`. The imaginary part of a real number IS a real number that
    happens to be zero; `0.0` is the CORRECT encoding there and `0` would be
    the wrong one. So "integral float" cannot mean "should have been an int" --
    that inference is wrong ~99% of the time here.

    Whether a field is *meant* to be an integer is a separate question, decided
    by declaration rather than by looking at the value, and it is asked by
    `computations/witness_integer_field_audit.py`. Bean `qou-xt5l`.

    Buckets stay DISJOINT: an integral float under a carved-out field counts as
    integral, not carved, because the carve-out excuses precision loss and no
    precision was lost.

    INTEGRALITY ONLY EXCUSES A FLOAT WHEN NOTHING CONTRADICTS IT, which is
    `integral_is_exact=False`. A `0.0` sitting beside a `_str` companion
    reading `4.2e-44` is not an exact integer, it is a value that rounded away
    to nothing — the worst precision loss this gate can find, and the self-test
    has carried that exact case since the rule was written: "a consumer doing
    arithmetic on it would get zero". So when a companion is present and does
    NOT agree, every float underneath counts, integral or not.
    """
    if isinstance(obj, dict):
        total = carved = integral = ephemeral = 0
        for k, v in obj.items():
            if k.endswith("_str"):
                t, c, i, e = _count(v, integral_is_exact)
                total += t
                carved += c
                integral += i
                ephemeral += e
                continue
            companion = obj.get(f"{k}_str")
            if companion is not None and _is_full_precision_shadow(v, companion):
                continue  # shadowed at full precision — not raw float64
            if k in EPHEMERAL_TIMING_FIELDS:
                t, _c, _i, _e = _count(v, integral_is_exact)
                ephemeral += t
                continue  # carve-out: wall-clock duration, not a payload number
            if k in LP_DUAL_F64_FIELDS:
                t, _c, i, e = _count(v, integral_is_exact)
                carved += t
                integral += i
                ephemeral += e
                continue  # carve-out: solver output, f64 by construction
            # A companion that is present but does NOT agree proves the float
            # differs from the true value, so integrality excuses nothing
            # underneath it.
            t, c, i, e = _count(v, integral_is_exact and companion is None)
            total += t
            carved += c
            integral += i
            ephemeral += e
        return total, carved, integral, ephemeral
    if isinstance(obj, list):
        total = carved = integral = ephemeral = 0
        for v in obj:
            t, c, i, e = _count(v, integral_is_exact)
            total += t
            carved += c
            integral += i
            ephemeral += e
        return total, carved, integral, ephemeral
    if isinstance(obj, float):
        if obj.is_integer():
            return (0, 0, 1, 0) if integral_is_exact else (1, 0, 1, 0)
        return 1, 0, 0, 0
    return 0, 0, 0, 0


CARVED: dict[str, int] = {}
#: Per-file tally for the float64-integrator carve-out, kept SEPARATE from
#: `CARVED` so the two excuses can never be read as one number.
CARVED_INTEGRATOR: dict[str, int] = {}
CARVED_DEPRECATED: dict[str, int] = {}
#: Per-file tally of floats holding an exactly-integral value (`0.0`, `54.0`).
#: NOT a precision finding and NOT counted as raw float64 — see `_count`. Kept
#: as its own dict so removing them from the headline cannot make them
#: invisible: whether such a field was MEANT to be an integer is asked by
#: `witness_integer_field_audit`, and this is the number that feeds it.
INTEGRAL: dict[str, int] = {}
#: Per-file tally of raw floats under a runtime-duration field. Its own dict
#: for the same reason as `INTEGRAL`: an excuse that cannot be seen cannot be
#: audited.
EPHEMERAL: dict[str, int] = {}


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
    INTEGRAL.clear()
    for p in sorted((scan_root or HERE).rglob("*.witness.json")):
        if (p.name in SELF_OUTPUTS
                or p.name.startswith(SELF_OUTPUT_PREFIX)
                or ("_deprecated" in p.parts or "fsh-guts" in p.parts)):
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        n, carved, integral, ephemeral = _count(d)
        rel = p.relative_to(ROOT).as_posix()
        # An explicit float64-integrator declaration moves this file's REMAINING
        # count into the integrator carve-out. Applied at witness level, not
        # field level, because an integrator's output has no fixed field names —
        # which is exactly why it needs a producer's on-the-record claim rather
        # than a name list.
        if ephemeral:
            EPHEMERAL[rel] = ephemeral
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
        if integral:
            INTEGRAL[rel] = integral
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
        # Integral-valued float: NOT a precision finding as of 2026-08-24
        # (owner directive, bean `qou-xt5l`). `1.0` is exact in binary64, so
        # this gate has nothing to say about it. Whether the field was MEANT to
        # be an integer is `witness_integer_field_audit`'s question. The two
        # companion cases below still count, because a disagreeing `_str`
        # proves the float is not the value.
        ({"v": 1.0}, 0),                                  # integral-valued float
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

        # ── the SECOND laundering guard (2026-08-23) ─────────────────
        # A companion with plenty of digits, describing a DIFFERENT number,
        # excused its f64 just as effectively as one with too few. Walked
        # into it: a producer wrote `round(primal_obj, 6)` beside a
        # full-precision companion and, the value being ~4.2e-44, the
        # rounding wrote 0.0. The pair read as "convenience copy + exact
        # value" while the copy was zero — and a consumer doing arithmetic
        # on it, the reader this rule exists to keep served, would get zero.
        ({"primal_obj_x": 0.0,
          "primal_obj_x_str":
              "4.203895392974451212771188749869748393840785825629547e-44"}, 1),
        # The repaired pair: the f64 IS the companion as a double.
        ({"primal_obj_x": 4.203895392974451e-44,
          "primal_obj_x_str":
              "4.203895392974451212771188749869748393840785825629547e-44"}, 0),
        # List form, one element disagreeing, still counts all of them.
        ({"v": [1.5, 0.0],
          "v_str": ["1.500000000000000000000000000001",
                    "9.999999999999999999999999999999e-30"]}, 2),

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
        # ── runtime-duration carve-out ────────────────────────────────
        # Wall-clock durations are runtime metadata, not payload numbers.
        ({"elapsed_sec": 4315.281763076782}, 0),
        ({"elapsed_seconds": 0.0006499290466308594}, 0),
        ({"durationMs": 12.5, "duration_sec": 0.75}, 0),
        # Nested anywhere, matching the by-NAME recursive strip the
        # qou_substrate mask performs.
        ({"data": {"sweep": [{"elapsed_sec": 0.54}, {"elapsed_sec": 0.40}]}}, 0),
        # ...and NOTHING else in the same witness is excused. This is the
        # discrimination that keeps the carve-out narrow — the identical float
        # under a payload name still counts, so a producer cannot launder a
        # measurement by naming it after a timer.
        ({"elapsed_sec": 0.54, "tau": 0.54, "E0_MeV": 4.185981357642159}, 2),
        # A near-miss name is NOT carved: only the reserved names are.
        ({"elapsed": 0.54, "seconds": 0.54, "elapsed_ms": 0.54}, 3),

        # THE TRAP ANY WIDENING OF THIS FILTER WILL WALK INTO. The current
        # filter is `"dur" or "elapsed"` over _EPHEMERAL_META_FIELDS, which is
        # safe. But it covers only the 5 declared duration names, while the
        # corpus carries ~495 timing-shaped float fields under names the mask
        # does not declare (walltime_sec 99, rust_secs 46, time_sec 42,
        # compute_time_sec 38, wall_sec 36, solve_time_s 33 ...). The obvious
        # next step is to broaden the substring test to "time"/"wall"/"_sec".
        #
        # DO NOT, without keeping these cases green. `_times_` is
        # MULTIPLICATION, and `y_times_chi` is the Frobenius pairing
        # y_lambda . chi_lambda -- 177 fields corpus-wide, the framework's
        # central object. A /time/ substring test excuses every one of them
        # from this gate, silently, and the gate stays green while doing it.
        # Measured on this corpus: broadening to /time|wall|_sec|elapsed|dur/
        # matches 84 distinct names, of which 19 are physics or ratios, and
        # excusing them would remove 361 REAL float64 fields from the gate.
        ({"y_times_chi": 0.123}, 1),
        ({"y_times_chi_abs": 0.123, "E0_times_f_MeV": 938.272}, 2),
        ({"rho_q_times_Vol": 2.0299, "m_e_times_hbar_q2": 0.00501}, 2),
        ({"Delta_lambda_D_times_h_minus_1": -1.585}, 1),
        ({"bracket_2_q_times_3_q": 4.44, "delta_net_times_E0": 0.78}, 2),
        # A ratio is not a duration either, however it is spelled.
        ({"time_speedup": 1.37}, 1),
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
             "Each root gets its OWN baseline file (see _baseline_path), so a "
             "root with no baseline yet reports every dirty file as NEW and "
             "such a run is ADVISORY until coverage is established. "
             "--rebaseline against a non-default root is PERMITTED and is how "
             "you establish that coverage: it writes that root's own file and "
             "cannot reach the corpus baseline. Once established the root can "
             "go blocking. Establishing coverage over an unscanned tree is a "
             "different act from silencing a regression in a covered one; "
             "only the latter is forbidden (bean qou-irzg).")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on a NEW dirty witness or an INCREASED count")
    ap.add_argument("--no-write", action="store_true",
                    help="read-only mode: evaluate and gate without writing the audit witness (bean qou-y8d0)")
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
    if EPHEMERAL:
        print(f"  runtime-duration carve-out     : {sum(EPHEMERAL.values()):,} field(s) "
              f"in {len(EPHEMERAL)} witness(es)  [NOT a precision finding — wall-clock "
              f"durations, names reserved as runtime metadata by qou_substrate's "
              f"_EPHEMERAL_META_FIELDS and stripped by name for comparison. A "
              f"RECLASSIFICATION, not draining.]")
        for _f, _n in sorted(EPHEMERAL.items(), key=lambda kv: -kv[1])[:5]:
            print(f"      {_n:6,d}  {_f}")
    if CARVED:
        print(f"  LP-dual carve-out excused      : {sum(CARVED.values()):,} "
              f"field(s) in {len(CARVED)} witness(es)  [NOT drained — see "
              f"LP_DUAL_F64_FIELDS]")
    if INTEGRAL:
        print(f"  integral-valued floats         : {sum(INTEGRAL.values()):,} "
              f"field(s) in {len(INTEGRAL)} witness(es)  [NOT a precision "
              f"finding — exact in binary64. Whether any of them was MEANT to "
              f"be an integer is `witness_integer_field_audit`'s question]")
    if prior:
        print(f"  baseline files / fields        : {len(prior)} / {base_total:,}")
        print(f"  drained since baseline         : {len(drained)} file(s), "
              f"{base_total - total:+,} field(s)")
        if INTEGRAL:
            # DO NOT READ THAT NUMBER AS WORK DONE. The baseline was recorded
            # while integral-valued floats still counted as raw float64, and
            # they stopped counting on 2026-08-24 (bean `qou-xt5l`). Most of
            # the "drain" above is that reclassification, not a producer
            # rewriting anything. Re-baselining would erase the history that
            # makes this legible, so the caveat is printed instead.
            print(f"      of which ~{sum(INTEGRAL.values()):,} is the "
                  f"2026-08-24 integral-float reclassification, not draining")
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
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        # DRAIN-ONLY, ENFORCED HERE rather than left to the operator.
        #
        # This file's own note has always said "the backlog is tolerated; it
        # must only SHRINK. Regenerate ONLY when draining." Nothing enforced
        # it. `--rebaseline` wrote the current counts verbatim, so a run made
        # while ANY entry had grown silently banked that regression -- the
        # precise move the note forbids, performed by the tool that carries
        # the note.
        #
        # Caught on 2026-08-29: a rebaseline after the H_9 A-operator
        # declaration would have banked `onepb-status-dashboard` at 5 -> 6.
        # That 6 arrived from main's own `629e257818` ("mpmath was defaulting
        # to dps=15") landing after the previous baseline was banked -- a
        # GOOD fix, correctly flagged, which a blind rebaseline would have
        # erased the evidence of. It was caught only because the operator
        # happened to diff the two files by hand first, which is not a
        # guarantee.
        #
        # Each entry is now floored at its previous value, and every entry
        # that WOULD have grown is named on stdout. Flooring alone would be
        # worse than the bug: it would keep the gate honest while hiding why,
        # so the report is the other half of the fix.
        _prev = {}
        if baseline_path.exists():
            try:
                _prev = (json.loads(baseline_path.read_text())
                         .get("files") or {})
            except (json.JSONDecodeError, OSError):
                _prev = {}
        _banked, _would_grow = {}, []
        for _f, _n in found.items():
            _o = _prev.get(_f)
            if _o is not None and _n > _o:
                _would_grow.append((_f, _o, _n))
                _banked[_f] = _o          # hold the floor
            else:
                _banked[_f] = _n
        if _would_grow:
            print(f"\n  NOT BANKED — {len(_would_grow)} entr"
                  f"{'y' if len(_would_grow) == 1 else 'ies'} would have GROWN;"
                  f" each held at its previous floor:")
            for _f, _o, _n in sorted(_would_grow, key=lambda t: t[2] - t[1],
                                     reverse=True):
                print(f"    {_o:6d} -> {_n:<6d}  {_f}")
            print("  Baselines drain, never grow. Fix at the producer; the\n"
                  "  gate keeps reporting these until you do.")

        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload_1 = {"note": "Witnesses known to carry raw float64, by count. The "
                     "backlog is tolerated; it must only SHRINK. Regenerate "
                     "ONLY when draining. Adding a file here to silence a "
                     "failure defeats the gate — fix at the producer instead.",
             "enforced_rule": "AGENTS.md: NO-FLOAT64 means none may enter a witness.",
             # Root-aware: #4677 owns the computations/ backlog and nothing
             # else. A non-default root's backlog belongs to whoever gated it,
             # and stamping every root with #4677 would send the next agent to
             # an arc that never touched these files.
             # Root-aware: #4677 owns the computations/ backlog and nothing
             # else. A non-default root's backlog belongs to whoever gated it.
             # Do NOT name a bean here — this string is written for EVERY
             # root, so a hardcoded id sends the next agent to the wrong arc
             # (it said qou-irzg, the audits-tree bean, while writing the
             # qou-mass baseline). The owning bean is recorded beside the
             # gate entry in scripts/precision-gates.sh, which is per-root.
             "drain_owner": ("PR #4677 (float64 residual, producer-side)"
                             if scan_root is None else
                             f"whoever gated {args.scan_root} — see the gate "
                             f"entry in scripts/precision-gates.sh"),
             "files_count": len(_banked),
             "fields_count": sum(_banked.values()),
             "files": dict(sorted(_banked.items()))}
        _prov_payload_1.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload_1, script_path=__file__, engine=None, q0_anchor=False)
        baseline_path.write_text(json.dumps(
            _prov_payload_1, indent=2) + "\n")
        print(f"\nRebaselined: {len(_banked)} files / "
              f"{sum(_banked.values()):,} fields recorded."
              + (f"  ({total - sum(_banked.values()):,} not banked — "
                 f"held at floor above.)" if _would_grow else ""))

    out = HERE / _output_name(scan_root)
    if not EPHEMERAL_PROVENANCE_OK:
        # Gate still gated (the exit code below is unchanged); witness NOT
        # written, because these counts are import-degraded.  Bean `qou-qvg6`.
        print(
            "\n  !! WITNESS NOT WRITTEN — provenance import failed.\n"
            "     `qou_substrate.witness._EPHEMERAL_META_FIELDS` is "
            "unavailable, so the runtime-duration carve-out is EMPTY and\n"
            "     every count above is degraded in the strict direction "
            "(dirty UP, drained DOWN). The gate result stands; the\n"
            "     numbers are not the corpus baseline and must not be "
            "committed. Install the package to regenerate:\n"
            "       pip install -e tools/qou-substrate\n"
            "     (bean qou-qvg6)",
            file=sys.stderr)
        # SAME verdict as the write path below — the gate is unchanged.
        return 1 if (args.strict and (new_files or grew)) else 0
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload_2 = {
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
            "ephemeral_duration_carved_out_fields": sum(EPHEMERAL.values()),
            "ephemeral_duration_carved_out_by_file": dict(
                sorted(EPHEMERAL.items(), key=lambda kv: -kv[1])),
            "ephemeral_duration_field_names": sorted(EPHEMERAL_TIMING_FIELDS),
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
    }
    _prov_payload_2.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload_2, script_path=__file__, engine=None, q0_anchor=False)
    if not args.no_write:
        out.write_text(json.dumps(_prov_payload_2, indent=2) + "\n")
        print(f"\nWrote {out.name}")
    # ADVISORY-MODE NOTICE (qou-6sts). Without --strict this function returns 0
    # no matter how red the corpus is, so `$?` is not a gate. The documented
    # paths already pass --strict (scripts/precision-gates.sh,
    # .github/workflows/witness-staleness.yml) -- this notice exists for the
    # HAND-run, which is how six PRs in one session came to report "gate
    # passed" off a bare invocation that could not have failed. The exit code
    # is deliberately unchanged so no existing caller's behaviour moves; the
    # fix is to make the inert exit visible, not to make it blocking.
    if not args.strict and (new_files or grew):
        print(
            f"\n  ⚠ ADVISORY MODE — findings above ({len(new_files)} new, "
            f"{len(grew)} regressed) but EXIT CODE IS 0.\n"
            "    `$?` only gates with --strict. Re-run as:\n"
            f"      python3 {_os.path.basename(__file__)} --strict"
        )
    return 1 if (args.strict and (new_files or grew)) else 0


if __name__ == "__main__":
    sys.exit(main())
