#!/usr/bin/env python3
"""Is the transverse NA-Stokes pairing `Omega_2` GAUGE-COVARIANT?  It is not.

Bean `qou-prjo`.  Successor to PR #4848 (single-generator scope-(b)), #4849
(multi-generator super-pairwise + the `sec 2.3` red-team note), #4850
(orbit-symmetry), #4818, #4798, #4619.

THE QUESTION
------------
PR #4849 sec 2.3 recorded that the germ `dq = q (d_q rho) rho^-1` transforms
INHOMOGENEOUSLY under a `q`-dependent change of representation basis `B(q)`,

    dq  |->  B dq B^-1 + (1 - Ad(rho))( q (d_q B) B^-1 ),

i.e. like a CONNECTION, not like a tensor, and left open whether the pairing
`Omega_2 = sum_ij J_ij [Fc_i, Fc_j]`, `Fc_k = U_k^-1 F_q U_k`, is nevertheless
covariant.  That question is PRIOR to "which germ observer pair", and it
dissolves it:

  * covariant     => ||Omega_2|| is gauge-invariant and #4849's 16.4x spread is
                     an observable-CHOICE problem;
  * not covariant => `Omega_2` has NO basis-independent value at all, and the
                     transverse route is dead for a more fundamental reason.

WHAT THIS PROBE MEASURES
------------------------
FORMALIZE-FIRST.  The algebra was proved in Lean BEFORE this ran:
`QOU/MassTheory/GermConnectionGaugeCovariance.lean` (sorry-free, generic
`Ring R`, `#print axioms` clean on all 48 declarations) proves

  * `germ_mul`                   -- the germ is a 1-COCYCLE for `Ad rho`;
  * `germ_conj`                  -- THE CONNECTION LAW (above);
  * `germCurvature_covariant_iff`-- covariance holds IFF the defect vanishes;
  * `gaugeDefect_ne_zero`        -- a concrete derivation/ring/units triple
                                    where the defect is NOT zero;
  * `listPairing_map_adAct`      -- the pairing is covariant GIVEN covariant
                                    inputs, so ALL the failure sits in `F_q`;
  * `cupSq_eq_neg_coboundary`    -- the covariant second-order object (the cup
                                    square) is EXACTLY a coboundary, explicit
                                    primitive `beta = D . alpha`;
  * `trace_germ_conj`            -- `tau(alpha(u))` IS gauge-invariant.

This probe checks all of that against the ACTUAL Hecke germ, exactly over
`Q(q)` where possible, and then measures the covariance defect of the real
`Omega_2` on the real `4He` atom word in TWO genuinely different gauges.

  A.  SYMBOLIC (sympy, exact in `Q(q)`), 2-dim Hecke rep of `H_3` -- #4848's rep
      A1  braid + Hecke certification
      A2  the connection law, verified by computing both sides independently
      A3  the defect `Delta != 0`, exhibited exactly
      A4  RETRO-CHECK ON #4848: in the gauge `B = diag(1,q)` the curvature is no
          longer an `Ad(rho(sigma_1))`-eigenvector, and `Omega_2` on `sigma_1^3`
          is NONZERO -- so #4848's vanishing holds only within a `q`-INDEPENDENT
          change of basis, not under the full connection freedom.
      A5  the cup-square coboundary identity, exactly, on braid words
      A6  `tr alpha(w)` is gauge-invariant and equals `q d_q log det rho(w)`
          -- pure writhe, i.e. the already-walled framing datum

  B.  NUMERIC, the corpus `4He` atom word (`atom_braid_word_3A(2,2)`, 12 strands,
      47 letters) in `H_12(q)`, `lambda = (11,1)` (dim 11) and `(10,1,1)` (dim 55)
      B1  gauge (a): `B(q) = diag(1, q, ..., q^(d-1))` on the Hoefsmit seminormal
          basis -- `B` is known explicitly, so the covariance defect
          `|| Ad(B)^-1 Omega_2' - Omega_2 || / ||Omega_2||` is measured directly.
      B2  gauge (b): the REDUCED BURAU basis at `t = q^-2`, scaled by `q` -- the
          gauge #4798/#4848 used, a different realization of the SAME
          `lambda = (11,1)` representation (character equality certified).  The
          comparison uses only CONJUGATION-INVARIANT readouts, `tr(Omega_2^k)`,
          so it needs no intertwiner and is readout-independent: conjugate
          operators have equal trace powers, full stop.

DISCIPLINE
----------
`free_parameters = 0`.  NO AME quantity, NO `g_2`, NO binding number enters the
compute or any selection -- there is no value to select, which is the finding.
`q0` = EXPERIMENTAL PROTON ANCHOR (`qou_substrate.constants`); no muon-serving
cache is touched; layer-pure.  The `A >= 3` germ is `q`-dependent (#4849 sec 2.2),
so the pin is material and is recorded.  Nothing is wired.  Bean stays OPEN.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent            # computations/probes
_COMP = HERE.parent                               # computations
for p in (str(_COMP), str(HERE), str(_COMP / "hecke"), str(_COMP / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import numpy as np                                          # noqa: E402
import sympy as sp                                          # noqa: E402

from hecke.hecke_characters import standard_young_tableaux  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A            # noqa: E402
from witness_base import WitnessBuilder                     # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR          # noqa: E402

Q0 = float(Q_50_DIGIT_STR)          # EXPERIMENTAL PROTON ANCHOR (owner directive 2026-08-07)

results: dict = {}
assertions: dict = {}


def _log(msg=""):
    print(msg, flush=True)


# ===========================================================================
# A.  SYMBOLIC -- exact over Q(q), 2-dimensional Hecke rep of H_3 (#4848's rep)
# ===========================================================================

q = sp.symbols("q", positive=True)


def _sym_hecke_H3():
    """#4848's 2-dim rep: rho(s1), rho(s2) with eigenvalues q, -1/q."""
    s1 = sp.Matrix([[q, -1 / q], [0, -1 / q]])
    s2 = sp.Matrix([[-1 / q, 0], [-q, q]])
    return s1, s2


