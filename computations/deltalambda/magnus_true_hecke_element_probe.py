#!/usr/bin/env python3
"""magnus_true_hecke_element_probe.py — this arc has been tracing the wrong ρ. (qou-o6ov)

WHAT THE DEFECT IS. Every probe in this arc builds its ρ as

    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]

and then applies a bare `σ_g` for each `g`. But `atom_braid_word_3A` does not return a braid word —
its own docstring says so in capitals (PR #5765) — and each triple `(c, d, g)` denotes the HECKE
ELEMENT `c·σ_g + d·1`. Taking `t[2]` alone discards `c` and `d`, so:

  * a `d = 0` letter is `σ_g`          — handled correctly by the bare form;
  * a `d = −h` letter is `σ_g⁻¹`       — applied as `σ_g`, which is WRONG;
  * an averaged letter `σ − (h/2)·1`   — applied as `σ_g`, which is WRONG, and this one is not even
    in the image of `ρ : B_n → H_n(q)`.

Measured at A=3 (n=9), 35 letters: **16 σ, 12 σ⁻¹, 7 averaged** — so **19 of 35 letters, 54 %, were
applied as the wrong operator.** The arc's ρ is therefore the POSITIVE BRAID on the generator
sequence, not the atom's Hecke element.

WHY IT WENT UNNOTICED FOR THE WHOLE ARC. `[int(t[2]) for t in ...]` reads as an obviously-correct
projection to "the generator indices", and it is — the error is in believing that is all a letter
carries. The name `atom_braid_word_3A` says "braid word", and a braid word's letters ARE bare
generators; the docstring correcting that name is 60 lines long and sits behind a function every
probe here calls without reading. A rename was considered and rejected (685 call sites, 382 files),
so the misnomer is load-bearing and permanent.

WHAT THIS PROBE MEASURES. The same complete n=9 census under BOTH elements, so the arc's conclusions
can be re-decided rather than merely doubted:

    ρ_bare  = Π σ_{g}            (what every prior probe used)
    ρ_true  = Π (c·σ_g + d·1)    (the object atom_braid_word_3A actually returns)

Both through the same sparse column-wise kernel, so any difference is the coefficients and nothing
else. `c·σ_g + d·1` applied to a vector is `c·(σ_g v) + d·v`, so ρ_true costs one extra axpy per
letter — the ≤2-sparse structure that lifted this arc's dim cap (#6729) is untouched.

SCOPE — this measures which element the arc's b-decay statements are about. It does not re-derive
any of them. NO-FLOAT64: mpf end to end, dps 65, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

_WANT_DPS = 65


def _assert_dps(where):
    """The #6710 trap: a deferred import can silently reset mp.mp.dps under us."""
    if mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"{where}: mp.dps is {mp.mp.dps}, wanted {_WANT_DPS}")


def classify(word, q):
    """(n_sigma, n_sigma_inv, n_averaged) — how many letters the bare form gets wrong."""
    h = q - 1 / q
    ns = ni = na = 0
    for c, d, _g in word:
        c = mp.mpf(str(c))
        d = mp.mpf(str(d))
        if d == 0 and c == 1:
            ns += 1
        elif abs(d + h) < mp.mpf("1e-50") and c == 1:
            ni += 1
        else:
            na += 1
    return ns, ni, na


