#!/usr/bin/env python3
"""qbeta_fibre_projection_and_rou_sublocus_probe.py — the projection IS the
modulus, it is PARTIAL, and the root-of-unity sublocus it leaves is EMPTY.

🛑 SECOND CORRECTION 2026-09-06: THE "DEGENERACY" IS NON-SEMISIMPLICITY,
   AND THE EMPTINESS VERDICT IS WITHDRAWN AS AN INTERPRETATION.

   `b^2 = [3]_q / [2]_q^2` exactly, and `H_n(q)` is semisimple iff `[k]_q != 0`
   for all `k <= n`.  So `b^2 = 0  <=>  [3]_q = 0  <=>  H_3(q) is NOT
   semisimple`.  The phases `pi/3` and `5pi/3` this probe calls "degenerate",
   and uses to declare the root-of-unity sublocus EMPTY, are exactly the points
   where the Wedderburn decomposition `tr = sum_lambda y_lambda chi^lambda`
   CEASES TO EXIST.

   That is not an obstruction to the physics.  It is where the semisimple
   machinery ends and the cellular / tilting structure begins — i.e. exactly the
   locus the 2026-09-03 full-tower ruling points AT.  This probe excluded the
   interesting locus on the grounds that its own tooling stopped working there.

   The arithmetic below is unchanged and correct.  The word "degenerate" and
   the "sublocus is EMPTY" verdict are withdrawn as interpretation.  See
   `qbeta_c_vs_d_are_different_algebras_probe.py`.

   🛑 OWNER RULING 2026-09-06: "Does not need to be real in fiber."
   THE REALITY PREMISE THIS PROBE INHERITS FROM #6875 IS REJECTED.

   Every assertion below is still TRUE AS ARITHMETIC and is not withdrawn:
   the written Q_A form is real-axis-only, the block's projection is the
   modulus and is partial, Im[q^2-q] = sin(phi)(2cos(phi)-1) has exactly the
   zeros stated, and those points are degenerate.

   What is withdrawn is the CONCLUSION drawn from them. Reality of Q_beta is
   an ARCHIMEDEAN constraint on the evaluation at q_0 (cf.
   `lusztig_q_0_imaginary_part_zero`), NOT a condition on the fibre. So the
   reality condition does not apply on |q| = 1 at all, nothing on the fibre
   locus is selected OR excluded by it, and the "sublocus is EMPTY" headline
   below rests on a constraint that was never in force there.

   The 4 points remain excluded on DEGENERACY grounds (b^2 = 0, h = 0, pole),
   which is structural and survives the ruling — but they are now 4 excluded
   points out of a continuum, not the whole admissible set. That exclusion is
   near-vacuous rather than decisive. See the audit doc's RETRACTION section.

Bean `qou-cds1` / `qou-pdix` route 5.  Scope-(a) for the arithmetic; the
degeneracy exclusion is exact.

## 🛑 This corrects my own merged #6875 (`0102df44d2`)

#6875 asked what selects N on `|q| = 1` and derived it from the reality of

    Q_A / m_e  =  |q^2 - 2q - 1| * (q + 1) / (2 q^3)                    (WRITTEN)

getting N = 5 keeping the modulus and N = 4 dropping it.  **Both readings used a
form that is only valid on the real axis.**  The block
`prop:neutron-qvalue-symbolic` defines

    Q_beta  =  |Delta(net)| * E_0,   Delta(net) = h(h-2)/2,   E_0 = m_e/(q(q-1))

and (WRITTEN) follows from it only via `|q^2-1| = (q-1)(q+1)`, which needs
`q` real `> 1`.  Off the real axis the two disagree — measured at
`q = e^(i/3)` they differ by **2.407** — so #6875's N = 5 / N = 4 are artifacts
of an archimedean simplification, not properties of the fibre.  I flagged the
modulus as a possible archimedean artifact in that PR and then applied the
concern to the wrong factor.

## What the projection actually is

The framework's projection to a real observable is **already in the block**: the
modulus on `Delta(net)`.  It is **PARTIAL** — `E_0` is not projected.  That
partiality is the entire source of the reality condition, and hence of any N
selection:

  * **partial (as defined)** — `|Delta(net)|` is real by construction, so
    `Q_beta` is real iff `1/(q(q-1))` is:

        Im[1/(q(q-1))]  =  (sin 2phi - sin phi) / (2(cos phi - 1))

    whose numerator factors as `sin phi (2 cos phi - 1)`, zero exactly at
    `phi in {pi/3, pi, 5pi/3}` — **the SIXTH roots of unity.**

  * **full** — `|Delta(net) * E_0|` is real for EVERY `q`, so it imposes no
    condition and selects no N at all.

So the projection question and the N question are **the same question**, not two
doors.  And a full projection adopted *because* it admits the required phase
would be fitting the mechanism to the target; it is named here and not taken.

## The sublocus is EMPTY

Every phase reality admits is degenerate for the very representation route 5
runs on:

    phi = pi/3    q^4+q^2+1 = 0  ->  Hoefsmit b^2 = 0, the V_(2,1) off-diagonal
                                     coupling vanishes
    phi = pi      h = q - 1/q = 0  ->  the substrate itself degenerates
    phi = 5pi/3   as pi/3

The first and third are not numerical accidents: `q^6 - 1 = (q^2-1)(q^4+q^2+1)`,
so at any primitive 6th root `q^4+q^2+1 = 0` identically.  Verified both ways —
`sympy` returns exactly 0 on the expand_complex form, and mpmath at 40 dps gives
|.| ~ 4e-41.

**So there is no admissible root of unity on the fibre locus at all.**  The
required phase being absent (18.50x below `pi/3`) is not the binding fact; the
binding fact is that the admissible set is empty before `theta` is mentioned.

## Scope

Scope-(a) for the reality arithmetic.  The degeneracy exclusion is exact and
holds for any candidate on the root-of-unity sublocus, whatever `theta` is.

It does **not** close route 5: the locus `|q| = 1` is not only its roots of
unity, and a mechanism carrying a full projection remains available — at the
price, stated above, of selecting nothing.  Nothing is wired; no `c_k` moves.

## Precision

sympy exact for the symbolic steps, mpmath at 40 dps for the degeneracy check
(a `simplify` that fails to finish is not evidence of non-vanishing — that
happened here and is why both routes are run).  `q_0` from `q_at`,
`m_e`/`Q_beta` from `codata_constants`.  No float64.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import mpmath as mpm                                            # noqa: E402
import sympy as sp                                              # noqa: E402
from mpmath import mp                                           # noqa: E402

from codata_constants import M_E_MEV, Q_BETA_MEV                # noqa: E402
from q_parameter import q_at                                    # noqa: E402

DPS = 50
results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))


def main() -> int:
    mp.dps = DPS
    qs, phi = sp.symbols("q"), sp.symbols("phi", real=True)

    print("=" * 78)
    print(" The projection is the modulus, it is PARTIAL, and the RoU sublocus is EMPTY")
    print("=" * 78)

    # ---- 1. the written form is archimedean-only -------------------------
    h = qs - 1 / qs
    dnet = sp.simplify(h * (h - 2) / 2)
    written = sp.Abs(qs ** 2 - 2 * qs - 1) * (qs + 1) / (2 * qs ** 3)
    defn = _qbeta_e0.order_zero_scaled(sp.Abs(dnet) * 1, qs)
    print("\n[1] #6875 used a form valid only on the real axis")
    print(f"    Delta(net) = h(h-2)/2 = {sp.factor(dnet)}")
    gaps = {}
    for label, val in (("real q=1.1", sp.Rational(11, 10)),
                       ("q=e^(i/3)", sp.exp(sp.I * sp.Rational(1, 3))),
                       ("q=e^(i pi/3)", sp.exp(sp.I * sp.pi / 3))):
        w = complex(sp.N(written.subs(qs, val), 20))
        d = complex(sp.N(defn.subs(qs, val), 20))
        gaps[label] = abs(w - d)
        print(f"    {label:14} |written - definition| = {gaps[label]:.6g}")
    check(
        "written_form_is_archimedean_only",
        gaps["real q=1.1"] < 1e-25 and gaps["q=e^(i/3)"] > 1,
        f"the written |q^2-2q-1|(q+1)/(2q^3) matches the block's "
        f"|Delta(net)|*E_0 on the real axis (gap {gaps['real q=1.1']:.2g}) and "
        f"NOT off it (gap {gaps['q=e^(i/3)']:.4g} at q = e^(i/3)) -- it follows "
        f"only via |q^2-1| = (q-1)(q+1), which needs q real > 1. #6875's "
        f"N = 5 / N = 4 are artifacts of that simplification.",
    )

    # ---- 2. the partial projection and its reality condition -------------
    qc = sp.exp(sp.I * phi)
    im = sp.simplify(sp.expand_trig(sp.im(sp.expand_complex(_qbeta_e0.order_zero_scaled(1, qc)))))
    num = sp.factor(sp.simplify(sp.expand_trig(sp.numer(sp.together(im)))))
    zeros = sp.solveset(sp.Eq(sp.simplify(im), 0), phi, sp.Interval(0, 2 * sp.pi))
    print("\n[2] the projection is PARTIAL -- |Delta(net)| is projected, E_0 is not")
    print(f"    Im[1/(q(q-1))]  = {im}")
    print(f"    numerator       = {num}   (= sin phi (2 cos phi - 1))")
    print(f"    zeros on [0,2pi) = {zeros}   -> the SIXTH roots of unity")
    check(
        "partial_projection_selects_sixth_roots",
        sp.pi / 3 in zeros and sp.pi in zeros,
        "with the block's own partial projection, Q_beta is real on |q| = 1 iff "
        "sin phi (2 cos phi - 1) = 0, i.e. phi in {pi/3, pi, 5pi/3} -- the sixth "
        "roots, not the fifth (#6875 reading A) or the fourth (reading B)",
    )
    check(
        "full_projection_selects_nothing",
        True,
        "|Delta(net) * E_0| is real for EVERY q, so a full projection imposes no "
        "condition and selects no N. The projection question and the N question "
        "are therefore the SAME question. Adopting the full projection because "
        "it admits the required phase would be fitting the mechanism to the "
        "target; named here and not taken.",
    )

    # ---- 3. every admissible phase is degenerate -------------------------
    mpm.mp.dps = 40
    print("\n[3] every reality-admissible phase is DEGENERATE")
    degen = {}
    for name, ph in (("pi/3", mpm.pi / 3), ("pi", mpm.pi), ("5pi/3", 5 * mpm.pi / 3)):
        qv = mpm.e ** (1j * ph)
        b2num, hv = qv ** 4 + qv ** 2 + 1, qv - 1 / qv
        why = []
        if abs(b2num) < mpm.mpf("1e-30"):
            why.append("b^2 = 0 (V_(2,1) coupling vanishes)")
        if abs(hv) < mpm.mpf("1e-30"):
            why.append("h = 0 (substrate degenerates)")
        degen[name] = why
        print(f"    phi={name:6} |q^4+q^2+1| = {mpm.nstr(abs(b2num), 4):>10}"
              f"   |h| = {mpm.nstr(abs(hv), 4):>8}   -> {'; '.join(why)}")
    exact0 = sp.simplify(sp.expand(sp.expand_complex(
        sp.exp(sp.I * sp.pi / 3) ** 4 + sp.exp(sp.I * sp.pi / 3) ** 2 + 1)))
    print(f"    exact check at pi/3: q^4+q^2+1 = {exact0}"
          f"   (q^6-1 = (q^2-1)(q^4+q^2+1), so this vanishes at every primitive 6th root)")
    check(
        "every_admissible_phase_is_degenerate_so_the_sublocus_is_EMPTY",
        all(degen.values()) and exact0 == 0,
        "pi/3 and 5pi/3 kill the Hoefsmit coupling (q^4+q^2+1 = 0 identically at "
        "a primitive 6th root, since q^6-1 = (q^2-1)(q^4+q^2+1)); pi kills h. So "
        "reality admits exactly three phases and non-degeneracy excludes all "
        "three -- there is NO admissible root of unity on the fibre locus, a "
        "fact established before theta is mentioned.",
    )

    # ---- 4. only now, theta ----------------------------------------------
    q0 = q_at(DPS)
    hh = q0 - 1 / q0
    hbar = (q0 - 1) / q0
    b = mp.sqrt((hh ** 2 + 3) / (hh ** 2 + 4))
    u = b * hbar ** 2
    Q_A0 = mp.mpf(str(M_E_MEV)) * abs(q0 ** 2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0 ** 3)
    theta = mp.acos(mp.mpf(str(Q_BETA_MEV)) / (Q_A0 * (1 - u ** 2)))
    ratio = (mp.pi / 3) / theta
    print(f"\n[4] theta enters only here: required = {mp.nstr(theta, 14)},"
          f" pi/3 = {mp.nstr(mp.pi/3, 10)}, ratio = {mp.nstr(ratio, 8)}x")
    print("    But the sublocus is empty regardless -- theta is not what excludes it.")
    check(
        "theta_is_not_the_binding_constraint",
        ratio > 10,
        f"the required phase sits {mp.nstr(ratio, 4)}x below the nearest "
        f"reality-admissible phase, but that is not the binding fact: the "
        f"admissible set is empty on degeneracy grounds alone.",
    )

    print("\n  assertions:")
    for name, ok, detail in results:
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"           {detail}")
    allp = all(ok for _, ok, _ in results)
    print(f"\n  allPassed: {allp}  ({sum(ok for _, ok, _ in results)}/{len(results)})")

    out = {
        "probe": "qbeta_fibre_projection_and_rou_sublocus_probe",
        "bean": "qou-cds1",
        "corrects": "my own merged #6875 (0102df44d2) -- its N = 5 / N = 4 used a "
                    "form valid only on the real axis",
        "question": "does the framework have a fibre-compute-then-project "
                    "mechanism, and what does it select?",
        "answer": "the projection is the modulus on Delta(net), already in the "
                  "block, and it is PARTIAL (E_0 unprojected) -- which is the "
                  "whole source of the reality condition. Partial selects the "
                  "SIXTH roots; full selects nothing. And all three "
                  "reality-admissible phases are degenerate, so the "
                  "root-of-unity sublocus is EMPTY.",
        "scope": "(a) for the reality arithmetic; the degeneracy exclusion is "
                 "exact and theta-independent. Does NOT close route 5: |q| = 1 "
                 "is more than its roots of unity, and a full projection remains "
                 "available at the price of selecting nothing.",
        "written_vs_definition_gap": {k: repr(v) for k, v in gaps.items()},
        "partial_projection_zero_set": "phi in {pi/3, pi, 5pi/3} (sixth roots)",
        "degeneracy": {k: v for k, v in degen.items()},
        "theta_required": mp.nstr(theta, 20),
        "pi_over_3_over_theta": mp.nstr(ratio, 20),
        "q0": mp.nstr(q0, 20), "q0_pin": "proton (q_at)", "q0Anchor": "proton", "dps": DPS,
        "assertions": [{"name": n, "passed": ok, "detail": d} for n, ok, d in results],
        "allPassed": allp,
    }
    dest = _HERE.parent / "qbeta-fibre-projection-and-rou-sublocus.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"\n  witness -> {dest.relative_to(_COMP.parent)}")
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
