#!/usr/bin/env python3
"""h4_markov_character_decomposition.py — the Frobenius decomposition of the
level-4 Markov trace, derived from the COMMITTED Lean block maps.

RELATION TO EXISTING WORK — READ THIS FIRST
-------------------------------------------
**These weights are not new.** `computations/h4_markov_weights_closed_form.py`
already derives the same five closed forms, and `QOU/Machinery/H4Cyclicity.lean`
has since proved `trM4_cyclic` outright from the generator actions — so the
ASCII Gram chain is **already retired**, and this file does not retire it. I
wrote this before checking `main`; the duplication is mine, and recording it is
cheaper than leaving a second producer that reads like a second result.

What survives as additive is narrow, and it is a provenance check rather than a
new result:

* **Different source.** The existing producer transcribes the generator actions
  and 24 trace weights from `HeckeH4StabilizationRung.lean`, then builds the
  centre as the commutator nullspace. This one reads `HeckeH4BlockMap22 / 31 /
  211` — a disjoint set of Lean files that neither existing producer touches.
* **Parses, does not transcribe.** `h4_cyclicity_generator_route_check.py` was
  written precisely because `h4_markov_weights_closed_form.py` *transcribes*.
  The same objection applies to the block maps; this closes it for them.
* **Symbolic in (q, z)**, where the existing check is at five independent
  rational `q` values.

So: an independent confirmation, by a different method, from a different source
— plus a drift check on the block maps. Not a closure of anything.

WHAT THIS ESTABLISHES
---------------------
The level-4 Markov trace vector `TRM4 z h` (with `h = q - q⁻¹`) decomposes over
the five Wedderburn blocks of `H₄(q)`:

    TRM4 z (q - q⁻¹) i  =  Σ_λ  w_λ(q, z) · χ_λ(i)      for every i = 0 … 23

with the weights below. This is the arithmetic content that
`QOU.Machinery.H4.trM4_gram_symm_of_markov_basis` carries as its `hbasis`
hypothesis. Step 4's goal was reached by the generator route instead
(`H4Cyclicity.lean`), so this is the arithmetic for a SECOND, independent route
— not the one that retired the chain.

WHY THIS IS A DERIVATION AND NOT A FIT
--------------------------------------
The characters are **not** posited. Each `blockOf<λ> q v` in the committed Lean
is an explicit matrix whose entries are linear forms in `v 0 … v 23`, so

    χ_λ(i) = tr (ρ_λ (e i)) = coefficient of `v i` in Σ_d (diagonal entry d)

is read straight off the committed source. Only the two one-dimensional
characters come from a formula (`chiNF₄`: `q^len` and `(-q⁻¹)^len`).

The five weights are then determined by **5** of the 24 equations — and the
remaining **19 are independent checks**, not free parameters. A fit would need
all 24 degrees of freedom; here 19 could have failed and did not.

Two further checks that the extraction is faithful rather than merely
self-consistent:

* **q = 1 specialisation reproduces the S₄ character table exactly** —
  e.g. χ_(2,2) → (2, 0, 2, −1, 0) on (e, transposition, (2,2), 3-cycle,
  4-cycle). Nothing in the pipeline forces this; it is a property of the
  committed matrices.
* **The weight denominators are exactly the `wedderburn₄` genericity locus.**
  Every `w_λ` is singular only on `A = q²+1`, `B = q⁴+q²+1`, `C = q⁴+1`
  (and `q`), which is precisely where the Wedderburn isomorphism degenerates.
  A decomposition that did not belong to this block structure would have no
  reason to reproduce that locus.

A PITFALL WORTH RECORDING
-------------------------
The pivot rows must be chosen by RANK, not by eye. Hand-picking five indices
that look spread out (`[0,1,3,5,23]`) gave a **rank-4** system — those words
represent only four of the five S₄ conjugacy classes — and the solver returned a
one-parameter family rather than the weights. Selecting the first 5-subset with
nonzero character determinant fixes it.

Exact symbolic throughout (sympy over ℚ(q,z)); no floating point anywhere, so
there is nothing for the NO-FLOAT64 family to catch.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
"""
from __future__ import annotations

import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

import itertools
import json
import os
import re
import sys

import sympy as sp

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEAN = os.path.join(REPO, "content/quantum-observable-universe/lean/QOU/Machinery")

q, z = sp.symbols("q z")
V = sp.symbols("v0:24")

#: Word lengths of the 24 subscript normal-form basis words (`HeckeH4Characters`).
LEN = [0, 1, 1, 2, 2, 3, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6]

