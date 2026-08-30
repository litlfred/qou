#!/usr/bin/env python3
"""Find consumers that read a PIN-STAMPED artifact and never reconcile its pin.

THE DEFECT.  A producer resolves a runtime q₀ (muon or proton, per
`q0_anchor_manifest.json`) and separately loads a table or cache that was
built at ONE fixed pin. Combining the two is a layer straddle — exactly what
AGENTS.md forbids under "never straddle the two layers inside one quantity".

WHY THIS AUDIT EXISTS ALONGSIDE `cached_accessor_shape_audit.py`.  That one
looks for the GUARDED shape: *"an `if` whose test"* compares the caller's q to
the cache's q, which is trivially satisfied when the caller passes the package
constant. It is a good audit and it is not this one. Measured on `main`
2026-08-30, it reports **2 hits, both the dead
`_y_lambda_at_convention_C_HISTORICAL` and its generated mirror**, and **zero**
of the two live straddles found that week:

    block_swap_binding            6e1009bed8   χ at muon, y_λ from the proton
                                               default — 18 ppb, the μ–p tension
    canonical_tr_m_via_chi_cache  93888aa431   χ from a PROTON-pinned cache with
                                               muon-pinned y_λ — 7.8e-8 on the
                                               proton, 2.9e-7 at ⁴He, and THE
                                               SOLE REASON L1 (1 ppQ) READ RED

Neither has an `if` to find. They read the default, or the cache, with no
comparison at all. So the existing audit detects the form that at least checks
something and is structurally blind to the form that checks nothing — the
detector is looking for a gate, and the defect is the absence of one.

WHAT THIS FLAGS.  A module that does all three:

  1. resolves a RUNTIME pin  (`Q_50_DIGIT_STR`, `q_parameter.Q`, `q_at`, …)
  2. loads a PIN-STAMPED artifact — a call to any function whose body READS A
     FILE (derived from the definitions, not from a name list)
  3. and NEVER reconciles them — the runtime pin is not passed into the loader,
     and no comparison mentions both a pin name and a stamp name

AND THEN MEASURES IT.  Stage 1 above is a shape analysis and returns a
high-recall candidate list. Stage 2 reads the two numbers off disk —
`q0_anchor_manifest.json` says which anchor a producer's stem resolves to, and
every pin-stamped artifact records the q₀ it was built at — and reports the
candidates where those two actually disagree. That is a measured mismatch, not
a suspicious shape.

Measured on `main` 2026-08-30: 130 shape candidates, **4 measured mismatches**,
all four hand-verified. Three of the four load an artifact whose proton twin
already exists beside it on disk (`atomic-tr-m-mpfr-50dps-proton.witness.json`,
`y-lambda-mpfr-proton-witness.json`), and a sibling module of one of them
(`tr_m_q_hecke_seminormal.py:103`) already selects between the two by anchor.

HIGH RECALL, BY DESIGN.  A hit is a CANDIDATE, not a verdict: a module may
reconcile in a way this cannot see, or may legitimately want a fixed-pin
artifact (a two-pin comparison producer reads both ON PURPOSE — see
`mu_substrate_tension_audit_100dps`). Read each one. What the audit buys is
that the list is short and every entry has a specific question attached.

WHAT IT DOES NOT SEE.  Stage 1's loader set is name-keyed, so a loader name
that is also used for a non-loader anywhere in the tree is dropped (`main` is
defined ~900 times and one of those reads a witness back). Stage 2 resolves
artifact filenames from string constants, so a path assembled entirely from
variables is invisible, and it cannot tell a constant that is READ from one
that is merely mentioned or written — the `_anchor_keyed` / fragment-length
gates exist because each of those produced a hand-verified false positive.

Exit 0 always — this reports, it does not gate. Flipping it to blocking needs
the candidate list triaged to zero first, per the pattern in
`scripts/precision-gates.sh`.
"""
from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
ROOT = _HERE.parent.parent

#: Names that resolve a RUNTIME pin — what the producer is actually computing at.
RUNTIME_PIN = {"Q_50_DIGIT_STR", "Q_MUON_50_DIGIT_STR", "q_at", "q_muon_at",
               "Q_MP", "Q", "Q_0_FLOAT", "Q0", "q_0"}

