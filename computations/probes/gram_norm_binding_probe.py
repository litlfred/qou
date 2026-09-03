#!/usr/bin/env python3
"""Probe: operator-space Gram norm G(W) = tr_M(W · W^♯) vs binding residuals.

EXPLORATORY (no production rewire, no fit). Motivation — session discussion
2026-07-03 on q-bar-type norms: the bar involution's ±1 eigenspaces are the
bar-even (binding / meson) and bar-odd (Q_β / lepton) channels, and any
pairing making the involution self-adjoint renders them orthogonal
(`prop:hecke-baer-star-generic`). The OBSERVABLE-level bar norm
‖tr_M‖ = √(tr(q₀)·tr(q₀⁻¹)) already exists (`tr_m_atom_via_transfer.
tr_m_bar_norm`). What did NOT exist is the OPERATOR-space pairing
diagnostic: the Frobenius/Markov Gram norm of the atom word itself,

    G(W) = tr_M(W · W^♯) = Σ_λ y_λ(q₀) · tr(ρ_λ(W) ρ_λ(W^♯)),

with ♯ the reversal anti-involution (fixes q and each letter c·σ_g + d·1,
reverses the word). Unlike the trivial bar-conjugate product W·W̄ = W·W⁻¹ = 1
(which erases all knot data), W·W^♯ is a genuine quadratic invariant: it is
the length² of W under the Frobenius pairing whose Gram matrix is
INDEFINITE at q₀ (`frobenius_gram_matrix_probe`), so G carries cross-channel
(off-diagonal) information that the linear trace tr_M(W) does not.

Question probed: does the Gram-norm binding

    B_gram = (α/2) · ln(G_free / G_atom)        (α = E₀; /2: G is quadratic)

track B_AME differently from the production B_sym = α·ln(tr_free/tr_atom)?
The per-isotope ratio r = B_gram / B_sym measures the cross-channel
asymmetry of the bound word: r ≡ 1 iff the Gram norm adds nothing beyond
the linear trace (channel-diagonal dominance); r ≠ 1 quantifies the
operator-space cross term that the 1-D observable projection drops.

PRECISION: float64 throughout (LOSSY — `hecke.hecke_characters.
build_seminormal_matrices` is a float64/scipy path). Adequate for the
%-level residual comparison this probe makes; NOT a production number.
Cross-checks: (1) the probe's linear trace Σ y_λ tr(ρ_λ(W)) is compared
per isotope against the 50-dps `tr_m_atom_zn` transfer value (expected
agreement ~1e-9 rel, float64 floor); (2) reversal invariance of the
LINEAR trace, tr_M(W^♯) = tr_M(W) (character symmetry χ^λ(T_{w⁻¹}) =
χ^λ(T_w)), is verified empirically — note this does NOT make G trivial:
the QUADRATIC tr_M(W·W^♯) ≠ tr_M(W)² in general.

Feasibility: dense/sparse seminormal per λ ⊢ 3A; Σ_λ d_λ² = (3A)! caps the
default at A ≤ 3. Measured 2026-08-25: ²H 0.02 s, ³H 0.45 s, ³He 0.42 s;
⁴He (n = 12, d_max = 7700, ~1.8 GB peak) 418 s, opt-in via --with-4he.
NB those figures hold only with the float coercion in `_letters` — without it
an mpf word coefficient promotes every letter to dtype=object and ³H alone runs
for hours (see that function's docstring, and bean qou-9ohz).

Emits `gram-norm-binding-probe.witness.json` (audit-only).

Usage:
    python3 -u probes/gram_norm_binding_probe.py 2>&1 | tee /tmp/gram_norm_probe.log
    python3 -u probes/gram_norm_binding_probe.py --with-4he 2>&1 | tee /tmp/gram_norm_probe.log
"""
from __future__ import annotations

# Path bridge (probes/ cluster subdirectory — flat-namespace imports).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import scipy.sparse as sps  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from hecke.hecke_characters import (  # noqa: E402
    build_seminormal_matrices, build_seminormal_matrices_mp, partitions_of)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as Q_50_STR  # noqa: E402

HERE = Path(__file__).resolve().parent

ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1)]
ISO_4HE = ("4He", 2, 2)


