#!/usr/bin/env python3
"""𝓑_n−𝓑_p brane-tower: χ_λ difference + the §4a tower-convergence parity gate
(item-A follow-on to PR #2485; tower test of doc 2026-06-17 §"decisive tower test").

The §4a Jacobi–Anger tower test (`qbeta_reeb_tower_jacobi_anger_physical_weight.py`,
doc `2026-06-13-reeb-phase-qbessel-identification.md` §4a) checks whether the bar-odd
brane-tower sector of χ_λ(𝓑_n−𝓑_p) is the Hahn–Exton q-Bessel matrix coefficient: its
`sinh((2m+1)η)` coefficients should be `2·J_{2m+1}(x)` at a single substrate-fixed x,
with the over-determination residual shrinking toward 0 as the tower extends
n = 3 → 6 → 9. At n=3 the physical-weight residual is 6.8% (proved-closed-form data);
the decisive gate is whether it shrinks at n=6, 9.

Doc 2026-06-17 §"decisive tower test" flagged the BLOCKER: there is no H₆/H₉
χ_λ(𝓑_n−𝓑_p) in the corpus — the explicit proton/neutron braids exist only at H₃ —
and producing them at higher levels is a *first-principles braid construction*, not a
mechanical evaluation. This probe commits, a priori, to the single most principled
embedding and reports whatever it gives (formalize-first: NO scan-over-embeddings-to-fit):

    CANONICAL A-NUCLEON EMBEDDING (committed before seeing any residual):
      β_p^{(A)} = atom_canonical_crossings(A, 0, include_inter=False)   [A free protons]
      β_n^{(A)} = atom_canonical_crossings(0, A, include_inter=False)   [A free neutrons]
      level n = 3A;  difference object χ_λ(β_n^{(A)} − β_p^{(A)}),  λ ⊢ n.
    Rationale: the literal A→A generalization of the SAME canonical word-builder that
    reproduces the Lean-proved H₃ closed forms at A=1 (intra-only, matching the
    single-nucleon convention); level = 3A matches the brane-tower / Hecke structure.

Computed exactly via the symbolic Hoefsmit engine (`hoefsmit_symbolic`). Findings
(see docs/audits/2026-06-19-bn-bp-brane-tower-parity-obstruction.md):

  1. n=3 VALIDATES: reproduces the three Lean-proved closed forms and the canonical
     BAR_ODD_COEFFS exactly; the §4a physical-weight single-x residual is 6.84%
     (x*≈4.5249), matching the harness on main.
  2. bar-involution invariant HOLDS: bar-odd coeffs of χ_{λ'} = −(bar-odd of χ_λ);
     the embedding passes the structural gate.
  3. PARITY OBSTRUCTION: the bar-odd order-parity ALTERNATES with A — odd {1,3,5} at
     n=3, EVEN {2,…,16} at n=6, odd again at n=9. At n=6 the odd-order tower coeffs
     W₁=W₃=W₅ vanish identically, so the §4a single-x test W₃/W₁=J₃(x)/J₁(x) is
     0/0 — UNDEFINED. The naive tower extension does not work for this embedding; a
     valid brane-tower embedding must PRESERVE odd order-parity and fill {7,9,11}.

Nothing wired; TIERED; c₃/Q_β stay cal-anchored regardless.

Run:  PYTHONPATH=computations:tools/pyhecke/python:tools/qou-substrate/python:computations/substrate:computations/qbeta \
        python3 -u computations/probes/bn_minus_bp_brane_tower_parity_probe.py
"""
import sys
import time
# Path bridge: puts computations/ and every cluster subdir (incl. substrate/,
# where _precision lives) on sys.path, so the bare-name import below resolves
# without the PYTHONPATH prefix in the docstring. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

t0 = time.time()


