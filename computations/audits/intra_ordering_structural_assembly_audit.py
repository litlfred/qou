#!/usr/bin/env python3
"""A grouped intra-nucleon word assembled BY CONSTRUCTION, under another name.

`pyhecke.atom.nucleon_word_letters` defines the legacy ordering in one line:

    if intra_order == "grouped":
        return [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]

Any caller that writes that expression — or the equivalent two sequential
loops — has built the grouped word, whatever it calls the result and whatever
values it read. This audit finds those sites.

WHY IT EXISTS — the value fingerprint could not see this
--------------------------------------------------------
`intra_ordering_value_fingerprint_audit` matches committed *numbers* against
the known grouped constants. That works on a producer whose witness carries a
trace value at a canonical atom, and it is blind to everything else: a symbolic
producer, a slow one nobody has re-run, one whose witness records a ratio or a
slope rather than a trace, one whose grouped value is not in the fingerprint
table. Working `qou-4383` I re-ran six safe producers looking for stale
artifacts and every one came back byte-identical, which retired the "stale
value" hypothesis and left the residue unexplained.

`tr_m_algebraic_q` is what explained it. It builds a symbolic mirror of the
production atom word, its witness had carried
`algebraic_q0_matches_transfer  computed=9.76e-01  tol=1e-09  passed=False`
since 2026-09-07, and the cause was not a value at all: it laid its intra
letters down as all of `_PROTON_G0` then all of `_PROTON_G1`. Those two
constants are the canonical letters **bucketed by generator** — as
`mass_at_3A_proper` says where it imports them, they "cannot express the
interleaving" — so the loop shape *is* the grouped branch and no input could
have made it canonical. σ₀ and σ₁ are adjacent and do not commute; the two
orderings are different elements of H₃(q), 82 % apart in |tr_M| at one proton.
Rebuilt on `nucleon_word_letters`, the deuteron went 4.23e-01 → 8.9e-14.

That is a defect in the SHAPE of the code, so the detector has to read shape.

WHAT IT FLAGS
-------------
A. **The grouped branch, cloned.** A list concatenation whose two operands are
   comprehensions over different iterables, tagging the left elements with
   offset `0` and the right with offset `1`. This is `nucleon_word_letters`'
   grouped branch transcribed, and the corpus carries several independent
   copies of it under names (`_nucleon_word`, `nucleon_word`, `_word`) that do
   not say "grouped".

B. **The same assembly as sequential loops.** Two consecutive `for` statements
   over a `…g0`-named and a `…g1`-named iterable, both accumulating into the
   same list. Same word, written long-hand.

C. **A frame declared but not built (blocking).** A file carrying an A or B
   assembly that also stamps `intra_ordering_frame`. The stamp is read off
   `atom_braid_word_3A`'s signature default, so it reports the frame the
   PRODUCTION builder considers canonical — which is a true statement about the
   signature and a false one about the word this file just built by hand. A
   witness consumer cannot tell those apart, and `canonical_trm_reference`
   trusts the field: this is the pin/ordering guard defeated by a correct-
   looking stamp. Zero today, so it is a gate rather than a ratchet.

D. **Detector integrity (blocking).** The A matcher is run against `atom.py`
   itself and MUST fire on the grouped assembly's own definition. If that gets
   rewritten, the pattern below stops describing "grouped" and this audit would
   go quiet while the defect it names got easier to commit. Binding the matcher
   to the definition it claims to track is what stops a silent retirement — the
   failure mode `scripts/precision-gates.sh` calls "how a checker goes quiet",
   reached from the other direction. Scoped to the FILE, not to a named
   function: it was pinned to `nucleon_word_letters` first, and hoisting the
   assembly into `grouped_word_from_chains` — the refactor this audit's own
   remedy asked for — broke it within the hour. A check that fails when the
   code it guards is tidied trains people to loosen it.

E. **Declared grouped assembly (advisory, never blocking).** Calls to
   `pyhecke.atom.grouped_word_from_chains`, counted and listed. That helper is
   the remedy for a site where the LEGACY frame is genuinely the object under
   study and the caller holds chains rather than quarks — the case
   `legacy_marshalled_frame` is in. Counting it is what keeps the remedy
   honest: converting an A/B site to a named call drains the ratchet, so
   without E a lazy sweep could green this gate while every value stayed
   wrong. E makes each such conversion show up as a visible, greppable choice
   instead of a disappearance.

NOT FLAGGED, deliberately
-------------------------
  * `nucleon_word_letters(…, intra_order="grouped")` — asking for the legacy
    word BY ITS NAME is the declared, reviewable use. The defect is building it
    unnamed, not needing it.
  * Order-insensitive use of the buckets: `vertex_volume(_PROTON_G0)`,
    `len(_PROTON_G0) + len(_PROTON_G1)`, per-generator channel decompositions.
    A bucket is the right object for a per-generator quantity; ~30 live modules
    import these constants and most never assemble a word. A detector that
    flagged all of them would be read by nobody.
  * `pyhecke/atom.py` — it defines the branch; check D requires it to match.
  * `_deprecated/`, `library/`.
  * B over iterables NOT named `…g0`/`…g1`. The name requirement is what keeps
    B from firing on every adjacent pair of loops in the corpus; the cost is
    that a rename hides the shape, which is why A — whose evidence is the
    literal `0`/`1` offsets, not the names — carries the bulk of the detection.

A and B are RATCHETS against a committed baseline, not pass/fail. They are red
on arrival, and per this repo's doctrine a gate that is red on arrival gets
skipped. THE BASELINE DRAINS, NEVER GROWS: fix at the site by calling
`nucleon_word_letters`, then `--rebaseline` to lower it.

Draining is NOT uniform work. Switching a site to the canonical ordering moves
**absolute** traces (3.785× at 2H, 7.868× at 3H, 6.891× at 3He, 14.325× at 4He)
while leaving log-ratios and the three bond constants untouched, so each site
has to be read for which kind of quantity it reports before it is switched.

Exit 0 when clean, 1 otherwise. `--self-test` runs the fixtures only;
`--files a.py b.py` scans a subset (and then refuses `--rebaseline`, since a
partial scan cannot distinguish "fixed" from "not looked at").

-- Ref: [manuscript] AGENTS.md
-- Ref: [manuscript] tools/pyhecke/python/pyhecke/atom.py nucleon_word_letters
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # computations/
REPO = os.path.dirname(ROOT)                       # repo root
ATOM_PY = os.path.join(REPO, "tools", "pyhecke", "python", "pyhecke", "atom.py")

SKIP_DIRS = {"__pycache__", "node_modules", ".git", ".lake", "library",
             "_deprecated", "data", "dist", "build", ".venv"}

#: This file quotes the grouped branch in its own docstring and fixtures.
SELF = os.path.abspath(__file__)

#: `atom.py` DEFINES the branch; check D requires it to match, so it must not
#: also be reported as a finding.
EXEMPT = {SELF, os.path.abspath(ATOM_PY)}

BASELINE = os.path.join(HERE, "intra-ordering-structural-assembly-baseline.json")

#: A name that holds the generator-0 / generator-1 bucket. Bare `g0`/`g1` are
#: included because all four corpus clones take them as parameters.
_G0_NAME = re.compile(r"(?:^|_)g0$", re.I)
_G1_NAME = re.compile(r"(?:^|_)g1$", re.I)

#: The stamp that check C pairs with an assembly.
#:
#: There is deliberately NO companion pattern exempting
#: `intra_order="grouped"`. That call needs no exemption: asking for the legacy
#: word by name does not produce the concat shape A matches, so it is quiet for
#: a structural reason rather than a listed one. A regex saying otherwise would
#: imply a check that does not exist.
_FRAME_STAMP = re.compile(r"intra_ordering_frame")


def _last_tuple_const(elt) -> object:
    """The last element of a tuple literal, if it is a constant."""
    if not isinstance(elt, ast.Tuple) or not elt.elts:
        return None
    tail = elt.elts[-1]
    return tail.value if isinstance(tail, ast.Constant) else None


def _comp_of(node):
    """A list comprehension, seen through an enclosing `list(...)`."""
    if isinstance(node, ast.ListComp):
        return node
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == "list" and len(node.args) == 1
            and isinstance(node.args[0], (ast.ListComp, ast.GeneratorExp))):
        return node.args[0]
    return None


def _iter_name(comp) -> str | None:
    if not comp.generators:
        return None
    it = comp.generators[0].iter
    return it.id if isinstance(it, ast.Name) else None


def match_grouped_concat(node) -> str | None:
    """Check A's matcher: is `node` the grouped branch, as an expression?

    Returns a human-readable description, or None. Kept as one function so
    check D can point it at `nucleon_word_letters` and demand a hit.
    """
    if not (isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add)):
        return None
    left, right = _comp_of(node.left), _comp_of(node.right)
    if left is None or right is None:
        return None
    if _last_tuple_const(left.elt) != 0 or _last_tuple_const(right.elt) != 1:
        return None
    ln, rn = _iter_name(left), _iter_name(right)
    if ln is None or rn is None or ln == rn:
        return None
    return f"[(…, 0) for … in {ln}] + [(…, 1) for … in {rn}]"


def _appends_into(body) -> set[str]:
    """Names that `body` appends/extends into, e.g. `factors.append(...)`."""
    out: set[str] = set()
    for n in ast.walk(ast.Module(body=list(body), type_ignores=[])):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr in ("append", "extend")
                and isinstance(n.func.value, ast.Name)):
            out.add(n.func.value.id)
    return out


def match_sequential_loops(body) -> list[tuple[int, str]]:
    """Check B's matcher over a statement list: consecutive g0 then g1 loops."""
    hits = []
    for i in range(len(body) - 1):
        a, b = body[i], body[i + 1]
        if not (isinstance(a, ast.For) and isinstance(b, ast.For)):
            continue
        an = a.iter.id if isinstance(a.iter, ast.Name) else None
        bn = b.iter.id if isinstance(b.iter, ast.Name) else None
        if not (an and bn and _G0_NAME.search(an) and _G1_NAME.search(bn)):
            continue
        shared = _appends_into(a.body) & _appends_into(b.body)
        if shared:
            hits.append((a.lineno,
                         f"for … in {an}: {sorted(shared)[0]}.append(…) "
                         f"then for … in {bn}: same accumulator"))
    return hits