def _letters(word, dim, sigmas):
    """Materialise the word's letters c·σ_g + d·1 as matrices for one λ.

    The coefficients (c, d) arrive from `atom_braid_word_3A` as a mix of
    `int` and `mpmath.mpf`; the seminormal σ are float64 (see the module
    PRECISION note). An mpf scalar times a float64 array yields a
    **dtype=object** array, and object dtype then propagates through every
    subsequent `@` in `_word_products`, running the whole matmul chain at
    Python speed. Measured on λ=(4,3,1,1), d=216: one matmul costs 0.74 ms
    in float64 and 13270 ms in object dtype — a factor of 1.8e4. Since the
    σ operand is *already* float64-truncated, the mpf carries no information
    the product can keep (verified at ²H: object vs coerced agree to 9e-16,
    the float64 floor), so coercing here loses nothing and is what makes
    ³H and beyond feasible at all.
    """
    eye = sps.identity(dim, format="csr") if sigmas and sps.issparse(sigmas[0]) \
        else np.eye(dim)
    out = []
    for c, d, g in word:
        sig = sigmas[g]
        out.append(float(c) * sig + float(d) * eye)
    return out


def _rmul(M: np.ndarray, L) -> np.ndarray:
    """M @ L for dense M and dense-or-sparse L (sparse dispatches via
    __rmatmul__; np.asarray normalises the np.matrix return of spmatrix)."""
    return np.asarray(M @ L)


def _word_products(word, dim, sigmas):
    """(ρ(W), ρ(W^♯)) — forward and reversed letter products (dense)."""
    letters = _letters(word, dim, sigmas)
    fwd = np.eye(dim)
    rev = np.eye(dim)
    for L in letters:
        fwd = _rmul(fwd, L)
    for L in reversed(letters):
        rev = _rmul(rev, L)
    return fwd, rev


def _letters_mp(word, dim, sigmas):
    """Exact twin of `_letters`: mp.matrix letters, mpf coefficients KEPT.

    The float coercion in `_letters` is sound only because the float64 builder
    has already truncated sigma. On this path `build_seminormal_matrices_mp`
    returns exact `mp.matrix`, so the word's mpf coefficients are the whole
    point and are carried through untouched."""
    eye = mp.eye(dim)
    out = []
    for c, d, g in word:
        cm = c if isinstance(c, mp.mpf) else mp.mpf(str(c))
        dm = d if isinstance(d, mp.mpf) else mp.mpf(str(d))
        out.append(cm * sigmas[g] + dm * eye)
    return out


def _gram_and_trace_mp(word, n, y_mp, q):
    """(G, T) at full working precision — the exact route through
    `build_seminormal_matrices_mp`. No float64 anywhere in the chain.

    Cost is measured, not extrapolated: 2H (d <= 16) completes in ~2 s; a 3H
    (d <= 216) run exceeded 30 min without finishing. The per-matmul ratio
    (29x at d=16, 561x at d=216) is a LOWER BOUND on the aggregate ratio and
    must not be multiplied into a whole-pipeline float64 time — the float64
    path gets a speedup on the large blocks that this path cannot use."""
    G = mp.mpf(0)
    T = mp.mpf(0)
    for lam in partitions_of(n):
        sigmas, dim = build_seminormal_matrices_mp(lam, q)[:2]
        if dim == 0:
            continue
        letters = _letters_mp(word, dim, sigmas)
        fwd = mp.eye(dim)
        rev = mp.eye(dim)
        for L in letters:
            fwd = fwd * L
        for L in reversed(letters):
            rev = rev * L
        # tr(fwd . rev) without materialising the product
        chi_sharp = mp.fsum(fwd[i, j] * rev[j, i]
                            for i in range(dim) for j in range(dim))
        chi = mp.fsum(fwd[i, i] for i in range(dim))
        yl = y_mp[tuple(lam)]
        G += yl * chi_sharp
        T += yl * chi
    return G, T


