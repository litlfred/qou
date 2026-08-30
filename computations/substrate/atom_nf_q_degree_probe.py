#!/usr/bin/env python3
"""
atom_nf_q_degree_probe — the q-degree of the six NF coefficients, as a function of A.

Bean `qou-brng` (the linking-vs-self-energy amplitude assignment), arc
`bk-crossing-mass-binding`.

`hecke_core_symbolic.build_atom_nf_sym(Z, N)` returns the atom's Hecke normal form as
six coefficients carried symbolically in q — six polynomials for any nucleus, at any A.
This probe measures their q-degree and asks how it scales with A.

## Why the degree is worth measuring

The NF coefficients are built by repeated `hm_sym(nf, 1, d, gen)`, i.e. by multiplying
by `(σ_gen + d·I)` with `d ∈ {0, −h, −h/2}` and `h = q − q⁻¹`. Each such factor moves the
Laurent degree by at most one, so the q-degree of the result COUNTS THE CROSSINGS in the
braid word — it is a purely algebraic readout of the word's length, with no anchor, no
substitution at q₀, and no AME input anywhere.

`build_atom_nf_sym` builds that word in three parts:

    per-nucleon internal structure   11 factors per nucleon   → 11·A
    inter-nucleon crossings          `for prev in range(k)`   → C(A,2)
    charge closure                   `for _ in range(Z)`      → Z

so the predicted crossing count is `M(Z,N) = 11A + A(A−1)/2 + Z`. The middle term is the
COMPLETE GRAPH on the nucleons: every nucleon crosses every earlier one, exactly once.

That matters for this arc. `QOU.Mass.CoordinationSaturation` proves that a complete-graph
coordination `M = C(A,2)` gives `B/A = ε·(A−1)/2`, which is unbounded — no plateau — and
that observed saturation therefore FORCES bounded degree. The q-degree measured here is an
independent, algebraic way to see which bond set the braid word actually uses: a degree
growing like `A²/2` is the complete graph; a degree growing linearly in `A` is bounded
coordination. The measurement does not itself decide the physics — it reads off the bond
set the *current* word encodes.

## Method

Two implementations, cross-checked against each other:

* `hm_sym` from `hecke_core_symbolic` — the authoritative multiplication table, sympy.
* `hm_laurent` — a literal transcription of the same two tables onto exact Laurent
  polynomials (`dict[int, Fraction]`), fast enough to reach large A.

Equality of the two is ASSERTED, both on random NF vectors and on complete builds, before
any degree is reported. Nothing here is float: coefficients are `fractions.Fraction`, the
q-exponents are `int`, and no value is ever substituted at q₀.

NO FLOAT64: no float arithmetic occurs. There is nothing to serialize at reduced
precision — the outputs are integers (degrees, term counts).
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from fractions import Fraction  # noqa: E402

import sympy as sp  # noqa: E402

from substrate.hecke_core_symbolic import (  # noqa: E402
    build_atom_nf_sym,
    hm_sym,
    _ground_state_ordering,
    q,
    h,
    HALF,
    ONE,
    NF_NAMES,
)

# ══════════════════════════════════════════════════════════════════════════════
# Exact Laurent polynomials in q:  dict[int exponent -> Fraction coefficient]
# ══════════════════════════════════════════════════════════════════════════════

ZERO_L: dict[int, Fraction] = {}
ONE_L: dict[int, Fraction] = {0: Fraction(1)}
H_L: dict[int, Fraction] = {1: Fraction(1), -1: Fraction(-1)}          # h = q − q⁻¹
NEG_H_L: dict[int, Fraction] = {1: Fraction(-1), -1: Fraction(1)}      # −h
NEG_HALF_H_L: dict[int, Fraction] = {1: Fraction(-1, 2), -1: Fraction(1, 2)}  # −h/2


def ladd(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    if not a:
        return dict(b)
    if not b:
        return dict(a)
    r = dict(a)
    for e, c in b.items():
        v = r.get(e, Fraction(0)) + c
        if v:
            r[e] = v
        else:
            r.pop(e, None)
    return r


def lmul(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    if not a or not b:
        return {}
    r: dict[int, Fraction] = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = ea + eb
            v = r.get(e, Fraction(0)) + ca * cb
            if v:
                r[e] = v
            else:
                r.pop(e, None)
    return r


def to_sympy(a: dict[int, Fraction]) -> sp.Expr:
    return sum(
        (sp.Rational(c.numerator, c.denominator) * q**e for e, c in a.items()),
        sp.Integer(0),
    )


def ldeg(a: dict[int, Fraction]) -> tuple[int, int]:
    """(max exponent, min exponent); (0, 0) for the zero polynomial."""
    if not a:
        return (0, 0)
    return (max(a), min(a))


# ══════════════════════════════════════════════════════════════════════════════
# hm_laurent — literal transcription of hecke_core_symbolic.hm_sym's two tables
# ══════════════════════════════════════════════════════════════════════════════

def hm_laurent(nf, c, d, gen):
    """Multiply an NF vector of Laurent polynomials by (c·σ_gen + d·I).

    Transcribed line-for-line from ``hecke_core_symbolic.hm_sym``; the two are
    asserted equal in ``check_equivalence`` below before any result is used.
    """
    r = [dict() for _ in range(6)]
    ch = lmul(c, H_L)
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, ch), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, ch), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, ch), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, ch), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, ch), (1, c), (4, d)]),
            (5, [(5, ch), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if not nf[si]:
            continue
        for ti, co in tgts:
            if not co:
                continue
            r[ti] = ladd(r[ti], lmul(nf[si], co))
    return r


def build_atom_nf_laurent(Z: int, N: int, *, inter_nucleon: bool = True):
    """Laurent mirror of ``build_atom_nf_sym`` — same control flow, same factors.

    ``inter_nucleon=False`` ABLATES the `for prev in range(k)` loop, i.e. drops the
    complete-graph inter-nucleon crossings and keeps only the per-nucleon internal
    structure and the charge closure. This is not a variant of the physics — it is the
    control that isolates which part of the word carries the A-dependence.
    """
    A = Z + N
    if A == 0:
        return [dict(ONE_L)] + [dict() for _ in range(5)], 0

    ordering = _ground_state_ordering(Z, N)
    nf = [dict(ONE_L)] + [dict() for _ in range(5)]
    steps = 0

    for k in range(A):
        kind = ordering[k]
        if kind == "p":
            for _ in range(3):
                nf = hm_laurent(nf, ONE_L, ZERO_L, 0); steps += 1
                nf = hm_laurent(nf, ONE_L, NEG_H_L, 1); steps += 1
            nf = hm_laurent(nf, ONE_L, ZERO_L, 0); steps += 1
            nf = hm_laurent(nf, ONE_L, NEG_HALF_H_L, 0); steps += 1
            nf = hm_laurent(nf, ONE_L, NEG_HALF_H_L, 1); steps += 1
            nf = hm_laurent(nf, ONE_L, ZERO_L, 0); steps += 1
            nf = hm_laurent(nf, ONE_L, ZERO_L, 0); steps += 1
        else:
            for _ in range(3):
                nf = hm_laurent(nf, ONE_L, ZERO_L, 0); steps += 1
                nf = hm_laurent(nf, ONE_L, NEG_H_L, 1); steps += 1
            nf = hm_laurent(nf, ONE_L, NEG_HALF_H_L, 0); steps += 1
            nf = hm_laurent(nf, ONE_L, NEG_HALF_H_L, 0); steps += 1
            nf = hm_laurent(nf, ONE_L, NEG_H_L, 1); steps += 1
            nf = hm_laurent(nf, ONE_L, ZERO_L, 0); steps += 1
            nf = hm_laurent(nf, ONE_L, ZERO_L, 0); steps += 1

        if inter_nucleon:
            for prev in range(k):
                ti, tj = ordering[prev], ordering[k]
                if ti == "p" and tj == "p":
                    nf = hm_laurent(nf, ONE_L, ZERO_L, 0)
                elif ti == "n" and tj == "n":
                    nf = hm_laurent(nf, ONE_L, NEG_H_L, 0)
                else:
                    nf = hm_laurent(nf, ONE_L, NEG_HALF_H_L, 0)
                steps += 1

    for _ in range(Z):
        nf = hm_laurent(nf, ONE_L, NEG_H_L, 1); steps += 1

    return nf, steps


# ══════════════════════════════════════════════════════════════════════════════
# Equivalence gate — the Laurent mirror must reproduce hm_sym exactly
# ══════════════════════════════════════════════════════════════════════════════

def check_equivalence() -> list[str]:
    """Assert hm_laurent == hm_sym, then build_atom_nf_laurent == build_atom_nf_sym."""
    lines = []

    # (1) per-step: deterministic spread of NF vectors, every gen and every d.
    seeds = [
        [ONE_L, {}, {}, {}, {}, {}],
        [{}, H_L, {}, {2: Fraction(3)}, {}, {-1: Fraction(1, 2)}],
        [{0: Fraction(1)}, {1: Fraction(-1), -1: Fraction(1)}, {3: Fraction(2, 3)},
         {}, {-2: Fraction(-5)}, {1: Fraction(7, 4)}],
    ]
    ds = [(ZERO_L, sp.Integer(0)), (NEG_H_L, -h), (NEG_HALF_H_L, -h * HALF)]
    n_step = 0
    for seed in seeds:
        seed_sym = [to_sympy(x) for x in seed]
        for gen in (0, 1):
            for dl, dsym in ds:
                got = hm_laurent(seed, ONE_L, dl, gen)
                want = hm_sym(seed_sym, ONE, dsym, gen)
                for i in range(6):
                    diff = sp.cancel(sp.expand(to_sympy(got[i]) - want[i]))
                    if diff != 0:
                        raise AssertionError(
                            f"hm mismatch: seed={seed} gen={gen} d={dsym} slot={i} "
                            f"diff={diff}"
                        )
                n_step += 1
    lines.append(f"  hm_laurent == hm_sym on {n_step} (seed, gen, d) cases x 6 slots  OK")

    # (2) LOCKSTEP whole build: run the sympy and Laurent builds side by side and
    #     compare after EVERY factor, so a control-flow transcription error is caught
    #     at the step it happens rather than being hidden by a later cancellation.
    #     The sympy side is expanded each step -- `sp.expand` is an identity, and
    #     without it `build_atom_nf_sym`'s unexpanded tree is not traversable at A>=3.
    n_build = n_lockstep = 0
    for (Z, N) in [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (2, 2)]:
        n_lockstep += _lockstep_build(Z, N)
        n_build += 1
    lines.append(
        f"  build_atom_nf_laurent == build_atom_nf_sym, checked after every factor, "
        f"on {n_build} nuclei / {n_lockstep} steps  OK"
    )
    return lines


def _lockstep_build(Z: int, N: int) -> int:
    """Run the sympy and Laurent builds in lockstep; assert equality at every step."""
    A = Z + N
    ordering = _ground_state_ordering(Z, N)
    nfs = [ONE] + [sp.Integer(0)] * 5
    nfl = [dict(ONE_L)] + [dict() for _ in range(5)]
    steps = 0

    def step(dl, dsym, gen):
        nonlocal nfs, nfl, steps
        nfs = [sp.expand(x) for x in hm_sym(nfs, ONE, dsym, gen)]
        nfl = hm_laurent(nfl, ONE_L, dl, gen)
        for i in range(6):
            if sp.expand(to_sympy(nfl[i]) - nfs[i]) != 0:
                raise AssertionError(
                    f"lockstep mismatch Z={Z} N={N} step={steps} slot={i} gen={gen}"
                )
        steps += 1

    Z0, ZH, ZN = (ZERO_L, sp.Integer(0)), (NEG_HALF_H_L, -h * HALF), (NEG_H_L, -h)
    for k in range(A):
        if ordering[k] == "p":
            for _ in range(3):
                step(*Z0, 0); step(*ZN, 1)
            step(*Z0, 0); step(*ZH, 0); step(*ZH, 1); step(*Z0, 0); step(*Z0, 0)
        else:
            for _ in range(3):
                step(*Z0, 0); step(*ZN, 1)
            step(*ZH, 0); step(*ZH, 0); step(*ZN, 1); step(*Z0, 0); step(*Z0, 0)
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                step(*Z0, 0)
            elif ti == "n" and tj == "n":
                step(*ZN, 0)
            else:
                step(*ZH, 0)
    for _ in range(Z):
        step(*ZN, 1)
    return steps


# ══════════════════════════════════════════════════════════════════════════════
# The measurement
# ══════════════════════════════════════════════════════════════════════════════

NUCLEI = [
    ("1H", 1, 0), ("n", 0, 1), ("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1),
    ("4He", 2, 2), ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5), ("12C", 6, 6),
    ("14N", 7, 7), ("16O", 8, 8), ("20Ne", 10, 10), ("24Mg", 12, 12),
    ("28Si", 14, 14), ("32S", 16, 16), ("40Ca", 20, 20),
]


def predicted_steps(Z: int, N: int) -> int:
    A = Z + N
    return 11 * A + A * (A - 1) // 2 + Z


def main() -> int:
    print("atom_nf_q_degree_probe — q-degree of the six NF coefficients vs A")
    print("=" * 78)
    print()
    print("Equivalence gate (Laurent mirror vs the authoritative hm_sym):")
    for ln in check_equivalence():
        print(ln)
    print()

    print("Crossing count: measured factor applications vs 11A + C(A,2) + Z")
    print(f"{'nucleus':>8} {'Z':>3} {'N':>3} {'A':>4} {'steps':>7} {'11A+C(A,2)+Z':>13} {'ok':>4}")
    rows = []
    for name, Z, N in NUCLEI:
        nf, steps = build_atom_nf_laurent(Z, N)
        pred = predicted_steps(Z, N)
        ok = "yes" if steps == pred else "NO"
        print(f"{name:>8} {Z:>3} {N:>3} {Z+N:>4} {steps:>7} {pred:>13} {ok:>4}")
        rows.append((name, Z, N, nf, steps))
    print()

    print("Per-coefficient Laurent degree  (max exponent, min exponent, span, #terms)")
    print(f"{'nucleus':>8} {'A':>4} " + " ".join(f"{nm:>16}" for nm in NF_NAMES))
    spans = []
    for name, Z, N, nf, steps in rows:
        cells = []
        smax = 0
        for i in range(6):
            hi, lo = ldeg(nf[i])
            nt = len(nf[i])
            cells.append(f"{hi:>4},{lo:>4},{hi-lo:>3},{nt:>3}" if nt else "           zero ")
            if nt:
                smax = max(smax, hi - lo)
        print(f"{name:>8} {Z+N:>4} " + " ".join(f"{c:>16}" for c in cells))
        spans.append((name, Z + N, Z, N, smax, steps))
    print()

    print("Degree span vs crossing count")
    print(f"{'nucleus':>8} {'A':>4} {'max span':>9} {'steps':>7} {'2*steps-span':>13}")
    for name, A, Z, N, smax, steps in spans:
        print(f"{name:>8} {A:>4} {smax:>9} {steps:>7} {2 * steps - smax:>13}")
    print()

    # ── (a) Bar-symmetry: is every coefficient invariant (or anti-invariant) under
    #        q -> q^{-1}?  This is a q-degree question's sharper twin: the tables above
    #        show hi = -lo for every slot and every nucleus, which is NECESSARY for
    #        bar-symmetry but not sufficient.  Test the coefficients themselves.
    print("Bar-symmetry of each coefficient under q -> 1/q  (even / odd / neither)")
    print(f"{'nucleus':>8} {'A':>4} {'steps%2':>8} "
          + " ".join(f"{nm:>9}" for nm in NF_NAMES) + "  rule")
    bar_rule_ok = True
    for name, Z, N, nf, steps in rows:
        cells = [bar_parity(nf[i]) for i in range(6)]
        # Claim: {γ, L₊, L₋} carry bar-parity (-1)^steps and {σ₀, σ₁, e⁻} carry
        # (-1)^(steps+1).  Checked, not asserted.
        want_a = "even" if steps % 2 == 0 else "odd"
        want_b = "odd" if steps % 2 == 0 else "even"
        ok = ([cells[i] for i in (0, 3, 4)] == [want_a] * 3
              and [cells[i] for i in (1, 2, 5)] == [want_b] * 3)
        bar_rule_ok &= ok
        print(f"{name:>8} {Z+N:>4} {steps % 2:>8} "
              + " ".join(f"{c:>9}" for c in cells) + ("  ok" if ok else "  NO"))
    print(f"  rule: bar-parity of (γ, L₊, L₋) = (-1)^(crossing count), "
          f"(σ₀, σ₁, e⁻) opposite  ->  {'holds on every nucleus' if bar_rule_ok else 'FAILS'}")
    print()

    # ── (b) Exponent parity: are all exponents of one parity (a Z/2 grading)?
    print("Exponent parity per slot  (all-even / all-odd / mixed; 'gaps' = missing rungs)")
    print(f"{'nucleus':>8} {'A':>4} " + " ".join(f"{nm:>13}" for nm in NF_NAMES))
    for name, Z, N, nf, steps in rows:
        cells = []
        for i in range(6):
            cells.append(exponent_parity(nf[i]))
        print(f"{name:>8} {Z+N:>4} " + " ".join(f"{c:>13}" for c in cells))
    print()

    # ── (c) THE ABLATION.  Rebuild each nucleus with the `for prev in range(k)`
    #        inter-nucleon loop switched off.  If the quadratic A-dependence of the
    #        degree survives, it is not the complete graph; if it collapses to linear,
    #        the complete graph is the whole of it.  This replaces a fit with a control.
    print("ABLATION: degree with the inter-nucleon loop ON vs OFF")
    print("  ON  = build_atom_nf_sym as written (complete graph, C(A,2) crossings)")
    print("  OFF = per-nucleon structure + charge closure only (no pair crossings)")
    print(f"{'nucleus':>8} {'A':>4} {'span ON':>9} {'span OFF':>9} {'ON-OFF':>8}")
    for name, Z, N in NUCLEI:
        A = Z + N
        nf_on, _ = build_atom_nf_laurent(Z, N, inter_nucleon=True)
        nf_off, _ = build_atom_nf_laurent(Z, N, inter_nucleon=False)
        s_on = max((ldeg(c)[0] - ldeg(c)[1]) for c in nf_on if c)
        s_off = max((ldeg(c)[0] - ldeg(c)[1]) for c in nf_off if c)
        print(f"{name:>8} {A:>4} {s_on:>9} {s_off:>9} {s_on - s_off:>8}")
    print()

    # Exact finite differences along an EVENLY SPACED N=Z chain (spacing hstep=4).
    # A degree-d polynomial in A has a vanishing (d+1)-th difference; the d-th is
    # constant and equals d!·(leading coeff)·hstep^d.  This is exact integer
    # arithmetic on measured integers -- there is no fit and no tolerance.
    HSTEP = 4
    CHAIN = [12, 16, 20, 24, 28, 32, 36, 40]
    on, off = [], []
    for A in CHAIN:
        nf_on, _ = build_atom_nf_laurent(A // 2, A // 2, inter_nucleon=True)
        nf_off, _ = build_atom_nf_laurent(A // 2, A // 2, inter_nucleon=False)
        on.append(max((ldeg(c)[0] - ldeg(c)[1]) for c in nf_on if c))
        off.append(max((ldeg(c)[0] - ldeg(c)[1]) for c in nf_off if c))
    delta = [b - a for a, b in zip(on, off)]

    print(f"Finite differences along the evenly spaced N=Z chain (A = {CHAIN}, "
          f"spacing {HSTEP})")
    for label, seq in (("span OFF (no pair crossings)", off),
                       ("span ON - span OFF (pair crossings alone)", [-d for d in delta]),
                       ("span ON (as written)", on)):
        d1 = [b - a for a, b in zip(seq, seq[1:])]
        d2 = [b - a for a, b in zip(d1, d1[1:])]
        d3 = [b - a for a, b in zip(d2, d2[1:])]
        print(f"  {label}")
        print(f"    values {seq}")
        print(f"    Δ      {d1}")
        print(f"    ΔΔ     {d2}")
        print(f"    ΔΔΔ    {d3}")
        if d2 and all(x == 0 for x in d2):
            print(f"    => LINEAR in A; slope = {Fraction(d1[0], HSTEP)} per nucleon")
        elif d3 and all(x == 0 for x in d3):
            lead = Fraction(d2[0], 2 * HSTEP * HSTEP)
            print(f"    => QUADRATIC in A; leading coefficient = {lead}")
        else:
            print("    => neither linear nor quadratic on this chain")
    print()

    # Closed forms, VERIFIED on every N=Z nucleus measured (not fitted-and-hoped).
    print("Closed forms on the N=Z chain, checked against every measured point")
    forms = [
        ("span OFF", lambda A: 23 * A - 2, off),
        ("span ON", lambda A: A * A + 14 * A + 42, on),
    ]
    for label, f, seq in forms:
        bad = [(A, f(A), s) for A, s in zip(CHAIN, seq) if f(A) != s]
        status = "all match" if not bad else f"MISMATCH {bad}"
        print(f"  {label:>9}: {status}")
    print()

    print("Reading")
    print("-" * 78)
    print("  * The six NF coefficients are LAURENT POLYNOMIALS in q, not general")
    print("    rational functions: build_atom_nf_sym never touches z or the Wedderburn")
    print("    weights, whose (q^2+1) and (q^4+4q^2+1) denominators enter only at the")
    print("    trace/volume step.  Every denominator here is a power of q.")
    print("  * Every coefficient is bar-EVEN or bar-ODD -- never neither -- and which")
    print("    one is fixed by the parity of the crossing count.  The NF vector is")
    print("    bar-graded, with {gamma, L+, L-} on one side and {s0, s1, e-} on the")
    print("    other.  This is the bar-parity the arc uses, visible on the word.")
    print("  * All exponents in a slot share one parity, and for A >= 12 the slot is")
    print("    DENSE in that sublattice (gaps=0): the coefficient is q^-D * P(q^2)")
    print("    with P of full degree D.  So the degree is not carried by a sparse")
    print("    leading term that could cancel downstream.")
    print("  * The q-degree is QUADRATIC in A, and the ablation shows the quadratic")
    print("    is ENTIRELY the inter-nucleon loop: with that loop off the span is")
    print("    exactly linear (23A - 2 on the N=Z chain, second difference 0), and")
    print("    the pair crossings alone contribute a term with leading coefficient")
    print("    exactly 1 in A^2.  That is a control, not a fit.")
    print("  * Consequence for the bk-crossing arc: the braid word this producer")
    print("    builds encodes the COMPLETE GRAPH on the nucleons -- the bond set")
    print("    QOU.Mass.CoordinationSaturation proves gives B/A = eps*(A-1)/2,")
    print("    unbounded, with no plateau.  The q-degree is an algebraic readout of")
    print("    which bond set a producer uses, needing no q0, no anchor and no AME.")
    return 0


def bar_parity(a: dict[int, Fraction]) -> str:
    """Is `a` fixed by q -> 1/q (even), negated (odd), or neither?"""
    if not a:
        return "zero"
    bar = {-e: c for e, c in a.items()}
    if bar == a:
        return "even"
    if bar == {e: -c for e, c in a.items()}:
        return "odd"
    return "NEITHER"


def exponent_parity(a: dict[int, Fraction]) -> str:
    """All exponents even, all odd, or mixed — plus how many rungs of that parity
    class are missing between the extreme exponents."""
    if not a:
        return "zero"
    par = {e % 2 for e in a}
    hi, lo = max(a), min(a)
    rungs = (hi - lo) // 2 + 1
    gaps = rungs - len(a)
    if par == {0}:
        tag = "even"
    elif par == {1}:
        tag = "odd"
    else:
        return f"MIXED({len(a)})"
    return f"{tag} gaps={gaps}"


if __name__ == "__main__":
    raise SystemExit(main())
