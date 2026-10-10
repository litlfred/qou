#!/usr/bin/env python3
"""full_tower_trace_coherence_probe.py — which partition weights define ONE trace
on the whole Hecke tower H_1 ⊂ H_2 ⊂ … ?

EXPLORATORY. NOT WIRED. Owner instruction 2026-10-10 (bean `qou-slz5`, "derive
the weight"): under D7 the mass/binding channel lives on the FULL tower, and no
full-tower weight is defined. Rather than rank candidate weights by how well
they reproduce binding energies (forbidden: selection against the target), this
probe applies the structural conditions a full-tower weight must satisfy and
reports which candidates survive.

SETTING. A trace on H_n(q) is tr = Σ_λ w_λ χ^λ, measure mu_λ = w_λ f^λ. Using
balanced generators σ_i, eigenvalues q and −1/q, and generic q (the Bratteli
diagram of the tower is the Young graph), the restriction tr_{n+1}|_{H_n} = tr_n
holds iff the weights are HARMONIC on the Young graph:

    w_λ = Σ_{μ = λ + □} w_μ                       (branching coherence)

A weight that fails this does not define a trace on the tower: a nucleus at
n = 3A and its sub-clusters at smaller n would be weighed by unrelated
functionals.

WHAT IS CHECKED (all exact in ℚ(q, y) with sympy unless stated)
  1. classical Plancherel (f^λ)²/n!                        — coherent (control)
  2. Molien  f^λ q^{−κ_λ} dim_q(λ)/[n]_q!                   — coherent
  3. quantum Plancherel dim_q(λ)²/Σ dim_q²                 — NOT coherent
  4. the Ocneanu/Markov family at imaginary rank x = i·y:
        w_λ(y) = Π_cells (y q^c + q^{−c}/y) / ((y + 1/y)^n Π_cells [h]_q)
     coherent, every weight strictly positive (faithful on ALL λ), Markov
     parameter z(y) = (q − q^{−1}) y²/(y² + 1) ∈ (0, q − q^{−1});
  5. its endpoints: y → 0 is exactly Molien (q^{−κ}); y → ∞ is the mirror
     Molien (q^{+κ}) — the two canonical (symmetrising) traces;
  6. the real-rank Markov traces (x real, N not an integer) have a NEGATIVE
     weight on some column/row — so for real q > 1 the positive Markov traces
     that are faithful on every partition are exactly z ∈ [0, q − q^{−1}];
  7. convention D, z_D = q³/(q²+1), lies OUTSIDE that interval at q0 (it is the
     N = 2 truncation, faithful only on ≤ 2-row shapes) — consistent with D7
     scoping D to the decay channel.

WHAT IS NOT CLAIMED. Coherence + positivity + faithfulness + Markov property do
not single out one point: they leave the interval z ∈ [0, q − q^{−1}]. Which
point (an endpoint = a canonical trace, or the self-dual midpoint y = 1,
z = (q − q^{−1})/2, fixed by the automorphism σ ↦ −σ^{−1}, λ ↦ λ') is a further
choice this probe does not make. Coherence for n ≤ 6 (Plancherel/Molien) and
n ≤ 5 (y-family) is checked, not proved for all n; the y-family's coherence for
all n is the standard Ocneanu theory, and Molien's is restriction of the
canonical trace τ(σ_w) = δ_{w,1}.

Precision: exact rational functions; the only numerics are signs and values at
the proton q0 (mpmath, 70 dps). No float64.
Output: full-tower-trace-coherence-probe.witness.json (this directory).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from sympy.utilities.iterables import partitions as _sp_partitions  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

q = sp.symbols("q", positive=True)
y = sp.symbols("y", positive=True)
N_MAX_PLANCHEREL = 6
N_MAX_FAMILY = 5


def parts(n):
    return [tuple(sorted([k for k, v in p.items() for _ in range(v)], reverse=True))
            for p in _sp_partitions(n)]


def cells(lam):
    return [(i, j) for i in range(len(lam)) for j in range(lam[i])]


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    return [lam[i] - j - 1 + conj[j] - i for (i, j) in cells(lam)]


def contents(lam):
    return [j - i for (i, j) in cells(lam)]


def qi(m):
    return (q**m - q**-m) / (q - q**-1)          # balanced q-integer


def qf(n):
    return sp.prod([qi(m) for m in range(1, n + 1)])


def f_lam(lam):
    return sp.factorial(sum(lam)) / sp.prod(hooks(lam))


def dim_q(lam):
    return qf(sum(lam)) / sp.prod([qi(h) for h in hooks(lam)])


def up(lam):
    out, ext = [], list(lam) + [0]
    for i in range(len(ext)):
        if i == 0 or ext[i] < ext[i - 1]:
            m = ext[:]
            m[i] += 1
            out.append(tuple(x for x in m if x))
    return out


def weight(family, lam):
    n = sum(lam)
    if family == "classical_plancherel":
        mu = f_lam(lam) ** 2 / sp.factorial(n)
    elif family == "molien":
        mu = f_lam(lam) * q ** (-sum(contents(lam))) * dim_q(lam) / qf(n)
    elif family == "mirror_molien":
        mu = f_lam(lam) * q ** (sum(contents(lam))) * dim_q(lam) / qf(n)
    elif family == "quantum_plancherel":
        mu = dim_q(lam) ** 2 / sum(dim_q(m) ** 2 for m in parts(n))
    elif family == "ocneanu_imaginary_rank":
        return (sp.prod([y * q**c + q**-c / y for c in contents(lam)])
                / ((y + 1 / y) ** n * sp.prod([qi(h) for h in hooks(lam)])))
    else:
        raise ValueError(family)
    return mu / f_lam(lam)


def coherence_defects(family, n_max):
    out = []
    for n in range(1, n_max + 1):
        for lam in parts(n):
            d = sp.simplify(weight(family, lam) - sum(weight(family, m) for m in up(lam)))
            if d != 0:
                out.append((lam, d))
    return out


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    Q = mp.mpf(Q_50_DIGIT_STR)
    checks = []

    def chk(name, ok, detail=""):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

    coh = {}
    for fam in ("classical_plancherel", "molien", "mirror_molien", "quantum_plancherel"):
        coh[fam] = coherence_defects(fam, N_MAX_PLANCHEREL)
    chk("classical Plancherel is branching-coherent (n<=6)", not coh["classical_plancherel"])
    chk("Molien f q^-kappa dim_q/[n]! is branching-coherent (n<=6)", not coh["molien"])
    chk("mirror Molien f q^+kappa dim_q/[n]! is branching-coherent (n<=6)", not coh["mirror_molien"])
    qp = coh["quantum_plancherel"]
    first_lam, first_def = (qp[0] if qp else (None, None))
    first_val = (mp.mpf(str(sp.N(first_def.subs(q, sp.Rational(Q_50_DIGIT_STR)), 70)))
                 if qp else None)
    chk("quantum Plancherel dim_q^2/D^2 is NOT branching-coherent",
        bool(qp), f"{len(qp)} failing (lambda) for n<={N_MAX_PLANCHEREL}; first at "
        f"{first_lam}, defect at q0 = {mp.nstr(first_val, 12) if qp else '-'}")
    small_ok = all(sum(l) >= 3 for l, _ in qp)
    chk("quantum Plancherel coherence holds at n=1,2 and first fails at n=3",
        small_ok and qp and sum(first_lam) == 3)

    fam_def = coherence_defects("ocneanu_imaginary_rank", N_MAX_FAMILY)
    chk("imaginary-rank Ocneanu family is branching-coherent (n<=5)", not fam_def)
    z = sp.factor(sp.simplify(weight("ocneanu_imaginary_rank", (2,)) * q
                              - weight("ocneanu_imaginary_rank", (1, 1)) / q))
    z_expected = (q - 1 / q) * y**2 / (y**2 + 1)
    chk("Markov parameter z(y) = (q - 1/q) y^2/(y^2+1)", sp.simplify(z - z_expected) == 0,
        str(z))
    ends_ok = all(
        sp.simplify(sp.limit(weight("ocneanu_imaginary_rank", lam), y, 0)
                    - weight("molien", lam)) == 0
        and sp.simplify(sp.limit(weight("ocneanu_imaginary_rank", lam), y, sp.oo)
                        - weight("mirror_molien", lam)) == 0
        for lam in parts(4))
    chk("y->0 is Molien and y->oo is mirror Molien (n=4, all lambda)", ends_ok)

    # 6. real-rank Markov traces: a negative weight appears (sample x = 3 at q0,
    #    not an integer power of q, so no truncation zero).
    x = mp.mpf(3)

    def w_real(lam):
        num = mp.fprod([x * Q**c - Q**(-c) / x for c in contents(lam)])
        den = (x - 1 / x) ** sum(lam) * mp.fprod(
            [(Q**h - Q**(-h)) / (Q - 1 / Q) for h in hooks(lam)])
        return num / den
    neg = None
    for m in range(1, 40):
        col = tuple([1] * m)
        if w_real(col) < 0:
            neg = (m, w_real(col))
            break
    chk("real-rank Markov trace (x=3) has a negative weight on a column",
        neg is not None, f"first at column length {neg[0]}, w = {mp.nstr(neg[1], 8)}"
        if neg else "")

    z_hi = Q - 1 / Q
    z_D = Q**3 / (Q**2 + 1)
    chk("convention D z_D lies outside the faithful-positive interval [0, q-1/q] at q0",
        z_D > z_hi, f"z_D = {mp.nstr(z_D, 15)}, q-1/q = {mp.nstr(z_hi, 15)}")

    w = WitnessBuilder("full-tower-trace-coherence-probe", engine="python",
                       start_time=t0)
    w.set_description(
        "Structural conditions on a full-tower mass weight (bean qou-slz5): "
        "branching coherence (one trace on the whole Hecke tower), positivity, "
        "faithfulness on every partition, Markov property. Quantum Plancherel "
        "dim_q^2/D^2 fails coherence (first at lambda=(3)); Molien and its mirror "
        "are coherent and are the endpoints of the faithful positive Markov "
        "interval z in [0, q-1/q]; convention D lies outside it. EXPLORATORY, "
        "not wired; no point of the interval is selected.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("q0", Q_50_DIGIT_STR)
    w.add_data("generators", "balanced sigma_i, eigenvalues q and -1/q")
    w.add_data("coherence_condition", "w_lambda = sum_{mu = lambda + box} w_mu")
    w.add_data("n_max_checked", {"plancherel_molien": N_MAX_PLANCHEREL,
                                 "ocneanu_family": N_MAX_FAMILY})
    w.add_data("quantum_plancherel_failures",
               [{"lambda": list(l), "defect": str(sp.factor(d))} for l, d in qp])
    w.add_data("quantum_plancherel_first_defect_at_q0",
               fmt(first_val) if qp else None)
    w.add_data("markov_parameter_of_family", str(z))
    w.add_data("faithful_positive_interval_at_q0",
               {"z_low": "0", "z_high": fmt(z_hi), "z_selfdual_midpoint": fmt(z_hi / 2)})
    w.add_data("z_D_at_q0", fmt(z_D))
    w.add_data("adoption", "none — no point of the interval is selected")
    w.add_data("checks", checks)
    for c in checks:
        w.add_assertion(name=c["name"], computed="1" if c["passed"] else "0",
                        expected="1", tolerance="0", source=c["detail"] or None)
    out = w.save()
    print(f"Witness: {out}  ({time.monotonic() - t0:.1f}s)")
    return 0 if all(c["passed"] for c in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
