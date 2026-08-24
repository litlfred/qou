#!/usr/bin/env python3


# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
3-TERM WEDDERBURN MASS FORMULA — canonical, no fitting.

This module supersedes the previous symmetrised 2-term blend. The
canonical formula uses the full 3-term Wedderburn decomposition that
fully accounts for all three orthogonal channels of the Hecke
algebra H_n(q):

    V_3term(g) = w_sym · λ_sym(g) + w_alt · λ_alt(g) + w_std · V_std(g)

with Wedderburn weights at n=3:

    w_sym = q² / D,   w_std = (q²+1)² / D,   w_alt = q² / D
    D     = q⁴ + 4q² + 1

The three channels (cf. content/quantum-observable-universe/braids-and-knots/
chirality-dual-space-derivation.md, wedderburn-trace-identity.md):

    trv (symmetric, partition [n]):     1-dim, trace τ(σ) = q
    alt (alternating, partition [1ⁿ]):  1-dim, trace τ(σ) = -q⁻¹
                                          ── this is the CHIRALITY channel
                                             (S-anti-invariant; the dual-space
                                             asymmetry τ_alt(σ) - τ_alt(σ⁻¹) = h
                                             up to sign)
    std (standard, partition [n-1,1]):  (n-1)-dim, 2×2 transfer matrix at n=3

WHY THIS REPLACES THE 2-TERM SYMMETRISED BLEND
==============================================

The earlier blend symmetrised the std-channel value under the
Frobenius antipode S (σ ↔ σ⁻¹) and added a determinant term, then
mixed them with a free phenomenological parameter. Because the
symmetrised expression is S-even, it identically annihilates the
alt Wedderburn channel — which is S-anti-invariant on odd chains.
The free mixing parameter, and a downstream n→p transition fitting
parameter, were then numerically tuned to absorb whatever the alt
channel would have contributed.

PSLQ at 25 digits over {1, G, π, 1/π, q₀, ℏ_q} with maxcoeff = 10⁶
falsified every closed-form candidate for that fitting parameter.
There is no closed form in the symmetrised frame because the
parameter is empirically standing in for a structural channel that
has been projected out. The fix is to restore the alt channel
directly, which is what V_3term does.

After this reformulation, no numerical root-find, no fitted mixing
parameter, and no n→p calibration constant appears in this file's
code path. The formula is canonical: every coefficient is a
Wedderburn-Artin weight ([wedderburn-trace-identity.md], Term 5 of
[six-term-mass-formula-complete.md]).

REFERENCES
==========

* prop:chirality-dual-space-derivation
* prop:wedderburn-trace-identity (sum dim_q(λ)² = [n]_q!)
* thm:six-term-mass-formula §Term 5 (chirality contribution H_A² Φ_3)
* docs/canonicalization-review.md §3.1 (why the fitted mixing
  parameter is structurally non-closed-form in the 2-term frame)
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp

_DPS = 50  # 50 decimal places per Sprint B requirement.

# Sprint B note (precision contract):
#   This is a high-precision scientific-calculation script, not a
#   reusable library. The canonical 3-term formula requires 50 dps so
#   the proton calibration test lands within its 1e-12 threshold;
#   under default mpmath precision (15 dps) the assertion would be
#   round-off-noise-bounded rather than algebra-bounded.
#
#   Therefore we set mp.mp.dps = _DPS globally at import time. This is
#   a deliberate, documented side-effect — *not* the bare mp.mp.dps = 50
#   that Gemini's review flagged. Callers that import this module
#   should treat 50-dps as the active precision floor; if a caller
#   needs lower precision in its own scope, it can use
#   `with mp.workdps(15):` locally.
#
#   The precision-critical calibration step inside main() additionally
#   wraps in `with mp.workdps(_DPS):` for explicit, locally-scoped
#   high precision (no reliance on the import-time global).
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps(_DPS)

from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1)  # noqa: E402
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP  # noqa: E402
from experimental_constants import M_P_MEV, M_N_MEV  # noqa: E402

# ── Substrate parameter and Markov parameter (AGENTS.md notation) ──
Q0 = Q_MP    # was f64 roundtrip — now genuine 50 dps via vol_4_1_at
QI = Q_INV_MP
# z = q³/(q²+1) — the Markov parameter, **convention D** (owner ruling
# 2026-08-15, reaffirmed 2026-08-23).  Was convention C,
# z = 1/(q^{1/2} + q^{-1/2}) = √q/(q+1), excised.
z_m = Q0**3 / (Q0**2 + 1)