def _germ_sym(M):
    """alpha(M) = q (d_q M) M^-1, exact."""
    return sp.simplify(q * M.diff(q) * M.inv())


def _ad(g, X):
    return sp.simplify(g * X * g.inv())


def _br(X, Y):
    return sp.expand(X * Y - Y * X)


def part_A():
    _log("=" * 74)
    _log("A.  SYMBOLIC (sympy, exact over Q(q)) -- 2-dim Hecke rep of H_3")
    _log("=" * 74)
    s1, s2 = _sym_hecke_H3()
    I2 = sp.eye(2)
    h = q - 1 / q

    # --- A1 certification --------------------------------------------------
    braid = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2)
    hk1 = sp.simplify(s1 * s1 - h * s1 - I2)
    hk2 = sp.simplify(s2 * s2 - h * s2 - I2)
    ok_cert = braid.is_zero_matrix and hk1.is_zero_matrix and hk2.is_zero_matrix
    _log(f"  A1  braid sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2 : {braid.is_zero_matrix}")
    _log(f"      Hecke (sigma - q)(sigma + 1/q) = 0 both gens        : "
         f"{hk1.is_zero_matrix and hk2.is_zero_matrix}")
    assertions["A1_rep_certified"] = 1 if ok_cert else 0

    a1, a2 = _germ_sym(s1), _germ_sym(s2)
    _log(f"      germ dq1 = {sp.simplify(a1).tolist()}   (#4848: H - 2E)")
    _log(f"      germ dq2 = {sp.simplify(a2).tolist()}   (#4848: -H)")
    F0 = _br(a1, a2)
    _log(f"      F_q = [dq1, dq2] = {sp.simplify(F0).tolist()}   (#4848: -4E)")
    assertions["A1_reproduces_4848_germ_curvature"] = (
        1 if sp.simplify(F0 - sp.Matrix([[0, -4], [0, 0]])).is_zero_matrix else 0)

    # --- A2 the connection law --------------------------------------------
    _log()
    _log("  A2  THE CONNECTION LAW.  Gauge B(q) = diag(1, q)  (a legitimate, "
         "q-DEPENDENT")
    _log("      change of basis: conjugation preserves braid + Hecke, so B rho B^-1 is")
    _log("      the SAME abstract representation in a different frame).")
    B = sp.diag(1, q)
    Theta = sp.simplify(q * B.inv() * B.diff(q))          # Theta = q B^-1 d_q B
    _log(f"      Theta = q B^-1 d_q B = {Theta.tolist()}")
    law_ok = True
    lhs_store, rhs_store = {}, {}
    for name, s in (("sigma1", s1), ("sigma2", s2)):
        direct = _germ_sym(sp.simplify(B * s * B.inv()))    # germ of the gauged rep
        X = sp.simplify(Theta - _ad(s, Theta))             # (1 - Ad rho) Theta
        law = sp.simplify(B * (_germ_sym(s) + X) * B.inv())
        same = sp.simplify(direct - law).is_zero_matrix
        law_ok = law_ok and same
        lhs_store[name] = sp.simplify(direct)
        rhs_store[name] = sp.simplify(X)
        _log(f"      {name}: germ(B rho B^-1) == B (germ(rho) + (1-Ad rho)Theta) B^-1 "
             f": {same}")
        _log(f"              inhomogeneous shift X = {sp.simplify(X).tolist()}")
    assertions["A2_connection_law_verified"] = 1 if law_ok else 0
    results["A2_gauge_B"] = "diag(1, q)"
    results["A2_Theta"] = str(Theta.tolist())
    results["A2_shift_sigma1"] = str(rhs_store["sigma1"].tolist())
    results["A2_shift_sigma2"] = str(rhs_store["sigma2"].tolist())

    # --- A3 the defect -----------------------------------------------------
    _log()
    _log("  A3  THE COVARIANCE DEFECT of F_q = [dq1, dq2].")
    X1 = rhs_store["sigma1"]
    X2 = rhs_store["sigma2"]
    Delta = sp.simplify(_br(a1, X2) + _br(X1, a2) + _br(X1, X2))
    Fg = sp.simplify(_germ_sym(sp.simplify(B * s1 * B.inv())) *
                     _germ_sym(sp.simplify(B * s2 * B.inv())) -
                     _germ_sym(sp.simplify(B * s2 * B.inv())) *
                     _germ_sym(sp.simplify(B * s1 * B.inv())))
    consistent = sp.simplify(Fg - B * (F0 + Delta) * B.inv()).is_zero_matrix
    nonzero = not sp.simplify(Delta).is_zero_matrix
    _log(f"      Delta = [a1,X2] + [X1,a2] + [X1,X2] = {sp.simplify(Delta).tolist()}")
    _log(f"      F' = B (F + Delta) B^-1                    : {consistent}")
    _log(f"      Delta != 0  (=> F_q is NOT a tensor)       : {nonzero}")
    assertions["A3_defect_formula_consistent"] = 1 if consistent else 0
    assertions["A3_defect_nonzero"] = 1 if nonzero else 0
    results["A3_defect_exact"] = str(sp.simplify(Delta).tolist())

    # --- A4 retro-check on #4848 ------------------------------------------
    _log()
    _log("  A4  RETRO-CHECK ON #4848 (sigma_1^3, the pn channel word).")
    _log("      #4848: F_q = -4E is an Ad(rho(s1))-eigenvector, so every transported")
    _log("      curvature lies on one line and Omega_2 = 0 for EVERY J and every handle")
    _log("      exponent.  That quantification does NOT include a q-DEPENDENT change of")
    _log("      basis.  In the gauge B = diag(1,q):")
    Fg_s = sp.simplify(Fg)
    # eigenvector test: Ad(rho'(s1)) F' proportional to F' ?
    s1g = sp.simplify(B * s1 * B.inv())
    AdF = _ad(s1g, Fg_s)
    # proportionality: AdF = c F' for a scalar c  <=>  all 2x2 minors vanish
    ratios = []
    for i in range(2):
        for j in range(2):
            ratios.append(sp.simplify(AdF[i, j] * Fg_s[1 - i, 1 - j]
                                      - AdF[1 - i, 1 - j] * Fg_s[i, j]))
    is_eig_base = all(sp.simplify(_ad(s1, F0)[i, j] * F0[1 - i, 1 - j]
                                  - _ad(s1, F0)[1 - i, 1 - j] * F0[i, j]) == 0
                      for i in range(2) for j in range(2))
    is_eig_gauged = all(r == 0 for r in ratios)
    _log(f"      base gauge  : F_q IS an Ad(sigma1)-eigenvector : {is_eig_base}")
    _log(f"      gauge diag(1,q): still an eigenvector?          : {is_eig_gauged}")
    # Omega_2 on sigma_1^3 in each gauge, ordered pairing over the 3 bands
    def omega_sigma1_cubed(sig1, F):
        U = [sp.eye(2), sig1, sp.simplify(sig1 * sig1)]
        Fc = [sp.simplify(u.inv() * F * u) for u in U]
        Om = sp.zeros(2, 2)
        for i in range(3):
            for j in range(i + 1, 3):
                Om += _br(Fc[j], Fc[i])
        return sp.simplify(Om)
    Om_base = omega_sigma1_cubed(s1, F0)
    Om_gauged = sp.simplify(omega_sigma1_cubed(s1g, Fg_s))
    _log(f"      Omega_2 (base gauge, sigma_1^3)   = {Om_base.tolist()}   [#4848: 0]")
    _log(f"      Omega_2 (gauge diag(1,q))         = {Om_gauged.tolist()}")
    assertions["A4_4848_zero_reproduced_in_base_gauge"] = (
        1 if Om_base.is_zero_matrix else 0)
    assertions["A4_4848_zero_is_gauge_dependent"] = (
        1 if not Om_gauged.is_zero_matrix else 0)
    results["A4_omega2_sigma1cubed_gauged"] = str(Om_gauged.tolist())

    # --- A5 the cup-square coboundary identity -----------------------------
    _log()
    _log("  A5  THE COVARIANT SECOND-ORDER OBJECT.  cup square (alpha U alpha)(u,v) =")
    _log("      [alpha(u), Ad(u) alpha(v)]  vs  -(d beta)(u,v) with beta = q d_q alpha.")
    words = {"s1": [1], "s2": [2], "s1s2": [1, 2], "s2s1": [2, 1],
             "s1s1s2": [1, 1, 2]}

    def rho_word(wl):
        M = sp.eye(2)
        for g in wl:
            M = M * (s1 if g == 1 else s2)
        return sp.simplify(M)

    cup_ok = True
    worst = None
    for nu, wu in words.items():
        for nv, wv in words.items():
            Ru, Rv, Ruv = rho_word(wu), rho_word(wv), rho_word(wu + wv)
            au, av = _germ_sym(Ru), _germ_sym(Rv)
            bu = sp.simplify(q * _germ_sym(Ru).diff(q))
            bv = sp.simplify(q * _germ_sym(Rv).diff(q))
            buv = sp.simplify(q * _germ_sym(Ruv).diff(q))
            cup = sp.simplify(_br(au, _ad(Ru, av)))
            cob = sp.simplify(_ad(Ru, bv) - buv + bu)
            d = sp.simplify(cup + cob)
            if not d.is_zero_matrix:
                cup_ok = False
                worst = (nu, nv, str(d.tolist()))
    _log(f"      cup(u,v) = -(d beta)(u,v) for all 25 word pairs : {cup_ok}")
    if worst:
        _log(f"      FAILING PAIR: {worst}")
    _log("      => the cup square is EXACTLY a coboundary; the class [alpha]U[alpha]")
    _log("         in H^2 is ZERO.  The covariant order-2 object vanishes identically.")
    assertions["A5_cup_square_is_coboundary"] = 1 if cup_ok else 0

    # --- A6 the gauge-invariant scalar -------------------------------------
    _log()
    _log("  A6  WHAT IS GAUGE-INVARIANT: tr alpha(w) = q d_q log det rho(w).")
    inv_ok = True
    for nu, wl in words.items():
        Rw = rho_word(wl)
        t_base = sp.simplify(sp.trace(_germ_sym(Rw)))
        t_gauged = sp.simplify(sp.trace(_germ_sym(sp.simplify(B * Rw * B.inv()))))
        logdet = sp.simplify(q * sp.diff(sp.log(sp.det(Rw)), q))
        same = sp.simplify(t_base - t_gauged) == 0 and sp.simplify(t_base - logdet) == 0
        inv_ok = inv_ok and same
        _log(f"      w = {nu:8s}  tr alpha = {t_base}   gauge-invariant + = "
             f"q d_q log det : {same}")
    _log("      det rho(sigma_i) = q * (-1/q) = -1 here, so tr alpha == 0: the only")
    _log("      invariant linear functional of the germ sees the ABELIANISATION only")
    _log("      (writhe / framing), the datum already walled by no_writhe_only_framing.")
    assertions["A6_trace_germ_gauge_invariant"] = 1 if inv_ok else 0


