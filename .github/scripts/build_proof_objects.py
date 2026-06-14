#!/usr/bin/env python3
"""Content-object-driven proof-objects.json generator (default lake/lean infra).

Supersedes the LaTeX-driven extract_proof_objects.py + update_proof_status.py
for the per-block content world. Status truth = the standard `lake build QOU`
output (warnings: "declaration uses 'sorry'", and "error:" lines); blocks are
keyed by content-block label and joined to the built library via `lean.ref`.

Two Lean layers exist (see docs/audits/2026-06-14-lean-two-layer-drift-triage.md):
  * library  — content/<paper>/lean/QOU/**.lean, compiled by `lake build QOU`
  * sibling  — content/<paper>/<chapter>/<block>.lean, NOT in any lean_lib

A block's Lean is taken from the library when its `lean.ref` resolves to a
built decl; otherwise from the colocated sibling.

Usage:
    python .github/scripts/build_proof_objects.py \
        [--paper content/quantum-observable-universe] \
        [--build-log /tmp/qou-build.log]   # lake build QOU 2>&1 output
        [--build-ok | --build-failed] \
        [--output proof-objects.json] \
        [--drift-output proof-objects-drift.json]

Without --build-log the status falls back to a static decl-span `sorry`
scan (no compile-error awareness); with it, status is build-verified.
"""
import argparse, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
SORRY = re.compile(r"(?<![A-Za-z_])sorry(?![A-Za-z_0-9-])")
DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+|scoped\s+)*"
    r"(theorem|lemma|def|abbrev|structure|class|instance|inductive)\s+([A-Za-z_][\w'\.]*)"
)
PREFIX = {"def:": "definition", "thm:": "theorem", "lem:": "lemma",
          "prop:": "proposition", "cor:": "corollary", "conj:": "conjecture",
          "rem:": "remark", "ex:": "example", "sim:": "simulator"}
PROVABLE = {"theorem", "lemma", "proposition", "corollary"}
NON_FORMALIZABLE = {"prose", "equation", "diagram", "simulator", "unknown"}


def strip_bc(t):
    return re.sub(r"/-.*?-/", "", t, flags=re.S)


def code(line):
    i = line.find("--")
    return line if i < 0 else line[:i]


# ----------------------------------------------------------------------------
# 1. library decl index (the thing `lake build QOU` compiles)
# ----------------------------------------------------------------------------
def build_lib_index(libdir):
    by_full, by_leaf, files = {}, {}, {}
    for lf in libdir.rglob("*.lean"):
        rel = str(lf.relative_to(REPO))
        lines = lf.read_text(encoding="utf-8", errors="ignore").splitlines()
        ns, decls = [], []
        for i, l in enumerate(lines):
            m_ns = re.match(r"\s*namespace\s+([\w.]+)", l)
            m_en = re.match(r"\s*end\s+([\w.]+)", l)
            if m_ns:
                ns.append(m_ns.group(1)); continue
            if m_en and ns:
                ns.pop(); continue
            md = DECL.match(l)
            if md:
                leaf = md.group(2)
                full = ".".join(ns) + "." + leaf if ns else leaf
                decls.append([full, leaf, i])
        for j, (full, leaf, si) in enumerate(decls):
            end = decls[j + 1][2] if j + 1 < len(decls) else len(lines)
            chunk = "\n".join(code(x) for x in lines[si:end])
            static_sorry = bool(SORRY.search(strip_bc(chunk)))
            rec = {"full": full, "leaf": leaf, "file": rel,
                   "start": si + 1, "end": end, "static_sorry": static_sorry,
                   "log_sorry": False, "log_error": False}
            by_full.setdefault(full, rec)
            by_leaf.setdefault(leaf, []).append(rec)
        files[rel] = lf
    return by_full, by_leaf, files


def resolve_ref(ref, by_full, by_leaf):
    if not ref:
        return ("no-ref", None)
    target = ref.split(":", 1)[1] if ":" in ref else ref
    leaf = target.split(".")[-1]
    if target in by_full:
        return ("exact", by_full[target])
    if leaf in by_leaf:
        return ("leaf", by_leaf[leaf][0])
    alt = re.sub(r"(?<!^)(?=[A-Z])", "_", leaf).lower()
    if alt in by_leaf:
        return ("leaf~", by_leaf[alt][0])
    return ("missing", None)


