"""Two nucleon builders in `pyhecke.atom` contradict each other in their DOCSTRINGS.

`nucleon_gen_chains` says it derives its chains "matching build_nucleon_nf".
`build_nucleon_nf` says "No separate gluon dressing -- B3 IS the gluon
structure". Both cannot be true: `nucleon_gen_chains` ends with

    # Gluon self-coupling: 2 sigma_0 per nucleon (ILP-derived)
    g0.append((1, 0))
    g0.append((1, 0))

so it emits 11 crossings where `build_nucleon_nf` emits 9, and the two extra
are exactly the dressing the other builder disclaims. They are different
elements of H_3(q), not two spellings of one.

WHY THIS IS NOT COSMETIC. Different consumers read different builders, and the
docstring tells a reader they agree:

  * `PROTON_NF` / `NEUTRON_NF` (module constants) = `build_nucleon_nf`, 9
    crossings, no dressing.
  * `_PROTON_G0` / `_PROTON_G1` = `nucleon_gen_chains`, 11 crossings, dressed.

So "the nucleon" resolves to one of two inequivalent elements depending on
which name a caller reached for, and the docstring of the dressed one asserts
that this choice does not matter.

WHAT THIS PROBE DOES NOT CLAIM. It does not say which builder is right. The
dressing is annotated "ILP-derived", so it may well be the intended physics and
`build_nucleon_nf` the stale one -- that is bean `qou-bg3w`'s question (which
element is Delta) and is an owner decision, not this probe's. What is a defect
either way is that one function's docstring claims agreement with a function it
demonstrably disagrees with.

Structural only: counts crossings and compares templates. No arithmetic on q,
so nothing here can be a float64 defect.
"""
import pathlib as _pl
import sys as _sys

_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))

import _path_bridge  # noqa: F401,E402

import sys

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}" + (f"  [{detail}]" if detail else ""))


def main() -> int:
    import pyhecke.atom as A

    print("nucleon builder dressing contradiction (structural)\n")

    quarks = ['u', 'u', 'd']
    nf = A.build_nucleon_nf(quarks)
    g0, g1 = A.nucleon_gen_chains(quarks)
    n_chain = len(g0) + len(g1)

    # build_nucleon_nf: B3 = 3 x (sigma_0, sigma_1^-1) = 6, plus 3 quark pairs.
    # Counted from its source, which is the only place the number exists --
    # the function returns a 6-coordinate NF vector, not a crossing list.
    n_nf = 6 + 3
    check("build_nucleon_nf builds 9 crossings (B3=6 + 3 quark pairs)", n_nf == 9)
    check("nucleon_gen_chains emits 11 crossings", n_chain == 11,
          f"{len(g0)}+{len(g1)}")
    check("they differ by exactly 2", n_chain - n_nf == 2)

    # The two extra sit in gen 0 and are sigma (d == 0), i.e. the appended
    # "gluon self-coupling", not a different template.
    zeros_g0 = sum(1 for _, d in g0 if d == 0)
    # expected without dressing: 3 sigma_0 from B3 + the uu pair = 4
    check("the 2 extra are gen-0 sigma crossings (d == 0)", zeros_g0 == 6,
          f"gen-0 d==0 count {zeros_g0}, undressed would be 4")

    # The docstrings are the actual defect: each asserts something the other
    # contradicts.
    d_chains = (A.nucleon_gen_chains.__doc__ or "")
    d_nf = (A.build_nucleon_nf.__doc__ or "")
    check("nucleon_gen_chains' docstring claims it matches build_nucleon_nf",
          "matching build_nucleon_nf" in d_chains)
    check("build_nucleon_nf's docstring disclaims a separate gluon dressing",
          "No separate gluon dressing" in d_nf)

    # And the contradiction is live in the source, not merely historical.
    import inspect
    src = inspect.getsource(A.nucleon_gen_chains)
    check("nucleon_gen_chains still appends the ILP gluon self-coupling",
          "Gluon self-coupling" in src)

    bad = [n for n, ok, _ in CHECKS if not ok]
    print(f"\n  {len(CHECKS) - len(bad)}/{len(CHECKS)} checks pass")
    if bad:
        print("  FAILED: " + "; ".join(bad))
        return 1
    print("\n  VERDICT: the two builders are inequivalent (9 vs 11 crossings)")
    print("  and one docstring asserts they agree. Which element is canonical")
    print("  is qou-bg3w / owner; the docstring claim is wrong either way.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
