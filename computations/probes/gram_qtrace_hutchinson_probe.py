#!/usr/bin/env python3
"""Probe: stochastic (Hutchinson) quadratic trace tr_M(W·W^♯) beyond n = 12 —
the A = 5 mirror pair ⁵He/⁵Li at the Gram level.

EXPLORATORY (no production rewire, no fit). The dense seminormal sweep
(`gram_norm_binding_probe.py`) caps at n = 3A = 12 (d_max(S₁₂) = 7700), so
³H/³He was the only mirror pair testable at the QUADRATIC (operator-space
Gram) level — where the bar-parity antisymmetry lives; the linear trace
cannot see it (`mirror_parity_linear_trace_probe.py`, refuted transfer).

This probe removes the cap for the *trace* (not the matrix): per block λ,

    χ♯_λ = tr(ρ_λ(W)·ρ_λ(W^♯))

is estimated by the Hutchinson identity tr(F·R) = E_z[(Fᵀz)·(Rz)] with
Rademacher z, needing only sparse letter mat-VEC products (Hoefsmit
generators have ≤ 2 nonzeros/row), never the dense d×d product. Blocks with
d ≤ --exact-dim (default 3000) are computed exactly (dense, cheap); larger
blocks are estimated with --samples Rademacher vectors and a per-block
standard-error estimate is propagated to the aggregate. This reaches
n = 15 (d_max(S₁₅) = 292 864, vectors ~2.3 MB) comfortably.

Validation: at n = 9 (³H/³He) the estimator (forced stochastic,
--exact-dim 0) is compared against the exact dense sweep — agreement
within the propagated stochastic error is asserted.

Question probed: does the A = 5 mirror pair (⁵He Z=2,N=3 / ⁵Li Z=3,N=2)
split ANTISYMMETRICALLY in bar-parity loading under binding, as ³H/³He did
at n = 9 (Gram level)? Both legs (q₀, q₀⁻¹) run through the q-parameterised
path, as in the dense probe.

PRECISION: float64 + stochastic error (doubly LOSSY, exploratory) —
adequate for the ~20% parity-shift effects under test; NOT a production
number. Per-block exact/stochastic status is recorded in the witness.

Emits `gram-qtrace-hutchinson-probe.witness.json` (audit-only).

Usage:
    python3 -u probes/gram_qtrace_hutchinson_probe.py --validate 2>&1 | tee /tmp/qtrace_val.log
    python3 -u probes/gram_qtrace_hutchinson_probe.py 2>&1 | tee /tmp/qtrace_a5.log
"""
from __future__ import annotations

# Path bridge (probes/ cluster subdirectory — flat-namespace imports).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import scipy.sparse as sps  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from hecke.hecke_characters import build_seminormal_matrices, partitions_of  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from gram_norm_binding_probe import _letters  # noqa: E402

RNG = np.random.default_rng(20260704)   # fixed seed: reproducible witness


def _apply(letters, z):
    """(L_k ··· L_1) z — apply letters right-to-left (L_1 first)."""
    v = z
    for L in letters:
        v = L @ v
    return v


def _apply_T(letters, z):
    """(L_1 ··· L_k)ᵀ z = L_kᵀ ··· L_1ᵀ z — apply transposed, L_1ᵀ first."""
    v = z
    for L in letters:
        v = L.T @ v
    return v


def _chi_sharp_from_letters(letters, dim, exact_dim, samples):
    """(χ♯, stderr, mode) given materialised letters for one block.

    F = ρ(W) = L_1···L_k, R = ρ(W^♯) = L_k···L_1. Exact: dense products.
    Stochastic: tr(F·R) = E_z[(Fᵀz)·(Rz)], z Rademacher — vectorised over
    a d×m block of z's per pass (sparse @ dense-matrix, chunked ≤ 64
    columns to bound memory at d ~ 3·10⁵).
    """
    if dim <= exact_dim:
        fwd = np.eye(dim)
        rev = np.eye(dim)
        for L in letters:
            fwd = np.asarray(fwd @ L)
        for L in reversed(letters):
            rev = np.asarray(rev @ L)
        return float(np.einsum("ij,ji->", fwd, rev)), 0.0, "exact"
    ests = np.empty(samples)
    done = 0
    while done < samples:
        m = min(64, samples - done)
        Z = 2.0 * RNG.integers(0, 2, size=(dim, m)) - 1.0   # Rademacher (fast)
        U = _apply_T(letters, Z)                    # Fᵀ Z (L_1ᵀ first)
        V = _apply(letters, Z)                      # R Z (L_1 first)
        ests[done:done + m] = np.einsum("im,im->m", U, V)
        done += m
    mean = float(ests.mean())
    stderr = float(ests.std(ddof=1) / math.sqrt(samples)) if samples > 1 else 0.0
    return mean, stderr, f"hutchinson({samples})"


def gram_qtrace_multi(words, n, y, *, q, exact_dim, samples, label=""):
    """[(G, stderr_G)] per word in `words` — Σ_λ y_λ·χ♯_λ with propagated
    stochastic error. The per-λ representation is built ONCE and shared
    across all words (the dominant cost at n = 15 is SYT/matrix
    construction, not the sampling)."""
    G = [0.0] * len(words)
    var = [0.0] * len(words)
    t0 = time.time()
    for lam in partitions_of(n):
        res = build_seminormal_matrices(lam, q=q)
        sigmas, dim = res[0], res[1]
        if dim == 0:
            continue
        yl = float(y[tuple(lam)])
        mode = ""
        for i, word in enumerate(words):
            letters = _letters(word, dim, sigmas)
            chi, se, mode = _chi_sharp_from_letters(
                letters, dim, exact_dim, samples)
            G[i] += yl * chi
            var[i] += (yl * se) ** 2
        if dim > 20000:
            print(f"      {label} λ={tuple(lam)} d={dim} [{mode}] "
                  f"({time.time()-t0:.0f}s)", flush=True)
    return [(g, math.sqrt(v)) for g, v in zip(G, var)]