#: Seed loaders — file-reading functions whose returned artifact carries a pin.
#: The full set is DERIVED, not curated (see `derive_pinned_loaders`): a curated
#: list was tried first and was wrong in four of six entries. It listed
#: `y_lambda_at` and `y_lambda_at_q0_mpmath`, neither of which reads a file at
#: all — both compute from the caller's `q_val`, so neither can straddle — and
#: the resulting scan reported 77 candidates of which ~65 were that one mistake.
#: AGENTS.md records the same error made the same way (a `y_lambda_at` entry in
#: `q0_producer_pin_classifier`'s MUON_ARTIFACTS reclassified 56 producers on an
#: association the code no longer has). A name list encodes a belief about a
#: function; reading the function encodes the function.
SEED_LOADERS: set[str] = set()

#: Fields a pin-stamped artifact records its own pin under. Recognised ONLY as
#: a dict-key ACCESS (`d.get("q0Value")`, `d["q_0"]`) — never as a bare name.
#: `q_0` is both a common local for the runtime pin and a common stamp key, so
#: a name-level test makes `if q_0 > x` satisfy "mentions a pin" and "mentions
#: a stamp" at once and clears every module that touches q_0 at all. That is
#: not hypothetical: it cleared instance B pre-fix on the first attempt here.
#: Dict keys under which an artifact records the q0 it was BUILT AT.
#:
#: ``"q"`` looks dangerously generic and is not. Measured on live
#: ``computations/`` (excluding ``_deprecated``): **5** ``.get("q")`` call
#: sites exist in the entire tree, and all five read a pin stamp off a loaded
#: artifact table — `y_lambda_symbolic_validate` x2, `y_lambda_macdonald_telescope`,
#: `muon_pin_three_values_probe`, and this file's own docstring. Zero false
#: positives at a hand-checked 5/5, against a real false NEGATIVE it was
#: causing: `y-lambda-mpfr-witness.json` stamps each per-n table with exactly
#: this key (`{"n", "num_partitions", "q", "z", "dps", "weights"}`), so every
#: consumer that correctly reconciles against it was invisible.
STAMP_KEYS = {"q0Value", "q_0", "q0", "anchor", "q0_value", "q_0_50dps", "q"}

#: Keyword names that hand the runtime pin DOWN into a loader.
PIN_KWARGS = {"q_str", "q0", "q_0", "q", "q0_str"}


def _calls(tree: ast.Module) -> list[ast.Call]:
    return [n for n in ast.walk(tree) if isinstance(n, ast.Call)]


def _call_name(node: ast.Call) -> str:
    f = node.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return ""


def _all_names(tree: ast.AST) -> set[str]:
    out: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Name):
            out.add(n.id)
        elif isinstance(n, ast.Attribute):
            out.add(n.attr)
        elif isinstance(n, ast.Constant) and isinstance(n.value, str):
            out.add(n.value)
    return out


#: Calls that read a file from disk / that write one.
_FILE_READS = {"load", "loads", "read_text", "read_bytes"}
_FILE_WRITES = {"dump", "dumps", "write_text", "write_bytes", "write"}


def _is_loader_def(fn: ast.AST) -> bool:
    """A function that READS an artifact off disk and hands it back.

    Three gates, all needed, each one bought by a false positive:

    * reads a file — the property that makes a straddle possible at all. A
      function computing from a `q` argument returns the pin the caller asked
      for and cannot straddle (`y_lambda_at`, `y_lambda_at_q0_mpmath`).
    * writes nothing — `save()` in `block_swap_binding` touches the same
      witness JSON and is not a loader.
    * returns a value — a `main()` that reads its own witness back is a driver,
      not a loader, and sweeping drivers in makes every producer a candidate.

    Deliberately NOT transitive. A one-hop closure was tried and it promoted
    `main` and the module's own top-level compute function to "loaders", at
    which point the audit flags every module for calling itself.
    """
    reads = writes = False
    returns_value = False
    for n in ast.walk(fn):
        if isinstance(n, ast.Call):
            name = _call_name(n)
            if name in _FILE_READS:
                reads = True
            elif name in _FILE_WRITES:
                writes = True
            elif name == "open":
                mode = "".join(a.value for a in n.args[1:]
                               if isinstance(a, ast.Constant) and isinstance(a.value, str))
                (writes := True) if ("w" in mode or "a" in mode) else (reads := True)
        elif isinstance(n, ast.Return) and n.value is not None:
            if not (isinstance(n.value, ast.Constant) and n.value.value in (0, 1, None)):
                returns_value = True
    return reads and not writes and returns_value


#: Regexes for a pin stamp as it appears in a witness/cache JSON on disk.
_STAMP_RE = re.compile(r'"(q0Value|q_0|q0|q0_value|anchor|q_0_50dps)"\s*:')


