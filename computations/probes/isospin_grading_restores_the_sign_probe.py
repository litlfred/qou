#!/usr/bin/env python3
"""Grading by `(T,S)` instead of flavour makes the two-nucleon sign pattern
REACHABLE — with no flavour grading at all — but forces the two channels into
exact mirror symmetry, where nature is `33.7x` asymmetric.

WHAT THIS TESTS
---------------
`two_nucleon_pattern_is_unreachable_probe` (bean `qou-v3u2`) proved that a
single-crossing bond with a **flavour-assigned** offset `d` cannot reproduce the
physical bound/unbound pattern: `mu(d) = z + d` is affine, so `{d : mu > 1}` is
a half-line and cannot contain both endpoints of `[-h, 0]` while excluding an
interior point. It named escape **(b)**: grade by `(T, S)`, selecting a different
*operator* per channel rather than a different offset. This runs that escape.

THE IDENTIFICATION IS FORCED BY PAULI, NOT FITTED
-------------------------------------------------
Two nucleons must have a totally antisymmetric wavefunction. In `1S0`
(spin-singlet, spatially symmetric) the isospin part must be **symmetric**, so
`T = 1`; in `3S1` (spin-triplet, spatially symmetric) it must be
**antisymmetric**, so `T = 0`. The two-strand Hecke algebra has exactly two
Wedderburn blocks — the symmetric `(2)` and the antisymmetric `(1,1)`, both
one-dimensional. The identification

    (2)    <->  T = 1   (1S0)     pp, nn, np-singlet
    (1,1)  <->  T = 0   (3S1)     np only

is therefore the only one available, and it is fixed by exchange symmetry rather
than chosen to fit anything.

WHAT THE BLOCKS GIVE
--------------------
The Hecke generator's eigenvalues are `+q` and `-1/q` (verified here against
`build_seminormal_matrices`), so a crossing `(1, d)` acts as `eig + d`:

    beta   d            mu_sym = q+d   |mu|      T=1      mu_anti = -1/q+d  |mu|      T=0
    0      0.000000     1.10997858     1.10998   UNBOUND  -0.90091828       0.90092   BOUND
    1/2   -0.10453015   1.00544843     1.00545   UNBOUND  -1.00544843       1.00545   unbound
    1     -0.20906030   0.90091828     0.90092   bound    -1.10997858       1.10998   unbound

**At `beta = 0` — a pure `sigma` crossing, with no flavour grading whatsoever —
the pattern is exactly right:** every `T = 1` state unbound (which is all of
`pp`, `nn`, *and* the `np` singlet), and the single `T = 0` state bound. The two
Wedderburn blocks do all of the work that flavour-assigned offsets could not do
at all.

THE WINDOW, IN CLOSED FORM
--------------------------
    T=1 unbound   <=>  |q + d| > 1      <=>  beta < q/(q+1) = 0.526061540067
    T=0 bound     <=>  |-1/q + d| < 1   <=>  beta < 1/(q+1) = 0.473938459933
    both          <=>  beta in [0, 1/(q+1))

The two thresholds are complementary — `q/(q+1) + 1/(q+1) = 1` exactly — and the
`T = 0` condition is the binding one. Two consequences:

* `1/(q+1) < 1/2` for **every** `q > 1`, so the unoriented average `beta = 1/2`
  can never sit inside the window, at any substrate;
* production's `beta_pn = 0.499656072298` misses it by `0.025717612`.

AND THE LIMIT: THE CHANNELS ARE FORCED INTO MIRROR SYMMETRY
-----------------------------------------------------------
Reachable is not the same as right. Writing `L = -log|mu|`, the asymmetry the
construction can produce between the bound and unbound channels is bounded:

    beta        L(T=0) bound     -L(T=1) unbound     ratio
    0           0.10434072       0.10434072          1.0000   <- maximum
    0.10        0.08140062       0.08532647          0.9540
    0.25        0.04794799       0.05610951          0.8545
    0.40        0.01557831       0.02601317          0.5989
    ->beta*     -> 0             0.01181758          -> 0

**The ratio is capped at exactly `1`, attained only at `beta = 0`, where both
channels equal `log q` precisely.** The single point that gets both signs right
is the point of exact mirror symmetry. Nature is not remotely symmetric:

    deuteron (3S1, T=0)        bound     2.224566 MeV
    np virtual state (1S0)     unbound   ~0.066 MeV
    experimental ratio                   33.7

so the construction is short by `33.7x` on a quantity it **cannot exceed 1** on.
That conclusion is robust to the virtual-state energy: at half or double the
quoted `66 keV` the ratio is `67.4` or `16.9`, both far outside `[0, 1]`.

Magnitudes, for completeness and with the usual caveat that this arc's absolute
scales are unreliable: `alpha log q = 0.43676831 MeV` against a deuteron of
`2.224566` (`5.09x` low) and against a `1S0` virtual state of `0.066` (`6.62x`
high) — the same number for both, which is the mirror symmetry restated.

VERDICT: NECESSARY, NOT SUFFICIENT
----------------------------------
This is real progress and should not be oversold. `qou-v3u2` proved the flavour
grading makes the sign pattern **impossible**; the `(T,S)` grading makes it
**reachable**, using structure (the two Wedderburn blocks) that already exists
and that nothing in the construction currently uses. That removes an
obstruction. It does not close the gap: the residual failure is a forced
degeneracy between the two channels, which is a different and quite specific
problem from the one it replaces.

DISCIPLINE
----------
No fit; nothing wired. The block eigenvalues are verified against
`build_seminormal_matrices` rather than assumed. The `T`/`S` assignment is fixed
by Pauli, not tuned. Experimental values are comparison targets only and the
`33.7x` conclusion is shown robust to the least certain of them.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] two_nucleon_pattern_is_unreachable_probe.py (escape (b) named there)
-- Ref: [data] CD-Bonn NN scattering lengths, Machleidt nucl-th/0006014 Tbl. XI
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    M_E_MEV as _ME  # noqa: E402,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from pyhecke.constants import pn_interface_offset  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
# `D_PN` is bound at `pyhecke.atom` import from `pyhecke.gram.q0`, which is a
# Python FLOAT -- so the module constant carries 2.0e-16 relative error and
# `mp.mpf(str(D_PN))` would read that as exact at this file's dps. Recompute
# the same `pn_interface_offset` at the working precision instead.
_D = pn_interface_offset(q_at(mp.mp.dps))
_MEM = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
ALPHA = _qbeta_e0.order_zero_scaled(_MEM, _Q)
B_DEUT = AME_B_DEUTERON_MEV_VALIDATION        # AME
B_VIRT = mp.mpf("0.066")           # np 1S0 virtual state, ~66 keV (approximate)


def main() -> int:
    assertions = []
    print("t7qv — does an isospin grading restore the two-nucleon sign?")

    # ── A1. the two-strand algebra has exactly the two channels needed ─
    print("\n  1. the identification is forced by Pauli, not fitted")
    mats = {lam: build_seminormal_matrices(list(lam))[0]
            for lam in ((2,), (1, 1))}
    dims = {lam: np.asarray(m[0], dtype=float).shape[0]
            for lam, m in mats.items()}
    print(f"     two-nucleon wavefunction must be totally antisymmetric:")
    print(f"       1S0 spin-singlet, spatially symmetric -> isospin SYMMETRIC "
          f"-> T=1")
    print(f"       3S1 spin-triplet, spatially symmetric -> isospin ANTISYM  "
          f"-> T=0")
    print(f"     the 2-strand Hecke algebra has exactly {len(mats)} Wedderburn "
          f"blocks, dims {dims}")
    print(f"       (2)   <-> T=1 (1S0)   pp, nn, np-singlet")
    print(f"       (1,1) <-> T=0 (3S1)   np only (Pauli forbids it for pp, nn)")
    ok = set(dims) == {(2,), (1, 1)} and set(dims.values()) == {1}
    assertions.append(("A1_two_blocks_match_the_two_isospin_channels", ok,
                       f"blocks {sorted(dims)} with dims {sorted(dims.values())}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. block eigenvalues are +q and -1/q ──────────────────────────
    print("\n  2. block eigenvalues, verified against the seminormal build")
    ev = {}
    for lam, m in mats.items():
        M = np.asarray(m[0], dtype=float)
        ev[lam] = float(np.linalg.eigvals(M)[0].real)
        print(f"     lambda={str(lam):<7s} T_0 -> {ev[lam]:+.14f}")
    d_sym = abs(ev[(2,)] - float(_Q))
    d_ant = abs(ev[(1, 1)] - float(-1 / _Q))
    print(f"     analytic  +q = {float(_Q):+.14f}   -1/q = {float(-1 / _Q):+.14f}")
    print(f"     agreement {d_sym:.2e} / {d_ant:.2e}")
    ok = d_sym < 1e-12 and d_ant < 1e-12
    assertions.append(("A2_block_eigenvalues_are_q_and_minus_inverse_q", ok,
                       f"sym matches +q to {d_sym:.1e}, antisym matches -1/q "
                       f"to {d_ant:.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the ungraded crossing reproduces the pattern ───────────────
    print("\n  3. beta = 0, NO flavour grading: does the pattern come out?")

    def chan(b):
        d = -b * _H
        return _Q + d, -1 / _Q + d

    print(f"     {'beta':<10s} {'d':>13s} {'|mu| sym':>10s} {'T=1':>9s} "
          f"{'|mu| anti':>10s} {'T=0':>9s}")
    rows = {}
    for lbl, b in (("0 (sigma)", mp.mpf(0)), ("1/2 (avg)", mp.mpf(1) / 2),
                   ("pn prod", -_D / _H), ("1 (inv)", mp.mpf(1))):
        ms, ma = chan(b)
        t1 = "UNBOUND" if abs(ms) > 1 else "bound"
        t0 = "BOUND" if abs(ma) < 1 else "unbound"
        rows[lbl] = (b, abs(ms), t1, abs(ma), t0)
        print(f"     {lbl:<10s} {float(-b * _H):13.8f} {float(abs(ms)):10.5f} "
              f"{t1:>9s} {float(abs(ma)):10.5f} {t0:>9s}")
    ms0, ma0 = chan(mp.mpf(0))
    ok = abs(ms0) > 1 and abs(ma0) < 1
    print(f"     at beta = 0 the T=1 channel is UNBOUND (|mu| = q = "
          f"{float(abs(ms0)):.5f}) and the")
    print(f"     T=0 channel is BOUND (|mu| = 1/q = {float(abs(ma0)):.5f}) — "
          f"exactly the physical")
    print(f"     pattern, from a crossing carrying NO flavour information at all.")
    print(f"     The two Wedderburn blocks do what flavour-assigned offsets")
    print(f"     provably could not do (qou-v3u2).")
    assertions.append(("A3_ungraded_crossing_gives_the_physical_pattern", ok,
                       f"beta=0: T=1 |mu| = {float(abs(ms0)):.6f} > 1 unbound, "
                       f"T=0 |mu| = {float(abs(ma0)):.6f} < 1 bound"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. the window, in closed form ─────────────────────────────────
    print("\n  4. the window of beta that works, in closed form")
    b_sym, b_ant = _Q / (_Q + 1), 1 / (_Q + 1)
    num_sym, num_ant = (_Q - 1) / _H, (1 - 1 / _Q) / _H
    b_pn = -_D / _H
    print(f"     T=1 unbound <=> beta < (q-1)/h   = {float(num_sym):.12f} "
          f"= q/(q+1) = {float(b_sym):.12f}")
    print(f"     T=0 bound   <=> beta < (1-1/q)/h = {float(num_ant):.12f} "
          f"= 1/(q+1) = {float(b_ant):.12f}")
    print(f"     both        <=> beta in [0, 1/(q+1))")
    print(f"     thresholds are complementary: q/(q+1) + 1/(q+1) = "
          f"{float(b_sym + b_ant):.12f}")
    print(f"     1/(q+1) < 1/2 for EVERY q > 1, so the unoriented average")
    print(f"     beta = 1/2 can never sit inside the window, at any substrate.")
    print(f"     production beta_pn = {float(b_pn):.12f} misses by "
          f"{float(b_pn - b_ant):.9f}")
    ok = (abs(num_sym - b_sym) < mp.mpf("1e-30")
          and abs(num_ant - b_ant) < mp.mpf("1e-30")
          and abs(b_sym + b_ant - 1) < mp.mpf("1e-30")
          and b_ant < mp.mpf("0.5") and b_pn > b_ant)
    assertions.append(("A4_window_is_beta_below_one_over_q_plus_one", ok,
                       f"window [0, {float(b_ant):.12f}); thresholds sum to "
                       f"{float(b_sym + b_ant):.6f}; beta_pn misses by "
                       f"{float(b_pn - b_ant):.6f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. the achievable asymmetry is capped at 1 ────────────────────
    print("\n  5. but the two channels are forced into mirror symmetry")
    print(f"     {'beta':>10s} {'L(T=0) bound':>14s} {'-L(T=1) unbound':>16s} "
          f"{'ratio':>9s}")
    ratios = []
    for b in (mp.mpf(0), mp.mpf("0.10"), mp.mpf("0.25"), mp.mpf("0.40"),
              b_ant * mp.mpf("0.99")):
        ms, ma = chan(b)
        L0, L1 = -mp.log(abs(ma)), -mp.log(abs(ms))
        r = L0 / (-L1)
        ratios.append(float(r))
        print(f"     {float(b):10.6f} {float(L0):14.8f} {float(-L1):16.8f} "
              f"{float(r):9.6f}")
    lq = mp.log(_Q)
    ms0, ma0 = chan(mp.mpf(0))
    exact = abs((-mp.log(abs(ma0))) - lq) + abs((mp.log(abs(ms0))) - lq)
    ok = max(ratios) <= 1 + 1e-12 and abs(ratios[0] - 1) < 1e-12 and exact < 1e-30
    print(f"     at beta = 0 both channels equal log q = {float(lq):.12f} "
          f"EXACTLY (residual {float(exact):.1e})")
    print(f"     the ratio is capped at 1 and attained ONLY there — the single")
    print(f"     point that gets both signs right is the point of exact mirror")
    print(f"     symmetry, and the ratio falls monotonically to 0 across the window.")
    assertions.append(("A5_channel_asymmetry_is_capped_at_one", ok,
                       f"max ratio {max(ratios):.9f} at beta=0 where both "
                       f"channels are log q to {float(exact):.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. nature is 33.7x asymmetric ─────────────────────────────────
    print("\n  6. against experiment — necessary, not sufficient")
    r_exp = B_DEUT / B_VIRT
    print(f"     deuteron (3S1, T=0)     bound    {float(B_DEUT):.6f} MeV")
    print(f"     np virtual state (1S0)  unbound  ~{float(B_VIRT):.3f} MeV")
    print(f"     experimental ratio               {float(r_exp):.4f}")
    print(f"     model ratio range                [0, 1]")
    print(f"     => short by {float(r_exp):.4f}x on a quantity capped at 1")
    rob = [float(B_DEUT / (B_VIRT * f)) for f in (mp.mpf("0.5"), mp.mpf(2))]
    print(f"     robust to the virtual-state energy: at half/double 66 keV the")
    print(f"     ratio is {rob[0]:.1f} / {rob[1]:.1f}, both far outside [0, 1]")
    md = ALPHA * lq
    print(f"     magnitudes: alpha log q = {float(md):.8f} MeV for BOTH channels")
    print(f"       vs deuteron {float(B_DEUT):.6f}  ({float(B_DEUT / md):.4f}x low)")
    print(f"       vs 1S0      {float(B_VIRT):.6f}  ({float(md / B_VIRT):.4f}x high)")
    ok = r_exp > 1 and min(rob) > 1 and float(max(ratios)) <= 1 + 1e-12
    assertions.append(("A6_nature_is_asymmetric_beyond_the_models_cap", ok,
                       f"experimental ratio {float(r_exp):.4f} vs model cap 1; "
                       f"robust {rob[0]:.1f}..{rob[1]:.1f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Escape (b) works, and it should not be oversold. Grading by (T,S)")
    print("  instead of flavour makes the two-nucleon sign pattern REACHABLE —")
    print("  at beta = 0, a crossing carrying no flavour information at all, the")
    print("  T=1 channel is unbound and the T=0 channel is bound, exactly as")
    print("  nature has it. The structure was already sitting in the two")
    print("  Wedderburn blocks and nothing in the construction uses it. That")
    print("  removes the impossibility qou-v3u2 proved for flavour grading.")
    print("  The window is beta in [0, 1/(q+1)) in closed form, with")
    print("  complementary thresholds summing to 1; beta = 1/2 is outside it at")
    print("  every substrate, and production's beta_pn misses by 0.0257.")
    print("  What it does NOT fix: the achievable asymmetry between the two")
    print("  channels is capped at exactly 1, attained only at beta = 0 where")
    print("  both equal log q. Nature's ratio is 33.7. So the failure changes")
    print("  character — from an impossible sign pattern to a forced")
    print("  degeneracy — rather than going away.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Runs escape (b) named by qou-v3u2: grade the two-nucleon bond by "
            "(T,S) rather than flavour. The identification is forced by Pauli — "
            "1S0 needs symmetric isospin (T=1), 3S1 needs antisymmetric (T=0) — "
            "and the two-strand Hecke algebra has exactly two one-dimensional "
            "Wedderburn blocks, symmetric (2) and antisymmetric (1,1), with "
            "eigenvalues +q and -1/q verified against build_seminormal_matrices. "
            "RESULT: at beta = 0, a pure sigma crossing carrying NO flavour "
            "information, |mu| = q = 1.10998 > 1 in the T=1 block (unbound: pp, "
            "nn and the np singlet) and |mu| = 1/q = 0.90092 < 1 in the T=0 "
            "block (bound: the deuteron). That is exactly the physical pattern, "
            "which qou-v3u2 proved a flavour-assigned offset cannot produce at "
            "all. The window is beta in [0, 1/(q+1)) = [0, 0.473938459933) in "
            "closed form, with complementary thresholds q/(q+1) + 1/(q+1) = 1 "
            "exactly; 1/(q+1) < 1/2 for every q > 1 so the unoriented average is "
            "always outside, and production's beta_pn = 0.499656 misses by "
            "0.025718. THE LIMIT: the achievable asymmetry between the bound and "
            "unbound channels, |L(T=0)|/|L(T=1)|, is capped at exactly 1 and "
            "attained only at beta = 0, where both channels equal log q "
            "precisely — the one point with both signs right is the point of "
            "exact mirror symmetry. Nature's ratio is 2.224566/0.066 = 33.7, "
            "robust to the virtual-state energy (17 to 67 at half/double). So "
            "escape (b) is necessary and not sufficient: it removes an "
            "impossibility and replaces it with a forced degeneracy.")
        wb.add_data("blocks",
                    {str(lam): {"dim": dims[lam],
                                "eigenvalue": f"{ev[lam]:+.14f}",
                                "isospin": "T=1 (1S0)" if lam == (2,)
                                else "T=0 (3S1)"} for lam in mats})
        wb.add_data("channels_by_beta",
                    {k: {"beta": mp.nstr(v[0], 12),
                         "abs_mu_sym": mp.nstr(v[1], 12), "T1": v[2],
                         "abs_mu_anti": mp.nstr(v[3], 12), "T0": v[4]}
                     for k, v in rows.items()})
        wb.add_data("window",
                    {"T1_threshold_q_over_q_plus_1": mp.nstr(b_sym, 15),
                     "T0_threshold_1_over_q_plus_1": mp.nstr(b_ant, 15),
                     "thresholds_sum": mp.nstr(b_sym + b_ant, 6),
                     "beta_pn_production": mp.nstr(b_pn, 15),
                     "beta_pn_miss": mp.nstr(b_pn - b_ant, 12)})
        wb.add_data("asymmetry_cap",
                    {"max_ratio": f"{max(ratios):.12f}",
                     "attained_at_beta": "0",
                     "both_channels_equal_log_q": mp.nstr(lq, 15),
                     "experimental_ratio": mp.nstr(r_exp, 8),
                     "robustness_half_double": [f"{rob[0]:.4f}", f"{rob[1]:.4f}"]})
        wb.add_data("magnitudes",
                    {"alpha_log_q_MeV": mp.nstr(md, 10),
                     "deuteron_MeV": mp.nstr(B_DEUT, 8),
                     "factor_low_vs_deuteron": mp.nstr(B_DEUT / md, 6),
                     "virtual_state_MeV": mp.nstr(B_VIRT, 4),
                     "factor_high_vs_1S0": mp.nstr(md / B_VIRT, 6)})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "'BOUND' IS READ AS |mu| < 1. The antisymmetric block's eigenvalue "
            "is NEGATIVE (-1/q), so the ratio there is negative and -log(mu) is "
            "undefined; the magnitude is used instead. That is defensible "
            "because the sign is fixed by WHICH Hecke eigenvalue the block "
            "carries (+q vs -1/q) and is not an energy sign — but it IS a "
            "convention, it is doing real work in this result, and it should be "
            "stated wherever the result is quoted. Under a convention that "
            "treats a negative ratio as unphysical rather than as a magnitude, "
            "the T=0 channel has no binding reading at all and this escape does "
            "not run.")
        wb.add_caveat(
            "THIS IS AT THE n=2 INTERFACE, NOT THE FULL CONSTRUCTION. It treats "
            "each nucleon as one strand, where the corpus's atom words give "
            "each nucleon three. The survey position is that the n=2 interface "
            "version stands (mu+/mu- ARE the n=2 Wedderburn weights) while the "
            "H_6-level conjugation argument does not. Lifting the (T,S) grading "
            "into the 3-strands-per-nucleon construction is NOT done here and "
            "is where this would have to be tested next.")
        wb.add_caveat(
            "NECESSARY, NOT SUFFICIENT — do not read this as the nuclear sector "
            "being fixed. It removes the impossibility proved in qou-v3u2 and "
            "replaces it with a forced degeneracy: the model cannot make the "
            "bound channel more than equally strong to the unbound one, where "
            "nature is 33.7x asymmetric. No magnitude is claimed; alpha log q = "
            "0.4368 MeV is 5.09x low against the deuteron and 6.62x high "
            "against the 1S0 virtual state, being the same number for both.")
        wb.add_caveat(
            "The np 1S0 virtual-state energy ~66 keV is the least certain input "
            "here and is quoted approximately. The conclusion is shown robust "
            "to it: at half or double that value the experimental ratio is 17 "
            "or 67, both far outside the model's achievable [0, 1].")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
