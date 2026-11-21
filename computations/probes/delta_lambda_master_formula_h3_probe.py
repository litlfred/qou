#!/usr/bin/env python3
"""Δ_λ master-formula route — H₃ collapse test + q-Casimir energy (EXPLORATORY).

Owner steer: attack the cooperative-binding (Δ_λ) gate via the master formula
(conj:confinement-frobenius-reciprocity) the way g_A is computed, NOT a Δ_λ
content-count ansatz. This is the tractable FIRST step from
docs/audits/2026-06-17-delta-lambda-master-formula-active-set-redesign.md §4:
test, at the single-nucleon H₃ level (existing 6×6 Gram, no new wall), whether
the master formula adds structure beyond the raw Markov trace.

Two decisive, parameter-free questions:

  Q1 (COLLAPSE). The prop ASSERTS binding is the O=H special case that
     "reduces to the raw trace". Test the cleanest instance: does the
     master-formula expectation of the IDENTITY observable,
        ⟨1⟩_T = Σ_{i,j∈A*} u_i (G⁻¹)_{ij} tr_M(b_j),
     equal the raw trace tr_M(T) of the bound state T = 𝓑_3 (proton)?
     - equal   ⇒ collapse holds ⇒ master formula adds nothing for O=1.
     - differ  ⇒ collapse FAILS ⇒ the G⁻¹+active-set machinery genuinely
       changes the answer (route is live; worth the H₆ deuteron build).

  Q2 (q-CASIMIR ENERGY). With O = the q-Casimir C_q (def:q-casimir),
     central, eigenvalue c_λ on Wedderburn block λ — principled candidate for
     O=H. Two readings (reported side by side, no tuning):
       (a) SU(2):  c_λ = [j]_q[j+1]_q,  j=(λ₁−λ₂)/2   (2-row blocks only)
       (b) Hecke JM-sum:  c_λ = Σ_{(i,j)∈λ}(j−i)     (all blocks; the
           Jucys–Murphy / symmetric-group Casimir — appropriate for the
           "full Hecke arena", keystone 2026-06-17). (b) reduces to the
           additive-content of (a) on 2-row blocks.
     Compute ⟨C_q⟩_T (master) vs the raw q-Casimir trace tr_M(C_q·T), to see
     whether the active-set dualisation reshapes the energy.

NO fit, NO production rewire, NO canonical witness. Single nucleon only — this
checks the MACHINERY + the collapse claim; it does NOT yet test cooperative
(≥2-nucleon) binding (that needs the H₆ Gram, the documented next step).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))
sys.path.insert(0, str(ROOT.parent / "tools" / "pyhecke" / "python"))

import mpmath as mp  # noqa: E402
# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# 50-dps source (NO FLOAT64). Behaviour is unchanged: Q_MP differs from the
# f64 Q by ~1e-17, far inside the 1e-12 cache tolerance either way.
#
# NOT a layer straddle, though it looks like one: `y-lambda-at-q0.witness.json`
# is muon-built, but the cache gate compares the caller's q against the
# WITNESS's own recorded q0, not against q_parameter.Q. |q_muon - q_proton| =
# 1.28e-8 is 12810x the 1e-12 tolerance, so a proton-q0 caller misses the
# muon cache and falls through to the live closed form at the q it asked for.
# (The 1e-12 sits between float64 ulp at q~1.11, 2.46e-16, and that anchor gap.)
# AGENTS.md still describes the older, broken gate -- the code is ahead of it.
from q_parameter import (Q_MP as q0, Q_INV_MP as qi0,      # noqa: E402
                         HA_MP as h_q)
from pyhecke.gram import NF_BASIS, NF_NAMES, TR_M  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from char_fast import chi_lambda_fast_mp  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

Q = mp.mpf(str(q0))
QI = mp.mpf(str(qi0))
H = Q - QI

PARTS3 = [(3,), (2, 1), (1, 1, 1)]   # partitions of 3 (H₃ Wedderburn blocks)


def qint(n: int) -> mp.mpf:
    """symmetric q-number [n]_q = (q^n − q^{-n})/(q − q^{-1})."""
    return (Q**n - Q**(-n)) / (Q - QI)


def casimir_su2(lam) -> mp.mpf:
    """(a) SU(2) q-Casimir [j]_q[j+1]_q, j=(λ₁−λ₂)/2; 0 for >2-row blocks."""
    if len(lam) > 2:
        return mp.mpf(0)
    l1 = lam[0]
    l2 = lam[1] if len(lam) > 1 else 0
    j2 = (l1 - l2)               # 2j  (integer)
    # [j]_q[j+1]_q with half-integer j → use [2j] form via q^{1/2}; here
    # j=(λ₁−λ₂)/2, so evaluate [j]_q[j+1]_q in q^{1/2}.
    qh = Q**(mp.mpf(1) / 2)
    def qn(x):  # [x]_q for possibly half-integer x, base q
        return (qh**(2*x) - qh**(-2*x)) / (qh**2 - qh**-2)
    j = mp.mpf(j2) / 2
    return qn(j) * qn(j + 1)


def casimir_jm(lam) -> mp.mpf:
    """(b) Jucys–Murphy / symmetric-group Casimir: additive content sum
    Σ_{(i,j)∈λ}(j−i) (0-indexed rows i, cols j). Defined on ALL blocks."""
    s = 0
    for i, row in enumerate(lam):
        for j in range(row):
            s += (j - i)
    return mp.mpf(s)


def nf_to_terms(word):
    """NF basis word (tuple of generator indices) → (c,d,gen) braid terms
    (positive braid: each σ_g = 1·σ_g + 0). char_fast convention."""
    return [(mp.mpf(1), mp.mpf(0), g) for g in word]


def proton_braid_terms():
    """𝓑_3 = (σ_0 σ_1^{-1})^3, with σ_1^{-1} = σ_1 − h (Hecke inverse)."""
    out = []
    for _ in range(3):
        out.append((mp.mpf(1), mp.mpf(0), 0))     # σ_0
        out.append((mp.mpf(1), -H, 1))            # σ_1^{-1} = σ_1 − h
    return out


def chi_vec(terms):
    """{λ: χ^λ(word)} over PARTS3 via char_fast (full Hoefsmit, any word)."""
    return {lam: mp.mpf(chi_lambda_fast_mp(lam, terms, Q).real) for lam in PARTS3}


def main() -> int:
    # Wedderburn Markov weights y_λ for H₃ (tr_M = Σ_λ y_λ χ^λ).
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(3, q0).items()}

    # ── sanity: Σ_λ y_λ χ^λ(b_j) must reproduce the given TR_M[j] ──
    chi_nf = [chi_vec(nf_to_terms(b)) for b in NF_BASIS]
    trM_recon = [mp.fsum(y[lam] * chi_nf[j][lam] for lam in PARTS3)
                 for j in range(len(NF_BASIS))]
    max_dev = max(abs(trM_recon[j] - mp.mpf(str(TR_M[j])))
                  for j in range(len(NF_BASIS)))
    # The committed Gram/TR_M witness (2026-05-28) is at the OLD q₀ (pre the
    # proton-anchor re-pin); char_fast here uses the current q₀, so a ~1e-8
    # stale-q₀ inconsistency is expected and harmless for this qualitative test.
    tol = mp.mpf(10)**-6
    print(f"  convention check: max|Σ y_λχ^λ(b_j) − TR_M[j]| = {mp.nstr(max_dev,3)}"
          f"  ({'OK (≈stale-q₀ noise)' if max_dev < tol else 'MISMATCH — abort'})")
    if max_dev >= tol:
        print("  conventions do not match; the Gram basis and char_fast disagree.")
        return 1

    # ── LP: proton bound state on the 6-elt NF basis (n_target = 1) ──
    GRAM = np.array(json.loads((ROOT / "gram-matrix-dual.witness.json")
                               .read_text())["gram_matrix"], dtype=float)
    GINV = np.array(json.loads((ROOT / "gram-matrix-dual.witness.json")
                               .read_text())["gram_inverse"], dtype=float)
    lp = solve_operator_selection_lp(np.asarray(TR_M, dtype=float), GRAM, 1.0)
    yv = np.asarray(lp.y_star, dtype=float)
    A = [i for i, v in enumerate(yv) if abs(v) > 1e-9] or list(range(6))
    print(f"  LP active set A* = {A}  ({[NF_NAMES[i] for i in A]}); "
          f"shadow u* = {[round(float(yv[i]),4) for i in A]}")
    # ── LP-solver vs prop:operator-selection-lp discrepancy ──
    # The prop claims the proton optimum is 𝓑_3 (objective tr_M(𝓑_3)≈0.998,
    # active set {σ_0, L_-} — TWO channels). The solver returns a degenerate
    # vertex (active {γ}, objective≈0): it finds LOWER action than 𝓑_3, so it
    # does NOT reproduce the prop's confinement selection.
    prot0 = proton_braid_terms()
    trM_p0 = mp.fsum(y[lam] * chi_vec(prot0)[lam] for lam in PARTS3)
    print(f"  LP-vs-prop: solver primal_obj = {float(lp.primal_obj):.4e}  "
          f"(active {[NF_NAMES[i] for i in A]})  vs  prop 𝓑_3 objective "
          f"tr_M(𝓑_3) = {mp.nstr(trM_p0,6)} (active {{σ_0, L_-}}). "
          f"{'⚠ solver finds lower-action degenerate vertex → does NOT select 𝓑_3' if float(lp.primal_obj) < float(trM_p0)-1e-3 else 'matches'}")

    def master(obs):   # ⟨O⟩_T = Σ_{i,j∈A*} u_i (G⁻¹)_{ij} ⟨O,b_j⟩
        u = yv[A]
        Ginv_A = GINV[np.ix_(A, A)]
        o = np.array([float(obs[j]) for j in A], dtype=float)
        return float(u @ Ginv_A @ o)

    # ── Q1: collapse — master ⟨1⟩_T  vs  raw tr_M(𝓑_3) ──
    obs_id = trM_recon                                   # ⟨1,b_j⟩ = tr_M(b_j)
    prot = proton_braid_terms()
    chi_prot = chi_vec(prot)
    trM_proton = mp.fsum(y[lam] * chi_prot[lam] for lam in PARTS3)
    m_id = master(obs_id)
    print("\n  Q1 COLLAPSE TEST (O = identity):")
    print(f"    raw    tr_M(𝓑_3)        = {mp.nstr(trM_proton, 10)}")
    print(f"    master ⟨1⟩_T            = {m_id:.10f}")
    rel = abs(mp.mpf(m_id) - trM_proton) / (1 + abs(trM_proton))
    collapse = rel < mp.mpf(10)**-6
    print(f"    rel diff               = {mp.nstr(rel,4)}  → "
          f"{'COLLAPSE HOLDS (master = raw)' if collapse else 'COLLAPSE FAILS (master ≠ raw — route is LIVE)'}")

    # ── Q2: q-Casimir energy — master ⟨C_q⟩_T  vs  raw tr_M(C_q·𝓑_3) ──
    print("\n  Q2 q-CASIMIR ENERGY (O = C_q):")
    for cname, cfn in (("SU(2) [j][j+1]", casimir_su2), ("Hecke JM content-sum", casimir_jm)):
        c = {lam: cfn(lam) for lam in PARTS3}
        obs_C = [mp.fsum(y[lam] * c[lam] * chi_nf[j][lam] for lam in PARTS3)
                 for j in range(len(NF_BASIS))]     # ⟨C_q,b_j⟩=tr_M(C_q b_j)
        raw_C = mp.fsum(y[lam] * c[lam] * chi_prot[lam] for lam in PARTS3)
        m_C = master(obs_C)
        print(f"    [{cname}]  c_λ = "
              f"{ {''.join(map(str,k)): mp.nstr(c[k],4) for k in PARTS3} }")
        print(f"        raw    tr_M(C_q·𝓑_3) = {mp.nstr(raw_C, 8)}")
        print(f"        master ⟨C_q⟩_T       = {m_C:.8f}")

    print("\n  NOTE: single-nucleon H₃ — checks the MACHINERY + the collapse "
          "claim. Cooperative (≥2-nucleon) binding needs the H₆ Gram (next step).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
