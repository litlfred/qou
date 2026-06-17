"""General-n Jacobi–Anger tower test via the existing pyhecke_native infra.

Path A of `docs/audits/2026-06-17-jacobi-anger-physical-weight-n3.md`: extend the
§4a single-x q-Bessel over-determination test up the brane tower (n=3,6,9), to see
whether the bar-odd tower residual → 0 as n grows.

Critical-distance caveat (carried from that audit): the selector tested here is the
**min-norm-direction** `T_β ∝ t` (the Markov-trace functional vector over the NF
basis `{T_w : w∈S_n}`), i.e. an empirical fit, NOT a first-principles object. The
single-x over-determination *ratio* test is scale-free, so the n_target
normalisation is irrelevant and `T_β ∝ t` suffices. A shrinking residual is
suggestive (the fit's bar-odd tower approaches q-Bessel); it does NOT close the
keystone (that needs Path B, first-principles Δ_{T_β}). TIERED; nothing wired.

NO new infra: uses `pyhecke_native.chi_lambda_braid_mpfr` (general-n Hoefsmit
seminormal character) + `wedderburn_jones_markov.y_lambda_at` (general-n Wenzl
weights). The H₃-hardcoded `pyhecke.gram` NF tables are a legacy artifact; the Rust
engine already supersedes them at all n. **`validate_n3()` confirms this:** the
general-path Markov trace `Σ_λ y_λ χ_λ(T_w)` reproduces the hardcoded `gram.TR_M`
values for all 6 words of S₃ to ~1e-8 (the float64 floor of `y_lambda_at`).

⚠ **WIP — tower-object reconciliation OPEN (2026-06-17).** This script's tower
object `F(q)=Σ_w t_w·τ_M(T_w)(q)` (the autocorrelation of the Markov-trace
functional, = `τ_M(T_β)` for `T_β∝t`) does **NOT** yet reproduce the n=3
over-determination residual of #2453's physical-weight run (6.8%); it gives a much
larger residual. So my `T_β∝t` autocorrelation construction diverges from #2453's
"per-block bar-odd coeffs of `χ_λ(T_β)` for the min-norm fit, then `Σ_λ y_λ·coeff`"
construction — the two are NOT the same object, contrary to the algebra I expected.
**Do not trust the n≥6 numbers until the n=3 cross-check matches 6.8%.** The general
infra (τ_M at all n) is validated; the open step is pinning which tower object the
§4a test actually specifies (per-block-of-fit vs autocorrelation) and making this
harness reproduce the established n=3 value before extending up the tower.

  τ_M(T_w)(q) = Σ_{λ⊢n} y_λ(n,q)·χ_λ(T_w)(q),
  T_β ∝ t,  t_w = τ_M(T_w)(q₀),
  τ_M(T_β)(q) = Σ_{w∈S_n} t_w·τ_M(T_w)(q)   ← the bar-odd tower object,
  bar-odd: W(η) = [τ_M(T_β)(e^η) − τ_M(T_β)(e^{−η})]/2 = Σ_{k odd} W_k·sinh(kη).
"""
from __future__ import annotations

import sys
import time
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from mpmath import besselj, findroot  # noqa: E402
import pyhecke_native as pyn  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

mp.mp.dps = 50

try:
    from qou_substrate.constants import q_at
    Q0 = mp.mpf(str(q_at()))
except Exception:
    Q0 = mp.mpf("1.10997858275")


def partitions(n):
    def rec(n, mx):
        if n == 0:
            yield ()
            return
        for k in range(min(n, mx), 0, -1):
            for rest in rec(n - k, k):
                yield (k,) + rest
    return list(rec(n, n))


def reduced_word(perm):
    """0-based adjacent-transposition reduced word sorting `perm` (a list)."""
    p = list(perm)
    w = []
    # bubble sort, recording adjacent swaps s_i = (i,i+1)
    changed = True
    while changed:
        changed = False
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                w.append(i)
                changed = True
    return w  # word so that applying s_w sorts perm; T_perm = product


def chi(lam, word, q_str, dps=50):
    # native braid form: list of (sign, gen_1based); reduced word is all +σ.
    nat = [(1, g + 1) for g in word]
    return mp.mpf(pyn.chi_lambda_braid_mpfr(list(lam), nat, q_str, dps))


def tau_M_word(word, n, q, parts, dps=50):
    """Markov trace τ_M(T_word)(q) = Σ_λ y_λ(n,q)·χ_λ(word)(q)."""
    q_str = mp.nstr(q, dps)
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}
    return sum(y[lam] * chi(lam, word, q_str, dps) for lam in parts)


