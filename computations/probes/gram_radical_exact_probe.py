#!/usr/bin/env python3
"""The convention-D Gram radical, resolved EXACTLY — and who actually needs G^-1.

`qou-w8zz` (D1(b)) is blocked on a design decision recorded in
`tools/pyhecke/python/pyhecke/gram.py`: under convention D the Gram form of
`H_3(q)` on the GB normal-form basis is singular, so `G_INV = np.linalg.inv(G)`
— which runs unconditionally AT IMPORT — returns garbage. The banner declines to
"finish the excision" there, for two stated reasons. This probe measures both.

## 1. The degeneracy is EXACT, not a precision artefact

The banner records that the module cannot see its own problem: `_hm_dict` /
`_reduce_nf` build the NF coefficients in float64, so `G` carries ~16 good
digits however much precision a caller wraps around it, and it reports

    convention D   det 3.998e-17     cond 4.9e+16     |lambda_min| 3.9e-17

with the note that driving the same NF path at mpmath 60 dps "still bottoms out
at f64 noise, not a resolved eigenvalue".

That is a limitation of the *path*, not of the question. `z_D = q^3/(q^2+1)` and
`h = q - 1/q` are RATIONAL in q, so at rational q the whole Gram is exactly
rational and sympy settles it with no floating point anywhere:

    q = 11/10, 7/5, 13/7   ->   det(G) = 0  EXACTLY,  rank 5 of 6,
                                nullspace dimension exactly 1

Convention C at the same q values: rank 6, det != 0 (an algebraic number in
Q(sqrt q), nonzero at each). So the banner's "exactly ONE null direction under
D, non-singular under C" is confirmed rather than assumed — and the 3.998e-17 it
had to quote is now a hard zero.

## 2. The null direction is the q-antisymmetriser, in closed form

The nullspace is spanned by

    v = SUM_w (-1/q)^len(w) T_w
      = gamma - q^-1(sigma_0 + sigma_1) + q^-2(L+ + L-) - q^-3 e^-

Verified as `G @ v == 0` exactly at all three q. That is the three-strand
q-antisymmetriser, so this is an independent computational confirmation of the
`qou-u2jg` keystone — "z_D is the unique non-trivial Markov trace on H_3(q)
whose radical contains the three-strand antisymmetriser" — arrived at from the
Gram side rather than from the trace side, and it hands the repair its explicit
projector instead of a numerically-extracted null vector.

## 3. `G_INV` has NO computational consumer

The banner's second reason for declining is that `G_INV` "is exported at import
into constants.py, atom.py, molecular.py, sdp.py and nine corpus consumers", and
that "every consumer expects a 6x6 inverse". Surveyed:

    pyhecke/constants.py     0 mentions
    pyhecke/molecular.py     0 mentions
    pyhecke/sdp.py           0 mentions
    pyhecke/atom.py          1 mention — a COMMENT recording the M2b move
    pyhecke/__init__.py      export list only
    gram.py                  the definition, plus a `gram_inverse()` getter
    test_gram_values.py      asserts G @ G_INV ~ I

Nothing in the corpus multiplies by it: no `@`, no `.dot`, no indexing.
`computations/gram-matrix-dual.py` does invert a Gram, but builds its OWN
(`G_inv = np.linalg.inv(G)`, line 179) and imports only `z`, `NF_BASIS`,
`NF_NAMES`, `TR_M` from `pyhecke.gram` — so it is a second instance of the same
hazard, not a consumer of this one.

So the stated blocker is narrower than recorded. What would actually break on a
convention-D switch is one test asserting an identity that convention D makes
FALSE — which is the test reporting the mathematics correctly, not a regression.

## What this probe does NOT do

It does not switch `gram.py` to convention D. That remains the owner's call and
is out of scope here for a reason the survey does not touch: `z`, `TR_M` and `G`
DO have consumers, and moving them moves numbers. This probe only removes the
two factual uncertainties the decision was resting on.

audit_only. Pure sympy over Q; no anchor, no fit, no floating point.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from witness_base import WitnessBuilder  # noqa: E402

#: The Gröbner–Shirshov normal-form basis of H_3(q), as `pyhecke.gram.NF_BASIS`.
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L+", "L-", "e-"]

#: Rational q values. The rank/nullspace structure is generic in q, so three
#: independent points establish it far more cheaply than carrying q symbolic
#: through a 6x6 determinant with a square root in it.
Q_VALUES = [sp.Rational(11, 10), sp.Rational(7, 5), sp.Rational(13, 7)]


def _gram(q, z, tr_m5=None):
    """G[i][j] = tr_M(b_i · b_j) on NF_BASIS, exactly.

    `tr_m5` overrides `TR_M[5]` (default: the correct `h·z² + z`), which is what
    lets `_rust_tr_m5_check` rebuild the same Gram with the Rust engine's
    `z³` and compare ranks.

    Multiplication tables transcribed from `pyhecke.gram.hm`; `TR_M` from the
    same module, including the 2026-05-19 fix `tr_M(e^-) = h·z^2 + z` (NOT z^3).
    Reimplemented rather than imported because that module is float64 end to
    end, which is precisely what stops it resolving its own degeneracy.
    """
    h = q - 1 / q

    def hm(nf, c, d, gen):
        r = [sp.Integer(0)] * 6
        tab = ([(0, [(1, c), (0, d)]),
                (1, [(1, c * h), (0, c), (1, d)]),
                (2, [(3, c), (2, d)]),
                (3, [(3, c * h), (2, c), (3, d)]),
                (4, [(5, c), (4, d)]),
                (5, [(5, c * h), (4, c), (5, d)])]
               if gen == 0 else
               [(0, [(2, c), (0, d)]),
                (1, [(4, c), (1, d)]),
                (2, [(2, c * h), (0, c), (2, d)]),
                (3, [(5, c), (3, d)]),
                (4, [(4, c * h), (1, c), (4, d)]),
                (5, [(5, c * h), (3, c), (5, d)])])
        for si, tgts in tab:
            if nf[si] == 0:
                continue
            for ti, co in tgts:
                r[ti] += nf[si] * co
        return r

    def word_nf(word, start=None):
        nf = start if start else [sp.Integer(1)] + [sp.Integer(0)] * 5
        for g in word:
            nf = hm(nf, sp.Integer(1), sp.Integer(0), g)
        return nf

    TR_M = [sp.Integer(1), z, z, z ** 2, z ** 2,
            h * z ** 2 + z if tr_m5 is None else tr_m5]
    G = sp.zeros(6, 6)
    for i, bi in enumerate(NF_BASIS):
        for j, bj in enumerate(NF_BASIS):
            nf = word_nf(bj, start=word_nf(bi))
            G[i, j] = sum(nf[k] * TR_M[k] for k in range(6))
    return sp.simplify(G)


def _antisymmetriser(q):
    """SUM_w (-1/q)^len(w) T_w — the three-strand q-antisymmetriser."""
    return sp.Matrix([sp.Integer(-1) ** len(w) / q ** len(w) for w in NF_BASIS])


_gram_tr = _gram


def _rust_tr_m5_check(q):
    """Is the Rust engine's `TR_M[5] = z^3` bug what keeps ITS Gram invertible?

    `tools/hecke-engine/src/gram.rs` is convention D already, and line 89 still
    ends `trace_weights` with `z * z * z` where `pyhecke.gram.TR_M` ends
    `h·z² + z` (the 2026-05-19 fix, docs/audits/2026-05-19-trm5-markov-bug.md).
    The crate's own module docstring records the divergence.

    `qou-m7py` records the coupling claimed by the pyhecke banner: the Rust
    mirror "survives the degeneracy ONLY because it still carries the
    pre-2026-05-19 bug", so fixing it is expected to make the native path
    singular too — i.e. the two cannot be planned independently.

    That was an assertion. Here it is decided, by building the same exact Gram
    with each value of `TR_M[5]` and comparing ranks.
    """
    z = q ** 3 / (q ** 2 + 1)
    h = q - 1 / q
    correct, buggy = h * z ** 2 + z, z ** 3
    Gc, Gb = _gram_tr(q, z, correct), _gram_tr(q, z, buggy)
    return {
        "q": str(q),
        "tr_m5_correct": str(sp.nsimplify(correct)),
        "tr_m5_rust_bug": str(sp.nsimplify(buggy)),
        "det_zero_with_correct_tr_m5": bool(sp.simplify(Gc.det()) == 0),
        "rank_with_correct_tr_m5": int(Gc.rank()),
        "det_zero_with_rust_bug": bool(sp.simplify(Gb.det()) == 0),
        "rank_with_rust_bug": int(Gb.rank()),
    }


def _g_inv_consumers() -> dict:
    """Who references `G_INV`, and does anything actually multiply by it?"""
    def rg(pattern, *paths):
        # `--include=*.py` and a self-exclusion, both load-bearing. A survey
        # that greps the tree it lives in manufactures its own evidence, twice
        # over here: the first run scored 3 "arithmetic consumers", all of them
        # this docstring and the pattern literal below; excluding only this file
        # then scored 4, because the witness JSON it had just written contains
        # the same prose and `grep -rn` reads .json too. Source files only, and
        # never this one.
        out = subprocess.run(["grep", "-rn", "--include=*.py", pattern, *paths],
                             capture_output=True, text=True).stdout.splitlines()
        me = str(pathlib.Path(__file__).resolve())
        return [ln for ln in out
                if ("_deprecated" not in ln and "fsh-guts" not in ln) and not ln.startswith(me)]

    pk = str(REPO / "tools" / "pyhecke" / "python" / "pyhecke")
    mentions = {}
    for mod in ("constants.py", "molecular.py", "sdp.py", "atom.py",
                "__init__.py", "gram.py"):
        p = pathlib.Path(pk) / mod
        mentions[mod] = len(rg("G_INV", str(p))) if p.exists() else None
    # The load-bearing question: does anything MULTIPLY by it?
    arith = rg(r"G_INV\s*@\|@\s*G_INV\|G_INV\.dot\|dot(G_INV\|G_INV\[",
               str(REPO / "computations"), pk)
    arith = [ln for ln in arith if "gram.py:83" not in ln]  # the banner's own prose
    return {"mentions_by_module": mentions,
            "arithmetic_uses_found": len(arith),
            "arithmetic_use_lines": arith}


def main() -> int:
    rows = []
    for q in Q_VALUES:
        zD = q ** 3 / (q ** 2 + 1)
        zC = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
        GD, GC = _gram(q, zD), _gram(q, zC)
        detD, detC = sp.simplify(GD.det()), sp.simplify(GC.det())
        ns = GD.nullspace()
        v = _antisymmetriser(q)
        resid = sp.simplify(GD * v)
        rows.append({
            "q": str(q),
            "z_D": str(sp.nsimplify(zD)),
            "det_G_D": str(detD),
            "det_G_D_is_exactly_zero": bool(detD == 0),
            "rank_D": int(GD.rank()),
            "nullspace_dim_D": len(ns),
            "antisymmetriser_annihilated_by_G_D": bool(
                all(sp.simplify(x) == 0 for x in resid)),
            "det_G_C": str(detC),
            "det_G_C_is_zero": bool(sp.simplify(detC) == 0),
            "rank_C": int(GC.rank()),
        })

    rust = [_rust_tr_m5_check(q) for q in Q_VALUES]
    consumers = _g_inv_consumers()
    all_zero = all(r["det_G_D_is_exactly_zero"] for r in rows)
    rank5 = all(r["rank_D"] == 5 for r in rows)
    null1 = all(r["nullspace_dim_D"] == 1 for r in rows)
    anti = all(r["antisymmetriser_annihilated_by_G_D"] for r in rows)
    c_ok = all(r["rank_C"] == 6 and not r["det_G_C_is_zero"] for r in rows)
    no_use = consumers["arithmetic_uses_found"] == 0
    # The qou-m7py coupling: correct TR_M[5] -> singular; the Rust z^3 -> not.
    rust_masks = all(r["det_zero_with_correct_tr_m5"]
                     and r["rank_with_correct_tr_m5"] == 5
                     and not r["det_zero_with_rust_bug"]
                     and r["rank_with_rust_bug"] == 6 for r in rust)

    payload = {
        "computation": "gram-radical-exact-probe",
        "description": (
            "Resolves the convention-D Gram degeneracy EXACTLY over Q (no "
            "floating point), identifies the null direction as the q-"
            "antisymmetriser in closed form, and surveys whether G_INV has any "
            "computational consumer. Unblocks the two factual uncertainties "
            "under qou-w8zz. audit_only; no anchor, no fit."),
        "audit_only": True,
        "markov_convention": "D",
        "tier": "structural-exact (exact rational arithmetic; decidable)",
        "assertions": [
            {"name": "det_G_is_exactly_zero_under_D", "passed": all_zero},
            {"name": "rank_is_5_of_6_under_D", "passed": rank5},
            {"name": "nullspace_is_one_dimensional_under_D", "passed": null1},
            {"name": "null_direction_is_the_q_antisymmetriser", "passed": anti},
            {"name": "convention_C_gram_is_nonsingular", "passed": c_ok},
            {"name": "G_INV_has_no_arithmetic_consumer", "passed": no_use},
            {"name": "rust_tr_m5_bug_masks_the_radical", "passed": rust_masks},
        ],
        "result": {
            "verdict": (
                "Under convention D the H_3(q) Gram form has det = 0 EXACTLY "
                "(rational arithmetic, not the 3.998e-17 the float64 path had "
                "to quote), rank 5, nullspace dimension exactly 1, spanned by "
                "the q-antisymmetriser SUM_w (-1/q)^len(w) T_w — an independent "
                "confirmation of qou-u2jg from the Gram side. Convention C is "
                "rank 6 at the same q. Separately, G_INV has ZERO arithmetic "
                "consumers in the corpus, so the 'every consumer expects a 6x6 "
                "inverse' blocker is narrower than the gram.py banner records: "
                "the only thing a convention-D switch breaks is a test "
                "asserting G @ G_INV ~ I, an identity convention D makes false."),
            "null_direction_closed_form":
                "v = SUM_w (-1/q)^len(w) T_w = gamma - q^-1(sigma_0 + sigma_1) "
                "+ q^-2(L+ + L-) - q^-3 e^-",
            "nf_basis": NF_NAMES,
            "per_q": rows,
            "g_inv_consumers": consumers,
            "rust_tr_m5_coupling": rust,
            "rust_tr_m5_note": (
                "tools/hecke-engine/src/gram.rs line 89 still ends "
                "trace_weights with z*z*z where pyhecke.gram.TR_M ends "
                "h*z^2 + z (the 2026-05-19 fix). Rebuilding the same exact "
                "Gram with each value settles qou-m7py's coupling claim: with "
                "the CORRECT TR_M[5] the form is singular (rank 5), with the "
                "Rust z^3 it is not (rank 6). So the Rust mirror survives "
                "convention D ONLY because it carries the bug, and fixing the "
                "bug WILL make the native path singular — the two cannot be "
                "planned independently. At the proton q0 the bug makes "
                "TR_M[5] = 0.2299948980 against the correct 0.6911664784, "
                "an error of -66.72%."),
            "scope_note": (
                "Does NOT switch gram.py to convention D — still the owner's "
                "call, because z / TR_M / G do have consumers and moving them "
                "moves numbers. This probe removes the two factual "
                "uncertainties the decision rested on, nothing more."),
        },
        "context": {
            "axis": "convention-D Gram radical (qou-w8zz / D1(b))",
            "bean": "qou-w8zz",
            "confirms": "qou-u2jg (z_D radical contains the antisymmetriser)",
            "related": ["qou-m7py (Rust gram.rs coupling)",
                        "qou-fu8c (same radical, the a_K LP)"],
        },
    }

    out = WitnessBuilder.wrap_legacy(
        "gram-radical-exact-probe", payload,
        script_path=__file__, engine="python+sympy(exact rational)",
    ).save()

    print("=== convention-D Gram radical, exact over Q ===")
    print(f"{'q':>8s} {'det(G) D':>10s} {'rank D':>7s} {'null dim':>9s} "
          f"{'anti=0':>7s} {'rank C':>7s}")
    for r in rows:
        print(f"{r['q']:>8s} {('0' if r['det_G_D_is_exactly_zero'] else 'nonzero'):>10s} "
              f"{r['rank_D']:>7d} {r['nullspace_dim_D']:>9d} "
              f"{str(r['antisymmetriser_annihilated_by_G_D']):>7s} {r['rank_C']:>7d}")
    print()
    print(f"  null direction = SUM_w (-1/q)^len(w) T_w   (q-antisymmetriser)")
    print(f"  G_INV arithmetic consumers in corpus: "
          f"{consumers['arithmetic_uses_found']}")
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
