#!/usr/bin/env python3
# polynomial_q_not_applicable: static provenance audit, emits no numeric physics.
"""Does a witness's `scriptFile` actually WRITE that witness?

Owner directive: NO FLOAT64 — this is the provenance half of the same
discipline: a number is only as trustworthy as the claim about where it came
from.

## The defect

`scriptFile` is treated everywhere as "the producer": `run_pipeline.py`
regenerates through it, `producer_repad_sweep.py` attributes padding by it, and
the P30 triage in
`docs/audits/2026-08-07-producer-repadding-empirical-sweep.md` counted with it.
**Nothing checks it.**

Six `chi-*.witness.json` name `delta_lambda_empirical_tabulation.py`. That
script reads them as `chi_witness` *inputs* and never writes them — nor does
any other script in the corpus. Re-running the named producer therefore does
nothing at all, which is exactly what was measured: `rc=0`, no `scriptHash`
gained, not one value moved. A witness naming a real script is not evidence
that the script produces it.

## Three verdicts, and the middle one is the point

Writing is not statically decidable in general — a path can be built from
variables, a loop, a config. So this reports what it can prove and refuses to
guess:

| verdict | meaning |
|---|---|
| `WRITES` | a `WitnessBuilder` name matches the stem — literal, or an f-string matched as a pattern |
| `UNCONFIRMED` | the script mentions *some* witness, or builds one under a computed name — cannot confirm, cannot deny |
| `NOT_A_PRODUCER` | the script mentions **no witness at all** — the claim cannot be true |

`UNCONFIRMED` is deliberately not folded into either neighbour. The `chi-*`
case is a filename that *appears* in the named script, so a "mentions it" test
would have called it a producer and reproduced the original error. Only
`NOT_A_PRODUCER` is asserted as wrong; `UNCONFIRMED` is asserted as unchecked,
which is a different and honest thing to say.

**Three times the rule was too aggressive, and each cost an order of
magnitude** — 324 → 189 → 28 → 3. Missing `WitnessBuilder.wrap_legacy` (229
call sites); treating an f-string name as unknowable rather than as a pattern;
and requiring the *concrete* filename when a script may write through a
computed path. Each intermediate was a plausible number, and each died on
reading one cited file. Hence the final rule's conservatism: absence is only
claimed when the script mentions no witness whatsoever.

## Why not just re-run and see

Because a re-run that writes nothing is indistinguishable from a producer whose
output happens to be unchanged — and that is the confusion this whole audit
arc keeps paying for. Static attribution answers "is this claim structurally
possible", which is the question `run_pipeline` needs before it decides a
witness is current.

## The three survivors, triaged

All three verified by hand; each has a different cause, and none is fixable by
re-running:

- **`kite_tail_reconciliation.witness.json`** — rename residue. The script
  writes `kite-tail-reconciliation` (hyphens) via `WitnessBuilder`, and the
  underscore-named file is a stale duplicate left behind by the rename. **Both
  are committed.** The tool is right to reject the claim: the named script
  produces the *other* file.
- **`psl27-irrep-verification.witness.json`** — no script in the corpus
  mentions it. A true orphan.
- **`sigma-all-evaluator.witness.json`** — its only producer,
  `build_sigma_all_evaluator_witness.py`, lives in `_deprecated/`. Orphaned by
  a deprecation.

None can be regenerated, and `run_pipeline` treats all three as current.
Deleting or re-attributing them is a corpus decision, not a tool fix, so this
records rather than acts.

## The 466 UNCONFIRMED, triaged — and why the obvious upgrade is unsafe

| | witnesses | shape |
|---:|---|---|
| **250** | no `WitnessBuilder` at all | hand-rolled `json.dump` / `write_text` |
| **197** | imports it, no resolvable constructor | `WitnessBuilder.stamp_staleness_metadata(...)` — 185 call sites |
| 15 | a builder exists, but no name matches | |
| 2 | name from a variable | |
| 2 | syntax error | |

The 197 are a **fourth** builder shape, found the same way as `wrap_legacy`:
`adjacent_vs_full_probe.py` assembles the payload by hand, writes it to
`Path(__file__).parent / "adjacent-vs-full-probe.witness.json"`, then calls
`stamp_staleness_metadata` for the metadata. They genuinely do produce their
witness, and the concrete filename is right there as a literal.

**The tempting upgrade — "literal filename present + the file writes something
⇒ WRITES" — is exactly the original bug.** `delta_lambda_empirical_tabulation`
contains the literal `"chi-proton-h3.witness.json"` *and* writes a witness of
its own; that rule would call it the producer of six witnesses it only reads,
which is the error this tool exists to catch. Upgrading these needs real
dataflow — the literal must reach a write, not merely coexist with one — so
they stay `UNCONFIRMED` until someone does that properly.

Usage:
    python3 computations/witness_provenance_audit.py
    python3 computations/witness_provenance_audit.py --strict     # exit 1 on NOT_A_PRODUCER
    python3 computations/witness_provenance_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import re
import json
import sys
from pathlib import Path

_DYNAMIC = "\x01re:"
_OPAQUE = "\x01opaque"

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def builder_names(tree: ast.AST) -> set[str]:
    """Witness stems this script constructs a WitnessBuilder for.

    Accepts `WitnessBuilder("stem")` and `WitnessBuilder(name="stem")`; a
    non-literal name is unknowable statically and is skipped, which pushes the
    witness to UNCONFIRMED rather than to a false NOT_A_PRODUCER.
    """
    out: set[str] = set()
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        # Two shapes construct a named witness:
        #   WitnessBuilder(...)                — direct
        #   WitnessBuilder.wrap_legacy(stem,…) — 229 call sites, and missing it
        #                                        put 300+ witnesses in
        #                                        NOT_A_PRODUCER on the first cut.
        if isinstance(f, ast.Attribute):
            owner = getattr(f.value, "id", "")
            if not (owner == "WitnessBuilder" and f.attr == "wrap_legacy"):
                continue
        elif getattr(f, "id", "") != "WitnessBuilder":
            continue
        cand = list(n.args[:1]) + [kw.value for kw in n.keywords if kw.arg == "name"]
        for c in cand:
            if isinstance(c, ast.Constant) and isinstance(c.value, str):
                out.add(c.value)
            elif isinstance(c, ast.JoinedStr):
                # A parameterised name: f"A-operator-extract-h{n}-{iface}".
                # The literal segments are still a pattern, so turn it into one
                # rather than give up — treating a dynamic name as "produces
                # nothing" put ~135 witnesses in NOT_A_PRODUCER on the second cut.
                parts = ["".join(re.escape(v.value)) if isinstance(v, ast.Constant)
                         and isinstance(v.value, str) else "\x00"
                         for v in c.values]
                out.add(_DYNAMIC + "^" + "".join(
                    p if p != "\x00" else ".+" for p in parts) + "$")
            else:
                out.add(_OPAQUE)   # name from a variable: unknowable either way
    return out


def classify(source: str, witness_filename: str) -> str:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return "UNCONFIRMED"
    stem = witness_filename[: -len(".witness.json")]
    names = builder_names(tree)
    if stem in names:
        return "WRITES"
    for n in names:
        if n.startswith(_DYNAMIC) and re.match(n[len(_DYNAMIC):], stem):
            return "WRITES"
    if _OPAQUE in names:
        # The script builds a witness whose name is computed. Cannot confirm it
        # is this one; cannot assert it is not. That is what UNCONFIRMED is for.
        return "UNCONFIRMED"
    # Conservative: a script that mentions ".witness.json" AT ALL may be writing
    # this one through a computed path — chi_at_q0_via_hoefsmit_mpfr writes
    # `chi-{atom}-h{n}-at-q0-50dps.witness.json` via a helper, so the concrete
    # name never appears. Only a script that never mentions a witness can be
    # asserted not to produce one.
    return "UNCONFIRMED" if ".witness.json" in source else "NOT_A_PRODUCER"


def scan(root: Path) -> list[dict]:
    comp = root / "computations"
    scripts = {p.name: p for p in comp.rglob("*.py") if "_deprecated" not in p.parts}
    out: list[dict] = []
    for w in sorted(comp.rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        sf = d.get("scriptFile")
        if not sf or sf.startswith("("):
            # No claim, or a prose annotation someone already triaged by hand.
            continue
        src_path = scripts.get(Path(sf).name)
        if src_path is None:
            out.append({"witness": w.relative_to(root).as_posix(), "scriptFile": sf,
                        "verdict": "SCRIPT_MISSING"})
            continue
        try:
            src = src_path.read_text(encoding="utf-8")
        except Exception:
            continue
        out.append({"witness": w.relative_to(root).as_posix(), "scriptFile": sf,
                    "verdict": classify(src, w.name)})
    return out


CASES = [
    ("builder positional", 'WitnessBuilder("chi-proton-h3")', "chi-proton-h3.witness.json", "WRITES"),
    ("builder keyword", 'WitnessBuilder(name="foo-bar", engine="python")', "foo-bar.witness.json", "WRITES"),
    ("wrap_legacy (229 call sites)", 'WitnessBuilder.wrap_legacy("foo-bar", payload)', "foo-bar.witness.json", "WRITES"),
    ("wrap_legacy for a different stem", 'WitnessBuilder.wrap_legacy("other", p)', "foo-bar.witness.json", "NOT_A_PRODUCER"),
    ("f-string name resolves as a pattern",
     'WitnessBuilder(f"A-operator-extract-h{n}-{iface}")',
     "A-operator-extract-h9-pn.witness.json", "WRITES"),
    ("f-string pattern that does NOT match",
     'WitnessBuilder(f"A-operator-extract-h{n}-{iface}")',
     "unrelated-thing.witness.json", "NOT_A_PRODUCER"),
    ("name from a variable: unknowable, so UNCONFIRMED",
     'WitnessBuilder(nm)', "anything.witness.json", "UNCONFIRMED"),
    ("unrelated attribute call", 'x.some_method("foo-bar")', "foo-bar.witness.json", "NOT_A_PRODUCER"),
    # The exact shape that fooled the original triage: the filename is present,
    # but only as an input the script READS.
    ("reads it as an input", '{"chi_witness": "chi-proton-h3.witness.json"}',
     "chi-proton-h3.witness.json", "UNCONFIRMED"),
    ("hand-rolled write", 'Path("out.witness.json").write_text(j)', "out.witness.json", "UNCONFIRMED"),
    ("never mentions a witness at all", 'x = 1\n', "orphan.witness.json", "NOT_A_PRODUCER"),
    ("templated path via a helper", 'OUT = f"chi-{atom}-h{n}.witness.json"',
     "chi-deuteron-h6.witness.json", "UNCONFIRMED"),
    ("builder for a DIFFERENT witness, no other mention",
     'WitnessBuilder("other")', "orphan.witness.json", "NOT_A_PRODUCER"),
    ("non-literal keyword name: also UNCONFIRMED, never asserted absent",
     'WitnessBuilder(name=nm)', "orphan.witness.json", "UNCONFIRMED"),
    ("syntax error degrades to unconfirmed", 'def (:', "x.witness.json", "UNCONFIRMED"),
]


def self_test() -> int:
    fails = 0
    for label, src, wf, want in CASES:
        got = classify(src, wf)
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any witness names a script that cannot produce it")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--list", choices=["NOT_A_PRODUCER", "UNCONFIRMED", "SCRIPT_MISSING", "WRITES"])
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    rows = scan(Path(a.root).resolve())
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print(f"witness-provenance: {len(rows)} witnesses carry a scriptFile claim\n")
    for k in ("WRITES", "UNCONFIRMED", "NOT_A_PRODUCER", "SCRIPT_MISSING"):
        print(f"  {k:<16} {counts.get(k, 0)}")
    if a.list:
        print(f"\n--- {a.list} ---")
        for r in rows:
            if r["verdict"] == a.list:
                print(f"  {r['witness']}  -> {r['scriptFile']}")
    bad = counts.get("NOT_A_PRODUCER", 0)
    if bad:
        print(f"\n{bad} witness(es) name a script that provably cannot produce them.")
        print("Re-running those regenerates nothing; run_pipeline still treats them as current.")
    return 1 if (a.strict and bad) else 0


if __name__ == "__main__":
    raise SystemExit(main())
