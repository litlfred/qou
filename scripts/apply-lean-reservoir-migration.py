#!/usr/bin/env python3
"""apply-lean-reservoir-migration.py — Deterministic Q3 Option 1 Multi-`lean_lib` Migration & Open-PR Fixup Tool.

Driven by `docs/audits/2026-11-24-lean-reservoir-module-map.json` (emitted by
`scripts/lean-kg-detangler.py --map-out`) and the detangler's classifier for newly
added modules on open PR branches:

  (a) Moves `.lean` library modules into their isolated `[[lean_lib]]` roots inside
      `folio/quantum-observable-universe/lean/`:
        - Tier A: `MathlibExt/`
        - Tier B (6 Reservoir libraries): `QCalculus/`, `TwistedFrobeniusHopf/`,
          `ToricConicOpt/`, `CompactQuantumMetrics/`, `HeckeTemperleyLieb/`,
          `BraidKnotOctonion/`
        - Monograph QOU (12 canonical chapter subgraphs): `QOU/Core/`,
          `QOU/LiftingDescent/`, `QOU/BraidsAndKnots/`, `QOU/BringsSurface/`,
          `QOU/Confinement/`, `QOU/EightfoldWay/`, `QOU/MassTheory/`,
          `QOU/Nuclear/`, `QOU/StandardModel/`, `QOU/FluidDynamics/`,
          `QOU/InformationTheory/`, `QOU/Observations/`
  (b) Declares the `7 + 1` `[[lean_lib]]` targets in
      `folio/quantum-observable-universe/lean/lakefile.toml` + root `<Lib>.lean` files.
  (c) Rewrites all `import Old.Module` lines across library `.lean` files and
      content-block `.lean` siblings across `folio/`.
  (d) Rewrites `.ts` `lean.ref` module paths when module-qualified (or when a
      sibling-less block previously resolved only through a retired folder aggregator),
      preserving the `qou:<Decl>` URI package prefix (`0` changes to `schemas/lean-packages.ts`).
  (e) Supports `--fixup-branch` mode so after the migration lands on `main`, any
      open PR branch (including newly authored `.lean` files under legacy synonym
      folders such as `QOU/BraidKnot/...`, `QOU/Mass/...`, `QOU/MathlibExt/...`)
      is automatically relocated and import-rewritten to match `main`.

Idempotent and single-threaded CPU-hygiene compliant.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
DEFAULT_MAP_PATH = REPO_ROOT / "docs" / "audits" / "2026-11-24-lean-reservoir-module-map.json"
DEFAULT_QOU_ROOT = REPO_ROOT / "folio" / "quantum-observable-universe"

COMMUNITY_LIBS_ORDERED: tuple[str, ...] = (
    "MathlibExt",
    "QCalculus",
    "TwistedFrobeniusHopf",
    "ToricConicOpt",
    "CompactQuantumMetrics",
    "HeckeTemperleyLieb",
    "BraidKnotOctonion",
)

CANONICAL_QOU_DIRS: frozenset[str] = frozenset({
    "Core",
    "LiftingDescent",
    "BraidsAndKnots",
    "BringsSurface",
    "Confinement",
    "EightfoldWay",
    "MassTheory",
    "Nuclear",
    "StandardModel",
    "FluidDynamics",
    "InformationTheory",
    "Observations",
})

COMMUNITY_LIB_SUMMARIES: dict[str, str] = {
    "MathlibExt": (
        "Tier-A selective `leanprover-community/mathlib4` core PR staging library "
        "(zero `QOU.*` and zero Tier-B imports)."
    ),
    "QCalculus": (
        "Standalone Lean Reservoir library: q-numbers, Gaussian binomials, q-Pochhammer, "
        "Thomae-Jackson q-calculus, Faddeev/quantum dilogarithms, and Habiro rings."
    ),
    "TwistedFrobeniusHopf": (
        "Standalone Lean Reservoir library: Nakayama-twisted Frobenius algebras, "
        "Sweedler H_4 and Taft Hopf algebras, Higman norm map, and ambidextrous adjunctions."
    ),
    "ToricConicOpt": (
        "Standalone Lean Reservoir library: Sturmfels-Thomas toric chambers, Graver test sets, "
        "symmetry-reduced LP/SDP duality certificates, and Farkas/Slater conic optimization."
    ),
    "CompactQuantumMetrics": (
        "Standalone Lean Reservoir library: finite-dimensional Rieffel-Connes compact quantum "
        "metric spaces, Lip-seminorms, Woronowicz O_q(SU(2)), and universal differentials."
    ),
    "HeckeTemperleyLieb": (
        "Standalone Lean Reservoir library: Iwahori-Hecke H_n(q), Temperley-Lieb TL_n(q), "
        "Jones/Markov/Ocneanu traces, Hoefsmit seminormal irreps, and Young/SYT/Schur-Weyl."
    ),
    "BraidKnotOctonion": (
        "Standalone Lean Reservoir library: Artin braid representations, Burau/Krammer/Alexander "
        "invariants, PL knot topology, hyperbolic volume bounds, octonions/G_2, and Bring's curve."
    ),
}

IMPORT_STMT_RE = re.compile(r"^(\s*import\s+)([A-Za-z0-9_'À-ÿ.]+)(.*)$")
TS_REF_RE = re.compile(r"""(\bref\s*:\s*["'])(qou:)([^"']+)(["'])""")


def _load_detangler() -> Any:
    spec = importlib.util.spec_from_file_location(
        "lean_kg_detangler", SCRIPTS_DIR / "lean-kg-detangler.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["lean_kg_detangler"] = mod
    spec.loader.exec_module(mod)
    return mod


def _git_mv_or_move(src: Path, dst: Path, repo_root: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        ["git", "mv", str(src.relative_to(repo_root)), str(dst.relative_to(repo_root))],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        shutil.move(str(src), str(dst))


def _prune_empty_dirs(root_dir: Path, keep_top: frozenset[str] | None = None) -> int:
    removed = 0
    if not root_dir.is_dir():
        return 0
    for dirpath, _dirnames, _filenames in sorted(os.walk(root_dir, topdown=False)):
        p = Path(dirpath)
        if p == root_dir:
            continue
        if keep_top and p.parent == root_dir and p.name in keep_top:
            continue
        try:
            if not any(p.iterdir()):
                p.rmdir()
                removed += 1
        except OSError:
            pass
    return removed


def _rewrite_lean_imports(text: str, mod_map: dict[str, str], dedup: bool = True) -> tuple[str, int]:
    """Rewrite header `import Old.Mod` lines using `mod_map` while preserving comments and body."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    seen_imports: set[str] = set()
    in_block = 0
    in_header = True
    changed = 0

    for ln in lines:
        if not in_header:
            out.append(ln)
            continue
        s = ln.strip()
        if in_block > 0:
            in_block += s.count("/-") - s.count("-/")
            if in_block < 0:
                in_block = 0
            out.append(ln)
            continue
        if s.startswith("/-"):
            delta = s.count("/-") - s.count("-/")
            if delta > 0:
                in_block = delta
            out.append(ln)
            continue
        if not s or s.startswith("--"):
            out.append(ln)
            continue
        m = IMPORT_STMT_RE.match(ln.rstrip("\r\n"))
        if m:
            eol = "\r\n" if ln.endswith("\r\n") else ("\n" if ln.endswith("\n") else "")
            prefix, imp_mod, suffix = m.group(1), m.group(2), m.group(3)
            new_imp = mod_map.get(imp_mod, imp_mod)
            if new_imp != imp_mod:
                changed += 1
            if dedup and new_imp in seen_imports:
                changed += 1
                continue
            seen_imports.add(new_imp)
            out.append(f"{prefix}{new_imp}{suffix}{eol}")
            continue
        in_header = False
        out.append(ln)

    return "".join(out), changed


