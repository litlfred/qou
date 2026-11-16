#!/usr/bin/env python3
"""Canonical nucleon / atom mass — the SINGLE entry point (facade).

ABSOLUTE MASS EXCISED (owner ruling 2026-08-11, bean qou-exam):
    The framework no longer claims/targets an ABSOLUTE nucleon/atom mass in MeV as
    a prediction. This facade stays the single entry point, but its MeV outputs are
    `m_e`-scaled REALIZATIONS of the dimensionless ratio (m_p/m_e, m_n/m_e) — a
    rendering for anyone who wants MeV, NOT a framework prediction. The predictive
    content is the ratio; do not report `m_p ≈ 938.27 MeV` as a prediction.
    Ruling: docs/audits/2026-08-11-excise-absolute-mass-notion.md. (No compute change.)

Owner ruling 2026-06-24: there is ONE correct [now: m_e-scaled] nucleon mass, the
**muon-anchored Hecke energy** (the production substrate-identity):

    m_p = dim V_{(2,1)} · (m_μ · F_Bor − |S_3| · m_e) = 2·(m_μ·F_Bor − 6·m_e)

    FIT (owner ruling 2026-11-18): the integer 12 = 2·6 in the −12·m_e term is
    SELECTED against m_p, not derived. It was read off the gap 2·m_μ·F_Bor − m_p
    ≈ 12·m_e (docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md);
    dim V_(2,1)·|S_3| is a factorisation of the integer, not a proof. At the
    proton pin q₀ is solved from this identity, so m_p is a round trip there.
    m_μ   = m_e · Vol(4₁) / ℏ_q²                      (muon = figure-8 knot 4₁)
    F_Bor = |tr_M(β_Bor)| · [3]_q! / q³               (dimensionless Hecke factor)
        → m_p ≈ 938.27 MeV, m_n ≈ 939.56 MeV  (matches CODATA; m_n predicted)

The c_q² (= 1/ℏ_q²) factor is applied ONCE, in the muon anchor m_μ, then
dressed by the *dimensionless* Borromean factor F_Bor.

DO NOT use the Borromean-volume forms for absolute nucleon/atom mass:
    m_e · Vol(𝓑₃) · λ_A / ℏ_q²       (per_knot_density_borromean)  → 966  (+2.96%, a FIT)
    m_e · Vol(𝓑₃) · tr_M / ℏ_q²      (per_knot_density_per_block)  → 406  (−57%)
Both apply 1/ℏ_q² to the wrong (Borromean) volume. They are DEPRECATED for
absolute mass (mass_vol_density emits a DeprecationWarning). Route every
absolute-mass consumer through THIS module instead.

Guardrail: docs/canonical-mass-formula-guardrail.md
Resolution: docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

_WITNESS = HERE / "m-p-substrate-identity-50dps.witness.json"


def _wrap_formattable_mpf(val):
    """Parse ``val`` (decimal string or mpf) at >= 50 dps into the module's one
    format-spec-compatible ``mp.mpf`` subclass (``_as_formattable_mpf``), so
    witness strings are never truncated to float64 (beans qou-4tui, qou-4ohh)."""
    import mpmath as mp
    with mp.workdps(max(50, mp.mp.dps)):
        return _as_formattable_mpf(str(val))


def _from_witness():
    if not _WITNESS.exists():
        return None
    preds = json.loads(_WITNESS.read_text())["data"]["predictions"]
    return (_wrap_formattable_mpf(preds["m_p_MeV"]),
            _wrap_formattable_mpf(preds["m_n_MeV"]))


def proton_neutron_mass_mev() -> tuple[float, float]:
    """Canonical (m_p, m_n) in MeV via the muon-anchored Hecke energy.

    Single canonical source: the git-tracked substrate-identity witness
    (50 dps), produced by ``m_p_substrate_identity_50dps.py``.

    There is deliberately NO formula fallback (owner directive 2026-07-19:
    "canonical derivation only — no silent fallback"). The prior fallback
    recomputed m_p from the F_Bor identity but derived m_n from the
    ``q_beta_toroidal_mev()`` near-match tower, whose Q_β (0.7823334279…)
    *diverges* from the canonical witness Q_β (0.7823343865… =
    ``q_beta_kashiwara_n2_mev``, which is the RETIRED MIXED BASE — z = 1
    Form A with a convention-D phase, labelled 2026-11-16; its +501 ppb on
    m_n is not a convention-D result, see
    ``qbeta/qbeta-mn-mixed-base-d-cells.witness.json``). A missing witness therefore raises with a
    regeneration instruction rather than silently substituting a
    non-canonical m_n. (Toroidal-tower over-claim audit:
    docs/audits/2026-07-19-qbeta-toroidal-tower-overclaim-audit.md; the
    2026-07-06 ruling "do not re-wire q_beta_toroidal_mev into
    canonical_mass.py".)
    """
    result = _from_witness()
    if result is None:
        raise FileNotFoundError(
            f"Canonical mass witness not found: {_WITNESS}\n"
            "Regenerate it with:\n"
            "    python3 computations/m_p_substrate_identity_50dps.py\n"
            "No formula fallback is provided — the canonical (m_p, m_n) come "
            "only from this witness (muon-anchored F_Bor identity + the "
            "canonical Kashiwara-N2 Q_β for m_n)."
        )
    return result


def proton_mass_mev() -> float:
    """Canonical proton mass (MeV) — muon-anchored Hecke energy ≈ 938.27."""
    return proton_neutron_mass_mev()[0]


def neutron_mass_mev() -> float:
    """Canonical neutron mass (MeV) — muon-anchored Hecke energy ≈ 939.56."""
    return proton_neutron_mass_mev()[1]


#: CAL-point relative 1σ uncertainties.
#  'canonical' = ideal math framework (CAL-2 = m_μ/m_e, 22 ppb);
#  'proton'    = physical-observations layer (CAL-2 = m_p/m_e, 0.06 ppb re-pin).
CAL_SIGMA_REL = {
    "canonical": {"q0": 2.2e-8, "m_e": 3.1e-10},   # muon-anchored CAL-2
    "proton":    {"q0": 6.0e-11, "m_e": 3.1e-10},  # proton-anchored CAL-2
}


def prediction_uncertainty_ppb(Z: int, N: int, layer: str = "canonical") -> float:
    """CAL-propagated reliability of the constituent mass Z·m_p + N·m_n, in ppb.

    Propagates the calibration-point 1σ (q₀ from CAL-2, m_e from CAL-1) through
    the canonical formula m_p(q₀, m_e) = 2(m_e·Vol(4₁)/ℏ_q²·F_Bor − 6·m_e) by
    finite difference, summing the q₀ and m_e contributions in quadrature. q₀
    and m_e enter both nucleons coherently, so we differentiate the constituent
    sum directly. The mass formula AMPLIFIES the CAL-2 error ~21× (ℏ_q=(q−1)/q
    is steep near q₀≈1.11): canonical (muon) → ~462 ppb; proton-layer → ~1.3 ppb.

    This is the theory error bar: a model deviation (err m_sym) far exceeding
    σ_pred is a genuine formula systematic, not calibration noise."""
    import mpmath as mp
    # Raised HERE, not at module scope, because `mp` is imported inside this
    # function — there is no module-level binding to assign to. Every mpmath
    # value below (q, m_e, the CAL sigmas) was otherwise built at mpmath's
    # default 15 dps, so what this producer emitted was honestly float64: no
    # fake precision to detect and no constant built too early, which is why the
    # padding / raw-float64 / import-time gates all passed it.
    # Gate: never_raises_dps_audit.py (bean qou-j6gb).
    mp.mp.dps = 50
    from m_p_substrate_identity_50dps import F_Bor
    from q_parameter import Q_MP as q0, vol_4_1_at
    from codata_constants import M_E_MEV
    from derived_masses import q_beta_kashiwara_n2_mev
    q = mp.mpf(str(q0)); m_e = mp.mpf(str(M_E_MEV))
    vol41 = vol_4_1_at(50)

    def constit(qq, mee):
        m_p = 2 * (mee * vol41 / ((qq - 1) / qq) ** 2 * F_Bor(qq) - 6 * mee)
        # RETIRED MIXED BASE (owner 2026-11-16): not a convention-D Q_β; see
        # qbeta/qbeta-mn-mixed-base-d-cells.witness.json for the D cells.
        m_n = m_p + q_beta_kashiwara_n2_mev() + mee  # Kashiwara b² Q_β (const in FD)
        return Z * m_p + N * m_n

    base = constit(q, m_e)
    sig = CAL_SIGMA_REL.get(layer, CAL_SIGMA_REL["canonical"])
    dq = q * mp.mpf(str(sig["q0"])); dme = m_e * mp.mpf(str(sig["m_e"]))
    d_q0 = (constit(q + dq, m_e) - constit(q - dq, m_e)) / 2
    d_me = (constit(q, m_e + dme) - constit(q, m_e - dme)) / 2
    return _wrap_formattable_mpf(
        mp.sqrt(d_q0 ** 2 + d_me ** 2) / abs(base) * mp.mpf(10) ** 9
    )


def _as_formattable_mpf(val):
    """Wrap an `mpmath.mpf` (or decimal string/number) in a subclass of `mp.mpf`
    that preserves full working precision in arithmetic while supporting
    standard float format specifiers (e.g. `f"{x:.6f}"`) at display boundaries.
    """
    import mpmath as mp

    class _FormattableMpf(mp.mpf):
        def __format__(self, format_spec: str) -> str:
            if not format_spec:
                return str(self)
            return format(float(self), format_spec)

        def __round__(self, n=None):
            return round(float(self), n)

        def _wrap(self, res):
            return _FormattableMpf(res) if isinstance(res, mp.mpf) else res

        def __add__(self, other):
            return self._wrap(super().__add__(other))

        def __radd__(self, other):
            return self._wrap(super().__radd__(other))

        def __sub__(self, other):
            return self._wrap(super().__sub__(other))

        def __rsub__(self, other):
            return self._wrap(mp.mpf(other).__sub__(mp.mpf(self)))

        def __mul__(self, other):
            return self._wrap(super().__mul__(other))

        def __rmul__(self, other):
            return self._wrap(super().__rmul__(other))

        def __truediv__(self, other):
            return self._wrap(super().__truediv__(other))

        def __rtruediv__(self, other):
            return self._wrap(mp.mpf(other).__truediv__(mp.mpf(self)))

        def __neg__(self):
            return self._wrap(super().__neg__())

        def __pos__(self):
            return self._wrap(super().__pos__())

        def __abs__(self):
            return self._wrap(super().__abs__())

    return _FormattableMpf(val)


def nucleon_mass_mev(species: str):
    """Canonical nucleon mass (MeV) at mpmath precision (bean qou-4tui).
    `species` ∈ {'p','proton','n','neutron'}.

    Returns an ``mpmath.mpf`` parsed directly from the decimal string in
    ``m-p-substrate-identity-50dps.witness.json`` at ≥50 dps (avoiding the
    ``float(...)`` truncation flagged in bean ``qou-4tui``), while supporting
    standard float format specifiers (e.g. ``f"{pred:.9f}"``) for legacy
    test/display callers.
    """
    import mpmath as mp
    s = species.lower()
    if s not in ("p", "proton", "n", "neutron"):
        raise ValueError(f"unknown nucleon species {species!r} (use 'p' or 'n')")
    if not _WITNESS.exists():
        # Delegate missing-witness FileNotFoundError to proton_neutron_mass_mev
        proton_neutron_mass_mev()
    preds = json.loads(_WITNESS.read_text())["data"]["predictions"]
    key = "m_p_MeV" if s in ("p", "proton") else "m_n_MeV"
    with mp.workdps(max(50, mp.mp.dps)):
        return _as_formattable_mpf(str(preds[key]))


def proton_qed_self_energy_borromean_mev(k_weighted: bool = False):
    """Proton connected 4th-order Borromean V³ electromagnetic self-energy M_p^{QED,conn} (MeV).

    NOT A DERIVED PREDICTION (2026-11-19, bean qou-99qc). The word dependence of the
    "connected" trace comes only from keeping quark pairs 1-2 and 2-3 and dropping 1-3; summed
    over all three pairs the insertion is word-independent (`trace_QPair_diff_word`). The m_e
    scale and the weighting options were chosen against targets. Do not cite as a derived split;
    the canonical masses are `proton_neutron_mass_mev`.

    Implements Lean theorem
    `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3`:
        tr_conn(p, V³) = (1/3) tr((Q_{12}^{(p)} + Q_{23}^{(p)}) V_p³)
                       = −2(q² − 1)⁴(q⁴ + q² + 1) / (27 q⁶)
        M_p^{QED,conn} = m_e · w(q) · |tr_conn(p, V³)|,
    where w(q) = q if `k_weighted=True` and 1 otherwise.
    Reads `two_term_borromean_qed_diagnostics` from `m-p-substrate-identity-50dps.witness.json`
    when available, with a direct 50-dps fallback computation so it works regardless of
    witness regeneration order. Preserves full ≥50-dps mpmath precision via `_as_formattable_mpf`.
    """
    import mpmath as mp
    if _WITNESS.exists():
        data = json.loads(_WITNESS.read_text()).get("data", {})
        diag = data.get("two_term_borromean_qed_diagnostics", {})
        key = "M_p_QED_conn_Kp_MeV" if k_weighted else "M_p_QED_conn_MeV"
        if key in diag:
            with mp.workdps(max(50, mp.mp.dps)):
                return _as_formattable_mpf(str(diag[key]))
    import _path_bridge  # noqa: F401
    with mp.workdps(max(50, mp.mp.dps)):
        from q_parameter import Q_MP as q0
        from codata_constants import M_E_MEV
        q = mp.mpf(str(q0))
        m_e = mp.mpf(str(M_E_MEV))
        q2 = q ** 2
        tr_conn_p = -2 * ((q2 - 1) ** 4) * (q2 ** 2 + q2 + 1) / (27 * (q2 ** 3))
        w = q if k_weighted else mp.mpf(1)
        return _as_formattable_mpf(m_e * w * abs(tr_conn_p))


def np_qed_splitting_borromean_conn_mev(weighting: str = "plain"):
    """(n − p) connected 4th-order Borromean V³ QED mass splitting Δm_QED^{conn} (MeV).

    NOT A DERIVED PREDICTION (2026-11-19, bean qou-99qc). The word dependence of the
    "connected" trace comes only from keeping quark pairs 1-2 and 2-3 and dropping 1-3; summed
    over all three pairs the insertion is word-independent (`trace_QPair_diff_word`). The m_e
    scale and the weighting options were chosen against targets. Do not cite as a derived split;
    the canonical masses are `proton_neutron_mass_mev`.

    Implements Lean theorems
    `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjn_borromeanV3_connected` and
    `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3`:
        Δtr_conn(V³) = +(q² − 1)⁴(4q⁴ + q² + 4) / (27 q⁶)
        Δm_QED^{conn} = −m_e · Δtr_conn^{(w)}(V³) < 0.
    Reads `two_term_borromean_qed_diagnostics` from `m-p-substrate-identity-50dps.witness.json`
    when available, with a direct 50-dps fallback computation for `weighting` in
    `{'plain', 'KnKp', 'Kp3', 'q'}`. Preserves full ≥50-dps mpmath precision via `_as_formattable_mpf`.
    """
    import mpmath as mp
    if _WITNESS.exists():
        data = json.loads(_WITNESS.read_text()).get("data", {})
        diag = data.get("two_term_borromean_qed_diagnostics", {})
        key_map = {
            "plain": "Delta_m_QED_conn_MeV",
            "KnKp": "Delta_m_QED_conn_KnKp_MeV",
            "Kp3": "Delta_m_QED_conn_Kp3_MeV",
            "q": "Delta_m_QED_conn_q_MeV",
        }
        key = key_map.get(weighting)
        if key and key in diag:
            with mp.workdps(max(50, mp.mp.dps)):
                return _as_formattable_mpf(str(diag[key]))
    import _path_bridge  # noqa: F401
    with mp.workdps(max(50, mp.mp.dps)):
        from q_parameter import Q_MP as q0
        from codata_constants import M_E_MEV
        q = mp.mpf(str(q0))
        m_e = mp.mpf(str(M_E_MEV))
        q2 = q ** 2
        q2_m1_4 = (q2 - 1) ** 4
        denom = 27 * (q2 ** 3)
        tr_conn_p = -2 * q2_m1_4 * (q2 ** 2 + q2 + 1) / denom
        tr_conn_n = q2_m1_4 * (2 * (q2 ** 2) - q2 + 2) / denom
        if weighting == "plain":
            delta_tr = tr_conn_n - tr_conn_p
        elif weighting == "KnKp":
            delta_tr = (tr_conn_n / q) - (q * tr_conn_p)
        elif weighting == "Kp3":
            delta_tr = tr_conn_n - (q * tr_conn_p)
        elif weighting == "q":
            delta_tr = q * (tr_conn_n - tr_conn_p)
        else:
            raise ValueError(
                f"np_qed_splitting_borromean_conn_mev: unknown weighting {weighting!r} "
                "(use 'plain', 'KnKp', 'Kp3', or 'q')"
            )
        return _as_formattable_mpf(-m_e * delta_tr)


def neutron_mass_two_term_mev(weighting: str = "plain"):
    """Two-term neutron mass m_n^{two-term} = m_n + Δm_QED^{conn}(V³) in MeV.

    NOT A DERIVED PREDICTION (2026-11-19, bean qou-99qc). The word dependence of the
    "connected" trace comes only from keeping quark pairs 1-2 and 2-3 and dropping 1-3; summed
    over all three pairs the insertion is word-independent (`trace_QPair_diff_word`). The m_e
    scale and the weighting options were chosen against targets. Do not cite as a derived split;
    the canonical masses are `proton_neutron_mass_mev`.

    Combines the canonical neutron mass `neutron_mass_mev()` with the connected
    4th-order Borromean V³ QED splitting `np_qed_splitting_borromean_conn_mev(weighting)`.
    At `weighting='plain'`, m_n^{two-term} ≈ 939.5655543 MeV (+147.0 ppb vs CODATA,
    reducing the +501.3 ppb Convention-D residual by 70.7% without free parameters).
    Preserves full ≥50-dps mpmath precision via `_as_formattable_mpf`.
    """
    import mpmath as mp
    if weighting == "plain" and _WITNESS.exists():
        data = json.loads(_WITNESS.read_text()).get("data", {})
        diag = data.get("two_term_borromean_qed_diagnostics", {})
        if "m_n_two_term_MeV" in diag:
            with mp.workdps(max(50, mp.mp.dps)):
                return _as_formattable_mpf(str(diag["m_n_two_term_MeV"]))
    with mp.workdps(max(50, mp.mp.dps)):
        mn = nucleon_mass_mev("n")
        dm_qed = np_qed_splitting_borromean_conn_mev(weighting=weighting)
        return _as_formattable_mpf(mn + dm_qed)


def gpmt_dmod_111(q=None):
    """Geer–Patureau-Mirand–Turaev (GPMT) modified quantum dimension d_mod((1,1,1))
    on the ≥3-row ideal I_{≥3} ⊂ H_3(q) under Convention D (`z_D = q³/(q²+1)`).

    Implements Lean theorem `QOU.MassTheory.GPMTThreeRowCumulantBridge.dMod111`:
        d_mod((1,1,1)) = −q³ / ((q² + 1)(q⁴ + q² + 1)) = −1 / ([2]_q [3]_q) < 0.
    """
    import mpmath as mp
    import _path_bridge  # noqa: F401
    with mp.workdps(max(50, mp.mp.dps)):
        if q is None:
            from q_parameter import Q_50_DIGIT_STR
            qx = mp.mpf(Q_50_DIGIT_STR)
        else:
            qx = mp.mpf(str(q))
        q2 = qx ** 2
        val = -(qx ** 3) / ((q2 + 1) * (q2 ** 2 + q2 + 1))
        return _as_formattable_mpf(val)


def gpmt_dmod_211(q=None):
    """GPMT modified quantum dimension d_mod((2,1,1)) in H_4(q) under Convention D.

    Implements Lean theorem `QOU.MassTheory.H4GPMTModifiedDimensionCumulants.dMod211`:
        d_mod((2,1,1)) = −q³(q⁴ + q² + 1) / ((q² + 1)³(q⁴ + 1)) = −[3]_q / ([2]_q² [4]_q) < 0.
    """
    import mpmath as mp
    import _path_bridge  # noqa: F401
    with mp.workdps(max(50, mp.mp.dps)):
        if q is None:
            from q_parameter import Q_50_DIGIT_STR
            qx = mp.mpf(Q_50_DIGIT_STR)
        else:
            qx = mp.mpf(str(q))
        q2 = qx ** 2
        val = -(qx ** 3) * (q2 ** 2 + q2 + 1) / (((q2 + 1) ** 3) * (q2 ** 2 + 1))
        return _as_formattable_mpf(val)


def gpmt_dmod_1111(q=None):
    """GPMT modified quantum dimension d_mod((1,1,1,1)) in H_4(q) under Convention D.

    Implements Lean theorem `QOU.MassTheory.H4GPMTModifiedDimensionCumulants.dMod1111`:
        d_mod((1,1,1,1)) = +q⁷ / ((q² + 1)³(q⁴ + 1)(q⁴ + q² + 1))
                         = +1 / ([2]_q² [3]_q [4]_q) > 0.
    """
    import mpmath as mp
    import _path_bridge  # noqa: F401
    with mp.workdps(max(50, mp.mp.dps)):
        if q is None:
            from q_parameter import Q_50_DIGIT_STR
            qx = mp.mpf(Q_50_DIGIT_STR)
        else:
            qx = mp.mpf(str(q))
        q2 = qx ** 2
        val = (qx ** 7) / (((q2 + 1) ** 3) * (q2 ** 2 + 1) * (q2 ** 2 + q2 + 1))
        return _as_formattable_mpf(val)


def gpmt_three_row_cumulants(q=None) -> dict:
    """Evaluate all Lean-proved GPMT ≥3-row modified-dimension cumulants and
    extensive sums at `q` (default: canonical 50-dps proton pin `Q_50_DIGIT_STR`).

    Covers both:
      - `QOU.MassTheory.GPMTThreeRowCumulantBridge` (uniform `d_mod((1,1,1))` scaling
        for `A = 2, 3, 4`: `mu2GPMT`, `mu3GPMT`, `mu4GPMT`, `BextGPMT(A)`), and
      - `QOU.MassTheory.H4GPMTModifiedDimensionCumulants` (per-partition `H_4(q)`
        `d_mod((2,1,1))` and `d_mod((1,1,1,1))` weighting: `sRow3GPMT_H4(4)`, `mu4GPMT_H4`).
    """
    import mpmath as mp
    with mp.workdps(max(50, mp.mp.dps)):
        d111 = gpmt_dmod_111(q)
        d211 = gpmt_dmod_211(q)
        d1111 = gpmt_dmod_1111(q)
        mu2 = _as_formattable_mpf(mp.mpf(0))
        mu3 = _as_formattable_mpf(-d111)
        mu4_uniform = _as_formattable_mpf(2 * d111)
        bext2 = _as_formattable_mpf(mp.mpf(0))
        bext3 = _as_formattable_mpf(-d111)
        bext4_uniform = _as_formattable_mpf(-6 * d111)
        srow3_h4_4 = _as_formattable_mpf(-3 * d211 + d1111)
        mu4_h4 = _as_formattable_mpf(srow3_h4_4 - 4 * mu3)
        bext4_h4 = _as_formattable_mpf(4 * mu3 + srow3_h4_4)
        return {
            "dMod111": d111,
            "dMod211": d211,
            "dMod1111": d1111,
            "mu2GPMT": mu2,
            "mu3GPMT": mu3,
            "mu4GPMT_uniform": mu4_uniform,
            "BextGPMT_2": bext2,
            "BextGPMT_3": bext3,
            "BextGPMT_4_uniform": bext4_uniform,
            "sRow3GPMT_H4_4": srow3_h4_4,
            "mu4GPMT_H4": mu4_h4,
            "BextGPMT_4_H4": bext4_h4,
        }


def inter_nucleon_pair_charge(Z: int) -> int:
    """Pairwise inter-nucleon electromagnetic bond count ∑_{i<j} Q_i Q_j = Z(Z − 1)/2.

    Matches `QOU.MassTheory.GPMTThreeRowCumulantBridge.pairChargeA3` for `A = 3`
    (`Z = 1 -> 0` for `³H`, `Z = 2 -> 1` for `³He`).
    """
    return Z * (Z - 1) // 2


if __name__ == "__main__":
    mp_, mn_ = proton_neutron_mass_mev()
    mp_qed_ = proton_qed_self_energy_borromean_mev()
    dm_qed_ = np_qed_splitting_borromean_conn_mev()
    mn_2t_ = neutron_mass_two_term_mev()
    print(f"canonical m_p = {mp_:.6f} MeV   m_n = {mn_:.6f} MeV "
          f"(muon-anchored Hecke energy, substrate-identity)")
    print(f"two-term Borromean QED: M_p^QED,conn = {mp_qed_*1e3:+.5f} keV   "
          f"Delta_m_QED^conn = {dm_qed_*1e3:+.5f} keV   m_n^two-term = {mn_2t_:.7f} MeV")
