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


def _computes(src: str, mods: "set[str]", idx=None) -> str:
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
    layers = _layer_of_source(src)
    if not layers and idx is not None:
        layers = _helper_layer(src, idx) | _call_site_layer(src, _SIGS)
    if layers == {"muon"}:
        return "muon"
    if layers == {"proton"}:
        return "proton"
    if len(layers) > 1:
        return "both"
    return "unknown"


def _layer_of_source(text: str) -> "set[str]":
    """Which pin layers does this snippet of source evidence carry?"""
    out = set()
    if "q-pinning-50-digit.witness.json" in text:
        out.add("muon")          # that witness IS the muon anchor-defining file
    for m in _Q0_LIT.finditer(text):
        try:
            v = mpf(m.group(0))
        except Exception:  # noqa: BLE001
            continue
        if abs((v - PIN_MUON) / PIN_MUON * mpf(10) ** 9) < _PIN_TOL_PPB:
            out.add("muon")
        elif abs((v - PIN_PROTON) / PIN_PROTON * mpf(10) ** 9) < _PIN_TOL_PPB:
            out.add("proton")
    return out


def _helper_layer(src: str, idx) -> "set[str]":
    """q0 layers reaching this producer through a SHARED HELPER.

    Keyed on the imported NAME, never on the module. `_gap_a4_qsafe` exports a
    muon pin as `Q_0_50DPS` and also exports `q_number`, `dim_q_partition`,
    `classical_dim_partition`, which carry no q0 at all; `_li_2_q_util` exports
    `load_q_50dps` (which reads the muon anchor-defining witness) alongside
    `li_2_q` and density helpers. Attributing a layer to every importer of the
    module would credit q0 to producers that only wanted a q-integer — the
    "spelled, not done" error this audit has already made twice.

    So: resolve the module to a unique local file, find each imported name's own
    top-level binding, and read the evidence from THAT binding's subtree only.
    """
    layers: "set[str]" = set()
    try:
        tree = ast.parse(src)
    except Exception:  # noqa: BLE001
        return layers
    for n in ast.walk(tree):
        if not isinstance(n, ast.ImportFrom) or not n.module:
            continue
        if n.module in _UNGOVERNED or _is_qparam(n.module):
            continue                      # handled by the callers, above
        cands = idx.get(n.module.split(".")[-1], [])
        if not cands:
            continue
        wanted = {a.name for a in n.names}
        # A stem matching several files is only a problem if they DISAGREE.
        # `_li_2_q_util` exists twice — under `computations/` and under
        # `qou-mass/src/qou_mass/_internal/` — and both resolve `load_q_50dps`
        # to the same muon anchor-defining witness. Refusing to answer there
        # would leave 13 stems "undetermined" over an ambiguity that changes
        # nothing. So: resolve every candidate, and accept the answer only when
        # they all agree.
        per_cand = []
        for c in cands:
            got: "set[str]" = set()
            try:
                hsrc = c.read_text(encoding="utf-8", errors="ignore")
                htree = ast.parse(hsrc)
            except Exception:  # noqa: BLE001
                continue
            hlines = hsrc.splitlines()
            for node in htree.body:       # top level only: that is the binding
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # A FUNCTION's body must NOT be read for a layer. This cost
                    # a 31-item false finding: `_li_2_q_util.load_q_50dps`
                    # MENTIONS `q-pinning-50-digit.witness.json`, but only reads
                    # it when the caller passes `anchor="muon"` — the default has
                    # been `"proton"` since 2026-08-22 (beans qou-dkm2/qou-v90i,
                    # which drained exactly this population). Attributing muon to
                    # every importer inverted the answer for all of them.
                    #
                    # A helper FUNCTION's layer lives at the CALL SITE, not in
                    # its body, and is resolved there. Constants are different:
                    # an imported name bound to a literal carries its value.
                    continue
                if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                    continue
                tgts = (node.targets if isinstance(node, ast.Assign)
                        else [node.target])
                bound = {t.id for t in tgts if isinstance(t, ast.Name)}
                if not (bound & wanted):
                    continue
                seg = "\n".join(
                    hlines[node.lineno - 1: (node.end_lineno or node.lineno)])
                got |= _layer_of_source(seg)
            if got:
                per_cand.append(frozenset(got))
        if per_cand and len(set(per_cand)) == 1:
            layers |= set(per_cand[0])
    return layers


