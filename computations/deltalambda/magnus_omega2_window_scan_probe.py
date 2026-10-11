#!/usr/bin/env python3
"""magnus_omega2_window_scan_probe.py — the Magnus Ω₂ pairing across the whole
faithful positive Markov window, A = 2, 3, 4.  Bean qou-uir6.

THE QUESTION
------------
Bean qou-za3q evaluated the second-order Magnus pairing

    P(w) = Σ_{λ ⊢ n} w_λ · tr(ρ_λ Ω₂_λ),        n = 3A,

at ONE trace: the convention-D Wenzl weight, z_D = q³/(q²+1).  Bean qou-uir6
records that every author classifies Ω₂ as a BINDING correction, that D7 puts
binding on the full tower, and that the faithful positive Markov traces on the
full tower are exactly the Ocneanu weights with z ∈ [0, h], h = q − 1/q
(`QOU.SchurWeyl.FullTowerTraceWindow`, `ocneanuWeight_pos_of_le`,
`sum_dim_ocneanuWeight_eq_one`, `sum_addable_ocneanuWeight`, all sorry-free).
z_D ≈ 0.6127 lies OUTSIDE that window (h ≈ 0.2091 at the proton q0).

This probe evaluates P(z) on the whole window, so the reconciliation question
has a measurement under it.  It selects NO point of the window.

METHOD — what is derived, what is reused, nothing chosen
--------------------------------------------------------
* Weights: the corpus definition, verbatim (`OcneanuWeight.lean:91`)

      w_μ(q,z) = ∏_{(i,j)∈μ} (q^{2i}(q²−1−qz) + q^{2j+1} z) / ∏_{(i,j)∈μ} (q^{2h(i,j)} − 1).

  Each numerator factor is LINEAR in z, the denominator is z-free, so w_μ is a
  polynomial of degree |μ| in z and therefore P(z) is a polynomial of degree
  ≤ n = 3A in z.  This probe builds that polynomial's coefficients exactly
  (mpf at the corpus compute precision) and evaluates / root-finds it — the
  endpoints z = 0 (Molien point, a = 0) and z = h (mirror-Molien, a = ∞) are
  plain evaluations of a polynomial, so "limit" and "value" coincide.
  Normalisation is Σ_λ f^λ w_λ = 1 (the y_λ-per-character slot, NOT y_λ f^λ),
  which is the slot the Ω₂ probes use for their Wenzl arm — checked below by
  reproducing their committed P_total_wenzl at z = z_D.
* Traces: tr(ρ_λ Ω₂_λ) for EVERY λ ⊢ n (including ≥3-row shapes, which Wenzl
  zeroes and the window does not), read from the committed witnesses of
  deuteron_magnus_omega2_sign_probe.py, triton_magnus_omega2_sign_probe.py,
  he4_magnus_omega2_sign_sparse_probe.py.  Nothing is recomputed.

PRECONDITIONS CHECKED (each is an assertion)
--------------------------------------------
1. every source witness is post the 2026-09-05 intra-nucleon ordering ruling
   (bean qou-hu1f; trap recorded in qou-za3q) and its producer builds the word
   with `atom_braid_word_3A`, whose default `intra_order` is "borromean";
2. every source carries ALL p(n) partitions (11 / 30 / 77);
3. every source was evaluated at the same q0 string this probe uses;
4. Σ_λ f^λ w_λ(z) ≡ 1 as a polynomial identity in z (coefficient check);
5. at z = z_D the weights equal `y_lambda_wenzl_bridge_numeric` and P(z_D)
   reproduces each witness's committed `P_total_wenzl`;
6. the imaginary-rank form (Lean `ocneanuWeight_zOfY`) agrees with the direct
   form at an interior window point;
7. every weight is strictly positive at every grid point of the window.

PRECISION
---------
mpmath throughout, no float64.  The traces carry 60 printed digits but are NOT
good to 60: each producer's germ A_g = q·∂_qσ_g·σ_g⁻¹ is a central finite
difference with EPS = 1e-50 at 70 dps, so rounding sets a relative floor near
1e-20.  This probe therefore records, at every grid point, the CANCELLATION
MARGIN  |P(z)| / Σ_λ w_λ(z)|tr_λ|  — a sign is reported as determined only
where that margin exceeds TRACE_REL_FLOOR = 1e-15 (five orders above the
estimated floor; the threshold is a precision guard, not a physics choice).
Root locations carry δz ≈ TRACE_REL_FLOOR · Σ w|tr| / |P'(z*)|.

DEGREE.  The z-coefficient of a cell's factor is q(q^{2j} − q^{2i}), zero on the
diagonal i = j; every μ contains (0,0), so deg w_μ ≤ |μ| − 1 and deg P ≤ 3A − 1
(measured 5 / 8 / 11).

RESULT (2026-10-11, proton q0; the witness is authoritative, not this text)
    A=2  P < 0 on all of [0, h]                       (no root in the window)
    A=3  P(0) = +2.9676e-4, one root z_T/h = 0.0038235, P < 0 on (z_T, h]
    A=4  P(0) = +2.8143e-7, one root z_He/h = 0.0100209, P < 0 on (z_He, h]
  So the sign pattern over A = 2,3,4 is (−,+,+) on [0, z_T), (−,−,+) on
  (z_T, z_He), and (−,−,−) on (z_He, h] — i.e. on ~99.0 % of the window the
  pattern matches z_D's (−,−,−), and only the sliver next to the Molien point
  carries the Plancherel-like (−,+,+). Margins at z = 0 are 1.45e-3 / 1.36e-5,
  far above the 1e-15 floor, so both z = 0 signs are determined.

NOT CLAIMED: that the window, z_D, or any z is the right trace for Ω₂ — that is
the owner decision qou-uir6 frames.  No point of the window is preferred, and
no z is ranked by the sign it gives or by agreement with anything.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent), str(HERE.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

# Corpus imports BEFORE our own set_compute_dps(): some corpus modules call
# set_compute_dps(50) at import time (memory TRAP, 2026-10-10).
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()

ORDERING_RULING = "2026-09-05"
TRACE_REL_FLOOR = mp.mpf("1e-15")
N_GRID = 20          # z_k = k·h/N_GRID, k = 0..N_GRID  (endpoints, h/2, 19 interior)
N_FINE = 2000        # fine sign scan used to bracket roots independently of polyroots

SOURCES = [
    # atom, A, witness, producer
    ("deuteron", 2, "deuteron-magnus-omega2-sign.witness.json",
     "deuteron_magnus_omega2_sign_probe.py"),
    ("triton", 3, "triton-magnus-omega2-sign.witness.json",
     "triton_magnus_omega2_sign_probe.py"),
    ("helium-4", 4, "he4-magnus-omega2-sign.witness.json",
     "he4_magnus_omega2_sign_sparse_probe.py"),
]
N_PARTITIONS = {6: 11, 9: 30, 12: 77}


# --------------------------------------------------------------- combinatorics
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def hook(lam, i, j):
    col = sum(1 for r in lam if r > j)
    return (lam[i] - j - 1) + (col - i - 1) + 1


def f_lambda(lam):
    """Hook-length formula, exact integer arithmetic."""
    num = 1
    for k in range(2, sum(lam) + 1):
        num *= k
    den = 1
    for i, j in cells(lam):
        den *= hook(lam, i, j)
    return num // den


# ------------------------------------------------------------- polynomial in z
def poly_mul(a, b):
    out = [mp.mpf(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def poly_eval(c, z):
    acc = mp.mpf(0)
    for x in reversed(c):
        acc = acc * z + x
    return acc


def poly_deriv(c):
    return [k * c[k] for k in range(1, len(c))]


def ocneanu_weight_poly(q, lam):
    """Coefficients (ascending in z) of ocneanuWeight q z lam — OcneanuWeight.lean:91.

    Per-cell numerator q^{2i}(q²−1−qz) + q^{2j+1} z = q^{2i}(q²−1) + (q^{2j+1} − q^{2i+1}) z.
    """
    num = [mp.mpf(1)]
    den = mp.mpf(1)
    for i, j in cells(lam):
        a = q ** (2 * i) * (q ** 2 - 1)
        b = q ** (2 * j + 1) - q ** (2 * i + 1)
        num = poly_mul(num, [a, b])
        den *= q ** (2 * hook(lam, i, j)) - 1
    return [c / den for c in num]


def imag_rank_weight(q, y, lam):
    """Lean `ocneanuWeight_zOfY`: ∏(y q^c + q^{-c}/y) / ((y+1/y)^n ∏ [h]_q), balanced [h]_q."""
    num = mp.mpf(1)
    den = (y + 1 / y) ** sum(lam)
    for i, j in cells(lam):
        c = j - i
        num *= y * q ** c + q ** (-c) / y
        hh = hook(lam, i, j)
        den *= (q ** hh - q ** (-hh)) / (q - 1 / q)
    return num / den


def sgn(x):
    return 0 if x == 0 else (1 if x > 0 else -1)


def file_hash12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


# ------------------------------------------------------------------------ main
def main() -> int:
    t0 = time.monotonic()
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    zD = q ** 3 / (q ** 2 + 1)
    print(f"dps {mp.mp.dps}   q0 {Q_50_DIGIT_STR}")
    print(f"h = q-1/q = {mp.nstr(h, 20)}   z_D = {mp.nstr(zD, 20)}  (outside [0,h])")

    checks = []

    def check(name, ok, detail=""):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}")

    grid = [h * k / N_GRID for k in range(N_GRID + 1)]
    atoms = []
    for atom, A, wname, pname in SOURCES:
        n = 3 * A
        print(f"\n=== {atom} (A={A}, n={n})")
        wp, pp = HERE / wname, HERE / pname
        doc = json.loads(wp.read_text())
        res = doc["results"]
        per = res["per_partition"]
        when = (doc.get("computedAt") or "")[:10]
        src = pp.read_text()
        live_hash = file_hash12(pp)
        rec_hash = doc.get("scriptHash")
        # --- preconditions
        check(f"{atom}: source post ordering ruling",
              bool(when) and when >= ORDERING_RULING, f"computedAt {when}")
        check(f"{atom}: producer builds word via atom_braid_word_3A, no intra_order override",
              "atom_braid_word_3A(" in src and "intra_order" not in src,
              "default intra_order='borromean' (mass_at_3A_proper.py:459)")
        shapes_w = {tuple(r["lambda"]) for r in per}
        shapes_all = set(partitions(n))
        check(f"{atom}: all p(n) partitions present incl. >=3-row",
              shapes_w == shapes_all and len(per) == N_PARTITIONS[n],
              f"{len(per)} of {len(shapes_all)}; max rows {max(len(s) for s in shapes_w)}")
        check(f"{atom}: source q0 equals this probe's q0",
              doc.get("q0Value") == Q_50_DIGIT_STR, f"{doc.get('q0Value')}")
        tr = {tuple(r["lambda"]): mp.mpf(r["tr_rho_Omega2"]) for r in per}

        # --- weight polynomials, normalisation identity
        wpoly = {lam: ocneanu_weight_poly(q, lam) for lam in shapes_all}
        norm = [mp.mpf(0)]
        for lam in shapes_all:
            norm = poly_add(norm, [f_lambda(lam) * c for c in wpoly[lam]])
        norm_err = max([abs(norm[0] - 1)] + [abs(c) for c in norm[1:]])
        check(f"{atom}: sum_lambda f^lambda w_lambda(z) == 1 identically in z",
              norm_err < mp.mpf(10) ** (-(mp.mp.dps - 15)), f"max coeff err {mp.nstr(norm_err, 3)}")

        # --- P(z) polynomial
        P = [mp.mpf(0)]
        for lam in shapes_all:
            P = poly_add(P, [tr[lam] * c for c in wpoly[lam]])
        dP = poly_deriv(P)

        # --- z_D cross-check against Wenzl bridge and the committed P_total_wenzl
        werr = mp.mpf(0)
        for lam in shapes_all:
            yw = y_lambda_wenzl_bridge_numeric(lam, q, dps=mp.mp.dps)
            werr = max(werr, abs(poly_eval(wpoly[lam], zD) - yw))
        P_zD = poly_eval(P, zD)
        P_w_committed = mp.mpf(res["P_total_wenzl"])
        dzd = abs(P_zD - P_w_committed)
        check(f"{atom}: w(z_D) == y_lambda_wenzl_bridge_numeric", werr < mp.mpf("1e-45"),
              f"max |diff| {mp.nstr(werr, 3)}")
        check(f"{atom}: P(z_D) reproduces committed P_total_wenzl",
              dzd < mp.mpf("1e-40") * max(1, abs(P_w_committed)),
              f"P(z_D) {mp.nstr(P_zD, 15)} vs {mp.nstr(P_w_committed, 15)}  |d| {mp.nstr(dzd, 3)}")

        # --- imaginary-rank cross-check at an interior point (y = 1 -> z = h/2)
        y0 = mp.mpf(1)
        zy = h * y0 ** 2 / (y0 ** 2 + 1)
        ierr = max(abs(poly_eval(wpoly[lam], zy) - imag_rank_weight(q, y0, lam))
                   for lam in shapes_all)
        check(f"{atom}: imaginary-rank form == direct form at y=1 (z=h/2)",
              ierr < mp.mpf("1e-50"), f"max |diff| {mp.nstr(ierr, 3)}")

        # --- grid
        rows = []
        min_w = None
        for k, z in enumerate(grid):
            ws = {lam: poly_eval(wpoly[lam], z) for lam in shapes_all}
            mw = min(ws.values())
            min_w = mw if min_w is None else min(min_w, mw)
            Pz = poly_eval(P, z)
            absum = sum(ws[lam] * abs(tr[lam]) for lam in shapes_all)
            margin = abs(Pz) / absum if absum else mp.mpf(0)
            determined = margin > TRACE_REL_FLOOR
            label = {0: "z=0 (Molien)", N_GRID: "z=h (mirror Molien)",
                     N_GRID // 2: "z=h/2"}.get(k, f"z={k}h/{N_GRID}")
            rows.append({"k": k, "label": label, "z": fmt(z), "P": fmt(Pz),
                         "sign": sgn(Pz) if determined else None,
                         "cancellation_margin": mp.nstr(margin, 6),
                         "sum_w_abs_tr": mp.nstr(absum, 15)})
            print(f"  {label:22s} z={mp.nstr(z, 8):>12}  P={mp.nstr(Pz, 15):>22}  "
                  f"margin {mp.nstr(margin, 3)}")
        check(f"{atom}: every weight strictly positive on the grid", min_w > 0,
              f"min w {mp.nstr(min_w, 5)}")

        # --- roots in [0,h]: polyroots, cross-checked by an independent fine sign scan
        deg = len(P) - 1
        while deg > 0 and P[deg] == 0:
            deg -= 1
        coeffs_desc = list(reversed(P[: deg + 1]))
        with mp.workdps(mp.mp.dps + 40):
            roots = mp.polyroots(coeffs_desc, maxsteps=400, extraprec=400)
        all_roots = [{"re": mp.nstr(mp.re(r), 20), "im": mp.nstr(mp.im(r), 20)} for r in roots]
        in_window = []
        for r in roots:
            if abs(mp.im(r)) < mp.mpf("1e-30") and 0 <= mp.re(r) <= h:
                in_window.append(mp.re(r))
        fine_changes = []
        prev = poly_eval(P, mp.mpf(0))
        for k in range(1, N_FINE + 1):
            z = h * k / N_FINE
            cur = poly_eval(P, z)
            if sgn(cur) != sgn(prev):
                fine_changes.append((h * (k - 1) / N_FINE, z))
            prev = cur
        root_rows = []
        for r in sorted(in_window):
            absum = sum(poly_eval(wpoly[lam], r) * abs(tr[lam]) for lam in shapes_all)
            dz = TRACE_REL_FLOOR * absum / abs(poly_eval(dP, r))
            root_rows.append({"z_root": fmt(r), "z_root_over_h": mp.nstr(r / h, 20),
                              "delta_z_from_trace_floor": mp.nstr(dz, 3)})
        check(f"{atom}: polyroots window-root count == fine sign-scan change count",
              len(in_window) == len(fine_changes),
              f"polyroots {len(in_window)}, sign changes {len(fine_changes)}")
        const_sign = len(in_window) == 0 and all(r["sign"] is not None for r in rows) \
            and len({r["sign"] for r in rows}) == 1
        print(f"  roots in [0,h]: {[mp.nstr(r, 15) for r in sorted(in_window)]}"
              f"   constant sign on window: {const_sign}")
        atoms.append({
            "atom": atom, "A": A, "n_strands": n, "n_partitions": len(per),
            "source_witness": wname, "source_computed_at": when,
            "source_scriptHash_recorded": rec_hash, "producer_hash_live": live_hash,
            "producer_hash_drifted": rec_hash != live_hash,
            "P_coefficients_ascending_in_z": [fmt(c) for c in P[: deg + 1]],
            "P_degree": deg,
            "P_at_zD_recomputed": fmt(P_zD), "P_total_wenzl_committed": res["P_total_wenzl"],
            "grid": rows,
            "roots_all_complex": all_roots,
            "roots_in_window": root_rows,
            "constant_sign_on_window": const_sign,
            "window_sign": rows[0]["sign"] if const_sign else None,
        })

    # sign pattern over A at each grid point
    pattern = []
    for k in range(N_GRID + 1):
        pattern.append({"label": atoms[0]["grid"][k]["label"], "z": atoms[0]["grid"][k]["z"],
                        "signs_A2_A3_A4": [a["grid"][k]["sign"] for a in atoms]})
    print("\nsign pattern over A=2,3,4:")
    for p in pattern:
        print(f"  {p['label']:22s} {p['signs_A2_A3_A4']}")

    wb = WitnessBuilder("magnus-omega2-window-scan", engine="mpmath",
                        start_time=t0)
    wb.set_description(
        "Magnus Omega2 pairing P(z) = sum_lambda w_lambda(z) tr(rho_lambda Omega2_lambda) "
        "across the full faithful positive Markov window z in [0, h], h = q - 1/q, at the "
        "proton q0, for A = 2, 3, 4, with w = ocneanuWeight (OcneanuWeight.lean:91). "
        "Re-weights the committed per-partition traces of the three sign probes (all "
        "p(n) partitions, post-ordering-ruling, borromean words); nothing recomputed. "
        "P(z) is a polynomial of degree <= 3A in z; its coefficients, a 21-point grid, "
        "and its roots in the window are recorded. Selects no point of the window. "
        "Bean qou-uir6.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data("q0", Q_50_DIGIT_STR)
    wb.add_data("h", fmt(h))
    wb.add_data("z_D", fmt(zD))
    wb.add_data("weight", "ocneanuWeight q z mu = prod_cells (q^{2i}(q^2-1-qz) + q^{2j+1} z) "
                          "/ prod_cells (q^{2h}-1); normalised sum_lambda f^lambda w_lambda = 1")
    wb.add_data("trace_rel_floor", fmt(TRACE_REL_FLOOR))
    wb.add_data("per_atom", atoms)
    wb.add_data("sign_pattern_over_A", pattern)
    wb.add_data("checks", checks)
    wb.add_data("adoption", "none — measurement for the qou-uir6 owner decision; not wired")
    wb.add_caveat(
        "Selects NO point of the window. The window is fixed by the sorry-free Lean "
        "(faithful + positive + full-tower Markov), not by this probe; z_D is evaluated "
        "only as a reproduction check against the committed Wenzl arm.")
    wb.add_caveat(
        "Trace precision: the producers' germ is a central finite difference "
        "(EPS = 1e-50 at 70 dps), so the traces are good to ~1e-20 relative despite 60 "
        "printed digits. A grid sign is recorded as null unless the cancellation margin "
        "|P|/sum w|tr| exceeds 1e-15.")
    wb.add_caveat(
        "The helium-4 source witness (computedAt 2026-09-11) has a recorded scriptHash "
        "that differs from its live producer; the clone is shallow so the diff cannot be "
        "inspected. Its word source (atom_braid_word_3A(2,2), default borromean) is "
        "unchanged since the ordering ruling and its P_total_wenzl is reproduced at z_D, "
        "so the traces are used; a regeneration was not run (H_12 sparse run is long).")
    for c in checks:
        wb.add_assertion(name=c["name"], computed="1" if c["passed"] else "0",
                         expected="1", tolerance="0", source=c["detail"] or None)
    out = wb.save()
    print(f"\nWitness: {out}  ({time.monotonic() - t0:.1f}s)")
    return 0 if all(c["passed"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
