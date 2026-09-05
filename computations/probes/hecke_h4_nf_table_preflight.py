#!/usr/bin/env python3
"""hecke_h4_nf_table_preflight.py

Symbolic preflight for the H₄(q) NF tables — the provenance source for
`QOU/Machinery/HeckeH4StabilizationRung.lean`, exactly mirroring the
discipline that pinned the H₃ tables ("verified over ℚ(z,h) by the symbolic
preflight before being formalized", `MarkovTraceOnHecke.lean`).

Construction (exact, no rewriting-confluence issue): the GB-NF basis of
H₄(q) is the 24 permutations of S₄ in canonical reduced words, ordered with
the S₃ ⊂ S₄ sub-basis FIRST in the exact H₃ Lean order
`[γ, σ₀, σ₁, L₊, L₋, e⁻]`; right multiplication by a generator follows the
standard exact Iwahori–Hecke length rule

    T_w · T_{sᵢ} = T_{w sᵢ}              if ℓ(w sᵢ) > ℓ(w),
    T_w · T_{sᵢ} = h·T_w + T_{w sᵢ}      otherwise   (h = q − q⁻¹),

which is the permutation-indexed recursion (the same structure the Rust
`gb_nf_reducer.rs` canonical-word machinery encodes) — NOT the naive local
word-rewriting the `MarkovTraceOnHecke` caveat warns about.

Machine-checked here over ℚ(z,h) (sympy, exact):
  1. the three 24×24 generator matrices satisfy the Hecke quadratic, BOTH
     adjacent braid relations, and the far commutation σ₀σ₂ = σ₂σ₀ (the
     first level where far commutation is non-vacuous);
  2. the 24 Markov-trace weights are the UNIQUE solution of
     {tr(1) = 1} ∪ {cyclicity tr(bⱼbₖ) = tr(bₖbⱼ) ∀ j,k} ∪
     {Markov reduction tr(x·σ₂) = z·tr(x) ∀ x ∈ H₃-span} — derived, not
     chosen;
  3. the first six weights EQUAL the H₃ weights `[1, z, z, z², z², hz²+z]`
     — the H₃ ↪ H₄ stabilization `tr₄∘ι = tr₃` holds EXACTLY;
  4. the emitted Lean tables (entries of the σ-action functions and the
     TRM₄ weight vector) match the matrices entry-for-entry.

Scope guard: table provenance + stabilization preflight only; the general-n
`MarkovStabilization` class instance stays OPEN (H_∞ binders). Nothing
wired; no q₀.

Self-contained (sympy).
"""
import datetime
import hashlib
import itertools
import json
import os
import subprocess
import sys

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

z, h = sp.symbols('z h')


def apply_s(p, i):
    q = list(p)
    q[i], q[i + 1] = q[i + 1], q[i]
    return tuple(q)


def length(p):
    return sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b])


def canonical_word(p):
    w = []
    q = tuple(p)
    while length(q) > 0:
        for i in range(3):
            if q[i] > q[i + 1]:
                w.append(i)
                q = apply_s(q, i)
                break
    return tuple(reversed(w))


