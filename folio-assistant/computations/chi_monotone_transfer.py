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
builder is re-lifted to MPFR here (δ rebuilt from flavor_split_subleading).
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
def _cells(shape: tuple[int, ...]) -> frozenset:
    return frozenset((r, c) for r, row in enumerate(shape) for c in range(row))


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


def _content(box: tuple[int, int]) -> int:
    return box[1] - box[0]


# ── MPFR re-lift of the (float) atom word ──────────────────────────────────
def word_to_mpfr(word, q: "mp.mpf"):
    """`[(d_mpf, gen0)]` from a `[(c, d_float, gen0)]` atom word.

    Every atom-word crossing has c=1; only d distinguishes σ / σ⁻¹ /
    averaged / color-weighted p-n. The float d carries ~17 sig digits, so
    we re-identify the template and rebuild d at full dps (δ from
    flavor_split_subleading). Raises on any unrecognised template so
    convention drift fails loudly (mirrors chi_cd_mpfr.to_braid_terms).
    """
    h = q - 1 / q
    h_f = float(h)
    delta = None
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
            if delta is None:
                from _li_2_q_util import flavor_split_subleading
                delta = flavor_split_subleading(q)
            d_mp = -(h * (mp.mpf("0.5") - delta / 4))
            if abs(float(d_mp) - df) > _TOL:
                raise ValueError(
                    f"unrecognised crossing (c={c}, d={d}) at gen={g}; expected "
                    "σ / σ⁻¹ / averaged / color-weighted p-n")
        out.append((d_mp, g))
    return out


# ── local seminormal block: diagonal of O_g = Π(σ_g + d·1) ─────────────────
def _local_diag(ds, s_lo, s_hi, q, qi):
    """`{s_mid: [O_g]_{s_mid,s_mid}}` for O_g = Π_j(σ_g + ds[j]·1) in the
    block s_lo ⊂ s_mid ⊂ s_hi (two boxes added). 1 or 2 intermediates."""
    added = _cells(s_hi) - _cells(s_lo)                  # exactly 2 cells
    inter = []                                            # (s_mid, box_first)
    for box in _addable(s_lo):                            # only valid corners
        if box in added:
            smid = _add(s_lo, box)
            if _cells(smid) <= _cells(s_hi):             # the other box completes
                inter.append((smid, box))
    if len(inter) == 1:                                  # dependent boxes → scalar
        smid, box1 = inter[0]
        (box2,) = added - {box1}
        delta = _content(box2) - _content(box1)          # ±1
        eig = q if delta == 1 else -qi
        val = mp.mpf(1)
        for d in ds:
            val *= (eig + d)
        return {smid: val}
    # 2×2 block, basis order (X, Y)
    (sX, bX), (sY, bY) = inter
    dXY = _content(bY) - _content(bX)
    diagX = (q - qi) / (1 - q ** (-2 * dXY))
    diagY = (q - qi) - diagX
    sig = mp.matrix([[diagX, mp.mpf(1)], [diagX * diagY + 1, diagY]])
    O = mp.eye(2)
    for d in ds:
        O = O * (sig + d * mp.eye(2))
    return {sX: O[0, 0], sY: O[1, 1]}


# ── the transfer-matrix sweep ──────────────────────────────────────────────
def chi_all_lambda(word, n: int, *, dps: int = 50, q=None):
    """`{λ ⊢ n: χ^λ(word)}` (mpf) for a MONOTONE (c,d,gen0) braid `word`,
    via the fine-Bratteli transfer matrix. NO d_λ materialisation."""
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

    # amp over fine-Bratteli edges (s_g, s_{g+1}); start at (∅, (1))
    amp = {((), (1,)): mp.mpf(1)}
    for g in range(0, n - 1):                             # apply O_g, g=0..n-2
        ds = gen_ds.get(g, [])                            # [] → identity factor
        new = defaultdict(mp.mpf)
        for (s_lo, s_mid), a in amp.items():
            for box in _addable(s_mid):
                s_hi = _add(s_mid, box)
                fmap = _local_diag(ds, s_lo, s_hi, q, qi)
                f = fmap.get(s_mid)
                if f is None:
                    continue
                new[(s_mid, s_hi)] += a * f
        amp = dict(new)

    out: dict[tuple, mp.mpf] = defaultdict(mp.mpf)
    for (s_lo, lam), a in amp.items():                    # s_{n-1} ⊂ s_n=λ
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

    # (1) vs char_fast (full Hoefsmit) on deuteron (n=6) and ³He (n=9)
    for atom, (Z, N) in (("D", (1, 1)), ("3He", (2, 1))):
        n = 3 * (Z + N)
        word = atom_braid_word_3A(Z, N)
        chi = chi_all_lambda(word, n)
        max_rel = mp.mpf(0)
        for lam in partitions_of(n):
            lam = tuple(lam)
            cf = chi_lambda_fast_mp(lam, word, q).real
            cv = chi.get(lam, mp.mpf(0))
            max_rel = max(max_rel, abs(cv - cf) / (1 + abs(cf)))
        ok = max_rel < mp.mpf(10) ** -12
        ok_all &= ok
        print(f"  transfer χ ≡ char_fast  {atom:<4} n={n:<3} "
              f"max_rel={mp.nstr(max_rel, 4)}  {'OK' if ok else 'MISMATCH'}")

    # (2) vs cached atom oracles (the per-basis-vector witnesses)
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
        chi = chi_all_lambda(atom_braid_word_3A(Z, N), n)
        d = json.loads(f.read_text())
        bp = d.get("by_partition") or d["data"]["by_partition"]
        ref = {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"])) for p in bp}
        max_rel = mp.mpf(0)
        for lam, rv in ref.items():
            cv = chi.get(lam, mp.mpf(0))
            max_rel = max(max_rel, abs(cv - rv) / (1 + abs(rv)))
        ok = max_rel < mp.mpf(10) ** -12
        ok_all &= ok
        print(f"  transfer χ ≡ oracle     {atom:<4} n={n:<3} λ={len(ref):<4} "
              f"max_rel={mp.nstr(max_rel, 4)}  {'OK' if ok else 'MISMATCH'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(_self_test())
