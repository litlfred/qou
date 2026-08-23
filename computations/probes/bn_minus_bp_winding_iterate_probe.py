#!/usr/bin/env python3
"""𝓑_n−𝓑_p winding-iterate tower: the parity-preserving candidate, REFUTED
(item-A follow-on, continuation of bn_minus_bp_brane_tower_parity_probe).

The companion probe `bn_minus_bp_brane_tower_parity_probe.py` showed the canonical
A-nucleon (strand-count) brane-tower fails the §4a Jacobi–Anger test on a parity
obstruction: the bar-odd order-parity alternates odd/even/odd with A, so the
odd-order single-x test is undefined at the even (n=6) level.

The natural next candidate (owner-proposed) is the SINGLE-NUCLEON WINDING ITERATE
β^k on the same 3 strands: β_p^k = atom_canonical_crossings(1,0,…) repeated k times,
β_n^k likewise. This stays in H₃ (λ ⊢ 3 only) and increases the Laurent degree with
k, so it CAN reach high orders {7,9,11,…}. The question: does it preserve odd parity,
and does the §4a single-x over-determination residual shrink as k grows?

Findings (this probe; see docs/audits/2026-06-19-bn-bp-brane-tower-parity-obstruction.md
§"Winding iterate"):

  1. ROOT CAUSE — order-parity = crossing-count parity. The Hoefsmit factors are
     degree-±1 in q, so χ_λ(word) has Laurent-exponent parity = (word length) mod 2.
     The nucleon word has odd length (11 crossings), so β^k has order-parity = k mod 2:
     odd k → odd orders {1,3,5,…}; even k → even orders. The winding tower ALTERNATES
     parity exactly like the A-nucleon strand tower (whose length is 11·A). One unified
     cause for both obstructions.

  2. The odd-k subtower (k=1,3,5,7) DOES preserve odd parity — so it is the honest
     convergence test. Its §4a single-x residual does NOT shrink: 6.84% (k=1) →
     no single-x solution (k=3) → ~95–100% (k=5) → erratic (k=7). A genuine
     Hahn–Exton q-Bessel tower would shrink monotonically toward 0. REFUTED.

  3. Combined verdict: the §4a keystone's two most natural first-principles
     embeddings — A-nucleon strand tower and single-nucleon winding tower — are BOTH
     refuted. The true brane-tower embedding (if the q-Bessel identification holds) is
     neither; a valid odd-parity-preserving tower needs even-length increments that
     still inject new odd-degree content, which neither construction provides. TIERED;
     nothing wired; c₃/Q_β stay cal-anchored.

Run:  PYTHONPATH=computations:computations/hecke:computations/qbeta:tools/pyhecke/python:tools/qou-substrate/python:computations/substrate \
        python3 -u computations/probes/bn_minus_bp_winding_iterate_probe.py
"""
import sys
import time
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

t0 = time.time()


