"""Exact count of tautological witness assertions: computed and expected are
the SAME expression, so the assertion holds by construction."""
import ast, pathlib, sys, json

roots = [pathlib.Path("computations"), pathlib.Path("scripts"), pathlib.Path("tools")]
files, parsed, failed = [], 0, 0
for r in roots:
    if r.exists(): files += list(r.rglob("*.py"))

taut, total_calls, by_file = [], 0, {}
for p in files:
    if "_deprecated" in p.parts: continue
    try:
        tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
        parsed += 1
    except Exception:
        failed += 1
        continue
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call): continue
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else None)
        if name != "add_assertion": continue
        total_calls += 1
        kw = {k.arg: k.value for k in node.keywords if k.arg}
        c, e = kw.get("computed"), kw.get("expected")
        if c is None or e is None:
            # positional form — compare 2nd and 3rd positional args if present
            if len(node.args) >= 3: c, e = node.args[1], node.args[2]
            else: continue
        if ast.dump(c) == ast.dump(e):
            taut.append((str(p), node.lineno, ast.unparse(c)[:60]))
            by_file[str(p)] = by_file.get(str(p), 0) + 1

print(f"files parsed {parsed} (unparseable {failed}); add_assertion calls {total_calls}")
print(f"TAUTOLOGICAL: {len(taut)}  ({100*len(taut)/max(total_calls,1):.1f}% of all assertions)")
print(f"across {len(by_file)} files\n")
print("top files:")
for f, n in sorted(by_file.items(), key=lambda x: -x[1])[:10]:
    print(f"  {n:3d}  {f}")
json.dump({"taut": taut, "total": total_calls}, open("/tmp/claude-0/-home-user-folio-assistant/02d2d727-2de1-54e7-abb4-e7c363854add/scratchpad/taut.json","w"))