# ===========================================================================
# B.  NUMERIC -- the real 4He atom word, two genuinely different gauges
# ===========================================================================


def _blocks(shape):
    n = sum(shape)
    syts, _cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    idx = {tuple(sorted(t.items())): i for i, t in enumerate(syts)}
    per_gen = []
    for k in range(1, n):
        out, done = [], set()
        for i in range(dim):
            if i in done:
                continue
            ck, ck1 = syts[i][k], syts[i][k + 1]
            r = contents[ck1] - contents[ck]
            sm = dict(syts[i])
            sm[k], sm[k + 1] = ck1, ck
            j = idx.get(tuple(sorted(sm.items())))
            if j == i:
                j = None
            out.append((i, j, r))
            done.add(i)
            if j is not None:
                done.add(j)
        per_gen.append(out)
    return per_gen, dim


def _entry_and_deriv(r, qv):
    """(a, a', b, da, da', db) for axial distance r -- CLOSED-FORM derivatives.

    Identical closed form to `nastokes_multigen_cluster_additivity_probe`
    (a = h/(1-q^-2r), a' = h/(1-q^2r), b = sqrt(a a' + 1)); reproduced rather
    than imported so this probe has no dependence on a sibling probe's state.
    """
    h = qv - 1.0 / qv
    dh = 1.0 + 1.0 / qv ** 2
    u = qv ** (-2 * r)
    du = (-2 * r) * qv ** (-2 * r - 1)
    v = qv ** (2 * r)
    dv = (2 * r) * qv ** (2 * r - 1)
    a = h / (1.0 - u)
    da = dh / (1.0 - u) + h * du / (1.0 - u) ** 2
    ap = h / (1.0 - v)
    dap = dh / (1.0 - v) + h * dv / (1.0 - v) ** 2
    bsq = a * ap + 1.0
    if bsq <= 0:
        return a, ap, 0.0, da, dap, 0.0
    b = bsq ** 0.5
    db = (ap * da + a * dap) / (2 * b) if b != 0 else 0.0
    return a, ap, b, da, dap, db


