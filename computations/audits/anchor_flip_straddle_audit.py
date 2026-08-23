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
import random
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
MUON_LITERAL = re.compile(r"1\.10997859555")
WRITES_WITNESS = ("write_text", "WitnessBuilder", "json.dump")
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


def candidates(kind: str = "inline") -> list[Path]:
    """Producers with a q of their own.

    ``inline``  -- derives q0 from the muon ratio (qou-5le1 Mode A). 9 files.
    ``literal`` -- hardcodes the muon 50-digit literal AND writes a witness.
                   207 files, which is why sampling exists.
    """
    out = []
    for p in sorted(REPO.rglob("*.py")):
        if any(x in p.parts for x in SKIP):
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        if kind == "inline":
            if "M_MU_OVER_M_E" in src and INLINE_Q0.search(src):
                out.append(p)
        else:
            # The literal must be in CODE, not prose. A docstring or comment
            # that MENTIONS the muon pin does not give the producer a q of its
            # own, and without a q of its own the anchor-flip test means
            # nothing -- such a producer SHOULD move, because the manifest q is
            # the only q it has.
            #
            # Measured: m_p_substrate_identity_50dps was selected on a single
            # DOCSTRING mention ("At q_0 = 1.1099785955573347... (50 dps,
            # m_p-pinned re-pin #1422)"), while its only q is
            # `q = mpf(Q_50_DIGIT_STR)` -- the manifest pin. It was then
            # reported as a STRADDLE whose assertion moved, which was wrong and
            # was the headline case of that run.
            #
            # Same prose-vs-code defect fixed in q0_producer_pin_classifier
            # (#5595). Comments never reach the AST, so they are excluded by
            # construction here; docstrings must be excluded explicitly.
            if not (".witness.json" in src and any(w in src for w in WRITES_WITNESS)):
                continue
            try:
                tree = ast.parse(src)
            except SyntaxError:
                continue
            docs = set()
            for n in ast.walk(tree):
                if isinstance(n, (ast.Module, ast.FunctionDef,
                                  ast.AsyncFunctionDef, ast.ClassDef)):
                    d = ast.get_docstring(n, clean=False)
                    if d:
                        docs.add(d)
            in_code = any(
                isinstance(n, ast.Constant) and isinstance(n.value, str)
                and MUON_LITERAL.search(n.value) and n.value not in docs
                for n in ast.walk(tree))
            if in_code:
                out.append(p)


    return out


# ---------------------------------------------------------------------------
# 🛑 `--literal` CANNOT CONCLUDE "STRADDLE". Measured 2026-08-23: it reported 3
# of 14, and ALL THREE were false positives, each for a DIFFERENT benign reason:
#
#   chirality_avg_content_chiral   the literal sits inside an ordinary STRING
#                                  explaining that the PREVIOUSLY COMMITTED
#                                  witness was muon-era. Not a docstring, so
#                                  the docstring guard above does not catch it.
#   sigma_all_evaluator            `_SELFTEST_Q0`, used only in a selftest. Its
#                                  own comment: "the witness IS emitted at the
#                                  live proton q_0 ... the two anchors are
#                                  deliberate."
#   qbeta_eigenphase_taylor_in_u   `Q0_MP_PIN` and `Q0_MUON_PIN` iterated in a
#                                  loop that BUILDS an anchor-comparison table.
#                                  A comparison producer needs both pins --
#                                  AGENTS.md sanctions exactly this.
#
# So a muon literal in code does NOT mean the producer has a q of its own IN
# THE COMPUTED PATH. It may be documentation, a pinned test constant, or one
# leg of a deliberate comparison, and no static selector distinguishes those
# from a live second anchor.
#
# `--candidates` (inline) is NOT affected and remains sound: it keys on a
# COMPUTED CLOSED FORM, `1/(1 - sqrt(Vol/ratio))`, which cannot appear for
# documentation. Its 3 straddles were independently confirmed by tracing the
# carrier to a shared defaulted `_cached_seminormal` call.
#
# Therefore `--literal` reports MOVES, a fact, instead of STRADDLE, a judgement.
LITERAL_VERDICT_NOTE = (
    "MOVES = its output changed under the anchor flip. In --literal mode that "
    "is NOT a straddle verdict: the selector cannot tell a computed second "
    "anchor from a documented one, a selftest constant, or a deliberate "
    "comparison leg. Read the producer."
)


def _run(prod: Path, anchor: str, timeout: int) -> int:
    env = dict(os.environ)
    env["QOU_Q0_ANCHOR"] = anchor
    r = subprocess.run([sys.executable, "-u", prod.name], cwd=prod.parent,
                       capture_output=True, timeout=timeout, env=env)
    return r.returncode


