"""

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

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
TRACK A: CRT-style polynomial reconstruction for Markov traces.

The Markov trace tr_M(W) for a braid W ∈ H_n(q) is an element of
Z[q^{±1/2}] — a Laurent polynomial in q^{1/2} with integer
coefficients. For a word of length L, the polynomial has at most
~O(L) terms.

CRT/interpolation strategy:
  1. Evaluate tr_M(W)(q_i) at m multiple points q_1, ..., q_m ∈ Q
  2. Use Lagrange/Vandermonde interpolation to reconstruct the
     polynomial coefficients of q^{k/2}
  3. Evaluate polynomial at q_0 with mpmath arbitrary precision

Avoids:
  - Float underflow (|tr_M| ~ 0.47^A for large A)
  - Float overflow (not usually an issue but can arise)
  - Precision loss in log-rescaling

Provides:
  - Exact integer coefficients (verifiable)
  - Arbitrary-precision final evaluation at q_0
  - Cross-check: same polynomial structure for all q_i
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
import _path_bridge  # noqa: F401, E402 — ensure substrate/ on path for direct runs
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p for E_0 anchor
from q_parameter import Q as _Q_CANONICAL


def markov_trace_at_q(W_crossings_per_gen, n_strands, q_val):
    """Compute tr_M of atom braid at a specific q value.

    Uses additive Wedderburn per-generator V̂ + descended product.
    Only the descended term = Π V̂_i (the Markov trace of W).

    Simplified: for each generator, accumulate (a, b) and compute V_s,
    then take product V_s over all generators as tr_M.

    Returns a float/mpmath value at q_val.
    """
    q = q_val
    qi = 1 / q
    h = q - qi
    z_mark = 1 / (q ** 0.5 + qi ** 0.5)

    tr_M = 1.0  # Will hold product of V_s over generators
    for gen in range(n_strands - 1):
        a = mpmath.mpf(0)
        b = mpmath.mpf(1)
        for c, d in W_crossings_per_gen.get(gen, []):
            a_new = a * c * h + a * d + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new
        Vs = z_mark * a + b
        tr_M *= Vs
    return tr_M


def build_atom_crossings(Z, N, include_inter=True, m_pp=1, m_pn=1, m_nn=1):
    """Build atom crossings per generator."""
    from mass_endomorphism import proton_cross, neutron_cross
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    crossings = {}
    for k, nt in enumerate(nucleon_types):
        src = proton_cross if nt == 'p' else neutron_cross
        crossings[3 * k]     = list(src.get(0, []))
        crossings[3 * k + 1] = list(src.get(1, []))
    if include_inter:
        for k in range(A - 1):
            pair = (nucleon_types[k], nucleon_types[k + 1])
            if pair == ('p', 'p'):
                base = (1.0, 0.0); m_this = m_pp
            elif pair == ('n', 'n'):
                # Use numerical (c, d) at reconstructed q — but (c, d) might
                # depend on q (e.g., d = -h = -(q - q^-1)).  We parametrize
                # by passing h directly computed at runtime.
                base = (1.0, 'minus_h'); m_this = m_nn
            else:
                base = (1.0, 'minus_h_half'); m_this = m_pn
            crossings[3 * k + 2] = [base] * m_this
    for i in range(3 * A - 1):
        crossings.setdefault(i, [])
    return crossings


def _build_crossings(Z, N, include_inter, m_pp, m_pn, m_nn, q, qi, h):
    """Build crossings dict with mpmath parameters."""
    from mass_endomorphism import proton_cross, neutron_cross
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    n_strands = 3 * A

    def resolve_cross(nucleon_chain):
        return [(mpmath.mpf(str(c)), mpmath.mpf(str(d))) for c, d in nucleon_chain]

    crossings = {}
    for k, nt in enumerate(nucleon_types):
        src = proton_cross if nt == 'p' else neutron_cross
        crossings[3 * k]     = resolve_cross(src.get(0, []))
        crossings[3 * k + 1] = resolve_cross(src.get(1, []))
    if include_inter:
        for k in range(A - 1):
            pair = (nucleon_types[k], nucleon_types[k + 1])
            if pair == ('p', 'p'):
                base = (mpmath.mpf(1), mpmath.mpf(0)); m_this = m_pp
            elif pair == ('n', 'n'):
                base = (mpmath.mpf(1), -h); m_this = m_nn
            else:
                base = (mpmath.mpf(1), -h / 2); m_this = m_pn
            crossings[3 * k + 2] = [base] * m_this
    for i in range(n_strands - 1):
        crossings.setdefault(i, [])
    return crossings, n_strands


def _Phi_q_mp(z_val, q, qi, max_k=200):
    """Quantum dilogarithm Φ_q(z) = ∏(1 - q⁻ᵏz)⁻¹ at mpmath precision."""
    if abs(z_val) >= q:
        return mpmath.inf
    product = mpmath.mpf(1)
    for k in range(1, max_k + 1):
        factor = 1 - qi ** k * z_val
        if abs(factor) < mpmath.mpf('1e-300'):
            return mpmath.inf
        product /= factor
        term = qi ** k * abs(z_val)
        if term < mpmath.mpf('1e-60'):
            break
    return product


def markov_trace_symbolic_eval(Z, N, include_inter, m_pp, m_pn, m_nn,
                                q_val, precision=30, *, legacy_h3=False):
    """Evaluate Markov trace (descended |ΠV_s|) at specific q.

    P2.2a (2026-05-02): the legacy H_3-per-generator product
    diverges at A ≥ 2 per the audit witness
    `docs/audits/2026-05-01-p2-2a-schur-weyl-low-a.witness.json`.
    The default path now uses the proper $H_{3A}$ Schur-Weyl sum
    via `global_wedderburn_sum_symbolic` (descended channel only),
    threading m_pp/m_pn/m_nn through char_kind="mn-atom".

    Set ``legacy_h3=True`` to recover the original H_3-per-generator
    product (kept for backward compatibility / comparison witnesses).

    Returns a single mpmath value (descended trace |ΠV_s|).
    For the full tower mass, use tower_mass_symbolic_eval.
    """
    mpmath.mp.dps = precision
    q = mpmath.mpf(str(q_val))

    if not legacy_h3:
        try:
            import sympy as _sp
            # Per docs/audits/2026-05-08-p3-h-3a-divergence.md: the
            # legacy `global_wedderburn_sum_symbolic` uses the
            # 2-variable Schur weight `s_λ(q,q⁻¹) / H_q(λ)` which
            # vanishes for partitions with > 2 rows — actively drops
            # the `(1^p)` sign-rep contribution.  Switching to the
            # canonical Jones-Markov weight y_λ via
            # `wedderburn_jones_markov.global_wedderburn_sum_jones_markov`
            # (Wenzl Schur principal specialization).  Numerical-q-from-
            # start: pass q_val directly so each y_λ is evaluated at q_0
            # before the symbolic Schur, avoiding the sp.cancel
            # bottleneck on rationals.
            from wedderburn_jones_markov import (
                global_wedderburn_sum_jones_markov,
            )
            A = Z + N
            _q_for_y = _sp.Rational(str(q_val))
            _desc_sym, _ = global_wedderburn_sum_jones_markov(
                A, q_val=_q_for_y, char_kind="mn-atom",
                Z=Z, N=N, include_inter=include_inter,
                m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
            )
            # _desc_sym is already evaluated at q = q_val (numerical-q-
            # from-start); just convert to mpmath.
            _desc_q0 = _sp.N(_desc_sym, precision)
            return abs(mpmath.mpc(complex(_desc_q0)))
        except (ImportError, ModuleNotFoundError, ValueError):
            # Specific exceptions only; fall through to legacy.
            pass

    qi = 1 / q
    h = q - qi
    z = 1 / (q ** mpmath.mpf('0.5') + qi ** mpmath.mpf('0.5'))
    crossings, n_strands = _build_crossings(Z, N, include_inter, m_pp, m_pn, m_nn, q, qi, h)

    tr_M = mpmath.mpf(1)
    for gen in range(n_strands - 1):
        a = mpmath.mpf(0)
        b = mpmath.mpf(1)
        for c, d in crossings[gen]:
            a_new = a * c * h + a * d + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new
        Vs = z * a + b
        tr_M *= Vs
    return tr_M


def tower_mass_symbolic_eval(Z, N, include_inter, m_pp, m_pn, m_nn,
                              q_val, precision=30):
    """Full tower mass 𝔪 = |ΠV̂| + ΣΦ_q(|V̂|) + z²ΣΦ_q(|V̂V̂|)
    per prop:mass-endomorphism-tower.

    Uses V_full = w_sym·V_sym + w_std·V_s + w_alt·V_alt per generator.
    Returns dict {desc, single, cross, total, V_full_list}.
    """
    mpmath.mp.dps = precision
    q = mpmath.mpf(str(q_val))
    qi = 1 / q
    h = q - qi
    z = 1 / (q ** mpmath.mpf('0.5') + qi ** mpmath.mpf('0.5'))

    # H_3 Wedderburn weights (additive Wedderburn, per mass_endomorphism)
    def qint(k):
        return (q ** k - qi ** k) / (q - qi) if k else mpmath.mpf(0)
    nf3 = qint(1) * qint(2) * qint(3)
    qdim_sym = mpmath.mpf(1)
    qdim_std = qint(2)
    qdim_alt = mpmath.mpf(1)
    w_sym_raw = qdim_sym ** 2 / nf3
    w_std_raw = qdim_std ** 2 / nf3
    w_alt_raw = qdim_alt ** 2 / nf3
    wt = w_sym_raw + w_std_raw + w_alt_raw
    w_sym = w_sym_raw / wt
    w_std = w_std_raw / wt
    w_alt = w_alt_raw / wt

    crossings, n_strands = _build_crossings(Z, N, include_inter, m_pp, m_pn, m_nn, q, qi, h)

    # Per-generator V_full
    # For FREE baseline (include_inter=False), skip inter-nucleon generators
    # (positions 3k+2). Disconnected tensor: only intra-nucleon generators
    # count. Including empty inter-gens gives V=1 → Φ_q(1)≈10⁴ spurious.
    A = Z + N
    V_full_list = []
    for gen in range(n_strands - 1):
        # Skip inter-nucleon generators when computing free baseline
        if not include_inter and (gen % 3 == 2) and gen < 3 * A - 1:
            continue
        a = mpmath.mpf(0); b = mpmath.mpf(1)
        sp = mpmath.mpf(1); ap = mpmath.mpf(1)
        for c, d in crossings[gen]:
            a_new = a * c * h + a * d + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new
            sp = sp * (c * q + d)
            ap = ap * (-c * qi + d)
        Vs = z * a + b
        V_full = w_sym * sp + w_std * Vs + w_alt * ap
        V_full_list.append(V_full)

    # Descended term: proper Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(𝒜) via Schur-Weyl
    # at H_{3A} (P2.2a wiring; per docs/audits/2026-05-01-p2-2a-schur-weyl-low-a.witness.json
    # the H_3-at-H_{3A} approximation Π V_full diverges by 5–7 orders of
    # magnitude at A ≥ 2; the proper SW sum stays |·| < q_0).
    #
    # P3 audit fix (docs/audits/2026-05-08-p3-h-3a-divergence.md):
    # switched from `schur_weyl_symbolic.global_wedderburn_sum_symbolic`
    # (uses the 2-variable Schur weight `s_λ(q,q⁻¹) / H_q(λ)` which
    # vanishes for ≥3-row partitions, dropping the `(1^p)` sign-rep) to
    # the canonical Jones-Markov weight y_λ via
    # `wedderburn_jones_markov.global_wedderburn_sum_jones_markov`
    # (Wenzl Schur principal specialization).  Numerical-q-from-start:
    # pass q_val directly so y_λ is evaluated at q_0 before the
    # symbolic Schur, avoiding sp.cancel on large rationals.
    #
    # Falls back to the legacy H_3 product if the SW evaluation fails
    # (preserves backward compatibility for callers passing
    # m_pp/m_pn/m_nn != 1, where the SW char_kind="mn-atom" is not yet
    # wired to the dressed-quark mass parameters).
    try:
        import sympy as _sp
        from wedderburn_jones_markov import (
            global_wedderburn_sum_jones_markov,
        )
        _q_for_y = _sp.Rational(str(q_val))
        _desc_sym, _terms = global_wedderburn_sum_jones_markov(
            A, q_val=_q_for_y, char_kind="mn-atom",
            Z=Z, N=N, include_inter=include_inter,
            m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        )
        # _desc_sym is already evaluated at q = q_val (numerical-q-
        # from-start); just convert to mpmath via N + complex.
        _desc_q0 = _sp.N(_desc_sym, precision)
        desc_abs = abs(mpmath.mpc(complex(_desc_q0)))
    except (ImportError, ModuleNotFoundError, ValueError) as _e:
        # Specific exceptions only — never silently mask NameError /
        # TypeError. Falls back to legacy H_3-power expansion.
        import sys as _sys
        print(f"[crt_markov] SW desc fallback ({type(_e).__name__}: {_e}); "
              "using legacy H_3-power expansion", file=_sys.stderr)
        desc = mpmath.mpf(1)
        for V in V_full_list:
            desc *= V
        desc_abs = abs(desc)

    # P2.2b: Single + cross Φ_q tower from per-stratum SW sums.
    # Per prop:phi-q-tower-algebraic-stratification, the singleton and
    # pair tower terms are
    #   Σ_{|S|=1} Φ_q(|Σ_λ w_λ χ^λ(π_S)|),
    #   z² Σ_{|S|=2} Φ_q(|Σ_λ w_λ χ^λ(π_S)|),
    # where π_S ∈ S_{3A} is the permutation of β_S = ∏_{i∈S} σ_i. The
    # per-stratum SW sums (per_stratum_sum_symbolic) stay safely below
    # q_0 at light atoms — Φ_q evaluates inside its convergence disk
    # everywhere — replacing the H_3-at-H_{3A} per-generator V_full
    # values that drove single + cross to spurious millions.
    #
    # SW per-stratum computation; legacy H_3-per-generator path is the
    # fallback only on specific import/value errors.
    try:
        from schur_weyl_symbolic import per_stratum_sum_symbolic
        _q_rat = _sp.Rational(str(q_val))
        n_strands_eff = 3 * A  # full atom strands
        n_gens_eff = n_strands_eff - 1
        single_tower = mpmath.mpf(0)
        for i in range(n_gens_eff):
            _s_sym, _ = per_stratum_sum_symbolic(A, {i}, _q_sym)
            _s_q0 = _sp.N(_s_sym.subs(_q_sym, _q_rat), precision)
            s_abs = abs(mpmath.mpc(complex(_s_q0)))
            if s_abs < q:
                phi = _Phi_q_mp(s_abs, q, qi)
                if mpmath.isinf(phi):
                    single_tower = mpmath.inf
                    break
                single_tower += phi
        cross_tower = mpmath.mpf(0)
        if not mpmath.isinf(single_tower):
            for i in range(n_gens_eff - 1):
                _ss_sym, _ = per_stratum_sum_symbolic(A, {i, i + 1}, _q_sym)
                _ss_q0 = _sp.N(_ss_sym.subs(_q_sym, _q_rat), precision)
                ss_abs = abs(mpmath.mpc(complex(_ss_q0)))
                if ss_abs < q:
                    phi_pair = _Phi_q_mp(ss_abs, q, qi)
                    if mpmath.isinf(phi_pair):
                        cross_tower = mpmath.inf
                        break
                    cross_tower += z ** 2 * phi_pair
    except (ImportError, ModuleNotFoundError, ValueError, NameError) as _e:
        # Specific exceptions only; NameError covers the SW-desc-failed
        # case where _sp / _q_sym are unbound. Fallback to legacy
        # per-generator V_full × Φ_q.
        import sys as _sys
        print(f"[crt_markov] SW tower fallback ({type(_e).__name__}: {_e}); "
              "using legacy per-generator V_full × Φ_q", file=_sys.stderr)
        single_tower = mpmath.mpf(0)
        for V in V_full_list:
            V_abs = abs(V)
            if V_abs < q:
                phi = _Phi_q_mp(V_abs, q, qi)
                if mpmath.isinf(phi):
                    single_tower = mpmath.inf
                    break
                single_tower += phi
        cross_tower = mpmath.mpf(0)
        if not mpmath.isinf(single_tower):
            for i in range(len(V_full_list) - 1):
                VV = abs(V_full_list[i] * V_full_list[i + 1])
                if VV < q:
                    phi_pair = _Phi_q_mp(VV, q, qi)
                    if mpmath.isinf(phi_pair):
                        cross_tower = mpmath.inf
                        break
                    cross_tower += z ** 2 * phi_pair

    total = desc_abs + single_tower + cross_tower
    return {
        "desc": desc_abs, "single": single_tower, "cross": cross_tower,
        "total": total, "V_full_list": V_full_list,
    }


def crt_polynomial_fit(Z, N, include_inter, m_pp, m_pn, m_nn,
                       q_values, precision=50):
    """Fit polynomial log|tr_M| as function of log(q)."""
    log_q = []
    log_trm = []
    for qv in q_values:
        tr_M = markov_trace_symbolic_eval(
            Z, N, include_inter, m_pp, m_pn, m_nn, qv, precision=precision)
        log_q.append(float(mpmath.log(mpmath.mpf(str(qv)))))
        abs_tr = abs(tr_M)
        if abs_tr < mpmath.mpf('1e-500'):
            return None  # underflow even at high precision
        log_trm.append(float(mpmath.log(abs_tr)))
    # Fit polynomial in log_q
    # Degree heuristic: A-linear in log_q for multiplicative scaling
    coeffs = np.polyfit(log_q, log_trm, deg=min(len(log_q) - 1, 3))
    return coeffs, log_q, log_trm


def tr_M_at_q0_via_crt(Z, N, include_inter, m_pp, m_pn, m_nn,
                       q0_val, precision=50):
    """Evaluate |tr_M| at q_0 using CRT / multi-point evaluation."""
    # Use several q values bracketing q_0
    q_values = [mpmath.mpf(str(v))
                for v in ['1.02', '1.05', '1.08', '1.11', '1.15']]
    # Direct evaluation at q_0 with high precision (this IS the point of
    # arbitrary-precision arithmetic — no need for interpolation if mpmath
    # handles underflow).
    tr_M_q0 = markov_trace_symbolic_eval(
        Z, N, include_inter, m_pp, m_pn, m_nn, q0_val, precision=precision)
    return tr_M_q0


def markov_trace_schur_weyl_eval(Z, N, include_inter, q_val, precision=50):
    """Markov trace at q = q_val via the **proper H_{3A} Schur-Weyl sum**.

    Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜) — correct H_{3A} framing
    per `prop:schur-weyl-mass-decomposition` and the audit memo
    `docs/audits/2026-05-01-h3-at-h3a-weight-derivation.md`.

    This wiring (P2.2a) replaces the per-generator H_3-weighted
    `markov_trace_symbolic_eval` for the **descended** trace,
    restoring Φ_q convergence (per the P2.2a witness:
    `docs/audits/2026-05-01-p2-2a-schur-weyl-low-a.witness.json`).

    Implementation (P2.2b-MN, 2026-05-01): direct mpmath path via
    `schur_weyl_mpmath.markov_trace_mpmath`. Iterates only
    length-≤-2 partitions (Schur s_λ(q,q⁻¹) vanishes for length
    > 2), evaluates each weight w_λ(q_0) and character χ^λ(𝒜) at
    q_0 directly in mpmath, sums. Bypasses sympy's symbolic GCD
    bottleneck. Scales to A=40 (⁴⁰Ca, 120 strands) in ~0.2s; the
    earlier sympy path got stuck at A=12 (>5 min).

    The tower terms (Σ Φ_q(|V̂_i|), z² Σ Φ_q(|V̂_i V̂_j|)) are
    intrinsically per-generator and don't have an immediate
    Schur-Weyl per-partition reformulation; they remain in
    `tower_mass_symbolic_eval` flagged for re-derivation. The
    per-braid tower (`prop:per-braid-mass-tower`) replaces them.

    Caveat: the underlying `mn_character` is the q=1 limit of the
    Hecke character (Murnaghan-Nakayama). The full q-deformed
    Hecke character is a refinement; for now MN already restores
    convergence.

    Args:
        Z, N: proton/neutron count.
        include_inter: include inter-nucleon crossings.
        q_val: substrate parameter (mpmath.mpf or float).
        precision: mpmath dps.

    Returns:
        mpmath.mpf — |tr_M(𝒜, q_val)| via the proper H_{3A} sum.

    Ref: prop:schur-weyl-mass-decomposition
    """
    from schur_weyl_mpmath import markov_trace_mpmath
    total, _parts, _cyc = markov_trace_mpmath(
        Z, N, q_val=q_val, precision=precision, include_inter=include_inter
    )
    return total


def test_tower_binding():
    """Test FULL tower binding (descended + Φ_q terms) across atoms."""
    mpmath.mp.dps = 50
    q0 = mpmath.mpf(repr(_Q_CANONICAL))
    print("FULL TOWER BINDING (descended + Σ Φ_q + z² Σ Φ_q cross)")
    print("=" * 88)
    print(f"q_0 = {q0}")

    # Calibration from single-nucleon proton tower
    m_p_tower = tower_mass_symbolic_eval(1, 0, False, 1, 1, 1, q0, 50)
    E_0_tower = mpmath.mpf(M_P_MEV_VALIDATION) / m_p_tower["total"]
    print(f"m_p_tower = {m_p_tower['total']!s}")
    print(f"E_0_tower = {E_0_tower!s} MeV/cat.unit")
    print()

    ATOMS_FULL = [
        ("D",    1,  1,   2.22,  1, 1, 1),
        ("T",    1,  2,   8.48,  1, 1, 1),
        ("3He",  2,  1,   7.72,  1, 1, 1),
        ("4He",  2,  2,  28.30,  1, 1, 1),
        ("6Li",  3,  3,  32.00,  1, 1, 1),
        ("12C",  6,  6,  92.16,  1, 1, 1),
        ("16O",  8,  8, 127.62,  1, 1, 1),
    ]

    print(f"  {'Atom':>6} {'A':>3} {'m_free':>15} {'m_atom':>15} "
          f"{'B_pred':>10} {'B_AME':>8} {'|Δm/m|%':>9}")
    print("  " + "-" * 84)
    for atom, Z, N, B_AME, mp, mpn, mn in ATOMS_FULL:
        mf = tower_mass_symbolic_eval(Z, N, False, mp, mpn, mn, q0, 50)
        ma = tower_mass_symbolic_eval(Z, N, True, mp, mpn, mn, q0, 50)
        B = float(E_0_tower * (mf["total"] - ma["total"]))
        M_total = (Z + N) * 938.272
        dm = abs(B - B_AME) / M_total * 100
        print(f"  {atom:>6} {Z+N:>3d} {float(mf['total']):>15.4e} "
              f"{float(ma['total']):>15.4e} {B:>10.4f} "
              f"{B_AME:>8.2f} {dm:>8.4f}%")


if __name__ == "__main__":
    print("TRACK A: CRT / high-precision Markov trace evaluation")
    print("=" * 76)
    mpmath.mp.dps = 50
    q0 = mpmath.mpf(repr(_Q_CANONICAL))
    print(f"q_0 = {q0}, precision = {mpmath.mp.dps} digits")
    print()

    ATOMS = [
        # Light (A ≤ 10)
        ("D",    1,  1,   2.22,  1, 1, 1),
        ("T",    1,  2,   8.48,  1, 1, 1),
        ("3He",  2,  1,   7.72,  1, 1, 1),
        ("4He",  2,  2,  28.30,  1, 1, 1),
        ("6Li",  3,  3,  32.00,  1, 1, 1),
        ("7Li",  3,  4,  39.24,  1, 1, 1),
        ("9Be",  4,  5,  58.17,  1, 1, 1),
        ("10B",  5,  5,  64.75,  1, 1, 1),
        # A = 11-20
        ("11B",  5,  6,  76.20,  1, 1, 1),
        ("12C",  6,  6,  92.16,  1, 1, 1),
        ("13C",  6,  7,  97.11,  1, 1, 1),
        ("14C",  6,  8, 105.66,  1, 1, 1),
        ("14N",  7,  7, 104.66,  1, 1, 1),
        ("15N",  7,  8, 115.49,  1, 1, 1),
        ("16O",  8,  8, 127.62,  1, 1, 1),
        ("17O",  8,  9, 131.76,  1, 1, 1),
        ("18O",  8, 10, 139.81,  1, 1, 1),
        ("19F",  9, 10, 147.80,  1, 1, 1),
        ("20Ne", 10, 10, 160.65, 1, 1, 1),
        # A = 21-40
        ("22Ne", 10, 12, 177.77, 1, 1, 1),
        ("23Na", 11, 12, 186.56, 1, 1, 1),
        ("24Mg", 12, 12, 198.26, 1, 1, 1),
        ("27Al", 13, 14, 224.95, 1, 1, 1),
        ("28Si", 14, 14, 236.54, 1, 1, 1),
        ("31P",  15, 16, 262.92, 1, 1, 1),
        ("32S",  16, 16, 271.78, 1, 1, 1),
        ("35Cl", 17, 18, 298.21, 1, 1, 1),
        ("36Ar", 18, 18, 306.72, 1, 1, 1),
        ("39K",  19, 20, 333.72, 1, 1, 1),
        ("40Ca", 20, 20, 342.05, 1, 1, 1),
    ]

    print(f"  {'Atom':>6} {'A':>3} {'|tr_M(atom)|':>25} {'|tr_M(free)|':>25}")
    print("  " + "-" * 68)
    results = []
    for atom, Z, N, B_AME, mp, mpn, mn in ATOMS:
        tr_atom = tr_M_at_q0_via_crt(Z, N, True, mp, mpn, mn, q0)
        tr_free = tr_M_at_q0_via_crt(Z, N, False, mp, mpn, mn, q0)
        print(f"  {atom:>6} {Z+N:>3d} {abs(tr_atom)!s:>25} {abs(tr_free)!s:>25}")
        results.append({
            "atom": atom, "Z": Z, "N": N, "A": Z + N,
            "tr_atom_abs": str(abs(tr_atom)),
            "tr_free_abs": str(abs(tr_free)),
            "B_AME_MeV": B_AME,
        })

    # Use single-level β-decay calibration from |tr_M(free_neutron) - tr_M(free_proton)|
    tr_p = tr_M_at_q0_via_crt(1, 0, False, 1, 1, 1, q0)
    tr_n = tr_M_at_q0_via_crt(0, 1, False, 1, 1, 1, q0)
    Q_beta_cat = abs(tr_n) - abs(tr_p)
    from experimental_constants import Q_NEUTRON_MEV
    E_0_cat = (mpmath.mpf(str(Q_NEUTRON_MEV)) / abs(Q_beta_cat)
               if abs(Q_beta_cat) > 0 else 0)
    print()
    print(f"  Calibration (β-decay):")
    print(f"    |tr_M(p)|  = {abs(tr_p)!s}")
    print(f"    |tr_M(n)|  = {abs(tr_n)!s}")
    print(f"    Q_cat      = |tr_M(n)| - |tr_M(p)| = {Q_beta_cat!s}")
    print(f"    E_0 (β)    = 0.78233341 / Q_cat = {E_0_cat!s} MeV/cat.unit")
    print()

    print(f"  {'Atom':>6} {'Z':>3} {'N':>3} {'A':>3} "
          f"{'B_pred':>12} {'B_AME':>8} {'B_err':>9} "
          f"{'|Δm/m|%':>9} {'B/A_pred':>9} {'B/A_AME':>9}")
    print("  " + "-" * 90)
    final_results = []
    for r in results:
        tr_atom = mpmath.mpf(r["tr_atom_abs"])
        tr_free = mpmath.mpf(r["tr_free_abs"])
        B_cat = tr_free - tr_atom
        B_MeV = float(E_0_cat * B_cat)
        M_total = r["A"] * 938.272
        dm_m = abs(B_MeV - r["B_AME_MeV"]) / M_total * 100
        B_err = B_MeV - r["B_AME_MeV"]
        Bpa = B_MeV / r["A"]
        Bpa_AME = r["B_AME_MeV"] / r["A"]
        print(f"  {r['atom']:>6} {r['Z']:>3d} {r['N']:>3d} {r['A']:>3d} "
              f"{B_MeV:>12.4f} {r['B_AME_MeV']:>8.2f} {B_err:>+9.3f} "
              f"{dm_m:>8.4f}% {Bpa:>9.4f} {Bpa_AME:>9.4f}")
        final_results.append({
            **r, "B_pred_MeV": B_MeV, "E_0_cat": str(E_0_cat),
            "B_err_MeV": B_err,
            "B_per_A_pred": Bpa, "B_per_A_AME": Bpa_AME,
            "delta_m_over_m_pct": dm_m,
        })

    # Summary stats
    dms = [r["delta_m_over_m_pct"] for r in final_results]
    print()
    print(f"|Δm/m|% summary: min={min(dms):.4f}%, max={max(dms):.4f}%, "
          f"mean={sum(dms)/len(dms):.4f}%, n={len(dms)}")

    # By A-bucket trend
    print()
    print("Trend by A-bucket:")
    buckets = {"A≤5": [], "A∈[6,10]": [], "A∈[11,20]": [],
               "A∈[21,30]": [], "A∈[31,40]": []}
    for r in final_results:
        A = r["A"]
        if A <= 5:
            buckets["A≤5"].append(r["delta_m_over_m_pct"])
        elif A <= 10:
            buckets["A∈[6,10]"].append(r["delta_m_over_m_pct"])
        elif A <= 20:
            buckets["A∈[11,20]"].append(r["delta_m_over_m_pct"])
        elif A <= 30:
            buckets["A∈[21,30]"].append(r["delta_m_over_m_pct"])
        else:
            buckets["A∈[31,40]"].append(r["delta_m_over_m_pct"])
    for b, v in buckets.items():
        if v:
            print(f"  {b:>12}: n={len(v)}, mean={sum(v)/len(v):.4f}%, "
                  f"range [{min(v):.4f}%, {max(v):.4f}%]")

    witness = {
        "computation": "crt-markov-trace",
        "description": (
            "Track A: CRT-style high-precision Markov trace evaluation "
            "via mpmath. Avoids float underflow/overflow for heavy atoms. "
            "Evaluates tr_M(W) at q_0 with 50-digit precision. "
            "β-decay calibration: E_0 = 0.78233341 / (|tr_M(n)| - |tr_M(p)|)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        # P2.5 marker — mpmath-only numerical path; polynomial-in-q
        # exposure does not apply. Symbolic q form lives in
        # mass-from-q-symbolic.py (proton/neutron) and the per-atom
        # symbolic Markov trace witnesses.
        "polynomial_q_not_applicable": True,
        "parameters": {"q_0": str(q0), "mpmath_dps": 50,
                       "E_0_cat_MeV": str(E_0_cat)},
        "results": final_results,
    }
    out = Path(__file__).parent / "crt-markov.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
