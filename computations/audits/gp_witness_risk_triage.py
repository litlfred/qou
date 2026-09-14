#!/usr/bin/env python3
"""Which committed witnesses could carry a number from the PRE-FIX GP path?

Bean `qou-b2ie`. The Geck-Pfeiffer q-Murnaghan-Nakayama path in
`pyhecke_native` returned WRONG characters on some plain braid words until the
trivial-rep guard landed (PR #3812, 2026-07-17) and the cyclic-shift completion
followed. After the guard the path REFUSES (panics) rather than returning a
wrong value, so a post-guard witness is either correct or absent.

The risk set is therefore: witnesses whose producer makes a LIVE GP call AND
whose `computedAt` predates the guard (or is missing).

Two over-counting traps this exists to avoid, both instances of the
detector-blindness class in `docs/audits/2026-08-15-detector-blindness-taxonomy.md`:

  1. "the witness blob names a GP producer" is not "a value came through GP" --
     the producer may import GP only for a cross-check, or mention it in prose.
  2. "the source file greps for chi_q_via_gp" is not "the source CALLS it" --
     16 of 30 grep-matched producers name it only in a docstring or comment.

Three over-counting traps, all of the detector-blindness class:

  1. "the witness blob names a GP producer" is not "a value came through GP".
  2. "the source greps for chi_q_via_gp" is not "the source CALLS it" -- 16 of
     30 grep-matched producers name it only in a docstring or comment.
  3. an AUDIT/CATALOGUE witness names every script it audited, so a substring
     match says "it listed this producer", not "this producer wrote it".
  4. a producer stem that is a PREFIX of another stem is credited with the
     longer one's witnesses unless the match is word-bounded.

Trap 3 is separated by how many producer stems the witness names: measured, the
audit catalogues name 579/132/1595 and the real GP products name 3 or 4.

NOT available as a cleaner key, both measured 2026-09-14 and both rejected:
a declared producer field exists on only ~4.5% of witnesses (18 of a 400
sample), and the witness-name-to-producer naming convention holds for only
51.2% (1780 of 3474). Neither can replace the substring match; the traps above
are what make it usable.

Measured 2026-09-14 on `main` with all four traps closed: **2 flagged**, and
both were then disposed of BY MEASUREMENT, so **0 committed witnesses carry a
pre-fix GP number**:

  derived-chi-catalogue-bridge-factor-omega   re-ran mathematically IDENTICAL
  derived-chi-catalogue-production-wire-demo  moved, but because the BRAID WORD
                                              changed grouped->interleaved
                                              (bean `qou-5c64`), not the kernel

A third candidate, `...-matrix-m-mu-n-prototype`, was trap 4 -- its real
producer never mentions a GP symbol. This script flags candidates; it does not
know which have been investigated, so it will keep printing those 2. Read-only
-- runs no producer and writes nothing.
"""
import ast, json, pathlib, re, subprocess, sys

GP = {"chi_lambdas_via_gp", "chi_q_via_gp", "chi_via_gp_hoefsmit"}
GUARD = "2026-07-17"          # PR #3812, refuse-on-disagreement
ROOT = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                   capture_output=True, text=True,
                                   check=True).stdout.strip())

SELF = "computations/audits/gp_witness_risk_triage.py"

grepped = subprocess.run(
    ["grep", "-rl", *sum((["-e", g] for g in sorted(GP)), []),
     "--include=*.py", "computations"],
    cwd=ROOT, capture_output=True, text=True).stdout.split()
grepped = [p for p in grepped if p != SELF]   # this audit names all three itself

