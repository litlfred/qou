"""Shared `lean_uniqueness_ref` metadata for per-nucleus witness producers.

Centralises the duplicated theorem / framework_doc / note fields that
per-nucleus producers attach to their witness JSON via
``builder.add_data("lean_uniqueness_ref", ...)`` — one place to update
if the theorem name, framework module path, or workplan moves.

Wiring pattern (Phase 3 of the 2026-06-09 strategy doc;
docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md):

    from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
    ...
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("deuteron (²H)"))

Dependency-free on purpose: importable without the heavy compute stack.
"""

NUCLEUS_EMPTY_SDP_THEOREM = (
    "qou:QOU.BraidKnot.NucleusEmptySDPUniqueness.nucleus_uniqueness_closed "
    "(parameterised by crossing count n)"
)

FRAMEWORK_DOC = (
    "content/quantum-observable-universe/lean/QOU/BraidKnot/"
    "NucleusEmptySDPUniqueness.lean"
)

NOTE = (
    "T_w uniqueness at the abstract empty-constraint SDP level "
    "(PR #1537/#1542 parameterised module). Workplan: "
    "docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md."
)


def lean_uniqueness_ref(
    nucleus: str,
    theorem: str = NUCLEUS_EMPTY_SDP_THEOREM,
) -> dict:
    """Return the standard `lean_uniqueness_ref` payload for `nucleus`.

    Pass a different `theorem` once a real (non-empty-constraint) SDP
    uniqueness theorem lands for the nucleus (Phase 1 of the strategy
    doc).
    """
    return {
        "nucleus": nucleus,
        "theorem": theorem,
        "framework_doc": FRAMEWORK_DOC,
        "note": NOTE,
    }
