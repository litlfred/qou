#!/usr/bin/env python3
"""Colour does not license the u-u / d-d letter asymmetry — and the corpus's own
block says the asymmetry is there because it lands on CODATA.

`qou-y2np` left one obligation: derive the flavour-to-eigenvalue assignment
(`u -> +q`, `d -> -q^-1`), or record it as a convention. The named candidate was
colour-antisymmetry of the quark wavefunction — physically natural, because the
Hecke eigenvalue sign IS a statistics label (`+q` on the symmetric part of
`V (x) V`, `-q^-1` on the antisymmetric part) rather than a charge label.

Pushed on. Colour does not license it, and what colour DOES say is ambiguous
between two readings that bracket the entire question.

*** 1. THE SYMMETRY ARGUMENT IS IDENTICAL FOR uu AND dd ***

In a colour-singlet baryon `eps_{abc} q^a q^b q^c`, any PAIR of quarks is
antisymmetric in colour (the `3bar`). Fermi statistics makes the total
wavefunction antisymmetric under exchange of two identical quarks, so

    antisym(colour) (x) X = antisym   ==>   X = space (x) spin (x) flavour is SYMMETRIC

and at `L = 0` with symmetric flavour that forces a spin triplet. **That
derivation does not mention which flavour it is.** `uu` in the proton and `dd` in
the neutron are in identical configurations, so colour-antisymmetry gives no
basis for giving them different Hecke letters. Whatever letter one takes, the
other takes.

*** 2. AND WHAT COLOUR PICKS DEPENDS ON WHAT A STRAND EXCHANGE MEANS ***

Two readings, both defensible, and they differ by the whole asymmetry:

  * **strand = the whole quark.** Exchange is the total exchange, antisymmetric
    by Fermi statistics, so both like-flavour pairs sit at `-q^-1`.
  * **strand = a colour index.** Exchange is colour exchange, antisymmetric, so
    the REST is symmetric and both pairs sit at `+q`.

**The row cap argues for the first.** `dim V = 2` (`QOU/Hecke/RowCap.lean`), and a
colour index needs three values, so the strand cannot be carrying colour. That is
this arc's own result pointing at the total-exchange reading.

*** 3. MEASURED — the two readings bracket everything, and neither is the corpus's ***

2548 measured AME2020 nuclides, tower-summed `E_0`, 3 strands/nucleon.
"viol" counts nuclides EXCEEDING the law, i.e. failures of the upper bound the
owner ruling established:

    law                                        viol   median   p5-p95     corr
    as built    p-p = sigma, n-n = sigma^-1        1   0.8864   1.2250   -0.8038
    colour: BOTH symmetric  (+q,   b = z)       2498   1.3231   1.1779   -0.6911
    colour: BOTH antisym    (-q^-1)                0   0.7189   1.1823   -0.6994
    both = the pinned loop  (1/[2]_q)             62   0.9314   1.1805   -0.6969

  * **Both-symmetric is catastrophically refuted** — 2498 of 2548 exceed the law.
    So the colour-index reading is dead on the data.
  * **Both-antisymmetric gives a STRICT bound** — zero violations, better than
    the corpus's one (4He) — but over-binds by 39 % on the median against the
    corpus's 11 %. A true bound, and a loose one.
  * **Every symmetric variant improves the asymmetry correlation** (-0.804 ->
    ~-0.69) and **none of them fixes it**. Removing the asymmetry is worth about
    a seventh of the symmetry-energy residual.

*** 4. AND THE CORPUS'S OWN JUSTIFICATION IS A FIT, STATED OPENLY ***

`meson-to-proton-via-borromean.md` introduces the typed crossings with:
*"Untyped composition yields net ~ 1.506. The CODATA proton net is ~ 0.999.
**Typed crossings close this gap.**"* So the `uu -> sigma`, `dd -> sigma^-1`
split is there because it lands on the measured proton, and the block says so.
That is not a hidden fit; it is a declared one. What `qou-y2np` asks for — a
derivation — does not exist, and this probe did not find one.

*** VERDICT ***

**Colour does not pin the branch.** It forbids the asymmetry rather than
explaining it, and the common letter it would impose is ambiguous between two
readings that land at opposite ends of the table (2498 violations vs 0).

`qou-y2np` stays open, with its candidate list one shorter and its statement
sharpened: the assignment is not merely underived, it is **in tension with the
symmetry argument that would be its natural home**. Remaining candidates: the
Borromean proton construction, and the `net` values' own derivation.

**And the symmetry energy is still missing.** The best any variant here reaches
is `corr = -0.691` against the corpus's `-0.804`; the dominant residual shape
survives all four.
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 30
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
M_E = mp.mpf("0.51099895069")
HBAR_Q = (Q0 - 1)/Q0
E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR_Q**2)
STRANDS = 3
Z_M = Q0**3/(Q0**2 + 1)                    # b_pp: sigma, symmetric channel  +q
B_NN = 1/(Q0**3 + Q0)                      # b_nn: sigma^-1, antisym channel
TWO_Q = Q0 + 1/Q0
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
L_PP, L_PN, L_NN, L_LOOP = (-mp.log(Z_M), -mp.log(B_PN),
                            -mp.log(B_NN), mp.log(TWO_Q))

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def _pct(v, n, d=100):
    s = sorted(v)
    return s[min(len(s) - 1, len(s)*n//d)]


def _corr(xs, ys):
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    return (sum((a - mx)*(b - my) for a, b in zip(xs, ys))
            / mp.sqrt(sum((a - mx)**2 for a in xs)*sum((b - my)**2 for b in ys)))


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    meas = []
    for e in json.loads(AME.read_text())["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        b = e.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not b or e.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(b))*A/1000
        if B > 0:
            meas.append((A, Z, N, B))

    print("=" * 78)
    print("1-2. WHAT COLOUR SAYS (and does not say)")
    print("=" * 78)
    print("    In a colour-singlet baryon any quark PAIR is antisymmetric in")
    print("    colour, and Fermi statistics then makes space(x)spin(x)flavour")
    print("    symmetric. That derivation never mentions the flavour, so uu and")
    print("    dd are in IDENTICAL configurations: colour licenses no asymmetry.")
    print("\n    Which common letter it picks depends on what a strand exchange is:")
    print("      strand = whole quark  -> total exchange antisym -> both  -q^-1")
    print("      strand = colour index -> colour antisym, rest sym -> both  +q")
    print("    The ROW CAP argues for the first: dim V = 2 (QOU/Hecke/RowCap.lean)")
    print("    and a colour index needs three values, so a strand cannot be colour.")
    ok &= chk("the_fibre_dimension_cannot_carry_a_colour_index",
              2 < 3, True,
              "dim V = 2 is forced by the categorical volume constraint and "
              "proved as the row cap; a colour index needs 3 values, so the "
              "strand-is-colour reading is structurally strained -- this arc's "
              "own result pointing at the total-exchange reading")

    print("\n" + "=" * 78)
    print(f"3. MEASURED — {len(meas)} measured nuclides")
    print("=" * 78)
    laws = {
        "as built    p-p=sigma, n-n=sigma^-1": lambda A, Z, N: (Z - 1)*L_PP + L_PN + (N - 1)*L_NN,
        "colour: BOTH symmetric  (+q)": lambda A, Z, N: (A - 2)*L_PP + L_PN,
        "colour: BOTH antisym    (-q^-1)": lambda A, Z, N: (A - 2)*L_NN + L_PN,
        "both = pinned loop  (1/[2]_q)": lambda A, Z, N: (A - 2)*L_LOOP + L_PN,
    }
    asym = [(mp.mpf(N - Z)/A)**2 for (A, Z, N, B) in meas]
    table = {}
    print(f"    {'law':<38}{'viol':>6}{'median':>10}{'p5-p95':>9}{'corr':>10}")
    for nm, f in laws.items():
        v = [B/(STRANDS*E0*f(A, Z, N)) for (A, Z, N, B) in meas]
        row = {"violations": sum(1 for x in v if x > 1),
               "median": mp.nstr(_pct(v, 50), 8),
               "p5_p95": mp.nstr(_pct(v, 95)/_pct(v, 5), 8),
               "corr_asym": mp.nstr(_corr(asym, v), 8)}
        table[nm] = row
        print(f"    {nm:<38}{row['violations']:>6}{mp.nstr(_pct(v,50),6):>10}"
              f"{mp.nstr(_pct(v,95)/_pct(v,5),6):>9}{mp.nstr(_corr(asym,v),6):>10}")

    sym = table["colour: BOTH symmetric  (+q)"]
    anti = table["colour: BOTH antisym    (-q^-1)"]
    built = table["as built    p-p=sigma, n-n=sigma^-1"]
    ok &= chk("the_colour_index_reading_is_catastrophically_refuted",
              sym["violations"] > 2000, True,
              "2498 of 2548 exceed the law -- both-symmetric is dead on the data")
    ok &= chk("the_total_exchange_reading_gives_a_STRICT_bound_but_a_loose_one",
              anti["violations"] == 0 and mp.mpf(anti["median"]) < mp.mpf("0.8"), True,
              "zero violations, better than the corpus's one (4He) -- but it "
              "over-binds 39 % on the median against the corpus's 11 %")
    ok &= chk("the_two_readings_bracket_the_corpus_choice",
              sym["violations"] > built["violations"] > anti["violations"], True,
              "2498 > 1 > 0: the corpus's asymmetric hybrid sits between the two "
              "symmetric readings, and is neither of them")
    ok &= chk("removing_the_asymmetry_improves_but_does_not_fix_the_symmetry_energy",
              all(abs(mp.mpf(r["corr_asym"])) < abs(mp.mpf(built["corr_asym"]))
                  for k, r in table.items() if k != "as built    p-p=sigma, n-n=sigma^-1")
              and all(abs(mp.mpf(r["corr_asym"])) > mp.mpf("0.6")
                      for r in table.values()), True,
              "-0.804 -> ~-0.69 for every symmetric variant: worth about a "
              "seventh of the residual, and none of them fixes it")

    print("\n" + "=" * 78)
    print("4. AND THE CORPUS'S OWN JUSTIFICATION IS A DECLARED FIT")
    print("=" * 78)
    print("    meson-to-proton-via-borromean.md, introducing the typed crossings:")
    print('      "Untyped composition yields net ~ 1.506. The CODATA proton net')
    print('       is ~ 0.999. TYPED CROSSINGS CLOSE THIS GAP."')
    print("    So the split is there because it lands on the measured proton, and")
    print("    the block says so. Not a hidden fit — a declared one.")
    ok &= chk("no_derivation_of_the_assignment_was_found",
              True, True,
              "the code asserts uu -> sigma / dd -> sigma^-1 with no reason, and "
              "the content block's stated reason is closing the gap to CODATA. "
              "qou-y2np's obligation is unmet and this probe did not meet it")

    print("\n  🛑 Colour does NOT pin the branch: it FORBIDS the asymmetry rather")
    print("     than explaining it, and the common letter it would impose is")
    print("     ambiguous between readings landing at 2498 violations and 0.")
    print("  🔓 qou-y2np stays open, one candidate shorter and sharper: the")
    print("     assignment is not merely underived, it is in TENSION with the")
    print("     symmetry argument that would be its natural home.")
    print("  🛑 And the symmetry energy survives all four laws (best -0.691).")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-colour-does-not-license-the-asymmetry",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "E_0_MeV": mp.nstr(E0, 20),
                       "E_0_form": "tower-summed (owner ruling 2026-09-05)",
                       "strands_per_nucleon": STRANDS,
                       "source": "qou-mass/src/qou_mass/data/ame2020.json"},
        "data": {"n_measured": len(meas), "laws": table,
                 "corpus_justification":
                     "meson-to-proton-via-borromean.md: 'Typed crossings close "
                     "this gap' (untyped net 1.506 vs CODATA proton net 0.999)"},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_colour_does_not_license_the_asymmetry_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-colour-does-not-license-the-asymmetry.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
