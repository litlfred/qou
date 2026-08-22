#!/usr/bin/env python3
"""chi_monotone_transfer — χ^λ for a MONOTONE braid word via the fine-
Bratteli transfer matrix (multiplicity-free). The SCALABLE atom-config χ.

This is step [b] of the large-A χ scaling plan (audit
docs/audits/2026-06-09-large-A-chi-bottleneck-scaling-plan.md §8). It
SUPERSEDES the coarse-multiplicity F-matrix design of §8a/§8b with a
simpler, provably-correct construction enabled by a structural fact:

  KEY FACT (verified, every atom D…⁷Li): the atom braid word
  `mass_at_3A_proper.atom_braid_word_3A` has a MONOTONE non-decreasing
  generator sequence — nucleon k uses gens 3k, 3k+1, junction 3k+2, then
  k+1 starts at 3k+3 > 3k+2; no generator is ever revisited.

For a monotone word W = O_0·O_1·…·O_{n-2} each O_g = Π_{j:g_j=g}(σ_g + d_j·1)
is a polynomial in σ_g ALONE (every atom-word factor has c=1; d ∈ {0 (σ),
−h (σ⁻¹), −h/2 (averaged), −h(½−δ/4) (color-weighted p-n)} — chi_cd_mpfr).

In the seminormal (Gelfand–Zetlin / fine-Bratteli) basis, σ_g changes ONLY
the shape s_{g+1} at level g+1 of the chain ∅=s_0 ⊂ s_1 ⊂ … ⊂ s_n=λ (one
box per step), fixing every other s_i. Closing the character trace forces
each level to return to its start (each O_g is the only operator on its
level and is applied once), so every O_g contributes its DIAGONAL block
entry and

    χ^λ(W) = Σ_{SYT chains ∅→…→λ}  Π_g [O_g]_{s_{g+1},s_{g+1}}

a product of LOCAL factors, each depending on three consecutive levels
(s_g, s_{g+1}, s_{g+2}) via the 2×2 (or 1×1) seminormal block. The sum
over chains is a TRANSFER MATRIX over fine-Bratteli EDGES (s_g ⊂ s_{g+1}):
multiplicity-free, |edges| ~ a few thousand at n=21, NEVER d_λ (~1.6×10⁷
at n=18). All χ^λ for λ ⊢ 3A come out of ONE sweep.

Hand-verified: χ^{(2,1)}(σ_0σ_1) = −1 (the S_3 3-cycle character); the
_self_test confirms χ ≡ char_fast (≡ pyhecke_native) for D (n=6), ³He
(n=9) and the cached atom oracles D/T/³He/⁴He.

NO float64 on the canonical path (owner ruling 2026-06-09): all numeric
work is mpmath at the 50-dps floor; the float (c,d) carried by the word
builder is re-lifted to MPFR here (δ rebuilt from flavor_split_leading).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from collections import defaultdict  # noqa: E402
from functools import lru_cache  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402

_TOL = 1e-9


# ── Young-lattice (fine Bratteli) primitives — partition = descending tuple ──
@lru_cache(maxsize=4096)
def _addable(shape: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Addable corner boxes (r, c) — adding one yields a valid partition."""
    rows = shape
    out = []
    for r in range(len(rows) + 1):
        cur = rows[r] if r < len(rows) else 0
        above = rows[r - 1] if r - 1 >= 0 else None
        if above is None or cur < above:
            out.append((r, cur))
    return tuple(out)


def _add(shape: tuple[int, ...], box: tuple[int, int]) -> tuple[int, ...]:
    r, _c = box
    rows = list(shape)
    if r == len(rows):
        rows.append(1)
    else:
        rows[r] += 1
    return tuple(rows)


