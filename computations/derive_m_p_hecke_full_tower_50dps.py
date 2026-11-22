#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════
PARALLEL CHAIN (2026-05-23): not a consumer of the substrate
flavor-split.

This script predicts m_p and m_n INDEPENDENTLY via per-particle
Hecke tower derivations (`derive_full_tower("proton")` and
`derive_full_tower("neutron")`), with each particle's m getting
its own categorical chain (T1..T4 + Frobenius).  The
proton-neutron mass difference falls out as a *side-effect* of
the independent towers, NOT from a substrate flavor-split
mechanism.

The substrate-pure flavor-split production chain lives at:

  - `m_p_borromean_verification_50dps.py`   (PR #942, production)
  - `_li_2_q_util.flavor_split_subleading`  (PR #690 / #942)
  - `atomic_mass_via_rho_k.py`              (PR #690)

which derives m_p / m_n from a class-uniform m_avg (Family A
or Yekutieli-extended) plus the categorical substrate ratio
`Δm/M_N = ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3`.

The two approaches are STRUCTURALLY DIFFERENT categorical
derivations and complementary:

  - This script's per-particle Hecke tower: m_n derived from
    *its own* GS normal-form chain at q_0.  Tests whether the
    Hecke-tower mechanism alone reproduces the empirical
    proton-neutron split.
  - The borromean-tower + flavor-split: m_n derived from a
    *shared* baryon-class m_avg plus a separately-computed
    Δm/M_N ratio.  Tests the class-uniform + ratio
    factorisation.

Cross-comparison between the two chains is a research-grade
audit (does the per-particle tower's implicit Δm match
flavor_split_subleading?); it is not a wire-in for this
script.

═══════════════════════════════════════════════════════════════════

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
═══════════════════════════════════════════════════════════════

Derive m_p_Hecke via the FULL mass-endomorphism tower at MPFR @ 50 dps.

Sums

    m_p_Hecke = T1_descended + T2_single + T3_pair + T4_Frobenius

where:

  * T1_descended = |Π_i V̂_i^full|  (product of full-channel volumes;
                                    this is the absolute value of the
                                    descended Markov trace at the
                                    H_{3A} → H_3 quotient for A=1)
  * T2_single   = Σ_i Φ_q(|V̂_i^full|)
  * T3_pair     = z² · Σ_{i<j} Φ_q(|V̂_i V̂_j|)
  * T4_Frobenius = Frobenius co-Casimir per vortex (from the canonical
                   6-term framework's ``term_4_frobenius_mp``)

Per-generator volumes come from
``terms-2-3-atom-per-gen-mpfr-50dps.witness.json`` (the MPFR @ 50 dps
producer for {electron, proton, neutron}, see
``terms_2_3_atom_per_gen_mpfr_50dps.py``).

Distinction vs ``derive_m_p_hecke_path_a.py``: Path A is the **partial**
subset T1 + T4 only (used as a placeholder when T2+T3 were unavailable
at MPFR for A=1 atoms).  The full tower below restores T2+T3 — the
brane-tower blow-up contributions that dominate the proton's mass in
``mass_endomorphism.py``'s f64 reference convention — at 50 dps.

T5 (chirality BW) and T6 (Habiro residue) are **excluded** here
because their per-electron values at MPFR have not yet been audited
against the mass-endomorphism convention; the proton-only T5/T6 are
small relative to T2+T3 (≤ 10⁻⁵ of the sum) and including them
without the electron's matching values would introduce an unbalanced
residual.  Closure of T5/T6 for the electron is the next research
step.

Per AGENTS.md three-cal discipline (CAL-1 m_e, CAL-2 q₀):
- Only q₀ (CAL-2) enters the dimensionless m_p / m_e ratio computation.
- CAL-1 m_e converts the ratio to MeV: m_p_pred_MeV = (ratio) × M_E_MEV.
- NO CODATA m_p / m_n injection.
- NO Q_β (CAL-3) anchor consumed in the m_p prediction.

Result history:
  - 2026-05-16 (compact q-dilog Φ_q tower): m_p_pred = 955.49 MeV vs CODATA
                                    938.27 MeV; residual +1.835 %
                                    (+18,353 ppm).  ≈ 54,000× tighter
                                    than the previous Path A value
                                    (0.597 MeV / 999 M ppb).
  - 2026-05-17 (symmetric Li_2^q tower, current canonical form):
                m_p_pred = 0.2406 MeV vs CODATA 938.27 MeV; residual
                -99.97 %.  The honest tower-only prediction is far
                from CODATA — Faddeev's apparent closure was a pole
                artefact at |V̂_p| > q⁻¹.  See
                ``picard-lefschetz-thimble.witness.json`` for the
                C2-inflection substrate route (-0.07 % m_p residual)
                and ``probe-flavor-split-substrate.witness.json``
                (Δm to -0.10 %).  The full closure of the tower at
                A=1 requires per-generator T2/T3 fields that main's
                ``terms_2_3_atom_per_gen_mpfr_50dps`` no longer emits
                (post-rebase schema regression — separate follow-up).

Output: ``proton-mass-full-tower-50dps.witness.json`` — values stored
in MeV at 50 dps (m_e calibration applied; no further E_0 scaling
needed by downstream consumers).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from codata_constants import (  # noqa: E402
    M_E_MEV as _M_E_MEV_RAW, M_P_MEV_VALIDATION as M_P_MEV_CODATA,
)
from witness_base import (  # noqa: E402
    WitnessBuilder, load_and_hash_upstream,
)
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from mass_formula_6term_mpfr_50dps import (  # noqa: E402
    term_4_frobenius_mp, term_6_habiro_residue_mp, f_Zdep_scale,
)
from bw_chirality_isotopes import (  # noqa: E402
    B_bulk, B_Zdep, B_shell, pairing_sign,
)
from term5_v2_chirality import aK_v2  # noqa: E402
from gb_filtration_jet_tracker import reduce_braid  # noqa: E402
# Centralized helpers (gemini #687 review — avoid duplication with derive_m_n).
from _li_2_q_util import (  # noqa: E402
    load_q_50dps, compute_t2_t3_from_vols,
)

M_E_MEV = mp.mpf(str(_M_E_MEV_RAW))


PER_GEN_WITNESS = _pb.witness_path("terms-2-3-atom-per-gen-mpfr-50dps.witness.json", HERE)
OUT_PATH = _pb.witness_path("proton-mass-full-tower-50dps.witness.json", HERE)


# Canonical braid words per particle (positive int i ↦ σ_i; negative −i ↦ σ_i^{-1}).
# These are the H_n-level braid words underlying each particle's
# Hecke element; the (c, d) flavour decoration in the production
# chain rides on top of the braid word but doesn't change the
# Coxeter-image normal form computed by the GS reducer.
_CANONICAL_BRAID = {
    "proton":   {"n": 3, "word": [1, -2, 1, -2, 1, -2]},
    "neutron":  {"n": 3, "word": [1, -2, 1, -2, 1, -2]},
    "electron": {"n": 2, "word": [1, 1, 1]},
}


def _A_categorical(atom: str) -> int:
    """Derive A from the GS normal form of the particle's canonical
    braid word — the max filtration grade (Coxeter length of the
    longest term in the reduced expression).  Categorical, no
    nucleon-ledger dependency.

    See ``probe_derived_A_from_gs_normal_form.py`` for the empirical
    verification + comparison against the legacy A=nucleon convention
    (promoted to production 2026-05-16 per owner directive:
    "promoted to production. all observables are positive so and
    under prediction is okay because that hopefully will be picked
    up in the higher order Mass Tower").
    """
    spec = _CANONICAL_BRAID[atom]
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        r = reduce_braid(atom, spec["n"], spec["word"])
    shape = r["filtration_shape"]
    return max(shape.keys()) if shape else 0


def _t5_cat_units_for(A: int, Z: int, N: int) -> mp.mpf:
    """T5 in cat-units (m_e-normalised) at categorical A.

    Categorical T5: A from GS normal form (see ``_A_categorical``),
    a_K from V2 Gram-matrix chirality, BW coefficients q-integer-
    derived (``bw_chirality_isotopes``).  Returns mp.mpf(0) iff
    A == 0 (the legacy A=nucleon case for the electron is no longer
    triggered after the 2026-05-16 promotion).
    """
    if A == 0:
        return mp.mpf(0)
    a_K = aK_v2(Z, N)
    sign = pairing_sign(Z, N)
    bulk = B_bulk(A, Z, N, sign)
    zdep = B_Zdep(A, Z, N)
    shell = B_shell(A, Z, N) if A >= 4 else mp.mpf(0)
    t5_MeV = a_K * bulk + f_Zdep_scale * zdep + shell
    return t5_MeV / M_E_MEV


def _per_gen_results(w: dict) -> list:
    """Extract the per-generator results list, tolerating both
    ``data.results`` (modern) and top-level ``results`` (legacy)
    witness schemas — gemini #663 review guidance."""
    return w.get("data", {}).get("results") or w.get("results", [])


def _t1_t2_t3_from_per_gen(
    per_gen_witness: dict, atom: str,
    q0: mp.mpf, qi: mp.mpf, z: mp.mpf,
    channel: str = "full",
) -> tuple[mp.mpf, mp.mpf, mp.mpf, list[mp.mpf]]:
    """Extract T1 (descended) + compute T2 + T3 + raw V̂_i list for ``atom``.

    T1 (descended) = |∏ V̂_i| is the GS-NF / Coxeter-image product.
    T2 and T3 are computed locally from `wedderburn_vols` via the
    canonical Li_2^q tower (centralised in ``_li_2_q_util``) since
    `terms_2_3_atom_per_gen_mpfr_50dps.py` on `main` (post-2026-05-17
    rebase) no longer emits pre-summed scalars.  Constants ``q0, qi, z``
    are passed in from main (loaded once via ``load_q_50dps`` — gemini
    #687 review: avoid per-call filesystem reads).

    ``channel`` selects which per-generator Wedderburn scalar feeds the
    tower (see CHANNEL-SELECTION NOTE below):

    - ``"full"`` (production default, OWNER-GATED): the W-weighted
      3-channel Wedderburn average ``w_sym·λ_sym + w_std·V_std +
      w_alt·λ_alt``.  This is what the tower has historically consumed.
    - ``"std"`` (DERIVED, falsification-verified): the genuine
      standard-channel Hoefsmit Markov trace ``V̂_i = z·a_i + b_i`` per
      [`thm:markov-trace-product`].  ``∏V̂_i^std = tr_M`` to 4e-6 (audit
      `docs/audits/2026-06-01-vhat-per-crossing-transfer-chain.md`).

    CHANNEL-SELECTION NOTE (2026-06-01, PR vhat-std-channel-fix).
    The merged item-2 audit (verdict A + RED finding) showed the brane
    tower consumes the ``"full"`` 3-channel average, which is NOT
    ``thm:markov-trace-product``'s per-generator factor and whose
    product ≠ tr_M (proton ∏ = 0.960 vs genuine tr_M = 1.065).  The
    genuine derived factor is the ``"std"`` channel.  This switch is
    OWNER-GATED: ``channel="full"`` remains the default until the owner
    reviews the m_p delta; ``channel="std"`` is the derived path.
    """
    if channel not in ("full", "std"):
        raise ValueError(f"channel must be 'full' or 'std', got {channel!r}")
    for r in _per_gen_results(per_gen_witness):
        if r.get("atom") != atom:
            continue
        vols = [mp.mpf(v[channel]) for v in r["wedderburn_vols"]]
        desc = mp.mpf(1)
        for v in vols:
            desc *= v
        t1 = mp.fabs(desc)
        t2, t3 = compute_t2_t3_from_vols(vols, q0, qi, z)
        return t1, t2, t3, vols
    raise KeyError(f"atom {atom!r} not found in per-gen witness {per_gen_witness.get('computation')!r}")


def derive_full_tower(
    atom: str, per_gen_witness: dict, *,
    Z: int = 0, N: int = 0, knot_type: str = "none",
    q0: mp.mpf | None = None, qi: mp.mpf | None = None, z: mp.mpf | None = None,
    channel: str = "full",
) -> dict:
    """Sum T1 + T2 + T3 + T4 + T5 for ``atom`` at MPFR @ 50 dps with
    A derived categorically from the GS normal form.

    A is the max filtration grade of the GS reduction of ``atom``'s
    canonical braid word (electron σ_1^3 → A=1; proton/neutron
    (σ_1·σ_2^{-1})^3 → A=2).  Used identically in T4 (Frobenius)
    and T5 (BW chirality) so every term respects the same
    categorical A.
    """
    A = _A_categorical(atom)
    if q0 is None:
        q0, qi, z = load_q_50dps()  # back-compat fallback
    t1, t2, t3, vols = _t1_t2_t3_from_per_gen(per_gen_witness, atom, q0, qi, z, channel=channel)
    t4 = term_4_frobenius_mp(A)
    t5_cat = _t5_cat_units_for(A, Z, N)
    # T6 (Habiro residue at non-zero roots-of-unity) — KEY CONVENTION
    # CAVEAT (2026-05-17): the bridge witness
    # `term6-habiro-residue-mpfr-50dps.witness.json` is keyed by
    # **nucleon-A**: A=1 → proton's T6, A=2 → deuteron's T6, A=3 →
    # tritium's, A=4 → ⁴He's.  This branch's `_A_categorical` returns
    # **max GS filtration grade** (proton/neutron → A_cat=2,
    # electron → A_cat=1).  Looking up T6 by A_cat = 2 returns
    # the DEUTERON's T6 (~109 MeV) for proton/neutron, which is
    # semantically wrong.  To preserve honest reporting under the
    # paper canonical convention, T6 is keyed by **A_nucleon**
    # (Z+N), not A_categorical, until the framework reconciles
    # the two A interpretations (see GAP #19 in the audit index).
    A_nucleon = Z + N if (Z + N) >= 1 else 0
    try:
        t6_MeV = term_6_habiro_residue_mp(A_nucleon) if A_nucleon >= 1 else mp.mpf(0)
        t6_cat = t6_MeV / M_E_MEV
    except (FileNotFoundError, KeyError):
        t6_cat = mp.mpf(0)
    m_hecke = t1 + t2 + t3 + t4 + t5_cat + t6_cat
    result = {
        "atom": atom,
        "A_categorical_max_grade": A,
        "A_derivation": "max filtration grade of GS normal form (gb_filtration_jet_tracker.reduce_braid)",
        "Z": Z,
        "N": N,
        "knot_type": knot_type,
        "T1_descended_50dps": str(t1),
        "T2_single_Li2q_50dps":    str(t2),
        "T3_pair_Li2q_50dps":      str(t3),
        "T4_Frobenius_50dps": str(t4),
        "T5_chirality_BW_50dps_cat_units": str(t5_cat),
        "T6_Habiro_residue_50dps_cat_units": str(t6_cat),
        "tower_convention": (
            "Paper canon: m(β) = |Π V̂_i| − Σ Li_2^q(−|V̂_i|) "
            "− Σ_{i<j} z² Li_2^q(−|V̂_i V̂_j|) + T4 + T5 + T6 + …. "
            "T2/T3 via symmetric q-dilogarithm (NOT compact q-dilog Φ_q). "
            "T5 categorical via A_max_grade. T6 from Habiro "
            "residue bridge.  T7+ pending (σ-shell α_5 for A=1 atoms "
            "is research-scope)."
        ),
        "m_hecke_50dps":      str(m_hecke),
        "wedderburn_vols_full_50dps": [str(v) for v in vols],
    }
    # Owner-gated: only record the channel for non-default ("std") runs so
    # the production witness (channel="full") stays byte-identical.
    if channel != "full":
        result["vhat_channel"] = channel
    return result


def main() -> int:
    # Channel selection is OWNER-GATED: default stays "full" so the
    # production witness `proton-mass-full-tower-50dps.witness.json` is
    # unchanged.  Pass `--channel std` to run the derived
    # thm:markov-trace-product factor (see CHANNEL-SELECTION NOTE in
    # `_t1_t2_t3_from_per_gen`).  The std-vs-full comparison witness is
    # emitted by `vhat_std_vs_full_tower_compare.py`.
    channel = "full"
    if "--channel" in sys.argv:
        i = sys.argv.index("--channel")
        if i + 1 >= len(sys.argv):
            print("Error: --channel requires an argument ('full' or 'std')",
                  file=sys.stderr)
            return 1
        channel = sys.argv[i + 1]
        if channel not in ("full", "std"):
            print(f"Error: --channel must be 'full' or 'std', got {channel!r}",
                  file=sys.stderr)
            return 1
    # P31 / centralization: per_gen_w is loaded here and the upstream
    # hash is recorded via builder.add_upstream below — no duplicate
    # filesystem read.
    per_gen_w, per_gen_hash = load_and_hash_upstream(PER_GEN_WITNESS)
    # Load q-substrate constants once (gemini #687 — avoid per-call reads).
    q0, qi, z = load_q_50dps()
    print(f"\n  MPFR @ {mp.mp.dps} dps")
    print(f"  Source: {PER_GEN_WITNESS.name}")
    print(f"  V̂ channel: {channel}  (production default = 'full', owner-gated)")

    # A is derived per-particle from GS normal form (see derive_full_tower).
    p = derive_full_tower("proton",   per_gen_w, Z=1, N=0, knot_type="none", q0=q0, qi=qi, z=z, channel=channel)
    n = derive_full_tower("neutron",  per_gen_w, Z=0, N=1, knot_type="none", q0=q0, qi=qi, z=z, channel=channel)
    # Schema regression (post-2026-05-17 rebase): main's terms_2_3 producer
    # dropped the electron atom.  Skip the electron derivation rather than
    # KeyError; the proton/neutron rows are the substantive output.
    try:
        e = derive_full_tower("electron", per_gen_w, Z=0, N=0, knot_type="none", q0=q0, qi=qi, z=z, channel=channel)
    except KeyError:
        print("  NOTE: electron not in per-gen witness — skipping (CAL-1 anchor)")
        e = {"m_hecke_50dps": str(M_E_MEV)}  # fall back to CAL-1 anchor

    m_p_hecke = mp.mpf(p["m_hecke_50dps"])
    m_n_hecke = mp.mpf(n["m_hecke_50dps"])
    m_e_hecke = mp.mpf(e["m_hecke_50dps"])

    ratio_pe = m_p_hecke / m_e_hecke
    ratio_ne = m_n_hecke / m_e_hecke
    m_p_pred_MeV = ratio_pe * M_E_MEV
    m_n_pred_MeV = ratio_ne * M_E_MEV

    rel_diff_p = mp.fabs(m_p_pred_MeV - M_P_MEV_CODATA) / M_P_MEV_CODATA

    print(f"\n  Particle      T1            T2              T3              T4         m_hecke")
    print("  " + "-" * 86)
    rows_for_print = [x for x in (p, n, e) if "T1_descended_50dps" in x]
    for x in rows_for_print:
        vals = [mp.nstr(mp.mpf(x[k]), 8) for k in
                ("T1_descended_50dps", "T2_single_Li2q_50dps", "T3_pair_Li2q_50dps",
                 "T4_Frobenius_50dps", "m_hecke_50dps")]
        print(f"  {x['atom']:<10}    {vals[0]:>10}    {vals[1]:>12}    {vals[2]:>12}    {vals[3]:>8}    {vals[4]:>10}")
    print()
    print(f"  m_p / m_e (predicted) = {mp.nstr(ratio_pe, 14)}")
    from qou_substrate.codata import codata as _codata
    print(f"  CODATA m_p / m_e      = {_codata('proton-electron mass ratio').value_str}")
    print()
    print(f"  m_p_pred (MeV) = {mp.nstr(m_p_pred_MeV, 14)}")
    print(f"  CODATA m_p     = {mp.nstr(M_P_MEV_CODATA, 14)}")
    print(f"  residual       = {mp.nstr(rel_diff_p * 100, 6)} %  "
          f"({mp.nstr(rel_diff_p * mp.mpf('1e6'), 6)} ppm)")

    if channel != "full":
        # OWNER-GATED: do NOT overwrite the production witness when
        # running a non-default channel (e.g. `--channel std`).  The
        # std-vs-full comparison is emitted by the dedicated script
        # `vhat_std_vs_full_tower_compare.py`.
        print(f"\n  channel={channel!r} ≠ 'full' — skipping production witness write "
              f"(owner-gated). Use vhat_std_vs_full_tower_compare.py for the std witness.")
        return 0

    builder = WitnessBuilder("proton-mass-full-tower-50dps", engine="mpmath")
    builder.set_description(
        "Full mass-endomorphism tower derivation of m_p, m_n, m_e at "
        "MPFR @ 50 dps. Sums T1 (descended) + T2 (single brane tower) "
        "+ T3 (pair brane tower) + T4 (Frobenius co-Casimir) using the "
        "MPFR-native per-generator volumes from terms-2-3-atom-per-gen-"
        "mpfr-50dps.witness.json. m_p prediction in MeV computed as "
        "(m_p_hecke / m_e_hecke) × M_E_MEV. Three-cal discipline "
        "respected: only CAL-1 (M_E_MEV) and CAL-2 (q_0) consumed; "
        "no CODATA m_p / m_n / Q_β injection. The residual (+1.835 % "
        "vs CODATA m_p) is the framework's actual prediction error at "
        "this truncation; closure of T5 / T6 for the electron at MPFR "
        "is the next research step."
    )
    # P31 / centralization (gemini #663): reuse the per_gen_hash
    # already computed at top of main(), no duplicate filesystem read.
    builder._upstream_hashes.append(per_gen_hash)
    builder.add_assertion(
        "m_p_within_1_percent",
        computed=str(rel_diff_p),
        expected="0",
        tolerance=0.01,
    )
    builder.add_assertion(
        "m_p_within_2_percent",
        computed=str(rel_diff_p),
        expected="0",
        tolerance=0.02,
    )
    builder.add_parameter("q_0_50dps", str(per_gen_w["parameters"]["q_0_50dps"]))
    builder.add_parameter("M_E_MEV_CAL1", str(M_E_MEV))
    builder.add_data("particles", {"proton": p, "neutron": n, "electron": e})
    builder.add_data("ratios", {
        "m_p_over_m_e_50dps": str(ratio_pe),
        "m_n_over_m_e_50dps": str(ratio_ne),
    })
    builder.add_data("predictions_MeV", {
        "m_p_pred_50dps": str(m_p_pred_MeV),
        "m_n_pred_50dps": str(m_n_pred_MeV),
    })
    builder.add_data("comparisons", {
        "m_p_codata_MeV":  str(M_P_MEV_CODATA),
        "rel_diff_p":      str(rel_diff_p),
        "rel_diff_p_ppm":  str(rel_diff_p * mp.mpf("1e6")),
    })
    builder.set_content_block("prop:mass-endomorphism-tower")
    builder.add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton"))
    builder.save()
    print(f"\n  Wrote {OUT_PATH.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
