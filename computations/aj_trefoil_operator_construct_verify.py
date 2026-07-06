#!/usr/bin/env python3
"""Construct + verify the trefoil quantum A-polynomial (AJ verification).

Bean 3eeq — "do the same for the trefoil" (the QOU electron knot), mirroring
computations/aj_figure_eight_operator_construct_verify.py (whose generic
exact-linear-algebra machinery this script imports).  AJ for the trefoil is
literature-established (two-bridge: Le 2006; torus-knot verifications since
[garoufalidis2004]); this is the corpus-side reproduction.

  1. TOWER: colored Jones of T(2,3) from the Rosso-Jones / twist-eigenvalue
     decomposition of the closure of sigma_1^3 in B_2:
         J_N ~ theta^{-3} * sum_{j=0}^{n} T_j^3 [2j+1]_v / [N]_v,
     n = N-1, w = q^{1/4} (v = w^2), T_j = eps_j w^{2j(j+1) - n(n+2)},
     theta = w^{n(n+2)} (the braiding eigenvalue genuinely lives at
     quarter-powers of q — pinned by the spin-1/2 case q^{1/4}/-q^{-3/4}).
     The sign and framing conventions are SELF-ANCHORED, not trusted: the
     script scans {eps_j = (-1)^{n-j} or (-1)^j} x {framing -3, +3} and
     requires J_1 = 1 exactly, J_N in Z[q^{+-1}] (w-powers multiple of 4),
     and J_2 equal to the trefoil Jones polynomial
     V(3_1) = -q^{-4} + q^{-3} + q^{-1} (or its mirror).  Exactly one
     convention must survive; everything downstream uses it.
  2. OPERATOR: minimal-window nullity-1 construction (mod-p structure pass,
     exact Fraction solves at many rational v, q = v^2; q-rational
     reconstruction) — expected inhomogeneous order 1 (the trefoil
     A-polynomial is linear in L), with order-2 fallback.
  3. VERIFY: exact symbolic annihilation (symbolic q) for N = 1..N_VERIFY.
  4. SPECIALIZE q -> 1: compare the homogeneous part against the classical
     trefoil A-polynomial references {1 + L M^6, L + M^6} (chirality pair,
     CCGLS) under the convention maps m -> M and m -> M^2, up to an L-free
     factor in M (the allowed AJ unit).

Audit-only; no production wiring.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE / "substrate"))
sys.path.insert(0, str(_HERE))

import sympy as sp

from aj_figure_eight_operator_construct_verify import (  # noqa: E402
    nullspace_modp, P,
)

q = sp.symbols("q")
m = sp.symbols("m")
L = sp.symbols("L")
M = sp.symbols("M")
w = sp.symbols("w")

N_VERIFY_SYMBOLIC = 10
DEG_Q = 10
V_SAMPLES = [Fraction(2), Fraction(3), Fraction(3, 2), Fraction(5, 2),
             Fraction(4), Fraction(5, 3), Fraction(7, 3), Fraction(5),
             Fraction(7, 2), Fraction(4, 3), Fraction(9, 4), Fraction(7, 4),
             Fraction(8, 3), Fraction(9, 2), Fraction(11, 4), Fraction(6),
             Fraction(10, 3), Fraction(11, 5), Fraction(13, 6), Fraction(12, 5),
             Fraction(13, 4), Fraction(7)]


# ---------- tower --------------------------------------------------------------

def qint(k: int, vv):
    """[k]_v = (v^k - v^-k)/(v - v^-1), exact for Fraction or sympy vv."""
    num = vv**k - vv**(-k)
    den = vv - vv**(-1)
    return num / den


def jones_trefoil(N: int, ww, sign_mode: str, framing: int):
    """J_N(T(2,3)) at w = ww (Fraction or sympy; q = w^4), convention flags."""
    n = N - 1
    vv = ww ** 2
    total = 0
    for j in range(0, n + 1):
        eps = (-1) ** (n - j) if sign_mode == "n-j" else (-1) ** j
        T = eps * ww ** (2 * j * (j + 1) - n * (n + 2))
        total = total + T**3 * qint(2 * j + 1, vv)
    theta_corr = ww ** (framing * n * (n + 2))
    return theta_corr * total / qint(N, vv)


def pick_convention():
    """Scan the convention set; return the unique one passing all anchors."""
    jones_31 = sp.expand(-q**(-4) + q**(-3) + q**(-1))   # left-handed V(3_1)
    jones_31m = sp.expand(jones_31.subs(q, 1 / q))       # mirror
    winners = []
    for sign_mode in ("n-j", "j"):
        for framing in (-3, 3):
            J1 = sp.simplify(jones_trefoil(1, w, sign_mode, framing))
            if sp.simplify(J1 - 1) != 0:
                continue
            J2w = sp.simplify(sp.factor(jones_trefoil(2, w, sign_mode, framing)))
            J2q = sp.expand(sp.simplify(J2w.subs(w, q ** sp.Rational(1, 4))))
            for chir, ref in (("left", jones_31), ("right", jones_31m)):
                if sp.simplify(J2q - ref) == 0:
                    winners.append((sign_mode, framing, chir))
    return winners


# ---------- generic exact solver pieces (ORDER-parameterized) ------------------

def unknowns_for(window, order):
    degs = list(window)
    us = []
    for j in range(order + 1):
        us += [(j, d) for d in degs]
    us += [("b", d) for d in degs]
    return us


def build_rows(J, mpow, unknown_list, nmax, order):
    rows = []
    for N in range(1, nmax - order + 1):
        row = []
        for u in unknown_list:
            j, d = u
            if j == "b":
                row.append(-mpow(N, d))
            else:
                row.append(mpow(N, d) * J[N + j])
        rows.append(row)
    return rows


def solve_unique_exact(rows):
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
    x = [Fraction(0)] * ncols
    x[fc] = Fraction(1)
    for (pr, pc) in pivots:
        x[pc] = -A[pr][fc]
    piv0 = next(t for t in x if t != 0)
    return [t / piv0 for t in x]


def main() -> int:
    t0 = time.monotonic()
    print("\n  AJ verification for the trefoil T(2,3): tower -> operator -> verify -> q->1\n")

    # ---- step 0: convention anchoring ----------------------------------------
    winners = pick_convention()
    print(f"  [conventions] surviving (sign, framing, chirality): {winners}")
    if len(winners) != 1:
        print("  ABORT: convention scan did not isolate exactly one candidate")
        return 1
    sign_mode, framing, chir = winners[0]

    # even-v-power sanity for a few N (tower lies in Z[q^{+-1}])
    def tower_q_symbolic(N: int):
        Jw = sp.simplify(sp.factor(jones_trefoil(N, w, sign_mode, framing)))
        Jq = sp.expand(sp.simplify(Jw.subs(w, q ** sp.Rational(1, 4))))
        return sp.expand(Jq)
    Jsym = {N: tower_q_symbolic(N) for N in range(1, N_VERIFY_SYMBOLIC + 3)}
    stray_sqrt = any(("sqrt" in str(Jsym[N])) or ("/4" in str(Jsym[N]))
                     or ("/2" in str(Jsym[N])) for N in range(1, 6))
    print(f"  [tower] J_N in Z[q^(+-1)] (no fractional q-powers), N<=5?  {not stray_sqrt}")
    if stray_sqrt:
        return 1

    # ---- step 1: minimal window via GF(p) (v-samples, q=v^2) ------------------
    def jones_frac(ww: Fraction, Nmax: int):
        return {N: jones_trefoil(N, ww, sign_mode, framing) for N in range(1, Nmax + 1)}

    v0 = Fraction(2)
    found = None
    for order in (1, 2):
        for size in range(2, 10):
            for lo in range(-size, 1):
                window = range(lo, lo + size)
                us = unknowns_for(window, order)
                nmax = (order + 2) * size + 12
                Jf = jones_frac(v0, nmax + order)
                qv_num = (v0.numerator ** 4) % P
                qv_den = (v0.denominator ** 4) % P
                qv = qv_num * pow(qv_den, P - 2, P) % P
                Jp = {N: (Jf[N].numerator % P) * pow(Jf[N].denominator % P, P - 2, P) % P
                      for N in Jf}
                def mpow(N, d, qv=qv):
                    return pow(qv, N * d, P) if d >= 0 else pow(pow(qv, P - 2, P), N * (-d), P)
                rows = build_rows(Jp, mpow, us, nmax, order)
                ns = nullspace_modp(rows)
                if len(ns) == 1:
                    found = (order, window, us)
                    print(f"  [window] minimal: order {order}, m-degrees "
                          f"[{min(window)}..{max(window)}] (nullity 1 mod p)")
                    break
            if found:
                break
        if found:
            break
    if not found:
        print("  [window] no nullity-1 window found — abort")
        return 1
    order, window, us = found
    size = len(list(window))
    nmax = (order + 2) * size + 12

    # ---- step 2: exact per-q solves -------------------------------------------
    per_q = {}
    for vv in V_SAMPLES:
        qv = Fraction(vv.numerator**4, vv.denominator**4)
        J = jones_frac(vv, nmax + order)
        def mpowf(N, d, qv=qv):
            return qv ** (N * d)
        rows = build_rows(J, mpowf, us, nmax, order)
        sol = solve_unique_exact(rows)
        if sol is None:
            print(f"  [exact] v={vv}: nullity != 1 — abort")
            return 1
        per_q[qv] = dict(zip(us, sol))
    print(f"  [exact] solved at {len(V_SAMPLES)} exact rational q = v^2 values "
          f"({time.monotonic()-t0:.0f}s)")

    # ---- step 3: reconstruct q-rational coefficients --------------------------
    qs = list(per_q.keys())
    coeff_fns = {}
    for u in us:
        vals = [sp.Rational(per_q[qv][u].numerator, per_q[qv][u].denominator)
                for qv in qs]
        if all(x == 0 for x in vals):
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
    a = {j: assemble(j) for j in range(order + 1)}
    b = assemble("b")
    print(f"\n  reconstructed operator (sum_j a_j J_(N+j) = b, order {order}):")
    for j in range(order + 1):
        print(f"    a{j}(q,m) = {sp.factor(sp.simplify(a[j]))}")
    print(f"    b(q,m)  = {sp.factor(sp.simplify(b))}")

    # ---- step 4: exact symbolic verification ----------------------------------
    ver_ok = {}
    for N in range(1, N_VERIFY_SYMBOLIC + 1):
        mv = q**N
        lhs = sum(a[j].subs(m, mv) * Jsym[N + j] for j in range(order + 1))
        resid = sp.cancel(sp.together(lhs - b.subs(m, mv)))
        ver_ok[N] = (sp.simplify(resid) == 0)
        if not ver_ok[N]:
            print(f"  [verify] N={N}: RESIDUAL != 0")
    all_ver = all(ver_ok.values())
    print(f"\n  [verify] symbolic annihilation N=1..{N_VERIFY_SYMBOLIC}?  {all_ver}"
          f"  ({time.monotonic()-t0:.0f}s)")
    if not all_ver:
        return 1

    # ---- step 5: q -> 1 vs classical trefoil A-polynomial ---------------------
    A_refs = {"1+L*M^6": 1 + L * M**6, "L+M^6": L + M**6}
    spec_results = {}
    any_match = False
    for name, msub in (("m->M", M), ("m->M^2", M**2)):
        op_cl = sp.Integer(0)
        ok = True
        for j in range(order + 1):
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
        entry = {"classical_limit": str(op_cl)}
        for rname, ref in A_refs.items():
            ratio = sp.cancel(op_cl / ref)
            num_, den_ = sp.fraction(sp.together(ratio))
            unit_match = (not num_.has(L)) and (not den_.has(L)) and \
                sp.simplify(sp.expand(op_cl * den_ - ref * num_)) == 0
            entry[rname] = {"ratio": str(sp.cancel(ratio)),
                            "matches_up_to_L_free_M_factor": bool(unit_match)}
            if unit_match:
                any_match = True
            print(f"  [q->1, {name} vs {rname}] ratio = {sp.cancel(ratio)} "
                  f"(L-free factor match: {unit_match})")
        spec_results[name] = entry

    elapsed = time.monotonic() - t0
    verdict = (
        (f"AJ VERIFIED for the trefoil (corpus-side): the minimal-window order-{order} "
         "inhomogeneous operator annihilates J_N(T(2,3)) exactly (symbolic q, "
         f"N=1..{N_VERIFY_SYMBOLIC}) and its q->1 homogeneous part matches the classical "
         "trefoil A-polynomial up to an L-free factor in M.")
        if any_match else
        ("PARTIAL: operator constructed + symbolically verified as annihilator; "
         "q->1 L-free-factor match did not close under the standard convention "
         "maps/chirality references — record for convention triage.")
    )
    print(f"\n  VERDICT: {verdict}\n  ({elapsed:.1f}s)")

    payload = {
        "description": (
            "Trefoil quantum A-polynomial: Rosso-Jones tower (self-anchored "
            "conventions), minimal-window exact construction of the annihilator, "
            "exact symbolic verification, q->1 specialization vs the classical "
            "trefoil A-polynomial (AJ verification at the QOU electron knot)."
        ),
        "computation": "aj_trefoil_operator_construct_verify",
        "audit_only": True,
        "context": {
            "literature": "AJ for two-bridge knots [garoufalidis2004] / Le 2006; trefoil = T(2,3)",
            "sibling": "computations/aj_figure_eight_operator_construct_verify.py",
            "classical_A_poly_refs": {k: str(x) for k, x in A_refs.items()},
        },
        "conventions": {"sign_mode": sign_mode, "framing": framing, "chirality": chir},
        "operator": {
            "order": order,
            "window": [min(window), max(window)],
            **{f"a{j}": str(sp.factor(sp.simplify(a[j]))) for j in range(order + 1)},
            "b": str(sp.factor(sp.simplify(b))),
        },
        "verification": {
            "symbolic_annihilation_N": {str(N): bool(x) for N, x in ver_ok.items()},
            "all_verified": bool(all_ver),
        },
        "specialization_q_to_1": spec_results,
        "verdict": verdict,
        "tier": "structural-exact annihilation; convention-sorted L-free-factor match at q=1",
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "aj-trefoil-operator-construct-verify", payload,
        script_path=__file__, engine="sympy",
        engine_version=sp.__version__, start_time=t0,
    ).save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
