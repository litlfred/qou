#!/usr/bin/env python3
"""Plancherel-functional coproduct density `u` on H_n(q) vs the refuted co-Casimir Δ_λ.

Owner-approved exploration (item 4, branch claude/frobenius-counit-axiom2-2026-10-13).

Setup (re-derived and checked below, exact arithmetic over Q(q)):

  H_n(q) generic semisimple  =>  A = ⊕_λ M_{d_λ},  d_λ = f^λ (classical SYT count).
  A Frobenius-compatible coproduct is fixed by
      Δ(1) = Σ_λ c_λ Σ_{ij} E^λ_ij ⊗ E^λ_ji ,   Δ(a) = (a⊗1)Δ(1) = Δ(1)(1⊗a).
  If the counit is ε = Σ_λ ε_λ χ_λ (ε(E^λ_ij) = ε_λ δ_ij), the counit law forces
  c_λ = 1/ε_λ (needs ε_λ ≠ 0 on every block).
  With the integral ∫ = tr_M = Σ_λ y_λ χ_λ (convention D, z = q³/(q²+1),
  normalisation Σ_λ y_λ f^λ = 1), the induced density is
      u := (∫⊗id)Δ(1) = Σ_λ (y_λ/ε_λ) p_λ ,
  and m(ϱ) = |∫(u·ϱ)| = |Σ_λ y_λ χ_λ(ϱ) · u_λ|, i.e. the EFFECTIVE Δ_λ is
      Δ_λ^{eff} = u_λ = y_λ / ε_λ          (NOT y_λ²·…; y_λ² is the summand y_λ·u_λ).

Counit choices examined (none selected by agreement with any target):
  (a)  ε = tr_M                        -> ε_λ = y_λ.  Under D, y_λ = 0 on every
       three-row block for n ≥ 3, so c_λ = 1/0: NO counit exists on H_n with this ε;
       only on the quotient H_n/rad (TL_n), where u = 1.
  (b)  ε = τ_P, the UNWEIGHTED PLANCHEREL FUNCTIONAL, as written in the corpus at
       mass-theory/frobenius-codim-universal.lean (docstring of
       frobenius_codim_tau_invariant):  τ_P(p_λ) = dim_q(λ)·d_λ/[n]_q!,
       dim_q(λ) = [n]_q!/Π_x [h(x)]_q (balanced).  ε_λ = dim_q(λ)/[n]_q!.
  (bκ) the CANONICAL TRACE: the same with the q^{-κ_λ} content factor that the corpus's
       QOU/MathlibExt/MolienFakeDegree.lean carries (Σ f^λ q^{-κ_λ} dim_q = [n]_q!,
       proved n=2,3,4): ε_λ = q^{-κ_λ} dim_q(λ)/[n]_q!.  This probe checks
       symbolically (n=2,3,4) that (bκ) IS the canonical trace τ(T_w) = δ_{w,1}
       and that (b) is NOT — a structural fact, not agreement with data.

Tests reported:
  (i)   is Δ^{(b)} ∝ co-Casimir 1/dim_q (ratio constant in λ)?
  (ii)  sign pattern vs the proved signed value Δ_λ = (-1)^{n(λ)} f^λ.
  (iii) the deuteron test of QOU.BraidKnot.DeltaLambdaRefutation
        (tol < |Σ y χ Δ − target|, and sign), χ_λ(β_D) taken verbatim from
        computations/rho-k-h3a-co-casimir.witness.json (60-digit strings).
  (iv)  three-row blocks: y = 0 ⇒ u = 0 there.

NO float anywhere in the computation.  Symbolic algebra in sympy over Q(q);
evaluation at the proton pin by exact Rational substitution; display / the
deuteron sum (whose χ input is a decimal string) in mpmath at 70 dps.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import itertools  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from y_lambda_su_n import (  # noqa: E402
    y_lambda_su_n_symbolic, partitions_of, f_lambda, q_int_sym)

mp.mp.dps = 70
HERE = Path(__file__).resolve().parent
COMP = HERE.parent
q = sp.Symbol("q", positive=True)

try:
    from qou_substrate.constants import Q_50_DIGIT_STR as _QSTR
except Exception:  # corpus accessor unavailable -> refuse rather than guess
    sys.path.insert(0, str(COMP.parent / "tools/qou-substrate/python"))
    from qou_substrate.constants import Q_50_DIGIT_STR as _QSTR
Q0_RAT = sp.Rational(_QSTR)          # exact rational of the 50-digit proton pin

PASS = FAIL = 0


def check(label, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def is_zero(e):
    return sp.cancel(sp.together(e)) == 0


def at_q0(e) -> mp.mpf:
    v = sp.cancel(sp.together(sp.sympify(e))).subs(q, Q0_RAT)
    v = sp.Rational(v)
    return mp.mpf(v.p) / mp.mpf(v.q)


# ── combinatorics ─────────────────────────────────────────────────────
def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def conj(lam):
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0]))


def hook(lam, i, j):
    lc = conj(lam)
    return (lam[i] - j - 1) + (lc[j] - i - 1) + 1


def kappa(lam):
    return sum(j - i for i, j in cells(lam))


def n_stat(lam):
    return sum(i * r for i, r in enumerate(lam))


def qfact(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= q_int_sym(k, q)
    return sp.cancel(r)


def dim_q(lam):
    """Corpus convention: [n]_q!/Π[h]_q, balanced (computations/substrate/young_qdim.py)."""
    den = sp.Integer(1)
    for (i, j) in cells(lam):
        den *= q_int_sym(hook(lam, i, j), q)
    return sp.cancel(qfact(sum(lam)) / den)


# ── seminormal representations of H_n(q), σ² = (q−q⁻¹)σ + 1 ─────────────
def syt(lam):
    n = sum(lam)
    out = []

    def rec(t, k):
        if k > n:
            out.append(tuple(tuple(r) for r in t))
            return
        for i in range(len(lam)):
            if len(t[i]) < lam[i] and (i == 0 or len(t[i - 1]) > len(t[i])):
                t[i].append(k)
                rec(t, k + 1)
                t[i].pop()
    rec([[] for _ in lam], 1)
    return out


def pos(T, k):
    for i, r in enumerate(T):
        if k in r:
            return i, r.index(k)


def swap(T, a, b):
    return tuple(tuple(b if x == a else a if x == b else x for x in r) for r in T)


def gen_matrix(lam, i):
    Ts = syt(lam)
    idx = {T: k for k, T in enumerate(Ts)}
    M = sp.zeros(len(Ts), len(Ts))
    for T in Ts:
        (r1, c1), (r2, c2) = pos(T, i), pos(T, i + 1)
        k = idx[T]
        if r1 == r2:
            M[k, k] = q
        elif c1 == c2:
            M[k, k] = -1 / q
        else:
            a = (c2 - r2) - (c1 - r1)
            qa = q_int_sym(abs(a), q) * (1 if a > 0 else -1)
            M[k, k] = sp.cancel(q ** a / qa)
            k2 = idx[swap(T, i, i + 1)]
            M[k, k2] = 1 if a > 0 else sp.cancel(1 - 1 / qa ** 2)
    return M


def simp(M):
    return M.applyfunc(lambda e: sp.cancel(sp.together(e)))


def reps(n):
    return {lam: [gen_matrix(lam, i) for i in range(1, n)] for lam in partitions_of(n)}


def reduced_words(n):
    """One reduced word per permutation of S_n (BFS on length)."""
    start = tuple(range(n))
    seen = {start: ()}
    frontier = [start]
    while frontier:
        nxt = []
        for p in frontier:
            for i in range(n - 1):
                if p[i] < p[i + 1]:
                    pp = list(p)
                    pp[i], pp[i + 1] = pp[i + 1], pp[i]
                    pp = tuple(pp)
                    if pp not in seen:
                        seen[pp] = seen[p] + (i,)
                        nxt.append(pp)
        frontier = nxt
    return list(seen.values())


def word_matrix(R, w, d):
    M = sp.eye(d)
    for i in w:
        M = M * R[i]
    return simp(M)


# ── Part 1: verify the Hecke reps, Markov trace (D) and canonical trace ──
def verify_traces(n):
    print(f"\n-- n = {n}: Hecke relations, Markov (conv D) and canonical-trace checks")
    R = reps(n)
    y = y_lambda_su_n_symbolic(n, q, 2)
    z = sp.cancel(q ** 3 / (q ** 2 + 1))
    ok = True
    for lam, gens in R.items():
        d = gens[0].shape[0] if gens else 1
        for g in gens:
            ok &= simp(g * g - (q - 1 / q) * g - sp.eye(d)).is_zero_matrix
        for a in range(len(gens) - 1):
            g, h = gens[a], gens[a + 1]
            ok &= simp(g * h * g - h * g * h).is_zero_matrix
    check(f"n={n}: seminormal matrices satisfy Hecke + braid relations", ok)
    check(f"n={n}: Σ_λ y_λ f^λ = 1",
          is_zero(sum(y[l] * f_lambda(l) for l in y) - 1))
    words = reduced_words(n)

    def trace_fn(weights, w):
        tot = sp.Integer(0)
        for lam, gens in R.items():
            d = len(syt(lam))
            tot += weights[lam] * word_matrix(gens, w, d).trace()
        return sp.cancel(sp.together(tot))

    # Markov: tr(x σ_{n-1}) = z tr(x) for x in H_{n-1} basis
    words_sub = [w for w in words if all(i < n - 2 for i in w)]
    mk = all(is_zero(trace_fn(y, w + (n - 2,)) - z * trace_fn(y, w)) for w in words_sub)
    check(f"n={n}: tr_M = Σ y_λ χ_λ is Markov with z = q³/(q²+1) on all "
          f"{len(words_sub)} x∈H_{n-1} basis words", mk)
    eps_b = {l: sp.cancel(dim_q(l) / qfact(n)) for l in R}
    eps_bk = {l: sp.cancel(q ** (-kappa(l)) * dim_q(l) / qfact(n)) for l in R}
    canon_bk = all(is_zero(trace_fn(eps_bk, w) - (1 if len(w) == 0 else 0)) for w in words)
    check(f"n={n}: (bκ) Σ q^-κ dim_q/[n]! χ_λ is the canonical trace "
          f"τ(σ_w)=δ_w,1 on all {len(words)} reduced words", canon_bk)
    canon_b = all(is_zero(trace_fn(eps_b, w) - (1 if len(w) == 0 else 0)) for w in words)
    check(f"n={n}: (b) unweighted Plancherel functional τ_P (no κ) is NOT the canonical trace "
          f"[structural fact recorded, not a selection]", not canon_b)
    t_b1 = trace_fn(eps_b, ())
    return {"n": n, "markov_D": mk, "canonical_bkappa": canon_bk,
            "canonical_b": canon_b, "tau_P_b_of_1": str(sp.factor(t_b1)),
            "tau_P_b_of_1_at_q0": mp.nstr(at_q0(t_b1), 20)}


# ── Part 2: coproduct axioms on abstract matrix units ──────────────────
def verify_coproduct(n, eps, tag):
    lams = partitions_of(n)
    d = {l: f_lambda(l) for l in lams}
    if any(is_zero(eps[l]) for l in lams):
        zeros = [l for l in lams if is_zero(eps[l])]
        print(f"  ({tag}) ε_λ = 0 on {zeros}: c_λ = 1/ε_λ undefined -> no counit on H_{n}")
        return False
    c = {l: sp.cancel(1 / eps[l]) for l in lams}
    units = [(l, i, j) for l in lams for i in range(d[l]) for j in range(d[l])]

    def mul(a, b):  # matrix-unit product, returns unit or None
        return (a[0], a[1], b[2]) if a[0] == b[0] and a[2] == b[1] else None

    D1 = {((l, i, j), (l, j, i)): c[l] for l in lams
          for i in range(d[l]) for j in range(d[l])}

    def Delta(a):  # (a⊗1)Δ(1)
        out = {}
        for (x, y_), v in D1.items():
            ax = mul(a, x)
            if ax is not None:
                out[(ax, y_)] = out.get((ax, y_), 0) + v
        return out

    def eps_of(x):
        return eps[x[0]] if x[1] == x[2] else 0

    ok = True
    for a in units:
        Da = Delta(a)
        left, right = {}, {}
        for (x, y_), v in Da.items():
            left[y_] = sp.cancel(left.get(y_, 0) + eps_of(x) * v)
            right[x] = sp.cancel(right.get(x, 0) + eps_of(y_) * v)
        tgt = {a: 1}
        for dct in (left, right):
            keys = set(dct) | set(tgt)
            ok &= all(is_zero(dct.get(k, 0) - tgt.get(k, 0)) for k in keys)
        # Frobenius relation (a⊗1)Δ(1) = Δ(1)(1⊗a)
        rhs = {}
        for (x, y_), v in D1.items():
            ya = mul(y_, a)
            if ya is not None:
                rhs[(x, ya)] = rhs.get((x, ya), 0) + v
        keys = set(Da) | set(rhs)
        ok &= all(is_zero(Da.get(k, 0) - rhs.get(k, 0)) for k in keys)
    # coassociativity on Δ(1)
    L, Rr = {}, {}
    for (x, y_), v in D1.items():
        for (x1, x2), w in Delta(x).items():
            L[(x1, x2, y_)] = L.get((x1, x2, y_), 0) + v * w
        for (y1, y2), w in Delta(y_).items():
            Rr[(x, y1, y2)] = Rr.get((x, y1, y2), 0) + v * w
    keys = set(L) | set(Rr)
    ok &= all(is_zero(L.get(k, 0) - Rr.get(k, 0)) for k in keys)
    check(f"n={n} ({tag}): counit law (both sides), Frobenius relation, "
          f"coassociativity on all {len(units)} matrix units", ok)
    # density u = (∫⊗id)Δ(1) with ∫ = tr_M
    y = y_lambda_su_n_symbolic(n, q, 2)
    u = {}
    for (x, y_), v in D1.items():
        if x[1] == x[2]:
            u[y_] = u.get(y_, 0) + y[x[0]] * v
    okd = all(is_zero(u.get((l, i, j), 0) - (sp.cancel(y[l] / eps[l]) if i == j else 0))
              for (l, i, j) in units)
    check(f"n={n} ({tag}): u = (tr_M⊗id)Δ(1) = Σ_λ (y_λ/ε_λ) p_λ", okd)
    return ok and okd


# ── Part 3: tables n = 2..6 ─────────────────────────────────────────────
def table(n):
    lams = partitions_of(n)
    y = y_lambda_su_n_symbolic(n, q, 2)
    F = qfact(n)
    rows = []
    for l in lams:
        dq = dim_q(l)
        ub = sp.cancel(y[l] * F / dq)
        ubk = sp.cancel(y[l] * q ** kappa(l) * F / dq)
        rows.append({
            "lambda": list(l), "d_lambda": f_lambda(l), "kappa": kappa(l),
            "n_lambda": n_stat(l),
            "dim_q": str(sp.factor(dq)), "y_D": str(sp.factor(y[l])),
            "u_b": str(sp.factor(ub)), "u_bkappa": str(sp.factor(ubk)),
            "ratio_u_b_over_cocasimir": str(sp.factor(sp.cancel(ub * dq))),
            "signed_target_value": (-1) ** n_stat(l) * f_lambda(l),
            "at_q0": {k: mp.nstr(at_q0(e), 15) for k, e in
                      (("dim_q", dq), ("y_D", y[l]), ("cocasimir", 1 / dq),
                       ("u_b", ub), ("u_bkappa", ubk))},
            "_sym": (dq, y[l], ub, ubk),
        })
    return rows


def main():
    print("Plancherel-functional coproduct density u vs co-Casimir 1/dim_q (conv D, exact)")
    print(f"proton pin q0 = {_QSTR}")
    trace_checks = [verify_traces(n) for n in (2, 3, 4)]

    print("\n-- coproduct axioms (abstract ⊕ M_{d_λ}, exact over Q(q))")
    cop = {}
    for n in (2, 3):
        y = y_lambda_su_n_symbolic(n, q, 2)
        cop[f"n{n}_a_trM"] = verify_coproduct(n, {l: y[l] for l in y}, "a: ε=tr_M")
        cop[f"n{n}_b"] = verify_coproduct(
            n, {l: sp.cancel(dim_q(l) / qfact(n)) for l in y}, "b: ε=τ_P")
        cop[f"n{n}_bkappa"] = verify_coproduct(
            n, {l: sp.cancel(q ** (-kappa(l)) * dim_q(l) / qfact(n)) for l in y},
            "bκ: ε=canonical")
    check("n=2 (a) ε=tr_M admits a counit (y_λ ≠ 0 at n=2)", cop["n2_a_trM"])
    check("n=3 (a) ε=tr_M admits NO counit on H_3 (y_(1³)=0 under D)",
          not cop["n3_a_trM"])

    tables = {}
    print("\n-- per-λ tables at q0 (exact symbolic in witness)")
    for n in range(2, 7):
        rows = table(n)
        tables[n] = rows
        print(f"\n n={n}  {'λ':<14}{'d':>4}{'dim_q':>12}{'y_D':>14}"
              f"{'1/dim_q':>12}{'u_b':>14}{'u_bκ':>14}{'(-1)^nλ f':>10}")
        for r in rows:
            a = r["at_q0"]
            print(f"      {str(tuple(r['lambda'])):<14}{r['d_lambda']:>4}"
                  f"{a['dim_q']:>12.10}{a['y_D']:>14.10}{a['cocasimir']:>12.10}"
                  f"{a['u_b']:>14.10}{a['u_bkappa']:>14.10}{r['signed_target_value']:>10}")
        # (i) proportionality: ratio u_b·dim_q = y_λ [n]! constant over λ?
        ratios = [sp.cancel(r["_sym"][2] * r["_sym"][0]) for r in rows]
        live = [x for x in ratios if not is_zero(x)]
        const = all(is_zero(x - live[0]) for x in live)
        r["_const"] = const
        print(f"  n={n} (i) u_b ∝ 1/dim_q over the {len(live)} live (y≠0) blocks? -> {const}"
              f"   ratio u_b·dim_q = y_λ[n]_q! (recorded, not asserted)")
        # (ii) sign: u_b, u_bκ ≥ 0 at q0 on every block
        nonneg = all(at_q0(r["_sym"][2]) >= 0 and at_q0(r["_sym"][3]) >= 0 for r in rows)
        check(f"n={n} (ii) u_b, u_bκ ≥ 0 on every block at q0", nonneg)
        # (iv) three-row blocks vanish
        three = [r for r in rows if len(r["lambda"]) >= 3]
        check(f"n={n} (iv) u_b = u_bκ = 0 on all {len(three)} ≥3-row blocks",
              all(is_zero(r["_sym"][2]) and is_zero(r["_sym"][3]) for r in three))

    # ── (iii) deuteron test (n = 6) ──
    print("\n-- (iii) deuteron test of QOU.BraidKnot.DeltaLambdaRefutation (n=6)")
    W = json.load(open(COMP / "rho-k-h3a-co-casimir.witness.json"))
    chi = {tuple(r["partition"]): mp.mpf(r["chi_lambda_beta_D_at_q0"])
           for r in W["data"]["per_lambda"]}
    yw = {tuple(r["partition"]): mp.mpf(r["y_lambda_at_q0"])
          for r in W["data"]["per_lambda"]}
    target = mp.mpf(W["data"]["target_signed"])
    tol = mp.mpf(1)
    rows6 = {tuple(r["lambda"]): r for r in tables[6]}
    ydiff = max(abs(at_q0(rows6[l]["_sym"][1]) - yw[l]) for l in rows6)
    check(f"exact y_λ(conv D) at q0 matches witness y_λ (max |Δ| = {mp.nstr(ydiff, 3)})",
          ydiff < mp.mpf("1e-40"))
    sums = {}
    for key, k in (("cocasimir", None), ("u_b", 2), ("u_bkappa", 3)):
        s = mp.mpf(0)
        for l, r in rows6.items():
            D = 1 / at_q0(r["_sym"][0]) if k is None else at_q0(r["_sym"][k])
            s += at_q0(r["_sym"][1]) * chi[l] * D
        sums[key] = s
    signed = mp.mpf(0)
    for l, r in rows6.items():
        signed += at_q0(r["_sym"][1]) * chi[l] * r["signed_target_value"]
    sums["signed_value_(-1)^n f"] = signed
    wit_cc = mp.mpf(W["data"]["co_casimir_prediction"]["sum_contributions_signed"])
    check(f"co-Casimir sum reproduces witness ({mp.nstr(wit_cc, 15)})",
          abs(sums["cocasimir"] - wit_cc) < mp.mpf("1e-40"))
    verdict3 = {}
    for k, s in sums.items():
        gap = abs(s - target)
        verdict3[k] = {"sum": mp.nstr(s, 20), "gap": mp.nstr(gap, 20),
                       "refuted_by_tol": bool(gap > tol),
                       "wrong_sign": bool(s > 0 and target < 0)}
        print(f"  {k:<22} Σ yχΔ = {mp.nstr(s, 15):>22}   |gap| = {mp.nstr(gap, 12):>18}"
              f"  > tol? {gap > tol}   wrong sign? {s > 0}")
    print(f"  target (−B_D/m_e)      = {mp.nstr(target, 15)}   tol = 1")

    print(f"\nPASS {PASS} / FAIL {FAIL}")
    out = {
        "computation": "plancherel-density-u-probe",
        "description": ("Density u=(tr_M⊗id)Δ(1) induced by the Frobenius coproduct "
                        "with counit ε (a: tr_M, b: corpus τ_P, bκ: canonical trace) "
                        "on H_n(q), convention D; compared with the refuted co-Casimir "
                        "Δ_λ=1/dim_q. Exact Q(q) arithmetic; q0 = proton pin."),
        "q0_anchor": "proton", "q0Value": _QSTR,
        "trace_checks": trace_checks, "coproduct_checks": cop,
        "tables": {str(n): [{k: v for k, v in r.items() if not k.startswith("_")}
                            for r in rows] for n, rows in tables.items()},
        "deuteron_test": {"target_signed": mp.nstr(target, 30), "tol": "1",
                          "results": verdict3,
                          "chi_source": "rho-k-h3a-co-casimir.witness.json"},
        "assertions_pass": PASS, "assertions_fail": FAIL, "allPassed": FAIL == 0,
    }
    path = HERE / "plancherel-density-u.witness.json"
    try:
        from qou_substrate.witness import WitnessBuilder as _WB
        out.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(out, script_path=__file__, engine=None,
                                     q0_anchor="proton")
    except Exception as exc:  # provenance stamp is best-effort
        print(f"  (provenance stamp skipped: {exc})")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(f"witness -> {path}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
