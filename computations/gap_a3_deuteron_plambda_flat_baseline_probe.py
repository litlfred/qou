#!/usr/bin/env python3
"""
GAP-A-3 §4 binding-P_λ probe — the flat baseline + the bar-even admissibility
constraint, now that the infra blocker (pyhecke_native / canonical χ^λ) is lifted.

This is the next step the cbnf bean explicitly deferred to an "infra-enabled
session" (`2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md`
§4–§5). The per-isotope binding gate is

    A(K)·Σ_{λ⊢3A} y_λ(q₀) χ^λ(β_K) P_λ(K) = −B(K)/m_e ,

with A(K) λ-independent (Phase-4 derived) and P_λ the OPEN partition projection.
cbnf §4's two grounded, non-fit observations:

  (i)  FLAT BASELINE: since tr_M(β_K)=Σ_λ y_λ χ^λ(β_K) (canonical Frobenius pairing),
       setting P_λ≡1 gives exactly A(K)·tr_M(β_K). So P_λ is the per-partition
       DEVIATION of binding from the flat mass/trace distribution; the binding lives
       entirely in the redistribution (P_λ−1) reweighted by y_λ χ^λ.
  (ii) BAR-EVEN ADMISSIBILITY: the v9 closure symmetrises χ^λ with χ^{λᵀ}; tr_M is the
       P_λ≡1 point; so any admissible P_λ must be λ↔λᵀ (transpose / bar) covariant.
       A candidate P_λ breaking that symmetry is refuted on paper.

This probe RUNS (i)+(ii) for the deuteron canonically (no convention re-derivation):
y_λ from `wedderburn_jones_markov.y_lambda_at`; χ^λ(β_D) from
`chi_monotone_transfer.chi_all_lambda(atom_braid_word_3A(1,1), 6)`. It reports the
flat baseline tr_M(β_D), the per-λ weights y_λ χ^λ, and the bar-even subspace
(dim 6 of p(6)=11) the binding redistribution must live in.

DISCIPLINE: NO fit; NO 7th ansatz. This characterises the admissible P_λ SUBSPACE
(the formalize-first pruning) + the flat baseline — it does NOT solve the
underdetermined 1-equation-11-unknowns system, and proposes no P_λ value.
"""
import sys
sys.path.insert(0, "computations")
import mpmath as mp
from wedderburn_jones_markov import y_lambda_at
from chi_monotone_transfer import chi_all_lambda
from mass_at_3A_proper import atom_braid_word_3A
from lr_coefficients import partitions_of
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

# --- muon anchor: READ, never retyped ---------------------------------------
# This file used to carry the muon q0 as a string literal. A transcribed pin
# cannot be re-pinned, cannot be flipped by QOU_Q0_ANCHOR, and reports a
# q0Anchor describing its label rather than its computation. The literal here
# was B = Vol(4_1)/206.7682830, the CODATA-2018 derivation -- superseded by the
# owner ruling of 2026-08-22 (A -> CODATA 2022, PR #5500). Reading the anchor
# is correct before and after that ruling; retyping either value is not.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[1]
                        / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor as _q0_for  # noqa: E402

set_compute_dps()
N_STRANDS = 6           # deuteron: 3A = 3·2
B_D_OVER_ME = mp.mpf("4.353")   # −B(D)/m_e target (gating-context canonical)
Q0 = mp.mpf(_q0_for("muon"))   # substrate q₀ (matches y-lambda witness hot path)


def transpose(lam):
    if not lam:
        return ()
    m = lam[0]
    return tuple(sum(1 for p in lam if p > j) for j in range(m))


