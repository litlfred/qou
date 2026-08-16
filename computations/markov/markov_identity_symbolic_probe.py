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

#: n = 6 (A = 2). The deuteron is the smallest atom that HAS a p-n interface,
#: so it is the smallest word whose χ the pinned-δ defect touched — and the
#: smallest non-trivial test of the identity that the normalisation result
#: does not already cover.
Z, N = 1, 1
N_STRANDS = 3 * (Z + N)


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


def main() -> int:
    # THE canonical symbol, imported rather than re-declared. A locally minted
    # `sp.Symbol("q", positive=True, real=True)` happens to compare equal to
    # this one, but nothing guarantees that and the failure it produces is
    # silent -- see `symbolic_y_lambda`'s note on the assumption-free `q` that
    # `sympify` mints.
    from hecke_symbolic import q  # noqa: E402

    from markov_peel import tr_M_atomic
    from mass_at_3A_proper import atom_braid_word_3A
    from hoefsmit_symbolic import chi_lambda_symbolic

    # ---- the peel side: exact rational function, no anchor -------------
    t0 = time.time()
    peel = sp.cancel(sp.together(tr_M_atomic(Z, N, use_fast=False)))
    t_peel = time.time() - t0
    peel_floats = len(peel.atoms(sp.Float))
    print(f"[peel] {t_peel:.1f}s   Float atoms={peel_floats}   "
          f"rational={peel.is_rational_function(q)}")

    # ---- the bridge side ----------------------------------------------
    # The SAME word the peel builds. `atom_braid_word_3A` returns (c, d, gen)
    # triples; the character path wants (gen, ctype), so classify each
    # crossing rather than re-deriving d.
    from canonical_braid_crossings import classify_crossing
    from q_parameter import Q_MP

    word = atom_braid_word_3A(Z, N)
    h_num = float(Q_MP - 1 / Q_MP)
    crossings = []
    for c, d, gen in ((t[0], t[1], t[2]) for t in word):
        ctype = classify_crossing(float(c), float(d), h_num,
                                  context="markov_identity_symbolic_probe")
        crossings.append((gen, ctype))
    ctypes_seen = sorted({ct for _, ct in crossings})
    print(f"[word] {len(crossings)} crossings, ctypes={ctypes_seen}")
    if "averaged_weighted" not in ctypes_seen:
        print("  ! no colour-weighted interface in this word — the probe "
              "would not exercise the fixed path; refusing to report a pass")
        return 2

    y = symbolic_y_lambda(N_STRANDS, q)
    # Route χ through the PRODUCER's cache rather than recomputing inline.
    # Two reasons, both learned the hard way on the first run:
    #   - it costs ~25 min at H_6 under the colour-weighted word (the symbolic
    #     δ makes entries far larger than the ~155 s the colour-blind estimate
    #     in that producer's docstring records), so an inline recompute makes
    #     every diagnostic re-run unaffordable and the result unrepeatable;
    #   - a second implementation of χ here is exactly the private-copy defect
    #     this whole arc keeps finding. The producer's loader is now
    #     convention-guarded, so reading it is safe in the way it was not
    #     before: a cache built for a different word is discarded, not served.
    t0 = time.time()
    from per_irrep_pole_deuteron_h6 import load_or_build_chi_deuteron
    chis, _ = load_or_build_chi_deuteron(q)
    total = sp.Integer(0)
    chi_floats = 0
    for lam in _partitions(N_STRANDS):
        chi = sp.cancel(chis[lam])
        chi_floats += len(chi.atoms(sp.Float))
        total += y[lam] * chi
    t_chi = time.time() - t0
    bridge = sp.cancel(sp.together(total))
    print(f"[bridge] {t_chi:.1f}s   Float atoms={len(bridge.atoms(sp.Float))}")

    # ---- the test ------------------------------------------------------
    residual = sp.cancel(sp.together(sp.expand(bridge - peel)))

    # GUARD: both sides must be expressions in ONE variable. Two means a
    # symbol-identity bug upstream (an assumption-free `q` from `sympify`
    # against `hecke_symbolic.q`), and the residual is then meaningless rather
    # than merely nonzero. Refuse to report a verdict instead of publishing an
    # artefact, which is exactly what the first run of this probe did.
    nfree = len(residual.free_symbols)
    if nfree > 1:
        print(f"\n  ! residual has {nfree} free symbols {residual.free_symbols} "
              f"— the two sides are not in the same variable. Refusing to "
              f"report an identity verdict.")
        return 2

    # `sp.simplify(r) == 0` is NOT a decision procedure and demonstrably fails
    # on these expressions. Use the degree bound: a nonzero rational p/s with
    # deg(p) = d has at most d roots, so vanishing at d+1 DISTINCT points
    # forces p == 0. Exact rationals throughout — no floating point, no appeal
    # to simplify.
    num, den = sp.fraction(residual)
    num = sp.expand(num)
    if num == 0:
        is_zero, method = True, "normalised-numerator"
    else:
        deg = int(sp.degree(num, q))
        pts, k = [], 2
        while len(pts) < deg + 1:
            c = sp.Rational(k, 7)
            if den.subs(q, c) != 0:
                pts.append(c)
            k += 1
        nonzero_at = [c for c in pts if sp.cancel(num.subs(q, c)) != 0]
        is_zero = not nonzero_at
        method = f"degree-bound (deg {deg}, {len(pts)} exact points)"
    print(f"\n[residual] identically zero: {is_zero}   via {method}")

    # DIAGNOSTICS, because "not identically zero" is not yet a finding.
    # A residual that is LARGE at q₀ means the two sides are different objects
    # -- a probe bug -- since bridge and peel are known to agree there to
    # ~1e-50 (atomic-tr-m-mpfr-50dps{,-proton}.witness.json). A residual that
    # VANISHES at q₀ and not elsewhere would be the real thing: an identity
    # that holds at the anchor but not as a function of q. Recording the
    # numbers is what separates those, and the first version of this probe
    # truncated the residual to 2000 chars and could answer neither.
    from mpmath import mp as _mp
    _mp.dps = 60
    probes = {
        "proton_q0": "1.1099785827513808075916690956",
        "muon_q0": "1.109978595557334719899763",
        "q_1_3": "1.3",
        "q_0_7": "0.7",
        "q_2": "2",
    }
    f_res = sp.lambdify(q, residual, "mpmath")
    f_peel = sp.lambdify(q, peel, "mpmath")
    evals = {}
    for name, qs in probes.items():
        qv = _mp.mpf(qs)
        try:
            rv, pv = f_res(qv), f_peel(qv)
            rel = abs(rv) / abs(pv) if pv != 0 else None
            evals[name] = {"q": qs, "residual": _mp.nstr(rv, 20),
                           "peel": _mp.nstr(pv, 20),
                           "relative": _mp.nstr(rel, 12) if rel is not None else None}
            print(f"  residual({name:10s}) = {_mp.nstr(rv, 14):>24}   "
                  f"rel {_mp.nstr(rel, 8) if rel is not None else '-'}")
        except Exception as exc:  # noqa: BLE001
            evals[name] = {"q": qs, "error": f"{type(exc).__name__}: {exc}"}
            print(f"  residual({name:10s}) FAILED {exc}")
    rnum, rden = sp.fraction(residual)
    deg_num = int(sp.degree(sp.expand(rnum), q))
    deg_den = int(sp.degree(sp.expand(rden), q))
    print(f"  residual degrees: num {deg_num} / den {deg_den}")

    witness = {
        "computation": "markov-identity-symbolic",
        "description": (
            "Tests Sum_lambda y_lambda(q)*chi^lambda(beta_D,q) = tr_M(beta_D)(q) "
            "as an identity of rational functions, with no q0 anywhere. Both "
            "sides are built from the same colour-weighted canonical word. "
            "Strictly stronger than the two settled facts it complements: the "
            "normalisation result evaluates at the identity braid, and the "
            "~1e-50 bridge-vs-peel agreements are two points of the q-line."
        ),
        "scriptFile": "markov/markov_identity_symbolic_probe.py",
        "q0Anchor": "independent",
        "q0_independence_note": (
            "No q0 is read. The peel's numeric (c,d) only select crossing "
            "templates; chi takes delta as the closed form flavor_split_leading(q). "
            "classify_crossing needs a numeric h to identify templates, which is "
            "a q-independent combinatorial choice, not a value entering the result."
        ),
        "atom": {"Z": Z, "N": N, "n_strands": N_STRANDS,
                 "n_crossings": len(crossings), "ctypes": ctypes_seen},
        "peel": {"float_atoms": peel_floats,
                 "rational_in_q": bool(peel.is_rational_function(q)),
                 "elapsed_sec": f"{t_peel:.2f}"},
        "bridge": {"float_atoms": len(bridge.atoms(sp.Float)),
                   "chi_float_atoms_total": chi_floats,
                   "elapsed_sec": f"{t_chi:.2f}"},
        "residual_is_identically_zero": bool(is_zero),
        "residual_degrees": {"numerator": deg_num, "denominator": deg_den},
        # The EVALUATIONS are the durable record, not the expression string.
        # A truncated `str(residual)[:2000]` is unparseable and cannot be
        # re-examined, which is how the first run produced a verdict nobody
        # could triage.
        "residual_evaluations": evals,
        "assertions": [
            {"name": "peel_is_float_free", "passed": peel_floats == 0},
            {"name": "chi_is_float_free_after_pr_5209", "passed": chi_floats == 0,
             "note": "before #5209 an averaged_weighted crossing carried a "
                     "q0-pinned delta, so chi was not a function of q at all"},
            {"name": "markov_identity_holds_identically_in_q",
             "passed": bool(is_zero)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy")
    out = REPO / "computations" / "markov-identity-symbolic.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nallPassed = {witness['allPassed']}  -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
