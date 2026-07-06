#!/usr/bin/env python3
"""Per-Z shard producer for the recursive atom-knot atlas.

Extends `canonical_mass_table_extended.py` with full AME 2020
coverage. For every (Z, N) in AME 2020 (3558 nuclides), emits a
per-element shard `canonical-isotope-witness-Z<NN>.witness.json`
containing AME reference values + layered framework predictions
(where any layer has coverage).

Layers (per `docs/coordination/show-mass-sweep-table.md`):

  L1 — canonical |tr_M(β_atom, q_0)| via `markov_peel + mpmath`.
       Reachable for A ≤ 6 today (n_strands ≤ 18); ⁶Li ≈ 17 min
       wall, anything heavier requires the Rust path. We **reuse**
       existing canonical-mass-table-extended values rather than
       recompute.
  L2 — α-cluster recursion `B(nα) = n·B(⁴He) + C(n,2)·c_αα` via
       `alpha_cluster_recursion.py`. Covers Z = N, A = 4n: ⁴He,
       ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca.
  L3 — paper-six-term sweep (off by default; future extension).
  L4 — composite mass M(A, Z) = N·m_n + Z·m_p − B(A, Z) using
       Borromean nucleon masses + any-layer B.
  L5 — Q-values Q_β(A, Z) = M(A, Z) − M(A, Z+1) − m_e from
       adjacent-row L4 (future extension).

This script is intentionally a **read-many, compute-little**
orchestrator. The L1 / L2 predictions live in their producer
witnesses; canonical_isotope_witness assembles them by Z and adds
AME reference values + L4 composite + provenance.

CLI:
    python3 canonical_isotope_witness.py             # Z=0..20 default
    python3 canonical_isotope_witness.py --max-z 30  # Z=0..30
    python3 canonical_isotope_witness.py --z 1,2     # just H + He shards

Per repo-owner directive 2026-05-19: "expand to make sure all
isotopes. keep recursive knot atlas an integral part of mass /
beta / Q / binding pipeline." Plus user decisions (per
`/coordinate` AskUserQuestion 2026-05-19): AME 2020 data source,
per-Z shards, atlas per-Z sections.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import U_MEV  # noqa: E402 — u→MeV factor (bean 46ke)


# ── Data loaders ──────────────────────────────────────────────────

def load_ame2020() -> dict:
    """Load the parsed AME 2020 reference data (data/ame2020.json)."""
    path = HERE / "data" / "ame2020.json"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found — run vendor_ame2020.py first."
        )
    return json.loads(path.read_text())


def load_layer1() -> dict:
    """Load the L1 canonical |tr_M| witness for p..⁶Li reuse."""
    path = _pb.witness_path("canonical-mass-table-extended.witness.json", HERE)
    return json.loads(path.read_text()) if path.exists() else {}


def load_layer2() -> dict:
    """Load the L2 α-cluster recursion witness."""
    path = _pb.witness_path("alpha-cluster-recursion.witness.json", HERE)
    return json.loads(path.read_text()) if path.exists() else {}


def load_layer3() -> dict:
    """Load the L3 low-isotope binding sweep (partial-shell)."""
    path = _pb.witness_path("low-isotope-binding-sweep.witness.json", HERE)
    return json.loads(path.read_text()) if path.exists() else {}


def load_borromean() -> dict:
    """Load m_p, m_n, m_μ from the Borromean tower witness."""
    path = _pb.witness_path("m-p-borromean-verification-50dps.witness.json", HERE)
    return json.loads(path.read_text()) if path.exists() else {}


# ── Borromean nucleon-mass extraction ─────────────────────────────

def borromean_m_p_m_n(borromean: dict) -> tuple[float | None, float | None]:
    """Return (m_p_pred_MeV, m_n_pred_MeV) from the Borromean witness."""
    data = borromean.get("data", borromean)
    try:
        m_p = float(data.get("proton", {}).get("m_p_pred_MeV"))
    except (TypeError, ValueError):
        m_p = None
    try:
        m_n = float(data.get("neutron", {}).get("m_n_pred_MeV"))
    except (TypeError, ValueError):
        m_n = None
    return m_p, m_n


# ── L1 / L2 lookups ───────────────────────────────────────────────

def l1_lookup(Z: int, N: int, layer1: dict) -> dict | None:
    """Return the L1 row for (Z, N) if present in canonical-extended."""
    rows = layer1.get("data", {}).get("rows", [])
    for r in rows:
        if int(r.get("Z", -1)) == Z and int(r.get("N", -1)) == N:
            return r
    return None


def l2_lookup(Z: int, N: int, layer2: dict) -> dict | None:
    """Return the L2 (α-cluster) row for (Z, N) if present.

    The alpha-cluster witness is hand-written (predates the
    WitnessBuilder convention) and stores rows at the top level,
    not under `data`. Probe both shapes.
    """
    rows = (
        layer2.get("data", {}).get("rows")
        or layer2.get("rows")
        or []
    )
    for r in rows:
        if int(r.get("Z", -1)) == Z and int(r.get("N", -1)) == N:
            return r
    return None


def l3_lookup(Z: int, N: int, layer3: dict) -> dict | None:
    """Return the L3 partial-shell / census row for (Z, N).

    L3 covers odd-A and non-magic light isotopes (⁷Li, ⁹Be, ¹¹B,
    ¹⁴N, ¹⁹F, etc.) via partial-shell interpolation between
    α-cluster anchor points. Accuracy is 5–36 % (worst at half-
    filled shells); use as a fallback after L1 / L2.
    """
    rows = (
        layer3.get("data", {}).get("rows")
        or layer3.get("rows")
        or []
    )
    for r in rows:
        if int(r.get("Z", -1)) == Z and int(r.get("N", -1)) == N:
            return r
    return None


# ── Row assembly ──────────────────────────────────────────────────

def assemble_row(
    ame_entry: dict, layer1: dict, layer2: dict, layer3: dict,
    m_p_borr: float | None, m_n_borr: float | None,
) -> dict:
    """Compose a per-nuclide row from AME reference + L1/L2 layers."""
    Z = ame_entry["Z"]
    N = ame_entry["N"]
    A = ame_entry["A"]
    element = ame_entry["element"]

    # Reference values from AME 2020 (B in MeV, m_excess in MeV;
    # the AME file stores keV → convert).
    b_ame_keV = ame_entry.get("binding_energy_total_keV")
    b_ame_mev = b_ame_keV / 1000.0 if b_ame_keV is not None else None
    me_keV = ame_entry.get("mass_excess_keV")
    me_mev = me_keV / 1000.0 if me_keV is not None else None
    qbeta_keV = ame_entry.get("beta_decay_energy_keV")
    qbeta_mev = qbeta_keV / 1000.0 if qbeta_keV is not None else None
    atomic_mass_u = ame_entry.get("atomic_mass_micro_u")
    if atomic_mass_u is not None:
        atomic_mass_u = atomic_mass_u / 1e6  # micro-u → u

    # Free nucleons (Z+N=1): mass prediction track.
    is_nucleon = (Z, N) in [(1, 0), (0, 1)]
    if is_nucleon:
        l1 = l1_lookup(Z, N, layer1)
        m_pred = (
            float(l1.get("prediction_MeV_50dps"))
            if (l1 and l1.get("prediction_MeV_50dps")) else None
        )
        m_ref = (
            float(l1.get("B_AME_MeV"))
            if (l1 and l1.get("B_AME_MeV") is not None) else None
        )
        m_err = m_pred - m_ref if (m_pred is not None and m_ref is not None) else None
        m_err_ppm = (m_err / m_ref * 1e6) if (m_err is not None and m_ref) else None
        return {
            "Z": Z, "N": N, "A": A, "element": element,
            "prediction_type": "mass",
            "layer": "L1-borromean-via-canonical",
            # canonical_status taxonomy (added 2026-05-19 per user
            # directive "L4 only use canonical; fix l1 empirical too";
            # updated 2026-05-22 per CAL-4 audit — Borromean tower
            # nucleons are NOT "canonical-substrate": their λ_p / λ_n
            # are fitted from CODATA per
            # `m_p_borromean_verification_50dps.py` CAL-4 banner):
            #   canonical-substrate    — pure substrate derivation
            #                            (NOT yet achieved for any
            #                            nucleon mass; reserved for
            #                            the eventual substrate-pure
            #                            λ_p / λ_n derivation).
            #   borromean-tower-via-fitted-lambda
            #                          — Borromean tower formula
            #                            consumed but λ_scale is
            #                            FITTED FROM CODATA, so the
            #                            ~1 ppb residual is
            #                            tautological.  This is what
            #                            L1-borromean currently is.
            #   canonical-with-empirical-assignment — canonical |tr_M| /
            #                            Vol(K) / m_e BUT the (knot, ρ_K)
            #                            assignment per atom is from the
            #                            framework hypothesis table, not
            #                            from a substrate derivation.
            #                            ρ_K(Z, N) substrate derivation
            #                            is OPEN (ILP / confinement).
            #   canonical-recursive    — derived from a lower canonical
            #                            tier via structural recursion
            #                            (L2 α-cluster: anchored on ⁴He
            #                            + c_αα via Vol(7²₁)).
            #   heuristic              — interpolation between canonical
            #                            anchors (L3 partial-shell);
            #                            NOT derivation, MUST NOT feed
            #                            downstream "canonical" outputs.
            #   pending                — no framework prediction.
            "canonical_status": "borromean-tower-via-fitted-lambda",
            "prediction_MeV_50dps": (
                l1.get("prediction_MeV_50dps") if l1 else None
            ),
            "reference_MeV_50dps": m_ref,
            "err_MeV": m_err,
            "err_ppm": m_err_ppm,
            "ame_reference": {
                "B_AME_keV": b_ame_keV,  # 0 for free nucleons
                "mass_excess_keV": me_keV,
                "atomic_mass_u": atomic_mass_u,
                "Q_beta_keV": qbeta_keV,
            },
        }

    # Composite nuclei: binding-energy prediction (D and up).
    #
    # Selection is CANONICITY-FIRST (user directive 2026-06-02 "excise
    # all non-canonical"): production emits a binding prediction ONLY
    # from a genuinely canonical layer (the α-cluster recursion). We do
    # NOT fall through layer order L1→L2→L3 — that previously let L1's
    # empirical (knot, ρ_K) assignment mask ⁴He's canonical α-cluster
    # result (29.96 MeV empirical shadowing the 28.296 MeV / 0.41 ppb
    # α-cluster value). Any non-canonical value is recorded under
    # `excised` for the audit trail, never shipped as a prediction.
    l1 = l1_lookup(Z, N, layer1)
    l2 = l2_lookup(Z, N, layer2)
    l3 = l3_lookup(Z, N, layer3)

    def _as_float(x):
        try:
            return float(x)
        except (TypeError, ValueError):
            return None

    # Canonical candidates: the α-cluster recursion (canonical-recursive;
    # c_αα = m_e·Vol(7²₁) is canonical). Present in L2 and/or the L3 sweep.
    canonical_candidates: list[tuple[float, str, str]] = []
    if l2 and _as_float(l2.get("B_pred_MeV")) is not None:
        canonical_candidates.append(
            (_as_float(l2["B_pred_MeV"]), "L2-alpha-cluster", "canonical-recursive")
        )
    if (l3 and str(l3.get("strategy", "")).startswith("α-cluster")
            and _as_float(l3.get("B_pred_MeV")) is not None):
        canonical_candidates.append(
            (_as_float(l3["B_pred_MeV"]), f"L3-{l3['strategy']}", "canonical-recursive")
        )

    # Non-canonical candidates (recorded as excised, never shipped):
    #   • L1 (knot, ρ_K) empirical-assignment
    #   • L3 census  B = ρ·Vol(census-knot), ρ hand-assigned
    #   • L3 partial-shell  linear interpolation between α anchors
    noncanonical_candidates: list[tuple[float, str, str]] = []
    if l1 and _as_float(l1.get("prediction_MeV_50dps")) is not None:
        noncanonical_candidates.append(
            (_as_float(l1["prediction_MeV_50dps"]), "L1-canonical",
             "canonical-with-empirical-assignment")
        )
    if (l3 and not str(l3.get("strategy", "")).startswith("α-cluster")
            and _as_float(l3.get("B_pred_MeV")) is not None):
        noncanonical_candidates.append(
            (_as_float(l3["B_pred_MeV"]),
             f"L3-{l3.get('strategy', 'partial-shell')}", "heuristic")
        )

    b_pred: float | None = None
    layer_used: str | None = None
    canonical_status: str = "pending"
    excised: dict | None = None
    if canonical_candidates:
        b_pred, layer_used, canonical_status = canonical_candidates[0]
    else:
        layer_used = "derivation-pending"
        canonical_status = (
            "derivation-pending" if noncanonical_candidates else "pending"
        )
        if noncanonical_candidates:
            ev, el, es = noncanonical_candidates[0]
            excised = {
                "excised_layer": el,
                "excised_status": es,
                "excised_prediction_MeV": ev,
                "reason": "non-canonical (heuristic / empirical-assignment) — "
                          "excised from production per user directive 2026-06-02",
            }

    err_MeV = (b_pred - b_ame_mev) if (b_pred is not None and b_ame_mev is not None) else None
    err_pct = (err_MeV / b_ame_mev * 100.0) if (err_MeV is not None and b_ame_mev) else None
    err_ppm = (err_MeV / b_ame_mev * 1e6) if (err_MeV is not None and b_ame_mev) else None

    # L4 composite mass: M = N·m_n + Z·m_p − B
    # CANONICAL ONLY (per user directive 2026-05-19): emit only when
    # B comes from a canonical-status layer (canonical-substrate,
    # canonical-with-empirical-assignment, canonical-recursive). The
    # heuristic L3 partial-shell and the pending atoms get NO
    # composite mass — those rows surface as L?-derivation-pending in
    # the atlas.
    m_composite_MeV: float | None = None
    composite_canonical_status: str = "pending"
    if (
        m_p_borr is not None
        and m_n_borr is not None
        and b_pred is not None
        and canonical_status in (
            "canonical-substrate",
            "canonical-with-empirical-assignment",
            "canonical-recursive",
        )
    ):
        m_composite_MeV = N * m_n_borr + Z * m_p_borr - b_pred
        composite_canonical_status = canonical_status

    # L4 reference: from AME atomic mass (× u→MeV, registry U_MEV ≈ 931.494).
    m_composite_ref_MeV = (
        atomic_mass_u * float(U_MEV) if atomic_mass_u is not None else None
    )
    m_composite_err_MeV = (
        m_composite_MeV - m_composite_ref_MeV
        if (m_composite_MeV is not None and m_composite_ref_MeV is not None)
        else None
    )
    m_composite_err_ppm = (
        m_composite_err_MeV / m_composite_ref_MeV * 1e6
        if (m_composite_err_MeV is not None and m_composite_ref_MeV)
        else None
    )

    return {
        "Z": Z, "N": N, "A": A, "element": element,
        "prediction_type": "binding_energy",
        "layer": layer_used or "L?-pending",
        "canonical_status": canonical_status,
        "prediction_MeV_50dps": b_pred,
        "reference_MeV_50dps": b_ame_mev,
        "err_MeV": err_MeV,
        "err_pct": err_pct,
        "err_ppm": err_ppm,
        "excised": excised,
        # L4 composite mass — emitted ONLY when B is canonical
        # (canonical_status ∈ {canonical-substrate,
        # canonical-with-empirical-assignment, canonical-recursive}).
        # No AME B fallback. heuristic / pending rows get None here.
        "composite_mass": {
            "M_pred_MeV": m_composite_MeV,
            "M_AME_MeV": m_composite_ref_MeV,
            "err_MeV": m_composite_err_MeV,
            "err_ppm": m_composite_err_ppm,
            "canonical_status": composite_canonical_status,
            "formula": "N·m_n + Z·m_p − B(A,Z)",
            "m_p_source": (
                "borromean-tower (conj:borromean-baryon-mass-formula)"
                if m_p_borr is not None else None
            ),
            "B_source": layer_used,
        },
        "ame_reference": {
            "B_AME_keV": b_ame_keV,
            "mass_excess_keV": me_keV,
            "atomic_mass_u": atomic_mass_u,
            "Q_beta_keV": qbeta_keV,
            "estimated": (
                ame_entry.get("binding_energy_per_A_estimated")
                or ame_entry.get("mass_excess_estimated")
            ),
        },
    }


# ── Shard emitter ────────────────────────────────────────────────

def emit_z_shard(
    Z: int, rows: list[dict],
    builder_upstreams: list[Path],
) -> Path:
    """Emit canonical-isotope-witness-Z<NN>.json for the given Z."""
    n_with_pred = sum(1 for r in rows if r.get("prediction_MeV_50dps") is not None)
    n_with_composite = sum(
        1 for r in rows
        if r.get("composite_mass", {}).get("M_pred_MeV") is not None
    )
    el = rows[0]["element"] if rows else "?"
    builder = (
        WitnessBuilder(
            f"canonical-isotope-witness-Z{Z:02d}",
            engine="python+mpmath",
        )
        .set_description(
            f"Per-Z={Z} shard of the recursive atom-knot atlas. "
            f"Element: {el}. Covers every (Z={Z}, N) in AME 2020. "
            "Each row carries: prediction_type ∈ {mass, "
            "binding_energy}; the prediction value (from L1 "
            "canonical |tr_M| via markov_peel+mpmath, OR L2 "
            "α-cluster recursion); the AME 2020 reference; "
            "err in MeV / % / ppm; L4 composite mass M = N·m_n "
            "+ Z·m_p − B (when nucleon masses + B are available). "
            "L1 source: canonical-mass-table-extended.witness.json; "
            "L2 source: alpha-cluster-recursion.witness.json; "
            "nucleon masses: m-p-borromean-verification-50dps.witness.json."
        )
        .add_parameter("Z", Z)
        .add_parameter("element", el)
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("rows_total", len(rows))
        .add_parameter("rows_with_prediction", n_with_pred)
        .add_parameter("rows_with_composite_mass", n_with_composite)
        .add_data("rows", rows)
    )
    for u in builder_upstreams:
        if u.exists():
            builder.add_upstream(u)
    return builder.save()


def emit_index(
    shards_written: list[tuple[int, Path]],
    ame_data: dict,
) -> Path:
    """Emit canonical-isotope-witness-index.json (cross-shard summary)."""
    by_z = {}
    for Z, path in shards_written:
        try:
            shard = json.loads(path.read_text())
            data = shard.get("data", {})
            by_z[Z] = {
                "shard_filename": path.name,
                "element": shard.get("parameters", {}).get("element"),
                "rows_total": shard.get("parameters", {}).get("rows_total"),
                "rows_with_prediction": shard.get("parameters", {}).get(
                    "rows_with_prediction"
                ),
                "rows_with_composite_mass": shard.get("parameters", {}).get(
                    "rows_with_composite_mass"
                ),
            }
        except (json.JSONDecodeError, OSError):
            pass

    builder = (
        WitnessBuilder(
            "canonical-isotope-witness-index", engine="python"
        )
        .set_description(
            "Cross-shard index for the per-Z canonical-isotope "
            "witness family. Each shard "
            "(canonical-isotope-witness-Z<NN>.witness.json) "
            "covers one element's isotope chain; this index "
            "aggregates the coverage map."
        )
        .add_parameter("n_shards", len(shards_written))
        .add_parameter("z_min", min(z for z, _ in shards_written) if shards_written else None)
        .add_parameter("z_max", max(z for z, _ in shards_written) if shards_written else None)
        .add_parameter("ame_source", ame_data.get("_metadata", {}).get("source"))
        .add_parameter("ame_entries", ame_data.get("_metadata", {}).get("n_entries"))
        .add_data("by_Z", by_z)
    )
    return builder.save()


# ── Main ──────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-z", type=int, default=20,
        help="Maximum Z to emit (default 20). Use 118 for full AME 2020."
    )
    parser.add_argument(
        "--z", default=None,
        help="Comma-separated explicit Z list (overrides --max-z)."
    )
    args = parser.parse_args(argv)

    ame = load_ame2020()
    layer1 = load_layer1()
    layer2 = load_layer2()
    layer3 = load_layer3()
    borromean = load_borromean()
    m_p_borr, m_n_borr = borromean_m_p_m_n(borromean)

    if args.z:
        z_list = [int(s.strip()) for s in args.z.split(",") if s.strip()]
    else:
        z_list = list(range(0, args.max_z + 1))

    # Bucket entries by Z.
    by_z: dict[int, list[dict]] = {z: [] for z in z_list}
    for entry in ame.get("entries", []):
        Z = entry["Z"]
        if Z in by_z:
            by_z[Z].append(entry)

    # Sort each bucket by N (rising isotope chain).
    for Z in by_z:
        by_z[Z].sort(key=lambda e: e["N"])

    print(f"  canonical_isotope_witness — Z = {z_list[0]}..{z_list[-1]}")
    print(f"  Borromean nucleon refs: m_p = {m_p_borr}, m_n = {m_n_borr}")
    print()
    print(f"  {'Z':>3}  {'element':<8}  {'rows':>5}  {'with_pred':>10}  {'with_composite_M':>17}  {'shard':>52}")
    print("  " + "-" * 100)

    shards_written: list[tuple[int, Path]] = []
    upstreams = [
        _pb.witness_path("canonical-mass-table-extended.witness.json", HERE),
        _pb.witness_path("alpha-cluster-recursion.witness.json", HERE),
        _pb.witness_path("low-isotope-binding-sweep.witness.json", HERE),
        _pb.witness_path("m-p-borromean-verification-50dps.witness.json", HERE),
        HERE / "data" / "ame2020.json",
    ]
    for Z, entries in by_z.items():
        if not entries:
            continue
        rows = [
            assemble_row(e, layer1, layer2, layer3, m_p_borr, m_n_borr)
            for e in entries
        ]
        path = emit_z_shard(Z, rows, upstreams)
        shards_written.append((Z, path))
        n_pred = sum(1 for r in rows if r.get("prediction_MeV_50dps") is not None)
        n_comp = sum(
            1 for r in rows
            if r.get("composite_mass", {}).get("M_pred_MeV") is not None
        )
        el = rows[0]["element"]
        print(f"  {Z:>3}  {el:<8}  {len(rows):>5}  {n_pred:>10}  {n_comp:>17}  {path.name:>52}")

    index_path = emit_index(shards_written, ame)
    print()
    print(f"  Index: {index_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