#: A branch test that names the ordering choice. A concat inside one is a
#: DECLARED legacy path, not a silent default — `closed_form_tau_M`'s
#: `if intra_order == "grouped"` (resolved under `qou-y2o7`) is the model: the
#: parameter defaults to borromean, the canonical arm calls the real producer,
#: and the grouped arm is opt-in and documented. Flagging that the same way as
#: an unconditional concat would put a fixed site and a broken one in one
#: undifferentiated list, which is how a 17-entry baseline stops being read.
_GUARD_TEST = re.compile(r"grouped|intra_order|legacy|historical", re.I)


def _guarding_branch(node, parents: dict) -> str | None:
    """The nearest enclosing `if` whose test names the ordering, if any."""
    cur = parents.get(id(node))
    while cur is not None:
        if isinstance(cur, ast.If):
            try:
                test = ast.unparse(cur.test)
            except Exception:                       # pragma: no cover
                test = ""
            if _GUARD_TEST.search(test):
                return test[:80]
        cur = parents.get(id(cur))
    return None


def scan_file(path: str) -> list[dict]:
    """A and B findings for one source file, plus C if the frame is stamped."""
    try:
        src = open(path, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError):
        return []
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []

    parents: dict = {}
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            parents[id(child)] = parent

    rel = os.path.relpath(path, REPO)
    found: list[dict] = []
    for node in ast.walk(tree):
        d = match_grouped_concat(node)
        if d:
            found.append({"check": "A", "path": rel,
                          "line": getattr(node, "lineno", 0), "detail": d,
                          "guard": _guarding_branch(node, parents)})
    for node in ast.walk(tree):
        for field in ("body", "orelse", "finalbody"):
            body = getattr(node, field, None)
            if isinstance(body, list):
                for line, d in match_sequential_loops(body):
                    stmt = next((x for x in body
                                 if getattr(x, "lineno", None) == line), None)
                    found.append({"check": "B", "path": rel,
                                  "line": line, "detail": d,
                                  "guard": _guarding_branch(stmt, parents)
                                           if stmt is not None else None})

    if found and _FRAME_STAMP.search(src):
        found.append({
            "check": "C", "path": rel, "line": 0,
            "detail": ("stamps `intra_ordering_frame` while assembling the "
                       "grouped word by hand — the stamp reports the "
                       "production builder's default, not what this file built"),
        })

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = (node.func.id if isinstance(node.func, ast.Name)
                  else node.func.attr if isinstance(node.func, ast.Attribute)
                  else None)
            if fn == "grouped_word_from_chains":
                found.append({"check": "E", "path": rel,
                              "line": node.lineno,
                              "detail": "declared grouped assembly"})
    return found


