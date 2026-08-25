# M1 adjudicated (GGM eq-(200) erratum), what the integer 3 actually is, and the Q3 negative (2026-08-11)

Three results from one session, in descending order of how much they change the
corpus's position. Sources: GGM 2012.00062v3, GGMW 2111.04763, Fantini–Wheeler
2410.20973 — all read from `library/` (no external lit was needed; every paper
was already in the repo).

---

## 1. M1 ADJUDICATED — the discrepancy is a typo in the paper, not in our compute

The M1 probe computed `S⁺₁₁(x;q)` from the q-Hahn Bessel holomorphic blocks
(GGM eq 127a/b) via the eq-(200) bilinear, and matched the printed coefficients
at `q⁰` and `q²` but not `q¹`. That is now settled by an **independent second
route**: the DGG flux-basis index table `I_{4₁}(0,e)(q)` (corpus-certified,
independently rebuilt by the LIT3 sweep) summed per eq (18),
`Ind^rot(0,x;q) = Σ_e I(0,e)(q)·x^e`:

| order | flux-basis index sum | block computation | printed eq (200) |
|---|---|---|---|
| `q⁰` | `1` | `1` | `1` ✅ |
| `q¹` | `−2 −2(x+x⁻¹) −1(x²+x⁻²)` | **same** | `−2 −1(x+x⁻¹) −2(x²+x⁻²)` ❌ |
| `q²` | `−3 −2(x+x⁻¹) −1(x²+x⁻²)` | **same** | same ✅ |

**Verdict: the printed `q¹` coefficient of GGM eq (200) is an erratum.** Two
independent computations — one from the block definitions, one from the flux-basis
index — agree with each other and disagree with the printed line, while agreeing
with it at every other order. Both readings sum to `−8` at `x = 1`, which is why
the eq-(61) tower `[1,−8,−9]` never revealed the problem; only the two-variable
check did. Corrected coefficient:

```
q¹ :  −(x⁻² + 2x⁻¹ + 2 + 2x + x²)      [printed: −(2x⁻² + x⁻¹ + 2 + x + 2x²)]
```

Provenance was checked at **span level** (font-size 8 = superscript) so this is
not a text-extraction artifact: both the block arguments and the printed
coefficient are as read. **So M1 is confirmed** — the eq-(21) dictionary target is
verified in-corpus as a two-variable identity, modulo this single erratum.
Worth reporting upstream.

---

## 2. 🔴 CORRECTION to the corpus — `A_ω = 3` is NOT "a 3d-index coefficient"

The corpus has been treating the exact dictionary (GGM Conjecture 4, eq 21) as if
it licensed calling the integer `3` a 3d-index/DT coefficient. It does not:

* Eq (21), `S⁺_{σ₁σ₁}(x;q) = Ind^rot_K(0,x;q)`, is **diagonal-only** and is the
  entry whose `q⁰` term is **1**, not 3 (its series is `1 − 8q − 9q² + …`).
* The **`3` lives in the off-diagonal `(σ₁,σ₂)` entry**, which eq (21) does not
  cover — only the weaker eq (20) statement *up to* `GL(r, ℤ(x,q))` touches it.

So the repo's `A_ω = 3` and its per-winding `I(0,e)` table describe **two
different matrix entries**. The honest statement is: *3 is the off-diagonal
Stokes constant at the singularity `ι₁,₂ = Vol(4₁)/π`, conjecturally (Conj 3(d),
no category named) a DT/BPS degeneracy.* Any corpus text asserting the stronger
reading should be corrected.

Two further facts that constrain every "explain the 3" attempt:

* **The 3 is not atomic and not 4₁-specific.** GGM eq (188):
  `S⁺(x;0) = [[1, x⁻¹+1+x],[0,1]]` — so `3 = s(1)` for `s(x) = x+1+x⁻¹`, a count
  of three unit-multiplicity states graded by meridian charge `e ∈ {−1,0,+1}`.
  The **same** `s(x)` appears for `5₂` (eqs 239/277/307), where the eq-(98)
  spectrum is `s(1)=3` and `s(1)+1=4`. Any story that explains `3` as a
  `4₁`-invariant is already refuted by `5₂` carrying the identical polynomial.
