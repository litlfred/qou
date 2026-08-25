#!/usr/bin/env python3
"""Can a `(gen_idx, ctype)` pair express the operator-valued p-n interface?

Bean `qou-gdtb` item 1 said no, twice over:

  > The pair form also cannot express the interface at all in principle:
  > `rho_k_h3a_refinement`'s own header says `I = σ_3 − (h/2)·1` is
  > **operator-valued**, non-scalar for 9 of 11 partitions λ ⊢ 6, while a
  > `(gen_idx, ctype)` pair denotes a *pure generator*.

This probe tests that claim and finds it is a CATEGORY ERROR. Two different
statements are being run together:

  (a) `ρ_λ(I)` is not a scalar matrix          — TRUE, and reproduced below
  (b) the pair form cannot denote `I`          — FALSE

(a) is a property of the REPRESENTATION. (b) would be a property of the
ENCODING. Neither implies the other, and the probe exhibits both at once:
every non-scalar λ still reconstructs exactly.

The reason (b) fails is one line of algebra. The interface is

    I = σ_g − (h/2)·1

i.e. exactly of the form `c·σ_g + d·1` with **d a scalar**. The pair names
the generator and the shift-class; `d_for_ctype` supplies the scalar. So

    I_pair = ρ_λ(σ_g) + d_for_ctype(ctype, h)·1  ==  ρ_λ(σ_g) − (h/2)·1

is an algebraic identity, holding for every λ and every representation.
`ρ_λ(σ_g)` is non-scalar, so `ρ_λ(I)` inherits that for free — there is
nothing left for the encoding to express.

The header the bean quoted (`rho_k_h3a_refinement.py:196`) is itself
correct: it says the BRANCHING COMBINER `A^λ_{μν}(I)` is operator-valued.
That is a statement about how `I` acts across a Wedderburn decomposition,
not about whether a braid word can denote it.

WHAT WAS REAL in item 1, and is now fixed: the label collapse. Both averaged
interfaces returned the ctype `averaged`, so consumers resolved the
colour-weighted one to `-h/2` and lost 6.879e-4 on that crossing. Measured
today on the deuteron word, exact triples vs classified pairs:

    worst relative |d_triple - d_pair| = 2.66e-16   (float64 epsilon)

WHERE THE PAIR FORM WOULD GENUINELY FAIL, stated so a later reader does not
have to re-derive it: an interface NOT of the form `c·σ_g + d·1` — a sum
over several generators, or a coefficient depending on λ. The corpus has no
such interface today. If one is ever introduced, the encoding must carry
triples (or grow a new ctype), and THAT is the real trigger to watch for —
not non-scalarity, which is universal and harmless.

Run: `python3 computations/probes/ctype_pair_expressiveness_probe.py`
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for p in (ROOT, ROOT / "hecke"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import _path_bridge  # noqa: F401, E402
import sympy as sp  # noqa: E402

from canonical_braid_crossings import d_for_ctype  # noqa: E402
from hecke_characters import partitions_of  # noqa: E402
from hoefsmit_symbolic import build_seminormal_matrices_symbolic  # noqa: E402

#: The interface sits at σ_3 in the H_6 block, per rho_k_h3a_refinement.
INTERFACE_GEN = 3
N = 6


def main() -> int:
    q = sp.symbols("q", positive=True)
    h = q - 1 / q

    print(__doc__.split("Run:")[0].strip()[:0] or "", end="")
    print(f"Interface I = σ_{INTERFACE_GEN} − (h/2)·1  over λ ⊢ {N}, "
          f"symbolic in q\n")
    print(f"{'λ':<20}{'dim':>4}  {'ρ_λ(I)':<12} max|I_pair − I_triple|")
    print("-" * 62)

    nonscalar = 0
    total = 0
    worst = sp.Integer(0)
    for lam in partitions_of(N):
        sig, dim = build_seminormal_matrices_symbolic(tuple(lam))
        if dim == 0:
            continue
        total += 1
        S = sig[INTERFACE_GEN]

        # Exact triple: d taken straight from the canonical word.
        i_triple = S - (h / 2) * sp.eye(dim)
        # Pair form: the ctype resolved through the canonical vocabulary.
        i_pair = S + d_for_ctype("averaged", h) * sp.eye(dim)

        delta = sp.simplify(i_triple - i_pair)
        maxdiff = max(abs(delta[i, j]) for i in range(dim) for j in range(dim))
        worst = max(worst, maxdiff)

        off = [sp.simplify(i_triple[i, j])
               for i in range(dim) for j in range(dim) if i != j]
        diag = [sp.simplify(i_triple[i, i]) for i in range(dim)]
        is_scalar = (all(e == 0 for e in off)
                     and all(sp.simplify(x - diag[0]) == 0 for x in diag))
        if not is_scalar:
            nonscalar += 1

        print(f"{str(tuple(lam)):<20}{dim:>4}  "
              f"{('scalar' if is_scalar else 'NON-scalar'):<12} {maxdiff}")

    print()
    print(f"NON-scalar ρ_λ(I): {nonscalar} of {total} partitions of {N}")
    print(f"worst |I_pair − I_triple| over all λ: {worst}")
    print()

    ok = (worst == 0) and (nonscalar > 0)
    if ok:
        print("VERDICT — the two properties are INDEPENDENT.")
        print(f"  {nonscalar} of {total} λ give a non-scalar ρ_λ(I), and every")
        print("  one of them reconstructs EXACTLY from the pair form.")
        print("  So 'operator-valued' does not imply 'inexpressible', and")
        print("  qou-gdtb item 1's second half does not hold.")
    else:
        print("VERDICT — claim NOT reproduced; re-read before acting on this.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
