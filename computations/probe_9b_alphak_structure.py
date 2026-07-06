#!/usr/bin/env python3
"""
probe_9b_alphak_structure.py — PROBE 2 (bean nf8d): two derive-or-refute
structure checks on the step-9b depth-stratified α_k assignment rule
(the unclosed gap per docs/audits/2026-06-09-binding-canonical-default-
depth-stratified.md: α_0 = α_1 = α_3 = 1, α_2 = z² ≈ 0.2493,
α_{k≥4} = m_e·8G ≈ 3.7445 — constants structural, ASSIGNMENT empirical).

(2a) α_3 centrality check — a character computation, not a fit.
    The depth-3 GB layer of H_3(q) is spanned by T_Δ, Δ = σ1σ2σ1 the
    Garside element (Δ is NOT central in H_3 — conjugation by Δ swaps
    σ1 ↔ σ2; Δ² IS the central full twist).  We test whether the
    natural Markov-marker series α_k = z^k degenerates at k = 3
    because of this (near-)centrality:

      • per-element Markov weight by depth (EXACT, symbolic + 50 dps):
          tr_M(T_w) = z^{ℓ(w)} for ℓ(w) = 0, 1, 2   (depths 0-2)
          tr_M(T_Δ) = z + h·z² = z·(1 + q^{1/2} − q^{-1/2})  ≠ z³
      • the mechanism (DERIVED): χ^{(2,1)}(T_Δ) = 0 exactly.
        ρ_{(2,1)}(Δ)² is the central full-twist scalar c·I and
        det ρ_{(2,1)}(Δ) = −1 < 0, so the two eigenvalues are ±√c
        ⇒ ρ_{(2,1)}(Δ) is TRACELESS.  The standard block drops out of
        the Markov trace at depth 3 and the weight collapses onto the
        two outer 1-dim blocks (q³, −q⁻³), which are cycle-type
        weight-z¹ objects (Δ has cycle type (2,1) — conjugate to the
        depth-1 transposition s1).  The BREAK in the z^k series at
        k = 3 is therefore structural, driven by centrality of Δ².
      • the VALUE α_3 = 1 is NOT derived: the collapsed weight
        relative to depth-1 is tr_M(T_Δ)/tr_M(T_1) = 1 + q^{1/2} −
        q^{-1/2} ≈ 1.1044 at q₀ (→ 1 exactly as q → 1) — a
        NEAR-MATCH to the assigned α_3/α_1 = 1 at the 10.4 % level.

(2b) α_{k≥4} plateau resummation — one evaluation per atom.
    Tests whether m_e·8G (8G = Vol(L6a4), the ⁴He magic-A plateau)
    equals the geometric resummation Σ_{k≥4} z^k·N_k at q₀, with N_k
    the per-depth element count of the GB filtration J^k/J^{k+1} of
    the relevant H_{3A}.  Four readings of N_k are evaluated (the
    depth-stratified compute's own layer data is the partition-depth
    stratification; the GB/Coxeter length grading is the audit doc's
    6-element H_3 multiplicative-closure reading):
      cox    — #{w ∈ S_{3A} : ℓ(w) = k}  (coefficients of [3A]_t!)
      parts  — #{λ ⊢ 3A : depth(λ) = k},  depth(λ) = len(λ) − 1
      dim    — Σ_{depth(λ)=k} d_λ        (classical block dims)
      dimsq  — Σ_{depth(λ)=k} d_λ²       (layer element count)
    Verdict per (atom, reading): IDENTITY (rel dev ≤ 1e-10),
    NEAR-MATCH (state %), or REFUTED-scope-(a).  A universal plateau
    also requires the resummation to be ATOM-INDEPENDENT; the
    cross-atom spread is recorded as a structural check.

No new fit constants.  Audit-only.  50 dps per computations/_precision.py.

Ref: docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md
Ref: docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md
Ref: prop:plancherel-term-7-formulation
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _li_2_q_util import load_q_50dps  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    y_lambda_wenzl_bridge_numeric,
    chi_lambda_mpmath,
    classical_dim,
    partitions_of,
)

TOL = mp.mpf("1e-40")  # 50-dps identity tolerance (≫ 1e-25 floor)


# ────────────────────────────────────────────────────────────────────
# (2a) symbolic layer — H_3 seminormal, exact in q
# ────────────────────────────────────────────────────────────────────

def symbolic_2a() -> dict:
    """Exact-in-q verification of every 2a identity via sympy.

    Seminormal H_3 matrices for λ = (2,1) (Hoefsmit; convention
    σ² = h·σ + 1, h = q − q⁻¹, eigenvalues q and −q⁻¹):
        ρ(T1) = diag(q, −q⁻¹)
        ρ(T2) = [[a, b], [b, a']],  a = h/(1−q⁴), a' = h/(1−q⁻⁴),
                b = √(a·a' + 1)
    y_λ solved exactly from the Markov data at depths ≤ 2
    (tr(1) = 1, tr(T1) = z, tr(T1T2) = z²) — the depth-3 value is
    then FORCED, which is the point of the check.
    """
    q = sp.Symbol("q", positive=True)
    h = q - 1 / q
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))

    a = h / (1 - q**4)
    ap = h / (1 - q**-4)
    b = sp.sqrt(a * ap + 1)
    T1 = sp.Matrix([[q, 0], [0, -1 / q]])
    T2 = sp.Matrix([[a, b], [b, ap]])

    # sanity: braid relation on the standard block
    braid_ok = sp.simplify((T1 * T2 * T1 - T2 * T1 * T2)).is_zero_matrix

    words = {
        "e": [],
        "T1": [T1],
        "T2": [T2],
        "T12": [T1, T2],
        "T21": [T2, T1],
        "T121": [T1, T2, T1],
    }
    depth = {"e": 0, "T1": 1, "T2": 1, "T12": 2, "T21": 2, "T121": 3}

    def chi21(mats):
        M = sp.eye(2)
        for m in mats:
            M = M * m
        return sp.trace(M), M

    chi = {}
    mats = {}
    for name, ms in words.items():
        c, M = chi21(ms)
        chi[name] = sp.simplify(c)
        mats[name] = M

    # χ for the 1-dim blocks: (3) → q^ℓ, (1³) → (−q⁻¹)^ℓ
    chi3 = {n: q ** depth[n] for n in words}
    chi111 = {n: (-1 / q) ** depth[n] for n in words}

    # Solve y exactly from the depth ≤ 2 Markov data
    y3, y21, y111 = sp.symbols("y3 y21 y111")
    eqs = [
        sp.Eq(y3 * 1 + y21 * 2 + y111 * 1, 1),          # M3: tr(1) = 1
        sp.Eq(y3 * q + y21 * chi["T1"] + y111 * (-1 / q), z),   # tr(T1) = z
        sp.Eq(y3 * q**2 + y21 * chi["T12"] + y111 * q**-2, z**2),  # tr(T12) = z²
    ]
    sol = sp.solve(eqs, [y3, y21, y111], dict=True)[0]

    def trM(name):
        return (sol[y3] * chi3[name] + sol[y21] * chi[name]
                + sol[y111] * chi111[name])

    # The forced depth-3 value and the claimed closed form
    forced = sp.simplify(trM("T121"))
    claimed = z + h * z**2
    identity_ok = sp.simplify(forced - claimed).equals(0)

    # χ^{(2,1)}(Δ) = 0 exactly
    chi21_delta_zero = chi["T121"].equals(0)

    # centrality data on the standard block
    M = sp.simplify(mats["T121"])
    det_delta = sp.simplify(M.det())            # expect −1
    delta_sq = sp.simplify(M * M)
    delta_sq_scalar = sp.simplify(delta_sq[0, 1]).equals(0) and \
        sp.simplify(delta_sq[0, 0] - delta_sq[1, 1]).equals(0)
    delta_not_scalar = not sp.simplify(M[0, 1]).equals(0)

    # collapsed weight relative to depth-1: 1 + q^{1/2} − q^{-1/2}
    rel = sp.simplify(forced / trM("T1"))
    rel_closed = 1 + sp.sqrt(q) - 1 / sp.sqrt(q)
    rel_ok = sp.simplify(rel - rel_closed).equals(0)

    # z^ℓ at depths ≤ 2 (holds by construction of the solve for T1/T12;
    # verify independently on T2 and T21)
    z_series_ok = (sp.simplify(trM("T2") - z).equals(0)
                   and sp.simplify(trM("T21") - z**2).equals(0))

    return {
        "braid_relation_ok": bool(braid_ok),
        "z_series_depth_le2_ok": bool(z_series_ok),
        "tr_T121_eq_z_plus_h_z2": bool(identity_ok),
        "chi21_delta_eq_zero": bool(chi21_delta_zero),
        "det_rho21_delta": sp.sstr(det_delta),
        "delta_squared_scalar_on_21": bool(delta_sq_scalar),
        "delta_not_scalar_on_21": bool(delta_not_scalar),
        "rel_weight_depth3_over_depth1": sp.sstr(rel_closed),
        "rel_weight_identity_ok": bool(rel_ok),
        "y_solved": {
            "y3": sp.sstr(sp.simplify(sol[y3])),
            "y21": sp.sstr(sp.simplify(sol[y21])),
            "y111": sp.sstr(sp.simplify(sol[y111])),
        },
    }


# ────────────────────────────────────────────────────────────────────
# (2a) numeric layer — 50 dps cross-check at q₀
# ────────────────────────────────────────────────────────────────────

def numeric_2a(q, qi, z) -> dict:
    h = q - qi
    words = {"e": [], "T1": [1], "T2": [2], "T12": [1, 2],
             "T21": [2, 1], "T121": [1, 2, 1]}
    depth = {"e": 0, "T1": 1, "T2": 1, "T12": 2, "T21": 2, "T121": 3}
    parts = [tuple(p) for p in partitions_of(3)]
    y = {lam: y_lambda_wenzl_bridge_numeric(list(lam), str(q), mp.mp.dps)
         for lam in parts}
    chi = {}
    for name, w in words.items():
        chi[name] = {lam: chi_lambda_mpmath(list(lam), w, str(q), mp.mp.dps)
                     for lam in parts}
    trM = {name: sum(y[lam] * chi[name][lam] for lam in parts)
           for name in words}

    dev_z_series = max(
        mp.fabs(trM[n] - z ** depth[n])
        for n in words if depth[n] <= 2
    )
    dev_t121 = mp.fabs(trM["T121"] - (z + h * z * z))
    dev_chi21_zero = mp.fabs(chi["T121"][(2, 1)])

    # α_3 comparison numbers (the observed assignment is α_3 = 1)
    z3 = z ** 3
    tr_delta = trM["T121"]
    rel_d3_d1 = tr_delta / trM["T1"]  # = 1 + q^{1/2} − q^{-1/2}
    return {
        "trM_by_word": {n: mp.nstr(trM[n], 30) for n in words},
        "max_dev_z_series_depth_le2": mp.nstr(dev_z_series, 5),
        "dev_tr_T121_vs_z_plus_hz2": mp.nstr(dev_t121, 5),
        "dev_chi21_T121_vs_zero": mp.nstr(dev_chi21_zero, 5),
        "alpha3_candidates": {
            "series_z3": mp.nstr(z3, 20),
            "tr_M_T121": mp.nstr(tr_delta, 20),
            "rel_depth3_over_depth1": mp.nstr(rel_d3_d1, 20),
            "rel_dev_from_assigned_1": mp.nstr(mp.fabs(rel_d3_d1 - 1), 10),
            "classical_limit_q_to_1": "1 (exact: 1 + q^{1/2} − q^{-1/2} → 1)",
        },
        "devs": {
            "z_series": dev_z_series,
            "t121": dev_t121,
            "chi21_zero": dev_chi21_zero,
            "rel_dev_alpha3": mp.fabs(rel_d3_d1 - 1),
        },
    }


# ────────────────────────────────────────────────────────────────────
# (2b) plateau resummation
# ────────────────────────────────────────────────────────────────────

def poincare_coeffs(n: int) -> list[int]:
    """Coefficients of [n]_t! = Π_{i=1}^{n-1} (1 + t + … + t^i):
    N_k = #{w ∈ S_n : ℓ(w) = k} (GB/Coxeter-length filtration)."""
    coeffs = [1]
    for i in range(1, n):
        new = [0] * (len(coeffs) + i)
        for k, c in enumerate(coeffs):
            for j in range(i + 1):
                new[k + j] += c
        coeffs = new
    return coeffs


def layer_counts(n: int) -> dict[str, dict[int, int]]:
    """N_k under the four readings for H_n."""
    cox = {k: c for k, c in enumerate(poincare_coeffs(n))}
    parts = {}
    dim = {}
    dimsq = {}
    for lam in partitions_of(n):
        k = len(lam) - 1
        d = classical_dim(lam)
        parts[k] = parts.get(k, 0) + 1
        dim[k] = dim.get(k, 0) + d
        dimsq[k] = dimsq.get(k, 0) + d * d
    return {"cox": cox, "parts": parts, "dim": dim, "dimsq": dimsq}


def resum_tail(counts: dict[int, int], z, k_min: int = 4):
    """Σ_{k ≥ k_min} z^k · N_k (exact finite sum at 50 dps)."""
    return sum(z ** k * mp.mpf(c) for k, c in counts.items() if k >= k_min)


def numeric_2b(q, qi, z) -> dict:
    target = mp.mpf(str(M_E_MEV)) * 8 * mp.catalan  # m_e · 8G  (MeV)
    target_dimless = 8 * mp.catalan                  # 8G = Vol(L6a4)
    atoms = {"nucleon(H_3)": 3, "D(H_6)": 6, "T/3He(H_9)": 9,
             "4He(H_12)": 12}
    out = {"target_me_8G_MeV": mp.nstr(target, 30),
           "target_8G_dimensionless": mp.nstr(target_dimless, 30),
           "per_atom": {}}
    spread = {r: [] for r in ("cox", "parts", "dim", "dimsq")}
    for name, n in atoms.items():
        counts = layer_counts(n)
        row = {}
        for reading, cnt in counts.items():
            S = resum_tail(cnt, z)
            rel = (mp.fabs(S / target - 1) if S != 0 else mp.mpf(1))
            rel8g = (mp.fabs(S / target_dimless - 1) if S != 0 else mp.mpf(1))
            if S != 0:
                spread[reading].append(S)
            if rel <= mp.mpf("1e-10"):
                verdict = "IDENTITY"
            elif rel <= mp.mpf("0.10"):
                verdict = f"NEAR-MATCH ({float(rel) * 100:.2f}%)"
            else:
                verdict = "REFUTED-scope-(a)"
            row[reading] = {
                "sum_k_ge4_zk_Nk": mp.nstr(S, 20),
                "rel_dev_vs_me8G": mp.nstr(rel, 6),
                "rel_dev_vs_8G": mp.nstr(rel8g, 6),
                "verdict_vs_me8G": verdict,
            }
        out["per_atom"][name] = row
    # atom-independence: plateau is universal, resummation must not scale with A
    indep = {}
    for reading, vals in spread.items():
        if len(vals) >= 2:
            lo, hi = min(vals), max(vals)
            indep[reading] = {
                "min": mp.nstr(lo, 12), "max": mp.nstr(hi, 12),
                "max_over_min": mp.nstr(hi / lo, 8) if lo > 0 else "inf",
                "atom_independent": bool(hi / lo - 1 < mp.mpf("1e-10")) if lo > 0 else False,
            }
    out["atom_independence"] = indep
    return out


# ────────────────────────────────────────────────────────────────────

def main() -> int:
    set_compute_dps()
    q, qi, z = load_q_50dps()

    print("=" * 72)
    print("PROBE 2 (9b, bean nf8d) — α_k assignment-rule structure checks")
    print("=" * 72)

    print("\n(2a) symbolic (exact in q) …")
    sym = symbolic_2a()
    for k, v in sym.items():
        print(f"  {k}: {v}")

    print("\n(2a) numeric at q₀ (50 dps) …")
    num = numeric_2a(q, qi, z)
    devs = num.pop("devs")
    for k, v in num.items():
        print(f"  {k}: {v}")

    print("\n(2b) plateau resummation Σ_{k≥4} z^k·N_k vs m_e·8G …")
    res = numeric_2b(q, qi, z)
    print(f"  target m_e·8G = {res['target_me_8G_MeV']} MeV")
    for atom, row in res["per_atom"].items():
        for reading, r in row.items():
            print(f"  {atom:>12s} {reading:>6s}: S = {r['sum_k_ge4_zk_Nk']:>24s}"
                  f"  → {r['verdict_vs_me8G']}")
    print(f"  atom-independence: "
          f"{ {k: v['max_over_min'] for k, v in res['atom_independence'].items()} }")

    # ── witness ──
    wb = WitnessBuilder("probe-9b-alphak-structure", engine="mpmath+sympy")
    wb.set_description(
        "PROBE 2 (bean nf8d) on the step-9b depth-stratified α_k "
        "assignment rule. (2a) α_3 centrality: exact character "
        "computation on H_3 — χ^{(2,1)}(Δ)=0 (Δ=σ1σ2σ1 Garside; Δ² "
        "central + det ρ_{(2,1)}(Δ)=−1 force tracelessness), so the "
        "Markov-marker series z^k breaks at k=3 STRUCTURALLY: "
        "tr_M(T_Δ) = z+h·z² = z(1+q^{1/2}−q^{-1/2}) ≠ z³ (derived, "
        "exact); the depth-3/depth-1 relative weight 1+q^{1/2}−q^{-1/2} "
        "≈ 1.1044 near-matches the assigned α_3/α_1 = 1 at 10.4% (exact "
        "as q→1); Δ itself is NOT central (off-diag ≠ 0). (2b) plateau "
        "resummation Σ_{k≥4} z^k N_k vs m_e·8G under 4 layer-count "
        "readings × 4 atoms: no IDENTITY; the sum is strongly atom-"
        "dependent, refuting (scope-(a)) the universal-plateau-as-"
        "geometric-resummation shape. No fit constants."
    )
    wb.set_audit_only(
        "docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md")
    wb.add_parameter("compute_dps", mp.mp.dps)
    wb.add_parameter("q0_source", "q-pinning-50-digit.witness.json (load_q_50dps)")
    wb.add_data("part_2a_symbolic", sym)
    wb.add_data("part_2a_numeric", num)
    wb.add_data("part_2b_resummation", res)

    wb.add_assertion(
        "symbolic_tr_T121_eq_z_plus_h_z2",
        computed=int(sym["tr_T121_eq_z_plus_h_z2"]), expected=1, tolerance=0,
        source="sympy exact: y solved from depth≤2 Markov data forces "
               "tr_M(T_Δ) = z + h·z²",
    )
    wb.add_assertion(
        "symbolic_chi21_delta_zero",
        computed=int(sym["chi21_delta_eq_zero"]), expected=1, tolerance=0,
        source="sympy exact: χ^{(2,1)}(σ1σ2σ1) = 0",
    )
    wb.add_assertion(
        "delta_squared_central_delta_not",
        computed=int(sym["delta_squared_scalar_on_21"]
                     and sym["delta_not_scalar_on_21"]),
        expected=1, tolerance=0,
        source="ρ_{(2,1)}(Δ)² scalar (full twist central) while ρ_{(2,1)}(Δ) "
               "is not scalar — Δ not central, Δ² central",
    )
    wb.add_assertion(
        "numeric_z_series_depth_le2",
        computed=float(devs["z_series"]), expected=0.0, tolerance=1e-40,
        source="tr_M(T_w) = z^{ℓ(w)} at 50 dps for all depth ≤ 2 basis words",
    )
    wb.add_assertion(
        "numeric_tr_T121_closed_form",
        computed=float(devs["t121"]), expected=0.0, tolerance=1e-40,
        source="tr_M(T_Δ) = z + h·z² at 50 dps (Wenzl-bridge y × seminormal χ)",
    )
    wb.add_assertion(
        "alpha3_value_not_derived_near_match_10pc",
        computed=float(devs["rel_dev_alpha3"]), expected=0.104,
        tolerance=0.01,
        source="collapsed depth-3/depth-1 weight 1+q^{1/2}−q^{-1/2} deviates "
               "from the assigned α_3 = 1 by ≈10.4% at q₀ (exact only at q→1) "
               "— the BREAK is derived, the VALUE 1 is a near-match",
    )
    # 2b: no reading is an identity, and every reading is atom-dependent
    any_identity = any(
        r["verdict_vs_me8G"] == "IDENTITY"
        for row in res["per_atom"].values() for r in row.values()
    )
    any_indep = any(v["atom_independent"]
                    for v in res["atom_independence"].values())
    wb.add_assertion(
        "plateau_resummation_no_identity",
        computed=int(any_identity), expected=0, tolerance=0,
        source="no (atom, N_k-reading) pair matches m_e·8G at 1e-10 — "
               "plateau ≠ Σ_{k≥4} z^k N_k (scope-(a): this resummation "
               "shape, as-is, alone)",
    )
    wb.add_assertion(
        "plateau_resummation_atom_dependent",
        computed=int(any_indep), expected=0, tolerance=0,
        source="every N_k reading gives an A-dependent tail sum; the "
               "α_{k≥4} plateau is A-independent, so the shape mismatch "
               "is structural (still scope-(a): other weightings untested)",
    )
    wb.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
