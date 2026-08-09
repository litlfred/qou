#!/usr/bin/env python3
"""averaged_label_consumer_scan.py — who else rebuilds a Hecke operator from the
lossy "averaged" crossing label?

THE DEFECT (bean qou-pin6; fixed in `rho_w_crystal_vertex_trace` 2026-08-09)
    `canonical_braid_crossings.classify_crossing` used to map two physically
    distinct crossings onto ONE label:

        d = -h/2                 color-BLIND
        d = -h*(1/2 - delta/4)   color-WEIGHTED p-n interface

    `atom_canonical_crossings` returns only `(gen_idx, ctype)`, so a consumer
    that reconstructs an operator from the ctype cannot tell which crossing it
    had. `rho_w_crystal_vertex_trace` built `sigma_g - (h/2)*1` for every
    averaged crossing, dropping delta on the single p-n interface, which put its
    chi^lambda 1.1e-4 away from the chi cache on every MIXED atom.

    `classify_crossing` now takes `distinguish_color=True` to split the label
    into `"averaged"` / `"averaged_pn"`. The default is unchanged, so every
    consumer that has not opted in still gets the lossy label.

WHO IS ACTUALLY AT RISK
    Grepping for the string `"averaged"` is far too coarse -- ~45 files mention
    it, most of which only COUNT crossings, name them in a docstring, or hand
    the word to a backend that re-derives coefficients from `(c, d)` itself.
    Those are unaffected.

    The vulnerable shape is specific, and this scan tests for it directly:

      1. the file actually CONSUMES a crossing word (imports
         `atom_canonical_crossings`), AND
      2. it BRANCHES on the ctype being "averaged" -- a comparison or a dict
         key -- AND
      3. it CONSTRUCTS something from `h` (h/2, h*0.5, ...), either inside that
         branch or in the operator table the branch looks up.

    All three together mean the operator is being rebuilt from a label that
    cannot distinguish the two crossings. Any one alone is harmless.

    Requirement 1 is not cosmetic. Without it the scan flags files whose
    "averaged" is a BOND-type key (pp / nn / pn) rather than a crossing ctype:
    `probe_9b_gate_interface_algebra` maps `"averaged"` to `f_pn` and ALREADY
    carries delta, so it is the opposite of the defect. Adding requirement 1
    took the report from 10 hits to 5 real ones.

    Requirement 3 must look outside the branch as well: `rho_w` dispatched
    `elif ctype == "averaged": G = inter[g]` while `inter` was built with h/2 in
    another function. A construct-in-branch test alone misses the very file the
    investigation started from.

    A consumer that opts into `distinguish_color=True` is reported as FIXED.

Read-only. Reports; fixes nothing.
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent

AVG_LITERALS = {"averaged", "averaged_pn"}


def _uses_h(node: ast.AST) -> bool:
    """Does this subtree build something from the substrate h?"""
    for n in ast.walk(node):
        if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Div, ast.Mult)):
            for side in (n.left, n.right):
                if isinstance(side, ast.Name) and side.id in ("h", "h_val", "H"):
                    return True
                if isinstance(side, ast.Attribute) and side.attr in ("h", "h_val"):
                    return True
    return False


def _dispatches_on_averaged(tree: ast.AST) -> list[int]:
    """Line numbers where the code BRANCHES on the ctype being averaged.

    Separate from the h-construction test because the two are routinely in
    different functions: `rho_w_crystal_vertex_trace` dispatched
    `elif ctype == "averaged": G = inter[g]` while `inter` was built with h/2
    inside `generator_word_matrices`. A construct-in-branch test alone misses
    exactly the file the whole investigation started from.
    """
    hits: list[int] = []
    for n in ast.walk(tree):
        if isinstance(n, ast.If):
            d = ast.dump(n.test)
            if any(f"'{a}'" in d or f'"{a}"' in d for a in AVG_LITERALS):
                hits.append(n.lineno)
        if isinstance(n, ast.Dict):
            for k in n.keys:
                if isinstance(k, ast.Constant) and k.value in AVG_LITERALS:
                    hits.append(getattr(k, "lineno", n.lineno))
        if isinstance(n, ast.Compare):
            d = ast.dump(n)
            if any(f"'{a}'" in d or f'"{a}"' in d for a in AVG_LITERALS):
                hits.append(n.lineno)
    return sorted(set(hits))


def _builds_from_h_anywhere(tree: ast.AST) -> bool:
    return _uses_h(tree)


def _branches_on_averaged_with_h(tree: ast.AST) -> list[int]:
    """Line numbers where an 'averaged' branch constructs from h."""
    hits: list[int] = []
    for n in ast.walk(tree):
        # if/elif ctype == "averaged": ... h/2 ...
        if isinstance(n, ast.If):
            test_src = ast.dump(n.test)
            if any(f"'{a}'" in test_src or f'"{a}"' in test_src
                   for a in AVG_LITERALS):
                if any(_uses_h(b) for b in n.body):
                    hits.append(n.lineno)
        # {"averaged": <expr built from h>}
        if isinstance(n, ast.Dict):
            for k, v in zip(n.keys, n.values):
                if isinstance(k, ast.Constant) and k.value in AVG_LITERALS:
                    if _uses_h(v):
                        hits.append(getattr(k, "lineno", n.lineno))
    return sorted(set(hits))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any consumer is still at risk")
    args = ap.parse_args(argv)

    at_risk, fixed, mentions_only = [], [], 0
    for p in sorted(COMPUTE_DIR.rglob("*.py")):
        if "_deprecated" in p.parts or p.parent == HERE:
            continue
        try:
            src = p.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        if "averaged" not in src:
            continue
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        # REQUIREMENT 1: it must actually consume a crossing word. Without this
        # the scan flags files whose "averaged" is a BOND-type key (pp/nn/pn),
        # not a crossing ctype — `probe_9b_gate_interface_algebra` maps
        # "averaged" to f_pn and already carries delta, so it is not the defect
        # at all. That check alone turned 10 reported hits into 5 real ones.
        consumes_word = "atom_canonical_crossings" in src
        # A file that already builds the color-weighted coefficient knows about
        # delta, so it is not blindly applying -h/2.
        has_delta = ("delta / 4" in src or "delta/4" in src
                     or "δ/4" in src or "δ / 4" in src)
        if not consumes_word:
            mentions_only += 1
            continue

        direct = _branches_on_averaged_with_h(tree)
        split = (_dispatches_on_averaged(tree) if not direct else [])
        if split and not _builds_from_h_anywhere(tree):
            split = []                      # dispatches, but builds no operator
        hits = direct or split
        if not hits:
            mentions_only += 1
            continue
        rel = str(p.relative_to(REPO))
        kind = "construct-in-branch" if direct else "dispatch + h elsewhere"
        if has_delta:
            kind += "; already references delta — verify by hand"
        if "distinguish_color=True" in src:
            fixed.append((rel, hits, kind))
        else:
            at_risk.append((rel, hits, kind))

    print("=" * 78)
    print('who rebuilds a Hecke operator from the lossy "averaged" label?')
    print("=" * 78)
    print(f"  files mentioning 'averaged' but NOT rebuilding an operator : "
          f"{mentions_only}  (unaffected)")
    print()
    print(f"  FIXED — opted into distinguish_color=True ({len(fixed)}):")
    for rel, hits, kind in fixed:
        print(f"      {rel}\n          {kind}, line(s) {hits}")
    print()
    print(f"  AT RISK — rebuilds from the lossy label ({len(at_risk)}):")
    for rel, hits, kind in at_risk:
        print(f"      {rel}\n          {kind}, line(s) {hits}")
    if at_risk:
        print()
        print("  Each of these applies the COLOR-BLIND -h/2 to every averaged")
        print("  crossing. On a MIXED atom (deuteron, tritium, He-3, He-4) that")
        print("  drops delta on the single p-n interface. Homogeneous atoms")
        print("  (p, n, pp, nn) have no p-n interface and are unaffected, which")
        print("  is why the defect stayed invisible.")
        print()
        print("  Fix: pass distinguish_color=True to atom_canonical_crossings and")
        print("  dispatch 'averaged_pn' to sigma_g - h*(1/2 - delta/4)*1.")
    print("=" * 78)
    return 1 if (args.strict and at_risk) else 0


if __name__ == "__main__":
    raise SystemExit(main())
