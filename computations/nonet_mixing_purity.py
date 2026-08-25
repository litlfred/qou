#!/usr/bin/env python3
"""Singlet-octet mixing purity of the pseudoscalar and vector nonets.

Scope (honest): this is a COMPARATOR computation over PDG central values,
not a framework derivation. It quantifies, convention-free, how far each
meson nonet sits from ideal mixing, in order to score whether the mixing
angle is a *content-bearing* derivation target.

Why it matters. Two eightfold-way relations are already proved to be
identities of the first-order octet-breaking ansatz, hence content-free
as targets:

  * Gell-Mann-Okubo          (QOU/Eightfold/GellMannOkuboIdentity.lean)
  * decuplet equal spacing   (QOU/Eightfold/DecupletEqualSpacing.lean)

The nonet mixing angle is the opposite case: the ansatz constrains it
NOT AT ALL (QOU/Eightfold/NonetMixingUnconstrained.lean, sorry-free --
with the GMO-fixed octet entry held fixed, any physical spectrum is
realisable by choosing the singlet entry and the mixing). So the
measured mixing carries information the symmetry does not supply. This
script measures how much, and shows that two nonets with IDENTICAL
SU(3) content sit at nearly opposite extremes.

Method (convention-free, deliberately). Mixing angles are quoted in the
literature under several incompatible sign/ordering conventions, which
is a recurring source of confusion (theta_V ~ 39 deg vs 50.8 deg is the
same physics read two ways). This script therefore reports the physical
quark content -- the ss-bar probability of the heavy state -- which is
convention-independent. Ideal mixing is exactly 100%.

The 2x2 mass matrix in the (octet, singlet) basis is reconstructed from
three inputs: the GMO-required octet member m_8^2 = (4 m_K*^2 - m_rho^2)/3,
and the two physical eigenvalues (trace fixes the singlet entry, det
fixes the off-diagonal SQUARE). The determinant leaves the off-diagonal
SIGN free; both branches are computed and the physical one -- the branch
maximising the heavy state's ss-bar content -- is reported, with the
other branch also recorded so the choice is auditable rather than hidden.

Precision: mpmath.mpf carried from the source literals per the NO-FLOAT64
discipline; no float64 anywhere, no fitted parameter. PDG values are
comparators, never inputs to a framework quantity.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401  (canonical sys.path bridge)
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import _precision  # noqa: E402  (sets compute/serialisation dps; supplies fmt)

# ------------------------------------------------------------ PDG comparators
# Central values, GeV. External data: comparators only.
PDG = {
    "pi": "0.13957039",
    "K": "0.493677",
    "eta": "0.547862",
    "etaprime": "0.95778",
    "rho": "0.77526",
    "Kstar": "0.89555",
    "omega": "0.78266",
    "phi": "1.019461",
}


def _m(key: str) -> mp.mpf:
    """PDG mass as an mpf carried from the source literal (never float64)."""
    return mp.mpf(PDG[key])


def _sym_eig_2x2(d1: mp.mpf, d2: mp.mpf, off: mp.mpf):
    """Eigenvalues and orthonormal eigenvectors of [[d1, off], [off, d2]].

    Closed form rather than a library call, so the arithmetic stays in
    mpmath at full working precision.  Returns ((lo, v_lo), (hi, v_hi)).
    """
    tr, det = d1 + d2, d1 * d2 - off**2
    disc = mp.sqrt(tr**2 - 4 * det)
    lo, hi = (tr - disc) / 2, (tr + disc) / 2

    def vec(lam: mp.mpf):
        # (d1 - lam) a + off b = 0  ->  (a, b) ∝ (off, lam - d1)
        a, b = off, lam - d1
        if a == 0 and b == 0:          # degenerate: matrix is already diagonal
            return (mp.mpf(1), mp.mpf(0))
        nrm = mp.sqrt(a**2 + b**2)
        return (a / nrm, b / nrm)

    return (lo, vec(lo)), (hi, vec(hi))


# |nn-bar> and |ss-bar> expressed in the (octet, singlet) basis.
def _nn_vec():
    return (1 / mp.sqrt(3), mp.sqrt(mp.mpf(2) / 3))


def _ss_vec():
    return (-mp.sqrt(mp.mpf(2) / 3), 1 / mp.sqrt(3))


def analyse(mK: mp.mpf, mpi: mp.mpf, m_lo: mp.mpf, m_hi: mp.mpf) -> dict:
    """Reconstruct the mass matrix and return the quark content."""
    m8sq = (4 * mK**2 - mpi**2) / 3            # GMO-required octet member
    m1sq = m_lo**2 + m_hi**2 - m8sq            # trace
    offsq = m8sq * m1sq - m_lo**2 * m_hi**2    # determinant

    if offsq < 0:
        return {"real_off_diagonal": False}

    off = mp.sqrt(offsq)
    nn, ss = _nn_vec(), _ss_vec()
    branches = {}
    for sgn in (1, -1):
        (_, v_lo), (_, v_hi) = _sym_eig_2x2(m8sq, m1sq, sgn * off)
        p_ss_hi = (v_hi[0] * ss[0] + v_hi[1] * ss[1]) ** 2
        p_nn_lo = (v_lo[0] * nn[0] + v_lo[1] * nn[1]) ** 2
        branches[sgn] = (p_ss_hi, p_nn_lo)

    sgn = max(branches, key=lambda s: branches[s][0])   # physical branch
    p_ss_hi, p_nn_lo = branches[sgn]
    other = branches[-sgn][0]

    return {
        "real_off_diagonal": True,
        "m8_GeV": mp.sqrt(m8sq),
        "m1_GeV": mp.sqrt(m1sq) if m1sq >= 0 else None,
        "off_diagonal_sign_chosen": sgn,
        "heavy_ssbar_probability": p_ss_hi,
        "light_nnbar_probability": p_nn_lo,
        "departure_from_ideal_pp": 100 * (1 - p_ss_hi),
        "rejected_branch_ssbar_probability": other,
    }


def gmo_deviation(mK: mp.mpf, m8: mp.mpf, mpi: mp.mpf) -> mp.mpf:
    """Relative deviation of 4 m_K^2 from 3 m_8^2 + m_pi^2, as a fraction."""
    return (4 * mK**2) / (3 * m8**2 + mpi**2) - 1


def main() -> None:
    # MUST come before any mpf arithmetic. Importing _precision does NOT set
    # mp.dps — it stays at mpmath's default 15, i.e. float64-equivalent, and
    # fmt() would then pad a 53-bit result out to OUTPUT_DPS digits and read
    # as measured. The float64-padding ratchet catches exactly that.
    _precision.set_compute_dps()

    wb = WitnessBuilder("nonet-mixing-purity")
    wb.set_content_block("rem:vector-meson-nonet")
    wb.set_description(
            "COMPARATOR (not a derivation): convention-free singlet-octet "
            "mixing purity of the pseudoscalar and vector meson nonets, from "
            "PDG central values. Scores whether the nonet mixing angle is a "
            "content-bearing derivation target. It is: the first-order octet "
            "ansatz constrains it not at all (NonetMixingUnconstrained.lean, "
            "sorry-free), unlike GMO and decuplet equal spacing, which are "
            "identities of the ansatz and hence content-free as targets. Two "
            "nonets with IDENTICAL SU(3) content sit at nearly opposite "
            "extremes: the vector nonet is ideally mixed to ~0.5 percentage "
            "points, the pseudoscalar nonet is ~50 pp away. No SU(3)-symmetric "
            "statement distinguishes them. Nothing fitted; nothing wired; PDG "
            "values are comparators only. The framework cannot currently "
            "attempt this -- the singlet is unavailable at dim V = 2 "
            "(RowCapObstruction.lean) -- so this scores the TARGET, not "
            "prospects."
    )

    ps = analyse(_m("K"), _m("pi"), _m("eta"), _m("etaprime"))
    vc = analyse(_m("Kstar"), _m("rho"), _m("omega"), _m("phi"))

    wb.add_data("pseudoscalar_nonet", {
        "states": "eta / eta-prime", **{k: str(v) for k, v in ps.items()}})
    wb.add_data("vector_nonet", {
        "states": "omega / phi", **{k: str(v) for k, v in vc.items()}})

    wb.add_data("gmo_deviation_on_physical_states", {
        "pseudoscalar_eta": str(gmo_deviation(_m("K"), _m("eta"), _m("pi"))),
        "vector_omega": str(gmo_deviation(_m("Kstar"), _m("omega"), _m("rho"))),
        "vector_phi": str(gmo_deviation(_m("Kstar"), _m("phi"), _m("rho"))),
        "note": (
            "GMO applied to the PHYSICAL states. It nearly works for the "
            "pseudoscalar eta (~6%) because that nonet is barely mixed, and "
            "fails badly for the physical omega (~32%) because that nonet is "
            "ideally mixed, so the physical omega is not the octet member. "
            "The failure is a mixing effect, not a failure of SU(3)."),
    })

    wb.add_data("convention_note", (
        "Reported as quark content, not as a mixing angle. Angle conventions "
        "differ across the literature (theta_V ~ 39 deg and ~50.8 deg are the "
        "same physics under complementary definitions); the ss-bar "
        "probability of the heavy state is convention-independent, with ideal "
        "mixing exactly 1. The determinant fixes only the SQUARE of the "
        "off-diagonal, so both sign branches are computed and the rejected "
        "one is recorded rather than silently dropped."))

    wb.add_data("honest_scope", (
        "Comparator only. This does NOT claim the framework derives the "
        "mixing, and it is not evidence for the framework. It establishes "
        "that a derivation WOULD be evidence -- which is exactly what the GMO "
        "and equal-spacing null results establish is NOT true of those two."))

    # Assertions carry mpf through _precision.fmt -- never float(), which
    # would inject raw float64 into the witness (NO-FLOAT64 ratchet).
    f = _precision.fmt
    wb.add_assertion(
        name="vector_nonet_is_near_ideal",
        computed=f(vc["heavy_ssbar_probability"]),
        expected="1", tolerance="0.01",
        unit="probability",
        source=("phi is ss-bar to within ~0.5 percentage points: the vector "
                "nonet is ideally mixed."))
    wb.add_assertion(
        name="pseudoscalar_nonet_is_far_from_ideal",
        computed=f(ps["heavy_ssbar_probability"]),
        expected="0.5", tolerance="0.05",
        unit="probability",
        source=("eta-prime is only ~50% ss-bar: the pseudoscalar nonet sits "
                "about as far from ideal mixing as possible."))
    wb.add_assertion(
        name="two_nonets_disagree_on_mixing",
        computed=f(vc["heavy_ssbar_probability"]
                   - ps["heavy_ssbar_probability"]),
        expected="0.49", tolerance="0.05",
        unit="probability",
        source=("The two nonets have identical SU(3) content yet differ by "
                "~0.49 in heavy-state ss-bar purity. No SU(3)-symmetric "
                "statement can distinguish them, so the mixing is genuinely "
                "extra data -- the content-bearing target."))

    out = wb.save()

    print("pseudoscalar nonet (eta/eta'):")
    print(f"  eta' ss-bar probability      = {ps['heavy_ssbar_probability']}")
    print(f"  departure from ideal (pp)    = {ps['departure_from_ideal_pp']}")
    print("vector nonet (omega/phi):")
    print(f"  phi  ss-bar probability      = {vc['heavy_ssbar_probability']}")
    print(f"  departure from ideal (pp)    = {vc['departure_from_ideal_pp']}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