def _json_index(root: Path) -> dict[str, list[Path]]:
    idx: dict[str, list[Path]] = {}
    for f in root.rglob("*.json"):
        idx.setdefault(f.name, []).append(f)
    return idx


def _module_reads_stamped_json(tree: ast.Module, idx: dict[str, list[Path]],
                               memo: dict[Path, bool]) -> bool:
    """Does this module name a JSON that CARRIES A PIN STAMP on disk?

    This is the "PIN-STAMPED" half of the premise, and leaving it unenforced
    was worth 171 candidates against 24. A loader reading an ordering cache, a
    GS checkpoint or a symbolic net is a file reader that cannot straddle,
    because the artifact has no pin to disagree with. Rather than guess from
    the loader's shape, open the file and look: a stamp key present in the
    committed artifact is evidence; a name that sounds like a cache is not.
    """
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Constant) and isinstance(n.value, str)):
            continue
        if not n.value.endswith(".json"):
            continue
        # Suffix, not basename: a path built by f-string leaves only its tail
        # as a literal (`f"chi-{atom}-h{n}-at-q0-50dps.witness.json"` gives
        # `-at-q0-50dps.witness.json`), and an exact-basename match found
        # nothing for exactly the caches this audit exists to follow.
        frag = n.value.rsplit("/", 1)[-1].lstrip("-_")
        for cand in idx.get(frag, []) or [f for names, fs in idx.items()
                                          for f in fs if names.endswith(frag)]:
            if cand not in memo:
                try:
                    memo[cand] = bool(_STAMP_RE.search(
                        cand.read_text(errors="ignore")[:200_000]))
                except Exception:                          # noqa: BLE001
                    memo[cand] = False
            if memo[cand]:
                return True
    return False


def derive_pinned_loaders(paths: list[Path]) -> set[str]:
    """Function names that return an artifact READ FROM DISK.

    Derived from the definitions, not curated. A curated list was tried first
    and was wrong in four of six entries — see SEED_LOADERS.

    A name qualifies only if EVERY definition of it is a loader. `main` is
    defined ~900 times here and one of those reads a witness back and returns
    it; without this, every module was a candidate for calling its own `main`.
    """
    idx = _json_index(ROOT / "computations")
    memo: dict[Path, bool] = {}
    loader: set[str] = set()
    other: set[str] = set()
    for p in paths:
        try:
            tree = ast.parse(p.read_text())
        except Exception:                                  # noqa: BLE001
            continue
        stamped = _module_reads_stamped_json(tree, idx, memo)
        for n in ast.walk(tree):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                (loader if (stamped and _is_loader_def(n)) else other).add(n.name)
    return (loader - other) | SEED_LOADERS


def _resolvable(tree: ast.Module) -> set[str]:
    """Names this module can actually call: defined here, or imported by name.

    Matching call sites to definitions by bare name across the whole tree is
    unsound and was measurably so: `hashlib.sha256(p.read_bytes())` and a
    file object's `.read()` both matched module-level `def`s of those names
    elsewhere in the corpus, and the candidate list went from 77 to 243 on
    that alone. A call is only evidence about a loader if this module could
    have reached that loader.
    """
    out: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out.add(n.name)
        elif isinstance(n, ast.ImportFrom):
            for a in n.names:
                out.add(a.asname or a.name)
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.asname:
                    out.add(a.asname)
    return out


def _reads_stamp(node: ast.AST) -> bool:
    """True if `node` contains a dict-key access naming a pin stamp."""
    for n in ast.walk(node):
        if isinstance(n, ast.Call) and _call_name(n) == "get":
            for a in n.args:
                if isinstance(a, ast.Constant) and a.value in STAMP_KEYS:
                    return True
        elif isinstance(n, ast.Subscript):
            s = n.slice
            if isinstance(s, ast.Constant) and s.value in STAMP_KEYS:
                return True
    return False


