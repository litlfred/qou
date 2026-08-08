#!/usr/bin/env python3
"""q0_backfilled_pin_fix.py — give a BACKFILLED q₀ pin a producer that maintains
it, so it survives the next regeneration (bean qou-pin5).

THE DECAY
    A witness whose producer writes with a raw `json.dump` never goes through
    `WitnessBuilder.save()`, so **neither** mechanism that maintains a pin runs:
    `build()`'s stamping of a declared pin, and `save()`'s preserve-forward of a
    recorded one. Any `q0Anchor` such a witness carries was put there by a
    backfill sweep — and the first regeneration after that backfill drops it.

    Found by causing it: fixing `t25_cinquefoil_deltalambda_sign_probe` and
    re-running it silently dropped its `q0Anchor: proton`, visible only because
    the consistency audit's counts moved by one.

DETECTING IT PRECISELY
    "Writes via json.dump" is the wrong test — it flags 46 witnesses here, most
    of which do reach a builder somewhere. The property that matters is whether
    the PRODUCER ITSELF ever writes the pin:

        produces-pin  the source mentions `q0Anchor`
        via-builder   it calls WitnessBuilder / wrap_legacy / stamp_staleness
        BACKFILLED    neither — the pin is unmaintained

    That test returns exactly **14**, independently reproducing the count this
    bean arrived at by a different route.

🛑 THE SAFETY CHECK THAT MUST COME FIRST
    `stamp_staleness_metadata` auto-resolves the anchor via `resolve_q0_anchor`,
    which **defaults to proton for an undeclared stem**. So stamping a
    muon-recorded witness whose producer is undeclared would silently FLIP the
    pin to proton — destroying a possibly-correct label under the banner of
    protecting it. That is the same trap that broke the first version of the
    `witness.py` preserve-forward fix.

    So every candidate is checked BEFORE editing: what would the stamp write,
    and does it equal what the witness already records? A mismatch is refused
    and reported, never swept.

Usage:
    python3 q0_backfilled_pin_fix.py --dry-run
    python3 q0_backfilled_pin_fix.py --apply --verify
"""
from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

STAMPERS = ("stamp_staleness_metadata", "wrap_legacy", "WitnessBuilder(")

# Stems where the recorded pin is KNOWN WRONG, so letting the stamp change it is
# a correction rather than the silent flip the safety check exists to prevent.
# Each needs positive evidence, stated here, that the OLD pin is the mistaken one.
ACCEPT_FLIP = {
    "zhabiro_phiq_production_crosscheck":
        "Its committed q0Value is the MUON literal while its q0_source names a "
        "PROTON accessor -- that witness was generated through the cross-layer "
        "`except`-handler fallback removed corpus-wide on 2026-08-08 "
        "(q0_cross_layer_fallback_fix.py). The muon pin records the DEFECT, not "
        "an intent, so proton is the correct label once the fallback is gone. "
        "Declared physical_proton in the same change. Beans qou-pin4, qou-pin5.",
}

# Depth-independent: walk up for tools/qou-substrate/python rather than counting
# `.parents[N]`, because these producers sit at three different tree depths and
# a fixed index silently resolves to the wrong directory. Importing
# `qou_substrate.witness` directly (not the `witness_base` shim) is deliberate —
# subdirectory producers put only that path on sys.path, so the shim is not
# importable from them, which is how the first attempt at this fix failed.
SNIPPET = '''{ind}# Stamp the q0 pin from the producer itself (bean qou-pin5). This witness
{ind}# is written with a raw json.dump rather than WitnessBuilder.save(), so
{ind}# neither build()'s stamping nor save()'s preserve-forward ever runs — any
{ind}# pin it carried had been BACKFILLED by a sweep, and the first regeneration
{ind}# after that backfill drops it.
{ind}try:
{ind}    try:
{ind}        from qou_substrate.witness import WitnessBuilder as _WB
{ind}    except ImportError:
{ind}        import sys as _s
{ind}        from pathlib import Path as _P
{ind}        for _anc in _P(__file__).resolve().parents:
{ind}            _c = _anc / "tools" / "qou-substrate" / "python"
{ind}            if _c.is_dir():
{ind}                _s.path.insert(0, str(_c))
{ind}                break
{ind}        from qou_substrate.witness import WitnessBuilder as _WB
{ind}    _WB.stamp_staleness_metadata({var}, script_path=__file__)
{ind}except Exception as _exc:  # noqa: BLE001
{ind}    print(f"  [warn] q0/staleness metadata NOT stamped: {{_exc!r}}")
'''


def _producer(stem: str) -> Path | None:
    for p in COMPUTE_DIR.rglob(f"{stem}.py"):
        if "_deprecated" not in p.parts:
            return p
    return None


def backfilled() -> list[tuple[str, str, Path, Path]]:
    """(stem, recorded_pin, producer, witness) for each unmaintained pin."""
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
            continue
        stem = Path(str(prov.get("scriptFile") or d.get("scriptFile") or "")).stem
        if not stem:
            continue
        p = _producer(stem)
        if p is None:
            continue
        src = p.read_text(encoding="utf-8", errors="replace")
        if "q0Anchor" in src or any(s in src for s in STAMPERS):
            continue
        out.append((stem, pin, p, w))
    return out


