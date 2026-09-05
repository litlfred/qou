#!/usr/bin/env python3
"""magnus_where_cancellation_lives_probe.py — is the cancellation in the 7-term a-sum, or spectral?
(qou-o6ov)

WHY THIS QUESTION. #6792 established that the arc's bound is loose almost entirely because of the
cancellation factor κ = |Σ eig| / Σ|eig| — the Cauchy–Schwarz half is uniform at ~2–4×, while 1/κ
spans 1.07 … 85.45. So bounding κ is the sub-problem. But κ is defined over dim_λ eigenvalues
(up to 216 at n=9), which is a hard object.

THE HOPE, and it was a specific one. The #6534 identity gives

    tr_λ(ρ·Ω₂^P) = c · Σ_a tr_λ([ρ, σ_a]·σ_(a+1)),      only ngen−1 = 7 terms

so IF the cancellation lived in that 7-term sum, the problem would shrink from dim eigenvalues to
seven numbers. Define κ_a = |Σ_a t_a| / Σ_a |t_a| and compare it to κ. Two clean outcomes were
possible and the probe reports either:
    κ_a ≈ κ   → the effect is captured by 7 terms; bounding it becomes finite and structural.
    κ_a ≫ κ   → the cancellation is genuinely spectral; no rearrangement of the a-sum reaches it.

THE ANSWER IS NEITHER, and the nuance is the result. κ factors as κ_a × κ_spec, and MEASURED at
n=9 the two are comparable — 1/κ_a spans 1.0 … 9.3 and 1/κ_spec spans 1.07 … 9.3 — and they
MULTIPLY. At (5,2,2): 9.3 × 5.75 = 53.4, which is the whole 1/κ. At the hook (6,1,1,1) the a-sum
barely cancels (κ_a = 0.969) and the spectral part supplies the entire 9.3×.

So the 7-term reduction does NOT capture the cancellation. Both levels contribute, in roughly equal
measure on a log scale, and a bound built on the a-sum alone can be no better than ~9× at n=9 —
against a total 1/κ reaching 85×. That closes the route the identity seemed to offer, which is
worth knowing precisely because the identity is exact and Lean-proved and therefore looked free.

NOTE ON WHAT κ_a IS NOT. κ_a is not a bound and not an approximation to κ; it is the OTHER factor
in an exact split. Reporting it alone would overstate the a-sum route, which is why the ratio column
(= 1/κ_spec) is printed beside it rather than left to be inferred.

scope-(a); NO-FLOAT64 (mpf, dps 65). Nothing wired.

dps NOTE: every probe in this arc pins mp.mp.dps at module scope, so dps is set AFTER all imports
here; the _assert_dps guards from #6710 are enabled on both imported probes deliberately.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
import magnus_commutator_bound_probe as C  # noqa: E402
import magnus_kappa_decomposition_probe as K  # noqa: E402

DEFAULT = [(8, 1), (7, 2), (6, 3), (6, 1, 1, 1), (5, 4), (5, 2, 2), (3, 3, 3)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    mp.mp.dps = args.dps           # AFTER the imports — see the module docstring
    C._WANT_DPS = args.dps
    K._WANT_DPS = args.dps

    q = base.Q0
    n = 3 * args.A
    Z, N = args.A // 2, args.A - args.A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[where] n={n}: κ = κ_a × κ_spec — an EXACT split, not an approximation")
    print(f"[where]   κ_a    = |Σ_a t_a| / Σ_a|t_a|,  t_a = tr([ρ,σ_a]σ_(a+1))   ({ngen-1} terms)")
    print(f"[where]   κ      = |Σ eig| / Σ|eig|                                   (dim_λ terms)")
    print(f"[where]   κ_spec = κ / κ_a, printed as its reciprocal in the ratio column\n")
    print("   λ                    dim     κ_a         κ        1/κ_a    1/κ_spec     1/κ")
    rows = []
    for lam in DEFAULT:
        m = C.measure(lam, gens, q, ngen)
        ta = [mp.re(x) for x in m["rhs_C"]]
        ka = abs(sum(ta)) / sum(abs(x) for x in ta)
        M, dim = K.build_X_dense(lam, gens, q, ngen)
        E, _ = mp.eig(M)
        tr = mp.re(sum(M[i, i] for i in range(dim)))
        k = abs(tr) / sum(abs(x) for x in E)
        rows.append((lam, dim, ka, k))
        print(f"  {str(lam):<20} {dim:>4}  {mp.nstr(ka,6):>9}  {mp.nstr(k,6):>9}  "
              f"{mp.nstr(1/ka,5):>7}  {mp.nstr(ka/k,5):>9}  {mp.nstr(1/k,6):>8}")

    inv_a = [1 / r[2] for r in rows]
    inv_s = [r[2] / r[3] for r in rows]
    print(f"\n  1/κ_a     spans {mp.nstr(min(inv_a),4)} … {mp.nstr(max(inv_a),4)}")
    print(f"  1/κ_spec  spans {mp.nstr(min(inv_s),4)} … {mp.nstr(max(inv_s),4)}")
    print("\n  ⇒ NEITHER FACTOR DOMINATES, and they MULTIPLY. The 7-term reduction does not capture")
    print("    the cancellation: a bound built on the a-sum alone can be no better than the 1/κ_a")
    print("    range above, against a total 1/κ reaching 85× elsewhere in the census (#6792).")
    print("    The route the #6534 identity seemed to offer is closed — worth stating precisely")
    print("    BECAUSE that identity is exact and Lean-proved, and therefore looked free.")


if __name__ == "__main__":
    main()
