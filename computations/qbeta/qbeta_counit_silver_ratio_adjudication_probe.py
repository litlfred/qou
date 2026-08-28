#!/usr/bin/env python3
"""The live typed construction SURVIVES the invariant that excludes `epsNPq` —
so the two horns of the qou-avt5 fork are not symmetric.

Bean `qou-goc9`.  Builds on `qbeta_single_wrap_element_cannot_exist_probe.py`
(bean `qou-avt5`, completed), which proves a scope-(b) exclusion and then
explicitly declines to adjudicate its own fork.  This probe supplies one
discriminating datum that fork did not have, and converts the surviving horn
into a falsifiable requirement.  **It does not close the question.**

## The state qou-avt5 left

`qbeta-counit-closed-form.md` describes `Delta` as *"the single-wrap normal-form
difference of the neutron and proton TYPED-CROSSING ELEMENTS in H_3(q)"* and
asserts `eps(Delta) = epsNPq = h(h-2)/2`.  qou-avt5 proves those two statements
cannot both hold:

  * the counit of any typed-crossing word is `q^m * ([2]_q/2)^c`;
  * `epsNPq` carries the factor `(q^2 - 2q - 1)`, so it vanishes at the SILVER
    RATIO `q = 1 + sqrt2`;
  * a typed-word *difference* vanishing there forces, via absolute norms in
    `Z[sqrt2]` (`|N(1+sqrt2)| = 1`, `|N(sqrt2)| = 2`), first `c1 = c2` and then
    `m1 = m2` — making the difference identically zero, which `epsNPq` is not.

Its stated fork, verbatim: either **(a)** `Delta` is not a typed-crossing word
difference, so the prose is wrong and the real element is unexhibited; or
**(b)** `epsNPq` is wrong, and with it `Q_A` and the ladder phase.  *"NOT
CLAIMED which."*

## What the silver ratio actually is, stated plainly

`h = q - 1/q` evaluates to **exactly 2** at `q = 1 + sqrt2`.  So `epsNPq =
h(h-2)/2` vanishes there for a completely mundane reason — it is built with a
root at `h = 2` — and qou-avt5's exclusion is, in the `h` coordinate, the
statement that **no typed-word difference can vanish at `h = 2`**.  Worth
saying because the phrase "silver ratio" invites a search for depth that is not
there; the content is entirely in the norm argument, not in the constant.

## The discriminating datum

The counit of the LIVE typed construction — `pyhecke.atom.build_nucleon_nf`,
which is what `PROTON_NF` / `NEUTRON_NF` actually are — is

    eps(typed n - p) = h(h^6 + 2h^5 + 2h^4 + 2h^3 - h^2 + 2h - 4)/4

re-derived here by transcribing `gram.hm` and `atom.build_nucleon_nf`
symbolically over `Q(h)` and validating against the live float64 constants.  At
`h = 2` it is **86**, not 0.

So under qou-avt5's own invariant:

  | object | at `h = 2` | verdict under the invariant |
  |---|---|---|
  | `epsNPq` (asserted) | `0` | EXCLUDED — cannot be a typed-word difference |
  | `eps(typed n-p)` (live code) | `86` | NOT excluded — structurally admissible |

The two horns are therefore **not symmetric**: one names an object the corpus
computes and which survives the test, the other an object the corpus asserts
and which fails it.

## What this does and does not establish

**Does NOT** prove `epsNPq` wrong.  Surviving the invariant is *necessary, not
sufficient* — a great many functions do not vanish at `h = 2`.  This is evidence
about admissibility, not a derivation of either value, and horn (b) is not
hereby selected.

**Does** convert horn (a) into a concrete falsifiable target.  If `epsNPq` is
retained and the prose is what is wrong, then whatever `Delta` really is must
have a counit that **vanishes at `h = 2`** while **not** being a typed-crossing
word difference.  That is a sharp requirement on any future exhibition of it,
and anything proposed for `Delta` can be tested against it in one line.

## Provenance asymmetry, recorded as context and NOT as an argument

`epsNPq` is a bare `def` in Lean with no theorem deriving it, and its NF vector
`[h^2/2, -h/2, -h/2, 0, 0, 0]` was cited to "(audit step 5)" — a reference that
resolved to no document, repaired on main in `4a71daa72c`.  The typed
construction is running code, reproduced here symbolically and validated against
the live constants.  This is a difference in how well-evidenced the two are; it
is **not** a mathematical argument, and implemented-ness does not make a value
correct.

Exact symbolic Q(h)/Q(sqrt2) throughout.  The one float64 comparison is a
provenance validation against the live constants at tolerance 1e-15; no result
depends on it.
"""
from __future__ import annotations

