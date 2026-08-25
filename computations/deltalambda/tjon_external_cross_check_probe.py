#!/usr/bin/env python3
"""tjon_external_cross_check_probe.py — the Tjon inputs re-derived from AME2020,
and the corpus ladder scored against the field's own dimensionless target.

Closes three QA beans raised by `local/paper-relevance-triage` against
`gap10_tjon_correlation_probe.py`:

  qou-3o9x  re-derive the AME-transcribed literals from library/mass_1.mas20.txt
  qou-f3ec  cross-check against the universal Tjon curve  [hammer2007fourbody]
  qou-l4cm  cross-check against the LO-EFT B_alpha        [platter2005tjon]

────────────────────────────────────────────────────────────────────────────
PART A — the AME inputs, derived rather than transcribed  (qou-3o9x)
────────────────────────────────────────────────────────────────────────────

`gap10_tjon_correlation_probe.py` carries

    RHO_STRONG = {2: 1, 3: "3.8128", 4: "13.0316"}

as hand-typed literals with a one-line comment ("Coulomb-corrected") and no
source. This part parses AME2020 directly, so a re-upload or a new evaluation
is caught by the file's `source_sha` instead of silently persisting behind a
literal that nothing re-derives.

Two things fall out, both worth recording:

* **`3.8128` is a 5-digit rounding.** The AME2020 value is `3.8127866`, so the
  literal is off by `3.5e-6` relative. Harmless at the 2-significant-figure
  level the Tjon score is read at, but it is a silent precision loss in a file
  that otherwise runs at 30 dps, and it is invisible without this derivation.

* **`13.0316` is NOT an AME ratio at all.** The raw AME value is `12.7196`.
  The literal implies `B = 28.9897 MeV`, i.e. a Coulomb correction of
  `+0.694 MeV` on top of the AME `28.2957`. That correction had no source
  anywhere in the corpus; it is checked here against the Coulomb-corrected
  `B_alpha^exp = 29.0 +/- 0.1 MeV` of [platter2005tjon] p. 5, which it is
  inside. The correction is now sourced, and the probe asserts it.

────────────────────────────────────────────────────────────────────────────
PART B — the external cross-check, and what it actually shows  (qou-f3ec/l4cm)
────────────────────────────────────────────────────────────────────────────

The beans asked for the corpus ladder to be scored against the field's own
target rather than only against three AME numbers, with the standing condition
that a mismatch is informative either way and an agreement must NOT be
back-fitted into any weight. Nothing here is fitted; nothing is wired.

[hammer2007fourbody] §III.B supplies the target: solving the four-boson
Yakubovsky equations with **no four-body parameter**, they find that away from
threshold the four-body ground state and the deepest three-body state are
related by a factor of `5`. That is dimensionless, convention-free, and — the
point — it is a ratio produced by a calculation containing no four-body input.

Stated that weakly on purpose. "No four-body parameter is needed to renormalise
at LO" is NOT "no four-body force exists": [jurgenson2009srg] puts the
four-nucleon force at tens to a few hundred keV, small but nonzero. The authors
also flag that their universality rests on the RG analysis of their ref. [12],
which Yamashita et al. dispute (§I, p. 3) — a dispute that explicitly *exempts*
the nuclear case, "4He atoms and nucleons (where this sensitivity is absent)",
which is the case at issue here. The argument needs only the weak reading, so
it takes only the weak reading.

The finding is not a score. Feeding `M(4) = 5*M(3)` into the simplex basis
gives (Lean `universal_ratio_forces_mu4`, sorry-free)

    mu4 = 9*mu2 + mu3

which at the nuclear `(mu2, mu3)` is `9.81` — about `2.6x` the value the
nuclear data themselves produce. **mu4 is largest in a calculation that carries
no four-body input at all**, which is a stronger form of the claim
`TjonSimplexForm` was already making on structural grounds.

And it is an exclusion, not merely a comparison: on the `mu4 = 0` baseline
`M(4) < 4*M(3)` strictly for any `mu2 > 0`, whatever `mu3` is (Lean
`tjon_baseline_lt_four_ratio`), so the ratio `5` is outside the baseline's
reachable range entirely. The EFT's "no four-body parameter at leading order"
and the simplex's `mu4 = 0` are therefore provably different conditions
(`universal_ratio_not_in_tjon_baseline`). [platter2005tjon] is cited by
`TjonSimplexForm` as motivation for the baseline; this is why it may not be
cited as a derivation of it.

For the corpus operator the external number makes the standing gap WIDER, not
narrower. The three ladders order as

    operator  ~1.18   <   nature  3.42   <   universal  5

so the surviving GAP-10 negative — the operator's ladder is too flat in A —
is reinforced by the field's own value. Scope-(a): this is a negative on the
operator's growth, against one more target; it excludes no ingredient.

[platter2005tjon]'s own LO numbers are carried through as the third comparison:
`B_alpha = 29.5 MeV` (a_t input) / `26.9` (B_d input) against the experimental
`29.0 +/- 0.1`, and the paper's note that the LO Tjon line is shifted from the
empirical one because finite-range effects are neglected — which is why nature
at `3.42` sits below the zero-range `5` rather than at it.

Operator ladder values are read from the committed GAP-10 witness (convention D)
rather than recomputed: the H_12 traces cost minutes and this probe changes
nothing about them. The witness path and its recorded scriptHash are asserted,
so a stale read is caught.

Convention D throughout (owner ruling 2026-08-09). Nothing fitted, nothing
wired, no Delta_lambda touched.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
REPO = COMP.parent
sys.path[:0] = [str(COMP), str(COMP / "hecke"), str(COMP / "habiro"),
                str(COMP / "substrate"), str(HERE)]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)

AME_PATH = REPO / "library" / "mass_1.mas20.txt"
GAP10_WITNESS = HERE / "gap10-tjon-correlation.witness.json"

# The literals gap10_tjon_correlation_probe.py carries, re-derived below.
RHO_STRONG_LITERAL = {2: mp.mpf(1), 3: mp.mpf("3.8128"), 4: mp.mpf("13.0316")}

# [platter2005tjon] p. 5, quoted verbatim in the ref note. Comparison targets
# only — never adopted, never fitted to.
PLATTER_B_ALPHA_EXP = mp.mpf("29.0")      # Coulomb-corrected experimental
PLATTER_B_ALPHA_EXP_UNC = mp.mpf("0.1")
PLATTER_B_ALPHA_LO_AT = mp.mpf("29.5")    # LO, a_t two-body input
PLATTER_B_ALPHA_LO_BD = mp.mpf("26.9")    # LO, B_d two-body input

# [hammer2007fourbody] §III.B: "Away from the thresholds, the binding energies
# of the ground and excited four-body states are related to the deepest
# three-body state by factors of 5 and 1.01, respectively."
# Contested in general (Yamashita et al., §I p.3) but NOT for the nuclear case,
# which those authors explicitly exempt. See the module docstring.
UNIVERSAL_B4_OVER_B3 = mp.mpf(5)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def read_ame_binding(path: Path):
    """B(A) in MeV for 2H, 3H, 4He from the AME2020 mass table.

    AME2020 `mass.mas20` fixed-width layout, per the file's own format block:
    columns 17-20 are A, 21-23 the element, and the third numeric field is
    BINDING ENERGY/A in keV. So B = A * (BE/A) / 1000.

    DO NOT refactor this onto `computations/vendor_ame2020.parse_line`.
    That module parses the same table — and `computations/data/ame2020.mas20.txt`
    is byte-identical to `library/mass_1.mas20.txt`, same sha256, so the two
    copies are not a divergence risk. The blocker is precision: its
    `_parse_value` returns `float(s)`, i.e. **float64**. Routing a binding
    energy through float64 before it reaches a witness is exactly what the
    NO-FLOAT64 discipline forbids, and it would put this probe back on the
    raw-float64 ratchet. `mp.mpf(<decimal string>)` below is exact from the
    source characters; `float()` is not.

    Reuse of the vendor module becomes correct the moment `_parse_value`
    carries `mpmath.mpf` instead — at which point delete this parser and
    call it.
    """
    want = {(2, "H"): "2H", (3, "H"): "3H", (4, "He"): "4He"}
    out = {}
    for line in path.read_text(encoding="latin-1").splitlines():
        if len(line) < 60 or not line[16:20].strip().isdigit():
            continue
        key = (int(line[16:20]), line[20:23].strip())
        if key not in want:
            continue
        # mass excess, its uncertainty, then BE/A: take the third float.
        fields = line[23:].replace("#", ".").split()
        be_per_a = mp.mpf(fields[2])
        out[want[key]] = key[0] * be_per_a / 1000
    missing = set(want.values()) - set(out)
    if missing:
        raise SystemExit(f"AME parse failed, missing {sorted(missing)}")
    return out


def main() -> int:
    print("=" * 74)
    print("TJON EXTERNAL CROSS-CHECK — AME2020 re-derivation + universal target")
    print("=" * 74)

    if not AME_PATH.exists():
        raise SystemExit(f"missing AME table: {AME_PATH}")
    if not GAP10_WITNESS.exists():
        raise SystemExit(f"missing GAP-10 witness: {GAP10_WITNESS}")

    # ── PART A: derive the inputs ───────────────────────────────────────
    ame_sha = sha256(AME_PATH)
    B = read_ame_binding(AME_PATH)
    print(f"\n[A] AME2020  {AME_PATH.relative_to(REPO)}  sha256 {ame_sha[:16]}…")
    for k in ("2H", "3H", "4He"):
        print(f"      B({k:3s}) = {mp.nstr(B[k], 12):>14s} MeV")

    r3_derived = B["3H"] / B["2H"]
    r4_derived_raw = B["4He"] / B["2H"]
    r3_lit = RHO_STRONG_LITERAL[3]
    r4_lit = RHO_STRONG_LITERAL[4]

    r3_rel = abs(r3_lit - r3_derived) / r3_derived
    b4_implied = r4_lit * B["2H"]
    coulomb_implied = b4_implied - B["4He"]
    coulomb_ok = abs(b4_implied - PLATTER_B_ALPHA_EXP) <= PLATTER_B_ALPHA_EXP_UNC

    print(f"\n      rho_strong[3] literal {mp.nstr(r3_lit, 8)}  vs derived "
          f"{mp.nstr(r3_derived, 12)}   rel {mp.nstr(r3_rel, 4)}")
    print(f"        -> the literal is a 5-digit ROUNDING of the AME value.")
    print(f"      rho_strong[4] literal {mp.nstr(r4_lit, 8)}  vs derived RAW "
          f"{mp.nstr(r4_derived_raw, 12)}")
    print(f"        -> not an AME ratio: implies B = {mp.nstr(b4_implied, 8)} MeV, "
          f"i.e. Coulomb +{mp.nstr(coulomb_implied, 4)} MeV")
    print(f"        -> [platter2005tjon] p.5 gives B_alpha^exp(Coulomb-corr) = "
          f"{PLATTER_B_ALPHA_EXP} +/- {PLATTER_B_ALPHA_EXP_UNC};  inside: {coulomb_ok}")

    # ── PART B: the simplex moments on each ladder ──────────────────────
    def moments(m2, m3, m4):
        """(mu2, mu3, mu4) from M(2), M(3), M(4) in the C(A,k) basis."""
        mu2 = m2
        mu3 = m3 - 3 * mu2
        mu4 = m4 - 6 * mu2 - 4 * mu3
        return mu2, mu3, mu4

    nat_mu = moments(mp.mpf(1), r3_lit, r4_lit)
    nat_ratio = r4_lit / r3_lit

    # the universal system, normalised to the same M(2) and M(3) as nature so
    # only the four-body ratio differs
    uni_m4 = UNIVERSAL_B4_OVER_B3 * r3_lit
    uni_mu = moments(mp.mpf(1), r3_lit, uni_m4)
    # Lean universal_ratio_forces_mu4: mu4 = 9*mu2 + mu3
    uni_mu4_lean = 9 * nat_mu[0] + nat_mu[1]

    print(f"\n[B] simplex moments  (mu2, mu3, mu4)  in the C(A,k) basis")
    print(f"      nature    M = (1, {mp.nstr(r3_lit, 8)}, {mp.nstr(r4_lit, 8)})"
          f"   -> mu = ({mp.nstr(nat_mu[0], 6)}, {mp.nstr(nat_mu[1], 6)}, "
          f"{mp.nstr(nat_mu[2], 6)})")
    print(f"      universal M = (1, {mp.nstr(r3_lit, 8)}, {mp.nstr(uni_m4, 8)})"
          f"   -> mu = ({mp.nstr(uni_mu[0], 6)}, {mp.nstr(uni_mu[1], 6)}, "
          f"{mp.nstr(uni_mu[2], 6)})")
    print(f"      Lean universal_ratio_forces_mu4:  mu4 = 9*mu2 + mu3 = "
          f"{mp.nstr(uni_mu4_lean, 8)}   matches: "
          f"{abs(uni_mu4_lean - uni_mu[2]) < mp.mpf('1e-25')}")
    print(f"      -> mu4 is {mp.nstr(uni_mu[2] / nat_mu[2], 4)}x LARGER for the "
          f"system with NO four-body force than for nature.")

    # the exclusion: mu4 = 0 baseline can never reach ratio 5
    baseline_m4 = 4 * r3_lit - 6 * mp.mpf(1)     # tjonPredict at nature's mu2,mu3
    baseline_ratio = baseline_m4 / r3_lit
    print(f"\n      mu4 = 0 baseline at nature's (mu2, mu3):  M(4) = "
          f"{mp.nstr(baseline_m4, 8)},  ratio {mp.nstr(baseline_ratio, 6)}")
    print(f"      Lean tjon_baseline_lt_four_ratio: the baseline ratio is < 4 for "
          f"ANY mu2 > 0, so the universal 5 is UNREACHABLE on it.")

    # ── operator ladder, read from the committed GAP-10 witness ─────────
    w = json.loads(GAP10_WITNESS.read_text())
    tj = w["data"]["tjon_correlation"]
    w_hash = w["scriptHash"]
    gap10_src = HERE / w["scriptFile"]
    gap10_fresh = sha256(gap10_src)[:len(w_hash)]
    gap10_current = gap10_fresh == w_hash
    conventions = {k: v for k, v in tj["results"].items() if k != "nature"}

    print(f"\n[C] operator ladders (GAP-10 witness, convention D)")
    print(f"      producer {w['scriptFile']}  scriptHash {w_hash}  "
          f"fresh {gap10_fresh}  current: {gap10_current}")
    if not gap10_current:
        print("      ⚠ the GAP-10 witness is STALE against its producer — the "
              "ladders below are not what the current producer emits.")
    ladders = {}
    for name, res in conventions.items():
        lad = {a: mp.mpf(res["ladder_normalised"][a]) for a in ("2", "3", "4")}
        ratio43 = lad["4"] / lad["3"]
        op_mu = moments(lad["2"], lad["3"], lad["4"])
        ladders[name] = {
            "ladder": {a: fmt(lad[a]) for a in ("2", "3", "4")},
            "ratio_M4_over_M3": fmt(ratio43),
            "mu": {"2": fmt(op_mu[0]), "3": fmt(op_mu[1]), "4": fmt(op_mu[2])},
            "gap_to_universal": fmt(UNIVERSAL_B4_OVER_B3 / ratio43),
            "gap_to_nature": fmt(nat_ratio / ratio43),
            "_r43": ratio43,
        }
        print(f"      {name}")
        print(f"        M(4)/M(3) = {mp.nstr(ratio43, 8)}"
              f"   mu3 = {mp.nstr(op_mu[1], 6)}  mu4 = {mp.nstr(op_mu[2], 6)}")
        print(f"        short of nature by {mp.nstr(nat_ratio / ratio43, 4)}x, "
              f"of universal by {mp.nstr(UNIVERSAL_B4_OVER_B3 / ratio43, 4)}x")

    best_ratio = max(v["_r43"] for v in ladders.values())
    print(f"\n      ORDERING:  operator {mp.nstr(best_ratio, 4)}  <  nature "
          f"{mp.nstr(nat_ratio, 4)}  <  universal {UNIVERSAL_B4_OVER_B3}")
    print("      The external target widens the ladder gap; it does not close it.")

    verdict = (
        f"AME2020 re-derivation: rho_strong[3] literal 3.8128 is a 5-digit rounding of the "
        f"derived {mp.nstr(r3_derived, 10)} (rel {mp.nstr(r3_rel, 3)}); rho_strong[4] literal "
        f"13.0316 is NOT an AME ratio (raw {mp.nstr(r4_derived_raw, 10)}) but implies "
        f"B = {mp.nstr(b4_implied, 8)} MeV, a Coulomb correction of "
        f"+{mp.nstr(coulomb_implied, 4)} MeV now sourced to [platter2005tjon]'s "
        f"B_alpha^exp = 29.0 +/- 0.1 (inside: {coulomb_ok}). CROSS-CHECK against "
        f"[hammer2007fourbody]'s universal B4/B3 = 5, the field's own parameter-free "
        f"target: feeding that ratio into the C(A,k) basis gives mu4 = 9*mu2 + mu3 = "
        f"{mp.nstr(uni_mu[2], 6)}, i.e. {mp.nstr(uni_mu[2] / nat_mu[2], 3)}x LARGER than "
        f"nature's mu4 for a calculation that carries NO four-body input at all — a stronger "
        f"form of TjonSimplexForm's thesis that mu4's size is a basis artifact. (Weak reading "
        f"only: 'no four-body parameter needed at LO' is not 'no four-body force exists'; "
        f"[jurgenson2009srg] puts the 4N force at tens-to-hundreds of keV, and Yamashita et al. "
        f"dispute the LO claim generally while exempting nucleons, the case at issue.) Sharper: the "
        f"mu4 = 0 baseline has M(4) < 4*M(3) strictly for any mu2 > 0 (Lean "
        f"tjon_baseline_lt_four_ratio), so ratio 5 is outside its reachable range and the "
        f"EFT's 'no four-body parameter' is PROVABLY NOT the simplex's mu4 = 0 "
        f"(universal_ratio_not_in_tjon_baseline) — the paper motivates the baseline, it does "
        f"not derive it. For the operator the external number makes the standing gap WIDER: "
        f"operator {mp.nstr(best_ratio, 4)} < nature {mp.nstr(nat_ratio, 4)} < universal 5. "
        f"Scope-(a) NEGATIVE on the operator's ladder growth against one further target; no "
        f"ingredient excluded, nothing fitted, nothing wired."
    )
    print(f"\n ⇒ {verdict}")

    for v in ladders.values():
        v.pop("_r43", None)

    wb = WitnessBuilder("tjon-external-cross-check", engine="mpmath")
    wb.set_description(
        "Closes QA beans qou-3o9x (re-derive the AME2020 literals of "
        "gap10_tjon_correlation_probe.py from library/mass_1.mas20.txt so a re-upload is "
        "caught by source_sha), qou-f3ec and qou-l4cm (cross-check the corpus Tjon ladder "
        "against the external sources, mismatch informative either way, no back-fitting). "
        "Part A derives B(2H), B(3H), B(4He) from the AME2020 mass table and shows "
        "rho_strong[3] is a 5-digit rounding while rho_strong[4] is a Coulomb-corrected "
        "value whose +0.694 MeV correction had no source in the corpus and is now checked "
        "against [platter2005tjon]. Part B scores against [hammer2007fourbody]'s universal "
        "B4/B3 = 5 and finds the simplex basis assigns that no-four-body-force system a "
        "LARGER mu4 than nature's, with the mu4 = 0 baseline provably unable to reach "
        "ratio 5 at all. Lean backing: QOU.MassTheory.TjonSimplexForm "
        "universal_ratio_forces_mu4, tjon_baseline_lt_four_ratio, "
        "universal_ratio_not_in_tjon_baseline, four_sub_two_mul_three (sorry-free, generic "
        f"CommRing). VERDICT: {verdict}")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_data("tjon_external_cross_check", {
        "lean": ("QOU.MassTheory.TjonSimplexForm: universal_ratio_forces_mu4, "
                 "tjon_baseline_lt_four_ratio, universal_ratio_not_in_tjon_baseline, "
                 "four_sub_two_mul_three, two_mu3_add_mu4_neg_of_flat"),
        "ame2020": {
            "source": str(AME_PATH.relative_to(REPO)),
            "source_sha256": ame_sha,
            "binding_MeV": {k: fmt(v) for k, v in B.items()},
            "ratio_3H_over_2H_derived": fmt(r3_derived),
            "ratio_4He_over_2H_derived_raw": fmt(r4_derived_raw),
            "literal_rho_strong": {str(a): fmt(RHO_STRONG_LITERAL[a]) for a in (2, 3, 4)},
            "literal_3_relative_error": fmt(r3_rel),
            "literal_4_implied_B_MeV": fmt(b4_implied),
            "literal_4_implied_coulomb_MeV": fmt(coulomb_implied),
            "coulomb_inside_platter_band": coulomb_ok,
        },
        "external_targets": {
            "universal_B4_over_B3": fmt(UNIVERSAL_B4_OVER_B3),
            "universal_source": "[hammer2007fourbody] §III.B, nucl-th/0610105",
            "platter_B_alpha_exp_MeV": fmt(PLATTER_B_ALPHA_EXP),
            "platter_B_alpha_LO_at_MeV": fmt(PLATTER_B_ALPHA_LO_AT),
            "platter_B_alpha_LO_Bd_MeV": fmt(PLATTER_B_ALPHA_LO_BD),
            "platter_source": "[platter2005tjon] p.5, nucl-th/0409040",
        },
        "moments": {
            "nature": {"2": fmt(nat_mu[0]), "3": fmt(nat_mu[1]), "4": fmt(nat_mu[2])},
            "universal": {"2": fmt(uni_mu[0]), "3": fmt(uni_mu[1]), "4": fmt(uni_mu[2])},
            "universal_over_nature_mu4": fmt(uni_mu[2] / nat_mu[2]),
            "baseline_mu4_zero_ratio": fmt(baseline_ratio),
        },
        "operator": ladders,
        "gap10_witness_scriptHash": w_hash,
        "gap10_producer_hash_fresh": gap10_fresh,
        "gap10_witness_current": gap10_current,
        "verdict": verdict,
    })
    wb.add_assertion("ame_literal_3_matches_to_5_digits", str(r3_rel < mp.mpf("1e-5")), "True")
    wb.add_assertion("ame_literal_4_is_not_raw_ratio",
                     str(abs(r4_lit - r4_derived_raw) > mp.mpf("0.1")), "True")
    wb.add_assertion("coulomb_correction_inside_platter_band", str(coulomb_ok), "True")
    wb.add_assertion("universal_mu4_exceeds_nature_mu4",
                     str(uni_mu[2] > nat_mu[2]), "True")
    wb.add_assertion("universal_ratio_outside_mu4_zero_baseline",
                     str(baseline_ratio < 4 < UNIVERSAL_B4_OVER_B3), "True")
    wb.add_assertion("operator_ladder_below_nature_and_universal",
                     str(best_ratio < nat_ratio < UNIVERSAL_B4_OVER_B3), "True")
    wb.add_assertion("gap10_witness_not_stale_against_producer", str(gap10_current), "True")
    wb.save()
    print("\nwitness → tjon-external-cross-check.witness.json")
    print("STRUCTURAL ASSERTIONS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
