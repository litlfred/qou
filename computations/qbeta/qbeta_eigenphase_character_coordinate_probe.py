#!/usr/bin/env python3
"""qbeta_eigenphase_character_coordinate_probe.py — the ladder's phase
constraint restated in the coordinate a Hecke character actually lives in,
and what that does to the "fine-tuning signature" and to the candidate basket.

BEAN `qou-pdix` (the S1 blocker: derive the Q_β ladder eigenphase α), sibling
of `qbeta_ladder_required_phase_probe.py` and
`qbeta_d_frame_terminus_probe.py`.

## The problem this addresses

Two results in the corpus point in opposite directions and are both about the
same object:

* `docs/audits/2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md` rejects
  the whole `α = (z−1)h/2` family because a viable `z` would need
  `z(q₀) = 0.4991044802` with `dz/dq = +400.2896759` — **slope/value 802** —
  and calls that "a fine-tuning signature, not a derivation."
* `QOU/QBeta/BraidImageEigenphaseAlgebraic.lean` excludes any braid-word
  character from supplying `2cos α`, by zero-counting, for **α surjective onto
  the non-positive reals** — the hypothesis `alphaC_surjective_nonpos` /
  `alphaD_neg_surjective_nonpos` supply for the `(z−1)h/2` family.

Both are stated in the `α`/`z` coordinate. But the object a braid word actually
produces is the **character** `P := tr M = 2cos α`, a Laurent polynomial in `q`;
`α = arccos(P/2)` is a derived quantity, bounded in `[0, π]`. So the natural
question is what these two constraints look like in `P`.

## What this probe measures

1. **The 802 is coordinate-dependent, with an exact closed form.** For any
   `α(q)` with `P = 2cos α` and `z = 1 + 2α/h`,

       (z′/z) / (P′/P)  =  −1 / (h·z·α) · 2   ≈  2/(h·z·|α|),

   which is large precisely **because `α` is small** — and `α` is small by
   construction, since the ladder's correction to `Q_A` is small. So the
   signature does not discriminate: every candidate with a small phase carries
   it. Measured here against the audit's own `z`, `dz/dq`.

2. **The exclusion of `(z−1)h/2` SURVIVES anyway**, and this probe does not
   rescue it. The other argument in `qbeta-ladder-required-phase.witness.json`
   — `dα_req/dq = +41.53` against `dα_C/dq = −0.455`, **opposite signs**, so
   the curves cross transversally rather than coincide — is invariant under
   this reparametrisation. Reported here so the two are not confused: what
   changes is *what the exclusion rests on*, not the exclusion.

3. **The two constraints in the character coordinate**, which is the usable
   output: a derived `P` must satisfy

       P(q₀)      = 1.997259194490263…   (± 1.14e-6, i.e. 5.7e-7 relative)
       |P′/P|(q₀) = 2.176…

4. **The candidate basket collapses under the second constraint.** The value
   basket `{2−h⁴, 2−h²/8, 2, 2−3h⁴, χ^{(2,1)}(𝓑₃), [2]_q}` — which
   `qbeta_d_frame_terminus_probe.py` correctly refuses to call an
   identification, since all six sit within 0.7 % on value — is spread from
   `0` to `0.102` in `|P′/P|` against a required `2.176`: every one is **21×
   to infinitely too flat**. The only form within 1.25× on slope is
   `tr M_{4₁}`, whose value is `−0.911` (out by 146 %).

   That is the point of the probe. The entropy bound (`σ_exp/t ≈ 10 %`, "a
   dozen small-height constants fit equally well") is a statement about
   matching **one** number. Matching value *and* log-slope is a second,
   independent constraint that the basket does not populate, and it is
   available at no experimental cost because it is a derivative of the same
   committed ladder.

## What this is NOT

Not a derivation of α, and not a proposal for `P`. Nothing here is fitted:
`P` and `|P′/P|` are read off the committed ladder by inversion, exactly as the
sibling probe reads off `α_req`, and the basket forms are the ones already
declared in the corpus. **No form is offered as a candidate** — the finding is
that the declared basket is empty against the two-constraint test, which is a
negative.

SCOPE. Scope-(a) throughout. Nothing here proves that no Laurent polynomial
meets the two constraints; it measures that no *declared* one does. The
coordinate-dependence in (1) is exact algebra and is scope-(b) for the claim
"slope/value is a coordinate-invariant fine-tuning measure", which it refutes.

PRECISION NOTE. `dα_req/dq` is a central difference at ±1e-4 relative in `q`,
inherited from the sibling probe, so `|P′/P| = 2.176` is good to ~4 figures.
That is far more than the 21× discrimination needs, and the *value* constraint
`P(q₀)` is exact to the compute dps. Stated because a slope quoted to 7 digits
would be a precision claim the central difference does not support.

BRANCH NOTE. `2cos` is even, so `±α` give the same `P` and opposite `P′`. Only
`|P′/P|` is branch-independent; the sign is not reported as a constraint.

Anchor: the experimental (proton) pin, per the 2026-08-07 owner directive.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
C2 = mp.mpf(-1)  # hardcoded in the committed extraction

# The audit's own figures, for the coordinate comparison in §1.
AUDIT_Z = mp.mpf("0.4991044802")
AUDIT_DZ_DQ = mp.mpf("400.2896759")


def q_a_over_me(q):
    return mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def alpha_required(q):
    """Invert the committed ladder for the phase it demands at `q` (c₃ = 0).

    Identical to the sibling probe's inversion; re-derived here rather than
    quoted so the two can disagree visibly if the ladder changes.
    """
    s = substrate_ladder_quantities(q, convention="C")
    u = s["u"]
    Q_A = ME * q_a_over_me(q)
    cos_req = QCOD / (Q_A * (1 + C2 * u ** 2))
    if not (-1 < cos_req < 1):
        raise ValueError(f"no real phase solves the ladder at q={q}")
    return u / 2 - mp.acos(cos_req), s


def d_alpha_required(q, rel_step="1e-4"):
    d = mp.mpf(rel_step)
    lo, _ = alpha_required(q * (1 - d))
    hi, _ = alpha_required(q * (1 + d))
    return (hi - lo) / (q * (1 + d) - q * (1 - d))


def h_of(q):
    return q - 1 / q


def main() -> int:
    q0 = q_at()
    a, s = alpha_required(q0)
    ap = d_alpha_required(q0)
    h = h_of(q0)
    u = s["u"]

    # ── §1. the same fact in two coordinates ───────────────────────────────
    # z-coordinate: z = 1 + 2α/h  (the audit's parametrisation)
    z = 1 + 2 * a / h
    hp = 1 + 1 / q0 ** 2                      # dh/dq
    zp = 2 * ap / h - 2 * a * hp / h ** 2
    z_logslope = zp / z

    # character coordinate: P = 2cos α = tr M
    P = 2 * mp.cos(a)
    Pp = -2 * mp.sin(a) * ap
    P_logslope = Pp / P

    inflation = z_logslope / P_logslope
    # Leading closed form. Dropping the 2*alpha*h'/h^2 term in dz/dq,
    #   z'/z  ~  (2 alpha'/h)/z      and      P'/P = -tan(alpha)*alpha',
    # so the ratio is -2/(h*z*tan alpha) ~ -2/(h*z*alpha) for small alpha.
    # Both signs matter: alpha < 0 at every substrate anchor, so the leading
    # minus is what makes the inflation positive.
    inflation_closed = -2 / (h * z * mp.tan(a))

    # the phase window (|c₃| ≤ 1) propagated to P:  dP = −2 sin(α) dα
    slope = mp.fabs(mp.sin(a - u / 2))
    alpha_window = u ** 3 / slope
    P_window = mp.fabs(2 * mp.sin(a)) * alpha_window

    print("=" * 78)
    print(" The ladder's phase constraint, in the coordinate a character lives in")
    print("=" * 78)
    print(f"""
  q₀        = {mp.nstr(q0, 20)}   (proton pin)
  h         = {mp.nstr(h, 16)}
  α_req     = {mp.nstr(a, 20)}
  dα_req/dq = {mp.nstr(ap, 10)}   (central difference, ±1e-4 rel)

  ── §1  the "fine-tuning signature" is coordinate-dependent ──

  in the audit's z = 1 + 2α/h:
      z          = {mp.nstr(z, 12)}      (audit records {mp.nstr(AUDIT_Z, 10)})
      dz/dq      = {mp.nstr(zp, 12)}      (audit records {mp.nstr(AUDIT_DZ_DQ, 10)})
      slope/value= {mp.nstr(z_logslope, 8)}    ← the "802, a fine-tuning signature"

  in the character coordinate P = 2cos α = tr M:
      P          = {mp.nstr(P, 18)}
      dP/dq      = {mp.nstr(Pp, 10)}
      |P′/P|     = {mp.nstr(mp.fabs(P_logslope), 8)}    ← unremarkable

  inflation (z′/z)/(P′/P)   = {mp.nstr(inflation, 8)}
  closed form −2/(h·z·tan α) = {mp.nstr(inflation_closed, 8)}
  ratio                      = {mp.nstr(inflation / inflation_closed, 8)}
                               (the {mp.nstr(mp.fabs(inflation / inflation_closed - 1) * 100, 3)} % residual is the
                                dropped 2αh′/h² term in dz/dq)

  The factor is large BECAUSE α is small, and α is small by construction —
  the ladder's correction to Q_A is a fraction of a percent. So slope/value
  in the z coordinate cannot discriminate between candidate phases: every
  candidate with a small phase carries the same inflation.

  ── §2  what this does NOT rescue ──

  The (z−1)h/2 family stays excluded, on the other argument in
  qbeta-ladder-required-phase.witness.json: dα_req/dq = +41.53 against
  dα_C/dq = −0.455 — OPPOSITE SIGNS, so the curves cross transversally
  rather than coincide. A derivative sign disagreement is invariant under
  this reparametrisation. What changes is what the exclusion rests on.

  ── §3  the two constraints, in the usable coordinate ──

      P(q₀)      = {mp.nstr(P, 18)}   ± {mp.nstr(P_window, 4)}
                                             (rel {mp.nstr(P_window / P, 4)})
      |P′/P|(q₀) = {mp.nstr(mp.fabs(P_logslope), 8)}
