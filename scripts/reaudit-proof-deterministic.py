#!/usr/bin/env python3
"""
Re-audit proof-QA sidecar verdicts from the 2026-06-22 ``qa-agent-drain``
batch for the *deterministically token-checkable* criteria.

That batch produced a high false-positive rate (verified against the actual
Lean source: ~86% of ``proof-no-decide-masking`` fails carry no ``decide``
token, ~76% of ``proof-no-trivial-true`` fails carry no ``: True`` conclusion).
This script recomputes those verdicts directly from the resolved Lean source
and appends a corrected agent entry (latest-wins) where the cached verdict is
contradicted by the source.

Resolution order for a block's Lean source:
  1. sibling ``<block>.lean``
  2. the ``lean.ref`` ``qou:QOU.<Mod>.<Decl>`` -> library file under
     ``content/quantum-observable-universe/lean/QOU/<Mod>.lean`` (and the
     ``<Mod>/<Decl>.lean`` variant).

Token criteria (evaluated on comment-stripped source):
  - proof-no-decide-masking : FAIL iff ``decide``/``native_decide`` present.
  - proof-no-trivial-true   : FAIL iff a declaration concludes ``: True``.

Conservative policy: this script only *corrects false positives* — it flips a
cached ``fail`` to ``pass`` when the source has no offending token (or to
``n/a`` when no Lean resolves at all). Blocks whose source *does* contain the
token are GENUINE fails and are left untouched (reported, for the content-fix
pass).

Usage:
  python3 scripts/reaudit-proof-deterministic.py [--apply] [--head <sha>]
Without --apply it is a dry run (prints the plan, writes nothing).
"""
from __future__ import annotations
import argparse, datetime, glob, hashlib, json, os, re, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEAN_ROOT = "content/quantum-observable-universe/lean/QOU"

# --- comment stripping -------------------------------------------------------
# State-machine stripper (per Gemini review on PR #2775): a regex stripper
# mishandles nested block comments `/- /- -/ -/`, line comments containing `/-`,
# and tokens like `decide` inside string literals. This walks the source.
def strip_comments(src: str) -> str:
    out = []
    i, n = 0, len(src)
    state = "normal"  # normal | string | line_comment | block_comment
    depth = 0
    while i < n:
        if state == "normal":
            if src[i:i + 2] == "/-":
                state, depth, i = "block_comment", 1, i + 2
            elif src[i:i + 2] == "--":
                state, i = "line_comment", i + 2
            elif src[i] == '"':
                state = "string"; out.append(src[i]); i += 1
            else:
                out.append(src[i]); i += 1
        elif state == "string":
            if src[i] == "\\":
                i += 2
            elif src[i] == '"':
                state = "normal"; out.append(src[i]); i += 1
            else:
                i += 1
        elif state == "line_comment":
            if src[i] == "\n":
                state = "normal"; out.append(src[i]); i += 1
            else:
                i += 1
        else:  # block_comment
            if src[i:i + 2] == "/-":
                depth += 1; i += 2
            elif src[i:i + 2] == "-/":
                depth -= 1; i += 2
                if depth == 0:
                    state = "normal"
            else:
                i += 1
    return "".join(out)

# --- token signals -----------------------------------------------------------
_DECIDE = re.compile(r"(?<![A-Za-z_])(?:native_decide|decide)(?![A-Za-z_])")
_TRUE_CONCL = re.compile(r":\s*True\b")

def has_decide(stripped: str) -> bool:
    return bool(_DECIDE.search(stripped))

def has_trivial_true(stripped: str) -> bool:
    return bool(_TRUE_CONCL.search(stripped))

# --- Lean source resolution --------------------------------------------------
def resolve_lean(qa_path: str) -> list[str]:
    base = qa_path[: -len(".qa.json")]
    out: list[str] = []
    sib = base + ".lean"
    if os.path.exists(sib):
        out.append(sib)
    ts_path = base + ".ts"
    if os.path.exists(ts_path):
        with open(ts_path, encoding="utf-8") as f:
            ts = f.read()
        m = re.search(r'ref:\s*"qou:QOU\.([^"]+)"', ts)
        if m:
            decl = m.group(1)
            mod = decl.rsplit(".", 1)[0].replace(".", "/")
            for cand in (f"{LEAN_ROOT}/{mod}.lean",
                         f"{LEAN_ROOT}/{decl.replace('.', '/')}.lean"):
                if os.path.exists(cand) and cand not in out:
                    out.append(cand)
    return out