def _build_decl_index(lean_root: Path, detangler: Any) -> tuple[dict[str, str], dict[str, str | None], set[str]]:
    """Index `full_decl_fqn -> module_name`, unambiguous `short_decl -> module_name`,
    and `basenames` across `lean_root` (post-move paths)."""
    fqn_to_mod: dict[str, str] = {}
    short_to_mod: dict[str, str | None] = {}
    basenames: set[str] = set()

    for p in sorted(lean_root.rglob("*.lean")):
        if ".lake" in p.parts or "blocks-shadow" in p.parts:
            continue
        basenames.add(p.name)
        mod_name = ".".join(p.relative_to(lean_root).with_suffix("").parts)
        if mod_name in ("QOU", *COMMUNITY_LIBS_ORDERED):
            continue
        raw = p.read_text(encoding="utf-8", errors="replace")
        code = detangler.strip_comments_and_strings(raw)
        ns_stack: list[str] = []
        open_kind: list[str] = []
        for raw_ln in code.splitlines():
            t = raw_ln.strip()
            if not t:
                continue
            m_ns = detangler.NS_EVENT_RE.match(raw_ln)
            if m_ns:
                kw, arg = m_ns.group(1), m_ns.group(2)
                if kw == "namespace" and arg:
                    ns_stack.append(arg)
                    open_kind.append("ns")
                elif kw == "section":
                    open_kind.append("sec")
                elif kw == "end":
                    if open_kind and open_kind.pop() == "ns" and ns_stack:
                        ns_stack.pop()
                continue
            m_d = detangler.DECL_KW_RE.match(raw_ln)
            if m_d and m_d.group(2):
                dname = m_d.group(2)
                fqn = ".".join([*ns_stack, dname]) if ns_stack else dname
                fqn_to_mod.setdefault(fqn, mod_name)
                short = dname.split(".")[-1]
                if short not in short_to_mod:
                    short_to_mod[short] = mod_name
                elif short_to_mod[short] != mod_name:
                    short_to_mod[short] = None

    return fqn_to_mod, short_to_mod, basenames


