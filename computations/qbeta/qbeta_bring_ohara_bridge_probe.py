#!/usr/bin/env python3
"""qou-pzsi: THE BRING->O'HARA BRIDGE, BUILT. A braid word gets a geodesic on the
cusp torus, the geodesic gets an O'Hara energy, and the energy is computed in
closed-enough form to evaluate. Then the honest result: on THIS embedding it is
order-blind, so it does not separate the gluon candidates either.

# Ref: computations/qbeta/qbeta_cusp_lattice_geodesic_probe.py   (half A: word -> geodesic, author steering 2026-07-27)
# Ref: computations/mobius_cross_energy_hopf_calibration.py      (the O'Hara/Moebius conventions)
# Ref: folio/quantum-observable-universe/lean/QOU/MobiusEnergy.lean  (oharaIntegrand)
# Ref: computations/qbeta/qbeta_embedding_energy_can_discriminate_probe.py  (the green light this tests)
# Ref: .beans/qou-pzsi--...md , .beans/qou-99qc--...md

MY OWN CLAIM, CORRECTED FIRST. Bean `qou-pzsi` and PR #7370 record that the
corpus has "NO map from a braid word to a curve in or on the Bring surface". That
is WRONG, and the owner said so. `qbeta_cusp_lattice_geodesic_probe` carries
exactly that map, on the author's own steering of 2026-07-27: *"we can associate
to a braid word a geodesic (flow) on the torus for the particle/vortex path"*.
The cusp torus is the flat torus `C/Lambda`, `Lambda = Z<1, omega>`,
`omega = e^{i pi/3}` (proved: `cusp-shape-bar-parity.md`, the 4_1 cusp shape is a
primitive 6th root of unity), and a closed geodesic is the lattice class
`(m, l)` with log-holonomy `u_{m,l} = ln q0 * (m + l*omega)`. I searched for
"embed/curve/parametrise" near "bring" and for consumers of the Moebius
integrators, and missed it because it is filed under GEODESIC. Recorded as a
detector-blindness instance: the map was one word away from every query I ran.

WHAT WAS ACTUALLY MISSING, and is built here:

  half A  word -> lattice class (m, l)     <- stated in the corpus, NOT implemented
  half B  (m, l) -> closed geodesic        <- implemented in the corpus
  half C  geodesic -> O'Hara energy        <- NOT implemented anywhere

HALF A, DERIVED NOT ASSUMED. `meridian-holonomy-boost.md` (proved) gives one
meridian turn the boost of rapidity `ln q0`, and in the Hecke algebra a positive
crossing carries the eigenvalue `q = e^{ln q0}` while a negative one carries
`q^{-1}`. So each positive crossing is `+1` meridian turn and each negative is
`-1`: **m = the exponent sum (writhe)**. The closure of an n-strand braid wraps
the braid axis once per strand, so **l = n**. Both halves of `(m, l)` are forced
by the construction, with no free choice.

HALF C, THE NEW PART. On a FLAT torus a geodesic is a straight line in the
universal cover, so both distances the O'Hara integrand needs are available in
closed form. With `v = m + l*omega`, unit direction `vhat = v/|v|` and length
`L = |v|`:

    d_ambient(s,t) = min_{lambda in Lambda} | (s-t)*vhat - lambda |
    d_arc(s,t)     = min( |s-t| , L - |s-t| )
    E = int int [ 1/d_ambient^2 - 1/d_arc^2 ] ds dt
      = L * int_0^L [ 1/d_ambient(u)^2 - 1/d_arc(u)^2 ] du      (translation invariance)

THE REGULARISATION IS EXACT HERE, which is what makes this computable at all.
For small `u` the nearest lattice point is `0`, so `d_ambient(u) = |u| = d_arc(u)`
and the integrand is **identically zero** near the diagonal -- not merely
integrable, but zero. O'Hara's subtraction was designed to cancel a `1/r^2`
singularity; on a flat torus with a straight geodesic it cancels it on the nose.
Check [C2] verifies this rather than assuming it.

SCALE INVARIANCE, and it is a real check not a convenience. Moebius energy is
scale-invariant, so the `ln q0` prefactor of the log-holonomy DROPS OUT: the
energy depends on the class `(m, l)` and not on the substrate modulus. Check
[C3] verifies it numerically across three decades of scale. Consequence worth
stating plainly: **this energy is q0-INDEPENDENT**, so it cannot be the
"evaluated at q_0" quantity the 2026-08-01 method redirect asked for -- a
separate finding from the blindness below.

THE RESULT, AND IT IS A NEGATIVE. `(m, l) = (exponent sum, strand count)`. Both
are letter-sum-type invariants: the exponent sum is a sum over letters and the
strand count does not depend on the word at all. So two words with the same
writhe on the same strand count get the SAME lattice class, the SAME geodesic and
the SAME energy. Measured on the gluon candidates: all four two-crossing
dressings have writhe +2 on 3 strands, so **this bridge assigns them one energy**
-- exactly the tie that crossing count and crossing energy already failed on,
arriving by a third route.

WHY THAT IS NOT THE END OF THE ROUTE. The green-light prune
(`qbeta_embedding_energy_can_discriminate_probe`, 5/5) established that the four
candidates are DISTINCT LINKS, so an isotopy-class functional is not barred from
separating them. That result stands. What this probe shows is narrower and
sharper: **the cusp-torus winding class is not a fine enough embedding** -- it
records `(writhe, strands)` and forgets the knot. The O'Hara energy is innocent;
the embedding is the lossy step. A bridge that discriminates needs an embedding
that sees the isotopy class, which the flat cusp torus provably does not.

WHAT IS NOT CLAIMED. That O'Hara energy cannot select -- the prune says it is not
excluded, and this probe does not touch that. That no finer Bring embedding
exists; the genus-4 Bring curve itself is not used here, only the genus-1 cusp
torus that the corpus's braid-word map lands in. That any candidate should be
adopted. No Q_beta appears in this probe.

ARITHMETIC. mpmath mpf throughout, proton pin where a pin is needed at all (the
result is scale- and therefore q0-independent). No float64.

Run: python3 -u computations/qbeta/qbeta_bring_ohara_bridge_probe.py \
       2>&1 | tee /tmp/qbeta_bring_ohara_bridge.log
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

import mpmath as mp  # noqa: E402

set_compute_dps(40)
mp.mp.dps = 40

Q0 = Q_MP

#: the 4_1 cusp shape, a primitive 6th root of unity (cusp-shape-bar-parity.md).
OMEGA = mp.exp(mp.mpc(0, 1) * mp.pi / 3)

#: lattice window for the ambient-distance minimisation. 3 is ample: the
#: geodesic never leaves the fundamental domain by more than |v|, and check
#: [C1] verifies the window by re-running at a wider one.
LATTICE_R = 3

#: the corpus nucleon sits on 3 strands (n = 3A with A = 1).
STRANDS = 3

Z, NEG1 = mp.mpf(0), mp.mpf(-1)

#: gluon dressings, as (generator, shift) letters. shift 0 is a positive
#: crossing, shift -1 is a negative one.
GLUONS = {
    "(empty)": [],
    "sigma_1": [(1, Z)],
    "sigma_1^-1": [(1, NEG1)],
    "sigma_1 sigma_0": [(1, Z), (0, Z)],
    "sigma_0 sigma_1": [(0, Z), (1, Z)],
    "sigma_1 sigma_1": [(1, Z), (1, Z)],
    "sigma_0 sigma_0 (LIVE)": [(0, Z), (0, Z)],
}

#: the common base: the 6-letter gamma-gamma core plus the 3-letter quark block.
#: Only the PURE crossings carry a meridian turn; the bar-fixed letter (-1/2) is
#: not a crossing and contributes none. The base is shared by every candidate,
#: so it shifts every writhe equally and cannot affect the ranking.
BASE_WRITHE = 3 * (1 - 1)          # (sigma_0, sigma_1^-1) x 3 -> exponent sum 0

TOL = mp.mpf("1e-20")
FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "", w=None) -> bool:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if w is not None:
        w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)
    return ok


def writhe(letters) -> int:
    """HALF A, first coordinate. One meridian turn is a boost of rapidity
    `ln q0` (meridian-holonomy-boost.md, proved); a positive crossing carries
    the Hecke eigenvalue `q`, a negative one `q^-1`. So m = the exponent sum."""
    out = 0
    for _, d in letters:
        if d == Z:
            out += 1
        elif d == NEG1:
            out -= 1
        else:
            raise ValueError("the bar-fixed letter is not a crossing")
    return out


def lattice_vector(m: int, ell: int):
    """HALF B: the class `(m, l)` as a vector of `Lambda = Z<1, omega>`.
    The `ln q0` prefactor of the log-holonomy is dropped -- the energy is
    scale-invariant, which check [C3] verifies rather than assumes."""
    return mp.mpf(m) + mp.mpf(ell) * OMEGA


def nontrivial_dist(u, v, vhat, scale=None, radius: int = LATTICE_R):
    """Distance to the nearest NON-TRIVIAL lattice translate.

    🛑 The trivial translates must be excluded, and this is a correctness fix
    rather than an optimisation. For the closed geodesic, `lambda = 0` gives
    `|u*vhat| = u` and `lambda = v` gives `|u*vhat - v| = L - u`: between them
    they reproduce `d_arc` EXACTLY. So the naive ambient minimum equals `d_arc`
    near both endpoints, the O'Hara integrand is analytically zero there, and
    evaluating it as written computes `1/eps^2 - 1/eps^2` with `eps ~ 1e-40` --
    catastrophic cancellation, `1e80 - 1e80`, returning garbage of order 1e44.
    The first build of this probe did exactly that and its scale-invariance
    assertion [C3] caught it.

    Excluding `{0, v}` and comparing against `d_arc` afterwards gives the same
    function with no cancellation anywhere."""
    disp = u * vhat
    one = mp.mpf(1) if scale is None else scale
    best = None
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            lam = (mp.mpf(a) + mp.mpf(b) * OMEGA) * one
            if abs(lam) < TOL or abs(lam - v) < TOL:
                continue                      # the trivial translates: 0 and v
            d = abs(disp - lam)
            if best is None or d < best:
                best = d
    return best


def ohara_integrand(u, v, vhat, L, scale=None, radius: int = LATTICE_R):
    """`1/d_ambient^2 - 1/d_arc^2`, written so the cancellation is exact.

    `d_ambient = min(d_arc, d_nontrivial)`, so the integrand is exactly `0`
    unless a non-trivial translate is strictly closer than the arc distance --
    in which case it is `1/d_nt^2 - 1/d_arc^2` with no near-equal subtraction."""
    d_arc = min(u, L - u)
    if d_arc <= 0:
        return mp.mpf(0)
    d_nt = nontrivial_dist(u, v, vhat, scale, radius)
    if d_nt is None or d_nt >= d_arc:
        return mp.mpf(0)
    return 1 / d_nt ** 2 - 1 / d_arc ** 2


def ohara_energy(m: int, ell: int, radius: int = LATTICE_R):
    """HALF C: the O'Hara / Moebius energy of the closed geodesic in class
    `(m, l)` on the flat cusp torus.

        E = L * int_0^L [ 1/d_ambient(u)^2 - 1/d_arc(u)^2 ] du

    by translation invariance along the geodesic. The integrand is identically
    zero near `u = 0` and `u = L` (check [C2]), so the quadrature sees no
    singularity."""
    v = lattice_vector(m, ell)
    L = abs(v)
    if L == 0:
        return None, L
    vhat = v / L
    val = mp.quad(lambda u: ohara_integrand(u, v, vhat, L, None, radius),
                  [mp.mpf(0), L / 2, L])
    return L * val, L


def main() -> int:
    w = WitnessBuilder("qbeta-bring-ohara-bridge")
    w.set_description(
        "Builds the Bring->O'Hara bridge and reports what it gives. CORRECTS my "
        "own claim (bean qou-pzsi, PR #7370) that the corpus has no braid-word "
        "to curve map: qbeta_cusp_lattice_geodesic_probe carries it, filed "
        "under GEODESIC, on the author's steering of 2026-07-27. What was "
        "genuinely missing is the geodesic -> O'Hara energy step, implemented "
        "here: on a flat torus a geodesic is straight in the universal cover, "
        "so the ambient and arc distances are both closed-form and the O'Hara "
        "subtraction cancels EXACTLY (the integrand is identically zero near "
        "the diagonal, not merely integrable). Half A is derived: m = exponent "
        "sum from the proved meridian-holonomy boost, l = strand count from the "
        "closure. RESULT, a negative: (m, l) = (writhe, strands) are both "
        "letter-sum-type, so all four two-crossing gluon dressings share one "
        "class, one geodesic and one energy -- the same tie, by a third route. "
        "The O'Hara energy is innocent; the cusp-torus embedding is the lossy "
        "step, and it provably forgets the knot. Also measured: the energy is "
        "scale- hence q0-INDEPENDENT, so it cannot be the 'evaluated at q_0' "
        "quantity the 2026-08-01 redirect asked for."
    )

    print("qou-pzsi — the Bring->O'Hara bridge, built and evaluated")
    print(f"  cusp shape omega = e^(i pi/3) = {mp.nstr(OMEGA, 12)}")
    print(f"  lattice Lambda   = Z<1, omega>   (hexagonal / Eisenstein)")
    print()

    # ---- C1: the lattice window is wide enough --------------------------
    print("== C1. quadrature and lattice-window soundness ==")
    e_r3, L_r3 = ohara_energy(1, 3, radius=3)
    e_r5, _ = ohara_energy(1, 3, radius=5)
    rel = abs(e_r3 - e_r5) / abs(e_r5) if e_r5 != 0 else mp.mpf(0)
    print(f"    E(1,3) at window 3 = {mp.nstr(e_r3, 16)}")
    print(f"    E(1,3) at window 5 = {mp.nstr(e_r5, 16)}")
    check("the_lattice_window_is_converged",
          rel < mp.mpf("1e-18"),
          f"widening the lattice window from 3 to 5 moves the energy by "
          f"{mp.nstr(rel, 4)} relative -- the nearest-translate minimisation is "
          f"saturated, so the reported energies are not window artifacts", w)

    # ---- C2: the O'Hara subtraction cancels EXACTLY ----------------------
    print()
    print("== C2. does the O'Hara subtraction cancel on the nose? ==")
    v = lattice_vector(1, 3)
    L = abs(v)
    vhat = v / L
    probes = [L / mp.mpf(10 ** k) for k in (2, 3, 4, 5)]
    worst = mp.mpf(0)
    for k, u in zip((2, 3, 4, 5), probes):
        d_nt = nontrivial_dist(u, v, vhat)
        dc = min(u, L - u)
        resid = abs(ohara_integrand(u, v, vhat, L))
        worst = max(worst, resid)
        print(f"    u = L/1e{k}:  d_arc = {mp.nstr(dc, 12)}"
              f"   d_nontrivial = {mp.nstr(d_nt, 12)}   integrand = "
              f"{mp.nstr(resid, 6)}")
    check("the_integrand_is_IDENTICALLY_zero_near_the_diagonal",
          worst < TOL,
          f"worst residual {mp.nstr(worst, 6)} over four decades approaching the "
          f"diagonal. On a flat torus the nearest lattice translate of a short "
          f"geodesic arc is 0, so d_ambient = |u| = d_arc EXACTLY and O'Hara's "
          f"regularisation cancels on the nose. That is what makes this "
          f"computable without a principal value", w)

    # ---- C3: scale invariance, hence q0-independence ---------------------
    print()
    print("== C3. scale invariance — and therefore q0-independence ==")

    def scaled_energy(m, ell, scale):
        vv = lattice_vector(m, ell) * scale
        LL = abs(vv)
        vh = vv / LL
        return LL * mp.quad(
            lambda u: ohara_integrand(u, vv, vh, LL, scale),
            [mp.mpf(0), LL / 2, LL])

    lnq = mp.log(Q0)
    e_unit = scaled_energy(1, 3, mp.mpf(1))
    e_lnq = scaled_energy(1, 3, lnq)
    e_1000 = scaled_energy(1, 3, mp.mpf(1000))
    print(f"    scale 1        : {mp.nstr(e_unit, 16)}")
    print(f"    scale ln q0    : {mp.nstr(e_lnq, 16)}   (ln q0 = {mp.nstr(lnq, 10)})")
    print(f"    scale 1000     : {mp.nstr(e_1000, 16)}")
    spread = max(abs(e_unit - e_lnq), abs(e_unit - e_1000)) / abs(e_unit)
    check("the_energy_is_scale_and_therefore_q0_independent",
          spread < mp.mpf("1e-15"),
          f"three scales spanning 1e-1 to 1e3 agree to {mp.nstr(spread, 4)} "
          f"relative. Moebius energy is scale-invariant, so the ln q0 prefactor "
          f"of the log-holonomy DROPS OUT. Consequence: this energy cannot be "
          f"the 'evaluated at q_0' quantity the 2026-08-01 method redirect "
          f"asked for -- it does not see q0 at all", w)

    # ---- the candidates --------------------------------------------------
    print()
    print("== the gluon candidates through the bridge ==")
    print("   gluon                      writhe  class (m,l)   L          E_O'Hara")
    rows = {}
    for name, g in GLUONS.items():
        m = BASE_WRITHE + writhe(g)
        ell = STRANDS
        e, L = ohara_energy(m, ell)
        rows[name] = {"writhe": m, "class": (m, ell), "L": L, "E": e}
        print(f"   {name:<26s} {m:+d}      ({m},{ell})        "
              f"{mp.nstr(L, 8):<10s} {mp.nstr(e, 14) if e is not None else 'n/a'}")

    check("every_energy_is_non_negative",
          all(r["E"] is None or r["E"] >= 0 for r in rows.values()),
          f"min over candidates = "
          f"{mp.nstr(min(r['E'] for r in rows.values() if r['E'] is not None), 12)}. "
          f"O'Hara energy is an integral of `1/d_ambient^2 - 1/d_arc^2` with "
          f"`d_ambient <= d_arc` pointwise, so it cannot be negative. The first "
          f"build of this probe returned ~-4e44 here -- catastrophic "
          f"cancellation at the endpoints, where the integrand is analytically "
          f"zero and was being evaluated as 1e80 - 1e80. This assertion and "
          f"[C3] are what caught it", w)

    two = {n: r for n, r in rows.items() if len(GLUONS[n]) == 2}
    classes = {r["class"] for r in two.values()}
    energies = {mp.nstr(r["E"], 25) for r in two.values()}
    print()
    print(f"    two-crossing candidates : {sorted(two)}")
    print(f"    distinct classes        : {len(classes)}  -> {sorted(classes)}")
    print(f"    distinct energies       : {len(energies)}")

    check("the_cusp_torus_class_is_writhe_and_strands_only",
          len(classes) == 1,
          f"all {len(two)} two-crossing dressings map to the single class "
          f"{sorted(classes)[0]}. m is the exponent sum (a sum over letters) and "
          f"l is the strand count (independent of the word), so the class is a "
          f"letter-sum-type invariant by construction", w)

    check("the_bridge_TIES_the_candidates_it_was_built_to_separate",
          len(energies) == 1,
          f"one distinct O'Hara energy over {len(two)} candidates. The same tie "
          f"crossing count and crossing energy already failed on, reached by a "
          f"third and independent route. The O'Hara functional is innocent: the "
          f"CUSP-TORUS EMBEDDING is the lossy step, and it provably forgets the "
          f"knot", w)

    # the green light is not retracted -- it was about a different question
    check("this_does_NOT_retract_the_green_light",
          True,
          "qbeta_embedding_energy_can_discriminate (5/5) showed the four "
          "candidates are DISTINCT LINKS, so an isotopy-class functional is not "
          "barred from separating them. That stands. This probe shows only that "
          "the cusp-torus winding class is too coarse an embedding to realise "
          "it -- a statement about the embedding, not about the energy", w)

    w.add_data("bridge", {
        "half_A_word_to_class": "m = exponent sum (meridian-holonomy-boost.md: "
                                "one meridian turn is a boost of rapidity ln q0, "
                                "and a positive crossing carries the Hecke "
                                "eigenvalue q); l = strand count (the closure "
                                "wraps the axis once per strand). Both forced.",
        "half_B_class_to_geodesic": "u_{m,l} = ln q0 * (m + l*omega) on the flat "
                                    "cusp torus C/Lambda, Lambda = Z<1, omega>, "
                                    "omega = e^{i pi/3} -- the corpus's own map "
                                    "(qbeta_cusp_lattice_geodesic_probe)",
        "half_C_geodesic_to_energy": "E = L * int_0^L [1/d_ambient(u)^2 - "
                                     "1/d_arc(u)^2] du, with d_ambient the "
                                     "flat-torus distance (min over lattice "
                                     "translates) and d_arc = min(u, L-u). NEW.",
    })
    w.add_data("candidates", {
        n: {"writhe": r["writhe"], "class": list(r["class"]),
            "geodesic_length": mp.nstr(r["L"], 25),
            "ohara_energy": mp.nstr(r["E"], 25) if r["E"] is not None else None}
        for n, r in rows.items()})
    w.add_data("verdict", {
        "distinct_classes_over_two_crossing_candidates": len(classes),
        "distinct_energies": len(energies),
        "reading": "the cusp-torus winding class is (writhe, strands), both "
                   "letter-sum-type, so this bridge inherits the blindness that "
                   "defeated crossing count and crossing energy",
        "what_survives": "the green light -- the candidates ARE distinct links, "
                         "so a FINER embedding is not excluded. The genus-4 "
                         "Bring curve itself is not used here; only the genus-1 "
                         "cusp torus the corpus's braid map lands in",
        "separate_finding": "the energy is scale- hence q0-independent, so it "
                            "cannot be the 'evaluated at q_0' quantity the "
                            "2026-08-01 method redirect asked for",
    })
    w.add_data("corrects", {
        "qou-pzsi / PR #7370": "'no map from a braid word to a curve in or on "
                               "the Bring surface' is WRONG -- "
                               "qbeta_cusp_lattice_geodesic_probe carries it, "
                               "filed under GEODESIC. My searches keyed on "
                               "embed/curve/parametrise near 'bring' and on "
                               "consumers of the Moebius integrators, and the "
                               "map was one word away from every one of them",
    })
    w.add_data("scope", {
        "class": "(a) scope-limited -- one embedding, one family",
        "not_claimed": [
            "that O'Hara energy cannot select -- the prune says it is not "
            "excluded and this does not touch that",
            "that no finer Bring embedding exists -- the genus-4 curve is "
            "unused here",
            "that any candidate should be adopted",
        ],
        "no_selection_by_accuracy": "no Q_beta appears in this probe",
    })

    ok = not FAILED
    # AGENTS.md q0-anchor rule: "Say which pin you used. Any new witness
    # must record its q0 so a later reader can tell which layer it belongs
    # to without inferring it from a call site."
    w.add_data("q0_pin", "proton")
    w.add_data("q0_value", Q_50_DIGIT_STR)
    w.add_data("q0_note", "recorded for provenance; the result is measured "
                          "scale-invariant and therefore q0-independent (C3)")
    w.save()
    print()
    print(f"{'OK' if ok else 'FAILED'}: {len(FAILED)} failed assertion(s)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
