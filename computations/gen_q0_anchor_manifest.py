#!/usr/bin/env python3
"""gen_q0_anchor_manifest.py — classify producers by CAL-layer q₀ anchor.

Scans every committed `computations/*.witness.json` (git HEAD), reads its q₀
signature, and maps it to the producing script's stem — emitting
`q0_anchor_manifest.json`, the single auditable registry of which producers are
IDEAL/canonical (muon) vs PHYSICAL-Observations (proton).  `q_parameter` reads
this manifest to auto-select the anchor for the running producer (bean `yfvb`).

Ground truth = the committed witness's own q₀:
  muon  1.109978595557…  → ideal   (CAL-2 = P_skew^β, m_μ/m_e)
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

# Explicit suffix allow-list for suffixed producer filenames (bean qou-5t8y).
# Many producers drop their role suffix (`_probe`, `_derivation`, `_test`, ...)
# when naming their witness (`fbor-normalisation-barsymmetry.witness.json` from
# `fbor_normalisation_barsymmetry_probe.py`). An open prefix match is ambiguous
# (`foo` would match `foo_bar_probe.py`), whereas requiring an exact stem plus
# one of these role suffixes -- and requiring a unique match per directory --
# resolves the 1,199 suffixed producers to their actual script stem
# (`Path(sys.argv[0]).stem`, which `q_parameter` keys on).
PRODUCER_SUFFIXES = (
    "_probe",
    "_derivation",
    "_test",
    "_verify",
    "_audit",
    "_check",
    "_scan",
    "_sweep",
)


def _committed_tree() -> tuple[list[str], set[str]]:
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "computations/"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.splitlines()
    wits = [l for l in out if l.endswith(".witness.json")]
    pys = {l for l in out if l.endswith(".py")}
    return wits, pys


def _committed_witnesses() -> list[str]:
    return _committed_tree()[0]


def _producer_stem(
    witness_rel: str,
    committed_pys: set[str] | None = None,
) -> str | None:
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

    Suffixed producer fallback (bean `qou-5t8y`): when no exact `<stem>.py`
    exists, check `<stem><suffix>.py` for `suffix` in `PRODUCER_SUFFIXES` and
    accept only when a single suffix matches in that directory, returning the
    full producer stem (`<stem><suffix>`) that `q_parameter` matches against
    `Path(sys.argv[0]).stem`.
    """
    if committed_pys is None:
        _, committed_pys = _committed_tree()
    stem = Path(witness_rel).name[: -len(".witness.json")]
    wdir = (ROOT / witness_rel).parent

    def _py_exists(base: Path, cand: str) -> bool:
        if (base / f"{cand}.py").exists():
            return True
        try:
            rel = (base / f"{cand}.py").relative_to(ROOT).as_posix()
        except ValueError:
            return False
        return rel in committed_pys

    for base in (wdir, HERE):
        for cand in (stem.replace("-", "_"), stem):
            if _py_exists(base, cand):
                return cand
    u_stem = stem.replace("-", "_")
    for base in (wdir, HERE):
        matches = [
            f"{u_stem}{sfx}"
            for sfx in PRODUCER_SUFFIXES
            if _py_exists(base, f"{u_stem}{sfx}")
        ]
        if len(matches) == 1:
            return matches[0]
    return None


def main() -> int:
    ideal, physical, ambiguous = {}, {}, {}
    wits, committed_pys = _committed_tree()
    for w in wits:
        prod = _producer_stem(w, committed_pys)
        if prod is None:
            continue
        txt = subprocess.run(["git", "show", f"HEAD:{w}"], cwd=ROOT,
                             capture_output=True, text=True).stdout
        has_m, has_p = (MUON in txt), (PROTON in txt)
        if has_m and not has_p:
            if prod in physical:
                ambiguous[prod] = w
                del physical[prod]
            elif prod not in ambiguous:
                ideal[prod] = w
        elif has_p and not has_m:
            if prod in ideal:
                ambiguous[prod] = w
                del ideal[prod]
            elif prod not in ambiguous:
                physical[prod] = w
        elif has_m and has_p:
            ideal.pop(prod, None)
            physical.pop(prod, None)
            ambiguous[prod] = w  # both signatures — manual ruling
        # neither: no q₀ field — omit (anchor-insensitive or non-derivation)

    manifest = {
        "_schema": "q0-anchor-manifest/v1",
        "_convention": "ideal=muon (CAL-2 P_skew^β); physical=proton (m_p/m_e). "
                       "q_parameter auto-selects by the running producer's stem; "
                       "QOU_Q0_ANCHOR env var overrides.",
        "ideal_muon": sorted(ideal),
        "physical_proton": sorted(physical),
        "ambiguous": sorted(ambiguous),
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    import sys as _sys  # noqa: E402
    _sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
    from qou_substrate.witness import WitnessBuilder as _WB
    manifest.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        manifest, script_path=__file__, engine=None, q0_anchor=None)
    (HERE / "q0_anchor_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"ideal/muon:      {len(ideal)}")
    print(f"physical/proton: {len(physical)}")
    print(f"ambiguous:       {len(ambiguous)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
