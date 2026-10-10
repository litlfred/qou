#!/usr/bin/env python3
"""Verify the `prop-universe-field` criterion per carrier, mechanically.

The defect: a `class`/`structure` field typed with the UNIVERSE `Prop` rather
than with *a* proposition —

    structure DescentData where
      level : ℕ
      restriction_exists : Prop        -- holds a proposition as DATA

The instance chooses the proposition, so `⟨_, True⟩` inhabits the carrier and
any `[DescentData]`-conditional result is unconditional. The audit
(`folio/pipeline/lean-vacuity-axiom-audit.ts`) flags it; this decides it, so
a ledger verdict rests on a re-runnable check rather than on trust.

`legit` requires one of: no bare `Prop` field; an `@marker` / `opaque marker`
opt-out; or a sibling field that genuinely CONSUMES the Prop-valued field.

TWO TRAPS, both measured on this corpus, both failing toward `legit`
-------------------------------------------------------------------
1. **A trailing `--` comment on the field line.** `isBPS : Prop -- placeholder`
   and `is_knot : Prop  -- single-component braid closure` are bare Prop
   fields; a naive `(\\w+)\\s*:\\s*(.+?)$` captures the comment as part of the
   type and the `== "Prop"` test fails. Two false `legit` verdicts came from
   exactly this.

2. **Consumption by a VACUOUS sibling.** `HorizonStructure` has
   `horizon_nonempty : degree_zero_blocked → True`, which does consume
   `degree_zero_blocked` syntactically and constrains nothing: `P → True` is
   provable for every `P`. A consumer whose conclusion is `True` is not a
   consumer.

Both bugs pointed at "not a defect", which is the comfortable answer. Strip
comments before parsing, and reject `→ True` consumers.

Usage:  scripts/lean-prop-universe-field-verify.py [--json OUT]
"""
from __future__ import annotations
import argparse, json, pathlib, re, sys

LEDGER = "docs/audits/lean-vacuity-review-ledger.json"
FIELD = re.compile(r"^\s+\[?(\w+)\s*:\s*(.+?)\s*\]?$")


def strip_line_comment(s: str) -> str:
    """Drop a trailing `--` comment. Trap 1."""
    i = s.find("--")
    return s if i < 0 else s[:i]


def vacuous_consumer(ftype: str, field: str) -> bool:
    """Does this sibling consume `field` only to conclude `True`? Trap 2."""
    if not re.search(rf"(?<![.\w]){re.escape(field)}(?![\w])", ftype):
        return False
    return bool(re.search(r"→\s*True\s*$|->\s*True\s*$", ftype.strip()))


def analyse(path: str, carrier: str) -> dict:
    lines = pathlib.Path(path).read_text(errors="ignore").split("\n")
    i = next((n for n, l in enumerate(lines)
              if re.match(rf"\s*(?:class|structure)\s+{re.escape(carrier)}\b", l)), None)
    if i is None:
        return {"carrier": carrier, "status": "CARRIER-NOT-FOUND"}
    j, fields = i + 1, []
    while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
        m = FIELD.match(strip_line_comment(lines[j]))
        if m:
            fields.append((m.group(1), m.group(2).strip()))
        j += 1
    prop_fields = [f for f, t in fields if t == "Prop"]
    real_consumers = {}
    for f in prop_fields:
        cons = [g for g, t in fields
                if g != f
                and re.search(rf"(?<![.\w]){re.escape(f)}(?![\w])", t)
                and not vacuous_consumer(t, f)]
        if cons:
            real_consumers[f] = cons
    marker = bool(re.search(r"@marker|opaque marker", "\n".join(lines[max(0, i - 25):j])))
    verdict = ("legit" if (marker or not prop_fields
                           or len(real_consumers) == len(prop_fields)) else "genuine")
    return {"carrier": carrier, "status": "OK", "line": i + 1, "file": path,
            "prop_fields": prop_fields, "real_consumers": real_consumers,
            "marker": marker, "verdict": verdict}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    a = ap.parse_args()
    d = json.load(open(LEDGER))
    rows = [(k, v) for k, v in d["entries"].items()
            if v.get("category") == "proof-claims-unencoded"
            and v.get("verdict") == "needs-agent"
            and not v.get("stale_prev_verdict")]
    out = []
    for k, _ in rows:
        path, carrier, _c = k.split("::")
        r = analyse(path, carrier)
        r["key"] = k
        out.append(r)
        if r["status"] != "OK":
            print(f"  {r['status']}  {carrier}")
            continue
        cons = ",".join(f"{f}<-{'/'.join(g)}" for f, g in r["real_consumers"].items()) or "-"
        print(f"  {r['verdict']:<8} {carrier:<38} Prop:{','.join(r['prop_fields']) or '(none)':<30} "
              f"consumed:{cons}")
    n_g = sum(1 for r in out if r.get("verdict") == "genuine")
    print(f"\ngenuine {n_g}   legit {sum(1 for r in out if r.get('verdict')=='legit')}   "
          f"unresolved {sum(1 for r in out if r['status']!='OK')}   of {len(out)}")
    if a.json:
        json.dump(out, open(a.json, "w"), indent=1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
