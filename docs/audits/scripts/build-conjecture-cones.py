#!/usr/bin/env python3
"""Compute downstream cones for the conjectures listed in §5 of the
2026-05-01 deep audit, and render a Markdown report with Mermaid
diagrams + summary tables.

Usage:
    cd content && python3 pipeline/content-graph-analysis.py --json > /tmp/qou-graph.json
    python3 docs/audits/scripts/build-conjecture-cones.py > docs/audits/conjecture-cones.md
"""
import json
import os
import sys
from collections import defaultdict, deque
from pathlib import Path

GRAPH_PATH = os.environ.get("QOU_GRAPH_JSON", "/tmp/qou-graph.json")
if not Path(GRAPH_PATH).exists():
    sys.stderr.write(
        f"error: {GRAPH_PATH} not found.\n"
        "Run: cd content && python3 pipeline/content-graph-analysis.py --json > /tmp/qou-graph.json\n"
    )
    sys.exit(1)

with open(GRAPH_PATH, "r", encoding="utf-8") as f:
    GRAPH = json.load(f)

# Validate the graph schema is the one this script understands. The
# `content-graph-analysis.py` tool emits {chapters, blocks, edges,
# chapter_edges, findings}; bail loudly on any other shape rather than
# silently producing empty cones.
_REQUIRED_KEYS = {"blocks", "edges"}
if not isinstance(GRAPH, dict) or not _REQUIRED_KEYS.issubset(GRAPH.keys()):
    sys.stderr.write(
        f"error: {GRAPH_PATH} does not match the expected "
        f"content-graph-analysis schema (need top-level keys "
        f"{sorted(_REQUIRED_KEYS)}; got {sorted(GRAPH.keys()) if isinstance(GRAPH, dict) else type(GRAPH).__name__}).\n"
        "Regenerate with: cd content && python3 pipeline/content-graph-analysis.py --json\n"
    )
    sys.exit(2)

# Map label → block info
LABEL_TO_BLOCK = {b["label"]: b for b in GRAPH["blocks"]}

# Build forward (uses) and reverse (used-by) adjacency.
# An edge `from -> to` means `from` USES `to` (from depends on to).
# So downstream cone of X = ancestors of X under `uses` = blocks that
# transitively use X.
USES = defaultdict(set)        # label -> set of labels it uses
USED_BY = defaultdict(set)     # label -> set of labels that use it
INTERPRETS = defaultdict(set)  # label -> set of labels it interprets
INTERPRETED_BY = defaultdict(set)

for e in GRAPH["edges"]:
    fr, to, typ = e["from"], e["to"], e["type"]
    if typ == "uses":
        USES[fr].add(to)
        USED_BY[to].add(fr)
    elif typ == "interprets":
        INTERPRETS[fr].add(to)
        INTERPRETED_BY[to].add(fr)


def downstream_cone(seed: str, *, include_interprets: bool = True) -> set[str]:
    """Set of labels that transitively depend on `seed` via uses[]
    (and optionally interprets)."""
    visited = set()
    q = deque([seed])
    while q:
        cur = q.popleft()
        for parent in USED_BY.get(cur, ()):
            if parent not in visited:
                visited.add(parent)
                q.append(parent)
        if include_interprets:
            for parent in INTERPRETED_BY.get(cur, ()):
                if parent not in visited:
                    visited.add(parent)
                    q.append(parent)
    return visited


def kind_emoji(kind: str) -> str:
    return {
        "definition":  "📐",
        "theorem":     "🔷",
        "proposition": "🔷",
        "lemma":       "🔷",
        "corollary":   "🔷",
        "conjecture":  "🟡",
        "remark":      "📝",
        "example":     "💡",
        "prose":       "📄",
        "equation":    "🔣",
        "diagram":     "🖼",
        "simulator":   "🎮",
    }.get(kind, "•")