# ── MPFR re-lift of the (float) atom word ──────────────────────────────────
def word_to_mpfr(word, q: "mp.mpf"):
    """`[(d_mpf, gen0)]` from a `[(c, d_float, gen0)]` atom word.

    Every atom-word crossing has c=1; only d distinguishes σ / σ⁻¹ /
    averaged / color-weighted p-n. The float d carries ~17 sig digits, so
    we re-identify the template and rebuild d at full dps (δ from
    flavor_split_leading). Raises on any unrecognised template so
    convention drift fails loudly (mirrors chi_cd_mpfr.to_braid_terms).
    """
    h = q - 1 / q
    h_f = float(h)
    color_deltas = None  # lazy: the live color-weight δ conventions
    out = []
    for c, d, g in word:
        cf, df = float(c), float(d)
        if abs(cf - 1.0) > _TOL:
            raise ValueError(f"unsupported crossing c={c} at gen={g} (expect c=1)")
        if abs(df) < _TOL:
            d_mp = mp.mpf(0)
        elif abs(df + h_f) < _TOL:
            d_mp = -h
        elif abs(df + h_f / 2) < _TOL:
            d_mp = -h / 2
        else:
            # Color-weighted p-n crossing `−h·(½ − δ/4)`. The word may have been
            # built under either live δ convention: the canonical single source
            # `_avg_color_delta()` (q=None / q₀ words — now `flavor_split_leading`
            # after the 2026-06-29 flavor-split de-wire) or `flavor_split_*(q)`
            # for q-parameterised words. Re-identify against all live conventions
            # and rebuild d at full dps from whichever matches; raise only if
            # NONE does, so genuine convention drift still fails loudly.
            if color_deltas is None:
                color_deltas = _color_weight_deltas(q)
            d_mp = next(
                (-(h * (mp.mpf("0.5") - dlt / 4)) for dlt in color_deltas
                 if abs(float(-(h * (mp.mpf("0.5") - dlt / 4))) - df) <= _TOL),
                None)
            if d_mp is None:
                raise ValueError(
                    f"unrecognised crossing (c={c}, d={d}) at gen={g}; expected "
                    "σ / σ⁻¹ / averaged / color-weighted p-n")
        out.append((d_mp, g))
    return out


def _color_weight_deltas(q: "mp.mpf"):
    """Live color-weight δ conventions a p-n crossing `−h·(½ − δ/4)` may use.

    Returns the canonical single source `_avg_color_delta()` (q₀, the
    `flavor_split_leading`-based value after the 2026-06-29 de-wire) plus the
    general-`q` leading/subleading variants, so `word_to_mpfr` re-identifies a
    crossing regardless of which δ built the word. Each is an `mp.mpf`; missing
    sources are skipped (the caller raises only if none match).
    """
    out = []
    for mod, name, arg in (("canonical_braid_crossings", "_avg_color_delta", None),
                           ("_li_2_q_util", "flavor_split_leading", q),
                           ("_li_2_q_util", "flavor_split_subleading", q)):
        try:
            fn = getattr(__import__(mod), name)
            out.append(fn() if arg is None else fn(arg))
        except Exception:
            pass
    return out


# ── Cayley–Hamilton reduction of O_g = Π(σ_g + d_j·1) ──────────────────────
def _alpha_beta(ds, q, qi):
    """O_g = Π_j(σ_g + d_j·1) = α·σ_g + β·I (Cayley–Hamilton).

    σ_g has eigenvalues q and −q⁻¹ on every 2×2 (and is one of them on a
    1×1), so O_g has eigenvalues E₁=Π(q+d_j), E₂=Π(−q⁻¹+d_j). Then any
    DIAGONAL entry of O_g is α·(that diagonal of σ_g) + β — the off-diagonal
    seminormal convention never enters the diagonal of a polynomial in σ_g.
    This is the key that removes the 2×2 matmul + q-power from the per-edge
    inner loop: the block diagonal becomes α·D(δ′) + β, a function of the
    content gap δ′ alone. Empty ds → identity (α=0, β=1)."""
    e1 = mp.mpf(1)
    e2 = mp.mpf(1)
    for d in ds:
        e1 *= (q + d)
        e2 *= (-qi + d)
    denom = q + qi
    return (e1 - e2) / denom, (q * e2 + qi * e1) / denom


# ── the transfer-matrix sweep ──────────────────────────────────────────────
def chi_all_lambda(word, n: int, *, dps: int = 50, q=None):
    """`{λ ⊢ n: χ^λ(word)}` (mpf) for a MONOTONE (c,d,gen0) braid `word`,
    via the fine-Bratteli transfer matrix. NO d_λ materialisation.

    State is `(shape s_{g+1}, c_this)` where c_this = content of the box
    added s_g→s_{g+1} (a removable corner of s_{g+1} — so (shape, c_this)
    is in bijection with the Bratteli edge s_g ⊂ s_{g+1}). Applying O_g
    advances s_{g+1}→s_{g+2} by one box (content c_other); the block
    diagonal is α_g·D(δ′)+β_g with δ′ = c_other − c_this. D(δ′) and (α,β)
    are cached, so the inner loop is ~3 mpf ops per edge."""
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
    Dc: dict[int, "mp.mpf"] = {1: q, -1: -qi}            # D(δ′): self-diagonal

    def D(delta: int):
        v = Dc.get(delta)
        if v is None:
            v = hq / (1 - q ** (-2 * delta))
            Dc[delta] = v
        return v

    # state (s_1=(1), c_this=0): the first box (0,0) has content 0
    amp = {((1,), 0): mp.mpf(1)}
    for g in range(0, n - 1):                             # apply O_g, g=0..n-2
        alpha, beta = ab.get(g, _ident)
        new = defaultdict(mp.mpf)
        for (shape, c_this), a in amp.items():
            for (r, c) in _addable(shape):
                c_other = c - r
                f = alpha * D(c_other - c_this) + beta
                new[(_add(shape, (r, c)), c_other)] += a * f
        amp = dict(new)

    out: dict[tuple, mp.mpf] = defaultdict(mp.mpf)
    for (lam, _c), a in amp.items():                      # s_n = λ
        out[lam] += a
    return dict(out)


