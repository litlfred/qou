#!/usr/bin/env python3
"""Construct + verify the figure-eight quantum A-polynomial (AJ verification).

Part of the "AJ in QOU, fully and honestly" tranche (audit:
docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md; bean lineage cp4i;
Lean statement: QOU/BraidKnot/AJFigureEight.lean `StrongAJFigureEight`).
The strong AJ conjecture is PROVED for 4_1 in the literature
([nguyen-tran-2021]); this script reproduces it corpus-side:

  1. FIND the minimal coefficient window: mod-p linear algebra (fast exact
     arithmetic in GF(p)) locates the smallest Laurent-degree window in
     m = q^N for which the inhomogeneous order-2 system
         a2(q,m) J_{N+2} + a1(q,m) J_{N+1} + a0(q,m) J_N = b(q,m)
     has a ONE-dimensional solution space — the canonical operator, no
     multiples, so per-q solutions are comparable across q.
  2. SOLVE exactly (Fraction Gauss) at many exact rational q values.
  3. RECONSTRUCT each m-coefficient as a rational function of q (exact
     numerator/denominator linear solve over Q).
  4. VERIFY the reconstructed symbolic operator annihilates J_N(4_1;q)
     SYMBOLICALLY (exact sympy, q symbolic) for N = 1..N_VERIFY — the
     verification is exact and independent of the construction heuristics,
     so steps 1-3 carry no epistemic weight.
  5. SPECIALIZE q -> 1 and compare the homogeneous part with the classical
     A-polynomial A_{4_1}(L, M) = M^4 L^2 - (M^8 - M^6 - 2M^4 - M^2 + 1) L + M^4
     (CCGLS tables) under the standard convention maps m -> M and m -> M^2
     (convention sorting against a FIXED reference — not a fit; the AJ
     statement allows an L-free rational factor in M).

J_N via the exact Lambda-Newton form (proved in Lean:
QOU/BraidKnot/HabiroNewtonLadder.lean). Audit-only; no production wiring.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE / "substrate"))

import sympy as sp

q = sp.symbols("q")
m = sp.symbols("m")
L = sp.symbols("L")
M = sp.symbols("M")

ORDER = 2
P = (1 << 61) - 1  # Mersenne prime for the structure pass
Q_STRUCTURE = Fraction(2)
Q_SAMPLES = [Fraction(2), Fraction(3), Fraction(5, 2), Fraction(7, 3),
             Fraction(4), Fraction(9, 4), Fraction(5), Fraction(11, 5),
             Fraction(3, 2), Fraction(8, 3), Fraction(7, 2), Fraction(13, 6),
             Fraction(6), Fraction(10, 3), Fraction(12, 5), Fraction(9, 2),
             Fraction(11, 4), Fraction(13, 4), Fraction(15, 4), Fraction(17, 6),
             Fraction(19, 6), Fraction(7)]
N_VERIFY_SYMBOLIC = 12
DEG_Q = 10  # max numerator/denominator q-degree in reconstruction


# ---------- colored Jones (Lambda-Newton form) --------------------------------

def jones_frac(qv: Fraction, Nmax: int) -> dict[int, Fraction]:
    out = {}
    for N in range(1, Nmax + 1):
        LamN = qv**N + qv**(-N)
        total, term = Fraction(1), Fraction(1)  # k=0 term included
        for k in range(1, N):
            term *= (LamN - (qv**k + qv**(-k)))
            total += term
        out[N] = total
    return out


def jones_modp(qnum: int, qden: int, Nmax: int) -> dict[int, int]:
    qv = qnum * pow(qden, P - 2, P) % P
    qinv = pow(qv, P - 2, P)
    out = {}
    for N in range(1, Nmax + 1):
        LamN = (pow(qv, N, P) + pow(qinv, N, P)) % P
        total, term = 1, 1
        for k in range(1, N):
            lamk = (pow(qv, k, P) + pow(qinv, k, P)) % P
            term = term * ((LamN - lamk) % P) % P
            total = (total + term) % P
        out[N] = total
    return out


# ---------- GF(p) linear algebra ----------------------------------------------

def nullspace_modp(rows: list[list[int]]) -> list[list[int]]:
    """Nullspace basis of the row-matrix over GF(P)."""
    if not rows:
        return []
    ncols = len(rows[0])
    A = [r[:] for r in rows]
    pivots = []  # (row, col)
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(A)) if A[i][c] % P), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], P - 2, P)
        A[r] = [x * inv % P for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(x - f * y) % P for x, y in zip(A[i], A[r])]
        pivots.append((r, c))
        r += 1
        if r == len(A):
            break
    pivot_cols = {c for _, c in pivots}
    free_cols = [c for c in range(ncols) if c not in pivot_cols]
    basis = []
    for fc in free_cols:
        v = [0] * ncols
        v[fc] = 1
        for (pr, pc) in pivots:
            v[pc] = (-A[pr][fc]) % P
        basis.append(v)
    return basis


def build_rows(J, mpow, unknown_list, nmax):
    """Rows of the annihilation system. J: dict N->value (field elems),
    mpow(N, d) -> m^d at that N. unknown ('b', d) or (j, d)."""
    rows = []
    for N in range(1, nmax - ORDER + 1):
        row = []
        for u in unknown_list:
            j, d = u
            if j == "b":
                row.append(-mpow(N, d))
            else:
                row.append(mpow(N, d) * J[N + j])
        rows.append(row)
    return rows


def unknowns_for(window):
    degs = list(window)
    us = []
    for j in range(ORDER + 1):
        us += [(j, d) for d in degs]
    us += [("b", d) for d in degs]
    return us


# ---------- exact Fraction Gauss ----------------------------------------------

def solve_unique_exact(rows: list[list[Fraction]]) -> list[Fraction] | None:
    """Given rows of a homogeneous system with nullity exactly 1 (assumed),
    return the solution normalized so its first nonzero entry is 1."""
    ncols = len(rows[0])
    A = [r[:] for r in rows]
    pivots = []
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = A[r][c]
        A[r] = [x / inv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        pivots.append((r, c))
        r += 1
        if r == len(A):
            break
    pivot_cols = [c for _, c in pivots]
    free_cols = [c for c in range(ncols) if c not in pivot_cols]
    if len(free_cols) != 1:
        return None
    fc = free_cols[0]
    v = [Fraction(0)] * ncols
    v[fc] = Fraction(1)
    for (pr, pc) in pivots:
        v[pc] = -A[pr][fc]
    piv0 = next(x for x in v if x != 0)
    return [x / piv0 for x in v]


def main() -> int:
    t0 = time.monotonic()
    print("\n  AJ verification for 4_1 (v2): minimal window -> exact -> verify -> q->1\n")

    # ---- step 1: minimal window via GF(p) ------------------------------------
    qn, qd = int(Q_STRUCTURE.numerator), int(Q_STRUCTURE.denominator)
    found = None
    for size in range(3, 12):
        for lo in range(-size, 1):
            window = range(lo, lo + size)
            us = unknowns_for(window)
            nmax = 4 * size + 14
            Jp = jones_modp(qn, qd, nmax + ORDER)
            qv = qn * pow(qd, P - 2, P) % P
            def mpow(N, d, qv=qv):
                return pow(qv, N * d, P) if d >= 0 else pow(pow(qv, P - 2, P), N * (-d), P)
            rows = build_rows(Jp, mpow, us, nmax)
            ns = nullspace_modp(rows)
            if len(ns) == 1:
                found = (window, us)
                print(f"  [window] minimal window found: degrees "
                      f"[{min(window)}..{max(window)}] (nullity 1 mod p at q={Q_STRUCTURE})")
                break
            elif len(ns) > 1:
                # window already too generous at this size; try next lo
                continue
        if found:
            break
    if not found:
        print("  [window] no nullity-1 window up to size 11 — abort")
        return 1
    window, us = found
    size = len(list(window))
    nmax = 4 * size + 14

    # support pattern from the mod-p solution (for reporting only)
    # ---- step 2: exact per-q solves ------------------------------------------
    per_q = {}
    for qv in Q_SAMPLES:
        J = jones_frac(qv, nmax + ORDER)
        def mpowf(N, d, qv=qv):
            return qv ** (N * d)
        rows = build_rows(J, mpowf, us, nmax)
        sol = solve_unique_exact(rows)
        if sol is None:
            print(f"  [exact] q={qv}: nullity != 1 — abort")
            return 1
        per_q[qv] = dict(zip(us, sol))
    print(f"  [exact] solved at {len(Q_SAMPLES)} exact rational q values "
          f"({time.monotonic()-t0:.0f}s)")

    # ---- step 3: reconstruct q-rational coefficient functions ----------------
    qs = list(per_q.keys())
    coeff_fns = {}
    for u in us:
        vals = [sp.Rational(per_q[qv][u].numerator, per_q[qv][u].denominator)
                for qv in qs]
        if all(v == 0 for v in vals):
            coeff_fns[u] = sp.Integer(0)
            continue
        p_syms = sp.symbols(f"p0:{DEG_Q + 1}")
        s_syms = sp.symbols(f"s0:{DEG_Q + 1}")
        eqs = []
        for qv, c in zip(qs, vals):
            qr = sp.Rational(qv.numerator, qv.denominator)
            eqs.append(sum(p_syms[i] * qr**i for i in range(DEG_Q + 1))
                       - c * sum(s_syms[i] * qr**i for i in range(DEG_Q + 1)))
        sol = sp.linsolve(eqs, [*p_syms, *s_syms])
        if not sol:
            print(f"  [reconstruct] {u}: no deg<={DEG_Q} rational function — abort")
            return 1
        vec = list(sol)[0]
        free = sorted(set().union(*[t.free_symbols for t in vec], set()),
                      key=lambda x: x.name)
        got = None
        for f_ in free:
            trial = {g: (1 if g == f_ else 0) for g in free}
            den = sum(vec[DEG_Q + 1 + i].subs(trial) * q**i for i in range(DEG_Q + 1))
            if den != 0:
                num = sum(vec[i].subs(trial) * q**i for i in range(DEG_Q + 1))
                got = sp.cancel(num / den)
                break
        if got is None:
            print(f"  [reconstruct] {u}: degenerate — abort")
            return 1
        coeff_fns[u] = got

    degs = list(window)
    def assemble(j):
        key = j if j != "b" else "b"
        return sp.cancel(sum(coeff_fns[(key, d)] * m**d for d in degs))
    a = {j: assemble(j) for j in range(ORDER + 1)}
    b = assemble("b")
    print("\n  reconstructed operator (a2 J_{N+2} + a1 J_{N+1} + a0 J_N = b):")
    for j in range(ORDER + 1):
        print(f"    a{j}(q,m) = {sp.factor(sp.simplify(a[j]))}")
    print(f"    b(q,m)  = {sp.factor(sp.simplify(b))}")

    # ---- step 4: EXACT symbolic verification (the epistemic step) ------------
    def jones_symbolic(N: int):
        LamN = q**N + q**(-N)
        total, term = sp.Integer(1), sp.Integer(1)
        for k in range(1, N):
            term = sp.expand(term * (LamN - (q**k + q**(-k))))
            total += term
        return total
    Jsym = {N: jones_symbolic(N) for N in range(1, N_VERIFY_SYMBOLIC + ORDER + 1)}
    ver_ok = {}
    for N in range(1, N_VERIFY_SYMBOLIC + 1):
        mv = q**N
        lhs = sum(a[j].subs(m, mv) * Jsym[N + j] for j in range(ORDER + 1))
        resid = sp.cancel(lhs - b.subs(m, mv))
        ver_ok[N] = (resid == 0)
        if not ver_ok[N]:
            print(f"  [verify] N={N}: RESIDUAL != 0")
    all_ver = all(ver_ok.values())
    print(f"\n  [verify] symbolic annihilation N=1..{N_VERIFY_SYMBOLIC}?  {all_ver}"
          f"  ({time.monotonic()-t0:.0f}s)")
    if not all_ver:
        return 1

    # ---- step 5: q -> 1 specialization vs classical A-polynomial -------------
    A_classical = M**4 * L**2 - (M**8 - M**6 - 2 * M**4 - M**2 + 1) * L + M**4
    spec_results = {}
    for name, msub in (("m->M", M), ("m->M^2", M**2)):
        op_cl = sp.Integer(0)
        ok = True
        for j in range(ORDER + 1):
            cj = sp.cancel(a[j].subs(m, msub))
            cj1 = sp.limit(cj, q, 1)
            if cj1 in (sp.oo, -sp.oo, sp.zoo, sp.nan):
                ok = False
                break
            op_cl += sp.expand(cj1) * L**j
        if not ok:
            spec_results[name] = "pole at q=1"
            continue
        op_cl = sp.expand(op_cl)
        ratio = sp.cancel(op_cl / A_classical)
        num_, den_ = sp.fraction(sp.together(ratio))
        unit_match = (not num_.has(L)) and (not den_.has(L)) and \
            sp.simplify(sp.expand(op_cl * den_ - A_classical * num_)) == 0
        spec_results[name] = {
            "classical_limit": str(op_cl),
            "ratio_to_A_classical": str(sp.cancel(ratio)),
            "matches_up_to_L_free_M_factor": bool(unit_match),
        }
        print(f"\n  [q->1, {name}] limit = {op_cl}")
        print(f"  [q->1, {name}] ratio to A_4_1 = {sp.cancel(ratio)} (L-free factor match: {unit_match})")

    any_match = any(isinstance(v, dict) and v["matches_up_to_L_free_M_factor"]
                    for v in spec_results.values())
    elapsed = time.monotonic() - t0
    verdict = (
        ("AJ VERIFIED for 4_1 (corpus-side): the minimal-window order-2 "
         "inhomogeneous operator annihilates J_N(4_1) exactly (symbolic q, "
         f"N=1..{N_VERIFY_SYMBOLIC}) and its q->1 homogeneous part matches the "
         "classical A-polynomial up to an L-free factor in M — independently "
         "reproducing [nguyen-tran-2021] at the QOU muon-anchor knot.")
        if any_match else
        ("PARTIAL: operator constructed + symbolically verified as annihilator; "
         "q->1 L-free-factor match did not close under standard convention maps — "
         "record for convention triage; do NOT declare AJ verified.")
    )
    print(f"\n  VERDICT: {verdict}\n  ({elapsed:.1f}s)")

    payload = {
        "description": (
            "Figure-eight quantum A-polynomial: minimal-window exact construction "
            "of the order-2 inhomogeneous annihilator of J_N(4_1), exact symbolic "
            "verification, q->1 specialization vs the classical A-polynomial "
            "(AJ verification at the QOU muon anchor)."
        ),
        "computation": "aj_figure_eight_operator_construct_verify",
        "audit_only": True,
        "context": {
            "literature": "strong AJ proved for 4_1 [nguyen-tran-2021]; AJ statement [garoufalidis2004]",
            "jones_object": "Lambda-Newton form; Lean: QOU/BraidKnot/HabiroNewtonLadder.lean",
            "lean_statement": "QOU/BraidKnot/AJFigureEight.lean StrongAJFigureEight",
            "classical_A_poly": "M^4 L^2 - (M^8 - M^6 - 2M^4 - M^2 + 1) L + M^4 (CCGLS)",
        },
        "operator": {
            "form": "a2(q,m) J_{N+2} + a1(q,m) J_{N+1} + a0(q,m) J_N = b(q,m), m=q^N",
            "window": [min(window), max(window)],
            "a2": str(sp.factor(sp.simplify(a[2]))),
            "a1": str(sp.factor(sp.simplify(a[1]))),
            "a0": str(sp.factor(sp.simplify(a[0]))),
            "b": str(sp.factor(sp.simplify(b))),
        },
        "construction": {
            "structure_prime": str(P),
            "q_samples": [str(x) for x in Q_SAMPLES],
            "reconstruction_deg_q": DEG_Q,
        },
        "verification": {
            "symbolic_annihilation_N": {str(N): bool(v) for N, v in ver_ok.items()},
            "all_verified": bool(all_ver),
        },
        "specialization_q_to_1": spec_results,
        "verdict": verdict,
        "tier": "structural-exact annihilation; convention-sorted L-free-factor match at q=1",
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "aj-figure-eight-operator-construct-verify", payload,
        script_path=__file__, engine="sympy",
        engine_version=sp.__version__, start_time=t0,
    ).save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
