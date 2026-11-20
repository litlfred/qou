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
import re
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
from qou_substrate import codata as _codata  # noqa: E402

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
#
# 2026-11-20: the frozen literal mpf("105.658397811") that stood here is
# replaced by a DERIVATION at the package's default (one-term proton) pin,
# read from qou_substrate.constants directly so no manifest rebinding can
# turn it into the muon tautology. Precision fix only: at the one-term pin
# the derived value rounds to the old literal (checked when this landed).
def _m_mu_pred_at(q_str: str) -> mpf:
    from qou_substrate.constants import vol_4_1_at as _vol
    with mp.workdps(max(70, mp.dps)):
        q = mpf(q_str)
        return mpf(str(M_E_MEV)) * _vol(70) / ((q - 1) / q) ** 2


def _proton_pin_strings() -> tuple[str, str]:
    """(one-term DEFAULT pin, two-term COMPARISON pin), both 50 digits."""
    from qou_substrate import constants as _qc
    return _qc.Q_50_DIGIT_STR, _qc.Q_PROTON_TWO_TERM_50_DIGIT_STR


_M_MU_PRED_PROTON_MEV = _m_mu_pred_at(_proton_pin_strings()[0])
_M_MU_PRED_SOURCE = (
    "DERIVED proton-anchored prediction m_e·Vol(4_1)/ℏ_q² at the package "
    "default one-term proton pin (m_p/m_e re-pin 2026-05-28); never read from "
    "the muon-flipped Borromean muon_check per bean tnjb / AGENTS.md "
    "§q₀-anchor STRICT rule 1"
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

# ── 1/α_EM — dimensionless gauge coupling ────────────────────────────
#
# 🛑 WHY THIS ROW DID NOT EXIST UNTIL 2026-09-07.
#
# Nothing excluded α_EM. It was simply never added, and the omission was
# load-bearing: at the proton pin with the derived Schwinger factor the
# framework predicts 1/α to **238×** its L2 target, which makes it the
# framework's SECOND-BEST prediction — better than every scored row except
# `m_K/m_π`, and four times better than `m_μ` (970×). A scorecard that omits
# its own second-best result because nobody added the row is not a scorecard.
#
# Adding it moves the headline from 1/5 to 1/6 scoreable, i.e. it makes the
# published ratio WORSE while making it more honest. That is the correct
# direction under the anti-fit rule, and it is the reason to add the row rather
# than a reason to hesitate.
#
# The reference is read from the registry (CODATA 2022), never hand-typed —
# see alpha_em_schwinger_ladder_probe.py, where the 2018 freeze this corpus
# carried was found to shift the residual by 2.2× its own size and flip its
# sign (#7069).
_ALPHA_INV_ENTRY = _codata.codata("inverse fine-structure constant")
OBSERVABLES["alpha_em_inv"] = (
    mpf(_ALPHA_INV_ENTRY.value_str),
    mpf(_ALPHA_INV_ENTRY.uncertainty_str),
    "validation (gauge coupling)",
    "qou_substrate.codata registry — 'inverse fine-structure constant', CODATA 2022",
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


CANONICAL_MARKOV_CONVENTION = "D"
"""The canonical Markov parameter convention: ``z = q³/(q²+1)``.

Fixed by the owner ruling of 2026-08-15, which excised convention C
(``z = √q/(q+1)``).  See AGENTS.md §"q₀ anchor convention" R1.
"""


#: Every ``markov_convention`` spelling measured in the corpus, as fixtures for
#: :func:`_normalise_markov_convention`.  Produced 2026-10-10 by scanning the
#: 3510 non-``_deprecated`` ``computations/**/*.witness.json``: **44 declare the
#: field (1.3 %), in 23 distinct spellings for 4 states.**  Kept here so a
#: change to the normaliser cannot silently reclassify one of them.
MARKOV_CONVENTION_SPELLINGS = {
    # -- D ----------------------------------------------------------------
    "D": "D",
    "D canonical": "D",
    "D (N = 2)": "D",
    "D (z = q^3/(q^2+1))": "D",
    "D  (z = q^3/(q^2+1))": "D",                      # note the double space
    "D (with C as control)": "D",
    "D canonical, C carried as control": "D",
    "D — z_D = q^3/(q^2+1), Wenzl level 2": "D",
    "D — the ruled functional, z_D = q^3/(q^2+1)": "D",
    "D (z = q^3/(q^2+1)); C measured for comparison": "D",
    "D (z = q^3/(q^2+1)) via closed_form_tau_M.markov_z": "D",
    # -- C ----------------------------------------------------------------
    "C": "C",
    # -- both compared; the stamp privileges neither ----------------------
    "both (C and D compared)": "both",
    "both, compared — D canonical": "both",
    "both admissible parameters are evaluated: z = q (level 1, the "
    "augmentation) and z_D = q^3/(q^2+1) (level 2, convention D)": "both",
    # -- no Markov parameter enters at all --------------------------------
    "not applicable": "n/a",
    "n/a (counit only)": "n/a",
    "n/a - no Markov parameter z enters": "n/a",
    "not applicable — no z enters this computation": "n/a",
    "convention-free — no z is specialised": "n/a",
    "convention-free — no Markov parameter is specialised": "n/a",
    "convention-free — z is symbolic; the D pin appears as one root": "n/a",
    "convention-free — the results hold for every z, and the floor contains "
    "no Markov parameter at all": "n/a",
}


def _normalise_markov_convention(raw) -> str:
    """Map a free-text ``markov_convention`` stamp to D / C / both / n/a.

    **Why this exists — a LATENT defect, not a live one.**  The check in
    :func:`_convention_frame_check` was

        matched = str(conv).strip().upper() == CANONICAL_MARKOV_CONVENTION

    an exact equality against the single character ``"D"``.  Measured
    2026-10-10 over the 3510 non-``_deprecated`` witnesses: **44 carry the
    field, in 23 distinct spellings, and only 13 are a bare** ``"D"``.  So ten
    of the eleven spellings that MEAN convention D — ``"D canonical"``,
    ``"D (z = q^3/(q^2+1))"``, ``"D (N = 2)"``, ``"D — the ruled functional,
    …"`` — classified as ``INHERITED_C``: a correctly-stamped *canonical*
    artifact reported as carrying the *excised* convention, on the dashboard
    AGENTS.md directs readers to quote for L2 status.

    It has never produced a wrong verdict, because the one cache this dashboard
    reads (``qbeta-ck-cache.witness.json``) carries the bare ``"C"`` — which
    the old check got right.  **Zero wrong verdicts is not a sound check**
    (detector-blindness taxonomy row 34): the moment ``qou-cds1`` lands and
    that cache is re-stamped with anything longer than one character, the
    dashboard calls the ruled result convention C.

    **Deliberately conservative.**  An unrecognised spelling returns
    ``"unparsed"`` — never ``"D"``, never ``"C"`` — so a new spelling fails
    *loudly* rather than being absorbed into either verdict.  ``"unparsed"`` is
    **not a clearance**: it means this function has nothing to say, in the same
    sense as the sibling consumer-control-arm audit's ``unmeasured``.
    """
    if raw is None:
        return "unparsed"
    s = " ".join(str(raw).split())           # collapse runs of whitespace
    for spelling, state in MARKOV_CONVENTION_SPELLINGS.items():
        if s == " ".join(spelling.split()):
            return state
    low = s.lower()
    # Rules below run only after the exact vocabulary misses.  Each is anchored
    # at the START of the stamp: a mention of C further along is in practice
    # "C carried as a control", which describes a D-framed computation.
    if low.startswith(("not applicable", "n/a", "convention-free",
                       "convention free")):
        return "n/a"
    if low.startswith("both"):
        return "both"
    if re.match(r"^d\b", low):
        return "D"
    if re.match(r"^c\b", low):
        return "C"
    return "unparsed"


def _convention_frame_check(cache: dict) -> dict:
    """Record the Markov convention a cached Q_β prediction was BUILT in.

    The convention sibling of :func:`_anchor_layer_check`, and it exists for
    the same reason: an inherited frame that is stamped one file upstream and
    **silent** at the point of publication.

    ``qbeta-ck-cache.witness.json`` carries ``data.markov_convention`` and a
    note saying C "was excised by owner ruling".  This dashboard consumed
    ``Q_pred_after_this_rung_MeV`` from it and published Q_β — and, through
    ``Q_beta_best``, the derived m_n and Δ_pn rows — with **no record of the
    frame at all**.  A reader of this witness could not tell, and AGENTS.md
    directs agents to quote this artifact for L2 status.

    Why this does NOT size the error, unlike the anchor check.  There, the
    D-frame counterpart of the number exists and the induced error is a
    derivative away.  Here it does not: ``qbeta_ck_cache.py`` **refuses to
    run** under D —

        if convention == "D":
            print(" REFUSING TO RUN -- convention D has no derived c_k ladder")
            raise SystemExit(2)

    — so the published Q_β is not merely stale, it is currently
    *unreproducible under the canonical convention*.  Any "induced convention
    error" figure emitted here would be manufactured.  The honest field is
    ``induced_error_ppb: None`` with the reason attached, and that is what
    this returns.  Naming a number we cannot compute is the failure mode this
    whole check exists to prevent.

    This does NOT re-derive the ladder.  That is tracked work with its own
    owner (bean ``qou-cds1``), and the 2026-08-30 bar-weight prune
    (``add3a7304a``) showed the obstruction is the *offset* — ``α = (z−1)h/2``
    mixes bar-weight −4 with weight 0 — so it is not a z-swap and must not be
    attempted from here.  This makes the frame loud; it does not change it.
    """
    data = cache.get("data", {}) or {}
    conv = data.get("markov_convention")
    if conv is None:
        return {
            "status": "unknown",
            "detail": ("cache carries no markov_convention stamp; the frame "
                       "cannot be verified from the artifact alone"),
            "canonical": CANONICAL_MARKOV_CONVENTION,
        }
    # The stamp is FREE TEXT -- 23 spellings for 4 states corpus-wide -- so it
    # is normalised rather than compared character-for-character against "D".
    # See `_normalise_markov_convention` for the measurement and for why an
    # unrecognised spelling is reported rather than absorbed into a verdict.
    state = _normalise_markov_convention(conv)
    matched = state == CANONICAL_MARKOV_CONVENTION
    status = {
        "D": "matched",
        "C": "INHERITED_C",
        "both": "both_conventions_compared",
        "n/a": "no_markov_parameter",
        "unparsed": "unparsed_stamp",
    }[state]
    return {
        "status": status,
        # `INHERITED_C` is the only status any consumer acts on, and only `C`
        # now reaches it. `unparsed_stamp` is NOT a clearance -- it says this
        # check has nothing to say about the frame.
        "cache_convention": conv,
        "cache_convention_normalised": state,
        "canonical": CANONICAL_MARKOV_CONVENTION,
        "cache_note": data.get("markov_convention_note"),
        # Deliberately None, not 0 and not a guess -- see the docstring.
        "induced_error_ppb": None,
        "induced_error_unquantifiable_reason": (
            None if matched else
            "qbeta_ck_cache.py raises SystemExit(2) under convention D "
            "('convention D has no derived c_k ladder'), so no D-frame "
            "counterpart of this prediction exists to difference against."
        ),
        "reproducible_under_canonical_convention": bool(matched),
        "tracked_by": None if matched else "qou-cds1",
    }


def _functional_admissibility_check() -> dict:
    """Is the functional the Q_β prediction rests on admissible under convention D?

    Why this exists, and why it is NOT the same as `_convention_frame_check`.

    That check asks whether the **`c_k` ladder** was built in convention C. This
    one asks a strictly stronger question about the thing the ladder sits on:
    whether the **base closed form's functional** is one convention D permits at
    all.

    It is not. `qbeta_published_form_is_the_inadmissible_z1_probe.py` (15/15,
    exact over ℚ(q), re-run and reproduced 2026-09-07) shows the published
    closed form `m_e·|q²−2q−1|(q+1)/(2q³)` is EXACTLY `|tr_M(Δ_S)|·E₀` at Markov
    parameter **`z = 1`** — the coordinate sum — and `ConventionDAdmissibleRoots.lean`
    (sorry-free) shows the only roots of the `(1³)` weight numerator are `z = q`
    (the augmentation) and `z_D = q³/(q²+1)`. `z = 1` is not one, and is not one
    AT the substrate pin either (the numerator vanishes at `z = 1` only at the
    supergolden ratio 1.4656, above `q₀ = 1.10998`).

    🟧 RULED 2026-09-08, RE-SCORED 2026-09-12 — read this before the rest.
    The owner ruled that `ε` **is** the Markov trace at `z_D`, and on
    2026-09-12 authorised the dashboard re-score onto it. So the `Q_β` row no
    longer scores the excluded `z = 1` cell, and this check's role has changed
    from *"the scored value rests on an excluded functional"* to *"here is the
    admissibility evidence, and which cell the ruling picked"*. It is kept
    rather than deleted because the `z = 1` identification is what makes the
    ruling legible, and because the re-score is guarded by a calibration that
    can fail — if it does, the old row is published and this check's note is
    again the live warning.

    The three cells at the proton pin: `z = 1` **+0.168 %** (retired,
    inadmissible), `z = q` **+12.470 %** (the augmentation — admissible, but
    the strictly finer one-row truncation, so NOT convention D), and
    **`z_D` −43.157 %** (RULED). Note the ruled cell is the FARTHEST of the
    three from CODATA. That is not a defect in the ruling: the choice turned on
    what `ε` means under D7, and ranking these cells by residual would be the
    selection-against-the-target AGENTS.md §"NO FITTING" forbids.

    🛑 COMPARE BASE TO BASE, and do not relate either to the 1279 ppb scored
    here. The 1279 ppb is the value AFTER the `c_k` ladder, which improves its
    own base by ~1312×; the 12.470 % is a base with no ladder on it, because no
    ladder has been derived on an admissible base — that is precisely what
    `qou-cds1` is. Dividing one by the other gives 97,498, a number that means
    nothing, and I wrote "~97×" for it before catching the slip. What the
    laddered value would become on an admissible base is **unknown**, and saying
    so is the honest statement.

    This does NOT decide which functional the framework should adopt — seven
    options are open and the choice is the owner's
    (`docs/audits/2026-09-05-qbeta-functional-decision-options.md`, `qou-99qc`).
    It records that the scored value rests on an excluded one, which is true
    under every one of those options.

    Everything is read from the committed probe witness; no figure is hardcoded
    here, so this cannot go stale against the probe the way a pasted number would.
    """
    path = COMPUTE_DIR / "qbeta" / "qbeta-published-form-is-the-inadmissible-z1.witness.json"
    try:
        w = json.loads(path.read_text())
    except Exception:
        return {"status": "NO-WITNESS", "witness": str(path.name)}
    solved = w.get("solved_markov_parameter", {})
    errs = w.get("err_pct_at_proton_pin", {})
    failed = [a["name"] for a in w.get("assertions", []) if not a.get("passed")]
    return {
        "status": "INADMISSIBLE_FUNCTIONAL" if not failed else "PROBE-FAILED",
        "scored_prediction_rests_on_z": solved.get("positive_branch"),
        "admissible_roots_under_D": solved.get("admissible_roots"),
        "err_pct_by_functional": errs,
        # RENAMED 2026-09-12 on owner instruction, from
        # `best_admissible_err_pct`, which read `errs["z=q (augmentation)"]`.
        # Two defects in one field. It named the augmentation — the owner ruled
        # for `z_D` (D7: convention D is the two-row truncation; the
        # augmentation is the strictly finer one-row truncation and is NOT D),
        # so a consumer of this witness took the wrong functional for the
        # adopted one. And "best" ranked the admissible cells BY RESIDUAL,
        # which is the selection-against-the-target AGENTS.md §"NO FITTING"
        # forbids — accuracy is a diagnostic here, never a tie-breaker. The
        # ruled cell is in fact 3.4609x FARTHER from CODATA than the
        # augmentation, so the old name asserted a ranking that points away
        # from the ruling. Both cells stay visible in
        # `err_pct_by_functional`; only the singled-out one changes.
        "ruled_cell_err_pct": errs.get("z=z_D (Markov, convention D)"),
        "ruled_cell_markov_parameter": "z_D = q^3/(q^2+1)",
        "augmentation_err_pct_for_comparison": errs.get("z=q (augmentation)"),
        "source_witness": path.name,
        "lean": "QOU.QBeta.ConventionDAdmissibleRoots (sorry-free)",
        "probe_assertions_failed": failed or None,
        "note": (
            "STRONGER THAN THE CONVENTION-FRAME NOTE, AND SEPARATE FROM IT. That "
            "note says the c_k LADDER is convention-C. This says the BASE the "
            "ladder sits on uses a functional convention D provably excludes: the "
            "published closed form solves to z = 1, which is not a root of the "
            "(1^3) weight numerator. The best ADMISSIBLE cell is +12.47% (the "
            "augmentation on Delta_S) against the published 0.16776%, and the "
            "RULED cell is -43.157% -- the ruled cell is the FARTHEST of the "
            "three from CODATA, which is the anti-fit directive working as "
            "designed, not a defect in the ruling. WHICH FUNCTIONAL TO ADOPT IS "
            "NO LONGER OPEN: the owner ruled 2026-09-08 that eps is the Markov "
            "trace at z_D = q^3/(q^2+1) (convention D, two-row truncation, D7), "
            "and authorised the dashboard re-score on 2026-09-12 with its price "
            "measured first (qbeta/qbeta-zd-rescore-price.witness.json). The "
            "Q_beta row is scored on the ruled base from that date, so this "
            "field records the admissibility EVIDENCE rather than a live defect "
            "-- it becomes the live warning again only if the re-score's "
            "calibration against this witness fails. Do NOT relate any cell to "
            "the ~1279 ppb the retired row used to show: that was post-ladder, "
            "and no ladder has been derived on an admissible base (qou-cds1, "
            "blocked on the phase qou-pdix), so what the ruled base would become "
            "with one is UNKNOWN. Applies to the m_n and Delta_pn rows, which "
            "are derived from this value -- and unlike the convention note, it is "
            "written ONTO those rows rather than cross-referenced from this one."
        ),
    }


def _qbeta_ruled_base() -> dict:
    """Q_β on the RULED base: the Markov trace at `z_D = q³/(q²+1)`.

    OWNER RULING 2026-09-08, and OWNER AUTHORISATION 2026-09-12 to score it.
    `ε` in `Q_β = |ε(Δ)|·E₀` is the Markov trace at `z_D` (convention D, the
    two-row truncation — D7). Until 2026-09-12 this dashboard scored the
    **retired `z = 1`** cell instead, which is the coordinate sum and is
    provably NOT an admissible root under D
    (`ConventionDAdmissibleRoots.lean`, sorry-free). The owner authorised the
    re-score with the price measured in
    `qbeta-zd-rescore-price.witness.json`: it degrades the `Q_β` / `m_n` /
    `Δ_pn` rows by roughly 5–7 orders of magnitude.

    DERIVED FROM q₀, NOT INVERTED FROM CODATA. The tempting implementation is
    to read the probe witness's recorded `-43.157175 %` residual and invert it
    (`pred = Q_exp·(1+err)`), which is arithmetically exact and optically
    circular: the row's residual would then be a pass-through of a number that
    was itself computed against CODATA. This instead evaluates the functional

        tr_M(Δ_S)(z) = q²/2 − q·z − 1 + z/q + 1/(2q²)      (affine trace)
        E₀           = m_e / (q(q−1))
        Q_β(z)       = |tr_M(Δ_S)(z)| · E₀

    at `z = z_D` from `q₀` alone — no CODATA anywhere in the value — and then
    CALIBRATES against the committed probe witness. If the calibration misses,
    `calibrated` is False and the caller keeps the old row rather than
    publishing a number my arithmetic invented.

    🛑 THE RESULT IS A BASE, WITH ZERO `c_k` RUNGS, AND THAT IS THE WHOLE
    CAVEAT. No ladder has been derived on an admissible base — that is exactly
    what `qou-cds1` is, blocked on the phase `qou-pdix`. On the retired `z = 1`
    base the five rungs bought 1 677 569 → 37.7 ppb, about 4.5 orders. So this
    row is NOT "convention D's accuracy"; it is the ruled base before any
    ladder exists, and the owner authorised a SECOND re-score once `qou-pdix`
    closes (bean `qou-iagg`). Quoting it as D's accuracy repeats the
    mislabelling bean `qou-99qc` already had to retract once.
    """
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    sys.path.insert(0, str(COMPUTE_DIR / "qbeta"))
    from qbeta_e0 import canonical as _e0_canonical, order_zero as _e0_order_zero
    q = mpf(Q_50_DIGIT_STR)
    z_D = q ** 3 / (q ** 2 + 1)
    # ── ELEMENT: THE gamma-gamma-SELECTED NUCLEON WORD (bean qou-wfvl) ────────
    # MIGRATED 2026-09-12. This scored `Delta_S`, the short normal-form element,
    # whose provenance is the census / NF construction. The owner ruled the SAME
    # DAY as the eps ruling (`qou-ales`, 2026-09-08): "All selection of great
    # words should be done through gamma gamma production and the semi-definite
    # product solutions at q0. Shouldn't use census." So `Delta_S` was not an
    # admissible element and the functional had been migrated without it.
    #
    # THE CHAIN, every link on main or committed -- NOT depending on the open
    # sibling PR #7212:
    #   1. `QOU.Mass.GammaGammaWordSelection.vertex i = [(i, +), (i+1, -)]`, so
    #      every gamma-gamma word has a NEGATIVE second letter. The gen-grouped
    #      core begins `sigma_0 sigma_0` (positive second letter) and is therefore
    #      excluded; the interleaved core `(sigma_0 sigma_1^-1)^3` is three
    #      vertices and is admitted.
    #   2. `qbeta-option-e-required-level.witness.json` (on main, q0_anchor
    #      proton, BOTH admissible parameters evaluated) carries `tr_conv_D` for
    #      all four candidate elements.
    # PR #7212 proves (1) as an explicit Lean lemma; it is OPEN, so it is cited
    # as corroboration, not as the authority. The authority is the ruling plus
    # `vertex`'s definition on main.
    #
    # NOT CHOSEN BY RESIDUAL, and that must stay true if a later agent revisits
    # this: the gamma-gamma-selected element happens to be 2.5x closer to CODATA
    # than `Delta_S`, but it is selected because it is DERIVED. Were it further
    # away it would still be the right element. Ranking candidates by residual is
    # the selection-against-the-target AGENTS.md forbids.
    _CENSUS = json.loads(
        (COMPUTE_DIR / "qbeta" / "qbeta-option-e-required-level.witness.json"
         ).read_text())
    _cand = _CENSUS["data"]["per_candidate"]
    _ELEMENT = "nuc11_interleaved"
    tr_M = mpf(_cand[_ELEMENT]["tr_conv_D"])
    # tr^{z_D}(Delta_S) = h^2/2 - z_D*h exactly (h = q - 1/q), kept so the
    # superseded cell stays reproducible and the delta is measurable.
    _tr_M_delta_S = q ** 2 / 2 - q * z_D - 1 + z_D / q + 1 / (2 * q ** 2)
    # E_0 THROUGH THE UNIFIED MODULE (owner instruction 2026-09-12). It had two
    # live forms differing by 1/(1 - hbar_q^2) = +0.9915 %, with no signal at
    # either call site; qbeta_e0 is now the single definition and the
    # tower-summed form is canonical per the 2026-09-03 full-tower ruling.
    # NOTE the tower SERIES is itself an open derivation (bean qou-y3bm) --
    # canonical by ruling, not by proof.
    pred = abs(tr_M) * _e0_canonical(q=q, m_e=M_E_MEV)
    pred_order_zero = abs(tr_M) * _e0_order_zero(q=q, m_e=M_E_MEV)

    # CALIBRATE THE TRACE, NOT THE E_0 CHOICE -- and this distinction is not
    # cosmetic: it was found by the guard firing. The probe witness's recorded
    # cell (-43.157175 %) was computed with the ORDER-ZERO E_0, so when E_0 was
    # unified onto the tower-summed form (+0.9915 %) the comparison missed by
    # ~0.56 points, `calibrated` went False, and the producer correctly refused
    # to publish -- silently reverting the whole row to the retired z = 1 cell.
    # The guard did its job; the calibration was asking the wrong question.
    # So: calibrate the TRACE against the recorded cell at the E_0 that cell was
    # computed with, then publish at the CANONICAL E_0. One check per claim.
    adm = _functional_admissibility_check()
    # Calibrate against the CENSUS witness's own recorded pct for the element
    # actually scored -- not against the Delta_S cell, which is a different
    # element. Both are at order-zero E_0, so the trace/E_0 separation below
    # still holds.
    recorded = _cand[_ELEMENT]["pct_D"]
    err_pct = (pred - Q_BETA_MEV) / Q_BETA_MEV * 100
    err_pct_order_zero = (pred_order_zero - Q_BETA_MEV) / Q_BETA_MEV * 100
    calibrated = False
    if recorded is not None:
        calibrated = abs(err_pct_order_zero - mpf(str(recorded))) < mpf("1e-4")
    return {
        "Q_beta_MeV": fmt(pred),
        "markov_parameter": "z_D = q^3/(q^2+1)",
        "E0_form": "tower_summed (canonical, qbeta_e0.canonical)",
        "E0_MeV": fmt(_e0_canonical(q=q, m_e=M_E_MEV)),
        "E0_tower_series_is_open": "qou-y3bm -- canonical by the 2026-09-03 "
                                   "full-tower ruling, series not derived",
        "Q_beta_MeV_at_order_zero_E0": fmt(pred_order_zero),
        "E0_choice_moves_row_pct": fmt(
            (pred / pred_order_zero - 1) * 100, 6),
        "err_pct": fmt(err_pct),
        "err_pct_at_order_zero_E0": fmt(err_pct_order_zero),
        "recorded_err_pct_in_probe_witness": recorded,
        "calibration_compares": "err_pct_at_order_zero_E0 vs the recorded cell -- "
                                "the cell was computed at order-zero E_0, so "
                                "calibrating the published (tower-E_0) value "
                                "against it would conflate the trace with the "
                                "E_0 choice and fail by ~0.56 points",
        "calibrated_against_probe_witness": bool(calibrated),
        "ck_rungs_applied": 0,
        "ladder_on_admissible_base_exists": False,
        "_pred": pred,
        "ruling": "owner 2026-09-08 (eps := Markov trace at z_D, D7); "
                  "re-score authorised 2026-09-12",
        "price_witness": "qbeta/qbeta-zd-rescore-price.witness.json",
        "second_rescore_due_after": "qou-pdix (phase) -> qou-cds1 (ladder); "
                                    "bean qou-iagg",
        # 🛑 THE ELEMENT IS RULED IN 6 OF ITS 11 LETTERS, NOT IN ALL OF THEM.
        # (This comment said "THE ELEMENT IS NOT RULED ... This row uses
        # delta_S" until 2026-09-13. That was the pre-migration text: 573b2ece24
        # had already moved the scored element to `nuc11_interleaved` and the row
        # had already improved 2.55x, 4.259e+8 -> 1.668e+8 ppb, while this block
        # still told a reader the row was delta_S at -43.157 %. PR #7212, cited
        # below as OPEN, merged as 85ffb930e2. Corrected, not re-argued.)
        #
        # What IS ruled: the 2026-09-08 owner ruling fixes `eps` (the Markov
        # trace at z_D), and the gamma-gamma word-selection ruling (qou-ales)
        # selects the nucleon ORDERING -- interleaved over gen-grouped.
        # The candidate census (witness qbeta-option-e-required-level) carries
        # FOUR elements, all undershooting at level 2 = z_D, at order-zero E_0:
        #     delta_S short NF        -43.157 %   <- superseded
        #     nuc9 build_nucleon_nf   -30.936 %
        #     nuc11 interleaved       -17.496 %   <- what this row scores
        #     nuc11 gen-grouped       -15.451 %
        # (on the canonical tower-summed E_0 the scored cell is -16.678 %.)
        #
        # What is NOT ruled, and it is a PARITY bound rather than an opinion.
        # `nuc11_interleaved` is ELEVEN letters, read off its construction in
        # qbeta_delta_candidate_census_probe.py: nuc9 = 3 x (sigma_0, sigma_1) core
        # = 6, + a 3-letter quark block = 9, + 2 sigma_0 gluon letters = 11.
        # Every gamma-gamma word has EVEN length, being a concatenation of
        # 2-letter vertices (`gammaGamma_length_even`, sorry-free). 11 is odd, so
        # nuc11_interleaved is not a gamma-gamma word and the ruling cannot have
        # selected it whole:
        #     core   6 letters  gamma-gamma-reachable (three vertices)
        #     quark  3 letters  NOT -- odd
        #     gluon  2 letters  NOT -- even, but both letters positive, and it
        #                       follows an odd block so no vertex boundary aligns
        # So the element is 6/11 ruling-derived and 5/11 census-derived, which
        # matters because qou-ales is "shouldn't use census". Measured and
        # surfaced to the owner on bean qou-99qc (2026-09-12); the counts are
        # emitted below as `element_ruled_letters` / `element_census_letters`.
        # `element_is_ruled` WAS left True DELIBERATELY -- it is an owner-facing
        # provenance label and re-meaning it is the owner's call, not an agent's.
        #
        # 🟧 CHANGED TO False 2026-10-11, AT THE OWNER'S REQUEST (ofri, in
        # session, 2026-10-11T07:22Z: draft the fix for review). The boolean now
        # answers "is the WHOLE scored element ruled?", and the answer is no:
        #   * 6/11 letters (the core) are gamma-gamma-reachable, and even that
        #     selection is CONDITIONAL -- on confinement reading 3, which is
        #     provisional ("try ... 3 for now", qou-ales), and on excluding the
        #     empty word, which reading 3 otherwise selects
        #     (GammaGammaFrobeniusSelection.frobeniusSelected_borromean /
        #     frobeniusSelected_nil, sorry-free);
        #   * 5/11 letters are CHOSEN: the 3-letter quark template and the
        #     sigma_0 sigma_0 gluon pair, whose "ILP-derived" citation is dead
        #     and which fails reading 3 (bean qou-99qc).
        # Evidence: word-provenance audit
        # (mass-endomorphism/klambda/word-provenance.md, 2026-10-11).
        # `element_ruled_status` carries the partial verdict as a string.
        # Consumer check at the change: no code reads `element_is_ruled`; the
        # only other mentions are prose in
        # qbeta_scored_element_is_not_gamma_gamma_produced_probe.py (and its
        # witness), which warns against reading True as "gamma-gamma-produced".
        #
        # So the figure is scoped twice over, not once: no ladder (above), AND
        # an element whose 5 free letters have no derived constraint. Do not read
        # it as the framework's Q_beta.
        "element_scored": _ELEMENT + " (gamma-gamma-selected nucleon word)",
        "element_is_ruled": False,
        # Corpus-derived cross-reference (2026-11-20): the CONTENT BLOCKS score a
        # DIFFERENT element on the same ruled base. `mass-comparison-table.md:33`
        # and `neutron-qvalue-symbolic.md:53` state Q_beta^{z_D} =
        # |h^2/2 - h z_D| E0_tower = 0.4491 MeV, i.e. element Delta_S (commit
        # 72a589b57b), while this row scores nuc11_interleaved (0.6519 MeV).
        # Both are on main at once. Recorded, NOT resolved: which element is
        # canonical is an owner decision (bean qou-99qc), and choosing by
        # residual is forbidden.
        "content_blocks_element": "delta_S (0.4491 MeV, tower E0; mass-comparison-table.md, neutron-qvalue-symbolic.md)",
        "element_conflict_open": "qou-99qc",
        "element_ruled_status": "partial",
        "element_ruled_status_rationale": (
            "6/11 letters (the core (sigma_0 sigma_1^-1)^3) are gamma-gamma-"
            "reachable, and even those are conditional on the provisional "
            "confinement reading 3 and on excluding the empty word "
            "(frobeniusSelected_borromean / frobeniusSelected_nil); the other "
            "5 letters (3-letter quark template + sigma_0 sigma_0 gluon pair) "
            "are chosen -- the gluon pair's 'ILP-derived' citation is dead and "
            "it fails reading 3 (qou-99qc). Source: word-provenance audit "
            "2026-10-11; False set at owner request 2026-10-11"
        ),
        # The boolean cannot express a partial selection; these two can, and
        # they are what the parity bound in the comment above measures. Kept
        # ALONGSIDE the boolean so no consumer breaks. 6 + 5 = 11 letters.
        "element_ruled_letters": 6,
        "element_census_letters": 5,
        "element_ruled_scope": (
            "the 6-letter core (sigma_0, sigma_1)^3 = three gamma-gamma "
            "vertices. The 3-letter quark block is odd and the 2-letter gluon "
            "pair has both letters positive, so neither is gamma-gamma "
            "reachable -- gammaGamma_length_even, sorry-free. qou-ales says "
            "'shouldn't use census' and 5 of 11 letters are still census-"
            "derived; those 5 have no derived constraint and are where a "
            "closing Delta would have to come from (bean qou-99qc, 2026-09-12)"
        ),
        "element_authority": "owner gamma-gamma ruling qou-ales 2026-09-08 + "
                             "GammaGammaWordSelection.vertex on main (a "
                             "gamma-gamma word's 2nd letter is negative, which "
                             "excludes the gen-grouped core)",
        "element_superseded": "delta_S (short NF) -- census-derived, "
                              "inadmissible under the gamma-gamma ruling; its "
                              "cell was -43.157175%",
        "Q_beta_MeV_on_superseded_delta_S": fmt(
            abs(_tr_M_delta_S) * _e0_canonical(q=q, m_e=M_E_MEV)),
        "element_ordering_proof_open_in": "PR #7212 (Lean lemma for the "
                                          "2nd-letter exclusion; corroboration, "
                                          "not the authority)",
        "element_candidates_level2_pct": {
            "delta_S short NF": "-43.157",
            "nuc9 build_nucleon_nf": "-30.936",
            "nuc11 interleaved (gamma-gamma-selected per PR #7212, OPEN)": "-17.496",
            "nuc11 gen-grouped": "-15.451",
        },
        "element_tracked_by": "qou-99qc (the Delta/eps fork, open); "
                              "PR #7212 narrows the nucleon-word branch",
    }


def _inherited_qbeta_scope(conv: dict, adm: dict,
                           ruled: dict | None = None) -> str | None:
    """The scope `m_n` and `Δ_pn` inherit from `Q_β`, written onto their own rows.

    `m_n = m_p + Q_β + m_e` and `Δ_pn = Q_β + m_e`, so every caveat on `Q_β`
    is a caveat on both. The `Q_β` row's convention note already says so — but
    it says so *on the `Q_β` row*, and a reader who lands on `m_n` sees a bare
    176.7× with nothing attached. That is the failure mode this corpus keeps
    recording under a different name each time: a correction applied at one
    site while the sites that inherit it stay clean.

    Returns None when neither scope applies, so a future state in which the
    ladder is re-derived under D on an admissible functional silently drops
    the note rather than leaving a stale one.

    **That promise did not hold, and the guard below is the repair.** The C
    note was gated on ``conv["status"] == "INHERITED_C"``, which is a property
    of ``qbeta-ck-cache.witness.json`` and not of the value this row scores.
    The cache is a convention-C artifact *by construction* and
    ``qbeta_ck_cache.py`` raises ``SystemExit(2)`` under D, so that status can
    never become anything else — the note could never drop, whatever happened
    downstream. Meanwhile the 2026-09-12 re-score moved ``Q_pred`` onto the
    ruled ``z_D`` base, so the committed witness carried both notes appended
    and they contradict each other: "the Q_beta term **was built in Markov
    convention C** … **not reproducible under the canonical convention**"
    beside "the Q_beta term **is now** |tr_M(Delta_S)(z_D)|*E0 at
    z_D = q^3/(q^2+1)". The second is current; the first is superseded and, on
    this row, false in both of its operative clauses — the value is built at
    z_D, which *is* the canonical convention.

    So the C note now fires only when the row does **not** rest on the ruled
    base, i.e. when the scored value genuinely came from the C cache. That is
    the same condition that selects ``Q_pred`` in the caller, which is what
    makes it the right one: it keys on the provenance of the number rather
    than on the convention of a file the number may no longer touch. What
    remains true under the ruled base — that no ``c_k`` ladder exists on an
    admissible functional — is already stated, correctly and in full, by the
    RULED-base note. Bean ``qou-zzwm``.
    """
    parts = []
    _on_ruled_base = bool(ruled is not None
                          and ruled.get("calibrated_against_probe_witness"))
    if conv.get("status") == "INHERITED_C" and not _on_ruled_base:
        parts.append(
            f"INHERITS THE Q_beta CONVENTION FRAME: this value is "
            f"m_p(substrate) + Q_beta + m_e, and the Q_beta term was built in "
            f"Markov convention {conv.get('cache_convention')}, excised by the "
            f"owner ruling of 2026-08-15 in favour of {conv.get('canonical')}. "
            f"Not reproducible under the canonical convention "
            f"(bean {conv.get('tracked_by')})."
        )
    if _on_ruled_base:
        # Re-scored 2026-09-12 on owner authorisation. The note that stood here
        # said the miss "understates the gap by an amount that is NOT yet
        # quantifiable" -- true while the row was on the retired cell, and now
        # the wrong statement: the row IS the ruled cell, and what is unknown
        # has moved to the other side (what a ladder would recover).
        parts.append(
            f"INHERITS THE RULED Q_beta BASE: this value is "
            f"m_p(substrate) + Q_beta + m_e, and the Q_beta term is now "
            f"|tr_M(Delta_S)(z_D)|*E0 at z_D = q^3/(q^2+1) -- the functional the "
            f"owner ruled on 2026-09-08 (convention D, two-row truncation, D7), "
            f"re-scored here on the 2026-09-12 authorisation. IT CARRIES ZERO "
            f"c_k RUNGS: no ladder has been derived on an admissible base "
            f"(qou-cds1, blocked on the phase qou-pdix), and on the retired "
            f"z = 1 base the five rungs bought ~4.5 orders. So this row is NOT "
            f"convention D's accuracy -- it is the ruled base before any ladder "
            f"exists, and a second re-score is authorised once qou-pdix closes "
            f"(bean qou-iagg). Price of the move: "
            f"{ruled.get('price_witness')}."
        )
    elif adm.get("status") == "INADMISSIBLE_FUNCTIONAL":
        parts.append(
            f"INHERITS THE Q_beta FUNCTIONAL ADMISSIBILITY DEFECT: the Q_beta "
            f"term's base closed form solves to Markov parameter "
            f"z = {adm.get('scored_prediction_rests_on_z')}, which convention D "
            f"excludes (admissible roots: "
            f"{', '.join(adm.get('admissible_roots_under_D') or [])}; "
            f"ConventionDAdmissibleRoots.lean, sorry-free). The RULED cell is "
            f"{adm.get('ruled_cell_err_pct')}% on Delta_S against the published "
            f"base of 0.16776%. The re-score onto the ruled base did not "
            f"calibrate, so this row still inherits the excluded functional -- "
            f"see the Q_beta row's note and fix the calibration."
        )
    return "  ".join(parts) if parts else None


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
    qbeta_convention = _convention_frame_check(ck_cache)
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
            Q_pred_laddered_z1 = mpf(Q_pred_str)
            # ── RE-SCORE ONTO THE RULED BASE (owner 2026-09-08 + 2026-09-12) ──
            # Until 2026-09-12 `Q_pred` here — and, through `Q_beta_best`, the
            # m_n and Delta_pn rows — was the LADDERED value on the retired
            # `z = 1` cell, a functional convention D provably excludes. The
            # owner ruled the functional (`eps` := Markov trace at `z_D`) and
            # then authorised this re-score with its price measured first
            # (`qbeta-zd-rescore-price.witness.json`): ~5-7 orders worse on all
            # three rows. Accuracy is a diagnostic here, not a tie-breaker, so a
            # worse number on the ruled base is the correct publication.
            #
            # The laddered figure is NOT deleted — it is recorded on the row as
            # the retired cell, because a reader needs to see what moved and by
            # how much. Dropping it would make this look like a regression of
            # unknown origin.
            _ruled = _qbeta_ruled_base()
            if _ruled["calibrated_against_probe_witness"]:
                Q_pred = _ruled["_pred"]
            else:
                # The functional evaluated here does not reproduce the committed
                # probe witness's own cell. Publish the old row rather than a
                # number this producer's arithmetic invented, and say so.
                Q_pred = Q_pred_laddered_z1
            Q_beta_best = Q_pred
            _anchor_note = ""
            _conv_note = ""
            # Same repair as in `_inherited_qbeta_scope`: this note must key on
            # whether the SCORED VALUE came from the C cache, not on the cache's
            # own convention. Two lines up, `Q_pred` is the ruled `z_D` base
            # whenever the calibration holds — built in convention D — so firing
            # the note on the cache's status printed "this prediction was built
            # in Markov convention C … UNREPRODUCIBLE under the canonical
            # convention" over a number built at `z_D = q³/(q²+1)`, which IS the
            # canonical convention. Both clauses were false of the published row.
            # What is still true (no `c_k` ladder on an admissible base) is said
            # by `_adm_note` / the ruled-base note below. Bean `qou-zzwm`.
            if (qbeta_convention.get("status") == "INHERITED_C"
                    and not _ruled["calibrated_against_probe_witness"]):
                _conv_note = (
                    f" ⚠ CONVENTION FRAME: this prediction was built in Markov "
                    f"convention {qbeta_convention['cache_convention']}, which "
                    f"the owner ruling of 2026-08-15 EXCISED in favour of "
                    f"{qbeta_convention['canonical']} "
                    f"(z = q³/(q²+1)). The induced error is NOT quantified here "
                    f"and that is deliberate: qbeta_ck_cache.py raises "
                    f"SystemExit(2) under D, so no D-frame counterpart exists to "
                    f"difference against — this figure is currently "
                    f"UNREPRODUCIBLE under the canonical convention. Re-derivation "
                    f"is tracked as bean qou-cds1 and is not a z-swap (the "
                    f"2026-08-30 bar-weight prune showed the obstruction is the "
                    f"offset, not z). Applies to the m_n and Δ_pn rows too, which "
                    f"are derived from this value."
                )
            _adm = _functional_admissibility_check()
            _adm_note = ""
            if _ruled["calibrated_against_probe_witness"]:
                _adm_note = (
                    f" 🟧 SCORED ON THE RULED BASE, ZERO c_k RUNGS. The owner "
                    f"ruled 2026-09-08 that eps in Q_beta = |eps(Delta)|*E0 is the "
                    f"Markov trace at z_D = q^3/(q^2+1) (convention D, the two-row "
                    f"truncation -- D7), and authorised this re-score 2026-09-12 "
                    f"with the price measured first "
                    f"({_ruled['price_witness']}). This row is now "
                    f"|tr_M(Delta_S)(z_D)|*E0 evaluated from q0 alone -- no CODATA "
                    f"in the value -- and calibrated against "
                    f"{_adm.get('source_witness')} (recorded cell "
                    f"{_ruled['recorded_err_pct_in_probe_witness']}%). "
                    f"🛑 IT IS A BASE: no c_k ladder has been derived on an "
                    f"admissible base (qou-cds1, blocked on the phase qou-pdix), so "
                    f"do NOT read this as convention D's accuracy. WHAT IT REPLACED, "
                    f"for comparison only: the laddered value on the RETIRED z = 1 "
                    f"cell was {fmt(Q_pred_laddered_z1, 12)} MeV (err 0.16776% base, "
                    f"~1279 ppb after five rungs) -- z = 1 is the coordinate sum and "
                    f"is provably NOT an admissible root under D (roots: "
                    f"{', '.join(_adm.get('admissible_roots_under_D') or [])}; "
                    f"ConventionDAdmissibleRoots.lean, sorry-free). On the retired "
                    f"base the ladder bought ~4.5 orders, so a z_D ladder could move "
                    f"this row a long way; a SECOND re-score is authorised once "
                    f"qou-pdix closes (bean qou-iagg). The ruled cell is also "
                    f"3.4609x farther from CODATA than the augmentation (z = q), "
                    f"which is admissible but is the finer one-row truncation and is "
                    f"NOT convention D -- recorded because a referee will notice, "
                    f"not as an argument: ranking cells by residual is the "
                    f"selection-against-the-target the anti-fit directive forbids. "
                    f"🛑 AND THE ELEMENT IS RULED IN "
                    f"{_ruled['element_ruled_letters']} OF ITS "
                    f"{_ruled['element_ruled_letters'] + _ruled['element_census_letters']} "
                    f"LETTERS, NOT IN ALL OF THEM: this row scores Delta = "
                    f"{_ruled['element_scored']}, selected over nuc11 gen-grouped "
                    f"by the gamma-gamma word-selection ruling (qou-ales). But "
                    f"that word is ELEVEN letters and every gamma-gamma word has "
                    f"EVEN length (gammaGamma_length_even, sorry-free), so the "
                    f"ruling reaches only the 6-letter core and provably cannot "
                    f"reach the 3-letter quark block (odd) or the 2-letter gluon "
                    f"pair (both letters positive). 5 of 11 letters are still "
                    f"census-derived, which is what qou-ales asks not to use. The "
                    f"corpus carries FOUR candidate Delta, all undershooting at "
                    f"z_D (order-zero E_0) -- delta_S -43.157%, nuc9 -30.936%, "
                    f"nuc11 interleaved -17.496% (this row, -16.678% on the "
                    f"canonical tower E_0), nuc11 gen-grouped -15.451%. So the "
                    f"figure is scoped TWICE: no ladder, and 5 element letters "
                    f"with no derived constraint ({_ruled['element_tracked_by']})."
                )
            elif _adm.get("status") == "INADMISSIBLE_FUNCTIONAL":
                _adm_note = (
                    f" 🛑 RE-SCORE ONTO THE RULED BASE DID NOT CALIBRATE, so "
                    f"this row is still the RETIRED z = 1 cell. The functional "
                    f"evaluated by _qbeta_ruled_base() gave "
                    f"{_ruled['err_pct']}% against the committed probe witness's "
                    f"{_ruled['recorded_err_pct_in_probe_witness']}%, so the "
                    f"producer published the old value rather than a number its own "
                    f"arithmetic invented. The base closed form scored here solves "
                    f"to Markov parameter z = "
                    f"{_adm['scored_prediction_rests_on_z']}, which is NOT one of "
                    f"the admissible roots under convention D "
                    f"({', '.join(_adm['admissible_roots_under_D'])}) — "
                    f"ConventionDAdmissibleRoots.lean, sorry-free, and "
                    f"{_adm['source_witness']} (15/15, exact over Q(q)). The RULED "
                    f"cell is {_adm['ruled_cell_err_pct']}% on Delta_S. Fix the "
                    f"calibration; do not read this row as the ruled position."
                )
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
                + _anchor_note + _conv_note + _adm_note,
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
        # The Q_beta row's convention caveat says "applies to the m_n and
        # Delta_pn rows too" -- but it is written on the Q_beta row, and a
        # reader of THESE rows sees nothing. That is the "fixed in one place,
        # survives in the others" failure this corpus keeps recording. Write
        # the inherited scope onto the derived rows themselves.
        _inherited = _inherited_qbeta_scope(qbeta_convention,
                                            _functional_admissibility_check(),
                                            _qbeta_ruled_base())
        for _obs, _val in (("m_n", m_n_path_c), ("Delta_pn", delta_pn_path_c)):
            _r = _row_for(_obs, _val, path_c_source)
            if _inherited:
                _r["note"] = _inherited
            rows.append(_r)
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

    # ── 1/α_EM — the derived Schwinger ladder at the proton pin ──────
    #
    # Read as a VALUE from the producer's witness, not back-computed from a
    # published residual. See the OBSERVABLES entry above for why this row
    # did not exist until 2026-09-07 and why adding it makes the headline
    # ratio worse.
    #
    # Scope, carried on the row so it cannot be quoted bare: the construction
    # is conditional on three unproved classes (ArchimedeanLimit,
    # BlochSuslinUniqueness, BringZeroModeBlochClass), so this is a
    # conditional prediction — the same tier caveat `m_K/m_π` carries for its
    # α_em input. The Schwinger factor itself is DERIVED (RT phase 3), not a
    # fitted knob.
    try:
        _alpha_w = load_witness("alpha-em-schwinger-ladder.witness.json")
        _alpha_inv_pred = _alpha_w["data"]["ladder_proton"].get("form_B_alpha_inv")
    except Exception:
        _alpha_inv_pred = None
    if _alpha_inv_pred is not None:
        _row = _row_for(
            "alpha_em_inv", mpf(str(_alpha_inv_pred)),
            "alpha-em-schwinger-ladder.witness.json :: data.ladder_proton.form_B_alpha_inv "
            "(cubic form with the derived Schwinger factor (1-h^2 alpha), proton pin)",
        )
        _row["note"] = (
            "CONDITIONAL on three unproved classes (ArchimedeanLimit, "
            "BlochSuslinUniqueness, BringZeroModeBlochClass) — a conditional "
            "prediction, not a proved derivation. The Schwinger factor is NOT "
            "FITTED and this is measured, not asserted: parametrising it as "
            "(1 - c*h^2*alpha), the c that hits CODATA exactly is 0.7312340272 "
            "and the 1-sigma window is [0.61846303, 0.84400502], so the "
            "published c = 1 lies OUTSIDE it, at 2.383 sigma -- a fitter would "
            "have taken 0.731. But it is NOT DERIVED either: the exact "
            "vertex-moment check (docs/audits/2026-07-14-alpha-em-phase3-"
            "schwinger-coefficient-exact-check.md) gives +0.1281 against the "
            "claimed -h^2 = -0.0437, wrong order and wrong sign, ratio -2.93, "
            "and recommends the tier 'structurally-motivated / "
            "empirically-anchored'. That is the honest label. Second-best scoreable row: 238x, against 970x (m_mu) and "
            "152-177x (the Q_beta trio). NOTE the residual's SIGN depends on the "
            "CODATA edition (the 2018->2022 shift is 2.2x the residual); the "
            "reference is read from the registry so the edition is not a choice."
        )
        rows.append(_row)
    else:
        rows.append({"obs": "alpha_em_inv", "status": "NO-WITNESS"})

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

    # ── m_K/m_π — derived closure (#1442 + #1448) ────────────────────
    # Closed form: m_K²/m_π² = [3]_q·[4]_q + (α_em/π)·(1 + log(1+ℏ_q))
    # - strong sector [3]_q·[4]_q: Lean-proved q-Clebsch–Gordan fusion
    #   (prop:meson-qcg-fusion-identity, QOU.BraidKnot.meson_qCG_3x4)
    # - EM sinh-channel: the FULL series `1 + log(1+ℏ_q)`.
    #
    #   🛑 DE-FITTED 2026-08-22 — this line used to carry the two-term
    #   truncation `(3q²−1)/(2q²)`, which is exactly `1 + ℏ_q − ℏ_q²/2`
    #   (Lean ring identity QOU.BraidKnot.meson_EM_closed_form — still
    #   true, and still proved; it is the IDENTIFICATION of that
    #   truncation as the physical factor that was wrong). The owner
    #   directive of 2026-08-09 already ruled the full series canonical
    #   (docs/precision-goals.md §L2) but no producer was updated, so
    #   the truncation stayed live here for 13 days.
    #
    #   Why the truncation is a fit, measured at 70 dps: the error as a
    #   function of stopping order is 479.1 / **23.4** / 53.5 / 51.3 /
    #   51.49 / 51.474 / 51.4755 ppb for orders ℏ¹…ℏ⁷, converging to
    #   51.4754 ppb = the untruncated `1 + log(1+ℏ_q)`. Order 2 is the
    #   ONLY order below the limit — a non-monotonic dip. Every further
    #   term walks away from the data. A stopping point that beats the
    #   series it approximates was chosen against the data.
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
    _hbar_q = 1 - 1 / q0
    _hbar_factor = 1 + mp.log(1 + _hbar_q)  # sinh-channel, FULL series
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
        "[3]_q·[4]_q + (α_em/π)·(1+log(1+ℏ_q)) — closed form. Strong core "
        "Lean-proved (qou:QOU.BraidKnot.meson_qCG_3x4). EM factor is the "
        "FULL series: the two-term truncation (3q²−1)/(2q²) was removed "
        "2026-08-22 as a data-selected stopping point (owner directive "
        "2026-08-09), costing 23.45 → 51.48 ppb — still inside the "
        "263.6 ppb target at 5.1× margin. NOT parameter-free: α_em is a "
        "CLASS-A acknowledged anchor (CS ansatz conditional on the open "
        "Witten-κ sorry) and the (3,4) pair is scan-selected — see "
        "docs/audits/2026-08-22-mK-mpi-l2-red-team.md",
    ))

    # ── Two-Term Borromean V³ QED Diagnostics (m_mu, Q_beta, m_n, Delta_pn) ──
    # Attach connected 4th-order Borromean V³ QED diagnostics. NOT parameter-free:
    # pair 1-3 is left out and the m_e scale is chosen (issue #8524,
    # probes/two_term_qed_pair_choice). Since the owner ruling of 2026-11-20 the
    # two-term value is the PRIMARY score (see the ruling block below), scoped
    # as a selection.
    # (`QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm`) at 50 dps without altering
    # any primary ruled z_D scores (respecting owner ruling 2026-09-12).
    from canonical_mass import (
        nucleon_mass_mev as _cm_nucleon_mass_mev,
        proton_qed_self_energy_borromean_mev as _cm_mp_qed_mev,
        np_qed_splitting_borromean_conn_mev as _cm_np_qed_mev,
    )
    _mp_qed_plain = mpf(str(_cm_mp_qed_mev(k_weighted=False)))
    _mp_qed_Kp = mpf(str(_cm_mp_qed_mev(k_weighted=True)))
    _dm_qed_plain = mpf(str(_cm_np_qed_mev(weighting="plain")))
    _dm_qed_KnKp = mpf(str(_cm_np_qed_mev(weighting="KnKp")))
    _dm_qed_Kp3 = mpf(str(_cm_np_qed_mev(weighting="Kp3")))
    _dm_qed_q = mpf(str(_cm_np_qed_mev(weighting="q")))

    _mn_sub_1term = mpf(str(_cm_nucleon_mass_mev("n")))
    _mn_sub_2term = _mn_sub_1term + _dm_qed_plain
    _mn_codata = OBSERVABLES["m_n"][0]
    _mn_sub_1term_err_ppb = (_mn_sub_1term - _mn_codata) / _mn_codata * mpf("1e9")
    _mn_sub_2term_err_ppb = (_mn_sub_2term - _mn_codata) / _mn_codata * mpf("1e9")
    _mn_sub_reduction_pct = (1 - abs(_mn_sub_2term_err_ppb) / abs(_mn_sub_1term_err_ppb)) * 100

    # Two-term proton pin as a named COMPARISON (owner ruling 2026-11-20:
    # one-term stays the default). EXACT findroot root
    # (qou_substrate.constants.q_proton_two_term_at), replacing a linearised
    # finite-difference shift that was 7.5e-15 low and whose note had the
    # sign of the shift wrong.
    _q_1t_str, _q_2t_str = _proton_pin_strings()
    _q0_2term_plain = mpf(_q_2t_str)
    _q0_1term = mpf(_q_1t_str)
    _dq_pin_ppb = (_q0_2term_plain - _q0_1term) / _q0_1term * mpf("1e9")
    _mmu_pred_2term_plain = _m_mu_pred_at(_q_2t_str)
    _mmu_codata = OBSERVABLES["m_mu"][0]
    _mmu_err_2term_ppb = rel_error_ppb(_mmu_pred_2term_plain, _mmu_codata)

    for _r in rows:
        _obs_name = _r.get("obs")
        if _obs_name == "m_mu" and "pred_MeV" in _r:
            _r["two_term_qed_diagnostics"] = {
                "lean_theorem": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3",
                "M_p_QED_conn_plain_MeV": fmt(_mp_qed_plain, 15),
                "M_p_QED_conn_plain_keV": fmt(_mp_qed_plain * mpf(1000), 12),
                "M_p_QED_conn_Kp_MeV": fmt(_mp_qed_Kp, 15),
                "q0_two_term_plain": fmt(_q0_2term_plain, 25),
                "m_mu_pred_two_term_plain_MeV": fmt(_mmu_pred_2term_plain, 12),
                "m_mu_err_two_term_plain_ppb": fmt(_mmu_err_2term_ppb, 4),
                "dq_two_term_minus_one_term_ppb": fmt(_dq_pin_ppb, 12),
                "note": (
                    "Diagnostic only — the primary m_mu score stays at the one-term proton "
                    "pin (owner ruling 2026-11-20: 'Revert to 1-term default'; at the "
                    "two-term pin alpha_em^-1 form B is at 495 sigma, PRs #8562/#8565). "
                    "The two-term comparison pin is the exact root of m_p^QCD + M_p^QED "
                    "= m_p^exp and sits +"
                    f"{fmt(_dq_pin_ppb, 6)} ppb ABOVE the one-term pin (M_p^QED > 0 lowers "
                    "the required m_p^QCD, and d(m_p^QCD/m_e)/dq < 0 here). The two-term "
                    "term is selection-scoped (plain weighting, m_e scale; covariant "
                    "all-pairs projection gives b = 0)."
                ),
            }
        elif _obs_name in ("Q_beta", "m_n", "Delta_pn") and "pred_MeV" in _r:
            _pred_1t = mpf(str(_r["pred_MeV"]))
            _codata_val = OBSERVABLES[_obs_name][0]
            _pred_2t = _pred_1t + _dm_qed_plain
            _err_2t_ppb = rel_error_ppb(_pred_2t, _codata_val)
            _diag = {
                "lean_theorem": "QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3",
                "Delta_m_QED_conn_plain_MeV": fmt(_dm_qed_plain, 15),
                "Delta_m_QED_conn_plain_keV": fmt(_dm_qed_plain * mpf(1000), 12),
                "Delta_m_QED_conn_KnKp_MeV": fmt(_dm_qed_KnKp, 15),
                "Delta_m_QED_conn_Kp3_MeV": fmt(_dm_qed_Kp3, 15),
                "Delta_m_QED_conn_q_MeV": fmt(_dm_qed_q, 15),
                "pred_two_term_plain_MeV": fmt(_pred_2t, 12),
                "err_two_term_plain_ppb": fmt(_err_2t_ppb, 4),
                "primary_ruled_zD_score_untouched": True,
            }
            if _obs_name == "m_n":
                _diag["substrate_identity_m_n_1term_MeV"] = fmt(_mn_sub_1term, 12)
                _diag["substrate_identity_m_n_1term_err_ppb"] = fmt(_mn_sub_1term_err_ppb, 4)
                _diag["substrate_identity_m_n_2term_plain_MeV"] = fmt(_mn_sub_2term, 12)
                _diag["substrate_identity_m_n_2term_plain_err_ppb"] = fmt(_mn_sub_2term_err_ppb, 4)
                _diag["substrate_identity_residual_reduction_pct"] = fmt(_mn_sub_reduction_pct, 4)
            _r["two_term_qed_diagnostics"] = _diag

    # ── OWNER RULING 2026-11-20: two-term QED is PRIMARY ────────────────────
    # Verbatim: "Put two term in scorecards and ALL compute". The scored value
    # of m_mu, Q_beta, m_n and Delta_pn is now the TWO-TERM value (plain
    # normalised connected Borromean V^3 trace at the m_e scale,
    # NucleonWeightSpaceTwoTerm). The one-term row is kept under `one_term`.
    #
    # SCOPE, stated with the ruling, not instead of it:
    #   * the insertion Q12+Q23 is not braid-covariant; on W_p its trace equals
    #     -tr(Q13 w) for every word (the dropped pair) — Lean proof on
    #     claude/two-term-qed-covariance-2026-11-20;
    #   * the covariant (all-pairs) projection gives M_p^QED = 0 and a
    #     word-independent n-p splitting (derived coefficient b = 0);
    #   * of the candidate scales only m_e lands near the mu-p gap
    #     (0.2201 keV vs 0.2288 keV needed); E0_tower gives 1.821 keV, alpha_bind
    #     1.613 keV, alpha_em*E0_tower 0.0133 keV. So the scale and the plain
    #     weighting are SELECTIONS. The four weightings stay in the diagnostics.
    # Do not read the two-term rows as derived until those are closed.
    _TWO_TERM_SCOPE = (
        "OWNER-RULED PRIMARY 2026-11-20 (two-term, plain weighting, m_e scale). "
        "Selection-scoped: non-covariant adjacent insertion (whole proton signal "
        "= dropped pair 1-3), scale m_e chosen among m_e/E0/alpha_bind/"
        "alpha_em*E0; covariant all-pairs projection gives b = 0. One-term "
        "value under `one_term`.")
    _two_term_pred = {"m_mu": _mmu_pred_2term_plain}
    for _r in rows:
        _o = _r.get("obs")
        if _o in ("Q_beta", "m_n", "Delta_pn") and "pred_MeV" in _r:
            _two_term_pred[_o] = mpf(str(_r["pred_MeV"])) + _dm_qed_plain
    for _i, _r in enumerate(rows):
        _o = _r.get("obs")
        if _o not in _two_term_pred:
            continue
        _one = {k: _r[k] for k in ("pred_MeV", "err_ppb", "miss_factor",
                                   "beats_1x_experimental",
                                   "beats_100x_experimental") if k in _r}
        _new = _row_for(_o, _two_term_pred[_o], _r.get("source_witness", ""))
        for _k in ("pred_MeV", "err_ppb", "miss_factor",
                   "beats_1x_experimental", "beats_100x_experimental",
                   "compute_truncation_ppb"):
            _r[_k] = _new[_k]
        _r["one_term"] = _one
        _r["scored_form"] = "two_term_plain_me"
        _r["two_term_scope"] = _TWO_TERM_SCOPE

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
        # `qbeta_convention` describes `qbeta-ck-cache.witness.json`, which is a
        # convention-C artifact by construction — `qbeta_ck_cache.py` raises
        # SystemExit(2) under D, so its `status` is pinned at INHERITED_C
        # forever. Read bare, that looks like a statement about the rows this
        # dashboard publishes, and since the 2026-09-12 re-score it is not one.
        # Say which, in the block itself, so a reader does not have to infer it
        # from `qbeta_ruled_base` three keys away. Bean `qou-zzwm`.
        "convention_frame_qbeta": {
            **qbeta_convention,
            "describes": "qbeta-ck-cache.witness.json (the c_k ladder cache)",
            "scored_rows_consume_this_cache": not bool(
                _ruled.get("calibrated_against_probe_witness")),
            "scored_rows_note": (
                "The Q_beta / m_n / Delta_pn rows published here are built at "
                "z_D = q^3/(q^2+1) -- the canonical convention -- on the base "
                "the owner ruled 2026-09-08, re-scored 2026-09-12. They do NOT "
                "consume this C cache, so this block records the cache's frame "
                "and is NOT a caveat on those rows. What IS open is that no "
                "c_k ladder exists on an admissible base (qou-cds1); see "
                "qbeta_ruled_base.ladder_on_admissible_base_exists."
            ) if _ruled.get("calibrated_against_probe_witness") else (
                "The Q_beta / m_n / Delta_pn rows published here DO consume "
                "this convention-C cache, so the frame above applies to them "
                "directly."
            ),
        },
        "functional_admissibility_qbeta": _functional_admissibility_check(),
        # EMITTED 2026-09-12. `_qbeta_ruled_base()` computes the element, the
        # E_0 form, the calibration verdict, the four candidate elements and the
        # superseded cell -- and NONE of it reached the witness: the dict was
        # consumed for `pred` and for the row's `note` string and then dropped.
        # A previous PR of mine claimed "the row now carries `element_scored` /
        # `element_is_ruled`" as structured fields. It did not; they were in
        # prose only. A field a consumer cannot read is not a record.
        "qbeta_ruled_base": {k: v for k, v in _qbeta_ruled_base().items()
                             if not k.startswith("_")},
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
    print(f"{'Observable':12}  {'role':26}  {'pred err (ppb)':>16}  "
          f"{'σ_exp (ppb)':>14}  {'100× target (ppb)':>20}  "
          f"{'miss factor':>14}  {'1×?':>3}  {'100×?':>5}")
    print("-" * 128)
    for r in out["rows"]:
        if r.get("status") == "NO-WITNESS":
            print(f"{r['obs']:12}  NO WITNESS")
            continue
        print(
            f"{r['obs']:12}  {r['role']:26}  {r['err_ppb']:>16}  "
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
    w.add_data("convention_frame_qbeta", out["convention_frame_qbeta"])
    w.add_data("functional_admissibility_qbeta", out["functional_admissibility_qbeta"])
    w.add_data("qbeta_ruled_base", out["qbeta_ruled_base"])
    # Third and last site of the same repair (see `_inherited_qbeta_scope`).
    # This caveat asserted that the three published rows "were built in Markov
    # convention C" and are "UNREPRODUCIBLE under the canonical convention".
    # Since the 2026-09-12 re-score they are built at `z_D = q³/(q²+1)`, so
    # both clauses are false of what the witness publishes, and the caveat sat
    # in the same file as `qbeta_ruled_base`, which says so. Gate on the scored
    # value's provenance, not on the cache's convention. Bean `qou-zzwm`.
    if (out["convention_frame_qbeta"].get("status") == "INHERITED_C"
            and not out["qbeta_ruled_base"].get(
                "calibrated_against_probe_witness")):
        w.add_caveat(
            "Q_β / m_n / Δ_pn rows: these figures were built in Markov "
            "convention C (z = √q/(q+1)), which the owner ruling of "
            "2026-08-15 excised in favour of the canonical D (z = q³/(q²+1)). "
            "The upstream qbeta-ck-cache.witness.json carries that stamp; "
            "this dashboard published the numbers without it, which is the "
            "defect being fixed here (bean qou-zzwm). NO induced-error figure "
            "is given, deliberately: qbeta_ck_cache.py raises SystemExit(2) "
            "under D, so no D-frame counterpart exists to difference against "
            "and any number here would be manufactured. These figures are "
            "therefore UNREPRODUCIBLE under the canonical convention. "
            "Re-derivation is bean qou-cds1 and is NOT a z-swap — the "
            "2026-08-30 bar-weight prune showed the obstruction is the "
            "offset (α = (z−1)h/2 mixes bar-weight −4 with weight 0), not z. "
            "This caveat makes the inherited frame visible; it does not "
            "change any value.")
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
        # Read `computed=…["total"], expected=…["total"]` — the same expression,
        # so it passed however the table was built (bean `qou-26f2`). There is
        # no external expectation for a snapshot count, but there IS an internal
        # one: the summary must agree with the rows actually serialised beside
        # it. That can fail if rows are filtered after the summary is built,
        # which is the realistic way this dashboard goes wrong.
        computed=len(out["rows"]),
        expected=out["summary"]["total"],
        tolerance=0,
        source="row count in the emitted payload vs the summary's own total",
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
