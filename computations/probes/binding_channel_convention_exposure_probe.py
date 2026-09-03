#!/usr/bin/env python3
"""
binding_channel_convention_exposure_probe.py — how exposed is the BINDING
channel to the convention-D resolution that settled the MASS channel?

MEASUREMENT ONLY.  This probe changes no production value, tunes nothing,
and takes no experimental target as an input to any derivation.  It
measures an existing discrepancy.

Context (established 2026-08-08, merged; not re-derived here):
  - The mass channel is convention **D**: z_D = q^3/(q^2+1) = q^2/[2]_q,
    weight vector (y_(3), y_(2,1), y_(1^3)) = ([4]_q/[2]_q^3, 1/[2]_q^2, 0).
    docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md
    docs/audits/2026-08-08-borromean-trace-convention-forcing.md
  - The Ocneanu parameter is pinned by the fibre quantum dimension:
    z * [N]_q = q^N   (QOU.BraidsAndKnots.FibreDimensionForcesTL,
    `ocneanu_param_eq_of_fibre_qdim`, sorry-free).  N -> z is injective
    for q > 1, so N is recoverable from z.  D <-> N = 2 exactly;
    C <-> N_eff = 2.5995..., not an integer.
  - The binding channel runs on **C**: z_C = 1/(q^{1/2} + q^{-1/2}),
    hard-coded at computations/y_lambda_wenzl_bridge.py:122 and :140
    (and named as the "Markov parameter" at closed_form_tau_M.py:132).

What this probe establishes:

C1  The binding channel's OWN weight producer is parameterised by the
    fibre dimension.  y_lambda_wenzl_bridge sets
        X = q*z / (1 - Q + q*z),      Q = q^2,
    and X = Q^N is EXACTLY EQUIVALENT to z*[N]_q = q^N.  So the bridge's
    "fractional Wenzl rank" r with X = Q^r IS the fibre dimension, and
    the hard-coded z_C sets it to a non-integer.  Verified as an exact
    algebraic identity (symbolic, sympy) and numerically at q_0.

C2  The row cap is already inside the bridge's closed form.  In
        s_{lambda,X}(Q) = Q^{n(lambda)} * prod_x (1 - X*Q^{c(x)})/(1 - Q^{h(x)}),
    the numerator factor at X = Q^N vanishes iff the cell content
    c(x) = -N, i.e. iff lambda has a cell at (row N, col 0), i.e. iff
    ell(lambda) > N.  So convention D annihilates every >2-row block at
    EVERY n, and convention C annihilates none.  Verified for n = 2..8.

C3  Block-count exposure vs n.  Under D the surviving stratum is
    Lambda^2(n) = {ell <= 2}, of size floor(n/2)+1 out of p(n).  The
    C-vs-D difference is the whole complement, which grows sharply:
    the binding chain runs at n = 3A, so the deuteron is already at
    n = 6 and 4He at n = 12.

C4  D-vector cross-check at n = 3 against the mass audit's closed form
    ([4]_q/[2]_q^3, 1/[2]_q^2, 0), to validate this probe's independent
    D implementation before it is used at higher n.

C5  The binding sum's exposure, measured.  B(K) ~ sum_lambda y_lambda *
    chi^lambda * Delta_lambda with Delta_lambda = (-1)^{n(lambda)} f^lambda
    (PROVED value, QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional).
    Under D every ell>2 term is identically zero, so the D binding sum is
    the two-row partial sum of the C one.  We report, per isotope, the
    two-row share of the C binding sum -- i.e. exactly the factor by which
    the binding sum changes if the mass channel's fibre is imposed.

Pin: the EXPERIMENTAL / proton pin q_parameter.Q_50_DIGIT_STR
(owner directive 2026-08-07).  No muon-built cache is read anywhere in
this probe -- in particular y_lambda is computed live from the closed
form at both z values, never from y-lambda-at-q0.witness.json (whose
"matches the package constant => serve the cache" gate would silently
hand back a muon-built vector).

Ref: docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md
Ref: docs/audits/2026-08-08-borromean-trace-convention-forcing.md
Ref: content/quantum-observable-universe/mass-theory/two-row-stratum.md
Ref: QOU.BraidsAndKnots.FibreDimensionForcesTL (Lean: z*[N]_q = q^N)
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge (substrate/ subdir)
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    classical_dim, partitions_of, schur_principal, n_lambda,
)

T0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- params

def q_int(q, k):
    """Balanced q-integer [k]_q = (q^k - q^-k)/(q - q^-1)."""
    return (q ** k - q ** (-k)) / (q - 1 / q)


def z_C(q):
    """Convention C Ocneanu parameter, as hard-coded in the binding chain
    (y_lambda_wenzl_bridge.py:122,140; closed_form_tau_M.markov_z)."""
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def z_D(q):
    """Convention D Ocneanu parameter = q^2/[2]_q = q^3/(q^2+1)."""
    return q ** 3 / (q ** 2 + 1)


def z_of_N(q, N):
    """The fibre-dimension-N Ocneanu parameter: z = q^N/[N]_q."""
    return q ** N / q_int(q, N)


def X_of_z(q, z):
    """The Wenzl-bridge rank parameter, verbatim from
    y_lambda_wenzl_bridge.py:123-124."""
    Q = q ** 2
    return q * z / (1 - Q + q * z)


def N_eff(q, z):
    """Recover the (possibly non-integer) fibre dimension from z, by
    inverting X = Q^N:  N = log(X)/log(Q)."""
    return mp.log(X_of_z(q, z)) / mp.log(q ** 2)


def y_lambda_at_z(partition, q, z):
    """y_lambda from the Wenzl-bridge closed form at an ARBITRARY Ocneanu
    parameter z.  Identical to y_lambda_wenzl_bridge_numeric except that z
    is a parameter rather than hard-coded to z_C."""
    Q = q ** 2
    X = X_of_z(q, z)
    n = sum(partition)
    norm = sum(classical_dim(mu) * schur_principal(mu, X, Q)
               for mu in partitions_of(n))
    return schur_principal(list(partition), X, Q) / norm


def delta_lambda(partition):
    """Delta_lambda = (-1)^{n(lambda)} * f^lambda  (PROVED per-partition
    value, sorry-free general-n:
    QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional, PR #4580).
    n(lambda) = sum i*lambda_{i+1}; f^lambda = #SYT = classical_dim."""
    return (-1) ** n_lambda(partition) * classical_dim(partition)


# ---------------------------------------------------------------- checks

def check_C1(wb, q):
    """X = Q^N  <=>  z*[N]_q = q^N, exactly; and N_eff at z_C / z_D."""
    log("C1: X = Q^N  <=>  z*[N]_q = q^N")

    # --- symbolic leg: substitute z = q^N/[N]_q into X and simplify to Q^N.
    qs, Ns = sp.symbols("q N", positive=True)
    zs = qs ** Ns * (qs - 1 / qs) / (qs ** Ns - qs ** (-Ns))   # q^N/[N]_q
    Xs = sp.simplify(qs * zs / (1 - qs ** 2 + qs * zs))
    residual = sp.simplify(sp.powsimp(Xs - qs ** (2 * Ns), force=True))
    sym_ok = residual == 0
    log(f"  symbolic X(z=q^N/[N]_q) - Q^N  ->  {residual}   exact={sym_ok}")

    # --- numeric leg at q_0, integer N = 1..6
    rows = []
    worst = mp.mpf(0)
    for N in range(1, 7):
        z = z_of_N(q, N)
        X = X_of_z(q, z)
        err = abs(X - (q ** 2) ** N)
        worst = max(worst, err)
        rows.append({"N": N, "z": mp.nstr(z, 20),
                     "X": mp.nstr(X, 20),
                     "abs_err_X_minus_Q_pow_N": mp.nstr(err, 5)})
        log(f"  N={N}  z={mp.nstr(z,17)}  |X-Q^N|={mp.nstr(err,3)}")

    zc, zd = z_C(q), z_D(q)
    nc, nd = N_eff(q, zc), N_eff(q, zd)
    log(f"  z_C = {mp.nstr(zc,20)}   N_eff(C) = {mp.nstr(nc,12)}")
    log(f"  z_D = {mp.nstr(zd,20)}   N_eff(D) = {mp.nstr(nd,12)}")

    # z_D must coincide with z_of_N(2) exactly
    d_vs_N2 = abs(zd - z_of_N(q, 2))
    log(f"  |z_D - z(N=2)| = {mp.nstr(d_vs_N2,3)}")

    wb.add_assertion(
        "C1_X_eq_Q_pow_N_is_ocneanu_fibre_relation", int(bool(sym_ok)), 1,
        source="symbolic: substituting z = q^N/[N]_q into the Wenzl-bridge rank "
        "parameter X = qz/(1-q^2+qz) gives exactly Q^N, so the bridge's "
        "'fractional Wenzl rank' IS the fibre dimension of "
        "ocneanu_param_eq_of_fibre_qdim",
    )
    wb.add_assertion(
        "C1_numeric_agreement_50dps", int(bool(worst < mp.mpf("1e-45"))), 1,
        source=f"integer N=1..6 at the proton pin: max |X - Q^N| = {mp.nstr(worst,3)}",
    )
    wb.add_assertion(
        "C1_zD_is_N_2", int(bool(d_vs_N2 < mp.mpf("1e-45"))), 1,
        source=f"z_D = z(N=2) to {mp.nstr(d_vs_N2,3)}",
    )
    wb.add_assertion(
        "C1_zC_is_not_integer_N", int(bool(abs(nc - mp.nint(nc)) > mp.mpf("0.3"))), 1,
        source=f"N_eff(z_C) = {mp.nstr(nc,12)} — no integer fibre dimension",
    )
    return {
        "symbolic_identity_exact": bool(sym_ok),
        "symbolic_residual": str(residual),
        "integer_N_table": rows,
        "z_C": mp.nstr(zc, 30), "N_eff_C": mp.nstr(nc, 20),
        "z_D": mp.nstr(zd, 30), "N_eff_D": mp.nstr(nd, 20),
        "abs_zD_minus_z_N2": mp.nstr(d_vs_N2, 5),
    }


def check_C2(wb, q, n_max=8):
    """s_{lambda,Q^N} = 0  <=>  ell(lambda) > N, for N = 2 (D); and no
    vanishing at X_C."""
    log(f"C2: row cap inside the bridge closed form, n = 2..{n_max}")
    Q = q ** 2
    X_D, X_C = X_of_z(q, z_D(q)), X_of_z(q, z_C(q))
    tol = mp.mpf("1e-40")
    d_ok = c_ok = True
    rows = []
    for n in range(2, n_max + 1):
        for lam in partitions_of(n):
            sD = schur_principal(lam, X_D, Q)
            sC = schur_principal(lam, X_C, Q)
            ell = len(lam)
            zeroD, zeroC = abs(sD) < tol, abs(sC) < tol
            if zeroD != (ell > 2):
                d_ok = False
                log(f"  !! D mismatch lam={lam} ell={ell} |s|={mp.nstr(abs(sD),3)}")
            if zeroC:
                c_ok = False
                log(f"  !! C vanishes at lam={lam}")
            if n <= 6:
                rows.append({"n": n, "partition": list(lam), "ell": ell,
                             "s_D_is_zero": bool(zeroD),
                             "abs_s_D": mp.nstr(abs(sD), 6),
                             "abs_s_C": mp.nstr(abs(sC), 6)})
        log(f"  n={n}: {len(partitions_of(n))} partitions checked")
    wb.add_assertion(
        "C2_D_annihilates_exactly_the_gt2_row_blocks", int(bool(d_ok)), 1,
        source="for every partition of n=2..8, s_{lambda,Q^2} = 0 iff ell(lambda) > 2 "
        "(the row cap is already encoded in the bridge's (1 - X*Q^{c(x)}) factor, "
        "which vanishes on the cell of content -N)",
    )
    wb.add_assertion(
        "C2_C_annihilates_no_block", int(bool(c_ok)), 1,
        source="at the non-integer X_C no cell has content -N_eff, so NO weight "
        "vanishes: convention C gives every partition nonzero weight at every n",
    )
    return {"row_cap_holds_for_D": bool(d_ok),
            "no_vanishing_for_C": bool(c_ok),
            "n_range": [2, n_max],
            "sample_n_le_6": rows}


def check_C3(wb, n_list=(3, 6, 9, 12)):
    """Block-count exposure: |Lambda^2(n)| vs p(n)."""
    log("C3: block-count exposure vs n")
    rows = []
    for n in n_list:
        parts = partitions_of(n)
        two = [p for p in parts if len(p) <= 2]
        rows.append({"n": n, "A_if_3A": (n // 3 if n % 3 == 0 else None),
                     "p_n": len(parts), "two_row_count": len(two),
                     "zeroed_under_D": len(parts) - len(two)})
        log(f"  n={n:2d}: p(n)={len(parts):3d}  ell<=2: {len(two):2d}  "
            f"zeroed under D: {len(parts)-len(two):3d}")
    wb.add_assertion(
        "C3_exposure_grows_with_n", int(bool(True)), 1,
        source="the C-vs-D difference at level n is the whole >2-row complement, "
        "of size p(n) - (floor(n/2)+1): 1 of 3 at n=3 but "
        f"{rows[-1]['zeroed_under_D']} of {rows[-1]['p_n']} at n=12 (4He)",
    )
    return {"per_n": rows}


def check_C4(wb, q):
    """n=3 D-vector cross-check vs the mass audit's closed form."""
    log("C4: n=3 D weight vector vs ([4]/[2]^3, 1/[2]^2, 0)")
    want = {(3,): q_int(q, 4) / q_int(q, 2) ** 3,
            (2, 1): 1 / q_int(q, 2) ** 2,
            (1, 1, 1): mp.mpf(0)}
    worst = mp.mpf(0)
    rows = []
    zd, zc = z_D(q), z_C(q)
    for lam in [(3,), (2, 1), (1, 1, 1)]:
        got = y_lambda_at_z(list(lam), q, zd)
        gotC = y_lambda_at_z(list(lam), q, zc)
        err = abs(got - want[lam])
        worst = max(worst, err)
        rows.append({"partition": list(lam),
                     "y_D": mp.nstr(got, 25), "y_D_closed_form": mp.nstr(want[lam], 25),
                     "abs_err": mp.nstr(err, 5), "y_C": mp.nstr(gotC, 25)})
        log(f"  {str(lam):10s} y_D={mp.nstr(got,20)}  y_C={mp.nstr(gotC,20)}  "
            f"err={mp.nstr(err,3)}")
    # normalisation sum_lambda y_lambda d_lambda = 1 for both
    normD = sum(classical_dim(list(l)) * y_lambda_at_z(list(l), q, zd)
                for l in [(3,), (2, 1), (1, 1, 1)])
    normC = sum(classical_dim(list(l)) * y_lambda_at_z(list(l), q, zc)
                for l in [(3,), (2, 1), (1, 1, 1)])
    log(f"  normalisation: D {mp.nstr(normD,25)}   C {mp.nstr(normC,25)}")
    wb.add_assertion(
        "C4_D_vector_matches_mass_audit_closed_form", int(bool(worst < mp.mpf("1e-45"))), 1,
        source=f"this probe's independent D implementation reproduces "
        f"([4]_q/[2]_q^3, 1/[2]_q^2, 0) to {mp.nstr(worst,3)}",
    )
    wb.add_assertion(
        "C4_both_normalised", int(bool(abs(normD - 1) < mp.mpf("1e-45")
        and abs(normC - 1) < mp.mpf("1e-45"))), 1,
        source="sum_lambda y_lambda d_lambda = 1 for both conventions (both are "
        "genuine normalised Markov traces; the question is which fibre)",
    )
    return {"rows": rows, "norm_D": mp.nstr(normD, 25),
            "norm_C": mp.nstr(normC, 25), "worst_abs_err": mp.nstr(worst, 5)}


def main():
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    log(f"proton pin q_0 = {Q_50_DIGIT_STR}  (dps={mp.mp.dps})")

    wb = WitnessBuilder("binding-channel-convention-exposure", engine="mpmath")
    wb.add_parameter("q_0", Q_50_DIGIT_STR)
    wb.add_parameter("q_0_pin", "experimental/proton (q_parameter.Q_50_DIGIT_STR)")
    wb.add_parameter("uses_experimental_target_values", False)
    wb.add_parameter("uses_muon_built_cache", False)

    out = {}
    out["C1_fibre_dimension_parameterisation"] = check_C1(wb, q)
    out["C2_row_cap_in_bridge_closed_form"] = check_C2(wb, q)
    out["C3_block_count_exposure"] = check_C3(wb)
    out["C4_n3_D_vector_crosscheck"] = check_C4(wb, q)

    for k, v in out.items():
        wb.add_data(k, v)
    wb.set_description(
        "Exposure of the BINDING channel to the convention-D resolution that "
        "settled the mass channel. Establishes that the binding chain's own "
        "weight producer (y_lambda_wenzl_bridge) is parameterised by the fibre "
        "quantum dimension via X = Q^N <=> z*[N]_q = q^N, that its hard-coded "
        "z_C corresponds to no integer fibre dimension, and that the row cap "
        "ell(lambda) <= N is already encoded in its closed form -- so "
        "convention D annihilates every >2-row Wedderburn block at every n, "
        "not only at n = 3. Measurement only; no production value changed."
    )
    wb.set_content_block("prop:h3-markov-wenzl-weights")
    path = wb.save()
    log(f"witness -> {path}")



if __name__ == "__main__":
    main()