def _anchor_signature(idx) -> "dict[str, tuple[str, list[str]]]":
    """Helper functions that take an `anchor`, and the DEFAULT they apply.

    Read from the helper's own `def` line, not assumed. `load_q_50dps` is the
    case that matters: `anchor: str = "proton"`. Verified by execution rather
    than by reading —

        load_q_50dps()               -> 1.10997858275138…   proton
        load_q_50dps(anchor="muon")  -> 1.10997859555733…   muon

    which is the check that should have preceded the 31-item false finding, and
    is why a bare call is now resolvable instead of being guessed.
    """
    seen: "dict[str, set]" = {}
    params_of: "dict[str, list[str]]" = {}
    # Duplicated helpers are the norm here, not the exception — `_li_2_q_util`
    # exists under both `computations/` and `qou-mass/src/qou_mass/_internal/`.
    # Skipping every duplicated stem is what kept this resolution from firing at
    # all. Collect from EVERY candidate and accept only where they agree.
    for cands in idx.values():
        for f in cands:
            try:
                tree = ast.parse(f.read_text(encoding="utf-8", errors="ignore"))
            except Exception:  # noqa: BLE001
                continue
            for node in tree.body:
                if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                params = [a.arg for a in node.args.args]
                if "anchor" not in params:
                    continue
                n_def = len(node.args.defaults)
                defaults = dict(zip(params[len(params) - n_def:],
                                    node.args.defaults))
                d = defaults.get("anchor")
                if isinstance(d, ast.Constant) and d.value in ("muon", "proton"):
                    seen.setdefault(node.name, set()).add(d.value)
                    params_of[node.name] = params
    out: "dict[str, tuple[str, list[str]]]" = {}
    for name, vals in seen.items():
        if len(vals) == 1:
            out[name] = (next(iter(vals)), params_of[name])
    return out


def _call_site_layer(src: str, sigs=None) -> "set[str]":
    """Layers determined at a helper CALL SITE.

    An explicit `anchor="muon"` settles it. A bare call takes the helper's own
    signature default, which is READ from that helper rather than assumed — see
    `_anchor_signature`.

    One exception is honoured because the helper documents it: `load_q_50dps`
    says an explicit ``path`` "wins over ``anchor``". A call passing `path` is
    therefore left undetermined rather than credited to the default.
    """
    out: "set[str]" = set()
    try:
        tree = ast.parse(src)
    except Exception:  # noqa: BLE001
        return out
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        explicit = None
        kwargs = {kw.arg for kw in n.keywords}
        for kw in n.keywords:
            if kw.arg == "anchor" and isinstance(kw.value, ast.Constant) \
                    and kw.value.value in ("muon", "proton"):
                explicit = kw.value.value
        if explicit:
            out.add(explicit)
            continue
        if not sigs or not isinstance(n.func, ast.Name):
            continue
        sig = sigs.get(n.func.id)
        if not sig:
            continue
        default, params = sig
        if "path" in kwargs:
            continue                  # an explicit path overrides the anchor
        if "path" in params and len(n.args) > params.index("path"):
            continue                  # …positionally, too
        out.add(default)
    return out


_SIGS: "dict[str, tuple[str, list[str]]]" = {}


#: What each manifest layer CLAIMS a producer computes at.
_LAYER_CLAIM = {"ideal_muon": "muon", "physical_proton": "proton"}


def _unbindable(f, src: str, mods: "set[str]", route: str,
                expect: str | None, idx=None) -> "tuple[str, str]":
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
    comp = _computes(src, mods, idx)
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
            return _unbindable(f, src, mods, _UNGOVERNED[m], expect, idx)
    if "q-pinning-50-digit.witness.json" in src:
        return _unbindable(f, src, mods,
                           "reads q-pinning-50-digit.witness.json directly",
                           expect, idx)

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
    return _unbindable(f, src, mods, _route(src, mods), expect, idx)


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
    global _SIGS
    _SIGS = _anchor_signature(idx)
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
        print(f"\n  DECLARED {args.layer!r} (claims {expect}) but COMPUTES THE"
              " OTHER LAYER, and the")
        print("  declaration cannot bind, so it cannot correct that. WHICH SIDE IS")
        print("  WRONG IS NOT THIS AUDIT'S CALL: gap_a4_T10 is declared proton and")
        print("  its producer, payload and stamp all say muon — there the MANIFEST")
        print("  is the false record. Elsewhere the compute is right and the stamp")
        print("  inherits the bad declaration. Read the producer before ruling:")
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
