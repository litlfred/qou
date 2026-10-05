#!/usr/bin/env python3
"""L3 run: rebuild the stale library cone into the hardlink mirror, then
lean-direct every target. Never calls lake. Results streamed to results.jsonl."""
import json, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path("/home/user/qou")
S = Path(os.environ.get("L3_WORK", "/tmp/lean-blocks-baseline"))  # must match plan.py
M = S / "mirror"
OPTS = ["-DautoImplicit=false", "-s", "65536"]
plan = json.load(open(S / "plan.json"))
lib = plan["lib"]
ENV = dict(os.environ, LEAN_PATH=str(M))
LIBROOTS = ("QOU", "UGB", "Fred2005")
LOGD = S / "logs"; LOGD.mkdir(exist_ok=True)
out = open(S / "results.jsonl", "a")
lock = threading.Lock()
T0 = time.time()


def emit(rec):
    with lock:
        out.write(json.dumps(rec) + "\n"); out.flush()
        print(f"[{time.time()-T0:7.0f}s] {rec['phase']:6} {rec['verdict']:28} {rec['module']}", flush=True)


def olean_of(mod):
    return M / (mod.replace(".", "/") + ".olean")


def first_error(text):
    for line in text.splitlines():
        if ": error" in line or line.startswith("error"):
            return line.strip()[:400]
    lines = [l for l in text.splitlines() if l.strip()]
    return (lines[0][:400] if lines else "")


def check_imports(imports, failed):
    """Return (verdict, detail) if the target cannot be meaningfully compiled."""
    for i in imports:
        if i in lib:
            if i in failed:
                return "skipped-red-dependency", i
            if not olean_of(i).exists():
                return "skipped-missing-qou-olean", i
        elif i.split(".")[0] in LIBROOTS:
            return "red-import-of-nonexistent-module", i
        elif not olean_of(i).exists():
            return "skipped-missing-mathlib-olean", i
    return None


def run_lean(args, cwd, log, timeout):
    t = time.time()
    try:
        r = subprocess.run(["lean", *OPTS, *args], cwd=cwd, env=ENV, capture_output=True,
                           text=True, timeout=timeout)
        txt, rc = r.stdout + r.stderr, r.returncode
    except subprocess.TimeoutExpired as e:
        txt, rc = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or ""), 124
    Path(log).write_text(txt)
    return rc, txt, time.time() - t


def build_phase():
    order = plan["build_order"]
    failed = set()
    done = {}
    events = {m: threading.Event() for m in order}

    def work(m):
        v = lib[m]
        for i in v["imports"]:
            if i in events:
                events[i].wait()
        bad = check_imports(v["imports"], failed)
        if bad:
            failed.add(m)
            emit({"phase": "build", "module": m, "src": v["src"], "verdict": bad[0], "detail": bad[1]})
            events[m].set(); return
        pkg = ROOT / v["pkg"]
        rel = Path(v["src"]).relative_to(v["pkg"])
        ol = olean_of(m); il = ol.with_suffix(".ilean")
        ol.parent.mkdir(parents=True, exist_ok=True)
        for f in (ol, il, ol.with_suffix(".trace")):
            if f.exists() or f.is_symlink():
                f.unlink()          # never write through a shared hardlink inode
        rc, txt, dt = run_lean(["-o", str(ol), "-i", str(il), str(rel)], pkg,
                               LOGD / ("build_" + m + ".log"), 3600)
        verdict = "green" if rc == 0 else ("timeout" if rc == 124 else "red")
        if rc != 0:
            failed.add(m)
            for f in (ol, il):
                if f.exists(): f.unlink()
        emit({"phase": "build", "module": m, "src": v["src"], "verdict": verdict, "exit": rc,
              "secs": round(dt, 1), "first_error": first_error(txt) if rc else ""})
        events[m].set()

    with ThreadPoolExecutor(3) as ex:
        list(ex.map(work, order))
    return failed


def target_phase(failed):
    def work(t):
        bad = check_imports(t["imports"], failed)
        if bad:
            emit({"phase": "target", "lib": t["lib"], "module": t["module"], "src": t["src"],
                  "verdict": bad[0], "detail": bad[1]})
            return
        rc, txt, dt = run_lean([t["src"]], ROOT, LOGD / ("t_" + t["lib"] + "_" + t["module"] + ".log"), 1800)
        verdict = "green" if rc == 0 else ("timeout" if rc == 124 else "red")
        emit({"phase": "target", "lib": t["lib"], "module": t["module"], "src": t["src"],
              "verdict": verdict, "exit": rc, "secs": round(dt, 1),
              "n_errors": txt.count(": error"), "first_error": first_error(txt) if rc else ""})
    with ThreadPoolExecutor(3) as ex:
        list(ex.map(work, plan["targets"]))


if __name__ == "__main__":
    failed = build_phase()
    print(f"BUILD DONE failed={len(failed)}", flush=True)
    target_phase(failed)
    print(f"ALL DONE {time.time()-T0:.0f}s", flush=True)
