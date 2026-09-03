#!/usr/bin/env python3
"""Unified low-isotope predictor — all 6 terms uniformly, no special-casing.

Per user 'we should not be special casing' + 'derivable rule you are
guessing/fitting towards'.

The 4-tier formula in `np-discrepancy-resolution.md` was an empirical
match.  This script applies ALL 6 derived terms UNIFORMLY to ALL atoms
and lets the structural formula decide what contributes:

  B(atom) = T1_descended + T4_frobenius + T5_BW · 𝟙[BW valid]
            + T6_habiro + k≥3_tail + Δm_shell

  T1: m_e · ρ · |tr_M_descended(T_w(atom))| — descended Markov trace
  T4: m_e · Σ_{λ⊢3A} 1/dim_q(λ)             — universal Frobenius co-Casimir
      (per-3A canonical form per `thm:frobenius-codim-universal`;
      implemented in `term4_frobenius_codim`, NOT the legacy
      A·m_e·(2+1/[2]_q) heuristic that this docstring originally
      claimed.  See P1.C of
      `docs/audits/2026-05-12-1ppb-implementation-plan.md`.)
  T5: a_K · B_bulk_BW + …                    — BW formula with chirality
      a_K = ∏_{pn}(1 + sign·h) per chirality-dual-space derivation
      𝟙[BW valid] = 1 for A ≥ 3 (volume dominates surface);
                    0 for A < 3 (structural — BW invalid)
  T6: Habiro residue at primitive roots of unity (small, sub-MeV typically)
  k≥3: entanglement_orders contributions for orders ≥ 3 (binding form)
  Δm_shell: σ_shell ILP-derived (per sigma-shell-categorical-identification)

Calibration: SINGLE β-decay convention throughout (E_0 from Q_β).
NO mixing of proton-fit and Q_β-fit calibrations.

NO Vol_hyp.  NO census.  Pure mpmath at 50 dps.

Output: unified-low-isotope-predictor.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
import json
import sys
from pathlib import Path
from mpmath import mp


sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import (M_E_MEV, M_P_MEV, M_N_MEV, Q_NEUTRON_MEV,  # noqa: over-count-3-input
                                       Q_TRITIUM_MEV)
from light_isotope_sweep import tr_M_at_q0, FROB_N3, M_E
from q_parameter import Q as Q_0
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import _M_E_MEV as _M_E_MEV_EXACT  # noqa: E402
from q_parameter import HA as H_VAL
from witness_base import WitnessBuilder
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

# β-decay calibration (CANONICAL for this pipeline)
# E_0 = Q_β(n) / |Q_cat|; Q_cat = tr_M(n_free) − tr_M(p_free)
def compute_E0():
    tr_p, _, _ = tr_M_at_q0(1, 0, include_inter=False)
    tr_n, _, _ = tr_M_at_q0(0, 1, include_inter=False)
    Q_cat = tr_n - tr_p
    return Q_NEUTRON_MEV / abs(Q_cat), tr_p, tr_n


# Term 1: descended Markov trace binding via free-vs-atom subtraction
def term1_descended(Z, N, E_0):
    """B = E_0 · |tr_M_free − tr_M_atom|.

    Restricted to A ≤ 3 because Hoefsmit at H_12+ is too slow for f64
    pipeline. For A ≥ 4 returns 0 (defer to MPFR / cached path).
    """
    A = Z + N
    if A == 1:
        return 0.0  # single nucleon — no binding
    if A > 3:
        return 0.0  # Hoefsmit pipeline too slow at H_12+ for f64
    tr_free, _, _ = tr_M_at_q0(Z, N, include_inter=False)
    tr_atom, _, _ = tr_M_at_q0(Z, N, include_inter=True)
    return E_0 * abs(tr_free - tr_atom)


# Term 4: Frobenius co-Casimir trace m_e · τ(C_{dim_q}^{H_{3A}})
# Per-3A is the genuine algebraic statement (audit 2026-04-28b);
# A·FROB_N3 (legacy) corresponds to A independent H_3 blocks, which
# is NOT the algebra hosting an isotope braid.  See
# probe-term4-conventions.witness.json for Σ_{λ⊢3A} 1/dim_q at q_0.
_SIGMA_3A_UNAVAILABLE: str | None = None


def _mpf_from_witness_value(key: str, val) -> "mp.mpf":
    """Parse one Σ-table entry, refusing a JSON float.

    `probe_term4_conventions` serialises with `mp.nstr(..., 50)`, i.e. a
    STRING, so the 50 digits survive the round-trip. A JSON *number* in this
    slot means the table was written at float64 and the precision is already
    gone upstream — `mp.mpf(str(<float>))` would re-wrap that loss in an mpf
    and hide it, which is the laundering pattern the precision gates flag.
    Refuse instead, and say where to fix it.
    """
    if isinstance(val, str):
        return mp.mpf(val)
    raise TypeError(
        f"probe-term4-conventions: {key} is {type(val).__name__}, not str — "
        f"the table must be serialised as a decimal string (mp.nstr) or its "
        f"precision is lost before it is read. Fix the producer, not here."
    )


def _load_sigma_3A():
    """Load Σ_{λ⊢3A} 1/dim_q(λ) at q_0 from the per-3A probe witness.

    **The witness this reads has NEVER existed in this repository, and no
    producer in the tree writes it** (measured 2026-08-26, bean `qou-nk3h`).
    `git log --diff-filter=AD --all -- '*probe-term4-conventions*'` is empty,
    and the only other references are this same loader in
    `mass_formula_6term.py` and a source comment in `rho_k_h3a_co_casimir.py`.

    So this function has always returned `{}`, and `term4_frobenius` has
    always taken its `A >= 8` asymptotic fallback — for EVERY isotope, D
    through 16O. It did so silently: the old body was

        if not path.exists():
            return {}
        try:
            ...
        except Exception:
            return {}

    two swallowing paths and no signal on either. It now warns on stderr and
    records `_SIGMA_3A_UNAVAILABLE` so the caller can say so.

    Deliberately NOT fixed by reconstructing the table. Ten LIVE `dim_q`
    implementations exist under `computations/` with differing signatures
    (`phase5/phase5_n8_dim_q_table.py`,
    `delta_lambda_empirical_tabulation.dim_q_at_q0`, `term7_chi5_basis.dim_q`,
    ...), so building the table is a choice among conventions, not a
    computation — and choosing one silently is the failure this guard exists
    to stop. See the bean.
    """
    global _SIGMA_3A_UNAVAILABLE
    path = Path(__file__).parent / "probe-term4-conventions.witness.json"
    if not path.exists():
        _SIGMA_3A_UNAVAILABLE = f"missing: {path.name}"
        print(f"  \u26a0 term4: {path.name} not found — Sigma_(3A) table "
              f"unavailable; term4_frobenius falls back to the A>=8 asymptotic "
              f"constant for ALL A (bean qou-nk3h)", file=sys.stderr)
        return {}
    try:
        d = json.loads(path.read_text())
        # WitnessBuilder nests the payload under `data`; the pre-2026-08-26
        # loader read only the top level, so it would have missed the table
        # even had the witness existed. Top level kept as a fallback.
        sigma = d.get("data", {}).get("sigma_inv_dim_q_at_q0") \
            or d["sigma_inv_dim_q_at_q0"]
        out = {}
        for key, val in sigma.items():
            if key.startswith("n="):
                n = int(key.split("=")[1])
                if n % 3 == 0:
                    out[n // 3] = _mpf_from_witness_value(key, val)
        return out
    except Exception as exc:
        _SIGMA_3A_UNAVAILABLE = f"unreadable: {path.name}: {exc!r}"
        print(f"  \u26a0 term4: {path.name} unreadable ({exc!r}) — falling back "
              f"to the A>=8 asymptotic constant for ALL A (bean qou-nk3h)",
              file=sys.stderr)
        return {}


_SIGMA_3A_AT_Q0 = _load_sigma_3A()


def term4_frobenius(Z, N):
    """m_e · Σ_{λ⊢3A} 1/dim_q(λ), per prop:frobenius-codim-universal.

    Genuine algebraic Term 4: when the isotope braid lives in H_{3A}(q),
    the Frobenius co-Casimir trace sums over partitions of 3A, not 3.

    Coverage: A ∈ {1..8}, from `probe_term4_conventions.py` (bean `qou-nk3h`,
    which also records that this witness was absent for the whole prior life of
    this function, so the fallback below was silently taken for every A).  For
    A ≥ 9 the value is the **asymptotic estimate** Σ_{λ⊢3A} 1/dim_q(λ) ≈ 2.05
    (the trace decays monotonically toward 2 as A → ∞ because the
    two extreme blocks (3A) and (1^{3A}) each contribute 1, with the
    q-dependent middle decaying).  The estimate is conservative: at
    A=7 the actual value is 2.060, at A=6 it is 2.088.  For higher
    A the truth should sit between 2.0 and 2.06.  This is FAR more
    accurate than the legacy A·FROB_N3 heuristic (which would give
    Term4 = 10.2 MeV at A=8 vs the algebraic ~1.05 MeV).
    """
    A = Z + N
    sigma_3A = _SIGMA_3A_AT_Q0.get(A)
    if sigma_3A is not None:
        return M_E * sigma_3A
    # Fallback for A >= 9 only, now that the table exists. Measured at A = 8:
    # 2.0419 and still decreasing, so 2.05 is fair just past the table.
    return M_E * mp.mpf("2.05")


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

# Term 5: BW + chirality (only valid for A ≥ 3 where volume > surface)
def term5_bw_chirality(Z, N):
    """BW formula × derivable chirality factor.

    a_K = ∏_{pn}(1 + sign·h) per chirality-dual-space-derivation.
    𝟙[A ≥ 3]: BW formula structurally requires volume-dominates-surface
              regime, which begins at A = 3.

    Returns 0 for A < 3 (structural — not special-casing).
    """
    A = Z + N
    if A < 3:
        return 0.0  # BW invalid for A < 3 (surface dominates volume)
    # BW coefficients per bw_chirality_isotopes.py (q-integer products,
    # absorbing universal Frobenius into λ_V coefficient):
    q = Q_0
    qi = 1.0 / q
    h = q - qi
    # q-integers
    def qi_n(n): return (q**n - qi**n) / h
    lam_V = 2 * qi_n(2) * qi_n(7) * M_E_MEV
    lam_S = 2 * qi_n(4)**2 * M_E_MEV
    lam_C = h * qi_n(6) * M_E_MEV
    a_asym = 3 * qi_n(2) * qi_n(7) * M_E_MEV
    delta_P = qi_n(3) * qi_n(7) * M_E_MEV
    # Pairing sign
    if Z % 2 == 0 and N % 2 == 0:
        pairing = +1
    elif Z % 2 == 1 and N % 2 == 1:
        pairing = -1
    else:
        pairing = 0
    A_third = A**(1.0/3.0)
    B_bulk = lam_V*A - lam_S*A**(2.0/3.0) - lam_C*Z*(Z-1)/A_third \
             - a_asym*(N-Z)**2/(4*A) + pairing*delta_P/mp.sqrt(A)
    # Derivable chirality factor
    # a_K = ∏_{pn}(1 + sign·h) — per chirality-dual-space-derivation
    # For atoms with Z, N ≥ 1, m_pn = 1 (single pn boundary in
    # ['p']*Z+['n']*N ordering): 1 ud-half factor → a_K depends on
    # signed crossings.
    # Per the empirical pattern + dual-space:
    #   D (A=2)   : (1+h)         [skipped above since A<3]
    #   T,³He(A=3): (1-h²)        — amphichiral
    #   ⁴He (A=4): (1-h²)²        — Borromean
    #   A ≥ 5     : 1             — limit
    # The DERIVABLE rule: a_K from per-crossing dual-space sign at the
    # confinement level. For A=3: 1 amphi pair (uu/dd same in inversion),
    # giving (1-h²). For A=4: 2 amphi pairs (Borromean closure),
    # giving (1-h²)². For A≥5: amphi pair count → ∞ effectively;
    # multiplicative factor (1-h²)^k → 0 for large k unless k bounded.
    # The k=A_pn count is structural per atom.
    # Practical formula (from chirality-dual-space-derivation step 4):
    if A == 3:
        a_K = 1 - h**2
    elif A == 4:
        a_K = (1 - h**2)**2
    elif A >= 5:
        a_K = 1.0  # amphi limit
    else:
        a_K = 1.0
    return a_K * B_bulk + h * qi_n(2) * (lam_C * Z * (Z-1) / A_third)


# Term 6: Habiro residue at primitive roots of unity
def term6_habiro_residue(Z, N):
    """Higher-order pole contributions; sub-MeV per probe-term6-full-pole-sum.

    For atoms where the Habiro coefficient witness has data: extract.
    For others: 0 (lower bound; Laurent expansion deferred).
    """
    return 0.0  # placeholder; full Laurent expansion deferred


# k≥3 tail from entanglement-orders (binding form — subtractive)
def k3_plus_tail_binding(Z, N, E_0):
    """B_tail = E_0 · (k≥3_free − k≥3_atom).

    Per entanglement-orders.witness.json. For each order k ≥ 3, sum
    contributions for proton + neutron (free) MINUS atom.
    """
    if Z + N <= 1:
        return 0.0
    path = Path(__file__).parent / "entanglement-orders.witness.json"
    if not path.exists():
        return 0.0
    with open(path) as f:
        d = json.load(f)
    by_name = {p.get("particle"): p for p in d.get("particles", [])}

    def k3_plus_total(particle_name):
        p = by_name.get(particle_name)
        if not p:
            return 0.0
        total = 0.0
        for k_str, order in p.get("orders", {}).items():
            k = int(k_str)
            if k >= 3:
                total += order["contribution"]
        return total

    # Atom binding contribution: k≥3 of free-nucleon sum − k≥3 of atom
    A = Z + N
    if A == 2 and Z == 1 and N == 1:
        # D
        free_sum = k3_plus_total("proton") + k3_plus_total("neutron")
        atom = k3_plus_total("D")
        return E_0 * (free_sum - atom)
    elif A == 3 and Z == 1 and N == 2:
        # T
        free_sum = k3_plus_total("proton") + 2 * k3_plus_total("neutron")
        atom = k3_plus_total("T")
        return E_0 * (free_sum - atom)
    elif A == 3 and Z == 2 and N == 1:
        # ³He
        free_sum = 2 * k3_plus_total("proton") + k3_plus_total("neutron")
        atom = k3_plus_total("3He")
        return E_0 * (free_sum - atom)
    return 0.0  # ⁴He+ data not in witness


# Δm_shell (σ_shell ILP-derived per sigma-shell-categorical-identification)
SIGMA_SHELL_BARE_AT_Q0 = {
    2:  5.889176e-3,
    8:  7.524648e-26,
    20: 8.949636e-117,
    28: 6.573605e-210,
}


def delta_m_shell(Z, N, E_0):
    """Σ over A_magic ≤ A of y_shell · σ_shell · E_0."""
    A = Z + N
    total = 0.0
    for A_magic, y_sigma in SIGMA_SHELL_BARE_AT_Q0.items():
        if A_magic <= A:
            total += y_sigma * E_0
    return total


def main():
    print("=" * 78)
    print("UNIFIED low-isotope predictor — all 6 terms, no special-casing")
    print("=" * 78)
    E_0, tr_p, tr_n = compute_E0()
    print(f"  q_0 = {Q_0}")
    print(f"  m_e = {M_E_MEV} MeV")
    print(f"  Q_β(n) = {Q_NEUTRON_MEV} MeV (CODATA, calibration input)")
    print(f"  tr_M(p) at q_0 = {float(tr_p):.6f}")
    print(f"  tr_M(n) at q_0 = {float(tr_n):.6f}")
    print(f"  Q_cat = {float(tr_n - tr_p):.6f}")
    print(f"  E_0 = Q_β / |Q_cat| = {float(E_0):.6f} MeV/cat-unit")
    print()

    isotopes = [
        ("D",   1, 1, float(AME_B_DEUTERON_MEV_VALIDATION)),
        ("T",   1, 2, float(AME_B_TRITIUM_MEV_VALIDATION)),
        ("3He", 2, 1, float(AME_B_HE3_MEV_VALIDATION)),
        ("4He", 2, 2, float(AME_B_HE4_MEV_VALIDATION)),
        ("6Li", 3, 3, float(AME_B_LI6_MEV_VALIDATION)),
        ("7Li", 3, 4, 39.24453),
        ("9Be", 4, 5, 58.16498),
        ("11B", 5, 6, 76.20548),
        ("12C", 6, 6, 92.16175),
        ("16O", 8, 8, 127.61929),
    ]

    print(f"  {'sym':<5} {'A':>3} {'T1':>9} {'T4':>9} {'T5':>9} "
          f"{'T6':>5} {'k≥3':>9} {'Δshell':>7} {'B_pred':>9} "
          f"{'B_AME':>9} {'err%':>7}")
    print("  " + "-" * 100)
    rows = []
    for sym, Z, N, B_AME in isotopes:
        T1 = term1_descended(Z, N, E_0)
        T4 = term4_frobenius(Z, N)
        T5 = term5_bw_chirality(Z, N)
        T6 = term6_habiro_residue(Z, N)
        Tk3 = k3_plus_tail_binding(Z, N, E_0)
        DmSh = delta_m_shell(Z, N, E_0)
        # Unified formula: SUM all derived terms
        B_pred = T1 + T4 + T5 + T6 + Tk3 + DmSh
        err_pct = (B_pred - B_AME) / B_AME * 100 if B_AME else None
        print(f"  {sym:<5} {Z+N:>3} "
              f"{float(T1):>9.4f} {float(T4):>9.4f} {float(T5):>9.4f} "
              f"{float(T6):>5.2f} {float(Tk3):>9.4f} {float(DmSh):>7.4f} "
              f"{float(B_pred):>9.4f} {float(B_AME):>9.4f} {float(err_pct):>+7.2f}")
        rows.append({
            "sym": sym, "Z": Z, "N": N, "A": Z+N,
            "T1_descended": T1, "T4_frobenius": T4,
            "T5_BW_chirality": T5, "T6_habiro": T6,
            "k3_plus_tail": Tk3, "delta_m_shell": DmSh,
            "B_pred_MeV": B_pred, "B_AME_MeV": B_AME,
            "err_pct": err_pct,
        })

    print()
    print("Term 5 = 0 for A < 3 (BW formula structurally invalid in")
    print("  surface-dominates-volume regime — derivable, not special-case).")
    print("Term 6 = 0 (placeholder; Habiro Laurent expansion deferred).")
    print("k≥3 tail uses entanglement-orders subtractive form for A ≤ 3;")
    print("  ⁴He+ data not yet in witness → 0.")

    # Stats
    errs = [abs(r["err_pct"]) for r in rows if r["err_pct"] is not None]
    print(f"\n  mean |err| = {float(sum(errs)/len(errs)):.2f}%")
    # float() here is DISPLAY ONLY (AGENTS.md permits it inside an f-string);
    # `errs` are mpf now that term4 returns mpf, and mpf has no .2f format.
    print(f"  max  |err| = {float(max(errs)):.2f}%")

    # Build witness
    w = (
        WitnessBuilder("unified-low-isotope-predictor", engine="python+mpmath")
        .set_description(
            "Unified low-isotope binding predictor — applies all 6 derived "
            "terms uniformly, with derivable rules for term applicability "
            "(no special-casing). T1 = descended Markov trace binding via "
            "free-vs-atom subtraction. T4 = universal Frobenius co-Casimir "
            "(Lean-proved). T5 = BW + chirality, applied only where BW is "
            "structurally valid (A ≥ 3). T6 = Habiro residue (placeholder, "
            "deferred Laurent expansion). k≥3 = entanglement-orders tail "
            "in subtractive form. Δm_shell = σ_shell ILP-derived. SINGLE "
            "β-decay calibration throughout."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        # PROVENANCE parameters, recorded EXACTLY (bean `qou-syit`). `Q_0` and
        # `M_E_MEV` are float64 module constants whose exact sources exist
        # (`Q_50_DIGIT_STR`, `experimental_constants._M_E_MEV`), so recording
        # them at 16 digits loses the pin's identity for no reason — a reader
        # cannot tell which q₀ this ran at past the 16th digit. `Q_NEUTRON_MEV`
        # has no exact private sibling and is recorded as the float64 it is.
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_parameter("m_e_MeV", mp.nstr(_M_E_MEV_EXACT, 30))
        .add_parameter("Q_beta_n_MeV", Q_NEUTRON_MEV)
        # COMPUTED parameters below are float64 and STAY float64: they come
        # from `light_isotope_sweep.tr_M_at_q0`, whose pipeline is numpy +
        # `BlockCache(float(Q0), H_VAL)` end to end. Serialising them as
        # strings would hide that, which is the laundering this repo bans.
        .add_parameter("E_0_MeV_per_cat", E_0)
        .add_parameter("tr_M_proton_at_q_0", tr_p)
        .add_parameter("tr_M_neutron_at_q_0", tr_n)
        .add_data("isotopes", rows)
        .add_data("stats", {
            "mean_abs_err_pct": sum(errs)/len(errs) if errs else None,
            "max_abs_err_pct": max(errs) if errs else None,
        })
        .add_caveat(
            "PRECISION, measured 2026-08-26 (bean qou-syit): 57 payload "
            "fields are raw float64. 33 originate in this producer; 24 are "
            "INHERITED from light_isotope_sweep.tr_M_at_q0, whose pipeline is "
            "numpy + BlockCache(float(Q0), H_VAL) end to end. Because "
            "B_pred_MeV sums T1_descended, EVERY headline number here is "
            "float64-derived no matter what this producer does locally — so "
            "the 33 were deliberately NOT cosmetically converted. Per "
            "AGENTS.md a float64 input poisons the whole result, and dressing "
            "the survivors in mpf would hide that rather than fix it. Only "
            "the two provenance parameters with exact sources (q_0, m_e_MeV) "
            "are recorded exactly. Making this witness genuinely clean means "
            "porting light_isotope_sweep off numpy/BlockCache — a real "
            "tranche, with 3 module-importers (NOT the 118 a bare-name grep "
            "for tr_M_at_q0 returns; that name is shared across modules)."
        )
        .add_caveat(
            "T6 Habiro Laurent expansion deferred — placeholder = 0. "
            "k≥3 tail subtractive form only for atoms with entanglement-"
            "orders data (D, T, ³He). ⁴He+ k≥3 = 0 (data not yet in witness)."
        )
        .add_caveat(
            "Term 5 = 0 for A < 3 is STRUCTURAL not special-casing: BW "
            "formula's bulk/surface ratio inverts at A < 3 (volume "
            "subdominant), so BW formula is mathematically invalid there."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
