#!/usr/bin/env python3
"""s013 redirect (ii), sourced sub-route — does the 0th-order q-Bessel Tricomi
function C_{0,q} (Raza–Fadel–Cesarano 2025, library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf eq. 11) supply
a PARAMETER-FREE (0-dof, falsifiable) reproduction of the keystone value-map
target bwS0 = {1, [4]_q, [5]_q, [4]_q[3]_q/[2]_q} ≈ {1, 4.110, 5.220, 6.220}?

Context. #3292 grounded that the target is COMPACT SU_q(2)/Hecke quantum-
dimension data (balanced Laurent polynomials in q₀), and that the disciplined
multi-argument non-compact q-Bessel row is an unfalsifiable ≥4-dof fit *unless*
its radial arguments are fixed by a Plancherel measure — which needs the
un-uploaded Koelink–Swarttouw q-Hankel kernel. The owner then uploaded
`library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf`, which is NOT that Plancherel source (it cites Koornwinder–
Swarttouw [22] but does not contain the kernel); what it DOES give is the
entire, parameter-free 0th-order q-Bessel Tricomi series (eq. 11):

    C_{0,q}(x) = Σ_{k≥0} (−1)^k x^k / ([k]_q!)²,     0 < q < 1,

with [k]_q = (1−q^k)/(1−q) (the paper's convention; §"quick recap"). By eq. (10)
C_{0,q}(x) = q-analog of J₀(2√x), so its positive real zeros {ξ₁ < ξ₂ < …} are
FIXED by q alone (Ismail, "The zeros of basic Bessel functions", ref [15]).

That makes a genuinely 0-dof, falsifiable check constructible from the upload —
no argument tuning, no free reals. This probe evaluates every natural
parameter-free quantity of C_{0,q} at the substrate (q = q₀⁻¹, the |q|<1 image
of the categorical q₀ > 1) and asks whether ANY of them reproduces the four
compact targets within 1%:

  * the ordered positive zeros ξ_j and their normalisations ξ_j/ξ₁, √ξ_j,
    √(ξ_j/ξ₁), consecutive gaps ξ_{j+1}−ξ_j;
  * C_{0,q} evaluated at the q-integer nodes [n]_q (n = 1..5) and at n = 1..5.

Formalize-first note: #3292's FACT 1 already gives the structural prior (compact
algebraic target vs. transcendental non-compact function). This is the cheap,
decisive one-shot the discipline permits — a 0-dof falsifiable check, not a wide
search. Expected outcome is a scope-(a) refutation, now carrying an in-repo
source for the q-Bessel-Tricomi sub-route specifically.

No fit; no tuned arguments; nothing wired.

Output: keystone-qbessel-tricomi-c0q-nodes.witness.json

# Ref: [manuscript] Raza–Fadel–Cesarano, "On 2-variable q-Legendre polynomials",
#      Carpathian Math. Publ. 2025, 17(1) 14–26 (library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf), eqs. (9)–(11)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf, findroot  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Categorical substrate q₀ (muon-canonical fibre value, as used by the merged
# compact-hecke probe); the paper's 0<q<1 convention uses its inverse image.
Q0 = mpf("1.1099785955541805")
Q = 1 / Q0                       # ≈ 0.90092, the |q|<1 evaluation point


def qint_unbalanced(n, q=Q):
    """[n]_q = (1−q^n)/(1−q) — the paper's convention (0<q<1)."""
    return (1 - q ** n) / (1 - q)


def qint_balanced(n, q=Q0):
    """Balanced [n]_q at q₀>1 — the compact-character convention of the target."""
    return (q ** n - q ** (-n)) / (q - q ** (-1))


_QFACT_CACHE = None


def qfact_table(nmax, q=Q):
    """Precompute [0]_q!..[nmax]_q! once (the per-eval bottleneck otherwise)."""
    global _QFACT_CACHE
    if _QFACT_CACHE is not None and len(_QFACT_CACHE) > nmax:
        return _QFACT_CACHE
    tab = [mpf(1)]
    for k in range(1, nmax + 1):
        tab.append(tab[-1] * qint_unbalanced(k, q))
    _QFACT_CACHE = tab
    return tab


