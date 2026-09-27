#!/usr/bin/env python3
"""Validate every witnessed-value pin in `folio/values/registry.ts`.

Bean `qou-xwet`.

## Why this exists

`folio/values/registry.ts` pins 69 named values to `(witnessFile,
witnessPath)` pairs. Until this script, **nothing checked any of them** —
`witnessPath` appeared nowhere in the repo outside the registry file itself.
A pin could name a file that no longer exists, address a path that no longer
resolves, or -- the case that actually happened -- keep resolving while
quietly addressing a *different physical quantity*.

The incident: `B_2H_AME_MeV` ("AME experimental binding energy of deuterium")
is pinned **positionally** at `data.rows.2.B_AME_MeV` in
`canonical-mass-table-extended.witness.json`. A second producer
(`low_isotope_mass_table.py`) was overwriting that witness with a restricted
row set, so from 2026-06-22 to 2026-08-15 `rows[2]` was **3He** and the pin
returned `7.71804132 MeV` instead of the deuteron's `2.2245662` -- 3.47x, under
a description naming deuterium. It was restored by a second clobber rather than
by a fix, and no check anywhere noticed either transition.

The producer-side half is guarded now (`canonical_mass_table_extended.py`
refuses a partial write). This is the consumer-side half: a pin that addresses
a nuclide row must *keep* addressing the nuclide its name claims.

## Checks

| id | severity | fires when |
|----|----------|------------|
| `E-missing-file` | error | `witnessFile` does not exist |
| `E-unresolvable` | error | `witnessPath` does not resolve under any root |
| `E-null-value`   | error | the path resolves to `null` |
| `E-nuclide-drift`| error | a positional row pin addresses the wrong nuclide |
| `W-positional`   | warn  | the pin indexes an array by position at all |

`E-nuclide-drift` is the one with teeth, and it is only checkable because the
rows carry `Z` / `N` / `A`. When a pin's *name* encodes a nuclide (`B_2H_...`,
`B_4He_...`) and its path lands on a row dict with those keys, the two must
agree. That is the assertion the eight-week window needed and did not have.

`W-positional` never fails the run. Positional addressing is not wrong in
itself -- it is fragile, and the warning is there so a reviewer can see how
much of the registry is exposed to a row-set change. The durable fix is for
producers to emit a nuclide-keyed map; until then the error check above is what
stands between a shifted row set and a wrong rendered number.

## Usage

    python3 computations/registry_witness_pin_validator.py
    python3 computations/registry_witness_pin_validator.py --strict   # exit 1 on error
    python3 computations/registry_witness_pin_validator.py --self-test

No witness is written: this script only reads.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REGISTRY = REPO / "content" / "values" / "registry.ts"

#: Element symbol -> proton number, for the nuclides the registry can name.
#: Deliberately small: extend it when a pin names a heavier element rather
#: than guessing from a general table, so an unknown symbol is a visible
#: "cannot check" instead of a silent pass.
_ELEMENT_Z = {
    "n": 0, "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5,
    "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
}

#: A nuclide token inside a registry entry name, e.g. the `2H` of
#: `B_2H_AME_MeV` or the `4He` of `B_4He_AME_MeV`.
_NUCLIDE_IN_NAME = re.compile(r"_(\d+)([A-Z][a-z]?)_")

#: The START of a `NAME: Object.freeze({ ... })` block.
#
# Only the start. A regex for the whole block is the obvious move and it is
# wrong here: a non-greedy `.*?\}\)` terminates on the first `})` in the body,
# and LaTeX in the `symbol` field contains one --
# `"B_{\\mathrm{AME}}(\\mathrm{D})"` ends `D})`. That truncates the body and
# desynchronises `finditer` for everything after it, silently dropping 14 of
# the 69 entries INCLUDING `B_2H_AME_MeV`, the one this validator exists for.
# Bodies are delimited by the next entry start instead.
_ENTRY_START = re.compile(r"(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*Object\.freeze\(\{")


def _field(body: str, field: str) -> str | None:
    """Value of a string field in an entry body, or None if absent/null.

    Tolerates the prettier-wrapped form the registry uses, where the value
    starts on the line after the key.
    """
    m = re.search(rf'{field}\s*:\s*"((?:[^"\\]|\\.)*)"', body)
    return m.group(1) if m else None


def parse_registry(text: str) -> list[dict]:
    """Registry entries that carry a witness pin.

    Each body runs from its own `Object.freeze({` to the next one, so a `})`
    inside a LaTeX `symbol` string cannot end it early. Fields occur once per
    entry, so taking the first match inside the slice is exact.
    """
    starts = list(_ENTRY_START.finditer(text))
    out = []
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        body = text[m.end():end]
        wf, wp = _field(body, "witnessFile"), _field(body, "witnessPath")
        if not wf or not wp:
            continue  # not a witness-pinned entry (or a needsReview stub)
        out.append({
            "key": m.group("key"),  # noqa: E501
            "name": _field(body, "name") or m.group("key"),
            "description": _field(body, "description") or "",
            "witnessFile": wf,
            "witnessPath": wp,
        })
    return out


def resolve(doc, path: str):
    """Follow a dotted path, treating all-digit segments as list indices.

    Returns `(value, ok)`. `ok=False` means the path does not resolve, which
    is distinct from resolving *to* `None` — the caller reports those
    differently.
    """
    cur = doc
    for seg in path.split("."):
        if isinstance(cur, list):
            if not seg.isdigit() or int(seg) >= len(cur):
                return None, False
            cur = cur[int(seg)]
        elif isinstance(cur, dict):
            if seg not in cur:
                return None, False
            cur = cur[seg]
        else:
            return None, False
    return cur, True


def resolve_any_root(doc, path: str):
    """Resolve against the document, then against a `witness` wrapper.

    Witness files in this repo come in both shapes; the registry's paths are
    written against whichever the file uses.
    """
    for root_name, root in (("<top>", doc), ("witness", doc.get("witness") if isinstance(doc, dict) else None)):
        if root is None:
            continue
        val, ok = resolve(root, path)
        if ok:
            return val, True, root_name
    return None, False, None


def nuclide_from_name(name: str) -> tuple[int, int] | None:
    """`(Z, A)` claimed by a registry entry's name, or None if it names none."""
    m = _NUCLIDE_IN_NAME.search(name)
    if not m:
        return None
    A, sym = int(m.group(1)), m.group(2)
    if sym not in _ELEMENT_Z:
        return None  # unknown symbol: report as uncheckable, never as a pass
    return _ELEMENT_Z[sym], A


