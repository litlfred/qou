#!/usr/bin/env python3
"""Independent derivation of the Whitehead-link adjoint Reidemeister torsion
|tau_adjoint(L5a1)| from the ideal-triangulation Neumann-Zagier data, closing the
gap qou-pn5j and upgrading c_sigma = 2^{-3/4} from IDENTIFICATION to DERIVATION.

Route 1 of bean qou-pn5j (Dimofte-Garoufalidis 1-loop = adjoint torsion).  The
1-loop invariant is the determinant of the gluing-equation Jacobian w.r.t.
log-shapes, on N equations = (N - #cusps independent edge equations) + (one
meridian per cusp):

    J_{k,j} = A_{k,j} - B_{k,j} * z_j/(1 - z_j),

where SnapPy's rect gluing equation k is   prod_i z_i^{A_i} (1 - z_i)^{B_i} = c_k,
so  d/d(log z_j) [ A log z + B log(1-z) ] = A - B * z/(1-z).

|tau| = |det J|  (validated: NO 1/2 factor and NO flattening monomial are needed
for the MODULUS, because the calibration below reproduces the known figure-eight
value |tau(4_1)| = sqrt(3) exactly).

CALIBRATION (non-circular): the SAME det(J) construction is run on 4_1, whose
adjoint torsion |tau| = sqrt(3) is classically known (trace field Q(sqrt(-3)),
c_sigma(4_1) = 3^{-1/4}).  Matching it pins the formula/normalization; L5a1 is
then a genuine prediction, NOT a fit of c_sigma.

RESULT (corrects the earlier qou-k00d inference).  The independent 1-loop
computation gives  |tau(L5a1)| = 4 sqrt(2) = 2^{5/2}  (det J = 4(1+i), a clean
Gaussian integer) -- i.e. a FACTOR OF 2 LARGER than the |tau| = 2 sqrt(2) that
the bare knot template c_sigma = |tau|^{-1/2} would infer from c_sigma = 2^{-3/4}.
The resolution is a per-cusp normalization: for a c-cusp link,

    c_sigma = 2^{(c-1)/2} * |tau_meridian|^{-1/2}

    - 4_1  (c=1):  2^0     * (sqrt 3)^{-1/2}   = 3^{-1/4}          (matches)
    - L5a1 (c=2):  2^{1/2} * (2^{5/2})^{-1/2}  = 2^{1/2-5/4} = 2^{-3/4}  (matches)

So c_sigma = 2^{-3/4} is DERIVED, via the geometrically-computed torsion
|tau| = 2^{5/2} plus the sqrt(2) two-cusp factor -- NOT via the (incorrect)
tau = 2 sqrt(2) inference.  The extra factor 2^{(c-1)/2} is consistent with the
two known cases (c = 1, 2); its general-c form is a smaller open sub-item (it
matches the standard per-cusp Gaussian-integration factor in the GGMW/Ohtsuki
saddle asymptotic).

⚠ REFUTED 2026-08-07 (PR #4691, bean qou-fl4t).  |det J| as computed here is
NOT a topological invariant: retriangulating the same manifold gives 8 distinct
values for 5_2 (a ONE-cusped knot), 17 for 6_2, 6 for L5a1, 7 for L6a4.  The
calibration on 4_1 cannot detect this — 4_1 has two tetrahedra, the one class
with no room to vary under Pachner moves.

The ambiguity group has since been identified (one_loop_ambiguity_group_probe.py):
it is the UNIT GROUP OF THE TRACE FIELD — sqrt(2) for L5a1/L6a4, sqrt(plastic)
for 5_2 (disc(x^3-x-1) = -23, the 5_2 trace field, ~30 digits).  That is exactly
where the dropped DG flattening monomial prod z''^f'' z'^f' lives, confirming the
diagnosis.  So the per-cusp factor 2^{(c-1)/2} below is not merely unproved, it
is UNIDENTIFIABLE: no universal constant absorbs a manifold-dependent unit group.

c_sigma = 2^{-3/4} therefore reverts to IDENTIFICATION (bean qou-pn5j, reopened).
[RESOLVED 2026-08-08: back to DERIVATION, but NOT by this file's route -- see
docs/audits/2026-08-08-c-sigma-derivation-status.md. The per-cusp factor below
does not exist; the derivation runs through the triangulation-invariant
computations/one_loop_torsion.py and carries the prefactor form as its one
stated assumption.]
Its NUMERICAL VALUE is unaffected — whitehead_c_sigma_hiprec.py pins it to ~20
digits independently, with no SnapPy and no det J.  Repair = restore the
flattening + the 1/2, then re-run the invariance probe.

⚠⚠ SUPERSEDED 2026-08-08 — THE PER-CUSP FACTOR DISSOLVES ENTIRELY.
(probes/one_loop_c_sigma_percusp_dissolution_probe.py; audit
docs/audits/2026-08-08-per-cusp-factor-dissolves.md)

The repair is done: `computations/one_loop_torsion.py` now computes the
triangulation-invariant DG invariant at ANY cusp number, giving
|tau(4_1)| = sqrt(3)/2, |tau(L5a1)| = sqrt(2), |tau(L6a4)| = 8 — NOT the
sqrt(3), 2^{5/2}, 64 computed here.  Against those,

    k_c := c_sigma * |tau_DG|^{1/2}   is the SAME constant 2^{-1/2}
    at c = 1 and c = 2, to 17 digits.

A per-cusp factor would require k to move by sqrt(2) between them; the measured
ratio is 0.999999999999999995.  So the correct law has NO per-cusp factor:

    c_sigma = 2^{-1/2} |tau_DG|^{-1/2}

and calibrating it on 4_1 ALONE predicts c_sigma(L5a1) = 2^{-3/4} to 17 digits
with nothing adjustable.

WHY THE FIT ABOVE LOOKED LIKE IT WORKED.  On the DEFAULT triangulations of 4_1,
L5a1 and L6a4 — and not in general — |tau_old| = 2^c |tau_DG|.  Substituting,
2^{(c-1)/2} |tau_old|^{-1/2} = 2^{-1/2} |tau_DG|^{-1/2} identically.  The
"standard per-cusp Gaussian-integration factor" claimed above was exactly the
c-dependence needed to undo that 2^c.  It is a reparametrization, and the 2^c
relation fails on 8 of the 13 manifolds tested — including 5_2, 6_2 and 7_4 at
c = 1, where there is no per-cusp factor to blame.

Audit-only; the derived tau is NOT wired to any production dashboard.
-- Ref: Dimofte-Garoufalidis, "The quantum content of the gluing equations",
        Geom. Topol. 17 (2013) 1253-1315 (1-loop invariant).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


def _rank_independent_rows(rows):
    """Greedily select a maximal set of C-linearly-independent row indices."""
    basis = []          # reduced echelon vectors
    chosen = []
    for idx, row in enumerate(rows):
        v = list(row)
        for b_idx, b in basis:
            piv = next(i for i, x in enumerate(b) if abs(x) > mp.mpf(10) ** -20)
            if abs(v[piv]) > mp.mpf(10) ** -20:
                f = v[piv] / b[piv]
                v = [vi - f * bi for vi, bi in zip(v, b)]
        if any(abs(x) > mp.mpf(10) ** -20 for x in v):
            basis.append((idx, v))
            chosen.append(idx)
    return chosen


def one_loop_torsion(name: str):
    """|det J| for manifold `name`, using indep. edges + one meridian per cusp."""
    import snappy
    M = snappy.Manifold(name)
    N = M.num_tetrahedra()
    ncusps = M.num_cusps()
    # High-precision shape read (bean qou-t0rf).  `complex(s)` is float64, so
    # the previous `mp.mpc(complex(s))` capped this computation near 16 digits
    # regardless of `mp.mp.dps`, and made its own 4_1 values wobble at digit 16
    # across runs.  Both halves are needed: asking SnapPy for `bits_prec` is
    # useless if the value is then routed through a double.
    _bits = int(mp.mp.dps * 3.3219) + 16
    z = [mp.mpc(mp.mpf(str(s.real()).replace(' ', '')), mp.mpf(str(s.imag()).replace(' ', '')))
         for s in M.tetrahedra_shapes('rect', bits_prec=_bits)]
    t = [z[j] / (1 - z[j]) for j in range(N)]           # z_j/(1-z_j)

    ge = M.gluing_equations('rect')                     # list of (A, B, c)
    nedges = len(ge) - 2 * ncusps                       # edges, then (mer,long)*cusps

    def jac_row(A, B):
        return [A[j] - B[j] * t[j] for j in range(N)]

    edge_rows = [jac_row(A, B) for (A, B, c) in ge[:nedges]]
    # one meridian per cusp: rect order is [mer, long] per cusp after the edges
    merid_rows = [jac_row(*ge[nedges + 2 * i][:2]) for i in range(ncusps)]

    indep = _rank_independent_rows(edge_rows)[: N - ncusps]
    J_rows = [edge_rows[i] for i in indep] + merid_rows
    J = mp.matrix(J_rows)
    det = mp.det(J)
    return abs(det), det, z


# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
mp.mp.dps = 50

if __name__ == "__main__":
    mp.mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 40

    print(f"1-loop adjoint torsion from NZ data — mpmath dps={mp.mp.dps}\n")

    # --- calibration on the figure-eight (|tau| = sqrt(3) known) ---
    tau41, det41, _ = one_loop_torsion('4_1')
    sqrt3 = mp.sqrt(3)
    rel41 = abs(tau41 - sqrt3) / sqrt3
    dig41 = int(-mp.log10(rel41)) if rel41 > 0 else 999
    print("CALIBRATION  4_1:")
    print(f"  |det J|      = {mp.nstr(tau41, 25)}")
    print(f"  sqrt(3)      = {mp.nstr(sqrt3, 25)}")
    print(f"  match: ~{dig41} digits   ({'OK' if dig41 >= 12 else 'FAIL'})\n")

    # --- prediction for the Whitehead link ---
    tauW, detW, zW = one_loop_torsion('L5a1')
    import snappy
    ncW = snappy.Manifold('L5a1').num_cusps()
    target = 4 * mp.sqrt(2)                              # 2^{5/2} (DERIVED torsion)
    relW = abs(tauW - target) / target
    digW = int(-mp.log10(relW)) if relW > 0 else 999
    # colored-Jones prefactor via the per-cusp normalization c_sigma = 2^{(c-1)/2}|tau|^{-1/2}
    csig = mp.power(2, (ncW - 1) / mp.mpf(2)) * tauW ** (mp.mpf(-1) / 2)
    csig_target = mp.power(2, mp.mpf(-3) / 4)
    rel_cs = abs(csig - csig_target) / csig_target
    dig_cs = int(-mp.log10(rel_cs)) if rel_cs > 0 else 999
    print("PREDICTION  L5a1 (Whitehead):")
    print(f"  shapes z     = {[mp.nstr(s, 6) for s in zW]}")
    print(f"  det J        = {mp.nstr(detW, 20)}   (= 4(1+i))")
    print(f"  |tau| = |det J| = {mp.nstr(tauW, 25)}")
    print(f"  4*sqrt(2)=2^5/2 = {mp.nstr(target, 25)}")
    print(f"  match: ~{digW} digits   ({'DERIVED' if digW >= 12 else 'NO MATCH'})")
    print(f"\n  c_sigma = 2^((c-1)/2)|tau|^(-1/2), c={ncW}:")
    print(f"    derived  = {mp.nstr(csig, 20)}")
    print(f"    2^(-3/4) = {mp.nstr(csig_target, 20)}   (match ~{dig_cs} digits)")

    # --- 3-cusp cross-check: Borromean rings L6a4 (corpus: W1 probe, PR #4238) ---
    # |det J_NZ(L6a4)| = 64 is ALREADY in the corpus
    # (computations/probes/borromean_nz_adjoint_torsion.py, 2026-07-25); this
    # reproduces it independently and tests the per-cusp factor at c=3.
    tauB, detB, zB = one_loop_torsion('L6a4')
    ncB = snappy.Manifold('L6a4').num_cusps()
    tauB_target = mp.mpf(64)                             # 2^6
    # Guard on the RELATIVE ERROR, not on tauB. Once the shape read stopped
    # losing precision to SnapPy's spaced exponents this hit 64 exactly, and
    # `tauB > 0` let log10(0) = -inf through into int() — a crash on success.
    relB = abs(tauB - tauB_target) / tauB_target
    digB = int(-mp.log10(relB)) if relB > 0 else 999
    # unified relation  exp(2 c0) = 2^{c-1}/|det J|  =>  c0 = (1/2) log(2^{c-1}/|det|)
    c0B_pred = mp.log(mp.power(2, ncB - 1) / tauB) / 2
    c0B_measured = mp.mpf("-1.3828105122579213")         # W1 Jones-side, NMAX=56 (borromean-jones-1loop-torsion.witness.json)
    csigB = mp.power(2, (ncB - 1) / mp.mpf(2)) * tauB ** (mp.mpf(-1) / 2)
    print(f"\n  CROSS-CHECK  L6a4 (Borromean, c={ncB}) — corpus |det|=64 (W1/#4238):")
    print(f"    |tau| = {mp.nstr(tauB, 18)}  (target 2^6=64; ~{digB} digits)")
    print(f"    c_sigma = 2^((c-1)/2)|tau|^-1/2 = {mp.nstr(csigB, 12)} (= 1/4)")
    print(f"    c0 predicted (unified law) = {mp.nstr(c0B_pred, 8)}")
    print(f"    c0 measured  (W1 Jones)    = {mp.nstr(c0B_measured, 8)}"
          f"   -> {mp.nstr(abs(c0B_pred-c0B_measured)/abs(c0B_measured)*100, 3)}% "
          f"(fit err; W1 p=1.4993 vs 3/2)")

    ok = dig41 >= 12 and digW >= 12 and dig_cs >= 12 and digB >= 12
    print("\n  ARITHMETIC:", "internally consistent at this precision."
          if ok else "not clean at this precision; inspect formula/curve choice.")
    print("  VERDICT: SUPERSEDED. The numbers above reproduce, but |det J| is not a")
    print("  topological invariant (PR #4691) and the per-cusp factor does not exist")
    print("  (probes/one_loop_c_sigma_percusp_dissolution_probe.py). The invariant")
    print("  values are |tau(4_1)|=sqrt(3)/2, |tau(L5a1)|=sqrt(2), |tau(L6a4)|=8, from")
    print("  computations/one_loop_torsion.py; the law is c_sigma = 2^{-1/2}|tau|^{-1/2}.")
    print("  c_sigma = 2^{-3/4} IS derived, but by that route, not this one --")
    print("  docs/audits/2026-08-08-c-sigma-derivation-status.md.")

    wit = {
        "superseded": "2026-08-08: |det J| here is not a topological invariant (PR #4691) and the per-cusp factor 2^{(c-1)/2} does not exist. Invariant values: |tau(4_1)|=sqrt(3)/2, |tau(L5a1)|=sqrt(2), |tau(L6a4)|=8 via computations/one_loop_torsion.py; law is c_sigma = 2^{-1/2}|tau_DG|^{-1/2}. c_sigma=2^{-3/4} is DERIVED by that route (docs/audits/2026-08-08-c-sigma-derivation-status.md), not by this file. Values below are retained for history only.",
        "description": "[SUPERSEDED] Independent 1-loop (Dimofte-Garoufalidis) adjoint Reidemeister torsion of the Whitehead link L5a1 from SnapPy Neumann-Zagier data: |tau(L5a1)|=4sqrt(2)=2^{5/2} (det J=4(1+i)), DERIVED (not inverted from c_sigma), calibrated on 4_1 where the same det(J) reproduces the known |tau|=sqrt(3). c_sigma=2^{-3/4} follows via c_sigma=2^{(c-1)/2}|tau|^{-1/2} (per-cusp sqrt(2) factor). CORRECTS the earlier qou-k00d inference tau=2sqrt(2) -> tau=4sqrt(2).",
        "computation": "whitehead_c_sigma_torsion", "audit_only": True,
        "dps": mp.mp.dps,
        "method": "1-loop invariant det(J), J_{kj}=A_{kj}-B_{kj} z_j/(1-z_j), (N-c indep edges)+(meridians)",
        "calib_4_1": {"det_abs": mp.nstr(tau41, 25), "sqrt3": mp.nstr(sqrt3, 25),
                       "match_digits": dig41},
        "whitehead_L5a1": {"num_cusps": ncW, "det": mp.nstr(detW, 20),
                            "tau_abs": mp.nstr(tauW, 25),
                            "target_2_pow_5_2": mp.nstr(target, 25),
                            "match_digits": digW},
        "c_sigma_relation": "c_sigma = 2^{(c-1)/2} * |tau_meridian|^{-1/2}   <=>   exp(2 c0) = 2^{c-1}/|det J_NZ|",
        "c_sigma_derived": mp.nstr(csig, 25),
        "c_sigma_target_2_pow_minus_3_4": mp.nstr(csig_target, 25),
        "c_sigma_match_digits": dig_cs,
        "borromean_L6a4_crosscheck": {
            "num_cusps": ncB, "tau_abs": mp.nstr(tauB, 25), "target_2_pow_6": "64",
            "match_digits": digB,
            "corpus_source": "computations/probes/borromean_nz_adjoint_torsion.py (W1, PR #4238, 2026-07-25) already has |det|=64; reproduced here independently",
            "c_sigma_derived": mp.nstr(csigB, 20),
            "c0_predicted_unified_law": mp.nstr(c0B_pred, 15),
            "c0_measured_W1_jones": "-1.3828105122579213",
            "note": "c=3 confirms the per-cusp factor: predicted c0=-1/2 ln16=-1.3863 vs W1 Jones-side -1.3828 (~0.25%, within the NMAX=56 fit error; W1 p=1.4993 vs 3/2)."},
        "corrects_prior_inference": "qou-k00d/PR#4571 recorded tau=2sqrt(2) (naive knot template); independent 1-loop gives tau=4sqrt(2)=2^{5/2}; resolved by the 2-cusp sqrt(2) normalization.",
        "cusp_factor_status": "2^{(c-1)/2} now supported on THREE cases: c=1 (4_1, exact), c=2 (L5a1, 20-digit c_sigma), c=3 (L6a4, ~0.25% vs W1 Borromean c0). Unifies the repo W1 knot relation exp(2c0)=1/|det| to exp(2c0)=2^{c-1}/|det|. General-c proof (per-cusp Gaussian factor) is a smaller open sub-item.",
        "derivation_complete": bool(ok),
        "reference": "Dimofte-Garoufalidis, Geom. Topol. 17 (2013) 1253; Porti adjoint torsion",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-c-sigma-torsion.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(wit, indent=2))
    print(f"\n  Witness: {out}")
