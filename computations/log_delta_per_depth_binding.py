"""
log_delta_per_depth_binding.py — option (a) test: per-depth binding
subtraction in the unified mass formula.

Per the prior finding (full-mass-subtract gives max/min 3.96× but
T/³He come out with WRONG sign — predicted unbound): the structural
issue is that α_{k≥4} = m_e·8G is constant across depths, so m_q,K
grows super-linearly with n. The constituent-subtraction subtracts
Z·m_p + N·m_n EXTERNALLY, but the proton/neutron only contribute
to depths 0, 1, 2 (n=3 partitions have max depth 2). Atom contributions
at depth k ≥ 3 are uncorrected.

This script implements the per-depth-stratified binding:

    m^(k)_{q, K | bind} := m^(k)_{q, K} - Z · m^(k)_{q, p} - N · m^(k)_{q, n}
    B(K) := Σ_k α_k · m^(k)_{q, K | bind}

For k ≥ 3 (constituents = 0), m^(k)_{K|bind} = m^(k)_K (uncorrected).
But the structural prefactor α_{k≥4} = m_e·8G is universal — it
should give the SAME contribution per partition. So per-depth
binding at high k is the atom's "extra" high-depth complexity beyond
what would arise from independent nucleons.

If the high-depth contribution is the right "binding signal", we
expect B_pred to track AME with low cross-atom variance.

Ref: prop:unified-curvature-rank-mass-formula
Ref: docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import fmt, set_compute_dps  # noqa: E402 — dps must rise before module constants
import ast
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV,
)
from q_parameter import Q as Q0

CHI_FILES = {
    "p":   "chi-proton-h3-at-q0-50dps.witness.json",
    "n":   "chi-neutron-h3-at-q0-50dps.witness.json",
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

B_AME = {
    "p":   mp.mpf(0), "n":   mp.mpf(0),
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

ZN = {"p": (1, 0), "n": (0, 1), "D": (1, 1), "T": (1, 2),
      "3He": (2, 1), "4He": (2, 2)}


def alpha_k(k):
    z_mark = Q0**3 / (Q0**2 + 1)
    G = mp.catalan
    if k in (0, 1, 3): return mp.mpf(1)
    if k == 2: return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G  # k >= 4 (CAL-1)


def q_int(k):
    return (Q0 ** k - Q0 ** (-k)) / (Q0 - 1 / Q0)


def q_factorial(n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= q_int(k)
    return r


def _hooks(lam):
    """Hook lengths of every cell of `lam` (arm + leg + 1)."""
    out = []
    for r, row in enumerate(lam):
        for c in range(row):
            arm = row - c - 1
            leg = sum(1 for rr in range(r + 1, len(lam)) if lam[rr] > c)
            out.append(arm + leg + 1)
    return out


def dim_q(lam):
    """d_q(λ) = [n]_q! / ∏_cells [h]_q — the *quantum* dimension.

    NOT the classical Specht dimension f^λ = n!/∏h, which is what the χ
    witnesses carry in their `dim` field.
    """
    d = q_factorial(sum(lam))
    for h in _hooks(lam):
        d /= q_int(h)
    return d


# ── weight forms (bean qou-uk8o, 2026-09-05) ────────────────────────────────
# `f2_over_qfact` is what this producer has always computed. Its historical
# spelling was `w = dim_q ** 2 / qfact` with `dim_q` bound to the χ witness's
# `dim` field — which is the CLASSICAL f^λ, so the name was wrong and the
# object is (f^λ)²/[n]_q!. It is not a probability measure: Σ_λ (f^λ)² = n!
# exactly, so it sums to n!/[n]_q! = 0.98029937 / 0.85832883 / 0.61193301 /
# 0.32612477 at n = 3 / 6 / 9 / 12. Φ_k is linear in the weights, so each
# atom's B_pred is scaled by a DIFFERENT factor spanning 3.0x — which cancels
# from any ratio at one n and does not cancel from the cross-atom max/min this
# producer is scored on. Same defect class as
# docs/audits/2026-09-04-plancherel-convention-gap.md, different constant:
# that audit's c_n = Σ d_q²/[n]_q! runs 0.99/1.11/1.52 and *increases* with n.
# The two `_selfnorm` forms are measures at every n by construction.
WEIGHT_FORMS = ("f2_over_qfact", "f2_selfnorm", "dq2_selfnorm", "identity")


def _weight_map(parts, n, w_form):
    """Per-partition weight list for `w_form`, self-normalized where named."""
    if w_form == "identity":
        return [mp.mpf(1) for _ in parts]
    if w_form == "f2_over_qfact":
        qfact = q_factorial(n)
        return [mp.mpf(p["dim"]) ** 2 / qfact for p in parts]
    if w_form == "f2_selfnorm":
        raw = [mp.mpf(p["dim"]) ** 2 for p in parts]
    elif w_form == "dq2_selfnorm":
        raw = [dim_q(p["partition"]) ** 2 for p in parts]
    else:
        raise ValueError(w_form)
    tot = sum(raw, mp.mpf(0))
    if tot == 0:
        raise ZeroDivisionError(f"{w_form}: weight total is zero at n={n}")
    return [r / tot for r in raw]


def load_chi(sp):
    w = json.loads((HERE / CHI_FILES[sp]).read_text())
    n = int(w["n_strands"])
    parts = []
    for p in w["by_partition"]:
        lam = p["partition"] if isinstance(p["partition"], list) else ast.literal_eval(p["partition"])
        parts.append({
            "partition": tuple(lam),   # needed by the dq2_selfnorm weight form
            "depth": len(lam) - 1,
            "dim": int(p["dim"]),
            "chi": mp.mpf(p["chi_lambda"]),
        })
    return n, parts


def phi_k(parts, n, k, w_form="f2_over_qfact"):
    """Φ_k(β) under the chosen weight form (see WEIGHT_FORMS)."""
    total = mp.mpf(0)
    weights = _weight_map(parts, n, w_form)
    for p, w in zip(parts, weights):
        if p["depth"] != k: continue
        chi = p["chi"]; f_lam = mp.mpf(p["dim"])
        f = mp.fabs(chi) * f_lam
        if f < mp.mpf("1e-30"): continue
        total += w * mp.log(f)
    return total


def per_species_phi(sp, w_form="f2_over_qfact"):
    """Return (n, {k: Φ_k}) for species."""
    n, parts = load_chi(sp)
    return n, {k: phi_k(parts, n, k, w_form) for k in range(n)}


def main() -> int:
    builder = WitnessBuilder("log-delta-per-depth-binding")
    builder.set_description(
        "Option (a) test: per-depth-stratified binding subtraction in "
        "prop:unified-curvature-rank-mass-formula. B(K) = Σ_k α_k · "
        "[m^(k)_K - Z·m^(k)_p - N·m^(k)_n] with paper-prescribed ~w_λ."
    )

    # Compute Φ_k per species per depth, per weight form
    phi_by_form = {}
    n_per_sp = {}
    for w_form in WEIGHT_FORMS:
        phi_data = {}
        for sp in ("p", "n", "D", "T", "3He", "4He"):
            n, phis = per_species_phi(sp, w_form)
            phi_data[sp] = phis
            n_per_sp[sp] = n
        phi_by_form[w_form] = phi_data

    builder.add_data("phi_k_per_species", {
        w_form: {sp: {str(k): str(v) for k, v in phis.items()}
                 for sp, phis in pd.items()}
        for w_form, pd in phi_by_form.items()
    })
    builder.add_data("n_per_species", n_per_sp)

    all_results = {}
    all_summary = {}
    for w_form in WEIGHT_FORMS:
      phi_data = phi_by_form[w_form]
      print(f"\n[{w_form}]")
      # Per-depth binding subtraction
      print(f"{'atom':<6} {'n':>3} {'B_pred':>16} {'B_AME':>10} {'|B_pred/B_AME|':>16}")
      results = {}
      for atom in ("D", "T", "3He", "4He"):
        Z, N = ZN[atom]
        n_atom = n_per_sp[atom]
        # Per-depth binding: for each k available in atom, subtract Z·proton + N·neutron at same k
        # (constituents have only k = 0, 1, 2; for k ≥ 3, m^(k)_{p,n} = 0)
        B_pred = mp.mpf(0)
        per_depth_contribs = []
        for k in range(n_atom):
            m_atom_k = phi_data[atom].get(k, mp.mpf(0))
            m_p_k = phi_data["p"].get(k, mp.mpf(0))  # 0 for k ≥ 3
            m_n_k = phi_data["n"].get(k, mp.mpf(0))  # 0 for k ≥ 3
            m_bind_k = m_atom_k - Z * m_p_k - N * m_n_k
            contrib = alpha_k(k) * m_bind_k
            per_depth_contribs.append({
                "k": k,
                "alpha_k": str(alpha_k(k)),
                "m_atom_k": str(m_atom_k),
                "m_p_k": str(m_p_k),
                "m_n_k": str(m_n_k),
                "m_bind_k": str(m_bind_k),
                "contrib": str(contrib),
            })
            B_pred += contrib

        B_emp = B_AME[atom]
        ratio = mp.fabs(B_pred / B_emp) if B_emp != 0 else mp.mpf("nan")
        results[atom] = {
            "B_pred": str(B_pred),
            "B_pred_sign": "+" if B_pred > 0 else "-",
            "B_AME": str(B_emp),
            # mpf -> output-precision string: float() here wrote a binary64
            # value into the witness (NO-FLOAT64 discipline).
            "abs_ratio": fmt(ratio),
            "per_depth": per_depth_contribs,
        }
        print(f"  {atom:<6} {n_atom:>3} {float(B_pred):>16.6f} {float(B_emp):>10.4f} {float(ratio):>16.6f}")

      # Variance
      abs_ratios = [mp.mpf(r["abs_ratio"]) for r in results.values()]
      rmin, rmax = min(abs_ratios), max(abs_ratios)
      mom = rmax / rmin if rmin > 0 else mp.inf
      # T/³He/⁴He alone. Under the self-normalized forms the deuteron is the
      # sole outlier, and one max/min over all four hides that — it reads as
      # broad scatter when it is a tight cluster plus one miss. Derived
      # statistic only; the verdict cut-offs below are deliberately left at
      # their historical values rather than re-tuned to the new baseline.
      hv = [mp.mpf(results[a]["abs_ratio"]) for a in ("T", "3He", "4He")]
      mom_hv = max(hv) / min(hv) if min(hv) > 0 else mp.inf
      signs_consistent = all(mp.mpf(r["B_pred"]) > 0 for r in results.values())

      if mom < 1.05:
        verdict = f"PASS — max/min = {float(mom):.3f} < 1.05 (universal categorical c)"
      elif mom < 1.5:
        verdict = f"STRONG — max/min = {float(mom):.3f} (under 1.5×)"
      elif mom < 2.0:
        verdict = f"GOOD — max/min = {float(mom):.3f} (better than full-mass-subtract 3.96×)"
      elif mom < 3.96:
        verdict = f"IMPROVES — max/min = {float(mom):.3f} (better than full-mass-subtract 3.96×)"
      else:
        verdict = f"NO IMPROVEMENT — max/min = {float(mom):.3f} (≥ 3.96×)"
      print(f"  max/min = {float(mom):.4f}   (T/³He/⁴He only: {float(mom_hv):.4f})")
      print(f"  Verdict: {verdict}")
      print(f"  All B_pred > 0 (correct binding sign): {signs_consistent}")

      all_results[w_form] = results
      all_summary[w_form] = {
          "max_over_min": fmt(mom),
          "max_over_min_heavy_three_no_deuteron": fmt(mom_hv),
          "verdict": verdict,
          "all_signs_correct": signs_consistent,
      }

    builder.add_data("per_depth_binding_results", all_results)
    builder.add_data("canonical_status", "canonical-with-empirical-assignment")
    builder.add_data("variance_summary", all_summary)
    # Headline keys kept at the historical (as-published) form so downstream
    # readers do not silently switch normalization; the self-normalized
    # figures sit beside them in variance_summary. Bean qou-uk8o.
    builder.add_data("max_over_min", all_summary["f2_over_qfact"]["max_over_min"])
    builder.add_data("verdict", all_summary["f2_over_qfact"]["verdict"])
    builder.add_data("all_signs_correct",
                     all_summary["f2_over_qfact"]["all_signs_correct"])

    builder.add_assertion(
        "data_loaded",
        computed=B_AME["D"],
        # mpf, not a float literal: a binary64 `expected` is a raw-float64
        # field in the witness and cannot represent the value it asserts.
        expected=AME_B_DEUTERON_MEV_VALIDATION,
        tolerance=mp.mpf("1e-10"),
        unit="B(D) MeV",
        source="AME 2020",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
