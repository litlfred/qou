#!/usr/bin/env python3
"""Resolve `beans/defs/*.md` merge conflicts that are pure concurrent APPENDS.

WHY THIS EXISTS
---------------
Beans are an append-only ledger, and several in-flight branches append a
session note to the same bean. Git sees two different additions at the same
end-of-file offset and calls it a conflict every time, even though the
resolution is never in doubt: keep both notes.

Measured on `main`, 2026-09-13:

    main                                  169 commits / 24 h  (~1 per 9 min)
    beans/defs/qou-brng--...derive-saturated    9 commits / 24 h
    beans/defs/qou-zlra--...is-graded-binding   6 commits / 24 h

so a branch that appends to `qou-brng` goes un-mergeable roughly every 2.7 h.
In one session, PRs #7237 / #7245 / #7251 / #7253 collided on these two files
five separate times; `qou-brng` alone conflicted three times in ~40 minutes,
twice while a resolution for the previous collision was being committed. Four
of the five collision surfaces across that cluster were these two ledgers.
None of them involved content, Lean, compute or a witness.

WHAT IT REFUSES TO DO
---------------------
It is deliberately narrow, because a bean can also be *edited*, and an edit is
a real conflict that a human must read. It exits 2 without writing anything
unless EVERY unmerged path is:

  * under `beans/defs/` and ending `.md`, and
  * a PURE APPEND on BOTH sides -- each side's BODY must literally start with
    the merge-base body.

So a side that rewrote an existing paragraph, reordered notes, or deleted
anything is never touched. The failure mode is "refuses to help", never
"silently drops someone's edit".

THE APPEND TEST APPLIES TO THE BODY, NOT THE FRONTMATTER (fixed 2026-10-10)
---------------------------------------------------------------------------
It used to apply to the whole file, masking only the single `updated_at:` line.
That made the script **refuse every bean conflict on current `main`**, because
the 2026-10-04 reorg (`58a1f3231c`, bean `qou-utbr`) INSERTS frontmatter keys
-- `priority:`, `tags:`, `parent:` -- into the middle of the block. An
insertion is not an append, so `theirs.startswith(base)` is false and the
script bailed with *"THEIRS is not a pure append (existing text changed)"* on
files whose bodies were textbook concurrent appends. Reproduced exactly; the
first divergence lands on `priority: normal` where the base has `created_at:`.

Measured consequence: a sub-agent resolving PR #7318 had **all six** of its
bean conflicts refused by the shipped script and resolved them by hand, which
is precisely the work AGENTS.md says is not winnable by hand at `main`'s commit
rate.

The split is the right fix rather than a wider mask because **a bean body and
a bean frontmatter are different kinds of object**, and AGENTS.md says so: *"A
bean is an APPEND-ONLY ledger"* describes the body. The frontmatter is a
mutable record -- `status:` moves through the bean's lifecycle, `parent:` is
re-pointed, keys are added by tooling -- so a pure-append assertion over it is
not merely too strict, it is the wrong predicate. Masking one more key would
have failed again on the next key the tooling adds.

Diagnosis note, recorded because it was wrong in a plausible way: the
sub-agent's report attributed the refusal to the script *"comparing ours-vs-
theirs on the frontmatter"* and recommended comparing ours-vs-base. The script
already compares both sides against the base (`o.startswith(b)` /
`t.startswith(b)`); the cause was the frontmatter being in scope at all. The
symptom was real and the remedy direction right, but the mechanism named was
not the code's.

WHAT IT GUARANTEES WHEN IT DOES WRITE
-------------------------------------
The merged file is asserted, before being written, to satisfy all of:

  * `theirs` (main) body preserved byte-for-byte as a prefix;
  * `ours` (the branch's) new note present verbatim;
  * `len(merged_body) == len(theirs_body) + len(ours_note)` -- nothing invented;
  * `theirs` frontmatter taken verbatim, with exactly one `updated_at:` key set
    to the later of the two timestamps.

If any assertion fails it raises rather than writing a half-merged ledger.

ONE THING IT DROPS, AND IT SAYS SO
----------------------------------
Taking `theirs` frontmatter verbatim is what keeps `main` byte-for-byte, and it
means a frontmatter change made ONLY on the branch (a `status:` the branch
moved, a `parent:` it re-pointed) is overwritten by main's value. That is
almost always right -- main is where the reorg and the lifecycle updates land
-- but it is a loss, so the script compares `ours` frontmatter against the
BASE and prints every key where they differ. Re-apply those with
`beans update` after committing. It is a warning rather than a refusal because
the body merge is still lossless and refusing would send you back to the hand
resolution this script exists to replace.

USAGE
-----
    git merge origin/main            # conflicts
    python3 scripts/bean-append-merge.py
    git commit

    python3 scripts/bean-append-merge.py --selftest   # no git needed

Exit codes: 0 = all conflicts resolved (or none present), 2 = at least one
conflict is not a pure append and needs a human.
"""
import subprocess
import re
import sys