def log(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


def conjugate(shape):
    if not shape:
        return ()
    m = shape[0]
    return tuple(sum(1 for r in shape if r > j) for j in range(m))


# Canonical n=3 bar-odd sinh-order coefficients (the §4a reference; rational,
# anchor-independent), reproduced from qbeta_reeb_tower_jacobi_anger_physical_weight.
CANON_BAR_ODD_N3 = {
    (3,): {3: (-1, 4), 5: (-1, 4)},
    (2, 1): {1: (1, 2), 3: (-1, 2)},
    (1, 1, 1): {3: (-1, 4), 5: (-1, 4)},
}


def main():
    import sympy as sp
    from fractions import Fraction as Fr
    from mpmath import mp, mpf, besselj, findroot
    set_compute_dps()

    from hoefsmit_symbolic import chi_lambda_symbolic, Q
    from canonical_braid_crossings import atom_canonical_crossings
    from wedderburn_jones_markov import y_lambda_at
    # Canonical shared partition enumerator (centralized; per Gemini review on
    # #2496 — no duplicated local helper). hoefsmit_symbolic above triggers
    # _path_bridge, putting computations/hecke on the path.
    from hecke_characters import partitions_of  # noqa: E402
    try:
        from qou_substrate.constants import q_at, q_muon_at
    except Exception:  # pragma: no cover
        from substrate.qou_substrate.constants import q_at, q_muon_at  # type: ignore

    def chi_diff(lam, A):
        """Exact symbolic χ_λ(β_n^{(A)} − β_p^{(A)}) under the canonical embedding."""
        bp = atom_canonical_crossings(A, 0, include_inter=False)
        bn = atom_canonical_crossings(0, A, include_inter=False)
        return sp.cancel(chi_lambda_symbolic(lam, bn) - chi_lambda_symbolic(lam, bp))

    def laurent_coeffs(expr):
        """k -> exact rational coeff of q^k (expr must be a Laurent polynomial)."""
        e = sp.cancel(sp.together(expr))
        num, den = sp.fraction(e)
        dp = sp.Poly(sp.expand(den), Q)
        assert len(dp.monoms()) == 1, f"denominator not a monomial: {den}"
        md, cd = dp.monoms()[0][0], dp.coeffs()[0]
        npy = sp.Poly(sp.expand(num), Q)
        return {m[0] - md: sp.nsimplify(c / cd)
                for m, c in zip(npy.monoms(), npy.coeffs())}

    def bar_odd(expr):
        """order k>0 -> sinh(kη) coefficient = a_k − a_{-k} (nonzero only)."""
        c = laurent_coeffs(expr)
        ks = sorted({abs(k) for k in c if k != 0})
        out = {}
        for k in ks:
            if k <= 0:
                continue
            v = sp.simplify(c.get(k, 0) - c.get(-k, 0))
            if v != 0:
                out[k] = v
        return out

    assertions = []
    levels = []

    # ── n=3: validate vs proved closed forms + canonical BAR_ODD_COEFFS ──
    log("=== n=3 (A=1): validate vs proved closed forms ===")
    closed = {
        (3,): -(Q**2 + 1)**2 * (Q**2 - 1) / (4 * Q),
        (2, 1): -(Q**4 + 1) * (Q**2 - 1) / (4 * Q**3),
        (1, 1, 1): -(Q**2 + 1)**2 * (Q**2 - 1) / (4 * Q**5),
    }
    n3_bar = {}
    n3_match = True
    for lam in partitions_of(3):
        d = chi_diff(lam, 1)
        cf_ok = sp.simplify(d - closed[lam]) == 0
        bo = bar_odd(d)
        n3_bar[lam] = bo
        canon = {k: sp.Rational(*v) for k, v in CANON_BAR_ODD_N3[lam].items()}
        bo_ok = (bo == canon)
        n3_match = n3_match and cf_ok and bo_ok
        log(f"  λ={lam!s:10s} closed-form={'OK' if cf_ok else 'MISMATCH'}  "
            f"bar-odd={ {k: str(v) for k, v in bo.items()} }  "
            f"vs canonical={'OK' if bo_ok else 'MISMATCH'}")
    assertions.append(("n3_reproduces_proved_closed_forms_and_canonical_bar_odd",
                       n3_match, True))

    # ── bar-involution invariant + parity, at n=3 and n=6 ──
    def analyze_level(A):
        n = 3 * A
        log(f"=== n={n} (A={A}): bar-odd decomposition + invariants ===")
        bar = {}
        all_orders = set()
        for lam in partitions_of(n):
            d = chi_diff(lam, A)
            bo = bar_odd(d)
            bar[lam] = bo
            all_orders |= set(bo.keys())
        # Conjugation invariant: bar-odd[λ'] = s · bar-odd[λ] for a single
        # level-wide sign s ∈ {+1, −1}. Empirically s = (−1)^(A−1) — itself
        # parity-graded (s=+1 at n=3, s=−1 at n=6), reinforcing the order-parity
        # alternation below. Detect s and assert it is consistent across all λ.
        def matches(a, b, sign):
            return a == {k: sp.simplify(sign * v) for k, v in b.items()}
        s_pos = all(matches(bar.get(conjugate(lam), {}), bo, +1)
                    for lam, bo in bar.items())
        s_neg = all(matches(bar.get(conjugate(lam), {}), bo, -1)
                    for lam, bo in bar.items())
        sign = +1 if s_pos else (-1 if s_neg else 0)
        expected_sign = (-1) ** (A - 1)
        invol_ok = (sign == expected_sign) and sign != 0
        parities = {k % 2 for k in all_orders}
        parity = ("odd" if parities == {1} else "even" if parities == {0}
                  else ("mixed" if parities else "empty"))
        log(f"  bar-odd orders present: {sorted(all_orders)}  -> parity={parity}")
        log(f"  conjugation invariant bar-odd[λ']=s·bar-odd[λ]: "
            f"s={sign:+d} (expected (−1)^(A−1)={expected_sign:+d}) "
            f"-> {'HOLDS' if invol_ok else 'FAILS'}")
        return n, bar, sorted(all_orders), parity, invol_ok, sign

    level_data = {}
    for A in (1, 2):
        n, bar, orders, parity, invol_ok, sign = analyze_level(A)
        level_data[A] = (bar, orders, parity, invol_ok, sign)
        assertions.append(
            (f"conjugation_invariant_sign_{'+' if sign > 0 else '-'}1_n{n}",
             invol_ok, True))

    # n=9 parity confirmation on cheap irreps (full p(9) symbolic is expensive
    # and moot given the n=6 obstruction): just confirm the parity flips back.
    log("=== n=9 (A=3): parity confirmation on cheap irreps ===")
    n9_orders = set()
    for lam in [(9,), (8, 1)]:
        bo = bar_odd(chi_diff(lam, 3))
        n9_orders |= set(bo.keys())
        log(f"  λ={lam!s:8s} bar-odd orders {sorted(bo.keys())}")
    n9_parity = ("odd" if {k % 2 for k in n9_orders} == {1}
                 else "even" if {k % 2 for k in n9_orders} == {0} else "mixed")
    log(f"  n=9 parity (cheap subset) = {n9_parity}")
    assertions.append(("parity_alternates_odd_even_odd_for_A_1_2_3",
                       (level_data[1][2], level_data[2][2], n9_parity)
                       == ("odd", "even", "odd"), True))

    # ── §4a single-x over-determination residual at each level (where defined) ──
    def physical_W(n, q, bar):
        y = {tuple(k): mpf(str(v)) for k, v in y_lambda_at(n, q).items()}
        W = {}
        for lam, bo in bar.items():
            yl = y.get(lam, mpf(0))
            for k, v in bo.items():
                W[k] = W.get(k, mpf(0)) + yl * mpf(str(sp.nsimplify(v)))
        return W

    def single_x_residual(W):
        if not all(W.get(k, mpf(0)) != 0 for k in (1, 3, 5)):
            return None, None
        R31 = W[3] / W[1]
        x = findroot(lambda x: besselj(3, x) / besselj(1, x) - R31, mpf("4.5"))
        pred = besselj(5, x) / besselj(1, x)
        return x, abs(pred - W[5] / W[1]) / abs(W[5] / W[1])

    log("=== §4a single-x over-determination residual (proton anchor) ===")
    qp = mpf(str(q_at()))
    tower = []
    n3_bar_full = {lam: n3_bar[lam] for lam in partitions_of(3)}
    for A, bar in ((1, n3_bar_full), (2, level_data[2][0])):
        n = 3 * A
        W = physical_W(n, qp, bar)
        x, resid = single_x_residual(W)
        if x is not None:
            log(f"  n={n}: single-x={mp.nstr(x, 8)}  residual={mp.nstr(resid, 6)} "
                f"({float(resid) * 100:.2f}%)")
            tower.append({"n": n, "odd_orders_present": True,
                          "single_x": mp.nstr(x, 12),
                          "overdet_residual": mp.nstr(resid, 8)})
        else:
            log(f"  n={n}: UNDEFINED — odd orders {{1,3,5}} vanish "
                f"(W_1={mp.nstr(W.get(1, mpf(0)), 4)}); §4a test inapplicable "
                f"(parity obstruction)")
            tower.append({"n": n, "odd_orders_present": False,
                          "single_x": None, "overdet_residual": None,
                          "reason": "odd-order tower coeffs vanish (even-parity level)"})
    assertions.append(("n6_single_x_test_undefined_parity_obstruction",
                       tower[1]["odd_orders_present"] is False, True))

    _emit_witness(level_data, n3_bar, n9_parity, tower, assertions, float(qp))

    ok = all(a[1] == a[2] for a in assertions)
    log(f"all assertions: {'PASS' if ok else 'FAIL'}")
    for name, got, exp in assertions:
        log(f"  [{'OK' if got == exp else 'XX'}] {name}: {got}")
    return 0 if ok else 1


def _emit_witness(level_data, n3_bar, n9_parity, tower, assertions, q0):
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

    def bar_to_json(bar):
        return {str(list(lam)): {str(k): str(v) for k, v in bo.items()}
                for lam, bo in bar.items()}

    out = {
        "name": "bn-minus-bp-brane-tower-parity",
        "description": "χ_λ(𝓑_n−𝓑_p) at brane-tower levels n=3,6 (exact symbolic "
                       "Hoefsmit) under the canonical A-nucleon embedding "
                       "β^{(A)}=atom_canonical_crossings(A or 0,...,include_inter=False). "
                       "The §4a Jacobi–Anger tower-convergence test (doc 2026-06-17): "
                       "n=3 reproduces the proved closed forms + 6.84% residual; the "
                       "bar-involution invariant holds; but the bar-odd order-parity "
                       "ALTERNATES with A (odd n=3, even n=6, odd n=9), so at n=6 the "
                       "odd-order tower coeffs vanish and the §4a single-x test is 0/0 "
                       "undefined — a parity obstruction. A valid brane-tower embedding "
                       "must preserve odd order-parity. TIERED; nothing wired.",
        "auditOnly": True,
        "probe": True,
        "substrate": {"q0_proton": q0, "q0_pin": "proton (canonical)"},
        "embedding": {
            "name": "canonical A-nucleon (free, same-type)",
            "beta_p": "atom_canonical_crossings(A, 0, include_inter=False)",
            "beta_n": "atom_canonical_crossings(0, A, include_inter=False)",
            "level": "n = 3A",
            "committed_a_priori": True,
            "rationale": "literal A->A generalization of the canonical word-builder "
                         "that reproduces the proved H_3 closed forms at A=1",
        },
        "n3_bar_odd_coefficients": bar_to_json(n3_bar),
        "n6_bar_odd_coefficients": bar_to_json(level_data[2][0]),
        "parity_by_level": {
            "n3_A1": level_data[1][2],
            "n6_A2": level_data[2][2],
            "n9_A3_cheap_subset": n9_parity,
            "finding": "order-parity alternates odd/even/odd with A=1,2,3",
        },
        "tower_convergence_test": tower,
        "conjugation_invariant": {
            "statement": "bar-odd(χ_{λ'}) = s·bar-odd(χ_λ), single level-wide "
                         "sign s = (−1)^(A−1) (parity-graded: +1 at n=3, −1 at n=6)",
            "n3_sign": level_data[1][4],
            "n3_holds": level_data[1][3],
            "n6_sign": level_data[2][4],
            "n6_holds": level_data[2][3],
        },
        "assertions": [
            {"name": n, "computed": (g if isinstance(g, (bool, str, list, tuple))
                                     else str(g)), "expected": e, "ok": g == e}
            for (n, g, e) in assertions
        ],
        "witness": {"scriptCommitSha": sha, "scriptHash": script_hash,
                    "producer": "computations/probes/bn_minus_bp_brane_tower_parity_probe.py"},
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(here, "..", "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    dest = os.path.join(here, "..", "bn-minus-bp-brane-tower-parity.witness.json")
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
