#!/usr/bin/env python3
"""Split self-stale witnesses by whether refreshing them is safe, or even useful.

`witness_dependency_drift.py` reports every witness whose `scriptHash` no longer
matches its producer. It cannot say *why*, because `scriptHash` is a whole-file
SHA-256: a docstring edit drifts it exactly as loudly as a changed formula. The
idle-backlog policy caps witness refreshes at 3 per pass and tells the agent to
`git diff` the producer first for precisely this reason (AGENTS.md §4, and the
worked case `canonical-ordering-dof`, which drifted on +21 lines that are *all*
comment).

At the current backlog — 700 self-stale of 2985 — "diff it first" is advice no
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

If they are identical, **the source cannot explain a payload change — but the
environment still can**, so a second gate applies. A producer may branch on what
is *installed*, and then the same source in a different environment writes a
different payload, silently, with no crash and no warning. Measured while
building this: `binding_canonical.py` re-run without `pyhecke_native` gives
`tr_M_atom = 0.575` where the committed witness has `0.388` — a 48 % move under
an unchanged AST. Committing that would have replaced a Rust-backed value with a
pure-Python fallback under a `chore(witness)` message. So:

A third gate is subtler still: some producers write a **bare** witness and never
emit provenance — the `scriptHash` / `commitSha` / `environment` block on disk
was added downstream. Re-running one of those *deletes the fields the drift
audit keys on*, making the witness permanently undecidable. Measured on
`d_u_closed_form_proof.py` and `yekutieli_volume_join.py`: 15 keys in, 7 and 9
keys out. Rare — 1 of 80 sampled producers — but both `cosmetic` candidates in
this corpus hit it, because bare producers are the old ones and old producers
are what drift.

  * `cosmetic`                   — source cosmetic, environment matches, and the
    producer writes its own provenance. Safe to refresh; only provenance moves.
  * `cosmetic_env_differs`       — **do not refresh.** Provision first, or leave.
  * `cosmetic_strips_provenance` — **do not refresh.** Fix the producer to emit
    provenance first; refreshing destroys the audit trail.

**The measured result on this corpus is `cosmetic = 0`.** Of 700 self-stale
witnesses, not one is safe to refresh by the naive "re-run the producer" advice.
That is the finding, not a limitation of the script: the idle-pass witness
budget has nothing to spend itself on here, and an agent that spends it anyway
is doing damage rather than maintenance.

**It is not a snapshot.** Re-measured three times across 1564 commits of main
(2026-08-11 and twice on 2026-08-19, corpus 2898 -> 2985 witnesses), `cosmetic`
came back 0 every time, and the class shape barely moved:

    2026-08-11   substantive 242   rewritten 329   unresolvable 107   cosmetic 0
    2026-08-19   substantive 239   rewritten 329   unresolvable 106   cosmetic 0
    2026-08-19   substantive 256   rewritten 338   unresolvable 103   cosmetic 0

So this is structural, not a bad week. Meanwhile main spent 45 `chore(witness)`
commits over those same 8 days, 13 of them titled "refresh provenance sha after
rebase" — hand-patching the `commitSha` of the `rewritten` class, which is
nearly half the backlog and which no branch-side edit can durably fix.

Three honest residual classes, reported separately rather than folded in:

  * `rewritten`    — the recorded `commitSha` resolves to nothing. Not damage:
    rebase-merge (AGENTS.md rule 8) rewrites every branch commit sha, so a
    witness produced on a feature branch records a sha the merge destroyed.
    AGENTS.md says this of `scriptCommitSha`; it is equally true of `commitSha`.
    Consequence: "diff the producer first" is unrunnable for these.
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


def find_producer(script_file: str) -> Path | None:
    """Resolve a witness `scriptFile` to a path under computations/."""
    direct = COMPUTATIONS / script_file
    if direct.is_file():
        return direct
    hits = list(COMPUTATIONS.rglob(script_file))
    return hits[0] if len(hits) == 1 else None


def triage() -> dict:
    classes: dict[str, list] = {
        "cosmetic": [], "cosmetic_env_differs": [],
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
