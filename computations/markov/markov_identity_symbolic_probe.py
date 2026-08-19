#!/usr/bin/env python3
"""
markov_identity_symbolic_probe.py — is `Σ_λ y_λ(q)·χ^λ(β) = tr_M(β)` an
identity in `q`, or only an agreement at the substrate anchor?

WHAT IS AND IS NOT ALREADY KNOWN.  Two weaker statements are settled:

  1. The weights are correctly Markov-normalised, symbolically:
     `Σ_{λ ⊢ n} y_λ(q)·dim V_λ = 1` exactly and identically in q, at every
     n from 2 to 6, and in Lean (`QOU/MathlibExt/MarkovNormalisation.lean`).
     That evaluates at the IDENTITY braid, where `χ^λ(1) = dim V_λ`.
  2. The full identity holds NUMERICALLY at both documented q₀ pins, to
     ~1e-50, on proton / neutron / deuteron / tritium / helium-3
     (`atomic-tr-m-mpfr-50dps{,-proton}.witness.json`, bridge vs peel).

Neither implies the general-β statement.  (1) is one point of the braid
group; (2) is two points of the q-line.  This probe tests the object both
of them leave alone: a NON-trivial braid, as a function of q.

WHY IT IS TESTABLE NOW.  Two things had to be true first, and the second was
false until PR #5209:

  - `markov_peel.tr_M_atomic` returns an exact integer-coefficient rational
    function of q -- no anchor enters it (the numeric `(c, d)` only *select*
    one of five crossing templates; the element carries the symbolic form).
    Bean `qou-8x1l` recorded the opposite as a blocking obstacle; that was
    refuted by `peel_anchor_identification_probe.py`.
  - `hecke_character_symbolic._q_character_compute` had to stop baking a
    q₀-pinned δ into `χ^λ` for any word with a p-n interface. It called
    `d_for_ctype(cross_d, h)` without the `delta=` override that function's
    own docstring reserves for q-symbolic callers, so an `averaged_weighted`
    crossing arrived as `-0.4996…*q + 0.4996…/q`. Fixed in #5209.

WHAT THIS PROBE DOES.  For the deuteron word β_D (A=2, n=6, the colour-
weighted canonical word `atom_braid_word_3A(1, 1)` -- the SAME call
`markov_peel` makes, so the two sides are the same object):

    residual(q) := Σ_{λ ⊢ 6} y_λ(q)·χ^λ(β_D, q)  −  tr_M_peel(β_D)(q)

and reduces it with `cancel`. The claim under test is `residual ≡ 0` as a
rational function -- no q₀ anywhere in the statement or the check.

A CACHE THAT LOOKS RIGHT AND IS NOT.  `computations/chi-deuteron-h6.witness.json`
holds symbolic `χ^λ(β_D)` for all 11 partitions of 6 and would save ~155 s.
It is tagged `convention: averaged-crossings` -- the colour-BLIND `−h/2`
interface -- while the peel builds the colour-WEIGHTED `−h(½ − δ/4)` word.
Pairing them is the same straddle class this arc is about, one level out
(crossing convention rather than anchor), so this probe recomputes χ rather
than reading that cache. Do not "optimise" it back in.

Run:
    python3 computations/markov/markov_identity_symbolic_probe.py
"""
from __future__ import annotations

import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import sympy as sp  # noqa: E402

#: Two atoms, deliberately, and the cheap one runs FIRST.
#:
#: `proton` (n = 3, 11 crossings) is the CONTROL. It costs seconds, and it is
#: what caught the symbol-identity bug that made the first deuteron run report
#: a false "not identically zero" after 25 minutes. A cheap case whose answer
#: is checkable is worth more than an expensive one you cannot triage — run it
#: before believing anything the expensive case says.
#:
#: `deuteron` (n = 6, 23 crossings) is the case that matters: the smallest atom
#: with a p-n interface, hence the smallest word whose χ the pinned-δ defect
#: touched, and the smallest test the normalisation result does not already
#: cover (that one evaluates at the identity braid).
ATOMS = [("proton", 1, 0), ("deuteron", 1, 1)]


def _partitions(n):
    """Partitions of n, each weakly decreasing, in reverse-lex order."""
    def rec(rem, cap):
        if rem == 0:
            yield ()
            return
        for part in range(min(rem, cap), 0, -1):
            for rest in rec(rem - part, part):
                yield (part,) + rest
    return list(rec(n, n))