def _rewrite_ts_lean_refs(
    qou_root: Path,
    lean_root: Path,
    mod_map: dict[str, str],
    valid_post_modules: set[str],
    fqn_to_mod: dict[str, str],
    short_to_mod: dict[str, str | None],
    basenames: set[str],
    apply_changes: bool,
) -> int:
    """Rewrite `.ts` `lean.ref` module paths if module-qualified (or if a sibling-less
    block's `lean.ref` lost a retired legacy aggregator path), preserving `qou:<Decl>`."""
    updated_files = 0
    for ts_path in sorted(qou_root.rglob("*.ts")):
        if ts_path.is_relative_to(lean_root) or ".lake" in ts_path.parts:
            continue
        raw_bytes = ts_path.read_bytes()
        if b"ref" not in raw_bytes or b"qou:" not in raw_bytes:
            continue
        txt = raw_bytes.decode("utf-8", errors="replace")
        has_sibling_lean = ts_path.with_suffix(".lean").is_file()

        def _repl(m: re.Match[str]) -> str:
            pre, scheme, decl, post = m.group(1), m.group(2), m.group(3), m.group(4)
            # 1. Exact module ref (`qou:<OldModule>`)
            if decl in mod_map and decl != "QOU":
                return f"{pre}{scheme}{mod_map[decl]}{post}"
            # 2. Longest module-qualified prefix (`qou:<OldModule>.<Suffix>`)
            parts = decl.split(".")
            for i in range(len(parts) - 1, 0, -1):
                cand_mod = ".".join(parts[:i])
                if cand_mod in mod_map and cand_mod != "QOU":
                    new_mod = mod_map[cand_mod]
                    rest = ".".join(parts[i:])
                    return f"{pre}{scheme}{new_mod}.{rest}{post}"
            # 3. Check if already valid under post-migration module paths or basename
            if not has_sibling_lean:
                short_name = parts[-1]
                resolves_post = (
                    decl in valid_post_modules
                    or any(".".join(parts[:i]) in valid_post_modules for i in range(len(parts), 1, -1))
                    or f"{short_name}.lean" in basenames
                )
                if not resolves_post:
                    resolved_mod = fqn_to_mod.get(decl) or short_to_mod.get(short_name)
                    if resolved_mod:
                        return f"{pre}{scheme}{resolved_mod}.{short_name}{post}"
            return m.group(0)

        new_txt = TS_REF_RE.sub(_repl, txt)
        if new_txt != txt:
            updated_files += 1
            if apply_changes:
                ts_path.write_text(new_txt, encoding="utf-8")
    return updated_files


