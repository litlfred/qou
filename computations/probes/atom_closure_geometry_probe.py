#!/usr/bin/env python3
"""atom_closure_geometry_probe — is the canonical atom word's Markov closure
hyperbolic?  For the ATOMS: no, under both intra-orderings and all three
averaging modes.  For the single NUCLEONS: yes under `"borromean"` only, and
with a mode-dependent volume that is therefore NOT a derived quantity.

WHY THIS EXISTS.  Bean `qou-mbbf` established that the closure has `A + 1`
components at every `A`, invariantly, so it is not the census-assigned binding
carrier (`8_11` has 1, `L6a4` has 3).  That left exactly one input undetermined
for the carrier decision: **is the closure hyperbolic at all?**  If it is, it is
a candidate binding carrier in its own right and the census assignment -- an
admitted AME-driven fit, ruled out as a selection mechanism on 2026-09-08 -- can
be retired in its favour.  If it is not, it has no volume to feed the
volume-based binding route and that option is simply unavailable.

`he4-link-volume-braid-closure.witness.json` answers it (`geometric: no`,
`Vol: 0`) but was computed **2026-07-04**, and `7db032fb48` (2026-09-05) changed
the word underneath it.  The producer's baked `CLOSURE` table is that stale
answer transcribed; `--live` recomputes, but needs SnapPy.

RESULT 1 -- THE ATOMS ARE NON-GEOMETRIC, AND IT IS NOT A CONVENTION ARTIFACT.
3H, 3He and 4He return `contains degenerate tetrahedra` on 12/12 randomised
attempts, under **both** intra-orderings and **all three** averaging modes
(`averaged -> +sigma`, `-> -sigma`, `-> drop`).  Six independent settings, same
answer.  So the 2026-07-04 rows reproduce exactly and the option of promoting
the closure to a binding carrier is closed by measurement, not by inertia.

RESULT 2 -- THE NUCLEON ROWS OF THAT TABLE ARE STALE, and the producer's own
comment is now false.  It reads *"Every mode (avg -> +sigma / -sigma / drop)
gives the same non-geometric outcome"*.  Under `"grouped"` (the word it was
measured on) that holds.  Under the live `"borromean"` word the proton and
neutron closures are **hyperbolic in all three modes**.

    proton    +sigma  9.966512   -sigma 11.942872   drop 10.215606
    neutron   +sigma 16.191143   -sigma  8.195703   drop 11.942872

🛑 DO NOT READ THOSE AS NUCLEON VOLUMES.  They vary by up to 2x with the
averaging mode, which is an unresolved rendering convention (how an `"averaged"`
crossing becomes a braid letter), not a physical or categorical input.  A
quantity that moves 2x under a convention nobody has fixed is not derived, and
selecting the mode whose number one likes is precisely the selection-against-
the-target that AGENTS.md's anti-fit rule forbids.  What is established here is
the qualitative flip (non-geometric -> geometric), which is mode-independent;
the magnitude is not.

NOT CLAIMED: that a nucleon SHOULD close to a hyperbolic link; any relation
between these volumes and any observable; anything about the atoms beyond
non-geometricity.  The component counts are `qou-mbbf`'s, not re-derived here.

DEPENDENCIES.  Needs `snappy` and `spherogram`; both `pip install` cleanly.
Skips with a clear message rather than failing when they are absent, because a
bare container is the default here.
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

# (label, Z, N, include_inter)
SPEC = [
    ("proton", 1, 0, False),
    ("neutron", 0, 1, False),
    ("3H", 1, 2, True),
    ("3He", 2, 1, True),
    ("4He", 2, 2, True),
]
ORDERS = ("borromean", "grouped")
AVG_MODES = ("+", "-", "drop")
ATOMS = {"3H", "3He", "4He"}
NUCLEONS = {"proton", "neutron"}


def _close(atom_canonical_crossings, spherogram, Z, N, inter, order, avg):
    """Markov-close the word and ask SnapPy for a hyperbolic structure."""
    crossings = atom_canonical_crossings(Z, N, include_inter=inter,
                                         intra_order=order)
    word: list[int] = []
    for gen, ctype in crossings:
        letter = gen + 1
        if ctype == "sigma":
            word.append(letter)
        elif ctype == "sigma_inv":
            word.append(-letter)
        elif avg == "+":
            word.append(letter)
        elif avg == "-":
            word.append(-letter)
        # avg == "drop": the averaged crossing contributes no letter

    link = spherogram.Link(braid_closure=word)
    link.simplify("global")
    manifold = link.exterior()

    best, geometric, n_ok = 0.0, False, 0
    for attempt in range(12):
        try:
            if attempt:
                manifold.randomize()
            sol = manifold.solution_type()
            n_ok += 1
            if "positively" in sol:
                geometric = True
                best = max(best, float(manifold.volume()))
        except Exception:
            pass
    if n_ok == 0:
        raise RuntimeError(f"SnapPy failed on all 12 attempts ({Z=}, {N=})")
    return geometric, round(best, 6), len(link.crossings)


def main() -> int:
    try:
        import snappy
        import spherogram
    except ImportError as exc:
        print(f"SKIP — {exc.name} not installed. `pip install snappy spherogram`")
        print("      (both install cleanly; a bare container is the default here)")
        return 0

    from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

    # Calibrate against a value the corpus proves elsewhere, before trusting
    # anything this probe says. Vol(4_1) = 2*Cl_2(pi/3), the muon anchor.
    fig8 = snappy.Manifold("4_1").volume()
    if abs(float(fig8) - 2.0298832128) > 1e-6:
        print(f"ABORT — SnapPy fig-8 sanity failed: {fig8}")
        return 1
    print(f"SnapPy calibrated: Vol(4_1) = {fig8} (corpus: 2.0298832128)\n")

    results: dict[tuple[str, str, str], tuple[bool, float, int]] = {}
    print(f"{'case':9s} {'intra_order':11s} {'avg':5s} {'geometric':>9s} "
          f"{'volume':>12s} {'crossings':>9s}")
    for label, Z, N, inter in SPEC:
        for order in ORDERS:
            for avg in AVG_MODES:
                geo, vol, cr = _close(atom_canonical_crossings, spherogram,
                                      Z, N, inter, order, avg)
                results[(label, order, avg)] = (geo, vol, cr)
                print(f"{label:9s} {order:11s} {avg:5s} {str(geo):>9s} "
                      f"{vol:12.6f} {cr:9d}")

    checks: list[tuple[str, bool, str]] = []

    atoms_flat = all(
        not results[(lab, o, a)][0]
        for lab in ATOMS for o in ORDERS for a in AVG_MODES
    )
    checks.append((
        "every ATOM is non-geometric in all 6 word/mode settings",
        atoms_flat,
        "this is what closes the carrier option: no volume to feed binding",
    ))

    atoms_zero = all(
        results[(lab, o, a)][1] == 0.0
        for lab in ATOMS for o in ORDERS for a in AVG_MODES
    )
    checks.append((
        "every ATOM has volume exactly 0",
        atoms_zero,
        "reproduces the 2026-07-04 witness rows under the LIVE word",
    ))

    nucleons_bor = all(
        results[(lab, "borromean", a)][0]
        for lab in NUCLEONS for a in AVG_MODES
    )
    checks.append((
        "both NUCLEONS are geometric under 'borromean', all 3 modes",
        nucleons_bor,
        "the qualitative flip; mode-independent, so not a rendering artifact",
    ))

    nucleons_grp = all(
        not results[(lab, "grouped", a)][0]
        for lab in NUCLEONS for a in AVG_MODES
    )
    checks.append((
        "both NUCLEONS are non-geometric under 'grouped', all 3 modes",
        nucleons_grp,
        "so the producer's baked table is stale, not wrong-when-written",
    ))

    # The magnitude is NOT convention-independent, and saying so is the point.
    proton_vols = {results[("proton", "borromean", a)][1] for a in AVG_MODES}
    spread_real = len(proton_vols) > 1
    checks.append((
        "the nucleon VOLUME is mode-dependent (so it is not derived)",
        spread_real,
        f"proton spans {min(proton_vols)}..{max(proton_vols)} across 3 modes",
    ))

    print()
    for name, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {why}")

    passed = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{passed}/{len(checks)} assertions passed")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
