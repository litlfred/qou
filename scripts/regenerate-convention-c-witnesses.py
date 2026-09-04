#!/usr/bin/env python3
"""Regenerate every witness still carrying a convention-C fingerprint.

The producers are all convention D (`convention-c-producer-audit.py` reports 0
actionable sites); their committed outputs are not. This closes that gap by
re-running each producer and recording exactly how far every number moved.

## Constraints this is built around

**Strictly serial.** Standing owner directive: never two producers concurrently
in one checkout. They share caches, witness paths and sys.path mutations.

**Resumable.** The container is ephemeral and has died mid-task twice at roughly
an hour each. One JSONL line is appended after *every* producer, and a resume
skips whatever is already recorded. A restart costs one producer, not the run.

**Nothing hand-edited.** Every number that lands in a witness comes from a
producer run. This script never writes into a witness itself.

## Reading the deltas

Three kinds of change come out of this and conflating them would make the report
meaningless:

* **structural zero** — a value that becomes exactly `0`. Under convention D
  every `y_λ` with `ℓ(λ) ≥ 3` vanishes identically; that is what the convention
  *is*, not a numerical shift, and reporting it as "−100 %" would be noise.
* **shift** — a genuine relative move. Reported in ppm. This is the physics.
* **q0-refresh** — a move at roughly the 9th significant digit with no
  convention content, from a witness that was simply stale against its q₀.
  Classified separately because a witness regenerated *before* its producer was
  migrated moves only this much and looks superficially like a result.

## Usage

    python3 scripts/regenerate-convention-c-witnesses.py --plan
    python3 scripts/regenerate-convention-c-witnesses.py --run [--timeout 900]
    python3 scripts/regenerate-convention-c-witnesses.py --report
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import signal
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parent.parent
LOG = REPO / ".work" / "convention-c-regen.jsonl"

#: Convention-C fingerprints, from the registry.
C_FINGERPRINTS = ["0.49932033418369", "0.41539579536", "0.2809296", "0.02274491"]

#: Fields that churn on every run and carry no numeric meaning.
VOLATILE = {"computedAt", "durationMs", "scriptHash", "commitSha",
            "scriptCommitSha", "engineVersion", "hostname", "elapsed",
            "elapsedMs", "timestamp", "generatedAt"}

NUM = re.compile(r"-?\d+\.\d{6,}(?:[eE][+-]?\d+)?")

#: Field names denoting a wall-clock measurement rather than a result.
#:
#: `VOLATILE` above is an exact-name set and covers the witness ENVELOPE
#: (`durationMs`, `elapsedMs`). It does not reach into `data`, where producers
#: name their own timings in snake_case and disagree about it: measured across
#: the witness tree there are `compute_time_sec` (183), `elapsed_sec` (34),
#: `wall_sec` (24), `milliseconds` (31), `rerun_seconds`, `compute_seconds`,
#: `elapsed_reduce_sec`, `y_lambda_load_time_sec`, `hutch_wall_sec`,
#: `t_dense_sec`, `mp_dps_runtime`, and more. Enumerating them is a losing game.
#:
#: Matching on the TIMING WORD (elapsed / wall / duration / runtime / rerun /
#: *_time_sec / compute_sec* / milliseconds) rather than on a `_seconds$`
#: suffix is deliberate and the distinction matters in this repo: a bare
#: `_seconds$` rule would also swallow a physical quantity measured in seconds
#: -- a lifetime, a decay time -- and silently hide exactly the kind of number
#: this sweep exists to detect moving.
_TIMING_FIELD = re.compile(
    r"(?:^|[._])(?:elapsed|wall|duration|runtime|rerun)"
    r"|_time_sec"
    r"|compute_sec|compute_time"
    r"|^t_[a-z0-9_]*_sec$"
    r"|milliseconds",
    re.I)


def _is_timing_field(field: str) -> bool:
    """True for a wall-clock field. `field` is a dotted path, so test the leaf."""
    leaf = field.rsplit(".", 1)[-1]
    return bool(_TIMING_FIELD.search(leaf))

#: sys.path additions producers expect. ABSOLUTE, deliberately.
#:
#: These were relative on the first run ("..", "../tools/pyhecke/python"), which
#: is correct only for a producer sitting directly in `computations/`. Each
#: producer runs from its OWN directory, so for `computations/alpha/foo.py` the
#: entry `../tools/pyhecke/python` resolved to `computations/tools/...` and the
#: producer died with `ModuleNotFoundError: No module named 'pyhecke'`. Four
#: failures were the harness's fault, not the producer's — which is exactly the
#: kind of thing that would otherwise be written up as "pre-existing breakage".
SYS_PATHS = [str(REPO / "computations" / d) if d else str(REPO / "computations")
             for d in ("", "substrate", "hecke", "markov", "alpha", "probes",
                       "qbeta", "deltalambda", "phase5", "sweeps", "audits")] + [
    str(REPO / "tools" / "pyhecke" / "python"),
    str(REPO / "tools" / "qou-substrate" / "python"),
    str(REPO / "qou-mass" / "src"),
]


#: Producers that take required positional arguments.
#:
#: The harness invokes every producer bare, which is right for the ~50 that
#: write their witness on import-and-run. A few instead take the object to
#: compute as argv and exit 2 on argparse before doing anything. That reads in
#: the journal as a producer failure, which it is not — the atom is simply not
#: recoverable from the witness path by the resolver.
#:
#: Keyed by producer path, valued by the argv that regenerates exactly the
#: in-scope witnesses. For `per_irrep_pole_atom` those are
#: `per-irrep-pole-proton-h3` and `per-irrep-pole-deuteron-h6`, so the atoms
#: are `proton` and `deuteron` and no others — passing the full ATOMS list
#: would rewrite six witnesses this campaign has not audited.
#:
#: A LOUD under-run is only half the problem, and the quiet half is worse.
#: `chi_at_q0_via_hoefsmit_mpfr.py` takes `atoms` as OPTIONAL, defaulting to
#: `["tritium", "helium-3"]` — two of the SIX witnesses it owns. Bare
#: invocation exits 0 having regenerated a third of its output, the harness
#: records `ok`, and the four untouched witnesses stay convention C while the
#: report implies the producer was covered. That is the exact failure mode
#: this campaign was reopened to eliminate, so it is tabled here too.
#:
#: `--fresh` on the chi producer is not optional. Its symbolic cache IS the
#: `chi-{atom}-h{n}.witness.json` it writes (module docstring), and the resume
#: check compares only the stored q0 — it has no notion of convention. Without
#: `--fresh` the producer resumes from precisely the convention-C data this
#: pass exists to replace, and reports success.
_ATOM_NAMES = ("beryllium-9", "beryllium-8", "lithium-7", "lithium-6",
               "lithium-5", "helium-4", "helium-3", "deuteron", "tritium",
               "neutron", "proton")


def _atoms_from_witnesses(witnesses):
    """Atom names implied by the witnesses a producer owns, in ATOMS order.

    Derived rather than hardcoded, so adding a witness extends the invocation
    automatically instead of silently falling outside a fixed list.
    """
    return [name for name in _ATOM_NAMES
            if any(name in pathlib.Path(w).name for w in witnesses)]


#: Values are either a static argv list or a callable taking the witnesses the
#: producer owns and returning argv. Keyed by BASENAME, so a producer that
#: moves between directories keeps its entry.
PRODUCER_ARGV = {
    "per_irrep_pole_atom.py": _atoms_from_witnesses,
    "chi_at_q0_via_hoefsmit_mpfr.py":
        lambda ws: _atoms_from_witnesses(ws) + ["--fresh"],
}


def producer_argv(producer: str, witnesses) -> list:
    """argv for `producer`, given the witnesses it owns in this run."""
    entry = PRODUCER_ARGV.get(pathlib.Path(producer).name)
    if entry is None:
        return []
    return list(entry(witnesses)) if callable(entry) else list(entry)


def numeric_fields(obj, out=None, path=""):
    """Flatten every high-precision number in a witness, keyed by JSON path."""
    out = {} if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in VOLATILE:
                continue
            numeric_fields(v, out, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            numeric_fields(v, out, f"{path}[{i}]")
    elif isinstance(obj, str):
        for m in NUM.findall(obj):
            out.setdefault(path, []).append(m)
    elif isinstance(obj, float):
        out.setdefault(path, []).append(repr(obj))
    elif isinstance(obj, int) and obj == 0:
        out.setdefault(path, []).append("0")
    return out


def snapshot(witness: pathlib.Path):
    try:
        raw = witness.read_text()
    except OSError:
        return {"exists": False}
    try:
        doc = json.loads(raw)
    except json.JSONDecodeError:
        doc = {}
    return {
        "exists": True,
        "sha256": hashlib.sha256(raw.encode()).hexdigest()[:16],
        "c_fingerprint": any(c in raw for c in C_FINGERPRINTS),
        "numbers": numeric_fields(doc),
    }


#: Below this a value is numerically indistinguishable from zero, so a RELATIVE
#: change against it is meaningless — dividing by something at the level of
#: machine noise manufactures astronomical ppm. The first draft of this report
#: led with "1.3e20 ppm" for 3.47e-18 -> 4.6e-4, which is not a physics result,
#: it is a division by epsilon.
NOISE_FLOOR = 1e-12


def classify(before: str, after: str):
    """Return (kind, relative_change) for one value.

    Kinds, and why each is kept separate:

    ``structural_zero``  became exactly 0. Convention D sends every ``y_lambda``
                         with ``ell(lambda) >= 3`` to zero identically; that is
                         the convention working, not a shift, and rendering it
                         as "-100%" would drown the real numbers.
    ``emerged``          was at or below the noise floor, now is not. A
                         quantity that was numerically zero acquiring a value is
                         a qualitative change and no ppm describes it.
    ``vanished``         the reverse: was real, now at the noise floor without
                         being exactly zero.
    ``noise``            both sides at the floor. Nothing happened.
    ``q0_refresh``       moved by less than 1e-7 relative, roughly the ninth
                         digit. No convention content -- a witness simply stale
                         against its q0. Kept separate because a witness
                         regenerated BEFORE its producer was migrated moves
                         exactly this much and looks like a result.
    ``timing``           a wall-clock measurement (see ``_is_timing_field``).
                         Moves on every run by whatever else the machine was
                         doing and says nothing about the computation's VALUES.
                         Classified rather than dropped: a producer that
                         suddenly takes 40x longer is worth seeing, it is just
                         not a numerical result.
    ``shift``            a genuine relative move, reported in ppm. The physics.
    """
    try:
        b, a = float(before), float(after)
    except ValueError:
        return ("unparseable", None)
    if b == a:
        return ("same", 0.0)
    if a == 0.0:
        return ("structural_zero", None)
    if abs(b) <= NOISE_FLOOR < abs(a):
        return ("emerged", None)
    if abs(a) <= NOISE_FLOOR < abs(b):
        return ("vanished", None)
    if abs(b) <= NOISE_FLOOR and abs(a) <= NOISE_FLOOR:
        return ("noise", None)
    rel = abs(a - b) / abs(b)
    if rel < 1e-7:                      # ~digit 8 and below
        return ("q0_refresh", rel)
    return ("shift", rel)


def diff(before: dict, after: dict):
    nb = before.get("numbers", {}) or {}
    na = after.get("numbers", {}) or {}
    rows = []
    for key in sorted(set(nb) | set(na)):
        xs, ys = nb.get(key, []), na.get(key, [])
        for i in range(max(len(xs), len(ys))):
            x = xs[i] if i < len(xs) else None
            y = ys[i] if i < len(ys) else None
            if x is None or y is None or x == y:
                continue
            kind, rel = classify(x, y)
            if kind == "same":
                continue
            # A wall-clock field is never physics, whatever its magnitude.
            # Checked AFTER classify so `rel` is still carried: a producer that
            # got 40x slower is worth seeing, it is just not a result.
            if _is_timing_field(key):
                kind = "timing"
            rows.append({"field": key, "before": x, "after": y,
                         "kind": kind, "rel": rel})
    return rows


def _is_convention_c(raw: str, doc) -> bool:
    """Is this witness convention C?

    TWO tests, because the first one is not sufficient and I shipped a campaign
    that assumed it was.

    1. **Fingerprint** — the witness contains a known convention-C decimal.
       Those constants are the `n = 3` values (`z_C` and the three `y_λ` at
       three strands), so this catches nothing computed at `n = 6`, `9` or `12`.

    2. **Structural** — the witness records a nonzero `y_λ` on a partition with
       three or more rows. Under convention D every such weight is *exactly*
       zero (Schur-Weyl on a two-dimensional fibre), so a nonzero one is
       convention C at any `n`, whatever numbers it happens to contain.

    Measured when test 2 was added: 46 witnesses matched test 1, 53 matched
    test 2, and only 12 matched both — the first work list missed 41, the whole
    nuclear layer among them. Test 2 is a property of the physics rather than of
    a decimal expansion, which is why it does not need a maintained list.

    THREE tests now — test 2 has the same shape of blind spot test 1 had.

    3. **Symbolic** — a weight held as an EXPRESSION carrying a half-integer
       power of `q`. Test 2 calls `float(v)` and skips what does not parse, so
       a sympy-valued weight is invisible to it. C is
       `z = 1/(q^{1/2} + q^{-1/2})`; D is `z = q^3/(q^2 + 1)`, rational and
       sqrt-free — so `q^{k/2}` in a weight expression is C at any `n`.

    Test 3 finds two witnesses the other two miss, and they are not inert:
    `y-lambda-wenzl-bridge-symbolic-witness.json` evaluates to nonzero `y_λ`
    on 3-, 4-, 5- and 6-row partitions at q₀ and feeds
    `rho_k_h3a_refinement`, whose Schur-Weyl check fails at 4.75e-8 and which
    is itself the upstream of five more producers.
    """
    if any(c in raw for c in C_FINGERPRINTS):
        return True
    if ("**" in raw or "sqrt" in raw) and _symbolic_hits(doc):
        return True
    if "partition" not in raw:
        return False
    return bool(_structural_hits(doc))


#: Half-integer power of q — see test 3 above.
_SQRT_Q = re.compile(r"q\s*\*\*\s*\(?\s*-?\d+\s*/\s*2\s*\)?"
                     r"|sqrt\(\s*q\s*\)"
                     r"|q\s*\*\*\s*-?0\.5")

_SYMBOLIC_WEIGHT_KEYS = ("y_lambda", "y_lam", "y_at_q0", "weight_lambda")


def _symbolic_hits(doc) -> bool:
    """A weight expression built under convention C. Mirrors the audit's test 3."""
    hit = False

    def walk(node):
        nonlocal hit
        if hit:
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str) and any(w in k for w in _SYMBOLIC_WEIGHT_KEYS):
                    try:
                        float(v)
                        continue
                    except (TypeError, ValueError):
                        pass
                    if _SQRT_Q.search(v):
                        hit = True
                        return
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return hit