def _update_paper_lakefile(lakefile_path: Path, apply_changes: bool) -> bool:
    """Update `folio/quantum-observable-universe/lean/lakefile.toml` with the 7 + 1 `[[lean_lib]]` targets,
    preserving `doc-gen4` sentinels and `QOUBlocks` generated section verbatim."""
    orig = lakefile_path.read_text(encoding="utf-8")
    if 'name = "HeckeTemperleyLieb"' in orig and 'name = "MathlibExt"' in orig:
        return False

    # Extract everything from `# NOTE: Fred2005` (or first `[[require]]`) to EOF verbatim
    marker = "# NOTE: Fred2005"
    idx = orig.find(marker)
    if idx < 0:
        idx = orig.find("[[require]]")
    assert idx >= 0, f"Unexpected structure in {lakefile_path}"
    tail_verbatim = orig[idx:]

    all_targets = [*COMMUNITY_LIBS_ORDERED, "QOU"]
    targets_toml = ", ".join(f'"{t}"' for t in all_targets)

    header_lines = [
        'name = "qou"',
        f"defaultTargets = [{targets_toml}]",
        "",
        "[leanOptions]",
        "autoImplicit = false",
        "profiler = true          # report per-declaration elaboration times",
        "",
        "################################################################################",
        "# Tier-A (`Mathlib4` Core Staging) & Tier-B (6 Standalone Lean Reservoir Libraries)",
        "#",
        "# Strict zero-`QOU.*` upward import boundary (`BP008`, `community_to_qou_cut_edges == 0`)",
        "# and strict inter-library DAG order (`MathlibExt` -> `QCalculus` -> `TwistedFrobeniusHopf`",
        "# -> `ToricConicOpt` -> `CompactQuantumMetrics` -> `HeckeTemperleyLieb` -> `BraidKnotOctonion`).",
        "# All 7 community libraries share `srcDir = \".\"` (0 extra `.lake/build` roots).",
        "################################################################################",
        "",
    ]
    for lb in COMMUNITY_LIBS_ORDERED:
        header_lines.extend([
            "[[lean_lib]]",
            f'name = "{lb}"',
            'srcDir = "."',
            f'globs = ["{lb}", "{lb}.+"]',
            'moreLeanArgs = ["-s", "65536"]',
            "",
        ])

    header_lines.extend([
        "################################################################################",
        "# Monograph QOU Library (12 Canonical Chapter Subgraphs under `QOU/`)",
        "################################################################################",
        "",
        "[[lean_lib]]",
        'name = "QOU"',
        'srcDir = "."',
        'globs = ["QOU", "QOU.+"]',
        'moreLeanArgs = ["-s", "65536"]',
        "",
    ])

    new_txt = "\n".join(header_lines) + tail_verbatim
    if apply_changes:
        lakefile_path.write_text(new_txt, encoding="utf-8")
    return True


def _write_community_root_lean_files(lean_root: Path, apply_changes: bool) -> int:
    written = 0
    for lb in COMMUNITY_LIBS_ORDERED:
        root_f = lean_root / f"{lb}.lean"
        if root_f.is_file():
            continue
        written += 1
        if apply_changes:
            content = (
                "/- Copyright (c) 2026 Quantum Observable Universe Contributors. "
                "Released under Apache 2.0 license. -/\n\n"
                f"/-!\n# `{lb}` — Root Module\n\n"
                f"{COMMUNITY_LIB_SUMMARIES[lb]}\n\n"
                "Individual modules are built via `globs = "
                f'["{lb}", "{lb}.+"]` in `lakefile.toml`; import targeted '
                f"`{lb}.<Module>` submodules directly rather than this root.\n-/\n\n"
                "set_option autoImplicit false\n"
            )
            root_f.write_text(content, encoding="utf-8")
    return written


