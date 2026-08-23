#!/usr/bin/env python3


# polynomial_q_not_applicable: validator, not a q-series compute.
"""Detect witnesses stale with respect to the substrate constant q₀.

**Why this exists.** `run_pipeline.py`'s staleness check keys on the
PRODUCER SCRIPT's `scriptHash` — so it is **blind to changes in imported
constants** like q₀. The 2026-05-28 q₀ re-pin (muon-anchor `m_μ/m_e` →
proton-anchor `m_p/m_e`, commit `01c18125`) shifted q₀ ~1.3e-8 *without
touching any producer script*, leaving ~390 witnesses carrying the
pre-re-pin q₀ that `run_pipeline.py` happily reports as "fresh". See
`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`.

This detector compares each witness's recorded q₀-shaped value(s) against
the *current* q₀ and flags mismatches — the detection half of the systemic
fix. Wire it into the witness-pipeline so any future constant re-pin
auto-flags the affected witnesses (which the `scriptHash` gate cannot).

**Two robustness properties** (added after Copilot review of #1500/#1501):

- The basin prefix is **derived from the live `Q_50_DIGIT_STR`**, never
  hard-coded, so the detector tracks a re-pin without manual edits. A
  re-pin that leaves the basin neighbourhood is caught *loudly* (an
  assertion + a zero-match guard) instead of silently reporting "0 stale".
- **Audit / state-tracking witnesses are exempt** (`*-audit` / `*-scan` /
  `*-compliance`): their convention is to record provenance values —
  sometimes an OLD q₀ on purpose (e.g. `q0-consistency-audit`'s
  `old_muon_q0`) — so a basin mismatch there is intentional, not staleness.
  Mirrors `witness_provenance_audit.AUDIT_SUFFIXES`.

    python3 witness_constant_staleness.py            # report
    python3 witness_constant_staleness.py --strict   # exit 1 if any stale
    python3 witness_constant_staleness.py --list      # full list (for regen)
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import glob
import json
import re
import sys
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Optional

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
for p in (str(HERE), str(HERE.parent.parent.parent / "tools" / "qou-substrate" / "python")):
    if p not in sys.path:
        sys.path.insert(0, p)

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402  current q₀

# q₀-shaped decimals are matched by a basin prefix DERIVED from the live q₀
# (never hard-coded), so the detector auto-tracks a re-pin. The first 5
# significant digits ("1.1099") are wide enough to span an adjacent re-pin
# (the 2026-05-28 muon→proton shift kept all of "1.10997…") yet narrow
# enough to ignore unrelated 1.x high-precision constants. A re-pin that
# leaves this neighbourhood is caught by the assertion + the zero-match
# guard in main(), NOT silently reported as "0 stale".
_BASIN = Q_50_DIGIT_STR[:6]  # e.g. "1.1099"
Q0_SHAPE = re.compile(re.escape(_BASIN) + r"\d{6,}")
assert Q0_SHAPE.match(Q_50_DIGIT_STR), (
    f"q₀ basin drift: current q₀ {Q_50_DIGIT_STR!r} does not match the "
    f"derived basin pattern {Q0_SHAPE.pattern!r}; widen _BASIN.")

getcontext().prec = 80


# ── Compare at the RECORDED value's own precision ────────────────────
#
# The comparison used to be `recorded[:n] != live[:n]` at a fixed n. That
# reports a witness stale whenever it serializes FEWER digits than n, because
# slicing a shorter string yields a shorter string and the two can never be
# equal — the value is right, the width is not.
#
# Measured on `main` 2026-08-23: `lever1-color-eq-intrinsic-tau-rapidity`
# records the proton q₀ as `1.10997858275` (13 chars). That is the live pin,
# correctly re-pinned by PR #5532 and merely serialized short; the gate called
# it stale. It was invisible until then because the field previously held a
# FULL-precision muon literal, so the widths happened to agree and only the
# digits differed. Re-pinning it to a shorter proton serialization exposed the
# comparator, not a staleness.
#
# So compare numerically, to the precision the witness actually states: a
# recorded value is fresh when it is within one unit in its own last place of
# the live q₀. One ulp (not a half) because a producer may either TRUNCATE or
# ROUND — a half-ulp bound would keep flagging round-ups such as `1.109978583`.
#
# This cannot mask a genuine pin flip. The muon and proton anchors are
# ~1.28e-8 apart, while the basin regex matches at least 10 decimals, capping
# the tolerance at 1e-10 — over two orders of magnitude tighter. That margin
# is not left as an argument: `_assert_tolerance_cannot_mask_a_pin_flip`
# below checks it against the live anchors at import, so widening `_BASIN`
# later fails loudly instead of quietly blunting the gate.


def _tolerance_for(recorded: str, max_sig: Optional[int] = None) -> Decimal:
    """One unit in `recorded`'s own last decimal place.

    `max_sig` caps how fine the comparison may get, in significant digits —
    the `--ndigits` knob. q₀ is ~1.1, so N significant digits is N-1 decimals.
    The cap can only LOOSEN the tolerance, never tighten it past what the
    witness actually states.
    """
    frac = recorded.split(".", 1)[1] if "." in recorded else ""
    decimals = len(frac)
    if max_sig is not None:
        decimals = min(decimals, max(max_sig - 1, 0))
    return Decimal(1).scaleb(-decimals)


def matches_live_q0(recorded: str, live: str = Q_50_DIGIT_STR,
                    max_sig: Optional[int] = None) -> bool:
    """True when `recorded` is the live q₀ to the precision it states."""
    try:
        return (abs(Decimal(recorded) - Decimal(live))
                <= _tolerance_for(recorded, max_sig))
    except ArithmeticError:
        return False


def _assert_tolerance_cannot_mask_a_pin_flip() -> None:
    """The loosest tolerance this comparator can grant must still separate
    the two anchors. Fails at import if a widened basin ever breaks that."""
    try:
        from qou_substrate.witness import _q0_value_for_anchor
        muon = _q0_value_for_anchor("muon")
        proton = _q0_value_for_anchor("proton")
    except Exception:
        return  # anchors unreadable in this container; nothing to check
    if not (muon and proton):
        return
    gap = abs(Decimal(muon) - Decimal(proton))
    # Shortest string the basin regex can match => loosest tolerance granted.
    shortest = _BASIN + "0" * 6
    loosest = _tolerance_for(shortest)
    assert loosest * 100 < gap, (
        f"q₀ staleness tolerance {loosest} is within 100x of the muon/proton "
        f"separation {gap}; the comparator could now accept a flipped pin. "
        f"Narrow the basin or tighten _tolerance_for.")


_assert_tolerance_cannot_mask_a_pin_flip()

# State-tracking witnesses whose convention is to record provenance
# (possibly an intentionally OLD q₀) — exempt from staleness, mirroring
# witness_provenance_audit.AUDIT_SUFFIXES.
AUDIT_SUFFIXES = (
    "-audit.witness.json",
    "-scan.witness.json",
    "-compliance.witness.json",
)


# ── Derived-output exemption ─────────────────────────────────────────
#
# The gate's premise is "a q₀-shaped number in a witness is a RECORDED PIN,
# so it must track the live q₀". That premise is false for one shape of
# producer: one that DERIVES q₀ as its subject rather than reading it.
#
# `knot-volumes` is the worked case (bean qou-bdkx). It reads no substrate
# q₀ at all — its q comes out of SnapPy's Vol(4₁) and the CODATA m_μ/m_e
# ratio, i.e. the CAL-2 ideal-layer DEFINITION, evaluated as an assertion's
# own subject and checked against that assertion's own `expected` ± `tol`.
# Its value therefore lands in the muon basin BY CONSTRUCTION and can never
# approach the proton pin, however fresh the run. The gate's standing
# instruction is "drain them at the producers, do NOT baseline" — but here
# there is nothing to drain: the producer is correct, and a re-run (verified
# 2026-08-23) reproduces a muon-basin number because that is the answer.
#
# So the exemption is NOT a baseline. It encodes the one case the premise
# does not cover, and it needs BOTH conditions to fire:
#
#   1. the witness positively declares `q0Anchor: "independent"` WITH a
#      `q0AnchorReason` — the producer asserting, auditably, that it reads
#      no pin (`q0_anchor_consistency_audit.py` separately counts the
#      reason-less declarations, so a thin claim stays visible); and
#   2. EVERY basin-matching value in the witness sits at an assertion's
#      `computed` / `expected` — a measured result checked against its own
#      expectation, never a constant recorded for downstream consumption.
#
# Condition 2 is what keeps this from becoming an escape hatch, and it is
# load-bearing rather than decorative: `z2bn-tau-derivation-probe` declared
# `independent` FALSELY (it hardcoded a q₀ and consumed it five times) and
# is still caught here, because its value sat at top-level `.q0`, not in an
# assertion. Measured against all six witnesses this gate flagged on
# 2026-08-23, condition 2 alone separates the one structural case from the
# five real ones. A value anywhere else — `.q0Value`, `.params.q0`,
# `.results.*` — stays flagged no matter what the witness declares.
#
# Anything not attributable to a walked JSON path is treated as NOT exempt,
# so a text match the walk cannot explain fails closed.
_ASSERTION_VALUE_KEYS = ("computed", "expected")


def _basin_paths(node, path: str = ""):
    """Yield (json_path, basin_value) for every q₀-shaped number/string."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _basin_paths(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _basin_paths(v, f"{path}[{i}]")
    else:
        text = repr(node) if isinstance(node, float) else str(node)
        for m in Q0_SHAPE.finditer(text):
            yield path, m.group(0)


