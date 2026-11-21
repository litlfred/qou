"""
Experimental constants with EXPLICIT uncertainties.

Every observed value has a central value AND an uncertainty.
No observed value may appear without ±.

Sources:
  CODATA 2022: https://physics.nist.gov/cuu/Constants/
  NNDC/ENSDF:  https://www.nndc.bnl.gov/ensdf/
  PDG 2024:    https://pdg.lbl.gov/
  SnapPy 3.3.2: https://snappy.math.uic.edu/

Usage:
    from experimental_constants import *

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""


# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

# ── Fundamental constants (CODATA 2022) ─────────────────────────
# Single source of truth: codata_2022_source.M_E_MEV = 0.51099895069(15)
# MeV (full 11-sig-fig CODATA-2022; same module codata_constants.py
# imports from). READ from the registry -- this file already did so for
# M_E_MEV and hardcoded everything else, which is how the CODATA-2018
# values below survived under 2022 labels (drain qou-7ot6-a, 2026-08-21).
#
# THESE ARE mpf, NOT float (changed 2026-08-29, bean qou-p77d).
#
# Until now every one of them was wrapped in `float()` on import, with the
# stated reason: "so the ~266 importers' float arithmetic / json.dumps stay
# intact (an mpf would break json.dumps)". That cast was the upstream cause
# of a whole class of float64 defects -- 291 non-integral float64 fields at
# `.assertions[].computed/.expected` across 57 producers, because a producer
# starting from these constants is float64 end to end however much mpmath it
# calls afterwards. `channel_product_mass.py` is the clearest case: it
# computes `Z*M_P_MEV + N*m_n + Z*me` in pure binary64 and then wraps the
# answer in `mp.log`, which cannot restore what was never there.
#
# The reason was measured before it was removed
# (`computations/audits/experimental_constants_float64_rationale_probe.py`)
# and is HALF TRUE, which is why it survived so long:
#
#   * "an mpf would break json.dumps" -- REAL for a bare `json.dumps`, and
#     there are hand-rolled ones in the tree. NOT true of the witness path,
#     which is where these fields come from: `qou_substrate/witness.py`
#     serializes with `json.dump(..., default=str)`, which renders an mpf at
#     full precision. So the reason never covered the case it was invoked for.
#   * "the importers' float arithmetic stays intact" -- mpf interoperates
#     with float for arithmetic and comparison -- but NOT with f-string format
#     specs. MEASURED 2026-09-07, operation by operation:
#         x * 3.0      OK        3.0 / x      OK        x < 1.0   OK
#         f"{x}"       OK        "%.6f" % x   OK
#         f"{x:.6f}"   TypeError: unsupported format string passed to mpf.__format__
#         format(x, ".6f")  same TypeError
#     So the clause "and f-string formatting" was wrong, and it is the clause
#     that bites: `{x:.3f}` in a table column is exactly the shape that made
#     three producers un-runnable (qou-9q4h, merged in #6971). `"%.6f" % x`
#     does work -- but it SILENTLY DOWNCASTS, byte-identical to `float(x)`, so
#     it is a display route and never a value route. (Not a gate blind spot:
#     `f64_into_mpmath_audit._is_display_only` already classifies `str % x` as
#     a display sink, which is correct.)
#   * "~266 importers" -- 213 live (+4 in the generated qou-mass mirror).
#     This figure is on its SECOND correction: the original "~266" was fixed to
#     "204", and 204 has since decayed to 213. Re-measure it with
#     `computations/audits/experimental_constants_float64_rationale_probe.py`
#     rather than trusting this line.
#
# THE ONE REAL HAZARD, and it is silent: `math.log(mpf)` and friends do NOT
# raise, they DOWNCAST. A module doing `import math` and calling `math.sqrt`
# on one of these values still gets binary64, with no error to notice. This
# module's own `Q_NEUTRON_MEV_ERR` did exactly that and is fixed below; any
# consumer wanting full precision must use `mpmath` equivalents.
from codata_2022_source import (  # noqa: E402
    M_E_MEV as _M_E_MEV,
    M_E_MEV_ERR as _M_E_MEV_ERR,
    M_P_MEV as _M_P_MEV,
    M_P_MEV_ERR as _M_P_MEV_ERR,
    M_N_MEV as _M_N_MEV,
    M_N_MEV_ERR as _M_N_MEV_ERR,
    M_N_MINUS_P_MEV as _M_N_MINUS_P_MEV,
    M_N_MINUS_P_MEV_ERR as _M_N_MINUS_P_MEV_ERR,
    M_MU_OVER_M_E as _M_MU_OVER_M_E,
    M_MU_OVER_M_E_ERR as _M_MU_OVER_M_E_ERR,
)
M_E_MEV     = _M_E_MEV
M_E_MEV_ERR = _M_E_MEV_ERR   # was 0.00000000015; table says ...16

# Energy scale for Q-values: κ = m_e / 3
# This is E_× × μ₀ where E_× = ½(q−q⁻¹)×m_e c² and μ₀ = m_e/(3×E_×).
KAPPA       = M_E_MEV / 3.0   # 0.170333 MeV

M_P_MEV     = _M_P_MEV       # was M_P_MEV_VALIDATION (CODATA-2018)
M_P_MEV_ERR = _M_P_MEV_ERR

# NOTE: the registry's M_N_MEV is the AME-DERIVED neutron mass
# (939.56542179), not the CODATA-direct 939.56542194. That is the corpus's
# deliberate choice -- see codata_2022_source -- so reading the registry
# follows it rather than the raw table. The literal here was 939.56542052,
# the CODATA-2018 DIRECT value: wrong edition and wrong determination.
M_N_MEV     = _M_N_MEV
M_N_MEV_ERR = _M_N_MEV_ERR

# ── Free neutron beta-decay Q-value (CODATA 2022) ────────────────
# n → p + e⁻ + ν̄ₑ,  Q = m_n − m_p − m_e
#
# Derived from individual CODATA 2022 mass-energy equivalents above.
# Cross-checked against the CODATA-listed neutron–proton mass difference:
#   m_n − m_p = 1.2933321 ± 0.0000005 MeV/c²
#   Source: https://physics.nist.gov/cgi-bin/cuu/Value?mnmpm
#   CODATA 2022, NIST Physics Laboratory, Gaithersburg MD 20899 USA
#
# Q_NEUTRON = m_n − m_p − m_e
#           = 939.56542052 − 938.27208816 − 0.51099895000
#           = 0.78233341 MeV
# δQ = sqrt(δm_n² + δm_p² + δm_e²)
#    = sqrt(5.4e-7² + 2.9e-7² + 1.5e-16²) ≈ 6.1e-7 MeV
# Was the literal 1.2933321 labelled "direct CODATA 2022 value" -- 320 ppb
# from the actual 2022 entry (1.29333251). Now read from the registry, where
# codata_table_vintage_audit checks it against the NIST table.
M_N_MINUS_P_MEV     = _M_N_MINUS_P_MEV
M_N_MINUS_P_MEV_ERR = _M_N_MINUS_P_MEV_ERR

# Computed below, inside the precision pin (it was here, at the importer's ambient
# dps -- 53-bit on a default import, so it held a binary64 value in an mpf).
# `_math.sqrt` here, on three mpf arguments, is the exact hazard named in the
# header: it does not raise, it returns a binary64 float. So the quadrature
# sum was silently the one float64 quantity left in this module the moment the
# casts came off. `_mpm.sqrt` keeps it mpf.
import mpmath as _mpm  # noqa: E402

# --- PRECISION PIN -----------------------------------------------------------------------------
# Every mpf below is built inside `_mpm.workdps(_CONST_DPS)`, so these constants carry the SAME
# digits no matter what precision the importer happened to have.
#
# WHY THIS IS NEEDED, MEASURED. Without it the module builds at the caller's AMBIENT dps, which
# for a fresh importer is mpmath's default 15. `VOL_FIGURE_EIGHT = 2*clsin(2, pi/3)` -- the value
# #6904 exactified precisely so it would stop being a float64 -- then came out **6.995e-17
# relative from true** on a default import, and exact only if the importer happened to raise dps
# BEFORE the import. Same file, same commit, two different values depending on import order,
# across 213 importers. Exactifying a constant does not help if it is then evaluated at binary64
# precision, and nothing in the module said which precision it was evaluated at.
#
# 60 dps is above `qou_substrate.precision`'s 50-dps compute floor with room to spare; an mpf is a
# fixed binary object once built, so a lower-precision consumer rounds it in arithmetic exactly as
# it rounds anything else.
_CONST_DPS = 60
# -----------------------------------------------------------------------------------------------
from codata_constants import M_P_MEV_VALIDATION
with _mpm.workdps(_CONST_DPS):
    # Inside the pin: at ambient dps-15 both differences below were binary64 values in an mpf
    # (measured 2026-10-05: m_n_derived_3input == mpf(float(...)) was True and it differed from
    # M_N_MEV, the value the comment below says it equals by construction).
    Q_NEUTRON_MEV     = M_N_MEV - M_P_MEV - M_E_MEV            # 0.78233341 MeV
    Q_NEUTRON_MEV_ERR = _mpm.sqrt(M_N_MEV_ERR**2 + M_P_MEV_ERR**2 + M_E_MEV_ERR**2)

# m_n via the 3-input scheme (m_n = m_p + Q_β + m_e) — the canonical anchor
# list pins m_p, m_e and the β-decay sector, deriving m_n rather than using
# it as a 4th input. Numerically identical to M_N_MEV by construction
# (Q_NEUTRON_MEV = M_N_MEV − M_P_MEV − M_E_MEV), so this is the same CODATA
# value, named for the 3-input consumers. Restores the missing export that
# delta_lambda_empirical_tabulation.py imports (bean t2vq).
with _mpm.workdps(_CONST_DPS):
    m_n_derived_3input = M_P_MEV + Q_NEUTRON_MEV + M_E_MEV     # = M_N_MEV

# NO FLOAT (owner ruling, 2026-09-07). The CODATA masses were flipped to mpf
# earlier; these four were the residue, and they were bare binary64 literals
# rather than casts -- so float64 round-tripped their digits and no VALUE was
# lost, but every consumer inherited a 17-digit floor it had to know to undo
# with `mpf(str(...))`. Carrying them as mpf removes the floor at the source.
#
# Measured before flipping: ZERO f-string format-spec uses across all four
# (17 + 6 + 4 + 4 importers), so the `f"{x:.6f}"` break that made three
# producers un-runnable in qou-9q4h has no site to fire at here.
with _mpm.workdps(_CONST_DPS):
    G_F_MEV     = _mpm.mpf("1.1663787e-11")   # ± 0.0000006e-11 MeV⁻²; CODATA 2022 (library/codata-2022/values.json). Was 1.1663788 (the PDG value), 2026-11-20.
    G_F_MEV_ERR = _mpm.mpf("0.0000006e-11")

# DERIVED EXACTLY, not stored. Since the 2019 SI redefinition both h and e are
# exact defining constants, so hbar in MeV·s = h / (2 pi) / (e · 1e6) is exact
# to any precision -- irrational only through pi. The stored 6.582119569e-22
# was a 10-digit TRUNCATION of that, 7.734e-11 relative from the true value,
# while the line's own comment said "exact in SI since 2019" and the ERR below
# says 0.0. The corpus already knew it was exact and stored it truncated --
# the same shape as the Vol(4₁) float64 this file carried until #6904
# (bean qou-9ies).
with _mpm.workdps(_CONST_DPS):
    _H_SI_EXACT = _mpm.mpf("6.62607015e-34")    # J·s,  exact by SI definition
    _E_SI_EXACT = _mpm.mpf("1.602176634e-19")   # C,    exact by SI definition
    HBAR_MEV_S  = _H_SI_EXACT / (2 * _mpm.pi) / (_E_SI_EXACT * _mpm.mpf("1e6"))
    HBAR_MEV_S_ERR = _mpm.mpf(0)  # exact by definition -- and now actually exact

# noqa: P31 - DELIBERATE determination choice, not a stale edition. The
# Cs-recoil value is retained on purpose; CODATA-2022 would be a
# different determination, not merely newer digits.
with _mpm.workdps(_CONST_DPS):
    ALPHA_EM_INV     = _mpm.mpf("137.035999084")  # noqa: P31 - CODATA 2018, Cs recoil, +/- 21e-9
    ALPHA_EM_INV_ERR = _mpm.mpf("0.000000021")

MU_OVER_E        = _M_MU_OVER_M_E      # was 206.7682830 (CODATA-2018)
MU_OVER_E_ERR    = _M_MU_OVER_M_E_ERR

with _mpm.workdps(_CONST_DPS):
    TAU_OVER_E       = _mpm.mpf("3477.23")   # ± 0.23 (CODATA 2022; m_τ = 1776.86 MeV, m_e = 0.511 MeV)
    TAU_OVER_E_ERR   = _mpm.mpf("0.23")

# ── Molecular bond dissociation energies (experimental comparison) ─
# Observed D_0 values used purely as comparison targets for the
# molecular binding computes — NOT inputs to any derivation.
# Source: NIST Chemistry WebBook (C≡O and N≡N bond dissociation energies).
D0_CO_EV         = 11.09          # eV, observed C≡O dissociation energy
D0_CO_EV_ERR     = 0.01
D0_N2_EV         = 9.79           # eV, observed N≡N dissociation (pure-covalent triple)
D0_N2_EV_ERR     = 0.01
D0_H2_EV         = 4.478          # ± 0.001, observed H–H bond dissociation (H₂)
D0_H2_EV_ERR     = 0.001
D0_CC_EV         = 3.60           # ± 0.05, observed C–C single bond (ethane-class)
D0_CC_EV_ERR     = 0.05
D0_CO2_DOUBLE_EV = 8.28           # ± 0.05, CO₂ C=O double-bond comparison (2-bond ref)
D0_CO2_DOUBLE_EV_ERR = 0.05

# ── Molecular bond lengths & resonance (experimental comparison) ───
# Benzene aromatic C–C vs single/double refs (Å); benzene resonance
# energy (kcal/mol). Comparison targets only — NOT inputs.
BOND_LEN_BENZENE_ANG    = 1.40    # ± 0.01, observed aromatic C–C (benzene)
BOND_LEN_CC_SINGLE_ANG  = 1.54    # ± 0.01, C–C single-bond reference
BOND_LEN_CC_DOUBLE_ANG  = 1.34    # ± 0.01, C=C double-bond reference
BENZENE_RESONANCE_KCAL  = 36.0    # ± 1, observed benzene resonance energy (kcal/mol)

# ── Molecular bond angles (experimental comparison) ────────────────
# Observed H–O–H angle and the symmetric tetrahedral reference. Used
# purely as comparison targets for the angle-shift compute — NOT inputs
# to any derivation. Sources: H₂O gas-phase geometry (Hoy & Bunker,
# J. Mol. Spectrosc. 74 (1979); NIST CCCBDB); tetrahedral = arccos(−1/3).
ANGLE_H2O_HOH_DEG         = 104.5     # ± 0.1, observed H–O–H bond angle (water, gas)
ANGLE_H2O_HOH_DEG_ERR     = 0.1
ANGLE_H2O_TETRAHEDRAL_DEG = 109.4712  # arccos(−1/3) in degrees, symmetric reference

G_A_PDG     = 1.2754          # ± 0.0013 (PDG 2024)
G_A_PDG_ERR = 0.0013

# ── Knot volumes (SnapPy 3.3.2) ─────────────────────────────────

# Vol(4_1) = 2·Cl_2(pi/3) is an EXACT closed form, not a SnapPy measurement.
# It sat here as a float64 (1.49e-16 from exact, 0.15x the whole L1 budget for
# one constant) under a "± 1e-12 (numerical precision)" banner, i.e. filed as a
# measured quantity with an uncertainty. Nobody re-measures a measurement,
# which is plausibly why it was never exactified. Bean qou-9ies.
#
# Computed at the caller's ambient precision, so it is exact to whatever dps is
# in force rather than frozen at any digit count.
with _mpm.workdps(_CONST_DPS):
    VOL_FIGURE_EIGHT     = 2 * _mpm.clsin(2, _mpm.pi / 3)
# Retained at 0: an exact constant has no measurement uncertainty, and the term
# is consumed by mass-from-q-symbolic's error budget. Dropping the NAME would
# break that import; giving it a fictitious 1e-12 inflates the budget with an
# uncertainty that does not exist. Measured: the old term was 2.2e-5 of the
# dominant m_mu/m_e term and its removal moves rel_hbar_sq by 2.45e-10
# relative — negligible, which is why this is safe to correct rather than
# something that silently restates a published error bar.
VOL_FIGURE_EIGHT_ERR = 0.0

VOL_THREE_TWIST      = 2.828122088330783  # ± 1e-12
VOL_THREE_TWIST_ERR  = 1e-12

# Borromean rings complement (L6a4). Canonical identity Vol(L6a4) = 8·G
# (Adams 1985). The literal here matches 8·mpmath.catalan at f64 precision.
# Producer witness: `snappy-borromean-volume.witness.json` (single source
# of truth for all precision tiers). Previous f64 value `7.327724753846269`
# was a stale numerical literal that disagreed with 8·G at digit 11;
# corrected in the SnapPy witness migration PR.
VOL_BORROMEAN        = 7.3277247534177521  # = 8·G to f64 precision
VOL_BORROMEAN_ERR    = 1e-15
# 50-dps string form for high-precision mpmath computations (use via
# `mp.mpf(VOL_BORROMEAN_50DPS_STR)` to preserve the full Catalan-constant
# expansion past float's 16-digit floor). Borromean rings complement
# admits the closed form 8 · G where G is Catalan's constant.
# Previous string carried a typo (`587766` instead of `341775` at digit 9);
# corrected to match `8·mpmath.catalan` at the declared precision.
# Authoritative source: `snappy-borromean-volume.witness.json` →
# `alt_precision["50"]`. Consumers should prefer reading from that
# witness rather than this constant; this constant is kept for backward
# compatibility with f64-tier consumers.
VOL_BORROMEAN_50DPS_STR = "7.3277247534177521204368281194590728861931949942534"
# Figure-eight knot complement, closed form Vol(4_1) = 2·Cl₂(π/3) (Thurston).
# Until 2026-08-30 this string agreed with 2·Cl₂(π/3) to only **36**
# significant digits: it ran `2.029883212819307250042405108549040` and then
# diverged at digit 37, continuing `5748300415990989` where the truth
# continues `5718833786150606` — abs err 2.947e-36, under a name promising
# 50. (The bad value is quoted here in two pieces deliberately: spelled as
# one decimal it becomes a fresh false positive in the very audit report
# discussed below.) No consumer wanted 36 digits: three
# probes read it straight into `mp.mpf(...)` and carried a 1e-36 error through
# 50-dps arithmetic that looked exact. Its sibling directly above is genuinely
# good (|VOL_BORROMEAN_50DPS_STR − 8·G| = 2.293e-50), so the two sat adjacent
# at a 14-order-of-magnitude quality difference with nothing saying so.
#
# Why it stood for so long is worth recording, because the usual explanation
# does not apply: `scripts/known-constant-literal-audit.py` scans this path by
# default and HAS been reporting this exact line, correctly, with the right
# first-wrong-digit. The detector was never blind and never mis-aimed. It was
# one of 90 candidates in that report, and nobody worked the pile. A finding
# that is printed and unread fails in the same place as one never generated.
#
# Replaced with the value the substrate computes rather than a retyped one:
# byte-identical to `qou_substrate.constants.VOL_FIGURE_EIGHT_50_STR`, which
# is `nstr(2*clsin(2, pi/3), 50)` evaluated at 60 dps. Gap is now 4.160e-52.
#
# THIS FILE IS THE SOURCE. `qou-mass/src/qou_mass/_internal/
# experimental_constants.py` is a GENERATED mirror of it — flattened and with
# `import _path_bridge` dropped, nothing else — produced by
# `scripts/sync-qou-mass-vendor.py` and gated by its `--check`. Probes under
# `computations/` import this copy; `qou-mass` consumers import the mirror,
# so the defect was live on both paths. Edit here and re-run `--apply`; never
# hand-edit the mirror.
VOL_4_1_50DPS_STR       = "2.0298832128193072500424051085490405718833786150606"

# ── Hyperbolic-knot volumes (used by per_atom_rho_deviation and
#    downstream Z=N ρ-correction probes — pulled from #523). ──
# Stored as Python floats (≈15-decimal-digit precision); each
# value carries an explicit `*_ERR` upper bound on the f64 storage
# error (per the module's "every observed value has central +
# uncertainty" convention). For true high-precision (50 dp+)
# evaluation, callers should compute via SnapPy / mpmath at the
# call site.
# witness-copy-intentional: source constant (SnapPy); downstream witnesses copy it, not
# the reverse.
VOL_6_2          = 4.400832516123046  # SnapPy 6_2 volume
VOL_6_2_ERR      = 1e-15
VOL_8_11         = 8.286316817806593  # SnapPy 8_11 volume
VOL_8_11_ERR     = 1e-15
VOL_L6A4         = 7.3277247534177521  # Borromean = 8·G (per VOL_BORROMEAN above)
VOL_L6A4_ERR     = 1e-15
# witness-copy-intentional: source constant (SnapPy), as VOL_6_2.
VOL_7_SQ_1       = 4.749499981874439  # Whitehead-pair / α-α coupling knot
VOL_7_SQ_1_ERR   = 1e-15
# EIGHT_G defined later (depends on CATALAN constant defined below).

# ── Observed half-lives (NNDC/ENSDF) ────────────────────────────

HALFLIFE_TRITIUM_YR     = 12.32    # ± 0.02 yr
HALFLIFE_TRITIUM_YR_ERR = 0.02

HALFLIFE_C14_YR     = 5730.0      # ± 40 yr
HALFLIFE_C14_YR_ERR = 40.0

HALFLIFE_CO60_YR     = 5.2714     # ± 0.0006 yr
HALFLIFE_CO60_YR_ERR = 0.0006

HALFLIFE_SR90_YR     = 28.79      # ± 0.06 yr
HALFLIFE_SR90_YR_ERR = 0.06

HALFLIFE_CS137_YR     = 30.17     # ± 0.16 yr
HALFLIFE_CS137_YR_ERR = 0.16

HALFLIFE_BI210_D     = 5.012      # ± 0.005 d
HALFLIFE_BI210_D_ERR = 0.005

# ── Observed Q-values (NNDC/ENSDF) ──────────────────────────────

Q_TRITIUM_MEV     = 0.01861       # ± 0.00001 MeV
Q_TRITIUM_MEV_ERR = 0.00001

Q_C14_MEV     = 0.15648           # ± 0.00004 MeV
Q_C14_MEV_ERR = 0.00004

Q_CO60_MEV     = 0.31817          # ± 0.00013 MeV
Q_CO60_MEV_ERR = 0.00013

Q_SR90_MEV     = 0.54590          # ± 0.00007 MeV
Q_SR90_MEV_ERR = 0.00007

Q_CS137_MEV     = 0.51400         # ± 0.00021 MeV
Q_CS137_MEV_ERR = 0.00021

Q_BI210_MEV     = 1.16270         # ± 0.00006 MeV
Q_BI210_MEV_ERR = 0.00006

# ── Observed log ft values (NNDC/ENSDF) ──────────────────────────

LOGFT_TRITIUM     = 3.053         # ± 0.001
LOGFT_TRITIUM_ERR = 0.001

LOGFT_C14     = 9.04              # ± 0.02
LOGFT_C14_ERR = 0.02

LOGFT_CO60     = 7.50             # ± 0.01
LOGFT_CO60_ERR = 0.01

LOGFT_SR90     = 7.63             # ± 0.01
LOGFT_SR90_ERR = 0.01

LOGFT_CS137     = 7.49            # ± 0.02
LOGFT_CS137_ERR = 0.02

LOGFT_BI210     = 7.10            # ± 0.02
LOGFT_BI210_ERR = 0.02

# ── Time conversions (exact) ────────────────────────────────────

SEC_PER_YR  = 3.15576e7           # Julian year (365.25 × 86400), exact by convention
SEC_PER_DAY = 86400.0             # exact

# ── Mathematical constants (exact / high-precision) ─────────────

# Catalan's constant G = sum_{n=0}^∞ (-1)^n / (2n+1)^2 — used in the
# binding-scale calibration α_bind = m_e · 8·G per prop:binding-scale-catalan.
CATALAN     = 0.91596559417721901505460351493238411077  # OEIS A006752, ≥30 dp

# 8·G with G = Catalan's constant — legacy magic-A volume input
# (mass_table_ppb.py historical form; differs from VOL_L6A4 at 1e-9
# because 8·G ≈ 7.32772475341... vs Vol(L6a4) ≈ 7.32772475384...).
# Defined here (not earlier with the other VOL_* constants) so it
# can reference CATALAN as the single source of truth — avoids
# divergence from a duplicated literal (per Copilot review on PR #591).
EIGHT_G     = 8.0 * CATALAN  # ≈ 7.327724753417752
EIGHT_G_ERR = 1e-15

# ── Error propagation helpers ────────────────────────────────────

def rel_err(val, err):
    """Relative error |δx/x|."""
    return abs(err / val) if val != 0 else float('inf')

def prop_power(val, err, n):
    """Propagate through x^n: δ(x^n) = |n| × x^{n-1} × δx."""
    return abs(n) * abs(val)**(n-1) * err

def prop_power_rel(rel, n):
    """Relative error of x^n = |n| × relative error of x."""
    return abs(n) * rel