def symbolic_y_lambda(n, q):
    """Convention-D `y_λ(q)` for λ ⊢ n, from the committed symbolic witness.

    Read rather than re-derived: this is the migrated convention-D root
    (`z = q³/(q²+1)`), and re-deriving it here would be a second
    implementation of the object under test.

    **`locals={"q": q}` is load-bearing.** `sp.sympify("q**2/(q**2+1)")` mints
    a BARE `Symbol("q")` carrying only `commutative=True`, while `markov_peel`
    and `chi_lambda_symbolic` both work in `hecke_symbolic.q`, which carries
    `positive`/`real`/`nonzero`/... . Sympy treats those as DIFFERENT
    variables, so `y[λ] * χ` silently became a product across two symbols and
    the residual could never cancel: 2 free symbols instead of 1, and a
    verdict of "not identically zero" that was pure artefact. Binding here is
    what makes the two sides expressions in one variable.

    This cost a full 25-minute n=6 run and a false negative that looked like a
    mathematical finding. The tell is cheap and worth keeping in mind:
    `len(residual.free_symbols)` must be 1 (or 0 when it vanishes), never 2.
    """
    doc = json.loads(
        (REPO / "computations"
         / "y-lambda-wenzl-bridge-symbolic-witness.json").read_text())
    table = doc["tables_by_n"][str(n)]["weights"]
    out = {}
    for row in table:
        # `partition` is serialised inconsistently in this witness — a JSON
        # string "[3, 2, 1]" for some n, a real list for others. Accept both
        # rather than assuming, since guessing wrong here fails loudly at
        # n=6 and SILENTLY (KeyError-free, wrong lookup) nowhere — but the
        # next reader deserves not to rediscover it.
        p = row["partition"]
        lam = tuple(json.loads(p) if isinstance(p, str) else p)
        out[lam] = sp.sympify(row["y_lambda_symbolic"], locals={"q": q})
    return out


def run_atom(name, Z, N, q):
    """Test the identity for one atom. Returns a result dict (never raises)."""
    from markov_peel import tr_M_atomic
    from canonical_braid_crossings import (
        atom_canonical_crossings, convention_label,
    )
    from hoefsmit_symbolic import chi_lambda_symbolic
    from mpmath import mp as _mp
    _mp.dps = 60

    n = 3 * (Z + N)
    crossings = atom_canonical_crossings(Z, N)
    ctypes_seen = sorted({ct for _, ct in crossings})
    print(f"\n=== {name}  (Z={Z}, N={N}, H_{n}, {len(crossings)} crossings)")
    print(f"  convention: {convention_label(crossings)}  ctypes={ctypes_seen}")

    t0 = time.time()
    peel = sp.cancel(sp.together(tr_M_atomic(Z, N, use_fast=False)))
    t_peel = time.time() - t0
    peel_floats = len(peel.atoms(sp.Float))
    print(f"  [peel]   {t_peel:6.1f}s  Float atoms={peel_floats}  "
          f"rational={peel.is_rational_function(q)}")

    y = symbolic_y_lambda(n, q)
    t0 = time.time()
    total, chi_floats = sp.Integer(0), 0
    for lam in _partitions(n):
        chi = sp.cancel(chi_lambda_symbolic(lam, crossings))
        chi_floats += len(chi.atoms(sp.Float))
        total += y[lam] * chi
    t_chi = time.time() - t0
    bridge = sp.cancel(sp.together(total))
    print(f"  [bridge] {t_chi:6.1f}s  Float atoms={len(bridge.atoms(sp.Float))}")

    residual = sp.cancel(sp.together(sp.expand(bridge - peel)))

    # GUARD: one variable, or the verdict is meaningless rather than merely
    # negative. Two symbols named `q` -- an assumption-free one from `sympify`
    # against `hecke_symbolic.q` -- is what made the first n=6 run report a
    # false "not identically zero" after 25 minutes.
    nfree = len(residual.free_symbols)
    if nfree > 1:
        print(f"  ! residual has {nfree} free symbols {residual.free_symbols} — "
              f"the sides are not in one variable; refusing a verdict")
        return {"atom": name, "error": "multiple free symbols",
                "free_symbols": sorted(str(s) for s in residual.free_symbols)}

    # `simplify(r) == 0` is not a decision procedure and failed here even once
    # the symbols agreed. Degree bound instead: a nonzero rational p/s with
    # deg(p) = d has at most d roots, so vanishing at d+1 distinct EXACT
    # rational points forces p == 0.
    num, den = sp.fraction(residual)
    num = sp.expand(num)
    if num == 0:
        is_zero, method, deg = True, "normalised-numerator", 0
    else:
        deg = int(sp.degree(num, q))
        pts, k = [], 2
        while len(pts) < deg + 1:
            c = sp.Rational(k, 7)
            if den.subs(q, c) != 0:
                pts.append(c)
            k += 1
        is_zero = not [c for c in pts if sp.cancel(num.subs(q, c)) != 0]
        method = f"degree-bound (deg {deg}, {len(pts)} exact points)"
    print(f"  [residual] identically zero: {is_zero}   via {method}")

    evals = {}
    f_res = sp.lambdify(q, residual, "mpmath")
    f_peel = sp.lambdify(q, peel, "mpmath")
    for lbl, qs in (("proton_q0", "1.1099785827513808075916690956"),
                    ("muon_q0", "1.109978595557334719899763"),
                    ("q_1_3", "1.3"), ("q_0_7", "0.7"), ("q_2", "2")):
        try:
            qv = _mp.mpf(qs)
            rv, pv = f_res(qv), f_peel(qv)
            rel = abs(rv) / abs(pv) if pv != 0 else None
            evals[lbl] = {"q": qs, "residual": _mp.nstr(rv, 20),
                          "peel": _mp.nstr(pv, 20),
                          "relative": _mp.nstr(rel, 12) if rel is not None else None}
        except Exception as exc:  # noqa: BLE001
            evals[lbl] = {"q": qs, "error": f"{type(exc).__name__}: {exc}"}
    return {
        "atom": name, "Z": Z, "N": N, "n_strands": n,
        "n_crossings": len(crossings), "ctypes": ctypes_seen,
        "convention": convention_label(crossings),
        "peel": {"float_atoms": peel_floats, "elapsed_sec": f"{t_peel:.2f}",
                 "rational_in_q": bool(peel.is_rational_function(q))},
        "bridge": {"float_atoms": len(bridge.atoms(sp.Float)),
                   "chi_float_atoms_total": chi_floats,
                   "elapsed_sec": f"{t_chi:.2f}"},
        "identically_zero": bool(is_zero), "zero_test_method": method,
        "residual_numerator_degree": deg,
        "residual_evaluations": evals,
    }


