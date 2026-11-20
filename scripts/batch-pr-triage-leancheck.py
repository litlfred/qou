#!/usr/bin/env python3
"""lean-direct verification of batch-PR Lean files against the shared restored
cache, read-only. Freshness = Lake's own source hash in each .trace (not mtime).
Stale QOU/UGB modules in the union cone are rebuilt into a private shadow
(first on LEAN_PATH); PR files are compiled in a per-PR overlay.
usage: leancheck.py plan|build|check <triage.json> [--prs N,N,...]"""
import json, os, re, subprocess, sys, pathlib, collections, time, shutil
from concurrent.futures import ThreadPoolExecutor
ROOT = pathlib.Path("/home/claude/qou")
W = pathlib.Path("/home/claude/wt/w4-cache/lean")
SHADOW = pathlib.Path(os.environ.get("W4_SHADOW", "/tmp/w4-shadow"))
PKGS = {"QOU": ROOT/"folio/quantum-observable-universe/lean",
        "UGB": ROOT/"folio/unital-groebner-bases/lean",
        "Fred2005": ROOT/"folio/fred2005-formal-groups/lean"}
OPTS = ["-DautoImplicit=false", "-s", "65536"]
IMP = re.compile(r"^\s*import\s+(.+)$")

def env():
    out = subprocess.run(["bash", "-c", f"source {ROOT}/scripts/lean-direct-env.sh >/dev/null; echo $PATH; echo $LEAN_PATH"],
                         capture_output=True, text=True).stdout.split("\n")
    return out[0], out[1]
PATH, RLP = env()

def imports_txt(txt):
    out = []
    code = re.sub(r"/-.*?-/", "", txt, flags=re.S)
    for line in code.splitlines():
        s = line.split("--")[0].strip()
        if not s: continue
        m = IMP.match(s)
        if m: out += m.group(1).split()
        elif s in ("prelude", "module"): continue
        else: break
    return out

def src_of(mod):
    top = mod.split(".")[0]
    if top not in PKGS: return None
    p = PKGS[top]/(mod.replace(".", "/") + ".lean")
    return p if p.exists() else None

def olean_dir(mod):
    return PKGS[mod.split(".")[0]]/".lake/build/lib/lean"

def trace_hash(mod):
    t = olean_dir(mod)/(mod.replace(".", "/") + ".trace")
    if not t.exists() or not t.with_suffix(".olean").exists(): return None
    def walk(x):
        if isinstance(x, list):
            if len(x) == 2 and isinstance(x[0], str) and x[0].endswith(".lean") and isinstance(x[1], str):
                yield x[1]
            for y in x: yield from walk(y)
    try:
        h = list(walk(json.loads(t.read_text())["inputs"]))
    except Exception:
        return None
    return h[0] if h else None

def text_hashes(paths):
    res = {}
    paths = list(paths)
    for i in range(0, len(paths), 400):
        r = subprocess.run(["lean", "--run", str(ROOT/"scripts/lean-blocks-baseline/lake-text-hash.lean"), *map(str, paths[i:i+400])],
                           capture_output=True, text=True, env={**os.environ, "PATH": PATH, "LEAN_PATH": RLP})
        for line in r.stdout.splitlines():
            h, p = line.split("\t", 1); res[p] = h
    return res

def cone(roots):
    seen, order, stack = set(), [], []
    def visit(m):
        if m in seen: return
        seen.add(m)
        p = src_of(m)
        if p is None: return
        for d in imports_txt(p.read_text(errors="replace")): visit(d)
        order.append(m)
    sys.setrecursionlimit(100000)
    for r in roots: visit(r)
    return order  # topo order (deps first), QOU/UGB/Fred only

def pr_files(n):
    sc = json.load(open("/home/claude/wt/w4-cache/scan.json"))[str(n)]["lean_files"]
    out = {}
    for fn, x in sc.items():
        if x.get("identical_on_main") or fn.endswith("/QOU.lean"): continue
        txt = subprocess.run(["git", "-C", str(ROOT), "show", f"refs/remotes/pr/{n}:{fn}"], capture_output=True, text=True).stdout
        out[fn] = txt
    return out

def mod_of(fn):
    m = re.search(r"/lean/((?:QOU|UGB|Fred2005)/.*)\.lean$", fn)
    return m.group(1).replace("/", ".") if m else None

