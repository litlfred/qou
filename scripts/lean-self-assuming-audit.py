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
# [name : type] instance-implicit and {name : type} implicit binders.
# Matching ONLY round brackets is what made this detector blind to the
# class-instance self-assuming variant that AGENTS.md §3b-cond rule 5 names:
# an `[ctx : C]` binder never entered the binder map at all (bean qou-24m2).
BINDER_INST = re.compile(
    r"\[(?P<names>[^\[\]:]+?)\s*:\s*(?P<type>(?:[^\[\]]|\[[^\[\]]*\])*)\]"
)
BINDER_IMPL = re.compile(
    r"\{(?P<names>[^{}:]+?)\s*:\s*(?P<type>(?:[^{}]|\{[^{}]*\})*)\}"
)
# `class C ... where` followed by its indented field block.
CLASS_DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?class\s+(?P<name>[A-Za-z_][A-Za-z0-9_.']*)"
    r"(?P<params>[^\n]*?)\bwhere\b(?P<body>(?:\n(?:[ \t]+[^\n]*|[ \t]*))*)",
    re.M,
)
CLASS_FIELD = re.compile(
    r"^[ \t]+(?P<field>[A-Za-z_][A-Za-z0-9_']*)\s*:\s*(?P<type>.+)$"
)
# `ctx.claim n ps hc hn` — a projection APPLICATION. The old bare-identifier
# guard rejected these outright, which was the second independent cause of the
# blindness: even with the binder parsed, the proof term never matched.
PROJ_APP = re.compile(
    r"^(?P<binder>[A-Za-z_][A-Za-z0-9_']*)\.(?P<field>[A-Za-z_][A-Za-z0-9_']*)"
    r"(?P<args>\s.*)?$",
    re.S,
)


def parse_classes(src: str) -> dict[str, dict[str, str]]:
    """Map `class name -> {field: declared type}` for classes declared in this
    file.  Cross-file classes are NOT resolved — see the module docstring note."""
    classes: dict[str, dict[str, str]] = {}
    for m in CLASS_DECL.finditer(src):
        fields: dict[str, str] = {}
        cur = None
        for line in m.group("body").split("\n"):
            if not line.strip():
                continue
            fm = CLASS_FIELD.match(line)
            if fm:
                cur = fm.group("field")
                fields[cur] = fm.group("type").strip()
            elif cur and line[:1] in (" ", "\t"):
                fields[cur] = fields[cur] + " " + line.strip()
            else:
                break
        classes[m.group("name")] = fields
    return classes


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
    classes = parse_classes(src)
    out = []
    for m in DECL.finditer(src):
        body = m.group("rest")
        # split at the LAST top-level `:=` that starts the proof term
        idx = body.rfind(":=")
        if idx < 0:
            continue
        proof = norm(body[idx + 2 :])
        # A bare identifier is rule 1; a projection application is rule 2.
        # Anything else (tactic block, real term) is not a candidate.
        is_bare = bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*", proof))
        proj = None if is_bare else PROJ_APP.match(proof)
        if not is_bare and proj is None:
            continue
        sig = body[:idx]
        # conclusion = text after the FIRST top-level `:` outside binders.
        #
        # This used to take the LAST such colon, which silently mis-parses any
        # conclusion containing a binder of its own: in
        #   theorem t (n : Nat) [ctx : C n] : ∀ ps : List Nat, P ps
        # every binder colon is inside brackets (depth > 0), so the only
        # top-level colons are the conclusion separator and the one in
        # `∀ ps : List Nat`.  Taking the last one made the "conclusion"
        # `List Nat, P ps` and no comparison could ever match.  Taking the
        # first is correct for both rules, since binder colons are bracketed.
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
                break
        if concl_at < 0:
            continue
        conclusion = norm(sig[concl_at + 1 :])
        binders = {}
        for rx in (BINDER, BINDER_INST, BINDER_IMPL):
            for b in rx.finditer(sig[:concl_at]):
                for nm in b.group("names").split():
                    binders[nm] = norm(b.group("type"))

        def _hit(hypothesis: str, variant: str) -> None:
            out.append(
                {
                    "decl": m.group("name"),
                    "kind": m.group("kw"),
                    "hypothesis": hypothesis,
                    "statement": conclusion,
                    "variant": variant,
                    "file": str(path),
                    "line": src[: m.start()].count("\n") + 1,
                }
            )

        if not conclusion:
            continue
        # Rule 1 — the proof IS a hypothesis whose type is the conclusion.
        if is_bare:
            if proof in binders and binders[proof] == conclusion:
                _hit(proof, "hypothesis-is-conclusion")
            continue
        # Rule 2 — the proof projects a class field whose DECLARED TYPE is the
        # conclusion: `class C where claim : P` + `theorem t [ctx : C] : P :=
        # ctx.claim ...`.  The class axiomatises the conclusion instead of the
        # hypotheses, which is exactly what §3b-cond rule 5 forbids.
        bname, fname = proj.group("binder"), proj.group("field")
        btype = binders.get(bname)
        if not btype:
            continue
        base = btype.split()[0].lstrip("@")  # `C M q` -> `C`
        ftype = classes.get(base, {}).get(fname)
        if ftype and norm(ftype) == conclusion:
            _hit(f"{bname}.{fname}", "class-field-is-conclusion")
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
        if h.get("variant") == "class-field-is-conclusion":
            print(f"    class field {h['hypothesis']} : {h['statement']}  ⊢  {h['statement']}")
        else:
            print(f"    ({h['hypothesis']} : {h['statement']})  ⊢  {h['statement']}")
        print()
    Path("/tmp/self-assuming.json").write_text(json.dumps(hits, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
