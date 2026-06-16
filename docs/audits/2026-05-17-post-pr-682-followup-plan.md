# Post-#682 follow-up plan: chi-cache extension, Habiro, chirality

> **Status (2026-05-17, this branch):** #682 ships the
> `Σ_λ y_λ(q_0) · χ^λ` combiner + 3-way 1ppb cross-check + Li_2^q
> production wiring. Three follow-ups remain compute-bound or
> governance-blocked.

## 1. Chi-cache completion for T / ³He / ⁴He (compute-bound)

**Current coverage** (`canonical-tr-m-via-chi-cache.witness.json`):

| Atom | $H_n$ | Coverage | Status |
|---|---|---|---|
| proton | 3 | 3/3 ✓ | complete |
| neutron | 3 | 3/3 ✓ | complete |
| deuteron | 6 | 11/11 ✓ | complete |
| tritium | 9 | 2/30 → up to ~6/30 (in-flight bg compute) | partial |
| ³He | 9 | 3/30 | partial |
| ⁴He | 12 | 0/77 | empty |

**To finish:**

```bash
# Tritium / ³He — each takes ~ minutes/partition × ~30 partitions
# under 4 workers → 1-2 hr per atom of clock time.
python3 computations/per_irrep_pole_atom.py tritium --workers $(nproc)
python3 computations/per_irrep_pole_atom.py helium-3 --workers $(nproc)

# ⁴He — H_12, 77 partitions, minutes-per-partition symbolic — hours of compute.
# May want a Rust accelerator (see #681 Q5).
python3 computations/per_irrep_pole_atom.py helium-4 --workers $(nproc)
```

The script supports **incremental saves** — each completed partition
is appended to `chi-{atom}-h{n}.witness.json` and the JSON is
rewritten, so a SIGTERM/timeout mid-loop preserves work done so far.
Re-running picks up where the previous attempt left off.

**Outcome when complete:** the 3-way 1ppb cross-check
(`cross_check_trM_1ppb.py`) covers all five common atoms with the
chi-cache path, not just p/n/D.

## 2. Habiro coefficient extension to T / ³He / ⁴He (Phase γ)

**Source script:** `computations/habiro/habiro_coefficients_atomic.py`

**Current coverage:** `habiro-coefficients-atomic.witness.json` covers
A ∈ {1, 1, 2} (p, n, D); A ∈ {3, 3, 4} (T, ³He, ⁴He) are missing.

**Effort:** O(several hours per atom) under the existing symbolic
Habiro engine. Independent compute; standalone witness; no new math
required.

**Unlocks:** `path_b_habiro_mass_probe.py` for the T/³He/⁴He atoms,
giving Path-3 (Habiro-tower) mass predictions alongside Path-2
(per-partition-k); side-by-side closure analysis becomes possible.

## 3. m_p Item B — chirality T5 (governance-blocked)

**Audit witness:** [`term5-aK-audit.witness.json`](../../computations/audits/term5-aK-audit.witness.json)
covers V1/V2/V3/V4 for {p, n} and **V1 only** for {D, T, ³He}.

**Audit script:** [`term5_aK_audit.py`](../../computations/audits/term5_aK_audit.py)
takes `--variants V1,V2,V3,V4` and `--atoms`. The script's own
docstring notes:

> "V2 alone takes >34 min for deuteron in this implementation."

So V2/V3/V4 for D/T/³He is **compute-bound** rather than
governance-blocked — running the audit at the full Cartesian product
is days of compute (12 cells × 30+ min each).

**Governance question (per audit):** which Hecke mirror convention
(V1, V2, V3, V4) is the canonical one? The four definitions differ
in how the σ_i ↔ σ_i^{-1} mirror is taken across averaged crossings;
no closed-form answer is yet known. The 2.2% gap between V1
chirality and the canonical Markov-paired chirality
(`a_K · C_K = τ(β · β*^-1)` per `prop:chirality-dual-space-derivation`)
is real and persists across atoms.

**Concrete next probe (no governance decision needed):** run
the V2 audit for deuteron only (~30 min). Sample-of-one is enough
to test whether the 2.2% gap holds across the V1 → V2 mirror
re-interpretation, or whether one of the other variants closes it.

```bash
python3 computations/audits/term5_aK_audit.py \
    --atoms deuteron --variants V2
```

## Priority order for the follow-up PR

1. **Tritium chi-cache completion** (1-2 hr, mechanical, extends 1ppb gate)
2. **³He chi-cache completion** (1-2 hr, mechanical, extends 1ppb gate)
3. **V2 chirality probe at deuteron** (~30 min, governance-informative)
4. **Habiro coefficient extension** (multi-hour per atom, opens Path-3)
5. **⁴He chi-cache** (multi-hour, requires Rust accelerator for tractability)

Each is independent and can ship as a separate witness-refresh PR.

## Related blocks

- [`rem:knot-fusion-step1-audit`](2026-05-17-knot-fusion-step1-audit.md) — the audit that surfaced Step 2 (closed by #682)
- [`conj:alpha-k-categorical-closure`](../../content/quantum-observable-universe/braids-and-knots/alpha-k-categorical-closure.md) — open closure question (PR #675)
- [`prop:chi-lambda-w0-sign-weighting`](../../content/quantum-observable-universe/braids-and-knots/chi-lambda-w0-sign-weighting.md) — (1, 0, -1) sign-character (PR #675)
- [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) — Li_2^q tower form, now wired
