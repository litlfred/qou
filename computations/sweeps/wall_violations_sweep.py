#!/usr/bin/env python3
"""
P0.1 wall-violation sweep over proof blocks.

For every `*-proof.md` under `content/quantum-observable-universe/`,
flag occurrences of Archimedean / hyperbolic-volume markers that
appear **at the proof level**, not as a τ-image discussion. The
strict-wall rule (AGENTS.md §τ-wall + audit doc §0) requires that
proofs of algebraic-side statements not invoke

  Mostow rigidity, Gromov volume, Thurston norm, hyperbolic Vol(K),
  SnapPy shapes, Kashaev volume, Murakami--Murakami volume conjecture

as derivation inputs. The sweep is conservative: it flags every
match, then a triage column distinguishes:

  - "proof-input" (likely violation): the marker is used as a
    derivation step, e.g. "by Mostow rigidity, ..." or "the
    hyperbolic volume gives ..."
  - "tau-image" (allowed): the marker appears under "τ-image",
    "Archimedean realization", or similar τ-side language.
  - "context-only" (allowed): the marker appears in introductory /
    motivational prose without being used as a proof step.

The triage labels are heuristic; the witness JSON output is the
input to a manual review pass.

Refs:
  docs/audits/2026-05-01-math-framework-deep-audit.md §0, §4
  docs/audits/2026-05-01-math-framework-workplan.md P0.1
"""


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "content" / "quantum-observable-universe"

# Markers to flag. Each marker has a regex pattern matched
# case-insensitively over the proof-block text.
MARKERS = [
    ("Mostow",            r"\bmostow\b"),
    ("Gromov",            r"\bgromov\b"),
    ("Thurston",          r"\bthurston\b"),
    ("Hyperbolic Vol(K)", r"\\?mathrm\{?vol\}?\(.*?\)|hyperbolic.{0,30}volume|\bvol\(k\)"),
    ("SnapPy",            r"\bsnappy\b"),
    ("Kashaev",           r"\bkashaev\b"),
    ("Murakami-Murakami", r"murakami[\s\-_]*murakami|murakami2001"),
    ("Volume conjecture", r"volume.{0,5}conjecture|kashaev[\s\-_]*volume[\s\-_]*conjecture"),
]

# Heuristic triage: language that signals the marker is on the
# τ-side / Archimedean side (allowed) rather than the algebraic
# proof-input side (violation).
TAU_SIDE_LANG = re.compile(
    r"\bτ-image\b|"
    r"\bτ\s*-?\s*pullback\b|"
    r"\barchimedean\s+realization\b|"
    r"\barchimedean\s+side\b|"
    r"\bunder\s+(?:the\s+)?(?:archimedean|fibre)\s+functor\b|"
    r"\bclassical\s+limit\b|"
    r"\bin\s+the\s+complex(?:[\s-]+side)?\b|"
    r"\bin\s+the\s+hyperbolic\s+realization\b|"
    r"\bpost[\s-]archimedean\b|"
    r"\bnaming\b.{0,40}\barchimedean\b",
    re.IGNORECASE,
)

# Proof-input language: marker is being used as a derivation step.
PROOF_INPUT_LANG = re.compile(
    r"\bby\s+(?:mostow|gromov|thurston|kashaev|murakami|the\s+volume\s+conjecture)\b|"
    r"\bapplying\s+(?:mostow|gromov|thurston|kashaev|murakami)\b|"
    r"\bgives\s+(?:the\s+)?(?:hyperbolic\s+)?volume\b|"
    r"\bvol\(.*?\)\s*=|"
    r"=\s*\\?mathrm\{?vol\}?\(",
    re.IGNORECASE,
)


def find_proof_md_files() -> list[Path]:
    return sorted(CONTENT.rglob("*-proof.md"))


def line_context(text: str, span_start: int, span_end: int,
                 ctx_chars: int = 80) -> str:
    lo = max(0, span_start - ctx_chars)
    hi = min(len(text), span_end + ctx_chars)
    snippet = text[lo:hi].replace("\n", " ")
    return ("…" if lo > 0 else "") + snippet + ("…" if hi < len(text) else "")


# Disclaimer headers / phrases that put a match into an explicitly-
# allowed region of the document. If any of these appears in the
# nearest ≤ 4 markdown headers preceding the match (or in the
# wider surrounding 600-char window), the match is reclassified
# from `proof-input` to `tau-image` regardless of localised wording.
DISCLAIMER_HEADER = re.compile(
    r"#+\s+(?:"
    r"post[\s-]archimedean\s+naming|"
    r"archimedean\s+naming|"
    r"τ[\s-]image|"
    r"tau[\s-]image|"
    r"archimedean\s+realization|"
    r"borrowed[,\s]+not\s+part\s+of\s+derivation"
    r")",
    re.IGNORECASE,
)
DISCLAIMER_INLINE = re.compile(
    r"borrowed[,\s]+not\s+part\s+of\s+derivation|"
    r"borrowed[,\s]+conventional[,\s]+and\s+used\s+only\s+as\s+naming|"
    r"used\s+only\s+as\s+naming|"
    r"τ-image\s+naming|"
    r"τ-side\s+naming|"
    r"not\s+a\s+derivation\s+(?:step|input)",
    re.IGNORECASE,
)