def _structural_hits(doc, tol: float = 1e-30):
    """Nonzero y_lambda on a 3+ row block.

    DELEGATES to `convention-c-witness-audit.scan_doc` rather than carrying a
    second copy. The copy that used to live here had drifted: its `part_of`
    handled only list-form partitions and returned None for the
    underscore-encoded form (`"3_2_1"`), which is exactly the encoding
    `binding-a3plus-*.witness.json` uses -- and which the audit's own docstring
    calls out as "must not be silently skipped, since skipping is how the
    fingerprint scan missed things".

    Measured at the moment of the fix, on three witnesses the audit flags:

        binding-a3plus-full-theta-assembly     audit 127 hits, harness 0
        binding-a3plus-joint-ji-combiner       audit 127 hits, harness 0
        probe-option-e-phase2-crystal-vertex   audit  28 hits, harness 0

    So `work_list()` was undercounting, and the campaign's own work list was
    missing convention-C witnesses on the same mechanism the audit exists to
    prevent. Two implementations of one test is the defect; one is the fix.
    """
    return _audit().scan_doc(doc, tol)


def _audit():
    """The canonical detector module, loaded once."""
    global _AUDIT_MOD
    if _AUDIT_MOD is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "cca", REPO / "scripts" / "convention-c-witness-audit.py")
        _AUDIT_MOD = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_AUDIT_MOD)
    return _AUDIT_MOD


