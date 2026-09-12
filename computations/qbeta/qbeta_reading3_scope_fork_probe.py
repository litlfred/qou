#!/usr/bin/env python3
"""qou-99qc: the SDP half of the ruling — reading 3 applied to the 5 letters the
gamma-gamma half provably cannot reach. It NARROWS by 3.2x and does not close,
AND its scope is ambiguous in a way that decides whether the census element is
admissible at all.

# Ref: computations/qbeta/qbeta_gamma_gamma_ruling_selects_ordering_probe.py (the gg half + parity bound)
# Ref: computations/qbeta/qbeta_delta_candidate_census_probe.py             (nuc9 / the models)
# Ref: content/quantum-observable-universe/lean/QOU/QBeta/GammaGammaSelectedDeltaVanishes.lean
# Ref: .beans/qou-ales--...md   (OWNER RULING 2026-09-08: gg production + the SDP)
# Ref: .beans/qou-99qc--...md

THE RULING HAS TWO HALVES and only one had been applied on this bean. Owner,
2026-09-08: *"All selection of great words should be done through gamma gamma
production AND the semi-definite product solutions at q0."* Owner, 2026-09-12:
*"try PSD confinement 3 for now, but keep 1 2 for later"*, where reading 3 is
Frobenius positivity PER BLOCK -- `chi_lambda(w) >= 0` on every block with
`y_lambda > 0`. At Wenzl level 2 that is `chi_(3) >= 0` and `chi_(2,1) >= 0`,
since `y_(1^3) = 0`.

HOW THE CHARACTERS ARE OBTAINED, and it needs no new machinery. `chi_(3)` is
the one-dimensional character `sigma -> q`, so a letter `sigma_g + dc*h` has
value `q + dc*h` and `chi_(3)(w) = prod_i (q + dc_i*h)` -- multiplicative, and
independent of WHICH generator each letter sits on. Then from
`tr_{z_D} = y_(3) chi_(3) + y_(2,1) chi_(2,1)` (level 2, `y_(1^3) = 0`),

    chi_(2,1)(w) = (tr_{z_D}(w) - y_(3) chi_(3)(w)) / y_(2,1)

CALIBRATED THREE WAYS before any conclusion is drawn: `chi_(2,1)(1) = 2` (the
block dimension) exactly; `chi_(3)(V^k) = 1` exactly for all k, which is the
sorry-free `unit_on_vertices_eq_one` reproduced numerically from the opposite
direction; and `y_(3) + 2 y_(2,1) = 1`.

RESULT 1 -- THE `(3)` BLOCK CANNOT DISCRIMINATE AT ALL. `chi_(3)` depends only
on the shift multiset, and the shifts are DETERMINED by flavour (this branch's
`pairCounts_determined`). So `chi_(3)` is one number per nucleon -- 1.3825 for
the proton, 1.1221 for the neutron -- for every one of the 32 generator
assignments. Positive, hence never binding. The whole content of reading 3 here
is `chi_(2,1) >= 0`.

RESULT 2 -- IT NARROWS BY 3.2x AND DOES NOT CLOSE. Of 32 assignments of the 3
quark + 2 gluon letters (shifts fixed, generators free), 20 survive for the
proton and 16 for the neutron: 320 admissible `Delta` pairs of 1024. The target
residual (0 %) lies INSIDE the admissible range [-98.57 %, +35.17 %], so
reading 3 does not exclude agreement -- but the NEAREST admissible pair misses
the experimental window by 122617x, so it cannot manufacture agreement either.
Falsifiable, and currently failing. Same shape as #7188's ordering result.

🛑 RESULT 3 -- THE SCOPE OF READING 3 IS AMBIGUOUS, AND THE TWO READINGS
DISAGREE ABOUT THE CENSUS ELEMENT. This is the finding, and it is an owner
question rather than a measurement:

  (A) reading 3 applies to the gamma-gamma-SELECTED CORE only.
      `chi_(2,1)(V^3) = +1.9942 >= 0` -> admissible, and k = 3 = beta_Bor is
      selected (the sibling's `frobeniusSelected_borromean`, #7207). The census
      element stands and every residual on this bean stands with it.

  (B) reading 3 applies to the WHOLE 11-crossing word.
      The census's own assignment -- `nuc9`'s quark generators (0,0,1) with the
      two `sigma_0` gluon letters -- gives `chi_(2,1) = -0.2806` (proton) and
      `-0.3720` (neutron). BOTH NEGATIVE. So the element every merged probe on
      this arc computes, the one producing -15.4514 % and -17.4959 %, is
      INADMISSIBLE under the ruling.

Both readings are consistent with the ruling as relayed. The sibling applied
(A); nothing in the owner's words settles it. This probe reports both and
selects neither -- picking the one whose numbers survive would be selection
against the target, and picking the one that invalidates the arc would be
equally unearned.

WHAT IS NOT CLAIMED. That reading (B) refutes anything. It is a scope-(a)
observation about ONE assignment under ONE reading. The `chi_(2,1)` extraction
is exact but derived by subtraction from `tr_{z_D}`, so it inherits that
quantity's convention (D) and pin (proton) and nothing more.

ARITHMETIC. mpmath mpf at 60 dps, proton pin, convention D. No float64.

Run: python3 -u computations/qbeta/qbeta_reading3_scope_fork_probe.py \
       2>&1 | tee /tmp/qbeta_reading3.log
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402

mp = _order.mp
set_compute_dps(60)
mp.mp.dps = 60

Q0, H0, ZD, E0, QB = _order.Q0, _order.H0, _order.ZD, _order.E0, _order.QB
TARGET = _order.TARGET
Q_50_DIGIT_STR = _order.Q_50_DIGIT_STR
Z, HALF, NEG1 = mp.mpf(0), mp.mpf(-1) / 2, mp.mpf(-1)

Y3 = (Q0 ** 4 + 1) / (Q0 ** 2 + 1) ** 2
Y21 = Q0 ** 2 / (Q0 ** 2 + 1) ** 2

CORE = [(0, Z), (1, NEG1)] * 3
QSHIFT = {"p": [Z, HALF, HALF], "n": [HALF, HALF, NEG1]}
CENSUS_ASSIGNMENT = ((0, 0, 1), (0, 0))   # nuc9's quark gens + nuc11's gluon

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def tr(letters):
    return _order.tr_at(_order.word_nf(letters), ZD)


def chi3(letters):
    v = mp.mpf(1)
    for _, dc in letters:
        v *= (Q0 + dc * H0)
    return v


def chi21(letters):
    return (tr(letters) - Y3 * chi3(letters)) / Y21


def assignments(kind):
    out = []
    for qg in itertools.product((0, 1), repeat=3):
        for gg in itertools.product((0, 1), repeat=2):
            w = (CORE
                 + [(qg[i], QSHIFT[kind][i]) for i in range(3)]
                 + [(gg[i], Z) for i in range(2)])
            out.append(((qg, gg), w))
    return out


def main() -> int:
    print("qou-99qc — the SDP half: reading 3 on the 5 letters the γγ half "
          "cannot reach\n")

    # ---- CHECK 1: calibrate the character extraction three ways -----------
    print("CHECK 1 — calibrate χ before concluding anything")
    check("y_weights_normalise", abs(Y3 + 2 * Y21 - 1) < mp.mpf("1e-50"),
          f"y_(3) + 2·y_(2,1) = 1 exactly; y_(3) = {mp.nstr(Y3, 18)}, "
          f"y_(2,1) = {mp.nstr(Y21, 18)}")
    check("chi21_of_identity_is_the_block_dimension",
          abs(chi21([]) - 2) < mp.mpf("1e-45"),
          f"χ_(2,1)(1) = {mp.nstr(chi21([]), 20)} = dim V_(2,1)")
    V = lambda k: [(0, Z), (1, NEG1)] * k
    check("chi3_of_every_vertex_power_is_one",
          all(abs(chi3(V(k)) - 1) < mp.mpf("1e-45") for k in range(6)),
          "reproduces the sorry-free unit_on_vertices_eq_one numerically, "
          "from the opposite direction")

    # ---- CHECK 2: the (3) block cannot discriminate -----------------------
    print("\nCHECK 2 — the `(3)` block carries NO information about the free letters")
    c3 = {}
    for kind in ("p", "n"):
        ws = assignments(kind)
        vals = [chi3(w) for _, w in ws]
        c3[kind] = vals[0]
        spread = max(vals) - min(vals)
        print(f"    {kind}: χ_(3) = {mp.nstr(vals[0], 14)} over all "
              f"{len(ws)} assignments (spread {mp.nstr(spread, 4)})")
        check(f"chi3_is_generator_independent_{kind}",
              spread < mp.mpf("1e-45") and vals[0] > 0,
              "χ_(3) = ∏(q + dᵢ) depends only on the shift multiset, which "
              "flavour DETERMINES — so it is positive and never binding")

    # ---- CHECK 3: reading 3 narrows but does not close -------------------
    print("\nCHECK 3 — χ_(2,1) ≥ 0 over the 32 generator assignments")
    surv = {}
    for kind in ("p", "n"):
        ws = assignments(kind)
        ok = [(t, w) for t, w in ws if chi21(w) >= 0]
        surv[kind] = ok
        vals = sorted(chi21(w) for _, w in ws)
        print(f"    {kind}: {len(ok)}/{len(ws)} survive   χ_(2,1) ∈ "
              f"[{mp.nstr(vals[0], 10)}, {mp.nstr(vals[-1], 10)}]")
    npairs = len(surv["p"]) * len(surv["n"])
    check("reading3_narrows_but_does_not_close",
          0 < npairs < 1024,
          f"{npairs} admissible Δ pairs of 1024 — a {mp.nstr(mp.mpf(1024)/npairs, 4)}× "
          "narrowing, not a selection")

    res = []
    for _, wp in surv["p"]:
        for _, wn in surv["n"]:
            d = tr(wn) - tr(wp)
            res.append((abs(d) * E0 / QB - 1) * 100)
    res.sort()
    print(f"    residual over admissible pairs: [{mp.nstr(res[0], 8)} %, "
          f"{mp.nstr(res[-1], 8)} %]")
    check("target_is_INSIDE_the_admissible_range",
          res[0] < 0 < res[-1],
          "so reading 3 does not exclude agreement — the falsifiability "
          "problem, not a solution")
    nearest = min(abs(r) for r in res)
    window_pct = mp.mpf("7.8e-7") * 100
    check("nearest_admissible_pair_misses_the_window",
          nearest / window_pct > 1000,
          f"nearest |residual| = {mp.nstr(nearest, 8)} %, missing the ~780 ppb "
          f"window by {mp.nstr(nearest / window_pct, 8)}× — so it cannot "
          "manufacture agreement either")

    # ---- CHECK 4: the scope fork ----------------------------------------
    print("\nCHECK 4 — 🛑 the scope of reading 3 decides the census element")
    c21_core = chi21(V(3))
    print(f"    (A) core only:  χ_(2,1)(V³) = {mp.nstr(c21_core, 12)}")
    check("reading_A_admits_the_core", c21_core >= 0,
          "k = 3 = β_Bor selected — the sibling's frobeniusSelected_borromean")
    for kind in ("p", "n"):
        w = dict(assignments(kind))[CENSUS_ASSIGNMENT]
        c = chi21(w)
        print(f"    (B) whole word, census assignment, {kind}: "
              f"χ_(2,1) = {mp.nstr(c, 12)}")
    cp = chi21(dict(assignments("p"))[CENSUS_ASSIGNMENT])
    cn = chi21(dict(assignments("n"))[CENSUS_ASSIGNMENT])
    check("reading_B_EXCLUDES_the_census_assignment",
          cp < 0 and cn < 0,
          "both negative — the element every merged probe on this arc "
          "computes is inadmissible under reading (B)")

    ok = all(r[1] for r in RESULTS)
    print()
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — the SDP half narrows the 5 free letters by 3.2x (1024 ->")
    print("320 admissible pairs) and does NOT close them. The target sits")
    print("inside the admissible range while the nearest admissible pair misses")
    print("the experimental window by 1.2e5x: falsifiable, currently failing.")
    print("The `(3)` block is structurally silent here — its character depends")
    print("only on the shift multiset, which flavour already determines.")
    print()
    print("🛑 AND THE SCOPE OF READING 3 IS AN OPEN OWNER QUESTION. Applied to")
    print("the γγ-selected CORE it admits V^3 and selects k = 3. Applied to the")
    print("WHOLE 11-crossing word it EXCLUDES the census assignment (χ_(2,1) =")
    print("-0.2806 proton, -0.3720 neutron), which would make every residual on")
    print("this bean inadmissible. Both readings fit the ruling as relayed.")
    print("This probe reports both and selects NEITHER.")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-reading3-scope-fork")
        w.set_description(
            "Applies the SDP half of the 2026-09-08 ruling (reading 3: "
            "Frobenius positivity per block) to the 5 letters the gamma-gamma "
            "half provably cannot reach. It narrows 1024 -> 320 admissible "
            "Delta pairs and does not close them; the target is inside the "
            "admissible range while the nearest pair misses the experimental "
            "window by 1.2e5x. The (3) block is structurally silent. AND the "
            "SCOPE of reading 3 is ambiguous: applied to the gg-selected core "
            "it admits V^3, applied to the whole 11-crossing word it EXCLUDES "
            "the census assignment. Reports both, selects neither."
        )
        w.add_data("markov_convention", "D — z_D = q^3/(q^2+1), Wenzl level 2")
        w.add_data("q0_anchor", "proton")
        w.add_data("q0_value", Q_50_DIGIT_STR)
        w.add_data("block_weights",
                   {"y_3": mp.nstr(Y3, 30), "y_2_1": mp.nstr(Y21, 30),
                    "y_1_1_1": "0 (level 2)"})
        w.add_data("chi3_generator_independent",
                   {k: mp.nstr(v, 20) for k, v in c3.items()})
        w.add_data("reading3_on_free_letters",
                   {"assignments_per_nucleon": 32,
                    "surviving_proton": len(surv["p"]),
                    "surviving_neutron": len(surv["n"]),
                    "admissible_pairs": npairs, "of": 1024,
                    "narrowing_factor": mp.nstr(mp.mpf(1024) / npairs, 8),
                    "residual_min_pct": mp.nstr(res[0], 12),
                    "residual_max_pct": mp.nstr(res[-1], 12),
                    "nearest_abs_residual_pct": mp.nstr(nearest, 12),
                    "nearest_over_window": mp.nstr(nearest / window_pct, 10)})
        w.add_data("scope_fork",
                   {"reading_A_core_only_chi21_V3": mp.nstr(c21_core, 20),
                    "reading_A_verdict": "admissible; selects k = 3 = beta_Bor",
                    "reading_B_whole_word_chi21_proton": mp.nstr(cp, 20),
                    "reading_B_whole_word_chi21_neutron": mp.nstr(cn, 20),
                    "reading_B_verdict":
                        "EXCLUDES the census assignment (both negative)"})
        w.add_caveat(
            "🛑 THE SCOPE OF READING 3 IS AN OPEN OWNER QUESTION, not a "
            "measurement. (A) core-only admits V^3 and selects k = 3, which is "
            "what the sibling applied on #7207. (B) whole-word excludes the "
            "census assignment and would make every residual on this bean "
            "inadmissible. BOTH fit the ruling as relayed. This probe selects "
            "NEITHER: picking (A) because its numbers survive is selection "
            "against the target, and picking (B) because it invalidates the "
            "arc is equally unearned."
        )
        w.add_caveat(
            "Reading 3 does NOT close the 5 free letters under either scope. "
            "320 of 1024 pairs survive, the target is inside the admissible "
            "range, and the nearest admissible pair misses the ~780 ppb window "
            "by 1.2e5x. So the SDP half is falsifiable and currently failing "
            "-- the same shape as #7188's ordering result, and NOT a rescue."
        )
        w.add_caveat(
            "chi_(2,1) is obtained by subtraction from tr_{z_D}, so it "
            "inherits that quantity's convention (D) and pin (proton) and "
            "nothing more. Calibrated three ways first: chi_(2,1)(1) = 2 "
            "exactly, chi_(3)(V^k) = 1 exactly (the sorry-free "
            "unit_on_vertices_eq_one, reproduced from the opposite direction), "
            "and y_(3) + 2 y_(2,1) = 1."
        )
        w.add_caveat(
            "Scope-(a): 32 generator assignments per nucleon with the SHIFTS "
            "held at their flavour-determined values and the census ORDER "
            "(core, quark, gluon). It does not enumerate positions, and it "
            "does not claim reading (B) refutes anything."
        )
        for name, passed, det in RESULTS:
            w.add_assertion(name, "1" if passed else "0", "1", "0", source=det or None)
        w.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
