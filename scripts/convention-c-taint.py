#!/usr/bin/env python3
"""Convention-C taint: witnesses whose *provenance* is C, not their content.

The three detectors in `convention-c-witness-audit.py` all read a witness's
own bytes:

  1. fingerprint — a known convention-C decimal appears
  2. structural  — a nonzero `y_λ` on a partition with 3+ rows
  3. symbolic    — a half-integer power of q in a weight expression

Each was added because the previous one missed a class. This script exists
because all three share a limit that adding a fourth content test cannot fix:
**a witness that merely records a number derived from convention-C inputs
carries no trace of the convention in its own content.**

The case that forced it: `atomic-tr-m-mpfr-50dps.witness.json` computes tr_M
"via the Hoefsmit + Wenzl bridge (Σ_λ y_λ · χ_λ)" — its own description says
so — over convention-C weights. It stores trace *values*: no partitions, no
weights, no sqrt. All three tests clear it, it was never in the work list, and
it is the reason `rho_k_h3a_refinement`'s Schur-Weyl check cannot be fixed by
migrating the `y_λ` alone (doing so moved the residual 4.75e-8 -> 0.1868).

Convention propagates along the dependency graph. So does this:

    seed    = witnesses failing any content test
    taint   = fixpoint of: a producer that READS a tainted witness
              produces tainted witnesses

Edges come from the source text (which witness names a producer mentions) and
ownership from each witness's `scriptFile`, so a new dependency taints itself.

WHAT A TAINT IS AND IS NOT
--------------------------
A taint is **provenance-suspect**, not "proved convention C". A producer may
read a tainted witness and never use the affected value, or use only a field
the convention does not touch. Treat the output as a *review queue* ordered by
how far it sits from a seed — not as a verdict, and not as grounds for
rewriting a witness that no content test flags.

The converse is much stronger: a witness that is NOT tainted and fails no
content test is clean on both axes.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "computations" / "audits"))
from _source_normalise import code_only  # noqa: E402

WITNESS_REF = re.compile(r"[A-Za-z0-9._-]+[.-]witness\.json")
#: NOTE the [.-]: 13 witnesses are named `foo-witness.json`, not
#: `foo.witness.json`, and the y_lambda family — the most-read upstream
#: in this campaign — is among them. A `\.witness\.json` pattern drops
#: exactly those edges. The harness carried the same bug.


def _load_audit():
    """Reuse the three content detectors rather than restating them."""
    spec = importlib.util.spec_from_file_location(
        "cca", REPO / "scripts" / "convention-c-witness-audit.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_graph(root: pathlib.Path):
    """owner[witness] -> producer;  reads[producer] -> {witness, ...}."""
    owner, docs = {}, {}
    for p in sorted(root.rglob("*witness.json")):
        if ("_deprecated" in str(p) or "fsh-guts" in str(p)):
            continue
        try:
            raw = p.read_text()
            doc = json.loads(raw)
        except (OSError, json.JSONDecodeError):
            continue
        docs[p.name] = (p, raw, doc)
        sf = doc.get("scriptFile") if isinstance(doc, dict) else None
        if sf:
            owner[p.name] = sf

    writes = {}
    for w, prod in owner.items():
        writes.setdefault(prod, set()).add(w)

    modsrc = _module_sources(root)
    reads = {}
    for prod in writes:
        # Resolve the producer beside a witness it OWNS. Producers emit next to
        # themselves, so an owned witness's directory is the correct tie-break
        # for a duplicated basename — see _read_source. Bean qou-kcii.
        hints = [docs[w][0].parent for w in sorted(writes[prod]) if w in docs]
        src = _read_source(root, prod, hints)
        refs = set(WITNESS_REF.findall(src))
        # Follow local imports: the filename literal often lives one module
        # away from the producer. See _imported_witnesses.
        refs |= _imported_witnesses(src, modsrc)
        reads[prod] = refs - writes[prod]
    return owner, writes, reads, docs


def _read_source(root: pathlib.Path, prod: str,
                 hint_dirs: "list[pathlib.Path] | None" = None) -> str:
    """Source text of producer `prod`, resolved deterministically.

    `hint_dirs` are directories of witnesses this producer OWNS, tried first:
    producers emit beside themselves, so that is the copy whose source
    actually generated those witnesses.

    This matters because the source text is what the edges are read out of —
    `build_graph` greps it for witness names — so resolving the wrong copy
    gives the taint fixpoint wrong edges, and convention-C taint is exactly
    the propagation this script exists to compute. Two producer basenames
    under computations/ are duplicated AND named by a witness scriptFile:
    qbeta_phib_2loop_bdictionary_probe.py (probes/ + qbeta/) and
    witness_provenance_audit.py (root + audits/, two different audits per bean
    qou-2r42). The old fallback returned the first `rglob` hit — os.scandir
    order, not sorted — so which one it read was filesystem-dependent and not
    reproducible from the source. Bean qou-kcii.
    """
    name = pathlib.Path(prod).name
    for d in (hint_dirs or []):
        try:
            return code_only((d / name).read_text())
        except OSError:
            continue
    for cand in (root / prod, root / name):
        try:
            return code_only(cand.read_text())
        except OSError:
            continue
    for hit in sorted(root.rglob(name)):
        if ("_deprecated" in hit.parts or "fsh-guts" in hit.parts):
            continue
        try:
            return code_only(hit.read_text())
        except OSError:
            continue
    return ""


def _module_sources(root: pathlib.Path) -> dict:
    """module stem -> code_only source text, for every .py under computations/."""
    out = {}
    # sorted: `setdefault` is first-wins, and rglob yields in os.scandir order,
    # so for a duplicated module stem the surviving source was whichever copy
    # the filesystem happened to hand over first — stable on one tree, but not
    # across machines. Bean qou-kcii.
    for p in sorted(root.rglob("*.py")):
        if ("_deprecated" in str(p) or "fsh-guts" in str(p)):
            continue
        try:
            out.setdefault(p.stem, code_only(p.read_text()))
        except OSError:
            continue
    return out


_IMPORT = re.compile(r"^\s*(?:from\s+([A-Za-z_][\w.]*)\s+import|import\s+([A-Za-z_][\w.]*))",
                     re.M)


def _imported_witnesses(src: str, modsrc: dict, depth: int = 2) -> set:
    """Witness names reachable through a producer's LOCAL imports.

    A producer often names no witness at all while reading one through a
    helper. `atomic_tr_m_mpfr_50dps.py` is the case that forced this: it
    computes tr_M by calling `tr_m_wenzl_bridge_mpfr.tr_M_via_wenzl_bridge_mpfr`,
    and the `y-lambda-mpfr-witness.json` literal — a structural seed — lives
    inside that helper's `_load_y_lambda`, not in the producer.

    Scanning only the producer's own text therefore missed the very witness
    this script was written for. Two hops by default: helpers import helpers,
    and the cost is a dict lookup.

    Only references that sit in an actual READ context count. Following every
    mention instead tainted 1917 of 2536 witnesses — 75% of the corpus, which
    is not a signal — because shared helpers name many witnesses in docstrings
    and lookup tables without reading them here.
    """
    seen, frontier, found = set(), {src}, set()
    for _ in range(depth):
        nxt = set()
        for text in frontier:
            for a, b in _IMPORT.findall(text):
                mod = (a or b).split(".")[0]
                if mod in seen or mod not in modsrc:
                    continue
                seen.add(mod)
                body = modsrc[mod]
                found |= _read_context_refs(body)
                nxt.add(body)
        if not nxt:
            break
        frontier = nxt
    return found


_READ_CTX = re.compile(r"read_text|open\(|json\.load|loads\(|read_bytes")


def _read_context_refs(body: str) -> set:
    """Witness names appearing within a few lines of an actual file read."""
    lines = code_only(body).splitlines()
    out = set()
    for i, line in enumerate(lines):
        names = WITNESS_REF.findall(line)
        if not names:
            continue
        ctx = "\n".join(lines[max(0, i - 4): i + 5])
        if _READ_CTX.search(ctx):
            out.update(names)
    return out


def seed_set(docs, audit):
    """Witnesses failing any of the three CONTENT tests."""
    seeds = {}
    for name, (_p, raw, doc) in docs.items():
        why = None
        if any(c in raw for c in getattr(audit, "C_FINGERPRINTS", ())):
            why = "fingerprint"
        elif audit.scan_doc(doc):
            why = "structural"
        elif ("**" in raw or "sqrt" in raw) and audit.scan_doc_symbolic(doc):
            why = "symbolic"
        if why:
            seeds[name] = why
    return seeds


def propagate(seeds, writes, reads):
    """Fixpoint. Returns taint[witness] = (distance_from_seed, via_producer)."""
    taint = {w: (0, None) for w in seeds}
    changed = True
    while changed:
        changed = False
        for prod, outs in writes.items():
            src_hits = [(taint[w][0], w) for w in reads.get(prod, ()) if w in taint]
            if not src_hits:
                continue
            dist = min(d for d, _ in src_hits) + 1
            via = min(src_hits)[1]
            for o in outs:
                if o not in taint or taint[o][0] > dist:
                    taint[o] = (dist, f"{prod} <- {via}")
                    changed = True
    return taint


def selftest() -> int:
    """The propagation and the read-context filter both have to be falsifiable."""
    bad = 0

    # propagate(): reachability, distance, and no taint without a path.
    writes = {"a.py": {"A.witness.json"},
              "b.py": {"B.witness.json"},
              "c.py": {"C.witness.json"},
              "z.py": {"Z.witness.json"}}
    reads = {"a.py": set(),
             "b.py": {"A.witness.json"},          # b reads the seed
             "c.py": {"B.witness.json"},          # c reads b's output
             "z.py": {"unrelated.witness.json"}}  # z reads nothing tainted
    t = propagate({"A.witness.json": "structural"}, writes, reads)
    cases = [
        ("seed stays at depth 0", t.get("A.witness.json", (None,))[0] == 0),
        ("direct reader is depth 1", t.get("B.witness.json", (None,))[0] == 1),
        ("transitive reader is depth 2", t.get("C.witness.json", (None,))[0] == 2),
        ("unconnected producer is NOT tainted", "Z.witness.json" not in t),
    ]

    # _read_context_refs(): a mention is not a read. This is the filter that
    # took the corpus from 1917 tainted (75%, no signal) to 562.
    body_read = 'p = HERE / "y-lambda-mpfr-witness.json"\nd = json.loads(p.read_text())'
    body_doc = '"""Superseded by y-lambda-mpfr-witness.json; see the audit."""\nx = 1'
    body_table = 'TABLE = {"proton": "y-lambda-mpfr-proton-witness.json"}  # not read here'
    body_comment_near_read = (
        '# Does NOT touch y-lambda-mpfr-witness.json\n'
        'd = json.loads((HERE / "clean.witness.json").read_text())\n'
    )
    cases += [
        ("witness next to read_text counts",
         "y-lambda-mpfr-witness.json" in _read_context_refs(body_read)),
        ("witness in a docstring does NOT count",
         "y-lambda-mpfr-witness.json" not in _read_context_refs(body_doc)),
        ("witness in a bare lookup table does NOT count",
         "y-lambda-mpfr-proton-witness.json" not in _read_context_refs(body_table)),
        ("witness in a comment adjacent to read_text does NOT count",
         "y-lambda-mpfr-witness.json" not in _read_context_refs(body_comment_near_read)
         and "y-lambda-mpfr-witness.json" not in WITNESS_REF.findall(code_only(body_comment_near_read))),
    ]

    for name, ok in cases:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}")
    print(f"selftest: {len(cases)-bad}/{len(cases)}"
          + ("" if bad else " — propagates along reads, stops at mentions."))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--list", action="store_true", help="show every tainted witness")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--max-depth", type=int, default=None,
                    help="only report taint within N hops of a seed")
    a = ap.parse_args()

    if a.selftest:
        return 1 if selftest() else 0

    audit = _load_audit()
    root = REPO / "computations"
    owner, writes, reads, docs = build_graph(root)
    seeds = seed_set(docs, audit)
    taint = propagate(seeds, writes, reads)

    derived = {w: v for w, v in taint.items() if v[0] > 0}
    if a.max_depth is not None:
        derived = {w: v for w, v in derived.items() if v[0] <= a.max_depth}

    print("convention-C taint (provenance, not content)\n")
    print(f"  witnesses scanned      : {len(docs)}")
    print(f"  producers with an owner: {len(writes)}")
    print(f"  seeds (content tests)  : {len(seeds)}")
    print(f"  derived by provenance  : {len(derived)}")
    print(f"  total suspect          : {len(seeds) + len(derived)}\n")

    by_depth = {}
    for w, (d, _via) in derived.items():
        by_depth.setdefault(d, []).append(w)
    for d in sorted(by_depth):
        names = sorted(by_depth[d])
        print(f"  depth {d}: {len(names)} witness(es)")
        show = names if a.list else names[:8]
        for n in show:
            print(f"      {n}   [{taint[n][1]}]")
        if not a.list and len(names) > len(show):
            print(f"      ... {len(names) - len(show)} more (--list)")

    if a.json:
        pathlib.Path(a.json).write_text(json.dumps({
            "seeds": [{"witness": w, "test": t} for w, t in sorted(seeds.items())],
            "derived": [{"witness": w, "depth": d, "via": v}
                        for w, (d, v) in sorted(derived.items())],
        }, indent=2))
        print(f"\n  json -> {a.json}")

    # Advisory by design: a taint is a review queue, not a verdict.
    return 0


if __name__ == "__main__":
    sys.exit(main())
