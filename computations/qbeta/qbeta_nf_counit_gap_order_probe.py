"""The single-wrap/typed NF gap is O(h^3) — so it CANNOT reach the O(t^2)
acceptance test, and "basis-change" is the wrong name for it.

Bean `qou-pdix` (child of `qou-cds1`), following its last entry, which made the
NF question the gate on branch 3: *"A 0.16% phase cannot be derived from an
object whose NF convention is unsettled at 0.58%. Scope-(a): settle which NF is
canonical FIRST; settling it moves the target by more than the target."*

Two results, neither of which is in the corpus.

## 1. It is not a change of BASIS. It is two different ELEMENTS.

`docs/audits/2026-05-11-q-beta-residual-decomposition.md` labels the 1.00579
factor **"basis-change typed-vs-single-wrap"**. Its own §2 proves the dual-basis
identity `G^-1 . t = e_gamma`, i.e. *"the framework's net sum_i (Delta_NF)_i IS
the Frobenius counit eps(beta)"*.

Those two statements cannot both be about one element. `eps` is a canonical
algebra map, so it is **basis-independent**: expanding one element in two bases
gives one value of `eps`. The two NFs give

    single-wrap   eps(n-p) = h(h-2)/2
    typed 6-term  eps(n-p) = h(h^6+2h^5+2h^4+2h^3-h^2+2h-4)/4

which are different polynomials. Therefore they are expansions of **different
elements**, and the label in §1 is a category error against §2 of the same
document.

That reframes the open question. "Which NF is canonical" sounds like a
convention to be picked; it is actually "which braid element is the canonical
nucleon pair", which is a modelling question with a physical criterion.

## 2. The gap is O(h^3), so it cannot touch the t^1 or t^2 coefficients

Exact, and it reproduces the audit's 1.00579 to six digits:

    eps_typed - eps_sw = h^3 (h^4 + 2h^3 + 2h^2 + 2h - 1) / 4
                       = -h^3/4 + h^4/2 + h^5/2 + h^6/2 + O(h^7)

So the two NFs **agree through O(h^2)** and first differ at **O(h^3)**.

Bean entry (6) states the branch-3 acceptance test as: reproduce `alpha` through
order `t^2` in `q = 1 + t`, with the coefficient pinned at `t^1` so `t^2` is a
prediction. Since `h = 2t - t^2 + ...`, an `O(h^3)` gap is `O(t^3)` and
**contributes nothing to the `t^1` or `t^2` coefficients**.

**The NF ambiguity therefore does NOT gate the entry-6 acceptance test.** The
bean's magnitude argument is untouched and still correct for the absolute
0.160% target — 0.579% really is 3.6x larger — but a magnitude at q0 and an
order in the expansion are different claims, and only the latter governs which
Taylor coefficients an ambiguity can move.

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
    # in t, with q = 1 + t and h = q - 1/q
    h_of_t = sp.simplify((1 + t) - 1 / (1 + t))
    gap_t = sp.series(GAP.subs(h, h_of_t), t, 0, 4).removeO()
    for k in (1, 2):
        checks.append((
            f"gap_has_no_t{k}_term",
            sp.simplify(gap_t.coeff(t, k)) == 0,
            f"the NF gap contributes nothing at order t^{k} — so it cannot "
            f"move the entry-6 acceptance test",
        ))
    checks.append((
        "gap_first_appears_at_t3",
        sp.simplify(sp.series(GAP.subs(h, h_of_t), t, 0, 4).removeO().coeff(t, 3)) != 0,
        "first nonzero order in t is 3",
    ))

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

    npass = sum(1 for _, ok, _ in checks if ok)
    for n, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}: {why}")
    print(f"\n{npass}/{len(checks)} assertions pass")
    for k, v in numeric.items():
        print(f"  {k} = {v}")

    w = WitnessBuilder("qbeta-nf-counit-gap-order",
                       engine="python+sympy+mpmath", output_dir=HERE,
                       _script_path=__file__)
    w.set_description(
        "The single-wrap vs typed nucleon-NF counit gap is "
        "h^3(h^4+2h^3+2h^2+2h-1)/4, leading -h^3/4, so the two NFs agree "
        "through O(h^2) and the gap contributes nothing at order t^1 or t^2. "
        "It therefore cannot move the qou-pdix entry-6 branch-3 acceptance "
        "test, which pins at t^1 and predicts t^2. Separately: because the "
        "Frobenius counit is a canonical (basis-independent) map, two "
        "expansions of ONE element cannot give different eps, so the 1.00579 "
        "factor is NOT a 'basis-change' as labelled in the 2026-05-11 audit "
        "- the two NFs expand DIFFERENT ELEMENTS. That audit's own section 2 "
        "proves the net IS the counit, which is what makes the section 1 "
        "label a category error against it.")
    w.set_content_block("prop:q-beta-spectral-bridge")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why}
                          for n, ok, why in checks])
    w.add_data("numeric_at_proton_pin", numeric)
    w.add_data("verdict", (
        "The NF ambiguity is O(h^3) = O(t^3) and does NOT gate the entry-6 "
        "acceptance test. The bean's magnitude argument (0.579% vs a 0.160% "
        "target) is untouched and still correct for the ABSOLUTE target; a "
        "magnitude at q0 and an order in the expansion are different claims."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save()
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