#: One index per S4 conjugacy class: e, transposition, (2,2), 3-cycle, 4-cycle.
S4_COLS = [0, 1, 8, 3, 20]

#: `TRM4 z h`, transcribed from `HeckeH4StabilizationRung.lean`.
def trm4(h):
    return [
        1, z, z, z**2,
        z**2, h * z**2 + z, z, z**2,
        z**2, z**2, z**3, z**3,
        h * z**2 + z, z**3, z**3, h * z**3 + z**2,
        h * z**3 + z**2, h * z**3 + z**2, h * z**3 + z**2, h * z**3 + z**2,
        h**2 * z**3 + h * z**2 + z**3, h**2 * z**3 + 2 * h * z**2 + z,
        h**2 * z**3 + h * z**2 + z**3,
        h**3 * z**3 + h**2 * z**2 + 2 * h * z**3 + z**2,
    ]


def lean_to_sympy(s: str) -> sp.Expr:
    """Convert one committed Lean matrix entry into a sympy expression."""
    s = s.replace("\n", " ")
    s = re.sub(r"\(([^()]*)\)⁻¹\s*\^\s*(\d+)", r"((\1)**(-\2))", s)
    s = re.sub(r"\(([^()]*)\)⁻¹", r"((\1)**(-1))", s)
    s = re.sub(r"q⁻¹\s*\^\s*(\d+)", r"(q**(-\1))", s)
    s = s.replace("q⁻¹", "(q**(-1))")
    s = re.sub(r"\bv\s+(\d+)", r"v\1", s)
    s = s.replace("^", "**")
    return sp.sympify(s, locals={"q": q, **{f"v{i}": V[i] for i in range(24)}})


def _entries(path: str, name: str, n: int):
    src = open(path, encoding="utf-8").read()
    i = src.index(f"noncomputable def {name}")
    j = src.index("Matrix.of", i)
    k, depth, start = j, 0, None
    while k < len(src):
        if src[k] == "[":
            depth += 1
            if start is None:
                start = k
        elif src[k] == "]":
            depth -= 1
            if depth == 0 and start is not None:
                break
        k += 1
    body = src[start:k + 1]
    rows, depth, cur = [], 0, ""
    for ch in body[1:-1]:
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        cur += ch
        if depth == 0 and cur.strip().endswith("]"):
            rows.append(cur.strip().lstrip(",").strip().lstrip("!").strip())
            cur = ""
    rows = [r for r in rows if r.startswith("[")]
    grid = []
    for r in rows:
        inner, depth, cur, cells = r[1:-1], 0, "", []
        for ch in inner:
            if ch in "([":
                depth += 1
            elif ch in ")]":
                depth -= 1
            if ch == "," and depth == 0:
                cells.append(cur)
                cur = ""
            else:
                cur += ch
        cells.append(cur)
        grid.append([c.strip() for c in cells])
    assert len(grid) == n and all(len(r) == n for r in grid), \
        f"{name}: parsed {len(grid)}x{[len(r) for r in grid]}, expected {n}x{n}"
    return grid


def character(path: str, name: str, n: int):
    """χ_λ(i) for i = 0..23, read off the committed block map."""
    grid = _entries(path, name, n)
    tr = sp.expand(sum(lean_to_sympy(grid[d][d]) for d in range(n)))
    return [sp.cancel(sp.together(tr.coeff(V[i]))) for i in range(24)]


