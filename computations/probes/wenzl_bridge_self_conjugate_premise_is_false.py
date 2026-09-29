"""The Wenzl-bridge premise `y_λ = w̃_λ on κ_λ = 0` is FALSE — in both
conventions, under every reading of the formula I could construct.

WHAT IS CLAIMED, AND WHERE.  `prop:wedderburn-weight-canonical`
(folio/quantum-observable-universe/mass-theory/wedderburn-weight-canonical)
defines the canonical q-deformed Wedderburn-block weight

    w̃_λ(q)  :=  dim_q(λ)² / [n]_q!

with dim_q the q-deformed Frame-Robinson-Thrall (hook-LENGTH) dimension, and
asserts a "Wenzl-bridge reduction"

    y_λ  =  w̃_λ        whenever  κ_λ = Σ_x c(x) = 0

("the self-conjugate stratum").  In the Lean this is the class field
`WedderburnWeightCanonical.y_eq_self_conjugate`.

IT IS FALSE.  Measured at every κ = 0 partition with n ≤ 6, at the proton q₀,
in BOTH the production convention D and the excised convention C:

    λ           κ    y^D(q₀)      y^C(q₀)      w̃(q₀)       equal?
    (1)         0    1.00000000   1.00000000   1.00000000   yes (trivially)
    (2,1)       0    0.24729789   0.28092963   0.66067377   NO
    (2,2)       0    0.06115624   0.06947330   0.16604895   NO
    (3,1,1)     0    0.00000000   0.01676661   0.29466896   NO
    (3,2,1)     0    0.00000000   0.00731845   0.35863564   NO

Only the trivial one-cell partition satisfies it.  Note that (2,2) and (3,2,1)
are exactly the two partitions the block's own cited script
`computations/_deprecated/bw_wenzl_shadow_equivalence.py` is said to have
verified.

TWO OF THE FOUR FAIL STRUCTURALLY, NOT NUMERICALLY — scope (b).  Convention D
is the 𝔰𝔩₂ point of the Ocneanu family
(`ocneanu_weights_are_sl_n_quantum_dimensions.py`), so y_λ = 0 identically
whenever λ has more than 2 rows: such a λ has a cell of content -2, whose
numerator factor carries [0]_q = 0.  Meanwhile w̃_λ is a ratio of products of
positive quantum integers and is strictly positive for q > 0.  So at (3,1,1)
and (3,2,1) the identity asserts 0 = (something positive) and NO choice of
parameter can reconcile them.  The invariant is the row bound; this is a
structural exclusion, not a near-miss.

(2,1) and (2,2) are scope (a): measured non-equality under every reading I
constructed, which is not the same as every reading that exists.

NO READING OF THE FORMULA RESCUES IT.  Six variants tested against y^D on the
four non-trivial κ = 0 partitions — symmetric vs unbalanced quantum integer,
q-deformed vs ordinary dimension, squared vs unsquared:

    dim_q^sym² / [n]!^sym      dim_ord² / [n]!^sym
    dim_q^unb² / {n}!^unb      dim_ord² / {n}!^unb
    dim_q^sym² / {n}!^unb      dim_q^sym  / [n]!^sym

Every one matches NONE of the four.

THE IMPLEMENTATION IS VALIDATED AGAINST THE CORPUS, not merely self-consistent.
At the partition in question the corpus quotes both convention values, and this
probe's `y` reproduces both: y^D(2,1) = 0.2472978867 against the registered
`1/[2]_q² ≈ 0.2472979`, and y^C(2,1) = 0.28092963 against the `0.2809`
recorded in `qbeta-canonical-markov-weights-explicit-instance-proof`.  So the
disagreement is not an artefact of how the Ocneanu product is coded here.

WHAT THIS DOES *NOT* INVALIDATE — and this is most of the block.
`y_eq_self_conjugate` is a CLASS FIELD, not a theorem: the Lean assumes it.  So
nothing in the corpus is *proved* wrong by its falsity ("conditional-proved ≠
premise-established").  What follows instead:

  * the class has no inhabitant carrying the intended `y` and `w̃` together,
    so any `[WedderburnWeightCanonical R]`-conditional result is vacuous at the
    intended instance rather than false;
  * `WedderburnWeightCanonical.beta_mul_h_eq_neg_C` — the file's one real
    theorem — is UNAFFECTED: its proof is `rw [c.beta_eq, c.C_eq]; ring` and
    never touches the `y` field.  The BW/LP scalings β = -½w̃ and C = w̃·h/2
    are definitional and stand;
  * the block's own off-stratum statement ("y_λ and w̃_λ are genuinely distinct
    weight families") is CORRECT and is, on this evidence, correct on the
    stratum too.

TWO COLLATERAL DEFECTS, both checked here.

  1. The block's `.md` writes the weight as `w_λ(q)` while its `.ts` title and
     its `.lean` both call it `w̃_λ`.  Those are two DIFFERENT registered
     families (notation register §7aa: y_λ / w_λ / w̃_λ are distinct at q ≠ 1),
     so the body conflates its own subject with another family.

  2. The Lean docstring cites
     `computations/probe-wedderburn-weight-scheme.witness.json` for the
     off-stratum ratios "≈0.14 to ≈2.54".  That file DOES NOT EXIST, and
     `git log --all` shows it never existed in tracked history.  It is the only
     evidence the docstring offers for that claim.

Exact symbolic arithmetic (sympy over ℚ(q); convention C in s = √q, where its
expressions are rational).  No floating point except the final display.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import sympy as sp

q = sp.Symbol("q", positive=True)
s = sp.Symbol("s", positive=True)          # s = √q, for convention C
Q0 = sp.Rational("1.1099785827513808")     # proton pin

CHECKS: list[tuple[str, bool]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def sym_int(m, v=q):
    return sp.cancel(sp.together((v ** m - v ** (-m)) / (v - 1 / v)))


def unb_int(m, v=q):
    return sp.cancel((v ** m - 1) / (v - 1))


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def hook(lam, i, j):
    return (lam[i] - j - 1) + sum(1 for r in range(i + 1, len(lam)) if lam[r] > j) + 1


def kappa(lam):
    return sum(j - i for (i, j) in cells(lam))


def qfact(n, f):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= f(k)
    return sp.cancel(sp.together(r))


def dimq_frt(lam, f):
    d = sp.Integer(1)
    for (i, j) in cells(lam):
        d *= f(hook(lam, i, j))
    return sp.cancel(sp.together(qfact(sum(lam), f) / d))


def dim_ordinary(lam):
    d = 1
    for (i, j) in cells(lam):
        d *= hook(lam, i, j)
    return sp.Integer(math.factorial(sum(lam)) // d)


def wtilde(lam):
    """The block's weight as its Lean states it: dim_q(λ)² / [n]_q!."""
    return sp.cancel(sp.together(dimq_frt(lam, sym_int) ** 2 / qfact(sum(lam), sym_int)))