live, aliased = set(), []
for p in sorted(grepped):
    try:
        tree = ast.parse((ROOT / p).read_text())
    except Exception:
        continue
    for nd in ast.walk(tree):
        # an aliased import would evade the name check below; measured 0 today,
        # but report it rather than assume it stays 0.
        if isinstance(nd, ast.ImportFrom):
            for a in nd.names:
                if a.name in GP and a.asname:
                    aliased.append((p, a.name, a.asname))
    if any(isinstance(nd, ast.Call)
           and (getattr(nd.func, "attr", None) in GP
                or getattr(nd.func, "id", None) in GP)
           for nd in ast.walk(tree)):
        live.add(pathlib.Path(p).stem)

stems = {pathlib.Path(p).stem for p in grepped}

# Every producer stem in the tree, used only to recognise CATALOGUE witnesses.
# An audit/inventory witness names the scripts it audited, so a substring match
# against its payload says "it listed this producer", not "this producer wrote
# it". Measured on the six candidates: the three audit catalogues name 579, 132
# and 1595 producer stems; the three real GP products name 3 or 4. Two orders of
# magnitude apart with no overlap, so the threshold is not delicate.
ALL_STEMS = {q.stem for q in (ROOT / "computations").glob("**/*.py")}
CATALOGUE_AT = 20

rows = []
for w in (ROOT / "computations").glob("**/*.witness.json"):
    if "_deprecated" in str(w):
        continue
    try:
        d = json.loads(w.read_text())
    except Exception:
        continue
    blob = json.dumps(d)
    # ALL matching stems, never `next(...)` over a set. A witness blob can name
    # more than one producer, and `next` picks an arbitrary one -- iteration
    # order over a set is not stable, so the same witness was classified as
    # risk in one run and safe in the next. Measured: that single-pick gave 3
    # where the correct answer is 6. Classify as risk if ANY naming producer
    # makes a live GP call.
    # Word-BOUNDARY match, never a bare substring. A producer stem that is a
    # PREFIX of another stem is otherwise credited with the longer one's
    # witnesses: `derived_chi_catalogue_matrix_m` is a prefix of
    # `..._mu_n`, `..._multi_a_benchmark` and `..._numerical`, and that alone
    # put `derived-chi-catalogue-matrix-m-mu-n-prototype` in the risk set --
    # whose real producer does not mention a GP symbol at all. `\b` treats `_`
    # as a word character, so `stem\b` will not match `stem_mu_n`.
    hits = [s for s in stems if re.search(rf"{re.escape(s)}\b", blob)]
    if not hits:
        continue
    at = (d.get("computedAt") or d.get("witness", {}).get("computedAt") or "")[:10]
    live_hits = [h for h in hits if h in live]
    named = sum(1 for q in ALL_STEMS if q in blob)
    rows.append((at, live_hits[0] if live_hits else hits[0],
                 bool(live_hits) and named < CATALOGUE_AT,
                 str(w.relative_to(ROOT)), named))

risk = [r for r in rows if r[2] and (not r[0] or r[0] < GUARD)]
print(f"grep-matched producers                : {len(grepped)}")
print(f"  with a LIVE GP call (AST)           : {len(live)}")
print(f"  prose/docstring only                : {len(grepped) - len(live)}")
print(f"aliased GP imports (AST blind spot)   : {len(aliased)}")
print(f"witnesses naming a grep-matched stem  : {len(rows)}")
print(f"  producer never calls GP             : {sum(1 for r in rows if not r[2])}")
print(f"  live GP call, computedAt >= {GUARD} : {sum(1 for r in rows if r[2] and r[0] and r[0] >= GUARD)}")
print(f"  live GP call, pre-guard or undated  : {len(risk)}   <-- RISK SET")
for r in sorted(risk):
    print(f"    {r[0] or '(undated)'} | {r[1]} -> {r[3]}  (names {r[4]} producers)")
cat = [r for r in rows if r[2] is False and r[4] >= CATALOGUE_AT]
if cat:
    print(f"  excluded as CATALOGUE witnesses (name >= {CATALOGUE_AT} producers): {len(cat)}")
    for r in sorted(cat)[:6]:
        print(f"    {r[3]}  (names {r[4]})")
sys.exit(0)
