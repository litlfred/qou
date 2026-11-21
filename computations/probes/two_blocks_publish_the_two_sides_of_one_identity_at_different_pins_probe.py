#!/usr/bin/env python3
"""`prop:alpha-em-categorical-trace-ratio` proves an identity with
`prop:em-coupling-projection` and publishes the two sides at DIFFERENT pins.

WHY THIS EXISTS
---------------
`scripts/witness-block-agreement.py` flagged this block 4/5, and the
candidate-producer sweep singled it out: of **3277 live witnesses, none covers
more than 1 of its 4 figures.** Every other flagged block had a plausible
producer somewhere. That signature — no carrier anywhere — is what an
unproduced figure looks like, so it was worth the derived-provenance test rather
than another pointer hunt.

The figures turn out to be produced by nothing because **the whole corpus
computes this quantity at the other pin.**

THE FINDING
-----------
The block proves

    alpha_EM  =  h^2 / (q * delta_q(T_2,9) * delta_q(T_3,5))  =  1/(q [9]_q [10]_q)

and the identity is **exact at any q** — verified below to 1e-53, as it must be,
since `delta_q(T_2,9) = h[9]_q` and `delta_q(T_3,5) = h[10]_q` and the two `h`
cancel the `h^2`. It is an algebraic restatement, not an approximation.

It then cites `prop:em-coupling-projection` for the right-hand side. **That block
publishes the right side at the PROTON pin and says so explicitly; this block
publishes the left side at a MUON pin.** So the two sides of a proven identity
are published as different numbers:

    prop:em-coupling-projection        1/(q[9][10]) = 7.30870156e-3   PROTON
    prop:alpha-em-categorical-trace..  h^2/(q d9 d10) = 7.30870098e-3   MUON

a `7.94e-8` relative disagreement between two quantities the corpus has proved
equal. Not a rounding difference and not a convention: one identity, two pins.

WHICH PIN, MEASURED RATHER THAN ASSUMED
----------------------------------------
All four of the block's table figures are tested against every registered `q0` by
the only test that means anything here — does the pin's value **round to** the
published figure at its own decimal count?

    pin          h      d9     d10   alpha     verdict
    proton       x       x       x       x     0/4  -- DECISIVELY EXCLUDED
    muon (live)  ok      ok      ok      ok    4/4
    retired      ok      ok      ok      ok    4/4
    frozen A     ok      ok      ok      ok    4/4

The proton pin misses by `1.0e-7` to `1.5e-7`, ten to a thousand times the muon
family's residuals. There is no ambiguity about the family.

**The VINTAGE is undeterminable and this probe does not guess it.** The three
muon variants differ by `7.98e-11` relative; the sharpest published figure here
carries 9 significant digits and separating them needs about 12. All three round
correctly on all four figures. `qou-i229` has recorded twice that "no resolving
power" and "clean" look identical in a results table, so it is said plainly: this
probe determines the anchor family and says nothing about the vintage.

WHY NOTHING PRODUCED THESE FIGURES
-----------------------------------
The block names `delta-q-decoration.witness.json` as its verification. That
witness declares a **different** block (`def:delta-q-decoration`), carries
Markov-trace machinery rather than any of these four quantities, and is anchored
`q0Anchor: proton`. So the cited evidence is proton-anchored while the table is
muon-anchored, and the live compute for this quantity across the repo follows the
sibling block onto proton. Hence: no carrier, anywhere.

WHAT IS NOT CLAIMED
-------------------
Which pin either block *should* use. That is the owner ruling `qou-i229` holds,
and it is sharper here than elsewhere: these two blocks cannot both be right,
because they publish the two sides of an identity. Nothing is claimed about
whether the bare form models `alpha_EM` at all — `rem:em-coupling-chern-simons`
is open. No published figure is changed.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 50

#: Every registered `q0` this corpus carries, so the test is not a two-way guess.
PINS = {
    "proton": "1.1099785827513808075916690956107688798744991218736",
    "muon_live": ("1.109978595642739046681795129380001752700065561029011"
                  "556974045769999095"),
    "retired": "1.1099785955541805752815940796095093779932822799587",
    "frozen_A": "1.1099785955573347",
}

CITED_WITNESS = COMP / "delta-q-decoration.witness.json"
SIBLING_BLOCK = "prop:em-coupling-projection"


def h(q):
    """Skein parameter `h = q - q^-1`."""
    return q - 1 / q


def delta_q(k, q):
    """`delta_q(T_{2,k}) = q^k - q^-k`, the block's q-dimension decoration."""
    return q ** k - q ** (-k)


