# α_EM correspondence attack, brick 4 — the σ↦J map's geometric carrier on Bring

**Date:** 2026-07-18 · **Axis:** the `1/π` correspondence wall (post-#3933) ·
**Tier:** symbolic-exact geometry (on-curve check, projective multipliers, Riemann–Hurwitz) ·
**Derives no clause; no fit; nothing wired; `1/(8π)` stays phase-4.**

Probe [`alpha_em_sigmaJ_geometric_carrier_probe.py`](../../computations/alpha_em/alpha_em_sigmaJ_geometric_carrier_probe.py)
→ [witness](../../computations/alpha_em/alpha-em-sigmaJ-geometric-carrier.witness.json) (4/4).

## Context

Merged #3933 constructed the σ↦J map at the degenerate locus: `σ_ss(q=±i)=±i`, type-correct
(`σ_ss²=−1`) and bar/conjugation-equivariant. This brick shows the map's target is not
abstract — **the Bring surface itself carries it**, via the (2,4,5) triangle group's
order-4 element (source geometry: Braden–Disney-Hogg, `library/arxiv-2208.13692v1/2208.13692v1.pdf`,
Prop 3.9 + §4.3 + Prop 4.6).

## Findings (all exact)

- **(G1)** `V=[1:i:−1:−i:0]` **lies on Bring** (`H₁=H₂=H₃=0` exactly) — the vertex
  coordinates are the 4th roots of unity; Bring's 30 vertices are its permutations.
- **(G2)** The order-4 rotation fixes `V` **with multiplier exactly `i`** (`U·V = i·V`).
  At a holomorphic fixed point the differential acts on the tangent line by the
  multiplier, and multiplication by `i` on the holomorphic tangent line **is** `J`:
  `dU|_V = i = J|_V`. **The (2,4,5) order-4 rotation realizes J by an automorphism, with
  multiplier = the democratic `q=i`.**
- **(G3)** `conj(V)=[1:−i:−1:i:0]` is fixed **with multiplier `−i`**: complex conjugation
  swaps the `(+i)`- and `(−i)`-multiplier vertex families — exactly as bar exchanges the
  degenerate points `q=±i` (#3933 B3) and as conjugation exchanges `spec(J)`.
- **(G4)** Riemann–Hurwitz with the two multiplier-`±i` vertices ramified (index 4) gives
  `genus(B/⟨U⟩)=1` — the elliptic quotient, which per the paper (§4.3, Weber's `T`) has
  `j=−25/2=j(5τ₀)`: **the same `E_{5τ₀}` appearing with multiplicity 3 in
  `Jac(Bring)≅E_{5τ₀}³×E_{τ₀}`**. The democratic/order-4 structure quotients onto the
  dominant Jacobian factor.

## Net

The τ target of the degenerate braiding is now **concrete**: `σ_ss(q=±i)=±i ↦ dU` at the
vertex pair `{V, conj(V)}` — same values, same involution equivariance, realized by an
actual automorphism of the actual surface, with the quotient landing on the
paper-confirmed `E_{5τ₀}`. **Remaining wall (unchanged):** the functorial statement
`τ(braiding) = this automorphism action`; its classical limit would inherit the conformal
structure `J` defines — and hence the heat-kernel unit `a₀` (Clause A).

## Lean formalization (same PR) + reconciliation with the τ-obstruction (`a6d522e0a`)

**Lean (sorry-free, `lean`-direct exit 0, core-only):**
[`QOU/Archimedean/SigmaJGeometricCarrier.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SigmaJGeometricCarrier.lean)
— models `ℤ[i]` as `Int` pairs (no Mathlib) and machine-verifies G1–G3 plus the brick-3
role-swap: `H₁=H₂=H₃=0` at `V`; `U·V=i·V`; `U·conj(V)=−i·conj(V)`; conjugation swaps the
families; `i²=−1`; bar exchanges `{±i}` while the transpose fixes them. Registered in
`QOU.lean`.

**Reconciliation.** The same-day sibling τ-correspondence probe (`a6d522e0a`, merged)
found the *obstruction*: through the nome, the channel-swap `q↦−q⁻¹` is a **holomorphic**
modular involution (`τ↦½−τ`) while Hodge conjugation is **anti-holomorphic** (`τ↦−τ̄`) —
so a holomorphic τ-functor cannot identify them directly, and "the anti-holomorphic
ingredient must enter through the fibre." **The brick-3/4 role-swap is exactly that
ingredient, now with its geometric carrier:** on the degenerate stratum the conjugation
doubling is carried by **bar = parameter conjugation** (anti-holomorphic; on `|q|=1`,
`q⁻¹=q̄`), which exchanges the degenerate pair `{±i}` — and its geometric realization is
coordinate conjugation exchanging the two vertex families (G3, Lean-verified). So the
obstruction and this brick compose rather than conflict: *holomorphic transpose swaps the
channels at generic q; anti-holomorphic bar/conjugation swaps the degenerate points and
the vertex families* — the two-strata structure is the resolution shape the obstruction
audit called for.

## Scope guard (STRICT)

Exact geometry only; derives **no** clause; no fit; nothing wired. Builds on merged #3933 +
the uploaded Braden–Disney-Hogg PDF; duplicates neither.

## Cross-references

- Bricks 1–3: `2026-07-18-alpha-em-conjugation-doubling-dictionary.md` (merged #3933)
- The conjecture + wall: `2026-07-18-alpha-em-perloop-conjecture-statement.md` (merged #3921)
- Vertices / quotients / Jacobian: Braden–Disney-Hogg arXiv:2208.13692 (Prop 3.9, §4.3, Prop 4.6)