def log(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


def main():
    import sympy as sp
    from mpmath import mp, mpf, besselj, findroot
    set_compute_dps()

    from hoefsmit_symbolic import chi_lambda_symbolic, Q
    from canonical_braid_crossings import atom_canonical_crossings
    from wedderburn_jones_markov import y_lambda_at
    try:
        from qou_substrate.constants import q_at
    except Exception:  # pragma: no cover
        from substrate.qou_substrate.constants import q_at  # type: ignore

    PARTS = [(3,), (2, 1), (1, 1, 1)]

    def laurent_coeffs(expr):
        e = sp.cancel(sp.together(expr))
        num, den = sp.fraction(e)
        dp = sp.Poly(sp.expand(den), Q)
        md, cd = dp.monoms()[0][0], dp.coeffs()[0]
        npy = sp.Poly(sp.expand(num), Q)
        return {m[0] - md: sp.nsimplify(c / cd)
                for m, c in zip(npy.monoms(), npy.coeffs())}

    def bar_odd(expr):
        c = laurent_coeffs(expr)
        ks = sorted({abs(k) for k in c if k != 0})
        return {k: (c.get(k, 0) - c.get(-k, 0)) for k in ks
                if k > 0 and (c.get(k, 0) - c.get(-k, 0)) != 0}

    def tower_W(k, q):
        """physical bar-odd tower coeffs W_order = Σ_λ y_λ(3,q)·baro_λ^{(k)}[order]."""
        y = {tuple(kk): mpf(str(v)) for kk, v in y_lambda_at(3, q).items()}
        bp, bn = (atom_canonical_crossings(1, 0, include_inter=False) * k,
                  atom_canonical_crossings(0, 1, include_inter=False) * k)
        W, orders = {}, set()
        for lam in PARTS:
            bo = bar_odd(sp.cancel(chi_lambda_symbolic(lam, bn)
                                   - chi_lambda_symbolic(lam, bp)))
            orders |= set(bo.keys())
            for o, v in bo.items():
                W[o] = W.get(o, mpf(0)) + y[lam] * mpf(str(sp.nsimplify(v)))
        return W, sorted(orders)

    def single_x_residual(W, orders):
        if not all(W.get(o, mpf(0)) != 0 for o in (1, 3, 5)):
            return None, None, None
        R31 = W[3] / W[1]
        x = None
        for seed in ("2", "3", "4", "4.5", "6", "8", "10", "12"):
            try:
                xx = findroot(lambda x: besselj(3, x) / besselj(1, x) - R31, mpf(seed))
                if abs(besselj(3, xx) / besselj(1, xx) - R31) < mpf("1e-20"):
                    x = xx
                    break
            except Exception:
                pass
        if x is None:
            return "no-solution", None, None
        highs = [o for o in orders if o >= 5 and o % 2 == 1 and W.get(o, mpf(0)) != 0]
        res5 = abs(besselj(5, x) / besselj(1, x) - W[5] / W[1]) / abs(W[5] / W[1])
        maxr = max(abs(besselj(o, x) / besselj(1, x) - W[o] / W[1]) / abs(W[o] / W[1])
                   for o in highs)
        return x, res5, maxr

    assertions = []

    # ── root cause: order-parity = (word length) mod 2 ──
    log("=== root cause: bar-odd order-parity = crossing-count parity ===")
    parity_rows = []
    parity_ok = True
    for k in (1, 2, 3):
        _, orders = tower_W(k, mpf(str(q_at())))
        pars = {o % 2 for o in orders}
        parity = "odd" if pars == {1} else "even" if pars == {0} else "mixed"
        expected = "odd" if (11 * k) % 2 == 1 else "even"
        ok = (parity == expected)
        parity_ok = parity_ok and ok
        parity_rows.append({"k": k, "word_length": 11 * k, "orders": orders,
                            "parity": parity, "expected_from_length": expected})
        log(f"  k={k}: L={11 * k} ({'odd' if 11 * k % 2 else 'even'} length) "
            f"-> orders {orders} parity={parity}  [{'OK' if ok else 'MISMATCH'}]")
    assertions.append(("order_parity_equals_crossing_count_parity", parity_ok, True))

    # ── odd-k subtower convergence test (the honest §4a test) ──
    log("=== odd-k winding subtower: does the §4a residual shrink? ===")
    qp = mpf(str(q_at()))
    tower = []
    for k in (1, 3, 5, 7):
        W, orders = tower_W(k, qp)
        x, res5, maxr = single_x_residual(W, orders)
        odd_orders = [o for o in orders if o % 2 == 1]
        if x == "no-solution":
            log(f"  k={k}: L={11 * k} odd_orders={odd_orders} -> NO single-x "
                f"solution near Bessel ratios")
            tower.append({"k": k, "word_length": 11 * k, "odd_orders": odd_orders,
                          "single_x": None, "res_W5": None, "res_max": None,
                          "note": "no single-x solution"})
        elif x is None:
            tower.append({"k": k, "word_length": 11 * k, "odd_orders": odd_orders,
                          "single_x": None, "res_W5": None, "res_max": None,
                          "note": "odd orders 1/3/5 not all present"})
        else:
            log(f"  k={k}: L={11 * k} x*={mp.nstr(x, 7)}  res(W5)="
                f"{float(res5) * 100:.2f}%  res(max over ≥5)={float(maxr) * 100:.2f}%")
            tower.append({"k": k, "word_length": 11 * k, "odd_orders": odd_orders,
                          "single_x": mp.nstr(x, 12),
                          "res_W5": mp.nstr(res5, 6),
                          "res_max": mp.nstr(maxr, 6)})

    # Refutation: residual does not shrink monotonically toward 0.
    res_seq = [float(t["res_max"]) for t in tower
               if t.get("res_max") is not None]
    converges = (len(res_seq) >= 2 and all(
        res_seq[i + 1] < res_seq[i] for i in range(len(res_seq) - 1))
        and res_seq[-1] < 0.01)
    log(f"  max-residual sequence (where defined): "
        f"{[f'{r * 100:.1f}%' for r in res_seq]}")
    log(f"  shrinks monotonically toward 0 (<1%)? {converges} -> "
        f"{'CONVERGES' if converges else 'REFUTED (no q-Bessel convergence)'}")
    assertions.append(("winding_subtower_residual_does_not_converge",
                       not converges, True))

    _emit_witness(parity_rows, tower, converges, assertions, float(qp))

    ok = all(a[1] == a[2] for a in assertions)
    log(f"all assertions: {'PASS' if ok else 'FAIL'}")
    for name, got, exp in assertions:
        log(f"  [{'OK' if got == exp else 'XX'}] {name}: {got}")
    return 0 if ok else 1


def _emit_witness(parity_rows, tower, converges, assertions, q0):
    import hashlib
    import json
    import os
    import subprocess

    here = os.path.dirname(os.path.abspath(__file__))
    script = os.path.abspath(__file__)
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", script],
            cwd=here, text=True).strip()
    except Exception:
        sha = None
    with open(script, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]

    out = {
        "name": "bn-minus-bp-winding-iterate",
        "description": "The single-nucleon winding iterate β^k on 3 strands as the "
                       "§4a brane-tower candidate (parity-preserving alternative to "
                       "the A-nucleon strand tower). Root cause: bar-odd order-parity "
                       "= (word length=11k) mod 2, so parity alternates with k exactly "
                       "as the strand tower alternates with A. The odd-k subtower "
                       "preserves odd parity but its §4a single-x over-determination "
                       "residual does NOT shrink (6.84% at k=1 → no-solution k=3 → "
                       "~95-100% k=5 → erratic k=7) — REFUTED. Both natural embeddings "
                       "(strand + winding) fail the §4a q-Bessel keystone. TIERED; "
                       "nothing wired.",
        "auditOnly": True,
        "probe": True,
        "substrate": {"q0_proton": q0, "q0_pin": "proton (canonical)"},
        "candidate": {
            "name": "single-nucleon winding iterate β^k (H_3, λ⊢3)",
            "beta_p_k": "atom_canonical_crossings(1,0,include_inter=False) * k",
            "beta_n_k": "atom_canonical_crossings(0,1,include_inter=False) * k",
            "committed_a_priori": True,
        },
        "root_cause": {
            "statement": "bar-odd order-parity = (Hecke word length) mod 2 "
                         "(Hoefsmit factors are degree ±1 in q); nucleon word "
                         "length = 11 (odd), so β^k parity = k mod 2",
            "parity_by_k": parity_rows,
        },
        "winding_subtower_test": tower,
        "verdict": {
            "converges_to_q_bessel": converges,
            "reading": "REFUTED — odd-k winding residual does not shrink toward 0; "
                       "not the Hahn-Exton q-Bessel tower object",
            "combined": "both natural embeddings refuted: A-nucleon strand tower "
                        "(parity obstruction at even levels) + winding iterate "
                        "(non-convergent odd-k subtower)",
        },
        "assertions": [
            {"name": n, "computed": (g if isinstance(g, (bool, str)) else str(g)),
             "expected": e, "ok": g == e}
            for (n, g, e) in assertions
        ],
        "witness": {"scriptCommitSha": sha, "scriptHash": script_hash,
                    "producer": "computations/probes/bn_minus_bp_winding_iterate_probe.py"},
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(here, "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    dest = os.path.join(here, "..", "bn-minus-bp-winding-iterate.witness.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"[witness] wrote {os.path.normpath(dest)}", flush=True)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)