def tracked_only() -> set[str] | None:
    """Tracked-file filter — see `_tracked_corpus` for why a ratchet needs one.

    Same helper `y_lambda_conflation_audit` uses. Its check D counted
    gitignored chi caches and moved whenever a sibling regenerated one; the
    risk here is smaller (untracked `.py` is usually a scratch script rather
    than a cache) but identical in kind, and this audit of all audits should
    not transcribe a shared helper instead of calling it.
    """
    from _tracked_corpus import tracked_files          # noqa: PLC0415
    #: `verify` names a file OUTSIDE this directory on purpose. Pointing it at
    #: SELF proved nothing: the first version listed only `computations/audits`
    #: and SELF is in there, so the check passed while every scanned source
    #: outside it read as untracked and A/B collapsed 17 -> 0.
    return tracked_files(HERE, verify=os.path.join(REPO, "AGENTS.md"))


def iter_sources(files: list[str] | None):
    if files:
        for f in files:
            p = os.path.abspath(f)
            if p not in EXEMPT and p.endswith(".py"):
                yield p
        return
    tracked = tracked_only()
    roots = [ROOT, os.path.join(REPO, "tools", "pyhecke")]
    for base in roots:
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in sorted(filenames):
                if not fn.endswith(".py"):
                    continue
                p = os.path.abspath(os.path.join(dirpath, fn))
                if p in EXEMPT:
                    continue
                if tracked is not None and p not in tracked:
                    continue
                yield p


