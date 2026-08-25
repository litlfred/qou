"""Canonical physical + algebraic constants for the QOU mass pipeline.

**M2 inversion (FINAL constants cluster of 2b Phase B)**: this module
owns the canonical α-EM derivation block, the figure-eight BW
modification constants, the molecular energy scales, and the E_0
calibration constant — the last surface remaining in `hecke_core.py`
that wasn't already pyhecke-owned.

After this PR, hecke_core.py is a **pure back-compat shim** —
~150 LOC of re-exports from pyhecke modules. The canonical surface
is 100 % pyhecke-owned.

Symbols owned by this module:

  α-EM derivation block (private intermediates + public outputs):
    q2, _bare_alpha_em, _bare_alpha_inv,
    _CS_T29, _CS_T35, _hbar_q2, _n2, _c1,
    _sl, _linking, _G_cl_11, _G_cl_22, _G_cl_12, _det_G_cl,
    _linking_q, _CS_q_29, _CS_q_35,
    _sl_q_29, _sl_q_35, _G_q_11, _G_q_22, _G_q_12, _det_G_q,
    _kappa_gram,
    ALPHA_EM_INV_DERIVED, alpha_em, alpha_em_derived

  Knot-volume binding scales:
    ALPHA_BORROMEAN, ALPHA_FIGURE8, ALPHA

  Electron traced volume (mass-tower formula):
    _a_e, _b_e, V_HAT_ELECTRON

  Figure-eight BW scaling factors:
    FIG8_A_BULK, FIG8_F_COUL, FIG8_F_EXCH,
    FIG8_R_311, FIG8_R_32, FIG8_R_41

  Molecular energy scales:
    E_HARTREE_EV, TWO_Q, E_MOL, KAPPA

  E_0 calibration (from CODATA-derived Q_β(n)):
    E_0_CALIBRATION_MEV, E_0_CALIBRATION_MEV_ERR
"""

from __future__ import annotations

import math

# Substrate (qou-substrate is the canonical owner of q0 / qi / h /
# q_int; the q_parameter.py back-compat shim re-exports them.)
try:
    from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int  # type: ignore[import-not-found]
except ImportError:
    from qou_substrate.constants import (  # type: ignore[import-not-found]
        Q as q0, Q_INV as qi, HA as h, q_int,
    )

# Gram primitives — pyhecke owns these (M2b inversion).
from pyhecke.gram import (  # type: ignore[import-not-found]
    z, W_SYM, W_STD, W_ALT,
)

# Experimental + knot-volume constants live in folio-assistant/
# computations/ for now (not yet pyhecke-owned). Pull through the
# legacy bridge.
from . import _legacy  # noqa: F401 — sys.path bridge
# Prefer the in-repo `computations/substrate/`
# (re-exported via flat-name `experimental_constants` / `knot_volumes`
# shims that _legacy adds to sys.path).  Fall back to qou_substrate
# (PyPI wheel) when pyhecke runs outside the repo — Pyodide, Sage,
# user installs.  Same chain `gram.py` and the first block of this
# file already use for q_parameter; consistency is what keeps the
# multi-environment compatibility going.
try:
    from experimental_constants import (  # type: ignore[import-not-found]
        M_E_MEV, M_P_MEV, M_N_MEV,
        Q_NEUTRON_MEV as _Q_NEUTRON_MEV,
        Q_NEUTRON_MEV_ERR as _Q_NEUTRON_MEV_ERR,
    )
    from knot_volumes import (  # type: ignore[import-not-found]
        CATALAN_G,
        VOL_BORROMEAN,
        VOL_4_1 as VOL_FIGURE8,  # legacy alias preserved
    )
except ImportError:
    from qou_substrate.constants import (  # type: ignore[import-not-found]
        M_E_MEV, M_P_MEV, M_N_MEV,
        Q_NEUTRON_MEV as _Q_NEUTRON_MEV,
        Q_NEUTRON_MEV_ERR as _Q_NEUTRON_MEV_ERR,
        CATALAN_G,
        VOL_BORROMEAN,
        VOL_FIGURE_EIGHT as VOL_FIGURE8,
    )


