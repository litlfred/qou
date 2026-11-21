#!/usr/bin/env python3
"""The block and the producer are two different functionals — measured, and the
discriminator is that one of them cannot be written in the other's variables.

Owner ruling 2026-09-12, verbatim: **"resolve functionals ... what lean
provable"**.  Beans qou-zlra (which found the mismatch, PR #7230), qou-t6be
(this resolution).  Lean: `QOU.MassTheory.UICFunctionalSelection` and
`QOU.MassTheory.UICLogSummandEven`, both sorry-free, lean-direct exit 0.

WHAT IS COMPARED

`prop:unified-iterative-correction` (`unified-iterative-correction.md:1-10`)
states

    B_lambda = m_e * H_q(lambda) * u_lambda * ( ln|tr M_lambda| - ln d_lambda )

with `u_lambda` called *"its Frobenius positivity LP shadow price"* and the
total *"summed strictly over all lambda"*.

`hecke_core_legacy.unified_iterative_correction` computes

    B = sum over lambda with tr M_lambda(atom) <= 0  of
          C_lambda^res * ( ln|tr M_lambda(atom)| - ln d_lambda )
    C_lambda^res = m_e * H_q(lambda) * y_lambda * rho_lambda(s_*)      (:548, :1915)
    rho_lambda(s) = 1 / (mu_lambda + s_*),  s_* = (q0-1)/q0            (:300-325, :520)
    y_lambda      = w_lambda/d_lambda - 1/[k]_q!                       (:328-360)
    gate          = Pass 2, final-state sign                           (:2176-2188)

THE SIX MEASUREMENTS

1.  BOTH totals are reproduced from (C_lambda, tr_lambda, d_lambda) alone, in
    mpf, to the full recorded precision.  This is the accumulator's own
    telescoping identity (`unified_telescope_partition` in the block's .lean),
    and it is what licenses every other measurement here: the running matrix
    product does not need to be re-derived, only its final trace.

2.  SUMMATION RANGE.  Ungated against gated at 2H and 4He, reproducing the
    3.4-4.6x spread the producer's own note records at :2148-2153 rather than
    quoting it.

3.  THE DISCRIMINATOR.  Flip the sign of every final trace.  The UNGATED total
    is bit-identical (the summand reads only |tr|); the GATED total moves.  So
    the gate is not a function of the data the block's formula displays --
    `gate_not_a_function_of_displayed_data`, measured.

4.  GENUINE COMPLEMENTARY SLACKNESS SELECTS NOTHING.  For a constraint
    <Phi, pi_lambda> >= 0, "tight" means tr = 0, not tr <= 0.  No active
    partition has tr = 0 at the final state, so the CS-justified gate is the
    empty sum -- `cs_selection_excludes_log_domain` / `uicGated_cs_eq`.

5.  THE RESOLVENT IS NOT NEGLIGIBLE, and it is not a sign.  C_lambda >= 0 on
    every partition in the table, and deleting rho (what the block's formula
    does) moves the gated total by a measured factor, not a rounding.

6.  y_lambda IS NOT THE PARTITION-INDEXED FROBENIUS DUAL EITHER.  The corrected
    `prop:mass-coefficient-shadow-price` (`:22-28`) allows one surviving reading
    of "shadow price" -- the partition-indexed solve, which at H_3 gives
    y*_(3) = y*_(2,1) = 1, y*_(1^3) = 0.  The producer's closed form gives
    (0, 0.167, 0).  Both candidate readings therefore fail.

WHAT IS NOT CLAIMED

Not that the gate is wrong.  Measurement 4 shows its STATED justification does
not hold; a selection rule can be right for a reason other than the one given
(AGENTS.md, scope-(a) vs scope-(b)).  Not that the ungated sum is the physics.
Not that any binding number here is accurate -- both readings are wrong-signed
against AME and that is qou-sv7h / qou-brng, untouched.

A PRECISION FINDING ABOUT THE PRODUCER, reported and NOT fixed here.  `mu_lambda`
(`q_laplacian_eigenvalue`, :292 `casimir_sum = 0.0`) and `s_*`
(`S_REEB_PLANCK`, :520) are float64, so `rho_lambda` and hence every
`C_lambda_resolvent_MeV` carries a float64-limited factor.  Measurement 5
quantifies the gap against an mpf recomputation.  Fixing it would move every
binding number in the corpus and is out of scope for a resolution PR; bean
qou-t6be carries it.

scope-(a); no fit; nothing wired; no c_k; L2 unchanged.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

from _precision import COMPUTE_DPS, fmt, set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
if mp.dps < 70:
    mp.dps = 70

import hecke_core_legacy as H  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   -- {detail}" if detail else ""))


# ── exact substrate constants, recomputed in mpf at the proton pin ──────────
Q = mp.mpf(str(q_at()))
QI = 1 / Q
HA = Q - QI
S_STAR = (Q - 1) / Q                       # the Planck-step Reeb frequency
Z_D = Q ** 3 / (Q ** 2 + 1)                # convention D, recorded for the frame


def q_int_mp(n: int):
    """Balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1), in mpf."""
    return (Q ** n - QI ** n) / HA


def mu_mp(partition) -> "mp.mpf":
    """Jucys-Murphy q-Casimir mu_lambda = sum_{cells} [c]_q [c+1]_q, in mpf.

    Mirrors `hecke_core_legacy.q_laplacian_eigenvalue` exactly; the producer
    accumulates the same sum in float64 (`casimir_sum = 0.0`, :292).
    """
    total = mp.mpf(0)
    for i, li in enumerate(partition):
        for j in range(li):
            c = j - i
            total += q_int_mp(c) * q_int_mp(c + 1)
    return total


KEXACT = 4          # cheapest level that carries the whole phenomenon
ATOMS = [(1, 1, "2H"), (2, 2, "4He")]


def final_traces(entry, ordering):
    """Final (signed trace, accumulated log-norm) of the running YSN product,
    from the same Rust MPFR kernel the producer's Pass 1 calls."""
    chains = [
        H._step_chain_generic(ordering[k], ordering[:k], entry["n_gens"])
        for k in range(len(ordering))
    ]
    steps = H._lp_kernel_steps(entry["partition"], chains)
    tr, log_norm = steps[-1]
    return mp.mpf(tr), mp.mpf(log_norm)


