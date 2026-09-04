#!/usr/bin/env python3
"""tau_dictionary_hauptmodul_validator.py — the t₅(τ₀) = −10 hauptmodul gate as a
discrete validator on q₀ ↦ τ dictionary candidates.

Consumer of uploaded-papers audit idea A2 (the Γ₀(5) hauptmodul gate,
docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md §A2), in the
same spirit as the A3 integer-trace prune. Companion to:

  - QOU/Archimedean/BringHauptmodulGate.lean  (exact-rational arithmetic lock:
    t = −10 is a root of (t²+250t+3125)³ + (121945/32)t⁵; Fricke 5³/(−10) = −25/2)
  - computations/probes/bring_hauptmodul_gate_probe.py  (the gate itself:
    η-quotient numerics at BDH22's τ₀ = −0.5 + 0.186676i land on −10)

THE GATE (RR92 Thm 1 gauge). Bring's modulus τ₀ is unique only mod Γ₀(5)
(Riera–Rodríguez 1992 Thm 1), so the invariant coordinate of the modulus is the
genus-0 hauptmodul of X₀(5),

    t₅(τ) = (η(τ)/η(5τ))⁶,   with  t₅(τ₀) = −10  exactly,

and the Fricke companion j(5τ₀) = 5³/t₅(τ₀) = −25/2. Any physical q₀ ↦ τ
dictionary is physical only through Γ₀(5)-invariants and must land on the
Γ₀(5)-class with t₅ = −10 — a discrete, parameter-free pass/fail: a candidate
dictionary missing t₅ = −10 is refuted-as-stated (scope-(a)) with no precision
search. Because t₅ and τ ↦ j(5τ) are Γ₀(5)-invariant, evaluating them at the
candidate τ directly tests CLASS membership — no orbit search is needed.

q₀-PIN INDEPENDENCE. The gate constrains the τ side only (t₅ = −10 has no q₀
in it); it is identical under the muon pin and the proton pin (AGENTS.md §q₀
anchor convention). Candidate MAPS may be evaluated at either pin; the two pins
differ by ~1.6e-8 relative, far below any verdict boundary here, and every
candidate below is evaluated at BOTH pins to demonstrate verdict stability.

CANDIDATES (corpus enumeration, 2026-07-24):

  REF  τ₀ = −0.5 + 0.186676i (BDH22 §2.2) — control; must PASS.
  C1   The exact nome dictionary τ = i·|ln q₀|/(2π) — the ONE concrete
       q₀ ↦ τ map the corpus has stated (tranche 7,
       computations/alpha_em/alpha_em_modular_family_probe.py, "the corpus's
       own B1 fibre dictionary"; zero free constants). Tier: caveated working
       choice (weight families under it already killed, scope-(a)).
  C1n  Naive nome branch τ = ln(q₀)/(2πi) — at real q₀ > 1 this lands in the
       LOWER half-plane (Im τ < 0): ill-defined as a modulus as stated.
  S1   STRAWMAN τ = i·ln q₀ (the canonical rate λ = ln q as pure-imaginary
       modulus). Demonstration only — NOT a proposal.
  S2   STRAWMAN τ = i·ℏ_q, ℏ_q = 1 − q₀⁻¹. Demonstration only — NOT a proposal.
  S3   STRAWMAN τ = −1/2 + i·ln q₀ (half-shift mimicking Re τ₀ = −1/2).
       Demonstration only — NOT a proposal.

Already-pruned method classes NOT point-evaluable here (recorded in the audit
doc, not in this witness): the reciprocal power-law q ↔ heat-time dictionaries
t = c/|λ|^p (killed, 2026-07-18-alpha-em-qt-dictionary-shape.md — target is
heat time, not a modulus) and endpoint-anchored period-side dictionaries
(polarization-blind, 2026-07-19-bring-polarized-q-dictionary-endpoint-
blindness.md — this gate composes with that constraint as a second,
independent discrete filter).

TOLERANCE LADDER (documented, pre-stated):

  ill-defined      Im τ ≤ 0 — the map does not produce a point of ℍ.
  PASS             |t₅(τ) + 10| ≤ 1e-3  AND  |j(5τ) + 25/2| ≤ 1.0
                   (matches bring_hauptmodul_gate_probe.py's tolerances; the
                   reference τ₀ is published to 6 d.p. only, so ~1e-5..1e-4
                   residuals are τ₀-truncation-limited, not compute-limited).
  NEAR             1e-3 < |t₅(τ) + 10| ≤ 1e-1 — numerically ambiguous; demands
                   a higher-precision candidate τ before any verdict.
  FAIL             |t₅(τ) + 10| > 1e-1 — refuted-as-stated (scope-(a)): the
                   map, as stated, does not land on the Bring class.

VALIDATOR SELF-CHECKS (validate the validator, all asserted):
  (i)   control: t₅(τ₀) ≈ −10, j(5τ₀) ≈ −25/2;
  (ii)  Γ₀(5)-invariance: t₅(τ₀+1) and t₅(τ₀/(5τ₀+1)) equal t₅(τ₀);
  (iii) Fricke: t₅(−1/(5τ₀)) ≈ 5³/t₅(τ₀) = −25/2;
  (iv)  sensitivity: t₅(i) is far from −10 (a non-class point FAILs).

Nothing here is wired to production; audit-only witness; NO FIT — no candidate
is tuned toward the gate, and a FAIL is a scope-(a) refutation of the stated
map only, never of any categorical ingredient.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Keeps
# flat-namespace imports (`from witness_base import …`) working from the
# `probes/` cluster subdirectory. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402
del _sys, _Path, _bridge

from mpmath import mp, mpc, mpf, exp, log, pi, kleinj  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# ── the two q₀ pins (AGENTS.md §q₀ anchor convention) ──────────────────────
# Both pins read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). The
# muon leg was the literal 1.1099785955573... -- the RETIRED self-certified
# pin A, superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. A
# mu-vs-p comparison whose muon leg is a retired literal compares live proton
# against yesterday's muon, which is the failure it exists to measure.
# Exception E1 of the 2026-08-30 ruling: both pins are read here on purpose.
Q0_MUON = mp.nstr(q_muon_at(50), 50, strip_zeros=False)
Q0_PROTON = Q_50_DIGIT_STR

# ── gate constants (exact side: BringHauptmodulGate.lean) ──────────────────
T5_TARGET = -10          # t₅(τ₀) = −10 exactly (rational root of the sextic)
J5_TARGET = mpf(-25) / 2  # Fricke companion j(5τ₀) = 5³/(−10) = −25/2

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# ── tolerance ladder (pre-stated; see module docstring) ────────────────────
TOL_PASS_T5 = mpf("1e-3")   # matches bring_hauptmodul_gate_probe.py
TOL_PASS_J5 = mpf("1.0")    # matches bring_hauptmodul_gate_probe.py j check
TOL_NEAR_T5 = mpf("1e-1")


def dedekind_eta(tau):
    """η(τ) = q^{1/24} ∏_{n≥1} (1 − qⁿ), q = e^{2πiτ}. Direct q-product
    (matching bring_hauptmodul_gate_probe.py's method) with ADAPTIVE term
    count: N chosen so |q|^N < 10^-(dps+10), covering candidates near the
    real axis (small Im τ) where 400 fixed terms would under-converge."""
    im = mp.im(tau)
    if im <= 0:
        raise ValueError("dedekind_eta: Im tau must be > 0")
    # |q| = e^{-2π Im τ};  need N·2π·Im τ / ln 10 > dps + 10
    n_terms = int((mp.dps + 10) * mp.log(10) / (2 * pi * im)) + 10
    n_terms = max(n_terms, 400)
    q = exp(2j * pi * tau)
    prod = mpc(1)
    for n in range(1, n_terms + 1):
        prod *= 1 - q**n
    return exp(2j * pi * tau / 24) * prod


def t5(tau):
    """The Γ₀(5) hauptmodul t₅(τ) = (η(τ)/η(5τ))⁶."""
    return (dedekind_eta(tau) / dedekind_eta(5 * tau)) ** 6


def gate(tau):
    """Evaluate both gates at a candidate τ. Returns a result dict with the
    hauptmodul residual, the Fricke-companion residual, and the ladder
    verdict. Both t₅ and τ ↦ j(5τ) are Γ₀(5)-invariant, so this tests
    Γ₀(5)-CLASS membership directly."""
    im = mp.im(tau)
    if im <= 0:
        return {
            "tau": mp.nstr(tau, 12),
            "im_tau": mp.nstr(im, 8),
            "verdict": "ill-defined",
            "reason": "Im tau <= 0: not a point of the upper half-plane",
        }
    t5_val = t5(tau)
    resid_t5 = abs(t5_val - T5_TARGET)
    j5_val = 1728 * kleinj(5 * tau)
    resid_j5 = abs(j5_val - J5_TARGET)
    if resid_t5 <= TOL_PASS_T5 and resid_j5 <= TOL_PASS_J5:
        verdict = "PASS"
    elif resid_t5 <= TOL_NEAR_T5:
        verdict = "NEAR"
    else:
        verdict = "FAIL"
    return {
        "tau": mp.nstr(tau, 12),
        "im_tau": mp.nstr(im, 8),
        "t5": mp.nstr(t5_val, 12),
        "abs_residual_t5_plus_10": mp.nstr(mpf(resid_t5), 6),
        "j_5tau": mp.nstr(j5_val, 12),
        "abs_residual_j5_plus_25_over_2": mp.nstr(mpf(resid_j5), 6),
        "verdict": verdict,
    }


def main():
    set_compute_dps()
    wb = WitnessBuilder("tau-dictionary-hauptmodul-validator", engine="mpmath")

    tau0 = mpc(mpf("-0.5"), mpf("0.186676"))  # BDH22 §2.2 (6 d.p. print)
    q0_mu = mpf(Q0_MUON)
    q0_p = mpf(Q0_PROTON)

    # ── validator self-checks ──────────────────────────────────────────────
    t5_ref = t5(tau0)
    assert abs(t5_ref - T5_TARGET) < TOL_PASS_T5, "control tau0 fails the gate"
    # Γ₀(5)-invariance: τ+1 and γτ = τ/(5τ+1) (γ = [[1,0],[5,1]] ∈ Γ₀(5))
    t5_shift = t5(tau0 + 1)
    t5_mobius = t5(tau0 / (5 * tau0 + 1))
    inv_dev = max(abs(t5_shift - t5_ref), abs(t5_mobius - t5_ref))
    assert inv_dev < mpf("1e-30"), f"Gamma0(5)-invariance broken: {inv_dev}"
    # Fricke image: t₅(−1/(5τ)) = 5³/t₅(τ) → −25/2 at τ₀
    t5_fricke = t5(-1 / (5 * tau0))
    fricke_dev = abs(t5_fricke - (125 / t5_ref))
    assert fricke_dev < mpf("1e-25"), f"Fricke check broken: {fricke_dev}"
    # sensitivity: a non-class point must FAIL loudly
    t5_i = t5(mpc(0, 1))
    assert abs(t5_i - T5_TARGET) > 1, "sensitivity check: t5(i) too close to -10"

    print("SELF-CHECKS:")
    print(f"  control      t5(tau0)        = {mp.nstr(t5_ref, 10)}  (|t5+10| = "
          f"{mp.nstr(mpf(abs(t5_ref - T5_TARGET)), 4)}; tau0-truncation-limited)")
    print(f"  invariance   max dev over {{tau0+1, tau0/(5tau0+1)}} = {mp.nstr(mpf(inv_dev), 4)}")
    print(f"  Fricke       |t5(-1/(5tau0)) - 125/t5(tau0)| = {mp.nstr(mpf(fricke_dev), 4)}"
          f"   (value {mp.nstr(t5_fricke, 8)} ~ -25/2)")
    print(f"  sensitivity  t5(i) = {mp.nstr(t5_i, 8)}  (far from -10)  ✓")

    # ── candidate dictionaries ─────────────────────────────────────────────
    def nome_exact(q0):     # C1 — the corpus's stated exact nome dictionary
        return mpc(0, abs(log(q0)) / (2 * pi))

    def nome_naive(q0):     # C1n — naive branch (lower half-plane at q0 > 1)
        return log(q0) / (2j * pi)

    def rate(q0):           # S1 strawman
        return mpc(0, log(q0))

    def hbar_q(q0):         # S2 strawman
        return mpc(0, 1 - 1 / q0)

    def rate_halfshift(q0):  # S3 strawman
        return mpc(mpf("-0.5"), log(q0))

    candidates = [
        ("REF-tau0", "tau0 = -0.5 + 0.186676i (BDH22; control)", None, tau0, "reference"),
        ("C1-nome-exact", "tau = i|ln q0|/(2pi)  [corpus: alpha_em_modular_family_probe.py]",
         nome_exact, None, "corpus-stated (caveated working choice)"),
        ("C1n-nome-naive", "tau = ln(q0)/(2pi i)  [naive branch, Im < 0]",
         nome_naive, None, "corpus-adjacent branch"),
        ("S1-rate", "tau = i ln q0  [STRAWMAN — demonstration only]",
         rate, None, "strawman"),
        ("S2-hbar", "tau = i (1 - 1/q0)  [STRAWMAN — demonstration only]",
         hbar_q, None, "strawman"),
        ("S3-rate-halfshift", "tau = -1/2 + i ln q0  [STRAWMAN — demonstration only]",
         rate_halfshift, None, "strawman"),
    ]

    # Both cross-candidate checks below used to be bare `assert`s here, and a
    # bare assert is the reason the witness carried `computed="stable",
    # expected="stable"`: on the only run where the check matters — one where a
    # verdict flips — the script dies before `wb.save()` and the witness does
    # not exist at all, so the constant had to stand in for it on every run
    # where it did not. Both outcomes are collected instead, published, and
    # enforced after the witness is written (see the end of `main`). A flip now
    # produces a red witness AND a non-zero exit, not silence.
    results = {}
    pin_verdict_sets: dict[str, list[str]] = {}   # q0-dependent candidates only
    print("\nCANDIDATE VERDICTS (both q0 pins where the map depends on q0):")
    for key, formula, fmap, fixed_tau, tier in candidates:
        if fmap is None:
            res = {"pin-independent": gate(fixed_tau)}
        else:
            res = {"muon-pin": gate(fmap(q0_mu)), "proton-pin": gate(fmap(q0_p))}
            pin_verdict_sets[key] = sorted({r["verdict"] for r in res.values()})
        results[key] = {"formula": formula, "tier": tier, "results": res}
        for pin, r in res.items():
            extra = (f"  t5 = {r['t5']}  |t5+10| = {r['abs_residual_t5_plus_10']}"
                     if "t5" in r else f"  ({r['reason']})")
            print(f"  {key:18s} [{pin:15s}] {r['verdict']:12s}{extra}")

    pin_stable = [k for k, v in pin_verdict_sets.items() if len(v) == 1]
    pin_flipped = {k: v for k, v in pin_verdict_sets.items() if len(v) != 1}

    # ── expected verdicts (pre-stated; asserted so exit 0 is meaningful) ───
    expected = {
        "REF-tau0": "PASS",
        "C1-nome-exact": "FAIL",
        "C1n-nome-naive": "ill-defined",
        "S1-rate": "FAIL",
        "S2-hbar": "FAIL",
        "S3-rate-halfshift": "FAIL",
    }
    verdict_matches = {}
    for key, exp_v in expected.items():
        got = sorted({r["verdict"] for r in results[key]["results"].values()})
        verdict_matches[key] = {"expected": exp_v, "got": got, "match": got == [exp_v]}
    verdict_mismatches = {k: v for k, v in verdict_matches.items() if not v["match"]}

    # ── witness ────────────────────────────────────────────────────────────
    wb.set_description(
        "t5(tau0) = -10 hauptmodul gate wired as a discrete validator on "
        "q0 -> tau dictionary candidates (uploaded-papers idea A2 consumer, "
        "A3-integer-trace-prune spirit). t5(tau) = (eta(tau)/eta(5tau))^6 and "
        "j(5tau) are Gamma0(5)-invariant (RR92 Thm 1 gauge), so evaluating "
        "them at a candidate tau tests Bring-class membership directly: "
        "PASS iff |t5+10| <= 1e-3 and |j(5tau)+25/2| <= 1.0. Control tau0 "
        "PASSes; the corpus's one stated dictionary (exact nome "
        "tau = i|ln q0|/(2pi)) FAILs — refuted-as-stated, scope-(a): the map, "
        "as stated, does not land on the Bring class. Three labelled strawmen "
        "(rate, hbar_q, half-shifted rate) demonstrate FAIL mechanics; the "
        "naive nome branch is ill-defined (Im tau < 0). Verdicts are "
        "q0-pin-independent (asserted across muon/proton pins). Gate composes "
        "with the polarization-blindness constraint (2026-07-19) as an "
        "independent discrete filter. Audit-only; nothing wired; no fit."
    )
    wb.set_audit_only("docs/audits/2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md")
    wb.add_data("gate", {
        "t5_target": "-10 (exact rational; QOU/Archimedean/BringHauptmodulGate.lean)",
        "fricke_target_j_5tau": "-25/2",
        "gauge": "Gamma0(5) residual gauge on Bring's modulus (RR92 Thm 1)",
        "q0_pin_independence": "gate constrains the tau side only; verdicts "
                               "asserted equal across muon/proton pins",
    })
    wb.add_data("tolerance_ladder", {
        "ill-defined": "Im tau <= 0 (not a modulus)",
        "PASS": "|t5+10| <= 1e-3 AND |j(5tau)+25/2| <= 1.0 "
                "(tau0-truncation scale of bring_hauptmodul_gate_probe.py)",
        "NEAR": "1e-3 < |t5+10| <= 1e-1 (needs higher-precision candidate tau)",
        "FAIL": "|t5+10| > 1e-1 — refuted-as-stated, scope-(a)",
    })
    wb.add_data("self_checks", {
        "control_t5_tau0": mp.nstr(t5_ref, 12),
        "gamma0_5_invariance_max_dev": mp.nstr(mpf(inv_dev), 6),
        "fricke_dev": mp.nstr(mpf(fricke_dev), 6),
        "sensitivity_t5_at_i": mp.nstr(t5_i, 12),
    })
    wb.add_data("candidates", results)
    wb.add_data("q0_pins", {"muon": Q0_MUON, "proton": Q0_PROTON})
    wb.add_caveat(
        "Strawmen S1-S3 are demonstration inputs for the validator mechanics, "
        "NOT dictionary proposals. A FAIL is scope-(a): the map, as stated, "
        "does not land on the Bring class; it excludes that stated map only, "
        "never an ingredient. tau0 itself is transcendental (Schneider); only "
        "its Gamma0(5)-invariants are exact."
    )
    wb.add_assertion(
        "control_tau0_passes",
        computed=abs(t5_ref - T5_TARGET),
        expected=0.0,
        tolerance=float(TOL_PASS_T5),
        source="|t5(tau0)+10| at BDH22 6-d.p. tau0 (truncation-limited ~2e-5).",
    )
    wb.add_assertion(
        "gamma0_5_invariance",
        computed=inv_dev,
        expected=0.0,
        tolerance=1e-30,
        source="max |t5(gamma tau0) - t5(tau0)| over gamma in {T, [[1,0],[5,1]]} "
               "subset Gamma0(5) — the validator tests class membership.",
    )
    wb.add_assertion(
        "fricke_involution",
        computed=fricke_dev,
        expected=0.0,
        tolerance=1e-25,
        source="|t5(-1/(5 tau0)) - 5^3/t5(tau0)|; image ~ -25/2 = j(5 tau0).",
    )
    c1_res = results["C1-nome-exact"]["results"]
    wb.add_assertion(
        "corpus_nome_dictionary_refuted_as_stated",
        computed="+".join(sorted({r["verdict"] for r in c1_res.values()})),
        expected="FAIL",
        tolerance=None,
        source="Exact nome dictionary tau = i|ln q0|/(2pi): |t5+10| = "
               f"{c1_res['muon-pin']['abs_residual_t5_plus_10']} (muon pin; "
               "proton pin identical) >> 1e-1 FAIL band — refuted-as-stated, "
               "scope-(a): the map, as stated, does not land on the Bring class.",
    )
    # Was `computed="stable", expected="stable"` — a literal describing a check
    # that had already aborted the run if it failed. Now it counts: how many
    # q0-dependent candidates returned a singleton verdict set, against how many
    # were evaluated at both pins. Zero q0-dependent candidates would read 0/0
    # and pass, so `n_pin_dependent_candidates` below records the denominator
    # the count came from.
    wb.add_data("pin_verdict_sets", pin_verdict_sets)
    wb.add_data("n_pin_dependent_candidates", len(pin_verdict_sets))
    wb.add_assertion(
        "verdicts_q0_pin_independent",
        computed=len(pin_stable),
        expected=len(pin_verdict_sets),
        tolerance=0,
        source=f"q0-dependent candidates whose verdict set is a singleton "
               f"across {{muon, proton}}: {len(pin_stable)} of "
               f"{len(pin_verdict_sets)} (gate constrains the tau side only; "
               f"pins differ by ~1.6e-8 relative). Flips: "
               f"{pin_flipped or 'none'}.",
    )
    # Same treatment for the pre-stated verdict table, which was the other bare
    # assert. It is on the abort path of the check above — a pin flip makes
    # `got` a two-element set and so would have tripped this one first, killing
    # the run before any of it reached the witness.
    wb.add_data("expected_verdict_check", verdict_matches)
    wb.add_assertion(
        "candidate_verdicts_match_prestated",
        computed=len(verdict_matches) - len(verdict_mismatches),
        expected=len(verdict_matches),
        tolerance=0,
        source="candidates whose observed verdict set equals the pre-stated "
               "single expected verdict (REF-tau0 PASS; C1n ill-defined; C1, "
               f"S1-S3 FAIL). Mismatches: {verdict_mismatches or 'none'}.",
    )
    # Explicit `comparison` stamp (bean qou-9ugp): this producer reads BOTH
    # pins deliberately, so no anchor list can classify it and it was going
    # out unstamped. Carries the values actually computed with.
    wb.save(q0_comparison(
        muon=Q0_MUON, proton=Q0_PROTON,
        reason='validates the tau-dictionary hauptmodul gate at BOTH pins; both pins are read on purpose and each is reported under its own key',
    ))

    # Enforce AFTER the witness exists, so a failure is recorded rather than
    # only raised. Exit status is unchanged from the old bare asserts.
    if pin_flipped:
        raise AssertionError(f"verdict flips across q0 pins: {pin_flipped}")
    if verdict_mismatches:
        raise AssertionError(f"verdicts differ from pre-stated: {verdict_mismatches}")
    print("\nwitness saved; all assertions passed.")


if __name__ == "__main__":
    main()