def seminormal(shape, qv):
    """rho(sigma_i) and d_q rho(sigma_i) in the Hoefsmit seminormal basis."""
    per_gen, dim = _blocks(shape)
    sig, dsig = [], []
    for blocks in per_gen:
        M, dM = np.zeros((dim, dim)), np.zeros((dim, dim))
        for (i, j, r) in blocks:
            a, ap, b, da, dap, db = _entry_and_deriv(r, qv)
            if j is None:
                M[i, i], dM[i, i] = a, da
            else:
                M[i, i], M[j, j] = a, ap
                M[i, j], M[j, i] = b, b
                dM[i, i], dM[j, j] = da, dap
                dM[i, j], dM[j, i] = db, db
        sig.append(M)
        dsig.append(dM)
    return sig, dsig, dim


def reduced_burau(n, qv):
    """rho_B(sigma_i) = q * beta_i(t = q^-2) and its exact d_q, dim n-1.

    beta_i = I except row i, which is (t, -t-1, 1) added on cols i-1, i, i+1
    (truncated at the boundary).  Eigenvalues 1 (mult n-2) and -t (mult 1), so
    scaling by q gives Hecke eigenvalues q and -1/q: the SAME representation as
    the seminormal lambda = (n-1, 1) block, in a different (q-dependent) basis.
    """
    d = n - 1
    sig, dsig = [], []
    for i in range(1, n):          # generator sigma_i, 1-based
        M = qv * np.eye(d)
        dM = np.eye(d).copy()
        r = i - 1                  # 0-based row
        M[r, r] = -1.0 / qv
        dM[r, r] = 1.0 / qv ** 2
        if r - 1 >= 0:
            M[r, r - 1] = 1.0 / qv
            dM[r, r - 1] = -1.0 / qv ** 2
        if r + 1 < d:
            M[r, r + 1] = qv
            dM[r, r + 1] = 1.0
        sig.append(M)
        dsig.append(dM)
    return sig, dsig, d


