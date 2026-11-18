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


def _from_witness() -> tuple[float, float] | None:
    if not _WITNESS.exists():
        return None
    preds = json.loads(_WITNESS.read_text())["data"]["predictions"]
    return float(preds["m_p_MeV"]), float(preds["m_n_MeV"])


def proton_neutron_mass_mev() -> tuple[float, float]:
    """Canonical (m_p, m_n) in MeV via the muon-anchored Hecke energy.

    Single canonical source: the git-tracked substrate-identity witness
    (50 dps), produced by ``m_p_substrate_identity_50dps.py``.

    There is deliberately NO formula fallback (owner directive 2026-07-19:
    "canonical derivation only — no silent fallback"). The prior fallback
    recomputed m_p from the F_Bor identity but derived m_n from the
    ``q_beta_toroidal_mev()`` near-match tower, whose Q_β (0.7823334279…)
    *diverges* from the canonical witness Q_β (0.7823343865… =
    ``q_beta_kashiwara_n2_mev``). A missing witness therefore raises with a
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
        m_n = m_p + q_beta_kashiwara_n2_mev() + mee  # Kashiwara b² Q_β (const in FD)
        return Z * m_p + N * m_n

    base = constit(q, m_e)
    sig = CAL_SIGMA_REL.get(layer, CAL_SIGMA_REL["canonical"])
    dq = q * mp.mpf(str(sig["q0"])); dme = m_e * mp.mpf(str(sig["m_e"]))
    d_q0 = (constit(q + dq, m_e) - constit(q - dq, m_e)) / 2
    d_me = (constit(q, m_e + dme) - constit(q, m_e - dme)) / 2
    return float(mp.sqrt(d_q0 ** 2 + d_me ** 2) / abs(base) * mp.mpf(10) ** 9)


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

    class _FormattableMpf(mp.mpf):
        def __format__(self, format_spec: str) -> str:
            if not format_spec:
                return str(self)
            return format(float(self), format_spec)

        def _wrap(self, res):
            return _FormattableMpf(res) if isinstance(res, mp.mpf) else res

        def __add__(self, other):
            return self._wrap(super().__add__(other))

        def __radd__(self, other):
            return self._wrap(super().__radd__(other))

        def __sub__(self, other):
            return self._wrap(super().__sub__(other))

        def __rsub__(self, other):
            return self._wrap(super().__rsub__(other))

        def __mul__(self, other):
            return self._wrap(super().__mul__(other))

        def __rmul__(self, other):
            return self._wrap(super().__rmul__(other))

        def __truediv__(self, other):
            return self._wrap(super().__truediv__(other))

        def __rtruediv__(self, other):
            return self._wrap(super().__rtruediv__(other))

        def __neg__(self):
            return self._wrap(super().__neg__())

        def __pos__(self):
            return self._wrap(super().__pos__())

        def __abs__(self):
            return self._wrap(super().__abs__())

    s = species.lower()
    if s not in ("p", "proton", "n", "neutron"):
        raise ValueError(f"unknown nucleon species {species!r} (use 'p' or 'n')")
    if not _WITNESS.exists():
        # Delegate missing-witness FileNotFoundError to proton_neutron_mass_mev
        proton_neutron_mass_mev()
    preds = json.loads(_WITNESS.read_text())["data"]["predictions"]
    key = "m_p_MeV" if s in ("p", "proton") else "m_n_MeV"
    with mp.workdps(max(50, mp.mp.dps)):
        return _FormattableMpf(str(preds[key]))


if __name__ == "__main__":
    mp_, mn_ = proton_neutron_mass_mev()
    print(f"canonical m_p = {mp_:.6f} MeV   m_n = {mn_:.6f} MeV "
          f"(muon-anchored Hecke energy, substrate-identity)")