def ground_ordering(Z: int, N: int) -> list[str]:
    """Ground-state p/n ordering, byte-identical to the producer's (:1821-1828)."""
    order, pc, nc = [], 0, 0
    for kk in range(Z + N):
        if (kk % 2 == 0 and pc < Z) or nc >= N:
            order.append("p")
            pc += 1
        else:
            order.append("n")
            nc += 1
    return order


def main() -> int:
    print(__doc__.split("\n\n")[0])
    print()
    print(f"  mp.dps = {mp.dps}  (COMPUTE_DPS = {COMPUTE_DPS})")
    print(f"  q0     = {mp.nstr(Q, 20)}   (proton pin, qou_substrate.constants.q_at)")
    print(f"  s_*    = {mp.nstr(S_STAR, 20)}")
    print(f"  z_D    = {mp.nstr(Z_D, 20)}   (convention D, frame record)")
    print()

    if not H._HAS_LP_KERNEL:
        print("  REFUSING: the Rust MPFR kernel is absent; the fallback YSN family")
        print("  violates the braid relation, so its traces are not a representation")
        print("  of H_n(q) and no verdict here would be about the producer.")
        return 1

    check("the producer evaluates at the proton pin",
          abs(mp.mpf(str(H.q0)) - Q) < mp.mpf("1e-15"),
          f"|q0_producer - q_at()| = {mp.nstr(abs(mp.mpf(str(H.q0)) - Q), 4)}")

    table = H._PARTITION_TABLE
    active = [e for e in table
              if e["k"] <= KEXACT and e.get("has_ysn", False) and len(e["ysn"]) > 0]
    print(f"\n  partition table: {len(table)} entries, {len(active)} active at "
          f"k_exact = {KEXACT}\n")

    # ── 5a. the scale never supplies a sign (Lean: uicGated_nonpos hypothesis) ──
    n_neg = sum(1 for e in table
                if mp.mpf(str(e["C_lambda_resolvent_MeV"])) < mp.mpf("-1e-12"))
    check("C_lambda >= 0 on every partition in the table",
          n_neg == 0, f"negative in {n_neg} of {len(table)}")

    # ── 6. y_lambda is not the partition-indexed Frobenius dual either ─────────
    print()
    y_h3 = {tuple(lam): mp.mpf(str(H.lp_shadow_price(lam)))
            for lam in H.partitions_of(3)}
    for lam, y in y_h3.items():
        print(f"    y_{lam} = {mp.nstr(y, 12)}")
    # prop:mass-coefficient-shadow-price :22-28 records the committed
    # partition-indexed solve as y*_(3) = y*_(2,1) = 1, y*_(1^3) = 0.
    frob_dual_h3 = {(3,): mp.mpf(1), (2, 1): mp.mpf(1), (1, 1, 1): mp.mpf(0)}
    mismatched = [lam for lam in y_h3
                  if abs(y_h3[lam] - frob_dual_h3[lam]) > mp.mpf("1e-6")]
    check("y_lambda differs from the partition-indexed Frobenius dual at H_3",
          len(mismatched) == 2,
          f"{len(mismatched)} of 3 blocks disagree: {mismatched}")

    rows = []
    for Z, N, name in ATOMS:
        A = Z + N
        ordering = ground_ordering(Z, N)
        print(f"\n  ── {name}  (Z={Z}, N={N}, A={A}, ordering {''.join(ordering)}) ──")

        # producer, as-is
        total, per_step = H.unified_iterative_correction(
            Z, N, return_per_step=True, k_exact=KEXACT, k_max=KEXACT)
        last = per_step[-1]
        raw_prod = mp.mpf(last["raw_total_MeV"])
        gated_prod = mp.mpf(last["gated_total_DISPROVED_SELECTION_MeV"])

        # independent mpf reconstruction from the final traces alone
        ung = mp.mpf(0)
        gat = mp.mpf(0)
        gat_flip = mp.mpf(0)
        ung_no_rho = mp.mpf(0)
        gat_no_rho = mp.mpf(0)
        n_zero_trace = 0
        per_block = []
        for e in active:
            tr, log_norm = final_traces(e, ordering)
            d = e["dim"]
            L = mp.log(abs(tr)) + log_norm - mp.log(d)
            C = mp.mpf(str(e["C_lambda_resolvent_MeV"]))
            # the block's formula, which omits rho: C / rho = m_e H_q y
            rho_prod = mp.mpf(str(e["resolvent_weight_planck"]))
            C_no_rho = C / rho_prod if rho_prod != 0 else mp.mpf(0)
            ung += C * L
            ung_no_rho += C_no_rho * L
            if tr <= 0:
                gat += C * L
                gat_no_rho += C_no_rho * L
            # sign-flip: |tr| unchanged, so L unchanged; only the gate sees it
            if -tr <= 0:
                gat_flip += C * L
            if tr == 0:
                n_zero_trace += 1
            per_block.append({
                "partition": list(e["partition"]),
                "dim": d,
                "trace_sign": 1 if tr > 0 else (0 if tr == 0 else -1),
                "log_ratio": fmt(L),
                "C_lambda_MeV": fmt(C),
                "gated": bool(tr <= 0),
            })

        rel_ung = abs(ung - raw_prod) / abs(raw_prod)
        rel_gat = abs(gat - gated_prod) / abs(gated_prod)
        ratio = raw_prod / gated_prod
        carriers = [b["partition"] for b in per_block
                    if b["gated"] and mp.mpf(b["C_lambda_MeV"]) > mp.mpf("1e-30")]

        print(f"    producer  ungated {mp.nstr(raw_prod, 18)}")
        print(f"    producer  gated   {mp.nstr(gated_prod, 18)}    ratio "
              f"{mp.nstr(ratio, 8)}")
        print(f"    mpf recon ungated {mp.nstr(ung, 18)}   rel {mp.nstr(rel_ung, 4)}")
        print(f"    mpf recon gated   {mp.nstr(gat, 18)}   rel {mp.nstr(rel_gat, 4)}")
        print(f"    sign-flipped: ungated {mp.nstr(ung, 18)} (identical), "
              f"gated {mp.nstr(gat_flip, 18)}")
        print(f"    gated set: {sum(1 for b in per_block if b['gated'])} of "
              f"{len(active)} blocks, of which {len(carriers)} carry C > 0: {carriers}")
        print(f"    rho deleted (the block's formula): gated "
              f"{mp.nstr(gat_no_rho, 18)}")

        # ── 1. the closed form reproduces the producer, both readings ──────────
        check(f"{name}: mpf reconstruction reproduces the producer's UNGATED total",
              rel_ung < mp.mpf("1e-40"), f"rel = {mp.nstr(rel_ung, 4)}")
        check(f"{name}: mpf reconstruction reproduces the producer's GATED total",
              rel_gat < mp.mpf("1e-40"), f"rel = {mp.nstr(rel_gat, 4)}")

        # ── 2. the summation range is a factor, not a rounding ────────────────
        check(f"{name}: gated and ungated differ by a factor in [3.3, 4.7]",
              mp.mpf("3.3") < ratio < mp.mpf("4.7"), f"ratio = {mp.nstr(ratio, 8)}")

        # ── 3. THE DISCRIMINATOR ──────────────────────────────────────────────
        # The ungated total is a function of |tr| alone, so the flip is exact
        # equality by construction, not a tolerance: it is the SAME expression.
        check(f"{name}: the gate MOVES under a sign flip that leaves |tr| fixed",
              abs(gat_flip - gat) > mp.mpf("1e-12"),
              f"gated {mp.nstr(gat, 12)} -> {mp.nstr(gat_flip, 12)}")

        # ── 4. genuine complementary slackness selects nothing ────────────────
        check(f"{name}: no active block has tr = 0, so the CS-justified gate is empty",
              n_zero_trace == 0, f"{n_zero_trace} of {len(active)} blocks at tr = 0")

        # ── 5b. deleting rho is not a rounding ────────────────────────────────
        rho_factor = gat_no_rho / gat
        check(f"{name}: deleting rho moves the gated total by more than 2x",
              abs(rho_factor) > 2, f"factor {mp.nstr(rho_factor, 8)}")

        rows.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "k_exact": KEXACT,
            "ungated_MeV": fmt(raw_prod),
            "gated_MeV": fmt(gated_prod),
            "ungated_over_gated": fmt(ratio),
            "recon_rel_ungated": fmt(rel_ung),
            "recon_rel_gated": fmt(rel_gat),
            "gated_sign_flipped_MeV": fmt(gat_flip),
            "gated_without_resolvent_MeV": fmt(gat_no_rho),
            "resolvent_deletion_factor": fmt(rho_factor),
            "n_active": len(active),
            "n_gated": sum(1 for b in per_block if b["gated"]),
            "n_gated_with_nonzero_scale": len(carriers),
            "n_zero_trace": n_zero_trace,
            "blocks": per_block,
        })

    # ── 5c. how much of rho is float64 ────────────────────────────────────────
    print("\n  ── the producer's resolvent is float64; mpf recomputation ──")
    worst_rel = mp.mpf(0)
    worst_lam = None
    for e in active:
        mu_exact = mu_mp(e["partition"])
        rho_exact = 1 / (mu_exact + S_STAR)
        rho_prod = mp.mpf(str(e["resolvent_weight_planck"]))
        rel = abs(rho_exact - rho_prod) / rho_exact
        if rel > worst_rel:
            worst_rel, worst_lam = rel, tuple(e["partition"])
    print(f"    worst relative gap over {len(active)} active blocks: "
          f"{mp.nstr(worst_rel, 6)} at lambda = {worst_lam}")
    check("the float64 resolvent agrees with mpf to better than 1e-12 relative",
          worst_rel < mp.mpf("1e-12"),
          f"worst {mp.nstr(worst_rel, 6)} at {worst_lam}")

    # ── witness ───────────────────────────────────────────────────────────────
    w = WitnessBuilder("uic-functional-resolution", engine="python+mpmath+rust")
    w.set_description(
        "Owner ruling 2026-09-12 ('resolve functionals ... what lean provable'): "
        "prop:unified-iterative-correction and "
        "hecke_core_legacy.unified_iterative_correction are different functionals, "
        "and the block's displayed formula CANNOT denote the producer's. The "
        "summand ln|tr M| - ln d is even in the trace, so the block's total is "
        "invariant under flipping any block trace's sign; the producer's Pass-2 "
        "gate keeps exactly tr <= 0 and therefore reads a datum the summand has "
        "destroyed. Measured here: both totals reproduced in mpf from the final "
        "traces alone; ungated/gated = 4.60 (2H) and 3.40 (4He); the sign flip "
        "leaves the ungated total identical and moves the gated one; no active "
        "block sits at tr = 0, so genuine complementary slackness (tight means "
        "tr = 0, not tr <= 0) selects the empty set; deleting the q-Laplacian "
        "resolvent the block omits moves the gated total by >2x; and y_lambda "
        "matches neither reading of 'LP shadow price'. Lean: "
        "QOU.MassTheory.UICFunctionalSelection (sorry-free)."
    )
    w.set_audit_only("docs/audits/2026-09-12-uic-functional-resolution.md")
    w.add_data("frame", {
        "q0_proton": fmt(Q),
        "s_star_reeb_planck": fmt(S_STAR),
        "z_D_convention_D": fmt(Z_D),
        "mp_dps": mp.dps,
        "k_exact": KEXACT,
        "kernel_live": True,
    })
    w.add_data("per_atom", rows)
    w.add_data("y_lambda_h3_vs_frobenius_dual", {
        "y_lambda_closed_form": {str(k): fmt(v) for k, v in y_h3.items()},
        "partition_indexed_frobenius_dual": {str(k): fmt(v)
                                             for k, v in frob_dual_h3.items()},
        "source": "prop:mass-coefficient-shadow-price lines 22-28",
    })
    w.add_data("resolvent_float64_gap", {
        "worst_relative": fmt(worst_rel),
        "worst_partition": list(worst_lam) if worst_lam else None,
        "note": ("mu_lambda and s_* are accumulated in float64 by the producer "
                 "(hecke_core_legacy.py:292, :520); reported, not fixed -- a fix "
                 "moves every binding number in the corpus. Bean qou-t6be."),
    })
    for nm, ok, _d in CHECKS:
        w.add_assertion(nm, computed="1" if ok else "0", expected="1",
                        tolerance="0", source="uic_functional_resolution_probe")
    print(f"\n  witness: {w.save()}")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print(f"  {npass}/{len(CHECKS)} checks passed")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