_AUDIT_MOD = None

def _resolve_producer(doc, witness: pathlib.Path, index, stems):
    """Find the .py that writes this witness, over three keys and a slug.

    `scriptFile` alone leaves 23 witnesses unowned, 11 of them wrongly: the
    corpus records a producer under three different keys and sometimes not at
    all. Resolution order, weakest assumption last:

    1. ``scriptFile`` / ``script`` / ``producer`` — a path or a bare filename.
       ``producer`` is the one that was being skipped, and it is not a rare
       spelling: it owns the whole `chi_at_q0_via_hoefsmit_mpfr` family.
    2. **slug match** on the witness basename, `-` to `_`. `e0-lambda-tryall`
       to `e0_lambda_tryall.py`. Only accepted on an exact stem hit, so it
       cannot silently bind a witness to a near-neighbour script.

    A `producer` naming a **Rust binary** (`rust-chi-q-via-gp-lossless`,
    `matrix-m-chi-q-via-gp`) resolves to nothing here by design — that layer
    needs the hecke-engine CLI, and is where `qou-j6il` found a binary
    returning convention C while its source read D. Better unowned and visible
    than bound to a Python script that does not produce it.

    `_deprecated/` is never a resolution: a witness whose producer was retired
    is history, and history may stay convention C provided it says so.
    """
    # Some files under computations/ are top-level JSON *lists*, not objects.
    if not isinstance(doc, dict):
        doc = {}
    for key in ("scriptFile", "script", "producer"):
        val = doc.get(key) or ""
        if not isinstance(val, str) or not val:
            continue
        hit = index.get(pathlib.Path(val).name)
        if hit and "_deprecated" not in str(hit):
            return hit
    base = witness.name
    for suffix in (".witness.json", "-witness.json", ".json"):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
            break
    hit = stems.get(base.replace("-", "_"))
    if hit and "_deprecated" not in str(hit):
        return hit
    return None


