#!/usr/bin/env python3
"""Move migrated stems to `physical_proton` -- AFTER their data moved, not before.

## The ordering is the whole point

`q0_anchor_manifest.json` does not merely *describe* which anchor a producer
uses; `substrate/q_parameter.py` *selects* the anchor by membership in
`ideal_muon`. So the manifest edit is the switch, and it can be made in either
order relative to regenerating the witnesses:

  * manifest first -> every listed producer silently changes anchor while its
    committed witness still holds muon numbers, and the anti-corruption guard
    ("Refusing to fall back to proton silently") stops being reachable for
    exactly the producers it protects. This is the shortcut proposed in #5049
    and held back in #5315; see AGENTS.md "Do NOT do it by emptying
    ideal_muon".
  * data first (this tool) -> the declaration stays truthful throughout, and
    only flips once the witness on disk already carries the proton q0.

The sweep runs producers under an explicit `QOU_Q0_ANCHOR=proton`, which
overrides the manifest, so the data can move while the manifest still says
muon. This finalizes that.

## What it refuses to move

  * ANCHOR-DEFINING producers. `q_pinning_50_digit` emits the witness that
    DEFINES the muon anchor (`witness._q0_value_for_anchor("muon")` reads its
    `derived_50_digit.q`). Re-pinning it does not migrate a consumer, it
    destroys the layer -- that is what took main red on 2026-08-19.
  * KEEP-ON-MUON producers: those that need the muon pin by design and refuse
    a proton run. Measured, not assumed -- the list is derived from producers
    whose proton leg failed in the sweep journal. Two confirmed so far:
    `atomic_tr_m_mpfr_50dps` (dual-layer, emits one witness per layer) and
    `cross_check_trM_1ppb` ("L1 cross-check must run under the MUON q0 pin").
  * Producers whose witness does NOT yet carry the proton q0 -- i.e. anything
    the sweep did not actually migrate, including the ones that time out or
    are broken on main (qou-2zjp). Relabelling those is the exact
    declaration-vs-data decoupling this ordering exists to avoid.

`ideal_muon` therefore does NOT end at zero, and a run that drove it to zero
would be a bug, not a completed migration.

Usage:
    python3 q0_manifest_finalize.py            # report only
    python3 q0_manifest_finalize.py --apply
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "q0_anchor_manifest.json"
JOURNAL = HERE / "q0-migration-decompose-progress.json"
MU_PREFIX = "1.109978595557"
PR_PREFIX = "1.109978582751"

ANCHOR_DEFINING = frozenset({"q_pinning_50_digit"})


def witness_state() -> dict[str, tuple[bool, bool]]:
    """stem -> (any witness still carries muon q0, any carries proton q0)."""
    out: dict[str, tuple[bool, bool]] = {}
    for p in HERE.rglob("*.witness.json"):
        if "_deprecated" in p.parts:
            continue
        try:
            t = p.read_text(encoding="utf-8")
            d = json.loads(t)
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(d, dict):
            continue
        sf = d.get("scriptFile") or ""
        stem = sf[:-3] if isinstance(sf, str) and sf.endswith(".py") else sf
        if not stem:
            continue
        m, pr = out.get(stem, (False, False))
        out[stem] = (m or (MU_PREFIX in t), pr or (PR_PREFIX in t))
    return out


def keep_on_muon() -> set[str]:
    """Producers that REFUSED a proton run -- measured from the sweep journal."""
    if not JOURNAL.exists():
        return set()
    try:
        done = json.loads(JOURNAL.read_text()).get("done", {})
    except Exception:  # noqa: BLE001
        return set()
    # rc_muon == 0 but rc_proton != 0: it runs fine at muon and declines proton.
    # A producer failing BOTH legs is broken (qou-2zjp), not keep-on-muon.
    return {s for s, v in done.items()
            if v.get("rc_muon") == 0 and v.get("rc_proton") not in (0, None)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ideal = list(man.get("ideal_muon", []))
    proton = list(man.get("physical_proton", []))
    state = witness_state()
    keep = keep_on_muon() | ANCHOR_DEFINING

    move, hold = [], {}
    for s in ideal:
        if s in keep:
            hold[s] = ("anchor-defining" if s in ANCHOR_DEFINING
                       else "keep-on-muon (refused its proton leg)")
            continue
        m, pr = state.get(s, (False, False))
        if pr and not m:
            move.append(s)
        elif pr and m:
            hold[s] = "emits BOTH pins — needs review, not a blind move"
        else:
            hold[s] = "witness still muon — not migrated yet"

    print(f"manifest: ideal_muon={len(ideal)} physical_proton={len(proton)}")
    print(f"  move to physical_proton : {len(move)}")
    print(f"  hold in ideal_muon      : {len(hold)}")
    for s, why in sorted(hold.items()):
        print(f"      {s:<52s} {why}")

    if not a.apply:
        print("\n(report only; pass --apply to write)")
        return 0

    man["ideal_muon"] = sorted(set(ideal) - set(move))
    man["physical_proton"] = sorted(set(proton) | set(move))
    MANIFEST.write_text(json.dumps(man, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    print(f"\nwrote {MANIFEST.name}: ideal_muon={len(man['ideal_muon'])} "
          f"physical_proton={len(man['physical_proton'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
