#!/usr/bin/env python3
"""knot_factor_binding_half_probe.py — the knot factor kappa and the binding half of
conj:knot-factor-frobenius-pairing (issue #8960, item 5).

PROBE, adopts nothing.  Exact arithmetic only (sympy rational functions of q); no
floats, no number at q0, no AME.

Conventions (AGENTS.md): sigma^2 = h sigma + 1, h = q - q^-1 (eigenvalues q, -q^-1);
Markov trace tr(x sigma_{n-1} y) = z tr(x y), tr(1) = 1, z = z_D = q^3/(q^2+1);
symmetrizing trace tau(sigma_w) = delta_{w,1}.  The knot factor is the unique
kappa with tr(x) = tau(x kappa) for all x  (QOU.Hecke.KnotFactor), and
kappa = sum_lambda y_lambda s_lambda e_lambda.

Part 1  kappa for n = 2, 3, 4 in the sigma_w basis (kappa = G^-1 t with
        G_{v,w} = tau(sigma_v sigma_w), t_v = tr(sigma_v)), its centrality, and
        its block scalars y_lambda s_lambda (seminormal characters).
Part 2  the binding half, three readings of "free trace minus convolved trace":
  R1  B/E0 = tr(W_free) - tr(W_atom) = tau((W_free - W_atom) kappa).
      Linearity of tau; holds for every pair of words in the same H_n (signs
      aside: the block uses |tr|).
  R2  free = product of the constituents' Markov traces on the parabolic
      H_a (x) H_b, with knot factor kappa_a (x) kappa_b; atom = tr on H_{a+b}.
      Claim tested: the tau-projection of kappa_{a+b} onto the parabolic span
      is kappa_a (x) kappa_b, hence tau(x (kappa_free - kappa_atom)) = 0 for every
      x in the parabolic, in particular x = W_free.
  R3  atom = the bond-convolved functional t_b(x) = tr(x b) (W_atom = W_free b,
      appended form).  Its pairing element is b kappa; t_b is a trace iff
      b kappa is central iff rho_lambda(b) is scalar on every block with
      y_lambda != 0.  Tested for the gamma-gamma bond b = (s_i s_{i+1}^-1)^3.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(COMP))
from y_lambda_su_n import y_lambda_su_n_symbolic  # noqa: E402

T0 = time.time()
q = sp.symbols("q", positive=True)
h = q - 1 / q
zD = q**3 / (q**2 + 1)


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def simp(e):
    return sp.factor(sp.cancel(sp.together(e)))


# ---------------------------------------------------------------- permutations
def compose(a, b):  # (a*b)(k) = a(b(k)), tuples on 0..n-1
    return tuple(a[b[k]] for k in range(len(a)))


def sgen(i, n):  # 1-based generator s_i swaps i-1, i (0-based positions)
    p = list(range(n))
    p[i - 1], p[i] = p[i], p[i - 1]
    return tuple(p)


def length(p):
    return sum(1 for a in range(len(p)) for b in range(a + 1, len(p)) if p[a] > p[b])


def reduced_word(p):
    """Reduced word (list of 1-based generators) with sigma_p = prod."""
    p = list(p)
    word = []
    n = len(p)
    # bubble sort from the right: p = w; find descent
    while True:
        for i in range(1, n):
            if p[i - 1] > p[i]:
                # p = p' * s_i  with l(p') = l(p) - 1
                p[i - 1], p[i] = p[i], p[i - 1]
                word.append(i)
                break
        else:
            break
    return list(reversed(word))


# ---------------------------------------------------------------- Hecke algebra
def mul_gen_left(i, x, n):
    """sigma_i * x, x a dict perm -> coeff."""
    s = sgen(i, n)
    out = {}
    for w, c in x.items():
        sw = compose(s, w)
        if length(sw) > length(w):
            out[sw] = out.get(sw, 0) + c
        else:
            out[w] = out.get(w, 0) + h * c
            out[sw] = out.get(sw, 0) + c
    return out


def basis_elem(w):
    return {w: sp.Integer(1)}


def mul(x, y, n):
    out = {}
    for w, c in x.items():
        acc = dict(y)
        for g in reversed(reduced_word(w)):
            acc = mul_gen_left(g, acc, n)
        for k, v in acc.items():
            out[k] = out.get(k, 0) + c * v
    return {k: sp.cancel(v) for k, v in out.items() if sp.cancel(v) != 0}


def markov_basis(w, cache={}):
    """tr(sigma_w), Ocneanu recursion via coset decomposition w = a * s_{n-1}...s_j."""
    n = len(w)
    key = w
    if key in cache:
        return cache[key]
    if n == 1:
        return sp.Integer(1)
    if w[n - 1] == n - 1:
        val = markov_basis(w[: n - 1])
        cache[key] = val
        return val
    # find coset rep c = s_{n-1} s_{n-2} ... s_j with a = w c^-1 in S_{n-1}
    for j in range(n - 1, 0, -1):
        c = tuple(range(n))
        for g in range(n - 1, j - 1, -1):
            c = compose(c, sgen(g, n))
        cinv = tuple(sorted(range(n), key=lambda k: c[k]))
        a = compose(w, cinv)
        if a[n - 1] == n - 1 and length(a) + length(c) == length(w):
            # sigma_w = sigma_a sigma_{n-1} sigma_{s_{n-2}..s_j}; tr = z tr(sigma_a sigma_rest)
            rest = tuple(range(n))
            for g in range(n - 2, j - 1, -1):
                rest = compose(rest, sgen(g, n))
            prod = mul(basis_elem(a), basis_elem(rest), n)
            val = zD * sum(cf * markov_basis(v[: n - 1]) for v, cf in prod.items())
            val = sp.cancel(val)
            cache[key] = val
            return val
    raise RuntimeError("no coset decomposition")


def tau(x, n):
    return x.get(tuple(range(n)), sp.Integer(0))


def trM(x):
    return sp.cancel(sum(c * markov_basis(w) for w, c in x.items()))


def knot_factor(n):
    W = sorted(itertools.permutations(range(n)), key=lambda p: (length(p), p))
    G = sp.Matrix(len(W), len(W), lambda a, b: tau(mul(basis_elem(W[a]), basis_elem(W[b]), n), n))
    t = sp.Matrix([markov_basis(w) for w in W])
    c = G.LUsolve(t)
    kap = {W[k]: simp(c[k]) for k in range(len(W)) if simp(c[k]) != 0}
    return W, kap


# ---------------------------------------------------------------- seminormal reps
def partitions(n, maxp=None):
    maxp = n if maxp is None else maxp
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxp), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def std_tableaux(shape):
    n = sum(shape)
    res = []

    def rec(T, k):
        if k > n:
            res.append({v: pos for pos, v in T.items()} if False else dict(T))
            return
        for r in range(len(shape)):
            row_len = sum(1 for (rr, cc) in T if rr == r)
            if row_len < shape[r] and (r == 0 or sum(1 for (rr, cc) in T if rr == r - 1) > row_len):
                T[(r, row_len)] = k
                rec(T, k + 1)
                del T[(r, row_len)]
    rec({}, 1)
    return [{v: pos for pos, v in T.items()} for T in res]  # value -> (row, col)


def qint(d):
    return (q**d - q**(-d)) / (q - 1 / q)


def seminormal(shape):
    tabs = std_tableaux(shape)
    idx = {tuple(sorted(T.items())): k for k, T in enumerate(tabs)}
    n = sum(shape)
    f = len(tabs)
    mats = {}
    for i in range(1, n):
        M = sp.zeros(f, f)
        for k, T in enumerate(tabs):
            (r1, c1), (r2, c2) = T[i], T[i + 1]
            d = (c2 - r2) - (c1 - r1)
            if r1 == r2:
                M[k, k] = q
            elif c1 == c2:
                M[k, k] = -1 / q
            else:
                M[k, k] = q**d / qint(d)
                T2 = dict(T)
                T2[i], T2[i + 1] = T[i + 1], T[i]
                k2 = idx[tuple(sorted(T2.items()))]
                M[k2, k] = 1 if d > 0 else (1 - 1 / qint(d)**2)
        mats[i] = M.applyfunc(sp.cancel)
    return mats


def rep_of_word(mats, word, f):
    """word: list of (gen, exponent +-1)."""
    M = sp.eye(f)
    for g, e in word:
        X = mats[g] if e == 1 else (mats[g] - h * sp.eye(f))
        M = M * X
    return M.applyfunc(sp.cancel)


def rep_of_elem(mats, x, f):
    out = sp.zeros(f, f)
    for w, c in x.items():
        out += c * rep_of_word(mats, [(g, 1) for g in reduced_word(w)], f)
    return out.applyfunc(sp.cancel)


def main():
    out = {"conventions": "sigma^2 = h sigma + 1, h = q - 1/q; z_D = q^3/(q^2+1); "
                          "tau(sigma_w) = delta_{w,1}; tr(1) = 1"}
    checks = {}

    # ---------- Part 1: kappa ----------
    part1 = {}
    kappas = {}
    for n in (2, 3, 4):
        log(f"knot factor n={n}")
        W, kap = knot_factor(n)
        kappas[n] = kap
        cent = all(
            not mul(basis_elem(sgen(i, n)), kap, n).keys() ^ mul(kap, basis_elem(sgen(i, n)), n).keys()
            and all(sp.cancel(mul(basis_elem(sgen(i, n)), kap, n)[k] - mul(kap, basis_elem(sgen(i, n)), n)[k]) == 0
                    for k in mul(kap, basis_elem(sgen(i, n)), n))
            for i in range(1, n))
        # tr(x) = tau(x kappa) on every basis element
        fact = all(sp.cancel(tau(mul(basis_elem(w), kap, n), n) - markov_basis(w)) == 0 for w in W)
        y = y_lambda_su_n_symbolic(n, q, 2)
        blocks = {}
        kblock = {}
        ytr_ok = True
        tau_ok = True
        for lam in partitions(n):
            mats = seminormal(lam)
            f = len(std_tableaux(lam))
            K = rep_of_elem(mats, kap, f)
            scal = simp(K[0, 0])
            kblock[lam] = scal
            is_scalar = (K - scal * sp.eye(f)).applyfunc(sp.cancel) == sp.zeros(f, f)
            blocks[str(lam)] = {"dim": f, "kappa_block_scalar": str(scal), "scalar": bool(is_scalar),
                                "y_lambda": str(simp(y[lam]))}
        # check tr = sum y chi, and recover s_lambda from tau = sum chi/s
        chis = {lam: (seminormal(lam), len(std_tableaux(lam))) for lam in partitions(n)}
        for w in W:
            chi = {lam: rep_of_word(m, [(g, 1) for g in reduced_word(w)], f).trace()
                   for lam, (m, f) in chis.items()}
            if sp.cancel(sum(y[lam] * chi[lam] for lam in chi) - markov_basis(w)) != 0:
                ytr_ok = False
        # Schur elements s_lambda from tau = sum_lambda chi_lambda / s_lambda (solved
        # independently of kappa), then check kappa block = y_lambda * s_lambda.
        lams = list(partitions(n))
        u = sp.symbols(f"u0:{len(lams)}")
        eqs = []
        for w in W:
            chi = [rep_of_word(chis[l][0], [(g, 1) for g in reduced_word(w)], chis[l][1]).trace() for l in lams]
            eqs.append(sp.together(sum(u[k] * chi[k] for k in range(len(lams))) - (1 if length(w) == 0 else 0)))
        sol = sp.solve(eqs, u, dict=True)[0]
        for k, lam in enumerate(lams):
            s_l = simp(1 / sol[u[k]])
            blocks[str(lam)]["s_lambda"] = str(s_l)
            ok = sp.cancel(kblock[lam] - y[lam] * s_l) == 0
            blocks[str(lam)]["kappa_block_eq_y_times_s"] = bool(ok)
            tau_ok = tau_ok and ok
        part1[n] = {
            "kappa_sigma_basis": {("s" + "".join(map(str, reduced_word(w)))) if reduced_word(w) else "e": str(c)
                                  for w, c in kap.items()},
            "central": bool(cent), "tr_eq_tau_x_kappa": bool(fact), "tr_eq_sum_y_chi": ytr_ok,
            "blocks": blocks,
        }
        checks[f"n{n}_central"] = bool(cent)
        checks[f"n{n}_factorisation"] = bool(fact)
        checks[f"n{n}_y_matches_y_lambda_su_n_symbolic"] = ytr_ok
        checks[f"n{n}_kappa_block_eq_y_s"] = tau_ok
        log(f"  n={n}: central={cent} tr=tau(x kappa)={fact} y-check={ytr_ok}")
    out["part1_kappa"] = part1

    # ---------- Part 2 R2: parabolic projection ----------
    log("R2: projection of kappa_4 onto H_2 (x) H_2 vs kappa_2 (x) kappa_2")
    k2 = kappas[2]
    # kappa_2 (x) kappa_2 in H_4: (1 + z s1)(1 + z s3)
    e = tuple(range(4))
    prod22 = mul({e: 1, sgen(1, 4): zD}, {e: 1, sgen(3, 4): zD}, 4)
    par = {e, sgen(1, 4), sgen(3, 4), compose(sgen(1, 4), sgen(3, 4))}
    proj = {w: c for w, c in kappas[4].items() if w in par}
    r2_22 = all(sp.cancel(proj.get(w, 0) - prod22.get(w, 0)) == 0 for w in par)
    # H_3 (x) H_1: projection onto S_3 should be kappa_3
    par31 = {w for w in kappas[4] if w[3] == 3} | {p + (3,) for p in itertools.permutations(range(3))}
    r2_31 = all(sp.cancel(kappas[4].get(w, 0) - kappas[3].get(w[:3], 0)) == 0 for w in par31)
    # nonparabolic part of kappa_4 is nonzero (so kappa_atom != kappa_free as elements)
    nonpar = {"".join(map(str, reduced_word(w))): str(c) for w, c in kappas[4].items() if w not in par}
    out["part2_R2"] = {"proj_kappa4_onto_H2xH2_eq_kappa2xkappa2": r2_22,
                       "proj_kappa4_onto_H3xH1_eq_kappa3": r2_31,
                       "kappa4_terms_outside_H2xH2": len(nonpar)}
    checks["R2_proj_22"] = r2_22
    checks["R2_proj_31"] = r2_31
    log(f"  proj 2+2 = kappa2(x)kappa2: {r2_22}; proj 3+1 = kappa3: {r2_31}; outside terms {len(nonpar)}")

    # ---------- Part 2 R3: bond-convolved functional ----------
    r3 = {}
    for (n, i) in ((3, 1), (6, 3)):
        log(f"R3: b = (s{i} s{i+1}^-1)^3 in H_{n}")
        bword = [(i, 1), (i + 1, -1)] * 3
        y = y_lambda_su_n_symbolic(n, q, 2)
        rows = {}
        for lam in partitions(n):
            yl = simp(y[lam])
            if yl == 0:
                continue
            mats = seminormal(lam)
            f = len(std_tableaux(lam))
            B = rep_of_word(mats, bword, f)
            s0 = B[0, 0]
            scalar = (B - s0 * sp.eye(f)).applyfunc(sp.cancel) == sp.zeros(f, f)
            rows[str(lam)] = {"dim": f, "rho_b_scalar": bool(scalar),
                              "char_b": str(simp(B.trace()))}
        r3[f"H{n}"] = {"bond": f"(s{i} s{i+1}^-1)^3", "blocks_with_y_nonzero": rows,
                       "t_b_is_a_trace": all(r["rho_b_scalar"] for r in rows.values())}
        checks[f"R3_H{n}_t_b_is_trace"] = r3[f"H{n}"]["t_b_is_a_trace"]
        log(f"  H_{n}: t_b trace? {r3[f'H{n}']['t_b_is_a_trace']}")
    out["part2_R3"] = r3

    # kappa at z_D is not invertible from n=3 on (y_(1^3) = 0)
    y3 = y_lambda_su_n_symbolic(3, q, 2)
    checks["kappa3_not_invertible_y111_zero"] = simp(y3[(1, 1, 1)]) == 0
    out["checks"] = checks
    out["verdict"] = {
        "R1": "holds by linearity of tau for every pair of words in one H_n (modulo the |.| signs)",
        "R2": "pairing the FREE word against kappa_free - kappa_atom gives 0 identically: "
              "the parabolic projection of kappa_atom is kappa_free",
        "R3": "the bond-convolved functional x -> tr(x b) is not a trace for the gamma-gamma bond, "
              "so it has no central knot factor; its pairing element b kappa is non-central",
    }

    try:
        sys.path.insert(0, str(COMP / "substrate"))
        import _path_bridge  # noqa: F401
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("knot-factor-binding-half", engine="sympy (exact, symbolic q)", output_dir=HERE)
        wb.set_description(
            "PROBE, adopts nothing (issue #8960 item 5). Knot factor kappa = sum y s e at z_D for "
            "n=2,3,4 (exact in q) and three readings of the binding half of "
            "conj:knot-factor-frobenius-pairing. No number at q0; no AME.")
        for k, v in out.items():
            wb.add_data(k, v)
        for k, v in checks.items():
            wb.add_assertion(k, computed=int(bool(v)), expected=int(k not in ("R3_H3_t_b_is_trace", "R3_H6_t_b_is_trace")),
                             tolerance=0, source="exact symbolic check")
        wb.save({"q0Anchor": "independent",
                 "q0AnchorReason": "every result is an exact rational function of q; no number at q0 is recorded"})
    except Exception as exc:  # noqa: BLE001
        log(f"WitnessBuilder unavailable ({exc}); writing plain JSON")
        (HERE / "knot-factor-binding-half.witness.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