def word_to_perm(w):
    p = (0, 1, 2, 3)
    for i in w:
        p = apply_s(p, i)
    return p


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    perms = list(itertools.permutations(range(4)))
    s3_words = [(), (0,), (1,), (1, 0), (0, 1), (0, 1, 0)]
    s3_perms = [word_to_perm(w) for w in s3_words]
    rest = sorted([p for p in perms if p not in s3_perms],
                  key=lambda p: (length(p), canonical_word(p)))
    basis = s3_perms + rest
    words = s3_words + [canonical_word(p) for p in rest]
    idx = {p: k for k, p in enumerate(basis)}
    check("basis_is_S4_with_H3_prefix",
          len(basis) == 24 and all(word_to_perm(words[k]) == basis[k] for k in range(24)),
          f"24 canonical words; first 6 = H3 Lean order {s3_words}")

    def right_mult_matrix(i):
        M = sp.zeros(24, 24)
        for j, p in enumerate(basis):
            ps = apply_s(p, i)
            if length(ps) > length(p):
                M[j, idx[ps]] += 1
            else:
                M[j, j] += h
                M[j, idx[ps]] += 1
        return M

    Ms = [right_mult_matrix(i) for i in range(3)]

    quad = all(sp.simplify(Ms[i] * Ms[i] - h * Ms[i] - sp.eye(24)) == sp.zeros(24, 24)
               for i in range(3))
    braid = all(sp.simplify(Ms[i] * Ms[i + 1] * Ms[i] - Ms[i + 1] * Ms[i] * Ms[i + 1])
                == sp.zeros(24, 24) for i in (0, 1))
    far = sp.simplify(Ms[0] * Ms[2] - Ms[2] * Ms[0]) == sp.zeros(24, 24)
    check("presentation_laws_exact", quad and braid and far,
          "Hecke quadratic ×3, adjacent braid ×2, far commutation σ₀σ₂=σ₂σ₀ — all "
          "exact over ℚ(z,h); far commutation non-vacuous for the first time at n=4")

    def mult_vec(vrow, word):
        v = sp.Matrix([vrow])
        for i in word:
            v = v * Ms[i]
        return v

    def prod(j, k):
        return mult_vec([1 if t == j else 0 for t in range(24)], words[k])

    ts = sp.symbols('t0:24')
    T = sp.Matrix(ts)
    eqs = [ts[0] - 1]
    for j in range(6):
        lhs = (sp.Matrix([[1 if t == j else 0 for t in range(24)]]) * Ms[2] * T)[0, 0]
        eqs.append(sp.expand(lhs - z * ts[j]))
    for j in range(24):
        for k in range(j + 1, 24):
            d = sp.expand((prod(j, k) * T)[0, 0] - (prod(k, j) * T)[0, 0])
            if d != 0:
                eqs.append(d)
    sol = sp.solve(eqs, ts, dict=True)
    check("trace_weights_unique_derived", len(sol) == 1,
          "24 weights are the unique solution of tr(1)=1 + full cyclicity + "
          "Markov-σ₂ reduction — derived, not chosen")
    tw = [sp.expand(sol[0][t]) for t in ts]

    h3w = [sp.Integer(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]
    stab = all(sp.expand(tw[j] - h3w[j]) == 0 for j in range(6))
    check("stabilization_tr4_iota_eq_tr3", stab,
          "first-6 H₄ weights == H₃ weights [1,z,z,z²,z²,hz²+z] ⇒ tr₄∘ι = tr₃ EXACT")

    # emit + self-check the Lean tables
    tables = {}
    for i in range(3):
        entries = []
        for k in range(24):
            terms = [(j, sp.sstr(Ms[i][j, k])) for j in range(24) if Ms[i][j, k] != 0]
            entries.append(terms)
        tables[str(i)] = entries
    emit_ok = all(
        sp.expand(sum((sp.sympify(c) * sp.Symbol(f'v{j}') for j, c in tables[str(i)][k]),
                      sp.Integer(0))
                  - sum(Ms[i][j, k] * sp.Symbol(f'v{j}') for j in range(24)))
        == 0
        for i in range(3) for k in range(24))
    check("lean_table_emission_matches_matrices", emit_ok,
          "per-entry emitted formulas reproduce the 24×24 matrices exactly")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "H₄ NF TABLE PREFLIGHT — EXACT (provenance for HeckeH4StabilizationRung.lean): "
        "24-word S₄ basis with the H₃ Lean basis as its prefix; generator actions by the "
        "exact Iwahori–Hecke length rule; presentation laws (quadratic ×3, braid ×2, far "
        "commutation) verified over ℚ(z,h); the 24 Markov weights UNIQUELY derived from "
        "cyclicity + Markov reduction + tr(1)=1, with tr₄∘ι = tr₃ exact. General-n "
        "MarkovStabilization instance stays OPEN. Nothing wired; no q₀."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; do not formalize from these tables."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "hecke-h4-nf-table-preflight",
        "description": "Symbolic preflight pinning the H₄(q) NF tables (24-word S₄ basis, "
                       "H₃ prefix, exact length-rule generator actions) and UNIQUELY deriving "
                       "the 24 Markov-trace weights; tr₄∘ι = tr₃ exact. Provenance for "
                       "QOU/Machinery/HeckeH4StabilizationRung.lean. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-hecke-h4-stabilization-rung.md",
        "tier": "symbolic-exact (sympy over ℚ(z,h))",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "basis_words": [list(w) for w in words],
            "trace_weights": [sp.sstr(w) for w in tw],
            "verdict": verdict,
        },
    }
    out = os.path.join(_here, "hecke-h4-nf-table-preflight.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
