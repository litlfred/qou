#!/usr/bin/env python3
"""qbeta_c3_barodd_hs_matrix_resolvent_probe.py

Does a MATRIX Gram-resolvent pairing supply the bar-odd flip that the SCALAR
Frobenius closure cannot? — the Hilbert–Schmidt matrix-O probe (PR #4064
synthesis, Frobenius-pairing lens).

Background. The scalar Frobenius closure `Σ_λ y_λ χ_λ Δ_λ` is smooth×smooth =
smooth and is proven-dead for the bar-odd carrier
`S(q) = c3_target_at(q, Q_β, m_e) + Vol(4₁)`
(`S(muon)=+0.00968`, `S(proton)=−0.03946`, opposite sign — bar-ODD). The
Frobenius-pairing lens proposed feeding the **matrix** interface operator O
(the figure-eight object `Vol(4₁)` references) through a matrix resolvent
`⟨O,(G−μ)⁻¹O⟩_HS = tr(Oᵀ(G−μ)⁻¹O)`, where `G` is the canonical H₃(q)
Markov/Hecke Gram matrix on the NF basis `[γ,σ₀,σ₁,L₊,L₋,e⁻]` and `μ` is a
geometric resolvent pole. Hypothesis: the matrix resolvent supplies a
geometric pole `μ(q)` producing the sign flip the scalar version lacks.

NO FIT: every `μ` is a geometric/canonical value (0 = Frobenius dual; 1;
`z = 1/(√q+1/√q)`; a Gram eigenvalue). Nothing is tuned to Q_β.

FINDINGS (scope-(a); no fit; nothing wired; no tier change):

  1. **No sign flip at ANY geometric μ.** `HS(proton)` and `HS(muon)` share
     sign at every μ tested — including the near-pole `μ = λ_min(G)−ε`
     (magnitude ~10⁶, same sign both anchors). `HS(proton)/HS(muon) ≈ +1.0000`
     vs the target ratio `−4.08`. Structural mismatch.

  2. **The pairing is BAR-EVEN** — `|HS(q)−HS(1/q)| ≪ |HS(q)+HS(1/q)|` at
     μ ∈ {0,1}. `S` is bar-ODD (Lean-proved `fig8Trace_im_odd`), so a **real**
     bar-even resolvent built from Markov-trace (bar-even) data structurally
     **cannot** carry `S`'s chirality — independent of magnitude.

  3. **Gram eigenvalues do not cross** between the anchors — all six shift by
     ~10⁻⁸ in the SAME direction. A fixed μ between `λ(proton)` and `λ(muon)`
     would need tuning to ~10⁻⁸ (a fit), and even then the pairing **diverges**
     (|HS|→∞ at the pole) rather than passing through a **zero** — the wrong
     KIND of sign change (`S` flips through a zero at q*, staying O(0.01); a
     resolvent flips through a pole, diverging).

CONCLUSION (scope-(a) — NOT scope-(b) for the general resolvent). This
construction — a **real** matrix Gram-resolvent pairing from Markov-trace data,
alone — does not reproduce the bar-odd `S`; it supplies a real bar-even
magnitude but not the sign flip. This reconfirms, from an independent MATRIX
direction, the corpus's bar-parity obstruction (`fig8Trace_im_odd`;
`CuspShapeBarParity`; the NZ-deformation argument
`qbeta_c3_barodd_nz_deformation_probe.py` finding 4). Because that obstruction
is a **proved invariant** (bar-parity), the correct framing is: a **real**
resolvent is excluded by bar-parity — a **complex / fibre-level** pole is NOT.
The surviving open object is the fibre-level complex pole→cusp phase `φ(q₀)`
(q-Pochhammer denominator pole `x=q^{−k}` × cusp phase `ω=e^{iπ/3}`) already set
up in `qbeta_c3_barodd_pole_cusp_phase_probe.py` — the same fibre continuation
(root-of-unity → real q₀) that is the c₃⟺q₀ crux `bwS0_eq_hecke`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))

# NF basis of H_3(q): words in generators 0 (σ₀), 1 (σ₁).
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
FIG8 = (0, -2, 0, -2)  # (σ₀ σ₁⁻¹)² — figure-eight 4₁ on 3 strands


def make_engine(q):
    HA = q - 1 / q
    sq = mp.sqrt(q)
    z = 1 / (sq + 1 / sq)
    TR_M = [mp.mpf(1), z, z, z * z, z * z, z * z * z]

    def hecke_mul(t1, t2):
        r = {}
        for w1, c1 in t1.items():
            for w2, c2 in t2.items():
                w = w1 + w2
                r[w] = r.get(w, mp.mpf(0)) + c1 * c2
        return r

    def reduce_nf(terms):
        changed = True
        while changed:
            changed = False
            nt = {}
            for word, coeff in terms.items():
                if abs(coeff) < mp.mpf(10) ** -40:
                    continue
                done = False
                for pos in range(len(word) - 1):
                    if word[pos] == word[pos + 1]:  # σ_i² = HA·σ_i + 1
                        pre, suf = word[:pos], word[pos + 2:]
                        w1 = pre + (word[pos],) + suf
                        w2 = pre + suf
                        nt[w1] = nt.get(w1, mp.mpf(0)) + coeff * HA
                        nt[w2] = nt.get(w2, mp.mpf(0)) + coeff
                        done = changed = True
                        break
                if done:
                    continue
                for pos in range(len(word) - 2):  # braid sorting
                    a, b, c = word[pos], word[pos + 1], word[pos + 2]
                    if a == c and abs(a - b) == 1:
                        trip = (b, a, b)
                        if trip < (a, b, a):
                            nw = word[:pos] + trip + word[pos + 3:]
                            nt[nw] = nt.get(nw, mp.mpf(0)) + coeff
                            done = changed = True
                            break
                if not done:
                    nt[word] = nt.get(word, mp.mpf(0)) + coeff
            terms = {w: c for w, c in nt.items() if abs(c) > mp.mpf(10) ** -40}
        return terms

    def expand_inverse_word(word):
        """σ_i⁻¹ = σ_i − HA; negative index g encodes σ_{−g−1}⁻¹."""
        terms = {(): mp.mpf(1)}
        for g in word:
            nt = {}
            if g >= 0:
                for w, c in terms.items():
                    nw = w + (g,)
                    nt[nw] = nt.get(nw, mp.mpf(0)) + c
            else:
                i = -g - 1
                for w, c in terms.items():
                    nw = w + (i,)
                    nt[nw] = nt.get(nw, mp.mpf(0)) + c
                    nt[w] = nt.get(w, mp.mpf(0)) - c * HA
            terms = nt
        return terms

    def to_vec(terms):
        return [terms.get(b, mp.mpf(0)) for b in NF_BASIS]

    return HA, z, TR_M, hecke_mul, reduce_nf, expand_inverse_word, to_vec


def gram(q):
    _HA, _z, TR_M, hmul, rnf, _ei, tovec = make_engine(q)
    G = mp.matrix(6, 6)
    for i in range(6):
        for j in range(6):
            prod = hmul({NF_BASIS[i]: mp.mpf(1)}, {NF_BASIS[j]: mp.mpf(1)})
            vec = tovec(rnf(prod))
            G[i, j] = sum(c * t for c, t in zip(vec, TR_M))
    return G


def left_reg_operator(q, raw_word):
    """Left-regular rep matrix O of a signed braid word on the NF basis."""
    _HA, _z, _TR, hmul, rnf, expinv, tovec = make_engine(q)
    word_terms = rnf(expinv(raw_word))
    O = mp.matrix(6, 6)
    for j in range(6):
        prod = hmul(word_terms, {NF_BASIS[j]: mp.mpf(1)})
        vec = tovec(rnf(prod))
        for i in range(6):
            O[i, j] = vec[i]
    return O


def hs_pairing(O, G, mu):
    R = (G - mu * mp.eye(6)) ** -1
    OT_R_O = O.T * R * O
    return sum(OT_R_O[i, i] for i in range(6))


def eigs(G):
    E, _ = mp.eig(G)
    return sorted([mp.re(e) for e in E])


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 74)
    print(" c₃ bar-odd S: matrix Gram-resolvent ⟨O,(G−μ)⁻¹O⟩  (Hilbert–Schmidt)")
    print("=" * 74)
    qp, qm = q_at(50), q_muon_at(50)
    print(f"\n TARGET  S(proton)={mp.nstr(S(qp),8)}  S(muon)={mp.nstr(S(qm),8)}  (bar-ODD flip)")

    mus = [("mu=0", lambda sub, ev: mp.mpf(0)),
           ("mu=1", lambda sub, ev: mp.mpf(1)),
           ("mu=z", lambda sub, ev: sub["z"]),
           ("mu=lambda_min-eps", lambda sub, ev: ev[0] - mp.mpf("1e-6"))]

    def at(q):
        sub = substrate_ladder_quantities(q)
        G = gram(q)
        ev = eigs(G)
        O = left_reg_operator(q, FIG8)
        hs = {name: hs_pairing(O, G, f(sub, ev)) for name, f in mus}
        return {"G": G, "ev": ev, "hs": hs}

    rp, rm = at(qp), at(qm)

    # ---- FINDING 1: no sign flip ----
    print("\n[1] sign flip between anchors?")
    flips = []
    ratios = []
    for name, _f in mus:
        vp, vm = rp["hs"][name], rm["hs"][name]
        flip = mp.sign(vp) != mp.sign(vm)
        flips.append(flip)
        if vm != 0:
            ratios.append(vp / vm)
        print(f"    {name:20s} proton={mp.nstr(vp,8):>16s} muon={mp.nstr(vm,8):>16s}  flip={flip}")
    any_flip = any(flips)
    ratio0 = rp["hs"]["mu=0"] / rm["hs"]["mu=0"]
    print(f"    HS ratio (mu=0) = {mp.nstr(ratio0,8)}  vs target ratio S(p)/S(m) = {mp.nstr(S(qp)/S(qm),6)}")

    # ---- FINDING 2: bar-parity ----
    print("\n[2] bar-parity of the pairing (q vs 1/q):")
    bar_even_all = True
    for mu in [mp.mpf(0), mp.mpf(1)]:
        Gp, Gi = gram(qp), gram(1 / qp)
        Op, Oi = left_reg_operator(qp, FIG8), left_reg_operator(1 / qp, FIG8)
        hp, hi = hs_pairing(Op, Gp, mu), hs_pairing(Oi, Gi, mu)
        even, odd = abs(hp - hi), abs(hp + hi)
        kind = "BAR-EVEN" if even < odd else "BAR-ODD"
        bar_even_all = bar_even_all and (even < odd)
        print(f"    mu={mp.nstr(mu,3)}: |HS(q)-HS(1/q)|={mp.nstr(even,4)}  "
              f"|HS(q)+HS(1/q)|={mp.nstr(odd,4)}  => {kind}")

    # ---- FINDING 3: eigenvalue non-crossing ----
    # No level crossing iff the between-anchor shift is tiny vs the eigenvalue
    # gaps: then no eigenvalue crosses zero or another, so no geometric pole
    # enters/leaves the anchor window without tuning mu to the shift scale (a fit).
    print("\n[3] Gram eigenvalues cross between anchors?")
    max_shift = max(abs(rm["ev"][k] - rp["ev"][k]) for k in range(6))
    min_gap = min(min(abs(rp["ev"][k + 1] - rp["ev"][k]) for k in range(5)),
                  min(abs(rp["ev"][k]) for k in range(6)))  # gaps + distance to 0
    no_crossing = max_shift < min_gap / 10
    print(f"    max |Δλ| between anchors = {mp.nstr(max_shift,4)} (~1e-8);  "
          f"min gap/|λ-to-0| = {mp.nstr(min_gap,4)}  => no crossing = {no_crossing}")

    verdict = (not any_flip) and bar_even_all
    print("\n" + "=" * 74)
    print(f" VERDICT: real matrix Gram-resolvent is BAR-EVEN, no flip — scope-(a) "
          f"negative  [{'PASS' if verdict else 'CHECK'}]")
    print("=" * 74)

    wb = WitnessBuilder("qbeta-c3-barodd-hs-matrix-resolvent", engine="mpmath")
    wb.set_description(
        "Hilbert–Schmidt matrix-O probe (PR #4064 Frobenius-pairing lens): does the "
        "MATRIX Gram-resolvent ⟨O,(G−μ)⁻¹O⟩=tr(Oᵀ(G−μ)⁻¹O) supply the bar-odd flip the "
        "SCALAR Frobenius closure Σy_λχ_λΔ_λ cannot? O = fig-8 (σ₀σ₁⁻¹)² left-reg rep on "
        "the H₃(q) NF basis; G = canonical Markov Gram; μ geometric (0/1/z/λ_min−ε), no "
        "fit. FINDINGS (scope-(a)): (1) NO sign flip at any μ — HS(p)/HS(m)≈+1.0000 vs "
        "target −4.08, incl. near-pole μ (mag ~1e6, same sign). (2) The pairing is "
        "BAR-EVEN (|HS(q)−HS(1/q)|≪|HS(q)+HS(1/q)|); S is bar-ODD (Lean fig8Trace_im_odd), "
        "so a real bar-even resolvent from Markov (bar-even) data cannot carry S's "
        "chirality. (3) Gram eigenvalues shift ~1e-8 same-direction, no crossing; a fixed μ "
        "between anchors would be a ~1e-8 fit AND diverge (pole) not zero-cross. A REAL "
        "matrix resolvent alone does not reproduce bar-odd S — reconfirms the proved "
        "bar-parity obstruction from a matrix direction. NOT scope-(b) for a COMPLEX "
        "fibre-level pole; surviving open object = pole→cusp phase φ(q₀) "
        "(qbeta_c3_barodd_pole_cusp_phase_probe.py), the fibre continuation that is the "
        "c₃⟺q₀ crux bwS0_eq_hecke. No fit; nothing wired; no tier change."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("target", {
        "S_proton": mp.nstr(S(qp), 8), "S_muon": mp.nstr(S(qm), 8),
        "target_ratio": mp.nstr(S(qp) / S(qm), 6), "bar_parity": "bar-ODD (opposite sign)"})
    wb.add_data("finding1_no_flip", {
        "hs_ratio_mu0": mp.nstr(ratio0, 8), "any_sign_flip": bool(any_flip),
        "hs_by_mu": {name: {"proton": mp.nstr(rp["hs"][name], 8),
                            "muon": mp.nstr(rm["hs"][name], 8)} for name, _ in mus},
        "verdict": "no geometric mu produces the sign flip; HS ratio ~+1 vs target -4.08"})
    wb.add_data("finding2_bar_even", {
        "bar_even_all_mu": bool(bar_even_all),
        "verdict": "real matrix Gram-resolvent is bar-EVEN; S is bar-ODD "
                   "(Lean fig8Trace_im_odd) => cannot carry the chirality"})
    wb.add_data("finding3_no_eigen_crossing", {
        "max_eigen_shift": mp.nstr(max_shift, 6), "min_gap_or_dist_to_zero": mp.nstr(min_gap, 6),
        "no_crossing": bool(no_crossing),
        "verdict": "eigenvalue shift ~3e-8 << min gap (O(0.1)); no level/zero crossing, so a "
                   "between-anchor geometric pole needs mu tuned to ~1e-8 (a fit) AND diverges "
                   "(pole) rather than zero-crossing like S at q*"})
    wb.add_data("scope", {
        "tier": "scope-(a) negative on a construction (real matrix Gram-resolvent)",
        "structural_exclusion_real_resolvent": True,
        "structural_exclusion_invariant": "bar-parity (fig8Trace_im_odd, CuspShapeBarParity)",
        "structural_exclusion_general_resolvent": False,
        "surviving_open_object": "fibre-level COMPLEX pole->cusp phase phi(q0) "
                                 "(qbeta_c3_barodd_pole_cusp_phase_probe.py); the "
                                 "root-of-unity->real-q0 continuation = c3<->q0 crux bwS0_eq_hecke",
        "c_k_wired": False, "fit": False})
    wb.add_assertion("no_sign_flip_at_any_geometric_mu",
                     computed=0.0 if any_flip else 1.0, expected=1.0, tolerance=0.5,
                     source="HS(proton)/HS(muon)~+1.0000 at every geometric mu (0/1/z/near-pole) "
                            "vs target ratio -4.08; no flip")
    wb.add_assertion("pairing_is_bar_even",
                     computed=1.0 if bar_even_all else 0.0, expected=1.0, tolerance=0.5,
                     source="|HS(q)-HS(1/q)| << |HS(q)+HS(1/q)| at mu in {0,1}; S is bar-ODD "
                            "(fig8Trace_im_odd) so a real bar-even resolvent cannot carry it")
    wb.add_assertion("gram_eigenvalues_do_not_cross",
                     computed=1.0 if no_crossing else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="max |dlambda| ~3e-8 << min eigen gap O(0.1); no level/zero crossing "
                            "=> no geometric pole enters the anchor window without a ~1e-8 fit")
    wb.save()
    print("\n  RESULT: real matrix Gram-resolvent route CLOSED by bar-parity (scope-a); "
          "only the complex fibre-level pole->cusp phase phi(q0) survives.")
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
