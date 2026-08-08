#!/usr/bin/env python3
"""Find self-assuming projections: `theorem f (h : P) ... : P := h`.

The triviality probe (folio-assistant lean-triviality-probe.ts) surfaces
these, but costs a `lean` elaboration per declaration (~11 min / 40
blocks). The shape is syntactic, so a static pass covers the whole corpus
in seconds and is the cheap pre-filter.

What it flags: a provable declaration whose entire proof term is a bare
identifier that names one of its own explicit hypotheses, AND whose
conclusion is syntactically the same as that hypothesis's type. That is
`P -> P` proved by `id` -- it asserts nothing about the objects involved.

Deliberately NOT flagged:
  * proofs with a tactic block (`:= by ...`) -- a `by exact h` may still
    be vacuous but needs elaboration to judge; out of scope here
  * `h.1`, `h.symm`, `f h` -- projections/applications do real work
  * conclusion differing from the hypothesis type in any way -- even a
    reassociation is content

Output is a candidate list for agent inspection, not a verdict.
"""

import re
import sys
import json
from pathlib import Path

# theorem/lemma NAME <binders> : CONCLUSION := PROOF
DECL = re.compile(
    r"^(?P<kw>theorem|lemma)\s+(?P<name>[A-Za-z_][A-Za-z0-9_.']*)\s*(?P<rest>.*?)(?=^\s*(?:@\[|/--|--|theorem|lemma|def|structure|class|instance|abbrev|noncomputable|end|namespace|\Z))",
    re.S | re.M,
)
# (name : type) explicit binder
BINDER = re.compile(r"\((?P<names>[^():]+?)\s*:\s*(?P<type>(?:[^()]|\([^()]*\))*)\)")


def _blank(text: str) -> str:
    """Blank a comment but KEEP its newlines, so byte offsets AND line
    numbers both survive. Replacing '\\n' with ' ' preserves offsets but
    silently shifts every reported line number after the first block
    comment."""
    return "".join(c if c == "\n" else " " for c in text)


def strip_comments(src: str) -> str:
    src = re.sub(r"/-.*?-/", lambda m: _blank(m.group(0)), src, flags=re.S)
    src = re.sub(r"--[^\n]*", lambda m: _blank(m.group(0)), src)
    return src


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def analyze(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    src = strip_comments(raw)
    out = []
    for m in DECL.finditer(src):
        body = m.group("rest")
        # split at the LAST top-level `:=` that starts the proof term
        idx = body.rfind(":=")
        if idx < 0:
            continue
        proof = norm(body[idx + 2 :])
        # bare identifier proof only (no tactics, no application, no projection)
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*", proof):
            continue
        sig = body[:idx]
        # conclusion = text after the last top-level `:` outside binders
        depth = 0
        concl_at = -1
        for i, ch in enumerate(sig):
            if ch in "([{":
                depth += 1
            elif ch in ")]}":
                depth -= 1
            elif ch == ":" and depth == 0:
                if i + 1 < len(sig) and sig[i + 1] == "=":
                    continue
                concl_at = i
        if concl_at < 0:
            continue
        conclusion = norm(sig[concl_at + 1 :])
        binders = {}
        for b in BINDER.finditer(sig[:concl_at]):
            for nm in b.group("names").split():
                binders[nm] = norm(b.group("type"))
        if proof in binders and binders[proof] == conclusion and conclusion:
            out.append(
                {
                    "decl": m.group("name"),
                    "kind": m.group("kw"),
                    "hypothesis": proof,
                    "statement": conclusion,
                    "file": str(path),
                    "line": src[: m.start()].count("\n") + 1,
                }
            )
    return out


def main():
    roots = sys.argv[1:] or ["content"]
    hits = []
    scanned = 0
    for root in roots:
        for p in Path(root).rglob("*.lean"):
            # Vendored dependency trees are not our corpus: Mathlib ships
            # `(h : P) : P := h` fixtures in MathlibTest/ on purpose.
            if ".lake" in p.parts:
                continue
            scanned += 1
            try:
                hits.extend(analyze(p))
            except Exception as e:  # noqa: BLE001
                print(f"  ! {p}: {e}", file=sys.stderr)
    print(f"scanned {scanned} .lean files — {len(hits)} self-assuming candidate(s)\n")
    for h in sorted(hits, key=lambda x: x["file"]):
        rel = h["file"]
        print(f"  {h['kind']} {h['decl']}")
        print(f"    {rel}:{h['line']}")
        print(f"    ({h['hypothesis']} : {h['statement']})  ⊢  {h['statement']}")
        print()
    Path("/tmp/self-assuming.json").write_text(json.dumps(hits, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