_ASSERTION_PATH = re.compile(
    r"^\.assertions\[\d+\]\.(?:" + "|".join(_ASSERTION_VALUE_KEYS) + r")$")


def derived_output_exempt(witness, max_sig: Optional[int] = None):
    """Return a reason string if every stale basin value is a derived output.

    ``witness`` is the raw JSON text of a witness, or an already-parsed
    mapping (the self-test below passes dicts, so nothing in this file has
    to serialize one). ``None`` means "not exempt" — including every parse
    failure, so the check fails closed.
    """
    if isinstance(witness, str):
        raw = witness
        try:
            doc = json.loads(raw)
        except json.JSONDecodeError:
            return None
    else:
        raw, doc = None, witness
    if not isinstance(doc, dict):
        return None
    if doc.get("q0Anchor") != "independent":
        return None
    if not str(doc.get("q0AnchorReason") or "").strip():
        return None

    walked = list(_basin_paths(doc))
    stale_walked = [(p, v) for p, v in walked
                    if not matches_live_q0(v, max_sig=max_sig)]
    if not stale_walked:
        return None  # nothing stale to excuse; leave the normal path alone

    # Every stale value must be attributable to an assertion measurement.
    offenders = [p for p, _ in stale_walked if not _ASSERTION_PATH.match(p)]
    if offenders:
        return None

    # And the raw-text scan must not see a stale value the walk missed.
    if raw is not None:
        raw_stale = {m.group(0) for m in Q0_SHAPE.finditer(raw)
                     if not matches_live_q0(m.group(0), max_sig=max_sig)}
        if not raw_stale <= {v for _, v in stale_walked}:
            return None

    return ", ".join(sorted({p for p, _ in stale_walked}))


