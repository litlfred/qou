#!/usr/bin/env python3
"""Extract the latest ⟦PROGRESS⟧/⟦DONE⟧ block from each dispatched agent.

Used by the `local/dispatch-agent` skill's 2-minute heartbeat. Reads each
`<agentId>.output` JSONL transcript in the given tasks dir and prints ONLY
the most recent progress block per agent — never the whole transcript
(which would overflow the parent's context).

Usage:
    python3 scripts/agent-progress.py <tasks-dir>

The tasks dir is the folder holding the `<agentId>.output` files; the
dispatch tool result names each agent's `output_file`, whose parent
directory is the tasks dir.
"""
import json
import os
import sys
import glob


def latest_block(path: str):
    """Return (block_text, is_done) for the last progress block, or (None, False)."""
    last = None
    try:
        with open(path) as fh:
            for line in fh:
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                if not isinstance(obj, dict):
                    continue
                msg = obj.get("message")
                if not isinstance(msg, dict):
                    continue
                for chunk in (msg.get("content") or []):
                    if isinstance(chunk, dict) and chunk.get("type") == "text":
                        text = chunk.get("text", "")
                        if "⟦PROGRESS⟧" in text or "⟦DONE⟧" in text:
                            idx = max(
                                text.rfind("⟦PROGRESS⟧"),
                                text.rfind("⟦DONE⟧"),
                            )
                            head = text.rfind("###", 0, idx)
                            last = text[head:] if head >= 0 else text
    except FileNotFoundError:
        return None, False
    is_done = bool(last and "⟦DONE⟧" in last)
    return last, is_done


def is_agent_output(path: str) -> bool:
    """True iff `path` is an AGENT transcript rather than a Bash job's stdout.

    The session tasks dir holds `<id>.output` for BOTH, and the glob fallback
    in `main()` cannot tell them apart by name. Measured 2026-10-10: a
    heartbeat over a dir with one agent and six backgrounded Bash commands
    printed seven rows, six of them `[live] (no progress block yet — agent
    still spinning up)` — for `pip install`, `setup-folio-assistant.sh` and a
    `precision-gates.sh` run. They never advance, because a Bash job does not
    emit `⟦PROGRESS⟧` blocks, so they read as permanently-hung agents and
    invite a `SendMessage` nudge to something that cannot receive one.

    Worse, it hides a real signal: one of those six had **timed out**
    (`GATE_EXIT=124`) and its row said "spinning up".

    The discriminator is the first line. An agent transcript is JSONL whose
    first record is a dict carrying `isSidechain`/`parentUuid`/`promptId`;
    Bash stdout is arbitrary text. Checking the first line only keeps this
    O(1) per file, which matters because the heartbeat runs every 120 s.
    """
    try:
        with open(path) as fh:
            first = fh.readline(4096).lstrip()
    except OSError:
        return False
    if not first.startswith("{"):
        return False
    try:
        obj = json.loads(first)
    except Exception:
        # A truncated first JSON line still indicates JSONL; a Bash job that
        # happens to print `{...}` as its first line does not. Require one of
        # the transcript-shaped keys to appear in the raw text.
        return any(k in first for k in ("isSidechain", "parentUuid", "promptId"))
    return isinstance(obj, dict) and any(
        k in obj for k in ("isSidechain", "parentUuid", "promptId", "message")
    )


def read_map(tasks: str) -> dict:
    """Map agentId -> label from a `dispatch-map.txt` beside the tasks dir.

    Without this the extractor reports EVERY `*.output` in the session tasks
    dir, including hundreds left by earlier dispatches, which buries the live
    agents and makes the heartbeat table unreadable.
    """
    labels = {}
    path = os.path.join(os.path.dirname(tasks.rstrip("/")), "dispatch-map.txt")
    try:
        with open(path) as fh:
            for line in fh:
                if "=" in line:
                    aid, label = line.split("=", 1)
                    labels[aid.strip()] = label.strip()
    except FileNotFoundError:
        pass
    return labels


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    tasks = sys.argv[1]
    labels = read_map(tasks)
    if labels:
        outputs = [os.path.join(tasks, aid + ".output") for aid in labels]
    else:
        # No dispatch map: fall back to the glob, but keep only genuine agent
        # transcripts. A Bash job's stdout lands here too and would otherwise
        # be reported as a hung agent -- see `is_agent_output`.
        allout = sorted(glob.glob(os.path.join(tasks, "*.output")))
        outputs = [p for p in allout if is_agent_output(p)]
        skipped = len(allout) - len(outputs)
        if skipped:
            print(f"(skipped {skipped} non-agent .output file(s) — "
                  f"backgrounded Bash jobs, not agents)\n")
    if not outputs:
        print(f"(no agent output files in {tasks})")
        return 0
    for path in outputs:
        aid = os.path.basename(path)[:-len(".output")]
        block, done = latest_block(path)
        tag = "[DONE]" if done else "[live]"
        print(f"===== {labels.get(aid, aid[:12])} {tag} =====")
        if block:
            print(block.strip()[:900])
        else:
            print("(no progress block yet — agent still spinning up)")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