def file_hash(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

def current_field_hash(qa_path: str) -> dict:
    base = qa_path[: -len(".qa.json")]
    fh = {}
    for ext in ("md", "ts", "lean"):
        h = file_hash(f"{base}.{ext}")
        if h:
            fh[ext] = h
    return fh

CRITERIA = {
    "proof-no-decide-masking": has_decide,
    "proof-no-trivial-true": has_trivial_true,
}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--head", default=None)
    args = ap.parse_args()
    os.chdir(REPO)
    head = args.head or subprocess.check_output(
        ["git", "rev-parse", "HEAD"]).decode().strip()
    now = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%S.000Z")
    today = now[:10]

    stats = {c: {"flip_pass": 0, "set_na": 0, "genuine_fail": 0} for c in CRITERIA}
    genuine: dict[str, list[str]] = {c: [] for c in CRITERIA}
    touched = 0

    for qa in sorted(glob.glob("content/**/*.qa.json", recursive=True)):
        try:
            with open(qa, encoding="utf-8") as f:
                d = json.load(f)
            if isinstance(d, list):  # tolerate list-wrapped sidecars
                d = d[0] if d else {}
        except Exception:  # noqa: BLE001  (skip any unreadable/invalid sidecar)
            continue
        crit = d.get("criteria") or {}
        lean_paths = None  # lazy
        stripped = None
        changed = False
        for cname, sig in CRITERIA.items():
            entries = crit.get(cname)
            if not entries or entries[-1].get("result") != "fail":
                continue
            if lean_paths is None:
                lean_paths = resolve_lean(qa)
                src = ""
                for lp in lean_paths:
                    try:
                        with open(lp, encoding="utf-8") as f:
                            src += f.read() + "\n"
                    except Exception:  # noqa: BLE001  (skip unreadable Lean)
                        pass
                stripped = strip_comments(src)
            if not lean_paths:
                result, note = "n/a", ("Re-audit %s: no Lean source resolves "
                                       "(no sibling .lean, no lean.ref); "
                                       "Lean-token criterion is n/a." % today)
                stats[cname]["set_na"] += 1
            elif sig(stripped):
                stats[cname]["genuine_fail"] += 1
                genuine[cname].append(qa)
                continue  # leave genuine fail untouched
            else:
                tok = ("`decide`/`native_decide`"
                       if cname == "proof-no-decide-masking" else "`: True`")
                result = "pass"
                note = ("Re-audit %s: no %s token in resolved Lean source (%s); "
                        "2026-06-22 batch fail was a false positive."
                        % (today, tok, ", ".join(lean_paths)))
                stats[cname]["flip_pass"] += 1
            entries.append({
                "field_hash": current_field_hash(qa),
                "result": result,
                "notes": note,
                "reviewed_at": now,
                "reviewed_sha": head,
                "reviewer": {
                    "kind": "agent",
                    "id": "local/qa-agent-drain",
                    "agent_skill": "local/qa-agent-drain",
                    "agent_model": "claude-opus-4-8",
                    "agent_date": today,
                },
            })
            changed = True
        if changed:
            touched += 1
            if args.apply:
                with open(qa, "w", encoding="utf-8") as f:
                    json.dump(d, f, indent=2, ensure_ascii=False)
                    f.write("\n")

    print("=== deterministic proof re-audit (%s) ===" % ("APPLY" if args.apply else "DRY RUN"))
    for c, s in stats.items():
        print(f"{c}: flip->pass={s['flip_pass']}  set->n/a={s['set_na']}  "
              f"genuine_fail(left)={s['genuine_fail']}")
    print(f"sidecars touched: {touched}")
    print("\nGenuine fails to fix in the content pass:")
    for c, lst in genuine.items():
        print(f"  {c}: {len(lst)}")
        for p in lst:
            print(f"     {p}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