# ── validation ─────────────────────────────────────────────────────────────
def _self_test() -> int:
    from char_fast import chi_lambda_fast_mp
    from lr_coefficients import partitions_of
    from mass_at_3A_proper import atom_braid_word_3A
    mp.mp.dps = 50
    q = mp.mpf(Q_50_DIGIT_STR)
    ok_all = True

    # (1) vs char_fast (full Hoefsmit) on the CANONICAL color-weighted
    #     deuteron word (n=6; char_fast is O(d_λ) per basis vector, slow at n≥9).
    word = atom_braid_word_3A(1, 1)                      # default: color-weighted
    chi = chi_all_lambda(word, 6)
    max_rel = mp.mpf(0)
    for lam in partitions_of(6):
        lam = tuple(lam)
        cf = chi_lambda_fast_mp(lam, word, q).real
        max_rel = max(max_rel, abs(chi.get(lam, mp.mpf(0)) - cf) / (1 + abs(cf)))
    ok = max_rel < mp.mpf(10) ** -12
    ok_all &= ok
    print(f"  transfer ≡ char_fast (color-weighted, n=6): "
          f"max_rel={mp.nstr(max_rel, 4)}  {'OK' if ok else 'MISMATCH'}")

    # (2) vs cached atom oracles D/T/³He/⁴He (n=6..12) — an exact (50-dps)
    #     cross-check of the transfer vs the per-basis-vector kernel to n=12.
    #
    #     This comparison used `pn_convention="strict_averaged"`, on the stated
    #     grounds that the oracle witnesses "used the strict_averaged pn
    #     convention, so we compare on the MATCHING word". That was wrong about
    #     the witnesses, and it made this self-test FAIL on main — quietly,
    #     since it is wired into no gate.
    #
    #     Measured by recomputing each oracle under both conventions:
    #
    #                    strict_averaged      bring_color_weighted
    #         D             2.625e-04              5.743e-50
    #         T             5.482e-04              8.257e-50
    #         3He           5.281e-04              7.487e-50
    #         4He           1.883e-03              4.079e-49
    #
    #     The oracles reproduce EXACTLY — to the full 50-dps working precision
    #     — under the canonical colour-weighted convention, and miss by 2.6e-4
    #     .. 1.9e-3 under strict_averaged. So the cached witnesses were always
    #     canonical; it was this comparison word that was stale. The residuals
    #     grow with A because the p-n interface `d` differs by 7.19e-05 and
    #     compounds per interface, which is the colour-weighting scale — not a
    #     precision scale, and the giveaway that the mismatch was structural.
    #
    #     Note the witnesses record no convention field at all (and no
    #     `scriptFile`), so the old comment could not be checked against them;
    #     it had to be tested by recomputation. Bean `qou-9ag4`.
    import json
    oracle = {"D": "chi-deuteron-h6-at-q0-50dps.witness.json",
              "T": "chi-tritium-h9-at-q0-50dps.witness.json",
              "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
              "4He": "chi-helium-4-h12-at-q0-50dps.witness.json"}
    zn = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
    for atom, fn in oracle.items():
        f = HERE / fn
        if not f.exists():
            print(f"  oracle {atom}: witness missing, skip"); continue
        Z, N = zn[atom]
        n = 3 * (Z + N)
        word = atom_braid_word_3A(Z, N, pn_convention="bring_color_weighted")
        chi = chi_all_lambda(word, n)
        d = json.loads(f.read_text())
        bp = d.get("by_partition") or d["data"]["by_partition"]
        ref = {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"])) for p in bp}
        max_rel = mp.mpf(0)
        for lam, rv in ref.items():
            cv = chi.get(lam, mp.mpf(0))
            max_rel = max(max_rel, abs(cv - rv) / (1 + abs(rv)))
        ok = max_rel < mp.mpf(10) ** -12
        ok_all &= ok
        print(f"  transfer ≡ oracle (color-weighted) {atom:<4} n={n:<3} "
              f"λ={len(ref):<4} max_rel={mp.nstr(max_rel, 4)}  {'OK' if ok else 'MISMATCH'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(_self_test())