def _stamp_derived(tree: ast.Module) -> set[str]:
    """Names bound from an artifact's own pin stamp.

    The guard that fixed instance B reads ``_cache_q0 = numerical.get("q0Value")``
    and then compares ``_cache_q0`` to the runtime pin. The comparison itself
    never mentions ``q0Value``, so a reconciliation test keyed on the literal
    field name cannot see it. Bind the name at the extraction site instead.

    A COMPREHENSION counts as an extraction site too. `y_lambda_symbolic_validate`
    collects its stamps as `recorded = [t.get("q") for t in tables.values() ...]`
    and compares against `recorded`'s elements; an assignment-only walk sees the
    `Assign` but its value is a `ListComp`, so the `.get` is reached — the case
    that needed adding is the loop variable, which is bound by a `comprehension`
    node rather than by an `Assign` at all.
    """
    out: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AnnAssign)) and n.value is not None:
            if not _reads_stamp(n.value):
                continue
            targets = n.targets if isinstance(n, ast.Assign) else [n.target]
        elif isinstance(n, ast.comprehension):
            if not _reads_stamp(n.iter) and not any(_reads_stamp(i) for i in n.ifs):
                continue
            targets = [n.target]
        elif isinstance(n, ast.For):
            if not _reads_stamp(n.iter):
                continue
            targets = [n.target]
        else:
            continue
        for t in targets:
            for sub in ast.walk(t):
                if isinstance(sub, ast.Name):
                    out.add(sub.id)
    return out


def _pin_derived(tree: ast.Module) -> set[str]:
    """Names bound from the RUNTIME PIN — the mirror of :func:`_stamp_derived`.

    That function exists because *"the comparison itself never mentions
    ``q0Value``, so a reconciliation test keyed on the literal field name
    cannot see it."* The identical argument applies to the other operand and
    was never made, so RECONCILIATION 2 tracked derivation on one side of the
    comparison and demanded a literal on the other.

    The cost was not hypothetical: it is blind to the fix pattern this audit's
    own findings recommend. Both straddles closed under `qou-y313` bind the pin
    to a local first —

        want = mp.mpf(Q_50_DIGIT_STR)          # ← the only mention of the pin
        ...
        if abs(mp.mpf(str(q_rec)) - want) < mp.mpf("1e-40"):

    — and the `Compare` node names `want`, `q_rec`, `abs`, `mp`, `str`, but not
    `Q_50_DIGIT_STR`. Measured: `atomic_tr_m_helium4` and
    `y_lambda_symbolic_validate` were both **still flagged after being
    correctly fixed and their witnesses regenerated to the right layer**. A
    detector that cannot see its own remedy can never be triaged to zero, which
    is the stated precondition for making this gate blocking.

    **One hop is not enough, and that was measured rather than assumed.** The
    first version of this stopped at a single assignment and still left
    `y_lambda_symbolic_validate` flagged, because that module aliases the pin at
    module level and then converts it inside the loader:

        Q0_STR = Q_50_DIGIT_STR        # hop 1  — caught by one hop
        ...
        want = mp.mpf(Q0_STR)          # hop 2  — NOT caught

    So this iterates to a fixed point over assignments. It is still assignments
    only — no arguments, no attributes, no returns.

    **Why growing this side is safe, and what actually guards the predicate.**
    A larger pin side cannot on its own clear anything, because the *other*
    operand must still be the artifact's own stamp (`sub & stamped` or
    `_reads_stamp`). That is the half instance B pre-fix fails: it compares the
    runtime pin against `_q0_value_for_anchor("muon")`, a check on the PIN
    involving **no artifact stamp at all**, and it must keep failing however
    many names the pin side acquires. It does, and `--selftest` fails if it
    stops.

    **The residual risk, stated rather than waved at:** a `Compare` that
    mentions a pin-derived name and a stamp-derived name without being a
    reconciliation would now clear. That is a false negative this trades for
    the false positives above, and it is the reason stage 2 exists — stage 2
    reads both numbers off disk and never consults this predicate at all.
    """
    out: set[str] = set()
    changed = True
    while changed:                       # fixed point: aliases of aliases
        changed = False
        for n in ast.walk(tree):
            if not isinstance(n, (ast.Assign, ast.AnnAssign)) or n.value is None:
                continue
            if not (_all_names(n.value) & (RUNTIME_PIN | out)):
                continue
            targets = n.targets if isinstance(n, ast.Assign) else [n.target]
            for t in targets:
                for sub in ast.walk(t):
                    if isinstance(sub, ast.Name) and sub.id not in out:
                        out.add(sub.id)
                        changed = True
    return out