# ── §5 conjectures, in order they appear in the audit ─────────────────
# Each entry: (audit_label, alias_in_content_or_None, short_form,
#              failure_consequence, status_note)
# The audit's §5 references some conjectures by anticipated names that
# either map to a different `kind:` (e.g. `lem:motivic-perpetual-
# obstruction` is currently a `lemma`) or have not yet been authored.
# We document the actual situation rather than producing a 0-cone row.
AUDIT_CONJECTURES = [
    ("conj:mass-endomorphism",
     None,
     "mass tower as single $H_n(q)$ element",
     "The tower formula remains correct as an *infinite series*; the closed form is just a convenience.",
     None),
    ("conj:phi-q-tower-jsj-bridge",
     None,
     "Hecke residue ↔ JSJ bridge",
     "Algebraic-side mass tower remains correct but loses the JSJ-bounded thimble interpretation.",
     None),
    ("conj:shared-denominator-cusp-holonomy",
     None,
     "shared cusp denominator (algebraic ↔ holonomy)",
     "Thimble integration domain identification weakens; algebraic side unaffected.",
     None),
    ("conj:denominator-zeros-as-sw-critical-points",
     None,
     "denominator zeros ↔ SW critical points",
     "τ-image identification for SW critical points loses precision; algebraic side unaffected.",
     None),
    ("conj:motivic-perpetual-obstruction",
     "conj:motivic-perpetual-obstruction",
     "no concrete `instance` at $q_0$",
     "Compute remains, formal-substrate identification weakens.",
     "Block-kind: post-rename 2026-05-02, this is now `conj:motivic-perpetual-obstruction` (was `lem:` — the Lean file's `sorry` was always the conjectural content)."),
    # Forward-looking labels (`conj:hahn-substrate`,
    # `conj:vacuum-epsilon`, `conj:bigbang-heatdeath`,
    # `conj:jones-birthday`, `conj:kashaev-surreal`) were dropped
    # from audit §5 in the 2026-05-02 cleanup pass — none had
    # been authored as content blocks, none had a concrete
    # failure-consequence in the §1 derivation chain. Re-add to
    # this seed list if and when corresponding content lands.
]


def block_filename(label: str) -> str | None:
    b = LABEL_TO_BLOCK.get(label)
    if not b:
        return None
    return f"content/quantum-observable-universe/{b['chapter_dir']}/{b['root_name']}.md"


def md_link(label: str) -> str:
    fn = block_filename(label)
    if fn:
        return f"[`{label}`](../../{fn})"
    return f"`{label}` _(unresolved)_"


def chapter_of(label: str) -> str:
    b = LABEL_TO_BLOCK.get(label)
    return b["chapter_dir"] if b else "<unresolved>"


def kind_of(label: str) -> str:
    b = LABEL_TO_BLOCK.get(label)
    return b["kind"] if b else "?"


def render_mermaid(seed: str, cone: set[str], *, max_nodes: int = 25) -> str:
    """Render a small Mermaid graph showing the seed and the cone above
    it, restricted to a tractable subset (the immediate parents and a
    representative sample of further-downstream nodes)."""
    # Always include direct dependents.
    direct = sorted(USED_BY.get(seed, set()) | INTERPRETED_BY.get(seed, set()))
    rest = sorted(cone - set(direct))
    nodes = direct[:max_nodes] + rest[: max(0, max_nodes - len(direct))]
    nodes = list(dict.fromkeys(nodes))  # de-dupe, keep order
    nodes_in_diagram = set(nodes) | {seed}

    # Build edges among nodes_in_diagram only.
    edges: set[tuple[str, str]] = set()
    for n in nodes_in_diagram:
        for tgt in USES.get(n, ()):
            if tgt in nodes_in_diagram:
                edges.add((n, tgt))
        for tgt in INTERPRETS.get(n, ()):
            if tgt in nodes_in_diagram:
                edges.add((n, tgt))

    # Mermaid id mapping (must be alphanumeric).
    def mid(label: str) -> str:
        return label.replace(":", "_").replace("-", "_")

    lines = ["```mermaid", "graph TD"]
    # Node styles
    for n in nodes_in_diagram:
        k = kind_of(n)
        emoji = kind_emoji(k)
        node_label = f"{emoji} {n}"
        if n == seed:
            lines.append(f'    {mid(n)}["⭐ {n}<br/>(conjecture)"]:::seed')
        elif k == "conjecture":
            lines.append(f'    {mid(n)}["{node_label}"]:::conj')
        elif k in {"theorem", "proposition", "lemma", "corollary"}:
            lines.append(f'    {mid(n)}["{node_label}"]:::prov')
        elif k == "remark":
            lines.append(f'    {mid(n)}["{node_label}"]:::rem')
        elif k == "definition":
            lines.append(f'    {mid(n)}["{node_label}"]:::def')
        else:
            lines.append(f'    {mid(n)}["{node_label}"]')
    for fr, to in sorted(edges):
        lines.append(f"    {mid(fr)} --> {mid(to)}")
    lines += [
        "    classDef seed fill:#fff3a8,stroke:#a06400,stroke-width:2px;",
        "    classDef conj fill:#ffe9b3,stroke:#a06400;",
        "    classDef prov fill:#cfe2f3,stroke:#1a4e8a;",
        "    classDef rem fill:#eaeaea,stroke:#666;",
        "    classDef def fill:#d9ead3,stroke:#274e13;",
        "```",
    ]
    # Note about truncation
    extra = len(cone) - len(nodes)
    if extra > 0:
        lines.append(f"\n_(showing {len(nodes)} of {len(cone)} downstream blocks; "
                     f"see table for full list)_")
    return "\n".join(lines)