# ----------------------------------------------------------------------------
# 2. parse the default `lake build QOU` log → sorry / error locations
# ----------------------------------------------------------------------------
def parse_build_log(text, files):
    # normalize a logged path to a repo-relative indexed path by suffix match
    tails = {}
    for rel in files:
        tails.setdefault(os.path.basename(rel), []).append(rel)

    def norm(p):
        base = os.path.basename(p)
        cands = tails.get(base, [])
        if len(cands) == 1:
            return cands[0]
        for c in cands:
            if p.replace("./", "").endswith(c) or c.endswith(p.replace("./", "")):
                return c
        return cands[0] if cands else None

    sorry_loc, error_loc = set(), set()
    for m in re.finditer(r"(\S+\.lean):(\d+):\d+:\s*warning:\s*declaration uses 'sorry'", text):
        r = norm(m.group(1))
        if r:
            sorry_loc.add((r, int(m.group(2))))
    for m in re.finditer(r"(\S+\.lean):(\d+):\d+:\s*error:", text):
        r = norm(m.group(1))
        if r:
            error_loc.add((r, int(m.group(2))))
    return sorry_loc, error_loc


def apply_log_to_index(by_full, sorry_loc, error_loc):
    # mark a decl if a sorry/error line falls within its [start,end) span
    per_file = {}
    for rec in by_full.values():
        per_file.setdefault(rec["file"], []).append(rec)
    for (f, ln) in sorry_loc:
        for rec in per_file.get(f, []):
            if rec["start"] <= ln < rec["end"] + 1:
                rec["log_sorry"] = True
    for (f, ln) in error_loc:
        for rec in per_file.get(f, []):
            if rec["start"] <= ln < rec["end"] + 1:
                rec["log_error"] = True


# ----------------------------------------------------------------------------
# 3. content-block manifest
# ----------------------------------------------------------------------------
def block_kind(txt, label):
    m = re.search(r"^\s*(definition|theorem|lemma|proposition|corollary|conjecture|"
                  r"remark|prose|example|simulator|equation|diagram)\s*\(", txt, re.M)
    if m:
        return m.group(1)
    for p, k in PREFIX.items():
        if label.startswith(p):
            return k
    return "unknown"


def walk_blocks(paper):
    blocks = []
    for ch in sorted(os.listdir(paper)):
        chd = paper / ch
        if not chd.is_dir() or ch == "lean":
            continue
        for ts in sorted(chd.glob("*.ts")):
            name = ts.stem
            if name == ch:
                continue
            txt = ts.read_text(encoding="utf-8", errors="ignore")
            lab = re.search(r"label\s*:\s*[\"']([^\"']+)[\"']", txt)
            if not lab:
                continue
            label = lab.group(1)
            ref = re.search(r"ref\s*:\s*[\"']([^\"']+)[\"']", txt)
            title = re.search(r"title\s*:\s*[\"'](.+?)[\"']\s*,", txt)
            uses = re.findall(r"[\"']((?:def|thm|lem|prop|cor|conj|rem):[\w-]+)[\"']", txt)
            sib = ts.with_suffix(".lean")
            blocks.append({
                "ch": ch, "name": name, "label": label,
                "kind": block_kind(txt, label),
                "ref": ref.group(1) if ref else None,
                "title": title.group(1).strip() if title else "",
                "uses": sorted(set(uses)),
                "sibling": str(sib.relative_to(REPO)) if sib.exists() else None,
            })
    return blocks


def sibling_sorry(relpath):
    body = (REPO / relpath).read_text(encoding="utf-8", errors="ignore")
    return bool(SORRY.search(strip_bc("\n".join(code(l) for l in body.splitlines()))))


