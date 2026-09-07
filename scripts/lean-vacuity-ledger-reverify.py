#!/usr/bin/env python3
"""Re-verify a stale vacuity-ledger verdict by comparing the DECLARATION, not the file.

Why a verdict goes stale
------------------------
`content/pipeline/lean-vacuity-axiom-audit.ts` keys staleness on `file_sha` =
`sha256(whole file)[:12]`.  So ANY edit to the file expires every verdict in it,
including edits nowhere near the reviewed declaration.  That is deliberate --
the machine cannot know an edit was irrelevant -- and it is why the
`needs-agent` queue fills with entries that already carry a written analysis
and a `stale_prev_verdict`.

Draining those is RE-VERIFICATION, not adjudication: establish that the
declaration is byte-identical to what was reviewed, and the prior verdict
stands unchanged.  That is the pattern the surviving `genuine` rows use
("RE-VERIFIED ... Declaration byte-identical against the recorded revision.
Verdict unchanged.").

Method
------
1. Walk `git log` for the file and find the revision whose blob hashes to the
   recorded `file_sha` prefix.  If no revision matches, say so -- do NOT guess.
2. Extract the declaration's full text at that revision and at HEAD.
3. Report IDENTICAL / CHANGED / NOT-FOUND per entry.

It writes nothing.  Restoring a verdict is a separate, deliberate edit, and
this is the evidence for it.

Usage:
  scripts/lean-vacuity-ledger-reverify.py [--category CAT] [--verdict V]
"""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys

LEDGER = "docs/audits/lean-vacuity-review-ledger.json"
DECL_HEAD = (r"^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|protected\s+|private\s+)*"
             r"(?:theorem|lemma|def|abbrev|instance|class|structure|axiom|opaque|example)\b")


def blob_at(rev: str, path: str) -> bytes | None:
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def find_rev(path: str, sha12: str, limit: int = 400) -> str | None:
    r = subprocess.run(["git", "log", f"-{limit}", "--format=%H", "--", path],
                       capture_output=True, text=True)
    for rev in r.stdout.split():
        b = blob_at(rev, path)
        if b is not None and hashlib.sha256(b).hexdigest()[:12] == sha12:
            return rev
    return None


def extract(text: str, decl: str) -> str | None:
    lines = text.split("\n")
    pat = re.compile(rf"{DECL_HEAD}\s+{re.escape(decl)}\b")
    for i, l in enumerate(lines):
        if not pat.match(l):
            continue
        j = i + 1
        while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
            j += 1
        return "\n".join(lines[i:j]).rstrip()
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", default="proof-no-self-assuming-projection")
    ap.add_argument("--verdict", default="needs-agent")
    a = ap.parse_args()

    d = json.load(open(LEDGER))
    rows = [(k, v) for k, v in d["entries"].items()
            if v.get("category") == a.category and v.get("verdict") == a.verdict]
    print(f"{len(rows)} row(s) category={a.category} verdict={a.verdict}\n")
    tally = {"IDENTICAL": 0, "CHANGED": 0, "NO-REV": 0, "NOT-FOUND": 0}
    for k, v in rows:
        path, decl, _ = k.split("::")
        sha = v.get("file_sha", "")
        rev = find_rev(path, sha) if sha else None
        if not rev:
            tally["NO-REV"] += 1
            print(f"  NO-REV      {decl:<44} file_sha {sha} not in the last 400 commits of {path}")
            continue
        old = blob_at(rev, path)
        new = blob_at("HEAD", path)
        o = extract(old.decode("utf-8", "replace"), decl) if old else None
        n = extract(new.decode("utf-8", "replace"), decl) if new else None
        if o is None or n is None:
            tally["NOT-FOUND"] += 1
            print(f"  NOT-FOUND   {decl:<44} (at {rev[:9]}: {'yes' if o else 'no'}, at HEAD: {'yes' if n else 'no'})")
            continue
        same = o == n
        tally["IDENTICAL" if same else "CHANGED"] += 1
        print(f"  {'IDENTICAL ' if same else 'CHANGED   '}  {decl:<44} reviewed at {rev[:9]}"
              + ("" if same else f"  ({len(o.splitlines())} -> {len(n.splitlines())} lines)"))
    print("\n" + "  ".join(f"{k}={v}" for k, v in tally.items()))
    print("\nIDENTICAL means the prior verdict applies unchanged and the entry can be")
    print("restored with a dated RE-VERIFIED evidence line. Everything else needs a read.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