def render_kind_breakdown(cone: set[str]) -> str:
    by_kind = defaultdict(int)
    for c in cone:
        by_kind[kind_of(c)] += 1
    parts = [f"**{k}** ×{n}" for k, n in sorted(by_kind.items(), key=lambda x: -x[1])]
    return ", ".join(parts) if parts else "_(empty cone)_"


def render_chapter_breakdown(cone: set[str]) -> dict[str, list[str]]:
    by_chap = defaultdict(list)
    for c in cone:
        by_chap[chapter_of(c)].append(c)
    for k in by_chap:
        by_chap[k].sort()
    return dict(by_chap)


# ── Build the report ──────────────────────────────────────────────────
out: list[str] = []
out.append("# Conjecture cones — §5 of the 2026-05-01 deep audit\n")
out.append(f"**Compiled** 2026-05-01 on `claude/tier-4-math-audit-EkI7a` (workplan task **P4.2**).\n")
out.append("**Pair:** "
           "[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md), "
           "[`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md).\n")
out.append("""
## Purpose

Each open conjecture from §5 of the deep audit gets a **downstream
cone**: the set of blocks that, by following `uses[]` (and
`interprets:` for `remark` blocks), transitively depend on the
conjecture.  The cone tells us *exactly* what becomes conjectural-by-
propagation if the named conjecture is left open — and conversely,
*how much of the paper is unblocked* once it is closed.

The cone respects the conjectural-propagation rule of AGENTS.md §3b:
any provable block (`theorem` / `proposition` / `lemma` /
`corollary`) appearing in the cone of an open `conj:` block is a
**propagation violation** and must be either demoted to `conjecture`
or refactored to remove the dependency.

## How to read the diagrams

- ⭐ **seed** — the conjecture under audit
- 🟡 **conjecture** — another conjecture downstream of the seed
- 🔷 **provable** (theorem / proposition / lemma / corollary) — a
  propagation violation, **must be demoted or refactored**
- 📐 **definition** — a definition that names something contingent on
  the seed (per §3b clarification, not itself a violation, but its
  downstream provable cone is)
- 📝 **remark** — a remark interpreting the seed (allowed)
- 💡 **example** — a concrete instance of the seed

Nodes are kept tractable: the diagram shows direct dependents plus a
representative sample of the cone (≤ 25 nodes per cone).  The full
cone counts are in the per-conjecture tables below the diagrams.

---

""")

# Summary table at top
out.append("## Summary table\n")
out.append("| Conjecture | Cone size | Propagation violations | Failure consequence |\n")
out.append("|------------|----------:|-----------------------:|---------------------|\n")

cones: dict[str, set[str]] = {}
violations: dict[str, list[str]] = {}
resolved_label: dict[str, str | None] = {}

for label, alias, _short, _conseq, _note in AUDIT_CONJECTURES:
    seed = label if label in LABEL_TO_BLOCK else (alias if alias and alias in LABEL_TO_BLOCK else None)
    resolved_label[label] = seed
    if seed is None:
        cones[label] = set()
        violations[label] = []
        continue
    cone = downstream_cone(seed)
    cones[label] = cone
    # Note: a lemma seed (like the motivic-perpetual case) is itself
    # provable in form, but its `sorry` is conjectural. Exclude the seed
    # from violation count.
    viol = sorted(c for c in cone if c != seed and kind_of(c) in {"theorem", "proposition", "lemma", "corollary"})
    violations[label] = viol

for label, alias, _short, conseq, _note in AUDIT_CONJECTURES:
    seed = resolved_label[label]
    if seed is None:
        out.append(f"| `{label}` | _(not authored)_ | — | {conseq} |\n")
    else:
        link_label = seed if seed != label else label
        out.append(f"| {md_link(seed)}{' (as `' + label + '`)' if seed != label else ''} | "
                   f"{len(cones[label])} | "
                   f"{len(violations[label])} | {conseq} |\n")

out.append("\n---\n\n")