# ── Self-test for the exemption ──────────────────────────────────────
#
# The exemption is the one place this gate can LOSE detection power, so its
# behaviour is checkable in place rather than by reading it. Every negative
# below is a shape that must stay flagged; the z2bn ones are not hypothetical
# (bean qou-bdkx). Run: `python3 witness_constant_staleness.py --selftest`.

_SELFTEST_STALE = "1.1099785955541805"


def _selftest() -> int:
    import copy

    base = {
        "q0Anchor": "independent",
        "q0AnchorReason": "derives q from Vol(4_1) and m_mu/m_e; reads no pin",
        "assertions": [{"name": "substrate q", "computed": float(_SELFTEST_STALE),
                        "expected": 1.10997, "tolerance": 1e-3}],
    }

    def case(label, doc, want):
        got = derived_output_exempt(doc) is not None
        ok = got == want
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}  (exempt={got}, want={want})")
        return ok

    checks = [("derived output, declared independent, value in an assertion",
               base, True)]

    def variant(label, mutate, want):
        d = copy.deepcopy(base)
        mutate(d)
        checks.append((label, d, want))

    variant("reason missing", lambda d: d.pop("q0AnchorReason"), False)
    variant("reason blank", lambda d: d.update(q0AnchorReason="  "), False)
    variant("declared proton", lambda d: d.update(q0Anchor="proton"), False)
    variant("no anchor declared", lambda d: d.pop("q0Anchor"), False)
    variant("+ top-level .q0 (the z2bn shape)",
            lambda d: d.update(q0=float(_SELFTEST_STALE)), False)
    variant("+ .q0Value", lambda d: d.update(q0Value=_SELFTEST_STALE), False)
    variant("+ .results.q0",
            lambda d: d.update(results={"q0": float(_SELFTEST_STALE)}), False)
    variant("stale value in an assertion NOTE, not computed/expected",
            lambda d: d["assertions"][0].update(note=f"was {_SELFTEST_STALE}"),
            False)
    variant("nothing stale to excuse",
            lambda d: d["assertions"][0].update(computed=float(Q_50_DIGIT_STR[:18])),
            False)

    # Raw-text path: a stale value the JSON walk cannot attribute to any
    # assertion (here, inside a key the walk does not treat as a value) must
    # fail closed even though the parsed document looks exempt.
    checks.append((
        "raw text carries a stale value the walk cannot attribute",
        '{"q0Anchor": "independent", "q0AnchorReason": "derived", '
        '"assertions": [{"computed": ' + _SELFTEST_STALE + ', '
        '"expected": 1.10997, "tolerance": 0.001}], '
        '"note": "an older run gave 1.1099785900000000"}',
        False))

    print("derived-output exemption self-test:")
    passed = all(case(*c) for c in checks)

    # ── the precision-aware comparator ───────────────────────────────
    #
    # The truncation case is the measured regression (bean qou-bdkx): a
    # correctly-re-pinned proton value, serialized short, was reported stale.
    # The muon rows are the property that must NOT be lost to the fix.
    live = Q_50_DIGIT_STR
    try:
        from qou_substrate.witness import _q0_value_for_anchor
        muon = _q0_value_for_anchor("muon") or ""
    except Exception:
        muon = ""

    cmp_checks = [
        ("live q0 at full precision", live, True),
        ("live q0 truncated to 13 chars (the measured case)", live[:13], True),
        ("live q0 truncated to 12 chars", live[:12], True),
        ("live q0 ROUNDED up at 11 decimals", "1.10997858275", True),
        ("a digit genuinely wrong in the 11th decimal", live[:12] + "9" + live[13:20], False),
    ]
    if muon:
        cmp_checks += [
            ("the muon pin at full precision must stay flagged", muon, False),
            ("the muon pin truncated to 13 chars must stay flagged", muon[:13], False),
            ("the muon pin truncated to 12 chars must stay flagged", muon[:12], False),
        ]

    print("precision-aware comparator self-test:")
    for label, v, want in cmp_checks:
        got = matches_live_q0(v)
        ok = got == want
        passed = passed and ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}  ({v[:16]}… fresh={got}, want={want})")

    print("PASS" if passed else "FAIL")
    return 0 if passed else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true",
                    help="check the derived-output exemption and exit")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any q₀-stale witness is found")
    ap.add_argument("--ndigits", type=int, default=12,
                    help="cap on significant digits compared (default 12). A "
                         "witness is compared at ITS OWN precision or this "
                         "cap, whichever is coarser — never at a fixed width, "
                         "which reported short serializations as stale.")
    ap.add_argument("--list", action="store_true",
                    help="print every stale witness (for driving the regen)")
    ap.add_argument("--tree", action="store_true",
                    help=("scan EVERY *.witness.json in the repository instead "
                          "of only computations/substrate/. Opt-in on purpose "
                          "-- see the scope note below."))
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    cur = Q_50_DIGIT_STR[: args.ndigits + 2]  # "1." + ndigits sig
    stale: list[tuple[str, list[str]]] = []
    derived: list[tuple[str, list[str], str]] = []
    total = 0
    exempt = 0
    matched_any = 0  # witnesses embedding ≥1 q₀-shaped value
    # SCOPE. As shipped this globs ONE directory, non-recursively: the 55
    # witnesses in computations/substrate/. The docstring above describes a
    # corpus-wide detector ("~390 witnesses carrying the pre-re-pin q0",
    # "wire it into the witness-pipeline so any future constant re-pin
    # auto-flags the affected witnesses"), so the narrow glob is an
    # implementation/intent mismatch, not a design choice.
    #
    # Measured 2026-08-23 with this file's own Q0_SHAPE, AUDIT_SUFFIXES and
    # derived_output_exempt, over the tree minus .git/.claude/_deprecated:
    #
    #     scanned 55   -> 3 q0-stale      (as shipped)
    #     scanned 2848 -> 454 q0-stale    (--tree)
    #
    # 454 is the same order as the ~390 the docstring names, which is what
    # says the wide scope was the intent.
    #
    # 454 is NOT 454 defects. By declared anchor: 340 declare none, 52
    # declare muon (consistent -- the GATED qou-1c4y migration, leave them),
    # 49 declare proton while carrying a non-proton q0-shaped value, 9
    # independent, 3 ambiguous, 1 comparison. The 49 are the contradictory
    # class bean qou-bdkx triages -- and that bean lists 2 of them, because
    # it was written from the 55-file scan. Even those 49 are CANDIDATES: a
    # proton-declaring witness may carry a muon value as a deliberate
    # comparison (one is literally named ...-model-comparison), and at least
    # one basin match, 1.109940825176, is neither pin. Per-witness triage,
    # never a batch fix.
    #
    # --tree is opt-in rather than the default because scripts/staleness-gates.sh
    # runs this --strict as a BLOCKING gate; flipping the default turns it red
    # with 454 findings in one commit. Bean qou-5op4 carries the flip.
    scan = (REPO_ROOT.rglob("*.witness.json") if args.tree
            else (Path(p) for p in sorted(glob.glob(str(HERE / "*.witness.json")))))
    for wf in sorted(scan):
        if args.tree and any(part in (".git", ".claude", "_deprecated",
                                      "node_modules") for part in Path(wf).parts):
            continue
        name = Path(wf).name
        if name.endswith(AUDIT_SUFFIXES):
            exempt += 1
            continue
        total += 1
        raw = Path(wf).read_text()
        matches = list(Q0_SHAPE.finditer(raw))
        if matches:
            matched_any += 1
        vals = {m.group(0) for m in matches}
        bad = sorted(v for v in vals if not matches_live_q0(v, max_sig=args.ndigits))
        if bad:
            why = derived_output_exempt(raw, max_sig=args.ndigits)
            if why:
                derived.append((name, bad, why))
            else:
                stale.append((name, bad))

    print(f"current q₀ (≈{args.ndigits} sig): {cur}  (basin {Q0_SHAPE.pattern})")
    print(f"scanned {total} witnesses ({exempt} audit-exempt, "
          f"{len(derived)} derived-output-exempt); q₀-stale: {len(stale)}")

    # Never silent: an exemption that stops being printed stops being reviewed.
    for name, bad, why in derived:
        print(f"  [derived output, not a recorded pin] {name}: {bad} at {why}")

    # Zero-match guard: normally hundreds of witnesses embed q₀. If NONE do,
    # the basin regex has silently stopped matching (an un-tracked re-pin or
    # a corpus change) — fail loudly rather than report a false "0 stale".
    if total and matched_any == 0:
        print(f"\nERROR: zero witnesses matched the q₀ basin "
              f"{Q0_SHAPE.pattern!r} across {total} scanned — basin/regex "
              f"drift, not '0 stale'. Update _BASIN.")
        return 2

    show = stale if args.list else stale[:20]
    for name, bad in show:
        print(f"  {name}: {bad}")
    if not args.list and len(stale) > 20:
        print(f"  … +{len(stale) - 20} more (use --list)")

    if args.strict and stale:
        print(f"\nSTRICT FAIL: {len(stale)} witnesses carry a stale q₀ "
              f"(re-pin regeneration incomplete).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