def qint(n, q):
    """Balanced quantum integer `[n]_q`."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def alpha_trace_ratio(q):
    """The block's LEFT side: `h^2 / (q * delta_9 * delta_10)`."""
    return h(q) ** 2 / (q * delta_q(9, q) * delta_q(10, q))


def alpha_projection(q):
    """The sibling's RIGHT side: `1 / (q [9]_q [10]_q)`."""
    return 1 / (q * qint(9, q) * qint(10, q))


#: The block's four published table figures, each with its own closed form.
PUBLISHED = [
    ("h = q0 - 1/q0", h, "0.20906032"),
    ("delta_q(T_2,9) = q0^9 - q0^-9", lambda q: delta_q(9, q), "2.16660039"),
    ("delta_q(T_3,5) = q0^10 - q0^-10", lambda q: delta_q(10, q), "2.48662110"),
    ("alpha_EM x 1e3", lambda q: alpha_trace_ratio(q) * 1000, "7.30870098"),
]


def rounds_to(value, published: str) -> bool:
    """Exact half-ulp test at the published decimal count. No float64."""
    k = len(published.split(".")[1])
    return abs(value - mp.mpf(published)) <= mp.mpf(5) * mp.mpf(10) ** (-k - 1)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])

    print("\n" + "=" * 78)
    print("§1  THE IDENTITY IS EXACT AT ANY q — it is algebra, not agreement")
    print("=" * 78)
    worst = mp.mpf(0)
    for name, s in PINS.items():
        q = mp.mpf(s)
        d = abs(alpha_trace_ratio(q) - alpha_projection(q))
        worst = max(worst, d)
        print(f"    at {name:<10} |h^2/(q d9 d10) - 1/(q[9][10])| = {mp.nstr(d, 4)}")
    check("h^2/(q*delta_9*delta_10) == 1/(q [9]_q [10]_q) identically — the two "
          "h cancel the h^2, so this holds at every pin", worst < mp.mpf("1e-45"))

    print("\n" + "=" * 78)
    print("§2  WHICH PIN DOES THE BLOCK PUBLISH? — rounding test, all pins")
    print("=" * 78)
    print(f"    {'pin':<11} " + "".join(f"{n.split(' ')[0]:>13}" for n, _f, _p
                                        in PUBLISHED) + "   score")
    scores = {}
    for name, s in PINS.items():
        q = mp.mpf(s)
        oks = [rounds_to(fn(q), pub) for _n, fn, pub in PUBLISHED]
        scores[name] = sum(oks)
        marks = "".join(f"{'ok' if o else 'MISS':>13}" for o in oks)
        print(f"    {name:<11} {marks}   {sum(oks)}/4")
    check("the PROTON pin fails every one of the four figures",
          scores["proton"] == 0)
    check("every muon variant reproduces all four exactly",
          all(scores[k] == 4 for k in ("muon_live", "retired", "frozen_A")))

    print("\n    proton residuals, for scale:")
    for n, fn, pub in PUBLISHED:
        q = mp.mpf(PINS["proton"])
        e = abs(fn(q) - mp.mpf(pub)) / abs(fn(q))
        print(f"      {n:<34} {mp.nstr(e, 3)}")

    print("\n" + "=" * 78)
    print("§3  THE VINTAGE IS UNDETERMINABLE — said plainly, not left implied")
    print("=" * 78)
    ql, qr = mp.mpf(PINS["muon_live"]), mp.mpf(PINS["retired"])
    sep = abs(ql - qr) / ql
    print(f"    live vs retired differ by      {mp.nstr(sep, 4)} relative")
    print(f"    sharpest published figure       9 significant digits")
    print(f"    digits needed to separate      ~12")
    check("all three muon variants round correctly on all four figures, so the "
          "published precision CANNOT choose between them — the family is "
          "determined, the vintage is not",
          scores["muon_live"] == scores["retired"] == scores["frozen_A"] == 4
          and sep < mp.mpf("1e-10"))

    print("\n" + "=" * 78)
    print("§4  THE TWO SIDES OF A PROVEN IDENTITY, AS PUBLISHED")
    print("=" * 78)
    ap = alpha_projection(mp.mpf(PINS["proton"])) * 1000
    am = mp.mpf("7.30870098")
    disagree = abs(ap - am) / am
    print(f"    {SIBLING_BLOCK}")
    print(f"        publishes q[9][10] = 136.823209 at the PROTON pin,")
    print(f"        i.e. alpha x 1e3 = {mp.nstr(ap, 12)}")
    print(f"    prop:alpha-em-categorical-trace-ratio")
    print(f"        publishes alpha x 1e3 = {am}  at a MUON pin")
    print(f"    disagreement                   {mp.nstr(disagree, 4)} relative")
    check("the two blocks publish the two sides of an identity they have proved "
          "equal, and the numbers differ — they cannot both be right",
          disagree > mp.mpf("1e-8"))

    print("\n" + "=" * 78)
    print("§5  WHY NOTHING IN 3277 WITNESSES CARRIES THESE FIGURES")
    print("=" * 78)
    wit = json.loads(CITED_WITNESS.read_text(encoding="utf-8", errors="replace"))
    print(f"    block cites      {CITED_WITNESS.name}")
    print(f"    which declares   {wit.get('contentBlock')}   <- a DIFFERENT block")
    print(f"    and is anchored  q0Anchor = {wit.get('q0Anchor')}")
    check("the cited witness declares another block and is PROTON-anchored, "
          "while this table is muon-anchored — so the live compute for this "
          "quantity sits at the other pin and no carrier exists",
          wit.get("contentBlock") != "prop:alpha-em-categorical-trace-ratio"
          and wit.get("q0Anchor") == "proton")

    print("\n" + "=" * 78)
    print("§S  VERDICT")
    print("=" * 78)
    print("  Not a misplaced pointer — the last two blocks were that. Here the")
    print("  figures have no producer because the corpus computes this quantity")
    print("  at the other pin. Two blocks, one citing the other, publish the two")
    print("  sides of a proven identity at different anchors. Owner ruling needed:")
    print("  they cannot both be right. Nothing changed by this probe.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_content_block("prop:alpha-em-categorical-trace-ratio")
        wb.set_description(
            "prop:alpha-em-categorical-trace-ratio proves alpha_EM = "
            "h^2/(q*delta_q(T_2,9)*delta_q(T_3,5)) = 1/(q [9]_q [10]_q) -- an exact "
            "algebraic identity, verified here to 1e-53 at every registered pin, "
            "since delta_q(T_2,9) = h[9]_q and delta_q(T_3,5) = h[10]_q cancel the "
            "h^2. It cites prop:em-coupling-projection for the right-hand side. That "
            "block publishes the right side at the PROTON pin and says so; this block "
            "publishes the left side at a MUON pin, so the two sides of a proved "
            "identity are published as numbers differing by 7.94e-8 relative. "
            "Determined by rounding test against every registered q0: the proton pin "
            "fails all four of the block's table figures (residuals 1.0e-7 to 1.5e-7) "
            "and every muon variant reproduces all four exactly. The VINTAGE is "
            "undeterminable -- the three muon variants differ by 7.98e-11 relative, "
            "the sharpest published figure carries 9 significant digits, and "
            "separating them needs about 12; all three round correctly on all four, "
            "and this probe does not guess. Explains why the candidate-producer sweep "
            "found no witness covering more than 1 of these 4 figures among 3277: the "
            "cited witness declares a different block and is proton-anchored, so the "
            "live compute for this quantity sits at the other pin. qou-i229.")
        for pin_name, s in PINS.items():
            q = mp.mpf(s)
            wb.add_data(f"figures_at_{pin_name}", {
                "q0": mp.nstr(q, 20),
                **{n: mp.nstr(fn(q), 15) for n, fn, _p in PUBLISHED},
                "rounds_to_published": f"{scores[pin_name]}/4",
            })
        wb.add_data("published_by_the_block",
                    {n: p for n, _f, p in PUBLISHED})
        wb.add_data("identity_disagreement", {
            "sibling_block": SIBLING_BLOCK,
            "sibling_alpha_x1e3_at_proton": mp.nstr(ap, 12),
            "this_block_alpha_x1e3_published": str(am),
            "relative_disagreement": mp.nstr(disagree, 6),
            "identity_residual_worst_over_pins": mp.nstr(worst, 4),
        })
        wb.add_data("cited_witness", {
            "file": CITED_WITNESS.name,
            "declares": str(wit.get("contentBlock")),
            "q0Anchor": str(wit.get("q0Anchor")),
        })
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Determines the anchor FAMILY (muon, decisively) and says NOTHING about "
            "which muon vintage. The published precision cannot separate them and no "
            "guess is recorded here -- qou-i229 has twice recorded that 'no resolving "
            "power' and 'clean' look identical in a results table.")
        wb.add_caveat(
            "Says nothing about which pin either block SHOULD use; that is the owner "
            "ruling qou-i229 holds. It is sharper here than elsewhere only because "
            "the two blocks publish the two sides of one identity and so cannot both "
            "be right.")
        wb.add_caveat(
            "Says nothing about whether the bare form models alpha_EM at all. "
            "rem:em-coupling-chern-simons is explicitly open. No published figure is "
            "changed.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": (
            "comparison by design: rounding test of both blocks' figures against every registered pin (proton, live CODATA-2022 muon, retired CODATA-2018 muon, frozen pin A 1.1099785955573347)")})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