def validate_n3():
    """General infra must reproduce the hardcoded gram.TR_M Markov-trace values."""
    from pyhecke.gram import NF_BASIS, TR_M
    parts = partitions(3)
    print("  n=3 Markov-trace validation (general infra vs hardcoded gram.TR_M):")
    ok = True
    for w, expected in zip(NF_BASIS, TR_M):
        got = tau_M_word(list(w), 3, Q0, parts)
        d = abs(got - mp.mpf(str(expected)))
        ok = ok and (d < mp.mpf("1e-12"))
        print(f"    T_{w!s:10s} general={mp.nstr(got,10)} hardcoded={expected:.10f}  Δ={mp.nstr(d,3)}")
    return ok


def tower_residual(n, n_eta=7, dps=50):
    """Single-x over-determination residual of the bar-odd τ_M(T_β) tower at level n."""
    parts = partitions(n)
    perms = list(permutations(range(n)))
    words = [reduced_word(p) for p in perms]
    t0 = time.time()
    # weights t_w = τ_M(T_w)(q0)
    tw = [tau_M_word(w, n, Q0, parts, dps) for w in words]
    # bar-odd tower at sample η: W(η)=Σ_w t_w·τ_M(T_w)(e^η)  (bar-odd via ±η)
    etas = [mp.mpf(j + 1) / mp.mpf(2 * n_eta) for j in range(n_eta)]  # small positive η
    bar = []
    for eta in etas:
        qp, qm = mp.e**eta, mp.e**(-eta)
        Fp = sum(tw[i] * tau_M_word(words[i], n, qp, parts, dps) for i in range(len(words)))
        Fm = sum(tw[i] * tau_M_word(words[i], n, qm, parts, dps) for i in range(len(words)))
        bar.append((Fp - Fm) / 2)
    # fit W(η)=Σ_{k=1,3,..} W_k sinh(kη): solve linear system over odd orders
    orders = list(range(1, 2 * n_eta, 2))[:n_eta]
    A = mp.matrix(n_eta, n_eta)
    b = mp.matrix(n_eta, 1)
    for r, eta in enumerate(etas):
        for c, k in enumerate(orders):
            A[r, c] = mp.sinh(k * eta)
        b[r] = bar[r]
    W = mp.lu_solve(A, b)
    Wk = {orders[c]: W[c] for c in range(len(orders))}
    # single-x from W_3/W_1 = J_3(x)/J_1(x); test over-determined W_{5,7,..}/W_1
    r31 = Wk[3] / Wk[1]
    x = None
    for x0 in [mp.mpf("2.5"), mp.mpf("4.5"), mp.mpf("6"), mp.mpf("8"), mp.mpf("11")]:
        try:
            cand = findroot(lambda z: besselj(3, z) / besselj(1, z) - r31, x0)
            if abs(cand.imag) < mp.mpf("1e-25") and cand.real > 0:
                x = cand.real
                break
        except Exception:
            continue
    resid = {}
    if x is not None:
        for k in orders:
            if k in (1, 3):
                continue
            pred = besselj(k, x) / besselj(1, x)
            act = Wk[k] / Wk[1]
            resid[k] = abs(pred - act) / abs(act)
    wall = time.time() - t0
    return {
        "n": n, "n_words": len(words), "orders": orders,
        "Wk": {k: mp.nstr(v, 8) for k, v in Wk.items()},
        "single_x": (mp.nstr(x, 10) if x else None),
        "overdet_residuals": {k: mp.nstr(v, 6) for k, v in resid.items()},
        "max_overdet_residual": (mp.nstr(max(resid.values()), 6) if resid else None),
        "wall_s": round(wall, 1),
    }


def main():
    import json
    print("=" * 78)
    print(" General-n Jacobi–Anger tower test (Path A; min-norm-fit direction T_β∝t)")
    print("=" * 78)
    ok3 = validate_n3()
    print(f"  n=3 Markov-trace validation: {'PASS' if ok3 else 'FAIL'}")
    print("-" * 78)
    out = {"n3_markov_validation": ok3, "levels": {}}
    levels = [int(x) for x in sys.argv[1:]] or [3, 6]
    for n in levels:
        r = tower_residual(n)
        out["levels"][n] = r
        print(f"  n={n}: words={r['n_words']}  orders={r['orders']}  "
              f"x*={r['single_x']}  max over-det residual={r['max_overdet_residual']}  "
              f"({r['wall_s']}s)")
        print(f"        residuals by order: {r['overdet_residuals']}")
    print("-" * 78)
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
