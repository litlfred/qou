#!/usr/bin/env python3
"""
probe_convention_d_vs_c_borromean.py — the D ≟ C check queued in the
trace-convention registry (2026-07-02 addendum of
docs/audits/2026-06-09-binding-trace-convention-split.md, PR #3261).

Question. Convention D is the Borromean single-pipeline closed form
τ_pipe = (4 + h² − 3h⁴ − h⁶)/(h² + 4) (Lean `BorromeanMarkovTrace`),
which PROBE 4 derived to be the SU(2)/Temperley–Lieb (Jones) Markov
decomposition. Convention C is the corpus-canonical Jones–Markov trace
(`markov_trace_canonical.tr_M_word`, axioms M1–M3 with
z = 1/(√q + 1/√q)). Are they the SAME evaluation at β_Bor — i.e. is
D = C at the Borromean braid word — or a third value?

Method (exact, no fit):
  * β_Bor = (σ₁ σ₂⁻¹)³ in B_3 — canonical 0-indexed (σ₀, σ₁⁻¹)³.
  * Route 1 (canonical C): expand each σ₁⁻¹ = σ₁ − h (Hecke) into the
    2³ positive subwords, evaluate `tr_M_word` symbolically in (z, h),
    substitute z = 1/(√q + 1/√q), h = q − 1/q.
  * Route 2 (recursive C): `markov_trace_recursive.markov_trace_of_word`
    on the signed 1-indexed word (1, −2, 1, −2, 1, −2).
  * Compare both, exactly (rational functions over t = √q; sympy
    `cancel` is exact/decidable there), against τ_pipe, and numerically
    at q₀ (50 dps) against the Wenzl-bridge value τ_W ≈ 0.9983666.

ANSWER (recorded): **D ≠ C, exactly.** Both C implementations agree on
the same rational function; D − C is a nonzero rational function with
value 1.9554e-4 at q₀; and C equals the symbolic Wenzl-bridge trace
Σ_λ y_λ^W·χ^λ(β_Bor) **exactly** (identical rational function — route
3, upgraded 2026-07-03 from the earlier 7-digit numeric match). So the
registry's naming tension resolves factually: the corpus-canonical
M1–M3 trace C IS the
Wenzl-bridge z-trace (one convention), and the Borromean single
pipeline / Lean `BorromeanMarkovTrace` closed form is the OTHER
convention (D, the SU(2)/TL Jones decomposition). Any consumer that
assumed the pipeline τ is the canonical tr_M value at β_Bor inherits
the 1.9554e-4 discrepancy — matters below 0.1 % precision only.

Output: probe-convention-d-vs-c-borromean.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from itertools import product
from pathlib import Path

import sympy as sp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
# computations/ itself is already on sys.path via the _path_bridge
# preamble above; only the cluster subdirs need explicit inserts.
sys.path.insert(0, str(HERE.parent / "markov"))
sys.path.insert(0, str(HERE.parent / "substrate"))

import markov_trace_recursive as R  # noqa: E402
from markov_trace_canonical import (  # noqa: E402
    tr_M_word, Z_SYMB, H_SYMB, q as HECKE_Q)
from q_parameter import Q as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# hecke/ cluster subdir is on sys.path via the _path_bridge preamble.
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic  # noqa: E402
from hecke_character_symbolic import q_character_on_braid_word  # noqa: E402


def main() -> int:
    # Work over t = √q (q = t²) so every expression is a RATIONAL
    # function of t — sympy's full `simplify` heuristic-GCD chokes on
    # mixed √q radicals; `cancel` on Q(t) is exact and decidable.
    t = sp.symbols("t", positive=True)
    z_of_t = t / (t**2 + 1)              # z = 1/(√q + 1/√q)
    h_of_t = t**2 - 1 / t**2             # h = q − 1/q

    # ── Route 1: canonical tr_M_word with σ₁⁻¹ = σ₁ − h expansion ──
    # β_Bor = (σ₀ · σ₁⁻¹)³; each σ₁⁻¹ slot contributes σ₁ (coeff 1)
    # or 1 (coeff −h).
    tr_c_sym = sp.Integer(0)
    for choice in product((True, False), repeat=3):
        word: list[int] = []
        coeff = sp.Integer(1)
        for keep in choice:
            word.append(0)
            if keep:
                word.append(1)
            else:
                coeff *= -H_SYMB
        tr_c_sym += coeff * tr_M_word(tuple(word), 3, Z_SYMB, H_SYMB)
    # Z_SYMB / H_SYMB may be expressions in the hecke_symbolic q-symbol
    # (not free symbols) — substitute the q-symbol itself as well, so
    # every residual q-subtree becomes rational in t.
    tr_c_t = sp.cancel(sp.together(
        tr_c_sym.subs({Z_SYMB: z_of_t, H_SYMB: h_of_t, HECKE_Q: t**2})))

    # ── Route 2: recursive signed-word trace (1-indexed) ──
    tr_rec = R.markov_trace_of_word(3, [1, -2, 1, -2, 1, -2])
    tr_rec_t = sp.cancel(sp.together(
        sp.sympify(tr_rec).subs({R.z_sym: z_of_t, R.q: t**2})))

    # ── Convention D: the pipeline / Lean closed form ──
    h = h_of_t
    tau_pipe = sp.cancel((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))

    d_minus_c1 = sp.cancel(sp.together(tau_pipe - tr_c_t))
    d_minus_c2 = sp.cancel(sp.together(tau_pipe - tr_rec_t))

    c1_minus_c2 = sp.cancel(sp.together(tr_c_t - tr_rec_t))

    # ── Route 3 (EXACT Wenzl bridge): tr_W = Σ_λ y_λ^W · χ^λ(β_Bor),
    # y_λ symbolic via the Wenzl bridge (witness-cached), χ^λ symbolic
    # via Hoefsmit matrices; crossings tagged "sigma" / "sigma_inv". ──
    qs = sp.symbols("q", positive=True)
    bor_crossings = [(0, "sigma"), (1, "sigma_inv")] * 3
    tr_w_sym = sp.Integer(0)
    for lam in ((3,), (2, 1), (1, 1, 1)):
        y_l = y_lambda_wenzl_bridge_symbolic(lam)
        chi_l = q_character_on_braid_word(lam, bor_crossings, qs)
        tr_w_sym += y_l * chi_l
    tr_w_t = sp.cancel(sp.together(sp.sympify(tr_w_sym).subs(qs, t**2)))
    c_minus_w = sp.cancel(sp.together(tr_c_t - tr_w_t))

    t0 = sp.sqrt(sp.Float(str(Q0), 60))
    n_c = sp.N(tr_c_t.subs(t, t0), 50)
    n_rec = sp.N(tr_rec_t.subs(t, t0), 50)
    n_pipe = sp.N(tau_pipe.subs(t, t0), 50)
    tau_w = sp.Float("0.9983666", 30)  # Wenzl-bridge value (PROBE 4 audit)

    print(f"tr_C (tr_M_word, expanded)  = {tr_c_t}")
    print(f"tr_C (recursive signed)     = {tr_rec_t}")
    print(f"tau_pipe (convention D)     = {tau_pipe}")
    print(f"C route1 − C route2         = {c1_minus_c2}")
    print(f"D − C (route 1)             = {d_minus_c1}")
    print(f"D − C (route 2)             = {d_minus_c2}")
    print(f"tr_W (exact Wenzl bridge)   = {tr_w_t}")
    print(f"C − W (exact)               = {c_minus_w}")
    print(f"numeric at q0: C (route 1)  = {n_c}")
    print(f"numeric at q0: C (route 2)  = {n_rec}")
    print(f"numeric at q0: D            = {n_pipe}")
    print(f"D − C at q0                 = {sp.N(n_pipe - n_c, 10)}")
    print(f"C − tau_W(7-digit quote)    = {sp.N(n_c - tau_w, 10)}")

    wb = WitnessBuilder("probe-convention-d-vs-c-borromean",
                        engine="sympy", output_dir=HERE)
    wb.set_description(
        "D =? C at beta_Bor: convention D (Borromean single-pipeline "
        "closed form / Lean BorromeanMarkovTrace, = SU(2)/TL Jones "
        "decomposition per PROBE 4) vs convention C (canonical "
        "Jones-Markov tr_M, markov_trace_canonical) — the one-line "
        "check queued in the trace-convention registry addendum "
        "(2026-06-09 audit, PR #3261).")
    wb.add_data("tr_C_rational_in_t_sqrtq", str(tr_c_t))
    wb.add_data("tau_pipe_rational_in_t_sqrtq", str(tau_pipe))
    wb.add_data("d_minus_c_rational_in_t_sqrtq", str(d_minus_c1))
    wb.add_data("tr_C_at_q0_50dps", str(n_c))
    wb.add_data("tau_pipe_at_q0_50dps", str(n_pipe))
    wb.add_data("d_minus_c_at_q0", str(sp.N(n_pipe - n_c, 15)))
    wb.add_data("verdict",
                "D != C EXACTLY: the Borromean single-pipeline / Lean "
                "closed form (convention D, SU(2)/TL Jones decomposition) "
                "is NOT the canonical M1-M3 Jones-Markov trace C; C "
                "coincides with the Wenzl-bridge z-trace (PROBE 4's "
                "tau_W). The registry's naming tension resolves: "
                "C = Wenzl-bridge (one convention), D = TL pipeline "
                "(another); gap 1.9554e-4 at q0.")
    wb.add_assertion(
        "c_routes_agree_exact", str(c1_minus_c2), "0",
        source="tr_M_word (Hecke-expanded) and markov_trace_recursive "
               "(signed word) must give the SAME rational function — two "
               "independent implementations of convention C")
    wb.add_assertion(
        "d_minus_c_nonzero_at_q0",
        float(sp.N(n_pipe - n_c, 15)), 1.9554e-4, tolerance=1e-6,
        source="D differs from C by the PROBE-4 gap figure — the "
               "convention split is exact, not numerical")
    wb.add_assertion(
        "c_equals_wenzl_bridge_EXACT", str(c_minus_w), "0",
        source="canonical C minus the symbolic Wenzl-bridge trace "
               "(y_lambda_wenzl_bridge_symbolic x Hoefsmit chi^lambda) "
               "cancels to 0 as a rational function — C and the Wenzl "
               "z-trace are the SAME convention, exactly (upgraded from "
               "the earlier 7-digit numeric match)")
    path = wb.save()
    ok = (str(c1_minus_c2) == "0") \
        and abs(float(sp.N(n_pipe - n_c, 15)) - 1.9554e-4) < 1e-6 \
        and (str(c_minus_w) == "0") \
        and d_minus_c1 != 0 and d_minus_c2 != 0
    print(f"witness: {path}")
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
