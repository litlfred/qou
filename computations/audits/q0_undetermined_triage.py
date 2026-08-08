#!/usr/bin/env python3
"""q0_undetermined_triage.py — decide, per producer, whether its UNDETERMINED
witness pin can be brought under the anchor audits by a manifest declaration.

THE GAP
    `q0_declared_vs_recorded_sweep.py` can only check a witness whose producer
    is POSITIVELY declared in `q0_anchor_manifest.json`. Everything else records
    a pin that nothing verifies. Owner decision 2026-08-08: declare where the
    code evidence is unambiguous.

    "Unambiguous" has to be earned per producer, because the manifest is a
    CONTROL INPUT, not a registry:

      * adding to `physical_proton` is behaviourally INERT — anything not under
        `ideal_muon` already resolves proton;
      * adding to `ideal_muon` RE-PINS the producer, a live numerical change;
      * and a declaration that CONTRADICTS a recorded pin destroys it, because
        `WitnessBuilder.save()`'s preserve-forward drops a pin the declaration
        disagrees with.

    So a wrong entry is not a wrong note. It silently changes numbers or erases
    a correct label.

THE CATEGORIES

    A  SAFE-PROTON     witness says proton, code resolves proton, no muon
                       evidence. Declaring `physical_proton` is inert and turns
                       UNDETERMINED into checkable. Pure win.

    B  TWO-LAYER       imports `q_muon_at`/`Q_MUON` alongside a proton accessor
                       — a deliberate cross-anchor comparison, which the owner
                       ruled legitimate on 2026-08-08. The manifest has one
                       field per producer and these genuinely use two layers, so
                       there is nothing honest to declare. LEAVE UNDECLARED, and
                       say so, rather than forcing a half-true label.

    C  MUON-ONLY       witness says muon, the only q₀ evidence is muon (a
                       hardcoded literal or a read of the muon witness), and the
                       producer takes NOTHING from `q_parameter`. Declaring
                       `ideal_muon` matches the witness and is inert **because
                       there is no `q_parameter` read to re-pin**. That last
                       clause is the whole safety argument and is checked, not
                       assumed.

    D  CONTRADICTION   code and witness disagree. Needs a per-producer decision
                       with evidence; never swept.

Read-only. Proposes; never edits the manifest.

Usage:
    python3 q0_undetermined_triage.py
    python3 q0_undetermined_triage.py --emit-proposal /tmp/proposal.json
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent
MANIFEST = COMPUTE_DIR / "q0_anchor_manifest.json"

MUON_NAMES = {"q_muon_at", "Q_MUON", "Q_MUON_MP", "q_muon"}
MUON_LITERAL = ("1.10997859555", "1.1099785955")
MUON_ARTIFACTS = ("q-pinning-50-digit", "y-lambda-at-q0")
Q0_MODULES = {"q_parameter", "qou_substrate"}

# Producers held out by an explicit decision, not by a rule. Declaring one of
# these would convert an UNDETERMINED pin into a DECL_MISMATCH, which is WORSE:
# the declaration only pays off once the witness is regenerated to match, and
# neither of these can be regenerated cleanly today.
HOLD_OUT = {
    # Two assertions fail on regeneration -- `structural_constants_match_probe1`
    # (0.0 -> 7.33e-07, tol 1e-09) and `m3_residuals_match_hpower_witness`
    # (5.8e-15 -> 2.9e-06, tol 1e-09), both cross-WITNESS comparisons. Proven
    # pre-existing: running the producer from a worktree at the pre-2026-08-08
    # base commit d8d22890 yields BIT-IDENTICAL failing values, so the committed
    # witness is simply stale and none of this is the anchor work. Bean qou-pin6.
    "probe_9b_gate_interface_algebra",
    # Regeneration drops the ENTIRE provenance block (commitSha, computedAt,
    # scriptFile, scriptHash, q0Anchor, q0Value...). The producer writes its own
    # `_provenance` with a raw json.dump and never calls `WitnessBuilder.save()`,
    # so those top-level keys were BACKFILLED by a sweep, not produced -- and the
    # first regeneration after a backfill drops them. Textbook qou-pin5. Its
    # committed q0Value is also the MUON literal, i.e. that witness was generated
    # through the cross-layer fallback removed on 2026-08-08. Fix the producer to
    # stamp its own pin first (qou-pin5), then declare.
    "zhabiro_phiq_production_crosscheck",
}


def _manifest() -> tuple[set[str], set[str]]:
    d = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return set(d.get("ideal_muon", [])), set(d.get("physical_proton", []))


def _producer(stem: str) -> Path | None:
    for p in COMPUTE_DIR.rglob(f"{stem}.py"):
        if "_deprecated" not in p.parts:
            return p
    return None


def _local_module(name: str) -> Path | None:
    """Resolve a bare-name import to a file in the computations tree."""
    for c in (COMPUTE_DIR / f"{name}.py", COMPUTE_DIR / "substrate" / f"{name}.py"):
        if c.exists():
            return c
    hits = [p for p in COMPUTE_DIR.rglob(f"{name}.py") if "_deprecated" not in p.parts]
    return hits[0] if len(hits) == 1 else None


def reaches_q0_transitively(path: Path, depth: int = 2) -> tuple[bool, str]:
    """Does this producer reach a q₀ through a LOCAL import chain?

    A file-local scan under-detects: `q0_producer_pin_classifier`'s `none`
    verdict means "no q₀ **in this file**", not "no q₀" (bean qou-pin4).

    But the converse mistake is just as bad, and qou-pin4 recorded it: 2 of 3
    flagged "transitive straddles" were FALSE because they imported
    `flavor_split_leading`/`subleading` — pure functions carrying no q₀ at all.
    So the test here is "imports a q₀-BEARING NAME from a module that itself
    reads q₀", not "imports a module that reads q₀".
    """
    seen: set[Path] = set()

    def walk(p: Path, d: int, trail: tuple[str, ...]) -> tuple[bool, str]:
        if d < 0 or p in seen:
            return False, ""
        seen.add(p)
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            return False, ""
        for n in ast.walk(tree):
            if not isinstance(n, ast.ImportFrom) or not n.module:
                continue
            root = n.module.split(".")[0]
            names = {a.name for a in n.names}
            if root in Q0_MODULES:
                bearing = {x for x in names
                           if x.startswith("Q") or x.startswith("q_")
                           or x in ("HA", "HBAR_Q", "TWO_Q", "LN_Q")} - MUON_NAMES
                if bearing:
                    return True, " -> ".join(trail + (p.stem, sorted(bearing)[0]))
            sub = _local_module(root)
            if sub is not None:
                # Only follow when a q₀-bearing name is actually taken from it.
                bearing = {x for x in names
                           if x.startswith("Q") or x.startswith("q_")
                           or x.lower().startswith("q0")}
                if bearing or root.startswith("q"):
                    ok, why = walk(sub, d - 1, trail + (p.stem,))
                    if ok:
                        return True, why
        return False, ""

    return walk(path, depth, ())


def evidence(path: Path) -> dict:
    """What q₀ sources does this file reach, and how."""
    src = path.read_text(encoding="utf-8", errors="replace")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"parse_error": True}

    imports_muon_accessor = False
    reads_q_parameter = False
    q_param_names: list[str] = []
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and n.module:
            root = n.module.split(".")[0]
            names = {a.name for a in n.names}
            if names & MUON_NAMES:
                imports_muon_accessor = True
            if root in Q0_MODULES:
                # Only a q₀-BEARING name counts. Importing a pure helper from
                # the same module is not a q₀ read — the lesson from qou-pin4,
                # where 2 of 3 "transitive straddles" were exactly this mistake.
                bearing = {x for x in names
                           if x.startswith("Q") or x.startswith("q_")
                           or x in ("HA", "HBAR_Q", "TWO_Q", "LN_Q")}
                bearing -= MUON_NAMES
                if bearing:
                    reads_q_parameter = True
                    q_param_names += sorted(bearing)
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.name.split(".")[0] in Q0_MODULES:
                    reads_q_parameter = True
                    q_param_names.append(a.name)

    has_muon_literal = any(m in src for m in MUON_LITERAL)
    reads_muon_artifact = any(m in src for m in MUON_ARTIFACTS)

    # A file-local scan under-detects (qou-pin4): follow local imports for a
    # q₀-BEARING name when the file itself shows none.
    transitive, via = (False, "")
    if not reads_q_parameter:
        transitive, via = reaches_q0_transitively(path)
    return {
        "transitive_q0": transitive,
        "transitive_via": via,
        "parse_error": False,
        "muon_accessor": imports_muon_accessor,
        "q_parameter": reads_q_parameter,
        "q_parameter_names": sorted(set(q_param_names))[:4],
        "muon_literal": has_muon_literal,
        "muon_artifact": reads_muon_artifact,
    }


def undetermined() -> list[tuple[str, str, str]]:
    muon, proton = _manifest()
    declared = muon | proton
    out = []
    for w in sorted(REPO.rglob("*.witness.json")):
        if ".git" in w.parts or "_deprecated" in w.parts:
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(d, dict):
            continue
        prov = d.get("provenance") if isinstance(d.get("provenance"), dict) else {}
        pin = prov.get("q0Anchor") or d.get("q0Anchor")
        if pin not in ("muon", "proton"):
            continue        # 'ambiguous' pins are a separate question
        sf = prov.get("scriptFile") or d.get("scriptFile") or ""
        stem = Path(str(sf)).stem
        if stem and stem not in declared:
            out.append((stem, pin, str(w.relative_to(REPO))))
    return out


def categorize(stem: str, pin: str, ev: dict) -> tuple[str, str]:
    if ev.get("parse_error"):
        return "D-CONTRADICTION", "producer does not parse"
    muon_ev = ev["muon_accessor"] or ev["muon_literal"] or ev["muon_artifact"]

    if ev["muon_accessor"] and ev["q_parameter"]:
        return ("B-TWO-LAYER",
                "imports an explicit muon accessor alongside a proton one — "
                "a deliberate cross-anchor comparison (owner ruling)")

    reaches_proton = ev["q_parameter"] or ev.get("transitive_q0")

    if pin == "proton":
        if not muon_ev and reaches_proton:
            return ("A-SAFE-PROTON",
                    "resolves proton via "
                    + (", ".join(ev["q_parameter_names"]) if ev["q_parameter"]
                       else f"transitive {ev.get('transitive_via') or 'import'}")
                    + "; no muon evidence")
        if muon_ev:
            return ("D-CONTRADICTION",
                    "witness says proton but the code carries muon evidence")
        return ("F-PIN-MAY-BE-SPURIOUS",
                "records proton but NO q0 source found at any depth -- the "
                "qou-pin1 shape (a pin on a symbolic artifact)")

    # pin == "muon"
    if muon_ev and not reaches_proton:
        return ("C-MUON-ONLY",
                "muon evidence only, and nothing read from q_parameter, so "
                "declaring ideal_muon re-pins nothing")
    if muon_ev and reaches_proton:
        return ("D-CONTRADICTION",
                "witness says muon but the code also reads "
                + (", ".join(ev["q_parameter_names"]) if ev["q_parameter"]
                   else f"transitive {ev.get('transitive_via') or 'q_parameter'}")
                + " (an ideal_muon entry would re-pin it)")
    if reaches_proton:
        return ("E-STALE-MUON-STAMP",
                "witness records muon but the code resolves PROTON via "
                + (", ".join(ev["q_parameter_names"]) if ev["q_parameter"]
                   else f"transitive {ev.get('transitive_via') or 'import'}")
                + " -- the witness is unreproducible (tnjb class)")
    return ("F-PIN-MAY-BE-SPURIOUS",
            "records muon but NO q0 source found at any depth -- the qou-pin1 "
            "shape (a pin on a symbolic artifact)")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--emit-proposal", default="")
    args = ap.parse_args(argv)

    rows = undetermined()
    buckets: dict[str, list[tuple[str, str, str]]] = {}
    for stem, pin, wit in rows:
        p = _producer(stem)
        if p is None:
            buckets.setdefault("D-CONTRADICTION", []).append(
                (stem, pin, "no producer file found"))
            continue
        cat, why = categorize(stem, pin, evidence(p))
        buckets.setdefault(cat, []).append((stem, pin, why))

    print("=" * 72)
    print("UNDETERMINED q₀ pins — triage")
    print("=" * 72)
    print(f"  witnesses with an unverifiable muon/proton pin : {len(rows)}")
    for h in sorted(HOLD_OUT):
        print(f"  HELD OUT: {h}")
    for cat in ("A-SAFE-PROTON", "E-STALE-MUON-STAMP", "C-MUON-ONLY",
                "B-TWO-LAYER", "F-PIN-MAY-BE-SPURIOUS", "D-CONTRADICTION"):
        items = buckets.get(cat, [])
        print(f"\n  {cat}  ({len(items)})")
        for stem, pin, why in sorted(items):
            print(f"      {stem:<46} pin={pin:<7} {why}")

    prop_proton = sorted(({s for s, _, _ in buckets.get("A-SAFE-PROTON", [])}
                          | {s for s, _, _ in buckets.get("E-STALE-MUON-STAMP", [])})
                         - HOLD_OUT)
    needs_regen = sorted({s for s, _, _ in buckets.get("E-STALE-MUON-STAMP", [])}
                         - HOLD_OUT)
    prop_muon = sorted({s for s, _, _ in buckets.get("C-MUON-ONLY", [])})
    print("\n" + "-" * 72)
    print(f"  proposed physical_proton (inert)     : {len(prop_proton)}")
    print(f"    of which ALSO need regeneration    : {len(needs_regen)}")
    print("      (their witness records muon that the code cannot reproduce;")
    print("       declaring alone leaves a DECL_MISMATCH -- regenerate too)")
    print(f"  proposed ideal_muon (re-pins — VERIFY): {len(prop_muon)}")
    print("  B-TWO-LAYER stays undeclared BY DESIGN: the manifest has one field")
    print("  per producer and these honestly use two layers.")
    if args.emit_proposal:
        Path(args.emit_proposal).write_text(json.dumps(
            {"physical_proton": prop_proton, "ideal_muon": prop_muon,
             "needs_regeneration": needs_regen}, indent=2))
        print(f"\n  proposal written: {args.emit_proposal}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
