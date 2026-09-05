#!/usr/bin/env python3
"""Bean qou-lsp9, second pass: the exclusion is not about `net`, it is
about H_2(q) being TWO-DIMENSIONAL -- and the one derived readout (the
canonical Markov trace) is excluded quantitatively.

WHAT THE FIRST PASS ESTABLISHED. `lepton_net_to_mass_bridge_exclusion.py`
excluded the multiplicative class m_n = C g^n net(n)^p on the proved
Binet asymptotics of the Morgan-Voyce continuant. That is correct, but
it is stated for ONE readout -- the unweighted net a_n + b_n -- and a
referee's first question is "so use the Markov trace instead".

THE GENERALISATION. H_2(q) has dimension 2! = 2, basis {1, sigma_0}, and
NF(sigma_0^w) = a_w * 1 + b_w * sigma_0 with a_w = b_{w-1}. So EVERY
linear functional phi on H_2(q) -- every possible way of reading a number
off the lepton's own braid -- is

    phi(sigma_0^w) = alpha * b_{w-1} + beta * b_w,
    alpha = phi(1),  beta = phi(sigma_0).

net is (alpha, beta) = (1, 1). The canonical Markov trace is
(alpha, beta) = (1, z) with z = 1/(q^{1/2} + q^{-1/2}), tr_M(1) = 1.
Both are single points of one two-parameter family.

THE INVARIANT (sorry-free Lean twin, `lepton_continuant_binet.lean`, §3:
`linFunctionalK_binet`, `linFunctionalK_two_step`,
`linFunctionalK_exactly_geometric`):

    phi(n) * (q + 1/q) = A q^n - (-1)^n B q^{-n},
        A = alpha + beta q,   B = alpha - beta / q

    phi(n+2) = q^2 phi(n) + (-1)^n (q - 1/q) B q^{-n}.

Every readout advances by the SAME factor q^2 per generation step; the
choice (alpha, beta) survives only inside B, so it can rescale the
vanishing correction but not the q^2. The degenerate direction B = 0
(alpha = beta/q) is EXACTLY geometric -- the one member that could have
behaved differently is the most rigid of all.

WHAT THIS DOES AND DOES NOT EXCLUDE. Honest scoping, because the naive
reading over-claims:

  (i) GENERIC READOUT -- EXCLUDED, scope-(b). If phi has no zero inside
      the generation window, its two-step ratios are q^2 (1 + O(q^{-2n}))
      and the tower is log-linear, while the observed one is log-concave
      (log-increments 5.332 then 2.822). In particular the CANONICAL
      Markov trace is such a readout, and this script measures how far it
      is from working. That is the derived case, and it fails.

 (ii) NODE READOUT -- the one escape, and POSITIVITY closes it. phi
      vanishes at real index n* = ln(B/A) / (2 ln q). Tuning A/B so a node
      sits just below the electron winding makes r_1 = phi(4)/phi(2)
      arbitrarily large, which CAN reproduce 206.8, so "no linear readout
      works" is FALSE as a bare statement and the escape is solved for
      here explicitly (a quadratic in u = A/B) rather than buried.

      Both roots come out with beta/alpha < 0: every escape requires
      phi(1) and phi(sigma_0) of OPPOSITE SIGN. But for q > 1 the Hecke
      parameter h = q - 1/q is positive, so the continuant b is positive
      from b_1 on, and any readout with alpha >= 0, beta > 0 is strictly
      positive at every index -- it has no node anywhere, not merely none
      inside the window. The canonical Markov trace is such a readout
      (tr_M(1) = 1, tr_M(sigma_0) = z > 0). So the escape is unavailable
      to the only derived candidate, which is what makes the exclusion
      scope-(b) rather than a failed search. Sorry-free Lean twins in
      `lepton_continuant_positivity.lean`: `linFunctionalK_pos`,
      `markovReadout_pos`.

      (Even granting a sign-indefinite readout, the class (A/B, g, p) is
      3 free parameters against 2 observed ratios -- underdetermined, so
      it would predict nothing at winding 9 in any case.)

q_0 CONVENTION. Experimental/proton pin (`q_parameter.Q_MP`) per the
2026-08-07 owner directive. No ideal-layer cache is read, so no layer
straddling is possible.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

# Shared, unit-tested maths (see test_lepton_tower_bend.py).
from lepton_tower_core import markov_z, morgan_voyce_b  # noqa: E402

from mpmath import mp, mpf, log, sqrt  # noqa: E402
from codata_constants import M_E_MEV

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# CODATA / PDG lepton masses (MeV). TARGETS of the excluded map only --
# nothing here is fitted to them except where explicitly labelled a fit.
M_E = M_E_MEV
M_MU = mpf("105.6583755")
M_TAU = mpf("1776.86")

# Corpus generation assignment: lepton at generation k is T(2, 2k+1).
WINDINGS = (3, 5, 7)




def main() -> None:
    set_compute_dps()
    q = mp.mpf(Q_MP)
    h = q - 1 / q
    z = markov_z(q)                          # canonical Markov parameter

    N = 15
    b = morgan_voyce_b(N, h)

    def phi(alpha, beta, w):
        """The linear readout at winding w: alpha*a_w + beta*b_w, a_w = b_{w-1}."""
        return alpha * b[w - 1] + beta * b[w]

    def amp(alpha, beta):
        """(A, B) of the Binet decomposition."""
        return alpha + beta * q, alpha - beta / q

    # --- (1) the master identity, verified against the recurrence ---------
    # phi(w) * (q + 1/q) = A q^{w-1} - (-1)^{w-1} B q^{-(w-1)}
    probe_pairs = {
        "net": (mpf(1), mpf(1)),
        "markov_trace_canonical": (mpf(1), z),
        "sigma_only": (mpf(0), mpf(1)),
        "identity_only": (mpf(1), mpf(0)),
        "degenerate_B_zero": (1 / q, mpf(1)),   # alpha = beta/q  =>  B = 0
        "asymmetric": (mpf("-0.37"), mpf("2.9")),
    }
    identity_err = mpf(0)
    for alpha, beta in probe_pairs.values():
        A, B = amp(alpha, beta)
        for w in range(1, N):
            n = w - 1
            lhs = phi(alpha, beta, w) * (q + 1 / q)
            rhs = A * q**n - (-1) ** n * B * q ** (-n)
            identity_err = max(identity_err, abs(lhs - rhs))

    # --- (2) two-step rigidity: every readout advances by q^2 -------------
    q2 = q**2
    two_step_err = mpf(0)
    for alpha, beta in probe_pairs.values():
        _, B = amp(alpha, beta)
        for w in range(1, N - 2):
            n = w - 1
            lhs = phi(alpha, beta, w + 2)
            rhs = q2 * phi(alpha, beta, w) + (-1) ** n * h * B * q ** (-n)
            two_step_err = max(two_step_err, abs(lhs - rhs))

    # --- (3) the observed tower --------------------------------------------
    obs_r1 = M_MU / M_E        # e -> mu   (windings 3 -> 5)
    obs_r2 = M_TAU / M_MU      # mu -> tau (windings 5 -> 7)
    obs_bend = obs_r1 / obs_r2         # 12.295 -- the log-concavity
    log_inc_obs = [log(obs_r1), log(obs_r2)]

    # --- (4) per-readout tower shape ---------------------------------------
    readouts = {}
    for name, (alpha, beta) in probe_pairs.items():
        p3, p5, p7 = (phi(alpha, beta, w) for w in WINDINGS)
        r1, r2 = p5 / p3, p7 / p5
        A, B = amp(alpha, beta)
        # node location: phi vanishes where A q^n = (-1)^n B q^{-n}
        node = None
        if A != 0 and B != 0 and (B / A) > 0:
            node = log(B / A) / (2 * log(q))
        readouts[name] = {
            "alpha": str(alpha),
            "beta": str(beta),
            "A_growing_amplitude": str(A),
            "B_decaying_amplitude": str(B),
            "ratio_w3_to_w5": str(r1),
            "ratio_w5_to_w7": str(r2),
            "log_increments": [str(log(abs(r1))), str(log(abs(r2)))],
            "bend_r1_over_r2": str(r1 / r2),
            "node_index_n_star": (str(node) if node is not None else None),
            # a pure power law m = C phi^p needs ONE p; report both
            "p_required_step_1": str(log(obs_r1) / log(abs(r1))),
            "p_required_step_2": str(log(obs_r2) / log(abs(r2))),
        }

    # --- (5) the DERIVED readout, measured -------------------------------
    a_c, b_c = probe_pairs["markov_trace_canonical"]
    c3, c5, c7 = (phi(a_c, b_c, w) for w in WINDINGS)
    cr1, cr2 = c5 / c3, c7 / c5
    canonical_bend = cr1 / cr2
    # The whole class m = C g^w phi^p has m-bend = phi-bend^p, so:
    p_canonical = log(obs_bend) / log(canonical_bend)

    # --- (6) the node escape: solve EXACTLY for the readout that DOES bend -
    # With u = A/B, phi(w) ∝ u q^{w-1} - (-1)^{w-1} q^{-(w-1)}; windings
    # 3,5,7 give n = 2,4,6 (even), so phi ∝ u q^n - q^{-n}. Writing
    # f_n = u q^n - q^{-n}, bend(u) = f_4^2 / (f_2 f_6), and
    # bend(u) = R rearranges to a QUADRATIC in u:
    #
    #   (1-R) q^8 u^2 + [ R(q^4 + q^-4) - 2 ] u + (1-R) q^-8 = 0
    #
    # Solved in closed form -- the earlier root-finder start point was not
    # bracketed and returned nothing, which would have hidden the escape.
    def bend_of_u(u):
        f2 = u * q**2 - q ** (-2)
        f4 = u * q**4 - q ** (-4)
        f6 = u * q**6 - q ** (-6)
        return (f4 / f2) / (f6 / f4)

    u_node = q ** (-4)     # exact zero of phi at n = 2 (the electron)
    R = obs_bend
    qa = (1 - R) * q**8
    qb = R * (q**4 + q ** (-4)) - 2
    qc = (1 - R) * q ** (-8)
    disc = qb**2 - 4 * qa * qc
    u_roots = []
    if disc >= 0:
        for sgn in (1, -1):
            u_roots.append((-qb + sgn * sqrt(disc)) / (2 * qa))

    def beta_over_alpha(u):
        """Invert u = (1 + t q)/(1 - t/q) for t = beta/alpha."""
        return (u - 1) / (q + u / q)

    node_solutions = []
    for u_r in u_roots:
        t = beta_over_alpha(u_r)
        node_solutions.append({
            "u": str(u_r),
            "bend_roundtrip": str(bend_of_u(u_r)),
            "residual": str(abs(bend_of_u(u_r) - obs_bend)),
            "implied_beta_over_alpha": str(t),
            "sign_of_beta_over_alpha": ("negative" if t < 0 else "positive"),
            "ratio_to_canonical_z": str(t / z),
        })
    escape_all_negative = bool(
        node_solutions
        and all(s["sign_of_beta_over_alpha"] == "negative" for s in node_solutions)
    )
    u_canonical = (a_c + b_c * q) / (a_c - b_c / q)

    results = {
        "master_identity": {
            "formula": "phi(w)*(q+1/q) = A q^{w-1} - (-1)^{w-1} B q^{-(w-1)}",
            "A": "alpha + beta*q",
            "B": "alpha - beta/q",
            "max_abs_err_over_6_readouts_w_1_to_14": str(identity_err),
            "verified": identity_err < mpf("1e-40"),
            "lean_twin": "QOU.Archimedean.linFunctionalK_binet",
        },
        "two_step_rigidity": {
            "formula": "phi(w+2) = q^2 phi(w) + (-1)^{w-1} h B q^{-(w-1)}",
            "max_abs_err": str(two_step_err),
            "verified": two_step_err < mpf("1e-40"),
            "reading": (
                "every H_2(q)-linear readout advances by the SAME q^2 per "
                "generation step; (alpha,beta) survives only inside B, so "
                "it rescales the vanishing correction, never the q^2"
            ),
            "lean_twin": "QOU.Archimedean.linFunctionalK_two_step",
        },
        "q_squared": str(q2),
        "observed_tower": {
            "m_mu_over_m_e": str(obs_r1),
            "m_tau_over_m_mu": str(obs_r2),
            "bend_r1_over_r2": str(obs_bend),
            "log_increments": [str(x) for x in log_inc_obs],
            "log_concave": bool(log_inc_obs[0] > log_inc_obs[1]),
        },
        "readouts": readouts,
        "canonical_markov_readout": {
            "z": str(z),
            "alpha_beta": ["1", str(z)],
            "u_equals_A_over_B": str(u_canonical),
            "ratios": [str(cr1), str(cr2)],
            "bend": str(canonical_bend),
            "observed_bend": str(obs_bend),
            "p_required_to_match_bend": str(p_canonical),
            "verdict": (
                "EXCLUDED. The derived readout has no node in the "
                "generation window, so its bend is 1 + O(q^{-2n}) while "
                "the observed bend is 12.3; matching it needs the "
                "exponent above, which is the same exponential "
                "fine-tuning the net showed. This is the case that "
                "matters, because z is derived rather than chosen."
            ),
        },
        "node_escape": {
            "mechanism": (
                "phi has a real zero at n* = ln(B/A)/(2 ln q). Placing a "
                "node just below the electron winding makes r_1 large, "
                "which CAN reproduce 206.8. Reported rather than buried, "
                "because the blanket claim 'no linear readout works' "
                "would be FALSE without the positivity argument below."
            ),
            "u_at_exact_electron_node": str(u_node),
            "solved_exactly_as_quadratic_in_u": True,
            "discriminant": str(disc),
            "solutions": node_solutions,
            "canonical_z": str(z),
            "every_escape_needs_opposite_signs": escape_all_negative,
            "why_positivity_closes_it": (
                "EVERY solution has beta/alpha < 0, i.e. requires phi(1) "
                "and phi(sigma_0) of OPPOSITE SIGN. For q > 1 the Hecke "
                "parameter h = q - 1/q is positive, so the continuant is "
                "positive from b_1 on; hence any readout with alpha >= 0 "
                "and beta > 0 is strictly positive at every index and has "
                "NO node at all. The canonical Markov trace is such a "
                "readout (tr_M(1) = 1 > 0, tr_M(sigma_0) = z > 0), so the "
                "escape is unavailable to it. Sorry-free Lean twin "
                "(lepton_continuant_positivity.lean): "
                "QOU.Archimedean.linFunctionalK_pos / markovReadout_pos."
            ),
            "why_it_would_not_be_a_derivation_anyway": (
                "even granting a sign-indefinite readout, the class "
                "(A/B, g, p) carries THREE free parameters against TWO "
                "observed ratios -- underdetermined, so a solution family "
                "exists for trivial counting reasons and predicts nothing "
                "at winding 9."
            ),
        },
        "verdict": (
            "Generalises the first-pass net exclusion from one readout to "
            "the whole 2-parameter space of H_2(q)-linear readouts. "
            "Scope-(b) for every POSITIVE readout -- including the "
            "canonical Markov trace, the only derived candidate -- on the "
            "proved invariant that the continuant is positive for q > 1, "
            "so a positive readout has no node and its tower is log-linear "
            "up to O(q^{-2n}) while the observed tower is log-concave. "
            "The only escape is a sign-indefinite readout, which no trace "
            "supplies and which would in any case be a 3-parameter fit to "
            "2 numbers."
        ),
    }

    all_ok = (
        results["master_identity"]["verified"]
        and results["two_step_rigidity"]["verified"]
        and results["observed_tower"]["log_concave"]
        and abs(p_canonical) > 10          # canonical readout is far off
        and escape_all_negative            # positivity closes the escape
    )

    w = WitnessBuilder(
        "lepton-linear-readout-rigidity",
        _script_path=__file__,
    )
    w.set_description(
        "Bean qou-lsp9 second pass. Every linear functional on the "
        "2-dimensional H_2(q) evaluated along the lepton generation "
        "braids obeys one two-step recursion with ratio q^2; the "
        "canonical Markov-trace readout is excluded quantitatively, and "
        "the surviving node escape is identified as a 3-parameter fit "
        "to 2 numbers rather than a derivation."
    )
    w.set_content_block("prop:lepton-continuant-recurrence")
    w.add_parameter("q0_anchor", "experimental/proton (q_parameter.Q_MP)")
    w.add_parameter("q0", str(q))
    w.add_parameter("h", str(h))
    w.add_parameter("z_markov", str(z))
    for k, v in results.items():
        w.add_data(k, v)
    w.add_data("all_checks_passed", all_ok)
    # Assertions (bean qou-srvu). This witness carried none, so `allPassed:
    # true` was vacuous -- green over an empty list. The two residuals below
    # were already computed and already compared against `mpf("1e-40")` at the
    # `verified` keys above; they were recorded as data and never asserted.
    #
    # THRESHOLD PROVENANCE: 1e-40 is this file's OWN declared bar, written
    # twice in `results` above as `... < mpf("1e-40")`. It is not a number
    # chosen to match the observation -- the measured margin is ~30 orders of
    # magnitude of headroom (4.3e-70 and 7.2e-71 against a 1e-40 bar).
    #
    # NOT asserted: `abs(p_canonical) > 10` (the 10 is an undeclared
    # order-of-magnitude bar with no stated provenance) and the composite
    # `all_ok` that depends on it.
    w.add_assertion(
        "master_identity_max_abs_err_over_6_readouts_w_1_to_14",
        computed=str(identity_err),
        expected="0",
        tolerance="1e-40",
        source="phi(w)*(q+1/q) = A q^{w-1} - (-1)^{w-1} B q^{-(w-1)}; "
               "Lean twin QOU.Archimedean.linFunctionalK_binet. Bar is this "
               "file's own mpf('1e-40')",
    )
    w.add_assertion(
        "two_step_rigidity_max_abs_err",
        computed=str(two_step_err),
        expected="0",
        tolerance="1e-40",
        source="phi(w+2) = q^2 phi(w) + (-1)^{w-1} h B q^{-(w-1)}; "
               "Lean twin QOU.Archimedean.linFunctionalK_two_step. Bar is this "
               "file's own mpf('1e-40')",
    )
    w.add_caveat(
        "Scope-(b) covers H_2(q)-linear readouts with no node in the "
        "generation window (including the canonical Markov trace). "
        "Readouts with a node are NOT excluded; they are unconstrained "
        "(3 parameters, 2 observations). Nothing here touches "
        "non-linear or non-H_2 bridges -- an additive interface term, "
        "or a route where the generation index enters through linking "
        "with the hyperbolic Higgs knot 4_1 -- which remain open "
        "(bean qou-htk4)."
    )
    w.save()

    print(f"q_0 (proton pin)   = {q}")
    print(f"h = q - 1/q        = {h}")
    print(f"z (Markov)         = {z}")
    print(f"master identity err= {identity_err}")
    print(f"two-step rigid err = {two_step_err}")
    print(f"observed bend      = {obs_bend}")
    print()
    for name, r in readouts.items():
        print(f"{name:26s} bend={r['bend_r1_over_r2'][:12]:>13s}  "
              f"log-incs={r['log_increments'][0][:7]}, {r['log_increments'][1][:7]}")
    print()
    print(f"CANONICAL tr_M: bend={canonical_bend}, needs p={p_canonical}")
    for s_ in node_solutions:
        print(f"node escape:    u={s_['u'][:10]}  beta/alpha="
              f"{s_['implied_beta_over_alpha'][:12]} ({s_['sign_of_beta_over_alpha']})"
              f"  x canonical z = {s_['ratio_to_canonical_z'][:8]}")
    print(f"all escapes need opposite signs = {escape_all_negative} "
          f"-> positivity forecloses them")
    print(f"VERDICT: canonical readout EXCLUDED (all_checks_passed={all_ok})")


if __name__ == "__main__":
    main()
