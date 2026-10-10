#!/usr/bin/env python3
"""full_tower_weight_two_arm_probe.py — the canonical binding under two FULL-TOWER
partition weights, side by side with the convention-D control.

EXPLORATORY. NOT WIRED. Owner instruction 2026-10-10 (bean `qou-zf9n`, T5 "try
both"): evaluate BOTH candidate full-tower weights for the mass/binding channel
as two arms, adopt neither. Per the anti-fit directive this probe does NOT rank
the arms by accuracy and does NOT recommend either; it reports what each
derives.

WHAT IS HELD FIXED (identical in every arm)
-------------------------------------------
* The braid words: `atom_braid_word_3A(Z, N, intra_order="borromean")` — the
  canonical interleaved atom word, with and without the inter-nucleon bonds.
* The characters: `chi_all_lambda_any(word, 3A, dps=50)` over ALL p(3A)
  partitions, at the proton-pinned q0 (`Q_50_DIGIT_STR`).
* The functional: `binding_canonical`'s `B_lin = Q_beta(n)·(tr(W_free) −
  tr(W_atom))`, plus — reported alongside, not instead — the log-free-energy
  `B_log = E_0·log(|tr(W_free)|/|tr(W_atom)|)` of `binding_log_free_energy.py`,
  `E_0 = m_e/(q0(q0−1))`.

WHAT VARIES: the partition weight. Every arm is written as a MEASURE `mu_λ`
on partitions with `Σ_λ mu_λ = 1`, entering the trace as

    tr(x) = Σ_λ (mu_λ / f^λ) · χ^λ(x),         so tr(1) = Σ_λ mu_λ = 1,

which is the normalisation the control already has (`Σ_λ y_λ f^λ = 1`).

  control   y_λ  = Wenzl/Ocneanu Markov weight, convention D (`y_lambda_at`,
            SU(2), zero on every λ with ≥ 3 rows);  mu_λ = y_λ·f^λ.
  arm M     Molien measure  mu_λ = f^λ · q^{−κ_λ} · dim_q(λ) / [n]_q!,
            κ_λ = Σ_cells content.  Σ_λ = 1 is LEAN-PROVED for every n and q>1:
            `QOU.MathlibExt.NormalizedSumUnconditional.molienSum_eq_qFactorial`.
  arm P     quantum Plancherel, self-normalised  mu_λ = dim_q(λ)² / D²,
            D² = Σ_λ dim_q(λ)²  (Reshetikhin–Turaev / Verlinde form).

`dim_q(λ) = [n]_q!/∏_cells [h]_q` with BALANCED q-integers — the corpus
convention, and the one `molienSum` is stated in.

🛑 The Molien weight as the owner's instruction wrote it, `f^λ·dim_q(λ)/[n]_q!`,
omits the `q^{−κ_λ}` twist. The Lean theorem that makes it sum to 1 INCLUDES
the twist (`molienSum := Σ dimSYT · q^(−contentSum) · qDim`), so the corpus
artifact decides and the twisted form is used. The untwisted sum is computed
and reported (`molien_untwisted_sum`) so the difference is visible, not hidden.

NAMING. The y_lambda conflation audit forbids calling a non-Wenzl weight
`y_lambda`. Here `y_lambda` names ONLY the convention-D control; the two arms are
`mu_molien` / `mu_plancherel_dq2_over_D2`, and every per-partition block
declares `weight_family`.

TL-SUPPORT (the zf9n question). Under convention D the closure is supported on
the Temperley–Lieb quotient (≤ 2-row partitions) by Schur vanishing at N = 2.
Both full-tower weights are strictly positive on EVERY λ, so the question
becomes quantitative: what fraction of (i) the binding trace difference
Σ_λ (mu/f)(χ_free − χ_atom) and (ii) the deuteron crystal closure
Σ_λ (mu/f)·χ^λ·sgn(w0)·f^λ (`rho_w_crystal_vertex_trace`'s formula) sits on
≤ 2-row λ. Both the signed fraction and the absolute-mass fraction are reported,
because a signed fraction of a cancelling sum can exceed 1.

Precision: mpmath throughout; weights at 70 dps, characters at their validated
50 dps (passed explicitly — `chi_all_lambda_any` has its own dps default). No
float64. Output: full-tower-weight-two-arm-probe.witness.json (this directory).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402

INTRA_ORDER = "borromean"
CHI_DPS = 50
ATOMS = (("D", 1, 1, AME_B_DEUTERON_MEV_VALIDATION),
         ("T", 1, 2, AME_B_TRITIUM_MEV_VALIDATION),
         ("3He", 2, 1, AME_B_HE3_MEV_VALIDATION),
         ("4He", 2, 2, AME_B_HE4_MEV_VALIDATION))
ARMS = ("control_D", "molien", "plancherel")
FAMILY = {
    "control_D": "markov_wenzl_ocneanu_convention_D_SU2 (y_lambda * f^lambda)",
    "molien": "molien_fake_degree f*q^-kappa*dim_q/[n]_q! (Lean: molienSum_eq_qFactorial)",
    "plancherel": "quantum_plancherel_self_normalised dim_q^2/D^2",
}


# ── exact combinatorics ────────────────────────────────────────────────────
def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    return [lam[i] - j - 1 + conj[j] - i - 1 + 1
            for i in range(len(lam)) for j in range(lam[i])]


def f_lambda(lam) -> int:
    n = sum(lam)
    num = 1
    for k in range(2, n + 1):
        num *= k
    den = 1
    for h in hooks(lam):
        den *= h
    assert num % den == 0
    return num // den


def content_sum(lam) -> int:
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def sgn_w0(lam) -> int:
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return -1 if sum(c * (c - 1) // 2 for c in conj) % 2 else 1


# ── balanced q-arithmetic, mpf ─────────────────────────────────────────────
def q_int(m: int, q):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def q_fact(n: int, q):
    out = mp.mpf(1)
    for m in range(1, n + 1):
        out *= q_int(m, q)
    return out


def dim_q(lam, q):
    den = mp.mpf(1)
    for h in hooks(lam):
        den *= q_int(h, q)
    return q_fact(sum(lam), q) / den


def measures(n: int, shapes, q):
    """{arm: {λ: mu_λ}} — every arm a measure on partitions of n."""
    qf = q_fact(n, q)
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}
    mu_ctrl = {s: y.get(s, mp.mpf(0)) * f_lambda(s) for s in shapes}
    mu_mol = {s: f_lambda(s) * q ** (-content_sum(s)) * dim_q(s, q) / qf
              for s in shapes}
    dq2 = {s: dim_q(s, q) ** 2 for s in shapes}
    D2 = mp.fsum(dq2.values())
    mu_pl = {s: v / D2 for s, v in dq2.items()}
    untwisted = mp.fsum(f_lambda(s) * dim_q(s, q) / qf for s in shapes)
    return ({"control_D": mu_ctrl, "molien": mu_mol, "plancherel": mu_pl},
            y, untwisted)


def tl_fractions(terms: dict):
    """(signed two-row fraction, absolute two-row fraction) of Σ terms."""
    tot = mp.fsum(terms.values())
    two = mp.fsum(v for s, v in terms.items() if len(s) <= 2)
    abs_tot = mp.fsum(abs(v) for v in terms.values())
    abs_two = mp.fsum(abs(v) for s, v in terms.items() if len(s) <= 2)
    signed = two / tot if tot != 0 else None
    return tot, signed, (abs_two / abs_tot if abs_tot != 0 else None)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(M_E_MEV)
    Qb = mp.mpf(Q_NEUTRON_MEV)
    E0 = m_e / (q * (q - 1))
    checks = []

    def chk(name, ok, detail=""):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

    rows = []
    for atom, Z, N, B_ame_src in ATOMS:
        A = Z + N
        n = 3 * A
        B_ame = mp.mpf(B_ame_src)
        w_atom = atom_braid_word_3A(Z, N, include_inter=True,
                                    intra_order=INTRA_ORDER)
        w_free = atom_braid_word_3A(Z, N, include_inter=False,
                                    intra_order=INTRA_ORDER)
        chi_a = {tuple(k): mp.mpf(v) for k, v in
                 chi_all_lambda_any(w_atom, n, dps=CHI_DPS).items()}
        chi_f = {tuple(k): mp.mpf(v) for k, v in
                 chi_all_lambda_any(w_free, n, dps=CHI_DPS).items()}
        mp.mp.dps = max(mp.mp.dps, 70)
        shapes = sorted(chi_a, reverse=True)
        mus, y, untwisted = measures(n, shapes, q)
        chk(f"{atom}: every arm is a probability measure (|Σ mu − 1| < 1e-45)",
            all(abs(mp.fsum(mus[a].values()) - 1) < mp.mpf("1e-45") for a in ARMS),
            " ".join(f"{a}={mp.nstr(mp.fsum(mus[a].values()) - 1, 3)}" for a in ARMS))
        arm_out = {}
        for arm in ARMS:
            mu = mus[arm]
            tw = {s: mu[s] / f_lambda(s) for s in shapes}
            tr_a = mp.fsum(tw[s] * chi_a[s] for s in shapes)
            tr_f = mp.fsum(tw[s] * chi_f[s] for s in shapes)
            d_terms = {s: tw[s] * (chi_f[s] - chi_a[s]) for s in shapes}
            dtr, d_signed, d_abs = tl_fractions(d_terms)
            B_lin = Qb * (tr_f - tr_a)
            # A trace below the characters' own resolution is ZERO to the
            # arithmetic used, not a small number: its log is set by rounding
            # residue. Measured: Molien tr(W_atom) ~1e-75 at 3He and 4He.
            floor = mp.mpf(10) ** (-(CHI_DPS - 10))
            vanishes = abs(tr_a) < floor or abs(tr_f) < floor
            B_log = (None if vanishes
                     else E0 * mp.log(abs(tr_f) / abs(tr_a)))
            out = {
                "weight_family": FAMILY[arm],
                "tr_atom": fmt(tr_a), "tr_free": fmt(tr_f),
                "delta_tr": fmt(dtr),
                "B_lin_MeV": fmt(B_lin),
                "B_lin_rel_err_vs_AME": fmt((B_lin - B_ame) / B_ame),
                "trace_vanishes_to_working_precision": bool(vanishes),
                "B_log_MeV": fmt(B_log) if B_log is not None else None,
                "B_log_rel_err_vs_AME": (fmt((B_log - B_ame) / B_ame)
                                         if B_log is not None else None),
                "tl_quotient_signed_fraction_of_delta_tr":
                    fmt(d_signed) if d_signed is not None else None,
                "tl_quotient_abs_fraction_of_delta_tr":
                    fmt(d_abs) if d_abs is not None else None,
                "mass_on_tl_quotient": fmt(mp.fsum(
                    mu[s] for s in shapes if len(s) <= 2)),
            }
            if atom == "D":
                c_terms = {s: tw[s] * chi_a[s] * sgn_w0(s) * f_lambda(s)
                           for s in shapes}
                c_tot, c_signed, c_abs = tl_fractions(c_terms)
                out["crystal_closure_sum"] = fmt(c_tot)
                out["crystal_closure_B_MeV"] = fmt(m_e * abs(c_tot))
                out["crystal_closure_captured_fraction"] = fmt(
                    m_e * abs(c_tot) / B_ame)
                out["crystal_closure_tl_signed_fraction"] = (
                    fmt(c_signed) if c_signed is not None else None)
                out["crystal_closure_tl_abs_fraction"] = (
                    fmt(c_abs) if c_abs is not None else None)
                out["crystal_closure_cancellation_ratio"] = fmt(
                    mp.fsum(abs(v) for v in c_terms.values()) / abs(c_tot))
            per = [{"partition": list(s), "f_lambda": f_lambda(s),
                    "mu": fmt(mu[s])} for s in shapes]
            out["per_partition"] = {"weight_family": FAMILY[arm], "rows": per}
            arm_out[arm] = out
            print(f"  {atom:>3} {arm:<11} B_lin={mp.nstr(B_lin, 10):>14} "
                  f"B_log={mp.nstr(B_log, 10) if B_log is not None else 'NA':>14} "
                  f"TL(Δtr) signed={mp.nstr(d_signed, 6) if d_signed is not None else 'NA'} "
                  f"abs={mp.nstr(d_abs, 6) if d_abs is not None else 'NA'}  "
                  f"({time.monotonic() - t0:.1f}s)", flush=True)
        # control must reproduce binding_canonical exactly (same words, y, chi)
        if atom in ("D", "T", "3He", "4He"):
            from binding_canonical import binding_canonical
            ref = binding_canonical(Z, N)
            gap = abs(mp.mpf(ref["delta_tr_exact"])
                      - mp.mpf(arm_out["control_D"]["delta_tr"]))
            chk(f"{atom}: control arm reproduces binding_canonical Δtr (< 1e-40)",
                gap < mp.mpf("1e-40"), f"gap={mp.nstr(gap, 3)}")
        rows.append({"atom": atom, "Z": Z, "N": N, "A": A, "n_strands": n,
                     "n_partitions": len(shapes),
                     "B_AME_MeV": mp.nstr(B_ame, 15),
                     "molien_untwisted_sum": fmt(untwisted),
                     "arms": arm_out})

    w = WitnessBuilder("full-tower-weight-two-arm-probe", engine="python",
                       start_time=t0)
    w.set_description(
        "Canonical binding (binding_canonical route, borromean words, proton q0) "
        "under the convention-D Markov weight (control) and two full-tower "
        "partition measures — Molien f·q^-κ·dim_q/[n]_q! and self-normalised "
        "quantum Plancherel dim_q²/D² — side by side, with the TL-quotient "
        "support fraction of each. EXPLORATORY: neither arm is adopted or "
        "wired; arms are NOT ranked by accuracy (anti-fit directive).")
    w.add_data("q0", Q_50_DIGIT_STR)
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("intra_order", INTRA_ORDER)
    w.add_data("chi_dps", CHI_DPS)
    w.add_data("trace_slot", "tr(x) = Σ_λ (mu_λ/f^λ) χ^λ(x); tr(1) = Σ mu = 1")
    w.add_data("functionals", {
        "B_lin": "Q_beta(n)·(tr(W_free) − tr(W_atom))  [binding_canonical route]",
        "B_log": "E_0·log(|tr(W_free)|/|tr(W_atom)|), E_0 = m_e/(q0(q0−1))  "
                 "[binding_log_free_energy route, reported alongside]",
    })
    w.add_data("E_0_MeV", fmt(E0))
    w.add_data("Q_beta_n_MeV", str(Q_NEUTRON_MEV))
    w.add_data("weight_families", FAMILY)
    w.add_data("molien_twist_note", (
        "Owner wrote f·dim_q/[n]_q!; the Lean-proved normalised form "
        "(molienSum_eq_qFactorial) carries q^-κ_λ. The twisted form is used; "
        "molien_untwisted_sum records the untwisted total."))
    w.add_data("vanishing_trace_note", (
        "Where |tr| < 1e-40 the trace is zero to the 50-dps characters' "
        "resolution and B_log is reported None (undefined), not as a number. "
        "Consistent with the Molien measure being the regular/symmetrising "
        "trace decomposition (identity-coefficient functional), per "
        "computations/probes/phi_k_weight_family_discriminator.py §A3 — "
        "recorded as consistency, not proved here."))
    w.add_data("adoption", "none — exploratory two-arm comparison, not wired")
    w.add_data("rows", rows)
    w.add_data("checks", checks)
    for c in checks:
        w.add_assertion(name=c["name"], computed="1" if c["passed"] else "0",
                        expected="1", tolerance="0", source=c["detail"] or None)
    out = w.save()
    print(f"Witness: {out}  ({time.monotonic() - t0:.1f}s)")
    return 0 if all(c["passed"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