def _y_lambda_exact(n, q):
    """y_λ(q) at full precision, from the SYMBOLIC weights.

    `y_lambda_at(n, q_val=...)` evaluates in float; passing `q_val=None`
    returns sympy expressions in q, which is the only exact source available.
    Substituting at mp.mp.dps and re-parsing keeps the whole chain off f64."""
    dps = mp.mp.dps
    ysym = y_lambda_at(n, q_val=None)
    qsym = None
    for v in ysym.values():
        if hasattr(v, "free_symbols") and v.free_symbols:
            qsym = next(iter(v.free_symbols))
            break
    out = {}
    for lam, e in ysym.items():
        if qsym is None or not getattr(e, "free_symbols", None):
            out[tuple(lam)] = mp.mpf(str(sp.N(e, dps + 5)))
        else:
            out[tuple(lam)] = mp.mpf(
                str(sp.N(e.subs(qsym, sp.Float(str(q), dps + 5)), dps + 5)))
    return out


def _conj(lam):
    """Conjugate partition λ′."""
    lam = tuple(lam)
    return tuple(sum(1 for row in lam if row > j) for j in range(lam[0]))


def _gram_and_trace(word, n, y, q=None):
    """(G, T, T_rev, per_lam): the aggregates Σ y_λ tr(ρWρW^♯) /
    Σ y_λ tr(ρW) / Σ y_λ tr(ρW^♯), plus the per-λ contribution map
    {λ: c_λ = y_λ·tr(ρ_λ(W)ρ_λ(W^♯))} for the block-decomposition
    analysis. `q=None` uses the module-default substrate q₀."""
    G = T = Trev = 0.0
    per_lam = {}
    t0 = time.time()
    for lam in partitions_of(n):
        res = build_seminormal_matrices(lam, q=q)
        sigmas, dim = res[0], res[1]
        if dim == 0:
            continue
        fwd, rev = _word_products(word, dim, sigmas)
        chi_sharp = float(np.einsum("ij,ji->", fwd, rev))
        chi = float(np.trace(fwd))
        chi_rev = float(np.trace(rev))
        yl = float(y[tuple(lam)])
        G += yl * chi_sharp
        T += yl * chi
        Trev += yl * chi_rev
        per_lam[tuple(lam)] = yl * chi_sharp
        if dim > 500:
            print(f"      λ={tuple(lam)} d={dim} done "
                  f"({time.time()-t0:.1f}s elapsed)", flush=True)
    return G, T, Trev, per_lam


def _stratum_stats(per_lam, G):
    """(self-conjugate share of G, chiral-pair antisymmetry share of G).

    Bar sends e_λ ↦ e_λ′ (`prop:hecke-baer-star-generic`), so the
    self-conjugate blocks are the bar-fixed stratum; the antisymmetric
    combination ½|c_λ − c_λ′| over chiral pairs is the block-level
    bar-odd content of the Gram norm at fixed q."""
    if G == 0.0:
        return None, None
    sc = sum(c for lam, c in per_lam.items() if _conj(lam) == lam)
    seen, anti = set(), 0.0
    for lam, c in per_lam.items():
        lc = _conj(lam)
        if lc == lam or lam in seen:
            continue
        seen.add(lc)
        anti += abs(c - per_lam.get(lc, 0.0)) / 2.0
    return sc / G, anti / abs(G)