# ----------------------------------------------------------------------------
# 4. status computation
# ----------------------------------------------------------------------------
def status_for(block, rec, have_log):
    kind = block["kind"]
    if kind in NON_FORMALIZABLE:
        return "n/a", "none", None
    is_def = kind == "definition"
    if rec is not None:  # library
        if rec["log_error"]:
            return "error", "library", False
        sor = rec["log_sorry"] if have_log else rec["static_sorry"]
        if sor:
            return "has_sorry", "library", False
        return ("stated" if is_def else "proved"), "library", True
    if block["sibling"]:  # sibling-only
        sor = sibling_sorry(block["sibling"])
        if sor:
            return "has_sorry", "sibling", False
        return ("stated" if is_def else "stated"), "sibling", True
    return "not_started", "none", False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", default="content/quantum-observable-universe")
    ap.add_argument("--build-log", type=Path, default=None)
    ap.add_argument("--build-ok", action="store_true")
    ap.add_argument("--build-failed", action="store_true")
    ap.add_argument("--output", type=Path, default=REPO / "proof-objects.json")
    ap.add_argument("--drift-output", type=Path, default=REPO / "proof-objects-drift.json")
    args = ap.parse_args()

    paper = REPO / args.paper
    libdir = paper / "lean" / "QOU"
    by_full, by_leaf, files = build_lib_index(libdir)

    have_log = False
    if args.build_log and args.build_log.exists():
        text = args.build_log.read_text(encoding="utf-8", errors="ignore")
        sloc, eloc = parse_build_log(text, files)
        apply_log_to_index(by_full, sloc, eloc)
        have_log = True
        print(f"build log: {len(sloc)} sorry-warnings, {len(eloc)} error-lines")
    else:
        print("no build log — static decl-span sorry scan (not build-verified)")

    blocks = walk_blocks(paper)
    objects, drift = [], {"library_missing_ref": [], "stale_sibling": [],
                          "unreferenced_library_decls": [], "genuinely_unformalized": []}
    referenced = set()
    from collections import Counter, defaultdict
    qstat = Counter(); sstat = Counter()
    kind_status = defaultdict(Counter)

    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO).decode().strip()
    except Exception:
        commit = None
    branch = os.environ.get("GIT_BRANCH")
    if not branch:
        try:
            branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=REPO).decode().strip()
        except Exception:
            branch = "main"

    for b in blocks:
        q, rec = resolve_ref(b["ref"], by_full, by_leaf)
        qstat[q] += 1
        if rec:
            referenced.add(rec["full"])
        status, source, sorry_free = status_for(b, rec, have_log)
        sstat[status] += 1
        kind_status[b["kind"]][status] += 1
        obj = {
            "label": b["label"], "object_type": b["kind"], "chapter": b["ch"],
            "title": b["title"], "source": source,
            "formalization_status": status,
        }
        if b["ref"]:
            lean = {"ref": b["ref"], "resolution": q, "sorry_free": sorry_free}
            if rec:
                lean["decl"] = rec["full"]
                lean["file"] = rec["file"]
                lean["github_source_url"] = (
                    f"https://github.com/litlfred/qou/blob/{branch}/{rec['file']}")
            if b["sibling"]:
                lean["sibling"] = b["sibling"]
            obj["lean"] = lean
        if b["uses"]:
            obj["uses"] = b["uses"]
        objects.append(obj)

        # drift accounting
        provable_or_def = b["kind"] in PROVABLE or b["kind"] == "definition"
        if provable_or_def:
            if q in ("missing", "no-ref") and not b["sibling"]:
                drift["genuinely_unformalized"].append(b["label"])
            elif q in ("missing", "no-ref") and b["sibling"]:
                drift["library_missing_ref"].append(b["label"])
            if rec and b["sibling"] and status == "proved":
                # library proved but a sibling also exists — possible stale dup
                if sibling_sorry(b["sibling"]):
                    drift["stale_sibling"].append(
                        {"label": b["label"], "decl": rec["full"], "sibling": b["sibling"]})

    drift["unreferenced_library_decls"] = sorted(
        f for f, rec in by_full.items()
        if f not in referenced and rec["full"].count(".") >= 2)[:2000]

    manifest = {
        "version": "2.0",
        "generator": "build_proof_objects.py (content-object driven, default lake/lean infra)",
        "manuscript": {
            "repo": "litlfred/qou",
            "paper": args.paper,
            "commit_sha": commit, "branch": branch,
            "build_verified": have_log,
            "build_ok": (args.build_ok and not args.build_failed) if (args.build_ok or args.build_failed) else None,
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
        "summary": {
            "blocks": len(objects),
            "ref_resolution": dict(qstat),
            "status": dict(sstat),
            "status_by_kind": {k: dict(v) for k, v in sorted(kind_status.items())},
            "library_decls_indexed": len(by_full),
        },
        "objects": objects,
    }
    args.output.write_text(json.dumps(manifest, indent=2) + "\n")
    args.drift_output.write_text(json.dumps({
        "generated_at": manifest["manuscript"]["generated_at"],
        "counts": {k: len(v) for k, v in drift.items()},
        **drift,
    }, indent=2) + "\n")

    print(f"\nwrote {args.output} — {len(objects)} blocks")
    print(f"  ref resolution: {dict(qstat)}")
    print(f"  status:         {dict(sstat)}")
    print(f"wrote {args.drift_output} — drift counts: "
          f"{ {k: len(v) for k, v in drift.items()} }")


if __name__ == "__main__":
    main()
