#!/usr/bin/env python3
"""qbeta_h4_tower_branching_preflight.py — formalize-first preflight for the
Q_β c_4 H₄-tower (Stage C): validate the H₃⊂H₄ machinery + branching map and
localize the OPEN content to the σ₃ (level-4) lift, WITHOUT fabricating c_4.

CONTEXT (1ppQ-Q_β keystone, the N≥1 tower).  PR #2465's mode→ladder bridge
(C13) refuted the A=1 / N=0 `Δtr_M`-seeded c_4; #2469's counit is also N=0;
#2106's Stage-B found "H₃ level support stops at ℓ=3 ⇒ c₄..c₈ require the
H_{n≥4} towers."  Synthesis: c_k≥3 live in the N≥1 / H_{n≥4} tower, not in any
A=1 functional.  This preflight does the formalize-first step BEFORE the
expensive Stage-C build: it checks the structural premise that the H₄ tower
adds a new degree of freedom only along the new strand σ₃.

WHY BRANCHING IS THE RIGHT (weight-free, non-fitting) PROBE.  For an element
`w ∈ H₃ ⊂ H₄` (a word in σ₁,σ₂ only — i.e. NOT involving the new strand σ₃),
its H₄ representation is determined by restriction:
    χ^μ_{H₄}(w) = Σ_{λ⊢3, λ ↗ μ} χ^λ_{H₃}(w)            (branching rule)
where `λ ↗ μ` means μ is obtained from λ by adding one box.  So the H₄ data of
a σ₃-FREE element carries NO information beyond its H₃ data — the tower adds a
new DOF ONLY through σ₃ (the level-4 direction).  This is the structural reason
the scalar-trace tower is trivial (C12: tr_M^{H₄}(ι w) = z·tr_M^{H₃}(w)); the
c_4 content must come from a σ₃-involving (length-4) operator lift, which is the
OPEN Stage-C categorical specification.

WHAT THIS PROBE ESTABLISHES (exact-ish at 50 dps; NO fit, NO c_4 value):

  1. H₄ Hoefsmit seminormal reps build + satisfy Hecke (σ_i²=(q−q⁻¹)σ_i+1) and
     braid (σ₁σ₂σ₁=σ₂σ₁σ₂, σ₂σ₃σ₂=σ₃σ₂σ₃, σ₁σ₃=σ₃σ₁) relations — the Stage-C
     foundation is correct (young_seminormal validated to λ⊢6).
  2. The H₃⊂H₄ branching map χ^μ(w) = Σ_{λ↗μ} χ^λ(w) holds for every σ₃-free
     decay word and every μ⊢4 (the structural induction map Stage-C builds on).
  3. σ₃-GATING DEMONSTRATED: σ₃-free elements have no new H₄ content ⇒ the c_4
     rung is gated on the OPEN length-4 σ₃-lift, not extractable from any A=1 /
     σ₃-free object (consistent with C12 + the C13 refutation).

DISCIPLINE (AGENTS.md §7b, refuted-class map, formalize-first): this is the
forward-pruning preflight, not a c_4 extraction.  It validates the foundation
and pins the open question; it does NOT propose a σ₃-lift (that would be
fitting).  No production wiring; no registry change.
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "70")

from young_seminormal import seminormal_sigma, chi_young, standard_tableaux  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50
Q = mp.mpf("1.1099785827513808075916690956107688798744991218735787360728142402")


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """Partitions of n in descending-part form (largest first)."""
    def rec(n, mx):
        if n == 0:
            yield ()
            return
        for k in range(min(n, mx), 0, -1):
            for rest in rec(n - k, k):
                yield (k,) + rest
    return list(rec(n, n))


def removable_to(mu: tuple[int, ...]) -> list[tuple[int, ...]]:
    """λ⊢(|mu|−1) obtained by removing one removable (corner) box from mu."""
    out = []
    for r in range(len(mu)):
        # box (r, mu[r]-1) is removable iff it's a corner:
        if r == len(mu) - 1 or mu[r] > mu[r + 1]:
            lam = list(mu)
            lam[r] -= 1
            lam = tuple(x for x in lam if x > 0)
            out.append(lam)
    return out


def word_of(gens: tuple[int, ...]):
    """H_n word (product of σ_g, 0-based g) in chi_young's (c,d,g) format."""
    return [(mp.mpf(1), mp.mpf(0), g) for g in gens]