def analyse(src: str, label: str, loaders: set[str]) -> tuple[bool, str]:
    """Return (is_candidate, reason).

    Reconciliation is judged PER LOADER CALL, not per module. A module that
    pins one artifact correctly and reads a second one blind is exactly the
    live defect (instance B: ``y_lambda_at(n, q_0)`` takes the runtime pin
    while ``_load_chi_cache(...)`` beside it takes nothing), so a module-wide
    "it reconciles somewhere" test clears the very case this exists to catch.
    """
    try:
        tree = ast.parse(src)
    except SyntaxError as exc:
        return False, f"unparseable: {exc}"

    names = _all_names(tree)
    pins = names & RUNTIME_PIN
    if not pins:
        return False, "no runtime pin"

    callable_here = loaders & _resolvable(tree)
    loader_calls = [c for c in _calls(tree)
                    if isinstance(c.func, ast.Name) and c.func.id in callable_here]
    if not loader_calls:
        return False, "no pinned-artifact loader"

    # RECONCILIATION 1 (per call) — the runtime pin is handed INTO this loader.
    unpinned: list[ast.Call] = []
    for c in loader_calls:
        passed = _all_names(ast.Module(body=[ast.Expr(a) for a in c.args],
                                       type_ignores=[]))
        pinned = bool(passed & RUNTIME_PIN)
        for kw in c.keywords:
            if kw.arg in PIN_KWARGS or (_all_names(kw.value) & RUNTIME_PIN):
                pinned = True
        if not pinned:
            unpinned.append(c)
    if not unpinned:
        return False, ("reconciled: every pinned-artifact load receives the "
                       "runtime pin")

    # RECONCILIATION 2 (module-wide) — a comparison against the ARTIFACT'S OWN
    # stamp, either the literal field name or a name bound from it.
    #
    # There is deliberately no "calls a reconciler helper" escape here. Instance
    # B pre-fix calls `_q0_value_for_anchor("muon")` to check that its runtime
    # q_0 matches a known anchor — a check on the PIN, involving no artifact
    # stamp at all — and an audit that accepted that as reconciliation cleared
    # the straddle it was written to find.
    stamped = _stamp_derived(tree)
    pin_side = RUNTIME_PIN | _pin_derived(tree)
    for n in ast.walk(tree):
        if isinstance(n, (ast.Compare, ast.If)):
            sub = _all_names(n)
            if (sub & pin_side) and ((sub & stamped) or _reads_stamp(n)):
                return False, ("reconciled: compares the runtime pin against "
                               "the artifact's own pin stamp")

    where = sorted({f"{_call_name(c)}:{c.lineno}" for c in unpinned})
    return True, (f"resolves {sorted(pins)[0]}; {len(unpinned)} pinned-artifact "
                  f"load(s) receive no pin and nothing compares against their "
                  f"stamp — {', '.join(where[:3])}")


def _sources() -> list[Path]:
    out = []
    for p in sorted((ROOT / "computations").rglob("*.py")):
        rel = str(p.relative_to(ROOT))
        if "_deprecated" in rel or "qou-mass" in rel:
            continue
        out.append(p)
    return out


def scan() -> list[tuple[str, str]]:
    loaders = derive_pinned_loaders(_sources())
    hits: list[tuple[str, str]] = []
    for p in sorted((ROOT / "computations").rglob("*.py")):
        rel = str(p.relative_to(ROOT))
        if "_deprecated" in rel or "/audits/" in rel or "qou-mass" in rel:
            continue
        try:
            src = p.read_text()
        except Exception:                                  # noqa: BLE001
            continue
        ok, why = analyse(src, rel, loaders)
        if ok:
            hits.append((rel, why))
    return hits


def selftest() -> int:
    """Prove the audit flags BOTH known straddles at their pre-fix revisions.

    A detector that has never fired on a real defect is not evidence. These two
    are the instances the existing shape audit misses, so if this one does not
    flag them it adds nothing. SKIP loudly (exit 2) if a revision is unreachable
    — an unrunnable self-test must not read as a passing one.
    """
    cases = [
        ("9ba8da4b28", "computations/block_swap_binding.py", "A: y_λ default vs muon χ"),
        ("1ee64005eb", "computations/canonical_tr_m_via_chi_cache.py", "B: proton cache vs muon y_λ"),
    ]
    loaders = derive_pinned_loaders(_sources())
    print("SELF-TEST — must flag both known pre-fix straddles")
    rc = 0
    for rev, path, desc in cases:
        try:
            src = subprocess.check_output(["git", "show", f"{rev}:{path}"],
                                          cwd=str(ROOT), stderr=subprocess.DEVNULL).decode()
        except Exception as exc:                           # noqa: BLE001
            print(f"  SKIP {desc} — cannot reach {rev} ({type(exc).__name__}). "
                  f"NOT a pass; unverified in this clone.")
            rc = max(rc, 2)
            continue
        ok, why = analyse(src, path, loaders)
        print(f"  {'FLAGGED' if ok else 'MISSED '} {desc}\n      {why}")
        if not ok:
            rc = 1
    # And the post-fix versions must NOT be flagged, or the audit never clears.
    for path, desc in [("computations/block_swap_binding.py", "A post-fix"),
                       ("computations/canonical_tr_m_via_chi_cache.py", "B post-fix")]:
        ok, why = analyse((ROOT / path).read_text(), path, loaders)
        print(f"  {'STILL FLAGGED' if ok else 'clear       '} {desc}\n      {why}")
        if ok:
            rc = 1
    print("  PASS" if rc == 0 else f"  rc={rc}")
    return rc



