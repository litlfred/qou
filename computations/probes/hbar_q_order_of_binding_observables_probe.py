#!/usr/bin/env python3
"""The ℏ_q classification of the binding observables — and one of them fails it.

WHY THIS EXISTS
---------------
`qou-ap3d`/`qou-ssz6` disqualified `log Z(3A)` as a binding magnitude by a
scale-free test: it does not vanish as `q → 1`, where every *energy* in the
framework does. I then asserted that the ℏ_q-suppressed observables — `Δ(net)`
and the trace differences — "do vanish classically and do pair with `E_0`
consistently", and recommended the lane go there.

**Measured, that is half wrong, and the half that fails is the one the binding
chain actually uses.** This probe classifies all three by the same test.

THE CLASSIFICATION
------------------
Leading order in `ℏ_q = (q−1)/q`, by log–log slope along `q = exp(η)` with
`η` swept over four decades (`η` is the substrate's own parameter, and
`q = exp η` sidesteps `reject_float64_q`, which refuses float64-round-trippable
sweep values):

    observable                          classical floor    deformation order
    ------------------------------------------------------------------------
    Δ(net) = h(h−2)/2,  h = q − 1/q     0 (exact)          ℏ_q^1
    Plancherel block sum (D, ⁴He, ¹²C)  0 (exact)          ℏ_q^2
    tr_M(W_free) − tr_M(W_atom)         **NONZERO**        ℏ_q^1

The first two pass. The third does not:

    deuteron   →  1/8   = 0.125      exactly    [assertion 1]
    ⁴He        →  7/128 = 0.0546875  exactly    [assertion 2]

extrapolated to `1.3e-10` and `3.0e-10`. Both are simple dyadic rationals, which
is not what a numerical artefact looks like. The deviation from the floor is
`ℏ_q^1` in both cases (`1.00078`, `1.0021`) [assertion 3].

WHAT THAT MEANS
---------------
At `q = 1` the Hecke algebra degenerates to `ℂ[S_n]` and there is no deformation
left. `Δ(net)` and the block sum both vanish there — they are pure deformation
observables. The trace difference does not: it returns a **topological**
remainder, the part of `tr_M(W_free) − tr_M(W_atom)` that survives when the
braiding is switched off, because the free word and the atom word close to
different links regardless of `q`.

So the trace difference is **not one quantity but two**, at different orders:

    tr_M(W_free) − tr_M(W_atom)  =  c₀  +  c₁·ℏ_q + O(ℏ_q²)

and at `q₀` the classical part is **22.46 %** of it for the deuteron, 4.88 % for
⁴He [data]. Whatever binding energy is read off this observable, that fraction of
it is present in a framework with no deformation at all.

THE REGISTRY'S ℏ_q INDEX IS WRONG FOR IT
------------------------------------------
`derivation_chain.E_0_CONVENTIONS["B_q_value_absorbed"]` states its operator
class as

> "Atom-level binding B(Z,N) = E_0·(|tr_M(W_free)| − |tr_M(W_atom)|) at H_{3A}.
>  **The trace-difference operator carries the ℏ_q² scaling**; E_0 is the
>  unit-action scale."

Measured, it carries neither: there is an `ℏ_q^0` floor, and the leading
*deformation* term is `ℏ_q^1`, not `ℏ_q^2`. That matters because the registry's
`ℏ_q` index is exactly what selects the `E_0` convention, and it is what the
"≈ 102× error" warning is computed from (bean `qou-59j5`).

Consequences, in increasing order of how much they should worry a reader:

1. `B = E_0^{(B)}·(tr_free − tr_atom)` totals `ℏ_q^0`, not `ℏ_q^2`. It predicts
   nonzero deuteron binding at `q = 1`: `0.78233 × 1/8 = 0.0978 MeV`.
2. Strip the floor and the deformation part is `ℏ_q^1`, which pairs with
   convention **A** (`ℏ_q^1`) to total `ℏ_q^2` — the same total as `Δ(net)×A`.
   So on ℏ_q grounds A is the consistent pairing for the *deformation* part,
   while the registry's rule says atom level MUST use B.
3. Neither convention pairs consistently with the observable *as a whole*,
   because its two parts sit at different orders. No single scale can.

AND TWO LIVE PRODUCERS ALREADY DISAGREE ABOUT WHICH ONE TO USE
----------------------------------------------------------------
On the identical quantity `tr_M(W_free) − tr_M(W_atom)`:

* `binding_canonical.binding_canonical` uses **convention B**:
  `B = Q_β(n)·Δtr` with `Q_beta_n_MeV = 0.78233340931`, commented in the source
  as "Q_β(n) is the MeV-dimensioned multiplier of the dimensionless trace
  difference". For the deuteron that is `0.78233 × 0.556545 = 0.4354 MeV`
  against AME `2.2246` — **5.11× short**.
* `derive_binding_chain_cooperative.bond_binding` uses **convention A**:
  `B_xy = E_0·(tr_free − tr_atom)` with `E_0 = m_e/(q₀(q₀−1)) = 4.18598`. Same
  Δtr, `4.18598 × 0.556545 = 2.3296 MeV`.

A factor of **5.35** apart — `E_0^{(A)}/E_0^{(B)}` — on the same trace
difference, in two live producers. This is the `E_0`-convention collision
`qou-59j5` catalogued, found in the wild rather than in a registry.

WHAT SURVIVES, AND IT IS THE POINT
-----------------------------------
`Δ(net)` passes cleanly: exactly `ℏ_q^1`, no floor, and paired with convention A
it totals `ℏ_q^2` and predicts `Q_β` to 0.168 %. The Plancherel block sum passes
too (`ℏ_q^2`, no floor). **The ℏ_q-suppressed route is not refuted** — my
recommendation was right about the category and wrong about one member of it.
What this probe removes is the assumption that the trace difference belongs to
that category without checking.

Usage:
    python3 computations/probes/hbar_q_order_of_binding_observables_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import b_over_a_evaluator as BOA  # noqa: E402
import tr_m_atom_via_transfer as TR  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60

# Convention values, quoted from the producers that use them.
E0_A_MEV = "4.18598136329447"        # derive_binding_chain_cooperative
E0_B_MEV = "0.78233340931"           # binding_canonical's Q_beta_n_MeV
AME_B_DEUTERON = mp.mpf("2.22456637")


def hbar_of_eta(eta) -> mp.mpf:
    q = mp.exp(mp.mpf(eta))
    return (q - 1) / q


def trace_difference(Z: int, N: int, eta) -> mp.mpf:
    """`tr_M(W_free) − tr_M(W_atom)` at `q = exp(η)`.

    Swept in `η` rather than in `q` directly: `reject_float64_q` refuses any `q`
    reproducible from its own float64, which is every round decimal. `exp(η)`
    for a decade `η` is a genuine 60-dps value, so the guard is satisfied rather
    than bypassed — no `allow_float64` override is used anywhere here.
    """
    ta, tf, _chi, _w = TR.tr_m_atom_zn(Z, N, dps=60, q=mp.exp(mp.mpf(eta)))
    return tf - ta


def classical_floor_and_order(Z: int, N: int) -> tuple[mp.mpf, mp.mpf, list]:
    """Richardson-extrapolate the `η → 0` limit, then the deviation's order."""
    etas = ["1e-3", "1e-4", "1e-5", "1e-6"]
    rows = [(mp.mpf(e), trace_difference(Z, N, e), hbar_of_eta(e)) for e in etas]
    (_, d1, h1), (_, d2, h2) = rows[-2], rows[-1]
    c0 = (d2 * h1 - d1 * h2) / (h1 - h2)          # first-order Richardson
    (_, da, ha), (_, db, hb) = rows[0], rows[-1]
    order = (mp.log(abs(da - c0)) - mp.log(abs(db - c0))) / (mp.log(ha) - mp.log(hb))
    return c0, order, rows