def certify(sig, h, tag):
    d = sig[0].shape[0]
    I = np.eye(d)
    worst = 0.0
    for M in sig:
        worst = max(worst, np.linalg.norm(M @ M - h * M - I))
    for i in range(len(sig) - 1):
        worst = max(worst, np.linalg.norm(sig[i] @ sig[i + 1] @ sig[i]
                                          - sig[i + 1] @ sig[i] @ sig[i + 1]))
    for i in range(len(sig)):
        for j in range(i + 2, len(sig)):
            worst = max(worst, np.linalg.norm(sig[i] @ sig[j] - sig[j] @ sig[i]))
    _log(f"      {tag:34s} braid+Hecke+far-commute worst residual = {worst:.2e}")
    return worst


def germs_from(sig, dsig, qv, h):
    """dq_i = q (d_q rho) rho^-1, using rho^-1 = rho - h (Hecke; no inversion)."""
    d = sig[0].shape[0]
    I = np.eye(d)
    return [qv * (dM @ (M - h * I)) for M, dM in zip(sig, dsig)]


def _letter_inv_coeffs(c, d, h):
    e = d / c
    A = 1.0 / (1.0 - e * h - e * e)
    return A / c, (-A * (h + e)) / c


def omega2(word, sig, h, F):
    """Omega_2 = listPairing([Fc_0, ...]) = sum_{i<j} [Fc_j, Fc_i], Yekutieli
    ordered transports U_k = rho(l_1)...rho(l_{k-1})."""
    d = sig[0].shape[0]
    I = np.eye(d)
    U, Ui = np.eye(d), np.eye(d)
    P = np.zeros((d, d))
    Om = np.zeros((d, d))
    for (c, dd, g) in word:
        Fk = Ui @ F @ U
        Om += Fk @ P - P @ Fk
        P = P + Fk
        al, be = _letter_inv_coeffs(c, dd, h)
        U = U @ (c * sig[g] + dd * I)
        Ui = (al * sig[g] + be * I) @ Ui
    return Om


def _trace_powers(M, kmax=4):
    out, P = [], np.eye(M.shape[0])
    for _ in range(kmax):
        P = P @ M
        out.append(float(np.trace(P)))
    return out


