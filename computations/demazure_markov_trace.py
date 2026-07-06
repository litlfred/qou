#!/usr/bin/env python3
"""Demazure-fiber Markov-trace evaluator (AGENTS.md §7b shortcut #3).

Replaces the manual Hecke-energy LP functional in
`sdp-primality-verifier-spec.md` by Kashiwara-graph weight-lattice
projection: for each Weyl element `w ∈ S_n`, the Demazure character
`D_w(λ)` cuts out a sub-crystal of `V_λ` (an "incomplete topological
state").  At the longest element `w_0`, `D_{w_0}(λ) = s_λ` recovers
the full Schur element; at intermediate `w`, the ratio
`D_w(λ) / D_{w_0}(λ)` is a structural resonance width — the
fraction of the Wedderburn block populated under the Demazure
filtration.

This script:

1. Implements the Demazure operator π_i recursively on Laurent
   polynomials in `x_1, …, x_n` (sympy).
2. Computes `D_w(λ)` for one canonical reduced word `w` per
   permutation in `S_n` (chosen by bubble-sort, n = 2, 3) and
   every partition `λ ⊢ n`.  Different reduced words for the same
   permutation give equal Demazure characters (the Demazure
   operators satisfy the braid relations on reduced words), so a
   single reduced word per permutation is sufficient.
3. At `w = w_0`, verifies `D_{w_0}(λ) = s_λ(x_1, …, x_n)` against
   sympy's `schur_polynomial`.
4. Emits the **Demazure-fiber Markov-trace functional**

       T^{Dem}(λ; w) := y_λ · D_w(λ) / D_{w_0}(λ),

   for every (λ, w), at the principal specialisation
   `x_i ↦ q^{i-1}` and the Wenzl-bridge `y_λ` from
   `prop:macdonald-hook-telescope`.  At `w = w_0` this reduces to
   `y_λ` and reproduces the Plancherel weights w_λ(q) used in the
   LP cost vector; at shorter `w` it gives a structural Demazure
   resonance width.

5. Saves a witness JSON consumable by future LP/SDP refactorings
   that wish to replace the manual Hecke-energy cost by the
   Demazure-fiber projection.

References
----------
- Kashiwara, "The crystal base and Littelmann's refined Demazure
  character formula", Duke Math. J. 71 (1993).
- Demazure, "Une nouvelle formule des caractères", Bull. Sci.
  Math. 98 (1974).
- Lecouvey, "Combinatorics of crystal graphs and Kostka–Foulkes
  polynomials" (2007).
- prop:macdonald-hook-telescope — y_λ closed form used here.
"""

from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_lengths_with_cells as hook_lengths  # noqa: E402


# ──────────────────────────────────────────────────────────────────
#  Demazure operator on sympy polynomials in x_1, …, x_n
# ──────────────────────────────────────────────────────────────────


def demazure_operator(f, x, i):
    """π_i (f) = (x_i · f − x_{i+1} · s_i f) / (x_i − x_{i+1}).

    `x` is the list of variables (1-indexed accessed as x[i-1]),
    `i ∈ {1, …, n−1}` is the simple-reflection index.
    """
    xi, xip1 = x[i - 1], x[i]
    si_f = f.subs({xi: xip1, xip1: xi}, simultaneous=True)
    num = xi * f - xip1 * si_f
    return sp.cancel(num / (xi - xip1))


def demazure_character(weight, word, x):
    """D_w (x^weight) = π_{i_1} … π_{i_k} (x^weight)."""
    n = len(weight)
    f = sp.S(1)
    for j, exp in enumerate(weight):
        if exp:
            f *= x[j] ** exp
    for i in word:
        f = demazure_operator(f, x, i)
    return sp.expand(f)


# ──────────────────────────────────────────────────────────────────
#  Reduced words and the longest element of S_n
# ──────────────────────────────────────────────────────────────────


def perm_to_reduced_word(perm):
    """Bubble-sort one reduced word for `perm` (a tuple representing
    permutation π such that perm[i] = π(i+1))."""
    p = list(perm)
    word = []
    while True:
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i + 1)
                break
        else:
            return word


def all_permutations(n):
    if n == 0:
        return [()]
    out = []
    for sub in all_permutations(n - 1):
        for k in range(n):
            out.append(sub[:k] + (n,) + sub[k:])
    return out


def w0_word(n):
    return perm_to_reduced_word(tuple(range(n, 0, -1)))


