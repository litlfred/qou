#!/usr/bin/env python3
"""gamma-gamma word selection at H_3 by the confinement-SDP positivity readings,
at the proton pin, reading NO AME / CODATA binding value (bean qou-ales step 3).

## What is scanned, and why it is one-dimensional

Owner ruling 2026-09-08: every canonical braid word is SELECTED by gamma-gamma
pair production + the confinement SDP at q_0, never by census. Step 1
(`QOU.Mass.GammaGammaWordSelection`) defined a gamma-gamma word as a product of
pair-production vertices `sigma_i sigma_{i+1}^-1` and `SDPSelected` as
"every Wedderburn block image is `Matrix.PosSemidef`, cost-minimal". Step 3's
Lean (`QOU.Mass.GammaGammaSelectorH3.gammaGamma_inH3_eq_vertexPow`) proves that
inside H_3 -- generators 0, 1 only -- the gamma-gamma words are EXACTLY the
powers `V^k = (sigma_0 sigma_1^-1)^k`. So the candidate set is `{V^k}`, and
the crossing budget bounds `k`: with the corpus's 11-crossing nucleon budget
(bean qou-1qsw: 6 Borromean + 3 quark + 2 gluon), `2k <= 11` gives `k <= 5`.
The budget is a SCAN PARAMETER here (`--kmax`, default 5), not a choice made
against any measured number.

## The three readings of "PSD" that are tested, per block

The Lean predicate is the literal `Matrix.PosSemidef`, which is Hermitian AND
non-negative quadratic form. A braid word's block image is a product of the
generator images and need not be symmetric, so the literal predicate can fail
on the Hermitian half alone. To make the selection legible the probe tests, on
each Wedderburn block image M of each candidate:

  (i)   literal   -- `|M - M^T| ~ 0` AND every eigenvalue of M >= -tol
                     (this is `SDPSelected.psd`; Lean: `vertex_not_psdFeasible`
                     proves it FAILS for the single vertex).
  (ii)  form      -- eigenvalues of the symmetric part (M + M^T)/2 >= -tol
                     (the `forall x, x^T M x >= 0` half only).
  (iii) frobenius -- the block TRACE chi_lambda(M) >= -tol on blocks with
                     y_lambda > 0 (constraint (1) of prop:confinement-sdp,
                     `<pi_lambda, Phi> >= 0`; under convention D y_(1^3) = 0 so
                     the sign block does not constrain).

Selection under each reading: minimal crossing count (`SDPSelected.cost` =
word length, the H_2 precedent of `sdp_gamma_gamma_to_qqbar.py`) among the
feasible candidates -- reported BOTH as the literal minimum (which is `k = 0`,
the identity, whenever it is feasible; Lean `sdpSelected_nil`) and as the
minimal NON-ZERO feasible word (owner ruling 2026-08-30, bean qou-1qsw: on H_2
the selected vertex is the minimal non-zero PSD power, `sigma_0^2`).

## The pp bond and the diproton sign (qou-vbyi)

The template pp bond is a single `sigma` at the interface generator
(`atom_braid_word_3A`: gen `3k+2`), which `not_gammaGamma_single` says is not
gamma-gamma-produced. The gamma-gamma bond candidates are the vertex powers
`(sigma_2 sigma_3^-1)^m` on the interface strands of H_6. This probe

  * tests the three readings on the bond word alone in every H_6 block
    (restriction of H_6 blocks to the <sigma_2, sigma_3> ~ H_3 subalgebra), and
  * computes the pp binding functional of the live law
    (`binding_log_free_energy.py`, scale ruled 2026-09-05 in
    `binding_canonical.py`'s banner)

        B_pp = E_0 . ln( tr_M(W_free) / tr_M(W_atom) ),
        E_0  = m_e . c_q^2 . hbar_q / (1 - hbar_q^2),   c_q = 1/(q-1), hbar_q = 1 - 1/q,

    where this E_0 is the notation register's TOWER-SUMMED hadronic scale
    E_0^full = 4.2275 MeV (notation-collisions.md). It is NOT the Q_beta base
    E_0^(N=0) = m_e/(q(q-1)) = 4.1860 MeV, 0.99 % smaller, which shares the
    bare name `E_0` in the Q_beta producers; the printout carries both.

    on the full six-strand words `W_free = p(0,1) p(3,4)` and
    `W_atom = W_free . bond`, for the template bond and for each gamma-gamma
    bond `m = 1..kmax`. The nucleon block `p(.,.)` is the 11-letter
    `build_atom_nf` block of `frobenius_admissibility_net_row_probe.py`
    (cross-checked there against the float64 builder to 5e-16). The SIGN of
    B_pp is the falsifiable output; positive = binds (the diproton defect,
    `QOU.QBeta.SingleCrossingAlwaysBinds`), negative = unbound.

Nothing here reads AME2020 or a CODATA binding energy; m_e (CAL-1) enters
only as the MeV scale E_0 = E_0^full > 0, which cannot change a sign.

## Precision

mpmath at 60 dps end to end. Hoefsmit orthogonal matrices from
`hoefsmit_mpmath.seminormal_matrices_mp`; y_lambda under convention D from
`y_lambda_su_n(n, q, 2)`. q_0 is the proton pin `Q_50_DIGIT_STR`. Tolerance
for "zero" is 1e-40 (the working precision is 1e-60).

Cross-checks (assertions, not fits):
  * the (2,1) Hoefsmit data equals the closed form a = h/(1-q^4),
    b^2 = [3]_q/[2]_q^2 (Lean `hoefsmitA_mul_A'_add_one`);
  * tr_M(V^3) in H_3 equals the Lean Borromean closed form
    (4 + h^2 - 3h^4 - h^6)/(h^2 + 4);
  * the template pp ratio tr_M(W_atom)/tr_M(W_free) equals z_D = q^3/(q^2+1)
    (connected-sum multiplicativity, `atom_braid_word_3A` docstring);
  * tr_M of the template words agrees with `tr_m_atom_via_transfer.tr_m_atom_zn(2, 0)`.

Witness: computations/probes/gamma-gamma-h3-psd-selector-probe.witness.json
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from pyhecke.wedderburn import partitions_of  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")


# ---------------------------------------------------------------- words ----
def vertex(i: int, h):
    """sigma_i sigma_{i+1}^-1 as (c, d, gen) triples (sigma^-1 = sigma - h)."""
    return [(mp.mpf(1), mp.mpf(0), i), (mp.mpf(1), -h, i + 1)]


def vertex_pow(i: int, k: int, h):
    w = []
    for _ in range(k):
        w += vertex(i, h)
    return w


def nucleon_block(kind: str, h, offset: int = 0):
    """The 11-letter per-nucleon block of `build_atom_nf` on generators
    (offset, offset+1); identical to `frobenius_admissibility_net_row_probe`."""
    one, zero = mp.mpf(1), mp.mpf(0)
    g0, g1 = offset, offset + 1
    w = []
    for _ in range(3):                       # B_3 = (sigma_0 sigma_1^-1)^3
        w.append((one, zero, g0))
        w.append((one, -h, g1))
    if kind == "p":                          # uu@0, ud@0, ud@1
        w += [(one, zero, g0), (one, -h / 2, g0), (one, -h / 2, g1)]
    else:                                    # ud@0, ud@0, dd@1
        w += [(one, -h / 2, g0), (one, -h / 2, g0), (one, -h, g1)]
    w += [(one, zero, g0), (one, zero, g0)]  # gluon sigma_0^2 (qou-1qsw)
    return w


def word_image(sigmas, dim, word):
    """Left-to-right product of (c sigma_g + d I) over the word, as mp.matrix."""
    M = mp.eye(dim)
    I = mp.eye(dim)
    for c, d, g in word:
        M = M * (c * sigmas[g] + d * I)
    return M


# ------------------------------------------------------------ positivity ----
def sym_norm(M):
    return mp.norm(M - M.T)


def min_eig_sym(M):
    """Smallest eigenvalue of the symmetric part (M + M^T)/2."""
    S = (M + M.T) / 2
    return min(mp.eigsy(S)[0])


def min_eig(M):
    """Smallest real part among the eigenvalues of M itself."""
    ev = mp.eig(M)[0]
    return min(mp.re(e) for e in ev)


def trace(M, dim):
    return mp.fsum(M[i, i] for i in range(dim))


def readings(M, dim):
    """The three positivity readings on one block image."""
    s = sym_norm(M)
    literal = bool(s < TOL and min_eig(M) >= -TOL)
    form = bool(min_eig_sym(M) >= -TOL)
    chi = trace(M, dim)
    frob = bool(chi >= -TOL)
    return {"asym_norm": s, "min_eig_sym_part": min_eig_sym(M), "chi": chi,
            "literal": literal, "form": form, "frobenius": frob}


def select(rows, key):
    """Cost-minimal (crossing count) feasible candidate under one reading."""
    feas = [r for r in rows if r[key]]
    lit = min(feas, key=lambda r: r["crossings"]) if feas else None
    nz = [r for r in feas if r["crossings"] > 0]
    nzmin = min(nz, key=lambda r: r["crossings"]) if nz else None
    return lit, nzmin


# ----------------------------------------------------------------- main ----
def main() -> int:
    t0 = time.time()
    anchor = os.environ.get("QOU_Q0_ANCHOR", "").strip().lower()
    if anchor in ("ideal", "muon", "canonical"):
        raise SystemExit("this probe is a PROTON-pin producer (owner directive "
                         "2026-08-07); refusing a muon override")
    kmax = 5
    for a in sys.argv[1:]:
        if a.startswith("--kmax="):
            kmax = int(a.split("=", 1)[1])
    mp.mp.dps = DPS
    q = Q_MP
    qi = 1 / q
    h = q - qi
    z_d = q ** 3 / (q ** 2 + 1)
    cache = BlockCacheMP(q, h)

    print(f"gamma-gamma H_3 PSD selector -- proton pin, convention D, {DPS} dps, "
          f"kmax = {kmax} (crossing budget {2 * kmax} <= 11, qou-1qsw)")
    print("=" * 78)
    print(f"  q0 (proton) : {Q_50_DIGIT_STR[:32]}...")
    print(f"  h = q - 1/q : {mp.nstr(h, 15)}    z_D = {mp.nstr(z_d, 15)}")

    # ---------------------------------------------------- H_3 blocks -------
    parts3 = [tuple(p) for p in partitions_of(3)]          # (3), (2,1), (1,1,1)
    reps3 = {lam: seminormal_matrices_mp(lam, cache=cache) for lam in parts3}
    y3 = y_lambda_su_n(3, q, 2)
    y3 = {tuple(k): mp.mpf(v) for k, v in y3.items()}
    print(f"  y_lambda(3) D: " + ", ".join(f"{lam}: {mp.nstr(y3[lam], 10)}" for lam in parts3))

    # (2,1) data vs the closed form in the Lean file
    S21, _, _ = reps3[(2, 1)]
    a_cf = h / (1 - q ** 4)
    ap_cf = h / (1 - q ** (-4))
    b2_cf = (q ** 2 + 1 + q ** (-2)) / (q + qi) ** 2
    s0, s1 = S21[0], S21[1]
    # which of s0/s1 is diagonal depends on SYT ordering; find the diagonal one
    diag_idx = 0 if abs(s0[0, 1]) < TOL else 1
    Sd, So = (s0, s1) if diag_idx == 0 else (s1, s0)
    dev_diag = max(abs(Sd[0, 0] - q), abs(Sd[1, 1] + qi)) if abs(Sd[0, 0] - q) < 1 else \
        max(abs(Sd[1, 1] - q), abs(Sd[0, 0] + qi))
    dev_a = min(abs(So[0, 0] - a_cf) + abs(So[1, 1] - ap_cf),
                abs(So[1, 1] - a_cf) + abs(So[0, 0] - ap_cf))
    dev_b2 = abs(So[0, 1] ** 2 - b2_cf)
    print(f"  Hoefsmit (2,1) vs closed form: diag {mp.nstr(dev_diag, 3)}, "
          f"a/a' {mp.nstr(dev_a, 3)}, b^2 - [3]/[2]^2 {mp.nstr(dev_b2, 3)}")
    print(f"  generator index: sigma_{diag_idx} is the diagonal one in this SYT order")

    # H_3 candidate table: V^k
    rows3 = []
    print(f"\n  H_3 nucleon candidates V^k = (sigma_0 sigma_1^-1)^k")
    print(f"  {'k':>2}{'cross':>6}  {'|M-M^T|(2,1)':>14}{'min eig sym':>14}{'chi(2,1)':>14}"
          f"{'chi(3)':>9}{'chi(1^3)':>9}  {'lit':>4}{'form':>5}{'frob':>5}  {'|V^k-I|':>10}")
    for k in range(0, kmax + 1):
        w = vertex_pow(0, k, h)
        blocks = {}
        for lam in parts3:
            sig, dim, _ = reps3[lam]
            M = word_image(sig, dim, w)
            blocks[lam] = (M, dim)
        r21 = readings(*blocks[(2, 1)])
        r3 = readings(*blocks[(3,)])
        r111 = readings(*blocks[(1, 1, 1)])
        M21, _ = blocks[(2, 1)]
        dist_I = mp.norm(M21 - mp.eye(2))
        tr_m = mp.fsum(y3[lam] * trace(*blocks[lam]) for lam in parts3)
        # literal / form on ALL blocks; frobenius on y>0 blocks (D: (3), (2,1))
        row = {
            "k": k, "crossings": 2 * k,
            "chi_3": r3["chi"], "chi_21": r21["chi"], "chi_111": r111["chi"],
            "asym_21": r21["asym_norm"], "min_eig_sym_21": r21["min_eig_sym_part"],
            "dist_to_identity_21": dist_I, "tr_M": tr_m,
            "literal": r3["literal"] and r21["literal"] and r111["literal"],
            "form": r3["form"] and r21["form"] and r111["form"],
            "frobenius": all(r["frobenius"] for lam, r in
                             ((lam, x) for lam, x in [((3,), r3), ((2, 1), r21), ((1, 1, 1), r111)])
                             if y3[lam] > TOL),
        }
        rows3.append(row)
        print(f"  {k:>2}{2 * k:>6}  {mp.nstr(r21['asym_norm'], 6):>14}"
              f"{mp.nstr(r21['min_eig_sym_part'], 8):>14}{mp.nstr(r21['chi'], 10):>14}"
              f"{mp.nstr(r3['chi'], 4):>9}{mp.nstr(r111['chi'], 4):>9}  "
              f"{str(row['literal'])[0]:>4}{str(row['form'])[0]:>5}{str(row['frobenius'])[0]:>5}"
              f"  {mp.nstr(dist_I, 6):>10}")

    # Borromean closed-form cross-check (k = 3)
    bor_cf = (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)
    bor_dev = abs(rows3[3]["tr_M"] - bor_cf) if kmax >= 3 else None
    if bor_dev is not None:
        print(f"  tr_M(V^3) = {mp.nstr(rows3[3]['tr_M'], 20)} vs Lean closed form: dev {mp.nstr(bor_dev, 3)}")
    one_dim_dev = max(max(abs(r["chi_3"] - 1), abs(r["chi_111"] - 1)) for r in rows3)
    print(f"  max |chi_(3) - 1|, |chi_(1^3) - 1| over k: {mp.nstr(one_dim_dev, 3)}   (Lean: trivChar_eq_one, altChar_eq_one)")

    sel3 = {}
    for key in ("literal", "form", "frobenius"):
        lit, nz = select(rows3, key)
        sel3[key] = {"min_feasible_k": None if lit is None else lit["k"],
                     "min_nonzero_feasible_k": None if nz is None else nz["k"],
                     "feasible_k": [r["k"] for r in rows3 if r[key]]}
        print(f"  selection [{key:9}]: feasible k = {sel3[key]['feasible_k']}; "
              f"min k = {sel3[key]['min_feasible_k']}; min NON-ZERO k = {sel3[key]['min_nonzero_feasible_k']}")

    # ----------------------------------------- H_6: bond alone, and pp ----
    parts6 = [tuple(p) for p in partitions_of(6)]
    y6 = y_lambda_su_n(6, q, 2)
    y6 = {tuple(k): mp.mpf(v) for k, v in y6.items()}
    reps6 = {lam: seminormal_matrices_mp(lam, cache=cache) for lam in parts6}
    dims6 = {lam: reps6[lam][1] for lam in parts6}
    norm6 = mp.fsum(y6[lam] * dims6[lam] for lam in parts6)
    print(f"\n  H_6: {len(parts6)} blocks, sum y_lambda f^lambda = {mp.nstr(norm6, 12)}; "
          f"y > 0 on {[lam for lam in parts6 if y6[lam] > TOL]}")

    def tr_m6(word):
        return mp.fsum(y6[lam] * trace(word_image(reps6[lam][0], reps6[lam][1], word), reps6[lam][1])
                       for lam in parts6)

    # bond alone, all H_6 blocks
    bond_rows = []
    print(f"\n  pp bond candidates on the H_6 interface: template sigma_2, and (sigma_2 sigma_3^-1)^m")
    print(f"  {'bond':>12}{'cross':>6}  {'lit':>4}{'form':>5}{'frob':>5}   worst block (y>0): chi")
    cands = [("template s2", [(mp.mpf(1), mp.mpf(0), 2)])]
    cands += [(f"G^{m}", vertex_pow(2, m, h)) for m in range(0, kmax + 1)]
    for name, bw in cands:
        per = {}
        for lam in parts6:
            sig, dim, _ = reps6[lam]
            per[lam] = readings(word_image(sig, dim, bw), dim)
        lit = all(per[lam]["literal"] for lam in parts6)
        form = all(per[lam]["form"] for lam in parts6)
        frob = all(per[lam]["frobenius"] for lam in parts6 if y6[lam] > TOL)
        worst = min((lam for lam in parts6 if y6[lam] > TOL), key=lambda l: per[l]["chi"])
        row = {"bond": name, "crossings": len(bw), "literal": lit, "form": form,
               "frobenius": frob,
               "chi_by_block": {str(lam): fmt(per[lam]["chi"]) for lam in parts6},
               "min_eig_sym_by_block": {str(lam): fmt(per[lam]["min_eig_sym_part"]) for lam in parts6}}
        bond_rows.append(row)
        print(f"  {name:>12}{len(bw):>6}  {str(lit)[0]:>4}{str(form)[0]:>5}{str(frob)[0]:>5}   "
              f"{worst}: {mp.nstr(per[worst]['chi'], 10)}")
    sel6 = {}
    for key in ("literal", "form", "frobenius"):
        gg = [r for r in bond_rows if r["bond"].startswith("G^")]
        lit, nz = select(gg, key)
        sel6[key] = {"min_feasible": None if lit is None else lit["bond"],
                     "min_nonzero_feasible": None if nz is None else nz["bond"],
                     "feasible": [r["bond"] for r in gg if r[key]],
                     "template_feasible": bond_rows[0][key]}
        print(f"  bond selection [{key:9}]: feasible = {sel6[key]['feasible']}; "
              f"min NON-ZERO = {sel6[key]['min_nonzero_feasible']}; template sigma_2 feasible: {bond_rows[0][key]}")

    # pp binding functional
    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    hbar_q = 1 - qi
    c_q = 1 / (q - 1)
    E0 = me * c_q ** 2 * hbar_q / (1 - hbar_q ** 2)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0_n0 = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    print(f"\n  E_0 = E_0^full (ruled 2026-09-05) = {mp.nstr(E0, 12)} MeV   [NOT the Q_beta base E_0^(N=0) = m_e/(q(q-1)) = {mp.nstr(E0_n0, 10)}]")

    w_free = nucleon_block("p", h, 0) + nucleon_block("p", h, 3)
    tr_free = tr_m6(w_free)
    pp_rows = []
    print(f"  tr_M(W_free) [p p, no bond] = {mp.nstr(tr_free, 20)}")
    print(f"  {'bond':>12}{'cross':>6}  {'tr_M(W_atom)':>26}{'ratio atom/free':>22}{'B_pp [MeV]':>16}  sign")
    for name, bw in cands:
        if name == "G^0":
            continue
        tr_atom = tr_m6(w_free + bw)
        ratio = tr_atom / tr_free
        B = E0 * mp.log(abs(tr_free) / abs(tr_atom))
        sign = "binds (B>0)" if B > 0 else ("unbound (B<0)" if B < 0 else "zero")
        pp_rows.append({"bond": name, "crossings": len(bw), "tr_M_atom": fmt(tr_atom),
                        "ratio_atom_over_free": fmt(ratio), "B_pp_MeV": fmt(B),
                        "sign": sign, "tr_atom_negative": bool(tr_atom < 0)})
        print(f"  {name:>12}{len(bw):>6}  {mp.nstr(tr_atom, 20):>26}{mp.nstr(ratio, 16):>22}"
              f"{mp.nstr(B, 10):>16}  {sign}")
    tmpl_ratio_dev = abs(mp.mpf(pp_rows[0]["ratio_atom_over_free"]) - z_d)
    print(f"  template ratio vs z_D: dev {mp.nstr(tmpl_ratio_dev, 3)}   (connected-sum multiplicativity)")

    # transfer-path cross-check of the template pp traces (L1, not a fit)
    xfer_dev = None
    try:
        from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: PLC0415
        tr_atom_x, tr_free_x, _, _ = tr_m_atom_zn(2, 0, dps=50)
        xfer_dev = max(abs(tr_free_x - tr_free) / abs(tr_free),
                       abs(tr_atom_x - mp.mpf(pp_rows[0]["tr_M_atom"])) / abs(tr_atom_x))
        print(f"  vs tr_m_atom_via_transfer(2,0): max rel dev {mp.nstr(xfer_dev, 3)}")
    except Exception as e:  # noqa: BLE001 -- cross-check only; report, do not hide
        print(f"  transfer cross-check unavailable: {type(e).__name__}: {e}")

    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")
    print("\nReading. LITERAL Matrix.PosSemidef (the Lean SDPSelected.psd) admits only k = 0\n"
          "among the vertex powers: a vertex power's (2,1) image is never symmetric\n"
          "(Lean proves k = 1; measured here for k <= kmax). The two weaker readings\n"
          "select the minimal NON-ZERO survivor reported above. The pp sign is what the\n"
          "live log law gives with each bond, no AME read; see the audit doc for scope.")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gamma-gamma-h3-psd-selector-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales step 3: SDPSelected at H_3 over the gamma-gamma candidate set, which "
        "inside H_3 is exactly the vertex powers (sigma_0 sigma_1^-1)^k (Lean "
        "gammaGamma_inH3_eq_vertexPow). Three positivity readings per Wedderburn block "
        "(literal Matrix.PosSemidef; quadratic-form half; Frobenius positivity "
        "chi_lambda >= 0 on y_lambda > 0 blocks) at the proton pin, cost = crossing "
        "count, crossing budget a scan parameter. Also the pp bond candidates on the "
        "H_6 interface and the pp binding sign under the live log law. No AME/CODATA "
        "binding value read."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_parameter("dps", DPS)
    w.add_parameter("kmax", kmax)
    w.add_parameter("crossing_budget_source", "qou-1qsw: 11 crossings per nucleon; 2k <= 11")
    w.add_parameter("tolerance", fmt(TOL))
    w.add_parameter("cost", "crossing count (word length), SDPSelected.cost")
    w.add_parameter("E_0_MeV", fmt(E0))
    w.add_parameter("E_0_formula", "m_e c_q^2 hbar_q/(1 - hbar_q^2), c_q = 1/(q-1), hbar_q = 1 - 1/q")
    w.add_parameter("E_0_register_name", "E_0^full (tower-summed hadronic scale, notation-collisions.md); NOT the Q_beta base E_0^(N=0) = m_e/(q(q-1)) = 4.1860 MeV")
    w.add_data("h", fmt(h))
    w.add_data("z_D", fmt(z_d))
    w.add_data("y_lambda_3", {str(lam): fmt(y3[lam]) for lam in parts3})
    w.add_data("h3_candidates", [{
        "k": r["k"], "crossings": r["crossings"], "chi_3": fmt(r["chi_3"]),
        "chi_21": fmt(r["chi_21"]), "chi_111": fmt(r["chi_111"]),
        "asym_norm_21": fmt(r["asym_21"]), "min_eig_sym_part_21": fmt(r["min_eig_sym_21"]),
        "dist_to_identity_21": fmt(r["dist_to_identity_21"]), "tr_M": fmt(r["tr_M"]),
        "literal": r["literal"], "form": r["form"], "frobenius": r["frobenius"]} for r in rows3])
    w.add_data("h3_selection", sel3)
    w.add_data("h6_bond_candidates", bond_rows)
    w.add_data("h6_bond_selection", sel6)
    w.add_data("pp_tr_M_free", fmt(tr_free))
    w.add_data("pp_binding", pp_rows)
    w.add_data("template_pp_bond", "sigma_2 (single crossing at the interface; not gamma-gamma-produced)")
    w.add_assertion(name="hoefsmit_21_matches_closed_form",
                    computed=fmt(dev_diag + dev_a + dev_b2), expected="0", tolerance="1e-50",
                    source="Lean hoefsmitA_mul_A'_add_one: a=h/(1-q^4), b^2=[3]/[2]^2")
    w.add_assertion(name="one_dim_blocks_of_gamma_gamma_words_are_one",
                    computed=fmt(one_dim_dev), expected="0", tolerance="1e-50",
                    source="Lean trivChar_eq_one, altChar_eq_one")
    if bor_dev is not None:
        w.add_assertion(name="trM_borromean_matches_lean_closed_form",
                        computed=fmt(bor_dev), expected="0", tolerance="1e-50",
                        source="(4+h^2-3h^4-h^6)/(h^2+4)")
    w.add_data("vertex_21_asym_norm", fmt(rows3[1]["asym_21"]) if kmax >= 1 else None)
    w.add_assertion(name="single_vertex_not_literal_psd_feasible",
                    computed=str(int(rows3[1]["literal"])) if kmax >= 1 else "n/a",
                    expected="0", tolerance="0",
                    source="Lean vertex_not_psdFeasible: (2,1) off-diagonals q b vs -b/q")
    w.add_assertion(name="literal_psd_feasible_count_is_one",
                    computed=str(len(sel3["literal"]["feasible_k"])), expected="1", tolerance="0",
                    source="Lean sdpSelected_nil + measured k <= kmax")
    w.add_assertion(name="template_pp_ratio_equals_z_D",
                    computed=fmt(tmpl_ratio_dev), expected="0", tolerance="1e-50",
                    source="connected-sum multiplicativity of tr_M")
    if xfer_dev is not None:
        w.add_assertion(name="template_traces_match_transfer_path",
                        computed=fmt(xfer_dev), expected="0", tolerance="1e-45",
                        source="tr_m_atom_via_transfer.tr_m_atom_zn(2,0)")
    w.add_assertion(name="h6_weights_normalised",
                    computed=fmt(norm6 - 1), expected="0", tolerance="1e-50",
                    source="y_lambda_su_n: sum y f = 1")
    out = w.save()   # anchor resolved from q0_anchor_manifest.json by stem -> proton
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