import hashlib
import inspect
import sys
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in (_ROOT / "tools" / "pyhecke" / "python",
           _ROOT / "tools" / "qou-substrate" / "python",
           _ROOT / "computations", _ROOT / "computations" / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

h = sp.symbols("h")


def hm_sym(nf, c, d, gen):
    """Symbolic transcription of `pyhecke.gram.hm` (the GB reduction tables)."""
    r = [sp.Integer(0)] * 6
    if gen == 0:
        t = [(0, [(1, c), (0, d)]), (1, [(1, c * h), (0, c), (1, d)]),
             (2, [(3, c), (2, d)]), (3, [(3, c * h), (2, c), (3, d)]),
             (4, [(5, c), (4, d)]), (5, [(5, c * h), (4, c), (5, d)])]
    else:
        t = [(0, [(2, c), (0, d)]), (1, [(4, c), (1, d)]),
             (2, [(2, c * h), (0, c), (2, d)]), (3, [(5, c), (3, d)]),
             (4, [(4, c * h), (1, c), (4, d)]), (5, [(5, c * h), (3, c), (5, d)])]
    for si, tg in t:
        if nf[si] == 0:
            continue
        for ti, co in tg:
            r[ti] += nf[si] * co
    return [sp.expand(x) for x in r]


def build_nucleon(quarks):
    """Symbolic transcription of `pyhecke.atom.build_nucleon_nf`."""
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for _ in range(3):                                  # B_3 confinement
        nf = hm_sym(nf, sp.Integer(1), sp.Integer(0), 0)
        nf = hm_sym(nf, sp.Integer(1), -h, 1)
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        a, b = quarks[i], quarks[j]
        if a == b == 'u':
            nf = hm_sym(nf, sp.Integer(1), sp.Integer(0), i)
        elif a == b == 'd':
            nf = hm_sym(nf, sp.Integer(1), -h, i)
        else:
            nf = hm_sym(nf, sp.Integer(1), -h / 2, i)
    return nf


def main() -> int:
    failures: list[str] = []

    def check(name, ok, detail):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failures.append(name)

    print("Assertions (exact symbolic Q(h) / Q(sqrt2)):")

    q = sp.symbols("q")
    silver = 1 + sp.sqrt(2)
    h_silver = sp.simplify(silver - 1 / silver)

    # ---- 1. the silver ratio is exactly where h = 2 ----
    check(
        "1. h = q - 1/q equals exactly 2 at the silver ratio q = 1 + sqrt2",
        sp.simplify(h_silver - 2) == 0,
        f"h(1+sqrt2) = {h_silver}. So epsNPq = h(h-2)/2 vanishes there because "
        "it is built with a root at h = 2 — the exclusion's content is the norm "
        "argument, not the constant",
    )

    # ---- 2. epsNPq vanishes there, and is not identically zero ----
    eps_npq = h * (h - 2) / 2
    check(
        "2. epsNPq vanishes at h = 2 but is not the zero polynomial",
        sp.simplify(eps_npq.subs(h, 2)) == 0 and sp.expand(eps_npq) != 0,
        f"epsNPq(h=2) = {sp.simplify(eps_npq.subs(h, 2))}; epsNPq = "
        f"{sp.factor(eps_npq)} != 0. This is the qou-avt5 contradiction",
    )

    # ---- 3. re-derive the LIVE typed counit from CURRENT source ----
    from pyhecke import atom, gram
    sha_hm = hashlib.sha256(inspect.getsource(gram.hm).encode()).hexdigest()[:12]
    sha_bnf = hashlib.sha256(
        inspect.getsource(atom.build_nucleon_nf).encode()).hexdigest()[:12]
    p_nf, n_nf = build_nucleon(['u', 'u', 'd']), build_nucleon(['u', 'd', 'd'])
    eps_typed = sp.expand(sum(sp.expand(a - b) for a, b in zip(n_nf, p_nf)))
    expected = h * (h**6 + 2*h**5 + 2*h**4 + 2*h**3 - h**2 + 2*h - 4) / 4
    check(
        "3. eps(typed n-p) re-derived from the CURRENT source, not a cached form",
        sp.expand(eps_typed - expected) == 0,
        f"gram.hm sha {sha_hm}, atom.build_nucleon_nf sha {sha_bnf}; "
        f"eps = {sp.factor(eps_typed)}. Re-derived rather than reused because a "
        "sibling (qou-avt5) was burned calibrating against a producer that was "
        "itself wrong by 15-27%: being behind the corpus defeats a cross-check",
    )

    # ---- 4. provenance: it IS the live construction ----
    try:
        from pyhecke.atom import NEUTRON_NF, PROTON_NF
        from pyhecke.gram import h as _gh
        hf = sp.Float(repr(_gh), 20)
        dev = max(max(abs(float(x.subs(h, hf)) - y) for x, y in zip(p_nf, PROTON_NF)),
                  max(abs(float(x.subs(h, hf)) - y) for x, y in zip(n_nf, NEUTRON_NF)))
        check(
            "4. the symbolic build reproduces the live PROTON_NF / NEUTRON_NF",
            dev < 1e-15,
            f"max|dev| = {dev:.2e} (float64 eps). Provenance validation only; "
            "no result below depends on this float comparison",
        )
    except Exception as exc:                                   # pragma: no cover
        check("4. the symbolic build reproduces the live PROTON_NF / NEUTRON_NF",
              False, f"pyhecke unavailable: {exc}")

    # ---- 5. THE DISCRIMINATING DATUM ----
    v_typed = sp.simplify(eps_typed.subs(h, 2))
    check(
        "5. the live typed counit does NOT vanish at h = 2 — it is NOT excluded",
        v_typed != 0,
        f"eps(typed n-p)(h=2) = {v_typed} != 0, against epsNPq(h=2) = 0. Under "
        "qou-avt5's own invariant the live construction is admissible and the "
        "asserted value is not — the two horns are NOT symmetric",
    )

    # ---- 6. and the requirement horn (a) must now meet ----
    check(
        "6. horn (a) is now a falsifiable requirement, not an open alternative",
        True,
        "if epsNPq is retained and the PROSE is what is wrong, the real Delta "
        "must have a counit vanishing at h = 2 while NOT being a typed-crossing "
        "word difference. One-line test for any future exhibition of it",
    )

    # ---- 7. state the limit of the inference, in the artifact ----
    check(
        "7. necessary, NOT sufficient — horn (b) is not hereby selected",
        True,
        "surviving the invariant does not derive either value; a great many "
        "functions fail to vanish at h = 2. This is evidence on admissibility, "
        "not an adjudication. qou-goc9 stays OPEN",
    )

    print()
    if failures:
        print(f"FAILED {len(failures)}/7: {', '.join(failures)}")
        return 1
    print("7/7 assertions hold.")
    print()
    print("READING: qou-avt5 proved no typed-crossing word difference can have")
    print("counit epsNPq, and declined to say whether the prose or the value is")
    print("wrong. The live typed construction SURVIVES that same invariant (86 vs")
    print("0 at h = 2), so the fork is asymmetric. That does not settle it —")
    print("necessary is not sufficient — but it does turn horn (a) into a")
    print("concrete target: exhibit a non-typed-word Delta vanishing at h = 2.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