# ── Wedderburn weights at n=3 ──────────────────────────────────────
# From [wedderburn-trace-identity.md]: q-deformed dimensions at n=3
# are dim_q([3]) = q, dim_q([2,1]) = q²+1, dim_q([1,1,1]) = q;
# [3]_q! = q⁴ + 4q² + 1 = D.  The Plancherel weights are
# w_λ = dim_q(λ)² / D, and they sum to 1 by construction:
#   q² + (q²+1)² + q²  =  q⁴ + 4q² + 1  =  D.
D = Q0**4 + 4*Q0**2 + 1
W_SYM = Q0**2 / D                     # trv channel weight
W_STD = (Q0**2 + 1)**2 / D            # std channel weight
W_ALT = Q0**2 / D                     # alt = chirality channel weight


def Phi_q(v, max_it=3000):
    """q-Pochhammer infinite product Φ_q(v) = ∏_{k≥1} 1/(1 - v/q^k).

    Used inside the brane-tower assembly (Term 2 / Term 3 of the
    six-term mass formula). Unchanged from the previous implementation.
    """
    if not isinstance(v, mp.mpf):
        v = mp.mpf(str(float(v)))
    if v >= 1:
        return mp.mpf('inf')
    p = mp.mpf(1)
    c = mp.mpf(1) / Q0
    # Per Gemini review: tolerances tied to current mp.mp.dps so they
    # scale automatically when precision is changed.
    tol_singular = mp.mpf(10) ** (-mp.mp.dps)
    tol_converge = mp.mpf(10) ** (-(mp.mp.dps + 20))
    for _ in range(max_it):
        t = mp.mpf(1) - c * v
        if abs(t) < tol_singular:
            return mp.mpf('inf')
        p /= t
        if abs(c * v) < tol_converge:
            break
        c /= Q0
    return p


# ──────────────────────────────────────────────────────────────────
# Three Wedderburn channels for an H_3(q) element from a chain word
# ──────────────────────────────────────────────────────────────────

def lam_sym(chain):
    """Symmetric (trv) channel eigenvalue — partition [3].

    On a single Hecke generator σ_i, τ_sym(σ_i) = q. On a chain word
    encoded as a list of (c, d) pairs (where each pair represents
    c·σ + d·1 in the standard basis), the 1-dim trv rep multiplies
    eigenvalues:
        λ_sym(g) = ∏_i (c_i · q + d_i).
    """
    val = mp.mpf(1)
    for c, d in chain:
        val *= mp.mpf(c) * Q0 + mp.mpf(d)
    return val


def lam_alt(chain):
    """Alternating (sign) channel eigenvalue — partition [1ⁿ].

    THIS IS THE CHIRALITY CHANNEL.

    The 1-dim sign rep of H_n(q) sends σ_i ↦ -q⁻¹ (so τ_alt(σ_i) = -q⁻¹).
    On a chain word:
        λ_alt(g) = ∏_i (-c_i/q + d_i).

    Per [chirality-dual-space-derivation.md], the per-crossing dual-space
    deviation τ_alt(σ) - τ_alt(σ⁻¹) = (-q⁻¹) - (-q) = q - q⁻¹ = h
    (up to channel sign), which is the canonical chirality content
    that the previous 2-term symmetrised blend dropped.
    """
    val = mp.mpf(1)
    for c, d in chain:
        val *= -mp.mpf(c) / Q0 + mp.mpf(d)
    return val


def V_std(chain):
    """Standard (2-dim) channel — partition [n-1, 1].

    At n=3 the std rep is 2-dimensional. Each chain element acts as a
    2×2 transfer matrix; V_std is the trace pairing
        V_std(g) = z · M[1,0] + M[1,1]
    where z is the Markov parameter and M = ∏_i T_i is the chain
    transfer-matrix product. This is the same "V_std" used in
    hecke_core._chain_V_full and is canonical (not S-symmetrised).
    """
    a = mp.mpf(0)
    b = mp.mpf(1)
    hv = Q0 - QI
    for c, d in chain:
        cm = mp.mpf(c)
        dm = mp.mpf(d)
        a_n = a * (cm * hv + dm) + b * cm
        b_n = a * cm + b * dm
        a, b = a_n, b_n
    return z_m * a + b