# Per-conjecture sections
for label, alias, short, conseq, status_note in AUDIT_CONJECTURES:
    cone = cones[label]
    viol = violations[label]
    seed = resolved_label[label]
    out.append(f"## {label}\n")
    if status_note:
        out.append(f"\n{status_note}\n\n")
    if seed is None:
        out.append(f"**Status:** label not present in content. **Cone size: 0.**\n\n")
        out.append(f"**Short form:** {short}  \n**Failure consequence:** {conseq}\n\n")
        out.append(f"_If/when this conjecture is authored, re-run the cone "
                   f"build script to populate this section._\n\n---\n\n")
        continue
    out.append(f"**Source:** {md_link(seed)}")
    if seed != label:
        out.append(f" (resolved from audit label `{label}`)")
    out.append("  ")
    out.append(f"**Chapter:** `{chapter_of(seed)}`  ")
    out.append(f"**Short form:** {short}  ")
    out.append(f"**Failure consequence:** {conseq}\n\n")
    out.append(f"**Cone size:** {len(cone)} downstream blocks "
               f"({render_kind_breakdown(cone)}).\n\n")

    if viol:
        out.append(f"**🔴 Propagation violations ({len(viol)})** — these provable blocks "
                   f"must be demoted to `conjecture` or refactored to drop the dependency:\n\n")
        for v in viol[:30]:
            out.append(f"- {kind_emoji(kind_of(v))} {md_link(v)} _(`{kind_of(v)}` in `{chapter_of(v)}`)_\n")
        if len(viol) > 30:
            out.append(f"- … and {len(viol) - 30} more\n")
        out.append("\n")
    else:
        out.append("**🟢 No propagation violations** — every downstream block is already "
                   "`conjecture` or `remark`/`example`/`definition`. Cone is propagation-clean.\n\n")

    # Diagram
    if cone:
        out.append("### Downstream cone diagram\n\n")
        out.append(render_mermaid(seed, cone))
        out.append("\n\n")

    # Per-chapter breakdown
    by_chap = render_chapter_breakdown(cone)
    if by_chap:
        out.append("### By chapter\n\n")
        for chap, members in sorted(by_chap.items()):
            out.append(f"**`{chap}`** — {len(members)} block{'s' if len(members) != 1 else ''}: ")
            out.append(", ".join(md_link(m) for m in members[:8]))
            if len(members) > 8:
                out.append(f", … (+{len(members) - 8})")
            out.append("\n\n")

    out.append("---\n\n")


# Aggregate footer
total_cone = set().union(*cones.values())
total_viol = set().union(*[set(v) for v in violations.values()])

out.append("## Aggregate summary\n\n")
out.append(f"- **Total blocks under at least one open audit conjecture:** {len(total_cone)}\n")
out.append(f"- **Total propagation violations across all {len(AUDIT_CONJECTURES)} cones:** {len(total_viol)}\n")
out.append(f"- **Conjectures with zero violations** (already propagation-clean): "
           f"{sum(1 for v in violations.values() if not v)} / {len(AUDIT_CONJECTURES)}\n")
out.append(f"- **Conjectures with > 0 violations** (need P3.1 sweep action): "
           f"{sum(1 for v in violations.values() if v)} / {len(AUDIT_CONJECTURES)}\n\n")
out.append("See workplan task **P3.1** (Conjectural-propagation sweep) for the action.\n\n")

# ── Methodology footnote: remark propagation ──────────────────────
out.append("""## Methodology — does propagation pass through remarks?

AGENTS.md §3b clarifies that the conjectural-propagation rule
(downstream of a `conj:` ⇒ kind must be `conjecture`) applies to
**provable kinds only** (`theorem`, `proposition`, `lemma`,
`corollary`).  Remarks make no logical claim and so are exempt.

However, this script computes the **transitive closure** of the
`uses[]` graph — including paths that pass through `remark` blocks.
This means that if

```
prop:A  →uses→  rem:B  →uses→  conj:C
```

then `prop:A` appears in the cone of `conj:C` even though the
intermediary `rem:B` is exempt.  The structural finding is real
(propagation flows), but whether the violation must be acted on
depends on the editor's reading of the chain:

1. If the prose of `rem:B` *itself* asserts a claim that depends on
   `conj:C`, then `prop:A`'s reliance on `rem:B` is a real
   propagation violation: `prop:A` must be demoted, or `rem:B`
   refactored to drop the conjecture from `uses[]` (switching to
   `interprets:` instead).
2. If `rem:B` is purely interpretive (a "see also" pointer) and the
   proof of `prop:A` does not depend on `conj:C`, then the violation
   is spurious; the cleanup is to **change `rem:B`'s
   `conj:C`-citation from `uses[]` to `interprets:`**.  Once that
   edge moves, `prop:A` no longer transitively `uses[]` `conj:C`.

The P3.1 sweep should resolve every cone-via-remark by case (1) or
case (2).  In particular, audit `rem:calibration-inputs` (cited by
≥ 2 propositions and itself listing `conj:mass-endomorphism` in
`uses[]`) — most likely a case (2) cleanup.

""")

# Note on automation
out.append("""## Reproducibility

This report is generated mechanically from the `uses[]` /
`interprets:` graph.  To rebuild after content changes:

```bash
cd content && python3 pipeline/content-graph-analysis.py --json > /tmp/qou-graph.json
python3 docs/audits/scripts/build-conjecture-cones.py > docs/audits/conjecture-cones.md
```

The seed list is the §5 table of
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md).
If new audit conjectures are added (or existing ones closed), update
`AUDIT_CONJECTURES` in the build script.
""")

print("".join(out))
