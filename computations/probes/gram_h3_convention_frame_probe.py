#!/usr/bin/env python3
"""The H_3(q) symbolic Gram is convention-C — and convention D is a ROOT of its
determinant, so the block's headline theorem is FALSE in the canonical frame.

`prop:gram-matrix-h3-symbolic` carries a witness assertion
`gram_h3_symbolic_matches_pyhecke` that has been red at `0.17218519049094…`
against a `1e-14` tolerance. Read as written, that assertion says the Lean
`gramEntry` closed forms have DRIFTED from the production `pyhecke` Gram. They
have not: both sides are internally exact and mutually consistent. The number
is the **convention gap**, and nothing else.

## What this probe establishes, exactly

Everything below is symbolic over `Q(q, z)` — the Markov weight `z` is carried
as a free symbol rather than substituted, which is what makes the conclusion an
identity in `q` instead of a numerical coincidence at `q_0`.

1. **The generic Gram.** `G[i][j] = tr_M(b_i · b_j)` on the Gröbner-Shirshov
   normal-form basis, with `TR_M = [1, z, z, z², z², h·z² + z]`, `h = q - 1/q`.

2. **CHECK 1 — the Lean file is convention C, exactly.** All 21 upper-triangle
   `gramEntry` definitions in `GramMatrixH3Symbolic.lean` equal `G(q, z)` at
   `z = z_C = √q/(q+1)`, entry for entry, with exact-zero difference. The Lean
   mathematics is *right*; it is right about C.

3. **CHECK 2 — the reference witness is convention D, exactly.** `G(q, z_D)` at
   `z_D = q³/(q²+1)` reproduces all 36 entries of `gram-matrix-dual.witness.json`
   to `2.3e-16`, i.e. to the float64 floor of the strings that witness stores.

4. **CHECK 3 — the failing number IS the gap.** `max |G(q₀,z_C) − G(q₀,z_D)|`
   reproduces the red assertion's `computed` field to every digit it records.

5. **CHECK 4 — the determinant, factored over Q(q, z):**

       det G(q,z) = −(z − q)⁵ (qz + 1)⁵ ((q²+1)z − q³) (q³z + qz + 1) / q⁸

   The third factor is `(q²+1)z − q³`. It vanishes **identically in q** exactly
   when `z = q³/(q²+1)` — which is convention D. So D is not merely a frame in
   which the Gram happens to be singular at the substrate anchor: **D is a root
   of the H_3 Gram determinant as a polynomial in z.** `det G(q, z_D) ≡ 0`, rank
   5, nullspace dimension 1, spanned by `(−q³, q², q², −q, −q, 1)` — which is
   `−q³ · Σ_w (−1/q)^len(w) T_w`, the three-strand q-antisymmetriser.

6. **CHECK 5 — cross-validation against a sorry-free Lean theorem.** Specialised
   to C and rewritten in `u = √q`, the determinant above reproduces
   `QOU.Interactions.GramMatrixH3Symbolic.gram_det_eq` factor for factor. That
   theorem is proved in Lean by a `det_fin_six` expansion, independently of this
   derivation, so it is a third-party check on the whole chain.

## Consequence for the content block (scope (b), structural)

Per AGENTS.md §"Before declaring 'refuted'": this is a **scope-(b) structural
exclusion**, and the invariant it cites is CHECK 4 — an exact polynomial
identity, not a numerical probe. Under the canonical convention D:

- `gramMatrix_det_ne_zero` is **false**, not unproved. It is a true theorem
  about convention C, and C was excised on 2026-08-09 / re-affirmed 2026-08-15.
- The positive-definiteness reading in the block's author notes is false twice
  over: the D-frame Gram is singular, and its spectrum at `q₀` carries a
  negative eigenvalue (`−0.7527…` in the reference witness), so it is
  **indefinite**, not merely semi-definite.
- The block's remaining Lean content survives the frame change: `isSymm` and
  `top_left = 1` hold for every `z`, as CHECK 6 records.

None of this is a defect in the Lean proofs. It is the ordinary consequence of
an owner ruling landing after the file was written, and the file never having
carried a convention label to make that visible.

## What is new here, and what is confirmation

The singularity itself is **already in the corpus**:
`computations/probes/gram_radical_exact_probe.py` established it exactly over ℚ
at three rational `q`, and `qou-u2jg` states the keystone from the trace side.
This probe adds three things that were not recorded: that the singularity is a
**determinant factor** (hence an identity in `q`, and hence D is *the* root
rather than *a* frame where it vanishes); that `prop:gram-matrix-h3-symbolic`
and its Lean file are C-frame casualties, which no bean or audit had connected;
and that the block's red assertion has been measuring the convention gap rather
than drift since the reference witness moved to D on 2026-08-15.

Exact arithmetic throughout (sympy over ℚ(q,z)); the only numeric step is the
comparison against the reference witness, which is mpmath at 60 dps because the
witness stores float64-rounded decimal strings.
"""