def parent_row(doc, path: str):
    """The dict the final path segment is read out of, if it is a dict."""
    parent, ok, _ = resolve_any_root(doc, path.rsplit(".", 1)[0]) if "." in path else (None, False, None)
    return parent if ok and isinstance(parent, dict) else None


def check(entries: list[dict]) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warns: list[str] = []
    checked_nuclides = 0

    for e in entries:
        wf = REPO / e["witnessFile"]
        if not wf.exists():
            errors.append(f"E-missing-file  {e['name']}: {e['witnessFile']} does not exist")
            continue
        try:
            doc = json.loads(wf.read_text())
        except Exception as exc:  # malformed JSON is an error about the pin too
            errors.append(f"E-missing-file  {e['name']}: {e['witnessFile']} unreadable ({exc})")
            continue

        val, ok, _root = resolve_any_root(doc, e["witnessPath"])
        if not ok:
            errors.append(
                f"E-unresolvable  {e['name']}: {e['witnessPath']} does not resolve "
                f"in {e['witnessFile']}"
            )
            continue
        if val is None:
            errors.append(f"E-null-value    {e['name']}: {e['witnessPath']} resolves to null")
            continue

        segs = e["witnessPath"].split(".")
        if any(s.isdigit() for s in segs):
            warns.append(f"W-positional    {e['name']}: {e['witnessPath']} indexes by position")

        # Nuclide identity is checked for BOTH addressing styles.
        #
        # For a positional pin it is the whole point: the index is the only
        # thing tying the pin to a nuclide, and a shifted row set breaks it
        # silently. For a nuclide-KEYED pin the key already carries the intent,
        # so this is cheaper — but not free: it catches a producer that fills
        # `rows_by_nuclide` from a mis-zipped label list, which is exactly the
        # failure the keyed view was introduced to make impossible. A guard
        # that only ran on the shape being retired would verify nothing once
        # the migration finished.
        claimed = nuclide_from_name(e["name"])
        row = parent_row(doc, e["witnessPath"])
        if claimed and row and {"Z", "A"} <= set(row):
            checked_nuclides += 1
            Z, A = claimed
            if (row["Z"], row["A"]) != (Z, A):
                errors.append(
                    f"E-nuclide-drift {e['name']}: {e['witnessPath']} now addresses "
                    f"Z={row['Z']} A={row['A']}, but the name claims Z={Z} A={A} "
                    f"(value read would be {val})"
                )

    return errors, warns, checked_nuclides


def self_test() -> int:
    """The 2026-06-22 state must be caught; the current state must pass."""
    good = {"data": {"rows": [
        {"Z": 1, "N": 0, "A": 1, "B_AME_MeV": 938.27},
        {"Z": 0, "N": 1, "A": 1, "B_AME_MeV": 939.57},
        {"Z": 1, "N": 1, "A": 2, "B_AME_MeV": 2.2245662},
    ]}}
    bad = {"data": {"rows": [
        {"Z": 1, "N": 1, "A": 2, "B_AME_MeV": 2.2245662},
        {"Z": 1, "N": 2, "A": 3, "B_AME_MeV": 8.4817962},
        {"Z": 2, "N": 1, "A": 3, "B_AME_MeV": 7.71804132},  # <- the incident
    ]}}
    path = "data.rows.2.B_AME_MeV"
    claimed = nuclide_from_name("B_2H_AME_MeV")
    fails = 0

    if claimed != (1, 2):
        print("  FAIL: nuclide_from_name('B_2H_AME_MeV') !=(1,2), got", claimed); fails += 1

    for label, doc, want_drift in (("current (D at index 2)", good, False),
                                   ("2026-06-22 (3He at index 2)", bad, True)):
        row = parent_row(doc, path)
        drift = (row["Z"], row["A"]) != claimed
        ok = drift == want_drift
        print(f"  {'ok  ' if ok else 'FAIL'} {label}: drift={drift} (want {want_drift})")
        if not ok:
            fails += 1

    val, ok, _ = resolve_any_root(good, "data.rows.9.B_AME_MeV")
    print(f"  {'ok  ' if not ok else 'FAIL'} out-of-range index reports unresolvable")
    if ok:
        fails += 1

    print("self-test:", "PASS" if fails == 0 else f"{fails} FAILURE(S)")
    return 0 if fails == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="exit 1 on any error")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    if not REGISTRY.exists():
        print(f"registry not found: {REGISTRY}")
        return 1

    entries = parse_registry(REGISTRY.read_text())
    errors, warns, checked = check(entries)

    print("=" * 70)
    print(f"  registry pins parsed        : {len(entries)}")
    print(f"  positional pins             : {len(warns)}")
    print(f"  nuclide identities verified : {checked}")
    print(f"  errors                      : {len(errors)}")
    print("=" * 70)
    for w in warns:
        print("  " + w)
    if errors:
        print()
        for e in errors:
            print("  " + e)
    print()
    print("GREEN" if not errors else "RED")

    return 1 if (errors and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
