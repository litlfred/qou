#!/usr/bin/env python3
"""Ratchet on NEWLY-unstamped witnesses: the gate that stops the q0Anchor refill.

The problem this exists for
---------------------------
``q0_anchor_consistency_audit.py`` counts witnesses with no top-level
``q0Anchor`` and calls the state ``Q0_ANCHOR_MISSING``. It IS wired into
``scripts/precision-gates.sh`` and ``witness-staleness.yml`` with ``--strict``,
but ``--strict`` there exits non-zero on ``Q0_FLIP`` **only** (its line 328) ---
and ``Q0_FLIP`` is 0. Its own header calls ``Q0_ANCHOR_MISSING``
*"pre-backfill; not a failure"*.

That is the right call for a *contradiction* detector: a missing anchor is not a
contradiction, and failing 1678 pre-existing witnesses would brick every commit.
The consequence, though, is that **nothing blocks the inflow**. Measured on
witness files newly ADDED to ``main`` (two independent methods agreeing exactly:
diffing added files, and this ratchet's own set-difference between revisions):

    origin/main~500..HEAD   60 of 101 arrived unstamped   (59.4%)
    origin/main~250..HEAD   20 of  44                     (45.5%)
    origin/main~100..HEAD   16 of  31                     (51.6%)

About half of every new witness lands with no anchor, so the standing population
is refilled as fast as it is drained --- 2015 on 2026-08-25, 2066 two days
later. A per-witness drain cannot win against that, and the ``UNDECLARED`` class
it runs through spans **1149 distinct producers**, so a per-producer drain
cannot either.

What this gate does
-------------------
The repo's own answer to "tolerate a backlog, refuse new arrivals" is a draining
ratchet (``witness_raw_float64_audit.py`` + ``raw-float64-baseline.json``). This
is that, for the anchor:

* the existing unstamped population is recorded in
  ``computations/q0-anchor-missing-baseline.json`` and tolerated;
* under ``--strict``, an unstamped witness **not in the baseline fails**;
* the baseline **drains, never grows** --- ``--rebaseline`` refuses to write a
  larger file.

It also catches a class the added-file diff structurally cannot: a witness that
**already existed and LOST its stamp**. That is not hypothetical. Validating
this gate against history turned up
``computations/signed-crossing-feasibility.witness.json``, whose anchor has
oscillated ``muon`` -> missing -> ``muon`` -> missing across four commits. It was
backfilled to ``muon`` in ``4101909790``, then dropped again by ``5baf5a45c3``
--- a commit whose subject reads *"register the producer's real pin"*, and which
did add the stem to the manifest under ``physical_proton``. The declaration had
no effect, because that producer ends in
``out.write_text(json.dumps(w, indent=2))`` and never enters ``build()``, where
the manifest is read. A count-based check cannot see any of this; the count went
up by one and looked like ordinary drift.

Why this does not "default a pin in"
------------------------------------
``WitnessBuilder.build()`` deliberately leaves an undeclared producer unstamped,
because inventing a pin would assert one nobody established. **That principle is
untouched here.** This gate never writes an anchor and never guesses one. It
refuses only to let a *new* witness arrive with the question unanswered, and the
producer author has three honest, cheap answers, all of which satisfy it:

* reads q₀ --> declare the stem in ``computations/q0_anchor_manifest.json``
  (``physical_proton`` is the standing default for new compute); the builder
  then stamps it. **Only works if the producer uses ``WitnessBuilder``** --- see
  ``INERT_DECLARATION`` in ``q0_anchor_missing_cause_partition.py``;
* never reads q₀ --> ``w.save({"q0Anchor": "independent",
  "q0AnchorReason": "<why>"})``, and **no** ``q0Value`` (one there is a
  ``Q0_FLIP``);
* reads q₀ but the pin is genuinely undetermined --> ``"ambiguous"`` with a
  ``q0AnchorReason`` naming what is undetermined.

Trap, inherited from bean ``qou-kx04``: use ``save(extra=...)``.
``add_data("q0Anchor", ...)`` nests the field under ``data``, where every reader
--- here and in the consistency audit, all of which read ``body["q0Anchor"]`` ---
is blind to it. The witness stays classified missing with the field visibly
present in the file.

Known limitation, not papered over: a **rename** of a baselined witness reads as
NEW and fails. The two ways out --- declare the producer, or drain the entry ---
are both the direction this gate wants anyway.

Usage
-----
    python3 computations/audits/q0_anchor_ratchet.py            # report
    python3 computations/audits/q0_anchor_ratchet.py --strict   # exit 1 on NEW
    python3 computations/audits/q0_anchor_ratchet.py --rebaseline           # drain only
    python3 computations/audits/q0_anchor_ratchet.py --rev origin/main ...  # rev-pinned

``--strict`` defaults to the WORKING TREE, because a gate must check what you are
about to commit. ``--rev`` reads from git instead, which is what the baseline was
generated with and what makes a reported number reproducible by anyone naming the
same revision --- this repo is worked by several agents against a shared
checkout, and a branch switch mid-measurement is a real failure mode here.

Scope is imported from ``q0_anchor_consistency_audit`` so the two cannot drift:
same ``AUDIT_SUFFIXES``, same skip of ``_deprecated``.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tarfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
BASELINE = REPO / "computations" / "q0-anchor-missing-baseline.json"

sys.path.insert(0, str(HERE))
try:
    from q0_anchor_consistency_audit import AUDIT_SUFFIXES
except ImportError:
    AUDIT_SUFFIXES = (
        "-audit.witness.json",
        "-scan.witness.json",
        "-compliance.witness.json",
    )


def _is_in_scope(name: str) -> bool:
    if "_deprecated" in Path(name).parts:
        return False
    return not any(name.endswith(suf) for suf in AUDIT_SUFFIXES)


def scan_worktree() -> list[str]:
    out: list[str] = []
    for wp in sorted((REPO / "computations").rglob("*.witness.json")):
        rel = str(wp.relative_to(REPO))
        if not _is_in_scope(rel):
            continue
        try:
            body = json.loads(wp.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue  # the consistency audit owns Q0_PARSE_ERROR
        if isinstance(body, dict) and not body.get("q0Anchor"):
            out.append(rel)
    return out


def scan_rev(rev: str) -> list[str]:
    p = subprocess.Popen(
        ["git", "archive", "--format=tar", rev, "computations/"],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd=str(REPO),
    )
    out: list[str] = []
    with tarfile.open(fileobj=p.stdout, mode="r|") as tf:
        for m in tf:
            if not (m.isfile() and m.name.endswith(".witness.json")):
                continue
            if not _is_in_scope(m.name):
                continue
            f = tf.extractfile(m)
            if f is None:
                continue
            try:
                body = json.loads(f.read())
            except json.JSONDecodeError:
                continue
            if isinstance(body, dict) and not body.get("q0Anchor"):
                out.append(m.name)
    p.wait()
    return sorted(out)


def load_baseline(path: Path) -> set[str]:
    try:
        return set(json.loads(path.read_text(encoding="utf-8")).get("files", []))
    except (OSError, json.JSONDecodeError):
        return set()


def write_baseline(path: Path, files: list[str], prev: set[str], rev: str,
                   establish: str | None = None) -> int:
    """Write the baseline. Growth is refused unless deliberately `establish`ed.

    The drain-only rule has one legitimate exception, and leaving it
    undocumented would be worse than naming it: while this gate's own PR is
    open, main keeps moving, and unstamped witnesses that land there are not
    this branch's doing. Without an exception the gate blocks its own landing
    and the only way through is to delete the baseline file so `prev` is empty
    --- an escape hatch that exists either way, but silently.

    So growth is permitted ONLY with `--establish "<reason>"`, which records the
    reason and the exact grown entries INTO the file, where a reviewer sees them
    in the diff. It must never be used to absorb a witness your own branch
    created; that is the refill this gate exists to stop.
    """
    grew = sorted(set(files) - prev)
    if prev and len(files) > len(prev) and not establish:
        print(
            f"REFUSED: --rebaseline would GROW the baseline "
            f"{len(prev)} -> {len(files)}.\n"
            "Baselines drain, never grow. Those entries are a refill: declare "
            "their producers, or have them record an honest q0Anchor.\n"
            "If and ONLY if they landed on main independently of your branch, "
            "re-establish deliberately:\n"
            '    --rebaseline --establish "rebased onto <sha>; these arrived on '
            'main, not from this branch"',
            file=sys.stderr,
        )
        for f in grew[:20]:
            print(f"    NEW {f}", file=sys.stderr)
        return 1
    path.write_text(json.dumps({
        "note": (
            "Witnesses carrying no top-level q0Anchor when this ratchet was "
            "introduced. A TOLERATED BACKLOG, not approval. Enforced by "
            "computations/audits/q0_anchor_ratchet.py; attributed by cause in "
            "computations/audits/q0_anchor_missing_cause_partition.py."
        ),
        "enforced_rule": (
            "An unstamped witness NOT listed here fails --strict. This list "
            "DRAINS ONLY: --rebaseline refuses to write a larger file. Never "
            "add an entry to silence a red gate. Fix it at the producer — "
            "declare the stem in q0_anchor_manifest.json (only effective if the "
            "producer uses WitnessBuilder), or record q0Anchor "
            "independent/ambiguous with a q0AnchorReason via save(extra=...)."
        ),
        "generated_from_rev": rev,
        **({"established": {
            "reason": establish,
            "grew_by": len(grew),
            "entries_added": grew,
        }} if establish and grew else {}),
        "drain_owner": "bean qou-y98b (refill gate); qou-1c4y (muon migration)",
        "files_count": len(files),
        "files": sorted(files),
    }, indent=2) + "\n", encoding="utf-8")
    print(f"baseline written from {rev}: {len(prev)} -> {len(files)}")
    return 0



def selftest() -> int:
    """Prove the gate can still SEE a new unstamped witness.

    A detector that has quietly gone blind reports a clean tree, which is
    indistinguishable from success --- this corpus has the scar: a name-keyed
    accessor audit reported zero hits after a narrowing, and the zero was the
    narrowing, not the tree. So the self-test asserts the POSITIVE case (a new
    unstamped witness IS caught), not merely that the script runs.

    Four properties, each of which has a way of being refactored away:
      A  a baselined unstamped witness does NOT fire      (backlog tolerated)
      B  a NEW unstamped witness DOES fire                (the whole point)
      C  a stamped witness never fires
      D  an audit-emitted witness (AUDIT_SUFFIXES) is out of scope, so a
         tightening of that list cannot silently swallow real witnesses
    """
    import shutil
    import tempfile

    global REPO, BASELINE
    saved = (REPO, BASELINE)
    tmp = Path(tempfile.mkdtemp(prefix="q0ratchet-selftest-"))
    try:
        (tmp / "computations" / "sub").mkdir(parents=True)
        REPO = tmp
        BASELINE = tmp / "computations" / "q0-anchor-missing-baseline.json"
        BASELINE.write_text(json.dumps(
            {"files_count": 1,
             "files": ["computations/old-unstamped.witness.json"]}))
        (tmp / "computations" / "old-unstamped.witness.json").write_text('{"r":1}')
        (tmp / "computations" / "sub" / "stamped.witness.json").write_text(
            '{"q0Anchor":"proton","q0Value":"1"}')

        base = load_baseline(BASELINE)
        got = set(scan_worktree())
        assert got == {"computations/old-unstamped.witness.json"}, \
            f"A/C: expected only the baselined witness unstamped, got {got}"
        assert not (got - base), "A: a baselined witness fired"

        new_w = tmp / "computations" / "sub" / "brand-new.witness.json"
        new_w.write_text('{"r":2}')
        got = set(scan_worktree())
        assert (got - base) == {"computations/sub/brand-new.witness.json"}, \
            f"B: a NEW unstamped witness was NOT caught — the gate is blind. {got - base}"

        new_w.rename(new_w.with_name("brand-new-audit.witness.json"))
        got = set(scan_worktree())
        assert not (got - base), "D: an audit-emitted witness fired"
    finally:
        REPO, BASELINE = saved
        shutil.rmtree(tmp, ignore_errors=True)
    print("selftest OK: A backlog tolerated, B new caught, C stamped ignored, "
          "D audit-emitted out of scope")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any unstamped witness is not in the baseline")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (draining only)")
    ap.add_argument("--rev", help="measure this git revision instead of the "
                                  "working tree (reproducible; immune to a "
                                  "concurrent branch switch)")
    ap.add_argument("--baseline", help="use this baseline file instead")
    ap.add_argument("--establish", metavar="REASON",
                    help="permit --rebaseline to GROW, recording REASON and the "
                         "added entries in the file. ONLY for entries that "
                         "landed on main independently of your branch (e.g. "
                         "rebasing this gate's own PR). Never to absorb a "
                         "witness your branch created.")
    # `--self-test` is the spelling scripts/precision-gates.sh invokes
    # (its line 467). `--selftest` is accepted as an alias so a hand-run does
    # not have to remember which. Getting this wrong is silent in the harness:
    # a self-test that errors on an unknown flag is indistinguishable from one
    # that fails, and both just print the gate name.
    ap.add_argument("--self-test", "--selftest", dest="self_test",
                    action="store_true",
                    help="prove the gate still catches a new unstamped witness")
    args = ap.parse_args()

    if args.self_test:
        return selftest()

    baseline_path = Path(args.baseline) if args.baseline else BASELINE
    missing = scan_rev(args.rev) if args.rev else scan_worktree()
    base = load_baseline(baseline_path)

    new = sorted(set(missing) - base)
    drained = sorted(base - set(missing))

    if args.rev:
        # Record the resolved sha, not the ref name. A baseline stamped
        # "origin/main" documents nothing a month later, when origin/main has
        # moved a thousand commits; a sha is re-measurable forever.
        _sha = subprocess.run(["git", "rev-parse", args.rev], capture_output=True,
                              text=True, cwd=str(REPO)).stdout.strip()
        src = f"{args.rev} ({_sha})" if _sha else args.rev
    else:
        src = "working tree"
    print(f"source                           : {src}")
    print(f"unstamped witnesses (live scope) : {len(missing)}")
    print(f"baseline                         : {len(base)}  ({baseline_path.name})")
    print(f"  drained since baseline         : {len(drained)}")
    print(f"  NEW (not in baseline)          : {len(new)}")

    if drained:
        print("\ndrained — regenerate the baseline to bank these:")
        for f in drained[:15]:
            print(f"    - {f}")
        if len(drained) > 15:
            print(f"    … and {len(drained) - 15} more")

    if new:
        print("\nNEW unstamped witnesses — this is the refill:")
        for f in new:
            print(f"    + {f}")
        print(
            "\nEach needs ONE of these AT THE PRODUCER (never hand-edit the JSON):\n"
            "  reads q0       -> declare the stem in computations/q0_anchor_manifest.json\n"
            "                    UNDER physical_proton OR ideal_muon (proton is the standing\n"
            "                    default for new compute); the builder then stamps it.\n"
            "                    TWO ways this silently does nothing:\n"
            "                      * the producer hand-rolls json.dump and never enters\n"
            "                        build(), where the manifest is read; or\n"
            "                      * the stem is declared under `ambiguous`. build() writes\n"
            "                        the stamp only `if _a in (\"muon\", \"proton\")`, so an\n"
            "                        `ambiguous` entry resolves correctly and is then\n"
            "                        DISCARDED. Measured 2026-08-29: 19 stems are declared\n"
            "                        ambiguous, 9 of their witnesses are unstamped, and every\n"
            "                        `ambiguous` stamp in the corpus came from the PRODUCER,\n"
            "                        never from the manifest. Bean qou-fl0a.\n"
            "  never reads q0 -> w.save({'q0Anchor': 'independent',\n"
            "                            'q0AnchorReason': '<why>'})  and NO q0Value\n"
            "  undetermined   -> 'ambiguous' + a q0AnchorReason naming what is undetermined.\n"
            "                    MUST be producer-side (see above) — a manifest `ambiguous`\n"
            "                    entry cannot satisfy this gate.\n"
            "Use save(extra=...), NOT add_data() — add_data nests the field under 'data',\n"
            "where every reader is blind to it (bean qou-kx04)."
        )

    if args.rebaseline:
        return write_baseline(baseline_path, missing, base, src, args.establish)

    if args.strict and new:
        print(f"\nFAIL (--strict): {len(new)} witness(es) newly unstamped.")
        return 1
    if args.strict:
        print("\nPASS (--strict): no new unstamped witnesses.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
