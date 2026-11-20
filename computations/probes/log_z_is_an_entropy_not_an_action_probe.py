#!/usr/bin/env python3
"""The extensive term is an ENTROPY, not an action — converting it to MeV needs a
temperature, and the framework has none.

THE QUESTION
------------
Bean `qou-59j5` closed with `E_0` not derivable and a four-convention registry
that cannot say which `E_0` the extensive term takes, because `log Z(3A)`
matches none of the registry's operator classes. Its successor question was
posed to be answerable **without any energy scale**:

    what `hbar_q` power does `log Z` carry, and does the framework assign an
    operator class to a bare partition function at all?

ANSWER: `hbar_q^0`, AND NO
---------------------------
`log Z` carries **zero** `hbar_q`. It has a nonzero classical limit, and every
observable in the framework's registry has a vanishing one. That is a clean
structural discriminator and it puts `log Z` outside the family the `E_0` ladder
is built for.

WHAT `Z(n)` ACTUALLY IS
------------------------
Rebuilt from `markov_weights_symbolic`'s own Schur/hook components, the
normaliser's coefficients in `q^{2k}` are **exactly the binomial coefficients**
[assertion 1]:

    Z(n) = Σ_λ s_λ(1,q²)·f^λ = Σ_k C(n,k)·q^{2k}       (n = 2 … 6, exact)

That is the **weight generating function of `(ℂ²)^{⊗n}`** — `q^{2k}` counting
the `k` down-spins among `n` strands, at Wenzl level `r = 2`. Setting `q = 1`:

    Z(n)|_{q=1} = 2^n = dim (ℂ²)^{⊗n}                   [assertion 2]

So `log Z(3A)` is a **graded log-dimension**. It is the entropy of the 3A-strand
Hilbert space, not the action of any operator. Nothing about it is an energy
until something multiplies it by one, and the previous probe showed the
framework cannot say what.

THE DISCRIMINATOR: BEHAVIOUR AT `q → 1`
----------------------------------------
Every operator class the `E_0` registry indexes **vanishes** in the classical
limit [assertion 3], measured, not argued:

    Delta(net) = h(h-2)/2,  h = q - 1/q          →  0   exactly at q = 1
    spectral block sum (deuteron)                →  0.0 exactly at q = 1
    spectral block sum (⁴He)                     →  0.0
    spectral block sum (¹²C)                     →  0.0

(the block sum vanishes for a visible reason: at `q = 1` every one-crossing
eigenvalue in `b_over_a_evaluator` becomes `±1`, so `Λ_free/Λ_nuc` has modulus 1
and its log is 0 — the Hecke algebra degenerates to the group algebra of `S_n`
and there is no deformation left to carry an energy.)

`log Z` does not vanish. It tends to `n log 2`.

AND THE CLASSICAL PIECE IS THE MAJORITY OF IT
----------------------------------------------
Per strand, at `q₀`:

    log(1 + q₀²) = 0.802922
                 = log 2  +  (q₀ − 1)  +  O((q₀−1)³)
                 = 0.693147 + 0.109979 − 0.000204

**86.33 %** of the extensive term is the `hbar_q^0` entropy `log 2`
[assertion 4] — the part that is still there at `q = 1`, where the framework has
no energies at all.

"BUT F = -kT log Z IS AN ENERGY" — THE RIGHT OBJECTION, AND ITS ANSWER
-----------------------------------------------------------------------
Entropy times temperature is an energy; "multiply a dimensionless log Z by an
energy scale" is the standard free-energy construction, not an abuse. So the
claim is NOT that log Z can never become an energy. It is sharper:

**the conversion needs a TEMPERATURE, the framework's `E_0` is an ACTION scale,
and the framework has no temperature.**

* `E_0`'s registry conventions are each (scale) x (`hbar_q`-suppressed operator),
  totalling `hbar_q^2` — see bean `qou-59j5`. Pairing that scale with an
  `hbar_q^0` log-dimension breaks the very bookkeeping the registry is indexed
  by. `E_0` is not a `kT`.
* The corpus already went looking for a `kT`. `computations/landauer_crossing_-
  energy_probe.py` tests exactly the Landauer identification
  `E_H = kT_eff x (information)` against five canonical candidate scales
  {`m_e c_q^2`, `m_mu`, `E_0`, `m_e/hbar_q`, `E_0 c_q^2`} = {52.05, 105.66,
  4.186, 5.157, 426.4} MeV. Its committed witness records
  `near_matches_5pct = {"proton": [], "neutron": []}` — **no candidate within
  5 %**, with ratios running 42x to 4266x [assertion 5]. That probe uses a
  different information measure (crossing information `l*eta_q` q-bits, not
  `log Z`), so it does not settle the question for this quantity — but it is the
  only attempt on record and it failed.
* Run directly for **this** measure: the temperature that would make
  `3 log(1+q_0^2) * kT = a_V` is `kT = 6.5595 MeV`, and the nearest framework
  scale is `m_e/hbar_q = 5.1573`, **27 % away**; nothing is within 5 %
  [assertion 6]. (Back-computed from `a_V`, so this is a refutation — no
  identification is available — not a derivation.)

WHAT THIS MEANS
---------------
"The extensive term is short of `a_V` by N" was comparing an entropy to an energy
through a conversion the framework does not supply, independently of which `E_0`
is picked. `a_V` is MeV per nucleon; `log Z(3A)/A` is `3 log 2 + O(hbar_q)` nats
per nucleon. The deficits reported all session — 1.57x, 6.9x, 8.38x, 12.84x —
each manufactured that missing conversion by choosing a scale.

This also explains, without any new hypothesis, why the *exponent* test passed
so cleanly (`qou-imcd`, A-exponent exactly 1) while every magnitude ansatz
failed: an extensive entropy and an extensive energy have the same `A`-scaling
by construction, and the exponent test cannot tell them apart. Six failed
magnitude ansätze were fitting a conversion between two different kinds of
quantity.

WHAT IS *NOT* CLAIMED
---------------------
That the `hbar_q^1` part is the energy. Stripping `log 2` leaves
`(q₀ − 1) = 0.109979` per strand, and it is tempting to call that the deformation
energy; the probe reports it and **declines to convert it to MeV**. It would
still be scale-ambiguous by the same 5.35x (convention A vs B), and picking the
scale that lands on `a_V` would be the same fit this lane has now walked into
three times. It is recorded as a measurement, not a candidate.

Usage:
    python3 computations/probes/log_z_is_an_entropy_not_an_action_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from math import comb, factorial
from pathlib import Path

import sympy as sp
from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import b_over_a_evaluator as BOA  # noqa: E402
import markov.markov_weights_symbolic as M  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

STRANDS_PER_NUCLEON = 3
M_E_MEV = mp.mpf("0.51099895069")
SEMF_A_V = mp.mpf("15.8")   # MeV, semi-empirical mass formula volume coefficient


def normaliser_poly(n: int) -> sp.Expr:
    """`Z(n)`, rebuilt from `markov_weights_symbolic`'s own components.

    Deliberately reconstructed rather than imported: assertion 1 compares this
    partition sum against the binomial theorem, so the two sides must be
    computed by different routes.
    """
    total = 0
    for shape in (tuple(s) for s in M.partitions_of(n)):
        hooks, _ = M.hooks_and_contents(list(shape))
        prod = 1
        for h in hooks:
            prod *= h
        f_lambda = factorial(n) // prod
        total += M.schur_principal_symbolic(list(shape)) * f_lambda
    return sp.expand(total)


def main() -> int:
    q = Q_MP
    hbar_q = (q - 1) / q
    w = WitnessBuilder("log-z-is-an-entropy-not-an-action-probe")
    w.set_description(
        "Answers the qou-59j5 successor question with no energy scale: log Z carries "
        "hbar_q^0 and the framework assigns it no operator class. Z(n) is the weight "
        "generating function of (C^2)^{tensor n}, so log Z(3A) is a graded log-dimension "
        "-- an entropy. Every registered operator class vanishes at q=1; log Z does not, "
        "and 86.33% of it is the classical log 2. Comparing it to a_V is a category error."
    )

    # ---- assertion 1: Z(n) coefficients ARE the binomial coefficients --------
    # Two genuinely different routes: a sum over partitions of principally
    # specialised Schur functions times hook-length degrees, vs C(n,k) from the
    # binomial theorem. Agreement identifies Z(n) as the weight generating
    # function of (C^2)^{tensor n}.
    q_sym = next(iter(M.Q_W.free_symbols))
    coeff_rows, coeffs_match = [], True
    for n in range(2, 7):
        poly = sp.Poly(normaliser_poly(n), q_sym)
        got = [int(poly.coeff_monomial(q_sym ** (2 * k))) for k in range(n + 1)]
        want = [comb(n, k) for k in range(n + 1)]
        if got != want:
            coeffs_match = False
        coeff_rows.append({"n": n, "Z_coeffs_in_q2k": got, "binomial_C_n_k": want,
                           "Z_at_q_1": sum(got), "two_to_the_n": 2 ** n})
    w.add_assertion(
        "normaliser_coefficients_are_the_binomial_coefficients",
        computed="1" if coeffs_match else "0",
        expected="1",
        source="coefficients of q^{2k} in Z(n) = sum over partitions of "
               "s_lambda(1,q^2) * f^lambda, rebuilt from markov_weights_symbolic's own "
               "hook/Schur components, vs C(n,k) from the binomial theorem, n = 2..6. "
               "Agreement identifies Z(n) as the weight generating function of "
               "(C^2)^{tensor n} with q^{2k} counting k down-spins among n strands.",
    )

    # ---- assertion 2: at q = 1 the normaliser IS the Hilbert-space dimension -
    dim_match = all(r["Z_at_q_1"] == r["two_to_the_n"] for r in coeff_rows)
    w.add_assertion(
        "normaliser_at_q_one_is_the_hilbert_space_dimension",
        computed="1" if dim_match else "0",
        expected="1",
        source="Z(n)|_{q=1} from the partition sum above vs 2^n = dim (C^2)^{tensor n} "
               "(independent: elementary linear algebra, not a corpus quantity), n = 2..6",
    )

    # ---- assertion 3: every registered operator class vanishes at q = 1 ------
    # This is the discriminator. The E_0 registry indexes conventions by
    # operator class; measured here, each of those classes is identically zero
    # in the classical limit.
    h_at_one = mp.mpf(1) - 1 / mp.mpf(1)
    delta_net_at_one = abs(h_at_one * (h_at_one - 2) / 2)
    block_sums_at_one = {}
    for name, (Z, N) in [("D", (1, 1)), ("4He", (2, 2)), ("12C", (6, 6))]:
        rec = BOA.spectral_b_over_a(Z, N, q=1.0)
        block_sums_at_one[name] = rec["B_over_A_spectral_only_MeV"]
    worst_operator = max([float(delta_net_at_one)]
                         + [abs(float(v)) for v in block_sums_at_one.values()])
    w.add_assertion(
        "every_registered_operator_class_vanishes_at_q_equals_one",
        computed=mp.nstr(mp.mpf(worst_operator), 12),
        expected="0",
        tolerance="1e-30",
        source="max over the E_0 registry's operator classes of |value at q = 1|: "
               "convention A's Delta(net) = h(h-2)/2 with h = q - 1/q, and convention B's "
               "spectral block sum via b_over_a_evaluator.spectral_b_over_a(q=1.0) at D, "
               "4He and 12C. All are identically zero: at q = 1 every one-crossing "
               "eigenvalue is +-1, so the Hecke algebra degenerates to C[S_n] and no "
               "deformation is left to carry an energy.",
    )

    # ---- assertion 4: log Z's classical share is the MAJORITY of it ----------
    log_loop = mp.log(1 + q ** 2)
    classical_share = mp.log(2) / log_loop
    w.add_assertion(
        "classical_entropy_is_the_majority_of_the_extensive_term",
        computed="1" if classical_share > mp.mpf("0.5") else "0",
        expected="1",
        source=f"log 2 / log(1+q_0^2) = {mp.nstr(classical_share, 8)}. The numerator is the "
               f"q = 1 value, which survives where every operator class above is zero; the "
               f"denominator is the full per-strand extensive term at q_0. A share above "
               f"1/2 means the extensive term is mostly the hbar_q^0 entropy.",
    )

    # ---- assertion 5: the corpus's own temperature hunt found nothing -------
    # Read from a committed witness produced by a different script. That probe
    # uses the crossing-information measure (l * eta_q q-bits), NOT log Z, so it
    # does not settle this quantity — but it is the only attempt on record.
    land = json.loads((HERE.parent / "landauer-crossing-energy-probe.witness.json").read_text())
    landauer_near = land["near_matches_5pct"]
    no_landauer_match = all(len(v) == 0 for v in landauer_near.values())
    ratios = [mp.mpf(r) for h in land["hadrons"].values()
              for r in h["ratio_vs_scale"].values()]
    w.add_assertion(
        "landauer_temperature_hunt_found_no_candidate_scale",
        computed="1" if no_landauer_match else "0",
        expected="1",
        source=f"near_matches_5pct from computations/landauer-crossing-energy-probe."
               f"witness.json is empty for both proton and neutron; its implied kT_eff is "
               f"~17856 MeV/q-bit against five canonical candidate scales, with ratios "
               f"running {mp.nstr(min(ratios), 6)}x to {mp.nstr(max(ratios), 6)}x. Different "
               f"information measure from log Z, so suggestive rather than decisive here.",
    )

    # ---- assertion 6: no framework scale is the temperature log Z would need -
    # kt_required is BACK-COMPUTED from a_V, so this can only ever refute an
    # identification, never establish one. That is exactly its use: it shows
    # there is nothing in the framework to identify the temperature with.
    kt_required = SEMF_A_V / (STRANDS_PER_NUCLEON * log_loop)
    candidates = {
        "m_e": M_E_MEV,
        "E_0 = m_e/(q(q-1))": M_E_MEV / (q * (q - 1)),
        "m_e/hbar_q": M_E_MEV / hbar_q,
        "m_e c_q^2 = m_e/hbar_q^2": M_E_MEV / hbar_q ** 2,
        "E_0 c_q^2": M_E_MEV / (q * (q - 1)) / hbar_q ** 2,
    }
    ratio_rows = {k: mp.nstr(kt_required / v, 8) for k, v in candidates.items()}
    nearest_name, nearest_ratio = min(
        ((k, kt_required / v) for k, v in candidates.items()),
        key=lambda kv: abs(kv[1] - 1))
    w.add_assertion(
        "no_framework_scale_matches_the_temperature_log_Z_would_need",
        computed="1" if abs(nearest_ratio - 1) > mp.mpf("0.05") else "0",
        expected="1",
        source=f"kT required for 3*log(1+q_0^2)*kT = a_V is "
               f"{mp.nstr(kt_required, 8)} MeV; the nearest of the framework's canonical "
               f"scales is {nearest_name} at ratio {mp.nstr(nearest_ratio, 6)}, i.e. "
               f"{mp.nstr(100 * abs(nearest_ratio - 1), 4)} % away. Asserting nothing is "
               f"within 5 %. Back-computed from a_V, so this refutes an identification "
               f"rather than establishing one.",
    )

    # ---- data ---------------------------------------------------------------
    w.add_data("temperature_hunt", {
        "why_a_temperature": "F = -kT log Z. Entropy times temperature is an energy, so the "
                             "objection 'log Z CAN become an energy' is correct. What the "
                             "framework lacks is the kT, not the arithmetic.",
        "why_E_0_is_not_it": "every E_0 registry convention is (scale) x (hbar_q-suppressed "
                             "operator), totalling hbar_q^2 (bean qou-59j5). Pairing that "
                             "with an hbar_q^0 log-dimension breaks the registry's own "
                             "index. E_0 is an action scale, not a temperature.",
        "kT_required_for_a_V_MeV": mp.nstr(kt_required, 12),
        "ratio_vs_framework_scales": ratio_rows,
        "nearest": nearest_name + " at " + mp.nstr(100 * abs(nearest_ratio - 1), 4) + " %",
        "landauer_probe_near_matches_5pct": landauer_near,
    })
    w.add_parameter("q0", mp.nstr(q, 30))
    w.add_parameter("hbar_q", mp.nstr(hbar_q, 25))
    w.add_parameter("strands_per_nucleon", STRANDS_PER_NUCLEON)

    w.add_data("Z_is_a_graded_dimension", coeff_rows)
    w.add_data("operator_classes_at_q_equals_one", {
        "convention_A_Delta_net": mp.nstr(delta_net_at_one, 6),
        "convention_B_block_sum": {k: str(v) for k, v in block_sums_at_one.items()},
        "why": "at q = 1 the one-crossing eigenvalues (sym: q, 1/q, (q+1/q)/2; alt: their "
               "negatives; std: 1) all become +-1, so |Lambda_free/Lambda_nuc| = 1 and its "
               "log is 0. H_n(q) -> C[S_n].",
        "at_q0_for_contrast": {
            "Delta_net": mp.nstr(abs((q - 1 / q) * ((q - 1 / q) - 2) / 2), 10),
            "block_sum_D": str(BOA.spectral_b_over_a(1, 1)["B_over_A_spectral_only_MeV"]),
        },
    })

    w.add_data("hbar_q_grading_of_the_extensive_term", {
        "log(1+q0^2)": mp.nstr(log_loop, 15),
        "hbar_q^0 term  (log 2)": mp.nstr(mp.log(2), 15),
        "hbar_q^1 term  (q0 - 1)": mp.nstr(q - 1, 15),
        "sum_of_first_two": mp.nstr(mp.log(2) + (q - 1), 15),
        "residual": mp.nstr(log_loop - mp.log(2) - (q - 1), 10),
        "note": "d/dq log(1+q^2) = 2q/(1+q^2) = 1 at q = 1 and the second derivative "
                "vanishes there, so the expansion is log 2 + (q-1) + O((q-1)^3). The "
                "residual measured above is consistent with that.",
        "classical_share_percent": mp.nstr(100 * classical_share, 6),
    })

    w.add_data("NOT_A_CANDIDATE", {
        "the_tempting_move": "strip log 2 and call the remainder (q0 - 1) = "
                             + mp.nstr(q - 1, 10) + " per strand the deformation energy",
        "why_it_is_not_reported_in_MeV": (
            "It would still be scale-ambiguous by the same 5.35x (convention A vs B, bean "
            "qou-59j5), so converting it would be picking a scale that lands somewhere -- "
            "the same fit this lane has walked into three times now. Recorded as a "
            "dimensionless measurement only."
        ),
    })

    w.add_data("what_this_explains", (
        "Why the EXPONENT test passed cleanly (qou-imcd: A-exponent exactly 1) while six "
        "magnitude ansaetze failed. An extensive entropy and an extensive energy have the "
        "same A-scaling by construction, so the exponent test cannot distinguish them. The "
        "magnitude ansaetze were fitting a conversion between two different KINDS of "
        "quantity, which is why they failed 'all in the same way'."
    ))

    w.add_data("verdict", (
        "log Z carries hbar_q^0 and has no operator class. Z(n) = sum_k C(n,k) q^{2k} is "
        "the weight generating function of (C^2)^{tensor n} and Z(n)|_{q=1} = 2^n is its "
        "dimension, so log Z(3A) is a graded log-dimension -- an ENTROPY. Every operator "
        "class the E_0 registry indexes vanishes at q = 1; log Z does not, and 86.33% of it "
        "is that classical log 2. Comparing log Z(3A)*E_0 to a_V is a CATEGORY ERROR, "
        "independently of which E_0 is chosen. Every deficit reported this session -- 1.57x, "
        "6.9x, 8.38x, 12.84x -- was an entropy measured against an energy through an "
        "undetermined conversion. The successor question is closed and the answer removes "
        "the comparison rather than settling it."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  Z(n) coeffs == C(n,k), n=2..6      : {coeffs_match}")
    print(f"  Z(n)|_(q=1) == 2^n == dim(C^2)^n   : {dim_match}")
    print(f"  Delta(net) at q=1                  : {mp.nstr(delta_net_at_one, 6)}")
    print(f"  block sums at q=1 (D, 4He, 12C)    : "
          f"{[str(v) for v in block_sums_at_one.values()]}")
    print(f"  log(1+q0^2)                        : {mp.nstr(log_loop, 12)}")
    print(f"    = log 2 {mp.nstr(mp.log(2), 10)} + (q0-1) {mp.nstr(q - 1, 10)} "
          f"+ {mp.nstr(log_loop - mp.log(2) - (q - 1), 4)}")
    print(f"  classical (hbar_q^0) share         : {mp.nstr(100 * classical_share, 6)} %")
    print(f"  required kT for a_V                : {mp.nstr(kt_required, 8)} MeV; nearest "
          f"framework scale {nearest_name} at {mp.nstr(100 * abs(nearest_ratio - 1), 4)} % away")
    print(f"  Landauer probe near-matches (5%)   : {landauer_near}")
    print(f"  => log Z(3A) is an ENTROPY. Converting it needs a TEMPERATURE, and the "
          f"framework has none.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
