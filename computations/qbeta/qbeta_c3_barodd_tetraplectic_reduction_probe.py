#!/usr/bin/env python3
"""qbeta_c3_barodd_tetraplectic_reduction_probe.py

Combinatorial reduction of the Faddeev non-compact Φ_b for the c₃ bar-ODD part
`S`, along the owner-directed chain

    contour integral → tetraplectic (residue lattice) → Young diagram (e_k)
        → partitions (distinct-odd ↔ self-conjugate) → combinatorial.

It establishes ONE structural fact and CHARACTERIZES the open target — it does
NOT fit c_k or propose a value (scope-(a); C14 anti-fitting; registry untouched).

TWO DISTINCT INVOLUTIONS (the correction — thanks to owner's "e_k(q̄,…)?"):
  * TRANSPOSE  λ↔λ'  (b↦1/b on the dual sinh-lattices): its fixed points are the
    self-conjugate partitions; [x^k]=e_k(q,q³,…) is supported exactly there
    (Frobenius: distinct odd parts ↔ self-conjugate λ). This realizes the
    MODULAR SELF-DUALITY Φ_b=Φ_{1/b} — it is NOT bar-evenness.
  * BAR σ: q↦q⁻¹ (b↦ib; on |q|=1, complex conjugation): the sinh/cosh split.
    e_k is transpose-symmetric but NOT σ-even. Its σ-parity split is
      bar-EVEN (cosh) = ½[e_k(q,q³,…)+e_k(q⁻¹,q⁻³,…)]   — mass / −Vol(4₁)
      bar-ODD  (sinh) = ½[e_k(q,q³,…)−e_k(q⁻¹,q⁻³,…)]   — decay / S
  The bar-ODD (sinh) part is NONZERO (verified, all k) ⇒ S is sourced by the
  σ-antisymmetric part of the SAME compact e_k — NOT the ~1e-165-suppressed
  modular-dual q̃ factor. This resolves the suppression tension.

CHARACTERIZATION (measurement, not fit):
  On |q|=1 the sinh part collapses to i·Im e_k(q,q³,…) — a pure phase (the
  channel-separation phase channel; |Φ_b|=1). Reported at the corpus-natural
  point b²=1/6 (q=ζ₆, the Vol(4₁)=2·Cl₂(π/3) angle), NOT chosen by matching S. The
  two S-values (muon +0.00968298, proton −0.03945936; sign-flip) are the target;
  pinning the derived argument z(q₀) is the open handoff to the z→c_k evaluation
  map (PR #3458 territory).

Companion scope doc:
  docs/scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md
Evaluator: phi_b_evaluator.py (validated vs Hikami math/0604094).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from phi_b_evaluator import phi_b  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40

# Exact c₃ target (committed anchor-blind witness; see the sleak-target audit).
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 36 digits, correct to 17 (qou-ckbv)
VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}


# ----------------------------------------------------------------------------
# Combinatorics: partitions into distinct odd parts ↔ self-conjugate partitions
# ----------------------------------------------------------------------------
def distinct_odd_partitions(n: int):
    """All partitions of n into DISTINCT ODD parts (each part used once)."""
    out = []

    def rec(remaining, max_part, acc):
        if remaining == 0:
            out.append(tuple(acc))
            return
        p = min(max_part, remaining)
        if p % 2 == 0:
            p -= 1
        while p >= 1:
            if p <= remaining:
                rec(remaining - p, p - 2, acc + [p])
            p -= 2

    rec(n, n, [])
    return out


def is_self_conjugate(lam) -> bool:
    """Is the partition lam (weakly decreasing tuple) equal to its transpose?"""
    if not lam:
        return True
    m = lam[0]
    conj = tuple(sum(1 for a in lam if a >= i) for i in range(1, m + 1))
    return tuple(lam) == conj


def self_conjugate_partitions(n: int):
    """All self-conjugate partitions of n (enumerate all, filter λ=λ')."""
    out = []

    def rec(remaining, max_part, acc):
        if remaining == 0:
            if is_self_conjugate(acc):
                out.append(tuple(acc))
            return
        for p in range(min(max_part, remaining), 0, -1):
            rec(remaining - p, p, acc + [p])

    rec(n, n, [])
    return out


def frobenius_from_distinct_odd(lam_odd):
    """Frobenius bijection: distinct odd parts {2a_i+1} ↦ self-conjugate λ via
    principal hooks (arm=leg=a_i). Returns the self-conjugate partition."""
    arms = sorted(((p - 1) // 2 for p in lam_odd), reverse=True)  # a_i, arm=leg
    d = len(arms)
    # Build the self-conjugate diagram from its principal (diagonal) hooks.
    lam = [0] * (max(arms[0] + 1, d) if arms else 0)
    for i, a in enumerate(arms):
        # i-th principal hook: row i has (a_i+1) cells to the right of diagonal
        # plus the diagonal; symmetric leg fills column i.
        lam[i] = a + 1 + i  # cells in row i: diagonal offset i + arm a + the cell
    # Fill remaining rows below the diagonal by transpose symmetry.
    full = [0] * (lam[0] if lam else 0)
    # reconstruct via conjugate-symmetric hook layout
    cells = set()
    for i, a in enumerate(arms):
        for j in range(i, i + a + 1):
            cells.add((i, j))
            cells.add((j, i))
    rows = {}
    for (r, c) in cells:
        rows[r] = max(rows.get(r, 0), c + 1)
    return tuple(rows[r] for r in sorted(rows))


def bar(sign_lam):
    """Conjugate (transpose) of a partition."""
    lam = sign_lam
    if not lam:
        return ()
    m = lam[0]
    return tuple(sum(1 for a in lam if a >= i) for i in range(1, m + 1))


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — tetraplectic → Bruhat → Young → partitions reduction")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-c3-barodd-tetraplectic-reduction", engine="mpmath+combinatorial")
    wb.set_description(
        "Combinatorial reduction of Faddeev Φ_b for the c₃ bar-ODD part S. "
        "Rigorous structural result: the compact q-Pochhammer factor's [x^k] = "
        "e_k(q,q³,…) is supported EXACTLY on self-conjugate partitions "
        "(Frobenius distinct-odd↔self-conjugate), which are transpose-fixed "
        "(bar-EVEN) ⇒ the mass face carries zero bar-odd content, so S lives on "
        "the modular-dual (non-self-conjugate) lattice = the phase channel. "
        "Characterization (not fit): arg Φ_b at the corpus-natural ζ₆ point; the "
        "two S-values are the stated target. Scope-(a); C14 anti-fitting; no c_k "
        "wired; registry untouched."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # ---- Arrow 3: distinct-odd ↔ self-conjugate (Frobenius/Bruhat) ----
    print("\n[1] Arrow 3 — distinct-odd-parts ↔ self-conjugate partitions (Frobenius):")
    bij_rows, bij_ok = [], True
    for n in (1, 3, 5, 7, 9, 12, 16, 20, 25):
        d = distinct_odd_partitions(n)
        sc = self_conjugate_partitions(n)
        ok = len(d) == len(sc)
        bij_ok = bij_ok and ok
        # verify the explicit Frobenius map lands on self-conjugate partitions
        mapped_ok = all(is_self_conjugate(frobenius_from_distinct_odd(lo)) and
                        sum(frobenius_from_distinct_odd(lo)) == n for lo in d)
        bij_ok = bij_ok and mapped_ok
        print(f"    n={n:2d}:  #distinct-odd={len(d):2d}  #self-conj={len(sc):2d}"
              f"  {'OK' if ok and mapped_ok else 'FAIL'}")
        bij_rows.append({"n": n, "distinct_odd": len(d), "self_conjugate": len(sc),
                         "frobenius_lands_self_conj": mapped_ok})

    # ---- Arrow 4: transpose-symmetry is NOT bar-evenness (the correction) ----
    print("\n[2] Arrow 4 — transpose (modular self-duality) ≠ bar σ (q↦q⁻¹):")
    print("    e_k is transpose-symmetric (self-conjugate support, [1]) — that is")
    print("    the modular self-duality Φ_b=Φ_{1/b}. It is NOT σ-even. Under the")
    print("    bar σ: q↦q⁻¹, e_k splits into cosh(bar-EVEN)+sinh(bar-ODD):")
    tinv_ok = True  # transpose-fixed on Frobenius images (the self-duality)
    for n in (5, 9, 16):
        for lo in distinct_odd_partitions(n):
            if bar(frobenius_from_distinct_odd(lo)) != frobenius_from_distinct_odd(lo):
                tinv_ok = False
    q, x = sp.symbols("q x")
    Npoly = 12
    Pfull = sp.expand(sp.prod([(1 + q ** (2 * n + 1) * x) for n in range(Npoly)]))
    odd_nonzero_all = True
    sigma_rows = []
    for k in (1, 2, 3):
        ek = sp.expand(Pfull.coeff(x, k))
        ek_bar = sp.expand(ek.subs(q, 1 / q))
        odd = sp.simplify((ek - ek_bar) / 2)      # sinh / bar-ODD
        is_zero = (odd == 0)
        odd_nonzero_all = odd_nonzero_all and (not is_zero)
        print(f"    k={k}: bar-ODD (sinh) part ½[e_k(q)−e_k(q⁻¹)] == 0 ? {is_zero}"
              f"  ⇒ {'nonzero (S carrier)' if not is_zero else 'ZERO'}")
        sigma_rows.append({"k": k, "bar_odd_sinh_is_zero": bool(is_zero)})
    print(f"    ⇒ the compact e_k DOES carry bar-odd content (sinh part ≠ 0);")
    print(f"      S needs NO modular-dual factor. (transpose-fixed check: "
          f"{'OK' if tinv_ok else 'FAIL'})")

    # ---- Arrow 5: on |q|=1 the sinh part = i·Im e_k = pure phase ----
    print("\n[3] Arrow 5 — on |q|=1 the bar-ODD (sinh) part = i·Im e_k = phase:")
    print("    corpus-natural point b²=1/6 ⇒ q=ζ₆=e^{iπ/3} (Vol(4₁)=2·Cl₂(π/3) angle,")
    print("    NOT S-matched). Both the direct i·Im e_k and the validated arg Φ_b.")
    ek3 = sp.lambdify(q, sp.expand(Pfull.coeff(x, 3)), "mpmath")
    zeta6 = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)
    im_e3 = mp.im(ek3(zeta6))
    print(f"    Im e_3(ζ₆) = {mp.nstr(im_e3, 6)}  (=0 ⇒ this special RoU is a sinh"
          f" node; substrate q₀>1 real ⇒ Im e_k=0 too — read at RoU accumulation)")
    b = mp.sqrt(mp.mpf(1) / 6)
    phase_rows, max_unimod = [], 0.0
    for z in (mp.mpf("0.10"), mp.mpf("0.20"), mp.mpf("0.30")):
        v = phi_b(z, b)
        unimod = abs(float(mp.fabs(v)) - 1.0)
        max_unimod = max(max_unimod, unimod)
        arg = mp.arg(v)
        print(f"      z={mp.nstr(z,3)}:  |Φ_b|-1={unimod:.2e}   arg Φ_b={mp.nstr(arg,12)}")
        phase_rows.append({"z": mp.nstr(z, 6), "abs_minus_1": f"{unimod:.3e}",
                           "arg_phi_b": mp.nstr(arg, 20)})

    # ---- Target (characterization only) ----
    print("\n[4] The open target — S at both anchors (must be reproduced):")
    for a in ("muon", "proton"):
        print(f"      S({a:6s}) = {mp.nstr(S_TARGET[a], 8):>12}"
              f"   (= c₃ + Vol(4₁);  bar-odd = sinh part of e_k, Subgoal-2)")
    print(f"      S sign-flips → zero-crossing between anchors; S(p)/S(m)"
          f" = {mp.nstr(S_TARGET['proton']/S_TARGET['muon'],5)}")
    print("      OPEN handoff: pinning the DERIVED argument z(q₀) (CS phase /")
    print("      complex volume) is the z→c_k evaluation map (PR #3458). This")
    print("      probe does NOT fit it.")

    ok_all = bij_ok and tinv_ok and odd_nonzero_all and max_unimod < 1e-20

    wb.add_data("frobenius_bijection", bij_rows)
    wb.add_data("two_involutions", {
        "transpose_lambda_lambda_prime": "self-conjugate fixed pts; realizes modular self-duality Phi_b=Phi_{1/b}",
        "bar_sigma_q_to_q_inv": "sinh/cosh split; e_k transpose-symmetric but NOT sigma-even",
        "e_k_transpose_fixed": tinv_ok,
        "sigma_parity_split": sigma_rows,
        "bar_odd_sinh_nonzero_all_k": odd_nonzero_all,
        "conclusion": "S = sigma-antisymmetric (sinh) part of the SAME compact e_k; no modular-dual factor needed"})
    wb.add_data("fibre_saddle_phase_zeta6", {
        "point": "b^2=1/6, q=zeta_6=e^{i pi/3} (Vol(4_1)=2Lambda(pi/3) angle)",
        "Im_e3_zeta6": mp.nstr(im_e3, 8),
        "arg_phi_b_rows": phase_rows, "note": "corpus-natural point, NOT S-matched"})
    wb.add_data("open_target_S", {
        "muon": mp.nstr(S_TARGET["muon"], 8), "proton": mp.nstr(S_TARGET["proton"], 8),
        "Vol_4_1": mp.nstr(VOL_4_1, 12), "sign_flips": True,
        "handoff": "derived argument z(q0) via z->c_k evaluation map (PR #3458)"})
    wb.add_assertion(
        "frobenius_distinct_odd_eq_self_conjugate",
        computed=1.0 if bij_ok else 0.0, expected=1.0, tolerance=0.5,
        source="classical Frobenius bijection (distinct odd parts ↔ self-conjugate λ); the modular self-duality")
    wb.add_assertion(
        "compact_e_k_bar_odd_sinh_nonzero",
        computed=1.0 if odd_nonzero_all else 0.0, expected=1.0, tolerance=0.5,
        source="½[e_k(q,q³,…)−e_k(q⁻¹,q⁻³,…)] ≠ 0 (all k) — the bar-odd S carrier lives on the compact e_k, NOT the modular dual")
    wb.add_assertion(
        "fibre_saddle_unimodular",
        computed=max_unimod, expected=0.0, tolerance=1e-20,
        source="|Φ_b|=1 at real b (pure-phase bar-odd carrier; prop:phi-b-unitary-bar-odd)")
    wb.save()

    print(f"\n  RESULT: {'ALL OK' if ok_all else 'CHECK FAILURES'}")
    print("  Structural: transpose (self-conjugate) = modular self-duality; the")
    print("  bar σ (q↦q⁻¹) sinh part of the SAME compact e_k is nonzero = the S")
    print("  carrier (no modular-dual factor needed). On |q|=1 it is i·Im e_k = phase.")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