# ──────────────────────────────────────────────────────────────────
#  Partition / Schur principal specialisation (Macdonald hook)
# ──────────────────────────────────────────────────────────────────


def n_lambda(p):
    return sum(i * p[i] for i in range(len(p)))


def f_lambda(p):
    n = sum(p)
    nfact = 1
    for k in range(2, n + 1):
        nfact *= k
    hp = 1
    for (_, _, h) in hook_lengths(p):
        hp *= h
    return nfact // hp


def partitions_of(n):
    if n == 0:
        return [()]
    out = []

    def rec(rem, mx, pre):
        if rem == 0:
            out.append(tuple(pre))
            return
        for k in range(min(rem, mx), 0, -1):
            rec(rem - k, k, pre + [k])

    rec(n, n, [])
    return out


def y_lambda_telescope(p, q_sym):
    """y_λ via the Macdonald hook-content telescope (closed form)."""
    Q = q_sym ** 2
    z = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))
    X = q_sym * z / (1 - Q + q_sym * z)
    cells = hook_lengths(p)
    n = sum(p)
    num = Q ** n_lambda(p) * (1 - Q) ** n
    den = (1 - X) ** n
    for (i, j, h) in cells:
        c = j - i
        num *= (1 - X * Q ** c)
        den *= (1 - Q ** h)
    return num / den


# ──────────────────────────────────────────────────────────────────
#  Demazure-fiber Markov-trace functional
# ──────────────────────────────────────────────────────────────────


def lambda_padded(p, n_strands):
    """Pad partition `p` with zeros to length `n_strands`."""
    return list(p) + [0] * (n_strands - len(p))


def schur_via_w0(p, x, n_strands):
    weight = lambda_padded(p, n_strands)
    return demazure_character(weight, w0_word(n_strands), x)


def principal_specialise(expr, x, q_sym):
    """Substitute x_i ↦ q^{i-1}."""
    return sp.expand(
        expr.subs({xi: q_sym ** i for i, xi in enumerate(x)})
    )


def collect_demazure_table(n_strands: int):
    """Compute D_w(λ) for every (λ, w) on S_{n_strands}."""
    x = sp.symbols(f"x1:{n_strands + 1}")
    q = sp.symbols("q", positive=True)

    perms = all_permutations(n_strands)
    parts = partitions_of(n_strands)
    w0 = w0_word(n_strands)

    table = {}
    for p in parts:
        weight = lambda_padded(p, n_strands)
        per_word = {}
        D_w0 = demazure_character(weight, w0, x)
        D_w0_ps = principal_specialise(D_w0, x, q)
        per_word["w0"] = {
            "word": list(w0),
            "D_w_polynomial": sp.sstr(D_w0),
            "D_w_principal": sp.sstr(D_w0_ps),
        }

        # All permutations: keyed by their reduced word as a tuple-string.
        for perm in perms:
            word = perm_to_reduced_word(perm)
            D_w = demazure_character(weight, word, x)
            D_w_ps = principal_specialise(D_w, x, q)
            if D_w0_ps.equals(0):
                raise ValueError(
                    f"D_{{w0}} vanishes at principal specialisation for "
                    f"partition {p}; ratio is undefined."
                )
            ratio = sp.cancel(D_w_ps / D_w0_ps)
            key = ",".join(str(c) for c in perm)
            per_word[key] = {
                "permutation": list(perm),
                "word": word,
                "length": len(word),
                "D_w_principal": sp.sstr(D_w_ps),
                "D_w_over_D_w0": sp.sstr(ratio),
            }

        # Markov-trace projection: T^Dem(λ; w) = y_λ · D_w / D_{w_0}
        y_lam = y_lambda_telescope(p, q)
        per_word_trace = {}
        for key, rec in per_word.items():
            if key == "w0":
                T = y_lam
            else:
                ratio_expr = sp.sympify(rec["D_w_over_D_w0"])
                T = sp.cancel(y_lam * ratio_expr)
            per_word_trace[key] = sp.sstr(T)

        table[str(list(p))] = {
            "partition": list(p),
            "f_lambda": f_lambda(p),
            "demazure": per_word,
            "demazure_markov_trace": per_word_trace,
        }
    return table


