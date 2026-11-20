"""
Canonical substrate parameter q — single source of truth.

All witness computations import q from here. When a better
measurement of m_μ/m_e or Vol(4_1) becomes available, update
THIS file and re-run all witnesses.

Derivation (2026-05-28: re-pinned from m_p/m_e — the most precise anchor):
    q solves the proton substrate identity (Newton solve, q_at below)
        m_p/m_e = 2·(Vol(4_1)/ℏ_q²)·F_Bor(q) − 12,
        F_Bor(q) = |tr_M(β_Bor,q)|·[3]_q!/q³,
        |tr_M(β_Bor,q)| = (4 + h² − 3h⁴ − h⁶)/(h² + 4)   (closed form).
    m_μ/m_e is now a PREDICTION (agrees to ~9.5σ). The muon-anchor
    closed form q = 1/(1 − √(Vol/(m_μ/m_e))) is kept as q_muon_at()
    for cross-check.

    Experimental error on q₀ (propagated; Vol is a math constant with
    zero error, so only the mass ratio contributes):
        m_p anchor : σ(q₀) = 0.00083 ppb = 830 ppQ   (sensitivity ≈ 21)
        m_μ anchor : σ(q₀) = 1.22    ppb = 1.2e6 ppQ (1474× looser)

    (Was "0.0029 ppb / 2853 ppQ / 429× looser" — computed from the
    CODATA-2018 uncertainty 1.1e-7 on m_p/m_e. The 2022 uncertainty is
    3.2e-8, so the proton anchor is 3.4× tighter than stated and the
    anchor-choice margin correspondingly larger. The q₀ VALUE is
    unchanged: the m_p/m_e value prints identically in both editions,
    so no witness needs regeneration.)

Sources:
    Vol(4_1)  = 2.029883212819307…        (2·Cl₂(π/3), exact math constant)
    m_p/m_e   = 1836.152673426 ± 3.2e-8   (CODATA 2022, 0.017 ppb — ANCHOR)
    m_μ/m_e   = 206.7682827 ± 4.6e-6      (CODATA 2022 — now a prediction)

    Both mass ratios are READ from the NIST table shipped at
    qou_substrate/data/allascii.txt, never transcribed. Two edition
    straddles were removed when that wiring landed (2026-08-15):
    m_μ/m_e was the CODATA-2018 value 206.7682830 (1.451 ppb off), and
    m_p/m_e carried the CODATA-2018 uncertainty 1.1e-7 (3.4× too wide)
    against a value that happens to print the same in both editions.

Anchor-choice rationale: observations/substrate-anchor-alternatives.md,
docs/audits/2026-05-28-mu-p-tension-substrate-floor.md.
"""

import math

from .codata import codata as _codata

# ── Input measurements with uncertainties ────────────────────────
# Vol(4_1) = 2·Cl₂(π/3), the figure-eight hyperbolic volume. COMPUTED, not
# transcribed.
#
# This was the hand-typed literal `2.029883212819307` until 2026-08-21. That
# is not merely f64-truncated — it is not even the correctly-rounded f64 of
# the true value, which is `2.0298832128193074`. The exact constant runs
# 2.02988321281930725004240510854904057188337861506...
#
# A decimal literal cannot be checked by reading it; an expression can, and
# `vol_4_1_at()` further down this module already computes the same thing.
# Having both meant one of them was free to be wrong, and it was the one every
# f64 path used.
#
# Measured blast radius before changing it: `Q` is IDENTICAL either way — the
# f64 Newton solve in `_solve_q_proton_f64` returns the same bits, because the
# discrepancy (1.23e-16 relative) is below what that solve resolves. So this
# corrects the constant without moving the substrate pin. What it does fix is
# every consumer that lifts this value into mpmath, where 1.23e-16 is real:
# the round-trip q_0 -> m_p/m_e improves from 1.2e-16 to 4.0e-49 when the
# exact form is used (`computations/probes/q0_roundtrip_exactness_probe.py`).
try:
    import mpmath as _mp_vol

    _prev_dps = _mp_vol.mp.dps
    try:
        _mp_vol.mp.dps = 60
        _VOL_4_1_EXACT = 2 * _mp_vol.clsin(2, _mp_vol.pi / 3)
        #: 50-digit decimal for mpmath consumers, mirroring Q_50_DIGIT_STR.
        VOL_FIGURE_EIGHT_50_STR = _mp_vol.nstr(
            _VOL_4_1_EXACT, 50, strip_zeros=False
        )
        VOL_FIGURE_EIGHT = float(_VOL_4_1_EXACT)
    finally:
        _mp_vol.mp.dps = _prev_dps
    del _mp_vol, _prev_dps
except ImportError:  # pragma: no cover — mpmath is a hard dependency
    # Correctly-rounded f64 of 2·Cl₂(π/3), i.e. float(exact), NOT a truncation.
    VOL_FIGURE_EIGHT = 2.0298832128193074
    VOL_FIGURE_EIGHT_50_STR = "2.0298832128193072500424051085490405718833786150606"

VOL_FIGURE_EIGHT_ERR = 1e-12               # storage precision (math value is exact)

# The two mass ratios are READ from the NIST table (qou_substrate/data/
# allascii.txt, 2022 CODATA adjustment), never transcribed. Until 2026-08-15
# they were hand-typed literals, and MASS_RATIO_MU_E carried the CODATA-2018
# value 206.7682830 under a "CODATA 2022" comment — 1.451 ppb (0.065σ) from
# the 2022 value 206.7682827. Nothing physical moved, but nothing could
# detect it either: there was no authoritative table in the repo to check
# against. Reading the table removes both the transcription step and the
# possibility of an unnoticed edition straddle.
_P_E                 = _codata("proton-electron mass ratio")
_MU_E                = _codata("muon-electron mass ratio")

MASS_RATIO_P_E       = float(_P_E.value)         # CODATA 2022 (m_p/m_e) — CALIBRATION ANCHOR
MASS_RATIO_P_E_ERR   = float(_P_E.uncertainty)   # 0.017 ppb
MASS_RATIO_MU_E      = float(_MU_E.value)        # CODATA 2022 — now a PREDICTION (cross-check)
MASS_RATIO_MU_E_ERR  = float(_MU_E.uncertainty)  # 22.2 ppb

