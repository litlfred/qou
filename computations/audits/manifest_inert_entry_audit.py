"""Manifest entries that cannot steer anything — and three detector shapes that DON'T work.

Bean `qou-cds3` names a class and leaves it unfiled:

    "a manifest entry is SILENTLY INERT for any producer whose WitnessBuilder
     is constructed without a script path ... a manifest entry for it is a
     false record. Not filed as its own bean yet."

I tried to build that detector. **The general form does not survive
measurement**, for a reason worth recording: there are TWO steering mechanisms
keyed on TWO DIFFERENT stems, and the bean's framing describes only one.

    q_parameter.py:107        _stem = Path(sys.argv[0]).stem      ENTRY POINT
    qou_substrate/witness.py  stem  = Path(_script_path).stem     CALLER FRAME
      (_script_path defaults to inspect.stack()[1].filename)

A producer run as `python3 foo.py` is steered correctly by `q_parameter`
whatever its WitnessBuilder does, because `sys.argv[0]` is the producer. So
"constructs no WitnessBuilder" does NOT imply "manifest entry is inert".

## Three shapes measured, all of which over-flag — do not rebuild these

1. **"listed but never constructs a WitnessBuilder"** -> reported **176**.
   Wrong: it models only the `_script_path` route. `torus_knot_markov_trace_
   closed_form` builds a plain dict and writes it with `json.dumps`, never
   touching WitnessBuilder — and is steered anyway, via `q_parameter`'s
   `sys.argv[0]` lookup at import.

2. **"a scriptFile stamped on many witnesses is a helper stamping foreign
   witnesses"** -> 37 shared basenames, and the two largest are legitimate.
   `canonical_isotope_witness.py` (120) and `_habiro_coefficient_extract.py`
   (26) are BOTH entry points, BOTH manifest-listed, and each emits its own
   named family (`habiro-coefficients-*`). One producer, many witnesses is the
   normal case here, not a defect. The leading underscore is not evidence.

3. **"scriptFile names a module with no `__main__`"** -> reported **90**.
   Wrong: those are producers that simply run at top level without a
   `__main__` guard, and each names its own witness
   (`meson-mass-from-hecke.witness.json` <- `meson_mass_from_hecke.py`).

The residual real cases exist — the bean records `habiro_interpolation_wlambda`
stamping `muon` through two re-runs while the manifest said `ambiguous` — but
they are found by RUNNING the producer and watching it ignore the manifest,
which is how that one was found. No static shape tried here separates them.

## What this audit does report: entries that cannot bind to anything

Narrow, exact, and checkable without running anything: a manifest entry whose
stem resolves ONLY to `fsh-guts/deprecated/computations/`. Such an entry asserts an
anchor class for a producer that has been retired, so it can never steer a run.
Unlike the three shapes above this has no false-positive mechanism — either the
live tree has the file or it does not.

Run:  python3 -u computations/audits/manifest_inert_entry_audit.py
"""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"
MANIFEST = COMP / "q0_anchor_manifest.json"
CLASSES = ("ideal_muon", "physical_proton", "ambiguous")


def main() -> int:
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    listed = {s: c for c in CLASSES for s in man.get(c, [])}
    print(f"manifest entries: {len(listed)} (" +
          ", ".join(f"{c}={len(man.get(c, []))}" for c in CLASSES) + ")")

    live = {p.stem for p in COMP.rglob("*.py") if ("_deprecated" not in p.parts and "fsh-guts" not in p.parts)}
    dead = {p.stem: str(p.relative_to(REPO))
            for p in COMP.rglob("*.py") if ("_deprecated" in p.parts or "fsh-guts" in p.parts)}

    deprecated_only = []
    missing_entirely = []
    for stem, cls in sorted(listed.items()):
        if stem in live:
            continue
        if stem in dead:
            deprecated_only.append({"stem": stem, "class": cls,
                                    "source": dead[stem]})
        else:
            missing_entirely.append({"stem": stem, "class": cls})

    # do committed witnesses still carry these names?
    still_named: dict[str, list[str]] = {}
    targets = {r["stem"] for r in deprecated_only} | {
        r["stem"] for r in missing_entirely}
    if targets:
        for w in COMP.rglob("*.witness.json"):
            try:
                d = json.loads(w.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            sf = (d.get("witness") or {}).get("scriptFile") or d.get("scriptFile")
            if isinstance(sf, str) and Path(sf).stem in targets:
                still_named.setdefault(Path(sf).stem, []).append(w.name)

    print(f"\n  entries whose producer is DEPRECATED-only : {len(deprecated_only)}")
    for r in deprecated_only:
        wn = still_named.get(r["stem"], [])
        print(f"    - {r['stem']}  [{r['class']}]  {r['source']}")
        for n in wn:
            print(f"        witness still names it: {n}")
    print(f"  entries with NO source anywhere          : {len(missing_entirely)}")
    for r in missing_entirely:
        print(f"    - {r['stem']}  [{r['class']}]")

    out = {
        "manifest_entries": len(listed),
        "deprecated_only": deprecated_only,
        "missing_entirely": missing_entirely,
        "witnesses_still_naming_them": still_named,
        "detector_shapes_that_overflag": {
            "no_WitnessBuilder_construction": 176,
            "shared_scriptFile_basename": 37,
            "scriptFile_module_without_main": 90,
        },
        "note": ("The general 'inert manifest entry' detector does not survive "
                 "measurement: q_parameter steers via sys.argv[0] (the entry "
                 "point) while WitnessBuilder stamps via inspect.stack()[1] "
                 "(the caller frame). Only the deprecated/missing classes are "
                 "decidable statically."),
    }
    dest = COMP / "audits" / "manifest-inert-entry-audit.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")
    print(f"\nrecord: {dest.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