def plan(prs):
    roots, per = set(), {}
    for n in prs:
        fs = pr_files(n); per[n] = fs
        prmods = {mod_of(f) for f in fs}
        for f, t in fs.items():
            for d in imports_txt(t):
                if d not in prmods: roots.add(d)
    order = cone(roots)
    hs = text_hashes([src_of(m) for m in order])
    stale = set()
    for m in order:
        cur = hs.get(str(src_of(m)))
        own = trace_hash(m) != cur or cur is None
        dep = any(d in stale for d in imports_txt(src_of(m).read_text(errors="replace")))
        if own or dep: stale.add(m)
    build = [m for m in order if m in stale]
    json.dump({"prs": prs, "cone": order, "build": build}, open(W/"plan.json", "w"))
    print(f"cone {len(order)}  stale-to-build {len(build)}")
    return build

def lp(extra=()):
    return ":".join([*map(str, extra), str(SHADOW), RLP])

def compile_to(src, mod, outdir, extra=(), timeout=1800, srcpath=None):
    o = outdir/(mod.replace(".", "/") + ".olean"); o.parent.mkdir(parents=True, exist_ok=True)
    il = o.with_suffix(".ilean")
    for f in (o, il, o.with_suffix(".trace")):   # NEVER write through a hardlink into the shared cache
        if f.exists() or f.is_symlink(): f.unlink()
    t0 = time.time()
    try:
        r = subprocess.run(["lean", *OPTS, "-o", str(o), "-i", str(il), str(srcpath or src)], capture_output=True, text=True,
                           timeout=timeout, cwd=str(ROOT), env={**os.environ, "PATH": PATH, "LEAN_PATH": lp(extra)})
        rc, out = r.returncode, r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        rc, out = 124, "TIMEOUT"
    return rc, out, time.time() - t0

def build():
    p = json.load(open(W/"plan.json")); todo = p["build"]
    SHADOW.mkdir(parents=True, exist_ok=True)
    done, failed = set(), {}
    log = open(W/"build.log", "a")
    deps = {m: [d for d in imports_txt(src_of(m).read_text(errors="replace")) if d in set(todo)] for m in todo}
    t0 = time.time(); remaining = list(todo)
    with ThreadPoolExecutor(2) as ex:
        while remaining:
            ready = [m for m in remaining if all(d in done or d in failed for d in deps[m])]
            if not ready: break
            batch = ready[:8]
            for m in batch: remaining.remove(m)
            def work(m):
                if any(d in failed for d in deps[m]): return m, 99, "blocked", 0
                return (m, *compile_to(src_of(m), m, SHADOW))
            for m, rc, out, dt in ex.map(work, batch):
                (done.add(m) if rc == 0 else failed.__setitem__(m, out[-600:]))
                print(f"[{len(done)+len(failed)}/{len(todo)} {time.time()-t0:.0f}s] {m} rc={rc} {dt:.0f}s", file=log, flush=True)
    json.dump({"done": sorted(done), "failed": failed}, open(W/"build.json", "w"), indent=1)
    print(f"built {len(done)} failed {len(failed)}")

def fqn_decls(txt, names):
    """map decl short name -> FQN using namespace/end tracking"""
    ns, out = [], {}
    code = re.sub(r"/-.*?-/", lambda m: "\n" * m.group(0).count("\n"), txt, flags=re.S)
    for line in code.splitlines():
        s = line.split("--")[0].strip()
        m = re.match(r"namespace\s+(\S+)", s)
        if m: ns.append(m.group(1)); continue
        m = re.match(r"end\s+(\S+)", s)
        if m and ns and ns[-1] == m.group(1): ns.pop(); continue
        m = re.match(r"(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma)\s+([^\s:({\[]+)", s)
        if m and m.group(2) in names and not s.startswith("private"):
            out[m.group(2)] = ".".join([*ns, m.group(2)]) if not m.group(2).startswith("_root_.") else m.group(2)[7:]
    return out