# --------------------------------------------------------------------------
# STAGE 2 — measure, don't guess.
#
# Stage 1 is a shape analysis and returns a high-recall candidate list. But
# both halves of a straddle are recorded on disk: `q0_anchor_manifest.json`
# says which anchor a producer's stem resolves to, and every pin-stamped
# artifact carries the q₀ it was built at. So for a candidate we can read the
# two numbers and compare them, and report a MEASURED mismatch rather than a
# suspicious shape. That is the difference between "this module has no guard"
# and "this module computes at the muon pin from a proton-built table".
# --------------------------------------------------------------------------

_Q0_PREFIX = 14   # muon 1.1099785956…, proton 1.1099785827… diverge at digit 10

#: Artifacts whose pin DISAGREEING with the reader is correct, not a straddle.
#:
#: `q-pinning-50-digit.witness.json` is the ANCHOR-DEFINING witness — it holds
#: the muon 50-digit string BY DEFINITION and is what
#: `witness._q0_value_for_anchor("muon")` reads. AGENTS.md rule 1 of the
#: migration authorisation forbids re-pinning it; a proton producer that names
#: it is reading the muon anchor's definition, which is the only way to read
#: it. Counting that as a mismatch made it the single largest class here (11
#: of 33) and every one was correct.
#:
#: `_deprecated/` artifacts are not live compute.
ARTIFACT_EXEMPT_NAMES = {"q-pinning-50-digit.witness.json"}
ARTIFACT_EXEMPT_DIRS = ("/_deprecated/",)

#: Producers that read BOTH pins on purpose. AGENTS.md names these three as
#: refusing a proton-only run by design: a dual-layer emitter, an assertion on
#: the anchor-defining witness, and an L1 cross-check that must run at muon.
#: A two-pin comparison producer reads the other layer deliberately — see
#: `mu_substrate_tension_audit_100dps`.
#: A stem containing one of these reads both pins as its subject matter — a
#: cross-anchor probe validating a verdict at the other anchor is doing exactly
#: what it says. Verified on `qbeta_singularity_cross_anchor_probe`, which
#: states in its first paragraph that it re-runs Step 1 at q_muon on purpose.
DUAL_PIN_STEM_MARKERS = ("cross_anchor", "crossanchor", "anchor_swing",
                         "anchor_consistency", "mu_substrate_tension",
                         "muon_vs", "_repin_", "pin_classifier")

DUAL_PIN_BY_DESIGN = {"atomic_tr_m_mpfr_50dps", "he4_stage2_ranking_seminormal_xcheck",
                      "cross_check_trM_1ppb", "mu_substrate_tension_audit_100dps",
                      "q0_repin_regen_batch", "q0_repin_sweep",
                      "witness_constant_staleness", "q0_anchor_gate_test",
                      "q_pinning_50_digit", "regenerate_y_lambda_mpfr"}


def _anchor_values() -> dict[str, str]:
    sys.path.insert(0, str(ROOT / "computations"))
    sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
    from qou_substrate.witness import _q0_value_for_anchor      # noqa: PLC0415
    return {a: str(_q0_value_for_anchor(a) or "") for a in ("muon", "proton")}


def _stem_anchor(stem: str) -> str:
    man = json.loads((ROOT / "computations" / "q0_anchor_manifest.json").read_text())
    if stem in man.get("ideal_muon", []):
        return "muon"
    if stem in man.get("ambiguous", []):
        return "ambiguous"
    return "proton"


