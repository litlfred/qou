#!/usr/bin/env python3
"""M₁ and its Fulman split as 3-cycle coefficients of Jucys–Murphy functional calculi.

Bean `qou-h315` (the M₁ > 0 machinery), gap `qou-k5r5`, epic `qou-x631`.

Background. ``M₁(n) = Cov_Planch(Σ_□ h, ω₃)`` with ``ω₃ = Σ_□ c² − C(n,2)``. The corpus splits
``Σ_□ h = A + D`` with ``A = Σ_□ |c|`` and ``D = Σ_u d_u²`` (``d_u`` = number of cells of
content ``u``), so ``M₁ = P − N`` with ``P = Cov(A, ω₃)`` and ``N = −Cov(D, ω₃)``.

Statement checked here. Let ``J_k = Σ_{i<k} (i k)`` be the Jucys–Murphy elements of ``C[S_n]``
(``J_1 = 0``). They commute, and on the Young vector ``v_T`` the element ``J_k`` acts by the
content of the box holding ``k`` in ``T``. So, for any functions ``φ`` and ``ψ``,
``Σ_k φ(J_k)`` and ``Σ_{k≠l} ψ(J_k − J_l)`` are symmetric functions of the ``J_k``. They are
therefore central (Jucys 1974) and act on ``V^λ`` by ``Σ_□ φ(c)`` and ``Σ_{□≠□'} ψ(c − c')``.
For a central ``Z`` with eigenvalue ``F(λ)``, ``[σ]Z = Σ_λ F(λ) f^λ χ^λ(σ)/n!``. With
``ω₃ = n(n−1)(n−2)χ^λ(σ)/(3 f^λ)`` (σ a 3-cycle) this gives

    Cov_Planch(F, ω₃) = (n(n−1)(n−2)/3) · [σ] Z_F .

Taking ``Z_A = Σ_k |J_k|`` and ``Z_D = n·e + Σ_{k≠l} δ(J_k = J_l)``:

    P(n)  = (n(n−1)(n−2)/3) · [(1 2 3)] Σ_k |J_k|  =  (n(n−1)(n−2)/3) · [(1 2 n)] |J_n|,
    −N(n) = (n(n−1)(n−2)/3) · [(1 2 3)] Σ_{k≠l} δ(J_k = J_l),
    M₁(n) = (n(n−1)(n−2)/3) · [(1 2 3)] ( Σ_k |J_k| + Σ_{k≠l} δ(J_k = J_l) ).

The second form of P is the single element ``|J_n|``. It follows from centrality of ``Z_A``:
``[(1 2 n)]Z_A`` picks up only ``|J_n|``, because ``|J_k|`` lies in ``C[S_k]`` and so has no
support on permutations moving ``n`` when ``k < n``.

Both sides are computed with no shared code:
  * the group-algebra side multiplies by transpositions only. ``φ(J_k)`` is built as the
    Lagrange polynomial in ``J_k`` through its possible eigenvalues ``−(k−1)…k−1``, and the
    same is done for ``J_k − J_l``. It uses no characters, no hook formula and no partitions;
  * the partition side uses the hook-length formula and cell contents.

All arithmetic is exact (``Fraction``); there is no float64. This is a REFORMULATION. It does not
prove M₁ > 0 or any bound. Nothing is fitted and nothing is wired.
"""
from __future__ import annotations

import sys
from collections import Counter
from fractions import Fraction as F
from math import comb, factorial

# ---------------------------------------------------------------- group-algebra side


