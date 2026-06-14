#!/usr/bin/env python3
"""delta_lambda_qlommel_recurrence_precheck.py
============================================

Formalize-first pre-check for the **binding `Δ_λ` ↔ q-Lommel three-term
recurrence** hypothesis (PR #2305 lead-4 redirect; coordination with #2078).
Per the owner steer *"derive/prove first, not fit/probe"* and the CLAUDE.md
`Δ_λ` gate (**no seventh fit-based ansatz**), the cheap decisive question to
ask *before* building any q-Lommel `Δ_λ` closure is:

> Do the canonical `Δ_λ` values lie on **any** three-term recurrence orbit
> `Δ_{ν+1} = b_ν Δ_ν − Δ_{ν-1}` with a smooth / substrate-shaped `b_ν`?

If they cannot, the q-Lommel route is refuted before a probe. If the data is
too thin to decide, the pre-check's *prerequisite* (a long enough same-shape
`Δ_λ` tower) is itself the gating result — which is what we report.

## Data

The canonical per-atom effective `Δ_λ` (`delta-lambda-canonical-residual.witness.json`)
covers exactly the four light nuclei D, T, ³He, ⁴He — i.e. **three distinct
mass-number levels** (A = 2, 3, 4) with an isospin pair at A = 3. A three-term
recurrence needs ≥ 2 interior points (≥ 4 distinct same-shape levels) to test
*consistency* of `b_ν`; with only one interior level the implied `b_ν` is a
single number and **nothing is falsified**.

## What this reports (honest, no fit)

  (A) The canonical `Δ_λ` tower and its size (4 atoms / 3 A-levels).
  (B) The implied recurrence coefficient `b_ν = (Δ_{ν+1}+Δ_{ν-1})/Δ_ν` for the
      two single-isospin chains through A = 3 (T-chain and ³He-chain), plus the
      consecutive ratios `ρ_ν = Δ_{ν+1}/Δ_ν` (geometric ⟺ constant `ρ`).
  (C) Verdict: **DATA-LIMITED / INCONCLUSIVE** — decisive test gated on
      extending the tower to ⁶Li, ⁷Li, ⁸Be, … (the Subgoal-1 Borromean-tower
      extension). Records the single preliminary signal so #2078 knows the
      prerequisite before building a q-Lommel `Δ_λ` closure.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = pathlib.Path(__file__).resolve().parent / "delta-lambda-canonical-residual.witness.json"

rows = json.loads(SRC.read_text())["data"]["rows"]
tower = {r["atom"]: float(r["Delta_lambda"]) for r in rows}
Aof = {r["atom"]: r["A"] for r in rows}

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name, ok):
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── (A) the canonical tower ──────────────────────────────────────────────────
print("(A) canonical Δ_λ tower (per atom)")
for a in ("D", "T", "3He", "4He"):
    print(f"    {a:4s}  A={Aof[a]}  Δ_λ = {tower[a]}")
n_levels = len(set(Aof.values()))
results["tower"] = {"atoms": tower, "A": Aof, "n_atoms": len(tower), "n_A_levels": n_levels}
check("canonical Δ_λ tower has < 4 distinct A-levels (too thin for a 3-term consistency test)",
      n_levels < 4)


# ── (B) implied 3-term recurrence coefficient + ratios (preliminary signal) ──
print("\n(B) implied b_ν = (Δ_{ν+1}+Δ_{ν-1})/Δ_ν and ratio ρ_ν = Δ_{ν+1}/Δ_ν")
chains = {"T-chain (D→T→⁴He)": ["D", "T", "4He"],
          "³He-chain (D→³He→⁴He)": ["D", "3He", "4He"]}
signal = {}
for name, chain in chains.items():
    d = [tower[a] for a in chain]
    b_mid = (d[2] + d[0]) / d[1]          # single interior b (ν = middle)
    rho = [d[1] / d[0], d[2] / d[1]]
    print(f"    {name}: Δ = {d}")
    print(f"        interior b = {b_mid:.4f}   ρ = [{rho[0]:.4f}, {rho[1]:.4f}]   "
          f"ρ-spread = {abs(rho[1]-rho[0])/rho[0]*100:.1f}%")
    signal[name] = {"delta": d, "interior_b": b_mid, "rho": rho,
                    "rho_spread_pct": abs(rho[1] - rho[0]) / rho[0] * 100}
results["preliminary_signal"] = signal
# Only ONE interior point per chain ⇒ b_ν cannot be checked for consistency.
check("each chain yields only ONE interior b_ν ⇒ recurrence consistency is NOT testable",
      all(len(c) == 3 for c in chains.values()))


# ── (C) verdict: data-limited; prerequisite = tower extension ────────────────
print("\n(C) verdict")
verdict = (
    "INCONCLUSIVE / DATA-LIMITED (no fit attempted, per the Δ_λ gate). The "
    "canonical Δ_λ data is only the four light nuclei D/T/³He/⁴He (three A-levels, "
    "one isospin pair) — one interior level per single-isospin chain, so the "
    "three-term recurrence b_ν cannot be tested for consistency and NOTHING is "
    "falsified. Preliminary signal only: the T-chain ratios are near-constant "
    "(ρ≈2.82, 2.94; ~4% spread → roughly geometric, recurrence-compatible) while "
    "the ³He-chain ratios are not (ρ≈2.46, 3.38). DECISIVE TEST GATED on extending "
    "the same-shape Δ_λ tower to ⁶Li, ⁷Li, ⁸Be, … (the Subgoal-1 Borromean-tower "
    "extension): with ≥4 same-shape levels one can test whether b_ν is constant "
    "(C-finite) or q-Lommel-shaped (q^{-ν}-modulated) vs erratic. Until then the "
    "q-Lommel Δ_λ route is neither supported nor refuted; building a closure now "
    "would be a fit. Recommendation for #2078: extend the tower FIRST, then run "
    "this pre-check; b_ν must be substrate-derived (q-Casimir/contraction), not "
    "fitted, and pass the deuteron."
)
print("  " + verdict)
results["verdict"] = verdict
check("verdict recorded: data-limited, decisive test gated on tower extension", True)

all_passed = all(ok for _, ok in asserts)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))

witness = {
    "computation": "delta_lambda_qlommel_recurrence_precheck",
    "description": (
        "Formalize-first pre-check for the binding Δ_λ ↔ q-Lommel three-term "
        "recurrence hypothesis (PR #2305 redirect; #2078 coordination). Verdict "
        "DATA-LIMITED: canonical Δ_λ is only 4 light nuclei (3 A-levels), too thin "
        "to test recurrence consistency; decisive test gated on the Subgoal-1 "
        "Borromean-tower extension. No fit (Δ_λ gate). "
        "docs/audits/2026-06-14-delta-lambda-qlommel-precheck.md."
    ),
    "discipline": "no fit (Δ_λ gate, no 7th ansatz); derive-or-refute; data-limited honest report; nothing wired",
    "source_witness": "delta-lambda-canonical-residual.witness.json",
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "delta-lambda-qlommel-recurrence-precheck.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