def check(prs):
    res = json.load(open(W/"check.json")) if (W/"check.json").exists() else {}
    sc = json.load(open("/home/claude/wt/w4-cache/scan.json"))
    for n in prs:
        fs = pr_files(n); ov = pathlib.Path(f"/tmp/w4-pr/{n}")
        shutil.rmtree(ov, ignore_errors=True); ov.mkdir(parents=True)
        backups = []
        mods = {mod_of(f): (f, t) for f, t in fs.items()}
        order, seen = [], set()
        def visit(m):
            if m in seen or m not in mods: return
            seen.add(m)
            for d in imports_txt(mods[m][1]): visit(d)
            order.append(m)
        for m in mods: visit(m)
        r = {"files": {}, "status": "pass"}
        for m in order:
            f, t = mods[m]
            names = [d["name"] for d in sc[str(n)]["lean_files"][f]["decls"] if d["kind"] in ("theorem", "lemma")]
            fq = fqn_decls(t, set(names))
            tmp = ov/"src"/(m.replace(".", "/") + ".lean"); tmp.parent.mkdir(parents=True, exist_ok=True)
            tmp.write_text(t)
            base = SHADOW/(m.replace(".", "/"))
            for ext in (".olean", ".ilean"):
                b = base.with_name(base.name + ext)
                if b.exists():
                    bk = ov/"bak"/(m.replace(".", "/") + ext); bk.parent.mkdir(parents=True, exist_ok=True)
                    os.rename(b, bk); backups.append((bk, b))
                else:
                    backups.append((None, b))
            rc, out, dt = compile_to(tmp, m, SHADOW, srcpath=tmp)
            ent = {"rc": rc, "secs": round(dt), "errors": [l for l in out.splitlines() if "error" in l][:8]}
            if rc == 0 and fq:
                ax = ov/"ax.lean"
                ax.write_text(f"import {m}\n" + "\n".join(f"#print axioms {q}" for q in fq.values()) + "\n")
                r2 = subprocess.run(["lean", *OPTS, str(ax)], capture_output=True, text=True, cwd=str(ROOT),
                                    env={**os.environ, "PATH": PATH, "LEAN_PATH": lp()}, timeout=600)
                axo = r2.stdout + r2.stderr
                ent["axioms_rc"] = r2.returncode
                ent["sorryAx"] = axo.count("sorryAx")
                ent["nonstd_axioms"] = sorted(set(re.findall(r"\b(?!propext\b|Classical\.choice\b|Quot\.sound\b)([A-Za-z_][\w.]*)\b", " ".join(re.findall(r"\[([^\]]*)\]", axo)))))
                ent["n_axiom_checked"] = len(fq)
            r["files"][f] = ent
            if rc != 0: r["status"] = "fail"
            elif ent.get("sorryAx") or ent.get("nonstd_axioms"): r["status"] = "fail"
        for bk, b in reversed(backups):   # restore the shadow to its pre-PR state
            if b.exists(): b.unlink()
            if bk is not None: os.rename(bk, b)
        res[str(n)] = r
        json.dump(res, open(W/"check.json", "w"), indent=1)
        print(n, r["status"], {k.split('/')[-1]: (v["rc"], v.get("sorryAx"), v.get("nonstd_axioms")) for k, v in r["files"].items()}, flush=True)
        shutil.rmtree(ov/"src", ignore_errors=True)

def run(prs):
    """For each PR in ascending order of stale-module need: build the missing
    stale modules of its cone into the shadow, then check the PR."""
    need = json.load(open(W/"need.json"))
    built = set((W/"built.txt").read_text().split()) if (W/"built.txt").exists() else set()
    bad = {}
    order = json.load(open(W/"plan.json"))["build"]
    pos = {m: i for i, m in enumerate(order)}
    log = open(W/"build.log", "a")
    for n in sorted(prs, key=lambda n: len(need[str(n)])):
        todo = sorted([m for m in need[str(n)] if m not in built], key=pos.get)
        blocked = [m for m in need[str(n)] if m in bad]
        for m in todo:
            if any(d in bad for d in imports_txt(src_of(m).read_text(errors="replace"))):
                bad[m] = "blocked"; continue
            rc, out, dt = compile_to(src_of(m), m, SHADOW)
            print(f"[pr {n}] {m} rc={rc} {dt:.0f}s", file=log, flush=True)
            if rc == 0:
                built.add(m); (W/"built.txt").write_text("\n".join(sorted(built)))
            else:
                bad[m] = out[-800:]
        miss = [m for m in need[str(n)] if m in bad]
        if miss:
            res = json.load(open(W/"check.json")) if (W/"check.json").exists() else {}
            res[str(n)] = {"status": "blocked", "reason": "main module(s) in cone fail to build: " + ",".join(miss[:5])}
            json.dump(res, open(W/"check.json", "w"), indent=1)
            print(n, "blocked", miss[:3], flush=True)
            continue
        check([n])
    json.dump(bad, open(W/"bad.json", "w"), indent=1)


if __name__ == "__main__":
    stage = sys.argv[1]
    prs = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else []
    {"plan": lambda: plan(prs), "build": build, "check": lambda: check(prs), "run": lambda: run(prs)}[stage]()
