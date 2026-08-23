#!/usr/bin/env python3
"""gen_q0_anchor_manifest.py — classify producers by CAL-layer q₀ anchor.

Scans every committed `computations/*.witness.json` (git HEAD), reads its q₀
signature, and maps it to the producing script's stem — emitting
`q0_anchor_manifest.json`, the single auditable registry of which producers are
IDEAL/canonical (muon) vs PHYSICAL-Observations (proton).  `q_parameter` reads
this manifest to auto-select the anchor for the running producer (bean `yfvb`).

Ground truth = the committed witness's own q₀:
  muon  1.109978595557…  → ideal   (CAL-2 = 𝔇_β, m_μ/m_e)
  proton 1.10997858275…  → physical (m_p/m_e)

A producer stem is the witness stem with '-'→'_' (and the raw stem), restricted
to those with an actual sibling `<stem>.py`.  Producers whose witnesses carry
BOTH or NEITHER signature are listed under `ambiguous` for manual ruling.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MUON = "1.109978595557"
PROTON = "1.10997858275"


def _committed_witnesses() -> list[str]:
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "computations/"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout
    return [l for l in out.splitlines() if l.endswith(".witness.json")]


def _producer_stem(witness_rel: str) -> str | None:
    """The producing script's stem, looked up beside the witness THEN at root.

    The witness-directory lookup is not cosmetic. `computations/` has held
    subdirectories (`probes/`, `qbeta/`, `substrate/`, ...) since long before
    this generator, and a root-only lookup returns None for every one of them —
    so the witness is never even read and the producer cannot appear in the
    manifest under any classification. Measured on `main` at the time this was
    fixed: **700 live witnesses** (plus 153 under `_deprecated/`) had their
    producer in a subdirectory only — 309 in `probes/`, 197 in `qbeta/`, 52 in
    `substrate/` — against 891 resolved at root. Roughly half the corpus.

    The consequence was bounded but one-directional, because `q_parameter`
    resolves an unlisted stem to **proton** (the standing default, owner
    directive 2026-08-07): a subdirectory producer that wanted proton got it by
    accident, while one that wanted muon was silently given proton, and
    `ideal_muon` was simply **unreachable** outside the root directory.
    """
    stem = Path(witness_rel).name[: -len(".witness.json")]
    wdir = (ROOT / witness_rel).parent
    for base in (wdir, HERE):
        for cand in (stem.replace("-", "_"), stem):
            if (base / f"{cand}.py").exists():
                return cand
    return None


def main() -> int:
    ideal, physical, ambiguous = {}, {}, {}
    for w in _committed_witnesses():
        prod = _producer_stem(w)
        if prod is None:
            continue
        txt = subprocess.run(["git", "show", f"HEAD:{w}"], cwd=ROOT,
                             capture_output=True, text=True).stdout
        has_m, has_p = (MUON in txt), (PROTON in txt)
        if has_m and not has_p:
            ideal[prod] = w
        elif has_p and not has_m:
            physical[prod] = w
        elif has_m and has_p:
            ambiguous[prod] = w  # both signatures — manual ruling
        # neither: no q₀ field — omit (anchor-insensitive or non-derivation)

    manifest = {
        "_schema": "q0-anchor-manifest/v1",
        "_convention": "ideal=muon (CAL-2 𝔇_β); physical=proton (m_p/m_e). "
                       "q_parameter auto-selects by the running producer's stem; "
                       "QOU_Q0_ANCHOR env var overrides.",
        "ideal_muon": sorted(ideal),
        "physical_proton": sorted(physical),
        "ambiguous": sorted(ambiguous),
    }
    (HERE / "q0_anchor_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"ideal/muon:      {len(ideal)}")
    print(f"physical/proton: {len(physical)}")
    print(f"ambiguous:       {len(ambiguous)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