def gram_qtrace(word, n, y, *, q, exact_dim, samples, label=""):
    """Single-word wrapper (kept for the --validate path)."""
    return gram_qtrace_multi([word], n, y, q=q, exact_dim=exact_dim,
                             samples=samples, label=label)[0]


def _parity(g0, gi):
    den = g0 + gi
    return (g0 - gi) / den if den != 0 else None


def run_isotope(name, Z, N, *, exact_dim, samples):
    import mpmath as mp
    n = 3 * (Z + N)
    q0 = mp.mpf(str(Q0))
    out = {"iso": name, "Z": Z, "N": N, "n": n}
    for tag, qv in (("q0", q0), ("qi", 1 / q0)):
        y = y_lambda_at(n, q_val=float(qv))
        wa = atom_braid_word_3A(Z, N, include_inter=True, q=qv)
        wf = atom_braid_word_3A(Z, N, include_inter=False, q=qv)
        (Ga, sa), (Gf, sf) = gram_qtrace_multi(
            [wa, wf], n, y, q=float(qv), exact_dim=exact_dim,
            samples=samples, label=f"{name}:{tag}")
        out[f"G_atom_{tag}"], out[f"se_atom_{tag}"] = Ga, sa
        out[f"G_free_{tag}"], out[f"se_free_{tag}"] = Gf, sf
    out["parity_atom"] = _parity(out["G_atom_q0"], out["G_atom_qi"])
    out["parity_free"] = _parity(out["G_free_q0"], out["G_free_qi"])
    out["delta_parity"] = (out["parity_atom"] - out["parity_free"]
                           if None not in (out["parity_atom"], out["parity_free"])
                           else None)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=200)
    ap.add_argument("--exact-dim", type=int, default=3000,
                    help="blocks with d <= this are computed exactly")
    ap.add_argument("--validate", action="store_true",
                    help="n=9 estimator-vs-exact validation only")
    args = ap.parse_args()

    builder = WitnessBuilder("gram-qtrace-hutchinson-probe", engine="python")
    builder.set_description(
        "Stochastic Hutchinson quadratic trace tr_M(W·W^sharp) beyond n=12: "
        "A=5 mirror pair bar-parity split (Gram level).")
    builder.add_parameter("q0", float(Q0))
    builder.add_parameter("samples", args.samples)
    builder.add_parameter("exact_dim", args.exact_dim)
    builder.add_parameter("rng_seed", 20260704)
    builder.add_parameter("precision", "float64 + stochastic (LOSSY, exploratory)")

    if args.validate:
        # n=9: force-stochastic vs exact on the same words/legs.
        import mpmath as mp
        q0 = float(mp.mpf(str(Q0)))
        y = y_lambda_at(9, q_val=q0)
        w = atom_braid_word_3A(2, 1, include_inter=True, q=mp.mpf(str(Q0)))
        Ge, _ = gram_qtrace(w, 9, y, q=q0, exact_dim=10**9, samples=1)
        Gs, se = gram_qtrace(w, 9, y, q=q0, exact_dim=0, samples=args.samples)
        z = abs(Gs - Ge) / se if se > 0 else 0.0
        print(f"  validation n=9 (3He atom): exact={Ge:.6f} "
              f"stochastic={Gs:.6f} ± {se:.6f}  (z={z:.2f})")
        builder.add_data("validation", {"exact": Ge, "stochastic": Gs,
                                        "stderr": se, "z": z})
        builder.add_assertion(
            name="hutchinson_matches_exact_3sigma",
            computed=z, expected=0.0, tolerance=3.0,
            unit="z-score |stochastic − exact| / stderr (n=9 ³He atom word)",
            source="Hutchinson estimator validation vs dense sweep.")
        builder.set_audit_only(
            "docs/audits/2026-07-03-qbar-norm-repitch-assessment.md")
        out = builder.save()
        print(f"\nWitness: {out}")
        return 0

    rows = [run_isotope("5He", 2, 3, exact_dim=args.exact_dim,
                        samples=args.samples),
            run_isotope("5Li", 3, 2, exact_dim=args.exact_dim,
                        samples=args.samples)]
    print("\n| iso | parity atom | parity free | Δ parity (binding) |")
    print("|---|--:|--:|--:|")
    def _f(v):
        return f"{v:+.6f}" if v is not None else "—"
    for r in rows:
        print(f"| {r['iso']} | {_f(r['parity_atom'])} "
              f"| {_f(r['parity_free'])} | {_f(r['delta_parity'])} |")
    dp0, dp1 = rows[0]["delta_parity"], rows[1]["delta_parity"]
    opposite = (dp0 * dp1 < 0) if (dp0 is not None and dp1 is not None) else False
    print(f"\n  A=5 mirror pair Δ-parity signs: "
          f"{'OPPOSITE (antisymmetric split)' if opposite else 'same sign'}")
    builder.add_data("rows", rows)
    builder.add_data("a5_mirror_opposite_signed", bool(opposite))
    builder.add_assertion(
        name="both_isotopes_computed",
        computed=float(sum(1 for r in rows if r["delta_parity"] is not None)),
        expected=2.0, tolerance=0.0,
        unit="isotopes with finite parity data (compute validity)",
        source="A=5 mirror pair at n=15 via Hutchinson quadratic trace.")
    builder.set_audit_only(
        "docs/audits/2026-07-03-qbar-norm-repitch-assessment.md")
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