def _discover_unmapped_legacy_files_for_fixup(
    lean_root: Path,
    base_mod_map: dict[str, str],
    detangler: Any,
) -> dict[str, dict[str, str]]:
    """Find any `.lean` files under legacy `lean/QOU/<NonCanonical>/...` or loose `lean/QOU/*.lean`
    on an open PR branch and compute collision-free target paths."""
    qou_dir = lean_root / "QOU"
    if not qou_dir.is_dir():
        return {}

    existing_new_mods: set[str] = set(base_mod_map.values())
    for p in lean_root.rglob("*.lean"):
        if ".lake" not in p.parts and "blocks-shadow" not in p.parts:
            existing_new_mods.add(".".join(p.relative_to(lean_root).with_suffix("").parts))

    comm_rank = {lb: idx for idx, lb in enumerate(COMMUNITY_LIBS_ORDERED)}
    extra_moves: dict[str, dict[str, str]] = {}

    legacy_candidates: list[Path] = []
    for p in sorted(qou_dir.rglob("*.lean")):
        rel_qou = p.relative_to(qou_dir)
        if len(rel_qou.parts) == 1:
            # Loose `QOU/<File>.lean`
            legacy_candidates.append(p)
        elif rel_qou.parts[0] not in CANONICAL_QOU_DIRS:
            legacy_candidates.append(p)

    for p in legacy_candidates:
        old_mod = ".".join(p.relative_to(lean_root).with_suffix("").parts)
        if old_mod in base_mod_map:
            new_mod = base_mod_map[old_mod]
            extra_moves[old_mod] = {
                "old_module": old_mod,
                "new_module": new_mod,
                "src_abs": str(p),
                "dst_abs": str(lean_root / (new_mod.replace(".", "/") + ".lean")),
            }
            continue

        # Brand-new file added on the open PR branch under a legacy directory!
        raw = p.read_text(encoding="utf-8", errors="replace")
        imps, _, _, _ = detangler.parse_header_imports_and_doc_order(raw)
        code = detangler.strip_comments_and_strings(raw)
        rel_lean = p.relative_to(lean_root)
        subdir = "<QOU-root-loose>" if len(rel_lean.parts) == 2 else rel_lean.parts[1]

        pur, _ = detangler.classify_intrinsic_purity(code, old_mod, raw)
        sor_tot, _ = detangler.count_sorries_by_kind(code)
        ax_cnt = sum(1 for mk in detangler.DECL_KW_RE.finditer(code) if mk.group(1) == "axiom")
        has_nd = bool(detangler.NATIVE_DECIDE_CHECK_RE.search(code))
        has_flt = bool(detangler.FLOAT_CHECK_RE.search(code))

        rewritten_local_imps = [
            base_mod_map.get(i, extra_moves.get(i, {}).get("new_module", i))
            for i in imps
            if i.startswith("QOU.") or any(i.startswith(f"{lb}.") for lb in COMMUNITY_LIBS_ORDERED)
        ]
        all_deps_in_comm = all(
            imp.split(".", 1)[0] in comm_rank for imp in rewritten_local_imps
        )

        target_prefix: str | None = None
        if pur == "pure_math" and sor_tot == 0 and ax_cnt == 0 and not has_nd and not has_flt and all_deps_in_comm:
            cand_part = detangler.classify_pure_math_target(old_mod, subdir, code)
            if cand_part in detangler.PARTITION_TO_LEAN_LIB:
                seed_lb = detangler.PARTITION_TO_LEAN_LIB[cand_part]
                r = comm_rank[seed_lb]
                for imp in rewritten_local_imps:
                    top_lb = imp.split(".", 1)[0]
                    if top_lb in comm_rank:
                        r = max(r, comm_rank[top_lb])
                target_prefix = COMMUNITY_LIBS_ORDERED[r]

        if target_prefix is None:
            if subdir == "<QOU-root-loose>":
                target_prefix = detangler.classify_loose_qou_module(old_mod)
            else:
                target_prefix = detangler.SUBDIR_TO_CANONICAL_QOU.get(subdir, "QOU.Core")

        mparts = old_mod.split(".")
        subtail = ".".join(mparts[2:]) if len(mparts) >= 3 else mparts[1]
        cand_new = f"{target_prefix}.{subtail}"
        if cand_new in existing_new_mods:
            orig_tag = "Root" if subdir == "<QOU-root-loose>" else subdir
            cand_new = f"{target_prefix}.{orig_tag}.{subtail}"
            idx_s = 2
            while cand_new in existing_new_mods:
                cand_new = f"{target_prefix}.{orig_tag}.{subtail}_{idx_s}"
                idx_s += 1
        existing_new_mods.add(cand_new)
        extra_moves[old_mod] = {
            "old_module": old_mod,
            "new_module": cand_new,
            "src_abs": str(p),
            "dst_abs": str(lean_root / (cand_new.replace(".", "/") + ".lean")),
        }

    return extra_moves