def V_3term(chain):
    """Canonical 3-term Wedderburn-weighted volume (NO fitting).

    V_3term(g) = w_sym · λ_sym(g) + w_alt · λ_alt(g) + w_std · V_std(g)

    All three channels are summed directly — no symmetrisation, no
    antipode averaging, no free α parameter. The alt term is the
    **chirality** contribution that the previous 2-term blend
    eliminated by symmetrising.

    Returns an mpmath.mpf at the current precision (50 dps).
    """
    return W_SYM * lam_sym(chain) + W_ALT * lam_alt(chain) + W_STD * V_std(chain)


def channel_decomposition(chain):
    """Per-channel breakdown of V_3term, useful for witnesses.

    Returns a dict with keys {'trv', 'alt', 'std', 'total'} mapping
    to the weighted contribution of each Wedderburn block.
    """
    s = W_SYM * lam_sym(chain)
    a = W_ALT * lam_alt(chain)
    t = W_STD * V_std(chain)
    return {
        'trv': s,
        'alt': a,
        'std': t,
        'total': s + a + t,
    }


# ──────────────────────────────────────────────────────────────────
# Brane tower assembly (Terms 1-3 of the six-term mass formula)
# ──────────────────────────────────────────────────────────────────

def tower(V_list):
    """Brane-tower mass assembly from a list of canonical V_3term values.

    Uses the same Φ_q + Markov-parameter combinatorial pattern as
    the previous implementation; only the per-vertex V is now the
    canonical 3-term formula instead of the 2-term blend.
    """
    abs_V = [mp.fabs(v) for v in V_list]
    n = len(abs_V)
    prod = mp.mpf(1)
    for v in abs_V:
        prod *= v
    total = prod
    for k in range(1, n + 1):
        for sub in combinations(range(n), k):
            pv = mp.mpf(1)
            for i in sub:
                pv *= abs_V[i]
            if pv >= 1:
                continue
            span = max(sub) - min(sub) if k >= 2 else 0
            total += z_m**(2 * span) * Phi_q(pv)
    return total


def particle_mass(g0_chain, g1_chain):
    """Canonical mass for a particle described by per-generator chains.

    Computes V_3term on each generator's crossing chain, then assembles
    via the brane tower. No fitting parameters, no root-find.
    Returns the dimensionless mass mp_v (to be calibrated against
    proton mass to extract MeV scale).
    """
    V0 = V_3term(g0_chain)
    V1 = V_3term(g1_chain)
    return tower([V0, V1])


# ──────────────────────────────────────────────────────────────────
# Entry point — diagnostic + witness emission
# ──────────────────────────────────────────────────────────────────