def work_list():
    """[(witness, producer)] for every convention-C witness."""
    index = {p.name: p for p in (REPO / "computations").rglob("*.py")}
    stems = {p.stem: p for p in (REPO / "computations").rglob("*.py")}
    items, orphans = [], []
    for w in sorted((REPO / "computations").rglob("*.json")):
        if "_deprecated" in str(w):
            continue
        try:
            raw = w.read_text()
        except OSError:
            continue
        try:
            _doc = json.loads(raw)
        except json.JSONDecodeError:
            _doc = {}
        if not _is_convention_c(raw, _doc):
            continue
        try:
            doc = json.loads(raw)
        except json.JSONDecodeError:
            doc = {}
        src = _resolve_producer(doc, w, index, stems)
        (items if src else orphans).append(
            (str(w.relative_to(REPO)), str(src.relative_to(REPO)) if src else None))
    return items, orphans


def work_list_from(path: pathlib.Path):
    """[(witness, producer)] from an explicit set, e.g. the D blast radius.

    `work_list()` answers "which witnesses are convention C **by content**".
    That is the wrong question after an upstream migration: a downstream
    witness recording a number derived from a migrated trace is stale without
    any convention-C content of its own. This takes the producer set as given
    (schema `convention-d-blast-radius/v1`) and reuses everything else --
    dependency ordering, per-producer timeout, journal, drift classification.

    Producers whose file is missing are dropped with a warning rather than
    silently, since a shrinking sweep that still says "done" is exactly the
    failure this harness exists to stop.
    """
    doc = json.loads(pathlib.Path(path).read_text())
    index = {q.name: q for q in (REPO / "computations").rglob("*.py")}
    items, missing = [], []
    for row in doc.get("producers", []):
        prod = row["producer"]
        src = index.get(pathlib.Path(prod).name)
        if src is None:
            missing.append(prod)
            continue
        rel = str(src.relative_to(REPO))
        for w in row.get("writes", []):
            wp = (REPO / "computations" / w)
            if not wp.exists():
                hits = list((REPO / "computations").rglob(w))
                if not hits:
                    continue
                wp = hits[0]
            items.append((str(wp.relative_to(REPO)), rel))
    if missing:
        print(f"  ! {len(missing)} producer(s) in the set have no file on disk: "
              f"{', '.join(pathlib.Path(m).name for m in missing[:5])}"
              + (" ..." if len(missing) > 5 else ""), flush=True)
    return items, []


#: Witness basenames referenced in a producer's source.
#: [.-] because 13 witnesses are `foo-witness.json`, including the
#: y_lambda family that five producers read. A `\.witness\.json`
#: pattern silently drops those dependency edges, which is the same
#: class of bug as ordering producers alphabetically.
_WITNESS_REF = re.compile(r"[A-Za-z0-9._-]+[.-]witness\.json")


