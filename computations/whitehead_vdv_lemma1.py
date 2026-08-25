#!/usr/bin/env python3
"""van der Veen's Whitehead-chain colored Jones at the Kashaev point —
first corpus transcription (bean qou-tc7p, brick W1 of milestone qou-k49o).

Source (do NOT cite from memory — this is the verified transcription):
  R. van der Veen, "Proof of the volume conjecture for Whitehead
  chains", arXiv:math/0611181 v2, uploaded 2026-08-01 as
  library/arxiv-math-0611181v2/0611181v2.pdf (owner commit 8ffce0a1).  Two layers are
  transcribed:

  (1) The generic-t tangle formula (p. 4, after Lemma 1; conventions
      of [Zheng, math/0508138]).  With [n] = (t^{n/2}-t^{-n/2})/
      (t^{1/2}-t^{-1/2}):

        T(n,t) = t^{n(n+1)}
        B(n,t) = [N(2n+1)]/[2n+1]
        C(n,t) = t^{(N^2-1)/2 + N(N-1)/2} *
                 sum_{k=0}^{N-1-n} t^{-N(n+k)}
                   prod_{j=1}^{n} (1-t^{N-j-k})(1-t^{j+k})/(1-t^j)

      where the framing factor t^{(N^2-1)/2} is included ONLY when
      c+d = 1 (both clasp strands on one component — vdV p. 4), and

        J_N(W_{a,b,c,d})(t) = sum_{n=0}^{N-1} ([2n+1]/[N]) T(n,t)^a
                              B(n,t)^b C(n,t)^c C(n,t^{-1})^d

  (2) Lemma 1 (p. 3), the closed forms at t = e^{2 pi i/N}:

        J_N(W_{a,1,c,d}) = phi_N sum_{n=0}^{N-1} (2n+1)
                           chi_{N,n}^{4a-c+d}
                           ( sum_{k=0}^{N-1-n} S_{n,k} )^{c+d}

        J_N(W_{a,b,c,d}) = 0 for b >= 2, N even; for N = 2M+1:
        J_N(W_{a,b,c,d}) = phi_N N^b chi_{N,M}^{4a-c+d}
                           ( sum_{k=0}^{M} S_{M,k} )^{c+d}

        chi_{N,n} = exp( n(n+1-N) pi i / (2N) )
        S_{n,k}   = prod_{j=1}^{n} 2 sin^2((k+j)pi/N) / sin(j pi/N)
        phi_N     = exp((N-1)(c-d) pi i / N)   if c+d = 1
                  = (-1)^{(N-1)(c-d)}          otherwise

  Named instances: Whitehead link = W_{0,1,1,0}; Borromean rings =
  W_{0,1,1,1}; the 2-belt chain W_{0,2,1,0} is the b >= 2 chain with
  Vol = 8 Lambda(pi/4) = 4G (vdV: Vol(W_{a,b,c,d}) = 8(c+d)Lambda(pi/4),
  octahedral decomposition, his [10]).

Correctness anchors (no fit; every claim machine-checked below):
  A1  internal: the generic-t formula evaluated on the unit circle at
      angle 2pi/N + delta (delta = 1e-20) matches Lemma 1's sin-form to
      O(delta) — for b=1 over (a,c,d) in {(0,1,0),(0,0,1),(1,1,0),
      (0,1,1)} and for b=2,3 (odd N).  This pins BOTH transcriptions
      against each other through the 0/0 resolution at the root.
  A2  external: the Borromean specialization W_{0,1,1,1} matches the
      corpus's independent GL2011/Habiro cyclotomic transcription
      (habiro_borromean_colored_jones.py, library/arxiv-math-0508100v6/0508100v6.pdf) in
      magnitude at the same near-root point — two unrelated published
      formulas, two independent transcriptions.
  A3  formula-free volume target: the growth rate (2pi/N) log|J_N|
      fitted with the known N^{(c+d+2b)/2} polynomial correction tends
      to 4G = 3.6638623767... for BOTH the Whitehead link W_{0,1,1,0}
      (b=1) and the 2-belt chain W_{0,2,1,0} (b=2, odd N).
  A4  structural (the facts the Lean bricks W3-W5 will formalize):
      S_{M,k} > 0 strictly; log S_{n,k} = 2(s_{n+k}-s_k) - s_n with
      s_m = sum_{j<=m} log(2 sin(j pi/N)); the b>=2 even-N vanishing
      (generic-t form is O(delta) at the near-root point); and the
      exact modulus identity |J_N(W_{a,b,c,d})| = N^b (sum_k S_{M,k})^
      {c+d} for b >= 2, N odd — the phase-free positive sum that makes
      the elementary squeeze possible for chains (unlike b=1, whose
      outer n-sum carries the chi phases and needs vdV's Lemma 4
      Gaussian analysis).

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

CATALAN = mp.catalan
VOL_4G = 4 * mp.catalan  # Vol(Whitehead) = Vol(W_{0,2,1,0}) = 8*Lambda(pi/4)


# ───────────────────── generic-t tangle formula ─────────────────────
def _tp(h, r):
    """t^r with t = exp(h) (h complex log of t; avoids branch cuts)."""
    return mp.exp(h * mp.mpf(r))


def qbr(n: int, h) -> mp.mpc:
    """Balanced quantum integer [n] at t = exp(h)."""
    return (_tp(h, mp.mpf(n) / 2) - _tp(h, -mp.mpf(n) / 2)) / (
        _tp(h, mp.mpf("0.5")) - _tp(h, mp.mpf("-0.5"))
    )


def C_tangle(N: int, n: int, h, framing: bool) -> mp.mpc:
    """Clasp tangle C(n,t), t = exp(h); framing factor iff c+d = 1."""
    pref = mp.mpf(N * (N - 1)) / 2
    if framing:
        pref += mp.mpf(N * N - 1) / 2
    total = mp.mpc(0)
    for k in range(0, N - n):
        prod = mp.mpc(1)
        for j in range(1, n + 1):
            prod *= (1 - _tp(h, N - j - k)) * (1 - _tp(h, j + k)) / (1 - _tp(h, j))
        total += _tp(h, -N * (n + k)) * prod
    return _tp(h, pref) * total


def J_vdv_t(N: int, a: int, b: int, c: int, d: int, h) -> mp.mpc:
    """Normalized colored Jones of W_{a,b,c,d} at t = exp(h) (generic t)."""
    framing = (c + d == 1)
    total = mp.mpc(0)
    for n in range(N):
        term = qbr(2 * n + 1, h) / qbr(N, h)
        if a:
            term *= _tp(h, a * n * (n + 1))
        if b:
            term *= (qbr(N * (2 * n + 1), h) / qbr(2 * n + 1, h)) ** b
        if c:
            term *= C_tangle(N, n, h, framing) ** c
        if d:
            term *= C_tangle(N, n, -h, framing) ** d
        total += term
    return total


# ─────────────────── Lemma 1: Kashaev-point forms ───────────────────
def S_nk(N: int, n: int, k: int) -> mp.mpf:
    """S_{n,k} = prod_{j=1}^{n} 2 sin^2((k+j)pi/N)/sin(j pi/N) (> 0)."""
    p = mp.mpf(1)
    for j in range(1, n + 1):
        p *= 2 * mp.sin((k + j) * mp.pi / N) ** 2 / mp.sin(j * mp.pi / N)
    return p


def _phi(N: int, c: int, d: int) -> mp.mpc:
    if c + d == 1:
        return mp.exp(1j * mp.pi * (N - 1) * (c - d) / N)
    return mp.mpc((-1) ** ((N - 1) * (c - d)))


def _chi(N: int, n: int) -> mp.mpc:
    return mp.exp(1j * mp.pi * n * (n + 1 - N) / (2 * N))


def J_kashaev_b1(N: int, a: int, c: int, d: int) -> mp.mpc:
    """Lemma 1, b = 1: phi_N sum_n (2n+1) chi^{4a-c+d} (sum_k S_{n,k})^{c+d}."""
    total = mp.mpc(0)
    for n in range(N):
        inner = mp.fsum(S_nk(N, n, k) for k in range(N - n))
        total += (2 * n + 1) * _chi(N, n) ** (4 * a - c + d) * inner ** (c + d)
    return _phi(N, c, d) * total


def J_kashaev_chain(N: int, a: int, b: int, c: int, d: int) -> mp.mpc:
    """Lemma 1, b >= 2: 0 for even N; single n = M slice for N = 2M+1."""
    assert b >= 2
    if N % 2 == 0:
        return mp.mpc(0)
    M = (N - 1) // 2
    inner = mp.fsum(S_nk(N, M, k) for k in range(M + 1))
    return _phi(N, c, d) * mp.mpf(N) ** b * _chi(N, M) ** (4 * a - c + d) * inner ** (c + d)


# ─────────────── Habiro/GL2011 Borromean (external anchor) ───────────────
def J_habiro_borromean(n: int, h) -> mp.mpc:
    """Corpus GL2011 App. A / Habiro sum, all colors n, q = exp(h).

    J = sum_{l=0}^{n-1} (-1)^l {n}^2 (prod_{j=1}^{l} {n+j}{n-j})^3
        / (prod_{j=l+1}^{2l+1} {j})^2,  {j} = q^{j/2} - q^{-j/2}.
    Mirrors habiro_borromean_colored_jones.py (sympy) numerically.
    """
    br = lambda j: _tp(h, mp.mpf(j) / 2) - _tp(h, -mp.mpf(j) / 2)
    total = mp.mpc(0)
    for l in range(0, n):
        num = br(n) ** 2
        for j in range(1, l + 1):
            num *= (br(n + j) * br(n - j)) ** 3
        den = mp.mpc(1)
        for j in range(l + 1, 2 * l + 2):
            den *= br(j) ** 2
        total += (-1) ** l * num / den
    return total


# ───────────────────────── anchor battery ─────────────────────────
def run_anchors():
    results = {}
    delta = mp.mpf("1e-20")

    # A1: generic-t form vs Lemma-1 sin-form at angle 2pi/N + delta.
    print("A1  generic-t formula vs Lemma 1 closed form (near-root, on-circle)")
    a1_worst = mp.mpf(0)
    for N in (4, 5, 6, 7):
        h = 1j * (2 * mp.pi / N + delta)
        for (a, c, d) in ((0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1)):
            jt = J_vdv_t(N, a, 1, c, d, h)
            jk = J_kashaev_b1(N, a, c, d)
            rel = abs(jt - jk) / max(abs(jk), mp.mpf("1e-30"))
            a1_worst = max(a1_worst, rel)
            print(f"    b=1 N={N} (a,c,d)=({a},{c},{d}): rel err {mp.nstr(rel, 3)}")
    for N in (5, 7):
        h = 1j * (2 * mp.pi / N + delta)
        for (a, b, c, d) in ((0, 2, 1, 0), (1, 2, 0, 1), (0, 3, 1, 0)):
            jt = J_vdv_t(N, a, b, c, d, h)
            jk = J_kashaev_chain(N, a, b, c, d)
            rel = abs(jt - jk) / max(abs(jk), mp.mpf("1e-30"))
            a1_worst = max(a1_worst, rel)
            print(f"    b={b} N={N} (a,c,d)=({a},{c},{d}): rel err {mp.nstr(rel, 3)}")
    a1_ok = a1_worst < mp.mpf("1e-10")
    results["a1_worst_rel_err"] = mp.nstr(a1_worst, 6)
    results["a1_ok"] = bool(a1_ok)
    print(f"    A1 {'PASSED' if a1_ok else 'FAILED'} (worst {mp.nstr(a1_worst, 3)})\n")

    # A2: Borromean specialization vs corpus Habiro/GL2011 sum (magnitude).
    print("A2  W_{0,1,1,1} vs independent Habiro/GL2011 Borromean transcription")
    a2_worst = mp.mpf(0)
    for N in (3, 4, 5, 6, 7, 8):
        h = 1j * (2 * mp.pi / N + delta)
        jv = J_vdv_t(N, 0, 1, 1, 1, h)
        jh = J_habiro_borromean(N, h)
        rel = abs(abs(jv) - abs(jh)) / max(abs(jh), mp.mpf("1e-30"))
        a2_worst = max(a2_worst, rel)
        print(f"    N={N}: |J_vdV|={mp.nstr(abs(jv), 10)}  |J_Habiro|={mp.nstr(abs(jh), 10)}  rel {mp.nstr(rel, 3)}")
    a2_ok = a2_worst < mp.mpf("1e-10")
    results["a2_worst_rel_err"] = mp.nstr(a2_worst, 6)
    results["a2_ok"] = bool(a2_ok)
    print(f"    A2 {'PASSED' if a2_ok else 'FAILED'} (worst {mp.nstr(a2_worst, 3)})\n")

    # A3: volume rate -> 4G, with 3-parameter fit r_N = V + alpha*logN/N + beta/N.
    print("A3  volume rate (2pi/N) log|J| -> 4G  (3-param tail fit)")

    def rate_fit(pts):
        # least squares for r = V + al*logN/N + be/N
        import statistics  # noqa: F401 (stdlib presence)
        A_rows, y = [], []
        for (Nv, r) in pts:
            A_rows.append((mp.mpf(1), mp.log(Nv) / Nv, mp.mpf(1) / Nv))
            y.append(r)
        # normal equations 3x3
        AT_A = [[mp.fsum(A_rows[i][p] * A_rows[i][q] for i in range(len(A_rows)))
                 for q in range(3)] for p in range(3)]
        AT_y = [mp.fsum(A_rows[i][p] * y[i] for i in range(len(A_rows))) for p in range(3)]
        sol = mp.lu_solve(mp.matrix(AT_A), mp.matrix(AT_y))
        return sol[0]

    # b=1 Whitehead link (O(N^3) work — moderate N grid)
    pts = []
    for N in (40, 60, 80, 100, 120):
        s = [mp.log(2 * mp.sin(j * mp.pi / N)) for j in range(1, N)]
        pref = [mp.mpf(0)]
        for v in s:
            pref.append(pref[-1] + v)  # pref[m] = s_m
        total = mp.mpc(0)
        for n in range(N):
            inner = mp.fsum(mp.exp(2 * (pref[n + k] - pref[k]) - pref[n])
                            for k in range(N - n))
            total += (2 * n + 1) * _chi(N, n) ** (-1) * inner
        r = 2 * mp.pi / N * mp.log(abs(total))
        pts.append((N, r))
        print(f"    W-link  N={N}: r_N = {mp.nstr(r, 10)}")
    v_b1 = rate_fit(pts)
    err_b1 = abs(v_b1 - VOL_4G)
    print(f"    W-link fit V = {mp.nstr(v_b1, 12)}  vs 4G = {mp.nstr(VOL_4G, 12)}  err {mp.nstr(err_b1, 3)}")

    # b=2 chain W_{0,2,1,0} (O(N^2) — larger odd-N grid)
    pts2 = []
    for N in (101, 151, 201, 301, 401):
        M = (N - 1) // 2
        s = [mp.log(2 * mp.sin(j * mp.pi / N)) for j in range(1, N)]
        pref = [mp.mpf(0)]
        for v in s:
            pref.append(pref[-1] + v)
        inner = mp.fsum(mp.exp(2 * (pref[M + k] - pref[k]) - pref[M]) for k in range(M + 1))
        r = 2 * mp.pi / N * (2 * mp.log(N) + mp.log(inner))
        pts2.append((N, r))
        print(f"    chain   N={N}: r_N = {mp.nstr(r, 10)}")
    v_b2 = rate_fit(pts2)
    err_b2 = abs(v_b2 - VOL_4G)
    print(f"    chain fit V = {mp.nstr(v_b2, 12)}  vs 4G = {mp.nstr(VOL_4G, 12)}  err {mp.nstr(err_b2, 3)}")
    a3_ok = err_b1 < mp.mpf("0.01") and err_b2 < mp.mpf("0.01")
    results["a3_vol_fit_whitehead_link"] = mp.nstr(v_b1, 15)
    results["a3_vol_fit_chain_b2"] = mp.nstr(v_b2, 15)
    results["a3_target_4G"] = mp.nstr(VOL_4G, 15)
    results["a3_ok"] = bool(a3_ok)
    print(f"    A3 {'PASSED' if a3_ok else 'FAILED'}\n")

    # A4: structural facts for the Lean bricks.
    print("A4  structural: positivity, log identity, even-N vanish, modulus identity")
    ok_pos = all(S_nk(N, (N - 1) // 2, k) > 0
                 for N in (5, 9, 13) for k in range(0, (N - 1) // 2 + 1))
    # log identity at (N,n,k) samples
    ok_log = True
    for (N, n, k) in ((9, 4, 2), (13, 6, 3), (15, 7, 0)):
        s = [mp.log(2 * mp.sin(j * mp.pi / N)) for j in range(1, N)]
        pref = [mp.mpf(0)]
        for v in s:
            pref.append(pref[-1] + v)
        lhs = mp.log(S_nk(N, n, k))
        rhs = 2 * (pref[n + k] - pref[k]) - pref[n]
        ok_log = ok_log and abs(lhs - rhs) < mp.mpf("1e-35")
    # even-N b>=2 vanishing of the generic-t form near the root
    h6 = 1j * (2 * mp.pi / 6 + delta)
    vanish = abs(J_vdv_t(6, 0, 2, 1, 0, h6))
    ok_vanish = vanish < mp.mpf("1e-10")
    # modulus identity for the chain
    ok_mod = True
    for N in (5, 7, 9):
        M = (N - 1) // 2
        inner = mp.fsum(S_nk(N, M, k) for k in range(M + 1))
        ok_mod = ok_mod and abs(abs(J_kashaev_chain(N, 0, 2, 1, 0)) - N ** 2 * inner) < mp.mpf("1e-30") * N ** 2 * inner
    a4_ok = ok_pos and ok_log and ok_vanish and ok_mod
    results["a4_positivity"] = bool(ok_pos)
    results["a4_log_identity"] = bool(ok_log)
    results["a4_even_N_vanish"] = mp.nstr(vanish, 3)
    results["a4_modulus_identity"] = bool(ok_mod)
    results["a4_ok"] = bool(a4_ok)
    print(f"    positivity {ok_pos}, log identity {ok_log}, "
          f"even-N |J|={mp.nstr(vanish, 3)}, modulus identity {ok_mod}")
    print(f"    A4 {'PASSED' if a4_ok else 'FAILED'}\n")

    results["all_ok"] = bool(a1_ok and a2_ok and a3_ok and a4_ok)
    return results


def main() -> int:
    mp.mp.dps = 60
    print(__doc__.split("\n")[0])
    print(f"  target 4G = {mp.nstr(VOL_4G, 20)}\n")
    results = run_anchors()

    import subprocess
    try:
        commit_sha = subprocess.run(
            ["git", "log", "-1", "--format=%H"],
            capture_output=True, text=True, cwd=Path(__file__).parent,
            check=True,
        ).stdout.strip()
    except Exception:
        commit_sha = "unknown"
    witness = {
        "engine": "mpmath",
        "scriptFile": "whitehead_vdv_lemma1.py",
        "commitSha": commit_sha,
        "description": (
            "van der Veen Whitehead-chain colored Jones (arXiv:math/0611181 "
            "Lemma 1 + generic-t tangle formula) — first corpus transcription "
            "with 4-anchor verification (internal t-form vs sin-form; external "
            "Borromean vs GL2011/Habiro; volume rate -> 4G for W-link b=1 and "
            "2-belt chain b=2; structural positivity/log-identity/vanishing/"
            "modulus facts for the Lean W3-W5 bricks)"
        ),
        "computation": "whitehead_vdv_lemma1",
        "audit_only": True,
        "precision_dps": 60,
        "source": "library/arxiv-math-0611181v2/0611181v2.pdf (owner commit 8ffce0a1); Habiro cross-ref library/1172-3/1172-3.pdf",
        **results,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).with_name("whitehead-vdv-lemma1.witness.json")
    out.write_text(json.dumps(witness, indent=1) + "\n")
    print(f"witness -> {out.name}")
    print("ALL ANCHORS PASSED" if results["all_ok"] else "ANCHOR FAILURE — do not proceed to W2")
    return 0 if results["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