def C0q(x, q=Q, terms=140):
    """0th-order q-Bessel Tricomi, library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf eq. (11).

    ([k]_q!)² grows like ((1-q)^{-k})² ≈ 10^{2k} at q≈0.9, so the alternating
    series converges fast; 140 terms is ample for |x| ≤ 400 at 50 dps."""
    qf = qfact_table(terms, q)
    x = mpf(x)
    s = mpf(0)
    xp = mpf(1)
    for k in range(terms):
        s += (-1 if k & 1 else 1) * xp / qf[k] ** 2
        xp *= x
    return s


def positive_zeros(n_zeros=6, q=Q):
    """First n positive real zeros of C_{0,q} by sign-change bracketing + refine.

    Coarse bracket scan (step 0.25) then Newton-refine each bracket — the scan
    is the cost driver, so keep the step as large as resolves the zero spacing."""
    qfact_table(160, q)                  # warm the cache once
    zeros = []
    x, dx = mpf("0.1"), mpf("0.25")
    prev = C0q(x, q)
    xmax = mpf("400")
    while len(zeros) < n_zeros and x < xmax:
        x2 = x + dx
        cur = C0q(x2, q)
        if prev == 0 or (prev < 0) != (cur < 0):
            try:
                z = findroot(lambda t: C0q(t, q), (x + x2) / 2)
                if z > 0 and (not zeros or abs(z - zeros[-1]) > mpf("1e-6")):
                    zeros.append(z)
            except Exception:  # noqa: BLE001 — bracket refine miss: skip, keep scanning
                pass
        prev, x = cur, x2
    return zeros


