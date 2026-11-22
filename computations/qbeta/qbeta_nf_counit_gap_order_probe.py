"""The NF gap is O(h^3) in the COUNIT and O(t) in ALPHA — the gate stands.

Bean `qou-pdix` (child of `qou-cds1`).

## RETRACTION of this probe's own first conclusion (same day)

This file first concluded: *"the NF ambiguity is O(t^3), so it does NOT gate the
entry-6 acceptance test."* **That is wrong, and the error is the interesting
part.** I proved a statement about the COUNIT `eps` and applied it to the PHASE
`alpha`. They are different functionals:

    alpha = (eps(n-p) - tr_M(n-p)) / 2          [bean entry (9)]

and only the `eps` half is insensitive. Measured, first nonzero order in `t`
with `q = 1 + t`, identical for BOTH conventions:

    eps   gap   t^3   (coeff -2)
    tr_M  gap   t^1   (coeff -1/4)
    ALPHA gap   t^1   (coeff  1/8)

**So the NF choice moves `alpha` at FIRST order and the bean's gate stands
exactly as written.** The bean was right; my correction of it was not.

## Why the two halves differ — this is the finding worth keeping

The counit sets every `z^k -> 1`. The Markov trace weights by `z^{#cr}`. The two
NFs differ precisely in the `L_+/L_-/e^-` coefficients, which carry crossing
numbers 2, 2, 3 — so under `eps` those differences cancel down to `O(h^3)`,
and under `tr_M` they survive at `O(t)` because each is weighted differently.

**The NF sensitivity of the phase lives entirely in the crossing-number
grading**, not in the algebra. That is a sharper statement of the gate than
"unsettled at 0.58%": it says WHERE the sensitivity is and why no re-basing of
the counit can remove it.

Corroboration that the machinery is right rather than merely self-consistent:
it reproduces bean entry (6) exactly, which was computed independently —
single-wrap C `alpha` coefficients `[-1/2, 1/4, -5/16]` (t^2 matches
`c*ln q`, t^3 does not) and single-wrap D `t^2 = 5/4` (does not match).

## What SURVIVES the retraction

1. **The closed form.** `eps_typed - eps_sw = h^3(h^4+2h^3+2h^2+2h-1)/4`,
   leading `-h^3/4`, reproducing the audit's 1.00579 to six digits. Verified
   twice; the Lean theorems are statements about `eps` only and are all correct.

2. **It is not a change of BASIS — it is two different ELEMENTS.**
   `docs/audits/2026-05-11-q-beta-residual-decomposition.md` §1 labels the
   1.00579 factor "basis-change typed-vs-single-wrap". Its own §2 proves the
   dual-basis identity `G^-1 . t = e_gamma`, i.e. *"the net IS the Frobenius
   counit"*. Those cannot both be about one element: `eps` is a canonical
   algebra map, hence basis-independent, so one element has one `eps`. The two
   NFs give different polynomials, so they expand DIFFERENT ELEMENTS and §1's
   label is a category error against §2 of the same document. Unaffected by the
   retraction, and it reframes the open question as *"which braid element is
   the canonical nucleon pair"* rather than a convention to be picked.

3. **The typed NF is worse, not better.** Switching to it does not repair the
   `t^3` mismatch; it destroys the `t^2` match that single-wrap C had:

       C single-wrap  [-1/2,  1/4, -5/16]   vs pred [-1/2,  1/4, -1/6]
       C typed        [-3/8, 11/16, -71/32] vs pred [-3/8,  3/16, -1/8]
       D single-wrap  [-1/2,  5/4, -1/2]    vs pred [-1/2,  1/4, -1/6]
       D typed        [-3/8, 19/16, -45/16] vs pred [-3/8,  3/16, -1/8]

   So single-wrap C remains the only combination matching `c*ln q` through
   `t^2`, and the recorded "tension with the ruling" is unchanged.

4. **The alpha-gap leading coefficient is 1/8 for BOTH conventions.** The NF
   sensitivity is convention-independent at leading order.

Run:  python3 -u computations/qbeta/qbeta_nf_counit_gap_order_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from q_parameter import q_at  # noqa: E402 — proton pin
from witness_base import WitnessBuilder  # noqa: E402

h = sp.Symbol("h")
t = sp.Symbol("t")

EPS_SW = h * (h - 2) / 2
EPS_TYPED = h * (h**6 + 2*h**5 + 2*h**4 + 2*h**3 - h**2 + 2*h - 4) / 4
GAP = sp.factor(sp.simplify(sp.expand(EPS_TYPED - EPS_SW)))


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    checks.append((
        "gap_closed_form",
        bool(sp.simplify(GAP - h**3 * (h**4 + 2*h**3 + 2*h**2 + 2*h - 1) / 4) == 0),
        "eps_typed - eps_sw = h^3 (h^4+2h^3+2h^2+2h-1)/4",
    ))
    checks.append((
        "gap_vanishes_to_order_three",
        sp.Poly(sp.expand(GAP * 4), h).monoms()[-1] == (3,),
        "lowest surviving power of h is 3: the two NFs agree through O(h^2)",
    ))
    checks.append((
        "gap_leading_coefficient_is_minus_quarter",
        bool(sp.limit(GAP / h**3, h, 0) == sp.Rational(-1, 4)),
        "leading term is -h^3/4",
    ))
    checks.append((
        "the_two_eps_differ",
        bool(sp.simplify(EPS_TYPED - EPS_SW) != 0),
        "different polynomials => (eps canonical) => DIFFERENT ELEMENTS, "
        "not two bases for one element",
    ))
    # in t, with q = 1 + t and h = q - 1/q: the COUNIT gap is O(t^3) ...
    h_of_t = sp.simplify((1 + t) - 1 / (1 + t))
    gap_t = sp.series(GAP.subs(h, h_of_t), t, 0, 4).removeO()
    for k in (1, 2):
        checks.append((
            f"counit_gap_has_no_t{k}_term",
            sp.simplify(gap_t.coeff(t, k)) == 0,
            f"the COUNIT gap contributes nothing at order t^{k}",
        ))
    checks.append((
        "counit_gap_first_appears_at_t3",
        sp.simplify(gap_t.coeff(t, 3)) != 0,
        "counit gap first nonzero order in t is 3",
    ))

    # ... but ALPHA = (eps - tr_M)/2, and the tr_M half is NOT insensitive.
    z = sp.Symbol("z")
    CR = [0, 1, 1, 2, 2, 3]          # crossing numbers of [γ,σ₀,σ₁,L₊,L₋,e⁻]
    TYPED = [h*(2*h**4 + h**2 - 2)/4,
             h**2*(h**2 + 1)*(2*h**2 + 1)/4,
             h**2*(h**2 - h + 1)*(h**2 + h + 1)/4,
             -h**5/4,
             h*(h**2 + 1)*(h**4 - 2)/4,
             -h**4*(h**2 + 2)/4]
    SW = [h**2/2, -h/2, -h/2, 0, 0, 0]
    tr = lambda v: sp.expand(sum(c * z**k for c, k in zip(v, CR)))
    ep = lambda v: sp.expand(sum(v))
    checks.append(("typed_eps_matches_recorded_vector",
                   bool(sp.simplify(ep(TYPED) - EPS_TYPED) == 0),
                   "the typed 6-term vector sums to the recorded eps_typed"))
    checks.append(("single_wrap_eps_matches_recorded_vector",
                   bool(sp.simplify(ep(SW) - EPS_SW) == 0),
                   "the single-wrap vector sums to the recorded eps_sw"))

    q_t = 1 + t
    zC, zD = sp.sqrt(q_t)/(q_t + 1), q_t**3/(q_t**2 + 1)

    def first_order(e, zv):
        ser = sp.expand(sp.series(sp.simplify(e.subs({z: zv, h: h_of_t})),
                                  t, 0, 5).removeO())
        for k in range(6):
            c = sp.simplify(ser.coeff(t, k))
            if c != 0:
                return k, sp.nsimplify(c)
        return None, 0

    alpha_gap = (ep(TYPED) - tr(TYPED)) / 2 - (ep(SW) - tr(SW)) / 2
    trm_gap = tr(TYPED) - tr(SW)
    for nm, zv in (("C", zC), ("D", zD)):
        k, c = first_order(trm_gap, zv)
        checks.append((f"trM_gap_reaches_t1_{nm}", k == 1,
                       f"the tr_M half of the gap is O(t), coeff {c} "
                       f"— NOT O(t^3)"))
        k, c = first_order(alpha_gap, zv)
        checks.append((f"alpha_gap_reaches_t1_{nm}", k == 1 and c == sp.Rational(1, 8),
                       f"ALPHA moves at FIRST order, coeff {c} — the bean's "
                       f"gate stands; this probe's first conclusion was wrong"))

    # reproduce bean entry (6) independently: single-wrap C matches c*ln q at t^2
    def alpha_coeffs(v, zv):
        a = sp.simplify((ep(v) - tr(v)) / 2)
        ser = sp.expand(sp.nsimplify(sp.series(a.subs({z: zv, h: h_of_t}),
                                               t, 0, 5).removeO()))
        return [sp.nsimplify(sp.simplify(ser.coeff(t, k))) for k in (1, 2, 3)]

    cC = alpha_coeffs(SW, zC)
    checks.append(("reproduces_bean_entry6_singlewrap_C",
                   cC == [sp.Rational(-1, 2), sp.Rational(1, 4), sp.Rational(-5, 16)],
                   "single-wrap C alpha = [-1/2, 1/4, -5/16], matching bean "
                   "entry (6) computed independently"))
    cD = alpha_coeffs(SW, zD)
    checks.append(("reproduces_bean_entry6_singlewrap_D_t2",
                   cD[1] == sp.Rational(5, 4),
                   "single-wrap D alpha t^2 = 5/4, matching bean entry (6)"))
    cCt = alpha_coeffs(TYPED, zC)
    checks.append(("typed_C_destroys_the_t2_match",
                   cCt[1] != -cCt[0] / 2,
                   f"typed C alpha t^2 = {cCt[1]} against c*ln q prediction "
                   f"{-cCt[0]/2}: the typed NF is WORSE, not better"))

    # numerics at the proton pin — reproduce the audit's 1.00579
    import mpmath as mp
    mp.mp.dps = 50
    q0 = mp.mpf(str(q_at()))
    hm = q0 - 1 / q0

    def ev(e):
        return mp.mpf(str(sp.N(e.subs(h, sp.Float(str(hm), 50)), 50)))

    a, b = ev(EPS_SW), ev(EPS_TYPED)
    ratio = b / a
    checks.append((
        "reproduces_audit_ratio_1_00579",
        bool(abs(ratio - mp.mpf("1.00579")) < mp.mpf("1e-5")),
        "matches docs/audits/2026-05-11-q-beta-residual-decomposition.md §1",
    ))
    numeric = {
        "q0_proton_pin": mp.nstr(q0, 30),
        "h_at_q0": mp.nstr(hm, 30),
        "eps_single_wrap": mp.nstr(a, 20),
        "eps_typed": mp.nstr(b, 20),
        "ratio_typed_over_single_wrap": mp.nstr(ratio, 20),
        "relative_gap": mp.nstr((b - a) / a, 20),
        "gap_closed_form": str(GAP),
    }

    # ---- what each (NF, convention) cell implies for the required N=1 factor
    REQ = mp.mpf("0.99839767")          # bean entry (8)
    zCv, zDv = mp.sqrt(q0) / (q0 + 1), q0**3 / (q0**2 + 1)
    cells = {}
    for nfn, v in (("single_wrap", SW), ("typed", TYPED)):
        for cn, zv in (("C", zCv), ("D", zDv)):
            a = (ep(v) - tr(v)) / 2
            av = mp.mpf(str(sp.N(a.subs({h: sp.Float(str(hm), 50),
                                         z: sp.Float(str(zv), 50)}), 50)))
            cells[f"{nfn}_{cn}"] = {
                "alpha": mp.nstr(av, 12),
                "cos_alpha": mp.nstr(mp.cos(av), 12),
                "unexplained_fraction_of_required_correction":
                    mp.nstr((mp.cos(av) - REQ) / (1 - REQ), 8),
            }
    checks.append((
        "all_four_cells_undercorrect",
        all(mp.mpf(c["unexplained_fraction_of_required_correction"]) > 0
            for c in cells.values()),
        "every (NF, convention) cell leaves part of the required 0.160% "
        "correction unexplained — none overshoots",
    ))
    checks.append((
        "canonical_choices_are_the_worst_cell",
        (mp.mpf(cells["typed_D"]["unexplained_fraction_of_required_correction"])
         == max(mp.mpf(c["unexplained_fraction_of_required_correction"])
                for c in cells.values())),
        "typed NF (what the live mass compute uses) + convention D (the "
        "2026-08-15 owner ruling) is the WORST of the four cells",
    ))
    numeric_cells = cells

    npass = sum(1 for _, ok, _ in checks if ok)
    for n, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}: {why}")
    print(f"\n{npass}/{len(checks)} assertions pass")
    for k, v in numeric.items():
        print(f"  {k} = {v}")
    print("\n  cell            alpha           cos(alpha)      unexplained")
    for k, v in numeric_cells.items():
        print(f"  {k:<15} {v['alpha']:>14} {v['cos_alpha']:>15} "
              f"{v['unexplained_fraction_of_required_correction']:>13}")

    w = WitnessBuilder("qbeta-nf-counit-gap-order",
                       engine="python+sympy+mpmath", output_dir=HERE,
                       _script_path=__file__)
    w.set_description(
        "RETRACTION-CARRYING. The single-wrap vs typed nucleon-NF COUNIT gap is "
        "h^3(h^4+2h^3+2h^2+2h-1)/4, leading -h^3/4, so the two NFs agree "
        "through O(h^2). BUT alpha = (eps - tr_M)/2 and the tr_M half is NOT "
        "insensitive: the tr_M gap is O(t) and the ALPHA gap is O(t) with "
        "coefficient 1/8 in BOTH conventions, so the NF choice moves the phase "
        "at FIRST order and the qou-pdix gate STANDS. This probe's first "
        "conclusion (that the gap could not move the entry-6 test) is "
        "RETRACTED. The sensitivity lives in the crossing-number grading: eps "
        "sets z^k -> 1 and the L/e differences cancel; tr_M weights by z^#cr "
        "and they survive. Separately: because the "
        "Frobenius counit is a canonical (basis-independent) map, two "
        "expansions of ONE element cannot give different eps, so the 1.00579 "
        "factor is NOT a 'basis-change' as labelled in the 2026-05-11 audit "
        "- the two NFs expand DIFFERENT ELEMENTS. That audit's own section 2 "
        "proves the net IS the counit, which is what makes the section 1 "
        "label a category error against it.")
    w.set_content_block("conj:q-beta-spectral-bridge")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why}
                          for n, ok, why in checks])
    w.add_data("numeric_at_proton_pin", numeric)
    w.add_data("nf_convention_cells_vs_required_N1", numeric_cells)
    w.add_data("verdict", (
        "GATE STANDS. The counit gap is O(t^3) but the ALPHA gap is O(t) with "
        "coefficient 1/8 in both conventions, because alpha = (eps - tr_M)/2 "
        "and tr_M weights by z^#cr where eps sets z^k -> 1. The bean was right "
        "and this probe's first conclusion was wrong. Surviving: the exact "
        "closed form; that the 1.00579 is NOT a basis change (eps is canonical, "
        "so different eps => different ELEMENTS); and that the typed NF is "
        "worse, destroying single-wrap C's t^2 match rather than repairing t^3."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save()
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
