# Door-iii FOLLOW-UP: twisted-combination + cross-term sinh/cosh C1²→GGM (2026-07-20)

**Bean:** `qou-vw3g` · **Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Status:** AUDIT — probe complete, **both options scope-(a) REFUTED**. No open
item declared; no conjecture status changed.

## 0. What this attacks

Door-iii ([`…doorIII-sinhcosh-bridge`](2026-07-20-qlift-doorIII-sinhcosh-bridge.md) +
[`…probe`](../../computations/probes/qlift_doorIII_sinhcosh_bridge_probe.py)) REFUTED
the naive **m-independent** linear combo of the C1 symmetric squares {f₊², f₊f₋, f₋²}
(+ bar copies) reproducing GGM eq-49: leading growth matched (sym² doubles C1's
slope-½ to slope-1 = GGM slope), the **sub-leading theta fine-structure** did not
(O(1) drift). This follow-up tests the two refined identifications the owner named.
C1: `[m+2]_q b_{m+2}=b_{m+1}+b_m` ({½,½}); GGM: `y_{m+1}=(2−q^m)y_m−y_{m−1}` ({−1,+1}).

## 1. The probe

[`qlift_doorIII_followup_twist_crossterm_probe.py`](../../computations/probes/qlift_doorIII_followup_twist_crossterm_probe.py)
(mpmath dps=60, q ∈ {0.9, 1.05, 1.10998}, m=0..50; fit m=0..14, extrapolate m=34..50;
kill `<1e-40` ⇒ LANDS, `O(1)` ⇒ REFUTED). A **twisted-target solver self-test**
recovers an in-span combo to ≤7.9e-56 at every q, so an O(1) residual is genuine.

- **OPTION 1 (twisted combination):** fit GGM to `q^{α·m}·{f₊²,f₊f₋,f₋²} +
  q^{−α·m}·{bar copies}` over a fixed-α grid α ∈ {−2,…,2}. A `q^{αm}` twist shifts
  only the sub-leading **linear-in-m** theta term, preserving the quadratic γ·m²
  slope — directly targeting Door-iii's fine-structure miss.
- **OPTION 2 (cross-term lead):** fit the 6-col basis, report which columns carry
  nonzero weight (is f₊f₋ essential?), plus the targeted 2-col `bar-even(f₊²) ± f₊f₋`
  fit and a no-cross control.

## 2. Verdict — REFUTED (both, scope-(a))

At **every** tested q, **every** target (forward y_a, y_b; recessive via Miller),
and **every** α in the grid, the tail residual is `1.0` for the forward legs and
`≥5.8e11` for the recessive leg (ill-conditioned) — under both options (Opt 1 twist,
Opt 2 6-col / targeted 2-col `bar-even(f₊²)±f₊f₋`). Neither refinement lands.

**Option 1:** the `q^{αm}` twist shifts the linear-in-m theta term but leaves the
**full sub-leading theta fine-structure** unreachable — one scalar twist is too
coarse for the theta oscillation Door-iii diagnosed. **Option 2:** f₊f₋ takes the
dominant fit weight (~0.95–1.0) — the solver *grabs* it — yet the fit still does not
extrapolate, so a nonzero cross-term weight is **not** evidence it is the connecting
datum (no-cross control is equally 1.0). Diagnostics show f₊f₋ sits at γ≈−0.53 = the
**same slope-1 class** as f₊², *not* the slope-0 datum the hypothesis posited.

**Scope-(a)** ("these constructions, alone, miss") — **not** (b): Door-i supplies the
module-level (b)-exclusion via isoclinicity; this measures the miss for these two.

## 3. Effect on the conjecture + recommendation

`conj:qdifference-kernel-prolongation-symbol` is **unchanged**. Both refined
non-module candidates fail, **reinforcing Door-i reading R1**: C1 is a distinct
object — its own Gevrey-½ module — from the colored-Jones/Stokes GGM carrier. The
naive combo (Door-iii), the twist, and the cross-term lead have now all missed; the
exact non-module identification is **closed-negative** for these classes.
**Recommendation:** upgrade Door-iii to a **scope-(b) Lean no-identity theorem** — a
proved invariant separating the two sub-leading theta fine-structures — retiring the
non-module carve-out for the sym²-of-C1 family.

## 4. Discipline

Scope-(a) vocabulary; pre-stated kill criterion + twisted-target solver self-test;
parameter-free; no AME data; the only "fit" is the m-independent linear-coefficient
solve (over a fixed-α grid) for the extrapolation kill-test. Corpus-grep: the whole
C1↔GGM trail is this branch's 2026-07-20 files; no closed item re-opened.
Witness: [`…followup…witness.json`](../../computations/probes/qlift_doorIII_followup_twist_crossterm_probe.witness.json).
