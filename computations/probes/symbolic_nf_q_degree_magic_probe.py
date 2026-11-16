#!/usr/bin/env python3
"""Symbolic NF q-degree: does the SURVIVING GRADING separate magic from non-magic?

WHY THIS EXISTS. The tower probes on this arc (`tower_walk_h3a_magic_probe`,
`tower_walk_magic_replication_probe`, `gamma_chain_tower_magic_probe`) all
evaluate at the single point q = q_0, and a scope retraction on 2026-08-30
established that this collapses the object that carries the many-body
structure. The corpus is explicit:

  * `trace-locality-gs-reconciliation` -- the GS algorithm "digests global
    entanglement into local coefficients"; the Markov trace then factorises
    locally over the normal form. DIGESTED, not destroyed.
  * `bond-order-eq-jet-degree-proof` -- adding a nucleon "rais[es] the
    Groebner-Shirshov normal-form length by a fixed increment", placing the
    n-nucleon cluster sub-word at JET VERTICAL DEGREE n.
  * `prop:gb-spectral-sequence` (E_2 collapse) + `prop:jet-prefix-gb-filtration`
    -- the associated graded gr_n IS the n-nucleon cluster contribution.

So the NF is not six numbers, it is six LAURENT POLYNOMIALS IN q, and the
q-degree is the surviving grading. This probe measures that grading directly.

THE SHORTCUT, and it is the point. `hecke_core_symbolic.build_atom_nf_sym`
carries raw sympy expression trees: one A=1 coefficient already has an srepr
of 22,358 characters, and A=2 took 862 s. That cost is expression swell, not
mathematics. Under convention D every coefficient stays in Q[q^{+-1}] (the
module's own docstring: "Under D, z is rational in q, so the Q[q^{+-1/2}]
half-power branch that C [required] is gone"), and inspecting the atom path,
EVERY multiplier is one of `1`, `0`, `-h`, `-h/2` with `h = q - 1/q`. So no
general polynomial multiplication occurs anywhere: multiplying by `h` is a
shift-and-subtract on exponents, and the rest is scaling by a rational.

Representing each coefficient as `dict[exponent -> Fraction]` therefore makes
the whole walk exact, linear in the number of terms, and gives the q-degree
for free. This is the "symbolic or other shortcut" the 686 GB figure was
missing one level up: nature does not carry a 22 KB unsimplified tree either.

CORRECTNESS GATE. `--verify` checks this implementation against the corpus's
own `hecke_core_symbolic.build_atom_nf_sym` by expanding both to canonical
Laurent form and comparing coefficient-by-coefficient, exactly (Fractions, no
float anywhere). It runs at A=1 (p and n) and A=2, and the probe REFUSES to
report a measurement if any coefficient disagrees.

RESULT: the grading does NOT separate magic from non-magic, at any level the
scan reaches -- A = 2..20, which covers Z = 2, 8 and 20, three magic numbers
no numeric probe on this arc could test. All four observables report
`interleaved` at every level; `ANY graded observable replicating across
levels: False`; and `degree_span` separates magic from non-magic cleanly at
**0 of 19** levels.

So the retraction that motivated this probe is confirmed in both directions.
The order structure IS real -- it survives the Groebner-Shirshov reduction,
and it distinguishes the proton from the neutron (kernel-checked in
`QOU.BraidKnot.LaurentWalk.proton_ne_neutron_degrees`, a distinction the
numeric normal form at q_0 cannot express). It just carries no magic signal.

THE ARTIFACT THAT WOULD HAVE FAKED A POSITIVE IS PARITY -- the sixth time on
this arc. I first hypothesised the degree span was monotone in Z at fixed A;
**that was wrong**, only 6 of 19 levels are monotone. What is actually there
is an even/odd zigzag concentrated at low Z. At A = 20:

    Z    4    3    2    1    0
    span 562  596  458  560  420
              ^         ^          odd Z sit ABOVE their even neighbours

Local minima favour even Z on **13 of 17** levels. Every magic number is even,
so a "magic Z has low degree span" test would have been measuring parity, not
shell structure -- exactly the artifact that killed the delta^2-Phi result,
the 4He NF collapse, and the A=3 participation split. The per-level control
below reports `interleaved` and refuses it, which is what the control is for.

WHAT IS MEASURED, per configuration (Z, N):
  * `max_degree` / `min_degree` -- the q-degree span of the NF
  * `n_terms` -- total monomials across the six coefficients
  * `degree_profile` -- per-coefficient (min, max) degree
  * `support` -- the set of exponents actually occupied
These are the graded observables. NO evaluation at q_0 occurs anywhere in
this probe, by design.

PRECISION: exact throughout. Coefficients are `fractions.Fraction`; there is
no float, no mpmath, and no evaluation at any numerical q. The NO-FLOAT64
discipline is satisfied trivially rather than by care.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from fractions import Fraction

# Repo-relative, not '/home/user/qou/...': the absolute path only resolved on
# the machine that wrote it, so `verify()` could not import hecke_core_symbolic
# anywhere else and the producer exited 1 before computing anything.
_COMP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [_COMP, os.path.join(_COMP, 'substrate')]

MAGIC = {2, 8, 20, 28, 50, 82, 126}

# ── Laurent polynomials in q over Q, as {exponent: Fraction} ──────────────

Lau = dict  # dict[int, Fraction]


def lau_zero() -> Lau:
    return {}


def lau_one() -> Lau:
    return {0: Fraction(1)}


def lau_add(a: Lau, b: Lau) -> Lau:
    if not a:
        return dict(b)
    if not b:
        return dict(a)
    r = dict(a)
    for e, c in b.items():
        v = r.get(e, Fraction(0)) + c
        if v:
            r[e] = v
        elif e in r:
            del r[e]
    return r


def lau_scale(a: Lau, k: Fraction) -> Lau:
    if not k:
        return {}
    return {e: c * k for e, c in a.items()}


def lau_mul_h(a: Lau) -> Lau:
    """Multiply by h = q - q^{-1}: a pure shift-and-subtract, no convolution."""
    r: Lau = {}
    for e, c in a.items():
        for shift, sgn in ((1, 1), (-1, -1)):
            k = e + shift
            v = r.get(k, Fraction(0)) + sgn * c
            if v:
                r[k] = v
            elif k in r:
                del r[k]
    return r


# ── The six-component NF step, mirroring hecke_core_symbolic.hm_sym ───────
#
# Multipliers in the atom path are only `1`, `0`, `-h`, `-h/2`, so `d` is
# encoded as (rational_factor, h_power) with h_power in {0, 1}: `0` is
# (0, 0), `-h` is (-1, 1), `-h/2` is (-1/2, 1).  `c` is always 1.

_TABLES = {
    0: [(0, [(1, 'c'), (0, 'd')]),
        (1, [(1, 'ch'), (0, 'c'), (1, 'd')]),
        (2, [(3, 'c'), (2, 'd')]),
        (3, [(3, 'ch'), (2, 'c'), (3, 'd')]),
        (4, [(5, 'c'), (4, 'd')]),
        (5, [(5, 'ch'), (4, 'c'), (5, 'd')])],
    1: [(0, [(2, 'c'), (0, 'd')]),
        (1, [(4, 'c'), (1, 'd')]),
        (2, [(2, 'ch'), (0, 'c'), (2, 'd')]),
        (3, [(5, 'c'), (3, 'd')]),
        (4, [(4, 'ch'), (1, 'c'), (4, 'd')]),
        (5, [(5, 'ch'), (3, 'c'), (5, 'd')])],
}


def hm_lau(nf: list[Lau], d_rat: Fraction, d_hpow: int, gen: int) -> list[Lau]:
    """NF <- NF * (sigma_gen + d), with c = 1 and d = d_rat * h^d_hpow."""
    r: list[Lau] = [{} for _ in range(6)]
    for si, tgts in _TABLES[gen]:
        src = nf[si]
        if not src:
            continue
        for ti, kind in tgts:
            if kind == 'c':
                term = src
            elif kind == 'ch':
                term = lau_mul_h(src)
            else:  # 'd'
                if not d_rat:
                    continue
                term = lau_mul_h(src) if d_hpow else src
                term = lau_scale(term, d_rat)
            r[ti] = lau_add(r[ti], term)
    return r


ZERO_D = (Fraction(0), 0)
MINUS_H = (Fraction(-1), 1)
MINUS_H_HALF = (Fraction(-1, 2), 1)


def ground_state_ordering(Z: int, N: int) -> list[str]:
    o, pc, nc = [], 0, 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            o.append("p"); pc += 1
        else:
            o.append("n"); nc += 1
    return o


def build_atom_nf_lau(Z: int, N: int) -> list[Lau]:
    """Exact Laurent mirror of hecke_core_symbolic.build_atom_nf_sym."""
    A = Z + N
    nf: list[Lau] = [lau_one(), {}, {}, {}, {}, {}]
    if A == 0:
        return nf
    ordering = ground_state_ordering(Z, N)
    for k in range(A):
        if ordering[k] == "p":
            for _ in range(3):
                nf = hm_lau(nf, *ZERO_D, 0)
                nf = hm_lau(nf, *MINUS_H, 1)
            nf = hm_lau(nf, *ZERO_D, 0)
            nf = hm_lau(nf, *MINUS_H_HALF, 0)
            nf = hm_lau(nf, *MINUS_H_HALF, 1)
            nf = hm_lau(nf, *ZERO_D, 0)
            nf = hm_lau(nf, *ZERO_D, 0)
        else:
            for _ in range(3):
                nf = hm_lau(nf, *ZERO_D, 0)
                nf = hm_lau(nf, *MINUS_H, 1)
            nf = hm_lau(nf, *MINUS_H_HALF, 0)
            nf = hm_lau(nf, *MINUS_H_HALF, 0)
            nf = hm_lau(nf, *MINUS_H, 1)
            nf = hm_lau(nf, *ZERO_D, 0)
            nf = hm_lau(nf, *ZERO_D, 0)
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                nf = hm_lau(nf, *ZERO_D, 0)
            elif ti == "n" and tj == "n":
                nf = hm_lau(nf, *MINUS_H, 0)
            else:
                nf = hm_lau(nf, *MINUS_H_HALF, 0)
    for _ in range(Z):
        nf = hm_lau(nf, *MINUS_H, 1)
    return nf


# ── Observables: the grading, never an evaluation ─────────────────────────

def profile(Z: int, N: int) -> dict:
    t0 = time.time()
    nf = build_atom_nf_lau(Z, N)
    per = []
    support: set[int] = set()
    for c in nf:
        if c:
            per.append([min(c), max(c), len(c)])
            support |= set(c)
        else:
            per.append(None)
    degs = [e for c in nf for e in c]
    return {
        "Z": Z, "N": N, "A": Z + N,
        "magic_Z": Z in MAGIC, "magic_N": N in MAGIC,
        "any_magic": (Z in MAGIC) or (N in MAGIC),
        "doubly_magic": (Z in MAGIC) and (N in MAGIC),
        "max_degree": max(degs), "min_degree": min(degs),
        "degree_span": max(degs) - min(degs),
        "n_terms": sum(len(c) for c in nf),
        "degree_profile": per,
        "support_size": len(support),
        "wall_ms": int(round((time.time() - t0) * 1000)),
    }


def verify() -> bool:
    """Exact agreement with the corpus's own symbolic builder."""
    import sympy as sp
    from hecke_core_symbolic import build_atom_nf_sym
    q = sp.Symbol("q", positive=True)
    ok = True
    for (Z, N) in [(1, 0), (0, 1), (1, 1)]:
        ref = build_atom_nf_sym(Z, N)
        mine = build_atom_nf_lau(Z, N)
        for i, (r, m) in enumerate(zip(ref, mine)):
            # canonical Laurent form of the sympy expression
            e = sp.expand(sp.cancel(sp.together(r)))
            d: dict[int, Fraction] = {}
            for term in sp.Add.make_args(e):
                pcoef, pexp = term.as_coeff_exponent(q)
                d[int(pexp)] = d.get(int(pexp), Fraction(0)) + Fraction(str(sp.nsimplify(pcoef)))
            d = {k: v for k, v in d.items() if v}
            if d != m:
                ok = False
                extra = set(m) - set(d)
                missing = set(d) - set(m)
                print(f"  MISMATCH Z={Z},N={N} coeff[{i}]: "
                      f"{len(d)} ref terms vs {len(m)} mine; "
                      f"extra exps {sorted(extra)[:5]} missing {sorted(missing)[:5]}",
                      flush=True)
            else:
                print(f"  ok  Z={Z},N={N} coeff[{i}]: {len(m)} terms, "
                      f"deg [{min(m) if m else 0}, {max(m) if m else 0}]", flush=True)
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true",
                    help="only run the exact cross-check against build_atom_nf_sym")
    ap.add_argument("--max-A", type=int, default=6)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    print("=== EXACT cross-check vs hecke_core_symbolic.build_atom_nf_sym ===",
          flush=True)
    t0 = time.time()
    if not verify():
        print("VERIFY FAILED — refusing to report a measurement.", flush=True)
        return 1
    print(f"  all coefficients agree exactly  [{time.time() - t0:.1f}s]\n", flush=True)
    if a.verify:
        return 0

    rows = []
    for A in range(1, a.max_A + 1):
        print(f"=== A={A} ===", flush=True)
        for Z in range(A, -1, -1):
            r = profile(Z, A - Z)
            tag = ("DOUBLY MAGIC" if r["doubly_magic"]
                   else "MAGIC" if r["any_magic"] else "neither")
            r["tag"] = tag
            rows.append(r)
            print(f"  Z={Z},N={A-Z:<2} {tag:<13} "
                  f"deg [{r['min_degree']:>4}, {r['max_degree']:>4}] "
                  f"span {r['degree_span']:>4}  terms {r['n_terms']:>5}  "
                  f"support {r['support_size']:>4}  [{r['wall_ms']}ms]",
                  flush=True)

    print("\n=== magic vs neither, per level ===", flush=True)
    verdicts = {}
    for A in range(1, a.max_A + 1):
        lv = [r for r in rows if r["A"] == A]
        mg = [r for r in lv if r["any_magic"]]
        nm = [r for r in lv if not r["any_magic"]]
        if not mg or not nm:
            print(f"  A={A}: not comparable ({len(mg)} magic / {len(nm)} neither)",
                  flush=True)
            continue
        v = {"n_magic": len(mg), "n_non_magic": len(nm)}
        for key in ("max_degree", "degree_span", "n_terms", "support_size"):
            mv = [r[key] for r in mg]
            nv = [r[key] for r in nm]
            v[key] = {
                "magic": mv, "non_magic": nv,
                "direction": ("magic_above" if min(mv) > max(nv)
                              else "magic_below" if max(mv) < min(nv)
                              else "interleaved"),
            }
        verdicts[A] = v
        print(f"  A={A}: " + "  ".join(
            f"{k}={v[k]['direction']}"
            for k in ("max_degree", "degree_span", "n_terms", "support_size")),
            flush=True)

    print("\n=== CROSS-LEVEL REPLICATION ===", flush=True)
    replication = {}
    for key in ("max_degree", "degree_span", "n_terms", "support_size"):
        dirs = {A: v[key]["direction"] for A, v in verdicts.items()}
        vals = set(dirs.values())
        replication[key] = {
            "per_level_direction": dirs,
            "consistent": len(vals) == 1 and "interleaved" not in vals,
            "contradictory": ("magic_above" in vals) and ("magic_below" in vals),
        }
        per = "  ".join(f"A={A}:{d}" for A, d in dirs.items())
        print(f"  {key:<14} {per}", flush=True)
        print(f"  {'':14} consistent={replication[key]['consistent']}  "
              f"CONTRADICTORY={replication[key]['contradictory']}", flush=True)

    any_rep = any(r["consistent"] for r in replication.values())
    print(f"\n  ANY graded observable replicating across levels: {any_rep}",
          flush=True)

    payload = {
        "probe": "symbolic_nf_q_degree_magic",
        "question": "does the q-degree grading of the symbolic NF -- the "
                    "structure that survives the Groebner-Shirshov reduction "
                    "and that evaluation at q_0 destroys -- separate magic "
                    "from non-magic nucleon configurations?",
        "control": "exhaustive at each level: every Z in 0..A",
        "arithmetic": "exact over Q (fractions.Fraction); no float, no mpmath, "
                      "no evaluation at any numerical q",
        "configurations": rows,
        "per_level_verdict": {str(k): v for k, v in verdicts.items()},
        "cross_level_replication": replication,
        "any_observable_replicates": any_rep,
    }
    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder.wrap_legacy(
            "symbolic-nf-q-degree-magic", payload,
            script_path=__file__, engine="python+fractions",
            output_dir=os.path.dirname(os.path.abspath(__file__)),
            start_time=t0,
        )
        wb.add_assertion("exact_agreement_with_build_atom_nf_sym",
                         computed="True", expected="True")
        for A, v in verdicts.items():
            wb.add_assertion(f"both_groups_non_empty_at_A{A}",
                             computed=str(v["n_magic"] > 0 and v["n_non_magic"] > 0),
                             expected="True")
        out = wb.save(extra={
            "auditOnly": True,
            "q0Anchor": "independent",
            "q0AnchorReason": "exact Laurent-polynomial normal forms over Q (fractions.Fraction); "
                              "only q-degrees and term counts are read, nothing is evaluated "
                              "at any numerical q",
        })
        print(f"\nWrote {out}", flush=True)
    except Exception as exc:  # pragma: no cover
        print(f"\n(witness not written: {exc})", flush=True)
        if a.out:
            with open(a.out, "w") as f:
                json.dump(payload, f, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
