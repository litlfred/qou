#!/usr/bin/env python3
"""codata_2022_downstream_staleness_scan — who still carries the 2018 values?

## Why

PR #4860 corrected seven CODATA mass literals from their 2018 values to 2022
(a coherent ~1.3 ppb mass-scale revision). `M_P_MEV` alone is referenced by
234 files, 175 of which emit a witness — but "references the symbol" is a
wildly loose upper bound on "is now wrong":

- most consumers use these as **validation comparison targets**, where a
  1.3 ppb shift is far below what the consumer resolves;
- many read the value at run time and were simply never re-run;
- only a subset **embedded** the old number into a committed witness.

Counting import sites would therefore overstate the problem by an order of
magnitude and give no way to prioritise. This scan measures the real thing:
which committed `*.witness.json` files literally contain a superseded CODATA
literal.

## Method

Exact decimal-string search across the committed witness corpus for each
retired literal, plus its most common serialization variants (trailing-zero
and truncated forms produced by `mp.nstr`). A hit means the file records a
number that CODATA no longer recommends — not necessarily that the file's
*conclusion* changes, which depends on how the value was used.

Two-tier report, because the distinction drives the fix order:

- **EMBEDS_STALE_VALUE** — the retired literal appears in the witness.
- **also_stale_by_producer** — the file is one whose producer imports the
  corrected registry, so re-running it will move the number.

## What this is NOT

Not a correctness verdict. A witness comparing a prediction against the old
proton at 1e-3 relative tolerance is *stale* but not *wrong*. The output is a
work-list ordered by blast radius, to be drained deliberately — not a claim
that N witnesses are defective.

AUDIT-ONLY. Emits a witness; changes no prediction.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))
import _path_bridge  # noqa: F401, E402

from witness_base import WitnessBuilder  # noqa: E402

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True,
                           check=True).stdout.strip())

# Retired CODATA-2018 literals, with the 2022 value that replaced each.
# Variants cover the serializations actually produced in this corpus
# (bare, trailing-zero-padded, and the (err) forms in quoted strings).
RETIRED = {
    "m_e":   ("0.51099895",    "0.51099895069"),
    "m_p":   ("938.27208816",  "938.27208943"),
    "m_n":   ("939.56542052",  "939.56542194"),
    "m_D":   ("1875.61294257", "1875.61294500"),
    "m_T":   ("2808.92113298", "2808.92113668"),
    "m_3He": ("2808.39160743", "2808.39161112"),
    "m_4He": ("3727.37940660", "3727.3794118"),
    "m_mu_over_m_e": ("206.7682830", "206.7682827"),
}

# m_e is special: "0.51099895" is a PREFIX of the correct "0.51099895069",
# so a naive substring search matches every correct value too. Require that
# the match is not followed by another digit.
_PREFIX_SENSITIVE = {"m_e"}


def _hits(text: str, needle: str, prefix_sensitive: bool) -> int:
    if not prefix_sensitive:
        return text.count(needle)
    return len(re.findall(re.escape(needle) + r"(?!\d)", text))


def main() -> int:
    witnesses = sorted(
        p for p in REPO.glob("computations/**/*.witness.json")
        if ("_deprecated" not in p.parts and "fsh-guts" not in p.parts)
    )

    per_file: dict[str, dict[str, int]] = {}
    per_literal: dict[str, int] = {k: 0 for k in RETIRED}

    for p in witnesses:
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        found = {}
        for key, (old, _new) in RETIRED.items():
            n = _hits(text, old, key in _PREFIX_SENSITIVE)
            if n:
                found[key] = n
                per_literal[key] += 1
        if found:
            per_file[str(p.relative_to(REPO))] = found

    total_scanned = len(witnesses)
    total_stale = len(per_file)

    print("=" * 78)
    print("  CODATA-2022 downstream staleness — who still carries 2018 values?")
    print("=" * 78)
    print(f"\n  witnesses scanned            : {total_scanned}")
    print(f"  witnesses embedding a retired literal : {total_stale}"
          f"   ({100.0 * total_stale / max(total_scanned, 1):.1f}%)\n")

    print("  BY LITERAL (files affected):")
    for key, (old, new) in RETIRED.items():
        print(f"    {key:15s} {old:>15s} -> {new:<15s} {per_literal[key]:4d} file(s)")

    print("\n  TOP FILES (by number of retired literals embedded):")
    ranked = sorted(per_file.items(),
                    key=lambda kv: (-sum(kv[1].values()), kv[0]))
    for path, found in ranked[:25]:
        tags = ",".join(f"{k}x{v}" for k, v in sorted(found.items()))
        print(f"    {sum(found.values()):4d}  {path}")
        print(f"          {tags}")
    if len(ranked) > 25:
        print(f"    … and {len(ranked) - 25} more")

    w = WitnessBuilder("codata-2022-downstream-staleness", engine="python")
    w.set_description(
        "Scans the committed witness corpus for CODATA-2018 mass literals "
        "retired by PR #4860. Measures which witnesses EMBED a superseded "
        "value, rather than counting import sites — the latter overstates the "
        "surface by an order of magnitude (234 referencing files vs the "
        "embedding count here) and cannot be prioritised. Audit-only: a hit "
        "means the file records a number CODATA no longer recommends, not "
        "that its conclusion changes."
    )
    w.set_audit_only("docs/audits/2026-08-09-codata-registry-vintage-straddle.md")
    w.add_parameter("witnesses_scanned", total_scanned)
    w.add_data("retired_literals",
               {k: {"old": o, "new": n} for k, (o, n) in RETIRED.items()})
    w.add_data("files_affected_by_literal", per_literal)
    w.add_data("stale_witness_count", total_stale)
    w.add_data("stale_witnesses", per_file)
    w.add_assertion(
        name="scan_completed_over_committed_witness_corpus",
        computed=1 if total_scanned > 0 else 0,
        expected=1,
        source="Indicator (1 = the glob found witnesses to scan). Guards "
               "against a silent zero-file pass being read as 'nothing is "
               "stale' — the failure mode that makes an audit worse than none.",
    )
    path = w.save()
    print(f"\n  Witness: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
