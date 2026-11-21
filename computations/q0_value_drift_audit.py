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
#
# BOTH ARE RESOLVED LIVE.  They used to be transcribed literals here:
#
#     Q_CANONICAL    = mpf("1.10997859555733471989...")   # the frozen anchor
#     PROTON_PIN_PPB = mpf("-11.5371")                    # measured against it
#
# and that is a defect of exactly the kind this audit exists to detect.  A
# drift detector whose reference is a transcription cannot see the reference
# drift.  Concretely, under the 2026-08-22 owner ruling ("A --> CODATA 2022")
# the anchor moves +0.0769 ppb, and a transcribed Q_CANONICAL would then have
# classified every CORRECTLY migrated witness as STALE while calling the
# superseded value canonical -- the ratchet inverted, pointing at the fix
# instead of the defect.  It was already doing so on the migration branch: it
# reported the re-derived anchor witness as the single NEW stale entry.
#
# PROTON_PIN_PPB moves with it.  It is an OFFSET measured against the muon
# anchor, so re-pinning the anchor changes it too (-11.5371 vs A becomes
# -11.6140 vs C); freezing the offset while the reference moves would drag
# every proton-pinned witness across the PIN_TOL_PPB window.  Deriving it
# from the two resolved pins keeps the pair consistent by construction.
#
# `_q0_value_for_anchor` is the anchor-LABEL resolver in qou_substrate --
# the same function that decides what gets stamped `muon` -- so this audit
# and the stamps it checks now read one source instead of two.
from qou_substrate.witness import _q0_value_for_anchor as _pin


def _resolved(anchor: str) -> mpf:
    v = _pin(anchor)
    if not v:
        raise SystemExit(
            f"q0_value_drift_audit: cannot resolve the {anchor} pin. "
            "Refusing to fall back to a transcribed literal -- a drift audit "
            "measuring against a guess is worse than no drift audit."
        )
    return mpf(v)


Q_CANONICAL = _resolved("muon")
_Q_PROTON = _resolved("proton")
# Offset of the proton-pinned value, in ppb, DERIVED rather than transcribed.
PROTON_PIN_PPB = (_Q_PROTON - Q_CANONICAL) / Q_CANONICAL * mpf(10) ** 9
PIN_TOL_PPB = mpf("0.5")             # how close to a named pin counts as that pin

# Field names that carry a substrate anchor. `q_star` / `qstar` are a
# DIFFERENT parameter (the decay-sector q*) and are deliberately excluded.
Q0_FIELD = re.compile(r"^(q_?0|q_?0_\d+dps|q0Value|q_zero|substrate_q)$", re.I)
EXCLUDE_FIELD = re.compile(r"star|\*|anchor$|err|sigma|unit", re.I)

# A field whose PATH names it as a retired / frozen pin is a deliberate
# record of that pin, not a stale copy of the live one.  The type case is a
# probe that evaluates one quantity "at every registered pin" and stores each
# under a key such as `figures_at_retired` / `figures_at_frozen_A`: re-running
# it reproduces the same retired value, because the retired value is its
# subject.  Such a field is reported in its own class so it stays visible,
# and only when it is still close to canonical (|d| < 100 ppb) -- a labelled
# field far from every anchor is still `unknown`.
RETIRED_LABEL = re.compile(r"retired|frozen", re.I)

# Only values in this neighbourhood are substrate anchors at all.
Q_LO, Q_HI = mpf("1.1"), mpf("1.12")


def _ppb(x: mpf) -> mpf:
    return (x - Q_CANONICAL) / Q_CANONICAL * mpf(10) ** 9


def classify(x: mpf, path: str = "") -> tuple[str, mpf]:
    d = _ppb(x)
    if abs(d) < mpf("1e-6"):
        return "canonical", d
    if abs(d - PROTON_PIN_PPB) < PIN_TOL_PPB:
        return "proton-pin", d
    if abs(d) < mpf("100") and RETIRED_LABEL.search(path):
        return "labelled-retired", d
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
                    cls, d = classify(x, p)
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on stale values NOT already in the baseline")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (only when draining — count must go DOWN)")
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
    for cls in ("canonical", "proton-pin", "labelled-retired", "STALE", "unknown"):
        n = len(by.get(cls, []))
        note = {"proton-pin": "  (documented physical-observations layer — legitimate)",
                "canonical": "  (CAL-2 muon pin — the computations/ convention)",
                "labelled-retired": "  (field path names a retired/frozen pin — deliberate record)"}.get(cls, "")
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
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload_1 = {"note": "Known-stale q0 fields. Regenerate ONLY when draining; "
                     "the count must go DOWN. Not a way to silence a new failure.",
             "count": len(stale),
             "stale_keys": sorted(key(r) for r in stale)}
        _prov_payload_1.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload_1, script_path=__file__, engine=None, q0_anchor=False)
        BASELINE.write_text(json.dumps(
            _prov_payload_1, indent=2) + "\n")
        print(f"\nRebaselined: {len(stale)} stale keys recorded.")

    out = HERE / "q0-value-drift-audit.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload_2 = {
        "schema": "witness/v1",
        "name": "q0-value-drift-audit",
        "description": "Substrate-anchor drift across witness JSONs. proton-pin is "
                       "legitimate (documented layer); STALE matches no documented pin.",
        "data": {"counts": {k: len(v) for k, v in by.items()},
                 "stale_total": len(stale), "new_stale": len(new_stale),
                 "rows": rows},
    }
    _prov_payload_2.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload_2, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(_prov_payload_2, indent=2) + "\n")
    print(f"\nWrote {out.name}")

    return 1 if (args.strict and new_stale) else 0


if __name__ == "__main__":
    sys.exit(main())
