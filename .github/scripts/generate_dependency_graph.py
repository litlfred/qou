"""
Generate Dependency Graph SVG from proof-objects.json

Produces a Graphviz DOT file and renders it to SVG showing the logical
dependency structure of all proof objects.  Nodes are organized into
subgraphs by chapter (vertical, top to bottom) with horizontal ordering
by theorem number within each chapter row.

Node colors:
  - Red:    No proof / blocking (formalization_status in {not_started, has_sorry})
  - Orange: Reviewed by LLM only (has agentic reviews, no human review)
  - Green:  Reviewed by human (has at least one human review)
  - Yellow: Stated in Lean but no reviews yet

Edges: thick lines connecting dependencies.

Each node links to the corresponding section in the published PDF
(using PDF named destinations / anchor tags).

Usage:
    python .github/scripts/generate_dependency_graph.py \\
        [--manifest proof-objects.json] \\
        [--output dependency-graph.svg] \\
        [--pdf-base-url https://litlfred.github.io/qou/quantum-observable-universe.pdf]
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_MANIFEST = REPO_ROOT / "proof-objects.json"
DEFAULT_OUTPUT = REPO_ROOT / "dependency-graph.svg"
DEFAULT_PDF_URL = "https://litlfred.github.io/qou/quantum-observable-universe.pdf"

# Chapter titles for subgraph labels
CHAPTER_TITLES = {
    1: "Ch.1 Quantum Observable Universe",
    2: "Ch.2 Categorical & Analytic Foundations",
    3: "Ch.3 Path Integrals and Braiding",
    4: "Ch.4 Lifting of Quantum Torsion",
    5: "Ch.5 Bring's Surface",
    6: "Ch.6 The Descartes Universe",
    7: "Ch.7 p-Adic Quantum Groups",
    8: "Ch.8 Gauge Field Fluid Dynamics",
    9: "Ch.9 Information Theory",
    10: "Ch.10 Interpretations",
    11: "Ch.11 Experimental Evidence",
    12: "Ch.12 Speculations",
}

# Short prefixes for display
TYPE_PREFIX = {
    "definition": "Def",
    "theorem": "Thm",
    "lemma": "Lem",
    "proposition": "Prop",
    "corollary": "Cor",
    "conjecture": "Conj",
    "example": "Ex",
    "remark": "Rem",
}


def node_color(obj):
    """Determine node fill color based on formalization and review status.

    - Red:    no proof / blocking (not_started or has_sorry)
    - Yellow: stated in Lean but no reviews
    - Orange: reviewed by LLM only
    - Green:  reviewed by human
    """
    reviews = obj.get("reviews", [])
    has_human = any(r.get("reviewer_type") == "human" for r in reviews)
    has_agentic = any(r.get("reviewer_type") == "agentic" for r in reviews)
    status = obj.get("formalization_status", "not_started")

    if has_human:
        return "#90EE90"  # light green
    if has_agentic:
        return "#FFD700"  # gold/orange
    if status in ("proved", "mathlib_ok"):
        return "#FFFACD"  # light yellow — proved but no review
    # not_started, stated, has_sorry
    return "#FF6B6B"  # light red


def node_border_color(obj):
    """Border color based on formalization status."""
    status = obj.get("formalization_status", "not_started")
    if status == "mathlib_ok":
        return "#006400"  # dark green
    if status == "proved":
        return "#228B22"  # forest green
    if status == "has_sorry":
        return "#FF8C00"  # dark orange
    if status == "stated":
        return "#DAA520"  # goldenrod
    return "#DC143C"  # crimson


def sanitize_id(label):
    """Convert a LaTeX label to a valid Graphviz node ID."""
    return re.sub(r"[^a-zA-Z0-9_]", "_", label)


def node_display_label(obj):
    """Short display label for the node."""
    label = obj["label"]
    obj_type = obj.get("object_type", "")
    prefix = TYPE_PREFIX.get(obj_type, obj_type.capitalize())
    # Extract the number part if available
    number = obj.get("latex", {}).get("number", "")
    if number:
        return f"{prefix} {number}"
    # Fallback: use the label suffix
    suffix = label.split(":", 1)[-1] if ":" in label else label
    # Truncate long names
    if len(suffix) > 20:
        suffix = suffix[:17] + "..."
    return f"{prefix}\\n{suffix}"


def pdf_anchor_url(obj, pdf_base_url):
    """Generate a URL linking to the object in the PDF.

    PDF viewers support named destinations.  LaTeX hyperref creates
    destinations from \\label{} commands.  The destination name is the
    label text itself.
    """
    label = obj["label"]
    return f"{pdf_base_url}#%s" % label


def generate_dot(manifest, pdf_base_url):
    """Generate a Graphviz DOT string from the manifest."""
    objects = manifest.get("objects", [])
    dependencies = manifest.get("dependencies", [])

    # Group objects by chapter
    by_chapter = {}
    for obj in objects:
        chapter = obj.get("latex", {}).get("chapter", 0)
        by_chapter.setdefault(chapter, []).append(obj)

    # Build label→object lookup
    obj_by_label = {obj["label"]: obj for obj in objects}

    lines = []
    lines.append("digraph ProofDependencies {")
    lines.append("  rankdir=TB;")
    lines.append("  newrank=true;")
    lines.append('  graph [fontname="Helvetica", fontsize=11, bgcolor="white",')
    lines.append("         pad=0.5, nodesep=0.4, ranksep=0.8];")
    lines.append('  node [fontname="Helvetica", fontsize=9, style="filled,rounded",')
    lines.append("        shape=box, penwidth=2.0, margin=\"0.1,0.05\"];")
    lines.append('  edge [penwidth=2.5, arrowsize=0.8];')
    lines.append("")

    # Legend
    lines.append("  subgraph cluster_legend {")
    lines.append('    label="Legend";')
    lines.append('    style=dashed; color="#888888"; fontsize=10;')
    lines.append('    legend_red   [label="No proof / Blocking" fillcolor="#FF6B6B" color="#DC143C"];')
    lines.append('    legend_orange [label="LLM Reviewed" fillcolor="#FFD700" color="#DAA520"];')
    lines.append('    legend_green [label="Human Reviewed" fillcolor="#90EE90" color="#228B22"];')
    lines.append('    legend_yellow [label="Proved (no review)" fillcolor="#FFFACD" color="#DAA520"];')
    lines.append("    legend_red -> legend_orange -> legend_green -> legend_yellow [style=invis];")
    lines.append("  }")
    lines.append("")

    # Chapter subgraphs
    for chapter_num in sorted(by_chapter.keys()):
        if chapter_num == 0:
            continue
        chapter_objects = by_chapter[chapter_num]
        # Sort by line number for horizontal ordering
        chapter_objects.sort(key=lambda o: o.get("latex", {}).get("line", 0))

        title = CHAPTER_TITLES.get(chapter_num, f"Ch.{chapter_num}")
        lines.append(f"  subgraph cluster_ch{chapter_num} {{")
        lines.append(f'    label="{title}";')
        lines.append(f'    style=rounded; color="#CCCCCC"; bgcolor="#F8F8F8";')
        lines.append(f"    fontsize=10;")

        # Create rank constraint for horizontal layout within chapter
        node_ids = []
        for obj in chapter_objects:
            nid = sanitize_id(obj["label"])
            node_ids.append(nid)
            fill = node_color(obj)
            border = node_border_color(obj)
            display = node_display_label(obj)
            url = pdf_anchor_url(obj, pdf_base_url)
            tooltip = obj.get("title", obj["label"])

            lines.append(
                f'    {nid} [label="{display}" fillcolor="{fill}" '
                f'color="{border}" URL="{url}" tooltip="{tooltip}" target="_blank"];'
            )

        # Force same rank (horizontal layout) within chapter
        if len(node_ids) > 1:
            lines.append(f"    {{ rank=same; {'; '.join(node_ids)}; }}")

        lines.append("  }")
        lines.append("")

    # Dependency edges
    for dep in dependencies:
        from_label = dep.get("from", "")
        to_label = dep.get("to", "")
        relation = dep.get("relation", "uses")

        if from_label not in obj_by_label or to_label not in obj_by_label:
            continue

        from_id = sanitize_id(from_label)
        to_id = sanitize_id(to_label)

        # Edge color: dark gray for uses, blue for proves
        if relation == "proves":
            edge_color = "#4169E1"  # royal blue
            edge_style = "solid"
        else:
            edge_color = "#555555"  # dark gray
            edge_style = "solid"

        lines.append(
            f'  {to_id} -> {from_id} [color="{edge_color}" style="{edge_style}"];'
        )

    lines.append("}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate dependency graph SVG from proof-objects.json."
    )
    parser.add_argument(
        "--manifest", type=Path, default=DEFAULT_MANIFEST,
        help="Path to proof-objects.json",
    )
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT,
        help="Output SVG file path",
    )
    parser.add_argument(
        "--pdf-base-url", type=str, default=DEFAULT_PDF_URL,
        help="Base URL for the published PDF (for anchor links)",
    )
    parser.add_argument(
        "--dot-only", action="store_true",
        help="Output DOT source instead of rendering SVG",
    )
    args = parser.parse_args()

    if not args.manifest.exists():
        print(f"❌ Manifest not found: {args.manifest}")
        print("Run extract_proof_objects.py first.")
        sys.exit(1)

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)

    dot_source = generate_dot(manifest, args.pdf_base_url)

    if args.dot_only:
        print(dot_source)
        return

    # Write DOT file
    dot_path = args.output.with_suffix(".dot")
    dot_path.write_text(dot_source, encoding="utf-8")

    # Render with Graphviz
    try:
        subprocess.run(
            ["dot", "-Tsvg", "-o", str(args.output), str(dot_path)],
            check=True,
            capture_output=True,
            text=True,
        )
        print(f"✅ Generated {args.output}")
    except FileNotFoundError:
        print("⚠️  Graphviz 'dot' not found — DOT file written but SVG not rendered.")
        print(f"   Install Graphviz and run: dot -Tsvg -o {args.output} {dot_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Graphviz error: {e.stderr}")
        sys.exit(1)


if __name__ == "__main__":
    main()
