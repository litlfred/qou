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
                for chunk in (obj.get("message", {}).get("content") or []):
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


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    tasks = sys.argv[1]
    outputs = sorted(glob.glob(os.path.join(tasks, "*.output")))
    if not outputs:
        print(f"(no agent output files in {tasks})")
        return 0
    for path in outputs:
        aid = os.path.basename(path)[:-len(".output")]
        block, done = latest_block(path)
        tag = "[DONE]" if done else "[live]"
        print(f"===== {aid[:12]} {tag} =====")
        if block:
            print(block.strip()[:900])
        else:
            print("(no progress block yet — agent still spinning up)")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