""")

    # ── §4. the declared basket, against BOTH constraints ──────────────────
    def hh(x):
        return x - 1 / x

    basket = [
        ("2 - h^4", lambda x: 2 - hh(x) ** 4),
        ("2 - h^2/8", lambda x: 2 - hh(x) ** 2 / 8),
        ("2 (identity word)", lambda x: 2 + 0 * x),
        ("2 - 3h^4", lambda x: 2 - 3 * hh(x) ** 4),
        ("chi^(2,1)(B_3) = 2-3h^4-h^6",
         lambda x: 2 - 3 * hh(x) ** 4 - hh(x) ** 6),
        ("[2]_q = q + 1/q", lambda x: x + 1 / x),
        ("tr M_4_1 = q^4-2q^2+1-2q^-2+q^-4",
         lambda x: x ** 4 - 2 * x ** 2 + 1 - 2 * x ** -2 + x ** -4),
    ]

    print("=" * 78)
    print(" §4  the declared value basket, tested on BOTH constraints")
    print("=" * 78)
    print(f"\n  {'form':34s} {'value miss %':>13} {'|P′/P|':>10} "
          f"{'slope ratio':>12}")
    print("  " + "-" * 74)
    rows = []
    min_flatness = None
    for name, f in basket:
        v = f(q0)
        d = mp.diff(f, q0)
        value_miss_pct = mp.fabs(v - P) / P * 100
        ls = mp.fabs(d / v) if v != 0 else mp.inf
        ratio = ls / mp.fabs(P_logslope)
        rows.append({
            "form": name,
            "value": fmt(v),
            "value_miss_pct": fmt(value_miss_pct),
            "abs_log_slope": fmt(ls),
            "slope_ratio_to_required": fmt(ratio),
        })
        if min_flatness is None or ratio > min_flatness:
            # track the LEAST flat (closest to the requirement from below)
            min_flatness = ratio
        print(f"  {name:34s} {mp.nstr(value_miss_pct, 4):>13} "
              f"{mp.nstr(ls, 5):>10} {mp.nstr(ratio, 4):>12}")

    # the six value-basket forms, excluding tr M_4_1 which is a value outlier
    value_basket = [r for r in rows if "tr M_4_1" not in r["form"]]
    worst = max(mp.mpf(r["slope_ratio_to_required"]) for r in value_basket)

    print(f"""
  Value alone spreads the six-form basket over 0.04 %–0.7 % — a factor 17,
  which is why the terminus probe calls it a basket and not an isolation.
  Log-slope spreads the SAME six over 0 to {mp.nstr(worst * mp.fabs(P_logslope), 4)} against a required
  {mp.nstr(mp.fabs(P_logslope), 6)}: the least flat is {mp.nstr(1 / worst, 4)}x too flat, the flattest is a
  constant with slope exactly 0.

  So the entropy objection — "a dozen small-height constants fit equally
  well" — is a statement about matching ONE number. The declared basket is
  EMPTY against the two-constraint test, and the second constraint costs no
  experimental precision: it is a derivative of the same committed ladder.