# ── Substrate q^2 ──
q2 = q0**2  # kept for local alpha_em derivation


# ── Fine structure constant ──
# α_EM enters the physics through THREE channels:
#   1. Coulomb term (term 3): uses HA·[6]_q·m_e, NOT α_EM.
#      The nuclear Coulomb interaction is encoded in the pp crossing eigenvalue.
#   2. Molecular binding: uses E_HARTREE = m_e·c²·α² → USES corrected α.
#   3. Half-lives: uses α_EM in Fermi phase space (Sommerfeld factor) → USES corrected α.
#
# Bare value (Hecke algebra projection, no CS correction).
# This is the multiplicative-chain identity from
# prop:alpha-em-shift-multiplicative-chain:
#   α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q
#          = q · [9]_q · [10]_q
# where α_shift(T_{p,k}) = k(p-1) on V_{(1^p)} per
# prop:alpha-shift-torus-knot. Verified to 50 dps in
# computations/alpha-em-shift-multiplicative-chain.witness.json
_bare_alpha_em = qi / (q_int(9) * q_int(10))
_bare_alpha_inv = q0 * q_int(9) * q_int(10)

# CS-corrected value with Gram matrix κ from J²(Bring's surface):
# 1/α = bare × (1 + c₁ + c₁²×κ) where:
#   c₁ = (CS₁+CS₂)·([2]_q/2)·ℏ_q²/bare  (J¹ correction)
#   κ = det(G_CS_classical)/det(G_CS_q)    (J² correction from Gram ratio)
#
# G_CS encodes the CS pairing of T_{2,9}∪T_{3,5} on Bring's surface:
#   Diagonal: CS + self-linking²/crossing²
#   Off-diagonal: mutual CS from linking number |2×5-3×9|=17
_CS_T29 = math.pi**2 * 10.0/9.0       # CS(T_{2,9}) = π²(m²-1)(n²-1)/(12mn)
_CS_T35 = math.pi**2 * 16.0/15.0      # CS(T_{3,5})
_hbar_q2 = (1.0 - qi)**2               # ℏ_q²
_n2 = q_int(2)
_c1 = (_CS_T29 + _CS_T35) * (_n2/2.0) * _hbar_q2 / _bare_alpha_inv

# Gram matrix of CS pairing (classical)
_sl = 8  # self-linking = (m-1)(n-1) for both T_{2,9} and T_{3,5}
_linking = 17  # |2×5-3×9|
_G_cl_11 = _CS_T29 + math.pi**2 * _sl**2 / (2*9)**2
_G_cl_22 = _CS_T35 + math.pi**2 * _sl**2 / (3*5)**2
_G_cl_12 = math.pi**2 * _linking**2 / (2*9 * 3*5)
_det_G_cl = _G_cl_11 * _G_cl_22 - _G_cl_12**2

# Gram matrix (q-deformed: replace m,n with [m],[n])
_linking_q = abs(_n2*q_int(5) - q_int(3)*q_int(9))
_CS_q_29 = math.pi**2 * (_n2**2-1)*(q_int(9)**2-1)/(12*_n2*q_int(9))
_CS_q_35 = math.pi**2 * (q_int(3)**2-1)*(q_int(5)**2-1)/(12*q_int(3)*q_int(5))
_sl_q_29 = (_n2-1)*(q_int(9)-1)
_sl_q_35 = (q_int(3)-1)*(q_int(5)-1)
_G_q_11 = _CS_q_29 + math.pi**2 * _sl_q_29**2 / (_n2*q_int(9))**2
_G_q_22 = _CS_q_35 + math.pi**2 * _sl_q_35**2 / (q_int(3)*q_int(5))**2
_G_q_12 = math.pi**2 * _linking_q**2 / (_n2*q_int(9) * q_int(3)*q_int(5))
_det_G_q = _G_q_11 * _G_q_22 - _G_q_12**2