def sweep(lam, word, q, ngen, *, true_coeffs):
    """(tr_λ(ρ·Ω₂^P), ‖ρ·Ω₂^P‖_F², dim) column-wise, under ρ_true or ρ_bare.

    The ONLY difference between the two branches is whether a letter's (c, d) is honoured.
    """
    _assert_dps(f"sweep({lam}, true={true_coeffs})")
    per_gen, dim = base.block_structure(tuple(lam))
    sig = base.sigma_csr(per_gen, dim, q)
    cc = 4 / (q + 1 / q) ** 2
    rev = list(reversed(word))
    tr = mp.mpf(0)
    frob = mp.mpf(0)
    for j in range(dim):
        e = [mp.mpf(0)] * dim
        e[j] = mp.mpf(1)
        acc = [mp.mpf(0)] * dim
        for a in range(ngen - 1):
            u = base.spmatvec(sig[a], base.spmatvec(sig[a + 1], e))
            w = base.spmatvec(sig[a + 1], base.spmatvec(sig[a], e))
            for r in range(dim):
                acc[r] += u[r] - w[r]
        v = [cc * x for x in acc]
        for c, d, g in rev:
            sv = base.spmatvec(sig[g], v)
            if true_coeffs:
                c = mp.mpf(str(c))
                d = mp.mpf(str(d))
                v = [c * sv[r] + d * v[r] for r in range(dim)]
            else:
                v = sv
        tr += v[j]
        for x in v:
            if x:
                frob += x * x
    return tr, frob, dim


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps            # AFTER imports (#6710 trap)

    q = base.Q0
    n = 3 * args.A
    Z, N = args.A // 2, args.A - args.A // 2
    word = [(t[0], t[1], int(t[2])) for t in atom_braid_word_3A(Z, N)]
    ngen = max(g for _c, _d, g in word) + 1

    ns, ni, na = classify(word, q)
    print(f"[trueelt] n={n}: atom_braid_word_3A returns HECKE letters c·σ_g + d·1, not braid")
    print(f"[trueelt] generators. This arc used a bare σ_g for every one of them.  (dps={args.dps})\n")
    print(f"  {len(word)} letters:  σ {ns}   σ⁻¹ {ni}   averaged {na}")
    print(f"  ⇒ {ni + na} of {len(word)} ({100 * (ni + na) // len(word)} %) were applied as the "
          f"WRONG operator by the bare form.\n")

    print(f"  {'b':>3}  {'λ':<26}{'dim':>5}{'|tr|/dim BARE':>16}{'|tr|/dim TRUE':>16}{'ratio':>10}")
    env_bare, env_true = {}, {}
    rows = []
    for lam in base.partitions(n):
        lam = tuple(lam)
        b = n - lam[0]
        tb, fb, dim = sweep(lam, word, q, ngen, true_coeffs=False)
        tt, ft, _ = sweep(lam, word, q, ngen, true_coeffs=True)
        ab, at = abs(tb) / dim, abs(tt) / dim
        env_bare[b] = max(env_bare.get(b, mp.mpf(0)), fb / dim)
        env_true[b] = max(env_true.get(b, mp.mpf(0)), ft / dim)
        rows.append((b, lam, dim, ab, at))
        r = (at / ab) if ab > 0 else mp.mpf("nan")
        print(f"  {b:>3}  {str(lam):<26}{dim:>5}{mp.nstr(ab, 7):>16}{mp.nstr(at, 7):>16}"
              f"{mp.nstr(r, 5):>10}")

    print("\n  ENVELOPE E(b) = max_{b(λ)=b} tr_λ(X*X)/dim_λ, both elements:")
    print(f"  {'b':>3}{'E(b) BARE':>18}{'E(b) TRUE':>18}")
    bs = sorted(k for k in env_true if 1 <= k <= n - 2)
    for b in bs:
        print(f"  {b:>3}{mp.nstr(env_bare[b], 8):>18}{mp.nstr(env_true[b], 8):>18}")
    dec_b = all(env_bare[bs[i + 1]] < env_bare[bs[i]] for i in range(len(bs) - 1))
    dec_t = all(env_true[bs[i + 1]] < env_true[bs[i]] for i in range(len(bs) - 1))
    print(f"\n  envelope strictly decreasing in b?   BARE {'YES ✓' if dec_b else 'NO ✗'}"
          f"    TRUE {'YES ✓' if dec_t else 'NO ✗'}")

    # The hook split, under the true element.
    def is_hook(l):
        return all(p == 1 for p in l[1:])

    print("\n  HOOK RANK within each level, by tr(X*X)/dim, under the TRUE element:")
    for b in bs:
        lvl = sorted([r for r in rows if r[0] == b], key=lambda r: -r[4])
        hk = [i for i, r in enumerate(lvl) if is_hook(r[1])]
        if hk and len(lvl) > 1:
            pos = hk[0]
            where = "MAX" if pos == 0 else ("MIN" if pos == len(lvl) - 1 else f"{pos + 1}/{len(lvl)}")
            print(f"    b={b}: hook is level-{where}  (of {len(lvl)} shapes)")
    print("\n  Read the ratio column, not the ✓ marks: a conclusion that holds under both elements")
    print("  is about the b-grading; one that holds under only one is about the letter coefficients.")


if __name__ == "__main__":
    main()