# ── check D: the matcher must still describe `nucleon_word_letters` ──────────

def check_detector_integrity() -> tuple[bool, str]:
    """A must fire on the grouped assembly's own definition, in `atom.py`.

    Deliberately scoped to the FILE rather than to a named function. It was
    pinned to `nucleon_word_letters` at first, and hoisting the assembly into
    `grouped_word_from_chains` — a refactor this audit's own remedy asked for —
    broke it within the hour. A check that fails when the code it guards is
    tidied trains people to loosen it. What must hold is that atom.py still
    defines the shape somewhere; where it lives is not this audit's business.
    """
    if not os.path.exists(ATOM_PY):
        return False, f"{ATOM_PY} not found — cannot confirm the matcher"
    try:
        tree = ast.parse(open(ATOM_PY, encoding="utf-8").read())
    except (OSError, SyntaxError) as exc:
        return False, f"{ATOM_PY} unreadable: {exc}"
    for sub in ast.walk(tree):
        d = match_grouped_concat(sub)
        if d:
            fn = next((n.name for n in ast.walk(tree)
                       if isinstance(n, ast.FunctionDef)
                       and n.lineno <= sub.lineno
                       and sub.lineno <= (n.end_lineno or n.lineno)), "?")
            return True, f"matched in atom.py:{sub.lineno} ({fn})  {d}"
    return False, ("atom.py no longer contains the concat shape this audit "
                   "matches on — the grouped assembly was rewritten and checks "
                   "A/B now describe nothing. Re-derive the matcher from the "
                   "new definition before trusting a green run.")


# ── self-test ────────────────────────────────────────────────────────────────

_MUST_FIRE = {
    "A_clone": '''
def _nucleon_word(g0, g1):
    return [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]
''',
    "A_clone_wrapped": '''
def _word(g0, g1):
    return (list((mp.mpf(c), mp.mpf(d), 0) for c, d in g0)
            + list((mp.mpf(c), mp.mpf(d), 1) for c, d in g1))
''',
    "B_loops": '''
def build(k, g0, g1):
    factors = []
    for _c, d in g0:
        factors.append((d, 3 * k))
    for _c, d in g1:
        factors.append((d, 3 * k + 1))
    return factors
''',
}