def dependency_order(by_producer: dict) -> list:
    """Order producers so an upstream witness is rewritten before its readers.

    Producers read each other's witnesses. Alphabetical order therefore
    regenerates downstream producers against *stale* upstream data and the
    output looks clean — nothing in the run reports it, because each producer
    individually succeeded.

    This is not hypothetical. `rho-k-h3a-refinement.witness.json` is read by
    five producers (`rho_k_co_casimir_extended`, `rho_k_h3a_co_casimir`,
    `rho_k_h3a_crystal`, `rho_k_h3a_frobenius_pairing`, `rho_k_h3a_lp_dual`)
    and written by `rho_k_h3a_refinement`, which sorts **last**. Every one of
    the five read convention-C weights while being counted as migrated. It is
    also how the campaign's first work list came to be wrong: a freshly
    migrated co-Casimir producer printed `live channels = 11 of 11`, impossible
    under convention D at n = 6, because its weights came from a stale upstream.

    Edges come from the source text (which witness names a producer mentions),
    not from a maintained list, so a new dependency orders itself.

    A cycle cannot be ordered; those producers are emitted in the original
    order with a warning rather than dropped, since a mutually-referential pair
    still needs running — it just needs running twice, which is a judgement for
    the operator, not something to silently paper over.
    """
    writes = {p: {pathlib.Path(w).name for w in ws} for p, ws in by_producer.items()}
    reads = {}
    for p in by_producer:
        try:
            src = (REPO / p).read_text()
        except OSError:
            src = ""
        reads[p] = set(_WITNESS_REF.findall(src)) - writes[p]

    # owner[witness] = the producer that writes it (within this run).
    owner = {w: p for p, ws in writes.items() for w in ws}
    deps = {p: {owner[w] for w in reads[p] if w in owner and owner[w] != p}
            for p in by_producer}

    ordered, placed = [], set()
    while True:
        ready = sorted(p for p in by_producer
                       if p not in placed and deps[p] <= placed)
        if not ready:
            break
        ordered.extend(ready)
        placed.update(ready)

    stuck = sorted(p for p in by_producer if p not in placed)
    if stuck:
        print(f"  ! {len(stuck)} producer(s) in a witness-dependency cycle; "
              f"running in name order: {', '.join(pathlib.Path(s).name for s in stuck)}",
              flush=True)
        ordered.extend(stuck)
    return ordered


def stale_readers():
    """Producers that ran BEFORE an upstream witness they read was rewritten.

    `dependency_order` fixes the order of work still pending. It cannot fix
    what already ran: a producer recorded early in the journal may have read a
    witness that a later producer then rewrote, so its committed output is
    against data that no longer exists.

    The journal is append-ordered, which is the only clock available — records
    carry no timestamp — and it is sufficient: if Q writes a witness P reads,
    and Q appears after P, then P read Q's pre-run value.

    Returns [(reader, [upstreams])] in journal order. An empty list is the
    campaign's real convergence criterion, and it is stronger than "every
    producer ran": a run can be 52-for-52 green and still be internally
    inconsistent.
    """
    items, _ = work_list()
    by_producer = {}
    for w, p in items:
        by_producer.setdefault(p, []).append(w)
    writes = {p: {pathlib.Path(w).name for w in ws} for p, ws in by_producer.items()}
    owner = {w: p for p, ws in writes.items() for w in ws}

    # The LAST record is the one that matters: a producer's committed witness
    # comes from its most recent run, so P is stale iff last(Q) > last(P).
    # Keying on the first record would flag a producer that was re-run after
    # its upstream — a false positive, and precisely the case a drain creates.
    # Today a second record only exists after a purge removes the first (the
    # harness skips producers already in the journal), so first and last
    # coincide; this keeps the check correct once that stops being true.
    pos = {}
    for i, line in enumerate(LOG.read_text().splitlines() if LOG.exists() else []):
        try:
            pos[json.loads(line)["producer"]] = i
        except Exception:                                        # noqa: BLE001
            continue
    order = sorted(pos, key=pos.get)

    out = []
    for p in order:
        if p not in by_producer:
            continue
        try:
            src = (REPO / p).read_text()
        except OSError:
            continue
        late = sorted({
            owner[w] for w in set(_WITNESS_REF.findall(src))
            if w in owner and owner[w] != p
            and (owner[w] not in pos or pos[owner[w]] > pos[p])
        })
        if late:
            out.append((p, late))
    return out


def done_set():
    if not LOG.exists():
        return set()
    out = set()
    for line in LOG.read_text().splitlines():
        try:
            out.add(json.loads(line)["producer"])
        except Exception:
            pass
    return out


#: Live producer subprocesses, so signal handlers can take them down with us.
_CHILDREN: list = []


def _kill_group(proc):
    """SIGTERM then SIGKILL the producer's whole process group."""
    if proc is None or proc.poll() is not None:
        return
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            os.killpg(os.getpgid(proc.pid), sig)
        except (ProcessLookupError, PermissionError, OSError):
            return
        try:
            proc.wait(timeout=10)
            return
        except subprocess.TimeoutExpired:
            continue


def _on_signal(signum, _frame):
    """Never leave a producer running after the harness dies."""
    print(f"\nreceived signal {signum} — terminating producer(s) before exit", flush=True)
    for proc in list(_CHILDREN):
        _kill_group(proc)
    try:
        (REPO / ".work" / "convention-c-regen.lock").unlink(missing_ok=True)
    except OSError:
        pass
    sys.exit(128 + signum)


for _sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
    signal.signal(_sig, _on_signal)