def ocneanu(lam, z, *, var=q, hb=None):
    hb = (var - 1 / var) if hb is None else hb
    zm = z - hb
    num = den = sp.Integer(1)
    for (i, j) in cells(lam):
        c, h = j - i, hook(lam, i, j)
        num *= z * var ** c - zm * var ** (-c)
        den *= var ** h - var ** (-h)
    return sp.cancel(sp.together(num / den))


STRATUM = [(2, 1), (2, 2), (3, 1, 1), (3, 2, 1)]   # every κ=0, n≤6, minus (1,)


def main() -> int:
    print("=" * 74)
    print("  THE WENZL-BRIDGE PREMISE IS FALSE ON ITS OWN STRATUM")
    print("=" * 74)
    print()

    root = Path(__file__).resolve().parents[2]
    blk = root / "folio" / "quantum-observable-universe" / "mass-theory"

    # ---- 0. what the block claims ------------------------------------------
    lean = (blk / "wedderburn-weight-canonical.lean")
    ltxt = lean.read_text() if lean.exists() else ""
    # 2026-09-04: the field was DROPPED on the owner's ruling (option A of the
    # three dispositions).  The check now guards the drop: the class must no
    # longer carry the field, and the module docstring must record why.
    field_line = any(l.strip().startswith("y_eq_self_conjugate :") for l in ltxt.splitlines())
    check("the block NO LONGER carries y_λ = w̃_λ on κ_λ = 0 as a class field "
          "(dropped 2026-09-04, owner ruling A)",
          "class WedderburnWeightCanonical" in ltxt and not field_line
          and "DROPPED" in ltxt and "y_self_conjugate" not in ltxt.split("class WedderburnWeightCanonical",1)[1],
          "it was a class field until 2026-09-04 — assumed, not proved — so nothing "
          "in the corpus was ever *proved* wrong by its falsity; now nothing asserts it")

    # ---- 1. the stratum is exactly what I test ------------------------------
    found = [lam for n in range(1, 7) for lam in partitions(n) if kappa(lam) == 0]
    check("κ = 0 for n ≤ 6 is exactly {(1)} ∪ the four tested",
          found == [(1,)] + sorted(STRATUM, key=lambda l: (sum(l), l), reverse=False)
          or set(found) == {(1,)} | set(STRATUM),
          f"{found}")

    # ---- 2. the measurement, both conventions -------------------------------
    zD = q ** 2 / sym_int(2)
    qs, hs = s ** 2, s ** 2 - 1 / s ** 2
    zC = s / (1 + s ** 2)
    s0 = sp.sqrt(Q0)

    print()
    print(f"    {'λ':<12}{'y^D(q0)':>13}{'y^C(q0)':>13}{'w̃(q0)':>13}   D=w̃  C=w̃")
    rowsD, rowsC = [], []
    for lam in [(1,)] + STRATUM:
        yD = ocneanu(lam, zD)
        yC = ocneanu(lam, zC, var=qs, hb=hs)
        w = wtilde(lam)
        eqD = sp.simplify(sp.cancel(yD - w)) == 0
        eqC = sp.simplify(sp.cancel(sp.together(yC - w.subs(q, qs)))) == 0
        rowsD.append(eqD)
        rowsC.append(eqC)
        print(f"    {str(lam):<12}{float(sp.N(yD.subs(q, Q0), 12)):>13.8f}"
              f"{float(sp.N(yC.subs(s, s0), 12)):>13.8f}"
              f"{float(sp.N(w.subs(q, Q0), 12)):>13.8f}   "
              f"{str(eqD):<5} {eqC}")
    print()
    check("convention D: the bridge holds ONLY at the trivial (1)",
          rowsD[0] and not any(rowsD[1:]),
          "fails at (2,1), (2,2), (3,1,1), (3,2,1)")
    check("convention C: it fails there too — this is not a convention issue",
          rowsC[0] and not any(rowsC[1:]))

    # ---- 3. two of them fail STRUCTURALLY (scope b) --------------------------
    threerow = [lam for lam in STRATUM if len(lam) > 2]
    zeroD = all(sp.simplify(ocneanu(lam, zD)) == 0 for lam in threerow)
    posw = all(sp.N(wtilde(lam).subs(q, Q0), 20) > 0 for lam in threerow)
    check("scope (b): at >2-row κ=0 partitions the identity asserts 0 = positive",
          zeroD and posw and len(threerow) == 2,
          f"{threerow}: y^D = 0 by the 𝔰𝔩₂ row bound (a cell of content -2 "
          f"carries [0]_q = 0), while w̃ > 0 as a ratio of positive quantum "
          f"integers — no parameter can reconcile them")

    # ---- 4. no reading of the formula rescues it ----------------------------
    variants = {
        "dim_q^sym² / [n]!^sym": lambda l: dimq_frt(l, sym_int) ** 2 / qfact(sum(l), sym_int),
        "dim_q^unb² / {n}!^unb": lambda l: dimq_frt(l, unb_int) ** 2 / qfact(sum(l), unb_int),
        "dim_q^sym² / {n}!^unb": lambda l: dimq_frt(l, sym_int) ** 2 / qfact(sum(l), unb_int),
        "dim_ord²   / [n]!^sym": lambda l: dim_ordinary(l) ** 2 / qfact(sum(l), sym_int),
        "dim_ord²   / {n}!^unb": lambda l: dim_ordinary(l) ** 2 / qfact(sum(l), unb_int),
        "dim_q^sym  / [n]!^sym": lambda l: dimq_frt(l, sym_int) / qfact(sum(l), sym_int),
    }
    survivors = {n: [str(l) for l in STRATUM
                     if sp.simplify(sp.cancel(ocneanu(l, zD) - f(l))) == 0]
                 for n, f in variants.items()}
    check("no reading of w̃ = dim_q²/[n]! satisfies the bridge",
          all(not v for v in survivors.values()),
          "; ".join(f"{n}: {v or 'none'}" for n, v in survivors.items()))

    # ---- 5. the implementation is validated against the corpus --------------
    yD21 = sp.N(ocneanu((2, 1), zD).subs(q, Q0), 12)
    yC21 = sp.N(ocneanu((2, 1), zC, var=qs, hb=hs).subs(s, s0), 12)
    check("this probe's y reproduces the corpus's own quoted values at (2,1)",
          abs(float(yD21) - 0.2472979) < 1e-6 and abs(float(yC21) - 0.2809) < 1e-4,
          f"y^D = {float(yD21):.10f} vs registered 1/[2]_q² ≈ 0.2472979; "
          f"y^C = {float(yC21):.8f} vs the 0.2809 recorded for convention C")

    # ---- 6. what survives ---------------------------------------------------
    check("the file's one real theorem does NOT depend on the false field",
          "rw [c.beta_eq, c.C_eq]" in ltxt,
          "beta_mul_h_eq_neg_C uses beta_eq and C_eq only — the BW/LP scalings "
          "β = -½w̃ and C = w̃·h/2 are definitional and stand")

    # ---- 7. two collateral defects -----------------------------------------
    md = (blk / "wedderburn-weight-canonical.md").read_text()
    ts = (blk / "wedderburn-weight-canonical.ts").read_text()
    # NB the .ts is a TypeScript string literal, so its backslashes are
    # DOUBLED on disk ("\\tilde"); the .md is raw markdown, single.  Matching
    # on the escaped form is what a first pass gets wrong here.
    check("the .md conflates w̃_λ with w_λ, two distinct registered families",
          "w_\\lambda(q)" in md and "tilde w" in ltxt and "tilde w_" in ts,
          "notation register §7aa: y_λ / w_λ / w̃_λ are distinct at q ≠ 1; the "
          ".ts title and the .lean both say w̃, the body says w")
    dead = root / "computations" / "probe-wedderburn-weight-scheme.witness.json"
    check("the Lean's cited off-stratum witness DOES NOT EXIST",
          "probe-wedderburn-weight-scheme.witness.json" in ltxt and not dead.exists(),
          "git log --all shows it never existed in tracked history; it is the "
          "only evidence the docstring offers for the ≈0.14–2.54 ratios")

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print()
    print("=" * 74)
    print(f"  {n_ok}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  The premise is false, in both conventions, under every")
    print("  reading tested; at the >2-row κ=0 partitions it is structurally")
    print("  false (0 = positive) and cannot be repaired by any parameter.  It was")
    print("  a CLASS FIELD, so nothing proved was invalidated — but the class had")
    print("  no inhabitant at the intended values, and the BW/LP scalings, which")
    print("  are definitional, are untouched.  DISPOSITION TAKEN 2026-09-04")
    print("  (owner ruling, option A): the field and its projection theorem are")
    print("  DROPPED; `y` stays in the class as data only.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
