#!/usr/bin/env python3
# polynomial_q_not_applicable: validator, not a q-series compute.
"""Detect LAYER STRADDLES empirically: run a producer at both q0 anchors and see
whether anything but the stamp moves.

THE RULE (AGENTS.md §"q0 anchor convention"): never mix an ideal-layer input
with an experimental-layer one inside a single computed quantity. The measured
cost of one instance is 11.54 ppb -- the mu-p tension itself.

WHY EMPIRICAL. Static analysis is per-file and the interesting straddles are
NOT. The worked case: `xi_ell_phi_q_probe` derives q0 inline from the muon
ratio and never names the manifest, yet its output moves 1.13e-7 when a stem is
added to `q0_anchor_manifest.json`. The manifest value arrives three modules
down, through a DEFAULTED PARAMETER:

    xi_ell_phi_q_probe
      |- q0 derived INLINE from M_MU_OVER_M_E              -> muon, always
      `- per_generator_V_hat_general:94
             _cached_seminormal(shape)      <-- no q passed
               `- mass_at_3A_proper:64  from q_parameter import Q as Q0
                                                           -> MANIFEST-RESOLVED

Nothing at the call site mentions an anchor, so no grep finds it. A per-file
scan of the same 16 files reports ONE candidate and misses this one entirely.

THE TEST. Run the producer twice, `QOU_Q0_ANCHOR=physical` then `=ideal`, and
diff its witnesses with ephemeral fields and the q0 stamp masked.

  * a producer whose ONLY q is the manifest one SHOULD move -- it is following
    the anchor, which is correct. Such a producer is not in scope here.
  * a producer with its OWN q that ALSO moves is mixing two sources. That is
    the straddle, and it is what this audit reports.

So scope matters: pass only producers that derive or hardcode a q of their own.
`--candidates` uses the inline-derivation set (imports `M_MU_OVER_M_E` and
computes `1/(1 - sqrt(...))`); `qou-5le1` Mode A.

MEASURED 2026-08-23 over those 9: **3 straddle** -- t6_tau_h5_embedding_probe
(15 fields), xi_ell_phi_q_probe (36), per_generator_V_hat_general (24, and it
is the module that carries the defect into the other two). 5 clean. 1 could not
be run (lepton_tower_probe_1_cinquefoil_muon) and is therefore UNTESTED, not
clean.

Usage:
    python3 anchor_flip_straddle_audit.py --candidates
    python3 anchor_flip_straddle_audit.py path/to/producer.py [...]
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
EPHEMERAL = {"computedAt", "commitSha", "durationMs", "environment", "invocation",
             "scriptHash", "scriptCommitSha", "engineVersion", "timestamp",
             "elapsed_seconds", "measured_at", "generated"}
STAMP_KEYS = ("q0Anchor", "q0Value")
INLINE_Q0 = re.compile(r"1\s*\)?\s*/\s*\(\s*(mp\.)?mpf?\(?1\)?\s*-\s*", re.I)
SKIP = (".git", ".claude", "_deprecated", "node_modules", "__pycache__")


def _flat(o, prefix="", out=None):
    out = {} if out is None else out
    if isinstance(o, dict):
        for k, v in o.items():
            _flat(v, f"{prefix}/{k}", out)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _flat(v, f"{prefix}/{i}", out)
    else:
        out[prefix] = o
    return out


def candidates() -> list[Path]:
    """Producers with a q of their own: the inline-derivation set."""
    out = []
    for p in sorted(REPO.rglob("*.py")):
        if any(x in p.parts for x in SKIP):
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        if "M_MU_OVER_M_E" in src and INLINE_Q0.search(src):
            out.append(p)
    return out


def _run(prod: Path, anchor: str) -> int:
    env = dict(os.environ)
    env["QOU_Q0_ANCHOR"] = anchor
    r = subprocess.run([sys.executable, "-u", prod.name], cwd=prod.parent,
                       capture_output=True, timeout=900, env=env)
    return r.returncode


def audit(prod: Path):
    """(verdict, detail). Restores every witness it touches."""
    saved = {f: f.read_bytes() for f in prod.parent.glob("*.witness.json")}

    def restore():
        for f, b in saved.items():
            f.write_bytes(b)

    try:
        if _run(prod, "physical") != 0:
            return "RUN-FAIL", "could not execute — UNTESTED, not clean"
        phys = {f: json.loads(f.read_text())
                for f in prod.parent.glob("*.witness.json")
                if f.read_bytes() != saved.get(f)}
        if not phys:
            return "NO-WITNESS", "library, or writes nothing"
        _run(prod, "ideal")
        for f, doc_p in phys.items():
            fa, fb = _flat(doc_p), _flat(json.loads(f.read_text()))
            moved = [k for k in sorted(set(fa) | set(fb))
                     if not any(e in k.split("/") for e in EPHEMERAL)
                     and not any(s in k for s in STAMP_KEYS)
                     and fa.get(k) != fb.get(k)]
            if moved:
                return "STRADDLE", f"{len(moved)} field(s) move, e.g. {moved[0]} [{f.name}]"
        return "clean", "anchor flip moves nothing but the stamp"
    finally:
        restore()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("producers", nargs="*")
    ap.add_argument("--candidates", action="store_true",
                    help="audit every inline-q0-derivation producer")
    args = ap.parse_args(argv)

    targets = ([Path(p) for p in args.producers] if args.producers
               else candidates() if args.candidates else [])
    if not targets:
        ap.error("give producer paths or --candidates")

    print("=" * 72)
    print("anchor-flip straddle audit — producers with a q of their own")
    print("=" * 72)
    counts = {}
    for t in targets:
        verdict, detail = audit(t if t.is_absolute() else REPO / t)
        counts[verdict] = counts.get(verdict, 0) + 1
        print(f"  {verdict:11s} {t.stem}: {detail}")
    print("\n  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("=" * 72)
    return 1 if counts.get("STRADDLE") else 0


if __name__ == "__main__":
    raise SystemExit(main())