class SerialLock:
    """Refuse to start if another instance is already running.

    Not paranoia: on 2026-08-10 two instances of this script were launched
    within a minute of each other and both began stepping through the producer
    list. Nothing was corrupted — they were killed before either finished a
    shared producer — but the standing directive is *never two producers
    concurrently in one checkout*, and "I was careful" is not a mechanism.

    Uses O_EXCL plus a liveness check, so a lock left behind by a container
    death (which has happened twice in this arc) does not wedge the next run.
    """

    def __init__(self, path: pathlib.Path):
        self.path = path

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                pid = int(self.path.read_text().strip())
            except (ValueError, OSError):
                pid = None
            alive = False
            if pid is not None:
                try:
                    os.kill(pid, 0)
                    alive = True
                except OSError:
                    alive = False
            if alive:
                sys.exit(f"REFUSING TO START: another run holds {self.path} (pid {pid}).\n"
                         f"Producers must run strictly serially in one checkout.")
            print(f"note: clearing stale lock from dead pid {pid}", flush=True)
            self.path.unlink(missing_ok=True)
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return self

    def __exit__(self, *exc):
        self.path.unlink(missing_ok=True)
        return False


def run_all(timeout: int, source: pathlib.Path | None = None):
    items, orphans = work_list_from(source) if source else work_list()
    # One producer may own several witnesses; run it once.
    by_producer = {}
    for w, p in items:
        by_producer.setdefault(p, []).append(w)

    already = done_set()
    todo = [(p, by_producer[p]) for p in dependency_order(by_producer)
            if p not in already]
    LOG.parent.mkdir(parents=True, exist_ok=True)

    print(f"producers: {len(by_producer)}   already done: {len(already)}   to run: {len(todo)}")
    print(f"orphan witnesses (no scriptFile): {len(orphans)}")
    print(f"log: {LOG}\n", flush=True)

    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join(SYS_PATHS) + os.pathsep + env.get("PYTHONPATH", "")

    for n, (producer, witnesses) in enumerate(todo, 1):
        before = {w: snapshot(REPO / w) for w in witnesses}
        t0 = time.time()
        # Own process group, so a kill of this harness takes the producer with
        # it. Killing the harness alone used to ORPHAN the producer: it kept
        # running, reparented to init, and the next harness happily started the
        # same script again. Three concurrent copies of binding_k_enumerator.py
        # were writing one witness before this was noticed. The SerialLock
        # guards harness instances; only this guards their children.
        proc = None
        try:
            proc = subprocess.Popen(
                [sys.executable, str(pathlib.Path(producer).name)]
                + producer_argv(producer, witnesses),
                cwd=str((REPO / producer).parent), env=env,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                start_new_session=True)
            _CHILDREN.append(proc)
            out, err = proc.communicate(timeout=timeout)
            status = "ok" if proc.returncode == 0 else f"exit{proc.returncode}"
            tail = (err or out or "").strip().splitlines()[-3:]
        except subprocess.TimeoutExpired:
            _kill_group(proc)
            try:
                out, err = proc.communicate(timeout=15)
            except Exception:                                    # noqa: BLE001
                out = err = ""
            status, tail = "timeout", (err or out or "").strip().splitlines()[-2:]
        except Exception as e:                                   # noqa: BLE001
            _kill_group(proc)
            status, tail = f"error:{type(e).__name__}", [str(e)[:200]]
        finally:
            if proc in _CHILDREN:
                _CHILDREN.remove(proc)
        secs = round(time.time() - t0, 1)
        after = {w: snapshot(REPO / w) for w in witnesses}

        rec = {
            "producer": producer, "status": status, "seconds": secs,
            "witnesses": [
                {"path": w,
                 "c_before": before[w].get("c_fingerprint"),
                 "c_after": after[w].get("c_fingerprint"),
                 "changed": before[w].get("sha256") != after[w].get("sha256"),
                 "deltas": diff(before[w], after[w])}
                for w in witnesses],
            "tail": tail,
        }
        with LOG.open("a") as fh:
            fh.write(json.dumps(rec) + "\n")

        cleared = sum(1 for w in witnesses
                      if before[w].get("c_fingerprint") and not after[w].get("c_fingerprint"))
        print(f"[{n:3d}/{len(todo)}] {status:>9} {secs:7.1f}s  "
              f"cleared {cleared}/{len(witnesses)}  {producer}", flush=True)

    print("\nrun complete", flush=True)


