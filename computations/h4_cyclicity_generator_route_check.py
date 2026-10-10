#!/usr/bin/env python3
"""Independent symbolic re-derivation of the H₄ generator-route cyclicity proof
(bean ``qou-x64l``, the ``H4GeneratorAction`` / ``H4WordAction`` /
``H4Cyclicity`` modules).

Why this exists
---------------
``QOU.Machinery.H4.trM4_cyclic`` is proved in Lean without the ASCII Gram
chain, by the observation that the trace-central elements form a *subalgebra*,
so cyclicity need only be checked on the three generators. Those three modules
were emitted by a generator script rather than typed by hand, and their
docstrings claim the emitter read its tables out of the Lean sources and
checked the resulting identities symbolically before any Lean was written.

**That emitter was never committed.** This script makes the claim checkable
again: it re-derives the same content from the same single source of truth and
re-checks the committed Lean against it. It is deliberately a *reader* of the
Lean sources — nothing here is transcribed, so a later edit to
``HeckeH4StabilizationRung.lean`` cannot silently invalidate it.

Note the contrast with ``h4_markov_weights_closed_form.py``, which states that
it *transcribes* the same three generator actions. Parsing rather than
transcribing is what lets this script also serve as a drift check on that one.

What is checked
---------------
1. **Tables parsed, not transcribed.** ``mulσ₀/₁/₂`` and ``TRM4`` are read out
   of ``QOU/Machinery/HeckeH4StabilizationRung.lean``; the 24 basis words are
   read out of ``wordAction`` in ``QOU/Machinery/HeckeH4AlgebraLaws.lean``.

2. **The Hecke presentation**, re-derived from the parsed actions alone: both
   quadratics ``σᵢ² = h·σᵢ + 1``, both braid relations, and far commutation.
   This is the check that the parse means what the module says it means.

3. **The 72 cyclicity identities** — for each basis word ``b_j`` and each
   generator ``σᵢ``,  ``tr(σᵢ · b_j) = tr(b_j · σᵢ)``, symbolically with ``z``
   and ``h`` free. These are the atomic facts ``H4Cyclicity`` proves in Lean;
   together with the subalgebra argument (associativity alone, proved there)
   they give ``trM4_cyclic``.

4. **The structural fact the word induction rests on**: every basis word
   ``b_j`` other than the identity is ``b_inner · σᵢ`` for a strictly shorter
   basis word ``b_inner``, and that product is a *single* basis vector on the
   nose — no quadratic fold. This is what lets ``H4WordAction`` peel one
   generator at a time.

5. **The committed Lean statements match the parsed tables, and cover every
   case.** The ``mulσᵢ_e₄_j`` statements of ``H4GeneratorAction.lean`` are
   parsed back out of the source and compared against the action computed here;
   then the set of ``(i, j)`` pairs is asserted to be exactly the 72 expected,
   each appearing once. The coverage half is the part Lean cannot do — it
   checks only the statements that are written, never the ones that are absent.

Note on what this does and does not add. Every statement checked here is
*already* machine-checked by Lean, so this script cannot make the theorem more
true — Lean proving ``mulσ₀_e₄_1`` means that statement holds. What it adds is
a check on the layer Lean cannot see: that the committed statements are about
the tables the modules claim to be about, computed by an independent
implementation. A Lean file can be sorry-free and internally consistent while
enumerating the wrong 72 facts; that is the failure mode this closes.

Mutation-tested — the checks discriminate
-----------------------------------------
A checker that cannot fail is worth nothing, so this one was run against four
deliberate corruptions of the sources, each restored afterwards. It caught all
four, and — the part that matters — each broke only the checks that actually
depend on what was corrupted:

===============================  ====================================================
corruption                       result
===============================  ====================================================
``TRM4[2]``  ``z`` → ``z^3``     [3] 4 failures; [2] [4] [5] unaffected (they do
(the trace table)                not read ``TRM4``)
``mulσ₀_e₄_6`` RHS               [5] 1 failure, naming the exact coefficient:
``e₄ 8`` → ``e₄ 9``              *"coefficient 8 disagrees with the table"*;
(a committed Lean statement)     [3] unaffected — the table itself is still sound
``mulσ₀`` row 2                  [2] presentation broken (quadratic, braid, far
``v 3`` → ``v 4``                commutation), [3] 18, [4] 4, [5] 2 — the deepest
(the generator action)           table, so everything downstream fails
``theorem mulσ₀_e₄_6``           [5] 71 statements, 1 failure:
**deleted entirely**             *"MISSING — no such statement in the file"*
===============================  ====================================================

The first three make some statement **false**, so Lean rejects them too — on
those this script is a redundant second opinion, not a unique catch. **The
fourth is the one Lean structurally cannot see:** delete a fact and every
remaining statement is still true, still sorry-free, still axiom-clean. Lean
only ever checks the statements that are written, never the ones that are
absent. So check [5] also asserts that the 72 ``(generator, basis)`` pairs are
present exactly once each — that coverage assertion, rather than the
per-statement comparison, is this script's distinct contribution.

Arithmetic and anchor
---------------------
Exact throughout — sympy over ``ℚ[z, h]``; no floats. The identities hold
identically in ``z`` and ``h``, so **nothing here is evaluated at a substrate
pin**. The canonical experimental (proton) anchor is still recorded, read live
from ``qou_substrate.constants`` rather than transcribed, per the 2026-08-07
owner directive: a reader must be able to tell which layer a witness belongs to
without inferring it from a call site. Same convention as the sibling producer
``h4_markov_weights_closed_form.py``.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
LEAN = REPO / "folio/quantum-observable-universe/lean/QOU/Machinery"
RUNG = LEAN / "HeckeH4StabilizationRung.lean"
LAWS = LEAN / "HeckeH4AlgebraLaws.lean"
GENACT = LEAN / "H4GeneratorAction.lean"

N = 24
z, h = sp.symbols("z h")

# Lean subscript digits used in the generator names.
SUB = {"₀": 0, "₁": 1, "₂": 2}


# --------------------------------------------------------------------------
# 1. Parse the source tables
# --------------------------------------------------------------------------
def _bracket_body(text: str, header_re: str) -> str:
    """Return the body of the ``![ ... ]`` literal following a `def` header."""
    m = re.search(header_re, text)
    if not m:
        raise SystemExit(f"parse: header not found: {header_re}")
    start = text.index("![", m.end()) + 2
    depth = 1
    i = start
    while depth:
        if text[i] == "[":
            depth += 1
        elif text[i] == "]":
            depth -= 1
        i += 1
    return text[start : i - 1]


def parse_mul_sigma(text: str, idx: int) -> list[dict[int, sp.Expr]]:
    """``mulσ_idx`` as 24 rows; row k maps source index -> coefficient.

    A row is ``v j`` or ``v j + h * v k``: the image of the basis under the
    right action, written in the basis.
    """
    body = _bracket_body(text, rf"def\s+mulσ{'₀₁₂'[idx]}\s*\(")
    entries = [e.strip() for e in body.split(",")]
    if len(entries) != N:
        raise SystemExit(f"mulσ{idx}: expected {N} entries, got {len(entries)}")
    rows = []
    for e in entries:
        row: dict[int, sp.Expr] = {}
        for term in e.split("+"):
            term = term.strip()
            if m := re.fullmatch(r"v\s+(\d+)", term):
                row[int(m.group(1))] = row.get(int(m.group(1)), sp.Integer(0)) + 1
            elif m := re.fullmatch(r"h\s*\*\s*v\s+(\d+)", term):
                row[int(m.group(1))] = row.get(int(m.group(1)), sp.Integer(0)) + h
            else:
                raise SystemExit(f"mulσ{idx}: unparsed term {term!r} in {e!r}")
        rows.append(row)
    return rows


def parse_trm4(text: str) -> list[sp.Expr]:
    body = _bracket_body(text, r"def\s+TRM4\s*\(")
    entries = [e.strip() for e in body.split(",")]
    if len(entries) != N:
        raise SystemExit(f"TRM4: expected {N} entries, got {len(entries)}")
    return [sp.sympify(e.replace("^", "**"), locals={"z": z, "h": h}) for e in entries]


def parse_word_actions(text: str) -> list[list[int]]:
    """The 24 basis words, as generator lists in *application* order.

    ``wordAction j`` is written outside-in — ``mulσ₀ h (mulσ₁ h u)`` applies
    ``σ₁`` first — so the returned list is reversed into application order:
    ``b_3 = σ₁·σ₀`` gives ``[1, 0]``.
    """
    body = _bracket_body(text, r"def\s+wordAction\s*\(")
    lams = re.findall(r"fun u =>(.*?)(?=,\s*\n\s*fun u =>|$)", body, flags=re.S)
    if len(lams) != N:
        raise SystemExit(f"wordAction: expected {N} lambdas, got {len(lams)}")
    words = []
    for lam in lams:
        gens = [SUB[s] for s in re.findall(r"mulσ([₀₁₂])", lam)]
        words.append(list(reversed(gens)))
    return words


# --------------------------------------------------------------------------
# 2. Action machinery
# --------------------------------------------------------------------------
def apply_gen(rows: list[dict[int, sp.Expr]], vec: list[sp.Expr]) -> list[sp.Expr]:
    """Right-multiply a coefficient vector by a generator."""
    return [sp.expand(sum(c * vec[src] for src, c in rows[k].items())) for k in range(N)]


def basis(j: int) -> list[sp.Expr]:
    return [sp.Integer(1) if i == j else sp.Integer(0) for i in range(N)]


def word_vec(word: list[int], gens, start: int = 0) -> list[sp.Expr]:
    v = basis(start)
    for g in word:
        v = apply_gen(gens[g], v)
    return v


def trace(vec: list[sp.Expr], trm4: list[sp.Expr]) -> sp.Expr:
    return sp.expand(sum(vec[i] * trm4[i] for i in range(N)))


def is_single_basis_vector(vec: list[sp.Expr]) -> int | None:
    """Index if ``vec`` is exactly one basis vector with coefficient 1."""
    hits = [i for i, c in enumerate(vec) if sp.simplify(c) != 0]
    if len(hits) == 1 and sp.simplify(vec[hits[0]] - 1) == 0:
        return hits[0]
    return None


# --------------------------------------------------------------------------
# 3. Checks
# --------------------------------------------------------------------------
def check_presentation(gens) -> list[str]:
    """Re-derive the Hecke presentation from the parsed actions alone."""
    fails = []
    for i in range(3):
        for j0 in range(N):
            v = basis(j0)
            lhs = apply_gen(gens[i], apply_gen(gens[i], v))
            rhs = [sp.expand(h * a + b) for a, b in zip(apply_gen(gens[i], v), v)]
            if any(sp.simplify(a - b) != 0 for a, b in zip(lhs, rhs)):
                fails.append(f"quadratic σ{i}² on e{j0}")
                break
    for i, j in ((0, 1), (1, 2)):
        for j0 in range(N):
            v = basis(j0)
            lhs = word_vec([i, j, i], gens, j0) if False else None
            a = apply_gen(gens[i], apply_gen(gens[j], apply_gen(gens[i], v)))
            b = apply_gen(gens[j], apply_gen(gens[i], apply_gen(gens[j], v)))
            if any(sp.simplify(x - y) != 0 for x, y in zip(a, b)):
                fails.append(f"braid σ{i}σ{j}σ{i} on e{j0}")
                break
    for j0 in range(N):
        v = basis(j0)
        a = apply_gen(gens[0], apply_gen(gens[2], v))
        b = apply_gen(gens[2], apply_gen(gens[0], v))
        if any(sp.simplify(x - y) != 0 for x, y in zip(a, b)):
            fails.append(f"far commutation σ0σ2 on e{j0}")
            break
    return fails


def check_cyclicity(words, gens, trm4):
    """The 72 atomic identities ``tr(σᵢ·b_j) = tr(b_j·σᵢ)``."""
    fails, checked = [], 0
    for j, word in enumerate(words):
        bj = word_vec(word, gens)                      # b_j = 1 · b_j
        for i in range(3):
            left = word_vec(word, gens, start=0)
            # σᵢ · b_j : start from the generator, then apply the word.
            sig = apply_gen(gens[i], basis(0))
            v = sig
            for g in word:
                v = apply_gen(gens[g], v)
            lhs = trace(v, trm4)
            # b_j · σᵢ
            rhs = trace(apply_gen(gens[i], bj), trm4)
            checked += 1
            if sp.simplify(sp.expand(lhs - rhs)) != 0:
                fails.append(f"tr(σ{i}·b_{j}) ≠ tr(b_{j}·σ{i})")
            del left
    return checked, fails


def check_word_tree(words, gens):
    """Every non-identity word is (shorter word)·generator, a single term."""
    fails, edges = [], 0
    index_of = {tuple(w): j for j, w in enumerate(words)}
    for j, word in enumerate(words):
        if not word:
            continue
        inner, g = word[:-1], word[-1]
        if tuple(inner) not in index_of:
            fails.append(f"b_{j}: prefix {inner} is not a basis word")
            continue
        b_inner = word_vec(inner, gens)
        prod = apply_gen(gens[g], b_inner)
        hit = is_single_basis_vector(prod)
        edges += 1
        if hit is None:
            fails.append(f"b_{j}: σ{g}·b_inner is not a single basis vector")
        elif hit != j:
            fails.append(f"b_{j}: σ{g}·b_inner = e{hit}, expected e{j}")
    return edges, fails


def check_lean_generator_action(gens):
    """Parse the committed ``mulσᵢ_e₄_j`` statements and compare to the table."""
    text = GENACT.read_text()
    pat = re.compile(
        r"theorem\s+mulσ([₀₁₂])_e₄_(\d+)\s*\([^)]*\)\s*:\s*"
        r"mulσ[₀₁₂]\s+h\s+\(e₄\s+\((\d+)\s*:\s*Fin 24\)\)\s*=\s*(.*?)\s*:=\s*by",
        re.S,
    )
    fails, checked = [], 0
    seen: list[tuple[int, int]] = []
    for m in pat.finditer(text):
        i, jname, jarg, rhs = SUB[m.group(1)], int(m.group(2)), int(m.group(3)), m.group(4)
        seen.append((i, jname))
        if jname != jarg:
            fails.append(f"mulσ{i}_e₄_{jname}: name/argument mismatch ({jarg})")
            continue
        claimed: dict[int, sp.Expr] = {}
        for term in rhs.split("+"):
            term = term.strip()
            if mm := re.fullmatch(r"e₄\s*\((\d+)\s*:\s*Fin 24\)", term):
                k = int(mm.group(1))
                claimed[k] = claimed.get(k, sp.Integer(0)) + 1
            elif mm := re.fullmatch(r"h\s*•\s*e₄\s*\((\d+)\s*:\s*Fin 24\)", term):
                k = int(mm.group(1))
                claimed[k] = claimed.get(k, sp.Integer(0)) + h
            else:
                fails.append(f"mulσ{i}_e₄_{jname}: unparsed RHS term {term!r}")
                claimed = None
                break
        if claimed is None:
            continue
        actual = apply_gen(gens[i], basis(jarg))
        checked += 1
        for k in range(N):
            if sp.simplify(actual[k] - claimed.get(k, sp.Integer(0))) != 0:
                fails.append(f"mulσ{i}_e₄_{jname}: coefficient {k} disagrees with the table")
                break

    # Coverage — the half Lean cannot check, since it only ever sees the
    # statements that were written, never the ones that are absent.
    expected = {(i, j) for i in range(3) for j in range(N)}
    got = set(seen)
    for dup in sorted({p for p in seen if seen.count(p) > 1}):
        fails.append(f"mulσ{dup[0]}_e₄_{dup[1]}: stated more than once")
    for miss in sorted(expected - got):
        fails.append(f"mulσ{miss[0]}_e₄_{miss[1]}: MISSING — no such statement in the file")
    for extra in sorted(got - expected):
        fails.append(f"mulσ{extra[0]}_e₄_{extra[1]}: unexpected (i, j) outside the 3 × 24 grid")
    return checked, fails


# --------------------------------------------------------------------------
def main() -> int:
    rung, laws = RUNG.read_text(), LAWS.read_text()
    gens = [parse_mul_sigma(rung, i) for i in range(3)]
    trm4 = parse_trm4(rung)
    words = parse_word_actions(laws)
    print(f"[1] parsed 3 generator actions + TRM4 + {len(words)} words from the Lean sources")

    pres_fails = check_presentation(gens)
    print(f"[2] Hecke presentation re-derived: {'OK' if not pres_fails else pres_fails}")

    n_cyc, cyc_fails = check_cyclicity(words, gens, trm4)
    print(f"[3] cyclicity identities checked: {n_cyc}  failures: {len(cyc_fails)}")

    n_edges, tree_fails = check_word_tree(words, gens)
    print(f"[4] word-tree edges checked: {n_edges}  failures: {len(tree_fails)}")

    n_lean, lean_fails = check_lean_generator_action(gens)
    print(f"[5] committed Lean statements re-checked: {n_lean}  failures: {len(lean_fails)}")

    all_fails = pres_fails + cyc_fails + tree_fails + lean_fails
    ok = not all_fails
    # The canonical experimental (proton) pin, read live — never transcribed.
    # Nothing below is evaluated at it; it is recorded so the witness declares
    # which layer it belongs to (owner directive 2026-08-07).
    try:
        import qou_substrate.witness as _qw

        q0_value = _qw._q0_value_for_anchor("proton")
    except Exception:  # noqa: BLE001
        q0_value = None

    witness = {
        "schema": "witness/v1",
        "q0Anchor": "proton",
        "q0Value": q0_value,
        "q0Note": (
            "Recorded for layer identification only. This computation is exact in "
            "symbolic z and h and is evaluated at no substrate pin, so no result "
            "here depends on this value."
        ),
        "description": (
            "Independent symbolic re-derivation of the H4 generator-route cyclicity "
            "content: the 72 atomic identities tr(sigma_i . b_j) = tr(b_j . sigma_i), "
            "the word-tree single-term edge property the induction rests on, and a "
            "re-check of the committed H4GeneratorAction statements against the "
            "generator-action tables parsed out of the Lean sources."
        ),
        "computation": {
            "script": "computations/h4_cyclicity_generator_route_check.py",
            "sources_read": [
                "folio/quantum-observable-universe/lean/QOU/Machinery/HeckeH4StabilizationRung.lean",
                "folio/quantum-observable-universe/lean/QOU/Machinery/HeckeH4AlgebraLaws.lean",
                "folio/quantum-observable-universe/lean/QOU/Machinery/H4GeneratorAction.lean",
            ],
            "arithmetic": "exact (sympy over Q[z,h]); no floats, no substrate anchor",
        },
        "results": {
            "hecke_presentation_rederived": not pres_fails,
            "cyclicity_identities_checked": n_cyc,
            "word_tree_edges_checked": n_edges,
            "lean_generator_statements_rechecked": n_lean,
            "failures": all_fails,
            "all_ok": ok,
        },
        "scope": (
            "Every statement checked here is already machine-checked by Lean, so "
            "this cannot make the theorem more true. It checks the layer Lean "
            "cannot see: that the committed statements are about the tables the "
            "modules claim to be about, computed by an independent implementation."
        ),
    }
    out = Path(__file__).with_name("h4-cyclicity-generator-route-check.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"[6] wrote {out.name}  all_ok={ok}")
    if all_fails:
        for f in all_fails[:20]:
            print(f"    FAIL {f}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