# ── Derived substrate parameter (m_p-pinned) ─────────────────────
# q is DERIVED (never hardcoded): f64 Newton solve of the proton
# substrate identity below; the arbitrary-precision derivation is
# q_at() (mpmath findroot). m_μ-anchor cross-check: q_muon_at().
def _solve_q_proton_f64(mp_me, vol, iters=80):
    """f64 Newton solve of the RAW proton substrate identity
        m_p/m_e = 2·(vol/ℏ_q²)·F_Bor(q) − 12
    for q, with |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4). Self-contained
    (closed-form tr_M ⇒ no Hecke machinery).

    NO fitted dressing: the multiplicative `habiro_ratio` tower
    (1+46u⁴)(1+4u⁵)(1−29u⁶) briefly lived here (introduced 592eade9,
    PR #3235) and was STRIPPED per the owner ruling of 2026-07-03 —
    it is the rounded-integer fit the 2026-05-28 floor audit rejects
    (true c₄ = 46.0319±0.011, see mp_habiro_c4_keystone_probe; the
    derivation target is the s5-so3 keystone). With the raw identity
    this pin sits ~11.5 ppb from the muon pin — the μ–p tension,
    deliberately left visible. See
    docs/audits/2026-07-03-trace-convention-decision-package.md §Add.3."""
    def _mp_of_q(q):
        h = q - 1.0 / q
        hbar_q = 1.0 - 1.0 / q
        hbar2 = hbar_q ** 2
        trM = abs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
        qf3 = (q**2 + 1 + q**-2) * (q + 1.0 / q)
        return 2 * vol / hbar2 * (trM * qf3 / q**3) - 12
    q = 1.11
    # f64 central difference: dq = q·1e-10 is the right scale for f64
    # (machine ε ≈ 2.2e-16); a dps-scaled dq would underflow here. The
    # arbitrary-precision path is q_at() (mpmath findroot, no manual dq).
    for _ in range(iters):
        f = _mp_of_q(q) - mp_me
        dq = q * 1e-10
        fp = (_mp_of_q(q + dq) - _mp_of_q(q - dq)) / (2 * dq)
        if fp == 0:
            break
        step = f / fp
        q -= step
        if abs(step) < 1e-15:  # f64-converged in ~4-5 iters; skip the rest
            break
    return q

Q         = _solve_q_proton_f64(MASS_RATIO_P_E, VOL_FIGURE_EIGHT)
HBAR_Q    = 1.0 - 1.0 / Q
HBAR_Q_SQ = HBAR_Q * HBAR_Q

# ── Uncertainty propagation (from the m_p/m_e anchor) ────────────
# q is pinned from m_p/m_e via the substrate identity; sensitivity
# S = dln(m_p)/dln(q) ≈ 21, so σ(q)/q = (1/S)·σ(m_p)/m_p. Vol(4_1) is a
# math constant (zero experimental error); only the mass ratio enters.
#   ⇒ σ(q₀) ≈ 0.00083 ppb = 830 ppQ (vs 1.22 ppb on the old muon anchor).
#
# STALE FIGURE CORRECTED 2026-08-31. This read "σ(q₀) ≈ 0.0029 ppb = 2853 ppQ",
# which is 3.6× the value the formula on the next line actually produces. It is
# reproduced exactly by the PRE-2026-08-21 σ(m_p/m_e) of 0.06 ppb (0.06/21 =
# 0.00286) — the figure AGENTS.md already records as corrected to 0.017. The
# CODE was never wrong: Q_ERR reads MASS_RATIO_P_E_ERR live, so it has tracked
# the correction all along; only this human-readable comment did not. Measured
# in computations/substrate/mmu_l2_reachability_scoping_probe.py (5/5), which
# also measures S_proton = 20.9970 against the 21.0 literal below (0.014 %).
# The 0.00083 above is what Q_ERR actually evaluates to; the live relative
# σ(m_p/m_e) is 0.0174 ppb rather than the 0.017 quoted in prose, and this
# figure is quoted from the code rather than recomputed from the rounded input
# — the failure mode being corrected here is precisely a figure that disagreed
# with the formula beside it.
_S_PROTON = 21.0
Q_ERR  = (Q / _S_PROTON) * (MASS_RATIO_P_E_ERR / MASS_RATIO_P_E)  # ~9.2e-13

# ── Derived constants from q ─────────────────────────────────────
Q_INV     = 1.0 / Q
HA        = Q - Q_INV                        # q - q⁻¹
E_CROSS   = 0.5 * HA                         # crossing energy ½(q - q⁻¹)
S_SKEIN   = math.sqrt(Q) - 1.0/math.sqrt(Q)  # Skein amplitude q^½ - q^{-½}
TWO_Q     = Q + Q_INV                        # [2]_q = q + q⁻¹
TANH_LN_Q = HA / TWO_Q                      # tanh(ln q)
LN_Q      = math.log(Q)                      # ln(q) — for base-q conversions

def log_q(x):
    """Base-q logarithm: log_q(x) = ln(x) / ln(q).
    Maps Skein polynomial ratios to q-integers: log_q(q^n) = n."""
    return math.log(x) / LN_Q

# ── q_int: EXACT, not float64 (2026-09-19, bean `qou-oiz3`) ──────
# This function used to be `(Q**n - Q_INV**n) / HA` over the binary64
# globals above. It is the ROOT of the corpus-wide float64 leak that
# PR #7245 mis-attributed to `pyhecke/wedderburn.py`: that module only
# CALLS this, accumulating into an `mp.mpf`, so its results are
# mpf-TYPED and float64-VALUED — they print 40 digits and carry ~16.
#
# The error is NOT bounded by float64 eps: `q_factorial(n)` multiplies
# n such factors, so it grows with the strand count. Measured worst
# relative move of `wedderburn_weight` over all partitions:
#   n=3 3.05e-16 · n=6 8.75e-16 · n=9 1.62e-15 · n=12 2.41e-15
# n = 3A, so at A >= 3 the L1 target (1 ppQ = 1e-15) was MISSED in the
# Wedderburn-weight layer, invisibly.
#
# Two caches. `_Q_AT_CACHE` exists because `q_at` is an uncached Newton
# solve and `q_int` is called inside O(n^2) hook loops. Both are keyed
# on the working precision and both are built INSIDE an explicit
# precision context, so neither can inherit the ambient `mp.dps` of
# whoever touched it first (the cached-mpf trap).
#
# `_Q_INT_DPS_FLOOR` is deliberate: mpmath's ambient default is 15 dps,
# so returning at the ambient precision would hand a bare-import caller
# FEWER digits than the float64 route it replaces. The floor makes the
# change non-regressive at every call site.
_Q_AT_CACHE: dict = {}
_Q_INT_CACHE: dict = {}
_Q_INT_DPS_FLOOR = 50


