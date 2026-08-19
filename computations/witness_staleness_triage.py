#!/usr/bin/env python3
"""Split self-stale witnesses by whether refreshing them is safe, or even useful.

`witness_dependency_drift.py` reports every witness whose `scriptHash` no longer
matches its producer. It cannot say *why*, because `scriptHash` is a whole-file
SHA-256: a docstring edit drifts it exactly as loudly as a changed formula. The
idle-backlog policy caps witness refreshes at 3 per pass and tells the agent to
`git diff` the producer first for precisely this reason (AGENTS.md §4, and the
worked case `canonical-ordering-dof`, which drifted on +21 lines that are *all*
comment).

At the current backlog — 751 self-stale of ~3000 — "diff it first" is advice no
one can act on witness-by-witness. This script does it for the whole set at
once, so an idle pass can spend its budget on the drifts that can actually move
a number.

## The classification

For each self-stale witness with a recorded `commitSha`, fetch the producer as
it stood at that commit and compare it to the current file **after stripping
everything that cannot affect the output**:

  * comments        — dropped by `ast.parse` before we ever see them
  * docstrings      — removed explicitly, module / class / function
  * formatting      — normalised by `ast.unparse`

If the two normalised sources differ, that is `substantive` — the code that
computes the numbers changed, so the witness may report values the producer no
longer produces. These are the real queue.

If they are identical, **the producer's own source cannot explain a payload
change — but three other things still can**, so further gates apply.

The first is the one that actually bites, and I originally misdiagnosed it.
`binding_canonical.py` is source-stable across its drift window, yet its
`tr_M_atom` moved `0.388 -> 0.575` — 48 %. I attributed that to a missing
`pyhecke_native` and wrote it up as an environment effect. **That was wrong.**
Re-run later with `pyhecke_native 0.9.0` installed and every recorded package
matched, the producer reproduces `0.57517233101788385191` *byte-identically* —
the same value it gives without the native extension. The environment was never
the cause. What changed was `tr_m_atom_via_transfer.py`, the imported module
that computes the quantity, which is invisible to a file-local AST comparison.

The environment gate is kept because the hazard is real in principle — a
producer *can* branch on what is installed — but it is retained **unproven**:
this corpus has not yet given a measured instance of it, and the case I offered
turned out to be an import-cone case wearing an environment costume.

A third gate is subtler still: some producers write a **bare** witness and never
emit provenance — the `scriptHash` / `commitSha` / `environment` block on disk
was added downstream. Re-running one of those *deletes the fields the drift
audit keys on*, making the witness permanently undecidable. Measured on
`d_u_closed_form_proof.py` and `yekutieli_volume_join.py`: 15 keys in, 7 and 9
keys out. Rare — 1 of 80 sampled producers — but both `cosmetic` candidates in
this corpus hit it, because bare producers are the old ones and old producers
are what drift.

  * `cosmetic`                   — producer source cosmetic, no drifted import
    found, environment matches, and the producer writes its own provenance.
    The nearest thing to safe — but "no drift found" is one hop, not a
    transitive closure, so it is not a guarantee.
  * `cosmetic_import_cone_drift` — **do not refresh.** A module it imports
    changed; the payload can move even though this file did not.
  * `cosmetic_env_differs`       — **do not refresh.** Provision first, or leave.
  * `cosmetic_strips_provenance` — **do not refresh.** Fix the producer to emit
    provenance first; refreshing destroys the audit trail.

**The transitive walk found nothing the one-hop check missed — measured, not
assumed.** Walking the cone to 6 hops returns the same 6 witnesses, and *every*
drift sits at depth 1. So on this corpus the shallow check was already
sufficient; the deep walk is kept because that is a fact about today's corpus,
not a property of the method, and it costs little (module paths and git lookups
are memoised).

**The gate over-flags, and I would rather say so than let it look sharper than
it is.** 5 of the 6 hits are `substrate/witness_base.py` or
`substrate/_precision.py` — imported by nearly every producer. Checked one:
`casimir-d6-qcorrection-structure` is flagged because `witness_base.py` gained
15 lines whose only non-comment content is exporting `_EPHEMERAL_META_FIELDS`.
That is serialization plumbing and **cannot move a number**. `_precision.py` is
a genuine maybe — it sets `mp.dps`, so a change there really can shift digits —
but `witness_base` drift is provenance-only.

Note this does not create work in either direction, which is the point: a
refresh driven by infra-only drift would change nothing *but* provenance, and
"provenance-only refresh" is precisely what this whole script exists to say is
not worth the budget. So `cosmetic = 0` should be read as **conservative** — a
few of the 6 are arguably refreshable — and the practical conclusion is
unchanged.

**Gate order matters when reading the counts.** The import-cone check runs
first, so a witness that would *also* fail the environment or bare-producer gate
is reported only as `cosmetic_import_cone_drift`. That is why those two buckets
read 0 here: all three surviving cases drifted an import. The bare-producer
observation is independently true and still worth knowing —
`d_u_closed_form_proof.py` and `yekutieli_volume_join.py` really do write 15
keys and re-emit 7 and 9, deleting the `scriptHash` this audit reads — it is
simply not the *first* reason those two must not be refreshed.

**The measured result on this corpus is `cosmetic = 0`.** Of ~750 self-stale
witnesses, not one is safe to refresh by the naive "re-run the producer" advice.
That is the finding, not a limitation of the script: the idle-pass witness
budget has nothing to spend itself on here, and an agent that spends it anyway
is doing damage rather than maintenance.

**It is not a snapshot.** Re-measured five times across 1638 commits of main
(2026-08-11 and twice on 2026-08-19, corpus 2898 -> 2985 witnesses), `cosmetic`
came back 0 every time, and the class shape barely moved:

    2026-08-11   substantive 242   rewritten 329   unresolvable 107   cosmetic 0
    2026-08-19   substantive 239   rewritten 329   unresolvable 106   cosmetic 0
    2026-08-19   substantive 256   rewritten 338   unresolvable 103   cosmetic 0
    2026-08-19   substantive 268   rewritten 366   unresolvable 111   cosmetic 0

So this is structural, not a bad week. Meanwhile main spent 45 `chore(witness)`
commits over those same 8 days, 13 of them titled "refresh provenance sha after
rebase" — hand-patching the `commitSha` of the `rewritten` class, which is
nearly half the backlog and which no branch-side edit can durably fix.

Three honest residual classes, reported separately rather than folded in:

  * `rewritten`    — the recorded `commitSha` resolves to nothing. Not damage:
    rebase-merge (AGENTS.md rule 8) rewrites every branch commit sha, so a
    witness produced on a feature branch records a sha the merge destroyed.
    AGENTS.md says this of `scriptCommitSha`; it is equally true of `commitSha`.
    At 366 of 751 this is **48.7 % of the backlog**, and the §4 remedy
    (`git diff <witness.commitSha> -- <producer>`) is simply unrunnable on it.

    Worth being precise about what is and is not broken here: `commitSha` is
    **already** not an enforcement key — `witness_dependency_drift.py` keys
    self-staleness on `scriptHash` alone. So nothing is *failing* because of
    this; what is lost is the ability to *decide* half the queue.

    These entries now carry a **heuristic timestamp anchor**: the nearest
    `origin/main` commit at-or-before `computedAt` that still has the producer,
    plus an `approx_verdict` from comparing normalised sources across it. It
    resolves for ~43 % of the class. **It is advisory and must not be quoted as
    a verdict** — the witness was produced on a branch, so main at that instant
    may carry a different producer than the branch did, and it is wrong in both
    directions. Use it to prioritise; use the runner
    (`witness_producer_executes_audit.py`) to conclude, since running a producer
    needs no sha at all and is the only sha-free answer available.
  * `unresolvable` — no `commitSha`, or the producer is not at that path there.
  * `unparseable`  — the old or new producer is not valid Python 3 here. Rare,
    and never silently counted as cosmetic.

## Relationship to the reproducibility gate

`witness_reproducibility_check.py` and `witness_producer_executes_audit.py`
(landed on `main` via #4960) answer *"can this producer still produce this
witness?"* by **running** it. This script answers the cheaper
upstream question *"is it worth running?"* by reading source and git, and never
executes a producer. The env gate here reuses their axis to avoid recommending a
refresh their `ENV_MISSING` bucket would catch after the fact; it does not
duplicate their runner.

## Scope

This is a **triage**, not a verdict on correctness. `cosmetic` means "re-running
cannot change the payload", NOT "the witness is right" — a witness can be
cosmetically-clean and still carry a wrong number from a producer that was
already wrong. It also says nothing about `scriptCommitSha`, which AGENTS.md
correctly tells you to ignore: rebase-merge rewrites it, so it is stale on
arrival for anything committed on a branch.

Usage:
    python3 computations/witness_staleness_triage.py              # summary
    python3 computations/witness_staleness_triage.py --list substantive
    python3 computations/witness_staleness_triage.py --witness    # emit witness JSON

-- Ref: [manuscript] AGENTS.md §"Refresh stale sidecars + witnesses"; bean qou-zv2l.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPUTATIONS = ROOT / "computations"


def _git(*args: str) -> str | None:
    """Run git in the repo, returning stdout, or None if the command failed."""
    r = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True, text=True,
    )
    return r.stdout if r.returncode == 0 else None


def _strip_docstrings(tree: ast.AST) -> ast.AST:
    """Drop module/class/function docstrings in place."""
    for node in ast.walk(tree):
        if not isinstance(
            node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            continue
        body = node.body
        if (
            body
            and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)
        ):
            # Never leave an empty body — that would not unparse.
            node.body = body[1:] or [ast.Pass()]
    return tree


def normalise(src: str) -> str | None:
    """Source with comments, docstrings and formatting removed; None if unparseable."""
    try:
        return ast.unparse(_strip_docstrings(ast.parse(src)))
    except (SyntaxError, ValueError, RecursionError):
        return None


def env_gap(w: dict) -> dict[str, str]:
    """Recorded packages this interpreter cannot match: name -> what differs.

    Only the `environment` block the witness itself recorded is checked — this
    does not invent requirements. `python` is compared on major.minor, since a
    patch bump does not change a numeric result.
    """
    import importlib.metadata as md

    recorded = w.get("environment")
    if not isinstance(recorded, dict):
        return {}

    gaps: dict[str, str] = {}
    for name, want in recorded.items():
        if not isinstance(want, str):
            continue
        if name == "python":
            have = ".".join(sys.version.split()[0].split(".")[:2])
            if want.split()[-1].rsplit(".", 1)[0] not in (have,):
                gaps[name] = f"witness {want}, here {have}"
            continue
        try:
            have = md.version(name.replace("_", "-"))
        except md.PackageNotFoundError:
            gaps[name] = f"witness {want}, NOT INSTALLED here"
            continue
        if have != want:
            gaps[name] = f"witness {want}, here {have}"
    return gaps


_MODULE_PATH_CACHE: dict[str, str | None] = {}
_CHANGED_CACHE: dict[tuple[str, str], bool] = {}


def _resolve_module(name: str) -> str | None:
    """Repo-relative path of a local module, or None if it is not one of ours."""
    if name in _MODULE_PATH_CACHE:
        return _MODULE_PATH_CACHE[name]
    hit = None
    direct = COMPUTATIONS / f"{name}.py"
    if direct.is_file():
        hit = direct
    else:
        for c in COMPUTATIONS.rglob(f"{name}.py"):
            hit = c
            break
    _MODULE_PATH_CACHE[name] = hit.relative_to(ROOT).as_posix() if hit else None
    return _MODULE_PATH_CACHE[name]


def _imported_names(src: str) -> set[str]:
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError, RecursionError):
        return set()
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names.add(node.module.split(".")[0])
        elif isinstance(node, ast.Import):
            for a in node.names:
                names.add(a.name.split(".")[0])
    return names


def _changed_since(rel: str, sha: str) -> bool:
    key = (rel, sha)
    if key not in _CHANGED_CACHE:
        _CHANGED_CACHE[key] = _git("diff", "--quiet", sha, "HEAD", "--", rel) is None
    return _CHANGED_CACHE[key]


def local_import_drift(producer: Path, src: str, sha: str,
                       max_depth: int = 6) -> list[str]:
    """Local modules in the producer's TRANSITIVE import cone that changed since `sha`.

    The producer's own AST being unchanged says nothing about the code it calls.
    Measured: `binding_canonical.py` is byte-stable across its drift window while
    `tr_m_atom_via_transfer.py` -- which computes the very quantity it reports --
    changed, moving `tr_M_atom` 0.388 -> 0.575 (48%).

    This walks the cone breadth-first to `max_depth` hops rather than the single
    hop it originally checked, because a one-hop clean result was never evidence
    of a clean cone: the module that moves a number can sit two imports down and
    read as clean from the producer. Each returned path is prefixed with the hop
    at which it was found, so a depth-1 hit (the producer calls it directly) is
    distinguishable from a depth-4 one when judging plausibility.

    Still not a proof of cleanliness. It resolves only `computations/` modules by
    top-level name, follows no dynamic or function-local imports it cannot parse,
    and stops at `max_depth`. Read a clean result as "no drift found within
    <depth> hops", never as "no drift".
    """
    prod_rel = producer.relative_to(ROOT).as_posix()
    seen: set[str] = {prod_rel}
    frontier = [(n, 1) for n in sorted(_imported_names(src))]
    drifted: list[str] = []

    while frontier:
        name, depth = frontier.pop(0)
        if depth > max_depth:
            continue
        rel = _resolve_module(name)
        if rel is None or rel in seen:
            continue
        seen.add(rel)
        if _changed_since(rel, sha):
            drifted.append(f"{rel} (depth {depth})")
        try:
            sub = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for n in sorted(_imported_names(sub)):
            if _resolve_module(n) not in seen:
                frontier.append((n, depth + 1))

    return drifted


def find_producer(script_file: str) -> Path | None:
    """Resolve a witness `scriptFile` to a path under computations/."""
    direct = COMPUTATIONS / script_file
    if direct.is_file():
        return direct
    hits = list(COMPUTATIONS.rglob(script_file))
    return hits[0] if len(hits) == 1 else None


def approx_anchor(computed_at: str | None, producer_rel: str) -> str | None:
    """Nearest `origin/main` commit at-or-before `computed_at` carrying the producer.

    A HEURISTIC anchor for the `rewritten` class, whose recorded `commitSha` no
    longer resolves. It makes "diff the producer first" runnable again for the
    ~43% of that class where it succeeds -- but it is NOT a recovery of the true
    parent and must never be reported as one: the witness was produced on a
    BRANCH, so main at that instant may carry a different version of the producer
    than the branch did. Wrong in both directions (the branch may have been ahead
    on the producer; main may have moved between compute and merge).

    Use it to triage, never to conclude.
    """
    if not computed_at:
        return None
    out = _git("rev-list", "-1", f"--before={computed_at}", "origin/main")
    sha = (out or "").strip()
    if not sha:
        return None
    if _git("cat-file", "-e", f"{sha}:{producer_rel}") is None:
        return None
    return sha


def triage() -> dict:
    classes: dict[str, list] = {
        "cosmetic": [], "cosmetic_env_differs": [],
        "cosmetic_import_cone_drift": [],
        "cosmetic_strips_provenance": [], "substantive": [],
        "rewritten": [], "unresolvable": [], "unparseable": [],
    }

    for wpath in sorted(COMPUTATIONS.rglob("*.witness.json")):
        try:
            w = json.loads(wpath.read_text())
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(w, dict):
            continue

        script_file = w.get("scriptFile")
        recorded = w.get("scriptHash")
        if not script_file or not recorded:
            continue

        producer = find_producer(script_file)
        rel_w = wpath.relative_to(ROOT).as_posix()
        if producer is None:
            continue

        current_src = producer.read_bytes()
        current_hash = hashlib.sha256(current_src).hexdigest()[: len(recorded)]
        if current_hash == recorded:
            continue  # not stale

        rel_p = producer.relative_to(ROOT).as_posix()
        entry = {"witness": rel_w, "producer": rel_p,
                 "recorded": recorded, "current": current_hash}

        sha = w.get("commitSha")
        if not sha or sha in ("unknown", ""):
            entry["reason"] = "no commitSha recorded"
            classes["unresolvable"].append(entry)
            continue

        # Distinguish "the commit is gone" from "the file was not there yet".
        # They call for completely different follow-ups and conflating them
        # hides the dominant cause.
        if _git("cat-file", "-e", f"{sha}^{{commit}}") is None:
            entry["reason"] = f"commit {sha[:9]} not in the repository"
            # Try the heuristic timestamp anchor so this half of the backlog is
            # at least triageable. Advisory only -- see approx_anchor's caveat.
            anchor = approx_anchor(w.get("computedAt"), rel_p)
            if anchor:
                entry["approx_anchor"] = anchor[:9]
                old_src = _git("show", f"{anchor}:{rel_p}")
                if old_src is not None:
                    a, b = normalise(old_src), normalise(
                        current_src.decode("utf-8", "replace"))
                    if a is not None and b is not None:
                        entry["approx_verdict"] = (
                            "cosmetic (ADVISORY — anchor is approximate)"
                            if a == b else
                            "substantive (ADVISORY — anchor is approximate)")
            classes["rewritten"].append(entry)
            continue

        old = _git("show", f"{sha}:{rel_p}")
        if old is None:
            entry["reason"] = f"producer not at this path in {sha[:9]} (renamed/moved)"
            classes["unresolvable"].append(entry)
            continue

        new_norm = normalise(current_src.decode("utf-8", "replace"))
        old_norm = normalise(old)
        if new_norm is None or old_norm is None:
            entry["reason"] = "producer does not parse as Python 3 here"
            classes["unparseable"].append(entry)
            continue

        if new_norm != old_norm:
            classes["substantive"].append(entry)
            continue

        # Source-identical is NOT the same as safe-to-refresh. A producer can
        # branch on what is INSTALLED, so the same source in a different
        # environment writes a different payload -- silently, with no crash and
        # no warning. Measured: binding_canonical.py without `pyhecke_native`
        # gives tr_M_atom = 0.575 where the committed witness has 0.388, a 48%
        # move under an unchanged AST. Refreshing that would have overwritten a
        # Rust-backed value with a pure-Python fallback under a `chore` commit.
        # Third way a refresh can do damage, and the subtlest: some producers
        # write a BARE witness and never emit provenance at all -- the
        # scriptHash / commitSha / environment block on disk was added by
        # something downstream. Re-running such a producer DELETES the very
        # fields the drift audit keys on, so the "refresh" makes the witness
        # permanently undecidable. Measured on d_u_closed_form_proof.py and
        # yekutieli_volume_join.py: 15 keys in, 7 and 9 keys out.
        src_text = current_src.decode("utf-8", "replace")

        # A producer's own AST can be stable while the code it CALLS changed.
        # This is the mechanism that actually moved binding_canonical, and it is
        # invisible to a file-local comparison -- check it before believing any
        # "cosmetic" verdict.
        drifted = local_import_drift(producer, src_text, sha)
        if drifted:
            entry["import_drift"] = drifted
            classes["cosmetic_import_cone_drift"].append(entry)
            continue

        if not any(k in src_text for k in ("WitnessBuilder", "scriptHash", "commitSha")):
            entry["reason"] = "producer writes no provenance — a re-run would strip it"
            classes["cosmetic_strips_provenance"].append(entry)
            continue

        missing = env_gap(w)
        if missing:
            entry["env_gap"] = missing
            classes["cosmetic_env_differs"].append(entry)
        else:
            classes["cosmetic"].append(entry)

    return classes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", choices=["cosmetic", "cosmetic_env_differs",
                                       "cosmetic_import_cone_drift",
                                       "cosmetic_strips_provenance",
                                       "substantive", "rewritten",
                                       "unresolvable", "unparseable"])
    ap.add_argument("--witness", action="store_true",
                    help="write witness-staleness-triage.witness.json")
    args = ap.parse_args()

    classes = triage()
    total = sum(len(v) for v in classes.values())

    print("=" * 74)
    print("SELF-STALE WITNESS TRIAGE — which drifts can move a number")
    print("=" * 74)
    print(f"  self-stale witnesses decided   : {total}")
    for name, label in (
        ("substantive", "code changed — a re-run CAN move the payload"),
        ("cosmetic", "source cosmetic AND environment matches — safe to refresh"),
        ("cosmetic_env_differs", "source cosmetic BUT environment differs — DO NOT refresh"),
        ("cosmetic_import_cone_drift", "source cosmetic BUT an imported module changed — DO NOT refresh"),
        ("cosmetic_strips_provenance", "source cosmetic BUT a re-run deletes provenance"),
        ("rewritten", "commitSha not in the repo — undecidable, see below"),
        ("unresolvable", "no commitSha, or producer moved since"),
        ("unparseable", "producer not valid Python 3 on this interpreter"),
    ):
        n = len(classes[name])
        pct = f"{100 * n / total:5.1f}%" if total else "    —"
        print(f"    {name:<13} {n:>5}  {pct}   {label}")
    print()
    print("  'cosmetic' means a re-run cannot change the payload. It does NOT")
    print("  mean the witness is correct — a stale-but-cosmetic witness can")
    print("  still carry a wrong number from a producer that was already wrong.")
    if classes["rewritten"]:
        print()
        print("  'rewritten': the recorded commitSha resolves to nothing. These are")
        print("  not damaged witnesses — the commit existed when they were written.")
        print("  Rebase-merge (AGENTS.md rule 8) rewrote every branch commit sha, so")
        print("  a witness produced on a feature branch records a sha that the merge")
        print("  itself destroyed. AGENTS.md already says this of scriptCommitSha;")
        print("  it is equally true of commitSha, and nothing branch-side can fix it.")
        print("  Consequence: 'git diff the producer first' is UNRUNNABLE for these,")
        print("  so a re-run is the only way to decide them. Price that before")
        print("  spending an idle pass on an expensive one.")

    if args.list:
        print()
        for e in classes[args.list]:
            extra = f"  [{e['reason']}]" if "reason" in e else ""
            print(f"  {e['witness']}\n      producer {e['producer']}"
                  f"  {e['recorded']} -> {e['current']}{extra}")

    if args.witness:
        out = COMPUTATIONS / "witness-staleness-triage.witness.json"
        out.write_text(json.dumps({
            "computation": "witness-staleness-triage",
            "scriptFile": "witness_staleness_triage.py",
            "scriptHash": hashlib.sha256(
                Path(__file__).read_bytes()).hexdigest()[:12],
            "commitSha": (_git("rev-parse", "HEAD") or "unknown").strip(),
            "description": (
                "Splits self-stale witnesses by whether re-running the producer "
                "could change the payload. Normalisation drops comments, "
                "docstrings and formatting via ast.unparse; equality of the "
                "normalised sources means a re-run is bookkeeping only."
            ),
            "scope": (
                "scope-(a): decides only whether a re-run can move the payload. "
                "Says nothing about whether a witness is numerically correct, "
                "and ignores scriptCommitSha, which rebase-merge rewrites."
            ),
            "counts": {k: len(v) for k, v in classes.items()},
            "data": classes,
        }, indent=1))
        print(f"\nWrote {out.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
