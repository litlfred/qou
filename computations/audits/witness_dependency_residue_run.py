#!/usr/bin/env python3
"""qou-wlaf residue campaign, attempt 2.

Attempt 1 was discarded: it called a witness MOVED that a flattened leaf
comparison showed had 0 differing fields, and its own comparison run
STANDALONE on the same pair returned equal. So the divergence lived in the
loop, not the comparison logic. Two changes:

  1. flattened LEAF comparison (the method verified against a known case),
     and it RECORDS WHICH FIELDS MOVED so a mask gap is re-classifiable from
     the checkpoint instead of costing another full sweep.
  2. an IN-LOOP self-test: the first iteration runs a producer known not to
     move and aborts unless the loop reports it IDENTICAL. Standalone
     validation is precisely what failed to catch attempt 1.
"""
import json, os, subprocess, sys, time
from pathlib import Path
from collections import Counter

ROOT = Path("/home/user/qou"); COMP = ROOT / "computations"
T = json.load(open("/tmp/residue_targets.json")); SHA = T["sha"]
# targets were collected against /home/user/qou; remap onto the worktree so the
# sweep can never touch the session's tree (the reason attempt 2 was stopped)
# RUN THIS IN A `git worktree`, never in the session tree: an earlier attempt
# dirtied it, transiently including witness-raw-float64-audit.witness.json —
# the audit witness commit b28296c0d already had to revert once for being
# swept in. Remap the collected absolute paths onto the worktree root.
_WT = os.environ.get("RESIDUE_WORKTREE")
if _WT:
    ROOT = Path(_WT); COMP = ROOT / "computations"
    T["witnesses"] = [[w.replace("/home/user/qou", _WT), s] for w, s in T["witnesses"]]
SELFTEST = "atom_braid_active_partitions"   # verified IDENTICAL by hand
VOL = {"timestamp","elapsed_seconds","measured_at","start_time_monotonic","computedAt",
       "durationMs","elapsed_sec","invocation","environment","scriptCommitSha",
       "commitSha","wall_sec","generated_at","runtime_seconds","engineVersion",
       "pyhecke_native_build","hostname","platform","python_version"}

