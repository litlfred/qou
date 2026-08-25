#!/usr/bin/env python3
"""Which Markov convention were the committed mass-table Habiro witnesses built under?

Settles the attribution left open by PR #5526.  That PR regenerated the 20
canonical atoms, observed that 16 moved, and declined to attribute the move --
reasoning that the deuteron's only interface factor is ``z``, that the deuteron
was unchanged, and therefore that a C->D change in ``z`` could not be the cause.

That reasoning compares the WRONG FIELD.  ``habiro_coefficients`` / ``p_in_u``
are invariant under C->D for an all-``positive`` atom, because the whole
convention difference is absorbed into ``denom_in_u``:

    p(u) := u^shift * denom * tr_M(u^2)

For an all-positive atom the interface product is a pure power ``z^k``, so
swapping ``z_C -> z_D`` rescales ``tr_M`` by a rational function that ``denom``
cancels -- the numerator ``p(u)`` is untouched.  As soon as one interface is
``negative``/``averaged``, ``z`` sits inside a SUM ``(z - h)``, the numerator
itself changes, and ``p(u)`` moves.  So the observed "16 move, 4 do not" split
is not evidence against the convention swap -- it is exactly its signature.

The deuteron did move, in every field that is not the numerator:

    tr_M_at_q0   0.565089262867502  ->  0.6933894087146489     (+22.7 %)
    denom_in_u   (q+1)-type factors ->  (q^2+1)-type factors

METHOD -- "test the answer, not the source" (AGENTS.md, convention-C guidance).
Rather than grepping for a spelling of ``z``, reconstruct each committed
``tr_M_in_q`` from the two A=1 atoms and the interface product, once under each
convention, and ask which one reproduces the committed value:

    tr_M(Z, N) == tau_p^Z * tau_n^N * PROD interface_factor(kind)

    positive -> z        negative -> z - h        averaged -> z - h/2
    convention C: z = sqrt(q)/(q+1)        convention D: z = q^3/(q^2+1)
    h = q - 1/q  (both)

PRECISION.  Exact arithmetic end to end -- no float anywhere.  The identity is
checked at rational points chosen as perfect squares (q = r^2) so that sqrt(q)
is itself exact and convention C is representable without a radical.  Three
independent points; a rational-function identity failing at none of them is not
a numerical near-miss.

RESULT (2026-08-23, against main @ b4f9e350e9): 25/25 committed atoms reproduce
under convention C.  The 2 that also reproduce under D are proton and neutron,
whose interface product is the empty product 1 -- for them C and D are the same
statement.  Every atom that HAS an interface is convention C.
"""
from __future__ import annotations

import glob
import json
import os
import sys

import sympy as sp

Q = sp.Symbol('q')

# Interface primitives.  h is convention-independent.
H_EXPR = Q - 1 / Q
Z_BY_CONVENTION = {
    'C': sp.sqrt(Q) / (Q + 1),      # 1/(q^{1/2} + q^{-1/2}), excised 2026-08-09
    'D': Q ** 3 / (Q ** 2 + 1),     # production Markov parameter
}

# Perfect-square rationals: sqrt(q) stays exact, so convention C is exact too.
TEST_POINTS = [sp.Rational(49, 25), sp.Rational(121, 9), sp.Rational(9, 4)]

WITNESS_GLOB = 'computations/habiro-coefficients-*.witness.json'
_PREFIX, _SUFFIX = 'habiro-coefficients-', '.witness.json'


def _slug(path: str) -> str:
    return os.path.basename(path)[len(_PREFIX):-len(_SUFFIX)]


def _interface_product(kinds, z):
    """PROD of per-interface factors, under the given z."""
    expr = sp.Integer(1)
    for kind in kinds:
        if kind == 'positive':
            expr *= z
        elif kind == 'negative':
            expr *= z - H_EXPR
        elif kind == 'averaged':
            expr *= z - H_EXPR / 2
        else:
            raise ValueError(f'unknown interface kind {kind!r}')
    return expr