def _q_at_cached(dps: int):
    """`q_at(dps)`, memoised on dps. `q_at` sets its own working
    precision, so the cached value carries `dps` digits whatever the
    ambient `mp.dps` was at first touch."""
    v = _Q_AT_CACHE.get(dps)
    if v is None:
        v = q_at(dps)
        _Q_AT_CACHE[dps] = v
    return v


def q_int(n):
    """Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}).

    Exact mpmath at ``max(mp.dps, 50)``, pinned on the proton anchor
    (`q_at`). Returns an ``mpf``; the previous binary64 return is gone.
    """
    if not HAS_MPMATH:
        # No silent float64 fallback — same disposition as the four
        # other fallbacks in this module (owner directive 2026-09-07,
        # AGENTS.md's own worked example of exemption 1).
        raise RuntimeError(
            "q_int requires mpmath: the float64 route was excised "
            "2026-09-19 (bean qou-oiz3) and there is no exact "
            "alternative without it. `pip install mpmath`"
        )
    d = max(_mp.mp.dps, _Q_INT_DPS_FLOOR)
    key = (n, d)
    val = _Q_INT_CACHE.get(key)
    if val is None:
        val = q_int_at(n, q=_q_at_cached(d + 10), dps=d)
        _Q_INT_CACHE[key] = val
    return val

# ── Error propagation for derived constants ──────────────────────
# All errors are δX = |dX/dq| × Q_ERR
Q_INV_ERR     = Q_ERR / Q**2
HA_ERR        = Q_ERR * (1 + Q_INV**2)          # d(q-q⁻¹)/dq = 1+q⁻²
E_CROSS_ERR   = 0.5 * HA_ERR
S_SKEIN_ERR   = Q_ERR * 0.5 * (Q**(-0.5) + Q**(-1.5))
TWO_Q_ERR     = Q_ERR * abs(1 - Q_INV**2)
TANH_LN_Q_ERR = Q_ERR * 2.0 / TWO_Q**2         # d(tanh)/dq

def q_int_err(n):
    """Uncertainty in [n]_q from Q_ERR."""
    # d[n]_q/dq = (n q^{n-1} + n q^{-n-1}) / (q-q⁻¹)
    #           - (q^n - q^{-n})(1+q⁻²) / (q-q⁻¹)²
    num_deriv = n * (Q**(n-1) + Q_INV**(n+1))
    denom_corr = (Q**n - Q_INV**n) * (1 + Q_INV**2) / HA
    return abs(num_deriv / HA - denom_corr / HA) * Q_ERR

# ── For hecke_engine (exact rational arithmetic) ─────────────────
# The engine uses Fraction(p_num, p_den) where q = p_num/p_den.
# We provide the best rational approximation at the engine's precision.
# 11099786 / 10000000 gives q to 7 significant figures.
Q_RAT_NUM = 11099786
Q_RAT_DEN = 10000000

# ── Centralized high-precision string for q_0 (for mpmath callers) ─
# Q_50_DIGIT_STR is DERIVED (q_str(50)) in the mpmath block below — it is
# NOT a hardcoded literal, so it can never drift from the canonical
# q_at() solve. Re-pinned 2026-05-28 from m_p/m_e via the proton
# substrate identity (m_μ/m_e is now a 9.5σ prediction; old muon value
# was 1.10997859555418…, −11.5 ppb away). See q_at()/q_muon_at() and
# docs/audits/2026-05-28-mu-p-tension-substrate-floor.md.

# ── High-precision (mpmath) parallel API ─────────────────────────
# The f64 globals above are bit-identical to what every existing
# witness script reads via `from q_parameter import Q, HBAR_Q, ...`.
# Don't change them — downstream f64 callers depend on stability.
#
# For the Clarabel high-precision / 50-dps work (CLARABEL_PRECISION_PLAN
# §S7), HP callers should use `q_at(dps)` or the `_MP` globals below,
# which carry mpmath.mpf values computed at 50 decimal digits by
# default.  Vol(4_1) is reused at 38-digit precision from
# `alpha_em_pslq_uniqueness.py`; the mass ratio is bounded by CODATA
# 2022's published precision (~7 sig figs).
#
# The mpmath path is bit-identical to f64 in the first ~15 digits
# (SnapPy's Vol limit); past that it is stable but bounded by
# CODATA m_μ/m_e uncertainty.

# Digit strings straight from the NIST table — see the note at the top of the
# "Input measurements" block above.
MASS_RATIO_P_E_STR   = _P_E.value_str    # CODATA 2022 (m_p/m_e) — pinning anchor
MASS_RATIO_MU_E_STR  = _MU_E.value_str   # CODATA 2022 — now a prediction (cross-check)

# ── _DPS_DEFAULT: 50 -> 70 (2026-09-19, bean `qou-5eg1`) ─────────
# This was a SURVIVOR of the old serialization floor, not a considered
# ceiling.  `qou_substrate/precision.py:80-82` records the move that
# left it behind, in its own words:
#
#     # Bumped 2026-05-31 (PR #1595): 50->60 output, 65->70 compute.
#
# `_DPS_DEFAULT` was not bumped with it, so for nearly four months the
# whole `_MP` constant family carried 50 digits while `COMPUTE_DPS` was
# 70 and `OUTPUT_DPS` 60.  Measured at `mp.dps = 120` before this
# change: `Q_MP` and `q_at(90)` agree to 50 significant digits and
# diverge at the 51st, |diff| = 1.1000161e-51.  A producer that raised
# compute precision and then `fmt`-serialised an `_MP`-derived value at
# `OUTPUT_DPS = 60` published ten digits that carried no information —
# and they are ARBITRARY digits, not trailing zeros, so the
# float64-padding ratchet cannot see them (it looks for the zero
# signature), `scriptHash` never drifts (the producer's own bytes are
# stable), and the raw-float64 ratchet sees a genuine `mpf`.  Exact
# arithmetic on a truncated input is invisible to all three.
#
# 70 = COMPUTE_DPS, so the constants now carry what the compute layer
# is entitled to assume they carry.
#
# NOT AN ANCHOR CHANGE.  `computations/q_pinning_50_digit.py` calls
# `q_at(mp.dps)` with the dps EXPLICIT (its line 108, after
# `set_compute_dps()`), so the anchor-defining witness is a function of
# `COMPUTE_DPS`, never of this constant.  Verified byte-identical
# across the bump.
_DPS_DEFAULT = 70