def mat_mul(A, B):
    return A * B


def main() -> int:
    t0 = time.monotonic()
    wb = WitnessBuilder("qbeta-h4-tower-branching-preflight", engine="python+mpmath",
                        start_time=t0)
    wb.set_description(
        "Formalize-first preflight for the Q_β c_4 H₄-tower (Stage C): validates "
        "the H₄ Hoefsmit seminormal reps (Hecke+braid relations) and the H₃⊂H₄ "
        "branching map χ^μ(w)=Σ_{λ↗μ}χ^λ(w) on the σ₃-free decay words, "
        "demonstrating that the tower adds a new DOF only along σ₃ (level-4). "
        "Localizes the c_4 content to the OPEN σ₃-lift; no c_4 fabricated, no fit."
    )
    wb.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" Q_β c_4 H₄-TOWER PREFLIGHT — seminormal validation + H₃⊂H₄ branching")
    print("=" * 78)

    # ── 1. validate H₄ seminormal reps: Hecke + braid relations ───
    print("\n  [1] H₄ Hoefsmit seminormal reps — Hecke + braid relations")
    qi = 1 / Q
    hecke_ok, braid_ok = True, True
    parts4 = partitions_of(4)
    for lam in parts4:
        d = len(standard_tableaux(lam))
        sig = {i: seminormal_sigma(lam, i, Q) for i in (1, 2, 3)}
        I = mp.eye(d)
        for i in (1, 2, 3):
            # Hecke: σ_i² − (q−q⁻¹)σ_i − 1 = 0
            resid = sig[i] * sig[i] - (Q - qi) * sig[i] - I
            if max(abs(resid[a, b]) for a in range(d) for b in range(d)) > mp.mpf(10) ** -40:
                hecke_ok = False
        # braid σ₁σ₂σ₁=σ₂σ₁σ₂ ; σ₂σ₃σ₂=σ₃σ₂σ₃
        for (i, j) in ((1, 2), (2, 3)):
            lhs = sig[i] * sig[j] * sig[i]
            rhs = sig[j] * sig[i] * sig[j]
            if max(abs((lhs - rhs)[a, b]) for a in range(d) for b in range(d)) > mp.mpf(10) ** -40:
                braid_ok = False
        # far commutation σ₁σ₃=σ₃σ₁
        c13 = sig[1] * sig[3] - sig[3] * sig[1]
        if max(abs(c13[a, b]) for a in range(d) for b in range(d)) > mp.mpf(10) ** -40:
            braid_ok = False
        print(f"    λ={str(lam):12s} dim={d}  reps built")
    print(f"    Hecke relation  σ_i²=(q−q⁻¹)σ_i+1 : {'OK' if hecke_ok else 'FAIL'}")
    print(f"    braid + far-commutation relations : {'OK' if braid_ok else 'FAIL'}")

    # ── 2. H₃⊂H₄ branching χ^μ(w)=Σ_{λ↗μ}χ^λ(w) on σ₃-free decay words ─
    print("\n  [2] H₃⊂H₄ branching on σ₃-free words (the structural induction map)")
    # the 6 H₃ Gröbner–Shirshov normal-form basis words (free-neutron-decay.py)
    nf_basis = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    parts3 = partitions_of(3)
    branch = {mu: removable_to(mu) for mu in parts4}
    print("    branching μ⊢4 ↓ H₃:")
    for mu in parts4:
        print(f"      {str(mu):12s} ↓ = {' + '.join(str(l) for l in branch[mu])}")
    max_branch_err = mp.mpf(0)
    for w in nf_basis:
        word = word_of(w)
        chi3 = {lam: chi_young(lam, word, Q) for lam in parts3}
        for mu in parts4:
            chi4 = chi_young(mu, word, Q)
            summed = mp.fsum(chi3[lam] for lam in branch[mu])
            err = abs(chi4 - summed) / (1 + abs(chi4))
            max_branch_err = max(max_branch_err, err)
    branch_ok = max_branch_err < mp.mpf(10) ** -40
    print(f"    χ^μ(w) = Σ_(λ↗μ) χ^λ(w) for all 6 σ₃-free words, all μ⊢4:")
    print(f"      max rel error = {mp.nstr(max_branch_err, 4)}  "
          f"{'OK (branching holds)' if branch_ok else 'MISMATCH'}")

    # ── 3. σ₃-gating: the level-4 direction is the open content ────
    max_h3_len = max(len(w) for w in nf_basis)
    print("\n  [3] σ₃-GATING (the open Stage-C content)")
    print(f"    H₃ normal-form words reach max length {max_h3_len} (σ₁σ₂σ₁) ⇒ the "
          f"decay operator's level grading stops at ℓ={max_h3_len}.")
    print("    A level-4 component requires a length-4 H₄ word involving σ₃ (the")
    print("    new strand). By [2], every σ₃-FREE element's H₄ data is the branched")
    print("    H₃ data — NO new DOF. So the c_4 rung is gated on the OPEN")
    print("    categorical σ₃-lift (Stage C), not extractable from any A=1 /")
    print("    σ₃-free object — consistent with C12 (trace stabilises to z·tr) and")
    print("    the C13 bridge refutation. NO σ₃-lift proposed here (would be a fit).")

    # ── witness ────────────────────────────────────────────────────
    wb.add_data("h4_seminormal_validation", {
        "partitions_of_4": [list(p) for p in parts4],
        "dims": {str(lam): len(standard_tableaux(lam)) for lam in parts4},
        "hecke_relation_ok": bool(hecke_ok),
        "braid_and_far_commutation_ok": bool(braid_ok),
        "tolerance": "1e-40",
    })
    wb.add_data("h3_h4_branching", {
        "map": {str(mu): [list(l) for l in branch[mu]] for mu in parts4},
        "verified_on_words": [list(w) for w in nf_basis],
        "max_rel_error": mp.nstr(max_branch_err, 6),
        "branching_holds": bool(branch_ok),
        "identity": "chi^mu_{H4}(w) = sum_{lambda -> mu} chi^lambda_{H3}(w)",
    })
    wb.add_data("sigma3_gating", {
        "h3_max_word_length": max_h3_len,
        "conclusion": "sigma_3-free elements carry no new H4 content (branching); "
                      "c_4 is gated on the OPEN length-4 sigma_3 lift (Stage C).",
        "no_sigma3_lift_proposed": True,
        "consistent_with": ["C12 (trace stabilisation z·tr)",
                            "C13 (Delta_trM-seeded bridge refuted, PR #2465)"],
    })
    wb.add_assertion(
        "h4_seminormal_relations_hold",
        computed=1.0 if (hecke_ok and braid_ok) else 0.0,
        expected=1.0, tolerance=0.0,
        source="H₄ Hoefsmit seminormal reps (all λ⊢4) satisfy the Hecke + braid "
               "+ far-commutation relations to 1e-40 — the Stage-C foundation.",
    )
    wb.add_assertion(
        "h3_h4_branching_holds",
        computed=1.0 if branch_ok else 0.0,
        expected=1.0, tolerance=0.0,
        source="χ^μ(w)=Σ_(λ↗μ)χ^λ(w) for all 6 σ₃-free decay words, all μ⊢4 "
               "(max rel err < 1e-40) — the H₃⊂H₄ structural map; σ₃-free "
               "elements add no new DOF, so c_4 is σ₃-gated (open Stage C).",
    )
    wb.save()
    print(f"\n  Witness: qbeta-h4-tower-branching-preflight.witness.json")
    print(f"  wall: {round(time.monotonic() - t0, 1)} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
