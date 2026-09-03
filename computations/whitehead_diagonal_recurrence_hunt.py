#!/usr/bin/env python3
"""Hunt for the diagonal q-difference recurrence of the Whitehead link
(L5a1) colored Jones — the input the GGMW `J_red` → c_{σ_geom}(q=1) recipe
needs (audit 2026-07-26).

The Whitehead has no published closed form (link-AJ is formulated-only), so
the tower is produced by the Masbaum-validated U_q(sl₂) R-matrix engine,
evaluated in EXACT modular arithmetic F_p at a base point s=t (q=t²): the
R-matrix entries are Laurent in s with integer exponents, so J(N) mod p is
exact.  numpy int64 with small primes (p~2²⁰) keeps the O(N³) braid-rep
matmul fast enough to reach N≈16.

Method mirrors `borromean_diagonal_recurrence_hunt.py`: for each (r,W) seek
Σ_{i=0}^r a_i(m) J[N+i] = 0, a_i Laurent in m=q^N over [−W..W]; build the
F_p linear system on FIT rows, take the nullspace, and certify a candidate
by survival on CHECK rows across several (p,t) samples.

VALIDATION FIRST: the same hunt is run on the figure-eight (whose recurrence
is KNOWN) — if it is not recovered at the reachable N, the negative on the
Whitehead is an N-reach statement, not a "no recurrence" claim.

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

PRIMES = [1048573, 1048583, 1048589]      # ~2²⁰ primes; int64-safe for N≤16
BASES = [3, 5, 7]                          # base t (s=t, q=t²)
FIG8 = [1, -2, 1, -2]                      # 4₁, writhe 0 (known recurrence)
WHITEHEAD = [1, -2, 1, -2, 1]             # L5a1, writhe +1


def minv(a, p):
    return pow(int(a) % p, p - 2, p)


def spow(t, e, p):
    """s^e mod p for integer e (s=t)."""
    return pow(t, e, p) if e >= 0 else minv(pow(t, -e, p), p)


def qbr(k, t, p):
    """{k}=s^k−s^{-k} mod p (here s=t)."""
    return (spow(t, k, p) - spow(t, -k, p)) % p


def qint(n, t, p):
    """[n]_q = (q^n−q^{-n})/(q−q^{-1}), q=s²=t²."""
    num = (spow(t, 2 * n, p) - spow(t, -2 * n, p)) % p
    den = (spow(t, 2, p) - spow(t, -2, p)) % p
    return num * minv(den, p) % p


def qfact(n, t, p):
    r = 1
    for k in range(1, n + 1):
        r = r * qint(k, t, p) % p
    return r


def gauss_inv(M, p):
    """Inverse of an n×n matrix over F_p (returns None if singular)."""
    n = M.shape[0]
    A = np.concatenate([M % p, np.eye(n, dtype=np.int64)], axis=1) % p
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r, c] % p != 0), None)
        if piv is None:
            return None
        A[[c, piv]] = A[[piv, c]]
        inv = minv(A[c, c], p)
        A[c] = A[c] * inv % p
        for r in range(n):
            if r != c and A[r, c] % p:
                A[r] = (A[r] - A[r, c] * A[c]) % p
    return A[:, n:] % p


def rmatrix(N, t, p):
    """Ř = P·q^{H⊗H/2}·Σ q^{n(n-1)/2}(q−q⁻¹)ⁿ/[n]! Eⁿ⊗Fⁿ over F_p (q=t²)."""
    E = np.zeros((N, N), dtype=np.int64)
    F = np.zeros((N, N), dtype=np.int64)
    Kd = [spow(t, 2 * (N - 1 - 2 * i), p) for i in range(N)]     # K=q^{H}=s^{2·wt}
    for i in range(N):
        if i - 1 >= 0:
            E[i - 1, i] = qint(N - i, t, p)
        if i + 1 <= N - 1:
            F[i + 1, i] = qint(i + 1, t, p)
    w = [N - 1 - 2 * i for i in range(N)]
    D = np.array([spow(t, w[i] * w[j], p) for i in range(N) for j in range(N)], dtype=np.int64)
    S = np.zeros((N * N, N * N), dtype=np.int64)
    En = np.eye(N, dtype=np.int64)
    Fn = np.eye(N, dtype=np.int64)
    for n in range(N):
        c = spow(t, n * (n - 1), p) * pow((spow(t, 2, p) - spow(t, -2, p)) % p, n, p) % p
        c = c * minv(qfact(n, t, p), p) % p
        S = (S + c * np.kron(En, Fn)) % p
        En = En @ E % p
        Fn = Fn @ F % p
    R = (D[:, None] * S) % p
    P = np.zeros((N * N, N * N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            P[j * N + i, i * N + j] = 1
    return P @ R % p, Kd


def colored_jones_modp(word, m, N, t, p):
    """Framing-corrected reduced colored Jones J(N) mod p (q=t²)."""
    Rc, Kd = rmatrix(N, t, p)
    Rci = gauss_inv(Rc, p)
    dim = N ** m
    rho = np.eye(dim, dtype=np.int64)
    for g in word:
        i = abs(g)
        blk = Rc if g > 0 else Rci
        L = np.eye(N ** (i - 1), dtype=np.int64)
        Rr = np.eye(N ** (m - i - 1), dtype=np.int64)
        op = np.kron(np.kron(L, blk), Rr) % p
        rho = op @ rho % p
    # trace with μ = K^{⊗m}
    idx = np.arange(dim)
    mu = np.ones(dim, dtype=np.int64)
    y = idx.copy()
    for _ in range(m):
        mu = mu * np.array(Kd, dtype=np.int64)[y % N] % p
        y //= N
    raw = int(np.sum(mu * np.diagonal(rho) % p) % p)
    val = raw * minv(qint(N, t, p), p) % p
    # framing q^{-w(N²-1)/2} = s^{-w(N²-1)} = t^{-w(N²-1)}
    wr = sum(1 if g > 0 else -1 for g in word)
    val = val * spow(t, -wr * (N * N - 1), p) % p
    return val


def nullspace_modp(M, p):
    """Basis of the right nullspace of M over F_p."""
    M = M % p
    rows, cols = M.shape
    A = M.copy()
    pivots = []
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i, c] % p != 0), None)
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        A[r] = A[r] * minv(A[r, c], p) % p
        for i in range(rows):
            if i != r and A[i, c] % p:
                A[i] = (A[i] - A[i, c] * A[r]) % p
        pivots.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(cols) if c not in pivots]
    basis = []
    for fc in free:
        v = np.zeros(cols, dtype=np.int64)
        v[fc] = 1
        for ri, pc in enumerate(pivots):
            v[pc] = (-A[ri, fc]) % p
        basis.append(v % p)
    return basis


def build_towers(word, m, Nmax):
    """{(p,t): {N: J mod p}} computed once per sample."""
    towers = {}
    for p in PRIMES:
        for t in BASES:
            towers[(p, t)] = {N: colored_jones_modp(word, m, N, t, p)
                              for N in range(1, Nmax + 1)}
    return towers


def hunt(towers, Nmax, r, W):
    """Try Σ_{i=0}^r a_i(m) J[N+i]=0, a_i Laurent in m∈[−W..W]. Certify across samples."""
    ks = list(range(-W, W + 1))
    ncol = (r + 1) * len(ks)
    ncheck = 4
    fit_ns = list(range(1, Nmax - r + 1))
    if len(fit_ns) <= ncol + ncheck:
        return {"status": "insufficient-N", "need_rows": ncol + ncheck + 1,
                "have_rows": len(fit_ns), "r": r, "W": W}
    fit = fit_ns[:ncol + 2]
    chk = fit_ns[ncol + 2:ncol + 2 + ncheck]
    ok_all = True
    for (p, t), J in towers.items():
        def row(n):
            out = []
            mn = spow(t, 2 * n, p)   # m=q^n=t^{2n}
            for i in range(r + 1):
                for k in ks:
                    out.append(J[n + i] * (pow(mn, k, p) if k >= 0
                                           else minv(pow(mn, -k, p), p)) % p)
            return out
        Mfit = np.array([row(n) for n in fit], dtype=np.int64) % p
        ns = nullspace_modp(Mfit, p)
        surv = False
        for v in ns:
            Mchk = np.array([row(n) for n in chk], dtype=np.int64) % p
            if np.all(Mchk @ v % p == 0):
                surv = True
                break
        ok_all = ok_all and surv
        if not ok_all:
            break
    return {"status": "CERTIFIED" if ok_all else "no-recurrence", "r": r, "W": W, "Nmax": Nmax}


def main() -> int:
    Nmax = int(sys.argv[sys.argv.index("--nmax") + 1]) if "--nmax" in sys.argv else 12
    grid = [(1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 1)]
    print(f"Diagonal recurrence hunt  (Nmax={Nmax}, primes~2²⁰, bases {BASES})\n")

    results = {}
    for label, word, m in [("figure-eight 4₁ [VALIDATION, known recurrence]", FIG8, 3),
                           ("Whitehead L5a1", WHITEHEAD, 3)]:
        print(f"  {label}:")
        results[label] = {}
        towers = build_towers(word, m, Nmax)
        for (r, W) in grid:
            res = hunt(towers, Nmax, r, W)
            results[label][f"r{r}_W{W}"] = res
            print(f"    r={r} W={W}: {res['status']}")
        print()

    fig_found = any(v.get("status") == "CERTIFIED" for v in results[list(results)[0]].values())
    print(f"  Harness validation (fig-8 recurrence found at Nmax={Nmax})? "
          f"{'YES' if fig_found else 'NO → Nmax too small even for the known 4₁ recurrence'}")

    wit = {
        "description": "Whitehead diagonal q-difference recurrence hunt (toward GGMW J_red → c_σ). mod-p nullspace certificate fed by the Masbaum-validated R-matrix engine.",
        "computation": "whitehead_diagonal_recurrence_hunt",
        "audit_only": True,
        "Nmax": Nmax, "grid": [f"r{r}_W{W}" for r, W in grid],
        "results": {k: {kk: vv.get("status") for kk, vv in v.items()} for k, v in results.items()},
        "figure_eight_harness_validated": bool(fig_found),
        "note": ("Nmax is capped by the O(N³) R-matrix braid-rep (no Whitehead closed form). "
                 "If the KNOWN fig-8 recurrence is not recovered, the Whitehead 'no-recurrence' "
                 "entries are N-reach statements; closing needs the 2-bridge b(8,3) O(N²) "
                 "transfer-matrix acceleration or a Habiro closed form."),
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-diagonal-recurrence-hunt.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(wit, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
