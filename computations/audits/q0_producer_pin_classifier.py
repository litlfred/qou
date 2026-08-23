#!/usr/bin/env python3
"""q0_producer_pin_classifier.py — classify a producer's q₀ pin from its CODE,
so `UNDETERMINED` witnesses can be brought under the anchor audits.

WHY THIS EXISTS
    `q0_declared_vs_recorded_sweep.py` can only check a witness whose producer
    is POSITIVELY declared in `q0_anchor_manifest.json`. As of 2026-08-08 that
    is 309 of 3057 witnesses; **266 carry a pin that nothing can verify**. The
    live 30.4 ppb `qbeta-ck-cache` mislabel survived precisely because its
    producer sat in that gap.

    Extending the manifest is what converts `UNDETERMINED` into a verdict. This
    script proposes entries from static evidence; it does not write them.

🛑 THE MANIFEST IS A CONTROL INPUT, NOT DOCUMENTATION
    `computations/substrate/q_parameter.py` reads `q0_anchor_manifest.json` at
    import time and applies the MUON anchor when the running producer's stem is
    listed under `ideal_muon` (env var `QOU_Q0_ANCHOR` overrides). So:

      * adding a stem to `ideal_muon` FLIPS that producer to the muon pin —
        a live numerical change, not a note about one;
      * adding a stem to `physical_proton` is behaviourally INERT, since
        anything not in `ideal_muon` already resolves to proton.

    Therefore only `physical_proton` entries may be proposed by a sweep.
    An `ideal_muon` entry is a configuration decision and is never auto-proposed
    here. (This corrects the first version of this script, which treated the
    manifest as a passive registry and would have proposed 26 `ideal_muon`
    additions — silently re-pinning 26 producers.)

THE EVIDENCE MODEL
    proton  — the producer resolves to proton TODAY: it reads a q₀ (via
              `q_parameter`, stem-resolved, or `qou_substrate.constants`
              directly) and its stem is not under `ideal_muon`. Note this is
              a statement about the CURRENT manifest, not about intent.
    muon    — imports an explicit muon accessor (`q_muon_at`, `Q_MUON`, …) or
              reads a known muon-built artifact: the `q-pinning-50-digit`
              witness, or the `y-lambda-at-q0` cache (the accessor AGENTS.md
              §q₀-anchor names as the straddle trap), or sets
              `QOU_Q0_ANCHOR` to an ideal/muon value.
    none    — no numeric q₀ reached at all (purely symbolic producer).
    BOTH    — both kinds of evidence in one producer: a straddle CANDIDATE,
              reported loudly and never auto-proposed.

TWO EXCLUSIONS THAT MATTER (learned the hard way, 2026-08-08)
    1. **`if __name__ == "__main__"` blocks are ignored.** `hoefsmit_symbolic`
       imports `from q_parameter import Q as q_num` inside its self-test only;
       counting that would have misclassified a purely SYMBOLIC producer as
       proton-pinned, which is exactly the error that put a spurious `proton`
       stamp on `chi-deuteron-h6.witness.json` (bean `qou-pin1`).
    2. **Only a single unambiguous signal is proposed.** `none` is never
       proposed as `ambiguous` automatically — a producer with no numeric q₀
       may still be one whose pin simply is not expressed in code this analyser
       reads. Proposals are deliberately conservative because the manifest is
       now load-bearing: `witness.py::build()` stamps declared pins, and
       preserve-forward DROPS a recorded pin that a declaration contradicts. A
       wrong entry therefore destroys a correct stamp.

OUTPUT
    A report and a proposal list. Applying it is a separate, reviewed step —
    this script never edits the manifest.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import q0_anchor_is_declared  # noqa: E402

PROTON_MODULES = {"q_parameter", "qou_substrate.constants", "constants"}
PROTON_NAMES = {"Q_50_DIGIT_STR", "q_at", "Q_MP", "Q_PROTON"}
MUON_ARTIFACTS = ("q-pinning-50-digit", "y-lambda-at-q0", "y_lambda_at")
MUON_ENV = ("ideal", "muon", "canonical")
# Explicit muon ACCESSORS. A producer importing one of these is reaching for the
# ideal layer on purpose -- typically a cross-anchor comparison probe -- so its
# muon stamp may be entirely correct. Missing these was a real classifier gap:
# `q_at, q_muon_at` co-imports were being scored proton-only, which would have
# put ~8 deliberately dual-layer probes into a tnjb regeneration batch.
MUON_NAMES = {"q_muon_at", "Q_MUON", "Q_MUON_MP", "q_muon"}


def strip_main_block(tree: ast.Module) -> list[ast.stmt]:
    """Module body with any `if __name__ == "__main__":` block removed."""
    out = []
    for node in tree.body:
        if isinstance(node, ast.If):
            t = node.test
            if (isinstance(t, ast.Compare)
                    and isinstance(t.left, ast.Name) and t.left.id == "__name__"
                    and any(isinstance(c, ast.Constant) and c.value == "__main__"
                            for c in t.comparators)):
                continue
        out.append(node)
    return out


def classify(path: Path) -> tuple[str, list[str]]:
    try:
        src = path.read_text(encoding="utf-8")
        tree = ast.parse(src)
    except Exception as exc:  # noqa: BLE001
        return "unreadable", [repr(exc)[:60]]

    body = strip_main_block(tree)
    proton: list[str] = []
    muon: list[str] = []

    class V(ast.NodeVisitor):
        def visit_ImportFrom(self, n):  # noqa: N802
            mod = n.module or ""
            if mod in PROTON_MODULES or mod.endswith(".constants"):
                names = [a.name for a in n.names]
                if any(x in MUON_NAMES for x in names):
                    muon.append(f"imports {[x for x in names if x in MUON_NAMES]}")
                if any(x == "Q" or x in PROTON_NAMES for x in names):
                    proton.append(f"from {mod} import {', '.join(names)}")
            self.generic_visit(n)

        def visit_Import(self, n):  # noqa: N802
            for a in n.names:
                if a.name in PROTON_MODULES:
                    proton.append(f"import {a.name}")
            self.generic_visit(n)

        def visit_Attribute(self, n):  # noqa: N802
            if n.attr in PROTON_NAMES:
                proton.append(f".{n.attr}")
            if n.attr in MUON_NAMES:
                muon.append(f".{n.attr}")
            self.generic_visit(n)

        def visit_Constant(self, n):  # noqa: N802
            if isinstance(n.value, str):
                s = n.value
                for art in MUON_ARTIFACTS:
                    if art in s:
                        muon.append(f'"{s[:48]}"')
                if s.strip().lower() in MUON_ENV and "ANCHOR" in src:
                    muon.append(f'env-like "{s}"')
                if s.startswith("1.10997859555"):
                    muon.append("hardcoded muon 50-digit")
            self.generic_visit(n)

    V().visit(ast.Module(body=body, type_ignores=[]))

    # de-dup, keep order
    proton = list(dict.fromkeys(proton))
    muon = list(dict.fromkeys(muon))
    if proton and muon:
        return "BOTH", [f"proton: {proton[:2]}", f"muon: {muon[:2]}"]
    if proton:
        return "proton", proton[:3]
    if muon:
        return "muon", muon[:3]
    return "none", []


def find_producer(script_name: str) -> Path | None:
    # `_deprecated/` holds 890 retired copies; 37 share a name with a live
    # file. The tie-break below sorts by (computations-first, fewest parts),
    # which TIES when the live copy is as deeply nested as the retired one --
    # `computations/probes/x.py` and `computations/_deprecated/x.py` are both
    # 3 parts. Measured: 3 of the 7 colliding `.py` names resolved to the
    # DEPRECATED copy (path_b_habiro_mass_probe, rho_k_markov_multiplicativity_probe,
    # term5_aK_audit). A retired copy is by definition not the producer.
    hits = [p for p in REPO.rglob(script_name)
            if ".git" not in p.parts and "_deprecated" not in p.parts
            and ".claude" not in p.parts and p.is_file()]
    if not hits:
        return None
    # prefer the computations/ copy over vendored duplicates
    hits.sort(key=lambda p: (0 if "computations" in p.parts else 1, len(p.parts)))
    return hits[0]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", type=int, default=20)
    ap.add_argument("--emit-proposal", type=str, default=None,
                    help="write the proposed manifest additions to this path")
    args = ap.parse_args(argv)

    witnesses = [w for w in REPO.rglob("*.witness.json") if ".git" not in w.parts]

    # producers of witnesses that carry a pin but are not yet declared
    undeclared: dict[str, list[str]] = defaultdict(list)
    for w in witnesses:
        try:
            b = json.loads(w.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(b, dict) or b.get("q0Anchor") not in ("muon", "proton"):
            continue
        script = b.get("scriptFile") or b.get("script")
        if not script:
            continue
        if q0_anchor_is_declared(Path(str(script))):
            continue
        undeclared[str(script)].append(
            f"{w.relative_to(REPO)}::{b['q0Anchor']}")

    print("=" * 72)
    print("q₀ producer pin classifier — proposals for the UNDETERMINED gap")
    print("=" * 72)
    print(f"  undeclared producers carrying pinned witnesses : {len(undeclared)}")

    counts: Counter = Counter()
    rows = []
    for script, wits in sorted(undeclared.items()):
        p = find_producer(Path(script).name)
        if p is None:
            counts["missing-producer"] += 1
            rows.append((script, "missing-producer", [], wits))
            continue
        verdict, ev = classify(p)
        recorded = {w.split("::")[1] for w in wits}
        agree = (len(recorded) == 1 and verdict in recorded)
        counts[verdict] += 1
        rows.append((script, verdict, ev, wits))
        if verdict in ("proton", "muon"):
            counts[f"{verdict}-{'agrees' if agree else 'DISAGREES'}"] += 1

    for k in ("proton", "muon", "none", "BOTH", "missing-producer", "unreadable"):
        if counts[k]:
            print(f"  {k:18s} : {counts[k]}")
    print(f"\n  of the code-classified: "
          f"proton agrees={counts['proton-agrees']} disagrees={counts['proton-DISAGREES']}, "
          f"muon agrees={counts['muon-agrees']} disagrees={counts['muon-DISAGREES']}")

    both = [r for r in rows if r[1] == "BOTH"]
    if both:
        print(f"\n  🛑 BOTH — straddle candidates ({len(both)}), never auto-proposed:")
        for script, _v, ev, wits in both[:args.show]:
            print(f"    {script}\n        {ev}\n        witnesses: {wits[:2]}")

    dis = [r for r in rows if r[1] in ("proton", "muon")
           and not ({w.split('::')[1] for w in r[3]} == {r[1]})]
    if dis:
        print(f"\n  ⚠ code says one pin, witness records the other ({len(dis)}):")
        for script, v, ev, wits in dis[:args.show]:
            print(f"    {script}: code={v}  witness={sorted({w.split('::')[1] for w in wits})}")
            print(f"        {ev[:2]}")

    # Proposal: ONLY the behaviourally-inert direction (physical_proton), and
    # only where the code evidence and the recorded pin already agree.
    # `ideal_muon` is deliberately never proposed — see the docstring: adding a
    # stem there re-pins the producer.
    proposal = {"physical_proton": []}
    for script, v, _ev, wits in rows:
        if v != "proton":
            continue
        recorded = {w.split("::")[1] for w in wits}
        if recorded != {v}:
            continue
        stem = Path(script).stem
        if stem not in proposal["physical_proton"]:
            proposal["physical_proton"].append(stem)
    for k in proposal:
        proposal[k].sort()
    n = sum(len(v) for v in proposal.values())
    print(f"\n  PROPOSED additions — physical_proton ONLY (behaviourally inert): {n}")
    print(f"    physical_proton: {len(proposal['physical_proton'])}")
    print("    ideal_muon     : 0 by construction — adding one RE-PINS the")
    print("                     producer, so it is a decision, not a sweep.")

    if args.emit_proposal:
        Path(args.emit_proposal).write_text(json.dumps(proposal, indent=2) + "\n")
        print(f"\n  proposal -> {args.emit_proposal}")

    print("\n" + "=" * 72)
    print("This script never edits the manifest. Applying the proposal is a")
    print("separate reviewed step — a wrong entry now DESTROYS a correct stamp,")
    print("since preserve-forward drops pins a declaration contradicts.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