def part_B():
    _log()
    _log("=" * 74)
    _log("B.  NUMERIC -- the corpus 4He atom word, two genuinely different gauges")
    _log("=" * 74)
    qv = Q0
    h = qv - 1.0 / qv
    n = 12
    word = [(float(c), float(d), g) for (c, d, g) in atom_braid_word_3A(2, 2)]
    _log(f"      q0 (EXPERIMENTAL PROTON ANCHOR) = {qv!r}")
    _log(f"      word = atom_braid_word_3A(2,2): {len(word)} letters, "
         f"gens {min(g for _,_,g in word)}..{max(g for _,_,g in word)}")
    results["q0_experimental_proton_anchor"] = repr(qv)
    results["word_provenance"] = "computations/mass_at_3A_proper.py::atom_braid_word_3A(2,2)"
    results["word_letters"] = len(word)

    GERM_PAIRS = [(0, 1), (3, 4)]

    # ---- B1  gauge (a): diag(1, q, ..., q^(d-1)) on the seminormal basis ----
    _log()
    _log("  B1  GAUGE (a): B(q) = diag(1, q, ..., q^(d-1)) on Hoefsmit seminormal.")
    _log("      B is known explicitly, so the covariance defect is measured DIRECTLY:")
    _log("      covariance <=> Ad(B)^-1 Omega_2' == Omega_2.")
    b1_rows = []
    for shape in [(11, 1), (10, 1, 1)]:
        sig, dsig, d = seminormal(shape, qv)
        certify(sig, h, f"seminormal {shape} dim {d}")
        gm = germs_from(sig, dsig, qv, h)
        # gauge: B diagonal, B_kk = q^k;  d_q B = diag(k q^(k-1))
        bd = np.array([qv ** k for k in range(d)])
        dbd = np.array([k * qv ** (k - 1) for k in range(d)])
        B = np.diag(bd)
        Binv = np.diag(1.0 / bd)
        Theta = np.diag(qv * dbd / bd)              # Theta = q B^-1 d_q B = diag(k)
        sig_g = [B @ M @ Binv for M in sig]
        dsig_g = [B @ dM @ Binv + np.diag(dbd) @ M @ Binv
                  + B @ M @ np.diag(-dbd / bd ** 2) for M, dM in zip(sig, dsig)]
        certify(sig_g, h, f"  gauged {shape} dim {d}")
        gm_g = germs_from(sig_g, dsig_g, qv, h)
        # cross-check against the Lean connection law
        law_err = max(float(np.linalg.norm(
            gm_g[i] - B @ (gm[i] + Theta - sig[i] @ Theta @ np.linalg.inv(sig[i]))
            @ Binv)) / max(1e-30, float(np.linalg.norm(gm_g[i])))
            for i in range(len(gm)))
        _log(f"      connection-law relative error over all germs : {law_err:.2e}")
        assertions[f"B1_connection_law_numeric_{shape}"] = 1 if law_err < 1e-9 else 0
        for (i, j) in GERM_PAIRS:
            F = gm[i] @ gm[j] - gm[j] @ gm[i]
            Fg = gm_g[i] @ gm_g[j] - gm_g[j] @ gm_g[i]
            Om = omega2(word, sig, h, F)
            Om_g = omega2(word, sig_g, h, Fg)
            pull = Binv @ Om_g @ B                  # Ad(B)^-1 Omega_2'
            rel = float(np.linalg.norm(pull - Om)) / max(1e-30, float(np.linalg.norm(Om)))
            row = {
                "shape": str(shape), "germ_pair": f"({i},{j})",
                "norm_Omega_base": float(np.linalg.norm(Om)),
                "norm_Omega_gauged": float(np.linalg.norm(Om_g)),
                "covariance_defect_rel": rel,
                "tr_Om2_base": float(np.trace(Om @ Om)),
                "tr_Om2_gauged": float(np.trace(Om_g @ Om_g)),
            }
            b1_rows.append(row)
            _log(f"      {str(shape):10s} germ {i},{j}:  ||Omega||={row['norm_Omega_base']:.4e}"
                 f"  ||Omega'||={row['norm_Omega_gauged']:.4e}"
                 f"  covariance defect = {rel:.3f}")
            _log(f"                        tr(Omega^2) = {row['tr_Om2_base']:.6e}"
                 f"   ->  {row['tr_Om2_gauged']:.6e}   (invariant iff equal)")
    results["B1_rows"] = b1_rows
    worst_def = max(r["covariance_defect_rel"] for r in b1_rows)
    assertions["B1_not_covariant"] = 1 if worst_def > 1e-3 else 0
    results["B1_worst_covariance_defect_rel"] = worst_def

    # ---- B2  gauge (b): reduced Burau, the #4798/#4848 gauge ---------------
    _log()
    _log("  B2  GAUGE (b): REDUCED BURAU at t = q^-2, scaled by q -- the gauge")
    _log("      #4798/#4848 used.  Same abstract rep as seminormal lambda = (11,1);")
    _log("      certified by CHARACTER EQUALITY on random words.  Comparison uses only")
    _log("      conjugation-INVARIANT readouts tr(Omega^k), so no intertwiner is needed:")
    _log("      conjugate operators have equal trace powers, full stop.")
    sigS, dsigS, dS = seminormal((11, 1), qv)
    sigB, dsigB, dB = reduced_burau(n, qv)
    certify(sigS, h, "seminormal (11,1)")
    certify(sigB, h, "reduced Burau (q-scaled)")
    assert dS == dB == 11, (dS, dB)
    rng = np.random.default_rng(20260809)
    char_worst = 0.0
    for _ in range(40):
        L = int(rng.integers(1, 9))
        gens = rng.integers(0, n - 1, size=L)
        MS, MB = np.eye(dS), np.eye(dB)
        for g in gens:
            MS = MS @ sigS[g]
            MB = MB @ sigB[g]
        tS, tB = float(np.trace(MS)), float(np.trace(MB))
        char_worst = max(char_worst, abs(tS - tB) / max(1.0, abs(tS)))
    _log(f"      character equality on 40 random words, worst rel diff = {char_worst:.2e}")
    assertions["B2_same_representation"] = 1 if char_worst < 1e-9 else 0
    results["B2_character_worst_rel_diff"] = char_worst

    gmS = germs_from(sigS, dsigS, qv, h)
    gmB = germs_from(sigB, dsigB, qv, h)
    b2_rows = []
    for (i, j) in GERM_PAIRS:
        FS = gmS[i] @ gmS[j] - gmS[j] @ gmS[i]
        FB = gmB[i] @ gmB[j] - gmB[j] @ gmB[i]
        OmS = omega2(word, sigS, h, FS)
        OmB = omega2(word, sigB, h, FB)
        tS = _trace_powers(OmS)
        tB = _trace_powers(OmB)
        rel = [abs(a - b) / max(1e-30, abs(a)) for a, b in zip(tS, tB)]
        row = {"germ_pair": f"({i},{j})",
               "trace_powers_seminormal": tS, "trace_powers_burau": tB,
               "rel_diff": rel,
               "norm_Omega_seminormal": float(np.linalg.norm(OmS)),
               "norm_Omega_burau": float(np.linalg.norm(OmB))}
        b2_rows.append(row)
        _log(f"      germ {i},{j}:  ||Omega||  seminormal {row['norm_Omega_seminormal']:.4e}"
             f"   Burau {row['norm_Omega_burau']:.4e}")
        for k in range(4):
            _log(f"                 tr(Omega^{k+1}) = {tS[k]:+.6e}  vs  {tB[k]:+.6e}"
                 f"   rel diff {rel[k]:.3e}")
    results["B2_rows"] = b2_rows
    worst_inv = max(max(r["rel_diff"][1:]) for r in b2_rows)   # skip tr(Omega)=0
    assertions["B2_invariants_differ_across_gauges"] = 1 if worst_inv > 1e-3 else 0
    results["B2_worst_invariant_rel_diff"] = worst_inv

    # trace control: tr(Omega) = 0 by listPairing_trace_zero
    tr_ctrl = max(abs(r["trace_powers_seminormal"][0]) / r["norm_Omega_seminormal"]
                  for r in b2_rows)
    _log(f"      trace control |tr Omega| / ||Omega|| = {tr_ctrl:.2e} "
         f"(listPairing_trace_zero)")
    assertions["B2_trace_control"] = 1 if tr_ctrl < 1e-10 else 0
    results["B2_trace_control"] = tr_ctrl


