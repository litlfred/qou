#!/usr/bin/env python3
"""binding_functional_window_probe.py — the two binding functionals across the faithful
positive Markov window z in [0, h], h = q - 1/q.

EXPLORATORY. NOT WIRED. Bean `qou-slz5`, option 4 of the owner's 2026-10-11 decision
("re-examine the binding functional"). This probe does NOT select a Markov point by
symmetry — that is bean `qou-wktw` — and does NOT compare anything to AME binding
energies (anti-fit directive: no ranking by agreement). It reports what each
(functional, z) combination DERIVES and where it is defined.

SETTING (all held fixed)
------------------------
* Words: `atom_braid_word_3A(Z, N, intra_order="borromean")`, with (W_atom) and without
  (W_free) the inter-nucleon bond letters — the canonical words of
  `full_tower_weight_two_arm_probe.py`.
* Characters: `chi_all_lambda_any(word, 3A, dps=50)` over ALL p(3A) partitions, at the
  proton-pinned q0 (`Q_50_DIGIT_STR`).
* Trace at Markov parameter z: tr_z(x) = Σ_λ w_λ(q, z) χ^λ(x), with w_λ the closed-form
  Ocneanu weight of `QOU.SchurWeyl.ocneanuWeight`:
      w_λ(q,z) = Π_{(i,j)∈λ} (q^{2i}(q² − 1 − q z) + q^{2j+1} z) / Π_{(i,j)∈λ} (q^{2h(i,j)} − 1).
  Every cell factor is LINEAR in z, so w_λ — and hence tr_z(x) — is a POLYNOMIAL in z of
  degree ≤ n. The probe carries those polynomials explicitly (mpf coefficients), so a
  root of tr_z in the window is located as a root of a polynomial, not by a grid search.
  FullTowerTraceWindow.lean (T2) proves this is THE Markov trace with parameter z for
  z ≠ h; at z = h (ζ = q² − 1 − q z = 0) the weights are still the polynomial values and
  are reported as the limit.
* Functionals (both from the corpus):
      B_lin(z) = Q_β(n) · (tr_z(W_free) − tr_z(W_atom))                 [binding_canonical]
      B_log(z) = E_0 · log(tr_z(W_free) / tr_z(W_atom)),  E_0 = m_e/(q0(q0 − 1))
                                                                   [binding_log_free_energy]
  B_log is reported in two readings: SIGNED (real only where the ratio is > 0) and ABS
  (log of |ratio|, which is what the live code takes). The difference is the question.

CROSS-CHECKS (asserted)
-----------------------
* Σ_λ f^λ w_λ(z) ≡ 1 as a polynomial in z (normalisation, Lean T2), every n.
* z = 0 reproduces the Molien measure f·q^{−κ}·dim_q/[n]_q! of the two-arm probe.
* z = z_D = q³/(q²+1) (outside the window, reference only) reproduces the convention-D
  y_λ (`y_lambda_at`) and binding_canonical's Δtr.
* FACTORISATION (measured, not assumed): tr_z(W_atom) = Π_bonds (c_k z + d_k) · tr_z(W_free)
  and tr_z(W_free) = Π_nucleons tr_z(W_nucleon), checked coefficient-by-coefficient on the
  polynomials. This is the split-braid multiplicativity of a Markov trace; it is checked
  here to the 50-dps resolution of the characters and is NOT proved here (the general-z
  bond formula is bean `qou-5zl1`).

RESULTS (2026-10-11, this probe's witness; 29/29 checks)
---------------------------------------------------------
* Structure (measured, coeff dev <= 1e-50, not proved): tr_z(W_atom) =
  Π_bonds(z + d_k)·P_p(z)^Z·P_n(z)^N, tr_z(W_free) = P_p^Z·P_n^N, with P_p, P_n EXACT
  quadratics in z over Q(q) (sympy; cubic term vanishes). P_n is anti-palindromic,
  P_n = K(1 − z²) + B z, so its roots pair z ↔ −1/z.
* In-window roots: pp bond z = 0; pn bond z_pn = h(1/2 − δ/4) = 0.499656 h; nn bond
  z = h; proton P_p at 0.432695 h; neutron P_n at 0.910019 h.
* B_log = −E_0 Σ_bonds log(z + d_k): the nucleon polynomials cancel IDENTICALLY, so the
  log functional sees only the bond letters, at every z. Signed reading: D and ³He need
  z > z_pn, T and ⁴He need z < z_pn — real for all four atoms on NO z in [0, h].
  Abs reading: finite on (0, h) minus {z_pn}, diverges at z_pn for every atom (all have
  a pn bond), and at z = 0 (³He, ⁴He) and z = h (T, ⁴He).
* B_lin = Q_β P_p^Z P_n^N (1 − Π(z + d_k)), sign = sign(P_p^Z P_n^N). Positive for all
  four atoms exactly on (z_n, h], z_n = neutron root. Using that requires the
  empirical SIGN "all four are bound" — a comparison-boundary input, not a derivation.

Precision: mpmath throughout, 70 dps weights, 50 dps characters (passed explicitly). No
float64. Output: binding-functional-window-probe.witness.json (this directory).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

# Corpus imports BEFORE set_compute_dps (some set dps at import time).
from _precision import set_compute_dps, fmt  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

INTRA_ORDER = "borromean"
CHI_DPS = 50
ATOMS = (("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2))
N_INTERIOR = 10


# ── exact combinatorics ────────────────────────────────────────────────────
def conj_of(lam):
    return [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []


def hook(lam, i, j):
    return lam[i] - j + conj_of(lam)[j] - i - 1


def f_lambda(lam) -> int:
    n = sum(lam)
    num = 1
    for k in range(2, n + 1):
        num *= k
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            den *= hook(lam, i, j)
    assert num % den == 0
    return num // den


def content_sum(lam) -> int:
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


# ── polynomials in z (ascending mpf coefficient lists) ─────────────────────
def pmul(a, b):
    out = [mp.mpf(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def padd(a, b, s=1):
    m = max(len(a), len(b))
    a = a + [mp.mpf(0)] * (m - len(a))
    b = b + [mp.mpf(0)] * (m - len(b))
    return [x + s * y for x, y in zip(a, b)]


def pscale(a, c):
    return [c * x for x in a]


def peval(a, z):
    acc = mp.mpf(0)
    for c in reversed(a):
        acc = acc * z + c
    return acc


def pmaxabs(a):
    return max(abs(x) for x in a) if a else mp.mpf(0)


def ocneanu_weight_poly(lam, q):
    """w_λ(q, z) as a polynomial in z (Lean `ocneanuWeight`, row i, column j)."""
    num = [mp.mpf(1)]
    den = mp.mpf(1)
    for i in range(len(lam)):
        for j in range(lam[i]):
            a0 = q ** (2 * i) * (q ** 2 - 1)
            a1 = q ** (2 * j + 1) - q ** (2 * i + 1)
            num = pmul(num, [a0, a1])
            den *= q ** (2 * hook(lam, i, j)) - 1
    return pscale(num, 1 / den)


def q_int(m, q):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def dim_q(lam, q):
    n = sum(lam)
    num = mp.mpf(1)
    for m in range(1, n + 1):
        num *= q_int(m, q)
    den = mp.mpf(1)
    for i in range(len(lam)):
        for j in range(lam[i]):
            den *= q_int(hook(lam, i, j), q)
    return num / den


def trace_poly(chi, wpoly):
    out = [mp.mpf(0)]
    for s, c in chi.items():
        out = padd(out, pscale(wpoly[s], c))
    return out


def real_roots_in(poly, lo, hi, scale_tol):
    """Real roots of poly in [lo, hi] (inclusive, tolerance-padded)."""
    p = list(poly)
    top = pmaxabs(p)
    while len(p) > 1 and abs(p[-1]) < scale_tol * top:
        p.pop()
    if len(p) <= 1:
        return []
    with mp.workdps(mp.mp.dps + 40):
        rts = mp.polyroots(list(reversed(p)), maxsteps=400, extraprec=400)
    pad = mp.mpf(10) ** (-30)
    out = []
    for r in rts:
        r = mp.mpc(r)
        if abs(r.imag) < mp.mpf(10) ** (-30) and lo - pad <= r.real <= hi + pad:
            out.append(r.real)
    return sorted(out)


def nucleon_subwords(word, A):
    """Split the free word into its A three-strand nucleon words (generators shifted)."""
    subs = [[] for _ in range(A)]
    for c, d, g in word:
        k = g // 3
        assert g % 3 in (0, 1), f"free word carries a bond letter at g={g}"
        subs[k].append((c, d, g - 3 * k))
    return subs


# ── exact nucleon trace polynomials over Q(q) (sympy) ──────────────────────
def exact_nucleon_polys(w_free_D, h_num):
    """P_p(z), P_n(z) EXACTLY in Q(q)[z]: H_3 irreps (the unique 2-dim (2,1) rep with
    σ1 = diag(q, −1/q), solved from the Hecke + braid relations) × the Lean Ocneanu
    weight. Letters are matched to the exact templates {0, −h, −h/2} (no δ enters a
    nucleon word). Returns {name: (ascending sympy coeffs, q-symbol)}."""
    qs, zs = sp.symbols("q z", positive=True)
    hs = qs - 1 / qs
    sig = [sp.diag(qs, -1 / qs),
           sp.Matrix([[-1 / (qs * (qs ** 2 + 1)), 1],
                      [(qs ** 2 - qs + 1) * (qs ** 2 + qs + 1) / (qs ** 2 + 1) ** 2,
                       hs + 1 / (qs * (qs ** 2 + 1))]])]
    for g in (0, 1):
        assert sp.simplify(sig[g] ** 2 - hs * sig[g] - sp.eye(2)) == sp.zeros(2)
    assert sp.simplify(sig[0] * sig[1] * sig[0] - sig[1] * sig[0] * sig[1]) == sp.zeros(2)

    def sym_d(d):
        for cand, v in ((sp.Integer(0), 0), (-hs, -h_num), (-hs / 2, -h_num / 2)):
            if abs(mp.mpf(d) - v) < mp.mpf("1e-40"):
                return cand
        raise ValueError(f"nucleon letter d={d} not in the exact template set")

    def weight(lam):
        num, den = sp.Integer(1), sp.Integer(1)
        for i in range(len(lam)):
            for j in range(lam[i]):
                num *= qs ** (2 * i) * (qs ** 2 - 1 - qs * zs) + qs ** (2 * j + 1) * zs
                den *= qs ** (2 * hook(lam, i, j)) - 1
        return num / den

    subs = {"proton": [t for t in w_free_D if t[2] in (0, 1)],
            "neutron": [(c, d, g - 3) for c, d, g in w_free_D if g in (3, 4)]}
    out = {}
    for name, word in subs.items():
        M = sp.eye(2)
        ch = {(3,): sp.Integer(1), (1, 1, 1): sp.Integer(1)}
        for c, d, g in word:
            assert abs(mp.mpf(c) - 1) < mp.mpf("1e-60")
            dd = sym_d(d)
            M = M * (sig[g] + dd * sp.eye(2))
            ch[(3,)] *= qs + dd
            ch[(1, 1, 1)] *= -1 / qs + dd
        ch[(2, 1)] = sp.factor(sp.simplify(M.trace()))
        P = sp.Poly(sp.cancel(sum(weight(l) * ch[l] for l in ch)), zs)
        out[name] = ([sp.factor(c) for c in reversed(P.all_coeffs())], qs)
    return out


def cluster_roots(roots, tol):
    """Merge numerically split multiple roots; [(root, multiplicity)]."""
    out = []
    for r in sorted(roots):
        if out and abs(r - out[-1][0]) < tol:
            m = out[-1][1]
            out[-1] = ((out[-1][0] * m + r) / (m + 1), m + 1)
        else:
            out.append((r, 1))
    return out


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    mp.mp.dps = max(mp.mp.dps, 70)
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    z_D = q ** 3 / (q ** 2 + 1)
    m_e = mp.mpf(M_E_MEV)
    Qb = mp.mpf(Q_NEUTRON_MEV)
    E0 = m_e / (q * (q - 1))
    floor = mp.mpf(10) ** (-(CHI_DPS - 10))
    checks = []

    def chk(name, ok, detail=""):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

    def log(msg):
        print(f"[{time.monotonic() - t0:7.1f}s] {msg}", flush=True)

    wcache = {}

    def weights(n, shapes):
        if n not in wcache:
            wcache[n] = {s: ocneanu_weight_poly(s, q) for s in shapes}
            norm = [mp.mpf(0)]
            for s in shapes:
                norm = padd(norm, pscale(wcache[n][s], f_lambda(s)))
            dev = pmaxabs(padd(norm, [mp.mpf(1)], -1))
            chk(f"n={n}: Σ f^λ w_λ(z) ≡ 1 as a polynomial in z", dev < mp.mpf("1e-60"),
                f"max coeff dev={mp.nstr(dev, 3)}")
            qf = mp.mpf(1)
            for m in range(1, n + 1):
                qf *= q_int(m, q)
            dmol = max(abs(wcache[n][s][0] - q ** (-content_sum(s)) * dim_q(s, q) / qf)
                       for s in shapes)
            chk(f"n={n}: w_λ(0) = Molien q^-κ dim_q/[n]_q!", dmol < mp.mpf("1e-60"),
                f"max dev={mp.nstr(dmol, 3)}")
            y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}
            dD = max(abs(peval(wcache[n][s], z_D) - y.get(s, mp.mpf(0))) for s in shapes)
            chk(f"n={n}: w_λ(z_D) = convention-D y_λ (y_lambda_at)", dD < mp.mpf("1e-45"),
                f"max dev={mp.nstr(dD, 3)}")
        return wcache[n]

    # the z grid
    grid = [("0 (Molien endpoint)", mp.mpf(0))]
    grid += [(f"{k}h/{N_INTERIOR + 1}", k * h / (N_INTERIOR + 1))
             for k in range(1, N_INTERIOR + 1)]
    grid += [("h/2 (sign-twist fixed point)", h / 2), ("h (mirror endpoint)", h)]

    rows = []
    for atom, Z, N in ATOMS:
        A = Z + N
        n = 3 * A
        w_atom = atom_braid_word_3A(Z, N, include_inter=True, intra_order=INTRA_ORDER)
        w_free = atom_braid_word_3A(Z, N, include_inter=False, intra_order=INTRA_ORDER)
        bonds = [(mp.mpf(c), mp.mpf(d), g) for c, d, g in w_atom if g % 3 == 2]
        log(f"{atom}: n={n}, {len(bonds)} bond letters, characters ...")
        chi_a = {tuple(k): mp.mpf(v) for k, v in
                 chi_all_lambda_any(w_atom, n, dps=CHI_DPS).items()}
        chi_f = {tuple(k): mp.mpf(v) for k, v in
                 chi_all_lambda_any(w_free, n, dps=CHI_DPS).items()}
        mp.mp.dps = max(mp.mp.dps, 70)
        shapes = sorted(chi_a, reverse=True)
        W = weights(n, shapes)
        P_a = trace_poly(chi_a, W)
        P_f = trace_poly(chi_f, W)
        log(f"{atom}: {len(shapes)} partitions; trace polynomials built")

        # control: z_D reproduces binding_canonical Δtr
        from binding_canonical import binding_canonical
        ref = binding_canonical(Z, N)
        gap = abs(mp.mpf(ref["delta_tr_exact"]) - (peval(P_f, z_D) - peval(P_a, z_D)))
        chk(f"{atom}: tr at z_D reproduces binding_canonical Δtr (< 1e-40)",
            gap < mp.mpf("1e-40"), f"gap={mp.nstr(gap, 3)}")

        # factorisation, measured on the polynomials
        bond_poly = [mp.mpf(1)]
        for c, d, _g in bonds:
            bond_poly = pmul(bond_poly, [d, c])
        fac_dev = pmaxabs(padd(P_a, pmul(bond_poly, P_f), -1))
        chk(f"{atom}: tr_z(W_atom) ≡ Π_bonds(c z + d)·tr_z(W_free) (coeff dev < 1e-40)",
            fac_dev < mp.mpf("1e-40"), f"dev={mp.nstr(fac_dev, 3)}")
        nuc_polys = []
        for sw in nucleon_subwords(w_free, A):
            chi3 = {tuple(k): mp.mpf(v) for k, v in
                    chi_all_lambda_any(sw, 3, dps=CHI_DPS).items()}
            mp.mp.dps = max(mp.mp.dps, 70)
            nuc_polys.append(trace_poly(chi3, weights(3, sorted(chi3, reverse=True))))
        prod_nuc = [mp.mpf(1)]
        for p in nuc_polys:
            prod_nuc = pmul(prod_nuc, p)
        split_dev = pmaxabs(padd(P_f, prod_nuc, -1))
        chk(f"{atom}: tr_z(W_free) ≡ Π_nucleons tr_z(W_nucleon) (coeff dev < 1e-40)",
            split_dev < mp.mpf("1e-40"), f"dev={mp.nstr(split_dev, 3)}")

        rtol = mp.mpf(10) ** (-12) * h   # polyroots splits a k-fold root by ~eps^(1/k)
        roots_a = cluster_roots(real_roots_in(P_a, mp.mpf(0), h, mp.mpf("1e-40")), rtol)
        roots_f = cluster_roots(real_roots_in(P_f, mp.mpf(0), h, mp.mpf("1e-40")), rtol)
        bond_roots = sorted(-d / c for c, d, _ in bonds)
        nuc_roots = [real_roots_in(p, mp.mpf(0), h, mp.mpf("1e-40")) for p in nuc_polys]
        if atom == "D":
            nuc_D = nuc_polys
            w_free_D = w_free

        samples = []
        for label, z in grid:
            ta, tf = peval(P_a, z), peval(P_f, z)
            van_a, van_f = abs(ta) < floor, abs(tf) < floor
            ratio = None if (van_a or van_f) else tf / ta
            B_lin = Qb * (tf - ta)
            b_abs = None if ratio is None else E0 * mp.log(abs(ratio))
            b_sgn = (E0 * mp.log(ratio)) if (ratio is not None and ratio > 0) else None
            samples.append({
                "label": label, "z": fmt(z), "z_over_h": mp.nstr(z / h, 12),
                "tr_atom": fmt(ta), "tr_free": fmt(tf),
                "tr_atom_vanishes": bool(van_a), "tr_free_vanishes": bool(van_f),
                "bond_factor_product": fmt(peval(bond_poly, z)),
                "B_lin_MeV": fmt(B_lin),
                "B_log_abs_MeV": fmt(b_abs) if b_abs is not None else None,
                "B_log_signed_MeV": fmt(b_sgn) if b_sgn is not None else None,
                "B_log_signed_defined": b_sgn is not None,
            })
            log(f"  {atom:>3} z={mp.nstr(z / h, 6):>8}h  tr_a={mp.nstr(ta, 8):>15} "
                f"tr_f={mp.nstr(tf, 8):>14}  B_lin={mp.nstr(B_lin, 8):>13}  "
                f"B_log|.|={mp.nstr(b_abs, 8) if b_abs is not None else 'undef':>11}  "
                f"B_log(signed)={mp.nstr(b_sgn, 8) if b_sgn is not None else 'undef'}")

        rows.append({
            "atom": atom, "Z": Z, "N": N, "A": A, "n_strands": n,
            "n_partitions": len(shapes),
            "bond_letters": [{"generator": g, "c": fmt(c), "d": fmt(d),
                              "root_z_eq_minus_d_over_c": fmt(-d / c),
                              "root_over_h": mp.nstr(-d / c / h, 15)}
                             for c, d, g in bonds],
            "tr_atom_poly_coeffs_ascending": [fmt(x) for x in P_a],
            "tr_free_poly_coeffs_ascending": [fmt(x) for x in P_f],
            "nucleon_trace_polys_ascending": [[fmt(x) for x in p] for p in nuc_polys],
            "nucleon_trace_roots_in_window": [[fmt(r) for r in rs] for rs in nuc_roots],
            "factorisation_max_coeff_dev": mp.nstr(fac_dev, 5),
            "split_max_coeff_dev": mp.nstr(split_dev, 5),
            "roots_in_window_tr_atom": [{"z": fmt(r), "z_over_h": mp.nstr(r / h, 15),
                                         "multiplicity": m} for r, m in roots_a],
            "roots_in_window_tr_free": [{"z": fmt(r), "z_over_h": mp.nstr(r / h, 15),
                                         "multiplicity": m} for r, m in roots_f],
            "bond_roots": [fmt(r) for r in bond_roots],
            "samples": samples,
        })

    # signed-log well-definedness: where is tr_free/tr_atom > 0 for every atom?
    # On the window both polynomials are known with their roots; test the sign of the
    # ratio on each sub-interval between consecutive critical points (all atoms pooled).
    crit = {mp.mpf(0), h}
    for r in rows:
        crit |= {mp.mpf(x["z"]) for x in r["roots_in_window_tr_atom"]}
        crit |= {mp.mpf(x["z"]) for x in r["roots_in_window_tr_free"]}
    crit = sorted(crit)
    intervals = []
    for lo, hi in zip(crit, crit[1:]):
        if hi - lo < mp.mpf(10) ** (-40):
            continue
        mid = (lo + hi) / 2
        signs, blin = {}, {}
        for r in rows:
            Pa = [mp.mpf(x) for x in r["tr_atom_poly_coeffs_ascending"]]
            Pf = [mp.mpf(x) for x in r["tr_free_poly_coeffs_ascending"]]
            signs[r["atom"]] = int(mp.sign(peval(Pf, mid) / peval(Pa, mid)))
            blin[r["atom"]] = int(mp.sign(peval(Pf, mid) - peval(Pa, mid)))
        intervals.append({"lo": fmt(lo), "hi": fmt(hi), "lo_over_h": mp.nstr(lo / h, 12),
                          "hi_over_h": mp.nstr(hi / h, 12), "ratio_sign": signs,
                          "B_lin_sign": blin,
                          "signed_log_real_for_all_atoms":
                              all(v > 0 for v in signs.values()),
                          "B_lin_positive_for_all_atoms":
                              all(v > 0 for v in blin.values())})
    selector = [iv for iv in intervals if iv["signed_log_real_for_all_atoms"]]
    blin_pos = [iv for iv in intervals if iv["B_lin_positive_for_all_atoms"]]
    print("\nPer open sub-interval of [0,h]: sign(tr_free/tr_atom) | sign(B_lin):")
    for iv in intervals:
        print(f"  ({iv['lo_over_h']}h, {iv['hi_over_h']}h): ratio {iv['ratio_sign']}"
              f"  B_lin {iv['B_lin_sign']}")
    print(f"Sub-intervals where signed B_log is real for ALL four atoms: {len(selector)}")
    print(f"Sub-intervals where B_lin > 0 for ALL four atoms: "
          f"{[(iv['lo_over_h'], iv['hi_over_h']) for iv in blin_pos]}")
    chk("signed B_log is real for all four atoms on NO sub-interval of [0,h]",
        len(selector) == 0, f"{len(selector)} intervals")

    # exact nucleon polynomials, checked against the 50-dps ones
    log("exact nucleon trace polynomials over Q(q) (sympy) ...")
    ex = exact_nucleon_polys(w_free_D, h)
    exact_out = {}
    for k, name in enumerate(("proton", "neutron")):
        coeffs, qs = ex[name]
        vals = [sp.lambdify(qs, c, "mpmath")(q) for c in coeffs]
        dev = max(abs(a - b) for a, b in zip(vals + [mp.mpf(0)] * 4, nuc_D[k] + [mp.mpf(0)] * 4))
        chk(f"exact {name} P(z) over Q(q) matches the 50-dps polynomial at q0 (< 1e-40)",
            dev < mp.mpf("1e-40"), f"dev={mp.nstr(dev, 3)}")
        exact_out[name] = {"coeffs_ascending_in_z": [str(c) for c in coeffs],
                           "degree_in_z": len(coeffs) - 1}
    cn = ex["neutron"][0]
    anti = sp.simplify(cn[0] + cn[2]) == 0 if len(cn) == 3 else False
    chk("neutron P_n(z) is anti-palindromic: z^0 coeff = −z^2 coeff exactly "
        "(roots pair z <-> −1/z)", anti)
    exact_out["neutron"]["anti_palindromic"] = bool(anti)
    if anti:
        K, B = cn[0], cn[1]   # P_n = K(1 − z²) + B z
        disc = sp.sqrt(B ** 2 + 4 * K ** 2)
        cands = [(B + disc) / (2 * K), (B - disc) / (2 * K)]
        cvals = [sp.lambdify(ex["neutron"][1], c, "mpmath")(q) for c in cands]
        k_in = [i for i, v in enumerate(cvals) if 0 <= v <= h]
        chk("exactly one root of P_n lies in [0, h]", len(k_in) == 1,
            f"roots at q0: {[mp.nstr(v, 12) for v in cvals]}")
        z_n_num = cvals[k_in[0]]
        exact_out["neutron"]["K"] = str(K)
        exact_out["neutron"]["B"] = str(B)
        exact_out["neutron"]["root_in_window_closed_form"] = (
            "P_n(z) = K(1 - z^2) + B z; roots (B ± sqrt(B^2 + 4K^2))/(2K), product −1. "
            f"In-window root at q0 is the '{'+' if k_in[0] == 0 else '−'}' branch; "
            "K < 0 iff q^3 − q − 1 < 0 (q below the plastic number), as at q0")
        exact_out["neutron"]["root_in_window_at_q0"] = fmt(z_n_num)
        exact_out["neutron"]["root_in_window_over_h"] = mp.nstr(z_n_num / h, 15)

    w = WitnessBuilder("binding-functional-window-probe", engine="python", start_time=t0)
    w.set_description(
        "B_lin and B_log (signed and abs readings) for D, T, 3He, 4He across the "
        "faithful positive Markov window z in [0, h], h = q - 1/q, with the trace at "
        "parameter z carried as an explicit polynomial in z (Ocneanu closed-form weight "
        "x characters over all p(3A) partitions, borromean words, proton q0). Locates "
        "the in-window roots of tr(W_atom), tr(W_free) and tests where each functional "
        "is defined. EXPLORATORY: not wired; no AME comparison; no selection by "
        "symmetry (bean qou-wktw).")
    w.add_data("q0", Q_50_DIGIT_STR)
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("h", fmt(h))
    w.add_data("z_D_reference_outside_window", fmt(z_D))
    w.add_data("intra_order", INTRA_ORDER)
    w.add_data("chi_dps", CHI_DPS)
    w.add_data("weight_family",
               "ocneanu_markov_weight(q, z) — QOU.SchurWeyl.ocneanuWeight; NOT y_lambda "
               "except at z = z_D")
    w.add_data("functionals", {
        "B_lin": "Q_beta(n)·(tr_z(W_free) − tr_z(W_atom))",
        "B_log_signed": "E_0·log(tr_z(W_free)/tr_z(W_atom)); real only where ratio > 0",
        "B_log_abs": "E_0·log|tr_z(W_free)/tr_z(W_atom)| (live-code reading)",
    })
    w.add_data("E_0_MeV", fmt(E0))
    w.add_data("Q_beta_n_MeV", str(Q_NEUTRON_MEV))
    w.add_data("vanishing_floor", f"|tr| < 1e-{CHI_DPS - 10} treated as zero")
    w.add_data("rows", rows)
    w.add_data("sign_intervals", intervals)
    w.add_data("signed_log_real_for_all_atoms_intervals", selector)
    w.add_data("B_lin_positive_for_all_atoms_intervals", blin_pos)
    w.add_data("exact_nucleon_trace_polynomials", exact_out)
    w.add_data("structure_note", (
        "Measured (coefficient dev <= 1e-50): tr_z(W_atom) = Π_bonds(z + d_k) · "
        "P_p(z)^Z · P_n(z)^N and tr_z(W_free) = P_p^Z P_n^N. Hence B_log(z) = "
        "−E_0 Σ_bonds log(z + d_k): the nucleon polynomials cancel identically and the "
        "log functional sees ONLY the bond letters; B_lin = Q_β P_p^Z P_n^N (1 − Π(z+d_k)) "
        "keeps them, and since |Π(z+d_k)| < 1 on the window its sign is sign(P_p^Z P_n^N). "
        "Split-braid multiplicativity is not proved here (bean qou-5zl1)."))
    w.add_data("adoption", "none — exploratory, not wired")
    w.add_data("checks", checks)
    for c in checks:
        w.add_assertion(name=c["name"], computed="1" if c["passed"] else "0",
                        expected="1", tolerance="0", source=c["detail"] or None)
    out = w.save()
    print(f"Witness: {out}  ({time.monotonic() - t0:.1f}s)")
    return 0 if all(c["passed"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