def verify_post_migration(qou_root: Path, detangler: Any) -> int:
    lean_root = qou_root / "lean"
    qou_dir = lean_root / "QOU"
    errors: list[str] = []

    # 1. Verify QOU/ contains ONLY the 12 canonical subdirectories and 0 loose .lean files
    if qou_dir.is_dir():
        for entry in sorted(qou_dir.iterdir()):
            if entry.is_file() and entry.suffix == ".lean":
                errors.append(f"Loose file remaining under QOU/: {entry.relative_to(REPO_ROOT)}")
            elif entry.is_dir() and entry.name not in CANONICAL_QOU_DIRS:
                errors.append(f"Non-canonical directory remaining under QOU/: QOU/{entry.name}/")

    # 2. Run detangler on post-migration layout and assert 0 cut-edges, 0 dangling, 0 cycles
    audit = detangler.analyze_corpus(qou_root)
    pg = audit["process_gate_status"]
    tb = audit["tier_a_and_tier_b_reservoir_packages"]
    dag = audit["dag_and_scc_analysis"]

    if pg["GW_Detangled"]["unresolved_dangling_imports"] != 0:
        errors.append(
            f"Unresolved dangling imports: {pg['GW_Detangled']['unresolved_dangling_imports']} "
            f"({dag['unresolved_imports'][:10]})"
        )
    if tb["community_to_qou_cut_edges_count"] != 0:
        errors.append(f"Community -> QOU cut-edges: {tb['community_to_qou_cut_edges_count']}")
    if tb["community_inter_package_scc_cycles"]:
        errors.append(f"Inter-community package SCC cycles: {tb['community_inter_package_scc_cycles']}")
    if dag["module_level_scc_cycles"]:
        errors.append(f"Module-level SCC cycles: {dag['module_level_scc_cycles']}")

    # 3. Check sibling .lean imports resolve to existing modules
    valid_local_mods = {
        ".".join(p.relative_to(lean_root).with_suffix("").parts)
        for p in lean_root.rglob("*.lean")
        if ".lake" not in p.parts and "blocks-shadow" not in p.parts
    }
    local_prefixes = ("QOU.", *(f"{lb}." for lb in COMMUNITY_LIBS_ORDERED))
    local_roots = {"QOU", *COMMUNITY_LIBS_ORDERED}
    for sib in sorted((REPO_ROOT / "folio").rglob("*.lean")):
        if "/lean/" in sib.as_posix() or ".lake" in sib.parts:
            continue
        raw = sib.read_text(encoding="utf-8", errors="replace")
        imps, _, _, _ = detangler.parse_header_imports_and_doc_order(raw)
        for imp in imps:
            if (imp in local_roots or imp.startswith(local_prefixes)) and imp not in valid_local_mods:
                errors.append(f"Dangling sibling import in {sib.relative_to(REPO_ROOT)}: {imp}")

    if errors:
        print(f"apply-lean-reservoir-migration --verify: FAILED ({len(errors)} error(s)):", file=sys.stderr)
        for e in errors[:40]:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(
        "apply-lean-reservoir-migration --verify: PASS "
        "(0 dangling imports, 0 community->QOU cut-edges, 0 inter-package cycles, "
        "12 canonical QOU/* subdirs, 0 loose QOU/*.lean files)"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--map", type=Path, default=DEFAULT_MAP_PATH, help="Path to module migration JSON map")
    ap.add_argument("--qou-root", type=Path, default=DEFAULT_QOU_ROOT, help="Path to folio/quantum-observable-universe")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Preview migration without writing changes (default)")
    mode.add_argument("--apply", action="store_true", help="Execute full Option 1 migration on this branch")
    mode.add_argument(
        "--fixup-branch",
        action="store_true",
        help="Fix up an open PR branch after Option 1 landed on main (moves legacy/new QOU/<OldDir> files & rewrites imports/refs)",
    )
    mode.add_argument("--verify", action="store_true", help="Verify post-migration layout invariants")
    args = ap.parse_args(argv)

    detangler = _load_detangler()
    qou_root = args.qou_root.resolve()
    lean_root = qou_root / "lean"

    if args.verify:
        return verify_post_migration(qou_root, detangler)

    if not args.map.is_file():
        print(f"Migration map not found at {args.map}; generate via `lean-kg-detangler.py --map-out`.", file=sys.stderr)
        return 2

    payload = json.loads(args.map.read_text(encoding="utf-8"))
    entries: dict[str, dict[str, str]] = payload["modules"]
    mod_map: dict[str, str] = {old_m: info["new_module"] for old_m, info in entries.items()}

    # Assert bijection across map entries
    if len(set(mod_map.values())) != len(mod_map):
        print("FATAL: non-bijective new_module entries in migration map!", file=sys.stderr)
        return 2

    apply_changes = bool(args.apply or args.fixup_branch)
    moved_files = 0

    if args.fixup_branch:
        extra = _discover_unmapped_legacy_files_for_fixup(lean_root, mod_map, detangler)
        for old_m, info in sorted(extra.items()):
            mod_map[old_m] = info["new_module"]
            src_p = Path(info["src_abs"])
            dst_p = Path(info["dst_abs"])
            if src_p.is_file() and src_p != dst_p:
                moved_files += 1
                if apply_changes:
                    _git_mv_or_move(src_p, dst_p, REPO_ROOT)
    else:
        for _old_m, info in sorted(entries.items()):
            src_p = REPO_ROOT / info["old_repo_rel_path"]
            dst_p = lean_root / info["new_lean_rel_path"]
            if src_p.is_file() and src_p.resolve() != dst_p.resolve():
                moved_files += 1
                if apply_changes:
                    _git_mv_or_move(src_p, dst_p, REPO_ROOT)

    pruned_dirs = 0
    if apply_changes:
        pruned_dirs = _prune_empty_dirs(lean_root / "QOU", keep_top=CANONICAL_QOU_DIRS)

    root_files_written = _write_community_root_lean_files(lean_root, apply_changes=apply_changes)
    lakefile_updated = _update_paper_lakefile(lean_root / "lakefile.toml", apply_changes=apply_changes)

    # Rewrite imports across all .lean files under folio/ (library + content-block siblings)
    lean_files_rewritten = 0
    import_lines_rewritten = 0
    folio_dir = REPO_ROOT / "folio"
    for lf in sorted(folio_dir.rglob("*.lean")):
        if ".lake" in lf.parts or "blocks-shadow" in lf.parts:
            continue
        orig_txt = lf.read_text(encoding="utf-8", errors="replace")
        new_txt, cnt = _rewrite_lean_imports(orig_txt, mod_map, dedup=True)
        if cnt > 0 and new_txt != orig_txt:
            lean_files_rewritten += 1
            import_lines_rewritten += cnt
            if apply_changes:
                lf.write_text(new_txt, encoding="utf-8")

    # Build post-move declaration/module sets for `.ts` `lean.ref` updates
    if apply_changes:
        fqn_to_mod, short_to_mod, basenames = _build_decl_index(lean_root, detangler)
        valid_post_modules = {
            ".".join(p.relative_to(lean_root).with_suffix("").parts)
            for p in lean_root.rglob("*.lean")
            if ".lake" not in p.parts and "blocks-shadow" not in p.parts
        }
    else:
        fqn_to_mod, short_to_mod, basenames = {}, {}, set()
        valid_post_modules = set(mod_map.values()) | {"QOU", *COMMUNITY_LIBS_ORDERED}

    ts_files_rewritten = _rewrite_ts_lean_refs(
        qou_root=qou_root,
        lean_root=lean_root,
        mod_map=mod_map,
        valid_post_modules=valid_post_modules,
        fqn_to_mod=fqn_to_mod,
        short_to_mod=short_to_mod,
        basenames=basenames,
        apply_changes=apply_changes,
    )

    mode_name = "APPLY" if args.apply else ("FIXUP-BRANCH" if args.fixup_branch else "DRY-RUN")
    print(f"apply-lean-reservoir-migration [{mode_name}]:")
    print(f"  mapped modules in table     : {len(mod_map)}")
    print(f"  .lean files moved           : {moved_files}")
    print(f"  empty legacy dirs pruned    : {pruned_dirs}")
    print(f"  community <Lib>.lean roots  : {root_files_written}")
    print(f"  paper lakefile.toml updated : {lakefile_updated}")
    print(f"  .lean files import-rewritten: {lean_files_rewritten} ({import_lines_rewritten} import lines)")
    print(f"  .ts lean.ref files updated  : {ts_files_rewritten}")

    if args.apply or args.fixup_branch:
        return verify_post_migration(qou_root, detangler)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
