#!/usr/bin/env python3
"""q0_declaration_bindability_audit.py — manifest declarations that CANNOT BIND.

Beans `qou-cds3` / `qou-fd0e`.

THE DEFECT. `computations/q0_anchor_manifest.json` declares a producer's q0
layer by listing its stem under `ideal_muon`. That declaration is honoured by
exactly one mechanism: the anchor auto-select in
`computations/substrate/q_parameter.py`, which rebinds the module's own q0
accessors when the running producer's `sys.argv[0]` stem is in the list. The
rebinding happens **inside the `q_parameter` module namespace**.

So a producer that never obtains q0 through `q_parameter` is unaffected by its
own declaration. Verified by execution, not by reading:

    q_parameter.q_at(50), stem in ideal_muon      -> 1.1099785955573347198997…  (muon)
    q_parameter.q_at(50), stem not in manifest    -> 1.10997858275138…          (proton)
    qou_substrate.constants.q_at(50)              -> 1.10997858275138…          (ALWAYS)

Declaring such a stem `ideal_muon` does not change one digit of what it
computes. It changes only what `resolve_q0_anchor` STAMPS on the witness — so
the sole effect of an unbindable declaration is to attach a muon label to a
proton computation. That is not a no-op; it is the mislabel this campaign is
chasing, manufactured by the mechanism meant to prevent it.

WHY A DEDICATED AUDIT. Nothing else can see this. The manifest is data, so no
Python check reads it; the anchor-consistency audit compares stamps against
payloads and never asks whether a declaration was capable of acting; and the
drift audit reports which producers are NOT declared, which is the opposite
question. This one asks: **of the stems that ARE declared, which declarations
can actually do anything?**

METHOD. For each declared stem, resolve it to exactly one `*.py`, AST-parse it,
and ask whether `q_parameter` is reachable:

  direct      the producer itself imports from `q_parameter`
  via_helper  it imports a LOCAL module that imports `q_parameter`

The second class is not decoration. `computations/probes/_gap_a4_qsafe.py`
supplies q0 to 17 producers, and a detector that inspects only the caller sees a
producer with no q0 route at all — the failure recorded in `qou-fd0e`. One level
of transitive resolution is followed, and `via_helper` is reported SEPARATELY
rather than merged into `direct`, because a helper that binds the name at import
time is not obviously equivalent to a call made later, and this audit does not
have the standing to assert that it is.

Anything else is `unbindable`, and the route it actually uses is printed, so the
finding arrives with its own diagnosis attached.

SCOPE IS PRINTED WHETHER OR NOT IT IS FLATTERING. A stem that resolves to zero
files or to several is `unresolved` — unexamined, not clean, counted separately,
and never folded into either verdict.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 60
PIN_MUON = mpf("1.10997859555733471989976322048322502665620840878")
PIN_PROTON = mpf("1.1099785827513808075916690956")
_PIN_TOL_PPB = mpf("1")
_Q0_LIT = re.compile(r"1\.109[0-9]{4,}")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parent
MANIFEST = ROOT / "q0_anchor_manifest.json"

_SKIP = {"_deprecated", ".git", "__pycache__", "node_modules"}

#: Modules whose q0 accessors the manifest CANNOT reach, with the reason.
_UNGOVERNED = {
    "qou_substrate.constants": "qou_substrate.constants (never anchor-governed)",
    "substrate.qou_substrate.constants": "qou_substrate.constants (never anchor-governed)",
}


def _index() -> "dict[str, list[Path]]":
    idx: "dict[str, list[Path]]" = {}
    for f in REPO.rglob("*.py"):
        if _SKIP & set(f.parts):
            continue
        idx.setdefault(f.stem, []).append(f)
    return idx


def _imports(tree) -> "set[str]":
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom) and n.module:
            out.add(n.module)
        elif isinstance(n, ast.Import):
            for a in n.names:
                out.add(a.name)
    return out


def _is_qparam(m: str) -> bool:
    return m == "q_parameter" or m.endswith(".q_parameter")


def _route(src: str, mods: "set[str]") -> str:
    """What DOES supply q0 here, when q_parameter does not?"""
    for m in mods:
        if m in _UNGOVERNED:
            return _UNGOVERNED[m]
    if "q-pinning-50-digit.witness.json" in src:
        return "reads q-pinning-50-digit.witness.json directly"
    if "1.10997859" in src or "1.1099785827" in src:
        return "hardcoded q0 literal"
    return "no q0 route found"


def _computes(src: str, mods: "set[str]") -> str:
    """What LAYER does an unbindable producer actually compute at?

    This split is the whole difference between a defect and a correct fix, and
    getting it wrong would report the `qou-fd0e` declarations as bugs. An
    unbindable declaration attaches a MUON stamp regardless; whether that stamp
    is true depends entirely on what the producer already computes:

      computes muon   -> the declaration makes a proton-defaulted stamp truthful
      computes proton -> the declaration attaches a false label  <- the defect

    Decided by mpmath distance for literals (so a truncation classifies like a
    50-digit value) and by call site for the ungoverned-module route.
    """
    if any(m in _UNGOVERNED for m in mods):
        try:
            tree = ast.parse(src)
        except Exception:  # noqa: BLE001
            return "unknown"
        called = {n.func.id for n in ast.walk(tree)
                  if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
        has_m, has_p = "q_muon_at" in called, "q_at" in called
        if has_m and has_p:
            return "both"
        if has_m:
            return "muon"
        if has_p:
            return "proton"
        return "unknown"
    if "q-pinning-50-digit.witness.json" in src:
        return "muon"          # that witness IS the muon anchor-defining file
    layers = set()
    for m in _Q0_LIT.finditer(src):
        try:
            v = mpf(m.group(0))
        except Exception:  # noqa: BLE001
            continue
        if abs((v - PIN_MUON) / PIN_MUON * mpf(10) ** 9) < _PIN_TOL_PPB:
            layers.add("muon")
        elif abs((v - PIN_PROTON) / PIN_PROTON * mpf(10) ** 9) < _PIN_TOL_PPB:
            layers.add("proton")
    if layers == {"muon"}:
        return "muon"
    if layers == {"proton"}:
        return "proton"
    if len(layers) > 1:
        return "both"
    return "unknown"


#: What each manifest layer CLAIMS a producer computes at.
_LAYER_CLAIM = {"ideal_muon": "muon", "physical_proton": "proton"}


def _unbindable(f, src: str, mods: "set[str]", route: str,
                expect: str | None) -> "tuple[str, str]":
    """Every unbindable exit goes through here, so the compute-layer split is
    applied uniformly. An earlier revision split only ONE of the three exits,
    and the two that bypassed it raised a KeyError rather than silently
    mis-bucketing — the one failure mode worth being grateful for.

    `expect` is what the DECLARED LAYER claims. The verdict is relative to it:
    an earlier revision hardcoded the muon framing, so running `--layer
    physical_proton` reported every correctly-proton producer as a false stamp.
    A detector whose labels invert on a different input is worse than no
    detector, because it reads as evidence.
    """
    comp = _computes(src, mods)
    if comp == "both":
        verdict = "unbindable_comparison"
    elif comp == "unknown" or expect is None:
        verdict = "unbindable_unknown"
    elif comp == expect:
        verdict = "unbindable_stamp_ok"
    else:
        verdict = "unbindable_stamp_FALSE"
    return verdict, f"{f.relative_to(REPO)}  ::  {route} -> computes {comp}"


def _classify(stem: str, idx, expect: str | None) -> "tuple[str, str]":
    cands = idx.get(stem, [])
    if len(cands) != 1:
        return "unresolved", f"{len(cands)} files match this stem"
    f = cands[0]
    try:
        src = f.read_text(encoding="utf-8", errors="ignore")
        tree = ast.parse(src)
    except Exception as exc:  # noqa: BLE001
        return "unresolved", f"{exc.__class__.__name__} parsing {f.name}"
    mods = _imports(tree)
    if any(_is_qparam(m) for m in mods):
        return "direct", str(f.relative_to(REPO))

    # A KNOWN-UNGOVERNED q0 module settles it, and must be tested BEFORE the
    # transitive step. Getting this order wrong silently cleared five producers
    # that are the campaign's central defect: `qou_substrate.constants` was
    # reduced to the bare stem `constants`, matched against an unrelated
    # `constants.py` elsewhere in the tree, and followed to q_parameter — so a
    # module listed two lines below as never-governed was reported bindable.
    # Never resolve a dotted import by its last component alone.
    for m in mods:
        if m in _UNGOVERNED:
            return _unbindable(f, src, mods, _UNGOVERNED[m], expect)
    if "q-pinning-50-digit.witness.json" in src:
        return _unbindable(f, src, mods,
                           "reads q-pinning-50-digit.witness.json directly", expect)

    # one transitive level: a LOCAL helper that itself reaches q_parameter
    for m in mods:
        if m in _UNGOVERNED or _is_qparam(m):
            continue
        base = m.split(".")[-1]
        cands = idx.get(base, [])
        if len(cands) != 1:
            continue          # ambiguous stem: do not guess which file it is
        h = cands[0]
        if h == f:
            continue
        try:
            htree = ast.parse(h.read_text(encoding="utf-8", errors="ignore"))
        except Exception:  # noqa: BLE001
            continue
        if any(_is_qparam(x) for x in _imports(htree)):
            return "via_helper", f"{f.relative_to(REPO)}  <- {base}"
    return _unbindable(f, src, mods, _route(src, mods), expect)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--layer", default="ideal_muon",
                    help="manifest layer to check (default ideal_muon)")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any declaration in the layer cannot bind")
    ap.add_argument("--show", type=int, default=40)
    args = ap.parse_args()

    man = json.loads(MANIFEST.read_text())
    stems = man.get(args.layer, [])
    idx = _index()
    expect = _LAYER_CLAIM.get(args.layer)
    if expect is None:
        print(f"  NOTE: layer {args.layer!r} claims no single compute layer, so"
              "\n        every unbindable stem is reported as undetermined"
              " rather than judged.")
    buckets: "dict[str, list[str]]" = {
        "direct": [], "via_helper": [], "unbindable_stamp_FALSE": [],
        "unbindable_stamp_ok": [], "unbindable_comparison": [],
        "unbindable_unknown": [], "unresolved": []}
    for s in sorted(stems):
        verdict, detail = _classify(s, idx, expect)
        buckets[verdict].append(f"{s}   {detail}")

    print("=" * 74)
    print(f" manifest declarations that cannot bind — layer {args.layer!r}")
    print("=" * 74)
    print(f"  declared stems                 {len(stems)}")
    print(f"    bindable, direct             {len(buckets['direct'])}")
    print(f"    bindable via a local helper  {len(buckets['via_helper'])}"
          "   <- reported separately, not merged")
    n_unb = sum(len(v) for k, v in buckets.items() if k.startswith("unbindable"))
    print(f"    CANNOT BIND                  {n_unb}")
    print("      of those, the stamp it attaches is:")
    print(f"        contradicts the declaration {len(buckets['unbindable_stamp_FALSE'])}"
          "   <- the defect")
    print(f"        agrees with it              {len(buckets['unbindable_stamp_ok'])}"
          "   <- benign; a stamp fix, not a layer fix")
    print(f"        a comparison (computes both) {len(buckets['unbindable_comparison'])}"
          " <- no single anchor is meaningful")
    print(f"        undetermined                 {len(buckets['unbindable_unknown'])}"
          "   <- unexamined, not clean")
    print(f"    unresolved                   {len(buckets['unresolved'])}"
          "   <- unexamined, not clean")

    if buckets["unbindable_stamp_FALSE"]:
        print(f"\n  DECLARED {args.layer!r} (claims {expect}), COMPUTES THE OTHER"
              " LAYER, and the declaration cannot")
        print("  bind — so it cannot fix the compute and only mislabels the witness:")
        for x in buckets["unbindable_stamp_FALSE"][:args.show]:
            print(f"    {x}")
    if buckets["unbindable_comparison"]:
        print("\n  cross-anchor (declaring EITHER layer rewrites one arm):")
        for x in buckets["unbindable_comparison"][:args.show]:
            print(f"    {x}")
    if buckets["unbindable_unknown"]:
        print(f"\n  compute layer undetermined ({len(buckets['unbindable_unknown'])}):")
        for x in buckets["unbindable_unknown"][:args.show]:
            print(f"    {x}")
    if buckets["unresolved"]:
        print(f"\n  unresolved ({len(buckets['unresolved'])}):")
        for x in buckets["unresolved"][:args.show]:
            print(f"    {x}")

    if args.strict and buckets["unbindable_stamp_FALSE"]:
        print("\n  --strict: exiting 1 on a declaration that cannot bind.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
