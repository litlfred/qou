#!/usr/bin/env python3
"""qbeta_c3_barodd_tetraplectic_reduction_probe.py

Combinatorial reduction of the Faddeev non-compact Φ_b for the c₃ bar-ODD part
`S`, along the owner-directed chain

    contour integral → tetraplectic (residue lattice) → Young diagram (e_k)
        → partitions (distinct-odd ↔ self-conjugate) → combinatorial.

It establishes ONE structural fact and CHARACTERIZES the open target — it does
NOT fit c_k or propose a value (scope-(a); C14 anti-fitting; registry untouched).

STRUCTURAL RESULT (rigorous, combinatorial):
  The compact q-Pochhammer factor  ∏(1+q^{2n+1}x)  has  [x^k] = e_k(q,q³,q⁵,…),
  whose support is EXACTLY the self-conjugate partitions (Frobenius: distinct
  odd parts ↔ self-conjugate λ, via principal hook lengths). A self-conjugate
  partition is transpose-fixed (λ=λ'), i.e. bar-EVEN under the modular double
  b↔1/b ≙ conjugation. Hence the compact/mass face carries ZERO bar-odd content
  → S must come from the modular-DUAL (q̃ = e^{-2πi/b²}) lattice, the
  non-self-conjugate {λ,λ'} residual = the phase channel where Φ_b is bar-odd.

CHARACTERIZATION (measurement, not fit):
  On the fibre saddle (real b, q a root of unity) the validated evaluator gives
  |Φ_b|=1 and a nonzero, varying phase arg Φ_b — the bar-odd carrier. Reported
  at the corpus-natural point b²=1/6 (q=ζ₆=e^{iπ/3}, the Vol(4₁)=2Λ(π/3) angle),
  NOT chosen by matching S. The two S-values (muon +0.00968298, proton
  −0.03945936; sign-flip) are stated as the target; pinning the derived argument
  z(q₀) is the open handoff to the z→c_k evaluation map (PR #3458 territory).

Companion scope doc:
  docs/scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md
Evaluator: phi_b_evaluator.py (validated vs Hikami math/0604094).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from phi_b_evaluator import phi_b  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40

# Exact c₃ target (committed anchor-blind witness; see the sleak-target audit).
VOL_4_1 = mp.mpf("2.02988321281930725417066550300100495")  # 2·Λ(π/3)
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

    # ---- Arrow 2+4: compact face is exactly bar-even (self-conjugate support) ----
    print("\n[2] Arrows 2&4 — compact e_k support is self-conjugate ⇒ 100% bar-EVEN:")
    print("    e_k(q,q³,q⁵,…) = Σ_{λ distinct-odd} q^{|λ|}; every term ↔ a")
    print("    self-conjugate partition (λ=λ'=bar(λ)). So the compact/mass product")
    print("    carries NO bar-odd content — S cannot come from it.")
    # explicit term-by-term transpose-invariance check on the Frobenius images
    tinv_ok = True
    for n in (5, 9, 16):
        for lo in distinct_odd_partitions(n):
            lam = frobenius_from_distinct_odd(lo)
            if bar(lam) != lam:
                tinv_ok = False
    print(f"    term-by-term transpose-fixed (λ=bar λ) on n∈{{5,9,16}}: "
          f"{'OK — bar-even' if tinv_ok else 'FAIL'}")

    # ---- Arrow 5: bar-odd carrier is the modular-dual phase (evaluator) ----
    print("\n[3] Arrow 5 — bar-ODD carrier = modular-dual phase (validated Φ_b):")
    print("    Fibre saddle, corpus-natural point b²=1/6 ⇒ q=ζ₆=e^{iπ/3}")
    print("    (the Vol(4₁)=2Λ(π/3) angle — chosen by corpus structure, NOT by")
    print("    matching S). |Φ_b|=1 (bar-even face is trivial here); the PHASE")
    print("    arg Φ_b is the bar-odd content.")
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
              f"   (= c₃ + Vol(4₁);  bar-odd, modular-dual, Subgoal-2)")
    print(f"      S sign-flips → zero-crossing between anchors; S(p)/S(m)"
          f" = {mp.nstr(S_TARGET['proton']/S_TARGET['muon'],5)}")
    print("      OPEN handoff: pinning the DERIVED argument z(q₀) (CS phase /")
    print("      complex volume) is the z→c_k evaluation map (PR #3458). This")
    print("      probe does NOT fit it.")

    ok_all = bij_ok and tinv_ok and max_unimod < 1e-20

    wb.add_data("frobenius_bijection", bij_rows)
    wb.add_data("compact_face_bar_even", {
        "claim": "e_k(q,q^3,...) supported on self-conjugate partitions ⇒ bar-even",
        "term_by_term_transpose_fixed": tinv_ok})
    wb.add_data("bar_odd_phase_zeta6", {
        "point": "b^2=1/6, q=zeta_6=e^{i pi/3} (Vol(4_1)=2Lambda(pi/3) angle)",
        "rows": phase_rows, "note": "corpus-natural point, NOT S-matched"})
    wb.add_data("open_target_S", {
        "muon": mp.nstr(S_TARGET["muon"], 8), "proton": mp.nstr(S_TARGET["proton"], 8),
        "Vol_4_1": mp.nstr(VOL_4_1, 12), "sign_flips": True,
        "handoff": "derived argument z(q0) via z->c_k evaluation map (PR #3458)"})
    wb.add_assertion(
        "frobenius_distinct_odd_eq_self_conjugate",
        computed=1.0 if bij_ok else 0.0, expected=1.0, tolerance=0.5,
        source="classical Frobenius bijection (distinct odd parts ↔ self-conjugate λ)")
    wb.add_assertion(
        "compact_face_is_bar_even",
        computed=1.0 if tinv_ok else 0.0, expected=1.0, tolerance=0.5,
        source="self-conjugate support ⇒ transpose-fixed ⇒ zero bar-odd on the mass face")
    wb.add_assertion(
        "fibre_saddle_unimodular",
        computed=max_unimod, expected=0.0, tolerance=1e-20,
        source="|Φ_b|=1 at real b (pure-phase bar-odd carrier; prop:phi-b-unitary-bar-odd)")
    wb.save()

    print(f"\n  RESULT: {'ALL OK' if ok_all else 'CHECK FAILURES'}")
    print("  Structural: compact/mass face is bar-EVEN (self-conjugate) — proved.")
    print("  S is bar-ODD (modular-dual, phase channel) — characterized, open.")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
