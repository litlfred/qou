"""Read qou's bibliography from its per-entry files (bean qou-l7pj).

Since the split, each entry is `folio/references/<id>.json`: the CSL-JSON
item with `"$schema": "folio-reference/v1"` first, and sometimes `_comment`,
an array of note lines. `folio/schema/references.ts` is the loader. Its ORDER
list gives the order `references.bib` is emitted in. Entries built by code,
today only `leitner2026`, stay there as `ref({...})` calls.

Python cannot run that module. Scripts that used to regex `references.ts`
read the entries here instead:

    import references_dir
    for e in references_dir.entries(REPO):   # dicts, in ORDER
        e["id"], e.get("title"), (e.get("library") or {}).get("docId")

An entry built by code comes back as a stub with only the fields its source
spells as literals (`id`, `type`), and `"_codeBuilt": True`. Its computed
title and author are not available here. The regex readers could not see
them before either.

`write_entry()` writes a file in the same format the split wrote it in. That
is `JSON.stringify(entry, null, 2)` plus a newline, so `json.dumps(indent=2,
ensure_ascii=False)` gives the same bytes. A rewrite that changes nothing
leaves the file byte-identical.
"""

from __future__ import annotations

import json
import os
import re

SCHEMA_TAG = "folio-reference/v1"


def references_dir(repo: str) -> str:
    return os.path.join(repo, "folio", "references")


def module_path(repo: str) -> str:
    return os.path.join(repo, "folio", "schema", "references.ts")


def require_split_layout(repo: str) -> None:
    """Exit with a message when the checkout predates the per-entry split.

    A scanner run against the old layout (all entries inline in
    references.ts) would otherwise find an empty directory and report
    nothing, which reads the same as a clean bibliography.
    """
    d = references_dir(repo)
    if not os.path.isdir(d) or not any(f.endswith(".json") for f in os.listdir(d)):
        raise SystemExit(
            f"{d} holds no entry files. This checkout predates the per-entry split "
            "(bean qou-l7pj), where the entries were inline in folio/schema/references.ts. "
            "Rebase onto a main that has folio/references/."
        )


def order(repo: str) -> list[str]:
    """Every id in ORDER, in order: `{ id: "<key>" }` slots and `ref({...})` entries."""
    src = open(module_path(repo), encoding="utf-8").read()
    start = src.index("const ORDER")
    end = src.index("\n];", start)
    body = src[start:end]
    slot = r'^  (?:\{ id: "([^"]+)" \},|ref\(\{\n(?:\s*//.*\n)*\s*id: "([^"]+)",)'
    return [a or b for a, b in re.findall(slot, body, re.M)]


def code_built(repo: str) -> list[dict]:
    """Stubs for the entries built in references.ts: `id`, `type` when literal, `_codeBuilt`."""
    src = open(module_path(repo), encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^  ref\(\{\n(.*?)\n  \}\),", src, re.S | re.M):
        body = m.group(1)
        rid = re.search(r'^\s*id: "([^"]+)",', body, re.M)
        if not rid:
            continue
        stub: dict = {"id": rid.group(1), "_codeBuilt": True}
        t = re.search(r'^\s*type: "([^"]+)",', body, re.M)
        if t:
            stub["type"] = t.group(1)
        out.append(stub)
    return out


def entry_path(repo: str, rid: str) -> str:
    return os.path.join(references_dir(repo), f"{rid}.json")


def read_entry(path: str) -> dict:
    return json.load(open(path, encoding="utf-8"))


def file_entries(repo: str) -> dict[str, dict]:
    """id -> the raw file content (with `$schema` and `_comment`), by file name order."""
    d = references_dir(repo)
    out: dict[str, dict] = {}
    for f in sorted(os.listdir(d)):
        if f.endswith(".json"):
            out[f[: -len(".json")]] = read_entry(os.path.join(d, f))
    return out


def entries(repo: str, *, keep_meta: bool = False) -> list[dict]:
    """Every entry, in ORDER. `$schema` and `_` keys are dropped unless `keep_meta`.

    Entries on disk that ORDER does not list are appended at the end in file
    name order. The TypeScript loader refuses that state, and this reader
    tolerates it, so a scanner still sees every key while ORDER is being
    fixed.
    """
    require_split_layout(repo)
    files = file_entries(repo)
    stubs = {s["id"]: s for s in code_built(repo)}
    out: list[dict] = []
    seen: set[str] = set()
    for rid in order(repo) + sorted(files):
        if rid in seen:
            continue
        seen.add(rid)
        if rid in files:
            e = files[rid]
            if not keep_meta:
                e = {k: v for k, v in e.items() if k != "$schema" and not k.startswith("_")}
            out.append(e)
        elif rid in stubs:
            out.append(stubs[rid])
    return out


def ids(repo: str) -> set[str]:
    return {e["id"] for e in entries(repo)}


def dumps(entry: dict) -> str:
    """The file text for an entry: `JSON.stringify(entry, null, 2)` + newline."""
    return json.dumps(entry, indent=2, ensure_ascii=False) + "\n"


def write_entry(repo: str, entry: dict) -> None:
    with open(entry_path(repo, entry["id"]), "w", encoding="utf-8") as fh:
        fh.write(dumps(entry))