def section_context(text: str, span_start: int) -> str:
    """Return the nearest preceding ## / ### markdown header before
    the match position. Empty string if no header found."""
    # Look backwards for the most recent line starting with `#`.
    prefix = text[:span_start]
    # Walk back through lines from the end.
    headers = []
    for line in reversed(prefix.splitlines()[-20:]):  # within last 20 lines
        if line.lstrip().startswith("#"):
            headers.append(line.strip())
    return "\n".join(headers[:4])  # up to 4 nearest headers


def triage(text: str, span_start: int, span_end: int, snippet: str) -> str:
    """Heuristic triage label.

    Refinement (2026-05-02): if the match sits in a section whose
    nearest preceding markdown header matches `DISCLAIMER_HEADER`,
    or if the surrounding 600-char window contains a
    `DISCLAIMER_INLINE` phrase, the match is reclassified as
    `tau-image` (allowed). This reduces the false-positive rate
    for proofs that already explicitly disclaim post-Archimedean
    citations as borrowed naming."""
    has_proof_input = bool(PROOF_INPUT_LANG.search(snippet))
    has_tau_side = bool(TAU_SIDE_LANG.search(snippet))
    section = section_context(text, span_start)
    if DISCLAIMER_HEADER.search(section):
        return "tau-image"
    wider = text[max(0, span_start - 300):min(len(text), span_end + 300)]
    if DISCLAIMER_INLINE.search(wider):
        return "tau-image"
    if has_proof_input and not has_tau_side:
        return "proof-input"
    if has_tau_side:
        return "tau-image"
    return "context-only"


def sweep_file(p: Path) -> dict:
    text = p.read_text(encoding="utf-8")
    matches = []
    for marker, pattern in MARKERS:
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            snippet = line_context(text, m.start(), m.end())
            matches.append({
                "marker": marker,
                "match": text[m.start():m.end()],
                "context": snippet,
                "char_offset": m.start(),
                "triage": triage(text, m.start(), m.end(), snippet),
            })
    if not matches:
        return None
    rel = p.relative_to(REPO).as_posix()
    return {
        "path": rel,
        "match_count": len(matches),
        "triage_summary": {
            label: sum(1 for m in matches if m["triage"] == label)
            for label in ("proof-input", "tau-image", "context-only")
        },
        "matches": matches,
    }


def main() -> int:
    files = find_proof_md_files()
    flagged = []
    for p in files:
        result = sweep_file(p)
        if result is not None:
            flagged.append(result)
    proof_input_total = sum(
        f["triage_summary"]["proof-input"] for f in flagged
    )
    tau_image_total = sum(
        f["triage_summary"]["tau-image"] for f in flagged
    )
    context_only_total = sum(
        f["triage_summary"]["context-only"] for f in flagged
    )
    witness = {
        "computation": "wall-violations-sweep",
        "purpose": (
            "P0.1 deliverable: list every `*-proof.md` block under "
            "content/quantum-observable-universe/ whose text matches "
            "Archimedean / hyperbolic-volume markers (Mostow, Gromov, "
            "Thurston, hyperbolic Vol(K), SnapPy, Kashaev, "
            "Murakami--Murakami, volume conjecture). Each match is "
            "heuristically triaged as proof-input (likely violation), "
            "tau-image (allowed), or context-only (allowed)."
        ),
        "narrative_block": "audit §4·B + workplan P0.1",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "n_proof_files_total": len(files),
        "n_proof_files_flagged": len(flagged),
        "totals": {
            "proof_input": proof_input_total,
            "tau_image": tau_image_total,
            "context_only": context_only_total,
        },
        "flagged_files": flagged,
        "triage_legend": {
            "proof-input": (
                "Marker appears with derivation-step language "
                "('by Mostow rigidity', 'gives Vol(K) = …'). LIKELY a "
                "wall violation; manual review required."
            ),
            "tau-image": (
                "Marker appears under explicit τ-image / Archimedean "
                "realization framing. Allowed."
            ),
            "context-only": (
                "Marker appears in motivational / introductory prose "
                "without being a proof step. Allowed."
            ),
        },
    }
    out = REPO / "folio-assistant" / "computations" / "wall-violations-sweep.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"  Witness written to {out.relative_to(REPO).as_posix()}")
    print(f"  Files swept:        {len(files)}")
    print(f"  Files with hits:    {len(flagged)}")
    print(f"  Total proof-input:  {proof_input_total}")
    print(f"  Total tau-image:    {tau_image_total}")
    print(f"  Total context-only: {context_only_total}")
    if proof_input_total > 0:
        print()
        print("  Files containing 'proof-input' triage hits "
              "(manual review required):")
        for f in flagged:
            n = f["triage_summary"]["proof-input"]
            if n > 0:
                print(f"    {n:>3d} × {f['path']}")
    # Exit cleanly: this is a *sweep*, not a gate. The witness
    # output is the action input for the manual review pass.
    return 0


if __name__ == "__main__":
    sys.exit(main())