from __future__ import annotations

import json
import pathlib
import sys

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

#: Gröbner–Shirshov normal-form basis of H_3(q), as `pyhecke.gram.NF_BASIS`.
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L+", "L-", "e-"]

q = sp.Symbol("q", positive=True)
z = sp.Symbol("z")
u = sp.Symbol("u", positive=True)
h = q - 1 / q

#: Markov–Ocneanu–Wenzl trace on the NF basis, with `z` free.
#: `TR_M[5] = h·z² + z` is the 2026-05-19 fix (NOT `z³`); see
#: docs/audits/2026-05-19-trm5-markov-bug.md.
TR_M = [sp.Integer(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]

Z_C = sp.sqrt(q) / (q + 1)      # convention C (excised 2026-08-09 / re-affirmed 2026-08-15)
Z_D = q ** 3 / (q ** 2 + 1)     # convention D (canonical, owner ruling 2026-08-15)


def reduce_nf(terms: dict) -> dict:
    """Reduce a `word -> coeff` dict to the 6-element NF basis, exactly.

    Two rewrite rules, applied to fixpoint: the Hecke relation
    `σ_i² = h·σ_i + 1`, and the braid relation `aba -> bab` oriented by the
    Gröbner–Shirshov order (so `σ_1σ_0σ_1 -> σ_0σ_1σ_0`). Coefficients are
    sympy expressions in `q` and `z`; no floating point and no tolerance
    threshold, so the `abs(c) > 1e-15` pruning that the float64 implementations
    in `gram-matrix-dual.py` / `pyhecke.gram` need has no analogue here.
    """
    changed = True
    while changed:
        changed = False
        out: dict = {}
        for word, c in terms.items():
            if c == 0:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    pre, suf = word[:p], word[p + 2:]
                    w1, w2 = pre + (word[p],) + suf, pre + suf
                    out[w1] = out.get(w1, 0) + c * h
                    out[w2] = out.get(w2, 0) + c
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, cc = word[p], word[p + 1], word[p + 2]
                if a == cc and abs(a - b) == 1 and (b, a, b) < (a, b, a):
                    nw = word[:p] + (b, a, b) + word[p + 3:]
                    out[nw] = out.get(nw, 0) + c
                    done = changed = True
                    break
            if not done:
                out[word] = out.get(word, 0) + c
        terms = {w: sp.expand(v) for w, v in out.items() if sp.simplify(v) != 0}
    return terms


def gram_generic() -> list:
    """`G[i][j] = tr_M(b_i · b_j)` as exact expressions in `q` and `z`."""
    G = [[None] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            reduced = reduce_nf({NF_BASIS[i] + NF_BASIS[j]: sp.Integer(1)})
            tot = sum(c * TR_M[NF_BASIS.index(w)] for w, c in reduced.items())
            G[i][j] = sp.factor(sp.simplify(sp.expand(tot)))
    return G


def lean_entry(i: int, j: int):
    """The 21 `gramEntry` closed forms transcribed from
    `QOU/Interactions/GramMatrixH3Symbolic.lean` (in `u = √q`)."""
    if i > j:
        i, j = j, i
    table = {
        (0, 0): sp.Integer(1),
        (0, 1): u / (u ** 2 + 1),
        (0, 3): u ** 2 / (u ** 2 + 1) ** 2,
        (0, 5): (u ** 2 + u - 1) / (u ** 2 + 1),
        (1, 1): (u ** 2 + u - 1) / u,
        (1, 3): (u ** 2 + u - 1) / (u ** 2 + 1),
        (1, 5): (u ** 4 + u - 1) * (u ** 4 + u ** 3 - 1) / (u ** 2 * (u ** 2 + 1) ** 2),
        (3, 4): (u ** 2 + u - 1) ** 2 / u ** 2,
        (3, 5): (u ** 10 + u ** 9 - u ** 8 - u ** 5 + u ** 2 + u - 1) / (u ** 4 * (u ** 2 + 1)),
        (5, 5): (u ** 12 + u ** 11 - 2 * u ** 10 - u ** 9 + 2 * u ** 8 + u ** 7
                 - u ** 6 - u ** 5 + 2 * u ** 4 + u ** 3 - 2 * u ** 2 - u + 1) / u ** 6,
    }
    alias = {(0, 2): (0, 1), (0, 4): (0, 3), (1, 2): (0, 3),
             (2, 2): (1, 1), (1, 4): (1, 3), (2, 3): (1, 3), (2, 4): (1, 3),
             (2, 5): (1, 5), (3, 3): (1, 5), (4, 4): (1, 5), (4, 5): (3, 5)}
    return table[alias.get((i, j), (i, j))]


#: The `gram_det_eq` factorisation proved sorry-free in the Lean file, in `u`.
LEAN_DET_C = -(
    (u - 1) * (u + 1) * (u ** 3 + u - 1) ** 5 * (u ** 3 + u ** 2 + 1) ** 5
    * (u ** 6 - u ** 5 + u ** 4 - u ** 3 + 2 * u ** 2 - u + 1)
    * (u ** 6 + u ** 5 + 2 * u ** 4 + u ** 3 + u ** 2 + u + 1)
) / (u ** 10 * (u ** 2 + 1) ** 12)


def main() -> int:
    set_compute_dps()
    G = gram_generic()
    M = sp.Matrix(6, 6, lambda i, j: G[i][j])
    det_qz = sp.factor(sp.simplify(M.det()))

    # ── CHECK 1: the Lean closed forms ARE G(q, z_C) ────────────────────────
    c_mismatches = []
    for i in range(6):
        for j in range(i, 6):
            in_u = G[i][j].subs(z, Z_C).subs(q, u ** 2)
            d = sp.simplify(sp.radsimp(in_u - lean_entry(i, j)))
            if d != 0:
                c_mismatches.append([i, j, str(d)])

    # ── D-frame closed forms (rational in q — no √q anywhere) ───────────────
    GD = {(i, j): sp.factor(sp.cancel(sp.together(sp.simplify(G[i][j].subs(z, Z_D)))))
          for i in range(6) for j in range(i, 6)}

    # ── CHECK 2 / 3: numeric comparison at the substrate anchor ─────────────
    q0 = mp.mpf(Q_50_DIGIT_STR)
    ref = json.loads((COMP / "gram-matrix-dual.witness.json").read_text())["gram_matrix"]
    worst_d_vs_ref, cell_ref = mp.mpf(0), None
    worst_cd, cell_cd = mp.mpf(0), None
    for i in range(6):
        for j in range(6):
            key = (i, j) if i <= j else (j, i)
            fD = sp.lambdify(q, GD[key], modules="mpmath")
            fC = sp.lambdify(q, sp.simplify(G[key[0]][key[1]].subs(z, Z_C)), modules="mpmath")
            dref = abs(fD(q0) - mp.mpf(repr(ref[i][j])))
            if dref > worst_d_vs_ref:
                worst_d_vs_ref, cell_ref = dref, (i, j)
            dcd = abs(fC(q0) - fD(q0))
            if dcd > worst_cd:
                worst_cd, cell_cd = dcd, (i, j)

    # the red assertion this probe explains
    red = json.loads((COMP / "gram-h3-symbolic-regression.witness.json").read_text())
    red_computed = next(a["computed"] for a in red["assertions"]
                        if a["name"] == "gram_h3_symbolic_matches_pyhecke")

    # ── CHECK 4: D is a root of the determinant, identically in q ───────────
    det_D = sp.cancel(sp.simplify(det_qz.subs(z, Z_D)))
    MD = sp.Matrix(6, 6, lambda i, j: sp.cancel(G[i][j].subs(z, Z_D))
                   if i <= j else sp.cancel(G[j][i].subs(z, Z_D)))
    null = MD.nullspace()
    antisym = sp.Matrix([sp.Rational(-1, 1) ** 0 * (-1 / q) ** len(w) for w in NF_BASIS])
    antisym_annihilated = sp.simplify(MD * antisym) == sp.zeros(6, 1)

    # ── CHECK 5: cross-validate C against the sorry-free Lean theorem ───────
    # sequential, NOT sp.subs({z: …, q: …}): a dict substitutes simultaneously,
    # so the `q` inside the freshly-substituted z_C would survive unrewritten.
    det_C_in_u = sp.cancel(sp.simplify(det_qz.subs(z, Z_C).subs(q, u ** 2)))
    lean_det_agrees = sp.simplify(det_C_in_u - LEAN_DET_C) == 0

    # ── CHECK 6: what survives the frame change, for every z ───────────────
    symm_all_z = all(sp.simplify(G[i][j] - G[j][i]) == 0 for i in range(6) for j in range(6))
    top_left_all_z = sp.simplify(G[0][0] - 1) == 0

    payload = {
        "generic_gram_q_z": {f"G[{i}][{j}]": str(G[i][j])
                             for i in range(6) for j in range(i, 6)},
        "det_generic_q_z": str(det_qz),
        "conventions": {
            "z_C": str(Z_C), "z_D": str(Z_D),
            "z_C_note": "convention C (excised 2026-08-09 / re-affirmed 2026-08-15)",
            "z_D_note": "convention D (canonical, owner ruling 2026-08-15)",
        },
        "check1_lean_is_convention_C": {
            "entries_compared": 21,
            "exact_mismatches": len(c_mismatches),
            "mismatch_detail": c_mismatches,
            "verdict": ("every gramEntry equals G(q, z_C) exactly"
                        if not c_mismatches else "DRIFT — see mismatch_detail"),
        },
        "check2_reference_is_convention_D": {
            "reference": "computations/gram-matrix-dual.witness.json",
            "max_abs_diff_vs_G_at_z_D": fmt(worst_d_vs_ref),
            "worst_cell": list(cell_ref),
            "note": ("the reference stores float64-rounded decimal strings, so "
                     "~1e-16 is agreement, not disagreement"),
        },
        "check3_red_assertion_is_the_convention_gap": {
            "assertion": "gram_h3_symbolic_matches_pyhecke",
            "recorded_computed": red_computed,
            "max_abs_C_minus_D_at_q0": fmt(worst_cd),
            "worst_cell": list(cell_cd),
            "abs_diff_recorded_vs_exact": fmt(abs(mp.mpf(red_computed) - worst_cd)),
            "reproduces_recorded_value": bool(abs(mp.mpf(red_computed) - worst_cd) < mp.mpf("1e-15")),
            "why_not_to_the_last_digit": (
                "the recorded value is (C-frame symbolic at 50 dps) minus the "
                "FLOAT64 reference the regression script reads out of "
                "gram-matrix-dual.witness.json; this probe differences two EXACT "
                "frames. The two therefore agree only to the float64 rounding of "
                "that reference entry (~1e-16), which is what the diff above is."),
        },
        "check4_D_is_a_root_of_the_determinant": {
            "det_factored": str(det_qz),
            "vanishing_factor": str(sp.expand((q ** 2 + 1) * z - q ** 3)),
            "det_at_z_D": str(det_D),
            "det_at_z_D_is_identically_zero": det_D == 0,
            "rank_at_z_D": int(MD.rank()),
            "nullspace_dim_at_z_D": len(null),
            "null_vector": [str(sp.simplify(x)) for x in null[0]] if null else [],
            "antisymmetriser_annihilated": bool(antisym_annihilated),
            "confirms": ("gram_radical_exact_probe.py (exact at 3 rational q) and "
                         "qou-u2jg (keystone, from the trace side) — this reaches "
                         "the same fact as an identity in q, from the determinant"),
        },
        "check5_cross_validation_vs_lean": {
            "lean_theorem": "QOU.Interactions.GramMatrixH3Symbolic.gram_det_eq",
            "det_C_rewritten_in_u": str(sp.factor(det_C_in_u)),
            "agrees_with_lean_factorization": bool(lean_det_agrees),
        },
        "check6_what_survives_the_frame_change": {
            "gramMatrix_isSymm_holds_for_every_z": bool(symm_all_z),
            "gramMatrix_top_left_holds_for_every_z": bool(top_left_all_z),
            "gramMatrix_det_ne_zero_under_D": False,
            "positive_definite_under_D": False,
            "spectrum_note": ("the reference witness records eigenvalues "
                              "[4.230, 0.753, 3.07e-17, 0.753, 0.753, -0.753] at q_0 — "
                              "one zero AND one negative, so the D-frame form is "
                              "indefinite, not merely positive-semi-definite"),
        },
        "convention_D_closed_forms": {
            f"G[{i}][{j}]": str(GD[(i, j)]) for i in range(6) for j in range(i, 6)
        },
        "convention_D_closed_form_note": (
            "every D-frame entry is a rational function of q with denominator a "
            "power of (q²+1) — the u = √q parametrisation the Lean file is built "
            "on is not needed under D, which also removes the Real.sqrt that "
            "forces that file onto ℝ (AGENTS.md §7c)"
        ),
        "context": {
            "block": "prop:gram-matrix-h3-symbolic",
            "lean": "content/quantum-observable-universe/lean/QOU/Interactions/GramMatrixH3Symbolic.lean",
            "bean": "qou-bm4i",
            "scope": ("(b) structural exclusion per AGENTS.md — the invariant is "
                      "the exact determinant factorisation in check4, not a probe"),
        },
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    out = WitnessBuilder.wrap_legacy(
        "gram-h3-convention-frame-probe", payload,
        script_path=__file__, engine="python+sympy(exact over Q(q,z))",
    ).save()

    print("=== H_3 Gram: which convention is each side in? ===")
    print(f"  det G(q,z) = {det_qz}")
    print(f"  vanishing factor (q²+1)z − q³  ⇒  z_D = q³/(q²+1) is a ROOT")
    print()
    print(f"  CHECK 1  Lean gramEntry == G(q, z_C)      mismatches: {len(c_mismatches)}/21")
    print(f"  CHECK 2  G(q, z_D) vs reference witness   max diff: "
          f"{mp.nstr(worst_d_vs_ref, 6)} at {cell_ref}")
    print(f"  CHECK 3  |C − D| at q_0, both exact       {mp.nstr(worst_cd, 21)}")
    print(f"           recorded (vs float64 reference)  {red_computed[:23]}")
    print(f"           agree to                          "
          f"{mp.nstr(abs(mp.mpf(red_computed) - worst_cd), 3)} (float64 floor)")
    print(f"  CHECK 4  det G(q, z_D) identically zero:  {det_D == 0}  "
          f"(rank {MD.rank()}, null dim {len(null)})")
    print(f"           antisymmetriser annihilated:      {antisym_annihilated}")
    print(f"  CHECK 5  agrees with Lean gram_det_eq:     {lean_det_agrees}")
    print(f"  CHECK 6  isSymm / top_left hold ∀ z:       {symm_all_z} / {top_left_all_z}")
    print()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
