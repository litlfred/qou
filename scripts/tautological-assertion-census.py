"""Exact count of tautological witness assertions: computed and expected are
the SAME expression, so the assertion holds by construction.

Test fixtures are counted **separately**, not silently dropped. A file like
`tools/qou-substrate/tests/test_declared_tolerance_literal.py` exists to feed
`computed="1", expected="1"` to the code under test — there the shape is the
point, and `drain-tautological-assertions.py` already refuses to rewrite it
(its `EXCLUDE`, learned by mangling that file). Folding them into one headline
made the corpus figure overstate the backlog by whatever the fixtures happen
to hold; reporting both keeps the number meaning what it says without hiding
anything.

    python3 scripts/tautological-assertion-census.py [--json PATH]
"""
import argparse
import ast
import json
import pathlib

# Same exclusion as `drain-tautological-assertions.py`, deliberately kept
# identical: a site the drain will never rewrite should not sit in the count
# that the drain's progress is measured against.
EXCLUDE = ("/tests/", "/test_", "conftest", "/fixtures/")


def is_fixture(path: str) -> bool:
    p = path.replace("\\", "/")
    return any(tok in p for tok in EXCLUDE)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", metavar="PATH",
                    help="also write the full site list here")
    args = ap.parse_args()

    roots = [pathlib.Path("computations"), pathlib.Path("scripts"),
             pathlib.Path("tools")]
    files, parsed, failed = [], 0, 0
    for r in roots:
        if r.exists():
            files += list(r.rglob("*.py"))

    taut, fixture_taut, total_calls, by_file = [], [], 0, {}
    for p in files:
        if "_deprecated" in p.parts:
            continue
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
            parsed += 1
        except Exception:
            failed += 1
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            name = (fn.attr if isinstance(fn, ast.Attribute)
                    else (fn.id if isinstance(fn, ast.Name) else None))
            if name != "add_assertion":
                continue
            total_calls += 1
            kw = {k.arg: k.value for k in node.keywords if k.arg}
            c, e = kw.get("computed"), kw.get("expected")
            if c is None or e is None:
                # positional form — compare 2nd and 3rd positional args
                if len(node.args) >= 3:
                    c, e = node.args[1], node.args[2]
                else:
                    continue
            if ast.dump(c) == ast.dump(e):
                site = (str(p), node.lineno, ast.unparse(c)[:60])
                if is_fixture(str(p)):
                    fixture_taut.append(site)
                else:
                    taut.append(site)
                    by_file[str(p)] = by_file.get(str(p), 0) + 1

    print(f"files parsed {parsed} (unparseable {failed}); "
          f"add_assertion calls {total_calls}")
    print(f"TAUTOLOGICAL: {len(taut)}  "
          f"({100 * len(taut) / max(total_calls, 1):.1f}% of all assertions)")
    print(f"across {len(by_file)} files")
    print(f"  (+ {len(fixture_taut)} in test fixtures, excluded — the shape is "
          f"deliberate there and the drain tool will not rewrite them)\n")
    print("top files:")
    for f, n in sorted(by_file.items(), key=lambda x: -x[1])[:10]:
        print(f"  {n:3d}  {f}")

    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(
            {"taut": taut, "fixture_taut": fixture_taut,
             "total": total_calls}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