def _artifact_pin(path: Path) -> str | None:
    """The q₀ a pin-stamped artifact records, as a string, if it records one."""
    try:
        txt = path.read_text(errors="ignore")
    except Exception:                                      # noqa: BLE001
        return None
    m = re.search(r'"(?:q0Value|q_0_50dps|q0_value|q_0)"\s*:\s*"?'
                  r'(1\.10997[0-9]*)', txt)
    return m.group(1) if m else None


def _consumed_at_artifact_q(tree: ast.Module) -> bool:
    """Does the module take q FROM the artifact it loaded?

    The seventh false-positive mechanism, and the subtlest: a module can pin
    proton, load a muon-built table, and be entirely correct — because it reads
    the artifact's OWN recorded q and evaluates there.
    `y_lambda_macdonald_telescope.cross_check_mpfr` does exactly that
    (`q_val = mp.mpf(table.get("q") or ...)`), so it is checking the witness
    against the closed form at the witness's own pin. Nothing straddles.

    That is reconciliation by USING the artifact's pin rather than comparing
    against it, and stage 2's "producer anchor != artifact stamp" test cannot
    tell the two apart — it reported this module as a straddle and the claim
    reached a PR body and a bean before the consumer was read. Hence: a `q`-ish
    key read out of loaded data is evidence the module anchors to the artifact.

    Its sibling reader `y_lambda_symbolic_validate` does NOT do this — it drops
    the witness's `q` at load and compares against the Wenzl bridge evaluated
    at its own runtime pin — and stays flagged. The two read the same file and
    only one of them straddles.
    """
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and _call_name(n) == "get":
            for a in n.args:
                if isinstance(a, ast.Constant) and a.value in ("q", "q0", "q_0"):
                    return True
        elif isinstance(n, ast.Subscript):
            sl = n.slice
            if isinstance(sl, ast.Constant) and sl.value in ("q", "q0", "q_0"):
                return True
    return False


#: Coefficient-like symbolic content: a polynomial in a variable, not a number.
_SYMBOLIC_RE = re.compile(r'"[^"]*\*\*?[a-z][^"]*"')


def _payload_is_pin_independent(path: Path, memo: dict[Path, bool]) -> bool:
    """True if the artifact's DATA cannot depend on the pin it is stamped with.

    THE EIGHTH FALSE-POSITIVE MECHANISM, and the first where I nearly changed
    correct code to satisfy this audit.

    `habiro-coefficients-extended.witness.json` carries a top-level q₀ stamp
    and was flagged as a muon artifact read by a proton producer. But its
    payload is a SYMBOLIC Habiro expansion — `a_m` entries like `"768"`,
    `"-35712*u - 35712"`, `"491861*u**2 + 503768*u + 515411"`, with
    `all_integral: true` — and the rows contain no q stamp at all. The
    consumer evaluates it at `u₀ = q₀^{1/2}` from its OWN runtime pin, so
    reading it at the proton pin is correct.

    The stamp records the run that PRODUCED the symbolic object, not a frame
    the data lives in. Stage 2 compares producer-anchor to artifact-stamp and
    cannot tell pin-STAMPED from pin-DEPENDENT; that distinction is what this
    restores.

    The test is evidence, not a name list: symbolic coefficient strings in the
    payload. It is deliberately narrow — a numeric artifact that merely
    happens to contain one such string will not match, and a symbolic artifact
    whose consumer nonetheless needs the stamp will be wrongly exempted. If
    that second case appears, tighten HERE rather than adding the producer to
    an allow-list, which would hide the reason.
    """
    if path not in memo:
        try:
            txt = path.read_text(errors="ignore")[:400_000]
            memo[path] = bool(_SYMBOLIC_RE.search(txt)) and '"all_integral"' in txt
        except Exception:                                  # noqa: BLE001
            memo[path] = False
    return memo[path]


def _anchor_keyed(tree: ast.Module) -> set[str]:
    """Filename constants that sit under an anchor key in a dict literal.

    ``_Y_LAMBDA_BY_ANCHOR = {"muon": HERE / "y-lambda-mpfr-witness.json",
                             "proton": HERE / "y-lambda-mpfr-proton-witness.json"}``
    is the CORRECT two-layer shape: the module holds both tables and picks by
    anchor. Counting the muon entry as a mismatch because the module pins
    proton inverts the verdict — it flags the one construction that cannot
    straddle. Verified by hand on `tr_m_wenzl_bridge_mpfr.py:67`.
    """
    out: set[str] = set()
    # A ternary is the same construction spelled differently:
    #     _REF_NAME = ("...-proton.witness.json" if anchor == "proton"
    #                  else "...witness.json")
    # `tr_m_q_hecke_seminormal.py:103` picks its reference witness this way and
    # was flagged for holding the muon name at all. Two .json literals inside
    # one IfExp are alternatives, not a straddle.
    for n in ast.walk(tree):
        if isinstance(n, ast.IfExp):
            lits = [c.value for c in ast.walk(n)
                    if isinstance(c, ast.Constant) and isinstance(c.value, str)
                    and c.value.endswith(".json")]
            if len(lits) >= 2:
                out.update(lits)
    for n in ast.walk(tree):
        if not isinstance(n, ast.Dict):
            continue
        for k, v in zip(n.keys, n.values):
            if not (isinstance(k, ast.Constant) and k.value in ("muon", "proton")):
                continue
            for sub in ast.walk(v):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                    out.add(sub.value)
    return out


