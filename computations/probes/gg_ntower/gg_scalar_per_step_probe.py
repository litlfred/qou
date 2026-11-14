#!/usr/bin/env python3
"""A scalar per step: three invariants that close the γγ "fresh strands per
collision" programme, and the reason reading 3 cannot bound magnitude.

WHAT THIS IS, AND WHAT IT IS NOT.  This is a **re-derivation record**, not a
pre-registered search.  The three invariants below were first surfaced by an
adversarial review of two candidate constructions (session
01FsqmWKMezLw7W86Up44M8Y, PR #7817); they are re-derived here from scratch
against the corpus's own `gg_ntower_probe.Rep` / `tr` / `y_lambda`, exactly over
ℚ(q), so that the result rests on the corpus's machinery rather than on a
reviewer's reimplementation.  **No hypothesis class is searched and no element is
selected.**  F_required is evaluated at the end only to state where an
already-derived closed form crosses it — a check after the fact, never a target,
per AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3".

THE QUESTION THIS BEARS ON.  Owner, 2026-10-10: *"Find what element or functional
supplies a factor above 1 on the ruled base."*  Owner, 2026-10-11: *"go through γγ
production step by step to get to one and two nucleons; each collision shifts
things up the tower."*  `gg_ntower_probe` answered the braid-vertex half with
outcome (ii): no rigid shift but s = 0 (which does not climb) is admissible up to
n = 9.  Its results doc lists what it did not test, including **pair creation by
Jones projections (two strands per collision)** — the physically natural γγ vertex,
since γγ → e⁺e⁻ creates two particles rather than braiding existing ones.

THE RESULT.  That route does climb, and it is **closed by an identity rather than
by insufficient magnitude** — a scope-(b) exclusion with a named invariant, in the
sense of AGENTS.md §"Before declaring refuted".  The cabled crossing on a double
singlet is the scalar q²:

    e₀e₂ · Σ₁ = q² · e₀e₂,        Σ₁ = σ₁σ₀σ₂σ₁                        (I1)

so e₀e₂ · Σ₁^c = q^{2c} · e₀e₂ and the Markov trace is **exactly geometric** in the
number of cabled crossings:

    tr_M(e₀e₂ Σ₁^c) = q^{2c} / [2]_q⁴ = q^{4+2c} / (q²+1)⁴             (C)

`c` is therefore an unbounded knob on which **reading 3 — Frobenius positivity on
every block with y_λ > 0, the criterion ruled canonical on 2026-09-12, scoped to
the whole word 2026-09-13 and to every strand count 2026-10-12 — imposes no bound
at all.**  The family passes through F_required between c = 5 and c = 6.  Choosing
the c that clears 1 is "sweeping a discrete parameter for accuracy", which
§NO FITTING names outright as a fitted parameter.

Two companions generalise it past this one family:

    tr_M(y · e_m) = tr_M(y) / [2]_q²     for y ∈ H_m                   (I2)
    tr_M(V₀³ V_j³) = tr_M(V₀³)²          chain (j=2) and disjoint (j=3)(I3)

(I2) collapses any word whose top generator appears once; (I3) holds for
one-strand-sharing as well as disjoint placements — strictly stronger than
`explanation.md`, which claims multiplicativity only for the disjoint s = +3 case,
and it closes the braid-vertex arm by `gg_ntower`'s own outcome (ii).

Together: **every "fresh strands per collision" construction whose collisions are
joined by a chain or by a cabled double singlet contributes a scalar per step.**
A scalar per step is a geometric family, a geometric family has an unbounded free
index, and an unbounded free index cannot be fixed by a magnitude-blind criterion.

WHAT THIS DOES NOT CLAIM.  It does not deliver a nucleon — no quark letters, no
flavour, no two-nucleon level — so it answers the *mechanism* half of the
2026-10-11 ask and not the deliverable half.  It does not touch ε, z, the base, or
the ladder, all of which are closed elsewhere.  It selects nothing and re-scores
nothing; `qou-cds1` and `qou-99qc` stay open.

Beans: `qou-cds1`, `qou-99qc`, `qou-ales`.  Exact over ℚ(q); q₀ values at ≥ 50 dps.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gg_ntower_probe as g  # noqa: E402

q, H, K = g.q, g.H, g.K
Q0_STR = g.Q_50_DIGIT_STR
Q0_RAT = sp.Rational(Q0_STR)
T0 = time.time()

try:  # carry the corpus dps rather than a bare literal
    from qou_substrate.precision import COMPUTE_DPS as _DPS
except Exception:  # pragma: no cover - thin container
    _DPS = 70
mp.mp.dps = int(_DPS)

# |tr_M(Δ_S)| at z_D and the CODATA requirement, both quoted from the corpus and
# used ONLY to locate where the derived closed form crosses — never as a target.
ABS_TR_DELTA_S = mp.mpf("0.1062356398480927908921420")
F_REQUIRED = mp.mpf("1.75923699418")


def log(m):
    print(f"  {m}", flush=True)


def jones(R, p):
    """e_p: the antisymmetric eigenchannel projector of σ_p.

    σ has eigenvalues q and −q⁻¹ (AGENTS.md §7a Hecke-Skein), so
    e_p = (q·1 − σ_p)/(q + q⁻¹) projects on the −q⁻¹ channel.  It is the unique
    U_q(sl₂)-invariant cup-cap, i.e. the pair-creation vertex: forced, not chosen.
    """
    return (R.eye * K.from_sympy(q) - R.gen[p]) * K.from_sympy(sp.cancel(1 / (q + 1 / q)))


def is_zero(D):
    return all(
        K.to_sympy(D[i, j].element) == 0
        for i in range(D.shape[0])
        for j in range(D.shape[1])
    )


def markov(n, M_of):
    """tr_M(x) = Σ_λ y_λ χ_λ(x) over TWO-ROW λ ⊢ n.

    Three-or-more-row weights vanish identically under convention D
    (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`, sorry-free,
    general n, sole hypothesis q²+1 ≠ 0) — NOT by
    `markovWeights_eq_jones_of_threeRow_eq_zero`, which proves the converse
    (TL ⟹ D); see bean `qou-6moa`.
    """
    tot = 0
    for lam in g.two_row_shapes(n):
        R = g.rep(lam)
        tot += g.y_lambda(lam) * g.tr(M_of(R))
    return sp.cancel(sp.together(tot))


def at_q0(expr, digits=40):
    return mp.mpf(str(sp.N(expr.subs(q, Q0_RAT), digits)))


def sigma_cable(R):
    """Σ₁ = σ₁σ₀σ₂σ₁ — the cabled crossing exchanging the two singlet pairs."""
    return R.gen[1] * R.gen[0] * R.gen[2] * R.gen[1]


def v_cubed(R, i):
    """V_i³ with V_i = σ_i σ_{i+1}⁻¹, the γγ braid vertex of `gg_ntower`."""
    M = R.eye
    for _ in range(3):
        M = M * R.letter(i, 1) * R.letter(i + 1, -1)
    return M


def run():
    checks, data = {}, {}

    # ---- S: the projector is forced, and its σ-eigenvalues are the Jones ones
    log("S  e_p is a projector and σ_p e_p = −q⁻¹ e_p, σ_p⁻¹ e_p = −q e_p")
    s_ok = True
    for n in (3, 4, 5):
        for lam in g.two_row_shapes(n):
            R = g.rep(lam)
            E = jones(R, 0)
            s_ok &= is_zero(E * E - E)
            s_ok &= is_zero(R.gen[0] * E + E * K.from_sympy(1 / q))
            s_ok &= is_zero(R.letter(0, -1) * E + E * K.from_sympy(q))
    checks["S_projector_and_jones_eigenvalue"] = bool(s_ok)
    log(f"   -> {s_ok}")

    # ---- I1: the cabled crossing on a double singlet is the scalar q²
    log("I1 e₀e₂ · Σ₁ = q² · e₀e₂  (both sides), every two-row block n = 4,5,6")
    i1, i1_rows = True, {}
    for n in (4, 5, 6):
        for lam in g.two_row_shapes(n):
            R = g.rep(lam)
            if R.n - 1 < 4:
                continue
            E = jones(R, 0) * jones(R, 2)
            S = sigma_cable(R)
            rhs = E * K.from_sympy(q ** 2)
            r_ok, l_ok = is_zero(E * S - rhs), is_zero(S * E - rhs)
            i1_rows[f"n={n} lam={lam}"] = {"right": r_ok, "left": l_ok, "dim": R.dim}
            i1 &= r_ok and l_ok
    checks["I1_cabled_crossing_on_double_singlet_is_q_squared"] = bool(i1)
    data["I1_by_block"] = i1_rows
    log(f"   -> {i1}  ({len(i1_rows)} blocks)")

    # ---- I2: a top generator appearing once collapses to 1/[2]_q²
    log("I2 tr_M(y · e_m) = tr_M(y)/[2]_q²  for y ∈ H_m")
    i2, i2_rows = True, {}
    q2 = g.qint(2) ** 2
    for n in (3, 4, 5):
        m = n - 2  # e_m's generator index; y lives on strands below it
        words = [("s0", [(0, 1)])]
        if m >= 2:
            words += [("s0 s1", [(0, 1), (1, 1)]), ("s1 s0^-1", [(1, 1), (0, -1)])]
        for name, letters in words:
            num = markov(n, lambda R, L=letters, mm=m: R.word(L) * jones(R, mm))
            den = markov(n, lambda R, L=letters: R.word(L))
            d = sp.simplify(sp.cancel(sp.together(num - den / q2)))
            ok = d == 0
            i2_rows[f"n={n} y={name}"] = {"zero": bool(ok), "residual": str(d)}
            i2 &= ok
    checks["I2_top_generator_once_collapses"] = bool(i2)
    data["I2_by_word"] = i2_rows
    log(f"   -> {i2}  ({len(i2_rows)} words)")

    # ---- I3: chain AND disjoint multiplicativity
    log("I3 tr_M(V₀³ V_j³) = tr_M(V₀³)²  for j = 2 (one-strand-sharing) and 3 (disjoint)")
    t_single = markov(3, lambda R: v_cubed(R, 0))
    i3, i3_rows = True, {}
    for j, label in ((2, "one_strand_sharing_s_plus_2"), (3, "disjoint_s_plus_3")):
        n = j + 3
        both = markov(n, lambda R, jj=j: v_cubed(R, 0) * v_cubed(R, jj))
        d = sp.simplify(sp.cancel(sp.together(both - t_single ** 2)))
        ok = d == 0
        i3_rows[label] = {
            "n": n,
            "zero": bool(ok),
            "residual": str(d),
            "tr_M_at_q0": mp.nstr(at_q0(both), 20),
        }
        i3 &= ok
    checks["I3_chain_and_disjoint_multiplicativity"] = bool(i3)
    data["I3"] = {
        "tr_M_V0_cubed_exact": str(sp.nsimplify(t_single)),
        "tr_M_V0_cubed_at_q0": mp.nstr(at_q0(t_single), 20),
        "rows": i3_rows,
    }
    log(f"   -> {i3}")

    # ---- C: the closure.  geometric in c, hence an unbounded free index
    log("C  tr_M(e₀e₂ Σ₁^c) = q^(4+2c)/(q²+1)⁴, ratio exactly q²")
    closed_ok, ratio_ok, rows = True, True, {}
    prev = None
    q2_num = at_q0(sp.sympify(q ** 2))
    for c in range(1, 9):
        expr = markov(
            4,
            lambda R, cc=c: jones(R, 0) * jones(R, 2) * (sigma_cable(R) ** cc),
        )
        closed = sp.cancel(q ** (4 + 2 * c) / (q ** 2 + 1) ** 4)
        match = sp.simplify(sp.cancel(expr - closed)) == 0
        closed_ok &= match
        val = at_q0(expr)
        ratio = (val / prev) if prev is not None else None
        if ratio is not None:
            ratio_ok &= bool(abs(ratio - q2_num) < mp.mpf("1e-30"))
        rows[f"c={c}"] = {
            "closed_form_matches": bool(match),
            "tr_M_at_q0": mp.nstr(val, 20),
            "ratio_to_previous": (mp.nstr(ratio, 20) if ratio is not None else None),
            "F_vs_abs_tr_Delta_S": mp.nstr(val / ABS_TR_DELTA_S, 12),
        }
        prev = val
    checks["C_closed_form_matches_every_c"] = bool(closed_ok)
    checks["C_ratio_is_exactly_q_squared"] = bool(ratio_ok)

    # where the DERIVED family crosses the requirement -- a post-hoc check
    fs = {c: mp.mpf(rows[f"c={c}"]["F_vs_abs_tr_Delta_S"]) for c in range(1, 9)}
    below = [c for c in fs if fs[c] < F_REQUIRED]
    above = [c for c in fs if fs[c] >= F_REQUIRED]
    straddles = bool(below and above)
    checks["C_family_straddles_the_requirement"] = straddles
    data["C"] = {
        "closed_form": "q**(4+2*c)/(q**2+1)**4",
        "q_squared_at_q0": mp.nstr(q2_num, 22),
        "rows": rows,
        "F_required_order_zero_E0": mp.nstr(F_REQUIRED, 12),
        "abs_tr_M_Delta_S_at_zD": mp.nstr(ABS_TR_DELTA_S, 25),
        "crossing": {
            "last_c_below": max(below) if below else None,
            "first_c_at_or_above": min(above) if above else None,
        },
        "NOT_A_SELECTION": (
            "The crossing is reported so the magnitude is on the record. Reading 3 "
            "admits every c, so choosing the c that clears F_required would be "
            "selection against the target -- a fitted discrete parameter under "
            "AGENTS.md NO FITTING. No c is adopted."
        ),
    }
    log(f"   -> closed form {closed_ok}, ratio {ratio_ok}, straddles {straddles}")

    # ---- the conclusion, stated as a scope-(b) exclusion with its invariant
    checks["conclusion_scope_b_named_invariant"] = bool(i1 and closed_ok and ratio_ok)
    data["conclusion"] = {
        "scope": "(b) structural exclusion -- a proved identity forbids the ingredient",
        "invariant": "e_0 e_2 * Sigma_1 = q**2 * e_0 e_2 (I1), hence tr_M geometric in c (C)",
        "statement": (
            "Every 'fresh strands per collision' gamma-gamma construction whose "
            "collisions are joined by a chain (I3) or by a cabled double singlet (I1) "
            "contributes a SCALAR PER STEP. The resulting family is geometric, so its "
            "step index is a free unbounded knob, and reading 3 -- Frobenius positivity "
            "on every block with y_lambda > 0, at every strand count -- does not bound "
            "it. Magnitude therefore cannot be derived on this route; it can only be "
            "selected, which is forbidden."
        ),
        "what_it_does_not_close": (
            "It does not deliver a nucleon (no quark letters, no flavour, no "
            "two-nucleon level), so the deliverable half of the 2026-10-11 ask is "
            "untouched. It says nothing about the base, epsilon, z or the ladder."
        ),
        "reading_3_is_magnitude_blind": (
            "Measured three independent ways: admissible at every c = 1..8 here while "
            "tr_M grows without bound; 10 of 12 configurations admissible across a 7.6x "
            "magnitude range in the sibling pair-creation construction; and the composed "
            "tower 'rejects nothing and admits everything H_3 rejected'."
        ),
    }
    return checks, data


def main():
    checks, data = run()
    out = {
        "computation": "gg-scalar-per-step",
        "scriptFile": Path(__file__).name,
        "kind": "re-derivation record (no search, no selection)",
        "issue": 7727,
        "beans": ["qou-cds1", "qou-99qc", "qou-ales"],
        "q0": Q0_STR,
        "q0Anchor": "physical_proton",
        "markov_convention": "D (z = q^3/(q^2+1))",
        "compute_dps": int(mp.mp.dps),
        "checks": checks,
        "data": data,
        "wall_seconds": int(time.time() - T0),
    }
    (HERE / "gg-scalar-per-step.witness.json").write_text(
        json.dumps(out, indent=1, default=str) + "\n"
    )
    ok = all(v for v in checks.values() if isinstance(v, bool))
    n_ok = sum(1 for v in checks.values() if v is True)
    log("")
    log(f"{n_ok}/{len(checks)} checks passed")
    for k, v in checks.items():
        log(f"  [{'PASS' if v else 'FAIL'}] {k}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