def convention_coverage(paths):
    """How many of these witnesses actually SAY which convention they are.

    The detector finds convention C two ways — a known decimal, or a nonzero
    `y_λ` on a three-or-more-row partition — and **both key on `y_λ` tables**.
    A convention-dependent quantity that is not a `y_λ` table is invisible to
    it. `tr_M(β)` is the case that bit: it is the Markov trace at parameter `z`,
    so it is fully convention-dependent, it carries no partition structure, and
    `atomic-tr-m-mpfr-50dps.witness.json` therefore never appeared in the work
    list at all. Everything derived downstream — ρ, Δρ, binding, mass — inherits
    the same invisibility.

    No syntactic rule fixes that: a bare trace value looks identical under
    either convention. The only thing that can distinguish them is
    **provenance** — the producer saying which convention it computed in.

    So rather than pretend to detect the undetectable, this counts how much of
    the corpus is even *capable* of answering the question. A witness with no
    `convention` field is not evidence of convention C; it is evidence that the
    work-list count is a lower bound of unknown slack, which is worth printing
    next to that count instead of leaving implied.
    """
    have, missing = [], []
    for rel in paths:
        try:
            doc = json.loads((REPO / rel).read_text())
        except (OSError, json.JSONDecodeError):
            continue
        # `markov_convention` specifically, NOT `convention`: the latter is
        # already used corpus-wide for the CROSSING convention
        # ("colour-weighted-averaged-crossing", "sign-only-crossings", …),
        # an orthogonal axis. Counting those as trace-convention provenance
        # would report seven witnesses as answered when none of them
        # addresses the question.
        if isinstance(doc, dict) and doc.get("markov_convention"):
            have.append((rel, doc["markov_convention"]))
        else:
            missing.append(rel)
    total = len(have) + len(missing)
    if not total:
        return
    print(f"trace-convention provenance: {len(have)}/{total} witnesses declare "
          f"a `markov_convention` field")
    for rel, conv in sorted(have):
        print(f"    {conv:<4} {rel.replace('computations/', '')}")
    if missing:
        print(f"  {len(missing)} declare nothing — for these the work-list "
              f"count is a LOWER BOUND, not a total.\n"
          f"  (A trace or a derived scalar looks the same under either "
          f"convention; only the producer knows.)")
    print()


def impact_vs_main(base: str = "origin/main"):
    """Total impact: every witness's CURRENT state against its state on `base`.

    The per-run JSONL records a single pass's before/after. Once the campaign
    needs more than one pass — and it does, because the first two ran in the
    wrong dependency order — those deltas answer "what did pass 3 change",
    which is not the question. A witness that moved in pass 1 and settled in
    pass 3 shows almost nothing in the pass-3 record while having moved a long
    way from what is committed on main.

    So measure the thing actually being asked for: committed-on-`base` versus
    on-disk-now, classified with the same rules. Independent of how many passes
    it took, and it stays correct if a pass has to be re-run.
    """
    changed = subprocess.run(
        ["git", "diff", "--name-only", base, "--", "computations"],
        cwd=str(REPO), capture_output=True, text=True).stdout.split()
    witnesses = [f for f in changed if f.endswith(".json")]
    print(f"impact vs {base}: {len(witnesses)} witness file(s) differ\n")
    convention_coverage(witnesses)

    kinds, shifts, per_witness = {}, [], []
    for rel in witnesses:
        old = subprocess.run(["git", "show", f"{base}:{rel}"], cwd=str(REPO),
                             capture_output=True, text=True)
        if old.returncode != 0:          # added on this branch, no base version
            per_witness.append((rel, "new", 0, None))
            continue
        try:
            before = {"numbers": numeric_fields(json.loads(old.stdout))}
            after = {"numbers": numeric_fields(json.loads((REPO / rel).read_text()))}
        except (json.JSONDecodeError, OSError):
            per_witness.append((rel, "unreadable", 0, None))
            continue
        rows = diff(before, after)
        worst = 0.0
        for d in rows:
            kind, rel_change = classify(d["before"], d["after"])
            kinds[kind] = kinds.get(kind, 0) + 1
            if kind == "shift":
                shifts.append((rel_change, rel, d))
                worst = max(worst, rel_change or 0.0)
        per_witness.append((rel, "changed" if rows else "provenance only",
                            len(rows), worst))

    print("delta kinds : " + (", ".join(f"{k}={v}" for k, v in sorted(kinds.items()))
                              or "none"))
    collapse = kinds.get("structural_zero", 0) + kinds.get("vanished", 0)
    print(f"convention-D collapse: {collapse} "
          f"(exactly 0: {kinds.get('structural_zero', 0)}, "
          f"below floor: {kinds.get('vanished', 0)})")

    print(f"\n{'witness':<62} {'deltas':>7} {'worst ppm':>14}")
    for rel, state, n, worst in sorted(per_witness, key=lambda t: -(t[3] or 0)):
        w = f"{worst*1e6:14.1f}" if worst else ("" if state != "changed" else "0.0")
        print(f"  {rel.replace('computations/', '')[:60]:<60} {n:7d} {w:>14}"
              + ("" if state == "changed" else f"  [{state}]"))

    shifts.sort(key=lambda t: t[0] or 0, reverse=True)
    print("\nlargest shifts overall:")
    for rel_change, rel, d in shifts[:10]:
        print(f"  {rel_change*1e6:14.1f} ppm  {rel.split('/')[-1]}  {d['field']}")
        print(f"        {d['before'][:26]} -> {d['after'][:26]}")