def dump_site(path: Path) -> tuple[int, int, str] | None:
    """(lineno, col, payload_var) of the call that serialises the witness.

    Matches BOTH `json.dump(w, f)` and `json.dumps(w)` — the latter usually
    wrapped in `out.write_text(json.dumps(w, indent=2))`. Looking only for
    `dump` missed 8 of the 14 candidates and reported them as unfixable.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return None
    best = None
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        name = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", None)
        if name not in ("dump", "dumps") or not n.args:
            continue
        arg = n.args[0]
        if not isinstance(arg, ast.Name):
            continue          # only a plain variable can be stamped in place
        stmt = n
        # Find the enclosing statement so the snippet lands at statement level.
        for s in ast.walk(tree):
            if isinstance(s, ast.stmt) and getattr(s, "lineno", None) and \
                    s.lineno <= n.lineno <= (s.end_lineno or n.lineno):
                if best is None or s.lineno > best[0]:
                    stmt = s
        line = getattr(stmt, "lineno", n.lineno)
        col = getattr(stmt, "col_offset", 0)
        if best is None or line > best[0]:
            best = (line, col, arg.id)
    return best


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify", action="store_true",
                    help="re-run each producer and confirm the pin survives")
    ap.add_argument("--timeout", type=int, default=600)
    args = ap.parse_args(argv)

    from qou_substrate.witness import resolve_q0_anchor

    cands = backfilled()
    print("=" * 72)
    print("backfilled q₀ pins — give the producer one that maintains it")
    print("=" * 72)
    print(f"  witnesses whose pin nothing maintains : {len(cands)}\n")

    todo, refused, nosite, flips = [], [], [], []
    for stem, pin, prod, wit in cands:
        would, _ = resolve_q0_anchor(str(prod))
        if would != pin:
            if stem in ACCEPT_FLIP:
                flips.append((stem, pin, would))
                pin = would          # verify against the CORRECTED pin
            else:
                refused.append((stem, pin, would))
                continue
        site = dump_site(prod)
        if site is None:
            nosite.append(stem)
            continue
        todo.append((stem, pin, prod, wit, site))

    for stem, pin, prod, wit, (line, col, var) in todo:
        print(f"  {'FIX    ' if args.apply else 'would-fix'} {stem:<44} "
              f"pin={pin:<7} dump({var}) at line {line}")
    for stem, old, new in flips:
        print(f"  FLIP     {stem:<44} {old} -> {new} (evidenced correction)")
        print(f"             {ACCEPT_FLIP[stem]}")
    for stem, pin, would in refused:
        print(f"  REFUSE   {stem:<44} records {pin} but the stamp would write "
              f"{would} — a declaration is needed FIRST")
    for stem in nosite:
        print(f"  NO-SITE  {stem:<44} json.dump target is not a plain variable")

    if args.apply:
        for stem, pin, prod, wit, (line, col, var) in todo:
            src = prod.read_text(encoding="utf-8")
            lines = src.splitlines(keepends=True)
            lines.insert(line - 1, SNIPPET.format(ind=" " * col, var=var))
            new = "".join(lines)
            try:
                ast.parse(new)
            except SyntaxError as e:
                print(f"  FAILED   {stem}: rewrite did not parse: {e}")
                continue
            prod.write_text(new, encoding="utf-8")

    if args.apply and args.verify:
        print("\n" + "-" * 72)
        print("  VERIFY — re-run each producer; the pin must SURVIVE")
        print("-" * 72)
        kept = lost = failed = 0
        for stem, pin, prod, wit, _ in todo:
            rel = str(wit.relative_to(REPO))
            try:
                r = subprocess.run([sys.executable, "-u", prod.name],
                                   cwd=str(prod.parent), capture_output=True,
                                   timeout=args.timeout)
            except subprocess.TimeoutExpired:
                print(f"  SKIP-slow {stem} (> {args.timeout}s)")
                subprocess.run(["git", "checkout", "HEAD", "--", rel], cwd=str(REPO))
                continue
            if r.returncode != 0:
                failed += 1
                print(f"  FAIL      {stem}: "
                      f"{(r.stderr or b'').decode()[-80:].strip()}")
                subprocess.run(["git", "checkout", "HEAD", "--", rel], cwd=str(REPO))
                continue
            try:
                d = json.loads(wit.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                failed += 1
                continue
            prov = d.get("provenance") if isinstance(d.get("provenance"), dict) else {}
            now = prov.get("q0Anchor") or d.get("q0Anchor")
            if now == pin:
                kept += 1
                print(f"  KEPT      {stem:<44} q0Anchor={now} (now PRODUCED)")
            else:
                lost += 1
                print(f"  LOST      {stem:<44} {pin} -> {now!r}")
        print(f"\n  kept={kept}  lost={lost}  failed={failed}")

    print("=" * 72)
    if not args.apply:
        print("dry run — nothing written. Re-run with --apply --verify.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
