"""Where the H_3(q) Gram degenerates, and whether the "hadronic melt" survives
convention D.

Bean `qou-vvv4`.

The corpus records, as computed output, the convention-C factorisation

    det G(u) = -(u-1)(u+1)(u^3+u-1)^5(u^3+u^2+1)^5 S1(u) S2(u) / (u^10 (u^2+1)^12)

(`QOU.Interactions.GramMatrixH3Symbolic`, `u = sqrt(q)`), and reads the
`(u^3+u-1)^5` zero at `u = 1/psi` as a hadronic phase transition
(`prop:spectrahedral-phase-collapse`).  What it does NOT record is *why* those
factors are there, and the two sibling content blocks disagree about the
transition they describe:

| | `spectrahedral-phase-collapse.md` (+ sorry-free Lean) | `...-melt.md` |
|---|---|---|
| threshold | `u = 1/psi ~ 0.68233`, `u = sqrt(q)`, so `q ~ 0.4656` | "`q = psi ~ 1.4655`" |
| direction | Lean hypothesis `u^3+u-1 < 0`, i.e. `u` BELOW | "Heated PAST", i.e. above |

This probe answers the mechanism question, and the two disagreements fall out
of the answer rather than being adjudicated by reading.

## Result

Solve for the Wedderburn weights of the Markov trace on `H_3(q)` with a FREE
loop parameter `z` (three partitions, three linear equations on `1`, `sigma`,
`sigma_1 sigma_2`):

    y_(3)    = (qz+1)(q^3 z + qz + 1) / ((q^2+1)(q^2-q+1)(q^2+q+1))
    y_(2,1)  = -q (z-q)(qz+1)         / ((q^2-q+1)(q^2+q+1))
    y_(1^3)  = q^2 (z-q)(q^2 z + z - q^3) / ((q^2+1)(q^2-q+1)(q^2+q+1))

`y_(1^3)` reproduces the 2026-08-26 audit's independently-derived form exactly.

**The Frobenius Gram on the NF basis is the Wedderburn product.**  Measured, not
assumed: with `d_lambda = 1, 2, 1`,

    det G(u) / ( y_(3) * y_(2,1)^4 * y_(1^3) ) |_{z=z_C}
        = -(u^4+1)^2 (u^2-u+1)^6 (u^2+u+1)^6 (u^4-u^2+1)^6 / u^28

which has **no positive real zero and no positive real pole**.  So on `u > 0`
every degeneracy of the corpus Gram IS a Wedderburn weight vanishing, and the
recorded factorisation is explained:

    (u^3+u-1)^5   <=>  z_C = q      kills y_(2,1) (power 4) and y_(1^3) (1)
    (u^3+u^2+1)^5 <=>  z_C = -1/q   kills y_(2,1) (power 4) and y_(3)   (1)
    (u-1)                           kills y_(1^3) at q = 1

The multiplicity 5 is `d^2` bookkeeping, not a coincidence: each condition hits
5 of the 6 dimensions of the regular representation.

## What that does to the melt

`y_(2,1)(z) = 0` has exactly two roots, `z = q` and `z = -1/q`.  Substituting
the two conventions:

  * **Convention C.**  `z_C = q` is `u^3+u-1 = 0` (`u = 1/psi`, `q = 1/psi^2 =
    0.46557`), and `z_C = -1/q` is `u^3+u^2+1 = 0` (real root `u = -psi`, outside
    `u > 0`).  So there IS a single positive-`q` degeneracy, at `q ~ 0.4656`, and
    `y_(2,1)` is NEGATIVE below it and positive above.

  * **Convention D (canonical).**  `z_D = q` forces `q = 0`; `z_D = -1/q` forces
    `q^4+q^2+1 = 0`.  **Neither has a real solution.**  Directly,

        y_(2,1)(z_D) = q^2/(q^2+1)^2        > 0 for every real q != 0
        y_(1^3)(z_D) = 0                     identically  (the D radical)
        y_(3)(z_D)   = (q^4+1)/(q^2+1)^2    > 0
        sum: y_(3) + 2 y_(2,1) + y_(1^3) = 1  exactly

Both of `...-melt.md`'s claims are wrong about the convention-C theorem it sits
beside — the threshold is `q = 1/psi^2`, not `q = psi`, and the melt is
approached by LOWERING `q`, not by heating past it — and under the canonical
convention the transition **does not exist at any real q**.

`y_(1^3)(z_D) = 0` is the same fact as `gramMatrixD_det_eq_zero`: D's Gram is
identically singular because it annihilates the antisymmetric block.  That is
why the D determinant cannot be used to locate a transition, and why the
question has to be asked of the *block weight*, which is a perfectly good
non-degenerate object under D.

## Scope

**Scope-(b) for the specific claim**, with the invariant cited: the (2,1)
Wedderburn weight cannot vanish at any real `q` under convention D, because
`y_(2,1)(z_D) = q^2/(q^2+1)^2` is a manifestly positive rational function.

**Scope-(a) for "there is no hadronic melt"**: this excludes the Wedderburn /
Gram-degeneracy route only.  A transition produced by some other mechanism —
an SDP feasibility boundary not driven by block-weight vanishing, a
higher-`n` block, an archimedean bound — is untouched.

Three different points are called "the supergolden" in this corpus and they are
not the same place:  `u = 1/psi` (Gram, convention C);  `q = psi` (`z_D = 1`,
where the Markov trace collapses onto the counit);  `u = -psi` (`detFactor4`,
outside the regime).  Same algebraic number, three roles.

Run:  python3 -u computations/hecke/h3_gram_degeneracy_is_wedderburn_weight_vanishing.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
mp.mp.dps = 50

u = sp.Symbol("u", positive=True)   # u = sqrt(q); the corpus Gram's variable
q = u ** 2
z = sp.Symbol("z")                  # FREE Markov loop parameter

Z_C = u / (u ** 2 + 1)              # sqrt(q)/(q+1)
Z_D = q ** 3 / (q ** 2 + 1)


def wedderburn_weights():
    """Solve tr_M = sum_lambda y_lambda chi^lambda on H_3(q) with z free.

    Uses the Hoefsmit seminormal (2,1) representation for chi^(2,1); the two
    one-dimensional characters are sigma -> q and sigma -> -1/q.
    """
    h = q - 1 / q
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    s1 = sp.Matrix([[q, 0], [0, -1 / q]])
    s2 = sp.Matrix([[d2, b], [b, d1]])
    braid_ok = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2, 2)

    chi21 = (sp.Integer(2), sp.simplify(sp.trace(s1)), sp.simplify(sp.trace(s1 * s2)))
    y3, y21, y111 = sp.symbols("y3 y21 y111")
    eqs = [
        sp.Eq(y3 * 1 + y21 * chi21[0] + y111 * 1, 1),
        sp.Eq(y3 * q + y21 * chi21[1] + y111 * (-1 / q), z),
        sp.Eq(y3 * q ** 2 + y21 * chi21[2] + y111 * q ** -2, z ** 2),
    ]
    sol = sp.solve(eqs, [y3, y21, y111], dict=True)[0]
    return (sp.cancel(sp.simplify(sol[y3])),
            sp.cancel(sp.simplify(sol[y21])),
            sp.cancel(sp.simplify(sol[y111])),
            braid_ok, chi21, h)


def main() -> int:
    Y3, Y21, Y111, braid_ok, chi21, h = wedderburn_weights()
    checks: list[tuple[str, bool, str]] = []

    def chk(name: str, ok: bool, why: str) -> None:
        checks.append((name, bool(ok), why))

    chk("seminormal_braid_relation", braid_ok,
        "sigma_1 sigma_2 sigma_1 = sigma_2 sigma_1 sigma_2 on V_(2,1)")
    chk("chi21_sigma_is_h", sp.simplify(chi21[1] - h) == 0,
        "chi^(2,1)(sigma) = q - 1/q = h")
    chk("chi21_sigma1sigma2_is_minus_one", sp.simplify(chi21[2] + 1) == 0,
        "chi^(2,1)(sigma_1 sigma_2) = -1")

    # --- the weights reproduce the 2026-08-26 audit's independent y_(1^3) ---
    audit_y111 = (-q ** 2 * (q - z) * (q ** 2 * z + z - q ** 3)
                  / ((q ** 2 + 1) * (q ** 2 - q + 1) * (q ** 2 + q + 1)))
    chk("y111_matches_2026_08_26_audit", sp.simplify(Y111 - audit_y111) == 0,
        "independent re-derivation of y_(1^3)(z) agrees exactly")
    chk("weights_sum_to_one", sp.simplify(Y3 + 2 * Y21 + Y111 - 1) == 0,
        "y_(3) + 2 y_(2,1) + y_(1^3) = 1 for every z (Markov normalisation)")

    # --- y_(2,1) roots in z ---
    y21_num = sp.numer(sp.together(Y21))
    roots_z = sp.solve(sp.Eq(y21_num, 0), z)
    chk("y21_roots_are_q_and_minus_inv_q",
        set(sp.simplify(r) for r in roots_z) == {sp.simplify(q), sp.simplify(-1 / q)},
        f"y_(2,1) = 0 iff z = q or z = -1/q; got {roots_z}")

    # --- the Gram determinant IS the Wedderburn product (measured) ---
    S1 = u ** 6 - u ** 5 + u ** 4 - u ** 3 + 2 * u ** 2 - u + 1
    S2 = u ** 6 + u ** 5 + 2 * u ** 4 + u ** 3 + u ** 2 + u + 1
    det_corpus = -((u - 1) * (u + 1) * (u ** 3 + u - 1) ** 5
                   * (u ** 3 + u ** 2 + 1) ** 5 * S1 * S2) / (u ** 10 * (u ** 2 + 1) ** 12)
    pred = sp.cancel(sp.together((Y3 * Y21 ** 4 * Y111).subs(z, Z_C)))
    ratio = sp.factor(sp.cancel(det_corpus / pred))
    rnum, rden = sp.fraction(sp.together(ratio))

    def pos_real_roots(poly):
        return [r for r in sp.real_roots(sp.Poly(poly, u)) if r > 0]

    chk("gram_det_is_wedderburn_product_no_pos_zeros",
        not pos_real_roots(rnum) and not pos_real_roots(rden),
        f"det G / (y3 y21^4 y111) = {sp.sstr(ratio)} — no positive real zero or pole, "
        "so on u>0 every Gram degeneracy is a weight vanishing")

    # --- convention C: the two nontrivial det factors ARE the y_(2,1) roots ---
    f3 = sp.factor(sp.numer(sp.together(sp.simplify(Z_C - q))))
    f4 = sp.factor(sp.numer(sp.together(sp.simplify(Z_C + 1 / q))))
    chk("detFactor3_is_zC_eq_q", sp.simplify(sp.cancel(f3 / (u ** 3 + u - 1)) - (-u)) == 0,
        f"z_C = q  <=>  u(u^3+u-1) = 0   [corpus detFactor3]; got {sp.sstr(f3)}")
    chk("detFactor4_is_zC_eq_minus_inv_q",
        sp.simplify(f4 - (u ** 3 + u ** 2 + 1)) == 0,
        f"z_C = -1/q  <=>  u^3+u^2+1 = 0  [corpus detFactor4]; got {sp.sstr(f4)}")

    # --- convention D: no degeneracy at all ---
    y21D = sp.cancel(sp.simplify(Y21.subs(z, Z_D)))
    y111D = sp.cancel(sp.simplify(Y111.subs(z, Z_D)))
    y3D = sp.cancel(sp.simplify(Y3.subs(z, Z_D)))
    chk("y21_at_zD_closed_form",
        sp.simplify(y21D - q ** 2 / (q ** 2 + 1) ** 2) == 0,
        "y_(2,1)(z_D) = q^2/(q^2+1)^2 — manifestly positive, never zero")
    chk("y111_at_zD_vanishes_identically", sp.simplify(y111D) == 0,
        "y_(1^3)(z_D) = 0 for every q — the D radical / TL quotient")
    chk("y3_at_zD_closed_form",
        sp.simplify(y3D - (q ** 4 + 1) / (q ** 2 + 1) ** 2) == 0,
        "y_(3)(z_D) = (q^4+1)/(q^2+1)^2")
    chk("zD_eq_q_has_no_positive_solution",
        sp.solve(sp.Eq(Z_D, q), u) == [],
        "z_D = q forces q = 0")
    chk("zD_eq_minus_inv_q_has_no_real_solution",
        sp.solve(sp.Eq(Z_D, -1 / q), u) == [],
        "z_D = -1/q forces q^4+q^2+1 = 0, no real root")

    # --- the melt DIRECTION under C, numerically at 50 dps ---
    psi = mp.findroot(lambda x: x ** 3 - x ** 2 - 1, mp.mpf("1.4"))
    u_th = 1 / psi
    q_th = u_th ** 2
    y21C = sp.lambdify(u, sp.simplify(Y21.subs(z, Z_C)), "mpmath")
    below = y21C(u_th * mp.mpf("0.9"))
    at = y21C(u_th)
    above = y21C(u_th * mp.mpf("1.1"))
    q0 = mp.mpf("1.1099785827513808")   # proton pin
    at_q0 = y21C(mp.sqrt(q0))
    chk("melt_is_below_not_above", below < 0 < above and abs(at) < mp.mpf("1e-40"),
        f"y_(2,1)(z_C) < 0 for u < 1/psi and > 0 for u > 1/psi "
        f"(below={mp.nstr(below,10)}, above={mp.nstr(above,10)})")
    chk("substrate_is_on_the_stable_side", at_q0 > 0,
        f"y_(2,1)(z_C) = {mp.nstr(at_q0,12)} > 0 at the proton pin q0")
    chk("threshold_q_is_inv_psi_squared_not_psi",
        abs(q_th - mp.mpf(1) / (psi * psi)) < mp.mpf("1e-45") and q_th < 1 < psi,
        f"threshold in q is 1/psi^2 = {mp.nstr(q_th,20)}, NOT psi = {mp.nstr(psi,20)}")

    # --- the third supergolden location: z_D = 1 (trace collapses onto counit) ---
    chk("zD_eq_one_is_q_eq_psi",
        sp.factor(sp.numer(sp.together(sp.simplify(Z_D - 1)))) == sp.factor(u ** 6 - u ** 4 - 1),
        "z_D = 1  <=>  q^3 = q^2+1  <=>  q = psi — a DIFFERENT point from u = 1/psi")
    chk("zC_never_reaches_one",
        sp.solve(sp.Eq(Z_C, 1), u) == [],
        "z_C = u/(u^2+1) <= 1/2 for all u>0, so eps = tr_M is unreachable under C at any q")

    npass = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{'=' * 78}\nH_3 Gram degeneracy = Wedderburn weight vanishing\n{'=' * 78}")
    print(f"\n  y_(3)   = {sp.sstr(Y3)}")
    print(f"  y_(2,1) = {sp.sstr(Y21)}")
    print(f"  y_(1^3) = {sp.sstr(Y111)}")
    print(f"\n  det G / (y3 y21^4 y111) = {sp.sstr(ratio)}")
    print(f"\n  at z_D:  y_(3) = {sp.sstr(y3D)}   y_(2,1) = {sp.sstr(y21D)}   "
          f"y_(1^3) = {sp.sstr(y111D)}")
    print(f"\n  psi = {mp.nstr(psi, 20)}")
    print(f"  convention-C threshold:  u = 1/psi = {mp.nstr(u_th, 20)}  "
          f"=>  q = {mp.nstr(q_th, 20)}")
    print(f"  y_(2,1) at proton pin q0 = {mp.nstr(at_q0, 12)}  (stable side)\n")
    for name, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {why}")
    print(f"\n  {npass}/{len(checks)} assertions passed\n")

    w = WitnessBuilder("h3-gram-degeneracy-is-wedderburn-weight-vanishing",
                       engine="python+sympy+mpmath", output_dir=HERE,
                       _script_path=__file__)
    w.set_description(
        "The convention-C H_3 Gram determinant's recorded factorisation is "
        "explained: det G = [unit on u>0] * y_(3) * y_(2,1)^4 * y_(1^3), so every "
        "positive-u degeneracy is a Wedderburn weight vanishing and the "
        "multiplicity-5 factors are d^2 bookkeeping. y_(2,1) = 0 iff z = q or "
        "z = -1/q; under convention C those are exactly detFactor3 (u^3+u-1) and "
        "detFactor4 (u^3+u^2+1). Under the canonical convention D neither has a "
        "real solution and y_(2,1)(z_D) = q^2/(q^2+1)^2 > 0, so the hadronic-melt "
        "degeneracy does not exist at any real q. Separately, "
        "spectrahedral-phase-collapse-melt.md misplaces the convention-C threshold "
        "(it says q = psi; the theorem gives u = 1/psi with u = sqrt(q), i.e. "
        "q = 1/psi^2) and inverts its direction (it says heated past; the weight "
        "goes negative BELOW).")
    w.set_content_block("prop:spectrahedral-phase-collapse")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why} for n, ok, why in checks])
    w.add_data("y_lambda_free_z", {"y_3": sp.sstr(Y3), "y_21": sp.sstr(Y21),
                                   "y_111": sp.sstr(Y111)})
    w.add_data("det_over_wedderburn_product", sp.sstr(ratio))
    w.add_data("at_convention_D", {"y_3": sp.sstr(y3D), "y_21": sp.sstr(y21D),
                                   "y_111": sp.sstr(y111D)})
    w.add_data("convention_C_threshold", {"u": mp.nstr(u_th, 30), "q": mp.nstr(q_th, 30),
                                          "psi": mp.nstr(psi, 30)})
    w.add_data("scope", (
        "Scope-(b) for 'the (2,1) Wedderburn weight cannot vanish at any real q "
        "under convention D', with the invariant cited: y_(2,1)(z_D) = "
        "q^2/(q^2+1)^2 is a manifestly positive rational function. Scope-(a) for "
        "'there is no hadronic melt' — this excludes the Wedderburn / "
        "Gram-degeneracy route only; a transition from some other mechanism is "
        "untouched."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save(extra={"q0Anchor": "independent",
             "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: Where the H_3(q) Gram degenerates, and whether the \"hadronic melt\" survives.",
             })
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