def main() -> int:
    print("=" * 100)
    print("3-TERM WEDDERBURN TOWER — canonical mass formula (no mixing-parameter fit)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  Wedderburn weights at n=3:")
    print(f"    w_sym = {float(W_SYM):.12f}  (trv channel)")
    print(f"    w_std = {float(W_STD):.12f}  (std channel)")
    print(f"    w_alt = {float(W_ALT):.12f}  (alt = chirality channel)")
    print(f"    sum   = {float(W_SYM + W_STD + W_ALT):.12f}  (= 1 by construction; w_λ = dim_q(λ)²/D)")
    print()

    # Per-particle: proton, neutron
    Vp0 = V_3term(_PROTON_G0)
    Vp1 = V_3term(_PROTON_G1)
    Vn0 = V_3term(_NEUTRON_G0)
    Vn1 = V_3term(_NEUTRON_G1)

    # Per-channel decomposition for each generator chain (illustrates
    # that the alt/chirality contribution is non-zero).
    p_g0 = channel_decomposition(_PROTON_G0)
    p_g1 = channel_decomposition(_PROTON_G1)
    n_g0 = channel_decomposition(_NEUTRON_G0)
    n_g1 = channel_decomposition(_NEUTRON_G1)

    print("  Per-channel decomposition (proton, gen 0):")
    for k in ('trv', 'alt', 'std', 'total'):
        print(f"    {k:>5} = {float(p_g0[k]):+.10e}")
    print("  Per-channel decomposition (neutron, gen 0):")
    for k in ('trv', 'alt', 'std', 'total'):
        print(f"    {k:>5} = {float(n_g0[k]):+.10e}")
    print()

    mp_v = tower([Vp0, Vp1])
    mn_v = tower([Vn0, Vn1])
    if mp_v == 0:
        print("  [ERROR] proton mass evaluated to 0 — cannot calibrate.")
        return 1

    # Calibrate energy scale on the proton (single point; no fit).
    # Do the division and multiplication at 50 dps so the scale carries
    # the full mpmath precision; only cast to float at the print boundary.
    with mp.workdps(_DPS):
        E0 = mp.mpf(str(M_P_MEV)) / mp_v
        mp_pred_MeV = float(mp_v * E0)  # exactly M_P_MEV by construction
        mn_pred_MeV = float(mn_v * E0)
    err_p_pct = (mp_pred_MeV - M_P_MEV) / M_P_MEV * 100
    err_neutron_pct = (mn_pred_MeV - M_N_MEV) / M_N_MEV * 100
    err_p_ppb = err_p_pct * 1e7
    err_neutron_ppb = err_neutron_pct * 1e7

    print("  Per-particle predictions vs CODATA:")
    print(f"    {'particle':<10} {'V_3term':>22} {'pred [MeV]':>14} {'CODATA [MeV]':>14} {'err [%]':>10} {'err [ppb]':>14}")
    print(f"    {'proton':<10} {float(mp_v):>+22.10e} {mp_pred_MeV:>14.6f} {M_P_MEV:>14.6f} {err_p_pct:>+10.4f} {err_p_ppb:>+14.4e}")
    print(f"    {'neutron':<10} {float(mn_v):>+22.10e} {mn_pred_MeV:>14.6f} {M_N_MEV:>14.6f} {err_neutron_pct:>+10.4f} {err_neutron_ppb:>+14.4e}")
    print()

    print("  Sanity checks (canonical-only enforcement):")
    # Forbidden tokens are read from a sibling manifest so this source
    # itself contains no occurrence of them. See test_three_term_wedderburn.py
    # for the authoritative grep-based enforcement.
    src = Path(__file__).read_text()
    manifest = (Path(__file__).parent / "three-term-forbidden-tokens.txt")
    if manifest.exists():
        needles = [ln.strip() for ln in manifest.read_text().splitlines()
                   if ln.strip() and not ln.startswith('#')]
    else:
        needles = []
    forbidden = [n for n in needles if n in src]
    print(f"    Forbidden tokens still in file (must be empty): {forbidden}")
    print()

    witness = {
        'computation': 'three-term-wedderburn',
        'description': (
            'Canonical 3-term Wedderburn-decomposition mass formula. '
            'V_3term(g) = w_sym·lam_sym + w_alt·lam_alt + w_std·V_std '
            'with Wedderburn weights w_sym=w_alt=q^2/D, w_std=(q^2+1)^2/D, '
            'D=q^4+4q^2+1. The alt channel restores the chirality contribution '
            '(prop:chirality-dual-space-derivation) that the previous 2-term '
            'symmetrised blend dropped. No fitted mixing parameter, no n->p '
            'transition calibration constant, no numerical root-find anywhere '
            'in the path. Eliminates empirical constants #1 and #5 of '
            'docs/canonicalization-review.md §3.1.'
        ),
        'computedAt': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'precision_dps': 50,
        'wedderburn_weights': {
            'w_sym': float(W_SYM),
            'w_std': float(W_STD),
            'w_alt': float(W_ALT),
            'D': float(D),
        },
        'particles': {
            'proton': {
                'V_3term': float(mp_v),
                'pred_MeV': mp_pred_MeV,
                'codata_MeV': M_P_MEV,
                'err_pct': err_p_pct,
                'err_ppb': err_p_ppb,
                'channel_decomposition_g0': {k: float(v) for k, v in p_g0.items()},
                'channel_decomposition_g1': {k: float(v) for k, v in p_g1.items()},
            },
            'neutron': {
                'V_3term': float(mn_v),
                'pred_MeV': mn_pred_MeV,
                'codata_MeV': M_N_MEV,
                'err_pct': err_neutron_pct,
                'err_ppb': err_neutron_ppb,
                'channel_decomposition_g0': {k: float(v) for k, v in n_g0.items()},
                'channel_decomposition_g1': {k: float(v) for k, v in n_g1.items()},
            },
        },
        'attestation': {
            'forbidden_tokens_present': forbidden,
            'forbidden_tokens_checked': needles,
            'canonical_only': len(forbidden) == 0,
        },
    }
    out = Path(__file__).parent / "three-term-wedderburn.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
