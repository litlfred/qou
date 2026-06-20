#!/usr/bin/env python3
"""
Keystone q-deformed shift — first structural crack via the canonical H3 -> H5 lift.

Context
-------
The functor-resolution doc (2026-06-13-s5-so3-fiber-action-functor-resolution.md)
§4 step 2 asks for "the precise algebraic shift in the H_3(q) Markov trace induced
by evaluating the knot through the ell=2 (E_{(3,2)}, muon) projector versus the
ell=1 (E_{(3,1,1)}, electron) projector", to test whether it resolves the 210 ppb
muon mass tension (GAP-A-4 operator-valued branching).

A standing objection was "which H_5 braid is the muon?" (PR #2511 flagged this as
an open structural input). This script records the resolution of that objection,
due to the owner's observation that the Bring/color structure already supplies a
canonical S_3 -> S_5 embedding (the 3 Borromean color strands sitting inside the 5
Bring coordinates, fixing 2). That embedding induces the STANDARD Hecke inclusion

    H_3 = <sigma_1, sigma_2>  ↪  H_5 = <sigma_1, sigma_2, sigma_3, sigma_4>,

so the Borromean braid  beta = (sigma_1^{-1} sigma_2)^3  lifts canonically to B_5
with strands 4,5 idle. No fit: the lifted braid is forced.

This canonical lift also SIDESTEPS the 2026-06-02 nonexistence theorem
(2026-06-02-h5-h3-functor-keystone.md). That theorem only blocked choosing a
distinguished BASIS VECTOR inside the multiplicity-2 space Hom(fiber, (2,1)).
The block-projector trace  tr(E_lambda . rho_5(beta))  is basis-independent: it
sums over both (2,1) copies automatically. No line is ever chosen.

What this script does (RAW, no tuning to 210 ppb, m_mu/m_e, h^4, or any target)
-----------------------------------------------------------------------------
1. Computes the per-block H_3(q) Borromean characters chi^mu(beta) and Markov
   weights y_mu^(3); reconstructs tr_M^(3)(beta).
2. Lifts beta to H_5 (idle strands 4,5) and computes chi^lambda(beta) and Markov
   weights y_lambda^(5) for every lambda ⊢ 5.
3. SELF-CHECK: Sum_{lambda ⊢ 5} y_lambda chi^lambda(beta) == tr_M^(3)(beta)
   (the normalized Markov trace is compatible with the inclusion H_3 ⊂ H_5:
   tr_5(x) = tr_3(x) for x carrying no sigma_3, sigma_4 — confirms the lift is
   honest, not a re-normalization).
4. Reports the operator-valued branching shift: the block-resolved contribution
   y_lambda chi^lambda for muon (3,2) vs electron (3,1,1), and their ratio.

Finding (see the companion .md): the muon/electron block ratio is O(1) (~3.07),
SEVEN orders of magnitude above the 210 ppb target. The operator-valued branching
is a leading-order generation-scale distinction, NOT an O(1e-7) residual knob.
This is positive evidence that 210 ppb is an anchor-shift artifact: there is no
natural O(1e-7) structural quantity at the keystone blocks.

Run:
    PYTHONPATH=tools/qou-substrate/python python3 \
        docs/audits/scripts/keystone_h3_h5_lift_block_shift.py
Requires: pyhecke_native wheel installed (tools/pyhecke-native), mpmath.
"""
import sys
import mpmath as mp

try:
    import pyhecke_native as ph
except ImportError:
    sys.exit("pyhecke_native not installed — build the wheel:\n"
             "  maturin build --release -m tools/pyhecke-native/Cargo.toml\n"
             "  pip install --force-reinstall "
             "tools/pyhecke-native/target/wheels/pyhecke_native-*.whl")

from qou_substrate.constants import q_at  # noqa: E402

DPS = 50
PPB_TARGET = mp.mpf("2.1e-7")  # 210 ppb muon tension (falsification reference ONLY)

# Borromean braid  beta = (sigma_1^{-1} sigma_2)^3  as (sign, generator) tuples.
# Valid verbatim in H_3 and in H_5 (uses only generators 1, 2).
BETA = [(-1, 1), (1, 2), (-1, 1), (1, 2), (-1, 1), (1, 2)]


