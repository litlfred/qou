#!/usr/bin/env python3
"""Is the Gram form nondegenerate on the LP ACTIVE SET? (50-dps, NO float64)

`borromean-axial-coupling.py` reads a `gram_inverse` key that
`be59f01376` removed, because the 6x6 NF Gram is SINGULAR (rank 5) and a
true inverse does not exist. Bean `qou-cnbm` framed the fix as a two-branch
decision: safe if the active set A misses the radical, a real modelling
question if it meets it. It then measured the radical to have FULL support
(6/6 nonzero in the NF basis), concluding no A escapes and the first branch
does not exist.

That conclusion is right about the radical and wrong about what follows,
because both branches ask about the WRONG object. The consumer computes

    pairing = u_A @ G_inv_A @ obs_A          # G_inv_A = GRAM_INV[ix_(A, A)]

and there are two inequivalent readings of "G^{-1} restricted to A":

    (a) restrict-then-nothing : (G^{-1})|_{A x A}   -- needs G invertible
    (b) restrict-then-invert  : (G|_{A x A})^{-1}   -- needs only the
                                                       RESTRICTION invertible

These differ by a Schur complement whenever A is proper, so (b) is not a
rename of (a). And (b) can exist when (a) does not: `ker(G) ∩ span(A) = 0`
is implied by the radical having full support, since a full-support vector
cannot lie in a proper coordinate subspace. **Full support is what makes (b)
available, not what rules it out** -- the bean read the same measurement as
closing the door.

This probe settles (b) by measurement, exactly. For every nonempty A it
reports the smallest |eigenvalue| of `G|_{A x A}`.

Precision: the committed `gram-matrix-dual.witness.json` stores the Gram as
RAW float64, so it cannot answer a singularity question on its own terms --
`det = 4.0e-17` there is indistinguishable from f64 noise. This probe takes
the exact-arithmetic route instead (`pyhecke.gram.gram_matrix_mp`, 50 dps at
the true substrate q_0) per the NO-FLOAT64 rule: a float64 input would have
resolved the answer at ~1e-16 no matter what is true, which is exactly the
scale of the thing being tested.
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402


def _min_abs_eig(M: list[list], dps: int) -> mp.mpf:
    """Smallest |eigenvalue| of a symmetric mpmath matrix."""
    A = mp.matrix(M)
    with mp.workdps(dps):
        eig = mp.eigsy(A, eigvals_only=True)
    return min((abs(eig[i]) for i in range(len(M))), key=lambda v: v)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    dps = 50

    from pyhecke.gram import gram_matrix_mp, radical_mp  # noqa: PLC0415
    G = gram_matrix_mp(dps)
    n = len(G)
    rad = radical_mp(dps)

    zero = mp.mpf(10) ** (-(dps // 2))
    support = sum(1 for x in rad if abs(mp.mpf(x)) > zero)

    rows, singular = [], []
    for k in range(1, n + 1):
        for A in itertools.combinations(range(n), k):
            sub = [[G[i][j] for j in A] for i in A]
            m = _min_abs_eig(sub, dps)
            is_sing = m < zero
            if is_sing:
                singular.append(list(A))
            rows.append({"A": list(A), "size": k,
                         "min_abs_eigenvalue": fmt(m), "singular": is_sing})

    proper_sing = [A for A in singular if len(A) < n]
    worst_proper = min((r for r in rows if r["size"] < n),
                       key=lambda r: mp.mpf(r["min_abs_eigenvalue"]))

    print("Gram restricted-nonsingularity probe (50 dps, exact route)")
    print("=" * 64)
    print(f"  radical support            : {support}/{n}")
    print(f"  subsets tested             : {len(rows)}")
    print(f"  singular restrictions      : {len(singular)} "
          f"({len(proper_sing)} of them proper)")
    print(f"  worst proper |lambda_min|  : "
          f"{mp.nstr(mp.mpf(worst_proper['min_abs_eigenvalue']), 8)} "
          f"at A={worst_proper['A']}")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gram-restricted-nonsingularity", engine="python",
                       start_time=t0)
    w.set_description(
        "Smallest |eigenvalue| of G|_{A×A} over every nonempty active set A, "
        "at 50-dps exact arithmetic. Decides whether the consumer's "
        "G^{-1}|_{A*} can be read as (G|_{A×A})^{-1} — invert the "
        "restriction — rather than as a restriction of a nonexistent inverse. "
        "The two differ by a Schur complement, so this is not a key rename."
    )
    w.add_data("radical_support", {"nonzero": support, "of": n})
    w.add_data("by_active_set", rows)
    w.add_data("singular_active_sets", singular)
    w.add_data("worst_proper_subset", worst_proper)
    w.add_assertion(
        name="restriction_nonsingular_on_every_proper_active_set",
        computed=len(proper_sing), expected=0, tolerance=0,
        source="a proper A with singular G|_{A×A} would leave the consumer's "
               "pairing genuinely undefined there",
    )
    print(f"Witness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