def measure(hits: list[tuple[str, str]]) -> list[tuple[str, str, str, str]]:
    """For each candidate, compare its producer's anchor to its artifacts'."""
    anchors = _anchor_values()
    idx = _json_index(ROOT / "computations")
    sym_memo: dict[Path, bool] = {}
    out: list[tuple[str, str, str, str]] = []
    for rel, _why in hits:
        path = ROOT / rel
        stem = path.stem
        want = _stem_anchor(stem)
        if want == "ambiguous" or stem in DUAL_PIN_BY_DESIGN:
            continue
        if any(mk in stem for mk in DUAL_PIN_STEM_MARKERS):
            continue
        want_val = anchors[want][:_Q0_PREFIX]
        try:
            tree = ast.parse(path.read_text())
        except Exception:                                  # noqa: BLE001
            continue
        if _consumed_at_artifact_q(tree):
            continue
        seen: set[Path] = set()
        keyed = _anchor_keyed(tree)
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Constant) and isinstance(n.value, str)):
                continue
            if not n.value.endswith(".json") or n.value in keyed:
                continue
            frag = n.value.rsplit("/", 1)[-1].lstrip("-_")
            cands = idx.get(frag, [])
            if not cands:
                # Suffix match, but only for a SPECIFIC tail. The f-string
                # `f"chi-{atom}-h{n}-at-q{_tag}-50dps.witness.json"` leaves the
                # literal `-50dps.witness.json`, which suffix-matches dozens of
                # unrelated witnesses — that is how `chi_at_q0_via_hoefsmit_mpfr`
                # came to be reported as loading `atomic-tr-m-mpfr-50dps`, an
                # artifact it never touches (and the constant was an OUTPUT
                # path). A tail must be long and near-unique to identify one.
                if len(frag) < 24:
                    continue
                cands = [f for names, fs in idx.items()
                         for f in fs if names.endswith(frag)]
                if len(cands) > 3:
                    continue
            for c in cands[:40]:
                if c in seen:
                    continue
                seen.add(c)
                cs = str(c)
                if c.name in ARTIFACT_EXEMPT_NAMES or \
                        any(d in cs for d in ARTIFACT_EXEMPT_DIRS):
                    continue
                if _payload_is_pin_independent(c, sym_memo):
                    continue
                got = _artifact_pin(c)
                if got and got[:_Q0_PREFIX] != want_val:
                    other = "muon" if want == "proton" else "proton"
                    out.append((rel, want, str(c.relative_to(ROOT)), other))
    return out


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    hits = scan()
    print("=" * 72)
    print("STAGE 1 — consumers loading a pin-stamped artifact with NO reconciliation")
    print("=" * 72)
    for rel, why in hits:
        print(f"  {rel}\n      {why}")
    print(f"\n  shape candidates: {len(hits)}   (high recall — each needs a verdict)")

    print("\n" + "=" * 72)
    print("STAGE 2 — MEASURED pin mismatch (producer anchor vs artifact stamp)")
    print("=" * 72)
    try:
        measured = measure(hits)
    except Exception as exc:                               # noqa: BLE001
        print(f"  unavailable: {type(exc).__name__}: {exc}")
        return 0
    by_mod: dict[str, list[tuple[str, str, str]]] = {}
    for rel, want, art, other in measured:
        by_mod.setdefault(rel, []).append((want, art, other))
    for rel, rows in sorted(by_mod.items()):
        print(f"  {rel}   pins {rows[0][0]}")
        for _want, art, other in rows[:4]:
            print(f"      loads {art}  (built at the {other} pin)")
    print(f"\n  measured mismatches: {len(by_mod)} module(s), "
          f"{len(measured)} artifact(s)")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