* **The 3 has a tower.** It is the first of `3, 9, 75, 642, 5580, 48558, …`
  (eq 62). An explanation of `3` alone that says nothing about the tower is not
  an explanation.

**There is exactly one genuine derivation of the 3 in the literature:**
Fantini–Wheeler 2410.20973 eqs (66)–(71) derive `S_{I,II} = [[1,0],[−3,1]]` by
explicit thimble decomposition plus the quantum-dilogarithm quasi-periodicity
relation, giving `3 = 2 + 1` (two copies of `I₀,₀` from the two thimble
decompositions, plus one from collapsing the descendant pair `I₋₁ + I₊₁ = I₀,₀`).
It is rigorous — and it is a re-derivation *inside* resurgence, not an
outside-in confirmation. Every external candidate fails:
`#flat connections` (3 for 4₁ but 4 for 5₂, which nevertheless shows both 3 and 4),
trace field `ℚ(√−3)` (already refuted here; 5₂'s field is the disc-−23 cubic and
still carries a 3), Alexander middle coefficient (3 for both, but the outer
coefficients differ while `s(x)` does not), A-polynomial / spectral networks
(explicitly flagged **open** by GGM themselves), knots–quivers (trefoil only;
4₁ is not a positive braid knot), GPPV `Ẑ` (4₁ does not appear).

---

## 3. Q3 — NO PRECEDENT connecting Stokes/DT data to decay observables

The question the corpus most needs answered, asked adversarially and answered
flatly. A sweep of all **329 papers in `library/`** (324 text-extractable),
cross-tabulating resurgence/DT/BPS vocabulary against particle-observable
vocabulary (decay width, branching ratio, half-life, muon, beta decay, Q-value,
CODATA, PDG, MeV), plus independent web search:

* **7 papers matched both; all 7 are false positives.** Every "Q-value" hit is
  the string "**ℚ-valued**". The only "Donaldson" in the CODATA review is
  *Petley & Donaldson (1984), Metrologia* — a thermometry reference.
* The one corpus paper proposing "fermions as hyperbolic knot complements"
  (Asselmeyer-Maluga 1910.09966, `physics.gen-ph`) contains **no mass ratio, no
  decay width, no lifetime, and no Stokes constant**.
* The nearest genuine relative — renormalon/Borel analyses of the hadronic τ
  decay width — involves renormalons of a 4d gauge theory: **no 3-manifold, no
  DT invariant, no knot**. Shared vocabulary, different object. Not a precedent.

**Verdict: NO PRECEDENT. The proposed identification is unsupported by any
literature.** Nobody has connected resurgent Stokes data or DT invariants of a
knot complement to a decay width, lifetime, branching ratio, mass, or mass ratio.

**And there is a structural obstruction, not merely an absence.** The Stokes
constants of `4₁` are **integers** — `3, 9, 75, 642, 5580, …` — integrality being
the entire content of the DT/BPS conjecture. The corpus's targets
`S(muon) = +0.00968298` and `S(proton) = −0.03945936` are small, non-integer,
**opposite-signed** reals. Any bridge would have to explain (i) why the same
`x+1+x⁻¹` appears for `5₂`, (ii) why the co-occurring `4` and the tower
`9, 75, 642` do not also surface as observables, and (iii) the sign asymmetry.
None of these has been addressed anywhere in the corpus.

**Recommendation.** This is the load-bearing gap, and it is now precisely stated
rather than merely suspected. Before further work is invested in the `A_ω`
periphery, the programme should either (a) produce a mechanism mapping an integer
Stokes constant to a small signed real residual, or (b) record that the
`A_ω → S` identification is a conjecture with no literature support and scope the
downstream claims accordingly. Continuing to elaborate the periphery without
addressing this is the failure mode the corpus's own anti-laundering rules exist
to prevent.