def _tree_witnesses() -> dict:
    """Every witness in the repo, so a SIBLING write cannot escape the restore.

    Snapshotting only `prod.parent` was a real bug, and it is the hazard
    AGENTS.md names: "Producers write SIBLING witnesses ... anything that
    re-runs producers to compare must restore the whole `computations/` tree
    afterwards, not the one file it was looking at." Measured 2026-08-23: a
    24-producer sample left `qbeta-habiro-cyclotomic.witness.json` modified and
    created `keystone-wrt-schurweyl-higher-colour-foreclosure.witness.json`
    outright -- both from producers this audit had classified NO-WITNESS,
    precisely because it was looking in the wrong directory for their output.
    """
    out = {}
    for f in REPO.rglob("*.witness.json"):
        if any(x in f.parts for x in SKIP):
            continue
        try:
            out[f] = f.read_bytes()
        except OSError:
            pass
    return out


def audit(prod: Path, timeout: int = 900, verdict_word: str = "STRADDLE"):
    """(verdict, detail). Restores every witness in the tree, not just local ones."""
    saved = _tree_witnesses()

    def restore():
        for f, b in saved.items():
            try:
                if f.read_bytes() != b:
                    f.write_bytes(b)
            except OSError:
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_bytes(b)
        # Witnesses the run CREATED did not exist in the snapshot; remove them
        # so the tree is left exactly as found.
        for f in REPO.rglob("*.witness.json"):
            if any(x in f.parts for x in SKIP):
                continue
            if f not in saved:
                f.unlink(missing_ok=True)

    try:
        try:
            rc = _run(prod, "physical", timeout)
        except subprocess.TimeoutExpired:
            return "TIMEOUT", f"exceeded {timeout}s — UNTESTED, not clean"
        if rc != 0:
            return "RUN-FAIL", "could not execute — UNTESTED, not clean"
        phys = {}
        for f in REPO.rglob("*.witness.json"):
            if any(x in f.parts for x in SKIP):
                continue
            try:
                if f.read_bytes() != saved.get(f):
                    phys[f] = json.loads(f.read_text())
            except (OSError, json.JSONDecodeError):
                continue
        if not phys:
            return "NO-WITNESS", "library, or writes nothing"
        try:
            _run(prod, "ideal", timeout)
        except subprocess.TimeoutExpired:
            return "TIMEOUT", f"exceeded {timeout}s on the second leg — UNTESTED"
        for f, doc_p in phys.items():
            fa, fb = _flat(doc_p), _flat(json.loads(f.read_text()))
            moved = [k for k in sorted(set(fa) | set(fb))
                     if not any(e in k.split("/") for e in EPHEMERAL)
                     and not any(s in k for s in STAMP_KEYS)
                     and fa.get(k) != fb.get(k)]
            if moved:
                return (verdict_word,
                        f"{len(moved)} field(s) move, e.g. {moved[0]} [{f.name}]")
        return "clean", "anchor flip moves nothing but the stamp"
    finally:
        restore()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("producers", nargs="*")
    ap.add_argument("--candidates", action="store_true",
                    help="audit every inline-q0-derivation producer")
    ap.add_argument("--literal", action="store_true",
                    help="audit the hardcoded-muon-literal producer set (207)")
    ap.add_argument("--sample", type=int, default=0,
                    help="audit a random sample of N (seeded, so reproducible)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=900,
                    help="per-run seconds; an exceeded run is UNTESTED, not clean")
    args = ap.parse_args(argv)

    targets = ([Path(p) for p in args.producers] if args.producers
               else candidates("inline") if args.candidates
               else candidates("literal") if args.literal else [])
    if not targets:
        ap.error("give producer paths, --candidates or --literal")
    population = len(targets)
    if args.sample and args.sample < population:
        random.Random(args.seed).shuffle(targets)
        targets = sorted(targets[:args.sample])

    print("=" * 72)
    print("anchor-flip straddle audit — producers with a q of their own")
    if args.literal:
        print("-" * 72)
        for line in LITERAL_VERDICT_NOTE.split(". "):
            if line.strip():
                print("  " + line.strip().rstrip(".") + ".")
    print("=" * 72)
    counts = {}
    for t in targets:
        verdict, detail = audit(t if t.is_absolute() else REPO / t, args.timeout,
                                "MOVES" if args.literal else "STRADDLE")
        counts[verdict] = counts.get(verdict, 0) + 1
        print(f"  {verdict:11s} {t.stem}: {detail}")
    print("\n  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    if args.sample and args.sample < population:
        tested = counts.get("STRADDLE", 0) + counts.get("clean", 0)
        print(f"  sample {len(targets)} of {population} (seed {args.seed}); "
              f"{tested} actually tested — "
              f"TIMEOUT/RUN-FAIL/NO-WITNESS are UNTESTED, not clean")
    print("=" * 72)
    return 1 if counts.get("STRADDLE") else 0  # MOVES never fails the gate


if __name__ == "__main__":
    raise SystemExit(main())
