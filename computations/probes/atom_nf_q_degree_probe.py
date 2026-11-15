#!/usr/bin/env python3
"""atom_nf_q_degree_probe.py
============================

**The q-degree of the six NF coefficients that `build_atom_nf_sym(Z, N)`
returns — measured exactly, for every nucleus up to A = 30.**

`hecke_core_symbolic.build_atom_nf_sym` returns the atom braid's normal form
as six coefficients in the NF basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]` (word lengths
`ℓ = 0, 1, 1, 2, 2, 3`).  Its docstring says the coefficients live in
`ℚ(q, √q)`.  Under **convention D** (`z = q³/(q²+1)`, owner ruling
2026-08-15) that is stale in two ways at once, and both matter here:

  * there is **no `√q`** — the half-power branch was a convention-C artefact
    and `z` does not enter `hm_sym` in either convention anyway; and
  * they are not general rational functions but **Laurent polynomials**:
    `hm_sym` only ever multiplies by `c = 1` and adds `d ∈ {0, −h, −h/2}`
    with `h = q − q⁻¹`, so every coefficient lies in `ℤ[½][q, q⁻¹]`.

So "q-degree" is well posed: each coefficient has a top exponent and a bottom
exponent, and this probe measures both.

## What is measured

1. **Support is exactly symmetric.**  Every non-zero coefficient has
   `lo = −hi`, for all six components and every `(Z, N)` tested.  There is
   no lop-sided Laurent tail.
2. **A ℤ/2 grading.**  Within one component every exponent has the same
   parity, and `exponent parity + ℓ(w)` is constant across all six
   components of a given nucleus.  The `c = 1` entries of `hm_sym` change
   the NF word length by one; the `c·h` and `d` entries keep the word and
   carry an odd power of q.  So the two parities are locked together.
3. **Bar involution.**  Consequently `cᵢ(1/q) = (−1)^p cᵢ(q)` with `p` that
   component's common exponent parity: each coefficient is an eigenvector
   of `q ↦ q⁻¹` with eigenvalue `±1` fixed by word length.
4. **Degree is quadratic in A**, from the `A(A−1)/2` inter-nucleon pair
   steps, and the constant depends sharply on isospin:

   * **All-proton ray (N = 0):** `deg(σ₀) = 12A + A(A−1)/2 − 1` exactly,
     verified A = 1…30.  That is *one less than the number of `hm_sym`
     calls* — proton-proton pairs carry `d = 0`, nothing cancels, and every
     step contributes a full degree.
   * **Pure-neutron ray (Z = 0):** `deg(γ) = A(A+1)/2`, the triangular
     number — but **only on 7 ≤ A ≤ 26**.  It breaks at A = 27 and the
     excess then grows by 2 per unit A.  Reported as a scoped observation,
     not a law: had this been checked only to A = 16, as the first sweep
     did, it would have looked exact.

5. **The max-plus (tropical) bound is not tight, and misses by a lot.**
   Taking degrees of the *effective* step matrix (same-target contributions
   summed first, so the structural `c·h + d = 0` of `σ⁻¹` is already
   included) gives a genuine upper bound — it is ≥ the true degree in every
   one of the components tested — but it is attained in under a third of
   them.  The gap is always even, is zero on the proton-rich side, and
   reaches **104 in degree** already at A = 12, the largest nucleus in
   this sweep — it is still growing there, so 104 is a floor on the gap,
   not a maximum.  The neutron-rich coefficients suffer massive
   leading-order cancellation that no degree-only model sees.

## Cost, and why the mirror exists

`build_atom_nf_sym` as written is **exponential**: `hm_sym` never
canonicalises, so the sympy expression tree multiplies out at every one of
the `11A + A(A−1)/2 + Z` calls.  A = 1 takes 0.13 s; A = 2 did not finish in
**15 minutes** in this session.  The corpus already diagnosed this correctly
— `compound_shift_nf.py` names "expression fan-out … without intermediate
canonicalization" and `crystal_shift_nf_atomic.py` calls the symbolic-q path
abandoned — and routed around it through crystal pole counting.

Two things follow, and only the second is new.  Wrapping each `hm_sym`
result in `sp.expand` is value-preserving and brings A = 8 down to ~8.5 s, so
the path is not intractable, only unnormalised.  And carrying the
coefficients as `dict[int, Fraction]` — exact, no sympy at all — reaches
A = 30 in seconds, which is what makes this measurement possible.

**This probe does not change `hecke_core_symbolic`.**  It mirrors `hm_sym`
line for line and *imports* `_ground_state_ordering` from the module rather
than copying it, so the strand order cannot drift; and it gates itself on
agreeing with the real function.

## What is NOT established

* No mechanism is claimed for the neutron-rich cancellation, nor for the
  A = 27 break in the triangular law.  Both are measured, not derived.
* `shift_NF(β) = 18Z + 21N + 1` (`prop:per-nucleon-shift-additive-linearity`)
  is a **different quantity** and does not match any degree here (deuteron:
  shift 40 against `deg(σ₀) = 23`, support span 46).  That is not a
  discrepancy — `shift_NF` is a `D(u)` exponent shift read off the crystal
  pole order, not the q-degree of an NF coefficient.  Recorded so the next
  reader does not "reconcile" two unrelated numbers.
* Nothing here is anchor-dependent: `q` is a symbol from start to finish and
  no q₀ is ever substituted.

Reference: prop:mass-endomorphism-tower, thm:wedderburn-mass-formula
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve()
_ROOT = _HERE.parent.parent.parent
_sys.path.insert(0, str(_ROOT / "computations"))
_sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
import _path_bridge as _b  # noqa: E402, F401
del _b

import time  # noqa: E402
from fractions import Fraction as F  # noqa: E402

import sympy as sp  # noqa: E402

import hecke_core_symbolic as HS  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

NF_NAMES = ["gamma", "sigma0", "sigma1", "L+", "L-", "e-"]
ELL = [0, 1, 1, 2, 2, 3]          # NF word lengths

# ── exact Laurent arithmetic: dict[exponent] -> Fraction ─────────────
# No floats anywhere in this file. Fraction is exact; the coefficients
# are half-integers (d = -h/2 for mixed quark and p-n crossings), so
# int would be wrong and float would be a NO-FLOAT64 violation.

ONE_LP = {0: F(1)}
H_LP = {1: F(1), -1: F(-1)}            # h    = q - q^-1
MH_LP = {1: F(-1), -1: F(1)}           # -h
MHALF_LP = {1: F(-1, 2), -1: F(1, 2)}  # -h/2


def lp_add(a, b):
    if not a:
        return dict(b)
    if not b:
        return dict(a)
    r = dict(a)
    for e, c in b.items():
        v = r.get(e, F(0)) + c
        if v:
            r[e] = v
        else:
            r.pop(e, None)
    return r


def lp_mul(a, b):
    if not a or not b:
        return {}
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1 + e2
            v = r.get(e, F(0)) + c1 * c2
            if v:
                r[e] = v
            else:
                r.pop(e, None)
    return r


def _tables(c, d, gen):
    """The hm_sym multiplication tables, verbatim from hecke_core_symbolic."""
    ch = lp_mul(c, H_LP)
    if gen == 0:
        return [
            (0, [(1, c), (0, d)]),
            (1, [(1, ch), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, ch), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, ch), (4, c), (5, d)]),
        ]
    return [
        (0, [(2, c), (0, d)]),
        (1, [(4, c), (1, d)]),
        (2, [(2, ch), (0, c), (2, d)]),
        (3, [(5, c), (3, d)]),
        (4, [(4, ch), (1, c), (4, d)]),
        (5, [(5, ch), (3, c), (5, d)]),
    ]


def hm_lp(nf, c, d, gen):
    """Exact mirror of ``hecke_core_symbolic.hm_sym``."""
    r = [{} for _ in range(6)]
    for si, tgts in _tables(c, d, gen):
        if not nf[si]:
            continue
        for ti, co in tgts:
            if co:
                r[ti] = lp_add(r[ti], lp_mul(nf[si], co))
    return r


def step_sequence(Z, N):
    """The (c, d, gen) sequence ``build_atom_nf_sym`` applies, in order.

    The strand order is taken from the module's own
    ``_ground_state_ordering`` — not re-implemented — so it cannot drift.
    """
    A = Z + N
    if A == 0:
        return []
    ordering = HS._ground_state_ordering(Z, N)
    seq = []
    for k in range(A):
        if ordering[k] == "p":
            for _ in range(3):
                seq.append((ONE_LP, {}, 0))
                seq.append((ONE_LP, MH_LP, 1))
            seq += [(ONE_LP, {}, 0), (ONE_LP, MHALF_LP, 0),
                    (ONE_LP, MHALF_LP, 1), (ONE_LP, {}, 0), (ONE_LP, {}, 0)]
        else:
            for _ in range(3):
                seq.append((ONE_LP, {}, 0))
                seq.append((ONE_LP, MH_LP, 1))
            seq += [(ONE_LP, MHALF_LP, 0), (ONE_LP, MHALF_LP, 0),
                    (ONE_LP, MH_LP, 1), (ONE_LP, {}, 0), (ONE_LP, {}, 0)]
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                seq.append((ONE_LP, {}, 0))
            elif ti == "n" and tj == "n":
                seq.append((ONE_LP, MH_LP, 0))
            else:
                seq.append((ONE_LP, MHALF_LP, 0))
    for _ in range(Z):
        seq.append((ONE_LP, MH_LP, 1))
    return seq


def build_atom_nf_lp(Z, N):
    """Exact Laurent mirror of ``build_atom_nf_sym``. Returns (nf, n_calls)."""
    nf = [dict(ONE_LP)] + [{} for _ in range(5)]
    seq = step_sequence(Z, N)
    for c, d, gen in seq:
        nf = hm_lp(nf, c, d, gen)
    return nf, len(seq)


# ── tropical (max-plus) degree bound ─────────────────────────────────

def _effective_matrix(c, d, gen):
    """M[s][t] with same-target contributions SUMMED.

    Summing first is what lets the tropical model see the one structural
    cancellation in the construction: on a d = -h step the diagonal is
    c*h + d = 0, i.e. the step is sigma^-1. A per-contribution degree
    model would miss it and the bound would be much weaker.
    """
    M = [[{} for _ in range(6)] for _ in range(6)]
    for si, tgts in _tables(c, d, gen):
        for ti, co in tgts:
            M[si][ti] = lp_add(M[si][ti], co)
    return M


def tropical_degrees(Z, N):
    """Max-plus upper bound on the six top-degrees. None = tropical zero."""
    v = [0, None, None, None, None, None]
    for c, d, gen in step_sequence(Z, N):
        T = [[(max(e) if e else None) for e in row]
             for row in _effective_matrix(c, d, gen)]
        out = [None] * 6
        for s in range(6):
            if v[s] is None:
                continue
            for t in range(6):
                if T[s][t] is None:
                    continue
                cand = v[s] + T[s][t]
                if out[t] is None or cand > out[t]:
                    out[t] = cand
        v = out
    return v


# ── gate: the mirror must reproduce the real function ────────────────

def _to_sympy(lp):
    if not lp:
        return sp.Integer(0)
    return sum(sp.Rational(c.numerator, c.denominator) * HS.q ** e
               for e, c in lp.items())


def cross_check(fails):
    """Gate the mirror against ``hecke_core_symbolic.build_atom_nf_sym``.

    Two rounds, deliberately:

    * **stock** — the real `hm_sym`, untouched, at A = 1.  This is the
      strongest form of the check but the function is exponential, so A = 1
      is as far as it goes (A = 2 does not finish in 15 min).
    * **normalised** — `hm_sym` wrapped in `sp.expand`, which is
      value-preserving, up to A = 6.  This is what reaches the
      inter-nucleon pair steps and the electron steps, which A = 1 has
      none of.

    Round 1 also checks that the two agree with each other at A = 1, so the
    wrapper used in round 2 is not taken on trust.
    """
    stock = HS.hm_sym
    results = {"stock_cases": [], "normalised_cases": [],
               "expand_is_value_preserving": None,
               "timing_note": ("`ms` is integer wall-clock, indicative only "
                               "-- no result depends on it. Recorded as int "
                               "because time.time() is float64 and a raw "
                               "float must not enter a witness.")}

    for Z, N in [(1, 0), (0, 1)]:
        t0 = time.time()
        sym = HS.build_atom_nf_sym(Z, N)
        lpv, _ = build_atom_nf_lp(Z, N)
        ok = all(sp.simplify(sp.expand(sym[i] - _to_sympy(lpv[i]))) == 0
                 for i in range(6))
        results["stock_cases"].append({"Z": Z, "N": N, "identical": ok,
                                       "ms": int((time.time() - t0) * 1000)})
        if not ok:
            fails.append(f"mirror != stock build_atom_nf_sym at Z={Z} N={N}")
        print(f"  stock       Z={Z} N={N} identical={ok}")

    def hm_norm(nf, c, d, gen):
        return [sp.expand(x) for x in stock(nf, c, d, gen)]

    try:
        HS.hm_sym = hm_norm
        same = all(sp.simplify(sp.expand(a - b)) == 0 for a, b in
                   zip(HS.build_atom_nf_sym(1, 0), stock_ref))
        results["expand_is_value_preserving"] = same
        if not same:
            fails.append("sp.expand wrapper changed build_atom_nf_sym at A=1")
        print(f"  sp.expand wrapper value-preserving at A=1: {same}")

        for Z, N in [(1, 1), (2, 1), (2, 2), (3, 2), (2, 3),
                     (3, 3), (0, 4), (4, 0), (0, 5), (5, 0)]:
            t0 = time.time()
            sym = HS.build_atom_nf_sym(Z, N)
            lpv, _ = build_atom_nf_lp(Z, N)
            ok = all(sp.simplify(sp.expand(sym[i] - _to_sympy(lpv[i]))) == 0
                     for i in range(6))
            results["normalised_cases"].append(
                {"Z": Z, "N": N, "identical": ok,
                 "ms": int((time.time() - t0) * 1000)})
            if not ok:
                fails.append(f"mirror != normalised build at Z={Z} N={N}")
            print(f"  normalised  Z={Z} N={N} identical={ok}")
    finally:
        HS.hm_sym = stock
    return results


stock_ref = None   # filled in main() before cross_check runs


def main() -> int:
    global stock_ref
    t0 = time.time()
    fails: list[str] = []

    def chk(label, cond):
        print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
        if not cond:
            fails.append(label)

    print("build_atom_nf_sym — q-degree of the six NF coefficients")
    print("=" * 68)

    print("\n1. GATE: exact Laurent mirror vs hecke_core_symbolic")
    stock_ref = HS.build_atom_nf_sym(1, 0)
    xc = cross_check(fails)

    print("\n2. Ring: Laurent polynomials in Z[1/2][q, q^-1]?")
    # Z[1/2] is the DYADIC rationals -- every a/2^k, not only the halves.
    # d = -h/2 enters once per mixed crossing and the denominators compound,
    # so the right test is "denominator is a power of two", not "divides 2".
    dyadic = 0
    max_den_exp = 0
    non_dyadic = set()
    for A in range(1, 9):
        for Z in range(0, A + 1):
            nf, _ = build_atom_nf_lp(Z, A - Z)
            for c in nf:
                for v in c.values():
                    d = v.denominator
                    if d & (d - 1):
                        non_dyadic.add(d)
                    elif d != 1:
                        dyadic += 1
                        max_den_exp = max(max_den_exp, d.bit_length() - 1)
    chk(f"every denominator is a power of two, i.e. the ring is Z[1/2][q,q^-1] "
        f"({len(non_dyadic)} non-dyadic denominators)", not non_dyadic)
    chk(f"non-integer coefficients do occur ({dyadic}), so it is not Z[q^+-1]; "
        f"deepest denominator 2^{max_den_exp}", dyadic > 0)

    print("\n3. Support symmetry (lo == -hi) and the Z/2 grading")
    asym = 0
    graded = 0
    ungraded = []
    mixed_parity = 0
    for A in range(1, 13):
        for Z in range(0, A + 1):
            nf, _ = build_atom_nf_lp(Z, A - Z)
            inv = set()
            for i, c in enumerate(nf):
                if not c:
                    continue
                if min(c) != -max(c):
                    asym += 1
                pars = {e % 2 for e in c}
                if len(pars) > 1:
                    mixed_parity += 1
                for p in pars:
                    inv.add((p + ELL[i]) % 2)
            if len(inv) <= 1:
                graded += 1
            else:
                ungraded.append((Z, A - Z))
    chk(f"support symmetric lo == -hi in every component ({asym} exceptions)",
        asym == 0)
    chk(f"every component has ONE exponent parity ({mixed_parity} exceptions)",
        mixed_parity == 0)
    chk(f"exponent parity + word length constant per nucleus "
        f"({graded}/{graded + len(ungraded)})", not ungraded)

    print("\n4. Bar involution c(1/q) = (-1)^p c(q)")
    bad_bar = 0
    for A in range(1, 11):
        for Z in range(0, A + 1):
            nf, _ = build_atom_nf_lp(Z, A - Z)
            for c in nf:
                if not c:
                    continue
                p = next(iter(c)) % 2
                sign = 1 if p == 0 else -1
                if any(c.get(-e, F(0)) != sign * v for e, v in c.items()):
                    bad_bar += 1
    chk(f"every coefficient is a +-1 eigenvector of q -> 1/q "
        f"({bad_bar} exceptions)", bad_bar == 0)

    print("\n5. All-proton ray (N = 0): deg(sigma0) = 12A + A(A-1)/2 - 1")
    proton_ray = []
    proton_ok = True
    for A in range(1, 31):
        nf, calls = build_atom_nf_lp(A, 0)
        got = max(nf[1])
        pred = 12 * A + A * (A - 1) // 2 - 1
        proton_ray.append({"A": A, "calls": calls, "deg_sigma0": got,
                           "closed_form": pred})
        proton_ok &= (got == pred) and (got == calls - 1)
    chk("closed form holds for every A = 1..30, and equals n_calls - 1",
        proton_ok)

    print("\n6. Pure-neutron ray (Z = 0): deg(gamma) vs the triangular number")
    neutron_ray = []
    for A in range(1, 31):
        nf, calls = build_atom_nf_lp(0, A)
        neutron_ray.append({"A": A, "calls": calls, "deg_gamma": max(nf[0]),
                            "triangular": A * (A + 1) // 2,
                            "deg_sigma0": max(nf[1])})
    hold = [r["A"] for r in neutron_ray if r["deg_gamma"] == r["triangular"]]
    first_break = next((r["A"] for r in neutron_ray
                        if r["A"] > min(hold) and
                        r["deg_gamma"] != r["triangular"]), None)
    chk(f"triangular law holds on the contiguous window A = {min(hold)}..{max(hold)}",
        hold == list(range(min(hold), max(hold) + 1)))
    chk(f"and it BREAKS at A = {first_break} — scoped observation, not a law",
        first_break == 27)

    print("\n7. Tropical (max-plus) bound vs actual degree")
    gaps: dict[int, int] = {}
    below = 0
    exact_rows = 0
    rows = 0
    for A in range(1, 13):
        for Z in range(0, A + 1):
            nf, _ = build_atom_nf_lp(Z, A - Z)
            act = [max(c) if c else None for c in nf]
            tro = tropical_degrees(Z, A - Z)
            rows += 1
            g = []
            for a, t in zip(act, tro):
                if a is None or t is None:
                    continue
                g.append(t - a)
                gaps[t - a] = gaps.get(t - a, 0) + 1
                if t < a:
                    below += 1
            if all(x == 0 for x in g):
                exact_rows += 1
    tot = sum(gaps.values())
    chk(f"tropical is a genuine UPPER bound ({below} violations of {tot})",
        below == 0)
    chk(f"but it is NOT tight: attained in {gaps.get(0, 0)}/{tot} components",
        gaps.get(0, 0) < tot)
    chk(f"every gap is even (the Z/2 grading again): "
        f"{sorted(k for k in gaps if k % 2)} odd gaps", not [k for k in gaps if k % 2])
    print(f"      exact on {exact_rows}/{rows} nuclei; max gap {max(gaps)}")

    print("\n8. Denominator = 2^(number of AVERAGED pn crossings)")
    # appendix-nf-witnesses/witness-computation-method.md states, for the
    # RUST hecke-engine, that the true value is poly / 2^{p_n} with p_n the
    # count of averaged (pn) crossings. hecke_core_symbolic is an
    # independent Python implementation; this checks the two agree.
    den_rows = []
    den_ok = True
    for A in range(1, 11):
        for Z in range(0, A + 1):
            N = A - Z
            n_avg = sum(1 for (c, d, g) in step_sequence(Z, N) if d == MHALF_LP)
            nf, _ = build_atom_nf_lp(Z, N)
            k = max((v.denominator.bit_length() - 1
                     for c in nf for v in c.values()), default=0)
            den_rows.append({"A": A, "Z": Z, "N": N,
                             "averaged_crossings": n_avg, "denominator_exp": k})
            den_ok &= (k == n_avg)
    chk("denominator exponent equals the averaged-crossing count on all 65 "
        "nuclei A<=10 (the published 2^{p_n} rule, independently reproduced)",
        den_ok)

    print("\n9. WHICH step kind opens the max-plus gap?")
    # The three inter-nucleon coefficients are, per the published table:
    #   pp  d = 0     -> sigma      (positive crossing)
    #   nn  d = -h    -> sigma^-1   (negative crossing)
    #   pn  d = -h/2  -> (sigma + sigma^-1)/2   (averaged; not a braid element)
    # Attribute every unit of gap to the step that opened it.
    opened: dict[str, int] = {}
    seen: dict[str, int] = {}
    tight_nuclei = []
    for A in range(1, 11):
        for Z in range(0, A + 1):
            N = A - Z
            nf = [dict(ONE_LP)] + [{} for _ in range(5)]
            tv = [0, None, None, None, None, None]
            prev = 0
            for (c, d, gen) in step_sequence(Z, N):
                nf = hm_lp(nf, c, d, gen)
                T = [[(max(e) if e else None) for e in row]
                     for row in _effective_matrix(c, d, gen)]
                out = [None] * 6
                for si in range(6):
                    if tv[si] is None:
                        continue
                    for ti in range(6):
                        if T[si][ti] is None:
                            continue
                        cand = tv[si] + T[si][ti]
                        if out[ti] is None or cand > out[ti]:
                            out[ti] = cand
                tv = out
                a = max((max(x) for x in nf if x), default=None)
                t_ = max((x for x in tv if x is not None), default=None)
                g = t_ - a
                dn = "0" if not d else ("-h" if d == MH_LP else "-h/2")
                key = f"gen{gen} d={dn}"
                seen[key] = seen.get(key, 0) + 1
                if g > prev:
                    opened[key] = opened.get(key, 0) + (g - prev)
                prev = g
            if prev == 0:
                tight_nuclei.append({"Z": Z, "N": N})
    total_units = sum(opened.values())
    avg_units = opened.get("gen0 d=-h/2", 0) + opened.get("gen1 d=-h/2", 0)
    avg_runs = seen.get("gen0 d=-h/2", 0) + seen.get("gen1 d=-h/2", 0)
    nn_units = opened.get("gen0 d=-h", 0)
    for k in sorted(seen):
        print(f"      {k:<14} run {seen[k]:>5}   opened {opened.get(k, 0):>5}")
    chk(f"the AVERAGED pn crossing opens NO gap ever ({avg_units} units in "
        f"{avg_runs} occurrences)", avg_units == 0)
    chk(f"the nn NEGATIVE crossing opens most of it ({nn_units}/{total_units} "
        f"units from {seen.get('gen0 d=-h', 0)} steps)",
        nn_units > total_units // 2)
    # N <= 2 (at most one nn pair) is NECESSARY but NOT sufficient: three
    # nuclei with one nn pair are still not tight. The step trace says why --
    # a single negative crossing's loss is recovered by the steps that FOLLOW
    # it, and in those three the nn step sits too near the end of the
    # sequence. Measured below rather than asserted.
    tight_by_N = all(r["N"] <= 2 for r in tight_nuclei)
    le2 = {(Z, A - Z) for A in range(1, 11) for Z in range(0, A + 1)
           if A - Z <= 2}
    tight_set = {(r["Z"], r["N"]) for r in tight_nuclei}
    exceptions = sorted(le2 - tight_set)
    chk(f"every tight nucleus has at most one nn pair, N <= 2 "
        f"({len(tight_nuclei)} tight) — NECESSARY", tight_by_N)
    chk(f"but N <= 2 is NOT sufficient: {len(exceptions)} of {len(le2)} such "
        f"nuclei are not tight — {exceptions}", bool(exceptions))

    # Steps remaining after the LAST nn step, tight vs not, for the N <= 2 set.
    tail_rows = []
    for (Z, N) in sorted(le2):
        seq = step_sequence(Z, N)
        idx = [i for i, (c, d, g) in enumerate(seq) if g == 0 and d == MH_LP]
        tail_rows.append({"Z": Z, "N": N,
                          "steps_after_last_nn": (len(seq) - 1 - idx[-1])
                                                 if idx else None,
                          "tight": (Z, N) in tight_set})
    short = [r for r in tail_rows
             if r["steps_after_last_nn"] is not None and not r["tight"]]
    long_ = [r for r in tail_rows
             if r["steps_after_last_nn"] is not None and r["tight"]]
    if short and long_:
        worst = max(r["steps_after_last_nn"] for r in short)
        best = min(r["steps_after_last_nn"] for r in long_)
        print(f"      steps after last nn step: not-tight <= {worst}, "
              f"tight >= {best}")
        chk(f"the not-tight ones are exactly those whose nn step has too few "
            f"steps after it (<= {worst} vs >= {best})", worst < best)

    print(f"\n{'ALL CHECKS PASSED' if not fails else str(len(fails)) + ' CHECK(S) FAILED'}")

    w = WitnessBuilder("atom-nf-q-degree", start_time=t0,
                       output_dir=_HERE.parent)
    w.set_description(
        "q-degree of the six NF coefficients of "
        "hecke_core_symbolic.build_atom_nf_sym(Z, N), measured exactly for "
        "every nucleus to A=30 via a Fraction-exact Laurent mirror gated "
        "against the real function. FINDINGS. (a) The coefficients are "
        "Laurent polynomials in Z[1/2][q,q^-1] -- NOT the 'Q(q, sqrt q)' the "
        "docstring claims; the sqrt q was a convention-C artefact and z never "
        "enters hm_sym. (b) Support is exactly symmetric, lo = -hi, in every "
        "component of every nucleus tested. (c) A Z/2 grading: exponent "
        "parity + NF word length is constant per nucleus, so each coefficient "
        "is a +-1 eigenvector of the bar involution q -> 1/q with the sign "
        "fixed by word length. (d) Degree is QUADRATIC in A, from the "
        "A(A-1)/2 pair steps. On the all-proton ray deg(sigma0) = "
        "12A + A(A-1)/2 - 1 exactly for A=1..30, one less than the number of "
        "hm_sym calls: pp pairs carry d=0 and nothing cancels. On the "
        "pure-neutron ray deg(gamma) = A(A+1)/2 on 7<=A<=26 and BREAKS at "
        "A=27 -- scoped observation, not a law; a sweep stopping at A=16 "
        "would have called it exact. (e) The max-plus bound on the effective "
        "step matrix is a genuine upper bound but is attained in under a "
        "third of components; the gap is always even, zero on the "
        "proton-rich side, and reaches 104 in degree at A=12 (the largest "
        "in this sweep, and still growing there -- a floor, not a max), so "
        "neutron-rich coefficients cancel at leading order in a way no "
        "degree-only model sees. NOT ESTABLISHED: no mechanism for that "
        "cancellation or for the A=27 break. shift_NF = 18Z+21N+1 is a "
        "DIFFERENT quantity (deuteron 40 vs deg(sigma0) 23) and is not "
        "reconciled here.")
    w.add_data("cross_check", xc)
    w.add_data("ring", {"non_dyadic_denominators": sorted(non_dyadic),
                        "non_integer_coefficients": dyadic,
                        "deepest_denominator_power_of_two": max_den_exp,
                        "ring": "Z[1/2][q, q^-1]  (dyadic, not merely halves)",
                        "docstring_says": "Q(q, sqrt q)  [stale: convention C]"})
    w.add_data("structure", {
        "support_asymmetric_components": asym,
        "mixed_parity_components": mixed_parity,
        "nuclei_with_parity_plus_wordlength_constant": graded,
        "bar_involution_exceptions": bad_bar,
        "nf_word_lengths": dict(zip(NF_NAMES, ELL)),
    })
    w.add_data("all_proton_ray", proton_ray)
    w.add_data("pure_neutron_ray", neutron_ray)
    w.add_data("triangular_law_window", {
        "holds_from": min(hold), "holds_to": max(hold),
        "breaks_at": first_break,
        "caution": "a sweep stopping at A=16 reports this as exact",
    })
    w.add_data("tropical_gap_histogram",
               {str(k): v for k, v in sorted(gaps.items())})
    w.add_data("not_established", {
        "neutron_rich_cancellation_mechanism": "measured, not derived",
        "A27_break_in_triangular_law": "measured, not derived",
        "shift_NF": ("18Z + 21N + 1 is a D(u) exponent shift from the crystal "
                     "pole order, not an NF-coefficient q-degree; it matches "
                     "nothing here and is not a discrepancy"),
        "A_above_30": "not measured",
    })
    w.add_data("denominator_is_two_to_the_averaged_crossing_count", {
        "rule": "denominator = 2^(number of d=-h/2 averaged crossings)",
        "published_as": ("folio/quantum-observable-universe/"
                         "appendix-nf-witnesses/witness-computation-method.md "
                         "states poly / 2^{p_n} for the RUST hecke-engine; "
                         "this reproduces it from the independent Python "
                         "hecke_core_symbolic"),
        "holds_on_all_65_nuclei_A_le_10": den_ok,
        "rows": den_rows,
    })
    w.add_data("gap_attribution_by_step_kind", {
        "crossing_dictionary": {
            "gen0 d=0": "sigma (positive crossing) -- pp pair, uu quark",
            "gen0 d=-h": "sigma^-1 (negative crossing) -- nn pair, dd quark",
            "gen0 d=-h/2": "(sigma + sigma^-1)/2 averaged -- pn pair, ud quark",
        },
        "published_convention": ("the three-row table is already in "
                                 "appendix-nf-witnesses/"
                                 "witness-computation-method.md; this probe "
                                 "re-derived it and adds only the DEGREE "
                                 "consequence below"),
        "steps_run": seen,
        "gap_units_opened": opened,
        "averaged_crossing_opens_zero_gap": {"units": avg_units,
                                             "occurrences": avg_runs},
        "tropical_tight_nuclei": tight_nuclei,
        "criterion": ("N <= 2 (at most one nn pair) is NECESSARY for the "
                      "max-plus bound to be tight, and NOT sufficient"),
        "n_le_2_but_not_tight": exceptions,
        "steps_after_last_nn_step": tail_rows,
    })
    w.add_data("checks_failed", fails)
    w.add_assertion("coefficients_are_laurent_over_Z_half", not non_dyadic, True)
    w.add_assertion("support_symmetric_lo_eq_minus_hi", asym == 0, True)
    w.add_assertion("parity_plus_wordlength_is_constant", not ungraded, True)
    w.add_assertion("bar_involution_eigenvectors", bad_bar == 0, True)
    w.add_assertion("all_proton_closed_form_A_1_to_30", proton_ok, True)
    w.add_assertion("triangular_law_breaks_at_A_27", first_break == 27, True)
    w.add_assertion("tropical_is_an_upper_bound", below == 0, True)
    w.add_assertion("tropical_bound_is_not_tight", gaps.get(0, 0) < tot, True)
    w.add_assertion("denominator_is_2_to_the_averaged_crossing_count", den_ok, True)
    w.add_assertion("averaged_pn_crossing_never_opens_a_gap", avg_units == 0, True)
    w.add_assertion("tight_implies_at_most_one_nn_pair", tight_by_N, True)
    w.add_assertion("at_most_one_nn_pair_is_NOT_sufficient",
                    bool(exceptions), True)
    w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": ("q is a sympy Symbol / a formal Laurent variable "
                           "from start to finish; no q0 is substituted "
                           "anywhere, so neither pin can affect any number "
                           "in this witness."),
    })
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
