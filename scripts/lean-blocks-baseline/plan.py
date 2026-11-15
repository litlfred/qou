#!/usr/bin/env python3
"""L3 plan: which library modules are stale vs the restored cache, decided by
Lake's own source-content hash recorded in each .trace (not by mtime/commit time).

Writes plan.json: {lib_modules: {mod: {src, own_stale, reason, imports}},
                   dirty_closure: [...], targets: [...], build_order: [...]}
"""
import json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path("/home/user/qou")
HERE = Path(__file__).resolve().parent
S = Path(os.environ.get("L3_WORK", "/tmp/lean-blocks-baseline"))  # plan.json, mirror/, logs/
S.mkdir(parents=True, exist_ok=True)
PKGS = [("folio/quantum-observable-universe/lean", "QOU"),
        ("folio/unital-groebner-bases/lean", "UGB"),
        ("folio/fred2005-formal-groups/lean", "Fred2005")]
IMPORT_RE = re.compile(r"^\s*(?:public\s+|private\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z0-9_.«»']+)")


def imports_of(p: Path):
    """Header-only: imports precede every command; comments may be interleaved."""
    out = []
    try:
        txt = p.read_text(errors="replace")
    except FileNotFoundError:
        return out
    i, n = 0, len(txt)
    depth = 0
    while i < n:
        if depth:
            if txt.startswith("/-", i):
                depth += 1; i += 2
            elif txt.startswith("-/", i):
                depth -= 1; i += 2
            else:
                i += 1
            continue
        if txt[i].isspace():
            i += 1; continue
        if txt.startswith("/-", i):
            depth = 1; i += 2; continue
        if txt.startswith("--", i):
            j = txt.find("\n", i); i = n if j < 0 else j + 1; continue
        j = txt.find("\n", i); line = txt[i:(n if j < 0 else j)]
        m = IMPORT_RE.match(line)
        if m:
            out.append(m.group(1))
            # several imports may share a line: `import A B`
            rest = line[m.end():].split("--")[0].split()
            out.extend(r for r in rest if r != "import")
        elif line.strip() in ("module", "prelude"):
            pass
        else:
            break
        i = n if j < 0 else j + 1
    return out


def main():
    lib = {}
    for rel, name in PKGS:
        pkg = ROOT / rel
        srcs = [pkg / f"{name}.lean"] + sorted((pkg / name).rglob("*.lean"))
        for src in srcs:
            if not src.exists():
                continue
            mod = ".".join(src.relative_to(pkg).with_suffix("").parts)
            olean = pkg / ".lake/build/lib/lean" / src.relative_to(pkg).with_suffix(".olean")
            trace = olean.with_suffix(".trace")
            lib[mod] = {"src": str(src.relative_to(ROOT)), "pkg": rel,
                        "olean": str(olean), "trace": str(trace),
                        "imports": imports_of(src)}
    # hashes via Lake's own Hash.ofText
    paths = [str(ROOT / v["src"]) for v in lib.values()]
    hashes = {}
    B = 400
    for i in range(0, len(paths), B):
        r = subprocess.run(["lean", "--run", str(HERE / "lake-text-hash.lean")] + paths[i:i + B],
                           capture_output=True, text=True, check=True)
        for line in r.stdout.splitlines():
            h, p = line.split("\t", 1)
            hashes[p] = h
    for mod, v in lib.items():
        cur = hashes[str(ROOT / v["src"])]
        v["cur_hash"] = cur
        if not Path(v["olean"]).exists():
            v["own_stale"], v["reason"] = True, "no-olean"
            continue
        if not Path(v["trace"]).exists():
            v["own_stale"], v["reason"] = True, "no-trace"
            continue
        d = json.load(open(v["trace"]))
        th = None
        for ent in d.get("inputs", []):
            if isinstance(ent, list) and len(ent) == 2 and isinstance(ent[0], str) and ent[0].endswith(".lean"):
                th = ent[1]
        v["trace_hash"] = th
        if th is None:
            v["own_stale"], v["reason"] = True, "trace-no-src-hash"
        elif th != cur:
            v["own_stale"], v["reason"] = True, "source-changed"
        else:
            v["own_stale"], v["reason"] = False, "fresh"
    # dirty closure
    rev = {m: [] for m in lib}
    for m, v in lib.items():
        for i in v["imports"]:
            if i in rev:
                rev[i].append(m)
    dirty = set(m for m, v in lib.items() if v["own_stale"])
    stack = list(dirty)
    while stack:
        m = stack.pop()
        for c in rev[m]:
            if c not in dirty:
                dirty.add(c)
                stack.append(c)
    # targets
    lst = subprocess.run(["python3", "scripts/gen-lean-blocks-shadow.py", "--list"], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    targets = []
    for line in lst.splitlines():
        libname, mod, src = line.split("\t")
        targets.append({"lib": libname, "module": mod, "src": src,
                        "imports": imports_of(ROOT / src)})
    # union cone of targets within library
    need = set()
    stack = [i for t in targets for i in t["imports"] if i in lib]
    while stack:
        m = stack.pop()
        if m in need:
            continue
        need.add(m)
        stack.extend(i for i in lib[m]["imports"] if i in lib)
    to_build = dirty & need
    # topo order
    order, seen = [], set()
    def visit(m):
        if m in seen:
            return
        seen.add(m)
        for i in lib[m]["imports"]:
            if i in to_build:
                visit(i)
        order.append(m)
    sys.setrecursionlimit(100000)
    for m in sorted(to_build):
        visit(m)
    from collections import Counter
    print("library modules", len(lib))
    print("own-stale reasons", Counter(v["reason"] for v in lib.values()))
    print("dirty closure", len(dirty))
    print("targets", len(targets), Counter(t["lib"] for t in targets))
    print("library cone of targets", len(need))
    print("to build (dirty ∩ cone)", len(to_build))
    json.dump({"lib": lib, "dirty": sorted(dirty), "need": sorted(need),
               "build_order": order, "targets": targets}, open(S / "plan.json", "w"), indent=1)


if __name__ == "__main__":
    main()
