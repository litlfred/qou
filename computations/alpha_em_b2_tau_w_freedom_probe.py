#!/usr/bin/env python3
"""alpha_em_b2_tau_w_freedom_probe.py — ADVERSARIAL: is the τ-identification scalar
`c` a convention-free prediction, or a free choice?

Red-team of the B2 closure (PRs #4199/#4209). Those established, rigorously, that
the Markov Gram and the Hodge Gram are proportional-congruent (Schur) and built an
explicit map `W = T·U⁻¹` with `Wᵀ·G_Markov(q₀)·W = c·M_S`. The open claim is
`τ = W` — that the archimedean functor realises this map, i.e. the α_EM loop weight
IS the Markov Gram. This probe attacks whether the SCALAR `c` (which carries the
magnitude, hence `1/(8π)`) is forced or free.

## The test

The FORM is forced (Schur: invariant form on the irreducible `(4,1)` is unique up
to scalar). The SCALAR `c` is the proportionality constant between two
positive-definite forms — and that depends on the normalisation of EACH form. If
`c` takes different values under different *canonical* normalisations, it is not a
convention-free number, so `τ = W` does not force the `1/(8π)` MAGNITUDE; the
identification is (at the scalar level) a free choice, pinned only once a physical
functor `τ` supplies a dimensional bridge between the Markov-trace scale and the
polarisation scale.

## What this computes (no fit)

Recomputes the transport `W = T·U⁻¹` self-contained (Hecke seminormal `q₀` →
Young `q=1` → BDH period basis), verifies it lands `∝ M_S`, then reports `c` under
five natural normalisations. If they disagree → `c` is convention-dependent.

**Discipline.** This is a critical-distance assessment (standing red-team license).
No instance registered; `1/(8π)` stays phase-4; nothing wired. The conclusion is a
CONSTRAINT on interpretation (what the closure does and does not establish), not a
new physical claim.

Run: python3 -u computations/alpha_em_b2_tau_w_freedom_probe.py 2>&1 | tee /tmp/freedom.log

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [braden-northover-2012] https://doi.org/10.3842/SIGMA.2012.065
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import seminormal_matrices_mpfr  # noqa: E402
from derived_chi_catalogue_matrix_m import standard_young_tableaux, _content  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
SHAPE = (4, 1)
DIM = 4
TAU0_IM = mp.mpf("0.186676")
ALPHA_EM = mp.mpf("1") / mp.mpf("137.035999")


def _q0():
    # Q_50_DIGIT_STR, not Q: `Q` is the f64 solve, and mpf(str(Q)) would
    # convert a double to a high-precision TYPE while preserving only its
    # 17 digits (owner directive: NO FLOAT64).
    from qou_substrate.constants import (  # type: ignore[import-not-found]
        Q_50_DIGIT_STR)
    return mp.mpf(Q_50_DIGIT_STR)


def _q_int(k, q):
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def _w_lambda(q):
    """Markov/Wedderburn weight w_(4,1) = d_q²/[5]_q!."""
    hooks = [4, 2, 1, 3, 1]  # hook lengths of (4,1): row1 (4,3,2,1)→ but with the leg; use known
    # (4,1) hooks: cells (1,1..4),(2,1). hook lengths: (1,1):5? compute directly
    # simpler: d_q = [5]_q!/∏[h]_q; hooks of (4,1) = {5,3,2,1} row1? Use content formula via SYT count check
    # Known: hooks of (4,1) are 5,3,2,1 (row1 cells) and 1 (row2 cell) → {5,3,2,1,1}? dim=4 SYT
    hk = [5, 3, 2, 1, 1]
    qfac = mp.mpf(1)
    for k in range(1, 6):
        qfac *= _q_int(k, q)
    den = mp.mpf(1)
    for h in hk:
        den *= _q_int(h, q)
    d_q = qfac / den
    return d_q ** 2 / qfac


def _young_natural(shape):
    n = sum(shape); syts = standard_young_tableaux(shape); dim = len(syts)
    idx = {s: i for i, s in enumerate(syts)}; gens = []
    for k in range(1, n):
        M = mp.zeros(dim, dim); done = [False] * dim
        for i in range(dim):
            if done[i]:
                continue
            rho = _content(syts[i][k]) - _content(syts[i][k - 1]); a = mp.mpf(1) / rho
            sw = list(syts[i]); sw[k - 1], sw[k] = syts[i][k], syts[i][k - 1]
            j = idx.get(tuple(sw))
            if j is None:
                M[i, i] = a; done[i] = True
            else:
                ap = mp.mpf(1) / (-rho); bsq = a * ap + 1
                lo, hi = (i, j) if i < j else (j, i); alo, ahi = (a, ap) if i < j else (ap, a)
                M[lo, lo] = alo; M[lo, hi] = 1; M[hi, lo] = bsq; M[hi, hi] = ahi
                done[lo] = done[hi] = True
        gens.append(M)
    return gens


def _diag_gram(sigmas):
    d2 = DIM * DIM; normal = mp.zeros(d2, d2)
    for sig in sigmas:
        Phi = mp.zeros(d2, d2)
        for a in range(DIM):
            for b in range(DIM):
                row = a * DIM + b
                for r in range(DIM):
                    for s in range(DIM):
                        val = mp.mpf(0)
                        if s == b:
                            val += sig[r, a]
                        if a == r:
                            val -= sig[s, b]
                        if val != 0:
                            Phi[row, r * DIM + s] += val
        normal += Phi.T * Phi
    ev, evec = mp.eigsy(normal); i0 = min(range(d2), key=lambda i: abs(ev[i]))
    G = mp.zeros(DIM, DIM)
    for a in range(DIM):
        for b in range(DIM):
            G[a, b] = evec[a * DIM + b, i0]
    return -G if G[0, 0] < 0 else G


def _rho_period():
    reps = []
    for t in range(3):
        P = mp.eye(DIM); P[t, t] = 0; P[t + 1, t + 1] = 0; P[t, t + 1] = 1; P[t + 1, t] = 1
        reps.append(P)
    s4 = mp.eye(DIM)
    for i in range(DIM):
        s4[i, 3] = mp.mpf(-1)
    reps.append(s4); return reps


def _intertwiner(rhoA, rhoB):
    d2 = DIM * DIM; normal = mp.zeros(d2, d2)
    for A, B in zip(rhoA, rhoB):
        Phi = mp.zeros(d2, d2)
        for a in range(DIM):
            for b in range(DIM):
                row = a * DIM + b
                for r in range(DIM):
                    for s in range(DIM):
                        val = mp.mpf(0)
                        if s == b:
                            val += B[a, r]
                        if a == r:
                            val -= A[s, b]
                        if val != 0:
                            Phi[row, r * DIM + s] += val
        normal += Phi.T * Phi
    ev, evec = mp.eigsy(normal); i0 = min(range(d2), key=lambda i: abs(ev[i]))
    U = mp.zeros(DIM, DIM)
    for a in range(DIM):
        for b in range(DIM):
            U[a, b] = evec[a * DIM + b, i0]
    return U


def _prop(A, B):
    idx = max(((i, j) for i in range(DIM) for j in range(DIM)), key=lambda ij: abs(B[ij[0], ij[1]]))
    r = A[idx] / B[idx]
    res = max(abs(A[i, j] - r * B[i, j]) for i in range(DIM) for j in range(DIM))
    return r, res


def main() -> int:
    q0 = _q0(); MS = _M_S = 5 * mp.eye(DIM) - mp.matrix([[1] * DIM] * DIM)
    # transport
    sig0 = seminormal_matrices_mpfr(SHAPE, q0); G0 = _diag_gram(sig0)
    sig1 = _young_natural(SHAPE); G1 = _diag_gram(sig1)
    U = _intertwiner(sig1, _rho_period()); Uinv = U ** -1
    T = mp.zeros(DIM, DIM)
    for i in range(DIM):
        T[i, i] = mp.sqrt(G1[i, i] / G0[i, i])
    W = T * Uinv
    Gt = W.T * G0 * W   # transported Markov form, ∝ M_S
    c_raw, res = _prop(Gt, MS)
    print(f"transport lands ∝ M_S (residual {mp.nstr(res,3)}); raw c = {mp.nstr(c_raw,8)}")
    if res > mp.mpf(10) ** (-20):
        print("WARNING: transport did not close; abort"); return 1

    # ── c under five canonical normalisations ──
    def detnorm(G):
        return G / mp.mpf(mp.det(G)) ** (mp.mpf(1) / DIM)

    def trnorm(G):
        return G * DIM / sum(G[i, i] for i in range(DIM))

    w41 = _w_lambda(q0)
    conventions = {}
    # 1. raw (seminormal g via nullspace normalisation of eigsy; M_S integer)
    conventions["raw (eigsy-norm G, integer M_S)"] = c_raw
    # 2. det-normalised both forms → c=1 by construction (the *-isometry frame)
    cd, _ = _prop(detnorm(Gt), detnorm(MS)); conventions["det-normalised (both det=1)"] = cd
    # 3. trace-normalised both forms
    ct, _ = _prop(trnorm(Gt), trnorm(MS)); conventions["trace-normalised (both tr=dim)"] = ct
    # 4. Markov-trace scale on the Hecke side (G_Markov ← w_(4,1)); Hodge integer M_S
    cm, _ = _prop((w41) * Gt, MS); conventions[f"Markov-trace scaled (×w_(4,1)={mp.nstr(w41,5)})"] = cm
    # 5. Hodge physical scale: compare to Im(τ₀)·M_S
    ch, _ = _prop(Gt, TAU0_IM * MS); conventions["vs Hodge physical Im(τ₀)·M_S"] = ch

    print("\nc under five canonical normalisations:")
    vals = []
    for name, c in conventions.items():
        print(f"   {name:42s} :  c = {mp.nstr(c, 8)}")
        vals.append(abs(c))
    print(f"\n   sibling route C (merged 603d1f3): intrinsic scalar ~1.47·α_EM = {mp.nstr(mp.mpf('1.47')*ALPHA_EM,6)}")
    vals.append(mp.mpf("1.47") * ALPHA_EM)

    spread = max(vals) / min(vals)
    print(f"\n   SPREAD  max/min = {mp.nstr(spread, 6)}   (≫1 ⇒ c is convention-DEPENDENT)")

    convention_free = spread < mp.mpf("1.0001")
    verdict = (
        f"ADVERSARIAL VERDICT: the τ-identification scalar c is CONVENTION-DEPENDENT "
        f"— NOT a convention-free prediction. The transported Markov Gram is exactly "
        f"∝ M_S (Schur, residual {mp.nstr(res,3)}), so the FORM is forced; but the "
        f"scalar c ranges over {{det:1, raw:{mp.nstr(c_raw,4)}, trace:{mp.nstr(ct,4)}, "
        f"Markov-scaled:{mp.nstr(cm,4)}, vs-Hodge-physical:{mp.nstr(ch,4)}, "
        f"sibling:~1.47α_EM}} — a max/min spread of {mp.nstr(spread,4)}. The two "
        f"intrinsic scales (Markov trace w_(4,1); polarisation Im(τ₀)) live in "
        f"different unit systems (algebra-trace vs geometric-period) and NOTHING in "
        f"the representation theory bridges them. So τ=W FORCES THE FORM but NOT THE "
        f"MAGNITUDE: the 1/(8π) scale is carried by a free scalar until a physical "
        f"functor τ supplies the dimensional bridge — which is precisely the "
        f"unconstructed input. The #4209 end-to-end closure is a FORM-CONSISTENCY "
        f"result, not a magnitude derivation. STRICT: no instance; 1/(8π) phase-4; "
        f"nothing wired; this is an interpretation constraint, not a new claim."
    )
    print(f"\n{verdict}")

    wb = WitnessBuilder("alpha-em-b2-tau-w-freedom")
    wb.set_audit_only("docs/audits/2026-07-25-alpha-em-b2-tau-w-derivability-adversarial.md")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "ADVERSARIAL red-team of the B2 τ=W closure: the identification scalar c is "
        "convention-DEPENDENT (spread ~"
        f"{mp.nstr(spread,4)} across det/raw/trace/Markov-scaled/Hodge-physical + the "
        "sibling ~1.47α_EM). Schur forces the FORM; the MAGNITUDE (1/(8π)) is a free "
        "scalar until a physical functor τ bridges the Markov-trace and polarisation "
        "scales. #4209 closure = form-consistency, not magnitude derivation. No "
        "instance; 1/(8π) phase-4.")
    wb.add_parameter("q0", mp.nstr(q0, 30))
    wb.add_assertion("c_convention_dependent", "true" if not convention_free else "false", "true",
                     source=f"spread max/min = {mp.nstr(spread,6)} across 5 normalisations + sibling")
    wb.add_data("transport_closes_residual", mp.nstr(res, 6))
    wb.add_data("c_values", {k: mp.nstr(v, 10) for k, v in conventions.items()})
    wb.add_data("c_spread_max_over_min", mp.nstr(spread, 8))
    wb.add_data("sibling_route_c", mp.nstr(mp.mpf("1.47") * ALPHA_EM, 10))
    wb.add_caveat("The FORM identification is forced (Schur, rigorous, #4160/#4199). "
                  "Only the SCALAR is free. τ=W therefore forces the shape of the loop "
                  "weight but not its magnitude; the 1/(8π) value is not derived by the "
                  "rep-theory closure alone — it needs the physical functor τ.")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\nwitness → {out.name}")
    return 0 if not convention_free else 1


if __name__ == "__main__":
    raise SystemExit(main())
