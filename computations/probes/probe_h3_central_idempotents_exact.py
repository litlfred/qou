#!/usr/bin/env python3
"""
probe_h3_central_idempotents_exact.py — §9.4 L-2 groundwork: the three
central idempotents of H_3(q), EXACT in ℚ(q), on the 6-word basis.

Goal. The `QOU.Hecke.WedderburnDecomp` class (PR #3261 added `central`)
carries `idempotent` / `orthogonal` / `central` / `complete` as AXIOMS
(Mathas §3.43 — the L-2 debt). At n = 3 these are finitely checkable:
this probe CONSTRUCTS π_(3), π_(2,1), π_(1³) explicitly as ℚ(q)-linear
combinations of the word basis {1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀} and
verifies all four axioms exactly, giving a future Lean session the
literal coefficients for a concrete n=3 `WedderburnDecomp` instance.

Method. ρ = ρ_(3) ⊕ ρ_(2,1) ⊕ ρ_(1³) (1-dim σ↦q; the rational seminormal
2-dim pair of `BorromeanCanonicalTraceDerivation.lean`; 1-dim σ↦−q⁻¹) is
a faithful 6-dim representation of the 6-dim algebra H_3(q) (Wedderburn),
so identities verified in ρ hold in H_3. Solve ρ_μ(π_λ) = δ_{λμ}·I for
the 6 coefficients of each π_λ (6 equations, 6 unknowns, unique).

Assertions (all exact sympy, ℚ(q)):
  A1 solutions exist and are unique (system rank 6);
  A2 idempotency π_λ² = π_λ and orthogonality π_λπ_μ = 0 (in ρ);
  A3 centrality [π_λ, σᵢ] = 0 (in ρ);
  A4 completeness Σ_λ π_λ = 1 (coefficient level);
  A5 canonical-trace values: tr_C(π_λ) = w_λ(t)·d_λ with the
     Markov-forced weights of BorromeanCanonicalTraceDerivation
     (so y_λ := tr_M(π_λ)/d_λ matches the Lean weight defs).

Output: probe-h3-central-idempotents-exact.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import sympy as sp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
from witness_base import WitnessBuilder  # noqa: E402

q = sp.symbols("q", positive=True)
h = q - 1 / q

# The three irreps (block-diagonal 4x4 total: 1 + 2 + 1)
S0_2 = sp.Matrix([[q, 0], [1, -1/q]])
S1_2 = sp.Matrix([[-1/q, 1], [0, q]])


def rho(word):
    """ρ(T_word) as (scalar_triv, 2x2 matrix, scalar_sign)."""
    triv, sign = sp.Integer(1), sp.Integer(1)
    M = sp.eye(2)
    for g in word:
        triv *= q
        sign *= -1/q
        M = M * (S0_2 if g == 0 else S1_2)
    return triv, sp.simplify(M), sign


WORDS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
RHO = [rho(w) for w in WORDS]


def solve_idempotent(target):
    """Solve rho(sum c_i T_wi) = diag-blocks(target) exactly."""
    cs = sp.symbols("c0:6")
    triv = sum(c * RHO[i][0] for i, c in enumerate(cs))
    two = sp.zeros(2, 2)
    for i, c in enumerate(cs):
        two += c * RHO[i][1]
    sign = sum(c * RHO[i][2] for i, c in enumerate(cs))
    t_triv, t_two, t_sign = target
    eqs = [sp.Eq(triv, t_triv), sp.Eq(sign, t_sign)]
    for a in range(2):
        for b in range(2):
            eqs.append(sp.Eq(two[a, b], t_two[a, b]))
    sol = sp.solve(eqs, list(cs), dict=True)
    assert len(sol) == 1, f"expected unique solution, got {len(sol)}"
    return [sp.cancel(sp.together(sol[0][c])) for c in cs]


PI = {
    "(3)": solve_idempotent((1, sp.zeros(2, 2), 0)),
    "(2,1)": solve_idempotent((0, sp.eye(2), 0)),
    "(1,1,1)": solve_idempotent((0, sp.zeros(2, 2), 1)),
}


def rho_of(coeffs):
    triv = sum(c * RHO[i][0] for i, c in enumerate(coeffs))
    two = sp.zeros(2, 2)
    for i, c in enumerate(coeffs):
        two += c * RHO[i][1]
    sign = sum(c * RHO[i][2] for i, c in enumerate(coeffs))
    return sp.cancel(triv), two.applyfunc(sp.cancel), sp.cancel(sign)


def main() -> int:
    lams = list(PI)
    images = {lam: rho_of(PI[lam]) for lam in lams}

    # A2 idempotency + orthogonality, A3 centrality — verified in the
    # faithful rho (blockwise scalar/matrix arithmetic).
    ok_idem = all(
        sp.simplify(images[l][0]**2 - images[l][0]) == 0
        and sp.simplify(images[l][1] * images[l][1] - images[l][1]) == sp.zeros(2, 2)
        and sp.simplify(images[l][2]**2 - images[l][2]) == 0
        for l in lams)
    ok_orth = all(
        sp.simplify(images[a][0] * images[b][0]) == 0
        and sp.simplify(images[a][1] * images[b][1]) == sp.zeros(2, 2)
        and sp.simplify(images[a][2] * images[b][2]) == 0
        for a in lams for b in lams if a != b)
    gens = [rho((0,)), rho((1,))]
    ok_cent = all(
        sp.simplify(images[l][1] * g[1] - g[1] * images[l][1]) == sp.zeros(2, 2)
        for l in lams for g in gens)

    # A4 completeness at coefficient level: sum of coefficient vectors
    # must be (1, 0, 0, 0, 0, 0).
    total = [sp.cancel(sum(PI[l][i] for l in lams)) for i in range(6)]
    ok_comp = total[0] == 1 and all(c == 0 for c in total[1:])

    # A5 canonical-trace values vs the Lean Markov-forced weights.
    # tr_C on words (canonical M1-M3 values): tr(1)=1, tr(sigma)=z,
    # tr(s0s1)=tr(s1s0)=z^2, tr(s0s1s0)=h z^2 + z.
    t = sp.symbols("t", positive=True)
    # LABELLED, NOT MIGRATED, 2026-08-10. `t/(t**2+1)` is the EXCISED convention
    # C written in the half-argument variable (with t = q^{1/2}); convention D
    # would read t**6/(t**4+1). Renamed z -> z_C so the producer audit clears it
    # as a labelled value rather than flagging it as a relapse.
    #
    # NOT changed to D, because that would be guessing at intent: this block
    # compares against "the Lean Markov-forced weights", and the Lean side is
    # now convention D. So either the comparison is currently mismatched (C
    # values against D-forced weights) and the fix is to migrate this line, or
    # the probe deliberately evaluates C for contrast and should say so the way
    # RESOLVED 2026-08-30 (qou-t9r1): the fear above is BACKWARDS. The Lean has
    # BOTH arms as separate declarations -- `BorromeanMarkovTrace` is D, and
    # `BorromeanCanonicalTraceDerivation` (`trC_borromean_derived`), which is the
    # one THIS probe compares against, is C. They are a deliberately-maintained
    # pair: `BorromeanTraceConventionSplit.lean` proves D != C sorry-free. So the
    # comparison is correctly paired and z_C is the object under test, not
    # residual C -- binding z_D here would assert a known-false equality.
    # Evidence is this probe's own exact-symbolic PASS: because D != C is a
    # THEOREM, a mismatched pairing could not pass. Ledger-adjudicated;
    # taxonomy row 20 (the D arm is in Lean, so no Python-side pairing test
    # can see it). Prior text kept below for provenance:
    # probe_convention_d_vs_c_borromean now does. Running it decides which;
    # neither answer should be assumed. Bean qou-9xla.
    z_C = t / (t**2 + 1)
    trc_words = [sp.Integer(1), z_C, z_C, z_C**2, z_C**2,
                 h.subs(q, t**2) * z_C**2 + z_C]
    den = ((t**2 + 1)**2 * (t**4 + 1) * (t**2 - t + 1)
           * (t**2 + t + 1) * (t**4 - t**2 + 1))
    wq = {
        "(3)": (t + 1) * (t**3 + t**2 + 1)
        * (t**6 - t**5 + t**4 - t**3 + 2*t**2 - t + 1) / den,
        "(2,1)": t**3 * (t**3 + t - 1) * (t**3 + t**2 + 1) * (t**4 + 1) / den,
        "(1,1,1)": t**6 * (t - 1) * (t**3 + t - 1)
        * (t**6 + t**5 + 2*t**4 + t**3 + t**2 + t + 1) / den,
    }
    dims = {"(3)": 1, "(2,1)": 2, "(1,1,1)": 1}
    ok_tr = True
    for l in lams:
        tr_pi = sum(sp.cancel(PI[l][i].subs(q, t**2)) * trc_words[i]
                    for i in range(6))
        diff = sp.cancel(sp.together(tr_pi - dims[l] * wq[l]))
        if diff != 0:
            ok_tr = False
            print(f"A5 FAIL for {l}: diff = {diff}")

    for l in lams:
        print(f"pi_{l} coefficients on (1, s0, s1, s0s1, s1s0, s0s1s0):")
        for w, c in zip(WORDS, PI[l]):
            print(f"    {w}: {c}")
    print(f"A2 idempotent: {ok_idem}   orthogonal: {ok_orth}")
    print(f"A3 central: {ok_cent}   A4 complete: {ok_comp}   A5 traces: {ok_tr}")

    wb = WitnessBuilder("probe-h3-central-idempotents-exact",
                        engine="sympy", output_dir=HERE)
    wb.set_description(
        "L-2 groundwork (Mathas 3.43 discharge at n=3): explicit central "
        "idempotents of H_3(q) on the 6-word basis, exact in Q(q); "
        "idempotency/orthogonality/centrality verified in the faithful "
        "sum-of-irreps rep, completeness at coefficient level, and "
        "tr_C(pi_lambda) = d_lambda * w_lambda matching the Lean "
        "Markov-forced weights (BorromeanCanonicalTraceDerivation). "
        "Coefficients ready for Lean transcription into a concrete n=3 "
        "WedderburnDecomp instance.")
    for l in lams:
        wb.add_data(f"pi_{l}_coeffs_words_1_s0_s1_s0s1_s1s0_s0s1s0",
                    [str(c) for c in PI[l]])
    wb.add_assertion("A2_idempotent_and_orthogonal",
                     str(ok_idem and ok_orth), "True",
                     source="pi_l^2 = pi_l and pi_a pi_b = 0 in faithful rho")
    wb.add_assertion("A3_central", str(ok_cent), "True",
                     source="[pi_l, sigma_i] = 0 in faithful rho")
    wb.add_assertion("A4_complete", str(ok_comp), "True",
                     source="sum_l pi_l = 1 at coefficient level")
    wb.add_assertion("A5_traces_match_lean_weights", str(ok_tr), "True",
                     source="tr_C(pi_l) = d_l * w_l(t) exactly (the Lean "
                            "wq3/wq21/wq111 closed forms)")
    path = wb.save()
    print(f"witness: {path}")
    ok = ok_idem and ok_orth and ok_cent and ok_comp and ok_tr
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
