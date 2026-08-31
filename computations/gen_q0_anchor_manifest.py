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
import sys as _sys
from pathlib import Path

# Path bootstrap for `qou_substrate` (bean `qou-0gli`, same class as `qou-ya1e`).
#
# `main()` imports `qou_substrate.witness` for its provenance stamp, and this
# file had no bootstrap for it — so the generator computed the whole manifest
# and then died at the save with `ModuleNotFoundError: qou_substrate`. That is
# almost certainly WHY the manifest drifted 296 entries out of date: it could
# not be regenerated. Searches upward so it works from any cwd.
def _bootstrap_qou_substrate() -> None:
    here = Path(__file__).resolve()
    for parent in here.parents:
        cand = parent / "tools" / "qou-substrate" / "python"
        if cand.is_dir():
            if str(cand) not in _sys.path:
                _sys.path.insert(0, str(cand))
            return


_bootstrap_qou_substrate()

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
# The muon layer has had THREE vintages and this generator saw only the first.
# Matching one of them is not "the muon prefix", it is a snapshot:
#
#   A   1.109978595557...   the original pin, superseded 2026-08-29
#   A'  1.109978595554...   the CODATA-2018 closed form
#   C   1.109978595642...   the CURRENT pin, served by
#                           q-pinning-50-digit.witness.json
#
# A and C diverge at the 10th significant figure, so the old single prefix
# `"1.109978595557"` does not match C. The consequence was not cosmetic: a
# producer correctly migrated to the CURRENT muon pin matched neither MUON nor
# PROTON, fell into the "neither: no q0 field — omit" branch below, dropped out
# of the manifest entirely, and was then defaulted to PROTON at runtime by
# `resolve_q0_anchor`. **Migrating a producer to the current muon pin silently
# re-declared it proton.** The tooling punished conformance.
#
# Found while triaging the qou-0hnz A-literal population (2026-08-30).
MUON_VINTAGES = (
    "1.109978595557",      # A  (superseded)
    "1.109978595554",      # A' (CODATA-2018 closed form)
    "1.109978595642",      # C  (current)
)
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
        has_m = any(v in txt for v in MUON_VINTAGES)
        has_p = PROTON in txt
        if has_m and not has_p:
            ideal[prod] = w
        elif has_p and not has_m:
            physical[prod] = w
        elif has_m and has_p:
            ambiguous[prod] = w  # both signatures — manual ruling
        # neither: no q₀ field — omit (anchor-insensitive or non-derivation)

    # NEVER SILENTLY DROP A NON-DEFAULTING DECLARATION (bean `qou-0gli`).
    #
    # "neither signature -> omit" above is safe ONLY for stems that would
    # resolve to the default anyway. It is not safe in general, because
    # ABSENCE IS NOT NEUTRAL: `resolve_q0_anchor` hands the runtime PROTON
    # default to any stem missing from this manifest. So omitting a stem that
    # was declared `ideal_muon` (or `ambiguous`) silently REDECLARES it as
    # proton — the exact class of mislabelling this manifest exists to prevent.
    #
    # Measured on the first honest regeneration of this file: 98 stems moved
    # `physical_proton -> absent`, which is harmless because the default is
    # already proton, but 4 moved `ideal_muon -> absent`, which is a silent
    # muon->proton flip:
    #     cross_check_trM_cw_seminormal_leg, frakV_askey_wilson_recurrence_tie_probe,
    #     he4_binding_k_stage2_probe, qbeta_physics
    #
    # A witness can lose its q₀ signature for reasons that say nothing about
    # its anchor (a payload reshaped, values serialised differently), so the
    # right response is to CARRY THE PRIOR DECLARATION FORWARD and say so,
    # not to infer "no signature" means "proton".
    _prior_path = HERE / "q0_anchor_manifest.json"
    _carried: list[str] = []
    if _prior_path.exists():
        _prior = json.loads(_prior_path.read_text(encoding="utf-8"))
        _seen = set(ideal) | set(physical) | set(ambiguous)
        for _key, _bucket in (("ideal_muon", ideal), ("ambiguous", ambiguous)):
            for _stem in _prior.get(_key, []):
                if _stem not in _seen:
                    _bucket[_stem] = "(carried: prior declaration, no current signature)"
                    _carried.append(f"{_stem} [{_key}]")

    manifest = {
        "_schema": "q0-anchor-manifest/v1",
        "_convention": "ideal=muon (CAL-2 𝔇_β); physical=proton (m_p/m_e). "
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
    from qou_substrate.witness import WitnessBuilder as _WB
    manifest.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        manifest, script_path=__file__, engine=None, q0_anchor=None)
    (HERE / "q0_anchor_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"ideal/muon:      {len(ideal)}")
    print(f"physical/proton: {len(physical)}")
    print(f"ambiguous:       {len(ambiguous)}")
    if _carried:
        print()
        print(f"  CARRIED FORWARD ({len(_carried)}) — declared before, no q0 signature now.")
        print("  Not dropped: absence would silently redeclare them PROTON.")
        for _c in _carried:
            print(f"    {_c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
