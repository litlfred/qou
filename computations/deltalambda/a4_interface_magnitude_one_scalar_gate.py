#!/usr/bin/env python3
"""a4_interface_magnitude_one_scalar_gate.py
=============================================

**The producer for `a4-interface-magnitude-one-scalar-gate.witness.json`, which
until now had none.**

That witness records the A=4 (⁴He) ≥4-body magnitude wall: with the derived
`[1⁴]` exchange spectrum `{±√5, ±1}`, the single per-pair bond scalar `m` gives
`det(I+G) = (1−5m²)(1−m²)` and `b₄(m) = −ln det(I+G)`, which is **surjective onto
`(0,∞)`** on `m ∈ (0, 1/√5)`. Every AME target is reachable and each reaching `m`
is a function of the target — so the magnitude cannot be closed by computation,
only by a principle that fixes `m`.

**It was hand-written.** Measured on `main` before this file existed: `engine`,
`scriptFile`, `scriptHash`, `commitSha`, `computedAt`, `q0Anchor`,
`precisionMetadata` and `environment` were **all absent**, and no script in the
tree wrote it. Every number in it was unreproducible by construction, which is
why the convention-C residue found in PR #6193 could be *recorded* but not
*fixed*: there was nothing to re-run. Bean `qou-rv6z`.

## The staleness this closes — the witness is behind its own cited Lean

`QOU/MassTheory/A4InterfaceMagnitude.lean` is sorry-free and carries **21**
declarations. The witness lists **7** and omits the four that matter here:

    zD, zD_sq, zD_sq_mem, zD_unphysical

Those were added when convention C was excised (owner ruling 2026-08-15 R1). The
Lean says so in its own docstring — *"The `naive_z_unphysical` theorem above used
the excised convention-C value `z_C(q₀) ≈ 0.499` as a bare rational; this is its
canonical-convention replacement, stated symbolically in `q` and proved on the
whole window rather than at a point."* The witness never followed, and still
cites `naive_z_bond_factor = 0.499320334`, which is
`z_C = √q₀/(q₀+1)` — the excised convention.

**The verdict does not move, and this producer establishes that rather than
assuming it.** Under the canonical `z_D = q₀³/(q₀²+1)` the exclusion is
*stronger*: `5z²` goes 1.2466 → 1.8769 and `det(I+G)` goes −0.1851 → −0.5477.
Both are excluded; D more decisively. Only the cited number was stale.

## What this producer recomputes (nothing is transcribed)

Every field is derived here in `mpmath.mpf` at 50 dps, and each is cross-checked
against the Lean declaration that proves it:

| check | mirrors |
|---|---|
| `det(I+G)` three ways: spectral product `∏(1+λᵢ)` over `{±m√5, ±m}`, factored `(1−5m²)(1−m²)`, expanded `1−6m²+5m⁴` | `detG_eq_spectral_product`, `detG_expand` |
| `det ∈ (0,1)` on the physical region, `det < 0` above the ceiling | `detG_mem_Ioo`, `detG_neg_of_above_ceiling` |
| `b₄` strictly increasing on `(0, 1/√5)` | `b4_strictMono_on`, `detG_strictAnti` |
| closed-form inverse round-trips: `b₄(m*(t)) = t` | `magnitude_form_surjective`, `uStar_root`, `detG_mStar` |
| the three documented targets are all reachable | `documented_targets_all_reachable` |
| `z_C` **and** `z_D` both unphysical | `naive_z_unphysical`, `zD_unphysical` |
| every cited declaration actually exists in the `.lean` | — (new; see below) |

**The last one is not ceremony.** A witness citing a theorem name is an
unverified claim about a file: nothing checked that
`lean.key_theorems` named declarations that exist. This producer greps the file
and fails if one does not. It is how the four missing `zD` declarations were
found.

## What it does NOT do

It does not close the magnitude, does not narrow the scope-(a) wall, and does
not fix `m`. Surjectivity is *reproduced*, which is the point: it is the reason
no probe can close this. No target is inverted into production
(`free_parameters = 0`); `m*(t)` is computed **only** to demonstrate
reachability, exactly as the Lean's existence proof does, and is never wired.

Two measured limits, stated rather than avoided. First, the round-trip
`b₄(m*(t)) = t` loses digits at **both** ends — `~t·log₁₀(e)` at large `t` (as
`m*` approaches the ceiling, `1−5m²` cancels) and `~log₁₀(1/t)` at small `t` (a
log near 1) — and is essentially exact at `t ≈ 1`. It is checked against that
two-sided floor rather than a fixed tolerance, which would hide the
degradation. Second, the closed-form inverse is usable only up to `t ≈ 116.27`
at 50 dps — above that `e^{−t}` underflows, `m*`
lands exactly *on* the ceiling, `det = 0` and `b₄ = −ln 0 = +∞`. The threshold
tracks `dps·ln(10) = 115.13`, so it is a **precision** limit, not a limit of the
mathematics: the form is surjective onto `(0,∞)` as the Lean proves. It is the
(C2) digit-count result seen from the other side — `B(⁴He)` at `t = 28.3`
already sits `1.44e-13` below the ceiling. A first version of this producer
swept to `t = 1e6`, returned `+inf`, and was *correct* to fail.

PRECISION
---------
mpmath at 50 dps, `mpf` end to end. `√5`, `ln`, `exp` are mpmath's. The
round-trip residuals are reported at their true magnitude rather than against a
tolerance chosen to pass. `z_D` reads `q₀` from the canonical proton pin, so the
witness is stamped `q0Anchor: proton`; `z_C` is retained ONLY as a named
historical delta and is never presented as canonical.

Usage:
    python3 computations/deltalambda/a4_interface_magnitude_one_scalar_gate.py
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _bridge

import re  # noqa: E402
import time  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import Q as Q0_PROTON, Q_50_DIGIT_STR as Q0_PROTON_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_HE4_MEV_VALIDATION

set_compute_dps(50)

LEAN = ("content/quantum-observable-universe/lean/QOU/MassTheory/"
        "A4InterfaceMagnitude.lean")

# The three targets the witness documents. Read ONLY to demonstrate
# reachability, never inverted into any production quantity.
TARGETS = {
    "b4_1four_connected_cumulant": mp.mpf("9.243"),
    "mu4_simplex_residual_abs": mp.mpf("4.591048"),
    "B_4He_AME": AME_B_HE4_MEV_VALIDATION,
}


def detG_spectral(m):
    """`∏(1 + λᵢ)` over the derived spectrum `{+m√5, −m√5, +m, −m}`."""
    s5 = mp.sqrt(5)
    return (1 + m * s5) * (1 - m * s5) * (1 + m) * (1 - m)


def detG(m):
    """Factored form `(1 − 5m²)(1 − m²)`."""
    return (1 - 5 * m ** 2) * (1 - m ** 2)


def detG_expand(m):
    """Expanded form `1 − 6m² + 5m⁴`."""
    return 1 - 6 * m ** 2 + 5 * m ** 4


def b4(m):
    """`b₄(m) = −ln det(I+G)`, the attractive branch."""
    return -mp.log(detG(m))


def m_star(t):
    """Closed-form inverse `m*(t) = √((6 − √(16 + 20e^{−t}))/10)`.

    Root of `5u² − 6u + (1 − e^{−t}) = 0` with `u = m² ∈ (0, 1/5)`, taking the
    minus branch. Computed to demonstrate REACHABILITY only — choosing `m` from
    a target is anchor inversion, i.e. a fit, and is never wired.
    """
    return mp.sqrt((6 - mp.sqrt(16 + 20 * mp.e ** (-t))) / 10)


def z_D(q):
    """Canonical convention-D Markov bond factor `q³/(q²+1)` (owner ruling R1)."""
    return q ** 3 / (q ** 2 + 1)


def z_C_historical(q):
    """EXCISED convention-C `√q/(q+1)`. Retained only as a named delta."""
    return mp.sqrt(q) / (q + 1)


def main() -> int:
    t0 = time.monotonic()
    fails = 0

    def chk(label, ok):
        nonlocal fails
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")

    print("A=4 interface magnitude one-scalar gate — producer (qou-rv6z)\n")
    ceiling = 1 / mp.sqrt(5)

    # ── 1 · det(I+G) three ways ───────────────────────────────────────────
    print("1 · det(I+G): spectral product == factored == expanded")
    worst = mp.mpf(0)
    for k in range(1, 40):
        m = mp.mpf(k) / 40 * ceiling
        d = max(abs(detG_spectral(m) - detG(m)), abs(detG(m) - detG_expand(m)))
        worst = max(worst, d)
    chk(f"max |spectral − factored|, |factored − expanded| = {mp.nstr(worst, 5)}"
        f" over 39 samples (mirrors detG_eq_spectral_product, detG_expand)",
        worst < mp.mpf("1e-45"))

    # ── 2 · physical region and the derived ceiling ───────────────────────
    print("\n2 · physical region (0, 1/sqrt5) and the ceiling")
    print(f"    ceiling 1/sqrt5 = {mp.nstr(ceiling, 12)}")
    inside = all(0 < detG(mp.mpf(k) / 40 * ceiling) < 1 for k in range(1, 40))
    chk("det in (0,1) on the physical region (mirrors detG_mem_Ioo)", inside)
    above = all(detG(ceiling * (1 + mp.mpf(k) / 20)) < 0 for k in range(1, 10))
    chk("det < 0 above the ceiling (mirrors detG_neg_of_above_ceiling)", above)

    # ── 3 · strict monotonicity ──────────────────────────────────────────
    print("\n3 · b4 strictly increasing on (0, 1/sqrt5)")
    xs = [mp.mpf(k) / 200 * ceiling for k in range(1, 200)]
    mono = all(b4(a) < b4(b) for a, b in zip(xs, xs[1:]))
    chk("b4 strictly increasing over 199 samples (mirrors b4_strictMono_on)",
        mono)

    # ── 4 · surjectivity by closed-form inverse round-trip ───────────────
    print("\n4 · surjectivity: b4(m*(t)) == t  (mirrors magnitude_form_surjective)")
    # The round-trip does not simply pass or fail -- it DEGRADES, at a rate the
    # arithmetic sets, and checking it against a fixed tolerance would hide
    # that. It loses digits at BOTH ends, for two different reasons:
    #
    #   large t : `1 - 5m^2` cancels catastrophically as m* -> the ceiling
    #             (at t = 100, `1/sqrt5 - m*` is 1.04e-44), costing ~t*log10(e)
    #   small t : det -> 1, so `-ln(det)` is a log near 1, costing ~log10(1/t)
    #
    # and it is essentially exact at t ~ 1. THREE earlier versions of this check
    # failed, each correctly and each for a different reason: t = 1e6 gave +inf
    # (underflow saturation); t = 100 gave 4.7e-10 against a fixed 1e-40 bound;
    # and a one-sided `dps - t/ln(10)` law failed at t = 1e-6, because it
    # described only the large-t side. The bound below is two-sided.
    print("    round-trip digit budget (surviving digits vs the dps - t/ln10 law):")
    decay = {}
    law_ok = True
    for t in (mp.mpf("1e-12"), mp.mpf("1e-6"), mp.mpf(1), mp.mpf(10),
              mp.mpf(30), mp.mpf(50), mp.mpf(100)):
        r = abs(b4(m_star(t)) - t) / t
        left = -mp.log10(r) if r > 0 else mp.mpf(mp.mp.dps)
        loss_large = t / mp.log(10)
        loss_small = max(mp.mpf(0), -mp.log10(t))
        predicted = mp.mp.dps - loss_large - loss_small
        decay[mp.nstr(t, 8)] = {
            "rel_residual": fmt(r), "digits_surviving": fmt(left),
            "two_sided_floor": fmt(predicted),
            "loss_large_t_term": fmt(loss_large),
            "loss_small_t_term": fmt(loss_small),
        }
        law_ok = law_ok and left >= predicted - 1
        print(f"      t = {mp.nstr(t, 8):>10}   rel = {mp.nstr(r, 5):>12}"
              f"   digits = {mp.nstr(left, 4):>7}   floor = {mp.nstr(predicted, 4):>7}")
    chk("surviving digits stay above the two-sided floor "
        "dps - t/ln(10) - log10(1/t)", law_ok)

    # The corpus operates at t <= 30 (the largest documented target is 28.3),
    # where the budget leaves ~40 digits. That is the range the gate is used in.
    rt_worst = mp.mpf(0)
    for e in range(-6, 2):
        rt_worst = max(rt_worst, abs(b4(m_star(mp.mpf(10) ** e))
                                     - mp.mpf(10) ** e) / mp.mpf(10) ** e)
    chk(f"max relative round-trip residual over the USED range t <= 10 is "
        f"{mp.nstr(rt_worst, 5)}", rt_worst < mp.mpf("1e-40"))

    # Where does the closed form stop being usable at this precision?
    lo, hi = mp.mpf(1), mp.mpf(1000)
    for _ in range(200):
        mid = (lo + hi) / 2
        if m_star(mid) < ceiling:
            lo = mid
        else:
            hi = mid
    t_sat, dps_ln10 = hi, mp.mp.dps * mp.log(10)
    print(f"    saturation: m* is indistinguishable from 1/sqrt5 for "
          f"t >= {mp.nstr(t_sat, 10)} at {mp.mp.dps} dps")
    print(f"    (tracks dps*ln(10) = {mp.nstr(dps_ln10, 10)}; a PRECISION "
          f"limit, not a limit of the mathematics)")
    chk("the saturation threshold tracks dps*ln(10) to within 2",
        abs(t_sat - dps_ln10) < 2)

    print("\n   the three documented targets (reachability only, never inverted):")
    target_rows = {}
    for name, t in TARGETS.items():
        ms = m_star(t)
        res = abs(b4(ms) - t) / t
        ok = (0 < ms < ceiling)
        target_rows[name] = {
            "target": fmt(t), "m_star": fmt(ms),
            "ceiling_minus_m_star": fmt(ceiling - ms),
            "roundtrip_rel_residual": fmt(res),
            "m_star_in_open_interval": bool(ok),
        }
        print(f"    {name:<32} t = {mp.nstr(t, 8):>10}  m* = {mp.nstr(ms, 12)}"
              f"  1/sqrt5 - m* = {mp.nstr(ceiling - ms, 6)}")
        chk(f"{name}: m* in (0, 1/sqrt5) and round-trips "
            f"(rel {mp.nstr(res, 4)})", ok and res < mp.mpf("1e-40"))

    # ── 5 · BOTH naive-z conventions — the staleness this closes ─────────
    print("\n5 · naive per-pair magnitude: convention C (excised) vs D (canonical)")
    q0 = mp.mpf(Q0_PROTON_STR)
    zc, zd = z_C_historical(q0), z_D(q0)
    naive = {}
    for label, z, note in (("z_C (EXCISED, historical)", zc,
                            "convention C, owner-excised 2026-08-09 / R1"),
                           ("z_D (CANONICAL)", zd,
                            "convention D, canonical per owner ruling R1")):
        five_z2, d = 5 * z ** 2, detG(z)
        naive[label.split()[0]] = {
            "z": fmt(z), "five_z_squared": fmt(five_z2), "detG": fmt(d),
            "above_ceiling": bool(five_z2 > 1), "excluded": bool(d < 0),
            "note": note,
        }
        print(f"    {label:<28} z = {mp.nstr(z, 12)}  5z^2 = {mp.nstr(five_z2, 10)}"
              f"  det = {mp.nstr(d, 10)}")
        chk(f"{label.split()[0]}: 5z^2 > 1 and det < 0 (EXCLUDED)",
            five_z2 > 1 and d < 0)
    chk("the exclusion STRENGTHENS under canonical D (det_D < det_C < 0)",
        detG(zd) < detG(zc) < 0)

    # ── 6 · every cited Lean declaration must exist ──────────────────────
    print("\n6 · cited Lean declarations exist in the file")
    src = _Path(LEAN).read_text()
    decls = set(re.findall(
        r"^(?:noncomputable )?(?:theorem|lemma|def) ([A-Za-z_][A-Za-z0-9_']*)",
        src, re.M))
    cited = ["detG_eq_spectral_product", "detG_expand", "detG_mem_Ioo",
             "detG_neg_of_above_ceiling", "naive_z_unphysical",
             "zD", "zD_sq", "zD_sq_mem", "zD_unphysical",
             "b4_strictMono_on", "detG_strictAnti",
             "magnitude_form_surjective", "documented_targets_all_reachable",
             "a4_magnitude_one_scalar_gate"]
    missing = [c for c in cited if c not in decls]
    print(f"    {len(decls)} declarations in the file; {len(cited)} cited here")
    chk(f"no cited declaration is missing (missing: {missing or 'none'})",
        not missing)
    chk("the four convention-D declarations the old witness omitted are present",
        all(d in decls for d in ("zD", "zD_sq", "zD_sq_mem", "zD_unphysical")))

    print(f"\n{'ALL CHECKS PASSED' if not fails else str(fails) + ' CHECK(S) FAILED'}")

    # ── witness ──────────────────────────────────────────────────────────
    w = WitnessBuilder("a4-interface-magnitude-one-scalar-gate", start_time=t0)
    w.set_description(
        "A=4 (4He) >=4-body magnitude via the interface operator: the derived "
        "-ln det(I+G) form (exchange spectrum {+-sqrt5, +-1}, #3924) is "
        "SURJECTIVE onto (0,inf) in its single free per-pair bond scalar "
        "m in (0, 1/sqrt5), so every documented target is reachable and each "
        "reaching m is a function of the target -- the magnitude cannot be "
        "closed by computation, only by a principle that FIXES m. "
        "REGENERATED 2026-08-30 by its first producer (bean qou-rv6z): the "
        "committed witness was hand-written with NO provenance (engine, "
        "scriptFile, scriptHash, commitSha, computedAt, q0Anchor, "
        "precisionMetadata, environment all absent) and no script wrote it, so "
        "its numbers were unreproducible. It was also STALE against its own "
        "cited Lean, which carries zD/zD_sq/zD_sq_mem/zD_unphysical (the "
        "convention-D replacement for the excised convention-C naive_z) while "
        "the witness cited only z_C = 0.499320334. Both conventions are now "
        "reported: the exclusion holds under each and STRENGTHENS under "
        "canonical D. Verdict unchanged -- WALL(scope-(a)) magnitude open, "
        "plus the scope-(b) exclusion of the naive uniform z.")
    w.add_data("provenance_note", {
        "regenerated_by": "computations/deltalambda/a4_interface_magnitude_one_scalar_gate.py",
        "previously": "hand-written, no producer, no provenance fields",
        "bean": "qou-rv6z",
        "fields_previously_absent": ["engine", "scriptFile", "scriptHash",
                                     "commitSha", "computedAt", "q0Anchor",
                                     "precisionMetadata", "environment"],
    })
    w.add_data("inputs", {
        "exchange_spectrum": "{+sqrt5, -sqrt5, +1, -1} (derived, "
                             "b4-slater-antisymmetrizer-exchange-sign, #3924)",
        "det_form": "det(I+G) = (1+m sqrt5)(1-m sqrt5)(1+m)(1-m) = (1-5m^2)(1-m^2)",
        "b4_form": "b4(m) = -ln det(I+G)  (attractive branch)",
        "writhe_ceiling": fmt(ceiling),
        "documented_targets_MeV": {k: fmt(v) for k, v in TARGETS.items()},
    })
    w.add_data("results", {
        "det_three_forms_max_disagreement": fmt(worst),
        "det_in_open_unit_interval_on_physical_region": bool(inside),
        "det_negative_above_ceiling": bool(above),
        "b4_strictly_increasing": bool(mono),
        "surjective_onto_positive_reals": True,
        "closed_form_inverse": "m*(t) = sqrt((6 - sqrt(16 + 20 exp(-t)))/10) "
                               "-- root of 5u^2-6u+(1-exp(-t))=0, u=m^2 in (0,1/5)",
        "max_roundtrip_rel_residual_used_range_t_le_10": fmt(rt_worst),
        "roundtrip_digit_budget": decay,
        "digit_loss_law": ("TWO-SIDED. Large t: 1-5m^2 cancels as m* -> the "
                           "ceiling, costing ~t*log10(e) digits. Small t: det "
                           "-> 1 so -ln(det) is a log near 1, costing "
                           "~log10(1/t). Essentially exact at t ~ 1. Checked as "
                           "a LAW rather than against a fixed tolerance, which "
                           "would hide the degradation -- and a one-sided "
                           "version of this law was itself wrong at small t."),
        "closed_form_saturation": {
            "t_threshold_at_this_dps": fmt(t_sat),
            "dps": mp.mp.dps,
            "dps_times_ln10": fmt(dps_ln10),
            "meaning": ("above this t, exp(-t) underflows, m* lands exactly ON "
                        "the ceiling, det = 0 and b4 = -ln 0 = +inf. The form "
                        "is surjective onto (0,inf) MATHEMATICALLY; it is "
                        "numerically usable to t ~ dps*ln(10). A PRECISION "
                        "limit, not a limit of the mathematics -- and the same "
                        "effect the (C2) digit-count result describes from the "
                        "other side: B(4He) at t = 28.3 already sits "
                        "1.44e-13 below the ceiling."),
        },
        "documented_targets_all_reachable": target_rows,
        "not_closed": "no identified categorical driver fixes m; the reaching m "
                      "depends on the target, so matching it is a FIT",
    })
    w.add_data("naive_z_exclusion_both_conventions", naive)
    w.add_data("lean", {
        "file": LEAN,
        "package_ref": "qou:QOU.MassTheory.A4InterfaceMagnitude",
        "sorry_free": True,
        "declarations_in_file": len(decls),
        "cited_and_verified_present": cited,
        "omitted_by_previous_witness": ["zD", "zD_sq", "zD_sq_mem",
                                        "zD_unphysical"],
    })
    w.add_data("scope", {
        "magnitude": "(a) -- open; the form reaches every target so computation "
                     "cannot close it",
        "naive_uniform_z": "(b) -- structurally excluded under BOTH Markov "
                           "conventions; invariant cited = the exchange "
                           "spectrum {+-sqrt5, +-1} fixing det = (1-5m^2)(1-m^2)",
        "free_parameters": 0,
        "targets_never_inverted_into_production": True,
    })
    w.add_data("checks_failed", fails)
    w.add_assertion("det_three_forms_agree", worst < mp.mpf("1e-45"), True)
    w.add_assertion("b4_strictly_increasing", mono, True)
    w.add_assertion("surjective_all_targets_reachable",
                    all(r["m_star_in_open_interval"] for r in target_rows.values()),
                    True)
    w.add_assertion("naive_z_excluded_under_both_conventions",
                    naive["z_C"]["excluded"] and naive["z_D"]["excluded"], True)
    w.add_assertion("exclusion_stronger_under_canonical_D",
                    detG(zd) < detG(zc), True)
    w.add_assertion("all_cited_lean_declarations_exist", not missing, True)
    w.add_assertion("saturation_threshold_tracks_dps",
                    abs(t_sat - dps_ln10) < 2, True)
    w.add_assertion("roundtrip_digits_track_the_law", law_ok, True)
    w.add_assertion("magnitude_closed_by_this_probe", False, False)
    w.save({
        "q0Anchor": "proton",
        "q0Value": str(Q0_PROTON_STR),
        "q0AnchorReason": (
            "the canonical convention-D naive bond factor z_D = q0^3/(q0^2+1) "
            "is evaluated at the proton pin (the standing default, owner "
            "directive 2026-08-07); z_C is reported at the same pin purely as a "
            "named historical delta. The gate itself -- the spectrum, det form, "
            "ceiling, monotonicity and surjectivity -- is q0-independent."),
    })
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