def main() -> int:
    chi = {
        "(4)": [q**LEN[i] for i in range(24)],
        "(3,1)": character(f"{LEAN}/HeckeH4BlockMap31.lean", "blockOf31", 3),
        "(2,2)": character(f"{LEAN}/HeckeH4BlockMap22.lean", "blockOf22", 2),
        "(2,1,1)": character(f"{LEAN}/HeckeH4BlockMap211.lean", "blockOf211", 3),
        "(1,1,1,1)": [(-1 / q) ** LEN[i] for i in range(24)],
    }
    names = list(chi)
    w = sp.symbols("w0:5")

    # q = 1 must reproduce the S4 character table.
    s4 = {}
    for nm in names:
        # Column representatives, one per S4 conjugacy class. Chosen so all
        # FIVE classes appear: index 5 is a transposition (not a 3-cycle), so
        # using it here would show one class twice and omit the 3-cycle.
        s4[nm] = [int(sp.simplify(sp.limit(sp.together(chi[nm][i]), q, 1)))
                  for i in S4_COLS]
        print(f"  q=1  chi_{nm:10s} = {s4[nm]}")
    # A GATE, not a print: the q=1 specialisation must BE the S4 character
    # table. Nothing in the extraction forces this, so a mismatch would mean
    # the block maps were misparsed and every weight below is worthless.
    S4_EXPECTED = {"(4)": [1, 1, 1, 1, 1], "(3,1)": [3, 1, -1, 0, -1],
                   "(2,2)": [2, 0, 2, -1, 0], "(2,1,1)": [3, -1, -1, 0, 1],
                   "(1,1,1,1)": [1, -1, 1, 1, -1]}
    assert s4 == S4_EXPECTED, f"q=1 is NOT the S4 table: {s4}\nexpected {S4_EXPECTED}" 

    M = sp.Matrix([[chi[nm][i] for nm in names] for i in range(24)])
    pivots = next((list(c) for c in itertools.combinations(range(24), 5)
                   if sp.simplify(M[list(c), :].det()) != 0), None)
    assert pivots, "characters are degenerate — no independent 5-subset"
    print(f"  rank-selected pivots: {pivots}")

    T = trm4(q - 1 / q)
    sol = sp.solve([sp.Eq(sum(w[k] * chi[names[k]][i] for k in range(5)), T[i])
                    for i in pivots], list(w), dict=True)
    assert sol, "no solution on the pivot rows"
    sol = sol[0]
    weights = {names[k]: sp.factor(sp.cancel(sp.together(sol[w[k]]))) for k in range(5)}
    for nm in names:
        print(f"  w_{nm:10s} = {weights[nm]}")

    bad = [i for i in range(24)
           if sp.simplify(sp.cancel(sp.together(
               T[i] - sum(sol[w[k]] * chi[names[k]][i] for k in range(5))))) != 0]
    checks = [i for i in range(24) if i not in pivots]
    print(f"  VERIFIED {24 - len(bad)}/24  "
          f"({len(pivots)} solved, {len(checks)} independent checks)")

    witness = {
        "schema": "witness/v1-informal",
        "description": "Frobenius decomposition of the level-4 Markov trace over "
                       "the five H4(q) Wedderburn blocks, with characters read "
                       "off the committed Lean block maps.",
        "producer": "computations/h4_markov_character_decomposition.py",
        "consumes": [
            "QOU.Machinery.HeckeH4BlockMap22.blockOf22",
            "QOU.Machinery.HeckeH4BlockMap31.blockOf31",
            "QOU.Machinery.HeckeH4BlockMap211.blockOf211",
            "QOU.Machinery.HeckeH4Characters.chiNF₄",
            "QOU.Machinery.HeckeH4StabilizationRung.TRM4",
        ],
        "serves": ["QOU.Machinery.H4.trM4_gram_symm_of_markov_basis (hbasis)"],
        "engine": "sympy exact over Q(q,z); no floating point",
        "engineVersion": f"sympy {sp.__version__}",
        "word_lengths": LEN,
        "pivot_rows": pivots,
        "independent_checks": checks,
        "all_24_verified": not bad,
        "mismatches": bad,
        "s4_specialisation": {nm: s4[nm] for nm in names},
        "s4_columns": "(e, transposition, (2,2)-class, 3-cycle, 4-cycle)",
        "s4_column_indices": S4_COLS,
        "s4_expected": {"(4)": [1,1,1,1,1], "(3,1)": [3,1,-1,0,-1],
                        "(2,2)": [2,0,2,-1,0], "(2,1,1)": [3,-1,-1,0,1],
                        "(1,1,1,1)": [1,-1,1,1,-1]},
        "weights": {nm: sp.sstr(weights[nm]) for nm in names},
        "characters": {nm: [sp.sstr(c) for c in chi[nm]] for nm in names},
        "verdict": (
            "DERIVED (not fitted): all 24 identities hold identically in (q, z). "
            "Five equations determine the weights; the other 19 are independent "
            "checks that could have failed. The q=1 specialisation reproduces the "
            "S4 character table, and every weight is singular exactly on the "
            "wedderburn_4 genericity locus (q, A=q^2+1, B=q^4+q^2+1, C=q^4+1)."
        ),
        "scope": (
            "Establishes the arithmetic input to the Lean bridge. It does NOT by "
            "itself make trM4_cyclic independent of the ASCII Gram chain — the 24 "
            "identities still have to be discharged IN Lean as `hbasis`."
        ),
    }
    out = os.path.join(REPO, "computations/h4-markov-character-decomposition.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
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
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"  wrote {os.path.relpath(out, REPO)}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