def verify_w0_equals_schur(n_strands: int):
    """At w = w_0, the Demazure character equals the Schur polynomial.

    We verify this via principal specialisation: the Demazure character
    `D_{w_0}(λ)` evaluated at `x_i = q^{i-1}` must equal the
    Macdonald-hook Schur principal specialisation.
    """
    x = sp.symbols(f"x1:{n_strands + 1}")
    q = sp.symbols("q", positive=True)
    Q = q
    X = sp.symbols("X")  # placeholder kept symbolic to compare structure

    results = {}
    for p in partitions_of(n_strands):
        D_w0 = schur_via_w0(p, x, n_strands)
        D_w0_ps = principal_specialise(D_w0, x, q)

        # Schur principal specialisation: s_λ(1, q, …, q^{n-1})
        # via Macdonald hook formula = q^{n(λ)} · ∏ (1-q^{n+c})/(1-q^h)
        cells = hook_lengths(p)
        target = q ** n_lambda(p)
        for (i, j, h) in cells:
            c = j - i
            target *= (1 - q ** (n_strands + c)) / (1 - q ** h)
        target = sp.cancel(sp.together(target))

        diff = sp.cancel(D_w0_ps - target)
        results[str(list(p))] = {
            "matches_schur_principal": (diff == 0),
            "diff_simplified": sp.sstr(diff),
        }
    return results


def main():
    builder = (
        WitnessBuilder("demazure-markov-trace", engine="sympy")
        .set_description(
            "Demazure-fiber Markov-trace evaluator: replaces the manual "
            "Hecke-energy LP cost vector by Kashiwara weight-lattice "
            "projection.  For every Weyl element w ∈ S_n and partition "
            "λ ⊢ n, computes the Demazure character D_w(λ), the "
            "principal-specialisation ratio D_w/D_{w_0}, and the "
            "Demazure-fiber Markov-trace functional T^Dem(λ; w) = "
            "y_λ · D_w(λ)/D_{w_0}(λ).  At w = w_0 reduces to the "
            "standard Markov trace; at shorter w gives the structural "
            "Demazure resonance width."
        )
        .set_content_block("prop:demazure-fiber-markov-trace")
    )

    # Scope: defaults to {2, 3} for sandbox (n=4 is 5·24=120 chars,
    # exceeds local 50 s wall-clock); CI sets QOU_EXTEND_SCOPE=1
    # to push to {2, 3, 4} (4 + 18 + 120 = 142 non-trivial chars).
    import os as _os
    n_max = 4 if _os.environ.get("QOU_EXTEND_SCOPE") == "1" else 3
    n_range = range(2, n_max + 1)

    # Expected non-trivial char counts: p(n)·n!
    pn_factorial = {2: 2 * 2, 3: 3 * 6, 4: 5 * 24}
    expected_nontrivial = sum(pn_factorial[n] for n in n_range)
    expected_partitions = sum(
        {2: 2, 3: 3, 4: 5}[n] for n in n_range
    )

    print(f"Step 1: verify D_{{w_0}}(λ) = s_λ at principal specialisation "
          f"(n = {list(n_range)})...")
    consistency = {}
    for n in n_range:
        rec = verify_w0_equals_schur(n)
        all_ok = all(r["matches_schur_principal"] for r in rec.values())
        flag = "OK" if all_ok else "FAIL"
        print(f"  n={n}  {flag}  ({len(rec)} partitions)")
        consistency[str(n)] = rec
        builder.add_assertion(
            name=f"D_w0_eq_schur_n{n}",
            computed=int(all_ok),
            expected=1,
            tolerance=0,
            source="sympy.cancel(D_{w_0}(λ) - hook-content) == 0",
        )

    print(f"Step 2: compute Demazure-fiber tables for n ∈ {list(n_range)}...")
    tables = {}
    nontrivial_total = 0
    for n in n_range:
        print(f"  n={n}...", flush=True)
        tables[str(n)] = collect_demazure_table(n)
        nt = sum(len(v["demazure"]) - 1 for v in tables[str(n)].values())
        nontrivial_total += nt
        print(f"    {len(tables[str(n)])} partitions, {nt} non-trivial "
              "Weyl elements")
    builder.add_assertion(
        name="non_trivial_demazure_chars",
        computed=nontrivial_total,
        expected=expected_nontrivial,
        tolerance=0,
        source=f"p(n)·n! summed over n ∈ {list(n_range)} = "
               + " + ".join(str(pn_factorial[n]) for n in n_range),
    )

    builder.add_data(
        "verification", {"demazure_w0_equals_schur": consistency}
    )
    builder.add_data("tables_by_n", tables)
    builder.add_data("precision", "symbolic_q")
    builder.add_data("truncation_eps", 0.0)

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
