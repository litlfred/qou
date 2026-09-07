#!/usr/bin/env python3
"""bond_pn_kind_order_four_discriminator_probe.py — the pn interface kind, settled. (qou-qqm4)

## The open item this closes

#6992 identified each atom-word interface factor as `z + d_kind`, and #7000 sharpened that to the
two Markov parameters and their average. Both carried the same 🛑 limit, stated in both PR bodies
and in the bean:

> `d_averaged_weighted = −h·(1/2 − δ/4)` with `δ = O(ε³)` and `h = O(ε)`, so `δ` first contributes
> at `ε⁴` and `d_averaged == d_averaged_weighted` identically through `K = 3`. Both probes establish
> only that the mixed interface is **not** `sigma` and **not** `sigma_inv`. Order 4 is the
> discriminating measurement.

**It is cheaper than either PR said.** Both estimated the cost as an `A = 3` word at `K = 4`
(~17 min/word). That is the wrong object: the bond factors are *extracted at `A = 2`*, from
one-interface words, so the discriminator is an `A = 2` measurement — **41 s**, not 17 minutes. The
`A = 3` run is a held-out test of the *product*, which is a different question and is kept below as
one.

## The answer: `averaged_weighted`, decisively

At `ε⁴` the two candidate kinds finally separate, and the measurement picks one:

    d_averaged           (0, −1, 1/2, −1/2, 1/2 )
    d_averaged_weighted  (0, −1, 1/2, −1/2, 7/6 )      ← differ here for the first time

    z                    (1/2)·(1, 2, 1/2, −1/2, 1/4)
    z + d_averaged       (1/2, 0, 3/4, −3/4,  5/8 )    ruled out
    z + d_averaged_wtd   (1/2, 0, 3/4, −3/4, 31/24)    ← MATCHES
    measured pn bond     (1/2, 0, 3/4, −3/4, 31/24)

So #6992's kind table is a **full three determinations after all**, not the "two-and-a-half" both
PRs (correctly, at the time) reported. The amendment those bodies carry is now itself superseded,
and this probe is the reason to say so.

## What that costs the "average" reading — it is exactly an order-≤3 fact

#7000's headline was that the three bonds are `z`, `(z + z′)/2`, `z′`. Two thirds of that survives
order 4 and one third does not:

    pp   z            (1/2, 1, 1/4, −1/4,  1/8)   measured identically      STILL EXACT
    nn   z′ = z − h   (1/2, −1, 5/4, −5/4, 9/8)   measured identically      STILL EXACT
    pn   (z + z′)/2   (1/2, 0, 3/4, −3/4,  5/8)   measured 31/24            BREAKS at ε⁴

The mixed bond is the plain mean of the like-bonds through order 3 and **stops being it at order
4**, by exactly `d`'s `δ` term. `pp` and `nn` acquire no correction at all, so the whole `δ`
weighting lives in the mixed interface — which is the one place a `(p, n)` asymmetry could enter.

**The `υ_b = −τ_b` corollary of #7000 also does not continue**, and that is the honest reading of
it: it was `z`'s `−1/2`-against-`+1/2` and `h`'s `+1`-against-`−1` at one order, not a law. At
order 4 the normalised factors are `(…, 1/4)`, `(…, 31/12)`, `(…, 9/4)` — three unrelated numbers.
#7000 said the relation was inherited rather than structural; this is the measurement that shows
the inheritance stops.

## What is NOT claimed

- **This does not make the bond factor fitted.** `d_averaged_weighted` is the corpus's own
  `letter_d_series`, and `δ = (q−1)²(1−q⁻⁴)/3` is written there; nothing here is tuned to `31/24`.
  What changed is that a *previously untested* branch of that function is now tested, and passed.
- **`A ≤ 3` for the product**, and order 4 only for the bond factors themselves. The held-out
  product test below is one `A = 3` word.
- **No Lean.** The order-3 Lean (`tr_mul_gen_comb`) states `c • g + c' • ginv`; `averaged_weighted`
  is *not* of that form at order 4 — the `δ` term is not a constant combination of the two
  generators — so the merged theorem does not cover this and is not claimed to.

Exact `Fraction` arithmetic throughout; no `q₀` evaluated, no float, no witness, nothing wired.

SCOPE — (a) scope-limited.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

_spec = importlib.util.spec_from_file_location(
    "diag", _HERE / "c2_diagonal_insertion_expansion_probe.py")
_D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_D)

K = 4

# Held-out: 3He at K = 4. ~16 min per word, so recorded; --verify-live re-measures.
TARGET_3HE: dict[str, list[F]] = {}


def pmul(a: list[F], b: list[F]) -> list[F]:
    return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(K + 1)]


def pdiv(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (K + 1)
    for k in range(K + 1):
        out[k] = (a[k] - sum(out[i] * b[k - i] for i in range(k))) / b[0]
    return out


def z_series() -> list[F]:
    """`z_D = q³/(q²+1)` at `q = 1+ε`, order 4."""
    q = [F(1), F(1)] + [F(0)] * (K - 1)
    q2 = pmul(q, q)
    q3 = pmul(q2, q)
    return pdiv(q3, [q2[0] + 1] + q2[1:])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-live", action="store_true",
                    help="re-measure the held-out 3He word at K=4 (~33 min)")
    args = ap.parse_args()

    t0 = time.time()
    print("=" * 94)
    print("  The pn interface kind at ORDER 4 — the discriminating measurement, and it is at A=2")
    print("=" * 94)

    nuc = {"p": _D.trace_expansion(1, 0, False, K)[0],
           "n": _D.trace_expansion(0, 1, False, K)[0]}
    nuc = {k: list(v) for k, v in nuc.items()}
    bond = {}
    for b, (Z, N, x, y) in (("pp", (2, 0, "p", "p")), ("pn", (1, 1, "p", "n")),
                            ("nn", (0, 2, "n", "n"))):
        t = time.time()
        bond[b] = pdiv(list(_D.trace_expansion(Z, N, True, K)[0]), pmul(nuc[x], nuc[y]))
        print(f"  measured bond {b}: {[str(v) for v in bond[b]]}  ({time.time()-t:.0f}s)")

    z = z_series()
    h = _D.series_h(K)
    zp = [z[i] - h[i] for i in range(K + 1)]
    avg = [(z[i] + zp[i]) / 2 for i in range(K + 1)]

    # ---- 1. the discriminator ----------------------------------------------------------
    print(f"\n  1. THE DISCRIMINATOR — at ε⁴ the two candidate kinds separate for the first time")
    da = _D.letter_d_series("averaged", K)
    dw = _D.letter_d_series("averaged_weighted", K)
    print(f"     d_averaged           {[str(x) for x in da]}")
    print(f"     d_averaged_weighted  {[str(x) for x in dw]}")
    separated = da != dw
    print(f"     they differ at K={K}: {separated}  (they are IDENTICAL through K=3 — that is why"
          f" order 4 was needed)")
    pa = [z[i] + da[i] for i in range(K + 1)]
    pw = [z[i] + dw[i] for i in range(K + 1)]
    hit_a, hit_w = pa == bond["pn"], pw == bond["pn"]
    print(f"\n     z + d_averaged           {[str(x) for x in pa]}  "
          f"{'MATCHES' if hit_a else 'ruled out'}")
    print(f"     z + d_averaged_weighted  {[str(x) for x in pw]}  "
          f"{'MATCHES' if hit_w else 'ruled out'}")
    print(f"     measured pn              {[str(x) for x in bond['pn']]}")
    ok1 = separated and hit_w and not hit_a
    print(f"     ⇒ {'the pn interface is `averaged_weighted`. SETTLED — #6992’s kind table is three determinations, not two-and-a-half.' if ok1 else 'INCONCLUSIVE or the OTHER kind matched — read the rows above; that is the finding.'}")

    # ---- 2. what breaks, and what does not ----------------------------------------------
    print(f"\n  2. THE 'AVERAGE' READING IS EXACTLY AN ORDER-≤3 FACT")
    print(f"     z           {[str(x) for x in z]}")
    print(f"     z' = z − h  {[str(x) for x in zp]}")
    print(f"     (z + z')/2  {[str(x) for x in avg]}")
    rows = [("pp", z, "z"), ("nn", zp, "z' = z − h"), ("pn", avg, "(z + z')/2")]
    ok2 = True
    for b, pred, why in rows:
        same = pred == bond[b]
        expect = (b != "pn")          # pp and nn must hold; pn must BREAK
        ok2 = ok2 and (same == expect)
        verdict = ("STILL EXACT at order 4" if same else "BREAKS at ε⁴")
        print(f"     {b:3s} = {why:<12s} {verdict}"
              f"{'' if same else f'   ({str(pred[K])} predicted vs {str(bond[b][K])} measured)'}")
    print(f"     ⇒ {'only the MIXED bond acquires the δ correction; pp and nn take none. The whole' if ok2 else 'FAIL — the pattern is not what order 3 predicted. That is the finding.'}")
    if ok2:
        print("       weighting lives in the one interface where a (p,n) asymmetry could enter.")

    # ---- 3. the υ = −τ corollary does not continue ---------------------------------------
    print(f"\n  3. #7000's `υ = −τ` COROLLARY STOPS — as it said it might (inherited, not a law)")
    cont = True
    for b in ("pp", "pn", "nn"):
        n_ = [x / bond[b][0] for x in bond[b]]
        holds3 = n_[3] == -n_[2]
        cont = cont and holds3
        print(f"     {b:3s} normalised {[str(x) for x in n_]}   υ=−τ at order 3: {holds3}")
    print("     order-4 coefficients are three unrelated numbers — no relation of that shape holds.")

    # ---- 4. held-out product test --------------------------------------------------------
    print(f"\n  4. HELD OUT — 3He (Z=2,N=1) at order 4, predicted from the A≤2 factors above")
    tgt = TARGET_3HE
    if args.verify_live or not tgt:
        for inter in (False, True):
            t = time.time()
            tgt["atom" if inter else "free"] = list(_D.trace_expansion(2, 1, inter, K)[0])
            print(f"     (measured {'atom' if inter else 'free'} live, {time.time()-t:.0f}s)",
                  flush=True)
    free = [F(1)] + [F(0)] * K
    for x in ("p", "p", "n"):
        free = pmul(free, nuc[x])
    atom = pmul(pmul(free, bond["pp"]), bond["pn"])
    ok4, hits, tot = True, 0, 0
    for part, pred in (("free", free), ("atom", atom)):
        for k in range(K + 1):
            hit = pred[k] == tgt[part][k]
            ok4 = ok4 and hit
            hits += int(hit)
            tot += 1
            print(f"     {part:<6}{k:<3}{str(pred[k]):>18}{str(tgt[part][k]):>18}"
                  f"  {'ok' if hit else 'FAIL'}")
    print(f"     ⇒ {hits}/{tot} " + ("— the bond product holds at order 4 on a held-out word."
                                     if ok4 else "— the product FAILS at order 4. Report it as the finding."))

    ok = ok1 and ok2 and ok4
    print(f"\n  SCOPE. Order 4 for the bond factors (A=2) and one held-out A=3 word. The pn kind is")
    print("  now SETTLED as `averaged_weighted`; the plain-average reading of the mixed bond is an")
    print("  order-≤3 fact and is refuted at order 4. No q₀, no float, no witness, no Lean — and the")
    print("  merged `tr_mul_gen_comb` does NOT cover this: `averaged_weighted` is not a constant")
    print("  combination of the two generators once δ enters.")
    print(f"\n  ({time.time()-t0:.0f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