def main() -> int:
    # THE canonical symbol, imported not re-declared -- see symbolic_y_lambda.
    from hecke_symbolic import q  # noqa: E402

    results = []
    for name, Z, N in ATOMS:
        try:
            results.append(run_atom(name, Z, N, q))
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {name} FAILED: {type(exc).__name__}: {exc}")
            results.append({"atom": name, "Z": Z, "N": N,
                            "error": f"{type(exc).__name__}: {exc}"})

    ok = [r for r in results if r.get("identically_zero")]
    witness = {
        "computation": "markov-identity-symbolic",
        "description": (
            "Tests Sum_lambda y_lambda(q)*chi^lambda(beta) = tr_M(beta) as an "
            "identity of RATIONAL FUNCTIONS -- no q0 in the statement or the "
            "check. Strictly stronger than the two facts it complements: the "
            "normalisation result Sum y_lambda*dim V_lambda = 1 evaluates at "
            "the IDENTITY braid, and the ~1e-50 bridge-vs-peel agreements are "
            "two points of the q-line. Both sides are built from the same "
            "colour-weighted canonical word, so the comparison is of one "
            "object rather than two conventions."
        ),
        "scriptFile": "markov/markov_identity_symbolic_probe.py",
        "q0Anchor": "independent",
        # Field renamed from `q0_independence_note` to the canonical
        # `q0AnchorReason` (bean qou-mw1p). The prose below was already
        # exactly right — this producer independently reached the same
        # token-plus-reason design — but under a name the audit does not
        # read, so `q0_anchor_consistency_audit` scored it
        # Q0_INDEPENDENT_NO_REASON despite the reason being present.
        "q0AnchorReason": (
            "No pin governs the result: the identity is checked SYMBOLICALLY, "
            "as an equality of rational functions in q, and the sole assertion "
            "reads only that symbolic check. The peel's numeric (c, d) only "
            "SELECT one of five crossing templates -- a q-independent "
            "combinatorial choice -- and chi takes delta as the closed form "
            "flavor_split_leading(q). Both substrate values DO appear in the "
            "source, as two of the five sample points in "
            "`residual_evaluations` (beside q = 1.3, 0.7, 2); they are "
            "reported, not depended on. Said explicitly because the earlier "
            "wording here was 'No q0 is read', which a reader grepping for "
            "1.1099 would find flatly contradicted by the file."
        ),
        "results": results,
        "assertions": [
            {"name": "identity_holds_identically_in_q_for_every_atom_tested",
             "passed": len(ok) == len(results) and bool(results)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy")
    out = REPO / "computations" / "markov-identity-symbolic.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n{len(ok)}/{len(results)} atoms: identity holds identically in q"
          f"   -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
