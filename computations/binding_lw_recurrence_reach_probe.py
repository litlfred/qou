#!/usr/bin/env python3
"""Does the depth-2 binding kernel R = x²−τx+1 PREDICT the selection-rule values
`lw(c)` beyond its three anchors (c = 1,2,3)?  — a falsifiable reach test (no fit).

Context (bean z2bn / lever 1; PR #2718 landed the kernel + spectral bridge)
---------------------------------------------------------------------------
The binding generating function obeys a depth-2 recurrence  a_{n+2} = τ·a_{n+1} − a_n
(det=1 symplectic; `R(q,x) = x² − τx + 1`).  The SW-period anchors are the canonical
selection-rule values

    lw(c) = (1/(c+1)) · Σ_{λ ⊢ c+1} dim_q(V_λ),   dim_q = [n]_q! / ∏_x [h_x]_q

(balanced quantum integers, q-hook-length formula).  `binding_selection_rule_tau_closure.py`
fixes  τ = (lw(1)+lw(3))/lw(2)  from the THREE anchors c=1,2,3 and then *defines* the
odd-partner a_5 := τ·lw(3) − lw(2).  It never checks that this recurrence prediction
equals the INDEPENDENTLY-computed lw(4) = (1/5)·Σ_{λ⊢5} dim_q.

This probe runs exactly that cross-check at c = 4 and c = 5:
    predicted:  â(c) = τ·lw(c−1) − lw(c−2)   (depth-2 recurrence, τ from c≤3 anchors)
    direct:     lw(c) = (1/(c+1)) Σ_{λ⊢c+1} dim_q   (canonical q-hook)
and reports the relative error.  If they agree, the depth-2 kernel genuinely generates
the selection rule (strong validation beyond the anchors).  If they differ, the depth-2
*constant* kernel is anchor-limited at c≤3 — consistent with the corpus note that a
constant kernel of depth ≤ 3 is refuted and the true object is a non-constant / higher-
depth kernel (`2026-06-04-c4-gap-no-constant-kernel-recursion.md`).

No fit: τ is fixed by the c≤3 anchors; lw(4), lw(5) are computed from dim_q with nothing
tuned.  q₀ enters only as the evaluation point.
"""
import json
import sys
import mpmath as mp

mp.mp.dps = 50


def q0_value():
    try:
        from qou_substrate.constants import q_at  # noqa
        return mp.mpf(str(q_at("proton")))
    except Exception:
        return mp.mpf("1.1099785900594")


Q0 = q0_value()


def qint(m, q):
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def q_factorial(m, q):
    r = mp.mpf(1)
    for k in range(1, m + 1):
        r *= qint(k, q)
    return r


def partitions(n, _max=None):
    if _max is None:
        _max = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, _max), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hooks(lam):
    lam = list(lam)
    cols = [0] * (lam[0] if lam else 0)
    for r in lam:
        for j in range(r):
            cols[j] += 1
    hs = []
    for i, r in enumerate(lam):
        for j in range(r):
            hs.append((r - 1 - j) + (cols[j] - 1 - i) + 1)
    return hs


def dim_q(lam, q):
    den = mp.mpf(1)
    for h in hooks(lam):
        den *= qint(h, q)
    return q_factorial(sum(lam), q) / den


def lw(c, q):
    """lw(c) = (1/(c+1)) Σ_{λ ⊢ c+1} dim_q(V_λ)."""
    n = c + 1
    s = mp.fsum(dim_q(lam, q) for lam in partitions(n))
    return s / (c + 1)


def main():
    q = Q0
    print(f"q_0 = {mp.nstr(q, 12)}")
    lws = {c: lw(c, q) for c in range(1, 6)}        # c = 1..5  (direct, canonical dim_q)
    for c in range(1, 6):
        print(f"  lw({c}) = (1/{c+1})Σ_(λ⊢{c+1}) dim_q = {mp.nstr(lws[c], 14)}")

    # τ fixed by the THREE anchors c=1,2,3 (the recurrence a_{c+1}=τ a_c − a_{c-1} at c=2)
    tau = (lws[1] + lws[3]) / lws[2]
    print(f"\n  τ (from c≤3 anchors, = (lw1+lw3)/lw2) = {mp.nstr(tau, 14)}  [expect 2.6424]")

    # falsifiable reach test: does the depth-2 recurrence PREDICT lw(4), lw(5)?
    rows = []
    for c in (4, 5):
        pred = tau * lws[c - 1] - lws[c - 2]          # depth-2 prediction
        direct = lws[c]                                # canonical dim_q
        rel = abs(pred - direct) / abs(direct)
        rows.append({
            "c": c,
            "lw_direct": mp.nstr(direct, mp.mp.dps),
            "recurrence_predicted": mp.nstr(pred, mp.mp.dps),
            "abs_err": mp.nstr(abs(pred - direct), 8),
            "rel_err": mp.nstr(rel, 8),
            "agrees_1e-6": bool(rel < mp.mpf(10) ** (-6)),
        })
        print(f"\n  c={c}: depth-2 predicts {mp.nstr(pred, 12)}, "
              f"direct lw({c}) = {mp.nstr(direct, 12)}")
        print(f"        rel error = {mp.nstr(rel, 6)}  "
              f"({'AGREES' if rel < mp.mpf(10)**(-6) else 'DIFFERS'})")

    extends = all(r["agrees_1e-6"] for r in rows)
    verdict = (
        ("CONFIRM: the depth-2 kernel R=x²−τx+1 (τ from c≤3 anchors) PREDICTS lw(4),lw(5) "
         "to <1e-6 — the selection rule is genuinely depth-2-generated beyond its anchors.")
        if extends else
        (f"SCOPE-LIMITED NEGATIVE (a): the depth-2 *constant* kernel does NOT predict lw(c) "
         f"beyond its c≤3 anchors — lw(4) misses by {rows[0]['rel_err']} "
         f"(rel), lw(5) by {rows[1]['rel_err']}. τ is fixed by three anchors (det=1 + one "
         "ratio), so matching c≤3 is automatic; the c≥4 deviation shows the constant "
         "depth-2 kernel is anchor-limited, consistent with the corpus 'depth ≤ 3 constant "
         "kernel refuted; true object is non-constant/higher-depth' "
         "(2026-06-04-c4-gap-no-constant-kernel-recursion.md). NOT a structural exclusion: "
         "the proved λ₊>1 extensive-growth property (PR #2718) stands; this only bounds the "
         "constant-kernel reach. No fit; q₀ only as evaluation point.")
    )
    print("\nVERDICT:\n" + verdict)

    out = {
        "description": ("Falsifiable reach test of the depth-2 binding kernel R=x²−τx+1: "
                        "does it predict the selection-rule values lw(4),lw(5) beyond its "
                        "c≤3 anchors? lw(c)=(1/(c+1))Σ_{λ⊢c+1} dim_q (canonical q-hook). "
                        "No fit; τ from c≤3 anchors."),
        "q0": mp.nstr(q, 16),
        "dps": mp.mp.dps,
        "tau": mp.nstr(tau, mp.mp.dps),
        "lw": {str(c): mp.nstr(lws[c], mp.mp.dps) for c in range(1, 6)},
        "reach_test": rows,
        "depth2_extends_beyond_anchors": extends,
        "verdict": verdict,
    }
    wpath = "computations/binding-lw-recurrence-reach.witness.json"
    with open(wpath, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"\nwitness -> {wpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
