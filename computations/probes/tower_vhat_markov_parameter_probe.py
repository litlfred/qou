#!/usr/bin/env python3
"""The tower's V̂ is affine in a Markov parameter — and that parameter is
NEITHER convention C NOR convention D.  Measuring it says which knob actually
sets the distance to the Φ_q pole (beans qou-xsue, qou-dchz, qou-2tuv).

WHAT IS BEING MEASURED, AND WHY IT IS THE RIGHT QUANTITY.

`QOU.BraidsAndKnots.prod_eq_linear` (this branch, sorry-free) proves that any
product of linear factors in ONE Hecke generator is linear in that generator:

    Π_k (c_k σ_i + d_k) = α_i σ_i + β_i

with (α, β) built by `collapseStep`.  Both tower producers run exactly that
recursion — `mass_at_3A_proper.per_generator_V_hat_3A` at lines 918-923 and
`mass_endomorphism.additive_wedderburn_volumes` at line 128 — and then take a
weighted trace of the result.  So both V̂ are of the shape

    V̂_i = α_i · Z + β_i · W,      Z := Σ_λ ω_λ tr(σ^λ)/dim λ,  W := Σ_λ ω_λ

which `QOU.BraidsAndKnots.vHat` names and `vHat_sub_vHat` says is AFFINE in Z.
`vHat_margin` then gives the conditioning: the margin to the Φ_q pole at |V̂| = q,
measured in Z, is the margin measured in V̂ **divided by α**.  So `α` is the
amplification from "how far the Markov parameter moved" to "how far the pole
moved", and Z is the only place a convention can enter.

THE QUESTION THIS SETTLES.  Bean `qou-dchz` item 1 records Φ_q towers that
converged under convention C (z = √q/(q+1) = 0.4993203) and emit `+inf` under
the canonical convention D (z = q³/(q²+1) = 0.6126880), D being 22.70 % larger
and hence closer to the pole.  It is natural to read the `mass_at_3A_proper`
pole problem (`qou-2tuv`; the docstring's "V̂ at 1.08837 against a cap of
1.087779") as the same effect.  It is not, and the difference matters for what
would fix it: that producer's weights are `normalized_plancherel`, whose own
docstring concedes it does not match "the canonical Jones parameter z for
tr_M(σ_i)".  This measures by how much.

EXACT ARITHMETIC.  σ_i in the Young-seminormal representation has only the two
Hecke eigenvalues q and −q⁻¹, so

    tr(σ^λ) = m₊ · q − m₋ · q⁻¹,   m₊ + m₋ = dim λ,   m₊ ∈ ℤ.

The committed producer builds those matrices in float64.  Rather than carry that
float into the answer (AGENTS.md §PROBES ARE NOT EXEMPT, rule 3), the float64
trace is used ONLY to identify the integer m₊ — the probe asserts the recovered
value is within 1e-6 of an integer before rounding — and every reported quantity
is then recomputed from that integer in mpmath at 50 dps.  `q`, the weights and
both conventions are mpf throughout.

WHAT THIS DOES NOT CLAIM.  Nothing here says what the right V̂ is.  The
`per_generator_V_hat_3A` docstring's verdict stands — "Both schemes are wrong
for the tower; that is the finding, and picking between them is not the fix" —
and this probe is scope-(a): it measures the constructions as built.  No
ingredient is excluded by it.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

import _path_bridge  # noqa: F401,E402
from mpmath import mp, mpf  # noqa: E402

mp.dps = 50

import mass_at_3A_proper as M3A  # noqa: E402
from q_parameter import Q_MP as Q_EXACT  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

Q = Q_EXACT
QI = 1 / Q

# The two Markov-parameter conventions, exact at 50 dps.
Z_C = mp.sqrt(Q) / (Q + 1)          # convention C — excised 2026-08-09/08-15
Z_D = Q ** 3 / (Q ** 2 + 1)         # convention D — canonical


def _fmt(x) -> str:
    return mp.nstr(mpf(x), 20)


def sigma_plus_multiplicity(shape: tuple[int, ...]) -> tuple[int, int, float]:
    """`m₊` for `shape`: the multiplicity of the eigenvalue `q` in σ_i.

    Recovered from the producer's own float64 seminormal matrix, then used only
    as an integer.  Returns `(m_plus, dim, distance_to_integer)` so the caller
    can assert the recovery was unambiguous rather than assume it.

    All σ_i are conjugate in H_n, so `m₊` does not depend on `i`; index 0 is
    read and the caller may rely on that.
    """
    import numpy as np

    sigmas, dim, _syts = M3A._cached_seminormal(shape, M3A.Q0_PROTON)
    if dim == 0:
        return 0, 0, 0.0
    s0 = sigmas[0]
    try:
        from scipy import sparse as sp_sparse
        tr_f64 = float(s0.diagonal().sum()) if sp_sparse.issparse(s0) else float(np.trace(s0))
    except ImportError:
        tr_f64 = float(np.trace(s0))
    # tr = m₊ q − (dim − m₊) q⁻¹  ⇒  m₊ = (tr + dim·q⁻¹) / (q + q⁻¹)
    q_f = float(M3A.Q0_PROTON)
    raw = (tr_f64 + dim / q_f) / (q_f + 1.0 / q_f)
    m_plus = int(round(raw))
    return m_plus, dim, abs(raw - m_plus)


def markov_parameter(A: int, scheme: str) -> dict:
    """`Z` and `W` for the given weight scheme at H_{3A}, in exact arithmetic.

    `Z = Σ_λ ω_λ tr(σ^λ)/dim λ` is the effective Markov parameter the tower's
    V̂ is affine in; `W = Σ_λ ω_λ` is what multiplies the identity coefficient.
    A weight scheme is a genuine Markov trace exactly when `W = 1`.
    """
    n = 3 * A
    # Q_EXACT, not the module default: both helpers take `q` and return mpf
    # when handed one, so the weight table is exact rather than an f64 table
    # re-read as mpf.  Measured difference: it moves Sigma omega_lambda for the
    # deuteron from 1 - 3.1e-16 to 1 exactly, which is the difference between
    # "is a Markov trace" holding and being 3e-16 short of holding.
    if scheme == "normalized_plancherel":
        table = M3A.normalized_plancherel_weights_3A(A, Q)
    elif scheme == "plancherel":
        nfac = M3A.qfac(n, Q)
        table = [(s, (M3A.dim_q(s, Q) ** 2) / nfac)
                 for s in M3A.partitions_of(n)]
    else:
        raise ValueError(scheme)

    Z = mpf(0)
    W = mpf(0)
    worst_int_dist = 0.0
    rows = []
    for shape, w_exact in table:
        m_plus, dim, dist = sigma_plus_multiplicity(shape)
        if dim == 0:
            continue
        worst_int_dist = max(worst_int_dist, dist)
        w = mpf(w_exact)
        # tr(σ^λ)/dim λ, exact given the integer multiplicity.
        tr_over_dim = (m_plus * Q - (dim - m_plus) * QI) / dim
        Z += w * tr_over_dim
        W += w
        rows.append({
            "partition": list(shape), "dim": dim, "m_plus": m_plus,
            "weight": _fmt(w), "tr_over_dim": _fmt(tr_over_dim),
        })
    return {"scheme": scheme, "n": n, "Z": Z, "W": W,
            "worst_integer_recovery_distance": worst_int_dist,
            "per_partition": rows}


def per_generator_alpha_beta(Z_num: int, N_num: int) -> list[dict]:
    """`(α_i, β_i)` per generator, by the producer's own recursion.

    Re-run here rather than imported because `per_generator_V_hat_3A` does not
    return them; the recursion is the one `prod_eq_linear` proves, and `δ` is
    taken at `Q0_PROTON` exactly as the producer takes it — but as `mpf`, so
    the coefficients carry no float64 rounding of their own.  The word itself
    is read from the producer.
    """
    A = Z_num + N_num
    n_strands = 3 * A
    n_gens = n_strands - 1
    word = M3A.atom_braid_word_3A(Z_num, N_num)
    by_gen: list[list] = [[] for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            by_gen[g].append((c, d))

    delta = Q - QI
    out = []
    for i in range(n_gens):
        a, b = mpf(0), mpf(1)
        for (c, d) in by_gen[i]:
            cc, dd = mpf(str(c)), mpf(str(d))
            a, b = a * cc * delta + a * dd + b * cc, a * cc + b * dd
        out.append({"gen": i, "alpha": a, "beta": b, "n_factors": len(by_gen[i])})
    return out


def analyse(Z_num: int, N_num: int, label: str) -> dict:
    """Everything the Lean says about one atom, measured."""
    A = Z_num + N_num
    ab = per_generator_alpha_beta(Z_num, N_num)
    schemes = {s: markov_parameter(A, s)
               for s in ("normalized_plancherel", "plancherel")}

    # The producer's own V̂, to check the affine form reproduces it.
    # Pinned to the scheme this probe analyses: #8521 moved the default to
    # "jones_wenzl" (convention D, owner 2026-11-18); the affine-form check below
    # is a statement about normalized_plancherel and is kept as one.
    prod = M3A.per_generator_V_hat_3A(Z_num, N_num, weight_scheme="normalized_plancherel")
    prod_V = [mpf(str(float(d["full"]))) for d in prod]

    gens = []
    npl = schemes["normalized_plancherel"]
    for rec, V_prod in zip(ab, prod_V):
        alpha, beta = rec["alpha"], rec["beta"]
        V_affine = alpha * npl["Z"] + beta * npl["W"]
        row = {
            "gen": rec["gen"],
            "n_factors": rec["n_factors"],
            "alpha": _fmt(alpha),
            "beta": _fmt(beta),
            "V_hat_affine": _fmt(V_affine),
            "V_hat_producer": _fmt(V_prod),
            "affine_vs_producer_abs": _fmt(abs(V_affine - V_prod)),
            "V_hat_over_q": _fmt(abs(V_affine) / Q),
        }
        # vHat_eq_iff: the Markov parameter that would put V̂ exactly on the pole.
        if alpha != 0:
            z_star = (Q - beta * npl["W"]) / alpha
            row["z_star_pole"] = _fmt(z_star)
            # vHat_margin: margin in Z = margin in V̂ divided by alpha.
            row["margin_in_Z"] = _fmt(z_star - npl["Z"])
            row["margin_in_Vhat_over_alpha"] = _fmt((Q - V_affine) / alpha)
        else:
            row["z_star_pole"] = None
            row["margin_in_Z"] = None
            row["margin_in_Vhat_over_alpha"] = None
        gens.append(row)

    return {
        "atom": label, "Z": Z_num, "N": N_num, "A": A, "n_generators": len(ab),
        "markov_parameters": {
            s: {"Z_eff": _fmt(v["Z"]), "W_sum": _fmt(v["W"]),
                "is_markov_trace_W_eq_1": bool(abs(v["W"] - 1) < mpf("1e-40")),
                    # Serialized as a STRING, not a float: it is an f64 diagnostic
                # (how far the f64-derived value sat from the integer it was
                # rounded to) and cannot be made exact, so emitting it as a
                # JSON number would put raw float64 in the witness for a
                # quantity that is only ever read as "small enough".
                "worst_integer_recovery_distance":
                    f"{v['worst_integer_recovery_distance']:.6e}",
                "per_partition": v["per_partition"]}
            for s, v in schemes.items()},
        "generators": gens,
        "max_abs_V_hat": _fmt(max(abs(mpf(g["V_hat_affine"])) for g in gens)),
    }


def conjugate_partition(shape: tuple[int, ...]) -> tuple[int, ...]:
    """The transpose (conjugate) of a partition."""
    if not shape:
        return ()
    return tuple(sum(1 for r in shape if r > j) for j in range(shape[0]))


def verify_lean_hypotheses(A: int) -> dict:
    """Check the three hypotheses `markov_param_eq_half_h` runs on, then its
    conclusion — against the production weight table, not against a model of it.

    A theorem is only as useful as its instantiation, and the failure mode this
    guards against is a correct proof of something the code does not satisfy.
    So: transpose-symmetry of the weights, the eigenvalue exchange
    `m₊(λ') = m₋(λ)`, the pair identity `t(λ) + t(λ') = h`, and finally
    `Z = h/2` at 45 digits.
    """
    h = Q - QI
    table = M3A.normalized_plancherel_weights_3A(A, Q)
    wmap = {tuple(s): mpf(w) for s, w in table}

    worst_w_asym = mpf(0)
    worst_pair_dev = mpf(0)
    exchange_ok = True
    rows = []
    for shape in wmap:
        conj = conjugate_partition(shape)
        if conj not in wmap:
            exchange_ok = False
            rows.append({"partition": list(shape), "conjugate_missing": True})
            continue
        worst_w_asym = max(worst_w_asym, abs(wmap[conj] - wmap[shape]))
        mp_s, d_s, _ = sigma_plus_multiplicity(shape)
        mp_c, d_c, _ = sigma_plus_multiplicity(conj)
        if not (d_s == d_c and mp_c == d_s - mp_s):
            exchange_ok = False
        t_s = (mp_s * Q - (d_s - mp_s) * QI) / d_s
        t_c = (mp_c * Q - (d_c - mp_c) * QI) / d_c
        worst_pair_dev = max(worst_pair_dev, abs(t_s + t_c - h))
        rows.append({
            "partition": list(shape), "conjugate": list(conj),
            "dim": d_s, "m_plus": mp_s, "m_plus_conjugate": mp_c,
        })

    Z = markov_parameter(A, "normalized_plancherel")["Z"]
    return {
        "A": A, "n": 3 * A,
        "h_eq_q_minus_qinv": _fmt(h),
        "half_h": _fmt(h / 2),
        "Z_eff": _fmt(Z),
        "abs_Z_minus_half_h": _fmt(abs(Z - h / 2)),
        "worst_weight_transpose_asymmetry": _fmt(worst_w_asym),
        "worst_trace_pair_deviation_from_h": _fmt(worst_pair_dev),
        "eigenvalue_exchange_holds": bool(exchange_ok),
        "per_partition": rows,
    }


def pn_identity_coefficient_relation() -> dict:
    """The proton's identity coefficient IS the neutron's V̂ — and why.

    Measured: at generator 1 of the canonical atom words,
    `β(proton) = 1.0883675333971881277792…= V̂(neutron)`, agreeing to ~50
    digits at 60 dps.  That is far too sharp to be an accident and far too
    specific to leave as one.

    It is `QOU.BraidsAndKnots.identity_coeff_avg_eq_trace_full`.  The two words
    differ in exactly one factor — `σ − h/2` for the proton against `σ − h` for
    the neutron — and appending the averaged factor then reading the identity
    coefficient is the *same linear functional* as appending the full factor
    then taking the Markov trace at `z = h/2`.  Both are `α − β·h/2`.  It holds
    for every prefix, over any field; nothing about this word, this `q` or this
    atom is used.

    `d = −h/2` is `AveragedCrossingCollapse`'s averaged crossing, the value
    `2d = −h` at which the σ-coefficient vanishes.

    Also checked here: every factor in `atom_braid_word_3A` has `c = 1` and
    `d ∈ {0, −h/2, −h}`, so every collapsed word is a product of just three
    distinct factors.  That is what makes the relation above reachable at all.
    """
    h = Q - QI
    ab_p = per_generator_alpha_beta(1, 0)
    ab_n = per_generator_alpha_beta(0, 1)
    beta_p = ab_p[1]["beta"]
    Z = markov_parameter(1, "normalized_plancherel")["Z"]
    V_n = ab_n[1]["alpha"] * Z + ab_n[1]["beta"]

    # The general identity, on the actual prefixes rather than on a model.
    # x = (σ − h)³ is the shared prefix of both generator-1 words.
    def step(ab, cd):
        a, b = ab
        c, d = cd
        return (a * (c * h + d) + b * c, a * c + b * d)

    x = (mpf(0), mpf(1))
    for _ in range(3):
        x = step(x, (mpf(1), -h))
    lhs = step(x, (mpf(1), -(h / 2)))[1]              # identity coeff, averaged
    rhs_pair = step(x, (mpf(1), -h))                  # full factor
    rhs = (h / 2) * rhs_pair[0] + rhs_pair[1]         # Markov trace at h/2

    # Every factor is (1, d) with d drawn from the FOUR-value template
    # `atom_braid_word_3A`'s docstring states: {0, -h, -h/2, -h(1/2 - delta/4)}.
    #
    # An earlier version of this check listed only the first three and FAILED,
    # by 7.19e-5, on exactly one factor out of 45 — the single inter-nucleon
    # generator.  That factor is the colour-weighted p-n interface
    # (pn_convention = "bring_color_weighted", canonical per the 2026-08-15
    # owner ruling R3), and the 7.19e-5 is its whole V̂.  The check is fixed by
    # stating the template correctly, not by widening a tolerance.
    #
    # `delta` is solved for from that one factor.  Note that predicting the
    # inter-nucleon V̂ from the solved delta is then CIRCULAR — `V̂ = h/2 + d`
    # and `delta := 4(1/2 + d/h)` give `h·delta/4 = h/2 + d` identically, so
    # that comparison can only ever pass.  (An earlier draft of this file
    # asserted the opposite, "a wrong delta cannot make this pass"; it is
    # recorded rather than deleted because the shape recurs.)  The content is
    # in the INDEPENDENT check below: the solved delta must equal
    # `pyhecke.constants.flavor_split_leading(q)`, which knows nothing about
    # this word.  That is what identifies the fourth template value as the
    # colour weighting rather than merely naming it so.
    delta_solved = None
    worst_factor_dev = mpf(0)
    n_factors = 0
    raw_d: list = []          # the mpf values themselves — NOT round-tripped
    seen_d: dict[str, int] = {}
    for (Zn, Nn) in ((1, 0), (0, 1), (1, 1)):
        for (c, d, _g) in M3A.atom_braid_word_3A(Zn, Nn):
            n_factors += 1
            dv = mpf(str(d))
            raw_d.append(dv)
            seen_d[_fmt(dv)] = seen_d.get(_fmt(dv), 0) + 1
            worst_factor_dev = max(worst_factor_dev, abs(mpf(str(c)) - 1))
            if min(abs(dv - a) for a in (mpf(0), -(h / 2), -h)) > mpf("1e-45"):
                # the colour-weighted one: d = -h(1/2 - delta/4)
                delta_solved = 4 * (mpf(1) / 2 + dv / h)
    # Compare against the RAW values.  Keying this loop off `seen_d` instead
    # would compare 20-digit round-trips and report a spurious ~5e-21 floor
    # that is this file's serializer, not the corpus (it did, before this note).
    allowed = [mpf(0), -(h / 2), -h]
    if delta_solved is not None:
        allowed.append(-(h * (mpf(1) / 2 - delta_solved / 4)))
    for dv in raw_d:
        worst_factor_dev = max(worst_factor_dev,
                               min(abs(dv - a) for a in allowed))

    # inter_nucleon_vHat: that generator's V̂ must be h*delta/4, predicted from
    # the delta solved above rather than read back off the same number.
    inter_pred = h * delta_solved / 4 if delta_solved is not None else None
    inter_meas = per_generator_alpha_beta(1, 1)[2]
    Z2 = markov_parameter(2, "normalized_plancherel")["Z"]
    inter_V = inter_meas["alpha"] * Z2 + inter_meas["beta"]

    # THE INDEPENDENT CHECK. `flavor_split_leading` is the closed form the
    # braid-word builder's own docstring names as the source of delta; it takes
    # only q and has never seen this word.
    from pyhecke.constants import flavor_split_leading
    delta_closed_form = mpf(flavor_split_leading(Q))

    return {
        "flavor_split_delta_solved_from_word": _fmt(delta_solved),
        "flavor_split_leading_closed_form": _fmt(delta_closed_form),
        "flavor_split_abs_difference": _fmt(abs(delta_solved - delta_closed_form)),
        "inter_nucleon_vHat_predicted_h_delta_over_4": _fmt(inter_pred),
        "inter_nucleon_vHat_measured": _fmt(inter_V),
        "inter_nucleon_vHat_abs_difference": _fmt(abs(inter_pred - inter_V)),
        "distinct_d_values": seen_d,
        "beta_proton_gen1": _fmt(beta_p),
        "V_hat_neutron_gen1": _fmt(V_n),
        "abs_difference": _fmt(abs(beta_p - V_n)),
        "identity_lhs_beta_of_x_times_avg": _fmt(lhs),
        "identity_rhs_trace_of_x_times_full": _fmt(rhs),
        "identity_abs_difference": _fmt(abs(lhs - rhs)),
        "h": _fmt(h),
        "half_h": _fmt(h / 2),
        "factors_checked": n_factors,
        "worst_factor_deviation_from_template": _fmt(worst_factor_dev),
    }


def reconcile_two_v_hats() -> dict:
    """The corpus carries TWO inequivalent V̂ for the same atom.  Name them.

    `tower_e0_pole_conditioning_probe` (PR #5940) reports the proton's V̂ as
    `[0.6629533727, 1.0646262154]`, 95.91 % of the pole.  This probe measures
    `[0.6713858244, 1.0551103188]`, 95.06 %.  Neither is a rounding of the
    other, and the reason is that they are different constructions, not
    different evaluations of one:

      * `mass_at_3A_proper.per_generator_V_hat_3A` — the full H_{3A} character
        sum, `V̂_i = Σ_λ ω_λ χ_λ(W_i)/d_λ`.
      * `canonical_tower.per_gen_V_hat_canonical` — "the Plancherel-averaged JM
        eigenvalue at position i+1, weighted by the per-generator crossing
        product", a different object by its own docstring.

    Recorded so the next reader does not treat the pair as a discrepancy to
    reconcile numerically.  Which (if either) is the right V̂ is the open
    question `per_generator_V_hat_3A`'s docstring already states; this only
    stops the two being confused for one.
    """
    import canonical_tower as CT

    out = {}
    for inc in (True, False):
        try:
            ct = [mpf(str(float(x)))
                  for x in CT.per_gen_V_hat_canonical(1, 0, include_inter=inc)]
        except Exception as exc:               # pragma: no cover - diagnostic
            ct = None
            out[f"canonical_tower_error_include_inter_{inc}"] = repr(exc)
        m3 = [mpf(str(float(d["full"])))
              for d in M3A.per_generator_V_hat_3A(1, 0, include_inter=inc)]
        out[f"include_inter_{inc}"] = {
            "canonical_tower.per_gen_V_hat_canonical":
                [_fmt(x) for x in ct] if ct is not None else None,
            "mass_at_3A_proper.per_generator_V_hat_3A": [_fmt(x) for x in m3],
            "max_over_q_canonical_tower":
                _fmt(max(abs(x) for x in ct) / Q) if ct else None,
            "max_over_q_mass_at_3A": _fmt(max(abs(x) for x in m3) / Q),
        }
    return out


def main() -> int:
    print(f"q                          = {_fmt(Q)}")
    print(f"convention C  z = sqrt(q)/(q+1) = {_fmt(Z_C)}")
    print(f"convention D  z = q^3/(q^2+1)   = {_fmt(Z_D)}   "
          f"({_fmt((Z_D / Z_C - 1) * 100)} % larger)")
    print()

    atoms = [(1, 0, "proton"), (0, 1, "neutron"), (1, 1, "deuteron")]
    results = []
    for (Zn, Nn, lab) in atoms:
        r = analyse(Zn, Nn, lab)
        results.append(r)
        npl = r["markov_parameters"]["normalized_plancherel"]
        pl = r["markov_parameters"]["plancherel"]
        print(f"--- {lab}  (A={r['A']}, {r['n_generators']} generators) ---")
        print(f"  Z_eff normalized_plancherel = {npl['Z_eff']}   "
              f"(W = {npl['W_sum']}, Markov trace: {npl['is_markov_trace_W_eq_1']})")
        print(f"  Z_eff plain plancherel      = {pl['Z_eff']}   "
              f"(W = {pl['W_sum']}, Markov trace: {pl['is_markov_trace_W_eq_1']})")
        print(f"  max |V_hat|                 = {r['max_abs_V_hat']}  "
              f"(pole at q = {_fmt(Q)})")
        worst = max(mpf(g["affine_vs_producer_abs"]) for g in r["generators"])
        print(f"  worst |affine - producer|   = {_fmt(worst)}")
        for g in r["generators"]:
            print(f"    gen {g['gen']:>2}  alpha={g['alpha']:>24}  "
                  f"V_hat={g['V_hat_affine']:>24}  |V|/q={g['V_hat_over_q']:>22}")
        print()

    # ---- assertions: what this probe is willing to be wrong about -----------
    checks: list[tuple[str, bool, str]] = []

    # 1. The affine form the Lean proves reproduces the producer's V̂.
    worst_affine = max(
        max(mpf(g["affine_vs_producer_abs"]) for g in r["generators"])
        for r in results)
    checks.append((
        "affine form reproduces per_generator_V_hat_3A",
        worst_affine < mpf("1e-12"),
        f"worst |alpha*Z + beta*W - V_producer| = {_fmt(worst_affine)}"))

    # 2. The integer multiplicity recovery was unambiguous everywhere.
    worst_int = max(
        float(v["worst_integer_recovery_distance"])
        for r in results for v in r["markov_parameters"].values())
    checks.append((
        "m_plus recovered unambiguously from float64 trace",
        worst_int < 1e-6,
        f"worst distance to nearest integer = {worst_int:.3e}"))

    # 3. THE FINDING. The scheme in production is not a Markov trace at the
    #    canonical parameter under EITHER convention.
    z_eff = mpf(results[0]["markov_parameters"]["normalized_plancherel"]["Z_eff"])
    checks.append((
        "production Z_eff differs from BOTH conventions by > 1 %",
        abs(z_eff / Z_C - 1) > mpf("0.01") and abs(z_eff / Z_D - 1) > mpf("0.01"),
        f"Z_eff = {_fmt(z_eff)}; vs C {_fmt((z_eff/Z_C - 1)*100)} %, "
        f"vs D {_fmt((z_eff/Z_D - 1)*100)} %"))

    # 4. W = 1 for the normalized scheme (that is what "normalized" buys) and
    #    NOT for the plain one (that is why the plain one overshoots the pole).
    npl_W1 = all(r["markov_parameters"]["normalized_plancherel"]
                 ["is_markov_trace_W_eq_1"] for r in results)
    pl_W1 = any(r["markov_parameters"]["plancherel"]
                ["is_markov_trace_W_eq_1"] for r in results)
    checks.append((
        "normalized scheme has W = 1; plain plancherel does not",
        npl_W1 and not pl_W1,
        f"normalized W=1 everywhere: {npl_W1}; plain W=1 anywhere: {pl_W1}"))

    # 5. The two V̂ constructions in the corpus are not each other.
    recon = reconcile_two_v_hats()
    inc = recon["include_inter_True"]
    ct_v = inc["canonical_tower.per_gen_V_hat_canonical"]
    m3_v = inc["mass_at_3A_proper.per_generator_V_hat_3A"]
    differ = (ct_v is not None
              and max(abs(mpf(a) - mpf(b)) for a, b in zip(ct_v, m3_v)) > mpf("1e-6"))
    checks.append((
        "the two corpus V_hat constructions differ well above rounding",
        differ,
        f"canonical_tower {ct_v} vs mass_at_3A_proper {m3_v}"))
    print("two V_hat constructions, proton, include_inter=True:")
    print(f"  canonical_tower.per_gen_V_hat_canonical   = {ct_v}"
          f"  (max/q = {inc['max_over_q_canonical_tower']})")
    print(f"  mass_at_3A_proper.per_generator_V_hat_3A  = {m3_v}"
          f"  (max/q = {inc['max_over_q_mass_at_3A']})")
    print()

    # 6. The Lean's hypotheses hold on the production weight table, and its
    #    conclusion Z = h/2 is what the table actually produces.
    lean_checks = [verify_lean_hypotheses(A) for A in (1, 2, 3)]
    print("markov_param_eq_half_h instantiated on the production weights:")
    for lc in lean_checks:
        print(f"  n={lc['n']:>2}  Z_eff={lc['Z_eff']}  h/2={lc['half_h']}  "
              f"|Z - h/2|={lc['abs_Z_minus_half_h']}")
        print(f"        weight transpose asymmetry {lc['worst_weight_transpose_asymmetry']}, "
              f"trace-pair deviation from h {lc['worst_trace_pair_deviation_from_h']}, "
              f"eigenvalue exchange {lc['eigenvalue_exchange_holds']}")
    print()
    checks.append((
        "weights are transpose-symmetric (markov_param_eq_half_h hypothesis hw)",
        all(mpf(lc["worst_weight_transpose_asymmetry"]) < mpf("1e-45")
            for lc in lean_checks),
        "worst |w(lambda') - w(lambda)| = "
        + max(lc["worst_weight_transpose_asymmetry"] for lc in lean_checks)))
    checks.append((
        "transposing exchanges the Hecke eigenvalue multiplicities",
        all(lc["eigenvalue_exchange_holds"] for lc in lean_checks),
        "m_plus(lambda') == dim - m_plus(lambda) for every shape at n = 3, 6, 9"))
    checks.append((
        "t(lambda) + t(lambda') = h (hypothesis ht)",
        all(mpf(lc["worst_trace_pair_deviation_from_h"]) < mpf("1e-45")
            for lc in lean_checks),
        "worst deviation = "
        + max(lc["worst_trace_pair_deviation_from_h"] for lc in lean_checks)))
    checks.append((
        "CONCLUSION: Z_eff = h/2 exactly, and independently of n",
        all(mpf(lc["abs_Z_minus_half_h"]) < mpf("1e-45") for lc in lean_checks),
        "worst |Z - h/2| over n = 3, 6, 9 = "
        + max(lc["abs_Z_minus_half_h"] for lc in lean_checks)))

    # 7. The p/n identity-coefficient relation, and the identity behind it.
    pn = pn_identity_coefficient_relation()
    print("proton identity coefficient vs neutron V_hat, generator 1:")
    print(f"  beta(proton)   = {pn['beta_proton_gen1']}")
    print(f"  V_hat(neutron) = {pn['V_hat_neutron_gen1']}")
    print(f"  |difference|   = {pn['abs_difference']}")
    print(f"  identity_coeff_avg_eq_trace_full on the shared prefix: "
          f"|lhs - rhs| = {pn['identity_abs_difference']}")
    print(f"  every one of {pn['factors_checked']} word factors is (1, d) with d in "
          f"the 4-value template {{0, -h/2, -h, -h(1/2 - delta/4)}}: worst "
          f"deviation {pn['worst_factor_deviation_from_template']}")
    print(f"  flavour split solved from the word: delta = "
          f"{pn['flavor_split_delta_solved_from_word']}")
    print(f"  inter-nucleon V_hat: predicted h*delta/4 = "
          f"{pn['inter_nucleon_vHat_predicted_h_delta_over_4']}, measured "
          f"{pn['inter_nucleon_vHat_measured']}, "
          f"differ {pn['inter_nucleon_vHat_abs_difference']}")
    print()
    checks.append((
        "proton's identity coefficient EQUALS the neutron's V_hat (gen 1)",
        mpf(pn["abs_difference"]) < mpf("1e-45"),
        f"|beta_p - V_n| = {pn['abs_difference']}"))
    checks.append((
        "and it is identity_coeff_avg_eq_trace_full, not a coincidence",
        mpf(pn["identity_abs_difference"]) < mpf("1e-45"),
        f"beta(x*(sigma - h/2)) vs trace(x*(sigma - h)) differ by "
        f"{pn['identity_abs_difference']}"))
    checks.append((
        "every braid-word factor is (1, d) with d in the 4-value template",
        mpf(pn["worst_factor_deviation_from_template"]) < mpf("1e-45"),
        f"{pn['factors_checked']} factors checked across p, n, d; worst "
        f"deviation {pn['worst_factor_deviation_from_template']}"))
    checks.append((
        "the fourth template value IS the colour weighting "
        "(delta solved from the word == flavor_split_leading(q))",
        mpf(pn["flavor_split_abs_difference"]) < mpf("1e-45"),
        f"solved {pn['flavor_split_delta_solved_from_word']} vs closed form "
        f"{pn['flavor_split_leading_closed_form']}, differ "
        f"{pn['flavor_split_abs_difference']} — this is the non-circular one; "
        f"h*delta/4 == V_hat is an identity and proves nothing on its own. "
        f"With the identification made, inter_nucleon_vHat says the p-n "
        f"interface reaches the tower ONLY through the colour weighting and "
        f"contributes exactly 0 under the colour-blind convention"))

    print("checks:")
    ok = True
    for name, passed, detail in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}")
        ok = ok and passed

    payload = {
        "description": (
            "The tower's V_hat is affine in an effective Markov parameter Z; "
            "measuring Z says whether the Phi_q-pole problem in "
            "per_generator_V_hat_3A is the convention C->D change (qou-dchz) "
            "or the weight scheme."),
        "scope": (
            "Scope-(a): measures the constructions AS BUILT. Says nothing "
            "about what the right V_hat is; per_generator_V_hat_3A's own "
            "verdict that both weight schemes are wrong for the tower "
            "stands unaltered."),
        "lean": [
            "qou:QOU.BraidsAndKnots.prod_eq_linear",
            "qou:QOU.BraidsAndKnots.vHat_sub_vHat",
            "qou:QOU.BraidsAndKnots.vHat_margin",
            "qou:QOU.BraidsAndKnots.vHat_eq_iff",
            "qou:QOU.BraidsAndKnots.markov_param_eq_half_h",
            "qou:QOU.BraidsAndKnots.markov_param_indep_of_weights",
            "qou:QOU.BraidsAndKnots.trace_pair_sum_eq_h",
            "qou:QOU.BraidsAndKnots.identity_coeff_avg_eq_trace_full",
        ],
        "q": _fmt(Q),
        "conventions": {
            "C_sqrt_q_over_q_plus_1": _fmt(Z_C),
            "D_q3_over_q2_plus_1": _fmt(Z_D),
            "D_over_C_percent_larger": _fmt((Z_D / Z_C - 1) * 100),
        },
        "atoms": results,
        "two_v_hat_constructions": recon,
        "pn_identity_coefficient_relation": pn,
        "lean_hypotheses_on_production_weights": lean_checks,
        "checks": [{"name": n, "passed": bool(p), "detail": d}
                   for (n, p, d) in checks],
        "all_checks_passed": bool(ok),
    }
    payload.setdefault("scriptFile", os.path.basename(__file__))
    WitnessBuilder.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=None)

    out = _HERE.parent / "tower-vhat-markov-parameter.witness.json"
    import json
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
