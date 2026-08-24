#!/usr/bin/env python3
"""Integer-typed witness fields must be serialised as integers, not `54.0`.

WHY THIS IS ITS OWN GATE
------------------------
`witness_raw_float64_audit` asks one question: did a value lose digits a double
cannot hold? An integral float — `0.0`, `54.0` — answers that question with
"no", because integers are exact in binary64. Until 2026-08-24 it counted them
anyway, and the cost was concrete: re-running eight producers flipped 82 fields
from `int` to `float`, the ratchet called all 82 a REGRESSION, and every one
was checked pair by pair as VALUE UNCHANGED (80 equal, 0 changed; 46 of them
literally `0` -> `0.0`). A serialisation detail was indistinguishable from a
dropped digit.

Splitting them is not a loosening. There IS a real question about `54.0` — was
that field meant to be an integer? — and it is a different question, with a
different answer method, and it gets asked here. Bean `qou-xt5l`.

WHY DECLARED AND NOT INFERRED
-----------------------------
The obvious rule, "a float whose value is integral should have been an int", is
wrong about 99% of the time in this corpus: of 225,385 integral floats across
856 live witnesses, 218,697 are exactly 0.0 and the bulk are `matrix_im` /
`matrix_re`. The imaginary part of a real number is a REAL that is zero. `0.0`
is the correct encoding and `0` would be a false claim.

The converse rule fails too. `matrix_im` has 160,704 integral values and zero
fractional ones, so "always a whole number" declares it an integer field — and
would be wrong. Meanwhile `word_cd` reads like a braid word and carries 83
fractional entries.

So intent is declared in `witness-integer-fields.json`, with a checkable reason
per field, and this gate enforces the declaration rather than guessing it.

WHAT CONSUMERS GET
------------------
Python's `json` distinguishes `3` from `3.0`; JavaScript's `JSON.parse` does
not — both arrive as `number`. So serialisation alone cannot tell a TypeScript
reader whether a field is a count or a measurement, and the registry is the
answer for both languages. `integer_fields()` below is the Python accessor; the
JSON file is the contract.

USAGE
    python3 computations/witness_integer_field_audit.py            # survey
    python3 computations/witness_integer_field_audit.py --strict   # gate
    python3 computations/witness_integer_field_audit.py --candidates
    python3 computations/witness_integer_field_audit.py --self-test
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REGISTRY = HERE / "witness-integer-fields.json"


def _load() -> tuple[dict, dict]:
    d = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return d.get("integer_fields", {}), d.get("known_real_fields", {})


def integer_fields() -> set[str]:
    """Field names declared integer-typed. The accessor consumers should use."""
    return set(_load()[0])


def _walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _walk(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _walk(v, f"{path}[{i}]")
    else:
        yield path, obj


def _leaf_name(path: str) -> str:
    return path.rsplit(".", 1)[-1].split("[")[0]


def _has_live_producer(d: dict) -> bool:
    """Whether this witness names a producer that still exists and is live.

    A violation in a witness whose producer is gone or deprecated CANNOT be
    fixed the way this gate demands, so it is reported separately rather than
    failing the run. This is a RULE, not a per-file carve-out: it cannot hide a
    new defect, because a newly written witness has a live producer by
    construction. `4he-binding-full-pipeline` is the case that motivated it --
    it self-declares `scriptFile: "(legacy — no matching producer found;
    provenance pending manual triage)"` and its only producer sits under
    `_deprecated/`.
    """
    sf = d.get("scriptFile")
    if not isinstance(sf, str) or not sf.endswith(".py"):
        return False
    name = Path(sf).name
    for cand in (ROOT / "computations").rglob(name):
        if "_deprecated" not in cand.parts:
            return True
    return False


def scan(root: Path | None = None):
    """(violations, orphan_violations, stats) over live witnesses.

    `violations[file] = [(path, value), ...]` for declared-integer fields that
    are serialised as JSON floats.
    `stats[name] = {'int': n, 'float_integral': n, 'float_fractional': n}` for
    every numeric field name, which is what `--candidates` reads.
    """
    root = root or (ROOT / "computations")
    violations: dict[str, list] = {}
    orphans: dict[str, list] = {}
    stats: dict[str, dict] = collections.defaultdict(
        lambda: {"int": 0, "float_integral": 0, "float_fractional": 0})
    declared = integer_fields()
    for p in sorted(root.rglob("*.witness.json")):
        if "_deprecated" in p.parts:
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        rel = p.relative_to(ROOT).as_posix()
        sink = violations if _has_live_producer(d) else orphans
        for path, v in _walk(d):
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                continue
            name = _leaf_name(path)
            if isinstance(v, int):
                stats[name]["int"] += 1
            elif v.is_integer():
                stats[name]["float_integral"] += 1
            else:
                stats[name]["float_fractional"] += 1
            if name in declared and isinstance(v, float):
                sink.setdefault(rel, []).append((path, v))
    return violations, orphans, stats


def candidates(stats: dict, known_real: dict) -> list[tuple[str, dict]]:
    """Field names worth CONSIDERING for the registry — proposed, never applied.

    The signal is not "always integral" (that is what wrongly nominates
    `matrix_im`). It is **written both ways**: the same field name appears as a
    JSON int in one place and a JSON float in another, with nothing fractional
    anywhere. A field that is genuinely real is not written as a bare int by
    accident, so inconsistency plus no-fractional is the shape of a count that
    some producer forgot to keep integral.
    """
    out = []
    declared = integer_fields()
    for name, s in stats.items():
        if name in declared or name in known_real:
            continue
        if s["float_fractional"] == 0 and s["int"] > 0 and s["float_integral"] > 0:
            out.append((name, s))
    return sorted(out, key=lambda kv: -(kv[1]["float_integral"]))


def self_test() -> int:
    """Prove the rule fires on a declared field and stays quiet elsewhere."""
    declared = {"dim_S_lambda"}
    cases = [
        ({"dim_S_lambda": 54.0}, 1, "declared field as float -> violation"),
        ({"dim_S_lambda": 54}, 0, "declared field as int -> clean"),
        ({"matrix_im": 0.0}, 0, "undeclared real that is integral -> clean"),
        ({"tolerance": 1e-9}, 0, "ordinary float -> clean"),
        ({"a": {"dim_S_lambda": 3.0}}, 1, "nested"),
        ({"xs": [{"dim_S_lambda": 3.0}, {"dim_S_lambda": 4}]}, 1, "in a list"),
        ({"dim_S_lambda": True}, 0, "bool is not a number"),
        ({"dim_S_lambda": "54"}, 0, "string is not a float"),
    ]
    bad = 0
    for payload, want, why in cases:
        got = sum(1 for path, v in _walk(payload)
                  if isinstance(v, float) and not isinstance(v, bool)
                  and _leaf_name(path) in declared)
        if got != want:
            print(f"  FAIL [{why}] {payload} expected {want}, got {got}")
            bad += 1
    # The candidate detector must NOT nominate an always-integral real.
    stats = {"matrix_im": {"int": 0, "float_integral": 900, "float_fractional": 0},
             "dim_S_lambda": {"int": 5, "float_integral": 7, "float_fractional": 0},
             "nf_net": {"int": 0, "float_integral": 9, "float_fractional": 3}}
    names = [n for n, _ in candidates(stats, {})]
    if "matrix_im" in names:
        print("  FAIL candidate detector nominated matrix_im (never written as int)")
        bad += 1
    if "nf_net" in names:
        print("  FAIL candidate detector nominated nf_net (has fractional values)")
        bad += 1
    if bad:
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases: a declared field as a float is a "
          "violation; an integral float on an undeclared field is not; and the "
          "candidate detector rejects both an always-integral real and a field "
          "with fractional values.")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    integer_decl, known_real = _load()
    violations, orphans, stats = scan()
    n_viol = sum(len(v) for v in violations.values())
    n_orph = sum(len(v) for v in orphans.values())

    print("=" * 74)
    print("WITNESS INTEGER-FIELD AUDIT — declared counts must serialise as ints")
    print("=" * 74)
    print(f"  declared integer fields : {len(integer_decl)}  "
          f"({', '.join(sorted(integer_decl)) or 'none'})")
    print(f"  declared real fields    : {len(known_real)}")
    print(f"  violations              : {n_viol} field(s) in "
          f"{len(violations)} witness(es)")
    for f, items in sorted(violations.items(), key=lambda kv: -len(kv[1])):
        print(f"      {len(items):5d}  {f}")
        for path, v in items[:3]:
            print(f"             {path} = {v!r}   (should be {int(v)})")
    if orphans:
        print(f"\n  in witnesses with NO LIVE PRODUCER: {n_orph} field(s) in "
              f"{len(orphans)} witness(es)  [cannot be fixed at a producer -- "
              f"there is none. Reported, not failed]")
        for f, items in sorted(orphans.items(), key=lambda kv: -len(kv[1])):
            print(f"      {len(items):5d}  {f}")
            for path, v in items[:3]:
                print(f"             {path} = {v!r}   (should be {int(v)})")

    if "--candidates" in argv or not violations:
        cands = candidates(stats, known_real)
        print(f"\n  candidates (written BOTH as int and as float, none fractional): "
              f"{len(cands)}")
        print("      Proposed only. Adding one needs a reason a reader can check —")
        print("      see the registry's $comment for why value-shape is not enough.")
        for name, s in cands[:20]:
            print(f"      {s['float_integral']:6d} float / {s['int']:6d} int   {name}")

    if n_viol and "--strict" in argv:
        print("\nFix AT THE PRODUCER: emit int(...) for a declared count. Do not")
        print("hand-edit a witness, and do not remove the field from the registry")
        print("to make this green.")
        return 1
    print("\n✓ no declared integer field is serialised as a float"
          if not n_viol else "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
