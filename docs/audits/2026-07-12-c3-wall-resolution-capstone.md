# The c₃ bar-odd `S` "wall": resolution capstone

**Date:** 2026-07-12 · **Branch:** `claude/c3-wall-capstone-normalization-oddchannel-2026-07-12` ·
**Consolidates:** merged PRs #3600, #3636, #3654 (this session). **Tier:** capstone
+ bridge (scope-(a); C14; no `c_k` wired; no fit; `conj:im-q-physical-role` stays a conjecture).

For four sessions the c₃ bar-odd part `S = c₃ + Vol(4₁)` (`S(muon)=+0.00968`,
`S(proton)=−0.03946`) was treated as a **near-singular substrate→u map** — the
"wall" — whose `dc₃/dq ≈ 4.66×10⁶` hypersensitivity and sign-flip demanded the
deformed-complex volume conjecture to close. This session resolved it: **the wall
is a `1/u³` representation artifact over smooth geometry.** There was no
singularity to break.

## The five results (each merged this session)

1. **`S` is the decay projection `Im(q)`** — `conj:im-q-physical-role`
   candidate (iii). The c₃ bar-odd `S = Q_β/E₀` is the decay-width observable
   that conjecture predicted. A non-fitting inversion gives a small, sign-flipped
   required `ε = Im(q)` (μ +1.3%, p −5.5%). [#3600]

2. **The sign-flip is STRUCTURAL, not a fit** — bar-odd parity. `S` is bar-odd
   under `σ:q↦q⁻¹`; with `q=q₀+iε`, `S(−ε)=−S(ε)`, so `sign S = sign ε`. No real
   `q₀` can produce the flip. Lean-proved sorry-free (`fig8Trace_im_odd`,
   `fig8Trace_im_real_zero`). [#3636]

3. **The hypersensitivity is a `1/u³` ladder artifact, not a singularity.** The
   c₃ extractor is `c₃=(Q_β/Q_{N2}−1)/u³`, `u=b·ℏ_q²≈0.0085`. The S=0 point `q*`
   root-found; `S'(q*)=3.84×10⁶ = 2.37 × (1/u³)`, a smooth `O(1)` prefactor over
   the tiny `u³`. The famous `dc₃/dq` swing is the ladder inversion magnifying a
   **smooth** numerator zero. The real precision limit is the experimental `Q_β`
   (`dq*/dQ_β≈−0.54`), not the anchor count. [#3636]

4. **`q*` is a third, decay-sector determination of `q₀`.** `q*` (ε=0, pure
   bar-even) is not the muon or proton mass pin, and not their precision-weighted
   reconciliation (`~0%` muon-ward; `q*` is `80.3%`). The μ-p substrate tension
   becomes a **μ-p-`Q_β` three-way** picture. [#3636]

5. **The Φ_b state integral CONFIRMS no physical singular map.** The saddle
   `𝔙(m)` (validated gluing solver, Vol(4₁) to 4e-18) at the real substrate
   meridian `m=q₀` gives `Im 𝔙 = 0` exactly (amphichirality) and a volume deficit
   `0.0094 ≈ |S(muon)|`; the finite-b correction adds `i·t·κ₁ = 0.058`
   (`2πb²=i·t` imaginary, `κ₁=11√3π/108`). Both **smooth + anchor-blind**. The
   state integral supplies the `S` scale from two geometric handles, no fit, but
   no anchor-dependence — so the sign-flip is representational, per result 3. [#3654]

## The unifying picture

The bar-odd `S` decomposes on the corpus's ladder as `S = h·D(u)` with `h=q−1/q`
the anchor-blind bar-odd carrier and `D(u)` a bar-even ℚ(√3) ladder function
(`qbeta_even_channel_bar_split`). The bridge:

- **Physics (smooth):** the state-integral `𝔙` is smooth; `Im 𝔙` / the volume
  deficit / `i·t·κ₁` all sit at the `|S|` scale `~0.01–0.06`; `Im 𝔙 = 0` at real
  substrate. The **decay-sector `q*`** is where this smooth object crosses zero.
- **Representation (the swing):** `c₃ = (…)/u³` re-expresses the smooth object;
  the `1/u³` magnifies its tiny anchor-dependence into the `±` sign-flip. The
  swing lives in `D(u)`, not in the geometry.

**So the "wall" was never physical.** Closing `S` to research precision needs
either a sharper neutron `Q_β` (which directly sharpens `q*`, result 3) or the
exact `D(u)` ladder function (the corpus's even/odd-channel program) — not a
singular-map derivation. The `conj:im-q-physical-role` candidate (iii) is
realized (`S` is the decay `Im(q)`); it remains a conjecture pending the exact
normalization.

## What NOT to re-chase (anti-duplication record)

Future agents: the c₃ `S` hypersensitivity is **not** evidence of a near-singular
`q₀→m` map, a phase near a quadrant boundary, or a magnitude singularity — those
framings are re-scoped (see #3636 audit). It is the `1/u³` ladder representation
of a smooth zero. Do not re-open the "singular wall" search.

## Cross-references
- #3600: `rem:figure-eight-reeb-theta-value`, `rem:c3-s-imq-decay-projection`, `conj:im-q-physical-role` candidate (iii).
- #3636: [`2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md`](2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md); `ImQDecayLinearResponse.lean`.
- #3654: `qbeta_c3_phib_finite_b_volume_correction_probe.py`, `qbeta_c3_phib_saddle_state_integral_probe.py`.
- Ladder decomposition: `qbeta_even_channel_bar_split_probe.py` (`S=h·D(u)`, D∈ℚ(√3)).
- Φ_b state-integral infra: #3596.
