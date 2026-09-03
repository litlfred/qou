#!/usr/bin/env python3
"""Mechanism-5 population by TAINT on the q0 bind, not by field name.

Companion detector to `q0_muon_population_partition.py::direct_pinners`, which
answers a different question and is not a superset.  Three ways of asking "who
binds q0 out of the anchor-DEFINING witness" disagree, and each one is blind
where the previous was not:

  * `direct_pinners` gates on ``READS_JSON = json.load|read_text|open(`` and
    excludes anything matching ``ROUTES_ANCHOR``.  The exclusion is correct
    for ITS question (who never resolves an anchor at all) and wrong for this
    one -- a file that reads the pin AND imports ``q_parameter`` is the rule-4
    straddle inside one quantity.  The gate also hides the idiom the bean
    itself quotes, ``record_upstream(Q_PIN, ...)["derived_50_digit"]["q"]``,
    which opens nothing of its own.
  * Keying on the field ``derived_50_digit`` misses
    ``probes/bwhk_st_matrix_corroboration.py``, which binds ``q0Value`` out of
    the SAME witness.  Keying on ``q0Value`` over-reports, because producers
    EMIT a field of that name.

So this one taints every name assigned from an expression that mentions the
pin witness, propagates through ``json.loads`` / ``read_text`` /
``record_upstream`` / subscripts / ``.get()``, and reports every key pulled
back out.  It is still not a superset either -- it loses cross-function flow,
where the field-keyed pass sees 21 files this one does not.  Measured
2026-08-24: field-keyed 79, taint 74, union 95, both 58.

Do not read any single number here as "the" population.  See
docs/audits/2026-08-24-mech5-producer-layer-triage.md.

Usage
-----
    python3 computations/audits/mech5_pin_bind_taint_audit.py [out.json]

Pure string/AST inspection -- no arithmetic, so the NO-FLOAT64 discipline is
satisfied vacuously.
"""
import ast, json, pathlib, sys, importlib.util
from collections import Counter

COMP = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "part", COMP / "audits" / "q0_muon_population_partition.py")
part = importlib.util.module_from_spec(spec); spec.loader.exec_module(part)
manifest = json.loads((COMP / "q0_anchor_manifest.json").read_text())
bucket = {s: n for n in ("ideal_muon", "physical_proton", "ambiguous")
          for s in manifest.get(n, [])}
PIN = "q-pinning-50-digit"
Q_KEYS = {"q", "q0Value", "q_0_50dps", "q_pinned", "q_50dps", "q_0"}


def analyse(src):
    tree = ast.parse(src)
    lines = src.splitlines()
    pin_line = [PIN in l for l in lines]

    def mentions_pin(n):
        a = getattr(n, "lineno", None)
        b = getattr(n, "end_lineno", None)
        if a is None:
            return False
        return any(pin_line[i] for i in range(a - 1, min(b or a, len(lines))))

    tainted = set()

    def is_tainted(n, depth=0):
        if depth > 12:
            return False
        if isinstance(n, ast.Name):
            return n.id in tainted
        if isinstance(n, ast.Constant):
            return False
        if mentions_pin(n):
            return True
        return any(is_tainted(c, depth + 1) for c in ast.iter_child_nodes(n))

    assigns = [n for n in ast.walk(tree) if isinstance(n, ast.Assign)]
    for _ in range(3):
        before = len(tainted)
        for n in assigns:
            if is_tainted(n.value):
                for t in n.targets:
                    if isinstance(t, ast.Name):
                        tainted.add(t.id)
        if len(tainted) == before:
            break

    def keychain(n):
        ks, cur = [], n
        while True:
            if isinstance(cur, ast.Subscript):
                ks.append(cur.slice.value if isinstance(cur.slice, ast.Constant) else "?")
                cur = cur.value
            elif (isinstance(cur, ast.Call) and isinstance(cur.func, ast.Attribute)
                  and cur.func.attr == "get" and cur.args
                  and isinstance(cur.args[0], ast.Constant)):
                ks.append(cur.args[0].value)
                cur = cur.func.value
            else:
                break
        return list(reversed(ks)), cur

    chains = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Subscript) or (
                isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "get"):
            ks, base = keychain(n)
            if ks and is_tainted(base):
                chains.add(".".join(str(k) for k in ks))
    return sorted(chains)


rows = []
for path in sorted(COMP.rglob("*.py")):
    if "_deprecated" in path.parts:
        continue
    src = path.read_text(errors="replace")
    if PIN not in src and "load_q_50dps" not in src:
        continue
    try:
        chains = analyse(src) if PIN in src else []
    except (SyntaxError, RecursionError):
        chains = []
    via = part._uses_muon_via_helper(src)
    binds_q = any(c.split(".")[-1] in Q_KEYS for c in chains)
    if not (binds_q or via):
        continue
    rows.append(dict(
        rel=str(path.relative_to(COMP)), stem=path.stem,
        tag=bucket.get(path.stem, "UNDECLARED"),
        intent=part.classify_intent(src),
        chains=chains, coread=part.co_read_fields(src),
        routes_anchor=bool(part.ROUTES_ANCHOR.search(src)),
        via_helper=bool(via), loc=len(src.splitlines()),
    ))

if len(sys.argv) > 1:
    json.dump(rows, open(sys.argv[1], "w"), indent=1)
print("TOTAL mech-5 (taint):", len(rows))
print("tag:", dict(Counter(r["tag"] for r in rows)))
print("routes anchor too:", sum(r["routes_anchor"] for r in rows))
print("intent:", dict(Counter(r["intent"] for r in rows)))
print("terminal q keys:", dict(Counter(
    c.split(".")[-1] for r in rows for c in r["chains"]
    if c.split(".")[-1] in Q_KEYS)))
