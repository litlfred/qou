#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Profile the canonical Markov pipeline to localize where T vs ³He
explodes.

Three stages:
  1. build_atom_symbolic — incremental SymbolicHeckeElement * factor
                           with periodic GS reduction
  2. div.reduce(elem)    — final pre-trace reduction
  3. tr_M_element        — Markov-axiom recursive trace

For each stage we record:
  - elapsed wall time
  - n_terms of the element after the stage
  - peak memory (RSS via psutil if available, else os)

Hypothesis: the build itself is fast for both, but the GS reduction
or the Markov-axiom recursion enters a long rewriting loop on the
(uud, udd, udd) word for ³He.
"""
import json
import os
import sys
import time
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from markov_trace_canonical import tr_M_element
from hecke_symbolic import SymbolicHeckeDivision, q as q_sym
from binding_canonical import build_atom_symbolic


def get_rss_mb():
    """Read RSS memory.  Returns MB.

    Uses psutil when available (cross-platform); falls back to
    /proc/self/status on Linux.  Returns 0.0 if neither works.
    """
    try:
        import psutil
        return psutil.Process().memory_info().rss / 1048576.0
    except Exception:
        try:
            with open('/proc/self/status') as f:
                for line in f:
                    if line.startswith('VmRSS:'):
                        return int(line.split()[1]) / 1024.0
        except Exception:
            pass
    return 0.0


def profile_isotope(label, Z, N, build_timeout=300, reduce_timeout=300,
                     trace_timeout=300):
    """Run the three stages and report per-stage walltime.

    The `*_timeout` parameters are POST-HOC THRESHOLDS: each stage
    runs to completion, and if its walltime exceeds the budget the
    function returns a status='timeout' record instead of continuing
    to subsequent stages.  This is NOT a hard interrupt — a stage
    that hangs will still hang.  For a true hard timeout wrap this
    in `multiprocessing.Process.join(timeout=...)` at the caller.
    """
    print(f"\n══ {label} (Z={Z}, N={N}) ══")
    rec = {"Z": Z, "N": N, "label": label}

    # Stage 1: build
    t0 = time.time()
    try:
        elem = build_atom_symbolic(Z, N, include_inter=True,
                                     m_pp=1, m_pn=1, m_nn=1)
    except Exception as e:
        print(f"  build FAILED: {type(e).__name__}: {e}")
        return {**rec, "stage": "build", "error": str(e)}
    t_build = time.time() - t0
    rss_after_build = get_rss_mb()
    n_terms_after_build = elem.n_terms()
    print(f"  ① build_atom_symbolic:  {t_build:>6.1f}s   "
          f"n_terms = {n_terms_after_build:>5}   RSS = {rss_after_build:.1f} MB")
    rec["build_sec"] = t_build
    rec["n_terms_after_build"] = n_terms_after_build
    rec["rss_after_build_mb"] = rss_after_build
    if t_build > build_timeout:
        return {**rec, "stage": "build", "status": "timeout"}

    # Stage 2: final reduce (already reduced inside build, but do once more)
    t0 = time.time()
    div = SymbolicHeckeDivision()
    try:
        elem_red, _ = div.reduce(elem)
    except Exception as e:
        print(f"  reduce FAILED: {type(e).__name__}: {e}")
        return {**rec, "stage": "reduce", "error": str(e)}
    t_reduce = time.time() - t0
    rss_after_reduce = get_rss_mb()
    n_terms_after_reduce = elem_red.n_terms()
    print(f"  ② final div.reduce:     {t_reduce:>6.1f}s   "
          f"n_terms = {n_terms_after_reduce:>5}   RSS = {rss_after_reduce:.1f} MB")
    rec["reduce_sec"] = t_reduce
    rec["n_terms_after_reduce"] = n_terms_after_reduce
    rec["rss_after_reduce_mb"] = rss_after_reduce
    if t_reduce > reduce_timeout:
        return {**rec, "stage": "reduce", "status": "timeout"}

    # Stage 3: tr_M_element
    A = Z + N
    n_strands = 3 * A
    t0 = time.time()
    try:
        tr_sym = tr_M_element(elem_red, n_strands)
    except Exception as e:
        print(f"  trace FAILED: {type(e).__name__}: {e}")
        return {**rec, "stage": "trace", "error": str(e)}
    t_trace = time.time() - t0
    rss_after_trace = get_rss_mb()
    print(f"  ③ tr_M_element:         {t_trace:>6.1f}s   "
          f"RSS = {rss_after_trace:.1f} MB")
    rec["trace_sec"] = t_trace
    rec["rss_after_trace_mb"] = rss_after_trace

    # Numerical evaluation
    t0 = time.time()
    try:
        tr_q0 = complex(sp.N(tr_sym.subs(q_sym, Q0)))
        if abs(tr_q0.imag) < 1e-9:
            tr_q0 = tr_q0.real
    except Exception as e:
        print(f"  eval FAILED: {type(e).__name__}: {e}")
        return {**rec, "stage": "eval", "error": str(e)}
    t_eval = time.time() - t0
    print(f"  ④ symbolic→q_0 eval:    {t_eval:>6.1f}s   "
          f"|tr_M| = {abs(tr_q0):.6f}")
    rec["eval_sec"] = t_eval
    rec["abs_tr_M_q0"] = float(abs(tr_q0))
    rec["status"] = "completed"
    return rec


if __name__ == "__main__":
    print("CANONICAL MARKOV PROFILING — T vs ³He stage breakdown")
    print("=" * 80)
    print(f"q_0 = {float(Q0):.6f}")

    cases = [
        ("T  ", 1, 2),
        ("³He", 2, 1),
    ]

    results = []
    for label, Z, N in cases:
        rec = profile_isotope(label, Z, N,
                                build_timeout=600, reduce_timeout=600,
                                trace_timeout=600)
        results.append(rec)

    # Summary
    print("\n══ SUMMARY ══")
    print(f"{'isotope':>8} {'build':>8} {'reduce':>8} {'trace':>8} "
          f"{'eval':>8} {'TOTAL':>8} {'n_terms':>10}")
    for r in results:
        if r.get("status") == "completed":
            tot = (r["build_sec"] + r["reduce_sec"]
                   + r["trace_sec"] + r["eval_sec"])
            print(f"{r['label']:>8} {r['build_sec']:>8.1f} "
                  f"{r['reduce_sec']:>8.1f} {r['trace_sec']:>8.1f} "
                  f"{r['eval_sec']:>8.1f} {tot:>8.1f} "
                  f"{r['n_terms_after_reduce']:>10}")
        else:
            print(f"{r['label']:>8}  STOPPED at stage {r.get('stage', '?')}")

    out = Path(__file__).parent / "canonical-isospin-profile.witness.json"
    out.write_text(json.dumps({
        "computation": "canonical-isospin-profile",
        "description": ("Stage-by-stage profile of the canonical Markov "
                         "pipeline on T vs ³He, identifying which stage "
                         "explodes."),
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