def main() -> int:
    mp.mp.dps = DPS
    q = q_at(DPS)
    qs = mp.nstr(q, DPS - 5)
    h = q - 1 / q          # h = q - q^{-1}
    hbar = 1 - 1 / q       # hbar_q = 1 - q^{-1}

    def chi(lam):
        return mp.mpf(ph.chi_lambda_braid_mpfr(list(lam), BETA, qs, DPS))

    print("Keystone q-deformed shift — canonical H_3 -> H_5 lift (RAW)")
    print("=" * 64)
    print(f"q_0  = {mp.nstr(q, 22)}")
    print(f"h    = q - 1/q     = {mp.nstr(h, 14)}")
    print(f"hbar = 1 - 1/q     = {mp.nstr(hbar, 14)}")
    print(f"210 ppb reference  = {mp.nstr(PPB_TARGET, 6)}  (falsification only)")

    # ---- H_3: where the Borromean genuinely lives ----
    parts3 = ph.partitions_of(3)
    y3 = ph.trace_weights_n(3, q)
    print("\n--- H_3(q) per block (Borromean home) ---")
    trM3 = mp.mpf(0)
    for lam, yl in zip(parts3, y3):
        yl = mp.mpf(yl)
        c = chi(lam)
        trM3 += yl * c
        print(f"  {str(lam):10} y={mp.nstr(yl, 10):14} "
              f"chi={mp.nstr(c, 12):16} y*chi={mp.nstr(yl * c, 12)}")
    print(f"  tr_M^(3)(beta) = {mp.nstr(trM3, 18)}")

    # ---- H_5: canonical lift, strands 4,5 idle ----
    parts5 = ph.partitions_of(5)
    y5 = ph.trace_weights_n(5, q)
    print("\n--- H_5(q) lifted braid (S_3->S_5 inclusion; strands 4,5 idle) ---")
    trM5 = mp.mpf(0)
    blocks = {}
    for lam, yl in zip(parts5, y5):
        yl = mp.mpf(yl)
        c = chi(lam)
        blocks[tuple(lam)] = (yl, c)
        trM5 += yl * c
        print(f"  {str(lam):12} y={mp.nstr(yl, 10):16} "
              f"chi={mp.nstr(c, 12):16} y*chi={mp.nstr(yl * c, 12)}")

    # ---- SELF-CHECK: lift preserves the Markov trace ----
    resid = abs(trM5 - trM3)
    print(f"\n  SELF-CHECK  Sum_{{l|-5}} y_l chi^l = {mp.nstr(trM5, 18)}")
    print(f"              tr_M^(3)(beta)         = {mp.nstr(trM3, 18)}")
    print(f"              |residual|             = {mp.nstr(resid, 6)}  "
          f"(expect ~1e-16: tr_5|_{{H_3}} = tr_3; y_lambda are f64-internal)")
    # Tolerance is f64-limited: trace_weights_n returns f64-precision weights,
    # so the residual floors at ~1e-15 even though chi^lambda is full MPFR.
    lift_ok = resid < mp.mpf("1e-12")
    assert lift_ok, "lift self-check FAILED: tr_5 != tr_3"

    # ---- operator-valued branching: muon (3,2) vs electron (3,1,1) ----
    ymu, cmu = blocks[(3, 2)]
    yel, cel = blocks[(3, 1, 1)]
    cmu_w, cel_w = ymu * cmu, yel * cel
    ratio = cmu_w / cel_w
    print("\n--- operator-valued branching: muon (3,2) vs electron (3,1,1) ---")
    print(f"  muon  (3,2)   : y={mp.nstr(ymu, 12)}  chi={mp.nstr(cmu, 12)}  "
          f"y*chi={mp.nstr(cmu_w, 12)}")
    print(f"  elec  (3,1,1) : y={mp.nstr(yel, 12)}  chi={mp.nstr(cel, 12)}  "
          f"y*chi={mp.nstr(cel_w, 12)}")
    print(f"  block ratio (mu/el) y*chi = {mp.nstr(ratio, 14)}")
    print(f"  |ratio - 1|               = {mp.nstr(abs(ratio - 1), 10)}")
    orders = mp.log(abs(ratio - 1) / PPB_TARGET, 10)
    print(f"  vs 210 ppb: |ratio-1| is {mp.nstr(orders, 4)} orders of magnitude "
          f"LARGER than the target")

    # ---- verdict (RAW; no fit) ----
    print("\n--- VERDICT (RAW) ---")
    print("  * The canonical H_3->H_5 lift exists and is computable (no fit).")
    print("  * Block-resolved traces are basis-free => sidestep the 2026-06-02")
    print("    multiplicity-2 nonexistence theorem (no line chosen).")
    print(f"  * muon/electron block contribution differ by O(1) (~{mp.nstr(ratio, 4)}),")
    print("    SEVEN orders above 210 ppb => leading-order generation selector,")
    print("    NOT an O(1e-7) residual knob.")
    print("  * Positive evidence that 210 ppb is an anchor-shift artifact: no")
    print("    natural O(1e-7) structural quantity lives at the keystone blocks.")
    print("\nALL CHECKS PASS." if lift_ok else "\nSELF-CHECK FAILED.")
    return 0 if lift_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