_kappa_gram = _det_G_cl / _det_G_q  # J² self-dual damping factor

# ── The CS tower is geometric — sum it exactly, do not truncate ──────
#
# The correction tower is  Σ_{j≥1} c₁^j κ^{j−1}, i.e. c₁ times a geometric
# series of ratio c₁·κ. It therefore has a closed form:
#
#     1 + Σ_{j≥1} c₁^j κ^{j−1}  =  1 + c₁/(1 − c₁κ)
#
# whose expansion is 1 + c₁ + c₁²κ + c₁³κ² + …, reproducing the previous
# order-2 truncation as its first three terms.
#
# This file previously shipped that order-2 truncation
# (`1 + _c1 + _c1**2 * _kappa_gram`). At the substrate anchor the ratio is
# c₁·κ ≈ 2.7e-3, so truncating cost **11.06 ppb** — significant for a
# constant consumed by ppb-level claims. The exact form is no more
# expensive to evaluate and has no order parameter to get wrong.
def _alpha_em_tower(c1, kappa):
    """Exact resummation of the CS correction tower (all orders)."""
    return 1.0 + c1 / (1.0 - c1 * kappa)


ALPHA_EM_INV_DERIVED = _bare_alpha_inv * _alpha_em_tower(_c1, _kappa_gram)
# ≈ 137.0359350940 at the proton-pinned substrate anchor.
#
# NOTE ON THE ANCHOR: this is proton-pinned (`Q` from qou-substrate is
# `_solve_q_proton_f64`, re-pinned 2026-05-28). A stale comment here used to
# read "= 137.035944 (55 ppb, 0.00004% error)"; that value is the MUON-anchor
# evaluation from before the re-pin — the two anchors differ by 11.5 ppb in q,
# which is ~200 ppb in α_em⁻¹ because bare ~ q·[9]_q·[10]_q is high degree.
# The "55 ppb" was additionally inconsistent with the "0.00004%" in the same
# comment (0.00004% is 400 ppb). Against CODATA 137.035999177 the current
# value sits at ≈ −468 ppb, and that residual is STRUCTURAL: the tower is
# converged, so no further orders can close it.


def alpha_em_inv_mp(dps: int = 50):
    """Arbitrary-precision α_EM⁻¹ via mpmath, exactly resummed.

    The float64 path above is accurate for this constant (it agrees with
    this function to ~13 digits — the arithmetic is short and well
    conditioned). This exists so callers making ppb- or ppq-level claims
    need not rely on that agreement holding, per the repo's precision
    discipline.
    """
    import mpmath as _mp
    with _mp.workdps(dps):
        try:
            from q_parameter import Q_50_DIGIT_STR as _qs
        except ImportError:
            from qou_substrate.constants import Q_50_DIGIT_STR as _qs
        q = _mp.mpf(_qs)
        qi_ = 1 / q

        def _qint(k):
            return (q**k - q**(-k)) / (q - 1 / q)

        pi = _mp.pi
        bare = q * _qint(9) * _qint(10)
        cs29 = pi**2 * _mp.mpf(10) / 9
        cs35 = pi**2 * _mp.mpf(16) / 15
        n2 = _qint(2)
        c1 = (cs29 + cs35) * (n2 / 2) * (1 - qi_)**2 / bare

        g_cl_11 = cs29 + pi**2 * 64 / _mp.mpf(18)**2
        g_cl_22 = cs35 + pi**2 * 64 / _mp.mpf(15)**2
        g_cl_12 = pi**2 * 289 / (_mp.mpf(18) * 15)
        det_cl = g_cl_11 * g_cl_22 - g_cl_12**2

        lk_q = abs(n2 * _qint(5) - _qint(3) * _qint(9))
        cs_q_29 = pi**2 * (n2**2 - 1) * (_qint(9)**2 - 1) / (12 * n2 * _qint(9))
        cs_q_35 = (pi**2 * (_qint(3)**2 - 1) * (_qint(5)**2 - 1)
                   / (12 * _qint(3) * _qint(5)))
        sl_q_29 = (n2 - 1) * (_qint(9) - 1)
        sl_q_35 = (_qint(3) - 1) * (_qint(5) - 1)
        g_q_11 = cs_q_29 + pi**2 * sl_q_29**2 / (n2 * _qint(9))**2
        g_q_22 = cs_q_35 + pi**2 * sl_q_35**2 / (_qint(3) * _qint(5))**2
        g_q_12 = pi**2 * lk_q**2 / (n2 * _qint(9) * _qint(3) * _qint(5))
        det_q = g_q_11 * g_q_22 - g_q_12**2

        kappa = det_cl / det_q
        return +(bare * (1 + c1 / (1 - c1 * kappa)))