def f64_json(o):
    """Serialize an f64 result tree for a witness: every float becomes its own
    repr string; ints/bools/None/strings pass through.

    Same rationale as nastokes_multigen_cluster_additivity_probe.f64_json: the
    numeric sweep here is float64 by design, so repr(float) is exactly the ~17
    digits the kernel produced. It round-trips bit-exactly and keeps raw
    float64 JSON out of the witness. Applied once at the sink so a field added
    later cannot miss it.
    """
    if isinstance(o, bool) or o is None:
        return o
    if isinstance(o, float):
        return repr(o)
    if isinstance(o, dict):
        return {k: f64_json(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [f64_json(v) for v in o]
    return o


def main() -> int:
    t0 = time.time()
    _log("NA-Stokes transverse pairing: IS Omega_2 GAUGE-COVARIANT?")
    _log("bean qou-prjo | formalize-first: Lean proved the algebra first")
    _log("(QOU/MassTheory/GermConnectionGaugeCovariance.lean, sorry-free)")
    _log()
    part_A()
    part_B()

    _log()
    _log("=" * 74)
    _log("VERDICT")
    _log("=" * 74)
    _log("  Omega_2 is NOT gauge-covariant.")
    _log("  * the germ transforms as a CONNECTION (A2, verified exactly);")
    _log("  * the curvature defect Delta is nonzero (A3, exhibited exactly);")
    _log("  * on the real 4He atom word the covariance defect")
    _log("    ||Ad(B)^-1 Omega' - Omega|| / ||Omega|| is O(1) (B1);")
    _log("  * the CONJUGATION-INVARIANT readouts tr(Omega^k) DIFFER between the")
    _log("    seminormal and reduced-Burau realizations of the SAME representation")
    _log("    (B2) -- readout-independent proof that Omega_2 is not a tensor.")
    _log("  So there is no basis-independent ||Omega_2||: #4798's 0..897 spread and")
    _log("  #4849's 16.4x germ-observer spread are not an unmade CHOICE -- there is")
    _log("  nothing to choose between.  The observer-pair selection question is void.")
    _log()
    _log("  #4848's zero is gauge-dependent too (A4): it holds within a q-INDEPENDENT")
    _log("  change of basis, not under the full connection freedom.  Its ALGEBRA is")
    _log("  correct; its 'gauge-independent' quantification did not range over")
    _log("  q-dependent regaugings.")
    _log()
    _log("  A covariant object DOES exist: the germ is a 1-cocycle, its class")
    _log("  [alpha] in H^1(B_n; gl_{Ad rho}) is the gauge-invariant content, and the")
    _log("  canonical second-order object built from it -- the cup square -- is")
    _log("  EXACTLY a coboundary (A5, Lean cupSq_eq_neg_coboundary), hence ZERO in")
    _log("  H^2.  Structural reason: q is a SINGLE direction; a curvature needs two,")
    _log("  and the generator indices i,j are group elements, not base directions.")
    _log("  The surviving invariant linear functional is tr alpha(w) = q d_q log det")
    _log("  rho(w) -- pure writhe/framing, already walled (A6).")
    _log()
    _log(f"  elapsed {time.time() - t0:.1f} s")

    w = WitnessBuilder("nastokes-germ-gauge-covariance", engine="sympy+numpy",
                       output_dir=HERE)
    w.set_description(
        "Bean qou-prjo.  Answers the question PR #4849 sec 2.3 left open: is the "
        "transverse NA-Stokes pairing Omega_2 gauge-covariant under the connection "
        "transformation law of the germ dq = q (d_q rho) rho^-1?  IT IS NOT.  "
        "Formalize-first: QOU/MassTheory/GermConnectionGaugeCovariance.lean "
        "(sorry-free, generic Ring, #print axioms clean on all 48 declarations) proves "
        "the germ is a 1-cocycle, proves the connection law, proves covariance holds "
        "IFF a defect vanishes, exhibits a concrete triple where it does not, proves "
        "the pairing is covariant GIVEN covariant inputs (so all failure sits in F_q), "
        "and proves the covariant second-order object -- the bracket cup square -- is "
        "EXACTLY a coboundary with explicit primitive beta = D.alpha, hence zero in H^2.  "
        "This probe verifies all of it against the actual Hecke germ: exactly over Q(q) "
        "in the 2-dim rep (connection law, nonzero defect, cup-square identity, "
        "gauge-invariance of tr alpha), and numerically on the corpus 4He atom word "
        "atom_braid_word_3A(2,2) in H_12(q) in TWO gauges -- diag(1,q,...,q^(d-1)) on "
        "Hoefsmit seminormal (covariance defect measured directly) and the reduced-Burau "
        "realization of the SAME lambda=(11,1) representation (compared via the "
        "conjugation-INVARIANT tr(Omega^k), so the comparison needs no intertwiner and "
        "is readout-independent).  Both show non-covariance.  Consequence: Omega_2 has "
        "no basis-independent value, so the germ-observer-pair selection question of "
        "#4849 is VOID rather than open.  Also retro-checks #4848: its Omega_2 = 0 on "
        "sigma_1^3 is itself gauge-dependent -- correct within a q-INDEPENDENT change of "
        "basis, not under the full connection freedom.  No AME quantity, no g_2, no "
        "binding number appears anywhere; free_parameters = 0; nothing wired; bean OPEN."
    )
    w.set_audit_only(True)
    w.add_parameter("q0_experimental_proton_anchor", repr(Q0))
    w.add_parameter("q0_pin", "experimental/proton (qou_substrate.constants.Q_50_DIGIT_STR)")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("algebra", "H_3(q) 2-dim rep (symbolic, exact Q(q)); H_12(q) "
                               "lambda=(11,1) and (10,1,1) (numeric)")
    w.add_parameter("gauges_compared",
                    "(a) Hoefsmit seminormal vs diag(1,q,...,q^(d-1)) rescaling; "
                    "(b) Hoefsmit seminormal lambda=(11,1) vs reduced Burau at "
                    "t=q^-2 scaled by q (the #4798/#4848 gauge)")
    w.add_parameter("germ_convention",
                    "logarithmic q-derivative q*(d_q rho)*rho^-1, analytic entry "
                    "derivatives; rho^-1 = rho - h from the Hecke relation")
    w.add_parameter("transport_convention",
                    "Yekutieli ordered partial product along the braid word")
    w.add_parameter("readout",
                    "conjugation-invariant tr(Omega^k) for the cross-gauge comparison; "
                    "Ad(B)^-1 Omega' - Omega for the explicitly-known gauge")
    w.add_parameter("lean_file",
                    "folio/quantum-observable-universe/lean/QOU/MassTheory/"
                    "GermConnectionGaugeCovariance.lean")
    for k, v in results.items():
        w.add_data(k, f64_json(v))
    for k, v in assertions.items():
        w.add_assertion(k, v, 1)
    w.add_caveat(
        "SCOPE-(b), STRUCTURAL EXCLUSION, for the claim 'Omega_2 (equivalently F_q) has "
        "a basis-independent value'.  Cited invariant: the germ is the right logarithmic "
        "derivative of a q-family, hence a 1-COCYCLE, defined only up to the coboundary "
        "(1 - Ad u)Theta; the induced defect on [dq_i, dq_j] is nonzero (Lean "
        "gaugeDefect_ne_zero; exhibited exactly here in A3), and the conjugation-invariant "
        "tr(Omega^k) demonstrably differ between two realizations of the SAME "
        "representation.  This is a proved algebraic obstruction, not a failed search.")
    w.add_caveat(
        "SCOPE-(a) for the residual question 'does SOME nonzero covariant functional of "
        "the germ exist'.  What is PROVED is that the canonical covariant second-order "
        "object (the bracket cup square) is identically a coboundary, and that the "
        "invariant linear functional tr alpha(w) = q d_q log det rho(w) sees only the "
        "abelianisation (writhe/framing, already walled).  A full classification of "
        "gauge-invariant functionals of [alpha] in H^1 is NOT attempted and stays open.")
    w.add_caveat(
        "RETRO-NARROWING OF #4848 (not a refutation).  Its algebra is correct and its "
        "quantification -- every intersection form J, every handle-exponent assignment -- "
        "is honoured.  But it did not range over q-DEPENDENT changes of representation "
        "basis, and under those the sigma_1^3 pairing is NONZERO (A4).  So #4848's "
        "scope-(b) should be read as conditional on a fixed germ trivialisation.  "
        "#4849 sec 2.3's parenthetical 'the answer there was 0 in every gauge' is "
        "correspondingly too strong.")
    w.add_caveat(
        "sorry-free != derived.  Nothing here derives a Delta_lambda, a binding energy, "
        "or a magnitude.  The bean's >= 3-body magnitude gate is untouched and OPEN.  "
        "This closes a route by showing its observable does not exist, which is a "
        "narrower and more fundamental statement than 'the value was not selected'.")
    w.add_caveat(
        "The A >= 3 germ is q-DEPENDENT (#4849 sec 2.2), so the q0 pin is material and "
        "is recorded.  q0 = experimental proton anchor per the owner directive of "
        "2026-08-07; no muon-serving cache is touched anywhere in this probe.")
    w.add_caveat(
        "Arithmetic: exact sympy over Q(q) in part A; float64 in part B, where the "
        "verdict is a 0-vs-O(1) question (covariance defect) and a "
        "relative-difference-of-invariants question at the 1e-1..1e0 level, not a "
        "1-ppQ question.  Representation certification residuals are reported.")
    w.save()
    _log("witness -> nastokes-germ-gauge-covariance.witness.json")

    ok = all(v == 1 for v in assertions.values())
    if not ok:
        _log("FAILING ASSERTIONS: "
             + ", ".join(k for k, v in assertions.items() if v != 1))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
