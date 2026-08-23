#!/usr/bin/env python3
"""Regenerate `qou-mass`'s vendored `_internal/` modules from `computations/`.

WHY THIS EXISTS
---------------
`qou-mass` ships standalone, so it carries copies of the `computations/`
modules it needs. Those copies were made by hand, and on 2026-08-15 every
single one had drifted from its source:

    _precision                166 changed lines
    active_set_pruning          1
    canonical_braid_crossings 200
    codata_constants          207
    experimental_constants     86
    hecke_characters          204
    hoefsmit_symbolic          19
    isotope_record_schema      32
    knot_volumes               26
    markov_trace_recursive     16
    markov_weights_symbolic    52
    q_parameter               418
    wedderburn_jones_markov    92
    witness_base              815

14 of 14. The drift was not adaptation — inspected, the vendored-only lines
are older docstring text, i.e. the copies are simply behind. One of them
(`canonical_braid_crossings`) was behind by a whole generation: it predated
`classify_crossing` and still carried the narrow `{0, -h, -h/2}` vocabulary
that the qou-gdtb / qou-8zjd arc removed everywhere else.

Hand-vendoring 22 more modules for the `qou-elb0` live-path work would have
guaranteed a repeat at ~2.5x the surface. So the copies are GENERATED now,
and `--check` makes a drifted copy a test failure rather than a discovery
three months later.

THE TRANSFORM
-------------
Two things, and deliberately only two:

1. **Flatten.** `computations/` has `substrate/`, `hecke/`, `markov/`
   subdirectories; `_internal/` is flat. Modules import each other by bare
   name (`from q_parameter import Q`), which resolves because `_internal`
   puts itself on `sys.path`. Flattening is what makes that work.
2. **Drop `import _path_bridge`.** That shim exists to paper over the
   subdirectory layout of `computations/`. A flat `_internal` does not need
   it, and it is not vendored, so leaving the import in would break every
   module on import. This is the one transform the old hand-copies also
   applied, and the only one they applied.

Nothing else is rewritten. If a module ever needs a genuine package-specific
adaptation, it does NOT belong in this script — give it a real seam upstream
so both sides can share one file.

USAGE
-----
    python3 scripts/sync-qou-mass-vendor.py --check    # exit 1 if drifted
    python3 scripts/sync-qou-mass-vendor.py --apply    # regenerate
    python3 scripts/sync-qou-mass-vendor.py --list     # show the cone
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO / "computations"
VENDOR = REPO / "qou-mass" / "src" / "qou_mass" / "_internal"

#: Modules the package's public API needs to reach. The vendored set is the
#: TRANSITIVE cone of these, computed from imports rather than listed by hand
#: -- a hand-maintained list is the same failure mode as a hand-maintained
#: copy. `mass_at_3A_proper` + `hecke_core` are what `canonical_braid()`'s
#: live path needs (qou-elb0); the rest are already-vendored entry points
#: kept so the cone never shrinks below what shipped.
ENTRY_POINTS = (
    "mass_at_3A_proper",
    "hecke_core",
    "canonical_braid_crossings",
    "hoefsmit_symbolic",
    "markov_weights_symbolic",
    "isotope_record_schema",
    "wedderburn_jones_markov",
    "markov_trace_recursive",
    "active_set_pruning",
    "knot_volumes",
    "_precision",
    "witness_base",
    "q_parameter",
    "codata_constants",
    "experimental_constants",
    "hecke_characters",
)

#: Never vendor these even if they appear in the cone.
EXCLUDE = {
    # The subdirectory shim; see THE TRANSFORM above.
    "_path_bridge",
}


def index_sources() -> dict[str, Path]:
    """Map bare module name -> path, over all of `computations/`."""
    idx: dict[str, Path] = {}
    for p in sorted(SRC_ROOT.rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        idx.setdefault(p.stem, p)
    return idx


def compute_cone(idx: dict[str, Path]) -> list[str]:
    """Transitive repo-local import cone of ENTRY_POINTS."""
    seen: set[str] = set()
    queue = list(ENTRY_POINTS)
    while queue:
        mod = queue.pop()
        if mod in seen or mod in EXCLUDE:
            continue
        seen.add(mod)
        path = idx.get(mod)
        if path is None:
            continue  # stdlib or a real third-party dep; not ours to vendor
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    queue.append(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.level == 0:
                    queue.append(node.module.split(".")[0])
    return sorted(m for m in seen if m in idx and m not in EXCLUDE)


def render(path: Path) -> str:
    """Source text as it should appear under `_internal/`.

    The bridge appears in two shapes and BOTH must be handled:

        # flat modules in computations/
        import _path_bridge  # noqa: F401, E402 — Phase 6 bridge...

        # modules under computations/substrate/ etc., a 4-line preamble
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
        import _path_bridge as _bridge   # noqa: E402, F401
        del _sys, _Path, _bridge

    Dropping only the `import` line in the second shape leaves
    `del ..., _bridge` referring to a name that was never bound, and every
    such module then dies at import with `NameError: name '_bridge' is not
    defined`. The package's tests did not catch this because they exercise
    the bundled-witness fast path, never the vendored modules -- which is
    the same reason the copies could rot unnoticed for months.
    """
    out = []
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        stripped = line.strip()
        if stripped.startswith("import _path_bridge"):
            continue
        # Drop the now-unbound `_bridge` from any `del` that names it,
        # keeping the rest of the statement intact.
        if stripped.startswith("del ") and "_bridge" in stripped:
            names = [n.strip() for n in stripped[4:].split(",")]
            names = [n for n in names if n != "_bridge"]
            if not names:
                continue
            indent = line[: len(line) - len(line.lstrip())]
            out.append(f"{indent}del {', '.join(names)}\n")
            continue
        out.append(line)
    return "".join(out)


#: Witnesses land in the PACKAGE ROOT, not `data/`, and that is forced
#: rather than chosen. The vendored modules resolve their witness paths
#: themselves, relative to `Path(__file__).resolve().parent.parent` -- which
#: mirrors `computations/substrate/foo.py` reaching up to `computations/`.
#: Inside the wheel that same expression is `_internal/` -> `qou_mass/`, so
#: this is where they look. Putting them in `data/` (tidier, and where the
#: hand-curated shards live) makes every one of them FileNotFoundError.
#:
#: The honest fix is a package-aware resolver in the modules so vendored
#: data can live under `data/` like everything else -- that is a change to
#: the modules, not to this script, and it is tracked separately. Until
#: then, matching the resolver beats fighting it.
WITNESS_DEST = REPO / "qou-mass" / "src" / "qou_mass"


def required_witnesses(cone: list[str], idx: dict[str, Path]) -> dict[str, Path]:
    """Witness JSONs the vendored modules load at runtime.

    Vendoring the Python alone is not enough: several cone modules read a
    `*.witness.json` on import or first call, so a wheel with the code but
    not the data fails at runtime with FileNotFoundError rather than
    ImportError -- later, and further from the cause.

    Scraped from source text rather than declared by hand, for the same
    reason the module cone is: a hand-kept list drifts exactly like a
    hand-kept copy. Names that match nothing under `computations/` are
    reported, not silently skipped -- a rename upstream should be loud.
    """
    import re
    names: set[str] = set()
    for mod in cone:
        text = idx[mod].read_text(encoding="utf-8", errors="replace")
        # Case-INSENSITIVE. The lowercase-only class silently skipped any
        # witness with a capital in its name — sublemma-2-1-A-operator-extract
        # .witness.json never entered the vendored set, which is exactly the
        # quiet miss this script exists to prevent ("a rename upstream should
        # be loud"). Bean qou-tnrz.
        names.update(re.findall(r"[A-Za-z0-9][A-Za-z0-9._-]*\.witness\.json",
                                text))
    found: dict[str, Path] = {}
    for name in sorted(names):
        hits = [p for p in SRC_ROOT.rglob(name) if "_deprecated" not in p.parts]
        if hits:
            found[name] = hits[0]
    return found


def extra_witnesses(wits: dict) -> dict:
    """Mirror witnesses OUTSIDE the runtime cone, synced where they sit.

    `required_witnesses` covers what the vendored modules load on import; those
    are forced into the package root by the resolver (see WITNESS_DEST). This
    covers the rest of the shipped witness data -- `data/` and
    `data/isotopes/` -- which had no sync path at all and so simply aged.

    Measured before this existed (bean qou-cdj8): 122 such files, every one
    with a same-named `computations/` twin, 120 of them 2026-05-19 copies
    predating both the q0-anchor convention (PR #4020) and the `environment`
    block, and one -- canonical-mass-table-extended -- recording `muon` where
    its source had moved to `proton`.

    Synced IN PLACE rather than into the root: these are not resolved by the
    modules, so the root's placement constraint does not apply, and moving them
    would change import paths for no reason. `_deprecated/` is excluded, matching
    `computations/_deprecated/`.
    """
    src_idx: dict[str, Path] = {}
    for q in (REPO / "computations").rglob("*.witness.json"):
        if "_deprecated" not in q.parts:
            src_idx.setdefault(q.name, q)
    out: dict[Path, Path] = {}
    for dest in sorted(WITNESS_DEST.rglob("*.witness.json")):
        if "_deprecated" in dest.parts:
            continue
        if dest.parent == WITNESS_DEST:      # the cone copies, handled above
            continue
        if dest.name in wits:                # a shadow of a cone copy
            continue
        src = src_idx.get(dest.name)
        if src is not None:
            out[dest] = src
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true",
                   help="exit 1 if any vendored copy differs from its source")
    g.add_argument("--apply", action="store_true", help="regenerate the copies")
    g.add_argument("--list", action="store_true", help="print the cone and exit")
    args = ap.parse_args()

    idx = index_sources()
    cone = compute_cone(idx)

    wits = required_witnesses(cone, idx)
    extras = extra_witnesses(wits)

    if args.list:
        print(f"{len(cone)} modules in the vendoring cone:")
        for m in cone:
            print(f"  {m:<34} {idx[m].relative_to(REPO)}")
        print(f"\n{len(wits)} witness JSON(s) they load at runtime:")
        for n, p in wits.items():
            print(f"  {n:<48} {p.stat().st_size:>8} B")
        print(f"\n{len(extras)} further witness JSON(s) shipped as package data:")
        for d in list(extras)[:6]:
            print(f"  {str(d.relative_to(WITNESS_DEST)):<48}")
        if len(extras) > 6:
            print(f"  ... and {len(extras) - 6} more")
        return 0

    drifted, missing, added = [], [], []
    for name, src in wits.items():
        dest = WITNESS_DEST / name
        want = src.read_bytes()
        # Report the path this actually writes. It was `f"data/{name}"`, but
        # `dest` is `WITNESS_DEST / name` -- the package ROOT, which is where
        # the resolver looks and where the header says these are forced to
        # live. No `data/q-pinning-50-digit.witness.json` exists; the label
        # pointed at a file that was never there. Harmless while `data/` held
        # nothing synced, and actively misleading now that it does.
        rel = dest.relative_to(WITNESS_DEST).as_posix()
        if not dest.exists():
            missing.append(rel)
        elif dest.read_bytes() != want:
            drifted.append(rel)
        if args.apply:
            dest.write_bytes(want)
    for dest, src in extras.items():
        rel = dest.relative_to(WITNESS_DEST)
        want = src.read_bytes()
        if dest.read_bytes() != want:
            drifted.append(str(rel))
        if args.apply:
            dest.write_bytes(want)
    for mod in cone:
        want = render(idx[mod])
        dest = VENDOR / f"{mod}.py"
        if not dest.exists():
            missing.append(mod)
        elif dest.read_text(encoding="utf-8") != want:
            drifted.append(mod)
        if args.apply:
            dest.write_text(want, encoding="utf-8")
            added.append(mod)

    # A vendored file with no counterpart in the cone is dead weight; report
    # it rather than deleting, since removing a shipped module is an API
    # decision and this script should not make one silently.
    orphans = sorted(
        p.stem for p in VENDOR.glob("*.py")
        if p.stem != "__init__" and p.stem not in cone
    )

    if args.apply:
        print(f"regenerated {len(added)} module(s) into "
              f"{VENDOR.relative_to(REPO)}")
        if orphans:
            print(f"  note: {len(orphans)} vendored file(s) are not in the "
                  f"cone: {', '.join(orphans)}")
        return 0

    if not drifted and not missing:
        print(f"vendored copies are in sync ({len(cone)} modules, "
              f"{len(wits)} witness JSON, {len(extras)} package-data "
              f"witness JSON)")
        # State what is NOT covered -- the count that used to be 122.
        #
        # It was 122 because the comparison reached only the cone plus the
        # witnesses `required_witnesses` scrapes, while `data/` and
        # `data/isotopes/` had no sync path at all. `extra_witnesses` now
        # covers them, so this should read 0; anything left is a shipped
        # witness with NO same-named source under `computations/`, which is
        # a real question (renamed upstream? hand-authored?) rather than
        # staleness. Bean qou-cdj8.
        covered = set(wits) | {d.name for d in extras}
        uncovered = sorted(
            q.relative_to(WITNESS_DEST).as_posix()
            for q in WITNESS_DEST.rglob("*.witness.json")
            if "_deprecated" not in q.parts and q.name not in covered
        )
        if uncovered:
            print(f"  note: {len(uncovered)} witness(es) have no source under "
                  f"computations/ and are synced by nothing: "
                  f"{', '.join(uncovered[:4])}"
                  + (" ..." if len(uncovered) > 4 else ""))

        # Duplicated names are worse than uncovered ones. The header above
        # explains that witnesses MUST sit in the package root because the
        # vendored modules resolve there; a `data/` copy of a synced witness
        # is unreachable at runtime, so it cannot fail loudly -- it just sits
        # there being read by humans. Two of the 17 such pairs are stale by a
        # month, including `q-pinning-50-digit`, the substrate modulus record.
        # Reported rather than deleted, for the same reason `orphans` is:
        # removing a shipped file is an API decision this script should not
        # make silently.
        shadowed = sorted(
            q.name for q in (WITNESS_DEST / "data").glob("*.witness.json")
            if (WITNESS_DEST / q.name).exists()
        )
        divergent = [n for n in shadowed
                     if (WITNESS_DEST / n).read_bytes()
                     != (WITNESS_DEST / "data" / n).read_bytes()]
        if shadowed:
            print(f"  note: {len(shadowed)} witness(es) exist in BOTH the "
                  f"package root and data/; the data/ copy is unreachable at "
                  f"runtime ({len(divergent)} of them also differ in content"
                  + (f": {', '.join(divergent)}" if divergent else "") + ")")
        if orphans:
            print(f"  note: not in cone: {', '.join(orphans)}")
        return 0

    if missing:
        print(f"MISSING from {VENDOR.relative_to(REPO)} ({len(missing)}):")
        for m in missing:
            print(f"  {m}")
    if drifted:
        print(f"DRIFTED from source ({len(drifted)}):")
        for m in drifted:
            print(f"  {m}")
    print("\nRun: python3 scripts/sync-qou-mass-vendor.py --apply")
    print("Do NOT hand-edit files under _internal/ -- they are generated.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