# Canonical α_EM: the CS-corrected value is physical
alpha_em = 1.0 / ALPHA_EM_INV_DERIVED
alpha_em_derived = alpha_em  # alias for backward compatibility


# ── Knot-volume binding scales ──
ALPHA_BORROMEAN = M_E_MEV * VOL_BORROMEAN          # binding scale for Borromean-like nuclei
ALPHA_FIGURE8 = M_E_MEV * VOL_FIGURE8             # binding scale for figure-8-like nuclei
ALPHA = ALPHA_BORROMEAN                             # default (backward compat)


# ── Electron traced volume V̂_e (mass-tower formula) ──
# Trefoil σ³ on 2 strands (1 generator), 3 crossings (c=1, d=0).
# V̂_e = W_SYM×q³ + W_STD×V_std + W_ALT×(-1/q)³
# where V_std = z·a+b from transfer matrix T(1,0)³.
# This is the SAME V̂ that gives m_p/m_e = 1870 in the mass-tower.
# B(D) = α × V̂_e (deuteron binding = Borromean scale × electron action).
# Reference: prop:mass-endomorphism-tower
_a_e, _b_e = 0.0, 1.0
for _ in range(3):
    _a_e, _b_e = _a_e * h + _b_e, _a_e
V_HAT_ELECTRON = W_SYM * q0**3 + W_STD * (z * _a_e + _b_e) + W_ALT * (-qi)**3


# ── Figure-eight BW scaling factors ──
# Each NF basis element lives at a jet level determined by word length:
#   J⁰: γ (length 0) → unknot, Vol=0, CS=0
#   J¹: σ₀, σ₁ (length 1) → unknot, Vol=0, CS=0
#   J²: L₊, L₋ (length 2) → Hopf link, torus, CS=π²/6
#   J³: e⁻ (length 3) → trefoil T₂₃, torus, CS=π²/3
#
# FIGURE-EIGHT BW MODIFICATION (Wedderburn-Artin theorem):
# The figure-eight 4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁ has character in the standard
# representation of H₃(q):
#   χ(4₁, [2,1]) = 2 - [3]_q = -1 - h²
# while the Borromean B₃ = (σ₀σ₁⁻¹)³ has χ(B₃, [2,1]) ≈ 2 (near-identity).
FIG8_A_BULK = 1.0 - h**2                # = 4 - [3]_q ≈ 0.956 (bulk: vol, surf, asym)
FIG8_F_COUL = z**2 * q_int(3) / q_int(2) # = z²[3]/[2] ≈ 0.377 (Coulomb)
FIG8_F_EXCH = z                           # = 1/(√q+1/√q) ≈ 0.499 (exchange)
# Character ratios for higher-level corrections (4₁ vs B₃):
FIG8_R_311 = -2 * h**2 / (6 - 2 * h**2 + 6 * h**2)  # [3,1,1] ratio ≈ -0.015
FIG8_R_32  = (-1 - 2*h**2) / (5 - 2*h**2 + 5*h**2)   # [3,2] ratio ≈ -0.218
FIG8_R_41  = (1 - h**2) / (4 - h**2 + 4*h**2)          # [4,1] ratio ≈ 0.239


