#!/usr/bin/env python3
"""Triage the vacuity ledger's `genuine` self-assuming-projection queue by
CARRIER SHAPE.

## Why this exists

`proof-no-self-assuming-projection` fires on `theorem foo … := x.field` where
the field's type is the theorem's conclusion. Two very different things have
that *identical* syntax:

  (a) a **definition's accessor** — `x : CategoricalJet` is a structure that
      DEFINES an object, its fields ARE the definition's axioms, and the
      theorem is Mathlib's `mul_assoc := Group.mul_assoc` idiom. Not a defect.

  (b) a **claim carrier's projection** — `x : HasFoo` is a class whose field
      IS the open result, so the theorem derives nothing. The real defect.

The detector cannot separate them (recorded in bean `qou-lo1t`, batch 2), and
neither can binder style: an earlier pass classified 116 entries as
instance-binder vs explicit-arg, read all 30 of the smaller bucket by hand, and
found the split carries no adjudicative content.

## RESULT: all three signals FAIL. Do not re-run this expecting a triage.

The script is kept as the record of a measured negative, so the next agent does
not spend the pass re-deriving it. Three signals were tried and validated
against the ledger's **8 hand-adjudicated `legit`** entries (ground truth for
class (a)) versus its 97 `genuine`:

| signal | legit (n=8) | genuine (n=97) | separates? |
|---|---|---|---|
| carrier holds data fields | 4 DEFINES / 4 ASSERTS | 65 / 30 | **no** — legit splits evenly |
| carrier is inhabited | 3 of 8 (38 %) | 29 of 97 (30 %) | **no** |
| referenced in >= 3 other files | 3 of 8 (38 %) | 2 of 97 (2 %) | one-way only |

The data-field bucket looked like it confirmed the batch-2 hypothesis at 67 %
DEFINES-OBJECT — and that reading is **wrong**, because half the *known* legit
entries land in the other bucket. Setup/parameter data (`Z : ℕ`, `q : ℝ` in a
`…Context`) is indistinguishable from definitional data (`jetObj`, `jetEval` in
a `CategoricalJet`); both are "data", and only the second means "defines an
object".

The third row is real but unusable for draining: it can promote a handful of
`genuine` entries to *suspect*, but 73 of 97 `genuine` and 3 of 8 `legit` both
sit at zero external sites, so it cannot classify the bulk.

**Conclusion: the (a)/(b) call is semantic and stays an agent judgement.** The
`genuine` count is a review queue, not a defect count, and no mechanical
reclassification of it is currently available.

Usage:
    python3 scripts/vacuity-carrier-shape-triage.py
    python3 scripts/vacuity-carrier-shape-triage.py --sample 12 --seed 7
    python3 scripts/vacuity-carrier-shape-triage.py --json out.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import random
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
LEDGER = REPO / "docs/audits/lean-vacuity-review-ledger.json"

# A field whose type mentions any of these is a proposition, not data.
PROP_MARKERS = re.compile(
    r"(?:\s=\s|\s≠\s|\s≤\s|\s<\s|\s≥\s|\s>\s|\s∈\s|\s∣\s|\bProp\b|∀|∃|↔|"
    r"\bSubsingleton\b|\bNonempty\b|\bIsUnit\b|\bMono\b|\bEpi\b|\bFact\b|"
    r"\bDecidable\b|\bIrreducible\b|\bTrue\b|\bFalse\b|\b¬)"
)

DECL_RE = re.compile(
    r"^(?P<kind>class|structure)\s+(?P<name>[A-Za-z_][A-Za-z0-9_'.]*)"
    r"(?P<rest>.*?)(?P<prop>:\s*Prop\s*)?\bwhere\b",
    re.S,
)


def carrier_decls(text: str) -> dict[str, dict]:
    """Map carrier name -> {kind, is_prop, fields:[(name,type)], line}."""
    out: dict[str, dict] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"^(class|structure)\s+([A-Za-z_][A-Za-z0-9_'.]*)", line)
        if not m:
            continue
        kind, name = m.group(1), m.group(2)
        # Header may wrap over several lines until `where`.
        header, j = [], i
        while j < len(lines):
            header.append(lines[j])
            if re.search(r"\bwhere\b", lines[j]):
                break
            if j > i and re.match(r"^\S", lines[j]) and "where" not in lines[j]:
                break  # header ended without `where` (extends-only / no fields)
            j += 1
        head = "\n".join(header)
        is_prop = bool(re.search(r":\s*Prop\s*(?:\bwhere\b|$)", head))

        # Field block: indented `name : type` lines until dedent to column 0.
        fields: list[tuple[str, str]] = []
        k = j + 1
        while k < len(lines):
            ln = lines[k]
            if ln.strip() and not ln.startswith((" ", "\t")):
                break
            fm = re.match(r"^\s+(?:/--.*)?([A-Za-z_][A-Za-z0-9_']*)\s*:\s*(.+)$", ln)
            if fm and not ln.lstrip().startswith(("--", "/-", "-/")):
                ftype = fm.group(2)
                k2 = k + 1
                while k2 < len(lines) and re.match(r"^\s{6,}\S", lines[k2]) and \
                        not re.match(r"^\s+[A-Za-z_][A-Za-z0-9_']*\s*:", lines[k2]):
                    ftype += " " + lines[k2].strip()
                    k2 += 1
                fields.append((fm.group(1), ftype.strip()))
            k += 1
        out[name] = {"kind": kind, "is_prop": is_prop, "fields": fields, "line": i + 1}
    return out


def is_data_field(ftype: str) -> bool:
    return not PROP_MARKERS.search(ftype)


def carrier_usage(carrier: str | None, home: str) -> dict:
    """Two signals that are about the carrier's ROLE, not its field types.

    * `sites`  — files mentioning the carrier other than its own. A structure
      that DEFINES an object gets constructed and consumed in several places;
      a claim carrier invented to host one theorem is mentioned only where it
      was declared.
    * `inhabited` — does anything build one? An open claim carrier has no
      instance (that is the honest open state, §3b-tax); a definition of an
      object is instantiated.
    """
    if not carrier:
        return {"sites": None, "inhabited": None}
    short = carrier.split(".")[-1]
    pat = re.compile(r"\b" + re.escape(short) + r"\b")
    sites, inhabited = set(), False
    for p in REPO.glob("content/**/*.lean"):
        rel = str(p.relative_to(REPO))
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not pat.search(txt):
            continue
        if rel != home:
            sites.add(rel)
        if re.search(r"^\s*(?:noncomputable\s+)?(?:instance|def|abbrev|example)"
                     r"[^\n:]*:\s*(?:[^\n]*\s)?" + re.escape(short) + r"\b",
                     txt, re.M):
            inhabited = True
    return {"sites": len(sites), "inhabited": inhabited}


def classify(entry_key: str, entry: dict) -> dict:
    relpath, decl, _cat = entry_key.split("::", 2)
    p = REPO / relpath
    res = {"key": entry_key, "file": relpath, "decl": decl,
           "carrier": None, "shape": "unknown", "why": "", "data_fields": []}
    if not p.exists():
        res["why"] = "file missing"
        return res
    text = p.read_text(encoding="utf-8", errors="replace")
    decls = carrier_decls(text)

    # Find the theorem and read its binders + body.
    short = decl.split(".")[-1]
    tm = re.search(
        r"^(?:theorem|lemma|def|instance|abbrev)\s+(?:[A-Za-z0-9_'.]*\.)?"
        + re.escape(short) + r"\b(?P<sig>.*?):=(?P<body>.*?)(?=\n\S|\Z)",
        text, re.S | re.M)
    if not tm:
        res["why"] = "declaration not located"
        return res
    sig, body = tm.group("sig"), tm.group("body")

    # The projection: `foo.bar` in the body -> binder `foo`.
    pm = re.search(r"\b([a-zA-Z_][A-Za-z0-9_']*)\.([a-zA-Z_][A-Za-z0-9_']*)", body)
    binder = pm.group(1) if pm else None

    carrier = None
    if binder:
        bm = re.search(r"[\[(]\s*" + re.escape(binder)
                       + r"\s*:\s*([A-Za-z_][A-Za-z0-9_'.]*)", sig)
        if bm:
            carrier = bm.group(1)
    if carrier is None:
        # Anonymous instance binder: `[Foo X]` with the body using `Foo.field`.
        bm = re.search(r"\[\s*([A-Z][A-Za-z0-9_'.]*)", sig)
        if bm:
            carrier = bm.group(1)
    res["carrier"] = carrier

    key = carrier.split(".")[-1] if carrier else None
    info = decls.get(key) if key else None
    if info is None:
        res["shape"] = "carrier-not-in-file"
        res["why"] = f"carrier {carrier!r} not declared in this file"
        return res

    data = [f for f in info["fields"] if is_data_field(f[1])]
    res["data_fields"] = [f"{n} : {t}" for n, t in data][:6]
    if info["is_prop"] or not data:
        res["shape"] = "ASSERTS"
        res["why"] = (f"{info['kind']} {key}"
                      + (" : Prop" if info["is_prop"] else "")
                      + f" — {len(info['fields'])} field(s), 0 data")
    else:
        res["shape"] = "DEFINES-OBJECT"
        res["why"] = (f"{info['kind']} {key} — {len(data)} data field(s) "
                      f"of {len(info['fields'])}")
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=10,
                    help="how many rows to print for hand-checking (0 = none)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--json", type=pathlib.Path)
    args = ap.parse_args()

    led = json.loads(LEDGER.read_text())
    rows = [classify(k, v) for k, v in led["entries"].items()
            if v.get("verdict") == "genuine"
            and v.get("category") == "proof-no-self-assuming-projection"]

    buckets: dict[str, list] = {}
    for r in rows:
        buckets.setdefault(r["shape"], []).append(r)

    print(f"genuine self-assuming-projection entries: {len(rows)}\n")
    for shape in sorted(buckets, key=lambda s: -len(buckets[s])):
        n = len(buckets[shape])
        print(f"  {shape:<22} {n:>4}   ({100*n/len(rows):.0f}%)")
    print("\nThis is a CANDIDATE split, not a verdict — hand-check before quoting it.\n")

    if args.sample:
        rnd = random.Random(args.seed)
        print(f"--- hand-check sample (seed {args.seed}) ---")
        for shape in sorted(buckets, key=lambda s: -len(buckets[s])):
            pool = buckets[shape]
            for r in rnd.sample(pool, min(args.sample, len(pool))):
                print(f"[{shape}] {r['decl']}  ({r['file']})")
                print(f"    carrier: {r['carrier']}  |  {r['why']}")
                if r["data_fields"]:
                    print(f"    data: {'; '.join(r['data_fields'])}")
            print()

    if args.json:
        args.json.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