def loglog_order(f, e1="1e-3", e2="1e-6") -> mp.mpf | None:
    v1, v2 = abs(mp.mpf(f(e1))), abs(mp.mpf(f(e2)))
    if v1 == 0 or v2 == 0:
        return None
    return ((mp.log(v1) - mp.log(v2))
            / (mp.log(hbar_of_eta(e1)) - mp.log(hbar_of_eta(e2))))


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    w = WitnessBuilder("hbar-q-order-of-binding-observables-probe")
    w.set_description(
        "Classifies the framework's binding observables by their behaviour as q -> 1. "
        "Delta(net) and the Plancherel block sum vanish (hbar_q^1 and hbar_q^2). The signed "
        "trace difference does NOT: it has an exact dyadic classical floor (1/8 at the "
        "deuteron, 7/128 at 4He) plus an hbar_q^1 deformation, so the E_0 registry's "
        "'carries the hbar_q^2 scaling' is wrong for it and no single E_0 convention pairs "
        "with it consistently."
    )

    # ---- assertions 1 & 2: the classical floors are exact dyadic rationals ---
    # These are the substantive claims: the limit is NONZERO, and it lands on a
    # simple rational to ~1e-10, which is not what a numerical artefact does.
    floors = {}
    for (Z, N), name, target, label in [
        ((1, 1), "D", mp.mpf(1) / 8, "1/8"),
        ((2, 2), "4He", mp.mpf(7) / 128, "7/128"),
    ]:
        c0, order, rows = classical_floor_and_order(Z, N)
        at_q0 = trace_difference(Z, N, mp.log(q0))
        floors[name] = {"c0": c0, "order": order, "rows": rows,
                        "at_q0": at_q0, "target": target, "label": label}
        w.add_assertion(
            f"{name}_trace_difference_classical_floor_is_{label.replace('/', '_over_')}",
            computed=mp.nstr(c0, 12),
            expected=mp.nstr(target, 12),
            tolerance="1e-8",
            source=f"Richardson extrapolation of tr_M(W_free) - tr_M(W_atom) to q -> 1 "
                   f"along q = exp(eta), eta = 1e-3..1e-6, via "
                   f"tr_m_atom_via_transfer.tr_m_atom_zn, vs the dyadic rational {label}. "
                   f"The claim under test is that the limit is NONZERO -- i.e. that this "
                   f"observable survives where the Hecke algebra degenerates to C[S_n].",
        )

    # ---- assertion 3: the deviation from the floor is first order -----------
    worst_order_dev = max(abs(floors[n]["order"] - 1) for n in floors)
    w.add_assertion(
        "trace_difference_deviation_from_the_floor_is_first_order_in_hbar_q",
        computed=mp.nstr(1 + worst_order_dev, 8),
        expected="1",
        tolerance="1e-2",
        source="log-log slope of |diff - c0| against hbar_q over eta = 1e-3..1e-6, worst "
               "case over the deuteron and 4He (measured "
               + ", ".join(f"{n}: {mp.nstr(floors[n]['order'], 8)}" for n in floors)
               + "). NOT hbar_q^2, which is what E_0_CONVENTIONS['B_q_value_absorbed'] "
                 "states for this operator class.",
    )

    # ---- assertion 4: Delta(net) DOES vanish, at first order ----------------
    delta_net = lambda e: (lambda h: h * (h - 2) / 2)(  # noqa: E731
        mp.exp(mp.mpf(e)) - 1 / mp.exp(mp.mpf(e)))
    order_dn = loglog_order(delta_net)
    w.add_assertion(
        "delta_net_is_exactly_first_order_with_no_classical_floor",
        computed=mp.nstr(order_dn, 8),
        expected="1",
        tolerance="1e-3",
        source="log-log slope of |Delta(net)| = |h(h-2)/2|, h = q - 1/q, against hbar_q "
               "over eta = 1e-3..1e-6. h vanishes identically at q = 1, so there is no "
               "floor to extrapolate -- this is convention A's operator class and it "
               "passes the test the trace difference fails.",
    )

    # ---- assertion 5: the Plancherel block sum is second order --------------
    block_orders = {}
    for name, (Z, N) in [("D", (1, 1)), ("4He", (2, 2)), ("12C", (6, 6))]:
        g = (lambda ZZ, NN: lambda e: BOA.spectral_b_over_a(
            ZZ, NN, q=float(mp.exp(mp.mpf(e))))["B_over_A_spectral_only_MeV"])(Z, N)
        block_orders[name] = loglog_order(g, "1e-3", "1e-5")
    worst_block = max(abs(mp.mpf(v) - 2) for v in block_orders.values())
    w.add_assertion(
        "plancherel_block_sum_is_second_order_with_no_classical_floor",
        computed=mp.nstr(2 + worst_block, 8),
        expected="2",
        tolerance="1e-2",
        source="log-log slope of b_over_a_evaluator.spectral_b_over_a against hbar_q, worst "
               "case over D, 4He, 12C (measured "
               + ", ".join(f"{k}: {mp.nstr(mp.mpf(v), 8)}" for k, v in block_orders.items())
               + "). At q = 1 every one-crossing eigenvalue is +-1, so the log-ratio is "
                 "identically zero and there is no floor.",
    )

    # ---- data ---------------------------------------------------------------
    w.add_parameter("q0", mp.nstr(q0, 30))
    w.add_parameter("sweep", "q = exp(eta), eta = 1e-3 .. 1e-6")

    w.add_data("classification", [
        {"observable": "Delta(net) = h(h-2)/2, h = q - 1/q",
         "classical_floor": "0 (exact -- h vanishes at q=1)",
         "deformation_order": mp.nstr(order_dn, 8),
         "registry_operator_class": "A_single_hecke_tick",
         "consistent_E0_pairing": "A (hbar_q^1) -> total hbar_q^2",
         "verdict": "PASSES"},
        {"observable": "Plancherel block sum (b_over_a_evaluator)",
         "classical_floor": "0 (exact -- eigenvalues -> +-1, log-ratio -> 0)",
         "deformation_order": {k: mp.nstr(mp.mpf(v), 8) for k, v in block_orders.items()},
         "registry_operator_class": "B_q_value_absorbed (trace-ratio family)",
         "consistent_E0_pairing": "B (hbar_q^0) -> total hbar_q^2",
         "verdict": "PASSES"},
        {"observable": "tr_M(W_free) - tr_M(W_atom)",
         "classical_floor": {n: mp.nstr(floors[n]["c0"], 15) + f"  (= {floors[n]['label']})"
                             for n in floors},
         "deformation_order": {n: mp.nstr(floors[n]["order"], 8) for n in floors},
         "registry_operator_class": "B_q_value_absorbed, stated as 'carries the hbar_q^2 "
                                    "scaling'",
         "consistent_E0_pairing": "NONE -- the floor is hbar_q^0 and the deformation is "
                                  "hbar_q^1, so no single scale pairs with the whole thing",
         "verdict": "FAILS"},
    ])

    w.add_data("classical_contamination_at_q0", {
        n: {"trace_difference_at_q0": mp.nstr(floors[n]["at_q0"], 15),
            "classical_floor": mp.nstr(floors[n]["c0"], 15),
            "classical_share_percent": mp.nstr(100 * floors[n]["c0"] / floors[n]["at_q0"], 6)}
        for n in floors
    })

    d_at_q0 = floors["D"]["at_q0"]
    w.add_data("the_two_producers_disagree", {
        "quantity": "tr_M(W_free) - tr_M(W_atom) for the deuteron = "
                    + mp.nstr(d_at_q0, 15),
        "binding_canonical (convention B)": {
            "scale_MeV": E0_B_MEV,
            "binding_MeV": mp.nstr(mp.mpf(E0_B_MEV) * d_at_q0, 10),
            "vs_AME_2.22456637": mp.nstr(AME_B_DEUTERON / (mp.mpf(E0_B_MEV) * d_at_q0), 6)
                                 + "x short",
        },
        "derive_binding_chain_cooperative (convention A)": {
            "scale_MeV": E0_A_MEV,
            "binding_MeV": mp.nstr(mp.mpf(E0_A_MEV) * d_at_q0, 10),
            "vs_AME_2.22456637": mp.nstr(AME_B_DEUTERON / (mp.mpf(E0_A_MEV) * d_at_q0), 6)
                                 + "x short",
        },
        "ratio": mp.nstr(mp.mpf(E0_A_MEV) / mp.mpf(E0_B_MEV), 8),
        "note": "Same trace difference, two live producers, two conventions, 5.35x apart. "
                "The registry rule 'atom level MUST use B' rests on the hbar_q^2 claim this "
                "probe refutes, so the rule cannot currently adjudicate. Recorded as an "
                "inconsistency to resolve, NOT resolved here -- picking the convention that "
                "lands closer to AME would be exactly the fit this lane keeps walking into.",
    })

    w.add_data("what_is_NOT_concluded", (
        "That the hbar_q-suppressed route is refuted. Delta(net) and the Plancherel block "
        "sum both pass the classical-limit test cleanly, and Delta(net) x convention A still "
        "predicts Q_beta to 0.168%. What is refuted is the assumption -- mine, stated last "
        "turn without checking -- that the trace difference belongs to that category. It "
        "does not, and the registry's hbar_q index for it is wrong by two orders."
    ))

    w.add_data("verdict", (
        "tr_M(W_free) - tr_M(W_atom) is NOT a pure deformation observable. It has an exact "
        "dyadic classical floor -- 1/8 at the deuteron, 7/128 at 4He, extrapolated to 1e-10 "
        "-- plus an hbar_q^1 deformation. At q0 the floor is 22.46% of it for the deuteron "
        "and 4.88% for 4He, so that fraction of any binding read off it is present in a "
        "framework with no deformation at all. E_0_CONVENTIONS says this operator class "
        "'carries the hbar_q^2 scaling'; measured it carries neither an hbar_q^2 leading "
        "term nor a vanishing limit. Since the two parts sit at different orders, no single "
        "E_0 convention pairs with it consistently -- and two live producers already "
        "disagree by 5.35x about which one to use."
    ))

    out = w.save()
    print(f"wrote {out}")
    print()
    print(f"  {'observable':38} {'classical floor':>20} {'deformation order':>18}")
    print(f"  {'Delta(net) = h(h-2)/2':38} {'0 (exact)':>20} {mp.nstr(order_dn, 8):>18}")
    for k, v in block_orders.items():
        print(f"  {'Plancherel block sum ' + k:38} {'0 (exact)':>20} "
              f"{mp.nstr(mp.mpf(v), 8):>18}")
    for n in floors:
        f = floors[n]
        print(f"  {'tr_free - tr_atom  ' + n:38} "
              f"{mp.nstr(f['c0'], 12) + ' = ' + f['label']:>20} "
              f"{mp.nstr(f['order'], 8):>18}")
    print()
    for n in floors:
        f = floors[n]
        print(f"  {n}: at q0 = {mp.nstr(f['at_q0'], 12)}, classical share "
              f"{mp.nstr(100 * f['c0'] / f['at_q0'], 6)} %")
    print(f"  deuteron binding: conv B {mp.nstr(mp.mpf(E0_B_MEV) * d_at_q0, 8)} MeV, "
          f"conv A {mp.nstr(mp.mpf(E0_A_MEV) * d_at_q0, 8)} MeV, AME 2.22456637 "
          f"-- two live producers, 5.35x apart")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