# ── Molecular energy scales ──
# Use the CS-corrected alpha_em above (NOT bare α).
E_HARTREE_EV = 511000.0 * alpha_em**2  # Hartree energy (eV)
TWO_Q = q0 + qi
E_MOL = E_HARTREE_EV / TWO_Q**2  # molecular energy unit (eV)
KAPPA = M_E_MEV                    # nuclear binding scale (MeV)


# ── E_0 calibration ──
# Free-neutron β-decay Q-value, derived from CODATA 2022:
#   Q_β(n) = m_n - m_p - m_e = 0.78233341 ± 6.1×10⁻⁷ MeV
# Authoritative source: experimental_constants.Q_NEUTRON_MEV (computed
# from CODATA mass constituents, not hardcoded). Audited by
# `e0_calibration_audit.py`.
#
# NAME WARNING — this constant is Q_beta(n), NOT the hadronic scale E_0.
#
# `prop:three-calibration-inputs` and its context note give
#     E_0 = m_e / (q_0 (q_0 - 1))            ~ 4.186 MeV   (CAL-1 + CAL-2)
#     Q_beta(n) = |Delta(net)| * E_0         ~ 0.782 MeV   (CAL-2 proxy)
#     Delta(net) = h (2 - h) / 2,  h = hbar_q
# and state outright that "E_0 != Q_beta(n) ... they differ by the
# dimensionless factor 1/|Delta(net)| ~ 5.31". Measured here: 5.3417 from the
# closed form, 5.3506 from the two numbers. `e0_calibration_audit.py` agrees —
# it defines "E_0 = Q_beta(n) / |Delta(net)|". This binding drops that division.
#
# The value is RIGHT (it is Q_beta); only the name is wrong, and the name is
# load-bearing: `mass_at_3A_proper.binding_3A(E_0=E_0_CALIBRATION_MEV)` scales
# every binding by a quantity ~5.34x too small, which is most of why that path
# reports -85% on the deuteron.
#
# `binding_canonical.py` already documents this exact trap in its own
# "Naming note (2026-05-17)": *"Earlier revisions misnamed this parameter
# `E_0`; the value used here is correct ... only the name was wrong."* The
# rename never reached here.
#
# NOT renamed in place: ~25 modules import `E_0_CALIBRATION_MEV`, and swapping
# the binding would silently change every one of their published numbers. The
# truthful name is added alongside; migration is per-caller and belongs with
# the scale decision (bean qou-2tuv), not with a constants-file edit.
Q_BETA_N_MEV     = _Q_NEUTRON_MEV
Q_BETA_N_MEV_ERR = _Q_NEUTRON_MEV_ERR

#: DEPRECATED ALIAS of `Q_BETA_N_MEV`. Misnomer — see the note above. New code
#: should import `Q_BETA_N_MEV` when it wants the beta-decay Q-value, and build
#: the hadronic scale as `m_e / (q_0 * (q_0 - 1))` when it wants E_0.
E_0_CALIBRATION_MEV     = Q_BETA_N_MEV
E_0_CALIBRATION_MEV_ERR = Q_BETA_N_MEV_ERR


__all__ = [
    # Substrate
    "q2",
    # α-EM
    "ALPHA_EM_INV_DERIVED", "alpha_em", "alpha_em_derived",
    # Knot-volume scales
    "ALPHA_BORROMEAN", "ALPHA_FIGURE8", "ALPHA",
    "CATALAN_G", "VOL_BORROMEAN", "VOL_FIGURE8",
    # Electron volume
    "V_HAT_ELECTRON",
    # FIG8
    "FIG8_A_BULK", "FIG8_F_COUL", "FIG8_F_EXCH",
    "FIG8_R_311", "FIG8_R_32", "FIG8_R_41",
    # Energy scales
    "E_HARTREE_EV", "TWO_Q", "E_MOL", "KAPPA",
    # E_0
    "Q_BETA_N_MEV", "Q_BETA_N_MEV_ERR",
    "E_0_CALIBRATION_MEV", "E_0_CALIBRATION_MEV_ERR",  # deprecated aliases
    # Mass constants (re-exported for one-stop convenience)
    "M_E_MEV", "M_P_MEV", "M_N_MEV",
]
