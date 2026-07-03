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
default at A ≤ 3 (n ≤ 9, instant). ⁴He (n = 12, d_max = 7700, ~1 GB peak,
minutes) is opt-in via --with-4he.

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

import numpy as np  # noqa: E402
import scipy.sparse as sps  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from hecke.hecke_characters import build_seminormal_matrices, partitions_of  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

HERE = Path(__file__).resolve().parent

ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1)]
ISO_4HE = ("4He", 2, 2)


def _letters(word, dim, sigmas):
    """Materialise the word's letters c·σ_g + d·1 as matrices for one λ."""
    eye = sps.identity(dim, format="csr") if sigmas and sps.issparse(sigmas[0]) \
        else np.eye(dim)
    out = []
    for c, d, g in word:
        sig = sigmas[g]
        out.append(c * sig + d * eye)
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
        # bar-parity split of G: rerun the whole pipeline at q₀⁻¹ through the
        # q-parameterised path. NB the q-explicit word uses the proven leading
        # flavor split (not the baked canonical δ), so both bar legs use the
        # SAME q-explicit path for internal consistency.
        qbar = {}
        if args.qbar:
            import mpmath as _mp
            q0m = _mp.mpf(str(Q0))
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