_MUST_STAY_QUIET = {
    "declared_grouped": '''
w = nucleon_word_letters(["u", "u", "d"], intra_order="grouped")
''',
    "canonical_call": '''
for c, d, off in nucleon_word_letters(quarks, intra_order=frame):
    factors.append((d, 3 * k + off))
''',
    "bucket_volumes": '''
Vp0 = vertex_volume(_PROTON_G0)
Vp1 = vertex_volume(_PROTON_G1)
n_p = len(_PROTON_G0) + len(_PROTON_G1)
''',
    "different_offsets": '''
rows = [(c, d, 0) for c, d in g0] + [(c, d, 0) for c, d in g1]
''',
}


def _fixture_hits(src: str) -> int:
    tree = ast.parse(src)
    n = sum(1 for node in ast.walk(tree) if match_grouped_concat(node))
    for node in ast.walk(tree):
        for field in ("body", "orelse", "finalbody"):
            body = getattr(node, field, None)
            if isinstance(body, list):
                n += len(match_sequential_loops(body))
    return n


#: Check C is BLOCKING AT ZERO, so nothing in a normal run exercises it. A
#: blocking check with no live example is indistinguishable from a broken one —
#: which is the failure mode this whole audit is about — so it gets its own
#: fixture pair, scanned through `scan_file` rather than `_fixture_hits`
#: because C is a whole-file property, not an AST-node one.
_C_FIRES = ('def _nucleon_word(g0, g1):\n'
            '    return [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]\n'
            'w.add_data("intra_ordering_frame", frame)\n')
_C_QUIET = ('w.add_data("intra_ordering_frame", frame)\n'
            'for c, d, off in nucleon_word_letters(quarks):\n'
            '    factors.append((d, 3 * k + off))\n')


