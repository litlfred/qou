#!/usr/bin/env python3
"""mass_table_comprehensive.py — full mass/binding table at current production tier.

Computes absolute masses AND binding energies for all nuclei from
proton (A=1) through ¹²C (A=12), using the current production
infrastructure:

  ABSOLUTE MASS — via the `canonical_mass` facade (muon-anchored Hecke
  energy), NOT the λ_A Borromean form:

    m_p = 2·(m_μ·F_Bor − 6·m_e),  m_μ = m_e·Vol(4₁)/ℏ_q²,
    F_Bor = |tr_M(β_Bor)|·[3]_q!/q³              → ≈938.27 / 939.56 MeV

  Composite nucleus mass = Z·m_p + N·m_n − B(K).

  ⚠ The form `m(K) = m_e·[Vol(𝓑₃)/ℏ_q²]·λ_A · (1 ± Δm/(2·M_N))` that this
  docstring previously advertised as "the current production tier" was
  **removed 2026-06-24** (owner ruling): applying 1/ℏ_q² to the *Borromean*
  volume with ρ=λ_A is a CODATA-implied FIT giving m_p ≈ 966 (+2.96%).
  λ_A is still computed here, but **only as a diagnostic column** (see
  `linking_weight_family_a` below) — it does not enter the mass.
  See docs/canonical-mass-formula-guardrail.md.

  Δm/M_N = substrate-pure flavor-split (PROVED per PR #942) remains the
  p/n split applied to the facade's nucleon masses.

  BINDING ENERGY:
    For A ≤ 3: binding_canonical with use_closed_form=True (PR #921;
    the Phase 5q closed form via tr_M_via_wenzl_bridge_mpfr).
    For A = 4: binding_canonical (H_12 Phase-1 extract wired via
    #944; currently closed-form path uses strict_averaged).
    For A ≥ 5: flagged as "not yet computed" (gated on H_12 Phase-2
    + higher H_{3A} kernels).

  KNOT ATLAS CROSS-REFERENCE:
    Each entry carries the methodology tag from the recursive atom
    knot atlas (prop:recursive-atom-knot-atlas) — principled-derivation,
    manual-historical-volume-match, magic-A-formula, recursive-on-⁴He,
    or not-computed.

Emits: mass-table-comprehensive.witness.json

Per AGENTS.md "Long-compute logging discipline": periodic progress
lines with wall + ETA.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_E_MEV,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
    Q_BETA_MEV,
)
from _li_2_q_util import (  # noqa: E402
    linking_weight_family_a,
)
from canonical_mass import proton_neutron_mass_mev  # noqa: E402  (canonical facade)
from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from codata_constants import AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []


def _dp(x, places: int = 6):
    """Serialize one table cell at its declared decimal width, as a STRING.

    Replaces `round(x, <places>)`, which emitted a JSON float. This table is
    the single largest raw-float64 witness in the corpus — 75,112 of the
    487,597 fields in `raw-float64-baseline.json`, 15.4 % of the whole
    backlog — and 74,850 of those are five columns of `round(..., 6)` over
    14,972 rows.

    **This is a TYPE fix, not a precision gain, and the two should not be
    conflated.** The arithmetic upstream of it is now `mpf` end to end (that
    is the other half of this change), but the values here are quantities of
    order 1e0–1e5 MeV serialized to six decimal places — ~1e-10 relative,
    six orders above binary64's floor. So the float64 that was in the
    arithmetic could not reach these digits, and the expected outcome of the
    whole drain is that **not one printed digit moves**. That is a checkable
    prediction, and it was checked; see the PR.

    Full-width serialization (`_precision.fmt`, 60 significant digits) was
    considered and rejected *here specifically*: it would roughly double a
    9.9 MB witness to print digits this file's own `set_description` says are
    meaningless — the per-generator Wedderburn volumes use H_3 weights at
    every A, so for A > 1 the weights are systematically wrong and these rows
    are "a coarse diagnostic, not a precision prediction"
    (docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md). Six decimals is a
    declared display convention, and it is now declared in one place instead
    of twenty-three call sites.

    `mpf` implements `__format__`, so `f"{x:.6f}"` is exact-then-round on the
    full-precision value rather than round-of-a-double.
    """
    return None if x is None else f"{x:.{places}f}"


def _fmt_or_none(x):
    """`_precision.fmt`, but preserving `None`.

    `fmt` short-circuits every non-mpf to `str(value)`, so `fmt(None)` is the
    four-character string `"None"` — which JSON-encodes as a *value*, not a
    null. Two of the summary fields below are `.get()` misses on the
    substrate-identity path (documented in the NOTE beside them), so they are
    `None` on every run of this producer.
    """
    return None if x is None else fmt(x)


# AME 2020 binding energies (MeV) — used for comparison only.
# Source: Wang et al., Chinese Physics C 45 (2021) 030003.
AME_BINDING = {
    "p": 0.0, "n": 0.0,
    "D": 2.22452, "T": float(AME_B_TRITIUM_MEV_VALIDATION), "3He": float(AME_B_HE3_MEV_VALIDATION),
    "4He": float(AME_B_HE4_MEV_VALIDATION), "6Li": float(AME_B_LI6_MEV_VALIDATION), "7Li": 39.2445,
    "9Be": 58.165, "10B": 64.751, "11B": 76.205,
    "12C": 92.162, "13C": 97.108, "14N": 104.659, "15N": 115.492,
    "16O": 127.619, "17O": 131.763, "18O": 139.808,
    "19F": 147.801, "20Ne": 160.645, "21Ne": 167.406, "22Ne": 177.770,
    "23Na": 186.564, "24Mg": 198.257, "25Mg": 205.588, "26Mg": 216.681,
    "27Al": 224.952, "28Si": 236.537, "29Si": 245.011, "30Si": 255.620,
    "31P": 262.917, "32S": 271.781, "33S": 280.422, "34S": 291.839,
    "36S": 308.714, "35Cl": 298.210, "37Cl": 317.100,
    "36Ar": 306.716, "38Ar": 327.343, "40Ar": 343.810,
    "39K": 333.723, "41K": 351.619,
    "40Ca": 342.052, "42Ca": 361.895, "43Ca": 369.828,
    "44Ca": 380.960, "46Ca": 398.769, "48Ca": 416.001,
    "45Sc": 387.849,
    "46Ti": 398.194, "47Ti": 407.073, "48Ti": 418.699,
    "49Ti": 426.841, "50Ti": 437.780,
    "50V": 434.794, "51V": 445.842,
    "50Cr": 435.049, "52Cr": 456.345, "53Cr": 464.287, "54Cr": 474.008,
    "55Mn": 482.071,
    "54Fe": 471.764, "56Fe": 492.254, "57Fe": 499.900, "58Fe": 509.946,
}

# CODATA masses (MeV) for cross-check
# The five `M_*_MEV_VALIDATION` constants are already `mpf`; `float(...)`
# downcast the reference values that every `m_err_pct` in the table is
# measured AGAINST, which is the last place to spend precision.
CODATA_MASS = {
    "p": M_P_MEV_VALIDATION,
    "n": M_N_MEV_VALIDATION,
    "D": M_D_MEV_VALIDATION,
    "T": M_T_MEV_VALIDATION,
    "3He": None,  # not in codata_constants; derive from AME
    "4He": M_HE4_MEV_VALIDATION,
}

# Atlas methodology tags (from recursive-atom-knot-atlas.md)
ATLAS_TAG = {
    "p": "principled-derivation",
    "n": "principled-derivation",
    "D": "principled-derivation (Q-CLT proxy)",
    "T": "principled-derivation (Q-CLT proxy)",
    "3He": "principled-derivation (Q-CLT proxy)",
    "4He": "principled-derivation (Q-CLT proxy)",
    "6Li": "principled-derivation (Q-CLT proxy)",
    "7Li": "principled-derivation (Q-CLT proxy)",
    "9Be": "principled-derivation (Q-CLT proxy)",
    "10B": "principled-derivation (Q-CLT proxy)",
    "12C": "principled-derivation (Q-CLT proxy)",
}

ELEMENTS = [
    "n", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

ISOTOPES = [("p", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2)]
# Add grid of theoretical isotopes up to Z=118, roughly spanning from proton to neutron drip line
for z in range(2, 119):
    n_min = max(0, int(0.5 * z) - 2)
    n_max = int(2.5 * z) + 5
    for n in range(n_min, n_max + 1):
        a = z + n
        if a > 4:  # Avoid duplicates with explicitly added H, He isotopes
            sym = f"{a}{ELEMENTS[z]}"
            ISOTOPES.append((sym, z, n))


def borromean_mass_prediction(
    q: mp.mpf, Z: int, N: int, atom_name: str = None,
) -> dict:
    """Predict absolute mass of nucleus (Z, N) from the canonical nucleon
    masses (+ substrate-pure flavor-split).

    m_p_pred, m_n_pred = `canonical_mass.proton_neutron_mass_mev()`
        — the muon-anchored Hecke energy m_p = 2·(m_μ·F_Bor − 6·m_e).
    m_nucleus = Z · m_p_pred + N · m_n_pred − B(K)

    ⚠ The name `borromean_mass_prediction` and the formula
    `m_avg = m_e · Vol(𝓑₃)/ℏ_q² · λ_A` this docstring used to state are
    **historical**: that λ_A route is a fit (m_p ≈ 966, +2.96%) and was
    removed 2026-06-24 by owner ruling — see the inline comment below and
    docs/canonical-mass-formula-guardrail.md. The function name is kept to
    avoid churning call sites; it no longer describes the mass route.

    If Vol(K) is available for the atom, a per-knot
    `m(K) = m_e · per_knot_density_per_block(Vol(K), tr_M(K), q)` column is
    additionally reported as the TRUTH-TRACKING OVERRIDE. That per-block
    reading is **not** a canonical absolute mass either (it gives
    m_p ≈ 406, −57%); per the guardrail `per_knot_density_per_block` is valid
    for binding *ratios*, where the scale cancels.
    """
    m_e = mp.mpf(str(M_E_MEV))

    # Canonical nucleon masses via the single facade — the muon-anchored Hecke
    # energy m_p = 2(m_μ·F_Bor − 6·m_e) (substrate-identity, ≈938.27/939.56).
    # The λ_A Family-A fallback (m_e·Vol(𝓑₃)·ρ/ℏ_q²) is a FIT and was removed
    # 2026-06-24 (owner ruling) — see docs/canonical-mass-formula-guardrail.md.
    _mp_can, _mn_can = proton_neutron_mass_mev()
    m_p_pred = mp.mpf(str(_mp_can))
    m_n_pred = mp.mpf(str(_mn_can))
    _source = "canonical_mass facade (muon-anchored Hecke energy)"
    linking_weight = linking_weight_family_a(q)   # reported for diagnostics only

    # Base definition (q-CLT statistical average). The two operands are mpf
    # by construction three lines up; `float(...)` on each of them collapsed
    # them to binary64 immediately after the `mp.mpf(str(...))` that had just
    # parsed them faithfully, so the sum was a double for no reason.
    m_nucleus_unbound_approx = Z * m_p_pred + N * m_n_pred

    # TRUTH-TRACKING OVERRIDE (per-knot VolDensity, symbolic top-down)
    m_nucleus_unbound_symbolic = None
    vol_K_used = None
    if atom_name is not None:
        try:
            # (no `import json` here: `record_upstream` parses the file itself
            # and returns the body, so the local alias was dead.)
            vol_witness = HERE / "per-atom-hyperbolic-volume.witness.json"
            if vol_witness.exists():
                vol_data = record_upstream(vol_witness, _UPSTREAM_RECORDS)["data"]
                vol_key = f"Vol_{atom_name}"
                if vol_key in vol_data:
                    from closed_form_tau_M import compute_tau_M_nucleon_H3, closed_form_tau_M
                    from _li_2_q_util import per_knot_density_per_block
                    tau_p_H3 = compute_tau_M_nucleon_H3("p", q)
                    tau_n_H3 = compute_tau_M_nucleon_H3("n", q)
                    tr_M_K = closed_form_tau_M(Z, N, q, tau_p_H3, tau_n_H3)
                    vol_K_used = mp.mpf(str(vol_data[vol_key]))
                    m_pb = m_e * per_knot_density_per_block(vol_K_used, tr_M_K, q)
                    m_nucleus_unbound_symbolic = m_pb
                    _source += " [OVERRIDE: per-knot VolDensity]"
                else:
                    _source += " [ERROR: missing Vol(K)]"
            else:
                _source += " [ERROR: missing per-atom-hyperbolic-volume.witness.json]"
        except Exception as e:
            _source += f" [ERROR: {e}]"

    m_avg = (m_p_pred + m_n_pred) / 2
    # Every value below stays `mpf`. This is an INTERNAL dict — the caller
    # decides the serialized width (`_dp`) — so casting to `float` here only
    # threw away digits on the way between two places that both wanted them.
    return {
        "linking_weight_family_a": linking_weight,
        "source": _source,
        "m_avg_MeV": m_avg,
        "m_p_pred_MeV": m_p_pred,
        "m_n_pred_MeV": m_n_pred,
        "m_nucleus_unbound_approx_MeV": m_nucleus_unbound_approx,
        "m_nucleus_unbound_symbolic_MeV": m_nucleus_unbound_symbolic,
        "vol_K": vol_K_used,
        "is_per_knot": m_nucleus_unbound_symbolic is not None,
    }


def try_binding_canonical(Z: int, N: int, q_str: str) -> dict | None:
    """Try to compute binding energy via binding_canonical with
    closed-form path. Returns None if the computation fails.

    Computes BOTH Q_β-scaled (legacy) and E₀×q⁻¹-scaled (PR #1361)
    results for comparison."""
    A = Z + N
    if A < 2:
        return {"B_pred_MeV": 0.0, "B_E0_MeV": 0.0, "method": "no binding (single nucleon)"}

    # If A>12 and alpha cluster, try alpha_cluster_binding first
    if A > 12 and Z == N and A % 4 == 0:
        try:
            from alpha.alpha_cluster_recursion import alpha_cluster_binding
            r = alpha_cluster_binding(Z, N)
            if r.get("applicable"):
                return {
                    "B_pred_MeV": float(r["B_pred_MeV"]),
                    "B_E0_MeV": float(r["B_pred_MeV"]),  # same scale
                    "method": "alpha_cluster_recursion (recursive-on-⁴He)",
                    "formula": r.get("formula"),
                }
        except Exception as e:
            print(
                f"WARN: alpha_cluster_binding failed for (Z={Z}, N={N}, A={A}): {e!s}",
                file=sys.stderr,
            )

    try:
        from binding_canonical import binding_canonical
        # `Q_BETA_MEV` is already an `mpf`; `float(Q_BETA_MEV)` downcast the
        # MeV-dimensioned multiplier of the whole formula before it entered.
        r = binding_canonical(
            Z, N,
            Q_beta_n_mev=Q_BETA_MEV,
            use_closed_form=True,
            verbose=False,
        )
        if r.get("status") != "solved":
            return {"B_pred_MeV": None, "method": f"binding_canonical failed: {r.get('status')}", "error": r.get("error")}

        B_qbeta = r.get("B_MeV")

        # E₀×q⁻¹ scale (PR #1361): B = E₀ × Δtr × (1-ℏ_q)
        # where E₀ = m_e/(q₀(q₀-1)), (1-ℏ_q) = q₀⁻¹
        #
        # Three `float(...)` casts used to sit inside this two-line
        # calculation, one of them around a product of two mpf values
        # (`q_val * (q_val - 1)`) that had to be computed at full precision
        # first in order to be thrown away. `q_str` is the 50-digit q₀
        # string; there is no reason for the scale built from it to be a
        # double.
        import mpmath as _mp
        q_val = _mp.mpf(q_str)
        E_0 = M_E_MEV / (q_val * (q_val - 1))
        scale_ratio = E_0 / Q_BETA_MEV / q_val
        # `if B_qbeta` (the previous guard) also nulls a legitimately ZERO
        # binding; the question being asked is whether the value exists.
        B_E0 = B_qbeta * scale_ratio if B_qbeta is not None else None

        return {
            "B_pred_MeV": B_E0,  # use E₀×q⁻¹ as primary
            "B_qbeta_MeV": B_qbeta,
            "tr_M_atom": r.get("tr_M_atom"),
            "tr_M_free": r.get("tr_M_free"),
            "method": "E₀×q⁻¹ (PR #1361)" + (" (closed-form)" if A <= 3 else " (symbolic)"),
        }
    except Exception as e:
        return {"B_pred_MeV": None, "method": f"error: {e}"}

def try_binding_symbolic_log_trace(Z: int, N: int) -> dict | None:
    """Compute binding energy via exact symbolic log trace (active partitions)."""
    if Z + N < 2:
        return None
    try:
        from binding_canonical import binding_canonical
        import math
        import mpmath as mp
        from codata_constants import M_E_MEV
        
        # Use closed-form to evaluate trace over active partitions (no explosion)
        r = binding_canonical(Z, N, use_closed_form=True, verbose=False)
        if r.get("status") != "solved":
            return None
            
        # `tr_M_atom` is the decimal string `binding_canonical` serializes at
        # the compute dps. `float(...)` read that decimal as a binary64 and
        # discarded ~34 of its digits before `log` ever saw it — the same
        # defect `binding_factor_f_sequence.py` documents at length for these
        # exact two fields. `mpmathify` parses a decimal as a decimal.
        # (`use_closed_form=True` traces are real by construction, so a
        # complex repr cannot reach here; the strip is defensive.)
        tr_s = str(r["tr_M_atom"]).replace("(", "").replace(")", "")
        tr = mp.mpmathify(tr_s.split("+")[0] if "j" in tr_s else tr_s)
        if tr <= 0:
            return None

        # B = -alpha * ln|tau_M|.  `float(mp.catalan)` truncated a constant
        # mpmath will supply at any precision, to 17 digits, in order to
        # multiply it by an m_e that was itself already mpf.
        alpha = M_E_MEV * 8 * mp.catalan
        B_pred = -alpha * mp.log(tr)

        return {
            "B_pred_MeV": B_pred,
            "method": "Exact symbolic (-alpha * ln|tau_M|)"
        }
    except Exception as e:
        return None

def try_binding_q_clt_proxy(Z: int, N: int) -> dict | None:
    """Compute binding energy via the rigorous Q-CLT per-crossing ln|V_i| proxy."""
    if Z + N < 2:
        return None
    try:
        from hecke_core import atom_per_generator_volumes
        import math
        import mpmath as mp
        from codata_constants import M_E_MEV
        
        vols = atom_per_generator_volumes(Z, N, include_inter=True)
        # This accumulates 3A logs — up to ~1254 terms at A = 418 — and it did
        # so in binary64. Be precise about what moving it to mpf buys and what
        # it does not: `atom_per_generator_volumes` may itself hand back
        # doubles, in which case the INPUTS are still f64 and no digit is
        # recovered. What is fixed is the SUMMATION, whose error grew with A
        # and so was worst exactly where the table is least checked. Claiming
        # more than that would be the "float64 agreement reported as exact"
        # error AGENTS.md forbids.
        sum_log_V = mp.mpf(0)
        _tiny = mp.mpf("1e-30")
        for v in vols:
            x = v["full"] if isinstance(v, dict) else v
            xm = mp.mpmathify(x) if isinstance(x, str) else mp.mpf(x)
            if abs(xm) > _tiny:
                sum_log_V += mp.log(abs(xm))

        # Binding energy is the negative of the mass correction
        alpha = M_E_MEV * 8 * mp.catalan
        B_pred = -alpha * sum_log_V
        
        return {
            "B_pred_MeV": B_pred,
            "method": "Q-CLT derivation (alpha * sum ln|V|)"
        }
    except Exception as e:
        return None


def main() -> int:
    t_start = time.monotonic()
    builder = WitnessBuilder(
        "mass-table-comprehensive",
        engine="mpmath",
        start_time=t_start,
    )
    # `add_upstream_records` is deliberately NOT called here. `_UPSTREAM_RECORDS`
    # is filled by `record_upstream(...)` inside `borromean_mass_prediction`,
    # which the row loop below calls once per isotope — so at this point the
    # list is still empty, and attaching it here recorded nothing. The
    # regenerated witness had no `upstream_witness_hashes` key at all despite
    # ~15,000 record_upstream calls. The attach now happens after the loop.
    builder.set_description(
        "Comprehensive mass/binding table over every (Z, N) in the AME "
        "enumeration — 14,972 rows spanning A = 1..418, Z = 0..118 — at the "
        "current production tier: Family A λ_A = 5/2 + (3/4)h² (PROVED) + "
        "substrate-pure flavor-split Δm/M_N (PROVED, PR #942). Binding "
        "energies via binding_canonical with use_closed_form=True for A ≤ 3 "
        "(PR #921); A = 4 uses the symbolic path. Each entry cross-references "
        "the recursive atom knot atlas methodology tag. "
        "PRECISION CAVEAT: the per-generator Wedderburn volumes come from "
        "pyhecke.atom.atom_per_generator_volumes, which uses H_3 weights at "
        "every A; for A > 1 the correct algebra is H_{3A} and the weights are "
        "systematically wrong (docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-"
        "audit.md). The proper H_{3A} sum is infeasible past A ≈ 12, so these "
        "rows are a coarse diagnostic, not a precision prediction."
    )
    builder.set_content_block("prop:recursive-atom-knot-atlas")
    builder.add_parameter("q_str", Q_50_DIGIT_STR)
    # dps is captured authoritatively in precisionMetadata.compute_dps;
    # not duplicated here (see Copilot review #1756, witness-line 23/40).

    q = mp.mpf(Q_50_DIGIT_STR)

    # Compute nucleon masses once
    nucleon = borromean_mass_prediction(q, 1, 0)
    m_p_pred = nucleon["m_p_pred_MeV"]
    m_n_pred = nucleon["m_n_pred_MeV"]

    print("=" * 120)
    print("COMPREHENSIVE MASS TABLE — QOU framework at current production tier")
    print(f"  q₀ = {Q_50_DIGIT_STR[:25]}...")
    print(f"  source: {nucleon.get('source', 'Family A')}")
    print(f"  linking_weight (Family A, PROVED) = {nucleon['linking_weight_family_a']:.10f}")
    print(f"  m_p^pred = {m_p_pred:.6f} MeV   (CODATA: {float(M_P_MEV_VALIDATION):.6f})")
    print(f"  m_n^pred = {m_n_pred:.6f} MeV   (CODATA: {float(M_N_MEV_VALIDATION):.6f})")
    print("=" * 120)
    print()
    print(f"\n{'Atom':>5s} {'Z':>2s} {'N':>2s} {'A':>2s}  "
          f"{'m_symb':>14s} {'m_qCLT':>14s} {'m_obs':>14s}  "
          f"{'B_sym':>12s} {'B_qCLT':>12s} {'B_AME':>11s}  "
          f"{'Methodology':>30s}  Caveats")
    print("-" * 150)

    rows = []
    # `mass-table-ppb.witness.json` was declared an upstream here and its body
    # bound to `mt_ppb_data`, which was then never read — two stores, zero
    # loads. Every B_pred_MeV below comes from this file's own sym / q-CLT /
    # binding_canonical paths, so the edge asserted a dependency the code does
    # not have and made drift-detection answer for a witness that cannot
    # affect a single published number. Removed rather than "wired up":
    # inventing a use for it would be the tail wagging the dog.

    for i, (name, Z, N) in enumerate(ISOTOPES):
        A = Z + N
        t0 = time.monotonic()

        nucleon = borromean_mass_prediction(q, Z, N, name)
        m_unbound_approx = nucleon.get("m_nucleus_unbound_approx_MeV")
        m_unbound_symbolic = nucleon.get("m_nucleus_unbound_symbolic_MeV")

        # Binding energies
        B_pred = 0.0
        B_qCLT = 0.0
        B_method = "n/a"
        if A >= 2:
            sym_binding = try_binding_symbolic_log_trace(Z, N)
            if sym_binding:
                B_pred = sym_binding.get("B_pred_MeV", 0.0)
                B_method = sym_binding.get("method", "?")
                
            qclt_binding = try_binding_q_clt_proxy(Z, N)
            if qclt_binding:
                B_qCLT = qclt_binding.get("B_pred_MeV", 0.0)
                if not sym_binding:
                    B_pred = B_qCLT
                    B_method = qclt_binding.get("method", "?")
        else:
            # Fallback for nucleon
            binding = try_binding_canonical(Z, N, Q_50_DIGIT_STR)
            if binding is not None:
                B_pred = binding.get("B_pred_MeV") or 0.0
                B_method = binding.get("method", "?")

        m_symbolic = (m_unbound_approx - B_pred) if (m_unbound_approx is not None and (B_pred > 0 or A == 1)) else None
        m_approx = (m_unbound_approx - B_qCLT) if (m_unbound_approx is not None and (B_qCLT > 0 or A == 1)) else None
        B_AME = AME_BINDING.get(name, 0.0)

        # CODATA/AME observed mass for comparison
        m_observed = CODATA_MASS.get(name)
        if m_observed is None and B_AME > 0:
            # Derive from AME: m = Z·m_p + N·m_n - B_AME (using CODATA nucleon masses)
            m_observed = (
                Z * M_P_MEV_VALIDATION
                + N * M_N_MEV_VALIDATION
                - mp.mpf(repr(B_AME))
            )

        # Errors against Observed
        m_err_pct_approx = ((m_approx - m_observed) / m_observed * 100) if (m_observed and m_approx is not None) else None
        m_err_pct_sym = ((m_symbolic - m_observed) / m_observed * 100) if (m_observed and m_symbolic is not None) else None
        B_err_pct = ((B_pred - B_AME) / B_AME * 100) if B_AME > 0 else None

        # Caveats
        caveats = []
        caveats.append("Family A λ_A (PROVED)")
        if Z > 0 and N > 0:
            caveats.append("flavor-split (PROVED)")
        if B_pred == 0 and A > 1:
            caveats.append(f"B computation failed: {B_method}")
        elif B_pred == 0:
            caveats.append("B NOT COMPUTED")
        if A > 4:
            caveats.append("H_{3A} kernel not available (Phase-2 gated)")

        if name in ATLAS_TAG:
            atlas_tag = ATLAS_TAG[name]
        elif B_method and "Exact symbolic" in B_method:
            atlas_tag = "principled-derivation (Q-CLT proxy)"
        elif B_method and "alpha_cluster_recursion" in B_method:
            atlas_tag = "recursive-on-⁴He"
        else:
            atlas_tag = "principled-derivation (extrapolated)"

        row = {
            "atom": name,
            "Z": Z, "N": N, "A": A,
            # Decimal strings at the declared width — see `_dp`. The truthiness
            # guards are kept EXACTLY as they were (`if m_approx`, not
            # `is not None`) so that which cells are null does not change:
            # this commit is meant to move the type and nothing else, and a
            # null/not-null flip would be indistinguishable from one in a diff
            # of 14,972 rows.
            "m_approx_MeV": _dp(m_approx) if m_approx else None,
            "m_symbolic_MeV": _dp(m_symbolic) if m_symbolic else None,
            "m_observed_MeV": _dp(m_observed) if m_observed else None,
            "m_err_pct_approx": _dp(m_err_pct_approx, 4) if m_err_pct_approx is not None else None,
            "m_err_pct_sym": _dp(m_err_pct_sym, 4) if m_err_pct_sym is not None else None,
            "B_pred_MeV": _dp(B_pred) if B_pred else None,
            "B_qCLT_MeV": _dp(B_qCLT) if B_qCLT else None,
            "B_AME_MeV": _dp(B_AME),
            "B_err_pct": _dp(B_err_pct, 4) if B_err_pct is not None else None,
            "binding_method": B_method,
            "atlas_methodology_tag": atlas_tag,
            "caveats": caveats,
        }
        rows.append(row)

        # Print row
        m_sym_s = f"{m_symbolic:14.6f}" if m_symbolic else "           n/a"
        m_app_s = f"{m_approx:14.6f}" if m_approx else "           n/a"
        m_obs_s = f"{m_observed:14.6f}" if m_observed else "           n/a"
        B_pred_s = f"{B_pred:12.6f}" if B_pred else "         n/a"
        B_qCLT_s = f"{B_qCLT:12.6f}" if B_qCLT else "         n/a"
        B_AME_s = f"{B_AME:11.6f}"

        elapsed = time.monotonic() - t0
        print(f"{name:>5s} {Z:>2d} {N:>2d} {A:>2d}  "
              f"{m_sym_s} {m_app_s} {m_obs_s}  "
              f"{B_pred_s} {B_qCLT_s} {B_AME_s}  "
              f"{atlas_tag:>30s}  "
              f"{'|'.join(caveats[:2])}"
              f"  [{elapsed:.1f}s]")

    # Summary
    print()
    n_computed = sum(1 for r in rows if r["m_approx_MeV"] is not None)
    # `r["B_pred_MeV"]` is now a decimal STRING, so `> 0` would compare a str
    # to an int and raise. Compare the value, not its serialization.
    n_binding = sum(1 for r in rows
                    if r["B_pred_MeV"] and mp.mpf(r["B_pred_MeV"]) > 0)
    n_gated = sum(1 for r in rows if any("gated" in c for c in r["caveats"]))
    print(f"Summary: {n_computed}/{len(rows)} masses computed; "
          f"{n_binding}/{len(rows)} binding energies computed; "
          f"{n_gated} gated on H_{{3A}} Phase-2.")

    builder.add_data("rows", rows)
    builder.add_data("summary", {
        "total_isotopes": len(rows),
        "masses_computed": n_computed,
        "binding_computed": n_binding,
        "gated_on_phase2": n_gated,
        # NOTE: keys below are populated only when `predict_p_n` returns
        # via the Family-A fallback path; the substrate-identity path
        # (canonical, post-2026-05-23 absorption of λ_scale into
        # VolDensity) does not emit them. Hence .get() — None here means
        # "substrate-identity path was taken", NOT "compute failure".
        # See `nucleon_path` field below for which path was used.
        "nucleon_path": nucleon.get(
            "path",
            "family_a" if "linking_weight_family_a" in nucleon else "substrate_identity",
        ),
        # These three come straight out of `borromean_mass_prediction`, which
        # now returns mpf. `fmt` is the canonical serializer and is used here
        # rather than `_dp` because these are single scalars, not 14,972-row
        # columns — the file-size argument that justifies six decimals in the
        # table does not apply to three fields, so they keep their digits.
        "linking_weight_family_a": _fmt_or_none(nucleon.get("linking_weight_family_a")),
        "vol_density_borromean_q": _fmt_or_none(nucleon.get("vol_density_borromean_q")),
        "delta_m_over_M_N": _fmt_or_none(nucleon.get("delta_m_over_M_N")),
        "m_p_pred_MeV": _fmt_or_none(m_p_pred),
        "m_n_pred_MeV": _fmt_or_none(m_n_pred),
        "production_tier": (
            "VolDensity(𝓑₃, q) via PROVED Family A linking_weight "
            "+ flavor-split (PROVED) — PR #1080 canonical framing"
        ),
        "research_tier_not_used": (
            "Strategy I linking_weight = Family A − G·h² "
            "(conjectural bijection, PURGED 2026-05-24 per PR #985)"
        ),
    })

    # The last three raw float64 fields in this witness. `add_assertion`
    # documents strings as the drained convention (`passed` coerces with
    # `float()` either way), and this particular assertion is a BOOLEAN that
    # was being projected onto a float — there was never a real number here to
    # lose, only a type. With these three gone the witness carries no raw
    # float64 at all, down from 75,112.
    builder.add_assertion(
        name="all_A_leq_4_masses_computed",
        computed="1" if all(
            r["m_approx_MeV"] is not None
            for r in rows if r["A"] <= 4
        ) else "0",
        expected="1",
        tolerance="0",
        source="All A ≤ 4 isotopes have absolute mass predictions",
    )

    builder.add_caveat(
        "Production tier uses Family A λ_A = 5/2 + (3/4)h² (PROVED, "
        "+2.89% from CODATA on m_p) + substrate-pure flavor-split "
        "(PROVED, 0.03% ratio match). Strategy I (λ_Y = λ_A − G·h², "
        "+1.33%) is NOT used in this mass table — it requires the "
        "Yekutieli bijection proof (research-grade; PR #978 / #991). "
        "Binding energies for A ≥ 5 are NOT computed — gated on H_12 "
        "Phase-2 (≥3500 test words; PR #944 delivered Phase-1 for A ≤ 4). "
        "Atlas methodology tags from prop:recursive-atom-knot-atlas."
    )

    builder.add_caveat(
        "H_3 vs H_{3A}: the per-generator Wedderburn volumes feeding the q-CLT "
        "column use H_3 weights at every A. For A > 1 the atomic braid lives in "
        "H_{3A}(q), so the weights are systematically wrong (audit "
        "2026-05-25-h3-vs-h3a-legacy-bug-audit.md). The correct sum over "
        "partitions of 3A is infeasible beyond A ≈ 12 — p(36) ≈ 18,000 and "
        "p(120) ≈ 1.8e9 — so no substitution can fix these rows; treat A > 12 "
        "as a coarse diagnostic. Measured shape: B_pred/B_AME falls to a "
        "plateau of ≈ 0.28 for A ≥ 12, i.e. the model gives ≈ 2.5 MeV per "
        "nucleon where nature gives ≈ 8."
    )

    # Attach upstream provenance AFTER the row loop — `record_upstream(...)`
    # inside `borromean_mass_prediction` only fills `_UPSTREAM_RECORDS` as rows
    # are computed, so attaching before the loop (as this did) recorded nothing.
    # `add_upstream_records` dedupes by (path, sha256), so the ~15,000 identical
    # records collapse to one edge per distinct upstream.
    builder.add_upstream_records(_UPSTREAM_RECORDS)

    out = builder.save()
    print(f"\n→ Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
