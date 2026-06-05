#!/usr/bin/env python3
"""Symbolic cross-check for `QOU.Machinery.MarkovTraceOnHecke` cyclicity.

Provenance artifact for the Lean theorem `trM_cyclic` (trace cyclicity
`tr_M(u·v) = tr_M(v·u)` on the H₃(q) NF model) and the full algebra
product `mulNF`. Replicates `tools/pyhecke/python/pyhecke/gram.py`'s `hm`
(right-multiplication by a generator) with `h, z` SYMBOLIC — no substrate
/ pyhecke import needed, since `hm` is pure arithmetic in `h` — and
verifies, over ℚ(z, h):

  (A)  cyclicity `tr_M(b_i b_j) = tr_M(b_j b_i)` for all 36 basis pairs;
  (A') the full bilinear statement `tr_M(u·v) − tr_M(v·u) = 0` (the exact
       Lean `trM_cyclic` claim) with symbolic `u, v`;
  (B)  the `mulNF` generator-composition order used in Lean (note the
       non-obvious `b₃ = σ₁σ₀`, `b₄ = σ₀σ₁` from the `hm` convention);
  (C)  the Hecke `σ₀² = h·σ₀ + 1` and Markov `tr(x·σ₁) = z·tr(x)` laws
       already proved in the Lean module (sanity).

EXPLORATORY / cross-check — NOT a wire decision. Δ_λ-gate: nothing wired;
c_3 unchanged. This file only validates the Markov-trace *machinery*.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

h, z = sp.symbols("h z")

# NF basis order [γ, σ₀, σ₁, L₊, L₋, e⁻]; TR_M mirrors gram.TR_M.
TR_M = [sp.Integer(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]


def hm(nf, c, d, gen):
    """Right-multiply NF 6-vector by (c·σ_gen + d·I).  Mirror of gram.hm."""
    r = [sp.Integer(0)] * 6
    if gen == 0:
        tables = [(0, [(1, c), (0, d)]), (1, [(1, c * h), (0, c), (1, d)]),
                  (2, [(3, c), (2, d)]), (3, [(3, c * h), (2, c), (3, d)]),
                  (4, [(5, c), (4, d)]), (5, [(5, c * h), (4, c), (5, d)])]
    else:
        tables = [(0, [(2, c), (0, d)]), (1, [(4, c), (1, d)]),
                  (2, [(2, c * h), (0, c), (2, d)]), (3, [(5, c), (3, d)]),
                  (4, [(4, c * h), (1, c), (4, d)]), (5, [(5, c * h), (3, c), (5, d)])]
    for si, tgts in tables:
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return [sp.expand(x) for x in r]


def e(i):
    v = [sp.Integer(0)] * 6
    v[i] = sp.Integer(1)
    return v


def mulσ0(v):
    return hm(v, 1, 0, 0)


def mulσ1(v):
    return hm(v, 1, 0, 1)


def tr(v):
    return sp.expand(sum(v[i] * TR_M[i] for i in range(6)))


def nf_of_word(word):
    v = e(0)
    for g in word:
        v = hm(v, 1, 0, g)
    return v


def main() -> int:
    # ── (B) producing word W_j with nf_of_word(W_j) = e_j ─────────────
    candidate_words = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    word_to_index = {}
    for w in candidate_words:
        nf = nf_of_word(w)
        idx = [i for i in range(6)
               if nf[i] == 1 and all(nf[k] == 0 for k in range(6) if k != i)]
        word_to_index[w] = idx[0] if idx else None
    assert all(v is not None for v in word_to_index.values()), \
        f"a producing word failed to reduce to a basis index: {word_to_index}"
    assert sorted(word_to_index.values()) == list(range(6)), \
        f"producing words must hit each basis index exactly once: {word_to_index}"
    index_to_word = {i: w for w, i in word_to_index.items()}

    def Rb(j, u):                       # right-mult by b_j = R_{W_j}
        out = u
        for g in index_to_word[j]:
            out = mulσ0(out) if g == 0 else mulσ1(out)
        return out

    def mul(u, v):                      # u·v = Σ_j v_j (u·b_j)
        acc = [sp.Integer(0)] * 6
        for j in range(6):
            ub = Rb(j, u)
            for k in range(6):
                acc[k] += v[j] * ub[k]
        return [sp.expand(x) for x in acc]

    # ── (A) cyclicity on all 36 basis pairs ──────────────────────────
    pair_fails = [(i, j) for i in range(6) for j in range(6)
                  if sp.expand(tr(mul(e(i), e(j))) - tr(mul(e(j), e(i)))) != 0]

    # ── (A') full bilinear cyclicity (the Lean statement) ────────────
    U = list(sp.symbols("u0:6"))
    V = list(sp.symbols("v0:6"))
    bilinear_diff = sp.expand(tr(mul(U, V)) - tr(mul(V, U)))

    # ── (C) Hecke + Markov sanity ────────────────────────────────────
    hecke_resid = [sp.expand(a - b) for a, b in zip(
        mulσ0(mulσ0(e(1))), [h * x + y for x, y in zip(mulσ0(e(1)), e(1))])]
    a_, b_ = sp.symbols("a b")
    x_h2 = [a_, b_, 0, 0, 0, 0]          # x ∈ H₂ = span{γ, σ₀}
    markov_resid = sp.expand(tr(mulσ1(x_h2)) - z * tr(x_h2))

    lean_terms = []
    for j in range(6):
        comp = "u"
        for g in index_to_word[j]:
            comp = f"mulσ{g} ({comp})"
        lean_terms.append({"j": j, "word": str(index_to_word[j]), "u_dot_bj": comp})

    assertions = [
        {"name": "cyclicity_all_36_basis_pairs",
         "computed": len(pair_fails), "expected": 0, "passed": not pair_fails,
         "source": "tr_M(b_i b_j) = tr_M(b_j b_i) for all i,j ∈ Fin 6 over ℚ(z,h)."},
        {"name": "cyclicity_full_bilinear_trM_uv_eq_vu",
         "computed": str(bilinear_diff), "expected": "0",
         "passed": bilinear_diff == 0,
         "source": "tr_M(u·v) − tr_M(v·u) expands to 0 with symbolic u,v "
                   "— the exact Lean `trM_cyclic` identity."},
        {"name": "hecke_sigma0_sq_eq_h_sigma0_plus_1",
         "computed": int(all(x == 0 for x in hecke_resid)), "expected": 1,
         "passed": all(x == 0 for x in hecke_resid),
         "source": "σ₀² = h·σ₀ + 1 on σ₀ (Lean `mulσ₀_hecke`)."},
        {"name": "markov_reduction_tr_x_sigma1_eq_z_tr_x_on_H2",
         "computed": str(markov_resid), "expected": "0",
         "passed": markov_resid == 0,
         "source": "tr(x·σ₁) = z·tr(x) for x ∈ H₂ (Lean `trM_markov_σ₁`)."},
    ]
    witness = {
        "engine": "sympy",
        "engineVersion": f"sympy-{sp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "h3-markov-trace-cyclicity-preflight",
        "scriptFile": "h3_markov_trace_cyclicity_preflight.py",
        "tier": "cross-check/provenance",
        "validates": "QOU.Machinery.MarkovTraceOnHecke.trM_cyclic + mulNF",
        "assertions": assertions,
        "data": {"mulNF_lean_terms": lean_terms,
                 "word_to_index": {str(w): i for w, i in word_to_index.items()}},
        "deltaLambdaGate": {"fittedForms": False, "wiredToProduction": False,
                            "note": "validates Markov-trace machinery only; c_3 unchanged."},
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    out = Path(__file__).resolve().parent / "h3-markov-trace-cyclicity-preflight.witness.json"
    out.write_text(json.dumps(witness, indent=2))

    print("✓ h3-markov-trace-cyclicity-preflight.witness.json")
    print(f"  (A) cyclicity all 36 basis pairs: {'PASS' if not pair_fails else pair_fails}")
    print(f"  (A') full bilinear tr(uv)-tr(vu) = {bilinear_diff}")
    print(f"  (B) mulNF order: " + ", ".join(f"v{t['j']}·{t['u_dot_bj']}" for t in lean_terms))
    print(f"  (C) Hecke OK={all(x==0 for x in hecke_resid)}  Markov OK={markov_resid==0}")
    assert witness["allPassed"], "cyclicity cross-check FAILED"
    return 0


if __name__ == "__main__":
    sys.exit(main())