def report():
    if not LOG.exists():
        print("no log yet")
        return
    recs = [json.loads(l) for l in LOG.read_text().splitlines() if l.strip()]
    ok = [r for r in recs if r["status"] == "ok"]
    bad = [r for r in recs if r["status"] != "ok"]
    total_secs = sum(r["seconds"] for r in recs)

    kinds, shifts, zeros = {}, [], 0
    cleared = still_c = 0
    for r in recs:
        for w in r["witnesses"]:
            if w["c_before"] and not w["c_after"]:
                cleared += 1
            elif w["c_after"]:
                still_c += 1
            for d in w["deltas"]:
                # RECLASSIFY from the raw values rather than trusting the stored
                # `kind`: records written before the noise-floor rule existed
                # carry the old labels, and a report that mixes the two is worse
                # than one that is merely wrong.
                kind, rel = classify(d["before"], d["after"])
                kinds[kind] = kinds.get(kind, 0) + 1
                if kind == "shift":
                    shifts.append((rel, r["producer"], w["path"], d))
                elif kind == "structural_zero":
                    zeros += 1

    print(f"producers run : {len(recs)}   ok {len(ok)}   failed {len(bad)}")
    print(f"wall time     : {total_secs/60:.1f} min")
    print(f"witnesses     : C cleared {cleared}   still C {still_c}")
    print(f"\ndelta kinds   : " + ", ".join(f"{k}={v}" for k, v in sorted(kinds.items())))
    print(f"structural zeros (y_lambda -> 0, ell(lambda)>=3): {zeros}")

    # Key on the magnitude only: two shifts can tie on `rel`, and the
    # tuple comparison then falls through to comparing dicts, which raises.
    # Magnitude distribution first. A list of extremes answers "what moved
    # most"; only the distribution answers "how much of the corpus moved", and
    # that is the question "total impact" is actually asking.
    buckets = [("< 1 ppm", 0), ("1 ppm - 100 ppm", 0), ("100 ppm - 1%", 0),
               ("1% - 10%", 0), ("10% - 100%", 0), ("> 100% (order-of-magnitude)", 0)]
    counts = [0] * 6
    for rel, *_ in shifts:
        if   rel < 1e-6:  counts[0] += 1
        elif rel < 1e-4:  counts[1] += 1
        elif rel < 1e-2:  counts[2] += 1
        elif rel < 1e-1:  counts[3] += 1
        elif rel < 1.0:   counts[4] += 1
        else:             counts[5] += 1
    print("\nshift magnitude distribution:")
    for (label, _), n in zip(buckets, counts):
        bar = "#" * min(40, n // max(1, max(counts) // 40 or 1))
        print(f"  {label:<30} {n:5d}  {bar}")

    shifts.sort(key=lambda t: t[0], reverse=True)
    print(f"\nlargest RELATIVE shifts:")
    for rel, prod, wpath, d in shifts[:12]:
        print(f"  {rel*1e6:16.1f} ppm  {wpath.split('/')[-1]}")
        print(f"        {d['field']}")
        print(f"        {d['before'][:26]} -> {d['after'][:26]}")

    def absdelta(t):
        try:
            return abs(float(t[3]["after"]) - float(t[3]["before"]))
        except ValueError:
            return 0.0
    shifts.sort(key=absdelta, reverse=True)
    print(f"\nlargest ABSOLUTE shifts (what actually moved in magnitude):")
    for rel, prod, wpath, d in shifts[:12]:
        print(f"  {absdelta((rel,prod,wpath,d)):18.9g}  ({rel*1e6:.1f} ppm)  {wpath.split('/')[-1]}")
        print(f"        {d['field']}")
        print(f"        {d['before'][:26]} -> {d['after'][:26]}")

    if bad:
        print(f"\nFAILURES ({len(bad)}):")
        for r in bad:
            print(f"  {r['status']:>10}  {r['producer']}")
            for t in r["tail"][-1:]:
                print(f"              {t[:150]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--from", dest="source", metavar="JSON",
                    help="run an explicit producer set (convention-d-blast-radius/v1) "
                         "instead of the convention-C content scan")
    ap.add_argument("--journal", metavar="PATH",
                    help="journal file for this sweep; a distinct sweep needs a "
                         "distinct clock, or done_set() skips it as already run")
    ap.add_argument("--stale", action="store_true",
                    help="list producers that ran before an upstream witness "
                         "they read was rewritten (exit 1 if any)")
    ap.add_argument("--impact-vs-main", dest="impact", nargs="?",
                    const="origin/main", metavar="REF",
                    help="total impact: every witness's CURRENT state against "
                         "its state on REF (default origin/main). This is the "
                         "campaign's merge gate — the per-run journal answers "
                         "'what did THIS pass change', which is a different "
                         "question once the campaign takes more than one pass")
    a = ap.parse_args()
    if a.journal:
        # A distinct sweep needs a distinct clock. done_set() keys off this
        # file, so reusing the convention-C journal would mark most of a D
        # sweep "already done" and skip it -- silently, and looking finished.
        global LOG
        LOG = pathlib.Path(a.journal)
    if a.impact:
        impact_vs_main(a.impact)
        return 0
    if a.stale:
        rows = stale_readers()
        if not rows:
            print("no stale readers — every producer ran after its upstreams")
            return 0
        print(f"{len(rows)} producer(s) ran against an upstream that changed after:")
        for p, ups in rows:
            print(f"  {p}")
            for u in ups:
                print(f"      reads a witness written later by  {u}")
        return 1
    if a.plan:
        items, orphans = (work_list_from(pathlib.Path(a.source)) if a.source
                          else work_list())
        by = {}
        for w, p in items:
            by.setdefault(p, []).append(w)
        print(f"{len(items)} witnesses / {len(by)} producers; {len(orphans)} orphan witnesses")
        for p, ws in sorted(by.items()):
            print(f"  {p}  ->  {len(ws)} witness(es)")
        for w, _ in orphans:
            print(f"  ORPHAN  {w}")
        return 0
    if a.run:
        with SerialLock(REPO / ".work" / "convention-c-regen.lock"):
            run_all(a.timeout, pathlib.Path(a.source) if a.source else None)
        return 0
    if a.report:
        report()
        return 0
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
