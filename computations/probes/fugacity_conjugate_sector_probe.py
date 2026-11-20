#!/usr/bin/env python3
"""The framework HAS a thermodynamic sector — and that is exactly why it has no
temperature.

THE QUESTION
------------
`qou-ap3d` showed `log Z(3A)` is an entropy and that no framework scale serves
as the `kT` that would turn it into MeV — an *empirical* negative (the Landauer
probe found nothing within 5 %). Its successor question was structural:

    does the framework have a thermodynamic sector at all? If `Z` is a partition
    function then `Q = q²` is a fugacity and there must be a conjugate variable.
    If there is none, `Z` is a normaliser and nothing more.

ANSWER: THERE IS A FULL CONJUGATE PAIR, AND NO ENERGY ANYWHERE IN IT
---------------------------------------------------------------------
`Z(n) = (1+Q)^n = Σ_k C(n,k)·Q^k` is the grand partition function of `n`
independent two-level sites. `Q = q₀²` is a **fugacity**, conjugate to `k` — the
number of strands in the second state — and the whole apparatus follows:

    log Q          = 2·η₀ = 0.2086814406            the field, βμ (or 2βh)
    <k>/n          = ∂log Z/∂log Q = Q/(1+Q)
                   = (1 + tanh η₀)/2 = 0.5519818550 [assertion 1]
    S/n            = log Z/n − (<k>/n)·log Q
                   = H(<k>/n) = 0.6877331765         [assertion 3]
    Var(k)/n       = Q/(1+Q)² = 0.2472978867          the susceptibility

The Legendre transform really is a Shannon entropy: it agrees with the binary
entropy `H(p)` of the measured occupancy to **1.1e-41** at 40 dps, which is the
precision floor. And

    S/n = log 2 − η₀²/2 + O(η₀⁴)

— the entropy deficit from maximal is `η₀²/2 = 0.005444` nats/strand.

WHY THAT SETTLES THE TEMPERATURE QUESTION STRUCTURALLY
-------------------------------------------------------
Read off the coefficients: they are the **bare binomials `C(n,k)`, pure integers
with no `q`-dependence at all** [assertion 4]. A partition function with a
Hamiltonian has coefficients `Ω_k·e^{−βE_k}`; this one has multiplicity only. So

* the spectrum is **linear in `k`** — the only `q` is `Q^k`, a field term with
  no interaction and no reference energy;
* therefore only the **product** `βμ = 2η₀` is determined. `β` alone appears
  nowhere in the construction, and a linear spectrum has no intrinsic scale:
  rescale `β` and `μ` inversely and `Z` is unchanged.

**So the temperature is not merely unfound, it is structurally absent.** The
Landauer probe's negative — no candidate scale within 5 %, off by 41.9x to
4266x — was looking for something the construction cannot contain. That upgrades
`qou-ap3d`'s empirical miss to a reason.

A1 DIES ON STRUCTURAL GROUNDS — WHICH CLOSES `qou-78pt` PROPERLY
------------------------------------------------------------------
Attack A1 is "the extensive term is the Markov normalisation we divide out; stop
dividing". What that retains is

    log Z = S + βμ·<k>

— a Shannon entropy plus a dimensionless field term. Both are pure numbers **by
construction**, not by an unlucky choice of convention. No member of the
normalisation family, and no choice among the four `E_0` conventions, can make
`log Z` an energy, because there is no `1/β` in the framework to multiply it by.

`qou-78pt` was reopened on 2026-08-31 when the "A1 REFUTED" verdict was withdrawn
(the 6-15x deficit turned out to be an `m_e`-vs-`E_0` artifact). It can now be
closed for the right reason: not "no family member reaches the target" — a
numerical claim that did not survive — but **"no family member is an energy"**.

A CROSS-CHECK THAT IS NOT A NEW CONSTANT
-----------------------------------------
The polarization of this two-level system,

    2·<k>/n − 1 = (Q−1)/(Q+1) = tanh η₀ = 0.1039637100524101457

is, to all 20 digits, the corpus's **already-derived "Coulomb/strong ratio"**
[assertion 2] — `def:coulomb-charge`, used in at least eight probes
(`charge_coulomb_tn3he_derived`, `em_linking_invariant_probe`,
`mirror_split_*`, …).

**This is not a new derivation of a new number.** The corpus reaches it from the
sinh/cosh channel split of the crossing energy `E_cross = n₊q − n₋q⁻¹`, whose
antisymmetric/symmetric ratio at `n₋ = 0` is `(q−q⁻¹)/(q+q⁻¹)`; multiply top and
bottom by `q` and that *is* `(Q−1)/(Q+1)`. Same one-line algebra, reached from
two different places.

What is worth recording is the **reading**: the same ratio is simultaneously an
energy ratio (the corpus's route) and a thermal polarization (this one). Being a
*ratio*, it is scale-free either way — which is precisely why it survives while
the extensive magnitude does not. The framework's derived quantities are ratios
and polarizations; its one attempt at an absolute magnitude is the one with no
scale.

Usage:
    python3 computations/probes/fugacity_conjugate_sector_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from math import comb, factorial
from pathlib import Path

import sympy as sp
from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import markov.markov_weights_symbolic as M  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

N_SITES = 12  # ⁴He's strand count; any n gives the same per-site quantities


def normaliser_coeffs(n: int) -> list[int]:
    """Coefficients of `Q^k` in `Z(n)`, from `markov_weights_symbolic`'s own
    Schur/hook components. Rebuilt rather than imported so assertion 4 compares
    the partition sum against the binomials by a different route."""
    total = 0
    for shape in (tuple(s) for s in M.partitions_of(n)):
        hooks, _ = M.hooks_and_contents(list(shape))
        prod = 1
        for h in hooks:
            prod *= h
        total += M.schur_principal_symbolic(list(shape)) * (factorial(n) // prod)
    q_sym = next(iter(M.Q_W.free_symbols))
    poly = sp.Poly(sp.expand(total), q_sym)
    return [poly.coeff_monomial(q_sym ** (2 * k)) for k in range(n + 1)]


def main() -> int:
    q = Q_MP
    Q = q ** 2
    eta = mp.log(q)
    w = WitnessBuilder("fugacity-conjugate-sector-probe")
    w.set_description(
        "The framework's normaliser Z(n) = (1+q^2)^n IS a grand partition function: q^2 is "
        "a fugacity conjugate to the strand-state count k, the Legendre transform is a "
        "Shannon entropy, and the polarization is the corpus's own Coulomb/strong ratio. "
        "But the coefficients are the bare binomials -- no Boltzmann weight -- so only the "
        "product beta*mu = 2*eta_0 is fixed and the temperature is STRUCTURALLY absent, "
        "not merely unfound. A1 dies on structural grounds."
    )

    # ---- the coefficients, rebuilt --------------------------------------------
    coeffs = normaliser_coeffs(N_SITES)

    # ---- assertion 1: <k>/n from an explicit moment vs the closed form -------
    # LHS: the statistical average sum_k k*C_k*Q^k / (n * sum_k C_k*Q^k), formed
    # from the rebuilt coefficients. RHS: the two-level closed form. Different
    # routes -- one is a finite sum over the partition data, the other is a
    # hyperbolic-function identity.
    num = sum(mp.mpf(int(c)) * k * Q ** k for k, c in enumerate(coeffs))
    den = sum(mp.mpf(int(c)) * Q ** k for k, c in enumerate(coeffs))
    mean_occ = num / (den * N_SITES)
    closed = (1 + mp.tanh(eta)) / 2
    w.add_assertion(
        "mean_occupancy_from_the_moment_equals_one_plus_tanh_eta_over_two",
        computed=mp.nstr(mean_occ, 25),
        expected=mp.nstr(closed, 25),
        tolerance="1e-35",
        source="explicit first moment <k>/n over the rebuilt Z(12) coefficients at Q = q_0^2, "
               "vs the free two-level closed form (1 + tanh eta_0)/2 with eta_0 = log q_0. "
               "Agreement is what makes Q a fugacity conjugate to k rather than a formal "
               "variable.",
    )

    # ---- assertion 2: the polarization IS the corpus's Coulomb/strong ratio --
    # INDEPENDENT side: tanh(ln q_0), reached in the corpus from the sinh/cosh
    # channel split of the crossing energy (def:coulomb-charge), a route with no
    # partition function in it. Same algebra, two different places.
    polarization = 2 * mean_occ - 1
    w.add_assertion(
        "polarization_is_the_corpus_coulomb_strong_ratio",
        computed=mp.nstr(polarization, 25),
        expected=mp.nstr(mp.tanh(mp.log(q)), 25),
        tolerance="1e-35",
        source="2<k>/n - 1 from the moment above, vs tanh(ln q_0) -- the 'derived "
               "Coulomb/strong ratio' of def:coulomb-charge, used by "
               "charge_coulomb_tn3he_derived.py, em_linking_invariant_probe.py and six "
               "others. The corpus reaches it as the antisymmetric/symmetric ratio "
               "(q-1/q)/(q+1/q) of E_cross at n_- = 0; multiplying through by q gives "
               "(Q-1)/(Q+1). NOT a new constant -- a second reading of one.",
    )

    # ---- assertion 3: the Legendre transform is a Shannon entropy ------------
    log_z_per_site = mp.log(1 + Q)
    entropy = log_z_per_site - mean_occ * mp.log(Q)
    shannon = -mean_occ * mp.log(mean_occ) - (1 - mean_occ) * mp.log(1 - mean_occ)
    w.add_assertion(
        "legendre_transform_of_log_Z_is_the_binary_shannon_entropy",
        computed=mp.nstr(entropy, 25),
        expected=mp.nstr(shannon, 25),
        tolerance="1e-35",
        source="S/n = log Z/n - (<k>/n)*log Q, the Legendre transform of the grand "
               "potential in the field log Q, vs the binary Shannon entropy H(p) of the "
               "occupancy p measured above. Two different constructions; agreement is what "
               "makes S an entropy rather than a leftover.",
    )

    # ---- assertion 4: there is NO Boltzmann weight --------------------------
    # The decisive one. Coefficients of Q^k are the bare multiplicities C(n,k):
    # pure integers, no q-dependence. A partition function with a Hamiltonian
    # would carry Omega_k * exp(-beta E_k) here.
    bare = all(c == comb(N_SITES, k) and c.is_Integer for k, c in enumerate(coeffs))
    w.add_assertion(
        "coefficients_are_bare_multiplicities_so_there_is_no_boltzmann_weight",
        computed="1" if bare else "0",
        expected="1",
        source=f"every coefficient of Q^k in the rebuilt Z({N_SITES}) is a q-INDEPENDENT "
               f"integer equal to C({N_SITES},k). A Hamiltonian would put Omega_k * "
               f"exp(-beta E_k) there. So the spectrum is linear in k, the only q is the "
               f"fugacity, and nothing in Z fixes beta or mu separately -- only the product "
               f"beta*mu = log Q = 2*eta_0.",
    )

    # ---- data ---------------------------------------------------------------
    w.add_parameter("q0", mp.nstr(q, 30))
    w.add_parameter("Q_fugacity", mp.nstr(Q, 30))
    w.add_parameter("eta0", mp.nstr(eta, 30))
    w.add_parameter("n_sites", N_SITES)

    w.add_data("the_conjugate_pair", {
        "partition_function": "Z(n) = (1+Q)^n = sum_k C(n,k) Q^k",
        "fugacity_Q": mp.nstr(Q, 20),
        "field_log_Q_is_beta_mu": mp.nstr(mp.log(Q), 20),
        "field_in_terms_of_eta0": "log Q = 2 eta_0 exactly",
        "conjugate_variable": "k, the number of strands in the second state",
        "mean_occupancy_per_site": mp.nstr(mean_occ, 20),
        "polarization": mp.nstr(polarization, 20),
        "entropy_per_site": mp.nstr(entropy, 20),
        "susceptibility_Var_k_per_site": mp.nstr(Q / (1 + Q) ** 2, 20),
    })

    w.add_data("entropy_expansion", {
        "S/n": mp.nstr(entropy, 20),
        "log 2": mp.nstr(mp.log(2), 20),
        "log 2 - eta0^2/2": mp.nstr(mp.log(2) - eta ** 2 / 2, 20),
        "residual": mp.nstr(entropy - (mp.log(2) - eta ** 2 / 2), 8),
        "eta0^4": mp.nstr(eta ** 4, 8),
        "reading": "S/n = log 2 - eta_0^2/2 + O(eta_0^4); the entropy deficit from maximal "
                   "is eta_0^2/2 = " + mp.nstr(eta ** 2 / 2, 8) + " nats per strand.",
    })

    w.add_data("why_there_is_no_temperature", {
        "what_is_fixed": "the product beta*mu = log Q = 2 eta_0 = "
                         + mp.nstr(mp.log(Q), 12),
        "what_is_not": "beta alone. It appears nowhere in the construction.",
        "the_reason": "the spectrum is LINEAR in k and the multiplicities are the bare "
                      "binomials, so Z is a free two-level system with a single "
                      "dimensionless field. Rescaling beta and mu inversely leaves Z "
                      "unchanged -- there is no intrinsic energy scale to extract.",
        "upgrade_over_qou-ap3d": "that bean recorded an EMPIRICAL negative (the corpus's "
                                 "Landauer probe found no candidate kT within 5%, off by "
                                 "41.9x-4266x). This is the REASON: the construction "
                                 "cannot contain one.",
    })

    w.add_data("A1_verdict", (
        "A1 ('the extensive term is the Markov normalisation; stop dividing it out') is "
        "DEAD ON STRUCTURAL GROUNDS. What it retains is log Z = S + beta*mu*<k>, a Shannon "
        "entropy plus a dimensionless field term, both pure numbers BY CONSTRUCTION. No "
        "member of the normalisation family and no choice among the four E_0 conventions "
        "can make it an energy, because the framework contains no 1/beta. qou-78pt was "
        "reopened when its numerical refutation was withdrawn; it can now close for the "
        "right reason -- not 'no member reaches the target' but 'no member is an energy'."
    ))

    w.add_data("the_coulomb_ratio_is_not_a_new_constant", {
        "value": mp.nstr(polarization, 20),
        "corpus_route": "def:coulomb-charge -- antisymmetric/symmetric channel ratio of "
                        "E_cross = n_+ q - n_- q^{-1} at n_- = 0, i.e. (q-1/q)/(q+1/q)",
        "this_route": "polarization 2<k>/n - 1 = (Q-1)/(Q+1) of the fugacity two-level system",
        "why_identical": "multiply (q-1/q)/(q+1/q) top and bottom by q to get (q^2-1)/(q^2+1) "
                         "= (Q-1)/(Q+1). One line of algebra; not a coincidence and not a "
                         "new derivation.",
        "what_is_new": "the READING. The same ratio is simultaneously an energy ratio and a "
                       "thermal polarization. Being a ratio it is scale-free either way, "
                       "which is exactly why it survives where the extensive magnitude does "
                       "not. The framework's derived quantities are ratios and "
                       "polarizations; its one absolute magnitude is the one with no scale.",
    })

    out = w.save()
    print(f"wrote {out}")
    print(f"  Q = q0^2 (fugacity)          : {mp.nstr(Q, 15)}")
    print(f"  log Q = 2*eta0 (= beta*mu)   : {mp.nstr(mp.log(Q), 15)}")
    print(f"  <k>/n  moment                : {mp.nstr(mean_occ, 20)}")
    print(f"         (1+tanh eta0)/2       : {mp.nstr(closed, 20)}")
    print(f"  polarization 2<k>/n - 1      : {mp.nstr(polarization, 20)}")
    print(f"  corpus tanh(ln q0)           : {mp.nstr(mp.tanh(eta), 20)}")
    print(f"  S/n (Legendre)               : {mp.nstr(entropy, 20)}")
    print(f"  binary Shannon H(p)          : {mp.nstr(shannon, 20)}")
    print(f"  S/n vs log2 - eta^2/2        : residual {mp.nstr(entropy - (mp.log(2) - eta ** 2 / 2), 6)}"
          f"  (eta^4 = {mp.nstr(eta ** 4, 6)})")
    print(f"  coefficients are bare C(n,k) : {bare}   <- no Boltzmann weight, hence no beta")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