def main():
    print(f"deuteron (Z=1,N=1), n={N_STRANDS}, dps={mp.mp.dps}\n")
    parts = [tuple(p) for p in partitions_of(N_STRANDS)]

    # y_λ at canonical q₀ (q_val=None ⇒ canonical pin)
    print("[1/2] computing y_λ (Markov weights, q₀ witness hot path) ...", flush=True)
    yraw = y_lambda_at(N_STRANDS, Q0)   # pass q₀ ⇒ precomputed-witness hot path (sub-ms)
    # y_lambda_at returns a dict {partition: value}
    y = {tuple(k): (v if isinstance(v, mp.mpf) else mp.mpf(str(v)))
         for k, v in yraw.items()}
    # χ^λ(β_D) canonical (atom braid word, color-weighted interface, q₀)
    print("[2/2] computing χ^λ(β_D) via canonical chi_all_lambda (H₆, may take a few min) ...", flush=True)
    chi = chi_all_lambda(atom_braid_word_3A(1, 1), N_STRANDS, dps=mp.mp.dps)
    print("    ... χ^λ done.\n", flush=True)
    chi = {tuple(k): v for k, v in chi.items()}

    # --- (i) flat baseline: tr_M(β_D) = Σ_λ y_λ χ^λ  (the P_λ≡1 point) ---
    print("Per-λ flat-trace weights w_λ = y_λ·χ^λ(β_D)  (the P_λ≡1 distribution):")
    print(f"  {'λ':<14}{'y_λ':>14}{'χ^λ(β_D)':>16}{'w_λ=y_λχ^λ':>16}{'λᵀ':>10}")
    w = {}
    for lam in parts:
        yl = y.get(lam, mp.mpf(0))
        cl = chi.get(lam, mp.mpf(0))
        wl = yl * cl
        w[lam] = wl
        print(f"  {str(lam):<14}{mp.nstr(yl,7):>14}{mp.nstr(cl,9):>16}"
              f"{mp.nstr(wl,9):>16}{str(transpose(lam)):>10}")
    # mp.fsum over the term collection avoids intermediate-rounding precision loss
    # vs a sequential `+=` accumulator (Gemini #2626). Display nstr widths are a
    # deliberate readability choice; full precision lives in the witness JSON.
    trM = mp.fsum(w.values())
    print(f"\n  tr_M(β_D) = Σ_λ w_λ = {mp.nstr(trM, 14)}   (= flat P_λ≡1 baseline, mod A(D))")
    print(f"  target −B(D)/m_e = {mp.nstr(B_D_OVER_ME,8)}")
    print(f"  ⇒ A(D) needed for flat baseline to hit target: A(D) = {mp.nstr(B_D_OVER_ME/abs(trM),8)} "
          f"(if P_λ≡1; the deviation P_λ−1 absorbs the rest once A(D) is the derived value)\n")

    # --- (ii) bar-even (λ↔λᵀ) admissibility structure ---
    self_conj = [lam for lam in parts if transpose(lam) == lam]
    seen, pairs = set(), []
    for lam in parts:
        lt = transpose(lam)
        if lam in seen or lt in seen:
            continue
        if lt != lam:
            pairs.append((lam, lt))
        seen.add(lam); seen.add(lt)
    print("Bar-even (transpose λ↔λᵀ) admissibility structure on P_λ:")
    print(f"  p({N_STRANDS}) = {len(parts)} partitions")
    print(f"  self-conjugate (λ=λᵀ): {self_conj}  ({len(self_conj)})")
    print(f"  conjugate pairs (λ,λᵀ): {pairs}  ({len(pairs)} pairs)")
    dim_even = len(self_conj) + len(pairs)
    print(f"  ⇒ bar-EVEN admissible P_λ subspace has dim {dim_even} (of {len(parts)});")
    print(f"    the binding redistribution (P_λ−1) must lie here (cbnf §4(ii)).")
    print()
    # bar-even check on the flat weights themselves: is w_λ already λ↔λᵀ-symmetric?
    print("Is the flat trace distribution w_λ itself bar-even (w_λ =? w_λᵀ)?")
    maxasym = mp.mpf(0)
    for lam, lt in pairs:
        d = abs(w[lam] - w[lt])
        maxasym = max(maxasym, d)
        print(f"  |w_{str(lam)} − w_{str(lt)}| = {mp.nstr(d,6)}")
    print(f"  max asymmetry over pairs = {mp.nstr(maxasym,6)}")
    print(f"  ⇒ {'flat trace is bar-EVEN' if maxasym < mp.mpf('1e-20') else 'flat trace is bar-MIXED (χ^λ ≠ χ^λᵀ at q₀): the bar-even P_λ must SYMMETRISE it'}")
    print("\nGAP-A-3 §4 PROBE COMPLETE (flat baseline + bar-even admissibility; no fit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