""")

    wb = WitnessBuilder("qbeta-eigenphase-character-coordinate", engine="python")
    wb.add_data("pin", {
        "q0": fmt(q0), "h": fmt(h), "u": fmt(u),
        "alpha_required": fmt(a),
        "d_alpha_required_dq": fmt(ap),
        "d_alpha_method": "central difference, +/-1e-4 relative in q",
    })
    wb.add_data("z_coordinate", {
        "z": fmt(z), "dz_dq": fmt(zp), "log_slope": fmt(z_logslope),
        "audit_z": fmt(AUDIT_Z), "audit_dz_dq": fmt(AUDIT_DZ_DQ),
    })
    wb.add_data("character_coordinate", {
        "P": fmt(P), "dP_dq": fmt(Pp),
        "abs_log_slope": fmt(mp.fabs(P_logslope)),
        "P_window_abs": fmt(P_window),
        "P_window_rel": fmt(P_window / P),
    })
    wb.add_data("coordinate_inflation", {
        "measured": fmt(inflation),
        "closed_form_2_over_h_z_alpha": fmt(inflation_closed),
    })
    wb.add_data("declared_basket", rows)

    wb.add_assertion(
        name="z_log_slope_reproduces_the_audit_802",
        computed=fmt(z_logslope / (AUDIT_DZ_DQ / AUDIT_Z)),
        expected="1", tolerance=mp.mpf("1e-2"),
        source=(
            "Ratio, not a difference: the witness tolerance is ABSOLUTE, so a "
            "quantity of order 800 must be normalised before it can carry a "
            "1 % tolerance. Re-derived from the ladder inversion rather than "
            f"quoted: z = {mp.nstr(z, 10)}, dz/dq = {mp.nstr(zp, 10)}, "
            f"slope/value = {mp.nstr(z_logslope, 8)} against the audit's "
            f"{mp.nstr(AUDIT_DZ_DQ / AUDIT_Z, 8)} "
            "(docs/audits/2026-08-30-cds1-two-row-cap-admissible-set-"
            "exhausted.md), agreeing to "
            f"{mp.nstr(mp.fabs(z_logslope / (AUDIT_DZ_DQ / AUDIT_Z) - 1) * 100, 3)} % — the two "
            "central differences use different step sizes. Agreement confirms "
            "this probe is measuring the same object the 'fine-tuning "
            "signature' was measured on."
        ),
    )
    wb.add_assertion(
        name="fine_tuning_signature_is_coordinate_dependent",
        computed=fmt(inflation / inflation_closed),
        expected="1", tolerance=mp.mpf("2e-2"),
        source=(
            "(z'/z)/(P'/P) equals the leading closed form -2/(h*z*tan alpha) "
            f"to {mp.nstr(mp.fabs(inflation / inflation_closed - 1) * 100, 3)} % — measured "
            f"{mp.nstr(inflation, 8)}, closed form "
            f"{mp.nstr(inflation_closed, 8)}. The residual is exactly the "
            "dropped 2*alpha*h'/h^2 term in dz/dq; asserted as a ratio "
            "because the witness tolerance is absolute. Note the sign: alpha "
            "< 0 at every substrate anchor, so the leading minus is what "
            "makes the inflation positive. The factor is large because alpha "
            "is small, which is forced by the ladder's correction being "
            "small, so slope/value in the z coordinate is not a "
            "coordinate-invariant measure of fine-tuning and cannot "
            "discriminate between candidate phases. Scope-(b) for that claim "
            "(it is exact algebra). Does NOT rescue the (z-1)h/2 family, "
            "which stays excluded by the opposite-sign slopes recorded in "
            "qbeta-ladder-required-phase.witness.json."
        ),
    )
    wb.add_assertion(
        name="declared_basket_is_empty_against_the_slope_constraint",
        computed=str(int(worst < mp.mpf("0.05"))),
        expected="1", tolerance=0,
        source=(
            "Every form in the corpus's declared value basket "
            "{2-h^4, 2-h^2/8, 2, 2-3h^4, chi^(2,1)(B_3), [2]_q} has "
            f"|P'/P| <= {mp.nstr(worst * mp.fabs(P_logslope), 4)} against a required "
            f"{mp.nstr(mp.fabs(P_logslope), 6)}, i.e. at least "
            f"{mp.nstr(1 / worst, 4)}x too flat; the constant has slope "
            "exactly 0. Value alone separates the six by only a factor 17 "
            "(0.04%-0.7%), which is why qbeta_d_frame_terminus_probe.py "
            "calls it a basket rather than an identification. The log-slope "
            "is a second constraint, independent and free (a derivative of "
            "the same committed ladder), and it empties the basket. "
            "Scope-(a): measures that no DECLARED form passes; does not "
            "prove no Laurent polynomial does."
        ),
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