def leaves(o, p=""):
    if isinstance(o, dict):
        for k, v in o.items():
            # "elapsed" anywhere is timing: the suffix list missed
            # elapsed_reduce_sec / elapsed_trace_sec, which end _sec but not
            # _elapsed_sec. A bare _sec suffix would be broader than needed and
            # could mask a real field, so key on the word instead.
            if (k in VOL or "elapsed" in k
                    or any(k.endswith(x) for x in
                           ('_seconds','_runtime','_wall_sec'))):
                continue
            yield from leaves(v, f"{p}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from leaves(v, f"{p}[{i}]")
    else:
        yield p, o

def restore():
    """Restore producer-written artifacts — and NEVER source.

    This ran `git checkout -- computations/` followed by an unrestricted
    `git clean -fd computations/`.  This script lives under that tree, so its
    own end-of-run restore reverted any uncommitted source edit AND deleted
    any newly-written untracked `.py` beneath it.  That is the qou-jtc6
    defect, one harness over: there it cost a fix that was written, tested
    green, and gone from disk before `git add` ran, leaving a commit carrying
    the message but not the change.

    The blanket form is NOT simply wrong — it defends against the opposite
    failure (a producer emits SIBLING witnesses, so restoring only the diffed
    file leaks a drifted witness; the tnjb corruption).  Excluding `.py`
    keeps that defence intact, because producers write data artifacts and
    never source.
    """
    out = subprocess.run(["git", "diff", "--name-only", "--", "computations/"],
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
    targets = [f for f in out if not f.endswith(".py")]
    if targets:
        subprocess.run(["git", "checkout", "--", *targets],
                       cwd=ROOT, capture_output=True)
    subprocess.run(["git", "clean", "-fdq", "-e", "*.py", "computations/"],
                   cwd=ROOT, capture_output=True)

def baseline(rel):
    r = subprocess.run(["git","show",f"{SHA}:{rel}"],cwd=ROOT,capture_output=True,text=True)
    if r.returncode != 0: return None
    try: return json.loads(r.stdout)
    except Exception: return None

prod = {}
for w, s in T["witnesses"]: prod.setdefault(s, []).append(w)
# PYTHONPATH must include the producer SUBDIRECTORIES, not just computations/.
# Producers are run from their own directory and import siblings by bare name
# (`char_fast`, `markov_peel`), which live in computations/substrate/ and
# computations/markov/. With only computations/ on the path they raise
# ModuleNotFoundError and get recorded as CRASH — a verdict about the harness,
# not the producer. AGENTS.md documents this exact misclassification.
_SUBDIRS = [COMP] + [d for d in sorted(COMP.iterdir())
                     if d.is_dir() and not d.name.startswith((".", "_"))]
env = dict(os.environ)
env["PYTHONPATH"] = ":".join(str(d) for d in _SUBDIRS) + ":" + env.get("PYTHONPATH", "")
BUDGET = int(sys.argv[1]) if len(sys.argv) > 1 else 240

def run_one(stem, ws):
    src = next((p for p in COMP.rglob(f"{stem}.py")), None)
    if src is None: return {"producer":stem,"verdict":"NO_SOURCE"}
    restore()
    t = time.time(); tb = False; rc = None; guard = False
    try:
        r = subprocess.run([sys.executable,"-u",str(src)],cwd=src.parent,env=env,
                           capture_output=True,text=True,timeout=BUDGET)
        rc = r.returncode; both = (r.stdout or "") + (r.stderr or "")
        tb = "Traceback (most recent call last)" in both
        # keep the exception line: a traceback is NOT proof of a defect. A guard
        # implemented as a raised domain exception is indistinguishable from a
        # crash by shape, and the discriminator is the exception TYPE and its
        # message. Without this, classifying a CRASH means re-running it.
        exc = [ln for ln in both.splitlines()
               if ln and ln[0].isalpha() and ("Error" in ln.split(":")[0]
                                              or "Exception" in ln.split(":")[0]
                                              or "Invalid" in ln.split(":")[0])]
        exc_line = exc[-1][:300] if exc else ""
        guard = any(k in both for k in ("Refusing","refuse","would publish","precision would"))
    except subprocess.TimeoutExpired: rc = "TIMEOUT"; exc_line = ""
    except Exception as e: rc = f"ERR:{type(e).__name__}"
    dt = time.time() - t
    moved, ident, fields = [], [], {}
    if rc != "TIMEOUT" and not tb:
        for w in ws:
            rel = str(Path(w).relative_to(ROOT))
            b = baseline(rel)
            if b is None: continue
            try: n = json.loads(Path(w).read_text())
            except Exception: continue
            lb, ln = dict(leaves(b)), dict(leaves(n))
            d = sorted(k for k in set(lb) | set(ln) if lb.get(k) != ln.get(k))
            if d: moved.append(rel); fields[rel] = d[:12]
            else: ident.append(rel)
    v = ("TIMEOUT" if rc=="TIMEOUT" else "GUARD_REFUSAL" if (guard and not tb)
         else "CRASH" if tb else "MOVED" if moved else "IDENTICAL")
    return {"producer":stem,"verdict":v,"rc":rc,"sec":round(dt,1),
            "moved":moved,"identical":len(ident),"fields":fields,
            "exception": locals().get("exc_line","")}

# ---- IN-LOOP SELF-TEST ----
print(f"PINNED {SHA}", flush=True)
st = run_one(SELFTEST, prod.get(SELFTEST, []))
print(f"SELFTEST {SELFTEST}: {st['verdict']} (expect IDENTICAL)", flush=True)
if st["verdict"] != "IDENTICAL":
    print("ABORT: the loop misclassifies a known-unmoved witness.")
    print("  fields it thinks moved:", json.dumps(st.get("fields"), indent=1)[:1500])
    restore(); sys.exit(2)
print("selftest passed — verdicts are trustworthy\n", flush=True)

# RESUME: containers get reprovisioned mid-sweep (three times this session),
# so a run that cannot resume loses everything each reset. Load prior verdicts
# and skip those producers; a TIMEOUT is NOT kept, since it says nothing about
# the witness and deserves a fresh attempt.
prior, done = [], set()
try:
    _p = json.load(open("/tmp/residue_results3.json"))["results"]
    # A producer that times out TWICE is not a budget artifact any more — it is
    # reproducibly slower than the budget. Retrying it on every resume costs the
    # full budget each cycle (3 x 180 s here) and can never terminate, so record
    # it as BUDGET_EXCEEDED and stop. Still excluded from the scoreable
    # denominator: it says nothing about whether the witness moved.
    for r in _p:
        if r.get("verdict") == "TIMEOUT":
            r["timeout_count"] = r.get("timeout_count", 0) + 1
            if r["timeout_count"] >= 2:
                r["verdict"] = "BUDGET_EXCEEDED"
    # carry the count forward: run_one returns a FRESH record with no
    # timeout_count, so without this the count resets to 0 on every retry and
    # BUDGET_EXCEEDED is never reached
    prior_timeouts = {r["producer"]: r.get("timeout_count", 0)
                      for r in _p if r.get("verdict") in ("TIMEOUT", "BUDGET_EXCEEDED")}
    prior = [r for r in _p
             if r.get("verdict") not in ("TIMEOUT", None)]
    done = {r["producer"] for r in prior}
    print(f"RESUME: {len(prior)} prior verdicts kept, {len(_p)-len(prior)} timeouts retried",
          flush=True)
except Exception:
    prior_timeouts = {}
if "prior_timeouts" not in dir():
    prior_timeouts = {}

results = prior + [st] if st["producer"] not in done else list(prior)
todo = [(s,w) for s,w in sorted(prod.items()) if s != SELFTEST and s not in done]
# TWO-TIER PASS. The runner is serial and container resets here cut it short,
# so a single slow producer at the full budget can consume an entire container
# lifetime and the queue barely advances. Tier 1 runs everything at a small
# budget to clear the many fast producers; anything exceeding it is DEFERRED —
# explicitly NOT a verdict — and retried at the full budget in tier 2.
#
# This does NOT create the mixed-budget inconsistency that simply lowering the
# budget would: a producer is only ever given a verdict by a run that completed
# within the budget it was given, and BUDGET_EXCEEDED is still reached only at
# the FULL budget, never the tier-1 one.
TIER1 = 25
deferred = []
for i,(stem,ws) in enumerate(todo,1):
    _full = BUDGET
    BUDGET = TIER1
    r = run_one(stem, ws)
    BUDGET = _full
    if r.get("verdict") == "TIMEOUT":
        deferred.append((stem, ws))
        print(f"[{i}/{len(todo)}] {stem:<48s} DEFERRED (>{TIER1}s)", flush=True)
        continue
    results.append(r)
    print(f"[{i}/{len(todo)}] {stem:<48s} {r['verdict']:<14s} {r['sec']:6.1f}s "
          f"moved={len(r.get('moved',[]))}", flush=True)
    json.dump({"sha":SHA,"results":results},open("/tmp/residue_results3.json","w"),indent=1)

print(f"\ntier 1 done: {len(deferred)} deferred to the full {BUDGET}s budget\n", flush=True)
_ndef = len(deferred)
for i,(stem,ws) in enumerate(deferred,1):
    r = run_one(stem, ws)
    if r.get("verdict") == "TIMEOUT":
        r["timeout_count"] = prior_timeouts.get(stem, 0) + 1
        if r["timeout_count"] >= 2:
            r["verdict"] = "BUDGET_EXCEEDED"
    results.append(r)
    print(f"[tier2 {i}/{_ndef}] {stem:<44s} {r['verdict']:<14s} {r['sec']:6.1f}s moved={len(r.get('moved',[]))}",flush=True)
    json.dump({"sha":SHA,"results":results},open("/tmp/residue_results3.json","w"),indent=1)
restore()
print("\n=== SUMMARY ==="); print(f"pinned {SHA}")
for k,v in Counter(x["verdict"] for x in results).most_common(): print(f"  {k:<16s} {v}")

# SENTINEL_EDIT
