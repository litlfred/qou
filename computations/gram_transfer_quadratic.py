#!/usr/bin/env python3
"""gram_transfer_quadratic — EXACT, d_λ-free "doubled-Bratteli" transfer for the
QUADRATIC Markov/Frobenius Gram norm of the atom braid word,

    G(W) = tr_M(W · W^♯) = Σ_λ y_λ(q) · tr(ρ_λ(W) ρ_λ(W^♯))
                         = Σ_λ y_λ(q) · ‖ρ_λ(W)‖_F² ,

clearing the dense n = 12 (⁴He) wall that `probes/gram_norm_binding_probe.py`
hits (Σ_λ d_λ² = (3A)! ; d_max = 7700 at n = 12, ~1 GB / minutes; infeasible
at n ≥ 15). This is the EXACT (mpmath 50-dps) drop-in replacement for that
float64 dense probe — same word, same ♯ convention, same aggregates — computed
by a transfer matrix over PAIRS of fine-Bratteli edges, never materialising
d_λ.

EXPLORATORY / AUDIT-ONLY. No production consumer, no fit. `set_audit_only`
points at the q-bar-norm re-pitch assessment
(`docs/audits/2026-07-03-qbar-norm-repitch-assessment.md`) whose diagnostic
this compute makes scalable.

──────────────────────────────────────────────────────────────────────────────
Construction (the whole point — an EXACT method that provably matches dense).

♯ is the reversal anti-involution (reverse letter order; fix q and each letter
c·σ_g + d·1), per `probes/gram_norm_binding_probe.py::_word_products` /
`sharp_involution`. Every seminormal (Hoefsmit) letter matrix c·σ_g + d·1 is
SYMMETRIC, so ρ_λ(W^♯) = ρ_λ(W)^T and

    tr(ρ_λ(W) ρ_λ(W^♯)) = tr(ρ_λ(W) ρ_λ(W)^T) = Σ_{S,T} ρ_λ(W)_{ST}² = ‖ρ_λ(W)‖_F².

The linear χ-transfer (`chi_monotone_transfer.chi_all_lambda`) tracks ONE
Bratteli chain and keeps only the DIAGONAL block of each O_g, because the
character trace forces every level back to its start. The Frobenius norm sums
over ALL matrix entries ρ(W)_{ST}, so the off-diagonal seminormal entry — the
term the linear transfer drops — matters. For a MONOTONE atom word each O_g =
Π_j(σ_g + d_j·1) is a polynomial in σ_g alone, acting on level g+1 only. A
matrix element ρ(W)_{ST} between two SYT S (chain a) and T (chain b) factors as
a single product over levels

    ρ(W)_{ST} = Π_{i=1}^{n-1}  F_i ,
    F_i = ⟨ b_i | O_{i-1}-block(endpoints b_{i-1}, a_{i+1}) | a_i ⟩ ,

because O_{i-1} rewrites level i from a_i (S's value, untouched) to b_i (T's
final value) with the fixed endpoints s_{i-1}=b_{i-1} (already final) and
s_{i+1}=a_{i+1} (S's value). Squaring, ‖ρ_λ(W)‖_F² = Σ_{S,T} Π_i F_i² is a
transfer over PAIRS of edges: state = (a_{i+1}, b_i) (the S-chain one level
ahead of the T-chain). Each O_g step multiplies the amplitude by F_i² where
F_i is the full q-seminormal block entry on the doubled edge — the DIAGONAL
α·D(δ)+β (as in the linear transfer) when a_i == b_i, and the OFF-DIAGONAL
α·b(δ), b(δ)=√(D(δ)·D(−δ)+1), when a_i ≠ b_i. Summing terminal states by
a_n = λ gives ‖ρ_λ(W)‖_F² per partition. Because the norm SQUARES each entry,
the sign convention on the off-diagonal b cancels — no ♯/seminormal-sign
ambiguity survives.

α, β (Cayley–Hamilton O_g = α·σ_g + β·I) and D(δ) = h/(1−q^{-2δ}) are exactly
`chi_monotone_transfer._alpha_beta` / the linear transfer's D; b(δ) is the
Hoefsmit off-diagonal √(a_δ·a_{−δ}+1) of `build_seminormal_matrices`. So the
transfer reproduces the dense product entry-for-entry, EXACTLY, at 50 dps.

Validated TWO ways:

  • EXACT (n ≤ 12): per-λ ‖ρ_λ(W)‖_F² ≡ the dense einsum ρ(W)·ρ(W)^T of
    `gram_norm_binding_probe` at n = 9 (³H/³He) and n = 12 (⁴He, the wall), to
    the float64 floor of the dense reference (the transfer itself carries
    50 dps). This is an exact, deterministic match.

  • STOCHASTIC (n = 15, ⁵He, where dense is infeasible): the transfer's EXACT
    aggregate G(W)=Σ y_λ‖ρ_λ(W)‖_F² is cross-checked against the INDEPENDENT
    stochastic Hutchinson estimator `probes/gram_qtrace_hutchinson_probe`
    (tr(F·R)=E_z[(Fᵀz)·(Rz)], Rademacher z), using the SAME word, ♯ convention
    and y_λ weights. The claim is honest: transfer(exact 50-dps) ≡
    Hutchinson(float64, stochastic) within k·σ of the propagated sampling error
    (NOT an exact match). Convention parity of the two estimators is first
    confirmed at n = 9 and n = 12 — where the transfer is ALSO pinned to the
    exact dense value — with the Hutchinson forced fully stochastic
    (exact_dim=0); only then is the n = 15 number trusted. See `--with-5he`
    (the default run stops at n = 12 and still runs the n=9/12 stochastic
    parity checks).

NO float64 on the transfer path (owner ruling 2026-06-09): all numeric work is
mpmath at the 50-dps floor; the float (c,d) word is re-lifted via
`chi_monotone_transfer.word_to_mpfr`. The dense reference used only for
validation is float64 (that is the method being superseded).

Emits `gram-transfer-quadratic.witness.json` (audit-only). Not an
operator-selection / LP-SDP compute — it is a Markov-trace quadratic — so no
primal/dual witness fields apply.

Usage:
    python3 -u gram_transfer_quadratic.py 2>&1 | tee /tmp/gram_transfer_quadratic.log
    python3 -u gram_transfer_quadratic.py --max-dense 9   # skip the ~min n=12 dense check
    python3 -u gram_transfer_quadratic.py --with-5he      # also reach + validate n=15
    python3 -u gram_transfer_quadratic.py --with-5he --hutchinson-samples 200
    python3 -u gram_transfer_quadratic.py --no-hutchinson # skip stochastic cross-check
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import argparse  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from collections import defaultdict  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from chi_monotone_transfer import (  # noqa: E402
    _addable, _add, word_to_mpfr, _alpha_beta,
)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

HERE = Path(__file__).resolve().parent

# 3A-strand isotopes; A = Z+N, n = 3A.
ISOTOPES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
ISO_5HE = ("5He", 2, 3)   # n = 15, beyond the dense wall (transfer only)


# ── Young-lattice geometry (contents / interleaved middles) ────────────────
def _subset(s: tuple, t: tuple) -> bool:
    """Young-diagram containment s ⊆ t (both descending partitions)."""
    return len(s) <= len(t) and all(s[i] <= t[i] for i in range(len(s)))


def _added_box(small: tuple, big: tuple) -> tuple[int, int]:
    """The single cell (r, c) of big \\ small (big = small + one box)."""
    for r in range(len(big)):
        s = small[r] if r < len(small) else 0
        if big[r] == s + 1:
            return (r, big[r] - 1)
    raise ValueError(f"{small} → {big} is not a single-box extension")


def _content(rc: tuple[int, int]) -> int:
    return rc[1] - rc[0]


def _axial(lo: tuple, mid: tuple, hi: tuple) -> int:
    """Axial distance δ = content(box mid→hi) − content(box lo→mid) for the
    two boxes added along lo ⊂ mid ⊂ hi (|hi| = |lo| + 2)."""
    return _content(_added_box(mid, hi)) - _content(_added_box(lo, mid))


def _middles(lo: tuple, hi: tuple) -> list[tuple]:
    """Shapes m with lo ⊂ m ⊂ hi and |m| = |lo|+1 (|hi| = |lo|+2): the ≤ 2
    intermediate shapes of the seminormal block with endpoints (lo, hi)."""
    out = []
    for box in _addable(lo):
        m = _add(lo, box)
        if _subset(m, hi) and sum(hi) == sum(m) + 1:
            out.append(m)
    return out


# ── the doubled-Bratteli transfer sweep ────────────────────────────────────
def gram_all_lambda(word, n: int, *, dps: int = 50, q=None):
    """`{λ ⊢ n: ‖ρ_λ(W)‖_F²}` (mpf) for a MONOTONE (c,d,gen0) braid `word`,
    via the doubled fine-Bratteli transfer matrix. NO d_λ materialisation.

    State before applying O_{i-1} (word gen g=i-1, i=1..n-1) is
    `(a_i, b_{i-1})`: the S-chain shape at level i and the T-chain shape at
    level i-1 (S one level ahead of T). Each step chooses a_{i+1} ⊃ a_i and an
    output middle b_i between b_{i-1} and a_{i+1}, multiplying the amplitude by
    F_i² where F_i is the seminormal block entry ⟨b_i|O_{i-1}|a_i⟩ with
    endpoints (b_{i-1}, a_{i+1}). Terminal states (a_n=λ, b_{n-1}) are summed
    by λ; b_n=λ is forced (b_{n-1} ⊂ λ). Off-diagonal α·b enters exactly when
    a_i ≠ b_i — the term the linear χ-transfer drops."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    if q is None:
        q = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    gens = word_to_mpfr(word, q)
    gen_ds: dict[int, list] = defaultdict(list)
    last = -1
    for d_mp, g in gens:                                  # group + assert monotone
        if g < last:
            raise ValueError(f"non-monotone word: gen {g} after {last}")
        last = g
        gen_ds[g].append(d_mp)
    ab = {g: _alpha_beta(ds, q, qi) for g, ds in gen_ds.items()}
    _ident = (mp.mpf(0), mp.mpf(1))                       # skipped gen → O_g = I
    hq = q - qi
    Dc: dict[int, "mp.mpf"] = {1: q, -1: -qi}            # D(δ): self-diagonal

    def D(delta: int):
        v = Dc.get(delta)
        if v is None:
            v = hq / (1 - q ** (-2 * delta))
            Dc[delta] = v
        return v

    Bc: dict[int, "mp.mpf"] = {}                          # b(δ): off-diagonal

    def Boff(delta: int):
        v = Bc.get(delta)
        if v is None:
            v = mp.sqrt(D(delta) * D(-delta) + 1)
            Bc[delta] = v
            Bc[-delta] = v
        return v

    def block(lo, hi, m_in, m_out, alpha, beta):
        delta = _axial(lo, m_in, hi)
        if m_in == m_out:                                # diagonal α·D(δ)+β
            return alpha * D(delta) + beta
        return alpha * Boff(delta)                        # off-diagonal α·b(δ)

    # state before F_1: a_1 = (1,), b_0 = ∅  (level-1 shape is forced (1,))
    amp = {((1,), ()): mp.mpf(1)}
    for i in range(1, n):                                 # apply O_{i-1}, i=1..n-1
        alpha, beta = ab.get(i - 1, _ident)
        new = defaultdict(mp.mpf)
        for (a_i, b_prev), A in amp.items():
            lo = b_prev
            for box in _addable(a_i):                     # a_{i+1} = a_i + box
                a_next = _add(a_i, box)
                hi = a_next
                if not _subset(lo, a_i):                  # a_i must be a middle
                    continue
                for b_i in _middles(lo, hi):              # output middle
                    f = block(lo, hi, a_i, b_i, alpha, beta)
                    if f == 0:
                        continue
                    new[(a_next, b_i)] += A * f * f
        amp = dict(new)

    out: dict[tuple, "mp.mpf"] = defaultdict(mp.mpf)
    for (a_n, _b_prev), A in amp.items():                 # s_n = λ (b_n = λ forced)
        out[a_n] += A
    return dict(out)


