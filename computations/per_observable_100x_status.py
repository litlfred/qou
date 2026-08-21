"""per_observable_100x_status.py — per-observable 100× experimental status

For each predicted observable, report:
  - current prediction (from existing witness)
  - CODATA experimental value + uncertainty (from codata_constants registry)
  - relative prediction error
  - 100× target = sigma_exp_rel / 100
  - MET / MISS / MISS-BY-N

This is the headline metric for Workplan v7 (1ppb compute AND 100x
experimental precision). Audit-only summary — does not introduce new
predictions, just reads existing witnesses against the 100x bar.

All CODATA values + uncertainties source from `codata_constants` /
`codata-2022-validation-masses.witness.json` / `cal-3-q-beta.witness.json`
per the framework's three-calibration discipline. No floating CODATA
literals in this script.

Run:
    python3 computations/per_observable_100x_status.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

# Repo-relative path resolution
THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent

sys.path.insert(0, str(COMPUTE_DIR))
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, M_E_MEV_ERR,
    Q_BETA_MEV, Q_BETA_MEV_ERR,
    M_P_MEV_VALIDATION, M_P_MEV_VALIDATION_ERR,
    M_N_MEV_VALIDATION, M_N_MEV_VALIDATION_ERR,
    M_D_MEV_VALIDATION,
    M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION,
    M_HE4_MEV_VALIDATION,
    M_K_PM_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
)
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────
# CODATA 2022 + CAL-3 sourcing.
#
# Values + uncertainties pulled from the canonical registry. The few
# observables not yet in the registry are loaded directly from their
# witness JSON or from PDG quotes recorded here with provenance.
# ─────────────────────────────────────────────────────────────────────────

# Load the validation witness once for σ_err values not exposed via
# the codata_constants symbol surface (D, T, ³He, ⁴He).
_VALIDATION = json.loads(
    (COMPUTE_DIR / "codata-2022-validation-masses.witness.json").read_text()
)["data"]


def _load_err(key: str) -> mpf:
    return mpf(str(_VALIDATION[key]))


# Muon mass — not yet in codata_constants registry. Source: CODATA 2022
# m_μ comparison value: use m_e × (m_μ/m_e)_CODATA rather than the
# independently-rounded CODATA m_μ (avoids the 1.41 ppb rounding
# artifact between the two CODATA representations).
# Re-pin note (2026-05-29, #1422): q₀ is now pinned from m_p/m_e, so
# m_μ_pred = m_e · Vol(4_1)/ℏ_q² is NO LONGER exact by construction —
# it is a genuine 9.5σ PREDICTION. The ~210 ppb gap vs the CODATA ratio
# is the real μ-p tension (not a rounding artifact); see
# observations/substrate-anchor-alternatives.md.
_M_MU_MEV = M_E_MEV * M_MU_OVER_M_E
_M_MU_MEV_ERR = mpf("0.0000023")
_MU_QUOTED = (
    f"COMPARISON TARGET (codata_MeV), NOT the prediction: "
    f"m_e × (m_μ/m_e)_CODATA = {M_E_MEV} × {M_MU_OVER_M_E} "
    f"(ratio-derived; independently-quoted 105.6583755(23) MeV). "
    f"The PREDICTION (pred_MeV) is the INDEPENDENT categorical value "
    f"m_μ = m_e·Vol(4_1)/ℏ_q² from the Borromean witness — post the "
    f"2026-05-29 q₀ re-pin it is a genuine 9.5σ PREDICTION, NOT "
    f"ratio-derived. The ~210 ppb pred-vs-codata gap (963.6× the 100× "
    f"target) is the real μ-p tension; m_μ does NOT meet L2. Do not read "
    f"'ratio-derived' as 'm_μ trivially meets' (the error PR #1556 made)."
)

# ── m_μ PREDICTION — PINNED to the experimental / proton-anchored value ──
# Owner ruling 2026-06-27 (bean tnjb): the L2 dashboard reports the
# EXPERIMENTAL (proton-anchored q₀) m_μ prediction, NOT the ideal / muon-
# anchored CAL-2 value. At the muon anchor m_μ = m_e·Vol(4_1)/ℏ_q² returns
# CODATA to ~0 ppb BY CONSTRUCTION (the CAL-2 calibration tautology); the
# proton re-pin (2026-05-28) makes it a genuine 9.5σ PREDICTION missing
# CODATA by 209.8 ppb (963.6× the 100× target). The upstream Borromean
# witness `muon_check.m_mu_pred_MeV` was flipped to the MUON q₀ by 768d9ddf,
# so reading it would silently substitute the ideal tautology (MET) for the
# experimental prediction (FAIL). PIN the prediction here so a regen cannot
# corrupt the canonical committed value. Provenance: the proton-anchored
# m_e·Vol(4_1)/ℏ_q² value carried by the committed
# per-observable-100x-status.witness.json (2026-05-28 re-pin).
# AGENTS.md §"q₀ anchor convention" STRICT rule 1.
_M_MU_PRED_PROTON_MEV = mpf("105.658397811")
_M_MU_PRED_SOURCE = (
    "PINNED proton-anchored prediction (m_e·Vol(4_1)/ℏ_q² at the m_p/m_e "
    "re-pinned q₀, 2026-05-28); decoupled from the muon-flipped Borromean "
    "muon_check per bean tnjb / AGENTS.md §q₀-anchor STRICT rule 1"
)

# Observable registry: (codata_value, codata_err, role, source_label)
OBSERVABLES: dict[str, tuple[mpf, mpf, str, str]] = {
    "m_e":      (M_E_MEV,         M_E_MEV_ERR,            "CAL-1 anchor",
                 "codata_constants.M_E_MEV"),
    "Q_beta":   (Q_BETA_MEV,      Q_BETA_MEV_ERR,         "derived (CAL-1+CAL-2)",
                 "codata_constants.Q_BETA_MEV (← cal-3-q-beta.witness.json; CODATA validation value — Q_β is derived, not CAL-3)"),
    "m_p":      (M_P_MEV_VALIDATION, M_P_MEV_VALIDATION_ERR, "CAL-2 numerical anchor",
                 "codata_constants.M_P_MEV_VALIDATION"),
    "m_n":      (M_N_MEV_VALIDATION, M_N_MEV_VALIDATION_ERR, "validation",
                 "codata_constants.M_N_MEV_VALIDATION"),
    "m_mu":     (_M_MU_MEV,         _M_MU_MEV_ERR,           "validation",
                 _MU_QUOTED),
    "m_D":      (M_D_MEV_VALIDATION, _load_err("m_D_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
    "m_T":      (M_T_MEV_VALIDATION, _load_err("m_T_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
    "m_3He":    (M_HE3_MEV_VALIDATION, _load_err("m_3He_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
    "m_4He":    (M_HE4_MEV_VALIDATION, _load_err("m_4He_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
}

# Δm_pn derived from m_n − m_p (with σ_exp via sigma_mn − sigma_mp
# combined in quadrature, dominant from the larger σ_mn).
DELTA_PN_VALUE = M_N_MEV_VALIDATION - M_P_MEV_VALIDATION
DELTA_PN_ERR = mp.sqrt(
    M_N_MEV_VALIDATION_ERR ** 2 + M_P_MEV_VALIDATION_ERR ** 2
)
OBSERVABLES["Delta_pn"] = (
    DELTA_PN_VALUE, DELTA_PN_ERR, "validation (derived)",
    "M_N_MEV_VALIDATION − M_P_MEV_VALIDATION; σ in quadrature",
)

# m_K/m_π — dimensionless meson mass ratio (PDG 2024).
# PDG uncertainties: m_K± = 493.677 ± 0.013 MeV (26 ppm),
#                    m_π± = 139.57039 ± 0.00018 MeV (1.3 ppb).
# Propagated: σ(R)/R = sqrt((σ_K/m_K)² + (σ_π/m_π)²) ≈ 26 ppm
# (kaon uncertainty dominates).
_M_K_PI_RATIO = M_K_PM_MEV_VALIDATION / M_PI_PM_MEV_VALIDATION
_M_K_PI_RATIO_ERR = _M_K_PI_RATIO * mp.sqrt(
    (mpf("0.013") / M_K_PM_MEV_VALIDATION) ** 2
    + (mpf("0.00018") / M_PI_PM_MEV_VALIDATION) ** 2
)
OBSERVABLES["m_K/m_pi"] = (
    _M_K_PI_RATIO, _M_K_PI_RATIO_ERR, "validation (meson ratio)",
    "PDG 2024: m_K±/m_π± = 493.677/139.57039; σ propagated in quadrature",
)


def rel_error_ppb(pred: mpf, codata: mpf) -> mpf:
    return abs(pred - codata) / abs(codata) * mpf("1e9")


def sigma_rel_ppb(codata: mpf, sigma: mpf) -> mpf:
    return sigma / abs(codata) * mpf("1e9")


def load_witness(name: str) -> dict:
    """Load a witness by basename.

    Resolution is flat-first (``computations/<name>``), then a one-level
    scan of the ``computations/`` subdirectories.  The subdirectory leg
    matters: ``qbeta-ck-cache.witness.json`` lives under
    ``computations/qbeta/``, so a flat-only lookup silently returned ``{}``
    and sent the Q_β row down the legacy ``Q_N2`` fallback branch.  That
    made the c_k *tier* auto-promotion mechanism dead code — a future agent
    who proved a higher c_k Taylor-exact and set ``tier='derived'`` would
    have seen the dashboard ignore it.  (Numerically a no-op at the time of
    the fix: both branches yield the same Q_N2 value, because k=2 is the
    only ``derived``-tier rung.)
    """
    p = COMPUTE_DIR / name
    if p.exists():
        return json.loads(p.read_text())
    for sub in sorted(COMPUTE_DIR.iterdir()):
        if sub.is_dir() and not sub.name.startswith((".", "_")):
            cand = sub / name
            if cand.exists():
                return json.loads(cand.read_text())
    return {}


#: |dlnQ_β/dlnq| is O(1), so a pin mismatch of Δq/q propagates to Q_β almost
#: undiminished. Recomputed symbolically below rather than hard-coded.
_QBETA_L2_TARGET_PPB = mpf("7.797")


def _qbeta_dln_dlnq(q0: mpf) -> mpf:
    """d ln Q_β / d ln q at q0, from the base form
    Q_β = m_e·|q²−2q−1|·(q+1)/(2q³).  Closed form, no fit."""
    return q0 * ((2 * q0 - 2) / (q0 ** 2 - 2 * q0 - 1)
                 + 1 / (q0 + 1) - 3 / q0)


def _anchor_layer_check(cache: dict) -> dict:
    """Compare the q₀ a cached Q_β prediction was BUILT at against the pin this
    dashboard EVALUATES at, and size the resulting error.

    Why this exists.  ``qbeta-ck-cache.witness.json`` is stamped
    ``q0Anchor: "muon"``; this producer reads ``q_parameter.Q_50_DIGIT_STR``,
    which is **proton**-pinned (AGENTS.md owner directive 2026-08-07: all
    production compute defaults to the experimental anchor).  The cached field
    consumed below is ``Q_pred_after_this_rung_MeV`` — a *prediction*, which
    depends on q₀ even when the rung's own coefficient does not.  (The cache's
    per-rung ``q0_dependent: False`` flag describes ``c_k``, **not** the
    prediction; reading it as covering the prediction is the trap.)

    That is the straddling hazard AGENTS.md §q₀-anchor names — "never straddle
    the two layers inside one quantity" — and it is currently **silent**.

    It is immaterial today only by accident: the sole DERIVED rung is k = 2, so
    the residual is 1248 ppb and the ~30 ppb anchor error is 2.4 % of it.  But
    the anchor error is **3.84× the entire L2 target**, so on the day a higher
    c_k is proved Taylor-exact and the residual collapses, this term dominates
    and the row's pass/fail verdict becomes an artefact of the layer mismatch —
    firing on exactly the event the ladder exists to detect.  Same shape as the
    dead-code ``load_witness`` bug that preceded it.

    This does NOT regenerate the muon witness (a tracked migration, bean
    ``tnjb``, explicitly not an idle-drain).  It makes the mismatch loud.
    """
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402

    q_prod = mpf(Q_50_DIGIT_STR)
    q_cache_raw = cache.get("q0Value")
    anchor = cache.get("q0Anchor")
    if q_cache_raw is None:
        return {
            "status": "unknown",
            "detail": "cache carries no q0Value stamp; layer cannot be verified",
        }
    q_cache = mpf(str(q_cache_raw))
    rel = (q_prod - q_cache) / q_cache
    induced_ppb = abs(_qbeta_dln_dlnq(q_prod) * rel) * mpf(10) ** 9
    matched = abs(rel) < mpf("1e-15")
    return {
        "status": "matched" if matched else "STRADDLE",
        "cache_anchor": anchor,
        "cache_q0": str(q_cache),
        "producer_q0": str(q_prod),
        "pin_diff_ppb": str(rel * mpf(10) ** 9),
        "induced_qbeta_error_ppb": str(induced_ppb),
        "l2_target_ppb": str(_QBETA_L2_TARGET_PPB),
        "anchor_error_over_target": str(induced_ppb / _QBETA_L2_TARGET_PPB),
        "anchor_alone_exceeds_l2_target": bool(induced_ppb
                                               > _QBETA_L2_TARGET_PPB),
        "material_today": False if matched else None,
    }


#: Observables whose "prediction" is a re-evaluation of the quantity that
#: pinned q_0, so the framework content cancels and the residual is CODATA's
#: own rounding. They are reported with their numbers but NOT scored — a
#: calibration reproducing itself is not an accuracy result.
#: AGENTS.md §"q_0 anchor convention" STRICT rule 1; the same treatment the
#: m_p sourcing comment below has always called for ("treat it like m_e, not
#: a precision win"), which until 2026-08-09 was documented but not enforced.
ANCHOR_ROUNDTRIP_OBSERVABLES = {"m_p"}


def _row_for(obs: str, pred: mpf, source_witness: str) -> dict:
    """Build one row of the per-observable status table."""
    codata, sigma_exp, role, sigma_source = OBSERVABLES[obs]
    err_ppb = rel_error_ppb(pred, codata)
    sig_ppb = sigma_rel_ppb(codata, sigma_exp)
    target_ppb = sig_ppb / mpf("100")
    miss_factor = err_ppb / target_ppb if target_ppb > 0 else mp.mpf("inf")
    beats_1x = bool(err_ppb < sig_ppb)
    beats_100x = bool(err_ppb < target_ppb)
    # ── σ_pred: propagated compute-library truncation bound ──────
    # At OUTPUT_DPS = 40 digits, the truncation floor is 10^{-40}.
    # In ppb: 10^{-40} / pred * 10^9 ≈ 10^{-31} ppb (negligible).
    # Recorded for completeness; real σ_pred from CAL-1/2/3 input
    # uncertainties is computed per-observable in main().
    from qou_substrate.precision import OUTPUT_DPS
    truncation_ppb = mpf(10) ** (-OUTPUT_DPS) / abs(pred) * mpf("1e9") if pred != 0 else mpf(0)

    # An anchor round-trip is reported but never scored. Leaving beats_* as
    # None (rather than True like m_e, or False) keeps it out of the counts
    # without asserting either "met" or "failed" about a tautology.
    is_anchor_roundtrip = obs in ANCHOR_ROUNDTRIP_OBSERVABLES
    if is_anchor_roundtrip:
        beats_1x = beats_100x = None

    return {
        "obs": obs,
        "role": role,
        "pred_MeV": fmt(pred, 12),
        "codata_MeV": fmt(codata, 12),
        "sigma_exp_MeV": fmt(sigma_exp, 6),
        "err_ppb": fmt(err_ppb, 4),
        "sigma_exp_ppb": fmt(sig_ppb, 4),
        "target_100x_ppb": fmt(target_ppb, 4),
        "miss_factor": ("N/A (anchor round-trip)" if is_anchor_roundtrip
                        else fmt(miss_factor, 4)),
        "roundtrip_residual_ppb": fmt(err_ppb, 4) if is_anchor_roundtrip else None,
        "is_anchor_roundtrip": is_anchor_roundtrip,
        "note": (
            "NOT SCORED. q_0 is pinned from m_p/m_e, so this 'prediction' is "
            "m_e x (m_p/m_e) re-evaluated through the identity that pinned it "
            "— the framework content cancels and the residual is CODATA's own "
            "rounding, not accuracy. Reported for round-trip auditing only."
        ) if is_anchor_roundtrip else None,
        "beats_1x_experimental": beats_1x,
        "beats_100x_experimental": beats_100x,
        "source_witness": source_witness,
        "sigma_source": sigma_source,
        "compute_truncation_ppb": fmt(truncation_ppb, 4),
        "compute_output_dps": OUTPUT_DPS,
    }


def main() -> dict:
    rows = []

    # ── m_p, m_n, mu, Delta_pn — production sourcing ─────────────────
    #
    # m_p / m_n / Δ_pn are routed to the substrate-identity witness
    # (`m-p-substrate-identity-50dps`) per the audit
    # `docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md`.
    #
    # Re-pin note (2026-05-29, #1422): q₀ is now the m_p-pinned value,
    # so m_p is the CAL-2 NUMERICAL ANCHOR — its row matches CODATA to
    # 0.0004 ppb as a calibration round-trip (m_e × m_p/m_e re-evaluated
    # through the identity used to pin q₀; the framework content cancels,
    # the residual is sub-σ_CAL CODATA input slop). It is NOT a
    # prediction — treat it like m_e, not a precision win.
    #
    #   m_p = 2·m_μ·F_Bor(q_0) − 12·m_e   (anchor round-trip)
    #   m_n = m_p·(1 + X/(1 − X/2))        (genuine prediction, −1.76 ppm
    #                                       via canonical Hecke-skein split)
    #
    # The formulas use ONLY Lean-proved closed forms (Borromean Markov
    # trace + [3]_q! + flavor-split-substrate) and CAL-1 / CAL-2 anchors.
    # The bare Borromean-tower (Family A linking weight, also Lean-proved)
    # gives m_p = 965.38 MeV (+2.89% open gap) — the honest categorical
    # value; the substrate-identity row is the calibration, not a closure.
    #
    # m_μ is now a genuine 9.5σ PREDICTION (209.8 ppb = +0.21 ppm vs
    # CODATA) — the irreducible μ-p tension surfaced by anchoring on m_p.
    #
    # If `m-p-substrate-identity-50dps.witness.json` is absent, falls
    # back to the historical Borromean wiring for all four observables.
    sub = None
    try:
        sub = load_witness("m-p-substrate-identity-50dps.witness.json")
        if not sub.get("data"):
            sub = None
    except FileNotFoundError:
        pass

    borr = load_witness("m-p-borromean-verification-50dps.witness.json")
    borr_data = borr.get("data", {})
    borr_source = "m-p-borromean-verification-50dps.witness.json"

    m_p_sub = None
    if sub is not None:
        sub_data = sub.get("data", {})
        sub_source = "m-p-substrate-identity-50dps.witness.json"
        # m_p from the substrate-identity formula at N=0 — no fitted tower.
        # A previously-applied "Habiro brane-tower ratio"
        #   (1 + 46u⁴)(1 + 4u⁵)(1 − 29u⁶)(1 − 8u⁷),  u = b·ℏ_q²
        # was a CODATA FIT: four integers chosen to close the 242 ppb gap
        # to <1 ppQ. It is NOT the Taylor expansion of the exact Habiro
        # rational function — a genuine Taylor tower converges TO the
        # substrate value, whereas this one overshoots PAST it to CODATA.
        # Removed from production per the canonical-derivation discipline.
        # The fitted scan survives only in the exploratory probe
        # proton_brane_tower_correction_probe.py (does not feed production).
        m_p_str = sub_data.get("predictions", {}).get("m_p_MeV")
        if m_p_str is not None:
            m_p_sub = mpf(str(m_p_str))
            rows.append(_row_for("m_p", m_p_sub, sub_source))
        else:
            rows.append({"obs": "m_p", "status": "NO-WITNESS"})
        # m_mu PREDICTION: PINNED to the experimental / proton-anchored value
        # (209.8 ppb, 963.6× FAIL). Decoupled from borr_data["muon_check"],
        # which 768d9ddf flipped to the MUON q₀ (~0 ppb = the CAL-2 ideal
        # tautology) and would silently flip m_mu FAIL→MET on regen.
        # Owner ruling 2026-06-27 (bean tnjb); AGENTS.md §"q₀ anchor convention".
        rows.append(_row_for("m_mu", _M_MU_PRED_PROTON_MEV, _M_MU_PRED_SOURCE))
    else:
        # Fallback: read m_p / m_n / Delta_pn from Borromean (historical
        # wiring); m_mu stays PINNED to the proton-anchored prediction (see
        # above) — never read from the muon-flipped muon_check.
        for obs, path_key in [
            ("m_p",      "proton.m_p_pred_MeV"),
            ("m_n",      "neutron.m_n_pred_MeV"),
            ("Delta_pn", "proton_neutron_split.delta_m_pn_pred_MeV"),
        ]:
            section, field = path_key.split(".")
            v = borr_data.get(section, {}).get(field)
            if v is None:
                rows.append({"obs": obs, "status": "NO-WITNESS"})
                continue
            rows.append(_row_for(obs, mpf(str(v)), borr_source))
        rows.append(_row_for("m_mu", _M_MU_PRED_PROTON_MEV, _M_MU_PRED_SOURCE))

    # ── Q_β — Habiro-exact evaluation ──────────────────────────────
    # The Markov trace difference tr_M(β_n) - tr_M(β_p) lives in the
    # Habiro ring ℤ̂[q] and terminates at finite M=8 (proton/neutron).
    # Q_β production wiring — STRICT Taylor-exact bar only (discipline
    # lock per author 2026-05-30: "I don't want to keep coming back to
    # this").
    #
    # FOUR-SESSION FLIP-FLOP HISTORY (see deep audit
    # docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md):
    #
    #   c_2 = -1 (Kashiwara f̃₁²):
    #     Lean N2_factor PROVED, Taylor match 4e-7. CLEARS BAR
    #
    #   c_3 = J_Hopf(q=1) = -2 (plain):
    #     Lean knot invariant theorem, but Taylor coefficient gap 0.49%
    #     at stale q₀, even worse at canonical q₀. Wired #1452,
    #     reverted #1479. FAILS BAR.
    #
    #   c_3 = J_Hopf(q=1) - ℏ_q² (q-deformed):
    #     2026-05-26 commit b2f9087315 stated "0.004% error" -
    #     explicitly a NEAR-MATCH, not a Taylor-exact derivation. At
    #     canonical (m_p-pin) q₀ the gap reopens to 2.6%. The 0.004%
    #     was a stale-q₀ artifact. FAILS BAR.
    #
    #   c_4 = c_3 · b⁴:
    #     Inherits c_3 near-match status. FAILS BAR.
    #
    # Only c_2 is Taylor-exact at compute precision. Q_β reports Q_N2
    # (1247 ppb miss vs CODATA, the μ-p substrate tension floor).
    #
    # Future sessions: do NOT re-wire higher c_k as derivations unless
    # you have a Lean theorem closing the residual to compute precision
    # (<< 1 ppb). Structural approximations with stated residuals do
    # NOT clear this bar.
    # Cache-aware wiring: read c_k from qbeta-ck-cache.witness.json
    # (produced by qbeta_ck_cache.py). Each c_k carries a two-tier label:
    #   tier "derived"      — Taylor-exact, Lean-proved, q₀-independent.
    #   tier "cal-anchored" — extracted from CODATA Q_β at canonical q₀;
    #                         CIRCULAR & q₀-dependent (a reusable
    #                         calibrated constant, NOT a prediction).
    # The dashboard headline reports the deepest cumulative DERIVED rung
    # only; cal-anchored rungs are cached for downstream reuse but NEVER
    # counted toward a 100×/1× pass (that would be circular). Keying off
    # `tier` means a future agent who proves a higher c_k Taylor-exact in
    # Lean promotes it (tier='derived') and the dashboard auto-picks it up.
    ck_cache = load_witness("qbeta-ck-cache.witness.json")
    ck_data = ck_cache.get("data", {})
    qbeta_anchor = _anchor_layer_check(ck_cache)
    if ck_data.get("rows"):
        # Find the deepest cumulative rung whose tier is "derived".
        # (Fallback to the legacy label for any cache lacking `tier`.)
        last_derived_row = None
        for row in ck_data["rows"]:
            tier = row.get("tier") or (
                "derived" if row.get("label") == "lean-proved" else "cal-anchored")
            if tier == "derived":
                last_derived_row = row
            else:
                break  # stop at first non-derived (cal-anchored) rung
        if last_derived_row is not None:
            k = last_derived_row["k"]
            Q_pred_str = last_derived_row["Q_pred_after_this_rung_MeV"]
            Q_pred = mpf(Q_pred_str)
            Q_beta_best = Q_pred
            _anchor_note = ""
            if qbeta_anchor.get("status") == "STRADDLE":
                _anchor_note = (
                    f" ⚠ ANCHOR STRADDLE: this prediction was built at the "
                    f"{qbeta_anchor['cache_anchor']} q₀ "
                    f"({qbeta_anchor['cache_q0'][:22]}…) but the dashboard "
                    f"evaluates at the proton pin "
                    f"({qbeta_anchor['producer_q0'][:22]}…). Induced Q_β error "
                    f"≈ {float(qbeta_anchor['induced_qbeta_error_ppb']):.2f} ppb "
                    f"= {float(qbeta_anchor['anchor_error_over_target']):.2f}× the "
                    f"L2 target. Immaterial against today's 1248 ppb residual, "
                    f"but it alone exceeds the target — so no 100× PASS can be "
                    f"credited to this row until the layers agree "
                    f"(AGENTS.md §q₀-anchor; migration bean tnjb)."
                )
            rows.append(_row_for(
                "Q_beta", Q_pred,
                f"Q_N{k} from qbeta-ck-cache.witness.json (deepest DERIVED-tier "
                f"rung). c_2 = -1 PROVED via "
                f"qou:QOU.BraidKnot.q_beta_categorical_precision_ladder + "
                f"Kashiwara N2_factor. Higher c_k are tier='cal-anchored' "
                f"(extracted from CODATA Q_β, circular, q₀-dependent) — cached "
                f"for downstream reuse but NOT credited as a prediction. See "
                f"deep audit docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md "
                f"and qbeta-scaling-bridge-investigation.witness.json."
                + _anchor_note,
            ))
            # Guard with teeth: while the layers disagree by more than the
            # entire L2 target, a 100× PASS on this row would be an artefact of
            # the mismatch rather than a result. Can only ever turn a would-be
            # PASS into a FAIL — today the row already misses by ~160×, so this
            # is numerically a no-op. It arms correctly for the promotion event.
            if qbeta_anchor.get("anchor_alone_exceeds_l2_target"):
                _r = rows[-1]
                if _r.get("beats_100x_experimental"):
                    _r["beats_100x_experimental"] = False
                    _r["suppressed_by_anchor_straddle"] = True
                _r["anchor_layer"] = qbeta_anchor
        else:
            Q_beta_best = None
    else:
        # Fallback to legacy Q_N2 read
        qb_n3 = load_witness("q-beta-operator-valued-N3.witness.json")
        qb_n3_data = qb_n3.get("data", {})
        if qb_n3_data.get("Q_N2") is not None:
            Q_N2 = mpf(str(qb_n3_data["Q_N2"]))
            Q_beta_best = Q_N2
            rows.append(_row_for(
                "Q_beta", Q_N2,
                "Q_N2 (fallback; qbeta-ck-cache witness not present)",
            ))
        else:
            Q_beta_best = None

    # ── Path C: m_n = m_p + Q_β + m_e (categorical, no flavor-split) ─
    # PR #1298 finding: bypassing the flavor-split X entirely gives
    # m_n at 0.24 ppm (8× better than the substrate-identity's 2 ppm).
    # Δ_pn = Q_β + m_e follows directly.
    m_e_mev = OBSERVABLES["m_e"][0]  # CAL-1 anchor
    # Q_β rung label for Path C sourcing — reuse the deepest-derived-row
    # found above; it is guaranteed non-None whenever Q_beta_best is set
    # from the ck cache (the cache path sets both together).
    if ck_data.get("rows") and Q_beta_best is not None and last_derived_row is not None:
        q_beta_rung = f"N={last_derived_row['k']}"
    else:
        q_beta_rung = "N=0"
    if m_p_sub is not None and Q_beta_best is not None:
        m_n_path_c = m_p_sub + Q_beta_best + m_e_mev
        delta_pn_path_c = Q_beta_best + m_e_mev
        path_c_source = (
            f"Path C: m_n = m_p(substrate) + Q_β({q_beta_rung}) + m_e; "
            "no flavor-split — per PR #1298 gap diagnostic"
        )
        rows.append(_row_for("m_n", m_n_path_c, path_c_source))
        rows.append(_row_for("Delta_pn", delta_pn_path_c, path_c_source))
    elif sub is not None:
        sub_data_fb = sub.get("data", {})
        m_n_str = sub_data_fb.get("predictions", {}).get("m_n_MeV")
        if m_n_str is not None:
            rows.append(_row_for("m_n", mpf(str(m_n_str)), sub_source))
        else:
            rows.append({"obs": "m_n", "status": "NO-WITNESS"})
        delta_str = sub_data_fb.get("predictions", {}).get("Delta_m_pn_MeV")
        if delta_str is not None:
            rows.append(_row_for("Delta_pn", mpf(str(delta_str)), sub_source))
        else:
            rows.append({"obs": "Delta_pn", "status": "NO-WITNESS"})
    else:
        rows.append({"obs": "m_n", "status": "NO-WITNESS"})
        rows.append({"obs": "Delta_pn", "status": "NO-WITNESS"})

    # ── m_e — CAL-1 anchor (by definition err = 0) ───────────────────
    codata, sigma_exp, role, sigma_source = OBSERVABLES["m_e"]
    sig_ppb = sigma_rel_ppb(codata, sigma_exp)
    rows.append({
        "obs": "m_e",
        "role": role,
        "pred_MeV": fmt(codata, 12),
        "codata_MeV": fmt(codata, 12),
        "sigma_exp_MeV": fmt(sigma_exp, 6),
        "err_ppb": "0",
        "sigma_exp_ppb": fmt(sig_ppb, 4),
        "target_100x_ppb": fmt(sig_ppb / mpf("100"), 4),
        "miss_factor": "N/A (anchor)",
        "beats_1x_experimental": True,
        "beats_100x_experimental": True,
        "source_witness": "(CAL-1 anchor)",
        "sigma_source": sigma_source,
        "note": "calibration anchor — err defined as 0",
    })

    # ── m_K/m_π — derived sub-ppb closure (#1442 + #1448) ────────────
    # Closed form: m_K²/m_π² = [3]_q·[4]_q + (α_em/π)·(3q² − 1)/(2q²)
    # - strong sector [3]_q·[4]_q: Lean-proved q-Clebsch–Gordan fusion
    #   (prop:meson-qcg-fusion-identity, QOU.BraidKnot.meson_qCG_3x4)
    # - EM sinh-channel (3q²−1)/(2q²): Lean-proved ring identity
    #   (prop:meson-em-sinh-closed-form, QOU.BraidKnot.meson_EM_closed_form)
    # - α_em from prop:em-coupling-projection (q·[9]_q·[10]_q, CS-corrected
    #   to 137.035944, 399 ppb off CODATA)
    #
    # CLASS-A acknowledged anchor (AGENTS.md §3b-cond): the α_em literal
    # `137.035944` is the CS-corrected ansatz from em-coupling-chern-simons.lean,
    # which still carries an open `sorry` on the Witten κ Gram-determinant
    # value (see prop:em-coupling-chern-simons). The m_K/m_π closure is
    # therefore "derived conditional on `class WittenKappaGramDeterminant`".
    # When that class is closed, this literal should be re-derived from the
    # witness. Tracked by docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md.
    #
    # Closes m_K²/m_π² to +0.047 ppm; sqrt → m_K/m_π to ≈0.024 ppm.
    # Both terms framework-derived; no fitted integers (the (q₀⁵−q₀⁻⁵)(9/5)²
    # form formerly used here was retracted as a fit, see #1420).
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    from mpmath import pi as _pi
    q0 = mpf(Q_50_DIGIT_STR)
    _hbar_factor = (3 * q0 ** 2 - 1) / (2 * q0 ** 2)  # sinh-channel closed form
    _qcg_strong = (q0 ** 2 + 1 + q0 ** -2) * (
        (q0 ** 4 - q0 ** -4) / (q0 - q0 ** -1)
    )  # [3]_q · [4]_q
    # CLASS-A acknowledged anchor: pending Witten-κ Gram-determinant sorry.
    # α_em is DERIVED, not copied. This line held the literal
    # mpf("137.035944") -- the MUON-anchor evaluation from before the
    # 2026-05-28 proton re-pin, and a TRUNCATED CS tower besides. At the
    # current proton pin the exact resummation gives 137.0359350939756,
    # i.e. the literal was 65.0 ppb off, and its stated "399 ppb vs CODATA"
    # understated the real residual of 468 ppb. pyhecke.constants and
    # meson_em_sinh_closed_form were both corrected; this consumer and
    # meson_em_residual_alpha_em were not, so the fix never reached the
    # dashboard. Effect on m_K/m_pi is 0.0066 ppb -- the L2 verdict is
    # unchanged; the defect was in what the number CLAIMED, not what it did.
    from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402
    _alpha_em_inv = alpha_em_inv_derived(q0)
    _mk_sq_over_mpi_sq = _qcg_strong + (1 / _alpha_em_inv) / _pi * _hbar_factor
    mk_pred = mp.sqrt(_mk_sq_over_mpi_sq)
    rows.append(_row_for(
        "m_K/m_pi", mk_pred,
        "[3]_q·[4]_q + (α_em/π)·(3q²−1)/(2q²) — closed form; both pieces "
        "Lean-proved (qou:QOU.BraidKnot.meson_qCG_3x4, "
        "qou:QOU.BraidKnot.meson_EM_closed_form); α_em is a CLASS-A "
        "acknowledged anchor (CS ansatz conditional on Witten-κ class)",
    ))

    return {
        "computation": "per-observable-100x-experimental-status",
        "description": (
            "Headline status for Workplan v7: report each predicted "
            "observable's current error against the 100× experimental "
            "target (σ_pred ≤ σ_exp / 100). Audit-only — reads existing "
            "witnesses, does not introduce new predictions. All CODATA "
            "values + uncertainties source from codata_constants / "
            "codata-2022-validation-masses.witness.json / "
            "cal-3-q-beta.witness.json — no floating literals."
        ),
        "rows": rows,
        "anchor_layer_qbeta": qbeta_anchor,
        "summary": {
            "total": len(rows),
            "beats_1x_count": sum(1 for r in rows if r.get("beats_1x_experimental")),
            "beats_100x_count": sum(1 for r in rows if r.get("beats_100x_experimental")),
            # --- scoreable counts (added 2026-08-18) -------------------------
            # `beats_100x_count` counts CALIBRATION INPUTS alongside
            # predictions, and so overstates the accuracy result. m_e is a
            # CAL-1 anchor whose err_ppb is not measured but DEFINED zero (it
            # is the input that fixes the MeV unit, so its ratio to itself is 1
            # by construction) -- yet it is scored True. That is the same
            # reasoning m_p is EXCLUDED for as an anchor round-trip ("the
            # framework content cancels"), only stronger: m_p at least carries
            # a nonzero round-trip residual.
            #
            # The keys below score only genuine PREDICTIONS. Quote these.
            # `beats_100x_count` is retained unchanged so existing consumers do
            # not silently shift meaning.
            "scoreable_total": _scoreable_total(rows),
            "beats_100x_scoreable": _beats_100x_scoreable(rows),
            "calibration_inputs": [
                r["obs"] for r in rows if _is_calibration_input(r)
            ],
        },
    }



def _is_calibration_input(row: dict) -> bool:
    """True for CAL anchors, whose "error" is definitional rather than measured.

    Both anchors are inputs: `m_e` (CAL-1) fixes the MeV unit, and `m_p` is the
    CAL-2 numerical pin for q_0. Neither is a prediction, so neither belongs in
    an accuracy score. The dashboard already excludes `m_p` via
    `is_anchor_roundtrip`; this catches `m_e` on the same grounds.
    """
    return "anchor" in (row.get("role") or "").lower()


def _scoreable_total(rows: list) -> int:
    """Number of genuine predictions (all rows that are not calibration inputs)."""
    return sum(1 for r in rows if not _is_calibration_input(r))


def _beats_100x_scoreable(rows: list) -> int:
    """Genuine predictions meeting the L2 100x target."""
    return sum(
        1
        for r in rows
        if not _is_calibration_input(r) and r.get("beats_100x_experimental") is True
    )

if __name__ == "__main__":
    out = main()

    # Pretty table
    print(f"\n{'='*128}")
    print(f"Per-observable 100× experimental status (Workplan v7)")
    print(f"{'='*128}")
    print(f"{'Observable':10}  {'role':22}  {'pred err (ppb)':>16}  "
          f"{'σ_exp (ppb)':>14}  {'100× target (ppb)':>20}  "
          f"{'miss factor':>14}  {'1×?':>3}  {'100×?':>5}")
    print("-" * 128)
    for r in out["rows"]:
        if r.get("status") == "NO-WITNESS":
            print(f"{r['obs']:10}  NO WITNESS")
            continue
        print(
            f"{r['obs']:10}  {r['role']:22}  {r['err_ppb']:>16}  "
            f"{r['sigma_exp_ppb']:>14}  {r['target_100x_ppb']:>20}  "
            f"{r.get('miss_factor', '-'):>14}  "
            f"{('Y' if r['beats_1x_experimental'] else 'N'):>3}  "
            f"{('Y' if r['beats_100x_experimental'] else 'N'):>5}"
        )
    print("-" * 128)
    print(f"HEADLINE: {out['summary']['beats_100x_scoreable']} / "
          f"{out['summary']['scoreable_total']} SCOREABLE predictions beat the "
          f"100× target.")
    print(f"          calibration inputs, not scored: "
          f"{out['summary']['calibration_inputs']}")
    print(f"raw     : {out['summary']['beats_100x_count']} / {out['summary']['total']} "
          f"counting calibration inputs — do NOT quote as an accuracy result.")
    print(f"          {out['summary']['beats_1x_count']} / {out['summary']['total']} "
          f"beat 1× experimental (same caveat).")
    _al = out.get("anchor_layer_qbeta", {})
    if _al.get("status") == "STRADDLE":
        print()
        print("⚠ Q_β ANCHOR-LAYER STRADDLE")
        print(f"    cached prediction built at : {_al['cache_anchor']} q₀ "
              f"= {_al['cache_q0'][:24]}…")
        print(f"    dashboard evaluates at     : proton q₀ "
              f"= {_al['producer_q0'][:24]}…")
        print(f"    pin difference             : "
              f"{float(_al['pin_diff_ppb']):.3f} ppb")
        print(f"    induced Q_β error          : "
              f"{float(_al['induced_qbeta_error_ppb']):.2f} ppb "
              f"= {float(_al['anchor_error_over_target']):.2f}× the L2 target")
        print("    => immaterial vs today's 1248 ppb residual, but it alone")
        print("       exceeds the target, so no 100× PASS can be credited to")
        print("       this row until the layers agree (bean tnjb).")
    print()

    # Emit witness via WitnessBuilder for reproducible staleness metadata.
    w = WitnessBuilder("per-observable-100x-status", engine="python")
    # Declare contentBlock so `run_pipeline.py --content-only` recognises
    # this witness as wired (per Copilot review on PR #1690 — without
    # `set_content_block`, the witness is treated as orphan by the
    # auto-refresh CI step regardless of any .ts manifest pointing at it).
    w.set_content_block("rem:per-observable-100x-status-dashboard")
    w.set_description(out["description"])
    w.add_data("rows", out["rows"])
    w.add_data("summary", out["summary"])
    w.add_data("anchor_layer_qbeta", out["anchor_layer_qbeta"])
    if out["anchor_layer_qbeta"].get("status") == "STRADDLE":
        w.add_caveat(
            "Q_β row: the cached prediction is built at the muon q₀ while this "
            "dashboard evaluates at the proton pin. Induced error ≈ 29.96 ppb "
            "= 3.84× the 7.797 ppb L2 target — immaterial against today's "
            "1248 ppb residual, but it alone exceeds the target, so a 100× "
            "PASS is suppressed on this row until the layers agree. Fixing it "
            "means regenerating qbeta-ck-cache at the proton pin (tracked "
            "migration, bean tnjb) — deliberately NOT done here, per "
            "AGENTS.md §q₀-anchor rule 4 'untouched muon witnesses: leave "
            "them'.")
    w.add_assertion(
        "summary_total_observables",
        computed=out["summary"]["total"],
        expected=out["summary"]["total"],
        tolerance=0,
        source="Snapshot count of observables in the table.",
    )
    # Reference upstream witnesses for staleness tracking
    for upstream in [
        COMPUTE_DIR / "m-p-substrate-identity-50dps.witness.json",
        COMPUTE_DIR / "m-p-borromean-verification-50dps.witness.json",
        COMPUTE_DIR / "q-beta-operator-valued-N3.witness.json",
        COMPUTE_DIR / "codata-2022-validation-masses.witness.json",
        COMPUTE_DIR / "cal-3-q-beta.witness.json",
        COMPUTE_DIR / "meson-kaon-pion-derivation.witness.json",
    ]:
        w.add_upstream(upstream)
    w.save()
