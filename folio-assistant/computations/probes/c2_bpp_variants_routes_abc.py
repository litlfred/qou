"""Routes A + B + C for the pp-Coulomb derivation, run end-to-end.
Plus A4 (bar-symmetric/antisymmetric decomposition) per user prompt
2026-06-04 ("why throw Re/Im info away prematurely?").

A. Compute-side tightening: diproton B_pp at H_6 via PR #1748's kernel
   at 50 dps. Four variants:
     A1 — |Re χ|              (source replication; sign-mixing)
     A2 — Re χ signed         (no abs)
     A3 — bar-product √(χ(q)χ(q⁻¹))   per PR #1742
     A4 — bar-symmetric/antisymmetric:
            χ_sym  := (χ(q) + χ(q⁻¹))/2  ← maps to STRONG (q+q⁻¹)
            χ_anti := (χ(q) − χ(q⁻¹))/2  ← maps to COULOMB (q−q⁻¹)

B. Hopf-tr_M closed-form: replace B_pp with the framework's
   Lean-proved Hopf trace 1 + (q-1)/√q (canonical at H_2),
   measure what "scale" closes the AME split.

C. Synthesis: which (B_pp variant, scale derivation) combination
   lands closest to the AME split.

## Key structural finding (A4, 2026-06-04)

The PER-CROSSING identity `Coulomb/strong = tanh(ln q₀)` does NOT
carry through to PER-BLOCK partition sums.  Per crossing the
ratio is (q-q⁻¹)/(q+q⁻¹) ≈ 0.10.  But after summing y_λ-weighted
χ_anti vs χ_sym over partitions:

  B_sym  = Σ_λ y_λ_sym · (χ_sym_free − χ_sym_atom)  = 1.081 MeV
  B_anti = Σ_λ y_λ_sym · (χ_anti_free − χ_anti_atom) = 0.996 MeV
  ratio anti/sym (block-level) = 0.921   vs per-crossing tanh(ln q₀)=0.104
  (off by 8.86×)

The source's formula `dHe = tanh(ln q₀) · B_pp` is structurally
inconsistent: it applies a per-crossing analytic ratio to a
per-block total. The 3.21× residual factor is largely the
accumulated approximation between per-crossing and per-block
levels — NOT a clean signature of a missing categorical multiplier.

EXPLORATORY. No production wiring. No fit.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

# Portable path setup — relative to this script (Copilot review PR #1765).
HERE = Path(__file__).resolve().parent           # …/probes/
COMPUTATIONS_ROOT = HERE.parent                  # …/folio-assistant/computations/
if str(COMPUTATIONS_ROOT) not in sys.path:
    sys.path.insert(0, str(COMPUTATIONS_ROOT))

import _path_bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_at_q_inv_via_native_mpfr import _word_to_signed  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402

AME_SPLIT = mp.mpf("0.7638")


# ─── ROUTE A — four B_pp variants ───
def bpp_variant(agg_fn, free_q0, atom_q0, free_qi, atom_qi, y_q0, y_qi, E0):
    """agg_fn takes (chi_free, chi_atom, chi_free_qi, chi_atom_qi, y, y_qi) → MeV scalar contribution."""
    B = mp.mpf(0)
    for lam in free_q0:
        c0 = free_q0[lam]
        ca = atom_q0[lam]
        ci = free_qi[lam]
        cai = atom_qi[lam]
        y = y_q0.get(lam)
        yi = y_qi.get(lam)
        if y is None:
            continue
        B += agg_fn(c0, ca, ci, cai, y, yi)
    return E0 * B


def agg_abs_re(c0, ca, ci, cai, y, yi):
    """Source convention: y_λ · (|Re χ_free| − |Re χ_atom|)."""
    return y * (abs(mp.re(c0)) - abs(mp.re(ca)))


def agg_signed_re(c0, ca, ci, cai, y, yi):
    """Signed: y_λ · (Re χ_free − Re χ_atom). No abs."""
    return y * (mp.re(c0) - mp.re(ca))


def agg_bar(c0, ca, ci, cai, y, yi):
    """PR #1742 bar form: y_λ_sym · (‖χ_free‖_bar − ‖χ_atom‖_bar)
    where ‖χ‖_bar = √(Re(χ(q)·χ(q⁻¹))) (sign-tracked, imaginary if pairing<0)."""
    y_sym = (y + yi) / 2

    def length(cq, cqi):
        pairing = mp.re(cq * cqi)
        if pairing >= 0:
            return mp.sqrt(pairing)
        else:
            return -mp.sqrt(-pairing)  # signed for the bar formula
    return y_sym * (length(c0, ci) - length(ca, cai))


def main() -> int:
    """Run Routes A+B+C+A4 end-to-end; emit witness JSON to the
    canonical computations dir (relative to this script)."""
    import pyhecke_native as pn  # heavy native dep — imported inside main()
    mp.mp.dps = 60

    q0 = mp.mpf(Q_50_DIGIT_STR)
    q0_inv = 1 / q0
    q0_str = Q_50_DIGIT_STR
    with mp.workdps(60):
        qi_str = mp.nstr(q0_inv, 50, strip_zeros=False)
    m_e = mp.mpf(str(M_E_MEV))
    E0 = m_e / (q0 * (q0 - 1))  # CAL-3 prefactor

    # Coulomb/strong ratio (proved symbolically equal to (q-q⁻¹)/(q+q⁻¹))
    tanh_lnq0 = mp.tanh(mp.log(q0))

    # ─── Build diproton chi caches at q₀ and q₀⁻¹ via PR #1748's kernel ───
    n = 6  # H_6 = 3·A = 3·(2+0) = 6
    word_free = atom_braid_word_3A(2, 0, include_inter=False)
    word_atom = atom_braid_word_3A(2, 0, include_inter=True)
    ws_free = _word_to_signed(word_free)
    ws_atom = _word_to_signed(word_atom)

    print(f"diproton H_{n}: free={len(ws_free)}fac atom={len(ws_atom)}fac")
    print(f"  q₀     = {float(q0):.10f}")
    print(f"  q₀⁻¹   = {float(q0_inv):.10f}")
    print(f"  E_0    = {float(E0):.6f} MeV (CAL-3)")
    print(f"  tanh(ln q₀) = (q-q⁻¹)/(q+q⁻¹) = {mp.nstr(tanh_lnq0, 12)}")
    print()

    t0 = time.time()
    free_q0 = {tuple(lam): mp.mpf(s) for lam, s in
               pn.chi_lambda_all_partitions_mpfr(n, ws_free, q0_str, 50)}
    atom_q0 = {tuple(lam): mp.mpf(s) for lam, s in
               pn.chi_lambda_all_partitions_mpfr(n, ws_atom, q0_str, 50)}
    free_qi = {tuple(lam): mp.mpf(s) for lam, s in
               pn.chi_lambda_all_partitions_mpfr(n, ws_free, qi_str, 50)}
    atom_qi = {tuple(lam): mp.mpf(s) for lam, s in
               pn.chi_lambda_all_partitions_mpfr(n, ws_atom, qi_str, 50)}
    print(f"  native chi: 4×11 partitions in {time.time()-t0:.2f}s")

    # y_lambda at q₀ and q₀⁻¹
    y_q0 = {tuple(lam): mp.mpf(str(y_lambda_wenzl_bridge_numeric(tuple(lam), q0_str, dps=50)))
            for lam in [tuple(p) for p in parts_of(n)]}
    y_qi = {tuple(lam): mp.mpf(str(y_lambda_wenzl_bridge_numeric(tuple(lam), qi_str, dps=50)))
            for lam in [tuple(p) for p in parts_of(n)]}

    variants = {
        "A1_abs_Re_chi (replicate source, 50dps)": agg_abs_re,
        "A2_signed_Re_chi (drop abs)            ": agg_signed_re,
        "A3_bar_pairing_per_PR1742              ": agg_bar,
    }

    print("\n── ROUTE A: B_pp variants on diproton at H_6 ──")
    print("  source value (30 dps witness):           0.237670  MeV  → 3.214× gap")
    print()
    A_results = {}
    for name, agg in variants.items():
        Bpp = bpp_variant(agg, free_q0, atom_q0, free_qi, atom_qi, y_q0, y_qi, E0)
        dHe = tanh_lnq0 * Bpp
        factor = AME_SPLIT / dHe if dHe != 0 else mp.inf
        A_results[name] = {
            "B_pp_MeV": mp.nstr(Bpp, 10),
            "dHe_MeV": mp.nstr(dHe, 10),
            "remaining_factor": mp.nstr(factor, 10),
        }
        print(f"  {name}: B_pp = {float(Bpp):>9.6f}  dHe = {float(dHe):>9.6f}  factor = {float(factor):>7.4f}×")

    # ─── ROUTE B — Hopf tr_M closed form ───
    # Lean-proved: tr_M(σ₁²) = 1 + (q-1)/√q on H_n (Markov-invariant, n ≥ 2)
    trM_Hopf = 1 + (q0 - 1) / mp.sqrt(q0)
    print("\n── ROUTE B: Hopf tr_M closed form (Lean-proved 1 + (q-1)/√q) ──")
    print(f"  tr_M(σ²)         = {mp.nstr(trM_Hopf, 12)}")
    print(f"  tr_M(σ²) − 1     = (q-1)/√q     = {mp.nstr(trM_Hopf - 1, 12)}")
    print(f"  tanh(ln q₀)      = (q²-1)/(q²+1) = {mp.nstr(tanh_lnq0, 12)}")
    print(f"  ratio            = {mp.nstr((trM_Hopf-1)/tanh_lnq0, 12)}")
    # Symbolic difference
    q = sp.symbols('q', positive=True, real=True)
    diff_sym = sp.simplify(((q - 1)/sp.sqrt(q)) - (q**2 - 1)/(q**2 + 1))
    print(f"  symbolic diff    = {sp.simplify(diff_sym)}  (not identical)")
    print("  ⇒ tr_M(σ²)−1 and tanh(ln q) are DIFFERENT q-rational objects, both real-positive at q₀")

    # What "scale" closes the AME split if we use tr_M(σ²)−1 instead of tanh(ln q₀)?
    need_scale_via_trM = AME_SPLIT / (trM_Hopf - 1)
    print("\n  If E_pp = scale · (tr_M(σ²)−1):")
    print(f"    scale = AME_split / (tr_M(σ²)−1) = {float(need_scale_via_trM):.6f} MeV")
    print(f"    in m_e units                      = {float(need_scale_via_trM/m_e):.6f}")
    # Hunt for a categorical identity for this scale
    for label, val in [
        ("m_e", m_e), ("m_e · A=2", 2*m_e), ("m_e · 3", 3*m_e),
        ("E_0", E0), ("E_0 · 2", 2*E0), ("E_0 · lw_c2", E0*((q0+1)**2/(3*q0))),
        ("E_0 · lw_c2 · 12/5", E0*((q0+1)**2/(3*q0))*mp.mpf(12)/5),
        ("E_0 · 12/5", E0*mp.mpf(12)/5),
        ("E_0 · (q+1)²/q", E0*((q0+1)**2/q0)),
        ("m_e · (q+1)²·12/5/(q·3)", m_e*((q0+1)**2/(3*q0))*mp.mpf(12)/5),
    ]:
        ratio = need_scale_via_trM / val
        if 0.1 < float(ratio) < 30:
            ratio_f = float(ratio)
            clean_check = ""
            for n_, d_ in [(1,1),(2,1),(3,2),(4,3),(5,3),(7,3),(7,4),(12,5),(5,2)]:
                if abs(ratio_f - n_/d_) < 0.01:
                    clean_check = f" ≈ {n_}/{d_}"
            print(f"    scale / {label:<28} = {ratio_f:>10.6f}{clean_check}")

    # ─── ROUTE C — synthesis ───
    print("\n── ROUTE C: synthesis — best chain candidate ──")
    lw_c2 = (q0 + 1)**2 / (3*q0)
    print(f"  lw_c2 at q₀ = {float(lw_c2):.8f}")
    print("  12/5         = 2.40000000   (Pieri H_3→H_4 trace at q=1, derived)")
    print()
    print(f"  {'variant':<46} {'dHe·lw_c2·(12/5)':>20} {'vs AME 0.7638':>14}")
    for name, agg in variants.items():
        Bpp = bpp_variant(agg, free_q0, atom_q0, free_qi, atom_qi, y_q0, y_qi, E0)
        dHe = tanh_lnq0 * Bpp
        pred = dHe * lw_c2 * (mp.mpf(12)/5)
        rel = (pred - AME_SPLIT) / AME_SPLIT * 100
        print(f"  {name}: {float(pred):>18.6f}  {float(rel):>+12.4f} %")

    # Hopf-route candidate: dHe_Hopf = m_e · (tr_M(σ²)−1) directly,
    dHe_Hopf = m_e * (trM_Hopf - 1)
    pred_Hopf = dHe_Hopf * lw_c2 * (mp.mpf(12)/5)
    print("\n  HOPF route (m_e · (tr_M(σ²)−1) · lw_c2 · (12/5)):")
    print(f"    = {float(pred_Hopf):.6f} MeV  vs AME 0.7638  → {float((pred_Hopf-AME_SPLIT)/AME_SPLIT*100):+.4f}%")
    print(f"  HOPF route × 4 (proton-pair factor 2·2): "
          f"{float(4*pred_Hopf):.6f}")
    for A in [1, 2, 3, 4]:
        p = A * m_e * (trM_Hopf - 1) * lw_c2 * (mp.mpf(12)/5)
        print(f"  A={A}: A·m_e·(tr_M-1)·lw_c2·(12/5) = {float(p):.6f}  vs AME 0.7638  ({float((p-AME_SPLIT)/AME_SPLIT*100):+.4f}%)")

    # ─── ROUTE A4 — bar-symmetric/antisymmetric decomposition ───
    print("\n── A4: BAR-SYM/ANTI DECOMPOSITION (no info loss) ──")
    B_sym = mp.mpf(0)
    B_anti = mp.mpf(0)
    for lam in free_q0:
        y = y_q0.get(lam)
        yi = y_qi.get(lam)
        if y is None:
            continue
        y_sym = (y + yi) / 2
        chi_sym_free = (free_q0[lam] + free_qi[lam]) / 2
        chi_sym_atom = (atom_q0[lam] + atom_qi[lam]) / 2
        chi_anti_free = (free_q0[lam] - free_qi[lam]) / 2
        chi_anti_atom = (atom_q0[lam] - atom_qi[lam]) / 2
        B_sym += y_sym * (mp.re(chi_sym_free) - mp.re(chi_sym_atom))
        B_anti += y_sym * (mp.re(chi_anti_free) - mp.re(chi_anti_atom))
    B_sym_MeV = E0 * B_sym
    B_anti_MeV = E0 * B_anti
    ratio_block = B_anti_MeV / B_sym_MeV if B_sym_MeV != 0 else mp.mpf(0)

    print(f"  B_sym  (bar-symmetric  → strong piece)  = {float(B_sym_MeV):.6f} MeV")
    print(f"  B_anti (bar-antisymm.  → Coulomb piece) = {float(B_anti_MeV):.6f} MeV")
    print(f"  block ratio anti/sym                    = {float(ratio_block):.6f}")
    print(f"  per-crossing tanh(ln q₀)                 = {float(tanh_lnq0):.6f}")
    print(f"  ratio mismatch                           = {float(ratio_block/tanh_lnq0):.4f}×")
    print()
    print("  IMPLICATION: source's `dHe = tanh(ln q₀) · B_pp` applies a")
    print("  PER-CROSSING analytic ratio to a PER-BLOCK total — structural")
    print("  inconsistency.  The 3.21× residual factor is largely this")
    print("  approximation, NOT a missing categorical multiplier.")
    print()
    print(f"  B_anti directly as Coulomb piece: vs AME 0.7638 MeV → "
          f"{float((B_anti_MeV-AME_SPLIT)/AME_SPLIT*100):+.4f}%")

    # Save witness — portable path (Copilot review PR #1765)
    out = {
        "computation": "route-abc-bpp-derivation",
        "description": (
            "Routes A+B+C for the pp-Coulomb derivation: (A) measure how 3 "
            "B_pp variants shift dHe and the 3.21× residual; (B) reframe via "
            "Lean-proved Hopf tr_M closed form (q-1)/√q; (C) synthesise. "
            "Plus A4: bar-sym/anti decomposition showing per-crossing tanh "
            "is NOT the per-block Coulomb/strong ratio. "
            "EXPLORATORY. No production wiring. No fit."),
        "q0": str(q0),
        "tanh_lnq0_aka_q_rational": mp.nstr(tanh_lnq0, 30),
        "ame_split_MeV": str(AME_SPLIT),
        "E_0_MeV": mp.nstr(E0, 12),
        "m_e_MeV": str(m_e),
        "route_A_variants": A_results,
        "route_B_hopf_trM": {
            "trM_Hopf_at_q0": mp.nstr(trM_Hopf, 16),
            "trM_minus_1": mp.nstr(trM_Hopf - 1, 16),
            "vs_tanh_lnq0_diff": mp.nstr((trM_Hopf - 1) - tanh_lnq0, 12),
            "needed_scale_MeV": mp.nstr(need_scale_via_trM, 12),
        },
        "route_A4_bar_sym_anti": {
            "B_sym_MeV": mp.nstr(B_sym_MeV, 12),
            "B_anti_MeV": mp.nstr(B_anti_MeV, 12),
            "block_ratio_anti_over_sym": mp.nstr(ratio_block, 12),
            "per_crossing_tanh_lnq0": mp.nstr(tanh_lnq0, 12),
            "ratio_mismatch_factor": mp.nstr(ratio_block / tanh_lnq0, 8),
        },
    }
    out_path = COMPUTATIONS_ROOT / "route-abc-bpp-derivation.witness.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWitness: {out_path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