def gram_norm_zn(Z: int, N: int, *, include_inter: bool, q=None, dps: int = 50):
    """`(G, per_lam, norms)` for isotope (Z,N): the aggregate
    G = Σ_λ y_λ·‖ρ_λ(W)‖_F², the per-λ contribution map
    `{λ: y_λ·‖ρ_λ(W)‖_F²}` (mirrors `gram_norm_binding_probe`'s per_lam), and
    the y-independent norms `{λ: ‖ρ_λ(W)‖_F²}` (for the dense cross-check).
    q=None → canonical q₀ baked word; a numeric q uses the q-parameterised
    word builder."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    n = 3 * (Z + N)
    qm = mp.mpf(Q_50_DIGIT_STR) if q is None else mp.mpf(str(q))
    word = (atom_braid_word_3A(Z, N, include_inter=include_inter) if q is None
            else atom_braid_word_3A(Z, N, include_inter=include_inter, q=qm))
    y = y_lambda_at_q0_mpmath(n, qm)
    norms = gram_all_lambda(word, n, dps=dps, q=qm)
    per_lam = {lam: y[lam] * norms[lam] for lam in norms}
    G = mp.fsum(per_lam.values())
    return G, per_lam, norms


# ── dense float64 reference (the method being superseded) ──────────────────
def _dense_gram_per_lambda(word, n):
    """`{λ: ‖ρ_λ(W)‖_F²}` (float) via the dense seminormal einsum of
    `gram_norm_binding_probe` — the float64 method this transfer replaces.
    Used only for validation. Imports numpy/scipy lazily so the transfer path
    has no float64 dependency."""
    import numpy as np
    import scipy.sparse as sps
    from hecke.hecke_characters import build_seminormal_matrices, partitions_of
    qf = float(mp.mpf(Q_50_DIGIT_STR))
    out = {}
    for lam in partitions_of(n):
        res = build_seminormal_matrices(tuple(lam), q=qf)
        sigmas, dim = res[0], res[1]
        if dim == 0:
            continue
        is_sparse = sps.issparse(sigmas[0])
        eye = sps.identity(dim, format="csr") if is_sparse else np.eye(dim)
        fwd = np.eye(dim)
        for c, d, g in word:                              # ρ(W) = Π (c·σ_g + d·I)
            fwd = np.asarray(fwd @ (c * sigmas[g] + d * eye))
        # ‖ρ(W)‖_F² = tr(ρ(W)·ρ(W)^♯) with ρ(W)^♯ = ρ(W)^T (symmetric letters)
        out[tuple(lam)] = float(np.einsum("ij,ji->", fwd, fwd.T))
    return out


# ── stochastic Hutchinson cross-check (independent estimator) ──────────────
# Isotopes whose EXACT transfer G_atom is additionally cross-checked against the
# stochastic Hutchinson quadratic-trace estimator
# (`probes/gram_qtrace_hutchinson_probe`).  The estimator computes the SAME
# aggregate G=Σ y_λ·tr(ρ_λ(W)ρ_λ(W^♯)) with the SAME ♯ (word reversal) and the
# transfer's own y_λ weights, so the ONLY difference is exact-transfer(50 dps)
# vs stochastic-trace(float64).  n ≤ 12 is forced FULLY stochastic
# (exact_dim=0) — every block, including the small ones already pinned to the
# dense reference, is independently sampled: the strongest convention-parity
# test.  n = 15 samples only blocks with d>exact_dim (small blocks exact) so the
# relative sampling error stays ≲1e-2 at a few-hundred probes.
HUTCH_ISOS = {"3He", "4He", "5He"}
HUTCH_EXACT_DIM = 3000   # n=15: blocks with d ≤ this computed exactly, rest sampled


def _hutchinson_gram_atom(Z, N, n, *, q0f, exact_dim, samples):
    """(G_hutch, stderr, wall_sec) — Hutchinson estimate of the SAME aggregate
    G_atom the transfer computes exactly, apples-to-apples: transfer's own y_λ
    (`y_lambda_at_q0_mpmath`) + the baked atom word (the word `gram_norm_zn`
    uses for G_atom and the dense cross-check).  The probe is imported lazily so
    the transfer path stays float64-free unless the cross-check runs."""
    import gram_qtrace_hutchinson_probe as _hutch
    y_mp = y_lambda_at_q0_mpmath(n, mp.mpf(Q_50_DIGIT_STR))
    word = atom_braid_word_3A(Z, N, include_inter=True)
    t0 = time.time()
    G, se = _hutch.gram_qtrace(word, n, y_mp, q=q0f, exact_dim=exact_dim,
                               samples=samples, label=f"{Z}p{N}n")
    return G, se, time.time() - t0


def main() -> int:
    run_start = time.monotonic()  # duration baseline (full compute, not just serialize)
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-dense", type=int, default=12,
                    help="max n to cross-check against the dense float64 einsum "
                         "(default 12 = ⁴He wall; set 9 to skip the ~min n=12 run)")
    ap.add_argument("--with-5he", action="store_true",
                    help="also compute + validate ⁵He (n=15); dense infeasible, "
                         "so validated stochastically vs the Hutchinson estimator")
    ap.add_argument("--hutchinson-samples", type=int, default=120,
                    help="Rademacher probes for the stochastic transfer-vs-"
                         "Hutchinson cross-check (default 120 → rel std err ≲1e-2)")
    ap.add_argument("--no-hutchinson", action="store_true",
                    help="skip the stochastic Hutchinson cross-check entirely")
    args = ap.parse_args()
    if (not args.no_hutchinson) and args.hutchinson_samples < 2:
        ap.error("--hutchinson-samples must be >= 2: a stochastic standard "
                 "error is undefined for < 2 samples, which would collapse the "
                 "z-score to 0 and pass the 3-sigma gate trivially (a false "
                 "validation). Use --no-hutchinson to skip the cross-check.")

    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    qi0 = 1 / q0
    isotopes = list(ISOTOPES) + ([ISO_5HE] if args.with_5he else [])

    # α (= E₀, MeV) for the B_gram diagnostic, mirroring the dense probe.
    from mass_binding_dashboard import _constants, _ame_table
    _me, _q0f, alpha = _constants()
    ame = _ame_table()

    rows = []
    max_dense_rel = mp.mpf(0)
    dense_checked = []
    hutch_checks = []       # per-isotope transfer(exact) vs Hutchinson(stochastic)
    max_hutch_z = 0.0
    for name, Z, N in isotopes:
        n = 3 * (Z + N)
        t0 = time.time()
        print(f"  {name}: n={n} …", flush=True)
        Ga, pl_a, norms_atom = gram_norm_zn(Z, N, include_inter=True)
        Gf, pl_f, _ = gram_norm_zn(Z, N, include_inter=False)
        wall = time.time() - t0

        # transfer ≡ dense (float64 einsum), per-λ, y-independent norms
        # (isolates the transfer's block algebra from the y_λ weights)
        drow = None
        if n <= args.max_dense:
            wa = atom_braid_word_3A(Z, N, include_inter=True)
            td = time.time()
            dref = _dense_gram_per_lambda(wa, n)
            iso_rel = mp.mpf(0)
            worst = None
            for lam, dv in dref.items():
                tv = norms_atom.get(lam, mp.mpf(0))
                rel = abs(tv - mp.mpf(dv)) / (1 + abs(mp.mpf(dv)))
                if rel > iso_rel:
                    iso_rel = rel
                    worst = (lam, float(tv), dv)
            max_dense_rel = max(max_dense_rel, iso_rel)
            dense_checked.append(n)
            drow = {"n": n, "n_lambda": len(dref),
                    "max_rel_transfer_vs_dense": mp.nstr(iso_rel, 4),
                    "worst_lambda": list(worst[0]) if worst else None,
                    "dense_wall_sec": f"{time.time() - td:.2f}"}
            print(f"      dense n={n}: max_rel(transfer,dense)="
                  f"{mp.nstr(iso_rel, 4)}  ({time.time()-td:.1f}s)", flush=True)

        # transfer(exact) ≡ Hutchinson(stochastic) within k·σ, INDEPENDENT
        # estimator (this is the ONLY validation available at n=15 where dense
        # is infeasible; at n≤12 it doubles as a convention-parity check, since
        # the transfer is there ALSO pinned to the exact dense value above).
        hrow = None
        if (not args.no_hutchinson) and name in HUTCH_ISOS:
            # n≤12: fully stochastic (exact_dim=0) — strongest parity test.
            # n=15: sample only the large blocks (small ones exact), keeping
            # the relative sampling error small at a few-hundred probes.
            edim = 0 if n <= 12 else HUTCH_EXACT_DIM
            Gh, se, hwall = _hutchinson_gram_atom(
                Z, N, n, q0f=float(q0), exact_dim=edim,
                samples=args.hutchinson_samples)
            z = float(abs(float(Ga) - Gh) / se) if se > 0 else 0.0
            max_hutch_z = max(max_hutch_z, z)
            relse = (se / abs(Gh)) if Gh != 0 else None
            hrow = {
                "n": n,
                "transfer_exact": mp.nstr(Ga, 16),
                "hutchinson": Gh, "hutchinson_stderr": se,
                "rel_stderr": relse,
                "deviation_sigma": z,
                "samples": args.hutchinson_samples,
                "exact_dim": edim,
                "mode": ("fully-stochastic" if edim == 0
                         else f"stochastic(d>{edim})"),
                "hutch_wall_sec": f"{hwall:.2f}",
            }
            hutch_checks.append(hrow)
            print(f"      hutch n={n}: transfer={mp.nstr(Ga, 10)} "
                  f"hutch={Gh:.6f} ± {se:.6f}  z={z:.2f}  "
                  f"relse={relse:.2e}  ({hwall:.1f}s)", flush=True)

        # bar-parity split of G at q₀ / q₀⁻¹ (q-parameterised word for both legs,
        # matching gram_norm_binding_probe --qbar internal consistency)
        Ga0, _, _ = gram_norm_zn(Z, N, include_inter=True, q=q0)
        Gai, _, _ = gram_norm_zn(Z, N, include_inter=True, q=qi0)
        Gf0, _, _ = gram_norm_zn(Z, N, include_inter=False, q=q0)
        Gfi, _, _ = gram_norm_zn(Z, N, include_inter=False, q=qi0)
        qbar = {
            "G_atom_even": Ga0 + Gai, "G_atom_odd": Ga0 - Gai,
            "G_free_even": Gf0 + Gfi, "G_free_odd": Gf0 - Gfi,
        }
        for k in list(qbar):
            qbar[k] = qbar[k] / 2

        B_gram = (mp.mpf("0.5") * alpha * mp.log(Gf / Ga)
                  if (Gf > 0 and Ga > 0) else None)
        bame = ame.get((Z, Z + N), (None,))[0]
        rows.append({
            "iso": name, "n": n,
            "G_atom": mp.nstr(Ga, 30), "G_free": mp.nstr(Gf, 30),
            "B_gram": (mp.nstr(B_gram, 12) if B_gram is not None else None),
            "B_AME": bame,
            "err_gram": (mp.nstr(bame / B_gram, 6)
                         if (bame is not None and B_gram) else None),
            "qbar": {k: mp.nstr(v, 30) for k, v in qbar.items()},
            "per_lambda_atom": [
                {"lam": list(lam), "c_lambda": mp.nstr(pl_a[lam], 24)}
                for lam in sorted(pl_a, key=lambda L: (-abs(pl_a[L]),))],
            "per_lambda_free": [
                {"lam": list(lam), "c_lambda": mp.nstr(pl_f[lam], 24)}
                for lam in sorted(pl_f, key=lambda L: (-abs(pl_f[L]),))],
            "dense_crosscheck": drow,
            "hutchinson_crosscheck": hrow,
            "wall_sec": round(wall, 3),
        })
        print(f"      G_atom={mp.nstr(Ga, 8)} G_free={mp.nstr(Gf, 8)} "
              f"B_gram={mp.nstr(B_gram, 6) if B_gram is not None else '—'} "
              f"({wall:.2f}s)", flush=True)

    # ── summary tables ──
    print("\n| iso | n | B_AME | B_gram | err_gram | G_atom | G_free |")
    print("|---|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        print(f"| {r['iso']} | {r['n']} | "
              f"{r['B_AME'] if r['B_AME'] is not None else '—'} | "
              f"{r['B_gram'] or '—'} | {r['err_gram'] or '—'} | "
              f"{mp.nstr(mp.mpf(r['G_atom']), 8)} | "
              f"{mp.nstr(mp.mpf(r['G_free']), 8)} |")

    print("\n| iso | dense n | #λ | max_rel(transfer,dense) | dense wall |")
    print("|---|--:|--:|--:|--:|")
    for r in rows:
        d = r["dense_crosscheck"]
        if d:
            print(f"| {r['iso']} | {d['n']} | {d['n_lambda']} | "
                  f"{d['max_rel_transfer_vs_dense']} | {d['dense_wall_sec']}s |")

    if hutch_checks:
        print("\n| iso n | transfer (exact) | Hutchinson ± σ | dev (σ) | "
              "rel σ | samples | mode | wall |")
        print("|---|--:|--:|--:|--:|--:|---|--:|")
        for r in rows:
            h = r["hutchinson_crosscheck"]
            if h:
                print(f"| {r['iso']} n={h['n']} | "
                      f"{mp.nstr(mp.mpf(h['transfer_exact']), 10)} | "
                      f"{h['hutchinson']:.6f} ± {h['hutchinson_stderr']:.6f} | "
                      f"{h['deviation_sigma']:.2f} | {h['rel_stderr']:.2e} | "
                      f"{h['samples']} | {h['mode']} | {h['hutch_wall_sec']}s |")

    max_n = max(r["n"] for r in rows)

    # ── witness ──
    builder = WitnessBuilder("gram-transfer-quadratic", engine="mpmath",
                             start_time=run_start)
    builder.set_description(
        "EXACT d_λ-free doubled-Bratteli transfer for the quadratic Markov/"
        "Frobenius Gram norm G(W)=tr_M(W·W^♯)=Σ y_λ‖ρ_λ(W)‖_F²; drop-in exact "
        "replacement for the float64 dense gram_norm_binding_probe, clearing "
        f"the n=12 dense wall (this run: max_n_reached={max_n}; n=15 optional "
        "via --with-5he). Exploratory, no fit.")
    builder.add_parameter("q0", Q_50_DIGIT_STR)
    builder.add_parameter("q0_inverse", mp.nstr(qi0, 50))
    builder.add_parameter("alpha_MeV", alpha)
    builder.add_parameter("dps", 50)
    builder.add_parameter("precision", "mpmath 50-dps (EXACT; no float64 on the "
                          "transfer path)")
    builder.add_parameter("isotopes", [r["iso"] for r in rows])
    builder.add_parameter("max_n_reached", max_n)
    builder.add_parameter(
        "sharp_involution",
        "word reversal; fixes q and each letter c·σ_g + d·1 (⇒ ρ(W^♯)=ρ(W)^T)")
    builder.add_parameter(
        "method",
        "doubled fine-Bratteli transfer over pairs of edges (state=(a_{i+1}, "
        "b_i)); diagonal α·D(δ)+β when a_i==b_i, off-diagonal α·√(D(δ)D(−δ)+1) "
        "when a_i≠b_i; ‖ρ_λ(W)‖_F²=Σ_{S,T}(Π F_i)²")
    builder.add_data("rows", rows)
    builder.add_data("dense_validated_n", dense_checked)
    builder.add_data("hutchinson_crosschecks", hutch_checks)
    builder.add_parameter(
        "hutchinson_estimator",
        "probes/gram_qtrace_hutchinson_probe: tr(F·R)=E_z[(Fᵀz)·(Rz)], "
        "Rademacher z; float64 + stochastic. Same word, same ♯ (reversal), "
        "same y_λ as the transfer — only exact-vs-stochastic differs.")
    hutch_validated_n = sorted({h["n"] for h in hutch_checks})
    builder.add_data("hutchinson_validated_n", hutch_validated_n)

    builder.add_assertion(
        name="exact_transfer_matches_dense_gram",
        computed=float(max_dense_rel), expected=0.0, tolerance=1e-8,
        unit=f"max rel diff per-λ ‖ρ_λ(W)‖_F² transfer(50dps) vs dense einsum "
             f"(float64) over n∈{dense_checked}",
        source="doubled-Bratteli transfer ≡ dense ρ(W)·ρ(W)^T of "
               "gram_norm_binding_probe; agreement at the float64 floor of the "
               "dense reference (the transfer carries 50 dps).",
    )
    builder.add_assertion(
        name="n12_wall_cleared_by_transfer",
        computed=(1.0 if max_n >= 12 else 0.0), expected=1.0, tolerance=0.5,
        unit="transfer reached ⁴He n=12 (and beyond) without d_λ materialisation",
        source="Σ_λ d_λ²=(3A)! caps the dense probe at A≤3 (opt-in ⁴He); the "
               "transfer is edge-count bound, not d_λ bound.",
    )
    if hutch_checks:
        builder.add_assertion(
            name="transfer_matches_hutchinson_within_error",
            computed=max_hutch_z, expected=0.0, tolerance=3.0,
            unit=f"max |transfer(exact 50dps) − Hutchinson(float64 stochastic)| "
                 f"/ σ_hutch over n∈{hutch_validated_n} (units of Hutchinson "
                 f"standard errors; 3 = 3σ)",
            source="INDEPENDENT stochastic estimator "
                   "probes/gram_qtrace_hutchinson_probe on the SAME word/♯/y_λ. "
                   "Convention parity confirmed at n=9,12 (fully stochastic, "
                   "exact_dim=0) where the transfer is ALSO pinned to the exact "
                   "dense value; this is the ONLY validation at n=15 (⁵He), "
                   "where dense is infeasible. Not an exact match — agreement "
                   "within propagated sampling error.",
        )
    builder.set_audit_only(
        "docs/audits/2026-07-03-qbar-norm-repitch-assessment.md")
    out = builder.save()
    print(f"\nWitness: {out}")
    hutch_ok = (not hutch_checks) or (max_hutch_z <= 3.0)
    all_passed = (bool(max_dense_rel <= mp.mpf("1e-8")) and max_n >= 12
                  and hutch_ok)
    print(f"Max Hutchinson deviation: {max_hutch_z:.2f}σ  "
          f"(over n∈{hutch_validated_n})" if hutch_checks
          else "Hutchinson cross-check: skipped")
    print(f"All assertions pass: {all_passed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