def _compose(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def _transp(i, j, n):
    t = list(range(n))
    t[i], t[j] = t[j], t[i]
    return tuple(t)


def _jm(k, n):
    """J_k (1-indexed) as a list of (coefficient, transposition)."""
    return [(1, _transp(i, k - 1, n)) for i in range(k - 1)]


def _left_mul(lin, vec):
    out = {}
    for c, t in lin:
        for g, v in vec.items():
            h = _compose(t, g)
            out[h] = out.get(h, 0) + c * v
    return {g: v for g, v in out.items() if v}


def _lagrange(points, phi):
    m = len(points)
    co = [F(0)] * m
    for a in points:
        val = phi(a)
        if val == 0:
            continue
        poly, den = [F(1)], F(1)
        for b in points:
            if b == a:
                continue
            poly = [(poly[i - 1] if i > 0 else 0) - b * (poly[i] if i < len(poly) else 0)
                    for i in range(len(poly) + 1)]
            den *= (a - b)
        for i in range(m):
            co[i] += val * poly[i] / den
    return co


def _coeff_of_function(lin, points, phi, n, target):
    """[target] φ(X), X = Σ c·perm (lin), via the Lagrange polynomial through `points`."""
    vec = {tuple(range(n)): F(1)}
    total = F(0)
    for c in _lagrange(points, phi):
        if c:
            total += c * vec.get(target, 0)
        vec = _left_mul(lin, vec)
    return total


def _three_cycle(a, b, c, n):
    t = list(range(n))
    t[a], t[b], t[c] = b, c, a
    return tuple(t)


def group_algebra_side(n):
    s123 = _three_cycle(0, 1, 2, n)
    s12n = _three_cycle(0, 1, n - 1, n)
    zA_123 = sum(_coeff_of_function(_jm(k, n), list(range(-(k - 1), k)), abs, n, s123)
                 for k in range(2, n + 1))
    absJn_12n = _coeff_of_function(_jm(n, n), list(range(-(n - 1), n)), abs, n, s12n)
    zD_123 = F(0)
    for k in range(1, n + 1):
        for l in range(1, n + 1):
            if k == l:
                continue
            lin = _jm(k, n) + [(-c, p) for c, p in _jm(l, n)]
            r = (k - 1) + (l - 1)
            zD_123 += _coeff_of_function(lin, list(range(-r, r + 1)),
                                         lambda a: 1 if a == 0 else 0, n, s123)
    s = F(n * (n - 1) * (n - 2), 3)
    return {"P": s * zA_123, "P_via_absJn": s * absJn_12n, "CovD": s * zD_123,
            "M1": s * (zA_123 + zD_123), "absJn_12n": absJn_12n}


# ---------------------------------------------------------------- partition side


def _parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in _parts(n - k, k):
            yield (k,) + p


def _conj(l):
    return tuple(sum(1 for r in l if r > j) for j in range(l[0])) if l else ()


def partition_side(n):
    P = CovD = M1 = F(0)
    for l in _parts(n):
        lc = _conj(l)
        cells = [(i, j) for i, r in enumerate(l) for j in range(r)]
        hooks = [(l[i] - j - 1) + (lc[j] - i - 1) + 1 for i, j in cells]
        hp = 1
        for h in hooks:
            hp *= h
        f = factorial(n) // hp
        w = F(f * f, factorial(n))
        cont = [j - i for i, j in cells]
        W = sum(c * c for c in cont) - comb(n, 2)
        A = sum(abs(c) for c in cont)
        D = sum(v * v for v in Counter(cont).values())
        assert sum(hooks) == A + D  # Fulman split Σh = Σ|c| + Σ d_u²
        P += w * A * W
        CovD += w * D * W
        M1 += w * sum(hooks) * W
    return {"P": P, "CovD": CovD, "M1": M1}


# ---------------------------------------------------------------- Plancherel-growth side
#
# Young's orthogonal form: on v_T the adjacent transposition s_k has diagonal entry 1/r_k(T),
# r_k = c_T(k+1) − c_T(k). Conjugating (1 2 n) to (n−2 n−1 n) = s_{n−2}s_{n−1} by S_{n−1}
# (which commutes with J_n) gives, for Z = Σ_k |J_k| + Σ_{k≠l} δ(J_k=J_l),
#     [(1 2 n)] Z = E_PG[ (i_n + j_n − 2) / (r_{n−1} r_{n−2}) ],
# over Plancherel growth (P(T) = f^λ/n!), where (i_n, j_n) is the 1-indexed position of box n.
# The eigenvalue |c_n| + 2#{l<n : c_l = c_n} equals i_n + j_n − 2. The −2 drops out because
# ρ_n(s) := E_PG[1{i_n + j_n = s}/(r_{n−1}r_{n−2})] has total mass [(1 2 n)]e = 0. Hence
#     M₁(n) = (n(n−1)(n−2)/3) · Σ_s s ρ_n(s),
# and M₁(n) > 0 follows from one sign change of ρ_n
# (YoungDiagramKernelSingleCrossing.firstMoment_pos_of_single_crossing).


def _dim(l):
    n = sum(l)
    if n == 0:
        return 1
    lc = _conj(l)
    h = 1
    for i, r in enumerate(l):
        for j in range(r):
            h *= (r - j - 1) + (lc[j] - i - 1) + 1
    return factorial(n) // h


def _addable(l):
    l = list(l)
    out = []
    for i in range(len(l) + 1):
        r = l[i] if i < len(l) else 0
        if i == 0 or l[i - 1] > r:
            nl = l[:]
            if i < len(l):
                nl[i] += 1
            else:
                nl.append(1)
            out.append((tuple(nl), i, r))
    return out


def plancherel_growth_side(n):
    """Returns M₁(n), P(n) from the last-three-box formula, and ρ_n as {s: mass}."""
    rho, M, P = {}, F(0), F(0)
    for mu in _parts(n - 3):
        fm = _dim(mu)
        for l1, i1, j1 in _addable(mu):
            for l2, i2, j2 in _addable(l1):
                for l3, i3, j3 in _addable(l2):
                    c1, c2, c3 = j1 - i1, j2 - i2, j3 - i3
                    w = F(fm * _dim(l3), (c3 - c2) * (c2 - c1))
                    s = i3 + j3 + 2
                    rho[s] = rho.get(s, 0) + w
                    M += w * s
                    P += w * abs(c3)
    nf = factorial(n)
    rho = {s: v / nf for s, v in rho.items()}
    scale = F(n * (n - 1) * (n - 2), 3) / nf
    return scale * M, scale * P, rho


def single_crossing(rho, n):
    """(ok, t): ρ ≤ 0 on s < t and ≥ 0 on s ≥ t, total mass 0, ρ ≠ 0."""
    svals = range(2, n + 2)
    if sum(rho.get(s, 0) for s in svals) != 0 or all(rho.get(s, 0) == 0 for s in svals):
        return False, None
    t = min((s for s in svals if rho.get(s, 0) > 0), default=None)
    if t is None:
        return False, None
    ok = all(rho.get(s, 0) <= 0 for s in svals if s < t) and \
        all(rho.get(s, 0) >= 0 for s in svals if s >= t)
    return ok, t


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    rows, ok = [], True
    print("n | P(n) | Cov(D,ω₃) | M₁(n) | [(12n)]|J_n|   (group algebra == partitions?)")
    for n in range(3, nmax + 1):
        g, p = group_algebra_side(n), partition_side(n)
        good = (g["P"] == p["P"] == g["P_via_absJn"] and g["CovD"] == p["CovD"]
                and g["M1"] == p["M1"])
        ok &= good
        rows.append({"n": n, "P": str(p["P"]), "CovD": str(p["CovD"]), "M1": str(p["M1"]),
                     "absJn_coeff_12n": str(g["absJn_12n"]), "match": good})
        print(f"{n} | {p['P']} | {p['CovD']} | {p['M1']} | {g['absJn_12n']}   {good}")
    print(f"\nRESULT: Jucys–Murphy form of P, N, M₁ verified n=3..{nmax}: {ok}")
    npg = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    pg_rows, pg_ok, cross_ok = [], True, True
    print(f"\nPlancherel-growth form; single crossing of ρ_n in s = i+j, n=3..{npg}")
    for n in range(3, npg + 1):
        M, Pn, rho = plancherel_growth_side(n)
        if n <= nmax:
            p = partition_side(n)
            pg_ok &= (M == p["M1"] and Pn == p["P"])
        sc, t = single_crossing(rho, n)
        cross_ok &= sc
        pg_rows.append({"n": n, "M1": str(M), "single_crossing": sc, "threshold_s": t})
        print(f"{n} | M₁ = {M} | single crossing: {sc} at s = {t}", flush=True)
    print(f"RESULT: PG formula == partition side n=3..{nmax}: {pg_ok}; "
          f"single crossing n=3..{npg}: {cross_ok}")
    ok = ok and pg_ok and cross_ok
    try:
        sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[1]
                               / "substrate"))
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-M1-jucys-murphy-form", engine="python-exact")
        w.set_description(
            "M₁ = Cov(Σh, ω₃) and its Fulman split P = Cov(Σ|c|, ω₃), N = −Cov(Σd_u², ω₃) as "
            "(n(n−1)(n−2)/3)·[3-cycle] of central Jucys–Murphy functional calculi: "
            "P ∝ [(12n)]|J_n| (one element), −N ∝ [(123)]Σ_{k≠l}δ(J_k=J_l). Group-algebra side "
            "(transpositions only) equals partition side (hook formula) exactly. Via Young's "
            "orthogonal form, M₁ = (n(n−1)(n−2)/3)·Σ_s s ρ_n(s), ρ_n a mass-zero signed measure "
            "on s = i+j of the n-th Plancherel-growth box; ρ_n has a single sign change for every "
            "checked n, which gives M₁>0 there via the Lean lemma "
            "firstMoment_pos_of_single_crossing. Single crossing for all n is NOT proved. "
            "No fit; nothing wired.")
        w.add_data("rows", rows)
        w.add_data("plancherel_growth_rows", pg_rows)
        w.add_assertion("m1_jucys_murphy_form", computed=str(int(ok)), expected="1",
                        tolerance=0,
                        source=f"group-algebra vs hook-formula n=3..{nmax}; Plancherel-growth "
                               f"formula == hook side n=3..{nmax}; single crossing n=3..{npg}")
        print(f"Witness: {w.save()}")
    except ImportError as e:
        print(f"(witness skipped — witness_base unavailable: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
