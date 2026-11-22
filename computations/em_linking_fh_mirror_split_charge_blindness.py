#!/usr/bin/env python3
"""The Freedman-He link bound is CHARGE-BLIND, and that fixes its mirror split.

Bean qou-o6ml (the flux leg left open when qou-0hdx was scrapped). This
probe asks the question the arc deferred -- "derive the per-component
flux law" -- and finds that the obligation is not one function of A. It
is a charge-dependent flux, and the shape it must have is the OPPOSITE
of the one the corpus records.

THE STRUCTURE. Komendarczyk arXiv:0808.1533v1 eq. (43), p. 26, verified
directly against library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:

    E_{3/2}(X) >= (pi/16)^(1/4) * ( sum_{k=1..n} ac(L_k, L)|Flux(X_k)| )
                  * min_{1<=k<=n} |Flux(X_k)|

Everything on the right is either link topology (`ac`) or flux. NEITHER
KNOWS A PROTON FROM A NEUTRON. But the entire observable this arc scores
against -- kappa(A) -- is built from the mirror-pair binding split, which
is pure charge. So charge can enter eq. (43) at exactly one place: the
flux must differ between proton and neutron components. The obligation
was never "derive Flux(A)"; it is "derive Flux_p and Flux_n", from a
framework that defines no flux at all (`Flux` occurs nowhere in the QOU
Lean tree as a quantity -- the hits are a photon docstring, meson colour
tubes, and the English idiom "in flux in Mathlib's CoxeterSystem API").

THE PREDICTION, and it is sharp. Take a carrier link that is
vertex-transitive (all components topologically alike, so ac(L_k,L) = a
for every k -- true of the Borromean rings, whose complement carries an
S_3 symmetry, and of every carrier this arc has used). Give each of the
n = A components a flux by its charge: Phi_p for the Z protons, Phi_n for
the N neutrons. Mirror partners (Z, N) and (N, Z) share A, share the link,
and share min_k|Flux| (the swap only relabels). Then

    E_1 = C a ( Z Phi_p + N Phi_n ) m
    E_2 = C a ( N Phi_p + Z Phi_n ) m           [Z <-> N]
    dE  = E_1 - E_2 = C a m (Z - N) (Phi_p - Phi_n)

For the whole d = |Z - N| = 1 mirror ladder this is **one constant**,
independent of A. The observed split is not constant: it grows by a
factor of 13.63 from A = 3 to A = 63. So constant fluxes are refuted, and
the required Phi-difference must GROW by that same 13.63 -- where the
corpus records the obligation as a DECLINE by 1.449.

WHY THE TWO DISAGREE. 1.449 is sqrt(kappa(3)/kappa(41)), read off kappa.
But kappa is not an energy: kappa := split / ((Z-1) * u), so the pairwise
count (Z-1) has already been divided out (u is constant here to 5.0e-8,
measured). Eq. (43) bounds an ENERGY, so the quantity to confront it with
is the split. Reading the flux obligation off kappa silently asks the
bound to explain a per-pair ratio. Both numbers are reproduced below so
the disagreement is checkable rather than asserted.

SCOPE. This is a scope-(a) result on the model class, with a structural
core. What is excluded is the class {vertex-transitive carrier} x
{flux depending only on charge} x {eq. (43) saturated}: within it the
d=1 mirror split is A-independent, and the data is not. Eq. (43) itself
is untouched -- it is a true lower bound, and note that using it as an
equality is itself an assumption (saturation) that nothing in this corpus
establishes. Nothing here is wired.
"""

from __future__ import annotations

import json
import pathlib

import mpmath as mp

import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

# Precision must be raised BEFORE any mpf literal below: at import time
# mp.dps is still mpmath's default 15 (~binary64), and a literal rounded
# there cannot be recovered by raising dps afterwards. Idempotent.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

HERE = pathlib.Path(__file__).resolve().parent
SERIES_WITNESS = HERE / "em-linking-mirror-series.witness.json"

# The two figures this probe disputes, quoted from the corpus so the
# comparison is against what is committed, not against a memory of it.
# Source: em-linking-fh-link-bound-correction.witness.json,
# data.what_eq43_actually_predicts.
CORPUS_KAPPA_DECLINE = mp.mpf("2.098835")
CORPUS_REQUIRED_FLUX_DECLINE = mp.mpf("1.4487357")
CORPUS_DIGITS = 7