# Note: previously this module reused a hardcoded 38-dps string for
# Vol(4_1) from `alpha_em_pslq_uniqueness.py:57`.  That string is
# inaccurate past digit ~30 — its trailing digits do not match the
# Clausen-converged value.  The function `vol_4_1_at` below recomputes
# from scratch at every requested precision, so q is correct at any
# dps the caller asks for.

try:
    import mpmath as _mp

    def vol_4_1_at(dps: int = _DPS_DEFAULT):
        """Hyperbolic volume of the figure-eight knot, computed at
        requested precision.  Identity: Vol(4_1) = 2 Cl_2(π/3) where
        Cl_2 is the Clausen function (mpmath.clsin)."""
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 10)  # +10 guard digits
            vol = 2 * _mp.clsin(2, _mp.pi / 3)
            return +vol  # round to current dps
        finally:
            _mp.mp.dps = prev

    def q_muon_at(dps: int = _DPS_DEFAULT):
        """CROSS-CHECK: q from the muon-anchor closed form
        q = 1/(1 − √(Vol(4_1)/(m_μ/m_e))). This was the pin until
        2026-05-28; now superseded by q_at() (m_p anchor). Differs from
        q_at() by ~11.5 ppb — that gap is the μ-p tension (9.5σ)."""
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 10)
            vol = vol_4_1_at(dps + 10)
            r = _mp.mpf(MASS_RATIO_MU_E_STR)
            hbar = _mp.sqrt(vol / r)
            q = _mp.mpf(1) / (_mp.mpf(1) - hbar)
            _mp.mp.dps = max(prev, dps)
            return +q
        finally:
            _mp.mp.dps = prev

    def q_at(dps: int = _DPS_DEFAULT):
        """Return q at requested mpmath precision, pinned from m_p/m_e
        (the most precise anchor) via the proton substrate identity:
            m_p/m_e = 2·(Vol(4_1)/ℏ_q²)·|tr_M(β_Bor)|·[3]_q!/q³ − 12,
            |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4)   (closed form).
        The closed-form tr_M needs no Hecke machinery, so this Newton
        solve is self-contained and exact at any dps. Caller should set
        ``mpmath.mp.dps`` ≥ ``dps`` before further mpmath arithmetic.

        RAW identity (owner ruling 2026-07-03): the fitted habiro_ratio
        tower that briefly dressed this solve (592eade9) is stripped —
        this pin sits ~11.5 ppb from q_muon_at() (the μ–p tension) and
        m_μ is a genuine ~210 ppb prediction at this q₀."""
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 15)
            vol = vol_4_1_at(dps + 15)
            mp_me = _mp.mpf(MASS_RATIO_P_E_STR)

            def _resid(q):
                h = q - 1 / q
                hbar_sq = (1 - 1 / q) ** 2
                trM = _mp.fabs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
                qf3 = (q**2 + 1 + q**(-2)) * (q + q**(-1))
                return 2 * vol / hbar_sq * (trM * qf3 / q**3) - 12 - mp_me

            q = _mp.findroot(_resid, _mp.mpf("1.10997858"))
            _mp.mp.dps = max(prev, dps)
            return +q
        finally:
            _mp.mp.dps = prev

    def q_str(dps: int = _DPS_DEFAULT) -> str:
        """Return q as a decimal string at requested precision —
        the canonical witness-JSON / Clarabel-HP serialisation."""
        return _mp.nstr(q_at(dps), dps, strip_zeros=False)

    # Compute the cached _MP globals at the default precision via
    # `mp.workdps` so this module does NOT mutate the caller's
    # `mp.mp.dps`.  Many downstream scripts set `mp.mp.dps` BEFORE
    # importing q_parameter; the previous global assignment silently
    # overrode their precision setting.  workdps restores on exit.
    with _mp.workdps(_DPS_DEFAULT):
        Q_MP         = q_at(_DPS_DEFAULT)            # m_p-pinned (proton identity)
        VOL_4_1_MP   = vol_4_1_at(_DPS_DEFAULT)
        Q_INV_MP     = _mp.mpf(1) / Q_MP
        # ℏ_q derived from the (m_p-pinned) q, NOT from Vol/m_μ — the
        # latter would be the muon value and inconsistent with Q_MP.
        HBAR_Q_MP    = _mp.mpf(1) - Q_INV_MP
        HBAR_Q_SQ_MP = HBAR_Q_MP ** 2
        HA_MP        = Q_MP - Q_INV_MP
        E_CROSS_MP   = HA_MP / 2
        S_SKEIN_MP   = _mp.sqrt(Q_MP) - _mp.mpf(1) / _mp.sqrt(Q_MP)
        TWO_Q_MP     = Q_MP + Q_INV_MP
        TANH_LN_Q_MP = HA_MP / TWO_Q_MP
        LN_Q_MP      = _mp.log(Q_MP)

    # Canonical 50-digit string — DERIVED from the already-cached Q_MP
    # (no hardcoded literal, no sync drift, no second findroot at import).
    # This is what witness scripts import.
    # PINNED AT 50 DELIBERATELY.  This used to read `_DPS_DEFAULT`, so the
    # bump above would have silently turned a constant whose NAME says 50
    # into a 70-digit string for its ~1500 consumers -- several of which
    # compare it by prefix or by length.  The name is the specification:
    # 50 digits is what this constant means.  Callers that want the full
    # working precision should use `q_str(dps)` / `q_at(dps)`.
    #
    # It is therefore a SECOND 50-dps channel and it is NOT closed by this
    # change: `mpf(Q_50_DIGIT_STR)` caps at 50 wherever it is used (e.g.
    # `pyhecke.constants.alpha_em_inv_mp`).  Measured: 525 committed
    # witnesses publish > 50 significant digits and have a producer that
    # references `Q_50_DIGIT_STR` or an `_MP` constant, against 116 for the
    # `_MP` constants alone.  Bean `qou-5eg1`, still open on that half.
    Q_50_DIGIT_STR = _mp.nstr(Q_MP, 50, strip_zeros=False)

    # ── THE MUON PIN'S ONE NAMED HOME (bean qou-5op4) ──────────────
    #
    # Until now the muon pin had NO canonical source. The proton pin has
    # exactly one — Q_50_DIGIT_STR above. The muon pin had a live derivation
    # (q_muon_at) plus hand-typed copies with two different truncations, and a
    # fixed-string grep for the 17-digit ancestor `1.1099785955541805` finds
    # **336 files** (222 .json, 73 .py, 41 .md). A literal cannot drift from a
    # source it does not have; these had none. That is the defect.
    #
    # THIS IS A FROZEN STRING, NOT A DERIVATION, AND THAT IS THE POINT.
    # `q_muon_at()` re-derives from MASS_RATIO_MU_E_STR and vol_4_1_at(), so it
    # RE-VALUES whenever CODATA moves — and it has. Three values are live today:
    #
    #   frozen (this constant, and AGENTS.md)  1.10997859555733471989976322048…
    #   17-digit ancestor (336 files)          1.1099785955541805…
    #   q_muon_at() as of 2026-08-24           1.10997859564273904668179512938…
    #
    #   rel(derived, frozen)   = 7.694e-11   (0.0769 ppb)
    #   rel(ancestor, frozen)  = 2.842e-12   (0.00284 ppb)
    #
    # Scale, so nobody mis-files this: both are far BELOW the 11.5 ppb μ–p
    # substrate tension (no layer is confused) and far ABOVE the 1 ppQ (1e-15)
    # L1 compute target. A precision defect, not a physics one.
    #
    # WHICH TO USE. A witness that must stay reproducible against its own
    # history imports this constant — it cannot re-value under it. A caller that
    # genuinely wants "the muon pin implied by today's CODATA" calls
    # q_muon_at(). Do not hand-type either; that is what produced the 336.
    #
    # REFRESH PROCEDURE (it goes stale BY DESIGN — that is the trade):
    # this string is only updated by a deliberate, owner-authorised re-pin that
    # also migrates the witnesses recording the old value. Never edit it to
    # silence a drift check. Sequenced behind PR #5500 (muon anchor -> CODATA
    # 2022, audit red, 53 witnesses outstanding) and behind the qou-1c4y
    # migration, whose four constraints — in particular "never re-pin an
    # anchor-DEFINING witness" and "do not split the change" — govern it.
    Q_MUON_50_DIGIT_STR = (
        "1.1099785955573347198997632204832250266562084087801536866079811461449"
    )

    def q_muon_frozen_at(dps: int = _DPS_DEFAULT):
        """The FROZEN muon pin as an mpf — reproducible, does not re-value.

        The counterpart to `q_muon_at()`, which derives and therefore moves
        with CODATA. Use this when a recorded value must still mean the same
        thing when read back later; use `q_muon_at()` when you want the pin
        implied by today's inputs. Bean qou-5op4.
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 10)
            q = _mp.mpf(Q_MUON_50_DIGIT_STR)
            _mp.mp.dps = max(prev, dps)
            return +q
        finally:
            _mp.mp.dps = prev

    HAS_MPMATH = True

    # ── q-PARAMETRIC quantum integers (bean qou-c041) ────────────────
    # The f64 `q_int(n)` above is PINNED to the module's Q: it takes n
    # only, with Q/Q_INV/HA as globals, so it cannot be evaluated at any
    # other q. A symbolic audit
    # (computations/audits/q_integer_duplication_audit.py) found 366
    # local reimplementations across computations/ and tools/, in 363
    # files, and that pinning is why: callers that vary q had nothing to
    # import. These two are what they can import instead.
    #
    # There are TWO conventions in the corpus and they are NOT
    # interchangeable — 126 definitions use the symmetric form, 30 the
    # classical one. They never take the same value anywhere both are
    # defined (Lean: QOU.Substrate.QIntegerConventions, sorry-free), so
    # pick deliberately:
    #
    #   symmetric  — quantum dimensions, Markov trace, Wedderburn
    #                weights, normalised Hecke bases
    #   classical  — the T_w (Iwahori, unnormalised) basis, Coxeter-length
    #                and coinvariant Poincare gradings, Gaussian binomials
    #
    # Bridge, proved in that Lean file at n = 2,3 and checked symbolically
    # to n = 7:   q^(n-1) * [n]_symmetric(q) = [n]_classical(q^2).

    def q_int_at(n: int, q=None, dps: int = _DPS_DEFAULT):
        """SYMMETRIC (balanced) quantum integer, q-parametric.

            [n]_q = (q^n - q^-n) / (q - q^-1)

        `q` defaults to the module's substrate value at `dps`. The
        removable singularity at q = 1 is handled: [n]_q -> n there,
        which the naive quotient reaches as 0/0 (a ZeroDivisionError in
        several corpus copies).
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 10)
            qq = q_at(dps + 10) if q is None else _mp.mpf(q)
            if qq == 1:
                _mp.mp.dps = max(prev, dps)
                return +_mp.mpf(n)
            val = (qq ** n - qq ** (-n)) / (qq - 1 / qq)
            _mp.mp.dps = max(prev, dps)
            return +val
        finally:
            _mp.mp.dps = prev

    def q_int_classical_at(n: int, q=None, dps: int = _DPS_DEFAULT):
        """CLASSICAL (Gaussian) quantum integer, q-parametric.

            [n]_q = (q^n - 1) / (q - 1) = 1 + q + ... + q^(n-1)

        Computed as the geometric sum, so it is total: defined at every
        q including q = 1, where it is n. This is NOT the symmetric
        bracket — see the block comment above before choosing.
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 10)
            qq = q_at(dps + 10) if q is None else _mp.mpf(q)
            val = _mp.fsum(qq ** i for i in range(n))
            _mp.mp.dps = max(prev, dps)
            return +val
        finally:
            _mp.mp.dps = prev

    # ── Borromean V³ = (σ₁σ₂⁻¹)³ 3-strand weight-space traces & two-term pin ──
    # Backed by sorry-free Lean 4 theorems in
    # `QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean` (bean qou-7ph7).
    # Tier A additive helpers: these do NOT modify `q_at()` or `Q_50_DIGIT_STR`.

    def tr_borromean_v3_at(q=None, dps: int = _DPS_DEFAULT):
        """3D weight-space trace of the Borromean braid V³ = (σ₁σ₂⁻¹)³ on W_p or W_n.

        Lean 4: `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_borromeanV3A`
        (and `trace_borromeanV3B`):
            tr(V³) = (-q¹² + 3q¹⁰ - 3q⁸ + 5q⁶ - 3q⁴ + 3q² - 1) / q⁶.
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 15)
            qq = q_at(dps + 15) if q is None else _mp.mpf(q)
            q2 = qq ** 2
            num = -(q2 ** 6) + 3 * (q2 ** 5) - 3 * (q2 ** 4) + 5 * (q2 ** 3) - 3 * (q2 ** 2) + 3 * q2 - 1
            val = num / (q2 ** 3)
            _mp.mp.dps = max(prev, dps)
            return +val
        finally:
            _mp.mp.dps = prev

    def tr_e21_borromean_v3_at(q=None, dps: int = _DPS_DEFAULT):
        """2D mixed-symmetry (2,1)-projected trace tr(e_{(2,1)} V³) = tr(V³) - 1.

        Lean 4: `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_e21p_borromeanV3`
        (and `trace_e21n_borromeanV3`):
            tr(e_{(2,1)} V³) = -(q⁴ - q² + 1)(q⁸ - 2q⁶ - 2q² + 1) / q⁶.
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 15)
            qq = q_at(dps + 15) if q is None else _mp.mpf(q)
            q2 = qq ** 2
            val = -(q2 ** 2 - q2 + 1) * (q2 ** 4 - 2 * (q2 ** 3) - 2 * q2 + 1) / (q2 ** 3)
            _mp.mp.dps = max(prev, dps)
            return +val
        finally:
            _mp.mp.dps = prev

    def tr_conn_borromean_p_at(q=None, dps: int = _DPS_DEFAULT):
        """Per-strand connected 4th-order Borromean charge trace on the proton W_p:
            tr_bar_conn(p, V³) = (1/3) tr((Q₁₂^(p) + Q₂₃^(p)) V_p³)
                               = -2(q² - 1)⁴(q⁴ + q² + 1) / (27 q⁶).

        Lean 4: (1/3) * `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3`.
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 15)
            qq = q_at(dps + 15) if q is None else _mp.mpf(q)
            q2 = qq ** 2
            val = -2 * ((q2 - 1) ** 4) * (q2 ** 2 + q2 + 1) / (27 * (q2 ** 3))
            _mp.mp.dps = max(prev, dps)
            return +val
        finally:
            _mp.mp.dps = prev

    def tr_conn_borromean_n_at(q=None, dps: int = _DPS_DEFAULT):
        """Per-strand connected 4th-order Borromean charge trace on the neutron W_n
        (after subtracting the static (-2/9) I₃ background per `QAdjn_eq_static_add_half_QAdjp`):
            tr_bar_conn(n, V³) = (1/3) (tr((Q₁₂^(n) + Q₂₃^(n)) V_n³) + (2/9) tr(V_n³))
                               = +(q² - 1)⁴(2q⁴ - q² + 2) / (27 q⁶).

        Lean 4: (1/3) * `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjn_borromeanV3_connected`.
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 15)
            qq = q_at(dps + 15) if q is None else _mp.mpf(q)
            q2 = qq ** 2
            val = ((q2 - 1) ** 4) * (2 * (q2 ** 2) - q2 + 2) / (27 * (q2 ** 3))
            _mp.mp.dps = max(prev, dps)
            return +val
        finally:
            _mp.mp.dps = prev

    def tr_conn_borromean_diff_at(q=None, dps: int = _DPS_DEFAULT):
        """Connected 4th-order Borromean charge trace difference (neutron minus proton):
            Δtr_bar_conn(V³) = tr_bar_conn(n, V³) - tr_bar_conn(p, V³)
                             = +(q² - 1)⁴(4q⁴ + q² + 4) / (27 q⁶).

        Lean 4: (1/3) * `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3`.
        """
        prev = _mp.mp.dps
        try:
            _mp.mp.dps = max(prev, dps + 15)
            qq = q_at(dps + 15) if q is None else _mp.mpf(q)
            q2 = qq ** 2
            val = ((q2 - 1) ** 4) * (4 * (q2 ** 2) + q2 + 4) / (27 * (q2 ** 3))
            _mp.mp.dps = max(prev, dps)
            return +val
        finally:
            _mp.mp.dps = prev

    def q_two_term_borromean_at(dps: int = _DPS_DEFAULT, k_weighted: bool = False):
        """Parallel two-term connected Borromean proton pin (Tier A diagnostic helper).

        Solves:
            2·(Vol(4₁)/ℏ_q²)·F_Bor(q) − 12 + w(q)·|tr_bar_conn(p, V³)| = m_p/m_e
        where w(q) = q if `k_weighted=True` (K_p^⊗3 determinant weight) else 1,
        via 14 Newton iterations at `dps + 25` guard digits starting from `q_at(dps + 25)`.

        Does NOT modify `q_at()` or `Q_50_DIGIT_STR`.
        """
        prev = _mp.mp.dps
        try:
            work_dps = max(prev, dps + 25)
            _mp.mp.dps = work_dps
            vol = vol_4_1_at(work_dps)
            mp_me = _mp.mpf(MASS_RATIO_P_E_STR)

            def _f(qq):
                h = qq - 1 / qq
                hbar_sq = (1 - 1 / qq) ** 2
                trM = _mp.fabs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
                qf3 = (qq ** 2 + 1 + qq ** (-2)) * (qq + qq ** (-1))
                qcd_term = 2 * vol / hbar_sq * (trM * qf3 / (qq ** 3)) - 12
                q2 = qq ** 2
                tr_conn_p_abs = 2 * ((q2 - 1) ** 4) * (q2 ** 2 + q2 + 1) / (27 * (q2 ** 3))
                w = qq if k_weighted else _mp.mpf(1)
                return qcd_term + w * tr_conn_p_abs - mp_me

            q = q_at(work_dps)
            eps = _mp.mpf(10) ** (-(work_dps // 2))
            for _ in range(14):
                fq = _f(q)
                dfq = (_f(q + eps) - _f(q - eps)) / (2 * eps)
                if dfq == 0:
                    break
                q = q - fq / dfq
            _mp.mp.dps = max(prev, dps)
            return +q
        finally:
            _mp.mp.dps = prev


except ImportError:
    HAS_MPMATH = False

    def vol_4_1_at(dps: int = _DPS_DEFAULT):
        raise RuntimeError("vol_4_1_at requires mpmath; install it with `pip install mpmath`")

    def q_at(dps: int = _DPS_DEFAULT):
        raise RuntimeError("q_at requires mpmath; install it with `pip install mpmath`")

    def q_str(dps: int = _DPS_DEFAULT) -> str:
        raise RuntimeError("q_str requires mpmath; install it with `pip install mpmath`")

    # No-mpmath fallback: only the f64-precision q is available. 50-dps
    # work requires mpmath; this string carries f64 precision only.
    Q_50_DIGIT_STR = repr(Q)

    # The frozen muon pin is a STRING, so it survives the no-mpmath path intact
    # — unlike Q_50_DIGIT_STR above, which degrades to f64 here. Bean qou-5op4.
    Q_MUON_50_DIGIT_STR = (
        "1.1099785955573347198997632204832250266562084087801536866079811461449"
    )

    def q_muon_frozen_at(dps: int = _DPS_DEFAULT):
        raise RuntimeError(
            "q_muon_frozen_at requires mpmath; the frozen string is still "
            "available as Q_MUON_50_DIGIT_STR"
        )

    # These RAISE rather than falling back to f64, matching the four above.
    # A q-integer is an input to quantum dimensions, Markov traces and
    # Wedderburn weights; computing one in binary64 and returning it silently
    # is the failure the NO-FLOAT64 discipline exists to prevent, and a caller
    # cannot tell a degraded result from a good one. Failing loudly is the
    # corpus convention here (cf. q_parameter.py, "Refusing to fall back to
    # proton silently"). Owner directive, 2026-09-07.

    def q_int_at(n: int, q=None, dps: int = _DPS_DEFAULT):
        raise RuntimeError("q_int_at requires mpmath; install it with `pip install mpmath`")

    def q_int_classical_at(n: int, q=None, dps: int = _DPS_DEFAULT):
        raise RuntimeError(
            "q_int_classical_at requires mpmath; install it with `pip install mpmath`"
        )

    def tr_borromean_v3_at(q=None, dps: int = _DPS_DEFAULT):
        raise RuntimeError("tr_borromean_v3_at requires mpmath; install it with `pip install mpmath`")

    def tr_e21_borromean_v3_at(q=None, dps: int = _DPS_DEFAULT):
        raise RuntimeError("tr_e21_borromean_v3_at requires mpmath; install it with `pip install mpmath`")

    def tr_conn_borromean_p_at(q=None, dps: int = _DPS_DEFAULT):
        raise RuntimeError("tr_conn_borromean_p_at requires mpmath; install it with `pip install mpmath`")

    def tr_conn_borromean_n_at(q=None, dps: int = _DPS_DEFAULT):
        raise RuntimeError("tr_conn_borromean_n_at requires mpmath; install it with `pip install mpmath`")

    def tr_conn_borromean_diff_at(q=None, dps: int = _DPS_DEFAULT):
        raise RuntimeError("tr_conn_borromean_diff_at requires mpmath; install it with `pip install mpmath`")

    def q_two_term_borromean_at(dps: int = _DPS_DEFAULT, k_weighted: bool = False):
        raise RuntimeError("q_two_term_borromean_at requires mpmath; install it with `pip install mpmath`")

# ── Experimental observable anchors (CODATA 2022) ─────────────
# Mirrored from `computations/substrate/experimental_constants.py`
# so consumers running outside the repo (Pyodide, Sage, PyPI installs)
# can reach the same MeV anchors without depending on the flat-name
# `experimental_constants` shim that only `_legacy` puts on sys.path.
# Authoritative source is the substrate cluster file; values match.
# READ from the NIST table, not transcribed -- same discipline as the two
# mass ratios above (PR #5149). This block was left on literals by that pass
# and three of the six were the CODATA-**2018** values under a "CODATA 2022"
# comment: M_P_MEV 938.27208816 (2022: ...943), M_N_MEV 939.56542052
# (2022: ...194), and M_N_MEV_ERR 0.00000054 (2022: 0.00000048). M_E_MEV_ERR
# was 0.00000000015 against the table's 0.00000000016. Q_NEUTRON_MEV below is
# DERIVED from all three, so it inherited the drift.

_E_MEV  = _codata("electron mass energy equivalent in MeV")
_P_MEV  = _codata("proton mass energy equivalent in MeV")

# NO-FLOAT64 (2026-09-12). `CodataEntry.value` is ALREADY an `mpmath.mpf`, so
# `float(...)` here is an active DOWNCAST of an exact table value, and the
# derived Q_NEUTRON_MEV below then did its arithmetic in binary64 across a
# catastrophic cancellation (0.78 MeV out of 939.57 — three digits gone).
#
# The `_STR` companions are the file's own established convention for exactly
# this, from MASS_RATIO_P_E_STR / MASS_RATIO_MU_E_STR above: carry the digits
# exactly as the NIST table prints them, so an mpmath consumer can reach full
# precision without a transcription step. `value_str` is a plain `str`, so the
# companions cost nothing and cannot themselves lose precision.
#
# The float names KEEP THEIR TYPE — 309 in-repo importers read them and a type
# change is not a precision fix. What changes is that the DERIVED quantities
# below are now computed in `mpf` and downcast once at the end, instead of
# accumulating three binary64 subtractions. Measured gain on Q_NEUTRON_MEV:
# 9.15e-14 MeV = 1.17e-4 ppb, which is 117x the framework's own L1 target of
# 1 ppQ (1e-6 ppb). Far below the 780 ppb experimental sigma, so no recorded
# comparison moves; it is an L1 compute-precision repair, not an L2 one.
M_E_MEV_STR     = _E_MEV.value_str
M_E_MEV_ERR_STR = _E_MEV.uncertainty_str
M_P_MEV_STR     = _P_MEV.value_str
M_P_MEV_ERR_STR = _P_MEV.uncertainty_str

M_E_MEV     = float(_E_MEV.value)
M_E_MEV_ERR = float(_E_MEV.uncertainty)
M_P_MEV     = float(_P_MEV.value)
M_P_MEV_ERR = float(_P_MEV.uncertainty)

# M_N is NOT read from the table, deliberately. The table's neutron entry is
# the CODATA-DIRECT value 939.56542194; the corpus canonically uses the
# AME-DERIVED 939.56542179 (codata_2022_source.M_N_MEV = M_N_MEV_AME_DERIVED),
# and this block documents itself as a mirror of
# computations/substrate/experimental_constants.py. Layer 2a cannot import
# from computations/, so the AME value is carried as a literal here.
#
# The distinction is load-bearing, not cosmetic: Q_NEUTRON_MEV below is
# m_n - m_p - m_e, and AME pins that DIFFERENCE rather than the absolute
# masses. Reading the CODATA-direct neutron from the table while taking the
# 2022 proton shifts Q_beta by +0.15 eV -- an artifact of mixing the two
# determinations, not a real change. A first pass of this drain did exactly
# that before the cancellation was noticed.
#
# Excluded from codata_table_vintage_audit by design: AME-derived quantities
# are not CODATA-adjustment outputs and checking them against the table is a
# category error (AGENTS.md).
M_N_MEV_STR     = "939.56542179"   # noqa: P31 - AME-derived, NOT CODATA; mirrors codata_2022_source.M_N_MEV
M_N_MEV_ERR_STR = "0.00000060"
M_N_MEV     = float(M_N_MEV_STR)
M_N_MEV_ERR = float(M_N_MEV_ERR_STR)

# β-decay endpoint Q-value (n → p + e⁻ + ν̄):
#   Q_β = m_n − m_p − m_e   (m_ν ≈ 0 in the rest mass budget)
#
# Computed in mpf and downcast ONCE, not accumulated in binary64. This is a
# catastrophic cancellation — 0.78 MeV as the difference of numbers near 939 —
# so the old `M_N_MEV - M_P_MEV - M_E_MEV` lost about three decimal digits.
# The exposed float is unchanged in type and now correctly rounded; the `_STR`
# companions carry the full-precision value for mpmath consumers.
#
# `workdps` is load-bearing, not decoration. Module import happens at the
# mpmath default of dps=15, so a bare `_mp.mpf("939.56542179")` here builds a
# binary53 value and `nstr(..., 50)` then prints ITS expansion — a float64
# number wearing 50 digits. Caught while writing this: the first version
# emitted `Q_NEUTRON_MEV_STR = 0.78233340930990846739945254739723168313503...`
# (the binary64 tail `...380859`) instead of the exact `0.78233340931`. That
# is the `mp.dps` no-op that scripts/precision-gates.sh gates on, reproduced
# inside the fix meant to remove a float64 path.
with _mp.workdps(_DPS_DEFAULT):
    _q_n_mp = (
        _mp.mpf(M_N_MEV_STR) - _mp.mpf(M_P_MEV_STR) - _mp.mpf(M_E_MEV_STR)
    )
    _q_n_err_mp = _mp.sqrt(
        _mp.mpf(M_N_MEV_ERR_STR) ** 2
        + _mp.mpf(M_P_MEV_ERR_STR) ** 2
        + _mp.mpf(M_E_MEV_ERR_STR) ** 2
    )
    Q_NEUTRON_MEV_STR     = _mp.nstr(_q_n_mp, _DPS_DEFAULT, strip_zeros=False)
    Q_NEUTRON_MEV_ERR_STR = _mp.nstr(_q_n_err_mp, _DPS_DEFAULT, strip_zeros=False)
Q_NEUTRON_MEV     = float(_q_n_mp)                      # ≈ 0.78233341 MeV
Q_NEUTRON_MEV_ERR = float(_q_n_err_mp)

# ── Knot-volume constants (math; SnapPy-verified) ─────────────
# Catalan's constant G = Σ (-1)^k / (2k+1)², used in figure-8 and
# Borromean hyperbolic volumes.  These f64 values are accurate to
# machine epsilon; the substrate cluster's knot_volumes.py carries
# the mpmath versions if higher precision is needed.
CATALAN_G       = 0.9159655941772190     # ± < f64 ε
VOL_BORROMEAN   = 8.0 * CATALAN_G        # 7.32772475… (8·G exactly)
VOL_4_1         = VOL_FIGURE_EIGHT        # alias: figure-8 = 4_1 in Rolfsen


if __name__ == "__main__":
    print(f"Substrate parameter q (canonical, m_p-pinned 2026-05-28)")
    print(f"  Vol(4_1)   = {VOL_FIGURE_EIGHT} (math constant)")
    print(f"  m_p/m_e    = {MASS_RATIO_P_E} ± {MASS_RATIO_P_E_ERR}  [ANCHOR]")
    print(f"  m_μ/m_e    = {MASS_RATIO_MU_E} ± {MASS_RATIO_MU_E_ERR}  [now a prediction, 9.5σ]")
    print(f"  ℏ_q²       = {HBAR_Q_SQ:.15f}")
    print(f"  ℏ_q        = {HBAR_Q:.15f}")
    print(f"  q          = {Q:.15f} ± {Q_ERR:.2e}")
    print(f"  q⁻¹        = {Q_INV:.15f} ± {Q_INV_ERR:.2e}")
    print(f"  q - q⁻¹    = {HA:.15f} ± {HA_ERR:.2e}")
    print(f"  E_×        = {E_CROSS:.15f} ± {E_CROSS_ERR:.2e}")
    print(f"  s          = {S_SKEIN:.15f} ± {S_SKEIN_ERR:.2e}")
    print(f"  [2]_q      = {TWO_Q:.15f} ± {TWO_Q_ERR:.2e}")
    print(f"  tanh(ln q) = {TANH_LN_Q:.15f} ± {TANH_LN_Q_ERR:.2e}")
    print(f"  [9]_q      = {q_int(9):.10f} ± {q_int_err(9):.2e}")
    print(f"  [10]_q     = {q_int(10):.10f} ± {q_int_err(10):.2e}")
    alpha = Q_INV / (q_int(9) * q_int(10))
    inv_alpha = 1.0 / alpha
    # α error: dα/dq involves all three factors
    alpha_err = alpha * math.sqrt((Q_INV_ERR/Q_INV)**2
                                  + (q_int_err(9)/q_int(9))**2
                                  + (q_int_err(10)/q_int(10))**2)
    print(f"  α          = {alpha:.10f} ± {alpha_err:.2e}")
    print(f"  1/α        = {inv_alpha:.6f} ± {inv_alpha**2 * alpha_err:.4f}")
    _ainv = _codata("inverse fine-structure constant")
    print(f"  CODATA 1/α = {_ainv.value_str} ± {_ainv.uncertainty_str}")
    print(f"  Rational:    {Q_RAT_NUM}/{Q_RAT_DEN}")