def _ame_and_alpha():
    from mass_binding_dashboard import _ame_table, _constants
    me, q0, alpha = _constants()
    return _ame_table(), alpha


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--with-4he", action="store_true",
                    help="include ⁴He (n=12, d_max=7700; ~1 GB peak, minutes)")
    ap.add_argument("--exact", action="store_true",
                    help="ALSO run the exact (mpmath) route via "
                         "build_seminormal_matrices_mp and report whether the "
                         "float64 verdict survives. Additive: the float64 "
                         "numbers above are unchanged. COST, measured not "
                         "extrapolated: 2H (d<=16) ~2 s; 3H/3He (d<=216) "
                         "exceeded 30 min WITHOUT finishing and are unmeasured; "
                         "4He (d=7700) is out of reach and is not run.")
    ap.add_argument("--exact-dps", type=int, default=50,
                    help="working precision for --exact (default 50)")
    ap.add_argument("--qbar", action="store_true",
                    help="also evaluate G at q₀⁻¹ (q-parameterised word/y/ρ) "
                         "and report the bar-parity even/odd split of G")
    args = ap.parse_args()
    isotopes = ISOTOPES + ([ISO_4HE] if args.with_4he else [])

    ame, alpha = _ame_and_alpha()
    rows = []
    max_xcheck = 0.0
    max_revres = 0.0
    for name, Z, N in isotopes:
        n = 3 * (Z + N)
        t0 = time.time()
        print(f"  {name}: n={n} …", flush=True)
        y = y_lambda_at(n, q_val=float(Q0))
        w_atom = atom_braid_word_3A(Z, N, include_inter=True)
        w_free = atom_braid_word_3A(Z, N, include_inter=False)
        Ga, Ta, Ta_rev, pl_a = _gram_and_trace(w_atom, n, y)
        Gf, Tf, Tf_rev, pl_f = _gram_and_trace(w_free, n, y)
        # per-λ redistribution: which blocks receive amplitude under binding
        sc_a, anti_a = _stratum_stats(pl_a, Ga)
        sc_f, anti_f = _stratum_stats(pl_f, Gf)
        delta = {lam: pl_a[lam] - pl_f.get(lam, 0.0) for lam in pl_a}
        top_recv = sorted(delta.items(), key=lambda kv: -abs(kv[1]))[:3]
        # redistribution aggregates (the w_n(K)-carrier cross-link, 2026-07-04):
        # R_abs = ½·‖Δc‖₁ over the signed per-λ decomposition (NB: G is
        # indefinite, so this is an ℓ¹ redistribution size, not a probability
        # TV distance) — derived, isospin-aware, and (unlike the hyperbolic
        # sub-link volume, Hopf Vol=0) NONZERO for the deuteron.
        R_abs = 0.5 * sum(abs(d) for d in delta.values())
        R_signed = sum(delta.values())            # = G_atom − G_free
        # chiral-antisymmetric part of the redistribution (block-level bar-odd)
        seen_p, R_anti = set(), 0.0
        for lam, d in delta.items():
            lc = _conj(lam)
            if lc == lam or lam in seen_p:
                continue
            seen_p.add(lc)
            R_anti += abs(d - delta.get(lc, 0.0)) / 2.0
        # bar-parity split of G: rerun the whole pipeline at q₀⁻¹ through the
        # q-parameterised path. NB the q-explicit word uses the proven leading
        # flavor split (not the baked canonical δ), so both bar legs use the
        # SAME q-explicit path for internal consistency.
        qbar = {}
        if args.qbar:
            import mpmath as _mp
            from q_parameter import Q_50_DIGIT_STR as _Q50
            # 50-dps source; the f64 `Q` is rejected by the word builder.
            q0m = _mp.mpf(str(_Q50))
            legs = {}
            for tag, qv in (("q0", q0m), ("qi", 1 / q0m)):
                yq = y_lambda_at(n, q_val=float(qv))
                wa = atom_braid_word_3A(Z, N, include_inter=True, q=qv)
                wf = atom_braid_word_3A(Z, N, include_inter=False, q=qv)
                Gaq = _gram_and_trace(wa, n, yq, q=float(qv))[0]
                Gfq = _gram_and_trace(wf, n, yq, q=float(qv))[0]
                legs[tag] = (Gaq, Gfq)
            (Ga0, Gf0), (Gai, Gfi) = legs["q0"], legs["qi"]
            qbar = {
                "G_atom_even": (Ga0 + Gai) / 2, "G_atom_odd": (Ga0 - Gai) / 2,
                "G_free_even": (Gf0 + Gfi) / 2, "G_free_odd": (Gf0 - Gfi) / 2,
            }
            qbar["odd_frac_atom"] = (abs(qbar["G_atom_odd"] / qbar["G_atom_even"])
                                     if qbar["G_atom_even"] != 0.0 else None)
            qbar["odd_frac_free"] = (abs(qbar["G_free_odd"] / qbar["G_free_even"])
                                     if qbar["G_free_even"] != 0.0 else None)
        # cross-check the linear trace against the 50-dps transfer engine
        ta50, tf50, _, _ = tr_m_atom_zn(Z, N, dps=50)
        xa = abs(Ta - float(ta50)) / abs(float(ta50))
        xf = abs(Tf - float(tf50)) / abs(float(tf50))
        max_xcheck = max(max_xcheck, xa, xf)
        # reversal invariance of the LINEAR trace (character symmetry)
        rr = max(abs(Ta - Ta_rev) / max(abs(Ta), 1e-300),
                 abs(Tf - Tf_rev) / max(abs(Tf), 1e-300))
        max_revres = max(max_revres, rr)
        B_sym = alpha * math.log(Tf / Ta)
        B_gram = (0.5 * alpha * math.log(Gf / Ga)
                  if (Gf > 0 and Ga > 0) else None)
        bame = ame.get((Z, Z + N), (None,))[0]
        rows.append({
            "iso": name, "n": n,
            "G_atom": Ga, "G_free": Gf, "tr_atom": Ta, "tr_free": Tf,
            "gram_over_tr2_atom": Ga / (Ta * Ta) if Ta != 0.0 else None,
            "gram_over_tr2_free": Gf / (Tf * Tf) if Tf != 0.0 else None,
            "B_sym": B_sym, "B_gram": B_gram,
            "r_gram_sym": (B_gram / B_sym
                           if (B_gram is not None and B_sym != 0.0) else None),
            "B_AME": bame,
            "err_sym": (bame / B_sym
                        if (bame is not None and B_sym != 0.0) else None),
            "err_gram": (bame / B_gram
                         if (bame is not None and B_gram is not None
                             and B_gram != 0.0) else None),
            "selfconj_share_atom": sc_a, "selfconj_share_free": sc_f,
            "chiral_anti_share_atom": anti_a, "chiral_anti_share_free": anti_f,
            "top_receivers": [{"lam": list(lam), "delta_c": dc}
                              for lam, dc in top_recv],
            "R_abs": R_abs, "R_signed": R_signed, "R_anti": R_anti,
            "delta_c_full": [{"lam": list(lam), "delta": d}
                             for lam, d in sorted(delta.items(),
                                                  key=lambda kv: -abs(kv[1]))],
            "qbar": qbar,
            "wall_sec": round(time.time() - t0, 2),
        })
        print(f"      G_atom={Ga:.6f} G_free={Gf:.6f} "
              f"B_gram={B_gram if B_gram is None else round(B_gram, 4)} "
              f"B_sym={B_sym:.4f} ({time.time()-t0:.1f}s)", flush=True)

    print("\n| iso | B_AME | B_sym | err sym | B_gram | err gram | "
          "B_gram/B_sym | G/tr² atom | G/tr² free |")
    print("|---|--:|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        def f(v, p=3):
            return f"{v:.{p}f}" if v is not None else "—"
        print(f"| {r['iso']} | {f(r['B_AME'],2)} | {f(r['B_sym'])} "
              f"| {f(r['err_sym'],2)} | {f(r['B_gram'])} | {f(r['err_gram'],2)} "
              f"| {f(r['r_gram_sym'],4)} | {f(r['gram_over_tr2_atom'],6)} "
              f"| {f(r['gram_over_tr2_free'],6)} |")

    print("\n| iso | selfconj share atom | selfconj share free "
          "| chiral-anti share atom | chiral-anti share free | top Δc_λ receivers |")
    print("|---|--:|--:|--:|--:|:--|")
    for r in rows:
        def f2(v):
            return f"{v:.4f}" if v is not None else "—"
        tops = "; ".join(f"{tuple(t['lam'])}: {t['delta_c']:+.4f}"
                         for t in r["top_receivers"])
        print(f"| {r['iso']} | {f2(r['selfconj_share_atom'])} "
              f"| {f2(r['selfconj_share_free'])} "
              f"| {f2(r['chiral_anti_share_atom'])} "
              f"| {f2(r['chiral_anti_share_free'])} | {tops} |")

    print("\n| iso | B_AME | R_abs | R_anti | R_signed | α·R_abs (MeV) |")
    print("|---|--:|--:|--:|--:|--:|")
    for r in rows:
        print(f"| {r['iso']} | {r['B_AME'] if r['B_AME'] is not None else '—'} "
              f"| {r['R_abs']:.4f} | {r['R_anti']:.4f} | {r['R_signed']:+.4f} "
              f"| {alpha * r['R_abs']:.3f} |")

    if args.exact:
        mp.mp.dps = args.exact_dps
        q_ex = mp.mpf(str(Q_50_STR))
        print(f"\n### EXACT route ({args.exact_dps} dps, "
              f"build_seminormal_matrices_mp — no float64 in the chain)")
        print("\n| iso | n | r=B_gram/B_sym (float64) | r (exact) | rel diff "
              "| G_atom (exact) | tr_atom (exact) |")
        print("|---|--:|--:|--:|--:|--:|--:|")
        for name, Z, N in ISOTOPES:
            n = 3 * (Z + N)
            row = next(r for r in rows if r["iso"] == name)
            t0 = time.time()
            y_ex = _y_lambda_exact(n, q_ex)
            wa = atom_braid_word_3A(Z, N, include_inter=True)
            wf = atom_braid_word_3A(Z, N, include_inter=False)
            Ga, Ta = _gram_and_trace_mp(wa, n, y_ex, q_ex)
            Gf, Tf = _gram_and_trace_mp(wf, n, y_ex, q_ex)
            # alpha CANCELS in r, so the verdict ratio needs no calibration input:
            #   r = ln(G_free/G_atom) / (2 * ln(tr_free/tr_atom))
            r_ex = (mp.log(Gf / Ga) / (2 * mp.log(Tf / Ta))
                    if (Gf > 0 and Ga > 0 and Ta != 0 and Tf != 0) else None)
            r_f64 = row["r_gram_sym"]
            rel = (abs(float(r_ex) - r_f64) / abs(r_f64)
                   if (r_ex is not None and r_f64) else None)
            print(f"| {name} | {n} | {r_f64:.10f} | {mp.nstr(r_ex, 12)} "
                  f"| {rel:.2e} | {mp.nstr(Ga, 12)} | {mp.nstr(Ta, 12)} |")
            print(f"      ({time.time() - t0:.1f}s)", flush=True)
        print("\n4He is NOT run exactly (d_max = 7700). NB the per-matmul "
              "ratio (561x at d=216) is a LOWER BOUND on the aggregate ratio, "
              "not an estimate of it: the float64 path gets a large speedup on "
              "the big blocks that the mpmath path cannot use, so multiplying a "
              "whole-pipeline float64 time by it understates the cost — "
              "measured, by at least an order of magnitude at 3H.")

    if args.qbar:
        print("\n| iso | G_even atom | G_odd atom | odd/even atom "
              "| G_even free | G_odd free | odd/even free |")
        print("|---|--:|--:|--:|--:|--:|--:|")
        for r in rows:
            qb = r["qbar"]
            if not qb:
                continue
            def f3(v):
                return f"{v:.6f}" if v is not None else "—"
            print(f"| {r['iso']} | {f3(qb['G_atom_even'])} "
                  f"| {f3(qb['G_atom_odd'])} | {f3(qb['odd_frac_atom'])} "
                  f"| {f3(qb['G_free_even'])} | {f3(qb['G_free_odd'])} "
                  f"| {f3(qb['odd_frac_free'])} |")

    builder = WitnessBuilder("gram-norm-binding-probe", engine="python")
    builder.set_description(
        "Exploratory operator-space Gram norm G(W)=tr_M(W·W^♯) vs binding "
        "residuals (q-bar / Baer-* norm discussion, 2026-07-03).")
    builder.add_parameter("q0", float(Q0))
    builder.add_parameter("alpha_MeV", alpha)
    builder.add_parameter("precision", "float64 (LOSSY, exploratory)")
    builder.add_parameter("isotopes", [r["iso"] for r in rows])
    builder.add_parameter(
        "sharp_involution",
        "word reversal; fixes q and each letter c·σ_g + d·1")
    builder.add_data("rows", rows)
    builder.add_assertion(
        name="linear_trace_matches_transfer_engine",
        computed=max_xcheck, expected=0.0, tolerance=1e-8,
        unit="max rel diff of Σ y_λ tr(ρ_λ(W)) vs 50-dps tr_m_atom_zn",
        source="float64 seminormal path vs canonical transfer (validation).",
    )
    builder.add_assertion(
        name="linear_trace_reversal_invariant",
        computed=max_revres, expected=0.0, tolerance=1e-10,
        unit="max rel |tr_M(W^♯) − tr_M(W)|",
        source="character symmetry χ^λ(T_{w⁻¹}) = χ^λ(T_w); the QUADRATIC "
               "Gram norm tr_M(W·W^♯) is the non-trivial diagnostic.",
    )
    builder.set_audit_only("docs/audits/2026-07-03-qbar-norm-repitch-assessment.md")
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