def main():
    targets = {
        "(5)": mpf("1"),
        "(4,1)": qint_balanced(4),
        "(3,2)": qint_balanced(5),
        "(3,1,1)": qint_balanced(4) * qint_balanced(3) / qint_balanced(2),
    }
    tvals = list(targets.values())

    zeros = positive_zeros(6)
    z1 = zeros[0] if zeros else mpf("nan")

    # Parameter-free candidate quantities (NO free reals). The j=1
    # self-normalisations ξ₁/ξ₁ and √(ξ₁/ξ₁) are identically 1 by construction
    # (true for ANY function's first zero) — they carry no content, so they are
    # excluded from the match gate rather than allowed to spuriously "hit" the
    # trivial target [1]_q = 1.
    candidates = {}
    for j, z in enumerate(zeros, 1):
        candidates[f"zero_{j}"] = z
        candidates[f"sqrt_zero_{j}"] = mp.sqrt(z)
        if j >= 2:
            candidates[f"zero_{j}_over_zero1"] = z / z1
            candidates[f"sqrt_zero_{j}_over_zero1"] = mp.sqrt(z / z1)
    for j in range(1, len(zeros)):
        candidates[f"gap_{j}"] = zeros[j] - zeros[j - 1]
    for n in range(1, 6):
        candidates[f"C0q_at_qint_{n}"] = C0q(qint_unbalanced(n))
        candidates[f"C0q_at_{n}"] = C0q(mpf(n))

    # 0-dof falsification gate: does ANY candidate match ANY of the four
    # compact targets within 1%?
    matches = []
    for cname, cval in candidates.items():
        for tname, tval in targets.items():
            if tval != 0 and abs(cval / tval - 1) < mpf("0.01"):
                matches.append((cname, tname, mp.nstr(cval, 8),
                                mp.nstr(tval, 8)))
    # Also: does the ORDERED zero/√zero vector reproduce the whole 4-vector?
    def vector_match(vec):
        if len(vec) < 4:
            return False
        return all(tv != 0 and abs(vec[i] / tv - 1) < mpf("0.01")
                   for i, tv in enumerate(tvals))
    whole_vec_match = (
        vector_match([mp.sqrt(z) for z in zeros])
        or vector_match([z / z1 for z in zeros])
        or vector_match(zeros))
    any_match = bool(matches) or whole_vec_match

    print("# s013 — q-Bessel Tricomi C_{0,q} (library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf eq.11) vs compact target\n")
    print(f"q0 = {mp.nstr(Q0, 12)}   q = 1/q0 = {mp.nstr(Q, 12)}")
    print(f"targets  {[mp.nstr(v, 7) for v in tvals]}")
    print(f"first {len(zeros)} positive zeros of C_0,q:")
    for j, z in enumerate(zeros, 1):
        print(f"  ξ_{j} = {mp.nstr(z, 10)}   √ξ_{j} = {mp.nstr(mp.sqrt(z), 8)}"
              f"   ξ_{j}/ξ_1 = {mp.nstr(z / z1, 8)}")
    print(f"\nmatches within 1%: {matches if matches else 'NONE'}")
    print(f"whole-4-vector match: {whole_vec_match}")

    verdict = (
        "REFUTED-as-is (scope a): no parameter-free quantity of the sourced "
        "0th-order q-Bessel Tricomi C_{0,q} (library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf eq. 11) — "
        "positive zeros, zero ratios/roots, consecutive gaps, or C_{0,q} at "
        "q-integer/integer nodes — reproduces the compact keystone target "
        "{1,[4]_q,[5]_q,[4][3]/[2]} within 1%, and the ordered zero vectors do "
        "not match the 4-vector. Consistent with #3292's type argument: a "
        "transcendental non-compact q-Bessel object does not hit the compact "
        "algebraic (Laurent-polynomial) target at its own parameter-free nodes. "
        "This closes the q-Bessel-Tricomi sub-route WITH an in-repo source; it "
        "does NOT structurally exclude a Plancherel-fixed E_q(2) row (still "
        "needs the un-uploaded Koelink–Swarttouw q-Hankel kernel)."
        if not any_match else
        "MATCH FOUND (near-match tier; NOT wired) — see matches/whole_vec_match; "
        "re-adjudicate before any use.")
    print(f"\nVERDICT: {'match' if any_match else 'REFUTED-as-is, scope (a)'}")

    wb = WitnessBuilder("keystone-qbessel-tricomi-c0q-nodes",
                        engine="mpmath", output_dir=HERE)
    wb.set_description(
        "s013 redirect (ii) sourced sub-route: test whether the 0th-order "
        "q-Bessel Tricomi C_{0,q} from the owner-uploaded Raza–Fadel–Cesarano "
        "2025 paper (library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf eq. 11) reproduces the compact "
        "value-map target {1,[4]_q,[5]_q,[4][3]/[2]} at any PARAMETER-FREE node "
        "(zeros, zero ratios, q-integer evaluations). 0-dof falsifiable; no "
        "argument tuning; expected scope-(a) refutation carrying an in-repo "
        "source. Nothing wired.")
    wb.add_data("q0", mp.nstr(Q0, 30))
    wb.add_data("q_eval_inverse", mp.nstr(Q, 30))
    wb.add_data("targets", {k: mp.nstr(v, 20) for k, v in targets.items()})
    wb.add_data("positive_zeros_C0q", [mp.nstr(z, 20) for z in zeros])
    wb.add_data("matches_within_1pct", matches)
    wb.add_data("whole_vector_match", str(whole_vec_match))
    wb.add_data("verdict", verdict)
    wb.add_assertion("zeros_found", str(len(zeros) >= 4), "True",
                     source="the sign-change scan must locate ≥4 positive zeros "
                            "for the 4-vector comparison to be meaningful")
    wb.add_assertion("no_parameter_free_match", str(any_match), "False",
                     source="refutation gate: a future convention/node change "
                            "producing a 0-dof match must FAIL this witness so "
                            "the near-match is re-adjudicated (not silently used)")
    path = wb.save()
    print(f"witness: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