def _scan_text(src: str, tmpdir: str, name: str) -> list[dict]:
    p = os.path.join(tmpdir, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(src)
    return scan_file(p)


def self_test() -> list[str]:
    import tempfile
    fails = []
    for name, src in _MUST_FIRE.items():
        if _fixture_hits(src) == 0:
            fails.append(f"must-fire fixture stayed quiet: {name}")
    for name, src in _MUST_STAY_QUIET.items():
        if _fixture_hits(src) != 0:
            fails.append(f"must-stay-quiet fixture fired: {name}")
    with tempfile.TemporaryDirectory() as td:
        hit = _scan_text(_C_FIRES, td, "c_fires.py")
        if not any(f["check"] == "C" for f in hit):
            fails.append("must-fire fixture stayed quiet: C_stamp_without_build")
        quiet = _scan_text(_C_QUIET, td, "c_quiet.py")
        if any(f["check"] == "C" for f in quiet):
            fails.append("must-stay-quiet fixture fired: C_stamp_with_canonical")
    return fails


# ── baseline ─────────────────────────────────────────────────────────────────

def _key(f: dict) -> str:
    return f"{f['path']}:{f['line']}:{f['check']}"


def _load_baseline() -> set[str]:
    try:
        with open(BASELINE, encoding="utf-8") as fh:
            return set(json.load(fh).get("sites", []))
    except (OSError, ValueError):
        return set()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--rebaseline", action="store_true")
    ap.add_argument("--files", nargs="*", default=None)
    args = ap.parse_args(argv)

    st = self_test()
    if args.self_test:
        for f in st:
            print(f"  FAIL {f}")
        ok_d, msg_d = check_detector_integrity()
        print(f"  detector integrity: {'PASS' if ok_d else 'FAIL'}  {msg_d}")
        print(f"  self-test: {'PASS' if not st else 'FAIL'} "
              f"({len(_MUST_FIRE) + 1} must-fire, "
              f"{len(_MUST_STAY_QUIET) + 1} must-stay-quiet)")
        return 0 if (not st and ok_d) else 1

    partial = bool(args.files)
    #: A partial scan sees a subset, so its "no longer fires" set is
    #: meaningless — the same footgun `y_lambda_conflation_audit` guards.
    if partial and args.rebaseline:
        print("  REFUSED: --rebaseline needs a whole-tree scan; drop --files.")
        return 1

    findings: list[dict] = []
    for path in iter_sources(args.files):
        findings.extend(scan_file(path))

    ab = [f for f in findings if f["check"] in ("A", "B")]
    c = [f for f in findings if f["check"] == "C"]
    e = [f for f in findings if f["check"] == "E"]
    keys = {_key(f) for f in ab}
    base = _load_baseline()
    new = sorted(k for k in keys if k not in base)
    fixed = [] if partial else sorted(base - keys)

    ok_d, msg_d = check_detector_integrity()

    if args.rebaseline:
        with open(BASELINE, "w", encoding="utf-8") as fh:
            json.dump({
                "_comment": ("Sites assembling the grouped intra-nucleon word "
                             "by construction. DRAINS, NEVER GROWS: fix by "
                             "calling pyhecke.atom.nucleon_word_letters."),
                "sites": sorted(keys),
            }, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"  rebaselined A/B at {len(keys)} sites -> {BASELINE}")

    print("=" * 78)
    print(" GROUPED INTRA-NUCLEON WORD ASSEMBLED BY CONSTRUCTION")
    print("=" * 78)
    na = sum(1 for f in ab if f["check"] == "A")
    nb = sum(1 for f in ab if f["check"] == "B")
    print(f"  A  grouped branch cloned as a concat      : {na}"
          f"   (ratchet, baseline {len(base)})")
    print(f"  B  same assembly as sequential loops      : {nb}   (ratchet)")
    print(f"  C  frame stamped but not built            : {len(c)}   (blocking)")
    print(f"  D  detector integrity                     : "
          f"{'PASS' if ok_d else 'FAIL'}   (blocking)")
    print(f"  E  DECLARED grouped assembly              : {len(e)}"
          f"   (advisory — counted, never blocking)")
    if partial:
        print("     partial scan (--files): the drain count needs a "
              "whole-tree run")
    print(f"     new since baseline : {len(new)}"
          f"{'' if partial else f'      drained : {len(fixed)}'}")
    print(f"  selftest : {'PASS' if not st else 'FAIL'} "
          f"({len(_MUST_FIRE) + 1} must-fire, {len(_MUST_STAY_QUIET) + 1} "
          f"must-stay-quiet)")

    if ab:
        guarded = [f for f in ab if f.get("guard")]
        bare = [f for f in ab if not f.get("guard")]
        for label, group in (("UNGUARDED — a silent default", bare),
                             ("guarded — a declared legacy branch", guarded)):
            if not group:
                continue
            print()
            print(f"  {label}: {len(group)}")
            for f in sorted(group, key=_key):
                mark = "NEW " if _key(f) in new else "    "
                print(f"  {mark}[{f['check']}] {f['path']}:{f['line']}")
                print(f"           {f['detail']}")
                if f.get("guard"):
                    print(f"           under: if {f['guard']}")
    if c:
        print()
        for f in c:
            print(f"  [C] {f['path']}")
            print(f"        {f['detail']}")
    if not ok_d:
        print()
        print(f"  [D] {msg_d}")
    if e:
        print()
        print("  Declared grouped uses (`grouped_word_from_chains`). Each is a")
        print("  visible choice, not a defect — but converting an A/B site here")
        print("  is only correct where the LEGACY frame is the object under")
        print("  study. Converting one that wanted the canonical word launders")
        print("  the defect and drains the ratchet for nothing:")
        for f in sorted(e, key=_key):
            print(f"  [E] {f['path']}:{f['line']}")
    if fixed:
        print()
        print(f"  {len(fixed)} baseline sites no longer fire — run with "
              f"--rebaseline to lower the ratchet.")
    if new or c or not ok_d or st:
        print()
        print("  FIX AT THE SITE. Call "
              "`pyhecke.atom.nucleon_word_letters(quarks, intra_order=…)` and "
              "place each letter at `3*k + off`. If the legacy word is what "
              "you want, ask for it by name — `intra_order=\"grouped\"` is not "
              "flagged. Widening the baseline is not a fix.")
    return 1 if (new or c or not ok_d or st) else 0


if __name__ == "__main__":
    sys.exit(main())