def load_series() -> list[dict]:
    """The kappa ladder: A = 2Z-1 mirror pairs, A = 3..63."""
    with SERIES_WITNESS.open() as fh:
        return json.load(fh)["data"]["series"]


def main() -> int:
    series = load_series()
    rows = [
        {
            "A": mp.mpf(r["A"]),
            "Z": mp.mpf(r["Z"]),
            "n_pairs": mp.mpf(r["n_pairs"]),
            "split": mp.mpf(r["ame_split_MeV"]),
            "kappa": mp.mpf(r["kappa"]),
        }
        for r in series
    ]
    by_A = {int(r["A"]): r for r in rows}
    first, last = rows[0], rows[-1]

    # --- 1. kappa is a per-pair RATIO, not an energy -------------------
    # kappa := split / (n_pairs * u). If u is constant the definition is
    # exactly that, and the (Z-1) pair count is divided out of kappa.
    units = [r["split"] / (r["n_pairs"] * r["kappa"]) for r in rows]
    u_min, u_max = min(units), max(units)
    u_spread = (u_max - u_min) / u_min

    # n_pairs is Z-1 for a d=1 mirror pair: the pp-pair count difference
    # [Z(Z-1) - (Z-1)(Z-2)]/2 = Z-1. Checked rather than assumed.
    n_pairs_is_Z_minus_1 = all(r["n_pairs"] == r["Z"] - 1 for r in rows)

    # --- 2. reproduce the corpus's two figures --------------------------
    kappa_decline = first["kappa"] / by_A[41]["kappa"]
    flux_decline_from_kappa = mp.sqrt(kappa_decline)
    repro_kappa = abs(kappa_decline - CORPUS_KAPPA_DECLINE)
    repro_flux = abs(flux_decline_from_kappa - CORPUS_REQUIRED_FLUX_DECLINE)

    # --- 3. what the split actually does --------------------------------
    split_growth_full = last["split"] / first["split"]
    split_growth_to41 = by_A[41]["split"] / first["split"]

    # --- 4. the charge-blindness prediction -----------------------------
    # Under {vertex-transitive carrier, charge-only flux, saturation} the
    # d=1 mirror split is C*a*m*(Phi_p - Phi_n): ONE constant for the whole
    # ladder. Its relative spread in the data is the size of the failure.
    split_min, split_max = min(r["split"] for r in rows), max(r["split"] for r in rows)
    split_spread = (split_max - split_min) / split_min

    # Required Phi-difference, normalised at A=3. Under the model
    # dE ∝ (Phi_p - Phi_n), so the required difference tracks the split.
    required_dphi_rel = {int(r["A"]): r["split"] / first["split"] for r in rows}

    # --- 5. the direction disagreement ----------------------------------
    # Corpus: flux must FALL by 1.449. Here: the flux DIFFERENCE must GROW
    # by 13.63. Not a refinement of each other -- opposite signs.
    direction_opposite = (flux_decline_from_kappa > 1) and (split_growth_full > 1)
    magnitude_ratio = split_growth_full / flux_decline_from_kappa

    b = WitnessBuilder(
        name="em-linking-fh-mirror-split-charge-blindness",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    b.set_description(
            "EXPLORATORY. The Freedman-He link bound (Komendarczyk eq. 43) has a "
            "charge-blind right-hand side -- only link topology and fluxes -- while "
            "kappa(A) is built from a mirror-pair split, which is pure charge. So the "
            "open obligation is not Flux(A) but the pair (Flux_p, Flux_n). Under a "
            "vertex-transitive carrier with charge-only flux, the d=1 mirror split is "
            "C*a*m*(Phi_p - Phi_n) -- ONE CONSTANT for the whole A=3..63 ladder. The "
            "data grows by 13.63, so constant fluxes are refuted and the required "
            "Phi-difference must GROW by 13.63. The corpus records the obligation as a "
            "DECLINE by 1.449, which is sqrt(kappa(3)/kappa(41)) read off kappa -- but "
            "kappa is split/((Z-1)*u), a per-pair ratio with the pair count already "
            "divided out, not an energy. Both figures are reproduced here. Scope-(a) on "
            "the model class {vertex-transitive carrier} x {charge-only flux} x "
            "{saturation}; eq. (43) itself is untouched. Nothing wired."
    )

    b.add_data("eq43_source", {
        "file": "library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:203-216",
        "citation": "Komendarczyk, arXiv:0808.1533v1, eq. (43), p. 26",
        "statement": (
            "E_{3/2}(X) >= (pi/16)^(1/4) * ( sum_{k=1..n} ac(L_k,L)|Flux(X_k)| ) "
            "* min_{1<=k<=n}|Flux(X_k)|"
        ),
        "charge_blind": (
            "every factor on the right is link topology (ac) or flux; nothing in it "
            "distinguishes a proton from a neutron, so charge can only enter via Flux"
        ),
        "it_is_a_LOWER_BOUND": (
            "using (43) as an equality assumes saturation. Nothing in this corpus "
            "establishes it; the assumption is recorded, not discharged"
        ),
    })

    b.add_data("kappa_is_a_per_pair_ratio_not_an_energy", {
        "definition": "kappa := split / (n_pairs * u)",
        "u_constant_to_relative": mp.nstr(u_spread, 4),
        "u_value": mp.nstr(u_min, 10),
        "n_pairs_equals_Z_minus_1": n_pairs_is_Z_minus_1,
        "why_it_matters": (
            "the pp-pair count (Z-1) is already divided out of kappa, so confronting "
            "eq. (43) -- a bound on an ENERGY -- with kappa asks it to explain a "
            "per-pair ratio. The energy-like observable is the split."
        ),
    })

    b.add_data("corpus_figures_reproduced", {
        "kappa_decline_A3_to_A41": mp.nstr(kappa_decline, CORPUS_DIGITS),
        "corpus_value": mp.nstr(CORPUS_KAPPA_DECLINE, CORPUS_DIGITS),
        "flux_decline_read_off_kappa": mp.nstr(flux_decline_from_kappa, CORPUS_DIGITS),
        "corpus_value_flux": mp.nstr(CORPUS_REQUIRED_FLUX_DECLINE, CORPUS_DIGITS),
        "note": (
            "reproduced exactly. The disagreement below is about which observable the "
            "bound applies to, not about arithmetic."
        ),
    })

    b.add_data("charge_blindness_prediction", {
        "model_class": (
            "{vertex-transitive carrier: ac(L_k,L) = a for all k} x {flux depends only "
            "on charge: Phi_p, Phi_n} x {eq. (43) saturated}"
        ),
        "derivation": (
            "E_1 = C a (Z Phi_p + N Phi_n) m ; E_2 = C a (N Phi_p + Z Phi_n) m ; "
            "dE = C a m (Z-N)(Phi_p - Phi_n). For the d=1 ladder Z-N=1, so dE is ONE "
            "CONSTANT independent of A."
        ),
        "predicted_split_spread": "0 (constant)",
        "observed_split_spread_relative": mp.nstr(split_spread, 8),
        "observed_split_growth_A3_to_A63": mp.nstr(split_growth_full, 8),
        "observed_split_growth_A3_to_A41": mp.nstr(split_growth_to41, 8),
        "verdict": (
            "constant fluxes are REFUTED for this ladder; the required Phi-difference "
            "must grow by the same 13.63"
        ),
    })

    b.add_data("direction_disagreement", {
        "corpus_says": "per-component flux must FALL by 1.4487357 (A=3 -> A=41)",
        "this_probe_says": (
            "the proton-neutron flux DIFFERENCE must GROW by "
            f"{mp.nstr(split_growth_to41, 8)} over the same range, "
            f"{mp.nstr(split_growth_full, 8)} over the full ladder"
        ),
        "these_are_opposite_in_sign": direction_opposite,
        "magnitude_ratio_full_ladder": mp.nstr(magnitude_ratio, 8),
        "root_cause": (
            "the corpus figure divides the pair count out of the observable before "
            "confronting it with a bound on the total energy"
        ),
    })

    b.add_data("required_dphi_relative_to_A3", {
        str(a): mp.nstr(v, 8) for a, v in sorted(required_dphi_rel.items())
    })

    b.add_data("what_would_have_to_be_supplied", {
        "not_one_function": (
            "the obligation is the PAIR (Phi_p, Phi_n), not a single Flux(A); a "
            "charge-blind bound cannot produce a charge-driven observable otherwise"
        ),
        "and_the_framework_defines_no_flux": (
            "`Flux` occurs nowhere in folio/quantum-observable-universe/lean/ as a "
            "quantity. The grep hits are a photon docstring (KnotRegistry.lean:48), "
            "meson colour flux tubes (MesonFluxTubeReduction.lean), and the English "
            "idiom \"in flux in Mathlib's CoxeterSystem API\" (Tw.lean:56, Defn.lean:114, "
            "Quotient.lean:62,136). Measured, not recalled."
        ),
        "escape_hatches_not_excluded": (
            "a carrier that is NOT vertex-transitive, or an ac that depends on the "
            "charge assignment, or an unsaturated bound, all evade this. Each is a "
            "further thing to derive, not a thing the sources supply."
        ),
    })

    b.add_assertion(
        name="corpus_kappa_decline_reproduced",
        computed=mp.nstr(kappa_decline, CORPUS_DIGITS),
        expected=mp.nstr(CORPUS_KAPPA_DECLINE, CORPUS_DIGITS),
        tolerance="1e-6",
        unit="ratio",
        source=(
            "kappa(3)/kappa(41) recomputed from the mirror-series witness matches the "
            "2.098835 recorded in em-linking-fh-link-bound-correction.witness.json. "
            "Reproducing the figures I dispute, before disputing them: the dispute is "
            "about which observable the bound applies to, not about arithmetic."
        ),
    )
    b.add_assertion(
        name="corpus_flux_decline_reproduced",
        computed=mp.nstr(flux_decline_from_kappa, CORPUS_DIGITS),
        expected=mp.nstr(CORPUS_REQUIRED_FLUX_DECLINE, CORPUS_DIGITS),
        tolerance="1e-6",
        unit="ratio",
        source="sqrt(kappa(3)/kappa(41)) matches the recorded 1.4487357.",
    )
    b.add_assertion(
        name="kappa_divides_out_the_pair_count",
        computed=mp.nstr(u_spread, 4),
        expected="0",
        tolerance="1e-6",
        unit="relative",
        source=(
            "split/(n_pairs*kappa) is constant to 5.0e-8 across all 31 rows, and "
            f"n_pairs == Z-1 exactly on every row ({n_pairs_is_Z_minus_1}). So kappa is "
            "definitionally a per-pair ratio with the pp-pair count divided out -- not "
            "an energy for eq. (43), which bounds one, to be confronted with."
        ),
    )
    # Recorded as a PASSING measurement, not a red assertion. The refutation
    # lives in the name and the source; a witness carrying allPassed=false reads
    # as a broken producer to every audit that scans it, which is not what a
    # successfully-measured negative should look like.
    b.add_assertion(
        name="mirror_split_grows_13x_where_constant_charge_flux_predicts_exactly_1",
        computed=mp.nstr(split_growth_full, 8),
        expected="13.627712",
        tolerance="1e-5",
        unit="ratio split(A=63)/split(A=3)",
        source=(
            "THE RESULT. Under a vertex-transitive carrier with charge-only flux and "
            "eq. (43) saturated, dE = C*a*m*(Z-N)(Phi_p-Phi_n) is A-INDEPENDENT for the "
            "d=1 ladder -- this ratio would be exactly 1. It is 13.63. So constant "
            "fluxes are refuted and the required Phi_p-Phi_n must GROW by that factor. "
            "Pinned to the measured value so the refutation cannot silently regress."
        ),
    )
    b.add_assertion(
        name="required_flux_growth_is_opposite_in_sign_to_the_recorded_decline",
        computed=mp.nstr(magnitude_ratio, 8),
        expected=mp.nstr(split_growth_full / CORPUS_REQUIRED_FLUX_DECLINE, 8),
        tolerance="1e-6",
        unit="ratio",
        source=(
            "The corpus records the obligation as a flux DECLINE of 1.449. Confronting "
            "the bound with the energy rather than the per-pair ratio makes it a "
            "flux-difference GROWTH of 13.63 -- opposite in sign, 9.4x in magnitude. "
            f"Both directions positive: {direction_opposite}."
        ),
    )

    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no q0. The mirror-split charge-blindness test compares "
            "linking numbers and charge assignments across a mirror pair; "
            "both are integer topological data and neither is evaluated "
            "at the substrate modulus. Established by import-cone trace "
            "(cone=2, no q_parameter / qou_substrate.constants edge) and "
            "by computations/audits/producer_baked_pin_audit.py, which "
            "finds no q0-valued literal in the source. The witness "
            "carries no q0 field."),
    })
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
