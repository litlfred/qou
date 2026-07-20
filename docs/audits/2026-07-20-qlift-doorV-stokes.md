# Door-v: the C1⊗C1 {+1,−1}→GGM residual is a diagonal ℤ/2 character, NOT a nontrivial unipotent Stokes automorphism (2026-07-20)

**Bean:** `qou-plnw` · **Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Status:** AUDIT — probe complete. **Nontrivial-unipotent-Stokes hypothesis
scope-(a) REFUTED**, with a **sharp positive characterization** of the residual.
No open item declared; no conjecture status changed.

## 0. What this attacks (positive-characterization step after Door-iv)

Door-iv ([`…doorIV-matrix`](2026-07-20-qlift-doorIV-matrix.md)) built `C1⊗C1` from
the carrier-lifted **growing** `f₊=[m]_q!·b_m` (~q^{+m²/4}) and forward **decaying**
`f₋=b` (~q^{−m²/4}); its `{+1,−1}` slopes (`f₊²`,`f₋²`) **contain** GGM's `{+1,−1}` —
first C1-construction with the right graded module — but the exact realization was
REFUTED (no low-degree rational gauge), the gap **localized** to sub-leading data
*within* the matching module. Door-v tests the positive reading: is that residual a
**STOKES AUTOMORPHISM** — a constant (m-independent on `gr`) **unipotent** factor
(RSZ Thm 5.5.7)? I.e. `GGM = (Stokes factor)·(TS-{+1,−1} realization)`.

## 1. The probe

[`qlift_doorV_stokes_automorphism_probe.py`](../../computations/probes/qlift_doorV_stokes_automorphism_probe.py)
(mpmath dps=70, q∈{0.9,1.05,1.10998}, m→60). Column-normalized value+shift
Casoratian frames: GGM `(y⁺ forward-dominant, y⁻ recessive-Miller)` vs TS
`(f₊², f₋²)` — normalization **strips the diagonal slope-scaling AND well-conditions**
the 2×2 inverse (raw cond ~q^{m²}~10⁷⁰ kills dps=70). `T_m = Ŷ^GGM (Ŷ^TS)⁻¹`.
**Decisive invariant test:** `R_m = T_m T_{m−1}⁻¹` off/diag → 0 ⟺ `T_m = D_m·U`,
`U` **constant** on `gr` (invariant to whatever sits in `D_m` — slope **or** a
`(−1)^m` character). **Positive control** = same-GGM-operator frame change
`(y_a,y⁻)` vs `(y_b,y⁻)` (a *genuine* constant matrix), calibrating the detector.
Pre-stated kill: `R` off/diag decays geom. (ratio<0.5) ⇒ `U` constant; `U`
off-diag → nonzero constant ⇒ **nontrivial Stokes LANDS**; `U`→I ⇒ trivial.

## 2. Result — three clean facts at the substrate (q=1.10998)

| quantity | CONTROL (same GGM op) | TEST (GGM vs TS-{+1,−1}) |
|---|---|---|
| `R` off/diag first→last | 2.6e−3 → 5.8e−4 | 1.16e−3 → 2.59e−4 |
| decay ratio (~q^{−m}) | **0.2235** | **0.2229** |
| `U[0,1],U[1,0]` last | −4.7e−3,−5.3e−3 (→0) | −2.1e−3,−2.4e−3 (→0) |
| diag sign oscillates | **False** | **True** |

Same at q=1.05. Reading:

1. **`U` IS constant.** `R` off/diag decays geometrically `~q^{−m}→0`,
   **identically** to the genuine-constant control (0.223 vs 0.224) — constant on
   `gr`; Door-iv's "sub-leading data" is *not m-chaotic*.
2. **The unipotent part is TRIVIAL.** `U[0,1],U[1,0]→0` (shrink ~q^{−m}), `U→I`:
   **no nontrivial Stokes jump** connects TS-{+1,−1} to GGM.
3. **The sole residual is a diagonal ℤ/2 `(−1)^m` character** — `diag_sign_osc`
   **True** for the test, **False** for the same-operator control. GGM's growing
   solution carries `y_{m+1}~−q^m y_m`; the all-positive squares `f₊²,f₋²`
   structurally **cannot** (a square is ≥0). Magnitudes/theta MATCH (off-diag→0,
   diag→unit); only the sign character separates them.

## 3. Verdict — REFUTED (scope-(a)) with sharp characterization

The Door-v **nontrivial-unipotent-Stokes hypothesis is REFUTED**: `U→I`. But the
residual is cleanly identified — a **constant diagonal ℤ/2 `(−1)^m` character** in
the *regular/torsion* part of the irregular type. That is a **formal-class (`gr`)
difference, NOT a Stokes (unipotent) datum**, so RSZ Thm 5.5.7 does not bridge
them: two anisoclinic `{+1,−1}` modules sharing slopes *and* theta magnitudes but
differing by a 2-torsion character sit in **different formal classes**. The
character mismatch has a **scope-(b) parity root** for *this* construction: a real
square is provably non-negative while GGM alternates sign (the same non-negativity
invariant as the KL-positivity prune) — the squares-based TS realization *cannot*
carry the sign, independent of any fit. (Module-level (b)-exclusion of C1 itself
is Door-i's; this is the narrower parity fact about the squares.)

## 4. Relation to the corpus A_ω / integer-3 (asked, answered)

**The integer-3 is NOT reproduced.** The `−3` Stokes constant
(`S⁰=[[1,0],[−3,1]]`, [`…g3-keystone`](2026-07-18-g3-stokes-keystone-evidence-base.md))
is GGM's **own** formal→actual jump; the TS→GGM comparison's unipotent part is
**trivial (0, not −3)**. The TS→GGM residual is instead the distinct **2-torsion
`(−1)^m` character** — a different class of datum (torsion vs the DT-integer Stokes).

## 5. Effect on the conjecture + recommendation

`conj:qdifference-kernel-prolongation-symbol` **unchanged**; reading **R1** (C1 /
its tensor square is a *distinct object* from the GGM/Stokes carrier) reinforced
and **sharpened**: after slopes match (Door-iv) and any diagonal factor is allowed,
the separation is a **single ℤ/2 character** and the Stokes bridge is **trivial**.
Any further C1→GGM attempt must break the parity wall (a sign-bearing, *not*
square-based, slope-{±1} construction) — not chase a Stokes matrix; there is none.

## 6. Discipline

scope-(a) vocabulary; pre-stated kill criterion; **positive control validates the
constancy detector** (same-operator ⇒ `R` off/diag→0, no character); the ℤ/2
residual is exact parity (squares ≥0), not a fit; no AME data. Corpus-grep: the
whole C1↔GGM trail is this branch's 2026-07-20 files; no closed item re-opened.
Witness:
[`…doorV…witness.json`](../../computations/probes/qlift_doorV_stokes_automorphism_probe.witness.json).