def _eval_exact(expr, q_val):
    """Evaluate at a perfect-square rational, keeping everything exact."""
    return sp.nsimplify(
        expr.subs(sp.sqrt(Q), sp.sqrt(q_val)).subs(Q, q_val), rational=True
    )


def _matches(tr_committed, base, kinds, z) -> bool:
    predicted = base * _interface_product(kinds, z)
    for q_val in TEST_POINTS:
        if sp.simplify(_eval_exact(tr_committed, q_val)
                       - _eval_exact(predicted, q_val)) != 0:
            return False
    return True


def main() -> int:
    def load(slug):
        with open(f'computations/{_PREFIX}{slug}{_SUFFIX}') as fh:
            return json.load(fh)

    tau_p = sp.sympify(load('proton')['tr_M_in_q'], locals={'q': Q})
    tau_n = sp.sympify(load('neutron')['tr_M_in_q'], locals={'q': Q})

    slugs = sorted(_slug(p) for p in glob.glob(WITNESS_GLOB))

    rows, tally = [], {'C': 0, 'D': 0, 'tested': 0}
    print(f"{'atom':<15}{'Z':>3}{'N':>3}  {'interfaces':<16} matches")
    for slug in slugs:
        data = load(slug)
        if 'Z' not in data or 'tr_M_in_q' not in data:
            continue                                  # aggregate, not an atom
        Z, N = data['Z'], data['N']
        kinds = data.get('interface_kinds') or []
        tr_committed = sp.sympify(data['tr_M_in_q'], locals={'q': Q})
        base = tau_p ** Z * tau_n ** N

        is_c = _matches(tr_committed, base, kinds, Z_BY_CONVENTION['C'])
        is_d = _matches(tr_committed, base, kinds, Z_BY_CONVENTION['D'])
        tally['C'] += is_c
        tally['D'] += is_d
        tally['tested'] += 1

        shape = ''.join(k[0] for k in kinds) or '(none)'
        verdict = 'C' if is_c and not is_d else ('D' if is_d and not is_c
                  else ('C=D (no interface)' if is_c and is_d else 'NEITHER'))
        rows.append({'atom': slug, 'Z': Z, 'N': N, 'interfaces': kinds,
                     'matches_C': bool(is_c), 'matches_D': bool(is_d)})
        print(f'{slug:<15}{Z:>3}{N:>3}  {shape:<16} {verdict}', flush=True)

    n = tally['tested']
    print()
    print(f"committed reproduced by convention C : {tally['C']}/{n}")
    print(f"committed reproduced by convention D : {tally['D']}/{n}")

    # Report whichever convention the table is UNIFORM in, rather than
    # asserting a particular one.  This probe was written to diagnose an
    # all-C table; once #5526 regenerated it the table became all-D, and a
    # verdict hard-coded to C reported "mixed / inconclusive" on a table that
    # is in fact perfectly uniform -- the checker's own orientation, mistaken
    # for a finding.  An interface-free atom matches BOTH conventions (empty
    # product), so uniformity is decided on the interface-carrying atoms only.
    with_iface = [r for r in rows if r['interfaces']]
    uniform_c = bool(with_iface) and all(
        r['matches_C'] and not r['matches_D'] for r in with_iface)
    uniform_d = bool(with_iface) and all(
        r['matches_D'] and not r['matches_C'] for r in with_iface)

    print()
    print(f'atoms carrying at least one interface : {len(with_iface)}')
    print(f'  ... uniformly convention C          : {uniform_c}')
    print(f'  ... uniformly convention D          : {uniform_d}')
    print(f'interface-free atoms (C == D)         : {len(rows) - len(with_iface)}')

    print()
    if uniform_d:
        print('VERDICT: the committed mass-table Habiro witnesses are '
              'convention D -- canonical per the 2026-08-15 R1 ruling.')
        return 0
    if uniform_c:
        print('VERDICT: the committed mass-table Habiro witnesses are '
              'convention C -- OFF-CANON, regenerate (see #5526).')
        return 1
    print('VERDICT: MIXED -- the table is not uniform in either convention. '
          'That is the worst state: inspect the table above.')
    return 1


if __name__ == '__main__':
    sys.exit(main())