def _show(stage: int, path: str):
    """Return one merge stage of `path`, or None if that stage is absent."""
    r = subprocess.run(["git", "show", f":{stage}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def _ts(text: str) -> str:
    m = re.search(r'^updated_at: (.*)$', text, flags=re.M)
    return m.group(1).strip() if m else ""


#: A bean file is `---\n<frontmatter>\n---\n<body>`. The split point is the END
#: of the second `---` line, so `fm + body == text` exactly and nothing is
#: dropped or duplicated by the round trip.
_SPLIT = re.compile(r'\A---\n.*?\n---\n', re.S)


def _split(text: str) -> tuple[str, str]:
    """Return ``(frontmatter_including_both_fences, body)``.

    A bean with no recognisable frontmatter block returns ``("", text)``, so the
    whole file is treated as body and the pure-append test applies to all of it
    -- the old behaviour, which is the safe default for an unexpected shape.
    """
    m = _SPLIT.match(text)
    return (text[:m.end()], text[m.end():]) if m else ("", text)


def _fm_keys(fm: str) -> dict[str, str]:
    """Top-level ``key: value`` pairs of a frontmatter block, for diffing only.

    Indented continuation lines (a `tags:` list) attach to the key above, so a
    changed list shows up as a change on `tags`. Good enough to NAME what
    differs; it is never used to reconstruct the block.
    """
    out: dict[str, str] = {}
    key = None
    for line in fm.splitlines():
        if line in ("---", ""):
            continue
        if line.startswith((" ", "\t")) and key is not None:
            out[key] += "\n" + line
        elif ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            out[key] = val.strip()
    return out


def _merge(path: str, base: str, ours: str, theirs: str):
    """Merge one bean. Returns ``(merged, note_len, dropped_fm_keys)``.

    On refusal returns ``(None, reason, ())`` so the caller can report it.
    Every assertion below is on the BODY; the frontmatter is taken from
    ``theirs`` with ``updated_at`` advanced, per the module docstring.
    """
    base_fm, b = _split(base)
    ours_fm, o = _split(ours)
    theirs_fm, t = _split(theirs)

    if not o.startswith(b):
        return None, "OURS body is not a pure append (existing text changed)", ()
    if not t.startswith(b):
        return None, "THEIRS body is not a pure append (existing text changed)", ()

    ours_note = o[len(b):]
    fm = re.sub(r'^updated_at: .*$',
                f'updated_at: {max(_ts(ours), _ts(theirs))}',
                theirs_fm, count=1, flags=re.M)

    body = t
    if ours_note and not body.endswith("\n"):
        body += "\n"
    body += ours_note
    merged = fm + body

    # Lossless guarantees, asserted before anything is written. All on the body:
    # the frontmatter is main's verbatim and is checked by the prefix test.
    assert merged.startswith(fm), f"{path}: frontmatter not preserved"
    assert body.startswith(t), f"{path}: main's body not preserved"
    assert ours_note in body, f"{path}: the branch's note was lost"
    assert len(body) == len(t) + len(ours_note) + (
        1 if (ours_note and not t.endswith("\n")) else 0
    ), f"{path}: body length mismatch -- invented content?"
    # Scoped to the FRONTMATTER: a bean body routinely quotes `updated_at:`
    # when a note discusses bean staleness, and counting those would make this
    # assertion fail on a correct merge.
    _n_ts = len(re.findall(r'^updated_at:', fm, flags=re.M))
    assert _n_ts == 1, f"{path}: expected exactly one updated_at in the " \
                       f"frontmatter, found {_n_ts}"

    # Frontmatter keys the BRANCH changed relative to the merge base. Those are
    # the ones main's version overwrites -- a loss, so name them. Keys main
    # changed are not a loss; main's value is the one being kept on purpose.
    bk, ok = _fm_keys(base_fm), _fm_keys(ours_fm)
    dropped = tuple(
        k for k in ok
        if k != "updated_at" and bk.get(k) != ok[k] and _fm_keys(fm).get(k) != ok[k]
    )
    return merged, len(ours_note), dropped


def _selftest() -> int:
    """Exercise the one case that made the old version refuse everything.

    No git, no repo state. Fails loudly if the frontmatter-insertion case
    regresses to a refusal, or if a genuine body edit stops being refused.
    """
    BASE = ("---\n# qou-test\ntitle: 'A test bean'\nstatus: todo\ntype: task\n"
            "created_at: 2026-08-01T00:00:00Z\n"
            "updated_at: 2026-08-01T00:00:00Z\n---\n\nBody paragraph one.\n")
    # OURS: the branch appends a note to the body and bumps updated_at.
    OURS = (BASE.replace("updated_at: 2026-08-01T00:00:00Z",
                         "updated_at: 2026-10-09T00:00:00Z")
            + "\n## my note\n\nAppended by the branch.\n")
    # THEIRS: main's 2026-10-04 reorg INSERTS keys mid-frontmatter and appends
    # its own note. This is what the old whole-file append test refused.
    THEIRS = (BASE.replace("type: task\n",
                           "type: task\npriority: normal\ntags:\n"
                           "    - reorg-2026-10-04\n")
                  .replace("updated_at: 2026-08-01T00:00:00Z\n---",
                           "updated_at: 2026-10-04T15:00:00Z\nparent: qou-abcd\n---")
              + "\n## main's note\n\nAppended on main.\n")

    fails = []

    merged, n, dropped = _merge("selftest", BASE, OURS, THEIRS)
    if merged is None:
        fails.append(f"frontmatter-insertion case REFUSED: {n}")
    else:
        for want in ("priority: normal", "- reorg-2026-10-04",
                     "parent: qou-abcd", "Body paragraph one.",
                     "Appended on main.", "Appended by the branch."):
            if want not in merged:
                fails.append(f"merged lost {want!r}")
        if "updated_at: 2026-10-09T00:00:00Z" not in merged:
            fails.append("updated_at is not the later of the two")
        if merged.count("updated_at:") != 1:
            fails.append(f"{merged.count('updated_at:')} updated_at keys")
        if dropped:
            fails.append(f"spurious dropped-key warning: {dropped}")

    # A genuine body EDIT must still refuse -- the safety property.
    EDITED = OURS.replace("Body paragraph one.", "Body paragraph ONE, rewritten.")
    m2, why, _ = _merge("selftest", BASE, EDITED, THEIRS)
    if m2 is not None:
        fails.append("a rewritten body paragraph was NOT refused")

    # A branch-only frontmatter change must be WARNED about, not silently lost.
    OURS_FM = OURS.replace("status: todo", "status: in-progress")
    m3, _, dropped3 = _merge("selftest", BASE, OURS_FM, THEIRS)
    if m3 is None:
        fails.append("branch-only frontmatter change was refused, not warned")
    elif "status" not in dropped3:
        fails.append(f"branch-only `status` change not reported; dropped={dropped3}")

    for f in fails:
        print(f"  FAIL {f}")
    print(f"  selftest: {'PASS' if not fails else f'{len(fails)} FAILURE(S)'}")
    return 0 if not fails else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return _selftest()

    paths = subprocess.run(["git", "diff", "--name-only", "--diff-filter=U"],
                           capture_output=True, text=True).stdout.split()
    if not paths:
        print("no unmerged paths")
        return 0

    refused = []
    for path in paths:
        if not (path.startswith("beans/defs/") and path.endswith(".md")):
            refused.append((path, "not a beans/defs/*.md ledger"))
            continue

        base, ours, theirs = _show(1, path), _show(2, path), _show(3, path)
        if base is None or ours is None or theirs is None:
            refused.append((path, "add/add or delete/modify -- no common base"))
            continue

        merged, note_len, dropped = _merge(path, base, ours, theirs)
        if merged is None:
            refused.append((path, note_len))   # note_len carries the reason
            continue

        with open(path, "w") as fh:
            fh.write(merged)
        subprocess.run(["git", "add", path], check=True)
        print(f"  resolved (lossless): {path}  [+{note_len} ch appended]")
        if dropped:
            print(f"    ⚠ frontmatter: took main's; the branch's own value for "
                  f"{', '.join(sorted(dropped))} is overwritten. Re-apply with "
                  f"`beans update` if still wanted.")

    if refused:
        print("\nREFUSED -- these are not pure appends; resolve by hand:")
        for path, why in refused:
            print(f"  {path}: {why}")
        return 2

    print("all bean conflicts resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
