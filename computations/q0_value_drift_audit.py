#!/usr/bin/env python3
# polynomial_q_not_applicable: static value audit; emits no numeric physics.
"""q0-value drift audit — catch stale substrate anchors, and RATCHET.

Bean: follow-up to `qou-ny4j` (the 73.6 ppQ stale `z`), which turned out to
be one instance of a corpus-wide class.

**The problem.** A witness or table that embeds `q_0` freezes whatever value
the producer had at the time. When the canonical pinning is re-solved, every
frozen copy silently goes stale. Nothing downstream notices, because a
q0-derived number has no independent check (see
`docs/audits/2026-08-06-markov-loop-value-rank-audit.md` §1).

**What this does.** Scans `*.witness.json` for q0-bearing fields, compares
each against the documented anchors at 65 dps, and classifies:

| class | meaning |
|---|---|
| `canonical` | matches the CAL-2 muon pin — the `computations/` layer convention |
| `proton-pin` | ~11.54 ppb below canonical: the documented physical-observations layer (`AGENTS.md` §q₀ anchor convention). **Legitimate, not drift.** |
| `STALE` | close to canonical but matching no documented pin |
| `unknown` | far from every anchor — needs a human look |

**Ratchet, not big-bang.** The existing backlog is large (203 live witnesses
at the time of writing). Demanding it drain before the gate turns on would
mean the gate never turns on, so instead:

* `--strict` fails only on stale values **not already in the baseline**
  (`q0-drift-baseline.json`). New staleness is blocked immediately; the
  historical backlog is recorded, not ignored.
* `--rebaseline` regenerates the baseline. Use it **only** when draining
  (the count must go DOWN); it is not a way to silence a new failure.

Two things this deliberately does NOT do:

* It does not rewrite witnesses. A stale witness is fixed by **re-running
  its producer**, never by hand-editing the number — the same discipline
  applied when fixing `q-beta-spectral-bridge-table-data.md`.
* It does not treat the proton pin as drift. Both layers are documented and
  intentional; conflating them would be the exact mistake `AGENTS.md`
  §"Recurring bug to watch (bean `tnjb`)" warns about.

Output: `q0-value-drift-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from mpmath import mp, mpf
except ImportError:  # pragma: no cover
    print("mpmath required", file=sys.stderr)
    raise

mp.dps = 65

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASELINE = HERE / "q0-drift-baseline.json"

# Documented anchors. Canonical is the CAL-2 muon pin carried by
# q-pinning-50-digit.witness.json; the proton pin is the physical-
# observations layer (AGENTS.md §q₀ anchor convention).
Q_CANONICAL = mpf("1.10997859555733471989976322048322502665620840878015368660798114614493")
PROTON_PIN_PPB = mpf("-11.5371")     # measured offset of the proton-pinned value
PIN_TOL_PPB = mpf("0.5")             # how close to a named pin counts as that pin

# Field names that carry a substrate anchor. `q_star` / `qstar` are a
# DIFFERENT parameter (the decay-sector q*) and are deliberately excluded.
Q0_FIELD = re.compile(r"^(q_?0|q_?0_\d+dps|q0Value|q_zero|substrate_q)$", re.I)
EXCLUDE_FIELD = re.compile(r"star|\*|anchor$|err|sigma|unit", re.I)

# Only values in this neighbourhood are substrate anchors at all.
Q_LO, Q_HI = mpf("1.1"), mpf("1.12")


def _ppb(x: mpf) -> mpf:
    return (x - Q_CANONICAL) / Q_CANONICAL * mpf(10) ** 9


def classify(x: mpf) -> tuple[str, mpf]:
    d = _ppb(x)
    if abs(d) < mpf("1e-6"):
        return "canonical", d
    if abs(d - PROTON_PIN_PPB) < PIN_TOL_PPB:
        return "proton-pin", d
    if abs(d) < mpf("100"):
        return "STALE", d
    return "unknown", d


def _walk(obj, path: str, out: list) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}" if path else k
            if isinstance(v, (str, float, int)) and Q0_FIELD.match(k) and not EXCLUDE_FIELD.search(k):
                try:
                    x = mpf(str(v))
                except Exception:
                    continue
                if Q_LO < x < Q_HI:
                    cls, d = classify(x)
                    out.append({"field": p, "value": str(v), "class": cls,
                                "ppb_vs_canonical": float(d)})
            else:
                _walk(v, p, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _walk(v, f"{path}[{i}]", out)


def scan() -> list[dict]:
    rows: list[dict] = []
    for p in sorted(HERE.rglob("*.witness.json")):
        rel = p.relative_to(ROOT).as_posix()
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        found: list = []
        _walk(data, "", found)
        for f in found:
            rows.append({"file": rel, **f})
    return rows


def layer_mismatches(canonical_rows: list) -> list:
    """`canonical`-classed values whose PRODUCER is no longer in the muon layer.

    `canonical` here means "matches the CAL-2 muon pin", which the header table
    defines as *the `computations/` layer convention* — not as the framework's
    canonical anchor. That was accurate when written. On 2026-08-19,
    `q0_anchor_manifest.json`'s `_migration_2026_08_19` moved **255** producers
    out of `ideal_muon` on owner authorisation, leaving 3.

    The class definition did not follow, and `canonical` is the one class that can
    never be `STALE`. So a witness written by a now-proton-layer producer, still
    carrying the muon pin, is invisible to this audit's staleness test.

    Diagnostic only: printed, never written to the witness, and it cannot change
    the exit code. Acting on it would move ~162 witnesses into `STALE`, none of
    them baselined, which fails a blocking gate — and `--rebaseline` is documented
    *"only when draining … not a way to silence a new failure"*. That choice is
    the owner's (bean `qou-fd0e`).
    """
    try:
        man = json.loads((HERE / "q0_anchor_manifest.json").read_text())
    except Exception as exc:  # noqa: BLE001 — reported, never silently empty
        return [{"error": f"manifest unreadable: {exc}"}]
    ideal = set(man.get("ideal_muon", []))
    repo = HERE.parent
    out, legit, unresolved, seen = [], [], [], set()
    for r in canonical_rows:
        f = r.get("file")
        if not f or f in seen:
            continue
        seen.add(f)
        # Resolve relative to the repo, not the process cwd.
        cand = Path(f) if Path(f).is_absolute() else (repo / f)
        if not cand.exists():
            hits = list(repo.rglob(Path(f).name))
            if not hits:
                unresolved.append({"witness": f, "why": "file not found"})
                continue
            cand = hits[0]
        try:
            sf = json.loads(cand.read_text()).get("scriptFile") or ""
        except Exception as exc:  # noqa: BLE001
            unresolved.append({"witness": f, "why": f"unreadable ({type(exc).__name__})"})
            continue
        stem = Path(str(sf)).stem
        if not stem:
            unresolved.append({"witness": f, "why": "no scriptFile"})
        elif stem in ideal:
            legit.append({"witness": f, "producer": stem})
        else:
            out.append({"witness": f, "producer": stem})
    # Three explicit classes. An UNRESOLVED witness is not evidence of either
    # verdict — reporting it by subtraction would count "could not check" as
    # "legitimately muon", which is the exact defect this session has been
    # cataloguing (beans qou-0uqm, qou-i5jy).
    return {"mismatch": out, "legit": legit, "unresolved": unresolved}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on stale values NOT already in the baseline")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (only when draining — count must go DOWN)")
    ap.add_argument("--layer-check", action="store_true",
                    help="report `canonical`-classed values whose producer is no "
                         "longer in the manifest's ideal_muon layer. Diagnostic: "
                         "printed, not written to the witness, cannot change the "
                         "exit code.")
    args = ap.parse_args()

    rows = scan()
    by = {}
    for r in rows:
        by.setdefault(r["class"], []).append(r)
    stale = by.get("STALE", [])
    unknown = by.get("unknown", [])

    print("=" * 74)
    print("q0-VALUE DRIFT AUDIT")
    print("=" * 74)
    for cls in ("canonical", "proton-pin", "STALE", "unknown"):
        n = len(by.get(cls, []))
        note = {"proton-pin": "  (documented physical-observations layer — legitimate)",
                "canonical": "  (CAL-2 muon pin — the computations/ convention)"}.get(cls, "")
        print(f"  {cls:<12} {n:>5}{note}")
    print(f"  {'TOTAL':<12} {len(rows):>5} q0-bearing fields in *.witness.json")

    prior = []
    if BASELINE.exists():
        prior = json.loads(BASELINE.read_text())["stale_keys"]
    key = lambda r: f"{r['file']}::{r['field']}"
    new_stale = [r for r in stale if key(r) not in set(prior)]

    if stale:
        print(f"\n  stale total: {len(stale)}   baseline: {len(prior)}   NEW: {len(new_stale)}")
        if new_stale:
            print("\n  NEW stale (not in baseline) — fix by RE-RUNNING THE PRODUCER,")
            print("  never by hand-editing the number:")
            for r in new_stale[:25]:
                print(f"    {r['file']}  {r['field']}  ({r['ppb_vs_canonical']:+.3g} ppb)")
            if len(new_stale) > 25:
                print(f"    ... and {len(new_stale) - 25} more")
    if unknown:
        print(f"\n  ⚠ {len(unknown)} value(s) matching no anchor — needs a human look:")
        for r in unknown[:10]:
            print(f"    {r['file']}  {r['field']} = {r['value']}")

    if args.rebaseline:
        BASELINE.write_text(json.dumps(
            {"note": "Known-stale q0 fields. Regenerate ONLY when draining; "
                     "the count must go DOWN. Not a way to silence a new failure.",
             "count": len(stale),
             "stale_keys": sorted(key(r) for r in stale)}, indent=2) + "\n")
        print(f"\nRebaselined: {len(stale)} stale keys recorded.")

    out = HERE / "q0-value-drift-audit.witness.json"
    out.write_text(json.dumps({
        "schema": "witness/v1",
        "name": "q0-value-drift-audit",
        "description": "Substrate-anchor drift across witness JSONs. proton-pin is "
                       "legitimate (documented layer); STALE matches no documented pin.",
        "data": {"counts": {k: len(v) for k, v in by.items()},
                 "stale_total": len(stale), "new_stale": len(new_stale),
                 "rows": rows},
    }, indent=2) + "\n")
    print(f"\nWrote {out.name}")

    if args.layer_check:
        mism = layer_mismatches(by.get("canonical", []))
        print("\n" + "=" * 66)
        print("  producer-layer check (--layer-check, diagnostic only)")
        print("=" * 66)
        if isinstance(mism, list) and mism and "error" in mism[0]:
            print(f"  {mism[0]['error']}")
        else:
            n_canon_files = len({r["file"] for r in by.get("canonical", [])})
            bad, ok, unk = mism["mismatch"], mism["legit"], mism["unresolved"]
            print(f"  canonical-classed witness files            : {n_canon_files}")
            print(f"  producer NOT in ideal_muon (blind to STALE): {len(bad)}")
            print(f"  legitimately muon-layer                    : {len(ok)}")
            print(f"  UNRESOLVED (not evidence either way)       : {len(unk)}")
            mism = bad
            for m in mism[:20]:
                print(f"    {m['witness'][:52]:54} <- {m['producer']}")
            if len(mism) > 20:
                print(f"    … and {len(mism) - 20} more")
        print("\n  Exit code unchanged — `new_stale` remains the only gate.")

    return 1 if (args.strict and new_stale) else 0


if __name__ == "__main__":
    sys.exit(main())
