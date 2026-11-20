---
# qou-rug0
title: Fixed-.parent-count path resolution is wrong in the vendored layout — audit the remaining shims
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T10:32:58Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---

`_precision.py`, `q_parameter.py` and `witness_base.py` all carried the same
broken snippet for locating the substrate checkout — a fixed `.parent` count that
was wrong in **both** layouts the file lives in. Those four copies are fixed
(upward search). But the wider corpus has the same *shape* at many different
depths, and those have not been audited.

## The bug class

A module computes a repo-relative path by counting `.parent` levels from
`__file__`. That count is layout-specific, and these files live in two layouts:

    computations/substrate/x.py                  -> repo root is 3 up
    qou-mass/src/qou_mass/_internal/x.py         -> repo root is 5 up

The vendor sync flattens the tree, so any fixed count is wrong somewhere. It
stays invisible because `import _path_bridge` normally resolves the import first
— and the sync STRIPS that import, which is exactly when the fallback is needed.

## Already fixed (upward search)

    computations/substrate/_precision.py     (+ vendored copy)
    computations/substrate/q_parameter.py    (+ vendored copy)
    computations/substrate/witness_base.py   (+ vendored copy)

Also `_li_2_q_util.py::_Q_WITNESS_DEFAULT`, which assumed
`Path(__file__).parent / "q-pinning-50-digit.witness.json"` — right for
computations/, wrong for the vendored layout where the witness sits one level up.

## Not audited

A scan for `Path(__file__).resolve()` followed by chained `.parent` finds the
same shape at 1, 2 and 3 levels across `computations/`, `computations/deltalambda/`,
`computations/qbeta/` and others. Each needs its own read — a bare count is not
automatically wrong, only wrong if that file is (or becomes) vendored, or is
moved between directory depths. Both have happened here: the Phase-6 refactor
moved substrate modules into `substrate/` and the comment in the broken snippet
shows someone incrementing the count by hand to compensate, and getting it wrong.

## Suggested fix

Prefer searching upward for a landmark (`tools/qou-substrate/python`, or a
`.git` / `pyproject.toml` marker) over counting levels. A small shared helper in
the substrate package would let the shims stop duplicating the snippet — the
three fixed here were byte-identical copies, which is why one bug appeared three
times.

## How this surfaced

The vendored `mass_at_3A_proper.tower_term_li2q` raised
`ModuleNotFoundError: No module named 'qou_substrate'` from `q_parameter.py:56`.
After the fixes it gets through to `pyhecke`, a genuine optional native
dependency, which is a different and legitimate failure.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8411, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
